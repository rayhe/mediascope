"""
Type E #586 - Podcast Sentiment Tracking: Fortieth Verification Cycle Sep 7 11:00 PDT
Guilty Feminist 498 Hold No 499 (Audible UK 5d-crawl re-surface still lists 498
"Politics with Felicity Ward and Hannah Spencer", Chortle 2h crawl Sep 13
Kings Place LPF no new episode, Ivy.fm 2d crawl Sep 5 Newcastle past /
Sep 13 upcoming, stale Listen Notes 206-224d, no 499 by 11:00 PDT / 18:00 UK,
weekly cadence note, 498-latest rests on #576 verification, weaker evidence
tier disclosed, secondary-only) +
EHE 28-Day Hold with LatestLY/Engadget/PetaPixel/AfroTech re-surfaces verified
already-in-corpus via pre-commit grep, GitHub commit/mirror hits rejected as
circular, no double-counting, no new primary motif, no competitor-equivalent
in forty cycles +
Attention Sphere 40th No-Match (circular GitHub rejected, Spotify Creators
<1h-fresh nonprofit re-confirmation, Left to Their Own Devices named,
task-spec misidentified) +
TWO new press surfaces (neoteo.com "Meta Disables Tampered Ray-Ban Cameras"
~Sep 6, neoteo zero corpus hits, sub-0.1% company estimate, second-loophole
detail, snippet-bounded, distinct outlet vs #547 PetaPixel / #576 Startup
Fortune, does NOT advance the #581 Times recency frontier; letsdatascience.com
"Meta Faces Expanded Smart Glasses Privacy Lawsuit" 8bd7207f, domain in corpus
but slug zero hits, Fortune-reported Aug 31 amended complaint ND Cal,
Bartone/Canu plaintiffs, bystanders added, distinct outlet/angle vs
#561/#576/#581 surfaces, snippet-bounded) +
Times/Cybernews/Bloomberg Law/Startup Fortune bricking/Kenyan/HateAid/
FastCo/RoadToVR/Reuters-Dec-2025/AfroTech explicitly distinguished as
in-corpus lineage +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs incl
WWW.ENGADGET.COM and neoteo/en/ and letsdatascience 8bd7207f listings as
surfaced, distinct from 581, fortieth verification cycle, extends #581 by
5 hours, not duplicate, iteration-log entry present and newest-first.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 586
DATE_STR = "2026-09-07 11:00 PDT"
TEST_FILE = Path(__file__).name


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_586_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #586", text, re.MULTILINE)
    assert m, "Iteration #586 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_586_block()
        assert "586" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_586_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_586_block()
        lower = block.lower()
        assert "580 d -> 581 e" not in lower  # previous cycle's rotation, not this one
        assert "585 d -> 586 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_fortieth_cycle_label(self):
        block = get_586_block()
        lower = block.lower()
        assert "fortieth" in lower

    def test_distinct_from_581(self):
        block = get_586_block()
        lower = block.lower()
        assert "thirty-ninth" not in lower
        assert "extends #581 by 5 hours" in block


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_586_block()
        assert "498" in block
        assert "Politics" in block

    def test_no_499_bounded(self):
        block = get_586_block()
        lower = block.lower()
        assert "no episode 499" in lower
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_586_block()
        assert "secondary-only" in block.lower()
        assert "Stated explicitly" in block

    def test_weaker_evidence_tier_disclosed(self):
        block = get_586_block()
        lower = block.lower()
        assert "weaker evidence tier" in lower

    def test_stale_listen_notes_crawls(self):
        block = get_586_block()
        assert "206-224 days" in block
        assert "Listen Notes" in block

    def test_cadence_note(self):
        block = get_586_block()
        assert "weekly" in block.lower()
        assert "11:00 PDT" in block
        assert "18:00 UK" in block

    def test_576_verification_basis(self):
        block = get_586_block()
        lower = block.lower()
        assert "rests on #576" in lower
        assert "audible uk" in lower

    def test_chortle_sep13(self):
        block = get_586_block()
        assert "Sep 13" in block
        assert "London Podcast Festival" in block
        assert "Kings Place" in block

    def test_ivym_past_and_upcoming(self):
        block = get_586_block()
        assert "Ivy.fm" in block
        assert "Newcastle Open Space" in block


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_586_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_586_block()
        assert "activist group, not a podcast" in block

    def test_latestly_resurface(self):
        block = get_586_block()
        assert "latestly.com" in block
        assert "39 days" in block

    def test_engadget_resurface(self):
        block = get_586_block()
        assert "2217151" in block
        assert "52 days" in block

    def test_petapixel_resurface(self):
        block = get_586_block()
        assert "petapixel.com/2026/07/23" in block
        assert "46 days" in block

    def test_afrotech_resurface(self):
        block = get_586_block()
        assert "afrotech.com/smart-glasses-ethics-and-consent" in block
        assert "crawled 3 hours" in block
        assert "in corpus" in block

    def test_github_circular_rejected(self):
        block = get_586_block()
        lower = block.lower()
        assert "circular" in lower
        assert "rejected" in lower
        assert "github.com/rayhe/mediascope/commit/584f331bde53b2f9eafbfed1bbd138546ea8820a" in block

    def test_no_new_primary_motif(self):
        block = get_586_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_586_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "forty verification cycles" in lower

    def test_no_double_counting(self):
        block = get_586_block()
        assert "No double-counting" in block


class TestAttentionSphereNoMatch:
    def test_40th_no_match(self):
        block = get_586_block()
        lower = block.lower()
        assert "fortieth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_586_block()
        lower = block.lower()
        assert "circular" in lower
        assert "rejected" in lower

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_586_block()
        assert "creators.spotify.com/pod/profile/anita-nowak/" in block
        assert "crawled less than 1 hour" in block
        assert "non-profit organization" in block

    def test_actual_podcast_named(self):
        block = get_586_block()
        assert "Left to Their Own Devices" in block
        assert "Toronto Star" in block

    def test_status_unchanged_misidentified(self):
        block = get_586_block()
        assert "misidentified" in block.lower()


class TestNewPressSurfaces:
    def test_neoteo_url_verbatim(self):
        block = get_586_block()
        assert "https://www.neoteo.com/en/meta-disables-tampered-ray-ban-cameras" in block

    def test_neoteo_zero_corpus_hits(self):
        block = get_586_block()
        lower = block.lower()
        assert "zero pre-commit grep hits" in lower
        assert "new-to-corpus domain" in lower

    def test_neoteo_tampering_estimate(self):
        block = get_586_block()
        assert "0.1%" in block
        assert "second loophole" in block.lower()

    def test_neoteo_distinct_outlet(self):
        block = get_586_block()
        lower = block.lower()
        assert "distinct outlet" in lower
        assert "#547" in block
        assert "#576" in block

    def test_neoteo_no_frontier_advance(self):
        block = get_586_block()
        lower = block.lower()
        assert "does not advance" in lower
        assert "recency frontier" in lower
        assert "times" in lower

    def test_letsdatascience_url_verbatim(self):
        block = get_586_block()
        assert "https://letsdatascience.com/news/meta-faces-expanded-smart-glasses-privacy-lawsuit-8bd7207f" in block

    def test_letsdatascience_domain_in_corpus_article_new(self):
        block = get_586_block()
        assert "IN CORPUS" in block
        lower = block.lower()
        assert "domain in corpus" in lower
        assert "article is new-to-corpus" in lower

    def test_letsdatascience_amended_complaint_details(self):
        block = get_586_block()
        assert "Fortune" in block
        assert "Aug 31" in block
        assert "Bartone" in block
        assert "Canu" in block
        assert "bystanders" in block.lower()

    def test_letsdatascience_distinct_from_561_576_581(self):
        block = get_586_block()
        lower = block.lower()
        assert "distinct outlet/angle" in lower
        assert "#561" in block
        assert "#576" in block
        assert "#581" in block

    def test_snippet_bounded(self):
        block = get_586_block()
        lower = block.lower()
        assert "snippet-bounded" in lower


class TestScoresAndDiscipline:
    def test_no_significance_claims(self):
        block = get_586_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_586_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "-8/10" in block

    def test_correlation_not_causation(self):
        block = get_586_block()
        assert "Correlation not causation" in block

    def test_no_em_dashes_in_block(self):
        block = get_586_block()
        # Matches the #581 convention (source-level escaped literal, which is
        # the six-character text "\u2014"), plus a real-character check via
        # chr(0x2014) that embeds no em dash in this source file.
        assert "\\u2014" not in block, "escape-sequence found in block"
        assert chr(0x2014) not in block, "em dash found in block"

    def test_no_em_dashes_in_test_file(self):
        src = Path(__file__).read_text(encoding="utf-8")
        # The escaped assertion literal above is not a real em dash; count
        # real occurrences only via chr(0x2014), which embeds no em dash
        # in this source file.
        assert src.count(chr(0x2014)) == 0, "real em dash found in test file source"


class TestSources:
    def test_chortle_verbatim(self):
        block = get_586_block()
        assert "https://www.chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist" in block

    def test_audible_uk_verbatim(self):
        block = get_586_block()
        assert "https://www.audible.co.uk/podcast/The-Guilty-Feminist/B08K5Y1B25" in block

    def test_listen_notes_localized_verbatim(self):
        block = get_586_block()
        assert "https://www.listennotes.com/pt/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block
        assert "https://www.listennotes.com/nl/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block

    def test_www_engadget_verbatim(self):
        block = get_586_block()
        # Listing surfaced the URL in uppercase; keep verbatim per the
        # always-verbatim-URLs rule.
        assert "https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in block

    def test_in_corpus_lineage_distinguished(self):
        block = get_586_block()
        for marker in ("via #581", "via #576", "via #561"):
            assert marker in block, f"missing in-corpus marker {marker}"
        assert "NOT new" in block

    def test_fastco_roadtovr_reuters_old_distinguished(self):
        block = get_586_block()
        assert "91571430" in block
        assert "roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/" in block
        assert "2025-12-09" in block

    def test_test_file_section(self):
        text = read_doc()
        assert "test_type_e_586_podcast_sentiment_fortieth_verification_sep07_11am.py" in text


class TestConfoundersAndLog:
    def test_five_strong_confounders(self):
        block = get_586_block()
        assert block.count("STRONG") >= 5

    def test_five_hour_cadence_bound(self):
        block = get_586_block()
        lower = block.lower()
        assert "five-hour cadence" in lower
        assert "11:00 PDT Sep 7" in block

    def test_log_entry_present_newest_first(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Iteration #586" in log or "#586 Type E" in log
        first_iteration = log.find("#586 Type E")
        prev_iteration = log.find("#585")
        assert first_iteration != -1 and prev_iteration != -1
        assert first_iteration < prev_iteration, \
            "iteration-log.md is not newest-first for #586"

    def test_rotation_transparency(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "585 D -> 586 E" in log

    def test_log_rotation_transparency_mentions_previous_commit(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "8e2f87a" in log

    def test_log_novelty_verification(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Novelty Verification" in log
        assert "fortieth cycle is new" in log.lower()
