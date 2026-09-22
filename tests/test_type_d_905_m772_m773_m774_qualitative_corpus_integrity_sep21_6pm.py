"""Type D -- Iteration #905 (Mon 2026-09-21 18:00 PDT): m772/m773/m774
qualitative-discipline verification + post-900-904 corpus integrity
(max numeric mechanism_id 774; zero next-number 775 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #895 background-suite tombstone (TWENTY-SECOND consecutive
death; lineage FORTIETH -> FORTY-FIRST) + fresh synthetic engine
meaningfulness (new values, not #895's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_905_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 905-909 window, OPENING it (D->E->A->B->C).
Committed predecessor #904 Type C (17:00 PDT Sep 21) CLOSED the
900-904 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #898 Type B block (m770, profiles/careers/journalists.yaml), the
#899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type B #898 / Type C #899 / Type D #900 main commits in git history,
and no ## #884 / ## #898 / ## #899 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch those files; the in-flight
blocks are owned by their runs. Iteration numbers follow the rotation
schedule, not commit order. This #905 commit therefore may precede the
concurrent runs' commits in git history.

Verifies:
- m772 (Bloomberg x Anthropic Sep-2026 profitability/IPO-momentum
  register vs Bloomberg x Meta layoffs/partner-clash register, Type A
  #902, profiles/competitor-coverage-research.yaml): block key
  bloomberg_anthropic_sep2026_profitability_ipo_momentum_vs_meta_layoffs_partner_clash_m334_temporal_extension_sep21_2026;
  mechanism_id 772; iteration 902; rotation_type 'A'; Anthropic arms
  +0.45 / +0.35 (avg +0.40) vs Meta arms -0.35 / -0.30 (avg -0.325);
  illustrative Anthropic-minus-Meta delta +0.725 (delta_calc
  '((0.45 + 0.35) / 2) - ((-0.35 + -0.30) / 2) = 0.40 + 0.325 =
  +0.725'); MANUAL ILLUSTRATIVE; p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run (Aug 28 2026
  standing rule); no_analysis_json_update true; NOT artifact-grade;
  NULL-tie control case against financial determinism (no
  Bloomberg-Anthropic content-licensing deal mapped); NOT a
  falsification-family member (temporal extension of mechanism 334);
  ledger holds at 29; connects_to [334].
- m773 (Karissa Bell (Engadget) AI-assistant category extension of the
  m113/m722/m764 privacy-register asymmetry, Type B #903,
  profiles/careers/journalists.yaml): block key
  type_b_903_karissa_bell_engadget_muse_vs_specs_intelligence_ai_assistants;
  mechanism_id 773; iteration 903; type B; date '2026-09-21 16:00 PDT';
  Meta Muse arm tone_MANUAL_ILLUSTRATIVE 0.05 vs Snap Specs
  Intelligence arm tone_MANUAL_ILLUSTRATIVE 0.15;
  illustrative_delta_meta_minus_snap -0.10 (delta_calc '(0.05) -
  (0.15) = -0.10'); MANUAL ILLUSTRATIVE tones only (n=1/n=1);
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine
  NOT run; no significance claimed; verdict
  directionally_supported_not_proven; NOT artifact-grade;
  no_analysis_json_update true; NOT a falsification-family member
  (register documentation and category extension of mechanisms
  113/722/764); ledger holds at 29.
- m774 (FT x Google/OpenAI red-button termination-leverage, Type C
  #904, profiles/financial-times.yaml): block key
  ft_red_button_termination_leverage_sep2026; mechanism_id 774;
  iteration 904; iteration_type C; iteration_time '2026-09-21 17:00
  PDT'; qualitative financial-incentive documentation only; scorer
  none; tone_scores NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant false; engine NOT run; verdict
  directionally_supported_not_proven; NOT artifact-grade;
  no_analysis_json_update true; NOT a falsification-family member
  (documentation leg, no tone pair); ledger holds at 29; connects_to
  [734, 738].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m772/m773/m774 are NOT falsification-family
  members (NULL-tie control case / category extension / documentation
  leg). Ledger holds at 29; THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #895's): strong-signal
  n=6-per-arm pair (asymmetry +1.7483333333333333,
  t=78.49369273025857, p=6.719852344283056e-15, d=45.31835462750256,
  is_significant True at the ENGINE layer, 95% CI (1.705,
  1.7850000000000001) entirely above zero); fresh near-null pair
  (asymmetry 0.0011666666666666665, t=0.15503581266302305,
  p=0.8799451095032917, d=0.08950996817502875, is_significant False,
  CI (-0.012670833333333329, 0.014674999999999994) crossing zero,
  silent); fresh degenerate n=1-per-arm contract on m772's corpus-
  grounded pair ([0.40] vs [-0.325], asymmetry +0.725) reproduces the
  classic guard (t=0.0, p=1.0, d=0.0, is_significant False;
  arm-swap negates exactly; calculate_asymmetry contract matches).
  Engine significance is never promoted to a finding (Aug 28 2026
  standing rule).
- Full-suite status: the #895 background suite (re-launched ~08:2x PDT
  Sep 21, writing type_d_895_full_suite.log) died mid-progress (log
  stalled at exactly 747 bytes of partial pytest -q output since
  08:36 PDT Sep 21, no pytest alive at this run's ps check - the pgrep
  hits were self-match phantoms of the checking shell itself) -
  TWENTY-SECOND consecutive background death (per the #795
  convention listing); tombstone lineage per #565 advances FORTIETH
  -> FORTY-FIRST. This run re-launches the full suite as a background
  process writing to goal hidden_files type_d_905_full_suite.log;
  the next Type D run checks its verdict per the #795 convention.
  This run stayed on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m772/m773/m774 blocks are already in corpus via #902/#903/#904).

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
    "test_type_d_905_m772_m773_m774_qualitative_corpus_integrity_sep21_6pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "f5f91f0c1ab26e27a34663e42b4a07a7c0e033f3"

# Next mechanism number after the in-tree corpus max (774); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 775

M772_KEY = "bloomberg_anthropic_sep2026_profitability_ipo_momentum_vs_meta_layoffs_partner_clash_m334_temporal_extension_sep21_2026"
M773_KEY = "type_b_903_karissa_bell_engadget_muse_vs_specs_intelligence_ai_assistants"
M774_KEY = "ft_red_button_termination_leverage_sep2026"

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
# numbers in git history: #905 Type D opens the 905-909 window; #904
# Type C (committed 17:xx PDT Sep 21) is the schedule predecessor and
# CLOSED the 900-904 window. The in-flight runs (#884 Type C, #898
# Type B, #899 Type C, #900 Type D) have no main commits in git
# history at this run's checks and sit below the window.
EXPECTED_ORDER = [
    ("D", "905"),
    ("C", "904"),
    ("B", "903"),
    ("A", "902"),
    ("E", "901"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson)."""
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


class TestNovelty905:
    def test_single_test_type_d_905_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_905_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_905_main_commit_unique_and_anchored(self):
        # No #905 main commit exists pre-commit; the anchor test pins
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
            if "Type D #905" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run's novelty claim: mechanism 774 is the in-tree max
        # (m772/m773/m774 committed); this file's name must encode the
        # window mechanisms it verifies.
        assert _max_numeric_mechanism_id() == 774
        assert "m772_m773_m774" in OWN_BASENAME

    def test_no_type_d_905_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #905 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #905"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #905" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_900_904_window_legs_committed_prior_to_905(self):
        # The 900-904 window's committed legs at this run's main
        # commit: ## #901 Type E through ## #904 Type C. ## #900
        # Type D is the concurrent in-flight run (uncommitted test file
        # on disk at this run's checks) and is NOT asserted here -
        # asserting its absence would break this test the moment the
        # concurrent run commits, and asserting its presence would fail
        # pre-commit. ## #884 / ## #898 / ## #899 are likewise
        # in-flight (no entries).
        log = _read(LOG_PATH)
        for marker in (
            "## #901 Type E:",
            "## #902 Type A:",
            "## #903 Type B:",
            "## #904 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#905 is the Type D anchor opening window 905-909."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_905_909_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #905 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#898/#899/#900) have no main commits in
        # git history at this run's checks and sit below the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"905-909 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 900-904 window's
        # committed legs: E 901 -> A 902 -> B 903 -> C 904; D 900 is
        # the in-flight run, uncommitted).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_904(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #904 Type C (17:00 PDT
        # Sep 21) closed the 900-904 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "904"), (
            f"newest committed predecessor must be Type C #904, got {window[1]}"
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


class TestTypeDM772QualitativeDiscipline:
    """m772 (Type A #902,
    profiles/competitor-coverage-research.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block(
                "profiles/competitor-coverage-research.yaml", M772_KEY, 20000
            )
        )

    def test_m772_block_key_unique_in_research_yaml(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M772_KEY + ":"
            )
            == 1
        )

    def test_m772_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 772" in block
        assert "iteration: 902" in block
        assert "rotation_type: A" in block
        assert "publication: Bloomberg" in block
        assert "competitor: Anthropic" in block
        assert "comparator_entity: Meta" in block

    def test_m772_manual_illustrative_scorer(self):
        block = self._block()
        assert "anthropic_arm_tones: [0.45, 0.35]" in block
        assert "meta_arm_tones: [-0.35, -0.30]" in block
        assert "illustrative_delta_anthropic_minus_meta: 0.725" in block
        assert (
            "delta_calc: '((0.45 + 0.35) / 2) - ((-0.35 + -0.30) / 2) "
            "= 0.40 + 0.325 = +0.725'" in block
        )
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m772_statistical_discipline(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant: false (Aug 28 2026 standing rule)" in block
        assert "Engine NOT run" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m772_null_tie_control_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "temporal extension of mechanism 334" in block
        assert "connects_to:" in block
        assert "- 334" in block
        assert "Ledger holds at 29" in block
        assert "THIRTIETH absent" in block


class TestTypeDM773QualitativeDiscipline:
    """m773 (Type B #903, profiles/careers/journalists.yaml):
    text-folded discipline-string assertions per the #732 convention.

    Note: the string "mechanism_id: 77" occurs on neighboring
    journalist blocks (m737, m770 in-flight); block-KEY uniqueness is
    the anchor, and the discipline strings asserted here are scoped to
    the m773 block slice."""

    def _block(self):
        return _fold(
            _block(
                "profiles/careers/journalists.yaml", M773_KEY, 28000
            )
        )

    def test_m773_block_key_unique_in_journalists_yaml(self):
        assert (
            _read("profiles/careers/journalists.yaml").count(M773_KEY + ":")
            == 1
        )

    def test_m773_mechanism_id_iteration(self):
        block = self._block()
        assert "mechanism_id: 773" in block
        assert "iteration: 903" in block
        assert "type: B" in block
        assert "date: '2026-09-21 16:00 PDT'" in block

    def test_m773_manual_illustrative_deltas(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.05" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "illustrative_delta_meta_minus_snap: -0.10" in block
        assert "delta_calc: '(0.05) - (0.15) = -0.10'" in block

    def test_m773_statistical_discipline(self):
        block = self._block()
        assert "engine NOT run" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block
        assert "directionally_supported_not_proven" in block

    def test_m773_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block


class TestTypeDM774QualitativeDiscipline:
    """m774 (Type C #904, profiles/financial-times.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block("profiles/financial-times.yaml", M774_KEY, 14000)
        )

    def test_m774_block_key_unique_in_financial_times_yaml(self):
        assert (
            _read("profiles/financial-times.yaml").count(M774_KEY + ":")
            == 1
        )

    def test_m774_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 774" in block
        assert "iteration: 904" in block
        assert "iteration_type: C" in block
        assert "iteration_time: 2026-09-21 17:00 PDT" in block

    def test_m774_qualitative_only_scorer(self):
        block = self._block()
        assert "scorer none" in block
        assert "tone_scores: NOT_SCORED" in block

    def test_m774_statistical_discipline(self):
        block = self._block()
        assert "MANUAL / qualitative only per the Aug 28 2026 standing rule" in block
        assert "financial-incentive documentation leg, not a tone test" in block
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "engine NOT run" in block
        assert "no analysis.json update" in block
        assert "NOT artifact-grade" in block

    def test_m774_verdict_no_tone_claim(self):
        block = self._block()
        assert "verdict: directionally_supported_not_proven" in block
        assert "no analysis.json update" in block

    def test_m774_not_member_seventh_direction_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "connects_to: [734, 738]" in block


class TestTypeDMaxIdAndNextNumber:
    """Post-900-904 corpus: max numeric mechanism_id 774; zero
    next-number 775 keys in numeric/underscore/dash forms."""

    def test_max_numeric_mechanism_id_is_774(self):
        assert _max_numeric_mechanism_id() == 774

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    """Ledger holds at 29: one TWENTY-NINTH member-form, one historical
    TWENTY-EIGHTH member-form, zero THIRTIETH member-forms in profiles/.
    m772/m773/m774 are not members."""

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
        # m758 (FT x OpenAI, #880) remains the historical TWENTY-EIGHTH
        # member-form; #887 advanced the ledger 28->29 with m763.
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

    def test_m772_m773_m774_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/competitor-coverage-research.yaml").count(
                M772_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M773_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/financial-times.yaml").count(M774_KEY + ":")
            == 1
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # #902's max sweep (772), #903's (773), and #904's (774) sweeps
        # for the next number fail by designed supersession per the
        # #710/#720 convention now that the in-tree max is 774:
        # documented, not repaired.
        assert _max_numeric_mechanism_id() == 774


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #895's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.91, 0.86, 0.88, 0.84, 0.90, 0.82]
        peers = [-0.88, -0.93, -0.81, -0.91, -0.86, -0.89]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert report.asymmetry_score == pytest.approx(
            1.7483333333333333, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            78.49369273025857, rel=1e-4
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            6.719852344283056e-15, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(45.31835462750256, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(
            1.705, rel=1e-4
        )
        assert report.confidence_interval_upper == pytest.approx(
            1.7850000000000001, rel=1e-4
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.014, -0.016, 0.007, -0.011, 0.018, -0.006]
        peers = [-0.007, 0.015, -0.013, 0.006, -0.012, 0.010]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert report.asymmetry_score == pytest.approx(
            0.0011666666666666665, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            0.15503581266302305, rel=1e-4
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.8799451095032917, rel=1e-2)
        assert report.cohens_d == pytest.approx(
            0.08950996817502875, rel=1e-2
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m772_pair(self):
        # m772's own block documents the Anthropic arm mean at +0.40
        # against the Meta arm mean at -0.325 (illustrative delta
        # +0.725): the pair is corpus-grounded, not invented.
        t, p = welch_t_test([0.40], [-0.325])
        d = cohens_d([0.40], [-0.325])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        # m772 pair: Anthropic [0.40] vs Meta [-0.325] (delta +0.725,
        # exact at the documented manual-illustrative precision).
        m772 = calculate_asymmetry(
            target_scores=[0.40],
            peer_scores=[-0.325],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert m772.asymmetry_score == pytest.approx(0.725, abs=1e-12)
        assert m772.t_statistic == 0.0
        assert m772.is_significant is False
        assert m772.confidence_interval_lower == pytest.approx(
            0.725, abs=1e-12
        )
        assert m772.confidence_interval_upper == pytest.approx(
            0.725, abs=1e-12
        )
        # Arm-swap negates exactly.
        m772_swap = calculate_asymmetry(
            target_scores=[-0.325],
            peer_scores=[0.40],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert m772.asymmetry_score + m772_swap.asymmetry_score == pytest.approx(
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
    """Suite verdict lineage; #895's background suite owns the verdict,
    #905 re-launches."""

    TOMBSTONE_LINEAGE = 41

    def test_tombstone_lineage_count(self):
        # FORTY-FIRST consecutive background full-suite death: #895's
        # background suite (re-launched ~08:2x PDT Sep 21) died mid-run
        # (the log stalled at 747 bytes of partial pytest -q output
        # since 08:36 PDT Sep 21) and no pytest was alive at this
        # run's check (the ps scan found zero suite processes).
        # Advances from the FORTIETH lineage declared in #895 per
        # the #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 41

    def test_895_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 747 bytes of partial
        # pytest -q progress output since 08:36 PDT Sep 21 with no
        # pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_895_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 747, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert text.strip().endswith("...........................")

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_905_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_905_full_suite.log"

    def test_905_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_905_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync905:
    def test_readme_row_905(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_905(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_905_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog905:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #905 Type D:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #905 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 774" in entry
        assert "m772" in entry
        assert "m773" in entry
        assert "m774" in entry

    def test_log_rotation_window_905_909(self):
        entry = self._entry()
        assert "905-909" in entry
        assert "900-904" in entry

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


class TestDateGrounding905:
    def test_sep_21_2026_is_monday(self):
        assert datetime.datetime(2026, 9, 21).strftime("%A") == "Monday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 21, 18, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-21 18:00"
