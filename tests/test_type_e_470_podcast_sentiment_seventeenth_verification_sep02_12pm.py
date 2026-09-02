"""
Type E #470 - Podcast Sentiment Tracking Seventeenth Verification Sep 2 12:00 PDT
Guilty Feminist 498 Hold No 499 as of 12:00 (zeno.fm opened this run) +
EHE 23-Day Hold Continues + Feminist Majority Foundation Advocacy-Press
Fifth Vertical (with balance note) + LatestLY Provenance Guard +
Attention Sphere 17th No-Match
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 470
DATE_STR = "2026-09-02 12:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_470_block():
    text = read_doc()
    marker = "## Iteration #470"
    idx = text.find(marker)
    assert idx != -1, "Iteration #470 block not found in podcast-sentiment.md"
    return text[idx:]


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_470_block()
        assert "470" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_470_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_470_block()
        assert "469" in block
        assert "D->E" in block

    def test_goal_and_job_ids(self):
        block = get_470_block()
        assert GOAL_ID in block
        assert JOB_ID in block

    def test_seventeenth_verification_labeled(self):
        block = get_470_block()
        lower = block.lower()
        assert "seventeenth" in lower


class TestGuiltyFeminist498Hold:
    def test_498_latest_no_499(self):
        block = get_470_block()
        assert "498" in block
        assert "499" in block
        lower = block.lower()
        assert "no 499" in lower or "no new episode beyond 498" in lower

    def test_official_list_https_opened_this_run(self):
        block = get_470_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        lower = block.lower()
        assert "opened" in lower or "this run" in lower

    def test_bounded_absence_language(self):
        block = get_470_block()
        lower = block.lower()
        assert "bounded" in lower
        assert "not universal proof" in lower

    def test_cadence_note(self):
        block = get_470_block()
        lower = block.lower()
        assert "cadence" in lower

    def test_extension_not_duplicate(self):
        block = get_470_block()
        lower = block.lower()
        assert "extension not duplicate" in lower or "extends #465" in lower or "5-hour extension" in lower


class TestEveryoneHatesElon:
    def test_activist_not_podcast(self):
        block = get_470_block()
        lower = block.lower()
        assert "activist group" in lower
        assert "not a podcast" in lower

    def test_23_day_hold(self):
        block = get_470_block()
        assert "23-day hold" in block or "23 day" in block.lower()

    def test_email_drive_standing(self):
        block = get_470_block()
        assert "9,000" in block
        lower = block.lower()
        assert "swns" in lower

    def test_fmf_fifth_vertical(self):
        block = get_470_block()
        assert "https://feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/" in block
        lower = block.lower()
        assert "feminist majority foundation" in lower
        assert "fifth" in lower

    def test_balance_note_recorded(self):
        block = get_470_block()
        lower = block.lower()
        assert "balance" in lower
        assert "blind" in lower or "visually impaired" in lower or "low-vision" in lower

    def test_latestly_provenance_guard(self):
        block = get_470_block()
        assert "https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html" in block
        lower = block.lower()
        assert "provenance" in lower

    def test_no_competitor_equivalent_bounded(self):
        block = get_470_block()
        lower = block.lower()
        assert "no equivalent" in lower or "no competitor" in lower


class TestAttentionSphere:
    def test_17th_no_match(self):
        block = get_470_block()
        lower = block.lower()
        assert "no-match" in lower or "no matching podcast" in lower
        assert "17th" in lower or "seventeenth" in lower

    def test_circular_rejection(self):
        block = get_470_block()
        lower = block.lower()
        assert "circular" in lower
        assert "reject" in lower

    def test_bounded_absence(self):
        block = get_470_block()
        lower = block.lower()
        assert "bounded" in lower


class TestEvidenceDiscipline:
    def test_manual_illustrative_label(self):
        block = get_470_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_correlation_not_causation(self):
        block = get_470_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_470_block()
        assert "\u2014" not in block, "Em dash found in #470 block"

    def test_https_only(self):
        block = get_470_block()
        urls = re.findall(r'https?://[^\s\)\"]+', block)
        assert urls, "Expected URLs in #470 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_470_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_470_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_465(self):
        block = get_470_block()
        assert "465" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #465" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_470_block()
        assert "Microsoft PCM" in block
        lower = block.lower()
        assert "already" in lower or "no pcm novelty" in lower


class TestIterationLog:
    def test_iteration_log_470_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#470" in log_text
        assert "Type E" in log_text
        assert "2026-09-02 12:00 PDT" in log_text

    def test_log_newest_first(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_470 = log_text.find("#470 Type E")
        idx_469 = log_text.find("#469 Type D")
        assert idx_470 != -1 and idx_469 != -1
        assert idx_470 < idx_469, "#470 entry must precede #469 (newest-first)"
