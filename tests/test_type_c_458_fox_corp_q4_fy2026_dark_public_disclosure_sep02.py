"""
Type C #458: Fox Corp Q4 FY2026 - DARK PUBLIC disclosure posture (new Tier 4)
- Iteration #458 Type C Financial Incentive Mapping Sep 2 2026 00:00 PDT
- Fox Corporation (Nasdaq: FOXA/FOX) holds 2 KNOWN Meta AI licensing deals (Fox News,
  Fox Sports, announced Dec 5 2025) yet disclosed ZERO AI licensing revenue in its
  Q4/FY2026 earnings release (Aug 6 2026) and earnings call highlights, 8 months later
- "Content and other" ($262M Q4, $1.729B FY) attributed entirely to sports sublicensing
- New Tier 4 in publisher_ai_revenue_opacity_index: DARK PUBLIC - public SEC filer,
  zero AI disclosure. Fits neither Tier 1 (private), Tier 2 (bundled but named), nor
  Tier 3 (transparent). Falsifies the assumption that public status yields visibility
- Materiality explanation labeled as inference, not a company statement
- Fox News coverage tone NOT_RATED here; no coverage-tone claim is made
- Structural incentive, correlation not causation, MANUAL ILLUSTRATIVE only
- p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, is_significant false

Sources (observed Sep 2 2026 UTC):
- PR Newswire Aug 6 2026 Fox Q4/FY2026 earnings release (full 579 lines read, zero AI
  licensing mentions) https://www.prnewswire.com/news-releases/fox-reports-fourth-quarter-fiscal-2026-revenue-of-4-21-billion-net-income-of-696-million-and-adjusted-ebitda-of-1-20-billion-302844930.html
- MarketBeat Aug 6 2026 Fox Q4 earnings call highlights (no AI licensing mention)
  https://www.marketbeat.com/instant-alerts/fox-q4-earnings-call-highlights-2026-08-06/
- Deal provenance: Digiday Dec 5 2025, TechCrunch Dec 5 2025 (Meta 13-partner group
  incl. Fox News, Fox Sports); this repo's Meta content-licensing partner list
"""
import pathlib
import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'


def load_competitor():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_tier4_block():
    raw = get_raw()
    idx = raw.find('label: DARK PUBLIC')
    assert idx != -1, "Tier 4 DARK PUBLIC block missing"
    return raw[idx:idx + 6000]


def get_tier4_parsed():
    data = load_competitor()
    tiers = data['publisher_ai_revenue_opacity_index']['opacity_tiers']
    matches = [t for t in tiers if t.get('tier') == 4]
    assert len(matches) == 1, "expected exactly one tier 4 entry"
    return matches[0]


def test_competitor_entities_yaml_parses():
    assert load_competitor() is not None


def test_opacity_index_exists():
    data = load_competitor()
    assert 'publisher_ai_revenue_opacity_index' in data


def test_tier_4_dark_public_label():
    block = get_tier4_block()
    assert 'DARK PUBLIC - Public Company, Zero AI Disclosure' in block


def test_tier_4_fox_entry_present():
    block = get_tier4_block()
    assert 'Fox Corporation (Fox News, Fox Sports)' in block


def test_fox_public_ownership():
    block = get_tier4_block()
    assert 'Nasdaq: FOXA, FOX' in block


def test_fox_two_known_meta_deals():
    tier4 = get_tier4_parsed()
    pubs = tier4['publishers']
    assert len(pubs) == 1
    fox = pubs[0]
    assert fox['ai_deals_known'] == 2
    assert 'Fox News' in fox['ai_deal_details']
    assert 'Fox Sports' in fox['ai_deal_details']
    assert 'Dec 5 2025' in fox['ai_deal_details']


def test_fox_report_date():
    tier4 = get_tier4_parsed()
    fox = tier4['publishers'][0]
    assert fox['report_date'] == '2026-08-06'


def test_fox_q4_revenue_figures():
    block = get_tier4_block()
    assert '$4.212B' in block
    assert '$262M' in block
    assert '$17.126B' in block
    assert '$1.729B' in block


def test_fox_content_other_attributed_to_sports_sublicensing():
    block = get_tier4_block()
    assert 'timing of sports sublicensing revenue' in block
    assert 'higher sports sublicensing revenue' in block


def test_fox_zero_ai_mentions_scoped():
    tier4 = get_tier4_parsed()
    fox = tier4['publishers'][0]
    assert fox['ai_licensing_mentions_in_release'] == 0
    assert fox['ai_licensing_mentions_in_call'] == 0
    assert 'not a full-transcript audit' in fox['verification_scope']


def test_fox_source_urls():
    block = get_tier4_block()
    assert 'prnewswire.com' in block
    assert 'marketbeat.com' in block


def test_mechanism_id_458_unique():
    raw = get_raw()
    assert raw.count('mechanism_id: 458') == 1, "mechanism_id 458 must appear exactly once"


def test_rotation_type_c():
    block = get_tier4_block()
    assert 'rotation: Type C' in block
    assert 'finding_type: financial_incentive_mapping' in block


def test_no_em_dash_in_tier4():
    block = get_tier4_block()
    assert '\u2014' not in block, "em dash banned"


def test_tiers_1_to_3_labels_intact():
    raw = get_raw()
    assert 'label: BLACK BOX - Zero Public Disclosure' in raw
    assert 'label: BUNDLED - Revenue Exists but AI-Specific Revenue Hidden' in raw
    assert 'label: TRANSPARENT - AI Revenue Explicitly Discussed' in raw


def test_fox_only_in_tier_4():
    raw = get_raw()
    idx_start = raw.find('publisher_ai_revenue_opacity_index')
    idx_tier4 = raw.find('- tier: 4')
    before = raw[idx_start:idx_tier4]
    assert 'Fox Corporation (Fox News, Fox Sports)' not in before, \
        "Fox Corp entry must not predate Tier 4 in the opacity index"


def test_materiality_framed_as_inference():
    block = get_tier4_block()
    assert 'inference, not a company statement' in block


def test_no_coverage_tone_claim():
    block = get_tier4_block()
    assert 'NOT_RATED' in block
    assert 'no coverage-tone claim is made here' in block
