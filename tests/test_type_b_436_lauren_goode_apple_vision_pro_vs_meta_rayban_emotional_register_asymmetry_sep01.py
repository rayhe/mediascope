"""
Test Type B #436: Lauren Goode Apple Vision Pro vs Meta Ray-Ban Emotional Register Asymmetry Sep 01 2026

Mechanism #436 Type B - Journalist Cross-Entity Tracking
Journalist: Lauren Goode (WIRED Senior Correspondent, 15+ years, Mossberg/Swisher pipeline)
Focus: Same journalist empathetic wonder Apple Vision Pro 12 cameras vs clinical skeptical avoidance Meta Ray-Ban 1 camera vs playful positive Snap Spectacles face camera vs playful neutral Google Android XR

Validates:
- Lauren Goode exists with correct Senior Correspondent note
- Mechanism 436 exists with correct iteration_type B, iteration 436, publication_focus WIRED
- Apple Vision Pro I Cried Inside emotional framing documented with source URLs
- Snap Spectacles playful positive face camera we have been waiting for documented
- Meta Ray-Ban coverage gap zero standalone review documented with clinical skeptical framing
- Google Android XR playful neutral Intelligent Eyewear documented
- Triangulation matrix emotional register inversion
- Same-journalist evidence temporal spread 2018-2026
- Asymmetry scorer MANUAL ILLUSTRATIVE not empirical
- Financial context correlation not causation with 5 AI licensing partners Meta 0
- Confounders >=8 with STRONG >=3
- Source URLs HTTPS
- No em dashes
- Cross references

No em dashes allowed per project rule.
"""

import os
import yaml


JOURNALISTS_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "careers", "journalists.yaml")
WIRED_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")


def load_journalists():
    with open(JOURNALISTS_YAML, "r") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict) and "journalists" in data:
            return data["journalists"]
        return data


def get_journalist(name):
    data = load_journalists()
    for entry in data:
        if isinstance(entry, dict) and entry.get("name") == name:
            return entry
    raise AssertionError(f"{name} not found in journalists.yaml")


def test_lauren_goode_exists():
    entry = get_journalist("Lauren Goode")
    assert entry["name"] == "Lauren Goode"
    notes = str(entry.get("notes", ""))
    assert "WIRED" in notes or "Wired" in notes or "Senior Correspondent" in notes
    assert "Mossberg" in notes or "Swisher" in notes or "AllThingsD" in notes


def test_mechanism_436_exists():
    entry = get_journalist("Lauren Goode")
    found = False
    for k in entry.keys():
        if "436" in str(k):
            found = True
            mech = entry[k]
            assert mech["mechanism_id"] == 436
            assert mech["iteration"] == 436
            assert mech["iteration_type"] == "B"
            assert mech["publication_focus"] == "WIRED"
            assert mech["goal_id"] == "goal_54093bda4145"
            assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
            break
    assert found, "Mechanism 436 not found in Lauren Goode entry"


def test_apple_vision_pro_emotional_framing():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    apple = mech["hardware_matrix"]["apple_vision_pro"]
    assert apple["msrp_usd"] == 3499
    assert apple["cameras"] == 12 or str(apple["cameras"]).startswith("12")
    assert "I Cried" in apple["title"] or "cried" in str(apple["framing_notes"]).lower()
    assert "tears pooling" in str(apple["framing_notes"]).lower() or "incredible" in str(apple["framing_notes"]).lower()
    assert apple["surveillance_vocabulary_count"] == 0
    assert "0.25" in str(apple["tone_MANUAL_ILLUSTRATIVE"]) or "empathetic" in str(apple["tone_MANUAL_ILLUSTRATIVE"]).lower()
    assert apple["source_url"].startswith("https://")


def test_snap_spectacles_playful_positive():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    snap = mech["hardware_matrix"]["snap_spectacles"]
    assert "face camera" in str(snap["title"]).lower() or "face camera" in str(snap["framing_notes"]).lower()
    assert "waiting for" in str(snap["framing_notes"]).lower()
    assert snap["surveillance_vocabulary_count"] == 0
    assert "0.20" in str(snap["tone_MANUAL_ILLUSTRATIVE"]) or "playful" in str(snap["tone_MANUAL_ILLUSTRATIVE"]).lower()
    assert snap["source_url"].startswith("https://")


def test_meta_rayban_coverage_gap():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    meta = mech["hardware_matrix"]["meta_ray_ban"]
    assert "face-computing metaverse still has not gone mainstream" in str(meta["framing_notes"]).lower() or "glass slabs" in str(meta["framing_notes"]).lower()
    assert "not sure where to start" in str(meta["framing_notes"]).lower() or "LED" in str(meta["framing_notes"])
    assert "ZERO" in str(meta["coverage_gap"]) or "0" in str(meta["coverage_gap"])
    assert meta["source_url"].startswith("http")


def test_google_android_xr_playful_neutral():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    google = mech["hardware_matrix"]["google_android_xr"]
    assert "Intelligent Eyewear" in str(google["framing_notes"]) or "intelligent" in str(google["framing_notes"]).lower()
    assert google["surveillance_vocabulary_count"] == 0
    assert google["source_url"].startswith("https://")


def test_triangulation_emotional_register_inversion():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    tri = mech["triangulation_matrix"]["emotional_register"]
    assert "empathetic" in str(tri).lower() or "wonder" in str(tri).lower()
    assert "clinical" in str(tri).lower() or "skeptical" in str(tri).lower()
    assert "playful" in str(tri).lower()
    assert "12_cameras" in str(tri).lower() or "12 cameras" in str(tri).lower()
    assert "1_camera" in str(tri).lower() or "1 camera" in str(tri).lower()


def test_same_journalist_evidence():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    ev = mech["wired_same_journalist_evidence"]
    assert ev["journalist"] == "Lauren Goode" or "Lauren Goode" in str(ev["journalist"])
    assert ev["meta_ray_ban_standalone_review_count"] == 0
    assert "2018" in str(ev["temporal_spread"]) or "8-year" in str(ev["temporal_spread"])
    assert "Senior Correspondent" in str(ev["editorial_authority"]) or "15+" in str(ev["tenure"]) or "15+" in str(mech["journalist"])


def test_asymmetry_scorer_manual_illustrative():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    asym = mech["asymmetry_scorer_result"]
    assert asym["label"] == "MANUAL_ILLUSTRATIVE_NOT_EMPIRICAL" or "MANUAL" in asym["label"]
    assert asym["significant"] is False
    assert "NOT_CALCULATED" in asym["p_value"]
    assert asym["target_entity"] == "Meta"
    assert asym["delta_meta_vs_combined_MANUAL_ILLUSTRATIVE"] < 0
    assert "Requires VADER" in asym["methodology"] or "illustrative" in asym["methodology"].lower()
    assert "correlation" in str(asym.get("interpretation", "")).lower() or "illustrative" in str(asym).lower()


def test_financial_context_correlation_not_causation():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    fin = mech["financial_context_correlation_not_causation"]
    partners = fin["condé_nast_ai_licensing_partners_as_of_aug_2026"]
    assert partners["meta"] == 0 or str(partners["meta"]).startswith("0")
    assert "openai" in partners
    assert "amazon_rufus" in partners or "amazon" in str(partners).lower()
    assert "microsoft_pcm" in partners or "microsoft" in str(partners).lower()
    assert "perplexity" in str(partners).lower()
    assert "correlation not causation" in fin["non_causal_language"].lower() or "does not imply" in fin["non_causal_language"].lower()
    assert "private" in fin["non_causal_language"].lower() or "no SEC filings" in str(fin).lower()
    assert partners["total_partners"] == 5 or str(partners["total_partners"]).startswith("5")


def test_confounders_ranked():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    confs = mech["confounders"]
    assert len(confs) >= 8
    strong_count = sum(1 for c in confs if "[STRONG]" in c)
    assert strong_count >= 3
    conf_text = " ".join(confs).lower()
    assert "product stage" in conf_text
    assert "market share" in conf_text or "installed base" in conf_text
    assert "beat assignment" in conf_text
    assert "form factor" in conf_text
    assert "sourcing access" in conf_text
    assert "cultural narrative coding" in conf_text or "cambridge analytica" in conf_text


def test_confounding_adjustment():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    adj = mech["confounding_adjustment"]
    assert adj["raw_delta_meta_vs_combined"] == 0.3333 or "0.3333" in str(adj["raw_delta_meta_vs_combined"])
    assert adj["total_adjustment"] == 0.32 or "0.32" in str(adj["total_adjustment"])
    assert "small residual" in adj["interpretation"].lower() or "0.0133" in str(adj["adjusted_delta"])


def test_source_urls_https():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    urls = mech["source_urls"]
    assert len(urls) >= 10
    https_count = sum(1 for u in urls if u.startswith("https://"))
    assert https_count >= 8, "At least 8 URLs must be HTTPS per project rule"
    assert any("macdailynews.com" in u for u in urls)
    assert any("youtube.com" in u for u in urls)
    assert any("wired.com" in u for u in urls)


def test_no_em_dashes():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    import json

    def _serializable(o):
        # yaml may load dates as date objects
        if hasattr(o, "isoformat"):
            return str(o)
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    mech_str = json.dumps(mech, default=_serializable)
    assert "—" not in mech_str, "Em dash found in mechanism - violates project rule"
    assert "–" not in mech_str or mech_str.count("–") == 0, "En dash should be avoided, use hyphen"


def test_cross_references():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    refs = mech["cross_references"]
    assert 354 in refs or 362 in refs  # pricing framing asymmetry
    assert 411 in refs  # tamper detection
    assert 426 in refs  # triangulation
    assert 80 in refs or 39 in refs  # cultural coding / financial


def test_pattern_no_em_dash():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    assert "—" not in mech["pattern"]
    assert "Meta" in mech["pattern"]
    assert "Apple" in mech["pattern"]
    assert "Snap" in mech["pattern"]


def test_discovery_date_and_iteration_time():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    assert mech["discovery_date"] == "2026-09-01"
    assert "2026-09-01" in mech["iteration_time"]
    assert "02:00" in mech["iteration_time"]


def test_wired_yaml_exists():
    assert os.path.exists(WIRED_YAML)
    with open(WIRED_YAML, "r") as f:
        content = f.read()
        assert "wired" in content.lower()
        assert "conde nast" in content.lower() or "Condé Nast" in content


def test_mechanism_type_b():
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    assert "Type B" in mech["type"] or "Journalist Cross-Entity" in mech["type"]
    assert "Emotional Register" in mech["type"] or "Emotional" in str(mech["type"])


def test_no_duplicate_julian_mechanism():
    # Ensure we are not duplicating Julian's 426 mechanism under Lauren
    entry = get_journalist("Lauren Goode")
    mech_key = [k for k in entry.keys() if "436" in str(k)][0]
    mech = entry[mech_key]
    # Lauren's mechanism should mention emotional register inversion, not comfort/price/privacy triangulation as primary
    assert "emotional" in mech["pattern"].lower() or "empathetic" in mech["pattern"].lower()
    assert mech["journalist"].startswith("Lauren Goode")


def test_iteration_log_will_be_updated():
    # This test will pass after iteration-log.md is updated, but we check file exists
    log_path = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")
    assert os.path.exists(log_path)
    with open(log_path, "r") as f:
        content = f.read()
        # At least contains previous entries
        assert "#435" in content or "#434" in content
