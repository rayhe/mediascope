"""
Type A Iteration #440 — WIRED x OpenAI Unshipped Hardware vs Meta Dormant NameTag
Activation-Status Evidentiary Standard Asymmetry

Validates #440 distinct from #33 and #359, URLs, framing, asymmetry illustrative,
no em dashes, no synthetic significance overclaim, confounders ranked, deal disclosure.

Iteration #440 2026-09-01 06:00 PDT Type A Competitor Coverage Deep Dive
"""

import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "wired.yaml"

def load_profile():
    with open(PROFILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_wired_440_mechanism_exists():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    key = "activation_status_evidentiary_standard_asymmetry_440"
    assert key in openai, f"Missing {key}"
    it = openai[key]
    assert it["mechanism_id"] == 440
    assert it["iteration"] == 440
    assert it["type"].startswith("Type A")

def test_wired_440_urls_verified():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    urls = it["source_urls"]
    assert "https://www.wired.com/story/openai-drops-io-branding-hardware-devices/" in urls
    assert "https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/" in urls
    assert "https://cybernoz.com/meta-tapped-a-pentagon-supplier-to-prototype-face-recognition-for-its-glasses/" in urls
    assert "https://www.phonearena.com/news/OpenAIs-secret-gadget-is-getting-delayed-until-next-year_id178098" in urls
    # Primary WIRED source inside openai_unshipped_hardware_coverage
    primary = it["openai_unshipped_hardware_coverage"]["primary_wired_source"]
    assert primary["url"] == "https://www.wired.com/story/openai-drops-io-branding-hardware-devices/"
    assert primary["framing"] == "neutral_business_delay"
    assert primary["deal_disclosed"] is False

def test_wired_440_activation_status_fields():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    # OpenAI status
    openai_cov = it["openai_unshipped_hardware_coverage"]
    assert openai_cov["activation_status"].startswith("unshipped")
    assert "no packaging" in openai_cov["primary_wired_source"]["language_evidence"][2].lower() or "packaging" in " ".join(openai_cov["primary_wired_source"]["language_evidence"]).lower()
    assert openai_cov["primary_wired_source"]["surveillance_language_count"] == 0
    # Meta status
    meta_cov = it["meta_dormant_nametag_coverage"]
    assert "dormant" in meta_cov["activation_status"]
    assert "deleted" in meta_cov["activation_status"].lower() or "removed" in meta_cov["activation_status"].lower()
    primary_meta = meta_cov["primary_wired_source"]
    assert primary_meta["framing"] == "adversarial_dormant_surveillance_infrastructure"
    assert "Silently Added" in primary_meta["language_evidence"]

def test_wired_440_evidentiary_comparison():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    comp = it["activation_status_evidentiary_comparison"]
    assert comp["openai"]["surveillance_vocab"] == "0 terms" or comp["openai"]["surveillance_vocab"] == 0 or "0" in str(comp["openai"]["surveillance_vocab"])
    assert comp["meta"]["surveillance_vocab"] != "0 terms"
    assert "7+" in str(comp["meta"]["surveillance_vocab"]) or "biometric" in str(comp["meta"]["surveillance_vocab"]).lower()

def test_wired_440_novelty_vs_33_359():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    novelty = it["novelty_vs_33_359"]
    assert "mechanism_33" in novelty
    assert "mechanism_359" in novelty
    assert "mechanism_440_distinct" in novelty
    distinct = novelty["mechanism_440_distinct"].lower()
    assert "evidentiary" in distinct or "activation-status" in distinct
    assert "capability" not in distinct or "adds evidentiary" in distinct or "evidentiary" in distinct

def test_wired_440_asymmetry_illustrative():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    scorer = it["asymmetry_scorer_result"]
    # All tones must be MANUAL ILLUSTRATIVE
    assert "MANUAL ILLUSTRATIVE" in scorer["target_avg_tone"] or "MANUAL ILLUSTRATIVE" in str(scorer["target_scores"])
    assert scorer["is_significant"] is False
    assert "not_calculated" in str(scorer["p_value"])
    assert "illustrative only" in scorer["methodology_note"].lower()
    assert "do not claim empirical significance" in scorer["methodology_note"].lower()

def test_wired_440_confounders_ranked():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    confs = it["confounders"]
    assert len(confs) >= 5
    strong = [c for c in confs if c.startswith("[STRONG]")]
    moderate = [c for c in confs if c.startswith("[MODERATE]")]
    weak = [c for c in confs if c.startswith("[WEAK]")]
    assert len(strong) >= 2, "Need at least 2 STRONG confounders"
    assert len(moderate) >= 2
    assert len(weak) >= 1
    # All must mention adjustment not_calculated
    for c in confs:
        assert "adjustment not_calculated" in c

def test_wired_440_no_em_dashes():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    import json
    blob = json.dumps(it, ensure_ascii=False)
    assert "\u2014" not in blob, "Em dash found in iteration 440 — banned"
    assert "--" not in blob or "not_calculated" in blob  # allow only in not_calculated? Actually double dash is not em dash but check
    # Ensure no em dash char

def test_wired_440_cautious_language():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    caut = it["cautious_language"].lower()
    assert "correlation does not imply causation" in caut
    assert "structural incentive" in caut
    assert "illustrative scores" in caut
    assert "empirical validation" in caut

def test_wired_440_source_attribution():
    data = load_profile()
    it = data["competitor_relationships"]["openai"]["activation_status_evidentiary_standard_asymmetry_440"]
    # Secondary corroboration must attribute WIRED
    secs = it["openai_unshipped_hardware_coverage"]["secondary_corroboration_attributing_wired"]
    for sec in secs:
        assert "attribution" in sec
        assert "wired" in sec["attribution"].lower()
    # Meta Rank One follow-up must attribute WIRED Jun 15
    rank = it["meta_dormant_nametag_coverage"]["rank_one_follow_up_attributing_wired"]
    assert "WIRED" in rank["attribution"] or "wired" in rank["attribution"].lower()
    assert rank["tone_approx"].startswith("MANUAL ILLUSTRATIVE") or "MANUAL ILLUSTRATIVE" in str(rank["tone_approx"])
