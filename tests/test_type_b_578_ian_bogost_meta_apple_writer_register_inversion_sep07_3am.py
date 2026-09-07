"""
Test Type B #578: Ian Bogost (Atlantic) Meta vs Apple Writer-Register Inversion

Type B: Journalist Cross-Entity Tracking - September 7, 2026 (03:00 PDT)

KEY FINDING: WRITER-LEVEL FALSIFICATION (bound) of the publication-level
deal-incentive prediction, not causal evidence. Ian Bogost is affirmative
toward Meta's AI training-data use (Sep 27 2023 "My Books Were Used to Train
Meta's Generative AI. Good." - subhead "It can have my next one too") while
adversarial toward Apple across seven years (Feb 2017 "The Myth of Apple's
Great Design"; Feb 3 2024 "The Apple Vision Pro Is Spectacular and Sad").
Direction is OPPOSITE the Atlantic-Apple softer prediction: the same writer
treats the no-deal entity (Meta) warmly and the deal-tied entity (Apple)
coldly. This BOUNDS mechanism #572 (Type A, same publication, Apple vs Meta),
which found publication-level register selection directionally consistent with
softer Apple. The coexistence is the finding: publication-level financial
incentives and writer-level philosophical registers are SEPARABLE mechanisms
pulling in opposite directions at the same outlet.

Meta corpus (1 item, affirmative copyright-philosophy essay):
- Sep 27 2023 "My Books Were Used to Train Meta's Generative AI. Good."
  (solo Bogost): contrasts his permissive stance with outraged authors calling
  Books3 a "smoking gun" for mega-corporate misbehavior.

Apple corpus (2 items, adversarial design criticism):
- Feb 3 2024 "The Apple Vision Pro Is Spectacular and Sad" (solo Bogost):
  melancholy first-person review, "A dispatch from the gypsum dunes of
  cyberspace".
- Feb 2017 "The Myth of Apple's Great Design" (solo Bogost): "Apple has great
  design is the biggest myth in technology today"; "In truth, Apple's products
  hide a shambles of bad design under the perfection of sleek exteriors."

CONFOUNDERS (5): STRONG genre asymmetry (copyright-philosophy essay vs
product/design criticism - the standing Type B boundary condition); STRONG
personal stake and ideology (Bogost's own books are in Books3; open-source/
copyright-permissive philosophy and design skepticism predate all three
pieces); MODERATE timing mismatch (2017 vs 2023 vs 2024); MODERATE thin Meta
corpus (n=1); WEAK headline authorship (Atlantic headlines frequently
editor-written).

COUNTEREVIDENCE (4): same-discourse opposite treatment (#16 Reisner foregrounded
Meta adversarially in the same Books3 discourse where Bogost wrote "Good.");
#572 publication-level opposite direction (unit of analysis changes the
verdict); the Meta piece is not Meta-the-company coverage (copyright-philosophy
essay, Meta as named practitioner); Bogost's Apple criticism is design-
philosophy not conduct scrutiny (zero accountability-register investigation of
Apple, consistent with #572's register-selection claim).

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level, n=1 vs
n=2, -1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical
significance test on hand-scored items would manufacture precision that does
not exist. is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-07):
- https://www.theatlantic.com/technology/archive/2023/09/books3-database-meta-training-ai/675461/
- https://ouci.dntb.gov.ua/en/works/4rggbqBL/ (academic bibliography confirming citation)
- http://bogost.com/author/ibogost/ (author archive confirming piece and lede)
- https://insights.hansdezwart.nl/author/ian-bogost (bibliography: "27 sep. 2023 - It can have my next one too")
- https://www.theatlantic.com/technology/archive/2024/02/apple-vision-pro-headset-review/677347/
- https://github.com/chanchann/awesome-vision-pro (verbatim URL listing)
- https://www.frontporchrepublic.com/2024/02/farming-workshops-music-and-apple-vision/ (authorship: "Ian Bogost has some concerns")
- https://redef.com/author/52a90d5b7106a204130000ce (Ian Bogost archive)
- https://www.theatlantic.com/technology/archive/2017/02/themythofapplesgreatdesign/516093/
- https://kottke.org/17/02/the-myth-of-apples-great-design (authorship + verbatim quotes)
- https://www.loopinsight.com/2017/02/10/the-myth-of-apples-great-design/ (date Feb 10 2017)
- https://digiday.com/media/media-briefing-publishers-see-apple-news-as-a-stable-revenue-stream-amid-volatile-referral-traffic/ (Apple News+ tie)
"""

import os

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

BLOCK_KEY = 'type_b_578_ian_bogost_meta_apple_writer_register_inversion'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_bogost_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Ian Bogost':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


def get_scorer(block=None):
    block = block if block is not None else get_bogost_block()
    return block.get('asymmetry_scorer_result_illustrative', {})


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 1+2 within-writer corpus."""

    def test_block_exists(self):
        assert get_bogost_block(), \
            f"{BLOCK_KEY} must exist on Ian Bogost"

    def test_iteration_and_date(self):
        block = get_bogost_block()
        assert block.get('iteration') == 578, \
            f"iteration must be 578, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-07', \
            f"date must be 2026-09-07, got {block.get('date')}"

    def test_design_is_within_journalist(self):
        design = get_bogost_block().get('design', '').lower()
        assert 'within-journalist' in design and 'atlantic' in design, \
            f"design must be within-journalist at the Atlantic, got: {design}"

    def test_meta_corpus_count(self):
        corpus = get_bogost_block().get('meta_corpus', [])
        assert len(corpus) == 1, \
            f"Meta corpus must have exactly 1 item, got {len(corpus)}"

    def test_apple_corpus_count(self):
        corpus = get_bogost_block().get('apple_corpus', [])
        assert len(corpus) == 2, \
            f"Apple corpus must have exactly 2 items, got {len(corpus)}"

    def test_every_item_has_source_url_and_verification(self):
        block = get_bogost_block()
        for item in block['meta_corpus'] + block['apple_corpus']:
            assert isinstance(item, dict), \
                f"corpus item must be a dict, got {type(item)}: {item}"
            assert item.get('url', '').startswith('http'), \
                f"Every corpus item needs a source URL, missing on: {item.get('title')}"
            assert item.get('verification'), \
                f"Every corpus item needs a verification note: {item.get('title')}"
            assert 'bogost' in item.get('byline', '').lower(), \
                f"Every corpus item must carry a Bogost byline: {item.get('title')}"

    def test_meta_flagship_is_books3_good_piece(self):
        corpus = get_bogost_block()['meta_corpus']
        piece = corpus[0]
        assert 'my books were used to train' in piece.get('title', '').lower(), \
            "Meta corpus must be the Books3 'Good.' piece"
        assert piece.get('date') == '2023-09-27', \
            f"Meta piece date must be 2023-09-27, got {piece.get('date')}"
        assert piece.get('url') == \
            'https://www.theatlantic.com/technology/archive/2023/09/books3-database-meta-training-ai/675461/', \
            "Meta piece must carry the exact canonical Atlantic URL"
        assert 'good' in piece.get('register', '').lower() or \
            'affirmative' in piece.get('register', '').lower(), \
            "Meta piece register must be affirmative"
        assert 'next one too' in piece.get('verbatim_markers', '').lower(), \
            "Meta piece must carry the 'It can have my next one too' marker"

    def test_apple_vision_pro_piece(self):
        corpus = get_bogost_block()['apple_corpus']
        piece = next(i for i in corpus if 'spectacular and sad' in i['title'].lower())
        assert piece.get('date') == '2024-02-03', \
            f"Vision Pro piece date must be 2024-02-03, got {piece.get('date')}"
        assert piece.get('url') == \
            'https://www.theatlantic.com/technology/archive/2024/02/apple-vision-pro-headset-review/677347/', \
            "Vision Pro piece must carry the exact canonical Atlantic URL"
        assert 'melancholy' in piece.get('register', '').lower(), \
            "Vision Pro piece register must be melancholy review"

    def test_apple_myth_piece(self):
        corpus = get_bogost_block()['apple_corpus']
        piece = next(i for i in corpus if 'myth' in i['title'].lower())
        assert piece.get('date') == '2017-02', \
            f"Myth piece date must be 2017-02, got {piece.get('date')}"
        assert piece.get('url') == \
            'https://www.theatlantic.com/technology/archive/2017/02/themythofapplesgreatdesign/516093/', \
            "Myth piece must carry the exact canonical Atlantic URL"
        assert 'biggest myth in technology today' in piece.get('verbatim_markers', '').lower(), \
            "Myth piece must carry the 'biggest myth' verbatim marker"


# ===================================================================
# Test Class 2: Register-Inversion Finding
# ===================================================================
class TestRegisterInversionFinding:
    """The finding must assert the writer-level inversion with bounds."""

    def test_finding_names_meta_warmth_marker(self):
        finding = get_bogost_block().get('finding', '').lower()
        assert 'good' in finding, \
            "Finding must cite the Meta-side affirmative marker ('Good.')"

    def test_finding_names_apple_adversarial_markers(self):
        finding = get_bogost_block().get('finding', '').lower()
        assert 'myth' in finding, \
            "Finding must cite the Apple-side adversarial marker (Myth piece)"
        assert 'spectacular and sad' in finding, \
            "Finding must cite the Apple Vision Pro piece"

    def test_finding_asserts_falsification_bound(self):
        finding = get_bogost_block().get('finding', '').lower()
        assert 'falsification' in finding, \
            "Finding must state writer-level falsification (bound)"
        assert 'opposite' in finding, \
            "Finding must state the observed direction is opposite the prediction"

    def test_finding_cross_references_572(self):
        finding = get_bogost_block().get('finding', '')
        assert '#572' in finding or 'mechanism 572' in finding.lower(), \
            "Finding must cross-reference mechanism #572 (the publication-level unit)"

    def test_finding_asserts_separable_mechanisms(self):
        finding = get_bogost_block().get('finding', '').lower()
        assert 'separable' in finding, \
            "Finding must state publication and writer mechanisms are separable"

    def test_finding_denies_causal_claim(self):
        finding = get_bogost_block().get('finding', '')
        assert 'CORRELATION NOT CAUSATION' in finding, \
            "Finding must explicitly deny a causal claim"


# ===================================================================
# Test Class 3: Confounders
# ===================================================================
class TestConfounders:
    """Five ranked confounders must be recorded."""

    def test_confounder_count(self):
        confounders = get_bogost_block().get('confounders', [])
        assert len(confounders) == 5, \
            f"Must record exactly 5 confounders, got {len(confounders)}"

    def test_genre_confounder_is_strong(self):
        confounders = get_bogost_block()['confounders']
        genre = next(c for c in confounders if 'genre' in c.lower())
        assert genre.startswith('[STRONG]'), \
            "Genre asymmetry must be rated STRONG"
        assert '493' in genre or '508' in genre, \
            "Genre confounder must cross-reference the boundary-condition family"

    def test_personal_stake_confounder_is_strong(self):
        confounders = get_bogost_block()['confounders']
        stake = next(c for c in confounders if 'personal stake' in c.lower() or 'ideolog' in c.lower())
        assert stake.startswith('[STRONG]'), \
            "Personal stake / ideology must be rated STRONG"
        assert 'books3' in stake.lower(), \
            "Must name Books3 as the personal-stake vector"

    def test_timing_confounder_present(self):
        confounders = get_bogost_block()['confounders']
        assert any('timing' in c.lower() for c in confounders), \
            "Must include the timing-mismatch confounder (2017 vs 2023 vs 2024)"

    def test_thin_meta_corpus_confounder_present(self):
        confounders = get_bogost_block()['confounders']
        thin = next(c for c in confounders if 'n=1' in c.lower())
        assert 'moderate' in thin.lower(), \
            "Thin Meta corpus (n=1) must be rated MODERATE"

    def test_headline_authorship_confounder_is_weak(self):
        confounders = get_bogost_block()['confounders']
        headline = next(c for c in confounders if 'headline' in c.lower())
        assert headline.startswith('[WEAK]'), \
            "Headline authorship must be rated WEAK"


# ===================================================================
# Test Class 4: Counterevidence
# ===================================================================
class TestCounterevidence:
    """Four counterevidence items must be recorded."""

    def test_counterevidence_count(self):
        ce = get_bogost_block().get('counterevidence', [])
        assert len(ce) == 4, \
            f"Must record exactly 4 counterevidence items, got {len(ce)}"

    def test_reisner_same_discourse_present(self):
        ce = get_bogost_block()['counterevidence']
        assert any('#16' in c or 'reisner' in c.lower() for c in ce), \
            "Must include the Reisner #16 same-Books3-discourse counterevidence"

    def test_572_opposite_direction_present(self):
        ce = get_bogost_block()['counterevidence']
        assert any('#572' in c for c in ce), \
            "Must include the #572 opposite-direction counterevidence"

    def test_not_company_coverage_present(self):
        ce = get_bogost_block()['counterevidence']
        assert any('not meta-the-company' in c.lower() or 'copyright-philosophy' in c.lower() for c in ce), \
            "Must include the not-Meta-the-company counterevidence"

    def test_design_not_conduct_present(self):
        ce = get_bogost_block()['counterevidence']
        assert any('design-philosophy' in c.lower() or 'conduct scrutiny' in c.lower() for c in ce), \
            "Must include the design-philosophy-not-conduct counterevidence"


# ===================================================================
# Test Class 5: Statistical Discipline
# ===================================================================
class TestStatisticalDiscipline:
    """Illustrative scoring must be labeled; no empirical significance claimed."""

    def test_scorer_block_exists(self):
        assert get_scorer(), \
            "asymmetry_scorer_result_illustrative must exist"

    def test_methodology_says_manual_illustrative(self):
        method = get_scorer().get('methodology', '').lower()
        assert 'manual illustrative' in method, \
            "Methodology must state MANUAL ILLUSTRATIVE"
        assert 'not an empirical measurement' in method, \
            "Methodology must deny empirical measurement"

    def test_n_is_1_vs_2(self):
        scorer = get_scorer()
        assert len(scorer['peer_scores']) == 1, \
            "Meta side must have exactly 1 illustrative tone"
        assert len(scorer['target_scores']) == 2, \
            "Apple side must have exactly 2 illustrative tones"

    def test_p_value_not_calculated(self):
        scorer = get_scorer()
        assert scorer.get('p_value') == 'NOT_CALCULATED', \
            "p_value must be NOT_CALCULATED (no manufactured significance)"
        assert scorer.get('is_significant') is False, \
            "is_significant must be false"
        assert scorer.get('correlation_not_causation') is True, \
            "correlation_not_causation must be true"

    def test_delta_math(self):
        scorer = get_scorer()
        expected = round(scorer['target_avg'] - scorer['peer_avg'], 3)
        assert abs(scorer['delta'] - expected) < 1e-9, \
            f"delta {scorer['delta']} must equal target_avg - peer_avg = {expected}"
        assert scorer['delta'] == -0.75, \
            f"delta must be -0.75, got {scorer['delta']}"
        assert 'inversion' in scorer.get('delta_direction', '').lower(), \
            "delta_direction must name the inversion of the softer prediction"

    def test_score_leaf_types(self):
        scorer = get_scorer()
        assert all(isinstance(x, float) for x in scorer['target_scores']), \
            "target_scores must be a list of floats"
        assert all(isinstance(x, float) for x in scorer['peer_scores']), \
            "peer_scores must be a list of floats"
        assert isinstance(scorer['target_avg'], float), \
            "target_avg must be a float"
        assert isinstance(scorer['peer_avg'], float), \
            "peer_avg must be a float"
        assert isinstance(scorer['p_value'], str), \
            "p_value must be the string NOT_CALCULATED"


# ===================================================================
# Test Class 6: Incentive Context
# ===================================================================
class TestIncentiveContext:
    """The Atlantic-Apple DUAL tie and softer prediction must be recorded."""

    def test_apple_dual_tie_named(self):
        ctx = get_bogost_block().get('incentive_context', {})
        deal = ctx.get('deal', '')
        assert 'Apple' in deal, \
            "Must name the Atlantic-Apple financial tie"
        assert '17B' in deal or '$17B' in deal, \
            "Must name the ~$17B LPJ Trust AAPL holdings"
        assert 'Apple News+' in deal, \
            "Must name the Apple News+ platform revenue tie"

    def test_deal_urls(self):
        ctx = get_bogost_block().get('incentive_context', {})
        assert ctx.get('deal_url', '').startswith('http'), \
            "Deal needs a source URL (Digiday)"
        assert ctx.get('sec_url', '').startswith('http'), \
            "SEC EDGAR URL must be recorded"

    def test_coverage_prediction_and_result(self):
        ctx = get_bogost_block().get('incentive_context', {})
        assert ctx.get('coverage_prediction') == 'softer', \
            "Standing coverage_prediction must be 'softer'"
        assert ctx.get('meta_financial_tie') == 'none documented', \
            "Meta side must record no documented tie"
        assert 'invert' in ctx.get('prediction_result', '').lower(), \
            "Prediction result must record the writer-level inversion"

    def test_hypothesis_states_subordination_expectation(self):
        hyp = get_bogost_block().get('hypothesis', '').lower()
        assert 'subordinate' in hyp, \
            "Hypothesis must state writer ideology was expected subordinate to the incentive"


# ===================================================================
# Test Class 7: Novelty and Rotation
# ===================================================================
class TestNoveltyAndRotation:
    """Iteration 578 must be novel and correctly rotated (577 A -> 578 B)."""

    def test_iteration_is_578_type_b(self):
        block = get_bogost_block()
        assert block.get('iteration') == 578, \
            "iteration must be 578"
        assert block.get('type') == 'B', \
            "type must be B (Journalist Cross-Entity Tracking)"

    def test_rotation_from_577_type_a(self):
        block = get_bogost_block()
        novelty = block.get('novelty', '').lower()
        assert 'type_b_578' in block.get('novelty', ''), \
            "Novelty must name the 578 block key"
        assert 'first dedicated type b on ian bogost' in novelty, \
            "Novelty must assert first dedicated Type B on Ian Bogost"
        assert 'mechanism #572' in block.get('novelty', '').lower() or \
            'mechanism 572' in novelty, \
            "Novelty must distinguish from mechanism #572"

    def test_block_key_unique_on_entry(self):
        data = load_journalists()
        for j in data.get('journalists', []):
            if j.get('name') == 'Ian Bogost':
                keys = [k for k in j.get('competitor_coverage', {}).keys()
                        if '578' in str(k)]
                assert keys == [BLOCK_KEY], \
                    f"Exactly one 578 block must exist on Bogost, got {keys}"

    def test_novelty_distinguishes_reisner_16(self):
        novelty = get_bogost_block().get('novelty', '')
        assert '#16' in novelty or 'mechanism #16' in novelty.lower(), \
            "Novelty must distinguish from mechanism #16 (Reisner)"
