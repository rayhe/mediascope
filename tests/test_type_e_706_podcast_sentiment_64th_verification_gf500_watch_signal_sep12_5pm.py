"""Type E #706: podcast sentiment 64th verification cycle (Sep 12 2026, 17:00 PDT).

Guilty Feminist 499 HOLDS at every directory with multi-day crawl lag; uk-podcasts.co.uk
flipped from 757 episodes / "Latest episode: 2026-09-07" (crawled 4h at #701) to 758
episodes / "Latest episode: 2026-09-12" (crawled 5h) - consistent with an off-cadence
Saturday drop of episode 500, but UNVERIFIED: the title-verification search returned no
episode-500 title, podscan.fm (crawled 5h) still shows the 499 transcript as newest,
au.radio.net (crawled 4d) still lists 757 episodes with 499 latest, Listen Notes (crawled
6d) still lags on 498, and the planned first-hand page read failed upstream this run.
No drop asserted per #503/iteration-492 discipline. The 500-watch item is ADVANCED:
episode 500 may have dropped as early as Sep 12, still penciled Mon Sep 14.

EHE 34-day hold continues: 7 re-surfaces observed this run, ALL verified in corpus
pre-commit: thetimes.com spoof-Epstein piece (48d, crawled 48d), latestly.com
spoof-Epstein fact-check (45d, crawled 21d, in corpus since #383/#445/#465),
petapixel.com Kylie Jenner lenticular "We're always watching" (52d, crawled 18d),
engadget.com London bus stops fake-ad piece (58d, crawled 8d, corpus holds lowercase
URL; this run's WWW uppercase form logged verbatim as same page per #676 convention),
feminist.org/news Feminist Majority Foundation "Helpful or Hurtful" piece (listed
updated 12d, crawled 2h, in corpus since #470/#561/#596; re-index, not republication),
sifted.eu tech-events ban piece (17d, crawled 17d, in corpus via #480), afrotech.com
smart-glasses ethics piece (58d, crawled 5h). No new primary campaign motif; last
campaign phase remains the circa Aug 10 Epstein poster; no competitor-equivalent
guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 64
cycles.

Attention Sphere 64th no-match as podcast: quoted-search top results were this
repository's own GitHub pages (rejected as circular per established discipline), the
creators.spotify.com Purposeful Empathy episode page with Ava Smithing as guest
(re-surfaced, crawled less than 1h; exact anita-nowak URL in corpus since #551-#586;
episode description labels "The Attention Sphere: Ava's non-profit organization" -
independent third-party corroboration of the nonprofit, not-podcast identity), and a
pulse.bot episode about a different "Spheres of Attention" productivity framework
(Mike Vardy; 80d/73d; unrelated concept, not a podcast named Attention Sphere).
Identity strand unchanged from #596; task-spec name remains misidentified; Tracked
Sources table 63->64 cycles through Sep 12 2026.

Press surfaces: ZERO new-to-corpus editorial press surfaces this run. Six news results
observed; five were verified in corpus pre-commit under previously logged URL keys,
and ONE URL key is logged verbatim in the podcast-sentiment.md section as a STALE
RE-INDEX of old editorial content (domain already corpus-known; no new editorial
content): reuters delays-global-rollout (249d stale re-index; also surfaced with a
?share=twitter param this run, a param-variant of the logged base key), digitaltrends
v19.2 firmware piece (~July 2026 content, crawled 47d, exact URL logged in #671, stale
re-index, NOT a press-surface advance), reuters doubling-output (242d stale re-index),
androidpolice Mar 31 2026 Blayzer/Scriber styles piece (165-day-old content, crawled
11d; URL key logged in #701; stale re-index), techcrunch Jan 6 2026 pause-expansion
piece (crawled 3d; NEW URL KEY this run; stale re-index of old content; NOT a frontier
advance), gizmodo FCC Blazer/Scriber piece (169-day-old content, crawled less than 1h;
in corpus via #676). The new URL key is now corpus-logged so future repo-wide greps
catch it. Recency frontier TIED at Sep 9 (fifteenth consecutive tie after #636, #641,
#646, #651, #656, #661, #666, #671, #676, #681, #686, #691, #696 and #701); the
petapixel.com Sep 9 piece remains the newest date-verified in-corpus Meta-glasses
press item.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d NOT_CALCULATED,
is_significant False; Type E monitoring-only, no mechanism block in profiles/. No
analysis.json update warranted.
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


class TestNovelty706:
    """Iteration 706 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_706_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_706*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_706_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_706 files, no #706 in git log); this test
        # pins that no duplicate #706 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type E #706:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type E #706 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard706.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestGF64thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_gf_row_still_499(self):
        assert "Active, 499 episodes (Sep 12 2026)" in self._table()

    def test_uk_podcasts_flipped_to_758_latest_2026_09_12(self):
        section = self._section()
        assert "758 episodes" in section
        assert '"Latest episode: 2026-09-12"' in section
        assert "crawled 5h" in section

    def test_flip_is_unverified_single_directory_signal(self):
        section = self._section()
        assert "UNVERIFIED" in section
        assert "single-directory signal" in section
        assert "no drop is asserted" in section

    def test_no_episode_500_title_in_verification_search(self):
        section = self._section()
        assert "title-verification search for episode 500 returned no episode-500 title" in section

    def test_au_radio_net_still_499_stale_4d(self):
        section = self._section()
        assert "au.radio.net (crawled 4d) still lists 757 episodes with 499 latest" in section

    def test_listen_notes_stale_on_498(self):
        section = self._section()
        assert "Listen Notes (crawled 6d) still lags on 498" in section

    def test_podscan_499_newest_5h(self):
        section = self._section()
        assert "podscan.fm (crawled 5h) still shows the 499 transcript as the newest numbered release" in section

    def test_chortle_sep_13_is_live_show_not_episode(self):
        section = self._section()
        assert "Chortle Sep 13 Kings Place LPF 14:00 live-show re-surface (crawled <1h) - a live show, not episode 500" in section

    def test_episode_500_watch_advanced_to_possible_sep_12(self):
        section = self._section()
        assert "500-watch ADVANCED" in section
        assert "may have dropped as early as Sep 12" in section
        assert "still penciled Mon Sep 14" in section

    def test_fetch_failure_recorded_no_assertion_of_drop(self):
        section = self._section()
        assert "first-hand page read failed upstream" in section
        assert "browser_open upstream_unavailable" in section


class TestEHE34DayHold64thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL verified in corpus pre-commit" in section
        assert "every URL key returns hits" in section

    def test_thetimes_latestly_petapixel_engadget_hits(self):
        section = self._section()
        assert "meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5 (48 days, crawled 48d)" in section
        assert "7538349.html (45 days, crawled 21d; in corpus since #383/#445/#465)" in section
        assert "kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/ (52 days, crawled 18d)" in section
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/ (58 days, crawled 8d" in section

    def test_feminist_org_sifted_afrotech_hits(self):
        section = self._section()
        assert "feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/ (listed updated 12d, crawled 2h" in section
        assert "sifted.eu/articles/should-tech-events-ban-smart-glasses/ (17 days, crawled 17d; in corpus via #480)" in section
        assert "afrotech.com/smart-glasses-ethics-and-consent (58 days, crawled 5h)" in section

    def test_no_new_primary_motif(self):
        section = self._section()
        assert "no new primary motif" in section

    def test_last_phase_circa_aug_10_epstein_poster(self):
        section = self._section()
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section

    def test_no_competitor_equivalent_in_64_cycles(self):
        section = self._section()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 64 cycles" in section

    def test_hold_day_count_34(self):
        section = self._section()
        assert "34-day hold continues (Aug 10 -> Sep 12, inclusive count)" in section


class TestAttentionSphere64thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_quoted_search_no_podcast(self):
        section = self._section()
        assert "returned no matching podcast (sixty-fourth no-match)" in section

    def test_circular_own_corpus_rejected(self):
        section = self._section()
        assert "this repository's own GitHub pages (rejected as circular per established discipline)" in section

    def test_pulse_vardy_framework_excluded_as_unrelated(self):
        section = self._section()
        assert "pulse.bot episode about a different \"Spheres of Attention\" productivity framework (Mike Vardy; 80d/73d" in section

    def test_identity_strand_unchanged_from_596(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section

    def test_spotify_creators_nonprofit_corroboration_resurface_sub1h(self):
        section = self._section()
        assert "creators.spotify.com Purposeful Empathy episode page with Ava Smithing as guest (re-surfaced, crawled <1h" in section
        assert "\"The Attention Sphere: Ava's non-profit organization\"" in section

    def test_table_row_carries_64_cycles(self):
        assert "64 verification cycles through Sep 12 2026, all no-match as a podcast" in self._table()

    def test_table_row_no_longer_says_63_cycles(self):
        assert "63 verification cycles through Sep 12 2026" not in self._table()


class TestPressSurfacesFrontierTie706:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def test_zero_new_to_corpus_editorial_surfaces(self):
        section = self._section()
        assert "ZERO new-to-corpus editorial press surfaces this run." in section

    def test_one_new_url_key_techcrunch_pause_expansion_stale_reindex(self):
        section = self._section()
        assert "https://techcrunch.com/2026/01/06/meta-pauses-international-expansion-of-its-ray-ban-display-glasses/" in section
        assert "NEW URL KEY this run; Jan 6 2026 pause-expansion piece, crawled 3d; stale re-index of old content" in section

    def test_reuters_share_twitter_is_param_variant_of_logged_key(self):
        section = self._section()
        assert "also surfaced with a ?share=twitter param this run; param-variant of the logged base key, not a new surface" in section

    def test_gizmodo_fcc_piece_already_in_corpus_via_676(self):
        section = self._section()
        assert "https://gizmodo.com/meta-has-more-smart-glasses-coming-whether-you-want-them-or-not-2000738619" in section
        assert "in corpus via #676" in section

    def test_androidpolice_url_key_logged_in_701_stale_reindex(self):
        section = self._section()
        assert "new-ray-ban-meta-styles-are-great-news-for-people-who-want-to-wear-them-all-day/ (Mar 31 2026 Blayzer/Scriber styles piece, 165 days, crawled 11d; URL key logged in #701" in section

    def test_digitaltrends_reuters_stale_resurfaces(self):
        section = self._section()
        assert "meta-breathes-new-life-into-your-gen-1-ray-ban-smart-glasses/ (~July 2026 v19.2 firmware piece, crawled 47d; exact URL logged in #671" in section
        assert "meta-delays-global-rollout-ray-ban-display-glasses-strong-us-demand-supply-2026-01-06/ (Reuters Jan 2026 delays-global-rollout; 249 days, crawled 249d; in corpus)" in section
        assert "meta-mulls-doubling-output-ray-ban-glasses-by-year-end-bloomberg-news-reports-2026-01-13/ (Reuters Jan 2026 doubling-output; 242 days, crawled 242d; in corpus)" in section

    def test_frontier_tied_at_sep_9_fifteenth_consecutive(self):
        section = self._section()
        assert "Recency frontier:** TIED at Sep 9, not advanced (fifteenth consecutive tie after #636, #641, #646, #651, #656, #661, #666, #671, #676, #681, #686, #691, #696 and #701)" in section

    def test_new_url_key_hygiene_logged(self):
        section = self._section()
        assert "URL-key hygiene note:** the techcrunch pause-expansion key is logged verbatim here so future repo-wide greps catch it as corpus-known" in section


class TestTypeECycleIntegrity706:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_tracked_sources_table_carries_64_cycles(self):
        assert "64 verification cycles through Sep 12 2026" in self._table()

    def test_no_63_cycle_regression_in_table(self):
        assert "63 verification cycles through Sep 12 2026" not in self._table()

    def test_cycle_count_matches_section_ordinal(self):
        section = self._section()
        assert "Sixty-fourth Cycle" in section
        assert "sixty-fourth no-match" in section
        assert "sixty-fourth verification cycle is new" in section


class TestStandingRules706:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def test_tone_not_scored(self):
        section = self._section()
        assert "No tone scores computed on any episode this run (no verified new episode)" in section

    def test_significance_not_calculated(self):
        section = self._section()
        assert "p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant False" in section

    def test_no_profiles_mechanism_block(self):
        # Type E is monitoring-only; no profiles/ changes this run.
        out = subprocess.run(
            ["git", "status", "--short", "profiles/"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        assert out.stdout.strip() == "", "profiles/ must be untouched by Type E: %r" % (out.stdout,)


class TestNoAnalysisJsonUpdate706:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #706")[-1]

    def test_no_publication_level_empirical_finding(self):
        section = self._section()
        assert "No claim of empirical significance. Do not claim empirical significance." in section

    def test_press_surface_tie_not_a_tone_finding(self):
        section = self._section()
        assert "ZERO new-to-corpus editorial press surfaces this run." in section
        assert "TIED at Sep 9" in section

    def test_analysis_json_untouched_this_run(self):
        out = subprocess.run(
            ["git", "status", "--short"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        changed = [l for l in out.stdout.splitlines() if "analysis.json" in l]
        assert not changed, "analysis.json must be untouched: %r" % (changed,)


class TestRotationCycleGuard706:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #706 main-commit SHA is known.
    ANCHORED_SHA = "04d38ae9db5590a6f0849e38d77b2345e86c7791"

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

    def test_window_702_706_closes_a_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "706"),
            ("D", "705"),
            ("C", "704"),
            ("B", "703"),
            ("A", "702"),
        ], "rotation window 702-706 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #706:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync706:
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
        assert "test_type_e_706" in text

    def test_test_file_table_row_present(self):
        text = _read("README.md")
        assert "test_type_e_706_podcast_sentiment_64th_verification_gf500_watch_signal_sep12_5pm.py" in text

    def test_iteration_log_entry_present(self):
        text = _read("iteration-log.md")
        assert "#706 Type E:" in text, "iteration-log entry for #706 missing"

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 705 D -> 706 E" in text
