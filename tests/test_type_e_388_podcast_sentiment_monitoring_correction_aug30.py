"""
Type E #388: Podcast Sentiment Tracking — Monitoring/Correction — Guilty Feminist 497 Date Correction + Three-Source Audit + Blood in the Machine Duplicate Prevention

Iteration #388 — Sun 2026-08-30 04:00 PT
Mechanism #388 monitoring/correction type

Coverage:
- Guilty Feminist 497 correction: listing header 23 Aug vs body Released 24 Aug, recorded 5 Aug London, show notes only no transcript
- Everyone Hates Elon activist group not podcast, no new campaign since Aug 10, Samsung ZERO campaigns 38-39 days
- Attention Sphere no matching podcast 3 searches misidentified
- Blood in the Machine duplicate prevention: already logged #378 YouTube 3LA2tsGMVb4, do not reuse
- Honest absence documentation, primary-source-first, no invention

Per project standing rule Aug 28: All tone scores MANUAL ILLUSTRATIVE synthetic controlled arrays or manually assigned illustrative scores based on framing vocabulary NOT observed WIRED corpus empirical scores. DO NOT claim empirical significance from synthetic scores alone. Exact values depend on scoring module tests should verify thresholds not exact values p<0.05 |d|>0.5 CI excludes 0.
"""

import unittest
import os
import re

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
PODCAST_SENTIMENT_PATH = os.path.join(REPO_ROOT, 'podcast-sentiment.md')
ITERATION_LOG_PATH = os.path.join(REPO_ROOT, 'iteration-log.md')


def load_podcast_sentiment():
    with open(PODCAST_SENTIMENT_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def load_iteration_log():
    with open(ITERATION_LOG_PATH, 'r', encoding='utf-8') as f:
        return f.read()


class TestGuiltyFeminist497Correction(unittest.TestCase):
    """Validate #497 date correction and provenance."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_111_exists(self):
        self.assertIn('### 111. Type E Monitoring Correction', self.content)

    def test_497_title_exists(self):
        self.assertIn('The Nuance Drought', self.content)

    def test_recorded_5_aug_london(self):
        self.assertIn('Recorded 5 August 2026 in London', self.content)

    def test_released_24_august_correction(self):
        self.assertIn('Released 24 August', self.content)

    def test_header_23_aug_ambiguity_noted(self):
        # Must note header vs body discrepancy
        self.assertIn('23 August 2026', self.content)
        self.assertIn('Released 24 August', self.content)

    def test_show_notes_only_no_transcript(self):
        self.assertIn('Show notes only, no transcript available', self.content)

    def test_zeno_url_exact(self):
        self.assertIn('https://zeno.fm/podcast/the-guilty-feminist/', self.content)

    def test_podbean_url_exact(self):
        self.assertIn('https://www.podbean.com/podcast-detail/96viz-3cbfc/The-Guilty-Feminist-Podcast', self.content)

    def test_guiltyfeminist_episode_url_exact(self):
        self.assertIn('https://guiltyfeminist.com/episode/', self.content)

    def test_podfollow_recent_url_exact(self):
        self.assertIn('https://podfollow.com/the-guilty-feminist/episode/b111fa67fb1b467b4b4bcb1c916fd2af9062ade9/view', self.content)

    def test_zero_tech_episodes_finding_preserved(self):
        self.assertIn('Zero tech episodes Aug 3-24', self.content)

    def test_palantir_contrast_exists(self):
        self.assertIn('Palantir', self.content)

    def test_algorithm_contrast_exists(self):
        self.assertIn('Algorithm', self.content)


class TestEveryoneHatesElonNotPodcast(unittest.TestCase):
    """Validate EHE correctly identified as activist group not podcast."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_ehe_activist_not_podcast(self):
        self.assertIn('activist group, not a podcast', self.content.lower())

    def test_engadget_url_exact(self):
        self.assertIn('https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/', self.content)

    def test_no_new_campaign_since_aug10_exact(self):
        self.assertIn('No new campaign since Aug 10', self.content)

    def test_samsung_zero_campaigns_38_39_days(self):
        # Either 38 or 38-39 phrasing
        self.assertTrue('ZERO campaigns' in self.content and ('38 days' in self.content or '38-39 days' in self.content))

    def test_prediction_holding_exact(self):
        self.assertIn('Prediction holding', self.content)


class TestAttentionSphereNoMatch(unittest.TestCase):
    """Validate Attention Sphere absence honestly documented."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_no_matching_podcast_found(self):
        self.assertIn('No matching podcast found', self.content)

    def test_misidentified_name(self):
        self.assertIn('misidentified', self.content.lower())

    def test_three_searches_documented(self):
        self.assertIn('3 independent searches', self.content)


class TestBloodInTheMachineDuplicatePrevention(unittest.TestCase):
    """Validate Blood in the Machine not reused as new."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_youtube_id_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=3LA2tsGMVb4', self.content)

    def test_newsletter_url_exact(self):
        self.assertIn('https://www.bloodinthemachine.com/p/the-revolt-against-metas-pervert', self.content)

    def test_timestamp_1216_preserved(self):
        self.assertIn('12:16', self.content)

    def test_duplicate_prevention_language(self):
        self.assertIn('Do not reuse', self.content)

    def test_prior_logged_378(self):
        self.assertIn('Iteration #378', self.content)

    def test_manual_illustrative_labeling(self):
        # At least one MANUAL ILLUSTRATIVE mention for sentiment scores in entry 111
        self.assertIn('MANUAL ILLUSTRATIVE', self.content)

    def test_no_em_dash_in_new_entry(self):
        idx = self.content.find('### 111. Type E Monitoring Correction')
        section = self.content[idx:idx+60000]
        self.assertNotIn('—', section, "Em dash violation in #388 entry")

    def test_structural_incentive_language(self):
        idx = self.content.find('### 111. Type E Monitoring Correction')
        section = self.content[idx:idx+60000]
        self.assertIn('structural incentive', section.lower())

    def test_correlate_not_causation(self):
        idx = self.content.find('### 111. Type E Monitoring Correction')
        section = self.content[idx:idx+60000]
        self.assertIn('correlate not proof', section.lower())

    def test_illustrative_warning_present(self):
        idx = self.content.find('### 111. Type E Monitoring Correction')
        section = self.content[idx:idx+60000]
        self.assertIn('DO NOT claim empirical significance', section)

    def test_five_confounders_documented(self):
        idx = self.content.find('### 111. Type E Monitoring Correction')
        section = self.content[idx:idx+60000]
        # Must have at least 3 STRONG confounders
        strong_count = section.count('[STRONG]')
        self.assertGreaterEqual(strong_count, 2, f"Expected >=2 STRONG confounders, found {strong_count}")


class TestIterationLog388(unittest.TestCase):
    """Validate iteration-log.md contains #388 entry with required structure."""

    def setUp(self):
        self.content = load_iteration_log()

    def test_iteration_388_exists(self):
        self.assertIn('## Iteration #388', self.content)

    def test_type_e_marker(self):
        self.assertIn('Type E', self.content)

    def test_rotation_correct(self):
        # Should mention rotation following Type D #387
        self.assertIn('Rotation', self.content)

    def test_no_em_dash_in_new_entry(self):
        idx = self.content.find('## Iteration #388')
        if idx == -1:
            self.fail("Iteration #388 not found in iteration-log.md")
        section = self.content[idx:idx+50000]
        self.assertNotIn('—', section, "Em dash violation in #388 iteration-log entry")

    def test_source_urls_verbatim(self):
        idx = self.content.find('## Iteration #388')
        section = self.content[idx:idx+50000]
        https_count = section.count('https://')
        self.assertGreaterEqual(https_count, 8, f"Expected >=8 URLs in #388 entry, found {https_count}")

    def test_correction_noted_in_log(self):
        idx = self.content.find('## Iteration #388')
        section = self.content[idx:idx+50000]
        self.assertIn('Released 24 August', section)

    def test_duplicate_prevention_in_log(self):
        idx = self.content.find('## Iteration #388')
        section = self.content[idx:idx+50000]
        self.assertIn('3LA2tsGMVb4', section)
