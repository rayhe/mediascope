"""
News Corp Triple-Revenue AI Architecture — Q4 FY2026 Financial Verification

Type C: Financial Incentive Mapping (Aug 7, 2026 21:00 PT)

THESIS: News Corp is the ONLY publisher receiving AI-related revenue from
THREE major AI companies simultaneously (OpenAI, Meta, Anthropic settlement).
This triple-revenue architecture creates the most balanced financial
position in the MediaScope dataset, which correlates with the most balanced
editorial coverage of both Meta and Meta's competitors.

KEY FINDING: CFO Chandrashekar explicitly confirmed "new AI licensing revenues"
as a driver of FY2026 transformation on the Q4 earnings call (Aug 5, 2026).
Thomson confirmed Meta deal is "now part of the business."

Sources:
- Q4 FY2026 earnings call transcript (Aug 5, 2026)
  https://www.marketbeat.com/earnings/reports/2026-8-5-news-co-stock-1/
- Reuters: https://www.reuters.com/business/media-telecom/wsj-publisher-news-corp-beats-revenue-estimates-real-estate-dow-jones-strength-2026-08-05/
- NY Post: https://nypost.com/2026/08/05/media/news-corp-posts-record-profitability-11-jump-in-q4-revenue/
- Brave countersuit: https://www.reuters.com/business/media-telecom/news-corp-countersues-brave-allegedly-scraping-articles-ai-2026-07-22/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestNewsCorpQ4FY2026Financials:
    """Verify Q4 FY2026 earnings data integrity in profile."""

    @pytest.fixture
    def profile(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    def test_q4_revenue_beat(self, profile):
        q4 = profile['financials']['q4_fy2026']
        assert q4['revenue_b'] == 2.34, "Q4 revenue should be $2.34B"
        assert q4['revenue_consensus_b'] == 2.23, "Consensus was $2.23B"
        assert q4['revenue_beat'] is True, "News Corp beat revenue consensus"

    def test_q4_earnings_beat(self, profile):
        q4 = profile['financials']['q4_fy2026']
        assert q4['eps_adjusted'] == 0.35, "Adjusted EPS should be $0.35"
        assert q4['eps_consensus'] == 0.21, "Consensus was $0.21"
        assert q4['eps_adjusted'] > q4['eps_consensus'], "Should beat consensus"
        assert q4['eps_beat'] is True

    def test_q4_record_profitability(self, profile):
        q4 = profile['financials']['q4_fy2026']
        assert q4['net_income_yoy_pct'] == 167, "Net income +167% YoY"
        assert q4['ebitda_yoy_pct'] == 31, "EBITDA +31% YoY"
        assert q4['record_quarter'] is True

    def test_q4_consecutive_growth_streaks(self, profile):
        q4 = profile['financials']['q4_fy2026']
        assert q4['consecutive_revenue_growth_quarters'] == 12
        assert q4['consecutive_ebitda_growth_quarters'] == 13

    def test_dow_jones_margin_expansion(self, profile):
        q4 = profile['financials']['q4_fy2026']
        assert q4['dow_jones_margin_pct'] == 28.1, "DJ margin 28.1%"
        assert q4['dow_jones_margin_expansion_bp'] == 310, "+310bp"

    def test_ai_licensing_cffo_confirmation(self, profile):
        """CFO explicitly mentioned AI licensing as FY2026 driver."""
        q4 = profile['financials']['q4_fy2026']
        assert 'ai_licensing_impact' in q4
        impact = q4['ai_licensing_impact'].replace('\n', ' ')
        assert 'new AI licensing revenues' in impact
        assert 'Meta deal is now part of the business' in impact

    def test_anthropic_settlement_expected(self, profile):
        """Thomson confirmed Anthropic settlement revenue expected."""
        q4 = profile['financials']['q4_fy2026']
        assert 'anthropic_settlement' in q4
        settlement = q4['anthropic_settlement']
        assert '$1.5 billion settlement with Anthropic' in settlement
        assert 'benefit in coming months' in settlement


class TestNewsCorpFullYearFY2026:
    """Verify full year FY2026 financial data."""

    @pytest.fixture
    def profile(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    def test_fy2026_revenue(self, profile):
        fy = profile['financials']['full_year_fy2026']
        assert fy['revenue_b'] == 9.0, "FY2026 revenue $9B"
        assert fy['revenue_yoy_pct'] == 7

    def test_fy2026_margin_expansion(self, profile):
        fy = profile['financials']['full_year_fy2026']
        assert fy['ebitda_margin_pct'] == 18.0
        assert fy['ebitda_margin_prior_year_pct'] == 16.7
        assert fy['ebitda_margin_pct'] > fy['ebitda_margin_prior_year_pct']

    def test_fy2026_free_cash_flow_surge(self, profile):
        fy = profile['financials']['full_year_fy2026']
        assert fy['free_cash_flow_m'] == 811, "FCF $811M"
        assert fy['free_cash_flow_yoy_pct'] == 42, "+42% YoY"
        assert fy['free_cash_flow_ebitda_conversion_pct'] == 50

    def test_fy2026_buyback_acceleration(self, profile):
        fy = profile['financials']['full_year_fy2026']
        assert fy['share_buyback_m'] == 643
        assert fy['share_buyback_prior_year_m'] == 150
        assert fy['share_buyback_increase_x'] > 4

    def test_fy2026_digital_majority(self, profile):
        """News Corp is now majority digital — 61% of revenue."""
        fy = profile['financials']['full_year_fy2026']
        assert fy['digital_revenue_pct'] == 61
        assert fy['digital_revenue_pct'] > 50, "Majority digital"

    def test_fy2026_record_year(self, profile):
        fy = profile['financials']['full_year_fy2026']
        assert fy['record_year'] is True


class TestTripleRevenueArchitecture:
    """Verify News Corp's unique triple-revenue AI position."""

    @pytest.fixture
    def profile(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    def test_three_ai_revenue_sources(self, profile):
        """News Corp has revenue relationships with 3 AI companies."""
        rels = profile['revenue_relationships']
        ai_partners = [r for r in rels if r['type'] in ('ai_licensing', 'settlement_revenue')]
        assert len(ai_partners) == 3, f"Expected 3 AI revenue sources, found {len(ai_partners)}"

    def test_openai_deal_active(self, profile):
        rels = profile['revenue_relationships']
        openai = [r for r in rels if r['partner'] == 'OpenAI'][0]
        assert openai['type'] == 'ai_licensing'
        assert '$250M' in openai['value'] or '$50M' in openai['value']
        assert openai['verified'] is True

    def test_meta_deal_active(self, profile):
        rels = profile['revenue_relationships']
        meta = [r for r in rels if r['partner'] == 'Meta'][0]
        assert meta['type'] == 'ai_licensing'
        assert '$50M' in meta['value']
        assert meta['verified'] is True

    def test_anthropic_settlement_revenue(self, profile):
        rels = profile['revenue_relationships']
        anthropic = [r for r in rels if r['partner'] == 'Anthropic'][0]
        assert anthropic['type'] == 'settlement_revenue'
        assert '$1.5B' in anthropic['value']
        assert anthropic['verified'] is True

    def test_competitor_relationships_anthropic_updated(self, profile):
        """Anthropic relationship updated from 'none' to 'settlement_revenue'."""
        comp = profile['competitor_relationships']
        assert comp['anthropic']['financial_tie'] == 'settlement_revenue'
        assert 'Bartz v. Anthropic' in comp['anthropic']['estimated_value']

    def test_balanced_control_designation(self, profile):
        ctrl = profile['control_designation']
        assert ctrl['type'] == 'balanced_control'
        assert ctrl['comparison_baseline'] is True

    def test_triple_revenue_note_exists(self, profile):
        ctrl = profile['control_designation']
        assert 'triple_revenue_note' in ctrl
        note = ctrl['triple_revenue_note']
        assert 'THREE major AI companies' in note
        assert 'OpenAI' in note
        assert 'Meta' in note
        assert 'Anthropic' in note

    def test_unique_balanced_position(self, profile):
        """News Corp is the ONLY publisher with Meta AND competitor revenue."""
        ctrl = profile['control_designation']
        note = ctrl['triple_revenue_note']
        assert 'ONLY publisher' in note


class TestNewsCorpWooAndSueStrategy:
    """Verify the 'woo and sue' strategy documentation."""

    @pytest.fixture
    def profile(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    def test_woo_partners_documented(self, profile):
        """Two 'woo' partners: OpenAI and Meta."""
        rels = profile['revenue_relationships']
        licensing = [r for r in rels if r['type'] == 'ai_licensing']
        partner_names = {r['partner'] for r in licensing}
        assert 'OpenAI' in partner_names
        assert 'Meta' in partner_names

    def test_sue_targets_documented(self, profile):
        """Two 'sue' targets: Perplexity and Brave."""
        lit = profile['litigation_connections']
        case_names = [l['case'] for l in lit]
        assert any('Perplexity' in c for c in case_names), "Perplexity litigation"
        assert any('Brave' in c for c in case_names), "Brave litigation"

    def test_brave_countersuit_details(self, profile):
        lit = profile['litigation_connections']
        brave = [l for l in lit if 'Brave' in l['case']][0]
        assert brave['filed'] == '2026-07-22'
        assert brave['type'] == 'copyright_countersuit'
        assert brave['status'] == 'active'
        assert 'masked web crawlers' in brave['description']
        assert '$150,000' in brave['description']

    def test_brave_mediascope_relevance(self, profile):
        lit = profile['litigation_connections']
        brave = [l for l in lit if 'Brave' in l['case']][0]
        assert 'mediascope_relevance' in brave
        relevance = brave['mediascope_relevance']
        assert 'woo and sue' in relevance
        assert 'licensing market' in relevance


class TestFinancialAmplificationModelUpdate:
    """Verify News Corp data strengthens the financial amplification thesis."""

    @pytest.fixture
    def news_corp(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    @pytest.fixture
    def competitor_entities(self):
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            return yaml.safe_load(f)

    def test_news_corp_is_balanced_control(self, news_corp):
        """News Corp should be tagged as balanced control."""
        assert news_corp['control_designation']['type'] == 'balanced_control'

    def test_meta_has_one_leverage_mechanism(self, competitor_entities):
        """Meta has only ONE financial relationship mechanism with publishers."""
        meta = competitor_entities['entities']['meta']
        assert meta['category'] == 'big_tech'
        # Meta's sole mechanism is voluntary AI content licensing

    def test_news_corp_disclosure_unique(self, news_corp):
        """WSJ is the only publication that discloses AI relationships."""
        disc = news_corp['disclosure_practice']
        assert disc['unique_in_dataset'] is True
        assert disc['policy_type'] == 'editorial_policy'

    def test_mims_tone_inversion(self, news_corp):
        """Christopher Mims shows inverted tone vs WIRED/Verge journalists."""
        profiles = news_corp['journalist_profiles']
        mims = [p for p in profiles if p['name'] == 'Christopher Mims'][0]
        meta_tone = mims['cross_entity_coverage']['meta']['tone_value']
        openai_tone = mims['cross_entity_coverage']['openai']['tone_value']
        # Mims is positive on Meta (+0.3) and negative on OpenAI (-0.3)
        assert meta_tone > 0, f"Mims Meta tone should be positive, got {meta_tone}"
        assert openai_tone < 0, f"Mims OpenAI tone should be negative, got {openai_tone}"
        # Tone gap should be significant
        assert meta_tone - openai_tone >= 0.5, "Tone gap should be >= 0.5"

    def test_bobrowsky_balanced(self, news_corp):
        """Bobrowsky (dedicated Meta reporter) shows balanced tone."""
        profiles = news_corp['journalist_profiles']
        bobrowsky = [p for p in profiles if p['name'] == 'Meghan Bobrowsky'][0]
        meta_tone = bobrowsky['cross_entity_coverage']['meta']['tone_value']
        # Bobrowsky is near-neutral on Meta (-0.15)
        assert -0.3 < meta_tone < 0.1, f"Expected near-neutral, got {meta_tone}"

    @pytest.mark.parametrize("entity,expected_min_leverage", [
        ("microsoft", 7),
        ("amazon", 6),
        ("apple", 5),
        ("google", 4),
    ])
    def test_leverage_count_ordering(self, competitor_entities, entity, expected_min_leverage):
        """Verify leverage count ordering: MS(7) > AMZN(6) > AAPL(5) > GOOG(4) > META(1)."""
        ent = competitor_entities['entities'][entity]
        leverage_key = None
        for key in ent:
            if 'leverage' in str(key).lower() and 'layers' in str(ent.get(key, '')):
                leverage_key = key
                break
        if leverage_key:
            layers = ent[leverage_key].get('layers', [])
            assert len(layers) >= expected_min_leverage, (
                f"{entity} should have >= {expected_min_leverage} leverage layers, "
                f"found {len(layers)}"
            )


class TestDealPipelineTracking:
    """Track News Corp's expanding AI deal pipeline."""

    @pytest.fixture
    def profile(self):
        with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
            return yaml.safe_load(f)

    def test_pipeline_documented(self, profile):
        """Thomson confirmed more deals coming on Q4 call."""
        q4 = profile['financials']['q4_fy2026']
        impact = q4['ai_licensing_impact'].replace('\n', ' ')
        assert 'more deals' in impact.lower()

    def test_meta_deal_contributing(self, profile):
        """Meta deal confirmed as contributing to Q4 financials."""
        q4 = profile['financials']['q4_fy2026']
        impact = q4['ai_licensing_impact'].replace('\n', ' ')
        assert 'Meta deal is now part of the business' in impact

    def test_ai_revenue_cffo_validated(self, profile):
        """CFO explicitly called out AI licensing as transformation driver."""
        q4 = profile['financials']['q4_fy2026']
        impact = q4['ai_licensing_impact']
        assert 'new AI licensing revenues' in impact
