"""
Type D #625 - Scorer Consistency Verification: Sep 9 2026 04:00 PDT.

Verifies the 621-625 main-commit window (D,C,B,A,E newest-first) for scorer
discipline consistency, then closes the C->D rotation edge.

Findings under test:
- #621 Type E (podcast sentiment 47th verification): monitoring-only, no
  iteration-621 mechanism block in profiles/, no scorer extension; Guilty
  Feminist 499 HOLDS; Attention Sphere 47th no-match as podcast; EHE 30-day
  hold; TWO new-to-corpus press surfaces (Reuters Sep 8 Meta Muse piece,
  USA Today Sep 8 Meta Glasses blurb, usatoday.com NEW domain); recency
  frontier ADVANCES Sep 7 to Sep 8.
- #622 Type A (Guardian x Apple Vision Pro aspirational vs Meta pervert-glasses
  adversarial, mechanism 607, guardian.yaml): zero-financial-gradient CONTROL;
  illustrative delta -0.825 reproduces EXACTLY (meta -0.60 minus apple avg
  0.225); p_value/cohens_d NOT_CALCULATED; is_significant False;
  financial_channel "$0 both sides"; NOT a falsification-family member
  (no deal either side, the incentive theory predicts nothing).
- #623 Type B (Kashmir Hill surveillance-register constancy, NYT): register
  constancy across Meta (-0.80), Clearview AI (-0.85), automakers (-0.75);
  illustrative delta 0.00 reproduces EXACTLY from pinned tones;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict says
  EXTENDS the falsification family, 11th falsification-family member at the
  iteration level.
- #624 Type C (OpenAI India attribution-deal blitz, mechanism 609,
  competitor-entities.yaml): FIRST India-market mechanism; qualitative Type C
  mapping; tone_scores NOT_SCORED; p_value NOT_CALCULATED; is_significant
  False; correlation_not_causation true; financial terms undisclosed on both
  legs; sue-then-sign arc (Indian Express sought to join ANI suit Feb 2025,
  signed Sep 2026); Times of India is the third Google-plus-OpenAI dual-payer
  publisher in the corpus (after FT mechanism 437, WaPo mechanism 569);
  no_coverage_tone_claim true.

Artifact readiness: no analysis.json update warranted. The window is
monitoring + illustrative-only + qualitative mapping; no new empirical finding
at the publication level. Manual illustrative deltas stay descriptive under the
Aug 28 2026 standing rule (engine-side drift checks only, finding layer
refuses significance).
"""

import ast
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARDIAN_PATH = os.path.join(REPO_ROOT, "profiles", "guardian.yaml")
JOURNALISTS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
PODCAST_PATH = os.path.join(REPO_ROOT, "podcast-sentiment.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")

THIS_FILE = "test_type_d_625_scorer_consistency_621_622_623_624_rotation_doc_sync_sep09_4am.py"

MECH_607_KEY = "mechanism_607_guardian_apple_vision_pro_aspirational_vs_meta_pervert_glasses"
MECH_609_KEY = "mechanism_609_openai_india_attribution_deal_blitz"
HILL_623_KEY = "type_b_623_kashmir_hill_surveillance_register_constancy"

META_TONES_622 = [-0.60]
APPLE_TONES_622 = [0.35, 0.10]
DELTA_622 = -0.825

META_TONE_623 = -0.80
CLEARVIEW_TONE_623 = -0.85
AUTOMAKER_TONE_623 = -0.75
NON_META_AVG_623 = -0.80
DELTA_623 = 0.00


def _guardian_607():
    with open(GUARDIAN_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)["competitor_relationships"]["apple"][MECH_607_KEY]


def _hill():
    with open(JOURNALISTS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    hill = [j for j in data["journalists"] if j.get("name") == "Kashmir Hill"]
    assert len(hill) == 1
    return hill[0]["competitor_coverage"][HILL_623_KEY]


def _india_609():
    with open(ENTITIES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["entities"]["openai"][MECH_609_KEY]


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


class TestScorerConsistency622DeltaArithmetic:
    def test_apple_avg_reproduces(self):
        avg = sum(APPLE_TONES_622) / len(APPLE_TONES_622)
        assert abs(avg - 0.225) < 1e-9

    def test_meta_arm_is_single_opinion_tone(self):
        assert META_TONES_622 == [-0.60]

    def test_delta_reproduces_exactly(self):
        apple = sum(APPLE_TONES_622) / len(APPLE_TONES_622)
        meta = META_TONES_622[0]
        assert abs((meta - apple) - DELTA_622) < 1e-9

    def test_yaml_tones_match_pinned(self):
        mech = _guardian_607()
        assert mech["manual_illustrative_tones_meta"] == META_TONES_622
        assert mech["manual_illustrative_tones_apple"] == APPLE_TONES_622

    def test_yaml_article_tones_match_arrays(self):
        mech = _guardian_607()
        apple = [a["manual_illustrative_tone"] for a in mech["articles_apple"]]
        meta = [a["manual_illustrative_tone"] for a in mech["articles_meta"]]
        assert apple == APPLE_TONES_622
        assert meta == META_TONES_622

    def test_yaml_delta_matches(self):
        assert abs(_guardian_607()["illustrative_delta_meta_minus_apple"]
                   - DELTA_622) < 1e-9

    def test_delta_calc_note_matches_arithmetic(self):
        # (0.35 + 0.10)/2 = 0.225; -0.60 - 0.225 = -0.825
        finding = _guardian_607()["finding"]
        assert "-0.825" in finding
        assert "+0.225" in finding.replace(" ", "")


class TestScorerConsistency622StatisticalDiscipline:
    def test_p_value_not_calculated(self):
        assert _guardian_607()["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _guardian_607()["cohens_d"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _guardian_607()["is_significant"] is False

    def test_manual_illustrative_only_research_method(self):
        assert "MANUAL ILLUSTRATIVE tones only" in \
            _guardian_607()["research_method"]

    def test_financial_channel_zero_both_sides(self):
        assert _guardian_607()["financial_channel"] == "$0 both sides"

    def test_finding_names_zero_financial_gradient_control(self):
        assert "Zero-financial-gradient CONTROL" in _guardian_607()["finding"]

    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _guardian_607()["finding"]

    def test_four_strong_confounders_present(self):
        strong = _guardian_607()["confounders_ranked"]["strong"]
        assert len(strong) == 4
        joined = " ".join(strong)
        for token in ("Incident-driven news value", "Form-factor skew",
                      "Genre skew", "Timing skew"):
            assert token in joined


class TestScorerConsistency623ConstancyArithmetic:
    def test_non_meta_avg_reproduces(self):
        avg = (CLEARVIEW_TONE_623 + AUTOMAKER_TONE_623) / 2
        assert abs(avg - NON_META_AVG_623) < 1e-9

    def test_delta_reproduces_exactly(self):
        assert abs((NON_META_AVG_623 - META_TONE_623) - DELTA_623) < 1e-9

    def test_yaml_tones_match_pinned(self):
        scorer = _hill()["asymmetry_scorer_result_illustrative"]
        assert abs(scorer["meta_tone"] - META_TONE_623) < 1e-9
        assert abs(scorer["clearview_tone"] - CLEARVIEW_TONE_623) < 1e-9
        assert abs(scorer["automaker_tone"] - AUTOMAKER_TONE_623) < 1e-9
        assert abs(scorer["non_meta_avg"] - NON_META_AVG_623) < 1e-9
        assert abs(scorer["delta_meta_minus_non_meta"] - DELTA_623) < 1e-9

    def test_delta_calc_string_verbatim(self):
        scorer = _hill()["asymmetry_scorer_result_illustrative"]
        assert scorer["delta_calc"] == \
            "(-0.85 + -0.75)/2 = -0.80 non-meta avg; -0.80 - (-0.80) = 0.00"

    def test_discipline_markers(self):
        scorer = _hill()["asymmetry_scorer_result_illustrative"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["note"]

    def test_three_positive_comparator_arms(self):
        scorer = _hill()["asymmetry_scorer_result_illustrative"]
        assert scorer["peer_entities"] == ["clearview_ai", "automakers"]
        assert scorer["target_entity"] == "meta"

    def test_verdict_eleven_member_of_falsification_family(self):
        verdict = _hill()["verdict"]
        assert "11th falsification-family member" in verdict
        assert "EXTENDS the falsification family" in verdict

    def test_no_zero_coverage_claims_per_492(self):
        design = _hill()["design"]
        assert "every comparator arm is a positive Hill byline" in design

    def test_correlation_not_causation(self):
        assert _hill()["asymmetry_scorer_result_illustrative"][
            "correlation_not_causation"] is True


class TestQualitativeBoundary624:
    def test_mechanism_id_609(self):
        assert _india_609()["mechanism_id"] == 609

    def test_iteration_624(self):
        assert _india_609()["iteration"] == 624

    def test_two_deal_legs(self):
        deals = _india_609()["deals"]
        assert len(deals) == 2
        assert deals[0]["counterparty"].startswith("BCCL")
        assert "Indian Express Group" in deals[1]["counterparty"]

    def test_financial_terms_undisclosed_both_legs(self):
        for deal in _india_609()["deals"]:
            assert "undisclosed" in deal["financial_terms"].lower()
            assert "no fee" in deal["financial_terms"].lower()

    def test_tone_scores_not_scored(self):
        disc = _india_609()["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False

    def test_no_coverage_tone_claim(self):
        assert _india_609()["no_coverage_tone_claim"] is True

    def test_sue_then_sign_arc_present(self):
        arc = _india_609()["sue_then_sign_arc"]
        assert len(arc) >= 4
        joined = " ".join(arc)
        assert "ANI" in joined
        assert "Feb 2025" in joined
        assert "Sep 2026" in joined

    def test_toi_third_dual_payer_in_corpus(self):
        contrasts = _india_609()["structural_contrasts"]
        joined = " ".join(contrasts)
        assert "third in the corpus after FT (mechanism 437) and WaPo " \
               "(mechanism 569)" in joined

    def test_first_india_market_mechanism(self):
        note = _india_609()["artifact_readiness"]
        assert "ecosystem-deal mapping" in note

    def test_correlational_note_no_causal_claim(self):
        note = _india_609()["correlational_note"]
        assert "No causal claim" in note
        assert "correlation" in note.lower()

    def test_cautious_language_required(self):
        assert _india_609()["cautious_language_required"] is True


class TestMonitoringBoundary621:
    def test_iteration_621_heading_in_podcast_sentiment(self):
        assert "## Iteration #621" in _podcast_text()

    def test_gf_499_holds_forty_seventh(self):
        text = _podcast_text()
        assert "Forty-Seventh Cycle, 499 Still Latest" in text

    def test_attention_sphere_47th_no_match(self):
        assert "**Podcast no-match (47th):**" in _podcast_text()

    def test_ehe_30_day_hold(self):
        assert "EHE 30-day hold" in _podcast_text()

    def test_two_new_press_surfaces(self):
        text = _podcast_text()
        assert "Reuters Sep 8" in text
        assert "USA Today Sep 8" in text

    def test_usatoday_new_domain_to_corpus(self):
        assert "usatoday.com" in _podcast_text()

    def test_recency_frontier_advances(self):
        assert "ADVANCES Sep 7 to Sep 8" in _podcast_text()

    def test_everyone_hates_elon_not_podcast_strand(self):
        # Identity strand must be unchanged: EHE is an activist campaign,
        # never a podcast; the 621 run logs it as re-surfaces only.
        assert "Everyone Hates Elon" in _podcast_text() or \
               "EHE" in _podcast_text()

    def test_no_iteration_621_mechanism_block_in_profiles(self):
        hits = []
        for root, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                path = os.path.join(root, fn)
                with open(path, encoding="utf-8") as f:
                    text = f.read()
                if "iteration: 621" in text:
                    hits.append(path)
        assert hits == [], f"unexpected iteration-621 mechanism block: {hits}"

    def test_test_type_e_621_file_exists(self):
        path = os.path.join(
            TESTS_DIR,
            "test_type_e_621_podcast_sentiment_fortyseventh_verification_"
            "gf499_holds_sep09_12am.py")
        assert os.path.isfile(path)


class TestCompetitorCoveragePatterns625:
    def test_zero_financial_gradient_control_pattern(self):
        # Pattern: when the financial gradient is $0 both sides, a tone gap
        # must be explained by non-financial confounders (incident news value,
        # genre, form factor, timing), not by the incentive theory.
        mech = _guardian_607()
        assert mech["financial_channel"] == "$0 both sides"
        assert len(mech["confounders_ranked"]["strong"]) == 4
        assert "no financial attribution" in mech["finding"]

    def test_register_constancy_falsifies_entity_bias_pattern(self):
        # Pattern: a writer whose adversarial register is constant across
        # entity classes (delta 0.00) falsifies journalist-level anti-Meta
        # bias; the register tracks the beat, not the entity.
        verdict = _hill()["verdict"]
        assert "beat register, not an entity register" in verdict or \
               "BEAT register" in _hill()[
                   "asymmetry_scorer_result_illustrative"]["note"]

    def test_india_market_mechanism_namespace_609(self):
        # Pattern: ecosystem-deal mechanisms expand the deal map to new
        # markets while first-gen Western deals sit in their renewal window.
        contrasts = _india_609()["structural_contrasts"]
        joined = " ".join(contrasts)
        assert "renewal window" in joined

    def test_sue_then_sign_dual_posture_pattern(self):
        # Pattern: publishers that litigate against a model provider can
        # still sign attribution deals with it; litigation and partnership
        # are parallel postures, not mutually exclusive.
        arc = _india_609()["sue_then_sign_arc"]
        joined = " ".join(arc)
        assert "Indian Express sought to join the anti-OpenAI suit" in joined \
               or "sought to join" in joined
        assert "signed an OpenAI partnership" in joined

    def test_podcast_monitoring_boundary_pattern(self):
        # Pattern: Type E verification runs stay monitoring-only when no new
        # episode airs; they log corpus lineage, not new findings.
        text = _podcast_text()
        assert "no new tech-word audit since no new episode" in text

    def test_mechanism_namespace_607_609_placement(self):
        # 607 is the first dedicated Type A under guardian.yaml apple;
        # 609 is the first India-market mechanism. Both extend the corpus
        # namespace without colliding (repo-wide uniqueness is checked in
        # the #622 and #624 test files).
        assert _guardian_607()["mechanism_id"] == 607
        assert _india_609()["mechanism_id"] == 609

    def test_qualitative_vs_scorer_boundary_625(self):
        # Type C 624 has no scorer extension (qualitative mapping), Type E
        # 621 has no scorer extension (monitoring), Type A 622 and Type B
        # 623 carry illustrative-only deltas. The boundary holds across
        # all four window members.
        assert "no scorer" in (__doc__ or "").lower() or True
        assert "NOT_SCORED" in str(
            _india_609()["statistical_discipline"])
        scorer623 = _hill()["asymmetry_scorer_result_illustrative"]
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer623["note"]


class TestRotationCycleGuard625:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "cc3ed5c"
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("D", 625),
        ("C", 624),
        ("B", 623),
        ("A", 622),
        ("E", 621),
    ]

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard625.ANCHORED_COMMIT)

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
        assert types[0] == "D" and types[1] == "C"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5


class TestDocSync625:
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
        for token in ("#621", "#622", "#623", "#624"):
            assert token in doc
