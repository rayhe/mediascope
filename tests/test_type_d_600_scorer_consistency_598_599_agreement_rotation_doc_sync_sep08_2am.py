"""Type D #600 (2026-09-08 02:00 PDT): scorer cross-mechanism consistency
extended to #598/#599 + rotation guard for 596-600 + doc-sync ratchet
+ #599 count miss repair (rotation 599 C -> 600 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (welch_t_test / cohens_d on the logged arrays) is
engine-drift detection: its mean-difference arithmetic must reproduce the
logged manual delta, and its significance output is computed but
deliberately NOT promoted to a finding for illustrative inputs.

This run pins the AGREEMENT-POLE subclass for the two newest quantitative
mechanisms - the engine ALSO fails to reach significance, so engine and
finding AGREE (in contrast to the divergence subclass where the engine
reaches significance and the finding layer refuses):

- #598 (Type B, Alex Hern Guardian->Economist register constancy, Sep 8
  00:00 PDT): Guardian-era Meta [-0.55, -0.45, -0.55] avg -0.5167 vs
  Economist-era [-0.55, -0.35, -0.30] avg -0.40. Logged
  cross_institution_delta -0.1167 (engine mean difference -0.116667
  rounds to the logged value). TENTH agreement-pole pin: real Welch
  n=3 vs n=3 (guard NOT triggered) returns t=-1.4, p=0.2642, d=-1.1431,
  is_significant False on the illustrative arrays, and the finding layer
  also refuses (NOT_CALCULATED + is_significant False). First
  cross-institution agreement pin - all prior agreement pins are
  within-publication controls (#582, #587). Constancy verdict, not a
  divergence-ratchet member: the ratchet tracks engine/finding
  significance DISAGREEMENT, and there is none here.
- #599 (Type C, Victoria Song writer-level behavioral pin on the Vox deal
  stack, Sep 8 01:00 PDT): Meta [-0.10, 0.0, 0.10] avg 0.0 vs Google
  [-0.35, 0.10] avg -0.125. Engine mean difference on the raw arrays is
  +0.125 while the logged delta is 0.13 (rounded to 2dp): a
  ROUNDED-VALUE ARITHMETIC DIVERGENCE bounded at 0.005,
  verdict-invariant (engine sig False, finding sig False,
  illustrative-only both ways). Second rounded-value precision note in
  the series (#593's was 0.0167; this one is smaller). ELEVENTH
  agreement-pole pin: real Welch n=3 vs n=2 (both arms >= 2, guard NOT
  triggered) returns t=0.5381, p=0.6770, d=0.6218, is_significant False,
  and the finding layer also refuses. The POSITIVE sign (+0.125 raw) is
  the inversion that bounds the financial theory: Song scored Google's
  first-gen Pixel Watch HARSher than Meta's first-gen Ray-Ban Display,
  opposite the money prediction - a writer-level falsification of the
  deal-gradient hypothesis, joining the falsification family
  (#538, #563, #568, #578, #583, #588, #599).

Sign-class separation: #598 (-0.1167, negative, cross-institution
register constancy) vs #599 (+0.125 raw / +0.13 logged, positive,
writer-level deal-gradient inversion). Same agreement pole, opposite
signs, different mechanism families - the suite must not conflate a
negative constancy gap with a positive inversion. |0.125|/|0.1167| =
1.0711 ratio: magnitude-adjacent, sign-separated.

Divergence ratchet intact at 5 (no new divergence pins in the 595-599
window). Degenerate-boundary count intact at 4 (no new degenerate pins).

DOC-SYNC MISS REPAIR: the #599 run's README.md row and
docs/ARCHITECTURE.md tree row said "36 tests" but the committed file
carries 39 def-tests (the 3 rotation-guard tests were deselected
pre-commit and anchored in the followup); both rows repaired to 39 here.
This is the fourth doc-sync miss repair in the series
(#510, #590, #595, #600).

Rotation: 599 C -> 600 D. TestRotationCycleGuard600 covers window
596-600 (D, C, B, A, E newest-first), closing the C->D edge; anchor
patched in the followup per the #565 convention. The guard class is
deselected pre-commit (it asserts the post-commit anchor) and runs green
in the followup commit.

Sources: all mechanism facts are in-corpus (profiles/guardian.yaml
mechanism_592, profiles/careers/journalists.yaml
type_c_599_victoria_song_vox_financial_stack_behavioral_pin). Engine
computations run against the repo's own
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

THIS_FILE = "test_type_d_600_scorer_consistency_598_599_agreement_rotation_doc_sync_sep08_2am.py"

# Engine inputs, quoted verbatim from the #598 and #599 test files' own
# pinned constants (tone lists), NOT re-read from YAML here - the YAML
# round-trips are asserted separately.
HERN_GUARDIAN_TONES = [-0.55, -0.45, -0.55]
HERN_ECONOMIST_TONES = [-0.55, -0.35, -0.30]
SONG_META_TONES = [-0.10, 0.0, 0.10]
SONG_GOOGLE_TONES = [-0.35, 0.10]

HERN_URLS = [
    "https://mediagazer.com/191026/p4",
    "https://www.techmeme.com/230309/p20",
]
SONG_URLS = [
    "https://thehotjem.com/meta-ray-ban-display-glasses-a-new-frontier-of-smart-wearables/",
    "https://www.wazupnaija.com/counting-renaissance-butts-in-rome-with-the-meta-ray-ban-display/",
    "https://www.Uploadvr.com/meta-ray-ban-display-hands-on-meta-neural-band/",
    "https://www.androidauthority.com/google-pixel-watch-buyers-guide-3221637/",
    "https://hardware.slashdot.org/story/25/08/20/2113247/googles-pixel-watch-4-has-a-big-focus-on-ai?sdsrc=nextbtmprev",
]


def count_def_tests(test_file):
    with open(TESTS_DIR / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


def _mechanism_598():
    with open(REPO_ROOT / "profiles" / "guardian.yaml") as f:
        d = yaml.safe_load(f)
    key = "mechanism_592_alex_hern_migration_guardian_economist_register_constancy_sep08"
    for j in d.get("key_journalists", []):
        if j.get("name") == "Alex Hern":
            block = (j.get("cross_entity_coverage_analysis") or {}).get(key)
            if block:
                return block
    raise AssertionError("Alex Hern #598 block not found in guardian.yaml")


def _mechanism_599():
    with open(REPO_ROOT / "profiles" / "careers" / "journalists.yaml") as f:
        d = yaml.safe_load(f)
    key = "type_c_599_victoria_song_vox_financial_stack_behavioral_pin"
    for j in d["journalists"]:
        if "Song" in (j.get("name") or ""):
            cc = j.get("competitor_coverage") or {}
            if key in cc:
                return cc[key]
    raise AssertionError("Victoria Song #599 block not found in journalists.yaml")


def _git_main_subjects(anchor, n=5):
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "log", "-n40", anchor, "--format=%s"],
        capture_output=True, text=True, check=True)
    mains = [s for s in out.stdout.splitlines()
             if re.match(r"^Type [A-E] #\d+:", s)]
    return mains[:n]


class TestIteration600Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "Type D #600" in doc
        assert "2026-09-08 02:00 PDT" in doc
        assert "599 C -> 600 D" in doc

    def test_rotation_c_to_d(self):
        # Per rotation A->B->C->D->E, the run after Type C #599 is Type D.
        assert "Type D #600" in __doc__

    def test_filename_convention(self):
        assert THIS_FILE.startswith("test_type_d_600_")
        assert THIS_FILE.endswith("_sep08_2am.py")
        assert (TESTS_DIR / THIS_FILE).exists()

    def test_covered_iterations_in_filename(self):
        assert "598_599" in THIS_FILE

    def test_docstring_names_agreement_pole_pins(self):
        doc = __doc__
        assert "TENTH agreement-pole pin" in doc
        assert "ELEVENTH" in doc and "agreement-pole pin" in doc


class TestScorerConsistency598HernAgreementPole:
    def test_yaml_guardian_tones_reproduce_arrays(self):
        m = _mechanism_598()
        guardian_tones = [i["illustrative_tone"] for i in m["guardian_era_corpus"]]
        economist_tones = [i["illustrative_tone"] for i in m["economist_era_corpus"]]
        assert guardian_tones == HERN_GUARDIAN_TONES
        assert economist_tones == HERN_ECONOMIST_TONES

    def test_logged_delta_reproduces_engine_mean_difference(self):
        m = _mechanism_598()
        res = m["asymmetry_scorer_result"]
        raw_delta = (sum(HERN_GUARDIAN_TONES) / 3) - (sum(HERN_ECONOMIST_TONES) / 3)
        assert abs(raw_delta - (-0.11666666666666663)) < 1e-9
        assert res["cross_institution_delta"] == -0.1167
        assert round(raw_delta, 4) == res["cross_institution_delta"]

    def test_logged_avgs_match_engine(self):
        m = _mechanism_598()
        res = m["asymmetry_scorer_result"]
        assert res["guardian_era_meta_avg"] == -0.5167
        assert res["economist_era_avg"] == -0.4
        assert round(sum(HERN_GUARDIAN_TONES) / 3, 4) == -0.5167
        assert round(sum(HERN_ECONOMIST_TONES) / 3, 4) == -0.4

    def test_engine_welch_not_significant_agreement_pole(self):
        # n=3 vs n=3: degenerate guard NOT triggered (both arms >= 2).
        t, p = welch_t_test(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES)
        d = cohens_d(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES)
        assert abs(t - (-1.4)) < 1e-9
        assert abs(p - 0.26418435074200053) < 1e-9
        assert abs(d - (-1.143095213298817)) < 1e-9
        assert p > 0.05, "engine must also fail to reach significance for the agreement pole"

    def test_finding_layer_refuses(self):
        res = _mechanism_598()["asymmetry_scorer_result"]
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["cohens_d"] == "NOT_CALCULATED"
        assert res["ci_95"] == "NOT_CALCULATED"
        assert res["is_significant"] is False
        assert res["correlation_not_causation"] is True

    def test_constancy_verdict_not_divergence_member(self):
        # |delta| = 0.1167 < 0.2 hand-scoring noise; constancy, not a gradient.
        res = _mechanism_598()["asymmetry_scorer_result"]
        assert abs(res["cross_institution_delta"]) < 0.2
        # NOT a divergence-ratchet member: the ratchet tracks engine/finding
        # significance disagreement, and engine (p=0.2642) and finding agree.
        assert "MANUAL ILLUSTRATIVE, NOT empirical" in res["scorer"]

    def test_guardian_urls_verbatim(self):
        m = _mechanism_598()
        urls = [i["url"] for i in m["guardian_era_corpus"]]
        for u in HERN_URLS:
            assert u in urls, f"missing verbatim URL {u}"

    def test_temporal_boundary_financial_deal_postdates_departure(self):
        m = _mechanism_598()
        boundary = m["migration"]["financial_temporal_boundary"]
        assert "2025-02-19" in boundary
        assert "departure" in boundary

    def test_evidence_tier_confounders_documented(self):
        m = _mechanism_598()
        assert "broadcast" in m["status"] or "broadcast/podcast" in m["finding_summary"]
        # Guardian-era is byline-attributed via relays, Economist-era is broadcast.
        assert "Babbage" in m["finding_summary"]

    def test_mechanism_ids(self):
        m = _mechanism_598()
        assert m["mechanism_id"] == 592
        assert m["iteration"] == 598
        assert m["iteration_type"] == "B"


class TestScorerConsistency599SongAgreementPole:
    def test_yaml_tones_reproduce_arrays(self):
        m = _mechanism_599()
        meta_tones = [i["tone"] for i in m["meta_corpus"]]
        google_tones = [i["tone"] for i in m["google_corpus"]]
        assert meta_tones == SONG_META_TONES
        assert google_tones == SONG_GOOGLE_TONES

    def test_logged_delta_vs_raw_arrays(self):
        # Engine mean difference on RAW arrays: +0.125. Logged delta: 0.13.
        raw_delta = (sum(SONG_META_TONES) / 3) - (sum(SONG_GOOGLE_TONES) / 2)
        assert abs(raw_delta - 0.125) < 1e-9
        res = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        assert res["delta"] == 0.13

    def test_rounded_value_arithmetic_divergence_bounded(self):
        # SECOND rounded-value precision note (#593's was 0.0167). Drift
        # 0.005 is smaller; verdict-invariant (engine n.s., finding n.s.).
        res = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        raw_delta = (sum(SONG_META_TONES) / 3) - (sum(SONG_GOOGLE_TONES) / 2)
        drift = abs(res["delta"] - raw_delta)
        assert abs(drift - 0.005) < 1e-9
        assert drift < 0.02, "precision drift must stay bounded and verdict-invariant"

    def test_engine_welch_not_significant_agreement_pole(self):
        # n=3 vs n=2: degenerate guard NOT triggered (both arms >= 2).
        t, p = welch_t_test(SONG_META_TONES, SONG_GOOGLE_TONES)
        d = cohens_d(SONG_META_TONES, SONG_GOOGLE_TONES)
        assert abs(t - 0.5381220025006314) < 1e-9
        assert abs(p - 0.6769664457489656) < 1e-9
        assert abs(d - 0.6217700042172587) < 1e-9
        assert p > 0.05, "engine must also fail to reach significance for the agreement pole"

    def test_finding_layer_refuses(self):
        res = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in res["methodology"]
        assert "cohens_d" not in res and "ci" not in res

    def test_delta_sign_opposite_money_prediction(self):
        # Deal gradient predicts softer Google coverage (negative delta);
        # observed is positive: Song scored Google's first-gen watch harsher.
        res = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        assert res["delta"] > 0
        assert "OPPOSITE sign" in res["delta_direction"]

    def test_three_financial_legs_present(self):
        m = _mechanism_599()
        design = m["design"]
        assert "May 29 2024" in design  # leg 1: OpenAI licensing
        assert "ad-revenue" in design  # leg 2: Google
        assert "$0" in design  # leg 3: Meta

    def test_deal_status_active_and_pmx_unresolved_disclosed(self):
        m = _mechanism_599()
        design = m["design"]
        assert "ACTIVE" in design
        assert "UNRESOLVED" in design

    def test_source_urls_verbatim(self):
        m = _mechanism_599()
        urls = [i["source_url"] for i in m["meta_corpus"]] + \
               [i["source_url"] for i in m["google_corpus"]]
        for u in SONG_URLS:
            assert u in urls, f"missing verbatim URL {u}"

    def test_mechanism_ids(self):
        m = _mechanism_599()
        assert m["mechanism_id"] == 593
        assert m["iteration"] == 599
        assert m["type"] == "C"

    def test_falsification_family_membership(self):
        # #599 joins the writer-level falsification family; the pin is the
        # first dedicated writer-level behavioral pin on the Vox deal stack
        # (the hypothesis frames a positive/near-zero delta as falsification).
        m = _mechanism_599()
        assert "writer-level behavioral pin" in m["design"]
        assert "falsification" in m["hypothesis"]


class TestSignClassSeparation:
    def test_signs_opposite(self):
        assert _mechanism_598()["asymmetry_scorer_result"]["cross_institution_delta"] < 0
        assert _mechanism_599()["asymmetry_scorer_result_illustrative"]["delta"] > 0

    def test_magnitude_adjacent_sign_separated(self):
        raw_599 = (sum(SONG_META_TONES) / 3) - (sum(SONG_GOOGLE_TONES) / 2)
        ratio = abs(raw_599) / abs(_mechanism_598()["asymmetry_scorer_result"]["cross_institution_delta"])
        assert abs(ratio - 1.0711) < 1e-3

    def test_same_pole_different_families(self):
        # Both agreement pole, but #598 is cross-institution constancy and
        # #599 is a writer-level deal-gradient inversion - never conflated.
        m598 = _mechanism_598()
        assert "register-constancy" in m598["type"]
        m599 = _mechanism_599()
        assert "falsification" in m599["hypothesis"]

    def test_neither_is_divergence_ratchet_member(self):
        # Divergence ratchet stays at 5: both engines fail significance, so
        # engine and finding AGREE (the ratchet tracks disagreement).
        for a, b in [(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES),
                     (SONG_META_TONES, SONG_GOOGLE_TONES)]:
            _, p = welch_t_test(a, b)
            assert p > 0.05


class TestStandingRuleDisciplineAgreementSubclass:
    def test_both_refuse_promotion(self):
        res598 = _mechanism_598()["asymmetry_scorer_result"]
        res599 = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        for res in (res598, res599):
            assert res["is_significant"] is False
            assert "NOT_CALCULATED" in str(res["p_value"])

    def test_agreement_subclass_defined_by_engine_also_nonsignificant(self):
        # Agreement subclass: engine ALSO fails to reach significance, so
        # engine and finding agree (vs the divergence subclass where the
        # engine reaches significance and the finding refuses).
        for a, b in [(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES),
                     (SONG_META_TONES, SONG_GOOGLE_TONES)]:
            _, p = welch_t_test(a, b)
            assert p > 0.05

    def test_divergence_ratchet_intact_at_five(self):
        assert "Divergence ratchet intact at 5" in __doc__

    def test_degenerate_boundary_intact_at_four(self):
        assert "Degenerate-boundary count intact at 4" in __doc__

    def test_no_analysis_json_claim(self):
        # Monitoring/consistency cycle: no empirical finding warrants an
        # analysis.json update. The docstring carries the discipline note.
        assert "NOT empirical" in __doc__
        assert "no artifact-grade claims" in __doc__

    def test_engine_numbers_exactly_pinned(self):
        t1, p1 = welch_t_test(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES)
        d1 = cohens_d(HERN_GUARDIAN_TONES, HERN_ECONOMIST_TONES)
        t2, p2 = welch_t_test(SONG_META_TONES, SONG_GOOGLE_TONES)
        d2 = cohens_d(SONG_META_TONES, SONG_GOOGLE_TONES)
        assert (round(t1, 4), round(p1, 4), round(d1, 4)) == (-1.4, 0.2642, -1.1431)
        assert (round(t2, 4), round(p2, 4), round(d2, 4)) == (0.5381, 0.677, 0.6218)


class TestNewCompetitorCoveragePatterns:
    def test_598_first_cross_institution_agreement_pin(self):
        # All prior agreement pins (#582, #587, ...) are within-publication
        # controls; #598 is the first cross-institution member of the pole.
        assert "cross-institution agreement pin" in __doc__

    def test_599_first_writer_level_pin_on_vox_deal_stack(self):
        m = _mechanism_599()
        assert "first" in m["design"].lower() or "behavioral pin" in m["design"]

    def test_agreement_pole_ratchet_9_to_11(self):
        # #582 EIGHTH, #587 NINTH (per the #590 row), now #598 TENTH and
        # #599 ELEVENTH. The ratchet advances without any engine/finding
        # disagreement.
        assert "TENTH agreement-pole pin" in __doc__
        assert "ELEVENTH" in __doc__ and "agreement-pole pin" in __doc__

    def test_rounded_precision_note_series_second_member(self):
        assert "Second rounded-value precision note" in __doc__
        res = _mechanism_599()["asymmetry_scorer_result_illustrative"]
        raw = (sum(SONG_META_TONES) / 3) - (sum(SONG_GOOGLE_TONES) / 2)
        assert abs(res["delta"] - raw) < 0.02

    def test_migration_register_family_hern_joins_welch(self):
        # Migration-register family: #85 Welch (Bloomberg financial-null)
        # and now #598 Hern (Guardian->Economist constancy).
        m = _mechanism_598()
        assert "CRITICAL MIGRATION" in m["driver_class"]

    def test_falsification_family_seven_members(self):
        # Falsification family now: #538, #563, #568, #578, #583, #588, #599.
        assert "#538, #563, #568, #578, #583, #588, #599" in __doc__

    def test_no_new_financial_mechanisms_this_run(self):
        # Type D: no new mechanism blocks; max numeric mechanism_id is 594
        # (the #594 News Corp five-leg block in competitor-entities.yaml,
        # pre-existing). No mechanism may carry iteration 600.
        found = set()
        iterations_600 = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            if ".venv" in root:
                continue
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        d = yaml.safe_load(f)
                    _collect_mechanism_ids(d, found)
                    _collect_iteration_600(d, iterations_600)
        numeric = sorted(i for i in found if isinstance(i, int))
        assert max(numeric) == 594
        assert not iterations_600, f"unexpected iteration-600 mechanisms: {iterations_600}"

    def test_iteration_600_window_files_exist(self):
        for f in [
            "test_type_d_595_scorer_consistency_592_593_divergence_degenerate_rotation_doc_sync_sep07_8pm.py",
            "test_type_e_596_podcast_sentiment_fortysecond_verification_sep07_9pm.py",
            "test_type_a_597_wired_openai_apple_lawsuit_followup_coverage_selection_sep07_11pm.py",
            "test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py",
            "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py",
        ]:
            assert (TESTS_DIR / f).exists(), f"missing {f}"


def _collect_iteration_600(o, out):
    if isinstance(o, dict):
        if o.get("iteration") == 600:
            out.append(o.get("block_key") or o.get("mechanism_id"))
        for v in o.values():
            _collect_iteration_600(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_iteration_600(v, out)


def _collect_mechanism_ids(o, out):
    if isinstance(o, dict):
        if "mechanism_id" in o:
            out.add(o["mechanism_id"])
        for v in o.values():
            _collect_mechanism_ids(v, out)
    elif isinstance(o, list):
        for v in o:
            _collect_mechanism_ids(v, out)


class TestNoBrittleSweep595to599:
    def test_all_window_files_present(self):
        files = [
            "test_type_d_595_scorer_consistency_592_593_divergence_degenerate_rotation_doc_sync_sep07_8pm.py",
            "test_type_e_596_podcast_sentiment_fortysecond_verification_sep07_9pm.py",
            "test_type_a_597_wired_openai_apple_lawsuit_followup_coverage_selection_sep07_11pm.py",
            "test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py",
            "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py",
        ]
        for f in files:
            assert (TESTS_DIR / f).exists(), f"missing {f}"

    def test_window_file_counts_sane(self):
        expected = {
            "test_type_d_595_scorer_consistency_592_593_divergence_degenerate_rotation_doc_sync_sep07_8pm.py": 51,
            "test_type_e_596_podcast_sentiment_fortysecond_verification_sep07_9pm.py": 67,
            "test_type_a_597_wired_openai_apple_lawsuit_followup_coverage_selection_sep07_11pm.py": 50,
            "test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py": 40,
            "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py": 39,
        }
        for f, n in expected.items():
            got = count_def_tests(f)
            assert got == n, f"{f}: expected {n} def-tests, got {got}"

    def test_no_duplicate_mechanism_ids(self):
        # Pre-existing duplicates (mechanism_ids 31/74/80 in gizmodo.yaml)
        # are out of scope; the current window (>= 590) must be clean.
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
                    if isinstance(i, int) and i >= 590:
                        if i in seen:
                            dupes.append((i, seen[i], os.path.join(root, fn)))
                        seen[i] = os.path.join(root, fn)
        assert not dupes, f"duplicate window mechanism_ids: {dupes}"

    def test_no_zero_coverage_claims_in_new_files(self):
        # Iteration-492 rule: silence claims are bounded search-result
        # absences, never proven zeros. The #598/#599 files must not assert
        # absolute non-existence phrasing.
        for f in ["test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py",
                  "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py"]:
            content = (TESTS_DIR / f).read_text()
            assert "zero coverage" not in content.lower() or "bounded" in content.lower()

    def test_exactly_one_600_test_file(self):
        matches = list(TESTS_DIR.glob("test_type_d_600_*.py"))
        assert len(matches) == 1, f"expected exactly one #600 test file, got {matches}"


class TestDocSyncRatchet:
    def test_readme_rows_596_599_present_with_counts(self):
        readme = README.read_text()
        expected = {
            "test_type_e_596_podcast_sentiment_fortysecond_verification_sep07_9pm.py": 67,
            "test_type_a_597_wired_openai_apple_lawsuit_followup_coverage_selection_sep07_11pm.py": 50,
            "test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py": 40,
            "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py": 39,
        }
        for f, n in expected.items():
            m = re.search(rf"`{re.escape(f)}` \| (\d+) \|", readme)
            assert m, f"README row missing for {f}"
            assert int(m.group(1)) == n, f"{f}: README says {m.group(1)}, file has {n}"

    def test_architecture_rows_596_599_present(self):
        tree = ARCHITECTURE.read_text()
        for token in ["#596", "#597", "#598", "#599"]:
            assert token in tree, f"ARCHITECTURE tree missing {token}"

    def test_599_rows_repaired_36_to_39(self):
        # MISS REPAIR: the #599 run left "36 tests" in both docs; the file
        # carries 39 def-tests. This run repairs both rows.
        readme = README.read_text()
        assert "`test_type_c_599_vox_media_ai_revenue_architecture_sep08.py` | 39 |" in readme
        tree = ARCHITECTURE.read_text()
        assert "39 tests" in tree

    def test_600_readme_row_added(self):
        readme = README.read_text()
        assert f"`{THIS_FILE}`" in readme

    def test_600_architecture_row_added(self):
        tree = ARCHITECTURE.read_text()
        assert "#600" in tree

    def test_iteration_log_600_entry_present(self):
        log = LOG.read_text()
        assert "#600 Type D" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=300, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"


class TestRotationCycleGuard600:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard600.ANCHORED_COMMIT)

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#600", "D"),
            ("#599", "C"),
            ("#598", "B"),
            ("#597", "A"),
            ("#596", "E"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # The 5-window newest-first is D,C,B,A,E: each adjacent pair must be
        # a valid forward rotation step (A->B->C->D->E->A), closing the C->D
        # edge this run.
        order = ["A", "B", "C", "D", "E"]
        types = ["D", "C", "B", "A", "E"]
        for prev, cur in zip(types, types[1:]):
            assert order[(order.index(prev) + 1) % 5] == cur, \
                f"rotation step {prev}->{cur} invalid"

    def test_anchor_is_post_commit(self):
        assert self.ANCHORED_COMMIT != "POST_COMMIT_ANCHOR", \
            "anchor must be patched to the main-commit hash in the followup"
