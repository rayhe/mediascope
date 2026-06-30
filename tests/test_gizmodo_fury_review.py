"""Tests for Gizmodo Meta Fury AI Glasses Review analysis (Jun 29, 2026).

Validates toolkit detection against a manually analyzed contradictory review
article: Raymond Wong's "The Worst Company Still Makes the Best Smart Glasses."

Key analytical challenge: the article gives a positive 3.5/5 review score but
wraps it in deeply negative editorial framing about privacy and ethics. VADER
reads the product review language as strongly positive, masking the negative
editorial posture. The contradictory-review framing correction (Path F) must
fire to bring the overall tone into the manually assessed range.

Source: https://gizmodo.com/meta-fury-ai-glasses-review-the-worst-company-still-makes-the-best-smart-glasses-2000777827
"""

from __future__ import annotations

import pathlib

import pytest

ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "gizmodo_meta_fury_review_2026_06_29_article.txt"
)


@pytest.fixture(scope="module")
def article_text() -> str:
    return ARTICLE_PATH.read_text()


@pytest.fixture(scope="module")
def headline(article_text: str) -> str:
    return article_text.strip().split("\n")[0]


# ── Entity detection ──────────────────────────────────────────────────


class TestEntityDetection:
    """Meta Fury, product names, and key players must be detected."""

    def test_meta_fury_detected(self, article_text: str):
        from mediascope.analyze.entities import detect_entities

        entities = detect_entities(article_text)
        fury_mentions = [
            e for e in entities
            if e.canonical_name == "Fury" and e.cluster == "Meta"
        ]
        assert len(fury_mentions) >= 1, (
            "Meta Fury / Fury should be detected as a Meta-cluster entity"
        )

    def test_muse_spark_detected(self, article_text: str):
        from mediascope.analyze.entities import detect_entities

        entities = detect_entities(article_text)
        spark = [e for e in entities if e.canonical_name == "Muse Spark"]
        assert len(spark) >= 1

    def test_key_entities_detected(self, article_text: str):
        from mediascope.analyze.entities import detect_entities

        entities = detect_entities(article_text)
        canonical_names = {e.canonical_name for e in entities}
        for expected in [
            "Andrew Bosworth", "Ray-Ban", "EssilorLuxottica",
            "Kylie Jenner", "Garmin", "Llama 4",
        ]:
            assert expected in canonical_names, (
                f"{expected} should be detected"
            )

    def test_cross_publication_refs_detected(self, article_text: str):
        from mediascope.analyze.entities import detect_entities

        entities = detect_entities(article_text)
        canonical_names = {e.canonical_name for e in entities}
        assert "The New York Times" in canonical_names
        assert "WIRED" in canonical_names

    def test_meta_glasses_models_detected(self, article_text: str):
        from mediascope.analyze.entities import detect_entities

        entities = detect_entities(article_text)
        canonical_names = {e.canonical_name for e in entities}
        assert "Adventurer" in canonical_names, "Adventurer model should be detected"
        assert "Starfire" in canonical_names, "Starfire model should be detected"


# ── Framing devices ──────────────────────────────────────────────────


class TestFramingDevices:
    """Article contains rich framing that the toolkit should detect."""

    def test_loaded_language_detected(self, article_text: str):
        from mediascope.analyze.framing import detect_framing_devices

        devices = detect_framing_devices(article_text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        # Manual count: "ickiness", "surveillance dystopia", "glassholism",
        # "facial recognition" x2, "dormant" code, "crushed" — at least 4
        assert len(loaded) >= 3, (
            f"Expected ≥3 loaded_language devices, got {len(loaded)}"
        )

    def test_rhetorical_question_detected(self, article_text: str):
        from mediascope.analyze.framing import detect_framing_devices

        devices = detect_framing_devices(article_text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) >= 1, "Closing rhetorical question should be detected"

    def test_self_referential_investigation(self, article_text: str):
        from mediascope.analyze.framing import detect_framing_devices

        devices = detect_framing_devices(article_text)
        sri = [
            d for d in devices
            if d.device_type == "self_referential_investigation"
        ]
        assert len(sri) >= 1, (
            "'Wired found' is self-referential investigation framing"
        )


# ── Sentiment dimensions ─────────────────────────────────────────────


class TestSentiment:
    """8-dimension sentiment must capture the contradictory review structure."""

    def test_overall_tone_negative(self, article_text: str, headline: str):
        """Despite 3.5/5 review score, overall editorial tone is negative."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.overall_tone < 0, (
            f"Overall tone should be negative (editorial wrapper dominates), "
            f"got {result.overall_tone:.3f}"
        )

    def test_framing_correction_fires(self, article_text: str, headline: str):
        """Contradictory review framing correction must activate."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.framing_corrected, (
            "Framing correction should fire for this contradictory review. "
            f"Raw tone: {result.raw_tone:.3f}, corrected: {result.overall_tone:.3f}"
        )

    def test_raw_tone_inflated(self, article_text: str, headline: str):
        """VADER's raw tone is inflated by product review language."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.raw_tone > 0.4, (
            f"Raw tone should be inflated positive, got {result.raw_tone:.3f}"
        )

    def test_emotional_intensity_elevated(self, article_text: str, headline: str):
        """Privacy/ethics loaded language drives elevated emotional intensity."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.emotional_language_intensity >= 0.5, (
            f"Emotional intensity should be ≥0.5 with privacy/disgust terms, "
            f"got {result.emotional_language_intensity:.3f}"
        )

    def test_anonymous_source_ratio_zero(self, article_text: str, headline: str):
        """All sources are named or institutional — no anonymous sources."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.anonymous_source_ratio == 0.0

    def test_headline_alignment_positive(self, article_text: str, headline: str):
        """After framing correction, headline-body alignment should be positive."""
        from mediascope.analyze.sentiment import analyze_composite

        result = analyze_composite(article_text, headline=headline)
        assert result.headline_body_alignment > 0, (
            f"Headline 'worst company + best glasses' aligns with body's "
            f"contradictory thesis, got {result.headline_body_alignment:.3f}"
        )


# ── Emotional language terms ─────────────────────────────────────────


class TestEmotionalTerms:
    """New privacy/disgust terms must be in the emotional language list."""

    def test_ick_terms_present(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        terms = set(EMOTIONAL_LANGUAGE)
        for term in ["icky", "ickier", "ickiness", "ick factor"]:
            assert term in terms, f"'{term}' should be in EMOTIONAL_LANGUAGE"

    def test_glassholism_present(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        assert "glassholism" in set(EMOTIONAL_LANGUAGE)

    def test_privacy_minefield_present(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        assert "privacy minefield" in set(EMOTIONAL_LANGUAGE)

    def test_spying_terms_present(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        terms = set(EMOTIONAL_LANGUAGE)
        for term in ["spying", "encroaching", "intrusion", "paranoid"]:
            assert term in terms, f"'{term}' should be in EMOTIONAL_LANGUAGE"


# ── Source extraction ─────────────────────────────────────────────────


class TestSourceExtraction:
    """Andrew Bosworth is the only directly-quoted named source."""

    def test_bosworth_detected(self, article_text: str):
        from mediascope.analyze.sources import extract_sources

        sources = extract_sources(article_text)
        named = [s for s in sources if s.source_type == "named"]
        names = [s.name for s in named]
        assert any("Bosworth" in n for n in names), (
            f"Andrew Bosworth should be detected as named source, got: {names}"
        )
