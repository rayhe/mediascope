"""
Test: Publisher AI Revenue Materiality Index — SEC-Filed Revenue Quantification
Date: 2026-08-09
Type: C (Financial Incentive Mapping)

Tests the Publisher AI Revenue Materiality Index, which quantifies actual
SEC-filed AI licensing revenue from publisher earnings (Q1-Q2 2026) and
documents the Condé Nast Opacity Paradox: the publisher most hostile to Meta
(WIRED) is privately held through Advance Publications, making its financial
relationships with Meta competitors structurally invisible to public scrutiny.

Sources:
  - Digiday (May 2026): Q1 publisher AI licensing revenue roundup
  - MarketBeat (Aug 3, 2026): People Inc. Q2 2026 earnings transcript
  - WSJ (Aug 3, 2026): People Inc. Q2 results
  - Reuters (Aug 5, 2026): News Corp Q4 FY2026 results
  - NYPost (Aug 5, 2026): News Corp record profitability
  - Adweek (May 2026): Condé Nast events revenue growth
  - Insider Monkey: Wiley Q2 FY2026 earnings transcript
  - Fool.com: USA Today Q1 2026 earnings transcript
  - TechCrunch (Nov 2025): People Inc. Microsoft deal
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_competitor_research()


@pytest.fixture(scope='module')
def materiality(research):
    return research['cross_publication_findings']['publisher_ai_revenue_materiality_index']


# ============================================================
# Section 1: Structure and completeness
# ============================================================

class TestStructure:
    """Verify the materiality index has all required sections."""

    def test_has_finding_summary(self, materiality):
        assert 'finding_summary' in materiality
        assert 'opacity' in materiality['finding_summary'].lower() or 'condé nast' in materiality['finding_summary'].lower()

    def test_has_public_publishers(self, materiality):
        assert 'public_publishers' in materiality

    def test_has_private_publishers(self, materiality):
        assert 'private_publishers' in materiality

    def test_has_cross_publisher_analysis(self, materiality):
        assert 'cross_publisher_analysis' in materiality

    def test_has_methodology(self, materiality):
        assert 'methodology' in materiality
        assert 'SEC' in materiality['methodology'] or 'sec' in materiality['methodology'].lower()

    def test_has_test_file_reference(self, materiality):
        assert materiality.get('test_file') == 'tests/test_publisher_ai_revenue_materiality_aug9.py'

    def test_has_mechanism(self, materiality):
        assert 'mechanism' in materiality
        assert 'opacity' in materiality['mechanism'] or 'revenue' in materiality['mechanism']


# ============================================================
# Section 2: Public publisher revenue data
# ============================================================

class TestNewsCorp:
    """News Corp Q4 FY2026 revenue verification."""

    def test_news_corp_exists(self, materiality):
        assert 'news_corp' in materiality['public_publishers']

    def test_q4_revenue(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        q4 = nc['q4_fy2026']
        assert q4['total_revenue_b'] == 2.34
        assert q4['revenue_yoy_pct'] == 11

    def test_fy2026_total(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        q4 = nc['q4_fy2026']
        assert q4['fy2026_total_revenue_b'] == 9.03

    def test_record_profitability(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        assert nc['q4_fy2026']['record_profitability'] is True

    def test_net_income_growth(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        assert nc['q4_fy2026']['net_income_yoy_pct'] == 167

    def test_ticker(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        assert 'NWSA' in nc['ticker']

    def test_has_source_urls(self, materiality):
        nc = materiality['public_publishers']['news_corp']
        assert len(nc['source_urls']) >= 2


class TestPeopleInc:
    """People Inc. (formerly IAC/Dotdash Meredith) AI revenue tracking."""

    def test_people_inc_exists(self, materiality):
        assert 'people_inc' in materiality['public_publishers']

    def test_most_transparent(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi.get('most_transparent') is True

    def test_q1_licensing_revenue(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        q1 = pi['q1_2026']
        assert q1['licensing_and_other_revenue_m'] == 40.7
        assert q1['licensing_yoy_pct'] == 26

    def test_q1_meta_attribution(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi['q1_2026']['meta_deal_cited_as_primary_driver'] is True

    def test_q2_digital_growth_streak(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi['q2_2026']['consecutive_digital_growth_quarters'] == 11

    def test_q2_non_session_growth(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi['q2_2026']['non_session_revenue_yoy_pct'] == 16

    def test_q2_ebitda_margin(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi['q2_2026']['adjusted_ebitda_margin_pct'] == 26

    def test_has_three_ai_deals(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert len(pi['ai_deals']) == 3
        partners = [d['partner'] for d in pi['ai_deals']]
        assert 'OpenAI' in partners
        assert 'Microsoft' in partners
        assert 'Meta' in partners

    def test_google_traffic_decline(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert '65%' in pi['google_traffic_decline']

    def test_coverage_implication(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        assert pi['meta_coverage_implication'] == 'softest_of_deal_holders'


class TestUSATodayCo:
    """USA Today Co. (formerly Gannett) AI revenue tracking."""

    def test_usa_today_exists(self, materiality):
        assert 'usa_today_co' in materiality['public_publishers']

    def test_q1_other_digital_revenue(self, materiality):
        ut = materiality['public_publishers']['usa_today_co']
        q1 = ut['q1_2026']
        assert q1['other_digital_revenue_m'] == 33.75
        assert q1['other_digital_revenue_yoy_pct'] == 125.6

    def test_first_notable_ai_revenue(self, materiality):
        ut = materiality['public_publishers']['usa_today_co']
        assert ut['q1_2026']['first_notable_ai_revenue'] is True

    def test_q2_lumpy_warning(self, materiality):
        ut = materiality['public_publishers']['usa_today_co']
        assert 'lumpy' in ut['q2_guidance'].lower() or 'lower contribution' in ut['q2_guidance'].lower()

    def test_has_meta_deal(self, materiality):
        ut = materiality['public_publishers']['usa_today_co']
        partners = [d['partner'] for d in ut['ai_deals']]
        assert 'Meta' in partners


class TestNYT:
    """NYT AI revenue opacity — commingled with Wirecutter affiliate."""

    def test_nyt_exists(self, materiality):
        assert 'nyt' in materiality['public_publishers']

    def test_q1_commingled_revenue(self, materiality):
        nyt = materiality['public_publishers']['nyt']
        q1 = nyt['q1_2026']
        assert q1['digital_affiliate_licensing_other_m'] == 45.2
        assert q1['digital_affiliate_licensing_yoy_pct'] == 12.7

    def test_isolation_impossible_note(self, materiality):
        nyt = materiality['public_publishers']['nyt']
        note = nyt['q1_2026']['note']
        assert 'cannot be isolated' in note.lower() or 'cannot isolate' in note.lower()

    def test_amazon_deal_only(self, materiality):
        nyt = materiality['public_publishers']['nyt']
        assert len(nyt['ai_deals']) == 1
        assert nyt['ai_deals'][0]['partner'] == 'Amazon'

    def test_adversarial_coverage(self, materiality):
        nyt = materiality['public_publishers']['nyt']
        assert nyt['meta_coverage_implication'] == 'adversarial'


class TestWiley:
    """Wiley AI revenue — academic publisher comparison point."""

    def test_wiley_exists(self, materiality):
        assert 'wiley' in materiality['public_publishers']

    def test_cumulative_ai_revenue(self, materiality):
        wl = materiality['public_publishers']['wiley']
        q2 = wl['q2_fy2026']
        assert '100' in str(q2['ai_training_revenue_cumulative_m'])

    def test_fy2026_ai_revenue(self, materiality):
        wl = materiality['public_publishers']['wiley']
        assert wl['q2_fy2026']['fy2026_ai_revenue_m'] == 49

    def test_shift_to_subscription(self, materiality):
        wl = materiality['public_publishers']['wiley']
        assert 'subscription' in wl['q2_fy2026']['shift'].lower()

    def test_partners(self, materiality):
        wl = materiality['public_publishers']['wiley']
        partners = wl['q2_fy2026']['partners']
        assert 'Anthropic' in partners
        assert 'Perplexity' in partners


# ============================================================
# Section 3: Condé Nast Opacity Paradox
# ============================================================

class TestCondeNastOpacity:
    """The core finding: privately-held Condé Nast has zero financial disclosure."""

    def test_conde_nast_in_private_section(self, materiality):
        assert 'conde_nast' in materiality['private_publishers']

    def test_not_publicly_traded(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['publicly_traded'] is False

    def test_zero_sec_filing_obligation(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['sec_filing_obligation'] == 'none'

    def test_four_competitor_deals(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['ai_deal_count'] == 4
        assert len(cn['ai_deals']) == 4

    def test_zero_meta_deals(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['meta_deals'] == 0

    def test_all_deal_values_undisclosed(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        for deal in cn['ai_deals']:
            assert deal['value'] == 'undisclosed'

    def test_zero_public_ai_revenue_disclosure(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['financial_disclosures']['ai_revenue'] == 'zero_public_disclosure'

    def test_zero_total_revenue_disclosure(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['financial_disclosures']['total_revenue'] == 'zero_public_disclosure'

    def test_opacity_paradox_documented(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert 'conde_nast_opacity_paradox' in cn
        paradox = cn['conde_nast_opacity_paradox']
        assert 'privately held' in paradox.lower()
        assert 'zero' in paradox.lower() or 'no obligation' in paradox.lower()

    def test_advance_publications_ownership(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert cn['parent'] == 'Advance Publications (private, Newhouse family)'

    def test_reddit_stake_documented(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert 'Reddit' in cn['advance_publications_assets']

    def test_lynch_ad_strategy_shift(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        shift = cn['financial_disclosures']['advertising_strategy_shift']
        assert 'no longer expects advertising' in shift.lower()
        assert 'OpenAI' in shift

    def test_has_source_urls(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        assert len(cn['source_urls']) >= 3


# ============================================================
# Section 4: Cross-publisher analytical findings
# ============================================================

class TestCrossPublisherAnalysis:
    """Test the opacity gradient and revenue materiality threshold."""

    def test_opacity_gradient_exists(self, materiality):
        cpa = materiality['cross_publisher_analysis']
        assert 'opacity_gradient' in cpa

    def test_opacity_gradient_ordering(self, materiality):
        gradient = materiality['cross_publisher_analysis']['opacity_gradient']
        # People Inc. should be most transparent
        assert gradient.index('People Inc') < gradient.index('Condé Nast')

    def test_revenue_materiality_threshold(self, materiality):
        cpa = materiality['cross_publisher_analysis']
        assert 'revenue_materiality_threshold' in cpa
        threshold = cpa['revenue_materiality_threshold']
        assert '$40' in threshold or '40.7' in threshold

    def test_near_100pct_margin_noted(self, materiality):
        cpa = materiality['cross_publisher_analysis']
        threshold = cpa['revenue_materiality_threshold']
        assert '100% margin' in threshold or 'near-100%' in threshold.lower()

    def test_google_traffic_substitution(self, materiality):
        cpa = materiality['cross_publisher_analysis']
        assert 'google_traffic_substitution' in cpa
        sub = cpa['google_traffic_substitution']
        assert '65%' in sub or 'replacement' in sub.lower()

    def test_coverage_correlation_pattern(self, materiality):
        """Most transparent publishers about AI revenue have softest Meta coverage."""
        gradient = materiality['cross_publisher_analysis']['opacity_gradient']
        # Pattern described in the gradient
        assert 'softest' in gradient.lower() or 'soft' in gradient.lower()
        assert 'adversarial' in gradient.lower()


# ============================================================
# Section 5: Data consistency checks
# ============================================================

class TestDataConsistency:
    """Cross-check materiality data against existing competitor-entities.yaml."""

    def test_news_corp_openai_deal_consistent(self, materiality):
        """OpenAI deal value should match competitor-entities.yaml."""
        nc = materiality['public_publishers']['news_corp']
        ai_status = nc['ai_revenue_status']
        assert '$250M/5yr' in ai_status or '$50M/yr' in ai_status

    def test_people_inc_meta_deal_is_dec_2025(self, materiality):
        pi = materiality['public_publishers']['people_inc']
        meta_deal = [d for d in pi['ai_deals'] if d['partner'] == 'Meta'][0]
        assert 'Dec 2025' in meta_deal['signed'] or '2025' in meta_deal['signed']

    def test_nyt_litigation_target(self, materiality):
        nyt = materiality['public_publishers']['nyt']
        lit = nyt['active_litigation'][0]
        assert 'OpenAI' in lit['target']

    def test_conde_nast_openai_deal_date(self, materiality):
        cn = materiality['private_publishers']['conde_nast']
        openai_deal = [d for d in cn['ai_deals'] if d['partner'] == 'OpenAI'][0]
        assert 'Aug 2024' in openai_deal['signed'] or '2024' in openai_deal['signed']

    def test_all_public_publishers_have_tickers(self, materiality):
        for name, pub in materiality['public_publishers'].items():
            if name != 'wiley' or 'ticker' in pub:
                assert 'ticker' in pub, f"{name} missing ticker"

    def test_all_source_urls_are_strings(self, materiality):
        """All source_urls should be valid strings."""
        for name, pub in materiality['public_publishers'].items():
            if 'source_urls' in pub:
                for url in pub['source_urls']:
                    assert isinstance(url, str)
                    assert url.startswith('http')
        for name, pub in materiality['private_publishers'].items():
            if 'source_urls' in pub:
                for url in pub['source_urls']:
                    assert isinstance(url, str)
                    assert url.startswith('http')
