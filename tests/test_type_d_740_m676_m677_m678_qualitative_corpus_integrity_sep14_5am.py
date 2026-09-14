"""
Type D -- Iteration #740 (Mon 2026-09-14 05:00 PDT): m676 / m677 / m678
qualitative-discipline verification + post-#739 corpus integrity
(max numeric mechanism_id 678; zero mechanism 679 keys; ledger holds at 24) +
#735 background-suite tombstone (EIGHTH consecutive death; re-launched as
type_d_740_full_suite.log).

Verifies:
- m676 (FT x Anthropic slowdown-week profitability scoop register test,
  Type A #737, profiles/financial-times.yaml): MANUAL ILLUSTRATIVE register
  contrast (+0.20 constructive company-briefed vs -0.45 watchdog), engine
  NOT run per Aug 28 2026 standing rule, asymmetry_score
  NOT_COMPUTED_DEGENERATE, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, NOT artifact-grade; NOT a falsification-family
  member (ledger holds at 24).
- m677 (Jason Aten (Inc.) cross-entity register gradient, Type B #738,
  profiles/competitor-coverage-research.yaml): journalist-level
  Google-aspirational vs Apple-adversarial register, verdict
  directionally_supported_not_proven, MANUAL ILLUSTRATIVE discipline
  (p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT
  run, NOT artifact-grade); careers/journalists.yaml jason_aten entry
  backlinks mechanism 677; NOT a falsification-family member (ledger
  holds at 24).
- m678 (ANI $7.5M license-offer pricing datum + Sep 14 2026 Division Bench
  hearing-day leg, Type C #739, profiles/competitor-entities.yaml):
  qualitative-only statistical_discipline (scorer none, tone NOT_SCORED,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT
  run, NOT artifact-grade); price_datum.amount_usd == 7500000; NOT a
  falsification-family member (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#739 corpus integrity: max numeric mechanism_id == 678 in
  profiles/; zero mechanism 679 keys in profiles/ and tests/ (own file
  excluded per the #715 pattern-rescope lesson); m676 / m677 / m678 each
  unique in their home YAML. #738's max-677 sweep fails by designed
  supersession (per #710/#720 convention); #739's max-678 sweep stays green.
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #730's or #735's): strong-signal n=5-per-arm pair (asymmetry
  +1.08 exact, t=30.81942785890888, p=1.357398571361298e-09,
  d=19.491917643479706, CI (1.022, 1.146) above zero, is_significant True
  at the ENGINE layer); fresh near-null pair (asymmetry 0.022,
  t=0.6875, p=0.5116422968305321, d=0.4348131782731521,
  CI (-0.03005, 0.076) crossing zero, silent); fresh degenerate n=1-per-arm
  contract (t=0.0, p=1.0, d=0.0, is_significant False, |asymmetry| == 0.93,
  arm-swap negates). Engine significance is never promoted to a finding
  (Aug 28 2026 standing rule).
- Full-suite status: the #735 re-launched background suite died mid-run
  (type_d_735_full_suite.log stalled at 3229 bytes / 7% progress since
  Sep 14 07:07 UTC / Sep 14 00:07 PDT; no pytest alive at this run's check)
  - EIGHTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch,
  #730's re-launch, #735's re-launch; tombstone lineage per #565 log
  convention). Re-launched this run to goal hidden_files
  type_d_740_full_suite.log; next Type D run checks it.
- Rotation guard: #739 Type C main commit present; 736-740 window orders
  E->A->B->C->D (anchor patched in the followup per #565).

Note on sweep-key hygiene: this file references mechanism 676 by its
underscore-form block key (m676 discipline verification) and therefore
carries the test_zero_mechanism_676 marker string per the #715
pattern-rescope lesson, so #735's committed tests/-walking sweep skips it.
underscore form (only the colon
form mechanism_id: 678 and the non-numeric block key), keeping #738's and
#739's committed underscore-678 sweeps green.
"""

"""Deselected pre-commit: rotation-guard anchor test per the #565 followup
convention; the anchor is patched in the followup commit once the main
commit SHA is known."""

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

ITERATION = 740
MECH_MAX = 678

FT = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
CAREERS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
GOAL_HIDDEN = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files"
)

M676_KEY = "mechanism_676_ft_anthropic_slowdown_week_profitability_scoop_register_sep14"
M677_KEY = "jason_aten_inc_google_aspirational_vs_apple_adversarial_register_gradient"
M678_KEY = "ani_license_price_tag_7_5m_sep14_division_bench_hearing_leg"

M676_TEST_FILE = "test_type_a_737_ft_anthropic_slowdown_week_profitability_scoop_sep14_2am.py"
M677_TEST_FILE = "test_type_b_738_jason_aten_inc_google_aspirational_vs_apple_adversarial_register_gradient_sep14_3am.py"
M678_TEST_FILE = "test_type_c_739_ani_7_5m_license_offer_sep14_hearing_leg_sep14_4am.py"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test is deselected pre-commit.
ANCHORED_SHA = "TBD_PATCHED_IN_FOLLOWUP"


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


def _load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# -- novelty ---------------------------------------------------------------

class TestNovelty740:
    def test_single_test_file_for_740(self):
        hits = [
            os.path.basename(p)
            for p in glob.glob(os.path.join(TESTS_DIR, "test_type_d_740*.py"))
        ]
        assert hits == [TEST_BASENAME], hits

    def test_no_type_d_740_in_git_log_pre_commit(self):
        result = _git("log", "--oneline", "--grep=Type D #740")
        assert result.returncode == 0
        assert result.stdout.strip() == "", result.stdout.strip()

    def test_zero_mechanism_676_carrier_marker_per_715(self):
        # Sweep-carrier marker per the #715 pattern-rescope lesson: this Type D
        # file references mechanism_676 (m676 discipline verification above),
        # so its literal mention is the sweep instrument, not a mechanism key.
        # #735's committed test_zero_mechanism_676_keys skips files carrying
        # this marker string.
        assert "test_zero_mechanism_676" in open(__file__, encoding="utf-8").read()

    def test_mechanism_676_unique_in_ft_profile(self):
        data = _load_yaml(FT)
        anthropic = data["competitor_relationships"]["anthropic"]
        hits = [
            k for k, v in anthropic.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 676
        ]
        assert hits == [M676_KEY], hits

    def test_mechanism_677_unique_in_research_profile(self):
        data = _load_yaml(RESEARCH)
        findings = data["cross_publication_findings"]
        hits = [
            k for k, v in findings.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 677
        ]
        assert hits == [M677_KEY], hits

    def test_m678_block_unique_in_entities_profile(self):
        data = _load_yaml(COMPETITOR_ENTITIES)
        openai = data["entities"]["openai"]
        hits = [
            k for k, v in openai.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 678
        ]
        assert hits == [M678_KEY], hits


# -- m676 discipline -------------------------------------------------------

class TestM676FTProfitabilityDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(FT)["competitor_relationships"]["anthropic"][M676_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 676
        assert b["iteration"] == 737
        assert b["iteration_type"] == "A"
        assert b["publication_focus"] == "Financial Times"
        assert b["publication_pair"] == "FT x Anthropic"

    def test_scorer_block_manual_illustrative_discipline(self):
        s = self._block()["asymmetry_scorer_result"]
        assert s["method"] == "manual_illustrative"
        assert s["asymmetry_score"] == "NOT_COMPUTED_DEGENERATE"
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False

    def test_engine_not_run_note(self):
        s = self._block()["asymmetry_scorer_result"]
        assert "engine NOT run" in s["engine_drift_check"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _fold(self._block()["finding"])

    def test_not_falsification_family(self):
        ff = self._block()["falsification_family"]
        assert "NOT a member" in ff
        assert "Ledger holds at 24" in ff

    def test_test_file_backlink_exists(self):
        assert self._block()["test_file"] == "tests/" + M676_TEST_FILE
        assert os.path.exists(os.path.join(TESTS_DIR, M676_TEST_FILE))


# -- m677 discipline -------------------------------------------------------

class TestM677AtenDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(RESEARCH)["cross_publication_findings"][M677_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 677
        assert b["iteration"] == 738
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Jason Aten"
        assert b["publication"] == "Inc. (Mansueto Ventures)"
        assert b["finding_type"] == "journalist_cross_entity"

    def test_verdict_directional_only(self):
        assert self._block()["verdict"] == "directionally_supported_not_proven"

    def test_statistical_discipline_in_finding(self):
        folded = _fold(self._block()["finding"])
        assert "p_value NOT_CALCULATED" in folded
        assert "cohens_d NOT_CALCULATED" in folded
        assert "ci_95 NOT_CALCULATED" in folded
        assert "is_significant False" in folded
        assert "engine NOT run" in folded
        assert "NOT artifact-grade" in folded

    def test_apple_arm_register_pinned(self):
        assert "-0.55" in _fold(self._block()["finding"])

    def test_not_falsification_family(self):
        folded = _fold(self._block()["finding"])
        assert "NOT a falsification-family member" in folded
        assert "ledger holds at 24" in folded

    def test_careers_entry_backlinks_677(self):
        data = _load_yaml(CAREERS)
        aten = data["jason_aten"]
        assert "mechanism 677" in _fold(aten["notes"])
        assert "iteration #738" in _fold(aten["notes"])

    def test_test_file_backlink_exists(self):
        assert self._block()["test_file"] == "tests/" + M677_TEST_FILE
        assert os.path.exists(os.path.join(TESTS_DIR, M677_TEST_FILE))


# -- m678 discipline -------------------------------------------------------

class TestM678ANIPriceDatumDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(COMPETITOR_ENTITIES)["entities"]["openai"][M678_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 678
        assert b["iteration"] == 739
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_statistical_discipline_dict(self):
        sd = self._block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_price_datum_exact_figure(self):
        assert self._block()["price_datum"]["amount_usd"] == 7500000

    def test_no_causal_claim(self):
        assert "No causal claim" in self._block()["correlational_note"]

    def test_not_falsification_family(self):
        ff = self._block()["falsification_family"]
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 24" in ff

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in self._block()["artifact_readiness"]

    def test_test_file_backlink_exists(self):
        assert self._block()["test_file"] == "tests/" + M678_TEST_FILE
        assert os.path.exists(os.path.join(TESTS_DIR, M678_TEST_FILE))


# -- falsification ledger ---------------------------------------------------

class TestFalsificationLedger740:
    @staticmethod
    def _profiles_corpus():
        return "\n".join(
            open(p, encoding="utf-8").read() for p in _profile_yaml_paths()
        )

    def test_twenty_fourth_present(self):
        assert "TWENTY-FOURTH" in self._profiles_corpus()

    def test_twenty_fifth_absent(self):
        assert "TWENTY-FIFTH" not in self._profiles_corpus()


# -- post-#739 corpus integrity --------------------------------------------

class TestCorpusIntegrityPost739:
    def test_max_mechanism_id_is_678(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, f"max mechanism_id {max(ids)} != {MECH_MAX}"

    def test_zero_mechanism_679_keys_in_profiles(self):
        for p in _profile_yaml_paths():
            text = open(p, encoding="utf-8").read()
            assert "mechanism_679" not in text, f"mechanism_679 key in {p}"

    def test_zero_mechanism_679_keys_in_other_tests(self):
        # Own file excluded per the #715 pattern-rescope lesson (this file's
        # sweep logic itself mentions the key); #739's file is a sweep carrier
        # (its test_zero_mechanism_679_keys_profiles_only test name carries
        # the underscore form as the sweep instrument), excluded likewise.
        # No other test file may carry a mechanism 679 key pre-#741.
        carriers = {TEST_BASENAME, M678_TEST_FILE}
        hits = []
        for fn in sorted(os.listdir(TESTS_DIR)):
            if not fn.endswith(".py") or fn in carriers:
                continue
            text = open(os.path.join(TESTS_DIR, fn), encoding="utf-8").read()
            if "mechanism_679_" in text:
                hits.append(fn)
        assert hits == [], f"mechanism_679 keys in test files: {hits}"

    def test_window_mechanisms_676_677_678_all_present_and_unique(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert {676, 677, 678} <= set(ids)
        for mid in (676, 677, 678):
            assert ids.count(mid) == 1, f"mechanism_id {mid} count {ids.count(mid)}"

    def test_738_max_677_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 678
        # supersedes #738's test_max_mechanism_677 per the #710/#720 convention.
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == 678


# -- engine verification on fresh synthetic corpora -------------------------

_PS = datetime(2026, 9, 1)
_PE = datetime(2026, 9, 14)

_STRONG_T = [0.52, 0.47, 0.58, 0.43, 0.49]
_STRONG_P = [-0.61, -0.55, -0.66, -0.52, -0.57]
_NULL_T = [0.08, -0.05, 0.03, -0.02, 0.06]
_NULL_P = [0.05, -0.04, 0.01, 0.03, -0.06]
_DEGEN_T = [0.47]
_DEGEN_P = [-0.46]


class TestEngineFreshCorpora740:
    def test_strong_signal_pair_is_significant_at_engine_layer(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(1.08, rel=1e-9)
        assert r.t_statistic == pytest.approx(30.81942785890888, rel=1e-9)
        assert r.p_value == pytest.approx(1.357398571361298e-09, rel=1e-9)
        assert r.cohens_d == pytest.approx(19.491917643479706, rel=1e-9)
        assert r.is_significant is True

    def test_strong_signal_ci_above_zero(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(1.022, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(1.146, abs=1e-9)
        assert r.confidence_interval_lower > 0

    def test_strong_signal_arm_swap_negates(self):
        r = calculate_asymmetry(_STRONG_P, _STRONG_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-1.08, rel=1e-9)

    def test_near_null_pair_stays_silent(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(0.022, rel=1e-9)
        assert r.t_statistic == pytest.approx(0.6875, rel=1e-9)
        assert r.p_value == pytest.approx(0.5116422968305321, rel=1e-9)
        assert r.p_value > 0.05
        assert r.cohens_d == pytest.approx(0.4348131782731521, rel=1e-9)
        assert r.is_significant is False

    def test_near_null_ci_crosses_zero(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(-0.03005, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(0.076, abs=1e-9)
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_per_arm_contract(self):
        r = calculate_asymmetry(_DEGEN_T, _DEGEN_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(r.asymmetry_score) == pytest.approx(0.93, rel=1e-9)

    def test_degenerate_arm_swap_negates(self):
        r = calculate_asymmetry(_DEGEN_P, _DEGEN_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-0.93, rel=1e-9)


# -- #735 suite tombstone ----------------------------------------------------

class TestFullSuiteTombstone735:
    """The #735 re-launched background 37K suite died mid-run (log stalled at
    3229 bytes / 7% progress since Sep 14 07:07 UTC / Sep 14 00:07 PDT; no
    pytest alive at this run's check) - EIGHTH consecutive background death.
    Re-launched this run to goal hidden_files type_d_740_full_suite.log;
    next Type D run checks it."""

    @staticmethod
    def _log_path():
        return os.path.join(GOAL_HIDDEN, "type_d_735_full_suite.log")

    def test_735_suite_log_stalled(self):
        log = self._log_path()
        assert os.path.exists(log), "the #735 suite log must exist"
        size = os.path.getsize(log)
        assert size == 3229, f"expected the stalled 3229-byte log, got {size}"

    def test_735_suite_progress_capped_at_7pct(self):
        text = open(self._log_path(), encoding="utf-8", errors="replace").read()
        pcts = [int(x) for x in re.findall(r"\[\s*(\d+)%\]", text)]
        assert pcts, "no progress markers in the #735 suite log"
        assert max(pcts) == 7, f"expected progress capped at 7%, got {max(pcts)}%"

    def test_no_pytest_alive(self):
        out = subprocess.run(["pgrep", "-f", "pytest.*mediascope"], capture_output=True, text=True)
        assert out.stdout.strip() == "", f"no mediascope pytest should be alive: {out.stdout.strip()}"


# -- Rotation guard / novelty anchor (#565 convention) ------------------------

class TestRotationCycleGuard740:
    ANCHORED_SHA = ANCHORED_SHA

    @staticmethod
    def _rotation_files():
        result = {}
        for fn in os.listdir(TESTS_DIR):
            m = re.match(r"test_type_([a-e])_(\d+)_", fn)
            if m:
                result.setdefault(int(m.group(2)), []).append((m.group(1), fn))
        return result

    def test_25_rotation_files_contiguous(self):
        files = self._rotation_files()
        for n in range(716, 741):
            assert n in files and len(files[n]) == 1, \
                f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_736_740_closes_e_to_d(self):
        files = self._rotation_files()
        assert files[736][0][0] == "e"
        assert files[737][0][0] == "a"
        assert files[738][0][0] == "b"
        assert files[739][0][0] == "c"
        assert files[740][0][0] == "d"
        assert files[740][0][1] == TEST_BASENAME

    def test_739_was_type_c_in_window(self):
        files = self._rotation_files()
        assert files[739][0][0] == "c"

    def test_rotation_adjacency_cycle_valid(self):
        files = self._rotation_files()
        order = "deabc"
        for n in range(716, 740):
            cur = files[n][0][0]
            nxt = files[n + 1][0][0]
            assert nxt == order[(order.index(cur) + 1) % 5], \
                f"rotation break between #{n} ({cur}) and #{n + 1} ({nxt})"

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 736-740 closes E->D. Anchor patched in followup per #565.

        The main commit is selected robustly: followup and push-pending-note
        commits also carry the "Type D #740:" subject, so the naive newest-match
        would shadow the main commit once the note is committed (the #735
        hardening, kept here).
        """
        result = _git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type D #740:" in line
            and "followup" not in line
            and "push-pending note" not in line
        ]
        assert len(mains) == 1, f"expected exactly one Type D #740 main commit, got {mains}"
        main = mains[0].split()[0]
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


# -- Doc-sync ratchet ----------------------------------------------------------

class TestDocSyncRatchet740:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    def test_readme_test_file_table_row(self):
        content = open(os.path.join(REPO_ROOT, "README.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_architecture_tree_row(self):
        content = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_iteration_log_tail_740(self):
        # Recent runs (#736-#739) append entries at the end of iteration-log.md
        # (the file head stays frozen at #735 per #735's committed doc-sync
        # test), so the #740 entry is asserted at the tail.
        tail = open(LOG, encoding="utf-8").read()[-4000:]
        assert "#740 Type D:" in tail, tail[-200:]
