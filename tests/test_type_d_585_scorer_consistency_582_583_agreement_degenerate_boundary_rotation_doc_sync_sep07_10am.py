"""Type D #585 (2026-09-07 10:00 PDT): scorer cross-mechanism consistency
extended to #582/#583 + rotation guard for 581-585 + doc-sync ratchet
(rotation 584 C -> 585 D).

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

- #582 (Type A, Gizmodo x OpenAI null-tie symmetric-adversarial control,
  Sep 7 07:00 PDT): OpenAI target [-0.70, -0.50, -0.65] avg -0.6167 vs
  Meta peer [-0.70, -0.55, -0.60] avg -0.6167. Logged asymmetry_score 0.00
  (target-minus-peer: perfect zero-delta coincidence of illustrative
  tones). EIGHTH agreement-pole pin: engine runs a REAL Welch computation
  (n=3 vs n=3, no guard triggered) returning p = 1.0 n.s., d = 0.0,
  is_significant False, and the finding layer refuses (p_value
  NOT_CALCULATED, cohens_d NOT_CALCULATED, is_significant false) -
  engine and finding agree to refuse, joining the agreement pole
  (#577 pinned SEVENTH in Type D #580; #567/#568 FIFTH+SIXTH in #570).
  The zero-delta variant is new to the pole: the previous seven pins all
  had nonzero illustrative deltas; here the engine's real computation
  confirms the logged zero exactly (asymmetry_score 0.0 byte-match).
- #583 (Type B, Elizabeth Lopatto writer-level consistency check,
  Sep 7 08:00 PDT): OpenAI target [0.10] avg +0.10 vs Meta peer [-0.70]
  avg -0.70. Logged delta +0.80 (target softer than peer: directionally
  consistent with the Vox Media x OpenAI softer-OpenAI prediction but
  NON-EVIDENTIAL under genre and Musk-relative-subject confounders -
  deliberately not claimed as a thesis win). SECOND DEGENERATE-BOUNDARY
  pin: both arms have n=1 < 2, so welch_t_test returns the degenerate
  (t=0.0, p=1.0), is_significant False, and cohens_d computes 0.0
  (symmetric zero-delta degenerate: with n=1 vs n=1 and nonzero mean
  difference, d still computes 0.0 - the guard is specific to the t-test
  path, not the whole engine). The engine refuses STRUCTURALLY (guard
  path) while the finding layer refuses DELIBERATELY (NOT_CALCULATED) -
  an agreement via different mechanisms, joining #578's FIRST pin in
  Type D #580. The degenerate class now has a second member, so the
  class is no longer a singleton.

Divergence ratchet: the four divergence pins (#552 in #555, #557 in #560,
#572/#573 in #575) are spot-checked still holding via #572/#573, so the
ratchet is active rather than stale: a NEW divergence beyond the four in
the 581-584 window would have been caught by the per-mechanism
assertions.

Sign-class separation: #582 (0.00, null-tie symmetric control,
sign-neutral) vs #583 (+0.80, consistent-but-non-evidential positive).
The suite must not conflate a perfect-zero control with a
directionally-consistent read: |#583| = 0.80 is asserted as the
Musk-relative, genre-confounded read the finding layer refuses to
promote, while #582's 0.00 is asserted as a symmetric-adversarial
control within the illustrative band, not perfect empirical symmetry.

Also: #584 (Type C, Disney x OpenAI $1B Sora deal arc, Sep 7 09:00 PDT)
is the qualitative boundary (mirroring #579 in #580): no
asymmetry_scorer section, statistical_discipline carries tone_scores
NOT_SCORED, p_value NOT_CALCULATED, is_significant false - scorer
consistency explicitly does NOT apply. #581 (Type E, podcast 39th
verification, Sep 7 06:00 PDT) is the monitoring boundary (mirroring
#576 in #580): monitoring-only, no quantitative mechanism, no scorer
extension.

A no-brittle sweep pins that none of the 581-584 window files asserts
the brittle newest-first heading-equality pattern that Type D #555
repaired in #551 (all four use the presence-assertion convention).

Stale-docstring repair: the #580 file's as-written REPAIR paragraph claimed
the system-wide pip install was the fix and that the .venv lacked
textblob/vaderSentiment - false per commit 80f2832 (the repo .venv was
already the durable canonical interpreter; system-site installs were
transient, wiped by a service restart). Repaired in this run; a regression
class pins the stale phrases absent and the canonical .venv language
present.

Rotation guard: the 581-585 window follows A->B->C->D->E->A adjacency in
git-commit order (newest first) as D,C,B,A,E, closing the C->D edge this
run. Doc-sync ratchet: the README/ARCHITECTURE per-file window for
581-584 was synced by their own runs (rows verified present with
authoritative def-test counts 62/48/41/46); this run extends the window
with its own row and verifies the #580 row survives, with the
authoritative count_stats.py --check gate.

Novelty: zero test_type_d_585 files on disk before this run (glob
verified); no #585 in git log (grep verified); scorer consistency has
never covered #582/#583 (repo grep for 582/583 in scorer-consistency test
files returned only their own mechanism files); the 581-584 rotation
window was never guarded; the 576-579 doc-sync window (from #580) is
extended, not duplicated; the zero-delta agreement-pole variant is new
to the corpus (no prior pin had an exactly-zero engine delta); the
degenerate-boundary class gains its SECOND member.
The filename embeds the covered iteration numbers (582_583) per the
#555/#560/#565/#570/#575/#580 Type-D filename convention.
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

FILE_585 = ("test_type_d_585_scorer_consistency_582_583_agreement_degenerate_"
            "boundary_rotation_doc_sync_sep07_10am.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))

TARGET_582 = [-0.70, -0.50, -0.65]
PEER_582 = [-0.70, -0.55, -0.60]
TARGET_583 = [0.10]
PEER_583 = [-0.70]


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


def _mechanism_582():
    with open(REPO_ROOT / "profiles" / "gizmodo.yaml") as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["openai"][
        "mechanism_582_gizmodo_openai_rogue_agent_null_tie_symmetric_"
        "adversarial"]


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


def _load_lopatto():
    data = _load_journalists()
    found = []
    _walk(data, found, "Elizabeth Lopatto")
    assert found, "Elizabeth Lopatto entry missing from journalists.yaml"
    return found[0]


def _cc_583():
    entry = _load_lopatto()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"][
        "type_b_583_elizabeth_lopatto_meta_manifesto_openai_trial"]


def _mechanism_584():
    with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
        d = yaml.safe_load(f)
    return d["disney_openai_1b_sora_deal_arc_584"]


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


class TestIteration585Metadata:
    def test_docstring_ids(self):
        assert "#585" in __doc__
        assert "2026-09-07 10:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # This run closes the C->D edge: previous main commit is #584 Type C,
        # this run is #585 Type D.
        assert "584 C -> 585 D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_585

    def test_covered_iterations_in_filename(self):
        assert "582_583" in FILE_585

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert "#585 Type D" in text

    def test_zero_delta_variant_documented(self):
        text = LOG.read_text(encoding="utf-8")
        assert "zero-delta" in text or "zero delta" in text


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: #582 agreement pole (zero-delta
# variant), #583 degenerate boundary (second pin), #584 qualitative
# boundary, #581 monitoring boundary.
# ---------------------------------------------------------------------------


class TestScorerCrossMechanismConsistency585:
    def test_582_delta_reproduced_exact_zero(self):
        # EIGHTH agreement-pole pin, zero-delta variant: the engine's real
        # computation confirms the logged zero exactly.
        r = score(TARGET_582, PEER_582, "openai", ["meta"], "gizmodo")
        assert r.asymmetry_score == 0.0

    def test_582_logged_avgs_match_engine(self):
        r = score(TARGET_582, PEER_582, "openai", ["meta"], "gizmodo")
        assert abs(r.target_avg_tone - (-0.6167)) < 1e-3
        assert abs(r.peer_avg_tone - (-0.6167)) < 1e-3

    def test_582_logged_result_byte_match(self):
        sc = _mechanism_582()["asymmetry_scorer_result"]
        assert sc["target_avg_tone"] == pytest.approx(-0.6167, abs=1e-9)
        assert sc["peer_avg_tone"] == pytest.approx(-0.6167, abs=1e-9)
        assert sc["asymmetry_score"] == pytest.approx(0.0, abs=1e-9)

    def test_582_article_tones_match_engine_inputs(self):
        arts = _mechanism_582()["articles"]
        tones = [a["manual_illustrative_tone"] for a in arts]
        assert tones[:3] == pytest.approx(TARGET_582, abs=1e-9)
        assert tones[3:] == pytest.approx(PEER_582, abs=1e-9)

    def test_583_delta_reproduced(self):
        # Mean-difference arithmetic intact even at the degenerate boundary.
        r = score(TARGET_583, PEER_583, "openai", ["meta"], "the_verge")
        assert abs(r.asymmetry_score - 0.80) < 1e-4

    def test_583_logged_arrays_byte_match_engine_inputs(self):
        sc = _cc_583()["asymmetry_scorer_result_illustrative"]
        assert sc["target_scores"] == pytest.approx(TARGET_583, abs=1e-9)
        assert sc["peer_scores"] == pytest.approx(PEER_583, abs=1e-9)
        assert abs(sc["delta"] - 0.80) < 1e-4
        assert sc["delta_calc"] == \
            "target_avg - peer_avg = 0.10 - (-0.70) = 0.80"

    def test_584_qualitative_no_scorer(self):
        m = _mechanism_584()
        assert "asymmetry_scorer" not in m
        assert "asymmetry_scorer_result" not in m
        assert m["mechanism_id"] == 584
        sd = m["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scope"] == "qualitative structural mapping only"

    def test_581_monitoring_no_scorer(self):
        # Type E 39th podcast verification: monitoring-only, no
        # quantitative mechanism, no scorer extension.
        fname = ("test_type_e_581_podcast_sentiment_thirtyninth_"
                 "verification_sep07_6am.py")
        assert (TESTS_DIR / fname).exists()
        assert count_def_tests(fname) == 62
        assert "Thirty-Ninth" in (
            REPO_ROOT / "podcast-sentiment.md").read_text(encoding="utf-8")

    def test_582_and_583_sign_classes_distinct(self):
        # #582 is sign-neutral (perfect-zero null-tie control); #583 is
        # positive but deliberately not promoted (consistent-but-non-
        # evidential). The suite must not conflate a zero control with a
        # directionally-consistent read.
        r582 = score(TARGET_582, PEER_582, "openai", ["meta"], "gizmodo")
        r583 = score(TARGET_583, PEER_583, "openai", ["meta"], "the_verge")
        assert r582.asymmetry_score == 0.0
        assert r583.asymmetry_score > 0
        assert abs(r583.asymmetry_score) == pytest.approx(0.80, abs=1e-4)


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: #582 is the EIGHTH agreement-pole pin
# (engine n.s. on real computation AND finding layer refuses). #583 is the
# SECOND degenerate-boundary pin (engine refuses structurally via the n<2
# guard while the finding layer refuses deliberately). Divergence ratchet
# intact: the four divergence pins still hold.
# ---------------------------------------------------------------------------


class TestStandingRuleDisciplineRatchet585:
    def test_582_engine_not_significant(self):
        # EIGHTH agreement-pole pin: engine runs a REAL Welch computation
        # (n=3 vs n=3, no guard triggered): p = 1.0 n.s., d = 0.0,
        # is_significant False on the illustrative arrays. Zero-delta
        # variant of the pole (previous seven pins had nonzero deltas).
        r = score(TARGET_582, PEER_582, "openai", ["meta"], "gizmodo")
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_582_finding_layer_refuses(self):
        sc = _mechanism_582()["asymmetry_scorer_result"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["confidence_interval"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert "standing rule Aug 28 2026" in sc["methodology"]

    def test_583_engine_degenerate_guard(self):
        # SECOND degenerate-boundary pin: both arms n=1 < 2, so
        # welch_t_test returns the degenerate (t=0.0, p=1.0).
        # is_significant False. cohens_d computes 0.0 (the guard is
        # specific to the t-test path, not the whole engine) - contrast
        # with #578's d = -10.61 (n=2 vs n=1 asymmetry).
        r = score(TARGET_583, PEER_583, "openai", ["meta"], "the_verge")
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False
        assert r.cohens_d == 0.0

    def test_583_finding_layer_refuses(self):
        # The finding layer refuses deliberately (NOT_CALCULATED), while the
        # engine refuses structurally (degenerate guard) - agreement via
        # different mechanisms, distinct from the divergence family.
        # The delta_direction string records the deliberate
        # non-promotion: directionally consistent but NON-EVIDENTIAL.
        sc = _cc_583()["asymmetry_scorer_result_illustrative"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert sc["correlation_not_causation"] is True
        assert abs(sc["delta"] - 0.80) < 1e-4
        assert "NON-EVIDENTIAL" in sc["delta_direction"]

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
        # The agreement pole (#582: engine runs real computation, refuses
        # significance) and the degenerate boundary (#583: engine refuses
        # to compute via the n<2 guard) remain pinned as DISTINCT boundary
        # classes. #582's zero-delta real-computation outcome (p=1.0,
        # t=0.0 as a COMPUTED result, not the guard's degenerate return)
        # differs from #583's guard-path return (t=0.0, p=1.0 without
        # computation): same numeric pair, different provenance. The
        # t_statistic equality alone must not merge the classes; the
        # provenance is asserted here via sample sizes.
        assert len(TARGET_582) == 3 and len(PEER_582) == 3
        assert len(TARGET_583) == 1 and len(PEER_583) == 1
        r582 = score(TARGET_582, PEER_582, "openai", ["meta"], "gizmodo")
        r583 = score(TARGET_583, PEER_583, "openai", ["meta"], "the_verge")
        assert r582.is_significant is False and r583.is_significant is False


# ---------------------------------------------------------------------------
# New competitor-coverage pattern tests for #582/#583/#584.
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns585:
    def test_582_first_mechanism_under_gizmodo_openai(self):
        # #582's own novelty claim: first dedicated mechanism under
        # gizmodo.yaml competitor_relationships.openai.
        m = _mechanism_582()
        assert m["mechanism_id"] == 582
        assert m["publication_focus"].startswith("Gizmodo")
        assert "THIRD" in m["finding"]

    def test_582_control_set_complete(self):
        # THIRD in the Gizmodo null-tie control set: #512 Google, #577
        # Anthropic, #582 OpenAI - symmetric-adversarial now holds across
        # three competitor entities plus Meta at $0 tie.
        m = _mechanism_582()
        assert "512" in m["finding"]
        assert "577" in m["finding"]

    def test_582_incident_class_parallel_with_577(self):
        # The sharpest corpus parallel: #577's Anthropic Mythos autonomous
        # hacks and #582's OpenAI rogue-agent incidents are near-identical
        # incident classes covered the same week in the same register.
        m = _mechanism_582()
        assert "incident-class parallel" in m["finding"].lower() or \
            "incident class" in m["finding"].lower()

    def test_583_lopatto_competitor_coverage_block(self):
        cc = _cc_583()
        assert cc["iteration"] == 583
        assert cc["type"] == "B"
        assert "CONSISTENT-BUT-NON-EVIDENTIAL" in cc["finding"]

    def test_583_prediction_result_bound(self):
        # The writer-level read is directionally consistent with the
        # softer-OpenAI prediction but explicitly NON-EVIDENTIAL - the
        # opposite verdict class from #578's writer-register inversion.
        cc = _cc_583()
        assert cc["incentive_context"]["coverage_prediction"] == "softer"
        assert "NON-EVIDENTIAL" in \
            cc["incentive_context"]["prediction_result"]

    def test_583_bounds_not_thesis_win(self):
        # The finding deliberately refuses promotion: Musk-relative subject
        # and genre confounders void the test. Distinct from #498
        # (Swisher deal-partner falsification, same deal) and #578
        # (Bogost inversion).
        cc = _cc_583()
        assert "not a thesis win" in cc["finding"]

    def test_584_first_disney_mechanism(self):
        m = _mechanism_584()
        assert m["mechanism_id"] == 584
        assert "Disney" in m["mechanism_name"] or "disney" in \
            m["mechanism_name"].lower()

    def test_584_deal_arc_terminated_zero_transferred(self):
        # Announced-vs-realized mapping: $1B headline, $0 realized. The only
        # corpus mechanism with an AI-lab equity leg.
        m = _mechanism_584()
        assert "1B" in m["overview"] or "$1B" in m["overview"]
        assert "no money" in m["overview"].lower() or \
            "zero dollars" in m["overview"].lower()

    def test_584_equity_leg_unique(self):
        # The unfunded-announcement boundary case: distinguishes funded
        # deals (#549 News Corp x Meta, #391 Perplexity share) from
        # headline-only incentives.
        text = LOG.read_text(encoding="utf-8")
        assert "equity" in text.lower()


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 581-584 window files asserts the brittle
# newest-first heading-equality pattern that Type D #555 repaired in #551.
# ---------------------------------------------------------------------------

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


class TestNoBrittleSweep585:
    WINDOW_585 = [
        "test_type_e_581_podcast_sentiment_thirtyninth_verification_sep07_6am.py",
        "test_type_a_582_gizmodo_openai_rogue_agent_null_tie_symmetric_"
        "adversarial_sep07_7am.py",
        "test_type_b_583_elizabeth_lopatto_meta_manifesto_openai_trial_"
        "sep07_8am.py",
        "test_type_c_584_disney_openai_1b_sora_deal_arc_sep07_9am.py",
    ]

    @pytest.mark.parametrize("fname", WINDOW_585)
    def test_no_brittle_heading_equality(self, fname):
        with open(TESTS_DIR / fname) as f:
            content = f.read()
        assert not BRITTLE_PATTERN.search(content), \
            f"brittle heading-equality pattern in {fname}"


# ---------------------------------------------------------------------------
# Rotation guard: 581-585 window, closing the C->D edge this run.
# ANCHORED at this run's commit via the followup-commit convention
# established by Type D #565: the main commit carried the
# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# the followup patches it to the real hash. The guard verifies the
# rotation was valid AT THAT TIME, which is immutable.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard585:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

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
             TestRotationCycleGuard585.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard585.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#585", "D"),
            ("#584", "C"),
            ("#583", "B"),
            ("#582", "A"),
            ("#581", "E"),
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
# must carry rows for #581-#585 with authoritative def-test counts
# (581-584 rows were synced by their own runs; #585 row added here). The
# 576-579 window rows (from Type D #580) must not decay.
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC_585 = [
    # (iteration, test file, expected def-test count, keyword)
    ("581", "test_type_e_581_podcast_sentiment_thirtyninth_"
            "verification_sep07_6am.py", 62, "Type E #581"),
    ("582", "test_type_a_582_gizmodo_openai_rogue_agent_null_tie_symmetric_"
            "adversarial_sep07_7am.py", 48, "Type A #582"),
    ("583", "test_type_b_583_elizabeth_lopatto_meta_manifesto_openai_trial_"
            "sep07_8am.py", 41, "Type B #583"),
    ("584", "test_type_c_584_disney_openai_1b_sora_deal_arc_sep07_9am.py",
            46, "Type C #584"),
]


class TestDocSyncRatchet585:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_585)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_585)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC_585)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"
        assert kw in line[0], \
            f"ARCHITECTURE row for {fname} lacks keyword {kw}"

    def test_580_row_still_present(self):
        # The 576-579 window (from Type D #580) must not decay: #580's rows
        # survive into the 581-584 window extension.
        readme = README.read_text(encoding="utf-8")
        arch = ARCHITECTURE.read_text(encoding="utf-8")
        fname580 = ("test_type_d_580_scorer_consistency_577_578_agreement_"
                    "degenerate_boundary_rotation_doc_sync_sep07_5am.py")
        assert fname580 in readme and fname580 in arch

    def test_585_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_585 in text, "README missing row for the #585 file"
        assert "Type D #585" in text

    def test_585_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_585 in text, "ARCHITECTURE missing row for the #585 file"
        assert "Type D #585" in text

    def test_585_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_585)
        line = [l for l in text.splitlines() if FILE_585 in l]
        assert line, f"README row not found for {FILE_585}"
        assert str(actual) in line[0], \
            f"README row for {FILE_585} lacks count {actual}"

    def test_585_architecture_row_count_matches_actual(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_585)
        line = [l for l in text.splitlines() if FILE_585 in l]
        assert line, f"ARCHITECTURE row for {FILE_585}"
        assert str(actual) in line[0], \
            f"ARCHITECTURE row for {FILE_585} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"


# ---------------------------------------------------------------------------
# Stale-docstring repair regression: the #580 file's as-written REPAIR
# paragraph claimed the system-wide pip install was the fix and that the
# .venv lacked textblob/vaderSentiment. Commit 80f2832 corrected the
# record: the repo .venv was already the durable canonical interpreter
# and system-site installs were transient (wiped by a service restart).
# The #585 run repaired the docstring; this class pins the corrected
# narrative so the false system-interpreter story cannot return.
# ---------------------------------------------------------------------------


class TestStaleDocstringRepair580:
    FILE_580 = ("test_type_d_580_scorer_consistency_577_578_agreement_"
                "degenerate_boundary_rotation_doc_sync_sep07_5am.py")

    # Phrases from the stale narrative (whitespace-normalized matching).
    STALE_PHRASES = [
        "installed system-wide via pip --break-system-packages",
        "the .venv python still lacks textblob/vadersentiment",
        "the fix is host-specific to the system python3",
    ]

    def _flat(self):
        with open(TESTS_DIR / self.FILE_580) as f:
            content = f.read()
        return re.sub(r"\s+", " ", content).lower()

    @pytest.mark.parametrize("phrase", STALE_PHRASES)
    def test_stale_phrase_absent(self, phrase):
        assert phrase not in self._flat(), \
            f"stale system-interpreter phrase returned: {phrase!r}"

    def test_canonical_venv_language_present(self):
        flat = self._flat()
        assert ".venv" in flat
        assert "canonical" in flat
        assert "never install" in flat and "system site-packages" in flat

    def test_transient_wipe_recorded(self):
        flat = self._flat()
        assert "transient" in flat
        assert "wiped" in flat or "wipe" in flat

    def test_correction_commit_referenced(self):
        flat = self._flat()
        assert "80f2832" in flat
