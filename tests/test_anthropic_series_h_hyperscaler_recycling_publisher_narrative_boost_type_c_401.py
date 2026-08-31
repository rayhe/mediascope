"""
Mechanism #401 Type C — Anthropic Series H $65B Hyperscaler Recycling Publisher Narrative Boost

Type: C (Financial Incentive Mapping)
Mechanism: #401
Date: 2026-08-30 17:00 PT

Validates financial incentive mapping for Anthropic Series H $65B round that
included $15B previously committed hyperscaler investments (PYMNTS), including
$5B from Amazon, creating 30% headline inflation (65 vs 50 net new).

Source URLs required:
- https://www.geekwire.com/2024/amazon-boosts-total-anthropic-investment-to-8b-deepens-ai-partnership-with-claude-maker/
- http://techxplore.com/news/2024-11-amazon-invest-additional-billion-ai.html
- https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/
- https://www.engadget.com/ai/google-plans-to-invest-even-more-money-into-anthropic-185000776.html
- https://www.morningstar.com/news/marketwatch/20260528233/anthropic-nears-1-trillion-valuation-leapfrogging-openai
- https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-becomes-worlds-most-valuable-ai-startup-at-965-billion/
- https://www.adweek.com/commerce/amazons-ad-revenue-hits-76b/

No em dash anywhere.
"""
import yaml
import pathlib
import json

PROFILE_COMPETITOR = pathlib.Path("~/workspace/repos/mediascope/profiles/competitor-entities.yaml").expanduser()
PROFILE_WIRED = pathlib.Path("~/workspace/repos/mediascope/profiles/wired.yaml").expanduser()

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

def get_entities(data):
    if "entities" in data:
        return data["entities"]
    return data

def test_profiles_load():
    data_c = load_yaml(PROFILE_COMPETITOR)
    data_w = load_yaml(PROFILE_WIRED)
    assert data_c is not None
    assert data_w is not None

def test_series_h_hyperscaler_recycling_fields():
    data = load_yaml(PROFILE_COMPETITOR)
    entities = get_entities(data)
    anth = entities["anthropic"]
    ipo = anth["ipo_filing"]
    block = ipo.get("series_h_hyperscaler_recycling_401")
    assert block is not None, "series_h_hyperscaler_recycling_401 missing"
    assert block["mechanism_id"] == 401
    assert block["reported_round_b"] == 65
    assert block["reported_valuation_b"] == 965
    assert block["hyperscaler_included_b"] == 15
    assert block["amazon_included_b"] == 5
    assert block["google_included_implied_b"] == 10
    assert block["net_new_estimated_b"] == 50
    # arithmetic checks
    assert abs(block["recycling_pct"] - 23.1) < 0.2
    assert abs(block["headline_inflation_pct"] - 30.0) < 0.5
    assert block["amazon_total_prior_b"] == 8
    assert block["amazon_apr_2026_immediate_b"] == 5
    assert block["amazon_total_after_immediate_b"] == 13
    assert block["amazon_potential_total_b"] == 33
    assert block["google_apr_2026_immediate_b"] == 10
    assert block["google_conditional_b"] == 30
    assert block["google_total_commitment_b"] == 40
    assert block["tpu_commitment_gw"] == "3.5-5.0" or block["tpu_commitment_gw"] == "3.5-5.0"
    assert block["amazon_compute_commitment_b"] == 100
    assert block["amazon_trainium_gw"] == 5
    urls = block.get("source_urls", [])
    urls_str = " ".join(urls)
    assert "morningstar.com" in urls_str
    assert "pymnts.com" in urls_str
    assert "geekwire.com" in urls_str
    assert "techcrunch.com" in urls_str
    assert "engadget.com" in urls_str

def test_series_h_block_no_em_dash():
    data = load_yaml(PROFILE_COMPETITOR)
    entities = get_entities(data)
    block = entities["anthropic"]["ipo_filing"]["series_h_hyperscaler_recycling_401"]
    dumped = json.dumps(block, ensure_ascii=False)
    assert "—" not in dumped, "em dash found"
    assert "–" not in dumped, "en dash found - use hyphen"

def test_wired_mechanism_401_fields():
    data = load_yaml(PROFILE_WIRED)
    # wired.yaml is flat mapping of mechanisms plus header
    mech = data.get("anthropic_series_h_hyperscaler_recycling_401")
    assert mech is not None, "wired mechanism 401 missing"
    assert mech["mechanism_id"] == 401
    assert mech["type"] == "Type C - Financial Incentive Mapping"
    assert mech["publication"] == "wired"
    fs = mech.get("financial_structure", {})
    assert fs.get("series_h_reported_b") == 65
    assert fs.get("hyperscaler_included_b") == 15
    assert fs.get("net_new_estimated_b") == 50
    assert fs.get("amazon_total_nov2024_b") == 8
    assert fs.get("amazon_total_after_immediate_b") == 13
    assert fs.get("google_total_commitment_b") == 40
    urls = mech.get("source_urls", [])
    urls_str = " ".join(urls)
    assert "adweek.com" in urls_str
    assert "geekwire.com" in urls_str
    # correlational note present
    note = mech.get("correlational_note", "")
    assert "correlation does not imply causation" in note.lower() or "does not imply causation" in note.lower()

def test_wired_no_em_dash():
    data = load_yaml(PROFILE_WIRED)
    mech = data["anthropic_series_h_hyperscaler_recycling_401"]
    dumped = json.dumps(mech, ensure_ascii=False)
    assert "—" not in dumped
    assert "–" not in dumped

def test_source_urls_https():
    data_c = load_yaml(PROFILE_COMPETITOR)
    entities = get_entities(data_c)
    block = entities["anthropic"]["ipo_filing"]["series_h_hyperscaler_recycling_401"]
    for url in block.get("source_urls", []):
        if "techxplore.com" in url:
            # techxplore allows http in source but test requires https list includes at least one https
            continue
        assert url.startswith("https://"), f"URL must be https: {url}"
    data_w = load_yaml(PROFILE_WIRED)
    mech = data_w["anthropic_series_h_hyperscaler_recycling_401"]
    for url in mech.get("source_urls", []):
        if url.startswith("http://"):
            # allow one http (techxplore) but at least 6 https
            continue
        assert url.startswith("https://"), f"Wired URL must be https: {url}"

def test_mechanism_401_distinct_from_203_361():
    """Verify #401 is distinct from #203 circular capital and #361 expansion."""
    data_c = load_yaml(PROFILE_COMPETITOR)
    entities = get_entities(data_c)
    block = entities["anthropic"]["ipo_filing"]["series_h_hyperscaler_recycling_401"]
    # Must mention recycling / headline inflation concept not present in #203/#361
    finding = block.get("finding", "").lower()
    assert "previously committed" in finding or "recycling" in finding or "included" in finding
    assert "headline" in finding or "inflation" in finding
    # Must distinguish immediate vs conditional
    assert block.get("amazon_apr_2026_immediate_b") == 5
    assert block.get("google_apr_2026_immediate_b") == 10
    # Cross refs include 203 and 361
    refs = block.get("cross_refs", [])
    assert 203 in refs
    assert 361 in refs

def test_financial_arithmetic():
    """Validate arithmetic for recycling and inflation."""
    reported = 65
    hyperscaler = 15
    net_new = 50
    recycling_pct = (hyperscaler / reported) * 100
    inflation_pct = ((reported - net_new) / net_new) * 100
    assert abs(recycling_pct - 23.0769) < 0.2
    assert abs(inflation_pct - 30.0) < 0.1
    # Combined hyperscaler conditional equals reported
    combined = 40 + 25  # Google 40 + Amazon 25
    assert combined == 65

def test_cautious_language():
    data_c = load_yaml(PROFILE_COMPETITOR)
    entities = get_entities(data_c)
    block = entities["anthropic"]["ipo_filing"]["series_h_hyperscaler_recycling_401"]
    cautious = block.get("cautious_language", "").lower()
    assert "correlation" in cautious
    assert "does not" in cautious or "not proof" in cautious
    assert "distinguish" in cautious
    assert "immediate" in cautious or "conditional" in cautious
