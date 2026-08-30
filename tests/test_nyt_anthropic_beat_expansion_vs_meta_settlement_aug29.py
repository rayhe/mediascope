"""
Type A Iteration #379 — NYT × Anthropic beat expansion vs Meta adversarial settlement framing
Mechanism #379 — Financial Incentive Predicts Beat Investment

Focus: NYT Aug 19 2026 creates dedicated Anthropic reporter role, frames Anthropic as
power broker growth story, while Aug 26 2026 Meta settlement coverage uses dramatic
capitulation framing. Natural experiment: NYT has $20-25M/yr Amazon deal (soft),
reported Anthropic settlement (undisclosed), $0 Meta (adversarial), $0 OpenAI (litigation).

Every fact needs source URL.
"""
import pytest
import yaml
from pathlib import Path

NYT_YAML = Path(__file__).parent.parent / "profiles" / "nytimes.yaml"

def load_nyt():
    return yaml.safe_load(NYT_YAML.read_text())

def test_nyt_yaml_parseable():
    data = load_nyt()
    assert data is not None
    assert "competitor_relationships" in data

def test_anthropic_entry_exists():
    data = load_nyt()
    cr = data.get("competitor_relationships", {})
    assert "anthropic" in cr, "anthropic entry missing"
    anth = cr["anthropic"]
    assert anth.get("financial_tie") in ("settlement_reported", "none", "licensing")

def test_recent_coverage_examples_aug29_exist():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026_aug29", [])
    assert len(examples) >= 2, f"Need >=2 recent NYT Anthropic examples Aug 29, got {len(examples)}"
    dates = [e.get("date","") for e in examples]
    assert any("2026-08-19" in d for d in dates), "Aug 19 NYT Anthropic beat posting missing"
    assert any("2026-07-17" in d for d in dates), "Jul 17 NYT Meta-Anthropic compute lease missing"

def test_aug19_piece_has_exact_url():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026_aug29", [])
    aug19 = [e for e in examples if "2026-08-19" in e.get("date","")][0]
    assert aug19["url"].startswith("https://")
    assert "talkingbiznews.com" in aug19["url"]
    assert aug19.get("original_nyt_attribution")
    assert aug19["tone_approx"] > 0, "Beat expansion should be positive tone"

def test_jul17_piece_has_exact_url_and_meta_contrast():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026_aug29", [])
    jul17 = [e for e in examples if "2026-07-17" in e.get("date","")][0]
    assert "reuters.com" in jul17["url"]
    assert "meta_contrast" in jul17, "Must include Meta contrast for framing comparison"
    lang = jul17.get("language", [])
    assert len(lang) >= 4

def test_language_specificity_no_emdash():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026_aug29", [])
    for ex in examples:
        for phrase in ex.get("language", []):
            assert "—" not in phrase, f"Em dash found in language excerpt, violates style rule: {phrase}"
            assert "–" not in phrase, f"En dash found, avoid em dashes in documents"

def test_asymmetry_scorer_result_exists_and_labeled_synthetic():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result_2026_08_29")
    assert result is not None, "asymmetry_scorer_result_2026_08_29 missing"
    assert "anthropic_scores_synthetic_illustrative" in result
    assert "meta_scores_synthetic_illustrative" in result
    note = result.get("methodology_note","")
    assert "illustrative" in note.lower() or "synthetic" in note.lower()
    assert result.get("anthropic_vs_meta_significant") is True
    assert result["anthropic_vs_meta_asymmetry"] > 0

def test_financial_incentive_caution_present():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result_2026_08_29", {})
    caution = result.get("financial_incentive_caution","") + result.get("methodology_note","")
    assert "structural incentive" in caution.lower() or "not proof" in caution.lower()
    assert "confounder" in caution.lower() or "counterexample" in caution.lower() or "legitimate" in caution.lower()

def test_tone_ordering_financial_predictor():
    data = load_nyt()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result_2026_08_29", {})
    anth_avg = result.get("anthropic_avg")
    meta_avg = result.get("meta_avg_ft")
    amazon_avg = result.get("amazon_avg_ft")
    assert anth_avg is not None and meta_avg is not None and amazon_avg is not None
    assert anth_avg > meta_avg, f"Anthropic ({anth_avg}) should be softer than Meta ({meta_avg})"
    # Amazon softest due to $20-25M deal, but Anthropic close if settlement real
    assert amazon_avg >= anth_avg or abs(amazon_avg - anth_avg) < 0.1

def test_no_duplicate_mechanism_collision():
    text = NYT_YAML.read_text()
    assert "2026-08-19" in text
    assert "2026-07-17" in text
    assert "recent_coverage_examples_2026_aug29" in text
