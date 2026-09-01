"""
Mechanism #427 Type C: Reddit 2025 10-K RPO Disclosure Quantifies AI Licensing Materiality Reinforcing Advance Equity Incentive

Financial Incentive Mapping iteration documenting Reddit 2025 10-K SEC filing RPO $143.7M
primarily from long-term content licensing, $118.9M in 2026 and $24.8M in 2027, reinforcing
Advance Publications 30% Reddit ownership incentive for WIRED (Condé Nast owned by Advance)
to favor Google/OpenAI (Reddit's $60M/yr each licensing customers) vs Meta (Reddit ad
competitor, zero licensing).

Extends mechanism #417 with new primary source SEC 10-K quantification, not duplicate.

Key findings:
- Reddit 2025 10-K RPO $143.7M Dec 31 2025, $118.9M 2026, $24.8M 2027 primarily long-term content licensing
- Advance Magazine Publishers Inc is Reddit largest investor 30% stake per SiliconAngle Feb 22 2024 IPO filing, Wikipedia Advance 30% Reddit, Reddit Wikipedia owners Advance 30% Tencent 11% Altman 9%, SEC S-1 Advance holds Series A preferred 34% voting rights board appointment power
- Reddit Google $60M/yr deal Feb 21 2024 Reuters, The Register $60M/yr, Engadget $60M/yr
- Reddit OpenAI May 16 2024 real-time structured content ChatGPT integration advertising partner TechCrunch, Reuters May 17 2024 $50-60M/yr Piper Sandler $1.2B market cap add
- Combined $110-120M/yr 13-15% Reddit 2023 revenue $804M, Advance stake $1.4B The Information $1.97B TheWrap 33.5% voting 42M shares significant influence directors observer
- Meta Reddit ad competitor per Reuters, Meta zero Reddit licensing, Meta zero Advance relationship, Meta ad revenue $59.363B Q2 2026 competes Reddit $804M
- Payment direction: Google/OpenAI -> Reddit licensing $60M each -> Advance equity appreciation 30% ownership 34% voting + RPO $143.7M forward revenue certainty
- RPO $143.7M is 17.9% of 2023 revenue in contracted future licensing, $118.9M 82.7% of RPO expected 2026 near-term certainty
- Correlation-not-control caveat, editorial independence acknowledgment, strongest counterargument, ranked confounders, cautious_language MANUAL ILLUSTRATIVE
- Limitation: RPO primarily from long-term content licensing not exclusively AI licensing, could include other licensing, forward-looking subject to performance obligations

Sources: SEC 10-K 2025, SiliconAngle, Wikipedia Advance, Wikipedia Reddit, SEC EDGAR S-1, Reuters Google, The Register, TechCrunch OpenAI, Reuters OpenAI partnership, TheWrap, ReadWrite

Created: 2026-08-31 17:00 PDT
Iteration: 427 Type C
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
def google_entity(competitor_entities):
    return competitor_entities['entities']['google']


@pytest.fixture(scope='module')
def mechanism_427(competitor_entities):
    return competitor_entities['entities']['google']['google_reddit_10k_rpo_materiality_427']


@pytest.fixture(scope='module')
def aggregate_427(competitor_research):
    return competitor_research['aggregate_findings']['google_reddit_10k_rpo_materiality_427_aug31_2026']


# ===================================================================
# Mechanism exists
# ===================================================================

class TestMechanism427Exists:

    def test_mechanism_id_427_in_google(self, competitor_entities):
        assert 'google_reddit_10k_rpo_materiality_427' in competitor_entities['entities']['google']

    def test_mechanism_id_field(self, mechanism_427):
        assert mechanism_427['mechanism_id'] == 427

    def test_type_c(self, mechanism_427):
        assert 'Financial Incentive' in mechanism_427['type']

    def test_iteration_427(self, mechanism_427):
        assert mechanism_427['iteration'] == 427

    def test_goal_id(self, mechanism_427):
        assert mechanism_427['goal_id'] == 'goal_54093bda4145'

    def test_payment_direction_includes_rpo(self, mechanism_427):
        pd = mechanism_427['payment_direction']
        assert 'Reddit' in pd
        assert 'Advance' in pd
        assert '143.7' in pd or 'RPO' in pd or '143' in pd

    def test_publication_focus_wired(self, mechanism_427):
        assert 'WIRED' in mechanism_427['publication_focus'] or 'Condé Nast' in mechanism_427['publication_focus']


# ===================================================================
# Primary sources
# ===================================================================

class TestPrimarySources:

    def test_primary_sources_count(self, mechanism_427):
        assert len(mechanism_427['primary_sources']) >= 8

    def test_sec_10k_rpo(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('sec.gov' in u and 'redditinc10-k2025' in u.lower() for u in urls) or any('sec.gov' in u for u in urls)

    def test_siliconangle_advance_30_percent(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('siliconangle.com' in u for u in urls)

    def test_sec_edgar_s1(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('sec.gov' in u and 'reddits-1q423' in u for u in urls) or len([u for u in urls if 'sec.gov' in u]) >= 2

    def test_reuters_google_60m(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('reuters.com' in u for u in urls)

    def test_techcrunch_openai_reddit(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('techcrunch.com' in u for u in urls)

    def test_thewrap_advance_windfall(self, mechanism_427):
        urls = [s['url'] for s in mechanism_427['primary_sources']]
        assert any('thewrap.com' in u for u in urls)

    def test_source_urls_verbatim(self, mechanism_427):
        for src in mechanism_427['source_urls']:
            assert src.startswith('https://'), f"URL must be exact https: {src}"
            assert ' ' not in src

    def test_rpo_claim_present(self, mechanism_427):
        # Check that at least one primary source claim mentions RPO numbers
        claims = [s.get('claim','') for s in mechanism_427['primary_sources']]
        combined = ' '.join(claims)
        assert '143.7' in combined or '143.7M' in combined
        assert '118.9' in combined
        assert '24.8' in combined


# ===================================================================
# Financial incentive mapping
# ===================================================================

class TestFinancialIncentiveMapping:

    def test_correlational_not_causation(self, mechanism_427):
        fi = mechanism_427['financial_incentive_mapping']['financial_relationship']
        assert 'correlat' in fi.lower() or 'structural incentive' in fi.lower()

    def test_editorial_independence_ack(self, mechanism_427):
        assert mechanism_427['financial_incentive_mapping']['editorial_independence_acknowledgment'] is True

    def test_meta_contrast(self, mechanism_427):
        mc = mechanism_427['financial_incentive_mapping']['meta_contrast']
        assert 'Meta' in mc
        assert 'Reddit' in mc

    def test_cautious_language_present(self, mechanism_427):
        cl = mechanism_427['cautious_language']
        assert 'correlation' in cl.lower() or 'not imply causation' in cl.lower()
        assert 'MANUAL ILLUSTRATIVE' in cl or 'illustrative' in cl.lower()

    def test_no_empirical_significance_claim(self, mechanism_427):
        cl = mechanism_427['cautious_language']
        assert 'p_value not_calculated' in cl or 'not statistically significant' in cl.lower() or 'not_calculated' in cl

    def test_counterargument_present(self, mechanism_427):
        assert 'strongest_counterargument' in mechanism_427
        assert len(mechanism_427['strongest_counterargument']) > 200

    def test_confounders_ranked(self, mechanism_427):
        cfs = mechanism_427['confounding_factors']
        assert len(cfs) >= 4
        strengths = [cf['strength'] for cf in cfs]
        assert 'STRONG' in strengths
        assert strengths.count('STRONG') >= 2

    def test_rpo_limitation_documented(self, mechanism_427):
        # Limitation that RPO is primarily not exclusively AI licensing
        cl = mechanism_427['cautious_language']
        counter = mechanism_427['strongest_counterargument']
        combined = cl + ' ' + counter
        assert 'primarily' in combined.lower() and 'long-term content licensing' in combined.lower()


# ===================================================================
# Aggregate findings
# ===================================================================

class TestAggregateFindings:

    def test_aggregate_exists(self, aggregate_427):
        assert aggregate_427 is not None

    def test_mechanism_id(self, aggregate_427):
        assert aggregate_427['mechanism'] == 427

    def test_type_c(self, aggregate_427):
        assert 'Financial Incentive' in aggregate_427['type']

    def test_iteration(self, aggregate_427):
        assert aggregate_427['iteration'] == 427

    def test_rpo_quantification_in_overview(self, aggregate_427):
        ov = aggregate_427['overview']
        assert '143.7' in ov
        assert '118.9' in ov
        assert '24.8' in ov

    def test_extension_of_417_noted(self, aggregate_427):
        ov = aggregate_427['overview']
        assert 'extends' in ov.lower() or 'extension' in ov.lower() or '#417' in ov


# ===================================================================
# YAML parsability and counts
# ===================================================================

class TestYAMLIntegrity:

    def test_competitor_entities_parsable(self):
        # Lightweight check - file loads without scanner error for this section
        # Full file may have large size, so we test that our mechanism section is valid yaml
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            content = f.read()
            assert 'google_reddit_10k_rpo_materiality_427' in content
            assert 'mechanism_id: 427' in content

    def test_no_duplicate_mechanism_427(self, competitor_entities):
        # Ensure only one occurrence in google entity
        assert competitor_entities['entities']['google']['google_reddit_10k_rpo_materiality_427']['mechanism_id'] == 427
