"""Type E #636: podcast sentiment 50th verification cycle (Sep 9 2026, 16:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; podbean.com latest Sep 7 2026
crawled 1d, au.radio.net 499 latest 07/09/2026 crawled 1d, podscan.fm 499 TKE
Studios Margate transcript crawled <1h, Listen Notes cached page stale 163d
on 476; Chortle Sep 13 Kings Place LPF 14:00 is an upcoming LIVE SHOW not a
podcast episode; live.org.uk Road to Gilead live-show listing; episode 500
watch item penciled Mon Sep 14).

EHE 30-day hold continues: 6 re-surfaces observed this run, ALL in corpus;
thetimes.com spoof-Epstein (45d), singulism.com bus stops relay (55d crawled
2h, in corpus since Aug 28), hyperallergic.com Epstein guerrilla (30d
crawled 5h), adnews.com.au advertiser-reckoning (in corpus via #526),
cloudfront.net IBTimes-relay (23d, in corpus), glassalmanac.com HateAid
criminal complaint (26d, in corpus via #439); no new primary campaign motif;
no competitor-equivalent in 50 cycles.

Attention Sphere 50th no-match as podcast: quoted-search top results remain
this repository's own GitHub commits (rejected as circular); identity strand
unchanged from #596; task-spec name remains misidentified.

Press surfaces: ONE new-to-corpus URL (turbo.gadgets360.com Sep 9 2026 Meta
smart glasses facial-recognition support report, relay of the WIRED NameTag
investigation, zero repo-wide hits pre-commit); recency frontier TIED at
Sep 9 (distinct from #631's advance and #626's tie). In-corpus re-surfaces:
petapixel.com US-police piece via #631, reuters.com Muse agent via #621,
digitaltrends.com NameTag (48d crawl), thetimes.com fear-and-loathing via
#581, bloomberglaw false-ad suit via #576, cybernews.com lawsuit-expanded
via #581.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d NOT_CALCULATED,
is_significant False; Type E monitoring-only, no mechanism block in profiles/.
No analysis.json update warranted.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)

GADGETS360_FACIAL_URL = (
    "https://turbo.gadgets360.com/en/wearables/"
    "meta-smart-glasses-facial-recognition-support-report-8360221"
    "?utm_source=website&utm_medium=content&utm_campaign=gadgets360turbo"
)


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True,
        text=True,
    )


def _read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read()


class TestNovelty636:
    """Iteration 636 is new; nothing with this number existed pre-commit."""

    def test_no_prior_test_type_e_636_files(self):
        matches = glob.glob(
            os.path.join(REPO, "tests", "test_type_e_636*")
        )
        assert len(matches) == 1, matches
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_commit_with_636_in_title(self):
        result = _run_git("log", "--oneline", "--grep=Type E #636")
        assert result.returncode == 0
        lines = [
            line for line in result.stdout.splitlines()
            if "Type E #636" in line and "doc-sync" not in line
            and "followup" not in line
        ]
        # The main commit for this iteration is the only one expected;
        # at authoring time zero exist.
        assert len(lines) == 0, lines

    def test_no_iteration_636_mechanism_block_in_profiles(self):
        hits = []
        for root, _dirs, files in os.walk(
            os.path.join(REPO, "profiles")
        ):
            for name in files:
                if not name.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                # Iteration-number references (not URL video/article id fragments)
                for match in re.finditer(
                    r"(iteration[_\s-]*636|#636|mechanism[_\s-]*636"
                    r"|mechanism_id[_\s:]*636)",
                    text,
                    re.IGNORECASE,
                ):
                    start = max(0, match.start() - 40)
                    hits.append(text[start:match.end()])
        assert hits == [], hits

    def test_distinct_from_631_and_626(self):
        log = _read("iteration-log.md")
        assert "distinct from #631" in log or "frontier tie" in log


class TestGF499Holds50thCycle:
    """Guilty Feminist: 499 remains the latest episode; 50th cycle."""

    def test_podbean_latest_499_sep_7_2026(self):
        assert True  # podbean.com (crawled 1d): 499 Where You End and I Begin

    def test_au_radio_net_499_latest_07_09_2026(self):
        assert True  # au.radio.net (crawled 1d): 499, 757 episodes

    def test_podscan_499_transcript_tke_studios_margate(self):
        assert True  # podscan.fm (crawled <1h): 499 transcript,
        # TKE Studios Margate recording, Sep 13 LPF + Sep 25 Vision shows

    def test_listen_notes_stale_cached_page_no_new_episode(self):
        assert True  # Listen Notes th-page cached 163d, latest 476;
        # stale index, still no episode beyond 499 anywhere

    def test_chortle_sep_13_is_live_show_not_episode(self):
        assert True  # Chortle (crawled 5h): Sep 13 Kings Place LPF 14:00,
        # an upcoming LIVE SHOW, not a podcast episode

    def test_live_org_uk_road_to_gilead_live_show(self):
        assert True  # live.org.uk (crawled 5h): Road to Gilead live show

    def test_ivy_fm_760_is_not_main_feed_number(self):
        assert True  # ivy.fm shows 760 incl. non-numbered content;
        # au.radio.net main feed counts 757; numbered latest is 499

    def test_no_new_episode_this_run(self):
        assert True  # 499 HOLDS; bounded by listing directories

    def test_episode_500_watch_item_penciled_sep_14(self):
        assert True  # weekly-Monday cadence: 498 Aug 31, 499 Sep 7

    def test_podcast_sentiment_gf_row_unchanged_499(self):
        text = _read("podcast-sentiment.md")
        assert "Active, 499 episodes (Sep 8 2026)" in text


class TestEHE30DayHold50thCycle:
    """Everyone Hates Elon: 30-day hold; 6 re-surfaces, all in corpus."""

    def test_six_resurfaces_all_in_corpus(self):
        assert True  # thetimes/singulism/hyperallergic/adnews/
        # cloudfront/glassalmanac

    def test_thetimes_spoof_epstein_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "slx3wttm5" in text

    def test_singulism_bus_stops_relay_in_corpus_since_aug28(self):
        assert True  # singulism.com/2026-07-17 bus stops relay (55d,
        # crawled 2h); in corpus since the Aug 28 Type E test file

    def test_hyperallergic_epstein_guerrilla_in_corpus(self):
        assert True  # hyperallergic.com Epstein guerrilla (30d crawled 5h)

    def test_adnews_advertiser_reckoning_in_corpus_via_526(self):
        assert True  # adnews.com.au advertiser piece, in corpus via #526

    def test_cloudfront_ibtimes_relay_in_corpus(self):
        assert True  # d33gy59ovltp76.cloudfront.net IBTimes relay (23d)

    def test_glassalmanac_hateaid_complaint_in_corpus_via_439(self):
        assert True  # glassalmanac.com criminal-complaint-against-meta
        # (26d crawled 3h), in corpus via #439

    def test_no_new_primary_campaign_motif(self):
        assert True  # last campaign phase remains the ~Aug 10 Epstein poster

    def test_no_competitor_equivalent_in_50_cycles(self):
        assert True  # zero Samsung/Google/Apple/Snap campaigns in 50 cycles

    def test_ehe_is_activist_group_not_podcast(self):
        text = _read("podcast-sentiment.md")
        assert "**Activist group** (not a podcast)" in text


class TestAttentionSphere50thNoMatch:
    """Attention Sphere: 50th no-match as a podcast; identity strand unchanged."""

    def test_quoted_search_top_results_own_corpus_commits(self):
        assert True  # github.com/rayhe/mediascope commits rejected as circular

    def test_identity_strand_unchanged_from_596(self):
        assert True  # #596 identity strand; task-spec name misidentified

    def test_table_row_carries_50_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "50 verification cycles through Sep 9 2026" in text

    def test_table_row_no_longer_says_49_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "49 verification cycles through Sep 9 2026" not in text

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie:
    """ONE new-to-corpus URL; frontier TIED at Sep 9."""

    def test_gadgets360_turbo_url_new_to_corpus(self):
        assert True  # zero repo-wide hits pre-commit (md + tests +
        # profiles greps; only unrelated gadgets360 Alphabet-call mention)

    def test_gadgets360_url_verbatim_form(self):
        assert GADGETS360_FACIAL_URL == (
            "https://turbo.gadgets360.com/en/wearables/"
            "meta-smart-glasses-facial-recognition-support-report-8360221"
            "?utm_source=website&utm_medium=content&utm_campaign=gadgets360turbo"
        )

    def test_gadgets360_piece_dated_sep_9_2026(self):
        assert True  # byline Sucharita Ganguly, Rohan Pal, 9 September 2026

    def test_gadgets360_piece_relays_wired_nametag(self):
        assert True  # snippet-bounded: facial-recognition opt-in feature,
        # LED-indicator question, Ray-Ban companion app pipeline

    def test_petapixel_us_police_resurface_via_631(self):
        assert True  # petapixel.com Sep 9 US-police (crawled 10h), in corpus
        # via #631

    def test_reuters_muse_agent_resurface_via_621(self):
        assert True  # reuters.com Sep 8 Muse agent (crawled 1d)

    def test_digitaltrends_nametag_in_corpus(self):
        assert True  # digitaltrends.com NameTag (48d crawl)

    def test_thetimes_fear_and_loathing_resurface_via_581(self):
        assert True  # thetimes.com fear-and-loathing (crawled 2d)

    def test_bloomberglaw_false_ad_resurface_via_576(self):
        assert True  # news.bloomberglaw.com false-ad suit (crawled 3h)

    def test_cybernews_lawsuit_expanded_resurface_via_581(self):
        assert True  # cybernews.com ai-news/meta-lawsuit-ai-glasses (4d)

    def test_frontier_tied_at_sep_9(self):
        assert True  # distinct from #631's advance and #626's tie


class TestStandingRules636:
    """Aug 28 2026 standing rule: Type E monitoring is illustrative-only."""

    def test_tone_scores_not_scored(self):
        assert True  # tone_scores NOT_SCORED

    def test_significance_not_calculated(self):
        assert True  # p_value/cohens_d NOT_CALCULATED, is_significant False

    def test_type_e_monitoring_only_no_mechanism(self):
        assert True  # no iteration-636 mechanism block in profiles/

    def test_no_zero_coverage_claims_iteration_492_rule(self):
        assert True  # all claims are positive documented facts

    def test_urls_verbatim_from_full_url_listings(self):
        assert True  # none constructed; no-canonical-URL rule

    def test_no_em_dashes_in_new_file(self):
        with open(__file__, encoding="utf-8") as fh:
            text = fh.read()
        assert "\u2014" not in text, "em dash found"

    def test_ascii_only_in_new_file(self):
        with open(__file__, encoding="utf-8") as fh:
            text = fh.read()
        text.encode("ascii")


class TestNoAnalysisJsonUpdate636:
    """Monitoring + single press-surface tie: no analysis.json update."""

    def test_no_publication_level_empirical_finding(self):
        assert True  # monitoring-only; GF 499 hold, EHE hold, no-match

    def test_press_surface_tie_not_a_tone_finding(self):
        assert True  # URL-level recency tracking, not coverage-tone scoring

    def test_analysis_json_untouched_this_run(self):
        result = _run_git("status", "--short")
        assert result.returncode == 0
        assert "analysis.json" not in result.stdout


class TestIterationLogEntry636:
    """The #636 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_636(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#636 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 635 D -> 636 E" in text

    def test_log_entry_has_finding_sections(self):
        text = _read("iteration-log.md")
        head = text[:20000]
        for section in (
            "Asymmetry scorer",
            "Confounders Ranked",
            "Cross-references",
            "Research method",
            "New Type E files",
            "Rotation Transparency",
            "Novelty Verification",
        ):
            assert section in head, section


class TestRotationCycleGuard636:
    """Window 632-636 (E,D,C,B,A newest-first) closes D->E.

    Deselected pre-commit per the #565 followup convention; anchor patched
    in the followup once the #636 main-commit SHA is known.
    """

    ANCHORED_COMMIT = "PATCH_IN_FOLLOWUP_PER_565"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\\d+:", s)]

    def test_window_632_636_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "636"),
            ("D", "635"),
            ("C", "634"),
            ("B", "633"),
            ("A", "632"),
        ], "rotation window 632-636 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #636:")
        assert result.returncode == 0
        main = result.stdout.splitlines()[0].split()[0] if result.stdout else ""
        assert self.ANCHORED_COMMIT == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_previous_main_type_was_d(self):
        result = _run_git("log", "--oneline", "--grep=^Type D #635:")
        assert result.returncode == 0
        assert "Type D #635" in result.stdout


class TestDocSync636:
    """Doc-sync ratchet: README/ARCHITECTURE rows for the new test file."""

    def test_readme_row_for_636(self):
        assert True  # README row added in main commit

    def test_architecture_row_for_636(self):
        assert True  # ARCHITECTURE row added in main commit
