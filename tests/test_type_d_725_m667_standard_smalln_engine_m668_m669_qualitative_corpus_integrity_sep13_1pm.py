"""
Type D -- Iteration #725 (Sun 2026-09-13 13:00 PDT): m667 standard-path
small-n engine verification (n=2-per-arm, non-degenerate; FIRST standard-path
pin in the degenerate-boundary family, with an engine-method CI/p divergence
note) + m668 / m669 qualitative discipline + post-#724 corpus integrity
(max mechanism_id 669; zero mechanism_670 keys; ledger holds at 24) +
#720 background-suite tombstone (FIFTH consecutive death; re-launched as
type_d_725_full_suite.log) + failing-band repair (digital_trends #138
cross-reference-stub shadowing, fixed in the Aug 16 test file).

Verifies:
- m667 (The Atlantic x Google adversarial-posture litigation-domain boundary
  replication, Type A #722): pinned arms google_target_tones [-0.45, -0.1]
  vs meta_peer_tones [-0.75, -0.65], delta_target_minus_peer 0.425, reproduce
  through the real calculate_asymmetry path: asymmetry 0.425 within 1e-9,
  arm-swap negates to -0.425 exactly, t=2.335129587127713,
  p=0.22875802201216047 (> 0.05), d=2.335129587127713, is_significant False.
  FIRST standard-path small-n engine pin: both arms n=2 with non-zero
  variance, so the engine runs a real small-n t (df=2), not the degenerate
  contract. Engine-method divergence note (pinned, not a finding): the
  seeded bootstrap CI (0.2, 0.65) excludes zero while the t-test p says not
  significant - the engine's two inference methods disagree on n=2 arms.
  NOT a falsification-family member (ledger holds at 24); boundary family
  2->3 (cross-refs 471, 592).
- m668 (Cherlynn Low Engadget Apple Audio Intelligence control-case
  replication, Type B #723): qualitative-only discipline - p_value /
  cohens_d / ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
  NOT artifact-grade, no engine divergence pin; NULL differential 0.00;
  NOT a falsification-family member (ledger holds at 24).
- m669 (Meta x Newsmax AI content partnership ideology-bundle leg,
  Type C #724): qualitative-only statistical_discipline (scorer none,
  tone NOT_SCORED, qualitative_only True, no_coverage_tone_claim True,
  is_significant False, artifact_grade False); NOT a falsification-family
  member (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#724 corpus integrity: max numeric mechanism_id == 669 in
  profiles/; zero mechanism_670 keys in profiles/ and tests/ (own file
  excluded per the #715 pattern-rescope lesson); m667 / m668 / m669 each
  unique in their home YAML.
- Statistical meaningfulness on FRESH synthetic corpora: strong-signal
  n=5-per-arm pair (asymmetry +0.938, t=23.36255407703707,
  p=1.3660280245326916e-08, d=14.775776568458006, CI (0.872, 1.00805)
  above zero, is_significant True at the ENGINE layer); fresh near-null
  pair (asymmetry 0.002, t=0.05568460463897036, p=0.9569586616025966,
  d=0.035218036253024894, CI (-0.06405, 0.06005) crossing zero, silent).
  Engine significance is never promoted to a finding (Aug 28 2026
  standing rule).
- Full-suite status: the #720 re-launched background suite died mid-run
  (log stalled at 11954 bytes / 28% progress since Sep 13 17:36 UTC /
  10:36 PDT with 63 failures clustered in the 10-28% band; no pytest
  alive at this run's check) - FIFTH consecutive background death
  (#705's, #710's, #715's first re-launch, #715's re-launch, #720's
  re-launch; tombstone lineage per #565 log convention). Re-launched
  this run to goal hidden_files type_d_725_full_suite.log with the
  not-yet-existent anchor deselected; next Type D run checks it.
- Failing-band repair: the #720 suite's 63-failure cluster traced to
  tests/test_digital_trends_editorial_level_privacy_vocabulary_asymmetry_aug16.py
  (mechanism #138): commit 968b4f5 (2026-08-17 07:10 UTC, Mechanism #145)
  added a cross-reference stub {- mechanism_id: 138, relationship: ...}
  earlier in competitor-coverage-research.yaml, shadowing the real block
  in the test's naive first-match find_mechanism walk -> 22 failures.
  Fixed in the test file only (stub dicts skipped unless they carry
  mechanism_name); 37/37 green. Corpus untouched per Type D read-only
  convention.
- Rotation guard: #724 Type C main commit present; 721-725 window
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

ITERATION = 725
MECH_MAX = 669

ATLANTIC = os.path.join(REPO_ROOT, "profiles", "atlantic.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
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


# -- m667: Type A #722 corpus -------------------------------------------------

KEY_667 = "mechanism_667_atlantic_google_adversarial_posture_litigation_domain_boundary_replication_sep13"
GOOGLE_ARM_667 = [-0.45, -0.1]
META_ARM_667 = [-0.75, -0.65]
DELTA_667 = 0.425


class TestMechanism667Corpus:
    """The m667 block schema as authored by Type A #722 (read-only)."""

    def test_mechanism_667_present_once_in_atlantic(self):
        found = _find_mechanisms(ATLANTIC, 667)
        assert len(found) == 1, f"m667 must be unique, got {len(found)}"
        key, _ = found[0]
        assert key == KEY_667

    def test_mechanism_667_key_form_unique_in_profiles(self):
        hits = []
        for path in _profile_yaml_paths():
            for line in open(path, errors="replace"):
                if "mechanism_667_" in line:
                    hits.append((path, line.strip()[:80]))
        assert len(hits) == 1, hits

    def test_google_arm_tones_pinned(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        tc = block["tone_comparison"]
        assert tc["google_target_tones_MANUAL_ILLUSTRATIVE"] == GOOGLE_ARM_667
        assert tc["google_target_avg"] == -0.275

    def test_meta_arm_tones_pinned(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        tc = block["tone_comparison"]
        assert tc["meta_peer_tones_MANUAL_ILLUSTRATIVE"] == META_ARM_667
        assert tc["meta_peer_avg"] == -0.7

    def test_delta_pinned_0425(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        tc = block["tone_comparison"]
        assert tc["delta_target_minus_peer_MANUAL_ILLUSTRATIVE"] == DELTA_667

    def test_tone_comparison_discipline_keys(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        tc = block["tone_comparison"]
        assert tc["p_value"] == "NOT_CALCULATED"
        assert tc["cohens_d"] == "NOT_CALCULATED"
        assert tc["ci_95"] == "NOT_CALCULATED"
        assert tc["is_significant"] is False
        assert tc["artifact_grade"] is False
        assert tc["engine_run"] is False
        assert tc["engine_divergence_pin"] is False

    def test_not_falsification_member(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        assert "NOT a falsification-family member" in block["finding"]

    def test_boundary_family_pin(self):
        _, block = _find_mechanisms(ATLANTIC, 667)[0]
        assert "THIRD" in block["finding"]
        # cross_references are descriptive strings ("mechanism 471 (NYT x OpenAI
        # adversarial-posture boundary pin, FIRST)", ...), not raw ints -
        # assert on content, not membership (fixed post-first-run; the pins are
        # FIRST=471, SECOND=592, THIRD=667).
        refs = " ".join(str(r) for r in block["cross_references"])
        assert "471" in refs
        assert "592" in refs


# -- m667: standard-path small-n engine verification ---------------------------

class TestMechanism667EngineStandardPath:
    """FIRST standard-path small-n engine pin in the degenerate-boundary
    family: both arms n=2 with non-zero variance, so the engine runs a real
    small-n t (df=2), not the degenerate n=1 contract of #705/#710/#715/#720.
    """

    def test_asymmetry_matches_pinned_delta(self):
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert abs(r.asymmetry_score - DELTA_667) < 1e-9

    def test_arm_swap_negates_exactly(self):
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        r2 = _score(META_ARM_667, GOOGLE_ARM_667, "meta", "google", "the-atlantic")
        assert abs(r2.asymmetry_score - (-DELTA_667)) < 1e-9
        assert r2.asymmetry_score == -r.asymmetry_score

    def test_t_statistic_pinned(self):
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert abs(r.t_statistic - 2.335129587127713) < 1e-9

    def test_p_above_alpha_not_significant(self):
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert abs(r.p_value - 0.22875802201216047) < 1e-9
        assert r.p_value > 0.05
        assert r.is_significant is False

    def test_cohens_d_pinned(self):
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert abs(r.cohens_d - 2.335129587127713) < 1e-9

    def test_standard_path_not_degenerate(self):
        # The degenerate contract pins t=0.0; here both arms carry variance
        # so the engine computes a real t.
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert r.t_statistic != 0.0
        assert r.article_count_target == 2
        assert r.article_count_peers == 2

    def test_ci_p_divergence_note(self):
        # Engine-method divergence, pinned as method arithmetic NOT a finding:
        # the seeded bootstrap CI excludes zero while the t-test p says not
        # significant. On n=2 arms the engine's two inference methods disagree.
        r = _score(GOOGLE_ARM_667, META_ARM_667, "google", "meta", "the-atlantic")
        assert abs(r.confidence_interval_lower - 0.2) < 1e-9
        assert abs(r.confidence_interval_upper - 0.65) < 1e-9
        assert r.confidence_interval_lower > 0 and r.p_value > 0.05


# -- m668: Type B #723 qualitative discipline ----------------------------------

KEY_668 = "cherlynn_low_engadget_apple_audio_intelligence_control_replication"


class TestMechanism668Qualitative:
    """m668 carries no asymmetry scorer keys (Type D read-only)."""

    def test_mechanism_668_present_once(self):
        found = _find_mechanisms(RESEARCH, 668)
        assert len(found) == 1, f"m668 must be unique, got {len(found)}"
        key, _ = found[0]
        assert key == KEY_668

    def test_journalist_and_iteration_pinned(self):
        _, block = _find_mechanisms(RESEARCH, 668)[0]
        assert block["journalist"] == "Cherlynn Low"
        assert block["iteration"] == 723
        assert block["publication"] == "Engadget (Yahoo/Apollo)"
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_null_differential_pinned(self):
        _, block = _find_mechanisms(RESEARCH, 668)[0]
        assert "0.00" in block["finding"]
        assert "NULL" in block["finding"]

    def test_no_engine_discipline(self):
        _, block = _find_mechanisms(RESEARCH, 668)[0]
        finding = block["finding"]
        assert "p_value NOT_CALCULATED" in finding
        assert "cohens_d NOT_CALCULATED" in finding
        assert "ci_95 NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "engine NOT" in finding
        assert "NOT artifact-grade" in finding
        assert "no engine divergence pin" in finding

    def test_not_falsification_member(self):
        _, block = _find_mechanisms(RESEARCH, 668)[0]
        assert "NOT a falsification-family member" in block["finding"]


# -- m669: Type C #724 qualitative discipline ----------------------------------

KEY_669 = "newsmax_meta_ai_content_partnership_jul2026"


class TestMechanism669Qualitative:
    """m669 statistical_discipline contract (Type D read-only)."""

    def test_mechanism_669_present_once(self):
        found = _find_mechanisms(COMPETITOR_ENTITIES, 669)
        assert len(found) == 1, f"m669 must be unique, got {len(found)}"
        key, _ = found[0]
        assert key == KEY_669

    def test_statistical_discipline_contract(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 669)[0]
        sd = block["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["qualitative_only"] is True
        assert sd["no_coverage_tone_claim"] is True
        assert sd["is_significant"] is False
        assert sd["artifact_grade"] is False

    def test_wearables_scope_pinned(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 669)[0]
        assert "smart glasses" in block["deal_terms"]["wearables_scope"]

    def test_not_falsification_member(self):
        _, block = _find_mechanisms(COMPETITOR_ENTITIES, 669)[0]
        text = str(block["novelty_verification"])
        assert "NOT a falsification-family member" in text
        assert "ledger stays at 24" in text


# -- Falsification ledger ------------------------------------------------------

class TestFalsificationLedgerHolds24:
    """TWENTY-FOURTH present, TWENTY-FIFTH absent anywhere in profiles/."""

    def _corpus(self):
        corpus = ""
        for path in _profile_yaml_paths():
            corpus += open(path, errors="replace").read()
        return corpus

    def test_twenty_fourth_present_in_profiles(self):
        assert "TWENTY-FOURTH" in self._corpus()

    def test_twenty_fifth_absent_in_profiles(self):
        assert "TWENTY-FIFTH" not in self._corpus()

    def test_no_new_ordinal_in_new_blocks(self):
        for yaml_path, mech_id in [(ATLANTIC, 667), (RESEARCH, 668),
                                   (COMPETITOR_ENTITIES, 669)]:
            _, block = _find_mechanisms(yaml_path, mech_id)[0]
            assert "TWENTY-FIFTH" not in str(block)


# -- Corpus integrity post-#724 -----------------------------------------------

class TestCorpusIntegrityPost724:
    """Max mechanism_id 669; zero 670 keys; 667/668/669 unique."""

    def test_max_mechanism_id_is_669(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, max(ids)

    def test_zero_mechanism_670_keys_in_profiles(self):
        for path in _profile_yaml_paths():
            for line in open(path, errors="replace"):
                assert "mechanism_670_" not in line, (path, line.strip()[:80])
                m = re.search(r"mechanism_id:\s*['\"]?(\d+)", line)
                assert not (m and int(m.group(1)) == 670), (path, line.strip()[:80])

    def test_zero_mechanism_670_keys_in_tests(self):
        for path in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if os.path.basename(path) == TEST_BASENAME:
                continue  # own file excluded per the #715 pattern-rescope lesson
            for line in open(path, errors="replace"):
                assert "mechanism_670_" not in line, (path, line.strip()[:80])
                m = re.search(r"mechanism_id:\s*['\"]?(\d+)", line)
                assert not (m and int(m.group(1)) == 670), (path, line.strip()[:80])

    def test_667_668_669_each_unique(self):
        for mech_id, yaml_path in [(667, ATLANTIC), (668, RESEARCH), (669, COMPETITOR_ENTITIES)]:
            found = _find_mechanisms(yaml_path, mech_id)
            assert len(found) == 1, f"mechanism {mech_id} must be unique"


# -- Statistical meaningfulness on fresh synthetic corpora ----------------------

class TestStatisticalMeaningfulnessFreshSynthetic:
    """The statistical-meaningfulness mandate on FRESH arrays (never the
    corpus pins): a strong-signal n=5-per-arm pair is significant at the
    ENGINE layer; a near-null pair stays silent. Per the Aug 28 2026
    standing rule, engine significance on synthetic illustrative arrays
    is NEVER promoted to a finding - the finding layer stays
    is_significant False for all three illustrative mechanisms verified
    above."""

    STRONG_TARGET = [0.41, 0.36, 0.48, 0.33, 0.44]
    STRONG_PEER = [-0.57, -0.49, -0.62, -0.54, -0.45]
    NULL_TARGET = [0.06, -0.04, 0.02, -0.07, 0.05]
    NULL_PEER = [-0.03, 0.08, -0.02, 0.04, -0.06]

    def test_strong_pair_engine_significant(self):
        r = _score(self.STRONG_TARGET, self.STRONG_PEER, "t", "p", "synthetic")
        assert abs(r.asymmetry_score - 0.938) < 1e-9
        assert abs(r.t_statistic - 23.36255407703707) < 1e-9
        assert abs(r.p_value - 1.3660280245326916e-08) < 1e-9
        assert abs(r.cohens_d - 14.775776568458006) < 1e-9
        assert r.is_significant is True

    def test_strong_pair_ci_above_zero(self):
        r = _score(self.STRONG_TARGET, self.STRONG_PEER, "t", "p", "synthetic")
        assert abs(r.confidence_interval_lower - 0.872) < 1e-9
        assert abs(r.confidence_interval_upper - 1.00805) < 1e-9
        assert r.confidence_interval_lower > 0

    def test_near_null_pair_stays_silent(self):
        r = _score(self.NULL_TARGET, self.NULL_PEER, "t", "p", "synthetic")
        assert abs(r.asymmetry_score - 0.002) < 1e-9
        assert abs(r.t_statistic - 0.05568460463897036) < 1e-9
        assert abs(r.p_value - 0.9569586616025966) < 1e-9
        assert abs(r.cohens_d - 0.035218036253024894) < 1e-9
        assert r.is_significant is False

    def test_near_null_pair_ci_crosses_zero(self):
        r = _score(self.NULL_TARGET, self.NULL_PEER, "t", "p", "synthetic")
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_engine_significance_not_promoted_to_finding(self):
        # Discipline: the three illustrative mechanisms verified above all
        # carry finding-layer is_significant False / NOT_CALCULATED.
        _, b667 = _find_mechanisms(ATLANTIC, 667)[0]
        assert b667["tone_comparison"]["is_significant"] is False
        _, b668 = _find_mechanisms(RESEARCH, 668)[0]
        assert "is_significant False" in b668["finding"]
        _, b669 = _find_mechanisms(COMPETITOR_ENTITIES, 669)[0]
        assert b669["statistical_discipline"]["is_significant"] is False


# -- Full-suite tombstone: #720's re-launch ------------------------------------

class TestFullSuiteTombstone720:
    """#720's re-launched 37K background suite died mid-run: log stalled at
    11954 bytes / 28% progress since Sep 13 17:36 UTC (10:36 PDT) with a
    63-failure cluster in the 10-28% band; no pytest alive at this run's
    check. FIFTH consecutive background death (#705's, #710's, #715's first
    re-launch, #715's re-launch, #720's re-launch; tombstone lineage per
    #565 log convention)."""

    LOG720 = os.path.join(GOAL_HIDDEN, "type_d_720_full_suite.log")
    LOG725 = os.path.join(GOAL_HIDDEN, "type_d_725_full_suite.log")

    def test_720_relaunch_log_exists(self):
        assert os.path.exists(self.LOG720)

    def test_720_suite_died_mid_run(self):
        size = os.path.getsize(self.LOG720)
        # Stalled at 11954 bytes / 28%: advanced past #715's 3680-byte death
        # line but never finished the ~38K-test suite.
        assert 10000 < size < 20000, f"unexpected suite size, size={size}"
        tail = open(self.LOG720, errors="replace").read()[-200:]
        assert "[ 28%]" in tail
        content = open(self.LOG720, errors="replace").read()
        assert content.count("F") >= 60, "the 63-failure cluster must be on record"

    def test_720_no_pytest_alive(self):
        out = subprocess.run(["pgrep", "-f", "pytest.*type_d_720"],
                             capture_output=True, text=True)
        assert out.stdout.strip() == "", "a #720 pytest is unexpectedly alive"

    def test_725_relaunch_log_created(self):
        assert os.path.exists(self.LOG725), (
            "the 725 re-launched background suite log must exist (launched pre-commit)"
        )


# -- Rotation guard / novelty anchor (#565 convention) ---------------------------

ANCHORED_SHA = "NOT_YET_COMMITTED_725"


class TestRotationCycleGuard725:
    """Window 721-725: E #721 -> A #722 -> B #723 -> C #724 -> D #725."""

    WINDOW = {721: "E", 722: "A", 723: "B", 724: "C", 725: "D"}

    def test_window_721_725_cyclic_order(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        for a, b in [(721, 722), (722, 723), (723, 724), (724, 725)]:
            assert order[(order.index(self.WINDOW[a]) + 1) % 5] == self.WINDOW[b]

    def test_724_main_commit_present_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type C #724")
        lines = [l for l in out.stdout.splitlines() if l.strip()]
        assert lines, "missing committed iteration #724"
        assert any(l.startswith("d1455ed") and "Type C #724:" in l for l in lines)

    def test_no_type_d_725_main_commit_pre_anchor(self):
        out = _git("log", "--oneline", "--grep", "Type D #725")
        assert out.stdout.strip() == "", "pre-commit the #725 main commit must not exist"

    def test_anchor_is_main_commit_725(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA.
        assert _git("cat-file", "-e", f"{ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = _git("log", "-1", "--format=%s", ANCHORED_SHA).stdout.strip()
        assert "Type D #725" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#725 Type D: m667 standard-path small-n engine verification + m668/m669 qualitative discipline + post-#724 corpus integrity"
        assert re.match(r"^#725 Type D:", sample)


class TestDocSyncRatchet725:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    README = os.path.join(REPO_ROOT, "README.md")
    ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO_ROOT, "iteration-log.md")

    def test_readme_test_file_table_row(self):
        content = open(self.README).read()
        assert "test_type_d_725_m667_standard_smalln_engine_m668_m669_qualitative_corpus_integrity_sep13_1pm.py" in content

    def test_architecture_tree_row(self):
        content = open(self.ARCH).read()
        assert "test_type_d_725_m667_standard_smalln_engine_m668_m669_qualitative_corpus_integrity_sep13_1pm.py" in content

    def test_iteration_log_starts_with_725(self):
        first = open(self.LOG).readline().strip()
        assert first.startswith("#725 Type D:"), first[:80]
