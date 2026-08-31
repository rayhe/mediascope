"""
Type A #415: FT OpenAI growth vs Meta capital/privacy asymmetry - Aug 31 2026
Financial Times $5-10M/yr OpenAI licensing (Apr 29 2024, Reuters primary terms undisclosed, WSJ via Digiday secondary) vs $0 Meta
compares Aug 25-27 OpenAI constructive/collective-action/neutral-technical framing vs Jun-Jul Meta cautionary surveillance/desperation framing.

Validates:
- Mechanism 415 exists in financial-times.yaml
- Primary Reuters deal source terms undisclosed, cash_terms_disclosed false, valuation secondary_report_based
- At least 3 OpenAI + 3 Meta articles with URLs exact
- No FT.com invented URLs where secondary used
- Asymmetry scorer MANUAL ILLUSTRATIVE labeled, no empirical significance claim
- Non-causal wording present
- No em dashes in prose fields
- Deal disclosure false for all FT OpenAI articles
"""
import os
import yaml

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "..", "profiles", "financial-times.yaml")

def load_profile():
    with open(PROFILE_PATH, 'r') as f:
        return yaml.safe_load(f)

def test_mechanism_415_exists():
    profile = load_profile()
    # openai block contains iteration_415
    openai = profile.get("competitor_relationships", {}).get("openai", {})
    # also check top-level competitor_relationships openai iteration
    # mechanism lives under competitor_relationships.openai.iteration_415...
    found = False
    # search in competitor_relationships.openai keys
    for k in openai.keys():
        if "iteration_415" in k:
            found = True
            mech = openai[k]
            assert mech.get("mechanism") == 415
            assert "Type A" in mech.get("type", "")
            break
    assert found, "Missing iteration_415 in competitor_relationships.openai"

def test_primary_terms_undisclosed_and_secondary():
    profile = load_profile()
    openai = profile["competitor_relationships"]["openai"]
    assert openai.get("cash_terms_disclosed") is False
    assert openai.get("valuation_source_type") == "secondary_report_based"
    primary = openai.get("valuation_primary_source", "")
    assert "not disclosed" in primary.lower() or "undisclosed" in primary.lower()
    sec = openai.get("valuation_secondary_source", "")
    assert "WSJ" in sec or "Digiday" in sec or "$5" in sec

def test_mechanism_415_source_provenance():
    profile = load_profile()
    openai = profile["competitor_relationships"]["openai"]
    mech_key = "iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"
    assert mech_key in openai, f"Missing {mech_key}"
    mech = openai[mech_key]
    # Must have primary Reuters deal source in financial_relationship
    fin = mech["financial_relationship"]
    assert "reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29" in fin["primary_source"]
    # At least 3 openai + 3 meta
    assert len(mech["ft_openai_growth_sources_aug2026"]) >= 3
    assert len(mech["ft_meta_capital_privacy_sources"]) >= 3
    urls = str(mech.get("source_urls",""))
    # Check key URLs present - FT-attributed OpenAI comparators
    assert "openai-nearly-double-workforce-8000-by-end-2026-ft-reports" in urls
    assert "openai-plans-chatgpt-superapp-overhaul-ahead-listing-ft-reports" in urls
    assert "openai-spending-hit-34-billion-last-year-ahead-planned-ipo-ft-reports" in urls
    assert "openai-floats-giving-government-5-share" in urls
    assert "openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents" in urls
    assert "meta-super-sensing-glasses-record-everything" in urls or "macrumors.com/2026/07/09/meta-super-sensing" in urls
    assert "meta-weighs-big-equity-raising" in urls
    # No invented ft.com primary where secondary used - openai first should be reuters citing FT
    assert mech["ft_openai_growth_sources_aug2026"][0]["url"].startswith("https://www.reuters.com/")

def test_scoring_manual_illustrative():
    profile = load_profile()
    mech = profile["competitor_relationships"]["openai"]["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]
    scorer = mech["asymmetry_scoring_manual_illustrative"]
    assert scorer["note"].startswith("MANUAL ILLUSTRATIVE") or "MANUAL ILLUSTRATIVE" in scorer["note"]
    assert scorer["p_value"] == "NOT CALCULATED no observed corpus" or "NOT CALCULATED" in str(scorer["p_value"])
    assert scorer["cohens_d"] == "NOT CALCULATED"
    assert scorer["significant"] is False
    assert scorer["empirical_required"] is True
    # delta check tolerance updated for 5 vs 3 source recalc
    assert abs(scorer["delta_manual_illustrative"] - (-0.6553)) < 0.02
    # synthetic_note must warn illustrative only
    synth = scorer.get("synthetic_note","") + mech.get("finding_summary","")
    assert "illustrative" in synth.lower()

def test_cautious_language_and_non_causal():
    profile = load_profile()
    mech = profile["competitor_relationships"]["openai"]["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]
    fin = mech["financial_relationship"]
    nc = fin["non_causal_language"].lower()
    assert "does not prove" in nc or "correlation does not" in nc
    assert "structural incentive" in nc or "predictor" in nc
    summary = mech["finding_summary"].lower()
    assert "proves editorial control" not in summary
    assert "proves" not in summary or "predicts" in summary

def test_deal_disclosure_false_all():
    profile = load_profile()
    mech = profile["competitor_relationships"]["openai"]["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]
    for art in mech["ft_openai_growth_sources_aug2026"]:
        assert art.get("deal_disclosed") is False, f"deal_disclosed should be false for {art.get('title')}"

def test_no_em_dashes():
    profile = load_profile()
    mech = profile["competitor_relationships"]["openai"]["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]
    for field in ["finding_summary", "type"]:
        text = str(mech.get(field, ""))
        assert "—" not in text, f"Em dash found in {field}"

def test_financial_relationship_values():
    profile = load_profile()
    mech = profile["competitor_relationships"]["openai"]["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]
    fin = mech["financial_relationship"]
    assert fin["cash_terms_disclosed"] is False
    assert fin["valuation_source_type"] == "secondary_report_based"
    assert fin["meta_estimated_value"] == "$0"
    assert fin["deal_disclosed_in_ft_coverage"] is False
