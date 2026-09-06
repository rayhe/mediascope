"""
Type C #559: Amazon x New York Times AI Content Licensing Deal (May 29 2025) -
$20-25M/Yr, Amazon's First Publisher AI Deal, NYT's First AI Licensing Pact,
First Dedicated Mechanism for an Amazon Deal With a Tracked Publication
- Iteration #559 Type C Financial Incentive Mapping Sep 6 2026 07:00 PDT
- Rotation 558 B -> 559 C.
- Novelty verified: zero dedicated amazon_x_nyt / Amazon x NYT mechanism blocks
  in profiles/competitor-entities.yaml before insertion (grep verified - only
  portfolio-list lines in mechanism 468 amazon_publisher_portfolio_after_deal,
  valuation-control citations, and nytimes.yaml financial lines); zero dedicated
  Conde Nast x Amazon or Hearst x Amazon mechanism blocks (grep verified);
  zero test files with 559 on disk before this run (glob verified); no Type C
  commit with 559 in the title (git log --grep verified).
  Distinct from mechanism 468 (Reach plc x Amazon Mar 2026, usage-based FOURTH
  Amazon deal - this mechanism is the FIRST Amazon publisher deal, flat-fee),
  mechanisms 371/372 (Amazon publisher leverage matrices - this mechanism
  supplies the flagship tracked-publication anchor deal), mechanism 549
  (News Corp x Meta $50M/yr Mar 2026 - the Meta-leg counterpart), mechanism 509
  (Anthropic zero-deal posture - Amazon is the lab that DID pay), mechanism 504
  (Conde Nast x OpenAI Aug 2024 - dual-payer publisher), and mechanism 489
  (Hearst x OpenAI - dual-payer publisher). First mechanism for an Amazon AI
  licensing deal with one of the seven tracked MediaScope publications (NYT).
- Findings (browser.search this run, verbatim full-URL listings; deal facts
  via search-result excerpts, second-hand, marked bounded in-mechanism):
  - Deal: announced May 29, 2025 via NYT company news release (Thursday);
    GeekWire May 29 2025 8:17am PT; TechTarget May 29 2025; AFP wire via
    spacedaily May 29 2025; Digiday 2025 publisher AI deals timeline
    'May 29: The New York Times and Amazon'.
  - Terms: disclosed Jul 30, 2025 by WSJ (Alexandra Bruell), 'people familiar
    with the matter': $20-25M/yr, multiyear (length undisclosed), amounting to
    nearly 1% of NYT's total 2024 revenue. Reprinted by Editor and Publisher,
    GeekWire, PYMNTS, The Wrap, eWeek, Engadget, livemint.
  - Scope: NYT editorial content, NYT Cooking, The Athletic; real-time
    summaries/short excerpts within Amazon products incl. Alexa; training of
    Amazon's proprietary foundation models; direct links back to Times
    products.
  - Firsts: Amazon's first AI-related publisher licensing agreement AND the
    NYT's first AI-related licensing pact (multiple outlets).
  - Sue/deal bifurcation: NYT sued OpenAI and Microsoft for copyright
    infringement Dec 2023 (federal judge rejected parts of dismissal motion
    Apr 2025, suit ongoing at Jul 2025 terms disclosure); instead of settling,
    the Times licensed to Amazon. Most prominent sue-one-lab-license-another
    case in the corpus.
  - Executive quotes: Levien (announcement) 'high-quality journalism is worth
    paying for'; Levien Q1 2026 earnings 'We've done a partnership with Amazon
    because it met those conditions. And so far, so good'; NYT stock +1.85% on
    announcement day, near all-time high (AFP).
  - Amazon publisher portfolio sequencing: NYT (May 29 2025, flat, first) ->
    Conde Nast (Rufus, Jul 15 2025) -> Hearst (Rufus, Jul 15 2025) -> Reach
    plc (usage-based, Mar 2 2026, #468).
  - Affiliate-to-licensing substitution: Wirecutter heavily Amazon-Associates
    dependent (~$50-100M+ estimated annual Amazon affiliate revenue, corpus
    derivation); Amazon quietly restructured Associates in early 2026 (Adweek,
    seven publishers confirmed); a 30-50% commission cut could cost NYT
    $15-50M+/yr; the fixed $20-25M/yr licensing payment hedges affiliate
    exposure (structural observation, not a coverage claim).
  - Directional predictions (predictions, not findings): Amazon softer (direct
    payer, largest documented Amazon publisher payment); OpenAI adversarial
    slot (being sued, zero-deal); Microsoft adversarial slot (co-defendant);
    Meta neutral to no-deal (13-publisher portfolio, none tracked); Google
    neutral to no-deal (no NYT deal; NYT 10-Q flags Google traffic reduction).
  - Structural contrasts: 468 (fourth Amazon deal, usage-based), 371/372
    (leverage matrices), 549 (Meta-leg counterpart), 509 (zero-deal
    counterpoint), 504/489 (dual-payer publishers), nytimes.yaml
    amazon_dependency and affiliate-cut lines.
  - No coverage-tone claim (no NYT post-deal Amazon-vs-Meta tone analysis
    in corpus).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 6 2026):
- https://www.geekwire.com/2025/amazon-inks-deal-with-new-york-times-to-license-newspapers-content-for-ai-platforms/
- https://www.editorandpublisher.com/stories/amazon-to-pay-new-york-times-at-least-20-million-a-year-in-ai-deal,256961
- https://www.pymnts.com/news/artificial-intelligence/2025/amazon-paying-new-york-times-25-million-dollars-ai-licensing/
- https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/
- https://www.techtarget.com/ai/news/366624903/The-New-York-Times-in-multiyear-licensing-deal-with-Amazon
- https://www.spacedaily.com/reports/New_York_Times_signs_AI_licensing_deal_with_Amazon_999.html
- https://www.geekwire.com/2025/report-amazon-to-pay-at-least-20m-a-year-in-ai-content-deal-with-new-york-times/
- https://www.thewrap.com/amazon-pay-20-million-new-york-times/
- http://engadget.com/ai/the-new-york-times-and-amazons-ai-licensing-deal-is-reportedly-worth-up-to-25-million-per-year-135523853.html
- https://www.eweek.com/news/amazon-new-york-times-licensing-deal-ai-training/
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_559_amazon_nyt_ai_licensing_deal'

EXPECTED_URLS = [
    'https://www.geekwire.com/2025/amazon-inks-deal-with-new-york-times-to-license-newspapers-content-for-ai-platforms/',
    'https://www.editorandpublisher.com/stories/amazon-to-pay-new-york-times-at-least-20-million-a-year-in-ai-deal,256961',
    'https://www.pymnts.com/news/artificial-intelligence/2025/amazon-paying-new-york-times-25-million-dollars-ai-licensing/',
    'https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/',
    'https://www.techtarget.com/ai/news/366624903/The-New-York-Times-in-multiyear-licensing-deal-with-Amazon',
    'https://www.spacedaily.com/reports/New_York_Times_signs_AI_licensing_deal_with_Amazon_999.html',
    'https://www.geekwire.com/2025/report-amazon-to-pay-at-least-20m-a-year-in-ai-content-deal-with-new-york-times/',
    'https://www.thewrap.com/amazon-pay-20-million-new-york-times/',
    'http://engadget.com/ai/the-new-york-times-and-amazons-ai-licensing-deal-is-reportedly-worth-up-to-25-million-per-year-135523853.html',
    'https://www.eweek.com/news/amazon-new-york-times-licensing-deal-ai-training/',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_entity():
    return load_entities()['entities']['amazon']


def get_mech():
    return get_entity()[MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('  apple:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_amazon_entity_present(self):
        e = load_entities()['entities']
        assert 'amazon' in e
        assert e['amazon']['display_name'] == 'Amazon'

    def test_mechanism_559_present_under_amazon(self):
        m = get_mech()
        assert m['mechanism_id'] == 559
        assert m['iteration'] == 559

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-06'
        assert m['time_pdt'] == '07:00'

    def test_mechanism_not_under_wrong_entity(self):
        entities = load_entities()['entities']
        for other in ('meta', 'openai', 'google', 'anthropic', 'microsoft', 'perplexity'):
            assert MECH_KEY not in entities[other], other

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'


class TestDealTerms:
    def test_announcement_date_may_29_2025(self):
        assert get_mech()['announcement_date'] == '2025-05-29'

    def test_terms_disclosure_jul_30_2025_wsj_bruell(self):
        m = get_mech()
        assert m['terms_disclosure_date'] == '2025-07-30'
        assert 'Alexandra Bruell' in m['terms_disclosed_by']

    def test_annual_value_20_25m(self):
        value = get_mech()['deal_terms']['annual_value']
        assert '$20-25 million per year' in value
        assert 'WSJ' in value

    def test_nearly_one_percent_of_2024_revenue(self):
        assert 'nearly 1%' in get_mech()['deal_terms']['relative_materiality']

    def test_scope_news_cooking_athletic_alexa_training(self):
        scope = get_mech()['deal_terms']['scope']
        for token in ('NYT Cooking', 'The Athletic', 'Alexa', 'proprietary foundation models'):
            assert token in scope, token

    def test_firsts_both_sides(self):
        firsts = ' '.join(get_mech()['deal_terms']['firsts'])
        assert "Amazon's first AI-related licensing agreement" in firsts
        assert "The New York Times' first AI-related licensing pact" in firsts


class TestSueDealBifurcation:
    def test_lawsuit_dec_2023_openai_microsoft(self):
        suit = get_mech()['sue_deal_bifurcation']['lawsuit']
        assert 'Dec 2023' in suit
        assert 'OpenAI' in suit and 'Microsoft' in suit

    def test_motion_to_dismiss_partially_rejected_apr_2025(self):
        note = get_mech()['sue_deal_bifurcation']['lawsuit_status_note']
        assert 'Apr 2025' in note
        assert 'numerous' in note

    def test_deal_choice_amazon_not_openai(self):
        choice = get_mech()['sue_deal_bifurcation']['deal_choice']
        assert 'Amazon' in choice
        assert 'OpenAI' in choice

    def test_most_prominent_sign_sue_case(self):
        sig = get_mech()['sue_deal_bifurcation']['mechanism_significance']
        assert '468' in sig and '549' in sig


class TestPortfolioSequencing:
    def test_four_deals_sequenced_nyt_first(self):
        seq = get_mech()['amazon_publisher_portfolio_sequencing']
        assert len(seq) == 4
        assert 'FIRST' in seq[0] and 'NYT' in seq[0]
        assert 'Conde Nast' in seq[1] and 'Jul 15 2025' in seq[1]
        assert 'Hearst' in seq[2] and 'Jul 15 2025' in seq[2]
        assert 'Reach plc' in seq[3] and 'Mar 2 2026' in seq[3]


class TestAffiliateSubstitution:
    def test_wirecutter_affiliate_base_estimated(self):
        base = get_mech()['affiliate_to_licensing_substitution']['wirecutter_amazon_affiliate_base']
        assert '$50-100M+' in base

    def test_commission_cuts_2026_adweek(self):
        cuts = get_mech()['affiliate_to_licensing_substitution']['affiliate_commission_cuts_2026']
        assert 'Adweek' in cuts
        assert '$15-50M+/yr' in cuts

    def test_hedge_framing_structural_not_coverage(self):
        dyn = get_mech()['affiliate_to_licensing_substitution']['substitution_dynamic']
        assert 'not a coverage claim' in dyn


class TestDirectionalPredictions:
    def test_five_predictions_present(self):
        preds = get_mech()['directional_predictions']
        assert len(preds) == 5

    def test_amazon_softer_openai_microsoft_adversarial(self):
        joined = ' '.join(get_mech()['directional_predictions'])
        assert 'Amazon: softer' in joined
        assert 'OpenAI: adversarial slot' in joined
        assert 'Microsoft: adversarial slot' in joined

    def test_meta_google_neutral_to_no_deal(self):
        joined = ' '.join(get_mech()['directional_predictions'])
        assert 'Meta: neutral to no-deal' in joined
        assert 'Google: neutral to no-deal' in joined

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_structural_contrasts_include_468_509_549(self):
        joined = ' '.join(get_mech()['structural_contrasts'])
        for token in ('468', '509', '549', '371', '372', '504', '489'):
            assert token in joined, token


class TestConfoundersAndDiscipline:
    def test_five_ranked_confounders(self):
        confs = get_mech()['ranked_confounders']
        assert len(confs) == 5
        assert [c['rank'] for c in confs] == [1, 2, 3, 4, 5]

    def test_confounder_strengths_labeled(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths == ['strong', 'strong', 'moderate', 'moderate', 'weak']

    def test_strongest_is_sourced_value_not_disclosed(self):
        assert 'people familiar with the matter' in get_mech()['ranked_confounders'][0]['confounder']

    def test_statistical_discipline_qualitative_only(self):
        sd = get_mech()['statistical_discipline']
        assert sd['p_value'] == 'NOT_CALCULATED'
        assert sd['is_significant'] is False
        assert sd['tone_scores'] == 'NOT_SCORED'
        assert sd['correlation_not_causation'] is True

    def test_caution_no_tone_claim(self):
        assert get_mech()['no_coverage_tone_claim'] is True
        assert get_mech()['cautious_language_required'] is True


class TestNoveltyAndSourceUrls:
    def test_novelty_first_dedicated_amazon_nyt(self):
        focus = get_mech()['type_c_focus']
        assert 'First dedicated Amazon x NYT mechanism in the corpus' in focus
        assert 'tracked MediaScope publications' in focus

    def test_all_ten_source_urls_present_verbatim(self):
        raw = get_raw_block()
        for url in EXPECTED_URLS:
            assert url in raw, url

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        found = re.findall(r'https?://[^\s\'"]+', raw)
        for url in found:
            assert url in EXPECTED_URLS, url


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII char in block'

    def test_raw_block_boundaries(self):
        raw = get_raw_block()
        assert raw.startswith('    ' + MECH_KEY + ':')
        assert 'mechanism_559' in raw
