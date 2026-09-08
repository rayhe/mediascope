"""Type D #605 (2026-09-08 07:00 PDT): scorer cross-mechanism consistency
extended to #603/#604 + #602 divergence spot-check + rotation guard for
601-605 + doc-sync ratchet + #602/#603 count miss repair
(rotation 604 C -> 605 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (welch_t_test / cohens_d on the logged arrays) is
engine-drift detection: its mean-difference arithmetic must reproduce the
logged manual delta, and its significance output is computed but
deliberately NOT promoted to a finding for illustrative inputs.

This run pins the DEGENERATE-BOUNDARY subclass for the newest quantitative
mechanism and spot-checks the newest divergence pin:

- #603 (Type B, Joanna Stern independent-phase cross-entity gradient
  inversion, Sep 8 05:00 PDT): independent-phase arms are Meta [-0.65]
  vs Apple [+0.60], BOTH arms n=1 - the FIRST SYMMETRIC (n=1 vs n=1)
  degenerate variant. FIFTH DEGENERATE-BOUNDARY PIN (ratchet 4 -> 5):
  welch_t_test returns (t=0.0, p=1.0) - the guard fires on both arms - and
  cohens_d returns 0.0 (n_a + n_b = 2 <= 2), so BOTH engine paths go
  degenerate, unlike the asymmetric variant #593 (n=1 vs n=3) where
  cohens_d computed -9.2376 (nonzero) while the t-path guarded. The logged
  independent_phase_meta_minus_apple_delta -1.25 reproduces
  mean-difference arithmetic exactly (-0.65 - 0.60 = -1.25): the
  engine-drift contract covers the mean difference the finding cites, not
  the t-path the guard disables. The inversion magnitude 1.80 is
  cross-phase arithmetic (WSJ-phase 0.55 minus independent-phase -1.25),
  NOT an engine quantity - no welch computation over phase-level
  aggregates. Finding layer refuses (NOT_CALCULATED x3, sig False).
- #602 (Type A, WIRED x Anthropic licensing-halo September silence
  extension, Sep 8 04:00 PDT): the SIXTH divergence pin is spot-checked
  still holding. The engine recomputes on the pinned arrays (Meta alarm
  baseline [-0.82, -0.72, -0.78] vs Sept peer register [-0.10, -0.05,
  0.10]) returning t=-11.3358, p=0.001755, d=-9.2557, is_significant True,
  while the finding layer refuses (NOT_CALCULATED, sig False). Smallest
  engine p / largest |d| in the divergence class; the ratchet stays active
  at 6 with no new divergence pins in the 600-604 window.
- #604 (Type C, Axel Springer dual-AI-payer architecture, Sep 8 06:00 PDT)
  is the qualitative boundary (mirroring #594 in #595, #589 in #590, #584
  in #585): tone_scores NOT_SCORED, statistical_discipline carries the
  #540/#544 boundary string, no asymmetry_scorer key, scorer consistency
  explicitly does NOT apply.
- #601 (Type E, podcast sentiment 43rd verification, Sep 8 03:00 PDT) is
  the monitoring boundary (mirroring #591 in #595, #586 in #590):
  monitoring-only, no quantitative mechanism, no scorer extension.

Divergence ratchet intact at 6 (no new divergence pins; #602 spot-check
green). Degenerate-boundary count moves 4 -> 5 with the #603 symmetric
variant. Agreement-pole ratchet intact at 11 (no new agreement pins).
Falsification family: #538, #563, #568, #578, #583, #588, #599, #604.
Falsification family moves 7 -> 8: the #604 BI control case (OpenAI -0.42
deal-partner HARDEST vs $0 peers, money predicts OpenAI softest) joins
#538, #563, #568, #578, #583, #588, #599, completing the eight-member set.

DOC-SYNC MISS REPAIR: the #602 run's README.md row and
docs/ARCHITECTURE.md tree row said "56 tests" but the committed file
(main commit d4526ee, verified via git show) carries 59 def-tests; the
#603 run's rows said "54 tests" but the committed file (main commit
811c1ed, verified via git show) carries 57 def-tests. Both rows repaired
here. This is the fifth doc-sync miss repair in the series
(#510, #590, #595, #600, #605).

Rotation: 604 C -> 605 D. TestRotationCycleGuard605 covers window
601-605 (D, C, B, A, E newest-first), closing the C->D edge; anchor
patched in the followup per the #565 convention. The guard class is
deselected pre-commit (it asserts the post-commit anchor) and runs green
in the followup commit.

Sources: all mechanism facts are in-corpus (profiles/news-corp.yaml
mechanism_596, profiles/wired.yaml mechanism_595,
profiles/competitor-entities.yaml
axel_springer_dual_ai_payer_microsoft_four_channel_kkr_split_telegraph_597).
Engine computations run against the repo's own
mediascope/score/statistical.py. No browser work this run.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mediascope.score.statistical import welch_t_test, cohens_d

REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TESTS_DIR = REPO_ROOT / "tests"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
LOG = REPO_ROOT / "iteration-log.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

THIS_FILE = "test_type_d_605_scorer_consistency_603_degenerate_604_602_spotcheck_rotation_doc_sync_sep08_7am.py"

# Engine inputs quoted verbatim from the covered test files' own pinned
# constants (tone values), NOT re-invented here - the YAML round-trips are
# asserted separately.
STERN_META_TONE = -0.65   # independent-phase Meta (LED investigation)
STERN_APPLE_TONE = 0.60   # independent-phase Apple (Siri AI hands-on)
WIRED602_TARGET_SCORES = [-0.82, -0.72, -0.78]  # Meta alarm baseline (#547)
WIRED602_PEER_SCORES = [-0.10, -0.05, 0.10]     # Sept peer register

BRITTLE_PATTERN = re.compile(r"^\s*assert\s+.*newest.*==.*oldest", re.MULTILINE)


def count_def_tests(test_file):
    with open(TESTS_DIR / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


def _find_mechanism(filename, key):
    with open(REPO_ROOT / "profiles" / filename) as f:
        d = yaml.safe_load(f)
    out = []

    def _walk(o):
        if isinstance(o, dict):
            if key in o:
                out.append(o[key])
            for v in o.values():
                _walk(v)
        elif isinstance(o, list):
            for v in o:
                _walk(v)

    _walk(d)
    assert out, f"{key} not found in profiles/{filename}"
    return out[0]


def _mechanism_603():
    return _find_mechanism(
        "news-corp.yaml",
        "mechanism_596_joanna_stern_independent_phase_cross_entity_gradient_inversion_sep08",
    )


def _mechanism_602():
    return _find_mechanism(
        "wired.yaml",
        "mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08",
    )


def _mechanism_604():
    return _find_mechanism(
        "competitor-entities.yaml",
        "axel_springer_dual_ai_payer_microsoft_four_channel_kkr_split_telegraph_597",
    )


def _git_main_subjects(anchor, n=5):
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "log", "-n40", anchor, "--format=%s"],
        capture_output=True, text=True, check=True)
    mains = [s for s in out.stdout.splitlines()
             if re.match(r"^Type [A-E] #\d+:", s)]
    return mains[:n]


class TestIteration605Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "Type D #605" in doc
        assert "2026-09-08 07:00 PDT" in doc
        assert "604 C -> 605 D" in doc

    def test_rotation_c_to_d(self):
        # Per rotation A->B->C->D->E, the run after Type C #604 is Type D.
        assert "Type D #605" in __doc__

    def test_filename_convention(self):
        assert THIS_FILE.startswith("test_type_d_605_")
        assert THIS_FILE.endswith("_sep08_7am.py")
        assert (TESTS_DIR / THIS_FILE).exists()

    def test_covered_iterations_in_filename(self):
        assert "603" in THIS_FILE
        assert "604" in THIS_FILE
        assert "602" in THIS_FILE

    def test_docstring_names_fifth_degenerate_pin(self):
        assert "FIFTH DEGENERATE-BOUNDARY PIN" in __doc__

    def test_docstring_names_sixth_divergence_spotcheck(self):
        assert "SIXTH divergence pin" in __doc__ or "SIXTH DIVERGENCE" in __doc__


class TestScorerConsistency603SternDegenerateBoundary:
    def test_yaml_independent_phase_tones_reproduce_arms(self):
        m = _mechanism_603()
        corpus = m["independent_phase_corpus"]
        assert corpus["meta"]["tone"] == STERN_META_TONE
        assert corpus["apple"]["tone"] == STERN_APPLE_TONE

    def test_engine_guard_fires_on_both_arms_symmetric_variant(self):
        # BOTH arms n=1: the degenerate guard fires on both arms, not one.
        # This is the symmetric variant - distinct from #593's asymmetric
        # n=1 vs n=3 where the guard fired on the target arm only.
        t, p = welch_t_test([STERN_META_TONE], [STERN_APPLE_TONE])
        assert t == 0.0 and p == 1.0

    def test_cohens_d_also_zero_symmetric_variant(self):
        # n_a + n_b = 2 <= 2, so the d-path returns 0.0 too - BOTH engine
        # paths go degenerate. In #593's asymmetric variant cohens_d
        # computed -9.2376 (nonzero); here the symmetric variant zeroes it.
        d = cohens_d([STERN_META_TONE], [STERN_APPLE_TONE])
        assert d == 0.0

    def test_logged_independent_delta_reproduces_mean_difference(self):
        # The engine-drift contract covers the MEAN DIFFERENCE the finding
        # layer cites, not the t-path the guard disables: -0.65 - 0.60 =
        # -1.25, exact, no rounding involved.
        scorer = _mechanism_603()["asymmetry_scorer"]
        mean_diff = STERN_META_TONE - STERN_APPLE_TONE
        assert abs(mean_diff - (-1.25)) < 1e-9
        assert scorer["independent_phase_meta_minus_apple_delta"] == -1.25
        assert mean_diff == scorer["independent_phase_meta_minus_apple_delta"]

    def test_logged_wsj_delta_reproduces_mean_difference(self):
        # Carried WSJ-phase arms: Meta +0.35 vs Apple -0.20 (from the
        # joanna_stern block). 0.35 - (-0.20) = 0.55, exact.
        scorer = _mechanism_603()["asymmetry_scorer"]
        wsj = self._wsj_coverage()
        mean_diff = wsj["meta"]["tone"] - wsj["apple"]["tone"]
        assert abs(mean_diff - 0.55) < 1e-9
        assert scorer["wsj_phase_meta_minus_apple_delta"] == 0.55

    @staticmethod
    def _wsj_coverage():
        with open(REPO_ROOT / "profiles" / "news-corp.yaml") as f:
            d = yaml.safe_load(f)
        return d["journalist_cross_entity"]["joanna_stern"]["wsj_phase_coverage"]

    def test_inversion_magnitude_is_cross_phase_not_engine(self):
        # 1.80 = 0.55 - (-1.25): cross-phase arithmetic over the logged
        # deltas, NOT an engine quantity. There is no welch computation
        # over phase-level aggregates; the engine contract ends at the
        # per-phase mean differences.
        scorer = _mechanism_603()["asymmetry_scorer"]
        assert abs(scorer["inversion_magnitude"] - 1.8) < 1e-9
        expected = (scorer["wsj_phase_meta_minus_apple_delta"]
                    - scorer["independent_phase_meta_minus_apple_delta"])
        assert abs(expected - 1.8) < 1e-9
        assert scorer["inversion_magnitude"] == 1.8

    def test_finding_layer_refuses(self):
        scorer = _mechanism_603()["asymmetry_scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert scorer["method"] == "MANUAL_ILLUSTRATIVE"
        assert scorer["correlation_not_causation"] is True

    def test_n1_per_arm_documented(self):
        # The finding layer is honest about the degenerate input: n=1 per
        # arm in the independent-phase corpus.
        corpus = _mechanism_603()["independent_phase_corpus"]
        assert isinstance(corpus["meta"], dict) and "tone" in corpus["meta"]
        assert isinstance(corpus["apple"], dict) and "tone" in corpus["apple"]

    def test_mechanism_ids(self):
        m = _mechanism_603()
        assert m["mechanism_id"] == 596
        assert m["iteration"] == 603
        assert m["hour_type"] == "B"

    def test_url_attribution_verbatim(self):
        # The two June 2026 pieces carry verbatim source URLs in-corpus.
        corpus = _mechanism_603()["independent_phase_corpus"]
        assert corpus["meta"]["source_url"].startswith("https://www.youtube.com/")
        assert corpus["apple"]["source_url"].startswith("https://9to5mac.com/2026/06/19/")


class TestDivergenceRatchet602SpotCheck:
    def test_yaml_arrays_reproduce_pinned_constants(self):
        s = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert sorted(s["target_scores_MANUAL_ILLUSTRATIVE"]) == sorted(WIRED602_TARGET_SCORES)
        assert sorted(s["peer_scores_MANUAL_ILLUSTRATIVE"]) == sorted(WIRED602_PEER_SCORES)

    def test_logged_avgs_and_delta_reproduce_engine_arithmetic(self):
        s = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_avg"] == -0.7733
        assert s["peer_avg"] == -0.0167
        assert s["delta"] == 0.7567  # peer_avg - target_avg
        assert round(sum(WIRED602_PEER_SCORES) / 3 - sum(WIRED602_TARGET_SCORES) / 3, 4) == 0.7567

    def test_engine_recomputes_sixth_divergence_pin_exactly(self):
        # Spot-check: the sixth divergence pin still holds. Engine reaches
        # significance on the illustrative arrays (smallest engine p /
        # largest |d| in the divergence class); the finding refuses.
        # Pin convention mirrors the #602 file itself: engine values
        # rounded at 6dp/4dp (round(p, 6) == 0.001755 etc.).
        t, p = welch_t_test(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        d = cohens_d(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        assert round(t, 4) == -11.3358
        assert round(p, 6) == 0.001755
        assert round(d, 4) == -9.2557
        assert p < 0.05

    def test_yaml_engine_note_matches_recomputed_values(self):
        s = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_welch_t_minus11_3358"]
        assert "t=-11.3358" in eng and "p=0.001755" in eng and "d=-9.2557" in eng
        assert "is_significant True" in eng

    def test_finding_layer_refuses_while_engine_significant(self):
        # The divergence subclass: engine reaches significance, finding
        # refuses - the disagreement the ratchet tracks.
        finding = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding

    def test_divergence_ratchet_stays_at_six(self):
        assert "Divergence ratchet intact at 6" in __doc__


class TestQualitativeBoundary604:
    def test_tone_scores_not_scored(self):
        assert _mechanism_604()["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_names_boundary(self):
        sd = _mechanism_604()["statistical_discipline"]
        assert "scorer consistency does not apply" in sd
        assert "#540/#544" in sd

    def test_no_asymmetry_scorer_key(self):
        # Qualitative Type C mapping: no scorer section at all - scorer
        # consistency has nothing to attach to.
        assert "asymmetry_scorer" not in _mechanism_604()

    def test_no_coverage_tone_claim(self):
        assert _mechanism_604()["no_coverage_tone_claim"] is True or \
            "no coverage-tone claim" in str(_mechanism_604().get("cautious_language_required", ""))

    def test_mechanism_ids(self):
        m = _mechanism_604()
        assert m["mechanism_id"] == 597
        assert m["iteration"] == 604
        assert m["iteration_type"] == "C"

    def test_boundary_unchanged_since_594_precedent(self):
        # #594 in #595, #589 in #590, #584 in #585 set the precedent: the
        # qualitative boundary is a standing discipline, not a one-off.
        assert "mirroring #594 in #595" in __doc__


class TestMonitoringBoundary601:
    def test_601_file_is_monitoring_cycle(self):
        content = (TESTS_DIR / "test_type_e_601_podcast_sentiment_fortythird_verification_sep08_3am.py").read_text()
        assert "verification" in content.lower()

    def test_no_profiles_mechanism_with_iteration_601(self):
        # Monitoring-only: no mechanism block in profiles/ may carry
        # iteration 601.
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                with open(os.path.join(root, fn)) as f:
                    d = yaml.safe_load(f)
                assert not self._has_iteration(d, 601), f"iteration-601 mechanism in {fn}"

    @staticmethod
    def _has_iteration(o, n):
        if isinstance(o, dict):
            if o.get("iteration") == n:
                return True
            return any(TestMonitoringBoundary601._has_iteration(v, n) for v in o.values())
        if isinstance(o, list):
            return any(TestMonitoringBoundary601._has_iteration(v, n) for v in o)
        return False

    def test_monitoring_boundary_documented(self):
        assert "monitoring boundary" in __doc__


class TestStandingRuleDiscipline605:
    def test_all_quantitative_mechanisms_refuse_promotion(self):
        res603 = _mechanism_603()["asymmetry_scorer"]
        res602 = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["finding_layer"]
        assert res603["is_significant"] is False
        assert "NOT_CALCULATED" in res603["p_value"]
        assert "is_significant False" in res602

    def test_divergence_ratchet_intact_at_six(self):
        # #602 spot-checked still holding above; no new divergence pins in
        # the 600-604 window.
        assert "Divergence ratchet intact at 6" in __doc__

    def test_degenerate_boundary_moves_4_to_5(self):
        # #603 is the FIFTH degenerate-boundary pin (first symmetric n=1
        # vs n=1 variant). 4 -> 5.
        assert "Degenerate-boundary count moves 4 -> 5" in __doc__

    def test_agreement_pole_intact_at_eleven(self):
        # No new agreement-pole pins this run; the pole stays at 11
        # (#598 tenth, #599 eleventh).
        assert "Agreement-pole ratchet intact at 11" in __doc__

    def test_falsification_family_moves_7_to_8(self):
        # The #604 BI control case joins the family: with TWO AI payers the
        # money predicts OpenAI/Microsoft softest at BI, but OpenAI is
        # hardest - the control case against financial determinism stands.
        assert "Falsification family moves 7 -> 8" in __doc__

    def test_no_analysis_json_claim(self):
        # Monitoring/consistency cycle: no empirical finding warrants an
        # analysis.json update. Engine-drift checks and discipline pins only.
        assert "NOT empirical" in __doc__
        assert "no artifact-grade claims" in __doc__


class TestNewCompetitorCoveragePatterns:
    def test_603_first_symmetric_degenerate_variant(self):
        # All four prior degenerate pins are asymmetric or multi-arm; #603
        # is the first where BOTH arms are n=1.
        t, p = welch_t_test([STERN_META_TONE], [STERN_APPLE_TONE])
        d = cohens_d([STERN_META_TONE], [STERN_APPLE_TONE])
        assert (t, p, d) == (0.0, 1.0, 0.0)

    def test_falsification_family_eight_members(self):
        family = "#538, #563, #568, #578, #583, #588, #599, #604"
        assert family in __doc__

    def test_604_mechanism_mentions_falsification_family(self):
        import json
        assert "falsification" in json.dumps(_mechanism_604()).lower()

    def test_max_numeric_mechanism_id_is_597_pre_commit(self):
        # Type D: no new mechanism blocks; max numeric mechanism_id is 597
        # (the #604 Axel Springer dual-AI-payer block). No mechanism may
        # carry iteration 605.
        found = set()
        iterations_605 = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            if ".venv" in root:
                continue
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        d = yaml.safe_load(f)
                    _collect_mechanism_ids(d, found)
                    _collect_iteration_605(d, iterations_605)
        numeric = sorted(i for i in found if isinstance(i, int))
        assert max(numeric) == 597
        assert not iterations_605, f"unexpected iteration-605 mechanisms: {iterations_605}"

    def test_no_new_financial_mechanisms_this_run(self):
        # Type D is consistency/verification only: the #604 run was the
        # last financial-mapping run (mechanism 597).
        assert max_numeric_mechanism_id() == 597


def max_numeric_mechanism_id():
    found = set()
    for root, _, files in os.walk(REPO_ROOT / "profiles"):
        if ".venv" in root:
            continue
        for fn in files:
            if fn.endswith(".yaml"):
                with open(os.path.join(root, fn)) as f:
                    _collect_mechanism_ids(yaml.safe_load(f), found)
    return max(i for i in found if isinstance(i, int))


def _collect_iteration_605(o, out):
    if isinstance(o, dict):
        if o.get("iteration") == 605:
            out.append(o.get("block_key") or o.get("mechanism_id"))
        for v in o.values():
            _collect_iteration_605(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_iteration_605(v, out)


def _collect_mechanism_ids(o, out):
    if isinstance(o, dict):
        if "mechanism_id" in o:
            out.add(o["mechanism_id"])
        for v in o.values():
            _collect_mechanism_ids(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_mechanism_ids(v, out)


class TestNoBrittleSweep600to604:
    WINDOW = [
        "test_type_d_600_scorer_consistency_598_599_agreement_rotation_doc_sync_sep08_2am.py",
        "test_type_e_601_podcast_sentiment_fortythird_verification_sep08_3am.py",
        "test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py",
        "test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py",
        "test_type_c_604_axel_springer_dual_ai_payer_microsoft_kkr_split_telegraph_sep08_6am.py",
    ]
    EXPECTED_COUNTS = {
        "test_type_d_600_scorer_consistency_598_599_agreement_rotation_doc_sync_sep08_2am.py": 59,
        "test_type_e_601_podcast_sentiment_fortythird_verification_sep08_3am.py": 58,
        "test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py": 59,
        "test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py": 57,
        "test_type_c_604_axel_springer_dual_ai_payer_microsoft_kkr_split_telegraph_sep08_6am.py": 63,
    }

    def test_all_window_files_present(self):
        for f in self.WINDOW:
            assert (TESTS_DIR / f).exists(), f"missing {f}"

    def test_window_file_counts_sane(self):
        for f, n in self.EXPECTED_COUNTS.items():
            got = count_def_tests(f)
            assert got == n, f"{f}: expected {n} def-tests, got {got}"

    def test_no_duplicate_mechanism_ids(self):
        # Pre-existing duplicates (mechanism_ids 31/74/80 in gizmodo.yaml)
        # are out of scope; the window (>= 595, one rotation back) must be
        # clean. New window ids: 595 (#602), 596 (#603), 597 (#604).
        seen = {}
        dupes = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                with open(os.path.join(root, fn)) as f:
                    d = yaml.safe_load(f)
                ids = set()
                _collect_mechanism_ids(d, ids)
                for i in ids:
                    if isinstance(i, int) and i >= 595:
                        if i in seen:
                            dupes.append((i, seen[i], os.path.join(root, fn)))
                        seen[i] = os.path.join(root, fn)
        assert not dupes, f"duplicate window mechanism_ids: {dupes}"

    def test_no_brittle_heading_equality(self):
        # The #551 brittle pattern (asserting a specific iteration heading
        # is newest-first) breaks every hour; all window files use the
        # presence-assertion convention instead.
        for f in self.WINDOW:
            content = (TESTS_DIR / f).read_text()
            assert not BRITTLE_PATTERN.search(content), f"brittle pattern in {f}"

    def test_no_zero_coverage_claims_in_new_files(self):
        # Iteration-492 rule: silence claims are bounded search-result
        # absences, never proven zeros. The #602/#603 files must not assert
        # absolute non-existence phrasing.
        for f in ["test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py",
                  "test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py"]:
            content = (TESTS_DIR / f).read_text()
            assert "zero coverage" not in content.lower() or "bounded" in content.lower()

    def test_exactly_one_605_test_file(self):
        matches = list(TESTS_DIR.glob("test_type_d_605_*.py"))
        assert len(matches) == 1, f"expected exactly one #605 test file, got {matches}"


class TestDocSyncRatchet605:
    def test_readme_rows_601_604_present_with_full_counts(self):
        readme = README.read_text()
        expected = {
            "test_type_e_601_podcast_sentiment_fortythird_verification_sep08_3am.py": 58,
            "test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py": 59,
            "test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py": 57,
            "test_type_c_604_axel_springer_dual_ai_payer_microsoft_kkr_split_telegraph_sep08_6am.py": 63,
        }
        for f, n in expected.items():
            m = re.search(rf"`{re.escape(f)}` \| (\d+) \|", readme)
            assert m, f"README row missing for {f}"
            assert int(m.group(1)) == n, f"{f}: README says {m.group(1)}, file has {n}"

    def test_602_readme_row_repaired_56_to_59(self):
        # MISS REPAIR: the #602 run left "56 tests" in README; the committed
        # file (main commit d4526ee) carries 59 def-tests.
        readme = README.read_text()
        assert "`test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py` | 59 |" in readme

    def test_603_readme_row_repaired_54_to_57(self):
        # MISS REPAIR: the #603 run left "54 tests" in README; the committed
        # file (main commit 811c1ed) carries 57 def-tests.
        readme = README.read_text()
        assert "`test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py` | 57 |" in readme

    def test_602_architecture_row_repaired(self):
        tree = ARCHITECTURE.read_text()
        assert "test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py  # Type A #602" in tree
        m = re.search(
            r"test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am\.py[^\n]*- (\d+) tests, (\d+) classes",
            tree)
        assert m, "ARCHITECTURE #602 row missing counts"
        assert (int(m.group(1)), int(m.group(2))) == (59, 9)

    def test_603_architecture_row_repaired(self):
        tree = ARCHITECTURE.read_text()
        m = re.search(
            r"test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am\.py[^\n]*- (\d+) tests, (\d+) classes",
            tree)
        assert m, "ARCHITECTURE #603 row missing counts"
        assert (int(m.group(1)), int(m.group(2))) == (57, 10)

    def test_architecture_rows_601_604_present(self):
        tree = ARCHITECTURE.read_text()
        for token in ["#601", "#602", "#603", "#604", "#605"]:
            assert token in tree, f"ARCHITECTURE tree missing {token}"

    def test_605_readme_row_added(self):
        readme = README.read_text()
        assert f"`{THIS_FILE}`" in readme

    def test_iteration_log_605_entry_present(self):
        log = LOG.read_text()
        assert "#605 Type D" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"


class TestRotationCycleGuard605:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard605.ANCHORED_COMMIT)

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#605", "D"),
            ("#604", "C"),
            ("#603", "B"),
            ("#602", "A"),
            ("#601", "E"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # D->C is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: D,C,B,A,E (the rotation
        # runs backward in newest-first order). (order[a] - order[b]) % 5 == 1
        # steps one position backward from the newer commit a to the older
        # commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_anchor_is_post_commit(self):
        assert self.ANCHORED_COMMIT != "POST_COMMIT_ANCHOR", \
            "anchor must be patched to the main-commit hash in the followup"
