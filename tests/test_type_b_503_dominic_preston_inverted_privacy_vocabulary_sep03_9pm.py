"""
Test Mechanism #503 (Type B #503): Dominic Preston (The Verge) inverted
privacy-vocabulary application - Meta vs Google/Samsung discipline check.

Type B: Journalist Cross-Entity Tracking - September 3, 2026, 21:00 PDT
Iteration #503 (rotation 502 A -> 503 B)

KEY FINDING: Dominic Preston, The Verge news editor (Feb 2025-present,
ex-Android Police managing reviews editor), applies privacy-problems
vocabulary to Google/Samsung camera hardware while his Meta AI-launch
coverage and his Google camera-AI launch coverage both run as straight
news-desk relay with zero privacy vocabulary. The privacy language lands
on the deal-adjacent entity, not on Meta - an inversion of the naive
financial-incentive prediction (Vox Media x OpenAI deal #494; The Verge
Google/Samsung ad dependency #81).

VERIFIED CORPUS (this run, via mirrors/excerpts; theverge.com direct fetch
is policy-blocked per standing rule, marked second-hand):

1. Samsung/Google glasses (Jul 22 2026, hands-on): dek verbatim "With a
   camera on every pair, Google's and Samsung's AI glasses face the same
   privacy problems as Meta's." Three-mirror verified (#492):
   - https://technewstube.com/theverge/1852147/samsungs-smart-glasses-actually-look-like/
   Canonical: https://www.theverge.com/tech/969382/samsung-google-smart-glasses-gentle-monster-warby-parker
   (surfaced verbatim in search results; not fetched first-hand)
2. Meta Muse Spark 1.1 (Jul 9 2026, news): "Meta says its new AI model is
   ready to compete on coding." Company-claim relay ("Meta says... a
   'step-change'"), mild deficit frame ("reentering the AI race"), one
   controversy note (Muse Image / Instagram), ZERO privacy vocabulary:
   - https://thetechstreetnow.com/meta-says-its-new-ai-model-is-ready-to-compete-on-coding/
   - https://www.techmeme.com/260709/p20#a260709p20
3. Google Search Live (May 20 2025, news): "Google debuts Search Live"
   (camera field-of-view AI feature). Straight launch news; zero privacy
   framing at headline level (bounded, excerpt-level):
   - https://www.techmeme.com/250520/p43

READING: privacy-vocabulary application looks event/genre-driven (a
camera-hardware hands-on draws the privacy dek) rather than entity-driven.
Joins the falsification family (#457, #471, #472, #492, #493, #498).
Boundary condition on the financial-incentive theory, not a universal rule.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE ONLY; is_significant False;
correlation_not_causation True; p_value NOT_CALCULATED. No empirical
significance claimed.
"""

import os
import re

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')

MECHANISM_KEY = 'verge_dominic_preston_inverted_privacy_vocabulary'
PRIVACY_DEK_FRAGMENT = 'face the same privacy problems as Meta'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_preston_profile():
    for j in load_journalists().get('journalists', []):
        if j.get('name') == 'Dominic Preston':
            return j
    return None


def get_mechanism_503():
    return load_research()['cross_publication_findings'][MECHANISM_KEY]


def get_coverage():
    return get_preston_profile().get('competitor_coverage', {})


def _heading_pos(marker):
    # Line-anchored search (per the #495 durable rule): plain str.index()
    # can match quoted mentions of a heading literal inside newer entries.
    log = open(os.path.join(REPO_ROOT, 'iteration-log.md'), encoding='utf-8').read()
    m = re.search(r'^' + re.escape(marker), log, re.MULTILINE)
    assert m, "heading not found: %s" % marker
    return m.start(), log


# ===================================================================
# Class 1: Preston profile exists with Verge news-editor tenure
# ===================================================================
class TestPrestonProfileExists:
    def test_profile_found(self):
        assert get_preston_profile() is not None, "Dominic Preston entry must exist in journalists.yaml"

    def test_verge_tenure_from_2025_02(self):
        career = get_preston_profile().get('career', [])
        verge = [c for c in career if c.get('publication') == 'the-verge']
        assert len(verge) == 1
        assert verge[0].get('start') == '2025-02'
        assert verge[0].get('role') == 'news_editor'

    def test_android_police_arc(self):
        pubs = {c.get('publication') for c in get_preston_profile().get('career', [])}
        assert 'android-police' in pubs

    def test_source_urls_https(self):
        urls = get_preston_profile().get('source_urls', [])
        assert len(urls) >= 1
        assert all(u.startswith('https://') for u in urls)


# ===================================================================
# Class 2: competitor_coverage block (first Preston Type B)
# ===================================================================
class TestPrestonCompetitorCoverageBlock:
    def test_block_present(self):
        assert 'competitor_coverage' in get_preston_profile(), "Preston needs a competitor_coverage block (first Type B)"

    def test_mechanism_id_503(self):
        analysis = get_coverage().get('cross_entity_analysis', {})
        assert analysis.get('mechanism_id') == 503
        assert analysis.get('iteration') == 503

    def test_pattern_inverted_application(self):
        analysis = get_coverage().get('cross_entity_analysis', {})
        assert analysis.get('pattern') == 'inverted_privacy_vocabulary_application'

    def test_falsification_family(self):
        analysis = get_coverage().get('cross_entity_analysis', {})
        fam = analysis.get('falsification_family', [])
        for expected in (492, 493, 498):
            assert expected in fam

    def test_test_file_points_here(self):
        analysis = get_coverage().get('cross_entity_analysis', {})
        assert analysis.get('test_file', '').endswith(
            'test_type_b_503_dominic_preston_inverted_privacy_vocabulary_sep03_9pm.py')


# ===================================================================
# Class 3: Samsung/Google corpus - privacy vocabulary at dek level
# ===================================================================
class TestPrestonSamsungGoogleCorpus:
    def test_privacy_dek_recorded(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('samsung_google_glasses_hands_on', {})
        assert PRIVACY_DEK_FRAGMENT in item.get('result', '')

    def test_dek_names_google(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('samsung_google_glasses_hands_on', {})
        assert "Google's" in item.get('result', '')

    def test_register_is_privacy_vocab(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('samsung_google_glasses_hands_on', {})
        assert 'privacy' in item.get('register', '').lower()

    def test_journal_yaml_dek_present(self):
        desc = get_coverage().get('cross_entity_analysis', {}).get('description', '')
        assert PRIVACY_DEK_FRAGMENT in desc


# ===================================================================
# Class 4: Meta corpus - straight relay, zero privacy vocabulary
# ===================================================================
class TestPrestonMetaCorpus:
    def test_muse_spark_item_recorded(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('meta_muse_spark_launch', {})
        assert 'Muse Spark 1.1' in item.get('piece', '')

    def test_meta_register_is_relay(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('meta_muse_spark_launch', {})
        assert 'relay' in item.get('register', '').lower()

    def test_meta_zero_privacy_vocabulary(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('meta_muse_spark_launch', {})
        assert 'zero privacy vocabulary' in item.get('result', '').lower()

    def test_meta_piece_date_jul_2026(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('meta_muse_spark_launch', {})
        assert 'Jul 9 2026' in item.get('piece', '')


# ===================================================================
# Class 5: Google Search Live - straight launch news (bounded)
# ===================================================================
class TestPrestonGoogleSearchLive:
    def test_search_live_item_recorded(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('google_search_live_launch', {})
        assert 'Search Live' in item.get('piece', '')

    def test_camera_feature_noted(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('google_search_live_launch', {})
        assert 'camera' in item.get('piece', '').lower()

    def test_bounded_headline_level(self):
        corpus = get_mechanism_503().get('cross_entity_corpus', {})
        item = corpus.get('google_search_live_launch', {})
        assert 'bounded' in item.get('result', '').lower()


# ===================================================================
# Class 6: statistical discipline and confounders
# ===================================================================
class TestMechanism503Discipline:
    def test_not_significant(self):
        assert get_mechanism_503()['statistical_discipline']['is_significant'] is False

    def test_correlation_not_causation(self):
        assert get_mechanism_503()['statistical_discipline']['correlation_not_causation'] is True

    def test_p_value_not_calculated(self):
        assert get_mechanism_503()['statistical_discipline']['p_value'] == 'NOT_CALCULATED'

    def test_manual_illustrative(self):
        assert 'MANUAL ILLUSTRATIVE' in get_mechanism_503()['statistical_discipline']['tone_scores']

    def test_confounders_ranked(self):
        confs = get_mechanism_503().get('confounding_factors', [])
        assert len(confs) >= 4
        strong = [c for c in confs if c.get('level') == 'STRONG']
        assert len(strong) >= 2, "need at least 2 STRONG confounders"

    def test_genre_confound_present(self):
        confs = get_mechanism_503().get('confounding_factors', [])
        text = ' '.join(c.get('factor', '') for c in confs).lower()
        assert 'genre' in text

    def test_dek_authorship_confound_present(self):
        confs = get_mechanism_503().get('confounding_factors', [])
        text = ' '.join(c.get('factor', '') for c in confs).lower()
        assert 'dek' in text

    def test_source_urls_https(self):
        urls = get_mechanism_503().get('source_urls', [])
        assert len(urls) >= 4
        assert all(u.startswith('https://') for u in urls)

    def test_no_em_dashes_in_mechanism(self):
        text = str(get_mechanism_503())
        assert '\u2014' not in text and '\u2013' not in text

    def test_ascii_only_in_mechanism(self):
        text = str(get_mechanism_503())
        assert all(ord(c) < 128 for c in text), "mechanism YAML must stay ASCII-only"


# ===================================================================
# Class 7: iteration log #503 (relative ordering, segment-scoped)
# ===================================================================
class TestIterationLog503:
    def test_log_orders_503_newest_first(self):
        i503, _ = _heading_pos('#503 Type B:')
        i502, _ = _heading_pos('#502 Type A:')
        i501, _ = _heading_pos('#501 Type E:')
        assert i503 < i502 < i501, "iteration log must keep #503 > #502 > #501 newest-first order"

    def test_log_names_preston_in_segment(self):
        i503, log = _heading_pos('#503 Type B:')
        i502, _ = _heading_pos('#502 Type A:')
        seg = log[i503:i502]
        assert 'Dominic Preston' in seg
        assert 'Type B' in seg

    def test_log_has_novelty_block(self):
        i503, log = _heading_pos('#503 Type B:')
        i502, _ = _heading_pos('#502 Type A:')
        seg = log[i503:i502]
        assert 'Novelty Verification' in seg

    def test_log_has_confounders_block(self):
        i503, log = _heading_pos('#503 Type B:')
        i502, _ = _heading_pos('#502 Type A:')
        seg = log[i503:i502]
        assert 'Confounders Ranked' in seg

    def test_novelty_no_prior_preston_type_b_files(self):
        tests_dir = os.path.join(REPO_ROOT, 'tests')
        names = os.listdir(tests_dir)
        preston = [n for n in names if 'preston' in n.lower()]
        assert preston == ['test_type_b_503_dominic_preston_inverted_privacy_vocabulary_sep03_9pm.py'], \
            "only the #503 file may reference preston, got: %s" % preston
