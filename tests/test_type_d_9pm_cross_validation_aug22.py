"""
Type D cross-validation (Aug 22, 9 PM PT):
Fixes: duplicate mechanism ID 236 (MacRumors→240, ICE/DHS stays 236),
mechanism #239 added to competitor-coverage-research.yaml (Condé Nast Snap Discover),
snap_specs_clad test updated for 5th financial axis,
doc sync (548→549 test files, ~20000 tests),
2 missing aug22 test files added to README/ARCHITECTURE.

Test count: 549
"""

import os
import glob
import yaml
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


class TestDuplicateMechanismIdFix(unittest.TestCase):
    """Verify mechanism ID 236 duplicate was resolved."""

    def _load_research(self):
        with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
            return yaml.safe_load(f)

    def test_mechanism_236_is_unique(self):
        """ID 236 should appear exactly once in cross_publication_findings + publications."""
        data = self._load_research()
        ids = []
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "mechanism_id" in val:
                    if val["mechanism_id"] == 236:
                        ids.append(key)
        assert len(ids) == 1, f"mechanism_id 236 appears in {len(ids)} entries: {ids}"

    def test_mechanism_240_exists(self):
        """MacRumors Show was renumbered to 240."""
        data = self._load_research()
        found = False
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 240:
                    found = True
                    assert "MacRumors" in val.get("name", ""), \
                        f"Mechanism 240 should be MacRumors Show, got: {val.get('name')}"
        assert found, "Mechanism 240 (renumbered MacRumors Show) not found"

    def test_no_duplicate_mechanism_ids(self):
        """No mechanism ID appears more than once across sections."""
        data = self._load_research()
        ids = []
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "mechanism_id" in val:
                    ids.append(val["mechanism_id"])
        duplicates = [x for x in ids if ids.count(x) > 1]
        assert not duplicates, f"Duplicate mechanism IDs: {set(duplicates)}"


class TestMechanism239Added(unittest.TestCase):
    """Verify mechanism #239 (Condé Nast Snap Discover) was added."""

    def _load_research(self):
        with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
            return yaml.safe_load(f)

    def test_mechanism_239_exists(self):
        data = self._load_research()
        found = False
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 239:
                    found = True
        assert found, "Mechanism 239 not found in YAML"

    def test_mechanism_239_is_type_c(self):
        data = self._load_research()
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 239:
                    assert val["type"] == "C", f"Mechanism 239 type should be C, got {val['type']}"
                    return
        self.fail("Mechanism 239 not found")

    def test_mechanism_239_has_source_urls(self):
        data = self._load_research()
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 239:
                    urls = val.get("source_urls", [])
                    assert len(urls) >= 4, f"Mechanism 239 should have 4+ source URLs, got {len(urls)}"
                    return

    def test_mechanism_239_has_confounding_factors(self):
        data = self._load_research()
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 239:
                    cfs = val.get("confounding_factors", [])
                    assert len(cfs) >= 4, f"Expected 4+ confounders, got {len(cfs)}"
                    return

    def test_no_contiguity_gaps_above_200(self):
        """All mechanism IDs from 201 to max should be present."""
        data = self._load_research()
        ids = set()
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "mechanism_id" in val:
                    ids.add(val["mechanism_id"])
        above_200 = {i for i in ids if i > 200}
        if above_200:
            max_id = max(above_200)
            expected = set(range(201, max_id + 1))
            # Known gaps — IDs that were skipped, reserved, or consolidated
            known_gaps = {241, 244, 249, 250, 258, 259, 260, 261, 264}
            missing = expected - ids - known_gaps
            assert not missing, f"Gaps in mechanism IDs above 200 (excluding known): {sorted(missing)}"


class TestDocSync(unittest.TestCase):
    """Verify doc files reflect current test count."""

    def test_test_file_count_is_550(self):
        actual = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        assert actual >= 550, f"Expected at least 550 test files, got {actual}"

    def test_readme_mentions_test_count(self):
        with open(os.path.join(REPO_ROOT, "README.md")) as f:
            content = f.read()
        actual = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        assert str(actual) in content, f"README should mention {actual} test files"

    def test_architecture_mentions_test_count(self):
        with open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")) as f:
            content = f.read()
        actual = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        assert str(actual) in content, f"ARCHITECTURE should mention {actual} test files"

    def test_all_aug22_files_in_readme(self):
        aug22_files = [os.path.basename(f) for f in glob.glob(os.path.join(TESTS_DIR, "test_*aug22*.py"))]
        with open(os.path.join(REPO_ROOT, "README.md")) as f:
            content = f.read()
        missing = [f for f in aug22_files if f not in content]
        assert not missing, f"Aug 22 files missing from README: {missing}"

    def test_all_aug22_files_in_architecture(self):
        aug22_files = [os.path.basename(f) for f in glob.glob(os.path.join(TESTS_DIR, "test_*aug22*.py"))]
        with open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")) as f:
            content = f.read()
        missing = [f for f in aug22_files if f not in content]
        assert not missing, f"Aug 22 files missing from ARCHITECTURE: {missing}"


class TestSnapSpecsQuintupleAxis(unittest.TestCase):
    """Verify snap_specs_clad test acknowledges 5th financial axis."""

    def test_competitor_entities_has_5_axes(self):
        with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
            data = yaml.safe_load(f)
        snap = data.get("snap", data.get("snap_inc", {}))
        if "hardware_devices" in snap:
            specs = snap["hardware_devices"].get("specs_consumer", {})
            clad = specs.get("clad_developer_ecosystem", {})
            axes = clad.get("publisher_financial_alignment_axes_snap", 0)
            assert axes >= 5, f"Expected 5+ axes after Discover addition, got {axes}"


if __name__ == "__main__":
    unittest.main()
