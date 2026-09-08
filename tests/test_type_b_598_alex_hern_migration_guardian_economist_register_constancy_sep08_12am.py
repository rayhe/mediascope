"""
Test Type B #598: Alex Hern institutional-migration register constancy -
Guardian UK technology editor (~2013-Sep 2024) to Economist AI writer
(~Oct 2024+). Adversarial accountability register toward Meta AND OpenAI
survives the institution change.

Type B: Journalist Cross-Entity Tracking - September 8, 2026 (00:00 PDT)

KEY FINDING: register CONSTANCY across a journalist-level institutional
migration, a control for the financial theory. Guardian-era Hern (byline-
attributed via Techmeme/Mediagazer relays): 2019 Meta fact-checking-
guidelines scoop ("some fact checkers say they learned about the change
only from Zuckerberg's testimony", tone -0.55); 2023 Meta WhatsApp Online
Safety Bill refusal ("would refuse to comply with the UK's Online Safety
Bill requirements to remove end-to-end encryption", tone -0.45); Guardian
Today in Focus metaverse episode calling the pitch "the impossibility of
it" plus "the fear of the fact that Facebook relies on other people's
platforms" (tone -0.55). Guardian-era Meta avg -0.5167 (n=3).
Economist-era Hern (broadcast/podcast tier): Babbage "OpenAI's alarming
escape" (Jul 29 2026) framing OpenAI's model breakout as "the first ever
fully autonomous AI hack" (tone -0.55); BBC Media Show (Sep 2026) outlining
implications of "Meta reducing its investment in virtual-reality projects"
(tone -0.35); Times Radio Moltbook segment weighing "the actual threat AI
only social media platforms like Moltbook pose to the future of society"
(tone -0.30). Economist-era avg -0.40 (n=3).

The ILLUSTRATIVE cross-institution delta is -0.1167, within hand-scoring
noise: CONSTANCY, not a gradient. p_value/cohens_d/ci_95 NOT_CALCULATED
per the standing Aug 28 2026 rule. is_significant: false.

WHY IT MATTERS: this is the first Type B to take up the in-corpus
journalists.yaml "CRITICAL MIGRATION: Guardian (11 years, UK tech editor)
-> Economist (AI writer, Oct 2024) ... high-signal migration for the DiD
analysis" flag. Driver class is journalist-level accountability habit, NOT
publication-driven (survives progressive daily broadsheet -> centrist
subscription weekly) and NOT financial-deal-driven: the Guardian-OpenAI
licensing partnership was announced 2025-02-19, five months AFTER Hern's
September 2024 departure, so no deal-softening pressure ever applied to
his Guardian tenure. A clean temporal boundary, parallel in function to
#472 (Bhuiyan within-Guardian discipline check) and #538 (Metz
litigation-adversary symmetry).

Guardian-era corpus (3 items, byline-attributed via relays):
- "Facebook updated fact-checking guidelines in August to include ads, but
  some fact checkers say they learned about the change only from
  Zuckerberg's testimony (Alex Hern/The Guardian)". https://mediagazer.com/191026/p4
- "Meta's Head of WhatsApp, Will Cathcart, says the service would refuse to
  comply with the UK's Online Safety Bill requirements to remove end-to-end
  encryption (Alex Hern/The Guardian)". https://www.techmeme.com/230309/p20
- Today in Focus #1467 metaverse transcript: "If you overlook the
  impossibility of it this is fantastic"; "the fear of the fact that
  Facebook relies on other people's platforms"; "Facebook is losing with
  young people".
  https://assets.nationbuilder.com/bestoftheleft/pages/5150/attachments/original/1644505335/_1467_No_One_Asked_For_The_Next_Big_Thing_%28Metaverse%29.pdf?1644505335

Economist-era corpus (3 items, broadcast/podcast tier):
- Babbage "OpenAI's alarming escape" (Jul 29 2026): "Recently, OpenAI
  admitted that its model broke out of a testing environment to carry out
  an assault on Hugging Face, another AI firm. It was the first ever fully
  autonomous AI hack... Alex Hern, The Economist's AI writer. Read Alex's
  exclusive conversation with Demis Hassabis about AI regulation."
  https://shows.acast.com/theeconomistbabbage/episodes/ai-catastrophe-could-be-around-the-corner
- BBC Media Show (Sep 2026): "Meta is reducing its investment in
  virtual-reality projects and directing greater resources into AI...
  Alex Hern, AI correspondent at The Economist, and Charlotte Henry...
  outline the implications." https://ivy.fm/tag/alex-hern
- Times Radio "Moltbook: AI Social Media a Flash in the Pan | Alex Hern":
  "Susan Owens is joined by The Economist's AI Writer, Alex Hern to weigh
  up the actual threat AI only social media platforms like Moltbook pose to
  the future of society." https://www.youtube.com/watch?v=RaTeJXdGezM

Migration sources (all verified 2026-09-08, URLs verbatim from Full-URL
listings in this run's browser.search query sets):
- https://muckrack.com/alex-hern-8 ("AI Writer for the Economist. Formerly the
  Guardian's UK Technology Editor"; farewell newsletter: "the end of my 11
  years at the Guardian, almost to the week: my first day was the release
  of the iPhone 5S, and on 9 September we will see the launch of the
  iPhone 16")
- https://talkingbiznews.com/media-news/guardian-tech-editor-hern-is-departing/
  ("Alex Hern, the tech editor at The Guardian, is leaving the publication
  after 11 years")
- https://newsworks.org.uk/news-and-opinion/the-guardian-releases-new-flagship-technology-newsletter/
  (TechScape: "Penned by its UK technology editor Alex Hern every Wednesday")
- https://champions-speakers.co.uk/speaker-agent/alex-hern (bio: "AI writer for
  The Economist"; "The Guardian's former UK Technology Editor")

CONFOUNDERS (6): STRONG evidence-tier asymmetry (written bylines via
relays vs broadcast/podcast appearances); STRONG genre asymmetry (news
scoops vs podcast guest commentary); MODERATE beat shift (platform
regulation/social media -> AI science/quantum); MODERATE timing skew
(2019-2023 vs 2026); WEAK selection bias (broadcasts book contrarian
voices); WEAK employer-audience shift (Economist weekly vs Guardian daily).

COUNTEREVIDENCE (5): post-migration corpus is broadcast-only, no Economist
print bylines in bounded search; Mistral CEO Mensch interview is neutral
industry-conversation register; Hassabis exclusive is access-based, softer
by construction; Guardian-era Meta sample n=3 with two relay attributions;
Guardian-OpenAI deal postdates departure, so tenure never tested deal
pressure (boundary condition, not falsification).

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE tones only (item level,
-1..+1 scale). p_value deliberately NOT_CALCULATED - a mechanical
significance test on hand-scored items would manufacture precision that
does not exist. is_significant: false. correlation_not_causation: true.

Sources: theguardian.com and wired.com direct fetch policy-blocked this
turn (browser.open failed, single attempt per terminal-failure convention);
all URLs verbatim from Full-URL listings or in-corpus records. No
zero-coverage claims per iteration-492. No canonical URLs constructed.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

BLOCK_KEY = 'mechanism_592_alex_hern_migration_guardian_economist_register_constancy_sep08'

TEST_FILE_NAME = 'test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py'

GUARDIAN_URLS = [
    'https://mediagazer.com/191026/p4',
    'https://www.techmeme.com/230309/p20',
    'https://assets.nationbuilder.com/bestoftheleft/pages/5150/attachments/original/1644505335/_1467_No_One_Asked_For_The_Next_Big_Thing_%28Metaverse%29.pdf?1644505335',
]

ECONOMIST_URLS = [
    'https://shows.acast.com/theeconomistbabbage/episodes/ai-catastrophe-could-be-around-the-corner',
    'https://ivy.fm/tag/alex-hern',
    'https://www.youtube.com/watch?v=RaTeJXdGezM',
]


def load_guardian():
    with open(os.path.join(PROFILES_DIR, 'guardian.yaml')) as f:
        return yaml.safe_load(f)


def get_hern_entry(data=None):
    data = data or load_guardian()
    for j in data.get('key_journalists', []):
        if j.get('name') == 'Alex Hern':
            return j
    return {}


def get_hern_block(data=None):
    entry = get_hern_entry(data)
    return entry.get('cross_entity_coverage_analysis', {}).get(BLOCK_KEY, {})


def get_scorer(block=None):
    block = block if block is not None else get_hern_block()
    return block.get('asymmetry_scorer_result', {})


# ===================================================================
# Test Class 1: YAML Parses, Hern Entry Carries the Block
# ===================================================================
class TestYamlAndEntry:
    def test_guardian_yaml_parses(self):
        data = load_guardian()
        assert data.get('key_journalists'), "key_journalists must exist"

    def test_hern_entry_exists(self):
        entry = get_hern_entry()
        assert entry, "Alex Hern must be in key_journalists"

    def test_hern_beat_notes_migration(self):
        entry = get_hern_entry()
        beat = entry.get('beat', '')
        patterns = entry.get('known_patterns', '')
        assert 'Economist' in beat, f"beat must note Economist move: {beat!r}"
        assert 'mechanism 592' in patterns or 'Mechanism 592' in patterns, \
            f"known_patterns must reference mechanism 592: {patterns!r}"

    def test_block_exists(self):
        assert get_hern_block(), f"{BLOCK_KEY} must exist on Alex Hern"

    def test_mechanism_id_592(self):
        block = get_hern_block()
        assert block.get('mechanism_id') == 592, \
            f"mechanism_id must be 592, got {block.get('mechanism_id')}"

    def test_iteration_598_type_b(self):
        block = get_hern_block()
        assert block.get('iteration') == 598, \
            f"iteration must be 598, got {block.get('iteration')}"
        assert block.get('iteration_type') == 'B', \
            f"iteration_type must be B, got {block.get('iteration_type')}"
        assert block.get('iteration_time') == '2026-09-08 00:00 PDT', \
            f"iteration_time mismatch: {block.get('iteration_time')}"


# ===================================================================
# Test Class 2: Migration Facts
# ===================================================================
class TestMigrationFacts:
    def test_guardian_tenure(self):
        mig = get_hern_block().get('migration', {})
        assert '2013' in mig.get('guardian_role', ''), \
            f"guardian_role must start ~2013: {mig.get('guardian_role')!r}"
        assert '2024' in mig.get('guardian_role', ''), \
            f"guardian_role must end Sep 2024: {mig.get('guardian_role')!r}"

    def test_economist_role(self):
        mig = get_hern_block().get('migration', {})
        assert 'AI writer' in mig.get('economist_role', ''), \
            f"economist_role must be AI writer: {mig.get('economist_role')!r}"

    def test_farewell_evidence_cites_eleven_years(self):
        mig = get_hern_block().get('migration', {})
        assert '11 years' in mig.get('farewell_evidence', ''), \
            "farewell_evidence must cite the 11-year tenure"

    def test_financial_temporal_boundary(self):
        mig = get_hern_block().get('migration', {})
        boundary = mig.get('financial_temporal_boundary', '')
        assert '2025-02-19' in boundary, \
            f"boundary must date the Guardian-OpenAI deal 2025-02-19: {boundary!r}"
        assert 'AFTER' in boundary or 'after' in boundary, \
            "boundary must state the deal postdates his departure"

    def test_institutional_contrast(self):
        mig = get_hern_block().get('migration', {})
        contrast = mig.get('institutional_contrast', '')
        assert 'broadsheet' in contrast and 'weekly' in contrast, \
            f"contrast must name both institution types: {contrast!r}"


# ===================================================================
# Test Class 3: Guardian-Era Corpus Attribution
# ===================================================================
class TestGuardianEraCorpus:
    def test_three_guardian_items(self):
        items = get_hern_block().get('guardian_era_corpus', [])
        assert len(items) == 3, \
            f"guardian_era_corpus must have 3 items, got {len(items)}"

    def test_guardian_urls_verbatim(self):
        items = get_hern_block().get('guardian_era_corpus', [])
        urls = [i.get('url') for i in items]
        assert urls == GUARDIAN_URLS, f"Guardian URLs must be verbatim: {urls}"

    def test_guardian_tones(self):
        items = get_hern_block().get('guardian_era_corpus', [])
        tones = [i.get('illustrative_tone') for i in items]
        assert tones == [-0.55, -0.45, -0.55], \
            f"Guardian tones must be [-0.55, -0.45, -0.55], got {tones}"

    def test_guardian_attributions_name_hern(self):
        items = get_hern_block().get('guardian_era_corpus', [])
        for item in items:
            attr = item.get('attribution', '')
            assert 'Hern' in attr or 'Guardian' in attr, \
                f"Guardian item must attribute Hern/Guardian: {attr!r}"

    def test_fact_checking_headline_present(self):
        items = get_hern_block().get('guardian_era_corpus', [])
        text = ' '.join(i.get('headline', '') + ' ' + i.get('register_note', '')
                        for i in items)
        assert 'fact-checking guidelines' in text, \
            "2019 Meta fact-checking scoop must be in the corpus"
        assert 'Online Safety Bill' in text, \
            "2023 WhatsApp Online Safety Bill item must be in the corpus"
        assert 'impossibility' in text, \
            "metaverse 'impossibility' item must be in the corpus"


# ===================================================================
# Test Class 4: Economist-Era Corpus Attribution
# ===================================================================
class TestEconomistEraCorpus:
    def test_three_economist_items(self):
        items = get_hern_block().get('economist_era_corpus', [])
        assert len(items) == 3, \
            f"economist_era_corpus must have 3 items, got {len(items)}"

    def test_economist_urls_verbatim(self):
        items = get_hern_block().get('economist_era_corpus', [])
        urls = [i.get('url') for i in items]
        assert urls == ECONOMIST_URLS, f"Economist URLs must be verbatim: {urls}"

    def test_economist_tones(self):
        items = get_hern_block().get('economist_era_corpus', [])
        tones = [i.get('illustrative_tone') for i in items]
        assert tones == [-0.55, -0.35, -0.3], \
            f"Economist tones must be [-0.55, -0.35, -0.3], got {tones}"

    def test_openai_alarming_escape_present(self):
        items = get_hern_block().get('economist_era_corpus', [])
        headlines = ' '.join(i.get('headline', '') for i in items)
        assert "OpenAI's alarming escape" in headlines, \
            "Babbage OpenAI item must be in the corpus"
        assert 'Meta reducing VR investment' in headlines or 'reducing VR' in headlines, \
            "BBC Media Show Meta VR item must be in the corpus"
        assert 'Moltbook' in headlines, \
            "Times Radio Moltbook item must be in the corpus"

    def test_all_source_urls_https(self):
        for u in get_hern_block().get('source_urls', []):
            assert u.startswith('https://'), f"non-https URL: {u}"

    def test_migration_source_urls_present(self):
        urls = get_hern_block().get('source_urls', [])
        assert 'https://muckrack.com/alex-hern-8' in urls
        assert 'https://talkingbiznews.com/media-news/guardian-tech-editor-hern-is-departing/' in urls


# ===================================================================
# Test Class 5: Statistical Discipline
# ===================================================================
class TestStatisticalDiscipline:
    def test_scorer_labeled_manual_illustrative(self):
        scorer = get_scorer()
        assert 'MANUAL ILLUSTRATIVE' in scorer.get('scorer', ''), \
            f"scorer must be labeled MANUAL ILLUSTRATIVE: {scorer.get('scorer')!r}"

    def test_stats_not_calculated(self):
        scorer = get_scorer()
        assert scorer.get('p_value') == 'NOT_CALCULATED', \
            f"p_value must be NOT_CALCULATED, got {scorer.get('p_value')}"
        assert scorer.get('cohens_d') == 'NOT_CALCULATED'
        assert scorer.get('ci_95') == 'NOT_CALCULATED'

    def test_not_significant(self):
        scorer = get_scorer()
        assert scorer.get('is_significant') is False, \
            "is_significant must be False"
        assert scorer.get('correlation_not_causation') is True

    def test_delta_within_hand_scoring_noise(self):
        scorer = get_scorer()
        delta = scorer.get('cross_institution_delta')
        assert abs(delta) < 0.2, \
            f"constancy claim requires |delta| < 0.2, got {delta}"
        assert 'CONSTANCY' in scorer.get('interpretation', ''), \
            "interpretation must state register constancy"

    def test_era_avgs_match_item_tones(self):
        scorer = get_scorer()
        block = get_hern_block()
        g = [i['illustrative_tone'] for i in block['guardian_era_corpus']]
        e = [i['illustrative_tone'] for i in block['economist_era_corpus']]
        assert abs(sum(g) / len(g) - scorer['guardian_era_meta_avg']) < 0.001
        assert abs(sum(e) / len(e) - scorer['economist_era_avg']) < 0.001


# ===================================================================
# Test Class 6: Confounders and Counterevidence
# ===================================================================
class TestConfoundersCounterevidence:
    def test_confounders_ranked_six(self):
        confs = get_hern_block().get('confounders_ranked', [])
        assert len(confs) == 6, f"must have 6 ranked confounders, got {len(confs)}"
        joined = ' '.join(confs)
        assert joined.count('STRONG') == 2, "must have 2 STRONG confounders"
        assert joined.count('MODERATE') == 2, "must have 2 MODERATE confounders"
        assert joined.count('WEAK') == 2, "must have 2 WEAK confounders"

    def test_evidence_tier_confounder_present(self):
        confs = get_hern_block().get('confounders_ranked', [])
        assert any('evidence-tier' in c for c in confs), \
            "evidence-tier asymmetry must be a ranked confounder"

    def test_counterevidence_five(self):
        ce = get_hern_block().get('counterevidence', [])
        assert len(ce) == 5, f"must have 5 counterevidence items, got {len(ce)}"

    def test_counterevidence_names_broadcast_only_and_mensch(self):
        ce = ' '.join(get_hern_block().get('counterevidence', []))
        assert 'broadcast-only' in ce, "counterevidence must flag broadcast-only corpus"
        assert 'Mensch' in ce, "counterevidence must flag the neutral Mensch interview"
        assert 'boundary condition' in ce, \
            "counterevidence must bound the financial-theory claim honestly"

    def test_driver_class_not_financial(self):
        dc = get_hern_block().get('driver_class', '')
        assert 'NOT financial-deal-driven' in dc, \
            "driver_class must exclude financial-deal-driven"
        assert 'NOT publication-driven' in dc, \
            "driver_class must exclude publication-driven"


# ===================================================================
# Test Class 7: Novelty and Uniqueness
# ===================================================================
class TestNovelty:
    def test_novelty_distinguishes_prior_units(self):
        novelty = get_hern_block().get('novelty', '')
        assert '#472' in novelty, \
            "Novelty must distinguish from #472 (Bhuiyan discipline check)"
        assert '#85' in novelty, \
            "Novelty must distinguish from #85 (Welch migration block)"
        assert '597 A -> 598 B' in novelty, \
            "Novelty must record the rotation 597 A -> 598 B"

    def test_block_key_unique_on_entry(self):
        data = load_guardian()
        entry = get_hern_entry(data)
        keys = [k for k in entry.get('cross_entity_coverage_analysis', {}).keys()
                if 'alex_hern_migration' in str(k)]
        assert keys == [BLOCK_KEY], \
            f"Exactly one 598 block must exist on Hern, got {keys}"

    def test_exactly_one_598_test_file(self):
        files = glob.glob(os.path.join(os.path.dirname(__file__),
                                       'test_type_b_598*.py'))
        assert len(files) == 1 and os.path.basename(files[0]) == TEST_FILE_NAME, \
            f"Exactly one 598 test file must exist, got {files}"

    def test_mechanism_592_unique_in_profiles(self):
        out = subprocess.run(
            ['grep', '-rl', 'mechanism_id: 592', PROFILES_DIR],
            capture_output=True, text=True)
        files = [f for f in out.stdout.splitlines() if f.strip()]
        assert files == [os.path.join(PROFILES_DIR, 'guardian.yaml')], \
            f"mechanism_id 592 must appear only in guardian.yaml, got {files}"

    def test_stale_core_stability_note_updated(self):
        with open(os.path.join(PROFILES_DIR, 'guardian.yaml')) as f:
            text = f.read()
        assert 'MIGRATION UPDATE 2026-09-08' in text, \
            "guardian.yaml notes must carry the dated Hern migration update"


# ===================================================================
# Test Class 8: Rotation Cycle Guard 598 (anchor patched in followup)
# Deselected pre-commit per the #565 followup convention.
# ===================================================================
class TestRotationCycleGuard598:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention.
    ANCHORED_COMMIT = "d1e8632"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type B #598 followup: ...") and doc-sync commits interleave
    # between mains since the #572/#573/#574 convention change; the naive
    # newest-5 filter broke on them. The colon immediately after the iteration
    # number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard598.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard598.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#598", "B"),
            ("#597", "A"),
            ("#596", "E"),
            ("#595", "D"),
            ("#594", "C"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # A->B is the edge this run closes; the full 5-window must be a
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
        assert len(nums) == len(set(nums)), \
            f"duplicate iteration numbers in window: {nums}"
