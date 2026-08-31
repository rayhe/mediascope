"""
Type C Financial Incentive Mapping - Mechanism 406
Amazon OpenAI 50B Contingent Tranche IPO Timeline plus Google 81.63B Ad Dependency plus Anthropic 10B Bank Revolver Publisher Incentive Triangulation

Verifies financial relationships with primary sources:
- Amazon 50B commitment to OpenAI 122B round at 852B valuation structured as 15B immediate + 35B contingent on IPO by 2028 or AGI
- Google Q2 2026 ad revenue 81.63B Search 63.27B YouTube 11.06B
- Anthropic pre-IPO revolving credit facility exceeding 10B target tier structure 1.25B/1B/0.75B
"""

import yaml
import os

PROFILE_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/competitor-entities.yaml")

def load_yaml():
    with open(PROFILE_PATH, 'r') as f:
        data = yaml.safe_load(f)
    return data

def test_mechanism_406_exists():
    data = load_yaml()
    assert "entities" in data
    assert "openai" in data["entities"]
    openai = data["entities"]["openai"]
    # mechanism should be under openai entity
    assert "amazon_openai_contingent_tranche_ipo_timeline_mechanism_406" in openai, "Mechanism 406 not found in openai entity"
    mech = openai["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    assert mech["mechanism_id"] == 406
    assert mech["type"] == "C"

def test_amazon_50b_structure():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    amazon = mech["amazon_openai_commitment"]
    assert amazon["amazon_commitment_b"] == 50
    assert amazon["amazon_immediate_b"] == 15
    assert amazon["amazon_contingent_b"] == 35
    assert "IPO by end of 2028" in amazon["contingent_milestone"] or "IPO" in amazon["contingent_milestone"]
    assert amazon["round_size_b"] == 122
    assert amazon["valuation_b"] == 852
    # source URLs must be https
    assert len(amazon["source_urls"]) >= 2
    for url in amazon["source_urls"]:
        assert url.startswith("https://")

def test_google_q2_ad_dependency():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    google = mech["google_q2_2026_ad_dependency"]
    assert google["total_google_advertising_b"] == 81.63
    assert google["search_other_b"] == 63.27
    assert google["total_alphabet_revenue_b"] == 119.8
    assert len(google["source_urls"]) >= 3
    for url in google["source_urls"]:
        assert url.startswith("https://") or url.startswith("http://")

def test_anthropic_credit_facility():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    anthropic = mech["anthropic_credit_facility"]
    assert anthropic["facility_target_b"] == 10
    assert anthropic["facility_exceeds_target"] == True
    assert anthropic["prior_facility_b"] == 2.5
    assert anthropic["tier_structure"]["tier_1_commitment_b"] == 1.25
    assert anthropic["tier_structure"]["tier_2_commitment_b"] == 1.0
    assert anthropic["tier_structure"]["tier_3_commitment_b_max"] == 0.75
    assert "Morgan Stanley" in anthropic["prior_participants"]
    assert "Goldman Sachs" in anthropic["ipo_banks"] or "Goldman Sachs Group Inc" in str(anthropic["prior_participants"])
    assert len(anthropic["source_urls"]) >= 3

def test_financial_triangulation():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    tri = mech["financial_triangulation"]
    assert tri["amazon_total_ai_exposure_b"] == 63
    assert tri["amazon_openai_b"] == 50
    assert tri["google_q2_ad_b"] == 81.63
    assert tri["meta_publisher_deals"] == 0
    assert "0 for Meta" in tri["predictor"] or "Meta" in tri["predictor"]

def test_no_em_dashes():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    # check finding and correlational_note have no em dashes
    text = mech["finding"] + mech["correlational_note"]
    assert "—" not in text, "Em dash found in mechanism text - violates no em dash rule"
    assert "–" not in text, "En dash found - use hyphen only"

def test_asymmetry_scorer_manual_illustrative():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    scorer = mech["asymmetry_scorer_result"]
    assert scorer["methodology"].startswith("MANUAL ILLUSTRATIVE")
    assert scorer["p_value"] == "not_calculated"
    assert scorer["cohens_d"] == "not_calculated"
    assert "not_calculated" in str(scorer["ci_95"])
    assert scorer["significant"] == False
    assert "MANUAL_ILLUSTRATIVE" in str(scorer.keys()) or any("MANUAL_ILLUSTRATIVE" in k for k in scorer.keys())

def test_source_urls_https_provenance():
    data = load_yaml()
    mech = data["entities"]["openai"]["amazon_openai_contingent_tranche_ipo_timeline_mechanism_406"]
    all_urls = mech["source_urls"]
    assert len(all_urls) >= 6
    # at least 4 https
    https_count = sum(1 for u in all_urls if u.startswith("https://"))
    assert https_count >= 4, f"Expected at least 4 https URLs, got {https_count}"
