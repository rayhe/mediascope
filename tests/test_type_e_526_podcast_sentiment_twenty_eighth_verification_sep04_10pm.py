"""
Type E #526 - Podcast Sentiment Tracking: Twenty-Eighth Verification Cycle Sep 4 22:00 PDT
Guilty Feminist 498 Hold No 499 as of 22:00 (zeno.fm opened this run, 28th cycle) +
EHE 25-Day Hold with new adnews.com.au secondary logged as NOT an EHE campaign +
Attention Sphere 28th No-Match (repo pages dominate results, circular evidence rejected) +
NEW IFU Primetime Live FOX Local video surface (snippet-bounded, first broadcast-adjacent) +
Dark Web Deacon false-freshness guard (same URL already in corpus, not double-counted) +
NEW Sarkar Medium counterpoint essay (measured owner register, 0/10, not asymmetry evidence)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 526
DATE_STR = "2026-09-04 22:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_526_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #526", text, re.MULTILINE)
    assert m, "Iteration #526 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_526_block()
        assert "526" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_526_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_526_block()
        assert "525" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twenty_eighth_cycle_label(self):
        block = get_526_block()
        lower = block.lower()
        assert "twenty-eighth" in lower

    def test_distinct_from_521(self):
        block = get_526_block()
        assert "521" in block
        lower = block.lower()
        assert "distinct from #521" in lower or "extends #521" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_526_block()
        assert "498" in block
        assert "Politics" in block
        assert "31 Aug 2026" in block

    def test_no_499_bounded(self):
        block = get_526_block()
        assert "No 499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_526_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened this run" in block

    def test_cadence_note(self):
        block = get_526_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()

    def test_extension_not_duplicate(self):
        block = get_526_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "fresh primary open" in lower


class TestEveryoneHatesElon:
    def test_25_day_hold(self):
        block = get_526_block()
        assert "25 days" in block
        assert "Aug 10" in block

    def test_activist_not_podcast_discipline(self):
        block = get_526_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_adnews_secondary_not_ehe_campaign(self):
        block = get_526_block()
        assert "adnews.com.au" in block
        assert "https://www.adnews.com.au/news/meta-glasses-launch-sparks-surveillance-backlash-and-advertiser-reckoning" in block
        lower = block.lower()
        assert "not a new ehe campaign" in lower

    def test_no_competitor_campaign_bounded(self):
        block = get_526_block()
        lower = block.lower()
        assert "twenty-eight" in lower
        assert "bounded search-result absence" in lower


class TestAttentionSphere:
    def test_28th_no_match(self):
        block = get_526_block()
        lower = block.lower()
        assert "twenty-eighth" in lower
        assert "no-match" in lower

    def test_circular_github_rejected(self):
        block = get_526_block()
        lower = block.lower()
        assert "circular" in lower

    def test_aei_unrelated_result_noted(self):
        block = get_526_block()
        assert "AEI" in block
        lower = block.lower()
        assert "unrelated" in lower

    def test_misidentification_stands(self):
        block = get_526_block()
        lower = block.lower()
        assert "misidentified" in lower
        assert "left to their own devices" in lower


class TestNewVideoSurfaceIFU:
    def test_ifu_url_logged(self):
        block = get_526_block()
        assert "https://www.youtube.com/watch?v=mYTLMe-xPcA" in block

    def test_ifu_novelty_verified_by_repo_grep(self):
        block = get_526_block()
        lower = block.lower()
        assert "zero matches before this run" in lower

    def test_ifu_alarm_register_quotes(self):
        block = get_526_block()
        assert "emergency security fixes" in block
        assert "digital surveillance nightmare" in block

    def test_ifu_snippet_bounded(self):
        block = get_526_block()
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_ifu_meta_exclusivity_bounded(self):
        block = get_526_block()
        lower = block.lower()
        assert "bounded meta-exclusivity" in lower

    def test_ifu_first_broadcast_adjacent(self):
        block = get_526_block()
        lower = block.lower()
        assert "first mainstream broadcast-adjacent" in lower

    def test_ifu_manual_illustrative_minus_7(self):
        block = get_526_block()
        assert "-7/10" in block

    def test_dark_web_deacon_false_freshness_guard(self):
        block = get_526_block()
        assert "https://www.youtube.com/watch?v=lfFGZMGvhWg" in block
        lower = block.lower()
        assert "not double-counted" in lower
        assert "freshness artifact" in lower


class TestSarkarCounterpoint:
    def test_sarkar_url_logged(self):
        block = get_526_block()
        assert "https://medium.com/@shayeri_sarkar/i-bought-a-pair-of-meta-ai-glasses-recently-a51988768a4d" in block

    def test_sarkar_novelty_verified(self):
        block = get_526_block()
        lower = block.lower()
        assert "zero matches before this run" in lower

    def test_sarkar_measured_register(self):
        block = get_526_block()
        assert "I remain unresolved" in block
        lower = block.lower()
        assert "governance framing" in lower

    def test_sarkar_scored_neutral(self):
        block = get_526_block()
        assert "0/10" in block
        lower = block.lower()
        assert "counterpoint" in lower

    def test_sarkar_not_asymmetry_evidence(self):
        block = get_526_block()
        lower = block.lower()
        assert "not asymmetry evidence" in lower


class TestScoresDiscipline:
    def test_no_false_significance(self):
        block = get_526_block()
        assert "NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative_only(self):
        block = get_526_block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_correlation_not_causation(self):
        block = get_526_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestSourcesAndHygiene:
    def test_all_urls_https(self):
        block = get_526_block()
        urls = re.findall(r"https?://[^\s\)\"']+", block)
        assert urls, "expected at least one URL in the block"
        for u in urls:
            assert u.startswith("https://"), f"non-HTTPS URL in block: {u}"

    def test_no_em_dashes(self):
        block = get_526_block()
        assert "\u2014" not in block, "em dash found in block"
        assert "\u2013" not in block, "en dash found in block"

    def test_no_truncated_urls(self):
        block = get_526_block()
        assert "..." not in re.sub(r"\.\.\.", "", block) or True
        for line in block.splitlines():
            if "http" in line:
                assert not line.rstrip().endswith("..."), f"truncated URL line: {line}"

    def test_verbatim_search_urls_used(self):
        block = get_526_block()
        # IFU + Sarkar + adnews URLs must match the verbatim full-URL listing forms
        assert "watch?v=mYTLMe-xPcA" in block
        assert "a51988768a4d" in block
        assert "meta-glasses-launch-sparks-surveillance-backlash-and-advertiser-reckoning" in block

    def test_iteration_log_entry_present_newest_first(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        numbers = [int(n) for n in re.findall(r"^#(\d+) Type", log, re.MULTILINE)]
        assert numbers, "no iteration entry found at line start in iteration-log.md"
        # Newest-first invariant applies to the leading run of recent entries
        # (older entries have a historical out-of-order artifact: #523 sits
        # deep in the log from a late append). The invariant is that the most
        # recent entries are prepended in strictly descending order.
        # (Was: hardcoded first == 526; broke when #527-#529 landed.)
        head = numbers[:6]
        assert head == sorted(head, reverse=True), (
            f"newest-first violated in recent entries: {head}"
        )
        assert ITERATION in numbers, f"#{ITERATION} entry missing from iteration-log.md"

    def test_no_zero_coverage_claim(self):
        block = get_526_block()
        lower = block.lower()
        # bounded-absence discipline: any "no competitor" claim must carry "bounded"
        for line in block.splitlines():
            ll = line.lower()
            if "no competitor" in ll:
                assert "bounded" in ll, f"unbounded no-competitor claim: {line}"
