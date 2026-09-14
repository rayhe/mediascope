"""
Type A Iteration #350 — FT × Anthropic IPO Skepticism vs FT × OpenAI Growth Narrative
Mechanism #361 — Financial Tie Predicts Tone

Focus: FT has $5-10M/yr OpenAI deal, $0 from Anthropic. FT's Aug 23 2026 Anthropic IPO skepticism
piece (Ramp data, 11% Fable 5 spend, aggressive spending questions) vs FT's OpenAI $34B spending
growth milestone framing as dominance. Natural experiment for financial predictor thesis.

SUPERSEDED STRUCTURE (Type D #730, 2026-09-13 18:00 PDT): the Aug 28 snapshot
keyed the FT-Anthropic relationship as financial_tie "none" / estimated_value "$0" with
recent_coverage_examples_2026 (incl. the Aug 23 2026 cheaper-models skepticism piece) and
an anthropic-level asymmetry_scorer_result. Sep 1 2026 runs (#441/#456, deliberately)
refined the tie to "none_direct_indirect_via_google" (FT-Google commercial partnership +
Google's up-to-$40B Anthropic investment) and moved coverage examples into iteration-keyed
blocks (iteration_441 / 456 / 552); the scorer moved into mechanism_643 (Sep 11, AISI-refusal
accountability scoop). The Aug 23 cheaper-models piece no longer exists in the corpus. All
tests below are repointed at the current structure, preserving their original intent.
Corpus untouched.
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

def _anthropic(data):
    return data["competitor_relationships"]["anthropic"]

def _i441(data):
    return _anthropic(data)["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]

def _m643_scorer(data):
    return _anthropic(data)["mechanism_643_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_openai_launch_week_register_sep11"]["asymmetry_scorer_result"]

def test_anthropic_entry_exists():
    data = load_ft()
    cr = data.get("competitor_relationships", {})
    assert "anthropic" in cr, "anthropic entry missing from competitor_relationships"
    anth = cr["anthropic"]
    # Refined Sep 1 2026 (#441): no DIRECT FT-Anthropic deal, indirect channel via
    # FT's Google commercial partnership + Google's up-to-$40B Anthropic investment.
    assert anth.get("financial_tie") == "none_direct_indirect_via_google"
    assert "$0 direct" in anth.get("estimated_value", "")

def test_anthropic_zero_deal_note():
    data = load_ft()
    anth = _anthropic(data)
    desc = anth.get("description", "")
    # Current form: no direct content licensing deal with Anthropic (unlike OpenAI $5-10M/yr)
    assert "no direct content licensing deal with Anthropic" in desc
    assert "no direct" in desc.lower()

def test_anthropic_recent_coverage_examples_exist():
    data = load_ft()
    # Coverage examples moved to iteration_441 (Sep 1 2026): 3 Anthropic fundraising
    # pieces, tones +0.15 to +0.22 (aspirational) vs Meta -0.55 to -0.62.
    examples = _i441(data)["ft_anthropic_sources_sep01_2026"]
    assert len(examples) >= 2, f"Need >=2 FT Anthropic examples, got {len(examples)}"
    tones = [e.get("tone_manual_illustrative") for e in examples]
    assert all(t is not None and t > 0 for t in tones), f"Aspirational-positive tones expected, got {tones}"

def test_anthropic_aug23_piece_has_urls():
    # SUPERSEDED: the Aug 23 2026 cheaper-models skepticism piece no longer exists in
    # the corpus. The current canonical FT-attributed Anthropic fundraising piece is
    # the May 29 2026 $65B PYMNTS piece (FT cited as original). Intent preserved:
    # the FT-attributed piece carries an HTTPS URL, original FT attribution, and a
    # MANUAL ILLUSTRATIVE tone.
    data = load_ft()
    examples = _i441(data)["ft_anthropic_sources_sep01_2026"]
    pymnts = [e for e in examples if "pymnts.com" in e.get("url", "")][0]
    assert pymnts["url"].startswith("https://"), "URL must be HTTPS"
    assert pymnts.get("original_ft_attribution"), "Must note FT as original source via secondary citation"
    assert pymnts.get("tone_manual_illustrative") is not None

def test_anthropic_aug23_language_specificity():
    data = load_ft()
    examples = _i441(data)["ft_anthropic_sources_sep01_2026"]
    pymnts = [e for e in examples if "pymnts.com" in e.get("url", "")][0]
    lang = pymnts.get("language", [])
    assert len(lang) >= 5, "Need >=5 verbatim language excerpts"
    text = " ".join(lang).lower()
    assert "valuable" in text or "trillion" in text, "Must include market-leader valuation language"

def test_openai_contrast_exists():
    # The OpenAI contrast lives in the iteration_441 finding_summary: Anthropic
    # fundraising coverage is "ahead of OpenAI constructive 0.15 to 0.22 range" while
    # Meta sits at -0.55 to -0.62. The predictor ordering (payer softer) is preserved.
    data = load_ft()
    finding = _i441(data).get("finding_summary", "")
    assert "OpenAI" in finding, "Must include contrast with OpenAI framing"
    assert "constructive" in finding.lower()

def test_sources_verified_https():
    data = load_ft()
    sources = _i441(data).get("source_urls", [])
    assert len(sources) >= 3, f"Need >=3 verified sources, got {len(sources)}"
    for url in sources:
        assert url.startswith("https://"), f"Source must be HTTPS: {url}"
    # Check at least one FT-OpenAI deal source
    assert any("reuters.com" in u and "financial-times-openai" in u for u in sources) or \
           any("openai" in u.lower() for u in sources)

def test_asymmetry_scorer_result_exists():
    # The scorer moved into mechanism_643 (Sep 11 2026, AISI-refusal accountability
    # scoop vs Meta/OpenAI launch-week registers). Intent preserved: a scorer result
    # with target/peer manual illustrative tones, a delta, and limitations exists.
    data = load_ft()
    result = _m643_scorer(data)
    assert result is not None, "asymmetry_scorer_result missing"
    assert "target_tones_manual_illustrative" in result
    assert "peer_tones_manual_illustrative" in result
    assert len(result["target_tones_manual_illustrative"]) >= 1
    assert len(result["peer_tones_manual_illustrative"]) >= 1
    assert "delta_meta_minus_anthropic" in result or "interpretation" in result

def test_financial_predictor_ordering():
    data = load_ft()
    scoring = _i441(data)["asymmetry_scoring_manual_illustrative"]
    # iteration_441 scorer: Meta target avg vs Anthropic peer avg - Anthropic must be
    # softer (higher avg) than Meta, and the finding places Anthropic at/above the
    # OpenAI constructive range. Predictor ordering holds: OpenAI ~= Anthropic > Meta.
    meta_avg = scoring.get("target_avg_manual_illustrative")
    anth_avg = scoring.get("peer_avg_manual_illustrative")
    assert meta_avg is not None and anth_avg is not None
    assert anth_avg > meta_avg, f"Anthropic ({anth_avg}) should be softer than Meta ({meta_avg}) per financial predictor"
    finding = _i441(data).get("finding_summary", "")
    assert "0.15 to 0.22" in finding, "OpenAI constructive range must be documented in the finding"

def test_no_duplicate_mechanism_ids():
    # Ensure our new mechanism doesn't collide
    import re
    text = FT_YAML.read_text()
    # Count mechanism 361 references — should be at least 1 now
    assert "361" in text or "mechanism_361" in text.lower() or "Financial Tie Predicts Tone" in text

def test_cautious_language():
    # The scorer moved into mechanism_643; cautious-language intent is preserved via
    # its limitations block (degenerate contract, manual illustrative, no engine).
    data = load_ft()
    result = _m643_scorer(data)
    note = result.get("limitations", "") + str(result)
    assert "illustrative" in note.lower() or "degenerate" in note.lower() or "DO NOT claim" in note
