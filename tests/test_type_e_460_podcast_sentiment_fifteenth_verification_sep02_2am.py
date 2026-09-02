"""
Type E #460 - Podcast Sentiment Tracking Fifteenth Verification Sep 2 02:00 PDT
Guilty Feminist 498 Hold No 499 as of 02:00 + EHE 23-Day Hold + New 9000 Email Drive
Surfaced via SWNS + Attention Sphere 15th No-Match + The Drum/AfroTech Secondary
"""
import re
from pathlib import Path

import pytest

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 460
DATE_STR = "2026-09-02 02:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_460_block():
    text = read_doc()
    marker = "## Iteration #460"
    idx = text.find(marker)
    assert idx != -1, "Iteration #460 block not found in podcast-sentiment.md"
    return text[idx:]


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_460_block()
        assert "460" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_460_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_460_block()
        assert "459" in block
        assert "D->E" in block

    def test_goal_and_job_ids(self):
        block = get_460_block()
        assert GOAL_ID in block
        assert JOB_ID in block

    def test_fifteenth_verification_labeled(self):
        block = get_460_block()
        lower = block.lower()
        assert "fifteenth" in lower


class TestGuiltyFeminist498Hold:
    def test_498_latest_no_499(self):
        block = get_460_block()
        assert "498" in block
        assert "499" in block
        lower = block.lower()
        assert "no 499" in lower or "no new episode beyond 498" in lower

    def test_official_list_https(self):
        block = get_460_block()
        assert "https://guiltyfeminist.com/list-of-episodes/" in block

    def test_bounded_absence_language(self):
        block = get_460_block()
        lower = block.lower()
        assert "bounded" in lower
        assert "not universal proof" in lower


class TestEveryoneHatesElon:
    def test_activist_not_podcast(self):
        block = get_460_block()
        lower = block.lower()
        assert "activist group" in lower
        assert "not a podcast" in lower

    def test_23_day_hold(self):
        block = get_460_block()
        assert "23-day hold" in block or "23 day" in block.lower()

    def test_email_drive_data_point(self):
        block = get_460_block()
        assert "9,000" in block
        lower = block.lower()
        assert "email" in lower
        assert "swns" in lower

    def test_email_drive_surfaced_not_new(self):
        block = get_460_block()
        lower = block.lower()
        assert "surfaced-not-new" in lower or "surfaced not new" in lower or "new to this log" in lower

    def test_email_drive_dating_bound(self):
        block = get_460_block()
        assert "https://muckrack.com/ben-barry-4/articles" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_460_block()
        lower = block.lower()
        assert "no equivalent" in lower or "no competitor" in lower


class TestAttentionSphere:
    def test_15th_no_match(self):
        block = get_460_block()
        lower = block.lower()
        assert "no-match" in lower or "no matching podcast" in lower
        assert "15th" in lower or "fifteenth" in lower

    def test_circular_rejection(self):
        block = get_460_block()
        lower = block.lower()
        assert "circular" in lower
        assert "reject" in lower

    def test_bounded_absence(self):
        block = get_460_block()
        lower = block.lower()
        assert "bounded" in lower


class TestSecondaryEcosystem:
    def test_thedrum_present_https(self):
        block = get_460_block()
        assert "https://www.thedrum.com/opinion/mark-palmer-is-the-glasses-partnership-with-meta-making-ray-ban-lose-its-cool" in block

    def test_afrotech_present_https(self):
        block = get_460_block()
        assert "https://afrotech.com/smart-glasses-ethics-and-consent" in block


class TestEvidenceDiscipline:
    def test_manual_illustrative_label(self):
        block = get_460_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_correlation_not_causation(self):
        block = get_460_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_460_block()
        assert "\u2014" not in block, "Em dash found in #460 block"

    def test_https_only(self):
        block = get_460_block()
        urls = re.findall(r'https?://[^\s\)\"]+', block)
        assert urls, "Expected URLs in #460 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_460_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "no empirical significance" in lower or "do not claim empirical" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_455(self):
        block = get_460_block()
        assert "455" in block
        lower = block.lower()
        assert "extension not duplicate" in lower or "not duplicate" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_460_block()
        assert "Microsoft PCM" in block
        lower = block.lower()
        assert "already" in lower or "no pcm novelty" in lower


class TestIterationLog:
    def test_iteration_log_460_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#460" in log_text
        assert "Type E" in log_text
        assert "2026-09-02 02:00 PDT" in log_text

    def test_log_newest_first(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_460 = log_text.find("#460 Type E")
        idx_459 = log_text.find("#459 Type D")
        assert idx_460 != -1 and idx_459 != -1
        assert idx_460 < idx_459, "#460 entry must precede #459 (newest-first)"
