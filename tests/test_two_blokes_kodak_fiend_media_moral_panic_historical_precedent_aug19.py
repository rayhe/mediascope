"""Tests for mechanism #177: Two Blokes Kodak Fiend Historical Precedent — Media-Driven Camera Moral Panic Cycle (1888-2026).

Australian tech podcast Two Blokes Talking Tech #744 (Aug 6, 2026) provides the strongest
counterexample to universal negative podcast framing, with hosts who personally own Meta glasses
defending the product and drawing a 138-year historical parallel to the 1888 "Kodak Fiend" panic.
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism_anywhere(data, mechanism_id):
    """Recursively search for a mechanism by ID anywhere in the data structure."""
    if isinstance(data, dict):
        if data.get('mechanism_id') == mechanism_id:
            return data
        for v in data.values():
            result = find_mechanism_anywhere(v, mechanism_id)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism_anywhere(item, mechanism_id)
            if result:
                return result
    return None


class TestMechanism177Exists(unittest.TestCase):
    """Mechanism #177 exists in the YAML with correct structure."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #177 not found in YAML")

    def test_mechanism_name_contains_kodak_fiend(self):
        self.assertIn('Kodak Fiend', self.mechanism.get('mechanism_name', ''))

    def test_mechanism_name_contains_historical(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertTrue('Historical' in name or 'historical' in name or '1888' in name)

    def test_mechanism_type(self):
        self.assertIn('historical_precedent', self.mechanism.get('mechanism_type', ''))

    def test_asymmetry_score_present(self):
        score = self.mechanism.get('asymmetry_score')
        self.assertIsNotNone(score)
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)


class TestHistoricalParallel(unittest.TestCase):
    """The Kodak Fiend / Meta Fiend historical parallel structure."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_historical_parallel_present(self):
        self.assertIn('historical_parallel', self.mechanism)

    def test_1888_kodak_entry(self):
        hp = self.mechanism.get('historical_parallel', {})
        self.assertIn('1888_kodak_fiend', hp)

    def test_2026_meta_entry(self):
        hp = self.mechanism.get('historical_parallel', {})
        self.assertIn('2026_meta_fiend', hp)

    def test_kodak_has_technology(self):
        kodak = self.mechanism.get('historical_parallel', {}).get('1888_kodak_fiend', {})
        self.assertIn('technology', kodak)
        self.assertIn('Kodak', kodak['technology'])

    def test_kodak_has_media_response(self):
        kodak = self.mechanism.get('historical_parallel', {}).get('1888_kodak_fiend', {})
        self.assertIn('media_response', kodak)
        self.assertIn('Fiend', kodak['media_response'])

    def test_meta_has_technology(self):
        meta = self.mechanism.get('historical_parallel', {}).get('2026_meta_fiend', {})
        self.assertIn('technology', meta)

    def test_meta_has_media_response(self):
        meta = self.mechanism.get('historical_parallel', {}).get('2026_meta_fiend', {})
        self.assertIn('media_response', meta)
        self.assertIn('pervert', meta['media_response'].lower())


class TestKeyQuotes(unittest.TestCase):
    """Key quotes from Two Blokes Talking Tech are preserved."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_key_quotes_present(self):
        self.assertIn('key_quotes', self.mechanism)

    def test_kodak_fiend_quote(self):
        quotes = self.mechanism.get('key_quotes', {})
        self.assertIn('trevor_long_kodak_fiend', quotes)
        self.assertIn('Meta Fiend', quotes['trevor_long_kodak_fiend'])

    def test_media_push_quote(self):
        quotes = self.mechanism.get('key_quotes', {})
        self.assertIn('trevor_long_media_push', quotes)

    def test_clickbait_quote(self):
        quotes = self.mechanism.get('key_quotes', {})
        self.assertIn('stephen_fenech_clickbait', quotes)

    def test_airtag_quote(self):
        quotes = self.mechanism.get('key_quotes', {})
        self.assertIn('trevor_long_airtag', quotes)

    def test_creep_label_quote(self):
        quotes = self.mechanism.get('key_quotes', {})
        self.assertIn('trevor_long_creep_label', quotes)


class TestEntityTreatment(unittest.TestCase):
    """Entity treatment within the Two Blokes episode."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_entity_treatment_present(self):
        self.assertIn('entity_treatment_within_episode', self.mechanism)

    def test_meta_treatment(self):
        entities = self.mechanism.get('entity_treatment_within_episode', {})
        self.assertIn('meta', entities)
        meta = entities['meta']
        self.assertIn('framing', meta)
        self.assertIn('privacy_alarm', meta)

    def test_samsung_zero_alarm(self):
        entities = self.mechanism.get('entity_treatment_within_episode', {})
        samsung = entities.get('samsung', {})
        alarm = samsung.get('privacy_alarm', '')
        self.assertIn('Zero', alarm)

    def test_apple_zero_alarm(self):
        entities = self.mechanism.get('entity_treatment_within_episode', {})
        apple = entities.get('apple', {})
        alarm = apple.get('privacy_alarm', '')
        self.assertIn('Zero', alarm)

    def test_kmart_zero_alarm(self):
        entities = self.mechanism.get('entity_treatment_within_episode', {})
        kmart = entities.get('kmart_anko', {})
        alarm = kmart.get('privacy_alarm', '')
        self.assertIn('Zero', alarm)

    def test_meta_vocabulary_positive(self):
        entities = self.mechanism.get('entity_treatment_within_episode', {})
        meta = entities.get('meta', {})
        vocab = meta.get('vocabulary', '')
        self.assertTrue(any(word in vocab for word in ['amazing', 'game changer', 'cool']))


class TestPodcastDetails(unittest.TestCase):
    """Podcast metadata for Two Blokes Talking Tech."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_podcast_details_present(self):
        self.assertIn('podcast_details', self.mechanism)

    def test_show_name(self):
        pd = self.mechanism.get('podcast_details', {})
        self.assertEqual(pd.get('show'), 'Two Blokes Talking Tech')

    def test_episode_number(self):
        pd = self.mechanism.get('podcast_details', {})
        self.assertEqual(pd.get('episode'), 744)

    def test_date(self):
        pd = self.mechanism.get('podcast_details', {})
        date_val = pd.get('date')
        # YAML may parse date as datetime.date or string
        if hasattr(date_val, 'isoformat'):
            self.assertEqual(date_val.isoformat(), '2026-08-06')
        else:
            self.assertEqual(str(date_val), '2026-08-06')

    def test_hosts(self):
        pd = self.mechanism.get('podcast_details', {})
        hosts = pd.get('hosts', [])
        self.assertEqual(len(hosts), 2)

    def test_transcript_available(self):
        pd = self.mechanism.get('podcast_details', {})
        fmt = pd.get('format', '')
        self.assertIn('transcript', fmt.lower())


class TestConfounders(unittest.TestCase):
    """Confounders for mechanism #177."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_confounders_present(self):
        self.assertIn('confounders', self.mechanism)

    def test_at_least_4_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4)

    def test_has_strong_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        strong = [c for c in confounders if c.get('strength') == 'strong']
        self.assertGreaterEqual(len(strong), 2)

    def test_kodak_fiend_confounder(self):
        confounders = self.mechanism.get('confounders', [])
        kodak_refs = [c for c in confounders if 'Kodak' in c.get('description', '') or 'historical' in c.get('description', '').lower()]
        self.assertGreaterEqual(len(kodak_refs), 1)


class TestCrossReferences(unittest.TestCase):
    """Cross-references to other mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_cross_references_present(self):
        self.assertIn('cross_references', self.mechanism)

    def test_references_podcast_ecosystem(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(144, refs, "Should reference #144 (Podcast Ecosystem Amplification)")

    def test_references_multi_vector(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(158, refs, "Should reference #158 (Multi-Vector Cultural Delegitimization)")

    def test_references_kmart(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(175, refs, "Should reference #175 (Australia Kmart Anko)")


class TestSignificance(unittest.TestCase):
    """Significance assessment for mechanism #177."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 177)

    def test_significance_present(self):
        self.assertIn('significance', self.mechanism)

    def test_counterexample_strength_high(self):
        sig = self.mechanism.get('significance', {})
        self.assertEqual(sig.get('counterexample_strength'), 'HIGH')

    def test_limitation_documented(self):
        sig = self.mechanism.get('significance', {})
        self.assertIn('limitation', sig)
        self.assertIn('asymmetry', sig['limitation'].lower())


class TestMechanism176AlsoExists(unittest.TestCase):
    """Verify mechanism #176 (Observer/Guardian Stigmatization Advocacy) is properly in the YAML."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism_anywhere(cls.data, 176)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #176 not found in YAML")

    def test_mechanism_name_contains_stigmatization(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertTrue('Stigmatization' in name or 'stigmatization' in name or 'Observer' in name)

    def test_asymmetry_score(self):
        score = self.mechanism.get('asymmetry_score')
        self.assertIsNotNone(score)
        self.assertGreaterEqual(score, 0.8)

    def test_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 1)


if __name__ == '__main__':
    unittest.main()
