"""
Type D #464: Full Suite Verification Sep 2 2026 06:00 PDT.

Validates persistence of:
- #460 Type E podcast sentiment fifteenth verification (podcast-sentiment.md markers:
  Fifteenth Verification, GF 498 hold no 499, EHE 23-day hold, 9,000 email drive via SWNS)
- #461 Type A The Verge x Microsoft Copilot retrenchment (the-verge.yaml iteration_461,
  mechanism 461 declared exactly once)
- #462 Type B The Verge Jess Weatherbed same-journalist cross-entity (the-verge.yaml
  mechanism_id 462 defined exactly once, cross_references excluded)
- #463 Type C USA TODAY Co. Q2 2026 Tier 2 BUNDLED (competitor-entities.yaml TDAY ticker,
  q2_2026_data block, ai_revenue_isolatable false)

Plus regression guards:
- Scorer statistical validity (Welch t-test, Cohen d, bootstrap CI) on realistic
  distributions; null distributions must NOT read significant
- YAML parse integrity across all profiles
- HTTPS-only sources, no literal em dashes, correlation-not-causation language,
  test-file self-reference in the 460-463 test files
- mechanism 464 uniqueness (Type D defines no data mechanism; the number must not
  collide with any existing mechanism_id or mechanism declaration)
- Iteration-log newest-first ordering 464, 463, 462, 461, 460, 459 (guards the #463
  log-order repair performed by this iteration)

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

GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"

FILES_460_463 = [
    "test_type_e_460_podcast_sentiment_fifteenth_verification_sep02_2am.py",
    "test_type_a_461_verge_microsoft_copilot_retrenchment_dedicated_beat_sep02_3am.py",
    "test_type_b_462_jess_weatherbed_tiktok_vs_meta_apple_cross_entity_sep02_4am.py",
    "test_type_c_463_usa_today_co_q2_2026_bundled_lumpiness_sep02_5am.py",
]
THIS_FILE = "test_type_d_464_full_suite_verification_sep02_6am.py"


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


def header_pos(text, num):
    """Position of the newest-first log header line for iteration num (line-anchored,
    so body-text mentions of '#NNN Type X' do not match)."""
    m = re.search(rf"^#{num} Type [A-E]:", text, re.M)
    return m.start() if m else -1


def header_count(text, num):
    return len(re.findall(rf"^#{num} Type [A-E]:", text, re.M))


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestIteration464Identity(unittest.TestCase):
    def test_464_header_present(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        self.assertGreaterEqual(header_pos(text, 464), 0)

    def test_464_date_present(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        idx = header_pos(text, 464)
        window = text[idx:idx + 3000]
        self.assertIn("2026-09-02 06:00 PDT", window)

    def test_464_goal_and_job_ids(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        idx = header_pos(text, 464)
        window = text[idx:idx + 3000]
        self.assertIn(GOAL_ID, window)
        self.assertIn(JOB_ID, window)

    def test_464_rotation_c_to_d(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        idx = header_pos(text, 464)
        window = text[idx:idx + 3000]
        self.assertIn("463", window)
        self.assertTrue("C->D" in window or "C -> D" in window)

    def test_464_test_file_self_reference(self):
        text = read_text(os.path.join(TESTS, THIS_FILE))
        self.assertIn("464", os.path.basename(__file__))
        self.assertIn("def test_", text)


class TestIteration460Persistence(unittest.TestCase):
    def test_fifteenth_verification_in_podcast_sentiment(self):
        text = read_text(os.path.join(REPO, "podcast-sentiment.md"))
        self.assertIn("Fifteenth", text)

    def test_460_gf_498_hold_markers(self):
        text = read_text(os.path.join(REPO, "podcast-sentiment.md"))
        self.assertIn("498", text)
        self.assertIn("499", text)

    def test_460_ehe_hold_and_email_drive_markers(self):
        text = read_text(os.path.join(REPO, "podcast-sentiment.md"))
        self.assertIn("23-day", text)
        self.assertIn("9,000", text)

    def test_460_test_file_exists_and_has_tests(self):
        path = os.path.join(TESTS, FILES_460_463[0])
        self.assertTrue(os.path.exists(path))
        text = read_text(path)
        self.assertGreaterEqual(len(re.findall(r"def test_", text)), 25)

    def test_460_goal_and_job_ids_in_test_file(self):
        text = read_text(os.path.join(TESTS, FILES_460_463[0]))
        self.assertIn(GOAL_ID, text)
        self.assertIn(JOB_ID, text)


class TestIteration461Persistence(unittest.TestCase):
    def test_461_marker_in_the_verge_yaml(self):
        text = read_text(os.path.join(PROFILES, "the-verge.yaml"))
        self.assertIn("iteration_461_sep02_2026_verge_microsoft_copilot_retrenchment", text)

    def test_461_mechanism_declared_once(self):
        text = read_text(os.path.join(PROFILES, "the-verge.yaml"))
        self.assertEqual(text.count("mechanism: 461"), 1,
                         "mechanism 461 must be declared exactly once")

    def test_461_goal_and_job_ids_in_yaml_block(self):
        text = read_text(os.path.join(PROFILES, "the-verge.yaml"))
        idx = text.find("iteration_461_sep02_2026")
        window = text[idx:idx + 6000]
        self.assertIn(GOAL_ID, window)
        self.assertIn(JOB_ID, window)

    def test_461_test_file_exists(self):
        path = os.path.join(TESTS, FILES_460_463[1])
        self.assertTrue(os.path.exists(path))
        self.assertGreaterEqual(
            len(re.findall(r"def test_", read_text(path))), 10)


class TestIteration462Persistence(unittest.TestCase):
    def test_462_mechanism_id_unique_definition(self):
        data = load_yaml(os.path.join(PROFILES, "the-verge.yaml"))
        ids = definition_ids(data)
        self.assertEqual(ids.count(462), 1,
                         "mechanism 462 must be defined exactly once")

    def test_462_weatherbed_block_present(self):
        text = read_text(os.path.join(PROFILES, "the-verge.yaml"))
        self.assertIn("jess_weatherbed_tiktok_vs_meta_apple_same_journalist_cross_entity_462", text)

    def test_462_goal_and_job_ids_in_yaml_block(self):
        text = read_text(os.path.join(PROFILES, "the-verge.yaml"))
        idx = text.find("jess_weatherbed_tiktok_vs_meta_apple_same_journalist_cross_entity_462")
        window = text[idx:idx + 6000]
        self.assertIn(GOAL_ID, window)
        self.assertIn(JOB_ID, window)

    def test_462_test_file_exists(self):
        path = os.path.join(TESTS, FILES_460_463[2])
        self.assertTrue(os.path.exists(path))
        self.assertGreaterEqual(
            len(re.findall(r"def test_", read_text(path))), 10)


class TestIteration463Persistence(unittest.TestCase):
    def test_463_tday_ticker_in_yaml(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        self.assertIn("NYSE: TDAY", text)

    def test_463_q2_2026_data_block(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        idx = text.find("name: USA Today Co. (Gannett)")
        window = text[idx:idx + 6000]
        self.assertIn("q2_2026_data", window)
        self.assertIn("536.3", window)
        self.assertIn("partners_named: 0", window)

    def test_463_ai_revenue_not_isolatable(self):
        text = read_text(os.path.join(PROFILES, "competitor-entities.yaml"))
        idx = text.find("name: USA Today Co. (Gannett)")
        window = text[idx:idx + 6000]
        self.assertIn("ai_revenue_isolatable: false", window)

    def test_463_goal_and_job_ids_in_log_entry(self):
        # #463 carries goal/job ids in its iteration-log entry (its test file and
        # YAML block do not repeat them, same pattern as #458 in the #459 run).
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        idx = header_pos(text, 463)
        window = text[idx:idx + 3000]
        self.assertIn(GOAL_ID, window)
        self.assertIn(JOB_ID, window)

    def test_463_test_file_exists(self):
        path = os.path.join(TESTS, FILES_460_463[3])
        self.assertTrue(os.path.exists(path))
        self.assertGreaterEqual(
            len(re.findall(r"def test_", read_text(path))), 15)


class TestScorerValidity464(unittest.TestCase):
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


class TestYamlIntegrity464(unittest.TestCase):
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

    def test_yaml_dates_json_serializable(self):
        data = load_yaml(os.path.join(PROFILES, "competitor-entities.yaml"))
        try:
            json.dumps(data, default=str)
        except TypeError as e:  # noqa: BLE001
            self.fail(f"YAML not JSON-serializable even with default=str: {e}")


class TestCitationHygiene460_463(unittest.TestCase):
    def test_https_only_sources(self):
        for name in FILES_460_463:
            text = read_text(os.path.join(TESTS, name))
            for url in re.findall(r"https?://[^\s\"'\)]+", text):
                self.assertTrue(url.startswith("https://"),
                                f"non-https URL in {name}: {url}")

    def test_no_proxy_or_localhost_urls(self):
        for name in FILES_460_463:
            text = read_text(os.path.join(TESTS, name))
            for url in re.findall(r"https?://[^\s\"'\)]+", text):
                self.assertNotIn("proxy", url.lower(), f"proxy URL in {name}: {url}")
                self.assertNotIn("localhost", url.lower(), f"localhost URL in {name}: {url}")

    def test_no_literal_em_dashes(self):
        # The \u2014 escape inside no-em-dash assertions is fine; a literal
        # U+2014 character is not.
        for name in FILES_460_463:
            text = read_text(os.path.join(TESTS, name))
            self.assertNotIn("—", text, f"literal em dash in {name}")

    def test_correlation_language_present(self):
        for name in FILES_460_463:
            text = read_text(os.path.join(TESTS, name)).lower()
            self.assertIn("correlation", text, f"correlation language missing in {name}")

    def test_no_causal_claim_language(self):
        for name in FILES_460_463:
            text = read_text(os.path.join(TESTS, name)).lower()
            self.assertNotIn("proves that", text, f"causal claim in {name}")
            self.assertNotIn("caused by", text, f"causal claim in {name}")


class TestMechanismUniqueness464(unittest.TestCase):
    def test_464_not_a_data_mechanism(self):
        # Type D defines no data mechanism; 464 must not collide with any
        # existing mechanism_id or mechanism declaration in profiles.
        for path in glob.glob(os.path.join(PROFILES, "*.yaml")):
            data = load_yaml(path)
            self.assertNotIn(464, definition_ids(data),
                             f"464 collides with a mechanism_id in {path}")
            text = read_text(path)
            self.assertNotIn("mechanism: 464", text,
                             f"464 collides with a mechanism declaration in {path}")

    def test_464_log_header_unique(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        self.assertEqual(header_count(text, 464), 1)


class TestLogOrder464(unittest.TestCase):
    def test_newest_first_464_to_459(self):
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        positions = [header_pos(text, n) for n in (464, 463, 462, 461, 460, 459)]
        self.assertTrue(all(p >= 0 for p in positions),
                        "all of #459-#464 must be logged")
        self.assertEqual(positions, sorted(positions),
                         "newest-first log order must be 464, 463, 462, 461, 460, 459")

    def test_463_repair_before_462(self):
        # Guards the #464 log-order repair: the #463 entry must sit between
        # #464 and #462, not appended at the file bottom.
        text = read_text(os.path.join(REPO, "iteration-log.md"))
        i464 = header_pos(text, 464)
        i463 = header_pos(text, 463)
        i462 = header_pos(text, 462)
        self.assertTrue(i464 < i463 < i462)


if __name__ == "__main__":
    unittest.main()
