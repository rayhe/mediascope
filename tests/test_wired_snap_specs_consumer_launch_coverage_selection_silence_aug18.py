"""
Test: WIRED Snap SPECS Consumer Launch Coverage Selection Silence (Mechanism #163)

TYPE A: Competitor Coverage Deep Dive — WIRED × Snap

FINDING: On June 16, 2026, Snap unveiled SPECS — its first consumer AR glasses ($2,195)
with 4 cameras, dual Snapdragon processors, OpenAI + Google Gemini multimodal AI, and
recording capabilities syncing to Snapchat — at AWE USA 2026. This is the most
camera-dense smart glasses product ever launched for consumers. WIRED published ZERO
standalone privacy investigations of Snap SPECS despite publishing an investigative
exposé on Meta's DORMANT NameTag facial recognition code just 12 days earlier (June 4-5).

TEMPORAL NATURAL EXPERIMENT:
  June 4-5, 2026: WIRED publishes NameTag exposé (Meta, 1 camera, code never activated)
  June 16, 2026: Snap SPECS unveiled at AWE (4 cameras, OpenAI+Gemini AI, consumer launch)
  June 2026+: WIRED publishes ZERO privacy investigations of Snap SPECS

HARDWARE COMPARISON:
  Snap SPECS: 4 cameras, dual Snapdragon processors, OpenAI+Gemini multimodal AI,
    recording syncs to Snapchat, consumer launch $2,195
  Meta Ray-Ban: 1 camera (12MP), Meta AI, privacy LED, consumer product $299-$539

Coverage confirmed at OTHER outlets (proving newsworthiness):
  FastCompany, Engadget, TechSpot, Tom's Guide, MacRumors, Road to VR, UploadVR,
  9to5Google — all covered Snap SPECS with neutral/aspirational framing.

FINANCIAL CONTEXT:
  Advance Publications (WIRED parent via Condé Nast) → ~30% Reddit stake ($9.5B)
  Reddit Q2 2026: $805M rev, $762M ad rev — direct Meta ad competitor
  Snap is Meta's competitor in social + AR glasses — not Advance's competitor
  WIRED's parent benefits when Meta's ad-competing position weakens

CROSS-REFERENCES:
  #130 (Snap privacy-free framing at Gizmodo)
  #159 (OpenAI companion vs Meta surveillance vocabulary bifurcation)
  #154 (WIRED Anthropic automode coverage silence)
  #162 (Advance Reddit equity-capital feedback loop)
"""

import unittest
import yaml
import os
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_yaml(filename):
    path = os.path.join(REPO_ROOT, 'profiles', filename)
    with open(path) as f:
        return yaml.safe_load(f)

def find_mechanism(data, slug_fragment):
    """Find a mechanism in cross_publication_findings or aggregate_findings by slug fragment."""
    for section_name in ['cross_publication_findings', 'aggregate_findings']:
        section = data.get(section_name, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if slug_fragment in key and isinstance(value, dict):
                    return value
    return None


class TestMechanismExistence(unittest.TestCase):
    """Mechanism #163 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism for WIRED Snap SPECS coverage silence must exist")

    def test_mechanism_id_is_163(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 163)

    def test_finding_type(self):
        ft = self.mechanism.get('finding_type', '')
        self.assertIn('coverage_selection', ft.lower())

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3, "Must have at least 3 source URLs")

    def test_has_test_file(self):
        tf = self.mechanism.get('test_file', '')
        self.assertIn('wired_snap_specs', tf)

    def test_has_confounders(self):
        conf = self.mechanism.get('confounders', self.mechanism.get('confounding_factors', []))
        self.assertGreaterEqual(len(conf), 4, "Must have at least 4 confounders")

    def test_has_cross_references(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 3)

    def test_date_is_august_2026(self):
        date = str(self.mechanism.get('date', ''))
        self.assertIn('2026-08', date)

    def test_asymmetry_score(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.7)


class TestSnapSpecsHardwareCapabilities(unittest.TestCase):
    """Document Snap SPECS hardware for comparison with Meta Ray-Ban."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_snap_camera_count(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        self.assertEqual(hw.get('camera_count'), 4)

    def test_snap_has_openai_integration(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        ai = hw.get('ai_integrations', [])
        self.assertTrue(any('openai' in str(x).lower() for x in ai))

    def test_snap_has_gemini_integration(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        ai = hw.get('ai_integrations', [])
        self.assertTrue(any('gemini' in str(x).lower() for x in ai))

    def test_snap_consumer_price(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        price = hw.get('price_usd', 0)
        self.assertEqual(price, 2195)

    def test_snap_launch_date(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        launch = str(hw.get('unveil_date', ''))
        self.assertIn('2026-06-16', launch)

    def test_meta_camera_count(self):
        hw = self.mechanism.get('meta_rayban_hardware', {})
        self.assertEqual(hw.get('camera_count'), 1)

    def test_camera_count_ratio(self):
        snap_hw = self.mechanism.get('snap_specs_hardware', {})
        meta_hw = self.mechanism.get('meta_rayban_hardware', {})
        self.assertGreater(snap_hw.get('camera_count', 0), meta_hw.get('camera_count', 0),
                          "Snap SPECS must have MORE cameras than Meta Ray-Ban")

    def test_snap_dual_snapdragon(self):
        hw = self.mechanism.get('snap_specs_hardware', {})
        self.assertEqual(hw.get('processor_count'), 2)


class TestTemporalNaturalExperiment(unittest.TestCase):
    """The 12-day gap between WIRED NameTag exposé and Snap SPECS launch."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_nametag_expose_date(self):
        timeline = self.mechanism.get('temporal_experiment', {})
        self.assertIn('2026-06', str(timeline.get('wired_nametag_expose_date', '')))

    def test_snap_specs_unveil_date(self):
        timeline = self.mechanism.get('temporal_experiment', {})
        self.assertIn('2026-06-16', str(timeline.get('snap_specs_unveil_date', '')))

    def test_gap_days(self):
        timeline = self.mechanism.get('temporal_experiment', {})
        gap = timeline.get('gap_days', 0)
        self.assertLessEqual(gap, 15, "Gap between WIRED NameTag exposé and Snap SPECS must be ≤15 days")

    def test_wired_snap_privacy_articles_count(self):
        timeline = self.mechanism.get('temporal_experiment', {})
        count = timeline.get('wired_snap_specs_privacy_articles', 0)
        self.assertEqual(count, 0, "WIRED published zero privacy investigations of Snap SPECS")

    def test_wired_meta_privacy_articles_count(self):
        timeline = self.mechanism.get('temporal_experiment', {})
        count = timeline.get('wired_meta_glasses_privacy_articles_2026', 0)
        self.assertGreaterEqual(count, 2, "WIRED published 2+ privacy articles on Meta glasses in 2026")


class TestCoverageAtOtherOutlets(unittest.TestCase):
    """Other outlets covered Snap SPECS — proving newsworthiness."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_other_outlets_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        self.assertGreaterEqual(len(outlets), 5)

    def test_fastcompany_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        outlet_names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('fastcompany' in str(n).lower() or 'fast company' in str(n).lower()
                           for n in outlet_names))

    def test_engadget_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        outlet_names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('engadget' in str(n).lower() for n in outlet_names))

    def test_no_outlet_raised_privacy_alarm(self):
        """No major outlet raised privacy alarm about Snap SPECS cameras."""
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        for o in outlets:
            if isinstance(o, dict):
                alarm = o.get('privacy_alarm_terms', 0)
                self.assertEqual(alarm, 0,
                    f"Outlet {o.get('outlet', '?')} should have zero privacy alarm terms for Snap SPECS")


class TestPrivacyVocabularyDelta(unittest.TestCase):
    """WIRED's privacy vocabulary for Meta vs Snap."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_meta_alarm_terms_documented(self):
        vocab = self.mechanism.get('wired_privacy_vocabulary', {})
        meta_terms = vocab.get('meta_glasses_alarm_terms', [])
        self.assertGreaterEqual(len(meta_terms), 5, "Must document 5+ Meta alarm terms from WIRED")

    def test_snap_alarm_terms_zero(self):
        vocab = self.mechanism.get('wired_privacy_vocabulary', {})
        snap_terms = vocab.get('snap_specs_alarm_terms', [])
        self.assertEqual(len(snap_terms), 0, "Snap SPECS should have zero alarm terms from WIRED")

    def test_vocabulary_ratio_is_infinite(self):
        vocab = self.mechanism.get('wired_privacy_vocabulary', {})
        ratio = vocab.get('alarm_term_ratio_description', '')
        self.assertIn('infinite', ratio.lower())

    def test_meta_terms_include_surveillance(self):
        vocab = self.mechanism.get('wired_privacy_vocabulary', {})
        meta_terms = [t.lower() for t in vocab.get('meta_glasses_alarm_terms', [])]
        self.assertTrue(any('surveillance' in t for t in meta_terms))

    def test_meta_terms_include_biometric(self):
        vocab = self.mechanism.get('wired_privacy_vocabulary', {})
        meta_terms = [t.lower() for t in vocab.get('meta_glasses_alarm_terms', [])]
        self.assertTrue(any('biometric' in t or 'faceprint' in t for t in meta_terms))


class TestWiredLegacySnapCoverage(unittest.TestCase):
    """WIRED's historical pattern: Snap glasses always get positive/neutral framing."""

    @classmethod
    def setUpClass(cls):
        cls.wired = load_yaml('wired.yaml')
        # snap_spectacles lives under cross_entity_wearables_framing.evidence
        cls.cewf = cls.wired.get('cross_entity_wearables_framing', {})
        cls.evidence = cls.cewf.get('evidence', {})

    def test_2018_snap_spectacles_tone(self):
        snap = self.evidence.get('snap_spectacles', {})
        tone = snap.get('tone', '')
        self.assertNotIn('surveillance', tone.lower())
        self.assertNotIn('alarm', tone.lower())

    def test_2018_snap_spectacles_privacy_false(self):
        snap = self.evidence.get('snap_spectacles', {})
        self.assertFalse(snap.get('privacy_concerns_raised', True))

    def test_meta_glasses_privacy_true(self):
        meta = self.evidence.get('meta_glasses', {})
        self.assertTrue(meta.get('privacy_concerns_raised', False))

    def test_camera_count_paradox_documented(self):
        paradox = self.cewf.get('camera_count_paradox', '')
        self.assertIn('camera', paradox.lower())


class TestFinancialIncentiveAlignment(unittest.TestCase):
    """Financial context: Advance's Reddit stake creates structural coverage incentive."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_advance_reddit_stake_documented(self):
        fin = self.mechanism.get('financial_context', {})
        stake = fin.get('advance_reddit_ownership_pct', 0)
        self.assertGreaterEqual(stake, 22)

    def test_reddit_meta_ad_competition(self):
        fin = self.mechanism.get('financial_context', {})
        self.assertTrue(fin.get('reddit_competes_with_meta_ads', False))

    def test_snap_not_advance_competitor(self):
        fin = self.mechanism.get('financial_context', {})
        self.assertFalse(fin.get('snap_competes_with_advance_interests', True),
                        "Snap does not directly compete with Advance's financial interests")

    def test_cross_reference_to_162(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(162, refs, "Must cross-reference mechanism #162 (Advance Reddit)")


class TestConfounderAnalysis(unittest.TestCase):
    """Confounders are documented with strength ratings."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism(cls.ccr, 'wired_snap_specs_consumer_coverage_selection_silence')

    def test_has_strong_confounders(self):
        conf = self.mechanism.get('confounders', self.mechanism.get('confounding_factors', []))
        strong = [c for c in conf if isinstance(c, dict) and c.get('strength', '').upper() == 'STRONG']
        self.assertGreaterEqual(len(strong), 2, "Must have at least 2 STRONG confounders")

    def test_meta_market_share_confounder(self):
        """Meta's dominant market share makes it a more natural target for scrutiny."""
        conf = self.mechanism.get('confounders', self.mechanism.get('confounding_factors', []))
        descriptions = [str(c.get('description', '') if isinstance(c, dict) else c) for c in conf]
        self.assertTrue(any('market share' in d.lower() or 'dominant' in d.lower() for d in descriptions))

    def test_nametag_genuine_violation_confounder(self):
        """NameTag was a genuine hidden code issue, distinct from disclosed cameras."""
        conf = self.mechanism.get('confounders', self.mechanism.get('confounding_factors', []))
        descriptions = [str(c.get('description', '') if isinstance(c, dict) else c) for c in conf]
        self.assertTrue(any('nametag' in d.lower() or 'hidden code' in d.lower() or 'genuine' in d.lower()
                           for d in descriptions))

    def test_price_point_confounder(self):
        """$2,195 niche vs mass-market may explain less editorial investment."""
        conf = self.mechanism.get('confounders', self.mechanism.get('confounding_factors', []))
        descriptions = [str(c.get('description', '') if isinstance(c, dict) else c) for c in conf]
        self.assertTrue(any('price' in d.lower() or 'niche' in d.lower() or '$2,195' in d for d in descriptions))


class TestDocSyncIntegrity(unittest.TestCase):
    """README and ARCHITECTURE list this test file and have consistent counts."""

    def test_test_file_exists_on_disk(self):
        test_path = os.path.join(REPO_ROOT, 'tests',
                                 'test_wired_snap_specs_consumer_launch_coverage_selection_silence_aug18.py')
        self.assertTrue(os.path.exists(test_path))

    def test_readme_lists_test_file(self):
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        with open(readme_path) as f:
            content = f.read()
        self.assertIn('test_wired_snap_specs_consumer_launch_coverage_selection_silence_aug18', content)

    def test_architecture_lists_test_file(self):
        arch_path = os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        self.assertIn('test_wired_snap_specs_consumer_launch_coverage_selection_silence_aug18', content)

    def test_file_counts_match(self):
        """README and ARCHITECTURE should agree on test file count."""
        readme_path = os.path.join(REPO_ROOT, 'README.md')
        arch_path = os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')
        test_files = glob.glob(os.path.join(REPO_ROOT, 'tests', 'test_*.py'))
        actual_count = len(test_files)

        with open(readme_path) as f:
            readme = f.read()
        with open(arch_path) as f:
            arch = f.read()

        # Both should mention the actual count
        self.assertIn(str(actual_count), readme,
                     f"README should contain actual test file count {actual_count}")
        self.assertIn(str(actual_count), arch,
                     f"ARCHITECTURE should contain actual test file count {actual_count}")


if __name__ == '__main__':
    unittest.main()
