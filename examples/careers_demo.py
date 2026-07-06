"""MediaScope Editorial Histories Demo.

Demonstrates the toolkit's novel contribution: applying causal inference
methods (difference-in-differences, interrupted time series, two-way
ANOVA bias decomposition) to journalist migration data at scale.

No prior work systematically applies DiD to journalist-level editorial
migration data. See docs/EDITORIAL_HISTORIES.md for the full methodology
and Card & Krueger (1994) for the original DiD framework.

This demo shows three capabilities:

    1. Career timeline exploration — browse 134 tracked journalists,
       their career events, and automatically detected migrations
    2. Migration analysis — find high-value moves between the five
       tracked publications (Wired, NYT, Guardian, Atlantic, MIT TR)
    3. DiD setup — how to frame the natural experiment when a journalist
       moves from Publication A to Publication B

Requires: pip install -e .  (from the mediascope repo root)
"""

from collections import Counter
from mediascope.careers.tracker import CareerTracker
from mediascope.careers.models import JournalistProfile, MigrationEvent


def section(title: str) -> None:
    """Print a section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def show_career_overview(tracker: CareerTracker) -> None:
    """Show the scope of the career dataset."""
    section("1. Dataset Overview")

    journalists = tracker.all_journalists()
    all_migrations = tracker.find_migrations()

    print(f"  Tracked journalists:      {len(journalists)}")
    print(f"  Total career events:      {sum(len(j.events) for j in journalists)}")
    print(f"  Detected migrations:      {len(all_migrations)}")
    print(f"  Multi-pub journalists:    {sum(1 for j in journalists if j.n_publications >= 2)}")
    print()

    # Publication distribution
    pub_counter: Counter[str] = Counter()
    for j in journalists:
        for pub in j.publications_worked_at:
            pub_counter[pub] += 1

    tracked_pubs = {"wired", "nytimes", "guardian", "atlantic", "mit-tech-review"}
    print("  Journalists per tracked publication:")
    for pub in sorted(tracked_pubs):
        print(f"    {pub:25s}  {pub_counter.get(pub, 0)}")
    print()

    # Career span statistics
    spans = [j.career_span_years for j in journalists if j.career_span_years > 0]
    if spans:
        print(f"  Career span range:        {min(spans):.1f} – {max(spans):.1f} years")
        print(f"  Median career span:       {sorted(spans)[len(spans) // 2]:.1f} years")


def show_journalist_profile(tracker: CareerTracker, name: str) -> None:
    """Display a journalist's full career timeline."""
    profile = tracker.get(name)
    if not profile:
        print(f"  Journalist '{name}' not found.")
        return

    print(f"  {profile.name}")
    print(f"  Current outlet:  {profile.current_publication or 'unknown'}")
    print(f"  Career span:     {profile.career_span_years:.1f} years")
    print(f"  Publications:    {profile.n_publications}")
    print(f"  Migrations:      {len(profile.migrations)}")
    print()

    # Career timeline
    print("  Career Timeline:")
    print(f"  {'Date Range':25s}  {'Publication':25s}  {'Role':25s}  {'Type'}")
    print(f"  {'-' * 25}  {'-' * 25}  {'-' * 25}  {'-' * 10}")
    for ev in profile.events:
        end_str = str(ev.date_end) if ev.date_end else "present"
        date_range = f"{ev.date_start} → {end_str}"
        print(f"  {date_range:25s}  {ev.publication_slug:25s}  {ev.role:25s}  {ev.event_type}")

    # Migrations
    if profile.migrations:
        print()
        print("  Detected Migrations:")
        for m in profile.migrations:
            gap_str = f"{m.gap_days} day gap" if m.gap_days > 0 else "seamless"
            print(f"    {m.from_publication} → {m.to_publication} ({gap_str})")


def show_high_value_migrations(tracker: CareerTracker) -> None:
    """Show migrations between tracked publications — the highest-value
    data for causal analysis because we have full profiles on both sides."""
    section("3. High-Value Migrations (Between Tracked Publications)")

    tracked_pubs = {"wired", "nytimes", "guardian", "atlantic", "mit-tech-review"}
    all_migs = tracker.find_migrations()

    # Filter to migrations where BOTH pubs are tracked
    both_tracked = [
        m for m in all_migs
        if m.from_publication in tracked_pubs and m.to_publication in tracked_pubs
    ]

    print(f"  Migrations between tracked publications: {len(both_tracked)}")
    print()

    if both_tracked:
        print(f"  {'Journalist':30s}  {'From':20s}  {'To':20s}  {'Gap'}")
        print(f"  {'-' * 30}  {'-' * 20}  {'-' * 20}  {'-' * 10}")
        for m in both_tracked:
            gap_str = f"{m.gap_days}d" if m.gap_days > 0 else "0d"
            print(f"  {m.journalist_name:30s}  {m.from_publication:20s}  {m.to_publication:20s}  {gap_str}")

    # Also show migrations TO tracked pubs (incoming talent)
    print()
    incoming = [
        m for m in all_migs
        if m.to_publication in tracked_pubs and m.from_publication not in tracked_pubs
    ]

    # Show the flow matrix
    print("  Migration Flow Matrix (incoming → tracked publication):")
    for pub in sorted(tracked_pubs):
        into = [m for m in incoming if m.to_publication == pub]
        from_pubs = Counter(m.from_publication for m in into)
        if into:
            top_sources = from_pubs.most_common(3)
            sources_str = ", ".join(f"{p} ({c})" for p, c in top_sources)
            print(f"    → {pub:25s}  {len(into)} arrivals, top sources: {sources_str}")


def show_did_setup(tracker: CareerTracker) -> None:
    """Demonstrate how to set up a DiD natural experiment from a migration."""
    section("4. Difference-in-Differences Setup")

    print("  When a journalist moves from Publication A to Publication B,")
    print("  it creates three testable natural experiments:\n")
    print("    1. SOURCE-SIDE:  Does A's coverage change after they leave?")
    print("       → Institutional vs. individual bias")
    print("    2. PORTABLE BIAS: Does the journalist's tone change at B?")
    print("       → Editorial capture vs. portable bias")
    print("    3. DEST-SIDE:    Does B's coverage change after they arrive?")
    print("       → The journalist's editorial influence\n")

    # Pick a concrete example: a migration between tracked pubs
    tracked_pubs = {"wired", "nytimes", "guardian", "atlantic", "mit-tech-review"}
    all_migs = tracker.find_migrations()
    both_tracked = [
        m for m in all_migs
        if m.from_publication in tracked_pubs and m.to_publication in tracked_pubs
    ]

    if not both_tracked:
        print("  No migrations between tracked publications found.")
        return

    example = both_tracked[0]
    journalist = tracker.get(example.journalist_name)
    if not journalist:
        return

    print(f"  EXAMPLE: {example.journalist_name}")
    print(f"  {example.from_publication} → {example.to_publication}")
    print(f"  Departed: {example.departure_date}")
    print(f"  Arrived:  {example.arrival_date}")
    print(f"  Gap:      {example.gap_days} days")
    print()

    print("  DiD REGRESSION MODEL:")
    print()
    print("    Y = β₀ + β₁·Treatment + β₂·Post + β₃·(Treatment × Post) + ε")
    print()
    print("  Where:")
    print(f"    Y          = article tone score toward target entity (e.g. Meta)")
    print(f"    Treatment  = 1 for {example.from_publication}, 0 for control pub")
    print(f"    Post       = 1 for articles after {example.departure_date}")
    print(f"    β₃         = CAUSAL EFFECT of {example.journalist_name}'s departure")
    print()
    print("  β₃ is the key number. It tells us how much this journalist's")
    print("  departure *caused* a change in coverage tone, after removing")
    print("  secular trends (like a news cycle shift) that would have")
    print("  happened regardless.")
    print()

    # The CLI equivalent
    print("  CLI EQUIVALENT:")
    print(f'    mediascope careers diff "{example.journalist_name}" --window 180 --target Meta')
    print()

    # Python API
    print("  PYTHON API:")
    print(f"    from mediascope.careers.migrations import MigrationAnalyzer")
    print(f"    analyzer = MigrationAnalyzer()")
    print(f'    result = analyzer.analyze_migration("{example.journalist_name}", window_days=180)')
    print(f"    print(f\"DiD estimate: {{result.did_estimate:.3f}}\")")
    print(f"    print(f\"p-value: {{result.p_value:.4f}}\")")
    print(f"    print(f\"Portable bias: {{result.portable_bias:.3f}}\")")


def show_pipeline_narrative(tracker: CareerTracker) -> None:
    """Show the longest and most interesting career pipelines."""
    section("5. Notable Career Pipelines")

    journalists = tracker.all_journalists()

    # Sort by migration count
    by_migs = sorted(journalists, key=lambda j: len(j.migrations), reverse=True)

    print("  Journalists with most migrations (natural experiment density):\n")
    print(f"  {'Name':30s}  {'Migrations':12s}  {'Pubs':6s}  {'Span':8s}  Pipeline")
    print(f"  {'-' * 30}  {'-' * 12}  {'-' * 6}  {'-' * 8}  {'-' * 40}")

    for j in by_migs[:15]:
        pipeline = " → ".join(j.publications_worked_at)
        # Truncate long pipelines
        if len(pipeline) > 60:
            pipeline = pipeline[:57] + "..."
        print(
            f"  {j.name:30s}  {len(j.migrations):12d}  "
            f"{j.n_publications:6d}  {j.career_span_years:6.1f}y  {pipeline}"
        )


def main():
    """Run the Editorial Histories demo."""
    print("MediaScope Editorial Histories Demo")
    print("=" * 70)
    print()
    print("The Editorial Histories module is MediaScope's novel contribution:")
    print("applying causal inference (DiD, ITS, two-way ANOVA) to journalist")
    print("migration data at scale. No prior work does this systematically.")
    print()
    print("See docs/EDITORIAL_HISTORIES.md for the full methodology.")

    tracker = CareerTracker()

    # 1. Dataset overview
    show_career_overview(tracker)

    # 2. Detailed journalist profiles
    section("2. Journalist Profiles")

    # Karen Hao — highest-value multi-pub migration
    print("  --- Karen Hao (MIT Tech Review → Atlantic) ---")
    show_journalist_profile(tracker, "Karen Hao")
    print()

    # Zoë Schiffer — The Verge → Platformer → Wired
    print("  --- Zoë Schiffer (The Verge → Platformer → Wired) ---")
    show_journalist_profile(tracker, "Zoë Schiffer")
    print()

    # Steve Lohr — NYT lifer, institutional framing baseline
    print("  --- Steve Lohr (NYT lifer — institutional baseline) ---")
    show_journalist_profile(tracker, "Steve Lohr")

    # 3. High-value migrations
    show_high_value_migrations(tracker)

    # 4. DiD setup
    show_did_setup(tracker)

    # 5. Notable pipelines
    show_pipeline_narrative(tracker)

    # Summary
    section("Summary")
    print("  The Editorial Histories module provides three causal analysis tools:")
    print()
    print("  1. Difference-in-Differences (DiD)")
    print("     When a journalist moves between publications, the move is a")
    print("     natural experiment. DiD isolates the causal effect of the")
    print("     personnel change from secular trends in the news cycle.")
    print()
    print("  2. Interrupted Time-Series (ITS)")
    print("     When a new editor-in-chief takes over, ITS measures the")
    print("     immediate level shift and gradual slope change in coverage tone.")
    print()
    print("  3. Bias Decomposition (Two-Way ANOVA)")
    print("     For journalists at 2+ publications, decomposes total variance")
    print("     into institutional, individual, and interaction components.")
    print("     The Portable Bias Score (0-1) tells you how much a journalist's")
    print("     tone travels with them vs. being shaped by institutional culture.")
    print()
    print("  These tools transform correlation ('Wired is negative about Meta')")
    print("  into testable causal claims ('Is the negativity institutional,")
    print("  individual, or both?').")
    print()
    print("  Full methodology: docs/EDITORIAL_HISTORIES.md")
    print("  Academic foundation: Card & Krueger (1994), DiD applied to editorial")
    print("  migration data at scale — no prior work does this.")


if __name__ == "__main__":
    main()
