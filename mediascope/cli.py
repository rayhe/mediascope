"""
MediaScope CLI — Main entry point for media bias analysis toolkit.

Usage:
    mediascope <command> [options]

Commands:
    ingest              Fetch and store articles from publication RSS feeds
    analyze             Run entity detection, sentiment, and framing analysis
    score               Calculate asymmetry scores with statistical tests
    report              Generate weekly/monthly bias reports
    disclose            Generate conflict-of-interest disclosure statements
    add-publication     Create a new publication profile from template
    list-publications   Show all configured publication profiles
    status              Show database statistics
"""

import os
import sys
import json
import shutil
from datetime import datetime, date
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

from mediascope.config import load_config, get_profiles_dir, get_db_path
from mediascope.profiles import load_profile, load_all_profiles, validate_profile
from mediascope.ingest import ArticleIngester
from mediascope.analysis import ArticleAnalyzer
from mediascope.scoring import AsymmetryScorer
from mediascope.reports import ReportGenerator
from mediascope.disclosure import DisclosureGenerator
from mediascope.db import MediaScopeDB

console = Console()


def _resolve_profile(slug: str):
    """Load and validate a publication profile by slug."""
    try:
        profile = load_profile(slug)
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] No profile found for '{slug}'")
        console.print(f"Run [cyan]mediascope list-publications[/cyan] to see available profiles.")
        raise SystemExit(1)

    errors = validate_profile(profile)
    if errors:
        console.print(f"[yellow]Warning:[/yellow] Profile '{slug}' has validation issues:")
        for err in errors:
            console.print(f"  • {err}")

    return profile


def _get_db():
    """Open and return the database connection."""
    db_path = get_db_path()
    try:
        return MediaScopeDB(db_path)
    except Exception as e:
        console.print(f"[red]Error:[/red] Could not open database at {db_path}: {e}")
        raise SystemExit(1)


@click.group(
    help="MediaScope — Systematic media bias analysis toolkit.\n\n"
         "Quantifies asymmetric coverage patterns by tracking sentiment, framing, "
         "and sourcing across publications and comparing treatment of different entities."
)
@click.version_option(version="0.1.0", prog_name="mediascope")
def cli():
    """MediaScope CLI root group."""
    pass


# ---------------------------------------------------------------------------
# ingest
# ---------------------------------------------------------------------------

@cli.command()
@click.option(
    "--publication", "-p",
    required=True,
    help="Publication slug (e.g. 'wired', 'nytimes').",
)
@click.option(
    "--since",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=None,
    help="Only ingest articles published on or after this date (YYYY-MM-DD).",
)
@click.option(
    "--until",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=None,
    help="Only ingest articles published on or before this date (YYYY-MM-DD).",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Show what would be ingested without writing to the database.",
)
def ingest(publication, since, until, dry_run):
    """Fetch articles from RSS feeds and store them in the database.

    Parses each configured RSS feed for the publication, scrapes full article
    text when possible, deduplicates against existing records, and stores
    new articles with metadata.
    """
    profile = _resolve_profile(publication)
    db = _get_db()

    feeds = profile.get("rss_feeds", [])
    if not feeds:
        console.print(f"[red]Error:[/red] No RSS feeds configured for '{publication}'.")
        raise SystemExit(1)

    console.print(
        Panel(
            f"[bold]{profile['name']}[/bold]\n"
            f"Feeds: {len(feeds)}  •  "
            f"Since: {since.strftime('%Y-%m-%d') if since else 'all'}  •  "
            f"Until: {until.strftime('%Y-%m-%d') if until else 'now'}",
            title="Ingesting",
            border_style="cyan",
        )
    )

    ingester = ArticleIngester(db=db, profile=profile)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        total_new = 0
        total_skipped = 0

        for feed in feeds:
            task = progress.add_task(
                f"Fetching [cyan]{feed['category']}[/cyan] feed…", total=None
            )
            try:
                result = ingester.ingest_feed(
                    feed_url=feed["url"],
                    category=feed.get("category", "uncategorized"),
                    since=since,
                    until=until,
                    dry_run=dry_run,
                )
                total_new += result.get("new", 0)
                total_skipped += result.get("skipped", 0)
                progress.update(
                    task,
                    description=(
                        f"[cyan]{feed['category']}[/cyan]: "
                        f"{result.get('new', 0)} new, {result.get('skipped', 0)} skipped"
                    ),
                    completed=True,
                )
            except Exception as e:
                progress.update(
                    task,
                    description=f"[red]{feed['category']}: {e}[/red]",
                    completed=True,
                )

    label = "Dry-run complete" if dry_run else "Ingest complete"
    console.print(
        f"\n[green]{label}:[/green] {total_new} new articles, "
        f"{total_skipped} duplicates skipped."
    )


# ---------------------------------------------------------------------------
# analyze
# ---------------------------------------------------------------------------

@cli.command()
@click.option(
    "--publication", "-p",
    required=True,
    help="Publication slug.",
)
@click.option(
    "--target", "-t",
    required=True,
    help="Target entity to analyse (e.g. 'Meta', 'Google').",
)
@click.option(
    "--since",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=None,
    help="Analyse articles from this date onward (YYYY-MM-DD).",
)
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="Re-analyse articles even if results already exist.",
)
def analyze(publication, target, since, force):
    """Run NLP analysis on ingested articles.

    For each article mentioning the target entity, performs:

    \b
    • Entity detection and co-occurrence mapping
    • 8-dimension sentiment scoring (tone, emotional intensity, agency, etc.)
    • Framing device detection (39 types: loaded language, CEO personalization, etc.)
    • Source extraction with stance analysis (adversarial / supportive / neutral)
    • Outsourced intensity measurement (editorial prose vs. quoted intensity)
    • Headline vs. body sentiment comparison with framing-aware correction
    """
    profile = _resolve_profile(publication)
    db = _get_db()

    entity_config = profile.get("target_entities", {}).get(target)
    if entity_config is None:
        console.print(
            f"[red]Error:[/red] Entity '{target}' is not configured in the "
            f"'{publication}' profile."
        )
        available = list(profile.get("target_entities", {}).keys())
        if available:
            console.print(f"Available entities: {', '.join(available)}")
        raise SystemExit(1)

    console.print(
        Panel(
            f"[bold]{profile['name']}[/bold] → entity [bold cyan]{target}[/bold cyan]\n"
            f"Since: {since.strftime('%Y-%m-%d') if since else 'all stored articles'}  •  "
            f"Force re-analyse: {'yes' if force else 'no'}",
            title="Analysing",
            border_style="green",
        )
    )

    analyzer = ArticleAnalyzer(db=db, profile=profile)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Loading articles…", total=None)

        articles = db.get_articles(
            publication=publication,
            since=since,
            entity_mention=target,
        )

        progress.update(
            task,
            description=f"Found {len(articles)} articles mentioning '{target}'.",
        )

        if not articles:
            console.print("[yellow]No matching articles found.[/yellow]")
            return

        analysed = 0
        skipped = 0

        for article in articles:
            if not force and db.has_analysis(article["id"], target):
                skipped += 1
                continue

            progress.update(
                task,
                description=f"Analysing ({analysed + skipped + 1}/{len(articles)}): "
                            f"[dim]{article.get('title', '')[:60]}…[/dim]",
            )
            try:
                analyzer.analyze_article(article, target_entity=target, entity_config=entity_config)
                analysed += 1
            except Exception as e:
                console.print(f"  [red]Error on article {article['id']}:[/red] {e}")

    console.print(
        f"\n[green]Analysis complete:[/green] {analysed} analysed, {skipped} already done."
    )


# ---------------------------------------------------------------------------
# score
# ---------------------------------------------------------------------------

@cli.command()
@click.option(
    "--publication", "-p",
    required=True,
    help="Publication slug.",
)
@click.option(
    "--target", "-t",
    required=True,
    help="Target entity (e.g. 'Meta').",
)
@click.option(
    "--period",
    type=click.Choice(["weekly", "monthly"], case_sensitive=False),
    default="weekly",
    help="Scoring period granularity.",
)
@click.option(
    "--compare",
    multiple=True,
    help="Additional entities to compare against (repeatable).",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Write JSON scores to this file (default: stdout).",
)
def score(publication, target, period, compare, output):
    """Calculate coverage asymmetry scores.

    Computes the Asymmetry Score (AS) by comparing how the publication treats
    the target entity vs. peers.  Statistical tests include:

    \b
    • Welch's t-test for sentiment differential (unequal variance)
    • Cohen's d effect size (practical significance)
    • Bootstrap confidence intervals (1,000 resamples, 95% CI)
    • Framing device density comparison
    • Source stance balance analysis
    """
    profile = _resolve_profile(publication)
    db = _get_db()

    scorer = AsymmetryScorer(db=db, profile=profile)

    comparators = list(compare) if compare else None

    console.print(
        Panel(
            f"[bold]{profile['name']}[/bold] → [bold cyan]{target}[/bold cyan]\n"
            f"Period: {period}  •  "
            f"Comparators: {', '.join(comparators) if comparators else 'auto-detect'}",
            title="Scoring",
            border_style="magenta",
        )
    )

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Computing asymmetry scores…", total=None)
        scores = scorer.compute(
            target=target,
            period=period,
            comparators=comparators,
        )
        progress.update(task, description="Done.", completed=True)

    # Render results
    if output:
        Path(output).write_text(json.dumps(scores, indent=2, default=str))
        console.print(f"[green]Scores written to {output}[/green]")
    else:
        _render_scores(scores, target, publication, period)


def _render_scores(scores: dict, target: str, publication: str, period: str):
    """Pretty-print scoring results to the console."""
    table = Table(
        title=f"Asymmetry Scores: {publication} → {target} ({period})",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")
    table.add_column("p-value", justify="right")
    table.add_column("Interpretation")

    for metric in scores.get("metrics", []):
        p = metric.get("p_value")
        p_str = f"{p:.4f}" if p is not None else "—"
        interp = metric.get("interpretation", "")
        table.add_row(
            metric.get("name", ""),
            f"{metric.get('value', 0):.3f}",
            p_str,
            interp,
        )

    console.print(table)

    aci = scores.get("aci") or scores.get("asymmetry_score")
    if aci is not None:
        color = "red" if aci > 0.6 else ("yellow" if aci > 0.3 else "green")
        console.print(
            f"\n  Asymmetry Score (AS): [{color}]{aci:.3f}[/{color}]"
        )


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

@cli.command()
@click.option(
    "--publication", "-p",
    required=True,
    help="Publication slug.",
)
@click.option(
    "--target", "-t",
    required=True,
    help="Target entity.",
)
@click.option(
    "--format", "fmt",
    type=click.Choice(["md", "html", "json"], case_sensitive=False),
    default="md",
    help="Output format.",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file path (default: auto-generated name).",
)
@click.option(
    "--period",
    type=click.Choice(["weekly", "monthly"], case_sensitive=False),
    default="weekly",
    help="Report period.",
)
def report(publication, target, fmt, output, period):
    """Generate a bias analysis report.

    Produces a structured report containing:

    \b
    • Executive summary with key findings
    • Sentiment distribution charts (Markdown tables or HTML)
    • Framing analysis breakdown
    • Conflict-of-interest context from the publication profile
    • Statistical significance indicators
    • Notable article examples (most positive, most negative)
    • Comparison to baseline publications
    """
    profile = _resolve_profile(publication)
    db = _get_db()

    generator = ReportGenerator(db=db, profile=profile)

    console.print(
        Panel(
            f"[bold]{profile['name']}[/bold] → [bold cyan]{target}[/bold cyan]\n"
            f"Format: {fmt}  •  Period: {period}",
            title="Generating Report",
            border_style="blue",
        )
    )

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Building report…", total=None)
        report_content = generator.generate(
            target=target,
            format=fmt,
            period=period,
        )
        progress.update(task, description="Done.", completed=True)

    if output is None:
        timestamp = datetime.now().strftime("%Y%m%d")
        ext = fmt if fmt != "md" else "md"
        output = f"reports/{publication}_{target}_{period}_{timestamp}.{ext}"

    out_path = Path(output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report_content)

    console.print(f"\n[green]Report saved to {output}[/green]")


# ---------------------------------------------------------------------------
# disclose
# ---------------------------------------------------------------------------

@cli.command()
@click.option(
    "--publication", "-p",
    required=True,
    help="Publication slug.",
)
@click.option(
    "--target", "-t",
    required=True,
    help="Target entity.",
)
@click.option(
    "--article-url",
    default=None,
    help="Specific article URL for contextual disclosure.",
)
@click.option(
    "--format", "fmt",
    type=click.Choice(["full", "social", "json"], case_sensitive=False),
    default="full",
    help="Output format: full (detailed), social (brief), json (structured).",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Write to file instead of stdout.",
)
def disclose(publication, target, article_url, fmt, output):
    """Generate a conflict-of-interest disclosure statement.

    Pulls ownership chain, revenue relationships, litigation connections,
    and known conflicts from the publication profile to produce a
    disclosure readers can use to evaluate coverage.

    \b
    Formats:
      full   — Multi-paragraph disclosure with evidence links
      social — Tweet/post-length summary (~280 chars)
      json   — Structured data for programmatic use
    """
    profile = _resolve_profile(publication)

    generator = DisclosureGenerator(profile=profile)

    disclosure = generator.generate(
        target=target,
        article_url=article_url,
        format=fmt,
    )

    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(disclosure)
        console.print(f"[green]Disclosure saved to {output}[/green]")
    else:
        console.print()
        console.print(disclosure)
        console.print()


# ---------------------------------------------------------------------------
# add-publication
# ---------------------------------------------------------------------------

@cli.command("add-publication")
@click.option(
    "--name", "-n",
    required=True,
    help="Full publication name (e.g. 'The Wall Street Journal').",
)
@click.option(
    "--slug", "-s",
    required=True,
    help="URL-safe identifier (e.g. 'wsj').",
)
@click.option(
    "--url", "-u",
    required=True,
    help="Publication homepage URL.",
)
@click.option(
    "--interactive", "-i",
    is_flag=True,
    default=False,
    help="Interactively fill in profile details after creation.",
)
def add_publication(name, slug, url, interactive):
    """Create a new publication profile from the template.

    Copies the _template.yaml and fills in basic fields. Use --interactive
    to walk through ownership chain, RSS feeds, and conflict fields.
    """
    profiles_dir = get_profiles_dir()
    template_path = profiles_dir / "_template.yaml"
    target_path = profiles_dir / f"{slug}.yaml"

    if target_path.exists():
        console.print(
            f"[red]Error:[/red] Profile '{slug}' already exists at {target_path}"
        )
        raise SystemExit(1)

    if not template_path.exists():
        console.print(
            f"[red]Error:[/red] Template not found at {template_path}"
        )
        raise SystemExit(1)

    # Read template and fill basic fields
    template_content = template_path.read_text()
    content = template_content.replace(
        'name: ""', f'name: "{name}"'
    ).replace(
        'slug: ""', f'slug: "{slug}"'
    ).replace(
        'url: ""', f'url: "{url}"', 1  # only first occurrence (homepage)
    )

    target_path.write_text(content)
    console.print(
        f"[green]Created profile:[/green] {target_path}\n"
        f"  Name: {name}\n"
        f"  Slug: {slug}\n"
        f"  URL:  {url}"
    )

    if interactive:
        console.print("\n[yellow]Interactive mode not yet implemented.[/yellow]")
        console.print(
            f"Edit the profile directly: [cyan]{target_path}[/cyan]"
        )
    else:
        console.print(
            f"\nNext steps:\n"
            f"  1. Edit [cyan]{target_path}[/cyan] to add RSS feeds, "
            f"ownership chain, and conflicts.\n"
            f"  2. Run [cyan]mediascope ingest -p {slug}[/cyan] to start "
            f"collecting articles."
        )


# ---------------------------------------------------------------------------
# list-publications
# ---------------------------------------------------------------------------

@cli.command("list-publications")
def list_publications():
    """Show all configured publication profiles.

    Lists every YAML profile in the profiles directory with key metadata:
    name, slug, number of RSS feeds, and number of configured conflicts.
    """
    profiles = load_all_profiles()

    if not profiles:
        console.print("[yellow]No publication profiles found.[/yellow]")
        console.print(
            "Run [cyan]mediascope add-publication --name '…' --slug … --url …[/cyan] "
            "to create one."
        )
        return

    table = Table(
        title="Publication Profiles",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Slug", style="bold")
    table.add_column("Name")
    table.add_column("URL")
    table.add_column("Feeds", justify="right")
    table.add_column("Entities", justify="right")
    table.add_column("Conflicts", justify="right")

    for p in sorted(profiles, key=lambda x: x.get("slug", "")):
        if p.get("slug", "").startswith("_"):
            continue  # skip template
        table.add_row(
            p.get("slug", "?"),
            p.get("name", "?"),
            p.get("url", ""),
            str(len(p.get("rss_feeds", []))),
            str(len(p.get("target_entities", {}))),
            str(len(p.get("known_conflicts", []))),
        )

    console.print(table)


# ---------------------------------------------------------------------------
# status
# ---------------------------------------------------------------------------

@cli.command()
def status():
    """Show database and system status.

    Displays article counts per publication, date ranges, analysis coverage,
    and disk usage.
    """
    db = _get_db()

    stats = db.get_stats()

    console.print(
        Panel(
            f"Database: [cyan]{get_db_path()}[/cyan]\n"
            f"Total articles: [bold]{stats.get('total_articles', 0):,}[/bold]\n"
            f"Total analyses: [bold]{stats.get('total_analyses', 0):,}[/bold]\n"
            f"Database size: {stats.get('db_size_mb', 0):.1f} MB",
            title="MediaScope Status",
            border_style="cyan",
        )
    )

    # Per-publication breakdown
    pub_stats = stats.get("publications", {})
    if pub_stats:
        table = Table(
            title="Per-Publication Stats",
            box=box.SIMPLE_HEAVY,
            show_header=True,
            header_style="bold",
        )
        table.add_column("Publication")
        table.add_column("Articles", justify="right")
        table.add_column("Analysed", justify="right")
        table.add_column("First Article")
        table.add_column("Last Article")
        table.add_column("Last Ingest")

        for slug, ps in sorted(pub_stats.items()):
            table.add_row(
                slug,
                f"{ps.get('article_count', 0):,}",
                f"{ps.get('analysed_count', 0):,}",
                ps.get("first_article_date", "—"),
                ps.get("last_article_date", "—"),
                ps.get("last_ingest", "—"),
            )

        console.print(table)
    else:
        console.print("[dim]No articles ingested yet.[/dim]")

    # Profile summary
    profiles = load_all_profiles()
    active = [p for p in profiles if not p.get("slug", "").startswith("_")]
    console.print(
        f"\nConfigured profiles: [bold]{len(active)}[/bold]  "
        f"({', '.join(p.get('slug', '?') for p in active) or 'none'})"
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# careers — Editorial Histories subcommand group
# ---------------------------------------------------------------------------

@cli.group()
def careers():
    """Track journalist migrations and editorial leadership changes.

    Uses difference-in-differences methodology to decompose media bias
    into institutional and individual components based on journalist
    movements between publications.

    See docs/EDITORIAL_HISTORIES.md for the full methodology.
    """
    pass


@careers.command("list")
def careers_list():
    """List all tracked journalists and their current outlets."""
    from mediascope.careers.tracker import CareerTracker

    tracker = CareerTracker()
    try:
        tracker.load()
    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] {e}")
        console.print("Create profiles/careers/journalists.yaml with career data.")
        raise SystemExit(1)

    journalists = tracker.all_journalists()
    if not journalists:
        console.print("[yellow]No journalists loaded.[/yellow]")
        return

    table = Table(
        title="Tracked Journalists",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Name", style="bold")
    table.add_column("Current Outlet")
    table.add_column("Current Role")
    table.add_column("Publications")
    table.add_column("Migrations", justify="right")
    table.add_column("Career Span", justify="right")

    for j in sorted(journalists, key=lambda x: x.name):
        table.add_row(
            j.name,
            j.current_publication or "[dim]—[/dim]",
            j.current_role or "[dim]—[/dim]",
            ", ".join(j.publications_worked_at),
            str(len(j.migrations)),
            f"{j.career_span_years:.0f}y",
        )

    console.print(table)
    console.print(f"\n[dim]{len(journalists)} journalists tracked.[/dim]")


@careers.command("show")
@click.argument("journalist_name")
def careers_show(journalist_name):
    """Show a journalist's full career timeline.

    JOURNALIST_NAME is case-insensitive.
    """
    from mediascope.careers.tracker import CareerTracker

    tracker = CareerTracker()
    tracker.load()

    profile = tracker.get(journalist_name)
    if not profile:
        console.print(f"[red]Error:[/red] No profile found for '{journalist_name}'.")
        console.print("Available journalists:")
        for j in tracker.all_journalists():
            console.print(f"  • {j.name}")
        raise SystemExit(1)

    console.print(
        Panel(
            f"[bold]{profile.name}[/bold]\n"
            f"Current: {profile.current_publication or 'unknown'} "
            f"({profile.current_role or 'unknown'})\n"
            f"Career span: {profile.career_span_years:.1f} years  •  "
            f"Publications: {profile.n_publications}  •  "
            f"Migrations: {len(profile.migrations)}",
            title="Journalist Profile",
            border_style="cyan",
        )
    )

    # Career timeline
    table = Table(
        title="Career Timeline",
        box=box.SIMPLE_HEAVY,
        show_header=True,
        header_style="bold",
    )
    table.add_column("Period")
    table.add_column("Publication", style="bold")
    table.add_column("Role")
    table.add_column("Beat")
    table.add_column("Notes")

    for ev in profile.events:
        end = ev.date_end.strftime("%Y-%m") if ev.date_end else "present"
        table.add_row(
            f"{ev.date_start.strftime('%Y-%m')} → {end}",
            ev.publication_slug,
            ev.role,
            ev.beat or "[dim]—[/dim]",
            (ev.notes or "")[:80],
        )

    console.print(table)

    # Migrations
    if profile.migrations:
        console.print("\n[bold]Detected Migrations:[/bold]")
        for m in profile.migrations:
            console.print(
                f"  • {m.from_publication} → {m.to_publication} "
                f"({m.departure_date.strftime('%Y-%m')} → "
                f"{m.arrival_date.strftime('%Y-%m')}, "
                f"gap: {m.gap_days}d, "
                f"{'lateral' if m.is_lateral else 'promotion' if m.is_promotion else 'move'})"
            )


@careers.command("migrations")
@click.option("--from-pub", default=None, help="Filter by source publication slug.")
@click.option("--to-pub", default=None, help="Filter by destination publication slug.")
def careers_migrations(from_pub, to_pub):
    """List all detected migration events between tracked publications."""
    from mediascope.careers.tracker import CareerTracker

    tracker = CareerTracker()
    tracker.load()

    migrations = tracker.find_migrations(from_pub=from_pub, to_pub=to_pub)

    if not migrations:
        console.print("[yellow]No migration events found.[/yellow]")
        return

    table = Table(
        title="Journalist Migrations",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Journalist", style="bold")
    table.add_column("From")
    table.add_column("To")
    table.add_column("Departed")
    table.add_column("Arrived")
    table.add_column("Gap", justify="right")
    table.add_column("Type")

    for m in migrations:
        mtype = "lateral" if m.is_lateral else ("promotion" if m.is_promotion else "move")
        table.add_row(
            m.journalist_name,
            m.from_publication,
            m.to_publication,
            m.departure_date.strftime("%Y-%m"),
            m.arrival_date.strftime("%Y-%m"),
            f"{m.gap_days}d",
            mtype,
        )

    console.print(table)
    console.print(f"\n[dim]{len(migrations)} migrations found.[/dim]")


@careers.command("leadership")
@click.argument("publication_slug")
def careers_leadership(publication_slug):
    """Show editorial leadership changes at a publication.

    PUBLICATION_SLUG is the publication identifier (e.g. 'wired', 'nytimes').
    """
    from mediascope.careers.editorial_leadership import LeadershipAnalyzer

    analyzer = LeadershipAnalyzer()
    try:
        changes = analyzer.load_changes()
    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise SystemExit(1)

    pub_changes = [
        c for c in changes
        if c.publication_slug.lower() == publication_slug.lower()
    ]

    if not pub_changes:
        console.print(
            f"[yellow]No leadership changes found for '{publication_slug}'.[/yellow]"
        )
        return

    table = Table(
        title=f"Editorial Leadership Changes: {publication_slug}",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Date")
    table.add_column("Position", style="bold")
    table.add_column("Outgoing")
    table.add_column("Incoming", style="bold green")
    table.add_column("Notes")

    for ch in pub_changes:
        table.add_row(
            ch.effective_date.strftime("%Y-%m"),
            ch.position,
            ch.outgoing_name or "[dim]—[/dim]",
            ch.incoming_name,
            (ch.notes or "")[:60],
        )

    console.print(table)


@careers.command("diff")
@click.argument("journalist_name")
@click.option(
    "--window", "-w",
    type=int,
    default=180,
    help="Analysis window in days before/after migration (default 180).",
)
@click.option(
    "--target", "-t",
    default=None,
    help="Target entity to filter articles by (e.g. 'Meta').",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Write JSON results to file.",
)
def careers_diff(journalist_name, window, target, output):
    """Run difference-in-differences analysis for a journalist's migration.

    Requires that articles have been ingested and analysed for the relevant
    publications. If the journalist has multiple migrations, each is analysed
    separately.

    JOURNALIST_NAME is case-insensitive.
    """
    from mediascope.careers.tracker import CareerTracker
    from mediascope.careers.migrations import MigrationAnalyzer

    tracker = CareerTracker()
    tracker.load()
    profile = tracker.get(journalist_name)

    if not profile:
        console.print(f"[red]Error:[/red] No profile for '{journalist_name}'.")
        raise SystemExit(1)

    if not profile.migrations:
        console.print(f"[yellow]{profile.name} has no detected migrations.[/yellow]")
        return

    db = _get_db()
    analyzer = MigrationAnalyzer(window_days=window)

    results = []
    for migration in profile.migrations:
        console.print(
            f"\n[bold]Analysing:[/bold] {migration.from_publication} → "
            f"{migration.to_publication} "
            f"({migration.departure_date.strftime('%Y-%m')})"
        )

        # Fetch articles
        src_articles = db.get_articles(
            publication=migration.from_publication,
            entity_mention=target,
        )
        dst_articles = db.get_articles(
            publication=migration.to_publication,
            entity_mention=target,
        )
        j_articles = db.get_articles(author=profile.name)

        if not src_articles and not dst_articles:
            console.print(
                "  [yellow]No articles found. Run 'mediascope ingest' for the "
                "relevant publications first.[/yellow]"
            )
            continue

        try:
            result = analyzer.analyze_migration(
                migration=migration,
                source_articles=src_articles,
                dest_articles=dst_articles,
                journalist_articles=j_articles,
                control_articles=None,  # would need a control publication
                window_days=window,
            )
            results.append(result)

            # Display result
            sig = "[bold red]SIGNIFICANT[/bold red]" if result.did_is_significant else "[dim]not significant[/dim]"
            console.print(f"  DiD estimate: {result.did_estimate:+.3f} ({sig}, p={result.did_p_value:.4f})")
            console.print(f"  Source change: {result.source_raw_change:+.3f}")
            console.print(f"  Dest change:   {result.dest_raw_change:+.3f}")
            console.print(f"  Journalist Δ:  {result.journalist_tone_change:+.3f}")
            console.print(f"  Portable bias: {result.portable_bias_estimate:.3f}")
            console.print(f"  Articles: {result.n_articles_pre} pre, {result.n_articles_post} post")

        except Exception as e:
            console.print(f"  [red]Error:[/red] {e}")

    if output and results:
        import json as _json
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(
            _json.dumps([r.to_dict() for r in results], indent=2, default=str)
        )
        console.print(f"\n[green]Results written to {output}[/green]")


@careers.command("analyze")
@click.argument("journalist_name")
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Write JSON decomposition to file.",
)
def careers_analyze(journalist_name, output):
    """Run bias decomposition for a journalist.

    Decomposes the journalist's coverage tone into institutional, individual,
    and interaction components. Requires the journalist to have worked at
    ≥2 tracked publications with ≥5 analysed articles each.

    JOURNALIST_NAME is case-insensitive.
    """
    from mediascope.careers.tracker import CareerTracker
    from mediascope.careers.influence import InfluenceScorer

    tracker = CareerTracker()
    tracker.load()
    profile = tracker.get(journalist_name)

    if not profile:
        console.print(f"[red]Error:[/red] No profile for '{journalist_name}'.")
        raise SystemExit(1)

    if profile.n_publications < 2:
        console.print(
            f"[yellow]{profile.name} has articles at only "
            f"{profile.n_publications} publication(s). Need ≥2 for decomposition.[/yellow]"
        )
        return

    db = _get_db()
    scorer = InfluenceScorer()

    # Gather articles by publication
    articles_by_pub: dict[str, list[dict]] = {}
    for pub in profile.publications_worked_at:
        articles = db.get_articles(publication=pub, author=profile.name)
        if articles:
            articles_by_pub[pub] = articles

    if len(articles_by_pub) < 2:
        console.print(
            "[yellow]Insufficient data: need analysed articles at ≥2 publications. "
            "Run 'mediascope ingest' and 'mediascope analyze' first.[/yellow]"
        )
        return

    result = scorer.decompose(
        journalist_name=profile.name,
        articles_by_pub=articles_by_pub,
    )

    console.print(
        Panel(
            f"[bold]{result.journalist_name}[/bold]\n"
            f"Publications: {result.n_publications}  •  "
            f"Articles: {result.n_articles}  •  "
            f"Confidence: {result.confidence:.2f}\n\n"
            f"Institutional: [cyan]{result.institutional_component:.3f}[/cyan]  "
            f"({result.institutional_component * 100:.1f}% of variance)\n"
            f"Individual:    [magenta]{result.individual_component:.3f}[/magenta]  "
            f"({result.individual_component * 100:.1f}% of variance)\n"
            f"Interaction:   [yellow]{result.interaction_effect:.3f}[/yellow]  "
            f"({result.interaction_effect * 100:.1f}% of variance)\n\n"
            f"Portable Bias Score: [bold]"
            f"{'[red]' if result.portable_bias_score > 0.7 else '[green]'}"
            f"{result.portable_bias_score:.3f}[/bold]\n"
            f"Dominant source: {result.dominant_source}",
            title="Bias Decomposition",
            border_style="magenta",
        )
    )

    if output:
        import json as _json
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(_json.dumps(result.to_dict(), indent=2))
        console.print(f"\n[green]Results written to {output}[/green]")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    """Entry point for the mediascope CLI."""
    try:
        cli(standalone_mode=True)
    except SystemExit:
        raise
    except Exception as e:
        console.print(f"\n[red]Unexpected error:[/red] {e}")
        console.print("[dim]Use --help on any command for usage info.[/dim]")
        sys.exit(1)


if __name__ == "__main__":
    main()
