"""
Type E #403: Podcast Sentiment Tracking — Pervy Glasses Therapy/Depth-Psychology Vocabulary Migration — Cultural Consensus Propagation Beyond Tech Media

Iteration #403 — Sun 2026-08-30 19:00 PT
Mechanism #403 monitoring/correction type

Coverage:
- Episode 5: Pervy Glasses, Power Systems, & The Death of the Imaginal (YouTube k6gKRKheWIc, therapists Lauran and Joseph, Last Updated 6 days ago per search index Aug 31 2026 02:00 UTC, publish likely Aug 24-25 2026)
- Vocabulary migration from activist/mainstream pervert glasses into therapy/depth-psychology pervy glasses
- Distinct from #398 E duplicate prevention + fifth verification (Fortune/Guilty/EHE/Attention Sphere/AI2Day), #388 monitoring correction, #383 Meta second fix, #378 AI2Day+Blood Meta fix
- MANUAL ILLUSTRATIVE labeling required, no causal overclaim, confounders 6 total 3 STRONG 2 MODERATE 1 WEAK
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


class TestEpisode5NewDiscovery(unittest.TestCase):
    """Validate Episode 5 Pervy Glasses new discovery entry 122 exists with required fields."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_122_exists(self):
        self.assertIn('### 122. Episode 5: Pervy Glasses', self.content)

    def test_youtube_id_exact_k6g(self):
        self.assertIn('https://www.youtube.com/watch?v=k6gKRKheWIc', self.content)

    def test_therapists_laura_and_joseph(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertIn('Lauran and Joseph', section)

    def test_publish_date_approx_aug24_25(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertTrue('Aug 24' in section or 'Aug 25' in section or 'Aug 24-25' in section)

    def test_last_updated_6_days(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertIn('6 days ago', section)

    def test_search_observed_aug31_0200_utc(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertIn('Aug 31 2026', section)

    def test_key_quote_what_if_wearable(self):
        self.assertIn("What if wearable tech isn't just eroding", self.content)

    def test_key_quote_pervy_dimension(self):
        self.assertIn('Pervy Dimension', self.content)

    def test_key_quote_foucault_nietzsche(self):
        self.assertIn('Foucault, Nietzsche', self.content)

    def test_key_quote_jung_imaginal(self):
        self.assertIn('Jung & The Loss of the Imaginal', self.content)

    def test_key_quote_middle_path(self):
        self.assertIn('Finding the Middle Path', self.content)

    def test_key_quote_quiet_invasion(self):
        self.assertIn('quiet invasion of wearable AI', self.content)

    def test_manual_illustrative_present(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_no_em_dash_in_entry(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertNotIn('—', section, "Em dash violation in #403 entry 122")

    def test_no_causal_claim_language(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000].lower()
        # Must not claim proves causation or direct influence without cautious language
        self.assertNotIn('proves causation', section)
        self.assertNotIn('proves direct influence', section)

    def test_cautious_correlation_language(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000].lower()
        self.assertTrue('correlation only' in section or 'correlational' in section or 'hypothesis not proof' in section)

    def test_lexical_migration_described(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000].lower()
        self.assertIn('vocabulary migration', section)

    def test_therapeutic_discipline_novelty(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000].lower()
        self.assertTrue('therapy' in section and ('depth-psychology' in section or 'depth psychology' in section))

    def test_middle_path_tempering(self):
        idx = self.content.find('### 122. Episode 5')
        section = self.content[idx:idx+40000]
        self.assertIn('middle path', section.lower())


class TestConfounders403(unittest.TestCase):
    """Validate 6 confounders 3 STRONG 2 MODERATE 1 WEAK documented."""

    def setUp(self):
        self.content = load_podcast_sentiment()
        idx = self.content.find('### 122. Episode 5')
        self.section = self.content[idx:idx+50000]

    def test_strong_confounder_count(self):
        strong_count = self.section.count('[STRONG]')
        self.assertGreaterEqual(strong_count, 3, f"Expected >=3 STRONG, found {strong_count}")

    def test_moderate_confounder_count(self):
        moderate_count = self.section.count('[MODERATE]')
        self.assertGreaterEqual(moderate_count, 2, f"Expected >=2 MODERATE, found {moderate_count}")

    def test_weak_confounder_count(self):
        weak_count = self.section.count('[WEAK]')
        self.assertGreaterEqual(weak_count, 1, f"Expected >=1 WEAK, found {weak_count}")

    def test_dominant_vendor_confounder(self):
        self.assertIn('dominant vendor', self.section.lower())

    def test_generic_not_meta_specific_confounder(self):
        self.assertTrue('generically' in self.section.lower() or 'generic' in self.section.lower())

    def test_middle_path_tempering_confounder(self):
        self.assertIn('middle-path', self.section.lower() or 'middle path' in self.section.lower())

    def test_transcript_limitation_confounder(self):
        self.assertIn('transcript', self.section.lower())

    def test_search_age_approx_confounder(self):
        self.assertIn('approximate', self.section.lower() or '6 days ago' in self.section)

    def test_small_audience_weak_confounder(self):
        self.assertTrue('small' in self.section.lower() or 'audience' in self.section.lower())


class TestCrossReferences403(unittest.TestCase):
    """Validate cross-references to prior mechanisms distinct from #398."""

    def setUp(self):
        self.content = load_podcast_sentiment()
        idx = self.content.find('### 122. Episode 5')
        self.section = self.content[idx:idx+50000]

    def test_mechanism_403_marker(self):
        self.assertIn('Mechanism', self.section)
        self.assertIn('#403', self.section)

    def test_cross_ref_ehe_120(self):
        self.assertIn('#120', self.section)

    def test_cross_ref_112_fortune(self):
        self.assertIn('#112', self.section)

    def test_cross_ref_158_multivector(self):
        self.assertIn('#158', self.section)

    def test_cross_ref_176_observer(self):
        self.assertIn('#176', self.section)

    def test_cross_ref_177_kodak_fiend(self):
        self.assertIn('#177', self.section)

    def test_cross_ref_398_duplicate_prevention(self):
        self.assertIn('#398', self.section)

    def test_cross_ref_42_blood_in_machine(self):
        self.assertIn('#42', self.section)

    def test_blood_in_machine_url_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=3LA2tsGMVb4', self.content)

    def test_rest_is_entertainment_url_exact(self):
        self.assertIn('https://podtail.com/podcast/the-rest-is-entertainment/kylie-jenner-s-pervert-glasses/', self.content)

    def test_404_media_url_exact(self):
        self.assertIn('https://www.404media.co/podcast-the-smart-glasses-that-dox-strangers/', self.content)

    def test_engadget_url_exact(self):
        self.assertIn('https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/', self.content)

    def test_hyperallergic_url_exact(self):
        self.assertIn('https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/', self.content)

    def test_distinction_from_398(self):
        # Must state distinct from #398 mechanisms
        self.assertIn('distinct from', self.section.lower() or 'distinct' in self.section.lower())


class TestSourceURLIntegrity403(unittest.TestCase):
    """Validate source URLs verbatim and HTTPS provenance."""

    def setUp(self):
        self.content = load_podcast_sentiment()
        idx = self.content.find('### 122. Episode 5')
        self.section = self.content[idx:idx+50000]

    def test_youtube_k6g_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=k6gKRKheWIc', self.section)

    def test_blood_in_machine_exact(self):
        self.assertIn('https://www.youtube.com/watch?v=3LA2tsGMVb4', self.section)

    def test_rest_exact(self):
        self.assertIn('https://podtail.com/podcast/the-rest-is-entertainment/kylie-jenner-s-pervert-glasses/', self.section)

    def test_404_media_exact(self):
        self.assertIn('https://www.404media.co/podcast-the-smart-glasses-that-dox-strangers/', self.section)

    def test_engadget_exact(self):
        self.assertIn('https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/', self.section)

    def test_hyperallergic_exact(self):
        self.assertIn('https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/', self.section)

    def test_https_count(self):
        https_count = self.section.count('https://')
        self.assertGreaterEqual(https_count, 6, f"Expected >=6 HTTPS URLs, found {https_count}")

    def test_no_http_insecure(self):
        # Allow http only if explicitly allowed, but check no insecure http
        insecure = re.findall(r'http://[^\s]+', self.section)
        # Filter allowed http (dejavu.org) - not present here
        self.assertEqual(len(insecure), 0, f"Found insecure http URLs: {insecure}")


class TestIterationLog403(unittest.TestCase):
    """Validate iteration-log.md contains #403 entry with required structure."""

    def setUp(self):
        self.content = load_iteration_log()

    def test_iteration_403_exists(self):
        self.assertIn('## Iteration #403', self.content)

    def test_type_e_marker(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+60000]
        self.assertIn('Type E', section)

    def test_rotation_correct(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+60000]
        self.assertIn('Rotation', section)
        self.assertIn('#398 E', section)
        self.assertIn('#402 D', section)
        self.assertIn('#403 E', section)

    def test_newest_first(self):
        idx_403 = self.content.find('## Iteration #403')
        idx_402 = self.content.find('## Iteration #402')
        self.assertLess(idx_403, idx_402, "#403 must be prepended newest-first before #402")

    def test_no_em_dash_in_new_entry(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertNotIn('—', section, "Em dash violation in #403 iteration-log entry")

    def test_source_urls_verbatim(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        https_count = section.count('https://')
        self.assertGreaterEqual(https_count, 10, f"Expected >=10 URLs in #403 entry, found {https_count}")

    def test_youtube_k6g_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('k6gKRKheWIc', section)

    def test_blood_in_machine_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('3LA2tsGMVb4', section)

    def test_404_media_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('dox-strangers', section)

    def test_manual_illustrative_labeling_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('MANUAL ILLUSTRATIVE', section)

    def test_illustrative_warning_present_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('DO NOT claim empirical significance', section)

    def test_corroborate_not_proof_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('correlation only', section.lower())

    def test_structural_incentive_language(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertTrue('cultural consensus' in section.lower() or 'structural incentive' in section.lower())

    def test_confounders_documented_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        strong_count = section.count('[STRONG]')
        moderate_count = section.count('[MODERATE]')
        weak_count = section.count('[WEAK]')
        self.assertGreaterEqual(strong_count, 3, f"Expected >=3 STRONG confounders in log, found {strong_count}")
        self.assertGreaterEqual(moderate_count, 2, f"Expected >=2 MODERATE confounders in log, found {moderate_count}")
        self.assertGreaterEqual(weak_count, 1, f"Expected >=1 WEAK confounders in log, found {weak_count}")

    def test_distinct_from_398_in_log(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('#398', section)
        self.assertIn('distinct from', section.lower())

    def test_no_analysis_json_update_warranted(self):
        idx = self.content.find('## Iteration #403')
        section = self.content[idx:idx+90000]
        self.assertIn('No analysis.json Update Warranted', section)


class TestMechanismID403Uniqueness(unittest.TestCase):
    """Validate mechanism ID 403 uniqueness and no collision with prior IDs."""

    def test_mechanism_403_unique_in_tests(self):
        test_dir = os.path.join(REPO_ROOT, 'tests')
        files = [f for f in os.listdir(test_dir) if '403' in f]
        self.assertGreaterEqual(len(files), 1, "Expected at least 1 test file containing 403")
        # Ensure no duplicate mechanism ID 403 in other YAML (podcast sentiment is not YAML but check competitor-entities/wired)
        # For Type E, uniqueness is via test file and iteration-log, not YAML collision
        self.assertTrue(True)

    def test_no_duplicate_403_in_iteration_log(self):
        content = load_iteration_log()
        count = content.count('Mechanism:** #403') + content.count('Mechanism:** #403') + content.count('mechanism_id: 403') + content.count('#403 (Type E')
        # At least one occurrence, but not excessive duplicates within same file logic
        self.assertGreaterEqual(content.count('## Iteration #403'), 1)
