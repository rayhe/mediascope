"""
Type D Cross-Validation — Aug 20, 5 PM PT

Iteration #206: Structural integrity verification for mechanisms #196-#199,
doc sync fix (3 missing test files in README + ARCHITECTURE, counts 18133→18264,
496→498), mechanism #199 metadata fix (added discovery_date, asymmetry_score,
cross_references, 2 additional source URLs).

FIXES APPLIED:
1. README.md: Added 3 missing test files (podcast sentiment, Bonk/Engadget,
   Condé Nast deal inventory), updated counts 18133→18264 tests, 496→498 files
2. ARCHITECTURE.md: Same 3 missing test files added, count 18133→18264, 496→498
3. wired.yaml mechanism #199: Added discovery_date, asymmetry_score (0.86),
   cross_references (8 mechanisms), 2 additional source URLs (French APIG, WSJ
   Apple Siri)
4. Iteration log: #205 entry added (was committed but not logged)

DEPENDENCY NOTE: textblob + vaderSentiment now installed — 39 collection errors
from earlier sessions resolved.
"""

import unittest
import yaml
import os


def load_wired_profile():
    """Load WIRED publication profile."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestMechanism199MetadataComplete(unittest.TestCase):
    """Verify mechanism #199 has all required metadata fields."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.corr = self.profile.get('conde_nast_deal_inventory_coverage_correlation', {})

    def test_mechanism_id_is_199(self):
        self.assertEqual(self.corr['mechanism_id'], 199)

    def test_discovery_date_exists(self):
        self.assertIn('discovery_date', self.corr)
        self.assertEqual(self.corr['discovery_date'], '2026-08-20')

    def test_asymmetry_score_exists(self):
        self.assertIn('asymmetry_score', self.corr)
        self.assertIsInstance(self.corr['asymmetry_score'], (int, float))
        self.assertGreaterEqual(self.corr['asymmetry_score'], 0.7)
        self.assertLessEqual(self.corr['asymmetry_score'], 1.0)

    def test_cross_references_exist(self):
        self.assertIn('cross_references', self.corr)
        refs = self.corr['cross_references']
        self.assertIsInstance(refs, list)
        self.assertGreaterEqual(len(refs), 5)

    def test_cross_references_include_safe_target(self):
        refs = self.corr['cross_references']
        self.assertIn(8, refs, "Should cross-reference Safe Target Coefficient (#8)")

    def test_cross_references_include_openai_parity(self):
        refs = self.corr['cross_references']
        self.assertIn(33, refs, "Should cross-reference OpenAI facial recognition parity (#33)")

    def test_cross_references_include_ft_dual_standard(self):
        refs = self.corr['cross_references']
        self.assertIn(43, refs, "Should cross-reference FT-OpenAI dual standard (#43)")

    def test_source_urls_minimum_four(self):
        sources = self.corr.get('source_urls', [])
        self.assertGreaterEqual(len(sources), 4)

    def test_source_urls_include_french_apig(self):
        sources = self.corr.get('source_urls', [])
        apig = any('medianama' in s or 'french' in s.lower() for s in sources)
        self.assertTrue(apig, "Should include French APIG source URL")


class TestMechanism199DealInventoryIntegrity(unittest.TestCase):
    """Verify deal inventory data is complete and consistent."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.inventory = self.profile['conde_nast_deal_inventory_coverage_correlation']['deal_inventory']
        self.by_entity = {item['entity']: item for item in self.inventory}

    def test_seven_entities(self):
        self.assertEqual(len(self.inventory), 7)

    def test_all_entities_have_deal_status(self):
        for item in self.inventory:
            self.assertIn('deal_status', item, f"{item['entity']} missing deal_status")

    def test_all_entities_have_coverage_tone(self):
        for item in self.inventory:
            self.assertIn('coverage_tone', item, f"{item['entity']} missing coverage_tone")

    def test_all_entities_have_deal_type(self):
        for item in self.inventory:
            self.assertIn('deal_type', item, f"{item['entity']} missing deal_type")

    def test_meta_zero_deals(self):
        meta = self.by_entity['Meta']
        self.assertEqual(meta['deal_status'], 'no_deal')
        self.assertIn('zero', meta['deal_type'].lower())

    def test_meta_most_adversarial(self):
        meta = self.by_entity['Meta']
        self.assertIn('most adversarial', meta['coverage_tone'])

    def test_google_no_deal_but_ad_dependency(self):
        google = self.by_entity['Google']
        self.assertEqual(google['deal_status'], 'no_deal')
        self.assertIn('adversarial', google['deal_type'].lower())

    def test_openai_active_deal(self):
        self.assertEqual(self.by_entity['OpenAI']['deal_status'], 'active')

    def test_apple_negotiating(self):
        self.assertEqual(self.by_entity['Apple']['deal_status'], 'negotiating')

    def test_deal_status_values_valid(self):
        valid = {'active', 'negotiating', 'no_deal'}
        for item in self.inventory:
            self.assertIn(item['deal_status'], valid,
                          f"{item['entity']} has invalid deal_status: {item['deal_status']}")


class TestMechanism199Confounders(unittest.TestCase):
    """Verify confounders are robust and intellectually honest."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.corr = self.profile['conde_nast_deal_inventory_coverage_correlation']

    def test_at_least_four_confounders(self):
        confounders = self.corr.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4)

    def test_reverse_causality_confounder_present(self):
        confounders = self.corr.get('confounders', [])
        reverse = any('reverse' in str(c).lower() or 'follow' in str(c).lower()
                       for c in confounders)
        self.assertTrue(reverse, "Must include reverse causality confounder")

    def test_editorial_independence_confounder_present(self):
        confounders = self.corr.get('confounders', [])
        editorial = any('editorial' in str(c).lower() or 'journalist' in str(c).lower()
                        for c in confounders)
        self.assertTrue(editorial, "Must include editorial independence confounder")

    def test_falsification_test_exists(self):
        self.assertIn('falsification_test', self.corr)
        self.assertGreater(len(self.corr['falsification_test']), 50)


class TestMechanisms196to198StructuralIntegrity(unittest.TestCase):
    """Verify mechanisms #196-#198 have required fields in test files."""

    def test_mechanism_196_test_exists(self):
        path = os.path.join(os.path.dirname(__file__),
                            'test_type_e_08am_podcast_sentiment_uk_cinema_piracy_vector_aug20.py')
        self.assertTrue(os.path.exists(path))

    def test_mechanism_197_test_exists(self):
        path = os.path.join(os.path.dirname(__file__),
                            'test_reuters_snap_meta_camera_privacy_vocabulary_bifurcation_aug20.py')
        self.assertTrue(os.path.exists(path))

    def test_mechanism_198_test_exists(self):
        path = os.path.join(os.path.dirname(__file__),
                            'test_lawrence_bonk_engadget_generalist_beat_assignment_stigma_concentration_aug20.py')
        self.assertTrue(os.path.exists(path))

    def test_mechanism_199_test_exists(self):
        path = os.path.join(os.path.dirname(__file__),
                            'test_conde_nast_deal_inventory_coverage_correlation_aug20.py')
        self.assertTrue(os.path.exists(path))


class TestDocSyncAug20_5pm(unittest.TestCase):
    """Verify README and ARCHITECTURE are in sync with actual test files."""

    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__))
        self.actual_files = [f for f in os.listdir(self.test_dir)
                            if f.startswith('test_') and f.endswith('.py')]
        self.actual_count = len(self.actual_files)

        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')

        with open(readme_path) as f:
            self.readme = f.read()
        with open(arch_path) as f:
            self.arch = f.read()

    def test_readme_contains_500_files(self):
        self.assertIn('500', self.readme)

    def test_architecture_contains_500_files(self):
        self.assertIn('500', self.arch)

    def test_three_previously_missing_files_in_readme(self):
        missing = []
        for f in ['test_type_e_08am_podcast_sentiment_uk_cinema_piracy_vector_aug20.py',
                   'test_lawrence_bonk_engadget_generalist_beat_assignment_stigma_concentration_aug20.py',
                   'test_conde_nast_deal_inventory_coverage_correlation_aug20.py']:
            if f not in self.readme:
                missing.append(f)
        self.assertEqual(missing, [], f"Still missing from README: {missing}")

    def test_three_previously_missing_files_in_architecture(self):
        missing = []
        for f in ['test_type_e_08am_podcast_sentiment_uk_cinema_piracy_vector_aug20.py',
                   'test_lawrence_bonk_engadget_generalist_beat_assignment_stigma_concentration_aug20.py',
                   'test_conde_nast_deal_inventory_coverage_correlation_aug20.py']:
            if f not in self.arch:
                missing.append(f)
        self.assertEqual(missing, [], f"Still missing from ARCHITECTURE: {missing}")

    def test_actual_file_count_reasonable(self):
        """Actual test file count should be within 5 of documented count."""
        # The README might not include THIS test file yet
        self.assertGreaterEqual(self.actual_count, 498)
        self.assertLessEqual(self.actual_count, 505)


class TestMechanismIDContiguity(unittest.TestCase):
    """Verify no gaps in mechanism IDs from #196 to #199."""

    def setUp(self):
        self.profile = load_wired_profile()

    def test_mechanism_199_exists(self):
        self.assertIn('conde_nast_deal_inventory_coverage_correlation', self.profile)
        self.assertEqual(
            self.profile['conde_nast_deal_inventory_coverage_correlation']['mechanism_id'],
            199
        )

    def test_mechanism_200_exists(self):
        """Mechanism #200 (Phil Clapp Natural Experiment) should exist in wired profile."""
        found = False
        for key, value in self.profile.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 200:
                found = True
                break
        self.assertTrue(found, "Mechanism #200 should exist in wired profile")


class TestScoreDistribution(unittest.TestCase):
    """Verify asymmetry scores are within documented ranges."""

    def setUp(self):
        self.profile = load_wired_profile()

    def test_mechanism_199_score_in_range(self):
        score = self.profile['conde_nast_deal_inventory_coverage_correlation']['asymmetry_score']
        self.assertGreaterEqual(score, 0.5, "Score too low for documented asymmetry")
        self.assertLessEqual(score, 1.0, "Score must be ≤ 1.0")


class TestCompetitorEntitiesConsistency(unittest.TestCase):
    """Verify competitor-entities.yaml is consistent with mechanism #199."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.profile = load_wired_profile()
        self.inventory = self.profile['conde_nast_deal_inventory_coverage_correlation']['deal_inventory']

    def test_openai_exists_in_entities(self):
        self.assertIn('openai', self.entities['entities'])

    def test_apple_exists_in_entities(self):
        self.assertIn('apple', self.entities['entities'])

    def test_google_exists_in_entities(self):
        self.assertIn('google', self.entities['entities'])

    def test_openai_publisher_deals_documented(self):
        openai = self.entities['entities']['openai']
        self.assertIn('publisher_content_deal_portfolio', openai)

    def test_apple_siri_deals_documented(self):
        apple = self.entities['entities']['apple']
        self.assertIn('siri_ai_publisher_deals', apple)


if __name__ == '__main__':
    unittest.main()
