"""Tests for humanization and surveillance_enumeration framing devices.

These devices were added from analysis of the WSJ Meta AI layoffs article
(Jul 14, 2026) and related coverage. Also tests the censored profanity
extension to emotional_appeal patterns discovered from the Gizmodo celebrity
backlash article (Jul 14, 2026).

Device provenance:
- humanization: WSJ "Meta Workers Accuse It of Using AI to Conduct
  Discriminatory Layoffs" (Jul 14/15, 2026) — timing-of-harm near life events,
  pregnancy context, age-specific vulnerability
- surveillance_enumeration: Same WSJ article — multi-item comma-separated
  lists of monitoring technologies and performance metrics
- censored profanity: Gizmodo "Smart Glasses Backlash Is Reaching New Celebrity
  Heights" (Jul 14, 2026) — "f*ck the glasses"
"""

import pytest

from mediascope.analysis import detect_framing_devices


# ── humanization ──────────────────────────────────────────────────────────

class TestHumanization:
    """Humanization device: emotionally resonant personal biographical detail."""

    def test_timing_of_harm_before_birth(self):
        text = (
            "One employee said she was told she was being laid off two days "
            "before giving birth to her second child."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_timing_of_harm_after_surgery(self):
        text = (
            "The worker learned of his termination just three weeks after "
            "his surgery, while still recovering at home."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_financial_devastation_retirement(self):
        text = (
            "The couple lost $715,000 — nearly all of their retirement "
            "savings — after responding to what appeared to be a legitimate "
            "investment opportunity."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_pregnancy_near_layoff(self):
        text = (
            "One plaintiff was on preapproved pregnancy leave when she "
            "received notice that her position had been eliminated."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_age_specific_vulnerability(self):
        text = (
            "The 78-year-old retiree was contacted by phone and ultimately "
            "lost more than $200,000 to the scheme."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_disability_near_termination(self):
        text = (
            "An engineer who has multiple sclerosis and had received "
            "accommodations for years was laid off in the latest round."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_no_false_positive_neutral_timeline(self):
        """Neutral timeline mentions should not trigger humanization."""
        text = (
            "The product launched three weeks before the holiday shopping "
            "season, giving retailers time to stock shelves."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" not in types


# ── surveillance_enumeration ──────────────────────────────────────────────

class TestSurveillanceEnumeration:
    """Surveillance enumeration device: multi-item monitoring/data lists."""

    def test_monitoring_tech_list(self):
        text = (
            "The company's monitoring tools tracked keystroke data, "
            "screen activity, email records, and browser history to build "
            "a profile of each worker's daily output."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "surveillance_enumeration" in types

    def test_performance_metric_accumulation(self):
        text = (
            "Managers relied on performance ratings, calibration scores, "
            "productivity metrics, and AI-token consumption to determine "
            "which employees would be cut."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "surveillance_enumeration" in types

    def test_tool_enumeration_in_monitoring_context(self):
        text = (
            "The company deployed keystroke loggers, AI dashboards, and "
            "screen capture software to monitor employees and used the "
            "resulting data to score each worker's contributions."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "surveillance_enumeration" in types

    def test_no_false_positive_product_feature_list(self):
        """Product feature lists should not trigger surveillance_enumeration."""
        text = (
            "The new headset includes a wide-angle camera, dual speakers, "
            "an improved display, and a faster processor for smoother "
            "augmented reality experiences."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "surveillance_enumeration" not in types


# ── censored profanity (emotional_appeal extension) ───────────────────────

class TestCensoredProfanity:
    """Censored profanity should be detected as emotional_appeal."""

    def test_censored_fck(self):
        text = "Can I just say, for the record, f*ck the glasses, Lorde said."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types

    def test_censored_sht(self):
        text = "He accused the company of talking a whole lot of sh*t."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types

    def test_censored_asshole(self):
        text = "One reviewer called the product a total a**hole move."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types

    def test_uncensored_does_not_rely_on_this_pattern(self):
        """Uncensored profanity may or may not match — this tests censored only."""
        # Just verify the censored variant is caught specifically
        text = "The critic wrote: this is complete bull$#t and everyone knows it."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types
