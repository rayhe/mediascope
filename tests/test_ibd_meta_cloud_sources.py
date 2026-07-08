"""Regression tests for IBD Meta cloud stock article (Jul 8, 2026).

Tests source extraction improvements discovered during Type A deep dive:
- "estimated/estimates" as neutral attribution verbs
- "Analysts with/at [Org] verb" organizational source pattern
- "according to [Compound Org]" pattern (IBD MarketSurge)
- "shockingly high" as loaded_language framing device
- "[Org] analyst [Name] also [verb]" with optional adverb between name and verb
- Financial analyst rating verbs (upgraded, stuck, maintained, reiterated)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.sources import (
    NEUTRAL_VERBS,
    extract_sources,
)
from mediascope.analyze.framing import detect_framing_devices


# ---------------------------------------------------------------------------
# Verb coverage
# ---------------------------------------------------------------------------


class TestFinancialAnalystVerbs:
    """Financial analyst attribution verbs should be in NEUTRAL_VERBS."""

    def test_estimated_in_neutral_verbs(self):
        assert "estimated" in NEUTRAL_VERBS

    def test_estimates_in_neutral_verbs(self):
        assert "estimates" in NEUTRAL_VERBS

    def test_upgraded_in_neutral_verbs(self):
        assert "upgraded" in NEUTRAL_VERBS

    def test_upgrades_in_neutral_verbs(self):
        assert "upgrades" in NEUTRAL_VERBS

    def test_downgraded_in_neutral_verbs(self):
        assert "downgraded" in NEUTRAL_VERBS

    def test_downgrades_in_neutral_verbs(self):
        assert "downgrades" in NEUTRAL_VERBS

    def test_stuck_in_neutral_verbs(self):
        assert "stuck" in NEUTRAL_VERBS

    def test_maintained_in_neutral_verbs(self):
        assert "maintained" in NEUTRAL_VERBS

    def test_reiterated_in_neutral_verbs(self):
        assert "reiterated" in NEUTRAL_VERBS

    def test_initiated_in_neutral_verbs(self):
        assert "initiated" in NEUTRAL_VERBS

    def test_projected_in_neutral_verbs(self):
        assert "projected" in NEUTRAL_VERBS

    def test_forecast_in_neutral_verbs(self):
        assert "forecast" in NEUTRAL_VERBS


# ---------------------------------------------------------------------------
# Source extraction: "Analysts with [Org] verb" pattern
# ---------------------------------------------------------------------------


class TestAnalystsWithOrgPattern:
    """Organizational sources via 'Analysts with/at [Org] verb'."""

    def test_analysts_with_semianalysis_estimated(self):
        text = (
            "Analysts with SemiAnalysis estimated in recent note that "
            "Meta signed contracts for more than 5 gigawatts of data "
            "center capacity in the first six months of the year."
        )
        sources = extract_sources(text)
        org_names = {s.name for s in sources if s.source_type == "organizational"}
        assert "SemiAnalysis" in org_names

    def test_analysts_at_erste_group_upgraded(self):
        text = (
            "Meanwhile, analysts with Erste Group upgraded their view "
            "on Meta to a buy rating from a previous hold."
        )
        sources = extract_sources(text)
        # May be captured as "named" by Pattern 1 (Name verb) before
        # the self-validating org pattern runs — either type is acceptable.
        all_names = {s.name for s in sources}
        assert "Erste Group" in all_names

    def test_analyst_singular_with_org(self):
        text = "An analyst with Bernstein Research estimated the market at $50B."
        sources = extract_sources(text)
        all_names = {s.name for s in sources}
        assert "Bernstein Research" in all_names

    def test_analysts_from_org(self):
        text = "Analysts from JPMorgan upgraded Meta to overweight."
        sources = extract_sources(text)
        org_names = {s.name for s in sources if s.source_type == "organizational"}
        assert "JPMorgan" in org_names


# ---------------------------------------------------------------------------
# Source extraction: "according to [Compound Org]"
# ---------------------------------------------------------------------------


class TestAccordingToCompoundOrg:
    """Compound org names via 'according to [Multi-word Org]'."""

    def test_according_to_ibd_marketsurge(self):
        text = (
            "While Meta briefly climbed above its 50-day line on "
            "Wednesday, the stock has not been able to sustain a rally "
            "ahead of that level since late April, according to IBD "
            "MarketSurge."
        )
        sources = extract_sources(text)
        org_names = {s.name for s in sources if s.source_type == "organizational"}
        assert "IBD MarketSurge" in org_names


# ---------------------------------------------------------------------------
# Source extraction: "[Org] analyst [Name] also verb" with adverb
# ---------------------------------------------------------------------------


class TestOrgAnalystNameWithAdverb:
    """Named source extraction with optional adverb between name and verb."""

    def test_needham_analyst_laura_martin_also_stuck(self):
        text = (
            "Meanwhile, Needham analyst Laura Martin also stuck by a "
            "hold rating for Meta in her latest note."
        )
        sources = extract_sources(text)
        named = {s.name for s in sources if s.source_type == "named"}
        assert "Laura Martin" in named

    def test_affiliation_is_needham(self):
        text = (
            "Meanwhile, Needham analyst Laura Martin also stuck by a "
            "hold rating for Meta in her latest note."
        )
        sources = extract_sources(text)
        laura = [s for s in sources if s.name == "Laura Martin"]
        assert len(laura) == 1
        assert laura[0].affiliation == "Needham"


# ---------------------------------------------------------------------------
# Framing: "shockingly high" as loaded_language
# ---------------------------------------------------------------------------


class TestShockinglyHighLoadedLanguage:
    """'Shockingly high' should trigger loaded_language framing device."""

    def test_shockingly_high_detected(self):
        text = (
            'The research firm added that Meta\'s 2027 capex could be '
            '"shockingly high."'
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "loaded_language" in types

    def test_shockingly_large_detected(self):
        text = "The fine was shockingly large, exceeding all estimates."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "loaded_language" in types

    def test_shockingly_low_detected(self):
        text = "Revenue came in shockingly low, missing by 40%."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "loaded_language" in types
