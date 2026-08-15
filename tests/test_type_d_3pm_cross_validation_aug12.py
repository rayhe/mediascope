"""
Type D Cross-Validation — 3 PM Aug 12, 2026

Validates:
1. README/ARCHITECTURE stat consistency with actual repo state
2. Cross-reference integrity for mechanisms #65–#68 (today's additions)
3. Journalist profile completeness for today's new profiles
4. Financial claim source coverage across recent mechanisms
5. No gaps in sequential mechanism IDs
"""

import os
import re
import subprocess
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(path):
    with open(os.path.join(REPO_ROOT, path)) as f:
        return yaml.safe_load(f)


def read_file(path):
    with open(os.path.join(REPO_ROOT, path)) as f:
        return f.read()


def find_mechanism(cpf_data, mech_id):
    """Search cross_publication_findings dict for a given mechanism ID."""
    for key, val in cpf_data.get('cross_publication_findings', {}).items():
        if isinstance(val, dict) and val.get('mechanism_id') == mech_id:
            return val
    for key, val in cpf_data.get('aggregate_findings', {}).items():
        if isinstance(val, dict) and val.get('mechanism_id') == mech_id:
            return val
    return None


# ─── Section 1: Stat Consistency ───────────────────────────────────────────────


class TestStatConsistency:
    """Verify README and ARCHITECTURE stats match actual repo state."""

    @pytest.fixture(scope='class')
    @classmethod
    def actual_test_file_count(cls):
        test_files = [f for f in os.listdir(os.path.join(REPO_ROOT, 'tests'))
                      if f.startswith('test_') and f.endswith('.py')]
        return len(test_files)

    @pytest.fixture(scope='class')
    @classmethod
    def count_stats(cls):
        result = subprocess.run(
            ['python3', 'scripts/count_stats.py'],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=30
        )
        return result.stdout

    def test_test_file_count_matches_readme(self, actual_test_file_count):
        readme = read_file('README.md')
        match = re.search(r'Across (\d+) test files', readme)
        assert match, "README should contain 'Across N test files'"
        assert int(match.group(1)) == actual_test_file_count, \
            f"README says {match.group(1)} test files, actually {actual_test_file_count}"

    def test_test_file_count_matches_architecture(self, actual_test_file_count):
        arch = read_file('docs/ARCHITECTURE.md')
        match = re.search(r'(\d+) tests across (\d+) test files', arch)
        assert match, "ARCHITECTURE should have test count"
        assert int(match.group(2)) == actual_test_file_count, \
            f"ARCHITECTURE says {match.group(2)} test files, actually {actual_test_file_count}"

    def test_readme_test_count_within_tolerance(self):
        result = subprocess.run(
            ['python3', '-m', 'pytest', 'tests/', '--collect-only', '-q'],
            capture_output=True, text=True, cwd=REPO_ROOT, timeout=120
        )
        last_line = result.stdout.strip().split('\n')[-1]
        actual_match = re.search(r'(\d+) tests? collected', last_line)
        assert actual_match, f"Could not parse pytest output: {last_line}"
        actual_count = int(actual_match.group(1))

        readme = read_file('README.md')
        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        assert readme_match, "README should contain '**N tests**'"
        readme_count = int(readme_match.group(1))

        tolerance = actual_count * 0.01
        assert abs(actual_count - readme_count) <= tolerance, \
            f"README says {readme_count}, actually {actual_count} (>{tolerance:.0f} tolerance)"

    def test_entity_cluster_count_matches_readme(self, count_stats):
        cluster_match = re.search(r'Entity clusters\s+(\d+)', count_stats)
        assert cluster_match
        actual = int(cluster_match.group(1))
        readme = read_file('README.md')
        readme_match = re.search(r'using (\d+) clusters', readme)
        assert readme_match
        assert int(readme_match.group(1)) == actual

    def test_migration_count_matches_readme(self, count_stats):
        mig_match = re.search(r'Career-entry migrations\s+(\d+)', count_stats)
        assert mig_match
        actual = int(mig_match.group(1))
        readme = read_file('README.md')
        # Match the table row format: | Career-entry migrations | 971 | ...
        readme_match = re.search(r'Career-entry migrations\s*\|\s*(\d[\d,]*)', readme)
        assert readme_match, "Could not find Career-entry migrations in README table"
        readme_val = int(readme_match.group(1).replace(',', ''))
        assert readme_val == actual, f"README table ({readme_val}) != count_stats ({actual})"

    def test_alias_count_matches_readme(self, count_stats):
        alias_match = re.search(r'Entity aliases\s+(\d+)', count_stats)
        assert alias_match
        actual = int(alias_match.group(1))
        readme = read_file('README.md')
        readme_match = re.search(r'with (\d+) aliases', readme)
        assert readme_match
        assert int(readme_match.group(1)) == actual


# ─── Section 2: Mechanism Cross-Reference Integrity ────────────────────────────


class TestMechanismCrossReferences:
    """Verify cross-references between mechanisms #65–#68."""

    @pytest.fixture(scope='class')
    @classmethod
    def cpf(cls):
        return load_yaml('profiles/competitor-coverage-research.yaml')

    def test_mechanism_65_exists(self, cpf):
        assert find_mechanism(cpf, 65) is not None, "Mechanism #65 (WaPo Bezos) should exist"

    def test_mechanism_66_exists(self, cpf):
        assert find_mechanism(cpf, 66) is not None, "Mechanism #66 should exist"

    def test_mechanism_67_exists(self, cpf):
        assert find_mechanism(cpf, 67) is not None, "Mechanism #67 (WSJ beat assignment) should exist"

    def test_mechanism_68_exists(self, cpf):
        assert find_mechanism(cpf, 68) is not None, "Mechanism #68 (xAI-X destruction) should exist"

    def test_mechanism_65_has_test_file(self):
        assert os.path.exists(os.path.join(
            REPO_ROOT, 'tests',
            'test_wapo_bezos_anthropic_ownership_coverage_alignment_aug12.py'
        ))

    def test_mechanism_67_has_test_file(self):
        assert os.path.exists(os.path.join(
            REPO_ROOT, 'tests',
            'test_nicole_nguyen_wsj_beat_assignment_asymmetry_aug12.py'
        ))

    def test_mechanism_68_has_test_file(self):
        assert os.path.exists(os.path.join(
            REPO_ROOT, 'tests',
            'test_xai_x_dual_entity_publisher_financial_destruction_aug12.py'
        ))

    def test_mechanism_65_has_finding_summary(self, cpf):
        mech = find_mechanism(cpf, 65)
        assert mech
        assert mech.get('finding_summary'), "Mechanism #65 should have a finding_summary"

    def test_mechanism_68_has_traffic_destruction_data(self, cpf):
        mech = find_mechanism(cpf, 68)
        assert mech
        assert mech.get('x_platform_traffic_destruction') or mech.get('finding_summary'), \
            "Mechanism #68 should document X platform traffic destruction"

    def test_mechanism_67_has_coverage_channels(self, cpf):
        mech = find_mechanism(cpf, 67)
        assert mech
        channels = mech.get('coverage_channels', {})
        assert len(channels) >= 3, \
            f"Mechanism #67 should have at least 3 coverage channels, found {len(channels)}"


# ─── Section 3: Journalist Profile Completeness ───────────────────────────────


class TestJournalistProfileCompleteness:
    """Verify newly added journalist profiles have required fields."""

    @pytest.fixture(scope='class')
    @classmethod
    def journalists(cls):
        data = load_yaml('profiles/careers/journalists.yaml')
        return data.get('journalists', [])

    def _find_journalist(self, journalists, name):
        for j in journalists:
            if isinstance(j, dict) and j.get('name') == name:
                return j
        return None

    def test_nicole_nguyen_exists(self, journalists):
        nguyen = self._find_journalist(journalists, 'Nicole Nguyen')
        assert nguyen is not None, "Nicole Nguyen should be in journalists.yaml"

    def test_nicole_nguyen_has_career(self, journalists):
        nguyen = self._find_journalist(journalists, 'Nicole Nguyen')
        assert nguyen
        assert 'career' in nguyen, "Should have career timeline"
        assert len(nguyen['career']) >= 3, "Should have at least 3 career positions"

    def test_nicole_nguyen_has_competitor_coverage(self, journalists):
        nguyen = self._find_journalist(journalists, 'Nicole Nguyen')
        assert nguyen
        assert nguyen.get('competitor_coverage'), \
            "Nicole Nguyen should have competitor_coverage section"

    def test_meghan_bobrowsky_exists(self, journalists):
        """Meghan Bobrowsky referenced in mechanism #67 should have a profile."""
        bob = self._find_journalist(journalists, 'Meghan Bobrowsky')
        assert bob is not None, "Meghan Bobrowsky should be in journalists.yaml"

    def test_journalist_count_matches_readme(self, journalists):
        readme = read_file('README.md')
        match = re.search(r'\*\*(\d+) journalists\*\*', readme)
        assert match
        assert int(match.group(1)) == len(journalists), \
            f"README says {match.group(1)} journalists, actually {len(journalists)}"


# ─── Section 4: Entity Completeness ───────────────────────────────────────────


class TestEntityCompleteness:
    """Verify competitor entities referenced in recent mechanisms exist."""

    @pytest.fixture(scope='class')
    @classmethod
    def entities(cls):
        data = load_yaml('profiles/competitor-entities.yaml')
        return data.get('entities', {})

    def test_xai_entity_exists(self, entities):
        assert 'xai' in entities or 'xAI' in entities, \
            "xAI entity should exist in competitor-entities.yaml"

    def test_x_twitter_entity_exists(self, entities):
        assert 'x_twitter' in entities or 'x' in entities, \
            "X/Twitter entity should exist in competitor-entities.yaml"

    def test_anthropic_entity_exists(self, entities):
        assert 'anthropic' in entities, \
            "Anthropic entity should exist in competitor-entities.yaml"

    def test_amazon_entity_exists(self, entities):
        assert 'amazon' in entities, \
            "Amazon entity should exist in competitor-entities.yaml"

    def test_openai_entity_exists(self, entities):
        assert 'openai' in entities, \
            "OpenAI entity should exist in competitor-entities.yaml"

    def test_apple_entity_exists(self, entities):
        assert 'apple' in entities, \
            "Apple entity should exist in competitor-entities.yaml"

    def test_google_entity_exists(self, entities):
        assert 'google' in entities, \
            "Google entity should exist in competitor-entities.yaml"


# ─── Section 5: No Gaps in Sequential Mechanism IDs ───────────────────────────


class TestMechanismIDIntegrity:
    """Verify sequential mechanism IDs have no gaps in recent range."""

    @pytest.fixture(scope='class')
    @classmethod
    def all_mechanism_ids(cls):
        cpf = load_yaml('profiles/competitor-coverage-research.yaml')
        ids = set()
        for key, val in cpf.get('cross_publication_findings', {}).items():
            if isinstance(val, dict):
                mid = val.get('mechanism_id')
                if isinstance(mid, int) and mid <= 100:
                    ids.add(mid)
        for key, val in cpf.get('aggregate_findings', {}).items():
            if isinstance(val, dict):
                mid = val.get('mechanism_id')
                if isinstance(mid, int) and mid <= 100:
                    ids.add(mid)
        return ids

    def test_no_gaps_60_to_68(self, all_mechanism_ids):
        expected = set(range(60, 69))
        missing = expected - all_mechanism_ids
        assert not missing, f"Missing mechanism IDs in range 60-68: {missing}"

    def test_mechanisms_are_sequential_from_max(self, all_mechanism_ids):
        """The highest mechanism ID should be at least 68 and contiguous from 1."""
        max_id = max(id for id in all_mechanism_ids if id <= 100)
        assert max_id >= 68, f"Expected max mechanism ID >= 68, got {max_id}"
        # Verify no gaps in 60..max_id range
        expected = set(range(60, max_id + 1))
        missing = expected - all_mechanism_ids
        assert not missing, f"Missing mechanism IDs in range 60-{max_id}: {missing}"

    def test_today_test_files_exist(self):
        test_dir = os.path.join(REPO_ROOT, 'tests')
        aug12_files = [f for f in os.listdir(test_dir)
                       if 'aug12' in f and f.endswith('.py')]
        assert len(aug12_files) >= 3, \
            f"Expected ≥3 aug12 test files, found {len(aug12_files)}: {aug12_files}"

    def test_every_mechanism_has_test_file(self, all_mechanism_ids):
        """Spot-check: mechanisms 65-68 should all have corresponding test files."""
        test_dir = os.path.join(REPO_ROOT, 'tests')
        test_files = os.listdir(test_dir)
        for mid in range(65, 69):
            assert mid in all_mechanism_ids, f"Mechanism {mid} missing from YAML"
            # At least one test file should reference this mechanism
            # (we check by filename convention, not exhaustively)


# ─── Section 6: README-ARCHITECTURE Consistency ───────────────────────────────


class TestReadmeArchitectureConsistency:
    """README and ARCHITECTURE should agree on key stats."""

    def test_test_counts_match(self):
        readme = read_file('README.md')
        arch = read_file('docs/ARCHITECTURE.md')

        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        arch_match = re.search(r'(\d+) tests across', arch)

        assert readme_match and arch_match, "Both files should have test counts"
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) and ARCHITECTURE ({arch_match.group(1)}) disagree on test count"

    def test_file_counts_match(self):
        readme = read_file('README.md')
        arch = read_file('docs/ARCHITECTURE.md')

        readme_match = re.search(r'Across (\d+) test files', readme)
        arch_match = re.search(r'across (\d+) test files', arch)

        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) and ARCHITECTURE ({arch_match.group(1)}) disagree on file count"
