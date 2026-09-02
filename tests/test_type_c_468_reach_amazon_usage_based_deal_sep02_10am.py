"""
Type C #468: Reach plc - Amazon usage-based AI licensing deal (Mar 2 2026)
- Iteration #468 Type C Financial Incentive Mapping Sep 2 2026 10:00 PDT
- Reach plc (UK national and regional publisher; Daily Mirror and Daily Express
  publisher per Press Gazette) signed a deal for its content to be used in
  Amazon's Nova AI model and Alexa assistant with compensation based on usage
- First usage-based (non-flat-fee) AI licensing structure in the MediaScope
  Amazon portfolio: NYT ($20-25M/yr flat, May 2025), Conde Nast (Rufus, Jul 2025),
  Hearst (Rufus, Jul 2025) are all flat/multi-year structures
- CEO Piers North staff memo frames it as a "repeatable model" giving "more
  visibility" into usage - the opposite of the Tier 1 BLACK BOX opacity posture
- Sign/sue bifurcation: Reach signed with Amazon while separately considering
  legal action against OpenAI (Press Gazette understands, not a Reach statement)
- Meta has zero known AI licensing deals with Reach plc
- Structural financial mapping only; correlation not causation; no tone scores,
  no p_value, no significance claim

Sources (observed Sep 2 2026 UTC):
- Press Gazette AI deals/lawsuits tracker (updated Sep 1 2026, Reach-Amazon
  section dated 2 March 2026, CEO memo quotes via Press Gazette)
  https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

PG_URL = 'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/'


def load_entities():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_mech():
    data = load_entities()
    return data['entities']['amazon']['mechanism_468_reach_plc_amazon_usage_based_deal']


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_468_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 468
    assert mech['iteration'] == 468


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date'] == '2026-09-02'
    assert mech['time_pdt'] == '10:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_publisher_identity():
    mech = get_mech()
    assert 'Reach plc' in mech['publisher']
    assert 'Mirror' in mech['publisher']
    assert 'Express' in mech['publisher']


def test_counterparty_and_deal_date():
    mech = get_mech()
    assert 'Amazon' in mech['tech_counterparty']
    assert mech['deal_date'] == '2026-03-02'


def test_scope_nova_and_alexa():
    mech = get_mech()
    assert 'Nova' in mech['scope']
    assert 'Alexa' in mech['scope']


def test_usage_based_compensation_structure():
    mech = get_mech()
    assert 'usage-based' in mech['compensation_structure']
    assert 'not one flat fee' in mech['compensation_structure']
    assert mech['deal_terms_disclosed'] is False


def test_ceo_memo_quotes():
    mech = get_mech()
    quotes = ' '.join(mech['ceo_memo_quotes'])
    assert 'fair return for content creators' in quotes
    assert 'repeatable model' in quotes
    assert 'more visibility' in quotes
    assert 'Piers North' in mech['ceo']


def test_sign_sue_bifurcation_scoped():
    mech = get_mech()
    bifurc = mech['sign_sue_bifurcation']
    assert 'OpenAI' in bifurc
    assert 'not a Reach statement' in bifurc


def test_amazon_portfolio_has_four_deals():
    mech = get_mech()
    portfolio = mech['amazon_publisher_portfolio_after_deal']
    assert len(portfolio) == 4
    joined = ' '.join(portfolio)
    assert 'NYT' in joined
    assert 'Conde Nast' in joined
    assert 'Hearst' in joined
    assert 'Reach plc' in joined


def test_meta_zero_reach_deals():
    mech = get_mech()
    assert 'zero' in mech['meta_comparison'].lower()
    assert 'Reach plc' in mech['meta_comparison']


def test_statistical_discipline():
    mech = get_mech()
    assert mech['correlation_not_causation'] is True
    assert mech['is_significant'] is False
    assert 'No p_value' in mech['statistical_note']


def test_confounders_ranked():
    mech = get_mech()
    conf = mech['confounders_ranked']
    assert len(conf['strong']) >= 2
    assert len(conf['moderate']) >= 2
    assert len(conf['weak']) >= 1
    strong_joined = ' '.join(conf['strong'])
    assert 'Press Gazette' in strong_joined


def test_source_url_https():
    mech = get_mech()
    assert PG_URL in mech['source_urls']
    assert all(u.startswith('https://') for u in mech['source_urls'])


def test_no_em_dash_in_mechanism_block():
    raw = get_raw()
    start = raw.find('mechanism_468_reach_plc_amazon_usage_based_deal')
    assert start != -1
    end = raw.find('  apple:', start)
    block = raw[start:end]
    assert '\u2014' not in block, 'em dash banned'


def test_no_causal_claim_language():
    raw = get_raw()
    start = raw.find('mechanism_468_reach_plc_amazon_usage_based_deal')
    end = raw.find('  apple:', start)
    block = raw[start:end].lower()
    assert 'proves' not in block
    assert 'caused by' not in block


def test_licensing_layer_updated():
    raw = get_raw()
    assert 'Reach plc (usage-based, Nova AI plus Alexa,' in raw
    assert 'mechanism 468' in raw


def test_mechanism_468_uniqueness():
    raw = get_raw()
    assert raw.count('mechanism_468_reach_plc_amazon_usage_based_deal') == 1
    assert len(re.findall(r'mechanism_id: 468\b', raw)) == 1


def test_novelty_markers():
    mech = get_mech()
    assert '443' in mech['novelty_verification']
    assert '458' in mech['novelty_verification']
    assert '463' in mech['novelty_verification']


def test_cross_references_present():
    mech = get_mech()
    refs = {r['mechanism_id'] for r in mech['cross_references']}
    assert 371 in refs
    assert 372 in refs


def test_test_file_self_reference():
    text = pathlib.Path(__file__).read_text()
    assert '468' in text
    assert 'Type C' in text
    assert 'reach_amazon' in pathlib.Path(__file__).name
