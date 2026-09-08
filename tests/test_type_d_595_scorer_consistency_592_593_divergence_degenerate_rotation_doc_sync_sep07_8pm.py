"""Type D #595 (2026-09-07 20:00 PDT): scorer cross-mechanism consistency
extended to #592/#593 + rotation guard for 591-595 + doc-sync ratchet
+ #594 count miss repair (rotation 594 C -> 595 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (calculate_asymmetry) computes t/p/CI on the logged
arrays, and its MEAN-DIFFERENCE arithmetic must reproduce the logged
manual delta (engine-drift detection). The engine's own significance
output is computed but deliberately NOT promoted to a finding for
illustrative inputs - this file pins that separation for the two newest
quantitative mechanisms, extending the divergence and degenerate-boundary
classes:

- #592 (Type A, Verge x Google adversarial-litigation boundary replication,
  Sep 7 17:00 PDT): Google target [0.0, -0.05, -0.2] avg -0.0833 vs Meta
  peer [-0.55, -0.6, -0.5] avg -0.55. Logged asymmetry_score 0.4667
  (target-minus-peer; engine mean difference 0.466667 rounds to the logged
  value). FIFTH divergence pin: the engine runs a REAL Welch computation
  (n=3 vs n=3, no guard triggered) returning t=7.0, p=0.006857, d=5.715476,
  is_significant True on the illustrative arrays, while the finding layer
  refuses deliberately (p_value NOT_CALCULATED, cohens_d NOT_CALCULATED,
  is_significant False). The divergence ratchet count moves 4 -> 5 (#552
  FIRST, #557 SECOND, #572 THIRD, #573 FOURTH, #592 FIFTH). p=0.006857 is
  the SMALLEST engine p among the divergence pins with pinned engine p
  values (#572 p~0.0299, #573 p~0.0243): the ratchet holds at its most
  engine-significant computation yet. The positive sign (+0.4667, Google
  coverage LESS adversarial than Meta despite PMC suing Google twice) is
  the inversion that bounds the theory: the engine's "significant" verdict
  points AWAY from the naive financial prediction, which is exactly why
  the standing rule refuses to promote it.
- #593 (Type B, Mark Gurman access-journalism register asymmetry, Sep 7
  18:00 PDT): Meta target [-0.15] avg -0.15 vs Apple peer [0.45, 0.35,
  0.35] with raw mean 0.3833 (logged peer_avg 0.4, rounded to 1dp). The
  logged delta -0.55 is computed on the ROUNDED averages (target_avg -
  peer_avg = -0.15 - 0.40 = -0.55, internally consistent per the #593
  file's own test_delta_math_is_consistent); the engine on the raw arrays
  gives -0.5333. This is a ROUNDED-AVG ARITHMETIC DIVERGENCE, bounded at
  0.0167 and verdict-invariant (engine sig False, finding sig False,
  illustrative-only both ways). Pinned as a data-precision note, NOT a
  divergence-ratchet member: the ratchet tracks engine/finding
  significance disagreement, not rounding. Convention recommendation:
  log averages at 4dp like #587/#592 so the logged delta reproduces
  engine arithmetic exactly. FOURTH DEGENERATE-BOUNDARY pin, asymmetric
  variant n=1 vs n=3: the degenerate guard fires when EITHER arm has n<2
  (target arm n=1), so welch_t_test returns (t=0.0, p=1.0),
  is_significant False, while cohens_d computes -9.2376 (nonzero: total
  n=4 > 2 and pooled sd nonzero; the guard is t-path-specific). Second-
  largest |d| in the degenerate class (#578 -10.61 with n=2 vs n=1 is
  largest) and the largest among n=1-arm members; the guard fires on
  sample size, not magnitude.

Sign-class separation: #592 (+0.4667, positive, litigation-boundary
inversion) vs #593 (-0.55 logged / -0.5333 engine, negative,
access-explained register gap). The suite must not conflate a positive
litigation-bounded inversion with a negative access-driven register gap:
|#592|/|#593-logged| = 0.8485 ratio, different mechanism families,
different verdict classes.

- #594 (Type C, News Corp five-leg AI revenue architecture, Sep 7 19:00
  PDT) is the qualitative boundary (mirroring #589 in #590, #584 in #585):
  no asymmetry_scorer section, statistical_discipline carries tone_scores
  NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  scope "qualitative structural mapping only" - scorer consistency
  explicitly does NOT apply. Five legs: openai_leg, meta_leg,
  microsoft_leg, anthropic_leg, bloomberg_leg (bloomberg leg NEW TO
  CORPUS, verified first-hand via the MarketBeat earnings transcript).
- #591 (Type E, podcast 41st verification, Sep 7 16:00 PDT) is the
  monitoring boundary (mirroring #586 in #590): monitoring-only, no
  quantitative mechanism, no scorer extension.

A no-brittle sweep pins that none of the 591-594 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired
in #551 (all four use the presence-assertion convention).

Divergence ratchet: the divergence count moves 4 -> 5 with #592's pin;
the four older pins (#552 in #555, #557 in #560, #572/#573 in #575) are
spot-checked still holding via #572/#573, so the ratchet is active rather
than stale: a NEW divergence beyond the five in the 591-594 window would
have been caught by the per-mechanism assertions.

DOC-SYNC MISS REPAIR: the #594 run's README.md and docs/ARCHITECTURE.md
rows say "43 tests" but the committed file (main commit 290db01, verified
via git show this run) carries 46 def-tests (43 non-guard + 3
rotation-guard; the #594 run's doc row counted 40+3, undercounting the
non-guard tests by 3). Both rows are repaired to 46 here before this run
adds its own #595 rows - the 591-595 window must be fully synced for the
ratchet to mean anything. Mirrors the Type D #510 and #590 miss-repair
precedents. The count_stats.py --check gate is the authoritative arbiter,
and the README top-level stats (Tests / Test files) are refreshed to the
post-run totals.

Rotation guard: the 591-595 window follows A->B->C->D->E->A adjacency in
git-commit order (newest first) as D,C,B,A,E, closing the D->C edge this
run. ANCHORED at this run's commit via the followup-commit convention
established by Type D #565: the main commit carries the
POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
the followup patches it to the real hash. The guard verifies the
rotation was valid AT THAT TIME, which is immutable.

Novelty: zero test_type_d_595 files on disk before this run (glob
verified); no #595 in git log (grep verified); scorer consistency has
never covered #592/#593 (repo grep over scorer-consistency test files
returns only an unrelated "28592 tests" string in #535); the 591-594
rotation window was never guarded; the 586-590 doc-sync window (from
#590) is extended, not duplicated; #592 is the FIFTH divergence pin and
carries the smallest engine p in the divergence class (0.006857); #593 is
the FOURTH degenerate-boundary pin and the first asymmetric (n=1 vs n=3)
variant; the rounded-avg arithmetic divergence (0.0167) is the first
bounded precision note in the consistency series.
The filename embeds the covered iteration numbers (592_593) per the
#555/#560/#565/#570/#575/#580/#585/#590 Type-D filename convention.
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

FILE_595 = ("test_type_d_595_scorer_consistency_592_593_divergence_"
            "degenerate_rotation_doc_sync_sep07_8pm.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_592 = [0.0, -0.05, -0.2]
PEER_592 = [-0.55, -0.6, -0.5]
TARGET_593 = [-0.15]
PEER_593 = [0.45, 0.35, 0.35]
LOGGED_593_PEER_AVG = 0.4
LOGGED_593_DELTA = -0.55

FILE_591 = ("test_type_e_591_podcast_sentiment_fortyfirst_"
            "verification_sep07_4pm.py")
FILE_592 = ("test_type_a_592_verge_google_adversarial_litigation_"
            "boundary_replication_sep07_5pm.py")
FILE_593 = ("test_type_b_593_mark_gurman_access_journalism_register_"
            "asymmetry_sep07_6pm.py")
FILE_594 = ("test_type_c_594_news_corp_five_leg_ai_revenue_"
            "architecture_sep07_7pm.py")
FILE_590 = ("test_type_d_590_scorer_consistency_587_588_agreement_degenerate_"
            "boundary_rotation_doc_sync_sep07_3pm.py")


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


def _mechanism_592():
    with open(REPO_ROOT / "profiles" / "the-verge.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["google"][
        "mechanism_590_verge_google_adversarial_litigation_"
        "boundary_replication"]


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


def _load_gurman():
    data = _load_journalists()
    found = []
    _walk(data, found, "Mark Gurman")
    assert found, "Mark Gurman entry missing from journalists.yaml"
    return found[0]


def _cc_593():
    entry = _load_gurman()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"][
        "type_b_593_mark_gurman_access_journalism_register_asymmetry"]


def _mechanism_594():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["news_corp_five_leg_ai_revenue_architecture_594"]


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


class TestIteration595Metadata:
    def test_docstring_ids(self):
        assert "#595" in __doc__
        assert "2026-09-07 20:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # This run closes the C->D edge: previous main commit is #594 Type C,
        # this run is #595 Type D.
        assert "594 C -> 595 D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_595

    def test_covered_iterations_in_filename(self):
        assert "592_593" in FILE_595

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#595 Type D" in text

    def test_docstring_names_fifth_divergence_and_fourth_degenerate(self):
        assert "FIFTH divergence" in __doc__
        assert "FOURTH DEGENERATE-BOUNDARY" in __doc__

    def test_docstring_names_miss_repair(self):
        assert "DOC-SYNC MISS REPAIR" in __doc__


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: #592 FIFTH divergence pin, #593
# FOURTH degenerate-boundary pin + rounded-avg arithmetic divergence note,
# #594 qualitative boundary, #591 monitoring boundary.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency595:
    def test_592_delta_reproduced(self):
        # FIFTH divergence pin: the engine's mean-difference arithmetic
        # reproduces the logged delta (0.4667 rounded from 0.466667).
        r = score(TARGET_592, PEER_592, "google", ["meta"], "the-verge")
        assert abs(r.asymmetry_score - 0.4667) < 1e-4

    def test_592_logged_avgs_match_engine(self):
        r = score(TARGET_592, PEER_592, "google", ["meta"], "the-verge")
        assert abs(r.target_avg_tone - (-0.0833)) < 1e-3
        assert abs(r.peer_avg_tone - (-0.55)) < 1e-3

    def test_592_logged_result_byte_match(self):
        sc = _mechanism_592()["asymmetry_scorer_result"]
        assert sc["target_avg_tone"] == pytest.approx(-0.0833, abs=1e-9)
        assert sc["peer_avg_tone"] == pytest.approx(-0.55, abs=1e-9)
        assert sc["asymmetry_score"] == pytest.approx(0.4667, abs=1e-9)
        assert sc["target_entity"] == "google"
        assert sc["peer_entities"] == ["meta"]

    def test_592_article_tones_match_engine_inputs(self):
        arts = _mechanism_592()["articles"]
        assert len(arts) == 6
        tones = [a["manual_illustrative_tone"] for a in arts]
        assert tones[:3] == pytest.approx(TARGET_592, abs=1e-9)
        assert tones[3:] == pytest.approx(PEER_592, abs=1e-9)

    def test_593_engine_delta_on_raw_arrays(self):
        # The engine on the RAW peer_scores gives -0.5333, not the logged
        # -0.55: the logged value was computed on the rounded peer_avg.
        r = score(TARGET_593, PEER_593, "Meta", ["Apple"], "bloomberg")
        assert abs(r.asymmetry_score - (-0.5333)) < 1e-4
        assert abs(r.target_avg_tone - (-0.15)) < 1e-9
        assert abs(r.peer_avg_tone - 0.383333) < 1e-4

    def test_593_logged_values_internally_consistent(self):
        # The YAML finding layer is internally consistent: delta equals
        # target_avg minus peer_avg on the LOGGED (rounded) values, exactly
        # as the #593 file's own test_delta_math_is_consistent asserts.
        sc = _cc_593()["asymmetry_scorer_result_illustrative"]
        assert sc["target_avg"] == pytest.approx(-0.15, abs=1e-9)
        assert sc["peer_avg"] == pytest.approx(LOGGED_593_PEER_AVG,
                                               abs=1e-9)
        assert sc["delta"] == pytest.approx(LOGGED_593_DELTA, abs=1e-9)
        assert abs(sc["delta"] - (sc["target_avg"] - sc["peer_avg"])) < 1e-9
        assert sc["delta_calc"] == \
            "target_avg - peer_avg = -0.15 - 0.40 = -0.55"

    def test_593_rounding_divergence_bounded_and_verdict_invariant(self):
        # Rounded-avg arithmetic divergence: |logged -0.55 - engine
        # -0.5333| = 0.0167. Bounded under 0.02 and verdict-invariant:
        # both engine and finding refuse significance on this pair, and
        # both are illustrative-only. A precision note, not a ratchet
        # member.
        r = score(TARGET_593, PEER_593, "Meta", ["Apple"], "bloomberg")
        sc = _cc_593()["asymmetry_scorer_result_illustrative"]
        drift = abs(sc["delta"] - r.asymmetry_score)
        assert drift == pytest.approx(0.0167, abs=1e-3)
        assert drift < 0.02
        assert r.is_significant is False
        assert sc["is_significant"] is False

    def test_593_logged_peer_avg_is_1dp_rounded(self):
        # Root cause of the arithmetic divergence: peer_avg is logged at
        # 1dp (0.4) while the raw peer_scores mean is 0.3833. The
        # recommendation (4dp logging, as in #587/#592) is recorded in the
        # module docstring.
        sc = _cc_593()["asymmetry_scorer_result_illustrative"]
        raw_mean = sum(PEER_593) / len(PEER_593)
        assert abs(sc["peer_avg"] - 0.4) < 1e-9
        assert abs(raw_mean - 0.383333) < 1e-4
        assert abs(sc["peer_avg"] - raw_mean) > 0.01

    def test_594_qualitative_no_scorer(self):
        m = _mechanism_594()
        assert "asymmetry_scorer" not in m
        assert "asymmetry_scorer_result" not in m
        assert m["mechanism_id"] == 594
        assert m["iteration_type"] == "C"
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scope"] == "qualitative structural mapping only"

    def test_591_monitoring_no_scorer(self):
        # Type E 41st podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        assert (TESTS_DIR / FILE_591).exists()
        assert count_def_tests(FILE_591) == 68
        assert "Forty-first" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_592_and_593_sign_classes_distinct(self):
        # #592 is positive (litigation-boundary inversion); #593 is
        # negative (access-explained register gap). The suite must not
        # conflate a positive litigation-bounded inversion with a negative
        # access-driven register gap.
        r592 = score(TARGET_592, PEER_592, "google", ["meta"], "the-verge")
        assert r592.asymmetry_score > 0
        assert LOGGED_593_DELTA < 0
        assert abs(r592.asymmetry_score) == pytest.approx(0.4667, abs=1e-4)
        assert abs(LOGGED_593_DELTA) == pytest.approx(0.55, abs=1e-4)
        # |#592|/|#593-logged| ~ 0.8485 ratio: distinct magnitudes,
        # distinct families.
        assert 0.83 < abs(r592.asymmetry_score) / abs(LOGGED_593_DELTA) \
            < 0.87


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #592 is the FIFTH divergence pin
# (engine significant on illustrative arrays AND finding layer refuses, at
# the smallest engine p in the class). #593 is the FOURTH
# degenerate-boundary pin (engine refuses structurally via the either-arm
# n<2 guard while the finding layer refuses deliberately, with nonzero d).
# Divergence ratchet intact: the four older divergence pins still hold.
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet595:
    def test_592_engine_divergence_fifth(self):
        # FIFTH divergence: the engine claims significance on the
        # illustrative arrays (t=7.0, p=0.006857 < 0.05, d=5.715476,
        # is_significant True). Smallest engine p among the divergence
        # pins with pinned engine p values (#572 p~0.0299, #573 p~0.0243).
        r = score(TARGET_592, PEER_592, "google", ["meta"], "the-verge")
        assert abs(r.t_statistic - 7.0) < 1e-6
        assert abs(r.p_value - 0.006857) < 1e-4
        assert r.p_value < 0.05
        assert abs(r.cohens_d - 5.715476) < 1e-4
        assert r.is_significant is True

    def test_592_finding_layer_refuses(self):
        m = _mechanism_592()
        sc = m["asymmetry_scorer_result"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["confidence_interval"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        # The standing-rule citation lives in statistical_discipline for
        # #592 (the scorer methodology string carries the MANUAL
        # ILLUSTRATIVE ONLY framing instead).
        assert "standing rule Aug 28 2026" in m["statistical_discipline"]

    def test_593_engine_degenerate_guard(self):
        # FOURTH degenerate-boundary pin, asymmetric variant n=1 vs n=3:
        # the guard fires because the TARGET arm has n=1 < 2 (either-arm
        # rule), so welch_t_test returns the degenerate (t=0.0, p=1.0),
        # is_significant False. cohens_d computes -9.2376 (nonzero: total
        # n=4 > 2, pooled sd nonzero; the guard is specific to the t-test
        # path). Second-largest |d| in the degenerate class (#578 -10.61
        # is largest) and the largest among n=1-arm members.
        r = score(TARGET_593, PEER_593, "Meta", ["Apple"], "bloomberg")
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False
        assert abs(r.cohens_d - (-9.2376)) < 1e-3

    def test_593_finding_layer_refuses(self):
        # The finding layer refuses deliberately (NOT_CALCULATED), while
        # the engine refuses structurally (degenerate guard) - agreement
        # via different mechanisms, distinct from the divergence family.
        sc = _cc_593()["asymmetry_scorer_result_illustrative"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert sc["correlation_not_causation"] is True
        assert sc["delta"] == pytest.approx(-0.55, abs=1e-9)

    def test_divergence_ratchet_still_holds_572(self):
        # THIRD divergence pin (#575) still active: engine claims
        # significance on the illustrative pair while the finding layer
        # refuses. A NEW divergence beyond the five would have been caught
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

    def test_divergence_and_degenerate_classes_distinct(self):
        # The divergence class (#592: engine COMPUTES significance,
        # t=7.0) and the degenerate boundary (#593: engine REFUSES to
        # compute, guard-path t=0.0/p=1.0) remain pinned as DISTINCT
        # boundary classes. #592's computed t differs from #593's
        # guard-path return without computation: the provenance is
        # asserted here via t provenance and sample sizes.
        assert len(TARGET_592) == 3 and len(PEER_592) == 3
        assert len(TARGET_593) == 1 and len(PEER_593) == 3
        r592 = score(TARGET_592, PEER_592, "google", ["meta"], "the-verge")
        r593 = score(TARGET_593, PEER_593, "Meta", ["Apple"], "bloomberg")
        assert r592.is_significant is True and r593.is_significant is False
        assert r592.t_statistic != 0.0
        assert r593.t_statistic == 0.0


# ---------------------------------------------------------------------------
# New competitor-coverage pattern tests for #592/#593/#594.
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns595:
    def test_592_mechanism_identity(self):
        m = _mechanism_592()
        # mechanism_id (590) and iteration (592) are separate sequences:
        # #592 is the iteration, mechanism #590 is the mechanism number.
        assert m["mechanism_id"] == 590
        assert m["iteration"] == 592
        assert m["iteration_type"] == "A"
        assert m["entity_pair"] == "Google vs Meta"
        assert len(m["articles"]) == 6
        assert len(m["confounders"]) == 8
        assert len(m["counter_evidence"]) == 4
        assert len(m["source_urls"]) == 4

    def test_592_litigation_domain_control(self):
        # The litigation-domain control is the structural core of the
        # boundary: two PMC suits against Google, adversarial posture
        # confined to the litigation domain.
        m = _mechanism_592()
        ldc = m["litigation_domain_control"]
        assert "ai_overviews_suit" in ldc
        assert "adtech_suit" in ldc

    def test_592_positive_sign_inversion(self):
        # The delta sign is POSITIVE (+0.4667, Google coverage less
        # adversarial than Meta) despite PMC suing Google twice - the
        # inversion that bounds the theory, replicated from NYT #471.
        m = _mechanism_592()
        assert m["asymmetry_scorer_result"]["asymmetry_score"] > 0
        blob = str(m["distinct_from"])
        assert "471" in blob

    def test_592_second_adversarial_posture_pin(self):
        # #592 is the second adversarial-posture boundary pin after #471
        # (NYT single OpenAI suit); PMC's dual-suit posture is stronger
        # and the boundary still holds.
        m = _mechanism_592()
        blob = str(m)
        assert "471" in blob

    def test_593_gurman_block_iteration_and_type(self):
        cc = _cc_593()
        assert cc["iteration"] == 593
        assert cc["type"] == "B"

    def test_593_corpus_sizes(self):
        # n=1 Meta item vs n=3 Apple items: the asymmetric sample that
        # triggers the degenerate guard on the target arm.
        cc = _cc_593()
        assert len(cc["meta_corpus"]) == 1
        assert len(cc["apple_corpus"]) == 3

    def test_593_verdict_boundary_null(self):
        # The verdict names the BOUNDARY/NULL pin: within one
        # access-dependent journalist, the gap is access-explained, not
        # money-explained.
        cc = _cc_593()
        assert cc["verdict"].startswith("BOUNDARY/NULL")
        assert "access" in cc["verdict"].lower()

    def test_593_cross_refs_falsification_family(self):
        # #593 joins the reporter-level falsification/alternative-driver
        # family (#538 Metz) and the genre-boundary family (#588 Stein),
        # with the #85 Bloomberg financial-null baseline and the #421
        # Knight same-lane sibling.
        cc = _cc_593()
        refs = " ".join(cc["cross_refs"])
        for num in ("#85", "#471", "#538", "#588", "#421"):
            assert num in refs, f"{num} missing from cross_refs"

    def test_593_hypothesis_null_deal_gradient(self):
        # The deal-gradient prediction is NULL (no deals either side), so
        # the financial theory predicts no gap: the observed gap must come
        # from access economics.
        cc = _cc_593()
        assert "NULL" in cc["hypothesis"]

    def test_594_five_legs(self):
        m = _mechanism_594()
        assert m["mechanism_id"] == 594
        assert list(m["legs"].keys()) == [
            "openai_leg", "meta_leg", "microsoft_leg",
            "anthropic_leg", "bloomberg_leg",
        ]

    def test_594_bloomberg_leg_new_to_corpus(self):
        # The Bloomberg expanded Dow Jones AI-rights leg is NEW TO CORPUS:
        # zero prior corpus mentions (grep verified at the #594 run), now
        # buyer-side-qualifying the #85 Bloomberg financial-null baseline.
        m = _mechanism_594()
        assert "bloomberg_leg" in m["legs"]
        assert "Bloomberg" in m["mechanism_name"]

    def test_594_predictions_not_findings(self):
        # The mechanism states directional predictions as testable
        # hypotheses for future Type A/B work, not as findings - the
        # qualitative discipline that keeps Type C honest.
        m = _mechanism_594()
        assert m["predictions_not_findings"] is True
        assert m["correlational_note"] is not None

    def test_594_meta_leg_neutralizes_wsj_prediction(self):
        # Key prediction note: the Meta leg NEUTRALIZES any
        # Meta-adversarial prediction for WSJ - News Corp is the dual-payer
        # template per #519/#549, unlike Conde Nast.
        blob = str(_mechanism_594())
        assert "dual-payer" in blob


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 591-594 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep595:
    WINDOW_595 = [FILE_591, FILE_592, FILE_593, FILE_594]

    @pytest.mark.parametrize("fname", WINDOW_595)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 591-595 window, closing the C->D edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carries the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard595:
    ANCHORED_COMMIT = "8fed1125e9bf74a51034183737acee8abd82d979"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type D #595 followup: ...") and doc-sync ("Type C #594
    # doc-sync: ...") commits interleave between mains since the #572/#573/#574
    # convention change; the naive newest-5 filter broke on them. The colon
    # immediately after the iteration number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard595.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard595.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#595", "D"),
            ("#594", "C"),
            ("#593", "B"),
            ("#592", "A"),
            ("#591", "E"),
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
# must carry rows for #591-#595 with authoritative def-test counts. The
# #594 rows said 43 but the committed file has 46 def-tests (miss repaired
# here per the #510/#590 precedent). The #590 row (from Type D #590) must
# not decay. count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_595 = [
    # (iteration, test file, expected def-test count, keyword)
    ("591", FILE_591, 68, "Type E #591"),
    ("592", FILE_592, 41, "Type A #592"),
    ("593", FILE_593, 29, "Type B #593"),
    ("594", FILE_594, 46, "Type C #594"),
]


class TestDocSyncRatchet595:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_595)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_595)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_595)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_590_row_still_present(self):
        # The previous Type D row (from #590) must not decay: #590's row
        # survives into the 591-594 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_590 in readme and FILE_590 in arch

    def test_595_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_595 in text, "README missing row for the #595 file"
        assert "Type D #595" in text

    def test_595_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_595 in text, "ARCHITECTURE missing row for the #595 file"
        assert "Type D #595" in text

    def test_595_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_595)
        line = [l for l in text.splitlines() if FILE_595 in l]
        assert line, f"README row not found for {FILE_595}"
        assert str(actual) in line[0], \
            f"README row for {FILE_595} lacks count {actual}"

    def test_595_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_595)
        line = [l for l in text.splitlines() if FILE_595 in l]
        assert line, f"ARCHITECTURE row for {FILE_595}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_595} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"
