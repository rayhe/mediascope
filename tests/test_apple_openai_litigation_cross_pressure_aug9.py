"""
Tests for Apple-OpenAI Litigation Publisher Cross-Pressure Analysis (Aug 9, 2026)

Type C: Financial Incentive Mapping — when Apple sues OpenAI, publications with
financial ties to BOTH companies face conflicting coverage incentives.

Verifies:
1. Cross-pressure publication mapping completeness
2. Apple vs OpenAI leverage comparison
3. Anthropic settlement date correction (Jun 20 → Jul 20)
4. Anthropic settlement detail expansion
5. Coverage artifact framing documentation
6. Financial implication analysis for both outcomes
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)


class TestAppleOpenAILitigationCrossPressure:
    """Tests for the cross-pressure analysis section."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        self.apple = data['entities']['apple']
        self.cross_pressure = self.apple['openai_litigation_publisher_cross_pressure']

    def test_cross_pressure_section_exists(self):
        assert 'openai_litigation_publisher_cross_pressure' in self.apple

    def test_overview_mentions_natural_experiment(self):
        overview = self.cross_pressure['overview']
        assert 'natural experiment' in overview.lower() or 'cross-pressure' in overview.lower()

    def test_overview_mentions_apple_news_plus(self):
        overview = self.cross_pressure['overview']
        assert 'News+' in overview or 'Apple News' in overview

    def test_overview_mentions_dual_financial_ties(self):
        overview = self.cross_pressure['overview']
        assert 'dual' in overview.lower() or 'both' in overview.lower()

    def test_prediction_favors_greater_leverage(self):
        overview = self.cross_pressure['overview']
        assert 'greater' in overview.lower() or 'GREATER' in overview

    def test_apple_leverage_count_is_five(self):
        overview = self.cross_pressure['overview']
        assert '5 mechanisms' in overview or 'FIVE' in overview or '5)' in overview


class TestDualRelationshipPublications:
    """Tests for publications with both Apple and OpenAI ties."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        self.pubs = apple['openai_litigation_publisher_cross_pressure']['dual_relationship_publications']
        self.pub_names = [p['publication'] for p in self.pubs]

    def test_at_least_five_publications_mapped(self):
        assert len(self.pubs) >= 5

    def test_conde_nast_included(self):
        assert any('Condé Nast' in p or 'Conde Nast' in p for p in self.pub_names)

    def test_atlantic_included(self):
        assert any('Atlantic' in p for p in self.pub_names)

    def test_vox_media_included(self):
        assert any('Vox Media' in p for p in self.pub_names)

    def test_news_corp_included(self):
        assert any('News Corp' in p for p in self.pub_names)

    def test_washington_post_included(self):
        assert any('Washington Post' in p for p in self.pub_names)

    def test_guardian_included(self):
        assert any('Guardian' in p for p in self.pub_names)

    def test_each_pub_has_openai_deal_field(self):
        for pub in self.pubs:
            assert 'openai_deal' in pub, f"Missing openai_deal for {pub['publication']}"

    def test_each_pub_has_apple_news_plus_field(self):
        for pub in self.pubs:
            assert 'apple_news_plus' in pub, f"Missing apple_news_plus for {pub['publication']}"

    def test_each_pub_has_cross_pressure_analysis(self):
        for pub in self.pubs:
            assert 'cross_pressure' in pub, f"Missing cross_pressure for {pub['publication']}"

    def test_guardian_unique_no_apple_news(self):
        guardian = [p for p in self.pubs if 'Guardian' in p['publication']]
        assert len(guardian) == 1
        assert 'NO' in guardian[0]['apple_news_plus'] or 'dropped' in guardian[0]['apple_news_plus'].lower()

    def test_atlantic_apple_stock_exposure_noted(self):
        atlantic = [p for p in self.pubs if 'Atlantic' in p['publication']]
        assert len(atlantic) == 1
        # LPJ Trust ~$17B Apple stock is the largest undisclosed conflict
        assert '$17B' in atlantic[0].get('apple_other', '') or '17B' in atlantic[0].get('apple_other', '')

    def test_news_corp_balanced_noted(self):
        news_corp = [p for p in self.pubs if 'News Corp' in p['publication']]
        assert len(news_corp) == 1
        assert 'balanced' in news_corp[0].get('cross_pressure', '').lower()

    def test_wapo_amazon_anthropic_chain_noted(self):
        wapo = [p for p in self.pubs if 'Washington Post' in p['publication']]
        assert len(wapo) == 1
        wapo_text = str(wapo[0])
        assert 'Amazon' in wapo_text and 'Anthropic' in wapo_text


class TestCoverageArtifacts:
    """Tests for documented coverage examples."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        self.cross_pressure = apple['openai_litigation_publisher_cross_pressure']
        self.artifacts = self.cross_pressure['key_coverage_artifacts']

    def test_at_least_three_coverage_artifacts(self):
        assert len(self.artifacts) >= 3

    def test_wsj_artifact_exists(self):
        wsj = [a for a in self.artifacts if a['publication'] == 'WSJ']
        assert len(wsj) == 1

    def test_wsj_has_url(self):
        wsj = [a for a in self.artifacts if a['publication'] == 'WSJ'][0]
        assert wsj['url'].startswith('https://')

    def test_wsj_framing_is_balanced(self):
        wsj = [a for a in self.artifacts if a['publication'] == 'WSJ'][0]
        assert 'balanced' in wsj['framing'].lower() or 'Balanced' in wsj['framing']

    def test_reuters_serves_as_control(self):
        reuters = [a for a in self.artifacts if a['publication'] == 'Reuters']
        assert len(reuters) == 1
        assert 'control' in reuters[0]['framing'].lower() or 'neutral' in reuters[0]['framing'].lower()

    def test_all_artifacts_have_dates(self):
        for a in self.artifacts:
            assert 'date' in a, f"Missing date for {a['publication']} artifact"

    def test_all_artifacts_have_framing(self):
        for a in self.artifacts:
            assert 'framing' in a, f"Missing framing for {a['publication']} artifact"


class TestFinancialImplications:
    """Tests for outcome-dependent financial implications."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        apple = data['entities']['apple']
        self.cross_pressure = apple['openai_litigation_publisher_cross_pressure']

    def test_apple_wins_implications_exist(self):
        assert 'apple_wins_financial_implications' in self.cross_pressure

    def test_openai_wins_implications_exist(self):
        assert 'openai_wins_financial_implications' in self.cross_pressure

    def test_apple_wins_mentions_hardware(self):
        text = self.cross_pressure['apple_wins_financial_implications']
        assert 'hardware' in text.lower()

    def test_openai_wins_mentions_employee_mobility(self):
        text = self.cross_pressure['openai_wins_financial_implications']
        assert 'mobility' in text.lower() or 'talent' in text.lower()

    def test_source_urls_exist(self):
        assert 'source_urls' in self.cross_pressure
        assert len(self.cross_pressure['source_urls']) >= 3


class TestAnthropicSettlementDateCorrection:
    """Verifies the Anthropic settlement date was corrected from Jun 20 to Jul 20."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        self.anthropic = data['entities']['anthropic']

    def test_publisher_deals_note_says_jul_not_jun(self):
        note = self.anthropic['publisher_deals_note']
        assert 'Jul 20 2026' in note
        assert 'Jun 20 2026' not in note

    def test_rogue_ai_settlement_says_jul(self):
        desc = self.anthropic['rogue_ai_incident']['description']
        assert 'Jul 20' in desc
        assert 'Jun 20' not in desc


class TestAnthropicSettlementDetails:
    """Tests for expanded settlement detail section."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        self.anthropic = data['entities']['anthropic']
        self.detail = self.anthropic['author_settlement_detail']

    def test_settlement_detail_section_exists(self):
        assert 'author_settlement_detail' in self.anthropic

    def test_amount_is_1_5b(self):
        assert self.detail['amount_b'] == 1.5

    def test_works_on_list_count(self):
        assert self.detail['works_on_list'] == 482460

    def test_claims_filed_percentage(self):
        assert self.detail['claims_filed_pct'] == 92.77

    def test_final_approval_date_is_jul_20(self):
        assert self.detail['final_approval_date'] == '2026-07-20'

    def test_final_approval_judge(self):
        assert 'Martínez-Olguín' in self.detail['final_approval_judge'] or \
               'Martinez-Olguin' in self.detail['final_approval_judge']

    def test_attorneys_fee_reduced(self):
        assert self.detail['attorneys_fee_approved_m'] < self.detail['attorneys_fee_reduced_from_m']

    def test_payment_start_date(self):
        assert self.detail['payment_start_estimated'] == '2026-08-10'

    def test_pirated_sources_listed(self):
        sources = self.detail['pirated_sources']
        assert any('LibGen' in s or 'Library Genesis' in s for s in sources)
        assert any('PiLiMi' in s or 'Pirate Library' in s for s in sources)

    def test_case_name(self):
        assert 'Bartz' in self.detail['case_name']

    def test_max_statutory_damages(self):
        assert 'trillion' in self.detail['max_statutory_damages'].lower() or \
               '1.05' in self.detail['max_statutory_damages']

    def test_source_urls_present(self):
        assert len(self.detail['source_urls']) >= 4

    def test_mediascope_note_distinguishes_book_vs_news(self):
        note = self.detail['mediascope_note']
        assert 'book' in note.lower() or 'NOT news' in note


class TestAppleLeverageHierarchy:
    """Tests for the leverage ranking consistency."""

    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_competitor_entities()
        self.apple = data['entities']['apple']

    def test_meta_contrast_still_present(self):
        leverage = self.apple['quintuple_publisher_leverage']
        assert 'meta_contrast' in leverage

    def test_leverage_ranking_in_overview(self):
        overview = self.apple['quintuple_publisher_leverage']['overview']
        assert 'Microsoft' in overview and 'Amazon' in overview

    def test_meta_has_fewest_mechanisms(self):
        overview = self.apple['quintuple_publisher_leverage']['overview']
        assert 'Meta:      1' in overview or 'Meta: 1' in overview or 'FEWEST' in overview
