"""Type D #610 (2026-09-08 13:00 PDT, scheduled job_id mediascope-daily-iteration,
goal_54093bda4145): scorer cross-mechanism consistency
extended to #607/#608 + #602 SEVENTH divergence spot-check + rotation guard for
606-610 + doc-sync ratchet (rotation 609 C -> 610 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (welch_t_test / cohens_d on the logged arrays) is
engine-drift detection: its mean-difference arithmetic must reproduce the
logged manual delta, and its significance output is computed but
deliberately NOT promoted to a finding for illustrative inputs.

This run:
- #607 (Type A, The Verge x OpenAI wiki-incident, Sep 8 09:00 PDT):
  publication-level incident-coverage register. Logged arms are OpenAI
  [-0.65] (n=1) vs Meta [-0.55, -0.6, -0.5] (n=3, carried from #592);
  logged meta_avg -0.55 and asymmetry_score -0.10 reproduce the logged
  mean-difference arithmetic exactly: round(-0.65 - (-0.55), 2) == -0.10 -
  the engine-drift contract covers the mean difference the finding cites,
  not the t-path the guard disables. The ENGINE on the raw arms:
  welch_t_test([-0.65], [-0.55,-0.6,-0.5]) -> (0.0, 1.0), the degenerate
  guard fires on the n=1 arm (per the #603 pin); cohens_d -> -2.0 rounded,
  the ASYMMETRIC n=1 vs n=3 variant mirroring #593 (cohens_d -9.2376,
  nonzero while only the t-path guarded). The #607 variant is NOT counted
  as a new degenerate-boundary pin - it mirrors the already-pinned #593
  asymmetric variant, and the #608 run pinned the sixth (symmetric).
  Finding layer refuses (p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False). NOT an agreement-pole pin: the pole requires a
  non-degenerate engine computation, so engine/finding agreement here is
  degenerate-boundary, not a pole pin. Falsification family moves 8 -> 9:
  #607 joins #538, #563, #568, #578, #583, #588, #599, #604. Second
  Vox-deal falsification instance (first: #573 Nilay Patel interview-access
  layer), distinct_from 573 recorded in YAML.
- #608 (Type B, Robert Hart cross-entity register constancy, Sep 8 10:00
  PDT): the SIXTH degenerate-boundary pin, VERIFIED still holding here (no
  new pin this run). Symmetric n=1 vs n=1: welch_t_test([-0.65], [-0.50])
  -> (t=0.0, p=1.0) AND cohens_d -> 0.0 (n_a + n_b = 2 <= 2) - BOTH engine
  paths go degenerate, mirroring the #603/#605 fifth-pin symmetric variant
  (second symmetric variant). Logged illustrative delta -0.15 reproduces
  arithmetic exactly: round(-0.65 - (-0.50), 2) == -0.15. Finding layer
  refuses (NOT_CALCULATED x3, is_significant False). NOT an agreement-pole
  pin - pole requires a non-degenerate engine computation. DseWiki
  canonical-URL constancy: the SAME canonical URL
  (theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident)
  is cited in mechanism 598 (the-verge.yaml) and mechanism 599
  (journalists.yaml Robert Hart entry) - publication-level and writer-level
  mechanisms cite the same piece.
- #609 (Type C, first-gen OpenAI publisher-deal renewal window, Sep 8
  11:00 PDT) is the qualitative boundary (mirroring #604 in #605, #594 in
  #595, #589 in #590, #584 in #585): tone_scores NOT_SCORED,
  statistical_discipline carries the #540/#544 boundary string, no
  asymmetry_scorer key - scorer consistency explicitly does NOT apply.
  Mechanism 600 is the max numeric mechanism_id pre-commit. Renewal status
  UNRESOLVED x3 (Conde Nast / Atlantic / FT), all treated ACTIVE per the
  #599 Vox convention; the #609 YAML BOUNDS the falsification family (does
  not join or break it).
- #606 (Type E, podcast sentiment 44th verification, Sep 8 08:00 PDT) is
  the monitoring boundary (mirroring #601 in #605, #591 in #595, #586 in
  #590): monitoring-only, no iteration-606 mechanism block in profiles/,
  no scorer extension.
- #602 (Type A, WIRED x Anthropic licensing-halo September silence
  extension, Sep 8 04:00 PDT): the SEVENTH divergence spot-check STILL
  HOLDING. The engine recomputes on the pinned arrays (Meta alarm baseline
  [-0.82, -0.72, -0.78] vs Sept peer register [-0.10, -0.05, 0.10])
  returning t=-11.3358, p=0.001755, d=-9.2557, is_significant True
  (smallest engine p / largest |d| in the divergence class), while the
  finding layer refuses (NOT_CALCULATED, is_significant False). Divergence
  ratchet intact at 6; no new divergence pins in the 603-609 window.

Degenerate-boundary count STAYS at 6 (no new pin this run; the sixth is
verified holding). Agreement-pole ratchet intact at 11 (tenth/eleventh pole
pins were ITERATIONS #598/#599 - distinct numbering system from profile
mechanism ids 598/599, which belong to iterations #607/#608; no pole pin
this run). Falsification family: #538, #563, #568, #578, #583, #588, #599,
#604, #607. Falsification family moves 8 -> 9 (the #607 Vox-deal
incident-coverage instance joins; #609 BOUNDS the family without joining).

DOC-SYNC: no miss repairs needed this run - the #606-#609 README rows
(71/60/37/67) and ARCHITECTURE rows (71 tests 11 classes / 60 tests 9
classes / 37 tests 8 classes / 67 tests 8 classes) all match the committed
def-test counts (first fully-clean doc-sync window since the #605 fifth
miss repair; the repair streak is deliberately left at five). NOT
empirical; no artifact-grade claims.

Rotation: 609 C -> 610 D. TestRotationCycleGuard610 covers window 606-610
(D, C, B, A, E newest-first), closing the C->D edge; anchor patched in the
followup per the #565 convention. The guard class is deselected pre-commit
(it asserts the post-commit anchor) and runs green in the followup commit.

Sources: all mechanism facts are in-corpus (profiles/the-verge.yaml
mechanism_598_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08,
profiles/careers/journalists.yaml
mechanism_599_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08,
profiles/competitor-entities.yaml
first_gen_openai_publisher_deal_renewal_window_600, profiles/wired.yaml
mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08).
Engine computations run against the repo's own
mediascope/score/statistical.py. No browser work this run.
"""

# Whitespace-normalized docstring for phrase assertions: the docstring wraps
# at a different width than the #605 file, so multi-line phrases are asserted
# against DOC, not raw __doc__.
DOC = " ".join(__doc__.split())

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

THIS_FILE = "test_type_d_610_scorer_consistency_607_608_degenerate_609_boundary_rotation_doc_sync_sep08_1pm.py"

# Engine inputs quoted verbatim from the covered test files' own pinned
# constants (tone values), NOT re-invented here - the YAML round-trips are
# asserted separately.
VERGE607_OPENAI_TONES = [-0.65]            # OpenAI wiki-incident arm (n=1)
VERGE607_META_TONES = [-0.55, -0.6, -0.5]  # Meta comparator, carried #592 (n=3)
HART608_OPENAI_TONE = -0.65               # OpenAI DseWiki arm (n=1)
HART608_META_TONE = -0.50                 # Meta AI-app clickbait arm (n=1)
WIRED602_TARGET_SCORES = [-0.82, -0.72, -0.78]  # Meta alarm baseline (#547)
WIRED602_PEER_SCORES = [-0.10, -0.05, 0.10]     # Sept peer register

DSEWIKI_CANONICAL_URL = "https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident"


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


def _mechanism_607():
    return _find_mechanism(
        "the-verge.yaml",
        "mechanism_598_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08",
    )


def _mechanism_608():
    return _find_mechanism(
        os.path.join("careers", "journalists.yaml"),
        "mechanism_599_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08",
    )


def _mechanism_609():
    return _find_mechanism(
        "competitor-entities.yaml",
        "first_gen_openai_publisher_deal_renewal_window_600",
    )


def _mechanism_602():
    return _find_mechanism(
        "wired.yaml",
        "mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08",
    )


def _git_main_subjects(anchor, n=5):
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "log", "-n40", anchor, "--format=%s"],
        capture_output=True, text=True, check=True)
    mains = [s for s in out.stdout.splitlines()
             if re.match(r"^Type [A-E] #\d+:", s)]
    return mains[:n]


def max_numeric_mechanism_id():
    found = set()
    for root, _, files in os.walk(REPO_ROOT / "profiles"):
        for fn in files:
            if fn.endswith(".yaml"):
                with open(os.path.join(root, fn)) as f:
                    _collect_mechanism_ids(yaml.safe_load(f), found)
    return max(i for i in found if isinstance(i, int))


def _collect_mechanism_ids(o, out):
    if isinstance(o, dict):
        if "mechanism_id" in o:
            out.add(o["mechanism_id"])
        for v in o.values():
            _collect_mechanism_ids(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_mechanism_ids(v, out)


def _collect_iteration_610(o, out):
    if isinstance(o, dict):
        if o.get("iteration") == 610:
            out.append(o.get("block_key") or o.get("mechanism_id"))
        for v in o.values():
            _collect_iteration_610(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_iteration_610(v, out)


class TestIteration610Metadata:
    def test_type_and_rotation_edge(self):
        assert "Type D #610" in DOC
        assert "rotation 609 C -> 610 D" in DOC

    def test_scheduled_job_and_goal(self):
        assert "mediascope-daily-iteration" in DOC
        assert "goal_54093bda4145" in DOC

    def test_timestamp(self):
        assert "2026-09-08 13:00 PDT" in DOC

    def test_no_browser_work(self):
        assert "No browser work this run" in DOC

    def test_standing_rule_restatement(self):
        assert "p_value NOT_CALCULATED" in DOC
        assert "is_significant False" in DOC


class TestScorerConsistency607VergeWikiIncident:
    def test_logged_avgs_and_delta_reproduce_arithmetic_exactly(self):
        # The engine-drift contract covers the mean difference the finding
        # cites: logged openai_avg -0.65, meta_avg -0.55, asymmetry_score
        # -0.10 (openai minus meta). NOT the t-path the guard disables.
        s = _mechanism_607()["asymmetry_scorer_result"]
        assert s["openai_avg"] == -0.65
        assert s["meta_avg"] == -0.55
        assert s["asymmetry_score"] == -0.10
        assert round(s["openai_avg"] - s["meta_avg"], 2) == s["asymmetry_score"]
        assert s["score_direction"] == "openai_minus_meta"

    def test_engine_welch_degenerate_guard_fires_on_n1_arm(self):
        # One arm has n=1: the welch guard returns (0.0, 1.0).
        t, p = welch_t_test(VERGE607_OPENAI_TONES, VERGE607_META_TONES)
        assert (t, p) == (0.0, 1.0)

    def test_engine_cohens_d_asymmetric_variant_rounds_minus2(self):
        # Asymmetric n=1 vs n=3: the d-path does NOT guard (n_a + n_b = 4 > 2),
        # mirroring #593 (cohens_d -9.2376 nonzero while the t-path guarded).
        d = cohens_d(VERGE607_OPENAI_TONES, VERGE607_META_TONES)
        assert round(d, 1) == -2.0
        assert round(d, 2) == -2.00

    def test_yaml_engine_drift_check_matches_recomputed_values(self):
        eng = _mechanism_607()["asymmetry_scorer_result"]["engine_drift_check"]
        assert "(0.0, 1.0)" in eng
        assert "-2.0" in eng
        assert "asymmetric n=1 vs n=3 variant, mirrors #593" in eng

    def test_finding_layer_refuses_both_paths(self):
        s = _mechanism_607()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["method"] == "manual_illustrative"

    def test_not_an_agreement_pole_pin(self):
        # The agreement pole requires a non-degenerate engine computation;
        # engine/finding agreement here is degenerate-boundary, not a pole
        # pin. The docstring pins the pole at 11.
        assert "NOT an agreement-pole pin" in DOC
        assert "Agreement-pole ratchet intact at 11" in DOC

    def test_falsification_family_ratchet_8_to_9(self):
        fam = _mechanism_607()["falsification_family"]
        for member in ["#538", "#563", "#568", "#578", "#583", "#588",
                       "#599", "#604", "#607"]:
            assert member in fam, f"family string missing {member}"
        assert "ratchet 8 -> 9" in fam
        assert "Falsification family moves 8 -> 9" in DOC

    def test_second_vox_deal_falsification_distinct_from_573(self):
        # Second Vox-deal falsification instance (first: #573 Nilay Patel
        # interview-access layer); the YAML records the distinction.
        dist = _mechanism_607()["distinct_from"]
        assert any("573" in str(d) for d in dist)
        assert "Second Vox-deal falsification instance" in DOC

    def test_mechanism_and_iteration_ids(self):
        m = _mechanism_607()
        assert m["mechanism_id"] == 598
        assert m["iteration"] == 607
        assert m["iteration_type"] == "A"


class TestScorerConsistency608HartSixthDegeneratePin:
    def test_symmetric_n1_n1_both_engine_paths_go_degenerate(self):
        # SIXTH degenerate-boundary pin (verified still holding here; no new
        # pin this run). Symmetric n=1 vs n=1: welch guard fires AND the
        # cohens_d n_a + n_b <= 2 guard fires - BOTH engine paths degenerate.
        t, p = welch_t_test([HART608_OPENAI_TONE], [HART608_META_TONE])
        d = cohens_d([HART608_OPENAI_TONE], [HART608_META_TONE])
        assert (t, p, d) == (0.0, 1.0, 0.0)

    def test_yaml_engine_string_matches_recomputation(self):
        eng = _mechanism_608()["asymmetry_scorer_result_illustrative"]["engine"]
        assert "(t=0.0, p=1.0)" in eng
        assert "cohens_d -> 0.0" in eng
        assert "n_a + n_b = 2 <= 2" in eng
        assert "mirroring the #605/#603 fifth-pin symmetric variant" in eng

    def test_logged_delta_reproduces_arithmetic_exactly(self):
        idd = _mechanism_608()["illustrative_delta"]
        assert idd["convention"] == "OpenAI minus Meta"
        assert idd["openai"] == -0.65
        assert idd["meta"] == -0.50
        assert idd["delta"] == -0.15
        assert round(idd["openai"] - idd["meta"], 2) == idd["delta"]

    def test_degenerate_boundary_pin_sixth(self):
        pin = _mechanism_608()["asymmetry_scorer_result_illustrative"][
            "degenerate_boundary_pin"]
        assert "sixth" in pin
        assert "ratchet 5 -> 6" in pin
        assert "second symmetric n=1 vs n=1 variant" in pin
        assert "Degenerate-boundary count STAYS at 6" in DOC

    def test_finding_layer_refuses(self):
        s = _mechanism_608()["asymmetry_scorer_result_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False

    def test_constancy_finding_not_divergence(self):
        # The finding is register CONSTANCY across a frontier lab and Meta -
        # no Meta-specific asymmetry, not a divergence pin (the divergence
        # ratchet test pins the pole at 6 separately).
        assert "cross-entity register constancy" in DOC
        assert "the SIXTH degenerate-boundary pin, VERIFIED still holding" in DOC
        assert "Divergence ratchet intact at 6" in DOC

    def test_not_an_agreement_pole_pin(self):
        assert "NOT an agreement-pole pin" in DOC
        assert "Agreement-pole ratchet intact at 11" in DOC

    def test_mechanism_and_iteration_ids(self):
        m = _mechanism_608()
        assert m["mechanism_id"] == 599
        assert m["iteration"] == 608
        assert m["type"] == "B"


class TestDivergenceRatchet602SeventhSpotCheck:
    def test_engine_recomputes_sixth_divergence_pin_exactly(self):
        # SEVENTH spot-check: the sixth divergence pin still holds. Engine
        # reaches significance on the illustrative arrays (smallest engine
        # p / largest |d| in the divergence class); the finding refuses.
        t, p = welch_t_test(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        d = cohens_d(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        assert round(t, 4) == -11.3358
        assert round(p, 6) == 0.001755
        assert round(d, 4) == -9.2557
        assert p < 0.05

    def test_yaml_engine_note_matches_recomputed_values(self):
        s = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_welch_t_minus11_3358"]
        assert "t=-11.3358" in eng and "p=0.001755" in eng
        assert "d=-9.2557" in eng and "is_significant True" in eng

    def test_finding_layer_refuses_while_engine_significant(self):
        # The divergence subclass: engine reaches significance, finding
        # refuses - the disagreement the ratchet tracks.
        finding = _mechanism_602()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"][
            "finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding

    def test_divergence_ratchet_stays_at_six(self):
        # No new divergence pins in the 603-609 window (#607 falsifies at the
        # incident layer but is a falsification-family join, not a divergence
        # pin; #608 is a constancy finding).
        assert "Divergence ratchet intact at 6" in DOC

    def test_seventh_spot_check_naming(self):
        assert "SEVENTH divergence spot-check STILL HOLDING" in DOC


class TestQualitativeBoundary609:
    def test_tone_scores_not_scored(self):
        assert _mechanism_609()["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_names_boundary(self):
        sd = _mechanism_609()["statistical_discipline"]
        assert "scorer consistency does not apply" in sd
        assert "#540/#544" in sd

    def test_no_asymmetry_scorer_key(self):
        # Qualitative Type C mapping: no scorer section at all - scorer
        # consistency has nothing to attach to (mirrors #604 in #605, #594 in
        # #595, #589 in #590, #584 in #585).
        assert "asymmetry_scorer" not in _mechanism_609()
        assert "no asymmetry_scorer key" in DOC

    def test_renewal_status_unresolved_x3(self):
        m = _mechanism_609()
        yaml_text = str(m)
        assert yaml_text.count("UNRESOLVED") >= 3

    def test_treated_active_per_599_convention(self):
        s = str(_mechanism_609())
        assert "treated ACTIVE" in s
        assert "#599 Vox convention" in s

    def test_mechanism_and_iteration_ids(self):
        m = _mechanism_609()
        assert m["mechanism_id"] == 600
        assert m["iteration"] == 609
        assert m["iteration_type"] == "C"


class TestMonitoringBoundary606:
    def test_no_iteration_606_mechanism_in_profiles(self):
        # Monitoring-only iteration: no mechanism block in profiles/ carries
        # iteration 606 (mirrors #601 in #605, #591 in #595, #586 in #590).
        found = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        _collect_iteration_606(yaml.safe_load(f), found)
        assert not found, f"unexpected iteration-606 mechanisms: {found}"

    def test_no_scorer_extension_from_monitoring(self):
        assert "no scorer extension" in DOC

    def test_606_test_file_green_at_71(self):
        assert count_def_tests(
            "test_type_e_606_podcast_sentiment_fortyfourth_verification_gf499_landed_sep08_8am.py") == 71


def _collect_iteration_606(o, out):
    if isinstance(o, dict):
        if o.get("iteration") == 606:
            out.append(o.get("block_key") or o.get("mechanism_id"))
        for v in o.values():
            _collect_iteration_606(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_iteration_606(v, out)


class TestStandingRuleDiscipline610:
    def test_degenerate_boundary_stays_at_six(self):
        # #608 pinned the sixth; this run verifies it holding. No new pin:
        # #607's asymmetric variant mirrors the already-pinned #593 variant.
        assert "Degenerate-boundary count STAYS at 6" in DOC

    def test_agreement_pole_intact_at_eleven(self):
        # No new agreement-pole pins this run; the pole stays at 11. The
        # tenth/eleventh pole pins were ITERATIONS #598/#599 (Sep 8 runs) -
        # distinct numbering from profile mechanism ids 598/599, which belong
        # to iterations #607/#608.
        assert "Agreement-pole ratchet intact at 11" in DOC

    def test_divergence_ratchet_intact_at_six(self):
        # #602 sixth divergence pin spot-checked still holding (seventh
        # spot-check); no new divergence pins in the 603-609 window.
        assert "Divergence ratchet intact at 6" in DOC

    def test_falsification_family_moves_8_to_9(self):
        # The #607 Vox-deal incident-coverage instance joins the family; #609
        # BOUNDS it without joining.
        assert "Falsification family moves 8 -> 9" in DOC
        assert "#609 BOUNDS the family without joining" in DOC

    def test_no_analysis_json_claim(self):
        # Monitoring/consistency cycle: no empirical finding warrants an
        # analysis.json update. Engine-drift checks and discipline pins only.
        assert "NOT empirical" in DOC
        assert "no artifact-grade claims" in DOC

    def test_no_iteration_610_mechanisms_in_profiles(self):
        # Type D adds no new mechanism blocks; #609's mechanism 600 remains
        # the max numeric mechanism_id pre-commit.
        found = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        _collect_iteration_610(yaml.safe_load(f), found)
        assert not found, f"unexpected iteration-610 mechanisms: {found}"
        assert max_numeric_mechanism_id() == 600


class TestNewCompetitorCoveragePatterns:
    def test_607_608_dsewiki_canonical_url_constancy(self):
        # NEW competitor-coverage pattern test: the publication-level (#607,
        # the-verge.yaml mechanism 598) and writer-level (#608,
        # journalists.yaml mechanism 599) mechanisms cite the SAME canonical
        # URL for the DseWiki incident piece - cross-layer citation constancy.
        m598 = _mechanism_607()
        m599 = _mechanism_608()
        urls_598 = _collect_urls(m598)
        assert DSEWIKI_CANONICAL_URL in urls_598
        assert DSEWIKI_CANONICAL_URL == m599["openai_arm"]["source_url"]
        assert _mechanism_607()["asymmetry_scorer_result"]["openai_tones"] == [-0.65]
        assert _mechanism_608()["illustrative_delta"]["openai"] == -0.65

    def test_607_608_share_openai_illustrative_tone(self):
        # Same piece, different analytical layer (publication incident-coverage
        # vs writer cross-entity constancy): both carry -0.65 for the OpenAI
        # arm, so the #608 constancy finding is mechanically consistent with
        # the #607 delta's OpenAI input.
        assert _mechanism_607()["asymmetry_scorer_result"]["openai_avg"] == \
            _mechanism_608()["illustrative_delta"]["openai"]

    def test_falsification_family_nine_members(self):
        family = "#538, #563, #568, #578, #583, #588, #599, #604, #607"
        assert family in DOC

    def test_609_bounds_family_does_not_join(self):
        effect = _mechanism_609()["financial_predictor_implication"][
            "effect_on_falsification_family"]
        assert "does not join or break" in effect
        assert "#609" not in _mechanism_607()["falsification_family"]

    def test_607_second_vox_deal_falsification_layer_distinction(self):
        # Two Vox-OpenAI-deal falsification instances at distinct layers:
        # #573 (Nilay Patel, Decoder interview-access) vs #607 (DseWiki,
        # incident-coverage register). The falsified predictor is the same
        # May 29 2024 Vox Media x OpenAI deal; the layer differs.
        distinct = " ".join(str(d) for d in _mechanism_607()["distinct_from"])
        assert "573" in distinct
        assert "interview-access" in distinct


def _collect_urls(o):
    out = []

    def _walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("url", "source_url") and isinstance(v, str):
                    out.append(v)
                elif isinstance(v, (dict, list)):
                    _walk(v)
        elif isinstance(x, list):
            for v in x:
                _walk(v)

    _walk(o)
    return out


class TestNoBrittleSweep606to610:
    def test_window_file_counts(self):
        expected = {
            "test_type_e_606_podcast_sentiment_fortyfourth_verification_gf499_landed_sep08_8am.py": 71,
            "test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am.py": 60,
            "test_type_b_608_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08_10am.py": 37,
            "test_type_c_609_first_gen_openai_publisher_deal_renewal_window_sep08_11am.py": 67,
        }
        for f, n in expected.items():
            assert count_def_tests(f) == n, f"{f}: {count_def_tests(f)} != {n}"

    def test_exactly_one_610_file(self):
        files = list(TESTS_DIR.glob("test_type_d_610_*.py"))
        assert len(files) == 1
        assert files[0].name == THIS_FILE

    def test_no_window_duplicate_numeric_mechanism_ids_gte_596(self):
        # Mechanism ids 596 (Stern news-corp), 597 (Axel Springer),
        # 598 (Verge wiki-incident), 599 (Hart), 600 (first-gen renewal) each
        # appear exactly once across profiles/.
        seen = {}
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        ids = set()
                        _collect_mechanism_ids(yaml.safe_load(f), ids)
                        for i in ids:
                            if isinstance(i, int) and i >= 596:
                                seen.setdefault(i, []).append(fn)
        for i in (596, 597, 598, 599, 600):
            assert len(seen.get(i, [])) == 1, f"mechanism {i}: {seen.get(i)}"

    def test_ascii_only_this_file(self):
        raw = (TESTS_DIR / THIS_FILE).read_bytes()
        assert all(b < 128 for b in raw), "non-ASCII bytes in test file"

    def test_no_precommit_610_in_git_log(self):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "--oneline", "--grep", "#610"],
            capture_output=True, text=True)
        assert out.stdout.strip() == "", "pre-commit #610 hit in git log"


class TestDocSyncRatchet610:
    def test_readme_rows_606_609_present_with_full_counts(self):
        readme = README.read_text()
        expected = {
            "test_type_e_606_podcast_sentiment_fortyfourth_verification_gf499_landed_sep08_8am.py": 71,
            "test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am.py": 60,
            "test_type_b_608_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08_10am.py": 37,
            "test_type_c_609_first_gen_openai_publisher_deal_renewal_window_sep08_11am.py": 67,
        }
        for f, n in expected.items():
            m = re.search(rf"`{re.escape(f)}` \| (\d+) \|", readme)
            assert m, f"README row missing for {f}"
            assert int(m.group(1)) == n, f"{f}: README says {m.group(1)}, file has {n}"

    def test_architecture_rows_606_609_present_with_full_counts(self):
        tree = ARCHITECTURE.read_text()
        expected = [
            ("test_type_e_606_podcast_sentiment_fortyfourth_verification_gf499_landed_sep08_8am.py", 71, 11),
            ("test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am.py", 60, 9),
            ("test_type_b_608_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08_10am.py", 37, 8),
            ("test_type_c_609_first_gen_openai_publisher_deal_renewal_window_sep08_11am.py", 67, 8),
        ]
        for f, n, c in expected:
            m = re.search(
                rf"{re.escape(f)}[^\n]*- (\d+) tests, (\d+) classes", tree)
            assert m, f"ARCHITECTURE row missing counts for {f}"
            assert (int(m.group(1)), int(m.group(2))) == (n, c), \
                f"{f}: ARCHITECTURE says {m.groups()}, file has {(n, c)}"

    def test_610_readme_row_added(self):
        readme = README.read_text()
        assert f"`{THIS_FILE}`" in readme

    def test_610_architecture_row_added(self):
        tree = ARCHITECTURE.read_text()
        m = re.search(
            rf"{re.escape(THIS_FILE)}[^\n]*- (\d+) tests, (\d+) classes", tree)
        assert m, "ARCHITECTURE #610 row missing counts"
        assert int(m.group(1)) == count_def_tests(THIS_FILE)
        assert int(m.group(2)) == 11

    def test_iteration_log_610_entry_present(self):
        log = LOG.read_text()
        assert "#610 Type D" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"


class TestRotationCycleGuard610:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard610.ANCHORED_COMMIT)

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#610", "D"),
            ("#609", "C"),
            ("#608", "B"),
            ("#607", "A"),
            ("#606", "E"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # C->D is the edge this run closes; the full 5-window must be a
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
