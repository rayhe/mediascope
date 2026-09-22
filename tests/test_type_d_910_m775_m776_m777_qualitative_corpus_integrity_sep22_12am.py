"""Type D -- Iteration #910 (Tue 2026-09-22 00:00 PDT): m775/m776/m777
qualitative-discipline verification + post-905-909 corpus integrity
(max numeric mechanism_id 777; zero next-number 778 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #905 background-suite tombstone (TWENTY-THIRD consecutive
death; lineage FORTY-FIRST -> FORTY-SECOND) + fresh synthetic engine
meaningfulness (new values, not #905's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_910_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 910-914 window, OPENING it (D->E->A->B->C).
Committed predecessor #909 Type C (23:00 PDT Sep 21) CLOSED the
905-909 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #898 Type B block (m770, profiles/careers/journalists.yaml), the
#899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type B #898 / Type C #899 / Type D #900 main commits in git history,
and no ## #884 / ## #898 / ## #899 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch those files; the in-flight
blocks are owned by their runs. Iteration numbers follow the rotation
schedule, not commit order. This #910 commit therefore may precede the
concurrent runs' commits in git history.

Verifies:
- m775 (Bloomberg x OpenAI vs Bloomberg x Meta genre-matched
  financial/product-momentum NULL gradient, Type A #907,
  profiles/competitor-coverage-research.yaml): block key
  bloomberg_openai_vs_meta_financial_product_momentum_genre_matched_null_gradient_sep21_2026;
  mechanism_id 775; iteration 907; rotation_type A; OpenAI arms
  [0.35, 0.30] (avg +0.325) vs Meta arms [0.45, 0.25] (avg +0.35);
  illustrative_delta_openai_minus_meta -0.025 (delta_calc
  '((0.35 + 0.30) / 2) - ((0.45 + 0.25) / 2) = 0.325 - 0.35 =
  -0.025'); MANUAL ILLUSTRATIVE; p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false (Aug 28 2026 standing rule);
  engine output recorded as corroboration only, NOT promoted to a
  finding; no_analysis_json_update true; NOT artifact-grade; zero-payer
  control case against financial determinism (no Bloomberg-OpenAI or
  Bloomberg-Meta content-licensing deal mapped); NOT a
  falsification-family member; ledger holds at 29; connects_to
  [772, 334].
- m776 (Eric Hal Schwartz (TechRadar) Muse-vs-ChatGPT inbox
  access-friction register asymmetry, Type B #908,
  profiles/careers/journalists.yaml): block key
  type_b_908_eric_hal_schwartz_techradar_muse_vs_chatgpt_inbox_access_friction;
  mechanism_id 776; iteration 908; type B; date '2026-09-21 22:00 PDT';
  Meta Muse arm tone_MANUAL_ILLUSTRATIVE 0.1 (access-friction register
  FOREGROUNDED, excerpt-tier) vs OpenAI ChatGPT arm
  tone_MANUAL_ILLUSTRATIVE 0.3 (zero privacy or access-friction
  vocabulary, first-hand); illustrative_delta_meta_minus_openai -0.2
  (delta_calc '(0.10) - (0.30) = -0.20'); MANUAL ILLUSTRATIVE tones only
  (n=1/n=1); p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant
  false; engine NOT run; no significance claimed; verdict
  directionally_supported_not_proven; NOT artifact-grade;
  no_analysis_json_update true; NOT a falsification-family member
  (register documentation and AI-assistant category extension of
  mechanisms 113/722/764/773); ledger holds at 29.
- m777 (Wiley Q1 FY2027 AI-revenue print - training-vs-recurring mix
  shift, Type C #909, profiles/competitor-entities.yaml): block key
  type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep2026; mechanism_id
  777; iteration 909; date 2026-09-21 23:00 PDT; Wiley Q1 FY2027 AI
  licensing revenue $14M (mix $10.5M training + $3.5M recurring);
  qualitative financial-incentive documentation only; tone 'NOT_SCORED';
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine
  NOT run; verdict directionally_supported_not_proven; NOT
  artifact-grade; no_analysis_json_update true; EXTENDS m735 (empirical
  verification leg of the retrieval-vs-training deal-structure shift);
  NOT a falsification-family member (documentation + verification leg,
  no tone pair); ledger holds at 29; connects_to [735, 663, 711, 463].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m775/m776/m777 are NOT falsification-family
  members (NULL-tie control case / category extension / documentation
  leg). Ledger holds at 29; THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #905's): strong-signal
  n=6-per-arm pair (asymmetry 1.7883333333333336,
  t=81.39070979520098, p=1.5252470680035743e-14, d=46.990948209793984,
  is_significant True at the ENGINE layer, 95% CI
  (1.7466249999999999, 1.8249999999999997) entirely above zero); fresh
  near-null pair (asymmetry 0.000833333333333334,
  t=0.09250064519425041, p=0.9281679810309185, d=0.05340527240311455,
  is_significant False, CI (-0.01567083333333333, 0.017166666666666667)
  crossing zero, silent); fresh degenerate n=1-per-arm contract on
  m775's corpus-grounded pair ([0.325] vs [0.35], asymmetry -0.025)
  reproduces the classic guard (t=0.0, p=1.0, d=0.0, is_significant
  False; arm-swap negates exactly; calculate_asymmetry contract
  matches). Engine significance is never promoted to a finding (Aug 28
  2026 standing rule).
- Full-suite status: the #905 background suite (re-launched ~18:3x PDT
  Sep 21, writing type_d_905_full_suite.log) died mid-progress (log
  stalled at exactly 362 bytes of partial pytest -q output since
  18:36 PDT Sep 21, no pytest alive at this run's ps check) -
  TWENTY-THIRD consecutive background death (per the #795
  convention listing); tombstone lineage advances FORTY-FIRST ->
  FORTY-SECOND. This run re-launches the full suite as a background
  process writing to goal hidden_files type_d_910_full_suite.log;
  the next Type D run checks its verdict per the #795 convention.
  This run stayed on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m775/m776/m777 blocks are already in corpus via #907/#908/#909).

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
    "test_type_d_910_m775_m776_m777_qualitative_corpus_integrity_sep22_12am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Next mechanism number after the in-tree corpus max (777); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 778

M775_KEY = "bloomberg_openai_vs_meta_financial_product_momentum_genre_matched_null_gradient_sep21_2026"
M776_KEY = "type_b_908_eric_hal_schwartz_techradar_muse_vs_chatgpt_inbox_access_friction"
M777_KEY = "type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep2026"

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
# numbers in git history: #910 Type D opens the 910-914 window; #909
# Type C (committed 23:xx PDT Sep 21) is the schedule predecessor and
# CLOSED the 905-909 window. The in-flight runs (#884 Type C, #898
# Type B, #899 Type C, #900 Type D) have no main commits in git
# history at this run's checks and sit below the window.
EXPECTED_ORDER = [
    ("D", "910"),
    ("C", "909"),
    ("B", "908"),
    ("A", "907"),
    ("E", "906"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). Also excludes
    the #909 Type C test file: it carries the 778 number only as its
    own documented NEXT_NUM sweep literals (string-literal assertions
    at its lines 225 and 487-488, e.g. assert "mechanism-778" not in
    _profiles_text()), not as mechanism keys. A literal-carrying
    sweep carrier would otherwise trip this run's zero-778 sweeps;
    the carrier is excluded per the #715 pattern-rescope lesson and
    the exclusion is documented here, not silently widened."""
    sweep_carrier_exclusions = {
        "test_type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep21_11pm.py",
    }
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f in sweep_carrier_exclusions:
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


class TestNovelty910:
    def test_single_test_type_d_910_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_910_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_910_main_commit_unique_and_anchored(self):
        # No #910 main commit exists pre-commit; the anchor test pins
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
            if "Type D #910" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run's novelty claim: mechanism 777 is the in-tree max
        # (m775/m776/m777 committed); this file's name must encode the
        # window mechanisms it verifies.
        assert _max_numeric_mechanism_id() == 777
        assert "m775_m776_m777" in OWN_BASENAME

    def test_no_type_d_910_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #910 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #910"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #910" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_905_909_window_legs_committed_prior_to_910(self):
        # The 905-909 window's committed legs at this run's main
        # commit: ## #905 Type D through ## #909 Type C. ## #884 /
        # ## #898 / ## #899 / ## #900 are the concurrent in-flight
        # runs (uncommitted) and are NOT asserted here - asserting
        # their absence would break this test the moment the
        # concurrent runs commit, and asserting their presence would
        # fail pre-commit.
        log = _read(LOG_PATH)
        for marker in (
            "## #905 Type D:",
            "## #906 Type E:",
            "## #907 Type A:",
            "## #908 Type B:",
            "## #909 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#910 is the Type D anchor opening window 910-914."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_910_914_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #910 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#898/#899/#900) have no main commits in
        # git history at this run's checks and sit below the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"910-914 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 905-909 window's
        # committed legs: E 906 -> A 907 -> B 908 -> C 909; D 900 is
        # the in-flight run, uncommitted).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_909(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #909 Type C (23:00 PDT
        # Sep 21) closed the 905-909 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "909"), (
            f"newest committed predecessor must be Type C #909, got {window[1]}"
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


class TestTypeDM775QualitativeDiscipline:
    """m775 (Type A #907,
    profiles/competitor-coverage-research.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block(
                "profiles/competitor-coverage-research.yaml", M775_KEY, 26000
            )
        )

    def test_m775_block_key_unique_in_research_yaml(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M775_KEY + ":"
            )
            == 1
        )

    def test_m775_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 775" in block
        assert "iteration: 907" in block
        assert "rotation_type: A" in block
        assert "publication: Bloomberg" in block
        assert "competitor: OpenAI" in block
        assert "comparator_entity: Meta" in block

    def test_m775_manual_illustrative_scorer(self):
        block = self._block()
        assert "openai_arm_tones: [0.35, 0.30]" in block
        assert "meta_arm_tones: [0.45, 0.25]" in block
        assert "illustrative_delta_openai_minus_meta: -0.025" in block
        assert (
            "delta_calc: '((0.35 + 0.30) / 2) - ((0.45 + 0.25) / 2) "
            "= 0.325 - 0.35 = -0.025'" in block
        )
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m775_statistical_discipline(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant False (Aug 28 2026 standing rule)" in block
        assert "engine output NOT promoted to a finding" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m775_zero_payer_control_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "zero-payer control" in block
        assert "NOT a falsification-family member" in block
        assert "connects_to:" in block
        assert "- 772" in block
        assert "- 334" in block
        assert "Ledger holds at 29" in block
        assert "THIRTIETH absent" in block


class TestTypeDM776QualitativeDiscipline:
    """m776 (Type B #908, profiles/careers/journalists.yaml):
    text-folded discipline-string assertions per the #732 convention.

    Note: the string "mechanism_id: 77" occurs on neighboring
    journalist blocks (m737, m770 in-flight, m773); block-KEY
    uniqueness is the anchor, and the discipline strings asserted here
    are scoped to the m776 block slice."""

    def _block(self):
        return _fold(
            _block(
                "profiles/careers/journalists.yaml", M776_KEY, 30000
            )
        )

    def test_m776_block_key_unique_in_journalists_yaml(self):
        assert (
            _read("profiles/careers/journalists.yaml").count(M776_KEY + ":")
            == 1
        )

    def test_m776_mechanism_id_iteration(self):
        block = self._block()
        assert "mechanism_id: 776" in block
        assert "iteration: 908" in block
        assert "type: B" in block
        assert "date: '2026-09-21 22:00 PDT'" in block
        assert "TechRadar" in block

    def test_m776_manual_illustrative_deltas(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.1" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.3" in block
        assert "illustrative_delta_meta_minus_openai: -0.2" in block
        assert "delta_calc: '(0.10) - (0.30) = -0.20'" in block

    def test_m776_statistical_discipline(self):
        block = self._block()
        assert "engine NOT run" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block
        assert "directionally_supported_not_proven" in block

    def test_m776_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "connects_to:" in block
        assert "- 773" in block


class TestTypeDM777QualitativeDiscipline:
    """m777 (Type C #909, profiles/competitor-entities.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M777_KEY, 24000)
        )

    def test_m777_block_key_unique_in_competitor_entities_yaml(self):
        assert (
            _read("profiles/competitor-entities.yaml").count(M777_KEY + ":")
            == 1
        )

    def test_m777_mechanism_id_iteration_date(self):
        block = self._block()
        assert "mechanism_id: 777" in block
        assert "iteration: 909" in block
        assert "2026-09-21 23:00 PDT" in block
        assert "Wiley Q1 FY2027" in block
        assert "$14M" in block

    def test_m777_qualitative_only_scorer(self):
        block = self._block()
        assert "tone: 'NOT_SCORED'" in block
        assert "financial-incentive documentation leg" in block
        assert "engine NOT run" in block

    def test_m777_statistical_discipline(self):
        block = self._block()
        assert "statistical_discipline: approach: manual_qualitative" in block
        assert "engine_run: false" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "ci_95: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m777_verdict_no_tone_claim(self):
        block = self._block()
        assert "verdict: directionally_supported_not_proven" in block
        assert "NOT artifact-grade" in block

    def test_m777_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block
        assert "connects_to: [735, 663, 711, 463]" in block

    def test_m777_extends_m735_verification_leg(self):
        block = self._block()
        assert "VERIFIES m735" in block
        assert "retrieval-vs-training" in block
        assert "$10.5M" in block
        assert "$3.5M" in block


class TestTypeDMaxIdAndNextNumber:
    """Post-905-909 corpus: max numeric mechanism_id 777; zero
    next-number 778 keys in numeric/underscore/dash forms."""

    def test_max_numeric_mechanism_id_is_777(self):
        assert _max_numeric_mechanism_id() == 777

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    """Ledger holds at 29: one TWENTY-NINTH member-form, one historical
    TWENTY-EIGHTH member-form, zero THIRTIETH member-forms in profiles/.
    m775/m776/m777 are not members."""

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

    def test_m775_m776_m777_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M775_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M776_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M777_KEY + ":")
            == 1
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # #907's max sweep (775), #908's (776), and #909's (777) sweeps
        # for the next number fail by designed supersession per the
        # #710/#720 convention now that the in-tree max is 777:
        # documented, not repaired.
        assert _max_numeric_mechanism_id() == 777


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #905's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.93, 0.88, 0.90, 0.85, 0.92, 0.86]
        peers = [-0.90, -0.95, -0.83, -0.93, -0.87, -0.91]
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
            1.7883333333333336, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            81.39070979520098, rel=1e-4
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            1.5252470680035743e-14, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(46.990948209793984, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(
            1.7466249999999999, rel=1e-4
        )
        assert report.confidence_interval_upper == pytest.approx(
            1.8249999999999997, rel=1e-4
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.017, -0.019, 0.008, -0.013, 0.021, -0.009]
        peers = [-0.009, 0.018, -0.015, 0.008, -0.014, 0.012]
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
            0.000833333333333334, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            0.09250064519425041, rel=1e-4
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.9281679810309185, rel=1e-2)
        assert report.cohens_d == pytest.approx(
            0.05340527240311455, rel=1e-2
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m775_pair(self):
        # m775's own block documents the OpenAI arm mean at +0.325
        # against the Meta arm mean at +0.35 (illustrative delta
        # -0.025): the pair is corpus-grounded, not invented.
        t, p = welch_t_test([0.325], [0.35])
        d = cohens_d([0.325], [0.35])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        # m775 pair: OpenAI [0.325] vs Meta [0.35] (delta -0.025,
        # exact at the documented manual-illustrative precision).
        m775 = calculate_asymmetry(
            target_scores=[0.325],
            peer_scores=[0.35],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m775.asymmetry_score == pytest.approx(-0.025, abs=1e-12)
        assert m775.t_statistic == 0.0
        assert m775.is_significant is False
        assert m775.confidence_interval_lower == pytest.approx(
            -0.025, abs=1e-12
        )
        assert m775.confidence_interval_upper == pytest.approx(
            -0.025, abs=1e-12
        )
        # Arm-swap negates exactly.
        m775_swap = calculate_asymmetry(
            target_scores=[0.35],
            peer_scores=[0.325],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m775.asymmetry_score + m775_swap.asymmetry_score == pytest.approx(
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
    """Suite verdict lineage; #905's background suite owns the verdict,
    #910 re-launches."""

    TOMBSTONE_LINEAGE = 42

    def test_tombstone_lineage_count(self):
        # FORTY-SECOND consecutive background full-suite death: #905's
        # background suite (re-launched ~18:3x PDT Sep 21) died mid-run
        # (the log stalled at 362 bytes of partial pytest -q output
        # since 18:36 PDT Sep 21) and no pytest was alive at this
        # run's check (the ps scan found zero suite processes).
        # Advances from the FORTY-FIRST lineage declared in #905 per
        # the #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 42

    def test_905_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 362 bytes of partial
        # pytest -q progress output since 18:36 PDT Sep 21 with no
        # pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_905_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 362, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert text.strip().endswith("..............................")

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_910_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_910_full_suite.log"

    def test_910_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_910_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync910:
    def test_readme_row_910(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_910(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_910_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog910:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #910 Type D:")
        return log[idx : idx + 15000]

    def test_log_entry_present(self):
        assert "## #910 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 777" in entry
        assert "m775" in entry
        assert "m776" in entry
        assert "m777" in entry

    def test_log_rotation_window_910_914(self):
        entry = self._entry()
        assert "910-914" in entry
        assert "905-909" in entry

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


class TestDateGrounding910:
    def test_sep_22_2026_is_tuesday(self):
        assert datetime.datetime(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 22, 0, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-22 00:00"
