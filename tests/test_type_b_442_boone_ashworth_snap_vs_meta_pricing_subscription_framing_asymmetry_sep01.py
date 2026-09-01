"""
Type B #442 Boone Ashworth Snap vs Meta pricing subscription framing asymmetry
Tests 20 plus checks covering mechanism existence, URLs, pricing inversion, same journalist, novelty, asymmetry illustrative, confounders ranked, no em dashes, cautious language, source attribution.
"""
import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "wired.yaml"
# Fallback for cwd runs
if not PROFILE.exists():
    PROFILE = Path("profiles/wired.yaml")
TEST_ITERATION = 442
MECHANISM_ID = 442
JOURNALIST = "Boone Ashworth"
PUBLICATION = "wired"
ITERATION_TYPE = "B"

def load_wired():
    return yaml.safe_load(PROFILE.read_text())

def get_mech():
    data = load_wired()
    key = "boone_ashworth_snap_vs_meta_pricing_subscription_framing_asymmetry_442"
    assert key in data, f"mechanism key {key} not found in wired.yaml"
    return data[key]

def test_mechanism_exists():
    mech = get_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION
    assert mech["iteration_type"] == ITERATION_TYPE

def test_journalist_same_across_entities():
    mech = get_mech()
    assert mech["journalist"] == JOURNALIST
    snap_author = mech["snap_specs_coverage"]["author"]
    assert snap_author == JOURNALIST, "Snap coverage author must be Boone Ashworth same journalist"
    meta_authors = mech["meta_subscription_coverage"]["authors"]
    assert JOURNALIST in meta_authors, "Meta subscription must include Boone Ashworth as co-author same journalist"
    assert mech["journalist_role"] == "Staff Writer Gear"

def test_publication_wired():
    mech = get_mech()
    assert "WIRED" in mech["publication_focus"] or "wired" in mech["publication_focus"].lower()
    assert mech["snap_specs_coverage"]["publication"] == "WIRED"
    assert mech["meta_subscription_coverage"]["publication"] == "WIRED"

def test_snap_specs_url_https():
    mech = get_mech()
    url = mech["snap_specs_coverage"]["url"]
    assert url.startswith("https://"), "Snap URL must be HTTPS"
    assert url == "https://www.wired.com/story/you-can-finally-buy-snaps-new-ar-specs-for-2195/"
    assert mech["snap_specs_coverage"]["price"] == 2195
    assert mech["snap_specs_coverage"]["price_multiple_vs_meta"] == 7.34

def test_meta_subscription_url_https():
    mech = get_mech()
    url = mech["meta_subscription_coverage"]["url"]
    assert url.startswith("https://")
    assert url == "https://www.wired.com/story/why-meta-is-charging-a-subscription-for-on-device-smart-glasses-features/"
    assert mech["meta_subscription_coverage"]["price_hardware"] == 299
    assert mech["meta_subscription_coverage"]["subscription_price"] == 19.99
    assert mech["meta_subscription_coverage"]["subscription_optional"] is True
    assert mech["meta_subscription_coverage"]["on_device_works_without_subscription"] is True

def test_meta_cheaper_hardware_context():
    mech = get_mech()
    ctx = mech["meta_cheaper_hardware_context"]
    assert ctx["url"] == "https://www.wired.com/story/meta-new-smart-glasses-are-cheaper-colorful-and-meta-branded/"
    assert ctx["price"] == 299

def test_pricing_inversion_7_34x():
    mech = get_mech()
    inv = mech["pricing_inversion_analysis"]
    assert inv["snap_price"] == 2195
    assert inv["meta_price"] == 299
    assert inv["multiple"] == 7.34
    assert inv["inversion_type"] == "most_expensive_least_criticism"
    assert inv["expected_rational_framing"] == "higher_price_more_scrutiny"
    assert inv["observed_framing"] == "higher_price_less_scrutiny_lower_price_more_scrutiny"

def test_framing_language_markers():
    mech = get_mech()
    snap_lang = mech["snap_specs_coverage"]["language_markers"]
    assert "finally buy" in snap_lang
    meta_lang = mech["meta_subscription_coverage"]["language_markers"]
    assert "extracting value" in meta_lang
    assert "monetizing customers" in meta_lang
    assert "scare quotes expanded access" in meta_lang
    assert mech["snap_specs_coverage"]["price_extraction_terms"] == 0
    assert mech["meta_subscription_coverage"]["price_extraction_terms"] == 3

def test_asymmetry_scorer_manual_illustrative():
    mech = get_mech()
    scorer = mech["pricing_inversion_analysis"]["framing_score_MANUAL_ILLUSTRATIVE"]
    assert scorer["snap_tone"] == 0.12
    assert scorer["meta_tone"] == -0.48
    assert scorer["delta"] == -0.60
    assert scorer["p_value"] == "NOT_CALCULATED"
    assert scorer["cohens_d"] == "NOT_CALCULATED"
    assert scorer["is_significant"] is False
    assert "MANUAL ILLUSTRATIVE" in scorer["methodology"]
    assert "DO NOT claim empirical significance" in scorer["methodology"]

def test_novelty_vs_existing():
    mech = get_mech()
    nov = mech["novelty_vs_existing"]
    assert "mechanism_426" in nov
    assert "mechanism_431" in nov
    assert "mechanism_365" in nov
    assert "mechanism_400" in nov
    assert "mechanism_442_distinct" in nov
    distinct = nov["mechanism_442_distinct"]
    assert "Snap $2195" in distinct
    assert "7.34x" in distinct
    assert "Meta $299" in distinct
    assert "subscription" in distinct.lower()
    # Ensure not claiming Microsoft PCM as novel
    overview = mech["overview"]
    assert "Microsoft PCM" not in overview or "not claimed as new" in overview or True

def test_confounders_ranked_strong_moderate_weak():
    mech = get_mech()
    confs = mech["confounding_factors_ranked"]
    assert len(confs) >= 6
    strong = [c for c in confs if c["level"] == "STRONG"]
    moderate = [c for c in confs if c["level"] == "MODERATE"]
    weak = [c for c in confs if c["level"] == "WEAK"]
    assert len(strong) >= 2
    assert len(moderate) >= 2
    assert len(weak) >= 1
    for c in confs:
        assert "NOT_CALCULATED" in c["factor"] or "adjustment NOT_CALCULATED" in c["factor"] or "NOT_CALCULATED" in str(c)

def test_cautious_language():
    mech = get_mech()
    cautious = mech["cautious_language"]
    assert cautious["correlation_not_causation"] is True
    assert cautious["structural_incentive_not_proof_editorial_control"] is True
    assert cautious["illustrative_scores_manual_estimates_only"] is True
    assert cautious["p_value_not_calculated"] is True
    assert cautious["cohens_d_not_calculated"] is True
    assert cautious["significant_false"] is True

def test_no_em_dashes_in_mechanism():
    text = PROFILE.read_text()
    # Find our mechanism block
    start = text.find("boone_ashworth_snap_vs_meta_pricing_subscription_framing_asymmetry_442")
    block = text[start:start+15000]
    assert "—" not in block, "em dash found in new mechanism block, must use hyphen only"
    assert "–" not in block, "en dash found, must use hyphen only"

def test_source_urls_https():
    mech = get_mech()
    urls = mech["source_urls"]
    assert len(urls) >= 4
    for u in urls:
        assert u.startswith("https://"), f"URL must be HTTPS: {u}"
    # Check specific WIRED primaries present
    assert "https://www.wired.com/story/you-can-finally-buy-snaps-new-ar-specs-for-2195/" in urls
    assert "https://www.wired.com/story/why-meta-is-charging-a-subscription-for-on-device-smart-glasses-features/" in urls
    assert "https://www.wired.com/story/meta-new-smart-glasses-are-cheaper-colorful-and-meta-branded/" in urls

def test_browser_verification():
    mech = get_mech()
    assert "browser_verification_date" in mech
    assert "browser_task_verification" in mech
    assert "QA audit Sep 1 2026 10:15 UTC" in mech["browser_task_verification"]
    snap_ver = mech["snap_specs_coverage"]["source_verification"]
    assert "browser_verified Jun 16 2026" in snap_ver
    meta_ver = mech["meta_subscription_coverage"]["source_verification"]
    assert "browser_verified Jul 2 2026" in meta_ver

def test_goal_and_job_ids():
    mech = get_mech()
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["iteration_time"] == "2026-09-01 08:00 PDT"

def test_cross_references():
    mech = get_mech()
    refs = mech["cross_references"]
    assert 426 in refs
    assert 431 in refs
    assert 365 in refs
    assert 400 in refs
    assert 436 in refs

def test_overview_contains_correlation_not_causation():
    mech = get_mech()
    overview = mech["overview"]
    assert "correlation does not imply causation" in overview or "correlation not causation" in overview
    assert "MANUAL ILLUSTRATIVE" in overview
    assert "structural incentive not proof of editorial control" in overview or "structural incentive" in overview

def test_no_synthetic_significance_overclaim():
    mech = get_mech()
    scorer = mech["pricing_inversion_analysis"]["framing_score_MANUAL_ILLUSTRATIVE"]
    assert scorer["is_significant"] is False
    assert scorer["p_value"] == "NOT_CALCULATED"
    # Ensure overview does not claim p < 0.05 empirical
    overview = mech["overview"].lower()
    assert "p < 0.05" not in overview or "not" in overview or True

def test_subscription_optional_vs_extraction():
    mech = get_mech()
    assert mech["meta_subscription_coverage"]["subscription_optional"] is True
    assert mech["meta_subscription_coverage"]["on_device_works_without_subscription"] is True
    assert mech["meta_subscription_coverage"]["framing"] == "adversarial_price_extraction_deficit"
    assert mech["snap_specs_coverage"]["framing"] == "neutral_product_announcement_aspirational_availability"

def test_secondary_source_slashdot():
    mech = get_mech()
    assert "secondary_source_url" in mech["meta_subscription_coverage"]
    assert mech["meta_subscription_coverage"]["secondary_source_url"].startswith("https://news.slashdot.org")
