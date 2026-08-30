"""
Type E #398: Podcast Sentiment Tracking — Duplicate Prevention + Fifth Verification — AI2Day Meta Fix Duplicate + Guilty Feminist 497 Fifth Verification + Attention Sphere Fifth + EHE 20-Day Hold + Fortune Re-Validation

Iteration #398 — Sun 2026-08-30 14:00 PT
Mechanism #398 monitoring/correction type

Coverage:
- AI2Day Daily Brief Aug 29 2026 Meta fixes Ray-Ban smart glasses recording YouTube 0qiKNKRetCw already logged #378 entry #41, duplicate prevention, 7 supporting print sources same fix Aug 27-28 2026 Threads Alex Himel VP AR
- Guilty Feminist 497 correction: Recorded 5 August 2026 in London Released 24 August per guiltyfeminist.com/episode/ body lines L2-L8, listing header 23 Aug vs body 24 Aug discrepancy noted #388 #393 #398, show notes only no transcript, fifth verification no new episode Aug 25-30
- Everyone Hates Elon activist group not podcast, no new campaign since Aug 10 20 days Aug 10-30, Samsung ZERO campaigns 40 days Jul 22-Aug 30, prediction holding
- Attention Sphere no matching podcast 5 independent searches misidentified
- Fortune AI Weekly re-validation no new episode Aug 29-30 same episode TVdoEPg42pQ double Meta framing vs Fortune Daily +3 OpenAI revolutionize same network opposite valence
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


class TestAI2DayDuplicatePrevention(unittest.TestCase):
    """Validate AI2Day Aug 29 2026 not reused as new discovery."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_117_exists(self):
        self.assertIn('### 117. AI2Day Daily Brief', self.content)

    def test_youtube_id_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=0qiKNKRetCw', self.content)

    def test_duplicate_prevention_language(self):
        self.assertIn('DUPLICATE PREVENTION', self.content)

    def test_prior_logged_378(self):
        self.assertIn('Iteration #378', self.content)

    def test_entry_41_reference(self):
        self.assertIn('entry #41', self.content.lower() + self.content)  # case-insensitive check for 41

    def test_do_not_reuse_phrase(self):
        self.assertIn('Do not reuse', self.content)

    def test_gadgetreview_url_exact(self):
        self.assertIn('https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered', self.content)

    def test_tech_insider_url_exact(self):
        self.assertIn('https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/', self.content)

    def test_aiweekly_url_exact(self):
        self.assertIn('https://aiweekly.co/alerts/meta-patches-smart-glasses-to-halt-recording-if-led-covered', self.content)

    def test_9to5google_url_exact(self):
        self.assertIn('https://9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/', self.content)

    def test_startupfortune_second_loophole_url_exact(self):
        self.assertIn('https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/', self.content)

    def test_letsdatascience_url_exact(self):
        self.assertIn('https://letsdatascience.com/news/meta-updates-smart-glasses-to-close-recording-loophole-8401db11', self.content)

    def test_alex_himel_quote_present(self):
        self.assertIn('The camera will now stop working if the light is covered', self.content)

    def test_manual_illustrative_labeling(self):
        idx = self.content.find('### 117. AI2Day Daily Brief')
        section = self.content[idx:idx+30000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 117. AI2Day Daily Brief')
        section = self.content[idx:idx+30000]
        self.assertNotIn('—', section, "Em dash violation in #398 entry 117")


class TestGuiltyFeministFifthVerification(unittest.TestCase):
    """Validate Guilty Feminist 497 fifth verification Aug 30 14:00 PT."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_118_exists(self):
        self.assertIn('### 118. The Guilty Feminist', self.content)

    def test_fifth_verification_marker(self):
        self.assertIn('Fifth Independent Verification', self.content)

    def test_recorded_5_aug_london(self):
        self.assertIn('Recorded 5 August 2026 in London', self.content)

    def test_released_24_august(self):
        self.assertIn('Released 24 August', self.content)

    def test_header_23_aug_noted(self):
        self.assertIn('23 Aug', self.content)

    def test_guiltyfeminist_episode_url_exact(self):
        self.assertIn('https://guiltyfeminist.com/episode/', self.content)

    def test_zeno_url_exact(self):
        self.assertIn('https://zeno.fm/podcast/the-guilty-feminist/', self.content)

    def test_no_new_episode_aug_25_30(self):
        self.assertIn('no new episode aug 25-30', self.content.lower())

    def test_zero_meta_ai_wearables_finding(self):
        idx = self.content.find('### 118. The Guilty Feminist')
        section = self.content[idx:idx+30000]
        self.assertIn('Zero episodes', section)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 118. The Guilty Feminist')
        section = self.content[idx:idx+30000]
        self.assertNotIn('—', section)


class TestAttentionSphereFifthVerification(unittest.TestCase):
    """Validate Attention Sphere fifth verification."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_119_exists(self):
        self.assertIn('### 119. Attention Sphere', self.content)

    def test_fifth_verification_marker(self):
        idx = self.content.find('### 119. Attention Sphere')
        section = self.content[idx:idx+20000]
        self.assertIn('Fifth', section)

    def test_no_matching_podcast_found(self):
        self.assertIn('No matching podcast found', self.content)

    def test_misidentified_name(self):
        self.assertIn('misidentified', self.content.lower())

    def test_five_searches_documented(self):
        self.assertIn('5 independent searches', self.content)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 119. Attention Sphere')
        section = self.content[idx:idx+20000]
        self.assertNotIn('—', section)


class TestEveryoneHatesElon20DayHold(unittest.TestCase):
    """Validate EHE 20-day hold Aug 10-30."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_120_exists(self):
        self.assertIn('### 120. Everyone Hates Elon', self.content)

    def test_no_new_campaign_since_aug10(self):
        self.assertIn('No New Campaign Since Aug 10', self.content)

    def test_20_days_marker(self):
        idx = self.content.find('### 120. Everyone Hates Elon')
        section = self.content[idx:idx+20000]
        self.assertTrue('20 days' in section or '20 Days' in section)

    def test_samsung_zero_40_days(self):
        idx = self.content.find('### 120. Everyone Hates Elon')
        section = self.content[idx:idx+20000]
        self.assertTrue('ZERO' in section and ('40 days' in section or '39' in section or '40' in section))

    def test_engadget_url_exact(self):
        self.assertIn('https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/', self.content)

    def test_manual_illustrative_present(self):
        idx = self.content.find('### 120. Everyone Hates Elon')
        section = self.content[idx:idx+20000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 120. Everyone Hates Elon')
        section = self.content[idx:idx+20000]
        self.assertNotIn('—', section)


class TestFortuneReValidation(unittest.TestCase):
    """Validate Fortune AI Weekly re-validation no new episode."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_121_exists(self):
        self.assertIn('### 121. Fortune AI Weekly', self.content)

    def test_no_new_episode_marker(self):
        idx = self.content.find('### 121. Fortune AI Weekly')
        section = self.content[idx:idx+30000]
        self.assertIn('No New Episode', section)

    def test_youtube_id_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=TVdoEPg42pQ', self.content)

    def test_double_meta_framing_noted(self):
        idx = self.content.find('### 121. Fortune AI Weekly')
        section = self.content[idx:idx+30000]
        self.assertIn('Double Meta', section)

    def test_fortune_daily_cross_ref(self):
        idx = self.content.find('### 121. Fortune AI Weekly')
        section = self.content[idx:idx+30000]
        self.assertIn('Fortune Daily', section)

    def test_manual_illustrative_present(self):
        idx = self.content.find('### 121. Fortune AI Weekly')
        section = self.content[idx:idx+30000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 121. Fortune AI Weekly')
        section = self.content[idx:idx+30000]
        self.assertNotIn('—', section)


class TestIterationLog398(unittest.TestCase):
    """Validate iteration-log.md contains #398 entry with required structure."""

    def setUp(self):
        self.content = load_iteration_log()

    def test_iteration_398_exists(self):
        self.assertIn('## Iteration #398', self.content)

    def test_type_e_marker(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+50000]
        self.assertIn('Type E', section)

    def test_rotation_correct(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+50000]
        self.assertIn('Rotation', section)
        self.assertIn('#397 D', section)
        self.assertIn('#398 E', section)

    def test_newest_first(self):
        # #398 should appear before #397
        idx_398 = self.content.find('## Iteration #398')
        idx_397 = self.content.find('## Iteration #397')
        self.assertLess(idx_398, idx_397, "#398 must be prepended newest-first before #397")

    def test_no_em_dash_in_new_entry(self):
        idx = self.content.find('## Iteration #398')
        if idx == -1:
            self.fail("Iteration #398 not found in iteration-log.md")
        section = self.content[idx:idx+80000]
        self.assertNotIn('—', section, "Em dash violation in #398 iteration-log entry")

    def test_source_urls_verbatim(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        https_count = section.count('https://')
        self.assertGreaterEqual(https_count, 10, f"Expected >=10 URLs in #398 entry, found {https_count}")

    def test_duplicate_prevention_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('0qiKNKRetCw', section)

    def test_fifth_verification_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('Fifth Verification', section)

    def test_correction_noted_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('Recorded 5 August 2026 in London', section)
        self.assertIn('Released 24 August', section)

    def test_manual_illustrative_labeling_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_illustrative_warning_present_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('DO NOT claim empirical significance', section)

    def test_corroborate_not_proof_in_log(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        # Must contain cautious language correlate not proof
        self.assertIn('correlate not proof', section.lower())

    def test_structural_incentive_language(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        self.assertIn('structural incentive', section.lower())

    def test_nine_confounders_documented(self):
        idx = self.content.find('## Iteration #398')
        section = self.content[idx:idx+80000]
        strong_count = section.count('[STRONG]')
        moderate_count = section.count('[MODERATE]')
        weak_count = section.count('[WEAK]')
        self.assertGreaterEqual(strong_count, 3, f"Expected >=3 STRONG confounders, found {strong_count}")
        self.assertGreaterEqual(moderate_count, 3, f"Expected >=3 MODERATE confounders, found {moderate_count}")
        self.assertGreaterEqual(weak_count, 1, f"Expected >=1 WEAK confounders, found {weak_count}")
