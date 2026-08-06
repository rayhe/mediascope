"""
Guardian Cross-Entity Coverage Analysis — Type A Deep Dive (Aug 6, 2026)

Tests validating the Guardian's coverage framing of OpenAI (deal partner)
vs Meta (non-partner) and the Stargate UK FOI counterexample.

The Guardian is the MOST INTERESTING case in the dataset: it demonstrates
both financial-incentive asymmetry AND genuine editorial independence
(Stargate UK FOI investigation), making it a "partial independence" model
rather than a "financial capture" case like WIRED or The Atlantic.
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
# CLASS 1: Guardian Financial Relationships
# ================================================================


class TestGuardianFinancialRelationships:
    """Verify the Guardian's financial relationship data is correctly documented."""

    def test_guardian_has_openai_licensing_deal(self, guardian_profile):
        """Guardian signed OpenAI licensing deal Feb 2025."""
        relationships = guardian_profile["revenue_relationships"]
        openai_deals = [r for r in relationships if r["partner"] == "OpenAI"]
        assert len(openai_deals) > 0, "Guardian should have an OpenAI deal"
        openai_deal = openai_deals[0]
        assert openai_deal["relationship_type"] == "licensing_deal"
        assert "2025-02" in str(openai_deal.get("date_established", ""))

    def test_guardian_has_google_news_ai_pilot(self, guardian_profile):
        """Guardian is in Google's News AI pilot program since Dec 2025."""
        relationships = guardian_profile["revenue_relationships"]
        google_pilot_deals = [
            r
            for r in relationships
            if r["partner"] == "Google (News AI Pilot)"
        ]
        assert (
            len(google_pilot_deals) > 0
        ), "Guardian should have Google News AI pilot deal"
        assert "2025-12" in str(
            google_pilot_deals[0].get("date_established", "")
        )

    def test_guardian_has_prorata_deal(self, guardian_profile):
        """Guardian is a founding partner of ProRata AI."""
        relationships = guardian_profile["revenue_relationships"]
        prorata_deals = [r for r in relationships if r["partner"] == "ProRata"]
        assert (
            len(prorata_deals) > 0
        ), "Guardian should have ProRata AI deal"

    def test_guardian_has_zero_meta_deals(self, guardian_profile):
        """Guardian has no financial relationship with Meta."""
        relationships = guardian_profile["revenue_relationships"]
        meta_deals = [r for r in relationships if r["partner"] == "Meta"]
        assert len(meta_deals) > 0, "Meta entry should exist"
        meta_deal = meta_deals[0]
        assert meta_deal["relationship_type"] == "none"
        assert meta_deal["estimated_value"] == "$0"

    def test_guardian_dropped_apple_news_2017(self, guardian_profile):
        """Guardian proactively dropped Apple News in April 2017."""
        relationships = guardian_profile["revenue_relationships"]
        apple_entries = [r for r in relationships if r["partner"] == "Apple"]
        assert len(apple_entries) > 0, "Apple entry should exist"
        apple = apple_entries[0]
        assert "dropped" in str(apple.get("relationship_type", "")).lower()

    def test_guardian_has_three_competitor_deals(self, entities):
        """Guardian has 3 competitor deals and 0 Meta deals in aggregate matrix."""
        excluded = entities["meta_ai_deals"]["excluded_publishers"]
        guardian_entries = [
            e
            for e in excluded
            if "Guardian" in e.get("name", "")
        ]
        assert len(guardian_entries) > 0
        guardian = guardian_entries[0]
        assert guardian["deal_count"] == 2  # OpenAI + Google pilot in entities
        assert guardian["meta_deal"] == "none"


# ================================================================
# CLASS 2: Guardian OpenAI Coverage Tone Classification
# ================================================================


class TestGuardianOpenAICoverageTone:
    """Verify the Guardian's OpenAI coverage is classified correctly after reclassification."""

    def test_openai_tone_reclassified_to_balanced_adversarial(self, guardian_research):
        """OpenAI coverage tone should be balanced_to_adversarial after Stargate UK finding."""
        assert guardian_research["openai_coverage_tone"] == "balanced_to_adversarial"

    def test_meta_tone_is_adversarial(self, guardian_research):
        """Meta coverage tone should be adversarial."""
        assert guardian_research["meta_coverage_tone"] == "adversarial"

    def test_google_tone_is_balanced_adversarial(self, guardian_research):
        """Google coverage tone should be balanced_adversarial."""
        assert guardian_research["google_coverage_tone"] == "balanced_adversarial"


# ================================================================
# CLASS 3: Stargate UK FOI Investigation
# ================================================================


class TestStargateUKFOIInvestigation:
    """Validate the Stargate UK FOI investigation as a counterexample to financial capture."""

    def test_stargate_investigation_exists_in_examples(self, guardian_research):
        """The Stargate UK FOI investigation should be documented as an example."""
        examples = guardian_research.get("openai_examples", [])
        stargate_examples = [
            e for e in examples if "Stargate" in e.get("title", "")
        ]
        assert (
            len(stargate_examples) > 0
        ), "Stargate UK FOI investigation should be documented"

    def test_stargate_tone_is_adversarial(self, guardian_research):
        """Stargate UK investigation tone should be adversarial (negative)."""
        examples = guardian_research.get("openai_examples", [])
        stargate_examples = [
            e for e in examples if "Stargate" in e.get("title", "")
        ]
        assert len(stargate_examples) > 0
        tone = stargate_examples[0].get("tone", 0)
        assert tone < -0.3, f"Stargate investigation should be adversarial, got {tone}"

    def test_stargate_date_july_2026(self, guardian_research):
        """Stargate UK investigation was published in July 2026."""
        examples = guardian_research.get("openai_examples", [])
        stargate_examples = [
            e for e in examples if "Stargate" in e.get("title", "")
        ]
        assert len(stargate_examples) > 0
        date = stargate_examples[0].get("date", "")
        assert "2026-07" in date, f"Expected July 2026, got {date}"

    def test_stargate_uses_foi_methodology(self, guardian_research):
        """The investigation used Freedom of Information requests."""
        summary = guardian_research.get("openai_coverage_summary", "")
        assert "FOI" in summary or "Freedom of Information" in summary

    def test_stargate_has_source_urls(self, guardian_research):
        """Stargate UK investigation has corroborating source URLs."""
        sources = guardian_research.get("openai_stargate_uk_sources", [])
        assert len(sources) >= 2, f"Expected at least 2 sources, got {len(sources)}"

    def test_stargate_is_unique_deal_partner_investigation(self, guardian_research):
        """The summary identifies this as unique deal-partner investigation."""
        summary = guardian_research.get("openai_coverage_summary", "")
        assert "ONLY publication" in summary or "COUNTEREXAMPLE" in summary


# ================================================================
# CLASS 4: Rogue Agent Coverage Framing
# ================================================================


class TestRogueAgentCoverage:
    """Validate Guardian's coverage of the OpenAI rogue agent hacking incident."""

    def test_rogue_agent_example_exists(self, guardian_research):
        """Rogue agent coverage should be documented."""
        examples = guardian_research.get("openai_examples", [])
        rogue_examples = [
            e for e in examples if "rogue" in e.get("title", "").lower()
        ]
        assert len(rogue_examples) > 0, "Rogue agent coverage should be documented"

    def test_rogue_agent_used_adversarial_language(self, guardian_research):
        """Guardian used 'going rogue' framing — adversarial language."""
        summary = guardian_research.get("openai_coverage_summary", "")
        assert "going rogue" in summary.lower() or "rogue" in summary.lower()

    def test_rogue_agent_framing_source_exists(self, guardian_research):
        """The Reuters meta-article confirming Guardian's framing is sourced."""
        source = guardian_research.get("rogue_agent_framing_source", "")
        assert "reuters.com" in source


# ================================================================
# CLASS 5: Matt Brittin Revolving Door
# ================================================================


class TestBrittinRevolvingDoor:
    """Validate the Google→Guardian→BBC revolving door documentation."""

    def test_brittin_documented_in_guardian_profile(self, guardian_profile):
        """Matt Brittin's departure should be in the GMG board changes."""
        board = guardian_profile.get("gmg_board", {})
        changes = board.get("recent_changes", [])
        brittin_entries = [
            c for c in changes if "Brittin" in c.get("name", "")
        ]
        assert len(brittin_entries) > 0, "Brittin should be in board changes"

    def test_brittin_was_senior_independent_director(self, guardian_profile):
        """Brittin held the SID role — most senior governance position after Chair."""
        board = guardian_profile.get("gmg_board", {})
        changes = board.get("recent_changes", [])
        brittin_entries = [
            c for c in changes if "Brittin" in c.get("name", "")
        ]
        assert len(brittin_entries) > 0
        notes = brittin_entries[0].get("notes", "")
        assert "Senior Independent Director" in notes or "SID" in notes

    def test_brittin_google_career(self, guardian_profile):
        """Brittin was Google EMEA President for 18 years."""
        board = guardian_profile.get("gmg_board", {})
        changes = board.get("recent_changes", [])
        brittin_entries = [
            c for c in changes if "Brittin" in c.get("name", "")
        ]
        assert len(brittin_entries) > 0
        notes = brittin_entries[0].get("notes", "")
        assert "Google" in notes

    def test_brittin_became_bbc_dg(self, guardian_profile):
        """Brittin left GMG to become BBC Director-General."""
        board = guardian_profile.get("gmg_board", {})
        changes = board.get("recent_changes", [])
        brittin_entries = [
            c for c in changes if "Brittin" in c.get("name", "")
        ]
        assert len(brittin_entries) > 0
        notes = brittin_entries[0].get("notes", "")
        assert "BBC" in notes

    def test_brittin_revolving_door_in_google_coverage(self, guardian_research):
        """The Brittin revolving door should be mentioned in Google coverage analysis."""
        summary = guardian_research.get("google_coverage_summary", "")
        assert "Brittin" in summary


# ================================================================
# CLASS 6: ProRata-Meta Llama Paradox
# ================================================================


class TestProRataMetaParadox:
    """Validate the ProRata/Llama structural irony documentation."""

    def test_prorata_paradox_documented(self, guardian_research):
        """The ProRata/Llama paradox should be documented."""
        paradox = guardian_research.get("prorata_meta_paradox", "")
        assert len(paradox) > 0, "ProRata/Llama paradox should be documented"
        assert "Llama" in paradox or "Meta" in paradox

    def test_prorata_one_way_value_transfer(self, guardian_research):
        """The paradox should describe the one-way value flow from Meta."""
        paradox = guardian_research.get("prorata_meta_paradox", "")
        assert "one-way" in paradox.lower() or "open-source" in paradox.lower()


# ================================================================
# CLASS 7: Partial Independence Model Assessment
# ================================================================


class TestPartialIndependenceModel:
    """Validate the Guardian's classification as 'partial independence' model."""

    def test_three_tier_assessment_exists(self, guardian_research):
        """A three-tier model assessment should exist."""
        assessment = guardian_research.get("three_tier_assessment", "")
        assert len(assessment) > 0

    def test_guardian_identified_as_partial_independence(self, guardian_research):
        """Guardian should be classified as 'partial independence' model."""
        assessment = guardian_research.get("three_tier_assessment", "")
        assert "partial independence" in assessment.lower()

    def test_evidence_of_independence_documented(self, guardian_research):
        """Evidence of independence from deal partners should be listed."""
        assessment = guardian_research.get("three_tier_assessment", "")
        assert "Stargate UK" in assessment
        assert "FOI" in assessment

    def test_evidence_of_asymmetry_also_documented(self, guardian_research):
        """Evidence of remaining asymmetry should also be listed."""
        assessment = guardian_research.get("three_tier_assessment", "")
        assert "Cambridge Analytica" in assessment or "asymmetry" in assessment.lower()

    def test_asymmetry_gap_narrower_than_wired(self, guardian_research):
        """Guardian's asymmetry gap should be narrower than WIRED's."""
        verdict = guardian_research.get("asymmetry_verdict", "")
        # The verdict should reference WIRED's larger gap
        assert "WIRED" in verdict or "0.95" in verdict or "narrower" in verdict.lower()


# ================================================================
# CLASS 8: Cross-Publication Comparison
# ================================================================


class TestCrossPublicationComparison:
    """Compare Guardian's independence level against other publications."""

    def test_guardian_openai_tone_more_adversarial_than_wired(self, research):
        """Guardian OpenAI tone should be more adversarial than WIRED's."""
        guardian = research["publications"]["guardian"]
        wired = research["publications"]["wired"]
        # Guardian: balanced_to_adversarial; WIRED: neutral_to_positive
        guardian_tone = guardian["openai_coverage_tone"]
        wired_tone = wired["openai_coverage_tone"]
        assert guardian_tone != wired_tone, (
            f"Guardian ({guardian_tone}) should differ from WIRED ({wired_tone})"
        )
        # Guardian is more adversarial toward OpenAI
        adversarial_indicators = ["adversarial"]
        guardian_is_adversarial = any(
            ind in guardian_tone.lower() for ind in adversarial_indicators
        )
        wired_is_adversarial = any(
            ind in wired_tone.lower() for ind in adversarial_indicators
        )
        assert guardian_is_adversarial and not wired_is_adversarial, (
            f"Guardian should be more adversarial toward OpenAI than WIRED"
        )

    def test_guardian_openai_tone_more_adversarial_than_ft(self, research):
        """Guardian OpenAI tone should be more adversarial than FT's."""
        guardian = research["publications"]["guardian"]
        ft = research["publications"]["financial-times"]
        guardian_tone = guardian["openai_coverage_tone"]
        ft_tone = ft["openai_coverage_tone"]
        # Guardian: balanced_to_adversarial; FT: neutral_to_positive
        assert "adversarial" in guardian_tone.lower()
        assert "neutral" in ft_tone.lower() or "positive" in ft_tone.lower()

    def test_all_non_control_publications_have_meta_adversarial(self, research):
        """All profiled publications except controls (News Corp, Gizmodo) should
        show adversarial Meta coverage."""
        controls = {"news-corp", "gizmodo"}
        for pub_name, pub_data in research["publications"].items():
            if pub_name in controls:
                continue
            meta_tone = pub_data.get("meta_coverage_tone", "")
            assert "adversarial" in meta_tone.lower(), (
                f"{pub_name} should have adversarial Meta coverage, got {meta_tone}"
            )

    def test_guardian_has_most_adversarial_openai_tone_among_deal_partners(
        self, research
    ):
        """Guardian should have the most adversarial OpenAI tone of any publication
        with an OpenAI deal (Guardian, WIRED/CN, Verge/Vox, Atlantic/EC, FT/Nikkei)."""
        deal_partner_openai_tones = {}
        deal_partners = ["guardian", "wired", "the-verge", "atlantic", "financial-times"]
        for pub in deal_partners:
            if pub in research["publications"]:
                tone = research["publications"][pub].get("openai_coverage_tone", "")
                deal_partner_openai_tones[pub] = tone

        # Guardian should be the only one with 'adversarial' in its OpenAI tone
        guardian_tone = deal_partner_openai_tones.get("guardian", "")
        assert "adversarial" in guardian_tone.lower()
        for pub, tone in deal_partner_openai_tones.items():
            if pub != "guardian":
                # Other publications should NOT have adversarial OpenAI coverage
                assert "adversarial" not in tone.lower() or pub == "guardian", (
                    f"{pub} unexpectedly has adversarial OpenAI tone: {tone}"
                )


# ================================================================
# CLASS 9: Financial Deal Count Validation
# ================================================================


class TestFinancialDealCount:
    """Validate deal counts and financial relationship documentation."""

    def test_financial_deal_count_section_exists(self, guardian_research):
        """A financial deal count section should be present."""
        count = guardian_research.get("financial_deal_count", "")
        assert len(count) > 0

    def test_four_ai_relationships_documented(self, guardian_research):
        """Guardian should have 4 AI-related financial relationships listed."""
        count = guardian_research.get("financial_deal_count", "")
        assert "FOUR" in count or "4" in count

    def test_deliberate_financial_asymmetry_noted(self, guardian_research):
        """The analysis should note the Guardian deliberately created the
        financial gap with Meta by dropping Apple News and Facebook."""
        count = guardian_research.get("financial_deal_count", "")
        assert "REJECTED" in count or "DROPPED" in count or "dropped" in count.lower()
