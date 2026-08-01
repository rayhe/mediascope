"""Regression tests for success_paradox framing device.

Discovered from Gizmodo "Smart Glasses Are a Hit Even as Privacy Concerns
Pile Up" (Jul 30, 2026) and MarketWatch "Big Tech is obsessed with smart
glasses. Now it has to convince people to wear them" (Jun 27, 2026).

success_paradox detects headline/lede structures where objectively positive
commercial news (revenue growth, market success) is immediately pivoted via
"even as" / "despite" / "but" to a negative narrative.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


def _has_device(text: str, device_type: str) -> bool:
    """Return True if detect_framing_devices finds *device_type* in *text*."""
    devices = detect_framing_devices(text)
    return any(d.device_type == device_type for d in devices)


class TestSuccessParadox:
    """Positive tests — should fire success_paradox."""

    def test_hit_even_as_concerns(self):
        """Gizmodo Jul 30 headline structure."""
        text = (
            "Smart Glasses Are a Hit Even as Privacy Concerns Pile Up. "
            "Revenue from its smart glasses nearly doubled in the second "
            "quarter compared to the same period last year."
        )
        assert _has_device(text, "success_paradox")

    def test_popular_despite_prickly_climate(self):
        """Gizmodo Jul 30 body language."""
        text = (
            "they're popular despite an increasingly prickly climate "
            "surrounding the category"
        )
        assert _has_device(text, "success_paradox")

    def test_nearly_doubled_but_backlash(self):
        """Revenue growth + but + backlash pattern."""
        text = (
            "Revenue from smart glasses nearly doubled in Q2, but the "
            "backlash over privacy issues continues to mount."
        )
        assert _has_device(text, "success_paradox")

    def test_growth_doesnt_mean_tipping_point(self):
        """Gizmodo Jul 30 closing language."""
        text = (
            "That growth doesn't mean a tipping point isn't coming, "
            "though, especially as more restrictions kick in."
        )
        assert _has_device(text, "success_paradox")

    def test_strong_sales_despite_scrutiny(self):
        """Generic success-despite-scrutiny pattern."""
        text = (
            "Meta reported strong sales growth in wearables despite "
            "intense scrutiny from privacy advocates and lawmakers."
        )
        assert _has_device(text, "success_paradox")

    def test_commercial_success_even_as_controversy(self):
        """Commercial success + even as + controversy."""
        text = (
            "The product line has been a commercial success even as "
            "controversy over facial recognition deepens."
        )
        assert _has_device(text, "success_paradox")

    def test_selling_well_despite_stigma(self):
        """Selling well + despite + glasshole stigma."""
        text = (
            "Meta's glasses are selling well despite the growing "
            "glasshole stigma that has dogged the category."
        )
        assert _has_device(text, "success_paradox")

    def test_market_success_but_privacy(self):
        """Market success + but + privacy concerns."""
        text = (
            "The market success of AI-powered eyewear is undeniable, "
            "but privacy concerns have escalated significantly."
        )
        assert _has_device(text, "success_paradox")

    def test_record_sales_while_backlash(self):
        """Record + while + backlash."""
        text = (
            "EssilorLuxottica reported record revenue from smart glasses "
            "while backlash over surveillance capabilities intensifies."
        )
        assert _has_device(text, "success_paradox")

    def test_boom_despite_criticism(self):
        """Boom + despite + criticism."""
        text = (
            "The smart glasses boom continues despite mounting criticism "
            "from civil liberties groups worldwide."
        )
        assert _has_device(text, "success_paradox")

    def test_doubled_yet_pushback(self):
        """Doubled + yet + pushback."""
        text = (
            "Smart glasses revenue more than doubled in the first half, "
            "yet the pushback from privacy advocates shows no signs of easing."
        )
        assert _has_device(text, "success_paradox")

    def test_surging_even_as_debate(self):
        """Surging + even as + debate."""
        text = (
            "Demand for AI glasses is surging even as the debate over "
            "their use in public spaces reaches fever pitch."
        )
        assert _has_device(text, "success_paradox")

    def test_popular_despite_hostile_climate(self):
        """Popular despite a hostile climate variation."""
        text = (
            "Ray-Ban Meta glasses remain popular despite a hostile "
            "regulatory climate in the European Union."
        )
        assert _has_device(text, "success_paradox")


class TestSuccessParadoxNegative:
    """Negative tests — should NOT fire success_paradox."""

    def test_pure_negative_no_success(self):
        """Pure negative article with no positive commercial framing."""
        text = (
            "Privacy concerns continue to pile up for Meta's smart glasses. "
            "Lawmakers are demanding answers about facial recognition."
        )
        assert not _has_device(text, "success_paradox")

    def test_pure_positive_no_pivot(self):
        """Pure positive article with no negative pivot."""
        text = (
            "EssilorLuxottica reported strong revenue growth in Q2, "
            "driven by AI-powered smart glasses and myopia products."
        )
        assert not _has_device(text, "success_paradox")

    def test_unrelated_despite(self):
        """'Despite' in a non-success-paradox context."""
        text = (
            "Despite the rain, thousands of fans gathered outside "
            "the stadium to watch the championship game."
        )
        assert not _has_device(text, "success_paradox")

    def test_grudging_concession_only(self):
        """Grudging concession without success-paradox structure."""
        text = (
            "Meta is now actually rolling out tamper detection for its "
            "smart glasses, though critics say it's too little too late."
        )
        assert not _has_device(text, "success_paradox")
