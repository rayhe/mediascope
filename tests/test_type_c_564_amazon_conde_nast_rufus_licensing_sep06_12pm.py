"""
Type C #564: Amazon x Conde Nast AI Content Licensing Deal (Jul 10 2025) -
Multi-Year Rufus Shopping Assistant Agreement, Terms Undisclosed, Second
AI-Lab Payer for WIRED's Owner, First Dedicated Amazon Deal Mechanism for a
Tracked Publication's Parent
- Iteration #564 Type C Financial Incentive Mapping Sep 6 2026 12:00 PDT
- Rotation 563 B -> 564 C.
- Novelty verified: zero dedicated amazon_x_conde_nast / Amazon x Conde Nast
  mechanism blocks in profiles/competitor-entities.yaml before insertion
  (grep verified; the #559 run's own novelty check confirmed zero dedicated
  Conde Nast x Amazon blocks, and only portfolio-list lines plus the
  Hearst-focused amazon_rufus_second_payer sub-block existed); zero test files
  with 564 on disk before this run (glob verified); no commit with 564 in the
  title (git log --grep verified).
  Distinct from mechanism 559 (Amazon x NYT May 2025, FIRST Amazon publisher
  AI deal, $20-25M/yr disclosed - this is the SECOND/THIRD deal, terms
  undisclosed, owner-level not title-level), mechanism 468 (Reach plc x Amazon
  Mar 2026, fourth deal, usage-based), mechanism 504 (Conde Nast x OpenAI Aug
  2024 - the FIRST AI-lab payer of WIRED's owner; this mechanism adds the
  SECOND payer), mechanism 489 plus the amazon_rufus_second_payer sub-block
  (Hearst dual-payer mirror, same-week parallel Rufus deal), mechanism 58
  (Conde Nast AI deal portfolio dependency INDEX - portfolio-level marginal
  revenue quantification, not deal-level Amazon mapping), mechanism 437 (FT
  dual payer companion), and mechanism 549 (News Corp x Meta, the Meta-leg
  counterpart). First Amazon AI licensing mechanism for a tracked
  publication's parent company (WIRED via Conde Nast).
- Findings (browser.search this run, 2 query sets, verbatim full-URL
  listings; deal facts via search-result excerpts, second-hand, marked
  bounded in-mechanism):
  - Deal: multi-year AI content licensing agreements between Amazon and
    Conde Nast (plus parallel Hearst deal) for Amazon's AI shopping assistant
    Rufus, reported Jul 10 2025 by Digiday (Jessica Davies); Digiday's 2025
    AI-deals timeline lists a Jul 15 variant.
  - Terms: fully undisclosed by all parties (Digiday, the-decoder.com,
    Engadget); first Rufus activations expected summer 2025.
  - Scope: Conde Nast content in Rufus; named titles Vogue, GQ, The New
    Yorker (Engadget); Hearst confirmed broad access across newspapers and
    magazines (Good Housekeeping, Cosmopolitan, Harper's Bazaar).
  - Sequencing: six weeks after the NYT x Amazon deal (May 29 2025);
    Engadget notes it is Conde Nast's second major AI deal since the OpenAI
    multi-year partnership (Aug 2024).
  - Analyst: Matt Prohaska (Prohaska Consulting) - "Amazon created the
    commerce media category that everyone else has been trying to copy";
    shopping-content publishers are natural bedfellows for Amazon's LLM
    ambitions.
  - Dual-payer: Conde Nast licensed to OpenAI (Aug 2024, mechanism 504)
    first, Amazon (Jul 2025) second; Perplexity and Microsoft PCM also pay
    per corpus portfolio line; Meta pays $0 to Conde Nast.
  - Magnitude context: mechanism 58 derived an estimated $3-10M/yr
    Amazon/Rufus contribution within $14-45M/yr total AI licensing -
    derived estimate, indicative only, not a disclosure.
  - Directional predictions (predictions, not findings): Amazon softer
    (direct payer, tempered by product-activation scope); OpenAI softer
    (first payer, deeper display deal); Meta neutral to no-deal; Anthropic
    zero-deal slot; Google neutral to no-deal.
  - Structural contrasts: 559 (first, disclosed), 468 (fourth,
    usage-based), 504 (first payer), 489 + amazon_rufus_second_payer
    (Hearst mirror), 58 (portfolio index), 437 (FT dual payer), 549
    (Meta-leg counterpart).
  - No coverage-tone claim (no WIRED post-deal Amazon-tone analysis in
    corpus).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 6 2026):
- https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/
- https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/
- https://www.engadget.com/big-tech/amazon-strikes-ai-licensing-deal-with-hearst-and-conde-nast-134849930.html
- https://www.glossy.co/fashion/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/
- https://www.editorandpublisher.com/stories/cond-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus,256658
- https://the-decoder.com/amazon-signs-multi-year-deals-with-conde-nast-and-hearst-to-add-editorial-content-to-its-rufus-ai/
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_564_amazon_conde_nast_rufus_ai_licensing_deal'

EXPECTED_URLS = [
    'https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/',
    'https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/',
    'https://www.engadget.com/big-tech/amazon-strikes-ai-licensing-deal-with-hearst-and-conde-nast-134849930.html',
    'https://www.glossy.co/fashion/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/',
    'https://www.editorandpublisher.com/stories/cond-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus,256658',
    'https://the-decoder.com/amazon-signs-multi-year-deals-with-conde-nast-and-hearst-to-add-editorial-content-to-its-rufus-ai/',
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
        d = load_entities()
        assert 'amazon' in d['entities']

    def test_mechanism_564_present_under_amazon(self):
        assert MECH_KEY in get_entity()

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['mechanism_id'] == 564
        assert m['iteration'] == 564
        assert m['rotation'] == 'Type C'
        assert m['date_analyzed'] == '2026-09-06'
        assert m['time_pdt'] == '12:00'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'

    def test_mechanism_not_under_wrong_entity(self):
        d = load_entities()['entities']
        for other in ('openai', 'google', 'meta', 'anthropic', 'microsoft'):
            assert MECH_KEY not in d[other], other

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'


class TestDealFacts:
    def test_announcement_date_jul_10_2025(self):
        assert get_mech()['announcement_date'] == '2025-07-10'

    def test_date_variant_jul_15_noted(self):
        assert '2025-07-15' in get_mech()['announcement_date_variant']

    def test_multi_year_structure(self):
        assert 'multi-year' in get_mech()['deal_terms']['structure']

    def test_terms_fully_undisclosed(self):
        assert 'undisclosed' in get_mech()['deal_terms']['payment']

    def test_scope_names_vogue_gq_new_yorker(self):
        scope = get_mech()['deal_terms']['scope']
        assert 'Vogue' in scope and 'GQ' in scope and 'New Yorker' in scope

    def test_rufus_product_described(self):
        assert 'shopping assistant' in get_mech()['deal_terms']['product']

    def test_activation_summer_2025(self):
        assert 'summer 2025' in get_mech()['deal_terms']['activation']

    def test_digiday_reporter_channel(self):
        assert 'Jessica Davies' in get_mech()['announcement_channel']


class TestDualPayerSignificance:
    def test_openai_first_payer_aug_2024(self):
        assert 'Aug 20 2024' in get_mech()['dual_payer_publisher_significance']['first_payer']

    def test_amazon_second_payer(self):
        assert 'Jul 2025' in get_mech()['dual_payer_publisher_significance']['second_payer']

    def test_owner_level_tie_to_wired(self):
        assert 'WIRED' in get_mech()['dual_payer_publisher_significance']['owner_level_tie']

    def test_parallel_hearst_same_week(self):
        assert 'same week' in get_mech()['dual_payer_publisher_significance']['parallel_hearst']

    def test_ft_companion_437(self):
        assert '437' in get_mech()['dual_payer_publisher_significance']['ft_companion']

    def test_meta_zero_to_conde_nast(self):
        assert '$0' in get_mech()['dual_payer_publisher_significance']['meta_zero']


class TestPortfolioSequencing:
    def test_four_deals_sequenced(self):
        seq = get_mech()['amazon_publisher_portfolio_sequencing']
        assert len(seq) == 4

    def test_nyt_first_conde_nast_second_reach_fourth(self):
        seq = ' | '.join(get_mech()['amazon_publisher_portfolio_sequencing'])
        assert 'FIRST' in seq and 'SECOND' in seq and 'FOURTH' in seq
        assert 'NYT' in seq and 'Conde Nast' in seq and 'Reach plc' in seq

    def test_sequencing_note_flat_to_usage_arc(self):
        assert 'usage-based' in get_mech()['sequencing_note']


class TestEstimatedMagnitude:
    def test_mechanism_58_estimate_cited(self):
        assert '$3-10M/yr' in get_mech()['estimated_magnitude_context']['mechanism_58_estimate']

    def test_estimate_status_derived_not_disclosure(self):
        assert 'not a disclosure' in get_mech()['estimated_magnitude_context']['estimate_status']

    def test_materiality_note_strategic_over_revenue(self):
        assert 'strategic significance' in get_mech()['estimated_magnitude_context']['materiality_note']


class TestDirectionalPredictions:
    def test_five_predictions_present(self):
        assert len(get_mech()['directional_predictions']) == 5

    def test_amazon_softer_tempered_by_scope(self):
        joined = ' | '.join(get_mech()['directional_predictions'])
        assert 'Amazon: softer' in joined

    def test_openai_softer_meta_neutral_anthropic_zero(self):
        joined = ' | '.join(get_mech()['directional_predictions'])
        assert 'OpenAI: softer' in joined
        assert 'Meta: neutral to no-deal' in joined
        assert 'Anthropic: zero-deal slot' in joined

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_structural_contrasts_include_559_468_504_58(self):
        joined = ' | '.join(get_mech()['structural_contrasts'])
        for ref in ('559', '468', '504', '58'):
            assert ref in joined, ref


class TestConfoundersAndDiscipline:
    def test_five_ranked_confounders(self):
        assert len(get_mech()['ranked_confounders']) == 5

    def test_confounder_strengths_labeled(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths.count('strong') == 2
        assert strengths.count('moderate') == 2
        assert strengths.count('weak') == 1

    def test_strongest_is_terms_undisclosed(self):
        top = get_mech()['ranked_confounders'][0]['confounder']
        assert 'undisclosed' in top

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
    def test_novelty_first_dedicated_amazon_conde_nast(self):
        focus = get_mech()['type_c_focus']
        assert 'First dedicated Amazon x Conde Nast mechanism in the corpus' in focus

    def test_all_six_source_urls_present_verbatim(self):
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
        assert 'mechanism_564' in raw
