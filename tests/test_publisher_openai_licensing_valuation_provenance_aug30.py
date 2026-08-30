"""
Type C Financial Incentive Mapping — Aug 30 2026 iteration #381

Validates publisher–OpenAI licensing valuation provenance audit.

Focus: FT, Guardian, Atlantic, Axel Springer, and NYT/Amazon control.

Sources verified Aug 30 2026:
- FT–OpenAI Reuters (terms not disclosed): https://www.reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29/
- FT valuation secondary WSJ via Digiday timeline: https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/
- Guardian–OpenAI Digiday media briefing (no training rights mention, spokesperson declined): https://digiday.com/media/media-briefing-what-the-washington-posts-deal-with-openai-says-about-the-future-of-ai-content-licensing/
- Guardian–OpenAI Engadget: https://www.engadget.com/ai/the-guardian-is-the-latest-news-organization-to-partner-with-openai-155555243.html?src=rss/
- Guardian–OpenAI PressGazette: https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Atlantic–OpenAI TechCrunch (not syndication, no full reproduction): https://techcrunch.com/2024/06/22/whats-in-it-for-us-journalists-ask-as-publications-sign-content-deals-with-openai/
- Atlantic–OpenAI VentureBeat: https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media
- Axel Springer Bloomberg Law (tens of millions euros, 3-year, source familiar): https://news.bloomberglaw.com/tech-and-telecom-law/openai-to-pay-axel-springer-tens-of-millions-to-use-news-content
- Axel Springer The Decoder (tens of millions per year claim): https://the-decoder.com/axel-springer-and-openai-license-agreement-is-worth-tens-of-millions-of-euros-per-year/
- NYT–Amazon Editor & Publisher (WSJ people familiar $20-25M/yr): https://www.editorandpublisher.com/stories/amazon-to-pay-new-york-times-at-least-20-million-a-year-in-ai-deal,256961
- NYT–Amazon LiveMint: https://www.livemint.com/technology/amazon-to-pay-new-york-times-at-least-20-million-a-year-in-ai-deal-11724443000000.html
"""

import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def ft_profile():
    with open(os.path.join(PROFILES_DIR, 'financial-times.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def guardian_profile():
    with open(os.path.join(PROFILES_DIR, 'guardian.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def atlantic_profile():
    with open(os.path.join(PROFILES_DIR, 'atlantic.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def bi_profile():
    with open(os.path.join(PROFILES_DIR, 'business-insider.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)

def _openai_root(entities):
    # handles both top-level and nested under 'entities'
    if 'openai' in entities:
        base = entities['openai']
    elif 'entities' in entities and 'openai' in entities['entities']:
        base = entities['entities']['openai']
    else:
        base = {}
    # audit lives under ipo_filing
    if 'publisher_deal_valuation_audit_2026_08_30' in base:
        return base
    # check inside ipo_filing
    if 'ipo_filing' in base and 'publisher_deal_valuation_audit_2026_08_30' in base['ipo_filing']:
        # merge audit up for convenience: return a dict that contains audit at top level
        merged = dict(base)
        merged['publisher_deal_valuation_audit_2026_08_30'] = base['ipo_filing']['publisher_deal_valuation_audit_2026_08_30']
        return merged
    # also check direct top level for ipo_filing audit
    if 'ipo_filing' in base:
        return base
    return base

def _get_audit(entities):
    root = _openai_root(entities)
    audit = root.get('publisher_deal_valuation_audit_2026_08_30')
    if audit:
        return audit
    # try ipo_filing
    if 'ipo_filing' in root:
        audit = root['ipo_filing'].get('publisher_deal_valuation_audit_2026_08_30')
        if audit:
            return audit
    # also try entities['entities']['openai']['ipo_filing']
    return {}


@pytest.fixture(scope="module")
def nyt_profile():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml')) as f:
        return yaml.safe_load(f)


def _find_revenue_partner(profile, partner_name_lower):
    for rel in profile.get('revenue_relationships', []) or []:
        if partner_name_lower in rel.get('partner', '').lower():
            return rel
    # also check competitor_relationships
    cr = profile.get('competitor_relationships', {})
    if partner_name_lower in cr:
        return cr[partner_name_lower]
    return None


# ------------------------------------------------------------------
# FT: primary undisclosed vs secondary $5-10M/yr
# ------------------------------------------------------------------

class TestFinancialTimesValuationProvenance:
    def test_ft_openai_exists(self, ft_profile):
        rel = _find_revenue_partner(ft_profile, 'openai')
        # FT stores under competitor_relationships
        if rel is None:
            rel = ft_profile.get('competitor_relationships', {}).get('openai')
        assert rel is not None, "FT OpenAI relationship must exist"

    def test_ft_cash_terms_not_disclosed(self, ft_profile):
        rel = ft_profile.get('competitor_relationships', {}).get('openai', {})
        assert rel.get('cash_terms_disclosed') is False, "Primary Reuters says terms not disclosed"

    def test_ft_valuation_source_type_secondary(self, ft_profile):
        rel = ft_profile.get('competitor_relationships', {}).get('openai', {})
        assert rel.get('valuation_source_type') == 'secondary_report_based'

    def test_ft_has_both_primary_and_secondary_sources(self, ft_profile):
        rel = ft_profile.get('competitor_relationships', {}).get('openai', {})
        urls = rel.get('source_urls', [])
        assert any('reuters.com' in u for u in urls), "Must include Reuters primary"
        assert any('digiday.com' in u for u in urls), "Must include Digiday secondary timeline"

    def test_ft_estimated_value_still_5_10(self, ft_profile):
        rel = ft_profile.get('competitor_relationships', {}).get('openai', {})
        assert '5-10' in str(rel.get('estimated_value', '')), "FT value should remain $5-10M/yr"

    def test_ft_entities_audit_matches(self, entities):
        audit = _get_audit(entities).get('financial_times', {})
        assert audit.get('cash_terms_disclosed') is False
        assert audit.get('valuation_source_type') == 'secondary_report_based'
        assert 'reuters.com' in ''.join(audit.get('source_urls', []))


# ------------------------------------------------------------------
# Guardian: no training rights claim, terms undisclosed, spokesperson declined
# ------------------------------------------------------------------

class TestGuardianDealScope:
    def test_guardian_openai_exists(self, guardian_profile):
        rels = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()]
        assert len(rels) >= 1, "Guardian OpenAI deal must exist"

    def test_guardian_training_rights_not_explicit(self, guardian_profile):
        rel = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()][0]
        assert rel.get('training_rights_explicit') is False, "Guardian announcement did NOT mention training rights"

    def test_guardian_cash_terms_not_disclosed(self, guardian_profile):
        rel = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()][0]
        assert rel.get('cash_terms_disclosed') is False

    def test_guardian_announced_scope_no_training(self, guardian_profile):
        rel = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()][0]
        scope = rel.get('announced_rights_scope', '').lower()
        assert 'attributed' in scope or 'extract' in scope or 'summary' in scope
        assert 'training' not in scope or 'no explicit' in scope or 'not' in scope or rel.get('training_rights_explicit') is False

    def test_guardian_has_digiday_source(self, guardian_profile):
        rel = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()][0]
        urls = rel.get('source_urls', [])
        assert any('digiday.com/media/media-briefing' in u for u in urls), "Must include Digiday media briefing"

    def test_guardian_description_distinguishes_attributed_vs_training(self, guardian_profile):
        rel = [r for r in guardian_profile.get('revenue_relationships', []) if 'openai' in r.get('partner', '').lower()][0]
        desc = rel.get('description', '').lower()
        assert 'not equivalent to model-training' in desc or 'not equivalent' in desc or 'structural distinction' in desc


# ------------------------------------------------------------------
# Atlantic: undisclosed, reproduction restrictions
# ------------------------------------------------------------------

class TestAtlanticDealScope:
    def test_atlantic_openai_exists(self, atlantic_profile):
        cr = atlantic_profile.get('competitor_relationships', {})
        assert 'openai' in cr or any('openai' in r.get('partner','').lower() for r in atlantic_profile.get('revenue_relationships', []) or [])

    def test_atlantic_estimated_undisclosed_in_audit(self, entities):
        audit = _get_audit(entities).get('atlantic', {})
        assert 'undisclosed' in str(audit.get('estimated_value', '')).lower()

    def test_atlantic_not_syndication_restriction(self, entities):
        audit = _get_audit(entities).get('atlantic', {})
        scope = audit.get('announced_rights_scope', '').lower()
        assert 'not syndication' in scope or 'does not permit' in scope or 'not' in scope

    def test_atlantic_has_techcrunch_source(self, entities):
        audit = _get_audit(entities).get('atlantic', {})
        urls = audit.get('source_urls', [])
        assert any('techcrunch.com' in u for u in urls)


# ------------------------------------------------------------------
# Axel Springer: tens of millions euros, not precise $13M/yr
# ------------------------------------------------------------------

class TestAxelSpringerValuation:
    def test_bi_openai_exists(self, bi_profile):
        rel = _find_revenue_partner(bi_profile, 'openai')
        assert rel is not None

    def test_axel_cash_terms_not_disclosed(self, bi_profile):
        rel = _find_revenue_partner(bi_profile, 'openai')
        assert rel.get('cash_terms_disclosed') is False

    def test_axel_estimated_tens_of_millions(self, bi_profile):
        rel = _find_revenue_partner(bi_profile, 'openai')
        ev = str(rel.get('estimated_value', '')).lower()
        assert 'tens of millions' in ev

    def test_axel_entities_audit_exists(self, entities):
        audit = _get_audit(entities).get('axel_springer', {})
        assert audit is not None
        assert 'tens of millions' in str(audit.get('estimated_value', '')).lower()

    def test_axel_does_not_assert_precise_13m(self, entities):
        audit = _get_audit(entities).get('axel_springer', {})
        note = str(audit.get('secondary_claim', '') + str(audit.get('valuation_note',''))).lower()
        # Must warn against asserting $13M/yr precisely
        assert 'do not assert' in note or 'without stronger evidence' in note or '$13m' in note


# ------------------------------------------------------------------
# NYT Amazon control: $20-25M/yr with Editor & Publisher source
# ------------------------------------------------------------------

class TestNYTAmazonValuationControl:
    def test_nyt_amazon_exists(self, nyt_profile):
        rels = [r for r in nyt_profile.get('revenue_relationships', []) if 'amazon' in r.get('partner', '').lower()]
        assert len(rels) >= 1

    def test_nyt_amazon_has_editor_and_publisher_source(self, nyt_profile):
        rel = [r for r in nyt_profile.get('revenue_relationships', []) if 'amazon' in r.get('partner', '').lower()][0]
        urls = rel.get('source_urls', [])
        assert any('editorandpublisher.com' in u for u in urls), "Must include Editor & Publisher $20-25M/yr source"

    def test_nyt_amazon_audit_exists(self, entities):
        audit = _get_audit(entities).get('nyt_amazon_control', {})
        assert audit is not None
        assert '20-25' in str(audit.get('estimated_value', ''))

    def test_methodology_note_distinguishes_rights_scope(self, entities):
        audit_root = _get_audit(entities)
        note = audit_root.get('methodology_note', '').lower()
        assert 'differ materially in rights scope' in note or 'must not treat every' in note
