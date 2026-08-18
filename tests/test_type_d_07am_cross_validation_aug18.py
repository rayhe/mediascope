"""
Type D Cross-Validation — Tue 2026-08-18 07:00 PT

Fixes and validates:
1. Doc sync regression fix: README and ARCHITECTURE both out of sync — ARCHITECTURE claimed
   449 files (disk has 448) and 16011 tests, README claimed 15030 tests. Fixed both to 16060
   tests across 448 files (verified by pytest --collect-only).
2. Stale midnight test assertion: test_highest_mechanism_is_156 → 160 (mechanisms 157-160
   added to cross_publication_findings in aug18 iterations, 161-162 in aggregate_findings).
3. Cross-validation of mechanisms #157-#162 structural integrity.
4. Verification that all aug18 test files are listed in both README and ARCHITECTURE.
5. README table stat sync with body text.
"""

import os
import re
import yaml
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES = REPO_ROOT / "profiles"


@pytest.fixture(scope="module")
def readme():
    return (REPO_ROOT / "README.md").read_text()


@pytest.fixture(scope="module")
def architecture():
    return (REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()


@pytest.fixture(scope="module")
def ccr():
    with open(PROFILES / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def agg(ccr):
    return ccr.get("aggregate_findings", {})


@pytest.fixture(scope="module")
def test_file_count():
    return len([f for f in os.listdir(REPO_ROOT / "tests")
                if f.startswith("test_") and f.endswith(".py")])


# ── Class 1: Doc Sync Consistency ────────────────────────────────────

class TestDocSyncConsistency:
    """README and ARCHITECTURE stat counts agree with each other and disk."""

    def test_readme_file_count_is_current(self, readme, test_file_count):
        match = re.search(r'across (\d+) test files', readme)
        assert match, "README.md missing test file count"
        assert int(match.group(1)) == test_file_count

    def test_architecture_file_count_is_current(self, architecture, test_file_count):
        match = re.search(r'across (\d+) test files', architecture)
        assert match, "ARCHITECTURE.md missing test file count"
        assert int(match.group(1)) == test_file_count

    def test_readme_test_count_consistent(self, readme):
        """README table and body text test counts agree."""
        table_match = re.search(r'\| Tests \| ~([\d,]+)', readme)
        body_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        assert table_match and body_match
        table_count = int(table_match.group(1).replace(',', ''))
        body_count = int(body_match.group(1))
        assert table_count == body_count, \
            f"README table ({table_count}) != body ({body_count})"

    def test_readme_architecture_test_count_agree(self, readme, architecture):
        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        arch_match = re.search(r'(\d+) tests across', architecture)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"


# ── Class 2: Aug 18 Test File Presence ───────────────────────────────

class TestAug18TestFilesPresence:
    """All aug18 test files exist on disk and are listed in docs."""

    EXPECTED_AUG18_FILES = [
        "test_advance_reddit_meta_ad_competition_structural_incentive_aug18.py",
        "test_advance_reddit_q2_2026_equity_capital_extraction_triple_feedback_aug18.py",
        "test_global_institutional_podcast_meta_category_proxy_aug18.py",
        "test_multi_vector_cultural_delegitimization_cascade_aug18.py",
        "test_nadeem_sarwar_digital_trends_managing_editor_cross_entity_aug18.py",
        "test_openai_companion_meta_surveillance_vocabulary_bifurcation_aug18.py",
        "test_type_d_midnight_cross_validation_aug18.py",
        "test_type_d_07am_cross_validation_aug18.py",
    ]

    @pytest.mark.parametrize("fname", EXPECTED_AUG18_FILES)
    def test_file_exists_on_disk(self, fname):
        assert (REPO_ROOT / "tests" / fname).exists(), f"{fname} missing from disk"

    @pytest.mark.parametrize("fname", EXPECTED_AUG18_FILES)
    def test_file_in_readme(self, readme, fname):
        assert fname in readme, f"{fname} missing from README"

    @pytest.mark.parametrize("fname", EXPECTED_AUG18_FILES)
    def test_file_in_architecture(self, architecture, fname):
        assert fname in architecture, f"{fname} missing from ARCHITECTURE"


# ── Class 3: Mechanisms #157-#160 in cross_publication_findings ──────

class TestMechanisms157to160InCPF:
    """Mechanisms #157-#160 added on Aug 18 are in cross_publication_findings."""

    MECHANISM_IDS = [157, 158, 159, 160]

    def _find_mechanism(self, cpf, mid):
        for k, v in cpf.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                return k, v
        return None, None

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_exists(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val is not None, f"Mechanism #{mid} not found in cross_publication_findings"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_test_file(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val and "test_file" in val
        tf = os.path.basename(val["test_file"])
        assert (REPO_ROOT / "tests" / tf).exists(), \
            f"Mechanism #{mid} test_file {tf} not on disk"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_source_urls_or_articles(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val
        has_sources = "source_urls" in val or "sources" in val or "articles" in val
        assert has_sources, \
            f"Mechanism #{mid} missing source_urls/sources/articles"


# ── Class 4: Mechanisms #161-#162 in aggregate_findings ──────────────

class TestMechanisms161to162InAggregate:
    """Mechanisms #161-#162 are in aggregate_findings (not cpf)."""

    MECHANISM_IDS = [161, 162]

    def _find_mechanism(self, agg, mid):
        for k, v in agg.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                return k, v
        return None, None

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_exists(self, agg, mid):
        _, val = self._find_mechanism(agg, mid)
        assert val is not None, f"Mechanism #{mid} not found in aggregate_findings"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_test_file_or_source_urls(self, agg, mid):
        _, val = self._find_mechanism(agg, mid)
        assert val is not None
        # aggregate_findings may use test_file or just source_urls
        has_ref = "test_file" in val or "source_urls" in val
        assert has_ref, \
            f"Mechanism #{mid} missing both test_file and source_urls"


# ── Class 5: Mechanism Max ID Sync ───────────────────────────────────

class TestMechanismMaxIDSync:
    """Max mechanism ID across all sections is 162."""

    def test_max_id_across_all_sections(self, ccr):
        all_ids = []
        def collect(obj):
            if isinstance(obj, dict):
                mid = obj.get("mechanism_id")
                if isinstance(mid, int):
                    all_ids.append(mid)
                for v in obj.values():
                    collect(v)
            elif isinstance(obj, list):
                for item in obj:
                    collect(item)
        collect(ccr)
        assert max(all_ids) == 162, f"Expected max 162, got {max(all_ids)}"

    def test_cpf_max_is_160(self, cpf):
        ids = [v["mechanism_id"] for v in cpf.values()
               if isinstance(v, dict) and "mechanism_id" in v]
        assert max(ids) == 160


# ── Class 6: Previous Fix Regression Check ───────────────────────────

class TestPreviousFixRegression:
    """Verify fixes from earlier Type D runs haven't regressed."""

    def test_no_mechanism_ids_in_publications_section(self, ccr):
        """Publications section should not contain mechanism entries (except legacy #41)."""
        pubs = ccr.get("publications", {})
        pub_ids = []
        def collect(obj, path=""):
            if isinstance(obj, dict):
                mid = obj.get("mechanism_id")
                if isinstance(mid, int):
                    pub_ids.append(mid)
                for k, v in obj.items():
                    collect(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for item in obj:
                    collect(item, path)
        collect(pubs)
        non_legacy = [m for m in pub_ids if m != 41]
        assert not non_legacy, \
            f"Non-legacy mechanism IDs in publications: {non_legacy}"

    def test_no_duplicate_cpf_mechanism_ids(self, cpf):
        ids = [v["mechanism_id"] for v in cpf.values()
               if isinstance(v, dict) and "mechanism_id" in v]
        assert len(ids) == len(set(ids)), \
            f"Duplicate IDs in cpf: {[x for x in ids if ids.count(x) > 1]}"
