"""
Type D Cross-Validation — 08:00 PM Aug 21, 2026 (Iteration #231)

Tests fixes applied during this iteration:
1. Mechanism #218 confounders→confounding_factors field rename (dict→string format)
2. Stale highest-mechanism assertions updated #216→#220 in two prior Type D files
3. PetaPixel test confounder accessor updated from dict to string format
4. Doc sync: 2 missing test files added to ARCHITECTURE.md, 1 to README.md
5. Type rotation guard extended to #217-#220
"""
import os
import re
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
DOCS_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs')
TESTS_DIR = os.path.dirname(__file__)


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


def find_all_mechanisms(data, results=None):
    """Recursively find all mechanism entries."""
    if results is None:
        results = {}
    if isinstance(data, dict):
        if 'mechanism_id' in data:
            mid = data['mechanism_id']
            if isinstance(mid, int):
                results[mid] = data
        for v in data.values():
            find_all_mechanisms(v, results)
    elif isinstance(data, list):
        for item in data:
            find_all_mechanisms(item, results)
    return results


@pytest.fixture(scope='module')
def competitor_research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def all_mechanisms(competitor_research):
    return find_all_mechanisms(competitor_research)


class TestMechanism218FieldFix:
    """Verify mechanism #218 confounders→confounding_factors rename completed."""

    def test_218_has_confounding_factors(self, all_mechanisms):
        assert 218 in all_mechanisms
        assert 'confounding_factors' in all_mechanisms[218], \
            "Mechanism #218 should have confounding_factors field"

    def test_218_no_confounders_field(self, all_mechanisms):
        assert 'confounders' not in all_mechanisms[218], \
            "Mechanism #218 should NOT have confounders field (renamed)"

    def test_218_confounding_factors_are_strings(self, all_mechanisms):
        cf = all_mechanisms[218].get('confounding_factors', [])
        assert len(cf) >= 5, f"Expected ≥5 confounders, got {len(cf)}"
        for i, item in enumerate(cf):
            assert isinstance(item, str), \
                f"confounding_factors[{i}] should be string, got {type(item)}"

    def test_218_confounding_factors_have_severity_prefix(self, all_mechanisms):
        cf = all_mechanisms[218].get('confounding_factors', [])
        for item in cf:
            assert re.match(r'^\[(STRONG|MODERATE|WEAK)\]', item), \
                f"Missing [SEVERITY] prefix: {item[:60]}"

    def test_218_has_2_strong_confounders(self, all_mechanisms):
        cf = all_mechanisms[218].get('confounding_factors', [])
        strong = [c for c in cf if c.startswith('[STRONG]')]
        assert len(strong) >= 2, f"Expected ≥2 STRONG confounders, got {len(strong)}"


class TestNoConfoundersFieldInRecent:
    """Ensure all mechanisms #214+ use confounding_factors, not confounders."""

    def test_recent_mechanisms_use_confounding_factors(self, all_mechanisms):
        for mid, mech in all_mechanisms.items():
            if mid >= 214:
                assert 'confounders' not in mech, \
                    f"Mechanism #{mid} uses 'confounders' — should be 'confounding_factors'"

    def test_recent_confounding_factors_are_strings(self, all_mechanisms):
        for mid, mech in all_mechanisms.items():
            if mid >= 214 and 'confounding_factors' in mech:
                for i, item in enumerate(mech['confounding_factors']):
                    assert isinstance(item, str), \
                        f"Mechanism #{mid} confounding_factors[{i}] is {type(item)}, expected str"


class TestHighestMechanismUpdated:
    """Verify highest mechanism is #220."""

    def test_highest_mechanism_is_220(self, all_mechanisms):
        max_id = max(all_mechanisms.keys())
        assert max_id == 220, f"Expected highest mechanism #220, got #{max_id}"

    def test_no_gaps_217_to_220(self, all_mechanisms):
        for mid in range(217, 221):
            assert mid in all_mechanisms, f"Missing mechanism #{mid}"


class TestTypeRotation217To220:
    """Verify type rotation for mechanisms #217-#220."""

    EXPECTED_ROTATION = {
        217: 'E',  # Podcast sentiment (Rabbit Hole + Kmart)
        218: 'A',  # Competitor deep dive (PetaPixel)
        219: 'B',  # Journalist cross-entity (James Pero)
        220: 'C',  # Financial incentive (Yahoo/Apollo)
    }

    def test_rotation_types_match(self, all_mechanisms):
        for mid, expected_type in self.EXPECTED_ROTATION.items():
            assert all_mechanisms[mid].get('type') == expected_type, \
                f"Mechanism #{mid} type={all_mechanisms[mid].get('type')}, expected {expected_type}"

    def test_all_have_discovery_date_aug21(self, all_mechanisms):
        for mid in range(217, 221):
            dd = all_mechanisms[mid].get('discovery_date', '')
            assert dd == '2026-08-21', \
                f"Mechanism #{mid} discovery_date={dd}, expected 2026-08-21"

    def test_all_have_asymmetry_scores(self, all_mechanisms):
        for mid in range(217, 221):
            score = all_mechanisms[mid].get('asymmetry_score')
            assert isinstance(score, (int, float)) and 0 <= score <= 1, \
                f"Mechanism #{mid} asymmetry_score={score}, expected 0-1 float"


class TestDocCountSync:
    """Verify doc counts match actual test file count."""

    def test_actual_count_is_526(self):
        actual = len([f for f in os.listdir(TESTS_DIR)
                      if f.startswith('test_') and f.endswith('.py')])
        # 525 existing + 1 this file = 526
        assert actual == 526, f"Expected 526 test files, got {actual}"

    def test_readme_mentions_all_aug21_test_files(self):
        with open(os.path.join(PROFILES_DIR, '..', 'README.md')) as f:
            readme = f.read()
        aug21_files = [f for f in os.listdir(TESTS_DIR)
                       if f.startswith('test_') and f.endswith('.py') and 'aug21' in f]
        missing = [f for f in aug21_files if f not in readme]
        # Exclude this very file since we're testing it during creation
        missing = [f for f in missing if f != 'test_type_d_8pm_cross_validation_aug21.py']
        assert len(missing) == 0, f"Missing from README: {missing}"

    def test_architecture_mentions_all_aug21_test_files(self):
        with open(os.path.join(DOCS_DIR, 'ARCHITECTURE.md')) as f:
            arch = f.read()
        aug21_files = [f for f in os.listdir(TESTS_DIR)
                       if f.startswith('test_') and f.endswith('.py') and 'aug21' in f]
        missing = [f for f in aug21_files if f not in arch]
        # Exclude this very file since we're testing it during creation
        missing = [f for f in missing if f != 'test_type_d_8pm_cross_validation_aug21.py']
        assert len(missing) == 0, f"Missing from ARCHITECTURE.md: {missing}"


class TestYAMLIntegrity:
    """Verify all profile YAMLs parse without errors."""

    def test_competitor_research_yaml_valid(self):
        data = load_yaml('competitor-coverage-research.yaml')
        assert data is not None
        assert isinstance(data, dict)

    def test_competitor_entities_yaml_valid(self):
        data = load_yaml('competitor-entities.yaml')
        assert data is not None

    def test_all_profile_yamls_parse(self):
        for f in os.listdir(PROFILES_DIR):
            if f.endswith('.yaml'):
                try:
                    load_yaml(f)
                except Exception as e:
                    pytest.fail(f"{f} failed to parse: {e}")
