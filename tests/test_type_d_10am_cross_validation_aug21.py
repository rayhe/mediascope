"""
Type D Cross-Validation — 10:00 AM Aug 21, 2026
Tests fixes applied during this iteration:
1. Added missing 'overview' field to mechanisms #209-#212
2. Validates all mechanisms >= 205 have required structural fields
3. Cross-validates mechanism counts, test corpus, and YAML integrity
4. Verifies recent three-entity camera wearable patterns are consistent
"""
import os
import re
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
DOCS_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs')
TESTS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='module')
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


# ============================================================
# Class 1: Overview Field Completeness Fix Validation
# ============================================================
class TestOverviewFieldFix:
    """Validate that mechanisms #209-#212 now have required 'overview' fields."""

    @pytest.mark.parametrize("mechanism_id", [209, 210, 211, 212])
    def test_mechanism_has_overview(self, competitor_research, mechanism_id):
        """Each mechanism #209-#212 should have an 'overview' field after fix."""
        pubs = competitor_research['publications']
        found = False
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == mechanism_id:
                found = True
                assert 'overview' in val, \
                    f"Mechanism #{mechanism_id} ({key}) still missing 'overview'"
                assert len(val['overview']) > 50, \
                    f"Mechanism #{mechanism_id} overview too short: {len(val['overview'])} chars"
                break
        assert found, f"Mechanism #{mechanism_id} not found in publications"

    def test_overview_not_copy_of_finding_summary(self, competitor_research):
        """Overview should not be identical to finding_summary."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 209:
                overview = val.get('overview', '')
                summary = val.get('finding_summary', '')
                if overview and summary:
                    assert overview != summary, \
                        f"Mechanism #{val['mechanism_id']} overview identical to finding_summary"


# ============================================================
# Class 2: All Recent Mechanisms Structural Completeness
# ============================================================
class TestRecentMechanismStructure:
    """Validate all mechanisms >= 205 have consistent structure."""

    REQUIRED_FIELDS = [
        'mechanism_id', 'name', 'type', 'discovery_date',
        'asymmetry_score', 'confounding_factors', 'overview'
    ]

    def test_all_recent_have_required_fields(self, competitor_research):
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                for field in self.REQUIRED_FIELDS:
                    assert field in val, \
                        f"Mechanism #{val.get('mechanism_id', '?')} ({key}) missing '{field}'"

    def test_asymmetry_scores_valid_range(self, competitor_research):
        """All asymmetry scores should be 0.0-1.0."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and 'asymmetry_score' in val:
                score = val['asymmetry_score']
                assert 0.0 <= score <= 1.0, \
                    f"Mechanism #{val.get('mechanism_id', '?')} score {score} out of range"

    def test_discovery_dates_are_2026(self, competitor_research):
        """All recent mechanisms should have 2026 discovery dates."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                date = val.get('discovery_date', '')
                assert date.startswith('2026-08'), \
                    f"Mechanism #{val.get('mechanism_id', '?')} date '{date}' not Aug 2026"

    def test_confounding_factors_have_severity(self, competitor_research):
        """Each confounding factor should start with [STRONG], [MODERATE], or [WEAK]."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                for factor in val.get('confounding_factors', []):
                    assert any(factor.startswith(f'[{s}]') for s in ['STRONG', 'MODERATE', 'WEAK']), \
                        f"Mechanism #{val.get('mechanism_id', '?')} factor missing severity: {factor[:60]}..."


# ============================================================
# Class 3: Mechanism ID Continuity
# ============================================================
class TestMechanismContinuity:
    """Verify mechanism IDs form a continuous sequence."""

    def test_no_gaps_in_recent_ids(self, competitor_research):
        pubs = competitor_research['publications']
        ids = sorted([
            val['mechanism_id']
            for val in pubs.values()
            if isinstance(val, dict) and 'mechanism_id' in val and val['mechanism_id'] >= 200
        ])
        if len(ids) >= 2:
            for i in range(1, len(ids)):
                assert ids[i] == ids[i - 1] + 1, \
                    f"Gap in mechanism IDs between #{ids[i - 1]} and #{ids[i]}"

    def test_highest_mechanism_is_212(self, competitor_research):
        pubs = competitor_research['publications']
        max_id = max(
            val.get('mechanism_id', 0)
            for val in pubs.values()
            if isinstance(val, dict)
        )
        assert max_id == 212, f"Expected highest mechanism #212, got #{max_id}"

    def test_mechanism_types_match_rotation(self, competitor_research):
        """Recent mechanisms should match the A/B/C/D/E rotation."""
        expected_types = {
            209: 'E',  # Podcast
            210: 'A',  # Competitor Coverage
            211: 'B',  # Journalist Cross-Entity
            212: 'C',  # Financial Incentive
        }
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') in expected_types:
                mid = val['mechanism_id']
                assert val['type'] == expected_types[mid], \
                    f"Mechanism #{mid} type '{val['type']}' expected '{expected_types[mid]}'"


# ============================================================
# Class 4: Three-Entity Camera Wearable Pattern Consistency
# ============================================================
class TestThreeEntityCameraPattern:
    """Validate the emerging three-entity camera wearable coverage pattern."""

    def test_perez_three_entity_has_all_entities(self, competitor_research):
        pubs = competitor_research['publications']
        entry = pubs.get('sarah_perez_three_entity_camera_wearable_reputation_shield', {})
        entities = entry.get('entity', '')
        for company in ['Apple', 'Google', 'Meta']:
            assert company in entities, f"Perez three-entity missing {company}"

    def test_pero_three_entity_has_all_entities(self, competitor_research):
        pubs = competitor_research['publications']
        entry = pubs.get('james_pero_three_entity_apple_reputational_credit_privacy_gradient', {})
        entities = entry.get('entity', '')
        for company in ['Apple', 'Google', 'Meta']:
            assert company in entities, f"Pero three-entity missing {company}"

    def test_three_entity_scores_above_threshold(self, competitor_research):
        """Three-entity mechanisms should show high asymmetry (>= 0.85)."""
        pubs = competitor_research['publications']
        three_entity_keys = [
            'sarah_perez_three_entity_camera_wearable_reputation_shield',
            'james_pero_three_entity_apple_reputational_credit_privacy_gradient',
        ]
        for key in three_entity_keys:
            entry = pubs.get(key, {})
            score = entry.get('asymmetry_score', 0)
            assert score >= 0.85, \
                f"{key} score {score} below 0.85 threshold for three-entity pattern"

    def test_three_entity_cross_reference_each_other(self, competitor_research):
        """Mechanisms #210 and #211 should cross-reference related mechanisms."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') in [210, 211]:
                refs = val.get('cross_references', [])
                assert len(refs) >= 3, \
                    f"Mechanism #{val['mechanism_id']} has only {len(refs)} cross-refs, expected >= 3"


# ============================================================
# Class 5: Test Corpus File Count Validation
# ============================================================
class TestCorpusIntegrity:
    """Verify test corpus counts and file references."""

    def test_aug21_test_files_exist(self):
        """All aug21 test files should exist."""
        aug21_files = [f for f in os.listdir(TESTS_DIR) if 'aug21' in f and f.endswith('.py')]
        assert len(aug21_files) >= 10, \
            f"Expected >= 10 aug21 test files, found {len(aug21_files)}"

    def test_all_referenced_test_files_exist(self, competitor_research):
        """Every test_file referenced in mechanisms >= 205 should exist on disk."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                test_file = val.get('test_file', '')
                if test_file:
                    full_path = os.path.join(TESTS_DIR, os.path.basename(test_file))
                    assert os.path.exists(full_path), \
                        f"Mechanism #{val['mechanism_id']} references missing file: {test_file}"

    def test_total_test_file_count_at_least_515(self):
        """Corpus should have >= 515 test files."""
        test_files = [f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')]
        assert len(test_files) >= 515, \
            f"Expected >= 515 test files, found {len(test_files)}"


# ============================================================
# Class 6: YAML Integrity
# ============================================================
class TestYAMLIntegrity:
    """Verify all profile YAML files parse cleanly."""

    def test_competitor_research_yaml_valid(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        assert 'publications' in data
        assert isinstance(data['publications'], dict)

    def test_competitor_entities_yaml_valid(self):
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)

    def test_all_profile_yamls_parse(self):
        """Every .yaml file in profiles/ should parse without error."""
        for fname in os.listdir(PROFILES_DIR):
            if fname.endswith('.yaml'):
                path = os.path.join(PROFILES_DIR, fname)
                with open(path) as f:
                    data = yaml.safe_load(f)
                assert data is not None, f"Profile {fname} parsed as None"
