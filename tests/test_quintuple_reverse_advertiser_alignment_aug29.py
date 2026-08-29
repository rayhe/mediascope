"""
Iteration #376 - Type C Financial Incentive Mapping
Mechanism #376 - Quintuple Reverse-Advertiser Alignment Aug 29

Tests for fresh financial channel: Meta $3.5B EssilorLuxottica stake + H1 2026 EUR 14.02B
Extends quadruple (372) to quintuple, verifies 103, compounds 53/94, extends 367/358.

Every factual claim needs source URL or citation.
Synthetic/manual tone scores must be labeled illustrative only, never empirical significance.
Maintain no-em-dash discipline.
"""

import yaml
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).parent.parent
COMPETITOR_ENTITIES = REPO_ROOT / "profiles" / "competitor-entities.yaml"
WIRED_YAML = REPO_ROOT / "profiles" / "wired.yaml"

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_amazon(data):
    return (data.get('entities') or data).get('amazon', {})

def test_mechanism_376_exists():
    data = load_yaml(COMPETITOR_ENTITIES)
    amazon = get_amazon(data)
    assert 'quintuple_reverse_advertiser_alignment_aug29' in amazon, "Mechanism 376 not found in amazon entity"
    mech = amazon['quintuple_reverse_advertiser_alignment_aug29']
    assert mech['mechanism_id'] == 376, f"Expected mechanism_id 376, got {mech.get('mechanism_id')}"
    assert mech['date_analyzed'] == '2026-08-29'
    assert mech['type'] == 'financial_incentive_mapping'
    assert mech['iteration'] == 376

def test_mechanism_376_type_c_focus():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    focus = mech.get('type_c_focus', '')
    assert 'EssilorLuxottica' in focus or 'essilorluxottica' in focus.lower(), "Focus must mention EssilorLuxottica"
    assert 'reverse' in focus.lower() or 'fifth' in focus.lower(), "Focus must mention reverse-advertiser or fifth channel"
    assert '3.5' in focus or '$3.5' in str(mech) or '3.5B' in str(mech), "Focus context should reference $3.5B stake"

def test_mechanism_376_financial_channels():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    channels = mech.get('financial_channels', {})
    assert len(channels) >= 5, f"Expected 5 channels, got {len(channels)}"
    assert 'channel_5_essilorluxottica_reverse_advertiser' in channels, "Missing channel 5 EssilorLuxottica reverse-advertiser"
    ch5 = channels['channel_5_essilorluxottica_reverse_advertiser']
    assert ch5['meta_stake_pct'] == 3
    assert ch5['meta_stake_value_b'] == 3.5
    assert 'reuters_url' in ch5 or 'reuters_date' in ch5
    assert ch5['reuters_date'] == '2025-07-08'
    # H1 2026 data
    h1 = ch5.get('essilorluxottica_h1_2026', {})
    assert h1['revenue_b_eur'] == 14.02
    assert h1['yoy_pct'] == 7.3
    assert h1['q2_revenue_b_eur'] == 7.175
    assert h1['ebit_margin_pct'] == 18.3

def test_mechanism_376_reuters_source():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    source_urls = mech.get('source_urls', [])
    reuters_urls = [u for u in source_urls if 'reuters.com' in u and 'essilorluxottica' in u.lower()]
    assert len(reuters_urls) >= 1, "Must include Reuters Jul 8 2025 EssilorLuxottica stake URL"
    # Verify exact URL pattern
    assert 'meta-takes-around-3-stake-ray-ban-parent-essilorluxottica' in reuters_urls[0]

def test_mechanism_376_essilorluxottica_h1_sources():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    source_urls = mech.get('source_urls', [])
    el_urls = [u for u in source_urls if 'essilorluxottica' in u.lower() or 'investing.com' in u or 'nasdaq.com' in u or 'finance.yahoo.com' in u]
    assert len(el_urls) >= 3, f"Expected at least 3 EssilorLuxottica H1 2026 sources, got {len(el_urls)}: {el_urls}"
    # Must include official EL press release
    official = [u for u in source_urls if 'essilorluxottica.com' in u]
    assert len(official) >= 1, "Must include official EssilorLuxottica press release"

def test_mechanism_376_quadruple_sources_preserved():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    source_urls = mech.get('source_urls', [])
    # Amazon, Alphabet, Apple, Google, Meta, Oakley-WIRED must be present
    assert any('adexchanger.com' in u for u in source_urls), "Missing AdExchanger Amazon source"
    assert any('zacks.com' in u and 'googl' in u.lower() or 'zacks.com' in u for u in source_urls), "Missing Zacks Alphabet source"
    assert any('wsj.com' in u for u in source_urls), "Missing WSJ Apple Siri AI source"
    assert any('pymnts.com' in u for u in source_urls), "Missing PYMNTS Google Showcase source"
    assert any('prnewswire.com' in u for u in source_urls), "Missing PRNewswire Meta Q2 source"
    assert any('WebWire.com' in u for u in source_urls), "Missing WebWire Oakley-WIRED alliance source"

def test_mechanism_376_quintuple_synthesis():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    synth = mech.get('quintuple_synthesis', {})
    assert synth['incentive_channels'] == 5
    assert 'channel_5_reverse_advertiser' in synth or 'channel_5' in str(synth)
    # Prediction must mention WIRED and reverse-advertiser nuance
    pred = synth.get('prediction', '')
    assert 'WIRED' in pred or 'wired' in pred.lower()
    assert 'EssilorLuxottica' in pred or 'essilorluxottica' in pred.lower()

def test_mechanism_376_asymmetry_quantification_illustrative():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    synth = mech.get('quintuple_synthesis', {})
    quant = synth.get('asymmetry_quantification_illustrative_only', '') or synth.get('asymmetry_quantification', '')
    # Must be labeled illustrative only
    full_text = str(synth) + str(mech.get('cautious_language',''))
    assert 'illustrative only' in full_text.lower() or 'illustrative synthetic' in full_text.lower(), "Must label synthetic scores as illustrative only"
    assert 'illustrative' in quant.lower() or 'illustrative' in full_text.lower()

def test_mechanism_376_confounding_factors():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    conf = mech.get('confounding_factors', [])
    assert len(conf) >= 5, f"Expected 5 confounding factors (2 STRONG, 2 MODERATE, 1 WEAK), got {len(conf)}"
    strengths = [c.get('strength') for c in conf]
    assert strengths.count('STRONG') >= 2, f"Expected at least 2 STRONG, got {strengths}"
    assert strengths.count('MODERATE') >= 2, f"Expected at least 2 MODERATE, got {strengths}"
    assert 'WEAK' in strengths, "Expected at least 1 WEAK"
    # Must mention correlation ≠ causation
    all_desc = ' '.join([c.get('description','') for c in conf])
    assert 'Correlation' in all_desc or 'correlation' in all_desc or 'causation' in all_desc

def test_mechanism_376_cautious_language():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    cautious = mech.get('cautious_language', '')
    assert 'correlation does not imply causation' in cautious.lower() or 'financial correlation' in cautious.lower()
    assert 'structural incentive' in cautious.lower() or 'structural' in cautious.lower()
    assert 'illustrative' in cautious.lower() or 'synthetic' in cautious.lower()
    assert 'welch' in cautious.lower() or 'cohen' in cautious.lower() or 'bootstrap' in cautious.lower()

def test_mechanism_376_no_em_dash():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    text = str(mech)
    # Check for em dash (—) and en dash (–) - project discipline says no em/en dashes
    assert '—' not in text, f"Found em dash in mechanism 376 - violates no-em-dash discipline"
    assert '–' not in text or text.count('–') == 0 or '–' not in text, f"Found en dash in mechanism 376"
    # Allow hyphen but not em dash - check specifically
    if '—' in text or '–' in text:
        raise AssertionError("Em dash or en dash found in mechanism 376")

def test_mechanism_376_cross_references():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    xrefs = mech.get('cross_references', [])
    assert len(xrefs) >= 4, f"Expected at least 4 cross-references (372, 367, 358, 103), got {len(xrefs)}"
    ids = [x.get('mechanism_id') for x in xrefs]
    assert 372 in ids, "Must extend mechanism 372 quadruple"
    assert 103 in ids, "Must verify mechanism 103 EssilorLuxottica advertising paradox"
    # Check extends relationships
    extends = [x for x in xrefs if x.get('relationship') == 'extends']
    assert len(extends) >= 2, "Expected at least 2 extends relationships"

def test_mechanism_376_coverage_prediction():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    pred = mech.get('coverage_prediction', {})
    assert 'model' in pred
    model = pred['model']
    assert 'WIRED' in model or 'Conde Nast' in model
    assert 'EssilorLuxottica' in model or 'essilorluxottica' in model.lower()
    assert 'Reuters' in model or 'Gizmodo' in model, "Must mention clean controls"

def test_mechanism_376_overview_freshness():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    overview = mech.get('overview', '')
    assert 'Reuters' in overview or 'reuters' in overview.lower()
    assert '14.02' in overview or 'EUR 14.02' in overview or '14.02B' in overview
    assert '3.5B' in overview or '$3.5B' in overview or '3%' in overview
    assert 'reverse-advertiser' in overview.lower() or 'reverse advertiser' in overview.lower()

def test_wired_yaml_essilorluxottica_updated():
    data = load_yaml(WIRED_YAML)
    # WIRED yaml structure: competitor_relationships.essilorluxottica or top-level essilorluxottica
    if 'competitor_relationships' in data and isinstance(data['competitor_relationships'], dict):
        el = data['competitor_relationships'].get('essilorluxottica', {})
    else:
        el = data.get('essilorluxottica', {})
    desc = el.get('description', '')
    assert 'Reuters' in desc or 'reuters.com' in desc.lower(), "WIRED EssilorLuxottica description must include Reuters verification"
    assert '14.02' in desc or 'EUR 14.02' in desc or 'H1 2026' in desc, "Must include H1 2026 verification"
    assert '3.5B' in desc or '$3.5B' in desc or '3%' in desc, "Must include $3.5B stake"
    # Check h1 verification block
    h1 = el.get('h1_2026_verification_aug29', {})
    assert h1.get('mechanism_id') == 376
    assert h1['meta_stake_value_b'] == 3.5
    assert h1['revenue_b_eur'] == 14.02
    assert len(h1.get('source_urls', [])) >= 3

def test_mechanism_376_id_unique():
    data = load_yaml(COMPETITOR_ENTITIES)
    # Collect all mechanism_ids across all entities
    all_ids = []
    entities = (data.get('entities') or data)
    for entity_key, entity_val in entities.items():
        if not isinstance(entity_val, dict):
            continue
        for mech_key, mech_val in entity_val.items():
            if isinstance(mech_val, dict) and 'mechanism_id' in mech_val:
                all_ids.append(mech_val['mechanism_id'])
    # 376 should appear exactly once
    assert all_ids.count(376) == 1, f"Mechanism ID 376 should appear exactly once, found {all_ids.count(376)} times"
    # Known pre-existing duplicate 235 is allowed (repo history), but 376 must not duplicate
    # Check no new duplicates introduced by this mechanism - filter out known duplicates
    from collections import Counter
    counts = Counter(all_ids)
    dups = [k for k,v in counts.items() if v>1 and k != 235]
    assert len(dups) == 0, f"Unexpected duplicate mechanism IDs introduced: {dups} (known allowed duplicate is 235)"

def test_yaml_valid():
    # Both files must be valid YAML
    try:
        load_yaml(COMPETITOR_ENTITIES)
        load_yaml(WIRED_YAML)
    except yaml.YAMLError as e:
        raise AssertionError(f"YAML invalid: {e}")

def test_no_duplication_of_103_or_372():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    overview = mech.get('overview', '')
    # Must explicitly extend 103 and 372, not duplicate them
    # Check that it mentions extending, not replacing
    xrefs = mech.get('cross_references', [])
    xref_text = str(xrefs)
    assert '372' in xref_text and '103' in xref_text, "Must cross-reference both 372 and 103 to show extension not duplication"
    # Overview should mention reverse-advertiser which is fresh, not just repeat 372 quadruple
    assert 'reverse' in overview.lower(), "Overview must emphasize fresh reverse-advertiser angle to avoid duplication claim"

def test_source_url_exactness():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    source_urls = mech.get('source_urls', [])
    # All URLs must be http/https
    for url in source_urls:
        assert url.startswith('http://') or url.startswith('https://'), f"Source URL must start with http/https: {url}"
    # Must have at least 10 URLs (quadruple had 10+, quintuple should have more)
    assert len(source_urls) >= 10, f"Expected at least 10 source URLs, got {len(source_urls)}"

def test_illustrative_labeling_everywhere():
    data = load_yaml(COMPETITOR_ENTITIES)
    mech = get_amazon(data)['quintuple_reverse_advertiser_alignment_aug29']
    full = str(mech)
    # If synthetic tone arrays mentioned, must be labeled illustrative only
    if 'tone' in full.lower() and ('-0.70' in full or '-0.80' in full or 'asymmetry' in full.lower()):
        assert 'illustrative only' in full.lower(), "Tone scores must be labeled illustrative only"
    # Check quintuple_synthesis specifically
    synth = mech.get('quintuple_synthesis', {})
    synth_str = str(synth)
    if 'predicted' in synth_str.lower() and ('-0.70' in synth_str or '+0.15' in synth_str):
        assert 'illustrative' in synth_str.lower(), "Predicted tone deltas must be labeled illustrative"
