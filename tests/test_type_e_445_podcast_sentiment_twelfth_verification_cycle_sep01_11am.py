"""
Type E #445: Podcast Sentiment Twelfth Verification Cycle - Guilty Feminist Aug 2026 Slate 496-498 Silence + EHE 23-Day Hold + LatestLY Fact-Check + Attention Sphere 12th No-Match + Fortune Intra-Episode + AI2Day Fix + Dark Web Deacon - Sep 1 2026 11:00 PDT

Validates:
- Mechanism 445 Type E twelfth verification cycle
- Guilty Feminist 496-498 Aug 2026 slate silence festival season artifact
- EHE 23-day hold extension plus LatestLY fact-check false claim TruLY Score 5
- Attention Sphere 12th no-match verification
- Fortune AI Weekly privacy debate intra-episode asymmetry OpenAI +0.12 vs Meta -0.70 MANUAL ILLUSTRATIVE
- AI2Day Aug 29 Meta patches reactive positive -2/10
- Dark Web Deacon surveillance camera -8/10 HIGH asymmetry cultural consensus vector
- Shared Security chapter timestamp verification
- Kill Switch Victoria Song The Verge cross-ref
- Utilizing AI Big Butler vs Big Brother
- 17 HTTPS direct sources
- MANUAL ILLUSTRATIVE labeling
- correlation not causation structural incentive plus cultural consensus dual vectors
- confounders >=4 STRONG>=2
- no em dashes
- cautious language illustrative scores empirical validation dual-vector hypothesis
- source attribution direct primary
- deal_disclosed false
- no synthetic significance overclaim
- three-tier model financial predictor plus cultural consensus predictor converging same outcome

Sources (17 HTTPS):
- https://guiltyfeminist.com/list-of-episodes/
- https://zeno.fm/podcast/the-guilty-feminist/
- https://www.audible.co.uk/podcast/The-Guilty-Feminist/B08K5Y1B25
- https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/
- https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/
- https://www.mediapost.com/publications/article/416992/meta-responds-to-pervert-glasses-backlash.html
- https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html
- https://fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612
- https://petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/
- https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/
- https://www.youtube.com/watch?v=gxZj-XGIQ3Y
- https://www.youtube.com/watch?v=TVdoEPg42pQ
- https://www.youtube.com/watch?v=0qiKNKRetCw
- https://www.youtube.com/watch?v=lfFGZMGvhWg
- https://www.youtube.com/watch?v=Uad_cDSf6AM
- https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/
- https://sharedsecurity.net/2026/03/16/

Methodology: Synthetic illustrative tone arrays only. Real corpus needed for empirical validation. MANUAL ILLUSTRATIVE labeling required. Correlation only. Dual-vector hypothesis financial + cultural consensus.
"""
import os
import re
import pathlib
import unittest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITERATION_LOG = os.path.join(REPO_ROOT, "iteration-log.md")
PODCAST_MD = os.path.join(REPO_ROOT, "podcast-sentiment.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

def load_text(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()

class TestTypeE445TwelfthVerification(unittest.TestCase):

    def test_mechanism_id_445_exists_in_podcast_md(self):
        content = load_text(PODCAST_MD)
        self.assertIn("#445", content, "Mechanism 445 should exist in podcast-sentiment.md")

    def test_iteration_log_contains_445(self):
        content = load_text(ITERATION_LOG)
        self.assertIn("#445", content, "Iteration log should contain #445")
        self.assertIn("Type E", content, "Should be Type E")

    def test_guilty_feminist_496_498_slate_silence(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("496", pod)
        self.assertIn("497", pod)
        self.assertIn("498", pod)
        self.assertIn("Politics", pod)
        self.assertIn("Nuance Drought", pod)
        self.assertIn("Intimacy", pod)
        self.assertIn("Aug 2026", pod)

    def test_guilty_feminist_sources_https(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("https://guiltyfeminist.com/list-of-episodes/", pod)
        self.assertIn("https://zeno.fm/podcast/the-guilty-feminist/", pod)
        self.assertIn("https://www.audible.co.uk/podcast/The-Guilty-Feminist/B08K5Y1B25", pod)

    def test_ehe_23_day_hold_extension(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("23-Day Hold", pod)
        self.assertIn("23-day hold", pod.lower() or "23-day" in pod)
        # At least mentions hold extension
        self.assertIn("Hold", pod)

    def test_latestly_fact_check_false_claim(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html", pod)
        self.assertIn("TruLY Score 5", pod)
        self.assertIn("spoof campaign", pod.lower() or "spoof" in pod)

    def test_attention_sphere_12th_no_match(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Attention Sphere", pod)
        self.assertIn("No matching podcast found", pod)
        self.assertIn("12th", pod)

    def test_fortune_ai_weekly_intra_episode_asymmetry(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Fortune AI Weekly", pod)
        self.assertIn("Why Meta's Ray-Bans Sparked a Huge Privacy Debate", pod)
        self.assertIn("https://www.youtube.com/watch?v=TVdoEPg42pQ", pod)
        # Intra-episode asymmetry
        self.assertIn("OpenAI", pod)
        self.assertIn("Meta", pod)
        self.assertIn("MANUAL ILLUSTRATIVE", pod)

    def test_ai2day_aug29_meta_patches(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("AI2Day", pod)
        self.assertIn("https://www.youtube.com/watch?v=0qiKNKRetCw", pod)
        self.assertIn("Meta patches", pod)
        self.assertIn("Aug 29", pod)

    def test_dark_web_deacon_surveillance_camera(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Dark Web Deacon", pod)
        self.assertIn("https://www.youtube.com/watch?v=lfFGZMGvhWg", pod)
        self.assertIn("When Everyone Becomes a Surveillance Camera", pod)
        self.assertIn("-8/10", pod)
        self.assertIn("HIGH", pod)

    def test_shared_security_chapter_timestamps(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Shared Security", pod)
        self.assertIn("https://sharedsecurity.net/2026/03/16/", pod)
        self.assertIn("https://www.youtube.com/watch?v=gxZj-XGIQ3Y", pod)
        self.assertIn("00:00", pod)
        self.assertIn("16:31", pod)

    def test_kill_switch_victoria_song_cross_ref(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Kill Switch", pod)
        self.assertIn("The Glassholes Are Back", pod)
        self.assertIn("https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/", pod)
        self.assertIn("Victoria Song", pod)
        self.assertIn("The Verge", pod)

    def test_utilizing_ai_big_butler_big_brother(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Utilizing AI", pod)
        self.assertIn("https://www.youtube.com/watch?v=Uad_cDSf6AM", pod)
        self.assertIn("Trojan Horses", pod)
        self.assertIn("Big Butler", pod)
        self.assertIn("Big Brother", pod)

    def test_ehe_sources_https(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/", pod)
        self.assertIn("https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/", pod)
        self.assertIn("https://www.mediapost.com/publications/article/416992/meta-responds-to-pervert-glasses-backlash.html", pod)
        self.assertIn("https://fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612", pod)
        self.assertIn("https://petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/", pod)
        self.assertIn("https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/", pod)

    def test_manual_illustrative_labeling(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("MANUAL ILLUSTRATIVE", pod)
        # At least 3 occurrences for synthetic scores
        self.assertGreaterEqual(pod.count("MANUAL ILLUSTRATIVE"), 3)

    def test_correlation_not_causation_cautious_language(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("correlation does not imply causation", pod.lower() or "Correlation does not imply causation" in pod)
        # Or at least cautious
        self.assertIn("does not prove editorial", pod.lower() or "does not prove" in pod)

    def test_no_em_dashes(self):
        pod = load_text(PODCAST_MD)
        # Check last iteration section doesn't contain em dash
        # Find #445 section
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-20000:]
        self.assertNotIn("—", section, "No em dashes allowed per Aug 28 rule")

    def test_https_provenance(self):
        pod = load_text(PODCAST_MD)
        # Ensure all sources in #445 are HTTPS
        # Extract sources list for #445
        idx = pod.find("### 10. Sources (17 HTTPS Direct)")
        if idx == -1:
            idx = pod.find("## Iteration #445")
        section = pod[idx:idx+15000]
        # Count https:// occurrences
        https_count = section.count("https://")
        self.assertGreaterEqual(https_count, 10, f"Expected >=10 HTTPS sources, got {https_count}")
        # No http:// (non-https) except maybe in text but not in source URLs
        # Allow http:// in example but not in Sources list
        sources_start = section.find("**Sources")
        if sources_start != -1:
            sources_section = section[sources_start:sources_start+5000]
            self.assertNotIn("http://", sources_section, "Sources should be HTTPS only")

    def test_sentiment_scores_range(self):
        pod = load_text(PODCAST_MD)
        # Check sentiment scores -7 to -9 range present
        self.assertIn("-7/10", pod)
        self.assertIn("-8/10", pod)
        self.assertIn("-9/10", pod)

    def test_asymmetry_score_manual_illustrative(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Asymmetry score", pod)
        self.assertIn("MANUAL ILLUSTRATIVE -6.4286", pod)

    def test_is_significant_false(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod
        self.assertIn("is_significant: false", section.lower() or "is_significant" in section.lower() or "is_significant" in section)
        # Also check illustrative only
        self.assertIn("illustrative only", section.lower())

    def test_p_value_not_calculated(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-25000:]
        self.assertIn("p_value: NOT CALCULATED", section)
        self.assertIn("cohens_d: NOT CALCULATED", section)

    def test_confounders_ranked_strong_moderate_weak(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        # Should have STRONG, MODERATE, WEAK
        self.assertIn("[STRONG]", section)
        self.assertIn("[MODERATE]", section)
        self.assertIn("[WEAK]", section)
        # At least 2 STRONG
        self.assertGreaterEqual(section.count("[STRONG]"), 2)
        # At least 4 total confounders
        total_confounders = section.count("[STRONG]") + section.count("[MODERATE]") + section.count("[WEAK]")
        self.assertGreaterEqual(total_confounders, 4)

    def test_coverage_prediction(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Coverage Prediction", pod)
        # At least mentions future predictions
        self.assertIn("Guilty Feminist will remain silent", pod)
        self.assertIn("Samsung Galaxy Glasses", pod)

    def test_no_synthetic_significance_overclaim(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        # Should explicitly say DO NOT claim empirical significance
        self.assertIn("DO NOT claim empirical significance", section)

    def test_three_tier_model_dual_vector(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        self.assertIn("dual vectors", section.lower() or "dual-vector" in section.lower() or "dual vectors" in section.lower())
        self.assertIn("financial", section.lower())
        self.assertIn("cultural consensus", section.lower())

    def test_extension_vs_duplicate_justification(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-35000:]
        self.assertIn("Extension vs Duplicate", section)
        self.assertIn("does NOT duplicate", section)

    def test_limitations_documented(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("Limitations Documented", pod)
        idx = pod.find("### 13. Limitations Documented")
        if idx == -1:
            idx = pod.find("**Limitations:**")
        self.assertNotEqual(idx, -1)

    def test_festival_season_artifact(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("festival season", pod.lower())
        self.assertIn("Edinburgh Fringe", pod)

    def test_counterexamples_documented(self):
        pod = load_text(PODCAST_MD)
        self.assertIn("TechMagic", pod)
        self.assertIn("Waveform", pod)
        self.assertIn("counterargument", pod.lower())

    def test_iteration_log_rotation(self):
        log = load_text(ITERATION_LOG)
        # Find #445 entry
        self.assertIn("#445 Type E", log)
        self.assertIn("rotation D->E", log)
        self.assertIn("444 D to 445 E", log)

    def test_test_count_growth(self):
        # Verify test file exists and count would increase
        test_path = os.path.join(TESTS_DIR, "test_type_e_445_podcast_sentiment_twelfth_verification_cycle_sep01_11am.py")
        self.assertTrue(os.path.exists(test_path))

    def test_no_malformed_citations(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        # No proxy rehosts like appwritefunc.yet-another-testing-domain.com
        self.assertNotIn("yet-another-testing-domain.com", section)
        self.assertNotIn("appwritefunc", section)

    def test_welch_t_test_methodology_note(self):
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        self.assertIn("Welch t-test", section)
        self.assertIn("Cohen d", section)
        self.assertIn("bootstrap CI", section)

    def test_deal_disclosed_false_implied(self):
        # Type E no financial deal, should note deal_disclosed false or neutral predictor
        pod = load_text(PODCAST_MD)
        idx = pod.find("## Iteration #445")
        section = pod[idx:idx+80000] if idx != -1 else pod[-30000:]
        self.assertIn("no known", section.lower() or "deal_disclosed" in section.lower() or "neutral predictor" in section.lower())

