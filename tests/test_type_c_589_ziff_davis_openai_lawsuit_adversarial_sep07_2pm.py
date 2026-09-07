"""Type C #589: Ziff Davis v. OpenAI copyright lawsuit (filed Apr 24 2025, live through
Sep 2026) - first adversarial financial-incentive mechanism in the corpus: a publisher
suing the AI lab for hundreds of millions in damages is the inverse of the licensing-deal
incentives; owner-level tie to corpus-covered publications CNET and ZDNET.

- Iteration #589 Type C Financial Incentive Mapping Sep 7 2026 14:00 PDT
- Rotation 588 B -> 589 C.
- Novelty verified: zero mechanism keys matching ziff in profiles/competitor-entities.yaml
  before insertion (grep verified); no dedicated Ziff Davis lawsuit mechanism in
  iteration-log.md (grep verified); zero test_type_c_589 files on disk before this run
  (glob verified); no #589 in git log (grep verified). Existing ziff mentions are
  boundary notes (PCMag is Ziff Davis NOT DDM-owned), portfolio lists, NYT/Dow Jones
  publisher-lawsuit list lines, and CNET/ZDNET ownership fields - no mechanism.
- Findings (browser.search this run, 2 query sets, verbatim full-URL listings;
  case facts second-hand via search-result excerpts, bounded in-mechanism; no pages
  opened first-hand):
  - Filing Apr 24 2025, Delaware federal court (Reuters): 62-page complaint; claims
    direct copyright infringement, contributory copyright infringement,
    DMCA 1201 circumvention + CMI removal, unjust enrichment, trademark dilution;
    "intentionally and relentlessly" reproduced exact copies and derivatives;
    robots.txt ignored, copyright management information removed (MediaNama);
    relief sought includes stopping OpenAI use and destroying models/data with
    Ziff Davis works.
  - Damages: "at least hundreds of millions of dollars" (NYT via eWeek, two
    anonymous sources); share price down 40% in the year before filing (TheWrap).
  - Legal arc: Jun 10 2025 OpenAI moves to dismiss/stay; Oct 8 2025 oral argument;
    Dec 15 2025 (2025 WL 3635559) partial dismissal - claims 4/5 gone (unjust
    enrichment preempted, DMCA circumvention), claims 3/6/7 survive (direct,
    contributory, CMI removal), stay for newer models o1 through GPT-5;
    Dec 18 2025 leave for second amended complaint denied as futile (robots.txt
    not a technological measure); Aug 6 2026 contributory copyright + trademark
    dilution dismissed with prejudice (active) / without prejudice (stayed);
    Sep 2026 Bloomberg Law "OpenAI Wins Partial Dismissal". Core case live.
  - Portfolio: 45+ brands, ~2M articles/yr, 5,000+ product reviews; tech brands
    CNET, ZDNET, PCMag, Mashable, IGN, Lifehacker; CNET Media Inc. a named
    plaintiff. CNET and ZDNET are corpus-covered publications (#588, triple-squeeze).
  - Sue-one-sign-the-other: same week WaPo struck an OpenAI licensing partnership
    (TheWrap); complaint explicitly rejects the licensing market OpenAI was
    cultivating ("flouted copyright and trademark law and discredited its own
    pretext").
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED; no coverage-tone claim; no zero-coverage claims per iteration-492.

Source URLs (case facts second-hand via search excerpts this run, Sep 7 2026):
- https://www.reuters.com/business/publisher-ziff-davis-sues-openai-copyright-infringement-2025-04-24/
- https://www.thewrap.com/openai-sued-ziff-davis-chatgpt-copyright-infringement/
- https://www.medianama.com/2025/04/223-ziff-davis-accuses-openai-content-ai-training/
- https://www.eweek.com/news/ziff-davis-sues-openai/
- https://news.bloomberglaw.com/ip-law/openai-wins-partial-dismissal-of-ziff-davis-copyright-lawsuit
- https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2025cv04315/643043/571/0.pdf
- https://archive.org/download/gov.uscourts.nysd.640396/gov.uscourts.nysd.640396.968.0.pdf
- https://www.courtlistener.com/docket/70338311/605/ziff-davis-inc-v-openai-inc/
"""
import pathlib

import yaml

REPO = pathlib.Path(__file__).parent.parent
PROFILES_DIR = REPO / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
LOG = REPO / 'iteration-log.md'

MECH_KEY = 'ziff_davis_openai_lawsuit_adversarial_incentive_589'

EXPECTED_URLS = [
    'https://www.reuters.com/business/publisher-ziff-davis-sues-openai-copyright-infringement-2025-04-24/',
    'https://www.thewrap.com/openai-sued-ziff-davis-chatgpt-copyright-infringement/',
    'https://www.medianama.com/2025/04/223-ziff-davis-accuses-openai-content-ai-training/',
    'https://www.eweek.com/news/ziff-davis-sues-openai/',
    'https://news.bloomberglaw.com/ip-law/openai-wins-partial-dismissal-of-ziff-davis-copyright-lawsuit',
    'https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2025cv04315/643043/571/0.pdf',
    'https://archive.org/download/gov.uscourts.nysd.640396/gov.uscourts.nysd.640396.968.0.pdf',
    'https://www.courtlistener.com/docket/70338311/605/ziff-davis-inc-v-openai-inc/',
]


def load_doc():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_mech():
    return load_doc()[MECH_KEY]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_top_level_key_present(self):
        doc = load_doc()
        assert MECH_KEY in doc

    def test_mechanism_id_and_iteration_589(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 589
        assert mech['iteration'] == 589
        assert mech['iteration_type'] == 'C'

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['rotation'] == 'Type C'
        assert mech['date_analyzed'] == '2026-09-07'
        assert mech['time_pdt'] == '14:00'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_ziff_davis_openai_adversarial(self):
        name = get_mech()['mechanism_name']
        assert 'Ziff Davis' in name
        assert 'OpenAI' in name
        assert 'adversarial' in name


class TestFilingFacts:
    def test_filing_date_apr_24_2025(self):
        assert get_mech()['filing']['date'] == '2025-04-24'

    def test_delaware_filing_consolidated_sdny(self):
        court = get_mech()['filing']['court_filed']
        assert 'Delaware' in court
        assert '1:25-md-03143' in court

    def test_judge_stein(self):
        assert 'Sidney H. Stein' in get_mech()['filing']['judge']

    def test_cnet_media_named_plaintiff(self):
        assert 'CNET Media, Inc.' in get_mech()['filing']['plaintiffs']

    def test_five_claims_listed(self):
        claims = get_mech()['filing']['claims']
        assert len(claims) == 5
        assert 'direct copyright infringement' in claims
        assert 'trademark dilution' in ' '.join(claims)

    def test_intentionally_and_relentlessly_allegation(self):
        joined = ' '.join(get_mech()['filing']['key_allegations'])
        assert 'intentionally and relentlessly' in joined

    def test_robots_txt_allegation(self):
        joined = ' '.join(get_mech()['filing']['key_allegations'])
        assert 'robots.txt' in joined

    def test_move_fast_and_break_things_quote(self):
        joined = ' '.join(get_mech()['filing']['key_allegations'])
        assert 'move fast and break things' in joined

    def test_licensing_market_rejection_quote(self):
        quote = get_mech()['filing']['licensing_market_quote']
        assert 'flouted copyright and trademark law' in quote

    def test_damages_floor_hundreds_of_millions(self):
        assert 'hundreds of millions of dollars' in get_mech()['damages']['reported_floor']


class TestLegalArcFacts:
    def test_six_arc_entries(self):
        assert len(get_mech()['legal_arc']) == 6

    def test_dec_2025_partial_dismissal_surviving_claims(self):
        joined = ' '.join(get_mech()['legal_arc'])
        assert '2025-12-15' in joined
        assert 'claims 3, 6, 7' in joined

    def test_newer_model_stay(self):
        joined = ' '.join(get_mech()['legal_arc'])
        assert 'GPT-5' in joined

    def test_robots_txt_denied_as_futile(self):
        joined = ' '.join(get_mech()['legal_arc'])
        assert '2025-12-18' in joined
        assert 'futile' in joined

    def test_aug_2026_with_prejudice_trim(self):
        joined = ' '.join(get_mech()['legal_arc'])
        assert '2026-08-06' in joined
        assert 'WITH PREJUDICE' in joined

    def test_sep_2026_bloomberg_partial_dismissal(self):
        joined = ' '.join(get_mech()['legal_arc'])
        assert 'Partial Dismissal' in joined

    def test_openai_fair_use_response(self):
        joined = ' '.join(get_mech()['openai_response'])
        assert 'fair use' in joined


class TestPortfolioAndOwnerTie:
    def test_brand_count_and_output(self):
        port = get_mech()['portfolio']
        assert '45+' in port['brand_count']
        assert '2M' in port['annual_output']

    def test_tech_brands_include_cnet_zdnet(self):
        brands = ' '.join(get_mech()['portfolio']['tech_brands'])
        assert 'CNET' in brands
        assert 'ZDNET' in brands

    def test_cnet_owner_tie_and_588_reference(self):
        tie = get_mech()['owner_publication_tie']
        assert 'CNET Media, Inc.' in tie['cnet']
        assert '588' in tie['cnet']

    def test_negative_sign_asserted(self):
        assert 'negative' in get_mech()['owner_publication_tie']['sign']

    def test_sue_one_sign_other_wapo(self):
        joined = ' '.join(get_mech()['sue_one_sign_other'])
        assert 'Washington Post' in joined


class TestAdversarialIncentiveStructure:
    def test_first_adversarial_mechanism_class(self):
        model = get_mech()['adversarial_incentive_model']
        assert 'first in corpus' in model['mechanism_class']
        assert 'adversarial' in model['mechanism_class']

    def test_vector_is_damages_plus_leverage(self):
        vector = get_mech()['adversarial_incentive_model']['vector']
        assert 'damages' in vector

    def test_prediction_is_mirror_image(self):
        pred = get_mech()['adversarial_incentive_model']['prediction']
        assert 'mirror image' in pred

    def test_bounded_no_tone_claim(self):
        assert 'no tone claim' in get_mech()['adversarial_incentive_model']['bounded']


class TestConfoundersAndDiscipline:
    def test_five_confounders_ranked(self):
        assert len(get_mech()['confounders_ranked']) == 5

    def test_strong_confounders_first(self):
        con = get_mech()['confounders_ranked']
        assert con[0].startswith('STRONG:')
        assert con[1].startswith('STRONG:')

    def test_statistical_discipline_not_calculated(self):
        disc = get_mech()['statistical_discipline']
        assert disc['is_significant'] is False
        assert disc['p_value'] == 'NOT_CALCULATED'
        assert disc['cohens_d'] == 'NOT_CALCULATED'
        assert disc['tone_scores'] == 'NOT_SCORED'

    def test_correlational_note_covers_adversarial(self):
        note = get_mech()['correlational_note']
        assert 'correlation' in note
        assert 'Adversarial' in note

    def test_cautious_language_and_no_tone_claim(self):
        mech = get_mech()
        assert mech['cautious_language_required'] is True
        assert mech['no_coverage_tone_claim'] is True


class TestNoveltyAndSources:
    def test_sources_list_matches_expected_urls(self):
        srcs = get_mech()['sources']
        assert len(srcs) == len(EXPECTED_URLS)
        for url in EXPECTED_URLS:
            assert url in srcs

    def test_reuters_is_first_source(self):
        assert 'reuters.com' in get_mech()['sources'][0]

    def test_novelty_names_firsts_and_distinctions(self):
        nov = get_mech()['novelty']
        assert 'first dedicated Ziff Davis mechanism' in nov
        assert 'first adversarial' in nov
        assert 'mechanism 588' in nov

    def test_research_method_names_query_sets(self):
        assert '2 browser.search query sets' in get_mech()['research_method']

    def test_verification_block(self):
        ver = get_mech()['verification']
        assert ver['iteration'] == 589
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-07 14:00 PDT'
        assert ver['yaml_parse_clean'] is True
        assert ver['ascii_only'] is True

    def test_iteration_log_mentions_589(self):
        text = LOG.read_text(encoding='utf-8')
        assert '#589 Type C' in text
        assert 'Ziff Davis' in text
