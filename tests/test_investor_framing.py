"""Tests for investor-media framing patterns and ticker entity detection.

Added Jul 7, 2026 — Type A article deep dive on Motley Fool
"Did Meta Overbuy AI Compute, or Is the Market Asking the Wrong Question?"
"""

import re

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import (
    _DEVICE_PATTERNS,
    detect_framing_devices,
)


# ── Entity detection: ticker symbols ──────────────────────────────────────

class TestTickerDetection:
    """Verify stock ticker symbols are resolved to their parent clusters."""

    def test_nvda_ticker_detected_as_nvidia(self):
        text = "Nvidia (NVDA +0.62%) systems are in high demand."
        results = detect_entities(text)
        nvda = [r for r in results if r.entity == "NVDA"]
        assert len(nvda) == 1
        assert nvda[0].cluster == "Nvidia"

    def test_meta_ticker_detected(self):
        text = "Meta Platforms (META +2.59%) is exploring cloud compute."
        results = detect_entities(text)
        meta = [r for r in results if r.entity == "META"]
        assert len(meta) == 1
        assert meta[0].cluster == "Meta"

    def test_rubin_platform_detected_as_nvidia(self):
        text = "Meta keeps fighting for Rubin, and future Nvidia platforms."
        results = detect_entities(text)
        rubin = [r for r in results if r.entity == "Rubin"]
        assert len(rubin) == 1
        assert rubin[0].cluster == "Nvidia"

    def test_rubin_and_later_detected(self):
        text = "commitments for Rubin, and later Nvidia platforms"
        results = detect_entities(text)
        rubin = [r for r in results if r.entity == "Rubin"]
        assert len(rubin) == 1

    def test_rubin_without_context_not_detected(self):
        """Rubin without Nvidia-related context should not be detected
        (to avoid false positives on the common surname)."""
        text = "Senator Rubin introduced the legislation today."
        results = detect_entities(text)
        rubin = [r for r in results if r.entity == "Rubin"]
        assert len(rubin) == 0

    def test_blackwell_platform_detected(self):
        text = "The Blackwell platform delivers 30x inference speedup."
        results = detect_entities(text)
        bw = [r for r in results if r.entity == "Blackwell"]
        assert len(bw) == 1
        assert bw[0].cluster == "Nvidia"


# ── Framing: narrative_reframing ──────────────────────────────────────────

class TestNarrativeReframing:
    """Verify narrative_reframing framing device patterns."""

    def test_pattern_registered(self):
        assert "narrative_reframing" in _DEVICE_PATTERNS

    def test_fair_but_incomplete(self):
        text = "That concern is fair. It is also incomplete."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_lazy_version_says(self):
        text = "The lazy version says every company needs every GPU forever."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_story_too_simple(self):
        text = "the overbought story is too simple."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_better_question_is(self):
        text = "The better question is whether Meta still chases the next cycle."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_real_question_is(self):
        text = "The real question is who benefits from this arrangement."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_no_false_positive_on_simple_adjective(self):
        """A simple use of 'better' without a reframing target should not fire."""
        text = "This phone has a better camera than the last model."
        devices = detect_framing_devices(text)
        nr = [d for d in devices if d.device_type == "narrative_reframing"]
        assert len(nr) == 0

    def test_valid_but_misleading(self):
        text = "That argument is valid. It is also misleading."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types

    def test_easy_version_says(self):
        text = "The easy reading is that the company overspent."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "narrative_reframing" in types


# ── Framing: dismissive_qualifier ─────────────────────────────────────────

class TestDismissiveQualifier:
    """Verify dismissive_qualifier framing device patterns."""

    def test_pattern_registered(self):
        assert "dismissive_qualifier" in _DEVICE_PATTERNS

    def test_easy_worry(self):
        text = "That gives investors an easy worry."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "dismissive_qualifier" in types

    def test_lazy_version(self):
        text = "The lazy version says Meta bought too much."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "dismissive_qualifier" in types

    def test_convenient_narrative(self):
        text = "That is a convenient narrative for the bears."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "dismissive_qualifier" in types

    def test_knee_jerk_response(self):
        text = "The knee-jerk response is to sell."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "dismissive_qualifier" in types

    def test_no_false_positive_on_neutral_adjective(self):
        text = "The careful analysis suggests a different conclusion."
        devices = detect_framing_devices(text)
        dq = [d for d in devices if d.device_type == "dismissive_qualifier"]
        assert len(dq) == 0


# ── Framing: bull_bear_structuring ────────────────────────────────────────

class TestBullBearStructuring:
    """Verify bull_bear_structuring framing device patterns."""

    def test_pattern_registered(self):
        assert "bull_bear_structuring" in _DEVICE_PATTERNS

    def test_what_would_support_thesis(self):
        text = "What Would Support the Thesis?"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_what_would_break_thesis(self):
        text = "What Would Break the Thesis?"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_bull_case_gets_stronger(self):
        text = "The bull case gets stronger if Meta keeps acting aggressively."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_bear_case_gets_stronger(self):
        text = "The bear case gets stronger if Meta's language shifts."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_first_signal_would_be(self):
        text = "The first signal would be sustained infrastructure guidance."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_clearest_warning_would_be(self):
        text = "The clearest warning would be a structural slowdown."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_conditional_narrative_judgment(self):
        text = (
            "If Meta keeps chasing the newest systems with urgency, "
            "the overbought narrative is incomplete."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "bull_bear_structuring" in types

    def test_no_false_positive_on_plain_conditional(self):
        """A plain 'if' without a narrative judgment should not fire."""
        text = "If the weather is nice, we should go outside."
        devices = detect_framing_devices(text)
        bb = [d for d in devices if d.device_type == "bull_bear_structuring"]
        assert len(bb) == 0


# ── Integration: full article analysis ────────────────────────────────────

class TestMotleyFoolArticle:
    """Integration tests against the Motley Fool Meta compute article."""

    @pytest.fixture
    def article_text(self):
        import os
        path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "motleyfool_meta_overbuy_compute_2026_07_07_article.txt",
        )
        if not os.path.exists(path):
            pytest.skip("Article text not available")
        with open(path) as f:
            return f.read()

    def test_entity_count_increased(self, article_text):
        """With ticker + Rubin, should detect >45 mentions."""
        results = detect_entities(article_text)
        assert len(results) >= 45

    def test_nvda_detected_in_article(self, article_text):
        results = detect_entities(article_text)
        nvda = [r for r in results if r.entity == "NVDA"]
        assert len(nvda) >= 1

    def test_rubin_detected_in_article(self, article_text):
        results = detect_entities(article_text)
        rubin = [r for r in results if r.entity == "Rubin"]
        assert len(rubin) >= 2  # appears 3 times in article

    def test_framing_diversity(self, article_text):
        """Should detect at least 4 distinct framing device types."""
        devices = detect_framing_devices(article_text)
        types = set(d.device_type for d in devices)
        assert len(types) >= 4

    def test_new_patterns_present(self, article_text):
        devices = detect_framing_devices(article_text)
        types = set(d.device_type for d in devices)
        assert "narrative_reframing" in types
        assert "dismissive_qualifier" in types
        assert "bull_bear_structuring" in types

    def test_total_framing_count_increased(self, article_text):
        """Should detect significantly more framing devices than the
        original 6 (was: 4× scale_magnitude + 2× analogy_metaphor)."""
        devices = detect_framing_devices(article_text)
        assert len(devices) >= 20
