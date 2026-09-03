"""
Type C #489: Hearst x OpenAI strategic content partnership (Oct 8 2024) and
Amazon Rufus dual-AI-payer mapping.
- Iteration #489 Type C Financial Incentive Mapping Sep 3 2026 07:00 PDT
- Rotation 488 B -> 489 C.
- First dedicated Hearst mechanism in the repo. Hearst (Oct 2024) previously
  appeared only as a portfolio-list name in
  publisher_content_deal_portfolio.notable_partners and in Amazon-deal impact
  lists; no dedicated mechanism existed (grep verified), no test_hearst* file,
  no Type C commit with Hearst in the title.
- Findings (party announcements plus contemporaneous reporting opened first-hand
  via browser.open this run): 20+ magazine brands and 40+ newspapers into OpenAI
  products (Houston Chronicle, SF Chronicle, Esquire, Cosmopolitan, ELLE,
  Runner's World, Women's Health named); ChatGPT 200M-weekly-user reach claim in
  both announcements; citations plus direct links; counterparties Jeff Johnson
  (Hearst Newspapers), Debi Chirichella (Hearst Magazines), Brad Lightcap (OpenAI
  COO); non-magazine/newspaper businesses excluded; NO financial terms, term
  length disclosed; no ad-tech collaboration unlike the Dotdash Meredith deal;
  WGAE filed a formal information request in opposition (Wheeler quotes);
  pre-existing entanglement via the OpenAI/Brown Institute/Hearst co-hosted AI
  and Journalism Summit; second payer mapped as Amazon Rufus multi-year deal
  (Jul 10 2025, Digiday, Hearst spokesperson confirmed, terms undisclosed),
  making Hearst a dual-AI-payer companion to mechanism 437 (FT: OpenAI plus
  Google); Hearst is absent from Meta's 13-partner AI licensing list, so $0
  from Meta.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Sources (opened via browser.open first-hand this run, Sep 3 2026, unless noted):
- Hearst announcement (Oct 8 2024)
  https://www.hearst.com/-/hearst-and-openai-announce-strategic-content-partnership
- OpenAI announcement mirror
  https://openai.com/index/hearst/
- Engadget on the OpenAI deal (no ad-tech collaboration distinction)
  https://www.engadget.com/ai/openai-partners-with-cosmopolitan-and-elle-publisher-hearst-180517248.html/
- TheWrap on the OpenAI deal (terms undisclosed)
  https://www.thewrap.com/openai-hearst-content-licensing-partnership/
- TheWrap on WGAE opposition (information request, Wheeler quotes)
  https://www.thewrap.com/wgae-hearst-openai-deal-statement/
- Engadget on the Amazon Rufus deal (spokesperson-confirmed, multi-year,
  terms undisclosed)
  https://www.engadget.com/big-tech/amazon-strikes-ai-licensing-deal-with-hearst-and-conde-nast-134849930.html
- Digiday on the Amazon Rufus deal (Jul 10 2025, Jessica Davies; URL from
  search, page not opened first-hand)
  https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/
- Glossy corroboration of the Rufus deal (URL from search)
  https://www.glossy.co/fashion/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/
- OpenAI Academy announcement (AI and Journalism Summit co-hosted with Brown
  Institute and Hearst)
  https://openai.com/index/openai-academy-for-news-organizations/
- Fast Company (The Information Jan 2024 benchmark band 1-5M USD/yr)
  https://www.FASTCOMPANY.COM/91116001/financial-times-openai-licensing-deal
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

HEARST_URL = 'https://www.hearst.com/-/hearst-and-openai-announce-strategic-content-partnership'
OPENAI_URL = 'https://openai.com/index/hearst/'
ENGADGET_OPENAI_URL = 'https://www.engadget.com/ai/openai-partners-with-cosmopolitan-and-elle-publisher-hearst-180517248.html/'
THEWRAP_DEAL_URL = 'https://www.thewrap.com/openai-hearst-content-licensing-partnership/'
THEWRAP_WGAE_URL = 'https://www.thewrap.com/wgae-hearst-openai-deal-statement/'
ENGADGET_RUFUS_URL = 'https://www.engadget.com/big-tech/amazon-strikes-ai-licensing-deal-with-hearst-and-conde-nast-134849930.html'
DIGIDAY_RUFUS_URL = 'https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/'
GLOSSY_RUFUS_URL = 'https://www.glossy.co/fashion/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/'
OPENAI_ACADEMY_URL = 'https://openai.com/index/openai-academy-for-news-organizations/'
FASTCO_URL = 'https://www.FASTCOMPANY.COM/91116001/financial-times-openai-licensing-deal'

MECH_KEY = 'mechanism_489_hearst_openai_dual_ai_payer_partnership'

EXPECTED_BRANDS = ['Houston Chronicle', 'San Francisco Chronicle', 'Esquire',
                   'Cosmopolitan', 'ELLE', "Runner's World", "Women's Health"]


def load_entities():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_mech():
    data = load_entities()
    return data['entities']['openai'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_489_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 489
    assert mech['iteration'] == 489


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-03'
    assert mech['time_pdt'] == '07:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_announcement_date():
    mech = get_mech()
    assert mech['announcement_date'] == '2024-10-08'


def test_deal_structure_brands():
    mech = get_mech()
    struct = mech['deal_structure']
    assert struct['brands_named'] == EXPECTED_BRANDS
    assert '20+' in struct['content_scope']
    assert '40+' in struct['content_scope']
    assert '200 million' in struct['reach_claim']
    assert 'citations and direct links' in struct['integration_model']
    assert 'Jeff Johnson' in struct['hearst_counterparties']
    assert 'Debi Chirichella' in struct['hearst_counterparties']
    assert 'Brad Lightcap' in struct['openai_counterparty']


def test_deal_structure_scope_exclusion_and_distinction():
    mech = get_mech()
    struct = mech['deal_structure']
    assert 'NOT' in struct['scope_exclusion']
    assert 'Fitch Group' in struct['scope_exclusion']
    assert 'Dotdash Meredith' in struct['structural_distinction']
    assert 'no ad-tech collaboration' in struct['structural_distinction']


def test_deal_terms_opacity():
    mech = get_mech()
    op = mech['deal_terms_opacity']
    assert op['exact_amount_undisclosed'] is True
    assert op['term_length_undisclosed'] is True
    assert 'TheWrap' in op['evidence'] or 'Engadget' in op['evidence']
    assert '1 to 5 million' in op['benchmark_band']
    assert 'not an outlier' in op['opacity_pattern']


def test_amazon_rufus_second_payer():
    mech = get_mech()
    rufus = mech['amazon_rufus_second_payer']
    assert rufus['announcement_date'] == '2025-07-10'
    assert 'Digiday' in rufus['reported_by']
    assert 'multi-year' in rufus['form']
    assert 'spokesperson' in rufus['hearst_scope']
    assert rufus['terms_undisclosed'] is True
    assert '437' in rufus['dual_payer_significance']


def test_labor_opposition():
    mech = get_mech()
    labor = mech['labor_opposition']
    assert 'WGAE' in labor['actor'] or 'Writers Guild' in labor['actor']
    assert 'Sam Wheeler' in labor['actor']
    assert 'information request' in labor['action']
    assert 'failing tech startup' in labor['verdict_quote']
    assert "robot" in labor['verdict_quote']
    joined = labor['concerns_raised']
    assert 'profit' in joined
    assert 'obsolete' in joined


def test_pre_existing_entanglement():
    mech = get_mech()
    ent = mech['pre_existing_entanglement']
    joined = ' '.join(ent)
    assert 'AI and Journalism Summit' in joined
    assert 'Brown Institute' in joined
    assert 'bounds sudden-capture' in joined


def test_meta_contrast():
    mech = get_mech()
    mc = mech['meta_contrast']
    assert '13' in mc
    assert 'News Corp' in mc
    assert '$0 from Meta' in mc
    assert 'CORRELATION' in mc and 'CAUSATION' in mc


def test_statistical_discipline():
    mech = get_mech()
    sd = mech['statistical_discipline']
    assert sd['correlation_not_causation'] is True
    assert sd['is_significant'] is False
    assert sd['p_value'] == 'NOT_CALCULATED'
    assert sd['tone_scores'] == 'none'


def test_ranked_confounders():
    mech = get_mech()
    confs = mech['ranked_confounders']
    assert len(confs) == 4
    assert [c['rank'] for c in confs] == [1, 2, 3, 4]
    assert confs[0]['strength'] == 'strong'
    assert 'party' in confs[0]['confounder'] or 'announcements' in confs[0]['confounder']
    assert confs[1]['strength'] == 'moderate'
    assert 'WGAE' in confs[1]['confounder'] or 'labor' in confs[1]['confounder']
    assert confs[2]['strength'] == 'moderate'
    assert 'coverage-tone' in confs[2]['confounder']


def test_cross_references():
    mech = get_mech()
    joined = ' '.join(mech['cross_references'])
    assert 'notable_partners' in joined
    assert '437' in joined
    assert '478' in joined
    assert '483' in joined


def test_novelty_verification():
    mech = get_mech()
    joined = ' '.join(mech['novelty_verification'])
    assert 'portfolio-list name' in joined
    assert 'test_hearst' in joined
    assert 'Not Microsoft PCM related' in joined


def test_source_urls():
    mech = get_mech()
    urls = mech['source_urls']
    assert len(urls) == 10
    for u in (HEARST_URL, OPENAI_URL, ENGADGET_OPENAI_URL, THEWRAP_DEAL_URL,
              THEWRAP_WGAE_URL, ENGADGET_RUFUS_URL, DIGIDAY_RUFUS_URL,
              GLOSSY_RUFUS_URL, OPENAI_ACADEMY_URL, FASTCO_URL):
        assert u in urls
    for u in urls:
        assert u.startswith('https://'), u


def test_caution_bounds_claim():
    mech = get_mech()
    assert 'No coverage-tone claim is made' in mech['caution']


def test_no_em_dash_or_nul_in_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index('european_ad_expansion_dual_dependency_aug30:')
    block = raw[start:end]
    assert '\u2014' not in block
    assert '\u2013' not in block
    assert '\x00' not in block
    assert block.isascii()


def test_mechanism_uniqueness_repo_wide():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1
    assert raw.count('mechanism_id: 489') == 1
