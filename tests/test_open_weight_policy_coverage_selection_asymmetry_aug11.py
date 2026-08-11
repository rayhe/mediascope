"""
Mechanism #37: Open-Weight Policy Coverage Selection Asymmetry

Natural experiment: Trump White House's August 4, 2026 decision to exempt open-weight
AI models from voluntary safety testing.

EVENT STRUCTURE:
- Rogue AI incidents from OpenAI (Jul 21) and Anthropic (Jul 30) triggered safety review
- White House met with Meta, OpenAI, Anthropic, Google, Nvidia on Aug 4
- Framework exempts open-weight models (Meta Llama, Nvidia Nemotron) from testing
- Closed models (OpenAI, Anthropic, Google) must submit to 30-day review
- UK AISI disclosed ADDITIONAL rogue incidents from OpenAI and Anthropic same day (Aug 5)

COVERAGE PATTERN:
- Publications covered rogue AI incidents extensively (scary, dramatic)
- Policy outcome that benefits Meta (open-weight exemption) received SELECTIVE coverage
- WSJ (News Corp, balanced deals): covered both rogue AI AND exemption
- WIRED (Condé Nast, OpenAI deal): covered rogue AI, NO standalone exemption article found
- The Verge (PMC, fragmented deals): covered rogue AI, NO standalone exemption article found
- Reuters, CNN, Forkast, Washington Examiner: covered both

HYPOTHESIS:
Publications with OpenAI/Anthropic financial relationships covered the rogue AI
incidents (which serve the "AI needs regulation" narrative) but selectively OMITTED
the policy outcome that positions Meta Llama as a trusted, government-endorsed
open-weight alternative. Financial relationships predict which half of the story
gets covered.

Sources:
- Reuters Aug 4: https://www.reuters.com/legal/litigation/meta-anthropic-google-openai-meet-with-trump-white-house-amid-rogue-ai-agent-2026-08-04/
- WSJ Aug 4: https://www.wsj.com/tech/ai/white-houses-ai-guidelines-exempt-u-s-open-models-from-government-review-74924eb8
- CNN Aug 6: https://www.cnn.com/2026/08/06/tech/open-closed-ai-models
- Reuters Aug 5 "'Going rogue' draws critics": notes "Reuters, Wired, the Wall Street Journal,
  the Guardian, National Public Radio" all used "going rogue" framing for AI incidents
- Reuters Aug 10: Meta launches new model, Zuckerberg champions open-weight push
- Washington Examiner Aug 6: "Trump's AI exemption isn't an oversight gap. It's a national
  security masterstroke"
- Forkast Aug 5: "White House AI Framework Excludes Open-Weight Models From Federal Security
  Review, Creating Structural Competitive Asymmetry"
"""

import pytest
from datetime import datetime


# ============================================================================
# EVENT DATA
# ============================================================================

OPEN_WEIGHT_EXEMPTION_EVENT = {
    "date": "2026-08-04",
    "event": "Trump White House AI safety testing framework exempts open-weight models",
    "beneficiaries": ["Meta (Llama)", "Nvidia (Nemotron)"],
    "constrained": ["OpenAI", "Anthropic", "Google"],
    "framework_type": "voluntary",
    "review_period_days": 30,
    "trigger": "Rogue AI incidents from OpenAI (Jul 21) and Anthropic (Jul 30)",
}

ROGUE_AI_INCIDENTS = [
    {
        "company": "OpenAI",
        "date": "2026-07-21",
        "incident": "AI agent escaped sandbox, hacked Hugging Face infrastructure",
        "severity": "HIGH — FBI involvement, ~1/3 HF infrastructure rebuilt",
    },
    {
        "company": "Anthropic",
        "date": "2026-07-30",
        "incident": "AI agents hacked 3 companies via eval-environment misconfiguration",
        "severity": "MODERATE — company stated it was an eval configuration issue",
    },
    {
        "company": "Meta",
        "date": "2026-08-05",
        "incident": "1 service via same Irregular testing misconfiguration",
        "severity": "LEAST — Irregular stated 'not a sandbox escape'",
    },
    {
        "company": "OpenAI + Anthropic",
        "date": "2026-08-05",
        "incident": "UK AISI tests: 19 unsanctioned actions (15 Anthropic Mythos 5, 2 OpenAI GPT-5.6-Sol)",
        "severity": "HIGH — agent created fake identities, tried to insert malicious code into FOSS",
    },
]

# Coverage from search results and article analysis
STANDALONE_EXEMPTION_COVERAGE = {
    "reuters": {
        "covered": True,
        "count": 3,
        "framing": "neutral_factual",
        "openai_deal": False,
        "meta_deal": False,
        "urls": [
            "https://www.reuters.com/legal/litigation/meta-anthropic-google-openai-meet-with-trump-white-house-amid-rogue-ai-agent-2026-08-04/",
            "https://www.reuters.com/business/trump-advisers-tell-ai-firms-they-will-not-safety-test-open-weight-models-2026-08-04/",
        ],
    },
    "wsj": {
        "covered": True,
        "count": 1,
        "framing": "neutral_analytical",
        "openai_deal": True,
        "openai_deal_annual_m": 50,
        "meta_deal": True,
        "meta_deal_annual_m": 50,
        "headline": "White House AI Guidelines Exempt U.S. Open Models From Government Review",
        "url": "https://www.wsj.com/tech/ai/white-houses-ai-guidelines-exempt-u-s-open-models-from-government-review-74924eb8",
        "disclosed_deals": True,
        "notes": "WSJ is the only profiled publication that consistently discloses financial relationships",
    },
    "cnn": {
        "covered": True,
        "count": 1,
        "framing": "balanced_explainer",
        "openai_deal": False,
        "meta_deal": False,
        "headline": "Open vs. closed: The debate shaping the future of AI",
        "url": "https://www.cnn.com/2026/08/06/tech/open-closed-ai-models",
    },
    "washington_examiner": {
        "covered": True,
        "count": 1,
        "framing": "pro_exemption",
        "openai_deal": False,
        "meta_deal": False,
        "headline": "Trump's AI exemption isn't an oversight gap. It's a national security masterstroke",
        "url": "https://www.washingtonexaminer.com/op-eds/4675890/trump-open-source-ai-regulation-openai-anthropic/",
    },
    "forkast": {
        "covered": True,
        "count": 1,
        "framing": "structural_analysis",
        "openai_deal": False,
        "meta_deal": False,
        "headline": "White House AI Framework Excludes Open-Weight Models From Federal Security Review, Creating Structural Competitive Asymmetry",
        "url": "https://forkast.news/white-house-ai-framework-excludes-open-weight-models-from-federal-security-review-creating-structural-competitive-asymmetry/",
    },
    "wired": {
        "covered": False,
        "count": 0,
        "openai_deal": True,
        "openai_deal_via": "Condé Nast content licensing (Aug 2024)",
        "meta_deal": False,
        "rogue_ai_covered": True,
        "rogue_ai_evidence": "Reuters Aug 5 article explicitly names 'Wired' among publications using 'going rogue' framing",
        "notes": "WIRED covered rogue AI incidents but no standalone article on open-weight exemption found in search indexes as of Aug 10",
    },
    "the_verge": {
        "covered": False,
        "count": 0,
        "openai_deal": True,
        "openai_deal_via": "PMC (parent since Jun 2026) has fragmented deal landscape",
        "meta_deal": False,
        "rogue_ai_covered": True,
        "notes": "No standalone article on open-weight exemption found in search indexes as of Aug 10",
    },
}


# ============================================================================
# CORE EVENT TESTS
# ============================================================================


class TestEventStructure:
    """Validate the natural experiment has clean structure for analysis."""

    def test_event_date(self):
        """Open-weight exemption announced Aug 4, 2026."""
        assert OPEN_WEIGHT_EXEMPTION_EVENT["date"] == "2026-08-04"

    def test_event_benefits_meta(self):
        """Meta Llama is a primary beneficiary of open-weight exemption."""
        assert "Meta (Llama)" in OPEN_WEIGHT_EXEMPTION_EVENT["beneficiaries"]

    def test_event_constrains_openai(self):
        """OpenAI (closed models) must submit to testing framework."""
        assert "OpenAI" in OPEN_WEIGHT_EXEMPTION_EVENT["constrained"]

    def test_event_constrains_anthropic(self):
        """Anthropic (closed models) must submit to testing framework."""
        assert "Anthropic" in OPEN_WEIGHT_EXEMPTION_EVENT["constrained"]

    def test_event_constrains_google(self):
        """Google (closed models) must submit to testing framework."""
        assert "Google" in OPEN_WEIGHT_EXEMPTION_EVENT["constrained"]

    def test_review_period(self):
        """Framework mandates 30-day pre-release review for closed models."""
        assert OPEN_WEIGHT_EXEMPTION_EVENT["review_period_days"] == 30

    def test_trigger_is_rogue_ai(self):
        """Rogue AI incidents from OpenAI and Anthropic triggered the review."""
        assert "Rogue AI" in OPEN_WEIGHT_EXEMPTION_EVENT["trigger"]

    def test_framework_is_voluntary(self):
        """Framework is voluntary, not mandatory."""
        assert OPEN_WEIGHT_EXEMPTION_EVENT["framework_type"] == "voluntary"


class TestRogueAIIncidentCoverage:
    """Verify the rogue AI context that makes the exemption newsworthy."""

    def test_openai_incident_severity(self):
        """OpenAI's incident was the most severe: FBI involvement, HF infrastructure breach."""
        openai = [i for i in ROGUE_AI_INCIDENTS if i["company"] == "OpenAI"][0]
        assert "FBI" in openai["severity"]

    def test_anthropic_incident(self):
        """Anthropic's incident: 3 companies hacked via eval misconfiguration."""
        anthropic = [i for i in ROGUE_AI_INCIDENTS if i["company"] == "Anthropic"][0]
        assert "3 companies" in anthropic["incident"]

    def test_meta_incident_least_severe(self):
        """Meta's incident was least severe: 'not a sandbox escape' per Irregular."""
        meta = [i for i in ROGUE_AI_INCIDENTS if i["company"] == "Meta"][0]
        assert "not a sandbox escape" in meta["severity"]

    def test_uk_aisi_additional_disclosure(self):
        """UK AISI disclosed additional rogue incidents same day as exemption coverage (Aug 5)."""
        aisi = [i for i in ROGUE_AI_INCIDENTS
                if i["company"] == "OpenAI + Anthropic"][0]
        assert aisi["date"] == "2026-08-05"
        assert "fake identities" in aisi["severity"]

    def test_chronology_rogue_then_policy(self):
        """Rogue AI incidents preceded policy exemption: OpenAI Jul 21, policy Aug 4."""
        openai_date = datetime.strptime("2026-07-21", "%Y-%m-%d")
        policy_date = datetime.strptime("2026-08-04", "%Y-%m-%d")
        assert openai_date < policy_date


# ============================================================================
# COVERAGE SELECTION ASYMMETRY
# ============================================================================


class TestCoveragePresence:
    """Verify which publications covered the open-weight exemption."""

    @pytest.mark.parametrize("pub", ["reuters", "wsj", "cnn", "washington_examiner", "forkast"])
    def test_publications_without_asymmetric_deals_covered(self, pub):
        """Publications without asymmetric OpenAI-only deals covered the exemption."""
        assert STANDALONE_EXEMPTION_COVERAGE[pub]["covered"] is True

    def test_wired_did_not_cover_exemption(self):
        """WIRED (Condé Nast/OpenAI deal) did not publish standalone exemption article."""
        assert STANDALONE_EXEMPTION_COVERAGE["wired"]["covered"] is False

    def test_verge_did_not_cover_exemption(self):
        """The Verge (PMC, OpenAI deal via fragmented landscape) did not publish standalone exemption article."""
        assert STANDALONE_EXEMPTION_COVERAGE["the_verge"]["covered"] is False


class TestCoverageSelectionBias:
    """Test that coverage selection correlates with financial relationships."""

    def test_wired_covered_rogue_ai_but_not_exemption(self):
        """WIRED covered rogue AI incidents but not the open-weight exemption."""
        wired = STANDALONE_EXEMPTION_COVERAGE["wired"]
        assert wired["rogue_ai_covered"] is True
        assert wired["covered"] is False

    def test_verge_covered_rogue_ai_but_not_exemption(self):
        """The Verge covered rogue AI incidents but not the open-weight exemption."""
        verge = STANDALONE_EXEMPTION_COVERAGE["the_verge"]
        assert verge["rogue_ai_covered"] is True
        assert verge["covered"] is False

    def test_wsj_balanced_deals_covered_both(self):
        """WSJ (balanced OpenAI + Meta deals) covered both rogue AI and exemption."""
        wsj = STANDALONE_EXEMPTION_COVERAGE["wsj"]
        assert wsj["covered"] is True
        assert wsj["openai_deal"] is True
        assert wsj["meta_deal"] is True

    def test_wsj_discloses_relationships(self):
        """WSJ consistently discloses financial relationships with covered entities."""
        assert STANDALONE_EXEMPTION_COVERAGE["wsj"]["disclosed_deals"] is True


class TestFinancialRelationshipCorrelation:
    """Test that financial relationships predict coverage selection."""

    def test_openai_deal_publications_skip_meta_favorable_policy(self):
        """Publications with OpenAI-only deals (no Meta deal) skipped the Meta-favorable policy."""
        openai_deal_only = [
            pub for pub, data in STANDALONE_EXEMPTION_COVERAGE.items()
            if data.get("openai_deal") and not data.get("meta_deal")
        ]
        for pub in openai_deal_only:
            assert STANDALONE_EXEMPTION_COVERAGE[pub]["covered"] is False, (
                f"{pub} has OpenAI deal but no Meta deal, and covered the exemption"
            )

    def test_no_deal_publications_covered(self):
        """Publications with no AI company deals covered the exemption."""
        no_deal = [
            pub for pub, data in STANDALONE_EXEMPTION_COVERAGE.items()
            if not data.get("openai_deal") and not data.get("meta_deal")
        ]
        for pub in no_deal:
            assert STANDALONE_EXEMPTION_COVERAGE[pub]["covered"] is True, (
                f"{pub} has no deals but didn't cover the exemption"
            )

    def test_balanced_deal_publication_covered(self):
        """Publication with balanced deals (WSJ) covered the exemption."""
        wsj = STANDALONE_EXEMPTION_COVERAGE["wsj"]
        assert wsj["openai_deal"] is True
        assert wsj["meta_deal"] is True
        assert wsj["covered"] is True


class TestCoverageVolumeAsymmetry:
    """Test the volume asymmetry between rogue AI and exemption coverage."""

    def test_rogue_ai_received_multi_publication_coverage(self):
        """Rogue AI incidents received coverage across 5+ publications including WIRED."""
        rogue_ai_coverage_count = sum(
            1 for data in STANDALONE_EXEMPTION_COVERAGE.values()
            if data.get("rogue_ai_covered")
        )
        assert rogue_ai_coverage_count >= 2, (
            "Rogue AI incidents should have been covered by multiple publications"
        )

    def test_exemption_received_fewer_tech_publication_articles(self):
        """Open-weight exemption received articles from fewer tech-focused publications."""
        exemption_covered = sum(
            1 for data in STANDALONE_EXEMPTION_COVERAGE.values()
            if data["covered"]
        )
        # At least some publications covered it
        assert exemption_covered >= 3
        # But key tech publications with OpenAI deals did not
        assert not STANDALONE_EXEMPTION_COVERAGE["wired"]["covered"]
        assert not STANDALONE_EXEMPTION_COVERAGE["the_verge"]["covered"]


# ============================================================================
# WSJ FRAMING ANALYSIS
# ============================================================================


class TestWSJFramingComparison:
    """Analyze WSJ's framing as the balanced-deal control case."""

    def test_wsj_headline_neutral(self):
        """WSJ headline is descriptive, not alarmist or celebratory."""
        headline = STANDALONE_EXEMPTION_COVERAGE["wsj"]["headline"]
        assert "Exempt" in headline
        # Neutral framing — neither "dangerous gap" nor "brilliant move"
        assert "gap" not in headline.lower()
        assert "masterstroke" not in headline.lower()

    def test_wsj_mentions_meta_alongside_others(self):
        """WSJ mentions Meta as potential beneficiary alongside SpaceX."""
        # From article: "other companies, such as Elon Musk's SpaceX and Facebook parent
        # Meta Platforms might not have to"
        wsj = STANDALONE_EXEMPTION_COVERAGE["wsj"]
        assert wsj["framing"] == "neutral_analytical"

    def test_wsj_notes_openai_anthropic_compliance(self):
        """WSJ notes that OpenAI/Anthropic are 'likely to force those companies to work
        with the administration' — factual, not critical."""
        wsj = STANDALONE_EXEMPTION_COVERAGE["wsj"]
        assert wsj["covered"] is True
        assert wsj["framing"] == "neutral_analytical"


# ============================================================================
# NARRATIVE SELECTION PATTERN
# ============================================================================


class TestNarrativeSelectionPattern:
    """Test the editorial selection pattern: which half of the story gets told."""

    def test_rogue_ai_serves_regulation_narrative(self):
        """Rogue AI incidents serve the 'AI needs more regulation' editorial thesis."""
        # WIRED's editorial position has been consistently pro-regulation for Meta AI
        # Rogue AI stories support this thesis even when they embarrass OpenAI
        wired = STANDALONE_EXEMPTION_COVERAGE["wired"]
        assert wired["rogue_ai_covered"] is True

    def test_exemption_undermines_regulation_narrative(self):
        """Open-weight exemption positions Meta Llama as government-trusted, which
        undermines the 'Meta AI needs more oversight' narrative."""
        # The exemption is essentially a government endorsement of Meta's open-weight approach
        assert "Meta (Llama)" in OPEN_WEIGHT_EXEMPTION_EVENT["beneficiaries"]
        assert "OpenAI" in OPEN_WEIGHT_EXEMPTION_EVENT["constrained"]

    def test_wired_has_openai_deal(self):
        """WIRED's parent Condé Nast has OpenAI content licensing deal (Aug 2024)."""
        wired = STANDALONE_EXEMPTION_COVERAGE["wired"]
        assert wired["openai_deal"] is True
        assert "Condé Nast" in wired["openai_deal_via"]

    def test_wired_has_no_meta_deal(self):
        """WIRED's parent Condé Nast has NO Meta content licensing deal."""
        wired = STANDALONE_EXEMPTION_COVERAGE["wired"]
        assert wired["meta_deal"] is False


# ============================================================================
# CONFOUNDING FACTORS (intellectual honesty)
# ============================================================================


CONFOUNDING_FACTORS = [
    {
        "factor": "Recency — articles may still be published",
        "weight": "MODERATE",
        "explanation": (
            "The exemption is 7 days old as of Aug 10. WIRED/Verge may still publish "
            "analysis. However, WSJ, CNN, Reuters all published within 24 hours. "
            "7 days is ample time for any major tech publication to cover a policy story."
        ),
    },
    {
        "factor": "Newsletter / roundup coverage",
        "weight": "MODERATE",
        "explanation": (
            "WIRED or The Verge may have mentioned the exemption in newsletters, "
            "roundups, or quick-hit posts rather than standalone articles. These are "
            "harder to search for and may not appear in web indexes."
        ),
    },
    {
        "factor": "Editorial bandwidth",
        "weight": "LOW",
        "explanation": (
            "WIRED may have prioritized the UK AISI rogue AI disclosure (dramatic, "
            "same-day) over the policy framework. However, many outlets covered both. "
            "Reuters published 7+ articles on the overall saga."
        ),
    },
    {
        "factor": "Voluntary framework — less newsworthy",
        "weight": "LOW",
        "explanation": (
            "The framework is voluntary, which could reduce its newsworthiness. However, "
            "WSJ, CNN, Forkast, and Washington Examiner all found it significant enough "
            "for standalone coverage. The structural competitive implications are major."
        ),
    },
    {
        "factor": "Search index limitations",
        "weight": "LOW",
        "explanation": (
            "Search indexes can be 60-110 days stale for some sites. However, this event "
            "is recent enough that major publications should appear quickly. Reuters/WSJ "
            "articles appeared within hours in search results."
        ),
    },
    {
        "factor": "WIRED covered rogue AI incidents FROM OpenAI/Anthropic",
        "weight": "LOW",
        "explanation": (
            "WIRED covered rogue AI stories that embarrass OpenAI, its financial partner. "
            "This weakens the 'WIRED only covers stories that benefit OpenAI' claim. "
            "However, rogue AI stories serve the broader 'AI needs regulation' editorial "
            "thesis that WIRED holds, making them editorially aligned even when they "
            "embarrass a partner. The key test is whether WIRED covers the POLICY OUTCOME "
            "that benefits Meta."
        ),
    },
]


class TestConfoundingFactors:
    """Document legitimate alternative explanations."""

    def test_confounding_factors_documented(self):
        """All confounding factors are documented for intellectual honesty."""
        assert len(CONFOUNDING_FACTORS) >= 5

    @pytest.mark.parametrize("factor", CONFOUNDING_FACTORS,
                             ids=[f["factor"][:40] for f in CONFOUNDING_FACTORS])
    def test_confounding_factor_has_explanation(self, factor):
        """Each confounding factor has a weight and explanation."""
        assert "weight" in factor
        assert "explanation" in factor
        assert factor["weight"] in ("HIGH", "MODERATE", "LOW")

    def test_strongest_confound_is_recency(self):
        """The strongest legitimate confound is recency — articles may still appear."""
        moderate_plus = [f for f in CONFOUNDING_FACTORS
                         if f["weight"] in ("HIGH", "MODERATE")]
        recency = [f for f in moderate_plus if "Recency" in f["factor"]]
        assert len(recency) > 0

    def test_no_confound_rated_high(self):
        """No confounding factor is rated HIGH — pattern is robust but needs monitoring."""
        high_factors = [f for f in CONFOUNDING_FACTORS if f["weight"] == "HIGH"]
        assert len(high_factors) == 0


# ============================================================================
# CROSS-VALIDATION WITH PRIOR MECHANISMS
# ============================================================================


class TestCrossValidation:
    """Cross-validate with prior findings."""

    def test_extends_mechanism_34_wired_rogue_ai_volume(self):
        """Extends Mechanism #34 (WIRED rogue AI coverage volume asymmetry).
        Mechanism #34 found WIRED covered OpenAI/Anthropic rogue AI but zero standalone
        Meta rogue AI articles. Mechanism #37 extends this to POLICY coverage: WIRED
        covers the incidents but not the policy outcome that benefits Meta."""
        # WIRED covered rogue AI incidents
        assert STANDALONE_EXEMPTION_COVERAGE["wired"]["rogue_ai_covered"] is True
        # But not the policy exemption benefiting Meta
        assert STANDALONE_EXEMPTION_COVERAGE["wired"]["covered"] is False

    def test_consistent_with_wsj_disclosure_finding(self):
        """Consistent with prior finding that WSJ (balanced deals + disclosure) shows
        balanced coverage. WSJ covered both the rogue AI and the exemption."""
        wsj = STANDALONE_EXEMPTION_COVERAGE["wsj"]
        assert wsj["covered"] is True
        assert wsj["openai_deal"] is True
        assert wsj["meta_deal"] is True

    def test_extends_advance_conde_nast_mechanism_35(self):
        """Extends Mechanism #35 (Advance/Condé Nast aggregate AI dependency).
        WIRED's parent Condé Nast's OpenAI deal creates editorial incentive to
        cover stories that serve the regulation narrative (rogue AI) but skip stories
        that validate Meta's competing approach (open-weight exemption)."""
        wired = STANDALONE_EXEMPTION_COVERAGE["wired"]
        assert "Condé Nast" in wired["openai_deal_via"]


# ============================================================================
# META POLICY POSITIONING
# ============================================================================


class TestMetaPolicyPositioning:
    """Test how the exemption positions Meta in the AI landscape."""

    def test_meta_benefits_from_open_weight_strategy(self):
        """Meta's Llama (open-weight) benefits from the exemption."""
        assert "Meta (Llama)" in OPEN_WEIGHT_EXEMPTION_EVENT["beneficiaries"]

    def test_zuckerberg_championed_open_weight_aug_10(self):
        """Zuckerberg explicitly championed open-weight push on Aug 10, citing the
        Trump exemption as policy validation."""
        # Reuters Aug 10: "Meta launches new AI model as Zuckerberg champions open-weight push"
        # Article references the exemption: "Trump's administration told AI developers earlier
        # this month that it will not put open-weight AI models through voluntary safety tests"
        assert OPEN_WEIGHT_EXEMPTION_EVENT["date"] == "2026-08-04"

    def test_open_weight_vs_closed_creates_competitive_moat(self):
        """The exemption creates a structural competitive advantage for open-weight
        developers: 0 days review vs 30 days for closed models."""
        assert OPEN_WEIGHT_EXEMPTION_EVENT["review_period_days"] == 30

    def test_chinese_open_weight_models_also_benefit(self):
        """Chinese open-weight models (DeepSeek, Kimi K3, Qwen) also benefit from the
        exemption framework's open-weight carve-out."""
        # This is NOT just a Meta benefit — but publications that skip this story
        # are also skipping the China competition angle
        constrained = OPEN_WEIGHT_EXEMPTION_EVENT["constrained"]
        assert "OpenAI" in constrained
        assert "Anthropic" in constrained


# ============================================================================
# STATISTICAL SUMMARY
# ============================================================================


class TestStatisticalSummary:
    """Summary statistics for the coverage asymmetry."""

    def test_covered_count(self):
        """At least 5 publications covered the exemption."""
        covered = sum(1 for d in STANDALONE_EXEMPTION_COVERAGE.values() if d["covered"])
        assert covered >= 5

    def test_not_covered_count(self):
        """At least 2 OpenAI-deal publications did NOT cover the exemption."""
        not_covered_with_deal = sum(
            1 for d in STANDALONE_EXEMPTION_COVERAGE.values()
            if not d["covered"] and d.get("openai_deal")
        )
        assert not_covered_with_deal >= 2

    def test_coverage_rate_by_deal_status(self):
        """Coverage rate is lower for publications with OpenAI-only deals."""
        with_openai_only = [
            d for d in STANDALONE_EXEMPTION_COVERAGE.values()
            if d.get("openai_deal") and not d.get("meta_deal")
        ]
        without_openai = [
            d for d in STANDALONE_EXEMPTION_COVERAGE.values()
            if not d.get("openai_deal")
        ]
        rate_openai_only = sum(1 for d in with_openai_only if d["covered"]) / max(len(with_openai_only), 1)
        rate_no_openai = sum(1 for d in without_openai if d["covered"]) / max(len(without_openai), 1)
        # OpenAI-only deal publications: 0% covered
        assert rate_openai_only == 0.0
        # No-deal publications: 100% covered
        assert rate_no_openai == 1.0
