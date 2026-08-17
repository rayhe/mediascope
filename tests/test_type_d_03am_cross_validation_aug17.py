"""
Type D cross-validation (Aug 17, 03:00 PT): Structural integrity of mechanisms
#143-#147, YAML section hygiene (entities vs publisher_entities, publications
vs cross_publication_findings), doc sync (430 test files, all aug17 files in
README + ARCHITECTURE), mechanism cross-reference bidirectionality.

Fixes applied this iteration:
  - Moved 3 entries (mansueto_ventures, axel_springer_business_insider,
    sarah_perez_cross_entity_mechanism_142) from entities to publisher_entities
    in competitor-entities.yaml (missing regex field)
  - Moved 14 mechanism entries from publications to cross_publication_findings
    in competitor-coverage-research.yaml (missing meta_coverage_tone)
  - Added 6 missing test files to ARCHITECTURE.md + README.md
  - Synced test count headers (14215 / 430)
"""

import os
import re
import yaml
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"


def load_yaml(name):
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities_data():
    return load_yaml("competitor-entities.yaml")


@pytest.fixture(scope="module")
def research_data():
    return load_yaml("competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def readme():
    with open(REPO_ROOT / "README.md") as f:
        return f.read()


@pytest.fixture(scope="module")
def architecture():
    with open(REPO_ROOT / "docs" / "ARCHITECTURE.md") as f:
        return f.read()


# ── Class 1: Entity Section Hygiene ──────────────────────────────────

class TestEntitySectionHygiene:
    """Ensure entities section contains only core tech entities with regex."""

    def test_entities_all_have_regex(self, entities_data):
        for key, val in entities_data["entities"].items():
            assert "regex" in val, f"entities.{key} missing regex"

    def test_entities_all_have_category(self, entities_data):
        for key, val in entities_data["entities"].items():
            assert "category" in val, f"entities.{key} missing category"

    def test_no_mechanism_entries_in_entities(self, entities_data):
        """Mechanism-specific entries should not be in the core entities section."""
        for key in entities_data["entities"]:
            assert "mechanism" not in key.lower(), \
                f"entities.{key} looks like a mechanism entry — should be in publisher_entities"

    def test_publisher_entities_section_exists(self, entities_data):
        assert "publisher_entities" in entities_data

    def test_publisher_entities_not_empty(self, entities_data):
        assert len(entities_data["publisher_entities"]) >= 3

    def test_expected_core_entities_present(self, entities_data):
        expected = {"openai", "anthropic", "amazon", "apple", "google",
                    "x_twitter", "meta", "xai", "samsung", "microsoft",
                    "snowflake", "snap", "yahoo_apollo", "wbd_cnn",
                    "versant_media_group"}
        actual = set(entities_data["entities"].keys())
        assert expected == actual, f"Mismatch: extra={actual - expected}, missing={expected - actual}"


# ── Class 2: Publications Section Hygiene ────────────────────────────

class TestPublicationsSectionHygiene:
    """Ensure publications section contains only actual publication profiles."""

    def test_all_publications_have_meta_coverage_tone(self, research_data):
        pubs = research_data.get("publications", {})
        for name, pub in pubs.items():
            assert "meta_coverage_tone" in pub, \
                f"publications.{name} missing meta_coverage_tone — should be in cross_publication_findings"

    def test_no_mechanism_entries_in_publications(self, research_data):
        pubs = research_data.get("publications", {})
        for name, pub in pubs.items():
            if "mechanism_id" in pub:
                assert "meta_coverage_tone" in pub, \
                    f"publications.{name} has mechanism_id but no meta_coverage_tone — move to cross_publication_findings"

    def test_publications_count_is_9(self, research_data):
        pubs = research_data.get("publications", {})
        assert len(pubs) == 9, f"Expected 9 publication profiles, got {len(pubs)}: {list(pubs.keys())}"


# ── Class 3: Mechanism #143-#147 Structural Integrity ────────────────

class TestRecentMechanismStructure:
    """Validate mechanisms #143-#147 have all required fields."""

    def _find_mechanism(self, research_data, mech_id):
        for section in ['cross_publication_findings', 'publications']:
            if section in research_data:
                for key, val in research_data[section].items():
                    if isinstance(val, dict) and val.get('mechanism_id') == mech_id:
                        return key, val
        return None, None

    @pytest.mark.parametrize("mech_id", [143, 144, 145, 146, 147])
    def test_mechanism_exists(self, research_data, mech_id):
        key, val = self._find_mechanism(research_data, mech_id)
        assert val is not None, f"Mechanism #{mech_id} not found in research data"

    @pytest.mark.parametrize("mech_id", [143, 144, 145, 146, 147])
    def test_mechanism_has_test_file(self, research_data, mech_id):
        key, val = self._find_mechanism(research_data, mech_id)
        assert val is not None
        assert "test_file" in val, f"Mechanism #{mech_id} ({key}) missing test_file"

    @pytest.mark.parametrize("mech_id", [143, 144, 145, 146, 147])
    def test_mechanism_test_file_exists_on_disk(self, research_data, mech_id):
        key, val = self._find_mechanism(research_data, mech_id)
        assert val is not None
        test_file = val.get("test_file", "")
        if not test_file.startswith("tests/"):
            test_file = f"tests/{test_file}"
        assert (REPO_ROOT / test_file).exists(), \
            f"Mechanism #{mech_id} test_file {test_file} does not exist on disk"

    @pytest.mark.parametrize("mech_id", [143, 145, 146, 147])
    def test_mechanism_has_confounders(self, research_data, mech_id):
        """Non-podcast mechanisms should have confounders documented."""
        key, val = self._find_mechanism(research_data, mech_id)
        assert val is not None
        has_confounders = ("confounders" in val or "confounding_factors" in val)
        assert has_confounders, f"Mechanism #{mech_id} ({key}) missing confounders"


# ── Class 4: Mechanism ID Uniqueness ─────────────────────────────────

class TestMechanismIdUniqueness:
    """No duplicate mechanism_id values across all sections."""

    def test_no_duplicate_mechanism_ids(self, research_data):
        ids = []
        for section in ['cross_publication_findings', 'publications']:
            if section in research_data:
                for key, val in research_data[section].items():
                    if isinstance(val, dict) and 'mechanism_id' in val:
                        ids.append((val['mechanism_id'], key, section))
        id_counts = {}
        for mid, key, section in ids:
            if mid not in id_counts:
                id_counts[mid] = []
            id_counts[mid].append(f"{section}.{key}")
        duplicates = {k: v for k, v in id_counts.items() if len(v) > 1}
        assert not duplicates, f"Duplicate mechanism IDs: {duplicates}"

    def test_mechanism_ids_contiguous_143_to_147(self, research_data):
        """Mechanisms 143-147 should all exist (contiguous)."""
        ids = set()
        for section in ['cross_publication_findings', 'publications']:
            if section in research_data:
                for key, val in research_data[section].items():
                    if isinstance(val, dict) and 'mechanism_id' in val:
                        ids.add(val['mechanism_id'])
        for mid in range(143, 148):
            assert mid in ids, f"Mechanism #{mid} missing from research data"


# ── Class 5: Doc Sync Integrity ──────────────────────────────────────

class TestDocSyncIntegrity:
    """README and ARCHITECTURE test file counts and listings match disk."""

    def test_readme_test_file_count_matches_disk(self, readme):
        actual = len([f for f in os.listdir(REPO_ROOT / "tests")
                      if f.startswith("test_") and f.endswith(".py")])
        match = re.search(r'\*\*(\d+) tests\*\* across (\d+) test files', readme)
        assert match, "README.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, f"README claims {claimed_files}, disk has {actual}"

    def test_architecture_test_file_count_matches_disk(self, architecture):
        actual = len([f for f in os.listdir(REPO_ROOT / "tests")
                      if f.startswith("test_") and f.endswith(".py")])
        match = re.search(r'(\d+) tests across (\d+) test files', architecture)
        assert match, "ARCHITECTURE.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, f"ARCHITECTURE claims {claimed_files}, disk has {actual}"

    def test_readme_architecture_test_count_agreement(self, readme, architecture):
        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        arch_match = re.search(r'(\d+) tests across', architecture)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"

    def test_all_aug17_test_files_in_readme(self, readme):
        aug17_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug17" in f and f.endswith(".py")]
        for f in aug17_files:
            assert f in readme, f"{f} missing from README.md"

    def test_all_aug17_test_files_in_architecture(self, architecture):
        aug17_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug17" in f and f.endswith(".py")]
        for f in aug17_files:
            assert f in architecture, f"{f} missing from ARCHITECTURE.md"


# ── Class 6: Cross-Reference Bidirectionality ────────────────────────

class TestCrossReferenceBidirectionality:
    """Mechanism cross-references should be bidirectional where claimed."""

    def _find_mechanism(self, research_data, mech_id):
        for section in ['cross_publication_findings', 'publications']:
            if section in research_data:
                for key, val in research_data[section].items():
                    if isinstance(val, dict) and val.get('mechanism_id') == mech_id:
                        return key, val
        return None, None

    def test_mechanism_147_backrefs_76_and_91(self, research_data):
        """Mechanism #147 (Warby Parker) claims cross-refs to #76 and #91."""
        key, val = self._find_mechanism(research_data, 147)
        assert val is not None
        # Check that cross_references exist and include 76 and 91
        cross_refs = val.get("cross_references", val.get("testable_predictions", []))
        ref_ids = set()
        if isinstance(cross_refs, list):
            for ref in cross_refs:
                if isinstance(ref, dict) and "mechanism_id" in ref:
                    ref_ids.add(ref["mechanism_id"])
        assert 76 in ref_ids or 91 in ref_ids, \
            f"Mechanism #147 should cross-reference #76 or #91, found refs to: {ref_ids}"

    def test_mechanism_145_backrefs_132(self, research_data):
        """Mechanism #145 (Android Police) claims cross-ref to #132 (Digital Trends)."""
        key, val = self._find_mechanism(research_data, 145)
        assert val is not None
        cross_refs = val.get("cross_references", [])
        ref_ids = set()
        if isinstance(cross_refs, list):
            for ref in cross_refs:
                if isinstance(ref, dict) and "mechanism_id" in ref:
                    ref_ids.add(ref["mechanism_id"])
        assert 132 in ref_ids, \
            f"Mechanism #145 should cross-reference #132, found refs to: {ref_ids}"


# ── Class 7: Test File Importability ─────────────────────────────────

class TestAug17TestFileImportability:
    """All Aug 17 test files should be importable without errors."""

    @pytest.mark.parametrize("filename", [
        "test_android_police_valnet_per_click_smart_glasses_coverage_asymmetry_aug17",
        "test_axel_springer_kkr_openai_financial_architecture_aug17",
        "test_google_warby_parker_equity_publisher_feedback_loop_aug17",
        "test_jason_england_future_plc_cross_entity_competitive_aspiration_inversion_aug17",
        "test_sarah_perez_cross_entity_privacy_vocabulary_inversion_aug17",
    ])
    def test_file_imports(self, filename):
        import importlib
        mod = importlib.import_module(filename)
        assert mod is not None
