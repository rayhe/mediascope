"""
Test Julian Chokkattu Google Android XR tamper detection enforcement gap vs Meta LED tamper-proof enforcement Aug 31 2026 Type B #411

Mechanism #411: WIRED Gear desk (Julian Chokkattu Senior Editor Gear) applies enthusiastic framing to Google Android XR glasses
which announce tamper detection but NOT automatic camera shutdown (weaker enforcement, no technical spec, unknown enforcement layer)
while applying adversarial mass surveillance / pervert glasses framing to Meta Ray-Ban glasses with stronger enforcement
(July 7 2026 LED physical tamper -> camera disabled mandatory v26 + Aug 27 2026 mid-recording cover -> camera stops).

Validates:
- Meta July 7 2026 tamper-proof update exists with multiple primary sources
- Meta Aug 27 2026 mid-recording cover fix exists with primary sources
- Google Android XR tamper detection announced but no camera shutdown confirmed
- WIRED Gear desk framing asymmetry same journalist 15-day swing
- Financial context stated as correlation not causation
- Confounders documented

No em dashes allowed per project rule.
"""

import os
import yaml

JOURNALISTS_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "careers", "journalists.yaml")


def load_journalists():
    with open(JOURNALISTS_YAML, "r") as f:
        data = yaml.safe_load(f)
        # File structure is dict with key 'journalists' containing list
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


def test_mechanism_411_exists():
    entry = get_chokkattu()
    key = "mechanism_411_google_android_xr_tamper_detection_enforcement_gap"
    assert key in entry, f"{key} missing in Julian Chokkattu entry"
    mech = entry[key]
    assert mech["mechanism_id"] == 411
    assert mech["iteration"] == 411
    assert mech["iteration_type"] == "B"
    assert "2026-08-31" in str(mech["discovery_date"]) or "2026-08-31" in str(mech["iteration_time"])


def test_meta_july_7_tamper_proof_documented():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    meta = mech["meta_enforcement"]["july_7_2026_tamper_proof"]
    assert "2026-07-07" in meta["date"] or "2026-07-07" in str(meta.get("title", ""))
    assert "tamper" in meta["description"].lower() or "LED" in meta["description"]
    # Must have at least 3 source URLs
    assert len(meta["source_urls"]) >= 3
    # Must credit Victoria Song origin node
    assert "Victoria Song" in meta.get("journalist_credit", "") or "victoria" in meta.get("journalist_credit", "").lower()


def test_meta_aug_27_mid_recording_fix_documented():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    aug = mech["meta_enforcement"]["aug_27_2026_mid_recording_cover_fix"]
    assert "2026-08-27" in aug["date"]
    assert "cover" in aug["description"].lower()
    assert "Himel" in aug["description"] or "Threads" in aug["description"]
    assert len(aug["source_urls"]) >= 3


def test_google_android_xr_enforcement_gap():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    google = mech["google_android_xr_enforcement"]
    assert "tamper" in google["title"].lower()
    assert google["enforcement_gap"]["google_tamper_detection_announced"] is True
    assert google["enforcement_gap"]["google_camera_automatic_shutdown_confirmed"] is False
    assert google["enforcement_gap"]["google_technical_spec_published"] is False
    assert google["enforcement_gap"]["meta_camera_shutdown_on_block"] is True
    assert google["enforcement_gap"]["meta_camera_shutdown_on_tamper_destroy"] is True
    assert google["enforcement_gap"]["meta_camera_shutdown_on_mid_recording_cover"] is True
    # Inversion statement must exist
    assert "inversion" in google["enforcement_gap"]


def test_wired_gear_desk_framing_asymmetry():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    wired = mech["wired_gear_desk"]
    assert "Julian Chokkattu" in str(wired["journalists"])
    # Google I/O 2026 framing
    google_framing = wired["google_io_2026_framing"]
    assert "Nano Banana" in str(google_framing["live_blog_examples"]) or "bananas" in str(google_framing["live_blog_examples"]).lower()
    assert google_framing["surveillance_vocabulary"] == 0
    # Meta Business Wars framing
    meta_framing = wired["meta_business_wars_framing"]
    assert "mass surveillance" in meta_framing["language"] or "mass surveillance" in str(meta_framing)
    assert "Creep" in str(meta_framing["titles"]) or "Creep" in str(meta_framing)
    # Temporal gap 15 days
    assert "15 days" in wired["temporal_gap"] or "15-day" in wired["temporal_gap"]


def test_asymmetry_scorer_manual_illustrative_not_empirical():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    asym = mech["asymmetry_scorer_result"]
    # Must be labeled manual illustrative
    assert "MANUAL_ILLUSTRATIVE" in asym["label"] or "MANUAL" in str(asym.get("target_scores_MANUAL_ILLUSTRATIVE"))
    assert asym["p_value"] == "NOT_CALCULATED - no observed corpus"
    assert asym["significant"] is False
    assert asym["empirical_validation_required"] is True
    assert "Illustrative only" in asym["methodology"] or "illustrative" in asym["methodology"].lower()
    # Delta must be negative (Meta more adversarial)
    assert asym["delta_MANUAL_ILLUSTRATIVE"] < 0
    # Must warn do not claim statistical significance
    assert "Do not claim statistical significance" in asym["methodology"] or "Requires VADER" in asym["methodology"]


def test_financial_context_correlation_not_causation():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    fin = mech["financial_context_correlation_not_causation"]
    # Google relationship - minimal verified claims only per quality audit
    assert fin["google_condé_nast_relationship"]["google_is_android_xr_platform_provider"] is True
    assert fin["google_condé_nast_relationship"]["samsung_is_google_android_xr_hardware_partner"] is True
    # Sources must exist for platform provider claim
    assert "google_is_android_xr_platform_provider_sources" in fin["google_condé_nast_relationship"]
    # Meta relationship - 0 deals documented
    assert fin["meta_condé_nast_relationship"]["meta_content_licensing_deal_with_wired"] == 0 or fin["meta_condé_nast_relationship"]["meta_content_licensing_deal_with_wired"] is False
    # Conflated claims removed - should NOT have vox_media or samsung_advertiser_rank without source
    # Quality audit removed unsupported programmatic claims
    assert "vox_media_depends_on_google_programmatic" not in fin["google_condé_nast_relationship"] or fin["google_condé_nast_relationship"].get("vox_media_depends_on_google_programmatic") is None
    # Non-causal language required
    assert "non_causal_language" in fin
    assert "do not prove editorial influence" in fin["non_causal_language"].lower() or "correlation" in fin["non_causal_language"].lower()
    assert "Correlation does not imply causation" in fin["non_causal_language"] or "Correlation does not imply" in fin["non_causal_language"] or "correlation not causation" in fin["non_causal_language"].lower()


def test_confounders_documented():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    confs = mech["confounders"]
    assert len(confs) >= 5
    # Must have STRONG confounders for product stage and market share
    strong_count = sum(1 for c in confs if "[STRONG]" in c)
    assert strong_count >= 2
    # Must discuss product stage, market share, beat assignment, form factor
    conf_text = " ".join(confs).lower()
    assert "product stage" in conf_text
    assert "market share" in conf_text or "installed base" in conf_text
    assert "beat assignment" in conf_text
    assert "form factor" in conf_text


def test_confounding_adjustment():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    adj = mech["confounding_adjustment"]
    assert adj["raw_delta"] == 0.74
    assert adj["total_adjustment"] > 0
    # pytest.approx replaced with manual tolerance to avoid pytest dependency
    assert abs(adj["adjusted_delta"] - 0.46) < 0.01
    assert "moderate" in adj["interpretation"].lower()


def test_source_urls_present():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    urls = mech["source_urls"]
    # Must have at least 8 URLs covering both Meta and Google
    assert len(urls) >= 8
    # Must include eweek for Google
    assert any("eweek.com" in u for u in urls)
    # Must include gizmodo for Meta tamper
    assert any("gizmodo.com" in u for u in urls)
    # Must include androidauthority for Samsung/Google
    assert any("androidauthority.com" in u for u in urls)
    # Must include fastcompany or wsj for Meta pervert glasses framing
    assert any("fastcompany.co.za" in u or "wsj.com" in u for u in urls)


def test_no_em_dashes_in_mechanism():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    # Check pattern field does not contain em dash character
    pattern = mech["pattern"]
    assert "—" not in pattern, "Em dash found in pattern - violates project rule"
    # Check a few other string fields
    for key in ["discovery_date", "iteration_time"]:
        val = str(mech.get(key, ""))
        assert "—" not in val


def test_cross_references_include_prior_mechanisms():
    mech = get_chokkattu()["mechanism_411_google_android_xr_tamper_detection_enforcement_gap"]
    refs = mech["cross_references"]
    # Must reference prior pricing asymmetry and samsung mechanisms
    assert 354 in refs
    assert 362 in refs
    assert 207 in refs
    # Must reference 410 FT mechanism
    assert 410 in refs
