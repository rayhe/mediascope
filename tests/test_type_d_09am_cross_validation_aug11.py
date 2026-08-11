"""
Type D cross-validation — Aug 11, 09:00 PT

Validates fixes from this session:
1. Mechanisms #42 and #43 moved from publications → cross_publication_findings
2. Snap entity added to competitor-entities.yaml (test expectation updated)
3. 05am cross-validation assertions made resilient (>= instead of ==)
4. No publications section entry should have a mechanism_id
5. All cross_publication_findings entries should have mechanism_id
6. README/ARCHITECTURE test counts updated

9 classes validating structural integrity after the section-move fix.
"""

import os
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
TESTS_DIR = REPO_ROOT / "tests"


def _load_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


def _load_entities():
    with open(PROFILES_DIR / "competitor-entities.yaml") as f:
        return yaml.safe_load(f)


class TestMechanism42InCorrectSection:
    """Mechanism #42 (compound_competitor_silence) must be in cross_publication_findings, not publications."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_not_in_publications(self):
        pubs = self.research.get("publications", {})
        assert "compound_competitor_silence" not in pubs

    def test_in_cross_publication_findings(self):
        cpf = self.research.get("cross_publication_findings", {})
        assert "compound_competitor_silence" in cpf

    def test_has_mechanism_id_42(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("compound_competitor_silence", {})
        assert entry.get("mechanism_id") == 42

    def test_has_test_file(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("compound_competitor_silence", {})
        test_file = entry.get("test_file", "")
        assert (REPO_ROOT / test_file).exists(), f"{test_file} does not exist"


class TestMechanism43InCorrectSection:
    """Mechanism #43 (dual_client_litigation_entanglement) must be in cross_publication_findings, not publications."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_not_in_publications(self):
        pubs = self.research.get("publications", {})
        assert "dual_client_litigation_entanglement" not in pubs

    def test_in_cross_publication_findings(self):
        cpf = self.research.get("cross_publication_findings", {})
        assert "dual_client_litigation_entanglement" in cpf

    def test_has_mechanism_id_43(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("dual_client_litigation_entanglement", {})
        assert entry.get("mechanism_id") == 43

    def test_has_test_file(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("dual_client_litigation_entanglement", {})
        test_file = entry.get("test_file", "")
        assert (REPO_ROOT / test_file).exists(), f"{test_file} does not exist"

    def test_has_dual_client_publications(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("dual_client_litigation_entanglement", {})
        pubs = entry.get("dual_client_publications", [])
        assert len(pubs) >= 5, f"Expected >=5 dual-client pubs, got {len(pubs)}"

    def test_has_source_urls(self):
        cpf = self.research.get("cross_publication_findings", {})
        entry = cpf.get("dual_client_litigation_entanglement", {})
        urls = entry.get("source_urls", [])
        assert len(urls) >= 5, f"Expected >=5 source URLs, got {len(urls)}"


class TestPublicationsSectionClean:
    """No entry in the publications section should have a mechanism_id — those belong in findings sections."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_no_mechanism_ids_in_publications(self):
        pubs = self.research.get("publications", {})
        for slug, pub in pubs.items():
            if isinstance(pub, dict):
                assert "mechanism_id" not in pub, \
                    f"publications.{slug} has mechanism_id={pub.get('mechanism_id')} — should be in cross_publication_findings"

    def test_all_publications_have_meta_coverage_tone(self):
        pubs = self.research.get("publications", {})
        for slug, pub in pubs.items():
            if isinstance(pub, dict):
                assert "meta_coverage_tone" in pub, \
                    f"publications.{slug} missing meta_coverage_tone"

    @pytest.mark.parametrize("expected_pub", [
        "wired", "the-verge", "atlantic", "nytimes", "financial-times",
        "guardian", "mit-tech-review", "gizmodo", "news-corp"
    ])
    def test_expected_publication_present(self, expected_pub):
        pubs = self.research.get("publications", {})
        assert expected_pub in pubs, f"{expected_pub} missing from publications"


class TestCrossPublicationFindingsComplete:
    """All mechanism entries should be in aggregate_findings or cross_publication_findings."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_at_least_26_unique_ids(self):
        ids = set()
        for section in ["aggregate_findings", "cross_publication_findings"]:
            for k, v in self.research.get(section, {}).items():
                if isinstance(v, dict) and "mechanism_id" in v:
                    ids.add(v["mechanism_id"])
        assert len(ids) >= 26, f"Expected >=26 IDs, got {len(ids)}"

    def test_max_id_at_least_43(self):
        ids = set()
        for section in ["aggregate_findings", "cross_publication_findings"]:
            for k, v in self.research.get(section, {}).items():
                if isinstance(v, dict) and "mechanism_id" in v:
                    ids.add(v["mechanism_id"])
        assert max(ids) >= 43

    def test_cross_pub_has_at_least_23(self):
        cpf = self.research.get("cross_publication_findings", {})
        ids = {v["mechanism_id"] for v in cpf.values() if isinstance(v, dict) and "mechanism_id" in v}
        assert len(ids) >= 23, f"Expected >=23, got {len(ids)}"

    def test_42_and_43_in_cross_pub(self):
        cpf = self.research.get("cross_publication_findings", {})
        ids = {v["mechanism_id"] for v in cpf.values() if isinstance(v, dict) and "mechanism_id" in v}
        assert 42 in ids, "Mechanism #42 not in cross_publication_findings"
        assert 43 in ids, "Mechanism #43 not in cross_publication_findings"


class TestSnapEntityExists:
    """Snap entity should exist in competitor-entities.yaml after mechanism #42 addition."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.entities = _load_entities()

    def test_snap_in_entities(self):
        entities = self.entities.get("entities", {})
        assert "snap" in entities, "snap missing from competitor-entities.yaml"

    def test_all_12_entities_present(self):
        entities = self.entities.get("entities", {})
        expected = {
            "openai", "anthropic", "amazon", "apple", "google",
            "x_twitter", "meta", "xai", "samsung", "microsoft",
            "snowflake", "snap"
        }
        assert set(entities.keys()) == expected


class TestMechanism42And43TestFilesPass:
    """The test files for mechanisms #42 and #43 should exist on disk."""

    def test_mechanism_42_test_file_exists(self):
        assert (TESTS_DIR / "test_chokkattu_wired_compound_competitor_silence_aug11.py").exists()

    def test_mechanism_43_test_file_exists(self):
        assert (TESTS_DIR / "test_dual_client_litigation_entanglement_index_aug11.py").exists()


class TestReadmeCountUpdated:
    """README should reflect current test count."""

    def test_readme_count_at_least_9432(self):
        readme = (REPO_ROOT / "README.md").read_text()
        # Find the test count in README
        import re
        match = re.search(r"\*\*(\d+)\s+tests\*\*", readme)
        assert match, "Could not find test count in README"
        count = int(match.group(1))
        assert count >= 9432, f"README says {count} tests, expected >=9432"


class TestStaleAssertionPrevention:
    """No exact == assertions on mechanism counts that will break when new mechanisms are added."""

    def test_05am_uses_gte_for_total_ids(self):
        """05am cross-validation should use >= not == for mechanism ID count."""
        source = (TESTS_DIR / "test_type_d_05am_cross_validation_aug11.py").read_text()
        # Should NOT have "len(ids) == 24"
        assert "len(ids) == 24" not in source, "05am still has hardcoded == 24"

    def test_05am_uses_gte_for_max_id(self):
        source = (TESTS_DIR / "test_type_d_05am_cross_validation_aug11.py").read_text()
        assert "== 40" not in source or "max(ids.keys()) == 40" not in source

    def test_05am_uses_gte_for_cross_pub(self):
        source = (TESTS_DIR / "test_type_d_05am_cross_validation_aug11.py").read_text()
        assert "len(cpf) == 21" not in source, "05am still has hardcoded == 21"


class TestTestFileCount:
    """Verify current test file count on disk."""

    def test_at_least_301_test_files(self):
        """Including this new test file, should have at least 301."""
        count = sum(1 for f in os.listdir(TESTS_DIR) if f.startswith("test_") and f.endswith(".py"))
        assert count >= 301, f"Expected >=301 test files, got {count}"
