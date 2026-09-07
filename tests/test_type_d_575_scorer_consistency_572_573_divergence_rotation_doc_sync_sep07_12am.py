"""Type D #575 (2026-09-07 00:00 PDT): scorer cross-mechanism consistency
extended to #572/#573 (THIRD and FOURTH engine-significance/finding-layer
DIVERGENCE pins - the divergence count moves 2 -> 4: #552, #557, #572,
#573), #571 monitoring boundary, #574 qualitative boundary, 571-574
rotation guard (anchored at this run's commit via the #565 followup-commit
convention), 571-574 doc-sync ratchet (rows verified present with
authoritative counts), no-brittle sweep over the 571-574 window, new
competitor-coverage pattern tests for #572 (Atlantic x Apple
accountability-register exemption, first dedicated mechanism under
competitor_relationships.apple) and #573 (Patel Decoder interview-access
entity selection, first competitor_coverage block on Nilay Patel).

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are
NOT empirical - p_value NOT_CALCULATED, is_significant False in the
mechanism YAML, correlation not causation, no artifact-grade claims. The
asymmetry engine (calculate_asymmetry) computes t/p/CI on the logged
arrays, and its MEAN-DIFFERENCE arithmetic must reproduce the logged
manual delta (engine-drift detection). The engine's own significance
output is computed but deliberately NOT promoted to a finding for
illustrative inputs - this file pins that separation for the two newest
quantitative mechanisms, and pins the THIRD and FOURTH divergence:

- #572 (Type A, The Atlantic x Apple accountability-register exemption vs
  Meta AI Watchdog targeting, Sep 6 20:00 PDT): Apple target [-0.35,
  -0.25] avg -0.30 vs Meta peer [-0.75, -0.65] avg -0.70. Logged
  delta_manual_illustrative 0.40 (target-minus-peer: target softer than
  peer by 0.40). THIRD divergence pin: engine Welch p ~ 0.0299, d = 5.66,
  is_significant True, while the finding layer refuses (significant False,
  p_value NOT CALCULATED no observed corpus, empirical_required True).
  The mechanism is the first dedicated mechanism under
  competitor_relationships.apple in atlantic.yaml (previously only the
  financial stub: DUAL investment + platform revenue tie, coverage
  prediction softer). Verdict: directionally_supported_not_proven -
  register SELECTION, not tone magnitude - the first directional
  confirmation in the recent control run, against the falsification family
  (#552, #557, #562, #567) which stands as the contrasting pole.
- #573 (Type B, Nilay Patel The Verge Decoder CEO-interview entity
  selection, Sep 6 22:00 PDT): OpenAI target [-0.70, -0.60, -0.45] avg
  -0.5833 vs Meta peer [-0.20, -0.15, -0.15] avg -0.1667, logged
  delta_manual_illustrative -0.4167 (target harsher than peer by 0.42).
  FOURTH divergence pin: engine Welch p ~ 0.0243, d = -4.56,
  is_significant True, while the finding layer refuses (is_significant
  False, p_value/cohens_d/ci_95 NOT_CALCULATED, empirical_required True).
  The YAML engine_check block carries the engine outputs (asymmetry
  -0.4167, p 0.0243, d -4.56, is_significant True, divergence 'fourth
  engine/finding divergence'). Verdict falsified_softer_prediction: the
  deal partner (Vox-OpenAI strategic content and product partnership, May
  29 2024) absorbs the adversarial register on the owner's flagship
  interview show while $0-deal Meta gets recurring product-forward CEO
  sit-downs. Joins the falsification family; distinct from #498 (Swisher
  personal register) and mechanism #6 (EIC Delegation Paradox).
- #574 (Type C, Apple training-data purchasing architecture, Sep 6 23:00
  PDT): qualitative - no asymmetry_scorer section (statistical_discipline
  carries tone_scores NOT_SCORED, p_value NOT_CALCULATED); scorer
  consistency explicitly does NOT apply, mirroring the #554/#559/#564/#569
  boundary.
- #571 (Type E, podcast 37th verification, Sep 6 19:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Divergence ratchet: with #572 and #573 both pinned as divergence, the
engine-significance/finding-layer divergence count MOVES 2 -> 4 (#552 in
#555, #557 in #560, #572 and #573 here). This file spot-checks that the
two older divergence pins still hold (engine claims significance on the
illustrative inputs while the finding layer refuses), so the ratchet is
active rather than stale: a NEW divergence beyond the four in the 571-574
window would have been caught by the per-mechanism divergence assertions.

Sign-class separation: #572 (+0.40, directional-support register
exemption) vs #573 (-0.4167, target-harsher falsification). Opposite sign
classes; the suite must not conflate a directional confirmation with a
falsification. |#573| ~ 1.04x |#572| - near-equal magnitudes on opposite
sides of the prediction.

Also: a no-brittle sweep - none of the 571-574 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired in
#551 (all four use the presence-assertion convention); this pins the
convention against regression. Rotation guard: the 571 E -> 572 A -> 573 B
-> 574 C window follows A->B->C->D->E->A adjacency in git-commit order
(newest first), closing the C->D edge this run. Doc-sync ratchet: the
README/ARCHITECTURE per-file window for 571-574 was already synced by
their own runs (rows verified present with authoritative def-test counts
56/34/31/43); this run extends the window with its own row and verifies
the #570 row survives, with the authoritative count_stats.py --check gate.

Novelty: zero test_type_d_575 files on disk before this run (glob
verified); no #575 in git log (grep verified); scorer consistency has
never covered #572/#573 (repo grep for 572/573 in scorer-consistency test
files returned only their own mechanism files); the 571-574 rotation
window was never guarded; the 566-569 doc-sync window (from #565/#570) is
extended, not duplicated. The filename embeds the covered iteration
numbers (572_573) per the #555/#560/#565/#570 Type-D filename convention.
"""

from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TESTS_DIR = REPO_ROOT / "tests"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
LOG = REPO_ROOT / "iteration-log.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_575 = ("test_type_d_575_scorer_consistency_572_573_divergence_rotation_"
            "doc_sync_sep07_12am.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_572 = [-0.35, -0.25]
PEER_572 = [-0.75, -0.65]
TARGET_573 = [-0.70, -0.60, -0.45]
PEER_573 = [-0.20, -0.15, -0.15]


def score(target, peer, target_entity, peers, slug):
    return calculate_asymmetry(
        target_scores=list(target),
        peer_scores=list(peer),
        target_entity=target_entity,
        peer_entities=list(peers),
        publication_slug=slug,
        period_start=PERIOD[0],
        period_end=PERIOD[1],
    )


def count_def_tests(test_file):
    """Static def-test count, same definition count_stats.count_tests uses."""
    with open(REPO_ROOT / "tests" / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


def _mechanism_572():
    with open(REPO_ROOT / "profiles" / "atlantic.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["apple"][
        "mechanism_572_atlantic_apple_accountability_register_exemption_vs_"
        "meta_watchdog"]


def _load_patel():
    with open(REPO_ROOT / "profiles" / "careers" / "journalists.yaml") as f:
        data = yaml.safe_load(f)
    found = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("name") == "Nilay Patel":
                found.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    assert found, "Nilay Patel entry missing from journalists.yaml"
    return found[0]


def _cc_573():
    entry = _load_patel()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"]["cross_entity_analysis"]


def _mechanism_574():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["entities"]["apple"][
        "mechanism_574_apple_training_data_purchasing_architecture"]


# ---------------------------------------------------------------------------
# Iteration metadata
# ---------------------------------------------------------------------------


class TestIteration575Metadata:
    def test_docstring_ids(self):
        assert "Type D #575" in __doc__
        assert "572_573" in __doc__

    def test_rotation_c_to_d(self):
        # The rotation runs A->B->C->D->E->A; #574 was Type C at 23:00 PDT,
        # so this 00:00 PDT run is Type D, closing the C->D edge.
        assert "rotation 574 C -> 575 D" in LOG.read_text(encoding="utf-8")
        assert "Type D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name.startswith("test_type_d_575")

    def test_covered_iterations_in_filename(self):
        assert "572_573" in Path(__file__).name

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#575" in text
        assert "Type D" in text
        assert "Scorer Consistency" in text


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine arithmetic must reproduce the
# logged MANUAL ILLUSTRATIVE deltas for #572 and #573 (1e-4), and the
# qualitative/monitoring boundaries for #574 and #571 must hold.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency575:
    def test_572_delta_reproduced(self):
        r = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        assert abs(r.asymmetry_score - 0.40) < 1e-4

    def test_572_engine_sign_is_target_softer(self):
        r = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        assert r.asymmetry_score > 0

    def test_572_logged_avgs_match_engine(self):
        r = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        assert abs(r.target_avg_tone - (-0.30)) < 1e-4
        assert abs(r.peer_avg_tone - (-0.70)) < 1e-4

    def test_572_logged_arrays_byte_match_engine_inputs(self):
        sc = _mechanism_572()["asymmetry_scoring_manual_illustrative"]
        assert sc["target_scores_manual_illustrative"] == pytest.approx(
            TARGET_572, abs=1e-9)
        assert sc["peer_scores_manual_illustrative"] == pytest.approx(
            PEER_572, abs=1e-9)
        assert sc["delta_manual_illustrative"] == pytest.approx(
            0.40, abs=1e-4)
        assert sc["delta_direction"] == "target softer than peer by 0.40"

    def test_573_delta_reproduced(self):
        r = score(TARGET_573, PEER_573, "OpenAI", ["Meta"], "the_verge")
        assert abs(r.asymmetry_score - (-0.4167)) < 1e-4

    def test_573_logged_avgs_match_engine(self):
        r = score(TARGET_573, PEER_573, "OpenAI", ["Meta"], "the_verge")
        assert abs(r.target_avg_tone - (-0.5833)) < 1e-3
        assert abs(r.peer_avg_tone - (-0.1667)) < 1e-3

    def test_573_logged_arrays_byte_match_engine_inputs(self):
        sc = _cc_573()["scorer"]
        assert sc["target_scores"] == pytest.approx(TARGET_573, abs=1e-9)
        assert sc["peer_scores"] == pytest.approx(PEER_573, abs=1e-9)
        assert abs(sc["delta_manual_illustrative"] - (-0.4167)) < 1e-4
        assert sc["delta_direction"] == "target harsher than peer by 0.42"
        eng = sc["engine_check"]
        assert abs(eng["asymmetry"] - (-0.4167)) < 1e-4
        assert abs(eng["p_value"] - 0.0243) < 1e-3
        assert abs(eng["cohens_d"] - (-4.56)) < 1e-2
        assert eng["is_significant"] is True

    def test_574_qualitative_no_scorer(self):
        m = _mechanism_574()
        assert "asymmetry_scorer" not in m
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"

    def test_571_monitoring_no_scorer(self):
        # Type E 37th podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        fname = ("test_type_e_571_podcast_sentiment_thirtyseventh_"
                 "verification_sep06_7pm.py")
        assert (TESTS_DIR / fname).exists()
        assert count_def_tests(fname) == 56
        assert "Thirty-Seventh" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_572_and_573_sign_classes_distinct(self):
        # #572 is a positive target-softer directional confirmation
        # (register exemption for Apple vs watchdog targeting of Meta);
        # #573 is a negative target-harsher falsification (deal partner
        # absorbs the adversarial register). Opposite sign classes; the
        # suite must not conflate a confirmation with a falsification.
        r572 = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        r573 = score(TARGET_573, PEER_573, "OpenAI", ["Meta"], "the_verge")
        assert r572.asymmetry_score > 0 > r573.asymmetry_score
        # Near-equal magnitudes on opposite sides of the prediction.
        assert abs(abs(r572.asymmetry_score) - abs(r573.asymmetry_score)) \
            < 0.02


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #572 and #573 are the THIRD and FOURTH
# divergence pins (engine is_significant True on the synthetic illustrative
# arrays AND finding layer refuses). Divergence count moves 2 -> 4.
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet575:
    def test_572_engine_claims_significance(self):
        # THIRD divergence: the engine claims significance on the
        # illustrative pair (Welch p ~ 0.0299, d = 5.66). The YAML block
        # records the divergence explicitly (engine_divergence True,
        # engine_is_significant True).
        r = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        assert abs(r.p_value - 0.0299) < 1e-3
        assert abs(r.cohens_d - 5.66) < 1e-2
        assert r.is_significant is True
        sc = _mechanism_572()["asymmetry_scoring_manual_illustrative"]
        assert sc["engine_divergence"] is True
        assert sc["engine_is_significant"] is True

    def test_572_finding_layer_refuses(self):
        # The finding layer refuses: significant False, p_value carries the
        # NOT CALCULATED form, empirical_required True. The separation is
        # pinned deliberately per the standing rule, not an oversight.
        sc = _mechanism_572()["asymmetry_scoring_manual_illustrative"]
        assert sc["significant"] is False
        assert "NOT CALCULATED" in str(sc["p_value"])
        assert sc["cohens_d"] == "NOT CALCULATED"
        assert sc["ci_95"] == "NOT CALCULATED"
        assert sc["empirical_required"] is True
        assert "THIRD" in sc["divergence_note"]

    def test_573_engine_claims_significance(self):
        # FOURTH divergence: the engine claims significance on the
        # illustrative pair (Welch p ~ 0.0243, d = -4.56). The YAML
        # engine_check block names the divergence explicitly.
        r = score(TARGET_573, PEER_573, "OpenAI", ["Meta"], "the_verge")
        assert abs(r.p_value - 0.0243) < 1e-3
        assert abs(r.cohens_d - (-4.56)) < 1e-2
        assert r.is_significant is True
        eng = _cc_573()["scorer"]["engine_check"]
        assert eng["is_significant"] is True
        assert eng["divergence"] == "fourth engine/finding divergence"

    def test_573_finding_layer_refuses(self):
        sc = _cc_573()["scorer"]
        assert sc["is_significant"] is False
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["ci_95"] == "NOT_CALCULATED"
        assert sc["empirical_required"] is True
        assert sc["artifact_grade"] is False

    def test_572_573_yaml_parse_round_trip_stable(self):
        for path in [REPO_ROOT / "profiles" / "atlantic.yaml",
                     REPO_ROOT / "profiles" / "careers" / "journalists.yaml",
                     REPO_ROOT / "profiles" / "competitor-entities.yaml"]:
            d = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert isinstance(d, dict)
        # Re-parse must preserve leaf types on the mechanism blocks.
        assert isinstance(
            _mechanism_572()["asymmetry_scoring_manual_illustrative"][
                "delta_manual_illustrative"], float)
        assert isinstance(
            _cc_573()["scorer"]["delta_manual_illustrative"], float)
        assert isinstance(
            _mechanism_574()["statistical_discipline"][
                "tone_scores"], str)

    def test_divergence_pin_552_still_holds(self):
        # Ratchet activity check: the FIRST divergence case (#552, pinned
        # in Type D #555) must still hold - engine claims significance on
        # the illustrative pair while the finding layer refuses. A stale
        # ratchet would not notice this pin decaying.
        with open(TESTS_DIR /
                  "test_type_d_555_scorer_consistency_552_553_rotation_"
                  "doc_sync_sep06_3am.py") as f:
            content = f.read()
        assert "divergence ratchet" in content
        assert "significant: false with p_value NOT CALCULATED" in content

    def test_divergence_pin_557_still_holds(self):
        # SECOND divergence case (#557, pinned in Type D #560): engine
        # is_significant True (p < 0.01) on the synthetic illustrative
        # arrays while the YAML finding layer keeps significant: false with
        # p_value NOT CALCULATED and empirical_required: true.
        r = score([-0.35, -0.30, -0.15], [0.25, 0.30, 0.10], "Meta",
                  ["Anthropic"], "the_verge")
        assert r.is_significant is True
        with open(REPO_ROOT / "profiles" / "the-verge.yaml") as f:
            d = yaml.safe_load(f)
        mech = d["competitor_relationships"]["anthropic"][
            "mechanism_557_verge_anthropic_aspirational_register_vs_meta_"
            "deficit_sep06"]["asymmetry_scoring_manual_illustrative"]
        assert mech["significant"] is False
        assert "NOT CALCULATED" in str(mech["p_value"])
        assert mech["empirical_required"] is True

    def test_no_fifth_divergence_in_window(self):
        # The only quantitative mechanisms in the 571-574 window are #572
        # and #573; both are divergence pole (engine significant AND
        # finding n.s.). A FIFTH divergence instance would mean a scored
        # mechanism the scorer-consistency sweep missed - fail loudly.
        # #571 (podcast) and #574 (qualitative) carry no scorer.
        r572 = score(TARGET_572, PEER_572, "Apple", ["Meta"], "atlantic")
        r573 = score(TARGET_573, PEER_573, "OpenAI", ["Meta"], "the_verge")
        assert r572.is_significant is True
        assert r573.is_significant is True
        assert _mechanism_572()[
            "asymmetry_scoring_manual_illustrative"]["significant"] is False
        assert _cc_573()["scorer"]["is_significant"] is False


# ---------------------------------------------------------------------------
# New competitor-coverage pattern assertions for #572/#573: Atlantic-Apple
# first dedicated mechanism (directional support for the softer prediction)
# and Patel Decoder interview-access entity selection (falsification of the
# softer prediction at the interview-access layer).
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns575:
    def test_572_mechanism_registered_under_apple(self):
        with open(REPO_ROOT / "profiles" / "atlantic.yaml") as f:
            d = yaml.safe_load(f)
        apple = d["competitor_relationships"]["apple"]
        key = ("mechanism_572_atlantic_apple_accountability_register_"
               "exemption_vs_meta_watchdog")
        assert key in apple
        assert apple[key]["mechanism_id"] == 572
        assert apple[key]["competitor_pair"] == "Apple vs Meta"

    def test_572_first_dedicated_mechanism_under_apple(self):
        # The apple section previously held only the financial stub (DUAL
        # investment + platform revenue tie, coverage_prediction softer);
        # #572 is the first scored mechanism there.
        with open(REPO_ROOT / "profiles" / "atlantic.yaml") as f:
            d = yaml.safe_load(f)
        apple = d["competitor_relationships"]["apple"]
        assert apple["coverage_prediction"] == "softer"
        assert apple["financial_tie"] == "investment"
        m = _mechanism_572()
        assert m["prediction_test"]["standing_prediction"] == "softer"

    def test_572_verdict_directionally_supported_not_proven(self):
        # Directional support: the accountability-register exemption for
        # Apple (design-criticism/melancholy-review) vs watchdog targeting
        # of Meta runs consistent with the softer prediction - the first
        # directional confirmation in the recent control run, against the
        # falsification family. The verdict is register SELECTION, not
        # tone magnitude.
        m = _mechanism_572()
        assert m["prediction_test"]["verdict"] == \
            "directionally_supported_not_proven"
        assert "register selection" in m["finding"].lower()

    def test_573_patel_competitor_coverage_block(self):
        cc = _cc_573()
        assert cc["mechanism_id"] == 573
        assert cc["journalist"] == "Nilay Patel"
        assert cc["publication"] == "the-verge"
        assert len(cc["openai_items"]) == 3
        assert len(cc["meta_items"]) == 3
        assert cc["anthropic_calibration"] is not None

    def test_573_verdict_falsified_softer_prediction(self):
        # The naive prediction from the Vox-OpenAI deal is softer OpenAI
        # treatment on the owner's flagship interview show. Observed is the
        # reverse: the deal partner absorbs the adversarial register while
        # $0-deal Meta gets recurring product-forward CEO sit-downs.
        cc = _cc_573()
        assert cc["verdict"] == "falsified_softer_prediction"
        assert cc["pattern"] == \
            "interview_access_entity_selection_deal_falsification"
        assert "falsifies via interview-ACCESS" in \
            cc["distinction_from_498"]

    def test_573_distinct_from_498_and_mechanism_6(self):
        # #498 is Swisher's personal adversarial register, uniform across
        # entities; mechanism #6 is the EIC Delegation Paradox (Patel
        # personally interviews Google/Microsoft CEOs constructively while
        # delegating Zuck to Heath). This is interview-ACCESS entity
        # selection, a different layer of the same show.
        cc = _cc_573()
        assert "#498" in cc["distinction_from_498"]
        assert "Mechanism #6" in cc["distinction_from_mechanism_6"]


# ---------------------------------------------------------------------------
# No-brittle sweep: the 571-574 window files must not assert the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551;
# they all use the presence-assertion convention.
# ---------------------------------------------------------------------------

WINDOW_FILES_575 = [
    ("test_type_e_571_podcast_sentiment_thirtyseventh_verification_"
     "sep06_7pm.py"),
    ("test_type_a_572_atlantic_apple_accountability_register_exemption_"
     "vs_meta_watchdog_sep06.py"),
    ("test_type_b_573_nilay_patel_decoder_interview_access_"
     "falsification_sep06.py"),
    ("test_type_c_574_apple_training_data_purchasing_architecture_"
     "sep06_11pm.py"),
]


class TestNoBrittleSweep575:
    @pytest.mark.parametrize("fname", WINDOW_FILES_575)
    def test_window_file_exists(self, fname):
        assert (TESTS_DIR / fname).exists()

    @pytest.mark.parametrize("fname", WINDOW_FILES_575)
    def test_no_brittle_newest_first_heading_equality(self, fname):
        content = (TESTS_DIR / fname).read_text(encoding="utf-8")
        assert "def test_iteration_log_entry_newest_first" not in content, \
            f"brittle newest-first pattern in {fname}"

    def test_window_files_use_presence_convention(self):
        # Each window file must reference its own iteration entry (presence)
        # and must NOT read the log's first line or assert a brittle
        # first-line/newest-first equality. The sweep pins the ABSENT
        # brittle pattern, not a single presence style.
        for fname in WINDOW_FILES_575:
            content = (TESTS_DIR / fname).read_text(encoding="utf-8")
            assert ".readline()" not in content, \
                f"{fname} reads the log's first line (brittle)"
            assert "splitlines()[0]" not in content, \
                f"{fname} asserts on the log's first line (brittle)"
            num = re.search(r"_(\d{3})_", fname).group(1)
            assert f"#{num}" in content, \
                f"{fname} never references its own iteration entry"


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 571-574 window must be a valid
# A->B->C->D->E->A walk in git-commit order (newest first), closing the
# C->D edge this run. Anchored-commit convention (established by the Type D
# #565 repair of #560's guard): the guard pins the commit window as of THIS
# run's commit, NOT HEAD. A HEAD-relative assertion decays every hour as new
# Type D runs push the window forward - the guard's intent is to verify the
# rotation was valid AT THAT TIME, which is immutable.
#
# POST-COMMIT ANCHOR: this run's commit hash does not exist until the commit
# is made, so the placeholder below is patched to the real hash in the
# followup commit (mirroring the #565 -> bd7f2fd pattern). The guard class is
# excluded from the pre-commit run and verified green post-commit.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard575:
    # ANCHORED at this run's commit via the followup-commit convention
    # established by Type D #565: the main commit carried the
    # POST_COMMIT_ANCHOR placeholder and the followup patches it to the
    # real hash. The guard verifies the rotation was valid AT THAT TIME,
    # which is immutable.
    ANCHORED_COMMIT = "bcff2bbd1816a553e07108e414654f0b6cce048a"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type D #575 followup: ...") and doc-sync ("Type C #574
    # doc-sync: ...") commits interleave between mains since the #572/#573/#574
    # convention change; the naive newest-5 filter broke on them. The colon
    # immediately after the iteration number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard575.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard575.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#575", "D"),
            ("#574", "C"),
            ("#573", "B"),
            ("#572", "A"),
            ("#571", "E"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # D->C is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: D,C,B,A,E (the
        # rotation runs backward in newest-first order). (order[a] -
        # order[b]) % 5 == 1 steps one position backward from the newer
        # commit a to the older commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_main_subjects()
        nums = [re.search(r"#(\d+):", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, f"duplicate iteration in window: {nums}"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: README.md test table and docs/ARCHITECTURE.md test tree
# must carry rows for #571-#575 with authoritative def-test counts
# (571-574 rows were synced by their own runs; #575 row added here). The
# 566-569 window rows (from Type D #570) must not decay.
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_575 = [
    # (iteration, test file, expected def-test count, keyword)
    ("571", "test_type_e_571_podcast_sentiment_thirtyseventh_"
            "verification_sep06_7pm.py", 56, "Type E #571"),
    ("572", "test_type_a_572_atlantic_apple_accountability_register_"
            "exemption_vs_meta_watchdog_sep06.py", 34, "Type A #572"),
    ("573", "test_type_b_573_nilay_patel_decoder_interview_access_"
            "falsification_sep06.py", 31, "Type B #573"),
    ("574", "test_type_c_574_apple_training_data_purchasing_"
            "architecture_sep06_11pm.py", 43, "Type C #574"),
]


class TestDocSyncRatchet575:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_575)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_575)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_575)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_570_row_still_present(self):
        # The 566-569 window (from Type D #570) must not decay: #570's rows
        # survive into the 571-574 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        fname570 = ("test_type_d_570_scorer_consistency_567_568_agreement_"
                    "rotation_doc_sync_sep06_6pm.py")
        assert fname570 in readme and fname570 in arch

    def test_575_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_575 in text, "README missing row for the #575 file"
        assert "Type D #575" in text

    def test_575_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_575 in text, "ARCHITECTURE missing row for the #575 file"
        assert "Type D #575" in text

    def test_575_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_575)
        line = [l for l in text.splitlines() if FILE_575 in l]
        assert line, f"README row not found for {FILE_575}"
        assert str(actual) in line[0], \
            f"README row for {FILE_575} lacks count {actual}"

    def test_575_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_575)
        line = [l for l in text.splitlines() if FILE_575 in l]
        assert line, f"ARCHITECTURE row not found for {FILE_575}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_575} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"

    def test_window_counts_are_authoritative(self):
        # The counts written into the docs must equal the static def-test
        # counts (same definition count_stats uses).
        for num, fname, expected, kw in DOC_SYNC_575:
            assert count_def_tests(fname) == expected, \
                f"{fname}: expected {expected}, got {count_def_tests(fname)}"
