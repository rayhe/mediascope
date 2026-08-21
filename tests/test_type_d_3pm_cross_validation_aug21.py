"""
Type D cross-validation — Aug 21, 3 PM PT (Iteration #226)

Fixes applied:
1. confounders→confounding_factors field rename in competitor-coverage-research.yaml for mechanisms #214, #215
2. confounding_factors format normalization for #216 (STRONG: → [STRONG])
3. Mechanism #216 added to competitor-coverage-research.yaml publications
4. Highest mechanism test updated #212→#216 with type rotation guard for #213-#216
5. Doc count sync: ARCHITECTURE 516→520, README 518→520
6. 7 missing test files added to ARCHITECTURE.md and README.md
7. news-corp.yaml confounders→confounding_factors field rename for profile consistency
"""
import pytest
import yaml
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(scope="module")
def competitor_research():
    with open(os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def architecture():
    with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def readme():
    with open(os.path.join(REPO, "README.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def test_file_count():
    tests_dir = os.path.join(REPO, "tests")
    return len([f for f in os.listdir(tests_dir) if f.startswith("test_") and f.endswith(".py")])


# ============================================================
# Class 1: Confounding Factors Format Consistency
# ============================================================
class TestConfoundingFactorsFormat:
    """All mechanisms >= 205 should use confounding_factors (not confounders) with [STRENGTH] prefix."""

    def test_no_confounders_field_in_recent(self, competitor_research):
        """No mechanism >= 205 should have 'confounders' (should be 'confounding_factors')."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                assert 'confounders' not in val, \
                    f"Mechanism #{val.get('mechanism_id')} uses 'confounders' — should be 'confounding_factors'"

    def test_confounding_factors_are_strings(self, competitor_research):
        """All confounding factors should be strings, not dicts."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                for cf in val.get('confounding_factors', []):
                    assert isinstance(cf, str), \
                        f"Mechanism #{val.get('mechanism_id')} has dict confounding_factor — should be string"

    def test_confounding_factors_severity_prefix(self, competitor_research):
        """All confounding factors should start with [STRONG], [MODERATE], or [WEAK]."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id', 0) >= 205:
                for cf in val.get('confounding_factors', []):
                    assert any(cf.startswith(f'[{s}]') for s in ['STRONG', 'MODERATE', 'WEAK']), \
                        f"Mechanism #{val.get('mechanism_id')} factor missing [SEVERITY] prefix: {cf[:60]}..."

    def test_mechanisms_214_215_216_fixed(self, competitor_research):
        """Specifically verify #214, #215, #216 have correct format (the ones that were broken)."""
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') in [214, 215, 216]:
                mid = val['mechanism_id']
                cfs = val.get('confounding_factors', [])
                assert len(cfs) >= 3, f"Mechanism #{mid} should have >=3 confounding factors"
                for cf in cfs:
                    assert isinstance(cf, str), f"#{mid}: confounding_factor is not a string"
                    assert cf.startswith('['), f"#{mid}: factor doesn't start with '[': {cf[:40]}"


# ============================================================
# Class 2: Mechanism #216 Existence in competitor-coverage-research.yaml
# ============================================================
class TestMechanism216InResearch:
    """Mechanism #216 (Condé Nast Meta Reverse Personnel Flow) should be in competitor-coverage-research.yaml."""

    def test_mechanism_216_exists(self, competitor_research):
        pubs = competitor_research['publications']
        ids = [val.get('mechanism_id') for val in pubs.values() if isinstance(val, dict)]
        assert 216 in ids, "Mechanism #216 missing from competitor-coverage-research.yaml"

    def test_mechanism_216_is_type_c(self, competitor_research):
        pubs = competitor_research['publications']
        for val in pubs.values():
            if isinstance(val, dict) and val.get('mechanism_id') == 216:
                assert val['type'] == 'C', f"#216 type should be C, got {val['type']}"

    def test_mechanism_216_has_test_file(self, competitor_research):
        pubs = competitor_research['publications']
        for val in pubs.values():
            if isinstance(val, dict) and val.get('mechanism_id') == 216:
                tf = val.get('test_file', '')
                assert 'aug21' in tf, f"#216 test file should reference aug21: {tf}"

    def test_mechanism_216_score_ambiguous(self, competitor_research):
        pubs = competitor_research['publications']
        for val in pubs.values():
            if isinstance(val, dict) and val.get('mechanism_id') == 216:
                score = val.get('asymmetry_score', 0)
                assert 0.3 <= score <= 0.6, f"#216 ambiguous score expected 0.3-0.6, got {score}"

    def test_highest_mechanism_is_216(self, competitor_research):
        pubs = competitor_research['publications']
        max_id = max(
            val.get('mechanism_id', 0)
            for val in pubs.values()
            if isinstance(val, dict)
        )
        assert max_id == 216, f"Expected highest mechanism #216, got #{max_id}"


# ============================================================
# Class 3: Doc Count Sync
# ============================================================
class TestDocCountSync:
    """ARCHITECTURE.md and README.md file counts match actual test file count."""

    def test_architecture_count_matches(self, architecture, test_file_count):
        m = re.search(r'(\d+)\s+test files', architecture)
        assert m, "ARCHITECTURE.md missing test file count"
        assert int(m.group(1)) == test_file_count, \
            f"ARCHITECTURE says {m.group(1)} but actual is {test_file_count}"

    def test_readme_table_count_matches(self, readme, test_file_count):
        m = re.search(r'Across\s+(\d+)\s+test files', readme)
        assert m, "README.md missing test file count in table"
        assert int(m.group(1)) == test_file_count, \
            f"README table says {m.group(1)} but actual is {test_file_count}"

    def test_readme_body_count_matches(self, readme, test_file_count):
        m = re.search(r'across\s+(\d+)\s+test files', readme)
        assert m, "README.md missing test file count in body"
        assert int(m.group(1)) == test_file_count, \
            f"README body says {m.group(1)} but actual is {test_file_count}"


# ============================================================
# Class 4: Mechanism ID Contiguity #205-#216
# ============================================================
class TestMechanismContiguity:
    """All mechanism IDs from 205 to 216 should exist without gaps."""

    def test_no_gaps_205_to_216(self, competitor_research):
        pubs = competitor_research['publications']
        ids = set()
        for val in pubs.values():
            if isinstance(val, dict) and 'mechanism_id' in val:
                ids.add(val['mechanism_id'])
        for expected in range(205, 217):
            assert expected in ids, f"Mechanism #{expected} missing from publications"

    def test_type_rotation_213_to_216(self, competitor_research):
        """Mechanisms 213-216 should follow E, A, B, C rotation."""
        expected = {213: 'E', 214: 'A', 215: 'B', 216: 'C'}
        pubs = competitor_research['publications']
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') in expected:
                mid = val['mechanism_id']
                assert val['type'] == expected[mid], \
                    f"#{mid} type '{val['type']}' expected '{expected[mid]}'"


# ============================================================
# Class 5: New Test Files in Documentation
# ============================================================
class TestNewFilesDocumented:
    """Aug 21 iteration #223-#226 test files should be listed in docs."""

    AUG21_FILES = [
        'test_conde_nast_meta_reverse_personnel_cbo_france_financial_architecture_aug21.py',
        'test_mia_sato_cross_entity_camera_product_vocabulary_bifurcation_aug21.py',
        'test_news_corp_cross_publication_camera_wearable_vocabulary_asymmetry_aug21.py',
        'test_type_e_11am_vergecast_two_episode_camera_vocabulary_cascade_aug21.py',
        'test_wired_triple_reporter_apple_camera_airpods_leak_coverage_silence_aug21.py',
        'test_conde_nast_cro_career_migration_snap_personnel_financial_architecture_aug21.py',
    ]

    def test_all_in_architecture(self, architecture):
        for f in self.AUG21_FILES:
            assert f in architecture, f"ARCHITECTURE.md missing {f}"

    def test_all_in_readme(self, readme):
        for f in self.AUG21_FILES:
            assert f in readme, f"README.md missing {f}"
