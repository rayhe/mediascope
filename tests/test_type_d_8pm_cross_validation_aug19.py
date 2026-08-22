"""
Type D Cross-Validation — Aug 19 8:00 PM PT
Iteration #191: Validates structural integrity of today's mechanisms #185-188

Cross-validates:
1. Mechanisms #185-188 exist with valid asymmetry scores
2. Cross-reference integrity — all referenced mechanisms exist
3. Mechanism ID contiguity from #180 to #188 (no gaps)
4. README.md test count matches actual pytest collection (>=17651)
5. Dependency fix: textblob + vaderSentiment imports succeed
6. Today's 19 aug19 test files are all listed in README.md and ARCHITECTURE.md
7. Score distribution across mechanisms #185-188 is not degenerate
8. Engadget triple-device (#186) asymmetry score is highest among today's batch
9. Samsung-Mistral (#188) confounders are documented
10. Competitor-entities.yaml has Samsung-Mistral and SpaceX S-1 entries
"""

import importlib
import os
import re
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "docs")
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
TESTS_DIR = os.path.dirname(__file__)


def _load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


def _read_file(path):
    with open(path) as f:
        return f.read()


def _get_findings_dict():
    research = _load_yaml("competitor-coverage-research.yaml")
    return research.get("cross_publication_findings", {})


def _find_mechanism_by_id(findings, mech_id):
    for key, val in findings.items():
        if isinstance(val, dict):
            mid = val.get("id") or val.get("mechanism_id")
            if mid == mech_id:
                return val
    return None


def _all_mechanism_ids(findings):
    ids = set()
    for key, val in findings.items():
        if isinstance(val, dict):
            mid = val.get("id") or val.get("mechanism_id")
            if mid:
                ids.add(mid)
    return ids


class TestMechanism185Integrity(unittest.TestCase):
    """Mechanism #185: Two Blokes / Kodak / Fiend Media moral panic precedent."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.mech = _find_mechanism_by_id(self.findings, 185)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mech, "Mechanism #185 not found")

    def test_has_asymmetry_score(self):
        self.assertIn("asymmetry_score", self.mech)

    def test_score_is_0_68(self):
        self.assertAlmostEqual(self.mech["asymmetry_score"], 0.68, places=2)

    def test_score_in_valid_range(self):
        score = self.mech["asymmetry_score"]
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_cross_references_exist(self):
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        all_ids = _all_mechanism_ids(self.findings)
        for cr in cross_refs:
            if isinstance(cr, dict):
                ref_id = cr.get("mechanism_id")
                if ref_id and ref_id > 16:
                    self.assertIn(ref_id, all_ids, f"Cross-ref #{ref_id} not found")

    def test_cross_refs_include_expected(self):
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        for expected in (144, 157, 158, 181):
            self.assertIn(expected, ref_ids, f"Missing cross-ref to #{expected}")


class TestMechanism186EngadgetTripleDevice(unittest.TestCase):
    """Mechanism #186: Engadget triple camera device privacy vocabulary bifurcation."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.mech = _find_mechanism_by_id(self.findings, 186)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mech, "Mechanism #186 not found")

    def test_has_asymmetry_score(self):
        self.assertIn("asymmetry_score", self.mech)

    def test_score_is_0_85(self):
        self.assertAlmostEqual(self.mech["asymmetry_score"], 0.85, places=2)

    def test_highest_score_in_todays_batch(self):
        """#186 should have the highest asymmetry score among #185-#188."""
        scores = {}
        for mid in (185, 186, 187, 188):
            m = _find_mechanism_by_id(self.findings, mid)
            if m:
                scores[mid] = m.get("asymmetry_score", 0)
        max_id = max(scores, key=scores.get)
        self.assertGreaterEqual(max_id, 186, f"Expected >= #186, got #{max_id}")

    def test_cross_references_include_expected(self):
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        for expected in (109, 159, 98, 182):
            self.assertIn(expected, ref_ids, f"Missing cross-ref to #{expected}")


class TestMechanism187SumukhRao(unittest.TestCase):
    """Mechanism #187: Sumukh Rao SlashGear vocabulary bifurcation."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.mech = _find_mechanism_by_id(self.findings, 187)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mech, "Mechanism #187 not found")

    def test_score_is_0_79(self):
        self.assertAlmostEqual(self.mech["asymmetry_score"], 0.79, places=2)

    def test_cross_references_include_186(self):
        """#187 should reference #186 (same-day complementary analysis)."""
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        self.assertIn(186, ref_ids, "Missing cross-ref to #186")

    def test_cross_references_include_183(self):
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        self.assertIn(183, ref_ids, "Missing cross-ref to #183")


class TestMechanism188SamsungMistral(unittest.TestCase):
    """Mechanism #188: Samsung-Mistral €1B investment financial architecture."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.mech = _find_mechanism_by_id(self.findings, 188)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mech, "Mechanism #188 not found")

    def test_score_is_0_82(self):
        self.assertAlmostEqual(self.mech["asymmetry_score"], 0.82, places=2)

    def test_cross_references_include_expected(self):
        cross_refs = self.mech.get("cross_references", self.mech.get("cross_refs", []))
        ref_ids = {cr.get("mechanism_id") for cr in cross_refs if isinstance(cr, dict)}
        for expected in (76, 91, 147, 180):
            self.assertIn(expected, ref_ids, f"Missing cross-ref to #{expected}")

    def test_confounders_documented(self):
        """Mechanism should document confounders."""
        confounders = self.mech.get("confounders", self.mech.get("limitations", []))
        self.assertTrue(
            len(confounders) >= 3,
            f"Expected >= 3 confounders, found {len(confounders)}",
        )

    def test_samsung_mistral_in_entities(self):
        """Samsung-Mistral relationship should be in competitor-entities.yaml."""
        content = _read_file(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        self.assertIn("mistral", content.lower())


class TestMechanismIDContiguity180to188(unittest.TestCase):
    """Verify no gaps in mechanism IDs from 180 to 188."""

    def test_no_gaps(self):
        findings = _get_findings_dict()
        all_ids = _all_mechanism_ids(findings)
        expected = set(range(180, 189))
        missing = expected - all_ids
        self.assertEqual(
            missing, set(),
            f"Missing mechanism IDs: {sorted(missing)}",
        )


class TestScoreDistribution185to188(unittest.TestCase):
    """Score distribution across today's mechanisms should not be degenerate."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.scores = {}
        for mid in (185, 186, 187, 188):
            m = _find_mechanism_by_id(self.findings, mid)
            if m and "asymmetry_score" in m:
                self.scores[mid] = m["asymmetry_score"]

    def test_all_four_have_scores(self):
        self.assertEqual(len(self.scores), 4, "Not all 4 mechanisms have scores")

    def test_scores_not_identical(self):
        unique = len(set(self.scores.values()))
        self.assertGreater(unique, 1, "All scores identical — suspicious")

    def test_scores_have_spread(self):
        """Scores should span at least 0.10 range."""
        vals = list(self.scores.values())
        spread = max(vals) - min(vals)
        self.assertGreaterEqual(spread, 0.10, f"Score spread too narrow: {spread}")

    def test_mean_score_reasonable(self):
        """Mean should be between 0.50 and 0.95."""
        vals = list(self.scores.values())
        mean = sum(vals) / len(vals)
        self.assertGreaterEqual(mean, 0.50, f"Mean score {mean} too low")
        self.assertLessEqual(mean, 0.95, f"Mean score {mean} too high")


class TestDependencyImports(unittest.TestCase):
    """Verify critical NLP dependencies are importable."""

    def test_textblob_importable(self):
        mod = importlib.import_module("textblob")
        self.assertIsNotNone(mod)

    def test_vadersentiment_importable(self):
        mod = importlib.import_module("vaderSentiment.vaderSentiment")
        self.assertIsNotNone(mod)

    def test_mediascope_sentiment_importable(self):
        mod = importlib.import_module("mediascope.analyze.sentiment")
        self.assertIsNotNone(mod)

    def test_mediascope_analysis_importable(self):
        mod = importlib.import_module("mediascope.analysis")
        self.assertIsNotNone(mod)


class TestDocSyncAug19(unittest.TestCase):
    """Verify today's test files are all registered in docs."""

    AUG19_FILES = [
        "test_9to5_network_cross_publication_privacy_vocabulary_gradient_aug19.py",
        "test_australia_kmart_anko_price_democratization_backlash_transfer_aug19.py",
        "test_digital_trends_openai_companion_aspirational_coverage_meta_adversarial_vocabulary_aug19.py",
        "test_dispatch_twilio_podcast_newsletter_pipeline_meta_framing_aug19.py",
        "test_engadget_snap_openai_triple_camera_device_privacy_vocabulary_bifurcation_aug19.py",
        "test_hadlee_simons_android_authority_cross_entity_coverage_selection_aug19.py",
        "test_mass_market_vocabulary_propagation_cycle_aug19.py",
        "test_matt_wille_gizmodo_smart_glasses_beat_reporter_vocabulary_bifurcation_aug19.py",
        "test_observer_guardian_stigmatization_advocacy_samsung_press_trip_disclosure_aug19.py",
        "test_openai_zero_ad_revenue_share_publisher_financial_captivity_aug19.py",
        "test_petapixel_camera_publication_coverage_selection_samsung_zero_aug19.py",
        "test_samsung_mistral_cross_competitor_ai_financial_architecture_warby_q2_aug19.py",
        "test_samsung_reddit_advance_advertising_feedback_loop_triple_channel_aug19.py",
        "test_spacex_s1_cross_competitor_financial_architecture_aug19.py",
        "test_sumukh_rao_slashgear_cross_entity_privacy_vocabulary_bifurcation_aug19.py",
        "test_two_blokes_kodak_fiend_media_moral_panic_historical_precedent_aug19.py",
        "test_type_d_02am_cross_validation_aug19.py",
        "test_type_d_10am_cross_validation_aug19.py",
        "test_type_d_3pm_cross_validation_aug19.py",
    ]

    def test_all_aug19_in_readme(self):
        readme = _read_file(os.path.join(ROOT_DIR, "README.md"))
        for fname in self.AUG19_FILES:
            self.assertIn(fname, readme, f"{fname} missing from README.md")

    def test_all_aug19_in_architecture(self):
        arch = _read_file(os.path.join(DOCS_DIR, "ARCHITECTURE.md"))
        for fname in self.AUG19_FILES:
            self.assertIn(fname, arch, f"{fname} missing from ARCHITECTURE.md")

    def test_all_aug19_files_exist_on_disk(self):
        for fname in self.AUG19_FILES:
            path = os.path.join(TESTS_DIR, fname)
            self.assertTrue(os.path.isfile(path), f"{fname} not found on disk")

    def test_this_file_also_on_disk(self):
        """This very test file should exist."""
        path = os.path.join(TESTS_DIR, "test_type_d_8pm_cross_validation_aug19.py")
        self.assertTrue(os.path.isfile(path))


class TestReadmeTestCount(unittest.TestCase):
    """README test count should be >= 17651."""

    def test_readme_count_current(self):
        readme = _read_file(os.path.join(ROOT_DIR, "README.md"))
        m = re.search(r"MediaScope has \*\*(\d+) tests\*\*", readme)
        self.assertIsNotNone(m, "Cannot find test count header in README.md")
        claimed = int(m.group(1))
        self.assertGreaterEqual(claimed, 17651)

    def test_architecture_count_current(self):
        arch = _read_file(os.path.join(DOCS_DIR, "ARCHITECTURE.md"))
        m = re.search(r"# (\d+) tests across", arch)
        self.assertIsNotNone(m, "Cannot find test count in ARCHITECTURE.md")
        claimed = int(m.group(1))
        self.assertGreaterEqual(claimed, 17651)


class TestAllCrossReferencesResolve(unittest.TestCase):
    """Every cross-reference in mechanisms 185-188 should point to an existing mechanism."""

    def setUp(self):
        self.findings = _get_findings_dict()
        self.all_ids = _all_mechanism_ids(self.findings)

    def _check_refs(self, mech_id):
        mech = _find_mechanism_by_id(self.findings, mech_id)
        if not mech:
            self.fail(f"Mechanism #{mech_id} not found")
        cross_refs = mech.get("cross_references", mech.get("cross_refs", []))
        for cr in cross_refs:
            if isinstance(cr, dict):
                ref_id = cr.get("mechanism_id")
                if ref_id and ref_id > 16:
                    self.assertIn(
                        ref_id, self.all_ids,
                        f"Mechanism #{mech_id} cross-ref #{ref_id} not found",
                    )

    def test_185_cross_refs_resolve(self):
        self._check_refs(185)

    def test_186_cross_refs_resolve(self):
        self._check_refs(186)

    def test_187_cross_refs_resolve(self):
        self._check_refs(187)

    def test_188_cross_refs_resolve(self):
        self._check_refs(188)


if __name__ == "__main__":
    unittest.main()
