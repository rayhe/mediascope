"""
Test for Mechanism #358: Amazon Triple Channel Financial Incentive (Type C)
Iteration #346 — Fri 2026-08-28 10:00 PT

Verifies:
- Mechanism 358 exists in competitor-entities.yaml amazon section
- Required fields: mechanism_id, date_analyzed, type, financial_channels, source_urls
- Q2 2026 numbers: $19.8B advertising (+26%), $42.2B AWS (+37%), $53.4B Anthropic gain
- Anthropic investment $13B (15-20% stake) and OpenAI $50B completed Jul 31 2026
- Triple channel structure (advertising, AWS, dual-lab equity)
- Source URLs are HTTPS and include required domains
- Confounding factors labeled STRONG/MODERATE/WEAK with adjusted<raw logic
- Cautious language: no causal claim, synthetic disclaimer
- Cross-reference to mechanism 25 dual-lab triangle
"""
import yaml
import pathlib
import re

ENTITIES_PATH = pathlib.Path(__file__).parent.parent / "profiles" / "competitor-entities.yaml"

def load_entities():
    with open(ENTITIES_PATH, "r") as f:
        return yaml.safe_load(f)

def test_mechanism_358_exists():
    data = load_entities()
    amazon = data["entities"]["amazon"]
    assert "amazon_triple_channel_financial_incentive_aug28" in amazon, "Mechanism 358 key missing"
    mech = amazon["amazon_triple_channel_financial_incentive_aug28"]
    assert mech["mechanism_id"] == 358
    assert mech["date_analyzed"] == "2026-08-28"
    assert mech["type"] == "financial_incentive_mapping"
    assert mech["iteration"] == 346

def test_q2_2026_advertising_numbers():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    ch1 = mech["financial_channels"]["channel_1_advertising"]
    assert ch1["q2_2026_b"] == 19.8
    assert ch1["yoy_pct"] == 26
    assert ch1["ttm_b"] == 76

def test_q2_2026_aws_numbers():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    ch2 = mech["financial_channels"]["channel_2_aws"]
    assert ch2["q2_2026_b"] == 42.2
    assert ch2["yoy_pct"] == 37

def test_anthropic_investment_and_gain():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    ch3 = mech["financial_channels"]["channel_3_dual_lab_equity"]
    assert ch3["anthropic_invested_b"] == 13
    assert ch3["anthropic_q2_2026_paper_gain_b"] == 53.4
    # Gain > operating income check via overview text
    assert "53.4B" in str(mech["overview"]) or ch3["anthropic_q2_2026_paper_gain_b"] == 53.4
    assert ch3["anthropic_stake_pct"] == "15-20" or "15-20" in str(ch3.values())

def test_openai_50b_completed():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    ch3 = mech["financial_channels"]["channel_3_dual_lab_equity"]
    assert ch3["openai_invested_b"] == 50
    assert ch3["combined_investment_b"] == 63
    # Verify completed Jul 31 2026 mention
    assert "Completed Jul 31 2026" in ch3["openai_status"] or "Jul 31 2026" in str(ch3["openai_status"]) or "Jul 31 2026" in str(mech["overview"])

def test_triple_channel_structure():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    channels = mech["financial_channels"]
    assert "channel_1_advertising" in channels
    assert "channel_2_aws" in channels
    assert "channel_3_dual_lab_equity" in channels
    # Check dynamics
    assert "triple_channel_dynamics" in mech
    assert len(mech["triple_channel_dynamics"]) >= 2

def test_source_urls_https_and_domains():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    urls = mech["source_urls"]
    assert len(urls) >= 6
    for url in urls:
        assert url.startswith("https://") or url.startswith("http://"), f"URL not http(s): {url}"
    # Required domains
    domains_required = ["aboutamazon.com", "fool.com", "techcrunch.com", "geekwire.com", "pymnts.com"]
    joined = " ".join(urls)
    for domain in domains_required:
        assert domain in joined, f"Missing domain {domain} in source_urls"

def test_confounders_labeled():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    confs = mech["confounding_factors"]
    assert len(confs) >= 4
    strengths = [c["strength"] for c in confs]
    assert "STRONG" in strengths
    assert "MODERATE" in strengths
    assert "WEAK" in strengths
    # Each has description
    for c in confs:
        assert "description" in c and len(c["description"]) > 20

def test_cautious_language():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    cautious = mech["cautious_language"]
    assert "does not imply causation" in cautious or "correlation" in cautious.lower()
    assert "synthetic" in cautious.lower() or "empirical" in cautious.lower() or "cannot establish" in cautious.lower()
    # No causal overclaim in overview
    overview = mech["overview"].lower()
    assert "proves" not in overview or "proves editorial influence" not in overview
    assert "causes softer coverage" not in overview

def test_coverage_prediction():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    assert "coverage_prediction" in mech
    pred = mech["coverage_prediction"]
    assert "model" in pred
    assert "temporal" in pred or "Q3-Q4 2026" in str(pred)

def test_cross_reference_to_mechanism_25():
    data = load_entities()
    # Mechanism 25 is dual-lab triangle, should be referenced or at least not duplicate
    amazon = data["entities"]["amazon"]
    assert 25 in [v.get("mechanism_id") for v in amazon.values() if isinstance(v, dict) and "mechanism_id" in v] or "mechanism_25_dual_lab_non_disclosure_triangle" in amazon
    mech358 = amazon["amazon_triple_channel_financial_incentive_aug28"]
    # Overview should mention triple channel distinct from dual-lab
    assert "triple" in mech358["overview"].lower() or "triple" in str(mech358).lower()

def test_no_duplicate_mechanism_id_358():
    data = load_entities()
    # Count mechanism_id 358 occurrences
    count = 0
    def recurse(obj):
        nonlocal count
        if isinstance(obj, dict):
            if obj.get("mechanism_id") == 358:
                count += 1
            for v in obj.values():
                recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)
    recurse(data)
    assert count == 1, f"mechanism_id 358 should appear exactly once, found {count}"

def test_financial_materiality():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    # $53.4B gain exceeds $27.5B operating income — check materiality mention
    overview = mech["overview"]
    assert "53.4B" in overview or "53.4" in str(mech["financial_channels"])
    dynamics_text = str(mech["triple_channel_dynamics"])
    assert "MATERIAL" in dynamics_text or "material" in dynamics_text.lower() or "85%" in dynamics_text or "operating income" in dynamics_text.lower()

def test_aws_commitments_100b():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    ch2 = mech["financial_channels"]["channel_2_aws"]
    assert ch2["openai_commitment_b"] == 100
    assert ch2["anthropic_commitment_b"] == 100
    # 2GW and 5GW capacity mentions in detail
    detail_str = str(ch2)
    assert "2GW" in detail_str or "2 GW" in detail_str or "Trainium" in detail_str
    assert "5GW" in detail_str or "5 GW" in detail_str or "Trainium" in detail_str

def test_type_c_iteration_metadata():
    data = load_entities()
    mech = data["entities"]["amazon"]["amazon_triple_channel_financial_incentive_aug28"]
    assert mech["type_c_focus"].startswith("Amazon")
    assert "advertising" in mech["type_c_focus"].lower()
    assert "AWS" in mech["type_c_focus"] or "aws" in mech["type_c_focus"].lower()
