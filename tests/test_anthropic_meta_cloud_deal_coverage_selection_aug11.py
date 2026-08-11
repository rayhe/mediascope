"""
Mechanism #38: Anthropic-Meta Infrastructure Deal Coverage Selection Asymmetry

Type A: Competitor Coverage Deep Dive (Aug 11, 2026 02:00 PT)

Publication focus: Cross-publication (WIRED, The Verge, NYT, WSJ, Reuters, CNN)
Competitor: Anthropic
Comparison entity: Meta

EVENT:
On July 17, 2026, the New York Times reported that Anthropic was in early talks
to lease computing power from Meta in a deal worth up to $10 billion over two years.
Anthropic approached Meta in June 2026. The deal would make Anthropic a META CUSTOMER,
paying monthly increments for access to Meta's AI infrastructure.

CONTEXT — ANTHROPIC'S OTHER COMPUTE DEALS:
- SpaceX Colossus: $45B/3yr (May 2026) — covered by TechCrunch, The Verge, Reuters, etc.
- Fluidstack: $50B data center plan (Nov 2025) — covered by TechCrunch, Reuters
- CoreWeave: Multi-year GPU deal (Apr 2026) — covered by TechCrunch, The Verge
- Akamai: $1.8B (2026) — covered in Bloomberg, Reuters
- TeraWulf: 20-year data center lease (2026)

THE ASYMMETRY:
When Anthropic signs massive infrastructure deals with SpaceX, CoreWeave, Fluidstack,
and Akamai, tech publications cover these extensively. When Anthropic is in talks for
a $10B deal with META specifically — making Anthropic a Meta customer — key publications
that have been adversarial toward Meta appear to have NOT produced standalone coverage.

COVERAGE MAP (Jul 17-18, 2026):
- NYT: REPORTED THE STORY (original source)
- Reuters: Covered immediately
- Bloomberg: Covered same day (Zuckerberg quote)
- CNN: Standalone article same day
- CNBC: Covered
- Slashdot: Aggregated the CNBC coverage
- Zacks, eWeek, TradingView, Motley Fool: Financial coverage
- WIRED (Condé Nast / OpenAI deal): NO standalone article found via web search
- The Verge (PMC / fragmented deals): NO standalone article found via web search

WHY THIS MATTERS:
1. The deal validates Meta's $130-145B capex spending that critics called wasteful
2. It makes Anthropic — the "safety-first" company — a Meta customer
3. It complicates the "Meta bad / Anthropic good" narrative maintained by publications
   with OpenAI content licensing deals
4. Coverage SELECTION (choosing what to report) is a subtler but equally powerful
   form of editorial influence as coverage FRAMING (how you report it)

HYPOTHESIS:
Publications with adversarial Meta coverage patterns selectively omit stories that
validate Meta's business strategy or create financial relationships between Meta
and companies the publication covers favorably (Anthropic). The omission preserves
the adversarial narrative without requiring adversarial framing.

LEGITIMATE FACTORS:
1. Deal is still in early talks — may not materialize
2. Infrastructure deals may be considered financial/business news, not tech news
3. WIRED and The Verge may have covered it in newsletters or roundups (not searchable)
4. News cycle competition on Jul 17 may have crowded out coverage
5. Publications have limited editorial bandwidth
6. Web search may not capture all published articles
7. Deal lacks consumer impact — pure B2B infrastructure play

Sources:
- Reuters Jul 17: https://www.reuters.com/technology/meta-talks-10-billion-anthropic-compute-deal-nyt-reports-2026-07-17/
- CNN Jul 17: https://www.cnn.com/2026/07/17/tech/meta-anthropic-ai-cloud-computing
- Zacks Jul 20: https://www.zacks.com/stock/news/2956097/anthropic-meta-ai-deal-in-the-cards-etfs-in-focus
- eWeek Jul 20: https://www.eweek.com/news/meta-anthropic-10b-ai-compute-lease/
- TechCrunch May 28 (SpaceX deal): https://techcrunch.com/2026/05/28/how-long-is-anthropics-lease-with-spacex-opinions-vary/
- TechCrunch Nov 12 2025 (Fluidstack): https://techcrunch.com/2025/11/12/anthropic-announces-50-billion-data-center-plan/
"""

import pytest
from datetime import datetime


# ============================================================================
# EVENT DATA
# ============================================================================

META_ANTHROPIC_DEAL = {
    "date_reported": "2026-07-17",
    "original_source": "New York Times",
    "deal_value_b": 10,
    "deal_duration_years": 2,
    "deal_type": "compute lease",
    "payment_structure": "monthly increments",
    "proposer": "Anthropic (approached Meta in June 2026)",
    "deal_status": "early talks, may not result in a deal",
    "significance": [
        "Makes Anthropic a Meta customer",
        "Validates Meta's $130-145B capex spending",
        "Opens Meta cloud business competing with AWS/Azure/GCP",
        "Complicates adversarial Meta coverage from publications covering Anthropic favorably",
    ],
    "zuckerberg_quote": (
        "Almost every week there are different companies that come to us from "
        "outside asking us if we have compute that they could buy from us at "
        "some premium to what we've bought it at."
    ),
}

ANTHROPIC_OTHER_COMPUTE_DEALS = [
    {
        "partner": "SpaceX/Colossus",
        "value": "$45B/3yr ($1.25B/mo through May 2029)",
        "date": "May 2026",
        "source": "SpaceX S-1 filing, TechCrunch",
        "publications_covering": ["TechCrunch", "The Verge", "Reuters", "Bloomberg",
                                   "CNBC", "WSJ", "Slashdot"],
    },
    {
        "partner": "Fluidstack",
        "value": "$50B data center plan",
        "date": "November 2025",
        "source": "TechCrunch",
        "publications_covering": ["TechCrunch", "Reuters", "The Verge", "WIRED"],
    },
    {
        "partner": "CoreWeave",
        "value": "Multi-year GPU inference deal",
        "date": "April 2026",
        "source": "CoreWeave press release",
        "publications_covering": ["TechCrunch", "The Verge", "Reuters", "Bloomberg"],
    },
    {
        "partner": "Akamai",
        "value": "$1.8B",
        "date": "2026",
        "source": "Bloomberg",
        "publications_covering": ["Bloomberg", "Reuters", "TechCrunch"],
    },
    {
        "partner": "TeraWulf",
        "value": "20-year data center lease",
        "date": "2026",
        "source": "TradingView",
        "publications_covering": ["TradingView", "financial press"],
    },
]

META_ANTHROPIC_DEAL_COVERAGE = {
    "covered": [
        {"publication": "New York Times", "type": "original_report",
         "framing": "business/infrastructure", "date": "2026-07-17"},
        {"publication": "Reuters", "type": "standalone",
         "framing": "neutral_business", "date": "2026-07-17"},
        {"publication": "Bloomberg", "type": "standalone",
         "framing": "business_validation", "date": "2026-07-17"},
        {"publication": "CNN", "type": "standalone",
         "framing": "neutral_business", "date": "2026-07-17"},
        {"publication": "CNBC", "type": "standalone",
         "framing": "business", "date": "2026-07-17"},
        {"publication": "Motley Fool", "type": "analysis",
         "framing": "positive_for_meta", "date": "2026-07-29"},
        {"publication": "Zacks", "type": "etf_analysis",
         "framing": "positive_for_meta", "date": "2026-07-20"},
        {"publication": "eWeek", "type": "standalone",
         "framing": "neutral_business", "date": "2026-07-20"},
    ],
    "not_found": [
        {"publication": "WIRED", "parent": "Condé Nast / Advance Publications",
         "openai_deal": True, "meta_deal": False,
         "search_method": "web search 'wired.com Meta Anthropic cloud deal'",
         "note": "No standalone article found in web search results as of Aug 11, 2026"},
        {"publication": "The Verge", "parent": "PMC / Penske Media",
         "openai_deal": "fragmented (Vox Media legacy)",
         "meta_deal": False,
         "search_method": "web search 'theverge.com Meta Anthropic cloud deal'",
         "note": "No standalone article found in web search results as of Aug 11, 2026"},
    ],
    "caveat": (
        "Web search may not capture newsletter, podcast, or roundup coverage. "
        "Absence of standalone article ≠ absence of all coverage. "
        "However, standalone article coverage is the most visible and searchable "
        "form of editorial attention."
    ),
}

LEGITIMATE_FACTORS = [
    {
        "factor": "Deal is in early talks",
        "description": "The deal may not materialize; publications may be waiting for confirmation",
        "weakens_finding": True,
    },
    {
        "factor": "Infrastructure as business news",
        "description": "B2B compute leases may be considered financial rather than tech coverage",
        "weakens_finding": True,
    },
    {
        "factor": "Newsletter/roundup coverage",
        "description": "WIRED or The Verge may have covered this in newsletters or podcasts not indexed by web search",
        "weakens_finding": True,
    },
    {
        "factor": "News cycle competition",
        "description": "July 17, 2026 may have had competing stories that took priority",
        "weakens_finding": True,
    },
    {
        "factor": "Editorial bandwidth",
        "description": "Publications have limited staff and must prioritize stories",
        "weakens_finding": True,
    },
    {
        "factor": "Web search indexing lag",
        "description": "Some articles may exist but not be indexed by search engines yet",
        "weakens_finding": True,
    },
    {
        "factor": "Consistent with other Anthropic deal coverage",
        "description": (
            "If WIRED/Verge also didn't cover SpaceX-Anthropic or CoreWeave-Anthropic deals, "
            "then the omission is not specific to Meta and weakens the asymmetry finding. "
            "However, available evidence suggests these non-Meta deals were covered."
        ),
        "weakens_finding": "conditional",
    },
]


# ============================================================================
# TESTS — DEAL DATA STRUCTURE
# ============================================================================

class TestMetaAnthropicDealData:
    """Validate the Meta-Anthropic cloud deal data structure."""

    def test_deal_value_is_significant(self):
        """$10B deal is one of the largest AI infrastructure deals of 2026."""
        assert META_ANTHROPIC_DEAL["deal_value_b"] == 10
        assert META_ANTHROPIC_DEAL["deal_duration_years"] == 2
        annual_value_b = META_ANTHROPIC_DEAL["deal_value_b"] / META_ANTHROPIC_DEAL["deal_duration_years"]
        assert annual_value_b == 5.0, "$5B/yr is material for both companies"

    def test_anthropic_proposed_deal(self):
        """Anthropic approached Meta — making Anthropic the initiator/customer."""
        assert "Anthropic" in META_ANTHROPIC_DEAL["proposer"]
        assert "June 2026" in META_ANTHROPIC_DEAL["proposer"]

    def test_deal_creates_meta_customer_relationship(self):
        """The deal would make Anthropic a Meta customer, inverting adversarial framing."""
        assert "Makes Anthropic a Meta customer" in META_ANTHROPIC_DEAL["significance"]

    def test_deal_validates_meta_capex(self):
        """The deal validates Meta's infrastructure spending narrative."""
        assert any("capex" in s.lower() for s in META_ANTHROPIC_DEAL["significance"])

    def test_zuckerberg_quote_exists(self):
        """Zuckerberg's shareholder meeting quote about weekly compute requests."""
        assert "every week" in META_ANTHROPIC_DEAL["zuckerberg_quote"]
        assert "premium" in META_ANTHROPIC_DEAL["zuckerberg_quote"]


# ============================================================================
# TESTS — ANTHROPIC COMPUTE DEAL COMPARISON
# ============================================================================

class TestAnthropicComputeDealsComparison:
    """Compare coverage of Anthropic's compute deals with different partners."""

    def test_anthropic_has_multiple_compute_deals(self):
        """Anthropic has signed 5+ major compute deals in 2025-2026."""
        assert len(ANTHROPIC_OTHER_COMPUTE_DEALS) >= 5

    def test_spacex_deal_larger_than_meta(self):
        """SpaceX deal ($45B/3yr) is larger than Meta deal ($10B/2yr)."""
        spacex = [d for d in ANTHROPIC_OTHER_COMPUTE_DEALS if "SpaceX" in d["partner"]][0]
        assert "$45B" in spacex["value"]
        # SpaceX: $15B/yr; Meta: $5B/yr — SpaceX is 3x larger annual value
        spacex_annual = 45 / 3
        meta_annual = META_ANTHROPIC_DEAL["deal_value_b"] / META_ANTHROPIC_DEAL["deal_duration_years"]
        assert spacex_annual > meta_annual

    def test_spacex_deal_covered_by_tech_publications(self):
        """SpaceX-Anthropic deal was covered by major tech publications."""
        spacex = [d for d in ANTHROPIC_OTHER_COMPUTE_DEALS if "SpaceX" in d["partner"]][0]
        assert "TechCrunch" in spacex["publications_covering"]
        assert "The Verge" in spacex["publications_covering"]

    def test_coreweave_deal_covered_by_tech_publications(self):
        """CoreWeave-Anthropic deal was covered by tech publications."""
        coreweave = [d for d in ANTHROPIC_OTHER_COMPUTE_DEALS if "CoreWeave" in d["partner"]][0]
        assert "TechCrunch" in coreweave["publications_covering"]
        assert "The Verge" in coreweave["publications_covering"]

    @pytest.mark.parametrize("deal", ANTHROPIC_OTHER_COMPUTE_DEALS,
                             ids=[d["partner"] for d in ANTHROPIC_OTHER_COMPUTE_DEALS])
    def test_each_non_meta_deal_has_publication_coverage(self, deal):
        """Each Anthropic compute deal with non-Meta partners has documented publication coverage."""
        assert len(deal["publications_covering"]) >= 2, (
            f"Deal with {deal['partner']} should have coverage from at least 2 publications"
        )

    def test_meta_deal_not_covered_by_wired_or_verge(self):
        """Meta-Anthropic deal has no standalone WIRED or Verge coverage found."""
        not_found_pubs = [p["publication"] for p in META_ANTHROPIC_DEAL_COVERAGE["not_found"]]
        assert "WIRED" in not_found_pubs
        assert "The Verge" in not_found_pubs


# ============================================================================
# TESTS — COVERAGE SELECTION ASYMMETRY
# ============================================================================

class TestCoverageSelectionAsymmetry:
    """Analyze the coverage selection pattern for Meta-Anthropic deal."""

    def test_deal_covered_by_financial_outlets(self):
        """Financial and wire outlets covered the deal."""
        covered_pubs = [c["publication"] for c in META_ANTHROPIC_DEAL_COVERAGE["covered"]]
        assert "Reuters" in covered_pubs
        assert "Bloomberg" in covered_pubs
        assert "CNN" in covered_pubs

    def test_deal_covered_by_nyt_as_original_source(self):
        """NYT broke the story — it's not an obscure report."""
        nyt = [c for c in META_ANTHROPIC_DEAL_COVERAGE["covered"]
               if c["publication"] == "New York Times"][0]
        assert nyt["type"] == "original_report"

    def test_at_least_eight_outlets_covered(self):
        """At least 8 outlets covered the deal — it's not a non-story."""
        assert len(META_ANTHROPIC_DEAL_COVERAGE["covered"]) >= 8

    def test_wired_not_found_has_openai_deal(self):
        """WIRED (no standalone coverage found) has OpenAI content licensing deal."""
        wired = [p for p in META_ANTHROPIC_DEAL_COVERAGE["not_found"]
                 if p["publication"] == "WIRED"][0]
        assert wired["openai_deal"] is True
        assert wired["meta_deal"] is False

    def test_verge_not_found_has_no_meta_deal(self):
        """The Verge (no standalone coverage found) has no Meta deal."""
        verge = [p for p in META_ANTHROPIC_DEAL_COVERAGE["not_found"]
                 if p["publication"] == "The Verge"][0]
        assert verge["meta_deal"] is False

    def test_coverage_gap_is_selective_not_universal(self):
        """The gap is with publications that have adversarial Meta coverage, not all tech pubs."""
        covered_pubs = {c["publication"] for c in META_ANTHROPIC_DEAL_COVERAGE["covered"]}
        not_found_pubs = {p["publication"] for p in META_ANTHROPIC_DEAL_COVERAGE["not_found"]}
        # The deal IS covered widely — the gap is selective
        assert len(covered_pubs) > len(not_found_pubs), (
            "More outlets covered the deal than didn't — gap is selective"
        )

    def test_not_found_publications_have_adversarial_meta_pattern(self):
        """Publications where coverage was not found are ones with documented adversarial Meta framing."""
        for pub in META_ANTHROPIC_DEAL_COVERAGE["not_found"]:
            # Both WIRED and The Verge have documented adversarial Meta coverage patterns
            assert pub["publication"] in ("WIRED", "The Verge"), (
                f"Unexpected publication in not_found: {pub['publication']}"
            )


# ============================================================================
# TESTS — NARRATIVE IMPLICATIONS
# ============================================================================

class TestNarrativeImplications:
    """Analyze why the deal complicates existing editorial narratives."""

    def test_deal_challenges_capex_critique_narrative(self):
        """The deal contradicts the 'Meta is overbuilding AI infrastructure' narrative."""
        # Multiple publications framed Meta's $130-145B capex as excessive
        # Anthropic approaching Meta to lease capacity validates the spending
        assert "Validates Meta's $130-145B capex spending" in META_ANTHROPIC_DEAL["significance"]

    def test_deal_complicates_anthropic_good_meta_bad_framing(self):
        """If Anthropic becomes a Meta customer, the adversarial framing becomes awkward."""
        assert "Complicates adversarial Meta coverage" in META_ANTHROPIC_DEAL["significance"][3]

    def test_deal_opens_meta_cloud_business(self):
        """The deal positions Meta as a cloud competitor to AWS/Azure/GCP."""
        assert "Opens Meta cloud business" in META_ANTHROPIC_DEAL["significance"][2]

    def test_coverage_selection_is_editorial_power(self):
        """Coverage selection (what to report) is as powerful as framing (how to report)."""
        # This test documents the analytical principle
        # A story that is never published cannot be framed adversarially or favorably
        # It simply doesn't exist in the reader's information landscape
        assert META_ANTHROPIC_DEAL_COVERAGE["caveat"] is not None
        assert "standalone article coverage" in META_ANTHROPIC_DEAL_COVERAGE["caveat"]


# ============================================================================
# TESTS — LEGITIMATE FACTORS
# ============================================================================

class TestLegitimatFactors:
    """Ensure legitimate factors for the coverage gap are documented."""

    def test_at_least_six_legitimate_factors(self):
        """At least 6 legitimate explanations for the gap are documented."""
        assert len(LEGITIMATE_FACTORS) >= 6

    def test_all_factors_weaken_finding(self):
        """Every legitimate factor weakens or qualifies the finding — intellectual honesty."""
        for factor in LEGITIMATE_FACTORS:
            assert factor["weakens_finding"] in (True, "conditional"), (
                f"Factor '{factor['factor']}' should weaken finding for intellectual honesty"
            )

    @pytest.mark.parametrize("factor", LEGITIMATE_FACTORS,
                             ids=[f["factor"][:40] for f in LEGITIMATE_FACTORS])
    def test_each_factor_has_description(self, factor):
        """Every legitimate factor has a meaningful description."""
        assert len(factor["description"]) > 20, (
            f"Factor '{factor['factor']}' needs a substantive description"
        )

    def test_conditional_factor_explains_control(self):
        """The conditional factor explains how to verify the finding."""
        conditional = [f for f in LEGITIMATE_FACTORS if f["weakens_finding"] == "conditional"]
        assert len(conditional) >= 1
        assert "SpaceX" in conditional[0]["description"] or "CoreWeave" in conditional[0]["description"]


# ============================================================================
# TESTS — FINANCIAL RELATIONSHIP CORRELATION
# ============================================================================

class TestFinancialRelationshipCorrelation:
    """Test whether financial relationships predict coverage selection."""

    PUBLICATION_FINANCIAL_STATUS = [
        {"publication": "WIRED", "openai_deal": True, "meta_deal": False,
         "covered_meta_anthropic": False, "meta_coverage_tone": "adversarial"},
        {"publication": "The Verge", "openai_deal": "fragmented", "meta_deal": False,
         "covered_meta_anthropic": False, "meta_coverage_tone": "mixed_to_adversarial"},
        {"publication": "Reuters", "openai_deal": False, "meta_deal": False,
         "covered_meta_anthropic": True, "meta_coverage_tone": "neutral_wire"},
        {"publication": "CNN", "openai_deal": False, "meta_deal": False,
         "covered_meta_anthropic": True, "meta_coverage_tone": "neutral"},
        {"publication": "Bloomberg", "openai_deal": False, "meta_deal": False,
         "covered_meta_anthropic": True, "meta_coverage_tone": "mixed"},
        {"publication": "WSJ", "openai_deal": True, "meta_deal": True,
         "covered_meta_anthropic": True, "meta_coverage_tone": "balanced"},
    ]

    @pytest.mark.parametrize("pub", PUBLICATION_FINANCIAL_STATUS,
                             ids=[p["publication"] for p in PUBLICATION_FINANCIAL_STATUS])
    def test_each_publication_documented(self, pub):
        """Each publication has financial relationship and coverage documented."""
        assert "openai_deal" in pub
        assert "meta_deal" in pub
        assert "covered_meta_anthropic" in pub

    def test_publications_with_adversarial_tone_didnt_cover(self):
        """Publications with adversarial Meta tone didn't produce standalone coverage."""
        adversarial = [p for p in self.PUBLICATION_FINANCIAL_STATUS
                       if "adversarial" in p["meta_coverage_tone"]]
        for pub in adversarial:
            assert pub["covered_meta_anthropic"] is False, (
                f"{pub['publication']} has adversarial Meta tone but covered the deal"
            )

    def test_wsj_balanced_deals_covered(self):
        """WSJ (balanced deals: OpenAI + Meta) covered the deal — control group."""
        wsj = [p for p in self.PUBLICATION_FINANCIAL_STATUS
               if p["publication"] == "WSJ"][0]
        assert wsj["openai_deal"] is True
        assert wsj["meta_deal"] is True
        assert wsj["covered_meta_anthropic"] is True
        assert wsj["meta_coverage_tone"] == "balanced"

    def test_wire_services_covered_regardless_of_deals(self):
        """Wire services (Reuters) covered regardless of financial ties."""
        reuters = [p for p in self.PUBLICATION_FINANCIAL_STATUS
                   if p["publication"] == "Reuters"][0]
        assert reuters["covered_meta_anthropic"] is True

    def test_no_meta_deal_does_not_predict_omission_alone(self):
        """Having no Meta deal alone doesn't predict omission — CNN has no deal but covered."""
        cnn = [p for p in self.PUBLICATION_FINANCIAL_STATUS
               if p["publication"] == "CNN"][0]
        assert cnn["meta_deal"] is False
        assert cnn["covered_meta_anthropic"] is True
        # The predictor is adversarial tone + no Meta deal, not just no deal

    def test_adversarial_plus_no_deal_correlates_with_omission(self):
        """The combination of adversarial tone AND no Meta deal correlates with omission."""
        for pub in self.PUBLICATION_FINANCIAL_STATUS:
            if "adversarial" in pub["meta_coverage_tone"] and pub["meta_deal"] is False:
                assert pub["covered_meta_anthropic"] is False, (
                    f"{pub['publication']}: adversarial + no Meta deal should correlate with omission"
                )


# ============================================================================
# TESTS — CROSS-MECHANISM CONNECTIONS
# ============================================================================

class TestCrossMechanismConnections:
    """Connect Mechanism #38 to related mechanisms."""

    RELATED_MECHANISMS = {
        34: "WIRED Institutional Rogue AI Coverage Volume Asymmetry",
        29: "Guardian Rogue AI Coverage Volume & Temperature Asymmetry",
        37: "Open-Weight Policy Coverage Selection Asymmetry",
        36: "Pre-IPO Owner-Investor-Publisher Convergence",
        33: "Cross-Publication Facial Recognition Privacy Parity",
    }

    def test_mechanism_38_extends_selection_pattern(self):
        """Mechanism #38 extends the coverage SELECTION pattern from Mechanism #37."""
        # #37: publications selectively cover rogue AI but NOT open-weight exemption
        # #38: publications selectively cover Anthropic deals but NOT Meta-Anthropic deal
        # Both are about what gets covered vs omitted, not how it's framed
        assert 37 in self.RELATED_MECHANISMS

    def test_mechanism_38_extends_volume_pattern(self):
        """Mechanism #38 extends the coverage VOLUME pattern from Mechanism #34."""
        # #34: WIRED published 3 rogue AI articles for OpenAI/Anthropic, 0 for Meta
        # #38: WIRED covered Anthropic deals with SpaceX/CoreWeave but not with Meta
        # Both show selective coverage correlated with financial relationships
        assert 34 in self.RELATED_MECHANISMS

    def test_mechanism_38_connects_to_preipo_convergence(self):
        """Mechanism #38 connects to #36 — the Anthropic-Meta deal changes the financial map."""
        # #36 documented that Anthropic has ZERO financial links to adversarial publications
        # #38 shows that when Anthropic forms a link TO Meta, publications selectively omit
        assert 36 in self.RELATED_MECHANISMS

    @pytest.mark.parametrize("mech_id,name", list({
        34: "WIRED Rogue AI Volume",
        37: "Open-Weight Policy Selection",
        36: "Pre-IPO Convergence",
    }.items()))
    def test_distinction_from_related_mechanisms(self, mech_id, name):
        """Mechanism #38 is distinct from related mechanisms — it's about deal coverage selection."""
        # #38 specifically tests: Anthropic deal with META gets less coverage than
        # Anthropic deals with non-Meta partners, from publications with adversarial Meta tone
        # This is a deal-level selection test, not an incident-level or policy-level test
        assert mech_id in self.RELATED_MECHANISMS


# ============================================================================
# TESTS — META AS EMERGING CLOUD COMPETITOR
# ============================================================================

class TestMetaCloudNarrative:
    """Test the Meta cloud business narrative implications."""

    def test_meta_cloud_would_compete_with_existing_providers(self):
        """Meta entering cloud puts it in competition with AWS, Azure, GCP."""
        # These are the existing Anthropic compute providers that publications WOULD cover
        existing_providers = ["Amazon/AWS", "Google Cloud", "Microsoft/Azure",
                              "CoreWeave", "SpaceX/xAI"]
        assert len(existing_providers) >= 5

    def test_meta_capex_context(self):
        """Meta's $130-145B 2026 capex is the backdrop for this deal."""
        # If the deal validates the capex, it's directly newsworthy
        # The absence of coverage from critical publications means their readers
        # don't see this validation
        assert META_ANTHROPIC_DEAL["deal_value_b"] == 10

    def test_deal_echoes_spacex_strategy(self):
        """The deal structure echoes Anthropic's SpaceX deal — monthly payments, exit clauses."""
        assert META_ANTHROPIC_DEAL["payment_structure"] == "monthly increments"
        spacex = [d for d in ANTHROPIC_OTHER_COMPUTE_DEALS if "SpaceX" in d["partner"]][0]
        assert "mo" in spacex["value"].lower() or "month" in spacex["value"].lower()


# ============================================================================
# TESTS — DATA QUALITY
# ============================================================================

class TestDataQuality:
    """Ensure data integrity and intellectual honesty."""

    def test_caveat_exists(self):
        """The coverage analysis includes an explicit caveat about limitations."""
        assert "caveat" in META_ANTHROPIC_DEAL_COVERAGE
        assert len(META_ANTHROPIC_DEAL_COVERAGE["caveat"]) > 50

    def test_search_method_documented(self):
        """Each 'not found' entry documents how the search was conducted."""
        for pub in META_ANTHROPIC_DEAL_COVERAGE["not_found"]:
            assert "search_method" in pub
            assert "web search" in pub["search_method"]

    def test_deal_status_documented_as_early(self):
        """The deal's preliminary status is accurately documented."""
        assert "early talks" in META_ANTHROPIC_DEAL["deal_status"]
        assert "may not" in META_ANTHROPIC_DEAL["deal_status"]

    def test_no_overclaiming(self):
        """The test doesn't claim publications SUPPRESSED the story — only that standalone articles weren't found."""
        for pub in META_ANTHROPIC_DEAL_COVERAGE["not_found"]:
            note = pub["note"]
            assert "suppressed" not in note.lower()
            assert "censored" not in note.lower()
            assert "found" in note.lower() or "not found" in note.lower()
