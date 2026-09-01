"""
Type C #432: Advance Publications Turnitin Dual-Sided AI Conflict Formalization Aug 31 2026 22:00 PDT

Mechanism: Advance profits from BOTH sides of AI content arms race - Condé Nast licenses TO AI (5 deals) AND Turnitin detects AI (16,000 institutions, 71M students, 200M AI detector papers) - arms-dealer-selling-to-both-sides dynamic, no disclosure in WIRED coverage.

Novelty verification:
- grep PCM in wired.yaml/competitor-entities.yaml shows Microsoft PCM already exhaustively covered via test_microsoft_septuple_leverage_aug7.py, wired.yaml lines 550 1224 1227 2915, existing Type C commit - do NOT claim PCM as new
- Advance Reddit dual licensing #417 and Reddit RPO #427 are prior work, explicitly cited as prior, not claimed as new here
- Turnitin dual-sided entry exists as type: dual_sided_ai_conflict Jun 26 2026 in wired.yaml without mechanism_id, test file, or SEC-style quantification - this formalizes it as mechanism 432 with 9+ primary sources, cautious language, confounders, and test file
- No existing mechanism_id 432, no existing test file for Turnitin dual-sided conflict formalization
- Standing rule Aug 31 2026: search profiles, tests, git history before claiming Type C novelty - completed, Turnitin dual-sided formalization with $1.75B acquisition quantification + 5-deal licensing portfolio + Palo Alto Online California colleges spend millions + LA Times Jun 21 2026 AI cheating wars not previously formalized as mechanism with tests

Sources:
- https://www.edsurge.com/news/2019-03-06-turnitin-to-be-acquired-by-advance-publications-for-1-75b
- https://turnitin.com/about/advance-acquires-turnitin
- https://en.wikipedia.org/wiki/Turnitin
- https://www.paloaltoonline.com/2025/07/california-colleges-spend-millions-turnitin-ai-faulty-tech/
- https://www.reuters.com/technology/openai-signs-content-deal-with-conde-nast-2024-08-20/
- https://www.technologyrecord.com/article/new-microsoft-platform-lets-publishers-set-terms-for-ai-content-use
- https://www.searchenginejournal.com/ppc-pulse-microsofts-publisher-marketplace-google-tag/566641/
- https://www.seroundtable.com/microsoft-publisher-content-marketplace-40875.html
- https://advance.com
- https://www.latimes.com/business/story/2026-06-21/ai-cheating-wars-colleges-turnitin
"""
import yaml
from pathlib import Path

def load_yaml(p):
    return yaml.safe_load(Path(p).read_text())

def test_mechanism_id_432_exists():
    ce = load_yaml("profiles/competitor-entities.yaml")
    assert "advance_turnitin_dual_sided_ai_conflict_432" in ce, "mechanism 432 must exist in competitor-entities.yaml"
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    assert m["mechanism_id"] == 432
    assert m["iteration"] == 432
    assert m["iteration_type"] == "C"
    assert m["type"] == "Type C Financial Incentive Mapping"

def test_wired_yaml_mechanism_432_exists():
    w = load_yaml("profiles/wired.yaml")
    assert "advance_turnitin_dual_sided_ai_conflict_432" in w, "mechanism 432 must exist in wired.yaml"
    m = w["advance_turnitin_dual_sided_ai_conflict_432"]
    assert m["mechanism_id"] == 432

def test_type_c_required_fields():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    required = ["date_analyzed", "type", "iteration", "iteration_type", "iteration_time", "scheduled_job_id", "goal_id", "publication_focus", "competitor_pair", "financial_channel", "payment_direction", "overview", "primary_sources", "source_urls", "test_file", "financial_incentive_mapping", "strongest_counterargument", "confounding_factors", "coverage_prediction", "cautious_language"]
    for f in required:
        assert f in m, f"missing field {f}"

def test_iteration_time_and_goal():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    assert m["iteration_time"] == "2026-08-31 22:00 PDT"
    assert m["goal_id"] == "goal_54093bda4145"
    assert m["scheduled_job_id"] == "mediascope-daily-iteration"
    assert "WIRED" in m["publication_focus"]

def test_publication_focus_wired():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    assert "WIRED" in m["publication_focus"] or "Condé Nast" in m["publication_focus"]

def test_financial_channel_turnitin():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    fc = m["financial_channel"].lower()
    assert "turnitin" in fc
    assert "1.75" in fc or "$1.75b" in fc

def test_payment_direction_dual_sided():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    pd = m["payment_direction"]
    assert "Condé Nast" in pd or "Conde Nast" in pd or "Condé" in pd
    assert "Turnitin" in pd
    assert "Advance Publications" in pd

def test_primary_sources_count_and_urls():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    ps = m["primary_sources"]
    assert len(ps) >= 8, f"need >=8 primary sources, got {len(ps)}"
    urls = [p["url"] for p in ps]
    # Check required URLs present
    assert any("edsurge.com" in u and "turnitin-to-be-acquired" in u for u in urls), "EdSurge Turnitin acquisition required"
    assert any("turnitin.com" in u and "advance-acquires" in u for u in urls), "Turnitin.com announcement required"
    assert any("wikipedia.org" in u and "Turnitin" in u for u in urls), "Wikipedia Turnitin required"
    assert any("paloaltoonline.com" in u for u in urls), "Palo Alto Online required"
    assert any("reuters.com" in u and "conde-nast" in u for u in urls), "Reuters Condé Nast OpenAI required"
    assert any("technologyrecord.com" in u for u in urls), "Technology Record PCM required"
    assert any("advance.com" in u for u in urls), "Advance.com required"

def test_source_urls_https_no_spaces():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    for url in m["source_urls"]:
        assert url.startswith("https://"), f"URL must be HTTPS: {url}"
        assert " " not in url, f"URL must not contain spaces: {url}"

def test_primary_sources_claims_contain_quantification():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    all_claims = " ".join([p["claim"] for p in m["primary_sources"]]).lower()
    assert "$1.75b" in all_claims or "1.75b" in all_claims
    assert "16,000" in all_claims or "16000" in all_claims
    assert "71m" in all_claims or "71m students" in all_claims or "71" in all_claims

def test_overview_contains_dual_sided_arms_dealer():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    ov = m["overview"].lower()
    assert "both sides" in ov or "both sides of the ai" in ov
    assert "arms-dealer" in ov or "arms dealer" in ov or "selling to both sides" in ov
    assert "turnitin" in ov
    assert "condé nast" in ov or "conde nast" in ov

def test_financial_incentive_mapping_acknowledgment():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    fim = m["financial_incentive_mapping"]
    assert fim["editorial_independence_acknowledgment"] is True
    assert "correlational" in fim["financial_relationship"].lower()
    assert "not proof of editorial control" in fim["financial_relationship"].lower()
    assert "no documented editorial directive" in fim["financial_relationship"].lower()

def test_meta_contrast():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    mc = m["financial_incentive_mapping"]["meta_contrast"]
    assert "Meta" in mc
    assert "zero" in mc.lower()

def test_strongest_counterargument_length():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    ca = m["strongest_counterargument"]
    assert len(ca) >= 200, f"counterargument must be >=200 chars, got {len(ca)}"
    assert "diversified portfolio" in ca.lower() or "diversified" in ca.lower()

def test_confounders_strength_labels():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    cfs = m["confounding_factors"]
    assert len(cfs) >= 4, f"need >=4 confounders, got {len(cfs)}"
    strong_count = sum(1 for cf in cfs if cf["strength"] == "STRONG")
    assert strong_count >= 2, f"need >=2 STRONG confounders, got {strong_count}"
    # Check Turnitin disclaimer confounder present
    all_desc = " ".join([cf["description"].lower() for cf in cfs])
    assert "privacy" in all_desc or "turnitin" in all_desc

def test_coverage_prediction_manual_illustrative():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    cp = m["coverage_prediction"]
    assert "MANUAL ILLUSTRATIVE" in cp["model"] or "MANUAL ILLUSTRATIVE" in cp["model"].upper()
    assert "welch" in cp["model"].lower() or "empirical validation" in cp["model"].lower()

def test_cautious_language_fields():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    cl = m["cautious_language"]
    assert cl["correlation_not_causation"] is True
    assert cl["no_editorial_control_claim"] is True
    assert cl["no_statistical_significance_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in cl["manual_illustrative_label"]
    assert cl["p_value_not_calculated"] is True
    assert cl["cohens_d_not_calculated"] is True

def test_no_em_dashes_in_overview():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    # Project rule: no em dashes in documents
    assert "—" not in m["overview"], "em dash found in overview, violates project rule"

def test_test_file_path_matches():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    assert m["test_file"] == "tests/test_type_c_432_advance_turnitin_dual_sided_ai_conflict_aug31.py"

def test_extension_of_prior_dual_sided_entry():
    ce = load_yaml("profiles/competitor-entities.yaml")
    m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
    ov = m["overview"]
    # Must acknowledge prior type entry Jun 26 2026, not claim original discovery of dual-sided conflict
    assert "Jun 26 2026" in ov or "Jun 26" in ov or "dual_sided_ai_conflict" in ov.lower() or "Formalization of prior" in ov

def test_yaml_parsability_both_files():
    # Ensure both YAML files still parse after insertion
    ce = load_yaml("profiles/competitor-entities.yaml")
    w = load_yaml("profiles/wired.yaml")
    assert ce is not None
    assert w is not None
