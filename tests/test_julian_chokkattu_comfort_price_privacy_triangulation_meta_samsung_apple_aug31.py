"""
Test Julian Chokkattu comfort/price/privacy triangulation Meta vs Samsung vs Apple Aug 31 2026 Type B #426

Mechanism #426: WIRED Senior Editor Gear Julian Chokkattu (7+ years, 3,627+ articles, primary Meta hardware reviewer)
applies consistent comfort criticism across Meta Display ($799, 69g), Samsung Galaxy XR ($1,799, 847g total, 19 cameras), Apple Vision Pro ($3,499, 600-650g, 12 cameras)
but applies selective price-extraction and privacy-alarm vocabulary ONLY to Meta (cheapest, fewest cameras, strongest LED enforcement)
while omitting for Samsung (2.25x price, 19 cameras) and Apple (4.38x price, 12 cameras) despite higher-risk hardware.

Validates:
- Meta Display $799 documented with tamper-proof Jul 7 + Aug 27 fixes
- Samsung Galaxy XR $1,799 545g+302g 19 cameras Dec 2025 review Needs More Polish
- Apple Vision Pro $3,499 12 cameras hands-on Jan 2024 future of computing bulky weird
- Same journalist across 2.5-year window
- Comfort symmetric (fair), price/privacy asymmetric (manufacturer-dependent)
- Financial context correlation not causation
- 8 confounders with STRONG/MODERATE/WEAK labels
- No em dashes per project rule

No em dashes allowed.
"""

import os
import yaml

JOURNALISTS_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "careers", "journalists.yaml")


def load_journalists():
    with open(JOURNALISTS_YAML, "r") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict) and "journalists" in data:
            return data["journalists"]
        return data


def get_chokkattu():
    data = load_journalists()
    for entry in data:
        if isinstance(entry, dict) and entry.get("name") == "Julian Chokkattu":
            return entry
    raise AssertionError("Julian Chokkattu not found in journalists.yaml")


def test_chokkattu_exists():
    entry = get_chokkattu()
    assert entry["name"] == "Julian Chokkattu"
    assert "3,627" in entry["notes"] or "3627" in entry["notes"] or "7+ years" in entry["notes"]


def test_mechanism_426_exists():
    entry = get_chokkattu()
    key = "mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"
    assert key in entry, f"{key} missing in Julian Chokkattu entry"
    mech = entry[key]
    assert mech["mechanism_id"] == 426
    assert mech["iteration"] == 426
    assert mech["iteration_type"] == "B"
    assert "2026-08-31" in str(mech["discovery_date"]) or "2026-08-31" in str(mech["iteration_time"])


def test_hardware_matrix_three_entities():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    matrix = mech["hardware_matrix"]
    assert "meta_ray_ban_display" in matrix
    assert "samsung_galaxy_xr" in matrix
    assert "apple_vision_pro" in matrix
    # Meta cheapest
    assert matrix["meta_ray_ban_display"]["msrp_usd"] == 799
    assert matrix["samsung_galaxy_xr"]["msrp_usd"] == 1799
    assert matrix["apple_vision_pro"]["msrp_usd"] == 3499
    # Camera counts
    assert matrix["samsung_galaxy_xr"]["camera"] or "19" in str(matrix["samsung_galaxy_xr"])
    # Meta has 1 camera documented somewhere
    meta_str = str(matrix["meta_ray_ban_display"]).lower()
    assert "12mp" in meta_str or "camera" in meta_str


def test_meta_enforcement_documented():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    meta = mech["hardware_matrix"]["meta_ray_ban_display"]
    # Tamper enforcement
    enforcement = meta.get("tamper_enforcement", [])
    enforcement_str = " ".join(enforcement).lower()
    assert "tamper" in enforcement_str or "disabled" in enforcement_str
    assert "led" in enforcement_str
    # Subscription documented
    sub = meta.get("subscription_optional", {})
    assert sub.get("price_per_month") == 19.99 or "19.99" in str(sub)
    assert sub.get("on_device") is True


def test_samsung_review_documented():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    samsung = mech["hardware_matrix"]["samsung_galaxy_xr"]
    wired = samsung["wired_review"]
    assert "Needs More Polish" in wired["title"] or "More Polish" in wired["title"]
    assert "Julian Chokkattu" in str(wired.get("author", "")) or "Chokkattu" in str(wired)
    # Comfort criticism
    comfort = wired.get("comfort_criticism", [])
    comfort_str = " ".join(comfort).lower()
    assert "comfortable" in comfort_str or "pressure" in comfort_str or "forehead" in comfort_str
    assert "warm" in comfort_str or "sweaty" in comfort_str
    # Privacy alarm absent
    assert wired["privacy_alarm"] == "absent" or wired["surveillance_vocabulary_count"] == 0
    assert wired["price_criticism"] == "absent" or "absent" in str(wired["price_criticism"]).lower()


def test_apple_vision_pro_documented():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    apple = mech["hardware_matrix"]["apple_vision_pro"]
    wired = apple["wired_coverage"]
    assert "future of computing" in str(wired.get("key_quotes", "")).lower() or "future" in str(wired).lower()
    assert wired["surveillance_vocabulary_count"] == 0
    assert "bulky" in str(wired).lower() or "weird" in str(wired).lower()
    # Price ratio 4.38
    assert apple["price_ratio_vs_meta"] == 4.38 or "4.38" in str(apple["price_ratio_vs_meta"])


def test_triangulation_matrix_symmetry():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    tri = mech["triangulation_matrix"]
    # Comfort symmetric HIGH
    comfort = tri["comfort_criticism"]
    assert comfort["symmetry"] == "HIGH" or "HIGH" in str(comfort["symmetry"]).upper()
    assert comfort["meta"] == "present" or "present" in str(comfort["meta"]).lower()
    # Price asymmetric LOW
    price = tri["price_extraction_framing"]
    assert price["symmetry"] == "LOW" or "LOW" in str(price["symmetry"]).upper()
    assert "extracting value" in str(price["meta_799_cheapest"]).lower() or "monetizing" in str(price["meta_799_cheapest"]).lower()
    assert "absent" in str(price["samsung_1799_2.25x"]).lower()
    assert "absent" in str(price["apple_3499_4.38x"]).lower()
    # Privacy asymmetric LOW
    privacy = tri["privacy_surveillance_framing"]
    assert "LOW" in privacy["symmetry"]
    assert "mass surveillance" in str(privacy["meta_1_camera"]).lower() or "pervert" in str(privacy["meta_1_camera"]).lower() or "surveillance" in str(privacy["meta_1_camera"]).lower()
    assert "0 terms" in str(privacy["samsung_19_cameras"]).lower() or privacy["meta_1_camera"] != privacy["samsung_19_cameras"]
    # Camera count inversion
    cam_inv = privacy["camera_count_inversion"]
    assert cam_inv["meta_cameras"] == 1
    assert cam_inv["samsung_cameras"] == 19
    assert cam_inv["apple_cameras"] == 12


def test_same_journalist_evidence():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    ev = mech["wired_gear_desk_same_journalist_evidence"]
    assert "Julian Chokkattu" in ev["journalist"]
    assert "7+ years" in ev["tenure"] or "3627" in str(ev["tenure"]) or "3,627" in str(ev["tenure"])
    assert ev["meta_hardware_primary_reviewer"] is True
    # Temporal spread 2.5 years
    assert "2.5" in str(ev["same_journalist_temporal_spread"]) or "2024" in str(ev["coverage_dates"])


def test_asymmetry_scorer_manual_illustrative():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    asym = mech["asymmetry_scorer_result"]
    assert asym["target_entity"] == "Meta"
    assert "Samsung" in str(asym["peer_entities"]) and "Apple" in str(asym["peer_entities"])
    assert asym["label"] == "MANUAL_ILLUSTRATIVE_NOT_EMPIRICAL" or "MANUAL" in asym["label"]
    assert asym["p_value"] == "NOT_CALCULATED - no observed corpus scoring" or "NOT_CALCULATED" in asym["p_value"]
    assert asym["significant"] is False
    assert asym["empirical_validation_required"] is True
    # Delta negative
    assert asym["delta_meta_vs_combined_MANUAL_ILLUSTRATIVE"] < 0
    assert asym["delta_meta_vs_samsung_MANUAL_ILLUSTRATIVE"] < 0
    assert asym["delta_meta_vs_apple_MANUAL_ILLUSTRATIVE"] < 0
    # Methodology warns
    assert "Illustrative only" in asym["methodology"] or "illustrative" in asym["methodology"].lower()
    assert "Do not claim statistical significance" in asym["methodology"] or "Requires VADER" in asym["methodology"]


def test_financial_context_correlation_not_causation():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    fin = mech["financial_context_correlation_not_causation"]
    partners = fin["condé_nast_ai_licensing_partners_as_of_aug_2026"]
    assert partners["meta"] == 0 or partners["meta"] == "0 documented" or "0" in str(partners["meta"])
    assert "openai" in partners
    assert "amazon_rufus" in partners
    assert "microsoft_pcm" in partners
    assert "perplexity" in str(partners).lower()
    # Directional prediction softer Samsung Apple vs adversarial Meta correlates but not causation
    assert "correlation not causation" in fin["non_causal_language"].lower() or "Correlation does not imply" in fin["non_causal_language"]
    # No SEC filings note
    assert "private" in fin["non_causal_language"].lower() or "no SEC filings" in str(fin).lower() or "private" in str(fin).lower()


def test_confounders_documented():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    confs = mech["confounders"]
    assert len(confs) >= 7
    strong_count = sum(1 for c in confs if "[STRONG]" in c)
    assert strong_count >= 2
    conf_text = " ".join(confs).lower()
    assert "product stage" in conf_text
    assert "market share" in conf_text or "installed base" in conf_text
    assert "form factor" in conf_text
    assert "beat assignment" in conf_text
    assert "cultural narrative" in conf_text or "cultural coding" in conf_text


def test_confounding_adjustment():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    adj = mech["confounding_adjustment"]
    assert adj["raw_delta_meta_vs_combined"] == 0.625
    assert adj["total_adjustment"] == 0.39
    assert abs(adj["adjusted_delta"] - 0.235) < 0.01
    assert "small_to_moderate" in adj["interpretation"].lower() or "moderate" in adj["interpretation"].lower()


def test_source_urls_present():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    urls = mech["source_urls"]
    assert len(urls) >= 12
    # Must include compuscoop for Apple
    assert any("compuscoop.com" in u for u in urls)
    # Must include technewsvision for Samsung
    assert any("technewsvision.co.uk" in u for u in urls)
    # Must include slashdot for Meta subscription
    assert any("slashdot.org" in u for u in urls)
    # Must include eweek for tamper
    assert any("eweek.com" in u for u in urls)
    # Must include wired expected primaries
    assert any("wired.com" in u for u in urls)


def test_no_em_dashes_in_mechanism():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    pattern = mech["pattern"]
    assert "—" not in pattern, "Em dash found in pattern - violates project rule"
    for key in ["discovery_date", "iteration_time"]:
        val = str(mech.get(key, ""))
        assert "—" not in val


def test_cross_references_include_prior_mechanisms():
    mech = get_chokkattu()["mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31"]
    refs = mech["cross_references"]
    assert 354 in refs  # pricing asymmetry Snap Meta
    assert 362 in refs  # Samsung price parity
    assert 411 in refs  # tamper detection gap
    assert 42 in refs   # compound silence


def test_wired_yaml_updated():
    # Optional: ensure wired.yaml exists and mentions Chokkattu triangulation if updated
    wired_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    if os.path.exists(wired_path):
        with open(wired_path, "r") as f:
            content = f.read()
            # At least Julian mentioned
            assert "Julian Chokkattu" in content or "Chokkattu" in content
