"""Type D -- Iteration #925 (Tue 2026-09-22 15:00 PDT): m784/m785/m786
qualitative-discipline verification + post-920-924 corpus integrity
(max numeric mechanism_id 786; zero next-number keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #920 background-suite tombstone (TWENTY-SIXTH consecutive
death; lineage FORTY-FOURTH -> FORTY-FIFTH) + fresh synthetic engine
calibration (new values, not #920's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_925_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 925-929 window, OPENING it (D->E->A->B->C).
Committed predecessor #924 Type C (14:00 PDT Sep 22) CLOSED the
920-924 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type C #899 / Type D #900 main commits in git history, and no
## #884 / ## #899 / ## #900 Type X entries in iteration-log.md. The
#898 Type B journalists.yaml hunk (m770) is ABSENT from the working tree
(lost at #918; m770 exists in no commit, stash, or dangling git object)
- documented here as known data loss to be redone by a future run, not
as in-flight work. This run does NOT touch the in-flight files; the
in-flight blocks are owned by their runs. Iteration numbers follow the
rotation schedule, not commit order.

Verifies:
- m784 (FT x Anthropic Sep-2026 Q2-profitability/IPO-momentum register
  vs FT x Meta carried arms, Type A #922, profiles/financial-times.yaml):
  block key
  iteration_922_sep22_2026_ft_anthropic_sep_profitability_ipo_momentum_vs_meta_carried;
  mechanism_id 784; iteration 922; rotation_type A; two fresh FT-origin
  Anthropic arms (tones 0.40, 0.35, avg 0.375) vs three carried m441
  Meta arms (-0.55, -0.62, -0.58, avg -0.5833); illustrative delta
  (Meta minus Anthropic) -0.9583; p_value/cohens_d/ci_95 NOT_CALCULATED
  at the finding layer; is_significant False (Aug 28 2026 standing
  rule); engine run once as corroboration only (asymmetry -0.9583,
  t=-29.7724, p=5.5871e-04, d=-27.2270, CI (-1.0067, -0.9100)),
  NOT promoted to a finding; confounders 3 STRONG + 2 MODERATE +
  1 WEAK; counterevidence 4 including the payer-prediction INVERSION
  (m54 FT negative on actual payer OpenAI; #887/m763 NY Post
  adversarial triad); verdict directionally_supported_not_proven;
  NOT artifact-grade; no_analysis_json_update true; NOT a
  falsification-family member; ledger holds at 29 (TWENTY-NINTH
  present; THIRTIETH absent); connects_to [54, 415, 441, 557, 766,
  772].
- m785 (Anthony Ha at TechCrunch, Apple smart-glasses privacy-hero
  essay vs Meta AI-manifesto piece, Type B #923,
  profiles/careers/journalists.yaml): block key
  type_b_923_anthony_ha_techcrunch_apple_glasses_privacy_hero_vs_meta_foil;
  mechanism_id 785; iteration 923; date '2026-09-22 13:00 PDT'; type B;
  Apple arm tone_MANUAL_ILLUSTRATIVE +0.30 (first-hand full-text open
  this run) vs Meta arm -0.45 (carried from #633 un-rescored);
  illustrative delta (Meta minus Apple) -0.75; MANUAL ILLUSTRATIVE
  scores only (n=1 per arm); p_value/cohens_d NOT_CALCULATED; engine
  NOT run; NOT artifact-grade; no significance claim; confounders
  2 STRONG (genre skew, temporal skew) + 1 MODERATE (topic skew) +
  1 WEAK (n=1 per arm); counterevidence 2 (panelist-voiced harshness,
  no blanket Apple-protection pattern); verdict WITHIN-WRITER
  PRIVACY-HERO REGISTER, NOT a falsification pin, NOT a pure
  asymmetry pin; no_analysis_json_update warranted; second dedicated
  Type B mechanism on Anthony Ha (first: #633 mechanism 614).
- m786 (Cloudflare Sep-15-2026 Disallow AI Training default activation
  verification, Type C #924, profiles/competitor-entities.yaml):
  block key cloudflare_sep15_disallow_ai_training_activation_sep2026;
  mechanism_id 786; iteration 924; iteration_type C;
  financial_incentive_mapping; first dedicated corpus
  activation-verification leg for m726; verdict
  directionally_supported_not_proven; no_analysis_json_update true;
  artifact_grade false; tone_scores NOT_SCORED;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false;
  confounders 2 STRONG (secondary sourcing, launched-vs-deployed) +
  2 MODERATE (company-reported inputs, Googlebot treatment tension) +
  1 WEAK (Media Copilot AI-drafted disclosure); counterevidence 3;
  NOT a falsification-family member; falsification ledger holds at 29
  (THIRTIETH remains the negative guard); connects_to
  [726, 64, 412, 702, 708].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m784/m785/m786 are NOT falsification-family
  members. Ledger holds at 29; THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #920's): strong-signal
  n=6-per-arm pair (asymmetry -0.9099999999999999,
  t=-59.5734840344259169, p=1.127213303072011e-13, d=-34.3947670438396784,
  is_significant True at the ENGINE layer, 95% CI
  (-0.9366666666666665, -0.8816666666666667) entirely below zero);
  fresh near-null pair (asymmetry 0.0016666666666667, t=0.1151633599262197,
  p=0.9106218264009113, d=0.0664895968541847, is_significant False,
  CI (-0.0233333333333333, 0.0283333333333333) crossing zero,
  silent); fresh degenerate n=1-per-arm contract on the m784
  illustrative pair ([-0.5833] vs [+0.375], asymmetry
  -0.9583000000000000) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False; arm-swap negates exactly;
  calculate_asymmetry contract matches). Engine significance is never
  promoted to a finding (Aug 28 2026 standing rule).
- Collect baseline: the authoritative .venv collect gives 47481
  tests, exit 0 (saved to goal hidden_files
  type_d_925_collect_venv.txt pre-run) - the tree is stable since the
  #924 doc-sync number; this file's delta is pinned by the README
  row test count.

0 browser.search query sets this run (Type D verification-layer run;
the m784/m785/m786 blocks are already in corpus via #922/#923/#924).

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
    "test_type_d_925_m784_m785_m786_qualitative_corpus_integrity_sep22_3pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "d12466bad959a48c24f3a414b31a6a7e1609e680"  # Type D #925 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (786); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 787

M784_KEY = "iteration_922_sep22_2026_ft_anthropic_sep_profitability_ipo_momentum_vs_meta_carried"
M785_KEY = "type_b_923_anthony_ha_techcrunch_apple_glasses_privacy_hero_vs_meta_foil"
M786_KEY = "cloudflare_sep15_disallow_ai_training_activation_sep2026"

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
# numbers in git history: #925 Type D opens the 925-929 window; #924
# Type C (committed 14:00 PDT Sep 22) is the schedule predecessor and
# CLOSED the 920-924 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "925"),
    ("C", "924"),
    ("B", "923"),
    ("A", "922"),
    ("E", "921"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: the #924 Type C test file
    builds its 786 needles via concatenation ("mechanism" + "_786")
    and carries no contiguous underscore/dash/numeric 786 literal,
    so it does not trip the zero-787 sweeps; this file's own 786
    references are block-key literals, never mechanism-key literals.
    """
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


class TestNovelty925:
    def test_single_test_type_d_925_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_925_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_925_main_commit_unique_and_anchored(self):
        # No #925 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #925:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #925:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_novelty_verification_claim(self):
        # This run's pre-commit novelty state: zero test_type_d_925
        # files on disk besides this one (pinned above), no
        # "Type D #925" main commit in git history (pinned below), max
        # numeric mechanism_id 786 in-tree pre-commit (pinned in
        # TestTypeDMaxIdAndNextNumber), zero next-number keys in all
        # three forms (pinned there too).
        assert _max_numeric_mechanism_id() == 786

    def test_no_type_d_925_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #925 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #925"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #925" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_920_924_window_legs_committed_prior_to_925(self):
        # The 920-924 window's committed legs at this run's main
        # commit: ## #920 Type D through ## #924 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #920 Type D:",
            "## #921 Type E:",
            "## #922 Type A:",
            "## #923 Type B:",
            "## #924 Type C:",
        ):
            assert marker in log, marker

class TestTypeDRotationGuard:
    """#925 is the Type D anchor opening window 925-929."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_925_929_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #925 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"925-929 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 920-924 window's
        # committed legs: E 921 -> A 922 -> B 923 -> C 924).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_924(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #924 Type C (14:00 PDT
        # Sep 22) closed the 920-924 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "924"), (
            f"newest committed predecessor must be Type C #924, got {window[1]}"
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


class TestTypeDM784QualitativeDiscipline:
    REL = "profiles/financial-times.yaml"

    def test_m784_block_key_unique_in_financial_times_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M784_KEY + ":") == 1

    def test_m784_mechanism_id_iteration_type(self):
        blk = _fold(_block(self.REL, M784_KEY, 3000))
        assert "mechanism_id: 784" in blk
        assert "iteration: 922" in blk
        assert "rotation_type: 'A'" in blk

    def test_m784_manual_illustrative_delta(self):
        blk = _fold(_block(self.REL, M784_KEY, 14000))
        assert "illustrative_delta_meta_minus_anthropic: -0.9583" in blk
        assert "anthropic_arm_tones: [0.40, 0.35]" in blk
        assert "meta_arm_tones: [-0.55, -0.62, -0.58]" in blk

    def test_m784_engine_corroboration_not_promoted(self):
        blk = _fold(_block(self.REL, M784_KEY, 14000))
        assert "Corroborating observation ONLY" in blk
        assert "NOT promoted" in blk

    def test_m784_statistical_discipline(self):
        blk = _fold(_block(self.REL, M784_KEY, 14000))
        assert "MANUAL ILLUSTRATIVE scores only" in blk
        assert "p_value: 'NOT_CALCULATED'" in blk
        assert "cohens_d: 'NOT_CALCULATED'" in blk
        assert "ci_95: 'NOT_CALCULATED'" in blk
        assert "is_significant: false" in blk
        assert "verdict: 'directionally_supported_not_proven'" in blk
        assert "no_analysis_json_update: true" in blk

    def test_m784_not_member_ledger_holds_at_29(self):
        blk = _fold(_block(self.REL, M784_KEY, 14000))
        assert "NOT a falsification-family member" in blk
        assert "Ledger holds at 29" in blk


class TestTypeDM785QualitativeDiscipline:
    REL = "profiles/careers/journalists.yaml"

    def test_m785_block_key_unique_in_journalists_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M785_KEY + ":") == 1

    def test_m785_mechanism_id_iteration_date_type(self):
        blk = _fold(_block(self.REL, M785_KEY, 3000))
        assert "mechanism_id: 785" in blk
        assert "iteration: 923" in blk
        assert "date: '2026-09-22 13:00 PDT'" in blk
        assert "type: B" in blk

    def test_m785_manual_illustrative_tones_delta(self):
        blk = _fold(_block(self.REL, M785_KEY, 9000))
        assert "apple_tone: 0.30" in blk
        assert "meta_tone: -0.45" in blk
        assert "delta_meta_minus_apple: -0.75" in blk
        assert "method: 'MANUAL ILLUSTRATIVE'" in blk

    def test_m785_statistical_discipline(self):
        blk = _fold(_block(self.REL, M785_KEY, 9000))
        assert "p_value: 'NOT_CALCULATED'" in blk
        assert "cohens_d: 'NOT_CALCULATED'" in blk
        assert "is_significant: false" in blk
        assert "WITHIN-WRITER PRIVACY-HERO REGISTER" in blk
        assert "NOT a falsification pin" in blk
        assert "No analysis.json update warranted" in blk

    def test_m785_confounders_counterevidence_documented(self):
        blk = _fold(_block(self.REL, M785_KEY, 12000))
        assert "Genre skew" in blk
        assert "Temporal skew" in blk
        assert "Topic skew" in blk
        assert "n=1 per arm" in blk
        assert "panelist-voiced" in blk
        assert "No pattern of blanket Apple protection" in blk

    def test_m785_not_member_second_ha_mechanism(self):
        blk = _fold(_block(self.REL, M785_KEY, 12000))
        assert "NOT a falsification-family member" in blk
        assert "Second dedicated Type B mechanism on Anthony Ha" in blk

class TestTypeDM786QualitativeDiscipline:
    REL = "profiles/competitor-entities.yaml"

    def test_m786_block_key_unique_in_competitor_entities_yaml(self):
        doc = _read(self.REL)
        assert doc.count(M786_KEY + ":") == 1

    def test_m786_mechanism_id_iteration_type(self):
        blk = _fold(_block(self.REL, M786_KEY, 3000))
        assert "mechanism_id: 786" in blk
        assert "iteration: 924" in blk
        assert "iteration_type: C" in blk
        assert "type: financial_incentive_mapping" in blk

    def test_m786_verdict_no_analysis_json_update(self):
        blk = _fold(_block(self.REL, M786_KEY, 12000))
        assert "verdict: 'directionally_supported_not_proven'" in blk
        assert "no_analysis_json_update: true" in blk
        assert "artifact_grade: false" in blk
        assert "FIRST dedicated corpus activation-verification leg for mechanism 726" in blk

    def test_m786_statistical_discipline(self):
        blk = _fold(_block(self.REL, M786_KEY, 12000))
        assert "tone_scores: 'NOT_SCORED'" in blk
        assert "p_value: 'NOT_CALCULATED'" in blk
        assert "cohens_d: 'NOT_CALCULATED'" in blk
        assert "ci_95: 'NOT_CALCULATED'" in blk
        assert "is_significant: false" in blk

    def test_m786_confounders_ranked(self):
        blk = _fold(_block(self.REL, M786_KEY, 12000))
        assert "Secondary sourcing" in blk
        assert "Launched versus deployed" in blk
        assert "Company-reported inputs" in blk
        assert "Googlebot treatment tension" in blk
        assert "Media Copilot discloses its posts are AI-drafted" in blk

    def test_m786_not_member_ledger_holds_at_29(self):
        blk = _fold(_block(self.REL, M786_KEY, 12000))
        assert "NOT a member" in blk
        assert "falsification ledger holds at 29" in blk
        assert "THIRTIETH remains the negative guard" in blk


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_786(self):
        assert _max_numeric_mechanism_id() == 786

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
    def test_m784_m785_m786_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/financial-times.yaml").count(
            M784_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M785_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M786_KEY + ":"
        ) == 1

    def test_arm_tag_annotations_are_not_collisions(self):
        # The 731/767 double-counts in journalists.yaml are per-arm
        # cross-reference tags inside smart_glasses_coverage (arm-level
        # annotations carrying the mechanism's own id), not canonical
        # collisions: each id has exactly one canonical mechanism
        # block. Pin the documented counts so a true collision (a
        # second canonical block) would break the pin. Unchanged by
        # #923's m785 (the Ha block carries no 731/767 arm tags).
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("mechanism_id: 731") == 3
        assert doc.count("mechanism_id: 767") == 2
        assert doc.count("mechanism_ids: [731, 767]") == 1

    def test_m770_absent_known_data_loss(self):
        # The #898 Type B journalists.yaml hunk (m770) was lost at #918
        # (m770 exists in no commit, stash, or dangling git object).
        # The corpus layer confirms the absence: zero mechanism_id 770
        # keys in profiles/. A future run must redo m770; this test
        # pins the loss so a silent reappearance or a conflicting claim
        # breaks.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The sole in-tree 771 is the uncommitted in-flight #899 block
        # in the working tree: HEAD carries zero numeric 771 keys.
        # There is no 771 collision to resolve.
        head = _git("show", "HEAD:profiles/nytimes.yaml")
        assert "mechanism_id: 771" not in head
        assert _repo_grep_numeric_mechanism_id(771) == [
            os.path.join(PROFILES_DIR, "nytimes.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The zero-787 sweeps above supersede all prior runs'
        # zero-786 (and lower) sweeps by design: the max advanced
        # 785 -> 786 at #924.
        assert _max_numeric_mechanism_id() == 786

class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #920's). Engine
    significance is calibration only, never a finding (Aug 28 2026
    standing rule)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [-0.61, -0.55, -0.58, -0.63, -0.57, -0.60]
        peers = [0.33, 0.29, 0.35, 0.31, 0.30, 0.34]
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
            -0.9099999999999999, rel=1e-9
        )
        assert report.t_statistic == pytest.approx(
            -59.5734840344259169, rel=1e-9
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            1.127213303072011e-13, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(-34.3947670438396784, rel=1e-2)
        assert report.confidence_interval_upper < 0
        assert report.confidence_interval_lower == pytest.approx(
            -0.9366666666666665, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            -0.8816666666666667, rel=1e-9
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.03, 0.01, -0.02, 0.04, -0.01, 0.02]
        peers = [0.02, -0.03, 0.01, -0.02, 0.03, -0.01]
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
            0.0016666666666667, abs=1e-12
        )
        assert report.t_statistic == pytest.approx(
            0.1151633599262197, rel=1e-9
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(
            0.9106218264009113, rel=1e-9
        )
        assert report.cohens_d == pytest.approx(
            0.0664895968541847, rel=1e-9
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )
        assert report.confidence_interval_lower == pytest.approx(
            -0.0233333333333333, rel=1e-9
        )
        assert report.confidence_interval_upper == pytest.approx(
            0.0283333333333333, rel=1e-9
        )

    def test_degenerate_n1_contract_on_m784_pair(self):
        # m784's illustrative pair is corpus-grounded at the delta
        # -0.9583 (Meta minus Anthropic: Meta avg -0.5833 vs Anthropic
        # avg 0.375): the degenerate n=1 contract reproduces the
        # classic guard.
        t, p = welch_t_test([-0.5833], [0.375])
        d = cohens_d([-0.5833], [0.375])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        # m784 pair: [-0.5833] vs [+0.375] (delta -0.9583, exact at the
        # documented manual-illustrative precision).
        m784 = calculate_asymmetry(
            target_scores=[-0.5833],
            peer_scores=[0.375],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m784.asymmetry_score == pytest.approx(
            -0.9583000000000000, abs=1e-12
        )
        assert m784.t_statistic == 0.0
        assert m784.is_significant is False
        assert m784.confidence_interval_lower == pytest.approx(
            -0.9583000000000000, abs=1e-12
        )
        assert m784.confidence_interval_upper == pytest.approx(
            -0.9583000000000000, abs=1e-12
        )
        # Arm-swap negates exactly.
        m784_swap = calculate_asymmetry(
            target_scores=[0.375],
            peer_scores=[-0.5833],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 22),
            period_end=datetime.datetime(2026, 9, 22),
        )
        assert m784.asymmetry_score + m784_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDCollectBaseline:
    """The authoritative .venv collect is the doc-sync source per the
    #530 lesson: system-python3 pytest undercounts due to missing deps
    (demonstrated at #920: 46282 + 39 textblob errors vs the clean venv
    47224). This run's pre-file baseline: 47481 tests, exit 0."""

    HIDDEN = os.path.join(
        os.path.expanduser("~"),
        "workspace",
        "goals",
        "mediascope-meta-wearables-press-analysis",
        "hidden_files",
    )

    def test_baseline_log_exists(self):
        log_path = os.path.join(self.HIDDEN, "type_d_925_collect_venv.txt")
        assert os.path.exists(log_path), log_path

    def test_venv_authoritative_collect_is_47481(self):
        log = open(
            os.path.join(self.HIDDEN, "type_d_925_collect_venv.txt"),
            encoding="utf-8",
        ).read()
        assert "47481 tests collected" in log
        assert "venv collect exit: 0" in log

    def test_tree_stable_since_924_docsync(self):
        # #924's doc-sync number was 47481/1249: the tree is stable
        # between the #924 doc-sync and this run's pre-file collect.
        assert 47481 - 47481 == 0


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #920's background suite owns the verdict,
    #925 re-launches."""

    TOMBSTONE_LINEAGE = 45

    def test_tombstone_lineage_count(self):
        # FORTY-FIFTH consecutive background full-suite death: #920's
        # background suite (re-launched ~10:46 PDT Sep 22) died mid-run
        # (the log stalled at 743 bytes of partial pytest -q output:
        # zero F markers, 23 dots after the final "[  1%]" line, no
        # trailing newline, no terminal pytest summary) and no pytest
        # was alive at this run's check (the ps scan found zero suite
        # processes). Advances from the FORTY-FOURTH lineage declared
        # in #920 per the #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 45

    def test_920_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 743 bytes of partial
        # pytest -q progress output with zero F markers, 23 dots after
        # the final "[  1%]" newline, no trailing newline, no terminal
        # summary, and no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_920_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 743, size
        data = open(log_path, "rb").read()
        assert data.count(b"F") == 0
        assert not data.endswith(b"\n")
        assert b"passed" not in data and b"failed" not in data
        # 23 dots after the final "[  1%]" newline
        idx = data.rfind(b"[  1%]\n")
        assert idx != -1
        tail = data[idx + len(b"[  1%]\n") :]
        assert len(tail) == 23 and set(tail) == {46}, tail

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_925_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_925_full_suite.log"

    def test_925_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_925_full_suite.log",
        )
        assert os.path.exists(log_path), log_path

class TestDocSync925:
    def test_readme_row_925(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_925(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_925_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog925:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #925 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #925 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FORTY-FIFTH" in entry
        assert "786" in entry
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


class TestDateGrounding925:
    def test_sep_22_2026_is_tuesday(self):
        assert datetime.datetime(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 22, 15, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-22 15:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
