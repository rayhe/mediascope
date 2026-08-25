"""
Type E (Podcast Sentiment): Rabbit Hole Fashion-to-Surveillance Cross-Domain Propagation

Tests for mechanism #296: Rabbit Hole podcast (Rosie Okotchi-Lipinski with Grace Robinson)
"The iPod hair clip to Meta glasses pipeline" (~Aug 20, 2026) propagates the Meta =
surveillance framing from tech journalism into fashion/cultural commentary.

Also covers mechanism #297 (Katie Couric mainstream journalism single-entity expert
authority direction) and mechanism #298 (Vergecast reading list camera wearable vocabulary
curation).

Iteration #282 — Tue 2026-08-25 05:00 PT
"""

import os
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def get_publications(data):
    return data.get('publications', data)


class TestRabbitHoleFashionSurveillanceCrossDomainPropagation(unittest.TestCase):
    """Tests mechanism #296: Cross-domain narrative propagation from tech journalism
    into fashion/cultural commentary via Rabbit Hole podcast."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.mechanism = pubs.get('rabbit_hole_fashion_surveillance_cross_domain_propagation', {})

    def test_mechanism_exists(self):
        pubs = get_publications(self.data)
        self.assertIn('rabbit_hole_fashion_surveillance_cross_domain_propagation', pubs)

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 296)

    def test_mechanism_type_is_cross_domain(self):
        self.assertEqual(self.mechanism.get('mechanism_type'), 'cross_domain_narrative_propagation')

    def test_entities_include_meta_and_competitors(self):
        entities = self.mechanism.get('entities_involved', [])
        for entity in ['meta', 'apple', 'google', 'samsung', 'snap']:
            self.assertIn(entity, entities)

    def test_meta_alarm_terms_greater_than_zero(self):
        self.assertGreater(self.mechanism.get('meta_alarm_terms', 0), 0)

    def test_competitor_alarm_terms_zero(self):
        self.assertEqual(self.mechanism.get('competitor_alarm_terms', 0), 0)

    def test_no_financial_incentive_detected(self):
        self.assertEqual(self.mechanism.get('financial_incentive'), 'none_detected')

    def test_asymmetry_score_above_threshold(self):
        self.assertGreaterEqual(self.mechanism.get('asymmetry_score', 0), 0.7)

    def test_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 2)

    def test_source_url_present(self):
        sources = self.mechanism.get('sources', [])
        self.assertTrue(any('youtube.com' in s for s in sources))


class TestKatieCouricExpertAuthorityMetaExclusiveFraming(unittest.TestCase):
    """Tests mechanism #297: Katie Couric mainstream journalism single-entity
    expert authority direction with Woodrow Hartzog."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.mechanism = pubs.get('katie_couric_mainstream_single_entity_expert_authority_direction', {})

    def test_mechanism_exists(self):
        pubs = get_publications(self.data)
        self.assertIn('katie_couric_mainstream_single_entity_expert_authority_direction', pubs)

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 297)

    def test_mechanism_type(self):
        self.assertEqual(self.mechanism.get('mechanism_type'), 'expert_authority_entity_selection')

    def test_expert_source_is_hartzog(self):
        expert = self.mechanism.get('expert_source', '')
        self.assertIn('Hartzog', expert)
        self.assertIn('Boston University', expert)

    def test_meta_alarm_terms_significantly_higher(self):
        meta_terms = self.mechanism.get('meta_alarm_terms', 0)
        competitor_terms = self.mechanism.get('competitor_alarm_terms', 0)
        self.assertGreater(meta_terms, 10)
        self.assertEqual(competitor_terms, 0)

    def test_stigma_label_imported(self):
        labels = self.mechanism.get('stigma_labels_imported', [])
        self.assertTrue(any(l.get('term') == 'pervert glasses' for l in labels))
        self.assertTrue(any(l.get('origin') == 'Bloomberg' for l in labels))

    def test_asymmetry_score_very_high(self):
        self.assertGreaterEqual(self.mechanism.get('asymmetry_score', 0), 0.85)

    def test_source_url(self):
        sources = self.mechanism.get('sources', [])
        self.assertTrue(any('katiecouric.com' in s for s in sources))


class TestVergecastReadingListCameraWearableVocabularyCuration(unittest.TestCase):
    """Tests mechanism #298: Vergecast two-episode reading list cross-entity
    camera wearable vocabulary curation (Aug 20-22, 2026)."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.mechanism = pubs.get(
            'vergecast_two_episode_reading_list_camera_wearable_vocabulary_curation', {}
        )

    def test_mechanism_exists(self):
        pubs = get_publications(self.data)
        self.assertIn(
            'vergecast_two_episode_reading_list_camera_wearable_vocabulary_curation',
            pubs
        )

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 298)

    def test_mechanism_type(self):
        self.assertEqual(self.mechanism.get('mechanism_type'), 'cross_medium_reading_list_curation')

    def test_three_episodes_tracked(self):
        episodes = self.mechanism.get('episodes', [])
        self.assertEqual(len(episodes), 3)

    def test_meta_article_is_menace(self):
        episodes = self.mechanism.get('episodes', [])
        pixel_ep = next((e for e in episodes if 'Pixel 11' in e.get('title', '')), None)
        self.assertIsNotNone(pixel_ep)
        self.assertIn('menace', pixel_ep.get('meta_article', '').lower())

    def test_apple_article_is_neutral(self):
        episodes = self.mechanism.get('episodes', [])
        pixel_ep = next((e for e in episodes if 'Pixel 11' in e.get('title', '')), None)
        self.assertIsNotNone(pixel_ep)
        apple_article = pixel_ep.get('apple_article', '')
        self.assertIn('appear', apple_article.lower())
        self.assertNotIn('menace', apple_article.lower())
        self.assertNotIn('creepy', apple_article.lower())

    def test_snap_specs_episode_zero_privacy_terms(self):
        episodes = self.mechanism.get('episodes', [])
        snap_ep = next((e for e in episodes if 'Snap' in e.get('title', '')), None)
        self.assertIsNotNone(snap_ep)
        self.assertEqual(snap_ep.get('privacy_terms', -1), 0)

    def test_meta_alarm_greater_than_competitor(self):
        self.assertGreater(
            self.mechanism.get('meta_alarm_terms', 0),
            self.mechanism.get('competitor_alarm_terms', 0)
        )


class TestPodcastSentimentDocHasNewEntries(unittest.TestCase):
    """Verify podcast-sentiment.md contains the new entries from iteration #282."""

    def setUp(self):
        sentinel_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentinel_path, 'r') as f:
            self.content = f.read()

    def test_rabbit_hole_entry_exists(self):
        self.assertIn('iPod hair clip to Meta glasses pipeline', self.content)
        self.assertIn('Rosie Okotchi-Lipinski', self.content)
        self.assertIn('Grace Robinson', self.content)

    def test_katie_couric_entry_exists(self):
        self.assertIn('Katie Couric Media', self.content)
        self.assertIn('Woodrow Hartzog', self.content)
        self.assertIn('Meta Glasses Privacy Concerns Raise Real Issues', self.content)

    def test_vergecast_aug21_entry_exists(self):
        self.assertIn('Pixel 11 gets in on the digicam trend', self.content)
        self.assertIn('Snap\'s Specs look good on nobody', self.content)

    def test_mechanism_296_referenced(self):
        self.assertIn('#296', self.content)

    def test_mechanism_297_referenced(self):
        self.assertIn('#297', self.content)

    def test_mechanism_298_referenced(self):
        self.assertIn('#298', self.content)


if __name__ == '__main__':
    unittest.main()
