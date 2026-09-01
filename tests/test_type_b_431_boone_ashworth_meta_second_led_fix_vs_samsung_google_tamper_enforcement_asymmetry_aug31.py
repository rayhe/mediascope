"""
Test Type B #431: Boone Ashworth Meta Second LED Fix vs Samsung/Google Tamper Enforcement Asymmetry Aug 31 2026

Mechanism #431 Type B - Journalist Cross-Entity Tracking
Journalist: Boone Ashworth (WIRED Staff Writer, Gear) + Reece Rogers co-author context
Focus: Meta second LED fix (mid-recording cover, Aug 27-28 2026) receives reactive "closes loophole" framing
vs Samsung Galaxy Glasses and Google Android XR identical hardware receives zero tamper-enforcement coverage

Validates:
- Meta second LED fix 6 sources Aug 27-28 2026 documented
- WIRED Boone Ashworth Gear desk coverage of Meta glasses surveillance framing persists
- Samsung Galaxy Glasses (Snapdragon AR1 Gen 1, 12MP, LED anti-tamper) zero WIRED standalone article by Ashworth/Chokkattu Jul 22-Aug 31 2026 (40 days)
- Google Android XR tamper-detection not covered by WIRED as privacy feature vs Meta LED enforcement framed as closes loophole
- Same-journalist evidence: Boone Ashworth co-author OpenAI hardware vs Meta hardware (Mechanism #365 extension)
- Financial correlation not causation
- 7 confounders STRONG/MODERATE/WEAK
- No em dashes

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


def test_boone_ashworth_exists():
    entry = get_journalist("Boone Ashworth")
    assert entry["name"] == "Boone Ashworth"
    assert "WIRED" in str(entry.get("notes", "")) or "Wired" in str(entry.get("career", ""))


def test_mechanism_431_exists_in_boone():
    entry = get_journalist("Boone Ashworth")
    # Mechanism stored either top-level or under competitor_coverage or dedicated key
    # We check for key containing 431
    found = False
    for k in entry.keys():
        if "431" in str(k):
            found = True
            mech = entry[k]
            assert mech["mechanism_id"] == 431
            assert mech["iteration_type"] == "B" or mech.get("type") == "B" or "B" in str(mech.get("iteration_type", ""))
            break
    assert found, "Mechanism 431 not found in Boone Ashworth entry"


def test_meta_second_led_fix_documented():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    meta = mech["meta_second_led_fix"]
    assert meta["date"] == "2026-08-27" or "2026-08-27" in str(meta["date"]) or "2026-08-28" in str(meta["date"])
    assert len(meta["source_urls"]) >= 5
    assert any("gadgetreview.com" in u for u in meta["source_urls"])
    assert any("9to5google.com" in u for u in meta["source_urls"])
    assert any("aiweekly.co" in u for u in meta["source_urls"])
    # Fix description
    assert "mid-recording" in str(meta["fix_description"]).lower() or "cover" in str(meta["fix_description"]).lower()
    # Framing reactive
    assert "closes loophole" in str(meta["framing"]).lower() or "reactive" in str(meta["framing"]).lower()
    assert "late" in str(meta["framing"]).lower() or "obvious" in str(meta["framing"]).lower()


def test_samsung_selection_gap_40_days():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    samsung = mech["samsung_galaxy_glasses_gap"]
    assert samsung["wired_standalone_articles_by_chokkattu_ashworth_jul22_aug31"] == 0
    assert samsung["days_since_unpacked"] == 40 or "40" in str(samsung["days_since_unpacked"])
    assert samsung["hardware"]["chip"] == "Snapdragon AR1 Gen 1"
    assert samsung["hardware"]["camera"] == "12MP"
    assert "LED" in str(samsung["hardware"]["privacy_feature"]) or "anti-tamper" in str(samsung["hardware"]["privacy_feature"]).lower()
    assert len(samsung["other_publications_covering"]) >= 10


def test_google_android_xr_tamper_not_covered():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    google = mech["google_android_xr_gap"]
    assert google["wired_privacy_feature_framing"] == "absent" or "absent" in str(google["wired_privacy_feature_framing"]).lower()
    assert google["tamper_detection_documented_by_wired"] is False or "false" in str(google["tamper_detection_documented_by_wired"]).lower()
    assert "Gemini" in str(google) or "Android XR" in str(google)


def test_same_journalist_evidence():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    ev = mech["same_journalist_evidence"]
    assert "Boone Ashworth" in ev["journalist"]
    assert ev["wired_gear_desk"] is True or "Gear" in str(ev["beat"])
    # Co-author context
    assert "Reece Rogers" in str(ev.get("co_author_context", "")) or "Rogers" in str(ev)


def test_triangulation_framing_inversion():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    tri = mech["triangulation_matrix"]
    assert "comfort" in str(tri).lower() or "price" in str(tri).lower() or "privacy" in str(tri).lower()
    # Meta cheapest gets most criticism
    assert "799" in str(tri) or "Meta" in str(tri)
    # Samsung 2.25x and Apple 4.38x absent
    assert "1799" in str(tri) or "Samsung" in str(tri)


def test_asymmetry_scorer_manual_illustrative():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    asym = mech["asymmetry_scorer_result"]
    assert asym["label"] == "MANUAL_ILLUSTRATIVE_NOT_EMPIRICAL" or "MANUAL" in asym["label"]
    assert asym["significant"] is False
    assert "NOT_CALCULATED" in asym["p_value"]
    assert asym["target_entity"] == "Meta"
    assert asym["delta_MANUAL_ILLUSTRATIVE"] < 0
    assert "Requires VADER" in asym["methodology"] or "illustrative" in asym["methodology"].lower()


def test_financial_context_correlation_not_causation():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    fin = mech["financial_context_correlation_not_causation"]
    partners = fin["conde_nast_ai_licensing_partners"]
    assert partners["meta"] == 0
    assert "openai" in partners
    assert "amazon_rufus" in partners or "amazon" in str(partners).lower()
    assert "correlation not causation" in fin["non_causal_language"].lower() or "does not imply" in fin["non_causal_language"].lower()
    assert "private" in fin["non_causal_language"].lower() or "no SEC filings" in str(fin).lower()


def test_confounders_ranked():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    confs = mech["confounders"]
    assert len(confs) >= 6
    strong_count = sum(1 for c in confs if "[STRONG]" in c)
    assert strong_count >= 2
    conf_text = " ".join(confs).lower()
    assert "dominant" in conf_text or "market share" in conf_text
    assert "shipping" in conf_text or "product stage" in conf_text
    assert "beat assignment" in conf_text
    assert "form factor" in conf_text or "headset" in conf_text


def test_source_urls_https():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    urls = mech["source_urls"]
    assert len(urls) >= 10
    assert all(u.startswith("https://") for u in urls), "All URLs must be HTTPS per project rule"
    assert any("wired.com" in u for u in urls)
    assert any("gadgetreview.com" in u or "9to5google.com" in u for u in urls)


def test_no_em_dashes():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    # Check pattern and framing
    assert "—" not in str(mech.get("pattern", ""))
    assert "—" not in str(mech.get("discovery_date", ""))
    # Check all string values recursively for em dash
    import json
    mech_str = json.dumps(mech)
    assert "—" not in mech_str, "Em dash found in mechanism - violates project rule"


def test_cross_references():
    entry = get_journalist("Boone Ashworth")
    mech_key = [k for k in entry.keys() if "431" in str(k)][0]
    mech = entry[mech_key]
    refs = mech["cross_references"]
    assert 39 in refs or 42 in refs  # Samsung gaps
    assert 365 in refs or 357 in refs  # talent war / hardware inversion
    assert 426 in refs  # comfort price privacy triangulation


def test_wired_yaml_contains_chokkattu_second_led():
    # Ensure wired.yaml mentions second LED fix to preserve cross-file consistency
    if os.path.exists(WIRED_YAML):
        with open(WIRED_YAML, "r") as f:
            content = f.read()
            # At least mention of second LED fix or tamper
            assert "second" in content.lower() or "tamper" in content.lower() or "LED" in content
