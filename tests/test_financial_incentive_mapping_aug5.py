"""
Tests for financial incentive mapping findings (Type C iteration, Aug 5 2026).

Validates three new findings:
1. Perplexity hypocrisy arc: WIRED plagiarism accusation → C&D → Condé Nast deal
2. Anthropic absence from publisher content licensing deals ($1.5B author settlement only)
3. Google coercive Showcase→AI pilot structure (triple leverage)

Source URLs:
- Perplexity Comet Plus: https://ppc.land/conde-nast-ceo-calls-google-ai-a-death-blow-as-search-traffic-collapses/
- Adweek (Condé Nast deals confirmed): https://www.adweek.com/media/conde-nast-vasanth-williams-chief-product-technology-officer-microsoft-ai-licensing-pilot/
- VentureBeat (Perplexity plagiarism context): http://venturebeat.com/ai/perplexity-unveils-revenue-sharing-plan-for-publishers
- Anthropic settlement: https://www.pymnts.com/legal/2026/anthropic-historic-1-billion-dollar-copyright-settlement-gets-judge-ok/
- Google coercion (PYMNTS): https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/
- Google coercion (NY Post): https://nypost.com/2026/06/26/business/google-looks-to-bleed-publishers-with-new-ai-partnerships-that-would-cull-their-content/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def _get_conde_nast(entities):
    for pub in entities['meta_ai_deals']['excluded_publishers']:
        if 'Condé Nast' in pub['name']:
            return pub
    pytest.fail("Condé Nast not found")


def _get_perplexity_deal(entities):
    cn = _get_conde_nast(entities)
    deals = [d for d in cn['deals_with_competitors'] if 'perplexity' in d['partner'].lower()]
    assert len(deals) == 1, "Should have exactly one Perplexity deal"
    return deals[0]


# ===================================================================
# 1. Perplexity Hypocrisy Arc
# ===================================================================

class TestPerplexityHypocrisyArc:
    """WIRED accused Perplexity of plagiarism, Condé Nast sent C&D, then signed deal."""

    def test_perplexity_deal_exists(self, entities):
        deal = _get_perplexity_deal(entities)
        assert deal is not None

    def test_perplexity_deal_type_is_commercial(self, entities):
        deal = _get_perplexity_deal(entities)
        assert deal['type'] == 'commercial_partnership'

    def test_perplexity_deal_has_source_url(self, entities):
        deal = _get_perplexity_deal(entities)
        assert 'source_url' in deal
        assert len(deal['source_url']) > 10

    def test_perplexity_deal_mentions_comet_plus(self, entities):
        deal = _get_perplexity_deal(entities)
        scope = deal.get('scope', '').lower()
        assert 'comet' in scope

    def test_perplexity_deal_mentions_16_titles(self, entities):
        deal = _get_perplexity_deal(entities)
        scope = deal.get('scope', '').lower()
        assert '16' in scope

    def test_perplexity_deal_notes_document_hypocrisy(self, entities):
        deal = _get_perplexity_deal(entities)
        notes = deal.get('notes', '').lower()
        assert 'plagiarism' in notes

    def test_perplexity_deal_notes_mention_cease_and_desist(self, entities):
        deal = _get_perplexity_deal(entities)
        notes = deal.get('notes', '').lower()
        assert 'cease' in notes or 'c&d' in notes

    def test_perplexity_deal_date_is_oct_2025(self, entities):
        deal = _get_perplexity_deal(entities)
        assert '2025-10' in str(deal.get('date', ''))

    def test_research_documents_hypocrisy_arc(self, research):
        wired = research['publications']['wired']
        summary = wired.get('perplexity_coverage_summary', '').lower()
        assert 'plagiarism' in summary
        assert 'deal' in summary

    def test_research_has_comet_plus_source(self, research):
        wired = research['publications']['wired']
        assert 'perplexity_comet_plus_source' in wired

    def test_research_has_plagiarism_source(self, research):
        wired = research['publications']['wired']
        assert 'perplexity_plagiarism_source' in wired

    def test_deal_after_plagiarism_accusation(self, entities):
        """Deal (Oct 2025) was signed AFTER plagiarism accusation (Jun 2024)."""
        deal = _get_perplexity_deal(entities)
        date_str = str(deal.get('date', ''))
        # Must be 2025 or later
        assert '2025' in date_str or '2026' in date_str


# ===================================================================
# 2. Anthropic Absence from Publisher Deals
# ===================================================================

class TestAnthropicPublisherAbsence:
    """Anthropic has $1.5B author settlement but zero publisher content deals."""

    def test_anthropic_entity_exists(self, entities):
        assert 'anthropic' in entities['entities']

    def test_anthropic_has_publisher_deals_note(self, entities):
        anthropic = entities['entities']['anthropic']
        assert 'publisher_deals_note' in anthropic

    def test_anthropic_zero_publisher_deals_documented(self, entities):
        anthropic = entities['entities']['anthropic']
        note = anthropic['publisher_deals_note'].lower()
        assert 'zero' in note

    def test_anthropic_settlement_amount_documented(self, entities):
        anthropic = entities['entities']['anthropic']
        note = anthropic['publisher_deals_note'].lower()
        assert '1.5' in note or 'billion' in note

    def test_anthropic_has_settlement_source(self, entities):
        anthropic = entities['entities']['anthropic']
        assert 'author_settlement_source' in anthropic
        assert 'pymnts' in anthropic['author_settlement_source'].lower()

    def test_anthropic_valuation_updated_to_2026(self, entities):
        anthropic = entities['entities']['anthropic']
        cap = anthropic.get('market_cap_approx', '')
        assert '183' in cap or '2026' in cap

    def test_no_profiled_publication_has_anthropic_deal(self, entities):
        """No MediaScope publication should have an Anthropic revenue relationship."""
        for pub in entities['meta_ai_deals']['excluded_publishers']:
            for deal in pub.get('deals_with_competitors', []):
                assert 'anthropic' not in deal.get('partner', '').lower(), \
                    f"{pub['name']} has unexpected Anthropic deal"

    def test_anthropic_warns_about_fabricated_nyt_report(self, entities):
        """Publisher deals note should warn about the fabricated TokenRing report."""
        anthropic = entities['entities']['anthropic']
        note = anthropic['publisher_deals_note'].lower()
        assert 'fabricated' in note or 'tokenring' in note or 'financialcontent' in note


# ===================================================================
# 3. Google Coercive Showcase → AI Pilot Structure
# ===================================================================

class TestGoogleCoerciveStructure:
    """Google demands AI training rights or publishers lose Showcase fees."""

    def test_coercion_detail_exists(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        assert 'coercion_detail' in pilot

    def test_coercion_mentions_showcase(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail'].lower()
        assert 'showcase' in detail

    def test_coercion_mentions_training_rights(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail'].lower()
        assert 'training' in detail

    def test_coercion_mentions_advertising_dependency(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail'].lower()
        assert 'advertising' in detail or 'ad' in detail

    def test_coercion_mentions_search_traffic(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail'].lower()
        assert 'traffic' in detail

    def test_coercion_quotes_jason_kint(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail']
        assert 'Kint' in detail or 'Digital Content Next' in detail

    def test_coercion_contrasts_with_meta(self, entities):
        """Coercion detail should note Meta's voluntary model for contrast."""
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        detail = pilot['coercion_detail'].lower()
        assert 'meta' in detail

    def test_pymnts_source_in_urls(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        urls = ' '.join(pilot.get('source_urls', []))
        assert 'pymnts' in urls.lower()

    def test_nypost_source_in_urls(self, entities):
        pilot = entities['meta_ai_deals']['cross_platform_summary']['google_news_ai_pilot']
        urls = ' '.join(pilot.get('source_urls', []))
        assert 'nypost' in urls.lower()


# ===================================================================
# 4. Updated Aggregate Counts
# ===================================================================

class TestUpdatedAggregateCounts:
    """Total counts reflect Perplexity + Snowflake deals (19 total as of Aug 5 23:00 PT)."""

    def test_total_is_19_not_17(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        assert matrix['total_competitor_deal_count'] == 19

    def test_wired_is_5_not_4(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        wired = [p for p in pubs if 'WIRED' in p['name']][0]
        assert wired['competitor_deals'] == 5

    def test_wired_platforms_include_perplexity(self, entities):
        pubs = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        wired = [p for p in pubs if 'WIRED' in p['name']][0]
        platforms_text = ' '.join(wired['platforms']).lower()
        assert 'perplexity' in platforms_text

    def test_sum_equals_total(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        individual = sum(p['competitor_deals'] for p in matrix['publications'])
        assert individual == matrix['total_competitor_deal_count']

    def test_critical_finding_mentions_19(self, entities):
        finding = entities['meta_ai_deals'].get('critical_finding', '')
        assert '19' in finding

    def test_critical_finding_mentions_perplexity(self, entities):
        finding = entities['meta_ai_deals'].get('critical_finding', '').lower()
        assert 'perplexity' in finding

    def test_statistical_note_mentions_5_for_conde_nast(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']
        note = matrix.get('statistical_note', '')
        assert '5' in note
