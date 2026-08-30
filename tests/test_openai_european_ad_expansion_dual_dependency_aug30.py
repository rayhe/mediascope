"""
Test OpenAI European Ad Expansion Dual Dependency - Mechanism 386 Type C
Iteration 386 Aug 30 2026 02:00 PT

Validates:
- Mechanism 386 exists in competitor-entities.yaml and wired.yaml
- Financial channels correctly mapped (licensing vs ad cannibalization)
- 31 markets European expansion verified via Adweek etc
- Source URLs present
- No causal claim - cautious language
- Illustrative tone arrays flagged illustrative only per standing rule Aug 28
- Em dash check
"""
import yaml
import pathlib
import re

def load_yaml(path):
    return yaml.safe_load(open(path))

def test_mechanism_386_competitor_entities():
    data = load_yaml("profiles/competitor-entities.yaml")
    openai = data["entities"]["openai"]
    # Find key
    key = None
    for k in openai.keys():
        if "european_ad_expansion" in k or "386" in str(k) or "dual_dependency" in k:
            if isinstance(openai[k], dict) and openai[k].get("mechanism_id") == 386:
                key = k
                break
        if isinstance(openai[k], dict) and openai[k].get("mechanism_id") == 386:
            key = k
            break
    assert key is not None, "Mechanism 386 not found in competitor-entities.yaml openai section"
    mech = openai[key]
    assert mech["mechanism_id"] == 386
    assert mech["iteration"] == 386
    assert mech["type"] == "financial_incentive_mapping" or "financial" in str(mech.get("type","")).lower() or "Type C" in str(mech.get("type",""))
    # Financial channels
    assert "channel_1_licensing_revenue" in mech or "financial_channels" in mech
    # Source URLs
    srcs = mech.get("source_urls", [])
    # also nested sources
    if "channel_1_licensing_revenue" in mech:
        srcs += mech["channel_1_licensing_revenue"].get("source_urls", [])
    if "channel_2_ad_cannibalization" in mech:
        srcs += mech["channel_2_ad_cannibalization"].get("source_urls", [])
    adweek_found = any("adweek.com" in s for s in srcs)
    assert adweek_found, f"Adweek source missing in mech {key} sources: {srcs[:5]}"
    # Cautious language - check dual_dependency_synthesis or finding
    text_blob = str(mech)
    assert "does not imply causation" in text_blob.lower() or "correlation does not imply" in text_blob.lower() or "does not prove causation" in text_blob.lower() or "correlate" in text_blob.lower(), "Cautious language missing"
    # No causal claim
    assert "proves editorial control" not in text_blob.lower()
    # Em dash check
    assert "—" not in text_blob, "Em dash found - violates project rule"
    # Illustrative warning
    assert "illustrative only" in text_blob.lower(), "Illustrative only warning missing for synthetic scores"
    print(f"PASS competitor-entities.yaml {key}")

def test_mechanism_386_wired():
    data = load_yaml("profiles/wired.yaml")
    # Find mechanism
    key = None
    for k,v in data.items():
        if isinstance(v, dict) and v.get("mechanism_id") == 386:
            key = k
            break
    assert key is not None, "Mechanism 386 not found in wired.yaml"
    mech = data[key]
    assert mech["mechanism_id"] == 386
    assert mech["iteration"] == 386
    # Check focus contains European ad expansion
    focus = str(mech.get("focus","")) + str(mech.get("finding",""))
    assert "European" in focus or "31" in focus, f"Focus missing European context: {focus[:200]}"
    # Source URLs
    srcs = mech.get("source_urls", [])
    assert any("adweek.com" in s for s in srcs), "Adweek missing in wired.yaml source_urls"
    assert any("reuters.com" in s for s in srcs), "Reuters missing"
    # Cautious language
    text_blob = str(mech)
    assert "correlation does not imply causation" in text_blob.lower() or "structural incentive" in text_blob.lower(), "Cautious language missing in wired.yaml"
    assert "—" not in text_blob, "Em dash in wired.yaml"
    assert "illustrative only" in text_blob.lower(), "Illustrative only missing in wired.yaml"
    # Check asymmetry scorer result has required fields
    scorer = mech.get("asymmetry_scorer_result", {})
    assert "delta" in scorer, "delta missing in scorer"
    assert "ci_95" in scorer or "ci" in str(scorer).lower()
    print(f"PASS wired.yaml {key}")

def test_no_causal_claim():
    # Ensure both files use cautious language not causal proof
    for path in ["profiles/competitor-entities.yaml", "profiles/wired.yaml"]:
        text = pathlib.Path(path).read_text()
        # Find mechanism 386 section slice
        if "386" in text:
            # crude check: ensure no sentence says "proves that OpenAI controls"
            assert "proves that OpenAI controls" not in text.lower()
            assert "proves editorial" not in text.lower()

if __name__ == "__main__":
    test_mechanism_386_competitor_entities()
    test_mechanism_386_wired()
    test_no_causal_claim()
    print("All tests PASS for mechanism 386")
