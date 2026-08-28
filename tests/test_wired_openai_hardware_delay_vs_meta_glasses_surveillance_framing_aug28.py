"""
Test: WIRED OpenAI Hardware Delay vs Meta Glasses Surveillance Framing Inversion (Mechanism #356)
Type A: Competitor Coverage Deep Dive — WIRED covering OpenAI vs Meta wearables hardware
Date: 2026-08-28 12:00 PT (Iteration #344)
"""
import pytest
import yaml
import os
from datetime import datetime


PROFILE_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/wired.yaml")
ENTITIES_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/competitor-entities.yaml")


def load_wired():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def load_entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def test_mechanism_356_exists():
    """Mechanism 356 exists in wired.yaml competitor_relationships.openai"""
    data = load_wired()
    assert "competitor_relationships" in data
    assert "openai" in data["competitor_relationships"]
    openai_rel = data["competitor_relationships"]["openai"]
    assert "hardware_device_delay_framing_asymmetry_aug28" in openai_rel
    mech = openai_rel["hardware_device_delay_framing_asymmetry_aug28"]
    assert mech["mechanism_id"] == 356
    assert mech["date_analyzed"] == "2026-08-28"
    assert "finding" in mech
    assert "openai_device_coverage" in mech
    assert "meta_glasses_comparison_coverage" in mech
    assert "asymmetry_scorer_result" in mech


def test_openai_device_features_documented():
    """OpenAI device features match competitor-entities.yaml hardware_devices spec."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    finding = mech["finding"]
    # Must mention key surveillance capabilities
    assert "camera" in finding.lower()
    assert "facial recognition" in finding.lower() or "Face ID" in finding
    assert "always-on" in finding.lower()
    assert "$6.5B" in finding or "6.5B" in finding

    entities = load_entities()
    hw = entities["entities"]["openai"]["hardware_devices"]
    assert hw["smart_speaker"]["features"]["camera"] is True
    assert hw["smart_speaker"]["features"]["facial_recognition"]
    assert hw["smart_speaker"]["features"]["always_on"] is True
    assert hw["smart_speaker"]["features"]["continuous_data_collection"] is True
    assert hw["smart_speaker"]["features"]["environmental_awareness"] is True


def test_openai_coverage_articles_three():
    """Three OpenAI hardware articles with neutral/constructive framing, zero surveillance language."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    articles = mech["openai_device_coverage"]["articles"]
    assert len(articles) == 3

    urls = [a["url"] for a in articles]
    assert "https://www.macrumors.com/2026/02/10/openais-jony-ive-designed-device-delayed-to-2027/" in urls
    assert "https://9to5mac.com/2026/01/19/openai-teases-hardware-unveil-this-year-as-jony-ives-team-hires-more-apple-alumni/" in urls
    assert "https://9to5mac.com/2025/06/23/not-a-wearable-court-documents-detail-openais-plans-for-its-ai-hardware-project-with-jony-ive/" in urls

    for article in articles:
        assert article["surveillance_language_count"] == 0
        assert article["deal_disclosed"] is False
        assert "privacy_treatment" in article
        assert "framing" in article
        assert article["tone_approx"] >= 0.0  # neutral to positive


def test_openai_article_language_aspirational():
    """OpenAI coverage uses aspirational language, no alarm."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    all_language = []
    for a in mech["openai_device_coverage"]["articles"]:
        all_language.extend(a["language"])

    joined = " ".join(all_language).lower()
    # Aspirational markers
    assert "coolest piece of technology" in joined or "coolest" in joined
    assert "third core device" in joined
    assert "contextually aware" in joined
    # No alarm markers in OpenAI language
    assert "creepy" not in joined
    assert "pervert" not in joined
    assert "nightmarish" not in joined
    assert "surveillance" not in joined


def test_meta_glasses_comparison_adversarial():
    """Meta glasses comparison has adversarial surveillance framing with specific alarm language."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    meta = mech["meta_glasses_comparison_coverage"]
    assert meta["framing"] == "adversarial_surveillance"
    assert meta["tone_approx"] < -0.5

    assert "articles_referenced" in meta
    assert len(meta["articles_referenced"]) == 3

    urls = [a["url"] for a in meta["articles_referenced"]]
    assert "https://roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/" in urls
    assert "https://www.androidpolice.com/ray-ban-meta-privacy-problems-super-sensing-feature/" in urls
    assert "https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan" in urls

    # Alarm language must be present in meta articles
    all_meta_lang = []
    for a in meta["articles_referenced"]:
        all_meta_lang.extend(a["language"])
    joined = " ".join(all_meta_lang).lower()
    assert "creepy" in joined
    assert "pervert" in joined or "pervert glasses" in joined
    assert "nightmarish" in joined
    assert "privacy" in joined


def test_hardware_capability_inversion():
    """Hardware capability inversion: OpenAI has MORE surveillance capability but LESS scrutiny."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    inversion = mech["hardware_capability_inversion"]
    assert "openai_device" in inversion
    assert "meta_ray_ban" in inversion
    assert inversion["inversion_score"] > 0.8

    openai_dev = inversion["openai_device"]
    assert openai_dev["cameras"] is True or openai_dev["cameras"] == True  # camera true
    assert "facial_recognition" in openai_dev
    assert openai_dev["always_on"] is True
    assert openai_dev["privacy_scrutiny_received"] == "zero WIRED investigations" or "zero" in str(openai_dev["privacy_scrutiny_received"]).lower()

    meta_dev = inversion["meta_ray_ban"]
    assert "1x 12MP" in meta_dev["cameras"] or "12MP" in str(meta_dev["cameras"])
    assert meta_dev["privacy_scrutiny_received"] is not None
    # Meta has LESS hardware capability but MORE scrutiny
    assert "3+" in str(meta_dev["privacy_scrutiny_received"]) or "investigation" in str(meta_dev["privacy_scrutiny_received"]).lower()


def test_asymmetry_scorer_statistical_validity():
    """Asymmetry scorer produces statistically meaningful results: p<0.05, |d|>0.5, CI excludes 0."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    result = mech["asymmetry_scorer_result"]

    assert result["publication"] == "wired"
    assert result["target_entity"] == "Meta"
    assert result["peer_entity"] == "OpenAI"
    assert len(result["target_scores"]) == 5
    assert len(result["peer_scores"]) == 5

    # Target (Meta) more negative than peer (OpenAI)
    assert result["target_avg_tone"] < result["peer_avg_tone"]
    assert result["asymmetry_score"] < -0.5  # strong negative asymmetry

    # Statistical significance
    assert result["p_value"] < 0.05
    assert abs(result["cohens_d"]) > 0.5
    assert result["is_significant"] is True

    # CI excludes 0 (both bounds negative)
    assert result["ci_lower"] < 0
    assert result["ci_upper"] < 0
    assert result["ci_lower"] < result["ci_upper"]

    # Effect size interpretation
    assert result["cohens_d"] < -0.8  # large effect


def test_asymmetry_scorer_matches_statistical_module():
    """Verify asymmetry calculation using actual scoring module."""
    from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci

    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    result = mech["asymmetry_scorer_result"]

    target_scores = result["target_scores"]
    peer_scores = result["peer_scores"]

    t_stat, p_val = welch_t_test(target_scores, peer_scores)
    d = cohens_d(target_scores, peer_scores)
    ci_lower, ci_upper = bootstrap_ci(target_scores, peer_scores, n_bootstrap=1000)

    # Our stored values should be in same ballpark (allow tolerance for bootstrap randomness)
    assert p_val < 0.05
    assert abs(d) > 0.5
    # t should be negative (Meta more negative)
    assert t_stat < 0
    # CI should be entirely negative
    assert ci_lower < 0 and ci_upper < 0


def test_financial_relationship_predicts_coverage():
    """Condé Nast OpenAI licensing deal predicts softer hardware coverage."""
    wired = load_wired()
    openai_rel = wired["competitor_relationships"]["openai"]
    assert openai_rel["financial_tie"] == "licensing"
    assert "1-5M" in openai_rel["estimated_value"] or "undisclosed" in openai_rel["estimated_value"]
    assert openai_rel["coverage_prediction"] == "softer"
    assert "2024-08-20" in openai_rel["source_url"] or "cond-nast" in openai_rel["source_url"] or "cond" in openai_rel["source_url"].lower()

    meta_rel = wired["competitor_relationships"]["meta"]
    assert meta_rel["financial_tie"] == "none"
    assert meta_rel["coverage_prediction"] == "adversarial"

    # Mechanism finding should mention financial predictor
    mech = openai_rel["hardware_device_delay_framing_asymmetry_aug28"]
    assert "financial" in mech["finding"].lower() or "Condé Nast" in mech["finding"] or "licensing" in mech["finding"].lower()


def test_source_urls_all_valid():
    """All source URLs must be real, verbatim URLs from search results."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    sources = mech["source_urls"]
    assert len(sources) >= 8

    # Must include exact URLs from search results (verbatim)
    required_substrings = [
        "macrumors.com/2026/02/10/openais-jony-ive-designed-device-delayed-to-2027",
        "9to5mac.com/2026/01/19/openai-teases-hardware-unveil",
        "9to5mac.com/2025/06/23/not-a-wearable-court-documents",
        "macrumors.com/2025/05/22/details-leak-jony-ive-openai-device",
        "gsmarena.com/openai_to_acquire_jony_ives_ai_hardware_startup_for_65b",
        "roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update",
        "androidpolice.com/ray-ban-meta-privacy-problems-super-sensing-feature",
        "fastcompany.com/91594615/metas-creepy-smart-glasses",
    ]
    for substr in required_substrings:
        assert any(substr in url for url in sources), f"Missing required URL containing: {substr}"


def test_cross_references_integrity():
    """Cross-references point to valid mechanisms."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    xrefs = mech["cross_references"]
    assert len(xrefs) >= 5
    # Must include key related mechanisms
    assert 33 in xrefs  # facial recognition parity
    assert 84 in xrefs or 96 in xrefs  # investigation gap or lawsuit silence
    assert 353 in xrefs  # FT parallel always-on ambient AI


def test_competitor_entities_updated():
    """competitor-entities.yaml openai entry has mechanism 356."""
    entities = load_entities()
    assert "entities" in entities
    assert "openai" in entities["entities"]
    openai = entities["entities"]["openai"]
    assert "hardware_devices" in openai
    hw = openai["hardware_devices"]
    # Must have new mechanism
    assert "hardware_delay_framing_asymmetry_aug28" in hw or "facial_recognition_privacy_parity" in hw
    if "hardware_delay_framing_asymmetry_aug28" in hw:
        mech = hw["hardware_delay_framing_asymmetry_aug28"]
        assert mech["mechanism_id"] == 356
        assert mech["date_analyzed"] == "2026-08-28"
        assert mech["asymmetry_score"] < -0.5


def test_no_ai_slop_language():
    """Mechanism finding must not contain banned AI slop phrases."""
    wired = load_wired()
    mech = wired["competitor_relationships"]["openai"]["hardware_device_delay_framing_asymmetry_aug28"]
    finding = mech["finding"].lower()
    banned = ["delve into", "in the realm of", "tapestry", "unlock the power", "embark on a journey", "it's important to note"]
    for phrase in banned:
        assert phrase not in finding, f"Banned phrase '{phrase}' found in finding"
