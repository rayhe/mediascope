"""
Test Type B #513: Dara Kerr (Guardian) Meta vs OpenAI Genre-Conditioned Register Split

Type B: Journalist Cross-Entity Tracking - September 4, 2026 (07:00 PDT)

KEY FINDING: DIRECTIONAL SUPPORT for the deal-incentive theory, heavily bounded
and not causal evidence. Dara Kerr, Guardian US tech reporter hired Jan 2025
(one month before the Feb 14 2025 Guardian-OpenAI licensing deal), applies an
adversarial accountability register to Meta and a neutral business-news register
to OpenAI. First dedicated deal-partner-side Type B data point; joins the
confirmation side of the theory.

Meta corpus (2 items, adversarial accountability):
- Aug 18 2026 "US states accuse Meta of covering up research on teen social
  media addiction in pivotal trial" (solo Kerr, courtroom): only outlet to quote
  the 233-page complaint itself; Kentucky AG tobacco-blueprint framing; Meta's
  response included; $200bn ask adjacent to the 1998 tobacco $200bn payout
  (reporter-level adjacency device).
- Mar 2026 "Landmark losses for Meta and YouTube as Big Tech misses point"
  (Kerr analysis via TechScape newsletter mirror): "In the span of just two days,
  the most powerful social media company in the world faced a more severe
  public reckoning than it has in years."

OpenAI corpus (2 items, neutral business news / balanced race frame):
- Jun 8 2026 "OpenAI confidentially files for initial public offering on US
  stock market" (Montgomery + Kerr): "$850bn+" valuation relayed unchallenged.
- Aug 9 2025 "'It's missing something': AGI, superintelligence and a race for
  the future" (Milmo + Kerr): Altman's "significant step on the path to AGI"
  relayed with his own caveat plus independent skepticism (Evans "very
  vibes-based", Bader "nowhere near that threshold"); Zuckerberg's
  "superintelligence is now in sight" in the same shared frame.

CONFOUNDERS (5): STRONG genre asymmetry (lawsuit/trial vs IPO/product launch);
STRONG fresh-hire timing (hired Jan 2025, deal Feb 14 2025 - inseparable);
MODERATE co-byline on both OpenAI items; MODERATE bounded second-hand
evidence (theguardian.com direct fetch policy-blocked); WEAK date span.

COUNTEREVIDENCE (4): same-event symmetry (landmark-losses frame hits YouTube/
Google too); shared race frame (skepticism applied to Altman as well);
outlet-consistent (Guardian has no Meta deal; adversarial Meta history since
Cambridge Analytica 2018); legitimate courtroom reporting (tobacco analogy is
the AGs' stated method, Meta's response included).

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level, n=2 vs
n=2, -1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical
significance test on two hand-scored items per side would manufacture precision
that does not exist. is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-04):
- https://www.theguardian.com/technology/2026/aug/18/meta-child-safety-addiction-lawsuit-states
- https://github.com/geeks-accelerator/de-amplify/blob/HEAD/docs/research/single-source/2026-08-18-guardian.md
- https://d33gy59ovltp76.cloudfront.net/news/landmark-losses-for-meta-and-youtube-as-big-tech-misses-point
- https://www.theguardian.com/technology/2026/jun/08/openai-ipo-files-for-public-stock-market
- https://www.theguardian.com/technology/2025/aug/09/its-missing-something-agi-superintelligence-and-a-race-for-the-future
- https://github.com/dbader13/academic-kickstart/blob/HEAD/content/post/20250809-Guardian/index.md
- http://openai.com/index/openai-and-guardian-media-group-launch-content-partnership/
- https://talkingbiznews.com/media-news/guardian-hires-kerr-as-a-tech-reporter/
"""

import os

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

BLOCK_KEY = 'type_b_513_dara_kerr_meta_openai_genre_conditioned_register_split'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_kerr_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Dara Kerr':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


def get_scorer(block=None):
    block = block if block is not None else get_kerr_block()
    return block.get('asymmetry_scorer_result_illustrative', {})


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 2+2 cross-entity corpus."""

    def test_block_exists(self):
        assert get_kerr_block(), \
            f"{BLOCK_KEY} must exist on Dara Kerr"

    def test_iteration_and_date(self):
        block = get_kerr_block()
        assert block.get('iteration') == 513, \
            f"iteration must be 513, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-04', \
            f"date must be 2026-09-04, got {block.get('date')}"

    def test_design_is_within_journalist(self):
        design = get_kerr_block().get('design', '').lower()
        assert 'within-journalist' in design and 'guardian' in design, \
            f"design must be within-journalist at the Guardian, got: {design}"

    def test_meta_corpus_count(self):
        corpus = get_kerr_block().get('meta_corpus', [])
        assert len(corpus) == 2, \
            f"Meta corpus must have exactly 2 items, got {len(corpus)}"

    def test_openai_corpus_count(self):
        corpus = get_kerr_block().get('openai_corpus', [])
        assert len(corpus) == 2, \
            f"OpenAI corpus must have exactly 2 items, got {len(corpus)}"

    def test_every_item_has_source_url(self):
        block = get_kerr_block()
        for item in block['meta_corpus'] + block['openai_corpus']:
            assert isinstance(item, dict), \
                f"corpus item must be a dict, got {type(item)}: {item}"
            assert item.get('url', '').startswith('http'), \
                f"Every corpus item needs a source URL, missing on: {item.get('title')}"
            assert item.get('verification'), \
                f"Every corpus item needs a verification note: {item.get('title')}"

    def test_meta_flagship_is_addiction_trial_piece(self):
        corpus = get_kerr_block()['meta_corpus']
        assert any('covering up' in i.get('title', '').lower() for i in corpus), \
            "Meta corpus must include the cover-up addiction-trial piece"
        piece = next(i for i in corpus if 'covering up' in i['title'].lower())
        assert piece.get('date') == '2026-08-18', \
            f"Trial piece date must be 2026-08-18, got {piece.get('date')}"
        assert 'solo' in piece.get('byline', '').lower(), \
            "Must record the solo Kerr byline on the trial piece"
        assert piece.get('url') == \
            'https://www.theguardian.com/technology/2026/aug/18/meta-child-safety-addiction-lawsuit-states', \
            "Trial piece must carry the exact canonical Guardian URL"

    def test_meta_landmark_losses_quoted(self):
        corpus = get_kerr_block()['meta_corpus']
        piece = next(i for i in corpus if 'landmark losses' in i['title'].lower())
        assert 'severe public reckoning' in piece.get('verbatim_markers', ''), \
            "Landmark-losses item must carry the verbatim reckoning quote"

    def test_openai_flagship_is_ipo_piece(self):
        corpus = get_kerr_block()['openai_corpus']
        assert any('initial public offering' in i.get('title', '').lower()
                   for i in corpus), \
            "OpenAI corpus must include the IPO filing piece"
        piece = next(i for i in corpus if 'initial public offering' in i['title'].lower())
        assert piece.get('date') == '2026-06-08', \
            f"IPO piece date must be 2026-06-08, got {piece.get('date')}"
        assert 'Kerr' in piece.get('byline', ''), \
            "Must record Kerr on the IPO byline"
        assert piece.get('url') == \
            'https://www.theguardian.com/technology/2026/jun/08/openai-ipo-files-for-public-stock-market', \
            "IPO piece must carry the exact canonical Guardian URL"

    def test_openai_agi_piece_is_balanced_race_frame(self):
        corpus = get_kerr_block()['openai_corpus']
        piece = next(i for i in corpus if 'missing something' in i['title'].lower())
        assert piece.get('date') == '2025-08-09', \
            f"AGI piece date must be 2025-08-09, got {piece.get('date')}"
        assert piece.get('register') == 'balanced race-frame reporting', \
            "AGI piece must be recorded as balanced race-frame, not claim relay"
        markers = piece.get('verbatim_markers', '').lower()
        assert 'vibes-based' in markers or 'nowhere near' in markers, \
            "AGI piece must carry the independent-skepticism verbatim markers"


# ===================================================================
# Test Class 2: Register-Split Finding
# ===================================================================
class TestRegisterSplitFinding:
    """The finding must assert the directional register split with bounds."""

    def test_finding_names_meta_adversarial_markers(self):
        finding = get_kerr_block().get('finding', '').lower()
        assert 'covering up' in finding or 'cover-up' in finding, \
            "Finding must cite the Meta-side adversarial marker (cover-up)"
        assert 'tobacco' in finding, \
            "Finding must cite the tobacco-blueprint marker"

    def test_finding_names_openai_business_markers(self):
        finding = get_kerr_block().get('finding', '').lower()
        assert '850bn' in finding, \
            "Finding must cite the OpenAI-side business marker ($850bn valuation)"
        assert 'agi' in finding, \
            "Finding must cite the AGI race-frame item"

    def test_finding_asserts_directional_support(self):
        finding = get_kerr_block().get('finding', '').lower()
        assert 'directional support' in finding, \
            "Finding must state directional support (not proof) for the theory"

    def test_finding_denies_causal_claim(self):
        finding = get_kerr_block().get('finding', '')
        assert 'CORRELATION NOT CAUSATION' in finding, \
            "Finding must explicitly deny a causal claim"

    def test_finding_notes_first_deal_partner_datapoint(self):
        finding = get_kerr_block().get('finding', '').lower()
        assert 'first' in finding and 'deal-partner' in finding, \
            "Finding must note this is the first dedicated deal-partner-side Type B data point"

    def test_finding_notes_genre_boundary_condition(self):
        finding = get_kerr_block().get('finding', '').lower()
        assert 'genre' in finding, \
            "Finding must engage the genre boundary condition"


# ===================================================================
# Test Class 3: Confounders
# ===================================================================
class TestConfounders:
    """Five ranked confounders must be recorded."""

    def test_confounder_count(self):
        confounders = get_kerr_block().get('confounders', [])
        assert len(confounders) == 5, \
            f"Must record exactly 5 confounders, got {len(confounders)}"

    def test_genre_confounder_is_strong(self):
        confounders = get_kerr_block()['confounders']
        genre = next(c for c in confounders if 'genre' in c.lower())
        assert genre.startswith('[STRONG]'), \
            "Genre asymmetry must be rated STRONG"
        assert '493' in genre and '508' in genre, \
            "Genre confounder must cross-reference the falsification/boundary family"

    def test_fresh_hire_confounder_is_strong(self):
        confounders = get_kerr_block()['confounders']
        hire = next(c for c in confounders if 'fresh-hire' in c.lower())
        assert hire.startswith('[STRONG]'), \
            "Fresh-hire timing must be rated STRONG"

    def test_cobyline_confounder_present(self):
        confounders = get_kerr_block()['confounders']
        assert any('co-byline' in c.lower() for c in confounders), \
            "Must include the co-byline confounder"

    def test_bounded_evidence_confounder_present(self):
        confounders = get_kerr_block()['confounders']
        bounded = next(c for c in confounders if 'bounded' in c.lower())
        assert 'policy-blocked' in bounded.lower(), \
            "Bounded-evidence confounder must name the theguardian.com fetch block"


# ===================================================================
# Test Class 4: Counterevidence
# ===================================================================
class TestCounterevidence:
    """Four counterevidence items must be recorded."""

    def test_counterevidence_count(self):
        ce = get_kerr_block().get('counterevidence', [])
        assert len(ce) == 4, \
            f"Must record exactly 4 counterevidence items, got {len(ce)}"

    def test_same_event_symmetry_present(self):
        ce = get_kerr_block()['counterevidence']
        assert any('youtube' in c.lower() or 'google' in c.lower() for c in ce), \
            "Must include the same-event symmetry counterevidence (YouTube/Google)"

    def test_shared_race_frame_present(self):
        ce = get_kerr_block()['counterevidence']
        assert any('race frame' in c.lower() for c in ce), \
            "Must include the shared race-frame counterevidence"

    def test_outlet_consistent_present(self):
        ce = get_kerr_block()['counterevidence']
        assert any('cambridge analytica' in c.lower() for c in ce), \
            "Must include the outlet-consistent counterevidence (Cambridge Analytica)"


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

    def test_n_is_2_vs_2(self):
        scorer = get_scorer()
        assert len(scorer['target_scores']) == 2, \
            "Meta side must have exactly 2 illustrative tones"
        assert len(scorer['peer_scores']) == 2, \
            "OpenAI side must have exactly 2 illustrative tones"

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
        assert scorer['delta'] == -0.65, \
            f"delta must be -0.65, got {scorer['delta']}"

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
    """The Guardian-OpenAI deal and Kerr's hire timing must be recorded."""

    def test_deal_named(self):
        ctx = get_kerr_block().get('incentive_context', {})
        assert 'OpenAI' in ctx.get('deal', ''), \
            "Must name the Guardian-OpenAI deal"

    def test_deal_date_and_url(self):
        ctx = get_kerr_block().get('incentive_context', {})
        assert ctx.get('deal_date') == '2025-02-14', \
            f"Deal date must be 2025-02-14, got {ctx.get('deal_date')}"
        assert ctx.get('deal_url', '').startswith('http'), \
            "Deal needs a source URL"

    def test_hire_timing_recorded(self):
        ctx = get_kerr_block().get('incentive_context', {})
        assert ctx.get('reporter_hire_date') == '2025-01', \
            "Must record Kerr's Jan 2025 hire date"
        assert 'one month' in ctx.get('timing_note', '').lower(), \
            "Timing note must flag the one-month gap to the deal"

    def test_hire_source_url(self):
        ctx = get_kerr_block().get('incentive_context', {})
        assert ctx.get('hire_source_url', '').startswith('http'), \
            "Hire timing needs a source URL"
