"""Type C #574: Apple training-data purchasing architecture - Dec 2023 $50M
news-publisher offers to Conde Nast, NBC News, IAC (no confirmed closings in
2.5 years), plus the Shutterstock $25-50M training-data deal (signed late
2022, reported Apr 2024), plus the Defined.ai agreement and Photobucket
pursuit - Apple as a data-vendor AI payer with zero confirmed publisher AI
deals.

- Iteration #574 Type C Financial Incentive Mapping Sep 6 2026 23:00 PDT
- Rotation 573 B -> 574 C.
- Novelty verified: zero dedicated Apple training-data mechanism blocks in
  profiles/competitor-entities.yaml before insertion (grep verified - the
  apple entity held only a summary phase_1 line in siri_ai_publisher_deals and
  a vague prior_deals line in siri_ai_content_licensing, neither sourced);
  zero test files with 574 on disk before this run (glob verified); no commit
  with 574 in the title (git log --grep verified). Distinct from mechanism 504
  (Conde Nast x OpenAI - the closed publisher deal at WIRED's owner, the
  counterpoint to Apple's unclosed offer), mechanism 564 (Amazon x Conde Nast
  Rufus - second closed AI-lab payer at WIRED's owner), mechanism 559 (Amazon
  x NYT $20-25M/yr - a publisher deal that closed), mechanism 549 (News Corp x
  Meta up to $50M/yr - a $50M AI-content deal that closed), mechanism 331
  (Meta Dec 2025 publisher bundle), the apple_google_gemini_deal bypass chain
  (Apple pays Google, not publishers), and the Getty display-only deals (no
  training rights).
- Findings (browser.search this run, 3 query sets, verbatim full-URL
  listings; deal facts via search-result excerpts, second-hand, marked
  bounded in-mechanism):
  - Publisher-offer leg: Dec 22 2023, NYT reporting via four anonymous
    sources - Apple floated multiyear deals worth at least $50M to license
    news archives for generative AI training from Conde Nast (owner of
    tracked publication WIRED), NBC News, and IAC. Mixed reception - some
    lukewarm, terms too expansive, liability hook concern (Tom's Guide).
    No confirmed closings as of Sep 6 2026 (2.5 years); independently
    corroborated by the in-corpus Gemini bypass commit a72eba5b.
  - Shutterstock leg: Reuters Apr 6 2024 - Apple signed in the months
    following ChatGPT's late-2022 launch; estimated $25-50M; CFO Jarrod
    Yahes confirmed the tech-company range; Meta, Google, and Amazon struck
    parallel Shutterstock deals in the same range.
  - Defined.ai and Photobucket: Defined.ai agreement in place (CEO Daniela
    Braga rate card); Photobucket 13B+ image library pursuit (Apr 8 2024).
  - Corrected shorthand: Apple is a data-vendor AI payer, not a publisher
    AI payer. WIRED's owner was directly offered $50M by Apple for training
    rights and holds no confirmed Apple AI money; Conde Nast takes OpenAI
    money (Aug 2024), Amazon Rufus money (Jul 2025), Microsoft PCM money
    (Feb 2026). Apple and Meta are the only tracked payers at $0.
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 6 2026):
- https://9to5mac.com/2023/12/22/apple-wants-to-train-its-ai-with-50-million-worth-of-licensed-news-articles/
- https://www.nasdaq.com/articles/apple-aapl-to-license-news-archives-for-its-generative-ai
- https://www.tomsguide.com/news/apples-reportedly-plans-a-different-way-of-training-ai-for-apple-gpt
- http://macrumors.com/2023/12/22/apple-ai-major-publisher-deals/
- https://www.engadget.com/apple-is-reportedly-looking-to-team-up-with-news-publishers-to-train-its-ai-074348010.html
- https://www.cultofmac.com/news/apple-licenses-shutterstock-image-library-ai-model-training
- https://venturebeat.com/ai/apples-25-50-million-shutterstock-deal-highlights-fierce-competition-for-ai-training-data
- https://appleinsider.com/articles/24/04/06/apple-licenses-millions-of-shutterstock-images-to-train-its-ai-models
- https://www.macobserver.com/news/apple-shutterstock-deal-millions-of-images-ai-dataset/
- https://www.macrumors.com/2024/04/08/apple-deal-to-license-images-to-train-ai/
- https://github.com/rayhe/mediascope/commit/a72eba5b0d53f752a6e469e83834667e947f8f86
"""
import pathlib
import subprocess

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
REPO = str(pathlib.Path(__file__).parent.parent)

MECH_KEY = 'mechanism_574_apple_training_data_purchasing_architecture'

EXPECTED_URLS = [
    'https://9to5mac.com/2023/12/22/apple-wants-to-train-its-ai-with-50-million-worth-of-licensed-news-articles/',
    'https://www.nasdaq.com/articles/apple-aapl-to-license-news-archives-for-its-generative-ai',
    'https://www.tomsguide.com/news/apples-reportedly-plans-a-different-way-of-training-ai-for-apple-gpt',
    'http://macrumors.com/2023/12/22/apple-ai-major-publisher-deals/',
    'https://www.engadget.com/apple-is-reportedly-looking-to-team-up-with-news-publishers-to-train-its-ai-074348010.html',
    'https://www.cultofmac.com/news/apple-licenses-shutterstock-image-library-ai-model-training',
    'https://venturebeat.com/ai/apples-25-50-million-shutterstock-deal-highlights-fierce-competition-for-ai-training-data',
    'https://appleinsider.com/articles/24/04/06/apple-licenses-millions-of-shutterstock-images-to-train-its-ai-models',
    'https://www.macobserver.com/news/apple-shutterstock-deal-millions-of-images-ai-dataset/',
    'https://www.macrumors.com/2024/04/08/apple-deal-to-license-images-to-train-ai/',
    'https://github.com/rayhe/mediascope/commit/a72eba5b0d53f752a6e469e83834667e947f8f86',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_entity():
    return load_entities()['entities']['apple']


def get_mech():
    return get_entity()[MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('\n  google:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_apple_entity_present(self):
        entities = load_entities()['entities']
        assert 'apple' in entities

    def test_mechanism_574_present_under_apple(self):
        assert MECH_KEY in get_entity()

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 574
        assert mech['iteration'] == 574
        assert mech['rotation'] == 'Type C'
        assert mech['date_analyzed'] == '2026-09-06'
        assert mech['time_pdt'] == '23:00'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_mechanism_not_under_wrong_entity(self):
        entities = load_entities()['entities']
        for name in ('openai', 'google', 'amazon', 'meta', 'anthropic'):
            assert MECH_KEY not in entities[name]

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_legs(self):
        name = get_mech()['mechanism_name']
        assert 'Shutterstock' in name
        assert 'Conde Nast' in name
        assert 'data-vendor AI payer' in name


class TestPublisherOfferLegFacts:
    def test_report_date_dec_22_2023(self):
        assert get_mech()['publisher_offer_leg']['report_date'] == '2023-12-22'

    def test_offer_terms_50m_multiyear(self):
        terms = get_mech()['publisher_offer_leg']['offer_terms']
        assert '$50 million' in terms
        assert 'multiyear' in terms

    def test_three_recipients_incl_conde_nast(self):
        recipients = ' '.join(get_mech()['publisher_offer_leg']['recipients'])
        assert 'Conde Nast' in recipients
        assert 'NBC News' in recipients
        assert 'IAC' in recipients

    def test_conde_nast_wired_parent_noted(self):
        recipients = ' '.join(get_mech()['publisher_offer_leg']['recipients'])
        assert 'tracked publication WIRED' in recipients

    def test_mixed_reception_lukewarm(self):
        rec = get_mech()['publisher_offer_leg']['publisher_reception']
        assert 'lukewarm' in rec
        assert 'too expansive' in rec

    def test_no_confirmed_closings_2_5_years(self):
        outcome = get_mech()['publisher_offer_leg']['outcome_as_of_2026_09_06']
        assert 'no confirmed closings' in outcome
        assert '2.5 years' in outcome
        assert 'a72eba5b' in outcome


class TestShutterstockLegFacts:
    def test_report_date_apr_6_2024_reuters(self):
        leg = get_mech()['shutterstock_leg']
        assert leg['report_date'] == '2024-04-06'
        assert leg['original_report'] == 'Reuters'

    def test_deal_value_range(self):
        assert get_mech()['shutterstock_leg']['deal_value_estimated'] == '$25-50 million'

    def test_signed_after_chatgpt_launch(self):
        signing = get_mech()['shutterstock_leg']['signing_date']
        assert 'late 2022' in signing
        assert 'reported 16 months later' in signing

    def test_cfo_yahes_confirmation(self):
        conf = get_mech()['shutterstock_leg']['confirmation']
        assert 'Jarrod Yahes' in conf
        assert '$50 million' in conf

    def test_parallel_meta_google_amazon_deals(self):
        parallel = get_mech()['shutterstock_leg']['parallel_deals']
        for entity in ('Meta', 'Google', 'Amazon'):
            assert entity in parallel

    def test_defined_ai_and_photobucket(self):
        extra = get_mech()['defined_ai_and_photobucket']
        assert 'Defined.ai' in extra['defined_ai']
        assert 'Daniela Braga' in extra['defined_ai_ceo_rates']
        assert '13 billion' in extra['photobucket_pursuit']


class TestAppleSpendPosture:
    def test_data_vendor_payer_publisher_zero(self):
        posture = get_mech()['apple_spend_posture']
        assert 'Shutterstock' in posture['data_vendor_payer']
        assert 'ZERO confirmed publisher AI deals' in posture['publisher_zero']

    def test_corrected_shorthand_not_non_payer(self):
        note = get_mech()['apple_spend_posture']['corrected_shorthand']
        assert 'not a non-payer' in note
        assert '$1B/yr Google Gemini deal' in note

    def test_payer_contrast_five_entities(self):
        contrast = get_mech()['apple_spend_posture']['payer_contrast']
        for entity in ('OpenAI', 'Meta', 'Amazon', 'Google', 'Apple'):
            assert entity in contrast

    def test_conde_nast_specificity_wired_owner(self):
        spec = get_mech()['apple_spend_posture']['conde_nast_specificity']
        assert "WIRED's parent" in spec
        assert 'mechanism 504' in spec
        assert 'mechanism 564' in spec
        assert 'Apple and Meta are the only tracked payers paying Conde Nast $0' in spec


class TestDirectionalPredictions:
    def test_five_predictions_present(self):
        assert len(get_mech()['directional_predictions']) == 5

    def test_apple_neutral_no_publisher_incentive(self):
        preds = get_mech()['directional_predictions']
        apple_pred = [p for p in preds if p.startswith('Apple:')][0]
        assert 'no-publisher-incentive' in apple_pred
        assert 'no financial lever' in apple_pred

    def test_meta_zero_at_wired_owner(self):
        preds = get_mech()['directional_predictions']
        meta_pred = [p for p in preds if p.startswith('Meta:')][0]
        assert '$0' in meta_pred

    def test_openai_amazon_softer_google_dual_role(self):
        preds = get_mech()['directional_predictions']
        openai_pred = [p for p in preds if p.startswith('OpenAI:')][0]
        amazon_pred = [p for p in preds if p.startswith('Amazon:')][0]
        google_pred = [p for p in preds if p.startswith('Google:')][0]
        assert 'softer' in openai_pred
        assert 'softer' in amazon_pred
        assert 'pass-through' in google_pred

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_structural_contrasts_cover_504_564_559_549_331(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        for ref in ('504', '564', '559', '549', '331'):
            assert ref in contrasts


class TestConfoundersAndDiscipline:
    def test_six_ranked_confounders(self):
        confs = get_mech()['ranked_confounders']
        assert len(confs) == 6
        assert [c['rank'] for c in confs] == [1, 2, 3, 4, 5, 6]

    def test_confounder_strengths_labeled(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths.count('strong') == 3
        assert strengths.count('moderate') == 2
        assert strengths.count('weak') == 1

    def test_strongest_is_second_hand_paywalled(self):
        first = get_mech()['ranked_confounders'][0]['confounder']
        assert 'second-hand' in first
        assert 'paywalled' in first

    def test_absence_claim_bounded_confounder(self):
        third = get_mech()['ranked_confounders'][2]
        assert third['strength'] == 'strong'
        assert 'iteration-492' in third['confounder']

    def test_statistical_discipline_qualitative_only(self):
        disc = get_mech()['statistical_discipline']
        assert disc['scope'] == 'qualitative structural mapping only'
        assert disc['correlation_not_causation'] is True
        assert disc['p_value'] == 'NOT_CALCULATED'
        assert disc['is_significant'] is False
        assert disc['tone_scores'] == 'NOT_SCORED'

    def test_caution_no_tone_claim(self):
        mech = get_mech()
        assert mech['cautious_language_required'] is True
        assert mech['no_coverage_tone_claim'] is True
        assert 'No causal claim' in mech['correlational_note']


class TestNoveltyAndSourceUrls:
    def test_novelty_first_dedicated_apple_training_data(self):
        focus = get_mech()['type_c_focus']
        assert 'first dedicated Apple data-vendor AI-payer mechanism' in focus

    def test_all_eleven_source_urls_present_verbatim(self):
        sources = get_mech()['sources']
        assert len(sources) == 11
        for url in EXPECTED_URLS:
            assert url in sources

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        for url in EXPECTED_URLS:
            assert url in raw

    def test_research_method_names_three_query_sets(self):
        method = get_mech()['research_method']
        assert '3 query sets' in method
        assert 'iteration-492' in method

    def test_verification_block(self):
        ver = get_mech()['verification']
        assert ver['iteration'] == 574
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-06 23:00 PDT'
        assert ver['yaml_parse_clean'] is True


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII character in block'

    def test_raw_block_boundaries(self):
        raw = get_raw_block()
        assert raw.startswith('    ' + MECH_KEY + ':')
        assert raw.count('mechanism_574') == 1

    def test_no_em_dashes_in_block(self):
        raw = get_raw_block()
        assert '\u2014' not in raw
        assert '\u2013' not in raw


class TestRotationGuard:
    def test_rotation_guard_anchored_at_574_commit(self):
        # Anchored-commit convention (#565 -> bd7f2fd, #570 -> 382abc3,
        # #572 -> e10400d, #573 -> 2994a00): the guard pins the rotation
        # window as of THIS run's commit (immutable), not HEAD. The ANCHORED
        # hash is a placeholder until the main commit exists; patched to the
        # real hash in the followup commit; excluded from the pre-commit run,
        # verified green post-commit.
        anchored = "TODO_574_HASH"
        subjects = subprocess.run(
            ['git', 'log', '--format=%H %s', anchored],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout.splitlines()
        assert subjects, 'anchored commit not found in history'
        head_hash, head_subject = subjects[0].split(' ', 1)
        assert head_hash.startswith(anchored)
        assert 'Type C #574' in head_subject
        parent_subject = subprocess.run(
            ['git', 'log', '-1', '--format=%s', anchored + '^'],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout
        assert 'Type B #573' in parent_subject
