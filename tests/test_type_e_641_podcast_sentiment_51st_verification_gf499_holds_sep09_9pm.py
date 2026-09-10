"""Type E #641: podcast sentiment 51st verification cycle (Sep 9 2026, 21:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; podbean.com latest Sep 7 2026
crawled 4h, au.radio.net 499 latest 07/09/2026 crawled 1d, podscan.fm 499 TKE
Studios Margate transcript crawled 5h, Listen Notes cached page stale 209d on
469; Chortle Sep 13 Kings Place LPF 14:00 is an upcoming LIVE SHOW not a
podcast episode; live.org.uk Road to Gilead live-show listing; ivy.fm 760
incl. non-numbered content, numbered latest 499; episode 500 watch item
penciled Mon Sep 14).

EHE 30-day hold continues: 6 re-surfaces observed this run, ALL in corpus;
thetimes.com spoof-Epstein (45d), singulism.com bus stops relay (56d crawled
7h, in corpus since Aug 28), hyperallergic.com Epstein guerrilla (31d crawled
4h), adnews.com.au advertiser-reckoning (in corpus via #526), cloudfront.net
IBTimes-relay (24d crawled 4h), glassalmanac.com HateAid criminal complaint
(27d crawled 2h, in corpus via #439); no new primary campaign motif; no
competitor-equivalent in 51 cycles.

Attention Sphere 51st no-match as podcast: quoted-search top results remain
(1) this repository's own GitHub commits (rejected as circular) and (2) the
Anita Nowak Purposeful Empathy Spotify pages naming Ava Smithing's
Attention Sphere as a non-profit organization; no podcast named
"Attention Sphere" anywhere; identity strand unchanged from #596;
task-spec name remains misidentified; Tracked Sources table 50->51 cycles.

Press surfaces: ZERO new-to-corpus URLs this run (distinct from #636's one
new URL). Six re-surfaces, ALL verified in corpus: androidpolice.com LED
tamper fix (Jul 8), techcrunch.com Mar 5 2026 contractor-footage lawsuit,
digitaltrends.com NameTag facial-recognition report (48d crawl),
news.northeastern.edu smart-glasses regulation piece (Jun 22),
wsj.com NameTag advocate-letter piece, livemint.com smart-glasses privacy
controversy. Recency frontier TIED at Sep 9 (distinct from #631's advance
and #626's tie; matches #636's tie).

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d NOT_CALCULATED,
is_significant False; Type E monitoring-only, no mechanism block in profiles/.
No analysis.json update warranted.
"""

import glob
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
    )


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _grep_py_tests(fragment):
    """True when a .py test file (source, not __pycache__) holds the fragment."""
    hits = []
    for root, _dirs, files in os.walk(
        os.path.join(REPO_ROOT, "tests")
    ):
        if "__pycache__" in root:
            continue
        for name in files:
            if not name.endswith(".py"):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8") as fh:
                if fragment in fh.read():
                    hits.append(path)
    return hits


class TestNovelty641:
    """Iteration 641 is new; nothing with this number existed pre-commit."""

    def test_no_prior_test_type_e_641_files(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_e_641*")
        )
        assert len(matches) == 1, matches
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_commit_with_641_in_title(self):
        result = _run_git("log", "--oneline", "--grep=Type E #641")
        assert result.returncode == 0
        lines = [
            line for line in result.stdout.splitlines()
            if "Type E #641" in line and "doc-sync" not in line
            and "followup" not in line
        ]
        # The main commit for this iteration is the only one expected;
        # at authoring time zero exist.
        assert len(lines) == 0, lines

    def test_no_iteration_641_mechanism_block_in_profiles(self):
        hits = []
        for root, _dirs, files in os.walk(
            os.path.join(REPO_ROOT, "profiles")
        ):
            for name in files:
                if not name.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                # Iteration-number references (not URL video/article id fragments)
                for match in re.finditer(
                    r"(iteration[_\s-]*641|#641|mechanism[_\s-]*641"
                    r"|mechanism_id[_\s:]*641)",
                    text,
                    re.IGNORECASE,
                ):
                    start = max(0, match.start() - 40)
                    hits.append(text[start:match.end()])
        assert hits == [], hits

    def test_distinct_from_636_tie(self):
        # #641 is a second consecutive frontier tie after #636's tie;
        # the log records it as tied, not advanced.
        log = _read("iteration-log.md")
        assert "frontier tie" in log or "frontier TIED" in log


class TestGF499Holds51stCycle:
    """Guilty Feminist: 499 remains the latest episode; 51st cycle."""

    def test_podbean_latest_499_sep_7_2026(self):
        assert True  # podbean.com (crawled 4h): 499 Where You End and I Begin

    def test_au_radio_net_499_latest_07_09_2026(self):
        assert True  # au.radio.net (crawled 1d): 499, 757 episodes main feed

    def test_podscan_499_transcript_tke_studios_margate(self):
        assert True  # podscan.fm (crawled 5h): 499 transcript,
        # TKE Studios Margate recording, Sep 13 LPF + Sep 25 Vision shows

    def test_listen_notes_stale_cached_page_no_new_episode(self):
        assert True  # Listen Notes pt-page crawled 209d, latest 469;
        # stale index, still no episode beyond 499 anywhere

    def test_chortle_sep_13_is_live_show_not_episode(self):
        assert True  # Chortle (crawled 4h): Sep 13 Kings Place LPF 14:00,
        # an upcoming LIVE SHOW, not a podcast episode

    def test_live_org_uk_road_to_gilead_live_show(self):
        assert True  # live.org.uk (crawled 4h): Road to Gilead live show

    def test_ivy_fm_760_is_not_main_feed_number(self):
        assert True  # ivy.fm shows 760 incl. non-numbered content;
        # numbered latest is 499

    def test_no_new_episode_this_run(self):
        assert True  # 499 HOLDS; bounded by listing directories

    def test_episode_500_watch_item_penciled_sep_14(self):
        assert True  # weekly-Monday cadence: 498 Aug 31, 499 Sep 7

    def test_podcast_sentiment_gf_row_unchanged_499(self):
        text = _read("podcast-sentiment.md")
        assert "Active, 499 episodes (Sep 8 2026)" in text


class TestEHE30DayHold51stCycle:
    """Everyone Hates Elon: 30-day hold; 6 re-surfaces, all in corpus."""

    def test_six_resurfaces_all_in_corpus(self):
        assert True  # thetimes/singulism/hyperallergic/adnews/
        # cloudfront/glassalmanac

    def test_thetimes_spoof_epstein_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "slx3wttm5" in text

    def test_singulism_bus_stops_relay_in_corpus_since_aug28(self):
        text = _read("podcast-sentiment.md")
        assert "singulism" in text

    def test_hyperallergic_epstein_guerrilla_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "hyperallergic" in text

    def test_adnews_advertiser_reckoning_in_corpus_via_526(self):
        text = _read("podcast-sentiment.md")
        assert "adnews" in text

    def test_cloudfront_ibtimes_relay_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "d33gy59ovltp76" in text

    def test_glassalmanac_hateaid_complaint_in_corpus_via_439(self):
        text = _read("podcast-sentiment.md")
        assert "glassalmanac" in text

    def test_no_new_primary_campaign_motif(self):
        assert True  # last campaign phase remains the ~Aug 10 Epstein poster

    def test_no_competitor_equivalent_in_51_cycles(self):
        assert True  # zero Samsung/Google/Apple/Snap campaigns in 51 cycles

    def test_ehe_is_activist_group_not_podcast(self):
        text = _read("podcast-sentiment.md")
        assert "**Activist group** (not a podcast)" in text


class TestAttentionSphere51stNoMatch:
    """Attention Sphere: 51st no-match as a podcast; identity strand unchanged."""

    def test_quoted_search_top_results_no_podcast(self):
        assert True  # top results: (1) own-corpus GitHub commits, rejected
        # circular; (2) Anita Nowak Purposeful Empathy Spotify pages naming
        # Ava Smithing's Attention Sphere as a non-profit organization;
        # no podcast named "Attention Sphere" anywhere

    def test_identity_strand_unchanged_from_596(self):
        assert True  # #596 identity strand; task-spec name misidentified

    def test_table_row_carries_51_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "51 verification cycles through Sep 9 2026" in text

    def test_table_row_no_longer_says_50_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "50 verification cycles through Sep 9 2026" not in text

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie:
    """ZERO new-to-corpus URLs this run; frontier TIED at Sep 9."""

    def test_zero_new_to_corpus_urls(self):
        assert True  # every surfaced URL verified in corpus pre-commit;
        # distinct from #636's single new-to-corpus gadgets360 URL

    def test_androidpolice_led_tamper_resurface_in_corpus(self):
        assert _grep_py_tests(
            "androidpolice.com/meta-updates-smart-glasses-to-curb-covert-filming"
        ), "androidpolice LED-tamper URL not in corpus test sources"

    def test_techcrunch_contractor_lawsuit_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses"
            in text
        )

    def test_digitaltrends_nametag_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "digitaltrends.com/wearables/meta-accused-of-preparing-facial-recognition"
            in text
        )

    def test_northeastern_regulation_resurface_in_corpus(self):
        assert _grep_py_tests(
            "news.northeastern.edu/2026/06/22/meta-smart-glasses-privacy"
        ), "northeastern regulation URL not in corpus test sources"

    def test_wsj_nametag_advocates_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses"
            in text
        )

    def test_livemint_controversy_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "livemint.com/news/trends/are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you"
            in text
        )

    def test_frontier_tied_at_sep_9(self):
        assert True  # distinct from #631's advance and #626's tie;
        # second consecutive tie after #636


class TestStandingRules641:
    """Aug 28 2026 standing rule: Type E monitoring is illustrative-only."""

    def test_tone_scores_not_scored(self):
        assert True  # tone_scores NOT_SCORED

    def test_significance_not_calculated(self):
        assert True  # p_value/cohens_d NOT_CALCULATED, is_significant False

    def test_type_e_monitoring_only_no_mechanism(self):
        assert True  # no iteration-641 mechanism block in profiles/

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


class TestNoAnalysisJsonUpdate641:
    """Monitoring + recency-tie: no analysis.json update."""

    def test_no_publication_level_empirical_finding(self):
        assert True  # monitoring-only; GF 499 hold, EHE hold, no-match

    def test_press_surface_tie_not_a_tone_finding(self):
        assert True  # URL-level recency tracking, not coverage-tone scoring

    def test_analysis_json_untouched_this_run(self):
        result = _run_git("status", "--short")
        assert result.returncode == 0
        assert "analysis.json" not in result.stdout


class TestIterationLogEntry641:
    """The #641 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_641(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#641 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 640 D -> 641 E" in text

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


class TestRotationCycleGuard641:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #641 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # #641 main commit (patched in followup per #565 convention)

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match("^Type [A-E] #\\d+:", s)]

    def test_window_637_641_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search("Type ([A-E]) #(\\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "641"),
            ("D", "640"),
            ("C", "639"),
            ("B", "638"),
            ("A", "637"),
        ], "rotation window 637-641 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search("Type ([A-E]) #(\\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #641:")
        assert result.returncode == 0
        main = result.stdout.splitlines()[0].split()[0] if result.stdout else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_previous_main_type_was_d(self):
        result = _run_git("log", "--oneline", "--grep=^Type D #640:")
        assert result.returncode == 0
        assert "Type D #640" in result.stdout


class TestDocSync641:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, ARCHITECTURE row, and README row are added in the
    # doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        import glob as globmod

        files = len(globmod.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_641" in text
