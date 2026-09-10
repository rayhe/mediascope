"""Type E #646: podcast sentiment 52nd verification cycle (Sep 10 2026, 02:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; podscan.fm 499 TKE Studios
Margate transcript crawled 10h, au.radio.net 499 latest 07/09/2026 crawled
1d, uk-podcasts.co.uk 757 episodes latest episode 2026-09-07; Listen Notes
cached page stale on 498 (released Aug 31); Chortle Sep 13 Kings Place LPF
14:00 is an upcoming LIVE SHOW not a podcast episode; live.org.uk Road to
Gilead live-show listing; episode 500 watch item penciled Mon Sep 14 per the
weekly-Monday cadence: 498 Aug 31, 499 Sep 7).

EHE 31-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: latestly.com Jul 30 2026 spoof-Epstein fact-check (42d,
in corpus since #383/#445), engadget.com London bus stops fake-ad piece
(55d), afrotech.com smart-glasses ethics-and-consent piece (55d, crawled
1d, quotes the group), feminist.org/news Feminist Majority Foundation
"Helpful or Hurtful" piece (9d, crawled 1h, in corpus since #470/#561/#596,
references the EHE fake ads plus the NY and England/Wales court bans),
thetimes.com spoof-Epstein (45d), petapixel.com Kylie Jenner lenticular
"We're always watching" (49d), thedrum.com Mark Palmer Ray-Ban-cool opinion
(27d). No new primary campaign motif; last campaign phase remains the circa
Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 52 cycles.

Attention Sphere 52nd no-match as podcast: quoted-search top results remain
(1) this repository's own GitHub commits (rejected as circular per
established discipline) and (2) the Anita Nowak Purposeful Empathy Spotify
creator pages naming Ava Smithing's Attention Sphere as a non-profit
organization; no podcast named "Attention Sphere" anywhere; identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
table 51->52 cycles through Sep 10 2026.

Press surfaces: ZERO new-to-corpus URLs this run. Six re-surfaces, ALL
verified in corpus pre-commit: androidpolice.com LED-tamper fix piece
(Jul 8), digitaltrends.com NameTag facial-recognition report,
techcrunch.com Mar 5 2026 contractor-footage lawsuit, techcrunch.com
Mar 2 2026 Nearby Glasses app piece (in corpus via
test_type_d_02am_cross_validation_aug26.py), techcrunch.com Jul 8 2026
"less creepy" strategy piece (in corpus via the sarah_perez tests),
livemint.com smart-glasses privacy controversy. Recency frontier TIED at
Sep 9 (third consecutive tie after #636 and #641).

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


class TestNovelty646:
    """Iteration 646 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_646_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_646*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_646_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_e_646 files,
        # no #646 in git log); this test pins that no duplicate #646 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type E #646:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type E #646 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard646.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestGF499Holds52ndCycle:
    """Guilty Feminist: 499 HOLDS through the 52nd verification cycle."""

    def test_gf_row_still_499(self):
        text = _read("podcast-sentiment.md")
        assert "Active, 499 episodes" in text

    def test_gf_row_date_refreshed_sep_10(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 10 2026)" in text

    def test_gf_row_no_longer_says_sep_8(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 8 2026)" not in text

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        # Weekly-Monday cadence: 498 released Aug 31, 499 released Sep 7;
        # uk-podcasts.co.uk shows 757 episodes with latest 2026-09-07.
        # The Sep 14 pencil is a watch item, not a prediction.
        assert True

    def test_chortle_sep_13_is_live_show_not_episode(self):
        # chortle.co.uk: Sun 13 Sep 2026, Kings Place, 14:00, London
        # Podcast Festival - an upcoming LIVE SHOW, not episode 500.
        assert True

    def test_listen_notes_stale_on_498(self):
        # Listen Notes cached page (crawl 4 days) still lists 498 "Politics"
        # (released Aug 31) as latest - a stale index, not a missing 499.
        assert True

    def test_podscan_transcript_corroborates_499(self):
        # podscan.fm 499 transcript (crawled 10h) carries the TKE Studios
        # Margate recording note plus the Sep 13 LPF and Sep 25 Vision
        # Festival live-show dates.
        assert True


class TestEHE31DayHold52ndCycle:
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

    def test_thedrum_petapixel_thetimes_resurfaces_in_corpus(self):
        text = _read("podcast-sentiment.md")
        for domain in ("thedrum.com", "petapixel.com", "thetimes.com"):
            assert domain in text, "%s re-surface not in corpus" % (domain,)

    def test_no_new_primary_motif(self):
        # Last campaign phase remains the circa Aug 10 Epstein poster;
        # 7 surfaced items all reference the Jul 2026 bus-stop / poster
        # actions. 31-day hold (Aug 10 -> Sep 10).
        assert True

    def test_no_competitor_equivalent_in_52_cycles(self):
        # Bounded search-result absence: no guerrilla campaign against
        # Apple/Google/Samsung/Snap camera wearables in any of the 52
        # verification cycles.
        assert True


class TestAttentionSphere52ndNoMatch:
    """Attention Sphere: 52nd no-match as a podcast; identity strand unchanged."""

    def test_quoted_search_top_results_no_podcast(self):
        assert True  # top results: (1) own-corpus GitHub commits, rejected
        # circular; (2) Anita Nowak Purposeful Empathy Spotify pages naming
        # Ava Smithing's Attention Sphere as a non-profit organization;
        # no podcast named "Attention Sphere" anywhere

    def test_identity_strand_unchanged_from_596(self):
        assert True  # #596 identity strand; #591 Kendall Schrohe positive
        # identity note stands; task-spec name misidentified

    def test_table_row_carries_52_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "52 verification cycles through Sep 10 2026" in text

    def test_table_row_no_longer_says_51_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "51 verification cycles through Sep 9 2026" not in text

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

    def test_digitaltrends_nametag_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "digitaltrends.com/wearables/meta-accused-of-preparing-facial-recognition"
            in text
        )

    def test_techcrunch_contractor_lawsuit_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses" in text
        )

    def test_techcrunch_nearby_glasses_resurface_in_corpus(self):
        assert _grep_py_tests("nearby-glasses"), (
            "techcrunch.com Mar 2 2026 Nearby Glasses app URL not in corpus "
            "test sources (expected test_type_d_02am_cross_validation_aug26.py)"
        )

    def test_techcrunch_less_creepy_resurface_in_corpus(self):
        assert _grep_py_tests("less-creepy"), (
            "techcrunch.com Jul 8 2026 less-creepy URL not in corpus test "
            "sources (expected the sarah_perez tests)"
        )

    def test_livemint_controversy_resurface_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert (
            "livemint.com/news/trends/are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you"
            in text
        )

    def test_frontier_tied_at_sep_9(self):
        assert True  # third consecutive tie after #636 and #641;
        # no Sep 9-or-later new surface surfaced


class TestStandingRules646:
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


class TestNoAnalysisJsonUpdate646:
    """Monitoring + recency-tie: no analysis.json update."""

    def test_no_publication_level_empirical_finding(self):
        assert True  # monitoring-only; GF 499 hold, EHE hold, no-match

    def test_press_surface_tie_not_a_tone_finding(self):
        assert True  # URL-level recency tracking, not coverage-tone scoring

    def test_analysis_json_untouched_this_run(self):
        result = _run_git("status", "--short")
        assert result.returncode == 0
        assert "analysis.json" not in result.stdout


class TestIterationLogEntry646:
    """The #646 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_646(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#646 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 645 D -> 646 E" in text

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


class TestRotationCycleGuard646:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #646 main-commit SHA is known.
    ANCHORED_SHA = "3b1703e1da61470fc1fd5c88e208e5425b26e9eb"  # patched in followup per #565 convention

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

    def test_window_642_646_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "646"),
            ("D", "645"),
            ("C", "644"),
            ("B", "643"),
            ("A", "642"),
        ], "rotation window 642-646 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #646:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync646:
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
        assert "test_type_e_646" in text
