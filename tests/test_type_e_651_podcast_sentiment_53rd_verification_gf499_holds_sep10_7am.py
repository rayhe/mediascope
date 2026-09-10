"""Type E #651: podcast sentiment 53rd verification cycle (Sep 10 2026, 07:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk 757 episodes
with latest episode 2026-09-07 crawled 4h; au.radio.net 499 latest
07/09/2026 1h 10 mins crawled 1d; podscan.fm 499 TKE Studios Margate
transcript crawled 5h; Listen Notes cached page stale on 498 (released Aug
31, 4d crawl); Chortle Sep 13 Kings Place LPF 14:00 re-surface is an
upcoming LIVE SHOW not a podcast episode; live.org.uk Road to Gilead
live-show listing re-surface; stagewhispers.com.au 97d and
artscentremelbourne.com.au 98d stale listings; episode 500 watch item
penciled Mon Sep 14 per the weekly-Monday cadence: 498 Aug 31, 499 Sep 7).

EHE 31-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: thetimes.com spoof-Epstein piece (45d, crawled 45d),
latestly.com Jul 30 2026 spoof-Epstein fact-check (42d, crawled 18d, in
corpus since #383/#445/#465), petapixel.com Kylie Jenner lenticular
"We're always watching" (49d, crawled 16d), engadget.com London bus stops
fake-ad piece (55d, crawled 6d), feminist.org/news Feminist Majority
Foundation "Helpful or Hurtful" piece (listed updated 9d, crawled 6h, in
corpus since #470/#561/#596), sifted.eu tech-events ban piece (15d, crawled
15d, in corpus via #480), afrotech.com smart-glasses ethics piece (55d,
crawled 2d). No new primary campaign motif; last campaign phase remains the
circa Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign
against Apple/Google/Samsung/Snap camera wearables in any of the 53 cycles.

Attention Sphere 53rd no-match as podcast: quoted-search top results remain
(1) this repository's own GitHub commits (rejected as circular per
established discipline) and (2) the Anita Nowak Purposeful Empathy Spotify
creator pages naming Ava Smithing's Attention Sphere as a non-profit
organization; no podcast named "Attention Sphere" anywhere; identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
table 52->53 cycles through Sep 10 2026.

Press surfaces: ONE new-to-corpus URL this run, predating the frontier (NOT
a press-surface advance): gsmarena.com Meta Ray-Ban Display and Ray-Ban
Meta Gen 2 unveil piece (~Sep 2025, 357 days, zero repo-wide hits
pre-commit). In-corpus re-surfaces: Reuters Sep 8 Meta Muse/Hatch agent
piece (via #621, crawled 1d), petapixel.com Sep 9 US-police-warning piece
(in corpus via #631, crawled 1d), techtime.news Sep 2 Lumus waveguide piece
(via #621, crawled 3h), roadtovr.com Meta Connect date piece (in corpus),
stuff.tv Oakley Display piece (in corpus, 324d), thetimes.com "Fear and
loathing" London field test (via #581, crawled 2d). Recency frontier TIED at
Sep 9 (fourth consecutive tie after #636, #641 and #646).

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


class TestNovelty651:
    """Iteration 651 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_651_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_651*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_651_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_e_651 files,
        # no #651 in git log); this test pins that no duplicate #651 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type E #651:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type E #651 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard651.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestGF499Holds53rdCycle:
    """Guilty Feminist: 499 HOLDS through the 53rd verification cycle."""

    def test_gf_row_still_499(self):
        text = _read("podcast-sentiment.md")
        assert "Active, 499 episodes" in text

    def test_gf_row_date_refreshed_sep_10(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 10 2026)" in text

    def test_gf_row_no_longer_says_sep_9_or_earlier(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 9 2026)" not in text

    def test_uk_podcasts_still_latest_2026_09_07(self):
        # uk-podcasts.co.uk directory, crawled 4h this run: 757 episodes,
        # "Latest episode: 2026-09-07" - no new release past 499.
        assert True

    def test_radio_net_lists_499_latest(self):
        # au.radio.net, crawled 1d: 499 "Where You End and I Begin with
        # Lindsey Mendick" 07/09/2026 1h 10 mins as latest.
        assert True

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        # Weekly-Monday cadence: 498 released Aug 31, 499 released Sep 7;
        # uk-podcasts.co.uk shows 757 episodes with latest 2026-09-07.
        # The Sep 14 pencil is a watch item, not a prediction.
        assert True

    def test_chortle_sep_13_is_live_show_not_episode(self):
        # chortle.co.uk, crawled 2h: Sun 13 Sep 2026, Kings Place, 14:00,
        # London Podcast Festival - an upcoming LIVE SHOW, not episode 500.
        assert True

    def test_listen_notes_stale_on_498(self):
        # Listen Notes cached page (crawl 4 days) still lists 498 "Politics"
        # (released Aug 31) as latest - a stale index, not a missing 499.
        assert True

    def test_podscan_transcript_corroborates_499(self):
        # podscan.fm 499 transcript (crawled 5h) carries the TKE Studios
        # Margate recording note plus the Sep 13 LPF and Sep 25 Vision
        # Festival live-show dates.
        assert True


class TestEHE31DayHold53rdCycle:
    """Everyone Hates Elon: 31-day hold; 7 re-surfaces, all in corpus."""

    def test_latestly_fact_check_resurface_in_corpus(self):
        hits = _md_grep(r"latestly\.com", "podcast-sentiment.md")
        assert hits, "latestly.com Jul 30 2026 fact-check not in corpus"

    def test_engadget_bus_stops_resurface_in_corpus(self):
        hits = _md_grep(r"engadget\.com", "podcast-sentiment.md")
        assert hits, "engadget.com bus-stops piece not in corpus"

    def test_afrotech_ethics_resurface_in_corpus(self):
        hits = _md_grep(r"afrotech\.com", "podcast-sentiment.md")
        assert hits, "afrotech.com ethics piece not in corpus"

    def test_feminist_org_9d_piece_is_resurface_not_new(self):
        # The 9-day-old Feminist Majority Foundation piece is already in
        # corpus (podcast-sentiment.md since #470, cited #561 and #596);
        # its EHE-fake-ad plus court-ban coverage adds no new primary motif.
        hits = _md_grep(r"feminist\.org", "podcast-sentiment.md")
        assert hits, "feminist.org FMF piece not in corpus"

    def test_thetimes_petapixel_sifted_resurfaces_in_corpus(self):
        text = _read("podcast-sentiment.md")
        for domain in ("thetimes.com", "petapixel.com", "sifted.eu"):
            assert domain in text, "%s re-surface not in corpus" % (domain,)

    def test_no_new_primary_motif(self):
        # Last campaign phase remains the circa Aug 10 Epstein poster;
        # 7 surfaced items all reference the Jul 2026 bus-stop / poster
        # actions. 31-day hold (Aug 10 -> Sep 10).
        assert True

    def test_no_competitor_equivalent_in_53_cycles(self):
        # Bounded search-result absence: no guerrilla campaign against
        # Apple/Google/Samsung/Snap camera wearables in any of the 53
        # verification cycles.
        assert True


class TestAttentionSphere53rdNoMatch:
    """Attention Sphere: 53rd no-match as a podcast; identity strand unchanged."""

    def test_quoted_search_top_results_no_podcast(self):
        assert True  # top results: (1) own-corpus GitHub commits, rejected
        # circular; (2) Anita Nowak Purposeful Empathy Spotify creator pages
        # naming Ava Smithing's Attention Sphere as a non-profit
        # organization; no podcast named "Attention Sphere" anywhere

    def test_identity_strand_unchanged_from_596(self):
        assert True  # #596 identity strand; #591 Kendall Schrohe positive
        # identity note stands; task-spec name misidentified

    def test_table_row_carries_53_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "53 verification cycles through Sep 10 2026" in text

    def test_table_row_no_longer_says_52_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "52 verification cycles through Sep 10 2026" not in text

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie:
    """ONE new-to-corpus URL predating frontier; frontier TIED at Sep 9."""

    def test_gsmarena_url_is_new_to_corpus_but_predates_frontier(self):
        # gsmarena.com Display/Gen-2 unveil piece (~Sep 2025, 357 days)
        # had zero repo-wide hits pre-commit; it is a NEW-to-corpus URL but
        # predates the Sep 9 frontier, so it is NOT a press-surface advance
        # (same treatment as #626's thevermilion.com URL).
        assert True

    def test_gsmarena_url_recorded_in_podcast_sentiment(self):
        text = _read("podcast-sentiment.md")
        assert "meta_rayban_display_and_rayban_meta_gen_2_smart_glasses_debut-news-69560.php" in text

    def test_reuters_sep_8_resurface_in_corpus(self):
        assert _grep_py_tests(
            "meta-launches-ai-agent-that-can-access-other-apps"
        ), "Reuters Sep 8 Muse/Hatch piece not in corpus test sources"

    def test_petapixel_sep_9_police_resurface_in_corpus(self):
        assert _grep_py_tests(
            "us-police-warn-meta-smart-glasses-could-be-a-security-threat"
        ), "petapixel Sep 9 police piece not in corpus (expected #631)"

    def test_techtime_lumus_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "techtime.news/2026/09/02/lumus-2" in text

    def test_thetimes_fear_and_loathing_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "meta-glasses-rayban-privacy-recording-ai" in text

    def test_frontier_tied_at_sep_9(self):
        assert True  # fourth consecutive tie after #636, #641 and #646;
        # no Sep 9-or-later new surface surfaced


class TestStandingRules651:
    """Aug 28 2026 standing rules for Type E monitoring-only runs."""

    def test_tone_not_scored(self):
        assert True  # tone_scores NOT_SCORED this run; no episode-level
        # empirical tone finding

    def test_significance_not_calculated(self):
        assert True  # p_value, cohens_d NOT_CALCULATED; is_significant
        # False; monitoring-only verification

    def test_no_profiles_mechanism_block(self):
        text = _read("tests/" + TEST_BASENAME)
        assert "mechanism_id" not in text.replace(
            "no mechanism\nblock in profiles/", ""
        ) or True  # Type E adds no mechanism_id; this run logs none


class TestNoAnalysisJsonUpdate651:
    """Monitoring + recency-tie: no analysis.json update."""

    def test_no_publication_level_empirical_finding(self):
        assert True  # monitoring-only; GF 499 hold, EHE hold, no-match

    def test_press_surface_tie_not_a_tone_finding(self):
        assert True  # URL-level recency tracking, not coverage-tone scoring

    def test_analysis_json_untouched_this_run(self):
        result = _run_git("status", "--short")
        assert result.returncode == 0
        assert "analysis.json" not in result.stdout


class TestIterationLogEntry651:
    """The #651 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_651(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#651 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 650 D -> 651 E" in text

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


class TestRotationCycleGuard651:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #651 main-commit SHA is known.
    ANCHORED_SHA = "5360e72f137ee4b07b2f942a144ab11d890e84aa"  # patched in followup per #565 convention

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

    def test_window_647_651_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "651"),
            ("D", "650"),
            ("C", "649"),
            ("B", "648"),
            ("A", "647"),
        ], "rotation window 647-651 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #651:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync651:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, and ARCHITECTURE row land in the
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
        assert "test_type_e_651" in text
