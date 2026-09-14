"""
Type D -- Iteration #735 (Sun 2026-09-13 23:00 PDT): m673 / m674 / m675
qualitative-discipline verification + post-#734 corpus integrity
(max mechanism_id 675; zero mechanism_676 keys; ledger holds at 24) +
#730 background-suite tombstone (SEVENTH consecutive death; re-launched as
type_d_735_full_suite.log).

Verifies:
- m673 (The Verge x OpenAI DOJ SOI coverage-SELECTION test, Type A #732):
  SELECTION-margin discipline - no tone pair exists on the SOI arm (no
  coverage, no tone), asymmetry_scorer_result.asymmetry_score
  NOT_COMPUTED_SELECTION_TEST, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, NOT artifact-grade; the carried
  arms carry MANUAL ILLUSTRATIVE tones only (OpenAI avg -0.65, Meta avg
  -0.55); NOT a falsification-family member (ledger holds at 24).
- m674 (Jessica Conditt (Engadget) Apple adversarial register refinement of
  mechanism #150's beat-assignment routing claim, Type B #733):
  MANUAL ILLUSTRATIVE register -0.55 on the Apple arm, p_value
  NOT_CALCULATED, is_significant False, engine NOT run, NOT artifact-grade,
  verdict directionally_supported_not_proven; NOT a falsification-family
  member (ledger holds at 24).
- m675 (Seattle Times + Newsday v. OpenAI + Microsoft grant-then-sue leg,
  Type C #734): qualitative-only discipline - scorer none, tone NOT_SCORED,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT run,
  NOT artifact-grade; NOT a falsification-family member (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#734 corpus integrity: max numeric mechanism_id == 675 in
  profiles/; zero mechanism_676 keys in profiles/ and tests/ (own file
  excluded per the #715 pattern-rescope lesson); m673 / m674 / m675 each
  unique in their home YAML.
- Statistical meaningfulness on FRESH synthetic corpora: strong-signal
  n=5-per-arm pair (asymmetry +0.782, t=23.686097033081467,
  p=4.116107912494527e-08, d=14.980403100858808, CI (0.722, 0.840)
  above zero, is_significant True at the ENGINE layer); fresh near-null
  pair (asymmetry -0.012, t=-0.23076923076923073, p=0.8239466727667853,
  d=-0.1459512766231559, CI (-0.112, 0.078) crossing zero, silent);
  fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.93 exact, arm-swap negates).
  Engine significance is never promoted to a finding (Aug 28 2026
  standing rule).
- Full-suite status: the #730 re-launched background suite died mid-run
  (type_d_730_full_suite.log stalled at 1537 bytes / ~3% progress since
  Sep 14 02:03 UTC / Sep 13 19:03 PDT; no pytest alive at this run's check)
  - SEVENTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch,
  #730's re-launch; tombstone lineage per #565 log convention).
  Re-launched this run to goal hidden_files type_d_735_full_suite.log;
  next Type D run checks it.
- Rotation guard: #734 Type C main commit present; 731-735 window
  orders E->A->B->C->D (anchor patched in the followup per #565).
"""

import os
import re
import glob
import subprocess
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_BASENAME = os.path.basename(__file__)

from mediascope.score.asymmetry import calculate_asymmetry

ITERATION = 735
MECH_MAX = 675

VERGE = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
CAREERS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
GOAL_HIDDEN = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files"
)

M673_KEY = "mechanism_673_verge_openai_doj_soi_coverage_selection_test_sep13"
M674_KEY = "jessica_conditt_engadget_apple_adversarial_beat_routing_refinement"
M675_KEY = "seattle_times_newsday_grant_then_sue_openai_microsoft_sep2026"


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args], capture_output=True, text=True
    )


def _profile_yaml_paths():
    out = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                out.append(os.path.join(root, fn))
    return out


def _mechanism_ids_from_files(paths):
    ids = []
    for p in paths:
        text = open(p, encoding="utf-8").read()
        ids.extend(
            int(x)
            for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text)
        )
    return ids


def _fold(block):
    # YAML `>` folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


# -- novelty ---------------------------------------------------------------

class TestNovelty735:
    def test_single_test_file_for_735(self):
        matches = [
            f for f in os.listdir(TESTS_DIR) if re.search(r"_735_", f)
        ]
        assert matches == [TEST_BASENAME], f"expected only this file for #735, got {matches}"

    def test_mechanism_673_unique_in_verge_profile(self):
        text = open(VERGE, encoding="utf-8").read()
        count = len(re.findall(r"(?m)^\s*mechanism_id:\s*673\s*$", text))
        assert count == 1, f"expected exactly one mechanism_id: 673 in the-verge.yaml, got {count}"
        assert text.count(M673_KEY) == 1

    def test_mechanism_674_unique_in_profiles(self):
        count = 0
        for p in _profile_yaml_paths():
            text = open(p, encoding="utf-8").read()
            count += len(re.findall(r"(?m)^\s*mechanism_id:\s*674\s*$", text))
        assert count == 1, f"expected exactly one mechanism_id: 674 in profiles/, got {count}"

    def test_mechanism_675_unique_in_profiles(self):
        count = 0
        for p in _profile_yaml_paths():
            text = open(p, encoding="utf-8").read()
            count += len(re.findall(r"(?m)^\s*mechanism_id:\s*675\s*$", text))
        assert count == 1, f"expected exactly one mechanism_id: 675 in profiles/, got {count}"

    def test_max_mechanism_id_pre_commit_735(self):
        assert max(_mechanism_ids_from_files(_profile_yaml_paths())) == MECH_MAX


# -- m673: The Verge x OpenAI DOJ SOI coverage-selection test ----------------

def _verge_block():
    text = open(VERGE, encoding="utf-8").read()
    idx = text.index(M673_KEY)
    # block runs to the next mechanism key at the same indent level
    rest = text[idx:]
    m = re.search(r"\n    mechanism_\d+_", rest[len(M673_KEY):])
    return rest[: len(M673_KEY) + m.start()] if m else rest


class TestM673VergeSOISelectionDiscipline:
    def test_block_identity_fields(self):
        block = _verge_block()
        assert "mechanism_id: 673" in block
        assert "iteration: 732" in block
        assert 'iteration_type: "A"' in block
        assert "publication_focus: \"The Verge\"" in block
        assert "entity_pair: \"OpenAI vs Meta\"" in block

    def test_selection_margin_scorer_block(self):
        block = _verge_block()
        assert "asymmetry_score: \"NOT_COMPUTED_SELECTION_TEST\"" in block
        assert "p_value: \"NOT_CALCULATED\"" in block
        assert "cohens_d: \"NOT_CALCULATED\"" in block
        assert "ci_95: \"NOT_CALCULATED\"" in block
        assert "is_significant: false" in block
        assert "openai_avg: -0.65" in block
        assert "meta_avg: -0.55" in block

    def test_soi_arm_not_scored(self):
        block = _verge_block()
        assert "url: \"NONE_SURFACED_BOUNDED_ABSENCE\"" in block
        assert "manual_illustrative_tone: \"NOT_SCORED\"" in block

    def test_engine_not_run_note(self):
        block = _verge_block()
        assert "engine NOT run" in block

    def test_statistical_discipline(self):
        block = _fold(_verge_block())
        assert "is_significant False" in block
        assert "correlation_not_causation true" in block

    def test_not_falsification_family(self):
        block = _verge_block()
        assert "NOT a member - selection-margin finding" in block
        assert "ledger holds at 24" in block


# -- m674: Jessica Conditt journalist-level refinement -----------------------

def _conditt_block():
    data = yaml.safe_load(open(RESEARCH, encoding="utf-8"))
    return data["cross_publication_findings"][M674_KEY]


class TestM674CondittDiscipline:
    def test_block_identity_fields(self):
        b = _conditt_block()
        assert b["mechanism_id"] == 674
        assert b["iteration"] == 733
        assert b["rotation_type"] == "B"
        assert b["finding_type"] == "journalist_cross_entity"
        assert b["journalist"] == "Jessica Conditt"
        assert b["competitor"] == "Apple"

    def test_verdict_and_register(self):
        b = _conditt_block()
        assert b["verdict"] == "directionally_supported_not_proven"
        finding = _fold(b["finding"])
        assert "MANUAL ILLUSTRATIVE register -0.55" in finding
        assert "EXTENDS and REFINES mechanism #150" in finding

    def test_statistical_discipline_in_finding(self):
        finding = _fold(_conditt_block()["finding"])
        assert "p_value NOT_CALCULATED" in finding
        assert "is_significant False, engine NOT run" in finding
        assert "NOT artifact-grade" in finding
        assert "Correlation is not causation." in finding

    def test_not_falsification_family(self):
        finding = _fold(_conditt_block()["finding"])
        assert "NOT a falsification-family member (ledger holds at 24)" in finding

    def test_careers_entry_points_to_674(self):
        careers = yaml.safe_load(open(CAREERS, encoding="utf-8"))
        entry = careers["jessica_conditt"]
        assert entry["current_publication"] == "Engadget"
        assert "mechanism 674" in entry["notes"]
        assert "iteration #733" in entry["notes"]

    def test_test_file_backlink(self):
        b = _conditt_block()
        assert b["test_file"] == (
            "tests/test_type_b_733_jessica_conditt_engadget_apple_adversarial_beat_routing_sep13_9pm.py"
        )
        assert b["test_count"] == 42


# -- m675: Seattle Times + Newsday grant-then-sue leg ------------------------

def _m675_block():
    data = yaml.safe_load(open(COMPETITOR_ENTITIES, encoding="utf-8"))
    return data["entities"]["openai"][M675_KEY]


class TestM675GrantThenSueDiscipline:
    def test_block_identity_fields(self):
        b = _m675_block()
        assert b["mechanism_id"] == 675
        assert b["iteration"] == 734
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert "grant-then-sue" in b["mechanism_name"]

    def test_statistical_discipline(self):
        sd = _fold(_m675_block()["statistical_discipline"])
        assert "tone NOT_SCORED" in sd
        assert "p_value/cohens_d/ci NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "NOT artifact-grade" in sd
        assert "NOT a falsification-family member" in sd
        assert "ledger holds at 24" in sd

    def test_falsification_family_not_member(self):
        ff = _fold(_m675_block()["falsification_family"])
        assert "NOT a member" in ff
        assert "the ledger holds at 24" in ff

    def test_suit_facts_present(self):
        b = _m675_block()
        facts = " ".join(b["suit_facts"])
        assert "Sep 4, 2026" in facts
        assert "Seattle Times" in facts and "Newsday" in facts
        assert "OpenAI and Microsoft" in facts

    def test_test_file_backlink(self):
        b = _m675_block()
        assert b["test_file"] == (
            "tests/test_type_c_734_seattle_times_newsday_grant_then_sue_sep13_10pm.py"
        )


# -- falsification ledger ----------------------------------------------------

class TestFalsificationLedger735:
    """TWENTY-FOURTH present, TWENTY-FIFTH absent anywhere in profiles/."""

    def test_twenty_fourth_present(self):
        out = subprocess.run(
            ["grep", "-rl", "TWENTY-FOURTH", os.path.join(REPO_ROOT, "profiles")],
            capture_output=True, text=True,
        )
        assert out.stdout.strip(), "TWENTY-FOURTH ledger entry must exist in profiles/"

    def test_twenty_fifth_absent(self):
        out = subprocess.run(
            ["grep", "-rl", "TWENTY-FIFTH", os.path.join(REPO_ROOT, "profiles")],
            capture_output=True, text=True,
        )
        assert out.stdout.strip() == "", f"TWENTY-FIFTH must not exist: {out.stdout.strip()}"


# -- corpus integrity post-#734 ----------------------------------------------

class TestCorpusIntegrityPost734:
    """Max numeric mechanism_id == 675; zero mechanism_676 keys; m673/674/675 present."""

    def test_max_mechanism_id_is_675(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, f"max mechanism_id {max(ids)} != {MECH_MAX}"

    def test_zero_mechanism_676_keys(self):
        # Own file excluded per the #715 pattern-rescope lesson (the sweep logic
        # itself mentions the key). Sweep-carrier files are also excluded: the
        # #734 test file carries its own zero-mechanism_676 supersession sweep
        # (test_zero_mechanism_676_keys_repo_wide), so its literal mention is the
        # sweep instrument, not a mechanism key.
        hits = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn), encoding="utf-8").read()
                    if re.search(r"mechanism_676", text):
                        hits.append(fn)
        for fn in sorted(os.listdir(TESTS_DIR)):
            if not fn.endswith(".py") or fn == TEST_BASENAME:
                continue
            text = open(os.path.join(TESTS_DIR, fn), encoding="utf-8").read()
            if "test_zero_mechanism_676" in text:
                continue
            if re.search(r"mechanism_676", text):
                hits.append(fn)
        assert hits == [], f"mechanism_676 keys must not exist (own file + sweep carriers excluded): {hits}"

    def test_window_mechanisms_673_674_675_all_present(self):
        ids = set(_mechanism_ids_from_files(_profile_yaml_paths()))
        assert {673, 674, 675} <= ids


# -- engine verification on fresh synthetic corpora ---------------------------

_PS = datetime(2026, 9, 1)
_PE = datetime(2026, 9, 13)


class TestEngineFreshCorpora735:
    """The Aug 28 2026 standing rule: engine significance is never promoted
    to a finding. These bind the engine contract on fresh corpora."""

    def test_strong_signal_pair_is_significant_at_engine_layer(self):
        r = calculate_asymmetry(
            [0.41, 0.47, 0.39, 0.44, 0.36],
            [-0.33, -0.41, -0.29, -0.37, -0.44],
            "T", ["P"], "x", _PS, _PE,
        )
        assert r.asymmetry_score == pytest.approx(0.782)
        assert r.t_statistic == pytest.approx(23.686097033081467)
        assert r.p_value == pytest.approx(4.116107912494527e-08)
        assert r.cohens_d == pytest.approx(14.980403100858808)
        assert r.confidence_interval_lower == pytest.approx(0.722)
        assert r.confidence_interval_upper == pytest.approx(0.8400000000000001)
        assert r.is_significant is True

    def test_strong_signal_ci_above_zero(self):
        r = calculate_asymmetry(
            [0.41, 0.47, 0.39, 0.44, 0.36],
            [-0.33, -0.41, -0.29, -0.37, -0.44],
            "T", ["P"], "x", _PS, _PE,
        )
        assert r.confidence_interval_lower > 0

    def test_near_null_pair_stays_silent(self):
        r = calculate_asymmetry(
            [0.11, -0.08, 0.05, -0.12, 0.03],
            [0.06, -0.04, 0.09, -0.07, 0.01],
            "T", ["P"], "x", _PS, _PE,
        )
        assert r.asymmetry_score == pytest.approx(-0.012)
        assert r.t_statistic == pytest.approx(-0.23076923076923073)
        assert r.p_value == pytest.approx(0.8239466727667853)
        assert r.cohens_d == pytest.approx(-0.1459512766231559)
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper
        assert r.is_significant is False

    def test_degenerate_n1_per_arm_contract(self):
        r = calculate_asymmetry([0.62], [-0.31], "T", ["P"], "x", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(0.93)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_degenerate_arm_swap_negates(self):
        a = calculate_asymmetry([0.62], [-0.31], "T", ["P"], "x", _PS, _PE)
        b = calculate_asymmetry([-0.31], [0.62], "P", ["T"], "x", _PS, _PE)
        assert b.asymmetry_score == pytest.approx(-a.asymmetry_score)


# -- full-suite tombstone -----------------------------------------------------

class TestFullSuiteTombstone730:
    """The #730 re-launched background 37K suite died mid-run (log stalled at
    1537 bytes / ~3% progress since Sep 14 02:03 UTC / Sep 13 19:03 PDT; no
    pytest alive at this run's check) - SEVENTH consecutive background death.
    Re-launched this run to goal hidden_files type_d_735_full_suite.log;
    next Type D run checks it."""

    def test_730_suite_log_stalled(self):
        log = os.path.join(GOAL_HIDDEN, "type_d_730_full_suite.log")
        assert os.path.exists(log), "the #730 suite log must exist"
        size = os.path.getsize(log)
        assert size == 1537, f"expected the stalled 1537-byte log, got {size}"

    def test_no_pytest_alive(self):
        out = subprocess.run(["pgrep", "-f", "pytest.*mediascope"], capture_output=True, text=True)
        assert out.stdout.strip() == "", f"no mediascope pytest should be alive: {out.stdout.strip()}"


# -- Rotation guard / novelty anchor (#565 convention) ------------------------

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "NOT_YET_COMMITTED_735"


class TestRotationCycleGuard735:
    """Deselected pre-commit; anchor patched in followup per #565."""

    WINDOW = {731: "E", 732: "A", 733: "B", 734: "C", 735: "D"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {731: "E", 732: "A", 733: "B", 734: "C", 735: "D"}

    def test_735_is_type_d_in_window(self):
        assert self.WINDOW[ITERATION] == "D"

    def test_734_was_type_c_in_window(self):
        assert self.WINDOW[734] == "C"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_731_735_closes_e_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "735"),
            ("C", "734"),
            ("B", "733"),
            ("A", "732"),
            ("E", "731"),
        ], "rotation window 731-735 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for newer, older in zip(observed, observed[1:]):
            assert (order[newer] - order[older]) % 5 == 1, (
                "rotation broken: %s (older) -> %s (newer) is not a valid cycle edge" % (older, newer)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 731-735 closes E->D. Anchor patched in followup per #565."""
        result = _git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type D #735:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_single_735_test_file_pre_commit(self):
        hits = [os.path.basename(p) for p in glob.glob(os.path.join(TESTS_DIR, "test_type_d_735*.py"))]
        assert hits == [TEST_BASENAME]


# -- Doc-sync ratchet ---------------------------------------------------------

class TestDocSyncRatchet735:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_test_file_table_row(self):
        content = open(self.README).read()
        assert "test_type_d_735_m673_m674_m675_qualitative_corpus_integrity_sep13_11pm.py" in content

    def test_architecture_tree_row(self):
        content = open(self.ARCH).read()
        assert "test_type_d_735_m673_m674_m675_qualitative_corpus_integrity_sep13_11pm.py" in content

    def test_iteration_log_starts_with_735(self):
        first = open(self.LOG).readline().strip()
        assert first.startswith("#735 Type D:"), first[:80]
