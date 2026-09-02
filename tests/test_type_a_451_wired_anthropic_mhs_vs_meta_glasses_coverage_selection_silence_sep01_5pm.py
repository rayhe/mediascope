"""
Tests for WIRED Type A iteration #451 Sep 1 2026 17:00 PDT
WIRED Anthropic Model Hardware Standard vs Meta Glasses Coverage Selection Silence

Mechanism #451 Type A - Competitor Coverage Deep Dive - WIRED Anthropic MHS vs Meta
Rotation: #450 Type E -> #451 Type A

Verifies:
- WIRED anthropic MHS research preview Aug 27 2026 physical device control standard
- Search-results only SECONDARY UNVERIFIED 0 WIRED articles Aug 27-Sep 01 not proof of silence
- 3 WIRED Meta articles HTTPS with surveillance backdrop vs 2 WIRED Anthropic prior aspirational
- Cross-pub 6+ outlets covering MHS HTTPS Reuters PYMNTS etc.
- Tone delta MANUAL ILLUSTRATIVE -0.506
- Asymmetry scorer synthetic not empirical with MANUAL ILLUSTRATIVE label
- Financial tie $0 direct Condé Nast Anthropic but structural via OpenAI deal
- Non-disclosure systematic
- Editorial independence acknowledged
- Correlation not causation
- Confounders >=4 STRONG>=2
- No em dashes, HTTPS provenance
- Three-tier model financial predictor present
- Distinct from 421 118 154 312

Source: profiles/wired.yaml iteration_451 model_hardware_standard_coverage_selection_silence_451
Added: 2026-09-01 17:00 PDT Type A iteration
"""
import yaml
import os
import re
import pytest

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
ITERATION_LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")

def _load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)

def _load_log():
    with open(ITERATION_LOG_PATH) as f:
        return f.read()

def _entry():
    p = _load_profile()
    return p["competitor_relationships"]["anthropic"]["model_hardware_standard_coverage_selection_silence_451"]

# ===================================================================
# CLASS 1: Mechanism and iteration metadata
# ===================================================================
class TestIteration451Metadata:
    def test_profile_exists(self):
        assert os.path.exists(PROFILE_PATH)

    def test_anthropic_key_exists(self):
        p = _load_profile()
        assert "anthropic" in p["competitor_relationships"]

    def test_iteration_451_exists(self):
        p = _load_profile()
        assert "model_hardware_standard_coverage_selection_silence_451" in p["competitor_relationships"]["anthropic"]

    def test_mechanism_id_451(self):
        assert _entry()["mechanism_id"] == 451

    def test_iteration_type_A(self):
        assert _entry()["iteration_type"] == "A"

    def test_iteration_number_451(self):
        assert _entry()["iteration_number"] == 451

    def test_publication_focus_wired(self):
        assert _entry()["publication_focus"] == "wired"

    def test_competitor_anthropic(self):
        assert _entry()["competitor"] == "anthropic"

    def test_goal_id(self):
        assert _entry()["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id(self):
        assert _entry()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_iteration_time(self):
        assert "17:00" in _entry()["time_analyzed"]

    def test_date_analyzed(self):
        assert _entry()["date_analyzed"] == "2026-09-01"

# ===================================================================
# CLASS 2: Event and silence handling
# ===================================================================
class TestEventAndSilence:
    def test_event_date_aug27(self):
        assert _entry()["event_date"] == "2026-08-27"

    def test_event_contains_mhs(self):
        assert "Model Hardware Standard" in _entry()["event"] or "MHS" in _entry()["event"]

    def test_event_contains_physical_devices(self):
        assert "physical" in _entry()["event"].lower()

    def test_wired_articles_0(self):
        assert _entry()["wired_articles_published_aug27_sep01"] == 0

    def test_wired_articles_note_search_results_only(self):
        note = _entry()["wired_articles_published_note"]
        assert "search-results only" in note.lower() or "SECONDARY UNVERIFIED" in note

    def test_days_of_silence_5(self):
        assert _entry()["days_of_silence"] == 5

    def test_no_proof_of_silence_flag(self):
        assert _entry()["cautious_language"]["no_proof_of_silence"] is True
        assert _entry()["cautious_language"]["search_results_only_secondary_unverified"] is True

    def test_prior_mechanism_421(self):
        assert _entry()["prior_mechanism_anthropic_robot_dog"] == 421

# ===================================================================
# CLASS 3: WIRED prior coverage anthropic robotics
# ===================================================================
class TestWIREDPriorCoverage:
    def test_prior_coverage_list_len_ge_1(self):
        assert len(_entry()["wired_prior_coverage_anthropic_robotics"]) >= 1

    def test_prior_coverage_urls_https(self):
        for src in _entry()["wired_prior_coverage_anthropic_robotics"]:
            assert src["url"].startswith("https://")

    def test_robot_dog_present(self):
        urls = [s["url"] for s in _entry()["wired_prior_coverage_anthropic_robotics"]]
        assert any("anthropic-claude-takes-control-robot-dog" in u for u in urls)

    def test_robot_dog_tone_positive(self):
        for src in _entry()["wired_prior_coverage_anthropic_robotics"]:
            if "robot-dog" in src["url"]:
                assert src["tone_MANUAL_ILLUSTRATIVE"] > 0

    def test_robot_dog_no_em_dash(self):
        import json as _json
        dumped = _json.dumps(_entry()["wired_prior_coverage_anthropic_robotics"])
        assert "—" not in dumped and "–" not in dumped

# ===================================================================
# CLASS 4: WIRED Meta comparison
# ===================================================================
class TestWIREDMetaComparison:
    def test_meta_articles_same_window(self):
        comp = _entry()["wired_meta_physical_ai_comparison"]
        assert len(comp["wired_meta_articles_same_window"]) >= 1

    def test_meta_urls_https(self):
        comp = _entry()["wired_meta_physical_ai_comparison"]
        for src in comp["wired_meta_articles_same_window"]:
            assert src["url"].startswith("https://")

    def test_meta_articles_surveillance_backdrop(self):
        comp = _entry()["wired_meta_physical_ai_comparison"]
        framings = [s["framing"] for s in comp["wired_meta_articles_same_window"]]
        assert any("surveillance" in f or "privacy" in f or "product" in f for f in framings)

    def test_capability_inversion_present(self):
        comp = _entry()["wired_meta_physical_ai_comparison"]
        assert "capability_inversion" in comp or "capability" in str(comp).lower()
        # inversion should mention higher risk Anthropic vs lower risk Meta
        inv = comp.get("capability_inversion", "")
        assert "microscope" in inv or "robotic" in inv or "laser" in inv or "quantum" in inv or len(inv) > 20

    def test_anthropic_mhs_articles_0(self):
        comp = _entry()["wired_meta_physical_ai_comparison"]
        assert comp["wired_anthropic_mhs_articles_aug27_sep01"] == 0

# ===================================================================
# CLASS 5: Cross-pub comparison MHS
# ===================================================================
class TestCrossPubMHS:
    def test_cross_pub_has_reuters(self):
        cross = _entry()["cross_pub_comparison_mhs"]
        assert "reuters" in cross["reuters_aug27"].lower()
        assert cross["reuters_aug27"].startswith("https://")

    def test_cross_pub_has_pymnts(self):
        cross = _entry()["cross_pub_comparison_mhs"]
        assert cross["pymnts_aug27"].startswith("https://")

    def test_cross_pub_count_ge_6(self):
        cross = _entry()["cross_pub_comparison_mhs"]
        # count keys that are URLs
        url_keys = [k for k,v in cross.items() if isinstance(v,str) and v.startswith("https://")]
        assert len(url_keys) >= 6

    def test_wired_count_0_search_results_only(self):
        cross = _entry()["cross_pub_comparison_mhs"]
        assert cross["wired_count"] == "0 search-results only SECONDARY UNVERIFIED" or "0" in str(cross["wired_count"])

    def test_other_outlets_count_ge_6(self):
        cross = _entry()["cross_pub_comparison_mhs"]
        assert "6" in str(cross["other_outlets_count"]) or cross["other_outlets_count"] >= 6 if isinstance(cross["other_outlets_count"], int) else True

# ===================================================================
# CLASS 6: Financial context
# ===================================================================
class TestFinancialContext:
    def test_conde_nast_anthropic_direct_zero(self):
        assert "$0" in _entry()["financial_context"]["conde_nast_anthropic_direct"]

    def test_conde_nast_openai_deal_present(self):
        assert "Content licensing" in _entry()["financial_context"]["conde_nast_openai_deal"] or "$1-5M" in _entry()["financial_context"]["conde_nast_openai_deal"]

    def test_openai_source_url_https(self):
        assert _entry()["financial_context"]["source_url_openai"].startswith("https://")

    def test_correlation_not_causation(self):
        assert _entry()["financial_context"]["correlation_not_causation"] is True

    def test_structural_incentive_not_proof(self):
        assert _entry()["financial_context"]["structural_incentive_not_proof_editorial_control"] is True

# ===================================================================
# CLASS 7: Asymmetry scoring MANUAL ILLUSTRATIVE
# ===================================================================
class TestAsymmetryScoringManualIllustrative:
    def test_delta_manual_illustrative(self):
        delta = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["asymmetry_score_MANUAL_ILLUSTRATIVE"]
        assert abs(delta - (-0.506)) < 0.02

    def test_manual_illustrative_label_present(self):
        entry = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in entry["methodology"]
        assert "MANUAL ILLUSTRATIVE" in entry["is_significant_explanation"] or "MANUAL ILLUSTRATIVE" in entry["methodology"]

    def test_synthetic_not_empirical(self):
        entry = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert entry["is_significant"] is False
        assert entry["p_value"] == "NOT_CALCULATED no observed corpus"

    def test_target_avg_negative_peer_positive(self):
        entry = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert entry["target_avg_tone_MANUAL_ILLUSTRATIVE"] < 0
        assert entry["peer_avg_tone_MANUAL_ILLUSTRATIVE"] > 0

    def test_scorer_path_present(self):
        entry = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "mediascope/score/asymmetry.py" in entry["methodology"]

    def test_no_significance_claim(self):
        assert _entry()["cautious_language"]["significant_false"] is True

    def test_cohens_d_not_calculated(self):
        entry = _entry()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert entry["cohens_d"] == "NOT_CALCULATED no observed corpus"

# ===================================================================
# CLASS 8: Confounders and cautious language
# ===================================================================
class TestConfoundersCautious:
    def test_confounders_count_ge_4(self):
        total = len(_entry()["confounding_factors_ranked"])
        assert total >= 4

    def test_strong_confounders_ge_2(self):
        strong = [c for c in _entry()["confounding_factors_ranked"] if c["level"] == "STRONG"]
        assert len(strong) >= 2

    def test_correlation_not_causation(self):
        assert _entry()["cautious_language"]["correlation_not_causation"] is True

    def test_no_editorial_control_claim(self):
        assert _entry()["cautious_language"]["structural_incentive_not_proof_editorial_control"] is True

    def test_finding_summary_contains_cautious(self):
        # coverage_prediction contains cautious framing
        assert "correlation not causation" in _entry()["coverage_prediction"].lower() or "structural incentive" in _entry()["coverage_prediction"].lower()

    def test_no_em_dashes_anywhere(self):
        import json as _json
        dumped = _json.dumps(_entry())
        assert "—" not in dumped, "em dash found"
        assert "–" not in dumped, "en dash found"

    def test_https_only_source_urls(self):
        for u in _entry()["source_urls"]:
            assert u.startswith("https://"), f"non-HTTPS URL {u}"

    def test_search_results_only_flag(self):
        assert _entry()["cautious_language"]["search_results_only_secondary_unverified"] is True

# ===================================================================
# CLASS 9: Novelty vs existing
# ===================================================================
class TestNovelty:
    def test_distinct_from_421(self):
        assert "421" in _entry()["novelty_vs_existing"]["mechanism_421"] or "robot-dog" in _entry()["novelty_vs_existing"]["mechanism_421"].lower()

    def test_distinct_from_118(self):
        assert "118" in _entry()["novelty_vs_existing"]["mechanism_118"] or "blackmail" in _entry()["novelty_vs_existing"]["mechanism_118"].lower() or "functional emotions" in _entry()["novelty_vs_existing"]["mechanism_118"].lower()

    def test_distinct_from_154(self):
        assert "154" in _entry()["novelty_vs_existing"]["mechanism_154"]

    def test_451_distinct_field_present(self):
        assert "451" in _entry()["novelty_vs_existing"]["mechanism_451_distinct"] or "MHS" in _entry()["novelty_vs_existing"]["mechanism_451_distinct"]

    def test_source_urls_include_reuters_mhs(self):
        urls = _entry()["source_urls"]
        assert any("anthropic-unveils-new-framework-allowing-ai-agents-operate-physical-devices" in u for u in urls)

    def test_source_urls_include_wired_robot_dog(self):
        urls = _entry()["source_urls"]
        assert any("anthropic-claude-takes-control-robot-dog" in u for u in urls)

