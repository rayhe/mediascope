"""Type D cross-validation — Aug 13, 1 AM PT

Validates data integrity fixes from iteration 78:
1. Mechanisms #60-76 all have test_file and date_added fields
2. Stale hardcoded assertions in prior cross-validation tests are fixed
3. count_stats.py class-level parametrize variable resolution
4. Mechanism ID contiguity across cross_publication_findings + aggregate_findings
5. README/ARCHITECTURE stat agreement with count_stats --pytest
"""

import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)


def read_file(name):
    with open(os.path.join(REPO_ROOT, name)) as f:
        return f.read()


def load_research():
    with open(os.path.join(REPO_ROOT, 'profiles', 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_research()


@pytest.fixture(scope='module')
def cpf(research):
    return research.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def agg(research):
    return research.get('aggregate_findings', {})


@pytest.fixture(scope='module')
def all_mechanism_ids(cpf, agg):
    ids = set()
    for section in (cpf, agg):
        for key, m in section.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if isinstance(mid, int):
                    ids.add(mid)
    return ids


# ===================================================================
# 1. MECHANISM FIELD COMPLETENESS (#60-76)
# ===================================================================

class TestMechanismFieldCompleteness:
    """All mechanisms #60+ must have test_file and date_added."""

    def test_all_cpf_mechanisms_have_test_file(self, cpf):
        missing = []
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if mid >= 60 and ('test_file' not in m or not m['test_file']):
                    missing.append(f"#{mid} ({key})")
        assert not missing, f"CPF mechanisms missing test_file: {missing}"

    def test_all_cpf_mechanisms_have_date_added(self, cpf):
        missing = []
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                if 'date_added' not in m:
                    missing.append(f"#{m['mechanism_id']} ({key})")
        assert not missing, f"CPF mechanisms missing date_added: {missing}"

    def test_all_test_files_exist_on_disk(self, cpf):
        missing = []
        for key, m in cpf.items():
            if isinstance(m, dict) and 'test_file' in m and m['test_file']:
                tf = m['test_file']
                path = os.path.join(REPO_ROOT, tf)
                if not os.path.exists(path):
                    missing.append(f"#{m.get('mechanism_id', '?')}: {tf}")
        assert not missing, f"Test files referenced but missing: {missing}"

    @pytest.mark.parametrize("mid", list(range(60, 77)))
    def test_mechanism_exists_in_yaml(self, all_mechanism_ids, mid):
        assert mid in all_mechanism_ids, f"Mechanism #{mid} not found in cpf or agg"


# ===================================================================
# 2. MECHANISM ID CONTIGUITY (ACROSS BOTH SECTIONS)
# ===================================================================

class TestMechanismIDContiguity:
    """No gaps in mechanism IDs when combining cpf + agg."""

    def test_no_gaps_17_to_max(self, all_mechanism_ids):
        max_id = max(all_mechanism_ids)
        expected = set(range(17, max_id + 1))
        missing = expected - all_mechanism_ids
        assert not missing, f"Missing mechanism IDs in range 17-{max_id}: {missing}"

    def test_max_is_at_least_76(self, all_mechanism_ids):
        assert max(all_mechanism_ids) >= 76

    def test_no_duplicates_between_cpf_and_agg(self, cpf, agg):
        """A mechanism ID should not appear in BOTH cpf and agg."""
        cpf_ids = {m['mechanism_id'] for m in cpf.values()
                   if isinstance(m, dict) and 'mechanism_id' in m}
        agg_ids = {m['mechanism_id'] for m in agg.values()
                   if isinstance(m, dict) and 'mechanism_id' in m}
        dupes = cpf_ids & agg_ids
        assert not dupes, f"Mechanism IDs in both cpf AND agg: {dupes}"


# ===================================================================
# 3. COUNT_STATS CLASS-LEVEL PARAMETRIZE FIX
# ===================================================================

class TestCountStatsParametrizeFix:
    """Verify count_stats regex handles class-level variable parametrize."""

    def test_regex_closer_to_pytest(self):
        """Regex count should be within 2% of pytest --collect-only."""
        result = subprocess.run(
            [sys.executable, 'scripts/count_stats.py'],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        regex_match = re.search(r'Total tests\s+(\d+)', result.stdout)
        assert regex_match
        regex_count = int(regex_match.group(1))

        result2 = subprocess.run(
            [sys.executable, '-m', 'pytest', 'tests/', '--collect-only', '-q', '--no-header'],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        last_line = result2.stdout.strip().split('\n')[-1]
        pytest_match = re.search(r'(\d+) tests? collected', last_line)
        assert pytest_match
        pytest_count = int(pytest_match.group(1))

        pct_diff = abs(pytest_count - regex_count) / pytest_count
        assert pct_diff < 0.02, \
            f"Regex ({regex_count}) vs pytest ({pytest_count}): {pct_diff:.1%} gap exceeds 2% threshold"

    def test_class_level_variable_resolved(self):
        """Class-level parametrize variables should be counted."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "count_stats", os.path.join(REPO_ROOT, "scripts/count_stats.py"))
        cs = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cs)

        # Simulate class-level variable
        content = '''
class TestFoo:
    MY_ITEMS = [
        "a",
        "b",
        "c",
    ]

    @pytest.mark.parametrize("item", MY_ITEMS)
    def test_something(self, item):
        pass
'''
        result = cs._resolve_variable_list("MY_ITEMS", content)
        assert result == 3, f"Expected 3 items from class-level var, got {result}"


# ===================================================================
# 4. README / ARCHITECTURE STAT AGREEMENT
# ===================================================================

class TestStatAgreement:
    """README and ARCHITECTURE should agree on key stats."""

    def test_test_count_agreement(self):
        readme = read_file('README.md')
        arch = read_file('docs/ARCHITECTURE.md')
        readme_match = re.search(r'\*\*(\d+) tests?\*\*', readme)
        arch_match = re.search(r'(\d+) tests? across', arch)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"

    def test_test_file_count_agreement(self):
        readme = read_file('README.md')
        arch = read_file('docs/ARCHITECTURE.md')
        readme_match = re.search(r'(\d+) test files', readme)
        arch_match = re.search(r'(\d+) test files', arch)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"

    def test_readme_test_count_matches_pytest(self):
        readme = read_file('README.md')
        readme_match = re.search(r'\*\*(\d+) tests?\*\*', readme)
        assert readme_match
        readme_count = int(readme_match.group(1))

        result = subprocess.run(
            [sys.executable, '-m', 'pytest', 'tests/', '--collect-only', '-q', '--no-header'],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        last_line = result.stdout.strip().split('\n')[-1]
        pytest_match = re.search(r'(\d+) tests? collected', last_line)
        assert pytest_match
        pytest_count = int(pytest_match.group(1))

        # Allow some slack since new tests may have been added since last README update
        assert abs(readme_count - pytest_count) <= pytest_count * 0.01, \
            f"README ({readme_count}) vs pytest ({pytest_count}): >1% drift"


# ===================================================================
# 5. PRIOR FIX STABILITY
# ===================================================================

class TestPriorFixesStable:
    """Regressions caught by prior Type D runs should stay fixed."""

    def test_mechanism_58_not_in_publications(self, research):
        """Mechanism #58 was misplaced in publications (fixed iteration 58)."""
        pubs = research.get('publications', {})
        for key, val in pubs.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 58:
                pytest.fail(f"Mechanism #58 still in publications under key '{key}'")

    def test_mechanism_60_61_no_cross_contamination(self, cpf):
        """Mechanisms #60 and #61 had swapped confounding_factors (fixed iteration 62)."""
        m60 = m61 = None
        for key, m in cpf.items():
            if isinstance(m, dict):
                if m.get('mechanism_id') == 60:
                    m60 = m
                elif m.get('mechanism_id') == 61:
                    m61 = m
        assert m60 and m61
        # #60 (Karen Hao) should reference Seetharaman (#57)
        xrefs_60 = str(m60.get('cross_references', ''))
        assert '57' in xrefs_60 or 'seetharaman' in xrefs_60.lower(), \
            "Mechanism #60 should cross-reference #57 (Seetharaman)"
        # #61 (Apple News+) should NOT reference Seetharaman
        xrefs_61 = str(m61.get('cross_references', ''))
        assert 'seetharaman' not in xrefs_61.lower(), \
            "Mechanism #61 should NOT cross-reference Seetharaman (that's #60's)"

    def test_no_mechanism_in_publications(self, research):
        """No mechanism_id should appear in publications section."""
        pubs = research.get('publications', {})
        found = []
        for key, val in pubs.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                found.append(f"#{val['mechanism_id']} in {key}")
        assert not found, f"Mechanisms in publications: {found}"
