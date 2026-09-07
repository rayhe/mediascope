"""
Type E #591 - Podcast Sentiment Tracking: Forty-First Verification Cycle Sep 7 16:00 PDT
Guilty Feminist 498 Hold No 499 (Listen Notes 1d crawl latest 498 "Politics"
recorded 20 Aug 2026 released 31 Aug, Audible UK 5d crawl still lists 498
latest "Politics with Felicity Ward and Hannah Spencer", Chortle 1h crawl
Sep 13 Kings Place LPF no new episode announced, guiltyfeminist.com 7h crawl
no episode number, weekly cadence 499 penciled for Sep 7 may index later,
no 499 by 16:00 PDT / 23:00 UK, 498-latest rests on #576 verification,
weaker evidence tier disclosed, secondary-only) +
EHE 28-Day Hold (singulism Jul 17 re-surface crawled 2d in corpus,
androidcentral Feb 2026 glassholes retrospective excluded as non-EHE
lineage, GitHub commits 584f331bde53b2f9eafbfed1bbd138546ea8820a and
0e7bfc0e7d3ee11edbe087d2328e04df32cb03d7 rejected as circular, no
double-counting, no new primary motif, no competitor-equivalent in
forty-one cycles) +
Attention Sphere 41st No-Match AS PODCAST plus FIRST POSITIVE IDENTITY:
raleighnewstoday.com names Kendall Schrohe executive director of the
Attention Sphere, "one of the advocacy groups affiliated with the
anti-Meta glasses ads in DC and New York City"; schrohe /
raleighnewstoday / attention-sphere zero pre-commit corpus hits,
new-to-corpus entity + outlet, task-spec misidentified as podcast
stands +
TWO new press surfaces (medianama.com "IFF notice says Meta liable for
Ray-Ban glasses recording" 2026-08-223-iff, zero "khan market" pre-commit
hits, IFF Khan Market bystander-recording legal notice, platform-vs-
manufacturer Section 79 IT Act argument, first Indian liability attempt,
distinct from in-corpus Economic Times Delhi-man Rs 2.05 crore notice via
#581, snippet-bounded; webpronews.com "Sam Altman Rejects Smart Glasses
as Uncomfortable", slug zero hits, Sweet Pea voice-first wearable,
Altman rejects glasses form factor "baggage" (weight, heat, recording
awareness), Zuckerberg "hard to imagine" divergence, distinct outlet/
angle, snippet-bounded; NEITHER advances the #581 Times recency
frontier) +
Times/StartupFortune/letsdatascience/Reuters-HateAid/AndroidPolice/
livemint/androidcentral explicitly distinguished as in-corpus lineage +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs
incl guiltyfeminist.com/?ref=quillette.com and medianama 223-iff and
webpronews slug and raleighnewstoday as surfaced, distinct from 586,
forty-first verification cycle, extends #586 by 5 hours, not duplicate,
iteration-log entry present and newest-first.
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
ITERATION = 591
DATE_STR = "2026-09-07 16:00 PDT"
TEST_FILE = Path(__file__).name

FILE_587 = "test_type_a_587_gizmodo_apple_null_tie_fourth_control_product_lane_boundary_sep07_12pm.py"
FILE_588 = "test_type_b_588_scott_stein_handson_review_register_constancy_sep07_1pm.py"
FILE_589 = "test_type_c_589_ziff_davis_openai_lawsuit_adversarial_sep07_2pm.py"
FILE_590 = "test_type_d_590_scorer_consistency_587_588_agreement_degenerate_boundary_rotation_doc_sync_sep07_3pm.py"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_591_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #591", text, re.MULTILINE)
    assert m, "Iteration #591 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_591_block()
        assert "591" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_591_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_591_block()
        lower = block.lower()
        assert "585 d -> 586 e" not in lower  # previous cycle's rotation, not this one
        assert "590 d -> 591 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_fortyfirst_cycle_label(self):
        block = get_591_block()
        lower = block.lower()
        assert "forty-first" in lower

    def test_distinct_from_586(self):
        block = get_591_block()
        lower = block.lower()
        assert "fortieth" not in lower
        assert "extends #586 by 5 hours" in block


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_591_block()
        assert "498" in block
        assert "Politics" in block

    def test_listen_notes_1d_crawl(self):
        block = get_591_block()
        assert "Listen Notes" in block
        assert "crawled 1 day" in block
        assert "Released 31 August" in block
        assert "Gilded Balloon at the Museum" in block

    def test_no_499_bounded(self):
        block = get_591_block()
        lower = block.lower()
        assert "no episode 499" in lower
        assert "bounded" in lower

    def test_cadence_note_and_deadline(self):
        block = get_591_block()
        assert "16:00 PDT" in block
        assert "23:00 UK" in block
        lower = block.lower()
        assert "weekly" in lower
        assert "may index later" in lower

    def test_secondary_only_disclosed(self):
        block = get_591_block()
        assert "secondary-only" in block.lower()
        assert "Stated explicitly" in block

    def test_weaker_evidence_tier_disclosed(self):
        block = get_591_block()
        lower = block.lower()
        assert "weaker evidence tier" in lower

    def test_chortle_1h_crawl(self):
        block = get_591_block()
        assert "Chortle" in block
        assert "crawled 1 hour" in block
        assert "Sep 13" in block
        assert "Kings Place" in block

    def test_audible_uk_5d_crawl(self):
        block = get_591_block()
        assert "Audible UK" in block
        assert "5 days" in block
        assert "Felicity Ward" in block

    def test_576_verification_basis(self):
        block = get_591_block()
        lower = block.lower()
        assert "rests on #576" in lower


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_591_block()
        assert "28-Day Hold" in block

    def test_activist_not_podcast(self):
        block = get_591_block()
        assert "activist group, not a podcast" in block

    def test_singulism_resurface_in_corpus(self):
        block = get_591_block()
        assert "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/" in block
        assert "crawled 2 days" in block
        assert "in corpus" in block

    def test_androidcentral_excluded_non_ehe_lineage(self):
        block = get_591_block()
        assert "androidcentral.com/wearables/everyone-hates-glassholes-and-now-even-the-us-air-force-is-in-agreement" in block
        lower = block.lower()
        assert "non-ehe lineage" in lower or "not ehe" in lower

    def test_github_circular_commits_rejected(self):
        block = get_591_block()
        lower = block.lower()
        assert "circular" in lower
        assert "rejected" in lower
        assert "github.com/rayhe/mediascope/commit/584f331bde53b2f9eafbfed1bbd138546ea8820a" in block
        assert "github.com/rayhe/mediascope/commit/0e7bfc0e7d3ee11edbe087d2328e04df32cb03d7" in block

    def test_no_new_primary_motif(self):
        block = get_591_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent_41_cycles(self):
        block = get_591_block()
        lower = block.lower()
        assert "no competitor-equivalent guerrilla campaign" in lower
        assert "forty-one verification cycles" in lower

    def test_no_double_counting(self):
        block = get_591_block()
        assert "No double-counting" in block


class TestAttentionSphereIdentity:
    def test_41st_no_match_as_podcast(self):
        block = get_591_block()
        lower = block.lower()
        assert "forty-first no-match" in lower
        assert "podcast" in lower

    def test_first_positive_identity(self):
        block = get_591_block()
        lower = block.lower()
        assert "first positive identity" in lower

    def test_raleighnewstoday_url_verbatim(self):
        block = get_591_block()
        assert "https://raleighnewstoday.com/meta-is-royally-screwing-up-its-smart-glasses-rollout" in block

    def test_kendall_schrohe_named(self):
        block = get_591_block()
        assert "Kendall Schrohe" in block
        assert "executive director" in block

    def test_dc_nyc_affiliation(self):
        block = get_591_block()
        lower = block.lower()
        assert "dc and new york city" in lower
        assert "one of the advocacy groups" in lower

    def test_schrohe_quote_bounded(self):
        block = get_591_block()
        assert "surveillance technology" in block.lower()
        assert "no amount of tweaking" in block.lower()

    def test_zero_precommit_hits_disclosed(self):
        block = get_591_block()
        lower = block.lower()
        assert "zero pre-commit corpus hits" in lower
        assert "new-to-corpus entity" in lower
        assert "new-to-corpus outlet" in lower

    def test_task_spec_still_misidentified_as_podcast(self):
        block = get_591_block()
        assert "misidentified" in block.lower()
        lower = block.lower()
        assert "as a podcast" in lower


class TestNewPressSurfaces:
    def test_medianama_url_verbatim(self):
        block = get_591_block()
        assert "https://www.medianama.com/2026/08/223-iff-meta-ray-ban-glasses/" in block

    def test_khan_market_zero_corpus_hits(self):
        block = get_591_block()
        lower = block.lower()
        assert "khan market" in lower
        assert "zero" in lower

    def test_iff_notice_details(self):
        block = get_591_block()
        assert "Internet Freedom Foundation" in block
        assert "Section 79" in block
        assert "platform" in block.lower()
        assert "manufacturer" in block.lower()

    def test_iff_first_indian_attempt(self):
        block = get_591_block()
        lower = block.lower()
        assert "first indian" in lower

    def test_iff_distinct_from_economic_times_delhi_man(self):
        block = get_591_block()
        assert "Rs 2.05 crore" in block
        assert "different plaintiff" in block.lower()

    def test_webpronews_url_verbatim(self):
        block = get_591_block()
        assert "https://www.webpronews.com/sam-altman-rejects-smart-glasses-as-uncomfortable-what-it-means-for-the-rush-to-put-ai-on-your-face/" in block

    def test_webpronews_domain_in_corpus_slug_new(self):
        block = get_591_block()
        lower = block.lower()
        assert "domain in corpus" in lower
        assert "slug" in lower

    def test_sweet_pea_details(self):
        block = get_591_block()
        assert "Sweet Pea" in block
        assert "voice-focused" in block.lower()
        assert "Jony Ive" in block

    def test_altman_rejection_details(self):
        block = get_591_block()
        lower = block.lower()
        assert "baggage" in lower
        assert "recording awareness" in lower

    def test_neither_advances_recency_frontier(self):
        block = get_591_block()
        lower = block.lower()
        assert "does not advance" in lower
        assert "recency frontier" in lower
        assert "times" in lower

    def test_snippet_bounded(self):
        block = get_591_block()
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_in_corpus_lineage_distinguished(self):
        block = get_591_block()
        for marker in ("via #581", "via #576", "via #586"):
            assert marker in block, f"missing in-corpus marker {marker}"
        assert "NOT new" in block


class TestScoresAndDiscipline:
    def test_no_significance_claims(self):
        block = get_591_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_591_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "-8/10" in block

    def test_correlation_not_causation(self):
        block = get_591_block()
        assert "Correlation not causation" in block

    def test_no_em_dashes_in_block(self):
        block = get_591_block()
        # Matches the #586/#581 convention (source-level escaped literal, which
        # is the six-character text "\u2014"), plus a real-character check via
        # chr(0x2014) that embeds no em dash in this source file.
        assert "\\u2014" not in block, "escape-sequence found in block"
        assert chr(0x2014) not in block, "em dash found in block"

    def test_no_em_dashes_in_test_file(self):
        src = Path(__file__).read_text(encoding="utf-8")
        # The escaped assertion literal above is not a real em dash; count
        # real occurrences only via chr(0x2014), which embeds no em dash
        # in this source file.
        assert src.count(chr(0x2014)) == 0, "real em dash found in test file source"


class TestSources:
    def test_listen_notes_verbatim(self):
        block = get_591_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block

    def test_audible_uk_verbatim(self):
        block = get_591_block()
        assert "https://www.audible.co.uk/podcast/The-Guilty-Feminist/B08K5Y1B25" in block

    def test_chortle_verbatim(self):
        block = get_591_block()
        assert "https://www.chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist" in block

    def test_guiltyfeminist_homepage_verbatim(self):
        block = get_591_block()
        # Listing surfaced the URL with a ref query param; keep verbatim per
        # the always-verbatim-URLs rule.
        assert "https://guiltyfeminist.com/?ref=quillette.com" in block

    def test_test_file_section(self):
        text = read_doc()
        assert TEST_FILE in text


class TestConfoundersAndLog:
    def test_five_strong_confounders(self):
        block = get_591_block()
        assert block.count("STRONG") >= 5

    def test_five_hour_cadence_bound(self):
        block = get_591_block()
        lower = block.lower()
        assert "five-hour cadence" in lower
        assert "16:00 PDT Sep 7" in block

    def test_log_entry_present_newest_first_anchored(self):
        # Anchored at the #590 main commit (eb31037): this verifies the
        # #591 run's predecessor state AT THAT TIME. Later iterations
        # (#592+) prepend their own entries, so the live newest-first
        # assertion is a time-bombshell; the anchored form is immutable
        # (rotation-guard anchor convention, Type D #565 followup).
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Iteration #591" in log or "#591 Type E" in log
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "show", "eb31037:iteration-log.md"],
            capture_output=True, text=True, check=True)
        anchored = out.stdout
        assert re.search(r"^#590 Type D", anchored, re.MULTILINE), \
            "no #590 Type D entry in iteration-log.md at eb31037"
        first_entry = re.search(r"^#\d+", anchored, re.MULTILINE)
        assert first_entry and first_entry.group(0) == "#590", \
            "iteration-log.md was not newest-first at #590 at eb31037"

    def test_rotation_transparency(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "590 D -> 591 E" in log

    def test_log_rotation_transparency_mentions_previous_commit(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "eb31037" in log

    def test_log_novelty_verification(self):
        log = LOG_PATH.read_text(encoding="utf-8")
        assert "Novelty Verification" in log
        assert "forty-first cycle is new" in log.lower()


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 587-590 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep591:
    WINDOW_591 = [FILE_587, FILE_588, FILE_589, FILE_590]

    @pytest.mark.parametrize("fname", WINDOW_591)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 587-591 window, closing the D->E edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carries the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard591:
    ANCHORED_COMMIT = "6da2928"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type E #591 followup: ...") and doc-sync ("Type C #589
    # doc-sync: ...") commits interleave between mains since the #572/#573/#574
    # convention change; the naive newest-5 filter broke on them. The colon
    # immediately after the iteration number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard591.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard591.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#591", "E"),
            ("#590", "D"),
            ("#589", "C"),
            ("#588", "B"),
            ("#587", "A"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # E->D is the edge this run closes; the full 5-window must be a
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
# must carry rows for #587-#591 with authoritative def-test counts. The
# #587/#588/#589/#590 rows were synced by their own runs (with the #588
# README row and both #589 rows repaired by #590). The #586 row must not
# decay. count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_591 = [
    # (iteration, test file, expected def-test count, keyword)
    ("587", FILE_587, 47, "Type A #587"),
    ("588", FILE_588, 38, "Type B #588"),
    ("589", FILE_589, 42, "Type C #589"),
    ("590", FILE_590, 46, "Type D #590"),
]


class TestDocSyncRatchet591:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_591)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_591)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCH.read_text(encoding="utf-8")
        assert fname in text, f"ARCHITECTURE missing row for {fname}"
        assert kw in text, f"ARCHITECTURE missing {kw} keyword"

    def test_591_own_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert TEST_FILE in text, "README missing own #591 row"

    def test_591_own_architecture_row_present(self):
        text = ARCH.read_text(encoding="utf-8")
        assert TEST_FILE in text, "ARCHITECTURE missing own #591 row"

    def test_586_row_survives(self):
        text = README.read_text(encoding="utf-8")
        assert "test_type_e_586_podcast_sentiment_fortieth_verification_sep07_11am.py" in text
        arch = ARCH.read_text(encoding="utf-8")
        assert "test_type_e_586_podcast_sentiment_fortieth_verification_sep07_11am.py" in arch
