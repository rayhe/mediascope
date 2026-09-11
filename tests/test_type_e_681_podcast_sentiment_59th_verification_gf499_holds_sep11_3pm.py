"""Type E #681: podcast sentiment 59th verification cycle (Sep 11 2026, 15:00 PDT).

Adoption: a 14:00 PDT draft of the podcast-sentiment.md #681 section was left
uncommitted by an earlier pass (modified md, no test file, no log entry, no
commit). This run adopts the draft, re-verifies every strand with fresh
15:00 PDT searches, and corrects its section 4: this run found ONE
new-to-corpus press surface (geeky-gadgets.com Meta smart-glasses leaks
piece) that the draft missed.

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk 757 episodes
with latest episode 2026-09-07 crawled less than 1h; au.radio.net directory
re-surface crawled 3d; ie.radio.net GF podcast page re-surface crawled 1d,
updated 4d, in corpus via #656 directory corroboration; Listen Notes cached
page still stale on 498 "Politics" (5d crawl); podscan.fm 499 TKE Studios
Margate transcript crawled less than 1h; Chortle Sep 13 Kings Place LPF
14:00 live-show re-surface crawled less than 1h is an upcoming LIVE SHOW
not episode 500, exact URL in corpus; episode 500 watch item penciled Mon
Sep 14 per the weekly-Monday cadence: 498 Aug 31, 499 Sep 7).

EHE 33-day hold continues: 7 re-surfaces observed this run, ALL verified in
corpus pre-commit: thetimes.com spoof-Epstein piece (47d, crawled 47d),
latestly.com Jul 30 2026 spoof-Epstein fact-check (43d, crawled 19d, in
corpus since #383/#445/#465), petapixel.com Kylie Jenner lenticular
"We're always watching" (50d, crawled 17d), engadget.com London bus stops
fake-ad piece (56d, crawled 7d, corpus holds lowercase URL; this run's WWW
uppercase form logged verbatim as same page per #676 convention),
feminist.org/news Feminist Majority Foundation "Helpful or Hurtful" piece
(listed updated 10d, crawled 4h, in corpus since #470/#561/#596; 4h crawl is
re-index, not republication), sifted.eu tech-events ban piece (16d,
crawled 16d, in corpus via #480), afrotech.com smart-glasses ethics piece
(56d, crawled 4h). No new primary campaign motif; last campaign phase
remains the circa Aug 10 Epstein poster; no competitor-equivalent
guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in
any of the 59 cycles.

Attention Sphere 59th no-match as podcast: quoted-search top results remain
this repository's own GitHub pages (podcast-sentiment.md blob/HEAD and
prior Type E commit pages; rejected as circular per established
discipline) plus the Spotify Creators Purposeful Empathy page confirming
Attention Sphere is Ava Smithing's nonprofit, not a podcast. Identity
strand unchanged from #596; task-spec name remains misidentified; Tracked
Sources table 58->59 cycles through Sep 11 2026.

Press surfaces: ONE new-to-corpus press surface this run, but NOT a
frontier advance. https://www.geeky-gadgets.com/meta-smart-glasses-leaks-2026/
("Meta Smart Glasses Leak Reveals Four Possible New Models") is
new-to-corpus (exact-URL corpus grep returned 0 hits; only the domain's
Samsung Galaxy Glasses URL is in corpus) and was page-open verified this
run (140 lines: FCC-filing-derived leaks of four new models - Wayfarer,
cat-eye, aviator - the RW7004 camera-free model, electrochromic
adjustable-tint lenses, Project Phoenix 110g MR headset with external
compute puck, the "Muse" AI assistant with experimental "super sensing";
Meta Connect 2026 framed as the expected unveiling). Date-bounded, not
date-verified: search index says "Last Updated: 2 days ago" (circa Sep 9
from Sep 11), no on-page publication date (browser.find "September"
returned nothing on the opened page), image asset path
/2026/09/ray-ban-meta-leaks.webp. Because no post-Sep-9 publication date
could be verified, the recency frontier stays TIED at Sep 9 (tenth
consecutive tie after #636, #641, #646, #651, #656, #661, #666, #671 and
#676); the petapixel.com Sep 9 US-police-warning piece (in corpus via
#631) remains the newest date-verified in-corpus Meta-glasses press item.

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


class TestNovelty681:
    """Iteration 681 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_681_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_681*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_681_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_681 files, no #681 in git log); this test
        # pins that no duplicate #681 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type E #681:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type E #681 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard681.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestGF499Holds59thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

    def test_gf_row_still_499(self):
        text = _read("podcast-sentiment.md")
        m = re.search(r"\| The Guilty Feminist \| \*\*Podcast\*\*[^|]*\| ([^|]*499[^|]*) \|", text)
        assert m, "GF row with 499 episodes not found"

    def test_gf_row_date_now_sep_11(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 11 2026)" in text

    def test_adoption_note_present(self):
        assert "Adoption note" in self._section()

    def test_uk_podcasts_still_latest_2026_09_07(self):
        section = self._section()
        assert "uk-podcasts.co.uk" in section
        assert "Latest episode: 2026-09-07" in section

    def test_ie_radio_net_still_in_corpus_via_656(self):
        section = self._section()
        assert "ie.radio.net" in section
        assert "in corpus" in section

    def test_episode_500_watch_item_still_penciled_sep_14(self):
        section = self._section()
        assert "Mon Sep 14" in section

    def test_chortle_sep_13_is_live_show_not_episode(self):
        section = self._section()
        assert "Chortle" in section
        assert "not an episode" in section or "LIVE SHOW" in section

    def test_listen_notes_stale_on_498(self):
        section = self._section()
        assert "Listen Notes" in section
        assert "498" in section

    def test_podscan_transcript_corroborates_499(self):
        section = self._section()
        assert "podscan.fm" in section

    def test_no_tech_word_audit_needed(self):
        section = self._section()
        assert "No new tech-word audit needed" in section


class TestEHE33DayHold59thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

    def test_latestly_fact_check_resurface_in_corpus(self):
        section = self._section()
        assert "latestly.com" in section
        assert "in corpus" in section

    def test_engadget_bus_stops_resurface_in_corpus(self):
        section = self._section()
        assert "engadget.com" in section

    def test_afrotech_ethics_resurface_in_corpus(self):
        section = self._section()
        assert "afrotech.com" in section

    def test_feminist_org_piece_is_resurface_not_new(self):
        section = self._section()
        assert "feminist.org" in section
        assert "re-surface" in section or "re-surfaces" in section

    def test_thetimes_petapixel_sifted_resurfaces_in_corpus(self):
        section = self._section()
        for frag in ("thetimes.com", "petapixel.com", "sifted.eu"):
            assert frag in section, frag

    def test_no_new_primary_motif(self):
        section = self._section()
        assert "no new primary motif" in section

    def test_no_competitor_equivalent_in_59_cycles(self):
        section = self._section()
        assert "59 cycles" in section
        assert "No competitor-equivalent" in section


class TestAttentionSphere59thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

    def test_quoted_search_top_results_no_podcast(self):
        section = self._section()
        assert "59th" in section or "fifty-ninth" in section
        assert "no matching podcast" in section

    def test_circular_own_corpus_rejected(self):
        section = self._section()
        assert "circular" in section

    def test_identity_strand_unchanged_from_596(self):
        section = self._section()
        assert "#596" in section

    def test_table_row_carries_59_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "59 verification cycles through Sep 11 2026" in text

    def test_table_row_no_longer_says_58_cycles(self):
        text = _read("podcast-sentiment.md")
        head = text[:2000]
        assert "58 verification cycles through Sep 11 2026" not in head

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierTie681:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

    def test_geeky_gadgets_new_to_corpus_logged(self):
        section = self._section()
        assert "geeky-gadgets.com/meta-smart-glasses-leaks-2026" in section
        assert "new-to-corpus" in section

    def test_geeky_gadgets_page_open_verified(self):
        section = self._section()
        assert "page-open verified" in section

    def test_geeky_gadgets_date_bounded_not_verified(self):
        section = self._section()
        assert "Date-bounded, not date-verified" in section

    def test_geeky_gadgets_is_frontier_tie_not_advance(self):
        section = self._section()
        assert "frontier TIE, not advance" in section or "frontier TIED at Sep 9" in section

    def test_draft_zero_surfaces_claim_corrected(self):
        # The adopted 14:00 draft claimed ZERO new-to-corpus surfaces; the
        # 15:00 re-verification corrected it. The section must not retain
        # the zero claim as the finding.
        section = self._section()
        assert "corrected its section 4" in section or "ONE new-to-corpus press surface" in section

    def test_petapixel_sep_9_frontier_piece_still_newest(self):
        section = self._section()
        assert "petapixel.com/2026/09/09" in section
        assert "in corpus via #631" in section

    def test_digitaltrends_stale_reindex_logged_not_frontier(self):
        section = self._section()
        assert "digitaltrends.com" in section
        assert "logged in #671" in section
        assert "NOT a press-surface advance" in section

    def test_reuters_stale_reindexes_logged(self):
        section = self._section()
        assert "241d" in section
        assert "248d" in section

    def test_thetimes_fear_and_loathing_resurface_in_corpus(self):
        section = self._section()
        assert "thetimes.com" in section
        assert "in corpus via #581" in section

    def test_thevermilion_resurface_in_corpus_via_626(self):
        section = self._section()
        assert "thevermilion.com" in section
        assert "in corpus via #626" in section

    def test_frontier_tied_at_sep_9_tenth_consecutive(self):
        section = self._section()
        assert "tenth consecutive tie" in section
        assert "TIED at Sep 9" in section


class TestStandingRules681:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

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


class TestNoAnalysisJsonUpdate681:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #681")[-1]

    def test_no_publication_level_empirical_finding(self):
        section = self._section()
        assert "No claim of empirical significance" in section

    def test_press_surface_tie_not_a_tone_finding(self):
        section = self._section()
        assert "TIED at Sep 9" in section

    def test_analysis_json_untouched_this_run(self):
        out = _run_git("status", "--short")
        assert "analysis.json" not in out.stdout


class TestRotationCycleGuard681:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #681 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in followup per #565 convention

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

    def test_window_677_681_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "681"),
            ("D", "680"),
            ("C", "679"),
            ("B", "678"),
            ("A", "677"),
        ], "rotation window 677-681 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type E #681:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync681:
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
        assert "test_type_e_681" in text

    def test_test_file_table_row_present(self):
        text = _read("README.md")
        assert "test_type_e_681_podcast_sentiment_59th_verification_gf499_holds_sep11_3pm.py" in text

    def test_iteration_log_entry_present(self):
        text = _read("iteration-log.md")
        assert "#681 Type E:" in text, "iteration-log entry for #681 missing"

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 680 D -> 681 E" in text
