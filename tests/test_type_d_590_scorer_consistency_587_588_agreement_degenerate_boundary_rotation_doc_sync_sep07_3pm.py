"""Type D #590 (2026-09-07 15:00 PDT): scorer cross-mechanism consistency
extended to #587/#588 + rotation guard for 586-590 + doc-sync ratchet
+ doc-sync miss repair (rotation 589 C -> 590 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (calculate_asymmetry) computes t/p/CI on the logged
arrays, and its MEAN-DIFFERENCE arithmetic must reproduce the logged
manual delta (engine-drift detection). The engine's own significance
output is computed but deliberately NOT promoted to a finding for
illustrative inputs - this file pins that separation for the two newest
quantitative mechanisms, extending the agreement-pole and
degenerate-boundary classes:

- #587 (Type A, Gizmodo x Apple null-tie control, Sep 7 12:00 PDT): Apple
  target [-0.50, -0.55, -0.40] avg -0.4833 vs Meta peer [-0.70, -0.55, -0.60]
  avg -0.6167. Logged asymmetry_score 0.1334 (target-minus-peer; engine
  mean difference 0.13333 rounds to the logged value). NINTH agreement-pole
  pin: engine runs a REAL Welch computation (n=3 vs n=3, no guard
  triggered) returning t=2.1381, p=0.0993 n.s., d=1.7457, is_significant
  False, and the finding layer refuses (p_value NOT_CALCULATED, cohens_d
  NOT_CALCULATED, is_significant false) - engine and finding agree to
  refuse, joining the agreement pole (#582 pinned EIGHTH in Type D #585;
  #577 pinned SEVENTH in #580; #567/#568 FIFTH+SIXTH in #570). NOTE:
  p=0.0993 is the CLOSEST any agreement pin has come to nominal
  significance (previous pins: #582 p=1.0, #577 p~0.1021). The pole's
  integrity is stress-tested at the boundary and holds: a real computation
  flirting with the line still refuses, and the finding layer still
  refuses deliberately. The small positive delta is the FOURTH zero-tie
  control direction (after #512, #577, #582): product-lane reputation-carve
  boundary, not a tie-driven gradient.
- #588 (Type B, Scott Stein (CNET) hands-on review register constancy,
  Sep 7 13:00 PDT): Meta target [0.65] avg +0.65 vs Samsung/Google peer
  [0.70] avg +0.70. Logged delta -0.05 (target_minus_peer arithmetic
  intact: 0.65 - 0.70). THIRD DEGENERATE-BOUNDARY pin: both arms n=1 < 2,
  so welch_t_test returns the degenerate (t=0.0, p=1.0), is_significant
  False, and cohens_d computes 0.0 (symmetric zero-delta degenerate, like
  #583's 0.0 with n=1 vs n=1 and nonzero mean difference - the guard is
  specific to the t-test path, not the whole engine; contrast #578's
  d=-10.61 with n=2 vs n=1). The engine refuses STRUCTURALLY (guard path)
  while the finding layer refuses DELIBERATELY (NOT_CALCULATED) - an
  agreement via different mechanisms, joining #578's FIRST pin (Type D
  #580) and #583's SECOND (Type D #585). NOTE: |-0.05| is the
  SMALLEST-magnitude degenerate delta in the class (#578 -0.75, #583
  +0.80). The guard fires on sample size, not magnitude: near-zero
  constancy is still refused, pinning that register constancy is a
  no-claim finding under the standing rule, not a promoted symmetry
  result.

Sign-class separation: #587 (+0.1334, positive small, null-tie control)
vs #588 (-0.05, negative near-zero, register constancy). The suite must
not conflate a small-positive product-lane boundary with a negative
near-zero constancy read: |#587|/|#588| = 2.67 ratio, different
mechanism families, different verdict classes.

Also: #589 (Type C, Ziff Davis v. OpenAI lawsuit, Sep 7 14:00 PDT) is the
qualitative boundary (mirroring #584 in #585, #579 in #580): no
asymmetry_scorer section, statistical_discipline carries tone_scores
NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant false,
scope "qualitative structural mapping only" - scorer consistency
explicitly does NOT apply. It is the FIRST adversarial (negative-sign)
financial-incentive mechanism in the corpus: a publisher suing the AI lab
for hundreds of millions in damages, the inverse of the licensing-deal
incentives. #586 (Type E, podcast 40th verification, Sep 7 11:00 PDT) is
the monitoring boundary (mirroring #581 in #585, #576 in #580):
monitoring-only, no quantitative mechanism, no scorer extension.

A no-brittle sweep pins that none of the 586-589 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired
in #551 (all four use the presence-assertion convention).

Divergence ratchet: the four divergence pins (#552 in #555, #557 in #560,
#572/#573 in #575) are spot-checked still holding via #572/#573, so the
ratchet is active rather than stale: a NEW divergence beyond the four in
the 586-589 window would have been caught by the per-mechanism
assertions.

DOC-SYNC MISS REPAIR: the #588 run added its ARCHITECTURE.md tree row but
missed the README.md table row; the #589 run missed both rows (neither
README nor ARCHITECTURE carries the #589 row). This run repairs all three
missing rows before adding its own #590 rows - the 586-590 window must be
fully synced for the ratchet to mean anything. Mirrors the Type D #510
doc-sync miss repair precedent. The count_stats.py --check gate is the
authoritative arbiter, and the README top-level stats (Tests / Test
files) are refreshed to the post-run totals.

Rotation guard: the 586-590 window follows A->B->C->D->E->A adjacency in
git-commit order (newest first) as D,C,B,A,E, closing the C->D edge this
run. Doc-sync ratchet: the README/ARCHITECTURE per-file window for
586-589 is fully synced after the miss repair (rows verified present with
authoritative def-test counts 58/47/38/42); this run extends the window
with its own row and verifies the #585 row survives, with the
authoritative count_stats.py --check gate.

Novelty: zero test_type_d_590 files on disk before this run (glob
verified); no #590 in git log (grep verified); scorer consistency has
never covered #587/#588 (repo grep for 587/588 in scorer-consistency test
files returned only their own mechanism files); the 586-589 rotation
window was never guarded; the 581-584 doc-sync window (from #585) is
extended, not duplicated; p=0.0993 is the closest-to-significance
agreement-pole engine computation in the corpus; the degenerate class
gains its THIRD member at the smallest magnitude yet (-0.05).
The filename embeds the covered iteration numbers (587_588) per the
#555/#560/#565/#570/#575/#580/#585 Type-D filename convention.
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

FILE_590 = ("test_type_d_590_scorer_consistency_587_588_agreement_degenerate_"
            "boundary_rotation_doc_sync_sep07_3pm.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_587 = [-0.50, -0.55, -0.40]
PEER_587 = [-0.70, -0.55, -0.60]
TARGET_588 = [0.65]
PEER_588 = [0.70]

FILE_586 = ("test_type_e_586_podcast_sentiment_fortieth_"
            "verification_sep07_11am.py")
FILE_587 = ("test_type_a_587_gizmodo_apple_null_tie_fourth_control_"
            "product_lane_boundary_sep07_12pm.py")
FILE_588 = ("test_type_b_588_scott_stein_handson_review_register_"
            "constancy_sep07_1pm.py")
FILE_589 = ("test_type_c_589_ziff_davis_openai_lawsuit_"
            "adversarial_sep07_2pm.py")
FILE_585 = ("test_type_d_585_scorer_consistency_582_583_agreement_degenerate_"
            "boundary_rotation_doc_sync_sep07_10am.py")


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


def _mechanism_587():
    with open(REPO_ROOT / "profiles" / "gizmodo.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["apple"][
        "mechanism_587_gizmodo_apple_null_tie_fourth_control_"
        "product_lane_boundary"]


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


def _load_stein():
    data = _load_journalists()
    found = []
    _walk(data, found, "Scott Stein")
    assert found, "Scott Stein entry missing from journalists.yaml"
    return found[0]


def _cc_588():
    entry = _load_stein()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"][
        "type_b_588_scott_stein_handson_review_register_constancy"]


def _mechanism_589():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["ziff_davis_openai_lawsuit_adversarial_incentive_589"]


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


class TestIteration590Metadata:
    def test_docstring_ids(self):
        assert "#590" in __doc__
        assert "2026-09-07 15:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # This run closes the C->D edge: previous main commit is #589 Type C,
        # this run is #590 Type D.
        assert "589 C -> 590 D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_590

    def test_covered_iterations_in_filename(self):
        assert "587_588" in FILE_590

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#590 Type D" in text

    def test_docstring_names_ninth_agreement_and_third_degenerate(self):
        assert "NINTH agreement-pole" in __doc__
        assert "THIRD DEGENERATE-BOUNDARY" in __doc__

    def test_docstring_names_miss_repair(self):
        assert "DOC-SYNC MISS REPAIR" in __doc__


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: #587 agreement pole (ninth pin,
# closest-to-significance variant), #588 degenerate boundary (third pin,
# smallest-magnitude variant), #589 qualitative boundary, #586 monitoring
# boundary.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency590:
    def test_587_delta_reproduced(self):
        # NINTH agreement-pole pin: the engine's mean-difference arithmetic
        # reproduces the logged delta (0.1334 rounded from 0.13333).
        r = score(TARGET_587, PEER_587, "apple", ["meta"], "gizmodo")
        assert abs(r.asymmetry_score - 0.1334) < 1e-4

    def test_587_logged_avgs_match_engine(self):
        r = score(TARGET_587, PEER_587, "apple", ["meta"], "gizmodo")
        assert abs(r.target_avg_tone - (-0.4833)) < 1e-3
        assert abs(r.peer_avg_tone - (-0.6167)) < 1e-3

    def test_587_logged_result_byte_match(self):
        sc = _mechanism_587()["asymmetry_scorer_result"]
        assert sc["target_avg_tone"] == pytest.approx(-0.4833, abs=1e-9)
        assert sc["peer_avg_tone"] == pytest.approx(-0.6167, abs=1e-9)
        assert sc["asymmetry_score"] == pytest.approx(0.1334, abs=1e-9)

    def test_587_article_tones_match_engine_inputs(self):
        arts = _mechanism_587()["articles"]
        tones = [a["manual_illustrative_tone"] for a in arts]
        assert tones[:3] == pytest.approx(TARGET_587, abs=1e-9)
        assert tones[3:] == pytest.approx(PEER_587, abs=1e-9)

    def test_588_delta_reproduced(self):
        # Mean-difference arithmetic intact even at the degenerate boundary.
        r = score(TARGET_588, PEER_588, "meta", ["samsung/google"], "cnet")
        assert abs(r.asymmetry_score - (-0.05)) < 1e-4

    def test_588_logged_arrays_byte_match_engine_inputs(self):
        sc = _cc_588()["asymmetry_scorer_result_illustrative"]
        assert sc["target_scores"] == pytest.approx(TARGET_588, abs=1e-9)
        assert sc["peer_scores"] == pytest.approx(PEER_588, abs=1e-9)
        assert abs(sc["delta"] - (-0.05)) < 1e-4
        assert sc["delta_calc"] == \
            "target_avg - peer_avg = 0.65 - 0.70 = -0.05"

    def test_589_qualitative_no_scorer(self):
        m = _mechanism_589()
        assert "asymmetry_scorer" not in m
        assert "asymmetry_scorer_result" not in m
        assert m["mechanism_id"] == 589
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scope"] == "qualitative structural mapping only"

    def test_586_monitoring_no_scorer(self):
        # Type E 40th podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        assert (TESTS_DIR / FILE_586).exists()
        assert count_def_tests(FILE_586) == 58
        assert "Fortieth" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_587_and_588_sign_classes_distinct(self):
        # #587 is positive small (null-tie control); #588 is negative
        # near-zero (register constancy). The suite must not conflate a
        # small-positive product-lane boundary with a negative near-zero
        # constancy read.
        r587 = score(TARGET_587, PEER_587, "apple", ["meta"], "gizmodo")
        r588 = score(TARGET_588, PEER_588, "meta", ["samsung/google"],
                     "cnet")
        assert r587.asymmetry_score > 0
        assert r588.asymmetry_score < 0
        assert abs(r587.asymmetry_score) == pytest.approx(0.1334, abs=1e-4)
        assert abs(r588.asymmetry_score) == pytest.approx(0.05, abs=1e-4)
        # |#587|/|#588| ~ 2.67 ratio: distinct magnitudes, distinct families.
        assert 2.5 < abs(r587.asymmetry_score) / abs(r588.asymmetry_score) \
            < 2.9


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #587 is the NINTH agreement-pole pin
# (engine n.s. on real computation AND finding layer refuses, at the
# closest-to-significance engine p yet). #588 is the THIRD
# degenerate-boundary pin (engine refuses structurally via the n<2 guard
# while the finding layer refuses deliberately). Divergence ratchet
# intact: the four divergence pins still hold.
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet590:
    def test_587_engine_real_computation_not_significant(self):
        # NINTH agreement-pole pin: engine runs a REAL Welch computation
        # (n=3 vs n=3, no guard triggered): t=2.1381, p=0.0993 n.s.,
        # d=1.7457, is_significant False on the illustrative arrays. This
        # is the closest-to-significance agreement pin in the corpus
        # (previous: #577 p~0.1021; #582 p=1.0): the pole holds even when
        # the computation flirts with the nominal line.
        r = score(TARGET_587, PEER_587, "apple", ["meta"], "gizmodo")
        assert abs(r.t_statistic - 2.1381) < 1e-3
        assert abs(r.p_value - 0.0993) < 1e-3
        assert r.p_value > 0.05
        assert abs(r.cohens_d - 1.7457) < 1e-3
        assert r.is_significant is False

    def test_587_finding_layer_refuses(self):
        sc = _mechanism_587()["asymmetry_scorer_result"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["confidence_interval"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert "standing rule Aug 28 2026" in sc["methodology"]

    def test_588_engine_degenerate_guard(self):
        # THIRD degenerate-boundary pin: both arms n=1 < 2, so
        # welch_t_test returns the degenerate (t=0.0, p=1.0).
        # is_significant False. cohens_d computes 0.0 (the guard is
        # specific to the t-test path, not the whole engine) - contrast
        # with #578's d = -10.61 (n=2 vs n=1). The guard fires on sample
        # size, not magnitude: |-0.05| is the smallest degenerate delta
        # yet and is still refused.
        r = score(TARGET_588, PEER_588, "meta", ["samsung/google"], "cnet")
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False
        assert r.cohens_d == 0.0

    def test_588_finding_layer_refuses(self):
        # The finding layer refuses deliberately (NOT_CALCULATED), while
        # the engine refuses structurally (degenerate guard) - agreement
        # via different mechanisms, distinct from the divergence family.
        # The delta_direction string records register constancy as a
        # no-claim finding, not a promoted symmetry result.
        sc = _cc_588()["asymmetry_scorer_result_illustrative"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert sc["correlation_not_causation"] is True
        assert abs(sc["delta"] - (-0.05)) < 1e-4
        assert "constancy" in sc["delta_direction"].lower()

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
        # The agreement pole (#587: engine runs real computation, refuses
        # significance at p=0.0993) and the degenerate boundary (#588:
        # engine refuses to compute via the n<2 guard) remain pinned as
        # DISTINCT boundary classes. #587's computed t=2.1381 differs from
        # #588's guard-path return (t=0.0, p=1.0 without computation): the
        # provenance is asserted here via sample sizes and t provenance.
        assert len(TARGET_587) == 3 and len(PEER_587) == 3
        assert len(TARGET_588) == 1 and len(PEER_588) == 1
        r587 = score(TARGET_587, PEER_587, "apple", ["meta"], "gizmodo")
        r588 = score(TARGET_588, PEER_588, "meta", ["samsung/google"],
                     "cnet")
        assert r587.is_significant is False and r588.is_significant is False
        assert r587.t_statistic != 0.0
        assert r588.t_statistic == 0.0


# ---------------------------------------------------------------------------
# New competitor-coverage pattern tests for #587/#588/#589.
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns590:
    def test_587_fourth_gizmodo_null_tie_control(self):
        # #587 completes the FOUR-mechanism Gizmodo null-tie control set:
        # #512 Google, #577 Anthropic, #582 OpenAI, #587 Apple - all at $0
        # tie, all symmetric-adversarial with Meta.
        m = _mechanism_587()
        assert m["mechanism_id"] == 587
        assert "FOURTH" in m["finding"]
        assert "512" in m["finding"]
        assert "577" in m["finding"]
        assert "582" in m["finding"]

    def test_587_first_mechanism_under_gizmodo_apple(self):
        # #587's own novelty claim: first dedicated mechanism under
        # gizmodo.yaml competitor_relationships.apple.
        m = _mechanism_587()
        assert m["publication_focus"].startswith("Gizmodo")
        assert m["asymmetry_scorer_result"]["target_entity"] == "apple"

    def test_587_product_lane_boundary(self):
        # The product-lane reputation-carve boundary distinguishes the
        # glasses lane (Apple-favoring gradient from hardware-sales
        # business model) from the controversy/news register (symmetric).
        m = _mechanism_587()
        assert "product-lane" in m["finding"].lower() or \
            "product lane" in m["finding"].lower()

    def test_588_stein_block_iteration_and_type(self):
        cc = _cc_588()
        assert cc["iteration"] == 588
        assert cc["type"] == "B"

    def test_588_verdict_register_constancy(self):
        # The verdict names register constancy: the same enthusiastic
        # hands-on register for Meta and Samsung/Google.
        cc = _cc_588()
        assert "constancy" in cc["verdict"].lower()

    def test_588_bounds_mechanism_106(self):
        # #588 bounds in-corpus mechanism #106 (Stein enthusiasm gradient
        # with privacy deferral) to the news/launch-keynote register: the
        # gradient does NOT replicate in product hands-ons.
        cc = _cc_588()
        assert "106" in cc["finding"]

    def test_589_first_adversarial_financial_mechanism(self):
        # First negative-sign financial-incentive mechanism in the corpus:
        # a publisher suing the AI lab is the inverse of the licensing-deal
        # incentives that dominate the corpus.
        m = _mechanism_589()
        assert m["mechanism_id"] == 589
        assert "adversarial" in m["mechanism_name"]
        assert "Ziff Davis" in m["mechanism_name"]
        assert "OpenAI" in m["mechanism_name"]

    def test_589_owner_level_cnet_zdnet_tie(self):
        # Owner-level tie: CNET and ZDNET are Ziff Davis properties and
        # corpus-covered publications (#588 CNET, triple-squeeze ZDNET).
        m = _mechanism_589()
        blob = str(m)
        assert "CNET" in blob and "ZDNET" in blob

    def test_589_sue_one_sign_other_contrast(self):
        # The sue-one-sign-the-other contrast (WaPo struck an OpenAI
        # licensing partnership the same week Ziff Davis sued) is pinned
        # as the boundary between adversarial and cooperative incentives.
        text = LOG.read_text(encoding="utf-8")
        assert "WaPo" in text or "Washington Post" in text

    def test_589_iteration_log_marks_negative_sign(self):
        text = LOG.read_text(encoding="utf-8")
        assert "negative-sign" in text or "adversarial" in text.lower()


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 586-589 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep590:
    WINDOW_590 = [FILE_586, FILE_587, FILE_588, FILE_589]

    @pytest.mark.parametrize("fname", WINDOW_590)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 586-590 window, closing the C->D edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carries the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard590:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type D #590 followup: ...") and doc-sync ("Type C #589
    # doc-sync: ...") commits interleave between mains since the #572/#573/#574
    # convention change; the naive newest-5 filter broke on them. The colon
    # immediately after the iteration number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard590.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard590.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#590", "D"),
            ("#589", "C"),
            ("#588", "B"),
            ("#587", "A"),
            ("#586", "E"),
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
# must carry rows for #586-#590 with authoritative def-test counts. The
# #588 README row and both #589 rows were MISSING before this run (miss
# repaired here per the #510 precedent); the #586/#587 rows were synced by
# their own runs. The #585 row (from Type D #585) must not decay.
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_590 = [
    # (iteration, test file, expected def-test count, keyword)
    ("586", FILE_586, 58, "Type E #586"),
    ("587", FILE_587, 47, "Type A #587"),
    ("588", FILE_588, 38, "Type B #588"),
    ("589", FILE_589, 42, "Type C #589"),
]


class TestDocSyncRatchet590:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_590)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_590)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_590)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_585_row_still_present(self):
        # The previous Type D row (from #585) must not decay: #585's row
        # survives into the 586-589 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_585 in readme and FILE_585 in arch

    def test_590_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_590 in text, "README missing row for the #590 file"
        assert "Type D #590" in text

    def test_590_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_590 in text, "ARCHITECTURE missing row for the #590 file"
        assert "Type D #590" in text

    def test_590_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_590)
        line = [l for l in text.splitlines() if FILE_590 in l]
        assert line, f"README row not found for {FILE_590}"
        assert str(actual) in line[0], \
            f"README row for {FILE_590} lacks count {actual}"

    def test_590_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_590)
        line = [l for l in text.splitlines() if FILE_590 in l]
        assert line, f"ARCHITECTURE row for {FILE_590}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_590} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"
