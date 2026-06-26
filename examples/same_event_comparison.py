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


if __name__ == "__main__":
    main()
