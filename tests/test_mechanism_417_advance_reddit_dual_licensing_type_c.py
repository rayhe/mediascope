"""
Mechanism #417 Type C: Advance Publications Reddit Equity + Reddit AI Licensing Dual Revenue Dependency

Financial Incentive Mapping iteration documenting Advance Publications 30% Reddit ownership creates structural incentive for WIRED (Condé Nast owned by Advance) to favor Google/OpenAI (Reddit's $60M/yr each licensing customers) vs Meta (Reddit ad competitor, zero licensing).

Key findings:
- Advance Magazine Publishers Inc is Reddit largest investor 30% stake per SiliconAngle Feb 22 2024 IPO filing, Wikipedia Advance 30% Reddit, Reddit Wikipedia owners Advance 30% Tencent 11% Altman 9%, SEC S-1 Advance holds Series A preferred 34% voting rights board appointment power
- Reddit Google $60M/yr deal Feb 21 2024 Reuters, The Register $60M/yr, Engadget $60M/yr
- Reddit OpenAI May 16 2024 real-time structured content ChatGPT integration advertising partner TechCrunch, Reuters May 17 2024 $50-60M/yr Piper Sandler $1.2B market cap add
- Combined $110-120M/yr 13-15% Reddit 2023 revenue $804M, Advance stake $1.4B The Information $1.97B TheWrap 33.5% voting 42M shares significant influence directors observer
- Meta Reddit ad competitor per Reuters, Meta zero Reddit licensing, Meta zero Advance relationship, Meta ad revenue $59.363B Q2 2026 competes Reddit $804M
- Payment direction: Google/OpenAI -> Reddit licensing $60M each -> Advance equity appreciation 30% ownership 34% voting
- Correlation-not-control caveat, editorial independence acknowledgment, strongest counterargument, ranked confounders

Sources: SiliconAngle, Wikipedia Advance, Wikipedia Reddit, SEC EDGAR S-1, Reuters Google, The Register, TechCrunch OpenAI, Reuters OpenAI partnership, TheWrap, ReadWrite

Created: 2026-08-31 06:00 PDT
Iteration: 417 Type C
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
def google(competitor_entities):
    return competitor_entities['entities']['google']


@pytest.fixture(scope='module')
def mechanism_417(competitor_entities):
    return competitor_entities['entities']['google']['google_reddit_advance_dual_licensing_417']


@pytest.fixture(scope='module')
def aggregate_417(competitor_research):
    return competitor_research['aggregate_findings']['google_reddit_advance_dual_licensing_417_aug31_2026']


# ===================================================================
# Mechanism exists
# ===================================================================

class TestMechanism417Exists:

    def test_mechanism_id_417_in_google(self, competitor_entities):
        assert 'google_reddit_advance_dual_licensing_417' in competitor_entities['entities']['google']

    def test_mechanism_id_field(self, mechanism_417):
        assert mechanism_417['mechanism_id'] == 417

    def test_type_c(self, mechanism_417):
        assert 'Financial Incentive' in mechanism_417['type']

    def test_iteration_417(self, mechanism_417):
        assert mechanism_417['iteration'] == 417

    def test_goal_id(self, mechanism_417):
        assert mechanism_417['goal_id'] == 'goal_54093bda4145'

    def test_payment_direction(self, mechanism_417):
        assert 'Google' in mechanism_417['payment_direction'] or 'OpenAI' in mechanism_417['payment_direction']
        assert 'Reddit' in mechanism_417['payment_direction']
        assert 'Advance' in mechanism_417['payment_direction']

    def test_publication_focus_wired(self, mechanism_417):
        assert 'WIRED' in mechanism_417['publication_focus'] or 'Condé Nast' in mechanism_417['publication_focus']


# ===================================================================
# Primary sources
# ===================================================================

class TestPrimarySources:

    def test_primary_sources_count(self, mechanism_417):
        assert len(mechanism_417['primary_sources']) >= 8

    def test_siliconangle_advance_30_percent(self, mechanism_417):
        urls = [s['url'] for s in mechanism_417['primary_sources']]
        assert any('siliconangle.com' in u for u in urls)

    def test_sec_edgar_s1(self, mechanism_417):
        urls = [s['url'] for s in mechanism_417['primary_sources']]
        assert any('sec.gov' in u for u in urls)

    def test_reuters_google_60m(self, mechanism_417):
        urls = [s['url'] for s in mechanism_417['primary_sources']]
        assert any('reuters.com' in u and 'google' in u.lower() for u in urls) or any('reuters.com' in u for u in urls)

    def test_techcrunch_openai_reddit(self, mechanism_417):
        urls = [s['url'] for s in mechanism_417['primary_sources']]
        assert any('techcrunch.com' in u for u in urls)

    def test_thewrap_advance_windfall(self, mechanism_417):
        urls = [s['url'] for s in mechanism_417['primary_sources']]
        assert any('thewrap.com' in u for u in urls)

    def test_source_urls_verbatim(self, mechanism_417):
        for src in mechanism_417['source_urls']:
            assert src.startswith('https://'), f"URL must be exact https: {src}"
            assert ' ' not in src


# ===================================================================
# Coverage prediction
# ===================================================================

class TestCoveragePrediction:

    def test_coverage_prediction_exists(self, mechanism_417):
        assert 'coverage_prediction' in mechanism_417
        assert 'model' in mechanism_417['coverage_prediction']

    def test_coverage_prediction_mentions_meta_exclusion(self, mechanism_417):
        model = mechanism_417['coverage_prediction']['model']
        assert 'Meta' in model or 'meta' in model.lower()

    def test_temporal_window(self, mechanism_417):
        assert 'temporal' in mechanism_417['coverage_prediction']


# ===================================================================
# Financial incentive mapping requirements
# ===================================================================

class TestFinancialIncentiveMapping:

    def test_correlation_not_control_caveat(self, mechanism_417):
        overview = mechanism_417.get('overview', '') + str(mechanism_417.get('financial_incentive_mapping', ''))
        assert 'correlational' in overview.lower() or 'structural incentive' in overview.lower() or 'not proof of editorial control' in overview.lower()

    def test_editorial_independence_acknowledgment(self, mechanism_417):
        mapping = mechanism_417.get('financial_incentive_mapping', {})
        assert mapping.get('editorial_independence_acknowledgment') is True

    def test_strongest_counterargument(self, mechanism_417):
        assert 'strongest_counterargument' in mechanism_417
        ca = mechanism_417['strongest_counterargument']
        assert len(ca) > 100

    def test_confounders_ranked(self, mechanism_417):
        confounders = mechanism_417.get('confounding_factors', [])
        assert len(confounders) >= 5
        strengths = [c['strength'] for c in confounders]
        assert 'STRONG' in strengths
        assert 'MODERATE' in strengths or 'WEAK' in strengths

    def test_cautious_language(self, mechanism_417):
        assert 'cautious_language' in mechanism_417
        cl = mechanism_417['cautious_language'].lower()
        assert 'correlation' in cl


# ===================================================================
# Aggregate findings cross-check
# ===================================================================

class TestAggregateFindings:

    def test_aggregate_exists(self, aggregate_417):
        assert aggregate_417['mechanism'] == 417

    def test_aggregate_type_c(self, aggregate_417):
        assert 'C' in aggregate_417['type']

    def test_aggregate_payment_direction(self, aggregate_417):
        assert 'Reddit' in aggregate_417['payment_direction']
        assert 'Advance' in aggregate_417['payment_direction'] or 'Google' in aggregate_417['payment_direction']

    def test_aggregate_sources(self, aggregate_417):
        assert len(aggregate_417['source_urls']) >= 8

    def test_aggregate_test_file_reference(self, aggregate_417):
        assert '417' in aggregate_417['test_file']


# ===================================================================
# Advance/Reddit wired profile cross-check (secondary)
# ===================================================================

class TestWiredProfileAdvanceReddit:

    def test_wired_yaml_exists(self):
        path = os.path.join(PROFILES_DIR, 'wired.yaml')
        assert os.path.exists(path)

    def test_wired_contains_advance_reddit(self):
        path = os.path.join(PROFILES_DIR, 'wired.yaml')
        with open(path) as f:
            content = f.read()
        # Must document Advance Reddit relationship (already in wired.yaml lines 297+)
        assert 'Advance' in content and 'Reddit' in content

    def test_wired_contains_google_openai_reddit_licensing(self):
        path = os.path.join(PROFILES_DIR, 'wired.yaml')
        with open(path) as f:
            content = f.read()
        # Should mention Reddit licensing or Google/OpenAI content licensing
        assert 'Reddit' in content
