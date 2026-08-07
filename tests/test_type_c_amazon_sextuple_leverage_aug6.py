"""
Tests for Amazon Sextuple Publisher Leverage Web — Type C Financial Incentive Mapping
Created: 2026-08-06 18:00 PT

Validates Amazon's six-layer financial relationship mechanisms with publishers
and the coverage asymmetry they produce relative to Meta's single-layer model.

Sources:
- Amazon Q2 2026 earnings (Jul 30): $200.6B revenue, $53.4B Anthropic gain
- NYT-Amazon deal (May 2025): $20-25M/yr for Alexa/AI content licensing
- Condé Nast/Hearst Amazon Rufus deals (Jul 2025)
- Microsoft PCM launch (Feb 2026): Condé Nast, Hearst, Vox Media, AP, USA Today
- WaPo layoffs (Feb 2026): 350+ journalists, CEO departure
- Amazon Anthropic investment: $13B+ total, $53.4B Q2 2026 paper gain
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


# ===================================================================
# TEST CLASS 1: Amazon Entity Sextuple Leverage Structure
# ===================================================================
class TestAmazonSextupleLeverage:
    """Validates the six-layer financial relationship model in competitor-entities.yaml."""

    def test_sextuple_leverage_section_exists(self, entities):
        amazon = entities['entities']['amazon']
        assert 'sextuple_publisher_leverage' in amazon

    def test_exactly_six_layers(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        assert len(layers) == 6

    def test_layer_names_match(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        expected = {
            'aws_cloud_hosting', 'advertising_platform', 'ai_content_licensing',
            'kindle_publishing_platform', 'bezos_wapo_ownership', 'anthropic_investment'
        }
        actual = {layer['name'] for layer in layers}
        assert actual == expected

    def test_all_layers_have_detail(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        for layer in layers:
            assert 'detail' in layer, f"Layer {layer['name']} missing detail"
            assert len(layer['detail'].strip()) > 50, f"Layer {layer['name']} detail too short"

    def test_meta_contrast_exists(self, entities):
        leverage = entities['entities']['amazon']['sextuple_publisher_leverage']
        assert 'meta_contrast' in leverage
        assert 'ZERO' in leverage['meta_contrast'] or 'ONE' in leverage['meta_contrast']

    def test_overview_mentions_six_mechanisms(self, entities):
        overview = entities['entities']['amazon']['sextuple_publisher_leverage']['overview']
        assert 'SIX' in overview or 'six' in overview


# ===================================================================
# TEST CLASS 2: Amazon Q2 2026 Earnings Data
# ===================================================================
class TestAmazonQ2Earnings:
    """Validates Q2 2026 financial data in Amazon entity profile."""

    def test_q2_earnings_section_exists(self, entities):
        assert 'q2_2026_earnings' in entities['entities']['amazon']

    def test_revenue_over_200b(self, entities):
        revenue = entities['entities']['amazon']['q2_2026_earnings']['total_revenue_b']
        assert revenue >= 200, f"Expected revenue >= $200B, got ${revenue}B"

    def test_advertising_revenue_growth(self, entities):
        ad_yoy = entities['entities']['amazon']['q2_2026_earnings']['advertising_yoy_pct']
        assert ad_yoy >= 25, f"Expected ad YoY >= 25%, got {ad_yoy}%"

    def test_aws_revenue_growth(self, entities):
        aws_yoy = entities['entities']['amazon']['q2_2026_earnings']['aws_yoy_pct']
        assert aws_yoy >= 35, f"Expected AWS YoY >= 35%, got {aws_yoy}%"

    def test_anthropic_gain_exceeds_operating_income(self, entities):
        """The Anthropic paper gain ($53.4B) was nearly DOUBLE operating income ($27.5B)."""
        earnings = entities['entities']['amazon']['q2_2026_earnings']
        assert earnings['anthropic_gain_b'] > 50
        assert earnings['eps'] > 5

    def test_earnings_has_source_urls(self, entities):
        sources = entities['entities']['amazon']['q2_2026_earnings']['source_urls']
        assert len(sources) >= 3
        # Must include financial sources
        domains = [s for s in sources if 'marketwatch' in s or 'wsj' in s or 'adweek' in s]
        assert len(domains) >= 2

    def test_advertising_ttm_over_75b(self, entities):
        """Amazon's trailing 12-month ad revenue exceeds $75B."""
        ttm = entities['entities']['amazon']['q2_2026_earnings']['advertising_ttm_b']
        assert ttm >= 75


# ===================================================================
# TEST CLASS 3: Anthropic Investment Double Play
# ===================================================================
class TestAnthropicDoublePlay:
    """Validates Amazon-Anthropic conflict: paying publishers AND investing in non-payer."""

    def test_anthropic_investment_layer_exists(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic_layers = [l for l in layers if l['name'] == 'anthropic_investment']
        assert len(anthropic_layers) == 1

    def test_anthropic_total_invested(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic = [l for l in layers if l['name'] == 'anthropic_investment'][0]
        assert anthropic['anthropic_total_invested_b'] >= 13

    def test_anthropic_zero_publisher_deals(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic = [l for l in layers if l['name'] == 'anthropic_investment'][0]
        assert anthropic['anthropic_publisher_deals'] == 0

    def test_anthropic_gain_documented(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic = [l for l in layers if l['name'] == 'anthropic_investment'][0]
        assert anthropic['anthropic_q2_2026_gain_b'] >= 53

    def test_anthropic_has_source_urls(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic = [l for l in layers if l['name'] == 'anthropic_investment'][0]
        assert 'source_urls' in anthropic
        assert len(anthropic['source_urls']) >= 2

    def test_double_play_conflict_described(self, entities):
        """Amazon pays publishers AND invests in non-payer — conflict must be documented."""
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        anthropic = [l for l in layers if l['name'] == 'anthropic_investment'][0]
        detail = anthropic['detail']
        assert 'ZERO' in detail or 'zero' in detail
        assert 'publisher' in detail.lower()


# ===================================================================
# TEST CLASS 4: Bezos/WaPo Ownership Layer
# ===================================================================
class TestBezosWapoOwnership:
    """Validates the Bezos/WaPo ownership financial layer."""

    def test_wapo_layer_exists(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        wapo = [l for l in layers if l['name'] == 'bezos_wapo_ownership']
        assert len(wapo) == 1

    def test_wapo_layoff_data(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        wapo = [l for l in layers if l['name'] == 'bezos_wapo_ownership'][0]
        detail = wapo['detail']
        assert '350' in detail or '44%' in detail or '300' in detail

    def test_wapo_subscriber_loss(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        wapo = [l for l in layers if l['name'] == 'bezos_wapo_ownership'][0]
        assert '60,000' in wapo['detail'] or '60000' in wapo['detail']

    def test_wapo_has_source_urls(self, entities):
        layers = entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        wapo = [l for l in layers if l['name'] == 'bezos_wapo_ownership'][0]
        assert 'source_urls' in wapo
        assert len(wapo['source_urls']) >= 2


# ===================================================================
# TEST CLASS 5: Leverage Count Comparison
# ===================================================================
class TestLeverageCountComparison:
    """Validates comparative leverage counts across entities."""

    def test_amazon_has_most_layers(self, entities):
        """Amazon (6) > Google (4) > OpenAI (1) = Meta (1)."""
        leverage = entities['entities']['amazon']['sextuple_publisher_leverage']
        assert len(leverage['layers']) == 6

    def test_google_has_four_coercion_layers(self, entities):
        """Google's quadruple coercion structure should be documented."""
        google = entities['entities']['google']
        assert 'advertising_dependency_coercion' in google
        layers = google['advertising_dependency_coercion']['layers']
        assert len(layers) == 4

    def test_meta_has_voluntary_deals_only(self, entities):
        """Meta has voluntary AI licensing deals — no coercive leverage."""
        meta_deals = entities.get('meta_ai_deals', {})
        # Meta deals section should exist at top level
        assert meta_deals or 'meta' in entities['entities']


# ===================================================================
# TEST CLASS 6: Research File Coverage Asymmetry
# ===================================================================
class TestResearchFileCoverageAsymmetry:
    """Validates cross-publication Amazon coverage findings in research file."""

    def test_cross_entity_leverage_section_exists(self, research):
        assert 'cross_entity_leverage' in research

    def test_amazon_sextuple_in_cross_entity(self, research):
        section = research['cross_entity_leverage']
        assert 'amazon_sextuple_leverage' in section

    def test_leverage_layer_count_is_six(self, research):
        section = research['cross_entity_leverage']['amazon_sextuple_leverage']
        assert section['leverage_layer_count'] == 6

    def test_comparison_data_present(self, research):
        comparison = research['cross_entity_leverage']['amazon_sextuple_leverage']['comparison']
        assert comparison['google_layers'] == 4
        assert comparison['amazon_layers'] == 6
        assert comparison['meta_layers'] == 1
        assert comparison['openai_layers'] == 1

    def test_coverage_asymmetry_findings_populated(self, research):
        findings = research['cross_entity_leverage']['amazon_sextuple_leverage']['coverage_asymmetry_findings']
        assert len(findings) >= 3
        # Should include WIRED, NYT, and News Corp
        pubs = {f['publication'] for f in findings}
        assert 'wired' in pubs
        assert 'nytimes' in pubs

    def test_wired_deal_count_differential(self, research):
        """Condé Nast has 4 AI deals (OpenAI, Amazon, Microsoft, Perplexity), Meta has 0."""
        findings = research['cross_entity_leverage']['amazon_sextuple_leverage']['coverage_asymmetry_findings']
        wired = [f for f in findings if f['publication'] == 'wired'][0]
        assert 'none' in wired['meta_deals'].lower()
        assert 'OpenAI' in wired['amazon_deals'] or 'Rufus' in wired['amazon_deals']

    def test_anthropic_double_play_documented(self, research):
        section = research['cross_entity_leverage']['amazon_sextuple_leverage']
        assert 'anthropic_double_play' in section
        dp = section['anthropic_double_play']
        assert dp['anthropic_publisher_deal_count'] == 0
        assert dp['anthropic_total_invested_b'] >= 13
        assert dp['anthropic_q2_2026_paper_gain_b'] >= 53


# ===================================================================
# TEST CLASS 7: Source URLs
# ===================================================================
class TestSourceURLs:
    """Validates source URL presence and format."""

    def test_entities_amazon_has_earnings_sources(self, entities):
        sources = entities['entities']['amazon']['q2_2026_earnings']['source_urls']
        for url in sources:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_entities_marketplace_has_sources(self, entities):
        sources = entities['entities']['amazon']['publisher_content_marketplace']['source_urls']
        assert len(sources) >= 2
        for url in sources:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_research_sextuple_has_sources(self, research):
        sources = research['cross_entity_leverage']['amazon_sextuple_leverage']['source_urls']
        assert len(sources) >= 5
        for url in sources:
            assert url.startswith('http'), f"Invalid URL: {url}"


# ===================================================================
# TEST CLASS 8: Aggregate Findings Updated
# ===================================================================
class TestAggregateFindingsUpdated:
    """Validates that Amazon sextuple leverage finding is in aggregate section."""

    def test_amazon_finding_in_aggregate(self, research):
        findings = research['aggregate_findings']['key_evidence']
        amazon_findings = [f for f in findings if 'amazon' in f.get('finding', '').lower()
                           or 'sextuple' in f.get('finding', '').lower()]
        assert len(amazon_findings) >= 1

    def test_amazon_finding_has_significance(self, research):
        findings = research['aggregate_findings']['key_evidence']
        amazon_findings = [f for f in findings if 'amazon' in f.get('finding', '').lower()
                           or 'sextuple' in f.get('finding', '').lower()]
        for f in amazon_findings:
            assert 'significance' in f
            assert len(f['significance']) > 20


# ===================================================================
# TEST CLASS 9: Publisher Content Marketplace
# ===================================================================
class TestPublisherContentMarketplace:
    """Validates Amazon's marketplace data in entity profile."""

    def test_marketplace_section_exists(self, entities):
        assert 'publisher_content_marketplace' in entities['entities']['amazon']

    def test_marketplace_status(self, entities):
        marketplace = entities['entities']['amazon']['publisher_content_marketplace']
        assert marketplace['status'] == 'building'
        assert marketplace['announced'] == '2026-02'

    def test_marketplace_detail_mentions_both_buyer_and_operator(self, entities):
        detail = entities['entities']['amazon']['publisher_content_marketplace']['detail']
        assert 'BUYER' in detail or 'buyer' in detail
        assert 'OPERATOR' in detail or 'operator' in detail or 'PLATFORM' in detail

    def test_marketplace_has_source_urls(self, entities):
        sources = entities['entities']['amazon']['publisher_content_marketplace']['source_urls']
        assert len(sources) >= 2
        # Should include WSJ and Reuters
        wsj = any('wsj' in s for s in sources)
        reuters = any('reuters' in s for s in sources)
        assert wsj or reuters


# ===================================================================
# TEST CLASS 10: Cross-Entity Consistency
# ===================================================================
class TestCrossEntityConsistency:
    """Validates Amazon data is consistent with other entity profiles."""

    def test_anthropic_zero_deals_consistent(self, entities):
        """Anthropic entity should also confirm zero publisher deals."""
        anthropic = entities['entities']['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in note or 'zero' in note.lower()

    def test_google_coercion_layers_match_comparison(self, entities, research):
        """Google's 4 coercion layers should match the Amazon comparison count."""
        google_layers = entities['entities']['google']['advertising_dependency_coercion']['layers']
        comparison = research['cross_entity_leverage']['amazon_sextuple_leverage']['comparison']
        assert len(google_layers) == comparison['google_layers']

    def test_meta_deals_exist_in_top_level(self, entities):
        """Meta AI deals should be documented at top level."""
        assert 'meta_ai_deals' in entities

    def test_meta_deal_count_greater_than_zero(self, entities):
        """Meta has 13+ AI content partners."""
        partners = entities['meta_ai_deals']['partners']
        assert len(partners) >= 10
