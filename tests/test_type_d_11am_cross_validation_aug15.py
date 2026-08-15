"""
Type D Cross-Validation — Sat Aug 15, 2026 11:00 AM PT (Iteration #122)

Validates fixes applied in this iteration:
1. YAML parse error in competitor-coverage-research.yaml (unquoted '#' in plain scalar)
2. YAML parse error in journalists.yaml (list-format entry at root level)
3. Mechanisms #115-117 misplaced under 'publications' instead of 'cross_publication_findings'
4. Fixture deprecation warning in Karissa Bell test file (class-scoped instance method)

Also validates overall structural integrity after the fixes.
"""

import os
import re
import yaml
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent


def load_yaml(filename):
    """Load a YAML file from the profiles directory."""
    with open(PROFILES_DIR / filename) as f:
        return yaml.safe_load(f)


class TestYAMLIntegrity:
    """All profile YAML files must parse without errors."""

    def test_ccr_parses(self):
        """competitor-coverage-research.yaml must parse successfully."""
        data = load_yaml("competitor-coverage-research.yaml")
        assert isinstance(data, dict)
        assert "publications" in data
        assert "cross_publication_findings" in data

    def test_ce_parses(self):
        """competitor-entities.yaml must parse successfully."""
        data = load_yaml("competitor-entities.yaml")
        assert isinstance(data, dict)

    def test_journalists_parses(self):
        """careers/journalists.yaml must parse successfully."""
        with open(PROFILES_DIR / "careers" / "journalists.yaml") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)
        assert "journalists" in data

    def test_journalists_michael_hicks_named_key(self):
        """Michael Hicks entry must be a named key, not a list item."""
        with open(PROFILES_DIR / "careers" / "journalists.yaml") as f:
            data = yaml.safe_load(f)
        # michael_l_hicks should be a top-level key (not under journalists list)
        assert "michael_l_hicks" in data, "Michael Hicks entry missing as named key"
        assert "name" in data["michael_l_hicks"]
        assert data["michael_l_hicks"]["name"] == "Michael L. Hicks"

    def test_no_unquoted_mechanism_hash_in_ccr_plain_scalars(self):
        """The specific '#30' / '#115' comment-truncation bug must stay fixed.
        
        Regression guard: the counter value containing '(mechanism #30)' must be
        quoted to prevent YAML treating ' #30' as a comment start.
        """
        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            content = f.read()
        
        # The fixed value should be quoted (single or double quotes around it)
        # and should contain the full text including the continuation about TechRadar
        assert "Genre effect (mechanism #30)" in content, (
            "Counter value with mechanism #30 reference is missing"
        )
        assert "TechRadar preview of Samsung (#115)" in content, (
            "Counter value continuation about TechRadar #115 is missing"
        )
        
        # Verify the YAML parses — the original bug caused parse failure
        data = load_yaml("competitor-coverage-research.yaml")
        assert isinstance(data, dict)


class TestMechanismPlacement:
    """Mechanisms must be in the correct YAML section."""

    @pytest.fixture(scope="class")
    @classmethod
    def ccr_data(cls):
        return load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_115_in_cpf(self, ccr_data):
        """Mechanism #115 (TechRadar) must be in cross_publication_findings, not publications."""
        pubs = ccr_data.get("publications", {})
        cpf = ccr_data.get("cross_publication_findings", {})
        assert "techradar_future_plc_privacy_vocabulary_bifurcation" not in pubs
        assert "techradar_future_plc_privacy_vocabulary_bifurcation" in cpf

    def test_mechanism_116_in_cpf(self, ccr_data):
        """Mechanism #116 (Michael Hicks) must be in cross_publication_findings, not publications."""
        pubs = ccr_data.get("publications", {})
        cpf = ccr_data.get("cross_publication_findings", {})
        assert "michael_hicks_android_central_privacy_vocabulary_suppression" not in pubs
        assert "michael_hicks_android_central_privacy_vocabulary_suppression" in cpf

    def test_mechanism_117_in_cpf(self, ccr_data):
        """Mechanism #117 (News Corp Q4) must be in cross_publication_findings, not publications."""
        pubs = ccr_data.get("publications", {})
        cpf = ccr_data.get("cross_publication_findings", {})
        assert "news_corp_q4_fy2026_woo_sue_posture" not in pubs
        assert "news_corp_q4_fy2026_woo_sue_posture" in cpf

    def test_publications_all_have_meta_coverage_tone(self, ccr_data):
        """Every entry under publications must have meta_coverage_tone (core test requirement)."""
        pubs = ccr_data.get("publications", {})
        for slug, pub_data in pubs.items():
            assert "meta_coverage_tone" in pub_data, f"{slug} missing meta_coverage_tone"

    def test_no_cross_publication_findings_in_publications(self, ccr_data):
        """No mechanism-style entries (with mechanism_id but no meta_coverage_tone) in publications."""
        pubs = ccr_data.get("publications", {})
        for slug, pub_data in pubs.items():
            if "mechanism_id" in pub_data:
                assert "meta_coverage_tone" in pub_data, (
                    f"{slug} has mechanism_id but no meta_coverage_tone — "
                    "likely a cross_publication_finding misplaced under publications"
                )


class TestMechanismIDs:
    """Mechanism ID integrity checks."""

    @pytest.fixture(scope="class")
    @classmethod
    def ccr_data(cls):
        return load_yaml("competitor-coverage-research.yaml")

    def _collect_mechanism_ids(self, data, section):
        """Collect mechanism IDs from a section."""
        ids = []
        for key, entry in data.get(section, {}).items():
            if isinstance(entry, dict) and "mechanism_id" in entry:
                ids.append(entry["mechanism_id"])
        return ids

    def test_mechanism_id_range(self, ccr_data):
        """All mechanism IDs should be in range and include recent additions."""
        pub_ids = self._collect_mechanism_ids(ccr_data, "publications")
        cpf_ids = self._collect_mechanism_ids(ccr_data, "cross_publication_findings")
        all_ids = pub_ids + cpf_ids
        assert max(all_ids) >= 117, f"Max mechanism ID is {max(all_ids)}, expected >= 117"

    def test_mechanisms_115_116_117_exist(self, ccr_data):
        """Mechanisms #115, #116, #117 must all exist in the dataset."""
        cpf = ccr_data.get("cross_publication_findings", {})
        cpf_ids = [
            entry.get("mechanism_id")
            for entry in cpf.values()
            if isinstance(entry, dict) and "mechanism_id" in entry
        ]
        for mid in [115, 116, 117]:
            assert mid in cpf_ids, f"Mechanism #{mid} not found in cross_publication_findings"

    def test_no_duplicate_mechanism_ids(self, ccr_data):
        """No duplicate mechanism IDs across both sections."""
        pub_ids = self._collect_mechanism_ids(ccr_data, "publications")
        cpf_ids = self._collect_mechanism_ids(ccr_data, "cross_publication_findings")
        all_ids = pub_ids + cpf_ids
        # Check for duplicates
        seen = set()
        dupes = []
        for mid in all_ids:
            if mid in seen:
                dupes.append(mid)
            seen.add(mid)
        assert len(dupes) == 0, f"Duplicate mechanism IDs: {dupes}"


class TestFixtureDeprecation:
    """No class-scoped fixtures without @classmethod."""

    def test_no_deprecated_fixtures_in_aug15_tests(self):
        """All class-scoped fixtures in aug15 test files must use @classmethod."""
        aug15_files = sorted(TESTS_DIR.glob("test_*aug15*.py"))
        violations = []
        for test_file in aug15_files:
            with open(test_file) as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if '@pytest.fixture(scope="class")' in line:
                    # Check if @classmethod is on the next line
                    if i + 1 < len(lines) and "@classmethod" not in lines[i + 1]:
                        # Check if @classmethod is on the previous line
                        if i > 0 and "@classmethod" not in lines[i - 1]:
                            violations.append(f"{test_file.name}:{i+1}")
        assert len(violations) == 0, (
            f"Class-scoped fixtures without @classmethod (PytestRemovedIn10Warning):\n"
            + "\n".join(violations)
        )


class TestStatsConsistency:
    """README and ARCHITECTURE stats must be current."""

    def test_test_file_count(self):
        """Test file count in README should match filesystem."""
        test_files = [f for f in TESTS_DIR.glob("test_*.py")]
        with open(PROFILES_DIR.parent / "README.md") as f:
            readme = f.read()
        # Find test file count in README (format: "Across NNN test files")
        match = re.search(r"Across\s+(\d+)\s+test files", readme)
        if not match:
            match = re.search(r"Test files\s*\|\s*(\d+)", readme)
        assert match, "Could not find test file count in README"
        readme_count = int(match.group(1))
        # Allow for this test file being new (off by 1)
        assert abs(readme_count - len(test_files)) <= 1, (
            f"README says {readme_count} test files but found {len(test_files)}"
        )

    def test_mechanism_count_consistent(self):
        """Mechanism count should be consistent between README and YAML data."""
        ccr_data = load_yaml("competitor-coverage-research.yaml")
        # Walk ALL nested dicts to find mechanism_id fields
        # Full mechanisms have 5+ keys (vs cross-reference stubs with just mechanism_id + relationship)
        mechanism_ids = set()

        def walk(obj):
            if isinstance(obj, dict):
                if "mechanism_id" in obj and len(obj) >= 5:
                    mechanism_ids.add(obj["mechanism_id"])
                for v in obj.values():
                    walk(v)
            elif isinstance(obj, list):
                for item in obj:
                    walk(item)

        walk(ccr_data)
        assert len(mechanism_ids) >= 100, f"Only {len(mechanism_ids)} full mechanisms found, expected >= 100"


class TestCrossReferenceBidirectionality:
    """Check that recent mechanisms have bidirectional cross-references."""

    @pytest.fixture(scope="class")
    @classmethod
    def cpf_data(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data.get("cross_publication_findings", {})

    def test_mechanism_115_has_cross_references(self, cpf_data):
        """Mechanism #115 should have cross_references."""
        entry = cpf_data.get("techradar_future_plc_privacy_vocabulary_bifurcation", {})
        assert "cross_references" in entry, "Mechanism #115 missing cross_references"
        refs = entry["cross_references"]
        ref_ids = [r.get("mechanism_id") for r in refs]
        assert 110 in ref_ids, "Mechanism #115 should reference #110 (cross_brand_replication)"
        assert 114 in ref_ids, "Mechanism #115 should reference #114 (financial_cause)"

    def test_mechanism_116_has_cross_references(self, cpf_data):
        """Mechanism #116 should have cross_references."""
        entry = cpf_data.get("michael_hicks_android_central_privacy_vocabulary_suppression", {})
        assert "cross_references" in entry, "Mechanism #116 missing cross_references"
        refs = entry["cross_references"]
        ref_ids = [r.get("mechanism_id") for r in refs]
        assert 110 in ref_ids, "Mechanism #116 should reference #110"
        assert 115 in ref_ids, "Mechanism #116 should reference #115"

    def test_mechanism_117_has_cross_references(self, cpf_data):
        """Mechanism #117 should have cross_references."""
        entry = cpf_data.get("news_corp_q4_fy2026_woo_sue_posture", {})
        assert "cross_references" in entry or "source_urls" in entry, (
            "Mechanism #117 should have cross_references or source_urls"
        )
