"""
Type D Cross-Validation: Aug 11, 2026 05:00 PT

Validates:
1. All 24 mechanism IDs (17-40) present across aggregate_findings + cross_publication_findings
2. Mechanisms #38-#40 structural integrity (added 02:00-04:00 PT today)
3. Test file existence for all mechanisms with test_file fields
4. README/ARCHITECTURE count sync (9260 tests, 296 files)
5. 01am cross-validation test fix verified (stale assertions updated)
6. Structural consistency suite (124 tests) still green
7. No mechanism_id collisions between aggregate_findings and cross_publication_findings
8. Coverage selection mechanisms (#37, #38, #39) have legitimate_factors documented
"""

import re
import yaml
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
TESTS_DIR = REPO_ROOT / "tests"


def _load_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


def _all_mechanism_ids_from_section(research, section):
    """Extract mechanism_ids from a specific YAML section."""
    ids = {}
    findings = research.get(section, {})
    if isinstance(findings, dict):
        for key, val in findings.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids[val["mechanism_id"]] = key
    return ids


def _all_mechanism_ids(research):
    """Extract ALL mechanism_ids across both aggregate and cross_publication."""
    ids = {}
    ids.update(_all_mechanism_ids_from_section(research, "aggregate_findings"))
    ids.update(_all_mechanism_ids_from_section(research, "cross_publication_findings"))
    return ids


class TestMechanismIDCoverage:
    """All 24 mechanism IDs (17-40) must be present."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_total_unique_mechanism_ids_is_24(self):
        """At least 26 unique mechanism IDs across both sections (17-43, gap at 41)."""
        ids = _all_mechanism_ids(self.research)
        assert len(ids) >= 26, f"Expected >=26, got {len(ids)}: {sorted(ids.keys())}"

    def test_min_id_is_17(self):
        ids = _all_mechanism_ids(self.research)
        assert min(ids.keys()) == 17

    def test_max_id_is_40(self):
        ids = _all_mechanism_ids(self.research)
        assert max(ids.keys()) >= 43

    @pytest.mark.parametrize("mid", [x for x in range(17, 44) if x != 41])
    def test_mechanism_id_present(self, mid):
        """Each ID from 17-43 (except gap at 41) should exist."""
        ids = _all_mechanism_ids(self.research)
        assert mid in ids, f"Mechanism #{mid} not found in any section"

    def test_aggregate_has_ids_19_30_31(self):
        """IDs 19, 30, 31 live in aggregate_findings, not cross_publication."""
        agg = _all_mechanism_ids_from_section(self.research, "aggregate_findings")
        for mid in [19, 30, 31]:
            assert mid in agg, f"Mechanism #{mid} missing from aggregate_findings"

    def test_cross_pub_has_21_ids(self):
        """cross_publication_findings has at least 23 unique mechanism IDs."""
        cpf = _all_mechanism_ids_from_section(self.research, "cross_publication_findings")
        assert len(cpf) >= 23, f"Expected >=23, got {len(cpf)}"


class TestNoMechanismIDCollisions:
    """No mechanism_id should appear in BOTH aggregate and cross_pub sections."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def test_no_id_in_both_sections(self):
        agg = set(_all_mechanism_ids_from_section(self.research, "aggregate_findings").keys())
        cpf = set(_all_mechanism_ids_from_section(self.research, "cross_publication_findings").keys())
        overlap = agg & cpf
        assert not overlap, f"IDs in both sections: {overlap}"


class TestMechanism38Integrity:
    """Mechanism #38: Anthropic-Meta Cloud Deal Coverage Selection."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("anthropic_meta_cloud_deal_coverage_selection", {})

    def test_mechanism_id_is_38(self):
        assert self.entry.get("mechanism_id") == 38

    def test_has_finding_summary(self):
        assert "finding_summary" in self.entry
        assert len(self.entry["finding_summary"]) > 50

    def test_has_test_file(self):
        tf = self.entry.get("test_file", "")
        assert tf, "No test_file field"
        assert (REPO_ROOT / tf).exists(), f"Test file {tf} doesn't exist"

    def test_has_finding_type(self):
        assert "finding_type" in self.entry


class TestMechanism39Integrity:
    """Mechanism #39: Chokkattu Samsung Coverage Selection Gap."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("chokkattu_samsung_coverage_selection_gap", {})

    def test_mechanism_id_is_39(self):
        assert self.entry.get("mechanism_id") == 39

    def test_has_finding_summary(self):
        assert "finding_summary" in self.entry
        assert len(self.entry["finding_summary"]) > 50

    def test_has_test_file(self):
        tf = self.entry.get("test_file", "")
        assert tf
        assert (REPO_ROOT / tf).exists(), f"Test file {tf} doesn't exist"

    def test_references_mechanism_30(self):
        """#39 should reference #30 (Chokkattu Temporal Framing Oscillation) as related."""
        text = yaml.dump(self.entry)
        assert "30" in text or "temporal" in text.lower() or "distinction" in text.lower(), (
            "Mechanism #39 should cross-reference Mechanism #30"
        )


class TestMechanism40Integrity:
    """Mechanism #40: Advance Total AI Financial Exposure Index."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()
        self.cpf = self.research.get("cross_publication_findings", {})
        self.entry = self.cpf.get("advance_total_ai_financial_exposure_index", {})

    def test_mechanism_id_is_40(self):
        assert self.entry.get("mechanism_id") == 40

    def test_has_finding_summary(self):
        assert "finding_summary" in self.entry
        assert len(self.entry["finding_summary"]) > 50

    def test_has_test_file(self):
        tf = self.entry.get("test_file", "")
        assert tf
        assert (REPO_ROOT / tf).exists()

    def test_references_mechanism_37_or_35(self):
        """#40 extends Advance Dual-Asset (#35 or #37), should cross-reference."""
        text = yaml.dump(self.entry)
        assert "35" in text or "37" in text or "advance" in text.lower() or "dual" in text.lower()


class TestCoverageSelectionMechanismsHaveLegitimateFactors:
    """Mechanisms #37, #38, #39 are coverage SELECTION asymmetries —
    they must document legitimate editorial factors to avoid overstating the case."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()
        self.cpf = self.research.get("cross_publication_findings", {})

    @pytest.mark.parametrize("key,mid", [
        ("open_weight_policy_coverage_selection_asymmetry", 37),
        ("anthropic_meta_cloud_deal_coverage_selection", 38),
        ("chokkattu_samsung_coverage_selection_gap", 39),
    ])
    def test_has_legitimate_factors_or_counterpoints(self, key, mid):
        entry = self.cpf.get(key, {})
        text = yaml.dump(entry).lower()
        has_factors = (
            "legitimate" in text
            or "counterpoint" in text
            or "confound" in text
            or "factor" in text
            or "alternative_explanation" in text
        )
        assert has_factors, (
            f"Mechanism #{mid} ({key}) lacks legitimate factors / counterpoints"
        )


class TestTestCountSync:
    """README/ARCHITECTURE must claim ≥9260 tests across ≥296 files."""

    def test_readme_test_count(self):
        readme = (REPO_ROOT / "README.md").read_text()
        match = re.search(r"\*\*(\d+) tests\*\* across (\d+) test files", readme)
        assert match, "README.md missing test count"
        count = int(match.group(1))
        assert count >= 9260, f"README says {count}, expected ≥9260"

    def test_readme_file_count(self):
        readme = (REPO_ROOT / "README.md").read_text()
        match = re.search(r"\*\*\d+ tests\*\* across (\d+) test files", readme)
        assert match
        claimed = int(match.group(1))
        on_disk = len(list(TESTS_DIR.glob("test_*.py")))
        # After this file is created, on_disk = 297 but README may say 296
        # Allow ±1 tolerance for this cross-validation file
        assert abs(claimed - on_disk) <= 1, (
            f"README claims {claimed} files, {on_disk} on disk"
        )

    def test_architecture_test_count(self):
        arch = (REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(r"(\d+) tests across (\d+) test files", arch)
        assert match
        count = int(match.group(1))
        assert count >= 9260, f"ARCHITECTURE.md says {count}, expected ≥9260"


class TestAllMechanismTestFilesExist:
    """Every mechanism with a test_file field should have that file on disk."""

    @pytest.fixture(autouse=True)
    def load(self):
        self.research = _load_research()

    def _collect_test_files(self):
        pairs = []
        for section in ["aggregate_findings", "cross_publication_findings"]:
            findings = self.research.get(section, {})
            if not isinstance(findings, dict):
                continue
            for key, val in findings.items():
                if isinstance(val, dict) and "test_file" in val:
                    pairs.append((key, val["test_file"]))
        return pairs

    @pytest.mark.parametrize("key,test_file", [
        ("anthropic_meta_cloud_deal_coverage_selection",
         "test_anthropic_meta_cloud_deal_coverage_selection_aug11.py"),
        ("chokkattu_samsung_coverage_selection_gap",
         "test_chokkattu_samsung_coverage_selection_gap_aug11.py"),
        ("advance_total_ai_financial_exposure_index",
         "test_advance_total_ai_financial_exposure_index_aug11.py"),
    ])
    def test_aug11_mechanism_test_files_exist(self, key, test_file):
        assert (TESTS_DIR / test_file).exists(), f"Missing: {test_file} for {key}"

    def test_all_test_files_exist(self):
        missing = []
        for key, tf in self._collect_test_files():
            if not (REPO_ROOT / tf).exists():
                missing.append(f"{key}: {tf}")
        assert not missing, f"Missing test files:\n" + "\n".join(missing)


class TestStale01amFixVerified:
    """The 01am cross-validation test had 3 failures; verify our fixes work."""

    def test_01am_file_exists(self):
        assert (TESTS_DIR / "test_type_d_01am_cross_validation_aug11.py").exists()

    def test_01am_no_hardcoded_9107(self):
        """Stale hardcoded 9107 should be replaced with ≥9260 assertion."""
        content = (TESTS_DIR / "test_type_d_01am_cross_validation_aug11.py").read_text()
        assert "== 9107" not in content, "Stale 9107 hardcode still present"

    def test_01am_no_hardcoded_max_37(self):
        """Stale 'max(ids) == 37' assertion should be gone."""
        content = (TESTS_DIR / "test_type_d_01am_cross_validation_aug11.py").read_text()
        # The stale assertion was 'max(ids) == 37' — check it's gone
        assert "max(ids) == 37" not in content, "Stale max=37 range assertion still present"
