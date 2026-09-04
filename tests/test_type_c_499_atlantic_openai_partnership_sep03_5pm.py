"""
Type C #499: The Atlantic x OpenAI strategic content and product partnership
(May 29 2024) - tracked-publication direct deal with pre-announcement
anti-deal op-ed irony.
- Iteration #499 Type C Financial Incentive Mapping Sep 3 2026 17:00 PDT
- Rotation 498 B -> 499 C.
- First dedicated Atlantic-deal mechanism in the repo. The Atlantic is itself
  a tracked publication (direct publication-to-competitor tie, not
  owner-level). Previously the Atlantic x OpenAI deal appeared only as
  one-line field values (openai_deal: May 2024, undisclosed) with no dedicated
  mechanism (grep verified), no test_type_c Atlantic file, no Type C commit
  mapping the deal. Existing Atlantic work covers ownership (atlantic.yaml)
  and Type A coverage analysis (mechanism 481).
- Findings (VentureBeat opened first-hand via browser.open this run;
  OpenAI announcement text via search-result excerpt; Nieman Lab, TheWrap,
  Engadget, Digiday, the-decoder, Fast Company, Slashdot x2 via verbatim
  search-result URLs/excerpts; TechCrunch Jun 2024 carried first-hand from
  mechanism 494): May 29 2024 strategic content and product partnership,
  Axios/Sara Fischer scoop, same day as the Vox deal (#494); counterparties
  Nicholas Thompson (Atlantic CEO) and Brad Lightcap (OpenAI COO, same signer
  as #494 Vox and #489 Hearst); Atlantic as premium news source in ChatGPT
  with attribution and link-back; archive licensed for training; Atlantic
  product team privileged OpenAI tech access; Atlantic Labs experimental
  microsite; multiyear (TheWrap), two-year per TechCrunch; terms undisclosed;
  pre-deal irony - Jessica Lessin's Atlantic op-ed ('media companies are
  making a huge mistake with AI') published days before, quoted back at
  management by the Atlantic union; Damon Beres 'A Devil's Bargain With
  OpenAI'; union 'deeply troubled by the opaque agreement'; Aug 2024 letter
  from ~60 journalists demanding AI contract protections; ChatGPT gibberish-
  URL attribution failures; Thompson LinkedIn video response ('hedge our
  bets'); Emerson Collective ownership cross-referenced not duplicated;
  Meta contrast $0 from Meta.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Sources (research provenance per mechanism research_method, Sep 3 2026):
- OpenAI announcement (May 29 2024, text via search excerpt)
  https://openai.com/index/enhancing-news-in-chatgpt-with-the-atlantic/
- Nieman Lab on Thompson/Lessin/Beres (search excerpt)
  https://www.niemanlab.org/2024/06/if-its-good-for-the-company-now-work-with-them-the-atlantic-ceo-on-signing-a-deal-with-openai/
- TheWrap on multiyear terms (search excerpt)
  https://www.thewrap.com/vox-the-atlantic-chatgpt-openai-deal/
- Engadget on the pre-deal screed irony (search excerpt)
  https://Www.engadget.com/the-atlantic-and-vox-media-made-their-own-deal-with-the-ai-devil-161017636.html
- TechCrunch on newsroom reaction (first-hand in #494)
  https://techcrunch.com/2024/06/22/whats-in-it-for-us-journalists-ask-as-publications-sign-content-deals-with-openai/
- VentureBeat announcement coverage (opened first-hand this run)
  https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media
- Slashdot/Ars Technica on union statements (search excerpts)
  https://news.slashdot.org/story/24/06/01/0245209/journalists-deeply-troubled-by-openais-content-deals-with-vox-the-atlantic
  https://slashdot.org/story/24/08/03/020259/journalists-at-the-atlantic-demand-assurances-their-jobs-will-be-protected-from-openai?utm_source=rss0.9mainlinkanon&utm_medium=feed
- Digiday on deal pros/cons incl. Lessin quotes (search excerpt)
  https://digiday.com/media/the-pros-and-cons-of-publishers-ai-licensing-deals/
- the-decoder on the Lessin 'relative pennies' quote (search excerpt)
  https://the-decoder.com/vox-media-and-the-atlantic-signed-licensing-agreements-with-openai/?amp=1
- Fast Company portfolio list (search excerpt)
  https://www.FastCompany.com/91130785/companies-reddit-news-corp-deals-openai-train-chatgpt-partnerships
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_499_atlantic_openai_strategic_partnership'
NEXT_MECH_KEY = 'mechanism_473_future_plc_openai_strategic_partnership:'

EXPECTED_URLS = [
    'https://openai.com/index/enhancing-news-in-chatgpt-with-the-atlantic/',
    'https://www.niemanlab.org/2024/06/if-its-good-for-the-company-now-work-with-them-the-atlantic-ceo-on-signing-a-deal-with-openai/',
    'https://www.thewrap.com/vox-the-atlantic-chatgpt-openai-deal/',
    'https://Www.engadget.com/the-atlantic-and-vox-media-made-their-own-deal-with-the-ai-devil-161017636.html',
    'https://techcrunch.com/2024/06/22/whats-in-it-for-us-journalists-ask-as-publications-sign-content-deals-with-openai/',
    'https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media',
    'https://news.slashdot.org/story/24/06/01/0245209/journalists-deeply-troubled-by-openais-content-deals-with-vox-the-atlantic',
    'https://slashdot.org/story/24/08/03/020259/journalists-at-the-atlantic-demand-assurances-their-jobs-will-be-protected-from-openai?utm_source=rss0.9mainlinkanon&utm_medium=feed',
    'https://digiday.com/media/the-pros-and-cons-of-publishers-ai-licensing-deals/',
    'https://the-decoder.com/vox-media-and-the-atlantic-signed-licensing-agreements-with-openai/?amp=1',
    'https://www.FastCompany.com/91130785/companies-reddit-news-corp-deals-openai-train-chatgpt-partnerships',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_raw():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return f.read()


def get_mech():
    data = load_entities()
    return data['entities']['openai'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_499_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 499
    assert mech['iteration'] == 499


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-03'
    assert mech['time_pdt'] == '17:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_announcement_date():
    mech = get_mech()
    assert mech['announcement_date'] == '2024-05-29'


def test_deal_structure_counterparties_and_scope():
    mech = get_mech()
    struct = mech['deal_structure']
    assert 'Nicholas Thompson' in struct['counterparties']
    assert 'Brad Lightcap' in struct['counterparties']
    assert 'Sara Fischer' in struct['scoop']
    assert 'premium news source' in struct['reach_and_attribution']
    assert 'theatlantic.com' in struct['reach_and_attribution']
    assert 'Atlantic Labs' in struct['atlantic_labs']
    assert 'multiyear' in struct['term_shape']
    assert 'two-year' in struct['term_shape']


def test_deal_terms_opacity():
    mech = get_mech()
    opacity = mech['deal_terms_opacity']
    assert opacity['exact_amount_undisclosed'] is True
    assert 'not immediately disclosed' in opacity['amount_evidence']
    assert '478' in opacity['opacity_pattern']
    assert '494' in opacity['opacity_pattern']


def test_pre_deal_anti_deal_irony():
    mech = get_mech()
    irony = mech['pre_deal_anti_deal_irony']
    assert 'Jessica Lessin' in irony['lessin_op_ed']
    assert 'huge mistake' in irony['lessin_op_ed']
    assert 'never, ever works as planned' in irony['lessin_quote_platforms']
    assert 'settling without litigation' in irony['lessin_quote_settling']
    assert 'relative pennies' in irony['lessin_quote_pennies']
    assert 'petty cash' in irony['contemporary_framing']


def test_newsroom_and_union_opposition():
    mech = get_mech()
    opp = mech['newsroom_and_union_opposition']
    assert 'deeply troubled' in opp['atlantic_union_statement']
    assert 'opaque agreement' in opp['atlantic_union_statement']
    assert 'Lessin' in opp['union_quotes_lessin']
    assert "Devil's Bargain" in opp['damon_beres']
    assert '60' in opp['august_2024_letter']
    assert 'gibberish' in opp['attribution_failures']
    assert 'not a syndication' in opp['no_syndication_guardrail']
    assert 'fairly insulated' in opp['all_hands']
    assert '494' in opp['analytical_note']


def test_thompson_public_response():
    mech = get_mech()
    resp = mech['thompson_public_response']
    assert 'LinkedIn' in resp['linkedin_video']
    assert 'hedge our bets' in resp['hedge_quote']
    assert 'navigate the web' in resp['discoverability_quote']


def test_ownership_layer_crossref_not_duplicated():
    mech = get_mech()
    own = mech['ownership_layer_crossref']
    assert 'Emerson Collective' in own['pointer']
    assert 'NOT duplicated' in own['pointer']
    assert 'atlantic.yaml' in own['pointer']


def test_meta_contrast():
    mech = get_mech()
    assert '$0 from Meta' in mech['meta_contrast']
    assert 'CORRELATION NOT CAUSATION' in mech['meta_contrast']


def test_mediascope_relevance_tracked_publication():
    mech = get_mech()
    rel = mech['mediascope_relevance']
    assert 'First dedicated Atlantic-deal mechanism' in rel
    assert 'tracked publication' in rel
    assert '481' in rel
    assert 'Type A' in rel


def test_statistical_discipline():
    mech = get_mech()
    disc = mech['statistical_discipline']
    assert disc['correlation_not_causation'] is True
    assert disc['is_significant'] is False
    assert disc['tone_scores'] == 'none'
    assert disc['p_value'] == 'NOT_CALCULATED'


def test_ranked_confounders():
    mech = get_mech()
    confs = mech['ranked_confounders']
    assert len(confs) == 4
    strengths = [c['strength'] for c in confs]
    assert strengths[0] == 'strong'
    assert strengths.count('moderate') == 2
    assert strengths[3] == 'weak'
    assert any('issuer communications' in c['confounder'] for c in confs)
    assert any('policy-blocked' in c['confounder'] for c in confs)


def test_research_method_marks_first_hand():
    mech = get_mech()
    assert 'opened first-hand' in mech['research_method']
    assert 'VentureBeat' in mech['research_method']


def test_source_urls():
    mech = get_mech()
    assert mech['source_urls'] == EXPECTED_URLS


def test_no_em_dash_or_nul_in_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index(NEXT_MECH_KEY)
    block = raw[start:end]
    assert '\u2014' not in block
    assert '\u2013' not in block
    assert '\x00' not in block
    assert block.isascii()


def test_mechanism_uniqueness_repo_wide():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1
    assert raw.count('mechanism_id: 499') == 1
