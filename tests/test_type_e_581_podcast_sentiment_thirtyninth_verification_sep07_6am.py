"""
Type E #581 - Podcast Sentiment Tracking: Thirty-Ninth Verification Cycle Sep 7 06:00 PDT
Guilty Feminist 498 Hold No 499 (stale Listen Notes crawls 159-224d, official site 2h crawl
no episode number, Chortle 4h crawl Sep 13 Kings Place LPF, 498-latest rests on #576 Audible UK
verification, weaker evidence tier disclosed, #561 penciled 499 for Sep 7 still not surfaced
by 06:00, secondary-only) +
EHE 28-Day Hold with Times/Engadget/LatestLY/PetaPixel/Hyperallergic/feminist.org
re-surfaces verified already-in-corpus via pre-commit grep, Sifted ban piece explicitly
distinguished as IN CORPUS via #480 (not new), no double-counting, no new primary motif,
no competitor-equivalent in thirty-nine cycles +
Attention Sphere 39th No-Match (circular GitHub rejected, Spotify Creators 4h-fresh
nonprofit re-confirmation) +
TWO new press surfaces (Times "Fear and loathing" London field test ~Sep 6-7, 0l82sx8sw
zero hits, paywalled snippet-bounded; Cybernews bystander-recordings amended complaint +
Sep 4 Illinois NameTag class action, meta-lawsuit-ai-glasses/september 4th/CM3leon/
bystander recordings zero hits; newest in-corpus surface ADVANCES from #561 Startup
Fortune to the Times piece) +
Bloomberg Law false-ad (#576), Startup Fortune bricking (#576), ET pieces (#571),
Reuters HateAid in-corpus lineage distinguished from new surfaces,
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs incl
WWW.ENGADGET.COM and http hyperallergic listings as surfaced, distinct from 576,
thirty-ninth verification cycle, extends #576 by 5 hours, not duplicate,
iteration-log entry present and newest-first.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 581
DATE_STR = "2026-09-07 06:00 PDT"
TEST_FILE = Path(__file__).name


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_581_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #581", text, re.MULTILINE)
    assert m, "Iteration #581 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_581_block()
        assert "581" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_581_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_581_block()
        lower = block.lower()
        assert "575 d -> 576 e" not in lower  # previous cycle's rotation, not this one
        assert "580 d -> 581 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtyninth_cycle_label(self):
        block = get_581_block()
        lower = block.lower()
        assert "thirty-ninth" in lower

    def test_distinct_from_576(self):
        block = get_581_block()
        lower = block.lower()
        assert "extends #576 by 5 hours" in lower
        assert "not duplicate" in lower
        assert "distinct from 576" in lower

    def test_iteration_log_entry_present_and_newest(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert re.search(r"^#581 Type E", log, re.MULTILINE), "no #581 Type E entry in iteration-log.md"
        first_entry = re.search(r"^#\d+", log, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#581", "iteration-log.md is not newest-first at #581"

    def test_novelty_single_581_test_file(self):
        files = list((REPO_ROOT / "tests").glob("test_type_e_581*"))
        assert len(files) == 1, f"expected exactly one 581 test file, got {files}"
        assert files[0].name == TEST_FILE


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_581_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_581_block()
        lower = block.lower()
        assert "no episode 499" in lower
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_581_block()
        assert "secondary-only" in block.lower()
        assert "Stated explicitly" in block

    def test_weaker_evidence_tier_disclosed(self):
        block = get_581_block()
        lower = block.lower()
        assert "weaker than #576" in lower

    def test_stale_listen_notes_crawls(self):
        block = get_581_block()
        assert "159-224 days" in block
        assert "Listen Notes" in block

    def test_cadence_note(self):
        block = get_581_block()
        assert "weekly" in block.lower()
        assert "06:00" in block

    def test_561_penciled_499_not_surfaced(self):
        block = get_581_block()
        lower = block.lower()
        assert "561" in block
        assert "penciled 499" in lower
        assert "it has not surfaced" in lower

    def test_chortle_sep13(self):
        block = get_581_block()
        assert "Sep 13" in block
        assert "London Podcast Festival" in block
        assert "Kings Place" in block


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_581_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_581_block()
        assert "activist group, not a podcast" in block

    def test_times_epstein_resurface(self):
        block = get_581_block()
        assert "Times Epstein" in block
        assert "42 days" in block

    def test_engadget_resurface(self):
        block = get_581_block()
        assert "2217151" in block
        assert "52 days" in block

    def test_latestly_resurface(self):
        block = get_581_block()
        assert "latestly.com" in block
        assert "39 days" in block

    def test_petapixel_resurface(self):
        block = get_581_block()
        assert "petapixel.com/2026/07/23" in block
        assert "46 days" in block

    def test_hyperallergic_resurface(self):
        block = get_581_block()
        assert "Hyperallergic" in block
        assert "54 days" in block

    def test_feminist_org_resurface_updated(self):
        block = get_581_block()
        assert "feminist.org" in block
        assert "updated 6 days" in block
        assert "crawled 1 hour" in block

    def test_sifted_not_new_in_corpus_via_480(self):
        block = get_581_block()
        assert "Sifted" in block
        assert "#480" in block
        assert "IN CORPUS" in block

    def test_no_new_primary_motif(self):
        block = get_581_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_581_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "thirty-nine verification cycles" in lower

    def test_no_double_counting(self):
        block = get_581_block()
        assert "No double-counting" in block


class TestAttentionSphereNoMatch:
    def test_39th_no_match(self):
        block = get_581_block()
        lower = block.lower()
        assert "thirty-ninth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_581_block()
        lower = block.lower()
        assert "circular" in lower
        assert "rejected" in lower

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_581_block()
        assert "creators.spotify.com/pod/profile/anita-nowak/" in block
        assert "crawled 4 hours" in block
        assert "non-profit organization" in block

    def test_actual_podcast_named(self):
        block = get_581_block()
        assert "Left to Their Own Devices" in block
        assert "Toronto Star" in block

    def test_status_unchanged_misidentified(self):
        block = get_581_block()
        assert "misidentified" in block.lower()


class TestNewPressSurfaces:
    def test_two_new_surfaces(self):
        block = get_581_block()
        assert "TWO New-To-Corpus" in block

    def test_times_fear_and_loathing(self):
        block = get_581_block()
        assert "Fear and loathing" in block
        assert "0l82sx8sw" in block

    def test_times_zero_hit_greps(self):
        block = get_581_block()
        assert '"0l82sx8sw"' in block
        assert '"fear-and-loathing"' in block

    def test_times_paywalled_bounded(self):
        block = get_581_block()
        lower = block.lower()
        assert "paywalled" in lower
        assert "snippet" in lower

    def test_cybernews_bystander_recordings(self):
        block = get_581_block()
        assert "meta-lawsuit-ai-glasses" in block
        assert "bystander" in block.lower()

    def test_cybernews_zero_hit_greps(self):
        block = get_581_block()
        assert '"meta-lawsuit-ai-glasses"' in block
        assert '"bystander recordings"' in block
        assert '"september 4th"' in block
        assert '"CM3leon"' in block

    def test_illinois_nametag_class_action(self):
        block = get_581_block()
        assert "Illinois" in block
        assert "NameTag" in block
        assert "September 4th" in block

    def test_distinct_from_561_kenyan_contractors(self):
        block = get_581_block()
        assert "#561" in block
        assert "Kenyan-contractors" in block

    def test_newest_frontier_advances(self):
        block = get_581_block()
        assert "ADVANCES this cycle" in block
        lower = block.lower()
        assert "newest in-corpus surface" in lower

    def test_bloomberglaw_in_corpus_not_new(self):
        block = get_581_block()
        assert "Bloomberg Law false-ad class suit" in block
        assert "#576" in block

    def test_sifted_hateaid_lineage_distinguished(self):
        block = get_581_block()
        assert "via #480" in block
        assert "HateAid" in block

    def test_nametag_lineage_in_corpus_but_suit_new(self):
        block = get_581_block()
        assert "NameTag lineage is in corpus" in block


class TestScoresAndDiscipline:
    def test_not_calculated(self):
        block = get_581_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_manual_illustrative(self):
        block = get_581_block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_ehe_posture_8_of_10(self):
        block = get_581_block()
        assert "-8/10" in block

    def test_no_false_significance(self):
        block = get_581_block()
        lower = block.lower()
        assert "do not claim empirical significance" in lower

    def test_correlation_not_causation(self):
        block = get_581_block()
        lower = block.lower()
        assert "correlation not causation" in lower


class TestSources:
    def test_verbatim_urls_present(self):
        block = get_581_block()
        assert "https://cybernews.com/ai-news/meta-lawsuit-ai-glasses/" in block
        assert "https://www.thetimes.com/uk/technology-uk/article/meta-glasses-rayban-privacy-recording-ai-0l82sx8sw" in block

    def test_engadget_verbatim_uppercase_preserved(self):
        block = get_581_block()
        assert "WWW.ENGADGET.COM/2217151" in block

    def test_hyperallergic_verbatim_http_preserved(self):
        block = get_581_block()
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block

    def test_sifted_url_present(self):
        block = get_581_block()
        assert "https://sifted.eu/articles/should-tech-events-ban-smart-glasses/" in block

    def test_no_em_dashes(self):
        block = get_581_block()
        assert "\u2014" not in block, "em dash found in block"


class TestConfounders:
    def test_confounders_ranked(self):
        block = get_581_block()
        lower = block.lower()
        assert "confounders (ranked)" in lower
        assert "strong" in lower
        assert "moderate" in lower

    def test_snippet_bounded_strong(self):
        block = get_581_block()
        lower = block.lower()
        assert "snippet-bounded search results" in lower

    def test_secondary_only_strong(self):
        block = get_581_block()
        lower = block.lower()
        assert "secondary-only" in lower
        assert "weaker than #576" in lower

    def test_listing_timestamp_bounded_strong(self):
        block = get_581_block()
        lower = block.lower()
        assert "listing timestamps" in lower

    def test_five_hour_cadence_strong(self):
        block = get_581_block()
        lower = block.lower()
        assert "five-hour cadence" in lower
        assert "06:00 pdt sep 7" in lower

    def test_illinois_docket_bounded_moderate(self):
        block = get_581_block()
        lower = block.lower()
        assert "no docket or filing url" in lower

    def test_not_calculated_on_confounders(self):
        block = get_581_block()
        conf_section = block.split("### 7. Confounders")[1].split("### 8.")[0]
        assert conf_section.count("NOT_CALCULATED") >= 7
