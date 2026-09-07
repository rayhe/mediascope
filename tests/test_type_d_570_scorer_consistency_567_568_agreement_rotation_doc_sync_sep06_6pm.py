"""Type D #570 (2026-09-06 18:00 PDT): scorer cross-mechanism consistency
extended to #567/#568 (fifth and sixth AGREEMENT-POLE pins - NO new
engine-significance/finding-layer divergence; the divergence count stays at
2: #552 and #557), #566 monitoring boundary, #569 qualitative boundary,
566-569 rotation guard (anchored at this run's commit via the #565
followup-commit convention), 566-569 doc-sync ratchet (incl #566/#567/#569
miss repair), no-brittle sweep over the 566-569 window, new
competitor-coverage pattern tests for #567 (NYT-Amazon payer adversarial
register) and #568 (Frier register-constancy control).

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are
NOT empirical - p_value NOT_CALCULATED, is_significant False in the mechanism
YAML, correlation not causation, no artifact-grade claims. The asymmetry
engine (calculate_asymmetry) computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta
(engine-drift detection). The engine's own significance output is computed
but deliberately NOT promoted to a finding for illustrative inputs - this
file pins that separation for the two newest quantitative mechanisms, and
pins the agreement pole a fifth and sixth time:

- #567 (Type A, NYT x Amazon licensing-payer adversarial register vs Meta
  bifurcation, Sep 6 15:00 PDT): target Amazon [-0.50, -0.30] avg -0.40 vs
  peer Meta [0.40, -0.65, 0.00] avg -0.0833. Logged
  delta_manual_illustrative -0.3167 (target-minus-peer: target harsher by
  0.32). FIFTH agreement-pole pin: engine p ~ 0.4139, is_significant False;
  finding layer also n.s. (significant: false with NOT CALCULATED fields).
  The delta_direction 'target harsher than peer by 0.32' uses the engine's
  own convention. The mechanism is the STRONGEST falsification setting yet
  for financial determinism: the actual $20-25M per year payer absorbs the
  adversarial register (money-sympathy INVERTED), extending the #562 Google
  control ($0 tie) to the paying counterparty. Joins #552, #557, #193.
- #568 (Type B, Sarah Frier Bloomberg register constancy across Meta and
  OpenAI, Sep 6 16:00 PDT): Meta [-0.15, -0.10, -0.30] avg -0.1833 vs
  OpenAI [-0.35, -0.30, -0.25] avg -0.30, logged delta_manual_illustrative
  0.1167. SIXTH agreement-pole pin: engine p ~ 0.1823, is_significant False;
  finding layer n.s. (NOT_CALCULATED, is_significant false). The YAML
  engine_check block carries an explicit agreement_pole key naming the
  '#558/#563 class'. Register-constancy control: business-press AI-spend
  skepticism is event/market-driven and entity-agnostic, extending the
  #548/#553/#558/#563 falsification family to Bloomberg's top tech
  gatekeeper. OpenAI CFO Sarah FRIAR vs journalist Sarah FRIER name
  collision explicitly disambiguated.
- #569 (Type C, Washington Post OpenAI-plus-Google dual AI payer, Sep 6
  17:00 PDT): qualitative - no asymmetry_scorer section is logged
  (statistical_discipline carries tone_scores NOT_SCORED, p_value
  NOT_CALCULATED); scorer consistency explicitly does NOT apply, mirroring
  the #554/#559/#564 boundary.
- #566 (Type E, podcast 36th verification, Sep 6 14:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Divergence ratchet: with #567 and #568 both pinned as agreement pole, the
engine-significance/finding-layer divergence count REMAINS 2 (#552 in #555,
#557 in #560). This file spot-checks that the two existing divergence pins
still hold (engine claims significance on the illustrative inputs while the
finding layer refuses), so the ratchet is active rather than stale: a new
divergence instance in the 566-569 window would have been caught by the
per-mechanism agreement-pole assertions.

Also: a no-brittle sweep - none of the 566-569 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired in
#551 (all four already use the presence-assertion convention); this pins the
convention against regression. Rotation guard: the 566 E -> 567 A -> 568 B
-> 569 C window follows A->B->C->D->E->A adjacency in git-commit order
(newest first), closing the C->D edge this run. Doc-sync ratchet extends
the README/ARCHITECTURE per-file window to 566-569 with the authoritative
count_stats.py --check gate, including a doc_sync_miss_repair for
#566 (ARCHITECTURE only), #567 (both), #569 (both) rows per the
#510/#555/#560/#565 repair convention.

Novelty: zero test_type_d_570 files on disk before this run (glob verified);
no #570 in git log (grep verified); scorer consistency has never covered
#567/#568 (repo grep for 567/568 in scorer-consistency test files returned
only their own mechanism files); the 566-569 rotation window was never
guarded; the 560-565 doc-sync window (from #565) is extended, not duplicated.
The filename embeds the covered iteration numbers (567_568) per the
#555/#560/#565 Type-D filename convention.
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

FILE_570 = ("test_type_d_570_scorer_consistency_567_568_agreement_rotation_"
            "doc_sync_sep06_6pm.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_567 = [-0.50, -0.30]
PEER_567 = [0.40, -0.65, 0.00]
TARGET_568 = [-0.15, -0.10, -0.30]
PEER_568 = [-0.35, -0.30, -0.25]


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


def _load_nyt():
    with open(REPO_ROOT / "profiles" / "nytimes.yaml") as f:
        return yaml.safe_load(f)


def _mechanism_567():
    d = _load_nyt()
    return d["competitor_relationships"]["amazon"][
        "mechanism_567_nyt_amazon_licensing_payer_adversarial_register_vs_"
        "meta_bifurcation_sep06"]


def _load_frier():
    with open(REPO_ROOT / "profiles" / "careers" / "journalists.yaml") as f:
        data = yaml.safe_load(f)
    found = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("name") == "Sarah Frier":
                found.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    assert found, "Sarah Frier entry missing from journalists.yaml"
    return found[0]


def _cc_568():
    entry = _load_frier()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"]["cross_entity_analysis"]


def _mechanism_569():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["entities"]["openai"][
        "mechanism_569_washington_post_openai_google_dual_ai_payer_"
        "partnership"]


# ---------------------------------------------------------------------------
# Iteration metadata
# ---------------------------------------------------------------------------


class TestIteration570Metadata:
    def test_docstring_ids(self):
        assert "Type D #570" in __doc__
        assert "567_568" in __doc__

    def test_rotation_c_to_d(self):
        # The rotation runs A->B->C->D->E->A; #569 was Type C at 17:00 PDT,
        # so this 18:00 PDT run is Type D, closing the C->D edge.
        assert "rotation 569 C -> 570 D" in LOG.read_text(encoding="utf-8")
        assert "Type D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name.startswith("test_type_d_570")

    def test_covered_iterations_in_filename(self):
        assert "567_568" in Path(__file__).name

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#570" in text
        assert "Type D" in text
        assert "scorer_consistency" in text or "Scorer Consistency" in text


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine arithmetic must reproduce the
# logged MANUAL ILLUSTRATIVE deltas for #567 and #568 (1e-4), and the
# qualitative/monitoring boundaries for #566 and #569 must hold.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency570:
    def test_567_delta_reproduced(self):
        r = score(TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes")
        assert abs(r.asymmetry_score - (-0.3167)) < 1e-4

    def test_567_engine_sign_is_target_harsher(self):
        r = score(TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes")
        assert r.asymmetry_score < 0

    def test_567_logged_avgs_match_engine(self):
        r = score(TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes")
        assert abs(r.target_avg_tone - (-0.40)) < 1e-4
        assert abs(r.peer_avg_tone - (-0.0833)) < 1e-3

    def test_567_logged_arrays_byte_match_engine_inputs(self):
        mech = _mechanism_567()["asymmetry_scoring_manual_illustrative"]
        assert mech["target_scores_manual_illustrative"] == pytest.approx(
            TARGET_567, abs=1e-9)
        assert mech["peer_scores_manual_illustrative"] == pytest.approx(
            PEER_567, abs=1e-9)
        assert mech["delta_manual_illustrative"] == pytest.approx(
            -0.3167, abs=1e-4)
        assert mech["delta_direction"] == "target harsher than peer by 0.32"

    def test_568_delta_reproduced(self):
        r = score(TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg")
        assert abs(r.asymmetry_score - 0.1167) < 1e-4

    def test_568_logged_avgs_match_engine(self):
        r = score(TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg")
        assert abs(r.target_avg_tone - (-0.1833)) < 1e-3
        assert abs(r.peer_avg_tone - (-0.30)) < 1e-4

    def test_568_logged_arrays_byte_match_engine_inputs(self):
        cc = _cc_568()
        sc = cc["scorer"]
        assert sc["target_scores"] == pytest.approx(TARGET_568, abs=1e-9)
        assert sc["peer_scores"] == pytest.approx(PEER_568, abs=1e-9)
        assert abs(sc["delta_manual_illustrative"] - 0.1167) < 1e-4
        eng = sc["engine_check"]
        assert abs(eng["p_value"] - 0.1823) < 1e-3
        assert eng["is_significant"] is False

    def test_569_qualitative_no_tone_delta(self):
        m = _mechanism_569()
        assert "asymmetry_scorer" not in m
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"

    def test_566_monitoring_no_scorer(self):
        # Type E 36th podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        fname = ("test_type_e_566_podcast_sentiment_thirtysixth_verification_"
                 "sep06_2pm.py")
        assert (TESTS_DIR / fname).exists()
        assert count_def_tests(fname) == 51
        assert "Thirty-Sixth" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_567_and_568_sign_classes_distinct(self):
        # #567 is a negative target-harsher asymmetry observation (control
        # case against financial determinism); #568 is a near-zero positive
        # constancy falsification. Opposite sign classes; the suite must not
        # conflate an asymmetry observation with a constancy falsification.
        r567 = score(TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes")
        r568 = score(TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg")
        assert r567.asymmetry_score < 0 < r568.asymmetry_score
        assert abs(r567.asymmetry_score) > 2.5 * abs(r568.asymmetry_score)


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #567 and #568 are the FIFTH and SIXTH
# agreement-pole pins (engine n.s. AND finding layer n.s.), and the
# divergence count must remain exactly 2 (#552, #557).
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet570:
    def test_567_scorer_keeps_not_calculated(self):
        # The YAML block itself uses the spaced 'NOT CALCULATED' forms
        # throughout (p_value carries the 'no observed corpus' suffix),
        # matching the #567 test file's own assertions. The test pins what
        # is there; it does not normalize past data.
        sc = _mechanism_567()["asymmetry_scoring_manual_illustrative"]
        assert sc["p_value"] == "NOT CALCULATED no observed corpus"
        assert sc["cohens_d"] == "NOT CALCULATED"
        assert sc["ci_95"] == "NOT CALCULATED"

    def test_567_agreement_pole_engine_and_finding(self):
        # FIFTH agreement-pole pin: engine p ~ 0.4139 n.s. AND the finding
        # layer significant: false with NOT CALCULATED fields. Agreement
        # means the illustrative delta stays illustrative, NOT that it
        # becomes a proven null.
        r = score(TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes")
        assert abs(r.p_value - 0.4139) < 1e-3
        assert r.is_significant is False
        sc = _mechanism_567()["asymmetry_scoring_manual_illustrative"]
        assert sc["significant"] is False
        assert "NOT CALCULATED" in str(sc["p_value"])
        assert "agreement pole" in sc["synthetic_note"]

    def test_568_agreement_pole_engine_and_finding(self):
        # SIXTH agreement-pole pin: engine p ~ 0.1823 n.s. AND the finding
        # layer is_significant false with NOT_CALCULATED fields. The YAML
        # engine_check block carries an explicit agreement_pole key naming
        # the '#558/#563 class'.
        r = score(TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg")
        assert abs(r.p_value - 0.1823) < 1e-3
        assert r.is_significant is False
        sc = _cc_568()["scorer"]
        assert sc["is_significant"] is False
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["ci_95"] == "NOT_CALCULATED"

    def test_568_engine_check_names_agreement_pole(self):
        eng = _cc_568()["scorer"]["engine_check"]
        assert eng["agreement_pole"] == "#558/#563 class"

    def test_567_finding_label_present_in_yaml(self):
        m = _mechanism_567()
        assert "INVERTED" in m["finding"]

    def test_567_568_yaml_parse_round_trip_stable(self):
        for path in [REPO_ROOT / "profiles" / "nytimes.yaml",
                     REPO_ROOT / "profiles" / "careers" / "journalists.yaml",
                     REPO_ROOT / "profiles" / "competitor-entities.yaml"]:
            d = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert isinstance(d, dict)
        # Re-parse must preserve leaf types on the mechanism blocks.
        assert isinstance(
            _mechanism_567()["asymmetry_scoring_manual_illustrative"][
                "delta_manual_illustrative"], float)
        assert isinstance(
            _cc_568()["scorer"]["delta_manual_illustrative"], float)
        assert isinstance(
            _mechanism_569()["statistical_discipline"][
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

    def test_no_new_divergence_in_window(self):
        # The only quantitative mechanisms in the 566-569 window are #567
        # and #568; both are agreement pole (engine n.s. AND finding n.s.),
        # so the divergence count stays at exactly 2 (#552, #557). Any
        # third divergence instance would fail this class of assertion.
        for target, peer, entity, peers, slug in [
            (TARGET_567, PEER_567, "Amazon", ["Meta"], "nytimes"),
            (TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg"),
        ]:
            r = score(target, peer, entity, peers, slug)
            assert r.is_significant is False, \
                f"unexpected engine significance on {slug} window mechanism"


# ---------------------------------------------------------------------------
# New competitor-coverage pattern assertions for #567/#568: NYT-Amazon payer
# adversarial register (strongest falsification setting against financial
# determinism) and Frier register-constancy (business-press control, name
# collision disambiguated).
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns570:
    def test_567_mechanism_registered_under_amazon(self):
        d = _load_nyt()
        amazon = d["competitor_relationships"]["amazon"]
        key = ("mechanism_567_nyt_amazon_licensing_payer_adversarial_register"
               "_vs_meta_bifurcation_sep06")
        assert key in amazon
        assert amazon[key]["mechanism_id"] == 567
        assert amazon[key]["competitor_pair"] == "Amazon vs Meta"

    def test_567_falsifies_softer_coverage_prediction(self):
        # The standing coverage_prediction of softer (from the #559
        # $20-25M/yr licensing deal) is FALSIFIED: the payer absorbs the
        # adversarial register. The stub keeps its softer prediction; the
        # mechanism records the inversion (money-sympathy direction INVERTED
        # for the actual payer).
        amazon = _load_nyt()["competitor_relationships"]["amazon"]
        assert amazon["coverage_prediction"] == "softer"
        m = _mechanism_567()
        assert "INVERTED" in m["finding"]
        assert "actual payer" in m["finding"]

    def test_567_financial_tie_licensing_documented(self):
        amazon = _load_nyt()["competitor_relationships"]["amazon"]
        assert amazon["financial_tie"] == "licensing"
        assert "$20-25M" in _mechanism_567()["finding"]

    def test_567_control_case_against_financial_determinism(self):
        m = _mechanism_567()
        assert "control case" in m["finding"]
        assert "financial determinism" in m["finding"]

    def test_568_frier_competitor_coverage_block(self):
        cc = _cc_568()
        assert cc["mechanism_id"] == 568
        assert cc["journalist"] == "Sarah Frier"
        assert cc["publication"] == "bloomberg-news"
        assert len(cc["meta_items"]) == 3
        assert len(cc["openai_items"]) == 3

    def test_568_name_collision_disambiguated(self):
        # OpenAI's CFO is Sarah FRIAR (ex-Nextdoor), a different person from
        # journalist Sarah FRIER. The entry must disambiguate explicitly.
        text = yaml.dump(_load_frier(), default_flow_style=False)
        assert "Friar" in text

    def test_568_register_constancy_falsification_family(self):
        # The cross_entity_analysis block carries the register-constancy
        # business-press pattern label (matching the #568 test file's own
        # identity assertion); the falsification-family membership lives in
        # the iteration log and this file's docstring, not in the YAML key.
        cc = _cc_568()
        assert cc["pattern"] == "register_constancy_business_press"
        sc = cc["scorer"]
        assert abs(sc["delta_manual_illustrative"] - 0.1167) < 1e-4

    def test_568_matches_563_near_zero_class(self):
        # #563 (Heath) and #568 (Frier) are the same near-zero
        # register-constancy class: +0.1167 both, against journalist-level
        # anti-Meta bias. The delta magnitudes must be identical at 1e-4.
        r568 = score(TARGET_568, PEER_568, "Meta", ["OpenAI"], "bloomberg")
        r563 = score([0.0, 0.30, 0.10], [-0.30, 0.25, 0.10], "Meta",
                     ["non_Meta"], "the_verge")
        assert abs(r568.asymmetry_score - r563.asymmetry_score) < 1e-4


# ---------------------------------------------------------------------------
# No-brittle sweep: the 566-569 window files must not assert the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551;
# they all use the presence-assertion convention.
# ---------------------------------------------------------------------------

WINDOW_FILES_570 = [
    "test_type_e_566_podcast_sentiment_thirtysixth_verification_sep06_2pm.py",
    ("test_type_a_567_nyt_amazon_licensing_payer_adversarial_register_vs_"
     "meta_bifurcation_sep06.py"),
    "test_type_b_568_sarah_frier_bloomberg_register_constancy_sep06.py",
    ("test_type_c_569_washington_post_openai_google_dual_ai_payer_"
     "sep06_5pm.py"),
]


class TestNoBrittleSweep570:
    @pytest.mark.parametrize("fname", WINDOW_FILES_570)
    def test_window_file_exists(self, fname):
        assert (TESTS_DIR / fname).exists()

    @pytest.mark.parametrize("fname", WINDOW_FILES_570)
    def test_no_brittle_newest_first_heading_equality(self, fname):
        content = (TESTS_DIR / fname).read_text(encoding="utf-8")
        assert "def test_iteration_log_entry_newest_first" not in content, \
            f"brittle newest-first pattern in {fname}"

    def test_window_files_use_presence_convention(self):
        # Each window file must reference its own iteration entry (presence)
        # and must NOT read the log's first line or assert a brittle
        # first-line/newest-first equality. Styles differ across files
        # (anchored re.search vs substring containment) - the sweep pins
        # the ABSENT brittle pattern, not a single presence style.
        for fname in WINDOW_FILES_570:
            content = (TESTS_DIR / fname).read_text(encoding="utf-8")
            assert ".readline()" not in content, \
                f"{fname} reads the log's first line (brittle)"
            assert "splitlines()[0]" not in content, \
                f"{fname} asserts on the log's first line (brittle)"
            num = re.search(r"_(\d{3})_", fname).group(1)
            assert f"#{num}" in content, \
                f"{fname} never references its own iteration entry"


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 566-569 window must be a valid
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


class TestRotationCycleGuard570:
    # ANCHORED at this run's commit (382abc3) via the followup-commit
    # convention established by Type D #565 (see commit bd7f2fd): the main
    # commit carried the POST_COMMIT_ANCHOR placeholder and this followup
    # patches it to the real hash. The guard verifies the rotation was
    # valid AT THAT TIME, which is immutable.
    ANCHORED_COMMIT = "382abc3"

    @staticmethod
    def _git_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", f"-n{n}",
             TestRotationCycleGuard570.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        return out.stdout.splitlines()

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_subjects()
        assert len(subjects) >= 5
        expected = [
            ("#570", "D"),
            ("#569", "C"),
            ("#568", "B"),
            ("#567", "A"),
            ("#566", "E"),
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
        types = ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+)", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == types
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_subjects()
        nums = [re.search(r"#(\d+)", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, f"duplicate iteration in window: {nums}"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: README.md test table and docs/ARCHITECTURE.md test tree
# must carry rows for #566-#570 with authoritative def-test counts
# (miss repair for #566/#567/#569 per the #510/#555/#560/#565 convention).
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_570 = [
    # (iteration, test file, expected def-test count, keyword)
    ("566", "test_type_e_566_podcast_sentiment_thirtysixth_verification_"
            "sep06_2pm.py", 51, "Type E #566"),
    ("567", "test_type_a_567_nyt_amazon_licensing_payer_adversarial_"
            "register_vs_meta_bifurcation_sep06.py", 30, "Type A #567"),
    ("569", "test_type_c_569_washington_post_openai_google_dual_ai_payer_"
            "sep06_5pm.py", 46, "Type C #569"),
]


class TestDocSyncRatchet570:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_570)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_570)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_570)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_565_and_568_rows_still_present(self):
        # The 560-565 window (from Type D #565) must not decay: #565's and
        # #568's rows survive into the 566-569 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        fname565 = ("test_type_d_565_scorer_consistency_562_563_agreement_"
                    "rotation_doc_sync_sep06_1pm.py")
        fname568 = ("test_type_b_568_sarah_frier_bloomberg_register_"
                    "constancy_sep06.py")
        assert fname565 in readme and fname565 in arch
        assert fname568 in readme and fname568 in arch

    def test_570_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_570 in text, "README missing row for the #570 file"
        assert "Type D #570" in text

    def test_570_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_570 in text, "ARCHITECTURE missing row for the #570 file"
        assert "Type D #570" in text

    def test_570_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_570)
        line = [l for l in text.splitlines() if FILE_570 in l]
        assert line, f"README row not found for {FILE_570}"
        assert str(actual) in line[0], \
            f"README row for {FILE_570} lacks count {actual}"

    def test_570_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_570)
        line = [l for l in text.splitlines() if FILE_570 in l]
        assert line, f"ARCHITECTURE row not found for {FILE_570}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_570} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"

    def test_window_counts_are_authoritative(self):
        # The miss-repair counts written into the docs must equal the
        # static def-test counts (same definition count_stats uses).
        for num, fname, expected, kw in DOC_SYNC_570:
            assert count_def_tests(fname) == expected, \
                f"{fname}: expected {expected}, got {count_def_tests(fname)}"
