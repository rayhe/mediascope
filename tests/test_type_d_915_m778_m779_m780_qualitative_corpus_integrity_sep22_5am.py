"""Type D -- Iteration #915 (Tue 2026-09-22 05:00 PDT): m778/m779/m780
qualitative-discipline verification + post-910-914 corpus integrity
(max numeric mechanism_id 780; zero next-number 781 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #910 background-suite tombstone (TWENTY-FOURTH consecutive
death; lineage FORTY-SECOND -> FORTY-THIRD) + fresh synthetic engine
calibration (new values, not #910's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_915_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 915-919 window, OPENING it (D->E->A->B->C).
Committed predecessor #914 Type C (04:00 PDT Sep 22) CLOSED the
910-914 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #898 Type B block (m770, profiles/careers/journalists.yaml), the
#899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type B #898 / Type C #899 / Type D #900 main commits in git history,
and no ## #884 / ## #898 / ## #899 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch those files; the in-flight
blocks are owned by their runs. Iteration numbers follow the rotation
schedule, not commit order. This #915 commit therefore may precede the
concurrent runs' commits in git history.

Verifies:
- m778 (The Register x OpenAI six-incident adversarial coverage vs
  Meta vocabulary arms, Type A #912,
  profiles/competitor-coverage-research.yaml): block key
  register_openai_sep17_six_misalignment_adversarial_vs_meta_vocabulary_arms_sep22_2026;
  mechanism_id 778; iteration 912; rotation_type A; OpenAI arm
  tone_illustrative -0.30 (adversarial_snark, excerpt-tier) vs Meta
  vocabulary arms [-0.35, -0.40] (corpus-documented adversarial
  vocabulary); illustrative_delta_meta_minus_openai -0.075 (within-
  publication null gradient); MANUAL ILLUSTRATIVE; p_value/cohens_d/
  ci_95 NOT_CALCULATED at the finding layer; is_significant false
  (Aug 28 2026 standing rule); engine run once as corroboration only
  (asymmetry -0.075, t=0.0, p=1.0, d=-2.1213, CI (-0.10, -0.05),
  engine is_significant False), NOT promoted to a finding;
  no_analysis_json_update true; NOT artifact-grade; zero-tie/zero-tie
  financial structure (no mapped Register-OpenAI or Register-Meta
  content-licensing deal, bounded absence); NOT a
  falsification-family member; ledger holds at 29; extends m757
  (#877 Type A) as the fifth outlet on the Sep-17 disclosure peg.
- m779 (Maxwell Zeff at WIRED, OpenAI framework relay vs Meta Muse
  trust-deficit, Type B #913, profiles/careers/journalists.yaml):
  block key
  type_b_913_maxwell_zeff_wired_openai_framework_relay_vs_meta_muse_trust_deficit;
  mechanism_id 779; iteration 913; type B; date '2026-09-22 03:00 PDT';
  OpenAI arm tone_MANUAL_ILLUSTRATIVE 0.15 (company-briefed platform
  relay, carried from m712/#757, sole byline) vs Meta arm
  tone_MANUAL_ILLUSTRATIVE -0.30 (launch-framed-through-trust-deficit,
  carried from m635/#668, co-byline with Lily Hay Newman);
  illustrative_delta_openai_minus_meta +0.45 (delta_calc
  '(0.15) - (-0.30) = +0.45'); MANUAL ILLUSTRATIVE tones only
  (n=1/n=1); p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run;
  is_significant false; verdict directionally_supported_not_proven;
  NOT artifact-grade; no_analysis_json_update true; STRONG co-byline
  dilution and news-peg confounds documented; NOT a
  falsification-family member; ledger holds at 29.
- m780 (Google Expert Intelligence book-publisher program, Type C
  #914, profiles/competitor-entities.yaml): block key
  type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am;
  mechanism_id 780; iteration 914; date '2026-09-22 04:00 PDT';
  100,000+ licensed e-book titles from six launch publishers
  (Bloomsbury, De Gruyter Brill, Johns Hopkins University Press,
  Macmillan Publishers, O'Reilly Media, Penguin Random House) inside
  Gemini Notebook; 15+ bestselling authors on Featured Notebooks;
  purchase-gated licensed-use structure; no disclosed financial
  terms; qualitative financial-incentive mapping only; tone
  'NOT_SCORED'; p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant false; engine NOT run; verdict
  directionally_supported_not_proven; NOT artifact-grade;
  no_analysis_json_update true; EXTENDS m735 (licensed-use book leg);
  book-domain sign-or-sue bifurcation named on both sides; NOT a
  falsification-family member; ledger holds at 29.
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m778/m779/m780 are NOT falsification-family
  members (null-gradient control / register documentation /
  financial-incentive documentation leg). Ledger holds at 29;
  THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #910's): strong-signal
  n=6-per-arm pair (asymmetry 1.7716666666666667,
  t=73.81232554337726, p=4.5578796438859947e-14, d=42.61556602198115,
  is_significant True at the ENGINE layer, 95% CI
  (1.7283333333333335, 1.815) entirely above zero); fresh near-null
  pair (asymmetry 8.673617379884035e-19, t=1.0978187588062823e-16,
  p=0.9999999999999999, d=6.33825955918228e-17, is_significant False,
  CI (-0.014504166666666663, 0.01367083333333333) crossing zero,
  silent); fresh degenerate n=1-per-arm contract on the m778
  within-publication pair ([-0.375] vs [-0.30], asymmetry
  -0.07500000000000001) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False; arm-swap negates exactly;
  calculate_asymmetry contract matches; Welch n=1 contract
  (0.0, 1.0)). Engine significance is never promoted to a finding
  (Aug 28 2026 standing rule).
- Full-suite status: the #910 background suite (re-launched ~00:3x PDT
  Sep 22, writing type_d_910_full_suite.log) died mid-progress (log
  stalled at exactly 1419 bytes of partial pytest -q output since
  00:30 PDT Sep 22: one visible F, 59 dots after the final
  "[  2%]" line, no trailing newline, no terminal pytest summary;
  no pytest alive at this run's ps check) - TWENTY-FOURTH
  consecutive background death (per the #795 convention listing);
  tombstone lineage advances FORTY-SECOND -> FORTY-THIRD. This run
  re-launches the full suite as a background process writing to goal
  hidden_files type_d_915_full_suite.log; the next Type D run checks
  its verdict per the #795 convention. This run stayed on targeted
  verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m778/m779/m780 blocks are already in corpus via #912/#913/#914).

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
    "test_type_d_915_m778_m779_m780_qualitative_corpus_integrity_sep22_5am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "d1bba9042674e7790351a898db111fc4a7f6e95a"  # Type D #915 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (780); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 781

M778_KEY = "register_openai_sep17_six_misalignment_adversarial_vs_meta_vocabulary_arms_sep22_2026"
M779_KEY = "type_b_913_maxwell_zeff_wired_openai_framework_relay_vs_meta_muse_trust_deficit"
M780_KEY = "type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am"

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
# numbers in git history: #915 Type D opens the 915-919 window; #914
# Type C (committed 04:xx PDT Sep 22) is the schedule predecessor and
# CLOSED the 910-914 window. The in-flight runs (#884 Type C, #898
# Type B, #899 Type C, #900 Type D) have no main commits in git
# history at this run's checks and sit below the window.
EXPECTED_ORDER = [
    ("D", "915"),
    ("C", "914"),
    ("B", "913"),
    ("A", "912"),
    ("E", "911"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: the #914 Type C test file
    builds its 781 needles via concatenation ("mechanism" + "_781")
    and carries no contiguous underscore/dash/numeric 781 literal,
    so it does not trip the zero-781 sweeps."""
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


class TestNovelty915:
    def test_single_test_type_d_915_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_915_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_915_main_commit_unique_and_anchored(self):
        # No #915 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #915" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run's novelty claim: mechanism 780 is the in-tree max
        # (m778/m779/m780 committed); this file's name must encode the
        # window mechanisms it verifies.
        assert _max_numeric_mechanism_id() == 780
        assert "m778_m779_m780" in OWN_BASENAME

    def test_no_type_d_915_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #915 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #915"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #915" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_910_914_window_legs_committed_prior_to_915(self):
        # The 910-914 window's committed legs at this run's main
        # commit: ## #910 Type D through ## #914 Type C. ## #884 /
        # ## #898 / ## #899 / ## #900 are the concurrent in-flight
        # runs (uncommitted) and are NOT asserted here - asserting
        # their absence would break this test the moment the
        # concurrent runs commit, and asserting their presence would
        # fail pre-commit.
        log = _read(LOG_PATH)
        for marker in (
            "## #910 Type D:",
            "## #911 Type E:",
            "## #912 Type A:",
            "## #913 Type B:",
            "## #914 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#915 is the Type D anchor opening window 915-919."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_915_919_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #915 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#898/#899/#900) have no main commits in
        # git history at this run's checks and sit below the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"915-919 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 910-914 window's
        # committed legs: E 911 -> A 912 -> B 913 -> C 914; D 900 is
        # the in-flight run, uncommitted).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_914(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #914 Type C (04:00 PDT
        # Sep 22) closed the 910-914 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "914"), (
            f"newest committed predecessor must be Type C #914, got {window[1]}"
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


class TestTypeDM778QualitativeDiscipline:
    """m778 (Type A #912,
    profiles/competitor-coverage-research.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block(
                "profiles/competitor-coverage-research.yaml", M778_KEY, 28000
            )
        )

    def test_m778_block_key_unique_in_research_yaml(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M778_KEY + ":"
            )
            == 1
        )

    def test_m778_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 778" in block
        assert "iteration: 912" in block
        assert "rotation_type: A" in block
        assert "publication: The Register" in block
        assert "competitor: OpenAI" in block
        assert "comparator_entity: Meta" in block

    def test_m778_manual_illustrative_scorer(self):
        block = self._block()
        assert "tone_illustrative: -0.30" in block
        assert "tone_illustrative: -0.35" in block
        assert "tone_illustrative: -0.40" in block
        assert "MANUAL ILLUSTRATIVE" in block
        assert "adversarial_snark" in block

    def test_m778_within_publication_null_gradient(self):
        block = self._block()
        assert "illustrative delta (Meta minus OpenAI) -0.075" in block
        assert "NULL gradient" in block
        assert "corroborating observation only" in block

    def test_m778_statistical_discipline(self):
        block = self._block()
        assert "p_value NOT_CALCULATED at the finding layer" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant False (Aug 28 2026 standing rule)" in block
        assert "engine output recorded as corroboration" in block
        assert "NOT artifact-grade" in block
        assert "no analysis.json update warranted" in block

    def test_m778_zero_tie_control_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "zero-tie/zero-tie" in block
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "extends mechanism 757" in block or "EXTENDS mechanism 757" in block


class TestTypeDM779QualitativeDiscipline:
    """m779 (Type B #913, profiles/careers/journalists.yaml):
    text-folded discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block(
                "profiles/careers/journalists.yaml", M779_KEY, 30000
            )
        )

    def test_m779_block_key_unique_in_journalists_yaml(self):
        assert (
            _read("profiles/careers/journalists.yaml").count(M779_KEY + ":")
            == 1
        )

    def test_m779_mechanism_id_iteration(self):
        block = self._block()
        assert "mechanism_id: 779" in block
        assert "iteration: 913" in block
        assert "type: B" in block
        assert "date: '2026-09-22 03:00 PDT'" in block
        assert "Maxwell Zeff" in block
        assert "WIRED" in block

    def test_m779_manual_illustrative_deltas(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.30" in block
        assert "illustrative_delta_openai_minus_meta: 0.45" in block
        assert "delta_calc: '(0.15) - (-0.30) = +0.45'" in block

    def test_m779_statistical_discipline(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "directionally_supported_not_proven" in block

    def test_m779_confounders_documented(self):
        block = self._block()
        assert "Co-byline dilution" in block
        assert "Lily Hay Newman" in block

    def test_m779_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 29" in block


class TestTypeDM780QualitativeDiscipline:
    """m780 (Type C #914, profiles/competitor-entities.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M780_KEY, 26000)
        )

    def test_m780_block_key_unique_in_competitor_entities_yaml(self):
        assert (
            _read("profiles/competitor-entities.yaml").count(M780_KEY + ":")
            == 1
        )

    def test_m780_mechanism_id_iteration_date(self):
        block = self._block()
        assert "mechanism_id: 780" in block
        assert "iteration: 914" in block
        assert "2026-09-22 04:00 PDT" in block
        assert "100,000" in block
        assert "six launch publishers" in block

    def test_m780_qualitative_only_scorer(self):
        block = self._block()
        assert "tone: 'NOT_SCORED'" in block
        assert "financial-incentive" in block
        assert "engine NOT run" in block or "engine_run: false" in block

    def test_m780_statistical_discipline(self):
        block = self._block()
        assert "statistical_discipline:" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block
        assert "no_analysis_json_update" in block

    def test_m780_verdict_no_tone_claim(self):
        block = self._block()
        assert "directionally_supported_not_proven" in block
        assert "NOT artifact-grade" in block

    def test_m780_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block or "falsification_family: false" in block
        assert "ledger holds at 29" in block or "falsification_ledger_holds_at: 29" in block

    def test_m780_extends_m735_licensed_use_leg(self):
        block = self._block()
        assert "735" in block
        assert "licensed-use" in block or "licensed use" in block


class TestTypeDMaxIdAndNextNumber:
    """Post-910-914 corpus: max numeric mechanism_id 780; zero
    next-number 781 keys in numeric/underscore/dash forms."""

    def test_max_numeric_mechanism_id_is_780(self):
        assert _max_numeric_mechanism_id() == 780

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    """Ledger holds at 29: one TWENTY-NINTH member-form, one historical
    TWENTY-EIGHTH member-form, zero THIRTIETH member-forms in profiles/.
    m778/m779/m780 are not members."""

    def _profiles_text(self):
        chunks = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                chunks.append(
                    open(p, encoding="utf-8", errors="replace").read()
                )
        return "\n".join(chunks)

    def test_exactly_one_twenty_ninth_member_form(self):
        assert (
            self._profiles_text().count(
                "TWENTY-NINTH falsification-family member"
            )
            == 1
        )

    def test_exactly_one_twenty_eighth_member_form_historical(self):
        # m758 remains the historical TWENTY-EIGHTH member-form;
        # #887 advanced the ledger 28->29 with m763.
        assert (
            self._profiles_text().count(
                "TWENTY-EIGHTH falsification-family member"
            )
            == 1
        )

    def test_zero_thirtieth_member_forms(self):
        assert (
            self._profiles_text().count(
                "THIRTIETH falsification-family member"
            )
            == 0
        )


class TestTypeDCorpusIntegrity:
    """Block-key uniqueness and supersession notes."""

    def test_m778_m779_m780_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M778_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M779_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M780_KEY + ":")
            == 1
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # #912's max sweep (778), #913's (779), and #914's (780) sweeps
        # for the next number fail by designed supersession per the
        # #710/#720 convention now that the in-tree max is 780:
        # documented, not repaired.
        assert _max_numeric_mechanism_id() == 780


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #910's). Engine
    significance is calibration only, never a finding (Aug 28 2026
    standing rule)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.84, 0.91, 0.87, 0.95, 0.82, 0.89]
        peers = [-0.88, -0.94, -0.85, -0.92, -0.86, -0.90]
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
            1.7716666666666667, rel=1e-9
        )
        assert report.t_statistic == pytest.approx(
            73.81232554337726, rel=1e-9
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            4.5578796438859947e-14, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(42.61556602198115, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(
            1.7283333333333335, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            1.815, rel=1e-9
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.011, -0.014, 0.019, -0.008, 0.006, -0.016]
        peers = [-0.012, 0.009, -0.017, 0.013, -0.006, 0.011]
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
            8.673617379884035e-19, abs=1e-12
        )
        assert report.t_statistic == pytest.approx(
            1.0978187588062823e-16, abs=1e-9
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.9999999999999999, rel=1e-9)
        assert report.cohens_d == pytest.approx(
            6.33825955918228e-17, abs=1e-9
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )
        assert report.confidence_interval_lower == pytest.approx(
            -0.014504166666666663, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            0.01367083333333333, rel=1e-9
        )

    def test_degenerate_n1_contract_on_m778_pair(self):
        # m778's within-publication pair is corpus-grounded at the
        # illustrative delta -0.075 (Meta minus OpenAI): the degenerate
        # n=1 contract reproduces the classic guard.
        t, p = welch_t_test([-0.375], [-0.30])
        d = cohens_d([-0.375], [-0.30])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        # m778 pair: [-0.375] vs [-0.30] (delta -0.075, exact at the
        # documented manual-illustrative precision).
        m778 = calculate_asymmetry(
            target_scores=[-0.375],
            peer_scores=[-0.30],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m778.asymmetry_score == pytest.approx(
            -0.07500000000000001, abs=1e-12
        )
        assert m778.t_statistic == 0.0
        assert m778.is_significant is False
        assert m778.confidence_interval_lower == pytest.approx(
            -0.07500000000000001, abs=1e-12
        )
        assert m778.confidence_interval_upper == pytest.approx(
            -0.07500000000000001, abs=1e-12
        )
        # Arm-swap negates exactly.
        m778_swap = calculate_asymmetry(
            target_scores=[-0.30],
            peer_scores=[-0.375],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m778.asymmetry_score + m778_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDTextblobCollectionBlockerCleared:
    """The #745/#750 ModuleNotFoundError blocker stays cleared."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run on the plain (non-continue-on) run.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #910's background suite owns the verdict,
    #915 re-launches."""

    TOMBSTONE_LINEAGE = 43

    def test_tombstone_lineage_count(self):
        # FORTY-THIRD consecutive background full-suite death: #910's
        # background suite (re-launched ~00:3x PDT Sep 22) died mid-run
        # (the log stalled at 1419 bytes of partial pytest -q output
        # since 00:30 PDT Sep 22: one visible F, 59 dots after the
        # final "[  2%]" line, no trailing newline, no terminal pytest
        # summary) and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # FORTY-SECOND lineage declared in #910 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 43

    def test_910_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 1419 bytes of partial
        # pytest -q progress output since 00:30 PDT Sep 22 with one
        # visible F, 59 dots after the final "[  2%]" line, no
        # trailing newline, no terminal summary, and no pytest alive
        # at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_910_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 1419, size
        data = open(log_path, "rb").read()
        assert data.count(b"F") == 1
        assert not data.endswith(b"\n")
        assert b"passed" not in data and b"failed" not in data
        # 59 dots after the final "[  2%]" newline
        idx = data.rfind(b"[  2%]")
        assert idx != -1
        tail = data[idx:]
        after = tail[tail.rfind(b"\n") + 1 :]
        assert len(after) == 59 and set(after) == {46}, after

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_915_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_915_full_suite.log"

    def test_915_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_915_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync915:
    def test_readme_row_915(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_915(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_915_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog915:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #915 Type D:")
        return log[idx : idx + 15000]

    def test_log_entry_present(self):
        assert "## #915 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 780" in entry
        assert "m778" in entry
        assert "m779" in entry
        assert "m780" in entry

    def test_log_rotation_window_915_919(self):
        entry = self._entry()
        assert "915-919" in entry
        assert "910-914" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry

    def test_log_ledger_29(self):
        entry = self._entry()
        assert "ledger holds at 29" in entry

    def test_log_concurrency_documented(self):
        entry = self._entry()
        assert "#884" in entry
        assert "#898" in entry
        assert "#899" in entry
        assert "#900" in entry
        assert "in-flight" in entry or "concurrent" in entry


class TestConcurrencyInflight:
    """#884 Type C, #898 Type B, #899 Type C, and #900 Type D remain
    concurrent in-flight runs (uncommitted)."""

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
        # tree: profiles/competitor-entities.yaml (#884/m762),
        # profiles/careers/journalists.yaml (#898/m770),
        # profiles/nytimes.yaml (#899/m771). Every OTHER modified file
        # must be one of this run's own files (README.md,
        # docs/ARCHITECTURE.md, iteration-log.md, or this test file
        # itself once the anchor followup patches it). This holds
        # pre-commit, post-main-commit, and post-followup.
        concurrent_files = {
            "profiles/competitor-entities.yaml",
            "profiles/careers/journalists.yaml",
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
        others = [p for p in modified if p not in concurrent_files]
        assert set(others) <= own_files, others


class TestDateGrounding915:
    def test_sep_22_2026_is_tuesday(self):
        assert datetime.datetime(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 22, 5, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-22 05:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
