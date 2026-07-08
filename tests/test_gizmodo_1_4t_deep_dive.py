"""Type A deep-dive tests for Gizmodo '$1.4 Trillion Existential Threat' article.

Discovered in MediaScope Type A iteration 2026-07-07 16:00 PT.
Tests framing gaps: headline scale_magnitude, missing loaded_language patterns
(exploiting, hooked), accumulation_cascade, market_cap_anchoring,
failed_defense_framing.

Article: "Meta's Teen Safety Case Just Became a $1.4 Trillion Existential Threat"
Publication: Gizmodo (July 7, 2026)
Source: https://gizmodo.com/metas-teen-safety-case-just-became-a-1-4-trillion-existential-threat-2000782306
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite, analyze_vader
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic
from mediascope.analyze.entities import detect_entities

# ----- Full article text ----- #

ARTICLE = (
    "Meta is facing $1.4 trillion in damages in a social media addiction case brought by four states. "
    "Thirty-three states have banded together to sue Meta, alleging that the company was exploiting its "
    "young users on Instagram and Facebook for profit, including by collecting data from children without "
    "parental consent. Four of those states — California, New Jersey, Colorado and Kentucky — also claim "
    "that the company misled consumers about the addictive design features on the platforms, thereby "
    "causing mental health problems in children who got hooked from an early age. "
    "The damages requested by those four states add up to a whopping $1.4 trillion, Meta said in a recent "
    "court filing, a figure that would allegedly go even higher with the other penalties the attorneys "
    "general seek to add. The number is high by many standards but especially when compared to the "
    "company's market capitalization, which is just above $1.5 trillion. "
    "Meta has denied the allegations, and recently attempted yet failed to get the addiction claims dismissed. "
    "In the latest court submission, the attorneys for Meta argued that the $1.4 trillion in damages was "
    "unsubstantiated and disproportionate. "
    "Meta has not found any case, under any cause of action, where one defendant was ordered to pay over "
    "one trillion dollars — or any number remotely close to that staggering figure, the attorneys claim. "
    "The states filings are sealed, but per Reuters, the penalties were calculated by multiplying the "
    "number of violations, aka the rough amount of young users impacted by the addictive design choices, "
    "by the fine amounts designated by state law. "
    "Meta argues that the number is so high that it has no parallel in the history of consumer protection enforcement. "
    "Indeed, the Federal Trade Commission recently described a 1 billion dollar penalty as the largest ever "
    "in a case involving an FTC rule violation, the filing states. The AGs demand exceeds even those "
    "record figures by several orders of magnitude, and is in gross disproportion to the specified violations alleged here. "
    "The case is now going to court in August, and if the judge rules against Meta, it could prove to be a "
    "substantial financial problem for the company. For months now, Meta executives have admitted to investors "
    "that they were anticipating some material loss this year due to scrutiny on youth-related issues. "
    "But the $1.4 trillion number was previously unknown, and it is far from the only youth-related headache "
    "the tech giant is bracing for. "
    "Meta has been plagued with mounting litigation over alleged deceptive social media practices targeting "
    "young users. In a watershed verdict delivered earlier this year, a judge found Meta and Google liable "
    "and ordered them to pay $6 million in damages to a now 20-year-old who said that deliberate addictive "
    "design features on social media platforms like Instagram got her hooked from a young age and exacerbated "
    "mental health problems like depression and anxiety. Prior to that verdict, platform operators were "
    "protected from liability for third-party content under Section 230 of the Communications Decency Act. "
    "The March verdict marked just the beginning of Meta's legal troubles. The company still has more than "
    "3,000 similar cases pending in California state court. Another 14 states have also brought claims similar "
    "to the one led by the four states, with the case set to go to trial early next year."
)

HEADLINE = "Meta's Teen Safety Case Just Became a $1.4 Trillion Existential Threat"


# --------------------------------------------------------------------------- #
# Loaded language — missing patterns
# --------------------------------------------------------------------------- #


class TestLoadedLanguageGaps:
    """Loaded language patterns missed in initial toolkit run."""

    def test_exploiting_detected(self):
        """'exploiting its young users' is strong loaded language."""
        devices = detect_framing_devices(ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence_texts = " ".join(d.evidence_text for d in loaded)
        assert any("exploit" in d.evidence_text.lower() for d in loaded), (
            f"'exploiting' not detected as loaded_language; "
            f"got: {[d.evidence_text for d in loaded]}"
        )

    def test_hooked_detected(self):
        """'got hooked from an early age' uses drug-addiction metaphor."""
        devices = detect_framing_devices(ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("hooked" in d.evidence_text.lower() for d in loaded), (
            f"'hooked' (addiction metaphor) not detected as loaded_language; "
            f"got: {[d.evidence_text for d in loaded]}"
        )


# --------------------------------------------------------------------------- #
# Headline framing
# --------------------------------------------------------------------------- #


class TestHeadlineFraming:
    """Headline: 'Meta's Teen Safety Case Just Became a $1.4 Trillion Existential Threat'"""

    def test_catastrophizing_detected(self):
        """'Existential Threat' in headline should trigger catastrophizing."""
        hd = detect_framing_devices(HEADLINE)
        types = {d.device_type for d in hd}
        assert "catastrophizing" in types

    def test_scale_magnitude_in_headline(self):
        """'$1.4 Trillion' in headline should trigger scale_magnitude."""
        hd = detect_framing_devices(HEADLINE)
        types = {d.device_type for d in hd}
        assert "scale_magnitude" in types, (
            f"$1.4 Trillion in headline not detected as scale_magnitude; "
            f"got types: {types}"
        )


# --------------------------------------------------------------------------- #
# Accumulation / litigation cascade
# --------------------------------------------------------------------------- #


class TestAccumulationCascade:
    """The article piles legal threats: 4 states → 33 states → 3,000 cases → 14 more states."""

    def test_multiple_scale_magnitudes(self):
        """Should detect multiple scale_magnitude instances for the cascade."""
        devices = detect_framing_devices(ARTICLE)
        scale = [d for d in devices if d.device_type == "scale_magnitude"]
        # At minimum: $1.4T (twice), $6M, plus ideally 3,000 cases
        assert len(scale) >= 3, (
            f"Expected >=3 scale_magnitude devices, got {len(scale)}: "
            f"{[d.evidence_text[:60] for d in scale]}"
        )

    def test_trend_bundling_for_legal_cascade(self):
        """Trend bundling should capture the 'beginning of Meta's legal troubles' framing."""
        devices = detect_framing_devices(ARTICLE)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert bundling, "No trend_bundling detected for legal cascade"


# --------------------------------------------------------------------------- #
# Topic classification
# --------------------------------------------------------------------------- #


class TestTopics:
    """Topic classification for the $1.4T penalty article."""

    def test_litigation_is_top_topic(self):
        topics = classify_topic(ARTICLE)
        assert topics, "No topics detected"
        assert topics[0].topic == "litigation"

    def test_child_safety_detected(self):
        topics = classify_topic(ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "child_safety" in topic_names


# --------------------------------------------------------------------------- #
# Source extraction
# --------------------------------------------------------------------------- #


class TestSources:
    """Source extraction for the Gizmodo $1.4T article."""

    def test_reuters_per_attribution(self):
        sources = extract_sources(ARTICLE)
        reuters = [s for s in sources if s.name == "Reuters"]
        assert reuters, "Reuters not extracted as source"
        assert reuters[0].source_type == "news_outlet"

    def test_filing_as_source(self):
        sources = extract_sources(ARTICLE)
        filing = [s for s in sources if "filing" in s.name.lower()]
        assert filing, "'the filing states' not extracted as documentary source"

    def test_meta_attorneys_as_legal_party(self):
        sources = extract_sources(ARTICLE)
        meta_legal = [s for s in sources if "attorney" in s.name.lower() or
                      s.source_type == "legal_party"]
        assert meta_legal, "Meta's attorneys not extracted as legal_party source"


# --------------------------------------------------------------------------- #
# Sentiment
# --------------------------------------------------------------------------- #


class TestSentiment:
    """Sentiment for a heavily negative litigation article."""

    def test_vader_strongly_negative(self):
        vader = analyze_vader(ARTICLE)
        assert vader["compound"] < -0.5, (
            f"VADER should be strongly negative for this article, "
            f"got {vader['compound']}"
        )

    def test_composite_negative(self):
        comp = analyze_composite(ARTICLE)
        assert comp.overall_tone < 0.0, (
            f"Composite should be negative, got {comp.overall_tone}"
        )


# --------------------------------------------------------------------------- #
# Entity detection
# --------------------------------------------------------------------------- #


class TestEntities:
    """Entity detection for the $1.4T article."""

    def test_meta_is_primary_entity(self):
        entities = detect_entities(ARTICLE)
        from collections import Counter
        counts = Counter(e.entity for e in entities)
        assert counts["Meta"] >= 8, f"Meta should appear 8+ times, got {counts['Meta']}"

    def test_google_detected(self):
        entities = detect_entities(ARTICLE)
        ent_names = {e.entity for e in entities}
        assert "Google" in ent_names

    def test_instagram_detected(self):
        entities = detect_entities(ARTICLE)
        ent_names = {e.entity for e in entities}
        assert "Instagram" in ent_names
