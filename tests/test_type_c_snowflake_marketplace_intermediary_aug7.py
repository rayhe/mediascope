"""
Type C: Snowflake Cortex Marketplace Intermediary — Publisher Financial
Relationship Layer

The emergence of AI content MARKETPLACES (Snowflake Cortex Knowledge
Extensions, Microsoft PCM, Amazon's planned AI content marketplace)
creates an ADDITIONAL financial relationship layer between publishers
and tech companies that the bilateral-deal model does not capture.

KEY FINDING — THREE-TIER PUBLISHER MONETIZATION ARCHITECTURE:

The publisher-AI financial landscape has evolved from bilateral deals
to a three-tier architecture:
  Tier 1: Bilateral deals (OpenAI-News Corp $50M/yr, Meta-News Corp $50M/yr)
  Tier 2: Marketplace operators (Microsoft PCM, Snowflake Cortex, Amazon planned)
  Tier 3: Collective licensing (NMA-Bria, UK PLS scheme, ProRata 500+ publishers)

Each tier creates distinct financial incentive mechanisms:
- Tier 1: Direct revenue → softer coverage of the paying entity
- Tier 2: Platform dependency → softer coverage of the marketplace operator
- Tier 3: Diffuse revenue → no specific coverage incentive per entity

Snowflake Cortex is the FIRST operationally neutral marketplace (unlike
Microsoft PCM, which is both marketplace operator AND first buyer via
Copilot). Snowflake doesn't take a revenue cut — it profits from
infrastructure usage. 17 publishers have joined including Washington Post,
AP, People Inc., USA Today Network, with FT and Economist expressing
interest. Six-figure deals with financial institutions confirmed.

CRITICAL CONTRAST — xAI'S LEGAL EXPOSURE WITHOUT PUBLISHER DEALS:

xAI maintains ZERO publisher content licensing deals but faces massive
legal exposure from AI-generated CSAM/deepfake lawsuits (Doe v. xAI,
CSAM class action, Baltimore city suit). xAI's "publisher-invisible"
status for financial incentive analysis remains accurate — no content
deals means no financial bias mechanism with publishers. But xAI's
legal position is uniquely adversarial: sued by cities, individuals,
and minors, while its CEO amplified the harmful content that triggered
the lawsuits.

Sources:
- Snowflake Cortex: https://digiday.com/media/publishers-quietly-cut-six-figure-deals-via-snowflakes-ai-licensing-platform/
- Snowflake marketplace: https://marketwirenews.com/stock/snow/news/snowflake-marketplace-adds-agentic-products-and-ai-r-4984352061288192.html
- NMA-Bria deal: https://digiday.com/media/news-media-alliance-signs-ai-licensing-deal-to-unlock-recurring-rag-revenue-for-small-and-mid-sized-publishers/
- WSJ marketplaces: https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00
- xAI CSAM suit: https://betanews.com/article/teens-sue-musk-xai-grok-ai-csam-deepfake-lawsuit/
- xAI deepfake class action: https://news.bloomberglaw.com/litigation/grok-maker-xai-faces-non-consensual-sexual-deepfake-class-suit
- Baltimore v xAI: https://decrypt.co/362265/baltimore-sues-x-xai-grok-deepfakes

Created: 2026-08-07 14:00 PT
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


# ===================================================================
# SNOWFLAKE CORTEX MARKETPLACE — Entity Documentation
# ===================================================================

class TestSnowflakeMarketplaceEntity:
    """Verify the Snowflake Cortex marketplace intermediary is documented
    in competitor-entities.yaml."""

    def test_snowflake_entity_exists(self, competitor_entities):
        assert 'snowflake' in competitor_entities['entities']

    def test_snowflake_display_name(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        assert sf['display_name'] == 'Snowflake'

    def test_snowflake_category_is_marketplace(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        assert sf['category'] == 'marketplace_intermediary'

    def test_snowflake_cortex_product_documented(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        assert 'cortex_knowledge_extensions' in sf

    def test_snowflake_publisher_count(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        assert cke['publisher_count'] >= 17

    def test_snowflake_revenue_model_no_cut(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        assert 'no' in cke['revenue_cut'].lower() or 'zero' in cke['revenue_cut'].lower()

    def test_snowflake_named_publishers(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        named = cke['named_publishers']
        expected = ['Washington Post', 'Associated Press', 'People Inc', 'USA Today']
        for pub in expected:
            assert any(pub.lower() in p.lower() for p in named), \
                f"Expected {pub} in named publishers"

    def test_snowflake_deal_scale(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        assert 'six-figure' in cke['deal_scale'].lower() or 'six figure' in cke['deal_scale'].lower()

    def test_snowflake_source_urls(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        assert len(cke['source_urls']) >= 2


# ===================================================================
# THREE-TIER ARCHITECTURE — Financial Relationship Taxonomy
# ===================================================================

class TestThreeTierArchitecture:
    """Verify the three-tier publisher monetization architecture is
    documented and distinguishes bilateral deals from marketplace
    operators from collective licensing."""

    def test_three_tier_section_exists(self, competitor_entities):
        assert 'marketplace_intermediary_landscape' in competitor_entities

    def test_tier_1_bilateral_deals(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        assert 'tier_1_bilateral' in landscape
        tier1 = landscape['tier_1_bilateral']
        assert 'direct' in tier1['description'].lower() or 'licensing' in tier1['description'].lower()

    def test_tier_2_marketplace_operators(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        assert 'tier_2_marketplace' in landscape
        tier2 = landscape['tier_2_marketplace']
        operators = tier2['operators']
        assert len(operators) >= 3
        operator_names = [o['name'] for o in operators]
        assert 'Microsoft PCM' in operator_names
        assert 'Snowflake Cortex' in operator_names

    def test_tier_3_collective_licensing(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        assert 'tier_3_collective' in landscape

    def test_microsoft_dual_role_noted(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        tier2 = landscape['tier_2_marketplace']
        ms_ops = [o for o in tier2['operators'] if 'Microsoft' in o['name']]
        assert len(ms_ops) == 1
        assert ms_ops[0]['dual_role'] is True

    def test_snowflake_neutral_status(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        tier2 = landscape['tier_2_marketplace']
        sf_ops = [o for o in tier2['operators'] if 'Snowflake' in o['name']]
        assert len(sf_ops) == 1
        assert sf_ops[0]['dual_role'] is False


# ===================================================================
# SNOWFLAKE vs MICROSOFT PCM CONTRAST
# ===================================================================

class TestSnowflakeVsMicrosoftPCM:
    """Snowflake and Microsoft PCM are both marketplace intermediaries,
    but with fundamentally different conflict profiles."""

    def test_snowflake_not_buyer(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        cke = sf['cortex_knowledge_extensions']
        assert cke.get('is_content_buyer') is False

    def test_microsoft_is_buyer(self, competitor_entities):
        ms = competitor_entities['entities']['microsoft']
        pcm = ms['septuple_publisher_leverage']
        pcm_layer = [l for l in pcm['layers'] if l['name'] == 'pcm_marketplace_operator']
        assert len(pcm_layer) == 1
        assert 'buyer' in pcm_layer[0]['detail'].lower()

    def test_snowflake_no_ai_lab_investment(self, competitor_entities):
        sf = competitor_entities['entities']['snowflake']
        assert sf.get('ai_lab_investments', 0) == 0

    def test_microsoft_dual_ai_lab_investment(self, competitor_entities):
        ms = competitor_entities['entities']['microsoft']
        layers = ms['septuple_publisher_leverage']['layers']
        layer_names = [l['name'] for l in layers]
        assert 'openai_investment_axis' in layer_names
        assert 'anthropic_investment' in layer_names


# ===================================================================
# xAI LITIGATION LANDSCAPE — Non-Publisher Legal Exposure
# ===================================================================

class TestXAILitigationLandscape:
    """Verify xAI's litigation landscape is documented — massive legal
    exposure from CSAM/deepfake lawsuits despite zero publisher deals."""

    def test_xai_publisher_deals_zero(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        assert 'ZERO' in xai['publisher_deals_note'] or 'zero' in xai['publisher_deals_note'].lower()

    def test_xai_litigation_section_exists(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        assert 'litigation' in xai

    def test_xai_csam_lawsuit(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        cases = xai['litigation']
        csam_cases = [c for c in cases if 'csam' in c['type'].lower() or 'child' in c.get('description', '').lower()]
        assert len(csam_cases) >= 1

    def test_xai_deepfake_class_action(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        cases = xai['litigation']
        deepfake_cases = [c for c in cases if 'deepfake' in c['type'].lower() or 'deepfake' in c.get('description', '').lower()]
        assert len(deepfake_cases) >= 1

    def test_xai_baltimore_city_suit(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        cases = xai['litigation']
        city_cases = [c for c in cases if 'baltimore' in c.get('plaintiff', '').lower()]
        assert len(city_cases) >= 1

    def test_xai_zero_copyright_lawsuits(self, competitor_entities):
        xai = competitor_entities['entities']['xai']
        cases = xai['litigation']
        copyright_cases = [c for c in cases if c['type'].lower() == 'copyright']
        assert len(copyright_cases) == 0, \
            "xAI should have zero publisher copyright lawsuits"

    def test_xai_legacy_media_lies_response(self, competitor_entities):
        """xAI's auto-response to press inquiries about lawsuits."""
        xai = competitor_entities['entities']['xai']
        assert 'Legacy Media Lies' in xai.get('press_response', '') or \
            any('legacy media' in c.get('company_response', '').lower()
                for c in xai.get('litigation', []))


# ===================================================================
# PUBLISHER MULTI-TIER FINANCIAL EXPOSURE
# ===================================================================

class TestPublisherMultiTierExposure:
    """Verify that publisher profiles document multi-tier financial
    exposure — same publishers appearing in bilateral deals AND
    marketplace participation."""

    def test_ap_multi_tier_presence(self, competitor_entities):
        """AP has bilateral deal (OpenAI) + Snowflake Cortex + Microsoft PCM."""
        sf = competitor_entities['entities']['snowflake']
        named = sf['cortex_knowledge_extensions']['named_publishers']
        assert any('associated press' in p.lower() or 'ap' == p.lower() for p in named)

    def test_usa_today_multi_tier_presence(self, competitor_entities):
        """USA Today: Perplexity bilateral + Microsoft PCM + Snowflake Cortex."""
        sf = competitor_entities['entities']['snowflake']
        named = sf['cortex_knowledge_extensions']['named_publishers']
        assert any('usa today' in p.lower() for p in named)

    def test_washington_post_bezos_snowflake_paradox(self, competitor_entities):
        """Washington Post is on Snowflake Cortex while owned by Jeff Bezos,
        whose Amazon has its own competing AI content marketplace."""
        sf = competitor_entities['entities']['snowflake']
        named = sf['cortex_knowledge_extensions']['named_publishers']
        assert any('washington post' in p.lower() for p in named)
        # Amazon also building a marketplace
        amazon = competitor_entities['entities']['amazon']
        assert 'publisher_content_marketplace' in amazon


# ===================================================================
# MARKETPLACE CONCENTRATION RISK
# ===================================================================

class TestMarketplaceConcentrationRisk:
    """The marketplace layer creates concentration risk: if publishers
    depend on Microsoft/Snowflake/Amazon to monetize their content with
    ALL AI builders, the marketplace operators gain leverage similar to
    Google's control over search referral traffic."""

    def test_marketplace_concentration_documented(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        assert 'concentration_risk' in landscape
        risk = landscape['concentration_risk']
        assert 'leverage' in risk.lower() or 'dependency' in risk.lower()

    def test_three_marketplace_operators_identified(self, competitor_entities):
        landscape = competitor_entities['marketplace_intermediary_landscape']
        tier2 = landscape['tier_2_marketplace']
        assert len(tier2['operators']) >= 3

    def test_meta_absent_from_marketplaces(self, competitor_entities):
        """Meta is NOT a marketplace operator and NOT a PCM participant —
        the only major AI company excluded from all marketplace tiers."""
        landscape = competitor_entities['marketplace_intermediary_landscape']
        tier2 = landscape['tier_2_marketplace']
        operator_names = [o['name'].lower() for o in tier2['operators']]
        assert not any('meta' in name for name in operator_names)


# ===================================================================
# FINANCIAL INCENTIVE IMPLICATIONS
# ===================================================================

class TestFinancialIncentiveImplications:
    """The marketplace intermediary layer creates new incentive
    mechanisms beyond bilateral deals."""

    def test_snowflake_publisher_incentive_neutral(self, competitor_entities):
        """Publishers on Snowflake have no incentive to cover Snowflake
        favorably because Snowflake is infrastructure, not a content
        buyer or AI lab."""
        sf = competitor_entities['entities']['snowflake']
        assert sf['category'] == 'marketplace_intermediary'
        assert sf['cortex_knowledge_extensions']['is_content_buyer'] is False

    def test_microsoft_marketplace_operator_incentive(self, competitor_entities):
        """Publishers on Microsoft PCM have strong incentive to cover
        Microsoft favorably because Microsoft is BOTH the marketplace
        AND the first buyer via Copilot."""
        ms = competitor_entities['entities']['microsoft']
        layers = ms['septuple_publisher_leverage']['layers']
        pcm = [l for l in layers if l['name'] == 'pcm_marketplace_operator']
        assert len(pcm) == 1

    def test_xai_financial_neutrality(self, competitor_entities):
        """xAI has zero financial relationships with publishers in either
        direction — no deals, no lawsuits. Financial bias should be zero."""
        xai = competitor_entities['entities']['xai']
        assert 'publisher-invisible' in xai['publisher_deals_note'].lower() or \
            'ZERO' in xai['publisher_deals_note']
        # Litigation is NOT publisher copyright — it's CSAM/deepfake
        cases = xai.get('litigation', [])
        copyright_cases = [c for c in cases if c['type'].lower() == 'copyright']
        assert len(copyright_cases) == 0
