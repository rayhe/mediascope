"""
Type D -- Iteration #715 (Sun 2026-09-13 03:00 PDT): scorer-degenerate
consistency (m661 + m662 pairs) + falsification-ledger membership +
qualitative discipline (m663) + post-#714 corpus integrity.

Verifies:
- m661 (NYT Apple Duo vs NYT Meta Muse, Type A #712): pinned
  illustrative delta +0.10 ([0.15] Apple vs [0.05] Meta) reproduces
  through the real calculate_asymmetry path under the classic degenerate
  n=1-per-arm contract (t=0.0, p=1.0, d=0.0, is_significant False);
  arm-swap negates to -0.10 exactly. NINETEENTH n=1-per-arm
  degenerate-ledger pair (eighteenth was m658 in #710). Minimal-gradient
  control (no known NYT x Apple AI licensing deal; NYT left Apple News
  in 2020) - NOT a falsification-family member.
- m662 (Brian X. Chen Duo value-review vs Ray-Ban privacy-alarm register,
  Type B #713): FIRST mechanism key on the Brian X. Chen journalist
  entry; pinned illustrative delta -0.65 ([-0.50] Meta vs [+0.15] Apple)
  reproduces through the real calculate_asymmetry path under the
  degenerate contract; arm-swap negates to +0.65 exactly. TWENTIETH
  n=1-per-arm degenerate-ledger pair. Zero-gradient control - NOT a
  falsification-family member; ledger holds at 22.
- m663 (Perplexity premium-data licensing layer via Cashmere, Type C
  #714): qualitative-only statistical_discipline (tone_scores
  NOT_SCORED, p_value NOT_CALCULATED, is_significant False); 9 sources,
  5 counterparties, 4 executive quotes; NOT a falsification-family
  member (ledger stays at 22 per #609/#614 qualitative boundary).
- Falsification ledger: TWENTY-FIRST present, TWENTY-SECOND present
  (m659 McCracken, journalist-attribution class), TWENTY-THIRD absent
  across the profiles corpus.
- Post-#714 corpus integrity: max numeric mechanism_id == 663 in
  profiles/; zero mechanism_664 keys in profiles/ and tests/;
  m661 / m662 / m663 each unique.
- Rotation guard: #714 Type C main commit present; 713-717 window
  orders B->C->D->E->A (anchor patched in the followup per #565).
- Full-suite status: the 37K suite re-launched under #710 died mid-run
  (log stalled at 2150 bytes / ~5% progress since Sep 12 22:46 PDT, no
  pytest alive at this run's check) - second consecutive background
  death; re-launched this run to goal hidden_files
  type_d_715_full_suite.log; next Type D run checks it.
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

ITERATION = 715
MECH_MAX = 663

COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
NYTIMES = os.path.join(REPO_ROOT, "profiles", "nytimes.yaml")


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
    competitor-entities.yaml, at competitor_relationships.<entity> in
    nytimes.yaml, and inside list entries under 'journalists' in
    journalists.yaml; the walk recurses into list values (per the #705
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


def _all_mechanism_ids(yaml_path):
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


class TestMechanism661CorpusPresence:
    """m661 lives at competitor_relationships.apple in nytimes.yaml."""

    def _mech(self):
        hits = _find_mechanisms(NYTIMES, 661)
        assert len(hits) == 1, f"m661 must be unique, got {len(hits)}"
        return hits[0][0], hits[0][1]

    def test_m661_present_at_nyt_apple(self):
        key, block = self._mech()
        assert "duo" in key and "muse" in key
        assert block["publication_focus"] == "nytimes"
        assert block["competitor"] == "apple"

    def test_m661_pinned_illustrative_delta(self):
        _, block = self._mech()
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert abs(scorer["delta_manual_illustrative"] - 0.10) < 1e-9
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [0.15]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [0.05]
        assert scorer["target_avg"] == 0.15
        assert scorer["peer_avg"] == 0.05
        assert block["apple_arm"]["average_manual_illustrative"] == 0.15
        assert block["meta_arm"]["average_manual_illustrative"] == 0.05

    def test_m661_iteration_attribution(self):
        _, block = self._mech()
        assert block["iteration"] == 712
        assert block["iteration_type"] == "A"
        assert block["mechanism_id"] == 661
        assert "test_type_a_712" in block["test_file"]

    def test_m661_minimal_gradient_not_falsification_member(self):
        _, block = self._mech()
        membership = str(block["falsification_family"]["membership"])
        assert "NOT a falsification-family member" in membership
        assert "minimal-gradient control" in membership


class TestMechanism661ScorerDegenerateContract:
    """NINETEENTH n=1-per-arm degenerate pair: [0.15] vs [0.05] through
    the real calculate_asymmetry path. The illustrative delta pins the
    block; the engine binds the significance flag, never the finding."""

    APPLE_ARM = [0.15]
    META_ARM = [0.05]

    def _score(self, target, peers):
        return calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Apple",
            peer_entities=["Meta"],
            publication_slug="nytimes",
            period_start=datetime(2026, 9, 8),
            period_end=datetime(2026, 9, 12),
        )

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - 0.10) < 1e-9

    def test_degenerate_contract_binds_significance(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        r = self._score(self.META_ARM, self.APPLE_ARM)
        assert abs(r.asymmetry_score - (-0.10)) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0

    def test_illustrative_delta_is_manual_only(self):
        _, block = _find_mechanisms(NYTIMES, 661)[0]
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["methodology"].startswith("MANUAL ILLUSTRATIVE")
        assert "DO NOT claim empirical significance" in scorer["methodology"]


class TestMechanism662ChenEntryPresence:
    """m662: FIRST mechanism key on the Brian X. Chen journalist entry."""

    def _entry_and_mech(self):
        data = _load_yaml(JOURNALISTS)
        chen = [j for j in data["journalists"] if j.get("name") == "Brian X. Chen"]
        assert len(chen) == 1, "Brian X. Chen entry must be unique"
        entry = chen[0]
        mech_keys = [k for k in entry if isinstance(k, str) and k.startswith("mechanism_")]
        assert len(mech_keys) == 1, f"Chen entry must carry exactly one mechanism, got {mech_keys}"
        assert "mechanism_662" in mech_keys[0]
        return entry, mech_keys[0], entry[mech_keys[0]]

    def test_m662_first_mechanism_on_chen_entry(self):
        _, key, block = self._entry_and_mech()
        assert block["mechanism_id"] == 662
        assert block["journalist"] == "Brian X. Chen"
        assert block["publication"] == "The New York Times"
        assert "duo_value_review_vs_rayban_privacy_alarm" in key

    def test_m662_pinned_delta_minus_065(self):
        _, _, block = self._entry_and_mech()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["delta_meta_minus_apple"] - (-0.65)) < 1e-9
        assert scorer["target_tones_manual_illustrative"] == [-0.5]
        assert scorer["reference_tones_manual_illustrative"] == [0.15]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert scorer["artifact_grade"] is False

    def test_m662_arm_tones_match_block_arms(self):
        _, _, block = self._entry_and_mech()
        assert block["meta_arm"]["tone_illustrative"] == -0.5
        assert block["apple_arm"]["tone_illustrative"] == 0.15
        assert block["meta_arm"]["byline"].startswith("Brian X. Chen")
        assert block["apple_arm"]["byline"].startswith("Brian X. Chen")

    def test_m662_zero_gradient_not_falsification_member(self):
        _, _, block = self._entry_and_mech()
        verdict = str(block["verdict"])
        assert "NOT a falsification-family member" in verdict
        assert "Zero-gradient financial control" in verdict or "zero-gradient" in verdict.lower()
        finctx = block["financial_context"]
        assert finctx["predictor"] == "zero_gradient_control"
        assert finctx["prediction"] == "no_differential_prediction"


class TestMechanism662ScorerDegenerateContract:
    """TWENTIETH n=1-per-arm degenerate pair: [-0.50] vs [0.15] through
    the real calculate_asymmetry path."""

    META_ARM = [-0.5]
    APPLE_ARM = [0.15]

    def _score(self, target, peers):
        return calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Meta",
            peer_entities=["Apple"],
            publication_slug="nytimes",
            period_start=datetime(2023, 12, 1),
            period_end=datetime(2026, 9, 12),
        )

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.META_ARM, self.APPLE_ARM)
        assert abs(r.asymmetry_score - (-0.65)) < 1e-9

    def test_degenerate_contract_binds_significance(self):
        r = self._score(self.META_ARM, self.APPLE_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        r = self._score(self.APPLE_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - 0.65) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0


class TestMechanism663QualitativeDiscipline:
    """m663: qualitative Type C mapping - no tone arms, no engine."""

    def _mech(self):
        hits = _find_mechanisms(COMPETITOR_ENTITIES, 663)
        assert len(hits) == 1, f"m663 must be unique, got {len(hits)}"
        return hits[0][0], hits[0][1]

    def test_m663_present_under_entities_perplexity(self):
        key, block = self._mech()
        assert "perplexity" in key and "cashmere" in key
        assert block["iteration"] == 714
        assert block["iteration_type"] == "C"
        assert block["type"] == "financial_incentive_mapping"

    def test_m663_qualitative_only(self):
        _, block = self._mech()
        assert block["tone_scores"] == "NOT_SCORED"
        disc = block["statistical_discipline"]
        assert "Qualitative Type C mapping" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "significant False" in disc
        # Corpus wording is "Not a falsification-family member" (sentence
        # case); pin the accurate casing, not the all-caps variant.
        assert "Not a falsification-family member" in disc
        assert "ledger stays 22" in disc

    def test_m663_evidence_base(self):
        _, block = self._mech()
        assert len(block["sources"]) == 9
        assert len(block["counterparties"]) == 5
        assert len(block["executive_quotes"]) == 4

    def test_m663_not_falsification_family_member(self):
        _, block = self._mech()
        disc = str(block["statistical_discipline"])
        assert "#609/#614 qualitative boundary" in disc


class TestFalsificationLedgerHolds:
    """Ledger stands at 22: TWENTY-SECOND (m659) present, no TWENTY-THIRD."""

    def test_twenty_first_and_twenty_second_present(self):
        hits21, hits22 = [], []
        for path in [COMPETITOR_ENTITIES, JOURNALISTS]:
            text = open(path, encoding="utf-8").read()
            if "TWENTY-FIRST" in text:
                hits21.append(path)
            if "TWENTY-SECOND" in text:
                hits22.append(path)
        assert hits21, "TWENTY-FIRST must be present in profiles/"
        assert hits22, "TWENTY-SECOND must be present in profiles/"

    def test_twenty_third_absent_everywhere(self):
        for path in [COMPETITOR_ENTITIES, JOURNALISTS, NYTIMES]:
            text = open(path, encoding="utf-8").read()
            assert "TWENTY-THIRD" not in text, f"TWENTY-THIRD unexpectedly in {path}"


class TestPost714CorpusIntegrity:
    """Max numeric mechanism_id == 663; no mechanism_664 keys anywhere."""

    def test_max_mechanism_id_is_663(self):
        ids = (
            self._ids(COMPETITOR_ENTITIES)
            + self._ids(JOURNALISTS)
            + self._ids(NYTIMES)
        )
        assert max(ids) == MECH_MAX

    def _ids(self, path):
        return _all_mechanism_ids(path)

    def test_zero_mechanism_664_keys_in_profiles(self):
        for path in [COMPETITOR_ENTITIES, JOURNALISTS, NYTIMES]:
            assert self._ids(path).count(664) == 0, f"mechanism 664 already in {path}"

    def test_zero_mechanism_664_references_in_tests(self):
        # Scoped to mechanism-id references: a bare "== 664" also matches
        # the historical iteration-#664 Type C file
        # (test_type_c_664_meta_reuters_ai_chatbot_deal_falsification_sep10_9pm.py,
        # where 664 is the iteration number via _mechanism()["iteration"]),
        # which is not a mechanism_664 key and must not trip this gate.
        own = TEST_BASENAME
        pattern = re.compile(r"mechanism_664\b|mechanism_id.{0,50}\b664\b")
        for path in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if os.path.basename(path) == own:
                continue
            text = open(path, encoding="utf-8").read()
            assert not pattern.search(text), f"stale mechanism_664 ref in {path}"

    def test_m661_m662_m663_unique_across_corpus(self):
        assert len(_find_mechanisms(NYTIMES, 661)) == 1
        assert len(_find_mechanisms(JOURNALISTS, 662)) == 1
        assert len(_find_mechanisms(COMPETITOR_ENTITIES, 663)) == 1


class TestFullSuiteStatus715:
    """The #710 re-launched 37K background suite died mid-run (second
    consecutive background death): no pytest alive at this run's check,
    type_d_710_full_suite.log stalled at 2150 bytes / ~5% progress since
    Sep 12 22:46 PDT. Tombstone pins + re-launch marker for the next
    Type D run."""

    LOG710 = os.path.expanduser(
        "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
        "hidden_files/type_d_710_full_suite.log"
    )
    LOG715 = os.path.expanduser(
        "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
        "hidden_files/type_d_715_full_suite.log"
    )

    def test_710_suite_log_is_stalled_tombstone(self):
        assert os.path.exists(self.LOG710)
        size = os.path.getsize(self.LOG710)
        assert size == 2150, f"expected stalled 2150-byte log, got {size}"
        text = open(self.LOG710, encoding="utf-8", errors="replace").read()
        assert not re.search(r"^=+ .*(passed|failed|error)", text, re.M), (
            "710 log must not carry a pytest final summary - the run died mid-collection"
        )

    def test_715_relaunch_log_created(self):
        assert os.path.exists(self.LOG715), (
            "the 715 re-launched background suite log must exist (launched pre-commit)"
        )


# -- Rotation guard / novelty anchor (#565 convention) ---------------------------
ANCHORED_SHA = "c0ea1eecf66df91a077401a054391d84cb69d404"


class TestRotationCycleGuard715:
    """Window 713-717: B #713 -> C #714 -> D #715 -> E #716 -> A #717."""

    WINDOW = {713: "B", 714: "C", 715: "D", 716: "E", 717: "A"}

    def test_window_713_717_cyclic_order(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        for a, b in [(713, 714), (714, 715), (715, 716), (716, 717)]:
            assert order[(order.index(self.WINDOW[a]) + 1) % 5] == self.WINDOW[b]

    def test_714_main_commit_present_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type C #714")
        lines = [l for l in out.stdout.splitlines() if l.strip()]
        assert lines, "missing committed iteration #714"
        assert any(l.startswith("afe77c3") and "Type C #714:" in l for l in lines)

    def test_no_type_d_715_main_commit_pre_anchor(self):
        out = _git("log", "--oneline", "--grep", "Type D #715")
        assert out.stdout.strip() == "", "pre-commit the #715 main commit must not exist"

    def test_anchor_is_main_commit_715(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA.
        assert _git("cat-file", "-e", f"{ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = _git("log", "-1", "--format=%s", ANCHORED_SHA).stdout.strip()
        assert "Type D #715" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#715 Type D: scorer-degenerate consistency m661+m662 + ledger holds + corpus integrity post-#714"
        assert re.match(r"^#715 Type D:", sample)


class TestDocSyncRatchet715:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_has_715_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_715_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_has_715_entry(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert re.search(r"^#715 Type D:", text, re.M)
