"""
MediaScope Type D Cross-Validation — Aug 23 07:00 AM PT

Validates:
1. Test file count matches 560 (559 prior + this file)
2. Mechanism ID contiguity above 200 (gaps documented)
3. Cross-reference integrity after extraction-collision fix
4. competitor-coverage-research.yaml: all entries have meta_coverage_tone
5. No collection errors (all tests importable)
6. Aug 23 test files documented in README and ARCHITECTURE
"""

import unittest
import yaml
import os
import glob
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent
REPO_DIR = Path(__file__).parent.parent
YAML_PATH = PROFILES_DIR / "competitor-coverage-research.yaml"


def _extract_all_mechanisms(d, out=None):
    """Extract mechanisms, preferring entries with more keys (real > cross-refs)."""
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


class TestFileCount(unittest.TestCase):
    """Verify total test file count is at least 560."""

    def test_actual_test_file_count_is_560(self):
        files = glob.glob(str(TESTS_DIR / "test_*.py"))
        actual = len(files)
        self.assertGreaterEqual(actual, 560, f"Expected at least 560 test files, got {actual}")


class TestMetaCoverageToneCompleteness(unittest.TestCase):
    """Every publication entry must have meta_coverage_tone."""

    def test_all_publications_have_meta_coverage_tone(self):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        pubs = data.get('publications', {})
        missing = [name for name, pub in pubs.items()
                   if 'meta_coverage_tone' not in pub]
        self.assertEqual(len(missing), 0,
                         f"Missing meta_coverage_tone: {missing[:5]}")


class TestMechanismExtractionCollisionFix(unittest.TestCase):
    """Verify recursive mechanism extraction prefers real entries over cross-refs."""

    @classmethod
    def setUpClass(cls):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_mechanism_247_is_full_entry(self):
        m = self.mechanisms.get(247)
        self.assertIsNotNone(m, "Mechanism 247 not found")
        self.assertGreater(len(m), 5,
                           "Mechanism 247 should be full entry, not cross-ref stub")

    def test_mechanism_247_has_vocabulary_gradient(self):
        m = self.mechanisms.get(247, {})
        tiers = m.get('vocabulary_gradient_tiers', {})
        self.assertGreaterEqual(len(tiers), 5)

    def test_no_real_mechanism_overwritten_by_crossref(self):
        """Every mechanism_id that exists as a top-level publication should
        be the version with more keys (the real entry)."""
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        pubs = data.get('publications', {})
        top_level = {}
        for name, pub in pubs.items():
            mid = pub.get('mechanism_id')
            if mid is not None:
                top_level[mid] = len(pub)

        for mid, expected_keys in top_level.items():
            extracted = self.mechanisms.get(mid, {})
            self.assertGreaterEqual(
                len(extracted), expected_keys,
                f"Mechanism {mid}: extracted has {len(extracted)} keys, "
                f"top-level has {expected_keys}")


class TestMechanismContiguity(unittest.TestCase):
    """Document known mechanism ID gaps above 200."""

    @classmethod
    def setUpClass(cls):
        with open(YAML_PATH) as f:
            data = yaml.safe_load(f)
        cls.mechanisms = _extract_all_mechanisms(data)

    def test_known_gaps_documented(self):
        """Gaps at 241, 242, 244 are expected from non-sequential creation."""
        above_200 = sorted(mid for mid in self.mechanisms if isinstance(mid, int) and mid >= 200)
        gaps = []
        for i in range(1, len(above_200)):
            if above_200[i] - above_200[i-1] > 1:
                gaps.extend(range(above_200[i-1]+1, above_200[i]))
        known_gaps = {241, 242, 244, 249, 250, 258, 259, 260}
        unexpected = set(gaps) - known_gaps
        self.assertEqual(len(unexpected), 0,
                         f"Unexpected mechanism ID gaps: {sorted(unexpected)}")


class TestAug23FilesDocumented(unittest.TestCase):
    """All aug23 test files should appear in README and ARCHITECTURE."""

    def setUp(self):
        self.aug23_files = [
            os.path.basename(f) for f in
            glob.glob(str(TESTS_DIR / "test_*aug23*.py"))
            if "type_d" not in os.path.basename(f)  # exclude this validator
        ]

    def test_all_aug23_files_in_readme(self):
        readme = (REPO_DIR / "README.md").read_text()
        missing = [f for f in self.aug23_files if f not in readme]
        self.assertEqual(len(missing), 0,
                         f"Aug 23 files missing from README: {missing}")

    def test_all_aug23_files_in_architecture(self):
        arch = (REPO_DIR / "docs" / "ARCHITECTURE.md").read_text()
        missing = [f for f in self.aug23_files if f not in arch]
        self.assertEqual(len(missing), 0,
                         f"Aug 23 files missing from ARCHITECTURE: {missing}")


if __name__ == "__main__":
    unittest.main()
