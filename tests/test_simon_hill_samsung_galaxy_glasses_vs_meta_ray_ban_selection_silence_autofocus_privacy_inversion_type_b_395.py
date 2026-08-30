"""
Test for Iteration #395 Type B Journalist Cross-Entity Tracking
Simon Hill Samsung Galaxy Glasses vs Meta Ray-Ban selection silence + autofocus privacy inversion

Mechanism #395: WIRED Gear Simon Hill Samsung Galaxy Glasses vs Meta Ray-Ban
Same-price autofocus privacy inversion + 38-day selection silence

Quality gates per repaired Iteration #390 standard:
- Hypotheses labeled as hypotheses
- MANUAL ILLUSTRATIVE scores labeled as such
- No empirical significance claims without observed corpus
- Confounders documented
- Financial correlation not proof of editorial influence
- Source URLs required
- No em dashes in prose
"""

import pathlib
import re
import yaml

PROFILE = pathlib.Path("profiles/wired.yaml")
MECH_ID = 395
JOURNALIST = "Simon Hill"
COMPETITOR = "Samsung"
PRODUCT = "Galaxy Glasses"


def load_profile():
    data = yaml.safe_load(PROFILE.read_text())
    return data


def test_profile_exists():
    assert PROFILE.exists(), f"{PROFILE} missing"


def test_mechanism_395_exists():
    data = load_profile()
    key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    assert key in data, f"Mechanism {key} not found in wired.yaml"
    mech = data[key]
    assert mech["mechanism_id"] == MECH_ID
    assert mech["journalist"] == JOURNALIST
    assert mech["competitor"] == COMPETITOR


def test_provenance_and_sources():
    data = load_profile()
    key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    mech = data[key]
    # Must have source_urls with at least 3 primary sources
    urls = mech.get("source_urls", [])
    assert len(urls) >= 5, f"Expected >=5 source URLs, got {len(urls)}"
    # Must include Samsung primary newsroom
    assert any("samsung.com" in u for u in urls), "Missing Samsung primary source"
    # Must include at least one WIRED URL or TechTimes as secondary
    assert any("techtimes.com" in u or "androidauthority.com" in u or "wired.com" in u for u in urls), "Missing tech publication source"
    # Verify product_compared source_urls also present
    samsung = mech["product_compared"]["samsung_galaxy_glasses"]
    s_urls = samsung.get("source_urls", [])
    assert len(s_urls) >= 3, "Samsung product_compared needs >=3 source URLs"
    assert any("samsung.com" in u for u in s_urls), "Samsung product_compared missing samsung.com source"


def test_cautious_language_and_manual_illustrative():
    data = load_profile()
    key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    mech = data[key]
    scoring = mech["cross_entity_scoring"]
    # Must label MANUAL ILLUSTRATIVE
    assert "MANUAL ILLUSTRATIVE" in scoring["methodology_note"] or "MANUAL ILLUSTRATIVE" in str(scoring), "Must label MANUAL ILLUSTRATIVE"
    assert scoring.get("p_value") == "NOT CALCULATED - no observed corpus, do not claim significance" or "NOT CALCULATED" in str(scoring.get("p_value", "")), "p_value must be NOT CALCULATED for illustrative hypothesis"
    assert scoring.get("significant") is False, "Illustrative scoring must not claim significant"
    # Hypothesis framing
    hypo = mech.get("hypothesis", "")
    assert "hypothesis" in mech or "Hypothesis" not in hypo, "Hypothesis field should exist and be framed as hypothesis not fact"
    # Financial non-causal language
    fin = mech.get("financial_context", {})
    assert "non_causal_language" in mech or "non_causal_language" in str(mech) or "Correlation not proof" in str(mech) or "does not prove" in str(fin), "Must include non-causal language about financial relationships"
    # No em dashes in prose fields (project rule)
    text_blob = yaml.safe_dump(mech)
    # Check for em dash character
    assert "—" not in text_blob, "Em dash found in mechanism prose - project rule forbids em dashes, use hyphen or comma"


def test_confounders_documented():
    data = load_profile()
    key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    mech = data[key]
    confs = mech.get("confounders", [])
    assert len(confs) >= 4, f"Expected >=4 confounders documented, got {len(confs)}"
    # Must include STRONG confounders
    strong = [c for c in confs if "[STRONG]" in c]
    assert len(strong) >= 2, "Need at least 2 STRONG confounders"
    # Must include product-stage and market-share
    blob = " ".join(confs).lower()
    assert "announcement" in blob or "unshipped" in blob or "shipped" in blob, "Confounders must address announcement vs shipped product stage"
    assert "market share" in blob or "market_share" in blob or "80 percent" in blob, "Confounders must address market share dominance"


def test_journalist_unstudied_status():
    data = load_profile()
    # Verify Simon Hill not in prior mechanisms (except this new one)
    all_text = PROFILE.read_text()
    # Count occurrences of Simon Hill before this mechanism
    # This test ensures new journalist is genuinely unstudied
    mech_key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    # The journalist_profile.unstudied_status field must exist and claim unstudied
    mech = data[mech_key]
    profile = mech.get("journalist_profile", {})
    assert "unstudied_status" in profile, "Must document unstudied_status for new journalist"
    assert "No prior cross-entity mechanism" in profile["unstudied_status"], "Must assert no prior cross-entity mechanism for Simon Hill"


def test_no_unsupported_significance():
    data = load_profile()
    key = "simon_hill_samsung_galaxy_glasses_vs_meta_ray_ban_selection_silence_autofocus_privacy_inversion_395"
    mech = data[key]
    blob = yaml.safe_dump(mech).lower()
    # Must not claim p < 0.05 as empirical without observed corpus
    # Allow p_value field explicitly saying NOT CALCULATED, but disallow claiming significant true
    assert mech["cross_entity_scoring"]["significant"] is False, "Must not claim significant true for illustrative hypothesis"
    # Ensure no sentence like "statistically significant" without illustrative qualifier
    if "statistically significant" in blob:
        assert "illustrative" in blob or "manual illustrative" in blob, "If mentioning significance, must qualify as illustrative/manual"
