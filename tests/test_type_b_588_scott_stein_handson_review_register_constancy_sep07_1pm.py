"""
Test Type B #588: Scott Stein (CNET) hands-on review register constancy -
Meta Ray-Ban Display (Sep 2025) vs Samsung Galaxy XR (Oct 2025).

Type B: Journalist Cross-Entity Tracking - September 7, 2026 (13:00 PDT)

KEY FINDING: REGISTER CONSTANCY (bound), not a gradient win.
Stein runs the same enthusiastic hands-on reviewer register on Meta and on
Samsung/Google hardware. Both pieces carry superlative framing, gushing
capability claims ("wild to use" / "the start of a new paradigm" for Meta;
"Like Apple Vision Pro for Half the Price (and Twice the AI)" / "an
all-seeing type of magic" for Samsung), measured product caveats on both
sides, named-executive access on both sides (Zuckerberg/Himmel/White for
Meta; Choi/Samat for Samsung/Google), and zero adversarial privacy framing
for either. The ILLUSTRATIVE delta is -0.05 (Meta +0.65 minus Samsung/Google
+0.70), inside hand-scoring noise.

This bounds in-corpus mechanism #106 (Scott Stein entity-selective
enthusiasm gradient with privacy deferral, found in the May 2026 Google I/O
news/launch-keynote piece): the gradient is a news-register phenomenon, not
Stein's writer-level review register. It does not replicate in Stein's
product hands-ons.

Meta corpus (1 item, hands-on at Meta campus, Sep 18 2025):
- "I Wore Meta's New Ray-Ban Display Glasses and Neural Band. I Feel
  Augmented" (CNET, $799, on sale Sep 30 2025). Headline-level enthusiasm,
  caveats: battery claim "take that with a grain of salt", +4.00/-4.00
  prescription limits, "functional step down from the Orion dream of last
  year", "major questions about how it'll work in the real world".
  Privacy: ZERO mentions in full text; display invisibility framed as a
  PERK ("Maybe I could privately see things displayed and not weird anyone
  out").

Samsung/Google corpus (1 item, hands-on at Samsung midtown NYC demo,
Oct 22 2025):
- "I Tried Samsung Galaxy XR: Like Apple Vision Pro for Half the Price
  (and Twice the AI)" (CNET, $1,799). Superlative headline, capability
  gushing, caveats: "hard to see who the Galaxy XR is meant for at its
  price", "feels as much like a stepping stone as an actual product",
  "Gemini's accuracy is still imperfect, though", "still very expensive".
  Privacy: no adversarial framing; camera AI "see what you're seeing"
  repeated as capability; one privacy-control line via Google exec quote
  (Samat: "you can authorize particular apps to be visible by the
  camera-enabled AI, and hide others").

CONFOUNDERS (6): STRONG hands-on demo genre (company-controlled demos -
the standing Type B genre boundary); STRONG product-class asymmetry
(glasses vs VR headset, different evaluation baselines); MODERATE
symmetric executive access (capture risk is equal, not entity-selective);
MODERATE thin corpus (n=1 vs n=1); WEAK headline authorship; WEAK five-week
timing gap.

COUNTEREVIDENCE (4): honest-reviewer caveats on both sides (not captured
puffery); the Samsung piece explicitly ranks the XR2+ Gen 2 as "better
than the Meta Quest 3" (Meta not spared); privacy deferral is
symmetric-non-adversarial (Meta zero mentions, Samsung/Google one exec
line - neither adversarial); Apple Vision Pro used as the NEUTRAL
benchmark in BOTH pieces with mixed verdicts for all parties.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level, n=1
vs n=1, -1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical
significance test on hand-scored items would manufacture precision that
does not exist. is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-07):
- https://newsatw.com/i-wore-metas-new-ray-ban-display-glasses-and-neural-band-i-feel-augmented/ (Meta Display piece, full CNET text mirror, Scott Stein/CNET photo credits; corroborated by newsflash.one + motozurnals.lv)
- https://newsatw.com/i-tried-samsung-galaxy-xr-like-apple-vision-pro-for-half-the-price-and-twice-the-ai/ (Galaxy XR piece, full CNET text mirror, Scott Stein/CNET photo credits; corroborated by newsflash.one + parlournews.com + technologynewso.com + telestraw.com)
- CNET YouTube channel: "I Tried Samsung Galaxy XR: Like Apple Vision Pro for Half the Price (and Twice the AI) https://zdcs.link/aADDRw" (official CNET promotion of the piece)
- https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear (independent corroboration: "tech blog CNET described as Like Apple Vision Pro for half the price")
- Canonical cnet.com URLs not retrievable via search this run (no URL guessing per browser rules); handled per iteration-492: multi-mirror corroboration, no zero-coverage claims.
"""

import glob
import os

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

BLOCK_KEY = 'type_b_588_scott_stein_handson_review_register_constancy'

TEST_FILE_NAME = 'test_type_b_588_scott_stein_handson_review_register_constancy_sep07_1pm.py'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_stein_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Scott Stein':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


def get_scorer(block=None):
    block = block if block is not None else get_stein_block()
    return block.get('asymmetry_scorer_result_illustrative', {})


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 1-vs-1 within-writer corpus."""

    def test_block_exists(self):
        assert get_stein_block(), \
            f"{BLOCK_KEY} must exist on Scott Stein"

    def test_iteration_and_date(self):
        block = get_stein_block()
        assert block.get('iteration') == 588, \
            f"iteration must be 588, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-07', \
            f"date must be 2026-09-07, got {block.get('date')}"

    def test_design_is_within_journalist_handson(self):
        design = get_stein_block().get('design', '').lower()
        assert 'within-journalist' in design, \
            f"design must be within-journalist, got: {design}"
        assert 'hands-on' in design or 'handson' in design.replace('-', ''), \
            f"design must name the hands-on-review register, got: {design}"

    def test_meta_item_has_title_date_sources(self):
        meta = get_stein_block().get('meta_item', {})
        assert 'Ray-Ban Display' in meta.get('title', ''), \
            "Meta item must be the Ray-Ban Display piece"
        assert meta.get('date') == '2025-09-18', \
            f"Meta item date must be 2025-09-18, got {meta.get('date')}"
        urls = meta.get('source_urls', [])
        assert len(urls) >= 3, \
            f"Meta item needs >=3 corroborating source URLs, got {len(urls)}"
        assert any('newsatw.com' in u for u in urls), \
            "newsatw.com mirror must be among the Meta sources"

    def test_samsung_item_has_title_date_sources(self):
        peer = get_stein_block().get('samsung_google_item', {})
        assert 'Galaxy XR' in peer.get('title', ''), \
            "Peer item must be the Galaxy XR piece"
        assert peer.get('date') == '2025-10-22', \
            f"Peer item date must be 2025-10-22, got {peer.get('date')}"
        urls = peer.get('source_urls', [])
        assert len(urls) >= 4, \
            f"Peer item needs >=4 corroborating source URLs, got {len(urls)}"
        assert any('newsatw.com' in u for u in urls), \
            "newsatw.com mirror must be among the peer sources"

    def test_both_items_stein_cnet_authorship(self):
        block = get_stein_block()
        assert block['meta_item'].get('byline') == 'Scott Stein', \
            "Meta item byline must be Scott Stein"
        assert block['samsung_google_item'].get('byline') == 'Scott Stein', \
            "Peer item byline must be Scott Stein"
        assert block['meta_item'].get('publication') == 'cnet', \
            "Meta item publication must be cnet"
        assert block['samsung_google_item'].get('publication') == 'cnet', \
            "Peer item publication must be cnet"


# ===================================================================
# Test Class 2: Register Constancy Finding
# ===================================================================
class TestRegisterConstancyFinding:
    """The block must document the constancy finding with quote evidence."""

    def test_verdict_is_register_constancy(self):
        verdict = get_stein_block().get('verdict', '')
        assert verdict.startswith('register_constancy'), \
            f"verdict must be register_constancy, got: {verdict[:60]}"

    def test_meta_enthusiasm_quotes_present(self):
        quotes = get_stein_block()['meta_item'].get('enthusiasm_quotes', [])
        assert len(quotes) >= 5, \
            f"Meta item needs >=5 enthusiasm quotes, got {len(quotes)}"
        blob = ' '.join(quotes).lower()
        assert 'new paradigm' in blob, \
            "Meta quotes must include the neural-band paradigm line"
        assert 'wild to use' in blob, \
            "Meta quotes must include the 'wild to use' line"

    def test_samsung_enthusiasm_quotes_present(self):
        quotes = get_stein_block()['samsung_google_item'].get('enthusiasm_quotes', [])
        assert len(quotes) >= 6, \
            f"Peer item needs >=6 enthusiasm quotes, got {len(quotes)}"
        blob = ' '.join(quotes).lower()
        assert 'half the price' in blob, \
            "Peer quotes must include the headline value-framing line"
        assert 'all-seeing type of magic' in blob, \
            "Peer quotes must include the Gemini magic line"

    def test_meta_caveats_present(self):
        caveats = get_stein_block()['meta_item'].get('caveats', [])
        assert len(caveats) >= 4, \
            f"Meta item needs >=4 caveats, got {len(caveats)}"
        blob = ' '.join(caveats).lower()
        assert 'grain of salt' in blob, \
            "Meta caveats must include the battery grain-of-salt line"
        assert 'orion' in blob, \
            "Meta caveats must include the Orion step-down line"

    def test_samsung_caveats_present(self):
        caveats = get_stein_block()['samsung_google_item'].get('caveats', [])
        assert len(caveats) >= 4, \
            f"Peer item needs >=4 caveats, got {len(caveats)}"
        blob = ' '.join(caveats).lower()
        assert 'stepping stone' in blob, \
            "Peer caveats must include the stepping-stone line"
        assert 'imperfect' in blob, \
            "Peer caveats must include the Gemini accuracy caveat"

    def test_symmetric_exec_access(self):
        block = get_stein_block()
        meta_exec = block['meta_item'].get('meta_exec_access', [])
        peer_exec = block['samsung_google_item'].get('samsung_google_exec_access', [])
        assert len(meta_exec) >= 3, \
            f"Meta exec access needs >=3 named sources, got {len(meta_exec)}"
        assert len(peer_exec) >= 2, \
            f"Peer exec access needs >=2 named sources, got {len(peer_exec)}"
        assert any('Choi' in e or 'Samat' in e for e in peer_exec), \
            "Peer exec access must name Choi and/or Samat"

    def test_privacy_treatment_documented_both(self):
        block = get_stein_block()
        meta_priv = block['meta_item'].get('privacy_treatment', '').lower()
        peer_priv = block['samsung_google_item'].get('privacy_treatment', '').lower()
        assert 'zero privacy' in meta_priv or 'no privacy' in meta_priv or 'zero' in meta_priv, \
            f"Meta privacy treatment must document zero privacy mentions, got: {meta_priv[:80]}"
        assert 'no adversarial' in peer_priv, \
            f"Peer privacy treatment must note no adversarial framing, got: {peer_priv[:80]}"
        assert 'samat' in peer_priv, \
            "Peer privacy treatment must attribute the control line to Samat"

    def test_finding_bounds_mechanism_106(self):
        finding = get_stein_block().get('finding', '')
        assert '106' in finding, \
            "finding must name mechanism #106 as the unit being bounded"
        assert 'news-register' in finding or 'news/launch' in finding.replace('-', '/'), \
            f"finding must bound #106 to the news/launch register, got: {finding[:120]}"


# ===================================================================
# Test Class 3: Confounders
# ===================================================================
class TestConfounders:
    """The block must carry a ranked confounder list with required strengths."""

    def _conf(self):
        return get_stein_block().get('confounders', [])

    def test_confounder_count(self):
        assert len(self._conf()) >= 6, \
            f"need >=6 confounders, got {len(self._conf())}"

    def test_strong_genre_boundary(self):
        blob = ' '.join(self._conf())
        assert '[STRONG]' in blob and 'genre' in blob.lower(), \
            "confounders must include a STRONG genre boundary entry"
        assert '#578' in blob, \
            "genre confounder must cite the standing boundary series"

    def test_strong_product_class_asymmetry(self):
        blob = ' '.join(self._conf()).lower()
        assert 'product-class' in blob or 'product class' in blob, \
            "confounders must include the product-class (glasses vs headset) asymmetry"

    def test_moderate_exec_access_symmetry(self):
        blob = ' '.join(self._conf())
        assert '[MODERATE]' in blob, \
            "confounders must include MODERATE entries"
        assert 'symmetric' in blob.lower(), \
            "confounders must note symmetric executive access"

    def test_weak_entries(self):
        blob = ' '.join(self._conf())
        assert '[WEAK]' in blob, \
            "confounders must include WEAK entries"
        assert 'headline' in blob.lower(), \
            "WEAK confounders must include headline authorship"


# ===================================================================
# Test Class 4: Counterevidence
# ===================================================================
class TestCounterevidence:
    """Counterevidence must stress-test the constancy finding honestly."""

    def test_counterevidence_count(self):
        ce = get_stein_block().get('counterevidence', [])
        assert len(ce) >= 4, \
            f"need >=4 counterevidence entries, got {len(ce)}"

    def test_honest_caveats_counterevidence(self):
        blob = ' '.join(get_stein_block().get('counterevidence', [])).lower()
        assert 'puffery' in blob or 'caveat' in blob, \
            "counterevidence must address whether enthusiasm is captured puffery"

    def test_meta_quest_comparison_counterevidence(self):
        blob = ' '.join(get_stein_block().get('counterevidence', []))
        assert 'Quest 3' in blob or 'Meta Quest' in blob, \
            "counterevidence must note the XR2+ 'better than the Meta Quest 3' comparison"

    def test_apple_neutral_benchmark_counterevidence(self):
        blob = ' '.join(get_stein_block().get('counterevidence', [])).lower()
        assert 'apple' in blob and 'benchmark' in blob, \
            "counterevidence must note Apple Vision Pro as the neutral benchmark in both pieces"


# ===================================================================
# Test Class 5: Statistical Discipline
# ===================================================================
class TestStatisticalDiscipline:
    """The ILLUSTRATIVE scorer must carry explicit discipline markers."""

    def test_delta_is_near_zero(self):
        scorer = get_scorer()
        delta = scorer.get('delta')
        assert isinstance(delta, (int, float)), \
            f"delta must be numeric, got {type(delta)}"
        assert abs(delta) <= 0.1, \
            f"constancy delta must be within 0.10 of zero, got {delta}"

    def test_tones_in_band(self):
        scorer = get_scorer()
        assert 0.6 <= scorer.get('target_avg', 0) <= 0.75, \
            f"Meta tone must be in the enthusiastic band, got {scorer.get('target_avg')}"
        assert 0.6 <= scorer.get('peer_avg', 0) <= 0.75, \
            f"Peer tone must be in the enthusiastic band, got {scorer.get('peer_avg')}"

    def test_p_value_not_calculated(self):
        assert get_scorer().get('p_value') == 'NOT_CALCULATED', \
            "p_value must be NOT_CALCULATED per the Aug 28 2026 standing rule"

    def test_not_significant(self):
        assert get_scorer().get('is_significant') is False, \
            "is_significant must be false for n=1 vs n=1 illustrative scores"

    def test_correlation_not_causation(self):
        assert get_scorer().get('correlation_not_causation') is True, \
            "correlation_not_causation must be true"

    def test_delta_direction_names_constancy(self):
        direction = get_scorer().get('delta_direction', '').lower()
        assert 'constancy' in direction, \
            f"delta_direction must name register constancy, got: {direction[:80]}"

    def test_methodology_explicit(self):
        method = get_scorer().get('methodology', '')
        assert 'MANUAL ILLUSTRATIVE' in method, \
            "methodology must state MANUAL ILLUSTRATIVE"
        assert 'NOT an empirical measurement' in method, \
            "methodology must disclaim empirical measurement"


# ===================================================================
# Test Class 6: Incentive Context
# ===================================================================
class TestIncentiveContext:
    """The finding must not overclaim on the incentive thesis."""

    def test_incentive_context_present(self):
        ctx = get_stein_block().get('incentive_context', '')
        assert 'Ziff Davis' in ctx, \
            "incentive context must name CNET's owner Ziff Davis"
        assert 'Google' in ctx, \
            "incentive context must name the Google search-traffic dependency"
        assert 'Meta' in ctx, \
            "incentive context must name the (absent) Meta financial relationship"

    def test_no_overclaim_on_publication_thesis(self):
        ctx = get_stein_block().get('incentive_context', '').lower()
        assert 'not an exoneration' in ctx or 'does not exonerate' in ctx, \
            "incentive context must refuse to exonerate publication-level patterns"

    def test_cross_references_present(self):
        refs = get_stein_block().get('cross_references', [])
        blob = ' '.join(refs)
        assert '#106' in blob, \
            "cross-references must include mechanism #106"
        assert '#548' in blob, \
            "cross-references must include #548 (constancy parallel)"


# ===================================================================
# Test Class 7: Novelty and Rotation
# ===================================================================
class TestNoveltyAndRotation:
    """Iteration 588 must be novel and correctly rotated (587 A -> 588 B)."""

    def test_iteration_is_588_type_b(self):
        block = get_stein_block()
        assert block.get('iteration') == 588, \
            "iteration must be 588"
        assert block.get('type') == 'B', \
            "type must be B (Journalist Cross-Entity Tracking)"

    def test_novelty_first_dedicated_type_b_on_stein(self):
        novelty = get_stein_block().get('novelty', '')
        assert 'type_b_588' in novelty, \
            "Novelty must name the 588 block key"
        assert 'first dedicated type b block on scott stein' in novelty.lower(), \
            "Novelty must assert first dedicated Type B on Scott Stein"

    def test_novelty_distinguishes_prior_units(self):
        novelty = get_stein_block().get('novelty', '')
        assert '#106' in novelty, \
            "Novelty must distinguish from #106 (same journalist)"
        assert '#548' in novelty, \
            "Novelty must distinguish from #548 (constancy parallel)"
        assert '#578' in novelty, \
            "Novelty must distinguish from #578 (opposite verdict class)"
        assert '587 A -> 588 B' in novelty, \
            "Novelty must record the rotation 587 A -> 588 B"

    def test_block_key_unique_on_entry(self):
        data = load_journalists()
        for j in data.get('journalists', []):
            if j.get('name') == 'Scott Stein':
                keys = [k for k in j.get('competitor_coverage', {}).keys()
                        if '588' in str(k)]
                assert keys == [BLOCK_KEY], \
                    f"Exactly one 588 block must exist on Stein, got {keys}"

    def test_exactly_one_588_test_file(self):
        files = glob.glob(os.path.join(os.path.dirname(__file__),
                                       'test_type_b_588*.py'))
        assert len(files) == 1 and os.path.basename(files[0]) == TEST_FILE_NAME, \
            f"Exactly one 588 test file must exist, got {files}"
