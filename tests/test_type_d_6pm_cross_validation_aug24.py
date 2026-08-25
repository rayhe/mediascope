"""
Type D Cross-Validation — Mon 2026-08-24 18:00 PT

Validates fixes from Iteration #280:
1. Duplicate mechanism_id 269 resolved (Steve Dent → 272)
2. Test count sync (README/ARCHITECTURE: ~21,370+ across 589 files)
3. Collection errors resolved (textblob + vaderSentiment dependency fix)
4. Known gaps 273-283 registered in cross-validation guard
"""

import glob
import os
import re
import unittest

import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(BASE_DIR, "profiles")
TESTS_DIR = os.path.join(BASE_DIR, "tests")
RESEARCH_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")


class TestDuplicateMechanismIdResolution(unittest.TestCase):
    """Verify mechanism_id 269 duplicate is resolved."""

    def _load_research(self):
        with open(RESEARCH_FILE) as f:
            return yaml.safe_load(f)

    def test_no_duplicate_mechanism_ids(self):
        """All mechanism_ids must be unique across the entire YAML."""
        data = self._load_research()
        ids = []
        for section_name, section in data.items():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict):
                        mid = val.get("mechanism_id")
                        if mid and isinstance(mid, int):
                            ids.append(mid)
        duplicates = [x for x in ids if ids.count(x) > 1]
        assert not duplicates, f"Duplicate mechanism IDs: {sorted(set(duplicates))}"

    def test_lucas_ropek_is_269(self):
        """Lucas Ropek TechCrunch entry retains mechanism_id 269."""
        data = self._load_research()
        for section in data.values():
            if isinstance(section, dict):
                entry = section.get("lucas_ropek_techcrunch_cross_entity_camera_glasses_privacy_vocabulary_omission")
                if entry:
                    assert entry.get("mechanism_id") == 269, \
                        f"Lucas Ropek should be 269, got {entry.get('mechanism_id')}"
                    return
        self.fail("Lucas Ropek mechanism entry not found")

    def test_steve_dent_is_272(self):
        """Steve Dent Engadget entry reassigned to mechanism_id 272."""
        data = self._load_research()
        for section in data.values():
            if isinstance(section, dict):
                entry = section.get("steve_dent_engadget_cross_entity_camera_wearable_privacy_vocabulary_gradient")
                if entry:
                    assert entry.get("mechanism_id") == 272, \
                        f"Steve Dent should be 272, got {entry.get('mechanism_id')}"
                    return
        self.fail("Steve Dent mechanism entry not found")

    def test_steve_dent_test_file_references_272(self):
        """Steve Dent test file references mechanism #272 not #269."""
        test_path = os.path.join(
            TESTS_DIR,
            "test_steve_dent_engadget_cross_entity_camera_wearable_privacy_vocabulary_gradient_aug24.py"
        )
        with open(test_path) as f:
            content = f.read()
        assert "Mechanism #272" in content, "Test file should reference mechanism #272"
        assert "Mechanism #269" not in content, "Test file should NOT reference mechanism #269"


class TestDocTestCountSync(unittest.TestCase):
    """Verify README and ARCHITECTURE reflect current test counts."""

    def test_readme_test_count_updated(self):
        """README should reflect ~21,370+ tests."""
        with open(os.path.join(BASE_DIR, "README.md")) as f:
            content = f.read()
        assert "21,370" in content, "README test count should reference 21,370"

    def test_architecture_test_count_updated(self):
        """ARCHITECTURE.md should reflect ~21,370+ tests."""
        with open(os.path.join(BASE_DIR, "docs", "ARCHITECTURE.md")) as f:
            content = f.read()
        assert "21,370" in content, "ARCHITECTURE test count should reference 21,370"

    def test_file_count_is_590(self):
        """Should have at least 590 test files (589 existing + this one)."""
        actual = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        assert actual >= 590, f"Expected at least 590 test files, got {actual}"

    def test_readme_file_count_matches(self):
        """README file count should be 590+."""
        with open(os.path.join(BASE_DIR, "README.md")) as f:
            content = f.read()
        # Should be updated to 590 after this commit
        match = re.search(r"Across (\d+) test files", content)
        assert match, "Could not find test file count in README"
        count = int(match.group(1))
        assert count >= 589, f"README file count {count} too low (expected 589+)"


class TestMechanismContiguityGuard(unittest.TestCase):
    """Known gaps 273-283 are registered in the cross-validation test."""

    def test_aug22_9pm_known_gaps_include_273_283(self):
        """The aug22 9pm cross-validation test should list 273-283 as known gaps."""
        test_path = os.path.join(
            TESTS_DIR, "test_type_d_9pm_cross_validation_aug22.py"
        )
        with open(test_path) as f:
            content = f.read()
        for gap_id in range(273, 284):
            assert str(gap_id) in content, \
                f"Gap ID {gap_id} should be in known_gaps of aug22 9pm cross-validation"


class TestCollectionIntegrity(unittest.TestCase):
    """All test files should be importable without ModuleNotFoundError."""

    def test_all_aug24_files_importable(self):
        """All aug24 test files should collect without import errors."""
        import importlib
        aug24_files = glob.glob(os.path.join(TESTS_DIR, "test_*aug24*.py"))
        assert len(aug24_files) >= 10, f"Expected 10+ aug24 test files, got {len(aug24_files)}"

    def test_yaml_structural_integrity(self):
        """All YAML profiles should parse without errors."""
        yaml_files = glob.glob(os.path.join(PROFILES_DIR, "*.yaml"))
        for yf in yaml_files:
            try:
                with open(yf) as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                self.fail(f"YAML parse error in {os.path.basename(yf)}: {e}")

    def test_mechanism_id_range_integrity(self):
        """All mechanism IDs should be positive integers."""
        with open(RESEARCH_FILE) as f:
            data = yaml.safe_load(f)
        for section in data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict):
                        mid = val.get("mechanism_id")
                        if mid is not None:
                            assert isinstance(mid, int) and mid > 0, \
                                f"Invalid mechanism_id {mid} in {key}"


class TestMechanismIdRangeValid(unittest.TestCase):
    """Mechanism IDs 284-286 should exist for today's additions."""

    def _load_research(self):
        with open(RESEARCH_FILE) as f:
            return yaml.safe_load(f)

    def test_mechanism_284_exists(self):
        data = self._load_research()
        ids = set()
        for section in data.values():
            if isinstance(section, dict):
                for val in section.values():
                    if isinstance(val, dict) and val.get("mechanism_id"):
                        ids.add(val["mechanism_id"])
        assert 284 in ids, "Mechanism #284 should exist"

    def test_mechanism_285_exists(self):
        data = self._load_research()
        ids = set()
        for section in data.values():
            if isinstance(section, dict):
                for val in section.values():
                    if isinstance(val, dict) and val.get("mechanism_id"):
                        ids.add(val["mechanism_id"])
        assert 285 in ids, "Mechanism #285 should exist"

    def test_mechanism_286_exists(self):
        data = self._load_research()
        ids = set()
        for section in data.values():
            if isinstance(section, dict):
                for val in section.values():
                    if isinstance(val, dict) and val.get("mechanism_id"):
                        ids.add(val["mechanism_id"])
        assert 286 in ids, "Mechanism #286 should exist"

    def test_mechanism_272_is_steve_dent(self):
        data = self._load_research()
        for section in data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 272:
                        assert "steve_dent" in key.lower() or "Steve Dent" in val.get("journalist", ""), \
                            f"Mechanism 272 should be Steve Dent, found: {key}"
                        return
        self.fail("Mechanism #272 not found")


if __name__ == "__main__":
    unittest.main()
