"""
Type A: FT × OpenAI licensing — competitor coverage deep dive
Iteration #384 — 2026-08-30 00:00 PT

Validates:
- FT OpenAI licensing deal primary source reports undisclosed terms
- Secondary valuation $5-10M/yr labeled secondary_report_based
- Meta comparators exact URLs (FT via Reuters)
- Deal disclosure status false for all FT OpenAI articles
- Non-causal wording — no proof of editorial influence
- Aggregate asymmetry labeled illustrative if synthetic
"""
import yaml
from pathlib import Path

PROFILE = Path("profiles/financial-times.yaml")

def load_profile():
    return yaml.safe_load(PROFILE.read_text())

def test_primary_terms_undisclosed():
    data = load_profile()
    openai = data.get("competitor_relationships", {}).get("openai", {})
    # cash_terms_disclosed must be false
    assert openai.get("cash_terms_disclosed") is False, "cash_terms_disclosed must be false"
    assert openai.get("valuation_source_type") == "secondary_report_based", "valuation must be secondary_report_based"
    primary = openai.get("valuation_primary_source", "")
    assert "not disclosed" in primary.lower() or "undisclosed" in primary.lower()

def test_secondary_valuation_source_present():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    sec = openai.get("valuation_secondary_source", "")
    assert "WSJ" in sec or "Digiday" in sec or "$5" in sec, f"secondary source missing: {sec}"

def test_meta_comparator_urls_exact():
    data = load_profile()
    # look in cross_entity_coverage_analysis for meta equity raising
    mechanisms = data.get("cross_entity_coverage_analysis", {})
    # Mechanism 356 should exist
    m356 = mechanisms.get("openai_funding_govt_stake_vs_meta_equity_framing_asymmetry")
    assert m356 is not None, "Mechanism 356 missing"
    meta_comps = m356.get("meta_coverage_comparator_2026", [])
    urls = [c.get("url") for c in meta_comps]
    # exact URL for Jun 5 FT via Reuters
    assert "https://www.reuters.com/technology/meta-weighs-big-equity-raising-finance-ai-infrastructure-ft-reports-2026-06-05/" in urls, f"Meta equity URL missing: {urls}"
    # Also check iteration 384 entry if present
    iter_key = "iteration_384_type_a_2026_08_30"
    if iter_key in mechanisms:
        entry = mechanisms[iter_key]
        meta_urls = [c.get("url") for c in entry.get("meta_comparators", [])]
        assert any("meta-weighs-big-equity" in u for u in meta_urls)

def test_deal_disclosure_status_false_all():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    examples = openai.get("recent_coverage_examples_2026_h1_h2", [])
    for ex in examples:
        assert ex.get("deal_disclosed") is False, f"deal_disclosed should be false for {ex.get('title')}"

    mechanisms = data.get("cross_entity_coverage_analysis", {})
    for key in ["openai_funding_govt_stake_vs_meta_equity_framing_asymmetry", "iteration_384_type_a_2026_08_30"]:
        mech = mechanisms.get(key)
        if not mech:
            continue
        for art in mech.get("openai_coverage_2026", []):
            assert art.get("deal_disclosed") is False, f"{key} openai coverage deal_disclosed false required"

def test_non_causal_wording():
    # Profile text must not claim proof/causation of editorial influence
    text = PROFILE.read_text().lower()
    # Ensure we don't have prohibited causal claim phrases in new iteration
    # We check the iteration_384 section specifically if present
    data = load_profile()
    mechanisms = data.get("cross_entity_coverage_analysis", {})
    iter_entry = mechanisms.get("iteration_384_type_a_2026_08_30")
    if iter_entry:
        summary = str(iter_entry.get("finding_summary","")).lower() + str(iter_entry.get("finding","")).lower()
        # Must not say "proves editorial influence" or "causes bias"
        assert "proves editorial influence" not in summary
        assert "proves that" not in summary or "financial relationship" not in summary  # loose
        # Must contain non-causal language
        assert any(phrase in str(iter_entry).lower() for phrase in ["predicts", "may", "structural incentive", "does not prove", "does not prove editorial", "correlation", "predictor"])

def test_aggregate_asymmetry_labeled_illustrative():
    data = load_profile()
    mechanisms = data.get("cross_entity_coverage_analysis", {})
    iter_entry = mechanisms.get("iteration_384_type_a_2026_08_30")
    if iter_entry:
        scorer = iter_entry.get("asymmetry_scorer_result", {})
        note = scorer.get("synthetic_note", "") + scorer.get("methodology_note","") + str(iter_entry.get("methodology_note",""))
        combined = (note + str(iter_entry)).lower()
        # If synthetic scores, must say illustrative
        if scorer:
            assert "illustrative" in combined or "synthetic" in combined, "aggregate asymmetry must be labeled illustrative when synthetic"
