"""
Type D #630 - Scorer Consistency Verification: Sep 9 2026 09:00 PDT.

Verifies the 626-630 main-commit window (D,C,B,A,E newest-first) for scorer
discipline consistency, then closes the C->D rotation edge.

Findings under test:
- #626 Type E (podcast sentiment 48th verification): monitoring-only, no
  iteration-626 mechanism block in profiles/, no scorer extension; Guilty
  Feminist 499 HOLDS (13:00 UK, weekly Monday cadence; episode 500 watch
  item penciled Mon Sep 14); Attention Sphere 48th no-match as podcast
  (identity strand unchanged from #596; task-spec still misidentified);
  EHE 30-day hold (6 re-surfaces, all in corpus; no new primary motif; no
  competitor equivalent in 48 cycles); ZERO new-to-corpus press surfaces
  (thevermilion.com Meta Ray-Ban Display Italy piece ~Sep 2025 new-to-corpus
  URL but predates the Sep 8 frontier, NOT a press-surface advance);
  recency frontier TIED at Sep 8 (distinct from #621's advance).
- #627 Type A (The Verge x Amazon Ring surveillance register vs Meta mixed
  product register, mechanism 610, the-verge.yaml amazon entity):
  FIRST dedicated Type A mechanism under the amazon entity (zero mechanism
  keys pre-insertion); illustrative delta +0.8167 reproduces EXACTLY from
  pinned tones target [0.45, 0.2, -0.3] avg 0.1167 vs peer [-0.8, -0.6]
  avg -0.7 (log rounds +0.82); p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant False; financial channel "$0 both sides" (The Verge x
  Amazon: no AI-content deal; PMC sold all Meta shares Q2 2025 per #112);
  zero-financial-gradient CONTROL, NOT a falsification-family member
  (no deal either side, the incentive theory predicts nothing; register gap
  is event/genre-driven).
- #628 Type B (Samuel Gibbs, Guardian consumer technology editor,
  within-writer genre register, mechanism 611, journalists.yaml):
  illustrative delta -0.25 reproduces EXACTLY (meta 0.10 minus apple 0.35;
  delta_calc string verbatim); p_value/cohens_d NOT_CALCULATED;
  is_significant False; apple arm +0.35 carried from #622 at identical
  value (no rescoring); verdict WITHIN-WRITER GENRE REGISTER (zero
  privacy-alarm vocabulary on the Meta arm, lone evaluative jab lands on
  Google Glass not Meta); NOT a falsification-family member (Guardian-Apple
  $0 / Guardian-Meta $0, zero-financial-gradient boundary as #622).
- #629 Type C (Anthropic $1.5B settlement distribution-phase payout fight,
  mechanism 612, competitor-entities.yaml anthropic entity): qualitative
  boundary; FIRST dedicated distribution-phase mechanism; tone_scores
  NOT_SCORED; NO asymmetry_scorer key in the block (scorer consistency
  explicitly does not apply); p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant False; falsification-family BOUNDARY member, NOT a pin
  (involuntary penalty-direction money flow predicts NO coverage
  softening, the opposite of the paid-licensing legs); $1,500 per-work
  publisher share is arithmetic from the 50-50 split, not a disclosed
  figure; Aug 10 2022 download-date cutoff; no_coverage_tone_claim true.

Artifact readiness: no analysis.json update warranted. The window is
monitoring + illustrative-only + qualitative mapping; no new empirical
finding at the publication level. Manual illustrative deltas stay
descriptive under the Aug 28 2026 standing rule (engine-side drift checks
only, finding layer refuses significance).
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
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")

THIS_FILE = "test_type_d_630_scorer_consistency_626_627_628_629_rotation_doc_sync_sep09_9am.py"

MECH_610_KEY = "mechanism_610_verge_amazon_ring_surveillance_vs_meta_mixed_register"
GIBBS_628_KEY = "type_b_628_samuel_gibbs_guardian_within_writer_genre_register"
MECH_612_KEY = "anthropic_settlement_distribution_phase_payout_fight_629"

TARGET_TONES_627 = [0.45, 0.2, -0.3]
PEER_TONES_627 = [-0.8, -0.6]
TARGET_AVG_627 = 0.1167
PEER_AVG_627 = -0.7
DELTA_627 = 0.8167

META_TONE_628 = 0.10
APPLE_TONE_628 = 0.35
DELTA_628 = -0.25

SETTLEMENT_PER_WORK = 3000
SETTLEMENT_PUBLISHER_SHARE = 1500


def _verge_610():
    with open(VERGE_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["competitor_relationships"]["amazon"][MECH_610_KEY]


def _gibbs():
    with open(JOURNALISTS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    gibbs = [j for j in data["journalists"] if j.get("name") == "Samuel Gibbs"]
    assert len(gibbs) == 1
    return gibbs[0]["competitor_coverage"][GIBBS_628_KEY]


def _anthropic_612():
    with open(ENTITIES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["entities"]["anthropic"][MECH_612_KEY]


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


class TestScorerConsistency627DeltaArithmetic:
    def test_mechanism_id_610(self):
        assert _verge_610()["mechanism_id"] == 610

    def test_iteration_627(self):
        assert _verge_610()["iteration"] == 627

    def test_target_avg_reproduces(self):
        avg = round(sum(TARGET_TONES_627) / len(TARGET_TONES_627), 4)
        assert avg == TARGET_AVG_627 == _verge_610()["asymmetry_scorer_manual_illustrative"]["target_avg_tone"]

    def test_peer_avg_reproduces(self):
        avg = round(sum(PEER_TONES_627) / len(PEER_TONES_627), 4)
        assert avg == PEER_AVG_627 == _verge_610()["asymmetry_scorer_manual_illustrative"]["peer_avg_tone"]

    def test_delta_reproduces_exactly(self):
        delta = round(TARGET_AVG_627 - PEER_AVG_627, 4)
        assert delta == DELTA_627 == _verge_610()["asymmetry_scorer_manual_illustrative"]["delta_manual_illustrative"]

    def test_log_rounding_plus_082(self):
        assert round(DELTA_627, 2) == 0.82

    def test_yaml_tones_match_pinned(self):
        scorer = _verge_610()["asymmetry_scorer_manual_illustrative"]
        assert scorer["target_tones"] == TARGET_TONES_627
        assert scorer["peer_tones"] == PEER_TONES_627

    def test_delta_direction_meta_minus_amazon(self):
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["delta_direction"] == "meta_minus_amazon"

    def test_n2_vs_n3_descriptive(self):
        note = _verge_610()["asymmetry_scorer_manual_illustrative"].get("synthetic_note", "")
        assert "n=2 vs n=3" in note


class TestScorerConsistency627StatisticalDiscipline:
    def test_p_value_not_calculated(self):
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci95_not_calculated(self):
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["confidence_interval_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["is_significant"] is False

    def test_manual_illustrative_only_research_method(self):
        text = open(VERGE_PATH, encoding="utf-8").read()
        idx = text.find(MECH_610_KEY)
        window = text[idx:idx + 14000]
        assert "MANUAL ILLUSTRATIVE" in window

    def test_financial_tie_none_amazon_entity(self):
        with open(VERGE_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        amazon = data["competitor_relationships"]["amazon"]
        tie = str(amazon.get("financial_tie", amazon.get("financial_ties", "")))
        assert tie and ("none" in tie.lower() or "$0" in tie or "0" in tie)

    def test_finding_names_zero_financial_gradient_control(self):
        assert "zero-financial-gradient" in _verge_610()["finding"].lower() or \
               "zero-financial-gradient" in _verge_610()["financial_triangulation"]["correlation_not_causation"].lower()

    def test_not_falsification_family_member(self):
        finding = _verge_610()["finding"]
        assert "NOT a falsification-family member" in finding

    def test_two_amazon_articles_pinned(self):
        arts = _verge_610()["amazon_articles"]
        assert len(arts) == 2
        assert arts[0]["manual_illustrative_tone"] == -0.8
        assert arts[1]["manual_illustrative_tone"] == -0.6

    def test_three_meta_articles_pinned(self):
        arts = _verge_610()["meta_articles_same_domain"]
        assert len(arts) == 3
        assert [a["manual_illustrative_tone"] for a in arts] == TARGET_TONES_627


class TestScorerConsistency628DeltaArithmetic:
    def test_mechanism_id_611(self):
        assert _gibbs()["mechanism_id"] == 611

    def test_iteration_628(self):
        assert _gibbs()["iteration"] == 628

    def test_delta_reproduces_exactly(self):
        scorer = _gibbs()["asymmetry_scorer"]
        assert scorer["meta_tone"] == META_TONE_628
        assert scorer["apple_tone"] == APPLE_TONE_628
        assert round(META_TONE_628 - APPLE_TONE_628, 2) == DELTA_628 == scorer["delta_meta_minus_apple"]

    def test_delta_calc_string_verbatim(self):
        assert _gibbs()["asymmetry_scorer"]["delta_calc"] == "0.10 - 0.35 = -0.25"

    def test_apple_tone_carried_from_622_identical(self):
        basis = _gibbs()["apple_arm"]["tone_basis"]
        assert "carried from #622" in basis
        assert _gibbs()["apple_arm"]["tone_score"] == 0.35

    def test_meta_arm_full_text_mirror(self):
        assert "full-text mirror" in _gibbs()["meta_arm"]["evidence_tier"]

    def test_yaml_tones_match_pinned(self):
        assert _gibbs()["meta_arm"]["tone_score"] == META_TONE_628
        assert _gibbs()["apple_arm"]["tone_score"] == APPLE_TONE_628


class TestScorerConsistency628StatisticalDiscipline:
    def test_p_value_not_calculated(self):
        assert _gibbs()["asymmetry_scorer"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _gibbs()["asymmetry_scorer"]["cohens_d"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _gibbs()["asymmetry_scorer"]["is_significant"] is False

    def test_method_manual_illustrative(self):
        assert "MANUAL ILLUSTRATIVE" in _gibbs()["asymmetry_scorer"]["method"]

    def test_verdict_within_writer_genre_register(self):
        assert "WITHIN-WRITER GENRE REGISTER" in _gibbs()["verdict"]

    def test_zero_privacy_alarm_vocabulary_meta_arm(self):
        notes = _gibbs()["meta_arm"]["register_notes"]
        assert "Zero privacy-alarm vocabulary" in notes

    def test_evaluative_jab_lands_on_google_glass(self):
        notes = _gibbs()["meta_arm"]["register_notes"]
        assert "Google Glass" in notes

    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _gibbs()["verdict"]

    def test_two_strong_genre_timing_confounders(self):
        confs = _gibbs()["confounders_ranked"]
        strong = [c for c in confs if c.get("strength") == "STRONG"]
        assert len(strong) == 2
        assert any("Genre" in c["text"] for c in strong)
        assert any("Timing" in c["text"] for c in strong)

    def test_no_zero_coverage_claims_both_arms_positive(self):
        assert _gibbs()["meta_arm"]["tone_score"] > 0
        assert _gibbs()["apple_arm"]["tone_score"] > 0

    def test_block_key_matches(self):
        assert _gibbs()["block_key"] == GIBBS_628_KEY


class TestQualitativeBoundary629:
    def test_mechanism_id_612(self):
        assert _anthropic_612()["mechanism_id"] == 612

    def test_iteration_629(self):
        assert _anthropic_612()["iteration"] == 629

    def test_tone_scores_not_scored(self):
        assert _anthropic_612()["tone_scores"] == "NOT_SCORED"

    def test_no_asymmetry_scorer_key(self):
        assert "asymmetry_scorer" not in _anthropic_612()

    def test_statistical_discipline_not_calculated(self):
        disc = _anthropic_612()["statistical_discipline"]
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc
        assert "is_significant False" in disc

    def test_falsification_family_boundary_not_pin(self):
        fam = _anthropic_612()["theory_prediction"]["falsification_family"]
        assert "Boundary member" in fam
        assert "not a new pin" in fam

    def test_penalty_direction_predicts_no_softening(self):
        pred = _anthropic_612()["theory_prediction"]["prediction"]
        assert "NO coverage softening" in pred

    def test_per_work_publisher_share_arithmetic(self):
        assert _anthropic_612()["distribution_mechanics"]["in_print_split"].startswith("50-50")
        assert SETTLEMENT_PER_WORK / 2 == SETTLEMENT_PUBLISHER_SHARE == 1500
        mapping = _anthropic_612()["financial_incentive_mapping"]["publisher_claim_value"]
        assert "circa $1,500" in mapping

    def test_download_date_cutoff_aug_10_2022(self):
        assert "August 10, 2022" in _anthropic_612()["distribution_mechanics"]["download_date_cutoff"]

    def test_three_claim_categories(self):
        assert len(_anthropic_612()["claim_categories"]) == 3

    def test_no_coverage_tone_claim(self):
        assert _anthropic_612()["no_coverage_tone_claim"] is True

    def test_cautious_language_required(self):
        assert _anthropic_612()["cautious_language_required"] is True

    def test_single_primary_source_url(self):
        srcs = _anthropic_612()["sources"]
        assert len(srcs) == 1
        assert "techcrunch.com/2026/09/06" in srcs[0]

    def test_first_dedicated_distribution_phase_mechanism(self):
        assert "First Dedicated Distribution-Phase Mechanism" in _anthropic_612()["mechanism_name"]
        assert "FIRST distribution-phase" in _anthropic_612()["novelty"]


class TestMonitoringBoundary626:
    def test_iteration_626_heading_in_podcast_sentiment(self):
        assert "## Iteration #626" in _podcast_text()

    def test_gf_499_holds_forty_eighth(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "499 HOLDS" in window
        assert "Forty-Eighth" in window

    def test_episode_500_watch_item_mon_sep_14(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "Mon Sep 14" in window

    def test_attention_sphere_48th_no_match(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "48th" in window and "no-match" in window.lower()

    def test_identity_strand_unchanged_from_596(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "#596" in window

    def test_ehe_30_day_hold(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "30-Day Hold Continues" in window

    def test_zero_new_to_corpus_press_surfaces(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "ZERO New-to-Corpus Press Surfaces" in window

    def test_recency_frontier_tied_sep_8(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "TIED at Sep 8" in window

    def test_thevermilion_new_url_predates_frontier_not_advance(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "thevermilion.com" in window
        assert "NOT a press-surface advance" in window

    def test_everyone_hates_elon_not_podcast_strand(self):
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "NOT a podcast" in window

    def test_no_iteration_626_mechanism_block_in_profiles(self):
        hits = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for fn in files:
                if not fn.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(root, fn)
                content = open(path, encoding="utf-8").read()
                for i, line in enumerate(content.splitlines(), 1):
                    if re.search(r"\biteration:\s*626\b", line):
                        hits.append(f"{path}:{i}")
        assert hits == [], f"unexpected iteration-626 mechanism blocks: {hits}"

    def test_test_type_e_626_file_exists(self):
        names = [f for f in os.listdir(TESTS_DIR) if f.startswith("test_type_e_626")]
        assert len(names) == 1


class TestCompetitorCoveragePatterns630:
    def test_zero_financial_gradient_control_pattern(self):
        # #627 joins #622 as a zero-gradient pair: $0 on both sides, so the
        # register gap must be event/genre-driven, bounding the theory.
        assert _verge_610()["asymmetry_scorer_manual_illustrative"]["peer_entities"] == ["amazon"]
        with open(VERGE_PATH, encoding="utf-8") as f:
            verge = yaml.safe_load(f)
        assert verge["competitor_relationships"]["amazon"].get("financial_tie") in (None, "none") or \
            "none" in str(verge["competitor_relationships"]["amazon"].get("financial_tie", "none")).lower()

    def test_within_writer_genre_register_pattern(self):
        # #628: the same writer's register tracks article genre (review vs
        # announcement), not entity; directionally opposite of an entity-bias read.
        assert _gibbs()["apple_arm"]["genre"] == "hands-on review"
        assert "announcement" in _gibbs()["meta_arm"]["genre"]
        assert DELTA_628 < 0  # illustrative meta-minus-apple is negative, genre explained

    def test_distribution_phase_boundary_pattern(self):
        # #629: penalty-direction money flow predicts NO softening, bounding
        # the falsification family without joining it.
        assert _anthropic_612()["theory_prediction"]["direction"].startswith("Adversarial and involuntary")
        assert "not softer" in _anthropic_612()["theory_prediction"]["prediction"]

    def test_podcast_monitoring_boundary_pattern(self):
        # #626: monitoring-only Type E extends no scorer and writes no
        # mechanism block; the discipline is consistency of the monitoring
        # cadence, not tone claims.
        text = _podcast_text()
        idx = text.find("## Iteration #626")
        window = text[idx:idx + 12000]
        assert "MANUAL ILLUSTRATIVE" in window
        assert "is_significant False" in window

    def test_mechanism_namespace_610_611_612_distinct_profiles(self):
        # 610: the-verge.yaml amazon entity; 611: journalists.yaml Gibbs;
        # 612: competitor-entities.yaml anthropic entity. Consecutive ids in
        # three distinct profiles in one window.
        assert _verge_610()["mechanism_id"] == 610
        assert _gibbs()["mechanism_id"] == 611
        assert _anthropic_612()["mechanism_id"] == 612

    def test_qualitative_vs_scorer_boundary_630(self):
        # #627/#628 carry MANUAL ILLUSTRATIVE scorer blocks; #629 deliberately
        # carries none. The window exercises both sides of the boundary.
        assert "asymmetry_scorer_manual_illustrative" in _verge_610()
        assert "asymmetry_scorer" in _gibbs()
        assert "asymmetry_scorer" not in _anthropic_612()
        assert "asymmetry_scorer_manual_illustrative" not in _anthropic_612()


class TestRotationCycleGuard630:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention. This class is
    # deselected pre-commit (it asserts the post-commit anchor) and runs
    # green in the followup.
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("D", 630),
        ("C", 629),
        ("B", 628),
        ("A", 627),
        ("E", 626),
    ]

    @staticmethod
    def _mains():
        return _git_main_subjects(TestRotationCycleGuard630.ANCHORED_COMMIT)

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


class TestDocSync630:
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
        for token in ("#626", "#627", "#628", "#629"):
            assert token in doc
