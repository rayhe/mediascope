"""MediaScope Same-Event Comparison Example.

Demonstrates the most powerful evidence technique in the toolkit:
comparing how different publications cover the exact same event.

When two outlets report on the same press release, court filing, or
product launch, the raw facts are held constant. Any difference in
tone, framing device density, source selection, or structural choices
is attributable to editorial DNA rather than event severity.

See METHODOLOGY.md §13 for the full theoretical framework.
"""

from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite, measure_outsourced_intensity
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.topics import classify_topic


def analyze_article(text: str, headline: str, target_entity: str = "Meta") -> dict:
    """Run the full analysis pipeline on a single article."""
    entities = detect_entities(text)
    sentiment = analyze_composite(text, headline)
    framing = detect_framing_devices(text)
    sources = extract_sources(text)
    stance = analyze_source_stance(sources, target_entity, full_text=text)
    outsourced = measure_outsourced_intensity(text)
    topics = classify_topic(text)

    return {
        "headline": headline,
        "word_count": len(text.split()),
        "primary_entity": get_primary_entity(entities),
        "sentiment": sentiment,
        "framing_devices": framing,
        "framing_device_count": len(framing),
        "framing_device_types": sorted(set(d.device_type for d in framing)),
        "sources": sources,
        "source_count": len(sources),
        "stance": stance,
        "outsourced_intensity": outsourced,
        "topics": topics,
    }


def compare_articles(
    article_a: dict,
    article_b: dict,
    pub_a: str,
    pub_b: str,
    event_description: str,
) -> str:
    """Generate a structured comparison report."""
    lines = []
    lines.append(f"# Same-Event Comparison: {event_description}")
    lines.append("")
    lines.append(f"**Event:** {event_description}")
    lines.append(f"**Publication A:** {pub_a}")
    lines.append(f"**Publication B:** {pub_b}")
    lines.append("")

    # --- Headline comparison ---
    lines.append("## Headlines")
    lines.append(f"- **{pub_a}:** {article_a['headline']}")
    lines.append(f"- **{pub_b}:** {article_b['headline']}")
    lines.append("")

    # --- Tone comparison ---
    tone_a = article_a["sentiment"].overall_tone
    tone_b = article_b["sentiment"].overall_tone
    tone_gap = tone_a - tone_b
    lines.append("## Tone Comparison")
    lines.append("")
    lines.append("| Dimension | {} | {} | Gap |".format(pub_a, pub_b))
    lines.append("|---|---|---|---|")
    lines.append(
        f"| **Overall tone** | {tone_a:.3f} | {tone_b:.3f} | {tone_gap:+.3f} |"
    )

    for dim in [
        "emotional_language_intensity",
        "source_authority_framing",
        "agency_attribution",
        "headline_body_alignment",
        "anonymous_source_ratio",
        "speculative_language_ratio",
        "comparative_framing",
    ]:
        val_a = getattr(article_a["sentiment"], dim, 0.0)
        val_b = getattr(article_b["sentiment"], dim, 0.0)
        label = dim.replace("_", " ").title()
        lines.append(f"| {label} | {val_a:.3f} | {val_b:.3f} | {val_a - val_b:+.3f} |")

    lines.append("")

    # --- Framing comparison ---
    lines.append("## Framing Device Comparison")
    lines.append("")
    lines.append(
        f"| Metric | {pub_a} | {pub_b} |"
    )
    lines.append("|---|---|---|")
    lines.append(
        f"| **Total devices** | {article_a['framing_device_count']} "
        f"| {article_b['framing_device_count']} |"
    )
    lines.append(
        f"| **Word count** | {article_a['word_count']} "
        f"| {article_b['word_count']} |"
    )

    # Per-device framing density (devices per 1,000 words)
    density_a = (
        article_a["framing_device_count"] / article_a["word_count"] * 1000
        if article_a["word_count"]
        else 0
    )
    density_b = (
        article_b["framing_device_count"] / article_b["word_count"] * 1000
        if article_b["word_count"]
        else 0
    )
    lines.append(
        f"| **Devices per 1K words** | {density_a:.1f} | {density_b:.1f} |"
    )
    lines.append("")

    # Device type breakdown
    all_types = sorted(
        set(article_a["framing_device_types"]) | set(article_b["framing_device_types"])
    )
    if all_types:
        lines.append("### Device Type Breakdown")
        lines.append("")
        lines.append(f"| Device Type | {pub_a} | {pub_b} |")
        lines.append("|---|---|---|")
        for dtype in all_types:
            count_a = sum(
                1 for d in article_a["framing_devices"] if d.device_type == dtype
            )
            count_b = sum(
                1 for d in article_b["framing_devices"] if d.device_type == dtype
            )
            lines.append(f"| {dtype} | {count_a} | {count_b} |")
        lines.append("")

    # --- Source comparison ---
    lines.append("## Source Deployment Comparison")
    lines.append("")
    lines.append(f"| Metric | {pub_a} | {pub_b} |")
    lines.append("|---|---|---|")
    lines.append(
        f"| **Total sources** | {article_a['source_count']} "
        f"| {article_b['source_count']} |"
    )
    lines.append(
        f"| **Adversarial** | {article_a['stance']['adversarial_count']} "
        f"| {article_b['stance']['adversarial_count']} |"
    )
    lines.append(
        f"| **Supportive** | {article_a['stance']['supportive_count']} "
        f"| {article_b['stance']['supportive_count']} |"
    )
    lines.append(
        f"| **Neutral** | {article_a['stance']['neutral_count']} "
        f"| {article_b['stance']['neutral_count']} |"
    )
    lines.append(
        f"| **Stance balance** | "
        f"{article_a['stance']['stance_balance']:.3f} | "
        f"{article_b['stance']['stance_balance']:.3f} |"
    )
    lines.append(
        f"| **Outsourced intensity** | "
        f"{article_a['outsourced_intensity']['outsourced_ratio']:.3f} | "
        f"{article_b['outsourced_intensity']['outsourced_ratio']:.3f} |"
    )
    lines.append("")

    # --- Interpretation ---
    lines.append("## Interpretation")
    lines.append("")
    if abs(tone_gap) > 0.3:
        more_neg = pub_a if tone_gap < 0 else pub_b
        lines.append(
            f"**Significant tone gap ({abs(tone_gap):.2f}).** {more_neg} covers this "
            f"event substantially more negatively than {pub_a if more_neg == pub_b else pub_b}."
        )
    elif abs(tone_gap) > 0.15:
        more_neg = pub_a if tone_gap < 0 else pub_b
        lines.append(
            f"**Moderate tone gap ({abs(tone_gap):.2f}).** {more_neg} leans more negative, "
            f"but the gap is within the range where editorial culture and genre conventions "
            f"(magazine vs wire service) could explain some of the difference."
        )
    else:
        lines.append(
            f"**Minimal tone gap ({abs(tone_gap):.2f}).** Both publications cover this "
            f"event with similar overall tone."
        )
    lines.append("")

    framing_diff = article_a["framing_device_count"] - article_b["framing_device_count"]
    if abs(framing_diff) >= 5:
        more_framed = pub_a if framing_diff > 0 else pub_b
        lines.append(
            f"**Large framing differential ({abs(framing_diff)} devices).** {more_framed} "
            f"deploys substantially more editorial framing techniques on the same facts. "
            f"This is the clearest signal of editorial DNA shaping coverage."
        )
    elif abs(framing_diff) >= 2:
        more_framed = pub_a if framing_diff > 0 else pub_b
        lines.append(
            f"**Moderate framing differential ({abs(framing_diff)} devices).** {more_framed} "
            f"uses more editorial framing, but the gap is not extreme."
        )
    lines.append("")

    # Limitations
    lines.append("## Limitations")
    lines.append("")
    lines.append(
        "- **Genre differences:** Wire services write breaking news; magazines write features. "
        "Some framing differences reflect genre conventions, not editorial bias."
    )
    lines.append(
        "- **Timing:** If one article was published later, the journalist had more time "
        "and potentially more sources."
    )
    lines.append(
        "- **Byline variation:** Individual journalists within a publication may differ. "
        "This comparison measures publication-level editorial culture."
    )
    lines.append(
        "- **Sample size:** A single article pair is anecdotal. Statistical confidence "
        "requires multiple same-event comparisons over time."
    )
    lines.append("")

    return "\n".join(lines)


def main():
    """Demo: compare wire-service vs magazine coverage of the same event.

    Uses sample text based on the MCI data exposure story (June 22, 2026),
    which was covered by both Reuters (wire service) and Wired (magazine)
    on the same day.
    """

    # --- Reuters version (wire-service baseline) ---
    reuters_text = """
    Meta Platforms has paused an internal program that tracked employee
    movements after a security incident exposed the data more broadly than
    intended, according to two people familiar with the matter.

    The program, known as MCI, collected badge swipe data from employees
    at Meta's offices. A configuration error made the data accessible to
    a wider group of employees than originally authorized, the sources said.

    Meta said in a statement that it "identified and addressed a
    configuration issue" and that there was "no indication that the data
    was accessed improperly."

    The company employs roughly 72,000 people globally.
    """

    reuters_headline = "Meta pauses employee-tracking program after data exposure"

    # --- Wired version (magazine editorial) ---
    wired_text = """
    For months, Meta quietly ran an internal surveillance program that
    tracked when and where its 72,000 employees swiped their badges,
    which buildings they entered, and how long they stayed. Now, a
    security failure has exposed that data far beyond its intended
    audience, according to three people with direct knowledge of the
    incident who spoke on condition of anonymity.

    The program, internally called MCI, was designed by Mark Zuckerberg's
    company as part of its push to enforce return-to-office mandates.
    As WIRED previously reported, Meta has been ratcheting up workplace
    monitoring since its 2023 restructuring.

    Meta said it had "identified and addressed a configuration issue"
    and found "no indication of improper access." But internal
    communications reviewed by WIRED paint a different picture: engineers
    scrambled for days to contain the exposure, and at least one manager
    described the incident as a "total failure of our security controls."

    "This is exactly what employees feared when they heard about MCI,"
    warned one privacy researcher at Stanford who reviewed the program's
    design. "You build a surveillance system, and eventually that system
    fails."

    The data breach is the latest in a string of internal controversies
    at Meta. Employee morale has cratered amid layoffs, mandatory
    return-to-office policies, and what workers describe as a "soul-crushing"
    environment in the Applied AI division.
    """

    wired_headline = "Meta Exposed Employee Badge Data From Internal Surveillance Program"

    # --- Run analysis ---
    print("Analyzing Reuters article...")
    reuters_analysis = analyze_article(reuters_text, reuters_headline)
    print(f"  Tone: {reuters_analysis['sentiment'].overall_tone:.3f}")
    print(f"  Framing devices: {reuters_analysis['framing_device_count']}")
    print()

    print("Analyzing Wired article...")
    wired_analysis = analyze_article(wired_text, wired_headline)
    print(f"  Tone: {wired_analysis['sentiment'].overall_tone:.3f}")
    print(f"  Framing devices: {wired_analysis['framing_device_count']}")
    print()

    # --- Generate comparison ---
    report = compare_articles(
        article_a=wired_analysis,
        article_b=reuters_analysis,
        pub_a="Wired",
        pub_b="Reuters",
        event_description="MCI Employee Badge Data Exposure (June 22, 2026)",
    )

    print("=" * 70)
    print(report)
    print("=" * 70)

    # --- Key takeaway ---
    tone_gap = abs(
        wired_analysis["sentiment"].overall_tone
        - reuters_analysis["sentiment"].overall_tone
    )
    framing_gap = (
        wired_analysis["framing_device_count"]
        - reuters_analysis["framing_device_count"]
    )
    print()
    print("KEY FINDINGS:")
    print(f"  Tone gap: {tone_gap:.2f} (same facts, different editorial stance)")
    print(f"  Framing gap: {framing_gap} devices (editorial technique differential)")
    print()
    print("  The wire-service baseline isolates the event's inherent severity")
    print("  from the magazine's editorial framing contribution. This is the")
    print("  media-analysis equivalent of a controlled experiment.")


def compare_multi_articles(
    articles: list[dict],
    publications: list[str],
    event_description: str,
    *,
    editorial_modes: dict[str, str] | None = None,
) -> str:
    """Generate an N-way cross-outlet comparison matrix.

    Unlike ``compare_articles`` (which handles A vs B), this function
    produces a single comparison table with one row per outlet, enabling
    visual inspection of the editorial gradient — the spectrum of
    editorial responses to the same underlying event.

    This implements the §10.3 requirement: "Present results in a
    comparison matrix … with one row per outlet."

    Parameters
    ----------
    articles : list[dict]
        Analysis results from ``analyze_article()``, one per outlet.
    publications : list[str]
        Human-readable outlet names, same order as *articles*.
    event_description : str
        Short description of the shared underlying event.
    editorial_modes : dict[str, str] | None
        Optional mapping from publication name to editorial mode
        (e.g. ``{"Reuters": "wire", "TechCrunch": "tech-editorial"}``).
    """
    if len(articles) < 2:
        raise ValueError("Need at least 2 articles for a comparison.")
    if len(articles) != len(publications):
        raise ValueError("articles and publications must be the same length.")

    modes = editorial_modes or {}
    lines: list[str] = []

    lines.append(f"# N-Way Cross-Outlet Comparison: {event_description}")
    lines.append("")
    lines.append(f"**Event:** {event_description}")
    lines.append(f"**Outlets:** {len(publications)}")
    lines.append("")

    # --- Outlet summary ---
    lines.append("## Outlet Summary")
    lines.append("")
    header = "| Outlet | Mode | Words | Date |"
    lines.append(header)
    lines.append("|---|---|---|---|")
    for pub, art in zip(publications, articles):
        mode = modes.get(pub, "—")
        words = art["word_count"]
        lines.append(f"| **{pub}** | {mode} | {words} | — |")
    lines.append("")

    # --- Tone comparison matrix ---
    tones = [art["sentiment"].overall_tone for art in articles]
    tone_range = max(tones) - min(tones)

    lines.append("## Tone Comparison Matrix")
    lines.append("")
    dims = [
        ("Overall tone", "overall_tone"),
        ("Emotional language intensity", "emotional_language_intensity"),
        ("Source authority framing", "source_authority_framing"),
        ("Agency attribution", "agency_attribution"),
        ("Headline-body alignment", "headline_body_alignment"),
        ("Anonymous source ratio", "anonymous_source_ratio"),
        ("Speculative language ratio", "speculative_language_ratio"),
        ("Comparative framing", "comparative_framing"),
    ]

    pub_headers = " | ".join(f"**{p}**" for p in publications)
    lines.append(f"| Dimension | {pub_headers} |")
    lines.append("|---" + "|---" * len(publications) + "|")

    for label, attr in dims:
        vals = []
        for art in articles:
            v = getattr(art["sentiment"], attr, 0.0)
            vals.append(f"{v:+.3f}" if attr == "overall_tone" else f"{v:.3f}")
        lines.append(f"| {label} | {' | '.join(vals)} |")

    lines.append("")
    lines.append(f"**Tone range: {tone_range:.3f}** ")
    most_neg = publications[tones.index(min(tones))]
    most_pos = publications[tones.index(max(tones))]
    lines.append(
        f"(most negative: {most_neg} at {min(tones):+.3f}, "
        f"most positive: {most_pos} at {max(tones):+.3f})"
    )
    lines.append("")

    # --- Framing device comparison ---
    lines.append("## Framing Device Comparison")
    lines.append("")
    lines.append(f"| Metric | {pub_headers} |")
    lines.append("|---" + "|---" * len(publications) + "|")

    counts = [art["framing_device_count"] for art in articles]
    lines.append(
        "| **Total devices** | "
        + " | ".join(str(c) for c in counts)
        + " |"
    )
    words = [art["word_count"] for art in articles]
    lines.append(
        "| **Word count** | "
        + " | ".join(str(w) for w in words)
        + " |"
    )
    densities = [c / w * 1000 if w else 0 for c, w in zip(counts, words)]
    lines.append(
        "| **Devices per 1K words** | "
        + " | ".join(f"{d:.1f}" for d in densities)
        + " |"
    )
    lines.append("")

    # Collect all device types across all articles
    all_types: set[str] = set()
    for art in articles:
        all_types.update(art["framing_device_types"])

    if all_types:
        lines.append("### Device Type Breakdown")
        lines.append("")
        lines.append(f"| Device Type | {pub_headers} |")
        lines.append("|---" + "|---" * len(publications) + "|")
        for dtype in sorted(all_types):
            row_vals = []
            for art in articles:
                count = sum(
                    1 for d in art["framing_devices"] if d.device_type == dtype
                )
                row_vals.append(str(count) if count else "—")
            lines.append(f"| {dtype} | {' | '.join(row_vals)} |")
        lines.append("")

    # --- Source deployment comparison ---
    lines.append("## Source Deployment Comparison")
    lines.append("")
    lines.append(f"| Metric | {pub_headers} |")
    lines.append("|---" + "|---" * len(publications) + "|")

    for metric_label, metric_key in [
        ("Total sources", "source_count"),
        ("Adversarial", "adversarial_count"),
        ("Supportive", "supportive_count"),
        ("Neutral", "neutral_count"),
    ]:
        vals = [str(art["stance"][metric_key]) if metric_key != "source_count"
                else str(art["source_count"])
                for art in articles]
        lines.append(f"| **{metric_label}** | {' | '.join(vals)} |")

    stance_vals = [f"{art['stance']['stance_balance']:.3f}" for art in articles]
    lines.append(f"| **Stance balance** | {' | '.join(stance_vals)} |")

    outsourced_vals = [
        f"{art['outsourced_intensity']['outsourced_ratio']:.3f}" for art in articles
    ]
    lines.append(f"| **Outsourced intensity** | {' | '.join(outsourced_vals)} |")
    lines.append("")

    # --- Cross-publication import detection ---
    import_pubs = []
    for pub, art in zip(publications, articles):
        for d in art["framing_devices"]:
            if d.device_type == "cross_publication_import":
                import_pubs.append((pub, d.evidence_text))

    if import_pubs:
        lines.append("## Cross-Publication Import Detection")
        lines.append("")
        lines.append(
            "This framing device is detectable only in N-way comparisons "
            "where the analyst has access to the source article. It occurs "
            "when a later article references an earlier outlet's loaded "
            "characterization as settled fact."
        )
        lines.append("")
        for pub, evidence in import_pubs:
            lines.append(f"- **{pub}:** `{evidence}`")
        lines.append("")

    # --- Interpretation ---
    lines.append("## Interpretation")
    lines.append("")
    if tone_range > 0.5:
        lines.append(
            f"**Large tone range ({tone_range:.2f}).** The same event "
            f"produces dramatically different editorial readings across "
            f"these {len(publications)} outlets. {most_neg} anchors the "
            f"negative end; {most_pos} anchors the positive end. This "
            f"spread isolates editorial DNA from event severity — the "
            f"facts are identical."
        )
    elif tone_range > 0.25:
        lines.append(
            f"**Moderate tone range ({tone_range:.2f}).** There is a "
            f"meaningful spread in editorial tone across outlets, though "
            f"some of the gap may reflect genre conventions (wire vs "
            f"financial vs tech-editorial)."
        )
    else:
        lines.append(
            f"**Narrow tone range ({tone_range:.2f}).** All outlets "
            f"cover this event with broadly similar tone. Editorial "
            f"DNA differences are minimal for this event."
        )
    lines.append("")

    # Framing density gradient
    max_density = max(densities)
    min_density = min(densities)
    if min_density > 0 and max_density - min_density > 10:
        densest = publications[densities.index(max_density)]
        sparsest = publications[densities.index(min_density)]
        lines.append(
            f"**Framing density gradient:** {densest} ({max_density:.1f} "
            f"devices/1K words) uses {max_density / min_density:.1f}× "
            f"the framing density of {sparsest} ({min_density:.1f} "
            f"devices/1K words)."
        )
        lines.append("")

    # Limitations
    lines.append("## Limitations")
    lines.append("")
    lines.append(
        "- **Genre differences:** Wire services, financial analysis, "
        "tech editorial, and industry trade press follow different "
        "conventions. Some differences reflect genre, not editorial bias."
    )
    lines.append(
        "- **Timing:** Articles published later had access to more "
        "sources and follow-up reporting."
    )
    lines.append(
        "- **Article length:** Longer articles have more room for "
        "framing devices. Per-1K-word density normalizes this, but "
        "longer articles also tend toward more analysis."
    )
    lines.append(
        "- **N-way advantage:** This comparison is stronger than any "
        "single pair because it reveals the gradient, not just a gap."
    )
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
