"""
Type D -- Iteration #705 (Sat 2026-09-12 15:00 PDT): mechanisms 655-657
corpus integrity + scorer-discipline verification.

Verifies:
- m655 (Fast Company Apple Duo vs Meta Muse, Type A #702): pinned
  illustrative delta +0.65 reproduces through the real
  calculate_asymmetry path under the classic degenerate n=1-per-arm
  contract (t=0.0, p=1.0, d=0.0, is_significant False); arm-swap
  negates exactly. Zero-gradient control (Mansueto Ventures has no
  known AI licensing deal) - NOT a falsification-family member.
- m656 (Parmy Olson Coxon-resignation Anthropic register constancy,
  Type B #703): journalist-level YAML mechanism present with pinned
  delta -0.04; TWENTY-FIRST falsification-family member
  (journalist-attribution class); register constancy verdict.
- m657 (ANI v. OpenAI India litigation leg, Type C #704): litigation-type
  financial-incentive mechanism present; qualitative-only
  statistical_discipline (scorer none, tone_scores NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False).
- Post-#704 corpus integrity: max numeric mechanism_id == 657;
  zero mechanism_658 keys in profiles/ and tests/; m655/m656/m657
  keys unique.
- Rotation guard: exactly one Type C #704 main commit (anchor patched
  in the followup per the #565 convention).
"""
import os
import re
import sys
import subprocess
import glob
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_BASENAME = os.path.basename(__file__)

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

ITERATION = 705
MECH_MAX = 657

COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")


def _load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


def _find_mechanism_in_profiles_yaml(yaml_path, mech_id):
    """Recursively find the (key, block) with mechanism_id == mech_id.

    Mechanisms live at entities.<entity>.mechanism_<id>_... in
    competitor-entities.yaml and inside list entries under 'journalists'
    in journalists.yaml; a recursive walk covers both shapes.
    """
    data = _load_yaml(yaml_path)
    found = []

    def walk(o):
        if isinstance(o, dict):
            for key, block in o.items():
                if isinstance(block, dict):
                    if block.get("mechanism_id") == mech_id:
                        found.append((key, block))
                    else:
                        walk(block)
                elif isinstance(block, list):
                    walk(block)
        elif isinstance(o, list):
            for item in o:
                walk(item)

    walk(data)
    if not found:
        return None, None
    if len(found) > 1:
        raise AssertionError(
            "mechanism_id %d appears %d times in %s: %r"
            % (mech_id, len(found), yaml_path, [k for k, _ in found])
        )
    return found[0]


def _count_mechanism_key(yaml_path, mech_id):
    text = open(yaml_path, encoding="utf-8").read()
    return len(re.findall(r"mechanism_%d[_\w]*:" % mech_id, text))


# ── Mechanism 655: Fast Company Duo (Type A #702) ──────────────────────────

class TestMechanism655CorpusPresence:
    """m655 pins the Duo launch-genre series at five publications."""

    def test_m655_present_unique_in_competitor_entities(self):
        key, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 655)
        assert block is not None, "mechanism_id 655 missing from competitor-entities.yaml"
        assert "mechanism_655" in key
        assert block["iteration"] == 702
        assert block["iteration_type"] == "A"
        assert block["competitor"] == "apple"
        # Uniqueness: exactly one mechanism_655* key in the file
        assert _count_mechanism_key(COMPETITOR_ENTITIES, 655) == 1

    def test_m655_pinned_delta_and_arms(self):
        _, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 655)
        res = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert abs(res["delta_manual_illustrative"] - 0.65) < 1e-9
        assert res["delta_calc"] == "0.35 - (-0.3) = 0.65"
        assert res["target_scores_MANUAL_ILLUSTRATIVE"] == [0.35]
        assert res["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.3]
        assert "is_significant False" in res["finding_layer"]
        assert res["artifact_grade"] is False

    def test_m655_zero_gradient_control_not_falsification_member(self):
        _, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 655)
        membership = block["falsification_family"]["membership"]
        assert "NOT a falsification-family member" in membership
        assert "zero-gradient control" in membership


class TestMechanism655ScorerDegenerateContract:
    """The m655 pair reproduces the classic n=1-per-arm contract exactly
    through the real calculate_asymmetry path (SEVENTEENTH n=1-per-arm
    degenerate-ledger pair; first sixteen per #700's finding)."""

    APPLE_ARM = [0.35]
    META_ARM = [-0.30]

    def _score(self, target, peers):
        return calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Apple",
            peer_entities=["Meta"],
            publication_slug="fastcompany",
            period_start=datetime(2026, 9, 8),
            period_end=datetime(2026, 9, 12),
        )

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - 0.65) < 1e-9
        assert abs(r.target_avg_tone - 0.35) < 1e-9
        assert abs(r.peer_avg_tone - (-0.30)) < 1e-9

    def test_degenerate_statistics(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert is_significant(r.p_value) is False

    def test_arm_swap_negates_exactly(self):
        fwd = self._score(self.APPLE_ARM, self.META_ARM)
        rev = self._score(self.META_ARM, self.APPLE_ARM)
        assert abs(rev.asymmetry_score - (-0.65)) < 1e-9
        assert abs(fwd.asymmetry_score + rev.asymmetry_score) < 1e-9

    def test_low_level_contracts_agree(self):
        t, p = welch_t_test(self.APPLE_ARM, self.META_ARM)
        assert t == 0.0 and p == 1.0
        assert cohens_d(self.APPLE_ARM, self.META_ARM) == 0.0


# ── Mechanism 656: Parmy Olson (Type B #703) ───────────────────────────────

class TestMechanism656CorpusPresence:
    """First YAML mechanism on Parmy Olson (journalist-attribution class)."""

    def test_m656_present_unique_in_journalists_yaml(self):
        key, block = _find_mechanism_in_profiles_yaml(JOURNALISTS, 656)
        assert block is not None, "mechanism_id 656 missing from journalists.yaml"
        assert "mechanism_656" in key
        assert block["iteration"] == 703
        assert block["type"] == "B"
        assert block["journalist"] == "Parmy Olson"
        assert _count_mechanism_key(JOURNALISTS, 656) == 1

    def test_m656_pinned_delta_near_null(self):
        _, block = _find_mechanism_in_profiles_yaml(JOURNALISTS, 656)
        res = block["asymmetry_scorer_result"]
        assert abs(res["target_avg"] - (-0.55)) < 1e-9
        assert abs(res["reference_avg"] - (-0.51)) < 1e-9
        assert abs(res["delta_anthropic_minus_meta"] - (-0.04)) < 1e-9
        assert res["is_significant"] is False
        assert "TWENTY-FIRST" in block["verdict"]

    def test_m656_degenerate_statistical_contract_disclosed(self):
        _, block = _find_mechanism_in_profiles_yaml(JOURNALISTS, 656)
        res = block["asymmetry_scorer_result"]
        assert res["statistical_contract"] == "degenerate_n1_per_arm"
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["cohens_d"] == "NOT_CALCULATED"


# ── Mechanism 657: ANI litigation leg (Type C #704) ─────────────────────────

class TestMechanism657CorpusPresence:
    """First dedicated litigation-type financial-incentive mechanism."""

    def test_m657_present_unique_in_competitor_entities(self):
        key, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 657)
        assert block is not None, "mechanism_id 657 missing from competitor-entities.yaml"
        assert "mechanism_657" in key
        assert block["iteration"] == 704
        assert block["iteration_type"] == "C"
        assert block["relationship_type"] == "litigation"
        assert _count_mechanism_key(COMPETITOR_ENTITIES, 657) == 1

    def test_m657_qualitative_only_discipline(self):
        _, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 657)
        disc = block["statistical_discipline"]
        assert disc["qualitative_only"] is True
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False

    def test_m657_no_tone_arrays_for_engine(self):
        """Deal/litigation legs carry no tone arms - the engine cannot run."""
        _, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 657)
        for banned in ("tone_scores", "target_tones_manual_illustrative",
                       "reference_tones_manual_illustrative"):
            assert banned not in block or block[banned] in ("NOT_SCORED", None), \
                "m657 must not carry engine-scored tone arrays, found %r" % (banned,)
        assert "batna_insight" in block
        assert "appeal_status" in block

    def test_m657_does_not_extend_falsification_ledger(self):
        _, block = _find_mechanism_in_profiles_yaml(COMPETITOR_ENTITIES, 657)
        blob = yaml.safe_dump(block)
        assert "TWENTY-SECOND" not in blob
        # Qualitative litigation legs are not falsification-family members;
        # the ledger holds at 21 after #703/m656 (TWENTY-FIRST).


# ── Post-#704 corpus integrity ─────────────────────────────────────────────

class TestPost704CorpusIntegrity:
    def test_max_numeric_mechanism_id_is_657(self):
        ids = []
        for path in (COMPETITOR_ENTITIES, JOURNALISTS):
            text = open(path, encoding="utf-8").read()
            ids += [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", text)]
        assert max(ids) == MECH_MAX, "expected max mechanism_id 657, got %d" % max(ids)

    def test_no_mechanism_658_in_profiles(self):
        for path in (COMPETITOR_ENTITIES, JOURNALISTS):
            text = open(path, encoding="utf-8").read()
            assert "mechanism_658" not in text, "unexpected mechanism_658 in %s" % path

    def test_no_mechanism_658_in_tests(self):
        own = os.path.abspath(__file__)
        for path in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if os.path.abspath(path) == own:
                continue
            if path.endswith(".pyc"):
                continue
            text = open(path, encoding="utf-8").read()
            assert "mechanism_658" not in text, "unexpected mechanism_658 in %s" % path

    def test_falsification_ledger_holds_at_21(self):
        text = open(JOURNALISTS, encoding="utf-8").read()
        assert "TWENTY-FIRST" in text
        assert "TWENTY-SECOND" not in text


# ── Rotation guard / novelty anchor (#565 convention) ───────────────────────

ANCHORED_SHA = "3336b073b241935817dd6c480659d290820ea0ec"


class TestRotationCycleGuard705:
    """Deselected pre-commit; anchor patched in the followup commit."""

    def test_type_d_705_file_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_d_705*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_d_705_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_d_705 files, no #705 in git log, zero
        # mechanism_658 keys in profiles/ and tests/, max mechanism_id 657,
        # m655/m656/m657 present and unique).
        import re as _re
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if _re.match(r"^[0-9a-f]{40} Type D #705:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type D #705 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == ANCHORED_SHA, "anchor patched in followup per #565 convention"


class TestRotationSequenceContinuity:
    """702 A -> 703 B -> 704 C -> 705 D is the rotation."""

    def test_type_d_705_log_entry_landed_with_commit(self):
        # Post-commit companion to the pre-commit novelty grep: the #705
        # entry is in the iteration log and the main commit exists.
        log = open(os.path.join(REPO_ROOT, "iteration-log.md"), encoding="utf-8").read()
        assert "#705 Type D" in log
        assert TEST_BASENAME in log
        out = _run_git("log", "--format=%s")
        assert "Type D #705:" in out.stdout

    def test_previous_hours_present_in_log(self):
        log = open(os.path.join(REPO_ROOT, "iteration-log.md"), encoding="utf-8").read()
        assert "#702 Type A" in log
        assert "#703 Type B" in log
        assert "#704 Type C" in log
