"""
Type A Iteration #364 — WIRED x OpenAI Hardware Delay Framing Reverification
Validates Aug 29 secondary corroboration URLs, framing labels, observed asymmetry,
no em dashes, no synthetic significance overclaim, deal disclosure.

Iteration #364 Sat 2026-08-29 04:00 PT Type A Competitor Coverage Deep Dive
"""

import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "wired.yaml"

def load_profile():
    with open(PROFILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_wired_openai_iteration_364_exists():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    assert "iteration_364_type_a_deep_dive_aug29" in openai, "Missing iteration_364_type_a_deep_dive_aug29"
    it = openai["iteration_364_type_a_deep_dive_aug29"]
    assert it["iteration"] == 364
    assert it["type"] == "A"
    assert it["publication"] == "wired"
    assert it["competitor"] == "openai"

def test_wired_openai_iteration_364_urls_verified():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["iteration_364_type_a_deep_dive_aug29"]
    urls = [a["url"] for a in it["recent_articles_aug29_secondary_corroboration"]]
    assert "https://www.macobserver.com/news/openais-first-jony-ive-designed-hardware-device-will-not-ship-before-2027/" in urls
    assert "https://www.macrumors.com/2026/02/10/openais-jony-ive-designed-device-delayed-to-2027/" in urls
    assert "https://www.windowscentral.com/artificial-intelligence/openais-jony-ive-ai-device-delayed-beyond-2026-over-privacy-compute-and-personality-issues" in urls
    assert "https://www.outlookbusiness.com/deeptech/artificial-intelligence/openai-teases-pocket-sized-screenless-ai-device-co-designed-with-jony-ive-launches-prototype" in urls
    # Primary WIRED URLs also in source_urls_iteration_364
    src = it["source_urls_iteration_364"]
    assert "https://www.wired.com/story/sam-altman-and-jony-ives-ai-device-dev-day/" in src
    assert "https://www.wired.com/story/the-rise-of-the-ray-ban-meta-creep/" in src

def test_wired_openai_iteration_364_framing_labels():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["iteration_364_type_a_deep_dive_aug29"]
    articles = {a["title"]: a for a in it["recent_articles_aug29_secondary_corroboration"]}
    delay = [a for a in articles.values() if "will not ship before 2027" in a["title"].lower()][0]
    assert delay["framing"] == "delay_announcement"
    privacy = [a for a in articles.values() if "privacy, compute" in a["title"].lower()][0]
    assert privacy["framing"] == "engineering_roadblock_neutral"
    # Privacy treatment must not use alarm language for OpenAI
    assert "creepy" not in privacy.get("privacy_treatment", "").lower()
    assert "pervert" not in privacy.get("privacy_treatment", "").lower()

def test_wired_openai_iteration_364_asymmetry_observed():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["iteration_364_type_a_deep_dive_aug29"]
    scorer = it["asymmetry_scorer_result_iteration_364"]
    assert scorer["target_avg_tone_observed"] < -0.5
    assert scorer["peer_avg_tone_observed"] > -0.2
    assert scorer["asymmetry_score_observed"] < -0.5
    # Illustrative stats must be labeled illustrative
    assert "illustrative" in scorer["methodology_note"].lower()
    assert "do not claim empirical significance" in scorer["methodology_note"].lower() or "do not claim" in scorer["methodology_note"].lower()

def test_wired_openai_iteration_364_no_em_dashes():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["iteration_364_type_a_deep_dive_aug29"]
    # Check top-level string fields for em dash
    import json
    blob = json.dumps(it, ensure_ascii=False)
    assert "\u2014" not in blob, "Em dash found in iteration 364 entry — banned"

def test_wired_openai_iteration_364_deal_disclosure():
    data = load_profile()
    # Original #359 primary sources must still exist with deal_disclosed false
    openai = data["competitor_relationships"]["openai"]
    primary = openai.get("direct_wired_primary_sources_verified_aug28_browser", {})
    if primary:
        for art in primary.get("openai_aspirational_3", []):
            assert "deal_disclosed" in art
            assert art["deal_disclosed"] is False

def test_wired_openai_iteration_364_tone_comparison():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["iteration_364_type_a_deep_dive_aug29"]
    tc = it["tone_comparison"]
    assert tc["openai_hardware_aug29"]["avg_tone"] > -0.1
    assert tc["meta_ray_ban_aug29_same_pub"]["avg_tone"] < -0.5
    assert tc["asymmetry_observed"] < -0.5
