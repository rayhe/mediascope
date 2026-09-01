"""
Tests for Financial Times Type A iteration #441 Sep 1 2026 07:00 PDT
FT Anthropic Fundraising Aspirational vs Meta Equity Raise Desperation Framing Asymmetry

Mechanism #441 Type A - Competitor Coverage Deep Dive - Financial Times Anthropic vs Meta
Rotation: #439 Type E -> #441 Type A

Verifies:
- Indirect financial relationship via FT-Google commercial partnership plus Google up to $40B Anthropic investment vs $0 Meta
- 3 FT Anthropic articles HTTPS with aspirational fundraising framing
- 3 FT Meta articles HTTPS with desperation surveillance framing
- Tone delta MANUAL ILLUSTRATIVE -0.7666
- Asymmetry scorer synthetic not empirical with MANUAL ILLUSTRATIVE label
- Non-disclosure systematic FT Google partnership and Google Anthropic investment not disclosed
- Editorial independence acknowledged
- Correlation not causation indirect channel
- Confounders >=4 STRONG>=2
- No em dashes, HTTPS provenance
- Three-tier model financial predictor present

Source: profiles/financial-times.yaml iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry
Added: 2026-09-01 07:00 PDT Type A iteration
"""
import yaml
import os
import re
import pytest

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "..", "profiles", "financial-times.yaml")
ITERATION_LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")

def _load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)

def _load_log():
    with open(ITERATION_LOG_PATH) as f:
        return f.read()

# ===================================================================
# CLASS 1: Mechanism and iteration metadata
# ===================================================================
class TestIteration441Metadata:
    def test_profile_exists(self):
        assert os.path.exists(PROFILE_PATH)

    def test_anthropic_key_exists(self):
        p = _load_profile()
        assert "anthropic" in p["competitor_relationships"]

    def test_iteration_441_exists(self):
        p = _load_profile()
        assert "iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry" in p["competitor_relationships"]["anthropic"]

    def test_mechanism_id_441(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["mechanism"] == 441

    def test_iteration_type_A(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["iteration_type"] == "A"

    def test_publication_focus_financial_times(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["publication"] == "Financial Times"

    def test_competitor_pair_anthropic_vs_meta(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "Anthropic" in entry["competitor_pair"] and "Meta" in entry["competitor_pair"]

    def test_goal_id(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_iteration_time(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "07:00" in entry["iteration_time"]

# ===================================================================
# CLASS 2: Financial relationship indirect via Google
# ===================================================================
class TestFinancialRelationshipIndirect:
    def test_anthropic_direct_zero(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "$0" in entry["financial_relationship"]["anthropic_direct"]

    def test_ft_google_partnership_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "Single figure millions" in entry["financial_relationship"]["ft_google_partnership"]

    def test_google_anthropic_investment_up_to_40b(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "$40B" in entry["financial_relationship"]["google_anthropic_investment"] or "40B" in entry["financial_relationship"]["google_anthropic_investment"]

    def test_amazon_anthropic_investment_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "25B" in entry["financial_relationship"]["amazon_anthropic_investment"]

    def test_meta_zero(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["meta_estimated_value"] == "$0"

    def test_primary_source_https_reuters_ft(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        # At least one source_urls contains Reuters FT attribution
        assert any(u.startswith("https://") for u in entry["source_urls"])
        assert "reuters.com/technology/anthropic-weighs-fundraising-near-1-trillion-valuation-ft-reports" in entry["source_urls"][2]

    def test_deal_disclosed_false(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["deal_disclosed_in_ft_coverage"] is False

    def test_non_causal_language_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "Correlation does not establish causation" in entry["financial_relationship"]["non_causal_language"]

    def test_editorial_independence_note(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "editorial" in entry["financial_relationship"]["editorial_independence_note"].lower()

# ===================================================================
# CLASS 3: FT Anthropic sources aspirational
# ===================================================================
class TestFTAnthropicSources:
    def test_three_anthropic_articles(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert len(entry["ft_anthropic_sources_sep01_2026"]) == 3

    def test_anthropic_urls_https(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        for src in entry["ft_anthropic_sources_sep01_2026"]:
            assert src["url"].startswith("https://")

    def test_anthropic_framing_aspirational(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        framings = [s["framing"] for s in entry["ft_anthropic_sources_sep01_2026"]]
        assert any("aspirational" in f or "constructive" in f or "growth" in f for f in framings)

    def test_anthropic_tone_manual_illustrative_positive(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        for src in entry["ft_anthropic_sources_sep01_2026"]:
            assert src["tone_manual_illustrative"] > 0

    def test_anthropic_first_source_trillion_valuation(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        first = entry["ft_anthropic_sources_sep01_2026"][0]
        assert "trillion" in first["title"].lower() or "trillion" in " ".join(first["language"]).lower()

    def test_anthropic_no_em_dash(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        import json as _json
        dumped = _json.dumps(entry)
        assert "—" not in dumped and "–" not in dumped

# ===================================================================
# CLASS 4: FT Meta sources adversarial desperation
# ===================================================================
class TestFTMetaSources:
    def test_three_meta_articles(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert len(entry["ft_meta_sources_sep01_2026"]) == 3

    def test_meta_urls_https(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        for src in entry["ft_meta_sources_sep01_2026"]:
            assert src["url"].startswith("https://")

    def test_meta_framing_desperation_or_surveillance(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        framings = [s["framing"] for s in entry["ft_meta_sources_sep01_2026"]]
        assert any("desperation" in f or "surveillance" in f or "adversarial" in f for f in framings)

    def test_meta_tone_manual_illustrative_negative(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        for src in entry["ft_meta_sources_sep01_2026"]:
            assert src["tone_manual_illustrative"] < 0

    def test_meta_equity_raise_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "equity raising" in entry["ft_meta_sources_sep01_2026"][0]["title"].lower() or "equity" in entry["ft_meta_sources_sep01_2026"][0]["framing"]

# ===================================================================
# CLASS 5: Asymmetry scoring MANUAL ILLUSTRATIVE
# ===================================================================
class TestAsymmetryScoringManualIllustrative:
    def test_delta_manual_illustrative(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        delta = entry["asymmetry_scoring_manual_illustrative"]["delta_manual_illustrative"]
        assert abs(delta - (-0.7666)) < 0.01

    def test_manual_illustrative_label_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "MANUAL ILLUSTRATIVE" in entry["asymmetry_scoring_manual_illustrative"]["note"]
        assert "MANUAL ILLUSTRATIVE" in entry["asymmetry_scoring_manual_illustrative"]["synthetic_note"]

    def test_synthetic_not_empirical(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["asymmetry_scoring_manual_illustrative"]["significant"] is False
        assert entry["asymmetry_scoring_manual_illustrative"]["p_value"] == "NOT CALCULATED no observed corpus"

    def test_target_avg_negative_peer_positive(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["asymmetry_scoring_manual_illustrative"]["target_avg_manual_illustrative"] < 0
        assert entry["asymmetry_scoring_manual_illustrative"]["peer_avg_manual_illustrative"] > 0

    def test_scorer_path_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "mediascope/score/asymmetry.py" in entry["asymmetry_scoring_manual_illustrative"]["scorer"]

    def test_no_significance_claim(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["significant_false"] is True

# ===================================================================
# CLASS 6: Confounders and cautious language
# ===================================================================
class TestConfoundersCautious:
    def test_confounders_count_ge_4(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        total = len(entry["confounders"]["strong"]) + len(entry["confounders"]["moderate"]) + len(entry["confounders"]["weak"])
        assert total >= 4

    def test_strong_confounders_ge_2(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert len(entry["confounders"]["strong"]) >= 2

    def test_correlation_not_causation(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["correlation_not_causation"] is True

    def test_no_editorial_control_claim(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["no_editorial_control_claim"] is True

    def test_finding_summary_contains_cautious(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        assert "Does not prove editorial causation" in entry["finding_summary"]

    def test_no_em_dashes_anywhere(self):
        p = _load_profile()
        import json as _json
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        dumped = _json.dumps(entry)
        assert "—" not in dumped, "em dash found"
        assert "–" not in dumped, "en dash found"

    def test_https_only_source_urls(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        for u in entry["source_urls"]:
            assert u.startswith("https://"), f"non-HTTPS URL {u}"

    def test_three_tier_model_predictor(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["anthropic"]["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]
        # financial predictor present via indirect channel is part of three-tier framing model
        assert "Single figure millions" in entry["financial_relationship"]["ft_google_partnership"] or "40B" in entry["financial_relationship"]["google_anthropic_investment"]
