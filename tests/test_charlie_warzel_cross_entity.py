"""
Tests for Charlie Warzel (The Atlantic) cross-entity coverage analysis.

Validates that Warzel's coverage allocation — as The Atlantic's primary technology
voice and Galaxy Brain author — demonstrates systematic asymmetry: decade-long
adversarial Meta coverage using moral condemnation language ("original sin,"
"destroying democracy," "caused January 6th") while covering OpenAI with exclusive
executive access, Apple with analytical ecosystem critique, and Google with narrative
framing. This asymmetry correlates with The Atlantic's financial incentive structure:
OpenAI content deal + dual Apple financial link ($17B ownership + Apple News+ revenue)
+ ZERO Meta financial relationships.

Key findings:
1. Vocabulary asymmetry: Meta gets existential condemnation language, OpenAI gets
   philosophical framing, Apple gets aspirational positioning.
2. Access asymmetry: Exclusive Sam Altman interview (OpenAI), ZERO cooperative
   Meta executive access despite 10+ years covering the company.
3. Investigation asymmetry: 10+ year sustained adversarial Meta beat, ZERO
   equivalent investigative effort on OpenAI, Apple, or Google despite comparable
   privacy/governance concerns.
4. Financial correlation: Adversarial energy allocates perfectly with The Atlantic's
   incentive structure — maximum toward Meta ($0 deals), minimum toward OpenAI/Apple
   (multiple financial links).
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        data = yaml.safe_load(f)
    return data.get('journalists', data) if isinstance(data, dict) else data


@pytest.fixture
def atlantic():
    with open(os.path.join(PROFILES_DIR, 'atlantic.yaml')) as f:
        return yaml.safe_load(f)


def _get_warzel(journalists):
    """Extract Charlie Warzel's journalist entry."""
    for j in journalists:
        if j.get('name') == 'Charlie Warzel':
            return j
    raise AssertionError("Charlie Warzel not found in journalists.yaml")


class TestWarzelHasCompetitorCoverage:
    """Charlie Warzel's profile includes cross-entity competitor_coverage analysis."""

    def test_competitor_coverage_exists(self, journalists):
        warzel = _get_warzel(journalists)
        assert 'competitor_coverage' in warzel, (
            "Charlie Warzel needs competitor_coverage section for cross-entity analysis"
        )

    def test_covers_meta(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'meta' in cc, "Meta coverage analysis missing"

    def test_covers_openai(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'openai' in cc, "OpenAI coverage analysis missing"

    def test_covers_apple(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'apple' in cc, "Apple coverage analysis missing"

    def test_covers_google(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'google' in cc, "Google coverage analysis missing"

    def test_covers_elon_musk_x(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'elon_musk_x' in cc, "Elon Musk/X coverage analysis missing"

    def test_has_asymmetry_score(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        assert 'cross_entity_asymmetry_score' in cc, "Asymmetry score missing"


class TestWarzelMetaAdversarialBeat:
    """Warzel has a career-defining adversarial posture toward Meta/Facebook."""

    def test_meta_article_count_ge_15(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel['competitor_coverage']
        count = cc['meta'].get('article_count_estimate', 0)
        assert count >= 15, (
            f"Meta article count {count} < 15. Warzel has 10+ years of sustained "
            "adversarial Meta coverage across three institutions (BuzzFeed, NYT, "
            "The Atlantic), including multiple podcast appearances specifically "
            "about Facebook's harms."
        )

    def test_meta_tone_is_adversarial(self, journalists):
        warzel = _get_warzel(journalists)
        tone = warzel['competitor_coverage']['meta'].get('tone', '')
        assert 'adversarial' in tone.lower(), (
            f"Meta tone '{tone}' should reflect Warzel's career-defining adversarial "
            "posture — 'original sin' language, causal-blame framing ('How Facebook "
            "caused January 6th'), moral condemnation."
        )

    def test_meta_has_examples(self, journalists):
        warzel = _get_warzel(journalists)
        examples = warzel['competitor_coverage']['meta'].get('examples', [])
        assert len(examples) >= 3, (
            f"Meta coverage needs at least 3 specific examples with source URLs. "
            f"Found {len(examples)}."
        )

    def test_meta_examples_have_source_urls(self, journalists):
        warzel = _get_warzel(journalists)
        examples = warzel['competitor_coverage']['meta'].get('examples', [])
        for ex in examples:
            assert 'source_url' in ex and ex['source_url'], (
                f"Example '{ex.get('title')}' missing source_url"
            )

    def test_meta_mirror_award_documented(self, journalists):
        """Warzel's 2019 Mirror Award for Facebook privacy reporting is documented."""
        warzel = _get_warzel(journalists)
        # Awards may be in a dedicated list or documented in the notes field
        awards = warzel.get('awards', [])
        notes = warzel.get('notes', '')
        mirror_in_awards = any('mirror' in a.get('title', '').lower() for a in awards)
        mirror_in_notes = 'mirror award' in notes.lower()
        assert mirror_in_awards or mirror_in_notes, (
            "Warzel's 2019 Mirror Award for Facebook privacy reporting should be "
            "documented — it establishes his career-defining Facebook beat."
        )


class TestWarzelOpenAIAccessAsymmetry:
    """Warzel has exclusive executive access to OpenAI but not Meta."""

    def test_openai_tone_reflects_access(self, journalists):
        warzel = _get_warzel(journalists)
        tone = warzel['competitor_coverage']['openai'].get('tone', '')
        assert 'access' in tone.lower() or 'analytical' in tone.lower(), (
            f"OpenAI tone '{tone}' should reflect Warzel's exclusive executive "
            "access — he conducted a Q&A with Sam Altman, which is cooperative "
            "journalism, not adversarial investigation."
        )

    def test_openai_has_sam_altman_interview(self, journalists):
        """Warzel conducted an exclusive Q&A with OpenAI CEO Sam Altman."""
        warzel = _get_warzel(journalists)
        examples = warzel['competitor_coverage']['openai'].get('examples', [])
        altman_refs = [e for e in examples if 'altman' in e.get('title', '').lower()
                       or 'altman' in e.get('framing_notes', '').lower()]
        assert len(altman_refs) >= 1, (
            "Warzel's exclusive Sam Altman Q&A should be documented — it demonstrates "
            "cooperative journalism with OpenAI that has no Meta equivalent."
        )

    def test_openai_not_adversarial(self, journalists):
        """Despite OpenAI's governance crises, Warzel does NOT apply adversarial framing."""
        warzel = _get_warzel(journalists)
        tone = warzel['competitor_coverage']['openai'].get('tone', '')
        assert 'adversarial' not in tone.lower(), (
            f"OpenAI tone '{tone}' should NOT be adversarial. Despite OpenAI's "
            "board coup, safety team departures, copyright lawsuits, and data "
            "practices, Warzel applies analytical/philosophical framing — not the "
            "moral condemnation he reserves for Meta."
        )

    def test_meta_lacks_executive_access(self, journalists):
        """Warzel has ZERO cooperative executive interviews with Meta leaders."""
        warzel = _get_warzel(journalists)
        meta_examples = warzel['competitor_coverage']['meta'].get('examples', [])
        access_examples = [e for e in meta_examples
                          if 'interview' in e.get('framing_notes', '').lower()
                          and ('cooperative' in e.get('framing_notes', '').lower()
                               or 'access' in e.get('framing_notes', '').lower())]
        # None of Meta's examples should reflect cooperative executive access
        assert len(access_examples) == 0, (
            "Warzel should have ZERO cooperative Meta executive access. His Meta "
            "coverage is exclusively adversarial/external."
        )


class TestWarzelAppleCoverageAbsence:
    """Despite dual Apple financial link, Warzel has no adversarial Apple coverage."""

    def test_apple_tone_is_analytical(self, journalists):
        warzel = _get_warzel(journalists)
        tone = warzel['competitor_coverage']['apple'].get('tone', '')
        assert 'analytical' in tone.lower() or 'critique' in tone.lower(), (
            f"Apple tone '{tone}' should reflect analytical/ecosystem critique — "
            "Warzel frames Apple as aspirational ('central technological force') "
            "not as harmful ('original sin')."
        )

    def test_apple_not_adversarial(self, journalists):
        warzel = _get_warzel(journalists)
        tone = warzel['competitor_coverage']['apple'].get('tone', '')
        assert 'adversarial' not in tone.lower(), (
            f"Apple tone '{tone}' should NOT be adversarial. Despite Apple's data "
            "collection, App Store monopoly, and labor concerns, Warzel does not "
            "apply the moral condemnation he reserves for Meta."
        )

    def test_apple_coverage_gap_documented(self, journalists):
        warzel = _get_warzel(journalists)
        gap = warzel['competitor_coverage']['apple'].get('coverage_gap_notes', '')
        assert len(gap) > 50, (
            "Apple coverage gap should document the absence of adversarial "
            "investigation despite Apple's privacy practices — this gap correlates "
            "with The Atlantic's dual Apple financial link."
        )


class TestWarzelVocabularyAsymmetry:
    """Warzel uses fundamentally different vocabulary for Meta vs. competitors."""

    def test_meta_uses_moral_language(self, journalists):
        """Meta coverage includes existential/moral condemnation vocabulary."""
        warzel = _get_warzel(journalists)
        meta_examples = warzel['competitor_coverage']['meta'].get('examples', [])
        all_framing = ' '.join(e.get('framing_notes', '') for e in meta_examples)
        all_titles = ' '.join(e.get('title', '') for e in meta_examples)
        combined = (all_framing + ' ' + all_titles).lower()
        moral_terms = ['original sin', 'destroying democracy', 'caused',
                       'mocking', 'contemptuous', 'causal', 'blame']
        found = [t for t in moral_terms if t in combined]
        assert len(found) >= 2, (
            f"Meta coverage should include moral condemnation language. "
            f"Found: {found}. Expected 2+ terms from: {moral_terms}"
        )

    def test_openai_uses_philosophical_language(self, journalists):
        """OpenAI coverage uses philosophical/analytical vocabulary."""
        warzel = _get_warzel(journalists)
        openai_examples = warzel['competitor_coverage']['openai'].get('examples', [])
        all_framing = ' '.join(e.get('framing_notes', '') for e in openai_examples)
        combined = all_framing.lower()
        analytical_terms = ['faith', 'analytical', 'philosophical', 'cooperative']
        found = [t for t in analytical_terms if t in combined]
        assert len(found) >= 1, (
            f"OpenAI coverage should use analytical/philosophical vocabulary. "
            f"Found: {found}. Expected 1+ terms from: {analytical_terms}"
        )

    def test_apple_uses_aspirational_language(self, journalists):
        """Apple coverage uses aspirational/business vocabulary."""
        warzel = _get_warzel(journalists)
        apple_examples = warzel['competitor_coverage']['apple'].get('examples', [])
        all_framing = ' '.join(e.get('framing_notes', '') for e in apple_examples)
        combined = all_framing.lower()
        aspirational_terms = ['aspirational', 'ambitious', 'central technological',
                            'ecosystem', 'lock-in', 'business critique']
        found = [t for t in aspirational_terms if t in combined]
        assert len(found) >= 1, (
            f"Apple coverage should use aspirational/business vocabulary. "
            f"Found: {found}. Expected 1+ terms from: {aspirational_terms}"
        )


class TestWarzelFinancialCorrelation:
    """Warzel's adversarial energy correlates with Atlantic financial incentives."""

    def test_atlantic_has_openai_deal(self, atlantic):
        """The Atlantic has an OpenAI content licensing deal."""
        ownership = atlantic.get('ownership_chain', [])
        # Check competitor deals or financial relationships
        all_text = str(atlantic).lower()
        assert 'openai' in all_text, (
            "The Atlantic profile should document its OpenAI content deal"
        )

    def test_atlantic_has_apple_financial_link(self, atlantic):
        """The Atlantic has a dual Apple financial link (ownership + News+)."""
        all_text = str(atlantic).lower()
        assert 'apple' in all_text, (
            "The Atlantic profile should document its Apple financial link"
        )

    def test_atlantic_has_zero_meta_deals(self, atlantic):
        """The Atlantic has ZERO financial relationships with Meta."""
        # Check for explicit statement of no Meta deal
        all_text = str(atlantic).lower()
        # The profile should document what deals exist; Meta should be absent
        # from deal partner lists
        meta_deal_terms = ['meta content deal', 'meta licensing deal',
                          'meta financial relationship']
        found = [t for t in meta_deal_terms if t in all_text]
        assert len(found) == 0, (
            f"The Atlantic should have ZERO Meta financial relationships. "
            f"Found unexpected terms: {found}"
        )

    def test_adversarial_energy_correlates_with_incentives(self, journalists):
        """Maximum adversarialism toward Meta ($0 deals), minimum toward OpenAI/Apple."""
        warzel = _get_warzel(journalists)
        cc = warzel['competitor_coverage']
        meta_tone = cc['meta'].get('tone', '').lower()
        openai_tone = cc['openai'].get('tone', '').lower()
        apple_tone = cc['apple'].get('tone', '').lower()

        # Meta should be adversarial
        assert 'adversarial' in meta_tone, (
            f"Meta tone '{meta_tone}' should be adversarial (Meta pays Atlantic $0)"
        )
        # OpenAI should NOT be adversarial
        assert 'adversarial' not in openai_tone, (
            f"OpenAI tone '{openai_tone}' should not be adversarial (OpenAI has content deal)"
        )
        # Apple should NOT be adversarial
        assert 'adversarial' not in apple_tone, (
            f"Apple tone '{apple_tone}' should not be adversarial (Apple has dual financial link)"
        )


class TestWarzelAsymmetryScore:
    """The overall cross-entity asymmetry score is documented and significant."""

    def test_asymmetry_score_above_threshold(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        score = cc.get('cross_entity_asymmetry_score', 0)
        assert score >= 0.75, (
            f"Asymmetry score {score} < 0.75. Warzel's 10+ year adversarial Meta "
            "beat combined with analytical/cooperative coverage of OpenAI and Apple "
            "represents high cross-entity asymmetry."
        )

    def test_asymmetry_notes_exist(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        notes = cc.get('asymmetry_notes', '')
        assert len(notes) > 200, (
            "Asymmetry notes should provide substantial analysis of Warzel's "
            "cross-entity coverage patterns."
        )

    def test_asymmetry_notes_mention_financial_correlation(self, journalists):
        warzel = _get_warzel(journalists)
        cc = warzel.get('competitor_coverage', {})
        notes = cc.get('asymmetry_notes', '').lower()
        assert 'financial' in notes or 'incentive' in notes, (
            "Asymmetry notes should connect Warzel's coverage patterns to "
            "The Atlantic's financial incentive structure."
        )


class TestWarzelCareerArc:
    """Warzel's career progression documents the institutional pipeline."""

    def test_multi_publication_flag(self, journalists):
        warzel = _get_warzel(journalists)
        assert warzel.get('multi_publication') is True, (
            "Warzel should be flagged as multi-publication: Adweek → BuzzFeed → "
            "NYT → The Atlantic"
        )

    def test_career_has_four_institutions(self, journalists):
        warzel = _get_warzel(journalists)
        career = warzel.get('career', [])
        assert len(career) >= 4, (
            f"Warzel's career should document at least 4 institutions: "
            f"Adweek, BuzzFeed, NYT, The Atlantic. Found {len(career)}."
        )

    def test_buzzfeed_role_documents_meta_beat(self, journalists):
        """BuzzFeed role should document the origin of Warzel's adversarial Meta beat."""
        warzel = _get_warzel(journalists)
        career = warzel.get('career', [])
        buzzfeed = [c for c in career if 'buzzfeed' in c.get('publication', '').lower()]
        assert len(buzzfeed) >= 1, "BuzzFeed career entry missing"
        bf = buzzfeed[0]
        notes = bf.get('notes', '').lower()
        assert 'facebook' in notes or 'meta' in notes, (
            "BuzzFeed career notes should document the origin of Warzel's "
            "adversarial Facebook/Meta coverage beat."
        )
