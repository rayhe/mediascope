"""
Test FT OpenAI Rogue Agents vs Meta Rogue Models Framing Asymmetry - Iteration #394 Type A
2026-08-30 10:00 PT

Validates mechanism_id 394 exists, source provenance, scoring, and cautious language.
"""
import os
import yaml
import pytest

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "..", "profiles", "financial-times.yaml")

def load_profile():
    with open(PROFILE_PATH, 'r') as f:
        return yaml.safe_load(f)

def test_mechanism_394_exists():
    profile = load_profile()
    ceca = profile.get("cross_entity_coverage_analysis", {})
    key = "iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"
    assert key in ceca, f"Missing {key} in cross_entity_coverage_analysis"
    mech = ceca[key]
    assert mech["mechanism_id"] == 394
    assert mech["type"] == "Type A: Competitor Coverage Deep Dive"
    assert "rogue" in mech["mechanism_name"].lower()

def test_source_provenance():
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    # Must have primary Reuters deal source
    assert "reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29" in str(mech["financial_relationship"]["primary_source"])
    # Must have at least 2 openai + 2 meta articles
    assert len(mech["openai_rogue_coverage_2026"]) >= 2
    assert len(mech["meta_rogue_comparators_2026"]) >= 2
    # Must have both rogue articles
    urls = str(mech["source_urls"])
    assert "openai-says-state-linked-hackers-are-using-its-models-for-cyberattacks" in urls
    assert "meta-ai-models-exploited-to-steal-police-gov-data-researchers" in urls
    # No invented FT URLs - must not claim ft.com primary where secondary used
    assert mech["openai_rogue_coverage_2026"][0]["url"].startswith("https://www.pymnts.com/")

def test_coding_fields_present():
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    # Required scoring fields
    assert "asymmetry_scorer_result" in mech
    scorer = mech["asymmetry_scorer_result"]
    assert scorer["target_entity"] == "Meta"
    assert "OpenAI" in scorer["peer_entities"]
    assert "target_avg_tone" in scorer
    assert "peer_avg_tone" in scorer
    assert "p_value" in scorer
    assert "cohens_d" in scorer
    # Confounders must be present
    assert len(mech["confounding_factors"]) >= 3
    # Cross refs must include 353 and 354
    refs = [r["mechanism_id"] for r in mech["cross_references"]]
    assert 353 in refs
    assert 354 in refs

def test_cautious_language_requirements():
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    # Non-causal language must be present
    nc = mech["financial_relationship"]["non_causal_language"]
    assert "does not prove" in nc or "Correlation does not establish causation" in nc
    # Synthetic note must warn illustrative not empirical
    synth = mech["asymmetry_scorer_result"]["synthetic_note"]
    assert "Illustrative" in synth or "illustrative" in synth
    assert "not empirical proof" in synth or "requires" in synth.lower()
    # Finding summary must not claim proof of editorial control
    summary = mech["finding_summary"].lower()
    assert "proves editorial control" not in summary
    assert "proves" not in summary or "predicts" in summary

def test_scorer_output_matches_computed():
    """Verify scorer math: target_avg -0.4733, peer_avg 0.0717, delta -0.545, p 0.0039, d -4.47"""
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    scorer = mech["asymmetry_scorer_result"]
    # Allow small floating tolerance
    assert abs(scorer["target_avg_tone"] - (-0.4733)) < 0.01
    assert abs(scorer["peer_avg_tone"] - 0.0717) < 0.01
    assert abs(scorer["asymmetry_score"] - (-0.545)) < 0.02
    assert scorer["p_value"] < 0.01
    assert scorer["is_significant"] == True
    assert abs(scorer["cohens_d"] - (-4.4695)) < 0.2

def test_no_em_dashes_in_prose():
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    # August 28 2026 rule: avoid em dashes in repo prose
    for field in ["finding_summary", "mechanism_name", "focus"]:
        text = str(mech.get(field, ""))
        assert "—" not in text, f"Em dash found in {field}: {text[:100]}"

def test_financial_relationship_undisclosed():
    profile = load_profile()
    mech = profile["cross_entity_coverage_analysis"]["iteration_394_type_a_rogue_agents_asymmetry_2026_08_30"]
    fin = mech["financial_relationship"]
    assert fin["cash_terms_disclosed"] == False
    assert fin["valuation_source_type"] == "secondary_report_based"
    assert fin["meta_estimated_value"] == "$0"
    assert fin["deal_disclosed_in_ft_coverage"] == False
