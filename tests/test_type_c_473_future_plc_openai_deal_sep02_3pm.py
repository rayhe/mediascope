"""
Type C #473: Future plc - OpenAI strategic partnership (Dec 5 2024)
- Iteration #473 Type C Financial Incentive Mapping Sep 2 2026 15:00 PDT
- Future plc (UK specialist publisher, LSE: FUTR, 200+ brands incl. Tom's Guide,
  TechRadar, PC Gamer) signed a content licensing and strategic partnership deal
  with OpenAI on Dec 5 2024. Payment involved but described by the company as
  "not financially material" (Press Gazette tracker paraphrase)
- ChatGPT surfaces Future content with attribution and links; Future already ran
  OpenAI-powered chatbots on Tom's Hardware and Who What Wear and uses OpenAI
  tools across sales, marketing, and editorial
- Wearables-beat relevance: Tom's Guide and TechRadar are leading smart-glasses
  review outlets, so the OpenAI financial tie sits directly on the beat that
  covers Meta vs competitor wearables
- Press Ranger/OtterlyAI study (mechanism 249) ranks Future plc the #1 AI citation
  beneficiary among OpenAI-licensed publishers (+48% ChatGPT citations)
- Meta has zero known AI licensing or content deals with Future plc
- Structural financial mapping only; correlation not causation; no tone scores,
  no p_value, no significance claim

Sources (observed Sep 2 2026 UTC):
- Press Gazette AI deals/lawsuits tracker (updated Sep 1 2026, Future section
  dated 5 December 2024, "not financially material" company statement)
  https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Digiday 2024 deals timeline (Dec 5 Future & OpenAI entry, chatbot/tooling detail)
  https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/
- Technology Mag, GameDeveloper, Maginative deal reports (brand list, quotes)
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

PG_URL = 'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/'
DIGIDAY_URL = 'https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/'


def load_entities():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_mech():
    data = load_entities()
    return data['entities']['openai']['mechanism_473_future_plc_openai_strategic_partnership']


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_473_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 473
    assert mech['iteration'] == 473


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date'] == '2026-09-02'
    assert mech['time_pdt'] == '15:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_publisher_identity():
    mech = get_mech()
    assert 'Future plc' in mech['publisher']
    assert '200+' in mech['publisher']


def test_counterparty_and_deal_date():
    mech = get_mech()
    assert mech['tech_counterparty'] == 'OpenAI'
    assert mech['deal_date'] == '2024-12-05'


def test_key_brands_include_wearables_review_outlets():
    mech = get_mech()
    brands = mech['key_brands']
    assert "Tom's Guide" in brands
    assert 'TechRadar' in brands
    assert 'PC Gamer' in brands
    assert len(brands) >= 8


def test_scope_attribution_and_links():
    mech = get_mech()
    assert 'attribution' in mech['scope']
    assert 'links' in mech['scope']


def test_payment_not_financially_material():
    mech = get_mech()
    assert 'not financially material' in mech['payment_terms']
    assert 'Press Gazette' in mech['payment_terms']


def test_preexisting_openai_deployment():
    mech = get_mech()
    pre = mech['preexisting_deployment']
    assert "Tom's Hardware" in pre
    assert 'Who What Wear' in pre
    assert 'sales' in pre


def test_executive_quotes_present():
    mech = get_mech()
    quotes = mech['executive_quotes']
    assert 'brad_lightcap_openai_coo' in quotes
    assert 'jon_steinberg_future_ceo' in quotes


def test_wearables_beat_relevance():
    mech = get_mech()
    rel = mech['wearables_beat_relevance']
    assert "Tom's Guide" in rel
    assert 'TechRadar' in rel
    assert 'smart glasses' in rel
    assert 'caswell' in rel.lower()


def test_citation_study_link_number_one_beneficiary():
    mech = get_mech()
    link = mech['citation_study_link']
    assert 'number 1' in link
    assert '249' in link
    assert '48 percent' in link


def test_meta_contrast_zero_deals():
    mech = get_mech()
    assert 'zero known' in mech['meta_contrast']
    assert 'Future plc' in mech['meta_contrast'] or 'Future' in mech['meta_contrast']


def test_statistical_discipline():
    mech = get_mech()
    disc = mech['statistical_discipline']
    assert disc['correlation_not_causation'] is True
    assert disc['is_significant'] is False
    assert disc['no_tone_scores'] is True
    assert disc['no_p_value'] is True


def test_confounders_ranked():
    mech = get_mech()
    conf = mech['confounders_ranked']
    assert len(conf['strong']) >= 2
    assert len(conf['moderate']) >= 1
    assert len(conf['weak']) >= 1
    strong_text = ' '.join(conf['strong'])
    assert 'single secondary source' in strong_text


def test_novelty_verification_notes():
    mech = get_mech()
    nov = mech['novelty_verification']
    assert 'zero hits' in nov
    assert '#468' in mech['distinct_from_prior']
    assert '#249' in mech['distinct_from_prior']


def test_portfolio_list_gap_closed():
    mech = get_mech()
    assert mech['portfolio_list_gap_closed'] is not None
    raw = get_raw()
    assert '- Future plc (Dec 2024)' in raw


def test_source_urls_https_only():
    mech = get_mech()
    urls = mech['source_urls']
    assert len(urls) >= 5
    for url in urls:
        assert url.startswith('https://'), url
    assert PG_URL in urls
    assert DIGIDAY_URL in urls


def test_no_em_dash_in_new_block():
    raw = get_raw()
    start = raw.index('mechanism_473_future_plc_openai_strategic_partnership')
    end = raw.index('  anthropic:', start)
    block = raw[start:end]
    assert '\u2014' not in block
    assert '\u2013' not in block


def test_mechanism_473_unique_in_file():
    raw = get_raw()
    assert raw.count('mechanism_473_future_plc_openai_strategic_partnership') == 1
    assert raw.count('mechanism_id: 473') == 1


def test_no_causal_claim_language():
    mech = get_mech()
    text = str(mech)
    assert 'proves' not in text.lower()
    assert 'causes softer coverage' not in text.lower()
