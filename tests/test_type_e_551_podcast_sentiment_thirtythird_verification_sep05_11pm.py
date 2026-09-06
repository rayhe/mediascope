"""
Type E #551 - Podcast Sentiment Tracking: Thirty-Third Verification Cycle Sep 5 23:00 PDT
Guilty Feminist 498 Hold No 499 as of 23:00 (search-result secondary, fresh <1h crawl, 33rd cycle) +
EHE 26-Day Hold with Times/Engadget/PetaPixel/AfroTech/Fstoppers/Sifted re-surfaces verified already-in-corpus via pre-commit grep, NOT new campaigns +
Attention Sphere 33rd No-Match (circular GitHub pages rejected, Spotify Creators <1h-fresh reconfirms nonprofit) +
NO new press surfaces this cycle (Sep 1 search window returned only older in-corpus items; eurweb new-to-corpus shape is a 177-day-old same-motif re-report; #531 Jezebel remains newest)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 551
DATE_STR = "2026-09-05 23:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_551_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #551", text, re.MULTILINE)
    assert m, "Iteration #551 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_551_block()
        assert "551" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_551_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_551_block()
        lower = block.lower()
        assert "545 d -> 546 e" not in lower  # previous cycle's rotation, not this one
        assert "550 d -> 551 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtythird_cycle_label(self):
        block = get_551_block()
        lower = block.lower()
        assert "thirty-third" in lower

    def test_distinct_from_546(self):
        block = get_551_block()
        assert "551" in block
        lower = block.lower()
        assert "thirty-third" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_551_block()
        assert "498" in block
        lower = block.lower()
        assert "latest episode" in lower or "498 hold" in lower

    def test_no_499_bounded(self):
        block = get_551_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_551_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_listennotes_secondary_fresh_crawl(self):
        block = get_551_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block
        lower = block.lower()
        assert "crawled <1h" in lower or "crawled less than 1 hour" in lower

    def test_cadence_note(self):
        block = get_551_block()
        lower = block.lower()
        assert "sep 7" in lower or "near sep 7" in lower

    def test_extension_not_duplicate(self):
        block = get_551_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "546" in block

    def test_zero_meta_episodes_across_cycles(self):
        block = get_551_block()
        lower = block.lower()
        assert "thirty-three verification cycles" in lower


class TestEveryoneHatesElon:
    def test_26_day_hold(self):
        block = get_551_block()
        lower = block.lower()
        assert "26-day hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_551_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_resurface_list(self):
        block = get_551_block()
        lower = block.lower()
        for token in ("thetimes.com", "engadget.com", "petapixel.com", "afrotech.com",
                      "fstoppers.com", "sifted.eu"):
            assert token in lower, f"missing re-surface token {token}"

    def test_fstoppers_in_corpus_verified(self):
        block = get_551_block()
        lower = block.lower()
        assert "11 hits" in lower
        assert "not new" in lower

    def test_no_new_campaign_motif(self):
        block = get_551_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_551_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "thirty-three verification cycles" in lower

    def test_no_double_counting(self):
        block = get_551_block()
        lower = block.lower()
        assert "no double-counting" in lower


class TestAttentionSphere:
    def test_33rd_no_match(self):
        block = get_551_block()
        lower = block.lower()
        assert "thirty-third no-match" in lower

    def test_circular_github_rejected(self):
        block = get_551_block()
        lower = block.lower()
        assert "circular" in lower

    def test_nonprofit_reconfirmation(self):
        block = get_551_block()
        assert "https://creators.spotify.com/pod/profile/anita-nowak/" in block
        lower = block.lower()
        assert "non-profit" in lower or "nonprofit" in lower
        assert "theattentionstudio.com" in lower

    def test_misidentified_status(self):
        block = get_551_block()
        lower = block.lower()
        assert "misidentified" in lower

    def test_bounded_claim(self):
        block = get_551_block()
        lower = block.lower()
        assert "bounded" in lower


class TestNewPressSurfaces:
    def test_no_new_press(self):
        block = get_551_block()
        lower = block.lower()
        assert "no new press surfaces this cycle" in lower

    def test_jezebel_newest(self):
        block = get_551_block()
        assert "531" in block
        lower = block.lower()
        assert "jezebel" in lower
        assert "remains the newest" in lower

    def test_eurweb_shape_handled(self):
        block = get_551_block()
        lower = block.lower()
        assert "eurweb" in lower
        assert "177" in block
        assert "same" in lower and "motif" in lower

    def test_window_bounded(self):
        block = get_551_block()
        assert "Sep 5 18:00-23:00 PDT" in block


class TestManualIllustrative:
    def test_not_calculated_triple(self):
        block = get_551_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block

    def test_is_significant_false(self):
        block = get_551_block()
        assert "is_significant False" in block

    def test_no_false_significance(self):
        block = get_551_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower

    def test_correlation_not_causation(self):
        block = get_551_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestDiscipline:
    def test_no_em_dashes(self):
        block = get_551_block()
        assert "\u2014" not in block
        assert "\u2013" not in block

    def test_https_only_urls(self):
        urls = re.findall(r"https?://\S+", get_551_block())
        for u in urls:
            assert u.startswith("https://"), f"non-HTTPS URL: {u}"

    def test_verbatim_urls_from_search(self):
        block = get_551_block()
        assert "WWW.ENGADGET.COM" in block  # verbatim from search full-URL listing

    def test_iteration_log_entry_newest_first(self):
        # Brittle-assertion repair (Type D #555): this file's run was
        # current at commit time, but the newest-first heading advances
        # each hour; assert presence of the #551 entry, not that it is
        # still the newest. Window persistence is pinned per-run.
        text = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#551 Type E", text, re.MULTILINE), \
            "iteration-log.md lost the #551 Type E entry"

    def test_test_file_self_reference(self):
        block = get_551_block()
        assert "test_type_e_551_podcast_sentiment_thirtythird_verification_sep05_11pm.py" in block
