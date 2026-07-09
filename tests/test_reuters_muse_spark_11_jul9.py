"""Tests for Reuters Muse Spark 1.1 article analysis (Jul 9, 2026).

Validates three improvements discovered during Type A deep dive:
1. pathologizing_metaphor false positive suppression on neutral "intervention"
2. comparative_framing detection for pricing comparisons
3. loaded_language detection for competitive dramatization
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import (
    NEGATIVE_COMPARISON,
    POSITIVE_COMPARISON,
    analyze_composite,
)


# ---------------------------------------------------------------------------
# Fix 1: pathologizing_metaphor — neutral "intervention" suppression
# ---------------------------------------------------------------------------

class TestPathologizingMetaphorIntervention:
    """Suppress 'intervention' in neutral technical contexts."""

    def test_less_human_intervention_suppressed(self):
        """'less human intervention' is neutral process language, not pathology."""
        text = (
            "The new system requires less human intervention "
            "thanks to automated quality checks."
        )
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert not patho, (
            f"'less human intervention' should not trigger pathologizing_metaphor, "
            f"got: {[d.evidence for d in patho]}"
        )

    def test_without_intervention_suppressed(self):
        """'without intervention' is neutral — should not fire."""
        text = "The pipeline runs end-to-end without intervention from engineers."
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert not patho

    def test_minimal_intervention_suppressed(self):
        """'minimal intervention' is neutral — should not fire."""
        text = "Deploying with minimal intervention from the ops team."
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert not patho

    def test_no_intervention_suppressed(self):
        """'no intervention required' is neutral — should not fire."""
        text = "The process completes with no intervention required."
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert not patho

    def test_reduced_intervention_suppressed(self):
        """'reduced intervention' is neutral — should not fire."""
        text = "AI agents dramatically reduced intervention from human operators."
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert not patho

    def test_genuine_intervention_preserved(self):
        """'staged an intervention' is genuine pathology framing — must fire."""
        text = (
            "Regulators staged an intervention, forcing Meta to address "
            "its data hoarding compulsion."
        )
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert patho, "genuine pathologizing 'intervention' should still be detected"

    def test_needs_intervention_preserved(self):
        """'needs an intervention' is pathology framing — must fire."""
        text = "The company's spending habits suggest it needs an intervention."
        devices = detect_framing_devices(text)
        patho = [d for d in devices if d.device_type == "pathologizing_metaphor"]
        assert patho, "pathologizing 'needs an intervention' should still be detected"


# ---------------------------------------------------------------------------
# Fix 2: comparative_framing — pricing comparison detection
# ---------------------------------------------------------------------------

class TestPricingComparisonDetection:
    """Pricing phrases should contribute to comparative framing score."""

    def test_priced_above_in_negative_comparison(self):
        assert "priced above" in NEGATIVE_COMPARISON

    def test_more_expensive_in_negative_comparison(self):
        assert "more expensive than" in NEGATIVE_COMPARISON

    def test_above_openai_in_negative_comparison(self):
        assert "above openai" in NEGATIVE_COMPARISON

    def test_priced_below_in_positive_comparison(self):
        assert "priced below" in POSITIVE_COMPARISON

    def test_cheaper_than_in_positive_comparison(self):
        assert "cheaper than" in POSITIVE_COMPARISON

    def test_undercuts_in_positive_comparison(self):
        assert "undercuts" in POSITIVE_COMPARISON

    def test_negative_pricing_comparison_nonzero(self):
        """Text with unfavorable pricing comparison should score negative."""
        text = (
            "Meta priced Muse Spark 1.1 at $1.25 per million input tokens, "
            "above OpenAI's entry-level GPT-5 mini. The premium may deter "
            "budget-conscious developers from adopting the platform."
        )
        result = analyze_composite(text)
        assert result.comparative_framing < 0.0, (
            f"Unfavorable pricing comparison should produce negative "
            f"comparative_framing, got {result.comparative_framing}"
        )

    def test_positive_pricing_comparison_nonzero(self):
        """Text with favorable pricing comparison should score positive."""
        text = (
            "Meta priced Muse Spark 1.1 well below Anthropic's Claude "
            "Sonnet 4.6, making it cheaper than most frontier alternatives."
        )
        result = analyze_composite(text)
        assert result.comparative_framing > 0.0, (
            f"Favorable pricing comparison should produce positive "
            f"comparative_framing, got {result.comparative_framing}"
        )


# ---------------------------------------------------------------------------
# Fix 3: loaded_language — competitive dramatization phrases
# ---------------------------------------------------------------------------

class TestCompetitiveDramatizationLoadedLanguage:
    """Heated/supremacy competitive language should trigger loaded_language."""

    def test_heated_competition_detected(self):
        text = "The release comes amid heated competition for AI supremacy."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert loaded, (
            "'heated competition for AI supremacy' should trigger loaded_language"
        )

    def test_heated_race_detected(self):
        text = "A heated race among chipmakers is driving up prices."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert loaded, "'heated race' should trigger loaded_language"

    def test_ai_supremacy_standalone_detected(self):
        text = "The quest for AI supremacy is reshaping the industry."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert loaded, "'AI supremacy' should trigger loaded_language"

    def test_tech_arms_race_detected(self):
        text = "The tech arms race between Meta and Google continues."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert loaded, "'tech arms race' should trigger loaded_language"


class TestCompetitivePositioningPitting:
    """'Pitting X against Y' and 'close the gap' competitive framing."""

    def test_pitting_against_detected(self):
        text = (
            "Meta released the model at aggressive pricing, pitting it "
            "directly against OpenAI and Anthropic."
        )
        devices = detect_framing_devices(text)
        comp = [d for d in devices if d.device_type == "competitive_positioning"]
        assert comp, "'pitting it directly against' should trigger competitive_positioning"

    def test_pitted_against_detected(self):
        text = "The new chip is pitted squarely against Nvidia's H100."
        devices = detect_framing_devices(text)
        comp = [d for d in devices if d.device_type == "competitive_positioning"]
        assert comp, "'pitted squarely against' should trigger competitive_positioning"

    def test_close_the_gap_detected(self):
        text = "Meta is trying to close the gap with OpenAI in the AI race."
        devices = detect_framing_devices(text)
        comp = [d for d in devices if d.device_type == "competitive_positioning"]
        assert comp, "'close the gap' should trigger competitive_positioning"

    def test_narrow_the_gap_detected(self):
        text = "The update helps narrow the gap between Meta and its rivals."
        devices = detect_framing_devices(text)
        comp = [d for d in devices if d.device_type == "competitive_positioning"]
        assert comp, "'narrow the gap' should trigger competitive_positioning"
