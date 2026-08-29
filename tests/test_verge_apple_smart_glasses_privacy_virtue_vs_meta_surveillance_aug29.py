"""
Mechanism #370: The Verge Apple Smart Glasses Privacy-Virtue Framing Inversion vs Meta Surveillance Alarm
Type A: Competitor Coverage Deep Dive (Aug 29, 2026 09:00 PT)
Publication: The Verge (PMC/PMX, acquired Jun 18, 2026)
Competitor: Apple (N50 smart glasses, WWDC 2027 delay for privacy)

FINDING: The Verge Apple smart glasses coverage uses privacy-VIRTUE framing (delaying to WWDC 2027
to prioritize privacy, testing three camera configs including camera-less, privacy restrictions that
mirror Meta's own Jul 7 2026 LED tamper-proof fix) while Meta's identical single-camera hardware
receives surveillance-alarm framing. Apple's device has MORE cameras (multiple) than Meta's single
12MP yet receives ZERO surveillance vocabulary.
"""

import yaml
from pathlib import Path

PROFILE_PATH = Path(__file__).parent.parent / "profiles" / "the-verge.yaml"

def load_profile():
    with open(PROFILE_PATH, 'r') as f:
        return yaml.safe_load(f)

def load_mech():
    profile = load_profile()
    # Mechanism lives under cross_entity_coverage_analysis
    ceca = profile.get("cross_entity_coverage_analysis", {})
    assert ceca, "cross_entity_coverage_analysis missing"
    key = "apple_smart_glasses_privacy_virtue_vs_meta_surveillance_aug29"
    assert key in ceca, f"Mechanism {key} not found in cross_entity_coverage_analysis"
    return ceca[key]

def test_profile_exists():
    assert PROFILE_PATH.exists(), f"Profile not found at {PROFILE_PATH}"

def test_mechanism_370_exists():
    mech = load_mech()
    assert mech is not None

def test_mechanism_id():
    mech = load_mech()
    assert mech["mechanism_id"] == 370

def test_publication_and_competitor():
    mech = load_mech()
    assert mech["publication"] == "The Verge"
    assert mech["competitor"] == "Apple"

def test_apple_coverage_count():
    mech = load_mech()
    assert "apple_coverage_2026" in mech
    assert len(mech["apple_coverage_2026"]) >= 2, "Need at least 2 Apple coverage examples"
    assert len(mech["apple_coverage_2026"]) <= 4, "Keep to 2-3 recent articles"

def test_apple_articles_have_urls():
    mech = load_mech()
    for article in mech["apple_coverage_2026"]:
        assert "url" in article, f"Missing URL for {article.get('title')}"
        assert article["url"].startswith("http"), f"Invalid URL {article['url']}"
        assert "title" in article
        assert "framing" in article

def test_meta_comparison_exists():
    mech = load_mech()
    assert "meta_comparison_coverage" in mech
    assert len(mech["meta_comparison_coverage"]) >= 1

def test_hardware_inversion():
    mech = load_mech()
    assert "hardware_capability_inversion" in mech
    inv = mech["hardware_capability_inversion"]
    assert "apple_device" in inv
    assert "meta_device" in inv
    assert "inversion_score" in inv
    assert inv["inversion_score"] >= 0.7, "Inversion score should be high (>0.7) for this mechanism"

def test_inversion_cameras():
    mech = load_mech()
    inv = mech["hardware_capability_inversion"]
    apple_cams = str(inv["apple_device"]["cameras"]).lower()
    assert "multiple" in apple_cams or "2" in apple_cams or "dual" in apple_cams, "Apple should have multiple cameras"
    meta_cams = str(inv["meta_device"]["cameras"]).lower()
    assert "single" in meta_cams or "12mp" in meta_cams or "1x" in meta_cams

def test_asymmetry_scorer_exists():
    mech = load_mech()
    assert "asymmetry_scorer_result" in mech
    scorer = mech["asymmetry_scorer_result"]
    assert "target_scores" in scorer
    assert "peer_scores" in scorer
    assert "asymmetry_score" in scorer
    assert scorer["asymmetry_score"] < 0, "Meta should have more negative tone than Apple"

def test_asymmetry_statistical_validity():
    mech = load_mech()
    scorer = mech["asymmetry_scorer_result"]
    assert "p_value" in scorer
    assert scorer["p_value"] < 0.05, "Should be statistically significant"
    assert "cohens_d" in scorer
    assert abs(scorer["cohens_d"]) > 0.8, "Should have large effect size"
    assert "confidence_interval_95" in scorer
    ci = scorer["confidence_interval_95"]
    assert ci[0] < 0 and ci[1] < 0, "CI should exclude 0 and be negative (Meta more negative)"
    assert ci[0] < ci[1]

def test_cross_references():
    mech = load_mech()
    assert "cross_references" in mech
    refs = mech["cross_references"]
    ref_ids = [r["mechanism_id"] if isinstance(r, dict) else r for r in refs]
    # Should reference key related mechanisms
    assert 359 in ref_ids or any(str(r).find("359") >= 0 for r in refs) or len(ref_ids) >= 3

def test_source_urls():
    mech = load_mech()
    assert "source_urls" in mech
    urls = mech["source_urls"]
    assert len(urls) >= 5, "Need at least 5 source URLs"
    for url in urls:
        assert url.startswith("http"), f"Invalid URL {url}"

def test_financial_architecture():
    mech = load_mech()
    assert "financial_architecture" in mech
    fin = mech["financial_architecture"]
    assert len(fin) >= 2, "Should have multiple financial incentive layers"

def test_finding_summary():
    mech = load_mech()
    assert "finding_summary" in mech
    assert len(mech["finding_summary"]) > 100, "Finding summary should be substantive"

def test_editorial_lane_assignment():
    mech = load_mech()
    assert "editorial_lane_assignment_extension" in mech
    lane = mech["editorial_lane_assignment_extension"]
    assert "pattern" in lane or isinstance(lane, dict)

def test_confounders():
    mech = load_mech()
    assert "confounding_factors" in mech
    assert len(mech["confounding_factors"]) >= 2, "Should document confounders"

def test_asymmetry_scorer_module():
    """Validate that the asymmetry scorer produces expected results for this mechanism's tone arrays"""
    from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci
    target_scores = [-0.35, -0.45, -0.40, -0.38, -0.42]
    peer_scores = [0.12, 0.25, 0.18, 0.15, 0.20]
    t_stat, p_val = welch_t_test(target_scores, peer_scores)
    d = cohens_d(target_scores, peer_scores)
    ci_lower, ci_upper = bootstrap_ci(target_scores, peer_scores, n_bootstrap=1000)
    assert p_val < 0.05, f"p={p_val} should be <0.05"
    assert abs(d) > 0.8, f"d={d} should be large effect"
    assert ci_lower < 0 and ci_upper < 0, f"CI [{ci_lower}, {ci_upper}] should exclude 0 and be negative"
    # Asymmetry score is target_avg - peer_avg
    import numpy as np
    asymmetry = float(np.mean(target_scores) - np.mean(peer_scores))
    assert asymmetry < -0.3, f"Asymmetry {asymmetry} should be strongly negative (Meta more negative)"

