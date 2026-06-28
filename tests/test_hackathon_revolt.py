"""Regression tests for Wired hackathon employee revolt article analysis.

Tests added in the Jun 28 15:00 PT Type A iteration covering:
- Ime Archibong entity detection
- Workplace-discontent emotional language terms
- Social proof amplification framing device
- AI hackathon topic classification
"""

import re

import pytest

from mediascope.analyze.entities import detect_entities, get_entity_distribution
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.sentiment import (
    EMOTIONAL_LANGUAGE,
    analyze_composite,
    measure_outsourced_intensity,
)
from mediascope.analyze.topics import classify_topic


# --- Fixtures ---

HACKATHON_ARTICLE = """\
Meta CEO Mark Zuckerberg's internal announcement on Friday about a "large" \
companywide AI hackathon next month quickly sparked frustration and disbelief \
among employees. In internal messages seen by WIRED, some workers wrote that \
added responsibilities in the wake of recent mass layoffs at the tech giant \
had left them with little time to join such ancillary activities. \
Ime Archibong, a vice president of product management at Meta, later shared \
additional details about the event, which he said would take place from July \
14 to July 16 and focus "exclusively on AI Innovation." \
Archibong's post drew swift pushback from several employees, who responded \
with angry messages and sarcastic memes. "I'm not sure that this company \
supports a hackathon culture anymore," one employee wrote in a comment that \
drew more than 200 thumbs-up and heart reactions. Dozens of people also \
reacted with laughs and thumbs-up to a meme. Meta declined to comment.\
"""


# --- Entity tests ---


class TestImeArchibongEntity:
    """Ime Archibong should be detected as a Meta cluster entity."""

    def test_archibong_detected(self):
        entities = detect_entities(HACKATHON_ARTICLE)
        archibong = [e for e in entities if "Archibong" in e.canonical_name]
        assert len(archibong) >= 1, "Ime Archibong should be detected"

    def test_archibong_in_meta_cluster(self):
        entities = detect_entities(HACKATHON_ARTICLE)
        archibong = [e for e in entities if "Archibong" in e.canonical_name]
        for e in archibong:
            assert e.cluster == "Meta", (
                f"Archibong should be in Meta cluster, got {e.cluster}"
            )


# --- Emotional language tests ---


class TestWorkplaceDiscontentTerms:
    """Workplace-discontent terms should be in EMOTIONAL_LANGUAGE list."""

    @pytest.mark.parametrize(
        "term",
        [
            "disappointing",
            "disappointed",
            "demoralizing",
            "demoralized",
            "discouraged",
            "disbelief",
            "skeptical",
            "sarcastic",
            "pushback",
            "revolt",
            "overburdened",
            "distress",
            "tone-deaf",
            "performative",
        ],
    )
    def test_term_in_emotional_language(self, term):
        assert term in EMOTIONAL_LANGUAGE, (
            f"'{term}' should be in EMOTIONAL_LANGUAGE list"
        )

    def test_hackathon_article_emotional_intensity_above_threshold(self):
        """With workplace-discontent terms, intensity should be non-trivial."""
        comp = analyze_composite(HACKATHON_ARTICLE)
        assert comp.emotional_language_intensity > 0.3, (
            f"Expected intensity > 0.3, got {comp.emotional_language_intensity}"
        )


# --- Social proof amplification tests ---


class TestSocialProofAmplification:
    """Social proof amplification framing device detection."""

    def test_detects_reaction_count(self):
        text = 'a comment that drew more than 200 thumbs-up and heart reactions'
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "social_proof_amplification" in types

    def test_detects_dozens_reacted(self):
        text = "Dozens of people also reacted with laughs"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "social_proof_amplification" in types

    def test_detects_in_hackathon_article(self):
        devices = detect_framing_devices(HACKATHON_ARTICLE)
        social_proof = [
            d for d in devices if d.device_type == "social_proof_amplification"
        ]
        assert len(social_proof) >= 2, (
            f"Expected >= 2 social proof amplification devices, got {len(social_proof)}"
        )

    def test_in_framing_summary(self):
        devices = detect_framing_devices(HACKATHON_ARTICLE)
        summary = summarize_framing(devices)
        assert "social_proof_amplification" in summary


# --- Topic classification tests ---


class TestAIHackathonTopic:
    """AI hackathon/Innovation should trigger ai_development topic."""

    def test_ai_development_detected(self):
        topics = classify_topic(HACKATHON_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names, (
            f"ai_development not detected. Topics: {topic_names}"
        )

    def test_ai_innovation_keyword_matched(self):
        topics = classify_topic(HACKATHON_ARTICLE)
        ai_dev = [t for t in topics if t.topic == "ai_development"]
        assert ai_dev, "ai_development topic should be present"
        keywords = ai_dev[0].matched_keywords
        assert any("AI" in k for k in keywords), (
            f"Expected an AI keyword match, got {keywords}"
        )


# --- Composite sentiment tests ---


class TestHackathonSentiment:
    """Composite sentiment should correctly identify negative tone."""

    def test_framing_corrected_negative(self):
        """On the full article, framing correction should produce negative tone."""
        import pathlib

        article_path = pathlib.Path(__file__).parent.parent / (
            "examples/sample_output/"
            "wired_meta_hackathon_employee_revolt_2026_06_13_article.txt"
        )
        if not article_path.exists():
            pytest.skip("Full article file not present")
        full_text = article_path.read_text()
        comp = analyze_composite(full_text)
        assert comp.overall_tone < 0, (
            f"Overall tone should be negative, got {comp.overall_tone}"
        )

    def test_high_anonymous_source_ratio(self):
        comp = analyze_composite(HACKATHON_ARTICLE)
        assert comp.anonymous_source_ratio > 0.5, (
            f"Anonymous source ratio should be > 0.5, got {comp.anonymous_source_ratio}"
        )

    def test_negative_agency(self):
        comp = analyze_composite(HACKATHON_ARTICLE)
        assert comp.agency_attribution < 0, (
            f"Agency should be negative, got {comp.agency_attribution}"
        )
