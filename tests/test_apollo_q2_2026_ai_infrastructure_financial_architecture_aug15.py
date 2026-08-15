"""
Mechanism #111: Apollo Global Management Q2 2026 — AI Infrastructure Financial
Architecture at Private Equity Scale

Type C: Financial Incentive Mapping (Aug 15, 2026 02:00 PT — Iteration #113)

KEY FINDING: Apollo's Q2 2026 earnings (Aug 4, 2026) reveal the financial architecture
connecting Yahoo publications (TechCrunch, Engadget) to AI competitor success has
EXPANDED significantly beyond the $38.4B previously documented:

- AUM crossed $1 TRILLION for the first time (Q1 2026)
- Record Capital Solutions Fees: $277M (5th consecutive quarter >$200M) — the
  specific revenue line where AI infrastructure deals generate fee income
- $74B originations in Q2 ALONE, EXCLUDING the $35B Broadcom AI XPV deal
  (recognized at close, not announcement, feeding future quarters)
- $50B+ in signed/announced deals to be recognized in future quarters
- Total AI infrastructure: $40B+ (Apollo's own Jan 2026 disclosure) since 2022
- NEW dedicated AI chip-focused partner: Reed Rayman (announced Aug 5, 2026)
- 60+ person digital infrastructure team
- Stream Data Centers majority stake (hyperscale developer)
- STACK Infrastructure European colocation carve-out

APOLLO'S AI COMPETITOR FINANCIAL EXPOSURE:
1. Anthropic: $35B XPV Platform lead investor (Jun 9, 2026) — Apollo-led capital
   solution finances Broadcom XPU compute infrastructure for Anthropic's capacity
   expansion at Fluidstack sites. Apollo generates fees on origination, structuring,
   and ongoing management. Broadcom supplies the XPUs and networking.
2. xAI: $3.5B of $5.4B Valor Compute Infrastructure (Jan 7, 2026) — triple net
   lease for Nvidia GB200 GPUs to power Grok training.
3. OpenAI: Named as FUTURE CUSTOMER of XPV Platform (20GW capacity through 2028)

NOTE: Google is NOT a hardware supplier in the XPV deal. The hardware is Broadcom XPUs.
Google's connection to Apollo/Yahoo is through the Yahoo Search Alliance and Google
ad tech dependency, documented separately.

TOTAL DOCUMENTED: $38.5B direct + $40B+ broader digital infrastructure since 2022
REVENUE IMPACT: Capital Solutions Fees hit record $277M in Q2 2026 — AI infrastructure
   is a growing share of Apollo's most profitable business line

YAHOO OWNERSHIP CHAIN:
- Apollo acquired Yahoo (then Verizon Media) in Sep 2021 for ~$5B
- Yahoo publishes TechCrunch and Engadget
- Yahoo CEO Jim Lanzone is vocally anti-AI-scraping (confounding factor)
- Yahoo Search powered by Google (renewed Search Alliance)
- Yahoo display ads depend on Google ad tech stack

FINANCIAL INCENTIVE CHAIN STRENGTHENING:
The Q2 2026 earnings data shows Apollo's AI infrastructure business is:
(a) LARGER than previously documented ($40B+ vs $38.4B)
(b) GROWING (record Capital Solutions Fees, new dedicated leadership)
(c) CENTRAL to Apollo's strategy (CEO Rowan: "momentum across the business")
(d) EXPANDING (XPV targets 20GW through 2028, OpenAI as future customer)

This strengthens the financial incentive analysis in mechanisms #104 (TechCrunch
privacy indictment) and #109 (Engadget Google privacy vocabulary zero-out):
Apollo's DIRECT financial interest in Anthropic, xAI, OpenAI, and Google succeeding
is not a one-time deal — it's Apollo's core growth strategy generating recurring
fee revenue.

CONFOUNDING FACTORS:
1. STRONG: Yahoo editorial operates independently from Apollo investment decisions;
   no evidence of direct editorial interference from Apollo
2. STRONG: Apollo is a diversified firm; AI infrastructure is one of many business lines
3. MODERATE: Yahoo CEO Jim Lanzone has publicly opposed AI content scraping, suggesting
   editorial-investment alignment may be limited
4. MODERATE: Capital Solutions Fee revenue is not broken out by AI vs non-AI
5. WEAK: Other private equity firms (Blackstone, KKR) also finance AI infrastructure
   without owning publications

META COMPARISON:
- Meta struck a $27B financing deal with Blue Owl Capital (Oct 2025) for data centers
- Blue Owl does NOT own any publications
- Apollo's unique position: ONLY private equity firm financing AI competitors that ALSO
  owns major tech publications covering those competitors

Sources:
  - Q2 2026 earnings: https://finance.biggo.com/news/US_APO_2026-08-04
  - Q2 details: https://www.gurufocus.com/news/9002954/apollo-global-management-inc-apo-q2-2026-earnings-call-highlights-record-fre-and-sre-drive-strong-quarter
  - AI deal leadership: https://www.pymnts.com/news/artificial-intelligence/2026/apollo-global-management-targets-more-ai-infrastructure-deals/
  - XPV Platform: https://www.globenewswire.com/news-release/2026/06/09/3308896/0/en/Apollo-Leads-35-Billion-Capital-Solution-for-Broadcom-AI-XPV-Platform-in-Partnership-with-Blackstone-and-Leading-Global-Banks.html
  - xAI deal: https://www.globenewswire.com/news-release/2026/01/07/3214463/0/en/Apollo-Backs-5-4-Billion-Valor-and-xAI-Data-Center-Compute-Infrastructure-Transaction-with-3-5-Billion-Capital-Solution.html
  - $40B+ digital infra: https://www.alternativeswatch.com/2026/01/07/apollo-leads-3-5bn-financing-for-xai-data-center-buildout/
  - Reuters XPV: https://www.reuters.com/business/apollo-blackstone-back-anthropics-35-billion-capacity-expansion-new-broadcom-tie-2026-06-09/
  - Record credit deal: https://www.tradingview.com/news/gurufocus:30620898d094b:0-apollo-lands-record-35-billion-ai-credit-deal-challenging-wall-street-banks/
"""

import yaml
import os
import pytest

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)

ENTITIES_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml'
)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities_data():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def mechanism_111(research_data):
    cpf = research_data.get('cross_publication_findings', {})
    section = cpf.get('apollo_q2_2026_ai_infrastructure_financial_architecture')
    assert section is not None, (
        "Missing apollo_q2_2026_ai_infrastructure_financial_architecture in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


@pytest.fixture(scope='module')
def yahoo_apollo_entity(entities_data):
    entity = entities_data.get('entities', {}).get('yahoo_apollo', {})
    assert entity, "Missing yahoo_apollo entity in competitor-entities.yaml"
    return entity


# ── Class 1: Mechanism Metadata ─────────────────────────────────────


class TestMechanismMetadata:
    """Verify mechanism #111 metadata is correctly documented."""

    def test_mechanism_id(self, mechanism_111):
        assert mechanism_111.get('mechanism_id') == 111

    def test_date_added(self, mechanism_111):
        assert mechanism_111.get('date_added') == '2026-08-15'

    def test_finding_type(self, mechanism_111):
        ft = mechanism_111.get('finding_type', '')
        assert 'financial' in ft.lower() or 'incentive' in ft.lower()

    def test_domain(self, mechanism_111):
        assert mechanism_111.get('domain') is not None

    def test_has_source_urls(self, mechanism_111):
        urls = mechanism_111.get('source_urls', [])
        assert len(urls) >= 4, f"Expected >=4 source URLs, got {len(urls)}"

    def test_has_test_file(self, mechanism_111):
        tf = mechanism_111.get('test_file', '')
        assert 'apollo_q2_2026' in tf


# ── Class 2: Q2 2026 Earnings Data ──────────────────────────────────


class TestQ2_2026_Earnings:
    """Verify Apollo Q2 2026 earnings data is documented."""

    def test_q2_earnings_section_exists(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings')
        assert q2 is not None, "Missing q2_2026_earnings section"

    def test_earnings_date(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        assert q2.get('report_date') == '2026-08-04'

    def test_fee_related_earnings_record(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        fre = q2.get('fee_related_earnings_m')
        assert fre == 785, f"FRE should be $785M, got {fre}"

    def test_fre_yoy_growth(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        growth = q2.get('fre_yoy_growth_pct')
        assert growth == 25, f"FRE YoY growth should be 25%, got {growth}"

    def test_spread_related_earnings_record(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        sre = q2.get('spread_related_earnings_m')
        assert sre == 877, f"SRE should be $877M, got {sre}"

    def test_adjusted_net_income(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        ani = q2.get('adjusted_net_income_b')
        assert ani == 1.3, f"Adjusted net income should be $1.3B, got {ani}"

    def test_capital_solutions_fees_record(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        csf = q2.get('capital_solutions_fees_m')
        assert csf == 277, f"Capital Solutions Fees should be $277M, got {csf}"

    def test_capital_solutions_consecutive_quarters(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        cq = q2.get('csf_consecutive_quarters_above_200m')
        assert cq == 5

    def test_originations_excluding_xpv(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        orig = q2.get('originations_b')
        assert orig == 74

    def test_xpv_excluded_from_originations(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        note = q2.get('originations_note', '')
        assert 'exclud' in note.lower() or 'xpv' in note.lower()

    def test_aum_above_1_trillion(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        aum = q2.get('aum_exceeded_1t')
        assert aum is True

    def test_organic_inflows_record(self, mechanism_111):
        q2 = mechanism_111.get('q2_2026_earnings', {})
        inflows = q2.get('organic_inflows_b')
        assert inflows == 60


# ── Class 3: AI Infrastructure Deal Portfolio ────────────────────────


class TestAIInfrastructureDealPortfolio:
    """Verify the complete Apollo AI infrastructure deal portfolio."""

    def test_deals_section_exists(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals')
        assert deals is not None

    def test_anthropic_xpv_deal(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform')
        assert xpv is not None
        assert xpv.get('amount_b') == 35

    def test_xpv_announcement_date(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform', {})
        assert xpv.get('date') == '2026-06-09'

    def test_xpv_role(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform', {})
        role = xpv.get('apollo_role', '')
        assert 'lead' in role.lower()

    def test_xpv_broadcom_hardware(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform', {})
        hw = xpv.get('hardware', '')
        assert 'broadcom' in hw.lower() or 'xpu' in hw.lower()

    def test_xpv_future_customers_include_openai(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform', {})
        future = xpv.get('future_customers', [])
        assert 'OpenAI' in future

    def test_xpv_capacity_target(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xpv = deals.get('anthropic_xpv_platform', {})
        assert xpv.get('platform_target_gw') == 20

    def test_xai_deal(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xai = deals.get('xai_valor_compute')
        assert xai is not None
        assert xai.get('apollo_amount_b') == 3.5

    def test_xai_deal_total(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xai = deals.get('xai_valor_compute', {})
        assert xai.get('total_deal_b') == 5.4

    def test_xai_hardware(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        xai = deals.get('xai_valor_compute', {})
        hw = xai.get('hardware', '')
        assert 'nvidia' in hw.lower() or 'gb200' in hw.lower()

    def test_total_documented_ai_b(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        total = deals.get('total_documented_ai_b')
        assert total >= 38.4, f"Total documented AI should be >= $38.4B, got {total}"

    def test_broader_digital_infra_total(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        broader = deals.get('broader_digital_infrastructure_since_2022_b')
        assert broader >= 40, f"Broader digital infra should be >= $40B, got {broader}"

    def test_stream_data_centers(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        assert deals.get('stream_data_centers_majority_stake') is True

    def test_stack_infrastructure(self, mechanism_111):
        deals = mechanism_111.get('ai_infrastructure_deals', {})
        assert deals.get('stack_infrastructure_european_carveout') is True


# ── Class 4: AI Deal Leadership Expansion ────────────────────────────


class TestAIDealLeadershipExpansion:
    """Verify the organizational expansion of Apollo's AI deal capability."""

    def test_organizational_section_exists(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion')
        assert org is not None

    def test_new_chip_leader(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion', {})
        leader = org.get('new_ai_chip_leader')
        assert leader is not None
        assert leader.get('name') == 'Reed Rayman'

    def test_chip_leader_title(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion', {})
        leader = org.get('new_ai_chip_leader', {})
        assert 'partner' in leader.get('title', '').lower()

    def test_chip_leader_announcement_date(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion', {})
        leader = org.get('new_ai_chip_leader', {})
        assert leader.get('date') == '2026-08-05'

    def test_digital_infra_team_size(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion', {})
        team_size = org.get('digital_infrastructure_team_size')
        assert team_size >= 60

    def test_focus_area(self, mechanism_111):
        org = mechanism_111.get('organizational_expansion', {})
        focus = org.get('rayman_focus', '')
        assert 'chip' in focus.lower() or 'semiconductor' in focus.lower()


# ── Class 5: Yahoo Ownership and Media Properties ────────────────────


class TestYahooOwnershipChain:
    """Verify the ownership chain and media property documentation."""

    def test_ownership_chain(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        assert chain.get('ultimate_owner') is not None
        assert 'Apollo' in chain.get('ultimate_owner', '')

    def test_yahoo_publications(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        pubs = chain.get('publications', [])
        assert 'TechCrunch' in pubs
        assert 'Engadget' in pubs

    def test_yahoo_acquisition_price(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        price = chain.get('acquisition_price_b')
        assert price == 5.0

    def test_yahoo_acquisition_date(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        assert '2021' in chain.get('acquisition_date', '')

    def test_google_search_alliance(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        assert chain.get('google_search_alliance') is True

    def test_meta_financial_relationship(self, mechanism_111):
        chain = mechanism_111.get('ownership_chain', {})
        meta = chain.get('meta_financial_relationship', '')
        assert 'none' in meta.lower() or '$0' in meta


# ── Class 6: Financial Incentive Architecture ────────────────────────


class TestFinancialIncentiveArchitecture:
    """Verify the financial incentive chain analysis."""

    def test_incentive_section_exists(self, mechanism_111):
        incentive = mechanism_111.get('financial_incentive_analysis')
        assert incentive is not None

    def test_entities_apollo_profits_from(self, mechanism_111):
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        entities = incentive.get('entities_with_financial_alignment', [])
        assert 'Anthropic' in entities
        assert 'xAI' in entities
        assert 'OpenAI' in entities

    def test_meta_not_in_aligned_entities(self, mechanism_111):
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        entities = incentive.get('entities_with_financial_alignment', [])
        assert 'Meta' not in entities

    def test_revenue_mechanism(self, mechanism_111):
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        mechanism = incentive.get('revenue_mechanism', '')
        assert 'capital solutions' in mechanism.lower() or 'fee' in mechanism.lower()

    def test_unique_position(self, mechanism_111):
        """Apollo is the ONLY PE firm financing AI competitors AND owning publications."""
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        unique = incentive.get('unique_position', '')
        assert 'only' in unique.lower() or 'unique' in unique.lower()

    def test_meta_comparison(self, mechanism_111):
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        meta_comp = incentive.get('meta_blue_owl_comparison', '')
        assert 'blue owl' in meta_comp.lower() or 'publication' in meta_comp.lower()

    def test_scaling_analysis(self, mechanism_111):
        """Q2 2026 shows this is EXPANDING, not static."""
        incentive = mechanism_111.get('financial_incentive_analysis', {})
        scaling = incentive.get('scaling_evidence', [])
        assert len(scaling) >= 3, f"Expected >=3 scaling evidence points, got {len(scaling)}"


# ── Class 7: Confounding Factors ─────────────────────────────────────


class TestConfoundingFactors:
    """Verify confounding factors are documented."""

    def test_confounding_factors_exist(self, mechanism_111):
        factors = mechanism_111.get('confounding_factors', [])
        assert len(factors) >= 4, f"Expected >=4 confounding factors, got {len(factors)}"

    def test_editorial_independence_factor(self, mechanism_111):
        factors = mechanism_111.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_editorial = any('editorial' in t.lower() and 'independen' in t.lower() for t in texts)
        assert has_editorial, "Must document editorial independence as confounding factor"

    def test_strong_factor_exists(self, mechanism_111):
        factors = mechanism_111.get('confounding_factors', [])
        strengths = [f.get('strength', '') for f in factors]
        assert 'STRONG' in strengths or 'strong' in [s.lower() for s in strengths]

    def test_lanzone_opposition_factor(self, mechanism_111):
        factors = mechanism_111.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_lanzone = any('lanzone' in t.lower() for t in texts)
        assert has_lanzone, "Must document Yahoo CEO Lanzone's anti-AI-scraping stance"

    def test_diversification_factor(self, mechanism_111):
        factors = mechanism_111.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_diversified = any('diversif' in t.lower() for t in texts)
        assert has_diversified, "Must document Apollo's diversified business as confounding factor"


# ── Class 8: Testable Predictions ────────────────────────────────────


class TestTestablePredictions:
    """Verify testable predictions based on the financial architecture."""

    def test_predictions_exist(self, mechanism_111):
        preds = mechanism_111.get('testable_predictions', [])
        assert len(preds) >= 3

    def test_predictions_are_falsifiable(self, mechanism_111):
        preds = mechanism_111.get('testable_predictions', [])
        for pred in preds:
            text = pred if isinstance(pred, str) else str(pred)
            assert len(text) > 20, f"Prediction too short to be falsifiable: {text}"


# ── Class 9: Cross-References ────────────────────────────────────────


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_exist(self, mechanism_111):
        xrefs = mechanism_111.get('cross_references', [])
        assert len(xrefs) >= 2

    def test_references_mechanism_104(self, mechanism_111):
        xrefs = mechanism_111.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 104 in ids, "Must reference mechanism #104 (TechCrunch privacy indictment)"

    def test_references_mechanism_109(self, mechanism_111):
        xrefs = mechanism_111.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 109 in ids, "Must reference mechanism #109 (Engadget Google privacy zero-out)"


# ── Class 10: Entity Profile Update ─────────────────────────────────


class TestEntityProfileUpdate:
    """Verify the yahoo_apollo entity in competitor-entities.yaml is updated."""

    def test_q2_2026_section_exists(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update')
        assert q2 is not None, "Missing q2_2026_financial_update in yahoo_apollo entity"

    def test_entity_aum(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update', {})
        aum = q2.get('aum_exceeded_1t')
        assert aum is True

    def test_entity_capital_solutions_fees(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update', {})
        csf = q2.get('capital_solutions_fees_m')
        assert csf == 277

    def test_entity_ai_infra_total_updated(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update', {})
        total = q2.get('total_digital_infrastructure_since_2022_b')
        assert total >= 40

    def test_entity_team_size(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update', {})
        team = q2.get('digital_infrastructure_team_size')
        assert team >= 60

    def test_entity_chip_leader(self, yahoo_apollo_entity):
        q2 = yahoo_apollo_entity.get('q2_2026_financial_update', {})
        leader = q2.get('ai_chip_leader')
        assert leader is not None
        assert 'rayman' in leader.lower() or 'Rayman' in leader
