"""
Type E #566 - Podcast Sentiment Tracking: Thirty-Sixth Verification Cycle Sep 6 14:00 PDT
Guilty Feminist 498 Hold No 499 as of 14:00 (search-result secondary, 15h crawl, 36th cycle,
cadence note 499 near Sep 7, Chortle LPF Sep 13, official site LPF next-live-show) +
EHE 28-Day Hold with Times/LatestLY/Engadget/PetaPixel/feminist.org/AfroTech/Hyperallergic
re-surfaces verified already-in-corpus via pre-commit grep, circular GitHub rejected,
NOT new campaigns, no competitor-equivalent in thirty-six cycles +
Attention Sphere 36th No-Match (circular GitHub pages rejected, Spotify Creators 8h-fresh
reconfirms nonprofit) +
ZERO new press surfaces this cycle (wearables-sweep returns itemized; three older hardware-launch
items explicitly not-in-corpus and NOT new surfaces; newest in-corpus surface remains #561
Startup Fortune Kenyan-contractors re-report ~Sep 5)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 566
DATE_STR = "2026-09-06 14:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_566_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #566", text, re.MULTILINE)
    assert m, "Iteration #566 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_566_block()
        assert "566" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_566_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_566_block()
        lower = block.lower()
        assert "560 d -> 561 e" not in lower  # previous cycle's rotation, not this one
        assert "565 d -> 566 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtysixth_cycle_label(self):
        block = get_566_block()
        lower = block.lower()
        assert "thirty-sixth" in lower

    def test_distinct_from_561(self):
        block = get_566_block()
        lower = block.lower()
        assert "thirty-sixth" in lower
        assert "561" in block  # references prior cycle by number, not as self

    def test_iteration_log_entry_present_and_newest(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#566 Type E", log, re.MULTILINE), "no #566 Type E entry in iteration-log.md"
        first_entry = re.search(r"^#\d+", log, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#566", "iteration-log.md is not newest-first at #566"

    def test_novelty_single_566_test_file(self):
        # Exactly one test_type_e_566 file on disk (no duplicates), per rotation convention.
        files = [p.name for p in Path(__file__).parent.glob("test_type_e_566*.py")]
        assert len(files) == 1, f"expected exactly one test_type_e_566 file, got {files}"


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_566_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_566_block()
        lower = block.lower()
        assert "no 499" in lower
        assert "bounded absence" in lower

    def test_secondary_only_disclosed(self):
        block = get_566_block()
        assert "Secondary-only" in block

    def test_listennotes_secondary_15h_crawl(self):
        block = get_566_block()
        assert "ListenNotes" in block
        assert "15 hours" in block

    def test_cadence_note_sep7(self):
        block = get_566_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()

    def test_chortle_lpf_sep13(self):
        block = get_566_block()
        assert "Sep 13" in block
        assert "London Podcast Festival" in block

    def test_official_site_lpf_next_live_show(self):
        block = get_566_block()
        assert "guiltyfeminist.com" in block
        assert "next live show" in block.lower()

    def test_zero_meta_wearables_thirtysix_cycles(self):
        block = get_566_block()
        lower = block.lower()
        assert "zero meta/wearables episodes across all thirty-six" in lower

    def test_extension_not_duplicate(self):
        block = get_566_block()
        lower = block.lower()
        assert "extends #561 by 5 hours" in lower
        assert "not duplicate" in lower


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_566_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_566_block()
        assert "activist group, not a podcast" in block

    def test_times_epstein_resurface(self):
        block = get_566_block()
        assert "slx3wttm5" in block
        assert "42 days" in block

    def test_latestly_resurface(self):
        block = get_566_block()
        assert "latestly.com" in block
        assert "38 days" in block

    def test_engadget_resurface(self):
        block = get_566_block()
        assert "2217151" in block
        assert "51 days" in block

    def test_petapixel_resurface(self):
        block = get_566_block()
        assert "petapixel.com/2026/07/23" in block
        assert "45 days" in block

    def test_feminist_org_resurface(self):
        block = get_566_block()
        assert "feminist.org" in block
        assert "#470" in block

    def test_afrotech_resurface(self):
        block = get_566_block()
        assert "afrotech.com" in block
        assert "51 days" in block

    def test_hyperallergic_resurface(self):
        block = get_566_block()
        assert "guerrilla-london-bus-ads" in block
        assert "53 days" in block

    def test_no_new_primary_motif(self):
        block = get_566_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_566_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "thirty-six verification cycles" in lower

    def test_no_double_counting(self):
        block = get_566_block()
        assert "No double-counting" in block


class TestAttentionSphereNoMatch:
    def test_36th_no_match(self):
        block = get_566_block()
        lower = block.lower()
        assert "thirty-sixth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_566_block()
        assert "circular" in block.lower()
        assert "github" in block.lower()

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_566_block()
        assert "anita-nowak" in block
        assert "non-profit organization" in block
        assert "8 hours" in block

    def test_actual_podcast_named(self):
        block = get_566_block()
        assert "Left to Their Own Devices" in block

    def test_status_unchanged_misidentified(self):
        block = get_566_block()
        lower = block.lower()
        assert "misidentified" in lower


class TestNewPressSurface:
    def test_zero_new_surfaces(self):
        block = get_566_block()
        lower = block.lower()
        assert "zero new" in lower

    def test_three_not_in_corpus_items_distinguished(self):
        block = get_566_block()
        lower = block.lower()
        assert "not-in-corpus" in lower
        assert "meta-debuts-new-cheaper-smart-glasses" in lower
        assert "meta-launches-its-own-299-smart-glasses" in lower
        assert "2184224" in lower

    def test_not_in_corpus_not_counted_as_discovery(self):
        block = get_566_block()
        lower = block.lower()
        assert "not double-counted as discoveries" in lower

    def test_newest_remains_561_startup_fortune(self):
        block = get_566_block()
        lower = block.lower()
        assert "newest in-corpus surface remains the #561 startup fortune" in lower

    def test_in_corpus_sweep_items_itemized(self):
        block = get_566_block()
        lower = block.lower()
        assert "thestreet" in lower
        assert "270 days" in lower
        assert "161 days" in lower
        assert "globenewswire" in lower


class TestScoresAndDiscipline:
    def test_not_calculated(self):
        block = get_566_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative(self):
        block = get_566_block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_ehe_posture_8_of_10(self):
        block = get_566_block()
        assert "-8/10" in block

    def test_no_false_significance(self):
        block = get_566_block()
        lower = block.lower()
        assert "do not claim empirical significance" in lower


class TestSources:
    def test_verbatim_urls_present(self):
        block = get_566_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block
        assert "https://creators.spotify.com/pod/profile/anita-nowak/" in block

    def test_http_listing_preserved_verbatim(self):
        block = get_566_block()
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block

    def test_no_em_dashes(self):
        block = get_566_block()
        assert "\u2014" not in block, "em dash found in #566 block"
        assert "\u2013" not in block, "en dash found in #566 block"


class TestConfounders:
    def test_six_confounders_ranked(self):
        block = get_566_block()
        assert block.count("- STRONG") >= 4
        assert block.count("- MODERATE") >= 2

    def test_snippet_bounded_strong(self):
        block = get_566_block()
        lower = block.lower()
        assert "snippet-bounded search results" in lower

    def test_secondary_only_strong(self):
        block = get_566_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_five_hour_cadence_strong(self):
        block = get_566_block()
        lower = block.lower()
        assert "five-hour cadence" in lower

    def test_not_calculated_on_confounders(self):
        block = get_566_block()
        assert "NOT_CALCULATED" in block
