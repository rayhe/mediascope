"""
Iteration #374 Type A - WIRED x Samsung Galaxy Glasses hardware parity extension
Tests Mechanism #39 persistence update (38 days) and Mechanism #374 (new samsung entry)
"""
import yaml
import os

def load_wired():
    with open('profiles/wired.yaml') as f:
        return yaml.safe_load(f)

def test_yaml_valid():
    load_wired()

def test_mechanism_39_preserved_and_updated():
    data = load_wired()
    # mechanism 39 may be under top-level key chokkattu_samsung_coverage_selection_gap
    m39 = data.get('chokkattu_samsung_coverage_selection_gap')
    assert m39 is not None, "Mechanism 39 missing"
    assert m39.get('mechanism_id') == 39
    upd = m39.get('aug29_post_launch_persistence_update')
    assert upd is not None, "Aug 29 persistence update missing on mechanism 39"
    assert upd.get('updated_gap_days') == 38
    assert upd.get('original_gap_days') == 20
    assert upd.get('wired_articles_samsung_aug29') == 0
    assert 'No results found' in upd.get('search_verification','')
    # hardware verified identical
    hw = upd.get('samsung_hardware_verified_identical')
    assert hw is not None
    assert 'Snapdragon AR1 Gen 1' in hw.get('chip','')
    assert '12MP' in hw.get('camera','')
    # source urls present
    urls = upd.get('source_urls', [])
    assert len(urls) >= 8, f"need 8+ source urls, got {len(urls)}"
    for u in urls:
        assert u.startswith('http'), f"url must start http: {u}"
    # must contain required domains
    domains = ''.join(urls)
    assert 'androidpolice.com' in domains
    assert 'gizmodo.com' in domains
    assert 'engadget.com' in domains
    assert 'androidauthority.com' in domains
    assert 'samsung.com' in domains or 'samsung' in domains.lower()

def test_samsung_competitor_relationship_added():
    data = load_wired()
    comp = data.get('competitor_relationships', {})
    assert 'samsung' in comp, "samsung missing from competitor_relationships"
    s = comp['samsung']
    assert s.get('financial_tie') in ('advertising', 'none', 'licensing')
    # must not claim content licensing
    desc = s.get('description','')
    assert 'zero content licensing' in desc.lower() or 'zero content licensing deals' in desc.lower() or 'zero' in desc.lower()
    hw_table = s.get('hardware_parity_table_aug29')
    assert hw_table is not None, "hardware_parity_table_aug29 missing"
    assert hw_table.get('mechanism_id') == 374
    assert hw_table.get('date_analyzed') == '2026-08-29'
    # samsung hardware verified
    s_hw = hw_table.get('samsung_hardware_verified_aug29')
    assert s_hw is not None
    assert 'AR1' in s_hw.get('chip','')
    assert '12MP' in s_hw.get('camera','')
    assert '9 hours' in s_hw.get('battery','') or '9hr' in s_hw.get('battery','').lower() or '9 hours' in str(s_hw.get('battery',''))
    # meta comparison
    meta_cmp = hw_table.get('meta_hardware_comparison')
    assert meta_cmp is not None
    # selection gap
    gap = hw_table.get('wired_selection_gap_persistence')
    assert gap is not None
    upd_gap = gap.get('updated_gap_days')
    # allow int 38 or string containing 38
    assert upd_gap == 38 or '38' in str(upd_gap), f"updated_gap_days should be 38, got {upd_gap}"
    wired_samsung = gap.get('wired_articles_samsung')
    # allow int 0 or string containing -> 0
    assert wired_samsung == 0 or '0 (Aug 11) -> 0 (Aug 29)' in str(wired_samsung) or '0' in str(wired_samsung)

def test_source_urls_exact_and_no_em_dash():
    data = load_wired()
    comp = data.get('competitor_relationships', {}).get('samsung', {}).get('hardware_parity_table_aug29', {})
    urls = comp.get('source_urls', [])
    # check no em dash in newly added material (search text)
    import json
    text = yaml.dump(comp)
    assert '—' not in text, "em dash found in new material"
    text2 = yaml.dump(data.get('chokkattu_samsung_coverage_selection_gap',{}).get('aug29_post_launch_persistence_update',{}))
    assert '—' not in text2, "em dash found in mechanism 39 update"
    # check urls are exact https
    for u in urls:
        assert u.startswith('https://') or u.startswith('http://')

def test_cautious_language_and_confounders():
    data = load_wired()
    m39_upd = data.get('chokkattu_samsung_coverage_selection_gap',{}).get('aug29_post_launch_persistence_update',{})
    cautious = m39_upd.get('cautious_language','')
    assert 'does not imply causation' in cautious.lower() or 'financial correlation' in cautious.lower()
    assert 'no claim of editorial control' in cautious.lower() or 'no claim' in cautious.lower()
    conf = m39_upd.get('confounders_reaffirmed','')
    assert 'London' in conf or 'market share' in conf.lower()

    comp = data.get('competitor_relationships',{}).get('samsung',{}).get('hardware_parity_table_aug29',{})
    legit = comp.get('legitimate_factors', [])
    assert len(legit) >= 5, "need 5+ legitimate factors"
    counter = comp.get('counterpoints', [])
    assert len(counter) >= 4, "need 4+ counterpoints"
    caut2 = comp.get('cautious_language','')
    assert 'does not imply causation' in caut2.lower() or 'financial correlation' in caut2.lower()

def test_no_unsupported_causal_language():
    data = load_wired()
    comp = data.get('competitor_relationships',{}).get('samsung',{}).get('hardware_parity_table_aug29',{})
    txt = str(comp).lower()
    # should not claim "proves bias" or "proves editorial control"
    assert 'proves bias' not in txt
    assert 'proves editorial control' not in txt
    assert 'because of financial' not in txt or 'financial incentive alone does not explain' in txt or 'financial correlation does not imply' in txt

def test_cross_references_include_39():
    data = load_wired()
    comp = data.get('competitor_relationships',{}).get('samsung',{}).get('hardware_parity_table_aug29',{})
    xrefs = comp.get('cross_references', [])
    assert 39 in xrefs, "must cross-reference mechanism 39"
    # should include privacy framing mechanisms
    assert 76 in xrefs or 91 in xrefs or 93 in xrefs

def test_illustrative_scorer_labeled_not_empirical():
    data = load_wired()
    comp = data.get('competitor_relationships',{}).get('samsung',{}).get('hardware_parity_table_aug29',{})
    scorer = comp.get('asymmetry_scorer_result_illustrative', {})
    assert scorer, "illustrative scorer missing"
    note = scorer.get('methodology_note','').lower()
    assert 'illustrative' in note
    assert 'not observed' in note or 'synthetic' in note
    # ensure does not claim empirical significance
    interp = scorer.get('interpretation','').lower()
    assert 'illustrative only' in interp

def test_iteration_374_not_duplicate_mechanism():
    # Ensure we did not create duplicate mechanism 39
    data = load_wired()
    # mechanism 39 should still be single
    assert data.get('chokkattu_samsung_coverage_selection_gap',{}).get('mechanism_id') == 39
    # new mechanism is 374, distinct
    comp = data.get('competitor_relationships',{}).get('samsung',{}).get('hardware_parity_table_aug29',{})
    assert comp.get('mechanism_id') == 374
    assert comp.get('mechanism_id') != 39
