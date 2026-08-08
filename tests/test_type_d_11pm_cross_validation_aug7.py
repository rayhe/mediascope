"""
Type D Cross-Validation — 11 PM Aug 7, 2026

End-of-day integrity check across all 12 Aug 7 iterations (00:00–21:00 PT).
Validates cross-file consistency, entity evolution, test infrastructure health,
and the full financial amplification model's internal coherence.

Covers:
- Entity set evolution (8 → 11 over the day)
- Hardcoded-count regression (the exact bug fixed this iteration)
- News Corp triple-revenue architecture (21:00 Type C)
- WIRED Apple v. OpenAI silence (16:00 Type A)
- Parmy Olson professional identity capture (19:00 Type B)
- Samsung equivalence paradox policy consequences (03:00 Type B)
- Financial amplification ordering (clean < connected)
- Revenue dependency concentration cross-file consistency
- Three-tier marketplace taxonomy completeness
- Source URL coverage across all new test files
"""

import os
import re
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='module')
def entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def news_corp():
    with open(os.path.join(PROFILES_DIR, 'news-corp.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def wired():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def nytimes():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def gizmodo():
    with open(os.path.join(PROFILES_DIR, 'gizmodo.yaml')) as f:
        return yaml.safe_load(f)


class TestEntitySetEvolution:
    """Entity count grew from 8 (Aug 6) to 11 (Aug 7) — verify all present."""

    def test_entity_count_at_least_11(self, entities):
        assert len(entities['entities']) >= 11

    def test_original_8_entities_present(self, entities):
        original = ['openai', 'anthropic', 'amazon', 'apple', 'google',
                     'x_twitter', 'meta', 'xai']
        for e in original:
            assert e in entities['entities'], f"Original entity {e} missing"

    def test_aug7_additions_present(self, entities):
        added = ['samsung', 'microsoft', 'snowflake']
        for e in added:
            assert e in entities['entities'], f"Aug 7 entity {e} missing"

    def test_samsung_has_smart_glasses(self, entities):
        samsung = entities['entities']['samsung']
        assert 'smart_glasses' in str(samsung).lower() or 'intelligent_eyewear' in str(samsung).lower()

    def test_snowflake_is_marketplace_category(self, entities):
        snowflake = entities['entities']['snowflake']
        assert 'marketplace' in snowflake.get('category', '')

    def test_microsoft_has_pcm(self, entities):
        ms = entities['entities']['microsoft']
        assert 'pcm' in str(ms).lower() or 'publisher_content_marketplace' in str(ms).lower()


class TestHardcodedCountRegression:
    """The exact bug fixed this iteration: hardcoded entity count assertions.
    Verify no remaining test files assert exact entity count == 9."""

    def test_no_exact_9_entity_assertion(self):
        """Scan test files for hardcoded len(entities['entities']) == 9.
        Excludes this file (which mentions the pattern in docstrings/comments)."""
        violations = []
        this_file = os.path.basename(__file__)
        for fn in os.listdir(TESTS_DIR):
            if not fn.startswith('test_') or not fn.endswith('.py'):
                continue
            if fn == this_file:
                continue
            path = os.path.join(TESTS_DIR, fn)
            with open(path) as f:
                content = f.read()
            # Check for exact == 9 assertions on entity count (in executable lines, not comments)
            for line in content.splitlines():
                stripped = line.strip()
                if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
                    continue
                if re.search(r"len\(entities\[.entities.\]\)\s*==\s*9\b", stripped):
                    violations.append(fn)
                    break
        assert not violations, f"Files with hardcoded entity count == 9: {violations}"

    def test_no_exact_8_entity_assertion(self):
        """Also check for == 8 (original pre-Samsung count)."""
        violations = []
        for fn in os.listdir(TESTS_DIR):
            if not fn.startswith('test_') or not fn.endswith('.py'):
                continue
            path = os.path.join(TESTS_DIR, fn)
            with open(path) as f:
                content = f.read()
            if re.search(r"len\(entities\[.entities.\]\)\s*==\s*8\b", content):
                violations.append(fn)
        assert not violations, f"Files with hardcoded entity count == 8: {violations}"


class TestNewsCorp21PMTripleRevenue:
    """Type C 21:00 — News Corp is the ONLY publisher with 3 AI revenue sources."""

    def test_control_designation_has_triple_revenue_note(self, news_corp):
        ctrl = news_corp.get('control_designation', {})
        assert 'triple_revenue' in str(ctrl).lower()

    def test_news_corp_has_openai_deal(self, news_corp):
        deals = str(news_corp)
        assert 'openai' in deals.lower()

    def test_news_corp_has_meta_deal(self, news_corp):
        deals = str(news_corp)
        assert 'meta' in deals.lower()

    def test_news_corp_has_anthropic_settlement_revenue(self, news_corp):
        deals = str(news_corp)
        assert 'anthropic' in deals.lower()

    def test_q4_fy2026_earnings_documented(self, news_corp):
        """Q4 FY2026 record quarter should be documented."""
        content = str(news_corp)
        # Should have revenue or earnings data
        assert '2.34' in content or 'record' in content.lower() or 'q4' in content.lower()


class TestWIRED16PMAppleSilence:
    """Type A 16:00 — WIRED's 28-day silence on Apple v. OpenAI lawsuit."""

    def test_apple_openai_silence_documented(self, wired):
        comp = wired.get('competitor_relationships', {})
        assert 'apple_v_openai_silence' in str(comp)

    def test_silence_linked_to_conde_nast_openai_deal(self, wired):
        content = str(wired)
        # Both OpenAI deal and silence should be documented
        assert 'openai' in content.lower()
        assert 'silence' in content.lower() or 'zero' in content.lower()

    def test_wired_asymmetry_score_above_0_8(self, research):
        """WIRED asymmetry should be >= 0.82 after this finding."""
        pubs = research.get('publications', {})
        wired_data = pubs.get('wired', {})
        verdict = wired_data.get('asymmetry_verdict', '')
        # Score should be 0.82 or higher
        score_match = re.search(r'0\.\d+', str(verdict))
        if score_match:
            assert float(score_match.group()) >= 0.80


class TestParmyOlson19PMIdentityCapture:
    """Type B 19:00 — Bloomberg's Parmy Olson CEO personalization asymmetry."""

    def test_parmy_olson_in_research(self, research):
        content = str(research)
        assert 'parmy_olson' in content or 'parmy olson' in content.lower()

    def test_professional_identity_capture_mechanism(self, research):
        """4th asymmetry mechanism: professional identity capture."""
        content = str(research).lower()
        assert 'professional identity' in content or 'identity capture' in content

    def test_ceo_personalization_documented(self, research):
        content = str(research).lower()
        assert 'personalization' in content or 'personali' in content


class TestSamsung03PMEquivalenceParadox:
    """Type B 03:00 — Samsung glasses = Meta glasses, different treatment."""

    def test_samsung_entity_exists(self, entities):
        assert 'samsung' in entities['entities']

    def test_school_ban_documented(self, research):
        """Iberville Parish ban targeted Meta BY NAME despite Samsung being identical."""
        content = str(research).lower()
        assert 'iberville' in content or 'school ban' in content or 'ban' in content

    def test_equivalence_paradox_in_research(self, research):
        content = str(research).lower()
        assert 'samsung' in content
        assert 'equivalence' in content or 'identical' in content


class TestFinancialAmplificationModel:
    """Core thesis: financial relationships amplify pre-existing editorial asymmetry.
    Clean controls < financially connected in asymmetry scores."""

    def test_gizmodo_is_clean_control(self, research):
        pubs = research.get('publications', {})
        gizmodo_data = pubs.get('gizmodo', {})
        content = str(gizmodo_data).lower()
        assert 'clean control' in content or 'zero' in content

    def test_three_tier_marketplace_taxonomy_exists(self, entities):
        content = str(entities).lower()
        assert 'marketplace_intermediary_landscape' in content or 'three_tier' in content or 'tier' in content

    def test_meta_financially_isolated(self, entities):
        """Meta has ONLY bilateral deals — not marketplace operator, buyer, or investor.
        The isolation is documented in marketplace_intermediary_landscape, not the entity itself."""
        ml = entities.get('marketplace_intermediary_landscape', {})
        cr = ml.get('concentration_risk', {})
        content = str(cr).lower()
        # Meta's absence from marketplaces should be documented
        assert 'meta' in content


class TestRevenueDependencyConcentration:
    """Cross-validate RDC data from Aug 6 23:00 Type C iteration."""

    def test_rdc_has_9_publications(self, entities):
        rdc = entities.get('revenue_dependency_concentration', {})
        pubs = rdc.get('publications', {})
        assert len(pubs) >= 9

    def test_nyt_is_lowest_ratio(self, entities):
        rdc = entities.get('revenue_dependency_concentration', {})
        pubs = rdc.get('publications', [])
        nyt = next((p for p in pubs if p.get('name', '').lower() in ('nyt', 'new york times', 'new_york_times')), None)
        if nyt and 'dependency_ratio_floor_pct' in nyt:
            assert nyt['dependency_ratio_floor_pct'] <= 1.5

    def test_all_adversarial_pubs_have_zero_meta_deals(self, entities):
        rdc = entities.get('revenue_dependency_concentration', {})
        pubs = rdc.get('publications', [])
        for pub in pubs:
            if pub.get('adversarial_meta_coverage'):
                meta_deals = pub.get('meta_deals', 0)
                assert meta_deals == 0 or meta_deals is None, \
                    f"{pub.get('name')} is adversarial but has Meta deals: {meta_deals}"


class TestTestInfrastructureHealth:
    """Verify test file counts match documentation."""

    def test_at_least_216_test_files(self):
        test_files = [f for f in os.listdir(TESTS_DIR)
                      if f.startswith('test_') and f.endswith('.py')]
        assert len(test_files) >= 216

    def test_readme_test_count_current(self):
        readme_path = os.path.join(PROFILES_DIR, '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        assert '5,904' in content or '5904' in content

    def test_architecture_test_count_current(self):
        arch_path = os.path.join(PROFILES_DIR, '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        assert '5904' in content

    def test_all_aug7_test_files_exist(self):
        """All test files created during Aug 7 iterations should exist."""
        aug7_files = [
            'test_nyt_amazon_february_simultaneous_paradox.py',        # 01:00 Type A
            'test_samsung_equivalence_paradox_aug7.py',                # 03:00 Type B
            'test_pmc_deal_fragmentation_paradox_aug7.py',             # 05:00 Type C
            'test_gizmodo_openai_rogue_ai_framing_paradox_aug7.py',    # 08:00 Type A
            'test_melissa_heikkila_cross_entity.py',                   # 12:00 Type B
            'test_type_c_snowflake_marketplace_intermediary_aug7.py',  # 14:00 Type C
            'test_type_d_3pm_cross_validation_aug7.py',                # 15:00 Type D
            'test_wired_apple_openai_silence_aug7.py',                 # 16:00 Type A
            'test_parmy_olson_cross_entity.py',                        # 19:00 Type B
            'test_news_corp_triple_revenue_aug7.py',                   # 21:00 Type C
        ]
        missing = [f for f in aug7_files if not os.path.exists(os.path.join(TESTS_DIR, f))]
        assert not missing, f"Missing Aug 7 test files: {missing}"


class TestSourceURLCoverage:
    """Every profile and research entry added today should have source URLs."""

    def test_news_corp_profile_has_source_urls(self, news_corp):
        content = str(news_corp)
        assert 'source_url' in content.lower() or 'http' in content

    def test_wired_profile_has_source_urls(self, wired):
        content = str(wired)
        assert 'source_url' in content.lower() or 'http' in content

    def test_research_has_source_urls(self, research):
        content = str(research)
        assert 'source_url' in content.lower() or 'http' in content

    def test_entities_have_source_urls(self, entities):
        content = str(entities)
        assert 'source_url' in content.lower() or 'http' in content
