"""
Type E #576 - Podcast Sentiment Tracking: Thirty-Eighth Verification Cycle Sep 7 01:00 PDT
Guilty Feminist 498 Hold No 499 (Audible UK 4d-crawl secondary, #561 penciled 499 for
Sep 7 not surfaced by 01:00, Ivy.fm 1d crawl Sep 5 event past + Sep 13 Kings Place LPF,
weekly cadence, secondary-only tier disclosed) +
EHE 28-Day Hold with LatestLY/Engadget/feminist.org/AfroTech/PetaPixel re-surfaces
verified already-in-corpus via pre-commit grep, circular GitHub rejected,
NOT new campaigns, no double-counting, no competitor-equivalent in thirty-eight cycles +
Attention Sphere 38th No-Match (circular GitHub pages rejected, Spotify Creators 10h-fresh
reconfirms nonprofit) +
TWO new press surfaces (Bloomberg Law false-ad class suit ND Cal naming Luxottica,
Kenyan-subcontractor labeling allegation, paywalled snippet-bounded; Startup Fortune
Sep 1 Semafor re-report on LED-tamper bricking; both new-to-corpus via zero-hit greps,
both pre-date #561 Startup Fortune newest) +
FastCo 91571430 explicitly distinguished as the in-corpus Jul 10 roundup (content 59 days
old), PetaPixel/Livemint/DigitalTrends in-corpus lineage distinguished from new surfaces,
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs incl
WWW.ENGADGET.COM listing as surfaced, distinct from 571, iteration-log entry present
and newest-first.
"""
import re
from pathlib import Path
from subprocess import run

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 576
DATE_STR = "2026-09-07 01:00 PDT"
TEST_FILE = Path(__file__).name


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_576_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #576", text, re.MULTILINE)
    assert m, "Iteration #576 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_576_block()
        assert "576" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_576_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_576_block()
        lower = block.lower()
        assert "570 d -> 571 e" not in lower  # previous cycle's rotation, not this one
        assert "575 d -> 576 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtyeighth_cycle_label(self):
        block = get_576_block()
        lower = block.lower()
        assert "thirty-eighth" in lower

    def test_distinct_from_571(self):
        block = get_576_block()
        lower = block.lower()
        assert "extends #571 by 6 hours" in lower
        assert "not duplicate" in lower
        assert "distinct from 571" in lower

    def test_iteration_log_entry_present_and_newest(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#576 Type E", log, re.MULTILINE), "no #576 Type E entry in iteration-log.md"
        first_entry = re.search(r"^#\d+", log, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#576", "iteration-log.md is not newest-first at #576"

    def test_novelty_single_576_test_file(self):
        files = list((REPO_ROOT / "tests").glob("test_type_e_576*"))
        assert len(files) == 1, f"expected exactly one 576 test file, got {files}"
        assert files[0].name == TEST_FILE


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_576_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_576_block()
        lower = block.lower()
        assert "no episode 499" in lower
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_576_block()
        assert "secondary-only" in block.lower()
        assert "Stated explicitly" in block

    def test_audible_uk_4d_crawl(self):
        block = get_576_block()
        assert "Audible UK" in block
        assert "crawled 4 days" in block

    def test_cadence_note_sep7(self):
        block = get_576_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()
        assert "01:00" in block

    def test_561_penciled_499_not_surfaced(self):
        block = get_576_block()
        lower = block.lower()
        assert "561" in block
        assert "penciled 499" in lower
        assert "has not appeared" in lower

    def test_chortle_sep13(self):
        block = get_576_block()
        assert "Sep 13" in block
        assert "London Podcast Festival" in block

    def test_ivy_fm_sep5_past_sep13_next(self):
        block = get_576_block()
        assert "Ivy.fm" in block
        assert "1 day" in block or "1-day" in block
        assert "Sep 5" in block
        assert "Kings Place" in block


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_576_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_576_block()
        assert "activist group, not a podcast" in block

    def test_latestly_resurface(self):
        block = get_576_block()
        assert "latestly.com" in block
        assert "39 days" in block

    def test_engadget_resurface(self):
        block = get_576_block()
        assert "2217151" in block
        assert "52 days" in block

    def test_petapixel_resurface(self):
        block = get_576_block()
        assert "petapixel.com/2026/07/23" in block
        assert "46 days" in block

    def test_feminist_org_resurface_updated(self):
        block = get_576_block()
        assert "feminist.org" in block
        assert "updated 6 days" in block
        assert "crawled 1 hour" in block

    def test_afrotech_resurface(self):
        block = get_576_block()
        assert "afrotech.com" in block
        assert "52 days" in block
        assert "10 hours" in block

    def test_no_new_primary_motif(self):
        block = get_576_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_576_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "thirty-eight verification cycles" in lower

    def test_no_double_counting(self):
        block = get_576_block()
        assert "No double-counting" in block


class TestAttentionSphereNoMatch:
    def test_38th_no_match(self):
        block = get_576_block()
        lower = block.lower()
        assert "thirty-eighth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_576_block()
        assert "circular" in block.lower()
        assert "github" in block.lower()

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_576_block()
        assert "anita-nowak" in block
        assert "non-profit organization" in block
        assert "10 hours" in block

    def test_actual_podcast_named(self):
        block = get_576_block()
        assert "Left to Their Own Devices" in block

    def test_status_unchanged_misidentified(self):
        block = get_576_block()
        lower = block.lower()
        assert "misidentified" in lower


class TestNewPressSurfaces:
    def test_two_new_surfaces(self):
        block = get_576_block()
        lower = block.lower()
        assert "two new-to-corpus" in lower
        assert "two new press surfaces" in lower

    def test_bloomberglaw_false_ad_class_suit(self):
        block = get_576_block()
        lower = block.lower()
        assert "meta faces false ad suit over ai glasses privacy promise" in lower
        assert "luxottica" in lower
        assert "northern district of california" in lower
        assert "designed for privacy" in lower
        assert "kenya" in lower

    def test_bloomberglaw_zero_hit_greps(self):
        block = get_576_block()
        lower = block.lower()
        assert "false-ad-suit" in lower
        assert "meta-faces-false-ad" in lower
        assert "zero repo hits" in lower

    def test_bloomberglaw_paywalled_bounded(self):
        block = get_576_block()
        lower = block.lower()
        assert "paywalled" in lower
        assert "search-result snippet" in lower

    def test_startupfortune_bricking_sep1(self):
        block = get_576_block()
        lower = block.lower()
        assert "meta-permanently-disables-cameras" in lower
        assert "semafor" in lower
        assert "<0.1%" in lower
        assert "7,000" in lower

    def test_startupfortune_zero_hit_greps(self):
        block = get_576_block()
        lower = block.lower()
        assert "startupfortune.com/meta-permanently" in lower

    def test_distinct_from_561_kenyan_contractors(self):
        block = get_576_block()
        lower = block.lower()
        assert "distinct claim class" in lower
        assert "kenyan-contractors" in lower

    def test_newest_remains_561_startup_fortune(self):
        block = get_576_block()
        lower = block.lower()
        assert "newest in-corpus surface" in lower
        assert "#561 startup fortune" in lower

    def test_fastco_91571430_not_new_distinguished(self):
        block = get_576_block()
        lower = block.lower()
        assert "fastcompany.com/91571430" in lower
        assert "in-corpus jul 10 roundup" in lower
        assert "59 days" in lower

    def test_petapixel_bricking_in_corpus_not_new(self):
        block = get_576_block()
        lower = block.lower()
        assert "petapixel sep 1" in lower
        assert "in corpus" in lower

    def test_livemint_digitaltrends_in_corpus_lineage(self):
        block = get_576_block()
        lower = block.lower()
        assert "livemint" in lower
        assert "digitaltrends" in lower


class TestScoresAndDiscipline:
    def test_not_calculated(self):
        block = get_576_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative(self):
        block = get_576_block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_ehe_posture_8_of_10(self):
        block = get_576_block()
        assert "-8/10" in block

    def test_no_false_significance(self):
        block = get_576_block()
        lower = block.lower()
        assert "do not claim empirical significance" in lower


class TestSources:
    def test_verbatim_urls_present(self):
        block = get_576_block()
        assert "https://news.bloomberglaw.com/litigation/meta-faces-false-ad-suit-over-ai-glasses-privacy-promise" in block
        assert "https://startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses/" in block
        assert "https://creators.spotify.com/pod/profile/anita-nowak/" in block

    def test_engadget_verbatim_uppercase_preserved(self):
        block = get_576_block()
        assert "https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in block

    def test_fastco_url_present(self):
        block = get_576_block()
        assert "https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses" in block

    def test_no_em_dashes(self):
        block = get_576_block()
        assert "—" not in block, "em dash found in #576 block"
        assert "–" not in block, "en dash found in #576 block"


class TestConfounders:
    def test_confounders_ranked(self):
        block = get_576_block()
        assert block.count("- STRONG") >= 5
        assert block.count("- MODERATE") >= 3

    def test_snippet_bounded_strong(self):
        block = get_576_block()
        lower = block.lower()
        assert "snippet-bounded search results" in lower

    def test_secondary_only_strong(self):
        block = get_576_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_paywalled_search_listing_strong(self):
        block = get_576_block()
        lower = block.lower()
        assert "paywalled" in lower
        assert "not direct page opens" in lower

    def test_five_hour_cadence_strong(self):
        block = get_576_block()
        lower = block.lower()
        assert "five-hour cadence" in lower

    def test_not_calculated_on_confounders(self):
        block = get_576_block()
        assert "NOT_CALCULATED" in block
