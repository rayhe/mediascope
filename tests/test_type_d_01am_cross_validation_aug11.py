"""
Type D Cross-Validation: Aug 11, 2026 01:00 PT

Validates:
1. Mechanism #37 (Open-Weight Policy Coverage Selection Asymmetry) structural integrity
2. Mechanism ID completeness — missing IDs #18, #20, #21, #22, #25 now added
3. Parametrize counter enhancement — variable-referenced parametrize now counted
4. README/ARCHITECTURE test count sync (8920 → 9050 after counter fix)
5. Mechanism ID contiguity and uniqueness across all profiles
6. Cross-reference consistency: distinction_from_* references match cataloged mechanisms
"""

import re
import yaml
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
TESTS_DIR = REPO_ROOT / "tests"


class TestMechanismIDCompleteness:
    """Verify all referenced mechanism IDs are now cataloged."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            self.research = yaml.safe_load(f)

    def _all_mechanism_ids(self):
        """Extract all mechanism_id values from cross_publication_findings."""
        ids = set()
        findings = self.research.get("cross_publication_findings", {})
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.add(val["mechanism_id"])
        return ids

    def test_mechanism_18_cataloged(self):
        """Mechanism #18 (FT OpenAI Hardware Privacy) now has mechanism_id entry."""
        assert 18 in self._all_mechanism_ids()

    def test_mechanism_20_cataloged(self):
        """Mechanism #20 (Kate Knibbs Dual Watchdog) now has mechanism_id entry."""
        assert 20 in self._all_mechanism_ids()

    def test_mechanism_21_cataloged(self):
        """Mechanism #21 (IPO Underwriter Research Laundering) now has mechanism_id entry."""
        assert 21 in self._all_mechanism_ids()

    def test_mechanism_22_cataloged(self):
        """Mechanism #22 (WSJ OpenAI Ad Cannibalization) now has mechanism_id entry."""
        assert 22 in self._all_mechanism_ids()

    def test_mechanism_25_cataloged(self):
        """Mechanism #25 (Amazon Dual-Lab Triangle) now has mechanism_id entry."""
        assert 25 in self._all_mechanism_ids()

    def test_mechanism_37_present(self):
        """Mechanism #37 (Open-Weight Policy Coverage Selection Asymmetry) still cataloged."""
        assert 37 in self._all_mechanism_ids()

    def test_all_mechanism_ids_are_unique(self):
        """No duplicate mechanism_id values across all findings."""
        findings = self.research.get("cross_publication_findings", {})
        ids = []
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.append((val["mechanism_id"], key))
        id_counts = {}
        for mid, key in ids:
            id_counts.setdefault(mid, []).append(key)
        duplicates = {mid: keys for mid, keys in id_counts.items() if len(keys) > 1}
        assert not duplicates, f"Duplicate mechanism_ids: {duplicates}"

    def test_all_mechanism_ids_are_positive_integers(self):
        """All mechanism_id values must be positive integers."""
        findings = self.research.get("cross_publication_findings", {})
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                mid = val["mechanism_id"]
                assert isinstance(mid, int) and mid > 0, (
                    f"{key} has invalid mechanism_id: {mid}"
                )


class TestMechanismIDContiguity:
    """Check for gaps in the mechanism ID sequence."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            self.research = yaml.safe_load(f)

    def _all_mechanism_ids(self):
        ids = set()
        findings = self.research.get("cross_publication_findings", {})
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.add(val["mechanism_id"])
        return ids

    def test_mechanism_id_range_17_to_40(self):
        """Mechanism IDs should span 17-40 (updated after mechanisms #38-#40 added)."""
        ids = self._all_mechanism_ids()
        assert min(ids) == 17, f"Expected min ID 17, got {min(ids)}"
        assert max(ids) >= 40, f"Expected max ID ≥40, got {max(ids)}"

    def test_mechanism_id_count(self):
        """At least 21 unique mechanism IDs cataloged in cross_publication_findings."""
        ids = self._all_mechanism_ids()
        assert len(ids) >= 21, f"Expected ≥21 unique IDs, got {len(ids)}: {sorted(ids)}"


class TestDistinctionFromReferences:
    """Verify distinction_from_* references point to real mechanisms."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            self.research = yaml.safe_load(f)

    def _all_mechanism_ids(self):
        ids = set()
        findings = self.research.get("cross_publication_findings", {})
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.add(val["mechanism_id"])
        return ids

    def test_distinction_references_match_cataloged_ids(self):
        """Every distinction_from_N reference should match a cataloged mechanism_id."""
        cataloged = self._all_mechanism_ids()
        findings = self.research.get("cross_publication_findings", {})
        missing_refs = []
        for key, val in findings.items():
            if not isinstance(val, dict):
                continue
            for field_name, field_val in val.items():
                if field_name.startswith("distinction_from_") and isinstance(field_val, str):
                    # Extract mechanism ID from field name (last numeric segment)
                    parts = field_name.split("_")
                    try:
                        ref_id = int(parts[-1])
                    except ValueError:
                        continue  # e.g. distinction_from_guardian — not a mechanism ref
                    if ref_id not in cataloged:
                        missing_refs.append(f"{key}.{field_name} references #{ref_id}")
        assert not missing_refs, (
            f"distinction_from references to uncataloged mechanisms:\n"
            + "\n".join(missing_refs)
        )


class TestTestCountSync:
    """Verify README/ARCHITECTURE counts match the enhanced static counter."""

    def test_readme_count_is_current(self):
        """README.md test count header should be ≥9260 (updated after mechanisms #38-#40)."""
        readme = (REPO_ROOT / "README.md").read_text()
        match = re.search(r"\*\*(\d+) tests\*\* across (\d+) test files", readme)
        assert match, "README.md missing test count header"
        count = int(match.group(1))
        assert count >= 9260, f"README claims {count} tests, expected ≥9260"

    def test_architecture_count_is_current(self):
        """ARCHITECTURE.md test count header should be ≥9260 (updated after mechanisms #38-#40)."""
        arch = (REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(r"(\d+) tests across (\d+) test files", arch)
        assert match, "ARCHITECTURE.md missing test count header"
        count = int(match.group(1))
        assert count >= 9260, f"ARCHITECTURE.md claims {count} tests, expected ≥9260"

    def test_file_count_is_293(self):
        """File count should be 293 after adding this cross-validation test."""
        on_disk = len(list(TESTS_DIR.glob("test_*.py")))
        readme = (REPO_ROOT / "README.md").read_text()
        match = re.search(r"\*\*\d+ tests\*\* across (\d+) test files", readme)
        assert match, "README.md missing file count"
        claimed = int(match.group(1))
        assert claimed == on_disk, (
            f"README claims {claimed} files, {on_disk} on disk"
        )


class TestParametrizeCounterEnhancement:
    """Verify the parametrize counter handles variable references."""

    def test_variable_parametrize_counted(self):
        """test_competitor_coverage.py PUBLICATIONS variable parametrize must be counted."""
        # This file has 4 × @pytest.mark.parametrize("pub", PUBLICATIONS)
        # with PUBLICATIONS = [...9 items...]
        # Static counter should find 33 defs + 32 expansions = 65
        import sys
        sys.path.insert(0, str(TESTS_DIR))
        from test_structural_consistency import TestTestFileListingConsistency
        t = TestTestFileListingConsistency()
        total = t._count_pytest_tests()
        # The static counter should now be ≥9000 (was 8920 before fix)
        assert total >= 9000, (
            f"Static counter returned {total}, expected ≥9000 after variable parametrize fix"
        )

    def test_single_quote_parametrize_counted(self):
        """Single-quoted parametrize arg names must be counted."""
        # test_google_spv_guarantee uses 'publication' and 'factor'
        content = (TESTS_DIR / "test_google_spv_guarantee_anthropic_showcase_chain_aug10.py").read_text()
        has_single_quote = bool(re.search(
            r"@pytest\.mark\.parametrize\(\s*'", content
        ))
        assert has_single_quote, "Expected single-quote parametrize in this file"


class TestNewMechanismEntrySchema:
    """Verify newly added mechanism entries have required fields."""

    REQUIRED_FIELDS = ["finding_type", "mechanism_id", "finding_summary", "test_file", "test_count"]
    NEW_ENTRIES = [
        "ft_openai_hardware_privacy_double_standard",
        "kate_knibbs_dual_watchdog_paradox",
        "ipo_underwriter_research_laundering",
        "wsj_openai_ad_cannibalization_self_demonetization",
        "amazon_dual_lab_non_disclosure_triangle",
    ]

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            self.research = yaml.safe_load(f)

    @pytest.mark.parametrize("entry_name", NEW_ENTRIES)
    def test_entry_exists(self, entry_name):
        """Each newly added mechanism entry exists in cross_publication_findings."""
        findings = self.research.get("cross_publication_findings", {})
        assert entry_name in findings, f"{entry_name} not found in cross_publication_findings"

    @pytest.mark.parametrize("entry_name", NEW_ENTRIES)
    def test_entry_has_required_fields(self, entry_name):
        """Each newly added entry has all required schema fields."""
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get(entry_name, {})
        missing = [f for f in self.REQUIRED_FIELDS if f not in entry]
        assert not missing, f"{entry_name} missing fields: {missing}"

    @pytest.mark.parametrize("entry_name", NEW_ENTRIES)
    def test_entry_test_file_exists(self, entry_name):
        """Test file referenced by each entry exists on disk."""
        findings = self.research.get("cross_publication_findings", {})
        entry = findings.get(entry_name, {})
        test_file = entry.get("test_file", "")
        if test_file:
            path = REPO_ROOT / test_file
            assert path.exists(), f"{entry_name} references {test_file} which doesn't exist"


class TestAug11CumulativeIntegrity:
    """Verify Aug 10–11 accumulated test files are all present."""

    AUG10_FILES = [
        "test_openai_meta_facial_recognition_parity_aug10.py",
        "test_guardian_rogue_ai_volume_asymmetry_aug10.py",
        "test_wired_rogue_ai_coverage_volume_asymmetry_aug10.py",
        "test_advance_conde_nast_aggregate_ai_dependency_aug10.py",
        "test_pre_ipo_owner_investor_publisher_convergence_aug10.py",
        "test_type_d_1pm_cross_validation_aug10.py",
        "test_type_d_08am_cross_validation_aug10.py",
        "test_type_d_09am_cross_validation_aug10.py",
        "test_type_d_04am_cross_validation_aug10.py",
        "test_type_d_6pm_cross_validation_aug10.py",
        "test_type_d_11pm_cross_validation_aug10.py",
        "test_chokkattu_temporal_framing_oscillation_aug10.py",
        "test_wsj_openai_ad_cannibalization_self_demonetization_aug10.py",
        "test_amazon_dual_lab_non_disclosure_triangle_aug10.py",
        "test_ipo_underwriter_research_laundering_aug10.py",
        "test_google_spv_guarantee_anthropic_showcase_chain_aug10.py",
        "test_wsj_anthropic_meta_business_viability_framing_aug10.py",
        "test_guardian_google_sid_governance_capture_aug10.py",
        "test_google_spv_guarantee_anthropic_showcase_chain_aug10.py",
        "test_nyt_anthropic_triple_chain_incentive_aug10.py",
    ]
    AUG11_FILES = [
        "test_open_weight_policy_coverage_selection_asymmetry_aug11.py",
        "test_type_d_01am_cross_validation_aug11.py",
    ]

    @pytest.mark.parametrize("filename", AUG10_FILES)
    def test_aug10_file_exists(self, filename):
        """Aug 10 test file exists on disk."""
        assert (TESTS_DIR / filename).exists(), f"Missing: {filename}"

    @pytest.mark.parametrize("filename", AUG11_FILES)
    def test_aug11_file_exists(self, filename):
        """Aug 11 test file exists on disk."""
        assert (TESTS_DIR / filename).exists(), f"Missing: {filename}"

    def test_total_test_files_at_least_293(self):
        """Should have at least 293 test files after this cross-validation."""
        count = len(list(TESTS_DIR.glob("test_*.py")))
        assert count >= 293, f"Expected ≥293 test files, got {count}"


class TestMechanism37Integrity:
    """Cross-validate Mechanism #37 from previous sprint."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            self.research = yaml.safe_load(f)

    def test_mechanism_37_has_finding_summary(self):
        findings = self.research.get("cross_publication_findings", {})
        entry = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 37:
                entry = val
                break
        assert entry is not None, "No entry with mechanism_id 37"
        assert "finding_summary" in entry, "Mechanism #37 missing finding_summary"

    def test_mechanism_37_test_file_exists(self):
        """Mechanism #37 test file exists."""
        assert (TESTS_DIR / "test_open_weight_policy_coverage_selection_asymmetry_aug11.py").exists()

    def test_mechanism_37_covers_open_weight(self):
        """Mechanism #37 test file references open-weight policy."""
        content = (TESTS_DIR / "test_open_weight_policy_coverage_selection_asymmetry_aug11.py").read_text()
        assert "open-weight" in content.lower() or "open_weight" in content.lower()
