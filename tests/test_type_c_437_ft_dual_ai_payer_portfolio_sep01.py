"""
Type C #437: FT Dual AI Payer Portfolio Sep 1 2026 03:00 PDT

Mechanism: Financial Times receives dual AI payer revenue OpenAI $5-10M/yr plus Google single figure millions GBP/yr combined $10-20M/yr estimated MANUAL ILLUSTRATIVE while Meta $0 creates structural incentive asymmetry 2 vs 0 payers.

Novelty verification:
- grep ft_dual_partner_wearables_coverage_silence_aug13 shows Type B wearables coverage selection mechanism #87, distinct from Type C financial incentive mapping dual payer portfolio quantification, not claimed as new here but cited as prior cross-ref
- grep financial_times dual payer shows no existing Type C mechanism_id 437, no existing test file for FT dual OpenAI+Google payer portfolio financial mapping
- Existing FT OpenAI single-payer $5-10M/yr and FT Google single figure millions are individual ties documented in financial-times.yaml and competitor-entities.yaml, but no mechanism formalizes DUAL portfolio combined value, payment_direction OpenAI->FT AND Google->FT vs Meta $0, confounding factors ranked, cautious language, MANUAL ILLUSTRATIVE
- Standing rule Sep 1 2026: search profiles, tests, git history before claiming Type C novelty - completed, dual payer portfolio with 6 primary sources, cautious language, confounders, and test file is genuinely novel per grep -rn mechanism_id 437 zero before iteration
- Reddit Google $60M/yr data deal per Reuters Feb 22 2024 positioned against competition for advertising dollars from TikTok and Meta is cited as contextual ad competition example, not claimed as novel, already heavily covered by mechanisms #40 #161 #162 #417 #427

Sources:
- https://www.reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29/
- https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/
- https://talkingbiznews.com/media-news/ft-signs-ai-deal-with-google/
- https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/?ref=wheresyoured.at
"""
import yaml
from pathlib import Path

def load_yaml(p):
    return yaml.safe_load(Path(p).read_text())

def test_mechanism_id_437_exists_ce():
    ce = load_yaml("profiles/competitor-entities.yaml")
    assert "ft_dual_ai_payer_portfolio_437" in ce, "mechanism 437 must exist in competitor-entities.yaml"
    m = ce["ft_dual_ai_payer_portfolio_437"]
    assert m["mechanism_id"] == 437
    assert m["iteration"] == 437
    assert m["iteration_type"] == "C"
    assert m["type"] == "Type C Financial Incentive Mapping"

def test_mechanism_id_437_exists_ft():
    ft = load_yaml("profiles/financial-times.yaml")
    assert "ft_dual_ai_payer_portfolio_437" in ft, "mechanism 437 must exist in financial-times.yaml"
    m = ft["ft_dual_ai_payer_portfolio_437"]
    assert m["mechanism_id"] == 437

def test_type_c_required_fields_ce():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    required = ["date_analyzed", "type", "iteration", "iteration_type", "iteration_time", "scheduled_job_id", "goal_id", "publication_focus", "competitor_pair", "financial_channel", "payment_direction", "overview", "primary_sources", "source_urls", "test_file", "financial_incentive_mapping", "strongest_counterargument", "confounding_factors", "coverage_prediction", "cautious_language"]
    for f in required:
        assert f in m, f"missing field {f} in competitor-entities.yaml"

def test_iteration_time_and_goal():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    assert m["iteration_time"] == "2026-09-01 03:00 PDT"
    assert m["goal_id"] == "goal_54093bda4145"
    assert m["scheduled_job_id"] == "mediascope-daily-iteration"
    assert "Financial Times" in m["publication_focus"]

def test_publication_focus_ft():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    assert "Financial Times" in m["publication_focus"] or "FT" in m["publication_focus"]

def test_financial_channel_dual_payer():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    fc = m["financial_channel"].lower()
    assert "dual" in fc
    assert "openai" in fc
    assert "google" in fc
    assert "5-10m" in fc or "$5" in fc

def test_payment_direction_dual():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    pd = m["payment_direction"]
    assert "OpenAI" in pd
    assert "Google" in pd
    assert "FT" in pd
    assert "Meta" in pd or "$0" in pd

def test_primary_sources_count_and_urls():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    ps = m["primary_sources"]
    assert len(ps) >= 6, f"need >=6 primary sources, got {len(ps)}"
    urls = [p["url"] for p in ps]
    assert any("reuters.com" in u and "financial-times-openai-sign-content-licensing" in u for u in urls), "Reuters FT OpenAI required"
    assert any("digiday.com" in u and "timeline" in u for u in urls), "Digiday timeline required"
    assert any("talkingbiznews.com" in u and "ft-signs-ai-deal-with-google" in u for u in urls), "Talking Biz News FT Google required"
    assert any("pressgazette.co.uk" in u and "google-ai-deals-uk-publishers" in u for u in urls), "Press Gazette UK publishers required"
    assert any("pressgazette.co.uk" in u and "news-publisher-ai-deals-lawsuits" in u for u in urls), "Press Gazette platforms required"
    assert any("reddit-ai-content-licensing-deal-with-google" in u for u in urls), "Reddit Google deal required"

def test_source_urls_https_no_spaces():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    for url in m["source_urls"]:
        assert url.startswith("https://"), f"URL must be HTTPS: {url}"
        assert " " not in url, f"URL must not contain spaces: {url}"

def test_primary_sources_claims_contain_quantification():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    all_claims = " ".join([p["claim"] for p in m["primary_sources"]]).lower()
    assert "$5" in all_claims or "5m" in all_claims or "5-10m" in all_claims
    assert "single figure millions" in all_claims or "single figure" in all_claims
    assert "200 publications" in all_claims or "200" in all_claims

def test_overview_contains_dual_payer():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    ov = m["overview"].lower()
    assert "dual" in ov
    assert "openai" in ov
    assert "google" in ov
    assert "meta" in ov
    assert "$0" in ov or "zero" in ov

def test_financial_incentive_mapping_acknowledgment():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    fim = m["financial_incentive_mapping"]
    assert fim["editorial_independence_acknowledgment"] is True
    assert "correlational" in fim["financial_relationship"].lower()
    assert "not proof of editorial control" in fim["financial_relationship"].lower()
    assert "no documented editorial directive" in fim["financial_relationship"].lower()

def test_meta_contrast():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    mc = m["financial_incentive_mapping"]["meta_contrast"]
    assert "Meta" in mc
    assert "zero" in mc.lower() or "$0" in mc

def test_strongest_counterargument_length():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    ca = m["strongest_counterargument"]
    assert len(ca) >= 200, f"counterargument must be >=200 chars, got {len(ca)}"
    assert "nikkei" in ca.lower() or "material" in ca.lower()

def test_confounders_strength_labels():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    cfs = m["confounding_factors"]
    assert len(cfs) >= 4, f"need >=4 confounders, got {len(cfs)}"
    strong_count = sum(1 for cf in cfs if cf["strength"] == "STRONG")
    assert strong_count >= 2, f"need >=2 STRONG confounders, got {strong_count}"

def test_coverage_prediction_manual_illustrative():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    cp = m["coverage_prediction"]
    assert "MANUAL ILLUSTRATIVE" in cp["model"] or "MANUAL ILLUSTRATIVE" in cp["model"].upper()
    assert "welch" in cp["model"].lower() or "empirical validation" in cp["model"].lower()

def test_cautious_language_fields():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    cl = m["cautious_language"]
    assert cl["correlation_not_causation"] is True
    assert cl["no_editorial_control_claim"] is True
    assert cl["no_statistical_significance_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in cl["manual_illustrative_label"]
    assert cl["p_value_not_calculated"] is True
    assert cl["cohens_d_not_calculated"] is True

def test_no_em_dashes_in_overview():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    assert "—" not in m["overview"], "em dash found in overview, violates project rule"
    assert "—" not in m["financial_channel"], "em dash in financial_channel"

def test_test_file_path_matches():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["ft_dual_ai_payer_portfolio_437"]
    assert m["test_file"] == "tests/test_type_c_437_ft_dual_ai_payer_portfolio_sep01.py"

def test_ft_yaml_google_enriched():
    ft = load_yaml("profiles/financial-times.yaml")
    google = ft["competitor_relationships"]["google"]
    assert "single figure millions" in google["estimated_value"].lower()
    assert google["cash_terms_disclosed"] is False
    assert "source_urls" in google
    assert len(google["source_urls"]) >= 3

def test_ft_yaml_dual_payer_iteration_nested():
    ft = load_yaml("profiles/financial-times.yaml")
    google = ft["competitor_relationships"]["google"]
    assert "iteration_437_sep01_2026_ft_dual_ai_payer_portfolio" in google
    nested = google["iteration_437_sep01_2026_ft_dual_ai_payer_portfolio"]
    assert nested["mechanism"] == 437
    assert "OpenAI" in nested["financial_relationship"]["openai_partner"] or "openai" in str(nested).lower()

def test_yaml_parsability_both_files():
    ce = load_yaml("profiles/competitor-entities.yaml")
    ft = load_yaml("profiles/financial-times.yaml")
    assert ce is not None
    assert ft is not None

def test_no_duplicate_mechanism_id():
    ce = load_yaml("profiles/competitor-entities.yaml")
    # Count occurrences of mechanism_id 437 in file text
    import pathlib
    text = pathlib.Path("profiles/competitor-entities.yaml").read_text()
    count_437 = text.count("mechanism_id: 437")
    assert count_437 == 1, f"mechanism_id 437 should appear exactly once in competitor-entities.yaml, got {count_437}"
