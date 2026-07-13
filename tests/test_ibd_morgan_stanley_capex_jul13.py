"""Tests for patterns added/fixed in the IBD Morgan Stanley CapEx article
deep dive (Jul 13, 2026).

Covers:
- escalation_amplification: "growing social backlash" (intervening adjective
  "social" was missing from the pattern)
- market_verdict: "market is penalizing" (new market-as-punitive-agent pattern)
- entity detection: Morgan Stanley, Mark Zuckerberg, SpaceX
- recovery_narrative fix: "reshaping [ProperNoun] Parish" (optional word before
  institution noun)
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


# ── escalation_amplification: "social" intervening adjective ─────────────────


class TestEscalationSocialAdjective:
    """'growing social backlash' should fire escalation_amplification."""

    def test_growing_social_backlash(self):
        text = "growing social backlash to data center development"
        assert "escalation_amplification" in _types(text)

    def test_rising_social_opposition(self):
        text = "rising social opposition to the project"
        assert "escalation_amplification" in _types(text)

    def test_mounting_social_resistance(self):
        text = "mounting social resistance to AI infrastructure"
        assert "escalation_amplification" in _types(text)


class TestEscalationPoliticalAdjective:
    """'growing political opposition' should fire escalation_amplification."""

    def test_growing_political_opposition(self):
        text = "growing political opposition to the pipeline"
        assert "escalation_amplification" in _types(text)

    def test_rising_political_backlash(self):
        text = "rising political backlash against big tech"
        assert "escalation_amplification" in _types(text)

    def test_mounting_political_resistance(self):
        text = "mounting political resistance to data centers"
        assert "escalation_amplification" in _types(text)


class TestEscalationConsumerAdjective:
    """'growing consumer backlash' should fire escalation_amplification."""

    def test_growing_consumer_backlash(self):
        text = "growing consumer backlash to the pricing change"
        assert "escalation_amplification" in _types(text)

    def test_rising_consumer_opposition(self):
        text = "rising consumer opposition to the new fees"
        assert "escalation_amplification" in _types(text)


class TestEscalationNationalCorporateAdjective:
    """National, corporate, industry, widespread adjectives."""

    def test_growing_national_opposition(self):
        text = "growing national opposition to data centers"
        assert "escalation_amplification" in _types(text)

    def test_mounting_corporate_resistance(self):
        text = "mounting corporate resistance to the regulation"
        assert "escalation_amplification" in _types(text)

    def test_rising_industry_backlash(self):
        text = "rising industry backlash against the mandate"
        assert "escalation_amplification" in _types(text)

    def test_growing_widespread_opposition(self):
        text = "growing widespread opposition to AI spending"
        assert "escalation_amplification" in _types(text)


# ── market_verdict: market-as-punitive-agent ─────────────────────────────────


class TestMarketPenalizingVerdict:
    """'market is penalizing' should fire market_verdict."""

    def test_market_penalizing(self):
        text = "the market is penalizing them for the spend"
        assert "market_verdict" in _types(text)

    def test_market_penalized(self):
        text = "the market has penalized Meta for overspending"
        assert "market_verdict" in _types(text)

    def test_wall_street_punishing(self):
        text = "Wall Street is punishing the stock"
        assert "market_verdict" in _types(text)

    def test_investors_discounting(self):
        text = "investors are discounting the AI revenue potential"
        assert "market_verdict" in _types(text)

    def test_market_dismissing(self):
        text = "Wall Street is dismissing the cloud strategy"
        assert "market_verdict" in _types(text)

    def test_market_not_giving_credit(self):
        text = "the market is not giving them credit for revenue upside"
        assert "market_verdict" in _types(text)

    def test_actual_ibd_sentence(self):
        """The exact quote from the IBD article."""
        text = (
            "Meta still has the most call optionality, where the market "
            "is penalizing them for the spend and not giving them credit "
            "for potential revenue from the spend"
        )
        assert "market_verdict" in _types(text)

    def test_no_false_positive_rewarding(self):
        """Positive market action should NOT fire market_verdict."""
        text = "the market is rewarding them for the pivot"
        assert "market_verdict" not in _types(text)


# ── recovery_narrative: proper noun before institution noun ──────────────────


class TestRecoveryNarrativeProperNoun:
    """'reshaping [ProperNoun] Parish/District/Town' should fire."""

    def test_reshaping_richland_parish(self):
        text = "The project is already reshaping Richland Parish."
        assert "recovery_narrative" in _types(text)

    def test_reshaping_jefferson_parish(self):
        text = "reshaping Jefferson Parish through investment"
        assert "recovery_narrative" in _types(text)

    def test_transforming_lake_district(self):
        text = "transforming Lake District communities"
        assert "recovery_narrative" in _types(text)

    def test_reshaping_the_parish_still_works(self):
        text = "reshaping the parish through investment"
        assert "recovery_narrative" in _types(text)


# ── entity detection ────────────────────────────────────────────────────────


class TestMorganStanleyEntity:
    """Morgan Stanley should detect as Financial Services."""

    def test_morgan_stanley(self):
        ents = _entity_clusters("Morgan Stanley analyst Brian Nowak")
        assert "Morgan Stanley" in ents
        assert ents["Morgan Stanley"] == "Financial Services"

    def test_morgan_stanley_in_context(self):
        text = "The Morgan Stanley analyst raised capex estimates"
        ents = _entity_clusters(text)
        assert "Morgan Stanley" in ents


class TestSpaceXEntity:
    """SpaceX should detect in Tesla/SpaceX cluster."""

    def test_spacex(self):
        ents = _entity_clusters("also including Microsoft and SpaceX")
        assert "SpaceX" in ents
        assert ents["SpaceX"] == "Tesla/SpaceX"
