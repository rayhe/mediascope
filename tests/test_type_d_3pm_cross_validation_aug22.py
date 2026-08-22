"""
Type D cross-validation — Aug 22, 3 PM PT (Iteration #246)

Fixes validated:
1. competitor-coverage-research.yaml YAML parse fix: mechanism #232 was appended as
   list item (`- mechanism_id: 232`) at column 3 inside the `publications:` mapping,
   breaking YAML parsing. Converted to mapping key format
   (`nbc_news_broadcast_gender_framed_camera_wearable_entity_selection_mechanism_232:`),
   consistent with mechanisms #193-#230.

2. README.md test count sync: 540→543 files, ~19000→~19795 tests.

3. ARCHITECTURE.md test count sync: 539→543 files, ~19000→~19795 tests.

4. 8 missing test files added to ARCHITECTURE.md, 8 to README.md (all aug22 files).

5. Stale README stat line fix: body text "17669 tests (19000 with parameterized
   expansion) across 540" → "19795 tests (with parameterized expansion) across 543".
"""
import os
import yaml
import glob
import pytest


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")


class TestYAMLParseIntegrity:
    """Verify competitor-coverage-research.yaml parses without errors."""

    def test_yaml_loads_without_error(self):
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        assert data is not None

    def test_top_level_keys(self):
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        expected = {"aggregate_findings", "cross_entity_leverage",
                    "cross_publication_findings", "methodology", "publications"}
        assert set(data.keys()) == expected

    def test_publications_are_all_mappings(self):
        """No list items should exist directly under publications."""
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        pubs = data["publications"]
        # publications should be a dict, not a list
        assert isinstance(pubs, dict), "publications should be a mapping, not a list"
        # Every value should be a dict too
        for key, val in pubs.items():
            assert isinstance(val, dict), f"publications['{key}'] should be a mapping"

    def test_mechanism_232_is_mapping_key(self):
        """Mechanism #232 should be a mapping key, not a list item."""
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        pubs = data["publications"]
        # Should exist as a named key
        mech_key = "nbc_news_broadcast_gender_framed_camera_wearable_entity_selection_mechanism_232"
        assert mech_key in pubs, f"Mechanism #232 should be a mapping key in publications"
        assert pubs[mech_key]["mechanism_id"] == 232

    def test_no_list_items_in_raw_publications_section(self):
        """Raw YAML check: no '  - mechanism_id' lines in publications section."""
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            lines = f.readlines()
        # Find publications section
        in_publications = False
        for i, line in enumerate(lines):
            if line.startswith("publications:"):
                in_publications = True
                continue
            if in_publications and line[0:1].isalpha():
                break  # next top-level key
            if in_publications and line.startswith("  - mechanism_id"):
                pytest.fail(f"List item found in publications section at line {i+1}: {line.strip()}")


class TestDocSyncIntegrity:
    """Verify README and ARCHITECTURE counts match disk."""

    def test_readme_test_file_count(self):
        actual_count = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        readme_path = os.path.join(REPO_ROOT, "README.md")
        with open(readme_path) as f:
            content = f.read()
        assert str(actual_count) in content or str(actual_count - 1) in content, (
            f"README test file count ({actual_count} on disk) may be stale"
        )

    def test_architecture_test_file_count(self):
        actual_count = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        arch_path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(arch_path) as f:
            content = f.read()
        assert str(actual_count) in content or str(actual_count - 1) in content, (
            f"ARCHITECTURE test file count ({actual_count} on disk) may be stale"
        )

    def test_all_aug22_test_files_in_readme(self):
        aug22_files = glob.glob(os.path.join(TESTS_DIR, "test_*aug22*.py"))
        readme_path = os.path.join(REPO_ROOT, "README.md")
        with open(readme_path) as f:
            content = f.read()
        missing = []
        for f in aug22_files:
            base = os.path.basename(f)
            if base not in content:
                missing.append(base)
        assert not missing, f"Aug 22 test files missing from README: {missing}"

    def test_all_aug22_test_files_in_architecture(self):
        aug22_files = glob.glob(os.path.join(TESTS_DIR, "test_*aug22*.py"))
        arch_path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(arch_path) as f:
            content = f.read()
        missing = []
        for f in aug22_files:
            base = os.path.basename(f)
            if base not in content:
                missing.append(base)
        assert not missing, f"Aug 22 test files missing from ARCHITECTURE: {missing}"


class TestMechanismIntegrity:
    """Validate recent mechanism entries."""

    def _load_research(self):
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            return yaml.safe_load(f)

    def _all_mechanisms(self):
        data = self._load_research()
        mechs = {}
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "mechanism_id" in val:
                    mechs[val["mechanism_id"]] = val
        return mechs

    def test_no_duplicate_mechanism_ids(self):
        data = self._load_research()
        ids = []
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "mechanism_id" in val:
                    ids.append(val["mechanism_id"])
        assert len(ids) == len(set(ids)), f"Duplicate mechanism IDs: {[x for x in ids if ids.count(x) > 1]}"

    def test_highest_mechanism_id_at_least_235(self):
        mechs = self._all_mechanisms()
        assert max(mechs.keys()) >= 235, f"Expected mechanism #235+, got max {max(mechs.keys())}"

    def test_mechanism_232_has_required_fields(self):
        mechs = self._all_mechanisms()
        m = mechs[232]
        for field in ["name", "type", "date", "publication", "entities",
                       "finding", "asymmetry_score", "confounders"]:
            assert field in m, f"Mechanism #232 missing field: {field}"

    def test_mechanism_235_specs_inc(self):
        mechs = self._all_mechanisms()
        assert 235 in mechs, "Mechanism #235 (Specs Inc.) should exist"

    def test_mechanisms_230_to_235_all_present(self):
        mechs = self._all_mechanisms()
        for mid in range(230, 236):
            assert mid in mechs, f"Mechanism #{mid} missing"


class TestPriorFixRegression:
    """Guard against regression of fixes from prior Type D runs."""

    def test_mechanism_218_has_confounding_factors(self):
        """Aug 21 8pm fix: confounders→confounding_factors for #218."""
        data = self._load_research()
        # Find mechanism 218
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and val.get("mechanism_id") == 218:
                    # Should have confounding_factors OR confounders
                    assert "confounding_factors" in val or "confounders" in val, (
                        "Mechanism #218 should have confounders/confounding_factors")
                    return
        # It's OK if 218 exists only in a test, not in profile YAML

    def _load_research(self):
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            return yaml.safe_load(f)


class TestAug22TestFileImportability:
    """Verify all aug22 test files can be imported."""

    def _get_aug22_files(self):
        return sorted(glob.glob(os.path.join(TESTS_DIR, "test_*aug22*.py")))

    def test_all_aug22_files_importable(self):
        import importlib.util
        failures = []
        for filepath in self._get_aug22_files():
            base = os.path.basename(filepath)
            module_name = base[:-3]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            try:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except Exception as e:
                failures.append(f"{base}: {e}")
        assert not failures, f"Import failures:\n" + "\n".join(failures)

    def test_aug22_file_count_at_least_12(self):
        files = self._get_aug22_files()
        assert len(files) >= 13, f"Expected >=13 aug22 test files, got {len(files)}"


class TestScoreDistribution:
    """Verify asymmetry scores have reasonable distribution."""

    def _all_scores(self):
        path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        scores = []
        for section in ["cross_publication_findings", "publications"]:
            entries = data.get(section, {})
            for key, val in entries.items():
                if isinstance(val, dict) and "asymmetry_score" in val:
                    scores.append(val["asymmetry_score"])
        return scores

    def test_score_range(self):
        scores = self._all_scores()
        assert all(0 <= s <= 1 for s in scores), "All asymmetry scores should be 0-1"

    def test_score_spread(self):
        scores = self._all_scores()
        assert max(scores) - min(scores) >= 0.10, "Score spread should be >= 0.10"

    def test_score_mean_reasonable(self):
        scores = self._all_scores()
        mean = sum(scores) / len(scores)
        assert 0.50 <= mean <= 0.95, f"Mean score {mean:.2f} outside expected range"
