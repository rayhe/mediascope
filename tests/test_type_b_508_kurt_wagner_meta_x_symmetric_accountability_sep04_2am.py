"""
Test Type B #508: Kurt Wagner (Bloomberg) Meta vs X Symmetric Accountability Framing

Type B: Journalist Cross-Entity Tracking — September 4, 2026 (02:00 PDT)

KEY FINDING: Wagner, Bloomberg's primary Meta/X beat reporter since 2019, applies
SYMMETRIC framing to Meta and X within the same publication: adversarial when the
news event is adversarial, executive-claim relay when the news event is business.
No entity-selective softening detected in the verified corpus.

Meta corpus (4 items):
- Mar 26 2026 "Meta, Google risk big tobacco-like fallout after addiction trial"
  (co-byline Alexandra S. Levine): puts Meta/Google in the same category as Big
  Tobacco and opioid makers over "products designed to be addictive"; the verdict
  is "the kind of black eye that often leads to an increase in government
  regulations." Full text verified via Bloomberg syndication.
- Mar 2026 "Meta Plans Deep Cuts to Metaverse Efforts": sourced accountability
  (budget cuts "as high as 30%", layoffs "as early as January").
- Oct 2025 "Meta Cutting Roughly 600 AI Jobs": straight business news.
- Jul 2026 Zuckerberg interview on Muse Spark 1.1 ("Zuckerberg Sets 'Aggressive'
  Price With Meta's Pay-to-Use AI"): granted-access claim relay ("pricing is going
  to be very aggressive and attractive", "state-of-the-art or very close to it").

X corpus (4 items):
- Mar 31 2025 "Musk's XAI Deal Offers an Unexpected Win for X Investors":
  investor-sympathetic business register ("unexpected win for X investors", $33B
  equity value). Headline + lede verified; full text paywalled (bounded).
- "Ex-Twitter Executives Sue Elon Musk for $128 Million in Severance Pay":
  adversarial accountability ("stiffing them on more than $128 million").
- "Battle for the Bird" (Feb 2024, book): deeply critical Musk passages
  ("darker, yet-to-be-defined motives", "employees' growing horror").
- "Elon Musk's X Is Testing 'Adult Content' Groups": neutral product news.

READING: framing tracks news GENRE, not entity — the softest items on both sides
are granted-access/deal reporting (Zuckerberg interview / xAI "win for investors")
and the hardest items on both sides are accountability events (addiction verdict /
severance suit, Musk book). Joins the falsification/boundary-condition family
(Type B #493 Fowler, #498 Swisher, #503 Preston): at Bloomberg, which holds no AI
content-licensing deal with any lab, the beat reporter shows journalist-level
consistency, constraining the financial-incentive theory to deal-holding
publications.

CONFOUNDERS (4): STRONG genre asymmetry; MODERATE co-byline on the flagship Meta
item (Levine); MODERATE one-year date gap between flagship items; WEAK
paywall-bounded X deal-piece evidence.

NEWSROOM UPDATE: Wagner promoted to Big Tech team leader (Jul 2026, announced by
Sarah Frier); parental leave from Aug 2026. Alexandra Levine expands to the Meta
beat alongside Riley Griffin — the continuity byline to watch.

Sources (all verified 2026-09-04):
- https://businessmirror.com.ph/2026/03/26/meta-google-risk-big-tobacco-like-fallout-after-addiction-trial/
- https://www.youtube.com/watch?v=oaTNCiTmASM
- https://pxlnv.com/linklog/meta-cuts-metaverse/
- https://muckrack.com/kurtwagner8/articles
- https://news.bloomberglaw.com/private-equity/musks-xai-deal-offers-an-unexpected-win-for-x-investors
- https://omny.fm/shows/bloomberg-businessweek/musk-s-xai-deal-offers-an-unexpected-win-for-x-inv
- https://muckrack.com/kurt-wagner-16/articles
- https://www.platformer.news/kurt-wagner-battle-for-the-bird-interview-zoe-schiffer-extremely-hardcore/
- https://www.citybiz.co/article/877466/bloomberg-promotes-kurt-wagner-to-lead-big-tech-coverage-team/
"""

import os
import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_wagner_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Kurt Wagner':
            return j.get('competitor_coverage', {}).get(
                'type_b_508_meta_x_symmetric_accountability', {})
    return {}


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 4+4 cross-entity corpus."""

    def test_block_exists(self):
        assert get_wagner_block(), \
            "type_b_508_meta_x_symmetric_accountability must exist on Wagner"

    def test_iteration_and_date(self):
        block = get_wagner_block()
        assert block.get('iteration') == 508, \
            f"iteration must be 508, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-04', \
            f"date must be 2026-09-04, got {block.get('date')}"

    def test_design_is_within_journalist(self):
        design = get_wagner_block().get('design', '').lower()
        assert 'within-journalist' in design and 'bloomberg' in design, \
            f"design must be within-journalist at Bloomberg, got: {design}"

    def test_meta_corpus_count(self):
        corpus = get_wagner_block().get('meta_corpus', [])
        assert len(corpus) >= 4, \
            f"Meta corpus must have >=4 items, got {len(corpus)}"

    def test_x_corpus_count(self):
        corpus = get_wagner_block().get('x_corpus', [])
        assert len(corpus) >= 4, \
            f"X corpus must have >=4 items, got {len(corpus)}"

    def test_every_item_has_source_url(self):
        block = get_wagner_block()
        for item in block['meta_corpus'] + block['x_corpus']:
            assert item.get('url', '').startswith('http'), \
                f"Every corpus item needs a source URL, missing on: {item.get('title')}"
            assert item.get('verification'), \
                f"Every corpus item needs a verification note: {item.get('title')}"

    def test_meta_flagship_is_addiction_trial_piece(self):
        corpus = get_wagner_block()['meta_corpus']
        assert any('big tobacco' in i.get('title', '').lower() for i in corpus), \
            "Meta corpus must include the Big Tobacco addiction-trial piece"
        piece = next(i for i in corpus if 'big tobacco' in i['title'].lower())
        assert piece.get('date') == '2026-03-26', \
            f"Addiction-trial piece date must be 2026-03-26, got {piece.get('date')}"
        assert 'Levine' in piece.get('byline', ''), \
            "Must record the Levine co-byline"

    def test_x_flagship_is_xai_deal_piece(self):
        corpus = get_wagner_block()['x_corpus']
        assert any('unexpected win' in i.get('title', '').lower() for i in corpus), \
            "X corpus must include the 'unexpected win for X investors' piece"
        piece = next(i for i in corpus if 'unexpected win' in i['title'].lower())
        assert piece.get('date') == '2025-03-31', \
            f"xAI-deal piece date must be 2025-03-31, got {piece.get('date')}"


# ===================================================================
# Test Class 2: Symmetric-Framing Finding
# ===================================================================
class TestSymmetricFramingFinding:
    """The finding must assert genre-driven symmetry with both registers named."""

    def test_finding_names_meta_adversarial_register(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'big tobacco' in finding, \
            "Finding must cite the Meta-side adversarial marker (Big Tobacco)"

    def test_finding_names_x_business_register(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'unexpected win' in finding, \
            "Finding must cite the X-side business marker (unexpected win)"

    def test_finding_names_x_adversarial_register(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'severance' in finding or 'battle for the bird' in finding, \
            "Finding must cite X-side adversarial evidence (severance suit or book)"

    def test_finding_asserts_genre_over_entity(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'genre' in finding, \
            "Finding must state framing tracks news genre, not entity"

    def test_finding_denies_entity_selective_softening(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'no entity-selective softening' in finding, \
            "Finding must explicitly record no entity-selective softening detected"

    def test_finding_joins_falsification_family(self):
        finding = get_wagner_block().get('finding', '')
        for marker in ('493', '498', '503'):
            assert marker in finding, \
                f"Finding must cross-reference falsification family (missing #{marker})"
        assert 'falsification' in finding.lower(), \
            "Finding must name the falsification/boundary-condition family"

    def test_finding_notes_bloomberg_has_no_ai_deal(self):
        finding = get_wagner_block().get('finding', '').lower()
        assert 'no ai content-licensing deal' in finding, \
            "Finding must note Bloomberg holds no AI content-licensing deal"


# ===================================================================
# Test Class 3: Confounders
# ===================================================================
class TestConfounders:
    """Four confounders with strengths must be recorded."""

    def test_confounder_count(self):
        confounders = get_wagner_block().get('confounders', [])
        assert len(confounders) >= 4, \
            f"Must record >=4 confounders, got {len(confounders)}"

    def test_genre_confounder_is_strong(self):
        confounders = get_wagner_block()['confounders']
        genre = next(c for c in confounders if 'genre' in c['factor'].lower())
        assert genre.get('strength') == 'STRONG', \
            "Genre asymmetry must be rated STRONG"

    def test_cobyline_confounder_present(self):
        confounders = get_wagner_block()['confounders']
        assert any('co-byline' in c['factor'].lower() for c in confounders), \
            "Must include the Levine co-byline confounder"

    def test_date_gap_confounder_present(self):
        confounders = get_wagner_block()['confounders']
        assert any('date gap' in c['factor'].lower() for c in confounders), \
            "Must include the date-gap confounder"

    def test_paywall_bound_confounder_present(self):
        confounders = get_wagner_block()['confounders']
        assert any('paywall' in c['factor'].lower() for c in confounders), \
            "Must include the paywall-bounded-evidence confounder"


# ===================================================================
# Test Class 4: Newsroom Update
# ===================================================================
class TestNewsroomUpdate:
    """The Jul 2026 promotion/leave/Levine update must be recorded."""

    def test_update_exists(self):
        assert get_wagner_block().get('newsroom_update_2026_07'), \
            "newsroom_update_2026_07 must exist"

    def test_promotion_recorded(self):
        update = get_wagner_block()['newsroom_update_2026_07']
        assert 'big tech team leader' in update.get('event', '').lower(), \
            "Must record the Big Tech team leader promotion"

    def test_parental_leave_recorded(self):
        update = get_wagner_block()['newsroom_update_2026_07']
        assert 'parental leave' in update.get('event', '').lower(), \
            "Must record the August 2026 parental leave"

    def test_levine_continuity_noted(self):
        update = get_wagner_block()['newsroom_update_2026_07']
        implication = update.get('implication', '')
        assert 'Levine' in implication and 'Meta' in implication, \
            "Must flag Levine as the Meta-beat continuity byline"

    def test_update_has_source(self):
        update = get_wagner_block()['newsroom_update_2026_07']
        assert update.get('url', '').startswith('http'), \
            "Newsroom update needs a source URL"
