"""
Type D -- Iteration #720 (Sun 2026-09-13 08:00 PDT): scorer-degenerate
consistency (m664 + m665 pairs) + qualitative discipline (m666) +
post-#719 corpus integrity + #715 background-suite tombstone (fourth
consecutive death; re-launched as type_d_720_full_suite.log).

Verifies:
- m664 (Reuters x OpenAI slowdown-week vs Reuters x Meta Muse, Type A
  #717): pinned illustrative delta +0.75 ([0.30] OpenAI vs [-0.45]
  Meta) reproduces through the real calculate_asymmetry path under the
  classic degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False); arm-swap negates to -0.75 exactly. TWENTY-THIRD
  falsification-family member (ledger 22->23). Manual-illustrative only;
  genre-mismatch confound load-bearing.
- m665 (Jennifer Valentino-DeVries NYT investigations register symmetry,
  Type B #718): FIRST mechanism key on her journalist entry; pinned
  illustrative delta -0.05 ([-0.60] OpenAI vs [-0.55 x3] Meta) reproduces
  through the real calculate_asymmetry path under a MIXED-n degenerate
  contract (n=1 vs n=3): t=0.0, p=1.0, is_significant False; arm-swap
  negates to +0.05 exactly. TENTH degenerate-boundary pin - first
  zero-variance-both-arms variant: cohens_d collapses to 0.0 EXACTLY
  (not junk), pinning the junk-d refinement: #667's junk d=+17.68 arose
  because the multi arm carried variance; when the n=3 arm has zero
  variance too, the pooled sd is 0 and the guard returns 0.0. TWENTY-FOURTH
  falsification-family member (ledger 23->24).
- m666 (EU antitrust probe into Google publisher-AI content use + Sep
  2026 opt-out questionnaire, Type C #719): qualitative-only
  statistical_discipline (tone_scores NOT_SCORED, p_value / cohens_d /
  ci_95 NOT_CALCULATED, is_significant False); no_coverage_tone_claim;
  no asymmetry scorer keys; NOT a falsification-family member
  (ledger stays at 24 per #609/#614 qualitative boundary).
- Falsification ledger: TWENTY-THIRD present (m664), TWENTY-FOURTH
  present (m665), TWENTY-FIFTH absent; ledger holds at 24.
- Post-#719 corpus integrity: max numeric mechanism_id == 666 in
  profiles/; zero mechanism_667 keys in profiles/ and tests/;
  m664 / m665 / m666 each unique.
- Statistical meaningfulness: fresh strong-signal synthetic n=5-per-arm
  pair reproduces engine significance at the ENGINE layer
  (asymmetry +0.796, t~18.63, p~7.5e-08, d~11.78, CI (0.726, 0.87)
  above zero, is_significant True); fresh near-null pair stays silent
  (t~0.26, p~0.803, CI crossing zero). Engine significance is never
  promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #715 re-launched background suite died mid-run
  (log stalled at 3680 bytes / 8% progress since Sep 13 11:08 UTC, no
  pytest alive at this run's check) - FOURTH consecutive background
  death (#705's, #710's, #715's first re-launch, #715's re-launch).
  Re-launched this run to goal hidden_files
  type_d_720_full_suite.log with the not-yet-existent anchor deselected;
  next Type D run checks it.
- Rotation guard: #719 Type C main commit present; 716-720 window
  orders E->A->B->C->D (anchor patched in the followup per #565).
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

ITERATION = 720
MECH_MAX = 666

COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
NYTIMES = os.path.join(REPO_ROOT, "profiles", "nytimes.yaml")
GOAL_HIDDEN = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files"
)


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

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, dict) and v.get("mechanism_id") == mech_id:
                    found.append((k, v))
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


def _count_mechanism_id_keys(max_exclusive=1000):
    """All numeric mechanism ids repo-wide (mechanism_<N>_ or mechanism_id: N)."""
    ids = set()
    for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"),
                          recursive=True):
        for line in open(path, errors="replace"):
            for m in re.finditer(r"mechanism_(\d+)_", line):
                ids.add(int(m.group(1)))
            for m in re.finditer(r"mechanism_id:\s*['\"]?(\d+)", line):
                ids.add(int(m.group(1)))
    return ids


def _score(target, peers, target_entity, peer_entity, publication_slug):
    return calculate_asymmetry(
        target_scores=target,
        peer_scores=peers,
        target_entity=target_entity,
        peer_entities=[peer_entity],
        publication_slug=publication_slug,
        period_start=datetime(2026, 9, 8),
        period_end=datetime(2026, 9, 13),
    )


# -- m664: Type A #717 corpus -------------------------------------------------

KEY_664 = "mechanism_664_reuters_openai_slowdown_week_register_vs_meta_muse_accountability_sep13"


class TestMechanism664Corpus:
    """m664 corpus block (Reuters x OpenAI slowdown-week, Type A #717)."""

    def _mech(self):
        found = _find_mechanisms(COMPETITOR_ENTITIES, 664)
        assert len(found) == 1, f"m664 must be unique, got {len(found)}"
        return found[0]

    def test_key_name(self):
        key, _ = self._mech()
        assert key == KEY_664

    def test_iteration_block(self):
        _, block = self._mech()
        assert block["iteration"] == 717
        assert block["iteration_type"] == "A"
        assert block["mechanism_id"] == 664
        assert "test_type_a_717" in block["test_file"]

    def test_pinned_arms(self):
        _, block = self._mech()
        assert block["openai_arm"]["manual_illustrative_tone"] == 0.3
        assert block["meta_arm"]["manual_illustrative_tone"] == -0.45
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [0.3]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.45]
        assert scorer["delta_manual_illustrative"] == 0.75
        assert scorer["delta_calc"] == "0.30 - (-0.45) = 0.75"

    def test_twenty_third_falsification_member(self):
        _, block = self._mech()
        membership = str(block["falsification_family"]["membership"])
        assert "TWENTY-THIRD member" in membership
        assert "ledger stood at 22" in membership

    def test_illustrative_discipline(self):
        _, block = self._mech()
        disc = block["statistical_discipline"]
        assert disc["is_significant"] is False
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["tone_scores"] == "ILLUSTRATIVE_NOT_EMPIRICAL"
        assert "Aug 28 2026 standing rule" in disc["rule"]

    def test_no_analysis_json_update(self):
        _, block = self._mech()
        assert "No analysis.json update warranted" in block["artifact_readiness"]


class TestMechanism664ScorerDegenerateContract:
    """[0.30] vs [-0.45] through the real calculate_asymmetry path: the
    classic n=1-per-arm degenerate contract (t=0.0, p=1.0, d=0.0,
    is_significant False). |asymmetry| == 0.75 within 1e-9 of the pinned
    MANUAL ILLUSTRATIVE delta; arm-swap negates exactly."""

    OPENAI_ARM = [0.30]
    META_ARM = [-0.45]

    def _score(self, target, peers):
        return _score(target, peers, "OpenAI", "Meta", "reuters")

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.OPENAI_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - 0.75) < 1e-9
        assert abs(r.target_avg_tone - 0.30) < 1e-9
        assert abs(r.peer_avg_tone - (-0.45)) < 1e-9

    def test_degenerate_contract_binds_significance(self):
        r = self._score(self.OPENAI_ARM, self.META_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert r.article_count_target == 1
        assert r.article_count_peers == 1

    def test_arm_swap_negates_exactly(self):
        r = self._score(self.META_ARM, self.OPENAI_ARM)
        assert abs(r.asymmetry_score - (-0.75)) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False


# -- m665: Type B #718 corpus ---------------------------------------------------

KEY_665 = "type_b_718_jennifer_valentino_devries_nyt_openai_meta_investigations_register_symmetry_sep13"


class TestMechanism665Corpus:
    """m665 corpus block (Valentino-DeVries investigations register
    symmetry, Type B #718) - FIRST mechanism key on her entry."""

    def _mech(self):
        found = _find_mechanisms(JOURNALISTS, 665)
        assert len(found) == 1, f"m665 must be unique, got {len(found)}"
        return found[0]

    def test_key_name_and_iteration_block(self):
        key, block = self._mech()
        assert key == KEY_665
        assert block["mechanism_id"] == 665
        assert block["iteration"] == 718
        assert block["iteration_type"] == "B"
        assert block["journalist"] == "Jennifer Valentino-DeVries"
        assert block["publication"] == "nytimes"

    def test_pinned_arms(self):
        _, block = self._mech()
        assert block["openai_arm"]["illustrative_tone"] == -0.60
        meta_tones = [a["illustrative_tone"] for a in block["meta_arms"]]
        assert len(meta_tones) == 3
        assert all(t == -0.55 for t in meta_tones)
        assert block["illustrative_delta_openai_minus_meta"] == -0.05

    def test_scorer_contract_text(self):
        _, block = self._mech()
        contract = str(block["scorer_contract"])
        assert "MANUAL ILLUSTRATIVE ONLY" in contract
        assert "degenerate n=1 vs n=3" in contract
        assert "is_significant False" in contract
        assert "Arm-swap negates delta to +0.05 exactly" in contract

    def test_twenty_fourth_falsification_member(self):
        _, block = self._mech()
        assert "TWENTY-FOURTH" in str(block["cross_references"])
        assert "TWENTY-FOURTH falsification-family member" in str(block["finding"])

    def test_first_mechanism_key_on_her_entry(self):
        data = _load_yaml(JOURNALISTS)
        val = None
        for entry in data["journalists"]:
            if entry.get("name") == "Jennifer Valentino-DeVries":
                val = entry
                break
        assert val is not None
        cc = val.get("competitor_coverage", {})
        assert len(cc) == 1, f"her competitor_coverage must hold exactly the m665 block, got {len(cc)}"
        assert KEY_665 in cc


class TestMechanism665MixedDegenerateBoundary:
    """[-0.60] vs [-0.55, -0.55, -0.55] through the real path: mixed-n
    (n=1 vs n=3) degenerate - TENTH degenerate-boundary pin (first
    through ninth per the #670/#695/#700 sweeps). The BOTH-arms-zero-
    variance variant: cohens_d collapses to 0.0 EXACTLY (guard), not
    junk. This pins the junk-d refinement against #667's +17.68: junk
    arises only when the non-singleton arm carries variance; here the
    n=3 arm has zero variance too, so the pooled sd is 0 and the engine
    guard returns 0.0. |asymmetry| == 0.05 within 1e-9 of the pinned
    illustrative delta; arm-swap negates to +0.05 exactly."""

    OPENAI_ARM = [-0.60]
    META_ARM = [-0.55, -0.55, -0.55]

    def _score(self, target, peers):
        return _score(target, peers, "OpenAI", "Meta", "nytimes")

    def test_delta_matches_pinned_illustrative(self):
        r = self._score(self.OPENAI_ARM, self.META_ARM)
        assert abs(r.asymmetry_score - (-0.05)) < 1e-9

    def test_mixed_degenerate_contract_binds_significance(self):
        r = self._score(self.OPENAI_ARM, self.META_ARM)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False

    def test_zero_variance_both_arms_collapses_d_to_zero(self):
        # NOT junk: both arms zero-variance -> pooled sd 0 -> guard 0.0.
        # Contrasts #667 (m634 pair, n=2 vs n=1, junk d=+17.68) where
        # the n=2 arm carried variance and the pooled sd collapsed to
        # that arm's own sd. Junk-d requires variance in the
        # non-singleton arm; this is the clean variant of the pin.
        r = self._score(self.OPENAI_ARM, self.META_ARM)
        assert r.cohens_d == 0.0

    def test_arm_swap_negates_exactly(self):
        r = self._score(self.META_ARM, self.OPENAI_ARM)
        assert abs(r.asymmetry_score - 0.05) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False


# -- m666: Type C #719 corpus ----------------------------------------------------

KEY_666 = "mechanism_666_eu_antitrust_google_publisher_ai_optout_quiz_sep2026"


class TestMechanism666QualitativeDiscipline:
    """m666 (EU antitrust probe into Google publisher-AI content use,
    Type C #719): qualitative-only - scorer consistency does not apply
    (per #540/#544 boundary)."""

    def _mech(self):
        found = _find_mechanisms(COMPETITOR_ENTITIES, 666)
        assert len(found) == 1, f"m666 must be unique, got {len(found)}"
        return found[0]

    def test_key_name_and_iteration_block(self):
        key, block = self._mech()
        assert key == KEY_666
        assert block["mechanism_id"] == 666
        assert block["iteration"] == 719
        assert block["iteration_type"] == "C"

    def test_no_scorer_keys_present(self):
        _, block = self._mech()
        scorer_keys = [k for k in block.keys()
                       if "scorer" in k.lower() or "asymmetry" in k.lower()]
        assert scorer_keys == [], f"m666 must carry no scorer keys, got {scorer_keys}"

    def test_statistical_discipline_qualitative(self):
        _, block = self._mech()
        disc = block["statistical_discipline"]
        assert disc["scope"] == "qualitative structural mapping only"
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False

    def test_no_coverage_tone_claim(self):
        _, block = self._mech()
        assert block["no_coverage_tone_claim"] is True

    def test_not_falsification_family_member(self):
        _, block = self._mech()
        hits = [x for x in block["novelty_verification"]
                if "NOT a falsification-family member" in str(x)]
        assert len(hits) == 1
        assert "ledger stays at 24" in str(hits[0])
        assert "#609/#614 qualitative boundary" in str(hits[0])

# -- Post-#719 corpus integrity -----------------------------------------------


class TestCorpusIntegrityPost719:
    """Max numeric mechanism_id == 666; zero mechanism_667 keys; the
    three new mechanisms each unique; falsification ledger holds at 24
    (TWENTY-FOURTH present, no TWENTY-FIFTH anywhere in profiles/)."""

    def test_max_numeric_mechanism_id_is_666(self):
        assert max(_count_mechanism_id_keys()) == MECH_MAX == 666

    def test_zero_mechanism_667_keys(self):
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"),
                              recursive=True):
            for line in open(path, errors="replace"):
                assert not re.search(r"mechanism_667(?![0-9])", line), path
        for path in glob.glob(os.path.join(TESTS_DIR, "*.py")):
            if os.path.basename(path) == TEST_BASENAME:
                continue
            for line in open(path, errors="replace"):
                if "mechanism_667" in line and "_mechanism()[" not in line:
                    assert re.search(r"iteration", line), (path, line[:100])

    def test_m664_m665_m666_each_unique_repo_wide(self):
        for mech_id, yaml_path in [(664, COMPETITOR_ENTITIES),
                                   (665, JOURNALISTS),
                                   (666, COMPETITOR_ENTITIES)]:
            found = _find_mechanisms(yaml_path, mech_id)
            assert len(found) == 1, f"mechanism {mech_id} must be unique"

    def test_falsification_ledger_holds_at_24(self):
        corpus = ""
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"),
                              recursive=True):
            corpus += open(path, errors="replace").read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus
        # The three new mechanisms' membership claims are pinned in their
        # own corpus classes; here we only assert the ledger cap.


# -- Statistical meaningfulness on fresh synthetic corpora ----------------------

class TestStatisticalMeaningfulnessFreshSynthetic:
    """The statistical-meaningfulness mandate on FRESH arrays (never the
    corpus pins): a strong-signal n=5-per-arm pair is significant at the
    ENGINE layer; a near-null pair stays silent. Per the Aug 28 2026
    standing rule, engine significance on synthetic illustrative arrays
    is NEVER promoted to a finding - the finding layer stays
    is_significant False for all three illustrative mechanisms verified
    above."""

    STRONG_TARGET = [0.28, 0.35, 0.22, 0.31, 0.19]
    STRONG_PEER = [-0.52, -0.48, -0.61, -0.44, -0.58]
    NULL_TARGET = [0.02, -0.03, 0.05, -0.01, 0.04]
    NULL_PEER = [-0.04, 0.01, 0.06, -0.02, 0.03]

    def test_strong_signal_significant_at_engine_layer(self):
        r = _score(self.STRONG_TARGET, self.STRONG_PEER,
                   "OpenAI", "Meta", "synthetic")
        assert abs(r.asymmetry_score - 0.796) < 1e-9
        assert abs(r.t_statistic - 18.627847812596183) < 1e-6
        assert 0 < r.p_value < 1e-6  # raw 7.52337720630625e-08
        assert abs(r.cohens_d - 11.781285398957863) < 1e-6
        assert r.confidence_interval_lower > 0  # (0.726, 0.87): above zero
        assert r.is_significant is True

    def test_near_null_stays_silent(self):
        r = _score(self.NULL_TARGET, self.NULL_PEER,
                   "OpenAI", "Meta", "synthetic")
        assert abs(r.t_statistic - 0.25819888974716126) < 1e-9
        assert abs(r.p_value - 0.8029410894689015) < 1e-9
        assert abs(r.cohens_d - 0.1632993161855453) < 1e-9
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper
        assert r.is_significant is False

    def test_engine_significance_never_promoted_to_finding(self):
        # The three illustrative mechanisms verified above must all keep
        # finding-layer is_significant False (Aug 28 2026 standing rule).
        _, b664 = _find_mechanisms(COMPETITOR_ENTITIES, 664)[0]
        assert b664["statistical_discipline"]["is_significant"] is False
        _, b665 = _find_mechanisms(JOURNALISTS, 665)[0]
        assert "is_significant False" in str(b665["scorer_contract"])
        _, b666 = _find_mechanisms(COMPETITOR_ENTITIES, 666)[0]
        assert b666["statistical_discipline"]["is_significant"] is False


# -- Full-suite status: #715 background tombstone + #720 re-launch --------------

class TestFullSuiteStatus720:
    """The #715 re-launched background suite died mid-run (FOURTH
    consecutive background death). Tombstoned here; re-launched as
    type_d_720_full_suite.log pre-commit; the next Type D run checks it."""

    LOG715 = os.path.join(GOAL_HIDDEN, "type_d_715_full_suite.log")
    LOG720 = os.path.join(GOAL_HIDDEN, "type_d_720_full_suite.log")

    def test_715_relaunch_log_exists(self):
        assert os.path.exists(self.LOG715)

    def test_715_suite_died_mid_run(self):
        # Stalled at 3680 bytes / 8% progress since Sep 13 11:08 UTC
        # (04:08 PDT); never advanced past the first test-file batch.
        size = os.path.getsize(self.LOG715)
        assert size < 10000, f"suite advanced past the death line, size={size}"
        tail = open(self.LOG715, errors="replace").read()[-200:]
        assert "[  8%]" in tail

    def test_715_no_pytest_alive(self):
        out = subprocess.run(["pgrep", "-f", "pytest.*type_d_715"],
                             capture_output=True, text=True)
        assert out.stdout.strip() == "", "a #715 pytest is unexpectedly alive"

    def test_720_relaunch_log_created(self):
        assert os.path.exists(self.LOG720), (
            "the 720 re-launched background suite log must exist (launched pre-commit)"
        )


# -- Rotation guard / novelty anchor (#565 convention) ---------------------------

ANCHORED_SHA = "2d975210c5d61d46207d5178ac9f96a2f676678b"


class TestRotationCycleGuard720:
    """Window 716-720: E #716 -> A #717 -> B #718 -> C #719 -> D #720."""

    WINDOW = {716: "E", 717: "A", 718: "B", 719: "C", 720: "D"}

    def test_window_716_720_cyclic_order(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        for a, b in [(716, 717), (717, 718), (718, 719), (719, 720)]:
            assert order[(order.index(self.WINDOW[a]) + 1) % 5] == self.WINDOW[b]

    def test_719_main_commit_present_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type C #719")
        lines = [l for l in out.stdout.splitlines() if l.strip()]
        assert lines, "missing committed iteration #719"
        assert any(l.startswith("cd71ea2") and "Type C #719:" in l for l in lines)

    def test_no_type_d_720_main_commit_pre_anchor(self):
        out = _git("log", "--oneline", "--grep", "Type D #720")
        assert out.stdout.strip() == "", "pre-commit the #720 main commit must not exist"

    def test_anchor_is_main_commit_720(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA.
        assert _git("cat-file", "-e", f"{ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = _git("log", "-1", "--format=%s", ANCHORED_SHA).stdout.strip()
        assert "Type D #720" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#720 Type D: scorer-degenerate consistency m664+m665 + m666 qualitative discipline + post-#719 corpus integrity"
        assert re.match(r"^#720 Type D:", sample)


class TestDocSyncRatchet720:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_test_file_table_row(self):
        content = open(self.README).read()
        assert "test_type_d_720_scorer_pair664_665_engine_degenerate_m666_qualitative_corpus_integrity_sep13_8am.py" in content

    def test_iteration_log_starts_with_720(self):
        first = open(self.LOG).readline().strip()
        assert first.startswith("#720 Type D:"), first[:80]
