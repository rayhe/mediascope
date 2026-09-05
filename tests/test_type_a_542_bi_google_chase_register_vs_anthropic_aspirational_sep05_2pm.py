"""Type A #542 (2026-09-05 14:00 PDT): Business Insider x Google chase/deficit
register vs Anthropic aspirational register - completing the BI four-entity
quad.

First dedicated BI x Google mechanism in the corpus (no google entity block
existed under competitor_relationships before this run). Two new BI Google
data points, both via attested secondaries (BI paywalled; no BI-original URLs
returned verbatim in this run's search results):

1. BI scoop: Google employees testing Gemini 3.8 Flash Preview on the
   internal Jetski coding platform (Aug 27 2026; attested by letsdatascience
   Sep 1 2026 citing an "August 27 Business Insider report", biggo, archyde,
   itechpost; corroborated by WSJ Sep 2 2026: "Business Insider previously
   reported that Google employees had been testing 3.8 Flash"). Register:
   insider scoop with chase/deficit company framing - "frantic cadence of the
   current AI race", "mounting pressure on Google to close the gap with
   OpenAI and Anthropic", Gemini 3.5 Pro months behind schedule, "conspicuous
   hole at the top of Google's portfolio". MANUAL ILLUSTRATIVE -0.20.

2. BI on Alphabet's earnings call (early May 2026, Q1 2026 call; attested by
   gadgets360 in two articles): CBO Philipp Schindler says ads are expected
   to "play a key role in growing Gemini" and that a format working in AI
   Mode would transfer to the Gemini app. Monetization/business register,
   growth-framed. MANUAL ILLUSTRATIVE +0.05.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026): Google [-0.20,
+0.05] avg -0.075 vs corpus Anthropic +0.12 (tone_approx, #420) vs corpus
Meta +0.08 (#399): Google harder than both $0-deal peers. Delta
(Google-Anthropic) -0.195; Google-Meta -0.155. p_value NOT_CALCULATED,
is_significant False. n=2 vs n=1 vs n=3. NOT artifact-grade.

Interpretation (falsification family, extends #399/#420): among BI's three
$0-deal entities the register splits by narrative position, not financial
tie. Anthropic (hype-cycle darling) gets valuation exuberance, Meta gets
product-execution neutral-positive, Google (incumbent) gets chase-deficit.
The Axel Springer-OpenAI licensing deal predicts OpenAI softest, but OpenAI
is hardest (-0.42, #399). Beat assignment, hype-cycle position, and product
stage dominate over direct licensing incentive in this window. Correlation
not causation.

Strongest counterargument: the chase register may be entirely news-driven -
Google genuinely trailed on frontier coding models (WSJ independently
documents scrapped 3.5 Pro candidates, the flagship hole, Shazeer/Dean
departures), so deficit framing is accurate reporting; and the Anthropic
aspirational piece was a funding-news peg where exuberance is the genre
default. Accepted as confounder; claim stays bounded, correlation-only,
MANUAL ILLUSTRATIVE.

Evidence hygiene: all URLs carried verbatim from tool output this run; no
businessinsider.com URLs constructed (none returned verbatim). No
zero-coverage claims (iteration-492 rule): the absence of a BI-original
settlement URL is stated as a bounded search-result statement only.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'business-insider.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = 'mechanism_542_bi_google_chase_register_vs_anthropic_aspirational_sep05'


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
    end = text.index('\nkey_journalists:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_google_entity_block_is_new_this_run(self):
        profile = _load_profile()
        entities = list(profile['competitor_relationships'].keys())
        assert 'google' in entities

    def test_mechanism_key_present_under_google(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['google']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 542
        assert m['iteration'] == 542
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-05'

    def test_publication_pair_and_comparators(self):
        m = _mechanism()
        assert m['publication_pair'] == 'BI x Google'
        assert m['competitor'] == 'google'
        assert 'anthropic' in m['comparison_entities']
        assert 'meta' in m['comparison_entities']

    def test_financial_tie_is_zero(self):
        g = _load_profile()['competitor_relationships']['google']
        assert g['financial_tie'] == 'none'
        assert g['estimated_value'] == '$0'

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'

    def test_cross_references_399_and_420(self):
        assert _mechanism()['cross_references'] == [399, 420]


class TestGoogleArticles:
    def test_two_google_articles(self):
        arts = _mechanism()['business_insider_google_articles']
        assert len(arts) == 2

    def test_jetski_scoop_present_with_date(self):
        arts = _mechanism()['business_insider_google_articles']
        scoop = arts[0]
        assert 'Jetski' in scoop['title']
        assert scoop['date'] == '2026-08-27'
        assert scoop['framing'] == 'insider_scoop_chase_deficit'

    def test_jetski_scoop_key_phrases(self):
        phrases = _mechanism()['business_insider_google_articles'][0][
            'key_phrases'
        ]
        joined = ' '.join(phrases)
        assert 'frantic cadence' in joined
        assert 'mounting pressure on Google to close the gap' in joined

    def test_jetski_scoop_tone(self):
        assert _mechanism()['business_insider_google_articles'][0][
            'tone_MANUAL_ILLUSTRATIVE'
        ] == -0.20

    def test_schindler_ads_piece_present(self):
        arts = _mechanism()['business_insider_google_articles']
        ads = arts[1]
        assert 'Schindler' in ads['title']
        assert ads['framing'] == 'monetization_business_register'
        assert ads['tone_MANUAL_ILLUSTRATIVE'] == 0.05

    def test_schindler_key_phrase_verbatim(self):
        phrases = _mechanism()['business_insider_google_articles'][1][
            'key_phrases'
        ]
        assert any('play a key role in growing Gemini' in p for p in phrases)

    def test_no_constructed_bi_urls(self):
        # Intent: no fabricated businessinsider.com URLs. The provenance
        # notes legitimately mention the domain name in prose ("no
        # businessinsider.com URL returned verbatim"), so match only
        # URL-shaped occurrences (scheme + domain), not prose mentions.
        block = _mechanism_block_text()
        assert not re.search(r'https?://[^\s"\']*businessinsider\.com', block)

    def test_attesting_secondaries_verbatim(self):
        secs = _mechanism()['business_insider_google_articles'][0][
            'attesting_secondaries'
        ]
        assert (
            'https://letsdatascience.com/news/'
            'google-reportedly-tests-gemini-38-flash-internally-4de352e8'
            in secs
        )
        assert (
            'https://www.wsj.com/tech/ai/'
            'new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052'
            in secs
        )
        ads_secs = _mechanism()['business_insider_google_articles'][1][
            'attesting_secondaries'
        ]
        assert (
            'https://www.gadgets360.com/ai/news/'
            'google-gemini-ai-ads-in-the-future-philipp-schindler-earnings-call-11434747'
            in ads_secs
        )


class TestCorpusComparators:
    def test_anthropic_comparator_from_420(self):
        comp = _mechanism()['corpus_comparators']['anthropic']
        assert '420' in comp['source']
        assert comp['tone_approx'] == 0.12
        assert comp['framing'] == 'valuation_exuberance'

    def test_meta_comparator_from_399(self):
        comp = _mechanism()['corpus_comparators']['meta']
        assert '399' in comp['source']
        assert comp['tone_avg_MANUAL_ILLUSTRATIVE'] == 0.08

    def test_openai_comparator_from_399(self):
        comp = _mechanism()['corpus_comparators']['openai']
        assert comp['tone_avg_MANUAL_ILLUSTRATIVE'] == -0.42


class TestScorer:
    def test_scorer_arrays(self):
        s = _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']
        assert s['google_scores'] == [-0.20, 0.05]
        assert s['anthropic_scores'] == [0.12]

    def test_scorer_averages(self):
        s = _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']
        assert s['google_avg'] == pytest.approx(-0.075)
        assert s['anthropic_avg'] == pytest.approx(0.12)

    def test_scorer_deltas(self):
        s = _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']
        assert s['delta'] == pytest.approx(-0.195)
        assert s['google_vs_meta_delta'] == pytest.approx(-0.155)

    def test_standing_rule_discipline(self):
        s = _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']
        assert s['p_value'] == 'NOT_CALCULATED'
        assert s['cohens_d'] == 'NOT_CALCULATED'
        assert s['ci'] == 'NOT_CALCULATED'
        assert s['is_significant'] is False

    def test_illustrative_warning_present(self):
        s = _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']
        assert 'MANUAL ILLUSTRATIVE' in s['illustrative_warning']
        assert 'not empirical' in s['illustrative_warning']

    def test_artifact_readiness_below_threshold(self):
        assert 'No analysis.json update warranted' in _mechanism()[
            'artifact_readiness'
        ]


class TestConfoundersAndCounterargument:
    def test_strong_confounders_present(self):
        strong = _mechanism()['confounders_ranked']['strong']
        assert len(strong) >= 3
        joined = ' '.join(strong)
        assert 'secondary attestations' in joined

    def test_strongest_counterargument_news_driven(self):
        ca = _mechanism()['strongest_counterargument']
        assert 'news-driven' in ca
        assert 'Accepted as confounder' in ca

    def test_finding_states_correlation_not_causation(self):
        assert 'Correlation not causation' in _mechanism()['finding']

    def test_finding_names_falsification_family(self):
        assert 'Falsification-family' in _mechanism()['finding']


class TestIterationLog:
    def _headings(self):
        with open(LOG) as f:
            text = f.read()
        return re.findall(r'^#(\d+) Type ([A-E]):', text, re.MULTILINE)

    def test_542_entry_present(self):
        headings = self._headings()
        assert ('542', 'A') in headings

    def test_542_newest_type_entry(self):
        headings = self._headings()
        idx_542 = headings.index(('542', 'A'))
        idx_541 = headings.index(('541', 'E'))
        assert idx_542 < idx_541

    def test_rotation_adjacency_541_e_then_542_a(self):
        headings = self._headings()
        idx_542 = headings.index(('542', 'A'))
        assert headings[idx_542 + 1] == ('541', 'E')

    def test_log_entry_mentions_google_pair(self):
        with open(LOG) as f:
            text = f.read()
        start = text.index('#542 Type A')
        end = text.index('#541 Type E')
        block = text[start:end]
        assert 'BI x Google' in block
        assert '-0.195' in block
