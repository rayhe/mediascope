"""
Iteration #352 — Type C Financial Incentive Mapping — Apple Q3 2026 Services Advertising Record + Siri AI Variable-Pay + Gemini Bypass Compound Leverage

Mechanism #363 validates Apple five-channel publisher financial capture Q3 2026:
- SEC 10-Q filing Jul 31 2026 language progression Q2→Q3 App Store dropped, advertising rising
- Q3 Services $30.7B record, 12% YoY, 28.1% of $109.4B total, 75.6% gross margin, 1.5B paid subs, 2.5B active devices
- Siri AI publisher deals WSJ Aug 12 2026 nine-figure variable pay-per-use multiyear (negotiation only as of Aug 20 2026)
- Gemini ~$1B/yr bypass Jan 12 2026, 1.2T params, structural-risk hypothesis publishers $0 conditional IF flows (reported/estimated not confirmed)
- App Store tax 15-30%, Apple One dilution, News+ 50% share Apple News total audience (free+paid) 125M MAU not paid subs
- Meta 0 Apple-specific channels vs 1 global voluntary licensing channel

All source URLs verified HTTPS — Primary sources SEC filings + earnings call + WSJ (tier 1), supplemented by trade/tech coverage MacRumors/GSMArena/Motley Fool/Tech-Insider/PPC Land for corroboration (tier 2).
"""

import yaml
from pathlib import Path
import re

COMPETITOR_YAML = Path(__file__).parent.parent / "profiles" / "competitor-entities.yaml"

def load_entities():
    with open(COMPETITOR_YAML, "r") as f:
        data = yaml.safe_load(f)
    return data

def test_yaml_parseable():
    data = load_entities()
    assert "entities" in data or "apple" in str(data).lower()

def test_apple_entity_exists():
    data = load_entities()
    assert "apple" in data.get("entities", {}) or "apple" in data
    # handle both top-level entities key
    entities = data.get("entities", data)
    assert "apple" in entities

def test_mechanism_363_exists():
    data = load_entities()
    entities = data.get("entities", data)
    apple = entities["apple"]
    assert "apple_siri_advertising_compound_leverage_q3_2026" in apple
    mech = apple["apple_siri_advertising_compound_leverage_q3_2026"]
    assert mech["mechanism_id"] == 363

def test_mechanism_363_iteration_352_type_c():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    assert mech["iteration"] == 352
    assert "Type C" in mech["type"]
    assert mech["date_analyzed"] == "2026-08-28"

def test_q3_earnings_verified():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    ch2 = mech["five_channel_consolidation_q3_2026"]["channel_2_advertising"]
    assert ch2["services_revenue_b"] == 30.7
    assert ch2["services_yoy_pct"] == 12
    assert ch2["q3_2026_record"] is True
    assert "advertising" in ch2["sec_10q_language"]
    # Q2 vs Q3 driver progression
    assert "App Store" in ch2["q2_drivers"]
    assert "App Store" not in ch2["q3_drivers"]
    assert ch2["app_store_dropped"] is True

def test_sec_filing_urls_present():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    urls = mech["source_urls"]
    # Must include SEC 10-Q
    assert any("sec.gov" in u and "aapl-20260627" in u for u in urls)
    assert any("sec.gov" in u for u in urls)

def test_siri_ai_deal_verified():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    ch3 = mech["five_channel_consolidation_q3_2026"]["channel_3_siri_ai_variable_pay"]
    assert ch3["source"] == "Wall Street Journal"
    assert "nine-figure" in ch3["budget"] or "100M" in str(ch3["budget"]) or "nine_figure" in str(ch3.get("budget","")).lower() or ch3["budget"] == "nine-figure ($100M+)"
    assert ch3["compensation_model"] == "variable pay-per-use when publisher content is used by Siri AI, not lump sum" or "variable" in ch3["compensation_model"]
    assert ch3["status"] == "in_negotiation"
    # WSJ URL present
    assert any("wsj.com" in u for u in ch3["source_urls"])

def test_gemini_bypass_verified():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    ch4 = mech["five_channel_consolidation_q3_2026"]["channel_4_gemini_bypass"]
    assert ch4["annual_value_b"] == 1.0
    assert ch4["model_parameters"] == 1.2 or "1.2 trillion" in str(ch4.get("model_parameters",""))
    # Publishers receive $0
    assert "$0" in ch4["mechanism"] or "receive $0" in ch4["mechanism"] or "publishers receive $0" in ch4["mechanism"].lower() or "$0" in str(ch4)

def test_meta_contrast_zero_channels():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    contrast = mech["meta_contrast"]
    assert contrast["apple_channels"] == 5
    assert contrast["meta_channels"] == 0
    assert contrast["meta_has_news_app"] is False

def test_leverage_ranking():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    ranking = mech["leverage_ranking_update"]
    assert ranking["microsoft"] == 7
    assert ranking["amazon"] == 6
    assert ranking["apple"] == 5
    assert ranking["google"] == 4
    assert ranking["meta"] == 1

def test_confounders_present():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    confounders = mech["confounding_factors"]
    assert len(confounders) >= 4
    strong_count = sum(1 for c in confounders if c["strength"] == "STRONG")
    assert strong_count >= 2

def test_cautious_language():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    cautious = mech["cautious_language"]
    assert "does not imply causation" in cautious or "correlation does not" in cautious.lower() or "STRUCTURAL INCENTIVE" in cautious
    assert "illustrative" in cautious.lower() or "Synthetic" in cautious

def test_source_urls_https():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    for url in mech["source_urls"]:
        assert url.startswith("https://"), f"URL not HTTPS: {url}"

def test_no_duplicate_mechanism_ids():
    # Global uniqueness check for 363
    data = load_entities()
    entities = data.get("entities", data)
    count_363 = 0
    for ent_name, ent_data in entities.items():
        if not isinstance(ent_data, dict):
            continue
        for k, v in ent_data.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 363:
                count_363 += 1
    assert count_363 == 1, f"mechanism 363 appears {count_363} times, expected 1"

def test_timeline_coherence():
    data = load_entities()
    mech = data["entities"]["apple"]["apple_siri_advertising_compound_leverage_q3_2026"]
    ch3 = mech["five_channel_consolidation_q3_2026"]["channel_3_siri_ai_variable_pay"]
    timeline = ch3["timeline"]
    assert "dec_2023" in timeline
    assert "jan_2026" in timeline
    assert "aug_2026" in timeline
    # Dec 2023 approach failed, Jan 2026 bypass, Aug 2026 return
    assert "No deals closed" in timeline["dec_2023"] or "no deals" in timeline["dec_2023"].lower()
    assert "Gemini" in timeline["jan_2026"]
