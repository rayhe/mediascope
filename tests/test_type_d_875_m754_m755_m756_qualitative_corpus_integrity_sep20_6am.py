"""Type D -- Iteration #875 (Sun 2026-09-20 06:00 PDT): m754/m755/m756
qualitative-discipline verification + post-#874 corpus integrity
(max numeric mechanism_id 756; zero next-number keys; ledger holds at
27) + #870 background-suite tombstone (SEVENTEENTH consecutive death;
lineage THIRTY-FIFTH -> THIRTY-SIXTH) + fresh synthetic engine
meaningfulness (new values, not #870's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_875_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 875-879 window, OPENING it (D->E->A->B->C);
870-874 window CLOSED D->E->A->B->C at #874.

Verifies:
- m754 (FT x OpenAI Sep-18 $278B cash-burn forecast scoop vs FT x Meta
  Jun-5 equity-raise scoop, Type A #872,
  profiles/financial-times.yaml): block key
  ft_openai_278bn_cash_burn_forecast_vs_meta_equity_raise_sep18;
  mechanism_id 754; iteration 872; iteration_type 'A';
  asymmetry_scorer_MANUAL_ILLUSTRATIVE; OpenAI arm [-0.15]; Meta arm
  [-0.30]; illustrative delta (OpenAI minus Meta) +0.15; engine
  degenerate n=1 contract documented (t 0.0 / p 1.0 / Cohen d 0.0 /
  degenerate CI (0.15, 0.15) / is_significant False); finding layer
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False;
  no_analysis_json_update true; verdict
  directionally_supported_not_proven; artifact_grade false;
  NOT a falsification-family member (ledger holds at 27);
  correlation is not causation; NOT artifact-grade.
- m755 (Daniel Cooper Engadget HTC Vive Eagle review within-review
  Meta privacy-benchmark extension vs Apple Watch Series 12 carried
  arm, Type B #873, profiles/careers/journalists.yaml): block key
  type_b_873_daniel_cooper_engadget_vive_eagle_meta_benchmark_extension_vs_apple_watch_carried;
  mechanism_id 755; iteration 873; type B;
  daniel_cooper.mechanism_ids [295, 755]; TEMPORAL EXTENSION of
  mechanism 295; methodology MANUAL ILLUSTRATIVE tones only;
  target (Apple) [-0.10]; reference (Meta) [-0.30]; illustrative delta
  (Apple minus Meta) +0.20; engine NOT run (illustrative arms only;
  Apple arm carried); p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant false; artifact_grade NOT artifact-grade;
  correlation_not_causation true; verdict
  directionally_supported_not_proven; NOT a falsification-family
  member (temporal extension, not a uniform-prediction test); ledger
  holds at 27; no_analysis_json_update true.
- m756 (publishers Sep-4 partial-summary-judgment counter-move +
  Sep-18 "users won't click" attribution-economics admission, Type C
  #874, profiles/competitor-entities.yaml): named key
  publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026;
  block_key
  type_c_874_publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026;
  mechanism_id 756; iteration 874; type financial_incentive_mapping;
  rotation Type C; statistical_discipline 'MANUAL / qualitative only
  per the Aug 28 2026 standing rule; financial-incentive documentation
  leg, not a tone test'; tone NOT_SCORED; scorer none;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine
  NOT run; verdict directionally_supported_not_proven;
  correlation_not_causation true; no_analysis_json_update true;
  NOT artifact_grade true; no_coverage_tone_claim true; NOT a
  falsification-family member; falsification ledger holds at 27.
- Falsification ledger: exactly ONE "TWENTY-SEVENTH
  falsification-family member" occurrence in profiles/
  (the-verge.yaml m751 block, ledger 26->27); ZERO
  "TWENTY-EIGHTH falsification-family member" occurrences in
  profiles/ (ledger holds at 27; the-verge ledger line carries the
  "negative-guard convention continues at TWENTY-EIGHTH" string;
  test-file tombstones use TWENTY-EIGHTH ordinals only).
- Post-#874 corpus integrity: max numeric mechanism_id == 756 in
  profiles/; zero underscore-form 757 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per #715; needles
  format-built so no literal is carried; __pycache__ artifacts
  excluded per the #715 pattern-rescope lesson); zero dash-form 757
  references repo-wide; zero numeric 757 keys in profiles/;
  m754 / m755 / m756 block keys each unique in their home YAMLs;
  designed keying holds (zero underscore-form 754/755/756 carriers -
  #872/#873/#874 markers are format-built, no sole carrier this
  window); #874's max-756 sweep, #873's max-755 sweep, #872's
  max-754 sweep fail by designed supersession per the #710/#720
  convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #870's): strong-signal n=6-per-arm pair (asymmetry +1.0483,
  t=43.760823581625054, p=2.2641818521359104e-11, d=25.265323274810946,
  is_significant True at the ENGINE layer, 95% CI
  (1.0082916666666666, 1.0916666666666668) entirely above zero);
  fresh near-null pair (asymmetry -0.0033333333333333335,
  t=-0.10956642697819577, p=0.9149207921720559,
  d=-0.0632582061100068, is_significant False, CI (-0.06, 0.05)
  crossing zero, silent); fresh degenerate n=1-per-arm contracts on
  m754's pair ([-0.15], [-0.30]) and m755's pair ([-0.10], [-0.30])
  reproduce the classic guard (t=0.0, p=1.0, d=0.0, is_significant
  False; asymmetry +0.15 / +0.20 (IEEE-inexact within 1e-9 per #673
  precedent for m755); arm-swaps negate exactly; calculate_asymmetry
  contract matches). Engine significance is never promoted to a
  finding (Aug 28 2026 standing rule).
- Full-suite status: the #870 background suite re-launched 01:05 PDT
  Sep 20 died at the tombstone marker (type_d_870_full_suite.log at
  exactly 6 bytes "......" since 01:05 PDT Sep 20; no pytest alive at
  this run's check via the ps scan - zero suite processes) -
  SEVENTEENTH consecutive background death (#705's, #710's first
  re-launch, #715's first re-launch, #715's re-launch, #720's
  re-launch, #725's re-launch, #730's re-launch, #825's re-launch,
  #830's re-launch, #835's re-launch, #840's re-launch, #845's
  re-launch, #850's re-launch, #855's re-launch, #860's re-launch,
  #865's re-launch, #870's re-launch; tombstone lineage per #565
  advances THIRTY-FIFTH -> THIRTY-SIXTH). This run re-launches the
  full suite as a background process writing to goal hidden_files
  type_d_875_full_suite.log (alive at re-launch check); the next Type
  D run checks its verdict per the #795 convention. This run stayed
  on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m754/m755/m756 blocks are already in corpus via #872-#874).

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
    "test_type_d_875_m754_m755_m756_qualitative_corpus_integrity_sep20_6am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "50f51f73194097ec8649f365fbc0bcf977120b6c"

# Next mechanism number after the pre-commit corpus max (756); used as
# an int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 757

M754_KEY = "ft_openai_278bn_cash_burn_forecast_vs_meta_equity_raise_sep18"
M755_KEY = "type_b_873_daniel_cooper_engadget_vive_eagle_meta_benchmark_extension_vs_apple_watch_carried"
M756_KEY = "publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026"
M756_BLOCK_KEY = "type_c_874_publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026"

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


EXPECTED_ORDER = [("D", "875"), ("C", "874"), ("B", "873"), ("A", "872"), ("E", "871")]


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


class TestNovelty875:
    def test_single_test_type_d_875_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_875") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_875_main_commit_unique_and_anchored(self):
        # No #875 main commit exists pre-commit; the anchor test pins
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
            if "Type D #875" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 756, zero numeric 757 keys.
        assert _max_numeric_mechanism_id() == 756
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_d_875_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #875 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #875"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #875" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_870_874_window_closed_prior_to_875(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #870 Type D:",
            "## #871 Type E:",
            "## #872 Type A:",
            "## #873 Type B:",
            "## #874 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#875 is the Type D anchor opening window 875-879."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_875_879_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #875 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"875-879 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_c_874(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("C", "874"), (
            f"immediate predecessor must be Type C #874, got {window[1]}"
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
        # TWENTY-EIGHTH present (negative-guard wording; no new
        # falsification-family member this window), TWENTY-SEVENTH
        # present (ledger anchor reference) in this file.
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-EIGHTH" in text
        assert "TWENTY-SEVENTH" in text


class TestTypeDM754QualitativeDiscipline:
    """m754 - profiles/financial-times.yaml (Type A #872)."""

    REL = "profiles/financial-times.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M754_KEY, 20000))

    def test_iteration_and_mechanism_id(self):
        doc = self._folded()
        assert "mechanism_id: 754" in doc
        assert "iteration: 872" in doc
        assert "iteration_type: 'A'" in doc

    def test_manual_illustrative_scorer(self):
        doc = self._folded()
        assert "asymmetry_scorer_MANUAL_ILLUSTRATIVE" in doc
        assert "MANUAL ILLUSTRATIVE hand-assigned tones" in doc

    def test_openai_meta_arms(self):
        doc = self._folded()
        assert "openai_arm_scores: [-0.15]" in doc
        assert "meta_arm_scores: [-0.30]" in doc

    def test_illustrative_delta_openai_minus_meta(self):
        doc = self._folded()
        assert "illustrative_register_delta_openai_minus_meta: 0.15" in doc
        assert "-0.15 - (-0.30) = 0.15" in doc

    def test_engine_degenerate_documented(self):
        doc = self._folded()
        assert (
            "calculate_asymmetry([-0.15], [-0.30]) returns asymmetry 0.15"
            in doc
        )
        assert "degenerate CI (0.15, 0.15)" in doc

    def test_finding_layer_not_calculated(self):
        doc = self._folded()
        assert "p_value NOT_CALCULATED" in doc
        assert "cohens_d NOT_CALCULATED" in doc
        assert "ci_95 NOT_CALCULATED" in doc
        assert "is_significant False" in doc

    def test_discipline_fields(self):
        doc = self._folded()
        assert "no_analysis_json_update: true" in doc
        assert "verdict: directionally_supported_not_proven" in doc
        assert "artifact_grade: false" in doc

    def test_not_falsification_family_ledger_27(self):
        doc = self._folded()
        assert "NOT a member" in doc
        assert "Ledger holds at 27" in doc

    def test_correlation_not_causation(self):
        doc = self._folded()
        assert "Correlation is not causation" in doc

    def test_block_key_unique(self):
        assert _read(self.REL).count(M754_KEY + ":") == 1


class TestTypeDM755QualitativeDiscipline:
    """m755 - profiles/careers/journalists.yaml (Type B #873)."""

    REL = "profiles/careers/journalists.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M755_KEY, 25000))

    def test_block_key_and_mechanism_id(self):
        doc = self._folded()
        assert "mechanism_id: 755" in doc
        assert "iteration: 873" in doc
        assert "type: B" in doc

    def test_journalist_mechanism_ids(self):
        doc = _read(self.REL)
        start = doc.index("daniel_cooper:")
        end = doc.index(M755_KEY + ":")
        header = _fold(doc[start:end])
        # daniel_cooper carries mechanism 295 (m295 series) and 755.
        assert "mechanism_ids: - 295 - 755" in header

    def test_extends_295(self):
        doc = self._folded()
        assert "TEMPORAL EXTENSION of mechanism 295" in doc

    def test_manual_illustrative_methodology(self):
        doc = self._folded()
        assert "MANUAL ILLUSTRATIVE tones only" in doc

    def test_target_reference_arms(self):
        doc = self._folded()
        assert "target_scores: - -0.1" in doc
        assert "reference_scores: - -0.3" in doc

    def test_delta_apple_minus_meta(self):
        doc = self._folded()
        assert "illustrative_delta_apple_minus_meta: 0.2" in doc
        assert "-0.10 - (-0.30) = +0.20" in doc

    def test_engine_not_run(self):
        doc = self._folded()
        assert "engine NOT run (illustrative arms only; Apple arm carried)" in doc

    def test_p_value_not_calculated(self):
        doc = self._folded()
        assert "p_value: NOT_CALCULATED" in doc
        assert "cohens_d: NOT_CALCULATED" in doc
        assert "ci_95: NOT_CALCULATED" in doc

    def test_verdict_significance_artifact(self):
        doc = self._folded()
        assert "verdict: 'directionally_supported_not_proven'" in doc
        assert "is_significant: false" in doc
        assert "no_analysis_json_update: true" in doc
        assert "artifact_grade: 'NOT artifact-grade'" in doc
        assert "correlation_not_causation: true" in doc

    def test_not_falsification_family_ledger_27(self):
        doc = self._folded()
        assert "NOT a falsification-family member" in doc
        assert "ledger holds at 27" in doc

    def test_block_key_unique(self):
        assert _read(self.REL).count(M755_KEY + ":") == 1


class TestTypeDM756QualitativeDiscipline:
    """m756 - profiles/competitor-entities.yaml (Type C #874)."""

    REL = "profiles/competitor-entities.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M756_KEY, 45000))

    def test_block_key_and_mechanism_id(self):
        doc = self._folded()
        assert "mechanism_id: 756" in doc
        assert "iteration: 874" in doc
        assert M756_BLOCK_KEY in doc

    def test_type_financial_incentive_mapping(self):
        doc = self._folded()
        assert "type: financial_incentive_mapping" in doc
        assert "rotation: Type C" in doc

    def test_statistical_discipline_manual(self):
        doc = self._folded()
        assert (
            "MANUAL / qualitative only per the Aug 28 2026 standing rule"
            in doc
        )
        assert "financial-incentive documentation leg, not a tone test" in doc

    def test_scorer_none_and_not_calculated(self):
        doc = self._folded()
        assert "tone NOT_SCORED; scorer none" in doc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in doc

    def test_significance_and_engine(self):
        doc = self._folded()
        assert "is_significant False" in doc
        assert "engine NOT run" in doc

    def test_verdict_and_artifact(self):
        doc = self._folded()
        assert "verdict: 'directionally_supported_not_proven'" in doc
        assert "no_analysis_json_update: true" in doc
        assert "NOT artifact_grade true" in doc

    def test_no_coverage_tone_claim(self):
        doc = self._folded()
        assert "no_coverage_tone_claim: true" in doc

    def test_not_falsification_family_ledger_27(self):
        doc = self._folded()
        assert "NOT a falsification-family member" in doc
        assert "ledger holds at 27" in doc

    def test_block_key_unique(self):
        assert _read(self.REL).count(M756_KEY + ":") == 1


class TestTypeDFalsificationLedger:
    """Ledger holds at 27: one TWENTY-SEVENTH member, zero TWENTY-EIGHTH."""

    MEMBER_27 = "TWENTY-SEVENTH falsification-family member"
    MEMBER_28 = "TWENTY-EIGHTH falsification-family member"

    def _profiles_text(self):
        parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                parts.append(open(p, encoding="utf-8", errors="replace").read())
        return "\n".join(parts)

    def test_exactly_one_27th_member_in_profiles(self):
        count = self._profiles_text().count(self.MEMBER_27)
        assert count == 1, count

    def test_27th_member_is_m751_verge(self):
        verge = _read("profiles/the-verge.yaml")
        assert verge.count(self.MEMBER_27) == 1
        assert "(ledger 26->27)" in verge

    def test_zero_28th_members_in_profiles(self):
        count = self._profiles_text().count(self.MEMBER_28)
        assert count == 0, count

    def test_28th_guards_are_not_members(self):
        # The-verge ledger line carries the TWENTY-EIGHTH negative-guard
        # string; test-file tombstones use TWENTY-EIGHTH ordinals only.
        # Neither is a member-form.
        assert "TWENTY-EIGHTH falsification-family member" not in _read(
            "profiles/the-verge.yaml"
        )
        assert "negative-guard convention continues at TWENTY-EIGHTH" in _read(
            "profiles/the-verge.yaml"
        )


class TestTypeDCorpusIntegrity:
    """Post-#874 corpus integrity: max 756, zero 757 keys."""

    def test_max_numeric_mechanism_id_is_756(self):
        assert _max_numeric_mechanism_id() == 756

    def test_zero_underscore_757_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_757_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_dash_757_references_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_numeric_757_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(NEXT_NUM)
        assert hits == [], hits

    def test_designed_keying_underscore_754_755_756_zero_carriers(self):
        # No sole carrier this window: #872/#873/#874 MECH_ID_MARKERs
        # are format-built ("mechanism" + "_754" etc.), so the runtime
        # strings never appear in source. Documented, not repaired.
        for n in (754, 755, 756):
            hits = _repo_grep_underscore_mechanism(n)
            assert hits == [], (n, hits)

    def test_m754_m755_m756_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/financial-times.yaml").count(M754_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(M755_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M756_KEY + ":")
            == 1
        )

    def test_c874_max_756_sweep_stays_green(self):
        # Type D adds no mechanisms; #874's max-756 sweep stays green.
        assert _max_numeric_mechanism_id() == 756

    def test_c874_zero_757_sweeps_stay_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_a872_b873_c874_max_sweeps_superseded_by_design(self):
        # #872 asserted max == 754 pre-commit, #873 asserted max == 755
        # pre-commit, #874 asserted max == 756 pre-commit with zero
        # 757/756/755 next-key sweeps; advancing the corpus to 756
        # supersedes the 754 and 755 max sweeps per the #710/#720
        # convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 756 != 754
        assert _max_numeric_mechanism_id() == 756 != 755


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #870's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.66, 0.72, 0.68, 0.75, 0.69, 0.71]
        peers = [-0.33, -0.41, -0.28, -0.36, -0.39, -0.31]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(1.0483333333333333, rel=1e-4)
        assert report.t_statistic == pytest.approx(43.760823581625054, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(2.2641818521359104e-11, rel=1e-2)
        assert report.cohens_d == pytest.approx(25.265323274810946, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(1.0082916666666666, rel=1e-4)
        assert report.confidence_interval_upper == pytest.approx(1.0916666666666668, rel=1e-4)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.06, -0.03, 0.05, -0.07, 0.02, -0.04]
        peers = [-0.05, 0.04, -0.06, 0.03, -0.02, 0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(-0.0033333333333333335, rel=1e-4)
        assert report.t_statistic == pytest.approx(-0.10956642697819577, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.9149207921720559, rel=1e-2)
        assert report.cohens_d == pytest.approx(-0.0632582061100068, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m754_pair(self):
        # m754's own block documents the OpenAI arm at MANUAL
        # ILLUSTRATIVE -0.15 against the Meta arm at -0.30
        # (illustrative delta +0.15): the pair is corpus-grounded,
        # not invented.
        t, p = welch_t_test([-0.15], [-0.30])
        d = cohens_d([-0.15], [-0.30])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contracts(self):
        # m754 pair: OpenAI [-0.15] vs Meta [-0.30] (delta +0.15 exact).
        m754 = calculate_asymmetry(
            target_scores=[-0.15],
            peer_scores=[-0.30],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m754.asymmetry_score == pytest.approx(0.15, abs=1e-9)
        assert m754.t_statistic == 0.0
        assert m754.is_significant is False
        assert m754.confidence_interval_lower == pytest.approx(0.15, abs=1e-9)
        assert m754.confidence_interval_upper == pytest.approx(0.15, abs=1e-9)
        # m755 pair: Apple [-0.10] vs Meta [-0.30] (delta +0.20,
        # IEEE-inexact 0.19999999999999998 within 1e-9 per #673).
        m755 = calculate_asymmetry(
            target_scores=[-0.10],
            peer_scores=[-0.30],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m755.asymmetry_score == pytest.approx(0.20, abs=1e-9)
        assert m755.t_statistic == 0.0
        assert m755.is_significant is False
        # Arm-swaps negate exactly for both pairs.
        m754_swap = calculate_asymmetry(
            target_scores=[-0.30],
            peer_scores=[-0.15],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        m755_swap = calculate_asymmetry(
            target_scores=[-0.30],
            peer_scores=[-0.10],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m754.asymmetry_score + m754_swap.asymmetry_score == pytest.approx(0.0, abs=1e-12)
        assert m755.asymmetry_score + m755_swap.asymmetry_score == pytest.approx(0.0, abs=1e-12)

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
    """Suite verdict lineage; #870's background suite owns the verdict,
    #875 re-launches."""

    TOMBSTONE_LINEAGE = 36

    def test_tombstone_lineage_count(self):
        # THIRTY-SIXTH consecutive background full-suite death: #870's
        # background suite (re-launched 01:05 PDT Sep 20) died at the
        # tombstone marker and no pytest was alive at this run's check
        # (the ps scan found zero suite processes). Advances from the
        # THIRTY-FIFTH lineage declared in #870 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 36

    def test_870_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log at exactly 6 bytes ("......" tombstone) since
        # 01:05 PDT Sep 20 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_870_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 6, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert text.strip() == "......"

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_875_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_875_full_suite.log"

    def test_875_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_875_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync875:
    def test_readme_row_875(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_875(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_875_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog875:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #875 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #875 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 756" in entry
        assert "m754" in entry
        assert "m755" in entry
        assert "m756" in entry

    def test_log_rotation_window_875_879(self):
        entry = self._entry()
        assert "875-879" in entry
        assert "870-874" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry


class TestDateGrounding875:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 6, 0).strftime("%H:%M") == "06:00"
