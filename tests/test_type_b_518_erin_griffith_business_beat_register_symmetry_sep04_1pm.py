"""
Test Type B #518: Erin Griffith (NYT) Meta vs OpenAI/Anthropic Business-Beat Register Symmetry

Type B: Journalist Cross-Entity Tracking - September 4, 2026 (13:00 PDT)

KEY FINDING: COMPANY-AGNOSTIC COUNTEREXAMPLE, heavily bounded, not causal
evidence. Erin Griffith, NYT startups/VC reporter (Fortune -> Wired -> NYT
migration; NYT-era since 2018-08), covers Meta and OpenAI/Anthropic in the
same finance-native business register - funding rounds, investor returns,
deal geopolitics. Her OpenAI/Anthropic coverage is investor-positive, and
her Meta coverage is geopolitics-framed; no detectable cross-entity register
split. The deal-incentive softening theory predicts nothing here (NYT has no
AI licensing deal) and observes nothing here. The lawsuit-incentive hardening
theory ALSO fails on this evidence: NYT is actively suing OpenAI for
copyright infringement, which predicts harder OpenAI coverage, yet her
OpenAI coverage is celebratory of investor wins. Beat genre dominates.

Meta corpus (2 items, near-neutral geopolitics/business register):
- Apr 30 2026 "The Split Between China and Silicon Valley Just Got Wider"
  (solo Griffith): Beijing demanded Meta unwind its $2B Manus acquisition;
  "Beijing's insistence that Meta unwind its deal with a Chinese A.I.
  start-up escalates the geopolitical fight over advanced tech." Meta is
  positioned as caught in a geopolitical crossfire, not as the wrongdoer
  (tone +0.05).
- Corpus-depth note: Meta appears in her 2026 corpus primarily as the
  $2B Manus acquirer; no second deep standalone Meta byline found in the
  Muck Rack 2026 window (tone 0.0).

OpenAI/Anthropic corpus (2 items, investor-positive business register):
- Sep 3 2026 "Silicon Valley's Big Money Is About to Get a Lot Bigger"
  (solo Griffith): PitchBook data, at least 95 investors backed both
  Anthropic and OpenAI ahead of IPOs; "Investing in the big AI companies
  is looking more like passive index fund investing (where access is the
  challenge!) than old-school VC" (tone +0.35).
- Apr 2026 "A.I. Companies Shatter Fund-Raising Records, as Boom
  Accelerates" (solo Griffith): OpenAI, Anthropic, Waymo with a $297B Q1
  2026 haul per Crunchbase; boom-acceleration framing (tone +0.25).

CONFOUNDERS (5): STRONG beat-genre dominance (VC/business reporter; the
funding-deal register structurally favors warm tones regardless of entity);
STRONG event asymmetry (geopolitical demand story vs funding/IPO windfall
stories - the news pegs differ in valence); MODERATE thin Meta corpus
(1-deep-plus-mention vs 2-deep); MODERATE scored-set byline balance (both
sides solo; earlier co-bylined OpenAI items excluded); WEAK URL provenance
(mirror/LinkedIn rather than canonical NYT URLs).

COUNTEREVIDENCE (3): NYT's active OpenAI copyright suit predicts harder
OpenAI coverage, yet observed coverage is investor-positive - cuts against
both deal-softening AND lawsuit-hardening theories; her 2017 Wired piece
"The Other Tech Bubble" proves adversarial tech-business framing is within
her capability, so the warm register is a beat choice; Guardian #517 shows
deal-partner coverage CAN carry register asymmetry - Griffith shows it need
not, so any general theory must condition on beat genre.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level,
n=2 vs n=2, -1..+1 scale; delta +0.275 means the OpenAI/Anthropic side
scored warmer - opposite the direction a deal-softening prediction would
imply). p_value deliberately NOT_CALCULATED - a mechanical significance
test on two hand-scored items per side would manufacture precision that
does not exist. is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-04):
- https://www.japantimes.co.jp/business/2026/04/30/tech/china-silicon-valley-split-wider/
- https://www.linkedin.com/posts/eringriffith_silicon-valleys-big-money-is-about-to-get-activity-7501320526422949888-tE8v
- https://muckrack.com/eringriffith/articles
- https://biztoc.com/x/0ad99294e781de3f
"""

import os

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')

BLOCK_KEY = 'type_b_518_erin_griffith_meta_openai_anthropic_business_beat_register_symmetry'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_griffith_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Erin Griffith':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified cross-entity corpus."""

    def test_block_exists(self):
        assert get_griffith_block(), \
            f"{BLOCK_KEY} must exist on Erin Griffith"

    def test_iteration_and_date(self):
        block = get_griffith_block()
        assert block.get('iteration') == 518, \
            f"iteration must be 518, got {block.get('iteration')}"
        assert block.get('iteration_type') == 'B', \
            f"iteration_type must be 'B', got {block.get('iteration_type')}"
        assert block.get('date') == '2026-09-04', \
            f"date must be 2026-09-04, got {block.get('date')}"

    def test_publication_and_beat(self):
        block = get_griffith_block()
        assert block.get('publication') == 'nytimes', \
            f"publication must be nytimes, got {block.get('publication')}"
        assert 'venture capital' in block.get('beat', ''), \
            f"beat must name venture capital, got {block.get('beat')}"

    def test_meta_corpus_count(self):
        corpus = get_griffith_block().get('meta_corpus', [])
        assert len(corpus) == 2, \
            f"Meta corpus must have exactly 2 items, got {len(corpus)}"

    def test_openai_anthropic_corpus_count(self):
        corpus = get_griffith_block().get('openai_anthropic_corpus', [])
        assert len(corpus) == 2, \
            f"OpenAI/Anthropic corpus must have exactly 2 items, got {len(corpus)}"

    def test_every_item_has_source_url_and_tone(self):
        block = get_griffith_block()
        for item in block['meta_corpus'] + block['openai_anthropic_corpus']:
            assert isinstance(item, dict), \
                f"corpus item must be a dict, got {type(item)}: {item}"
            assert item.get('url', '').startswith('http'), \
                f"Every corpus item needs a source URL, missing on: {item.get('title')}"
            assert isinstance(item.get('tone'), (int, float)) and -1 <= item['tone'] <= 1, \
                f"Tone must be a number in [-1, 1]: {item.get('title')}"
            assert item.get('byline'), \
                f"Every corpus item must record byline status: {item.get('title')}"

    def test_meta_flagship_is_manus_piece(self):
        corpus = get_griffith_block()['meta_corpus']
        assert any('split between china and silicon valley' in i.get('title', '').lower()
                   for i in corpus), \
            "Meta corpus must include the China/Silicon Valley Manus piece"
        piece = next(i for i in corpus
                     if 'split between china and silicon valley' in i['title'].lower())
        assert piece.get('date') == '2026-04-30', \
            f"Manus piece date must be 2026-04-30, got {piece.get('date')}"
        assert 'solo' in piece.get('byline', '').lower(), \
            "Must record the solo Griffith byline on the Manus piece"
        assert 'Manus' in piece.get('summary', ''), \
            "Manus summary must name the acquisition"

    def test_meta_manus_quotes_present(self):
        corpus = get_griffith_block()['meta_corpus']
        piece = next(i for i in corpus
                     if 'split between china and silicon valley' in i['title'].lower())
        quotes = ' '.join(piece.get('quotes', []))
        assert 'unwind its deal' in quotes, \
            "Manus piece must carry the Beijing-unwind quote"
        assert 'Meta had agreed to acquire Manus' in quotes, \
            "Manus piece must carry the acquisition quote"

    def test_openai_flagship_is_big_money_piece(self):
        corpus = get_griffith_block()['openai_anthropic_corpus']
        assert any('big money' in i.get('title', '').lower() for i in corpus), \
            "OpenAI/Anthropic corpus must include the Big Money piece"
        piece = next(i for i in corpus if 'big money' in i['title'].lower())
        assert piece.get('date') == '2026-09-03', \
            f"Big Money piece date must be 2026-09-03, got {piece.get('date')}"
        quotes = ' '.join(piece.get('quotes', []))
        assert '95' in piece.get('summary', '') or '95 investors' in quotes or \
            '95 investors' in piece.get('summary', ''), \
            "Big Money piece must cite the 95-investor PitchBook figure"

    def test_openai_fundraising_records_piece(self):
        corpus = get_griffith_block()['openai_anthropic_corpus']
        assert any('fund-raising records' in i.get('title', '').lower() for i in corpus), \
            "OpenAI/Anthropic corpus must include the fund-raising records piece"
        piece = next(i for i in corpus if 'fund-raising records' in i['title'].lower())
        assert '$297 billion' in piece.get('summary', ''), \
            "Fund-raising piece must cite the $297B Q1 figure"


# ===================================================================
# Test Class 2: Register Symmetry Finding
# ===================================================================
class TestRegisterSymmetryFinding:
    """The finding must state the company-agnostic counterexample and deny causality."""

    def test_finding_names_counterexample(self):
        finding = get_griffith_block().get('finding', '')
        assert 'COUNTEREXAMPLE' in finding, \
            "Finding must name the company-agnostic counterexample"

    def test_finding_notes_same_register(self):
        finding = get_griffith_block().get('finding', '').lower()
        assert 'business register' in finding or 'finance-native' in finding, \
            "Finding must name the shared business/finance-native register"

    def test_finding_denies_causal_claim(self):
        finding = get_griffith_block().get('finding', '')
        assert 'heavily bounded' in finding.lower(), \
            "Finding must carry the heavily-bounded qualifier"
        block = get_griffith_block()
        assert block['statistical_discipline']['correlation_not_causation'] is True, \
            "correlation_not_causation must be True"

    def test_finding_names_both_failed_theories(self):
        finding = get_griffith_block().get('finding', '').lower()
        assert 'lawsuit' in finding, \
            "Finding must name the lawsuit-incentive hardening theory"
        assert 'no ai licensing deal' in finding or 'no\nai licensing deal' in finding or \
            'ai licensing deal' in finding, \
            "Finding must note NYT has no AI licensing deal"

    def test_temporal_bound_recorded(self):
        bound = get_griffith_block().get('temporal_bound', '')
        assert '2018-08' in bound, \
            f"Temporal bound must anchor the NYT era at 2018-08, got: {bound}"


# ===================================================================
# Test Class 3: Confounders Ranked
# ===================================================================
class TestConfounders:
    """Confounders must be ranked with the genre confounder strongest."""

    def test_confounder_tiers_exist(self):
        conf = get_griffith_block().get('confounders_ranked', {})
        assert set(conf.keys()) == {'strong', 'moderate', 'weak'}, \
            f"Confounders must have strong/moderate/weak tiers, got {list(conf.keys())}"

    def test_confounder_count(self):
        conf = get_griffith_block().get('confounders_ranked', {})
        total = sum(len(conf[t]) for t in conf)
        assert total == 5, \
            f"Must record exactly 5 confounders, got {total}"

    def test_genre_confounder_is_strong(self):
        strong = ' '.join(get_griffith_block()['confounders_ranked']['strong']).lower()
        assert 'beat-genre' in strong or 'genre' in strong, \
            "A strong confounder must name beat-genre dominance"

    def test_event_asymmetry_confounder_is_strong(self):
        strong = ' '.join(get_griffith_block()['confounders_ranked']['strong']).lower()
        assert 'valence' in strong or 'event asymmetry' in strong, \
            "A strong confounder must name the event-valence asymmetry"

    def test_thin_meta_corpus_confounder_present(self):
        moderate = ' '.join(get_griffith_block()['confounders_ranked']['moderate']).lower()
        assert 'thin meta corpus' in moderate, \
            "Moderate tier must record the thin Meta corpus limit"


# ===================================================================
# Test Class 4: Counter-evidence
# ===================================================================
class TestCounterevidence:
    """Counter-evidence must include the lawsuit-theory failure."""

    def test_counterevidence_count(self):
        ce = get_griffith_block().get('counter_evidence', [])
        assert len(ce) == 3, \
            f"Must record exactly 3 counter-evidence items, got {len(ce)}"

    def test_lawsuit_theory_failure_present(self):
        ce = ' '.join(get_griffith_block()['counter_evidence']).lower()
        assert 'suing openai' in ce or 'copyright suit' in ce, \
            "Counter-evidence must name NYT suing OpenAI"

    def test_capability_counterevidence_present(self):
        ce = ' '.join(get_griffith_block()['counter_evidence'])
        assert 'The Other Tech Bubble' in ce, \
            "Counter-evidence must cite her adversarial Wired piece as capability proof"

    def test_517_boundary_condition_present(self):
        ce = ' '.join(get_griffith_block()['counter_evidence'])
        assert '#517' in ce and 'genre' in ce.lower(), \
            "Counter-evidence must set the #517 boundary condition (asymmetry can exist; genre conditions it)"


# ===================================================================
# Test Class 5: Statistical Discipline
# ===================================================================
class TestStatisticalDiscipline:
    """Manual illustrative tones only; no manufactured precision."""

    def test_p_value_not_calculated(self):
        sd = get_griffith_block()['statistical_discipline']
        assert sd['p_value'] == 'NOT_CALCULATED', \
            f"p_value must be NOT_CALCULATED, got {sd['p_value']}"
        assert sd['is_significant'] is False, \
            "is_significant must be False"

    def test_delta_math(self):
        tones = get_griffith_block()['manual_illustrative_tones']
        assert tones['meta'] == [0.05, 0.0], \
            f"meta tones must be [0.05, 0.0], got {tones['meta']}"
        assert tones['openai_anthropic'] == [0.35, 0.25], \
            f"openai_anthropic tones must be [0.35, 0.25], got {tones['openai_anthropic']}"
        expected_delta = round(sum(tones['openai_anthropic']) / 2 -
                               sum(tones['meta']) / 2, 3)
        assert tones['delta'] == expected_delta == 0.275, \
            f"delta must be 0.275, got {tones['delta']}"
        assert tones['meta_avg'] == 0.025 and tones['openai_anthropic_avg'] == 0.3, \
            "Averages must match the tone lists"

    def test_delta_direction_noted(self):
        note = get_griffith_block()['manual_illustrative_tones']['note']
        assert 'MANUAL ILLUSTRATIVE' in note and 'deal-softening' in note, \
            "Tone note must flag manual illustrative status and the anti-prediction direction"

    def test_n_is_2_vs_2(self):
        note = get_griffith_block()['manual_illustrative_tones']['note']
        assert 'n=2 vs n=2' in note, \
            "Tone note must state the sample size"

    def test_no_manufactured_precision_note(self):
        note = get_griffith_block()['statistical_discipline']['note']
        assert 'manufacture precision' in note, \
            "Statistical discipline note must explain why p is not calculated"


# ===================================================================
# Test Class 6: YAML Safety and Novelty
# ===================================================================
class TestYamlSafetyAndNovelty:
    """Silent-mangle guards (per #507) and first-unit novelty."""

    def test_single_competitor_coverage_key(self):
        data = load_journalists()
        for j in data.get('journalists', []):
            if j.get('name') == 'Erin Griffith':
                keys = list(j.get('competitor_coverage', {}).keys())
                assert keys == [BLOCK_KEY], \
                    f"Griffith must have exactly this one competitor_coverage key, got {keys}"

    def test_no_null_or_mangled_leaves(self):
        block = get_griffith_block()

        def walk(x, path='block'):
            if isinstance(x, dict):
                for k, v in x.items():
                    assert isinstance(k, str), f"non-str key at {path}"
                    walk(v, f"{path}.{k}")
            elif isinstance(x, list):
                assert len(x) > 0, f"empty list at {path}"
                for i, v in enumerate(x):
                    walk(v, f"{path}[{i}]")
            else:
                assert x is not None, f"NULL leaf at {path} - silent # mangling?"
                assert isinstance(x, (str, int, float, bool)), \
                    f"unexpected leaf type {type(x)} at {path}"

        walk(block)

    def test_ascii_only_strings(self):
        block = get_griffith_block()

        def walk(x):
            if isinstance(x, dict):
                for v in x.values():
                    walk(v)
            elif isinstance(x, list):
                for v in x:
                    walk(v)
            elif isinstance(x, str):
                x.encode('ascii')

        walk(block)  # raises UnicodeEncodeError on non-ASCII

    def test_novelty_statement(self):
        novelty = get_griffith_block().get('novelty', '')
        assert 'First dedicated Type B on Erin Griffith' in novelty, \
            "Novelty must claim the first dedicated Type B on Griffith"
        assert 'test_type_b_518' in novelty, \
            "Novelty must reference the 518 file-number check"

    def test_research_method_recorded(self):
        method = get_griffith_block().get('research_method', '')
        assert 'browser.search' in method and 'browser.open' in method, \
            "Research method must name the tools used"
        assert 'no canonical URLs constructed' in method, \
            "Research method must state the URL-verbatim rule"
