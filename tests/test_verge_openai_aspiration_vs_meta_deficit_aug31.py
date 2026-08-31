"""
Iteration 425 Type A - The Verge OpenAI Aspiration vs Meta Deficit Framing
Competitor Coverage Deep Dive

Validates that The Verge's 2025-2026 OpenAI vs Meta AI coverage shows distinct
framing divergence (aspiration vs deficit) that tracks financial licensing incentive
direction, while preserving counterexamples and acknowledging confounders.

Financial relationship: Vox Media/OpenAI licensing May 29 2024 (Reuters primary)
- OpenAI receives Verge archive for training, Vox Media receives licensing fees + tech
- PMC acquired Vox Media Jun 2026, deal transfer status unclear but no termination
- Meta receives $0 AI licensing from Verge/PMC

Coverage pattern documented:
- OpenAI: Atlas browser, GPT-5 prep, GPT-5.6 upgrade - aspiration/innovation (+0.18 MANUAL ILLUSTRATIVE)
- Meta: Muse Spark reentry, researcher rejection, Live AI utility doubt - deficit (-0.28 MANUAL ILLUSTRATIVE)
- Gap 0.46 raw, 0.12 confounder-adjusted

Preserves:
- Nilay Patel critical of OpenAI (unconstrained, child safety)
- Victoria Song positive on Meta hardware (best glasses, turning point)
- Hayden Field critical OpenAI governance piece (vibes off)

Sources: All factual claims require URL backing per project rules.
"""

import pytest
from pathlib import Path
import yaml

PROFILE_PATH = Path(__file__).parent.parent / "profiles" / "the-verge.yaml"

def load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)

def test_profile_exists():
    assert PROFILE_PATH.exists(), f"Profile not found at {PROFILE_PATH}"

def test_iteration_425_exists():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    assert key in data, f"Missing iteration key {key}"
    iteration = data[key]
    assert iteration["iteration"] == 425
    assert iteration["publication"] == "The Verge"
    assert iteration["rotation_type"] == "A"

def test_financial_relationship_sourced():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    fr = iteration["financial_relationship"]
    assert fr["partner"] == "OpenAI"
    assert "2024-05-29" in fr["date_established"]
    assert len(fr["primary_source_urls"]) >= 1
    # Reuters must be present as primary
    assert any("reuters.com" in url for url in fr["primary_source_urls"])
    # Secondary sources must include Press Gazette or TechCrunch
    assert len(fr["secondary_source_urls"]) >= 2

def test_openai_coverage_has_sources():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    openai = iteration["openai_coverage_2025_2026"]
    assert len(openai["articles"]) >= 3
    for article in openai["articles"]:
        assert "title" in article
        assert "url" in article
        assert article["url"].startswith("http")
        assert "framing" in article
        assert "tone_approx" in article
        # No surveillance framing for OpenAI in this mechanism
        assert article.get("surveillance_terms", 0) == 0

def test_meta_coverage_has_sources():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    meta = iteration["meta_coverage_2025_2026"]
    assert len(meta["articles"]) >= 3
    for article in meta["articles"]:
        assert "title" in article
        assert "url" in article
        assert article["url"].startswith("http")
        assert "framing" in article
        assert "deficit" in article["framing"] or "rejection" in article["framing"] or "skepticism" in article["framing"] or "reentry" in article["framing"] or "solution" in article["framing"]

def test_counterexamples_preserved():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    # OpenAI critical counterexample must exist
    openai_ce = iteration["openai_coverage_2025_2026"]["critical_counterexamples_preserved"]
    assert len(openai_ce) >= 1
    assert any("vibes" in ce["title"].lower() or "critical" in ce["framing"] for ce in openai_ce)
    # Meta positive counterexample must exist
    meta_ce = iteration["meta_coverage_2025_2026"]["balanced_counterexamples_preserved"]
    assert len(meta_ce) >= 1
    assert any("best glasses" in ce["title"].lower() or "balanced" in ce["framing"] or "positive" in ce["framing"] for ce in meta_ce)

def test_disclosure_pattern_documented():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    disclosure = iteration["disclosure_pattern"]
    assert "Selective" in disclosure["pattern"] or "selective" in disclosure["pattern"].lower()
    assert len(disclosure["evidence"]) >= 3
    # Must note OpenAI licensing not disclosed
    evidence_text = " ".join(disclosure["evidence"])
    assert "OpenAI" in evidence_text

def test_editorial_independence_acknowledged():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    ei = iteration["editorial_independence"]
    assert "statement" in ei
    stmt = ei["statement"].lower()
    assert "editorial independence" in stmt
    assert "structural incentive" in stmt or "correlational" in stmt
    assert "not proof" in stmt or "not causation" in stmt or "not prove" in stmt

def test_confounders_ranked():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    confounders = iteration["confounding_factors_ranked"]
    assert len(confounders) >= 5
    # Must be ranked 1..n
    ranks = [c["rank"] for c in confounders]
    assert ranks == sorted(ranks)
    assert ranks[0] == 1
    # Rank 1 must be STRONG
    assert confounders[0]["strength"] == "STRONG"
    # Must include product novelty, talent war, beat structure
    factors_text = " ".join([c["factor"] for c in confounders]).lower()
    assert "product novelty" in factors_text or "launch cadence" in factors_text or "novelty" in factors_text
    assert "talent war" in factors_text or "researcher rejection" in factors_text
    assert "beat" in factors_text or "reporter" in factors_text

def test_strongest_counterargument_present():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    sca = iteration["strongest_counterargument"]
    assert len(sca) > 200
    # Must mention market dynamics or genuine news value
    assert "market dynamics" in sca.lower() or "genuine" in sca.lower() or "product cadence" in sca.lower()

def test_limitations_present():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    limitations = iteration["limitations"]
    assert len(limitations) >= 5
    # Must acknowledge proxy sources and small sample
    lim_text = " ".join(limitations).lower()
    assert "proxy" in lim_text or "blocked" in lim_text
    assert "sample size" in lim_text or "small" in lim_text
    assert "manual illustrative" in lim_text

def test_asymmetry_scoring_manual_illustrative_labeled():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    scoring = iteration["asymmetry_scoring_manual_illustrative"]
    assert "MANUAL ILLUSTRATIVE" in scoring["methodology"]
    assert "DO NOT" in scoring["warning"] or "not computed" in str(scoring.get("p_value", "")).lower() or "illustrative only" in scoring["warning"].lower()
    assert scoring["is_significant"] is False
    assert "openai_avg" in scoring
    assert "meta_avg" in scoring
    assert "raw_gap" in scoring
    assert "confounder_adjusted_gap" in scoring
    # Raw gap should be ~0.46
    assert 0.3 < scoring["raw_gap"] < 0.7
    # Adjusted gap should be small ~0.12
    assert 0.05 < scoring["confounder_adjusted_gap"] < 0.25

def test_finding_summary_present():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    summary = iteration["finding_summary"]
    assert len(summary) > 200
    assert "aspiration" in summary.lower() or "innovation" in summary.lower()
    assert "deficit" in summary.lower() or "reentry" in summary.lower()
    assert "OpenAI" in summary
    assert "Meta" in summary

def test_cross_references_present():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    xrefs = iteration["cross_references"]
    assert len(xrefs) >= 4
    # Must reference Hayden Field mechanism #52, Apple paradox #368, Google paradox #112
    xref_ids = [x["mechanism_id"] for x in xrefs]
    assert 52 in xref_ids
    assert 368 in xref_ids or 112 in xref_ids

def test_no_em_dashes():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    # Check key text fields for em dash character
    text_to_check = str(iteration)
    assert "—" not in text_to_check, "Em dash found - must use hyphen per project rules"
    assert "–" not in text_to_check, "En dash found - must use hyphen per project rules"

def test_source_urls_all_valid_format():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    for url in iteration["source_urls"]:
        assert url.startswith("https://") or url.startswith("http://")
        assert " " not in url

def test_distinct_from_existing_mechanisms():
    """Ensure this mechanism is distinct from hardware privacy inversions"""
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    # This mechanism must be about AI model/product framing, not glasses hardware privacy
    assert "hardware privacy" not in iteration["mechanism_name"].lower()
    assert "smart glasses" not in iteration["mechanism_name"].lower() or "product" in iteration["mechanism_name"].lower()
    # Finding summary must mention Atlas, GPT-5, Muse Spark - not just glasses cameras
    summary_lower = iteration["finding_summary"].lower()
    assert "atlas" in summary_lower or "gpt-5" in summary_lower or "muse spark" in summary_lower

def test_test_count_matches():
    data = load_profile()
    key = "iteration_425_aug31_2026_verge_openai_product_vs_meta_deficit_asymmetry"
    iteration = data[key]
    assert iteration["test_count"] == 18
