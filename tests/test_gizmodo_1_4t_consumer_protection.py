"""Tests for Gizmodo Meta $1.4T youth penalty article deep dive (Jul 7, 2026 6pm).

Validates toolkit improvements from Type A deep dive (18:00 PT iteration):
- consumer_protection topic detection (new topic)
- valuation_comparison framing device (new device)
- strategic_disclosure quote-tolerance fix
- entity detection accuracy
- catastrophizing headline detection
"""

import re

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.topics import classify_topic

# --- Article text (body only, after frontmatter) ---
ARTICLE_BODY = (
    "Meta is facing $1.4 trillion in damages in a social media addiction "
    "case brought by four states.\n\n"
    "Thirty-three states have banded together to sue Meta, alleging that the "
    "company was exploiting its young users on Instagram and Facebook for "
    "profit, including by collecting data from children without parental "
    "consent. Four of those states\u2014California, New Jersey, Colorado and "
    "Kentucky\u2014also claim that the company misled consumers about the "
    "addictive design features on the platforms, thereby causing mental "
    "health problems in children who got hooked from an early age.\n\n"
    "The damages requested by those four states add up to a whopping $1.4 "
    "trillion, Meta said in a recent court filing, a figure that would "
    "allegedly go even higher with the other penalties the attorneys general "
    "seek to add. The number is high by many standards but especially when "
    "compared to the company\u2019s market capitalization, which is just "
    "above $1.5 trillion.\n\n"
    "Meta has denied the allegations, and recently attempted yet failed to "
    "get the addiction claims dismissed. In the latest court submission, the "
    "attorneys for Meta argued that the $1.4 trillion in damages was "
    "unsubstantiated and disproportionate.\n\n"
    "\u201cMeta has not found any case, under any cause of action, where one "
    "defendant was ordered to pay over one trillion dollars\u2014or any "
    "number remotely close to that staggering figure,\u201d the attorneys "
    "claim.\n\n"
    "The states\u2019 filings are sealed, but per Reuters, the penalties "
    "were calculated by multiplying the number of violations, aka the rough "
    "amount of young users impacted by the addictive design choices, by the "
    "fine amounts designated by state law.\n\n"
    "Meta argues that the number is so high that it has no parallel \u201cin "
    "the history of consumer protection enforcement.\u201d\n\n"
    "\u201cIndeed, the Federal Trade Commission recently described a \u2018$1 "
    "billion penalty\u2019 as the \u2018largest ever in a case involving an "
    "FTC rule violation,\u2019\u201d the filing states. \u201cThe AGs\u2019 "
    "demand exceeds even those record figures by several orders of "
    "magnitude, and is in gross disproportion to the specified violations "
    "alleged here.\u201d\n\n"
    "The case is now going to court in August, and if the judge rules "
    "against Meta, it could prove to be a substantial financial problem for "
    "the company. For months now, Meta executives have admitted to investors "
    "that they were anticipating some material loss this year due to "
    "\u201cscrutiny on youth-related issues.\u201d But the $1.4 trillion "
    "number was previously unknown, and it is far from the only "
    "youth-related headache the tech giant is bracing for.\n\n"
    "Meta has been plagued with mounting litigation over alleged deceptive "
    "social media practices targeting young users. In a watershed verdict "
    "delivered earlier this year, a judge found Meta and Google liable and "
    "ordered them to pay $6 million in damages to a now 20-year-old who "
    "said that deliberate addictive design features on social media "
    "platforms like Instagram got her hooked from a young age and "
    "exacerbated mental health problems like depression and anxiety. Prior "
    "to that verdict, platform operators were protected from liability for "
    "third-party content under Section 230 of the Communications Decency "
    "Act.\n\n"
    "The March verdict marked just the beginning of Meta\u2019s legal "
    "troubles. The company still has more than 3,000 similar cases pending "
    "in California state court. Another 14 states have also brought claims "
    "similar to the one led by the four states, with the case set to go to "
    "trial early next year."
)

HEADLINE = (
    "Meta\u2019s Teen Safety Case Just Became a $1.4 Trillion "
    "Existential Threat"
)

FULL_TEXT = f"# {HEADLINE}\n\n{ARTICLE_BODY}"


class TestConsumerProtectionTopic:
    """consumer_protection topic should fire on consumer protection litigation."""

    def test_consumer_protection_detected(self):
        topics = classify_topic(ARTICLE_BODY)
        topic_names = {t.topic for t in topics}
        assert "consumer_protection" in topic_names, (
            f"consumer_protection topic not detected. Topics found: {topic_names}"
        )

    def test_consumer_protection_keywords(self):
        topics = classify_topic(ARTICLE_BODY)
        cp = next(t for t in topics if t.topic == "consumer_protection")
        assert "consumer protection" in cp.matched_keywords or \
               "consumer protection enforcement" in cp.matched_keywords, (
            f"Expected 'consumer protection' keyword match. Got: {cp.matched_keywords}"
        )

    def test_attorneys_general_keyword(self):
        topics = classify_topic(ARTICLE_BODY)
        cp = next(t for t in topics if t.topic == "consumer_protection")
        assert "attorneys general" in cp.matched_keywords, (
            f"Expected 'attorneys general' in consumer_protection keywords. "
            f"Got: {cp.matched_keywords}"
        )

    def test_misled_consumers_keyword(self):
        topics = classify_topic(ARTICLE_BODY)
        cp = next(t for t in topics if t.topic == "consumer_protection")
        assert "misled consumers" in cp.matched_keywords, (
            f"Expected 'misled consumers' in consumer_protection keywords. "
            f"Got: {cp.matched_keywords}"
        )

    def test_litigation_still_primary(self):
        """Litigation should remain the highest-confidence topic."""
        topics = classify_topic(ARTICLE_BODY)
        if not topics:
            pytest.skip("No topics detected")
        top = topics[0]
        assert top.topic == "litigation", (
            f"Expected litigation as top topic, got {top.topic}"
        )


class TestValuationComparison:
    """valuation_comparison framing device should fire on market-cap anchoring."""

    def test_valuation_comparison_detected(self):
        framings = detect_framing_devices(ARTICLE_BODY)
        vc = [f for f in framings if f.device_type == "valuation_comparison"]
        assert len(vc) >= 1, (
            "valuation_comparison not detected. "
            "Article says 'compared to the company\u2019s market capitalization'."
        )

    def test_valuation_comparison_evidence(self):
        framings = detect_framing_devices(ARTICLE_BODY)
        vc = [f for f in framings if f.device_type == "valuation_comparison"]
        assert any("market" in f.evidence_text.lower() for f in vc), (
            f"valuation_comparison evidence should reference 'market'. "
            f"Got: {[f.evidence_text for f in vc]}"
        )


class TestStrategicDisclosureQuoteFix:
    """strategic_disclosure should match 'has no parallel' even with quotes."""

    def test_no_parallel_with_curly_quotes(self):
        text = (
            "Meta argues that the number is so high that it has no parallel "
            "\u201cin the history of consumer protection enforcement.\u201d"
        )
        framings = detect_framing_devices(text)
        sd = [f for f in framings if f.device_type == "strategic_disclosure"]
        assert len(sd) >= 1, (
            "strategic_disclosure not detected on 'has no parallel \u201cin "
            "the history of\u2019 with curly quotes."
        )

    def test_no_parallel_with_straight_quotes(self):
        text = (
            'It has no parallel "in the history of consumer protection '
            'enforcement."'
        )
        framings = detect_framing_devices(text)
        sd = [f for f in framings if f.device_type == "strategic_disclosure"]
        assert len(sd) >= 1, (
            "strategic_disclosure not detected on 'has no parallel' with "
            "straight quotes."
        )

    def test_no_analog_without_quotes(self):
        """Original case (no quotes) should still work."""
        text = "The penalty has no analog in the history of antitrust enforcement."
        framings = detect_framing_devices(text)
        sd = [f for f in framings if f.device_type == "strategic_disclosure"]
        assert len(sd) >= 1, (
            "strategic_disclosure regression: 'has no analog' without quotes "
            "no longer matches."
        )


class TestCatastrophizingHeadline:
    """Headline 'Existential Threat' should trigger catastrophizing."""

    def test_existential_threat_in_headline(self):
        framings = detect_framing_devices(FULL_TEXT)
        cats = [f for f in framings if f.device_type == "catastrophizing"]
        assert len(cats) >= 1, (
            "catastrophizing not detected in headline containing "
            "'Existential Threat'."
        )


class TestEntityDetection:
    """Verify entity extraction on this article."""

    def test_meta_cluster_dominant(self):
        entities = detect_entities(ARTICLE_BODY)
        meta_count = sum(1 for e in entities if e.cluster == "Meta")
        assert meta_count >= 10, (
            f"Expected at least 10 Meta cluster mentions, got {meta_count}"
        )

    def test_google_detected(self):
        entities = detect_entities(ARTICLE_BODY)
        google = [e for e in entities if e.cluster == "Google"]
        assert len(google) >= 1, "Google entity not detected"

    def test_section_230_detected(self):
        entities = detect_entities(ARTICLE_BODY)
        s230 = [e for e in entities if e.canonical_name == "Section 230"]
        assert len(s230) >= 1, "Section 230 entity not detected"

    def test_ftc_detected(self):
        entities = detect_entities(ARTICLE_BODY)
        ftc = [e for e in entities if "FTC" in e.entity]
        assert len(ftc) >= 1, "FTC entity not detected"

    def test_attorneys_general_detected(self):
        entities = detect_entities(ARTICLE_BODY)
        ag = [e for e in entities if e.cluster == "State Attorneys General"]
        assert len(ag) >= 1, "State Attorneys General cluster not detected"


class TestFramingSummary:
    """Overall framing balance for the article."""

    def test_scale_magnitude_prominent(self):
        framings = detect_framing_devices(ARTICLE_BODY)
        summary = summarize_framing(framings)
        assert summary.get("scale_magnitude", 0) >= 5, (
            "Expected at least 5 scale_magnitude devices in a $1.4T article"
        )

    def test_loaded_language_prominent(self):
        framings = detect_framing_devices(ARTICLE_BODY)
        summary = summarize_framing(framings)
        assert summary.get("loaded_language", 0) >= 5, (
            "Expected at least 5 loaded_language devices (exploiting, "
            "whopping, staggering, plagued, deceptive, watershed, hooked)"
        )

    def test_no_false_positive_guilt_by_association(self):
        framings = detect_framing_devices(ARTICLE_BODY)
        gba = [f for f in framings if f.device_type == "guilt_by_association"]
        assert len(gba) == 0, (
            "Unexpected guilt_by_association in a straight litigation report"
        )
