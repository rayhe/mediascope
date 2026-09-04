"""
Type E #511 - Podcast Sentiment Tracking: Twenty-Fifth Verification Cycle Sep 4 05:00 PDT
Guilty Feminist 498 Hold No 499 as of 05:00 (zeno.fm opened this run, 25th cycle) +
EHE 25-Day Hold, No New Vertical, Six-Vertical Count Standing +
Attention Sphere 25th No-Match (nonprofit identification stays secondary-only)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 511
DATE_STR = "2026-09-04 05:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_511_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #511", text, re.MULTILINE)
    assert m, "Iteration #511 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_511_block()
        assert "511" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_511_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_511_block()
        assert "510" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twentyfifth_cycle_label(self):
        block = get_511_block()
        lower = block.lower()
        assert "twenty-fifth" in lower

    def test_extends_506(self):
        block = get_511_block()
        lower = block.lower()
        assert "506" in block
        assert "extends" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_511_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_511_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_511_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened" in block.lower()

    def test_cadence_note(self):
        block = get_511_block()
        lower = block.lower()
        assert "sep 7" in lower or "sept 7" in lower or "september 7" in lower

    def test_extension_not_duplicate(self):
        block = get_511_block()
        assert "506" in block
        lower = block.lower()
        assert "extends" in lower


class TestEveryoneHatesElon:
    def test_25_day_hold(self):
        block = get_511_block()
        assert "25" in block
        lower = block.lower()
        assert "hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_511_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_six_vertical_count_standing(self):
        block = get_511_block()
        lower = block.lower()
        assert "six" in lower
        assert "feminist majority foundation" in lower
        assert "sifted" in lower

    def test_no_new_vertical_this_cycle(self):
        block = get_511_block()
        lower = block.lower()
        assert "no new" in lower
        assert "seventh" in lower

    def test_provenance_guard(self):
        block = get_511_block()
        assert "latestly" in block.lower()

    def test_email_drive_standing(self):
        block = get_511_block()
        assert "9,000" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_511_block()
        lower = block.lower()
        assert "no competitor" in lower
        assert "bounded" in lower

    def test_known_corpus_only(self):
        block = get_511_block()
        lower = block.lower()
        assert "known" in lower
        assert "corpus" in lower


class TestAttentionSphere:
    def test_25th_no_match(self):
        block = get_511_block()
        lower = block.lower()
        assert "twenty-fifth" in lower
        assert "no-match" in lower or "no match" in lower

    def test_circular_rejection(self):
        block = get_511_block()
        lower = block.lower()
        assert "circular" in lower

    def test_bounded_claim(self):
        block = get_511_block()
        lower = block.lower()
        assert "bounded" in lower

    def test_nonprofit_identification_stays_secondary(self):
        block = get_511_block()
        lower = block.lower()
        assert "nonprofit" in lower
        assert "secondary-only" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_511_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_511_block()
        assert "-8/10" in block

    def test_correlation_not_causation(self):
        block = get_511_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_511_block()
        assert "\u2014" not in block, "Em dash found in #511 block"

    def test_https_only(self):
        block = get_511_block()
        urls = re.findall(r'https?://[^\s)\"]+', block)
        assert urls, "Expected URLs in #511 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_511_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_511_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_506(self):
        block = get_511_block()
        assert "506" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #506" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_511_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_511_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#511" in log_text
        assert "Type E" in log_text
        assert "2026-09-04 05:00 PDT" in log_text

    def test_log_newest_first_relative(self):
        # Durable rule (fixed #495): relative newest-first ordering between
        # neighboring entries, never absolute-top assertions.
        # Fix #516: anchor to line-start entry headings. The unanchored
        # find("#510 Type D") matched the #515 entry's prose ("the #510 Type D
        # guard hardcoded its own window's static commit list"), a test-staleness
        # failure of the same class #515 repaired in the #510 file. Entry
        # headings are line-start "#NNN Type X", so MULTILINE anchors resolve
        # to the actual entries. Guard intent (relative newest-first between
        # neighboring entries) is unchanged.
        log_text = LOG_PATH.read_text(encoding="utf-8")
        m511 = re.search(r"^#511 Type E", log_text, re.MULTILINE)
        m510 = re.search(r"^#510 Type D", log_text, re.MULTILINE)
        assert m511 is not None and m510 is not None
        assert m511.start() < m510.start(), "#511 entry must precede #510 (newest-first)"
