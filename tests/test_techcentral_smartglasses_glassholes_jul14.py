"""Tests for TechCentral smart glasses privacy editorial (Jul 14, 2026).

Type A article deep dive — opinion/editorial genre.  Validates fixes for:
- Negated loaded_language suppression ("not a gimmick")
- Editorial conclusion ironic_quotation suppression ("no")
- Source extraction false positive suppression ("Name Tag", "Balance", "Name")
- New entity clusters (Warby Parker, Be My Eyes, BBC)
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.sources import extract_sources

_ARTICLE_PATH = (
    Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "techcentral_smartglasses_glassholes_2026_07_14_article.txt"
)


@pytest.fixture(scope="module")
def article_text() -> str:
    return _ARTICLE_PATH.read_text()


@pytest.fixture(scope="module")
def framing_devices(article_text):
    return detect_framing_devices(article_text)


@pytest.fixture(scope="module")
def framing_summary(framing_devices):
    return summarize_framing(framing_devices)


@pytest.fixture(scope="module")
def entities(article_text):
    return detect_entities(article_text)


@pytest.fixture(scope="module")
def sources(article_text):
    return extract_sources(article_text)


@pytest.fixture(scope="module")
def sentiment(article_text):
    return analyze_composite(article_text)


# ── Sentiment ─────────────────────────────────────────────────────────────

class TestSentiment:
    def test_tone_is_negative(self, sentiment):
        """Opinion editorial about privacy threat should register negative."""
        assert sentiment.overall_tone < 0

    def test_emotional_intensity_moderate_to_high(self, sentiment):
        """Editorial uses emotive language — should be above 0.4."""
        assert sentiment.emotional_language_intensity > 0.4

    def test_agency_attribution_present(self, sentiment):
        """Meta is assigned agency for privacy decisions."""
        assert sentiment.agency_attribution > 0.3

    def test_no_anonymous_sources(self, sentiment):
        """Opinion piece has no anonymous sources."""
        assert sentiment.anonymous_source_ratio == 0.0


# ── Entities ──────────────────────────────────────────────────────────────

class TestEntities:
    def test_meta_dominant(self, entities):
        """Meta should be the most mentioned entity."""
        c = Counter(e.canonical_name for e in entities)
        assert c.most_common(1)[0][0] == "Meta"
        assert c["Meta"] >= 8

    def test_warby_parker_detected(self, entities):
        """Warby Parker mentioned as smart glasses competitor."""
        names = {e.canonical_name for e in entities}
        assert "Warby Parker" in names

    def test_be_my_eyes_detected(self, entities):
        """Be My Eyes mentioned as Meta accessibility partner."""
        names = {e.canonical_name for e in entities}
        assert "Be My Eyes" in names

    def test_bbc_detected(self, entities):
        """BBC mentioned as investigative source."""
        names = {e.canonical_name for e in entities}
        assert "BBC" in names

    def test_google_detected(self, entities):
        names = {e.canonical_name for e in entities}
        assert "Google" in names

    def test_snap_detected(self, entities):
        names = {e.canonical_name for e in entities}
        assert "Snap" in names or "Spectacles" in names

    def test_samsung_detected(self, entities):
        names = {e.canonical_name for e in entities}
        assert "Samsung" in names

    def test_aclu_detected(self, entities):
        """American Civil Liberties Union mentioned in privacy coalition."""
        names = {e.canonical_name for e in entities}
        assert "American Civil Liberties Union" in names


# ── Framing Devices ───────────────────────────────────────────────────────

class TestFraming:
    def test_loaded_language_count(self, framing_summary):
        """Should detect multiple loaded language instances."""
        assert framing_summary.get("loaded_language", 0) >= 6

    def test_gimmick_not_loaded_language(self, framing_devices):
        """'That is not a gimmick' — negated loaded term should be suppressed."""
        gimmick_hits = [
            d for d in framing_devices
            if d.device_type == "loaded_language"
            and "gimmick" in d.evidence_text.lower()
        ]
        assert len(gimmick_hits) == 0, (
            "Negated 'gimmick' in 'That is not a gimmick' should not be "
            "flagged as loaded_language"
        )

    def test_no_ironic_quotation_false_positive(self, framing_devices):
        """Editorial conclusion '"no"' should not be flagged as ironic_quotation."""
        no_hits = [
            d for d in framing_devices
            if d.device_type == "ironic_quotation"
            and d.evidence_text.strip(' "\u201c\u201d') == "no"
        ]
        assert len(no_hits) == 0, (
            "Editorial conclusion 'should be \"no\"' is sincere, not ironic"
        )

    def test_glassholes_ironic_quotation_detected(self, framing_devices):
        """'glassholes' should be detected as ironic_quotation."""
        hits = [
            d for d in framing_devices
            if d.device_type == "ironic_quotation"
            and "glasshole" in d.evidence_text.lower()
        ]
        assert len(hits) >= 1

    def test_surveillance_loaded_language(self, framing_devices):
        """'surveillance device' is loaded language."""
        hits = [
            d for d in framing_devices
            if d.device_type == "loaded_language"
            and "surveillance" in d.evidence_text.lower()
        ]
        assert len(hits) >= 1

    def test_confession_framing_detected(self, framing_summary):
        """'itself has admitted that' is confession framing."""
        assert framing_summary.get("confession_framing", 0) >= 1

    def test_consent_alarm_detected(self, framing_summary):
        """'without their knowledge' is consent alarm."""
        assert framing_summary.get("consent_alarm", 0) >= 1

    def test_litigation_framing_detected(self, framing_summary):
        """'sued Meta' is litigation framing."""
        assert framing_summary.get("litigation_framing", 0) >= 1

    def test_trend_bundling_detected(self, framing_summary):
        """Industry catching up = trend bundling."""
        assert framing_summary.get("trend_bundling", 0) >= 1


# ── Source Extraction ─────────────────────────────────────────────────────

class TestSources:
    def test_no_false_positive_sources(self, sources):
        """Opinion piece with no direct quotes should extract 0 sources."""
        assert len(sources) == 0, (
            f"Expected 0 sources for opinion editorial, got: "
            f"{[s.name for s in sources]}"
        )

    def test_name_tag_not_extracted(self, sources):
        """Product name 'Name Tag' should not be extracted as a source."""
        names = {s.name for s in sources}
        assert "Name Tag" not in names
        assert "Name" not in names

    def test_balance_not_extracted(self, sources):
        """Sentence-opening abstract noun 'Balance' should not be a source."""
        names = {s.name for s in sources}
        assert "Balance" not in names


# ── Negation Filter Regression Tests ──────────────────────────────────────

class TestNegationFilter:
    """Test the loaded_language negation filter with synthetic examples."""

    @pytest.mark.parametrize("text,term", [
        ("That is not a gimmick; it is life-changing.", "gimmick"),
        ("This was never a stunt — the results speak for themselves.", "stunt"),
        ("It is hardly a surveillance device when the user controls it.", "surveillance"),
        ("The technology isn't a threat to anyone.", "threat"),
        ("Far from a failure, the project succeeded.", "failure"),
    ])
    def test_negated_loaded_terms_suppressed(self, text, term):
        """Negated loaded terms should not be detected as loaded_language."""
        devices = detect_framing_devices(text)
        hits = [
            d for d in devices
            if d.device_type == "loaded_language"
            and term in d.evidence_text.lower()
        ]
        assert len(hits) == 0, (
            f"Negated '{term}' should be suppressed in: {text}"
        )


# ── Editorial Conclusion Filter Regression Tests ─────────────────────────

class TestEditorialConclusionFilter:
    """Test the ironic_quotation editorial conclusion filter."""

    @pytest.mark.parametrize("text", [
        'The answer to this question should be "no".',
        'The answer must be "yes" — there is no alternative.',
        'The response ought to be "never".',
    ])
    def test_editorial_conclusion_suppressed(self, text):
        """Single-word quotes in editorial conclusions should not be ironic_quotation."""
        devices = detect_framing_devices(text)
        hits = [
            d for d in devices
            if d.device_type == "ironic_quotation"
        ]
        assert len(hits) == 0, (
            f"Editorial conclusion should not be ironic_quotation in: {text}"
        )
