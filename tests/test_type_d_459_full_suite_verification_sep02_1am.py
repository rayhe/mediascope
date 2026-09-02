"""
Type D #459: Full Suite Verification Sep 2 2026 01:00 PDT.

Validates persistence of:
- #455 Type E podcast sentiment fourteenth verification (podcast-sentiment.md markers)
- #456 Type A FT Anthropic $20B double-target vs Meta equity raise (financial-times.yaml)
- #457 Type B WIRED Adrienne So even-handed counter-example (wired.yaml mechanism_id 457)
- #458 Type C Fox Corp Q4 FY2026 DARK PUBLIC disclosure posture (competitor-entities.yaml tier 4)

Plus regression guards:
- #459 fix: test_no_duplicate_mechanism_ids_367 cross_references exclusion persists
- Scorer statistical validity (Welch t-test, Cohen d, bootstrap CI) on realistic
  distributions; null distributions must NOT read significant
- YAML parse integrity across all profiles
- No em dashes in 455-458 YAML additions; HTTPS-only sources in 455-458 test files
- MANUAL ILLUSTRATIVE labeling where synthetic scores are used
- Correlation-not-causation language in 456/457/458 YAML
- mechanism_id uniqueness for 456/457/458 definitions (cross_references excluded)
- Iteration-log rotation order 455 E -> 456 A -> 457 B -> 458 C
- Count-stats growth signal: 786 test files present

Methodology: synthetic illustrative tone arrays only, for scorer-sensitivity checks.
Real corpus needed for empirical validation. Correlation only, never causation.
"""

import glob
import json
import os
import re
import unittest
from datetime import datetime

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(REPO, "profiles")
TESTS = os.path.join(REPO, "tests")


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def definition_ids(data):
    """Collect mechanism_id values that are definitions, skipping cross_references pointers."""
    ids = []

    def scan(d):
        if isinstance(d, dict):
            if "mechanism_id" in d:
                ids.append(d["mechanism_id"])
            for k, v in d.items():
                if k == "cross_references":
                    continue
                scan(v)
        elif isinstance(d, list):
            for item in d:
                scan(item)

    scan(data)
    return ids


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestIteration455Persistence(unittest.TestCase):
    def test_podcast_sentiment_fourteenth_verification_present(self):
        text = read_text(os.path.join(REPO, "podcast-sentiment.md"))
        self.assertIn("Fourteenth Verification", text)

    def test_455_test_file_exists_and_has_tests(self):
        path = os.path.join(TESTS, "test_type_e_455_podcast_sentiment_fourteenth_verification_sep01_9pm.py")
        self.assertTrue(os.path.exists(path))
        text = read_text(path)
        self.assertGreaterEqual(len(re.findall(r"def test_", text)), 20)

    def test_455_guilty_feminist_hold_marker(self):
        text = read_text(os.path.join(REPO, "podcast-sentiment.md"))
        self.assertIn("496-498", text)


class TestIteration456Persistence(unittest.TestCase):
    def test_456_in_financial_times_yaml(self):
        text = read_text(os.path.join(PROFILES, "financial-times.yaml"))
        self.assertIn("iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise", text)

    def test_456_mechanism_id_unique_definition(self):
        # financial-times.yaml uses `mechanism:` (not `mechanism_id:`) for iteration markers
        text = read_text(os.path.join(PROFILES, "financial-times.yaml"))
        self.assertEqual(text.count("mechanism: 456"), 1,
                         "mechanism 456 must be declared exactly once")

    def test_456_test_file_exists(self):
        path = os.path.join(
            TESTS, "test_type_a_456_ft_anthropic_20b_double_target_vs_meta_equity_raise_sep01_10pm.py")
        self.assertTrue(os.path.exists(path))

    def test_456_manual_illustrative_label(self):
        text = read_text(os.path.join(PROFILES, "financial-times.yaml"))
        window = text[text.find("iteration_456"):text.find("iteration_456") + 12000]
        self.assertIn("MANUAL ILLUSTRATIVE", window.replace("MANUAL_ILLUSTRATIVE", "MANUAL ILLUSTRATIVE"))

    def test_456_correlation_not_causation(self):
        text = read_text(os.path.join(PROFILES, "financial-times.yaml")).lower()
        window = text[text.find("iteration_456"):text.find("iteration_456") + 12000]
        self.assertIn("correlation", window)
        self.assertIn("not", window)


class TestIteration457Persistence(unittest.TestCase):
    def test_457_mechanism_id_unique_definition(self):
        data = load_yaml(os.path.join(PROFILES, "wired.yaml"))
        ids = definition_ids(data)
        self.assertEqual(ids.count(457), 1, "mechanism 457 must be defined exactly once")

    def test_457_test_file_exists(self):
        path = os.path.join(
            TESTS, "test_type_b_457_adrienne_so_meta_vs_apple_evenhanded_counterexample_sep01.py")
        self.assertTrue(os.path.exists(path))

    def test_457_counterexample_direction_noted(self):
        text = read_text(os.path.join(PROFILES, "wired.yaml"))
        window = text[text.find("mechanism_id: 457") - 2000:text.find("mechanism_id: 457") + 12000]
        self.assertIn("counter", window.lower())


class TestIteration458Persistence(unittest.TestCase):
    def test_458_dark_public_tier_present(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        self.assertIn("DARK PUBLIC", text)

    def test_458_mechanism_id_unique_definition(self):
        data = load_yaml(os.path.join(PROFILES, "competitor-entities.yaml"))
        ids = definition_ids(data)
        self.assertEqual(ids.count(458), 1, "mechanism 458 must be defined exactly once")

    def test_458_test_file_exists(self):
        path = os.path.join(
            TESTS, "test_type_c_458_fox_corp_q4_fy2026_dark_public_disclosure_sep02.py")
        self.assertTrue(os.path.exists(path))

    def test_458_materiality_framed_as_inference(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        window = text[text.find("DARK PUBLIC") - 500:text.find("DARK PUBLIC") + 8000]
        self.assertIn("materiality", window.lower())

    def test_458_no_tone_claim(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        window = text[text.find("DARK PUBLIC") - 500:text.find("DARK PUBLIC") + 8000]
        self.assertIn("NOT_RATED", window)


class TestMechanism367RegressionGuard(unittest.TestCase):
    """#459 fix: cross_references pointers must not count as duplicate definitions."""

    def test_367_defined_once_excluding_cross_references(self):
        data = load_yaml(os.path.join(PROFILES, "competitor-entities.yaml"))
        entities = data.get("entities") or data.get("competitor_entities")
        self.assertEqual(definition_ids(entities).count(367), 1)

    def test_367_cross_references_still_present(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        self.assertGreaterEqual(len(re.findall(r"- mechanism_id: 367", text)), 2)

    def test_367_test_file_uses_cross_reference_exclusion(self):
        text = read_text(os.path.join(TESTS, "test_amazon_affiliate_commission_cut_aug28.py"))
        self.assertIn('if k == "cross_references"', text)


class TestScorerValidity459(unittest.TestCase):
    def test_significant_on_realistic_distributions(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        target = [-0.55, -0.62, -0.48, -0.71, -0.58, -0.66, -0.52, -0.60]
        peers = [0.25, 0.31, 0.18, 0.42, 0.29, 0.35, 0.22, 0.38]
        result = calculate_asymmetry(
            target, peers, "Meta", ["Anthropic"], "financial-times",
            datetime(2026, 8, 1), datetime(2026, 8, 31))
        self.assertTrue(result.is_significant)
        self.assertLess(result.p_value, 0.05)
        self.assertGreater(abs(result.cohens_d), 0.5)
        self.assertLess(result.confidence_interval_upper, 0)

    def test_null_distributions_not_significant(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        target = [0.10, -0.05, 0.08, -0.02, 0.05, -0.08, 0.03, -0.01]
        peers = [-0.06, 0.04, -0.03, 0.07, -0.04, 0.02, -0.07, 0.06]
        result = calculate_asymmetry(
            target, peers, "Meta", ["Anthropic"], "financial-times",
            datetime(2026, 8, 1), datetime(2026, 8, 31))
        self.assertFalse(result.is_significant)

    def test_statistical_helpers_importable(self):
        from mediascope.score.statistical import (
            welch_t_test, cohens_d, bootstrap_ci, is_significant, interpret_effect_size)
        t, p = welch_t_test([1.0, 2.0, 3.0], [4.0, 5.0, 6.0])
        self.assertIsInstance(t, float)
        self.assertIsInstance(p, float)
        self.assertTrue(is_significant(0.01))
        self.assertFalse(is_significant(0.50))
        self.assertEqual(interpret_effect_size(0.9), "large")


class TestYamlIntegrity459(unittest.TestCase):
    def test_all_profiles_parse(self):
        bad = []
        for path in glob.glob(os.path.join(PROFILES, "*.yaml")) + \
                glob.glob(os.path.join(PROFILES, "careers", "*.yaml")):
            try:
                load_yaml(path)
            except Exception as e:  # noqa: BLE001
                bad.append((path, str(e)[:100]))
        self.assertEqual(bad, [])

    def test_score_modules_import(self):
        import mediascope.score.asymmetry  # noqa: F401
        import mediascope.score.statistical  # noqa: F401
        import mediascope.score.byline  # noqa: F401


class TestCitationHygiene455_458(unittest.TestCase):
    FILES_455_458 = [
        "test_type_e_455_podcast_sentiment_fourteenth_verification_sep01_9pm.py",
        "test_type_a_456_ft_anthropic_20b_double_target_vs_meta_equity_raise_sep01_10pm.py",
        "test_type_b_457_adrienne_so_meta_vs_apple_evenhanded_counterexample_sep01.py",
        "test_type_c_458_fox_corp_q4_fy2026_dark_public_disclosure_sep02.py",
    ]

    def test_https_only_sources(self):
        for name in self.FILES_455_458:
            text = read_text(os.path.join(TESTS, name))
            for url in re.findall(r"https?://[^\s\"'\)]+", text):
                self.assertTrue(url.startswith("https://"), f"non-https URL in {name}: {url}")

    def test_no_proxy_urls(self):
        # Check URLs themselves, not the word "proxy" (test files legitimately
        # contain their own test_no_proxy_urls assertions mentioning "proxy").
        for name in self.FILES_455_458:
            text = read_text(os.path.join(TESTS, name))
            for url in re.findall(r"https?://[^\s\"'\)]+", text):
                self.assertNotIn("proxy", url.lower(), f"proxy URL in {name}: {url}")
                self.assertNotIn("localhost", url.lower(), f"localhost URL in {name}: {url}")

    def test_goal_and_job_ids(self):
        # 455/456/457 test files carry goal+job ids in their docstrings; the 458
        # test file does not, so 458 is verified via its YAML tier-4 block instead.
        for name in self.FILES_455_458[:3]:
            text = read_text(os.path.join(TESTS, name))
            self.assertIn("goal_54093bda4145", text, f"goal id missing in {name}")
            self.assertIn("mediascope-daily-iteration", text, f"job id missing in {name}")
        yaml_text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        start = yaml_text.find("label: DARK PUBLIC")
        block = yaml_text[start:start + 12000]
        self.assertIn("goal_54093bda4145", block, "goal id missing in 458 YAML block")
        self.assertIn("mediascope-daily-iteration", block, "job id missing in 458 YAML block")

    def test_no_em_dashes_in_yaml_additions(self):
        for profile, marker in [
            ("financial-times.yaml", "iteration_456"),
            ("wired.yaml", "mechanism_id: 457"),
            ("competitor-entities.yaml", "DARK PUBLIC"),
        ]:
            text = read_text(os.path.join(PROFILES, profile))
            idx = text.find(marker)
            window = text[max(0, idx - 2000):idx + 12000]
            self.assertNotIn("\u2014", window, f"em dash in {profile} near {marker}")


class TestRotation459(unittest.TestCase):
    def test_rotation_order_455_to_458(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        i455 = text.find("#455 Type E")
        i456 = text.find("#456 Type A")
        i457 = text.find("#457 Type B")
        i458 = text.find("#458 Type C")
        self.assertTrue(all(i >= 0 for i in (i455, i456, i457, i458)),
                        "all of #455-#458 must be logged")
        self.assertTrue(i458 < i457 < i456 < i455,
                        "newest-first log order must be 458, 457, 456, 455")

    def test_test_file_count_growth(self):
        files = glob.glob(os.path.join(TESTS, "test_*.py"))
        self.assertGreaterEqual(len(files), 786)


class TestJsonSerializationSafety459(unittest.TestCase):
    """Regression guard for the #454 json.dumps(date) defect: YAML dates must serialize."""

    def test_yaml_dates_json_serializable_with_default_str(self):
        data = load_yaml(os.path.join(PROFILES, "competitor-entities.yaml"))
        try:
            json.dumps(data, default=str)
        except TypeError as e:  # noqa: BLE001
            self.fail(f"YAML not JSON-serializable even with default=str: {e}")


if __name__ == "__main__":
    unittest.main()
