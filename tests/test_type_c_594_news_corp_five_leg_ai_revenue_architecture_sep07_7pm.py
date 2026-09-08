"""Type C #594: News Corp five-leg AI revenue architecture (Sep 2026 status verification) -
OpenAI + Meta + Microsoft/HarperCollins + Anthropic settlement + Bloomberg expanded
Dow Jones AI rights. First dedicated multi-leg aggregation mechanism for News Corp;
first corpus record of the Bloomberg expanded AI-rights deal (announced on the Q2
FY2026 earnings call Feb 5 2026, zero prior corpus mentions grep-verified).

- Iteration #594 Type C Financial Incentive Mapping Sep 7 2026 19:00 PDT
- Rotation 593 B -> 594 C.
- Novelty verified: zero mechanism keys matching news_corp four-leg/triple-payer/quad
  in profiles/competitor-entities.yaml before insertion (grep verified); no dedicated
  News Corp multi-leg aggregation mechanism in iteration-log.md (grep verified); zero
  test_type_c_594 files on disk before this run (glob verified); no #594 in git log
  (grep verified); zero Bloomberg-leg mentions in competitor-entities.yaml and
  iteration-log.md before this run (grep verified). Profile-level notes in
  news-corp.yaml listed four legs but no mechanism block existed.
- Findings (4 browser.search query sets this run, verbatim full-URL listings;
  browser.open first-hand read of the News Corp Q2 FY2026 earnings transcript via
  MarketBeat, Feb 5 2026; Q3 FY2026 Thomson quotes second-hand via search-result
  excerpts, bounded per iteration-492 rule; no pages opened for the Q3 quotes;
  no zero-coverage claims; no canonical URLs constructed):
  - Bloomberg leg (NEW): Thomson on the Q2 FY2026 call: "We are establishing new AI
    partnerships, which we expect to generate additional revenues, including an
    expanded deal with Bloomberg for AI rights for our peerless Dow Jones content."
    First-hand read Sep 7 2026.
    https://www.marketbeat.com/earnings/reports/2026-2-5-news-co-stock-1/
  - Anthropic leg status: Thomson Q2 FY2026 call: "Anthropic has already agreed to
    pay $1.5 billion for using pirated books. We and our authors at HarperCollins
    naturally expect to receive our fair share of that payout starting later this
    calendar year." Sep 6 2026 TechCrunch: publishers including HarperCollins
    asserting claims on author payments, including reverted-rights titles
    (April Henry example), $3,000 per work, 50-50 author/publisher splits.
    https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/
  - Thomson doctrine (Q3 FY2026 call May 7 2026, second-hand excerpts): "We are an
    AI inputs company"; "Semiconductors are inputs. Energy is an input. Editorial
    is an absolutely essential input."; "We are negotiating several further deals
    with companies who recognize the preciousness of our provenance."
    https://www.MarketBeat.com/earnings/reports/2026-5-7-news-co-stock-1/
  - TheWrap Q3 coverage: revenue $2.19B (+9%); "IP powers AI" framing.
    https://www.thewrap.com/industry-news/business/news-corp-q3-earnings/
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED; no coverage-tone claim; no zero-coverage claims per iteration-492.
"""
import pathlib
import re
import subprocess

import yaml

REPO = pathlib.Path(__file__).parent.parent
PROFILES_DIR = REPO / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
NEWS_CORP_PATH = PROFILES_DIR / 'news-corp.yaml'
LOG = REPO / 'iteration-log.md'

MECH_KEY = 'news_corp_five_leg_ai_revenue_architecture_594'

EXPECTED_URLS = [
    'https://www.marketbeat.com/earnings/reports/2026-2-5-news-co-stock-1/',
    'https://www.MarketBeat.com/earnings/reports/2026-5-7-news-co-stock-1/',
    'https://www.thewrap.com/industry-news/business/news-corp-q3-earnings/',
    'https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/',
    'https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244',
    'https://www.eweek.com/news/harpercollins-books-train-microsoft-ai-models/',
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

    def test_mechanism_id_and_iteration_594(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 594
        assert mech['iteration'] == 594

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['rotation'] == 'Type C'
        assert mech['iteration_type'] == 'C'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_type_financial_incentive_mapping(self):
        mech = get_mech()
        assert mech['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_five_legs(self):
        name = get_mech()['mechanism_name']
        assert 'five-leg' in name
        for token in ('OpenAI', 'Meta', 'Microsoft', 'Anthropic', 'Bloomberg'):
            assert token in name, f'missing {token} in mechanism_name'

    def test_no_em_dashes_in_block(self):
        text = open(ENTITIES_PATH, encoding='utf-8').read()
        start = text.index(MECH_KEY)
        block = text[start:start + 12000]
        assert '\u2014' not in block


class TestFiveLegs:
    def test_exactly_five_legs(self):
        legs = get_mech()['legs']
        assert len(legs) == 5
        assert set(legs) == {
            'openai_leg', 'meta_leg', 'microsoft_leg', 'anthropic_leg',
            'bloomberg_leg',
        }

    def test_openai_leg_values(self):
        leg = get_mech()['legs']['openai_leg']
        assert leg['partner'] == 'OpenAI'
        assert leg['value'] == '$250M over 5 years'
        assert leg['mechanism'] == 519

    def test_meta_leg_values(self):
        leg = get_mech()['legs']['meta_leg']
        assert leg['partner'] == 'Meta'
        assert leg['value'] == 'up to $50M/yr, 3-year'
        assert leg['announced'] == '2026-03-04'
        assert leg['mechanism'] == 549

    def test_microsoft_leg_values(self):
        leg = get_mech()['legs']['microsoft_leg']
        assert 'Microsoft' in leg['partner']
        assert leg['value'] == '$5,000 per title, 50/50 author/publisher split, 3-year term'
        assert leg['mechanism'] == 524
        assert 'never officially confirmed' in leg['scope']

    def test_anthropic_leg_is_settlement_channel(self):
        leg = get_mech()['legs']['anthropic_leg']
        assert leg['channel'] == 'settlement_revenue'
        assert leg['approved'] == '2026-07-20'
        assert '$3,000 per work' in leg['value']

    def test_anthropic_leg_thomson_quote(self):
        status = get_mech()['legs']['anthropic_leg']['status']
        assert 'fair share of that payout' in status
        assert 'starting later this calendar year' in status

    def test_anthropic_leg_sep_2026_distribution_friction(self):
        status = get_mech()['legs']['anthropic_leg']['status']
        assert 'Sep 6 2026 TechCrunch' in status
        assert 'HarperCollins' in status
        assert 'reverted-rights' in status
        assert 'April Henry' in status

    def test_bloomberg_leg_is_new(self):
        leg = get_mech()['legs']['bloomberg_leg']
        assert leg['announced'] == '2026-02-05'
        assert leg['announcement_channel'] == 'News Corp Q2 FY2026 earnings call'
        assert leg['value'] == 'undisclosed'
        assert 'Dow Jones' in leg['scope']
        assert 'NEW TO CORPUS' in leg['corpus_status']

    def test_bloomberg_leg_verbatim_quote(self):
        leg = get_mech()['legs']['bloomberg_leg']
        assert 'expanded deal with Bloomberg for AI rights' in leg['verbatim']
        assert 'peerless Dow Jones content' in leg['verbatim']

    def test_bloomberg_leg_first_hand(self):
        leg = get_mech()['legs']['bloomberg_leg']
        assert leg['read_first_hand'] is True
        assert leg['read_date'] == '2026-09-07'

    def test_bloomberg_leg_qualifies_mechanism_85(self):
        note = get_mech()['legs']['bloomberg_leg']['bloomberg_posture_note']
        assert 'mechanism 85' in note
        assert 'BUYER' in note


class TestThomsonDoctrine:
    def test_input_company_quotes(self):
        doc = get_mech()['thomson_doctrine']
        assert 'AI inputs company' in doc['input_company']
        assert 'Semiconductors are inputs' in doc['input_company']
        assert 'Editorial is an absolutely essential input' in doc['input_company']

    def test_pipeline_quote(self):
        assert 'negotiating several further deals' in get_mech()['thomson_doctrine']['pipeline']
        assert 'preciousness of our provenance' in get_mech()['thomson_doctrine']['pipeline']

    def test_woo_and_sue_quote(self):
        assert 'woo and a sue strategy' in get_mech()['thomson_doctrine']['woo_and_sue']

    def test_vertical_ai_quote(self):
        assert 'vertical specialist AI companies' in get_mech()['thomson_doctrine']['vertical_ai']

    def test_factiva_genai(self):
        assert '8,000 premium news' in get_mech()['thomson_doctrine']['factiva_genai']


class TestDirectionalPredictions:
    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_seven_predictions(self):
        preds = get_mech()['directional_predictions']
        assert len(preds) == 7

    def test_meta_leg_neutralizes_adversarial_prediction(self):
        preds = ' '.join(get_mech()['directional_predictions'])
        assert 'NEUTRALIZES any Meta-adversarial prediction' in preds

    def test_google_apple_predictions(self):
        preds = ' '.join(get_mech()['directional_predictions'])
        assert 'Google harder-to-neutral' in preds
        assert 'Apple neutral' in preds

    def test_no_causal_language_in_predictions(self):
        preds = ' '.join(get_mech()['directional_predictions'])
        assert 'proves' not in preds
        assert 'causes' not in preds


class TestConfoundersAndDiscipline:
    def test_six_confounders_ranked(self):
        confs = get_mech()['ranked_confounders']
        assert len(confs) == 6
        assert [c['rank'] for c in confs] == [1, 2, 3, 4, 5, 6]

    def test_strong_confounders_first(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths[:3] == ['strong', 'strong', 'strong']

    def test_bloomberg_undisclosed_is_top_confounder(self):
        top = get_mech()['ranked_confounders'][0]['confounder']
        assert 'undisclosed' in top

    def test_statistical_discipline_not_calculated(self):
        disc = get_mech()['statistical_discipline']
        assert disc['is_significant'] is False
        assert disc['p_value'] == 'NOT_CALCULATED'
        assert disc['cohens_d'] == 'NOT_CALCULATED'
        assert disc['ci_95'] == 'NOT_CALCULATED'
        assert disc['tone_scores'] == 'NOT_SCORED'
        assert disc['scope'] == 'qualitative structural mapping only'

    def test_correlational_note(self):
        note = get_mech()['correlational_note']
        assert 'correlation' in note
        assert 'No causal claim' in note

    def test_cautious_language_and_no_tone_claim(self):
        mech = get_mech()
        assert mech['cautious_language_required'] is True
        assert mech['no_coverage_tone_claim'] is True


class TestCrossReferencesAndProfile:
    def test_novelty_names_distinctions(self):
        nov = get_mech()['novelty']
        for token in ('mechanism 519', '524', '549', '509', '539', '85'):
            assert token in nov, f'missing {token} in novelty'

    def test_novelty_claims_first_aggregation(self):
        assert 'first dedicated News Corp multi-leg aggregation' in get_mech()['novelty']

    def test_news_corp_profile_has_bloomberg_partner(self):
        with open(NEWS_CORP_PATH, encoding='utf-8') as f:
            profile = yaml.safe_load(f)
        rels = profile['revenue_relationships']
        partners = {p['partner'] for p in rels if isinstance(p, dict)}
        assert 'Bloomberg' in partners
        bloom = next(p for p in rels if p.get('partner') == 'Bloomberg')
        assert bloom['type'] == 'ai_licensing'
        assert '594' in bloom['scope']

    def test_profile_note_references_five_channels(self):
        with open(NEWS_CORP_PATH, encoding='utf-8') as f:
            text = f.read()
        assert 'five channels total' in text


class TestNoveltyAndSources:
    def test_sources_list_matches_expected_urls(self):
        srcs = get_mech()['sources']
        assert len(srcs) == len(EXPECTED_URLS)
        for url in EXPECTED_URLS:
            assert url in srcs

    def test_marketbeat_q2_is_first_source(self):
        assert 'marketbeat.com/earnings/reports/2026-2-5' in get_mech()['sources'][0]

    def test_research_method_names_query_sets(self):
        assert '4 browser.search query sets' in get_mech()['research_method']

    def test_research_method_names_first_hand_read(self):
        assert 'browser.open first-hand read' in get_mech()['research_method']

    def test_verification_block(self):
        ver = get_mech()['verification']
        assert ver['iteration'] == 594
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-07 19:00 PDT'
        assert ver['yaml_parse_clean'] is True
        assert ver['ascii_only'] is True

    def test_iteration_log_mentions_594(self):
        text = LOG.read_text(encoding='utf-8')
        assert '#594 Type C' in text
        assert 'News Corp' in text


# ===================================================================
# Rotation-cycle guard. Deselected pre-commit per the #565 followup
# convention; the followup commit patches POST_COMMIT_ANCHOR with the
# main iteration commit hash.
# ===================================================================
class TestRotationCycleGuard594:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO), "log", "-n40",
             TestRotationCycleGuard594.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard594.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#594", "C"),
            ("#593", "B"),
            ("#592", "A"),
            ("#591", "E"),
            ("#590", "D"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # C->B is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: C,B,A,E,D (the rotation
        # runs backward in newest-first order). (order[a] - order[b]) % 5 == 1
        # steps one position backward from the newer commit a to the older
        # commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #\d+:", s)
            assert m, f"subject does not match main-commit pattern: {s!r}"
            observed.append(m.group(1))
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation edge {a}->{b} invalid in {observed}"

    def test_anchor_is_real_commit(self):
        out = subprocess.run(
            ["git", "-C", str(REPO), "cat-file", "-t",
             TestRotationCycleGuard594.ANCHORED_COMMIT],
            capture_output=True, text=True, check=True)
        assert out.stdout.strip() == "commit"
