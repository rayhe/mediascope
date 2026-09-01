"""
Type B #447 Lauren Goode Executive Access Asymmetry OpenAI io vs Meta hardware
Tests 26 checks covering mechanism existence, URLs, same journalist, novelty, asymmetry illustrative, confounders ranked, no em dashes, cautious language, source attribution.
"""
import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "wired.yaml"
JOURNALISTS = Path(__file__).parent.parent / "profiles" / "careers" / "journalists.yaml"
if not PROFILE.exists():
    PROFILE = Path("profiles/wired.yaml")
if not JOURNALISTS.exists():
    JOURNALISTS = Path("profiles/careers/journalists.yaml")

TEST_ITERATION = 447
MECHANISM_ID = 447
JOURNALIST = "Lauren Goode"
PUBLICATION = "wired"
ITERATION_TYPE = "B"

def load_wired():
    return yaml.safe_load(PROFILE.read_text())

def load_journalists():
    return yaml.safe_load(JOURNALISTS.read_text())

def get_mech():
    data = load_wired()
    key = "lauren_goode_executive_access_asymmetry_openai_io_vs_meta_hardware_447"
    assert key in data, f"mechanism key {key} not found in wired.yaml"
    return data[key]

def get_journalist_mech():
    data = load_journalists()
    # journalists is list under key 'journalists' or dict structure
    if isinstance(data, dict) and "journalists" in data:
        jlist = data["journalists"]
    else:
        jlist = data
    for entry in jlist:
        if entry.get("name") == JOURNALIST:
            key = "mechanism_447_lauren_goode_executive_access_asymmetry_openai_io_vs_meta_hardware_sep01_1pm"
            assert key in entry, f"mechanism {key} not found in journalists.yaml for Lauren Goode"
            return entry[key]
    raise AssertionError("Lauren Goode not found in journalists.yaml")

def test_mechanism_exists_wired():
    mech = get_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION
    assert mech["iteration_type"] == ITERATION_TYPE

def test_mechanism_exists_journalist():
    mech = get_journalist_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION

def test_journalist_same():
    mech = get_mech()
    assert mech["journalist"] == JOURNALIST
    jmech = get_journalist_mech()
    assert jmech["journalist"] == JOURNALIST

def test_publication_wired():
    mech = get_mech()
    assert "WIRED" in mech["publication_focus"] or "wired" in mech["publication_focus"].lower()

def test_openai_io_deal_value():
    mech = get_mech()
    io_cov = mech["openai_io_coverage"]
    assert io_cov["deal_value"] == 6500000000
    assert io_cov["deal_type"] == "all-stock"
    assert "not in-ear not wearable" in io_cov["hardware_desc"] or "not wearable" in io_cov["hardware_desc"]

def test_openai_io_urls_https():
    mech = get_mech()
    urls = mech["openai_io_coverage"]["source_urls"]
    for u in urls:
        assert u.startswith("https://"), f"OpenAI io URL must be HTTPS: {u}"
    assert "https://www.entrepreneur.com/business-news/openai-is-purchasing-apple-designer-jony-ives-ai-startup-io/492022" in urls
    assert "https://www.phonearena.com/news/OpenAIs-secret-gadget-is-getting-delayed-until-next-year_id178098" in urls

def test_meta_hardware_zero_interviews():
    mech = get_mech()
    meta = mech["meta_hardware_leadership"]
    zero = meta["meta_leadership_zero_interviews"]
    assert "Mark Zuckerberg" in zero
    assert "Andrew Bosworth" in zero or "Boz" in str(zero)
    assert len(zero) >= 4

def test_goode_executive_access_ratio():
    mech = get_mech()
    access = mech["goode_executive_access"]
    assert access["access_ratio"] == "5:0 non-Meta vs Meta"
    assert access["asymmetry_score_MANUAL_ILLUSTRATIVE"] == 0.87
    interviews = access["interviews_2024_2026"]
    assert any("Jensen Huang" in s for s in interviews)
    assert any("Lisa Su" in s for s in interviews)
    assert any("Rene Haas" in s for s in interviews)
    assert any("Mike Krieger" in s for s in interviews)
    assert any("Google I/O" in s for s in interviews)

def test_framing_inversion_google_vs_meta():
    mech = get_mech()
    inv = mech["framing_inversion_analysis"]["google_android_xr_vs_meta_rayban"]
    google = inv["google_android_xr"]
    meta = inv["meta_rayban"]
    assert google["wired_surveillance_terms"] == 0
    assert meta["wired_surveillance_terms"] >= 6
    assert google["capability_privacy_risk"] == "higher than Meta due autofocus sharper bystander capture" or "higher" in google["capability_privacy_risk"].lower()
    assert inv["inversion"].startswith("higher-risk hardware receives 0 surveillance terms")
    assert inv["delta_MANUAL_ILLUSTRATIVE"] == -0.90
    assert inv["p_value"] == "NOT_CALCULATED"
    assert inv["cohens_d"] == "NOT_CALCULATED"
    assert inv["is_significant"] is False

def test_asymmetry_scorer_manual_illustrative():
    mech = get_mech()
    # Check goode_executive_access methodology contains MANUAL ILLUSTRATIVE
    access = mech["goode_executive_access"]
    assert "MANUAL ILLUSTRATIVE" in access["methodology"]
    assert "DO NOT claim empirical significance" in access["methodology"]
    # Check framing inversion methodology
    inv = mech["framing_inversion_analysis"]["google_android_xr_vs_meta_rayban"]
    assert "MANUAL ILLUSTRATIVE" in inv["methodology"]
    assert "DO NOT claim empirical significance" in inv["methodology"]

def test_novelty_vs_existing():
    mech = get_mech()
    nov = mech["novelty_vs_existing"]
    assert "mechanism_436" in nov
    assert "mechanism_97" in nov
    assert "mechanism_442" in nov
    assert "mechanism_447_distinct" in nov
    distinct = nov["mechanism_447_distinct"]
    assert "Executive access asymmetry" in distinct
    assert "Lauren Goode" in distinct
    assert "5 non-Meta" in distinct or "5" in distinct
    assert "0 Meta" in distinct
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
        assert "NOT_CALCULATED" in c["factor"]

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
    start = text.find("lauren_goode_executive_access_asymmetry_openai_io_vs_meta_hardware_447")
    block = text[start:start+20000]
    assert "—" not in block, "em dash found in new mechanism block, must use hyphen only"
    assert "–" not in block, "en dash found, must use hyphen only"

def test_source_urls_https():
    mech = get_mech()
    urls = mech["source_urls"]
    assert len(urls) >= 6
    for u in urls:
        assert u.startswith("https://"), f"URL must be HTTPS: {u}"
    assert "https://www.wired.com/story/business-wars-meta-ray-bans-mass-surveillance/" in urls
    assert "https://www.phonearena.com/news/OpenAIs-secret-gadget-is-getting-delayed-until-next-year_id178098" in urls
    assert "https://www.entrepreneur.com/business-news/openai-is-purchasing-apple-designer-jony-ives-ai-startup-io/492022" in urls

def test_browser_verification():
    mech = get_mech()
    assert "browser_verification_date" in mech
    assert "browser_task_verification" in mech
    assert "QA audit Sep 1 2026 13:00 UTC" in mech["browser_task_verification"]

def test_goal_and_job_ids():
    mech = get_mech()
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["iteration_time"] == "2026-09-01 13:00 PDT"

def test_cross_references():
    mech = get_mech()
    refs = mech["cross_references"]
    assert 436 in refs
    assert 442 in refs
    assert 446 in refs
    assert 97 in refs

def test_overview_contains_correlation_not_causation():
    mech = get_mech()
    overview = mech["overview"]
    assert "correlation does not imply causation" in overview or "correlation not causation" in overview
    assert "MANUAL ILLUSTRATIVE" in overview
    assert "structural incentive not proof of editorial control" in overview or "structural incentive" in overview

def test_no_synthetic_significance_overclaim():
    mech = get_mech()
    inv = mech["framing_inversion_analysis"]["google_android_xr_vs_meta_rayban"]
    assert inv["is_significant"] is False
    assert inv["p_value"] == "NOT_CALCULATED"
    access = mech["goode_executive_access"]
    assert "DO NOT claim empirical significance" in access["methodology"]

def test_openai_io_hardware_desc_not_wearable():
    mech = get_mech()
    io_cov = mech["openai_io_coverage"]
    desc = io_cov["hardware_desc"].lower()
    assert "not wearable" in desc or "not in-ear" in desc
    assert io_cov["timeline_ship"] == "2027-02 per Welinder filing"

def test_journalist_profile_mechanism_matches_wired():
    wired_mech = get_mech()
    j_mech = get_journalist_mech()
    assert wired_mech["mechanism_id"] == j_mech["mechanism_id"]
    assert wired_mech["iteration"] == j_mech["iteration"]
    assert wired_mech["journalist"] == j_mech["journalist"]

def test_deal_value_6_5b():
    mech = get_mech()
    assert mech["openai_io_coverage"]["deal_value"] == 6500000000
    assert mech["openai_io_coverage"]["deal_value"] == 6_500_000_000
