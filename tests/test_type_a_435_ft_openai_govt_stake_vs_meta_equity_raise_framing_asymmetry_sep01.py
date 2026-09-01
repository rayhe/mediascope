"""
Tests for Financial Times Type A iteration #435 Sep 1 2026 01:00 PDT
FT OpenAI Government Stake Benefit-Sharing vs Meta Equity Raise Desperation Framing Asymmetry

Mechanism #435 Type A - Competitor Coverage Deep Dive - Financial Times OpenAI vs Meta

Verifies:
- Financial relationship documentation $5-10M/yr licensing vs $0
- 3 FT OpenAI articles HTTPS with constructive framing
- 3 FT Meta articles HTTPS surveillance/desperation framing
- Tone delta MANUAL ILLUSTRATIVE -0.7033
- Asymmetry scorer synthetic not empirical
- Non-disclosure systematic
- Editorial independence acknowledged
- Correlation not causation
- Confounders >=4 STRONG>=2
- No em dashes, HTTPS provenance

Source: profiles/financial-times.yaml iteration_435
Added: 2026-09-01 01:00 PDT Type A iteration
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
class TestIteration435Metadata:
    def test_profile_exists(self):
        assert os.path.exists(PROFILE_PATH)

    def test_iteration_435_exists(self):
        p = _load_profile()
        assert "iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry" in p["competitor_relationships"]["openai"]

    def test_mechanism_id_435(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["mechanism"] == 435

    def test_iteration_type_A(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["iteration_type"] == "A"

    def test_publication_focus_financial_times(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["publication"] == "Financial Times"

    def test_competitor_pair_openai_vs_meta(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert "OpenAI" in entry["competitor_pair"] and "Meta" in entry["competitor_pair"]

    def test_goal_id(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["scheduled_job_id"] == "mediascope-daily-iteration"

# ===================================================================
# CLASS 2: Financial relationship
# ===================================================================
class TestFinancialRelationship:
    def test_openai_financial_tie_licensing(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["partner"] == "OpenAI"
        assert entry["financial_relationship"]["deal_type"] == "licensing"
        assert "$5-10M" in entry["financial_relationship"]["estimated_value"]

    def test_meta_zero(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["meta_estimated_value"] == "$0"

    def test_primary_source_https(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["primary_source"].startswith("https://")
        assert "financial-times-openai-sign-content-licensing" in entry["financial_relationship"]["primary_source"]

    def test_deal_disclosed_false(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["financial_relationship"]["deal_disclosed_in_ft_coverage"] is False

    def test_non_causal_language(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert "Correlation does not establish causation" in entry["financial_relationship"]["non_causal_language"]

# ===================================================================
# CLASS 3: FT OpenAI sources
# ===================================================================
class TestFTOpenAISources:
    def test_three_openai_articles(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert len(entry["ft_openai_sources_sep01_2026"]) == 3

    def test_openai_urls_https(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for art in entry["ft_openai_sources_sep01_2026"]:
            assert art["url"].startswith("https://")
            assert " " not in art["url"]

    def test_openai_govt_stake_article(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        titles = [a["title"] for a in entry["ft_openai_sources_sep01_2026"]]
        assert any("5 percent" in t or "5% " in t or "Trump" in t for t in titles)

    def test_openai_framing_constructive(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        framings = [a["framing"] for a in entry["ft_openai_sources_sep01_2026"]]
        assert any("constructive" in f for f in framings)

    def test_openai_tone_manual_illustrative_range(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for art in entry["ft_openai_sources_sep01_2026"]:
            assert -0.2 <= art["tone_manual_illustrative"] <= 0.3

# ===================================================================
# CLASS 4: FT Meta sources
# ===================================================================
class TestFTMetaSources:
    def test_three_meta_articles(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert len(entry["ft_meta_sources_sep01_2026"]) == 3

    def test_meta_urls_https(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for art in entry["ft_meta_sources_sep01_2026"]:
            assert art["url"].startswith("https://")

    def test_meta_equity_raise_present(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        titles = [a["title"].lower() for a in entry["ft_meta_sources_sep01_2026"]]
        assert any("equity raising" in t or "equity" in t for t in titles)

    def test_meta_framing_adversarial_or_desperation(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        framings = [a["framing"] for a in entry["ft_meta_sources_sep01_2026"]]
        assert any("desperation" in f or "adversarial" in f or "surveillance" in f for f in framings)

    def test_meta_tone_negative(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for art in entry["ft_meta_sources_sep01_2026"]:
            assert art["tone_manual_illustrative"] < 0

# ===================================================================
# CLASS 5: Asymmetry scoring and cautious language
# ===================================================================
class TestAsymmetryScoringAndCautious:
    def test_delta_manual_illustrative(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["asymmetry_scoring_manual_illustrative"]["delta_manual_illustrative"] == -0.7033

    def test_manual_illustrative_note(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert "MANUAL ILLUSTRATIVE" in entry["asymmetry_scoring_manual_illustrative"]["note"]

    def test_synthetic_not_empirical(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["asymmetry_scoring_manual_illustrative"]["significant"] is False
        assert entry["asymmetry_scoring_manual_illustrative"]["empirical_required"] is True

    def test_cautious_language_correlation_not_causation(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["correlation_not_causation"] is True

    def test_no_editorial_control_claim(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["no_editorial_control_claim"] is True

    def test_no_statistical_significance_claim(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["no_statistical_significance_claim"] is True

    def test_p_value_not_calculated(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        assert entry["cautious_language"]["p_value_not_calculated"] is True

    def test_source_urls_https_no_spaces(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for url in entry["source_urls"]:
            assert url.startswith("https://")
            assert " " not in url
            assert url == url.strip()

    def test_no_em_dashes(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        # Check overview fields for em dash character
        text_to_check = str(entry)
        assert "—" not in text_to_check

    def test_iteration_log_contains_435(self):
        log = _load_log()
        assert "#435 Type A" in log
        assert "FT OpenAI Government Stake" in log or "FT OpenAI" in log

    def test_confounder_count(self):
        p = _load_profile()
        entry = p["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        conf = entry["confounders"]
        # At least 2 strong, total >=4
        assert len(conf["strong"]) >= 2
        total = len(conf.get("strong", [])) + len(conf.get("moderate", [])) + len(conf.get("weak", []))
        assert total >= 4

    def test_asymmetry_scorer_result_in_log(self):
        log = _load_log()
        assert "MANUAL ILLUSTRATIVE" in log
        assert "-0.7033" in log or "-0.5833" in log
