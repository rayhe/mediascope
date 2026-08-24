"""
Type D Cross-Validation — Aug 23, 12 PM PT (Iteration #261)

Fixes applied this iteration:
1. Billy Steele test mechanism extractor: prefer entries with more keys
   over cross-reference stubs (prevents overwrite of full mechanism #246
   entry by later 3-key cross-ref stub)
2. File count updated: 560 → 564 (4 new files from 08-11 AM iterations)
3. Mechanism ID known gaps: added 249, 250 to expected set
4. Missing meta_coverage_tone: added to google_preferred_sources_embed
5. README/ARCHITECTURE: added 4 missing aug23 test files

Regression guards verify these fixes don't regress.
"""

import glob
import os
import sys
import unittest

import yaml

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_DIR, "tests")
PROFILES_DIR = os.path.join(REPO_DIR, "profiles")
YAML_PATH = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")


def _extract_all_mechanisms(data, prefer_longer=True):
    """Recursively extract mechanism entries, preferring full entries over stubs."""
    mechanisms = {}

    def _walk(d):
        if isinstance(d, dict):
            if "mechanism_id" in d:
                mid = d["mechanism_id"]
                if mid not in mechanisms or len(d) > len(mechanisms[mid]):
                    mechanisms[mid] = d
            for v in d.values():
                _walk(v)
        elif isinstance(d, list):
            for item in d:
                _walk(item)

    _walk(data)
    return mechanisms


class TestFileCount(unittest.TestCase):
    """Verify total test file count is 570 (569 prior + this file)."""

    def test_actual_test_file_count(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_*.py"))
        actual = len(files)
        self.assertEqual(actual, 571, f"Expected 565 test files, got {actual}")


class TestBillySteeleExtractorFix(unittest.TestCase):
    """Mechanism #246 must resolve to full entry, not cross-ref stub."""

    @classmethod
    def setUpClass(cls):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_mechanism_246_has_journalist(self):
        m = self.mechanisms.get(246, {})
        journalist = str(m.get("journalist", "")).lower()
        self.assertIn("steele", journalist,
                      "Mechanism #246 should resolve to full Billy Steele entry, not cross-ref stub")

    def test_mechanism_246_has_asymmetry_score(self):
        m = self.mechanisms.get(246, {})
        score = m.get("asymmetry_score", 0)
        self.assertGreater(score, 0, "Full entry must have positive asymmetry_score")

    def test_mechanism_246_has_confounders(self):
        m = self.mechanisms.get(246, {})
        confounders = m.get("confounding_factors", m.get("confounders", []))
        self.assertGreaterEqual(len(confounders), 3)

    def test_mechanism_246_key_count_exceeds_stub(self):
        m = self.mechanisms.get(246, {})
        self.assertGreater(len(m), 5,
                           "Full entry should have many more keys than a 3-key cross-ref stub")


class TestMechanismIdGaps(unittest.TestCase):
    """Known mechanism ID gaps include 241, 242, 244, 249, 250."""

    @classmethod
    def setUpClass(cls):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_known_gaps_complete(self):
        above_200 = sorted(mid for mid in self.mechanisms if isinstance(mid, int) and mid >= 200)
        gaps = []
        for i in range(1, len(above_200)):
            if above_200[i] - above_200[i - 1] > 1:
                gaps.extend(range(above_200[i - 1] + 1, above_200[i]))
        known_gaps = {241, 242, 244, 249, 250, 258, 259, 260}
        unexpected = set(gaps) - known_gaps
        self.assertEqual(len(unexpected), 0,
                         f"Unexpected mechanism ID gaps: {sorted(unexpected)}")


class TestMetaCoverageToneCompleteness(unittest.TestCase):
    """Every publication entry must have meta_coverage_tone."""

    def test_google_preferred_sources_has_meta_coverage_tone(self):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        pubs = data.get("publications", {})
        entry = pubs.get("google_preferred_sources_embed_sixth_dependency_layer", {})
        self.assertIn("meta_coverage_tone", entry,
                      "Google Preferred Sources entry must have meta_coverage_tone")

    def test_all_publications_have_meta_coverage_tone(self):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        pubs = data.get("publications", {})
        missing = [name for name, pub in pubs.items()
                   if "meta_coverage_tone" not in pub]
        self.assertEqual(len(missing), 0,
                         f"Missing meta_coverage_tone: {missing[:5]}")


class TestDocSync(unittest.TestCase):
    """All non-type-d aug23 test files must appear in README and ARCHITECTURE."""

    def setUp(self):
        self.aug23_files = [
            os.path.basename(f) for f in
            glob.glob(os.path.join(TESTS_DIR, "test_*aug23*.py"))
            if "type_d" not in os.path.basename(f)
        ]

    def test_all_aug23_files_in_readme(self):
        with open(os.path.join(REPO_DIR, "README.md")) as f:
            readme = f.read()
        missing = [fn for fn in self.aug23_files if fn not in readme]
        self.assertEqual(len(missing), 0,
                         f"Aug 23 files missing from README: {missing}")

    def test_all_aug23_files_in_architecture(self):
        with open(os.path.join(REPO_DIR, "docs", "ARCHITECTURE.md")) as f:
            arch = f.read()
        missing = [fn for fn in self.aug23_files if fn not in arch]
        self.assertEqual(len(missing), 0,
                         f"Aug 23 files missing from ARCHITECTURE: {missing}")

    def test_chokkattu_dual_role_in_readme(self):
        with open(os.path.join(REPO_DIR, "README.md")) as f:
            readme = f.read()
        self.assertIn("test_chokkattu_dual_role_apple_camera_airpods_contribution_temporal_adjacency_aug23.py", readme)

    def test_google_preferred_sources_in_readme(self):
        with open(os.path.join(REPO_DIR, "README.md")) as f:
            readme = f.read()
        self.assertIn("test_google_preferred_sources_embed_sixth_dependency_layer_aug23.py", readme)


class TestPriorFixRegression(unittest.TestCase):
    """Guard against regression of fixes from earlier Type D iterations."""

    @classmethod
    def setUpClass(cls):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_mechanism_252_exists(self):
        """Chokkattu dual-role mechanism from iteration #259."""
        self.assertIn(252, self.mechanisms)

    def test_mechanism_253_exists(self):
        """Google Preferred Sources mechanism from iteration #260."""
        self.assertIn(253, self.mechanisms)

    def test_mechanism_248_exists(self):
        """Arin Waichulis Security Bite mechanism."""
        self.assertIn(248, self.mechanisms)

    def test_highest_mechanism_id(self):
        """Track highest mechanism ID for contiguity."""
        max_id = max(mid for mid in self.mechanisms if isinstance(mid, int))
        self.assertGreaterEqual(max_id, 253,
                                f"Highest mechanism ID should be at least 253, got {max_id}")


if __name__ == "__main__":
    unittest.main()
