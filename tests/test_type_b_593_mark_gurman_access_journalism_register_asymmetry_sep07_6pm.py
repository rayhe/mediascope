"""
Test Type B #593: Mark Gurman (Bloomberg) access-journalism register asymmetry -
Meta Ray-Ban Display review (Oct 2025, spec-critical) vs Apple N50 smart glasses
scoops (Apr-Jul 2026, insider-aspirational).

Type B: Journalist Cross-Entity Tracking - September 7, 2026 (18:00 PDT)

KEY FINDING: BOUNDARY/NULL PIN for the financial theory, not a gradient win.
Gurman renders the same hardware category (camera glasses) in two registers:
- Meta (Oct 2025 Ray-Ban Display review, via Techmeme relay): spec-critical.
  "good for uses like navigation and AI queries, the neural band is great, but
  the display has low resolution and the camera is 1080p (Mark Gurman/Bloomberg)".
  Praise is capability-anchored, caveats specification-anchored. Tone -0.15.
- Apple (Apr-Jul 2026 Power On scoops, via MacRumors/Slashdot/Road-to-VR relays):
  insider-aspirational. Four frame styles, acetate "more durable and luxurious"
  than standard plastic, "instantly recognizable as Apple" ("icon"), "many"
  colors (Apr 13 2026); Apple employees telling Bloomberg the strategy is to
  "outdo competitors by tightly integrating the glasses with the iPhone and
  offering a higher-end build" (Slashdot relay of the same report); Vision Air
  shelved to accelerate N50 glasses to "take on Ray-Ban Meta" (Jul 2026).
  Tones +0.45 / +0.35 / +0.35, avg +0.40.

The ILLUSTRATIVE delta is -0.55 (Meta -0.15 minus Apple +0.40), hand-scored,
n=1 vs n=3, p_value NOT_CALCULATED per the standing Aug 28 2026 rule.

WHY IT MATTERS: Bloomberg LP is Terminal-revenue-driven with zero documented
AI content-licensing deals with Meta, Apple, or OpenAI (in-corpus mechanism
#85, Chris Welch career-migration block). The financial-deal gradient therefore
predicts a NULL register gap for Gurman. The observed gap is better explained
by ACCESS economics: Gurman's Apple scoops depend on anonymous Apple employees
(access preservation; in-corpus the-verge.yaml notes Apple design scoops via
Gurman/Bloomberg drive high-engagement traffic with low legal risk), while his
Meta hardware coverage is reviewable-product journalism with no access to
preserve. The gap is access-explained, not money-explained. This bounds the
financial theory and joins the reporter-level falsification/alternative-driver
family with #538 (Metz litigation-adversary symmetry) and the genre-boundary
family with #588 (Stein hands-on constancy).

Meta corpus (1 item, Bloomberg review via Techmeme relay, Oct 9 2025):
- "Meta Ray-Ban Display review: good for uses like navigation and AI queries,
  the neural band is great, but the display has low resolution and the camera
  is 1080p (Mark Gurman/Bloomberg)". http://www.techmeme.com/251009/p36

Apple corpus (3 items, Power On scoops via secondary relays):
- "Apple Testing Four Smart Glasses Styles Made of High-End Materials"
  (MacRumors, Apr 13 2026, relay of Gurman Power On). Acetate "more durable and
  luxurious" than standard plastic; four styles; "many" colors; "instantly
  recognizable as Apple". https://www.macrumors.com/2026/04/13/apple-smart-glasses-four-styles/
- "Apple AI Glasses Will Rival Meta's With Several Styles, Oval Cameras"
  (Slashdot, Apr 13 2026, relay of same Gurman report). Apple employees:
  "outdo competitors by tightly integrating the glasses with the iPhone and
  offering a higher-end build". https://apple.slashdot.org/story/26/04/13/215252/apple-ai-glasses-will-rival-metas-with-several-styles-oval-cameras
- "Apple Reportedly Shelves Cheaper & Lighter Vision Pro for Smart Glasses to
  Rival Meta" (Road to VR, ~Jul 2026, relay of Gurman Power On). Vision Air on
  hold; N50 accelerated to take on Ray-Ban Meta / Ray-Ban Display ($800).
  https://roadtovr.com/apple-vision-pro-smart-glasses-meta-report/

CONFOUNDERS (6): STRONG genre asymmetry (shipped-product review vs unreleased-
product scoop - the standing Type B genre boundary); STRONG product reality
(Meta Display shipped with reviewable specs; N50 has shipped nothing);
MODERATE access-preservation incentive (stated as the driver, partly circular);
MODERATE evidence tier (all secondary relays, Bloomberg originals paywalled/
newsletter); MODERATE timing skew (Oct 2025 vs Apr-Jul 2026); WEAK "better
made"/"outdo competitors" lines are employee-attributed, not Gurman's voice.

COUNTEREVIDENCE (4): Gurman's Meta review was net-positive on substance
(neural band "great"); his Apple scoops carried one real insider concern (AI
failings); n=1 vs n=3 hand-scoring noise; Bloomberg's financial independence
makes the null structural, not comparative.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (article level,
-1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical significance
test on hand-scored items would manufacture precision that does not exist.
is_significant: false. correlation_not_causation: true.

Sources (all verified 2026-09-07): URLs verbatim from Full-URL listings in the
two browser.search query sets this run. No zero-coverage claims per
iteration-492. No canonical URLs constructed. Bloomberg originals paywalled or
newsletter-only; characterizations are relay-bounded and labeled as such.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

BLOCK_KEY = 'type_b_593_mark_gurman_access_journalism_register_asymmetry'

TEST_FILE_NAME = 'test_type_b_593_mark_gurman_access_journalism_register_asymmetry_sep07_6pm.py'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_gurman_block(data=None):
    data = data or load_journalists()
    for j in data.get('journalists', []):
        if j.get('name') == 'Mark Gurman':
            return j.get('competitor_coverage', {}).get(BLOCK_KEY, {})
    return {}


def get_scorer(block=None):
    block = block if block is not None else get_gurman_block()
    return block.get('asymmetry_scorer_result_illustrative', {})


# ===================================================================
# Test Class 1: Corpus Documented on Both Entities
# ===================================================================
class TestCorpusDocumented:
    """The profile block must carry a verified 1-vs-3 within-writer corpus."""

    def test_block_exists(self):
        assert get_gurman_block(), \
            f"{BLOCK_KEY} must exist on Mark Gurman"

    def test_iteration_and_date(self):
        block = get_gurman_block()
        assert block.get('iteration') == 593, \
            f"iteration must be 593, got {block.get('iteration')}"
        assert block.get('date') == '2026-09-07', \
            f"date must be 2026-09-07, got {block.get('date')}"

    def test_design_is_within_journalist(self):
        design = get_gurman_block().get('design', '').lower()
        assert 'within-journalist' in design, \
            f"design must be within-journalist, got: {design}"
        assert 'gurman' in design or 'bloomberg' in design, \
            "design must name Gurman/Bloomberg"

    def test_meta_item_has_verbatim_url_and_tone(self):
        items = get_gurman_block().get('meta_corpus', [])
        assert len(items) == 1, \
            f"Meta corpus must have exactly 1 item, got {len(items)}"
        item = items[0]
        assert 'Ray-Ban Display' in item.get('title', ''), \
            "Meta item must be the Ray-Ban Display review"
        assert item.get('source_url') == 'http://www.techmeme.com/251009/p36', \
            f"Meta source URL must be the verbatim Techmeme URL, got {item.get('source_url')}"
        assert item.get('tone') == -0.15, \
            f"Meta item tone must be -0.15, got {item.get('tone')}"
        assert item.get('register') == 'spec-critical', \
            "Meta item register must be spec-critical"

    def test_apple_items_have_verbatim_urls_and_tones(self):
        items = get_gurman_block().get('apple_corpus', [])
        assert len(items) == 3, \
            f"Apple corpus must have exactly 3 items, got {len(items)}"
        urls = [i.get('source_url') for i in items]
        assert urls[0] == 'https://www.macrumors.com/2026/04/13/apple-smart-glasses-four-styles/', \
            f"Apple item 1 URL mismatch: {urls[0]}"
        assert urls[1] == 'https://apple.slashdot.org/story/26/04/13/215252/apple-ai-glasses-will-rival-metas-with-several-styles-oval-cameras', \
            f"Apple item 2 URL mismatch: {urls[1]}"
        assert urls[2] == 'https://roadtovr.com/apple-vision-pro-smart-glasses-meta-report/', \
            f"Apple item 3 URL mismatch: {urls[2]}"
        tones = [i.get('tone') for i in items]
        assert tones == [0.45, 0.35, 0.35], \
            f"Apple tones must be [0.45, 0.35, 0.35], got {tones}"
        assert all(i.get('register') == 'insider-aspirational' for i in items), \
            "All Apple items must carry the insider-aspirational register"

    def test_all_items_bloomberg_byline_or_relay(self):
        block = get_gurman_block()
        meta = block['meta_corpus'][0]
        assert 'Gurman' in meta.get('notes', ''), \
            "Meta item notes must attribute Gurman"
        for item in block['apple_corpus']:
            assert 'Gurman' in item.get('notes', '') or 'Power On' in item.get('notes', ''), \
                f"Apple item must attribute Gurman/Power On: {item.get('title')}"


# ===================================================================
# Test Class 2: Register Asymmetry Finding (Boundary/Null Pin)
# ===================================================================
class TestRegisterAsymmetryFinding:
    """The block must document the boundary/null-pin verdict with the numbers."""

    def test_verdict_is_boundary_null_pin(self):
        verdict = get_gurman_block().get('verdict', '').lower()
        assert 'boundary/null' in verdict or 'boundary' in verdict, \
            "Verdict must name the boundary/null-pin class"
        assert 'access-explained' in verdict, \
            "Verdict must state the gap is access-explained, not money-explained"

    def test_delta_math_is_consistent(self):
        scorer = get_scorer()
        assert scorer.get('delta') == -0.55, \
            f"delta must be -0.55, got {scorer.get('delta')}"
        calc = scorer['target_avg'] - scorer['peer_avg']
        assert abs(scorer['delta'] - calc) < 1e-9, \
            f"delta must equal target_avg - peer_avg = {calc}"
        assert scorer['target_scores'] == [-0.15], \
            "target scores must be [-0.15]"
        assert scorer['peer_scores'] == [0.45, 0.35, 0.35], \
            "peer scores must be [0.45, 0.35, 0.35]"

    def test_falsification_family_membership(self):
        verdict = get_gurman_block().get('verdict', '')
        assert '#538' in verdict, \
            "Verdict must place the unit with #538 (Metz falsification family)"
        assert '#588' in verdict, \
            "Verdict must place the unit with #588 (Stein genre-boundary family)"

    def test_financial_gradient_null_prediction(self):
        hypothesis = get_gurman_block().get('hypothesis', '')
        assert 'NULL' in hypothesis, \
            "Hypothesis must state the deal-gradient prediction is NULL"
        fin = get_gurman_block().get('financial_context', '')
        assert 'Terminal' in fin, \
            "financial_context must name Bloomberg Terminal revenue"
        assert 'no documented' in fin.lower(), \
            "financial_context must document no AI content-licensing deals"


# ===================================================================
# Test Class 3: Confounders Ranked
# ===================================================================
class TestConfounders:
    """The six ranked confounders must be present and ordered."""

    def test_six_confounders_present(self):
        confounders = get_gurman_block().get('confounders', [])
        assert len(confounders) == 6, \
            f"must have 6 confounders, got {len(confounders)}"

    def test_strength_ranking(self):
        confounders = get_gurman_block().get('confounders', [])
        strong = [c for c in confounders if c.startswith('[STRONG]')]
        moderate = [c for c in confounders if c.startswith('[MODERATE]')]
        weak = [c for c in confounders if c.startswith('[WEAK]')]
        assert len(strong) == 2, \
            f"must have 2 STRONG confounders, got {len(strong)}"
        assert len(moderate) == 3, \
            f"must have 3 MODERATE confounders, got {len(moderate)}"
        assert len(weak) == 1, \
            f"must have 1 WEAK confounder, got {len(weak)}"

    def test_genre_boundary_named_as_strong(self):
        confounders = get_gurman_block().get('confounders', [])
        strong_text = ' '.join(c for c in confounders if c.startswith('[STRONG]'))
        assert 'genre' in strong_text.lower(), \
            "A STRONG confound must be the review-vs-scoop genre asymmetry"
        assert '#588' in strong_text, \
            "Genre confound must cite the standing Type B genre boundary (#588)"


# ===================================================================
# Test Class 4: Counterevidence
# ===================================================================
class TestCounterevidence:
    """Four counterevidence items must be present."""

    def test_four_counterevidence(self):
        ce = get_gurman_block().get('counterevidence', [])
        assert len(ce) == 4, \
            f"must have 4 counterevidence items, got {len(ce)}"

    def test_counterevidence_covers_both_sides(self):
        ce_text = ' '.join(get_gurman_block().get('counterevidence', [])).lower()
        assert 'net-positive' in ce_text or 'neural band' in ce_text, \
            "Counterevidence must note Gurman's Meta review was net-positive"
        assert 'ai failings' in ce_text, \
            "Counterevidence must note the Apple insider concern line"


# ===================================================================
# Test Class 5: Statistical Discipline
# ===================================================================
class TestStatisticalDiscipline:
    """The Aug 28 2026 standing rule: no empirical claims from hand scores."""

    def test_p_value_not_calculated(self):
        scorer = get_scorer()
        assert scorer.get('p_value') == 'NOT_CALCULATED', \
            "p_value must be NOT_CALCULATED"
        assert scorer.get('is_significant') is False, \
            "is_significant must be false"
        assert scorer.get('correlation_not_causation') is True, \
            "correlation_not_causation must be true"

    def test_methodology_states_manual_illustrative(self):
        method = get_scorer().get('methodology', '').lower()
        assert 'manual illustrative' in method, \
            "methodology must state MANUAL ILLUSTRATIVE tones"
        assert 'not an empirical measurement' in method, \
            "methodology must disclaim empirical measurement"

    def test_delta_direction_label_present(self):
        direction = get_scorer().get('delta_direction', '').lower()
        assert 'access' in direction, \
            "delta_direction must attribute the gap to access, not deals"
        assert 'null' in direction, \
            "delta_direction must note the NULL deal-gradient prediction"


# ===================================================================
# Test Class 6: Financial Context and Cross-References
# ===================================================================
class TestIncentiveContext:
    """Bloomberg's financial-null and the access-economics driver must be documented."""

    def test_cross_refs(self):
        refs = get_gurman_block().get('cross_refs', [])
        ref_text = ' '.join(refs)
        for tag in ('#85', '#471', '#538', '#588', '#421'):
            assert tag in ref_text, \
                f"cross_refs must include {tag}"

    def test_access_journalism_incentive_noted(self):
        fin = get_gurman_block().get('financial_context', '')
        assert 'access journalism' in fin.lower(), \
            "financial_context must name access journalism as the driver class"
        assert 'legal risk' in fin.lower() or 'traffic' in fin.lower(), \
            "financial_context must cite the traffic/low-legal-risk incentive"

    def test_research_method(self):
        method = get_gurman_block().get('research_method', '')
        assert '2 browser.search' in method, \
            "research_method must record the 2 query sets"
        assert 'iteration-492' in method, \
            "research_method must cite the no-zero-coverage rule (iteration-492)"
        assert 'verbatim' in method.lower(), \
            "research_method must state URLs were verbatim from Full-URL listings"


# ===================================================================
# Test Class 7: Novelty and Rotation
# ===================================================================
class TestNoveltyAndRotation:
    """Iteration 593 must be novel and correctly rotated (592 A -> 593 B)."""

    def test_iteration_is_593_type_b(self):
        block = get_gurman_block()
        assert block.get('iteration') == 593, \
            "iteration must be 593"
        assert block.get('type') == 'B', \
            "type must be B (Journalist Cross-Entity Tracking)"

    def test_novelty_first_dedicated_type_b_on_gurman(self):
        novelty = get_gurman_block().get('novelty', '')
        assert 'type_b_593' in novelty, \
            "Novelty must name the 593 block key"
        assert 'first dedicated type b' in novelty.lower() and 'gurman' in novelty.lower(), \
            "Novelty must assert first dedicated Type B on Mark Gurman"

    def test_novelty_distinguishes_prior_units(self):
        novelty = get_gurman_block().get('novelty', '')
        assert '#85' in novelty, \
            "Novelty must distinguish from #85 (Bloomberg financial-null source)"
        assert '#538' in novelty, \
            "Novelty must distinguish from #538 (falsification parallel)"
        assert '592 A -> 593 B' in novelty, \
            "Novelty must record the rotation 592 A -> 593 B"

    def test_block_key_unique_on_entry(self):
        data = load_journalists()
        for j in data.get('journalists', []):
            if j.get('name') == 'Mark Gurman':
                keys = [k for k in j.get('competitor_coverage', {}).keys()
                        if '593' in str(k)]
                assert keys == [BLOCK_KEY], \
                    f"Exactly one 593 block must exist on Gurman, got {keys}"

    def test_exactly_one_593_test_file(self):
        files = glob.glob(os.path.join(os.path.dirname(__file__),
                                       'test_type_b_593*.py'))
        assert len(files) == 1 and os.path.basename(files[0]) == TEST_FILE_NAME, \
            f"Exactly one 593 test file must exist, got {files}"


# ===================================================================
# Test Class 8: Rotation Cycle Guard 593 (anchor patched in followup)
# Deselected pre-commit per the #565 followup convention.
# ===================================================================
class TestRotationCycleGuard593:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type B #593 followup: ...") and doc-sync commits interleave
    # between mains since the #572/#573/#574 convention change; the naive
    # newest-5 filter broke on them. The colon immediately after the iteration
    # number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard593.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard593.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#593", "B"),
            ("#592", "A"),
            ("#591", "E"),
            ("#590", "D"),
            ("#589", "C"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # B->A is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: B,A,E,D,C (the rotation
        # runs backward in newest-first order). (order[a] - order[b]) % 5 == 1
        # steps one position backward from the newer commit a to the older
        # commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_main_subjects()
        nums = [re.search(r"#(\d+):", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, f"duplicate iteration in window: {nums}"
