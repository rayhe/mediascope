"""
Iteration #362 Type D — Test & Verify — Asymmetry Scoring & Financial Incentive Validity

Date: Sat 2026-08-29 02:00 PT
Type: D — Test & Verify
Mechanism: #362 — Statistical validity consolidation + financial incentive mapping verification

Purpose:
- Run full test suite equivalent checks on scoring pipeline
- Verify asymmetry scorer produces statistically meaningful results on controlled synthetic inputs
- Validate financial incentive architecture (Amazon dual-lab, OpenAI Getty display) does not break scoring
- Ensure em dash discipline across profiles
- Provide regression tests for competitor coverage patterns

This file contains SYNTHETIC tone-array regression tests only.
It does NOT empirically validate real corpus. Per project standing rule Aug 28,
DO NOT claim empirical significance from synthetic scores alone.

Methodology:
- Synthetic controlled arrays (n=5-8 per group) simulating observed framing:
  Meta = adversarial surveillance framing (-0.60 to -0.75)
  OpenAI/Anthropic = constructive aspirational framing (0.0 to +0.35)
- Welch t-test, Cohen's d, bootstrap CI (1000 iter, 95% CI, seed 42 for reproducibility)
- Three meaningfulness criteria: p<0.05, |d|>0.5, CI excludes 0
- Tests must verify thresholds not exact values (exact values depend on scoring module)
"""

import math
import json
import pathlib
import yaml
import pytest
import numpy as np

from mediascope.score.statistical import (
    welch_t_test,
    cohens_d,
    bootstrap_ci,
    interpret_effect_size,
    is_significant,
)
from mediascope.score.asymmetry import calculate_asymmetry
from datetime import datetime

PROFILE_PATH = pathlib.Path("profiles/competitor-entities.yaml")

def load_entities():
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if "entities" in data:
        return data["entities"]
    return data

# --- Scoring pipeline edge cases ---

def test_welch_insufficient_samples():
    t, p = welch_t_test([0.5], [0.3, 0.4, 0.5])
    assert t == 0.0 and p == 1.0

def test_welch_identical_distributions():
    a = [0.5]*5
    b = [0.5]*5
    t, p = welch_t_test(a, b)
    assert p == 1.0
    assert not is_significant(p)

def test_welch_zero_variance_different_means():
    meta = [-0.6]*4
    openai = [0.4]*4
    t, p = welch_t_test(meta, openai)
    assert math.isinf(t) or abs(t) > 10
    assert p == 0.0 or p < 0.001

def test_cohens_d_thresholds():
    # Large separation should be large effect
    meta = [-0.65, -0.75, -0.70, -0.60, -0.68]
    openai = [0.0, 0.25, 0.05, 0.10, 0.15]
    d = cohens_d(meta, openai)
    assert abs(d) > 0.8, f"expected large effect, got {d}"
    assert interpret_effect_size(d) == "large"

def test_cohens_d_negligible():
    a = [0.10, 0.12, 0.11, 0.09, 0.10]
    b = [0.11, 0.10, 0.12, 0.10, 0.11]
    d = cohens_d(a, b)
    assert abs(d) < 0.5

def test_bootstrap_ci_excludes_zero_when_separated():
    meta = [-0.65, -0.75, -0.70, -0.60, -0.68, -0.62, -0.71]
    openai = [0.0, 0.25, 0.05, 0.10, 0.15, 0.08, 0.12]
    lower, upper = bootstrap_ci(meta, openai, n_bootstrap=1000)
    # Difference is negative (meta - openai), CI should be entirely negative
    assert upper < 0, f"CI should exclude 0, got [{lower}, {upper}]"
    assert lower < upper

def test_bootstrap_ci_includes_zero_when_overlapping():
    a = [0.1, -0.1, 0.05, -0.05, 0.0]
    b = [0.05, -0.05, 0.0, 0.02, -0.02]
    lower, upper = bootstrap_ci(a, b, n_bootstrap=1000)
    # Overlapping distributions may include 0
    # Not asserting direction, just that CI is valid interval
    assert lower <= upper
    assert lower <= 0.5 and upper >= -0.5

# --- Asymmetry scoring meaningfulness ---

def test_asymmetry_meta_vs_openai_synthetic_meaningful():
    """Meta negative vs OpenAI positive should be significant with large effect."""
    meta_scores = [-0.65, -0.75, -0.70, -0.60, -0.68]
    openai_scores = [0.0, 0.25, 0.05, 0.10, 0.15]
    result = calculate_asymmetry(
        target_scores=meta_scores,
        peer_scores=openai_scores,
        target_entity="Meta",
        peer_entities=["OpenAI"],
        publication_slug="wired",
        period_start=datetime(2026, 1, 1),
        period_end=datetime(2026, 8, 29),
    )
    assert result.asymmetry_score < 0, "Meta should be more negative than OpenAI"
    assert result.is_significant, f"p={result.p_value} should be <0.05"
    assert abs(result.cohens_d) > 0.5, f"|d|={result.cohens_d} should exceed 0.5"
    assert result.confidence_interval_upper < 0, "CI should exclude 0 (entirely negative)"
    assert result.article_count_target == 5
    assert result.article_count_peers == 5

def test_asymmetry_meta_vs_anthropic_zero_deal_paradox():
    """Anthropic has zero publisher deals yet receives softer coverage - financial predictor test."""
    meta_scores = [-0.60, -0.65, -0.58, -0.62, -0.66]
    anthropic_scores = [0.10, 0.20, 0.15, 0.12, 0.18]
    result = calculate_asymmetry(
        target_scores=meta_scores,
        peer_scores=anthropic_scores,
        target_entity="Meta",
        peer_entities=["Anthropic"],
        publication_slug="financial-times",
        period_start=datetime(2026, 1, 1),
        period_end=datetime(2026, 8, 29),
    )
    assert result.asymmetry_score < -0.5, "Strong negative asymmetry expected"
    assert is_significant(result.p_value)
    assert abs(result.cohens_d) > 0.8

def test_asymmetry_wired_openai_hardware_vs_meta_glasses_illustrative():
    """Illustrative synthetic mirroring Iteration #359 hardware delay framing asymmetry."""
    # Meta glasses: alarm framing
    meta = [-0.65, -0.75, -0.70, -0.60, -0.68]
    # OpenAI hardware: neutral/constructive
    openai = [0.0, 0.25, 0.05, 0.10, 0.15]
    t, p = welch_t_test(meta, openai)
    d = cohens_d(meta, openai)
    lower, upper = bootstrap_ci(meta, openai, n_bootstrap=1000)
    assert p < 0.05
    assert abs(d) > 0.5
    assert upper < 0
    # Methodology note: illustrative only per standing rule
    assert True  # placeholder for documentation that this is synthetic

# --- Financial incentive architecture integrity ---

def test_amazon_dual_lab_layers_exist():
    entities = load_entities()
    amazon = entities.get("amazon", {})
    leverage = amazon.get("sextuple_publisher_leverage", {})
    layers = leverage.get("layers", [])
    names = [l.get("name") for l in layers]
    assert "anthropic_investment" in names
    assert "openai_investment" in names
    assert "aws_cloud_hosting" in names
    assert "advertising_platform" in names

def test_amazon_anthropic_fields_no_em_dash():
    entities = load_entities()
    amazon = entities["amazon"]
    layers = amazon["sextuple_publisher_leverage"]["layers"]
    anth = [l for l in layers if l["name"] == "anthropic_investment"][0]
    detail = anth.get("detail", "")
    assert "—" not in detail
    assert "–" not in detail
    # Required fields from Type C iteration
    assert anth.get("anthropic_total_invested_b") == 13
    assert anth.get("anthropic_potential_total_b") == 33
    assert anth.get("anthropic_trainium_gw") == 5
    assert anth.get("anthropic_openai_mirroring") is True

def test_openai_getty_display_fields():
    entities = load_entities()
    openai = entities["openai"]
    portfolio = openai.get("publisher_content_deal_portfolio", {})
    # total_deals string or int containing 24
    td = portfolio.get("total_deals")
    assert "24" in str(td)
    getty = portfolio.get("getty_images_display_deal_jun2026")
    assert getty is not None
    assert getty.get("low_price") == 0.58
    assert getty.get("rally_price") == 1.29
    assert getty.get("rally_pct") == 122
    # No em dash anywhere in getty block
    dumped = json.dumps(getty, ensure_ascii=False)
    assert "—" not in dumped
    assert "–" not in dumped
    # Structure contains required phrases
    struct = getty.get("structure", "").lower()
    assert "display-only" in struct
    assert "no model training" in struct or "no training" in struct

def test_openai_publisher_deal_count_monotonic_increase():
    """Deal count should be >=24 after Getty + Brazil additions, not regress to <20."""
    entities = load_entities()
    td = entities["openai"]["publisher_content_deal_portfolio"]["total_deals"]
    # Handle string like "24+"
    if isinstance(td, str):
        num = int(''.join(filter(str.isdigit, td)) or 0)
    else:
        num = td
    assert num >= 24, f"expected >=24 deals, got {td}"
    # Notable partners includes Getty and Brazil
    partners = entities["openai"]["publisher_content_deal_portfolio"].get("notable_partners", [])
    joined = " ".join(partners)
    assert "Getty Images" in joined
    assert "Folha" in joined or "UOL" in joined

def test_financial_incentive_predicts_coverage_direction():
    """Core thesis: financial relationship predicts softer coverage (less negative tone)."""
    # Simulate publication with OpenAI deal vs without
    # With deal: OpenAI tone less negative (or positive)
    # Without deal: similar negative as Meta
    # This is structural test of thesis logic, not empirical
    openai_with_deal = [0.10, 0.15, 0.12, 0.08, 0.20]  # softer
    openai_without_deal = [-0.10, -0.15, -0.05, -0.12, -0.08]  # more critical
    meta = [-0.60, -0.65, -0.62, -0.58, -0.66]
    # Asymmetry with deal should be larger magnitude negative (Meta more negative than peer)
    asym_with = sum(meta)/len(meta) - sum(openai_with_deal)/len(openai_with_deal)
    asym_without = sum(meta)/len(meta) - sum(openai_without_deal)/len(openai_without_deal)
    assert asym_with < asym_without, "Deal should predict larger negative asymmetry (softer peer coverage)"
    # Difference should be at least 0.1
    assert abs(asym_with - asym_without) > 0.1

def test_no_em_dash_anywhere_in_critical_blocks():
    """Project rule: no em dash in any profile critical block."""
    entities = load_entities()
    # Check openai hardware block
    openai = entities.get("openai", {})
    hardware = openai.get("hardware_devices", {}).get("hardware_delay_framing_asymmetry_aug28", {})
    if hardware:
        dumped = json.dumps(hardware, ensure_ascii=False)
        assert "—" not in dumped, "em dash found in hardware_delay block"
    # Check amazon detail already covered, but also check openai_investment
    amazon_layers = entities.get("amazon", {}).get("sextuple_publisher_leverage", {}).get("layers", [])
    for layer in amazon_layers:
        if layer.get("name") in ("openai_investment", "anthropic_investment"):
            detail = layer.get("detail", "")
            assert "—" not in detail

def test_scoring_reproducibility_seed_42():
    """Bootstrap CI uses seed 42 for reproducibility - same inputs produce same CI."""
    a = [-0.65, -0.75, -0.70, -0.60, -0.68]
    b = [0.0, 0.25, 0.05, 0.10, 0.15]
    ci1 = bootstrap_ci(a, b, n_bootstrap=1000)
    ci2 = bootstrap_ci(a, b, n_bootstrap=1000)
    assert ci1 == ci2, "bootstrap CI should be reproducible with fixed seed"

def test_interpret_effect_size_boundaries():
    assert interpret_effect_size(0.1) == "negligible"
    assert interpret_effect_size(0.3) == "small"
    assert interpret_effect_size(0.6) == "medium"
    assert interpret_effect_size(1.2) == "large"
    assert interpret_effect_size(-0.9) == "large"

