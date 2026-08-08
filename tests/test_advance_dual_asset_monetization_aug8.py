"""
Type C: Financial Incentive Mapping — Advance Publications Dual-Asset AI Content Monetization Architecture
Date: 2026-08-08 06:00 PT

KEY FINDING: Advance Publications operates TWO parallel content monetization channels
through its subsidiaries (Reddit 23.3% economic stake + Condé Nast wholly owned),
creating the most comprehensive undisclosed conflict of interest in AI journalism.

Reddit Q2 2026 earnings (Jul 30): $805M revenue (+61% YoY), Other Revenue $43M (+24% YoY,
includes data licensing), annualized ~$172M. Google deal $60M/yr, OpenAI ~$70M/yr.
Wells Fargo projects combined renewal at $550M/yr. Huffman: "range of outcomes is wide."

Condé Nast strategic pivot (Oct 2025): CEO Lynch says advertising "no longer a growth engine."
Pivoting to events (+40% 2025), subscriptions, commerce, and AI licensing (5 active deals).

WIRED's editorial coverage of AI content licensing directly supports Advance's financial
interests through BOTH subsidiaries — yet this dual-asset conflict is never disclosed.

Sources:
- Reddit Q2 2026 earnings call transcript: https://www.fool.com/earnings/call-transcripts/2026/07/30/reddit-rddt-q2-2026-earnings-call-transcript/
- Reddit Q2 2026 earnings: http://www.shacknews.com/article/150199/reddit-rddt-q2-2026-earnings-results
- Reddit data licensing renewal projections: https://www.barrons.com/articles/buy-reddit-stock-price-pick-eef67fe8
- Reddit ownership: https://fourweekmba.com/who-owns-reddit/
- Condé Nast events strategy: https://www.adweek.com/media/conde-nast-events-revenue-2026/
- Condé Nast-OpenAI deal: https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/
- Advance Reddit IPO windfall: https://www.thewrap.com/conde-nast-advance-publications-reddit-ipo/
- Reddit AI deal dynamics: https://www.webpronews.com/reddit-negotiates-dynamic-ai-data-deals-with-google-openai/
- Reddit earnings highlights: https://www.zacks.com/stock/news/2965766/rddt-q2-earnings-call-highlights-ai-user-growth-push
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_wired_profile():
    path = os.path.join(PROFILES_DIR, 'wired.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestRedditQ2_2026Earnings:
    """Verify Reddit Q2 2026 financial data in competitor entities."""

    def test_reddit_q2_revenue(self):
        data = load_competitor_entities()
        google = data['entities']['google']
        # Reddit earnings tracked in google entity (via Advance/Reddit relationship)
        # Check advance_dual_asset section exists
        assert 'advance_dual_asset_monetization' in data, \
            "Missing advance_dual_asset_monetization section in competitor-entities.yaml"

    def test_reddit_q2_total_revenue(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['total_revenue_m'] == 805

    def test_reddit_q2_revenue_yoy_pct(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['revenue_yoy_pct'] == 61

    def test_reddit_q2_other_revenue(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['other_revenue_m'] == 43

    def test_reddit_q2_other_revenue_yoy(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['other_revenue_yoy_pct'] == 24

    def test_reddit_q2_ad_revenue(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['ad_revenue_m'] == 762

    def test_reddit_q2_net_income(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['net_income_m'] == 253

    def test_reddit_q2_eps(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['eps'] == 1.25

    def test_reddit_q2_ebitda_margin_pct(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['ebitda_margin_pct'] == 43

    def test_reddit_q2_dau_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['dau_m'] == 130.3

    def test_reddit_q2_wau_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert reddit['wau_m'] == 514.6


class TestAdvanceOwnershipStructure:
    """Verify Advance Publications ownership data."""

    def test_advance_reddit_economic_stake_pct(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['advance_reddit_economic_stake_pct'] == 23.3

    def test_advance_conde_nast_ownership(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['advance_conde_nast_ownership'] == 'wholly_owned'

    def test_advance_board_designation_rights(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['advance_reddit_board_designees'] == 2

    def test_advance_reddit_board_observer(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['advance_reddit_board_observer'] == 1

    def test_sam_altman_reddit_stake(self):
        """Sam Altman (OpenAI CEO) owns 8.7% of Reddit — personal financial
        interest in the very data licensing ecosystem his company participates in."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['sam_altman_reddit_stake_pct'] == 8.7


class TestRedditDataLicensingDeals:
    """Verify Reddit AI data licensing deal data."""

    def test_google_deal_annual_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert deals['google_deal_annual_m'] == 60

    def test_openai_deal_annual_est_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert deals['openai_deal_annual_est_m'] == 70

    def test_combined_current_annual_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert deals['combined_current_annual_m'] == 130

    def test_wells_fargo_renewal_projection_m(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert deals['wells_fargo_renewal_projection_annual_m'] == 550

    def test_other_revenue_annualized_m(self):
        """Q2 Other Revenue $43M × 4 = $172M annualized run rate."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert deals['other_revenue_annualized_m'] == 172

    def test_renewal_status(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        deals = section['reddit_data_licensing']
        assert 'negotiat' in deals['renewal_status'].lower() or \
               'not binary' in deals['huffman_quote'].lower()


class TestCondeNastStrategicPivot:
    """Verify Condé Nast pivot from advertising to AI licensing."""

    def test_lynch_advertising_quote(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        assert 'no longer' in pivot['lynch_advertising_assessment'].lower() or \
               'not a growth engine' in pivot['lynch_advertising_assessment'].lower()

    def test_events_revenue_growth_2025_pct(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        assert pivot['events_revenue_growth_2025_pct'] == 40

    def test_events_revenue_projected_growth_2026_pct(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        assert pivot['events_revenue_projected_growth_2026_pct'] == 22

    def test_conde_nast_ai_deal_count(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        assert pivot['ai_deal_count'] >= 5

    def test_conde_nast_ai_partners(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        partners = pivot['ai_partners']
        assert 'OpenAI' in partners
        assert 'Amazon' in partners or 'Rufus' in str(partners)
        assert 'Microsoft' in partners or 'PCM' in str(partners)
        assert 'Perplexity' in partners

    def test_conde_nast_meta_deal(self):
        """Condé Nast has ZERO Meta deals despite 5 competitor deals."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        assert pivot['meta_deal'] == 'none'

    def test_new_growth_pillars(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        pivot = section['conde_nast_strategic_pivot']
        pillars = pivot['new_growth_pillars']
        assert 'events' in [p.lower() for p in pillars]
        assert any('licens' in p.lower() for p in pillars)


class TestDualAssetConflictMechanism:
    """Verify the dual-asset conflict of interest analysis."""

    def test_dual_asset_overview_exists(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert 'overview' in section
        assert len(section['overview']) > 100

    def test_dual_asset_mentions_reddit(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert 'Reddit' in section['overview']

    def test_dual_asset_mentions_conde_nast(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        overview = section['overview']
        assert 'Condé Nast' in overview or 'Conde Nast' in overview

    def test_dual_asset_mentions_wired(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert 'WIRED' in section['overview']

    def test_dual_asset_editorial_incentive(self):
        """Every WIRED article arguing 'AI must pay for content' benefits both
        Reddit's renewal negotiations AND Condé Nast's own licensing revenue."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        analysis = section['editorial_incentive_analysis']
        assert 'Reddit' in analysis
        assert 'Condé Nast' in analysis or 'Conde Nast' in analysis

    def test_disclosure_status(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['disclosed_in_wired_coverage'] is False

    def test_asset_count(self):
        """Advance has exactly 2 content monetization assets."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert len(section['content_monetization_assets']) == 2

    def test_asset_types(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assets = section['content_monetization_assets']
        asset_types = [a['type'] for a in assets]
        assert 'user_generated_content' in asset_types
        assert 'professional_editorial_content' in asset_types


class TestSamAltmanRedditConflict:
    """Sam Altman owns 8.7% of Reddit while running OpenAI — the company
    that pays Reddit $70M/yr for data licensing AND pays Condé Nast for
    editorial content. Triple financial entanglement."""

    def test_altman_stake_documented(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['sam_altman_reddit_stake_pct'] == 8.7

    def test_altman_conflict_description(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        conflict = section['altman_reddit_conflict']
        assert 'OpenAI' in conflict
        assert 'Reddit' in conflict

    def test_altman_profits_from_both_sides(self):
        """Altman profits when Reddit charges OpenAI more (his Reddit equity rises)
        AND when OpenAI signs more publisher deals (his OpenAI equity rises).
        He wins regardless of who pays whom."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        conflict = section['altman_reddit_conflict']
        assert 'both' in conflict.lower() or 'dual' in conflict.lower() or \
               'regardless' in conflict.lower()


class TestAdvanceFinancialMath:
    """Quantitative validation of Advance's financial exposure."""

    def test_reddit_market_cap_range(self):
        """Reddit market cap at ~$29B (at $140/share × 206.6M diluted shares)."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        math = section['financial_math']
        assert 25 <= math['reddit_market_cap_approx_b'] <= 40

    def test_advance_reddit_equity_value_b(self):
        """Advance's 23.3% of Reddit ≈ $6-8B."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        math = section['financial_math']
        assert 5 <= math['advance_reddit_equity_value_approx_b'] <= 10

    def test_licensing_renewal_equity_impact(self):
        """If licensing renewal hits $550M/yr, additional equity value
        for Advance is estimated at $2-4B at Reddit's revenue multiples."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        math = section['financial_math']
        assert math['licensing_renewal_equity_impact_est_b'] >= 1

    def test_meta_contrast_leverage_count(self):
        """Advance family has dual-asset leverage; Meta has 1 mechanism
        (voluntary licensing). Advance benefits from 2 parallel channels."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert section['advance_content_monetization_channels'] == 2
        assert section['meta_content_monetization_channels'] == 1


class TestSearchReferralVolatility:
    """Reddit's search traffic decline creates financial pressure that
    strengthens Advance's incentive for AI-friendly editorial coverage."""

    def test_search_volatility_documented(self):
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert 'search' in reddit.get('traffic_note', '').lower() or \
               'volatile' in reddit.get('traffic_note', '').lower()

    def test_ai_overviews_impact_quote(self):
        """Huffman: 'AI overviews has yet to make a similar level of positive
        impact' — Reddit affected by same traffic cannibalization as publishers."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        reddit = section['reddit_q2_2026']
        assert 'AI overviews' in reddit.get('huffman_ai_overviews_quote', '') or \
               'positive impact' in reddit.get('huffman_ai_overviews_quote', '')


class TestCrossEntityIntegration:
    """Ensure new Advance dual-asset data integrates with existing entity profiles."""

    def test_conde_nast_excluded_publisher_still_present(self):
        """Condé Nast should still be in excluded_publishers with deal_count >= 5."""
        data = load_competitor_entities()
        excluded = data.get('meta_ai_deals', {}).get('excluded_publishers', [])
        conde_entries = [e for e in excluded
                         if 'Condé Nast' in e.get('name', '') or 'Conde Nast' in e.get('name', '')]
        assert len(conde_entries) >= 1
        assert conde_entries[0]['deal_count'] >= 5

    def test_reddit_deal_renewal_in_google_entity(self):
        """Google entity should still have reddit_deal_instability or renewal data."""
        data = load_competitor_entities()
        google = data['entities']['google']
        has_reddit = ('reddit_deal_instability' in google or
                      'reddit_deal_renewal_projections' in google)
        assert has_reddit

    def test_advance_perplexity_triangle_still_present(self):
        """The Advance-Reddit-Perplexity triangle should still be documented
        in the Google entity's reddit_perplexity_litigation section."""
        data = load_competitor_entities()
        google = data['entities']['google']
        assert 'reddit_perplexity_litigation' in google
        triangle = google['reddit_perplexity_litigation'].get(
            'advance_conde_nast_perplexity_triangle', '')
        assert 'Advance' in triangle or 'Condé Nast' in triangle or 'Conde Nast' in triangle

    def test_source_urls_present(self):
        """All findings must have source URLs."""
        data = load_competitor_entities()
        section = data['advance_dual_asset_monetization']
        assert 'source_urls' in section
        assert len(section['source_urls']) >= 5
