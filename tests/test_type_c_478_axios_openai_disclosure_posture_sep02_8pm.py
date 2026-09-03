"""
Type C #478: Axios x OpenAI disclosure posture and deal-terms opacity mapping
- Iteration #478 Type C Financial Incentive Mapping Sep 2 2026 20:00 PDT
- Extends mechanism 53 (triple-layer journalism funding, Layer 2 Axios deal
  structure). This mechanism maps ONLY the disclosure posture, confidentiality
  terms, and CEO-stance reversal documented by CJR and Nieman Lab reporting
  opened first-hand this run. No duplicate deal-structure mapping.
- Findings: three-year OpenAI newsroom-funding deal (Jan 2025) has confidential
  payment terms (exact amount and legal-action-waiver status undisclosed; OpenAI
  spox Kayla Wood: confidential under the agreement); Axios does not disclose the
  deal in job listings ($65K-$125K) or most of its own OpenAI coverage (CJR);
  CEO Jim VandeHei criticized the "welfare-state mentality of companies begging
  OpenAI and Google for money" in Apr 2024 then accepted the deal 9 months later
  (Nieman Lab); deal text is "silent" on the editorial firewall and VandeHei's
  conflict test is "the market will set the relationship" (CJR).
- Counter-evidence recorded: Axios continued adversarial OpenAI coverage (teen
  suicide allegations, Musk litigation); local reporters in funded cities covered
  data center fights. Disclosure gap does not equal coverage softening.
- Statistical discipline: structural mapping only; correlation not causation;
  is_significant false; no tone scores; no p_value; qualitative only.

Sources (opened via browser.open this run, Sep 2 2026):
- CJR "Axios Wants to Save Local News with AI"
  https://www.cjr.org/feature/axios-wants-to-save-local-news-with-ai-jim-vandehei-tech-newsletters.php
- Nieman Lab "OpenAI will fund four Axios Local newsrooms"
  https://www.niemanlab.org/2025/01/openai-will-fund-four-axios-local-newsrooms-as-part-of-a-broader-partnership-focused-on-juicing-local-news/
- TechCrunch Jan 15 2025 (deal announcement)
  https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
- Adweek Jan 2026 (second round, 7-9 more cities)
  https://www.adweek.com/media/axios-local-openai-2026/
- OpenAI announcement
  https://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

CJR_URL = 'https://www.cjr.org/feature/axios-wants-to-save-local-news-with-ai-jim-vandehei-tech-newsletters.php'
NIEMAN_URL = 'https://www.niemanlab.org/2025/01/openai-will-fund-four-axios-local-newsrooms-as-part-of-a-broader-partnership-focused-on-juicing-local-news/'
TECHCRUNCH_URL = 'https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/'
ADWEEK_URL = 'https://www.adweek.com/media/axios-local-openai-2026/'
OPENAI_URL = 'https://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/'

MECH_KEY = 'mechanism_478_axios_openai_disclosure_posture'


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


def test_mechanism_478_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 478
    assert mech['iteration'] == 478


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-02'
    assert mech['time_pdt'] == '20:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_extends_mechanism_53_no_duplicate_structure():
    mech = get_mech()
    assert mech['extends_mechanism'] == 53
    scope = mech['extension_scope']
    assert 'ONLY' in scope or 'only' in scope
    assert 'No duplicate deal-structure mapping' in scope


def test_deal_terms_confidentiality():
    mech = get_mech()
    conf = mech['deal_terms_confidentiality']
    assert conf['exact_amount_undisclosed'] is True
    assert conf['legal_action_waiver_status_undisclosed'] is True
    assert 'Kayla Wood' in conf['on_record']
    assert 'confidential under the agreement' in conf['on_record']
    assert conf['term_years'] == 3


def test_disclosure_gap_job_listings_and_coverage():
    mech = get_mech()
    gap = mech['disclosure_gap']
    assert '65K' in gap['job_listings'] and '125K' in gap['job_listings']
    assert 'most' in gap['own_coverage']
    assert 'media deals' in gap['own_coverage']


def test_rank_and_file_unease_recorded():
    mech = get_mech()
    gap = mech['disclosure_gap']
    assert 'Holly Moore' in gap['rank_and_file_unease']


def test_vandehei_stance_reversal():
    mech = get_mech()
    rev = mech['vandehei_stance_reversal']
    assert 'welfare-state mentality' in rev['april_2024']
    assert 'VandeHei' in rev['april_2024'] or 'Jim VandeHei' in rev['april_2024']
    assert rev['interval_months'] == 9
    assert 'Sam Altman' in rev['january_2025']


def test_editorial_firewall_posture():
    mech = get_mech()
    fw = mech['editorial_firewall_posture']
    assert 'silent' in fw['deal_text']
    assert 'market will set the relationship' in fw['conflict_of_interest_test']


def test_counter_evidence_bounds_capture_claim():
    mech = get_mech()
    fw = mech['editorial_firewall_posture']
    ce = fw['counter_evidence_noted']
    assert 'Musk' in ce
    assert 'data center' in ce


def test_deepening_second_round():
    mech = get_mech()
    deep = mech['deepening']
    assert '2026' in deep['second_round']
    assert '13' in str(deep['bankrolled_count_cjr'])
    assert '43' in deep['target']


def test_structural_context():
    mech = get_mech()
    ctx = mech['structural_context']
    assert 'Cox Enterprises' in ctx['owner']
    assert '525M' in ctx['owner']
    assert 'Not unionized' in ctx['union_status']
    assert 'Chris Lehane' in ctx['openai_deal_champion']


def test_statistical_discipline():
    mech = get_mech()
    disc = mech['statistical_discipline']
    assert disc['correlation_not_causation'] is True
    assert disc['is_significant'] is False
    assert disc['no_tone_scores'] is True
    assert disc['no_p_value'] is True
    assert disc['qualitative_only'] is True


def test_ranked_confounders():
    mech = get_mech()
    confs = mech['ranked_confounders']
    assert len(confs) >= 4
    ranks = [c['rank'] for c in confs]
    assert ranks == sorted(ranks)
    strengths = {c['strength'] for c in confs}
    assert 'strong' in strengths


def test_cross_references():
    mech = get_mech()
    refs = mech['cross_references']
    joined = ' '.join(refs)
    assert '53' in joined
    assert '349' in joined


def test_novelty_verification():
    mech = get_mech()
    nov = mech['novelty_verification']
    joined = ' '.join(nov)
    assert 'VandeHei' in joined
    assert '53' in joined


def test_source_urls_https_only():
    mech = get_mech()
    urls = mech['source_urls']
    assert len(urls) >= 5
    for url in urls:
        assert url.startswith('https://'), url
    assert CJR_URL in urls
    assert NIEMAN_URL in urls
    assert TECHCRUNCH_URL in urls
    assert ADWEEK_URL in urls
    assert OPENAI_URL in urls


def test_no_em_dash_in_new_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index('    european_ad_expansion_dual_dependency_aug30:', start)
    block = raw[start:end]
    assert chr(0x2014) not in block
    assert chr(0x2013) not in block
    assert '\x00' not in block


def test_mechanism_478_unique_in_file():
    raw = get_raw()
    assert raw.count(MECH_KEY) == 1
    assert raw.count('mechanism_id: 478') == 1
