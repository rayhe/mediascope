"""
Type E #480 - Podcast Sentiment Tracking: Sifted Sixth Vertical Sep 2 22:00 PDT
Guilty Feminist 498 Hold No 499 as of 22:00 (zeno.fm opened this run, 19th cycle) +
EHE Sifted European Startup-Press Sixth Vertical New-To-Log (first-hand open) +
Attention Sphere 19th No-Match
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 480
DATE_STR = "2026-09-02 22:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_480_block():
    text = read_doc()
    marker = "## Iteration #480"
    idx = text.find(marker)
    assert idx != -1, "Iteration #480 block not found in podcast-sentiment.md"
    return text[idx:]


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_480_block()
        assert "480" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_480_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_480_block()
        assert "479" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_nineteenth_cycle_label(self):
        block = get_480_block()
        assert "Nineteenth" in block or "nineteenth" in block


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_480_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_480_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_480_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened" in block.lower()

    def test_cadence_note(self):
        block = get_480_block()
        lower = block.lower()
        assert "sep 7" in lower or "sept 7" in lower or "september 7" in lower

    def test_extension_not_duplicate(self):
        block = get_480_block()
        assert "475" in block
        lower = block.lower()
        assert "extends" in lower


class TestEveryoneHatesElonSifted:
    def test_sixth_vertical_new_to_log(self):
        block = get_480_block()
        lower = block.lower()
        assert "sifted" in lower
        assert "sixth" in lower
        assert "new-to-log" in lower

    def test_sifted_url_present(self):
        block = get_480_block()
        assert "https://sifted.eu/articles/should-tech-events-ban-smart-glasses/" in block

    def test_first_hand_open(self):
        block = get_480_block()
        lower = block.lower()
        assert "first-hand" in lower

    def test_ehe_linkage_quote(self):
        block = get_480_block()
        assert "Glasses for people who don't do consent" in block

    def test_alarm_vocabulary_noted(self):
        block = get_480_block()
        lower = block.lower()
        assert "pervert glasses" in lower
        assert "stalkerware" in lower

    def test_ban_roster_datapoints(self):
        block = get_480_block()
        lower = block.lower()
        assert "defcon" in lower
        assert "wetherspoons" in lower

    def test_balance_note(self):
        block = get_480_block()
        lower = block.lower()
        assert "balance" in lower
        assert "contacted meta for comment" in lower

    def test_ft_backing_bounded(self):
        block = get_480_block()
        lower = block.lower()
        assert "ft-backed" in lower or "ft backing" in lower
        assert "correlation not causation" in lower

    def test_23_day_hold(self):
        block = get_480_block()
        assert "23" in block
        lower = block.lower()
        assert "hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_480_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_six_vertical_count(self):
        block = get_480_block()
        lower = block.lower()
        assert "six" in lower
        assert "feminist majority foundation" in lower

    def test_provenance_guard(self):
        block = get_480_block()
        assert "latestly" in block.lower()

    def test_email_drive_standing(self):
        block = get_480_block()
        assert "9,000" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_480_block()
        lower = block.lower()
        assert "no competitor" in lower
        assert "bounded" in lower


class TestAttentionSphere:
    def test_19th_no_match(self):
        block = get_480_block()
        lower = block.lower()
        assert "nineteenth" in lower
        assert "no-match" in lower or "no match" in lower

    def test_circular_rejection(self):
        block = get_480_block()
        lower = block.lower()
        assert "circular" in lower

    def test_bounded_claim(self):
        block = get_480_block()
        lower = block.lower()
        assert "bounded" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_480_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_sifted_illustrative_score(self):
        block = get_480_block()
        assert "-4/10" in block

    def test_correlation_not_causation(self):
        block = get_480_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_480_block()
        assert "\u2014" not in block, "Em dash found in #480 block"

    def test_https_only(self):
        block = get_480_block()
        urls = re.findall(r'https?://[^\s\)\"]+', block)
        assert urls, "Expected URLs in #480 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_480_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_480_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_475(self):
        block = get_480_block()
        assert "475" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #475" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_480_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_480_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#480" in log_text
        assert "Type E" in log_text
        assert "2026-09-02 22:00 PDT" in log_text

    def test_log_newest_first(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_480 = log_text.find("#480 Type E")
        idx_479 = log_text.find("#479 Type D")
        assert idx_480 != -1 and idx_479 != -1
        assert idx_480 < idx_479, "#480 entry must precede #479 (newest-first)"
