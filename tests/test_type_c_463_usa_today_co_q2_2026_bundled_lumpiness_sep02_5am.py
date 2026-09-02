"""
Type C #463: USA TODAY Co. Q2 2026 - Tier 2 BUNDLED posture deepened
- Iteration #463 Type C Financial Incentive Mapping Sep 2 2026 05:00 PDT
- USA TODAY Co. (NYSE: TDAY; renamed from Gannett, ticker changed from GCI) reported
  Q2 2026 Aug 6 2026: total revenue $536.3M (-8.3% YoY)
- Digital Other revenue $20.4M (+20.2% YoY) driven by syndication, licensing
  agreements, commerce - AI licensing buried in 3-way bundle, not isolatable
- Zero AI deal partners named on the call even when an analyst asked directly about
  new AI licensing deals; Reed declined specifics pending announcements
- Reed confirmed Q2 content licensing lumpiness, cited as partial driver of the 8.3%
  total revenue decline - validates Gosser Q1 2026 lumpy warning; disclosure-without-
  disclosure: AI licensing moves the total but no dollars and no names are disclosed
- New leverage posture: prepared to cut off Google crawlers to force a fair licensing
  deal; expects summary judgment ruling in USA TODAY Co. v Google in September 2026
- Release forward-looking boilerplate names growth of AI content licensing as a
  strategic pillar while disclosing zero figures
- Tier 2 BUNDLED confirmed, not Tier 3: constant AI licensing talk, zero AI revenue
  breakout, zero partner names
- Structural incentive mapping only; correlation not causation; MANUAL ILLUSTRATIVE only
- p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, is_significant false

Sources (observed Sep 2 2026 UTC):
- BusinessWire Aug 6 2026 USA TODAY Co. Q2 2026 earnings release (primary)
  https://www.businesswire.com/news/home/20260806055001/en/USA-TODAY-Co.-Announces-Second-Quarter-Results-Reiterates-Business-Outlook
- Motley Fool Aug 13 2026 Q2 2026 earnings call transcript (Reed, Gosser, Roberts)
  https://www.fool.com/earnings/call-transcripts/2026/08/13/usa-today-tday-q2-2026-earnings-call-transcript/
- Q1 2026 baseline: Digiday media briefing (existing source_url in YAML)
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

BW_URL = 'https://www.businesswire.com/news/home/20260806055001/en/USA-TODAY-Co.-Announces-Second-Quarter-Results-Reiterates-Business-Outlook'
FOOL_URL = 'https://www.fool.com/earnings/call-transcripts/2026/08/13/usa-today-tday-q2-2026-earnings-call-transcript/'


def load_competitor():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_tier2_block():
    raw = get_raw()
    idx = raw.find('label: BUNDLED - Revenue Exists but AI-Specific Revenue Hidden')
    assert idx != -1, 'Tier 2 BUNDLED block missing'
    tier3 = raw.find('- tier: 3', idx)
    return raw[idx:tier3]


def get_usa_today_entry():
    data = load_competitor()
    tiers = data['publisher_ai_revenue_opacity_index']['opacity_tiers']
    tier2 = [t for t in tiers if t.get('tier') == 2][0]
    matches = [p for p in tier2['publishers'] if 'USA Today Co.' in p.get('name', '')]
    assert len(matches) == 1, 'expected exactly one USA Today Co. entry in Tier 2'
    return matches[0]


def test_competitor_entities_yaml_parses():
    assert load_competitor() is not None


def test_opacity_index_exists():
    data = load_competitor()
    assert 'publisher_ai_revenue_opacity_index' in data


def test_tier2_bundled_label_intact():
    block = get_tier2_block()
    assert 'BUNDLED - Revenue Exists but AI-Specific Revenue Hidden' in block


def test_usa_today_entry_in_tier2():
    entry = get_usa_today_entry()
    assert entry['name'] == 'USA Today Co. (Gannett)'


def test_ticker_updated_to_tday():
    entry = get_usa_today_entry()
    assert 'TDAY' in entry['ownership']
    assert 'GCI' in entry['ownership']


def test_q2_2026_data_present():
    entry = get_usa_today_entry()
    q2 = entry.get('q2_2026_data')
    assert q2 is not None
    assert q2['report_date'] == '2026-08-06'


def test_q2_total_revenue_figures():
    entry = get_usa_today_entry()
    q2 = entry['q2_2026_data']
    assert q2['total_revenue_m'] == 536.3
    assert q2['revenue_yoy_pct'] == -8.3


def test_q2_digital_other_bundle():
    entry = get_usa_today_entry()
    q2 = entry['q2_2026_data']
    assert q2['digital_other_revenue_m'] == 20.4
    assert q2['digital_other_yoy_pct'] == 20.2
    assert 'not separately broken out' in q2['digital_other_drivers']


def test_zero_partners_named():
    entry = get_usa_today_entry()
    assert entry['q2_2026_data']['partners_named'] == 0


def test_ai_revenue_not_isolatable():
    entry = get_usa_today_entry()
    assert entry['ai_revenue_isolatable'] is False


def test_lumpiness_validates_q1_warning():
    entry = get_usa_today_entry()
    q2 = entry['q2_2026_data']
    assert 'lumpiness' in q2['lumpiness']
    assert 'Gosser' in q2['lumpiness']
    assert 'lumpy' in entry['cfo_warning']


def test_google_crawler_leverage_posture():
    entry = get_usa_today_entry()
    posture = entry['q2_2026_data']['google_posture']
    assert 'cut off Google crawlers' in posture
    assert 'September 2026' in posture


def test_machine_readable_reformatting():
    entry = get_usa_today_entry()
    assert 'machine readable' in entry['q2_2026_data']['machine_readable']


def test_source_urls_https_and_primary():
    entry = get_usa_today_entry()
    urls = entry['q2_2026_data']['source_urls']
    assert BW_URL in urls
    assert FOOL_URL in urls
    assert all(u.startswith('https://') for u in urls)


def test_statistical_discipline_flag():
    entry = get_usa_today_entry()
    assert entry['q2_2026_data']['correlation_not_causation'] is True


def test_no_em_dash_in_tier2_usa_today():
    block = get_tier2_block()
    start = block.find('USA Today Co. (Gannett)')
    tier_people = block.find('- name: People Inc.', start)
    usa_block = block[start:tier_people]
    assert '\u2014' not in usa_block, 'em dash banned'


def test_no_causal_claim_language():
    block = get_tier2_block()
    start = block.find('USA Today Co. (Gannett)')
    tier_people = block.find('- name: People Inc.', start)
    usa_block = block[start:tier_people].lower()
    assert 'proves' not in usa_block


def test_mechanism_463_novelty_markers():
    raw = get_raw()
    assert raw.count('digital_other_revenue_m: 20.4') == 1


def test_test_file_self_reference():
    text = pathlib.Path(__file__).read_text()
    assert '463' in text
    assert 'Type C' in text
    assert 'usa_today' in pathlib.Path(__file__).name
