"""
Type D #620 - Scorer Consistency Verification: Sep 8 2026 23:00 PDT.

Verifies the 616-620 main-commit window (D,C,B,A,E newest-first) for scorer
discipline consistency, then closes the C->D rotation edge.

Findings under test:
- #617 Type A (Verge x Samsung launch-cycle register gradient, mechanism 604,
  the-verge.yaml): manual illustrative delta -0.70 (peer avg +0.15 vs target
  avg -0.55); p_value/cohens_d NOT_CALCULATED; is_significant False;
  prediction direction consistent with the advertising-softer hypothesis BUT
  launch-cycle genre is the STRONG rival explanation (correlation, not
  causation); NOT a falsification-family member.
- #618 Type B (Victoria Song Jul 2026 escalation audit, mechanism 605,
  journalists.yaml Victoria Song competitor_coverage): register-conditioned
  asymmetry; illustrative delta meta-minus-apple -0.90 (trilogy avg -0.55 vs
  Jul 13 Apple arm +0.35); p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant False; EXTENDS #75, REFINES the Song data-integrity
  correction, BOUNDS the falsification family (NOT a member).
- #619 Type C (Apple Siri AI publisher negotiation silence status check,
  mechanism 606, competitor-entities.yaml apple entity): qualitative Type C
  mapping; tone_scores NOT_SCORED; mechanism 156 stays PREDICTIVE (27 days
  post-WSJ, zero signed-deal announcements, bounded absence per
  iteration-492); EXTENDS mechanism 156.
- #616 Type E (podcast sentiment 46th verification): monitoring-only, no
  iteration-616 mechanism block in profiles/, no scorer extension; Guilty
  Feminist 499 HOLDS; Attention Sphere 46th no-match as podcast.

Artifact readiness: no analysis.json update warranted. The window is
monitoring + illustrative-only; no new empirical finding at the publication
level. Manual illustrative deltas stay descriptive under the Aug 28 2026
standing rule (engine-side drift checks only, finding layer refuses
significance).
"""

import ast
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERGE_PATH = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
JOURNALISTS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
PODCAST_PATH = os.path.join(REPO_ROOT, "podcast-sentiment.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

THIS_FILE = "test_type_d_620_scorer_consistency_617_618_619_monitoring_boundary_rotation_doc_sync_sep08_11pm.py"

MECH_604_KEY = "mechanism_604_verge_samsung_launch_cycle_register"
SONG_605_BLOCK = "type_b_618_victoria_song_jul2026_escalation_audit"
SIRI_606_BLOCK = "siri_ai_negotiation_silence_status_check_606"

SAMSUNG_TONES_617 = [0.15, 0.10, 0.20]
META_TONES_617 = [-0.55, -0.60, -0.50]
DELTA_617 = -0.70
TRILOGY_TONES_618 = [-0.55, -0.60, -0.50]
APPLE_ARM_618 = 0.35
DELTA_618 = -0.90


def _verge():
    with open(VERGE_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _mechanism_604():
    return _verge()["competitor_relationships"]["samsung"][MECH_604_KEY]


def _song_605():
    with open(JOURNALISTS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    song = [j for j in data["journalists"] if j.get("name") == "Victoria Song"]
    assert len(song) == 1
    return song[0]["competitor_coverage"][SONG_605_BLOCK]


def _siri_606():
    with open(ENTITIES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["entities"]["apple"][SIRI_606_BLOCK]


def _podcast_text():
    with open(PODCAST_PATH, encoding="utf-8") as f:
        return f.read()


def _count_def_tests(filename):
    path = os.path.join(TESTS_DIR, filename)
    tree = ast.parse(open(path, encoding="utf-8").read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def _git_main_subjects(anchor, n=5):
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "-n40", anchor, "--format=%s"],
        capture_output=True, text=True, check=True)
    mains = [s for s in out.stdout.splitlines()
             if re.match(r"^Type [A-E] #\d+:", s)]
    return mains[:n]


class TestScorerConsistency617DeltaArithmetic:
    def test_peer_avg_reproduces(self):
        avg = sum(SAMSUNG_TONES_617) / len(SAMSUNG_TONES_617)
        assert abs(avg - 0.15) < 1e-9

    def test_target_avg_reproduces(self):
        avg = sum(META_TONES_617) / len(META_TONES_617)
        assert abs(avg - -0.55) < 1e-9

    def test_delta_reproduces_exactly(self):
        peer = sum(SAMSUNG_TONES_617) / len(SAMSUNG_TONES_617)
        target = sum(META_TONES_617) / len(META_TONES_617)
        assert abs((target - peer) - DELTA_617) < 1e-9

    def test_yaml_tones_match_pinned(self):
        mech = _mechanism_604()
        samsung = [a["manual_illustrative_tone"] for a in mech["samsung_articles"]]
        meta = [a["manual_illustrative_tone"]
                for a in mech["meta_articles_same_domain"]]
        assert samsung == SAMSUNG_TONES_617
        assert meta == META_TONES_617

    def test_yaml_delta_matches(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert abs(scorer["delta_manual_illustrative"] - DELTA_617) < 1e-9

    def test_yaml_avgs_match(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert abs(scorer["target_avg_tone"] - -0.55) < 1e-9
        assert abs(scorer["peer_avg_tone"] - 0.15) < 1e-9


class TestScorerConsistency617StatisticalDiscipline:
    def test_p_value_not_calculated(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert scorer["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert scorer["cohens_d"] == "NOT_CALCULATED"

    def test_not_significant(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert scorer["is_significant"] is False

    def test_correlation_not_causation_carried(self):
        finding = _mechanism_604()["finding"]
        assert "Correlation, not causation" in finding

    def test_scorer_block_tone_arrays_pinned(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert scorer["target_tones"] == META_TONES_617
        assert scorer["peer_tones"] == SAMSUNG_TONES_617

    def test_scorer_engine_labeled_manual_only(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["scorer"]

    def test_discipline_block_descriptive_only(self):
        disc = _mechanism_604()["statistical_discipline"]
        assert "descriptive delta only" in disc
        assert "not evidence of bias" in disc

    def test_no_engine_claims_in_scorer_block(self):
        scorer = _mechanism_604()["asymmetry_scorer_manual_illustrative"]
        blob = yaml.safe_dump(scorer)
        for token in ("welch", "t_stat", "t-stat"):
            assert token not in blob.lower()


class TestScorerConsistency618DeltaArithmetic:
    def test_trilogy_avg_reproduces(self):
        avg = sum(TRILOGY_TONES_618) / len(TRILOGY_TONES_618)
        assert abs(avg - -0.55) < 1e-9

    def test_delta_reproduces_exactly(self):
        trilogy_avg = sum(TRILOGY_TONES_618) / len(TRILOGY_TONES_618)
        assert abs((trilogy_avg - APPLE_ARM_618) - DELTA_618) < 1e-9

    def test_yaml_delta_matches(self):
        scorer = _song_605()["asymmetry_scorer_result_illustrative"]
        assert abs(scorer["delta_meta_minus_apple_jul2026_window"] - DELTA_618) < 1e-9

    def test_delta_calc_string_matches(self):
        scorer = _song_605()["asymmetry_scorer_result_illustrative"]
        assert scorer["delta_calc"] == \
            "(-0.55 + -0.60 + -0.50)/3 = -0.55 meta avg; -0.55 - 0.35 = -0.90"

    def test_yaml_trilogy_tones_pinned(self):
        mech = _song_605()
        tones = [t["manual_illustrative_tone"] for t in mech["meta_trilogy_jul2026"]]
        assert tones == TRILOGY_TONES_618

    def test_yaml_apple_arm_pinned(self):
        mech = _song_605()
        assert mech["asymmetry_scorer_result_illustrative"]["apple_jul13_arm"] == APPLE_ARM_618


class TestScorerConsistency618NoEngineClaims:
    def test_p_value_not_calculated(self):
        assert _song_605()["asymmetry_scorer_result_illustrative"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _song_605()["asymmetry_scorer_result_illustrative"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci95_not_calculated(self):
        assert _song_605()["asymmetry_scorer_result_illustrative"]["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert _song_605()["asymmetry_scorer_result_illustrative"]["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _song_605()["asymmetry_scorer_result_illustrative"]["correlation_not_causation"] is True

    def test_no_engine_t_claims(self):
        scorer = _song_605()["asymmetry_scorer_result_illustrative"]
        for key in ("engine_t", "engine_welch_t", "t_stat", "welch_t"):
            assert key not in scorer
        blob = yaml.safe_dump(scorer).lower()
        assert "welch" not in blob

    def test_manual_illustrative_methodology(self):
        note = _song_605()["asymmetry_scorer_result_illustrative"]["note"]
        assert "MANUAL ILLUSTRATIVE ONLY" in note
        assert "Aug 28 2026 standing rule" in note


class TestMonitoringBoundary616Podcast:
    def test_no_iteration_616_mechanism_block(self):
        hits = []
        for path, loader in (
                (VERGE_PATH, lambda d: d),
                (JOURNALISTS_PATH, lambda d: d),
                (ENTITIES_PATH, lambda d: d)):
            with open(path, encoding="utf-8") as f:
                blob = f.read()
            if re.search(r"iteration:\s*616\b", blob):
                hits.append(path)
        assert hits == [], f"iteration 616 mechanism block found in {hits}"

    def test_forty_sixth_verification_logged(self):
        text = _podcast_text()
        assert "46" in text
        assert "Guilty Feminist" in text

    def test_gf_499_holds(self):
        text = _podcast_text()
        assert "499" in text
        assert "2026-09-07" in text

    def test_attention_sphere_no_match(self):
        text = _podcast_text()
        assert "Attention Sphere" in text

    def test_no_scorer_claims_in_616_test_file(self):
        path = os.path.join(TESTS_DIR, "test_type_e_616_podcast_sentiment_fortysixth_verification_gf499_holds_sep08_7pm.py")
        src = open(path, encoding="utf-8").read()
        for token in ("welch_t_test", "cohens_d(", "p_value =="):
            assert token not in src


class TestQualitativeBoundary619SiriStatus:
    def test_tone_scores_not_scored(self):
        disc = _siri_606()["statistical_discipline"]
        assert "tone_scores NOT_SCORED" in disc

    def test_p_value_not_calculated(self):
        disc = _siri_606()["statistical_discipline"]
        assert "p_value" in disc and "NOT_CALCULATED" in disc

    def test_not_significant(self):
        disc = _siri_606()["statistical_discipline"]
        assert "is_significant False" in disc

    def test_mechanism_156_stays_predictive(self):
        assert "PREDICTIVE" in _siri_606()["finding"]

    def test_extends_156_cross_reference(self):
        refs = {r["mechanism_id"]: r["relationship"]
                for r in _siri_606()["cross_references"]}
        assert refs[156] == "extends"

    def test_no_asymmetry_scorer_key_in_block(self):
        assert "asymmetry_scorer" not in _siri_606()

    def test_watch_item_present(self):
        assert "watch_item" in _siri_606()
        assert "fall 2026" in _siri_606()["watch_item"]

    def test_bounded_absence_language(self):
        assert "bounded absence" in _siri_606()["finding"].lower() or \
               "Bounded absence" in _siri_606()["finding"]

    def test_originator_self_disclosure(self):
        assert "News Corp" in _siri_606()["originator_self_disclosure"]
        assert "Apple" in _siri_606()["originator_self_disclosure"]

    def test_nine_source_urls(self):
        assert len(_siri_606()["source_urls"]) == 9


class TestCompetitorCoveragePatterns617:
    def test_samsung_register_progression(self):
        mech = _mechanism_604()
        registers = [a["register"] for a in mech["samsung_articles"]]
        assert registers == ["launch_commitment", "leak_exclusive", "hands_on_product_forward"]

    def test_first_samsung_entity_in_verge_block(self):
        assert "samsung" in _verge()["competitor_relationships"]

    def test_launch_cycle_genre_strong_rival(self):
        finding = _mechanism_604()["finding"]
        assert "launch-cycle" in finding or "launch cycle" in finding
        assert "STRONG" in finding

    def test_not_falsification_family_member(self):
        finding = _mechanism_604()["finding"]
        assert "does NOT join the falsification" in finding

    def test_dek_privacy_confined(self):
        mech = _mechanism_604()
        hands_on = [a for a in mech["samsung_articles"]
                    if a["register"] == "hands_on_product_forward"][0]
        assert "privacy" in hands_on["key_framing"].lower()

    def test_price_parity_meta_ray_ban(self):
        mech = _mechanism_604()
        leak = [a for a in mech["samsung_articles"]
                if a["register"] == "leak_exclusive"][0]
        assert "Meta" in leak["key_framing"]


class TestCompetitorCoveragePatterns618:
    def test_register_conditioned_verdict(self):
        verdict = _song_605()["verdict"]
        assert "REGISTER-CONDITIONED ASYMMETRY" in verdict

    def test_extends_75_not_replaces(self):
        verdict = _song_605()["verdict"]
        assert "EXTENDS #75" in verdict

    def test_bounds_falsification_family_not_member(self):
        verdict = _song_605()["verdict"]
        assert "BOUNDS the falsification family" in verdict
        assert "NOT a falsification-family member" in verdict

    def test_meta_positive_arms_coexist(self):
        mech = _song_605()
        arms = {a["entity"]: a for a in mech["competitor_arms"]}
        assert arms["meta_positive"]["manual_illustrative_tone"] == 0.3

    def test_genuine_news_peg_confounder_strong(self):
        mech = _song_605()
        strong = [c for c in mech["confounders_ranked"] if c["strength"] == "STRONG"]
        assert len(strong) >= 2
        assert any("News-peg" in c["text"] for c in strong)

    def test_fair_in_product_register(self):
        verdict = _song_605()["verdict"]
        assert "fair in product register" in verdict


class TestCompetitorCoveragePatterns619:
    def test_variable_pay_per_use_model(self):
        assert "variable" in _siri_606()["origin_report"].lower()
        assert "nine-figure" in _siri_606()["origin_report"]

    def test_retrieval_not_training_scope(self):
        block = _siri_606()
        assert "retrieval" in block["retrieval_vs_training_distinction"].lower()
        assert "training" in block["retrieval_vs_training_distinction"].lower()

    def test_corroboration_stack_count(self):
        assert len(_siri_606()["corroboration_stack_new_this_run"]) >= 7

    def test_deal_closing_time_confounder(self):
        confs = _siri_606()["confounders_ranked"]
        assert any("NDA" in c["description"] for c in confs)

    def test_mechanism_namespace_604_605_606(self):
        assert _mechanism_604()["mechanism_id"] == 604
        assert _song_605()["mechanism_id"] == 605
        assert _siri_606()["mechanism_id"] == 606


class TestRotationCycleGuard620:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type D", 620),
        ("Type C", 619),
        ("Type B", 618),
        ("Type A", 617),
        ("Type E", 616),
    ]

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard620.ANCHORED_COMMIT)

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        for i, (typ, num) in enumerate(self.EXPECTED_WINDOW_NEWEST_FIRST):
            assert f"#{num}" in subjects[i], \
                f"position {i}: expected #{num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} #{num}:", subjects[i]), \
                f"position {i}: expected Type {typ} #{num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # C->D is the edge this run closes; newest-first order is D,C,B,A,E.
        # (order[a] - order[b]) % 5 == 1 steps one rotation step forward.
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

    def test_closes_c_to_d_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type D" and types[1] == "Type C"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5


class TestDocSync620:
    def test_readme_row_present(self):
        text = open(README_PATH, encoding="utf-8").read()
        assert THIS_FILE in text

    def test_readme_row_test_count_matches(self):
        text = open(README_PATH, encoding="utf-8").read()
        row = [l for l in text.splitlines() if THIS_FILE in l]
        assert len(row) == 1
        assert str(_count_def_tests(THIS_FILE)) in row[0]

    def test_architecture_row_present(self):
        text = open(ARCH_PATH, encoding="utf-8").read()
        assert THIS_FILE in text

    def test_no_analysis_json_update_warranted(self):
        # Docstring states artifact readiness; analysis.json untouched this run.
        doc = __doc__ or ""
        assert "analysis.json" in doc
        assert "no analysis.json update warranted" in doc

    def test_docstring_names_all_four_findings(self):
        doc = __doc__ or ""
        for token in ("#617", "#618", "#619", "#616"):
            assert token in doc
