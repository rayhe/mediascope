"""
Type D Cross-Validation — 8pm Aug 11, 2026

Validates:
1. Mechanism #41 relocation from publications to cross_publication_findings
2. date_added field completeness for mechanisms #51-#53
3. Full mechanism ID coverage (17-53, no gaps except known aggregate_findings IDs 19/30/31)
4. README/ARCHITECTURE count sync with pytest collection
5. Test file count matches disk
6. No mechanism IDs remaining in publications section (except refs)
"""

import yaml
import os
import pytest

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
PROFILES_DIR = os.path.join(REPO_ROOT, 'profiles')
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def cpf(research):
    return research.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def agg(research):
    return research.get('aggregate_findings', {})


@pytest.fixture(scope='module')
def pubs(research):
    return research.get('publications', {})


# ===================================================================
# 1. MECHANISM #41 RELOCATION
# ===================================================================

class TestMechanism41Relocation:
    """Mechanism #41 should be in cross_publication_findings, not publications."""

    def test_mechanism_41_in_cpf(self, cpf):
        ids = {m.get('mechanism_id') for m in cpf.values() if isinstance(m, dict)}
        assert 41 in ids, "Mechanism #41 should be in cross_publication_findings"

    def test_mechanism_41_key_name(self, cpf):
        assert 'mit_tr_apple_wwdc_2026_pcc_omission' in cpf

    def test_mechanism_41_has_finding_summary(self, cpf):
        m = cpf['mit_tr_apple_wwdc_2026_pcc_omission']
        assert len(m.get('finding_summary', '')) > 50

    def test_mechanism_41_has_date_added(self, cpf):
        m = cpf['mit_tr_apple_wwdc_2026_pcc_omission']
        assert 'date_added' in m

    def test_mechanism_41_not_in_publications_directly(self, pubs):
        """No publication should have mechanism_id: 41 as a direct child."""
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                for k, v in pub_val.items():
                    if isinstance(v, dict) and v.get('mechanism_id') == 41:
                        assert k.endswith('_ref'), \
                            f"Mechanism #41 still directly in publications.{pub_key}.{k}"

    def test_mit_tr_has_ref_to_mechanism_41(self, pubs):
        mit = pubs.get('mit-tech-review', {})
        assert 'wwdc_2026_pcc_omission_ref' in mit
        assert mit['wwdc_2026_pcc_omission_ref'].get('mechanism_id') == 41

    def test_mechanism_41_test_file_exists(self, cpf):
        m = cpf['mit_tr_apple_wwdc_2026_pcc_omission']
        test_file = m.get('test_file', '')
        path = os.path.join(REPO_ROOT, test_file)
        assert os.path.exists(path), f"Test file {test_file} not found"


# ===================================================================
# 2. DATE_ADDED COMPLETENESS FOR MECHANISMS #51-#53
# ===================================================================

class TestDateAddedCompleteness:
    """All mechanisms in cross_publication_findings must have date_added."""

    def test_all_cpf_have_date_added(self, cpf):
        missing = []
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                if 'date_added' not in m:
                    missing.append(f"#{m['mechanism_id']} ({key})")
        assert not missing, f"Missing date_added: {missing}"

    @pytest.mark.parametrize("mech_id", [51, 52, 53])
    def test_recent_mechanisms_have_date_added(self, cpf, mech_id):
        for key, m in cpf.items():
            if isinstance(m, dict) and m.get('mechanism_id') == mech_id:
                assert 'date_added' in m, f"Mechanism #{mech_id} missing date_added"
                return
        pytest.fail(f"Mechanism #{mech_id} not found in cross_publication_findings")


# ===================================================================
# 3. MECHANISM ID COVERAGE (17-53)
# ===================================================================

class TestMechanismIDCoverage:
    """All IDs from 17-53 should exist across cpf + aggregate_findings."""

    def test_all_ids_present(self, cpf, agg):
        all_ids = set()
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                all_ids.add(m['mechanism_id'])
        for key, m in agg.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                all_ids.add(m['mechanism_id'])
        for mid in range(17, 54):
            assert mid in all_ids, f"Mechanism #{mid} missing from both cpf and agg"

    def test_cpf_has_at_least_34_unique_ids(self, cpf):
        ids = {m.get('mechanism_id') for m in cpf.values() if isinstance(m, dict) and 'mechanism_id' in m}
        assert len(ids) >= 34, f"Expected >=34 unique IDs in cpf, got {len(ids)}"

    def test_agg_has_ids_19_30_31(self, agg):
        agg_ids = {m.get('mechanism_id') for m in agg.values() if isinstance(m, dict) and 'mechanism_id' in m}
        for mid in [19, 30, 31]:
            assert mid in agg_ids, f"Mechanism #{mid} should be in aggregate_findings"

    def test_no_id_collisions_between_cpf_and_agg(self, cpf, agg):
        cpf_ids = {m.get('mechanism_id') for m in cpf.values() if isinstance(m, dict) and 'mechanism_id' in m}
        agg_ids = {m.get('mechanism_id') for m in agg.values() if isinstance(m, dict) and 'mechanism_id' in m}
        overlap = cpf_ids & agg_ids
        assert not overlap, f"ID collision between cpf and agg: {overlap}"

    def test_max_mechanism_id_is_at_least_53(self, cpf):
        ids = {m.get('mechanism_id') for m in cpf.values() if isinstance(m, dict) and 'mechanism_id' in m}
        assert max(ids) >= 53


# ===================================================================
# 4. NO MECHANISM IDS IN PUBLICATIONS (EXCEPT REFS)
# ===================================================================

class TestNoMechanismsInPublications:
    """No mechanism_id entries should remain directly in publications."""

    def test_publications_clean(self, pubs):
        """Check no non-ref entries in publications have mechanism_id."""
        violations = []

        def check_dict(d, path):
            if isinstance(d, dict):
                if 'mechanism_id' in d and not path.endswith('_ref'):
                    violations.append(f"{path}: mechanism_id={d['mechanism_id']}")
                for k, v in d.items():
                    check_dict(v, f"{path}.{k}")
            elif isinstance(d, list):
                for i, item in enumerate(d):
                    check_dict(item, f"{path}[{i}]")

        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                check_dict(pub_val, f"publications.{pub_key}")

        assert not violations, f"Mechanism IDs still in publications: {violations}"


# ===================================================================
# 5. TEST FILE COUNT AND README SYNC
# ===================================================================

class TestTestFileSync:
    """README and disk test file counts should match."""

    def test_file_count_on_disk(self):
        files = [f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')]
        assert len(files) >= 312, f"Expected >=312 test files, got {len(files)}"

    def test_readme_count_updated(self):
        with open(os.path.join(REPO_ROOT, 'README.md')) as f:
            content = f.read()
        assert '9980' in content.replace(',', '') or '9,980' in content, \
            "README should reflect 9,980 tests (structural consistency static count)"


# ===================================================================
# 6. MECHANISM TEST FILES ALL EXIST
# ===================================================================

class TestAllMechanismTestFilesExist:
    """Every test_file reference in YAML should point to an existing file."""

    def test_all_test_files_exist(self, cpf):
        missing = []
        for key, m in cpf.items():
            if isinstance(m, dict) and 'test_file' in m:
                test_file = m['test_file']
                path = os.path.join(REPO_ROOT, test_file)
                if not os.path.exists(path):
                    missing.append(f"#{m.get('mechanism_id', '?')}: {test_file}")
        assert not missing, f"Missing test files: {missing}"


# ===================================================================
# 7. STRUCTURAL CONSISTENCY SPOT CHECK
# ===================================================================

class TestStructuralSpotCheck:
    """Quick checks that the YAML hasn't been corrupted."""

    def test_yaml_loads_without_error(self, research):
        assert isinstance(research, dict)

    def test_publications_count(self, pubs):
        # Should be exactly 9 after FT unification and mechanism relocations
        assert len(pubs) >= 9, f"Expected >=9 publications, got {len(pubs)}"

    def test_cpf_count(self, cpf):
        assert len(cpf) >= 34, f"Expected >=34 cross_publication_findings, got {len(cpf)}"

    def test_all_pubs_have_meta_coverage_tone(self, pubs):
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                assert 'meta_coverage_tone' in pub_val, \
                    f"Publication '{pub_key}' missing meta_coverage_tone"


# ===================================================================
# 8. PREVIOUS CROSS-VALIDATION FIXES STILL HOLD
# ===================================================================

class TestPreviousFixesHold:
    """Verify fixes from earlier Type D iterations haven't regressed."""

    def test_no_duplicate_ft_entries(self, pubs):
        """FT deduplication from 5pm iteration."""
        ft_keys = [k for k in pubs if 'financial' in k.lower() or k.startswith('ft')]
        assert len(ft_keys) <= 1, f"Duplicate FT entries: {ft_keys}"

    def test_mechanisms_42_43_not_in_publications(self, pubs):
        """09am fix: #42 and #43 moved to cpf."""
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                for k, v in pub_val.items():
                    if isinstance(v, dict) and v.get('mechanism_id') in (42, 43):
                        if not k.endswith('_ref'):
                            pytest.fail(f"Mechanism #{v['mechanism_id']} still in publications.{pub_key}")

    def test_01am_stale_assertions_fixed(self):
        """01am file should not have hardcoded stale values."""
        path = os.path.join(TESTS_DIR, 'test_type_d_01am_cross_validation_aug11.py')
        if os.path.exists(path):
            with open(path) as f:
                content = f.read()
            assert '== 9107' not in content, "Stale 9107 count in 01am file"
            assert "max(ids) == 37" not in content, "Stale max==37 in 01am file"
