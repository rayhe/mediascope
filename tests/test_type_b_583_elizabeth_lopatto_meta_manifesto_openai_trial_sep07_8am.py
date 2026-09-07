"""
Test Type B #583: Elizabeth Lopatto (The Verge) Meta vs OpenAI Writer-Level
Consistency Check - Directionally Consistent but Non-Evidential

Type B: Journalist Cross-Entity Tracking - September 7, 2026 (08:00 PDT)

KEY FINDING: CONSISTENT-BUT-NON-EVIDENTIAL (bound), not a thesis win.
Elizabeth Lopatto is adversarial toward Meta's AI manifesto (Aug 10 2026
"Mark Zuckerberg doesn't understand how to live": "An AI future of sleek,
streamlined, and totally empty relationships.") and writes the Musk v.
Altman trial dispatch containing the "never been more sympathetic to Sam
Altman" line (Apr 29 2026 "Elon Musk's worst enemy in court is Elon Musk").
The ILLUSTRATIVE delta is +0.80 (OpenAI +0.10 minus Meta -0.70: target
softer than peer), directionally consistent with the softer-OpenAI prediction
under the Vox Media x OpenAI strategic partnership (May 29 2024, #494).
But the sympathy line is a Musk-relative measure, not an OpenAI measure:
it records how badly Musk performed on cross-examination, and the same
coverage mocks OpenAI's own Brockman and frames the trial as "nobody looks
good doing it". Genre mismatch (personal column vs courtroom dispatch) is
the standing Type B boundary condition. The unit bounds the corpus: a case
that looks direction-consistent on the headline line collapses under genre
and subject confounders.

Meta corpus (1 item, adversarial personal column):
- Aug 10 2026 "Mark Zuckerberg doesn't understand how to live" (solo
  Lopatto): adversarial column on Zuckerberg's "The Future Is For Everyone"
  AI manifesto; subhead "An AI future of sleek, streamlined, and totally
  empty relationships."

OpenAI corpus (1 item, courtroom dispatch):
- Apr 29 2026 "Elon Musk's worst enemy in court is Elon Musk" (solo
  Lopatto): Musk cross-examination day dispatch. "About five hours into Elon
  Musk's testimony, I typed the following sentence into my notes: 'I have
  never been more sympathetic to Sam Altman in my life.'"

CONFOUNDERS (5): STRONG genre asymmetry (personal adversarial column vs
courtroom dispatch - the standing Type B boundary condition); STRONG
Musk-relative subject (the sympathy line measures Musk's testimony, not
OpenAI's virtue); MODERATE timing mismatch (Apr vs Aug 2026); MODERATE thin
corpus (n=1 vs n=1); WEAK headline authorship (Verge headlines frequently
editor-written).

COUNTEREVIDENCE (4): Musk-relative measure (Altman-sympathy is a statement
about Musk's testimony, same logic as #578's not-Meta-the-company
counterevidence); within-piece anti-OpenAI-founder material (Brockman mocked,
"nobody looks good doing it"); #498 Swisher deal-partner falsification (same
Vox Media x OpenAI deal did not soften Swisher); #425 domain-bounding (Verge
incentive pattern held in the PRODUCT domain; courtroom genre is outside it).

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level, n=1
vs n=1, -1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical
significance test on hand-scored items would manufacture precision that does
not exist. is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-07):
- https://www.theverge.com/ai-artificial-intelligence/977623/mark-zuckerberg-ai-manifesto-dim-vision (manifesto essay; canonical URL via wesearch.press metadata, byline + pub time 2026-08-10T18:00:00-04:00)
- https://www.theverge.com/tech/921022/elon-musk-cross-openai-altman (trial dispatch; canonical URL via GitHub ai-news-tracker 2026-04-30.md verbatim listing)
- https://wesearch.press/s/mark-zuckerberg-doesnt-understand-how-to-live-d8f43f47 (wesearch metadata for manifesto essay)
- https://www.youtube.com/watch?v=f4KgyG-AuAo (Vergecast video discussing the manifesto essay)
- https://www.youtube.com/watch?v=xWCq5pYmBu4 (Vergecast: Musk v. Altman trial discussion)
- https://about.fb.com/news/2026/08/the-future-is-for-everyone/ (primary Meta manifesto)
- https://github.com/aredwan-xyz/ai-news-tracker/blob/HEAD/news/2026-04-30.md (trial piece URL listing)
- https://inkbrief.in/article/elon-musks-worst-enemy-in-court-is-elon-musk-278828 (byline + verbatim quote corroboration)
- https://times42.com/11971135 (byline corroboration: "Elizabeth Lopatto @ The Verge")
- https://washingtonhorizon.com/musk-v-altman-tea-temper-and-a-stargate-cameo-as-tesla-ceo-testifies-in-openai-trial/ (line attributed to Lopatto)
- https://www.el-balad.com/17002456 (verbatim quote corroboration)
- https://www.reuters.com/technology/openai-signs-content-deals-with-atlantic-vox-media-2024-05-29/ (Vox Media x OpenAI deal, May 29 2024, in-corpus)
"""

import os

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

BLOCK_KEY = 'type_b_583_elizabeth_lopatto_meta_manifesto_openai_trial'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_lopatto_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Elizabeth Lopatto':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


def get_scorer(block=None):
    block = block if block is not None else get_lopatto_block()
    return block.get('asymmetry_scorer_result_illustrative', {})


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 1-vs-1 within-writer corpus."""

    def test_block_exists(self):
        assert get_lopatto_block(), \
            f"{BLOCK_KEY} must exist on Elizabeth Lopatto"

    def test_iteration_and_date(self):
        block = get_lopatto_block()
        assert block.get('iteration') == 583, \
            f"iteration must be 583, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-07', \
            f"date must be 2026-09-07, got {block.get('date')}"

    def test_design_is_within_journalist_verge(self):
        design = get_lopatto_block().get('design', '').lower()
        assert 'within-journalist' in design and 'verge' in design, \
            f"design must be within-journalist at The Verge, got: {design}"

    def test_meta_corpus_count(self):
        corpus = get_lopatto_block().get('meta_corpus', [])
        assert len(corpus) == 1, \
            f"Meta corpus must have exactly 1 item, got {len(corpus)}"

    def test_openai_corpus_count(self):
        corpus = get_lopatto_block().get('openai_corpus', [])
        assert len(corpus) == 1, \
            f"OpenAI corpus must have exactly 1 item, got {len(corpus)}"

    def test_every_item_has_source_url_and_verification(self):
        block = get_lopatto_block()
        for item in block['meta_corpus'] + block['openai_corpus']:
            assert isinstance(item, dict), \
                f"corpus item must be a dict, got {type(item)}: {item}"
            assert item.get('url', '').startswith('http'), \
                f"Every corpus item needs a source URL, missing on: {item.get('title')}"
            assert item.get('verification'), \
                f"Every corpus item needs a verification note: {item.get('title')}"
            assert 'lopatto' in item.get('byline', '').lower(), \
                f"Every corpus item must carry a Lopatto byline: {item.get('title')}"

    def test_meta_flagship_is_manifesto_essay(self):
        corpus = get_lopatto_block()['meta_corpus']
        piece = corpus[0]
        assert "doesn't understand how to live" in piece.get('title', '').lower(), \
            "Meta corpus must be the manifesto essay"
        assert piece.get('date') == '2026-08-10', \
            f"Meta piece date must be 2026-08-10, got {piece.get('date')}"
        assert piece.get('url') == \
            'https://www.theverge.com/ai-artificial-intelligence/977623/mark-zuckerberg-ai-manifesto-dim-vision', \
            "Meta piece must carry the exact canonical Verge URL"
        assert 'adversarial' in piece.get('register', '').lower(), \
            "Meta piece register must be adversarial"
        assert 'empty relationships' in piece.get('verbatim_markers', '').lower(), \
            "Meta piece must carry the 'empty relationships' subhead marker"

    def test_openai_trial_dispatch(self):
        corpus = get_lopatto_block()['openai_corpus']
        piece = corpus[0]
        assert "worst enemy in court" in piece.get('title', '').lower(), \
            "OpenAI corpus must be the trial dispatch"
        assert piece.get('date') == '2026-04-29', \
            f"Trial piece date must be 2026-04-29, got {piece.get('date')}"
        assert piece.get('url') == \
            'https://www.theverge.com/tech/921022/elon-musk-cross-openai-altman', \
            "Trial piece must carry the exact canonical Verge URL"
        assert 'courtroom' in piece.get('register', '').lower(), \
            "Trial piece register must be courtroom dispatch"
        assert 'never been more sympathetic to sam altman' in \
            piece.get('verbatim_markers', '').lower(), \
            "Trial piece must carry the Altman-sympathy verbatim marker"


# ===================================================================
# Test Class 2: Consistent-But-Non-Evidential Finding
# ===================================================================
class TestConsistentButNonEvidentialFinding:
    """The finding must assert directional consistency with a bound, not a win."""

    def test_finding_names_manifesto_marker(self):
        finding = get_lopatto_block().get('finding', '').lower()
        assert 'empty relationships' in finding, \
            "Finding must cite the Meta-side adversarial marker"

    def test_finding_names_sympathy_line(self):
        finding = get_lopatto_block().get('finding', '').lower()
        assert 'sympathetic to sam altman' in finding, \
            "Finding must cite the Altman-sympathy line"

    def test_finding_asserts_directional_consistency(self):
        finding = get_lopatto_block().get('finding', '')
        assert 'CONSISTENT-BUT-NON-EVIDENTIAL' in finding, \
            "Finding must state the consistent-but-non-evidential verdict"

    def test_finding_denies_thesis_win(self):
        finding = get_lopatto_block().get('finding', '').lower()
        assert 'not a thesis win' in finding, \
            "Finding must explicitly deny that this is a thesis win"

    def test_finding_names_musk_relative_measure(self):
        finding = get_lopatto_block().get('finding', '').lower()
        assert 'musk-relative' in finding, \
            "Finding must state the sympathy line is a Musk-relative measure"

    def test_finding_denies_causal_claim(self):
        finding = get_lopatto_block().get('finding', '')
        assert 'CORRELATION NOT CAUSATION' in finding, \
            "Finding must explicitly deny a causal claim"

    def test_finding_cross_references_498(self):
        block = get_lopatto_block()
        joined = (block.get('finding', '') + ' ' +
                  str(block.get('counterevidence', ''))).lower()
        assert '#498' in joined or 'mechanism 494' in joined, \
            "Finding/counterevidence must cross-reference #498/#494 (the deal)"


# ===================================================================
# Test Class 3: Confounders
# ===================================================================
class TestConfounders:
    """Five ranked confounders must be recorded."""

    def test_confounder_count(self):
        confounders = get_lopatto_block().get('confounders', [])
        assert len(confounders) == 5, \
            f"Must record exactly 5 confounders, got {len(confounders)}"

    def test_genre_confounder_is_strong(self):
        confounders = get_lopatto_block()['confounders']
        genre = next(c for c in confounders if 'genre' in c.lower())
        assert genre.startswith('[STRONG]'), \
            "Genre asymmetry must be rated STRONG"
        assert '498' in genre or '578' in genre, \
            "Genre confounder must cross-reference the boundary-condition family"

    def test_musk_relative_confounder_is_strong(self):
        confounders = get_lopatto_block()['confounders']
        musk = next(c for c in confounders
                    if 'musk-relative' in c.lower())
        assert musk.startswith('[STRONG]'), \
            "Musk-relative subject must be rated STRONG"
        assert 'cross-examination' in musk.lower(), \
            "Must name cross-examination as the contaminating event"

    def test_timing_confounder_present(self):
        confounders = get_lopatto_block()['confounders']
        assert any('timing' in c.lower() for c in confounders), \
            "Must include the timing-mismatch confounder (Apr vs Aug 2026)"

    def test_thin_corpus_confounder_present(self):
        confounders = get_lopatto_block()['confounders']
        thin = next(c for c in confounders if 'n=1' in c.lower())
        assert 'moderate' in thin.lower(), \
            "Thin corpus (n=1 vs n=1) must be rated MODERATE"

    def test_headline_authorship_confounder_is_weak(self):
        confounders = get_lopatto_block()['confounders']
        headline = next(c for c in confounders if 'headline' in c.lower())
        assert headline.startswith('[WEAK]'), \
            "Headline authorship must be rated WEAK"


# ===================================================================
# Test Class 4: Counterevidence
# ===================================================================
class TestCounterevidence:
    """Four counterevidence items must be recorded."""

    def test_counterevidence_count(self):
        ce = get_lopatto_block().get('counterevidence', [])
        assert len(ce) == 4, \
            f"Must record exactly 4 counterevidence items, got {len(ce)}"

    def test_musk_relative_measure_present(self):
        ce = get_lopatto_block()['counterevidence']
        assert any('musk-relative' in c.lower() for c in ce), \
            "Must include the Musk-relative-measure counterevidence"

    def test_brockman_mockery_present(self):
        ce = get_lopatto_block()['counterevidence']
        assert any('brockman' in c.lower() for c in ce), \
            "Must include the within-piece Brockman-mockery counterevidence"

    def test_498_swisher_present(self):
        ce = get_lopatto_block()['counterevidence']
        assert any('#498' in c for c in ce), \
            "Must include the #498 Swisher deal-partner falsification counterevidence"

    def test_425_domain_bound_present(self):
        ce = get_lopatto_block()['counterevidence']
        assert any('#425' in c for c in ce), \
            "Must include the #425 domain-bounding counterevidence"


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

    def test_n_is_1_vs_1(self):
        scorer = get_scorer()
        assert len(scorer['peer_scores']) == 1, \
            "Meta side must have exactly 1 illustrative tone"
        assert len(scorer['target_scores']) == 1, \
            "OpenAI side must have exactly 1 illustrative tone"

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
        assert scorer['delta'] == 0.8, \
            f"delta must be 0.8, got {scorer['delta']}"
        assert 'consistent' in scorer.get('delta_direction', '').lower(), \
            "delta_direction must name the directional consistency with the prediction"
        assert 'non-evidential' in scorer.get('delta_direction', '').lower(), \
            "delta_direction must carry the non-evidential bound"

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
    """The Vox Media x OpenAI deal and softer prediction must be recorded."""

    def test_openai_deal_named(self):
        ctx = get_lopatto_block().get('incentive_context', {})
        deal = ctx.get('deal', '')
        assert 'Vox Media' in deal and 'OpenAI' in deal, \
            "Must name the Vox Media x OpenAI financial tie"
        assert '#494' in deal, \
            "Must cite in-corpus deal mechanism #494"

    def test_deal_url_and_date(self):
        ctx = get_lopatto_block().get('incentive_context', {})
        assert ctx.get('deal_url', '').startswith('http'), \
            "Deal needs a source URL (Reuters)"
        assert ctx.get('deal_date') == '2024-05-29', \
            "Deal date must be 2024-05-29"

    def test_coverage_prediction_and_result(self):
        ctx = get_lopatto_block().get('incentive_context', {})
        assert ctx.get('coverage_prediction') == 'softer', \
            "Standing coverage_prediction must be 'softer'"
        assert ctx.get('meta_financial_tie') == 'none documented', \
            "Meta side must record no documented tie"
        assert 'non-evidential' in ctx.get('prediction_result', '').lower(), \
            "Prediction result must record the non-evidential bound"

    def test_hypothesis_states_prediction(self):
        hyp = get_lopatto_block().get('hypothesis', '').lower()
        assert 'softer openai' in hyp, \
            "Hypothesis must state the softer-OpenAI prediction"


# ===================================================================
# Test Class 7: Novelty and Rotation
# ===================================================================
class TestNoveltyAndRotation:
    """Iteration 583 must be novel and correctly rotated (582 A -> 583 B)."""

    def test_iteration_is_583_type_b(self):
        block = get_lopatto_block()
        assert block.get('iteration') == 583, \
            "iteration must be 583"
        assert block.get('type') == 'B', \
            "type must be B (Journalist Cross-Entity Tracking)"

    def test_rotation_from_582_type_a(self):
        novelty = get_lopatto_block().get('novelty', '')
        assert 'type_b_583' in novelty, \
            "Novelty must name the 583 block key"
        assert 'first dedicated type b on elizabeth lopatto' in novelty.lower(), \
            "Novelty must assert first dedicated Type B on Elizabeth Lopatto"

    def test_block_key_unique_on_entry(self):
        data = load_journalists()
        for j in data.get('journalists', []):
            if j.get('name') == 'Elizabeth Lopatto':
                keys = [k for k in j.get('competitor_coverage', {}).keys()
                        if '583' in str(k)]
                assert keys == [BLOCK_KEY], \
                    f"Exactly one 583 block must exist on Lopatto, got {keys}"

    def test_novelty_distinguishes_prior_units(self):
        novelty = get_lopatto_block().get('novelty', '')
        assert '#436' in novelty, \
            "Novelty must distinguish from #436 (Goode)"
        assert '#498' in novelty, \
            "Novelty must distinguish from #498 (Swisher, same deal)"
        assert '#578' in novelty, \
            "Novelty must distinguish from #578 (Bogost, opposite verdict class)"

    def test_exactly_one_583_test_file(self):
        import glob
        files = glob.glob(os.path.join(os.path.dirname(__file__),
                                       'test_type_b_583*.py'))
        assert len(files) == 1 and os.path.basename(files[0]) == \
            'test_type_b_583_elizabeth_lopatto_meta_manifesto_openai_trial_sep07_8am.py', \
            f"Exactly one 583 test file must exist, got {files}"
