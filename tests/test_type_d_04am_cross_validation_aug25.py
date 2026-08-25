"""
Type D cross-validation (Aug 25, 04:00 PT):

Fixes applied this iteration:
1. YAML structure fix: 3 list-item mechanism entries (288, 292, 293) converted to
   named mapping keys under publications: section. Was causing yaml.parser.ParserError
   ("expected <block end>, but found '-'") that broke 2 test files on collection.
2. Duplicate mechanism_id fix: Daniel Cooper (mech 293) duplicated Jonny Evans (293) →
   renumbered Cooper to 295.
3. Missing fixture fix: test_conde_nast_post_search_openai_citation_dependency_financial
   _architecture_aug25.py missing competitor_research fixture + publications path →
   added imports (os, yaml), PROFILES_DIR, fixture, and .get("publications", {}) wrapper.
4. Stale assertion fixes: Steve Dent mechanism_id 269→272, Anthropic IPO banks 3→4
   (added Citigroup), doc test count strings, README/ARCHITECTURE file counts 601/600→599.

Validates: YAML integrity, mechanism ID uniqueness, doc count sync, recent mechanism
structural integrity, fixture availability.
"""

import glob
import os
import re
import unittest
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests")
PROFILES_DIR = os.path.join(BASE_DIR, "profiles")


def _load_research():
    with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


class TestYAMLStructuralIntegrity(unittest.TestCase):
    """YAML parses without errors after list-item to mapping-key conversion."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_research()
        cls.pubs = cls.data.get("publications", {})

    def test_yaml_parses_successfully(self):
        """competitor-coverage-research.yaml should parse without errors."""
        self.assertIsInstance(self.data, dict)

    def test_publications_is_mapping(self):
        """Publications section should be a mapping, not a list."""
        self.assertIsInstance(self.pubs, dict)

    def test_no_list_items_at_publications_level(self):
        """No list items should exist at the publications level."""
        self.assertNotIsInstance(self.pubs, list)

    def test_mechanism_288_is_named_key(self):
        """Mechanism #288 (WSJ Amrith Ramkumar) is a named mapping key."""
        key = "wsj_amrith_ramkumar_data_retention_vocabulary_bifurcation"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 288)

    def test_mechanism_292_is_named_key(self):
        """Mechanism #292 (Chandra Steele) is a named mapping key."""
        key = "chandra_steele_android_police_cross_entity_camera_privacy_displacement"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 292)

    def test_mechanism_295_is_named_key(self):
        """Mechanism #295 (Daniel Cooper) is a named mapping key (renumbered from 293)."""
        key = "daniel_cooper_engadget_within_review_cross_entity_privacy_benchmark_inversion"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 295)

    def test_mechanism_293_is_jonny_evans_only(self):
        """Mechanism #293 belongs only to Jonny Evans (was duplicated with Cooper)."""
        key = "jonny_evans_computerworld_appleholic_cross_entity_privacy_champion_vocabulary_bifurcation"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 293)


class TestNoDuplicateMechanismIds(unittest.TestCase):
    """All mechanism_ids across the YAML must be unique."""

    def test_no_duplicate_mechanism_ids(self):
        data = _load_research()
        ids = []
        for section_name, section in data.items():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict):
                        mid = val.get("mechanism_id")
                        if mid and isinstance(mid, int):
                            ids.append(mid)
        dupes = [x for x in set(ids) if ids.count(x) > 1]
        self.assertEqual(dupes, [], f"Duplicate mechanism IDs: {dupes}")


class TestDocCountSync(unittest.TestCase):
    """README and ARCHITECTURE file counts match actual test files on disk."""

    @classmethod
    def setUpClass(cls):
        cls.actual_count = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        with open(os.path.join(BASE_DIR, "README.md")) as f:
            cls.readme = f.read()
        with open(os.path.join(BASE_DIR, "docs", "ARCHITECTURE.md")) as f:
            cls.arch = f.read()

    def test_readme_file_count_matches_actual(self):
        m = re.search(r"Across (\d+) test files", self.readme)
        self.assertIsNotNone(m, "README should state test file count")
        self.assertEqual(int(m.group(1)), self.actual_count)

    def test_architecture_file_count_matches_actual(self):
        m = re.search(r"(\d+)\s*test files", self.arch)
        self.assertIsNotNone(m, "ARCHITECTURE should state test file count")
        self.assertEqual(int(m.group(1)), self.actual_count)

    def test_at_least_599_test_files(self):
        """Should have at least 599 test files."""
        self.assertGreaterEqual(self.actual_count, 599)


class TestCondeNastAug25FixtureAvailability(unittest.TestCase):
    """The Condé Nast post-search test can import and collect without errors."""

    def test_fixture_available(self):
        """competitor_research fixture is defined in the test file."""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cn_test",
            os.path.join(TESTS_DIR,
                         "test_conde_nast_post_search_openai_citation_dependency_financial_architecture_aug25.py")
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertTrue(hasattr(mod, "competitor_research"),
                        "competitor_research fixture should be defined")


class TestAnthropicIPOBanksUpdated(unittest.TestCase):
    """Anthropic IPO underwriter banks include Citigroup (4 banks total)."""

    def test_four_ipo_banks(self):
        with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
            entities = yaml.safe_load(f)
        anthropic = entities.get("entities", {}).get("anthropic", {})
        ipo = anthropic.get("ipo_filing", {})
        banks = ipo.get("ipo_banks_reported", [])
        self.assertIn("Citigroup", banks)
        self.assertEqual(len(banks), 4)


class TestMaxMechanismId(unittest.TestCase):
    """Highest mechanism_id should be >= 295 (Daniel Cooper renumbered, grew since)."""

    def test_max_mechanism_id(self):
        data = _load_research()
        max_id = 0
        for section in data.values():
            if isinstance(section, dict):
                for val in section.values():
                    if isinstance(val, dict):
                        mid = val.get("mechanism_id", 0)
                        if isinstance(mid, int) and mid > max_id:
                            max_id = mid
        self.assertGreaterEqual(max_id, 295)
