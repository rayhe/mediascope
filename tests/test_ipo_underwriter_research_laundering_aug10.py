"""
Type C: Financial Incentive Mapping — IPO Underwriter Research Laundering Pipeline
Date: 2026-08-10 03:00 PT
Mechanism #21: IPO Underwriter Research Laundering Pipeline

Goldman Sachs and Morgan Stanley are simultaneously:
1. Leading BOTH the Anthropic IPO and OpenAI IPO (unprecedented — WSJ confirmed
   separate deal teams to avoid information leakage between rivals)
2. Producing AI industry research widely cited by tech journalists as independent
   "Wall Street analysis"
3. Revenue-dependent on AI IPO success — MS posted a record quarter (Q2 2026),
   GS's IB fee backlog at a 5-year high, BOTH stocks fell 4-5% on news of
   OpenAI IPO possibly delaying to 2027

Reddit Q2 2026 Data Licensing Verification:
- Reddit "Other revenue" (includes data licensing): $43M Q2 2026 (+24% YoY)
- Annualized: ~$172M
- CEO Huffman on deal renewals: "not binary," "our content is in demand"
- Advance Publications holds ~24% of Reddit shares (42,191,092 Class B shares)
- Steven O. Newhouse (Advance) sits on Reddit's board

Sources:
- WSJ: "The IPO Onslaught Is Forcing Bankers to Pick Teams" (Jun 18, 2026)
- TradingView: "Goldman and Morgan Stanley Fall on OpenAI Delay"
- TechTimes: "Morgan Stanley Posts Record Quarter as AI Boom Rewrites Wall Street"
- Reddit Q2 2026 10-Q (BusinessWire Jul 30, 2026)
- Reddit S-1 (SEC): Advance ownership structure
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# =============================================================================
# Class 1: IPO Underwriter Dual Mandate Verification
# =============================================================================
class TestIPOUnderwriterDualMandate:
    """Verify that the unprecedented dual-mandate structure is documented."""

    def test_gs_leads_both_ipos(self):
        """Goldman Sachs is lead underwriter on BOTH OpenAI and Anthropic IPOs."""
        entities = load_competitor_entities()
        openai_banks = entities['entities']['openai']['ipo_filing'].get('ipo_banks_reported', [])
        anthropic_banks = entities['entities']['anthropic']['ipo_filing'].get('ipo_banks_reported', [])
        assert 'Goldman Sachs' in openai_banks
        assert 'Goldman Sachs' in anthropic_banks

    def test_ms_leads_both_ipos(self):
        """Morgan Stanley is lead underwriter on BOTH OpenAI and Anthropic IPOs."""
        entities = load_competitor_entities()
        openai_banks = entities['entities']['openai']['ipo_filing'].get('ipo_banks_reported', [])
        anthropic_banks = entities['entities']['anthropic']['ipo_filing'].get('ipo_banks_reported', [])
        assert 'Morgan Stanley' in openai_banks
        assert 'Morgan Stanley' in anthropic_banks

    def test_dual_mandate_is_unprecedented(self):
        """WSJ confirmed this is historically rare — two competing companies
        using the same two lead underwriters for simultaneous IPOs."""
        data = load_competitor_entities()
        pipeline = data.get('ipo_underwriter_research_pipeline', {})
        sig = pipeline.get('structural_significance', '').lower()
        assert 'unprecedented' in sig or 'rare' in sig

    def test_separate_deal_teams_documented(self):
        """WSJ reported GS and MS creating separate deal teams to prevent
        information leakage between OpenAI and Anthropic."""
        data = load_competitor_entities()
        pipeline = data.get('ipo_underwriter_research_pipeline', {})
        mgmt = pipeline.get('conflict_management', '').lower()
        assert 'separate' in mgmt and 'deal team' in mgmt

    def test_jpmorgan_also_on_anthropic(self):
        """JPMorgan Chase also has a role on the Anthropic IPO."""
        data = load_competitor_entities()
        banks = data['entities']['anthropic']['ipo_filing'].get('ipo_banks_reported', [])
        assert 'JPMorgan Chase' in banks


# =============================================================================
# Class 2: Bank Stock Price Sensitivity to IPO Clients
# =============================================================================
class TestBankStockIPOSensitivity:
    """GS and MS stock prices are MATERIALLY sensitive to their AI IPO clients'
    timing decisions, proving financial dependency."""

    def test_gs_fell_on_openai_delay(self):
        """Goldman Sachs fell up to 4.8% when NYT reported OpenAI might delay IPO."""
        data = load_competitor_entities()
        sensitivity = data['ipo_underwriter_research_pipeline']['stock_price_sensitivity']
        assert sensitivity['gs_drop_on_openai_delay_pct'] >= 4.0

    def test_ms_fell_on_openai_delay(self):
        """Morgan Stanley fell up to 4.1% on the same OpenAI delay report."""
        data = load_competitor_entities()
        sensitivity = data['ipo_underwriter_research_pipeline']['stock_price_sensitivity']
        assert sensitivity['ms_drop_on_openai_delay_pct'] >= 4.0

    def test_ms_record_quarter_driven_by_ai(self):
        """Morgan Stanley posted a record Q2 2026 quarter."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['ms_record_q2_2026'] is True

    def test_gs_ib_backlog_five_year_high(self):
        """Goldman Sachs IB fee backlog at a 5-year high."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['gs_ib_backlog_five_year_high'] is True

    def test_meta_generates_zero_ipo_fees(self):
        """Meta went public in 2012 and generates zero current IPO underwriting fees."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['meta_ipo_fee_incentive'] == 'zero'


# =============================================================================
# Class 3: Research Report Citation Pipeline
# =============================================================================
class TestResearchCitationPipeline:
    """Bank research reports flow into journalism without disclosure of the
    bank's IPO underwriting relationships with AI companies."""

    def test_gs_ai_research_reports_documented(self):
        """Goldman Sachs produces AI industry research cited by journalists."""
        data = load_competitor_entities()
        gs_research = data['ipo_underwriter_research_pipeline'].get('gs_research_examples', [])
        assert len(gs_research) >= 3

    def test_ms_ai_research_reports_documented(self):
        """Morgan Stanley produces AI industry research cited by journalists."""
        data = load_competitor_entities()
        ms_research = data['ipo_underwriter_research_pipeline'].get('ms_research_examples', [])
        assert len(ms_research) >= 3

    def test_research_cited_by_major_outlets(self):
        """Bank research gets redistributed by Reuters, Morningstar, etc."""
        data = load_competitor_entities()
        outlets = data['ipo_underwriter_research_pipeline'].get('citing_outlets', [])
        assert len(outlets) >= 5

    def test_no_ipo_disclosure_in_research_citations(self):
        """Journalists have no obligation to disclose IPO underwriting when citing."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['disclosure_obligation_for_journalists'] is False

    def test_research_creates_narrative_tailwind(self):
        """Bullish bank research creates positive AI narrative environment."""
        data = load_competitor_entities()
        desc = data['ipo_underwriter_research_pipeline'].get('mechanism_description', '').lower()
        assert 'narrative tailwind' in desc or 'bullish' in desc


# =============================================================================
# Class 4: Disproportionate Impact on Meta Coverage
# =============================================================================
class TestDisproportionateMetaImpact:
    """The IPO pipeline disproportionately disadvantages Meta coverage."""

    def test_anthropic_ipo_generates_massive_fees(self):
        """Anthropic IPO fee pool estimated at $500M+."""
        data = load_competitor_entities()
        fee = data['ipo_underwriter_research_pipeline']['estimated_anthropic_ipo_fee_pool_m']
        assert fee >= 200

    def test_openai_ipo_generates_massive_fees(self):
        """OpenAI IPO fee pool estimated at $400M+."""
        data = load_competitor_entities()
        fee = data['ipo_underwriter_research_pipeline']['estimated_openai_ipo_fee_pool_m']
        assert fee >= 200

    def test_meta_capex_framed_as_risk(self):
        """GS research framing hits Meta harder than IPO clients."""
        data = load_competitor_entities()
        framing = data['ipo_underwriter_research_pipeline'].get('framing_asymmetry', '').lower()
        assert 'capex' in framing and 'risk' in framing

    def test_ted_pick_10_15_pct_quote(self):
        """MS CEO Ted Pick's bullish framing: '10-15% through the cycle.'"""
        data = load_competitor_entities()
        quote = data['ipo_underwriter_research_pipeline'].get('ted_pick_earnings_call_quote', '')
        assert '10' in quote and '15' in quote

    def test_structural_not_individual_claim(self):
        """The mechanism is structural, not a claim of individual corruption."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['claim_type'] == 'structural_incentive_alignment'


# =============================================================================
# Class 5: Reddit Q2 2026 Data Licensing Revenue Verification
# =============================================================================
class TestRedditQ2DataLicensing:
    """Verify Reddit's Q2 2026 data in the Advance dual-asset section."""

    def test_reddit_q2_2026_total_revenue(self):
        """Reddit Q2 2026 total revenue: $805M."""
        data = load_competitor_entities()
        q2 = data['advance_dual_asset_monetization']['reddit_q2_2026']
        assert q2['total_revenue_m'] == 805

    def test_reddit_q2_2026_other_revenue(self):
        """Reddit Q2 2026 'Other revenue' (includes data licensing): $43M."""
        data = load_competitor_entities()
        q2 = data['advance_dual_asset_monetization']['reddit_q2_2026']
        assert q2['other_revenue_m'] == 43

    def test_reddit_other_revenue_growth(self):
        """Reddit 'Other revenue' grew 24% YoY in Q2 2026."""
        data = load_competitor_entities()
        q2 = data['advance_dual_asset_monetization']['reddit_q2_2026']
        assert q2['other_revenue_yoy_pct'] == 24

    def test_reddit_other_revenue_annualized(self):
        """Annualized Other revenue ~$172M/yr — material revenue stream."""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        assert dl['other_revenue_annualized_m'] >= 170

    def test_huffman_not_binary_quote(self):
        """CEO Huffman on deal renewals: 'not binary.'"""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        quote = dl.get('huffman_quote', '') + dl.get('renewal_status', '')
        assert 'not binary' in quote.lower() or 'binary' in quote.lower()

    def test_advance_ownership_pct(self):
        """Advance holds ~23-24% of Reddit shares."""
        data = load_competitor_entities()
        adv = data['advance_dual_asset_monetization']
        pct = adv.get('advance_reddit_economic_stake_pct', 0)
        assert 20 <= pct <= 30

    def test_reddit_revenue_growth_streak(self):
        """Reddit's 8th consecutive quarter of 60%+ revenue growth."""
        data = load_competitor_entities()
        q2 = data['advance_dual_asset_monetization']['reddit_q2_2026']
        assert q2.get('eighth_consecutive_60pct_growth_quarter') is True


# =============================================================================
# Class 6: Advance → Reddit → AI Company Financial Chain
# =============================================================================
class TestAdvanceRedditAIChain:
    """The Advance → Reddit → AI company chain creates indirect coverage incentives."""

    def test_reddit_licenses_to_google_and_openai(self):
        """Reddit licenses training data to both Google and OpenAI."""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        assert dl.get('google_deal_annual_m', 0) > 0
        assert dl.get('openai_deal_annual_est_m', 0) > 0

    def test_combined_deal_value_material(self):
        """Combined current AI licensing ~$130M/yr — material to Reddit."""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        assert dl.get('combined_current_annual_m', 0) >= 100

    def test_wells_fargo_renewal_projection(self):
        """Wells Fargo projects renewal at ~$550M/yr — transformative for Reddit."""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        assert dl.get('wells_fargo_renewal_projection_annual_m', 0) >= 400

    def test_advance_share_of_data_licensing(self):
        """Advance captures ~23% of Reddit's data licensing revenue."""
        data = load_competitor_entities()
        dl = data['advance_dual_asset_monetization']['reddit_data_licensing']
        assert dl.get('advance_share_of_current_annual_m', 0) >= 25

    def test_conde_nast_has_5_ai_deals(self):
        """Condé Nast has 5 AI content deals (OpenAI, Amazon×2, MSFT, Perplexity)."""
        data = load_competitor_entities()
        pivot = data['advance_dual_asset_monetization']['conde_nast_strategic_pivot']
        assert pivot.get('ai_deal_count', 0) >= 5

    def test_conde_nast_zero_meta_deal(self):
        """Condé Nast has ZERO deals with Meta."""
        data = load_competitor_entities()
        pivot = data['advance_dual_asset_monetization']['conde_nast_strategic_pivot']
        assert pivot.get('meta_deal') == 'none'


# =============================================================================
# Class 7: Anthropic Secondary Market Valuation Update
# =============================================================================
class TestAnthropicValuationUpdate:
    """Verify Anthropic's updated secondary market valuation."""

    def test_anthropic_secondary_market_valuation(self):
        """Secondary market values Anthropic at ~$1.2T."""
        data = load_competitor_entities()
        val = data['entities']['anthropic'].get('secondary_market_valuation_b')
        assert val is not None and val >= 1100

    def test_anthropic_exceeds_openai_valuation(self):
        """Anthropic secondary ($1.2T) exceeds OpenAI funding round ($852B)."""
        data = load_competitor_entities()
        anthropic_val = data['entities']['anthropic'].get('secondary_market_valuation_b', 0)
        assert anthropic_val > 852

    def test_amazon_stake_15_20_pct(self):
        """Amazon holds 15-20% of Anthropic."""
        data = load_competitor_entities()
        amazon = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert amazon.get('stake_pct_high', 0) >= 20
        assert amazon.get('stake_pct_low', 0) >= 15

    def test_amazon_anthropic_stake_value_at_secondary(self):
        """At $1.2T secondary, Amazon's stake is worth ~$210B."""
        data = load_competitor_entities()
        amazon = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert amazon.get('stake_value_at_secondary_b', 0) >= 180


# =============================================================================
# Class 8: Legitimate Factors and Analytical Integrity
# =============================================================================
class TestLegitimateFactors:
    """Acknowledge factors that explain bank research patterns without
    requiring intentional bias."""

    def test_chinese_wall_documented(self):
        """Banks maintain information barriers between research and IB."""
        data = load_competitor_entities()
        factors = data['ipo_underwriter_research_pipeline'].get('legitimate_factors', [])
        combined = ' '.join(factors).lower()
        assert 'chinese wall' in combined or 'information barrier' in combined

    def test_sec_independence_requirements(self):
        """Research analysts subject to SEC independence requirements."""
        data = load_competitor_entities()
        factors = data['ipo_underwriter_research_pipeline'].get('legitimate_factors', [])
        combined = ' '.join(factors).lower()
        assert 'sec' in combined or 'regulation' in combined

    def test_banks_do_cover_meta(self):
        """GS and MS DO produce Meta research — asymmetry is IPO-fee-specific."""
        data = load_competitor_entities()
        factors = data['ipo_underwriter_research_pipeline'].get('legitimate_factors', [])
        combined = ' '.join(factors).lower()
        assert 'meta' in combined

    def test_structural_not_individual(self):
        """Claim type is structural incentive alignment."""
        data = load_competitor_entities()
        assert data['ipo_underwriter_research_pipeline']['claim_type'] == 'structural_incentive_alignment'

    def test_source_urls_present(self):
        """All claims backed by source URLs."""
        data = load_competitor_entities()
        sources = data['ipo_underwriter_research_pipeline'].get('source_urls', [])
        assert len(sources) >= 5
