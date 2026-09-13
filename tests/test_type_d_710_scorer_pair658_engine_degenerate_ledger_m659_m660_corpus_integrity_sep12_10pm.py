"""
Type D -- Iteration #710 (Sat 2026-09-12 22:00 PDT): scorer-degenerate
consistency (m658 pair) + falsification-ledger membership (m659) +
qualitative discipline (m660) + post-#709 corpus integrity.

Verifies:
- m658 (Bloomberg Apple Duo vs Bloomberg Meta Muse, Type A #707):
  pinned illustrative delta +0.35 ([0.40] Apple vs [0.05] Meta) reproduces
  through the real calculate_asymmetry path under the classic degenerate
  n=1-per-arm contract (t=0.0, p=1.0, d=0.0, is_significant False);
  arm-swap negates to -0.35 exactly. EIGHTEENTH n=1-per-arm
  degenerate-ledger pair. Zero-gradient control (no Bloomberg LP AI
  licensing deal with Apple or Meta) - NOT a falsification-family member.
- m659 (Harry McCracken register constancy, Type B #708): journalist-level
  YAML mechanism present with pinned delta -0.10 (-0.475 vs -0.38);
  TWENTY-SECOND falsification-family member (journalist-attribution
  class); ledger holds at 22.
- m660 (OpenAI India attribution-deal economics layer, Type C #709):
  qualitative-only statistical_discipline (scorer none, tone_scores
  NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
  False); NOT a falsification-family member (ledger stays at 22 per
  #609/#614 qualitative boundary).
- Post-#709 corpus integrity: max numeric mechanism_id == 660 in
  profiles/; zero mechanism_661 keys in profiles/ and tests/; m658 /
  m659 / m660 each unique; TWENTY-FIRST present, TWENTY-SECOND present,
  TWENTY-THIRD absent.
- Rotation guard: #709 Type C main commit present; 708-712 window
  closes C->D->E->A (anchor patched in the followup per #565).

Full-suite status: the 37K suite launched under #705 was killed mid-run
(log truncated at 206 bytes, no pytest alive at #710 check); re-launched
this run in the background to goal hidden_files type_d_710_full_suite.log
with the not-yet-existent anchor deselected; next Type D run checks it.
"""

import os
import re
import sys
import glob
import subprocess
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_BASENAME = os.path.basename(__file__)

from mediascope.score.asymmetry import calculate_asymmetry

ITERATION = 710
MECH_MAX = 660

COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")


def _load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True, text=True, timeout=60,
    )


def _find_mechanisms(yaml_path, mech_id):
    """Recursively find (key, block) pairs with mechanism_id == mech_id.

    Mechanisms live at entities.<entity>.mechanism_<id>_... in
    competitor-entities.yaml and inside list entries under 'journalists'
    in journalists.yaml; the walk recurses into list values (per the #705
    tooling fix - a dict-only walk silently misses journalists.yaml).
    """
    data = _load_yaml(yaml_path)
    found = []

    def walk(o):
        if isinstance(o, dict):
            for key, block in o.items():
                if isinstance(block, dict):
                    if block.get("mechanism_id") == mech_id:
                        found.append((key, block))
                walk(block)
        elif isinstance(o, list):
            for item in o:
                walk(item)

    walk(data)
    return found


class TestMechanism658CorpusPresence:
    """m658 lives at entities.apple in competitor-entities.yaml."""

    def _mech(self):
        hits = _find_mechanisms(COMPETITOR_ENTITIES, 658)
        assert len(hits) == 1, f"m658 must be unique, got {len(hits)}"
        return hits[0][0], hits[0][1]

    def test_m658_present_under_entities_apple(self):
        key, block = self._mech()
        assert "bloomberg" in key and "duo" in key
        assert block["publication_focus"] == "bloomberg"
        assert block["competitor"] == "apple"

    def test_m658_pinned_illustrative_delta(self):
        _, block = self._mech()
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert abs(scorer["delta_manual_illustrative"] - 0.35) < 1e-9
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [0.4]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [0.05]
        assert scorer["target_avg"] == 0.4
        assert scorer["peer_avg"] == 0.05

    def test_m658_iteration_attribution(self):
        _, block = self._mech()
        assert block["iteration"] == 707
        assert block["iteration_type"] == "A"
        assert block["mechanism_id"] == 658

    def test_m658_not_falsification_family_member(self):
        _, block = self._mech()
        membership = str(block["falsification_family"]["membership"])
        assert "NOT a falsification-family member" in membership
        assert "zero-gradient control" in membership


class TestMechanism658ScorerDegenerateContract:
    """EIGHTEENTH n=1-per-arm degenerate pair: [0.40] vs [0.05] through the
    real calculate_asymmetry path. The illustrative delta pins the block;
    the engine binds the significance flag, never the finding."""

    APPLE_ARM = [0.40]
    META_ARM = [0.05]

    def _score(self, target, peers):
        return calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Apple",
            peer_entities=["Meta"],
            publication_slug="bloomberg",
            period_start=datetime(2026, 9, 8),
            period_end=datetime(2026, 9, 12),
        )

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - 0.35) < 1e-9

    def test_degenerate_contract_binds_significance(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        r = self._score(self.META_ARM, self.APPLE_ARM)
        assert abs(r.asymmetry_score - (-0.35)) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0

    def test_illustrative_delta_is_manual_only(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 658)[0]
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["methodology"].startswith("MANUAL ILLUSTRATIVE")
        assert "DO NOT claim empirical significance" in scorer["methodology"]


class TestMechanism659LedgerMembership:
    """m659: TWENTY-SECOND falsification-family member (journalist-attribution
    class); McCracken register constancy bounds the Aug 20 #201 thesis."""

    def _mech(self):
        hits = _find_mechanisms(JOURNALISTS, 659)
        assert len(hits) == 1, f"m659 must be unique, got {len(hits)}"
        return hits[0][0], hits[0][1]

    def test_m659_present_unique_on_mccracken_entry(self):
        _, block = self._mech()
        assert block["journalist"] == "Harry McCracken"
        assert block["publication"] == "Fast Company"
        assert block["iteration"] == 708

    def test_m659_twenty_second_marker(self):
        _, block = self._mech()
        verdict = str(block["verdict"])
        assert "TWENTY-SECOND" in verdict
        assert "falsification-family member" in verdict
        assert "journalist-attribution" in verdict

    def test_m659_pinned_delta_and_discipline(self):
        _, block = self._mech()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["delta_competitor_minus_meta"] - (-0.1)) < 1e-9
        assert scorer["target_tones_manual_illustrative"] == [-0.5, -0.45]
        assert scorer["reference_tones_manual_illustrative"] == [-0.38]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_m659_ledger_holds_at_22(self):
        hits21 = []
        hits22 = []
        for path in [COMPETITOR_ENTITIES, JOURNALISTS]:
            text = open(path, encoding="utf-8").read()
            if "TWENTY-FIRST" in text:
                hits21.append(path)
            if "TWENTY-SECOND" in text:
                hits22.append(path)
        assert hits21, "TWENTY-FIRST must be present in profiles/"
        assert hits22, "TWENTY-SECOND must be present in profiles/"
        assert "TWENTY-THIRD" not in open(COMPETITOR_ENTITIES, encoding="utf-8").read()
        assert "TWENTY-THIRD" not in open(JOURNALISTS, encoding="utf-8").read()


class TestMechanism660QualitativeDiscipline:
    """m660: qualitative Type C economics layer - no tone arms, no engine."""

    def _mech(self):
        hits = _find_mechanisms(COMPETITOR_ENTITIES, 660)
        assert len(hits) == 1, f"m660 must be unique, got {len(hits)}"
        return hits[0][0], hits[0][1]

    def test_m660_present_under_entities_openai(self):
        key, block = self._mech()
        assert "india" in key and "economics" in key
        assert block["iteration"] == 709
        assert block["iteration_type"] == "C"

    def test_m660_qualitative_only(self):
        _, block = self._mech()
        disc = block["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["correlation_not_causation"] is True

    def test_m660_not_falsification_family_member(self):
        _, block = self._mech()
        fam = str(block["falsification_family"])
        assert "NOT a member" in fam
        assert "ledger stays at 22" in fam


class TestPost709CorpusIntegrity:
    """No mechanism_661 keys anywhere; max numeric mechanism_id == 660."""

    def _all_mechanism_ids(self, yaml_path):
        ids = []

        def walk(o):
            if isinstance(o, dict):
                for block in o.values():
                    if isinstance(block, dict) and isinstance(block.get("mechanism_id"), int):
                        ids.append(block["mechanism_id"])
                    walk(block)
            elif isinstance(o, list):
                for item in o:
                    walk(item)

        walk(_load_yaml(yaml_path))
        return ids

    def test_max_mechanism_id_is_660(self):
        ids = self._all_mechanism_ids(COMPETITOR_ENTITIES) + self._all_mechanism_ids(JOURNALISTS)
        assert max(ids) == MECH_MAX

    def test_zero_mechanism_661_keys_in_profiles(self):
        for path in [COMPETITOR_ENTITIES, JOURNALISTS]:
            assert self._all_mechanism_ids(path).count(661) == 0

    def test_zero_mechanism_661_references_in_tests(self):
        own = TEST_BASENAME
        pattern = re.compile(r"mechanism_661\b|mechanism_id['\"]?\s*:\s*661|==\s*661")
        for path in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if os.path.basename(path) == own:
                continue
            text = open(path, encoding="utf-8").read()
            assert not pattern.search(text), f"stale 661 ref in {path}"

    def test_m658_m659_m660_unique_across_corpus(self):
        for mid, path in [(658, COMPETITOR_ENTITIES), (659, JOURNALISTS), (660, COMPETITOR_ENTITIES)]:
            assert len(_find_mechanisms(path, mid)) == 1


# ── Rotation guard / novelty anchor (#565 convention) ───────────────────────────
ANCHORED_SHA = "NOT_YET_COMMITTED_anchor_deselected_pre_commit_per_565"


class TestRotationCycleGuard710:
    """Window 708-712: B #708 -> C #709 -> D #710 -> E #711 -> A #712."""

    WINDOW = {708: "B", 709: "C", 710: "D", 711: "E", 712: "A"}

    def test_window_708_712_cyclic_order(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        for a, b in [(708, 709), (709, 710), (710, 711), (711, 712)]:
            assert order[(order.index(self.WINDOW[a]) + 1) % 5] == self.WINDOW[b]

    def test_709_main_commit_present_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type C #709")
        main = [l for l in out.stdout.splitlines() if l.strip().startswith(("4fb22bc",))]
        assert out.stdout.strip() != "", "missing committed iteration #709"
        assert any("Type C #709:" in l for l in out.stdout.splitlines())

    def test_no_type_d_710_main_commit_pre_anchor(self):
        out = _git("log", "--oneline", "--grep", "Type D #710")
        assert out.stdout.strip() == "", "pre-commit the #710 main commit must not exist"

    def test_anchor_is_main_commit_710(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA.
        assert _git("cat-file", "-e", f"{ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = _git("log", "-1", "--format=%s", ANCHORED_SHA).stdout.strip()
        assert "Type D #710" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#710 Type D: scorer-degenerate consistency m658 + ledger m659 + corpus integrity post-#709"
        assert re.match(r"^#710 Type D:", sample)


class TestDocSyncRatchet710:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_has_710_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_710_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_has_710_entry(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert re.search(r"^#710 Type D:", text, re.M)
