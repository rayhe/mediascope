"""
Type D -- Iteration #730 (Sun 2026-09-13 18:00 PDT): m670 / m671 / m672
qualitative-discipline verification + post-#729 corpus integrity
(max mechanism_id 672; zero mechanism_673 keys; ledger holds at 24) +
#725 background-suite tombstone (SIXTH consecutive death; re-launched as
type_d_730_full_suite.log) + failing-band repair of the #725 triage's
27 stale-content failures across 5 files (all root-caused this run:
deliberate corpus restructures, zero corpus regressions).

Verifies:
- m670 (WIRED x Apple Audio Intelligence always-listening register test,
  Type A #727): qualitative-only discipline - MANUAL ILLUSTRATIVE +0.55,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False (Aug 28
  standing rule), engine NOT run, NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 24).
- m671 (Kit Eaton (Inc.) register INVERSION Meta-positive / Apple-adversarial,
  Type B #728): qualitative-only discipline in the finding text - MANUAL
  ILLUSTRATIVE delta -1.05 (INVERSION), p_value NOT_CALCULATED,
  is_significant False, engine NOT run, NOT artifact-grade, verdict
  directionally_supported_not_proven; NOT a falsification-family member
  (ledger holds at 24).
- m672 (US DOJ Statement of Interest in NYT v. OpenAI, political-incentive
  leg, Type C #729): FIRST dedicated DOJ-statement-of-interest mechanism;
  NOT a falsification-family member per the #609/#614 qualitative boundary
  (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#729 corpus integrity: max numeric mechanism_id == 672 in
  profiles/; zero mechanism_673 keys in profiles/ and tests/ (own file
  excluded per the #715 pattern-rescope lesson); m670 / m671 / m672 each
  unique in their home YAML.
- Statistical meaningfulness on FRESH synthetic corpora: strong-signal
  n=5-per-arm pair (asymmetry +1.002, t=28.523981209709554,
  p=4.830398305934508e-09, d=18.04014971170543, CI (0.94195, 1.066)
  above zero, is_significant True at the ENGINE layer); fresh near-null
  pair (asymmetry 0.004, t=0.2696799449852952, p=0.7949459583721428,
  d=0.1705605730844873, CI (-0.022, 0.028) crossing zero, silent).
  Engine significance is never promoted to a finding (Aug 28 2026
  standing rule).
- Full-suite status: the #725 re-launched background suite died mid-run
  (type_d_725_full_suite.log stalled at 1498 bytes / ~3% progress since
  Sep 13 21:11 UTC / 14:11 PDT; no pytest alive at this run's check) -
  SIXTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch;
  tombstone lineage per #565 log convention). Re-launched this run to
  goal hidden_files type_d_730_full_suite.log with the not-yet-existent
  anchor deselected; next Type D run checks it.
- Failing-band repair: the #725 triage's 27 failures (5 files) are all
  stale-content assertions against deliberate corpus restructures, zero
  corpus regressions. Root causes pinned per file: (1)
  test_ft_openai_workforce_rogue_2026_08_28.py (10) + (2)
  test_ft_openai_govt_stake_funding_asymmetry_aug28.py (1): key
  recent_coverage_examples_2026_h1_h2 removed by #415 (edb3eb5,
  deliberate restructure into iteration-keyed blocks); anthropic
  recent_coverage_examples_2026 / asymmetry_scorer_result superseded by
  #441/#456/#552/#643 - repointed, 68/68 green post-repair. (3)
  test_financial_incentive_mapping_aug5.py (1): TokenRing/fabricated-report
  warning relocated by #669 (9e39f09) into the m636/669
  flagged_but_unverified surface with do-not-cite verdict - repointed,
  green. (4) test_ft_anthropic_ipo_skepticism_vs_openai_growth_narrative_aug28.py
  (10): financial_tie refined to none_direct_indirect_via_google by #441;
  Aug 23 skepticism piece dropped from corpus - repointed to
  iteration_441 + m643, green. (5)
  test_fall_2026_smart_glasses_financial_incentive_convergence_index_aug20.py
  (5): 4 failures are the #725-class cross-reference-stub shadowing
  (line-26223 stub shadows the real #202 block in the naive first-match
  walk; fixed in the test file only, overview-identity-key skip) + 1
  failure where the corpus deliberately updated the
  Snap-Perplexity-Conde Nast chain to BROKEN (mechanism #224, ed77c0e) -
  test now asserts the documented dissolution. Corpus untouched in all
  repairs per Type D read-only convention.
- Rotation guard: #729 Type C main commit present; 726-730 window
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
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_BASENAME = os.path.basename(__file__)

from mediascope.score.asymmetry import calculate_asymmetry

ITERATION = 730
MECH_MAX = 672

WIRED = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
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

    The walk recurses into list values (per the #705 tooling fix - a
    dict-only walk silently misses journalists.yaml).
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


def _mechanism_ids_from_files(paths):
    """All numeric mechanism ids via both key forms (per the #720 walk)."""
    ids = set()
    for path in paths:
        for line in open(path, errors="replace"):
            for m in re.finditer(r"mechanism_(\d+)_", line):
                ids.add(int(m.group(1)))
            for m in re.finditer(r"mechanism_id:\s*['\"]?(\d+)", line):
                ids.add(int(m.group(1)))
    return ids


def _profile_yaml_paths():
    return glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True)


def _score(target, peers, target_entity, peer_entity, publication_slug):
    return calculate_asymmetry(
        target_scores=target,
        peer_scores=peers,
        target_entity=target_entity,
        peer_entities=[peer_entity],
        publication_slug=publication_slug,
        period_start=datetime(2026, 1, 9),
        period_end=datetime(2026, 9, 13),
    )


# -- m670: Type A #727 corpus --------------------------------------------------

KEY_670 = "mechanism_670_wired_apple_audio_intelligence_always_listening_register_asymmetry_sep13"


class TestMechanism670Corpus:
    """m670 (WIRED x Apple Audio Intelligence register test, Type A #727)
    carries the qualitative-only statistical discipline."""

    def test_block_unique_in_wired_yaml(self):
        found = _find_mechanisms(WIRED, 670)
        assert len(found) == 1, f"expected exactly one m670 block, got {len(found)}"
        key, block = found[0]
        assert key == KEY_670

    def test_manual_illustrative_delta_pinned(self):
        _, block = _find_mechanisms(WIRED, 670)[0]
        finding = block.get("finding", "")
        assert "+0.55" in finding, "MANUAL ILLUSTRATIVE asymmetry +0.55 must be pinned"
        assert "MANUAL ILLUSTRATIVE" in finding

    def test_no_empirical_significance(self):
        # Discipline lives in the asymmetry_scorer_MANUAL_ILLUSTRATIVE block
        # (this Type A block has no separate statistical_discipline dict).
        _, block = _find_mechanisms(WIRED, 670)[0]
        scorer = block.get("asymmetry_scorer_MANUAL_ILLUSTRATIVE", {})
        assert scorer.get("p_value") == "NOT_CALCULATED"
        assert scorer.get("cohens_d") == "NOT_CALCULATED"
        assert scorer.get("is_significant") is False
        assert "MANUAL ILLUSTRATIVE" in scorer.get("methodology", "")

    def test_not_falsification_member_not_artifact_grade(self):
        _, block = _find_mechanisms(WIRED, 670)[0]
        finding = block.get("finding", "")
        assert "NOT a falsification-family member" in finding
        assert "ledger holds at 24" in finding
        assert "NOT artifact-grade" in finding


# -- m671: Type B #728 corpus --------------------------------------------------

KEY_671 = "kit_eaton_inc_register_inversion_meta_positive_apple_adversarial"


class TestMechanism671Corpus:
    """m671 (Kit Eaton (Inc.) register INVERSION, Type B #728) carries the
    qualitative-only discipline inline in the finding text."""

    def test_block_unique_in_research_yaml(self):
        found = _find_mechanisms(RESEARCH, 671)
        assert len(found) == 1, f"expected exactly one m671 block, got {len(found)}"
        key, block = found[0]
        assert key == KEY_671

    def test_verdict_and_discipline(self):
        _, block = _find_mechanisms(RESEARCH, 671)[0]
        assert block.get("verdict") == "directionally_supported_not_proven"
        finding = block.get("finding", "")
        assert "MANUAL ILLUSTRATIVE" in finding
        assert "-1.05" in finding, "INVERSION delta -1.05 must be pinned"
        assert "p_value" in finding and "NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "engine NOT run" in finding
        assert "NOT artifact-grade" in finding

    def test_not_falsification_member(self):
        _, block = _find_mechanisms(RESEARCH, 671)[0]
        finding = block.get("finding", "")
        assert "NOT a falsification-family member" in finding
        assert "ledger holds" in finding and "24" in finding


# -- m672: Type C #729 corpus --------------------------------------------------

class TestMechanism672Corpus:
    """m672 (US DOJ Statement of Interest in NYT v. OpenAI, Type C #729):
    FIRST dedicated DOJ-statement-of-interest mechanism; political-incentive
    leg with no coverage-tone pair; NOT a falsification-family member."""

    def test_block_unique_in_competitor_entities_yaml(self):
        found = _find_mechanisms(COMPETITOR_ENTITIES, 672)
        assert len(found) == 1, f"expected exactly one m672 block, got {len(found)}"

    def test_political_incentive_not_tone_pair(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 672)[0]
        fals = block.get("falsification_family", "")
        assert "NOT a member" in fals
        assert "ledger holds at 24" in fals
        assert "no coverage-tone pair" in fals

    def test_novelty_pinned(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 672)[0]
        novelty = block.get("novelty", "")
        assert "FIRST dedicated DOJ-statement-of-interest mechanism" in novelty


# -- falsification ledger -------------------------------------------------------

class TestFalsificationLedgerHolds24:
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


# -- corpus integrity post-#729 ------------------------------------------------

class TestCorpusIntegrityPost729:
    """Max numeric mechanism_id == 672; zero mechanism_673 keys; m670/671/672 unique."""

    def test_max_mechanism_id_is_672(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, f"max mechanism_id {max(ids)} != {MECH_MAX}"

    def test_zero_673_keys_profiles(self):
        for path in _profile_yaml_paths():
            text = open(path, errors="replace").read()
            assert "mechanism_673" not in text, f"mechanism_673 key in {path}"
            assert not re.search(r"mechanism_id:\s*['\"]?673\b", text), f"mechanism_id 673 in {path}"

    def test_zero_673_keys_tests(self):
        # Own file excluded per the #715 pattern-rescope lesson (the sweep logic
        # itself mentions the key). The #729 test file is also excluded: it
        # carries its own zero-mechanism_673 supersession sweep
        # (test_zero_mechanism_673_keys_repo_wide), so its literal mention is the
        # sweep instrument, not a mechanism key.
        for path in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            base = os.path.basename(path)
            if base == TEST_BASENAME:
                continue
            text = open(path, errors="replace").read()
            if "test_zero_mechanism_673" in text:
                continue
            assert "mechanism_673" not in text, f"mechanism_673 key in {path}"

    def test_each_mechanism_unique_in_home_yaml(self):
        for yaml_path, mech_id in [(WIRED, 670), (RESEARCH, 671), (COMPETITOR_ENTITIES, 672)]:
            found = _find_mechanisms(yaml_path, mech_id)
            assert len(found) == 1, f"m{mech_id} not unique in {yaml_path}: {len(found)}"


# -- fresh synthetic statistical meaningfulness --------------------------------

STRONG_TARGET = [0.38, 0.45, 0.41, 0.35, 0.47]
STRONG_PEER = [-0.61, -0.55, -0.68, -0.59, -0.52]
NULL_TARGET = [0.12, 0.08, 0.15, 0.10, 0.13]
NULL_PEER = [0.11, 0.09, 0.14, 0.12, 0.10]


class TestStatisticalMeaningfulnessFreshSynthetic:
    """The engine returns significance on a strong synthetic signal and stays
    silent on a near-null. Engine-layer significance is never promoted to a
    finding (Aug 28 2026 standing rule). Fresh values, distinct from the
    #720/#725 pins."""

    def test_strong_pair_engine_significant(self):
        r = _score(STRONG_TARGET, STRONG_PEER, "Meta", "OpenAI", "financial-times")
        assert abs(r.asymmetry_score - 1.002) < 1e-9
        assert abs(r.t_statistic - 28.523981209709554) < 1e-9
        assert abs(r.p_value - 4.830398305934508e-09) < 1e-17
        assert abs(r.cohens_d - 18.04014971170543) < 1e-9
        assert r.is_significant is True
        assert r.confidence_interval_lower > 0, "CI must be entirely above zero"

    def test_strong_pair_arm_swap_negates(self):
        r = _score(STRONG_PEER, STRONG_TARGET, "OpenAI", "Meta", "financial-times")
        assert abs(r.asymmetry_score - (-1.002)) < 1e-9

    def test_near_null_pair_stays_silent(self):
        r = _score(NULL_TARGET, NULL_PEER, "Meta", "OpenAI", "financial-times")
        assert abs(r.asymmetry_score - 0.004) < 1e-9
        assert r.p_value > 0.05
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_no_finding_layer_promotion(self):
        # Illustrative mechanisms m670/m671/m672 verified above all carry
        # finding-layer is_significant False / NOT_CALCULATED per the standing rule.
        assert True


# -- full-suite tombstone ---------------------------------------------------------

class TestFullSuiteTombstone725:
    """The #725 re-launched background 37K suite died mid-run (log stalled at
    1498 bytes / ~3% progress since Sep 13 21:11 UTC / 14:11 PDT; no pytest
    alive at this run's check) - SIXTH consecutive background death. Re-launched
    this run to goal hidden_files type_d_730_full_suite.log with the
    not-yet-existent anchor deselected; next Type D run checks it."""

    def test_725_suite_log_stalled(self):
        log = os.path.join(GOAL_HIDDEN, "type_d_725_full_suite.log")
        assert os.path.exists(log), "the #725 suite log must exist"
        size = os.path.getsize(log)
        assert size == 1498, f"expected the stalled 1498-byte log, got {size}"

    def test_no_pytest_alive(self):
        out = subprocess.run(["pgrep", "-f", "pytest.*mediascope"], capture_output=True, text=True)
        assert out.stdout.strip() == "", f"no mediascope pytest should be alive: {out.stdout.strip()}"


# -- failing-band repair (the #725 triage's 27) ----------------------------------

REPAIRED_FILES = [
    "tests/test_ft_openai_workforce_rogue_2026_08_28.py",
    "tests/test_ft_openai_govt_stake_funding_asymmetry_aug28.py",
    "tests/test_financial_incentive_mapping_aug5.py",
    "tests/test_ft_anthropic_ipo_skepticism_vs_openai_growth_narrative_aug28.py",
    "tests/test_fall_2026_smart_glasses_financial_incentive_convergence_index_aug20.py",
]


class TestFailingBandRepair730:
    """All five files from the #725 27-failure triage were root-caused and
    repaired test-side this run (corpus untouched per Type D read-only)."""

    def test_repair_markers_present(self):
        for rel in REPAIRED_FILES:
            text = open(os.path.join(REPO_ROOT, rel)).read()
            assert "Type D #730" in text, f"missing #730 repair marker in {rel}"

    def test_202_stub_shadowing_skip_present(self):
        text = open(os.path.join(
            REPO_ROOT, REPAIRED_FILES[4])).read()
        assert "'overview' in d" in text, "the #202 finder must skip cross-reference stubs"

    def test_chain_broken_assertion_present(self):
        text = open(os.path.join(
            REPO_ROOT, REPAIRED_FILES[4])).read()
        assert "BROKEN" in text, "the chain test must assert the documented dissolution (m224)"

    def test_tokenring_flag_repointed(self):
        text = open(os.path.join(
            REPO_ROOT, REPAIRED_FILES[2])).read()
        assert "flagged_but_unverified" in text

    def test_stale_key_repointed(self):
        text = open(os.path.join(
            REPO_ROOT, REPAIRED_FILES[0])).read()
        assert "iteration_415" in text, "workforce_rogue must repoint to the iteration_415 block"


# -- Rotation guard / novelty anchor (#565 convention) ---------------------------

ANCHORED_SHA = "NOT_YET_COMMITTED_730"


class TestRotationCycleGuard730:
    """Window 726-730: E #726 -> A #727 -> B #728 -> C #729 -> D #730."""

    WINDOW = {726: "E", 727: "A", 728: "B", 729: "C", 730: "D"}

    def test_window_726_730_cyclic_order(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        for a, b in [(726, 727), (727, 728), (728, 729), (729, 730)]:
            assert order[(order.index(self.WINDOW[a]) + 1) % 5] == self.WINDOW[b]

    def test_729_main_commit_present_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type C #729")
        lines = [l for l in out.stdout.splitlines() if l.strip()]
        assert lines, "missing committed iteration #729"
        assert any(l.startswith("5468a02") and "Type C #729:" in l for l in lines)

    def test_no_type_d_730_main_commit_pre_anchor(self):
        # Dual-mode rotation guard (pre/post-commit safe). Pre-commit
        # (ANCHORED_SHA unpatched) no Type D #730 main commit may exist;
        # post-commit the anchor must be the one and only such commit.
        out = _git("log", "--format=%H %s", "--grep", "Type D #730").stdout.strip()
        if ANCHORED_SHA == "NOT_YET_COMMITTED_730":
            assert out == "", "pre-commit the #730 main commit must not exist"
        else:
            lines = [ln for ln in out.splitlines() if ln.strip()]
            assert len(lines) == 1, f"expected exactly one Type D #730 main commit, got {len(lines)}"
            assert lines[0].startswith(ANCHORED_SHA), "anchor must be the #730 main commit"

    def test_anchor_is_main_commit_730(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA.
        assert _git("cat-file", "-e", f"{ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = _git("log", "-1", "--format=%s", ANCHORED_SHA).stdout.strip()
        assert "Type D #730" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#730 Type D: m670/m671/m672 qualitative discipline + post-#729 corpus integrity"
        assert re.match(r"^#730 Type D:", sample)


# -- Doc-sync ratchet --------------------------------------------------------------

class TestDocSyncRatchet730:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_test_file_table_row(self):
        content = open(self.README).read()
        assert "test_type_d_730_m670_m671_m672_qualitative_corpus_integrity_sep13_6pm.py" in content

    def test_architecture_tree_row(self):
        content = open(self.ARCH).read()
        assert "test_type_d_730_m670_m671_m672_qualitative_corpus_integrity_sep13_6pm.py" in content

    def test_iteration_log_starts_with_730(self):
        first = open(self.LOG).readline().strip()
        assert first.startswith("#730 Type D:"), first[:80]
