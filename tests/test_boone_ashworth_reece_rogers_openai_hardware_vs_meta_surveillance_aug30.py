"""
Type B #385: Boone Ashworth + Reece Rogers cross-entity camera wearable framing inversion.

Mechanism #385: Same journalists frame Meta single-camera glasses as mass surveillance / creep
while framing OpenAI camera/mic ambient hardware as happiness / peaceful transformation, zero
surveillance vocabulary despite greater capability (cameras + mics + knows everything you ever
thought/read/said). Google Android XR neutral in same series.

Sources verified Aug 30 2026:
- Business Wars episodes: https://toppodcast.com/podcast_feeds/business-wars/
- VentureBeat Dev Day: https://venturebeat.com/ai/heres-what-jony-ive-and-sam-altman-revealed-about-their-secretive-ai
- Forbes India prototype: https://www.forbesindia.com/article/news/inside-openais-first-ai-device/2988960/1
- Hypebeast prototype: https://hypebeast.com/2025/11/openai-x-jony-ive-screenless-ai-device-reaches-prototype
- WIRED primary blocked: https://www.wired.com/story/sam-altman-and-jony-ives-ai-device-dev-day/ (wired.com blocked by policy, secondary used)

Illustrative synthetic tone scores only, not empirical significance.
"""
import yaml
import pathlib
import re

def load_journalists():
    p = pathlib.Path(__file__).parent.parent / "profiles/careers/journalists.yaml"
    data = yaml.safe_load(p.read_text())
    return data['journalists'] if isinstance(data, dict) and 'journalists' in data else data

def test_ashworth_exists():
    data = load_journalists()
    names = [j['name'] for j in data if 'name' in j]
    assert 'Boone Ashworth' in names, "Boone Ashworth must exist"

def test_mechanism_385_exists():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    cc = ashworth.get('competitor_coverage', {})
    iter385 = cc.get('iteration_385_type_b_2026_08_30_01_00_pt')
    assert iter385 is not None, "iteration_385 must exist in Ashworth competitor_coverage"
    assert iter385['mechanism_id'] == 385
    assert iter385['iteration'] == 385

def test_primary_sources_verified():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    sources = iter385['primary_sources_verified']
    assert len(sources) >= 3, "Need at least 3 verified sources"
    urls = [s['url'] for s in sources]
    assert any('toppodcast.com' in u for u in urls), "Business Wars source required"
    assert any('venturebeat.com' in u for u in urls), "VentureBeat source required"
    assert any('forbesindia.com' in u for u in urls), "Forbes India source required"

def test_wired_primary_blocked_documented():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    blocked = iter385.get('wired_primary_blocked')
    assert blocked is not None, "WIRED block must be documented"
    assert 'wired.com' in blocked['url']
    assert 'blocked' in blocked['block_policy'].lower()

def test_cross_entity_comparison_same_journalist():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    comp = iter385['cross_entity_comparison']
    assert comp['meta']['framing'].lower().find('mass surveillance') >= 0 or 'surveillance' in comp['meta']['framing'].lower()
    assert comp['openai']['framing'].lower().find('happy') >= 0 or 'peaceful' in comp['openai']['framing'].lower()
    assert comp['openai']['surveillance_vocabulary'] == 'zero' or comp['openai']['surveillance_vocabulary'] == 0 or 'zero' in str(comp['openai']['surveillance_vocabulary']).lower()

def test_illustrative_synthetic_labeling():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    ill = iter385['illustrative_asymmetry']
    assert ill['label'] == 'illustrative_synthetic_not_empirical'
    assert 'synthetic' in str(ill['p_value']).lower() or 'illustrative' in str(ill['p_value']).lower()
    # Verify delta calculation
    assert abs(ill['delta'] - 1.55) < 0.01, f"Delta should be 1.55, got {ill['delta']}"

def test_confounders_documented():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    conf = iter385['confounders']
    assert len(conf) >= 4, "At least 4 confounders required"
    # Check for STRONG/MODERATE/WEAK tagging
    tags = ''.join(conf)
    assert '[STRONG]' in tags
    assert '[MODERATE]' in tags

def test_non_causal_language():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    assert 'does not prove editorial influence' in iter385['non_causal_language'] or 'not prove' in iter385['non_causal_language'].lower()

def test_hardware_parity_documented():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    comp = iter385['cross_entity_comparison']
    meta_hw = comp['meta']['hardware'].lower()
    openai_hw = comp['openai']['hardware'].lower()
    assert '12mp' in meta_hw or 'camera' in meta_hw
    assert 'camera' in openai_hw and ('microphone' in openai_hw or 'mic' in openai_hw)

def test_reece_rogers_coauthor_noted():
    data = load_journalists()
    ashworth = next(j for j in data if j.get('name') == 'Boone Ashworth')
    iter385 = ashworth['competitor_coverage']['iteration_385_type_b_2026_08_30_01_00_pt']
    assert 'Reece Rogers' in iter385['journalist'] or 'Rogers' in iter385['summary']
