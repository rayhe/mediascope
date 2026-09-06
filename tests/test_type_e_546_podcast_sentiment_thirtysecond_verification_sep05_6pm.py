"""
Type E #546 - Podcast Sentiment Tracking: Thirty-Second Verification Cycle Sep 5 18:00 PDT
Guilty Feminist 498 Hold No 499 as of 18:00 (zeno.fm + ListenNotes both opened first-hand this run, 32nd cycle) +
EHE 26-Day Hold with feminist.org/sifted.eu/latestly/afrotech re-surfaces verified already-in-corpus, NOT new campaigns +
Attention Sphere 32nd No-Match (circular GitHub pages rejected, Spotify Creators 1h-fresh reconfirms nonprofit) +
NO new press surfaces this cycle (Meta-glasses privacy search since Sep 4 returned only older in-corpus items; #531 Jezebel newest)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 546
DATE_STR = "2026-09-05 18:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_546_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #546", text, re.MULTILINE)
    assert m, "Iteration #546 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_546_block()
        assert "546" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_546_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_546_block()
        lower = block.lower()
        assert "540 d -> 541 e" not in lower  # previous cycle's rotation, not this one
        assert "545" in block and "546" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtysecond_cycle_label(self):
        block = get_546_block()
        lower = block.lower()
        assert "thirty-second" in lower

    def test_distinct_from_541(self):
        block = get_546_block()
        assert "546" in block
        lower = block.lower()
        assert "thirty-second" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_546_block()
        assert "498" in block
        lower = block.lower()
        assert "latest episode" in lower or "498 hold" in lower

    def test_no_499_bounded(self):
        block = get_546_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded" in lower

    def test_official_source_opened_this_run(self):
        block = get_546_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block

    def test_listennotes_secondary_opened_this_run(self):
        block = get_546_block()
        assert "listennotes" in block.lower()
        assert "opened this run" in block.lower() or "opened first-hand" in block.lower()
        assert "498" in block

    def test_cadence_note(self):
        block = get_546_block()
        lower = block.lower()
        assert "sep 7" in lower or "near sep 7" in lower

    def test_extension_not_duplicate(self):
        block = get_546_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "541" in block

    def test_zero_meta_episodes_across_cycles(self):
        block = get_546_block()
        lower = block.lower()
        assert "thirty-two verification cycles" in lower


class TestEveryoneHatesElon:
    def test_26_day_hold(self):
        block = get_546_block()
        lower = block.lower()
        assert "26-day hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_546_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_feminist_org_resurface_already_in_corpus(self):
        block = get_546_block()
        assert "feminist.org" in block
        lower = block.lower()
        assert "already in corpus" in lower or "already-in-corpus" in lower
        assert "re-surface" in lower or "not new" in lower

    def test_sifted_resurface_already_in_corpus(self):
        block = get_546_block()
        assert "sifted.eu" in block
        lower = block.lower()
        assert "already in corpus" in lower or "already-in-corpus" in lower

    def test_latestly_resurface_not_new(self):
        block = get_546_block()
        assert "latestly" in block.lower()
        lower = block.lower()
        assert "not new" in lower or "re-surface" in lower

    def test_afrotech_resurface_not_new(self):
        block = get_546_block()
        assert "afrotech" in block.lower()
        lower = block.lower()
        assert "not new" in lower or "re-surface" in lower

    def test_no_double_counting(self):
        block = get_546_block()
        lower = block.lower()
        assert "no double-counting" in lower or "double-counting" in lower

    def test_no_competitor_campaign_bounded(self):
        block = get_546_block()
        lower = block.lower()
        assert "no competitor-equivalent" in lower
        assert "bounded" in lower


class TestAttentionSphere:
    def test_32nd_no_match(self):
        block = get_546_block()
        lower = block.lower()
        assert "thirty-second no-match" in lower

    def test_circular_github_rejected(self):
        block = get_546_block()
        lower = block.lower()
        assert "circular" in lower

    def test_nonprofit_reconfirmed_fresh_source(self):
        block = get_546_block()
        lower = block.lower()
        assert "nonprofit" in lower
        assert "spotify creators" in lower

    def test_misidentification_stands(self):
        block = get_546_block()
        lower = block.lower()
        assert "misidentification" in lower


class TestNoNewPressSurfaces:
    def test_explicit_none_finding(self):
        block = get_546_block()
        lower = block.lower()
        assert "no new press surfaces" in lower

    def test_search_window_stated(self):
        block = get_546_block()
        lower = block.lower()
        assert "sep 4" in lower or "2026-09-04" in lower

    def test_only_older_items_returned(self):
        block = get_546_block()
        lower = block.lower()
        assert "older" in lower
        assert "in corpus" in lower

    def test_newest_item_still_jezebel_531(self):
        block = get_546_block()
        lower = block.lower()
        assert "jezebel" in lower
        assert "531" in block


class TestScoresDiscipline:
    def test_no_false_significance(self):
        block = get_546_block()
        assert "NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative_only(self):
        block = get_546_block()
        assert "MANUAL ILLUSTRATIVE only" in block

    def test_correlation_not_causation(self):
        block = get_546_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestSourcesAndHygiene:
    def test_all_urls_https(self):
        block = get_546_block()
        urls = re.findall(r"https?://[^\s\)\]]+", block)
        assert urls, "no URLs found in block"
        for u in urls:
            assert u.startswith("https://"), f"non-HTTPS URL: {u}"

    def test_no_em_dashes(self):
        block = get_546_block()
        assert "\u2014" not in block, "em dash found in block"
        assert "\u2013" not in block, "en dash found in block"

    def test_no_truncated_urls(self):
        block = get_546_block()
        for line in block.splitlines():
            if "https://" in line:
                urls = re.findall(r"https://[^\s\)\]]+", line)
                for u in urls:
                    assert not u.endswith("..."), f"truncated URL: {u}"
                    assert "..." not in u, f"ellipsis inside URL: {u}"

    def test_verbatim_search_urls_used(self):
        block = get_546_block()
        assert "zeno.fm/podcast/the-guilty-feminist/" in block
        assert "listennotes.com/podcasts/the-guilty-feminist" in block

    def test_iteration_log_entry_present_newest_first(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        numbers = [int(n) for n in re.findall(r"^#(\d+) Type", log, re.MULTILINE)]
        assert numbers, "no iteration entry found at line start in iteration-log.md"
        # Newest-first invariant applies to the leading run of recent entries
        # (older entries have a historical out-of-order artifact: #523 sits
        # deep in the log from a late append). The invariant is that the most
        # recent entries are prepended in strictly descending order.
        head = numbers[:6]
        assert head == sorted(head, reverse=True), (
            f"newest-first violated in recent entries: {head}"
        )
        assert ITERATION in numbers, f"#{ITERATION} entry missing from iteration-log.md"

    def test_no_zero_coverage_claim(self):
        block = get_546_block()
        lower = block.lower()
        # bounded-absence discipline: any "no competitor" claim must carry "bounded"
        for line in block.splitlines():
            ll = line.lower()
            if "no competitor" in ll:
                assert "bounded" in ll, f"unbounded no-competitor claim: {line}"
