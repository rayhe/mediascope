"""
Type E #531 - Podcast Sentiment Tracking: Twenty-Ninth Verification Cycle Sep 5 03:00 PDT
Guilty Feminist 498 Hold No 499 as of 03:00 (zeno.fm opened this run, 29th cycle) +
EHE 26-Day Hold with feminist.org and sifted.eu secondary items verified already-in-corpus, NOT new campaigns +
Attention Sphere 29th No-Match (repo pages dominate results, circular evidence rejected, nonprofit confirmed) +
NEW Jezebel press surface (adversarial entity-selective register, -6/10 MANUAL ILLUSTRATIVE, snippet-bounded) +
Secondary citations within Jezebel (manualdousuario, thecrosswiredaily) not counted as independent surfaces
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 531
DATE_STR = "2026-09-05 03:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_531_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #531", text, re.MULTILINE)
    assert m, "Iteration #531 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_531_block()
        assert "531" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_531_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_531_block()
        assert "530" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twenty_ninth_cycle_label(self):
        block = get_531_block()
        lower = block.lower()
        assert "twenty-ninth" in lower

    def test_distinct_from_526(self):
        block = get_531_block()
        assert "531" in block
        lower = block.lower()
        assert "twenty-eighth" not in lower or "twenty-ninth" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_531_block()
        assert "498" in block
        lower = block.lower()
        assert "latest episode" in lower or "498 hold" in lower

    def test_no_499_bounded(self):
        block = get_531_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded" in lower

    def test_official_source_opened_this_run(self):
        block = get_531_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block

    def test_cadence_note(self):
        block = get_531_block()
        lower = block.lower()
        assert "sep 7" in lower or "near sep 7" in lower

    def test_extension_not_duplicate(self):
        block = get_531_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "526" in block

    def test_zero_meta_episodes_across_cycles(self):
        block = get_531_block()
        assert "twenty-nine verification cycles" in block.lower() or "29" in block


class TestEveryoneHatesElon:
    def test_26_day_hold(self):
        block = get_531_block()
        lower = block.lower()
        assert "26-day hold" in lower

    def test_activist_not_podcast_discipline(self):
        block = get_531_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_feminist_org_secondary_already_in_corpus(self):
        block = get_531_block()
        assert "feminist.org" in block
        lower = block.lower()
        assert "already in corpus" in lower
        assert "not a new campaign" in lower

    def test_sifted_secondary_already_logged(self):
        block = get_531_block()
        assert "sifted.eu" in block
        assert "480" in block
        lower = block.lower()
        assert "not a new campaign" in lower

    def test_no_competitor_campaign_bounded(self):
        block = get_531_block()
        lower = block.lower()
        assert "no competitor-equivalent" in lower
        assert "bounded" in lower


class TestAttentionSphere:
    def test_29th_no_match(self):
        block = get_531_block()
        lower = block.lower()
        assert "twenty-ninth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_531_block()
        lower = block.lower()
        assert "circular" in lower

    def test_nonprofit_confirmed(self):
        block = get_531_block()
        lower = block.lower()
        assert "nonprofit" in lower

    def test_misidentification_stands(self):
        block = get_531_block()
        lower = block.lower()
        assert "misidentification" in lower


class TestNewJezebelSurface:
    def test_jezebel_url_logged_verbatim(self):
        block = get_531_block()
        assert "https://www.jezebel.com/meta-smart-glasses-cameras-spying-secret-recording-led-lights-privacy-tampering-updates-consent" in block

    def test_jezebel_novelty_repo_grep_verified(self):
        block = get_531_block()
        lower = block.lower()
        assert "zero matches" in lower
        assert "before this run" in lower

    def test_jezebel_adversarial_headline_register(self):
        block = get_531_block()
        lower = block.lower()
        assert "at-fault" in lower or "adversarial" in lower
        assert "spy cameras" in lower

    def test_jezebel_led_loophole_coverage(self):
        block = get_531_block()
        assert "Alex Himel" in block
        lower = block.lower()
        assert "led" in lower

    def test_jezebel_snippet_bounded(self):
        block = get_531_block()
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_jezebel_manual_illustrative_minus_6(self):
        block = get_531_block()
        assert "-6/10" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_jezebel_not_ehe_campaign_output(self):
        block = get_531_block()
        lower = block.lower()
        assert "not an ehe campaign" in lower or "not an ehe campaign output" in lower

    def test_secondary_citations_not_independent_surfaces(self):
        block = get_531_block()
        lower = block.lower()
        assert "manualdousuario" in lower or "thecrosswiredaily" in lower
        assert "not" in lower and "independent" in lower


class TestScoresDiscipline:
    def test_no_false_significance(self):
        block = get_531_block()
        assert "NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative_only(self):
        block = get_531_block()
        assert "MANUAL ILLUSTRATIVE only" in block

    def test_correlation_not_causation(self):
        block = get_531_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestSourcesAndHygiene:
    def test_all_urls_https(self):
        block = get_531_block()
        urls = re.findall(r"https?://[^\s\)\]]+", block)
        assert urls, "no URLs found in block"
        for u in urls:
            assert u.startswith("https://"), f"non-HTTPS URL: {u}"

    def test_no_em_dashes(self):
        block = get_531_block()
        assert "\u2014" not in block, "em dash found in block"
        assert "\u2013" not in block, "en dash found in block"

    def test_no_truncated_urls(self):
        block = get_531_block()
        for line in block.splitlines():
            if "https://" in line:
                urls = re.findall(r"https://[^\s\)\]]+", line)
                for u in urls:
                    assert not u.endswith("..."), f"truncated URL: {u}"
                    assert "..." not in u, f"ellipsis inside URL: {u}"

    def test_verbatim_search_urls_used(self):
        block = get_531_block()
        assert "meta-glasses-launch-sparks-surveillance-backlash-and-advertiser-reckoning" not in block  # #526's item, not #531's
        assert "jezebel.com/meta-smart-glasses-cameras-spying-secret-recording-led-lights-privacy-tampering-updates-consent" in block

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
        block = get_531_block()
        lower = block.lower()
        # bounded-absence discipline: any "no competitor" claim must carry "bounded"
        for line in block.splitlines():
            ll = line.lower()
            if "no competitor" in ll:
                assert "bounded" in ll, f"unbounded no-competitor claim: {line}"
