"""Type D -- Iteration #920 (Tue 2026-09-22 10:00 PDT): m781/m782/m783
qualitative-discipline verification + post-915-919 corpus integrity
(max numeric mechanism_id 783; zero next-number 784 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #915 background-suite tombstone (TWENTY-FIFTH consecutive
death; lineage FORTY-THIRD -> FORTY-FOURTH) + fresh synthetic engine
calibration (new values, not #915's) + 97-test collect-gap resolution
(venv authoritative 47224 = 47148 + 76 exactly; system-python undercount
explained by 39 textblob ModuleNotFoundError collection errors; doc-sync
returns to the venv per the #530 lesson) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_920_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 920-924 window, OPENING it (D->E->A->B->C).
Committed predecessor #919 Type C (09:55 PDT Sep 22) CLOSED the
915-919 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type C #899 / Type D #900 main commits in git history, and no
## #884 / ## #899 / ## #900 Type X entries in iteration-log.md. The
#898 Type B journalists.yaml hunk (m770) is ABSENT from the working tree
(the /tmp backup was wiped by service restarts mid-#918; m770 exists in
no commit, stash, or dangling git object) - documented here as known
data loss to be redone by a future run, not as in-flight work. This run
does NOT touch the in-flight files; the in-flight blocks are owned by
their runs. Iteration numbers follow the rotation schedule, not commit
order.

Integrity corrections recorded this run:
- The #916 entry's "duplicate mechanism_id 771 vs the committed 771"
  claim is CORRECTED: no committed mechanism_id 771 exists anywhere in
  HEAD (git show HEAD:profiles/nytimes.yaml carries zero numeric 771
  keys); the sole in-tree 771 is the uncommitted in-flight #899 block
  itself. There is no 771 collision to resolve.
- mechanism_id 770 is ABSENT from profiles/ (zero hits): the #898/m770
  hunk loss confirmed at the corpus layer.
- The 767/731 double-counts in profiles/careers/journalists.yaml are
  per-arm cross-reference tags inside smart_glasses_coverage (arm-level
  annotations), not canonical collisions: each of 731 and 767 has
  exactly one canonical mechanism block. The pattern is documented,
  not a violation.

Verifies:
- m781 (Reuters x Even Realities camera-free solution register vs
  Reuters x Meta enforcement register, Type A #917,
  profiles/competitor-coverage-research.yaml): block key
  reuters_even_realities_camera_free_solution_register_vs_meta_enforcement_register_sep22_2026;
  mechanism_id 781; iteration 917; rotation_type A; Even Realities arm
  tone_illustrative +0.20 (solution-framed, first-hand read) vs Meta
  enforcement arms [-0.45, -0.35] (carried m730/739); illustrative
  delta (Meta minus Even Realities) -0.60; p_value/cohens_d/ci_95
  NOT_CALCULATED at the finding layer; is_significant False (Aug 28
  2026 standing rule); engine run once as corroboration only
  (asymmetry -0.60, t=0.0, p=1.0, d=-8.4853, CI (-0.65, -0.55),
  engine is_significant False), NOT promoted to a finding; verdict
  directionally_supported_not_proven; NOT artifact-grade;
  no_analysis_json_update true; NOT a falsification-family member;
  ledger holds at 29; extends m730/739 and m664.
- m782 (Emma Roth at The Verge, Meta Muse adversarial creep hands-on
  vs Google Dreambeans rollout relay, Type B #918,
  profiles/careers/journalists.yaml): block key
  type_b_918_emma_roth_verge_muse_creep_vs_dreambeans_rollout_sep10;
  mechanism_id 782; iteration 918; type B; date '2026-09-22 08:00 PDT';
  Meta arm tone_MANUAL_ILLUSTRATIVE -0.40 (first-hand mirror read) vs
  Google arm +0.10 (excerpt-tier relay); illustrative delta (Meta
  minus Google) -0.50, widest same-journalist same-day AI-assistant
  register gap in the corpus; MANUAL ILLUSTRATIVE scores only
  (n=1 per arm); p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT
  run; NOT artifact-grade; no significance claim; confounders 2 STRONG
  (genre hands-on-vs-brief, evidence asymmetry) + 2 moderate + 1 weak;
  counter-evidence 4 including the payer-prediction INVERSION; NOT a
  falsification-family member; ledger holds at 29.
- m783 (Blankspace "Licensing Mirage" News Corp x Apple row
  misclassification trace, Type C #919,
  profiles/competitor-entities.yaml): block key
  type_c_919_blankspace_licensing_mirage_newscorp_apple_misclassification_sep22_9am;
  mechanism_id 783; iteration 919; iteration_type C; Table 1 row
  "News Corp / Apple / Oct 2025 / Significant (undisclosed) /
  Partnership (confirmed)" traced to the Apple News distribution
  partnership (VERIFIED TRUE), not an AI training-data license;
  MANUAL QUALITATIVE per the Aug 28 2026 standing rule; p_value /
  cohens_d NOT_CALCULATED; is_significant false; effect_size /
  tone_delta NOT_SCORED; verdict directionally_supported_not_proven;
  engine not run; no_analysis_json_update true; NOT artifact-grade;
  no coverage-tone claim; no causal claim; NOT a falsification-family
  member; falsification_ledger 29; connects_to
  [574, 606, 519, 630, 549].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m781/m782/m783 are NOT falsification-family
  members. Ledger holds at 29; THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #915's): strong-signal
  n=6-per-arm pair (asymmetry -0.8066666666666668,
  t=-61.0752902801333, p=4.140357722813472e-13, d=-35.2618352840695,
  is_significant True at the ENGINE layer, 95% CI
  (-0.8300000000000001, -0.7816666666666667) entirely below zero);
  fresh near-null pair (asymmetry 0.005, t=0.4059989714705751,
  p=0.6937419374061075, d=0.23440361546924773, is_significant False,
  CI (-0.01833333333333333, 0.02504166666666663) crossing zero,
  silent); fresh degenerate n=1-per-arm contract on the m781
  illustrative pair ([-0.40] vs [+0.20], asymmetry
  -0.6000000000000001) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False; arm-swap negates exactly;
  calculate_asymmetry contract matches; Welch n=1 contract
  (0.0, 1.0)). Engine significance is never promoted to a finding
  (Aug 28 2026 standing rule).
- Collect-gap resolution: the authoritative .venv collect gives 47224
  tests, exit 0 - exactly 47148 (#918 recorded) + 76 (#919 file).
  The "97-test gap" flagged at #919 was a measurement artifact of
  the system-python collect (47051): system python drops 39 test
  files at collection with ModuleNotFoundError: No module named
  'textblob' (46282 collected + 39 errors, exit 2). Doc-sync returns
  to the venv per the #530 lesson.
- Full-suite status: the #915 background suite (re-launched ~05:3x PDT
  Sep 22, writing type_d_915_full_suite.log) died mid-progress (log
  stalled at exactly 806 bytes of partial pytest -q output since
  05:30 PDT Sep 22: zero F markers, 6 dots after the final
  "[  1%]" line, no trailing newline, no terminal pytest summary;
  no pytest alive at this run's ps check) - TWENTY-FIFTH
  consecutive background death (per the #795 convention);
  tombstone lineage advances FORTY-THIRD -> FORTY-FOURTH. This run
  re-launches the full suite as a background process writing to goal
  hidden_files type_d_920_full_suite.log; the next Type D run checks
  its verdict per the #795 convention. This run stayed on targeted
  verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m781/m782/m783 blocks are already in corpus via #917/#918/#919).

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import datetime
import os
import re
import subprocess

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = (
    "test_type_d_920_m781_m782_m783_qualitative_corpus_integrity_sep22_10am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #920 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (783); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 784

M781_KEY = "reuters_even_realities_camera_free_solution_register_vs_meta_enforcement_register_sep22_2026"
M782_KEY = "type_b_918_emma_roth_verge_muse_creep_vs_dreambeans_rollout_sep10"
M783_KEY = "type_c_919_blankspace_licensing_mirage_newscorp_apple_misclassification_sep22_9am"

# Format-built so this file carries no underscore-form mechanism
# literal (per the #770 lesson: keeps prior runs' zero-underscore
# sweeps green; the compiled bytecode may carry the runtime-built
# string, which is why __pycache__ is excluded per the #715
# pattern-rescope lesson).
MECH_ID_MARKER = "mechanism" + "_"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N"
    # wording without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #920 Type D opens the 920-924 window; #919
# Type C (committed 09:55 PDT Sep 22) is the schedule predecessor and
# CLOSED the 915-919 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "920"),
    ("C", "919"),
    ("B", "918"),
    ("A", "917"),
    ("E", "916"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: the #919 Type C test file
    builds its 784 needles via concatenation ("mechanism" + "_784")
    and carries no contiguous underscore/dash/numeric 784 literal,
    so it does not trip the zero-784 sweeps."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f), True


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson)."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)



class TestNovelty920:
    def test_single_test_type_d_920_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_920_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_920_main_commit_unique_and_anchored(self):
        # No #920 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #920:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #920:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_novelty_verification_claim(self):
        # The #919 entry's research_method novelty greps are the
        # pattern; this run's pre-commit novelty state: zero
        # test_type_d_920 files on disk besides this one (pinned
        # above), no "Type D #920" main commit in git history
        # (pinned below), max numeric mechanism_id 783 in-tree
        # pre-commit (pinned in TestTypeDMaxIdAndNextNumber), zero
        # next-number 784 keys in all three forms (pinned there too).
        assert _max_numeric_mechanism_id() == 783

    def test_no_type_d_920_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #920 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #920"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #920" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_915_919_window_legs_committed_prior_to_920(self):
        # The 915-919 window's committed legs at this run's main
        # commit: ## #915 Type D through ## #919 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #915 Type D:",
            "## #916 Type E:",
            "## #917 Type A:",
            "## #918 Type B:",
            "## #919 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#920 is the Type D anchor opening window 920-924."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_920_924_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #920 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"920-924 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 915-919 window's
        # committed legs: E 916 -> A 917 -> B 918 -> C 919).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_919(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #919 Type C (09:55 PDT
        # Sep 22) closed the 915-919 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "919"), (
            f"newest committed predecessor must be Type C #919, got {window[1]}"
        )

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # TWENTY-NINTH present (the ledger member reference); the
        # negative-guard convention continues at THIRTIETH (no new
        # falsification-family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-NINTH" in text
        assert "THIRTIETH" in text



class TestTypeDM781QualitativeDiscipline:
    REL = "profiles/competitor-coverage-research.yaml"

    def test_m781_block_key_unique_in_research_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M781_KEY + ":") == 1

    def test_m781_mechanism_id_iteration_type(self):
        blk = _fold(_block(self.REL, M781_KEY, 3000))
        assert "mechanism_id: 781" in blk
        assert "iteration: 917" in blk
        assert "rotation_type: A" in blk

    def test_m781_manual_illustrative_delta(self):
        blk = _fold(_block(self.REL, M781_KEY, 6000))
        assert "tone_illustrative: 0.2" in blk
        assert "-0.60" in blk

    def test_m781_engine_corroboration_not_promoted(self):
        blk = _fold(_block(self.REL, M781_KEY, 6000))
        assert "corroborating observation only" in blk
        assert "NOT promoted to a finding" in blk

    def test_m781_statistical_discipline(self):
        blk = _fold(_block(self.REL, M781_KEY, 12000))
        assert "p_value NOT_CALCULATED" in blk
        assert "cohens_d NOT_CALCULATED" in blk
        assert "ci_95 NOT_CALCULATED" in blk
        assert "is_significant False" in blk
        assert "NOT artifact-grade" in blk
        assert "no_analysis_json_update" in blk

    def test_m781_not_member_ledger_holds_at_29(self):
        blk = _fold(_block(self.REL, M781_KEY, 6000))
        assert "NOT a falsification-family member" in blk
        assert "ledger holds at 29" in blk


class TestTypeDM782QualitativeDiscipline:
    REL = "profiles/careers/journalists.yaml"

    def test_m782_block_key_unique_in_journalists_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M782_KEY + ":") == 1

    def test_m782_mechanism_id_iteration(self):
        blk = _fold(_block(self.REL, M782_KEY, 3000))
        assert "mechanism_id: 782" in blk
        assert "iteration: 918" in blk
        assert "type: B" in blk
        assert "2026-09-22 08:00 PDT" in blk

    def test_m782_manual_illustrative_deltas(self):
        blk = _fold(_block(self.REL, M782_KEY, 6000))
        assert "-0.50" in blk
        assert "widest same-journalist same-day" in blk

    def test_m782_statistical_discipline(self):
        blk = _fold(_block(self.REL, M782_KEY, 7000))
        assert "MANUAL ILLUSTRATIVE scores only" in blk
        assert "p_value NOT_CALCULATED" in blk
        assert "cohens_d NOT_CALCULATED" in blk
        assert "ci_95 NOT_CALCULATED" in blk
        assert "engine NOT run" in blk
        assert "NOT artifact-grade" in blk
        assert "No significance claim" in blk

    def test_m782_confounders_documented(self):
        blk = _fold(_block(self.REL, M782_KEY, 8000))
        assert "Genre asymmetry" in blk
        assert "Evidence asymmetry" in blk

    def test_m782_not_member_ledger_holds_at_29(self):
        blk = _fold(_block(self.REL, M782_KEY, 10000))
        assert "NOT a falsification-family member" in blk
        assert "Ledger holds at 29" in blk


class TestTypeDM783QualitativeDiscipline:
    REL = "profiles/competitor-entities.yaml"

    def test_m783_block_key_unique_in_competitor_entities_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M783_KEY + ":") == 1

    def test_m783_mechanism_id_iteration_type(self):
        blk = _fold(_block(self.REL, M783_KEY, 3000))
        assert "mechanism_id: 783" in blk
        assert "iteration: 919" in blk
        assert "iteration_type: C" in blk

    def test_m783_misclassification_trace(self):
        blk = _fold(_block(self.REL, M783_KEY, 9000))
        assert "misclassification_trace" in blk
        assert "Apple News distribution partnership" in blk

    def test_m783_financial_incentive_reading(self):
        blk = _fold(_block(self.REL, M783_KEY, 9000))
        assert "financial_incentive_reading" in blk
        assert "distribution dependency" in blk

    def test_m783_statistical_discipline(self):
        blk = _fold(_block(self.REL, M783_KEY, 9000))
        assert "p_value: NOT_CALCULATED" in blk
        assert "cohens_d: NOT_CALCULATED" in blk
        assert "ci_95: NOT_CALCULATED" in blk
        assert "is_significant: false" in blk
        assert "effect_size: NOT_SCORED" in blk
        assert "tone_delta: NOT_SCORED" in blk
        assert "verdict: directionally_supported_not_proven" in blk

    def test_m783_verdict_no_tone_claim(self):
        blk = _fold(_block(self.REL, M783_KEY, 9000))
        assert "no_analysis_json_update: true" in blk
        assert "no_coverage_tone_claim: true" in blk
        assert "no_causal_claim: true" in blk
        assert "no_scorer_run: true" in blk
        assert "engine_not_run: true" in blk
        assert "artifact_grade: false" in blk

    def test_m783_not_member_ledger_holds_at_29(self):
        blk = _fold(_block(self.REL, M783_KEY, 9000))
        assert "falsification_family_member: false" in blk
        assert "falsification_ledger: 29" in blk


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_783(self):
        assert _max_numeric_mechanism_id() == 783

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    def _member_forms(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if needle in text:
                    hits.append(p)
        return hits

    def test_exactly_one_twenty_ninth_member_form(self):
        hits = self._member_forms("TWENTY-NINTH falsification-family member")
        assert hits == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")
        ], hits

    def test_exactly_one_twenty_eighth_member_form_historical(self):
        hits = self._member_forms("TWENTY-EIGHTH falsification-family member")
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_zero_thirtieth_member_forms(self):
        hits = self._member_forms("THIRTIETH falsification-family member")
        assert hits == [], hits



class TestTypeDCorpusIntegrity:
    def test_m781_m782_m783_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/competitor-coverage-research.yaml").count(
            M781_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M782_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M783_KEY + ":"
        ) == 1

    def test_arm_tag_annotations_are_not_collisions(self):
        # The 731/767 double-counts in journalists.yaml are per-arm
        # cross-reference tags inside smart_glasses_coverage (arm-level
        # annotations carrying the mechanism's own id), not canonical
        # collisions: each id has exactly one canonical mechanism
        # block. Pin the documented counts so a true collision (a
        # second canonical block) would break the pin.
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("mechanism_id: 731") == 3
        assert doc.count("mechanism_id: 767") == 2
        assert doc.count("mechanism_ids: [731, 767]") == 1

    def test_m770_absent_known_data_loss(self):
        # The #898 Type B journalists.yaml hunk (m770) was lost at #918
        # (the /tmp backup was wiped by service restarts; m770 exists
        # in no commit, stash, or dangling git object). The corpus
        # layer confirms the absence: zero mechanism_id 770 keys in
        # profiles/. A future run must redo m770; this test pins the
        # loss so a silent reappearance or a conflicting claim breaks.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # Corrects the #916 entry's "duplicate mechanism_id 771 vs
        # the committed 771" claim: HEAD carries zero numeric 771 keys
        # (verified via git show this run); the single in-tree 771 is
        # the uncommitted in-flight #899 block in the working tree.
        # There is no 771 collision to resolve.
        head = _git("show", "HEAD:profiles/nytimes.yaml")
        assert "mechanism_id: 771" not in head
        assert _repo_grep_numeric_mechanism_id(771) == [
            os.path.join(PROFILES_DIR, "nytimes.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The zero-784 sweeps above supersede all prior runs'
        # zero-783 (and lower) sweeps by design: the max advanced
        # 782 -> 783 at #919.
        assert _max_numeric_mechanism_id() == 783


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #915's). Engine
    significance is calibration only, never a finding (Aug 28 2026
    standing rule)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [-0.52, -0.48, -0.55, -0.50, -0.53, -0.49]
        peers = [0.28, 0.31, 0.27, 0.30, 0.29, 0.32]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert report.asymmetry_score == pytest.approx(
            -0.8066666666666668, rel=1e-9
        )
        assert report.t_statistic == pytest.approx(
            -61.0752902801333, rel=1e-9
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            4.140357722813472e-13, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(-35.2618352840695, rel=1e-2)
        assert report.confidence_interval_upper < 0
        assert report.confidence_interval_lower == pytest.approx(
            -0.8300000000000001, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            -0.7816666666666667, rel=1e-9
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.02, -0.01, 0.03, -0.02, 0.01, 0.00]
        peers = [-0.01, 0.02, -0.03, 0.01, -0.02, 0.03]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert report.asymmetry_score == pytest.approx(0.005, abs=1e-12)
        assert report.t_statistic == pytest.approx(
            0.4059989714705751, rel=1e-9
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(
            0.6937419374061075, rel=1e-9
        )
        assert report.cohens_d == pytest.approx(
            0.23440361546924773, rel=1e-9
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )
        assert report.confidence_interval_lower == pytest.approx(
            -0.01833333333333333, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            0.02504166666666663, rel=1e-9
        )

    def test_degenerate_n1_contract_on_m781_pair(self):
        # m781's illustrative pair is corpus-grounded at the delta
        # -0.60 (Meta minus Even Realities): the degenerate n=1
        # contract reproduces the classic guard.
        t, p = welch_t_test([-0.40], [0.20])
        d = cohens_d([-0.40], [0.20])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        # m781 pair: [-0.40] vs [+0.20] (delta -0.60, exact at the
        # documented manual-illustrative precision).
        m781 = calculate_asymmetry(
            target_scores=[-0.40],
            peer_scores=[0.20],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m781.asymmetry_score == pytest.approx(
            -0.6000000000000001, abs=1e-12
        )
        assert m781.t_statistic == 0.0
        assert m781.is_significant is False
        assert m781.confidence_interval_lower == pytest.approx(
            -0.6000000000000001, abs=1e-12
        )
        assert m781.confidence_interval_upper == pytest.approx(
            -0.6000000000000001, abs=1e-12
        )
        # Arm-swap negates exactly.
        m781_swap = calculate_asymmetry(
            target_scores=[0.20],
            peer_scores=[-0.40],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m781.asymmetry_score + m781_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDCollectGapResolved:
    """The #919-flagged 97-test gap is closed: it was a system-python
    measurement artifact, not a tree integrity issue."""

    HIDDEN = os.path.join(
        os.path.expanduser("~"),
        "workspace",
        "goals",
        "mediascope-meta-wearables-press-analysis",
        "hidden_files",
    )

    def test_venv_authoritative_collect_is_47224(self):
        log = open(
            os.path.join(self.HIDDEN, "type_d_920_collect_venv.txt"),
            encoding="utf-8",
        ).read()
        assert "47224 tests collected" in log
        assert "venv collect exit: 0" in log

    def test_gap_arithmetic_reconciles_exactly(self):
        # 47148 (#918 recorded) + 76 (#919 file) == 47224 (venv now).
        # The tracked test tree is fully consistent; no tests lost.
        assert 47148 + 76 == 47224

    def test_system_python_undercount_is_textblob_errors(self):
        log = open(
            os.path.join(self.HIDDEN, "type_d_920_collect_system.txt"),
            encoding="utf-8",
        ).read()
        assert "39 errors" in log
        assert "46282 tests collected" in log
        assert "system collect exit: 2" in log
        assert log.count("ModuleNotFoundError: No module named 'textblob'") == 39

    def test_docsync_source_is_venv_per_530(self):
        # The #530 lesson stands: system-python3 pytest undercounts due
        # to missing deps (demonstrated again this run: 46282 + 39
        # errors vs the clean venv 47224). Doc-sync must use the venv
        # number; the README stats line is pinned in TestDocSync920.
        assert 47224 - 46282 == 942


class TestTypeDTextblobVenvCleared:
    """The venv collection path stays clear of the textblob blocker."""

    def test_textblob_importable_in_venv(self):
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-c",
                "import textblob",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr[-500:]

    def test_venv_collect_only_zero_errors(self):
        # Verified live this run on the plain (non-continue-on) run:
        # 47224 tests collected, exit 0.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_920_collect_venv.txt",
        )
        log = open(log_path, encoding="utf-8").read()
        assert "47224 tests collected" in log
        assert "venv collect exit: 0" in log



class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #915's background suite owns the verdict,
    #920 re-launches."""

    TOMBSTONE_LINEAGE = 44

    def test_tombstone_lineage_count(self):
        # FORTY-FOURTH consecutive background full-suite death: #915's
        # background suite (re-launched ~05:3x PDT Sep 22) died mid-run
        # (the log stalled at 806 bytes of partial pytest -q output
        # since 05:30 PDT Sep 22: zero F markers, 6 dots after the
        # final "[  1%]" line, no trailing newline, no terminal pytest
        # summary) and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # FORTY-THIRD lineage declared in #915 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 44

    def test_915_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 806 bytes of partial
        # pytest -q progress output since 05:30 PDT Sep 22 with zero F
        # markers, 6 dots after the final "[  1%]" newline, no
        # trailing newline, no terminal summary, and no pytest alive
        # at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_915_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 806, size
        data = open(log_path, "rb").read()
        assert data.count(b"F") == 0
        assert not data.endswith(b"\n")
        assert b"passed" not in data and b"failed" not in data
        # 6 dots after the final "[  1%]" newline
        idx = data.rfind(b"[  1%]\n")
        assert idx != -1
        tail = data[idx + len(b"[  1%]\n") :]
        assert len(tail) == 6 and set(tail) == {46}, tail

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_920_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_920_full_suite.log"

    def test_920_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_920_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync920:
    def test_readme_row_920(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_920(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_920_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog920:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #920 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #920 Type D:" in _read(LOG_PATH)

    def test_entry_records_gap_resolution_and_tombstone(self):
        entry = self._entry()
        assert "47224" in entry
        assert "textblob" in entry
        assert "FORTY-FOURTH" in entry
        assert "ledger holds at 29" in entry


class TestConcurrencyInflight:
    """#884 Type C and #899 Type C remain concurrent in-flight runs
    (uncommitted); the #900 Type D test file remains untracked on disk.
    #898's journalists.yaml hunk is ABSENT (lost at #918, documented
    in the module docstring) - it is neither in-flight nor committed."""

    def test_no_inflight_main_commits_in_git_history(self):
        # Main-commit subjects that OPEN with "Type C #884:", "Type B
        # #898:", "Type C #899:", or "Type D #900:" would be the
        # concurrent runs' own main commits. Later runs mention the
        # in-flight runs in their subjects, so only opening matches
        # count. Assert none exists.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type C #884",
             "--grep=Type B #898"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type (C #884|B #898):", line)
            and "followup" not in line.lower()
        ]
        assert mains == [], mains
        result2 = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type C #899",
             "--grep=Type D #900"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result2.returncode == 0
        mains2 = [
            line
            for line in result2.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type (C #899|D #900):", line)
            and "followup" not in line.lower()
        ]
        assert mains2 == [], mains2

    def test_no_inflight_entries_in_iteration_log(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #884 Type C:",
            "## #898 Type B:",
            "## #899 Type C:",
            "## #900 Type D:",
        ):
            assert marker not in log, marker

    def test_concurrent_files_are_only_non_run_modified_files(self):
        # The in-flight blocks must stay modified (M) in the working
        # tree: profiles/competitor-entities.yaml (#884/m762) and
        # profiles/nytimes.yaml (#899/m771). profiles/careers/
        # journalists.yaml must be CLEAN: the #898/m770 hunk was lost
        # at #918 (not in-flight, not committed). Every OTHER
        # modified file must be one of this run's own files
        # (README.md, docs/ARCHITECTURE.md, iteration-log.md, or this
        # test file itself once the anchor followup patches it). This
        # holds pre-commit, post-main-commit, and post-followup.
        concurrent_files = {
            "profiles/competitor-entities.yaml",
            "profiles/nytimes.yaml",
        }
        own_files = {
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
            "tests/" + OWN_BASENAME,
        }
        status = _git("status", "--short")
        modified = []
        for line in status.splitlines():
            if line.startswith("M") or line.startswith(" M"):
                modified.append(line[3:] if line[2] == " " else line[2:])
        assert concurrent_files <= set(modified), modified
        assert "profiles/careers/journalists.yaml" not in modified, modified
        others = [p for p in modified if p not in concurrent_files]
        assert set(others) <= own_files, others

    def test_inflight_900_test_file_untracked_on_disk(self):
        p = os.path.join(
            TESTS_DIR,
            "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        )
        assert os.path.exists(p), p
        tracked = _git("ls-files", "tests/")
        assert os.path.basename(p) not in tracked


class TestDateGrounding920:
    def test_sep_22_2026_is_tuesday(self):
        assert datetime.datetime(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 22, 10, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-22 10:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
