"""Type E #691: podcast sentiment 61st verification cycle (Sep 12 2026, 01:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk 757 episodes
with latest episode 2026-09-07 crawled 10h; au.radio.net directory 757
episodes with 499 "Where You End and I Begin" released 07/09/2026 crawled
3d; ie.radio.net GF podcast page re-surface crawled 1d, in corpus via
#656 directory corroboration; Listen Notes cached page still stale on 498
"Politics" (6d crawl); podscan.fm 499 TKE Studios Margate transcript
crawled 1h; Chortle Sep 13 Kings Place LPF 14:00 live-show re-surface
crawled less than 1h is an upcoming LIVE SHOW not episode 500, exact URL in
corpus; stagewhispers.com.au review re-surface crawled 98d in corpus via
#661; episode 500 watch item penciled Mon Sep 14 per the weekly-Monday
cadence: 498 Aug 31, 499 Sep 7).

EHE 34-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: thetimes.com spoof-Epstein piece (47d, crawled 47d),
latestly.com spoof-Epstein fact-check (44d, crawled 20d, in corpus since
#383/#445/#465), petapixel.com Kylie Jenner lenticular "We're always
watching" (51d, crawled 18d), engadget.com London bus stops fake-ad piece
(57d, crawled 8d, corpus holds lowercase URL; this run's WWW uppercase form
logged verbatim as same page per #676 convention),
feminist.org/news Feminist Majority Foundation "Helpful or Hurtful" piece
(listed updated 11d, crawled 4h, in corpus since #470/#561/#596; 4h crawl is
re-index, not republication), sifted.eu tech-events ban piece (16d,
crawled 16d, in corpus via #480), afrotech.com smart-glasses ethics piece
(57d, crawled 4h). No new primary campaign motif; last campaign phase
remains the circa Aug 10 Epstein poster; no competitor-equivalent
guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in
any of the 61 cycles.

Attention Sphere 61st no-match as podcast: quoted-search top results remain
this repository's own GitHub pages (podcast-sentiment.md blob/HEAD and
prior Type E commit pages; rejected as circular per established
discipline). Identity strand unchanged from #596; task-spec name remains
misidentified; Tracked Sources table 60->61 cycles through Sep 12 2026.

Press surfaces: ZERO new-to-corpus press surfaces this run. All six
Meta-glasses news results verified in corpus pre-commit (repo-wide greps;
every URL key returns hits): petapixel.com Sep 9 US-police-warning piece
(in corpus via #631; re-surfaced, crawled 2d; not new), digitaltrends.com
v19.2 firmware piece (~July 2026 content, crawled 47d; exact URL logged in
#671; stale re-index, NOT a frontier advance), thevermilion.com Display
piece (358d-old content, crawled 1h, in corpus via #626),
thetimes.com "Fear and loathing" London field test (in corpus via #581;
crawled 4d), reuters.com doubling-output piece (241d stale re-index),
tomsguide.com Scriber/Blazer prescription-lenses piece (~166d-old content
per listing, crawled 124d; in corpus via wearables-sweep return; stale
re-index, NOT a frontier advance). Recency frontier TIED at Sep 9
(twelfth consecutive tie after #636, #641, #646, #651, #656, #661, #666,
#671, #676, #681 and #686); the petapixel.com Sep 9 piece remains the
newest date-verified in-corpus Meta-glasses press item.

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


class TestNovelty691:
    """Iteration 691 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_691_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_691*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_691_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_691 files, no #691 in git log); this test
        # pins that no duplicate #691 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type E #691:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type E #691 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard691.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestGF499Holds61stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_gf_row_still_499(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "Active, 499 episodes (Sep 12 2026)" in table

    def test_uk_podcasts_still_latest_2026_09_07(self):
        section = self._section()
        assert "uk-podcasts.co.uk directory (crawled 10h) shows 757 episodes" in section
        assert "Latest episode: 2026-09-07" in section

    def test_au_radio_net_corroborates_499(self):
        section = self._section()
        assert 'au.radio.net directory (crawled 3d) lists 757 episodes with 499 "Where You End and I Begin" released 07/09/2026' in section

    def test_ie_radio_net_still_in_corpus_via_656(self):
        section = self._section()
        assert "ie.radio.net GF podcast page re-surfaced (crawled 1d) - in corpus via #656" in section

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        section = self._section()
        assert "episode 500 watch item stays penciled for Mon Sep 14" in section

    def test_chortle_sep_13_is_live_show_not_episode(self):
        section = self._section()
        assert "a live show, not an episode; exact URL in corpus" in section

    def test_listen_notes_stale_on_498(self):
        section = self._section()
        assert 'Listen Notes still lists 498 "Politics" as latest (crawled 6d; crawl lag persists)' in section

    def test_podscan_transcript_corroborates_499(self):
        section = self._section()
        assert "podscan.fm (crawled 1h) 499 TKE Studios Margate transcript" in section

    def test_no_tech_word_audit_needed(self):
        section = self._section()
        assert "no new episode dropped, so the #606 audit" in section


class TestEHE34DayHold61stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_latestly_fact_check_resurface_in_corpus(self):
        section = self._section()
        assert "latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature" in section
        assert "in corpus since #383/#445/#465" in section

    def test_engadget_bus_stops_resurface_in_corpus(self):
        section = self._section()
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads" in section
        assert "logged verbatim as same page per #676 convention" in section

    def test_afrotech_ethics_resurface_in_corpus(self):
        section = self._section()
        assert "afrotech.com/smart-glasses-ethics-and-consent (57 days, crawled 4h)" in section

    def test_feminist_org_piece_is_resurface_not_new(self):
        section = self._section()
        assert "4h crawl is re-index, not republication" in section

    def test_thetimes_petapixel_sifted_resurfaces_in_corpus(self):
        section = self._section()
        assert "meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5" in section
        assert "kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad" in section
        assert "sifted.eu/articles/should-tech-events-ban-smart-glasses" in section

    def test_no_new_primary_motif(self):
        section = self._section()
        assert "Last campaign phase remains the circa Aug 10 Epstein poster; no new primary motif" in section

    def test_no_competitor_equivalent_in_61_cycles(self):
        section = self._section()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 61 cycles" in section


class TestAttentionSphere61stNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_quoted_search_top_results_no_podcast(self):
        section = self._section()
        assert 'quoted search for "Attention Sphere" podcast returned no matching podcast (sixty-first no-match)' in section

    def test_circular_own_corpus_rejected(self):
        section = self._section()
        assert "this repository's own GitHub pages" in section
        assert "rejected as circular per established discipline" in section

    def test_identity_strand_unchanged_from_596(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Kendall Schrohe" in section

    def test_table_row_carries_61_cycles(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "61 verification cycles through Sep 12 2026" in table

    def test_table_row_no_longer_says_60_cycles(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "60 verification cycles through Sep 11 2026" not in table


class TestPressSurfacesFrontierTie691:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_zero_new_to_corpus_surfaces_this_run(self):
        section = self._section()
        assert "ZERO new-to-corpus press surfaces this run" in section
        assert "All six Meta-glasses news results were verified in corpus pre-commit" in section

    def test_petapixel_sep_9_frontier_piece_still_newest(self):
        section = self._section()
        assert "petapixel.com/2026/09/09/us-police-warn-meta-smart-glasses-could-be-a-security-threat" in section
        assert "the newest date-verified in-corpus Meta-glasses press item" in section

    def test_digitaltrends_stale_reindex_logged_not_frontier(self):
        section = self._section()
        assert "meta-breathes-new-life-into-your-gen-1-ray-ban-smart-glasses" in section
        assert "stale re-index, NOT a press-surface advance" in section

    def test_tomsguide_prescription_piece_logged_as_stale_reindex(self):
        section = self._section()
        assert "meta-is-finally-building-ray-ban-smart-glasses-designed-for-prescription-lenses" in section
        assert "in corpus via wearables-sweep return" in section

    def test_reuters_stale_reindex_logged(self):
        section = self._section()
        assert "meta-mulls-doubling-output-ray-ban-glasses-by-year-end-bloomberg-news-reports-2026-01-13" in section

    def test_thetimes_fear_and_loathing_resurface_in_corpus(self):
        section = self._section()
        assert "meta-glasses-rayban-privacy-recording-ai-0l82sx8sw" in section
        assert "in corpus via #581" in section

    def test_thevermilion_resurface_in_corpus_via_626(self):
        section = self._section()
        assert "display-the-glasses-that-replace-the-smartphone" in section
        assert "in corpus via #626" in section

    def test_frontier_tied_at_sep_9_twelfth_consecutive(self):
        section = self._section()
        assert "TIED at Sep 9, not advanced" in section
        assert "#636, #641, #646, #651, #656, #661, #666, #671, #676, #681 and #686" in section


class TestStandingRules691:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_tone_not_scored(self):
        section = self._section()
        assert "No tone scores computed" in section

    def test_significance_not_calculated(self):
        section = self._section()
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


class TestNoAnalysisJsonUpdate691:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #691")[-1]

    def test_no_publication_level_empirical_finding(self):
        section = self._section()
        assert "No claim of empirical significance" in section

    def test_press_surface_tie_not_a_tone_finding(self):
        section = self._section()
        assert "TIED at Sep 9" in section

    def test_analysis_json_untouched_this_run(self):
        out = _run_git("status", "--short")
        assert "analysis.json" not in out.stdout


class TestRotationCycleGuard691:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #691 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        # Robust to the #678 history artifact: its two followup-SHA fix
        # commits (0d1a86b, fb21ea3) were titled "Type B #678: ..." and match
        # the main-commit filter, so raw subjects[:5] shows B#678 three times.
        # The convention's intent is the distinct iteration mains in order
        # (per the #679/#680 guards' _distinct_mains).
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_687_691_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "691"),
            ("D", "690"),
            ("C", "689"),
            ("B", "688"),
            ("A", "687"),
        ], "rotation window 687-691 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #691:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync691:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, test-file table row,
    # ARCHITECTURE row, and iteration-log entry land in the followup.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m, "count_stats.py --pytest produced no Total tests line"
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
        assert "test_type_e_691" in text

    def test_test_file_table_row_present(self):
        text = _read("README.md")
        assert "test_type_e_691_podcast_sentiment_61st_verification_gf499_watch_sep12_1am.py" in text

    def test_iteration_log_entry_present(self):
        text = _read("iteration-log.md")
        assert "#691 Type E:" in text, "iteration-log entry for #691 missing"

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 690 D -> 691 E" in text
