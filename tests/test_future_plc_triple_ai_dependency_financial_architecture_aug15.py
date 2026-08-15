"""
Mechanism #114: Future plc Triple-Layer AI Competitor Financial Dependency Architecture

Type C: Financial Incentive Mapping (Aug 15, 2026 06:00 PT — Iteration #117)

KEY FINDING: Future plc (LSE: FUTR, owner of Tom's Guide, TechRadar, Tom's Hardware,
PC Gamer, Marie Claire, ~170 brands) has THREE simultaneous financial dependencies on
Meta's competitors, creating a compound incentive structure that mechanism #110
(editor-in-chief-level framing asymmetry) previously documented the EFFECT of, but
not the full CAUSE.

LAYER 1: GOOGLE TRAFFIC REVENUE DEPENDENCY (existential)
- H1 2026 (six months to Mar 31 2026): Revenue £349.1M (down 8%), PBT £18.4M (down 67%)
- 60%+ of group revenue from Google-dependent brands (CEO Kevin Li Ying's own segmentation)
- "Brands in transition" (45% of revenue, -5% YoY) + "Non-diversified brands" (15%, -18% YoY)
  = 60% Google-dependent
- Only 9% of revenue from "destination brands" (not Google-dependent)
- Google Search AND Google Discover audiences both down ~20% YoY
- Programmatic advertising (80-90% margin): UK down 19%, US down 16%
- eCommerce affiliates down 24%
- Market cap: ~£280M (crashed from ~£4B in Dec 2022)

LAYER 2: OPENAI CONTENT LICENSING DEAL (strategic partnership)
- Signed December 5, 2024
- All 200+ Future brands licensed to ChatGPT with attribution and links
- OpenAI-based chatbots deployed on Tom's Hardware and Who What Wear
- Future using OpenAI tools for sales, marketing, and editorial productivity
- CEO Jon Steinberg: "ChatGPT provides a whole new avenue for people to discover
  our incredible specialist content"
- One of OpenAI's 20+ publisher content deals

LAYER 3: FUTURE OPTIC — AI VISIBILITY ADVERTISING PRODUCT (commercial investment)
- Future Optic sells brands the ability to appear prominently in LLMs: ChatGPT AND Gemini
- £2M booked at H1 2026, £10M full-year pipeline
- H2 expected to generate more than double H1 sales
- External AI visibility recognition from SimilarWeb, Peec, Ahrefs, Promptwatch
- Future plc is COMMERCIALLY INVESTED in both Google Gemini and OpenAI ChatGPT succeeding
- If negative coverage reduced those platforms' usage, Future Optic's product value decreases

META FINANCIAL RELATIONSHIP: $0
- No content licensing deal
- No advertising dependency
- No commercial products dependent on Meta platform success
- Meta IS a direct ad competitor to Google (reducing Google ad share hurts Future's
  programmatic revenue)

THE COMPOUND STRUCTURE:
1. Google dependency → can't afford negative Google coverage (existential threat)
2. OpenAI content deal → can't afford negative OpenAI coverage (strategic partnership)
3. Future Optic → commercially invested in BOTH Google and OpenAI platforms succeeding
4. Meta has $0 relationship AND competes with Google for ad spend → Meta coverage
   carries zero financial risk AND attacking Meta doesn't threaten any dependency

This EXPLAINS mechanism #110's finding: Tom's Guide editors use combative language
positioning Google as hero ("blow away," "get smoked," "defeat") against Meta as
villain, while hedging every Meta positive with "but" qualifiers. The financial
architecture makes this editorial behavior structurally rational.

CONFOUNDING FACTORS:
1. STRONG: Future plc editorial operates independently from business partnerships;
   no evidence of direct editorial interference from OpenAI or Google
2. STRONG: Google traffic decline hurts Future — they could resent Google, not protect it
3. MODERATE: Meta's genuine privacy controversies may justify harsher coverage
4. MODERATE: CEO Kevin Li Ying's strategy pivot away from Google could reduce dependency
5. WEAK: Tom's Guide editors may genuinely believe Google products are superior
6. WEAK: Industry-wide Meta-skeptical framing could explain differential coverage

Sources:
  - H1 2026 results: https://ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/
  - Reuters H1 2026: https://www.reuters.com/business/uk-publisher-futures-shares-plummet-changes-google-search-traffic-hit-margins-2026-03-31/
  - TradingPedia: https://www.tradingpedia.com/2026/03/31/future-plc-cuts-2026-outlook-amid-google-traffic-shift/
  - ADVFN results: https://uk.advfn.com/stock-market/london/future-FUTR/share-news/Future-PLC-2026-Half-Year-Results/98522253
  - OpenAI deal (Digiday): https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/
  - OpenAI deal (Neowin): http://www.neowin.net/news/openai-partners-with-future-on-specialist-content/
  - OpenAI deal (Technology Magazine): https://technologymag.org/openai-strikes-content-deal-with-toms-guide-owner-future/
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
def mechanism_114(research_data):
    cpf = research_data.get('cross_publication_findings', {})
    section = cpf.get('future_plc_triple_ai_dependency_financial_architecture')
    assert section is not None, (
        "Missing future_plc_triple_ai_dependency_financial_architecture in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


@pytest.fixture(scope='module')
def future_plc_entity(entities_data):
    # future_plc is nested under essilorluxottica in competitor-entities.yaml
    entity = entities_data.get('essilorluxottica', {}).get('future_plc', {})
    assert entity, "Missing future_plc under essilorluxottica in competitor-entities.yaml"
    return entity


# ── Class 1: Mechanism Metadata ─────────────────────────────────────


class TestMechanismMetadata:
    """Verify mechanism #114 metadata is correctly documented."""

    def test_mechanism_id(self, mechanism_114):
        assert mechanism_114.get('mechanism_id') == 114

    def test_date_added(self, mechanism_114):
        assert mechanism_114.get('date_added') == '2026-08-15'

    def test_finding_type(self, mechanism_114):
        ft = mechanism_114.get('finding_type', '')
        assert 'financial' in ft.lower() or 'compound' in ft.lower()

    def test_domain(self, mechanism_114):
        domain = mechanism_114.get('domain', '')
        assert domain is not None and len(domain) > 0

    def test_has_source_urls(self, mechanism_114):
        urls = mechanism_114.get('source_urls', [])
        assert len(urls) >= 6, f"Expected >=6 source URLs, got {len(urls)}"

    def test_has_test_file(self, mechanism_114):
        tf = mechanism_114.get('test_file', '')
        assert 'future_plc_triple_ai_dependency' in tf

    def test_publication_owner(self, mechanism_114):
        owner = mechanism_114.get('publication_owner', '')
        assert 'Future plc' in owner or 'future' in owner.lower()

    def test_iteration(self, mechanism_114):
        it = mechanism_114.get('iteration')
        assert it == 117


# ── Class 2: Layer 1 — Google Traffic Revenue Dependency ─────────────


class TestGoogleTrafficDependency:
    """Verify Layer 1: Google traffic revenue dependency financials (H1 2026)."""

    def test_layer1_section_exists(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency')
        assert layer1 is not None, "Missing layer_1_google_traffic_dependency section"

    def test_h1_2026_revenue_m(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        revenue = layer1.get('h1_2026_revenue_gbp_m')
        assert revenue == 349.1, f"H1 2026 revenue should be £349.1M, got {revenue}"

    def test_h1_2026_revenue_yoy_change(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        change = layer1.get('revenue_yoy_change_pct')
        assert change == -8, f"Revenue YoY change should be -8%, got {change}"

    def test_h1_2026_pbt_m(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        pbt = layer1.get('h1_2026_pbt_gbp_m')
        assert pbt == 18.4, f"H1 2026 PBT should be £18.4M, got {pbt}"

    def test_h1_2026_pbt_yoy_change(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        change = layer1.get('pbt_yoy_change_pct')
        assert change == -67, f"PBT YoY change should be -67%, got {change}"

    def test_google_dependent_revenue_share(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        share = layer1.get('google_dependent_revenue_share')
        assert share == 0.60, f"Google-dependent share should be 0.60, got {share}"

    def test_brands_in_transition_share(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        seg = layer1.get('segmentation', {})
        bit = seg.get('brands_in_transition_pct')
        assert bit == 45

    def test_non_diversified_brands_share(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        seg = layer1.get('segmentation', {})
        ndb = seg.get('non_diversified_brands_pct')
        assert ndb == 15

    def test_non_diversified_brands_yoy(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        seg = layer1.get('segmentation', {})
        yoy = seg.get('non_diversified_brands_yoy_pct')
        assert yoy == -18

    def test_destination_brands_share(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        seg = layer1.get('segmentation', {})
        db = seg.get('destination_brands_pct')
        assert db == 9

    def test_google_search_audience_decline(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        decline = layer1.get('google_search_audience_yoy_decline_pct')
        assert decline == -20

    def test_programmatic_uk_decline(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        prog = layer1.get('programmatic_uk_yoy_pct')
        assert prog == -19

    def test_programmatic_us_decline(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        prog = layer1.get('programmatic_us_yoy_pct')
        assert prog == -16

    def test_ecommerce_affiliates_decline(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        ecom = layer1.get('ecommerce_affiliates_yoy_pct')
        assert ecom == -24

    def test_market_cap_crash(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        mc = layer1.get('market_cap_gbp_m')
        assert mc == 280

    def test_market_cap_peak(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        peak = layer1.get('market_cap_peak_gbp_b')
        assert peak == 4.0

    def test_dependency_classified_existential(self, mechanism_114):
        layer1 = mechanism_114.get('layer_1_google_traffic_dependency', {})
        severity = layer1.get('dependency_severity', '')
        assert 'existential' in severity.lower()


# ── Class 3: Layer 2 — OpenAI Content Licensing Deal ─────────────────


class TestOpenAIContentDeal:
    """Verify Layer 2: OpenAI content licensing deal structure."""

    def test_layer2_section_exists(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal')
        assert layer2 is not None, "Missing layer_2_openai_content_deal section"

    def test_deal_date(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        assert layer2.get('signed_date') == '2024-12-05'

    def test_brands_licensed(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        count = layer2.get('brands_licensed_count')
        assert count >= 200, f"Expected >=200 brands licensed, got {count}"

    def test_chatgpt_integration(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        assert layer2.get('chatgpt_content_licensing') is True

    def test_openai_chatbots_deployed(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        bots = layer2.get('openai_chatbots_deployed_on', [])
        assert "Tom's Hardware" in bots
        assert "Who What Wear" in bots

    def test_openai_tools_editorial(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        assert layer2.get('openai_tools_for_editorial') is True

    def test_ceo_quote(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        quote = layer2.get('ceo_endorsement_quote', '')
        assert 'ChatGPT' in quote or 'discover' in quote.lower()

    def test_deal_type(self, mechanism_114):
        layer2 = mechanism_114.get('layer_2_openai_content_deal', {})
        dtype = layer2.get('deal_type', '')
        assert 'strategic' in dtype.lower() or 'content' in dtype.lower()


# ── Class 4: Layer 3 — Future Optic AI Visibility Product ────────────


class TestFutureOpticAIVisibility:
    """Verify Layer 3: Future Optic commercial AI investment product."""

    def test_layer3_section_exists(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic')
        assert layer3 is not None, "Missing layer_3_future_optic section"

    def test_product_description(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        desc = layer3.get('product_description', '')
        assert 'llm' in desc.lower() or 'ai visibility' in desc.lower()

    def test_h1_revenue_booked(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        booked = layer3.get('h1_2026_revenue_booked_gbp_m')
        assert booked == 2

    def test_full_year_pipeline(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        pipeline = layer3.get('full_year_pipeline_gbp_m')
        assert pipeline == 10

    def test_platforms_served(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        platforms = layer3.get('platforms', [])
        assert 'ChatGPT' in platforms
        assert 'Gemini' in platforms

    def test_h2_growth_expectation(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        h2 = layer3.get('h2_expected_sales_vs_h1', '')
        assert 'double' in h2.lower() or '2x' in h2.lower()

    def test_commercial_investment_in_competitors(self, mechanism_114):
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        assert layer3.get('commercially_invested_in_competitor_platforms') is True

    def test_negative_coverage_risk(self, mechanism_114):
        """If negative coverage of Google/OpenAI reduces platform usage, Future Optic value drops."""
        layer3 = mechanism_114.get('layer_3_future_optic', {})
        risk = layer3.get('negative_coverage_reduces_product_value', '')
        assert risk is True or 'true' in str(risk).lower()


# ── Class 5: Meta Zero Relationship ──────────────────────────────────


class TestMetaZeroRelationship:
    """Verify that Meta has zero financial relationship with Future plc."""

    def test_meta_section_exists(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship')
        assert meta is not None

    def test_meta_content_licensing(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship', {})
        assert meta.get('content_licensing_deal') is False or meta.get('content_licensing_deal') == 'none'

    def test_meta_advertising_dependency(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship', {})
        assert meta.get('advertising_dependency') is False or meta.get('advertising_dependency') == 'none'

    def test_meta_commercial_products(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship', {})
        assert meta.get('commercial_products_dependent_on_meta') is False or \
            meta.get('commercial_products_dependent_on_meta') == 'none'

    def test_meta_ad_competitor_to_google(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship', {})
        assert meta.get('meta_competes_with_google_for_ad_spend') is True

    def test_total_meta_financial_value(self, mechanism_114):
        meta = mechanism_114.get('meta_financial_relationship', {})
        value = meta.get('total_financial_relationship_usd')
        assert value == 0


# ── Class 6: Compound Incentive Architecture ─────────────────────────


class TestCompoundIncentiveArchitecture:
    """Verify the compound incentive structure: all three layers reinforce."""

    def test_compound_section_exists(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture')
        assert compound is not None

    def test_three_layers_documented(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        layers = compound.get('reinforcing_layers', [])
        assert len(layers) == 3, f"Expected 3 reinforcing layers, got {len(layers)}"

    def test_meta_as_safe_target(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        safe = compound.get('meta_safe_target')
        assert safe is True

    def test_explains_mechanism_110(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        explains = compound.get('explains_mechanism_110_editorial_effect', '')
        assert 'combative' in explains.lower() or 'hero' in explains.lower() or \
            'editorial' in explains.lower()

    def test_zero_risk_meta_coverage(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        risk = compound.get('meta_coverage_financial_risk', '')
        assert 'zero' in risk.lower() or '0' in risk

    def test_google_coverage_risk(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        risk = compound.get('google_coverage_financial_risk', '')
        assert 'existential' in risk.lower() or 'high' in risk.lower()

    def test_openai_coverage_risk(self, mechanism_114):
        compound = mechanism_114.get('compound_incentive_architecture', {})
        risk = compound.get('openai_coverage_financial_risk', '')
        assert 'strategic' in risk.lower() or 'moderate' in risk.lower() or \
            'partnership' in risk.lower()


# ── Class 7: Confounding Factors ─────────────────────────────────────


class TestConfoundingFactors:
    """Verify confounding factors are documented with appropriate strengths."""

    def test_confounding_factors_exist(self, mechanism_114):
        factors = mechanism_114.get('confounding_factors', [])
        assert len(factors) >= 5, f"Expected >=5 confounding factors, got {len(factors)}"

    def test_editorial_independence_factor(self, mechanism_114):
        factors = mechanism_114.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_editorial = any('editorial' in t.lower() and 'independen' in t.lower() for t in texts)
        assert has_editorial, "Must document editorial independence as confounding factor"

    def test_strong_factor_exists(self, mechanism_114):
        factors = mechanism_114.get('confounding_factors', [])
        strengths = [f.get('strength', '').upper() for f in factors]
        assert 'STRONG' in strengths, "Must have at least one STRONG confounding factor"

    def test_google_resentment_factor(self, mechanism_114):
        """Google traffic decline HURTS Future — they could resent Google, not protect it."""
        factors = mechanism_114.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_resentment = any('resent' in t.lower() or 'decline' in t.lower() for t in texts)
        assert has_resentment

    def test_meta_privacy_factor(self, mechanism_114):
        factors = mechanism_114.get('confounding_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_privacy = any('privacy' in t.lower() or 'controversi' in t.lower() for t in texts)
        assert has_privacy

    def test_each_factor_has_counter(self, mechanism_114):
        factors = mechanism_114.get('confounding_factors', [])
        for f in factors:
            counter = f.get('counter', '')
            assert len(counter) > 10, f"Factor '{f.get('factor', '')[:40]}...' missing counter-argument"


# ── Class 8: Testable Predictions ────────────────────────────────────


class TestTestablePredictions:
    """Verify testable predictions based on the financial architecture."""

    def test_predictions_exist(self, mechanism_114):
        preds = mechanism_114.get('testable_predictions', [])
        assert len(preds) >= 4, f"Expected >=4 predictions, got {len(preds)}"

    def test_predictions_are_falsifiable(self, mechanism_114):
        preds = mechanism_114.get('testable_predictions', [])
        for pred in preds:
            text = pred if isinstance(pred, str) else str(pred)
            assert len(text) > 20, f"Prediction too short to be falsifiable: {text}"

    def test_predictions_reference_future_plc_brands(self, mechanism_114):
        preds = mechanism_114.get('testable_predictions', [])
        all_text = ' '.join(preds if all(isinstance(p, str) for p in preds) else [str(p) for p in preds])
        assert "Tom's Guide" in all_text or "TechRadar" in all_text or "Future" in all_text


# ── Class 9: Cross-References ────────────────────────────────────────


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_exist(self, mechanism_114):
        xrefs = mechanism_114.get('cross_references', [])
        assert len(xrefs) >= 3, f"Expected >=3 cross-references, got {len(xrefs)}"

    def test_references_mechanism_110(self, mechanism_114):
        """Must reference mechanism #110 (Future plc editor-in-chief-level framing)."""
        xrefs = mechanism_114.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 110 in ids, "Must reference mechanism #110 (Future plc editorial effect)"

    def test_references_mechanism_108(self, mechanism_114):
        """Must reference mechanism #108 (Ziff Davis triple squeeze)."""
        xrefs = mechanism_114.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 108 in ids, "Must reference mechanism #108 (Ziff Davis triple squeeze)"

    def test_references_mechanism_109(self, mechanism_114):
        """Must reference mechanism #109 (Engadget Google privacy zero-out)."""
        xrefs = mechanism_114.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 109 in ids, "Must reference mechanism #109 (Engadget Google privacy zero-out)"

    def test_cross_references_have_connections(self, mechanism_114):
        xrefs = mechanism_114.get('cross_references', [])
        for xref in xrefs:
            conn = xref.get('connection', '')
            assert len(conn) > 20, f"Cross-reference to #{xref.get('mechanism_id')} missing connection text"


# ── Class 10: Entity Profile Update ─────────────────────────────────


class TestEntityProfileUpdate:
    """Verify the future_plc entity in competitor-entities.yaml is updated."""

    def test_openai_deal_section_exists(self, future_plc_entity):
        deal = future_plc_entity.get('openai_content_deal')
        assert deal is not None, "Missing openai_content_deal in future_plc entity"

    def test_openai_deal_date(self, future_plc_entity):
        deal = future_plc_entity.get('openai_content_deal', {})
        assert deal.get('signed_date') == '2024-12-05'

    def test_openai_deal_brands_count(self, future_plc_entity):
        deal = future_plc_entity.get('openai_content_deal', {})
        count = deal.get('brands_licensed_count')
        assert count >= 200

    def test_future_optic_section_exists(self, future_plc_entity):
        optic = future_plc_entity.get('future_optic')
        assert optic is not None, "Missing future_optic in future_plc entity"

    def test_future_optic_pipeline(self, future_plc_entity):
        optic = future_plc_entity.get('future_optic', {})
        pipeline = optic.get('full_year_pipeline_gbp_m')
        assert pipeline == 10

    def test_h1_2026_detailed_financials(self, future_plc_entity):
        fin = future_plc_entity.get('h1_2026_detailed_financials')
        assert fin is not None, "Missing h1_2026_detailed_financials in future_plc entity"

    def test_h1_2026_revenue(self, future_plc_entity):
        fin = future_plc_entity.get('h1_2026_detailed_financials', {})
        rev = fin.get('revenue_gbp_m')
        assert rev == 349.1

    def test_compound_architecture_section(self, future_plc_entity):
        compound = future_plc_entity.get('compound_incentive_architecture')
        assert compound is not None, "Missing compound_incentive_architecture in future_plc entity"

    def test_mechanism_114_in_mechanisms_list(self, future_plc_entity):
        mechs = future_plc_entity.get('mechanisms', [])
        ids = [m.get('mechanism_id') for m in mechs]
        assert 114 in ids, "Mechanism #114 not in future_plc entity mechanisms list"
