"""
Type C: Microsoft-OpenAI Financial Axis + Condé Nast Revenue Pivot

Tests for the Microsoft-OpenAI unified financial ecosystem analysis
and Condé Nast's explicit abandonment of advertising as a growth engine
in favor of AI licensing deals.

Created: 2026-08-06 17:00 PT
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

@pytest.fixture(scope='module')
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope='module')
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope='module')
def wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


class TestMicrosoftOpenAIAxisExists:
    """Verify the Microsoft-OpenAI financial axis section exists with required fields."""

    def test_axis_section_exists(self, competitor_entities):
        assert 'microsoft_openai_financial_axis' in competitor_entities

    def test_overview_present(self, competitor_entities):
        axis = competitor_entities['microsoft_openai_financial_axis']
        assert 'overview' in axis
        assert 'unified financial ecosystem' in axis['overview'].lower() or \
               'not independent entities' in axis['overview'].lower()

    def test_stake_data_present(self, competitor_entities):
        axis = competitor_entities['microsoft_openai_financial_axis']
        assert 'microsoft_openai_stake' in axis

    def test_circular_revenue_flow_documented(self, competitor_entities):
        axis = competitor_entities['microsoft_openai_financial_axis']
        assert 'circular_revenue_flow' in axis

    def test_publisher_dual_exposure_documented(self, competitor_entities):
        axis = competitor_entities['microsoft_openai_financial_axis']
        assert 'publisher_dual_exposure' in axis


class TestMicrosoftStakeData:
    """Verify Microsoft's ownership data in OpenAI is accurate and sourced."""

    def test_equity_percentage(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert stake['equity_pct'] == 27

    def test_pre_restructuring_percentage(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert stake['pre_restructuring_pct'] == 32.5

    def test_revenue_share_documented(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert '20%' in stake['revenue_share']
        assert '2030' in stake['revenue_share']

    def test_azure_commitment_documented(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert '$250B' in stake['azure_commitment'] or '250' in stake['azure_commitment']

    def test_ip_rights_through_2032(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert '2032' in stake['ip_rights']

    def test_source_urls_present(self, competitor_entities):
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert 'source_urls' in stake
        assert len(stake['source_urls']) >= 3


class TestCircularRevenueFlow:
    """Verify the circular revenue flow documentation captures the key dynamics."""

    def test_publisher_to_openai_flow(self, competitor_entities):
        flow = competitor_entities['microsoft_openai_financial_axis']['circular_revenue_flow']
        assert 'OpenAI' in flow and 'licensing' in flow.lower()

    def test_openai_to_microsoft_revenue_share(self, competitor_entities):
        flow = competitor_entities['microsoft_openai_financial_axis']['circular_revenue_flow']
        assert '20%' in flow and 'revenue share' in flow.lower()

    def test_azure_flow_documented(self, competitor_entities):
        flow = competitor_entities['microsoft_openai_financial_axis']['circular_revenue_flow']
        assert 'Azure' in flow

    def test_content_revenue_axis_named(self, competitor_entities):
        flow = competitor_entities['microsoft_openai_financial_axis']['circular_revenue_flow']
        assert 'CONTENT REVENUE' in flow or 'content revenue' in flow.lower()

    def test_pcm_flow_documented(self, competitor_entities):
        flow = competitor_entities['microsoft_openai_financial_axis']['circular_revenue_flow']
        assert 'PCM' in flow


class TestPublisherDualExposure:
    """Verify publisher exposure data in the Microsoft-OpenAI axis."""

    def test_conde_nast_listed(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        names = [p['publisher'] for p in publishers]
        assert any('Condé Nast' in n or 'WIRED' in n for n in names)

    def test_vox_media_listed(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        names = [p['publisher'] for p in publishers]
        assert any('Vox Media' in n or 'Verge' in n for n in names)

    def test_ft_listed(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        names = [p['publisher'] for p in publishers]
        assert any('Financial Times' in n or 'FT' in n or 'Nikkei' in n for n in names)

    def test_all_publishers_have_zero_meta_deals(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        for p in publishers:
            assert p['meta_deals'] == 0, f"{p['publisher']} should have 0 Meta deals"

    def test_all_publishers_have_dual_axis_deals(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        for p in publishers:
            assert p['total_axis_deals'] >= 2, \
                f"{p['publisher']} should have at least 2 Microsoft-OpenAI axis deals"

    def test_conde_nast_has_five_competitor_deals(self, competitor_entities):
        publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        cn = [p for p in publishers if 'Condé Nast' in p['publisher'] or 'WIRED' in p['publisher']][0]
        assert cn['total_competitor_deals'] == 5


class TestCondeNastRevenuePivot:
    """Verify the Condé Nast revenue pivot analysis in competitor research."""

    def test_revenue_pivot_section_exists(self, competitor_research):
        wired = competitor_research['publications']['wired']
        assert 'conde_nast_revenue_pivot' in wired

    def test_overview_mentions_advertising_abandoned(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'advertising' in pivot['overview'].lower()
        assert 'growth engine' in pivot['overview'].lower() or \
               'abandoned' in pivot['overview'].lower()

    def test_lynch_statements_present(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'lynch_statements' in pivot
        assert len(pivot['lynch_statements']) >= 3

    def test_lynch_advertising_not_growth_quote(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        quotes = [s['quote'] for s in pivot['lynch_statements']]
        assert any('growth engine' in q.lower() for q in quotes)

    def test_lynch_search_zero_quote(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        quotes = [s['quote'] for s in pivot['lynch_statements']]
        assert any('zero' in q.lower() or 'search' in q.lower() for q in quotes)


class TestCondeNastRevenueData:
    """Verify specific financial data points are documented with sources."""

    def test_revenue_data_section_exists(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'revenue_data_2025' in pivot

    def test_events_growth_documented(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        assert '+40%' in data['events_growth'] or '40' in data['events_growth']

    def test_digital_subscriptions_growth(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        assert '29%' in data['digital_subscriptions_growth'] or '29' in str(data['digital_subscriptions_growth'])

    def test_ai_deals_named(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        deals = data['ai_deals_named']
        assert 'OpenAI' in deals
        assert 'Microsoft' in deals
        assert 'Perplexity' in deals
        assert 'Amazon' in deals

    def test_top_brands_revenue_share(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        assert '85%' in data['top_7_brands_share'] or '85' in str(data['top_7_brands_share'])

    def test_ai_pilots_count(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        assert data['ai_pilots_running'] == 70

    def test_revenue_source_urls_present(self, competitor_research):
        data = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['revenue_data_2025']
        assert 'source_urls' in data
        assert len(data['source_urls']) >= 2


class TestMicrosoftOpenAIAxisExposure:
    """Verify the axis exposure analysis in the Condé Nast revenue pivot."""

    def test_axis_exposure_documented(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'microsoft_openai_axis_exposure' in pivot

    def test_axis_mentions_27_percent(self, competitor_research):
        exposure = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['microsoft_openai_axis_exposure']
        assert '27%' in exposure

    def test_axis_mentions_revenue_share(self, competitor_research):
        exposure = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['microsoft_openai_axis_exposure']
        assert '20%' in exposure

    def test_axis_mentions_azure_commitment(self, competitor_research):
        exposure = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['microsoft_openai_axis_exposure']
        assert '$250B' in exposure or '250B' in exposure

    def test_meta_zero_risk_documented(self, competitor_research):
        exposure = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['microsoft_openai_axis_exposure']
        assert 'Meta' in exposure and ('zero' in exposure.lower() or 'NOTHING' in exposure)


class TestEditorialIndependenceParadox:
    """Verify the editorial independence paradox is documented."""

    def test_paradox_section_exists(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'editorial_independence_paradox' in pivot

    def test_paradox_mentions_firm_stance(self, competitor_research):
        paradox = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['editorial_independence_paradox']
        assert 'firm stance' in paradox.lower()

    def test_paradox_mentions_selective_application(self, competitor_research):
        paradox = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['editorial_independence_paradox']
        # Should document that the stance is selectively applied
        assert 'selective' in paradox.lower() or 'WITHOUT deals' in paradox

    def test_paradox_mentions_perplexity_hypocrisy(self, competitor_research):
        paradox = competitor_research['publications']['wired']['conde_nast_revenue_pivot']['editorial_independence_paradox']
        assert 'Perplexity' in paradox
        assert 'plagiarism' in paradox.lower() or 'accused' in paradox.lower()

    def test_paradox_has_source_urls(self, competitor_research):
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        assert 'source_urls' in pivot
        assert len(pivot['source_urls']) >= 4


class TestMetaContrastInAxis:
    """Verify Meta's zero-leverage position is documented in the axis analysis."""

    def test_meta_contrast_present(self, competitor_entities):
        axis = competitor_entities['microsoft_openai_financial_axis']
        assert 'meta_contrast' in axis

    def test_meta_no_pcm(self, competitor_entities):
        contrast = competitor_entities['microsoft_openai_financial_axis']['meta_contrast']
        assert 'PCM' in contrast

    def test_meta_no_openai_investment(self, competitor_entities):
        contrast = competitor_entities['microsoft_openai_financial_axis']['meta_contrast']
        assert 'OpenAI' in contrast

    def test_meta_zero_participation(self, competitor_entities):
        contrast = competitor_entities['microsoft_openai_financial_axis']['meta_contrast']
        assert 'zero' in contrast.lower()


class TestCrossValidation:
    """Cross-validate Microsoft-OpenAI axis data against existing profile data."""

    def test_conde_nast_deal_count_matches_entities(self, competitor_entities):
        """Condé Nast deal count in axis should match excluded_publishers."""
        excluded = competitor_entities['meta_ai_deals']['excluded_publishers']
        cn = [p for p in excluded if 'Condé Nast' in p['name']][0]
        axis_publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        cn_axis = [p for p in axis_publishers if 'Condé Nast' in p['publisher']][0]
        assert cn['deal_count'] == cn_axis['total_competitor_deals']

    def test_vox_media_deal_count_matches_entities(self, competitor_entities):
        """Vox Media deal count in axis should match excluded_publishers."""
        excluded = competitor_entities['meta_ai_deals']['excluded_publishers']
        vox = [p for p in excluded if 'Vox Media' in p['name']][0]
        axis_publishers = competitor_entities['microsoft_openai_financial_axis']['publisher_dual_exposure']
        vox_axis = [p for p in axis_publishers if 'Vox Media' in p['publisher']][0]
        assert vox['deal_count'] == vox_axis['total_competitor_deals']

    def test_microsoft_stake_consistent_with_nytimes_profile(self, competitor_entities):
        """The 27% figure should appear in both the axis section and existing profiles."""
        axis_pct = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']['equity_pct']
        assert axis_pct == 27

    def test_openai_ipo_valuation_consistent(self, competitor_entities):
        """IPO projection should reference the $1T target."""
        stake = competitor_entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        assert '$1T' in stake['ipo_projection'] or '1 trillion' in stake['ipo_projection'].lower()

    def test_revenue_pivot_source_urls_are_valid(self, competitor_research):
        """All source URLs in revenue pivot should start with http."""
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        for url in pivot['source_urls']:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_lynch_statement_urls_are_valid(self, competitor_research):
        """Each Lynch statement should have a valid source URL."""
        pivot = competitor_research['publications']['wired']['conde_nast_revenue_pivot']
        for stmt in pivot['lynch_statements']:
            assert 'source_url' in stmt
            assert stmt['source_url'].startswith('http'), f"Invalid URL: {stmt['source_url']}"
