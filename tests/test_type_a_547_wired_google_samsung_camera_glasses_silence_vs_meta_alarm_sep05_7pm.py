"""Type A #547 (2026-09-05 19:00 PDT): WIRED x Google/Samsung camera glasses
45-day coverage silence + enthusiastic I/O demo register vs WIRED x Meta
glasses alarm baseline.

First scored WIRED x Google mechanism in the corpus (no target_entity google
asymmetry scorer run existed in wired.yaml before this run). Two
WIRED-Google/Samsung data points vs the WIRED Meta glasses alarm baseline:

1. Google I/O 2026 (May 19, 2026): five WIRED reporters live-blogged Google's
   camera-equipped Gemini smart glasses with enthusiastic/playful register
   ("actually bananas", zero privacy vocabulary, mechanism #3740). Same
   Chokkattu who framed Meta's glasses as a tool for mass surveillance.
   Proxy-only per mechanism #430 (no direct wired.com URL surfaced this run),
   so second-hand attested. MANUAL ILLUSTRATIVE +0.15.

2. Samsung "intelligent eyewear" (Galaxy Unpacked, Jul 22, 2026): same
   Snapdragon AR1 Gen 1 chip as Meta's glasses; camera with LED indicator and
   a visible physical camera-kill switch on the stage unit; single right-side
   camera (not for 3D face mapping or face recognition); Warby Parker and
   Gentle Monster frames; fall 2026 launch. WIRED standalone coverage
   Jul 22-Sep 5, 2026 (45 days): zero articles surfaced - extends the 38-day
   silence through Aug 28 (mechanism #374/#5722), stated as a bounded
   search-result absence per the iteration-492 rule, not a proven zero.

Comparator baseline (WIRED x Meta glasses, direct wired.com URLs, corpus
tones): "Meta Is Warned That Facial Recognition Glasses Will Arm Sexual
Predators" (Apr 13, 2026, Cameron, -0.82, hypothetical feature, no actual
harm); "The Rise of the Ray-Ban Meta Creep" (Mar 23, 2026, -0.72);
"Meta Silently Added Face-Recognition Code NameTag" (Jun 4, 2026,
Cameron/Mehrotra, -0.78). Array avg -0.773.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Google [+0.15] avg 0.15 vs Meta [-0.82, -0.72, -0.78] avg -0.773. Delta
(Google minus Meta) +0.923. p_value NOT_CALCULATED, is_significant False.
NOT artifact-grade: n=1 scored Google item, proxy-flagged I/O claims,
bounded silence claim, heavy confounders.

Interpretation (falsification family, extends #3740/#430/#374/#5722): the
google entity block's "adversarial" coverage prediction FAILS for this product
lane. Conde Nast gets $0 AI licensing from Google (the only AI company CN has
no deal with), Advance sued Google (Jan 14, 2026 SDNY), and Lynch called
Google AI Overviews a revenue "death blow" - yet WIRED covered Google's camera
glasses with delight and has published nothing standalone on Samsung's
physical camera-kill switch. The soft register cannot be bought loyalty.

Strongest counterargument: the split is plausibly all news-driven. Meta is the
only shipped camera-glasses product at scale with documented bad facts
(LED-tamperers prompting Meta to brick thousands of glasses; hidden NameTag
face-recognition code in millions of phones), giving WIRED's watchdog
reporters real stories in the alarm register. Google's glasses were a stage
demo and Samsung's are pre-launch, so enthusiastic demo coverage and sparse
pre-launch coverage are genre defaults, not company favoritism. Accepted as a
major confounder; claim stays bounded, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: all URLs carried verbatim from tool output this run; no
wired.com URLs constructed for the Google I/O or Samsung items (none returned
verbatim). The 45-day Samsung silence is stated as a bounded search-result
statement only (iteration-492 rule). No em dashes in any new prose.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'wired.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = 'mechanism_547_wired_google_samsung_camera_glasses_silence_vs_meta_alarm_sep05'


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['google'][MECH_KEY]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index('\n  microsoft:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_google(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['google']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 547
        assert m['iteration'] == 547
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-05'

    def test_publication_pair_and_comparators(self):
        m = _mechanism()
        assert m['publication_pair'] == 'WIRED x Google'
        assert m['competitor'] == 'google'
        assert 'meta' in m['comparison_entities']
        assert 'samsung' in m['comparison_entities']

    def test_google_entity_block_predates_mechanism(self):
        g = _load_profile()['competitor_relationships']['google']
        assert g['financial_tie'] == 'adversarial_litigation'
        assert g['estimated_value'] == '$0 (seeking unspecified damages)'

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'

    def test_prediction_failure_documented(self):
        assert 'FAILS' in _mechanism()['finding']

    def test_no_em_dashes_in_block(self):
        assert '\u2014' not in _mechanism_block_text()


class TestGoogleArticles:
    def test_io_item_proxy_flagged(self):
        arts = _mechanism()['articles']
        io = [a for a in arts if 'I/O 2026' in a['title']][0]
        assert io['url'] is None
        assert io['evidence_grade'] == 'secondary_attested'
        assert io['manual_illustrative_tone'] == 0.15

    def test_samsung_memeburn_url_verbatim(self):
        arts = _mechanism()['articles']
        urls = [a.get('url') for a in arts]
        assert 'https://memeburn.com/samsung-smart-glasses-2026/' in urls

    def test_samsung_mobilesyrup_url_verbatim(self):
        arts = _mechanism()['articles']
        urls = [a.get('url') for a in arts]
        assert 'http://mobilesyrup.com/2026/07/22/samsung-google-tease-smartglasses-fall-launch/' in urls

    def test_samsung_newsroom_url_verbatim(self):
        arts = _mechanism()['articles']
        urls = [a.get('url') for a in arts]
        assert 'https://news.samsung.com/us/samsung-interview-galaxy-unpacked-july-2026-inside-engineering-intelligent-eyewear' in urls

    def test_camera_kill_switch_documented(self):
        assert 'camera-kill switch' in _mechanism()['finding']

    def test_silence_window_bounded(self):
        f = _mechanism()['finding']
        assert '45 days' in f
        assert 'iteration-492 rule' in f
        assert 'not a proven zero' in f

    def test_bricking_news_peg(self):
        arts = _mechanism()['articles']
        urls = [a.get('url') for a in arts]
        assert 'https://petapixel.com/2026/09/01/meta-claims-to-have-bricked-thousands-of-smart-glasses/' in urls


class TestCorpusComparators:
    def test_three_meta_comparator_articles(self):
        arts = _mechanism()['articles']
        meta = [a for a in arts if a.get('framing', '').startswith('alarm_')]
        assert len(meta) == 3

    def test_meta_tones_match_corpus(self):
        arts = _mechanism()['articles']
        meta = [a for a in arts if a.get('framing', '').startswith('alarm_')]
        tones = {a['title']: a['tone_approx'] for a in meta}
        assert any('-0.82' in str(v) for v in tones.values())
        assert any('-0.72' in str(v) for v in tones.values())
        assert any('-0.78' in str(v) for v in tones.values())

    def test_meta_urls_direct_wired(self):
        arts = _mechanism()['articles']
        meta = [a for a in arts if a.get('framing', '').startswith('alarm_')]
        for a in meta:
            assert a['url'].startswith('https://www.wired.com/story/')

    def test_predator_piece_hypothetical(self):
        arts = _mechanism()['articles']
        pred = [a for a in arts if 'Sexual Predators' in a['title']][0]
        assert 'hypothetical' in pred['actual_harm']


class TestScorer:
    def test_arrays(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['target_entity'] == 'google'
        assert r['target_tones_manual_illustrative'] == [0.15]
        assert r['reference_tones_manual_illustrative'] == [-0.82, -0.72, -0.78]

    def test_arithmetic(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert abs(r['target_avg'] - 0.15) < 1e-9
        assert abs(r['reference_avg'] - (-0.773)) < 0.001
        assert abs(r['delta_google_minus_meta'] - 0.923) < 0.001

    def test_manual_illustrative_guards(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['p_value'] == 'NOT_CALCULATED'
        assert r['cohens_d'] == 'NOT_CALCULATED'
        assert r['ci'] == 'NOT_CALCULATED'
        assert r['is_significant'] is False
        assert r['artifact_grade'] is False

    def test_limitations_stated(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert 'n=1' in r['limitations']


class TestConfoundersAndCounterargument:
    def test_confounders_present(self):
        confs = _mechanism()['confounders']
        assert len(confs) >= 5
        blob = ' '.join(c if isinstance(c, str) else str(c.get('text', c)) for c in confs)
        assert '70 percent' in blob
        assert 'Cameron' in blob

    def test_strongest_counterargument_news_driven(self):
        ca = _mechanism()['strongest_counterargument']
        assert 'news-driven' in ca
        assert 'MANUAL ILLUSTRATIVE' in ca
        assert 'correlation-only' in ca

    def test_financial_context_zero_google(self):
        fc = _mechanism()['financial_context']
        assert '$0 AI licensing from Google' in fc
        assert 'SUED Google' in fc

    def test_novelty_extends_prior(self):
        nov = _mechanism()['novelty']
        for prior in ['#3740', '#430', '#374']:
            assert prior in nov


class TestIterationLog:
    def test_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#547' in text
        assert 'Type A' in text

    def test_log_entry_relative_order(self):
        with open(LOG) as f:
            text = f.read()
        m546 = re.search(r'^#546\b', text, re.MULTILINE)
        m547 = re.search(r'^#547\b', text, re.MULTILINE)
        assert m547 is not None and m546 is not None
        assert m547.start() < m546.start()

    def test_log_entry_content(self):
        with open(LOG) as f:
            text = f.read()
        start = text.index('#547 Type A')
        end = text.index('#546 Type E')
        block = text[start:end]
        assert 'WIRED x Google' in block
        assert '+0.923' in block
        assert 'NOT artifact-grade' in block
