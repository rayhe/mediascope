"""
Type E #516 - Podcast Sentiment Tracking: Twenty-Sixth Verification Cycle Sep 4 10:00 PDT
Guilty Feminist 498 Hold No 499 as of 10:00 (zeno.fm opened this run, 26th cycle) +
EHE 25-Day Hold, NEW IBTimes UK Seventh Press Vertical (rehost provenance caveat) +
Attention Sphere 26th No-Match (nonprofit identification stays secondary-only)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 516
DATE_STR = "2026-09-04 10:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_516_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #516", text, re.MULTILINE)
    assert m, "Iteration #516 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_516_block()
        assert "516" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_516_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_516_block()
        assert "515" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twenty_sixth_cycle_label(self):
        block = get_516_block()
        lower = block.lower()
        assert "twenty-sixth" in lower

    def test_extends_511(self):
        block = get_516_block()
        assert "#511" in block
        assert "5 hours" in block or "5-hour" in block


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_516_block()
        assert "498" in block
        assert "Politics" in block
        assert "31 Aug 2026" in block

    def test_no_499_bounded(self):
        block = get_516_block()
        assert "No 499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_516_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened this run" in block

    def test_cadence_note(self):
        block = get_516_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()

    def test_extension_not_duplicate(self):
        block = get_516_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "fresh primary open" in lower


class TestEveryoneHatesElon:
    def test_25_day_hold(self):
        block = get_516_block()
        assert "25 days" in block
        assert "Aug 10" in block

    def test_activist_not_podcast_discipline(self):
        block = get_516_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_ibtimes_seventh_vertical_new(self):
        block = get_516_block()
        assert "IBTimes UK" in block
        assert "seventh press vertical" in block.lower()

    def test_ibtimes_provenance_caveat(self):
        block = get_516_block()
        lower = block.lower()
        assert "provenance caveat" in lower
        assert "cloudfront" in lower
        assert "ibtimes.co.uk" in lower

    def test_ibtimes_linkage_quotes(self):
        block = get_516_block()
        assert "We're always watching" in block
        assert "giving fascism, not fashion" in block

    def test_ibtimes_self_reference_bounded(self):
        block = get_516_block()
        lower = block.lower()
        assert "self-reference" in lower
        assert "bounded" in lower

    def test_seven_vertical_count(self):
        block = get_516_block()
        lower = block.lower()
        assert "six to seven" in lower
        assert "uk online press" in lower

    def test_provenance_guard(self):
        block = get_516_block()
        assert "latestly.com" in block
        lower = block.lower()
        assert "spoof activism" in lower

    def test_email_drive_standing(self):
        block = get_516_block()
        assert "9,000" in block
        assert "muckrack.com" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_516_block()
        lower = block.lower()
        assert "twenty-six" in lower
        assert "bounded search-result absence" in lower

    def test_known_corpus_only(self):
        block = get_516_block()
        lower = block.lower()
        assert "known july/august corpus" in lower


class TestNewPressItems:
    def test_tribune_times_snippet_bounded(self):
        block = get_516_block()
        assert "Tribune Times" in block
        assert "tribunetimes.co.uk" in block
        lower = block.lower()
        assert "snippet-bounded" in lower
        assert "not an ehe vertical" in lower or "not a vertical" in lower

    def test_reuters_lse_snippet_bounded(self):
        block = get_516_block()
        assert "lse.co.uk" in block
        lower = block.lower()
        assert "cinema" in lower
        assert "snippet-bounded" in lower


class TestAttentionSphere:
    def test_26th_no_match(self):
        block = get_516_block()
        lower = block.lower()
        assert "twenty-sixth" in lower
        assert "no-match" in lower or "no matching podcast" in lower

    def test_circular_rejection(self):
        block = get_516_block()
        lower = block.lower()
        assert "circular" in lower
        assert "not cited as evidence" in lower

    def test_bounded_claim(self):
        block = get_516_block()
        lower = block.lower()
        assert "bounded search-result absence" in lower

    def test_nonprofit_identification_stays_secondary(self):
        block = get_516_block()
        lower = block.lower()
        assert "secondary-only" in lower
        assert "left to their own devices" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_516_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_516_block()
        assert "-8/10" in block

    def test_ibtimes_illustrative_score_not_asymmetry_evidence(self):
        block = get_516_block()
        assert "-4/10" in block
        lower = block.lower()
        assert "not scored as asymmetry evidence" in lower

    def test_correlation_not_causation(self):
        block = get_516_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_516_block()
        assert "\u2014" not in block, "Em dash found in #516 block"

    def test_https_only(self):
        block = get_516_block()
        urls = re.findall(r'https?://[^\s)\"]+', block)
        assert urls, "Expected URLs in #516 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_516_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_516_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_511(self):
        block = get_516_block()
        assert "511" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #511" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_516_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_516_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#516" in log_text
        assert "Type E" in log_text
        assert "2026-09-04 10:00 PDT" in log_text

    def test_log_newest_first_relative(self):
        # Durable rule (fixed #495): relative newest-first ordering between
        # neighboring entries, never absolute-top assertions.
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_516 = log_text.find("#516 Type E")
        idx_515 = log_text.find("#515 Type D")
        assert idx_516 != -1 and idx_515 != -1
        assert idx_516 < idx_515, "#516 entry must precede #515 (newest-first)"
