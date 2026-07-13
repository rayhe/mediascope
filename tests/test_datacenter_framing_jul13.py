"""Tests for framing patterns added in the WSJ Meta Louisiana data center
article deep dive (Jul 13, 2026).

Covers:
- escalation_amplification: "growing public opposition" (intervening adjective)
- loaded_language: "aggressive bets", infrastructure burden language,
  "life-altering"/"life-changing"
- recovery_narrative: "breathing new life into" revitalization idioms
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _types(text: str) -> set[str]:
    """Return the set of device_type strings detected in *text*."""
    return {d.device_type for d in detect_framing_devices(text)}


# ── escalation_amplification: intervening adjective ─────────────────────────


class TestEscalationWithInterveningAdjective:
    """Growing/rising + adjective + opposition/backlash should fire."""

    def test_growing_public_opposition(self):
        text = "amid growing public opposition to data centers"
        assert "escalation_amplification" in _types(text)

    def test_rising_community_resistance(self):
        text = "rising community resistance to the pipeline"
        assert "escalation_amplification" in _types(text)

    def test_mounting_local_backlash(self):
        text = "mounting local backlash against the rezoning"
        assert "escalation_amplification" in _types(text)

    def test_intensifying_environmental_protest(self):
        text = "intensifying environmental protest over emissions"
        assert "escalation_amplification" in _types(text)

    def test_growing_grassroots_pushback(self):
        text = "growing grassroots pushback from residents"
        assert "escalation_amplification" in _types(text)


# ── loaded_language: gambling metaphors ──────────────────────────────────────


class TestGamblingMetaphors:
    """Aggressive bets, big gamble, etc. in business context."""

    def test_aggressive_bets(self):
        text = "Zuckerberg's aggressive bets on AI"
        assert "loaded_language" in _types(text)

    def test_big_gamble(self):
        text = "the company's big gamble on infrastructure"
        assert "loaded_language" in _types(text)

    def test_massive_wager(self):
        text = "a massive wager that AI will pay off"
        assert "loaded_language" in _types(text)

    def test_aggressive_play(self):
        text = "an aggressive play for market share"
        assert "loaded_language" in _types(text)


# ── loaded_language: infrastructure burden ───────────────────────────────────


class TestInfrastructureBurden:
    """Burdening customers, surging prices, taxed grids."""

    def test_burdening_customers(self):
        text = "burdening electricity customers with higher costs"
        assert "loaded_language" in _types(text)

    def test_burdening_ratepayers(self):
        text = "the project risks burdening ratepayers"
        assert "loaded_language" in _types(text)

    def test_surging_electricity_prices(self):
        text = "surging electricity prices across the region"
        assert "loaded_language" in _types(text)

    def test_surging_energy_costs(self):
        text = "surging energy costs have alarmed officials"
        assert "loaded_language" in _types(text)

    def test_taxed_grids(self):
        text = "has led to taxed grids and outages"
        assert "loaded_language" in _types(text)

    def test_strained_infrastructure(self):
        text = "strained infrastructure unable to cope"
        assert "loaded_language" in _types(text)

    def test_overburdened_systems(self):
        text = "overburdened systems serving rural communities"
        assert "loaded_language" in _types(text)


# ── loaded_language: life-altering / life-changing ───────────────────────────


class TestLifeAlteringLanguage:
    """Positive magnitude idioms used editorially."""

    def test_life_altering(self):
        text = "It's life-altering for our teachers"
        assert "loaded_language" in _types(text)

    def test_life_changing(self):
        text = "a life-changing opportunity for the community"
        assert "loaded_language" in _types(text)

    def test_life_transforming(self):
        text = "the life-transforming impact of the investment"
        assert "loaded_language" in _types(text)


# ── recovery_narrative: revitalization idioms ────────────────────────────────


class TestRevitalizationIdioms:
    """Breathing new life, revitalizing, etc."""

    def test_breathing_new_life_into(self):
        text = "breathing new life into the region"
        assert "recovery_narrative" in _types(text)

    def test_breathed_life_into(self):
        text = "has breathed life into the local economy"
        assert "recovery_narrative" in _types(text)

    def test_injecting_new_life_into(self):
        text = "injecting new life into a struggling town"
        assert "recovery_narrative" in _types(text)

    def test_revitalizing(self):
        text = "revitalizing the corridor with new development"
        assert "recovery_narrative" in _types(text)

    def test_transforming_rural_economy(self):
        text = "transforming the rural economy of the parish"
        assert "recovery_narrative" in _types(text)
