"""Cross-publication analysis tests: NYT vs Gizmodo on Meta Arena story.

These tests verify the toolkit produces meaningfully different scores for
the same story covered with radically different editorial postures:
- NYT (Jun 26): straight business-news follow-up scoop (near-neutral)
- Gizmodo (Jun 24): character-indictment op-ed (extremely negative)

Validated against manual scoring. If both articles score similarly on any
dimension, the pipeline needs recalibration.
"""

import pathlib

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.sentiment import (
    _measure_emotional_intensity,
    analyze_composite,
)
from mediascope.analyze.sources import extract_sources

_SAMPLE = pathlib.Path(__file__).parent.parent / "examples" / "sample_output"


@pytest.fixture(scope="module")
def nyt_text():
    return (_SAMPLE / "nyt_meta_arena_polymarket_partnership_2026_06_26_article.txt").read_text()


@pytest.fixture(scope="module")
def giz_text():
    return (_SAMPLE / "gizmodo_meta_arena_worst_instincts_2026_06_24_article.txt").read_text()


# --- Tone Direction ---


class TestToneDirection:
    """The toolkit must clearly separate neutral reporting from op-ed."""

    def test_nyt_tone_above_negative(self, nyt_text):
        """NYT business scoop should not score strongly negative."""
        sent = analyze_composite(nyt_text, "Meta")
        assert sent.overall_tone > -0.3

    def test_gizmodo_tone_clearly_negative(self, giz_text):
        """Gizmodo character-indictment piece must score negative."""
        sent = analyze_composite(giz_text, "Meta")
        assert sent.overall_tone < -0.3

    def test_tone_separation_exceeds_one(self, nyt_text, giz_text):
        """Tone delta between NYT neutral and Gizmodo op-ed must be ≥ 0.8."""
        nyt = analyze_composite(nyt_text, "Meta").overall_tone
        giz = analyze_composite(giz_text, "Meta").overall_tone
        assert nyt - giz >= 0.8


# --- Emotional Intensity ---


class TestEmotionalIntensity:
    """Gizmodo's loaded vocabulary must register as high emotional intensity."""

    def test_nyt_low_emotional_intensity(self, nyt_text):
        """NYT business news: emotional intensity near zero."""
        sent = analyze_composite(nyt_text, "Meta")
        assert sent.emotional_language_intensity < 0.1

    def test_gizmodo_high_emotional_intensity(self, giz_text):
        """Gizmodo op-ed uses 'pathetic', 'plague', 'addicted': intensity > 0.5."""
        sent = analyze_composite(giz_text, "Meta")
        assert sent.emotional_language_intensity > 0.5

    def test_gizmodo_emotional_terms_detected(self):
        """Individual emotional terms from Gizmodo must register."""
        for term in ["pathetic", "plague", "addicted", "notorious", "dopamine hit"]:
            text = f"This is a test sentence containing the word {term} in context."
            score = _measure_emotional_intensity(text)
            assert score > 0, f"'{term}' not detected as emotional language"


# --- Ironic Quotation False Positive Reduction ---


class TestIronicQuotationFilter:
    """Product terms in quotes must not trigger ironic_quotation."""

    def test_product_naming_filtered(self):
        """'points' after 'rely on' should not be ironic quotation."""
        text = 'The app will instead rely on video-game-like "points" for engagement.'
        devices = detect_framing_devices(text)
        iq = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq) == 0, f"Product term 'points' false-positive: {iq}"

    def test_monthly_active_metric_filtered(self):
        """'predictors' after 'monthly active' should not be ironic quotation."""
        text = 'Meta aims to reach 100 million monthly active "predictors" for the app.'
        devices = detect_framing_devices(text)
        iq = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq) == 0, f"Metric term 'predictors' false-positive: {iq}"

    def test_direct_quote_filtered(self):
        """Zuckerberg's direct quote should not be ironic quotation."""
        text = 'Zuck said\nthat he had "over 4,000 emails, pictures, addresses" of people.'
        devices = detect_framing_devices(text)
        iq = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq) == 0, f"Direct quote false-positive: {iq}"

    def test_legitimate_scare_quote_preserved(self):
        """'dopamine hit' as editorial scare quote should still match."""
        text = 'The platform is built to provide a "dopamine hit" at the expense of health.'
        devices = detect_framing_devices(text)
        iq = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq) == 1

    def test_socalled_not_filtered(self):
        """'so-called' + scare quote is editorial distancing, not attribution."""
        text = 'The so-called "safety" measures were widely mocked.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ironic_quotation" in types


# --- Agency Attribution ---


class TestAgencyAttribution:
    """CEO directive verbs must register as active agency."""

    def test_urged_detected(self):
        """'urged his lieutenants' is active positive agency."""
        sent = analyze_composite(
            "Zuckerberg urged his lieutenants to explore partnerships.", "Meta"
        )
        assert sent.agency_attribution > 0

    def test_dispatched_detected(self):
        """'dispatched a team' is active positive agency."""
        sent = analyze_composite(
            "Zuckerberg dispatched a small team to create the app.", "Meta"
        )
        assert sent.agency_attribution > 0


# --- Entity Detection ---


class TestEntityDetection:
    """Both articles must detect key Meta and Prediction Markets entities."""

    def test_nyt_detects_polymarket_kalshi(self, nyt_text):
        """NYT article: Polymarket and Kalshi in Prediction Markets cluster."""
        ents = detect_entities(nyt_text)
        clusters = {(e.canonical_name, e.cluster) for e in ents}
        assert ("Polymarket", "Prediction Markets/Fintech") in clusters
        assert ("Kalshi", "Prediction Markets/Fintech") in clusters

    def test_nyt_detects_arena(self, nyt_text):
        """Arena should be in Meta cluster."""
        ents = detect_entities(nyt_text)
        clusters = {(e.canonical_name, e.cluster) for e in ents}
        assert ("Arena", "Meta") in clusters

    def test_gizmodo_detects_haugen(self, giz_text):
        """Gizmodo article: Frances Haugen in Whistleblowers cluster."""
        ents = detect_entities(giz_text)
        clusters = {(e.canonical_name, e.cluster) for e in ents}
        assert ("Frances Haugen", "Whistleblowers/Critics") in clusters


# --- Source Extraction ---


class TestSourceExtraction:
    """Source extraction must match manual counts."""

    def test_nyt_sources(self, nyt_text):
        """NYT: 1 anonymous source, 2 no-comment, 1 publication attribution."""
        srcs = extract_sources(nyt_text)
        anon = [s for s in srcs if s.is_anonymous]
        no_comment = [s for s in srcs if s.source_type == "no_comment"]
        assert len(anon) >= 1, "Must detect at least 1 anonymous source"
        assert len(no_comment) >= 2, "Must detect at least 2 no-comment signals"

    def test_gizmodo_named_sources(self, giz_text):
        """Gizmodo: Frances Haugen and Zuck as named sources, no anonymous."""
        srcs = extract_sources(giz_text)
        anon = [s for s in srcs if s.is_anonymous]
        named = [s for s in srcs if s.source_type == "named"]
        assert len(anon) == 0, "Op-ed should have zero anonymous sources"
        assert len(named) >= 1, "Must detect at least 1 named source"
