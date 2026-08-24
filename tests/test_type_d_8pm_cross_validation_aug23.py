"""
Type D cross-validation — Sun 2026-08-23 8 PM PT

Fixes validated in this iteration:
1. YAML parse fix: mechanism #257 was a list item (`- mechanism_id: 257`) under
   `publications:` which expects mapping keys — converted to named key
   `anthropic_2t_ipo_publisher_financial_captivity_acceleration`
2. String mechanism_ids in cross-references (TWiT_451_podcast, mia_sato_cross_entity,
   ziff_davis_financial) replaced with proper integer IDs (261, 215, 108)
3. Missing `meta_coverage_tone` added to 2 new publication entries
4. Missing test file `test_abrar_al_heeti_cnet...aug23.py` added to README + ARCHITECTURE
5. File count updated from 565 → 570 in prior Type D tests
6. textblob dependency restored for sentiment analysis tests
"""

import glob
import os
import unittest
from pathlib import Path

import yaml

REPO_DIR = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_DIR / "tests"
YAML_PATH = REPO_DIR / "profiles" / "competitor-coverage-research.yaml"
README_PATH = REPO_DIR / "README.md"
ARCH_PATH = REPO_DIR / "docs" / "ARCHITECTURE.md"


def _load_yaml():
    with open(YAML_PATH) as f:
        return yaml.safe_load(f)


def _extract_all_mechanisms(d, out=None):
    """Extract all mechanism_id values from nested YAML structure."""
    if out is None:
        out = {}
    if isinstance(d, dict):
        if "mechanism_id" in d:
            mid = d["mechanism_id"]
            if mid not in out or len(d) > len(out[mid]):
                out[mid] = d
        for v in d.values():
            _extract_all_mechanisms(v, out)
    elif isinstance(d, list):
        for item in d:
            _extract_all_mechanisms(item, out)
    return out


class TestYAMLParsesClean(unittest.TestCase):
    """The YAML file must parse without errors."""

    def test_yaml_loads(self):
        data = _load_yaml()
        self.assertIsInstance(data, dict)
        self.assertIn("publications", data)

    def test_publications_are_mapping_keys(self):
        """No list items directly under publications — all must be named keys."""
        data = _load_yaml()
        pubs = data.get("publications", {})
        self.assertIsInstance(pubs, dict, "publications should be a mapping, not a list")
        for key in pubs:
            self.assertIsInstance(key, str, f"Publication key {key!r} should be a string")


class TestFileCount(unittest.TestCase):
    """Verify total test file count is 571 (570 prior + this file)."""

    def test_actual_test_file_count(self):
        files = glob.glob(str(TESTS_DIR / "test_*.py"))
        actual = len(files)
        self.assertEqual(actual, 571, f"Expected 571 test files, got {actual}")


class TestMechanismIdTypes(unittest.TestCase):
    """All mechanism_id values must be integers (or None for placeholder entries)."""

    def test_no_string_mechanism_ids(self):
        data = _load_yaml()
        mechs = _extract_all_mechanisms(data)
        string_ids = [
            (mid, type(mid).__name__)
            for mid in mechs
            if mid is not None and not isinstance(mid, int)
        ]
        self.assertEqual(
            len(string_ids), 0,
            f"Found string mechanism_ids (should be integers): {string_ids}"
        )

    def test_mechanism_257_exists(self):
        """Mechanism #257 (Anthropic $2T IPO) must exist as a proper mapping key."""
        data = _load_yaml()
        pubs = data.get("publications", {})
        entry = pubs.get("anthropic_2t_ipo_publisher_financial_captivity_acceleration")
        self.assertIsNotNone(entry, "Mechanism #257 entry not found in publications")
        self.assertEqual(entry.get("mechanism_id"), 257)

    def test_mechanism_255_exists(self):
        """Mechanism #255 (Abrar Al-Heeti) must exist."""
        data = _load_yaml()
        pubs = data.get("publications", {})
        entry = pubs.get(
            "abrar_al_heeti_cnet_cross_entity_cross_medium_camera_wearable_privacy_vocabulary_bifurcation"
        )
        self.assertIsNotNone(entry, "Mechanism #255 entry not found")
        self.assertEqual(entry.get("mechanism_id"), 255)


class TestMetaCoverageToneCompleteness(unittest.TestCase):
    """Every publication entry must have meta_coverage_tone."""

    def test_all_publications_have_meta_coverage_tone(self):
        data = _load_yaml()
        pubs = data.get("publications", {})
        missing = [name for name, pub in pubs.items()
                   if "meta_coverage_tone" not in pub]
        self.assertEqual(
            len(missing), 0,
            f"Missing meta_coverage_tone: {missing}"
        )


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Cross-references within publication entries use integer mechanism_ids."""

    def test_abrar_cross_refs_are_integers(self):
        data = _load_yaml()
        pubs = data.get("publications", {})
        entry = pubs.get(
            "abrar_al_heeti_cnet_cross_entity_cross_medium_camera_wearable_privacy_vocabulary_bifurcation",
            {}
        )
        xrefs = entry.get("cross_references", [])
        for xref in xrefs:
            if isinstance(xref, dict) and "mechanism_id" in xref:
                self.assertIsInstance(
                    xref["mechanism_id"], int,
                    f"Cross-reference mechanism_id should be int, got {xref['mechanism_id']!r}"
                )

    def test_anthropic_cross_refs_are_integers(self):
        data = _load_yaml()
        pubs = data.get("publications", {})
        entry = pubs.get(
            "anthropic_2t_ipo_publisher_financial_captivity_acceleration", {}
        )
        xrefs = entry.get("cross_references", [])
        for xref in xrefs:
            if isinstance(xref, dict) and "mechanism_id" in xref:
                self.assertIsInstance(
                    xref["mechanism_id"], int,
                    f"Cross-reference mechanism_id should be int, got {xref['mechanism_id']!r}"
                )


class TestMechanismContiguity(unittest.TestCase):
    """Document known mechanism ID gaps above 200."""

    @classmethod
    def setUpClass(cls):
        data = _load_yaml()
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_known_gaps_documented(self):
        """Gaps are expected from non-sequential creation."""
        above_200 = sorted(
            mid for mid in self.mechanisms
            if isinstance(mid, int) and mid >= 200
        )
        gaps = []
        for i in range(1, len(above_200)):
            if above_200[i] - above_200[i - 1] > 1:
                gaps.extend(range(above_200[i - 1] + 1, above_200[i]))
        known_gaps = {241, 242, 244, 249, 250, 258, 259, 260}
        unexpected = set(gaps) - known_gaps
        self.assertEqual(
            len(unexpected), 0,
            f"Unexpected mechanism ID gaps: {sorted(unexpected)}"
        )

    def test_highest_mechanism_is_261(self):
        int_ids = [mid for mid in self.mechanisms if isinstance(mid, int)]
        self.assertEqual(max(int_ids), 261)


class TestDocSync(unittest.TestCase):
    """All Aug 23 test files must appear in README and ARCHITECTURE."""

    @classmethod
    def setUpClass(cls):
        cls.aug23_files = sorted(
            os.path.basename(f)
            for f in glob.glob(str(TESTS_DIR / "test_*aug23*.py"))
        )
        with open(README_PATH) as f:
            cls.readme = f.read()
        with open(ARCH_PATH) as f:
            cls.arch = f.read()

    def test_all_aug23_files_in_readme(self):
        missing = [f for f in self.aug23_files if f not in self.readme]
        self.assertEqual(
            len(missing), 0,
            f"Aug 23 files missing from README: {missing}"
        )

    def test_all_aug23_files_in_architecture(self):
        missing = [f for f in self.aug23_files if f not in self.arch]
        self.assertEqual(
            len(missing), 0,
            f"Aug 23 files missing from ARCHITECTURE: {missing}"
        )


class TestSentimentImport(unittest.TestCase):
    """Verify textblob is installed and sentiment analysis module imports."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

    def test_sentiment_module_importable(self):
        from mediascope.analyze.sentiment import analyze_composite  # noqa: F401


class TestPriorFixRegression(unittest.TestCase):
    """Guards against regression of fixes from earlier Type D iterations."""

    def test_no_list_items_in_publications(self):
        """Mechanism entries must be named mapping keys, not list items."""
        data = _load_yaml()
        pubs = data.get("publications", {})
        # If publications had list items, yaml.safe_load would make it a list
        self.assertIsInstance(pubs, dict)

    def test_mechanism_232_mapping_key(self):
        """Mechanism #232 was fixed from list→mapping in 3pm Aug 22 iteration."""
        data = _load_yaml()
        pubs = data.get("publications", {})
        found = any(
            pub.get("mechanism_id") == 232
            for pub in pubs.values()
            if isinstance(pub, dict)
        )
        self.assertTrue(found, "Mechanism #232 not found as publication mapping value")


if __name__ == "__main__":
    unittest.main()
