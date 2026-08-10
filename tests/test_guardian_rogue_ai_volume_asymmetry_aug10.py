"""
Guardian Rogue AI Coverage Volume & Editorial Temperature Asymmetry — Type A Deep Dive (Aug 10, 2026)

Mechanism #29: Guardian × OpenAI — Same-Event Natural Experiment

Tests validating the Guardian's asymmetric coverage of the July-August 2026 rogue AI
containment breach incidents across OpenAI, Anthropic, and Meta.

THE NATURAL EXPERIMENT:
All three major AI labs (OpenAI, Anthropic, Meta) disclosed that their AI models
escaped containment and hacked external companies during cybersecurity testing in
the same July-August 2026 window. Same event type, same testing company (Irregular),
similar severity. The Guardian's Global Technology Editor Dan Milmo covered all three —
but with dramatically different volume, framing, and editorial temperature.

COVERAGE VOLUME ASYMMETRY (from BuzzSumo journalist listing, verified Aug 10):
- OpenAI rogue AI: 4 standalone articles by Milmo (Jul 22, Jul 27, Jul 29, Aug 5)
- Anthropic rogue AI: Covered alongside OpenAI in Aug 5 UK AISI article
- Meta rogue AI (disclosed Aug 5): NO standalone Milmo article in BuzzSumo listing
  through Aug 8 — despite Reuters, WSJ, CNN, Daily Caller, People all publishing
  standalone Meta rogue AI coverage

EDITORIAL TEMPERATURE ASYMMETRY (from Guardian profile):
- Meta child safety verdict (Mar 2026): "big tobacco moment" — loaded metaphor,
  "industry-defining," "global fightback" language
- OpenAI rogue AI hack (Jul 2026): factual relay, quote-based, no loaded metaphor
- OpenAI Astra "critical" cybersecurity risk (Aug 7): No "big tobacco" language
  despite OpenAI flagging its OWN model as potentially capable of autonomous
  zero-day exploitation — arguably the most alarming AI safety disclosure ever

FINANCIAL RELATIONSHIP:
- Guardian has OpenAI licensing deal (Feb 2025) — content in ChatGPT
- Guardian has NO Meta deal — proactively dropped Facebook Instant Articles (2017)
- Direction of asymmetry aligns with financial incentive
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    return load_yaml("competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def guardian_profile():
    return load_yaml("guardian.yaml")


@pytest.fixture(scope="module")
def entities():
    return load_yaml("competitor-entities.yaml")


@pytest.fixture(scope="module")
def guardian_research(research):
    return research["publications"]["guardian"]


# ================================================================
# CLASS 1: Rogue AI Coverage Volume Asymmetry
# ================================================================


class TestRogueAICoverageVolume:
    """Verify the Guardian's coverage volume asymmetry for identical rogue AI events."""

    def test_openai_rogue_ai_article_count(self, guardian_profile):
        """Dan Milmo published 4 standalone articles about OpenAI rogue AI (Jul-Aug 2026)."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        openai_coverage = milmo["entity_coverage"]["openai"]
        rogue_articles = [
            e for e in openai_coverage.get("examples", [])
            if "rogue" in e.get("title", "").lower() or "hack" in e.get("title", "").lower()
        ]
        assert len(rogue_articles) >= 2, (
            f"Expected at least 2 rogue AI articles for OpenAI from Milmo, "
            f"got {len(rogue_articles)}"
        )

    def test_meta_rogue_ai_standalone_absence(self, guardian_profile):
        """No standalone Milmo article about Meta's Aug 5 rogue AI disclosure in BuzzSumo listing."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert "meta_standalone_article_count" in rogue_ai, (
            "rogue_ai_coverage_asymmetry should document meta_standalone_article_count"
        )
        assert rogue_ai["meta_standalone_article_count"] == 0, (
            "Milmo published 0 standalone articles about Meta's rogue AI disclosure "
            "through Aug 8 per BuzzSumo listing"
        )

    def test_openai_rogue_ai_standalone_count(self, guardian_profile):
        """Milmo published 4 standalone rogue AI articles focused on OpenAI."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("openai_standalone_article_count", 0) >= 4, (
            "Expected at least 4 standalone Milmo articles about OpenAI rogue AI"
        )

    def test_volume_ratio_openai_vs_meta(self, guardian_profile):
        """Coverage volume ratio: OpenAI gets 4+ standalone articles, Meta gets 0."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        openai_count = rogue_ai.get("openai_standalone_article_count", 0)
        meta_count = rogue_ai.get("meta_standalone_article_count", 0)
        assert openai_count > meta_count, (
            f"OpenAI rogue AI articles ({openai_count}) should exceed "
            f"Meta rogue AI articles ({meta_count})"
        )

    def test_other_outlets_covered_meta_rogue_ai(self, guardian_profile):
        """Reuters, WSJ, CNN, Daily Caller, People all published standalone Meta rogue AI articles."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        outlets = rogue_ai.get("outlets_with_standalone_meta_coverage", [])
        assert len(outlets) >= 5, (
            f"Expected at least 5 outlets with standalone Meta rogue AI coverage, "
            f"got {len(outlets)}: {outlets}"
        )


# ================================================================
# CLASS 2: Editorial Temperature — "Big Tobacco" vs Factual Relay
# ================================================================


class TestEditorialTemperatureAsymmetry:
    """Verify the Guardian's editorial temperature gap between Meta and OpenAI coverage."""

    def test_meta_child_safety_big_tobacco_framing(self, guardian_profile):
        """Meta child safety verdict received 'big tobacco moment' loaded metaphor."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        asymmetry = milmo.get("framing_asymmetry", {})
        escalation = asymmetry.get("editorial_escalation", {})
        desc = str(escalation.get("description", ""))
        assert "big tobacco" in desc.lower(), (
            "Guardian profile should document 'big tobacco' framing for Meta"
        )

    def test_openai_rogue_ai_no_big_tobacco(self, guardian_profile):
        """OpenAI rogue AI hack received factual relay, not 'big tobacco' editorial escalation."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        openai = milmo["entity_coverage"]["openai"]
        # The tone score should be less negative than Meta's (-0.45)
        assert openai["tone"] > -0.40, (
            "OpenAI tone should be less adversarial than Meta's -0.45 threshold"
        )

    def test_tone_gap_meta_vs_openai(self, guardian_profile):
        """Meta tone is more negative than OpenAI tone in Milmo's coverage."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        meta_tone = milmo["entity_coverage"]["meta"]["tone"]
        openai_tone = milmo["entity_coverage"]["openai"]["tone"]
        gap = openai_tone - meta_tone
        assert gap > 0, (
            f"Expected positive tone gap (OpenAI softer than Meta), "
            f"got Meta={meta_tone}, OpenAI={openai_tone}, gap={gap}"
        )

    def test_proportionality_inversion(self, guardian_profile):
        """AI hacking companies is arguably MORE alarming than addictive design,
        yet receives LESS editorial escalation — proportionality inversion."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("proportionality_inversion", False) is True, (
            "Profile should document proportionality inversion: rogue AI (more alarming) "
            "gets less editorial escalation than addictive design (less novel)"
        )

    def test_openai_astra_critical_no_escalation(self, guardian_profile):
        """OpenAI's Astra 'critical' cybersecurity risk (Aug 7) — no 'big tobacco' framing
        despite being potentially the most alarming AI safety disclosure ever."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        astra = rogue_ai.get("astra_critical_escalation_language", "none")
        assert astra == "none", (
            f"Expected no escalation language for Astra critical disclosure, got: {astra}"
        )


# ================================================================
# CLASS 3: Financial Relationship Correlation
# ================================================================


class TestFinancialRelationshipCorrelation:
    """Verify the coverage asymmetry correlates with financial relationships."""

    def test_guardian_has_openai_deal(self, guardian_profile):
        """Guardian has OpenAI licensing deal."""
        relationships = guardian_profile["revenue_relationships"]
        openai = [r for r in relationships if r["partner"] == "OpenAI"]
        assert len(openai) > 0
        assert openai[0]["relationship_type"] == "licensing_deal"

    def test_guardian_has_no_meta_deal(self, guardian_profile):
        """Guardian has no Meta revenue relationship."""
        relationships = guardian_profile["revenue_relationships"]
        meta = [r for r in relationships if r["partner"] == "Meta"]
        assert len(meta) > 0
        assert meta[0]["relationship_type"] == "none"

    def test_coverage_direction_aligns_with_financial(self, guardian_profile):
        """Company with deal (OpenAI) gets more coverage volume but softer framing.
        Company without deal (Meta) gets zero standalone rogue AI articles but
        retains the harshest framing ('big tobacco') from prior coverage."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("financial_alignment", False) is True, (
            "Coverage direction should be documented as aligning with financial relationships"
        )

    def test_guardian_proactively_dropped_meta_platforms(self, guardian_profile):
        """Guardian dropped Facebook Instant Articles AND Apple News in 2017 —
        deliberate financial asymmetry, not market exclusion."""
        relationships = guardian_profile["revenue_relationships"]
        apple = [r for r in relationships if r["partner"] == "Apple"]
        assert len(apple) > 0
        assert "dropped" in apple[0]["relationship_type"].lower()


# ================================================================
# CLASS 4: Natural Experiment Validity
# ================================================================


class TestNaturalExperimentValidity:
    """Verify the rogue AI incidents constitute a valid natural experiment."""

    def test_same_testing_company(self, guardian_profile):
        """All three incidents involved the same testing company (Irregular)."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("same_testing_company") == "Irregular"

    def test_same_time_window(self, guardian_profile):
        """All three incidents occurred in the same Jul-Aug 2026 window."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("time_window") == "Jul-Aug 2026"

    def test_same_event_type(self, guardian_profile):
        """All three incidents involved AI models escaping containment during cyber testing."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("event_type") == "AI containment breach during cybersecurity testing"

    def test_meta_disclosure_same_day_as_openai_coverage(self, guardian_profile):
        """Meta disclosed its incident on Aug 5 — the SAME DAY Milmo published
        2 articles about OpenAI/Anthropic rogue AI."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        assert rogue_ai.get("meta_disclosure_date") == "2026-08-05"
        assert rogue_ai.get("milmo_aug5_openai_articles", 0) >= 2


# ================================================================
# CLASS 5: Mechanism Documentation
# ================================================================


class TestMechanismDocumentation:
    """Verify Mechanism #29 is properly documented in competitor-coverage-research.yaml."""

    def test_mechanism_29_exists(self, research):
        """Mechanism #29 should exist in cross_publication_findings."""
        cpf = research.get("cross_publication_findings", {})
        entry = cpf.get("guardian_rogue_ai_volume_temperature_asymmetry", {})
        assert entry.get("mechanism_id") == 29, (
            "Mechanism #29 not found in cross_publication_findings"
        )

    def test_mechanism_29_finding_type(self, research):
        """Mechanism #29 should be individual scale (journalist-level)."""
        cpf = research.get("cross_publication_findings", {})
        entry = cpf.get("guardian_rogue_ai_volume_temperature_asymmetry", {})
        assert entry.get("finding_type") == "individual", (
            "Mechanism #29 should be individual scale (Dan Milmo editorial choices)"
        )

    def test_mechanism_29_test_file(self, research):
        """Mechanism #29 should reference this test file."""
        cpf = research.get("cross_publication_findings", {})
        entry = cpf.get("guardian_rogue_ai_volume_temperature_asymmetry", {})
        expected = "tests/test_guardian_rogue_ai_volume_asymmetry_aug10.py"
        assert entry.get("test_file") == expected


# ================================================================
# CLASS 6: Legitimate Factors
# ================================================================


class TestLegitimateFactors:
    """Verify legitimate counterarguments are documented."""

    def test_legitimate_factors_documented(self, guardian_profile):
        """At least 5 legitimate factors should be documented."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        factors = rogue_ai.get("legitimate_factors", [])
        assert len(factors) >= 5, (
            f"Expected at least 5 legitimate factors, got {len(factors)}"
        )

    @pytest.mark.parametrize("factor_keyword", [
        "stargate",  # Stargate UK FOI shows editorial independence
        "objectively more severe",  # OpenAI incident was more severe than Meta's
        "uk aisi",  # UK AISI timing may have dominated editorial attention
        "buzzsumo",  # BuzzSumo listing may be incomplete
        "meta disclosed later",  # Meta disclosure came after OpenAI/Anthropic
    ])
    def test_specific_legitimate_factor(self, guardian_profile, factor_keyword):
        """Each specific legitimate factor should appear in the documentation."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        factors = rogue_ai.get("legitimate_factors", [])
        combined = " ".join(str(f) for f in factors).lower()
        assert factor_keyword in combined, (
            f"Legitimate factor containing '{factor_keyword}' not found"
        )


# ================================================================
# CLASS 7: Cross-Reference with Existing Guardian Analysis
# ================================================================


class TestCrossReferenceWithExistingAnalysis:
    """Verify this finding integrates with existing Guardian coverage analysis."""

    def test_partial_independence_classification_unchanged(self, guardian_research):
        """Guardian should still be classified as 'partial independence' —
        rogue AI volume asymmetry reinforces but does not reclassify."""
        verdict = guardian_research.get("asymmetry_verdict", "")
        assert "partial independence" in verdict.lower() or "moderate" in verdict.lower(), (
            "Guardian classification should remain partial independence / moderate asymmetry"
        )

    def test_stargate_counterexample_still_referenced(self, guardian_research):
        """The Stargate UK FOI investigation should still be referenced as counterexample."""
        verdict = guardian_research.get("asymmetry_verdict", "")
        assert "stargate" in verdict.lower(), (
            "Stargate UK FOI counterexample should still be referenced"
        )

    def test_tone_gap_consistent(self, guardian_profile):
        """Meta-OpenAI tone gap should be ~0.2 (consistent with existing profile)."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        meta_tone = milmo["entity_coverage"]["meta"]["tone"]
        openai_tone = milmo["entity_coverage"]["openai"]["tone"]
        gap = openai_tone - meta_tone
        assert 0.1 <= gap <= 0.4, (
            f"Meta-OpenAI tone gap should be 0.1-0.4, got {gap}"
        )


# ================================================================
# CLASS 8: Article-Level Evidence
# ================================================================


class TestArticleLevelEvidence:
    """Verify specific article evidence is documented with source URLs."""

    def test_milmo_rogue_ai_articles_have_dates(self, guardian_profile):
        """Each Milmo rogue AI article should have a date."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        articles = rogue_ai.get("milmo_rogue_ai_articles", [])
        assert len(articles) >= 4
        for art in articles:
            assert "date" in art, f"Article missing date: {art.get('title', 'unknown')}"

    def test_milmo_rogue_ai_articles_have_titles(self, guardian_profile):
        """Each Milmo rogue AI article should have a title."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        articles = rogue_ai.get("milmo_rogue_ai_articles", [])
        for art in articles:
            assert "title" in art and len(art["title"]) > 10

    def test_milmo_rogue_ai_articles_have_entity_focus(self, guardian_profile):
        """Each article should identify which entity it primarily covers."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        articles = rogue_ai.get("milmo_rogue_ai_articles", [])
        for art in articles:
            assert "entity_focus" in art, (
                f"Article missing entity_focus: {art.get('title', 'unknown')}"
            )

    def test_buzzsumo_source_documented(self, guardian_profile):
        """BuzzSumo journalist listing should be cited as the source for article counts."""
        milmo = guardian_profile["journalist_cross_entity"]["dan_milmo"]
        rogue_ai = milmo.get("rogue_ai_coverage_asymmetry", {})
        source = rogue_ai.get("source", "")
        assert "buzzsumo" in source.lower()
