"""Regression tests for IBD 'Sticker Shock' article analysis (Jul 8, 2026).

Tests competitive deficit framing patterns, source affiliation for
single-surname re-references, conditional/speculative organizational
source filtering, and D.A. Davidson entity detection.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.entities import detect_entities


# --- Article text fragments used across tests ---

IBD_ARTICLE_TEXT = (
    "Enterprise sticker shock from AI token costs is driving a shift "
    "toward open-source AI models, according to a new report from "
    "D.A. Davidson analyst Gil Luria.\n\n"
    "The trend could benefit Meta Platforms, which may return to "
    "open-source leadership once Meta acknowledges defeat in the "
    "frontier model race, Luria said.\n\n"
    "Meta wants to catch up to the capabilities of Anthropic, OpenAI "
    "and Google in frontier AI. But open-source models could fill the "
    "vacuum as enterprises balk at rising costs.\n\n"
    "Meta uses AI to sell more ads for more money. CEO Mark Zuckerberg "
    "has positioned the company as the leader in open-source AI with "
    "its Llama model family.\n\n"
    "Nvidia stands to benefit from the open-source trend as companies "
    "build their own AI infrastructure. Microsoft, Amazon, Palantir "
    "and Micron are also positioned to gain.\n\n"
    "The Chinese AI startup DeepSeek demonstrated that capable models "
    "can be built at a fraction of the cost of frontier models, "
    "further fueling the open-source momentum.\n\n"
    "Zuckerberg recently announced Muse Spark, a new AI venture, and "
    "Z.ai as part of Meta broader AI strategy."
)


# =====================================================================
# Framing: competitive_deficit patterns
# =====================================================================


class TestCompetitiveDeficitFraming:
    """New competitive_deficit patterns discovered in IBD article."""

    def test_acknowledges_defeat_detected(self):
        """'acknowledges defeat' should fire competitive_deficit."""
        text = "once Meta acknowledges defeat in the frontier model race"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_admits_defeat_detected(self):
        """'admits defeat' variant should also fire."""
        text = "The company admits defeat in the AI race"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_concedes_failure_detected(self):
        """'concedes failure' variant should fire."""
        text = "Google concedes failure in its social media ambitions"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_accepts_its_limitations_detected(self):
        """'accepts its limitations' variant should fire."""
        text = "Apple accepts its limitations in the AI space"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_wants_to_catch_up_to_competitor(self):
        """'wants to catch up to [Competitor]' should fire."""
        text = (
            "Meta wants to catch up to the capabilities of Anthropic, "
            "OpenAI and Google in frontier AI"
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_racing_to_catch_up_with_competitor(self):
        """'racing to catch up with [Competitor]' variant."""
        text = "Samsung is racing to catch up with Apple in mixed reality"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_fill_the_vacuum(self):
        """'fill the vacuum' should fire competitive_deficit."""
        text = "open-source models could fill the vacuum"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_step_into_the_void(self):
        """'stepping into the void' variant should fire."""
        text = "startups are stepping into the void left by Meta"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_full_article_finds_all_three(self):
        """Full IBD article should produce exactly 3 competitive_deficit."""
        devices = detect_framing_devices(IBD_ARTICLE_TEXT)
        cd = [d for d in devices if d.device_type == "competitive_deficit"]
        assert len(cd) == 3


# =====================================================================
# Sources: single-surname affiliation & conditional org filtering
# =====================================================================


class TestSingleSurnameAffiliation:
    """Single-surname re-references should use full-text introduction."""

    def test_luria_affiliation_is_da_davidson(self):
        """'Luria said' should get affiliation from 'D.A. Davidson
        analyst Gil Luria' introduction, not nearby 'of Anthropic'."""
        sources = extract_sources(IBD_ARTICLE_TEXT)
        luria = [s for s in sources if s.name == "Luria"]
        assert len(luria) == 1
        assert luria[0].affiliation == "D.A. Davidson"

    def test_luria_not_affiliated_with_anthropic(self):
        """Luria should NOT have affiliation 'Anthropic' (false positive
        from local context window containing 'of Anthropic')."""
        sources = extract_sources(IBD_ARTICLE_TEXT)
        luria = [s for s in sources if s.name == "Luria"]
        assert len(luria) == 1
        assert luria[0].affiliation != "Anthropic"


class TestConditionalOrgSourceFilter:
    """Conditional/speculative org + verb should not create a source."""

    def test_once_meta_acknowledges_not_a_source(self):
        """'once Meta acknowledges defeat' is speculative, not
        real attribution — should NOT produce an organizational source."""
        sources = extract_sources(IBD_ARTICLE_TEXT)
        meta_org = [
            s for s in sources
            if s.name == "Meta" and s.source_type == "organizational"
        ]
        assert len(meta_org) == 0

    def test_if_google_admits_not_a_source(self):
        """'if Google admits failure' should not be a source."""
        text = "Investors will react if Google admits failure in AI search."
        sources = extract_sources(text)
        google_org = [
            s for s in sources
            if s.name == "Google" and s.source_type == "organizational"
        ]
        assert len(google_org) == 0

    def test_when_apple_concedes_not_a_source(self):
        """'when Apple concedes' should not be a source."""
        text = "Markets will shift when Apple concedes defeat in VR."
        sources = extract_sources(text)
        apple_org = [
            s for s in sources
            if s.name == "Apple" and s.source_type == "organizational"
        ]
        assert len(apple_org) == 0

    def test_real_org_source_still_works(self):
        """'Meta said' without conditional qualifier should still work."""
        text = "Meta said it would invest $65B in AI infrastructure."
        sources = extract_sources(text)
        meta_org = [
            s for s in sources
            if s.name == "Meta" and s.source_type == "organizational"
        ]
        assert len(meta_org) == 1


# =====================================================================
# Entities: D.A. Davidson detection
# =====================================================================


class TestDADavidsonEntity:
    """D.A. Davidson should be detected as a financial entity."""

    def test_da_davidson_detected(self):
        """'D.A. Davidson' should be detected in Financial Services."""
        entities = detect_entities(IBD_ARTICLE_TEXT)
        da = [e for e in entities if "Davidson" in e.entity]
        assert len(da) >= 1
        assert da[0].canonical_name == "D.A. Davidson"
        assert da[0].cluster == "Financial Services"

    def test_other_analyst_firms_detected(self):
        """Other analyst firms added alongside D.A. Davidson should
        also be detectable."""
        for firm in ["Needham", "Jefferies", "Wedbush", "Piper Sandler"]:
            text = f"According to a {firm} report, AI spending will rise."
            entities = detect_entities(text)
            found = [e for e in entities if firm in e.entity]
            assert len(found) >= 1, f"{firm} not detected as entity"
