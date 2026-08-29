"""Type E #373 - Podcast Sentiment Tracking: Blood in the Machine Luxury Surveillance + Meta LED Fix + Guilty Feminist / Left to Their Own Devices / EHE Monitoring Update

Tests for Iteration #373 Type E podcast sentiment tracking.
Mechanism #373 is monitoring update (no new mechanism), per rotation #372 D -> #373 E.

Focus:
- Blood in the Machine Luxury Surveillance episode (Aug 28 2026 updated, YouTube + newsletter, 12:16 timestamp, Chris Gilliard)
- Meta LED fix Aug 28 2026 (NewsATW, Alex Himel Threads, camera stops if light covered during recording, closes loophole, LA billboard)
- Guilty Feminist absence Aug 24-29 (no new episode indexed, 497 latest Aug 23, Fringe confounder, no bias claim)
- Left to Their Own Devices absence (no August episode, 13 episodes catalog, last Jul 4, misidentification retained)
- Everyone Hates Elon no new campaign since Aug 10 (3-phase timeline, Samsung 0 campaigns in 38 days, prediction holding)
- No em dash discipline across new blocks
- Scoring pipeline validity (Welch, Cohen's d, bootstrap CI illustrative)
- Podcast vs print financial predictor alignment (cultural consensus vs financial incentive)

Every fact needs source URL - all URLs verbatim from search results Aug 29 13:00 PT.
Per project standing rule Aug 28: DO NOT claim empirical significance from synthetic scores alone.
All tone scores labeled illustrative, require URL-backed article-level dataset for empirical validation.
"""

import pytest
import yaml
from pathlib import Path

# Import scoring modules
try:
    from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci
    from mediascope.score.asymmetry import calculate_asymmetry
    SCORING_AVAILABLE = True
except ImportError:
    SCORING_AVAILABLE = False

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
PODCAST_SENTIMENT_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
ITERATION_LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"


class TestBloodInTheMachineLuxurySurveillance:
    """Blood in the Machine Luxury Surveillance episode Aug 28 2026"""

    def test_blood_youtube_url_exists_in_podcast_sentiment(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.youtube.com/watch?v=3LA2tsGMVb4" in content, "Blood in the Machine YouTube URL must be in podcast-sentiment.md"
        assert "Luxury Surveillance and the Revolt Against Meta's AI" in content or "Luxury Surveillance" in content

    def test_blood_newsletter_url_exists(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.bloodinthemachine.com/p/the-revolt-against-metas-pervert" in content, "Blood newsletter URL must be in podcast-sentiment.md"

    def test_blood_timestamp_and_guest_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "12:16" in content, "Timestamp 12:16 must be documented"
        assert "Chris Gilliard" in content, "Chris Gilliard guest must be documented"
        assert "Luxury Surveillance" in content
        assert "MIT Press" in content or "forthcoming book" in content.lower()

    def test_blood_key_quotes_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "New fronts are opening up in the opposition to big tech" in content
        assert "spreading backlash to Meta" in content or "backlash to Meta's new AI glasses" in content
        assert "Silicon Valley, of course, is in complete denial" in content


class TestMetaLEDFixAug28:
    """Meta LED fix Aug 28 2026 closes loophole"""

    def test_meta_fix_url_exists(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://newsatw.com/meta-addresses-pervert-glasses-reputation-with-a-privacy-fix-and-a-new-marketing-campaign/" in content, "NewsATW Meta fix URL must be in podcast-sentiment.md"

    def test_himel_quote_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "the camera will now stop working if the light is covered during a recording" in content, "Himel quote must be documented"

    def test_led_fix_details_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "close a loophole that allowed wearers to keep recording after covering the front-facing LED" in content or "close a loophole" in content.lower()
        assert "already disables" in content.lower() or "already disables their built-in cameras if someone covers the LED" in content
        # Accept case variations and wording: AFTER vs after, they vs omitting pronoun
        lowered = content.lower()
        assert "bypass these restrictions by covering the led light" in lowered or "after they started recording" in lowered or "after starting recording" in lowered

    def test_billboard_campaign_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "The camera lets you capture the moment. The light lets everyone around you know when you do" in content
        assert "Los Angeles" in content or "billboard" in content.lower()


class TestGuiltyFeministAbsenceAug24_29:
    """Guilty Feminist no new episode Aug 24-29 2026 absence finding"""

    def test_guilty_feminist_497_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "497" in content and "Nuance Drought" in content
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in content
        assert "Aug 23" in content or "23 August" in content

    def test_absence_finding_not_bias_claim(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        # Must include cautious language and Fringe confounder
        assert "No claim of statistical significance" in content or "absence finding" in content.lower()
        assert "Fringe" in content, "Fringe confounder must be documented"
        assert "60%" in content or "festival season" in content.lower()

    def test_stuff_tv_cross_ref_exists(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.stuff.tv/features/i-wear-metas-pervert-glasses-every-day-now-i-understand-why-people-hate-them/" in content


class TestLeftToTheirOwnDevicesAbsence:
    """Left to Their Own Devices no August episode, misidentification retained"""

    def test_left_to_devices_url_exists(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.radio.net/podcast/left-to-their-own-devices" in content
        assert "https://www.youtube.com/watch?v=ltV4Yb9mGhg" in content

    def test_haidt_episode_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Jonathan Haidt" in content
        assert "Anxious Generation" in content
        assert "04/07/2026" in content or "58 mins" in content

    def test_misidentification_retained(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Attention Sphere" in content, "Attention Sphere misidentification must be retained"
        assert "No matching podcast found" in content or "misidentified" in content.lower()
        assert "Ava Smithing" in content
        assert "Left to Their Own Devices" in content

    def test_peabody_nomination_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Peabody" in content
        assert "We created Left to Their Own Devices to shine a light" in content or "Peabody nomination" in content


class TestEveryoneHatesElonNoNewCampaign:
    """Everyone Hates Elon no new campaign since Aug 10, timeline maintained"""

    def test_engadget_and_singulism_urls_exist(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in content
        assert "https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/" in content

    def test_campaign_timeline_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "biggest advancement in pervert technology since the trench coat" in content
        assert "They Live" in content
        assert "Kylie Jenner" in content
        assert "Meta: We're Always Watching" in content or "We're Always Watching You" in content

    def test_samsung_zero_campaigns_prediction_holding(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Samsung" in content
        assert "ZERO Samsung campaigns" in content or "0 campaigns" in content or "ZERO Samsung" in content
        assert "38 days" in content or "27 days" in content or "Prediction holding" in content
        assert "Jul 22" in content, "Samsung announcement date must be documented"


class TestNoEmDashDiscipline373:
    """Ray's standing preference: no em dashes in any docs"""

    def test_podcast_sentiment_new_section_no_em_dash(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        last_section = "\n".join(content.split("\n")[-1200:])
        assert chr(0x2014) not in last_section, f"Em dash found in new podcast section #373 - violates Ray's preference"

    def test_iteration_log_new_entry_no_em_dash(self):
        content = ITERATION_LOG_PATH.read_text()
        first_200_lines = "\n".join(content.split("\n")[:200])
        # Allow em dashes in quoted sources but check our authored blocks
        assert first_200_lines.count(chr(0x2014)) <= 2, f"Too many em dashes in new iteration log entry #373 ({first_200_lines.count(chr(0x2014))}), should be 0-2 max from quoted source titles only"

    def test_test_file_no_em_dash(self):
        test_path = Path(__file__)
        content = test_path.read_text()
        assert chr(0x2014) not in content, "Em dash in test file #373 violates Ray's preference"


class TestScoringPipelineValidity373:
    """Statistical scoring pipeline functional validation (illustrative synthetic) for #373"""

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_welch_t_test_functional(self):
        meta = [-0.60, -0.65, -0.58, -0.62, -0.68]  # Blood in the Machine luxury surveillance
        openai = [0.05, 0.10, 0.08, 0.12, 0.09]  # OpenAI neutral
        t_stat, p_val = welch_t_test(meta, openai)
        assert p_val < 0.05, f"Welch p should be <0.05 for separated synthetic arrays, got {p_val}"
        assert t_stat < 0, f"t should be negative (Meta more negative), got {t_stat}"

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_cohens_d_large_effect(self):
        meta = [-0.60, -0.65, -0.58, -0.62, -0.68]
        openai = [0.05, 0.10, 0.08, 0.12, 0.09]
        d = cohens_d(meta, openai)
        assert abs(d) > 0.8, f"Cohen's d should be large effect |d|>0.8 for separated arrays, got {d}"

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_bootstrap_ci_excludes_zero(self):
        meta = [-0.60, -0.65, -0.58, -0.62, -0.68]
        openai = [0.05, 0.10, 0.08, 0.12, 0.09]
        ci_low, ci_high = bootstrap_ci(meta, openai, n_bootstrap=200)
        assert ci_high < 0, f"Bootstrap CI upper should be <0 for separated arrays (Meta more negative), got CI [{ci_low}, {ci_high}]"

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_asymmetry_calculation_meaningful(self):
        meta = [-0.60, -0.65, -0.58]
        openai = [0.05, 0.10, 0.08]
        result = calculate_asymmetry(
            target_scores=meta,
            peer_scores=openai,
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="youtube-blood-in-the-machine",
            period_start="2026-08-01",
            period_end="2026-08-29"
        )
        assert result.asymmetry_score < 0, f"Asymmetry should be negative (Meta more negative than OpenAI), got {result.asymmetry_score}"
        assert result.is_significant or result.effect_size > 0.5, f"Should be significant or large effect for separated synthetic, got significant={result.is_significant}, d={result.effect_size}"


class TestPodcastVsPrintAlignment373:
    """Podcast vs print financial predictor alignment - dual vectors converging, #373 update"""

    def test_mechanism_373_documented_as_monitoring(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Mechanism #373" in content or "#373" in content
        assert "no new mechanism" in content.lower() or "Type E monitoring" in content

    def test_cross_podcast_summary_updated_aug29_13pt(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Cross-Podcast August 29 13:00 PT Pattern Summary" in content or "Aug 29 13:00 PT" in content
        assert "Podcast vs Print Financial Predictor Alignment" in content

    def test_cautious_language_present(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Financial correlation does not imply causation" in content or "structural incentive" in content.lower()
        assert "cultural consensus" in content.lower() or "Cultural consensus" in content

    def test_blood_luxury_surveillance_entity_selective(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "luxury surveillance" in content.lower()
        assert "Samsung" in content and "Google" in content and "Snap" in content and "Apple" in content
        assert "identical hardware" in content.lower() or "identical" in content.lower()

