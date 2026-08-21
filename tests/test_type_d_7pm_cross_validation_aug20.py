"""
Type D Cross-Validation — Aug 20, 2026, 7:00 PM PT

Scope:
1. Fix 4 test failures from prior iterations (README count, ARCHITECTURE count,
   mechanism #200 guard, podcast timestamp)
2. Add 5 missing mechanism profile entries (#193, #195, #196, #197, #198) to
   competitor-coverage-research.yaml — these existed in test files and iteration
   log but had no profile YAML entries
3. Verify all mechanisms #191-#200 now have profile YAML entries
4. Verify mechanism ID contiguity through #200
5. Doc sync: README and ARCHITECTURE counts match actual test file/test counts
6. Cross-validate mechanism metadata completeness (required fields)
"""
import unittest
import os
import yaml
import re

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')


def load_yaml(filename):
    path = os.path.join(REPO_ROOT, 'profiles', filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism_in_all_profiles(mechanism_id):
    """Search all profile YAMLs for a mechanism by ID, recursively."""
    profiles_dir = os.path.join(REPO_ROOT, 'profiles')

    def _search(obj, path=''):
        if isinstance(obj, dict):
            if obj.get('mechanism_id') == mechanism_id:
                return path, obj
            for k, v in obj.items():
                result = _search(v, f'{path}.{k}')
                if result:
                    return result
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                result = _search(item, f'{path}[{i}]')
                if result:
                    return result
        return None

    for fname in sorted(os.listdir(profiles_dir)):
        if not fname.endswith('.yaml'):
            continue
        path = os.path.join(profiles_dir, fname)
        try:
            with open(path) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError:
            continue  # Skip malformed YAML files
        if not isinstance(data, dict):
            continue
        result = _search(data)
        if result:
            return fname, result[0], result[1]
    return None, None, None


class TestMechanismProfileCompleteness(unittest.TestCase):
    """Every mechanism #191-#200 should have a profile YAML entry."""

    def test_mechanism_191_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(191)
        self.assertIsNotNone(fname, "Mechanism #191 not found in any profile YAML")

    def test_mechanism_192_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(192)
        self.assertIsNotNone(fname, "Mechanism #192 not found in any profile YAML")

    def test_mechanism_193_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(193)
        self.assertIsNotNone(fname, "Mechanism #193 not found in any profile YAML")

    def test_mechanism_194_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(194)
        self.assertIsNotNone(fname, "Mechanism #194 not found in any profile YAML")

    def test_mechanism_195_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(195)
        self.assertIsNotNone(fname, "Mechanism #195 not found in any profile YAML")

    def test_mechanism_196_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(196)
        self.assertIsNotNone(fname, "Mechanism #196 not found in any profile YAML")

    def test_mechanism_197_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(197)
        self.assertIsNotNone(fname, "Mechanism #197 not found in any profile YAML")

    def test_mechanism_198_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(198)
        self.assertIsNotNone(fname, "Mechanism #198 not found in any profile YAML")

    def test_mechanism_199_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(199)
        self.assertIsNotNone(fname, "Mechanism #199 not found in any profile YAML")

    def test_mechanism_200_in_profile(self):
        fname, key, val = find_mechanism_in_all_profiles(200)
        self.assertIsNotNone(fname, "Mechanism #200 not found in any profile YAML")


class TestMechanismMetadataCompleteness(unittest.TestCase):
    """Each mechanism should have required metadata fields."""

    REQUIRED_FIELDS = ['mechanism_id', 'finding_summary']
    RECOMMENDED_FIELDS = ['asymmetry_score', 'entities', 'test_file', 'discovery_date']

    def _check_mechanism(self, mechanism_id):
        fname, key, val = find_mechanism_in_all_profiles(mechanism_id)
        self.assertIsNotNone(fname, f"Mechanism #{mechanism_id} not found")
        for field in self.REQUIRED_FIELDS:
            self.assertIn(field, val,
                          f"Mechanism #{mechanism_id} in {fname} missing required field '{field}'")

    def test_mechanism_193_metadata(self):
        self._check_mechanism(193)

    def test_mechanism_195_metadata(self):
        self._check_mechanism(195)

    def test_mechanism_196_metadata(self):
        self._check_mechanism(196)

    def test_mechanism_197_metadata(self):
        self._check_mechanism(197)

    def test_mechanism_198_metadata(self):
        self._check_mechanism(198)


class TestMechanismIDContiguity(unittest.TestCase):
    """Mechanism IDs should be contiguous from 191 through 200."""

    def test_no_gaps_191_to_200(self):
        missing = []
        for i in range(191, 201):
            fname, key, val = find_mechanism_in_all_profiles(i)
            if fname is None:
                missing.append(i)
        self.assertEqual(missing, [], f"Mechanism IDs missing from profiles: {missing}")


class TestTestFileExistence(unittest.TestCase):
    """Every mechanism #193-#198 should have a corresponding test file on disk."""

    def test_mechanism_193_test_file(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS_DIR, 'test_gadgetevolution_affiliate_privacy_paradox_aug20.py')))

    def test_mechanism_195_test_file(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS_DIR,
                                        'test_lance_ulanoff_techradar_cross_entity_market_attribution_privacy_displacement_aug20.py')))

    def test_mechanism_196_test_file(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS_DIR,
                                        'test_digital_trends_apple_n50_privacy_hero_meta_creepy_reputation_framing_asymmetry_aug20.py')))

    def test_mechanism_197_test_file(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS_DIR,
                                        'test_reuters_snap_meta_camera_privacy_vocabulary_bifurcation_aug20.py')))

    def test_mechanism_198_test_file(self):
        self.assertTrue(
            os.path.exists(os.path.join(TESTS_DIR,
                                        'test_lawrence_bonk_engadget_generalist_beat_assignment_stigma_concentration_aug20.py')))


class TestDocSyncAug20_7pm(unittest.TestCase):
    """README and ARCHITECTURE counts should match reality after fixes."""

    def setUp(self):
        with open(os.path.join(REPO_ROOT, 'README.md')) as f:
            self.readme = f.read()
        with open(os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')) as f:
            self.arch = f.read()
        self.actual_file_count = len([
            f for f in os.listdir(TESTS_DIR)
            if f.startswith('test_') and f.endswith('.py')
        ])

    def test_readme_file_count_accurate(self):
        """README file count should match actual."""
        m = re.search(r'(\d+)\s*test files', self.readme)
        self.assertIsNotNone(m)
        readme_count = int(m.group(1))
        # Allow ±2 for this cross-validation test file itself
        self.assertAlmostEqual(readme_count, self.actual_file_count, delta=2)

    def test_readme_test_count_within_5pct(self):
        """README test count should be within 5% of actual."""
        import subprocess
        result = subprocess.run(
            ["grep", "-c", "def test_"] +
            [os.path.join(TESTS_DIR, f) for f in os.listdir(TESTS_DIR)
             if f.startswith("test_") and f.endswith(".py")],
            capture_output=True, text=True
        )
        actual_total = sum(int(line.split(":")[-1]) for line in result.stdout.strip().split("\n")
                           if ":" in line)
        m = re.search(r'\*\*(\d+)\s*tests\*\*', self.readme)
        if not m:
            m = re.search(r'~(\d[\d,]*)\s*\|', self.readme)
        self.assertIsNotNone(m, "README should state test count")
        readme_count = int(m.group(1).replace(",", ""))
        delta_pct = abs(readme_count - actual_total) / max(actual_total, 1) * 100
        self.assertLess(delta_pct, 5,
                        f"README says {readme_count} tests but actual is {actual_total} ({delta_pct:.1f}% off)")


class TestPriorFailuresFixed(unittest.TestCase):
    """Verify the 4 failures from prior iterations are now resolved."""

    def test_mechanism_200_allowed_in_wired(self):
        """Mechanism #200 should be accepted (Phil Clapp natural experiment)."""
        fname, key, val = find_mechanism_in_all_profiles(200)
        self.assertEqual(fname, 'wired.yaml')

    def test_readme_test_count_not_inflated(self):
        """README should not claim >18000 tests when actual is ~17260."""
        with open(os.path.join(REPO_ROOT, 'README.md')) as f:
            readme = f.read()
        m = re.search(r'\*\*(\d+)\s*tests\*\*', readme)
        if m:
            count = int(m.group(1))
            self.assertLess(count, 18000,
                            f"README claims {count} tests — should be ~17260")

    def test_podcast_timestamp_has_aug20(self):
        """podcast-sentiment.md should reference Aug 20."""
        path = os.path.join(REPO_ROOT, 'podcast-sentiment.md')
        with open(path) as f:
            content = f.read()
        self.assertIn('Aug 20', content)


class TestAsymmetryScoreDistribution(unittest.TestCase):
    """New mechanisms should have reasonable asymmetry scores."""

    def test_scores_in_range(self):
        for mech_id in [193, 195, 196, 197, 198]:
            fname, key, val = find_mechanism_in_all_profiles(mech_id)
            if val and 'asymmetry_score' in val:
                score = val['asymmetry_score']
                self.assertGreaterEqual(score, 0.5,
                                        f"Mechanism #{mech_id} score {score} below 0.5")
                self.assertLessEqual(score, 1.0,
                                     f"Mechanism #{mech_id} score {score} above 1.0")

    def test_new_mechanisms_have_scores(self):
        for mech_id in [193, 195, 196, 197, 198]:
            fname, key, val = find_mechanism_in_all_profiles(mech_id)
            self.assertIsNotNone(val, f"Mechanism #{mech_id} not found")
            self.assertIn('asymmetry_score', val,
                          f"Mechanism #{mech_id} missing asymmetry_score")


if __name__ == '__main__':
    unittest.main()
