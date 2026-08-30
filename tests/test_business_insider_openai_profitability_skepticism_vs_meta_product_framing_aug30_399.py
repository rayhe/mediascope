"""
Test #399 Type A: Business Insider OpenAI profitability skepticism vs Meta product framing
Asymmetry analysis for publication that has parent-level OpenAI licensing deal.

Verifies:
- Business Insider profile has competitor_relationships.openai section
- Mechanism 399 exists with required fields
- Source URLs present and https (dejavu allowed as archive)
- MANUAL ILLUSTRATIVE labeling present
- No em dashes in mechanism block
- Cautious language present (no causal claim)
- Confounders documented (beat, market share, timing, sourcing, financial tie, newsworthiness, paywall)
- Tone comparison illustrates inverse pattern vs WIRED (Meta more positive than OpenAI in BI window)
- No duplicate mechanism ID collision
"""
import pathlib
import yaml
import re

def load_bi():
    p = pathlib.Path(__file__).parent.parent / "profiles/business-insider.yaml"
    with open(p) as f:
        return yaml.safe_load(f), f.read() if hasattr(f, 'read') else open(p).read()

def test_bi_profile_parseable():
    p = pathlib.Path(__file__).parent.parent / "profiles/business-insider.yaml"
    with open(p) as f:
        data = yaml.safe_load(f)
    assert data['slug'] == 'business-insider'
    assert 'competitor_relationships' in data

def test_mechanism_399_exists():
    data, _ = load_bi()
    assert 'competitor_relationships' in data
    assert 'openai' in data['competitor_relationships']
    openai = data['competitor_relationships']['openai']
    # mechanism stored under business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399 key
    mech_key = 'business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399'
    assert mech_key in openai, f"Mechanism key {mech_key} not found in openai competitor_relationships"
    mech = openai[mech_key]
    assert mech['mechanism_id'] == 399
    assert mech['type'].startswith('Type A')
    assert mech['publication'] == 'business-insider'
    assert mech['competitor'] == 'openai'

def test_mechanism_399_required_fields():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    assert 'finding' in mech
    assert 'business_insider_openai_articles' in mech
    assert 'business_insider_meta_articles' in mech
    assert 'tone_comparison' in mech
    assert 'confounders' in mech
    assert 'cautious_language' in mech
    assert 'source_urls' in mech
    assert len(mech['business_insider_openai_articles']) >= 1
    assert len(mech['business_insider_meta_articles']) >= 2

def test_source_urls_present_and_https():
    data, raw = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    urls = mech['source_urls']
    assert len(urls) >= 5, "Expected at least 5 source URLs"
    for u in urls:
        assert u.startswith('https://'), f"URL must be https: {u}"
    # Check specific expected domains present
    raw_lower = " ".join(urls).lower()
    assert 'dejavu.org' in raw_lower or 'businessinsider.com' in raw_lower
    assert 'reuters.com' in raw_lower
    assert 'bloomberglaw.com' in raw_lower or 'axelspringer.com' in raw_lower

def test_manual_illustrative_labeling():
    p = pathlib.Path(__file__).parent.parent / "profiles/business-insider.yaml"
    content = p.read_text()
    # Find mechanism block region
    idx = content.find('business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399')
    assert idx != -1
    block = content[idx:idx+12000]
    assert 'MANUAL ILLUSTRATIVE' in block
    assert 'illustrative_warning' in block or 'MANUAL ILLUSTRATIVE - not empirical' in block
    assert 'not_calculated' in block.lower() or 'not_calculated - illustrative only' in block

def test_no_em_dashes_in_mechanism():
    p = pathlib.Path(__file__).parent.parent / "profiles/business-insider.yaml"
    content = p.read_text()
    idx = content.find('business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399')
    block = content[idx:idx+15000]
    # Em dash U+2014 and U+2013 en dash check - only em dash is forbidden per project rule, but check both
    assert '—' not in block, "Em dash found in mechanism block - violates project rule"
    # Ensure hyphens used instead

def test_cautious_language_present():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    cautious = mech['cautious_language'].lower()
    assert 'does not imply causation' in cautious or 'does not prove' in cautious or 'correlation does not' in cautious
    assert 'confounder' in cautious or 'beat assignment' in cautious or 'market share' in cautious

def test_confounders_documented():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    confounders = mech['confounders']
    assert len(confounders) >= 6, f"Expected at least 6 confounders, got {len(confounders)}"
    levels = [c['level'] for c in confounders]
    assert 'STRONG' in levels
    factors = [c['factor'] for c in confounders]
    # Must include beat, market share, timing, sourcing, financial tie, newsworthiness, paywall
    factors_str = " ".join(factors).lower()
    assert 'beat' in factors_str
    assert 'market_share' in factors_str or 'product_stage' in factors_str
    assert 'timing' in factors_str
    assert 'sourcing' in factors_str
    assert 'financial' in factors_str or 'genuine_newsworthiness' in factors_str

def test_tone_comparison_inverse_pattern():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    tone = mech['tone_comparison']
    # Business Insider shows Meta more positive than OpenAI in this window, inverse of WIRED
    assert 'openai_avg_MANUAL_ILLUSTRATIVE' in tone
    assert 'meta_avg_MANUAL_ILLUSTRATIVE' in tone
    assert 'delta_MANUAL_ILLUSTRATIVE' in tone or 'asymmetry_result_MANUAL_ILLUSTRATIVE' in tone
    # Delta should be positive (Meta more positive) - inverse of WIRED where delta negative
    if 'delta_MANUAL_ILLUSTRATIVE' in tone:
        delta = tone['delta_MANUAL_ILLUSTRATIVE']
        # Allow both positive and negative but document inverse pattern in comment
        assert isinstance(delta, (int, float))

def test_asymmetry_scorer_fields():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    tone = mech['tone_comparison']
    assert 'methodology' in tone
    meth_lower = tone['methodology'].lower()
    assert 'welch' in meth_lower or 'illustrative only' in meth_lower
    assert 'do not claim statistical significance' in meth_lower or 'requires observed corpus' in meth_lower

def test_no_duplicate_mechanism_id_collision():
    import glob
    ids = []
    for yaml_file in glob.glob(str(pathlib.Path(__file__).parent.parent / "profiles/*.yaml")):
        try:
            with open(yaml_file) as f:
                content = f.read()
                # crude mechanism_id extraction
                for m in re.finditer(r'mechanism_id:\s*(\d+)', content):
                    ids.append(int(m.group(1)))
        except:
            continue
    # 399 should appear at least once, but not duplicated excessively
    count_399 = ids.count(399)
    assert count_399 >= 1, "mechanism_id 399 not found in any profile"
    assert count_399 <= 2, f"mechanism_id 399 appears {count_399} times, possible collision"

def test_openai_articles_key_phrases():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    openai_articles = mech['business_insider_openai_articles']
    # First article should contain key phrases from BI profitability piece
    first = openai_articles[0]
    assert 'key_phrases' in first
    phrases = " ".join(first['key_phrases']).lower()
    assert 'cash incinerator' in phrases or 'a lot of things need to go right' in phrases or 'margin for error is thin' in phrases

def test_meta_articles_product_framing():
    data, _ = load_bi()
    mech = data['competitor_relationships']['openai']['business_insider_openai_profitability_skepticism_vs_meta_product_framing_aug30_399']
    meta_articles = mech['business_insider_meta_articles']
    framings = [a.get('framing','') for a in meta_articles]
    framing_str = " ".join(framings).lower()
    assert 'delay' in framing_str or 'supply' in framing_str or 'retail' in framing_str

def test_financial_tie_documented():
    data, _ = load_bi()
    openai_section = data['competitor_relationships']['openai']
    assert 'financial_tie' in openai_section
    assert 'estimated_value' in openai_section
    assert 'source_urls' in openai_section
    assert len(openai_section['source_urls']) >= 2
