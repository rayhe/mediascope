"""
Type E #383: Podcast Sentiment Tracking — Meta Second Fix 6-Source Aggregate + HateAid ZIT Criminal Complaint + Guilty Feminist August Silence Third Verification + EHE Prediction Holding 38 Days

Iteration #383 — Sat 2026-08-29 23:00 PT
Mechanisms #383-#385

Coverage:
- Meta second LED fix Aug 27-29 6-source aggregate (GadgetReview, Tech Insider, Startup Fortune, RoadToVR, abit.ee, Zot News)
- EHE prediction holding 38 days no new campaign since Aug 10, Samsung ZERO campaigns
- Guilty Feminist Aug 3-24 full slate third independent verification zero tech episodes
- HateAid ZIT criminal complaint Aug 12 feminist legal parallel to EHE
- Cross-podcast August 2026 pattern 7 surfaces, cultural consensus vector not financial incentive vector
- Hardware capability inversion extension 0.94 (higher than #359 0.92 due to continuous monitoring)
- Every fact needs source URL verbatim, no em dash, structural incentive only not proof of editorial influence

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


class TestMetaSecondFixAggregate(unittest.TestCase):
    """Validate Meta second LED fix 6-source aggregate entry 107."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_107_exists(self):
        self.assertIn('### 107. Meta Second LED Fix 6-Source Aggregate', self.content)

    def test_gadgetreview_url_exact(self):
        self.assertIn('https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered', self.content)

    def test_techinsider_url_exact(self):
        self.assertIn('https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/', self.content)

    def test_startupfortune_url_exact(self):
        self.assertIn('https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/', self.content)

    def test_roadtovr_url_exact(self):
        self.assertIn('https://roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/', self.content)

    def test_abitee_url_exact(self):
        self.assertIn('https://abit.ee/en/smart-glasses/meta-smart-glasses-privacy-ray-ban-meta-recording-indicator-wearables-en', self.content)

    def test_zot_url_exact(self):
        self.assertIn('https://zot.news/article/meta-fixes-smart-glasses-recording-loophole-launches-marketing-campaign-to-shed-pervert-glasses-image-mtc6qzhl', self.content)

    def test_himel_quote_exact(self):
        self.assertIn('camera will now stop working if the light is covered during a recording', self.content)

    def test_inversion_score_094(self):
        self.assertIn('0.94', self.content)

    def test_manual_illustrative_labeling(self):
        # At least one MANUAL ILLUSTRATIVE mention for sentiment scores in entry 107
        self.assertIn('MANUAL ILLUSTRATIVE', self.content)


class TestEveryoneHatesElonPredictionHolding(unittest.TestCase):
    """Validate EHE prediction holding 38 days entry 108."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_108_exists(self):
        self.assertIn('### 108. Everyone Hates Elon - Prediction Holding', self.content)

    def test_engadget_url_exact(self):
        self.assertIn('https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/', self.content)

    def test_singulism_url_exact(self):
        self.assertIn('https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/', self.content)

    def test_petapixel_url_exact(self):
        self.assertIn('https://petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/', self.content)

    def test_times_url_exact(self):
        self.assertIn('https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5', self.content)

    def test_latestly_url_exact(self):
        self.assertIn('https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html', self.content)

    def test_hyperallergic_url_exact(self):
        self.assertIn('http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/', self.content)

    def test_no_new_campaign_since_aug10_exact(self):
        self.assertIn('No new campaign since Aug 10', self.content)

    def test_samsung_zero_campaigns_38_days_exact(self):
        self.assertIn('ZERO campaigns in 38 days', self.content)

    def test_prediction_holding_exact(self):
        self.assertIn('Prediction holding', self.content)


class TestGuiltyFeministAugustSlateThirdVerification(unittest.TestCase):
    """Validate Guilty Feminist Aug 3-24 third independent verification entry 109."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_109_exists(self):
        self.assertIn('### 109. The Guilty Feminist - August 2026 Full Slate Audit - Third Independent Verification', self.content)

    def test_podfollow_497_url_exact(self):
        self.assertIn('https://podfollow.com/the-guilty-feminist/episode/38f82f0a0ec7abb78f61037546a56ef9f8908e48/view', self.content)

    def test_podfollow_494_url_exact(self):
        self.assertIn('https://podfollow.com/the-guilty-feminist/episode/fc891a87ad9cd949dad23341e1ff15ab606dc11e/view', self.content)

    def test_guiltyfeminist_list_url_exact(self):
        self.assertIn('https://guiltyfeminist.com/list-of-episodes/', self.content)

    def test_zero_tech_episodes_finding(self):
        self.assertIn('Zero tech episodes Aug 3-24', self.content)

    def test_palantir_contrast_exists(self):
        self.assertIn('Palantir', self.content)

    def test_algorithm_contrast_exists(self):
        self.assertIn('Algorithm', self.content)


class TestHateAidCriminalComplaint(unittest.TestCase):
    """Validate HateAid ZIT criminal complaint entry 110."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_110_exists(self):
        self.assertIn('### 110. HateAid Criminal Complaint Aug 12 2026', self.content)

    def test_reuters_url_exact(self):
        self.assertIn('https://www.reuters.com/legal/government/german-advocacy-group-lodges-criminal-complaint-over-meta-ai-glasses-2026-08-12/', self.content)

    def test_betanews_url_exact(self):
        self.assertIn('https://betanews.com/article/meta-criminal-complaint-germany-smart-glasses/', self.content)

    def test_archyde_url_exact(self):
        self.assertIn('https://www.archyde.com/german-advocacy-group-files-criminal-complaint-over-meta-ai-glasses/', self.content)

    def test_no_place_to_escape_quote_exact(self):
        self.assertIn("There's no place to escape from smart glasses", self.content)

    def test_tdddg_law_mentioned(self):
        self.assertIn('TDDDG', self.content)

    def test_zit_mentioned(self):
        self.assertIn('ZIT', self.content)

    def test_parallel_feminist_frames(self):
        # Must document two parallel feminist frames never intersect
        self.assertIn('Two parallel feminist frames', self.content)

    def test_disproportionately_targets_women(self):
        self.assertIn('disproportionately', self.content.lower())


class TestIterationLog383(unittest.TestCase):
    """Validate iteration-log.md contains #383 entry with required structure."""

    def setUp(self):
        self.content = load_iteration_log()

    def test_iteration_383_exists(self):
        self.assertIn('## Iteration #383', self.content)

    def test_type_e_marker(self):
        self.assertIn('Type E', self.content)

    def test_rotation_correct(self):
        self.assertIn('Rotation correct', self.content)

    def test_no_em_dash_in_new_entry(self):
        # Find #383 section and ensure no em dash violations (project style rule)
        idx = self.content.find('## Iteration #383')
        section = self.content[idx:idx+50000]
        self.assertNotIn('—', section, "Em dash violation in #383 entry")

    def test_structural_incentive_language(self):
        # #383 now at top due to newest-first ordering; use first occurrence
        idx = self.content.find('## Iteration #383')
        section = self.content[idx:idx+50000]
        # Must use structural incentive only not proof of editorial influence
        self.assertIn('structural incentive', section.lower())

    def test_source_urls_verbatim(self):
        idx = self.content.find('## Iteration #383')
        section = self.content[idx:idx+50000]
        # At least 6 second fix URLs + 6 EHE + 3 Guilty + 3 HateAid = 18 URLs, check for https count
        https_count = section.count('https://')
        self.assertGreaterEqual(https_count, 15, f"Expected >=15 URLs in #383 entry, found {https_count}")

