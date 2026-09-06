"""Type B #553 (2026-09-06 01:00 PDT): Caroline Haskins (WIRED) surveillance-beat
register-constancy test - WIRED business-desk reporter covering Silicon Valley,
surveillance, and labor.

Career arc: The Outline (intern) -> Motherboard/Vice (staff writer, obtained
Palantir police manual) -> BuzzFeed News (senior tech reporter, broke Ring,
Clearview AI, Gaggle stories) -> Business Insider (research editor / senior tech
reporter, AI and surveillance) -> freelance 1+ yr (Guardian, TIME, CNET) ->
WIRED business desk (started 2026-03-10, reports to Zoe Schiffer, Director of
Business & Industry). Career source:
https://github.com/rayhe/mediascope/commit/886459669ba34653919b8e26ce6dbb7178dc291c

Meta pieces (3):
1. Project Cannes investigation Jul 1 2026 ("Meta Contractors Posed as Teens to
   Test Rival AI Chatbots on Suicide, Sex, and Drugs"), investigative
   adversarial, -0.80. Byline repository-attributed (commit 88645966).
   Repo analysis:
   https://github.com/rayhe/mediascope/blob/HEAD/examples/sample_output/wired_meta_project_cannes_contractors_2026_07_01_analysis.md
2. "Meta's New Feel-Good AI Ad Uses a Song About the World Ending" Jul 23 2026,
   https://www.wired.com/story/meta-david-bowie-apocalypse-ad-is-optimistic-actually/
   ironic cultural critique, -0.35. Byline secondary-attested via
   https://singulism.com/en/2026-07-24-meta-david-bowie-ad-five-years/
3. "The Zuckerbergs Are Hiring a Lifeguard but Calling It a 'Beach Water
   Person'" May 19 2026,
   https://www.wired.com/story/mark-zuckerberg-priscilla-chan-lifeguard-beach-water-person/
   euphemism satire, -0.25. Byline secondary-attested via inforeader author
   listing.

Non-Meta surveillance pieces (3):
1. "A Georgia Cop Used Flock to Track 2 Other Cops - His Ex and Her Friend"
   Aug 27 2026,
   https://www.wired.com/story/a-georgia-cop-used-flock-to-track-2-other-cops-his-ex-and-her-friend/
   investigative adversarial, -0.65. Byline via
   https://muckrack.com/caroline_haskins/articles
2. "Flock Highlighted Police Departments Using Its Tech. Now 4 Face Allegations
   of Misuse" Aug 6 2026, -0.60. Byline via inforeader author listing; no
   verbatim wired.com URL surfaced, not constructed.
3. "The 'Guardrail Guy' Went Viral for Posting About Flock Cameras. Then
   Someone Destroyed Them" Aug 3 2026, -0.45. Byline via
   https://wesearch.press/s/the-guardrail-guy-went-viral-for-posting-about-flock-cameras-bae46044

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [-0.80, -0.35, -0.25] avg -0.467 vs non-Meta [-0.65, -0.60, -0.45]
avg -0.567. Delta (Meta minus non-Meta) +0.10. p_value NOT_CALCULATED,
is_significant False, artifact-grade False.

Interpretation (falsification family; distinct from #548 Mehrotra which is a
different reporter on a different desk, and from commit 88645966 which added
Haskins to journalist tracking with no framing comparison): Haskins applies
the investigative-adversarial register to Meta (Project Cannes, -0.80) and to
non-Meta surveillance targets (Flock ALPR misuse, -0.65/-0.60) with comparable
severity. Meta avg -0.467 vs non-Meta -0.567 is near-zero constancy with Meta
marginally SOFTER, which runs against the journalist-level anti-Meta bias
hypothesis. Consistent with the #548 Mehrotra, #457 Adrienne So, and #493
Fowler company-agnostic precedents.

Strongest counterargument: the genre split could mask entity selectivity -
Haskins may choose the investigative register for Flock but the ironic register
for Meta even when Meta conduct warrants investigation. The Bowie-ad glasses
parenthetical shows she reaches for surveillance vocabulary against Meta even
in culture pieces, which could indicate a standing anti-Meta frame. The one
matched-genre pair (Cannes -0.80 vs Georgia cop -0.65) favors constancy, but
n=1 per genre-cell is too thin for a firm claim. MANUAL ILLUSTRATIVE,
correlation-only.

Evidence hygiene: URLs carried verbatim from tool output this run; the
truncated wired.com slug for the Atlanta-suburb Flock piece was NOT used and
the piece was NOT scored; no wired.com URLs constructed. No em dashes in any
new prose.

Novelty (per durable rule): zero caroline_haskins keys in
journalist_cross_entity_coverage before this run (grep verified); no #553 in
git log (grep verified); commit 88645966 added Haskins to tracking only, no
framing comparison; #548 is Mehrotra (different reporter, different desk).
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'wired.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['journalist_cross_entity_coverage']['caroline_haskins']


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index('  caroline_haskins:')
    end = text.index('\n  wired_openai_rogue_swarm_aug26_followup_silence:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present(self):
        profile = _load_profile()
        assert 'caroline_haskins' in profile['journalist_cross_entity_coverage']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 553
        assert m['iteration'] == 553
        assert m['type'].startswith('Type B')
        assert m['journalist'] == 'Caroline Haskins'
        assert m['date_analyzed'] == '2026-09-06'

    def test_finding_type_falsification(self):
        m = _mechanism()
        assert m['finding_type'] == 'journalist_cross_entity_register_constancy_falsification'

    def test_distinguishes_from_prior(self):
        m = _mechanism()
        blob = ' '.join(m['distinguishes_from'])
        assert 'mechanism 548' in blob
        assert '88645966' in blob
        assert 'different desk' in blob

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'


class TestCareerTimeline:
    def test_wired_start_date(self):
        m = _mechanism()
        assert '2026-03-10' in m['career_timeline']['wired']
        assert 'Zoe Schiffer' in m['career_timeline']['wired']

    def test_surveillance_beat_arc(self):
        m = _mechanism()
        tl = m['career_timeline']
        assert 'Palantir' in tl['motherboard_vice']
        assert 'Clearview AI' in tl['buzzfeed']

    def test_career_source_commit(self):
        m = _mechanism()
        assert m['career_timeline']['career_source'] == \
            'https://github.com/rayhe/mediascope/commit/886459669ba34653919b8e26ce6dbb7178dc291c'


class TestMetaPieces:
    def test_three_meta_pieces(self):
        assert len(_mechanism()['meta_pieces']) == 3

    def test_project_cannes_adversarial(self):
        m = _mechanism()
        pc = [p for p in m['meta_pieces'] if p.get('internal_codename') == 'Project Cannes']
        assert len(pc) == 1
        assert pc[0]['tone_approx'] == -0.80
        assert pc[0]['register'] == 'investigative_adversarial'
        assert pc[0]['evidence_grade'] == 'repository_attributed'

    def test_bowie_ad_direct_url(self):
        m = _mechanism()
        ad = [p for p in m['meta_pieces'] if 'Feel-Good AI Ad' in p['title']]
        assert len(ad) == 1
        assert ad[0]['url'] == 'https://www.wired.com/story/meta-david-bowie-apocalypse-ad-is-optimistic-actually/'
        assert ad[0]['tone_approx'] == -0.35
        assert ad[0]['register'] == 'ironic_cultural_critique'
        assert 'harassing women while surreptitiously recording them' in ad[0]['key_quote']

    def test_lifeguard_direct_url(self):
        m = _mechanism()
        lg = [p for p in m['meta_pieces'] if 'Beach Water Person' in p['title']]
        assert len(lg) == 1
        assert lg[0]['url'] == 'https://www.wired.com/story/mark-zuckerberg-priscilla-chan-lifeguard-beach-water-person/'
        assert lg[0]['tone_approx'] == -0.25
        assert lg[0]['register'] == 'euphemism_satire'

    def test_meta_registers_span_genres(self):
        m = _mechanism()
        regs = {p['register'] for p in m['meta_pieces']}
        assert regs == {'investigative_adversarial', 'ironic_cultural_critique', 'euphemism_satire'}


class TestNonMetaPieces:
    def test_three_non_meta_pieces(self):
        assert len(_mechanism()['non_meta_surveillance_pieces']) == 3

    def test_georgia_cop_direct_url(self):
        m = _mechanism()
        gc = [p for p in m['non_meta_surveillance_pieces'] if 'Georgia Cop' in p['title']]
        assert len(gc) == 1
        assert gc[0]['url'] == 'https://www.wired.com/story/a-georgia-cop-used-flock-to-track-2-other-cops-his-ex-and-her-friend/'
        assert gc[0]['tone_approx'] == -0.65
        assert gc[0]['register'] == 'investigative_adversarial'

    def test_flock_misuse_no_constructed_url(self):
        m = _mechanism()
        fm = [p for p in m['non_meta_surveillance_pieces'] if '4 Face Allegations' in p['title']]
        assert len(fm) == 1
        assert 'url' not in fm[0]
        assert 'not constructed' in fm[0]['notes']
        assert fm[0]['tone_approx'] == -0.60

    def test_guardrail_guy_register(self):
        m = _mechanism()
        gg = [p for p in m['non_meta_surveillance_pieces'] if 'Guardrail Guy' in p['title']]
        assert len(gg) == 1
        assert gg[0]['register'] == 'advocate_sympathetic_surveillance_critical'
        assert gg[0]['tone_approx'] == -0.45


class TestScorer:
    def test_arrays(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['target_entity'] == 'meta'
        assert r['target_tones_manual_illustrative'] == [-0.80, -0.35, -0.25]
        assert r['reference_tones_manual_illustrative'] == [-0.65, -0.60, -0.45]

    def test_arithmetic(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert abs(r['target_avg'] - (-0.467)) < 0.001
        assert abs(r['reference_avg'] - (-0.567)) < 0.001
        assert abs(r['delta_meta_minus_non_meta'] - 0.10) < 0.001
        assert r['interpretation'] == 'near_zero_constancy_not_asymmetry'

    def test_manual_illustrative_guards(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['p_value'] == 'NOT_CALCULATED'
        assert r['cohens_d'] == 'NOT_CALCULATED'
        assert r['ci'] == 'NOT_CALCULATED'
        assert r['is_significant'] is False
        assert r['artifact_grade'] is False

    def test_limitations_stated(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert 'n=3 vs n=3' in r['limitations']


class TestConfoundersAndCounterargument:
    def test_confounders_present_and_ranked(self):
        m = _mechanism()
        confs = m['confounders']
        assert len(confs) >= 5
        assert confs[0]['strength'] == 'STRONG'
        blob = ' '.join(c['text'] for c in confs)
        assert 'Genre mismatch' in blob
        assert 'Beat assignment' in blob

    def test_strongest_counterargument_genre_split(self):
        ca = _mechanism()['strongest_counterargument']
        assert 'genre split' in ca
        assert 'MANUAL ILLUSTRATIVE' in ca
        assert 'correlation-only' in ca

    def test_financial_context_control_case(self):
        fc = _mechanism()['financial_context']
        assert 'Flock Safety' in fc
        assert '$5-10M' in fc
        assert 'does not imply causation' in fc


class TestNoEmDashes:
    def test_no_em_dashes_in_block(self):
        assert '—' not in _mechanism_block_text()


class TestIterationLog:
    def test_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#553' in text
        assert 'Type B' in text

    def test_log_entry_relative_order(self):
        with open(LOG) as f:
            text = f.read()
        m552 = re.search(r'^#552\b', text, re.MULTILINE)
        m553 = re.search(r'^#553\b', text, re.MULTILINE)
        assert m553 is not None and m552 is not None
        assert m553.start() < m552.start()

    def test_log_entry_content(self):
        with open(LOG) as f:
            text = f.read()
        start = text.index('#553 Type B')
        end = text.index('#552 Type A')
        block = text[start:end]
        assert 'Haskins' in block
        assert '+0.10' in block
        assert 'NOT artifact-grade' in block
