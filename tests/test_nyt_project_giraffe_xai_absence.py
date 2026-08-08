"""
Tests for NYT-OpenAI Project Giraffe discovery obstruction, xAI publisher
absence, and Snowflake Cortex marketplace findings (Type C iteration, Aug 5 2026 23:00 PT).

Validates three findings:
1. NYT-OpenAI litigation escalation: Project Giraffe, 78M conversations,
   sanctions motion (Jul 2026)
2. xAI publisher absence: zero deals, zero lawsuits, "publisher-invisible"
3. Snowflake Cortex marketplace: new AI licensing platform with 17 publishers,
   deepening the NYT "Litigation Paradox"

Source URLs:
- TechCrunch (Project Giraffe): https://techcrunch.com/2026/07/09/new-york-times-says-openai-hid-evidence-in-chatgpt-copyright-trial/
- Reuters (sanctions motion): https://www.reuters.com/legal/litigation/new-york-times-led-group-asks-court-sanction-openai-us-copyright-dispute-2026-07-09/
- PYMNTS (OpenAI lying): https://www.pymnts.com/legal/2026/openai-accused-of-lying-to-court-in-newspaper-lawsuit/
- Digiday (Snowflake Cortex): https://digiday.com/media/publishers-quietly-cut-six-figure-deals-via-snowflakes-ai-licensing-platform/
- WSJ (marketplace frontier): https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00
- Livemint (xAI-Telegram deal): https://www.livemint.com/technology/tech-news/telegram-partners-with-xai-grok-chatbot-to-be-integrated-in-300-million-deal/amp-11748452711863.html
- Nextgov (xAI GSA contract): https://www.nextgov.com/acquisition/2025/09/gsa-inks-onegov-deal-grok-ai/408334/
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
def meta_deals(entities):
    return entities['meta_ai_deals']


def _get_nyt(entities):
    for pub in entities['meta_ai_deals']['excluded_publishers']:
        if 'New York Times' in pub['name']:
            return pub
    pytest.fail("NYT not found")


def _get_xai(entities):
    return entities['entities'].get('xai')


# ===================================================================
# 1. NYT-OpenAI Project Giraffe & Discovery Obstruction
# ===================================================================

class TestProjectGiraffe:
    """NYT revealed OpenAI had internal infringement measurement tools while
    claiming to the court that such searches were infeasible."""

    def test_nyt_has_litigation_escalation(self, entities):
        nyt = _get_nyt(entities)
        assert 'litigation_escalation_jul2026' in nyt

    def test_escalation_date_is_jul_2026(self, entities):
        nyt = _get_nyt(entities)
        esc = nyt['litigation_escalation_jul2026']
        assert esc['date'] == '2026-07-09'

    def test_escalation_mentions_project_giraffe(self, entities):
        nyt = _get_nyt(entities)
        detail = nyt['litigation_escalation_jul2026']['detail'].lower()
        assert 'project giraffe' in detail

    def test_escalation_mentions_bloom_filter(self, entities):
        nyt = _get_nyt(entities)
        detail = nyt['litigation_escalation_jul2026']['detail'].lower()
        assert 'bloom' in detail

    def test_escalation_mentions_78m_conversations(self, entities):
        nyt = _get_nyt(entities)
        detail = nyt['litigation_escalation_jul2026']['detail']
        assert '78 million' in detail or '78M' in detail

    def test_escalation_mentions_vinnie_monaco(self, entities):
        nyt = _get_nyt(entities)
        detail = nyt['litigation_escalation_jul2026']['detail']
        assert 'Monaco' in detail

    def test_escalation_has_source_urls(self, entities):
        nyt = _get_nyt(entities)
        urls = nyt['litigation_escalation_jul2026'].get('source_urls', [])
        assert len(urls) >= 2
        assert any('techcrunch' in u for u in urls)
        assert any('reuters' in u for u in urls)

    def test_escalation_mentions_sanctions(self, entities):
        nyt = _get_nyt(entities)
        event = nyt['litigation_escalation_jul2026']['event'].lower()
        assert 'sanction' in event

    def test_escalation_mentions_deleted_conversations(self, entities):
        nyt = _get_nyt(entities)
        detail = nyt['litigation_escalation_jul2026']['detail'].lower()
        assert 'deleted' in detail or 'unsearchable' in detail

    def test_nyt_counsel_quote_present(self, entities):
        nyt = _get_nyt(entities)
        quote = nyt['litigation_escalation_jul2026'].get('nyt_counsel_quote', '')
        assert 'lied' in quote.lower()


# ===================================================================
# 2. NYT Litigation Paradox Deepening
# ===================================================================

class TestNYTLitigationParadox:
    """NYT sues OpenAI while monetizing through 3+ AI channels."""

    def test_nyt_deal_count_at_least_3(self, entities):
        nyt = _get_nyt(entities)
        assert nyt['deal_count'] >= 3

    def test_nyt_has_snowflake_deal(self, entities):
        nyt = _get_nyt(entities)
        partners = [d['partner'] for d in nyt['deals_with_competitors']]
        has_snowflake = any('snowflake' in p.lower() for p in partners)
        assert has_snowflake, f"Expected Snowflake in NYT deals, got: {partners}"

    def test_nyt_snowflake_is_commercial_partnership(self, entities):
        nyt = _get_nyt(entities)
        snowflake_deals = [d for d in nyt['deals_with_competitors']
                          if 'snowflake' in d['partner'].lower()]
        assert len(snowflake_deals) == 1
        assert snowflake_deals[0]['type'] == 'commercial_partnership'

    def test_nyt_snowflake_mentions_rag(self, entities):
        nyt = _get_nyt(entities)
        snowflake_deals = [d for d in nyt['deals_with_competitors']
                          if 'snowflake' in d['partner'].lower()]
        scope = snowflake_deals[0].get('scope', '').lower()
        assert 'rag' in scope

    def test_nyt_still_zero_meta_deals(self, entities):
        nyt = _get_nyt(entities)
        assert nyt['meta_deal'] == 'none'

    def test_nyt_aggregate_matrix_updated(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        nyt_entry = [p for p in matrix if p['name'] == 'NYT'][0]
        assert nyt_entry['competitor_deals'] >= 3

    def test_nyt_aggregate_includes_snowflake(self, entities):
        matrix = entities['meta_ai_deals']['aggregate_incentive_matrix']['publications']
        nyt_entry = [p for p in matrix if p['name'] == 'NYT'][0]
        platforms_str = ' '.join(nyt_entry['platforms']).lower()
        assert 'snowflake' in platforms_str


# ===================================================================
# 3. xAI Publisher Absence
# ===================================================================

class TestXAIPublisherAbsence:
    """xAI has zero publisher deals and zero publisher lawsuits."""

    def test_xai_entity_exists(self, entities):
        xai = _get_xai(entities)
        assert xai is not None, "xAI entity should exist in competitor-entities.yaml"

    def test_xai_category_is_ai_lab(self, entities):
        xai = _get_xai(entities)
        assert xai['category'] == 'ai_lab'

    def test_xai_has_publisher_deals_note(self, entities):
        xai = _get_xai(entities)
        assert 'publisher_deals_note' in xai

    def test_xai_zero_publisher_deals(self, entities):
        xai = _get_xai(entities)
        note = xai['publisher_deals_note'].lower()
        assert 'zero publisher content licensing deals' in note

    def test_xai_mentions_twitter_data(self, entities):
        xai = _get_xai(entities)
        note = xai['publisher_deals_note'].lower()
        assert 'twitter' in note or 'x/' in note

    def test_xai_mentions_grokipedia(self, entities):
        xai = _get_xai(entities)
        note = xai['publisher_deals_note'].lower()
        assert 'grokipedia' in note

    def test_xai_mentions_telegram_deal(self, entities):
        xai = _get_xai(entities)
        note = xai['publisher_deals_note'].lower()
        assert 'telegram' in note

    def test_xai_publisher_invisible(self, entities):
        xai = _get_xai(entities)
        note = xai['publisher_deals_note'].lower()
        assert 'publisher-invisible' in note

    def test_xai_has_telegram_source(self, entities):
        xai = _get_xai(entities)
        assert 'telegram_deal_source' in xai
        assert 'livemint' in xai['telegram_deal_source']

    def test_xai_not_in_excluded_publishers(self, entities):
        """xAI should not appear as an excluded publisher — it's an entity,
        not a publisher being excluded from Meta deals."""
        excluded_names = [p['name'].lower() for p in
                         entities['meta_ai_deals']['excluded_publishers']]
        assert not any('xai' in n for n in excluded_names)


# ===================================================================
# 4. Snowflake Cortex Marketplace
# ===================================================================

class TestSnowflakeCortex:
    """Snowflake Cortex Knowledge Extensions as new AI licensing platform."""

    def test_snowflake_in_cross_platform_summary(self, entities):
        summary = entities['meta_ai_deals']['cross_platform_summary']
        assert 'snowflake_cortex' in summary

    def test_snowflake_has_partners(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        partners = sf.get('confirmed_partners', [])
        assert len(partners) >= 4

    def test_snowflake_includes_washington_post(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        partners = sf.get('confirmed_partners', [])
        assert any('Washington Post' in p for p in partners)

    def test_snowflake_includes_ap(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        partners = sf.get('confirmed_partners', [])
        assert any('Associated Press' in p or 'AP' in p for p in partners)

    def test_snowflake_includes_nyt(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        partners = sf.get('confirmed_partners', [])
        assert any('New York Times' in p or 'NYT' in p for p in partners)

    def test_snowflake_has_source_urls(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        urls = sf.get('source_urls', [])
        assert len(urls) >= 1
        assert any('digiday' in u for u in urls)

    def test_snowflake_mentions_rag(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        desc = sf.get('description', '').lower()
        assert 'rag' in desc

    def test_snowflake_mediascope_relevance_mentions_litigation_paradox(self, entities):
        sf = entities['meta_ai_deals']['cross_platform_summary']['snowflake_cortex']
        relevance = sf.get('mediascope_relevance', '').lower()
        assert 'litigation paradox' in relevance or 'nyt' in relevance


# ===================================================================
# 5. Amazon Marketplace Emerging
# ===================================================================

class TestAmazonMarketplaceEmerging:
    """Amazon building a new marketplace beyond Rufus/Alexa+ bilateral deals."""

    def test_amazon_marketplace_in_cross_platform(self, entities):
        summary = entities['meta_ai_deals']['cross_platform_summary']
        assert 'amazon_marketplace_emerging' in summary

    def test_amazon_marketplace_has_source(self, entities):
        am = entities['meta_ai_deals']['cross_platform_summary']['amazon_marketplace_emerging']
        # Data may use source_urls (list) or source_url (string)
        urls = am.get('source_urls', [am.get('source_url', '')])
        urls_str = str(urls).lower()
        assert urls, "Amazon marketplace should have source URL(s)"
        assert 'wsj' in urls_str


# ===================================================================
# 6. Updated Aggregate Totals
# ===================================================================

class TestUpdatedAggregates:
    """Aggregate deal counts should reflect new Snowflake addition."""

    def test_total_competitor_deals_at_least_19(self, entities):
        total = entities['meta_ai_deals']['aggregate_incentive_matrix']['total_competitor_deal_count']
        assert total >= 19

    def test_total_meta_deals_still_zero(self, entities):
        total = entities['meta_ai_deals']['aggregate_incentive_matrix']['total_meta_deal_count']
        assert total == 0

    def test_critical_finding_mentions_project_giraffe(self, entities):
        finding = entities['meta_ai_deals']['critical_finding'].lower()
        assert 'project giraffe' in finding

    def test_critical_finding_mentions_xai(self, entities):
        finding = entities['meta_ai_deals']['critical_finding'].lower()
        assert 'xai' in finding

    def test_critical_finding_mentions_snowflake(self, entities):
        finding = entities['meta_ai_deals']['critical_finding'].lower()
        assert 'snowflake' in finding

    def test_critical_finding_mentions_marketplace(self, entities):
        finding = entities['meta_ai_deals']['critical_finding'].lower()
        assert 'marketplace' in finding

    def test_statistical_note_mentions_19(self, entities):
        note = entities['meta_ai_deals']['aggregate_incentive_matrix']['statistical_note']
        assert '19' in note
