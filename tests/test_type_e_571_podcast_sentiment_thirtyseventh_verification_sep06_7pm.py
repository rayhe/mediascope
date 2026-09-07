"""
Type E #571 - Podcast Sentiment Tracking: Thirty-Seventh Verification Cycle Sep 6 19:00 PDT
Guilty Feminist 498 Hold No 499 as of 19:00 (search-result secondary, 20h crawl, 37th cycle,
cadence note 499 near Sep 7, Chortle LPF Sep 13, official site LPF next-live-show) +
EHE 28-Day Hold with Times/Engadget/LatestLY/PetaPixel/feminist.org/AfroTech/Hyperallergic
re-surfaces verified already-in-corpus via pre-commit grep, circular GitHub rejected,
NOT new campaigns, no competitor-equivalent in thirty-seven cycles +
Attention Sphere 37th No-Match (circular GitHub pages rejected, Spotify Creators 4h-fresh
reconfirms nonprofit) +
TWO new press surfaces (ET Sep 3 guardrails piece + ET Sep 1 Delhi legal notice, both
new-to-corpus, both pre-date #561 Startup Fortune newest; cited from topic-page proxy
listing, flagged) +
PetaPixel bricking in corpus and Malwarebytes NameTag as in-corpus lineage explicitly
distinguished from new surfaces
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 571
DATE_STR = "2026-09-06 19:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_571_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #571", text, re.MULTILINE)
    assert m, "Iteration #571 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_571_block()
        assert "571" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_571_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_571_block()
        lower = block.lower()
        assert "565 d -> 566 e" not in lower  # previous cycle's rotation, not this one
        assert "570 d -> 571 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtyseventh_cycle_label(self):
        block = get_571_block()
        lower = block.lower()
        assert "thirty-seventh" in lower

    def test_distinct_from_566(self):
        block = get_571_block()
        lower = block.lower()
        assert "thirty-seventh" in lower
        assert "566" in block  # references prior cycle by number, not as self

    def test_iteration_log_entry_present_and_newest(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#571 Type E", log, re.MULTILINE), "no #571 Type E entry in iteration-log.md"
        first_entry = re.search(r"^#\d+", log, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#571", "iteration-log.md is not newest-first at #571"

    def test_novelty_single_571_test_file(self):
        # Exactly one test_type_e_571 file on disk (no duplicates), per rotation convention.
        files = [p.name for p in Path(__file__).parent.glob("test_type_e_571*.py")]
        assert len(files) == 1, f"expected exactly one test_type_e_571 file, got {files}"


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_571_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_571_block()
        lower = block.lower()
        assert "no 499" in lower
        assert "bounded absence" in lower

    def test_secondary_only_disclosed(self):
        block = get_571_block()
        assert "Secondary-only" in block

    def test_listennotes_secondary_20h_crawl(self):
        block = get_571_block()
        assert "ListenNotes" in block
        assert "20 hours" in block

    def test_cadence_note_sep7(self):
        block = get_571_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()

    def test_chortle_lpf_sep13(self):
        block = get_571_block()
        assert "Sep 13" in block
        assert "London Podcast Festival" in block

    def test_official_site_lpf_next_live_show(self):
        block = get_571_block()
        assert "guiltyfeminist.com" in block
        assert "next live show" in block.lower()

    def test_zero_meta_wearables_thirtyseven_cycles(self):
        block = get_571_block()
        lower = block.lower()
        assert "zero meta/wearables episodes across all thirty-seven" in lower

    def test_extension_not_duplicate(self):
        block = get_571_block()
        lower = block.lower()
        assert "extends #566 by 5 hours" in lower
        assert "not duplicate" in lower


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_571_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_571_block()
        assert "activist group, not a podcast" in block

    def test_times_epstein_resurface(self):
        block = get_571_block()
        assert "slx3wttm5" in block
        assert "42 days" in block

    def test_latestly_resurface(self):
        block = get_571_block()
        assert "latestly.com" in block
        assert "39 days" in block

    def test_engadget_resurface(self):
        block = get_571_block()
        assert "2217151" in block
        assert "52 days" in block

    def test_petapixel_resurface(self):
        block = get_571_block()
        assert "petapixel.com/2026/07/23" in block
        assert "46 days" in block

    def test_feminist_org_resurface_updated(self):
        block = get_571_block()
        assert "feminist.org" in block
        assert "#470" in block
        assert "updated 6 days" in block

    def test_afrotech_resurface(self):
        block = get_571_block()
        assert "afrotech.com" in block
        assert "52 days" in block

    def test_hyperallergic_resurface(self):
        block = get_571_block()
        assert "guerrilla-london-bus-ads" in block
        assert "54 days" in block

    def test_no_new_primary_motif(self):
        block = get_571_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_571_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "thirty-seven verification cycles" in lower

    def test_no_double_counting(self):
        block = get_571_block()
        assert "No double-counting" in block


class TestAttentionSphereNoMatch:
    def test_37th_no_match(self):
        block = get_571_block()
        lower = block.lower()
        assert "thirty-seventh no-match" in lower

    def test_circular_github_rejected(self):
        block = get_571_block()
        assert "circular" in block.lower()
        assert "github" in block.lower()

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_571_block()
        assert "anita-nowak" in block
        assert "non-profit organization" in block
        assert "4 hours" in block

    def test_actual_podcast_named(self):
        block = get_571_block()
        assert "Left to Their Own Devices" in block

    def test_status_unchanged_misidentified(self):
        block = get_571_block()
        lower = block.lower()
        assert "misidentified" in lower


class TestNewPressSurfaces:
    def test_two_new_surfaces(self):
        block = get_571_block()
        lower = block.lower()
        assert "two new-to-corpus" in lower
        assert "two new press surfaces" in lower

    def test_et_guardrails_sep3(self):
        block = get_571_block()
        lower = block.lower()
        assert "meta puts guardrails in place" in lower
        assert "sep 3, 2026" in lower
        assert "recording light is tampered with" in lower

    def test_et_delhi_legal_notice_sep1(self):
        block = get_571_block()
        lower = block.lower()
        assert "delhi man" in lower
        assert "2.05 crore" in lower
        assert "sep 1, 2026" in lower
        assert "internet freedom foundation" in lower

    def test_proxy_listing_flagged(self):
        block = get_571_block()
        lower = block.lower()
        assert "topic-page proxy" in lower
        assert "not a direct article url" in lower

    def test_newest_remains_561_startup_fortune(self):
        block = get_571_block()
        lower = block.lower()
        assert "newest in-corpus surface" in lower
        assert "#561 startup fortune" in lower

    def test_petapixel_bricking_in_corpus_not_new(self):
        block = get_571_block()
        lower = block.lower()
        assert "petapixel sep 1" in lower or "petapixel" in lower
        assert "in corpus" in lower

    def test_malwarebytes_nametag_lineage_not_new_surface(self):
        block = get_571_block()
        lower = block.lower()
        assert "malwarebytes" in lower
        assert "not a new surface" in lower

    def test_norway_older_not_counted(self):
        block = get_571_block()
        lower = block.lower()
        assert "norway" in lower
        assert "not in corpus" in lower


class TestScoresAndDiscipline:
    def test_not_calculated(self):
        block = get_571_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative(self):
        block = get_571_block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_ehe_posture_8_of_10(self):
        block = get_571_block()
        assert "-8/10" in block

    def test_no_false_significance(self):
        block = get_571_block()
        lower = block.lower()
        assert "do not claim empirical significance" in lower


class TestSources:
    def test_verbatim_urls_present(self):
        block = get_571_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block
        assert "https://creators.spotify.com/pod/profile/anita-nowak/" in block

    def test_proxy_url_preserved_verbatim(self):
        block = get_571_block()
        assert "https://appwritefunc.yet-another-testing-domain.com/api/grab?url=https://economictimes.indiatimes.com/topic/meta-smart-glasses" in block

    def test_http_listing_preserved_verbatim(self):
        block = get_571_block()
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block

    def test_no_em_dashes(self):
        block = get_571_block()
        assert "‑" not in block, "em dash found in #571 block"
        assert "–" not in block, "en dash found in #571 block"


class TestConfounders:
    def test_confounders_ranked(self):
        block = get_571_block()
        assert block.count("- STRONG") >= 5
        assert block.count("- MODERATE") >= 3

    def test_snippet_bounded_strong(self):
        block = get_571_block()
        lower = block.lower()
        assert "snippet-bounded search results" in lower

    def test_secondary_only_strong(self):
        block = get_571_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_topic_page_proxy_strong(self):
        block = get_571_block()
        lower = block.lower()
        assert "topic-page listing" in lower

    def test_five_hour_cadence_strong(self):
        block = get_571_block()
        lower = block.lower()
        assert "five-hour cadence" in lower

    def test_not_calculated_on_confounders(self):
        block = get_571_block()
        assert "NOT_CALCULATED" in block
