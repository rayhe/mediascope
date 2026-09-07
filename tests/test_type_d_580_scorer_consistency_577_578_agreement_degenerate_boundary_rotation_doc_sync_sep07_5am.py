"""Type D #580 (2026-09-07 05:00 PDT): dependency restoration + scorer
cross-mechanism consistency extended to #577/#578 (rotation 579 C -> 580 D).

REPAIR: the suite would not COLLECT at run start - 39 test modules errored
on ModuleNotFoundError: textblob (mediascope/analyze/sentiment.py imports
it), and pytest itself failed to launch on missing pygments. Installed
system-wide via pip --break-system-packages (externally managed env):
pygments 2.21.0, textblob, vaderSentiment (second missing module in
sentiment.py, surfaced after textblob). Collection now clean: 30372 tests,
0 errors - exactly the README's authoritative count, so
scripts/count_stats.py --check passes green again. Its pre-fix STALE
verdict (README=30372 vs actual=29430) was a collection artifact of the 39
erroring modules, not real README drift. The .venv python still lacks
textblob/vaderSentiment - the fix is host-specific to the system python3,
documented in the iteration-log entry, not silently assumed.

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (calculate_asymmetry) computes t/p/CI on the logged
arrays, and its MEAN-DIFFERENCE arithmetic must reproduce the logged
manual delta (engine-drift detection). The engine's own significance
output is computed but deliberately NOT promoted to a finding for
illustrative inputs - this file pins that separation for the two newest
quantitative mechanisms, in two NEW boundary classes:

- #577 (Type A, Gizmodo x Anthropic null-tie symmetric-adversarial
  control, Sep 7 02:00 PDT): Anthropic target [-0.55, -0.45, -0.50] avg
  -0.50 vs Meta peer [-0.70, -0.55, -0.60] avg -0.6167. Logged
  asymmetry_score 0.12 (target-minus-peer: Anthropic marginally softer).
  SEVENTH agreement-pole pin: engine Welch p ~ 0.1021 n.s., d = 1.81,
  is_significant False, and the finding layer refuses (p_value
  NOT_CALCULATED, cohens_d NOT_CALCULATED, is_significant false) - engine
  and finding agree to refuse on real computation, joining the agreement
  pole (#567/#568 pinned FIFTH+SIXTH in Type D #570; FIRST-FOURTH earlier).
- #578 (Type B, Ian Bogost writer-register inversion, Sep 7 03:00 PDT):
  Apple target [-0.25, -0.35] avg -0.30 vs Meta peer [0.45] avg +0.45.
  Logged delta -0.75 (target harder than peer: INVERSION of the
  softer-Apple prediction). FIRST DEGENERATE-BOUNDARY pin: the peer arm
  has n=1 < 2, so welch_t_test returns the degenerate (t=0.0, p=1.0) and
  is_significant False while cohens_d computes -10.61 and the
  mean-difference arithmetic still reproduces -0.75. The engine refuses
  STRUCTURALLY (guard path) while the finding layer refuses DELIBERATELY
  (NOT_CALCULATED) - an agreement via different mechanisms, the first
  corpus pin of the engine's n<2 degenerate path. The agreement pole
  (engine refuses significance on real computation) and the degenerate
  boundary (engine refuses to compute) are now pinned as DISTINCT
  boundary classes.

Divergence ratchet: the four divergence pins (#552 in #555, #557 in #560,
#572/#573 in #575) are spot-checked still holding, so the ratchet is
active rather than stale: a NEW divergence beyond the four in the 576-579
window would have been caught by the per-mechanism assertions.

Sign-class separation: #577 (+0.1167, null-tie symmetric-adversarial
control, directional-support) vs #578 (-0.75, writer-level inversion,
falsification family). Opposite sign classes; the suite must not conflate
a control with a falsification. |#578| ~ 6.4x |#577| - the inversion is a
large register effect against the small null-tie noise.

Also: #579 (Type C, Wikimedia Enterprise, Sep 7 04:00 PDT) is the
qualitative boundary (mirroring #574 in #575): no asymmetry_scorer
section, statistical_discipline carries tone_scores NOT_SCORED, p_value
NOT_CALCULATED, is_significant false - scorer consistency explicitly does
NOT apply. #576 (Type E, podcast 38th verification, Sep 7 01:00 PDT) is
the monitoring boundary (mirroring #571 in #575): monitoring-only, no
quantitative mechanism, no scorer extension.

A no-brittle sweep pins that none of the 576-579 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired in
#551 (all four use the presence-assertion convention). Rotation guard:
the 576 E -> 577 A -> 578 B -> 579 C window follows A->B->C->D->E->A
adjacency in git-commit order (newest first), closing the C->D edge this
run. Doc-sync ratchet: the README/ARCHITECTURE per-file window for
576-579 was already synced by their own runs (rows verified present with
authoritative def-test counts 56/47/40/43); this run extends the window
with its own row and verifies the #575 row survives, with the authoritative
count_stats.py --check gate.

Novelty: zero test_type_d_580 files on disk before this run (glob
verified); no #580 in git log (grep verified); scorer consistency has
never covered #577/#578 (repo grep for 577/578 in scorer-consistency test
files returned only their own mechanism files); the 576-579 rotation
window was never guarded; the 571-574 doc-sync window (from #575) is
extended, not duplicated; the degenerate-boundary class is new to the
corpus (no prior test asserts the engine's n<2 guard path). The filename
embeds the covered iteration numbers (577_578) per the
#555/#560/#565/#570/#575 Type-D filename convention.
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

FILE_580 = ("test_type_d_580_scorer_consistency_577_578_agreement_degenerate_"
            "boundary_rotation_doc_sync_sep07_5am.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_577 = [-0.55, -0.45, -0.50]
PEER_577 = [-0.70, -0.55, -0.60]
TARGET_578 = [-0.25, -0.35]
PEER_578 = [0.45]


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


def _mechanism_577():
    with open(REPO_ROOT / "profiles" / "gizmodo.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["anthropic"][
        "mechanism_577_gizmodo_anthropic_null_tie_symmetric_adversarial"]


def _load_journalists():
    with open(REPO_ROOT / "profiles" / "careers" / "journalists.yaml") as f:
        return yaml.safe_load(f)


def _walk(o, out, name):
    if isinstance(o, dict):
        if o.get("name") == name:
            out.append(o)
        for v in o.values():
            _walk(v, out, name)
    elif isinstance(o, list):
        for v in o:
            _walk(v, out, name)


def _load_bogost():
    data = _load_journalists()
    found = []
    _walk(data, found, "Ian Bogost")
    assert found, "Ian Bogost entry missing from journalists.yaml"
    return found[0]


def _cc_578():
    entry = _load_bogost()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"][
        "type_b_578_ian_bogost_meta_apple_writer_register_inversion"]


def _mechanism_579():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["wikimedia_enterprise_ai_training_deals_579"]


def _mechanism_572():
    with open(REPO_ROOT / "profiles" / "atlantic.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["apple"][
        "mechanism_572_atlantic_apple_accountability_register_exemption_vs_"
        "meta_watchdog"]


def _cc_573():
    entry_data = _load_journalists()
    found = []
    _walk(entry_data, found, "Nilay Patel")
    assert found, "Nilay Patel entry missing from journalists.yaml"
    return found[0]["competitor_coverage"]["cross_entity_analysis"]


# ---------------------------------------------------------------------------
# Iteration metadata
# ---------------------------------------------------------------------------


class TestIteration580Metadata:
    def test_docstring_ids(self):
        assert "#580" in __doc__
        assert "2026-09-07 05:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # This run closes the C->D edge: previous main commit is #579 Type C,
        # this run is #580 Type D.
        assert "579 C -> 580 D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_580

    def test_covered_iterations_in_filename(self):
        assert "577_578" in FILE_580

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#580 Type D" in text

    def test_dep_repair_documented(self):
        text = LOG.read_text(encoding="utf-8")
        assert "39" in text and "textblob" in text


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: #577 agreement pole, #578 degenerate
# boundary, #579 qualitative boundary, #576 monitoring boundary.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency580:
    def test_577_delta_reproduced(self):
        r = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        assert abs(r.asymmetry_score - 0.1167) < 1e-3

    def test_577_engine_sign_is_target_softer(self):
        r = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        assert r.asymmetry_score > 0

    def test_577_logged_avgs_match_engine(self):
        r = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        assert abs(r.target_avg_tone - (-0.50)) < 1e-4
        assert abs(r.peer_avg_tone - (-0.6167)) < 1e-3

    def test_577_logged_result_byte_match(self):
        sc = _mechanism_577()["asymmetry_scorer_result"]
        assert sc["target_avg_tone"] == pytest.approx(-0.5, abs=1e-9)
        assert sc["peer_avg_tone"] == pytest.approx(-0.617, abs=1e-3)
        assert sc["asymmetry_score"] == pytest.approx(0.12, abs=1e-3)

    def test_577_article_tones_match_engine_inputs(self):
        arts = _mechanism_577()["articles"]
        tones = [a["manual_illustrative_tone"] for a in arts]
        assert tones[:3] == pytest.approx(TARGET_577, abs=1e-9)
        assert tones[3:] == pytest.approx(PEER_577, abs=1e-9)

    def test_578_delta_reproduced(self):
        # Mean-difference arithmetic intact even at the degenerate boundary.
        r = score(TARGET_578, PEER_578, "apple", ["meta"], "atlantic")
        assert abs(r.asymmetry_score - (-0.75)) < 1e-4

    def test_578_logged_arrays_byte_match_engine_inputs(self):
        sc = _cc_578()["asymmetry_scorer_result_illustrative"]
        assert sc["target_scores"] == pytest.approx(TARGET_578, abs=1e-9)
        assert sc["peer_scores"] == pytest.approx(PEER_578, abs=1e-9)
        assert abs(sc["delta"] - (-0.75)) < 1e-4
        assert sc["delta_calc"] == "target_avg - peer_avg = -0.30 - 0.45 = -0.75"

    def test_579_qualitative_no_scorer(self):
        m = _mechanism_579()
        assert "asymmetry_scorer" not in m
        assert m["mechanism_id"] == 579
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scope"] == "qualitative structural mapping only"

    def test_576_monitoring_no_scorer(self):
        # Type E 38th podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        fname = ("test_type_e_576_podcast_sentiment_thirtyeighth_"
                 "verification_sep07_1am.py")
        assert (TESTS_DIR / fname).exists()
        assert count_def_tests(fname) == 56
        assert "Thirty-Eighth" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_577_and_578_sign_classes_distinct(self):
        # #577 is a positive null-tie control (Anthropic marginally softer at
        # a zero-tie publication); #578 is a negative writer-level inversion
        # (Apple harder than Meta despite the Atlantic-Apple dual tie).
        # Opposite sign classes; the suite must not conflate a control with
        # a falsification.
        r577 = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        r578 = score(TARGET_578, PEER_578, "apple", ["meta"], "atlantic")
        assert r577.asymmetry_score > 0 > r578.asymmetry_score
        # The inversion is a large register effect against small null-tie
        # noise: ~6.4x magnitude ratio.
        assert abs(abs(r578.asymmetry_score) - 0.75) < 1e-4
        assert abs(r578.asymmetry_score) / abs(r577.asymmetry_score) > 6


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #577 is the SEVENTH agreement-pole pin
# (engine n.s. on real computation AND finding layer refuses). #578 is the
# FIRST degenerate-boundary pin (engine refuses structurally via the n<2
# guard while the finding layer refuses deliberately). Divergence ratchet
# intact: the four divergence pins still hold.
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet580:
    def test_577_engine_not_significant(self):
        # SEVENTH agreement-pole pin: engine Welch p ~ 0.1021 n.s.,
        # d = 1.81, is_significant False on the illustrative arrays.
        r = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        assert abs(r.p_value - 0.1021) < 1e-3
        assert abs(r.cohens_d - 1.8074) < 1e-3
        assert r.is_significant is False

    def test_577_finding_layer_refuses(self):
        sc = _mechanism_577()["asymmetry_scorer_result"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["confidence_interval"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert "standing rule Aug 28 2026" in sc["methodology"]

    def test_578_engine_degenerate_guard(self):
        # FIRST degenerate-boundary pin: peer arm n=1 < 2, so welch_t_test
        # returns the degenerate (t=0.0, p=1.0). is_significant False.
        # cohens_d still computes (-10.61) - the guard is specific to the
        # t-test path, not the whole engine.
        r = score(TARGET_578, PEER_578, "apple", ["meta"], "atlantic")
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False
        assert abs(r.cohens_d - (-10.6066)) < 1e-3

    def test_578_finding_layer_refuses(self):
        # The finding layer refuses deliberately (NOT_CALCULATED), while the
        # engine refuses structurally (degenerate guard) - agreement via
        # different mechanisms, distinct from the divergence family.
        sc = _cc_578()["asymmetry_scorer_result_illustrative"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert sc["correlation_not_causation"] is True
        assert abs(sc["delta"] - (-0.75)) < 1e-4

    def test_divergence_ratchet_still_holds_572(self):
        # THIRD divergence pin (#575) still active: engine claims
        # significance on the illustrative pair while the finding layer
        # refuses. A NEW divergence beyond the four would have been caught
        # by the per-mechanism assertions above.
        r = score([-0.35, -0.25], [-0.75, -0.65], "Apple", ["Meta"],
                  "atlantic")
        assert r.is_significant is True
        sc = _mechanism_572()["asymmetry_scoring_manual_illustrative"]
        assert sc["engine_divergence"] is True
        assert sc["significant"] is False
        assert "NOT CALCULATED" in str(sc["p_value"])
        assert "THIRD" in str(sc["divergence_note"])

    def test_divergence_ratchet_still_holds_573(self):
        # FOURTH divergence pin (#575) still active.
        r = score([-0.70, -0.60, -0.45], [-0.20, -0.15, -0.15], "OpenAI",
                  ["Meta"], "the_verge")
        assert r.is_significant is True
        eng = _cc_573()["scorer"]["engine_check"]
        assert eng["is_significant"] is True
        assert eng["divergence"] == "fourth engine/finding divergence"

    def test_agreement_and_degenerate_classes_distinct(self):
        # The agreement pole (#577: engine refuses significance on real
        # computation) and the degenerate boundary (#578: engine refuses to
        # compute) are pinned as DISTINCT boundary classes.
        r577 = score(TARGET_577, PEER_577, "anthropic", ["meta"], "gizmodo")
        r578 = score(TARGET_578, PEER_578, "apple", ["meta"], "atlantic")
        assert r577.p_value < 1.0 and r577.t_statistic != 0.0
        assert r578.p_value == 1.0 and r578.t_statistic == 0.0
        assert r577.is_significant is False and r578.is_significant is False


# ---------------------------------------------------------------------------
# New competitor-coverage pattern tests for #577/#578/#579.
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns580:
    def test_577_first_mechanism_under_gizmodo_anthropic(self):
        # #577's own novelty claim: first dedicated mechanism under
        # gizmodo.yaml competitor_relationships.anthropic.
        m = _mechanism_577()
        assert m["mechanism_id"] == 577
        assert m["publication_focus"].startswith("Gizmodo")
        assert "null-tie" in m["finding"].lower()

    def test_577_control_pair_second(self):
        # SECOND in the Gizmodo null-tie control pair (after #512 Gizmodo x
        # Google); cross-references the first control.
        m = _mechanism_577()
        assert "512" in m["finding"]

    def test_577_domain_bounded(self):
        # The symmetric-adversarial claim is domain-bounded to
        # controversy/news; business-domain Anthropic items run
        # neutral-business.
        m = _mechanism_577()
        assert "Domain-bounded" in m["finding"] or \
            "domain-bounded" in m["finding"]

    def test_578_bogost_competitor_coverage_block(self):
        cc = _cc_578()
        assert cc["iteration"] == 578
        assert cc["type"] == "B"
        assert "WRITER-LEVEL FALSIFICATION" in cc["finding"]

    def test_578_inversion_direction_bound(self):
        # The writer-level gradient inverts the publication-level prediction:
        # prediction softer Apple than Meta; observed Apple harder.
        cc = _cc_578()
        assert cc["incentive_context"]["coverage_prediction"] == "softer"
        assert cc["incentive_context"]["prediction_result"] == \
            "inverted at writer level (Apple harder, Meta warmer)"

    def test_578_bounds_572(self):
        # #578 explicitly bounds mechanism #572 (Type A, same publication
        # Apple vs Meta, opposite direction at publication level).
        cc = _cc_578()
        assert "572" in cc["finding"] or "#572" in str(cc.get("counterevidence"))

    def test_579_first_wikimedia_mechanism(self):
        m = _mechanism_579()
        assert m["mechanism_id"] == 579
        assert m["iteration_type"] == "C"
        assert "Wikimedia" in m["mechanism_name"]

    def test_579_openai_standout_asymmetry(self):
        m = _mechanism_579()
        assert "OpenAI" in m["overview"]
        assert "24+" in m["overview"]

    def test_579_roster_bounded_per_492(self):
        # Absences are bounded per the iteration-492 rule (Reuters says
        # "among other firms") - no zero-coverage claims.
        m = _mechanism_579()
        assert "492" in m["overview"] or "bounded" in m["overview"]


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 576-579 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep580:
    WINDOW_580 = [
        "test_type_e_576_podcast_sentiment_thirtyeighth_verification_sep07_1am.py",
        "test_type_a_577_gizmodo_anthropic_null_tie_symmetric_adversarial_sep07_2am.py",
        "test_type_b_578_ian_bogost_meta_apple_writer_register_inversion_sep07_3am.py",
        "test_type_c_579_wikimedia_enterprise_ai_training_deals_sep07_4am.py",
    ]

    @pytest.mark.parametrize("fname", WINDOW_580)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 576-579 window, closing the C->D edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carried the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard580:
    ANCHORED_COMMIT = "18eec0faafbc9cea5a1567f469543c51aa2c6423"

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
             TestRotationCycleGuard580.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard580.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#580", "D"),
            ("#579", "C"),
            ("#578", "B"),
            ("#577", "A"),
            ("#576", "E"),
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
# must carry rows for #576-#580 with authoritative def-test counts
# (576-579 rows were synced by their own runs; #580 row added here). The
# 571-574 window rows (from Type D #575) must not decay.
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_580 = [
    # (iteration, test file, expected def-test count, keyword)
    ("576", "test_type_e_576_podcast_sentiment_thirtyeighth_"
            "verification_sep07_1am.py", 56, "Type E #576"),
    ("577", "test_type_a_577_gizmodo_anthropic_null_tie_symmetric_"
            "adversarial_sep07_2am.py", 47, "Type A #577"),
    ("578", "test_type_b_578_ian_bogost_meta_apple_writer_register_"
            "inversion_sep07_3am.py", 40, "Type B #578"),
    ("579", "test_type_c_579_wikimedia_enterprise_ai_training_deals_"
            "sep07_4am.py", 43, "Type C #579"),
]


class TestDocSyncRatchet580:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_580)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_580)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_580)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_575_row_still_present(self):
        # The 571-574 window (from Type D #575) must not decay: #575's rows
        # survive into the 576-579 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        fname575 = ("test_type_d_575_scorer_consistency_572_573_divergence_"
                    "rotation_doc_sync_sep07_12am.py")
        assert fname575 in readme and fname575 in arch

    def test_580_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_580 in text, "README missing row for the #580 file"
        assert "Type D #580" in text

    def test_580_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_580 in text, "ARCHITECTURE missing row for the #580 file"
        assert "Type D #580" in text

    def test_580_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_580)
        line = [l for l in text.splitlines() if FILE_580 in l]
        assert line, f"README row not found for {FILE_580}"
        assert str(actual) in line[0], \
            f"README row for {FILE_580} lacks count {actual}"

    def test_580_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_580)
        line = [l for l in text.splitlines() if FILE_580 in l]
        assert line, f"ARCHITECTURE row for {FILE_580}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_580} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"
