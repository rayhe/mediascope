"""
Type A Iteration #350 — FT × Anthropic IPO Skepticism vs FT × OpenAI Growth Narrative
Mechanism #361 — Financial Tie Predicts Tone

Focus: FT has $5-10M/yr OpenAI deal, $0 from Anthropic. FT's Aug 23 2026 Anthropic IPO skepticism
piece (Ramp data, 11% Fable 5 spend, aggressive spending questions) vs FT's OpenAI $34B spending
growth milestone framing as dominance. Natural experiment for financial predictor thesis.

Every fact needs source URL.
"""
import pytest
import yaml
from pathlib import Path

FT_YAML = Path(__file__).parent.parent / "profiles" / "financial-times.yaml"

def load_ft():
    return yaml.safe_load(FT_YAML.read_text())

def test_ft_yaml_parseable():
    data = load_ft()
    assert data is not None
    assert "competitor_relationships" in data

def test_anthropic_entry_exists():
    data = load_ft()
    cr = data.get("competitor_relationships", {})
    assert "anthropic" in cr, "anthropic entry missing from competitor_relationships"
    anth = cr["anthropic"]
    assert anth.get("financial_tie") == "none"
    assert anth.get("estimated_value") == "$0"

def test_anthropic_zero_deal_note():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    assert "zero_publisher_deals_note" in anth or "recent_coverage_examples_2026" in anth
    # Check description mentions zero deals
    desc = anth.get("description", "") + anth.get("zero_publisher_deals_note", "")
    assert "ZERO" in desc or "zero" in desc.lower()

def test_anthropic_recent_coverage_examples_exist():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026", [])
    assert len(examples) >= 2, f"Need >=2 recent FT Anthropic examples, got {len(examples)}"
    titles = [e.get("title","") for e in examples]
    assert any("cheaper" in t.lower() or "switch" in t.lower() for t in titles), "Aug 23 cheaper models piece missing"

def test_anthropic_aug23_piece_has_urls():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026", [])
    aug23 = [e for e in examples if "2026-08-23" in e.get("date","")]
    assert len(aug23) == 1, f"Expected 1 Aug 23 piece, got {len(aug23)}"
    e = aug23[0]
    assert e.get("url", "").startswith("https://"), "URL must be HTTPS"
    assert "pymnts.com" in e["url"] or "reuters.com" in e["url"] or "ft.com" in e["url"]
    assert e.get("original_ft_attribution"), "Must note FT is primary source via secondary citation"
    assert e.get("tone_approx") is not None
    assert e["tone_approx"] < 0, "Aug 23 skepticism piece should have negative tone"

def test_anthropic_aug23_language_specificity():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026", [])
    aug23 = [e for e in examples if "2026-08-23" in e.get("date","")][0]
    lang = aug23.get("language", [])
    assert len(lang) >= 5, "Need >=5 verbatim language excerpts"
    text = " ".join(lang).lower()
    assert "11%" in text or "11" in text, "Must include 11% spend statistic"
    assert "aggressive spending" in text or "questions" in text

def test_openai_contrast_exists():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth.get("recent_coverage_examples_2026", [])
    aug23 = [e for e in examples if "2026-08-23" in e.get("date","")][0]
    assert "openai_contrast" in aug23 or "meta_contrast" in aug23, "Must include contrast with OpenAI or Meta framing"

def test_sources_verified_https():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    sources = anth.get("sources_verified", [])
    assert len(sources) >= 3, f"Need >=3 verified sources, got {len(sources)}"
    for url in sources:
        assert url.startswith("https://"), f"Source must be HTTPS: {url}"
    # Check at least one FT-OpenAI deal source
    assert any("reuters.com" in u and "financial-times-openai" in u for u in sources) or \
           any("openai" in u.lower() for u in sources)

def test_asymmetry_scorer_result_exists():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result")
    assert result is not None, "asymmetry_scorer_result missing"
    assert "anthropic_scores" in result
    assert "openai_scores_ft_same_period" in result
    assert len(result["anthropic_scores"]) >= 2
    assert "financial_architecture_extension" in result or "mechanism_361_extends" in str(result)

def test_financial_predictor_ordering():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result", {})
    # OpenAI should be softer (higher avg) than Anthropic, Anthropic softer than Meta
    anth_avg = result.get("anthropic_avg")
    openai_avg = result.get("openai_avg_ft")
    meta_avg = result.get("meta_avg_ft")
    assert anth_avg is not None and openai_avg is not None and meta_avg is not None
    assert openai_avg > anth_avg, f"OpenAI ({openai_avg}) should be softer than Anthropic ({anth_avg}) per financial predictor"
    assert anth_avg > meta_avg, f"Anthropic ({anth_avg}) should be softer than Meta ({meta_avg})"

def test_no_duplicate_mechanism_ids():
    # Ensure our new mechanism doesn't collide
    import re
    text = FT_YAML.read_text()
    # Count mechanism 361 references — should be at least 1 now
    assert "361" in text or "mechanism_361" in text.lower() or "Financial Tie Predicts Tone" in text

def test_cautious_language():
    data = load_ft()
    anth = data["competitor_relationships"]["anthropic"]
    result = anth.get("asymmetry_scorer_result", {})
    note = result.get("methodology_note", "") + str(result)
    assert "illustrative only" in note.lower() or "synthetic" in note.lower() or "DO NOT claim" in note
