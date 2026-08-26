"""
Test: ICYMI (Slate) "Surveillance Glasses For Girls!" — Gendered Entity-Exclusive Cultural Consensus (Mechanism #311)

Type E — Podcast Sentiment Tracking
Date: Aug 25, 2026

Episode: "Surveillance Glasses For Girls!" (Jul 8, 2026)
Host: Kate Lindsay
Guest: Matt Bernstein (host, A Bit Fruity)
Publisher: Slate (Graham Holdings Company)
Platform: Acast
Source URL: https://shows.acast.com/icymi/episodes/6a4d47cd4d6f6e9e984eb3e8

Core Finding:
ICYMI (Slate/Graham Holdings) episode applies surveillance/alarm vocabulary exclusively to Meta
glasses while zero competitor camera-equipped wearables are mentioned. This is significant because
Graham Holdings has ZERO documented AI financial relationships with any company (no OpenAI deal,
no Google Showcase, no Apple News Plus, no Perplexity licensing, no Meta relationship). When
a publication with no financial incentive produces the identical entity-selective framing as
publications with documented financial incentives (WIRED/Advance with OpenAI deal, FT with
OpenAI/Google deals, etc.), it demonstrates the framing has become self-sustaining cultural
consensus. The financial incentive chain created the initial asymmetry; cultural consensus now
maintains and propagates it without requiring further financial fuel.

The gendered framing ("Surveillance Glasses For Girls!") adds a feminist lens that further
concentrates scrutiny on Meta's Kylie Jenner collaboration while ignoring Google's Warby Parker
partnership, Samsung's Gentle Monster collaboration, and Apple's upcoming smart glasses — all
targeting fashion-conscious consumers with identical camera hardware.

Cross-references:
- Mechanism #35: Advance/Condé Nast aggregate AI revenue dependency (initial financial incentive)
- Mechanism #296: Rabbit Hole fashion-surveillance podcast (parallel cultural consensus)
- Mechanism #227: Taylor Lorenz Back Row fashion podcast (gendered framing parallel)
- Mechanism #225: Vergecast three-episode vocabulary convergence (source vocabulary)

Confounders:
1. MODERATE: Meta has shipped 10M+ glasses vs zero for competitors
2. MODERATE: BBC investigations documented real Meta glasses misuse
3. WEAK: Podcast format favors concrete examples over hypotheticals
4. STRONG: Kylie Jenner collaboration is a genuine news event — "sinister" is editorial choice
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


def find_mechanism(data, mechanism_id):
    """Recursively search for a mechanism by ID across all sections."""
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                mid = value.get('mechanism_id') or value.get('mechanism_number')
                if mid == mechanism_id:
                    return value
                result = find_mechanism(value, mechanism_id)
                if result:
                    return result
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        mid = item.get('mechanism_id') or item.get('mechanism_number')
                        if mid == mechanism_id:
                            return item
                        result = find_mechanism(item, mechanism_id)
                        if result:
                            return result
    return None


class TestMechanism311Exists(unittest.TestCase):
    """Verify mechanism #311 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism(cls.data, 311)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #311 must exist")

    def test_mechanism_type(self):
        self.assertIn('podcast_sentiment', self.mechanism.get('type', ''),
                      "Mechanism #311 must be podcast_sentiment type")

    def test_mechanism_domain(self):
        self.assertEqual(self.mechanism.get('domain'), 'podcast_sentiment_tracking')

    def test_finding_type(self):
        finding_type = self.mechanism.get('finding_type', '')
        self.assertIn('cultural_consensus', finding_type,
                      "Finding type must reference cultural consensus")


class TestICYMIPodcastProfile(unittest.TestCase):
    """Verify ICYMI podcast source details are documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism(cls.data, 311)

    def test_podcast_publisher_is_slate(self):
        podcast = self.mechanism.get('podcast', {})
        publisher = podcast.get('publisher', '')
        self.assertIn('Slate', publisher,
                      "Podcast publisher must be Slate")

    def test_parent_company_is_graham_holdings(self):
        podcast = self.mechanism.get('podcast', {})
        parent = podcast.get('parent_company', '')
        self.assertIn('Graham Holdings', parent,
                      "Parent company must be Graham Holdings")

    def test_no_ai_financial_relationships(self):
        podcast = self.mechanism.get('podcast', {})
        financial = podcast.get('financial_relationships_with_ai_companies', '')
        self.assertIn('none', str(financial).lower(),
                      "ICYMI/Slate must have no documented AI financial relationships")

    def test_episode_details(self):
        episode = self.mechanism.get('episode', {})
        self.assertEqual(episode.get('title'), 'Surveillance Glasses For Girls!')
        self.assertEqual(episode.get('date'), '2026-07-08')
        self.assertIn('Matt Bernstein', episode.get('guest', ''))


class TestEntityCoverageAsymmetry(unittest.TestCase):
    """Verify Meta-exclusive surveillance framing with zero competitor coverage."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism(cls.data, 311)
        cls.entity_coverage = cls.mechanism.get('entity_coverage', {})
        cls.vocab = cls.mechanism.get('vocabulary_analysis', {})

    def test_meta_mentioned(self):
        meta = self.entity_coverage.get('meta', {})
        self.assertTrue(meta.get('mentioned'), "Meta must be mentioned")

    def test_meta_framing_is_adversarial(self):
        meta = self.entity_coverage.get('meta', {})
        self.assertEqual(meta.get('framing'), 'adversarial',
                         "Meta framing must be adversarial")

    def test_apple_not_mentioned(self):
        apple = self.entity_coverage.get('apple', {})
        self.assertFalse(apple.get('mentioned', True),
                         "Apple must not be mentioned in episode")

    def test_google_not_mentioned(self):
        google = self.entity_coverage.get('google', {})
        self.assertFalse(google.get('mentioned', True),
                         "Google must not be mentioned in episode")

    def test_samsung_not_mentioned(self):
        samsung = self.entity_coverage.get('samsung', {})
        self.assertFalse(samsung.get('mentioned', True),
                         "Samsung must not be mentioned in episode")

    def test_snap_not_mentioned(self):
        snap = self.entity_coverage.get('snap', {})
        self.assertFalse(snap.get('mentioned', True),
                         "Snap must not be mentioned in episode")

    def test_meta_alarm_vocabulary_nonzero(self):
        count = self.vocab.get('meta_alarm_count', 0)
        self.assertGreaterEqual(count, 5,
                                "Meta alarm vocabulary count must be >= 5")

    def test_competitor_alarm_vocabulary_zero(self):
        for entity in ['apple', 'google', 'samsung', 'snap']:
            count = self.vocab.get(f'{entity}_alarm_count', 0)
            self.assertEqual(count, 0,
                             f"{entity} alarm vocabulary count must be 0")


class TestGenderedFraming(unittest.TestCase):
    """Verify gendered framing analysis is documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism(cls.data, 311)
        cls.gendered = cls.mechanism.get('gendered_framing', {})

    def test_gendered_framing_present(self):
        self.assertTrue(self.gendered.get('present'),
                        "Gendered framing must be present")

    def test_gendered_angle_is_feminist(self):
        angle = self.gendered.get('angle', '')
        self.assertIn('feminist', angle.lower(),
                      "Gendered angle must reference feminist framing")

    def test_competitor_equivalent_absent(self):
        equiv = self.gendered.get('equivalent_analysis_for_competitors', '')
        self.assertEqual(equiv, 'absent',
                         "Equivalent gendered analysis for competitors must be absent")


class TestCulturalConsensusEvidence(unittest.TestCase):
    """Verify cultural consensus propagation evidence."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        cls.mechanism = find_mechanism(cls.data, 311)
        cls.consensus = cls.mechanism.get('cultural_consensus_evidence', {})

    def test_financial_incentive_absent(self):
        self.assertTrue(self.consensus.get('financial_incentive_absent'),
                        "Financial incentive must be documented as absent")

    def test_parent_company_ai_deals_none(self):
        deals = self.consensus.get('parent_company_ai_deals', '')
        self.assertEqual(deals, 'none',
                         "Parent company AI deals must be 'none'")

    def test_framing_matches_financially_incentivized_publications(self):
        self.assertTrue(
            self.consensus.get('framing_matches_financially_incentivized_publications'),
            "Framing must match that of financially incentivized publications")

    def test_comparable_publications_listed(self):
        comparables = self.consensus.get('comparable_publications_with_financial_ties', [])
        self.assertGreaterEqual(len(comparables), 3,
                                "At least 3 comparable financially-tied publications must be listed")

    def test_cross_references_include_financial_incentive_mechanism(self):
        refs = self.mechanism.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        self.assertIn(35, ref_ids,
                      "Must cross-reference mechanism #35 (Advance/Condé Nast financial incentive)")

    def test_cross_references_include_parallel_cultural_consensus(self):
        refs = self.mechanism.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        self.assertIn(296, ref_ids,
                      "Must cross-reference mechanism #296 (Rabbit Hole cultural consensus)")


if __name__ == '__main__':
    unittest.main()
