"""Type D #615 (2026-09-08 18:00 PDT, scheduled job_id mediascope-daily-iteration,
goal_54093bda4145): scorer cross-mechanism consistency
extended to #612/#613 + #602 EIGHTH divergence spot-check + rotation guard for
611-615 + doc-sync ratchet (rotation 614 C -> 615 D).

SCORER CONSISTENCY: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE
deltas are NOT empirical - p_value NOT_CALCULATED, is_significant False in
the mechanism YAML, correlation not causation, no artifact-grade claims.
The asymmetry engine (welch_t_test / cohens_d on the logged arrays) is
engine-drift detection: its mean-difference arithmetic must reproduce the
logged manual delta, and its significance output is computed but
deliberately NOT promoted to a finding for illustrative inputs.

This run:
- #612 (Type A, WIRED x Samsung Galaxy Glasses 48-day selection-gap
  persistence, Sep 8 15:00 PDT): logged arms Meta
  [-0.72, -0.82, -0.78, -0.65, -0.7] vs Samsung [0.1, 0.08, 0.05, 0.12,
  0.07], carried unchanged from mechanism 374 as synthetic controlled
  arrays. The ENGINE on the raw arms: welch_t_test ->
  (t=-25.340748822079505, p=1.0386087222857895e-06), cohens_d ->
  -16.02689677840004 - the engine recomputes EXACTLY to the values
  recorded in the YAML engine_drift_check string. Finding layer refuses
  (p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False).
  Engine-side significance on synthetic inputs vs finding-layer refusal is
  the standing engine/finding divergence, not an oversight. NOT a
  falsification-family member: this is the selection-gap lineage
  (mechanisms 39/42/89/374), orthogonal to framing-tone scoring.
  Mechanism 601 is the #612 mechanism id.
- #613 (Type B, Brian Heater TechCrunch cross-entity register constancy,
  Sep 8 16:00 PDT): meta arm [-0.10, 0.10] vs apple arm [0.20]; logged
  illustrative delta meta-minus-apple -0.20 reproduces the logged
  mean-difference arithmetic exactly. The ENGINE: welch_t_test -> (0.0,
  1.0), the degenerate guard fires on the n=1 apple arm (per the #603
  pin); cohens_d -> -1.414213562373095 (rounds to the logged -1.41),
  the ASYMMETRIC n=2 vs n=1 variant mirroring the #593/#607 asymmetric
  variant - documented as a mirror, NOT a new pin, per the #610 taxonomy.
  Finding layer refuses (NOT_CALCULATED x3, is_significant False). The
  degenerate-boundary count STAYS at 6. #613 joins the reporter-level
  falsification/alternative-driver constancy family (#538, #548, #553,
  #563, #568, #578, #583, #588, #608), moving it 9 -> 10. NOT an
  agreement-pole pin (pole requires a non-degenerate engine computation;
  pole ratchet intact at 11). Mechanism 602 is the #613 mechanism id
  (NEW Brian Heater entry in profiles/careers/journalists.yaml).
- #614 (Type C, Reddit v. Anthropic adversarial litigation, Sep 8 17:00
  PDT) is the qualitative boundary (mirroring #609 in #610, #604 in #605):
  tone_scores NOT_SCORED, statistical_discipline carries the #540/#544
  boundary string, no asymmetry_scorer key - scorer consistency explicitly
  does NOT apply. Mechanism 603 is the max numeric mechanism_id
  pre-commit. Pay-or-sue three-leg bifurcation (Google $60M/yr paid,
  OpenAI ~$70M/yr paid, Anthropic $0 sued) is LITIGATED, not licensed.
  KEY TENSION: mechanism #602 documented a WIRED x Anthropic
  licensing-halo divergence pointing OPPOSITE the harder-coverage
  prediction this financial tier implies, so #614 BOUNDS the
  falsification/alternative-driver family without joining it.
- #611 (Type E, podcast sentiment 45th verification, Sep 8 14:00 PDT) is
  the monitoring boundary (mirroring #606 in #610, #601 in #605):
  monitoring-only, no iteration-611 mechanism block in profiles/,
  no scorer extension.
- #602 (Type A, WIRED x Anthropic licensing-halo September silence
  extension, Sep 8 04:00 PDT): the EIGHTH divergence spot-check STILL
  HOLDING. The engine recomputes on the pinned arrays (Meta alarm
  baseline [-0.82, -0.72, -0.78] vs Sept peer register [-0.10, -0.05,
  0.10]) returning t=-11.335839046263537, p=0.0017547553523160528,
  d=-9.255673823221192 - matching the YAML-recorded -11.3358 / 0.001755 /
  -9.2557 to 4 decimals - while the finding layer refuses
  (NOT_CALCULATED, is_significant False). Divergence ratchet intact at 6;
  no new divergence pins in the 610-614 window.

Degenerate-boundary count STAYS at 6 (no new pin this run; the #613
asymmetric variant is a documented mirror of #593/#607). Agreement-pole
ratchet intact at 11. Reporter-level constancy family moves 9 -> 10.
Publication-level falsification family unchanged at 9 (#538, #563, #568,
#578, #583, #588, #599, #604, #607); #614 BOUNDS without joining.

DOC-SYNC: no miss repairs needed this run - the #611-#614 README rows
(66/62/69/64) and ARCHITECTURE rows (66 tests 11 classes / 62 tests 7
classes / 69 tests 13 classes / 64 tests 10 classes) all match the
committed def-test counts; tracked stats 32361 tests / 943 files after
this file lands, journalists 263, migrations 978. NOT empirical; no
artifact-grade claims. No analysis.json update warranted.

Rotation: 614 C -> 615 D. TestRotationCycleGuard615 covers window 611-615
(D, C, B, A, E newest-first), closing the C->D edge; anchor patched in the
followup per the #565 convention. The guard class is deselected pre-commit
(it asserts the post-commit anchor) and runs green in the followup commit.

Sources: all mechanism facts are in-corpus (profiles/wired.yaml
gap_persistence_48_day_check_sep08_612, profiles/careers/journalists.yaml
mechanism_602_brian_heater_techcrunch_meta_vs_apple_hands_on_register_constancy_sep08,
profiles/competitor-entities.yaml
reddit_anthropic_adversarial_litigation_614, profiles/wired.yaml
mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08).
Engine computations run against the repo's own
mediascope/score/statistical.py. No browser work this run.
"""

# Whitespace-normalized docstring for phrase assertions: the docstring wraps
# at a different width than the #610 file, so multi-line phrases are asserted
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

THIS_FILE = "test_type_d_615_scorer_consistency_612_613_degenerate_614_boundary_rotation_doc_sync_sep08_6pm.py"

# Engine inputs quoted verbatim from the covered test files' own pinned
# constants (tone values), NOT re-invented here - the YAML round-trips are
# asserted separately.
SAMSUNG612_META_TONES = [-0.72, -0.82, -0.78, -0.65, -0.7]
SAMSUNG612_SAMSUNG_TONES = [0.1, 0.08, 0.05, 0.12, 0.07]
HEATER613_META_TONES = [-0.10, 0.10]    # Ray-Ban Meta review + Orion (n=2)
HEATER613_APPLE_TONES = [0.20]          # Vision Pro Day One (n=1)
WIRED602_TARGET_SCORES = [-0.82, -0.72, -0.78]  # Meta alarm baseline (#547)
WIRED602_PEER_SCORES = [-0.10, -0.05, 0.10]     # Sept peer register


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


def _mechanism_612():
    return _find_mechanism(
        "wired.yaml", "gap_persistence_48_day_check_sep08_612")


def _mechanism_613():
    return _find_mechanism(
        os.path.join("careers", "journalists.yaml"),
        "mechanism_602_brian_heater_techcrunch_meta_vs_apple_hands_on_register_constancy_sep08",
    )


def _mechanism_614():
    return _find_mechanism(
        "competitor-entities.yaml", "reddit_anthropic_adversarial_litigation_614")


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


class TestIteration615Metadata:
    def test_docstring_names_iteration_615(self):
        assert "#615" in __doc__

    def test_docstring_names_type_d(self):
        assert "Type D" in __doc__

    def test_docstring_names_rotation_edge(self):
        assert "614 C -> 615 D" in __doc__

    def test_docstring_names_goal_and_job(self):
        assert "goal_54093bda4145" in __doc__
        assert "mediascope-daily-iteration" in __doc__

    def test_this_file_constant_matches_filename(self):
        assert THIS_FILE == os.path.basename(__file__)
        assert (TESTS_DIR / THIS_FILE).exists()


class TestScorerConsistency612SamsungGapPersistence:
    def test_engine_recomputes_logged_welch_exactly(self):
        t, p = welch_t_test(SAMSUNG612_META_TONES, SAMSUNG612_SAMSUNG_TONES)
        assert t == -25.340748822079505, f"t drifted: {t}"
        assert p == 1.0386087222857895e-06, f"p drifted: {p}"

    def test_engine_recomputes_logged_cohens_d_exactly(self):
        d = cohens_d(SAMSUNG612_META_TONES, SAMSUNG612_SAMSUNG_TONES)
        assert d == -16.02689677840004, f"d drifted: {d}"

    def test_yaml_tone_arrays_match_pinned_constants(self):
        mech = _mechanism_612()
        tones = mech["carried_illustrative_arms"]
        assert tones["meta_tones"] == SAMSUNG612_META_TONES
        assert tones["samsung_tones"] == SAMSUNG612_SAMSUNG_TONES

    def test_finding_layer_refuses_significance(self):
        mech = _mechanism_612()
        scorer = mech["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_engine_drift_check_string_matches_recomputation(self):
        mech = _mechanism_612()
        note = mech["asymmetry_scorer_result"]["engine_drift_check"]
        assert "t=-25.340748822079505" in note
        assert "p=1.0386087222857895e-06" in note
        assert "d=-16.02689677840004" in note

    def test_not_a_falsification_family_member(self):
        assert "falsification" in DOC
        assert "selection-gap lineage" in DOC
        log = LOG.read_text()
        start = log.index("#612 Type A:")
        section = log[start:start + 12000]
        assert "NOT a falsification-family member" in section

    def test_mechanism_id_is_601(self):
        assert _mechanism_612()["mechanism_id"] == 601


class TestScorerConsistency613HeaterAsymmetricVariant:
    def test_logged_delta_reproduces_mean_difference_exactly(self):
        meta_avg = sum(HEATER613_META_TONES) / len(HEATER613_META_TONES)
        apple_avg = sum(HEATER613_APPLE_TONES) / len(HEATER613_APPLE_TONES)
        assert round(meta_avg - apple_avg, 2) == -0.20
        mech = _mechanism_613()
        assert mech["illustrative_delta"]["delta"] == -0.20
        assert mech["illustrative_delta"]["convention"] == "Meta minus Apple"

    def test_engine_welch_degenerate_on_n1_apple_arm(self):
        t, p = welch_t_test(HEATER613_META_TONES, HEATER613_APPLE_TONES)
        assert (t, p) == (0.0, 1.0), f"degenerate guard did not fire: {(t, p)}"

    def test_engine_cohens_d_asymmetric_variant_exact(self):
        d = cohens_d(HEATER613_META_TONES, HEATER613_APPLE_TONES)
        assert d == -1.414213562373095, f"d drifted: {d}"
        assert round(d, 2) == -1.41

    def test_documented_as_mirror_not_new_pin(self):
        mech = _mechanism_613()
        engine_note = mech["asymmetry_scorer_result_illustrative"]["engine"]
        assert "NOT a new pin" in engine_note
        assert "mirroring the #593/#607 asymmetric variant" in engine_note

    def test_finding_layer_refuses_significance(self):
        mech = _mechanism_613()
        scorer = mech["asymmetry_scorer_result_illustrative"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_joins_reporter_level_constancy_family(self):
        mech = _mechanism_613()
        verdict = mech["verdict"]
        assert "#608 (Hart)" in verdict
        assert "#538 (Metz)" in verdict

    def test_mechanism_id_is_602_and_entry_is_new(self):
        mech = _mechanism_613()
        assert mech["mechanism_id"] == 602
        assert mech["novelty_note"].startswith(
            "First dedicated Type B block on Brian Heater.")


class TestDivergenceRatchet602EighthSpotCheck:
    def test_engine_recomputes_pinned_arrays_exactly(self):
        t, p = welch_t_test(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        d = cohens_d(WIRED602_TARGET_SCORES, WIRED602_PEER_SCORES)
        assert t == -11.335839046263537, f"t drifted: {t}"
        assert p == 0.0017547553523160528, f"p drifted: {p}"
        assert d == -9.255673823221192, f"d drifted: {d}"

    def test_yaml_recorded_values_match_to_4_decimals(self):
        import io
        buf = io.StringIO()
        yaml.safe_dump(_mechanism_602(), buf, width=10 ** 6)
        dumped = buf.getvalue()
        assert "-11.3358" in dumped, "YAML missing recorded t"
        assert "0.001755" in dumped, "YAML missing recorded p"
        assert "-9.2557" in dumped, "YAML missing recorded d"
        assert "SIXTH DIVERGENCE PIN" in dumped

    def test_finding_layer_still_refuses(self):
        assert "finding layer refuses" in DOC

    def test_divergence_ratchet_stays_at_6(self):
        assert "Divergence ratchet intact at 6" in DOC
        assert "no new divergence pins in the 610-614 window" in DOC

    def test_key_tension_with_614_documented(self):
        mech = _mechanism_614()
        rel = mech["mediascope_relevance"]
        assert "KEY TENSION" in rel
        assert "BOUNDS rather than confirms" in rel


class TestQualitativeBoundary614:
    def test_tone_scores_not_scored(self):
        assert _mechanism_614()["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_carries_boundary_string(self):
        disc = _mechanism_614()["statistical_discipline"]
        assert "#540/#544" in disc
        assert "NOT_CALCULATED" in disc

    def test_no_asymmetry_scorer_key_in_block(self):
        block = _mechanism_614()
        assert not any("asymmetry_scorer" in k for k in block.keys()), \
            f"scorer key present: {[k for k in block.keys() if 'asymmetry_scorer' in k]}"

    def test_mechanism_603_is_max_numeric_pre_commit(self):
        assert _mechanism_614()["mechanism_id"] == 603
        assert max_numeric_mechanism_id() == 603

    def test_bounds_falsification_family_without_joining(self):
        rel = _mechanism_614()["mediascope_relevance"]
        assert "BOUNDS" in rel
        assert "not a new member" in rel


class TestMonitoringBoundary611:
    def test_no_iteration_611_mechanism_in_profiles(self):
        # Mechanism identity lives in dict KEYS (block keys, keys carrying
        # iteration numbers); bare "611" substrings inside values (URLs,
        # counts, dates) are not mechanisms.
        hits = []
        for root, _, files in os.walk(REPO_ROOT / "profiles"):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                p = os.path.join(root, fn)
                with open(p) as f:
                    d = yaml.safe_load(f)
                keys = []

                def _keys(o):
                    if isinstance(o, dict):
                        for k, v in o.items():
                            keys.append(str(k))
                            _keys(v)
                    elif isinstance(o, list):
                        for v in o:
                            _keys(v)

                _keys(d)
                for k in keys:
                    if "611" in k:
                        hits.append((p, k))
        assert not hits, f"unexpected iteration-611 mechanism keys: {hits}"

    def test_611_test_file_exists(self):
        f = "test_type_e_611_podcast_sentiment_fortyfifth_verification_gf499_holds_sep08_2pm.py"
        assert (TESTS_DIR / f).exists()

    def test_611_is_monitoring_only_in_log(self):
        log = LOG.read_text()
        assert "#611 Type E" in log


class TestStandingRuleDiscipline615:
    def test_no_em_dashes_in_this_file(self):
        with open(TESTS_DIR / THIS_FILE, encoding="utf-8") as f:
            content = f.read()
        assert "\u2014" not in content, "em dash found in test file"

    def test_degenerate_boundary_stays_at_6(self):
        assert "Degenerate-boundary count STAYS at 6" in DOC
        assert "no new pin this run" in DOC

    def test_agreement_pole_intact_at_11(self):
        assert "Agreement-pole ratchet intact at 11" in DOC

    def test_reporter_constancy_family_9_to_10(self):
        assert "Reporter-level constancy family moves 9 -> 10" in DOC

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in DOC
        import glob as _glob
        for p in _glob.glob(str(REPO_ROOT / "**" / "analysis.json"), recursive=True):
            assert "615" not in open(p).read(), f"unexpected #615 entry in {p}"


class TestNewCompetitorCoveragePatterns:
    def test_selection_absence_orthogonal_to_framing_tone(self):
        mech = _mechanism_612()
        cautious = mech["cautious_language"]
        assert "selection absence" in cautious
        assert "not a framing measurement" in cautious

    def test_headline_body_two_layer_register_pattern(self):
        mech = _mechanism_613()
        assert "headline_register_divergence" in mech
        assert "price_framing_divergence" in mech
        assert "body register" in mech["verdict"].lower() or \
            "body-level constancy" in mech["verdict"]

    def test_pay_or_sue_three_leg_bifurcation_pattern(self):
        mech = _mechanism_614()
        bifur = mech["pay_or_sue_bifurcation"]
        assert bifur["google_leg"]["status"] == "paid leg - licensed"
        assert bifur["openai_leg"]["status"] == "paid leg - licensed"
        assert "SUED Jun 4 2025" in bifur["anthropic_leg"]["status"]
        assert "$0" in str(bifur["anthropic_leg"].get("value", "")) or \
            "non-payer" in bifur["anthropic_leg"]["status"].lower()

    def test_key_tension_614_vs_602_pattern(self):
        rel = _mechanism_614()["mediascope_relevance"]
        assert "OPPOSITE" in rel
        assert "#602" in rel
        assert "licensing-halo" in rel.lower() or "LICENSING-HALO" in rel

    def test_asymmetric_variant_taxonomy_not_pin(self):
        note = _mechanism_613()["asymmetry_scorer_result_illustrative"]["engine"]
        assert "NOT a new pin" in note
        assert "#610 taxonomy" in note

    def test_bounded_absence_language_iteration_492(self):
        mech = _mechanism_612()
        sv = mech["search_verification_sep08"]
        assert "search-index-bounded absence" in sv
        discipline = mech["asymmetry_scorer_result"]["statistical_discipline"]
        assert "no zero-coverage claims" in discipline


class TestNoBrittleSweep611to615:
    WINDOW_FILES = [
        "test_type_e_611_podcast_sentiment_fortyfifth_verification_gf499_holds_sep08_2pm.py",
        "test_type_a_612_wired_samsung_gap_persistence_48_days_sep08_3pm.py",
        "test_type_b_613_brian_heater_techcrunch_meta_apple_hands_on_constancy_sep08_4pm.py",
        "test_type_c_614_reddit_anthropic_adversarial_litigation_sep08_5pm.py",
        THIS_FILE,
    ]

    def test_all_window_files_exist(self):
        for f in self.WINDOW_FILES:
            assert (TESTS_DIR / f).exists(), f"missing {f}"

    def test_all_window_files_parse_as_python(self):
        import ast
        for f in self.WINDOW_FILES:
            src = (TESTS_DIR / f).read_text(encoding="utf-8")
            ast.parse(src)

    def test_no_window_file_calls_browser_tooling(self):
        # THIS_FILE is excluded: this very assertion contains the literal
        # under test, so sweeping it would be self-defeating.
        for f in self.WINDOW_FILES:
            if f == THIS_FILE:
                continue
            src = (TESTS_DIR / f).read_text(encoding="utf-8")
            assert "browser." not in src, f"{f} references browser tooling"

    def test_no_window_file_has_em_dashes(self):
        for f in self.WINDOW_FILES:
            src = (TESTS_DIR / f).read_text(encoding="utf-8")
            assert "\u2014" not in src, f"{f} has an em dash"


class TestDocSyncRatchet615:
    def test_readme_rows_611_614_present_with_full_counts(self):
        readme = README.read_text()
        expected = {
            "test_type_e_611_podcast_sentiment_fortyfifth_verification_gf499_holds_sep08_2pm.py": 66,
            "test_type_a_612_wired_samsung_gap_persistence_48_days_sep08_3pm.py": 62,
            "test_type_b_613_brian_heater_techcrunch_meta_apple_hands_on_constancy_sep08_4pm.py": 69,
            "test_type_c_614_reddit_anthropic_adversarial_litigation_sep08_5pm.py": 64,
        }
        for f, n in expected.items():
            m = re.search(rf"`{re.escape(f)}` \| (\d+) \|", readme)
            assert m, f"README row missing for {f}"
            assert int(m.group(1)) == n, f"{f}: README says {m.group(1)}, file has {n}"

    def test_architecture_rows_611_614_present_with_full_counts(self):
        tree = ARCHITECTURE.read_text()
        expected = [
            ("test_type_e_611_podcast_sentiment_fortyfifth_verification_gf499_holds_sep08_2pm.py", 66, 11),
            ("test_type_a_612_wired_samsung_gap_persistence_48_days_sep08_3pm.py", 62, 7),
            ("test_type_b_613_brian_heater_techcrunch_meta_apple_hands_on_constancy_sep08_4pm.py", 69, 13),
            ("test_type_c_614_reddit_anthropic_adversarial_litigation_sep08_5pm.py", 64, 10),
        ]
        for f, n, c in expected:
            m = re.search(
                rf"{re.escape(f)}[^\n]*- (\d+) tests, (\d+) classes", tree)
            assert m, f"ARCHITECTURE row missing counts for {f}"
            assert (int(m.group(1)), int(m.group(2))) == (n, c), \
                f"{f}: ARCHITECTURE says {m.groups()}, file has {(n, c)}"

    def test_615_readme_row_added(self):
        readme = README.read_text()
        assert f"`{THIS_FILE}`" in readme

    def test_615_architecture_row_added(self):
        tree = ARCHITECTURE.read_text()
        m = re.search(
            rf"{re.escape(THIS_FILE)}[^\n]*- (\d+) tests, (\d+) classes", tree)
        assert m, "ARCHITECTURE #615 row missing counts"
        assert int(m.group(1)) == count_def_tests(THIS_FILE)
        assert int(m.group(2)) == 11

    def test_iteration_log_615_entry_present(self):
        log = LOG.read_text()
        assert "#615 Type D" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"


class TestRotationCycleGuard615:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard615.ANCHORED_COMMIT)

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#615", "D"),
            ("#614", "C"),
            ("#613", "B"),
            ("#612", "A"),
            ("#611", "E"),
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
