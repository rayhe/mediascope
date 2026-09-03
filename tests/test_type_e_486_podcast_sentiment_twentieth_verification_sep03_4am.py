"""
Type E #486 - Podcast Sentiment Tracking: Twentieth Verification Cycle Sep 3 04:00 PDT
Guilty Feminist 498 Hold No 499 as of 04:00 (zeno.fm opened this run, 20th cycle) +
EHE 24-Day Hold, No New Vertical, Six-Vertical Count Standing +
Attention Sphere 20th No-Match
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 486
DATE_STR = "2026-09-03 04:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_486_block():
    text = read_doc()
    marker = "## Iteration #486"
    idx = text.find(marker)
    assert idx != -1, "Iteration #486 block not found in podcast-sentiment.md"
    return text[idx:]


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_486_block()
        assert "486" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_486_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_486_block()
        assert "485" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twentieth_cycle_label(self):
        block = get_486_block()
        lower = block.lower()
        assert "twentieth" in lower

    def test_extends_480(self):
        block = get_486_block()
        lower = block.lower()
        assert "480" in block
        assert "extends" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_486_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_486_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_486_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened" in block.lower()

    def test_cadence_note(self):
        block = get_486_block()
        lower = block.lower()
        assert "sep 7" in lower or "sept 7" in lower or "september 7" in lower

    def test_extension_not_duplicate(self):
        block = get_486_block()
        assert "480" in block
        lower = block.lower()
        assert "extends" in lower


class TestEveryoneHatesElon:
    def test_24_day_hold(self):
        block = get_486_block()
        assert "24" in block
        lower = block.lower()
        assert "hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_486_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_six_vertical_count_standing(self):
        block = get_486_block()
        lower = block.lower()
        assert "six" in lower
        assert "feminist majority foundation" in lower
        assert "sifted" in lower

    def test_no_new_vertical_this_cycle(self):
        block = get_486_block()
        lower = block.lower()
        assert "no new" in lower
        assert "seventh" in lower

    def test_provenance_guard(self):
        block = get_486_block()
        assert "latestly" in block.lower()

    def test_email_drive_standing(self):
        block = get_486_block()
        assert "9,000" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_486_block()
        lower = block.lower()
        assert "no competitor" in lower
        assert "bounded" in lower

    def test_known_corpus_only(self):
        block = get_486_block()
        lower = block.lower()
        assert "known" in lower
        assert "corpus" in lower


class TestAttentionSphere:
    def test_20th_no_match(self):
        block = get_486_block()
        lower = block.lower()
        assert "twentieth" in lower
        assert "no-match" in lower or "no match" in lower

    def test_circular_rejection(self):
        block = get_486_block()
        lower = block.lower()
        assert "circular" in lower

    def test_bounded_claim(self):
        block = get_486_block()
        lower = block.lower()
        assert "bounded" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_486_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_486_block()
        assert "-8/10" in block

    def test_correlation_not_causation(self):
        block = get_486_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_486_block()
        assert " " not in block, "Em dash found in #486 block"

    def test_https_only(self):
        block = get_486_block()
        urls = re.findall(r'https?://[^\s\)\"]+', block)
        assert urls, "Expected URLs in #486 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_486_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_486_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_480(self):
        block = get_486_block()
        assert "480" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #480" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_486_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_486_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#486" in log_text
        assert "Type E" in log_text
        assert "2026-09-03 04:00 PDT" in log_text

    def test_log_newest_first(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_486 = log_text.find("#486 Type E")
        idx_485 = log_text.find("#485 Type D")
        assert idx_486 != -1 and idx_485 != -1
        assert idx_486 < idx_485, "#486 entry must precede #485 (newest-first)"
