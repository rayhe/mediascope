"""Tests for patterns added in the Barron's Meta AI Splurge / J.P. Morgan
article deep dive (Jul 13, 2026).

Covers:
- pathologizing_metaphor: "splurge" and variants
- competitive_deficit: "lags behind ... compared with [competitors]" bridge
- entity detection: J.P. Morgan with periods, Epoch AI
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities


def _types(text: str) -> set[str]:
    """Return the set of device_type strings detected in *text*."""
    return {d.device_type for d in detect_framing_devices(text)}


def _entity_clusters(text: str) -> dict[str, str]:
    """Return {canonical_name: cluster} from detected entities."""
    return {e.canonical_name: e.cluster for e in detect_entities(text)}


# ── pathologizing_metaphor: splurge ──────────────────────────────────────────


class TestSplurgePathologizing:
    """'splurge' and variants should fire pathologizing_metaphor."""

    def test_ai_splurge_continues(self):
        text = "Meta AI Splurge Continues"
        assert "pathologizing_metaphor" in _types(text)

    def test_spending_splurge(self):
        text = "the company's spending splurge"
        assert "pathologizing_metaphor" in _types(text)

    def test_splurge_on(self):
        text = "splurge on infrastructure"
        assert "pathologizing_metaphor" in _types(text)

    def test_splurged_on_data_centers(self):
        text = "Meta splurged on new data centers"
        assert "pathologizing_metaphor" in _types(text)

    def test_splurging_on_ai(self):
        text = "the company is splurging on AI"
        assert "pathologizing_metaphor" in _types(text)

    def test_headline_splurge(self):
        """The actual headline from the Barron's article."""
        text = "Meta AI Splurge Continues and J.P. Morgan Is Worried for the Stock"
        assert "pathologizing_metaphor" in _types(text)


# ── competitive_deficit: compared with bridge ────────────────────────────────


class TestCompetitiveDeficitComparedWith:
    """'lags behind ... compared with [competitors]' should fire."""

    def test_barrons_actual_sentence(self):
        """The exact sentence from the Barron's article."""
        text = (
            "concerns his company lags behind in cutting-edge models "
            "compared with the likes of ChatGPT-developer OpenAI or "
            "Claude maker Anthropic"
        )
        assert "competitive_deficit" in _types(text)

    def test_lags_behind_compared_to(self):
        text = "the company lags behind compared to Google and Anthropic"
        assert "competitive_deficit" in _types(text)

    def test_lagging_behind_relative_to(self):
        text = "Meta is lagging behind relative to OpenAI in model quality"
        assert "competitive_deficit" in _types(text)

    def test_fallen_behind_measured_against(self):
        text = "the firm has fallen behind when measured against Microsoft"
        assert "competitive_deficit" in _types(text)

    def test_falling_behind_compared_with(self):
        text = "falling behind in key areas compared with Anthropic"
        assert "competitive_deficit" in _types(text)

    def test_trailing_stacked_against(self):
        text = "trailing far behind when stacked against Google and OpenAI"
        assert "competitive_deficit" in _types(text)

    def test_no_false_positive_compared_favorably(self):
        """'compared with' without a deficit verb should not fire."""
        text = "Meta performed well compared with Anthropic"
        assert "competitive_deficit" not in _types(text)


# ── entity detection: J.P. Morgan variants ───────────────────────────────────


class TestJPMorganEntityDetection:
    """J.P. Morgan with periods should detect as Financial Services."""

    def test_jp_morgan_with_periods(self):
        ents = _entity_clusters("J.P. Morgan analyst Doug Anmuth")
        assert "J.P. Morgan" in ents
        assert ents["J.P. Morgan"] == "Financial Services"

    def test_jp_morgan_no_space(self):
        ents = _entity_clusters("J.P.Morgan reiterated a Neutral rating")
        assert "J.P.Morgan" in ents
        assert ents["J.P.Morgan"] == "Financial Services"

    def test_jpmorgan_still_works(self):
        ents = _entity_clusters("JPMorgan analyst said")
        assert "JPMorgan" in ents
        assert ents["JPMorgan"] == "Financial Services"

    def test_jp_morgan_no_periods_still_works(self):
        ents = _entity_clusters("JP Morgan upgraded the stock")
        assert "JP Morgan" in ents
        assert ents["JP Morgan"] == "Financial Services"


# ── entity detection: Epoch AI ───────────────────────────────────────────────


class TestEpochAIEntityDetection:
    """Epoch AI should detect as Financial Services (research firm)."""

    def test_epoch_ai_detection(self):
        ents = _entity_clusters("analysis firm Epoch AI estimates")
        assert "Epoch AI" in ents
        assert ents["Epoch AI"] == "Financial Services"

    def test_epoch_ai_in_sentence(self):
        text = (
            "A typical one-gigawatt AI data center requires $38 billion "
            "according to analysis firm Epoch AI"
        )
        ents = _entity_clusters(text)
        assert "Epoch AI" in ents
