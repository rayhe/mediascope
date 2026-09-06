"""
Type E #556 - Podcast Sentiment Tracking: Thirty-Fourth Verification Cycle Sep 6 04:00 PDT
Guilty Feminist 498 Hold No 499 as of 04:00 (search-result secondary, 5h crawl, 34th cycle,
official-site parity, cadence note Sep 7) +
EHE 27-Day Hold with Times/LatestLY/PetaPixel/Engadget/feminist.org/AfroTech/Hyperallergic
re-surfaces verified already-in-corpus via pre-commit grep, NOT new campaigns +
Attention Sphere 34th No-Match (circular GitHub pages rejected, Spotify Creators 5h-fresh
reconfirms nonprofit) +
NO new press surfaces this cycle (Sep 1 search window returned only older in-corpus items;
#531 Jezebel remains newest)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 556
DATE_STR = "2026-09-06 04:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_556_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #556", text, re.MULTILINE)
    assert m, "Iteration #556 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_556_block()
        assert "556" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_556_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_556_block()
        lower = block.lower()
        assert "550 d -> 551 e" not in lower  # previous cycle's rotation, not this one
        assert "555 d -> 556 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtyfourth_cycle_label(self):
        block = get_556_block()
        lower = block.lower()
        assert "thirty-fourth" in lower

    def test_distinct_from_551(self):
        block = get_556_block()
        lower = block.lower()
        assert "thirty-fourth" in lower
        assert "551" in block  # references prior cycle by number, not as self


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_556_block()
        assert "498" in block
        lower = block.lower()
        assert "latest episode" in lower or "498 hold" in lower

    def test_no_499_bounded(self):
        block = get_556_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_556_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_listennotes_secondary_5h_crawl(self):
        block = get_556_block()
        assert "ListenNotes" in block or "listennotes" in block.lower()
        assert "5 hours" in block

    def test_cadence_note(self):
        block = get_556_block()
        assert "Sep 7" in block
        lower = block.lower()
        assert "cadence" in lower

    def test_official_site_parity(self):
        block = get_556_block()
        assert "guiltyfeminist.com" in block
        lower = block.lower()
        assert "kings place" in lower or "london podcast festival" in lower

    def test_zero_meta_episodes_across_cycles(self):
        block = get_556_block()
        lower = block.lower()
        assert "zero meta/wearables episodes across all thirty-four" in lower


class TestEveryoneHatesElon:
    def test_27_day_hold(self):
        block = get_556_block()
        assert "27 days" in block

    def test_activist_not_podcast_discipline(self):
        block = get_556_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_resurface_list(self):
        block = get_556_block()
        lower = block.lower()
        for shape in ["times", "latestly", "petapixel", "engadget", "feminist.org",
                      "afrotech", "hyperallergic"]:
            assert shape in lower, f"missing re-surface shape: {shape}"

    def test_feminist_org_in_corpus_verified(self):
        block = get_556_block()
        assert "29 corpus hits" in block

    def test_afrotech_hyperallergic_in_corpus_verified(self):
        block = get_556_block()
        assert "10 corpus hits" in block
        assert "5 corpus files" in block

    def test_no_new_campaign_motif(self):
        block = get_556_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_556_block()
        lower = block.lower()
        assert "no competitor-equivalent" in lower

    def test_no_double_counting(self):
        block = get_556_block()
        assert "No double-counting" in block


class TestAttentionSphere:
    def test_34th_no_match(self):
        block = get_556_block()
        assert "Thirty-Fourth No-Match" in block or "thirty-fourth no-match" in block.lower()

    def test_circular_github_rejected(self):
        block = get_556_block()
        lower = block.lower()
        assert "circular" in lower

    def test_nonprofit_reconfirmation(self):
        block = get_556_block()
        lower = block.lower()
        assert "non-profit organization" in lower
        assert "theattentionstudio.com" in lower

    def test_misidentified_status(self):
        block = get_556_block()
        lower = block.lower()
        assert "misidentified" in lower

    def test_bounded_claim(self):
        block = get_556_block()
        lower = block.lower()
        assert "bounded search-result absence" in lower


class TestNewPressSurfaces:
    def test_no_new_press(self):
        block = get_556_block()
        lower = block.lower()
        assert "no new press surfaces this cycle" in lower

    def test_jezebel_newest(self):
        block = get_556_block()
        assert "#531 Jezebel" in block
        lower = block.lower()
        assert "newest" in lower

    def test_older_items_all_in_corpus(self):
        block = get_556_block()
        lower = block.lower()
        for shape in ["reuters.com", "techcrunch.com", "livemint.com",
                      "forbesindia.com", "epic.org"]:
            assert shape in lower, f"missing press shape: {shape}"

    def test_window_bounded(self):
        block = get_556_block()
        assert "Sep 5 23:00 - Sep 6 04:00 PDT" in block


class TestStatisticalDiscipline:
    def test_not_calculated_triple(self):
        block = get_556_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block

    def test_is_significant_false(self):
        block = get_556_block()
        assert "is_significant False" in block

    def test_no_false_significance(self):
        block = get_556_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower

    def test_correlation_not_causation(self):
        block = get_556_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestSourceHygiene:
    def test_no_em_dashes(self):
        # Per #553 precedent: block-level check via escape, never a literal
        # em-dash token (a literal trips its own assertion).
        block = get_556_block()
        assert "\u2014" not in block
        assert "\u2013" not in block

    def test_urls_mostly_https_verbatim_http_documented(self):
        # The search full-URL listing for Hyperallergic was http, copied
        # verbatim per the verbatim rule; everything else must be https.
        urls = re.findall(r"https?://\S+", get_556_block())
        for u in urls:
            ok = u.startswith("https://") or u.startswith(
                "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/"
            )
            assert ok, f"non-HTTPS non-verbatim URL: {u}"

    def test_verbatim_urls_from_search(self):
        block = get_556_block()
        assert "WWW.ENGADGET.COM" in block  # verbatim from search full-URL listing
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block

    def test_iteration_log_entry_presence(self):
        # Brittle-assertion repair (Type D #555): assert presence of the #556
        # entry, not newest-firstness (the heading advances each hour).
        text = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#556 Type E", text, re.MULTILINE), \
            "iteration-log.md lost the #556 Type E entry"

    def test_test_file_self_reference(self):
        block = get_556_block()
        assert "test_type_e_556_podcast_sentiment_thirtyfourth_verification_sep06_4am.py" in block


class TestIterationLogEntry:
    def test_log_contains_type_e_556(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert "#556 Type E" in text

    def test_log_carries_thirtyfourth_label(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert "Thirty-Fourth" in text or "thirty-fourth" in text

    def test_log_carries_rotation_555_to_556(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert "555 D -> 556 E" in text

    def test_log_distinct_from_551(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#551 Type E", text, re.MULTILINE)
        assert re.search(r"^#556 Type E", text, re.MULTILINE)

    def test_log_mentions_previous_commit(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert "1a5b689" in text
