"""
Type C: Microsoft Septuple Publisher Leverage — Entity Profile

Microsoft has SEVEN distinct financial relationship mechanisms with
publishers, more than any other tech company in the MediaScope dataset.
This test verifies the Microsoft entity profile captures all seven
layers, the dual AI lab investment paradox (OpenAI + Anthropic), and
the FY26 Q4 earnings data.

KEY FINDING: Microsoft is the ONLY company that operates as both a
BUYER of publisher content AND the MARKETPLACE OPERATOR through which
publishers sell to other AI builders. It also simultaneously invests in
the AI lab with the MOST publisher deals (OpenAI) and one with ZERO
deals (Anthropic), profiting regardless of which model prevails.

Created: 2026-08-07 13:00 PT
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
def microsoft(competitor_entities):
    return competitor_entities['entities']['microsoft']


class TestMicrosoftEntityExists:
    """Verify Microsoft top-level entity exists with standard fields."""

    def test_entity_in_entities_section(self, competitor_entities):
        assert 'microsoft' in competitor_entities['entities']

    def test_display_name(self, microsoft):
        assert microsoft['display_name'] == 'Microsoft'

    def test_category_big_tech(self, microsoft):
        assert microsoft['category'] == 'big_tech'

    def test_ceo_satya_nadella(self, microsoft):
        assert microsoft['ceo'] == 'Satya Nadella'

    def test_market_cap_present(self, microsoft):
        assert 'market_cap_approx' in microsoft

    def test_aliases_include_key_brands(self, microsoft):
        aliases = microsoft['aliases']
        assert 'Azure' in aliases
        assert 'Copilot' in aliases
        assert 'LinkedIn' in aliases

    def test_regex_pattern_present(self, microsoft):
        assert 'regex' in microsoft


class TestFY26Q4Earnings:
    """Verify FY26 Q4 earnings data (reported Jul 29, 2026)."""

    def test_earnings_section_exists(self, microsoft):
        assert 'fy26_q4_earnings' in microsoft

    def test_report_date(self, microsoft):
        assert microsoft['fy26_q4_earnings']['report_date'] == '2026-07-29'

    def test_total_revenue(self, microsoft):
        assert microsoft['fy26_q4_earnings']['total_revenue_b'] == 90.0

    def test_revenue_yoy_growth(self, microsoft):
        assert microsoft['fy26_q4_earnings']['total_revenue_yoy_pct'] == 18

    def test_operating_income(self, microsoft):
        assert microsoft['fy26_q4_earnings']['operating_income_b'] == 40.6

    def test_azure_growth(self, microsoft):
        assert microsoft['fy26_q4_earnings']['azure_revenue_yoy_pct'] == 43

    def test_search_ad_growth(self, microsoft):
        assert microsoft['fy26_q4_earnings']['search_ad_rev_ex_tac_yoy_pct'] == 10

    def test_linkedin_growth(self, microsoft):
        assert microsoft['fy26_q4_earnings']['linkedin_revenue_yoy_pct'] == 12

    def test_anthropic_q4_gain(self, microsoft):
        assert microsoft['fy26_q4_earnings']['anthropic_investment_q4_gain_b'] == 3.2

    def test_openai_q4_writedown(self, microsoft):
        assert microsoft['fy26_q4_earnings']['openai_investment_q4_impact_m'] == -600

    def test_fy26_total_revenue(self, microsoft):
        assert microsoft['fy26_q4_earnings']['fy26_total_revenue_b'] == 331.8

    def test_azure_first_100b(self, microsoft):
        assert microsoft['fy26_q4_earnings']['azure_fy26_total_over_100b'] is True

    def test_bing_1b_mau(self, microsoft):
        bing_mau = microsoft['fy26_q4_earnings']['bing_mau_milestone']
        assert '1B' in str(bing_mau)

    def test_ai_business_arr(self, microsoft):
        assert microsoft['fy26_q4_earnings']['ai_business_arr_b'] == 37

    def test_source_urls_present(self, microsoft):
        assert len(microsoft['fy26_q4_earnings']['source_urls']) >= 2


class TestSeptupleLeverage:
    """Verify all seven layers of Microsoft's publisher leverage."""

    def test_septuple_section_exists(self, microsoft):
        assert 'septuple_publisher_leverage' in microsoft

    def test_exactly_seven_layers(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        assert len(layers) == 7

    def test_overview_mentions_seven(self, microsoft):
        overview = microsoft['septuple_publisher_leverage']['overview']
        assert 'SEVEN' in overview

    def test_overview_mentions_amazon_comparison(self, microsoft):
        overview = microsoft['septuple_publisher_leverage']['overview']
        assert 'Amazon' in overview and 'six' in overview.lower()


class TestLayer1OpenAIAxis:
    """Verify Layer 1: OpenAI investment axis."""

    def test_openai_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'openai_investment_axis' in names

    def test_openai_stake_mentioned(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'openai_investment_axis'][0]
        assert '27%' in layer['detail']
        assert '$13B' in layer['detail']

    def test_revenue_share_mentioned(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'openai_investment_axis'][0]
        assert '20%' in layer['detail']
        assert '2030' in layer['detail']

    def test_azure_commitment_mentioned(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'openai_investment_axis'][0]
        assert '$250B' in layer['detail']


class TestLayer2AnthropicInvestment:
    """Verify Layer 2: Anthropic investment."""

    def test_anthropic_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'anthropic_investment' in names

    def test_anthropic_5b_invested(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert layer['invested_b'] == 5

    def test_anthropic_q4_gain(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert layer['q4_fy26_gain_b'] == 3.2

    def test_anthropic_azure_commitment(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert layer['azure_commitment_b'] == 30

    def test_anthropic_annual_spending(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert layer['annual_model_spending_m'] == 500

    def test_anthropic_zero_publisher_deals_noted(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert 'ZERO publisher content licensing deals' in layer['detail']

    def test_anthropic_source_urls(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'anthropic_investment'][0]
        assert len(layer['source_urls']) >= 3


class TestLayer3PCM:
    """Verify Layer 3: PCM marketplace operator role."""

    def test_pcm_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'pcm_marketplace_operator' in names

    def test_pcm_dual_role_documented(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'pcm_marketplace_operator'][0]
        assert 'platform operator' in layer['detail'].lower()
        assert 'buyer' in layer['detail'].lower() or 'demand' in layer['detail'].lower()

    def test_pcm_seven_publishers_listed(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'pcm_marketplace_operator'][0]
        detail = layer['detail']
        assert 'Condé Nast' in detail
        assert 'Hearst' in detail
        assert 'Vox Media' in detail


class TestLayer4CopilotDaily:
    """Verify Layer 4: Copilot Daily content partnerships."""

    def test_copilot_daily_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'copilot_daily_content' in names

    def test_copilot_daily_partners_listed(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'copilot_daily_content'][0]
        detail = layer['detail']
        assert 'Reuters' in detail
        assert 'Financial Times' in detail


class TestLayer5MSN:
    """Verify Layer 5: MSN/Start content licensing."""

    def test_msn_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'msn_start_licensing' in names

    def test_msn_oldest_relationship_noted(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'msn_start_licensing'][0]
        assert 'OLDEST' in layer['detail'] or 'oldest' in layer['detail'].lower()


class TestLayer6BingSearch:
    """Verify Layer 6: Bing search advertising."""

    def test_bing_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'bing_search_advertising' in names

    def test_bing_1b_mau_noted(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'bing_search_advertising'][0]
        assert '1B' in layer['detail'] or '1 billion' in layer['detail'].lower()


class TestLayer7Azure:
    """Verify Layer 7: Azure enterprise hosting."""

    def test_azure_layer_exists(self, microsoft):
        layers = microsoft['septuple_publisher_leverage']['layers']
        names = [l['name'] for l in layers]
        assert 'azure_enterprise_hosting' in names

    def test_azure_revenue_q4(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'azure_enterprise_hosting'][0]
        assert '$39.3B' in layer['detail']

    def test_azure_100b_milestone(self, microsoft):
        layer = [l for l in microsoft['septuple_publisher_leverage']['layers']
                 if l['name'] == 'azure_enterprise_hosting'][0]
        assert '$100B' in layer['detail'] or '100B' in layer['detail']


class TestMetaContrast:
    """Verify the Meta contrast is documented."""

    def test_meta_contrast_exists(self, microsoft):
        assert 'meta_contrast' in microsoft['septuple_publisher_leverage']

    def test_meta_one_mechanism(self, microsoft):
        contrast = microsoft['septuple_publisher_leverage']['meta_contrast']
        assert 'ONE' in contrast

    def test_seven_fold_noted(self, microsoft):
        contrast = microsoft['septuple_publisher_leverage']['meta_contrast']
        assert 'seven' in contrast.lower() or 'SEVEN' in contrast


class TestDualAILabParadox:
    """Verify the dual AI lab investment paradox is documented."""

    def test_paradox_section_exists(self, microsoft):
        assert 'dual_ai_lab_investment_paradox' in microsoft['septuple_publisher_leverage']

    def test_paradox_mentions_both_labs(self, microsoft):
        paradox = microsoft['septuple_publisher_leverage']['dual_ai_lab_investment_paradox']
        assert 'OpenAI' in paradox
        assert 'Anthropic' in paradox

    def test_paradox_mentions_q4_hedge(self, microsoft):
        paradox = microsoft['septuple_publisher_leverage']['dual_ai_lab_investment_paradox']
        assert '$600M' in paradox or '600' in paradox
        assert '$3.2B' in paradox or '3.2B' in paradox

    def test_paradox_mentions_wins_either_way(self, microsoft):
        paradox = microsoft['septuple_publisher_leverage']['dual_ai_lab_investment_paradox']
        assert 'wins either way' in paradox.lower() or \
               'regardless' in paradox.lower() or \
               'profits regardless' in paradox.lower()


class TestPublisherDealsNote:
    """Verify the publisher deals note covers MediaScope-profiled publications."""

    def test_publisher_deals_note_exists(self, microsoft):
        assert 'publisher_deals_note' in microsoft

    def test_five_of_seven_noted(self, microsoft):
        note = microsoft['publisher_deals_note']
        assert '5 of 7' in note

    def test_conde_nast_mentioned(self, microsoft):
        note = microsoft['publisher_deals_note']
        assert 'Condé Nast' in note

    def test_ft_mentioned(self, microsoft):
        note = microsoft['publisher_deals_note']
        assert 'FT' in note or 'Financial Times' in note

    def test_gizmodo_clean_control(self, microsoft):
        note = microsoft['publisher_deals_note']
        assert 'Gizmodo' in note
        assert 'clean control' in note.lower() or 'No relationship' in note
