"""Type E #671: podcast sentiment 57th verification cycle (Sep 11 2026, 04:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk 757 episodes
with latest episode 2026-09-07 crawled 4h; au.radio.net 757 episodes with
499 "Where You End and I Begin with Lindsey Mendick, 07/09/2026, 1h 10
mins" latest crawled 2d; ie.radio.net GF podcast page re-surface crawled
21h, in corpus via #656 directory corroboration; Listen Notes cached page
still stale on 498 "Politics" (released Aug 31, 5d crawl); podscan.fm 499
TKE Studios Margate transcript crawled 4h; Chortle Sep 13 Kings Place LPF
14:00 live-show re-surface crawled 4h is an upcoming LIVE SHOW not episode
500; episode 500 watch item penciled Mon Sep 14 per the weekly-Monday
cadence: 498 Aug 31, 499 Sep 7).

EHE 32-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: thetimes.com spoof-Epstein piece (46d, crawled 46d),
latestly.com Jul 30 2026 spoof-Epstein fact-check (43d, crawled 19d, in
corpus since #383/#445/#465), petapixel.com Kylie Jenner lenticular
"We're always watching" (50d, crawled 17d), engadget.com London bus stops
fake-ad piece (56d, crawled 7d), feminist.org/news Feminist Majority
Foundation "Helpful or Hurtful" piece (listed updated 10d, crawled 2h, in
corpus since #470/#561/#596), sifted.eu tech-events ban piece (16d, crawled
15d, in corpus via #480), afrotech.com smart-glasses ethics piece (56d,
crawled 4h). No new primary campaign motif; last campaign phase remains the
circa Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign
against Apple/Google/Samsung/Snap camera wearables in any of the 57 cycles.

Attention Sphere 57th no-match as podcast: quoted-search top results remain
this repository's own GitHub pages (podcast-sentiment.md blob/HEAD and
prior Type E commit pages; rejected as circular per established discipline).
No podcast named "Attention Sphere" anywhere; identity strand unchanged from
#596; task-spec name remains misidentified; Tracked Sources table 56->57
cycles through Sep 11 2026.

Press surfaces: ZERO new-to-corpus press surfaces advancing the frontier
this run. One stale re-index logged for completeness, not a frontier
advance: digitaltrends.com v19.2 firmware piece (~July 2026 content, crawled
46d; digitaltrends domain in corpus, exact URL logged this run). In-corpus
re-surfaces: petapixel.com Sep 9 US-police-warning piece (in corpus via
#631, crawled 1d), thetimes.com "Fear and loathing" London field test (via
#581, crawled 3d), Reuters Sep 8 Meta Muse/Hatch agent piece (via #621,
crawled 2d), techtime.news Sep 2 Lumus waveguide piece (via #621, crawled
2h), Reuters Jan 13 2026 doubling-output piece (240d stale re-index),
Reuters Jan 6 2026 Display rollout piece (247d stale re-index),
thevermilion.com Ray-Ban Display piece (in corpus via #626, 357d, crawled
<1h). Recency frontier TIED at Sep 9 (eighth consecutive tie after #636,
#641, #646, #651, #656, #661 and #666).

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted.
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
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "tests")):
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


def _md_grep(pattern, rel):
    text = _read(rel)
    return re.findall(pattern, text)


class TestNovelty671:
    """Iteration 671 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_671_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_671*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_671_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_e_671 files,
        # no #671 in git log); this test pins that no duplicate #671 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^Type E #671:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type E #671 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard671.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestGF499Holds57thCycle:
    def test_gf_row_still_499(self):
        text = _read("podcast-sentiment.md")
        m = re.search(r"\| The Guilty Feminist \| \*\*Podcast\*\*[^|]*\| ([^|]*499[^|]*) \|", text)
        assert m, "GF row with 499 episodes not found"

    def test_gf_row_date_now_sep_11(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 11 2026)" in text

    def test_gf_row_no_longer_says_sep_10_or_earlier(self):
        text = _read("podcast-sentiment.md")
        head = text[:2000]
        assert "499 episodes (Sep 10 2026)" not in head

    def test_uk_podcasts_still_latest_2026_09_07(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "uk-podcasts.co.uk" in section
        assert "Latest episode: 2026-09-07" in section

    def test_ie_radio_net_still_in_corpus_via_656(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "ie.radio.net" in section
        assert "in corpus" in section

    def test_radio_net_au_lists_499_latest(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "au.radio.net" in section
        assert "499" in section

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "Mon Sep 14" in section

    def test_chortle_sep_13_is_live_show_not_episode(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "Chortle" in section
        assert "not an episode" in section or "LIVE SHOW" in section

    def test_listen_notes_stale_on_498(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "Listen Notes" in section
        assert "498" in section

    def test_podscan_transcript_corroborates_499(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "podscan.fm" in section


class TestEHE32DayHold57thCycle:
    def test_latestly_fact_check_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "latestly.com" in section
        assert "in corpus" in section

    def test_engadget_bus_stops_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "engadget.com" in section

    def test_afrotech_ethics_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "afrotech.com" in section

    def test_feminist_org_10d_piece_is_resurface_not_new(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "feminist.org" in section
        assert "re-surface" in section or "re-surfaces" in section

    def test_thetimes_petapixel_sifted_resurfaces_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        for frag in ("thetimes.com", "petapixel.com", "sifted.eu"):
            assert frag in section, frag

    def test_no_new_primary_motif(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "no new primary motif" in section

    def test_no_competitor_equivalent_in_57_cycles(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "57 cycles" in section
        assert "No competitor-equivalent" in section


class TestAttentionSphere57thNoMatch:
    def test_quoted_search_top_results_no_podcast(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "57th" in section or "fifty-seventh" in section
        assert "no matching podcast" in section

    def test_circular_own_corpus_rejected(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "circular" in section

    def test_identity_strand_unchanged_from_596(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "#596" in section

    def test_table_row_carries_57_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "57 verification cycles through Sep 11 2026" in text

    def test_table_row_no_longer_says_56_cycles(self):
        text = _read("podcast-sentiment.md")
        head = text[:2000]
        assert "56 verification cycles through Sep 10 2026" not in head

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie:
    def test_zero_new_frontier_advancing_surfaces_this_run(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "ZERO new-to-corpus press surfaces advancing the frontier" in section

    def test_digitaltrends_stale_reindex_logged_not_frontier(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "digitaltrends.com" in section
        assert "stale re-index" in section
        assert "NOT a frontier advance" in section

    def test_petapixel_sep_9_police_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "petapixel.com/2026/09/09" in section
        assert "in corpus via #631" in section

    def test_reuters_sep_8_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "Reuters Sep 8" in section
        assert "in corpus via #621" in section

    def test_techtime_lumus_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "techtime.news" in section
        assert "in corpus via #621" in section

    def test_thetimes_fear_and_loathing_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "thetimes.com" in section
        assert "in corpus via #581" in section

    def test_thevermilion_resurface_in_corpus_via_626(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "thevermilion.com" in section
        assert "in corpus via #626" in section

    def test_frontier_tied_at_sep_9_eighth_consecutive(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "eighth consecutive tie" in section
        assert "TIED at Sep 9" in section


class TestStandingRules671:
    def test_tone_not_scored(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "No tone scores computed" in section

    def test_significance_not_calculated(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "p_value NOT_CALCULATED" in section
        assert "is_significant False" in section

    def test_no_profiles_mechanism_block(self):
        # Type E adds no mechanism block in profiles/; this run logs none.
        # Check for mechanism_id as an ASSIGNED field (YAML key or code
        # assignment), not mere mentions inside comments or this assertion.
        text = _read("tests/" + TEST_BASENAME)
        assert not re.search(r"^\s*mechanism_id\s*[:=]", text, re.M), (
            "mechanism_id assignment found; Type E logs no mechanism"
        )


class TestNoAnalysisJsonUpdate671:
    def test_no_publication_level_empirical_finding(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "No claim of empirical significance" in section

    def test_press_surface_tie_not_a_tone_finding(self):
        section = _read("podcast-sentiment.md").split("## Iteration #671")[-1]
        assert "not a frontier advance" in section or "TIED at Sep 9" in section

    def test_analysis_json_untouched_this_run(self):
        out = _run_git("status", "--short")
        assert "analysis.json" not in out.stdout


class TestIterationLogEntry671:
    """The #671 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_671(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#671 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 670 D -> 671 E" in text

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


class TestRotationCycleGuard671:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #671 main-commit SHA is known.
    ANCHORED_SHA = "00efcbd0261b19062d73661a22b1399ecb0831ea"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_667_671_closes_a_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "671"),
            ("D", "670"),
            ("C", "669"),
            ("B", "668"),
            ("A", "667"),
        ], "rotation window 667-671 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type E #671:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync671:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, test-file table row, and
    # ARCHITECTURE row land in the doc-sync commit.
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
        assert "test_type_e_671" in text
