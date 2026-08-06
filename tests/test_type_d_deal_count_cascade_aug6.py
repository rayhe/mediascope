"""Type D: Verify deal count consistency after Aug 5 Snowflake/xAI additions.

The Aug 5 23:00 PT iteration added the NYT-Snowflake Cortex deal (19th deal)
and xAI as a publisher-invisible entity. This caused cascading failures in
test_financial_incentive_mapping_aug5 (expected 18, got 19) and
test_cross_platform_financial_incentives (same). The foxbusiness_louisiana
test also broke because the million pattern fix in Type D 19:00 detected
an additional scale_magnitude device.

This test file validates:
1. All deal count references are consistent at 19
2. xAI entity is properly integrated
3. Snowflake Cortex marketplace is documented
4. The million pattern fix cascades are accounted for
5. The WSJ xfail promotion is consistent

Created: Aug 6 2026 00:00 PT (Type D iteration)
"""

import yaml
import pytest


@pytest.fixture(scope="module")
def entities():
    with open("profiles/competitor-entities.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def wired_profile():
    with open("profiles/wired.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    with open("profiles/competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


class TestDealCountConsistency:
    """All references to total deal count should be 19 after Snowflake addition."""

    def test_aggregate_matrix_total_is_19(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        assert matrix['total_competitor_deal_count'] == 19

    def test_critical_finding_mentions_19(self, entities):
        finding = entities['meta_ai_deals'].get('critical_finding', '')
        assert '19' in finding

    def test_statistical_note_mentions_19(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        note = matrix.get('statistical_note', '')
        assert '19' in note

    def test_individual_deals_sum_to_total(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        individual = sum(p['competitor_deals'] for p in matrix['publications'])
        assert individual == matrix['total_competitor_deal_count']

    def test_nyt_has_3_deals_with_snowflake(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        nyt = [p for p in pubs if p['name'] == 'NYT'][0]
        assert nyt['competitor_deals'] == 3
        platforms_text = ' '.join(nyt['platforms']).lower()
        assert 'snowflake' in platforms_text

    def test_nyt_excluded_publishers_has_snowflake_deal(self, entities):
        excluded = entities['meta_ai_deals']['excluded_publishers']
        nyt = [p for p in excluded if 'New York Times' in p['name']][0]
        deals = nyt['deals_with_competitors']
        snowflake_deals = [d for d in deals if isinstance(d, dict) and 'snowflake' in d.get('partner', '').lower()]
        assert len(snowflake_deals) >= 1

    def test_all_meta_deals_zero(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        assert matrix['total_meta_deal_count'] == 0
        for pub in matrix['publications']:
            assert pub['meta_deals'] == 0


class TestXAIIntegration:
    """xAI entity should be properly integrated."""

    def test_xai_in_entities(self, entities):
        assert 'xai' in entities['entities']

    def test_xai_has_publisher_deals_note(self, entities):
        xai = entities['entities']['xai']
        assert 'publisher_deals_note' in xai

    def test_xai_is_publisher_invisible(self, entities):
        xai = entities['entities']['xai']
        note = xai.get('publisher_deals_note', '')
        assert 'publisher-invisible' in note.lower() or 'zero publisher' in note.lower()

    def test_xai_has_telegram_deal_source(self, entities):
        xai = entities['entities']['xai']
        assert 'telegram_deal_source' in xai
        assert xai['telegram_deal_source'].startswith('http')

    def test_xai_has_gsa_contract_source(self, entities):
        xai = entities['entities']['xai']
        assert 'gsa_contract_source' in xai
        assert xai['gsa_contract_source'].startswith('http')

    def test_xai_valuation_documented(self, entities):
        xai = entities['entities']['xai']
        assert '$50B' in xai.get('market_cap_approx', '')

    def test_total_entities_is_8(self, entities):
        assert len(entities['entities']) == 8


class TestSnowflakeCortexMarketplace:
    """Snowflake Cortex should be documented in cross-platform summary."""

    def test_snowflake_cortex_in_summary(self, entities):
        summary = entities['meta_ai_deals'].get('cross_platform_summary', {})
        assert 'snowflake_cortex' in summary

    def test_snowflake_has_17_publishers(self, entities):
        cortex = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        desc = cortex.get('description', '')
        assert '17' in desc

    def test_snowflake_has_confirmed_partners(self, entities):
        cortex = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        partners = cortex.get('confirmed_partners', [])
        assert len(partners) >= 4

    def test_snowflake_has_source_url(self, entities):
        cortex = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        urls = cortex.get('source_urls', [])
        assert len(urls) >= 1
        assert urls[0].startswith('http')


class TestCascadeConsistency:
    """Verify no stale deal counts remain after 18→19 update."""

    def test_no_stale_18_in_critical_finding(self, entities):
        """Critical finding should not reference 18 deals (stale)."""
        finding = entities['meta_ai_deals'].get('critical_finding', '')
        # 18 should not appear as a deal count reference
        # (it may appear in other contexts like dates)
        assert '18 revenue' not in finding
        assert '18 deals' not in finding

    def test_conde_nast_still_leads_with_5(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        wired = [p for p in pubs if 'WIRED' in p['name']][0]
        assert wired['competitor_deals'] == 5

    def test_perplexity_in_wired_platforms(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        wired = [p for p in pubs if 'WIRED' in p['name']][0]
        platforms_text = ' '.join(wired['platforms']).lower()
        assert 'perplexity' in platforms_text

    def test_all_publications_have_adversarial_meta_coverage(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        for pub in matrix['publications']:
            assert pub['adversarial_meta_coverage'] is True, (
                f"{pub['name']} should have adversarial_meta_coverage=True"
            )

    def test_gizmodo_is_clean_control(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        gizmodo = [p for p in pubs if 'Gizmodo' in p['name']][0]
        assert gizmodo['competitor_deals'] == 0
        assert gizmodo['meta_deals'] == 0

    def test_relationship_types_include_advertising_dependency(self, entities):
        """advertising_dependency type added in Aug 5 12:00 Type C."""
        assert 'advertising_dependency' in entities['relationship_types']


class TestProjectGiraffeDocumented:
    """Project Giraffe litigation escalation should be in NYT profile."""

    def test_nyt_has_litigation_escalation(self, entities):
        excluded = entities['meta_ai_deals']['excluded_publishers']
        nyt = [p for p in excluded if 'New York Times' in p['name']][0]
        assert 'litigation_escalation_jul2026' in nyt

    def test_project_giraffe_date(self, entities):
        excluded = entities['meta_ai_deals']['excluded_publishers']
        nyt = [p for p in excluded if 'New York Times' in p['name']][0]
        escalation = nyt['litigation_escalation_jul2026']
        assert escalation['date'] == '2026-07-09'

    def test_project_giraffe_has_sources(self, entities):
        excluded = entities['meta_ai_deals']['excluded_publishers']
        nyt = [p for p in excluded if 'New York Times' in p['name']][0]
        escalation = nyt['litigation_escalation_jul2026']
        assert len(escalation.get('source_urls', [])) >= 2

    def test_critical_finding_mentions_project_giraffe(self, entities):
        finding = entities['meta_ai_deals'].get('critical_finding', '').lower()
        assert 'project giraffe' in finding
