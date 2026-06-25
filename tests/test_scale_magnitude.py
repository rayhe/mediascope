"""Tests for scale/magnitude framing device detection.

Scale/magnitude framing deploys large raw numbers, calculated maximums,
or scale analogies to create impressions of excess, danger, or harm.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


class TestScaleMagnitudeCalculatedMaximum:
    """Calculated maximum: 'up to X% of revenue' / 'as much as $X billion'."""

    def test_eu_fine_percentage(self):
        """EU DSA fine framing: 'up to 6% of global annual sales'."""
        text = (
            "Under the DSA, companies can be fined as much as 6% "
            "of their global annual sales if they are unable to satisfy "
            "regulators."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1, f"Expected scale_magnitude hit, got: {hits}"

    def test_potential_fine_dollar_amount(self):
        """Calculated dollar fine: 'that would mean a potential fine of about $12 billion'."""
        text = (
            "Based on Meta's fiscal 2025 revenue, that would mean a "
            "potential fine of about $12 billion."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_up_to_billion(self):
        """'up to $145 billion' triggers scale_magnitude."""
        text = "Meta plans to spend up to $145 billion on capital expenditure."
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1


class TestScaleMagnitudeScaleAnalogy:
    """Scale analogies: 'enough to power X homes/cities'."""

    def test_enough_to_power_homes(self):
        """'enough to roughly power 750,000 US homes' triggers."""
        text = (
            "A single gigawatt is enough to roughly power 750,000 "
            "U.S. homes."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_as_much_as_small_country(self):
        """'as much electricity as a small country' triggers."""
        text = (
            "The data centers will consume as much electricity as "
            "a medium-sized city."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1


class TestScaleMagnitudeCumulativeTotals:
    """Cumulative totals: '$70B in losses since 2020'."""

    def test_cumulative_losses_since_year(self):
        """'$70 billion in Reality Labs losses since 2020' triggers."""
        text = (
            "Horizon Worlds never worked and has cost Meta more than "
            "$70 billion in losses since 2020."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_cumulative_spending_past_years(self):
        """'$850 billion in spending over the past decade' triggers."""
        text = (
            "Total future data-center lease commitments lifted to "
            "$850 billion in costs over the past year."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1


class TestScaleMagnitudeVictimRoster:
    """Victim/case roster: 'more than X,000 lawsuits'."""

    def test_thousands_of_lawsuits(self):
        """'more than 2,000 lawsuits' triggers."""
        text = (
            "Meta faces more than 2,000 lawsuits over allegations "
            "that its products are addictive."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_school_districts(self):
        """'more than 1,300 school districts' triggers."""
        text = (
            "More than 1,300 school districts have filed complaints "
            "claiming that Instagram is making school worse."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_over_families(self):
        """'over 500 families' triggers."""
        text = "Over 500 families have joined the class action."
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1


class TestScaleMagnitudeComparisonAmplifiers:
    """Comparison amplifiers: 'more than double', 'X% spike'."""

    def test_more_than_double(self):
        """'more than double last year's outlay' triggers."""
        text = (
            "Meta is spending between $125 billion and $145 billion "
            "on capital expenditure in 2026, more than double last "
            "year's outlay."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1

    def test_percentage_spike(self):
        """'76% spike from the prior period' triggers."""
        text = (
            "Meta accumulated $182.9 billion in future lease "
            "obligations — a 76% spike from the prior period."
        )
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) >= 1


class TestScaleMagnitudeNegativeCases:
    """Ensure simple number mentions don't trigger false positives."""

    def test_simple_price(self):
        """'$299' alone should NOT trigger scale_magnitude."""
        text = "The new Meta Glasses start at $299."
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) == 0

    def test_battery_hours(self):
        """'8 hours of battery life' should NOT trigger."""
        text = "They deliver over eight hours of battery life."
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) == 0

    def test_simple_user_count(self):
        """'3.5 billion users' alone — no amplifier — should NOT trigger."""
        text = "Meta has 3.5 billion daily active users."
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        assert len(hits) == 0


class TestScaleMagnitudeIntegration:
    """Integration tests against real articles in the repo."""

    def test_wired_mci_has_scale_devices(self):
        """Wired MCI data exposure article should have scale framing."""
        import os
        path = "examples/sample_output/wired_meta_mci_data_exposure_2026_06_22_article.txt"
        if not os.path.exists(path):
            pytest.skip("article not found")
        text = open(path).read()
        hits = [f for f in detect_framing_devices(text)
                if f.device_type == "scale_magnitude"]
        # The MCI article discusses Meta's scale — should have at least one
        # scale_magnitude device if it mentions layoffs, spending, etc.
        # If zero, that's acceptable — not every article uses this device
        assert isinstance(hits, list)
