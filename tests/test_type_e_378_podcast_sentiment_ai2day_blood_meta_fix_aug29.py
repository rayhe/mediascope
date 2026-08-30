"""Type E #378 - Podcast Sentiment Tracking: AI2Day Daily Brief Meta Fix + Blood in the Machine Luxury Surveillance Deep-Dive + Second Loophole Closure Stack

Tests for Iteration #378 Type E podcast sentiment tracking.
Mechanism #378 is monitoring update (no new mechanism), per rotation #377 D -> #378 E.

Focus:
- AI2Day Daily Brief Aug 29 2026 (YouTube https://www.youtube.com/watch?v=0qiKNKRetCw, 0:16 chapter, backlash framing, acknowledges fix)
- Blood in the Machine deep-dive validation (YouTube https://www.youtube.com/watch?v=3LA2tsGMVb4, newsletter https://www.bloodinthemachine.com/p/the-revolt-against-metas-pervert, 12:16 timestamp, Chris Gilliard, Luxury Surveillance MIT Press forthcoming)
- Meta second loophole closure technical stack 6 sources (GadgetReview, StartupFortune, Tech-Insider, Softonic, Zotpaper, abit.ee) Himel quote, layered history v26 hardware-level tamper detection, Aug 28 continuous monitoring, market 7M pairs 69.2% Q1 2026 20M aim daily use tripled YoY, enforcement ad removal bans, CNIL Jun 29, framing finally fixing / useful it's also late / simple loophole)
- Everyone Hates Elon no new campaign since Aug 10 (re-verified Aug 29 17:00 PT, 38 days Samsung 0)
- Guilty Feminist no new episode Aug 24-29 (re-verified, 497 Nuance Drought Aug 23, Fringe STRONG confounder, no bias claim)
- Left to Their Own Devices no August episode (re-verified, 13 episodes catalog last Jul 4 Haidt, Attention Sphere misidentification retained)
- No em dash discipline across new blocks
- Scoring pipeline validity (Welch, Cohen's d, bootstrap CI illustrative, manual illustrative scores labeled)
- No truncated ellipsis URLs in iteration-log sources list
- Podcast vs print financial predictor alignment (cultural consensus vs financial incentive, Waveform positive counterexample)

Every fact needs source URL - all URLs verbatim from search results Aug 29 17:00 PT.
Per project standing rule Aug 28: DO NOT claim empirical significance from synthetic scores alone.
All tone scores labeled illustrative manual, require URL-backed article-level dataset for empirical validation.
"""

import pytest
from pathlib import Path

try:
    from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci
    from mediascope.score.asymmetry import calculate_asymmetry
    SCORING_AVAILABLE = True
except ImportError:
    SCORING_AVAILABLE = False

PODCAST_SENTIMENT_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
ITERATION_LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"


class TestAI2DayDailyBriefMetaFix:
    """AI2Day Daily Brief Meta fixes Ray-Ban smart glasses recording Aug 29 2026"""

    def test_ai2day_youtube_url_exists(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.youtube.com/watch?v=0qiKNKRetCw" in content, "AI2Day YouTube URL must be in podcast-sentiment.md"

    def test_ai2day_chapter_and_framing_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "0:16" in content, "Chapter 0:16 must be documented"
        assert "Meta patches its Ray-Ban smart glasses to stop secret recordings after public" in content
        assert "reactive fix after backlash" in content.lower() or "patches its Ray-Ban" in content

    def test_ai2day_acknowledges_fix_not_alarm_vocab(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        # Must note it does NOT apply alarm vocabulary
        assert "does NOT apply alarm vocabulary" in content or "NOT apply alarm vocabulary" in content or "does not apply" in content.lower()
        # Must note acknowledges fix
        assert "Acknowledges fix" in content or "acknowledges fix" in content.lower()

    def test_ai2day_independent_financial_predictor(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "ai2day.live" in content
        assert "independent" in content.lower()


class TestBloodInTheMachineDeepDiveValidation:
    """Blood in the Machine Luxury Surveillance deep-dive validation Aug 27-28 2026"""

    def test_blood_youtube_and_newsletter_urls_exist(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.youtube.com/watch?v=3LA2tsGMVb4" in content, "Blood YouTube URL must be in podcast-sentiment.md"
        assert "https://www.bloodinthemachine.com/p/the-revolt-against-metas-pervert" in content, "Blood newsletter URL must be in podcast-sentiment.md"

    def test_blood_timestamp_guest_academic_context(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "12:16" in content, "Timestamp 12:16 must be documented"
        assert "Chris Gilliard" in content
        assert "Luxury Surveillance" in content
        # MIT Press forthcoming or Real Life Mag
        assert "MIT Press" in content or "reallifemag" in content.lower() or "forthcoming" in content.lower()

    def test_blood_key_quotes_and_cross_refs(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "New fronts are opening up in the opposition to big tech" in content
        assert "Pervert Glasses by the masses is unfolding at breakneck pace" in content or "pervert glasses" in content.lower()
        # Cross-refs: Flock, Heatmap, Politico, Futurism, 404 Media, BBC, Billboard
        assert "Heatmap" in content or "heatmap.news" in content
        assert "Flock" in content

    def test_blood_financial_predictor_zero_cultural_consensus(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "independent Substack" in content or "Brian Merchant" in content
        assert "cultural consensus" in content.lower() or "zero financial" in content.lower() or "no Meta deal" in content.lower()


class TestMetaSecondLoopholeClosureStack:
    """Meta second loophole closure technical stack Aug 28 2026 6 sources"""

    def test_six_source_urls_exist(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered" in content
        assert "https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/" in content
        assert "https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/" in content
        assert "https://en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed" in content
        assert "https://zot.news/article/meta-fixes-smart-glasses-recording-loophole-launches-marketing-campaign-to-shed-pervert-glasses-image-mtc6qzhl" in content
        assert "https://abit.ee/en/smart-glasses/meta-smart-glasses-privacy-ray-ban-meta-recording-indicator-wearables-en" in content

    def test_himel_quote_and_layered_history(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "The camera won't start recording if the LED is blocked" in content
        assert "camera will now stop working if the light is covered during a recording" in content or "stop working if the light is covered during a recording" in content
        # Layered history
        assert "v26" in content.lower() or "mandatory" in content.lower()
        assert "hardware-level" in content.lower() or "hardware level" in content.lower()

    def test_market_context_and_enforcement(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "7 million" in content or "7M" in content
        assert "69.2%" in content
        # Enforcement ad removal
        assert "removes ads" in content or "removes ads, posts and Marketplace" in content

    def test_framing_finally_fixing_useful_late_simple_loophole(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        # At least 2 of these framings documented
        assert "finally fixing" in content.lower() or "finally" in content.lower()
        assert "useful" in content.lower() and "late" in content.lower() or "That's useful. It's also late" in content

    def test_cnil_regulator_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "CNIL" in content
        assert "almost invisible way" in content or "look too much like ordinary glasses" in content


class TestEveryoneHatesElonReverification:
    """Everyone Hates Elon no new campaign since Aug 10 re-verified Aug 29 17:00 PT"""

    def test_engadget_singulism_urls_exist(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in content or "engadget.com/2217151" in content
        assert "https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/" in content

    def test_timeline_and_samsung_zero(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "No new campaign since Aug 10" in content or "no new campaign since Aug 10" in content.lower()
        assert "Samsung" in content
        assert "38 days" in content or "0 campaigns" in content
        assert "Prediction holding" in content


class TestGuiltyFeministReverification:
    """Guilty Feminist no new episode Aug 24-29 re-verified"""

    def test_497_nuance_drought_and_zeno(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "497" in content and "Nuance Drought" in content
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in content

    def test_fringe_confounder_and_absence_language(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Fringe" in content, "Fringe confounder must be documented"
        assert "STRONG" in content or "strong" in content.lower()
        assert "absence" in content.lower()
        assert "not intentional omission" in content.lower() or "not bias" in content.lower() or "No claim of statistical significance" in content


class TestLeftToTheirOwnDevicesReverification:
    """Left to Their Own Devices no August episode re-verified"""

    def test_radio_net_urls_and_haidt(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "https://www.radio.net/podcast/left-to-their-own-devices" in content
        assert "Jonathan Haidt" in content
        assert "Anxious Generation" in content

    def test_misidentification_retained(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Attention Sphere" in content
        assert "No matching podcast found" in content or "misidentified" in content.lower()
        assert "Ava Smithing" in content

    def test_peabody_nomination(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Peabody" in content


class TestNoEmDashDiscipline378:
    """Ray's standing preference: no em dashes in any docs"""

    def test_podcast_sentiment_new_section_no_em_dash(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        last_section = "\n".join(content.split("\n")[-1500:])
        assert chr(0x2014) not in last_section, f"Em dash found in new podcast section #378 - violates Ray's preference"

    def test_iteration_log_new_entry_no_em_dash(self):
        content = ITERATION_LOG_PATH.read_text()
        first_300_lines = "\n".join(content.split("\n")[:300])
        # Allow em dashes in quoted sources but check our authored blocks - should be 0-3 max from quoted titles
        assert first_300_lines.count(chr(0x2014)) <= 3, f"Too many em dashes in new iteration log entry #378 ({first_300_lines.count(chr(0x2014))}), should be 0-3 max from quoted source titles only"

    def test_test_file_no_em_dash(self):
        test_path = Path(__file__)
        content = test_path.read_text()
        assert chr(0x2014) not in content, "Em dash in test file #378 violates Ray's preference"


class TestNoTruncatedEllipsisURLs:
    """Exact URLs only - no truncated ellipsis URLs in iteration-log sources list except where base domain only noted"""

    def test_iteration_log_sources_no_ellipsis_truncation(self):
        content = ITERATION_LOG_PATH.read_text()
        # Extract sources list section (first 400 lines contains sources list)
        first_400 = "\n".join(content.split("\n")[:400])
        # Sources list should contain exact verified URLs - check for bad patterns like "https://ai2day.live/story/meta-patche..."
        # Those truncated URLs are NOT allowed in Sources List section (they are allowed only in description of source story truncation noted as truncated)
        # Count occurrences of "..." in sources list - should be 0 for URLs (we allow ... in verbatim quotes but not URLs)
        # The sources list is after "### Sources List" heading
        if "### Sources List" in first_400:
            sources_section = first_400.split("### Sources List")[1]
            # Remove lines that are not URLs (allow ... in non-URL text? No, sources list is URLs only)
            lines = [l for l in sources_section.split("\n") if l.strip().startswith("- https")]
            for line in lines:
                assert "..." not in line, f"Truncated ellipsis URL found in sources list: {line} - must be exact verified URL or base domain only"


class TestManualIllustrativeScoresLabeled:
    """All tone scores must be labeled manual illustrative not empirical per project standing rule Aug 28"""

    def test_podcast_sentiment_manual_illustrative_labeled(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        last_1500 = "\n".join(content.split("\n")[-1500:])
        # Must contain MANUAL ILLUSTRATIVE in new entries
        assert "MANUAL ILLUSTRATIVE" in last_1500 or "manual illustrative" in last_1500.lower(), "New podcast entries must label sentiment scores as manual illustrative per Aug 28 rule"

    def test_iteration_log_manual_illustrative_labeled(self):
        content = ITERATION_LOG_PATH.read_text()
        first_400 = "\n".join(content.split("\n")[:400])
        assert "MANUAL ILLUSTRATIVE" in first_400 or "manual illustrative" in first_400.lower(), "Iteration log #378 must label sentiment scores as manual illustrative"


class TestScoringPipelineValidity378:
    """Statistical scoring pipeline functional validation (illustrative synthetic) for #378"""

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_welch_t_test_functional(self):
        meta = [-0.60, -0.65, -0.58, -0.62, -0.68]  # Blood in the Machine luxury surveillance negative
        openai = [0.05, 0.10, 0.08, 0.12, 0.09]  # OpenAI neutral aspirational
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
        diff = sum(meta)/len(meta) - sum(openai)/len(openai)
        ci_low, ci_high = bootstrap_ci(meta, openai, n_bootstrap=1000)
        # CI should exclude 0 for large effect
        assert ci_low < 0 and ci_high < 0, f"Bootstrap CI should be entirely negative, got [{ci_low}, {ci_high}]"

    @pytest.mark.skipif(not SCORING_AVAILABLE, reason="Scoring modules not available")
    def test_asymmetry_threshold(self):
        from datetime import datetime, timedelta
        meta_scores = [-0.60, -0.65, -0.58, -0.62, -0.68]
        competitor_scores = [0.05, 0.10, 0.08, 0.12, 0.09]
        # calculate_asymmetry requires target_entity, peer_entities, publication_slug, period_start, period_end
        result = calculate_asymmetry(
            target_scores=meta_scores,
            peer_scores=competitor_scores,
            target_entity="Meta",
            peer_entities=["OpenAI", "Apple", "Google"],
            publication_slug="test_publication",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 29)
        )
        # result is AsymmetryScore dataclass, asymmetry_score is target_avg - peer_avg
        asymmetry_val = result.asymmetry_score if hasattr(result, 'asymmetry_score') else result
        assert abs(asymmetry_val) > 0.5, f"Asymmetry should be |asymmetry|>0.5 for separated arrays, got {asymmetry_val}"


class TestPodcastVsPrintFinancialPredictorAlignment:
    """Podcast vs print financial predictor alignment - cultural consensus vs financial incentive, Waveform positive counterexample"""

    def test_waveform_positive_counterexample_documented(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "Waveform" in content, "Waveform positive counterexample must be documented"
        assert "positive counterexample" in content.lower() or "POSITIVE COUNTEREXAMPLE" in content

    def test_cultural_consensus_vs_financial_incentive(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        assert "cultural consensus" in content.lower()
        assert "financial incentive" in content.lower() or "financial predictor" in content.lower()

    def test_structural_incentive_not_proof_of_influence(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        last_2000 = "\n".join(content.split("\n")[-2000:])
        assert "structural" in last_2000.lower() or "structural incentive" in last_2000.lower()
        assert "not proof" in last_2000.lower() or "not prove" in last_2000.lower() or "not proof of editorial influence" in last_2000.lower()

    def test_confounders_preserved(self):
        content = PODCAST_SENTIMENT_PATH.read_text()
        # Must preserve 5 confounders 2 STRONG 2 MODERATE 1 WEAK
        assert "STRONG" in content
        assert "MODERATE" in content or "moderate" in content.lower()
        assert "WEAK" in content or "weak" in content.lower()
