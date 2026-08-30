"""
Type C Financial Incentive Mapping - Google Alongside-AI-Content Ad Dominance vs Chatbot Marginality - Iteration 396

Tests for mechanism google_alongside_ai_content_ad_dominance_mechanism_396
- Validates schema, uniqueness, provenance, cautious wording, no em dash, no significance claim
- Does NOT claim execution results - validation via allowed non-terminal mechanisms only
"""

import os
import yaml

REPO_ROOT = os.path.expanduser("~/workspace/repos/mediascope")
COMPETITOR_YAML = os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml")
WIRED_YAML = os.path.join(REPO_ROOT, "profiles/wired.yaml")

MECHANISM_KEY = "google_alongside_ai_content_ad_dominance_mechanism_396"
MECHANISM_ID = 396

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_mechanism_exists_in_competitor_entities():
    data = load_yaml(COMPETITOR_YAML)
    assert "entities" in data
    assert "openai" in data["entities"], "openai entity should exist"
    entity = data["entities"]["openai"]
    # mechanism is under advertising_business.google_alongside_ai_content...
    assert "advertising_business" in entity
    adv = entity["advertising_business"]
    assert MECHANISM_KEY in adv, f"{MECHANISM_KEY} should be under entities.openai.advertising_business"
    mech = adv[MECHANISM_KEY]
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == 396
    assert mech["type"] == "C"
    assert mech["type_label"] == "financial_incentive_mapping"

def test_mechanism_exists_in_competitor_entities():
    data = load_yaml(COMPETITOR_YAML)
    assert "entities" in data
    assert "openai" in data["entities"], "openai entity should exist"
    entity = data["entities"]["openai"]
    # mechanism is under entities.openai.google_alongside_ai_content_ad_dominance_mechanism_396 (sibling of european_ad_expansion)
    assert MECHANISM_KEY in entity, f"{MECHANISM_KEY} should be under entities.openai"
    mech = entity[MECHANISM_KEY]
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == 396
    assert mech["type"] == "C"
    assert mech["type_label"] == "financial_incentive_mapping"

def test_wired_yaml_mechanism_exists():
    data = load_yaml(WIRED_YAML)
    # top-level mechanism
    assert MECHANISM_KEY in data, f"{MECHANISM_KEY} should be top-level in wired.yaml"
    mech = data[MECHANISM_KEY]
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == 396
    # also competitor_relationships.openai entry
    assert "competitor_relationships" in data
    cr = data["competitor_relationships"]
    assert "openai" in cr
    assert MECHANISM_KEY in cr["openai"], f"{MECHANISM_KEY} should be in competitor_relationships.openai"

def test_source_provenance_https():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["openai"][MECHANISM_KEY]
    urls = mech.get("source_urls", [])
    assert len(urls) >= 5, "should have at least 5 source URLs"
    for url in urls:
        assert url.startswith("https://"), f"source URL should be https: {url}"
        # check domains are expected
        assert any(d in url for d in ["emarketer.com", "adweek.com", "fastcompany.com", "digiday.com", "bestmediainfo.com", "neowin.net", "9to5google.com", "reuters.com"]), f"unexpected source domain: {url}"

def test_emarketer_quantification():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["openai"][MECHANISM_KEY]
    em = mech.get("emarketer_counter_forecast", {})
    assert em["us_ai_ad_spend_2026_b"] == 32.03
    assert em["us_ai_ad_spend_alongside_ai_content_2026_b"] == 26.42
    assert em["alongside_ai_content_pct_2026"] == 80
    assert em["chatbot_ads_pct_2026"] == 8
    assert em["us_chatbot_ad_market_2030_b"] == 5.41
    assert em["miss_magnitude_pct"] == 90

def test_google_q2_2026_numbers():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["openai"][MECHANISM_KEY]
    g = mech.get("google_q2_2026", {})
    assert g["total_google_advertising_b"] == 81.63
    assert g["search_b"] == 63.27
    assert g["youtube_b"] == 11.05
    assert g["network_b"] == 7.3

def test_cautious_language_no_causal_claim():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["openai"][MECHANISM_KEY]
    note = mech.get("correlational_note", "")
    assert "correlation does not imply causation" in note.lower() or "does not imply" in note.lower() or "correlational" in note.lower()
    assert "causation" in note.lower() or "causal" in note.lower() or "editorial control" in note.lower()
    # check wired.yaml top-level cautious language too
    w_data = load_yaml(WIRED_YAML)
    w_mech = w_data[MECHANISM_KEY]
    w_note = w_mech.get("correlational_note", "")
    assert "correlation does not imply causation" in w_note.lower()

def test_manual_illustrative_labeling_and_no_significance():
    data = load_yaml(WIRED_YAML)
    mech = data[MECHANISM_KEY]
    tone_result = mech.get("asymmetry_scorer_result", {})
    methodology = tone_result.get("methodology", "")
    assert "MANUAL ILLUSTRATIVE" in methodology
    assert tone_result.get("p_value") == "not_calculated"
    assert tone_result.get("significant") is False
    # cohens_d and ci_95 should be not_calculated
    assert tone_result.get("cohens_d") == "not_calculated"
    # No em dash in cautious_language and overview
    cautious = mech.get("correlational_note", "")
    assert "—" not in cautious, "correlational_note should not contain em dash"
    assert "—" not in mech.get("finding", ""), "finding should not contain em dash"

def test_mechanism_uniqueness():
    # Ensure mechanism_id 396 not used elsewhere in wired.yaml top-level and competitor_relationships
    data = load_yaml(WIRED_YAML)
    count_396 = 0
    for k, v in data.items():
        if isinstance(v, dict) and v.get("mechanism_id") == 396:
            count_396 += 1
    # also check inside competitor_relationships.openai
    cr_openai = data.get("competitor_relationships", {}).get("openai", {})
    for k, v in cr_openai.items():
        if isinstance(v, dict) and v.get("mechanism_id") == 396:
            count_396 += 1
    # We have 2 entries (top-level + competitor_relationships) - both 396, so count should be 2
    assert count_396 == 2, f"mechanism_id 396 should appear exactly twice (top-level + competitor_relationships.openai), found {count_396}"

def test_no_em_dash_in_competitor_yaml():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["openai"][MECHANISM_KEY]
    # check finding and notes have no em dashes
    for field in ["finding", "correlational_note"]:
        val = mech.get(field, "")
        if isinstance(val, str):
            assert "—" not in val, f"{field} should not contain em dash"
