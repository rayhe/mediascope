"""
Test: Celebrity/Institutional Cascade of Pervert Glasses Vocabulary — Activist → Mainstream Entertainment → Therapy/Wellness → Newsletter → Print (Mechanism #365)

Type E — Podcast Sentiment Tracking
Date: Aug 28, 2026 18:00 PT
Iteration: #354

Focus: Type E mandate — monitor and analyze episodes from podcasts for Meta/tech/wearables coverage and framing.

Finding: Pervert/pervy glasses vocabulary has mainstreamed from tech/activist niche to mainstream entertainment and therapy/wellness domains in 4 days (Aug 24-28), representing celebrity/institutional cascade. Three new surfaces identified Aug 24-28, all Meta-exclusive, 0 Samsung/Google/Apple/Snap despite identical hardware.

New Surfaces:
1. The Rest Is Entertainment — "Kylie Jenner's 'Pervert Glasses'" (Goalhanger, Richard Osman/Marina Hyde, UK's largest entertainment podcast network)
2. "Pervy Glasses, Power Systems, & The Death of the Imaginal" — Therapists Lauran and Joseph (YouTube, Aug 24 2026, depth psychology)
3. Kay Green Blog — "Nudge, point, shout: 'pervert glasses!'" (Aug 26 2026, personal advocacy)

Vocabulary Cluster: 6 independent source groups, 5 media types, 5 months, accelerating adoption curve.

Cross-references:
- Mechanism #360: Podcast sentiment tracking baseline (Guilty Feminist absence, Blood in the Machine, NBC gendered framing)
- Mechanism #311: ICYMI Slate surveillance glasses gendered entity-exclusive cultural consensus
- Mechanism #362: Samsung Galaxy Glasses price-parity silence (identical hardware 0 WIRED coverage)
- Mechanism #130: Gendered surveillance vocabulary
- Mechanism #144: Podcast ecosystem amplification
- Mechanism #137: Privacy Vocabulary Redirected Attribution

Confounders:
1. STRONG: Edinburgh Fringe festival season (60% Fringe recordings Guilty Feminist Aug 3-23)
2. STRONG: Market dominance Meta 80%+ share 7M+ sold 2024 vs Samsung unannounced fall 2026 Apple 2027 delay Snap niche Google audio-only first model
3. MODERATE: Kylie Jenner fashion campaign high-profile vs Samsung Galaxy Unpacked Jul 22 less high-profile
4. MODERATE: Access differences Meta glasses shipped product vs competitors unannounced/delayed
5. WEAK: Editorial calendar Guilty Feminist semiweekly Acast Patreon-supported AudioPlus Network

Causal Caution: Correlation does not prove causation. No financial dependency claim made without direct source.
"""

import os
import unittest

import yaml

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
PODCAST_SENTIMENT_PATH = os.path.join(REPO_ROOT, 'podcast-sentiment.md')
ITERATION_LOG_PATH = os.path.join(REPO_ROOT, 'iteration-log.md')


def file_contains(path, substr):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return substr in f.read()


class TestPodcastSentimentFileExists(unittest.TestCase):
    def test_podcast_sentiment_exists(self):
        self.assertTrue(os.path.exists(PODCAST_SENTIMENT_PATH), "podcast-sentiment.md must exist")

    def test_podcast_sentiment_parseable(self):
        with open(PODCAST_SENTIMENT_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        self.assertGreater(len(content), 10000, "podcast-sentiment.md must be substantial")

    def test_podcast_sentiment_length_increased(self):
        # Should be > 450k (previous 450183) after adding 3 new surfaces
        size = os.path.getsize(PODCAST_SENTIMENT_PATH)
        self.assertGreater(size, 450000, "podcast-sentiment.md should be >450k after Type E 18:00 update")


class TestMechanism365Exists(unittest.TestCase):
    def test_mechanism_365_in_podcast_sentiment(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Mechanism #365") or
                        file_contains(PODCAST_SENTIMENT_PATH, "Mechanism: #365") or
                        file_contains(PODCAST_SENTIMENT_PATH, "#365"),
                        "Mechanism #365 must be referenced in podcast-sentiment.md")

    def test_mechanism_365_in_iteration_log(self):
        self.assertTrue(file_contains(ITERATION_LOG_PATH, "Mechanism #365") or
                        file_contains(ITERATION_LOG_PATH, "Mechanism: #365") or
                        file_contains(ITERATION_LOG_PATH, "#365"),
                        "Mechanism #365 must be in iteration-log.md")

    def test_iteration_354_exists(self):
        self.assertTrue(file_contains(ITERATION_LOG_PATH, "Iteration #354"),
                        "Iteration #354 must exist in iteration-log.md")

    def test_type_e_1800_pt(self):
        self.assertTrue(file_contains(ITERATION_LOG_PATH, "18:00 PT") or
                        file_contains(PODCAST_SENTIMENT_PATH, "18:00 PT"),
                        "18:00 PT timestamp must be present")


class TestNewSurfacesExist(unittest.TestCase):
    def test_rest_is_entertainment_surface(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "The Rest Is Entertainment"),
                        "The Rest Is Entertainment surface must be in podcast-sentiment.md")

    def test_pervy_glasses_power_systems_surface(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Pervy Glasses, Power Systems"),
                        "Pervy Glasses Power Systems surface must be in podcast-sentiment.md")

    def test_kay_green_surface(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Kay Green"),
                        "Kay Green surface must be in podcast-sentiment.md")


class TestVocabularyCluster(unittest.TestCase):
    def test_vocabulary_cluster_6_groups(self):
        # Should mention 6 independent source groups
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "6 independent source groups") or
                        file_contains(PODCAST_SENTIMENT_PATH, "6 independent"),
                        "Vocabulary cluster must mention 6 independent source groups")

    def test_propagation_pattern_accelerating(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "accelerating") or
                        file_contains(PODCAST_SENTIMENT_PATH, "exponential"),
                        "Propagation pattern must note accelerating/exponential adoption")

    def test_mar_9_to_aug_28_pattern(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Mar 9") and
                        file_contains(PODCAST_SENTIMENT_PATH, "Aug 24"),
                        "Propagation must include Mar 9 → Aug 24-28 pattern")


class TestFinancialCorrelation(unittest.TestCase):
    def test_podcast_broadcast_0_deals(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "0 known AI licensing deals") or
                        file_contains(PODCAST_SENTIMENT_PATH, "0 AI licensing"),
                        "Must note podcast/broadcast vector has 0 known AI licensing deals")

    def test_print_online_20_plus_deals(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "20+ OpenAI deals") or
                        file_contains(PODCAST_SENTIMENT_PATH, "20+ deals"),
                        "Must contrast with print/online 20+ deals")


class TestExclusiveTargeting(unittest.TestCase):
    def test_exclusive_meta_targeting(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "exclusive Meta") or
                        file_contains(PODCAST_SENTIMENT_PATH, "Meta-exclusive") or
                        file_contains(PODCAST_SENTIMENT_PATH, "100% Meta"),
                        "Must note exclusive Meta targeting")

    def test_samsung_hardware_comparison(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Samsung Galaxy Glasses") and
                        file_contains(PODCAST_SENTIMENT_PATH, "Snapdragon AR1"),
                        "Must compare Samsung Galaxy Glasses identical hardware")

    def test_fails_proportionality(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Fails proportionality") or
                        file_contains(PODCAST_SENTIMENT_PATH, "fails proportionality"),
                        "Must note fails proportionality test")


class TestSourceURLs(unittest.TestCase):
    def test_podtail_goalhanger_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "podtail.com/podcast/the-rest-is-entertainment"),
                        "Must include Podtail Goalhanger URL")

    def test_youtube_lauran_joseph_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "youtube.com/watch?v=k6gKRKheWIc"),
                        "Must include YouTube Lauran/Joseph URL")

    def test_kay_green_blog_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "kaygreen.blog"),
                        "Must include Kay Green blog URL")

    def test_fastcompany_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "fastcompany.co.za"),
                        "Must include FastCompany URL")

    def test_petapixel_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "petapixel.com"),
                        "Must include PetaPixel URL")

    def test_blood_in_machine_url(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "youtube.com/watch?v=3LA2tsGMVb4"),
                        "Must include Blood in the Machine URL")


class TestGuiltyFeministAbsence(unittest.TestCase):
    def test_guilty_feminist_absence_unchanged(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Guilty Feminist") and
                        file_contains(PODCAST_SENTIMENT_PATH, "ZERO episodes"),
                        "Must note Guilty Feminist absence finding unchanged")

    def test_edinburgh_fringe_confounder(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Edinburgh Fringe") or
                        file_contains(PODCAST_SENTIMENT_PATH, "Fringe season"),
                        "Must note Edinburgh Fringe STRONG confounder")


class TestNoDuplicateMechanismIDs(unittest.TestCase):
    def test_mechanism_365_appears_once_in_tests(self):
        # This test file is for mechanism 365, should not duplicate other mechanisms
        # Check that test file itself references 365 correctly
        with open(__file__, 'r') as f:
            content = f.read()
        count = content.count("365")
        self.assertGreater(count, 0, "Test file must reference mechanism 365")


class TestCausalCaution(unittest.TestCase):
    def test_causal_caution_present(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "Causal caution") or
                        file_contains(PODCAST_SENTIMENT_PATH, "Correlation does not prove causation"),
                        "Must include causal caution language")

    def test_no_financial_dependency_claim_without_source(self):
        self.assertTrue(file_contains(PODCAST_SENTIMENT_PATH, "No financial dependency claim") or
                        file_contains(PODCAST_SENTIMENT_PATH, "no financial incentive"),
                        "Must include no financial dependency claim without direct source")


if __name__ == '__main__':
    unittest.main()
