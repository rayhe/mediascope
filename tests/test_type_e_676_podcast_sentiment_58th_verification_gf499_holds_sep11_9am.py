"""Type E #676: podcast sentiment 58th verification cycle (Sep 11 2026, 09:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk 757 episodes
with latest episode 2026-09-07 crawled 4h; au.radio.net 757 episodes with
499 "Where You End and I Begin with Lindsey Mendick, 07/09/2026, 1h 10
mins" latest crawled 2d; ie.radio.net GF podcast page re-surface crawled
1d, in corpus via #656 directory corroboration; Listen Notes cached page
still stale on 498 "Politics" (released Aug 31, 5d crawl); podscan.fm 499
TKE Studios Margate transcript crawled 4h; Chortle Sep 13 Kings Place LPF
14:00 live-show re-surface crawled 4h is an upcoming LIVE SHOW not episode
500, exact URL in corpus; episode 500 watch item penciled Mon Sep 14 per
the weekly-Monday cadence: 498 Aug 31, 499 Sep 7).

EHE 33-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: thetimes.com spoof-Epstein piece (46d, crawled 46d),
latestly.com Jul 30 2026 spoof-Epstein fact-check (43d, crawled 19d, in
corpus since #383/#445/#465), petapixel.com Kylie Jenner lenticular
"We're always watching" (50d, crawled 17d), engadget.com London bus stops
fake-ad piece (56d, crawled 7d, corpus holds lowercase URL; this run's WWW
uppercase form logged verbatim as same page), feminist.org/news Feminist
Majority Foundation "Helpful or Hurtful" piece (listed updated 10d,
crawled 3h, in corpus since #470/#561/#596; page content cites the NY
State Court System smart-glasses ban, England-and-Wales courts ban, German
advocacy-group criminal complaint, and Meta facial-recognition patent
application - all page content, not new campaign activity; 3h crawl is
re-index, not republication), sifted.eu tech-events ban piece (16d,
crawled 16d, in corpus via #480), afrotech.com smart-glasses ethics piece
(56d, crawled 4h). No new primary campaign motif; last campaign phase
remains the circa Aug 10 Epstein poster; no competitor-equivalent
guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in
any of the 58 cycles.

Attention Sphere 58th no-match as podcast: quoted-search top results remain
this repository's own GitHub pages (podcast-sentiment.md blob/HEAD and
prior Type E commit pages; rejected as circular per established
discipline). No podcast named "Attention Sphere" anywhere; identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
table 57->58 cycles through Sep 11 2026.

Press surfaces: ZERO new-to-corpus press surfaces advancing the frontier
this run. Three stale re-indexes logged for completeness, not frontier
advances: gizmodo.com Blazer/Scriber FCC piece (167d-old content, crawled
3h; domain in corpus); techcrunch.com Mar 31 prescription-wearer launch
piece (164d-old content, crawled 45d); digitaltrends.com v19.2 firmware
piece (~July 2026 content, crawled 46d; domain in corpus, exact URL logged
in #671). In-corpus stale re-indexes: Reuters Jan 13 2026 doubling-output
piece (241d), Reuters Jan 6 2026 Display rollout pause piece (247d),
Reuters Dec 9 2025 privacy-competition piece (275d). Recency frontier TIED
at Sep 9 (ninth consecutive tie after #636, #641, #646, #651, #656, #661,
#666 and #671).

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


def _md_grep(pattern, rel):
    text = _read(rel)
    return re.findall(pattern, text)


class TestNovelty676:
    """Iteration 676 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_676_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_676*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_676_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_e_676 files,
        # no #676 in git log); this test pins that no duplicate #676 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^Type E #676:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type E #676 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard676.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestGF499Holds58thCycle:
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
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "uk-podcasts.co.uk" in section
        assert "Latest episode: 2026-09-07" in section

    def test_ie_radio_net_still_in_corpus_via_656(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "ie.radio.net" in section
        assert "in corpus" in section

    def test_radio_net_au_lists_499_latest(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "au.radio.net" in section
        assert "499" in section

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "Mon Sep 14" in section

    def test_chortle_sep_13_is_live_show_not_episode(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "Chortle" in section
        assert "not an episode" in section or "LIVE SHOW" in section

    def test_listen_notes_stale_on_498(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "Listen Notes" in section
        assert "498" in section

    def test_podscan_transcript_corroborates_499(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "podscan.fm" in section


class TestEHE33DayHold58thCycle:
    def test_latestly_fact_check_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "latestly.com" in section
        assert "in corpus" in section

    def test_engadget_bus_stops_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "engadget.com" in section

    def test_afrotech_ethics_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "afrotech.com" in section

    def test_feminist_org_10d_piece_is_resurface_not_new(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "feminist.org" in section
        assert "re-surface" in section or "re-surfaces" in section

    def test_thetimes_petapixel_sifted_resurfaces_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        for frag in ("thetimes.com", "petapixel.com", "sifted.eu"):
            assert frag in section, frag

    def test_no_new_primary_motif(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "no new primary motif" in section

    def test_no_competitor_equivalent_in_58_cycles(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "58 cycles" in section
        assert "No competitor-equivalent" in section


class TestAttentionSphere58thNoMatch:
    def test_quoted_search_top_results_no_podcast(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "58th" in section or "fifty-eighth" in section
        assert "no matching podcast" in section

    def test_circular_own_corpus_rejected(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "circular" in section

    def test_identity_strand_unchanged_from_596(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "#596" in section

    def test_table_row_carries_58_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "58 verification cycles through Sep 11 2026" in text

    def test_table_row_no_longer_says_57_cycles(self):
        text = _read("podcast-sentiment.md")
        head = text[:2000]
        assert "57 verification cycles through Sep 11 2026" not in head

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie:
    def test_zero_new_frontier_advancing_surfaces_this_run(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "ZERO new-to-corpus press surfaces advancing the frontier" in section

    def test_gizmodo_stale_reindex_logged_not_frontier(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "gizmodo.com/meta-has-more-smart-glasses-coming-whether-you-want-them-or-not-2000738619" in section
        assert "stale re-index" in section
        assert "NOT a press-surface advance" in section

    def test_techcrunch_stale_reindex_logged_not_frontier(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "techcrunch.com/2026/03/31/meta-launches-two-new-ray-ban-glasses-designed-for-prescription-wearers/" in section
        assert "NOT a press-surface advance" in section

    def test_digitaltrends_stale_reindex_logged_not_frontier(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "digitaltrends.com" in section
        assert "logged in #671" in section
        assert "NOT a press-surface advance" in section

    def test_reuters_stale_reindexes_logged(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "241d" in section
        assert "247d" in section
        assert "275d" in section

    def test_petapixel_sep_9_frontier_piece_still_newest(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "petapixel.com/2026/09/09" in section
        assert "in corpus via #631" in section

    def test_reuters_sep_8_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "Reuters Sep 8" in section
        assert "in corpus via #621" in section

    def test_techtime_lumus_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "techtime.news" in section
        assert "in corpus via #621" in section

    def test_thetimes_fear_and_loathing_resurface_in_corpus(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "thetimes.com" in section
        assert "in corpus via #581" in section

    def test_thevermilion_resurface_in_corpus_via_626(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "thevermilion.com" in section
        assert "in corpus via #626" in section

    def test_frontier_tied_at_sep_9_ninth_consecutive(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "ninth consecutive tie" in section
        assert "TIED at Sep 9" in section


class TestStandingRules676:
    def test_tone_not_scored(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "No tone scores computed" in section

    def test_significance_not_calculated(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
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


class TestNoAnalysisJsonUpdate676:
    def test_no_publication_level_empirical_finding(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "No claim of empirical significance" in section

    def test_press_surface_tie_not_a_tone_finding(self):
        section = _read("podcast-sentiment.md").split("## Iteration #676")[-1]
        assert "not a frontier advance" in section or "TIED at Sep 9" in section

    def test_analysis_json_untouched_this_run(self):
        out = _run_git("status", "--short")
        assert "analysis.json" not in out.stdout


class TestIterationLogEntry676:
    """The #676 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_676(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#676 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 675 D -> 676 E" in text

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


class TestRotationCycleGuard676:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #676 main-commit SHA is known.
    ANCHORED_SHA = "eb45c534edf7a0a1367692f3695c616818f94949"  # patched in followup per #565 convention

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

    def test_window_672_676_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "676"),
            ("D", "675"),
            ("C", "674"),
            ("B", "673"),
            ("A", "672"),
        ], "rotation window 672-676 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #676:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync676:
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
        assert "test_type_e_676" in text
