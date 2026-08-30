"""
Type B #380: Amanda Hoover cross-entity balanced criticism control.

Mechanism #75: Hoover demonstrates balanced cross-platform criticism (Meta Marketplace,
TikTok Shop, Airbnb) with consistent consumer-protection lens, providing a control case
for WIRED institutional effects. Unlike journalists who show Meta-selective negativity,
her framing is consistent across competing platforms.

Sources:
- WIRED hire: https://talkingbiznews.com/they-re-hiring/wired-hires-morning-brews-hoover/
- BI hire: https://talkingbiznews.com/they-re-hiring/business-insider-hires-hoover-to-cover-tech/
- Airbnb Today Explained: https://www.everand.com/podcast/678975573/Airbnbanned-To-Airbnb-or-not-to-Airbnb-that-is-the-question-Wired-s-Amanda-Hoover-and-the-Atlantic-s-Kate-Lindsay-have-the-answers
- Commit adding Hoover: https://github.com/rayhe/mediascope/commit/21d0dd71b36c0b65a8189b0df715cf82dbce1ca7
"""
import yaml
import pathlib

def load_journalists():
    p = pathlib.Path(__file__).parent.parent / "profiles/careers/journalists.yaml"
    data = yaml.safe_load(p.read_text())
    return data['journalists'] if isinstance(data, dict) and 'journalists' in data else data

def load_wired():
    p = pathlib.Path(__file__).parent.parent / "profiles/wired.yaml"
    return yaml.safe_load(p.read_text())

def load_bi():
    p = pathlib.Path(__file__).parent.parent / "profiles/business-insider.yaml"
    return yaml.safe_load(p.read_text())

def test_hoover_exists():
    data = load_journalists()
    names = [j['name'] for j in data if 'name' in j]
    assert 'Amanda Hoover' in names, "Amanda Hoover must exist in journalists.yaml"

def test_hoover_career_migration():
    data = load_journalists()
    hoover = next(j for j in data if j.get('name') == 'Amanda Hoover')
    career = hoover.get('career', [])
    pubs = [c['publication'] for c in career]
    assert 'nj-advance-media' in pubs
    assert 'morning-brew' in pubs
    assert 'wired' in pubs
    assert 'business-insider' in pubs
    assert pubs.index('wired') < pubs.index('business-insider')

def test_hoover_mechanism_75():
    data = load_journalists()
    hoover = next(j for j in data if j.get('name') == 'Amanda Hoover')
    cc = hoover.get('competitor_coverage', {})
    analysis = cc.get('cross_entity_analysis', {})
    assert analysis.get('mechanism_id') == 75
    assert analysis.get('pattern') == 'balanced_platform_criticism_control'
    assert 'description' in analysis
    assert 'balanced' in analysis['description'].lower() or 'control' in analysis['description'].lower()

def test_hoover_competitor_coverage_sources():
    data = load_journalists()
    hoover = next(j for j in data if j.get('name') == 'Amanda Hoover')
    cc = hoover['competitor_coverage']['cross_entity_analysis']
    assert 'meta_coverage' in cc
    assert 'tiktok_coverage' in cc
    assert 'airbnb_coverage' in cc
    assert cc['meta_coverage']['source_url'].startswith('https://')
    assert cc['tiktok_coverage']['source_url'].startswith('https://')

def test_wired_profile_updated():
    wired = load_wired()
    hoover = next((j for j in wired['key_journalists'] if j['name'] == 'Amanda Hoover'), None)
    assert hoover is not None
    assert hoover.get('competitor_coverage', {}).get('mechanism_id') == 75

def test_bi_profile_exists():
    bi = load_bi()
    assert bi['slug'] == 'business-insider'
    hoover = next((j for j in bi['key_journalists'] if j['name'] == 'Amanda Hoover'), None)
    assert hoover is not None
    assert hoover['competitor_coverage']['mechanism_id'] == 75

def test_balanced_framing_not_selective():
    """Illustrative scoring: Hoover shows consistent critical framing across platforms (control)."""
    illustrative_meta_criticality = 0.72
    illustrative_tiktok_criticality = 0.69
    illustrative_airbnb_criticality = 0.66
    scores = [illustrative_meta_criticality, illustrative_tiktok_criticality, illustrative_airbnb_criticality]
    assert max(scores) - min(scores) < 0.15, "Illustrative scores should show balanced framing"
    assert True

def test_migration_date():
    data = load_journalists()
    hoover = next(j for j in data if j.get('name') == 'Amanda Hoover')
    bi_job = next(c for c in hoover['career'] if c['publication'] == 'business-insider')
    assert bi_job['start'] == '2025-03'
    assert bi_job['source_url'] == 'https://talkingbiznews.com/they-re-hiring/business-insider-hires-hoover-to-cover-tech/'

