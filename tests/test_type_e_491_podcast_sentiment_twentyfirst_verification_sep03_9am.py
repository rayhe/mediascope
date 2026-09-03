"""
Type E #491 - Podcast Sentiment Tracking: Twenty-First Verification Cycle Sep 3 09:00 PDT
Guilty Feminist 498 Hold No 499 as of 09:00 (zeno.fm opened this run, 21st cycle) +
EHE 24-Day Hold, No New Vertical, Six-Vertical Count Standing +
Attention Sphere 21st No-Match
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 491
DATE_STR = "2026-09-03 09:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_491_block():
    text = read_doc()
    marker = "## Iteration #491"
    idx = text.find(marker)
    assert idx != -1, "Iteration #491 block not found in podcast-sentiment.md"
    # Newest-first doc: the #491 block ends where the next-older
    # "## Iteration #" entry begins. Slicing to EOF would sweep in older
    # entries (e.g. #486's own PCM guard) and break per-block assertions.
    rest = text[idx + len(marker):]
    nxt = rest.find("## Iteration #")
    block = marker + (rest[:nxt] if nxt != -1 else rest)
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_491_block()
        assert "491" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_491_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_491_block()
        assert "490" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twentyfirst_cycle_label(self):
        block = get_491_block()
        lower = block.lower()
        assert "twenty-first" in lower

    def test_extends_486(self):
        block = get_491_block()
        lower = block.lower()
        assert "486" in block
        assert "extends" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_491_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_491_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_491_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened" in block.lower()

    def test_cadence_note(self):
        block = get_491_block()
        lower = block.lower()
        assert "sep 7" in lower or "sept 7" in lower or "september 7" in lower

    def test_extension_not_duplicate(self):
        block = get_491_block()
        assert "486" in block
        lower = block.lower()
        assert "extends" in lower


class TestEveryoneHatesElon:
    def test_24_day_hold(self):
        block = get_491_block()
        assert "24" in block
        lower = block.lower()
        assert "hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_491_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_six_vertical_count_standing(self):
        block = get_491_block()
        lower = block.lower()
        assert "six" in lower
        assert "feminist majority foundation" in lower
        assert "sifted" in lower

    def test_no_new_vertical_this_cycle(self):
        block = get_491_block()
        lower = block.lower()
        assert "no new" in lower
        assert "seventh" in lower

    def test_provenance_guard(self):
        block = get_491_block()
        assert "latestly" in block.lower()

    def test_email_drive_standing(self):
        block = get_491_block()
        assert "9,000" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_491_block()
        lower = block.lower()
        assert "no competitor" in lower
        assert "bounded" in lower

    def test_known_corpus_only(self):
        block = get_491_block()
        lower = block.lower()
        assert "known" in lower
        assert "corpus" in lower


class TestAttentionSphere:
    def test_21st_no_match(self):
        block = get_491_block()
        lower = block.lower()
        assert "twenty-first" in lower
        assert "no-match" in lower or "no match" in lower

    def test_circular_rejection(self):
        block = get_491_block()
        lower = block.lower()
        assert "circular" in lower

    def test_bounded_claim(self):
        block = get_491_block()
        lower = block.lower()
        assert "bounded" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_491_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_491_block()
        assert "-8/10" in block

    def test_correlation_not_causation(self):
        block = get_491_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_491_block()
        assert "—" not in block, "Em dash found in #491 block"

    def test_https_only(self):
        block = get_491_block()
        urls = re.findall(r'https?://[^\s\)\"]+', block)
        assert urls, "Expected URLs in #491 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_491_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_491_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_486(self):
        block = get_491_block()
        assert "486" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #486" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_491_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_491_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#491" in log_text
        assert "Type E" in log_text
        assert "2026-09-03 09:00 PDT" in log_text

    def test_log_newest_first(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_491 = log_text.find("#491 Type E")
        idx_490 = log_text.find("#490 Type D")
        assert idx_491 != -1 and idx_490 != -1
        assert idx_491 < idx_490, "#491 entry must precede #490 (newest-first)"
