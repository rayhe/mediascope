"""
Test: FT OpenAI Govt Stake & Funding vs Meta Equity Raise Framing Asymmetry (Mechanism #356)
Type A: Competitor Coverage Deep Dive — FT covering OpenAI vs Meta capital formation
Date: 2026-08-28 08:00 PT (Iteration #344)
"""
import pytest
import os
import yaml
from datetime import datetime
from mediascope.score.asymmetry import calculate_asymmetry


PROFILE_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")


def load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def test_mechanism_356_metadata():
    """Mechanism 356 exists and has required fields."""
    data = load_profile()
    assert "cross_entity_coverage_analysis" in data
    ceca = data["cross_entity_coverage_analysis"]
    assert "openai_funding_govt_stake_vs_meta_equity_framing_asymmetry" in ceca
    mech = ceca["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    assert mech["mechanism_id"] == 356
    assert mech["date_analyzed"] == "2026-08-28"
    assert "finding" in mech
    assert "openai_coverage_2026" in mech
    assert "meta_coverage_comparator_2026" in mech
    assert "asymmetry_scorer_result" in mech
    assert mech["asymmetry_scorer_result"]["target_entity"] == "Meta"


def test_openai_coverage_4_articles_constructive():
    """FT OpenAI coverage has 4 articles with constructive/neutral framing and URLs."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    openai = mech["openai_coverage_2026"]
    assert len(openai) >= 4
    # Each must have URL and framing
    for article in openai:
        assert "url" in article and article["url"].startswith("https://")
        assert "framing" in article
        assert article["framing"] in ["neutral_growth_with_mild_skepticism", "growth_milestone", "constructive_enterprise_growth", "constructive_political_strategy"]
        assert article["deal_disclosed"] is False
    # Check specific articles present
    urls = [a["url"] for a in openai]
    assert any("100-billion-dollar-funding-round" in u for u in urls)
    assert any("34-billion" in u or "34-billion-last-year" in u for u in urls)
    assert any("superapp-overhaul" in u for u in urls)
    assert any("5-share-in-company" in u or "government-5" in u for u in urls)


def test_meta_coverage_comparator_desperation():
    """Meta comparator coverage has desperation framing and stock impact."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    meta = mech["meta_coverage_comparator_2026"]
    assert len(meta) >= 2
    first = meta[0]
    assert first["framing"] == "desperation_uncertainty"
    assert any("creative ways to raise cash" in lang for lang in first["language"])
    assert first["stock_impact"] == "-6.6% on FT report (Morningstar)" or "-6.6%" in str(first.get("stock_impact",""))
    assert "https://www.reuters.com/technology/meta-weighs-big-equity-raising" in first["url"]


def test_competitor_relationships_openai_enriched():
    """competitor_relationships.openai has recent_coverage_examples with 4 articles and source URLs."""
    data = load_profile()
    rels = data["competitor_relationships"]
    assert "openai" in rels
    assert rels["openai"]["financial_tie"] == "licensing"
    assert rels["openai"]["coverage_prediction"] == "softer"
    assert "recent_coverage_examples_2026_h1_h2" in rels["openai"]
    examples = rels["openai"]["recent_coverage_examples_2026_h1_h2"]
    assert len(examples) >= 4
    for ex in examples:
        assert "url" in ex and ex["url"].startswith("https://")
        assert "framing" in ex
        assert ex["deal_disclosed"] is False
    # Verify source_url for deal still present
    assert "2024-04-29" in rels["openai"]["source_url"]


def test_asymmetry_scorer_funding_govt_stake():
    """Asymmetry scorer produces significant result for funding/govt stake vs equity raise."""
    target_scores = [-0.55, -0.48, -0.62, -0.51]
    peer_scores = [0.05, 0.08, 0.18, 0.12, 0.15, 0.22, 0.08]
    result = calculate_asymmetry(
        target_scores=target_scores,
        peer_scores=peer_scores,
        target_entity="Meta",
        peer_entities=["OpenAI"],
        publication_slug="financial-times",
        period_start=datetime(2026, 1, 28),
        period_end=datetime(2026, 7, 2),
    )
    assert result.asymmetry_score < -0.5  # Meta more negative than OpenAI
    assert result.p_value < 0.05
    assert abs(result.cohens_d) > 0.8  # huge effect
    assert result.is_significant is True
    assert result.confidence_interval_lower < 0 and result.confidence_interval_upper < 0
    assert result.target_avg_tone < 0
    assert result.peer_avg_tone > 0


def test_ft_openai_deal_nondisclosure_systematic():
    """FT systematic non-disclosure across 4 funding/stake/spending articles."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    comparison = mech["comparison"]
    assert comparison["undisclosed_conflict"] is not None
    assert "4 funding/stake/spending articles" in comparison["undisclosed_conflict"] or "4" in comparison["undisclosed_conflict"]
    assert comparison["financial_relationship_predicts_coverage"] is True
    assert mech["openai_coverage_2026"][0]["deal_disclosed"] is False
    assert mech["openai_coverage_2026"][1]["deal_disclosed"] is False
    assert mech["openai_coverage_2026"][2]["deal_disclosed"] is False
    assert mech["openai_coverage_2026"][3]["deal_disclosed"] is False


def test_cross_references_mechanism_356():
    """Mechanism 356 cross-references prior mechanisms."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    assert "cross_references" in mech
    refs = [r["mechanism_id"] for r in mech["cross_references"]]
    assert 54 in refs  # capital-raise framing asymmetry
    assert 353 in refs  # superapp vs super-sensing
    assert 10 in refs  # partner validation


def test_confounders_adjusted_score():
    """Confounders documented and adjusted score is moderate."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    assert "confounding_factors" in mech
    assert len(mech["confounding_factors"]) >= 4
    # Adjusted score should be less than raw but still meaningful
    assert mech["raw_asymmetry_score"] > mech["adjusted_asymmetry_score"]
    assert mech["adjusted_asymmetry_score"] > 0.2  # moderate
    assert mech["adjusted_asymmetry_score"] < 0.6


def test_source_urls_all_present():
    """All source URLs are present and valid HTTPS."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    assert "source_urls" in mech
    urls = mech["source_urls"]
    assert len(urls) >= 6
    for url in urls:
        assert url.startswith("https://")
    # Must include deal source
    assert any("financial-times-openai-sign-content-licensing" in u for u in urls)
    # Must include FT originals via Reuters/PYMNTS
    assert any("pymnts.com" in u for u in urls)
    assert any("reuters.com" in u for u in urls)


def test_asymmetry_scorer_result_documented():
    """Asymmetry scorer result has statistically meaningful fields."""
    data = load_profile()
    mech = data["cross_entity_coverage_analysis"]["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry"]
    result = mech["asymmetry_scorer_result"]
    assert result["p_value"] < 0.001
    assert abs(result["cohens_d"]) > 2.0
    assert result["is_significant"] is True
    assert result["ci_excludes_zero"] is True
    assert "synthetic_note" in result
    assert "Real validation requires" in result["synthetic_note"]
