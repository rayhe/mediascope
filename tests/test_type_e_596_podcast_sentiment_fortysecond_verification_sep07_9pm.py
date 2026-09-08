"""
Type E #596 - Podcast Sentiment Tracking: Forty-Second Verification Cycle Sep 7 21:00 PDT
Guilty Feminist 498 Hold No 499 (Listen Notes 1d crawl latest 498 "Politics"
recorded 20 Aug 2026 released 31 Aug, Chortle 6h crawl Sep 13 Kings Place LPF
no new episode announced, weekly cadence 499 penciled for Sep 7 may index
later, no 499 by 21:00 PDT / 04:00 UK Sep 8, 498-latest rests on #576
verification, weaker evidence tier disclosed, secondary-only; NEW-TO-CORPUS
beyondthejoke.co.uk DFW Channel 4 "Next Week's News" non-TX pilot host-news,
zero pre-commit hits, not an episode; live.org.uk Sep 13 re-surface in
corpus; podfollow/artscentremelbourne/marieclaire excluded) +
EHE 29-Day Hold (re-surfaces only, all in corpus: feminist.org FMF piece via
#470 listed updated 7d crawled under 1h, thedrum.com Mark Palmer via #460
listed updated 25d crawled 4h, latestly.com Jul 30 fact-check in corpus, Times
spoof-Epstein in corpus, engadget bus stops in corpus; androidcentral Feb 2026
glassholes retrospective excluded as non-EHE lineage, no double-counting, no
new primary motif, no competitor-equivalent in forty-two cycles) +
Attention Sphere 42nd No-Match AS PODCAST (quoted search returns own-corpus
GitHub commits, rejected circular) plus TWO identity-strand extensions:
breakingnewstoday.eu mirror of the Schrohe story (zero "breakingnewstoday"
pre-commit hits, new outlet same story, Kendall Schrohe ED / DC-NYC
affiliation / anti-surveillance quote, snippet-bounded) and raleighnewstoday
"Meta Smart Glasses Privacy Failures Analysis" new page (zero "privacy
failures analysis" pre-commit hits, NEW Attention Sphere statement naming
STOP with shutter-sound / hardware-switch / privacy-impact-assessment asks,
snippet-bounded; outlet in corpus via #591; task-spec still misidentified as
podcast) +
startupfortune/MediaNama-IFF/MediaNama-Jul23/webpronews/letsdatascience/
Reuters-HateAid/androidpolice/livemint/singulism/engadget explicitly
distinguished as in-corpus lineage; NEITHER surface advances the #581 Times
recency frontier +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, distinct from 591, forty-second verification cycle, extends #591 by
5 hours, not duplicate, iteration-log entry present and newest-first.
"""
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
README = REPO_ROOT / "README.md"
ARCH = REPO_ROOT / "docs" / "ARCHITECTURE.md"
TESTS_DIR = REPO_ROOT / "tests"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 596
DATE_STR = "2026-09-07 21:00 PDT"
TEST_FILE = Path(__file__).name

FILE_592 = "test_type_a_592_verge_google_adversarial_litigation_boundary_replication_sep07_5pm.py"
FILE_593 = "test_type_b_593_mark_gurman_access_journalism_register_asymmetry_sep07_6pm.py"
FILE_594 = "test_type_c_594_news_corp_five_leg_ai_revenue_architecture_sep07_7pm.py"
FILE_595 = "test_type_d_595_scorer_consistency_592_593_divergence_degenerate_rotation_doc_sync_sep07_8pm.py"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_596_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #596", text, re.MULTILINE)
    assert m, "Iteration #596 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_596_block()
        assert "596" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_596_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_596_block()
        lower = block.lower()
        assert "590 d -> 591 e" not in lower  # previous cycle's rotation, not this one
        assert "595 d -> 596 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_fortysecond_cycle_label(self):
        block = get_596_block()
        lower = block.lower()
        assert "forty-second" in lower

    def test_distinct_from_591(self):
        block = get_596_block()
        lower = block.lower()
        assert "forty-first" not in lower
        assert "extends #591 by 5 hours" in block


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_596_block()
        assert "498" in block
        assert "Politics with Felicity Ward and Hannah Spencer" in block

    def test_listen_notes_1d_crawl(self):
        block = get_596_block()
        assert "Listen Notes" in block
        assert "crawled 1 day" in block
        assert "Recorded 20 August 2026 at Gilded Balloon at the Museum" in block

    def test_no_499_bounded(self):
        block = get_596_block()
        lower = block.lower()
        assert "no 499" in lower
        assert "21:00 PDT" in block
        assert "04:00 UK" in block
        assert "bounded search-result absence" in lower

    def test_cadence_note_and_deadline(self):
        block = get_596_block()
        lower = block.lower()
        assert "weekly cadence" in lower
        assert "499 was penciled for" in lower
        assert "may index later" in lower

    def test_secondary_only_disclosed(self):
        block = get_596_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_weaker_evidence_tier_disclosed(self):
        block = get_596_block()
        lower = block.lower()
        assert "weaker evidence tier" in lower
        assert "disclosed" in lower

    def test_chortle_6h_crawl(self):
        block = get_596_block()
        assert "Chortle" in block
        assert "crawled 6 hours" in block
        assert "13 Kings Place" in block

    def test_576_verification_basis(self):
        block = get_596_block()
        assert "#576" in block
        assert "Audible UK verification" in block

    def test_beyondthejoke_new_host_news(self):
        block = get_596_block()
        assert "beyondthejoke.co.uk" in block
        assert "Next Week's News" in block
        assert "Syeda Irtizaali" in block
        assert "Sharon Horgan and Clelia Mountford" in block
        lower = block.lower()
        assert 'zero pre-commit "beyondthejoke" hits' in lower
        assert "not a gf episode" in lower

    def test_live_org_resurface_in_corpus(self):
        block = get_596_block()
        assert "live.org.uk" in block
        assert "in corpus via #358" in block.lower()

    def test_non_episode_items_excluded(self):
        block = get_596_block()
        lower = block.lower()
        assert "podfollow" in lower
        assert "excluded" in lower

class TestEHEHold:
    def test_29_day_hold(self):
        block = get_596_block()
        assert "29-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_596_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_feminist_org_resurface_in_corpus(self):
        block = get_596_block()
        assert "feminist.org" in block
        assert "in corpus via #470" in block.lower()
        assert "listed updated 7 days" in block

    def test_thedrum_resurface_in_corpus(self):
        block = get_596_block()
        assert "thedrum.com" in block
        assert "in corpus via #460" in block.lower()
        assert "crawled 4 hours" in block

    def test_latestly_and_times_resurface_in_corpus(self):
        block = get_596_block()
        lower = block.lower()
        assert "latestly.com jul 30 fact-check" in lower
        assert "in corpus" in lower
        assert "times spoof-epstein" in lower

    def test_androidcentral_excluded_non_ehe_lineage(self):
        block = get_596_block()
        lower = block.lower()
        assert "androidcentral" in lower
        assert "non-ehe lineage" in lower

    def test_no_new_primary_motif(self):
        block = get_596_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower
        assert "re-surfaces only" in lower

    def test_no_competitor_equivalent_42_cycles(self):
        block = get_596_block()
        lower = block.lower()
        assert "forty-two verification cycles" in lower
        assert "no competitor-equivalent" in lower

    def test_no_double_counting(self):
        block = get_596_block()
        lower = block.lower()
        assert "no double-counting" in lower


class TestAttentionSphereIdentity:
    def test_42nd_no_match_as_podcast(self):
        block = get_596_block()
        lower = block.lower()
        assert "forty-second no-match" in lower
        assert "quoted search" in lower

    def test_circular_github_rejected(self):
        block = get_596_block()
        lower = block.lower()
        assert "own-corpus github commits" in lower
        assert "rejected as circular" in lower

    def test_breakingnewstoday_new_outlet(self):
        block = get_596_block()
        assert "breakingnewstoday.eu" in block
        lower = block.lower()
        assert 'zero pre-commit "breakingnewstoday" hits' in lower
        assert "new outlet, not a new story" in lower or "new outlet for the identity strand" in lower
        assert "Kendall Schrohe" in block
        assert "executive director of the Attention Sphere" in block
        assert "anti-Meta glasses ads in DC and New York City" in block

    def test_schrohe_quote_bounded(self):
        block = get_596_block()
        assert "There's not much Meta can do to convince me" in block
        assert "snippet-bounded" in block.lower()

    def test_privacy_failures_analysis_new_page(self):
        block = get_596_block()
        assert "Meta Smart Glasses Privacy Failures Analysis" in block
        lower = block.lower()
        assert 'zero pre-commit "privacy failures analysis" hits' in lower
        assert "outlet is in corpus via #591" in lower
        assert "the page and the statement are new" in lower

    def test_new_anti_surveillance_statement(self):
        block = get_596_block()
        assert "We are not anti-technology; we are anti-surveillance." in block
        assert "they are selling a weapon of harassment" in block
        assert "Surveillance Technology Oversight Project" in block
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_task_spec_still_misidentified_as_podcast(self):
        block = get_596_block()
        lower = block.lower()
        assert "task-spec name remains misidentified as a podcast" in lower
        assert "still no podcast" in lower


class TestNewSurfaces:
    def test_three_new_surfaces(self):
        block = get_596_block()
        lower = block.lower()
        assert "three new surfaces" in lower or "tWO identity-strand extensions + one host-news surface" in lower.replace("two", "tWO")

    def test_breakingnewstoday_recency_bound(self):
        block = get_596_block()
        assert "listed updated 42d, crawled 22d" in block

    def test_recency_frontier_holds(self):
        block = get_596_block()
        assert "#581 Times recency frontier" in block
        assert "does not advance" in block
        assert "newest-in-corpus surface" in block

    def test_snippet_bounded(self):
        block = get_596_block()
        lower = block.lower()
        assert lower.count("snippet-bounded") >= 3

    def test_in_corpus_lineage_distinguished(self):
        block = get_596_block()
        lower = block.lower()
        assert "startupfortune" in lower
        assert "medianama" in lower
        assert "webpronews" in lower
        assert "letsdatascience" in lower
        assert "reuters hateaid" in lower
        assert "in corpus" in lower
        assert "not new" in lower


class TestScoresAndDiscipline:
    def test_no_significance_claims(self):
        block = get_596_block()
        assert "p_value NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "no claim of empirical significance" in block.lower()

    def test_ehe_illustrative_score(self):
        block = get_596_block()
        assert "MANUAL ILLUSTRATIVE -8/10" in block

    def test_correlation_not_causation(self):
        block = get_596_block()
        assert "Correlation not causation" in block

    def test_no_em_dashes_in_block(self):
        block = get_596_block()
        assert "\u2014" not in block

    def test_no_em_dashes_in_test_file(self):
        text = Path(__file__).read_text(encoding="utf-8")
        assert "\u2014" not in text


class TestSources:
    def test_listen_notes_verbatim(self):
        block = get_596_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block

    def test_chortle_verbatim(self):
        block = get_596_block()
        assert "https://www.chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist" in block

    def test_beyondthejoke_verbatim(self):
        block = get_596_block()
        assert "https://www.beyondthejoke.co.uk/content/5690/tv-deborah-frances-white" in block

    def test_breakingnewstoday_verbatim(self):
        block = get_596_block()
        assert "https://breakingnewstoday.eu/tech/meta-is-royally-screwing-up-its-smart-glasses-rollout/" in block

    def test_feminist_org_verbatim(self):
        block = get_596_block()
        assert "https://feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/" in block

    def test_thedrum_verbatim(self):
        block = get_596_block()
        assert "https://www.thedrum.com/opinion/mark-palmer-is-the-glasses-partnership-with-meta-making-ray-ban-lose-its-cool" in block

    def test_latestly_verbatim(self):
        block = get_596_block()
        assert "https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html" in block

    def test_test_file_section(self):
        text = read_doc()
        assert TEST_FILE in text

class TestConfoundersAndLog:
    def test_five_strong_confounders(self):
        block = get_596_block()
        assert block.count("STRONG") >= 5

    def test_five_hour_cadence_bound(self):
        block = get_596_block()
        lower = block.lower()
        assert "five-hour cadence" in lower
        assert "21:00 PDT Sep 7" in block

    def test_mirror_counts_as_outlet_not_story(self):
        block = get_596_block()
        lower = block.lower()
        assert "mirror" in lower
        assert "new outlet, not a new story" in lower or "same story" in lower

    def test_log_entry_present_newest_first_anchored(self):
        # Anchored at the #595 main commit (8fed112): this verifies the
        # #596 run's predecessor state AT THAT TIME. Later iterations
        # (#597+) prepend their own entries, so the live newest-first
        # assertion is a time-bombshell; the anchored form is immutable
        # (rotation-guard anchor convention, Type D #565 followup).
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Iteration #596" in log or "#596 Type E" in log
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "show", "8fed112:iteration-log.md"],
            capture_output=True, text=True, check=True)
        anchored = out.stdout
        assert re.search(r"^#595 Type D", anchored, re.MULTILINE), \
            "no #595 Type D entry in iteration-log.md at 8fed112"
        first_entry = re.search(r"^#\d+", anchored, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#595", \
            "iteration-log.md was not newest-first at #595 at 8fed112"

    def test_rotation_transparency(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "595 D -> 596 E" in log

    def test_log_rotation_transparency_mentions_previous_commit(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "8fed112" in log

    def test_log_novelty_verification(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Novelty Verification" in log
        assert "forty-second cycle is new" in log.lower()


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 592-595 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep596:
    WINDOW_596 = [FILE_592, FILE_593, FILE_594, FILE_595]

    @pytest.mark.parametrize("fname", WINDOW_596)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 592-596 window, closing the D->E edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carries the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard596:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type E #596 followup: ...") and doc-sync commits interleave
    # between mains since the #572/#573/#574 convention change; the naive
    # newest-5 filter broke on them. The colon immediately after the
    # iteration number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard596.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard596.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#596", "E"),
            ("#595", "D"),
            ("#594", "C"),
            ("#593", "B"),
            ("#592", "A"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # D->E is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: E,D,C,B,A (the
        # rotation runs backward in newest-first order). (order[a] -
        # order[b]) % 5 == 1 steps one position backward from the newer
        # commit a to the older commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_main_subjects()
        nums = [re.search(r"#(\d+):", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, f"duplicate iteration in window: {nums}"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: README.md test table and docs/ARCHITECTURE.md test tree
# must carry rows for #592-#596 with authoritative def-test counts. The
# #592/#593/#594/#595 rows were synced by their own runs (with the #592
# README row added by #593 and the #594 row repaired by #595). The #591 row
# must not decay. count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_596 = [
    # (iteration, test file, expected def-test count, keyword)
    ("592", FILE_592, 41, "Type A #592"),
    ("593", FILE_593, 29, "Type B #593"),
    ("594", FILE_594, 46, "Type C #594"),
    ("595", FILE_595, 51, "Type D #595"),
]


class TestDocSyncRatchet596:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_596)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_596)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCH.read_text(encoding="utf-8")
        assert fname in text, f"ARCHITECTURE missing row for {fname}"
        assert kw in text, f"ARCHITECTURE missing {kw} keyword"

    def test_596_own_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert TEST_FILE in text, "README missing own #596 row"

    def test_596_own_architecture_row_present(self):
        text = ARCH.read_text(encoding="utf-8")
        assert TEST_FILE in text, "ARCHITECTURE missing own #596 row"

    def test_591_row_survives(self):
        text = README.read_text(encoding="utf-8")
        assert "test_type_e_591_podcast_sentiment_fortyfirst_verification_sep07_4pm.py" in text
        arch = ARCH.read_text(encoding="utf-8")
        assert "test_type_e_591_podcast_sentiment_fortyfirst_verification_sep07_4pm.py" in arch
