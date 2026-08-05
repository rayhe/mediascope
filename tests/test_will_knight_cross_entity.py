"""
Tests for Will Knight (WIRED) cross-entity AI coverage analysis.

Validates that Knight's coverage allocation — as WIRED's most influential AI voice
(AI Lab newsletter, 20+ year AI beat veteran) — demonstrates systematic asymmetry:
7+ dedicated OpenAI articles, 5+ Google DeepMind articles, 3+ Anthropic articles,
and ZERO dedicated Meta AI articles. This matters because Knight controls WIRED's
"fundamental technology" narrative layer, and his coverage choices determine which
AI companies WIRED's audience perceives as leading the field.

Key findings:
1. Coverage volume asymmetry: OpenAI/DeepMind get deep organizational coverage,
   Meta AI gets ZERO dedicated coverage despite operating one of the world's top
   AI research labs (FAIR) and releasing the most widely used open-weight models.
2. Talent framing asymmetry: OpenAI "poaches" (active, aggressive verb), Google
   DeepMind "signs licensing deals to hire" (neutral, professional language).
   Meta appears only as a poaching VICTIM, never as a talent destination.
3. Executive access asymmetry: Multiple extended Demis Hassabis Q&As, ZERO
   Yann LeCun interviews despite LeCun's equal prominence (Turing Award winner).
4. Three-layer WIRED exclusion: technology (Knight avoidance), business (Schiffer
   adversarialism), consumer (Goode lane avoidance) — Meta is adversarially covered
   or not covered at all across every editorial function.
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


def _get_knight(journalists):
    """Extract Will Knight's journalist entry."""
    for j in journalists:
        if j.get('name') == 'Will Knight':
            return j
    raise AssertionError("Will Knight not found in journalists.yaml")


class TestKnightHasCompetitorCoverage:
    """Will Knight's profile includes cross-entity competitor_coverage analysis."""

    def test_competitor_coverage_exists(self, journalists):
        knight = _get_knight(journalists)
        assert 'competitor_coverage' in knight, (
            "Will Knight needs competitor_coverage section for cross-entity analysis"
        )

    def test_covers_openai(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'openai' in cc, "OpenAI coverage analysis missing"

    def test_covers_google_deepmind(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'google_deepmind' in cc, "Google DeepMind coverage analysis missing"

    def test_covers_anthropic(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'anthropic' in cc, "Anthropic coverage analysis missing"

    def test_covers_meta(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'meta' in cc, "Meta coverage analysis missing"

    def test_covers_apple(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'apple' in cc, "Apple coverage analysis missing"

    def test_has_asymmetry_score(self, journalists):
        knight = _get_knight(journalists)
        cc = knight.get('competitor_coverage', {})
        assert 'cross_entity_asymmetry_score' in cc, "Asymmetry score missing"


class TestKnightCoverageVolumeAsymmetry:
    """Knight's article count allocation reveals structural asymmetry."""

    def test_openai_article_count_ge_7(self, journalists):
        knight = _get_knight(journalists)
        cc = knight['competitor_coverage']
        count = cc['openai'].get('article_count_estimate', 0)
        assert count >= 7, (
            f"OpenAI article count {count} < 7. Knight has published 7+ dedicated "
            "OpenAI articles covering talent, organizational dynamics, safety research, "
            "robotics ambitions, and product reviews."
        )

    def test_google_deepmind_article_count_ge_5(self, journalists):
        knight = _get_knight(journalists)
        cc = knight['competitor_coverage']
        count = cc['google_deepmind'].get('article_count_estimate', 0)
        assert count >= 5, (
            f"Google DeepMind article count {count} < 5. Knight has published 5+ "
            "dedicated DeepMind articles including multiple Hassabis Q&As, talent "
            "acquisitions, and robotics integrations."
        )

    def test_anthropic_article_count_ge_3(self, journalists):
        knight = _get_knight(journalists)
        cc = knight['competitor_coverage']
        count = cc['anthropic'].get('article_count_estimate', 0)
        assert count >= 3, (
            f"Anthropic article count {count} < 3. Knight has published 3+ Anthropic "
            "pieces including Trump ban scoop, supply chain risk follow-up, and "
            "Agentic AI Foundation launch."
        )

    def test_meta_article_count_is_zero(self, journalists):
        knight = _get_knight(journalists)
        cc = knight['competitor_coverage']
        count = cc['meta'].get('article_count_estimate', 0)
        assert count == 0, (
            f"Meta article count {count} != 0. CRITICAL: Knight has ZERO identified "
            "dedicated articles about Meta's AI technology, strategy, or leadership. "
            "Meta appears only peripherally (as poaching victim, benchmark comparison, "
            "or national security concern)."
        )

    def test_openai_exceeds_meta_by_at_least_7(self, journalists):
        """The OpenAI-Meta coverage delta should be at least 7 articles."""
        knight = _get_knight(journalists)
        cc = knight['competitor_coverage']
        openai_count = cc['openai'].get('article_count_estimate', 0)
        meta_count = cc['meta'].get('article_count_estimate', 0)
        delta = openai_count - meta_count
        assert delta >= 7, (
            f"OpenAI-Meta delta is {delta}, expected >= 7. Knight publishes 7+ "
            "dedicated OpenAI articles and ZERO Meta AI articles despite Meta "
            "operating FAIR (one of the world's top AI research labs) and releasing "
            "the most widely used open-weight AI models (Llama series)."
        )


class TestKnightToneAsymmetry:
    """Knight applies different editorial tones to different companies."""

    def test_openai_tone_reflects_deep_access(self, journalists):
        knight = _get_knight(journalists)
        tone = knight['competitor_coverage']['openai'].get('tone', '')
        assert 'access' in tone.lower() or 'institutional' in tone.lower(), (
            f"OpenAI tone '{tone}' should reflect Knight's deep institutional access "
            "— organizational analyses, talent scoops, safety research coverage."
        )

    def test_google_deepmind_tone_is_reverential(self, journalists):
        knight = _get_knight(journalists)
        tone = knight['competitor_coverage']['google_deepmind'].get('tone', '')
        assert 'reverential' in tone.lower() or 'executive' in tone.lower(), (
            f"DeepMind tone '{tone}' should reflect reverential executive access — "
            "multiple extended Hassabis Q&As with aspirational language."
        )

    def test_meta_tone_reflects_absence(self, journalists):
        knight = _get_knight(journalists)
        tone = knight['competitor_coverage']['meta'].get('tone', '')
        assert 'absent' in tone.lower() or 'peripheral' in tone.lower(), (
            f"Meta tone '{tone}' should reflect absence or peripheral coverage — "
            "Knight has ZERO dedicated Meta AI articles."
        )

    def test_apple_tone_is_constructive(self, journalists):
        knight = _get_knight(journalists)
        tone = knight['competitor_coverage']['apple'].get('tone', '')
        assert 'constructive' in tone.lower(), (
            f"Apple tone '{tone}' should reflect constructive analysis — Knight "
            "frames Apple AI as 'the value of seeing AI as a feature'."
        )


class TestKnightTalentFramingAsymmetry:
    """Knight uses different language for talent movements between companies."""

    def test_openai_talent_uses_poach_language(self, journalists):
        """OpenAI taking Meta engineers = 'poaches' (aggressive vocabulary)."""
        knight = _get_knight(journalists)
        openai_examples = knight['competitor_coverage']['openai'].get('examples', [])
        poach_articles = [e for e in openai_examples
                          if 'poach' in e.get('title', '').lower()]
        assert len(poach_articles) >= 1, (
            "Knight's OpenAI talent coverage should include at least one article "
            "using 'poaches' language — positions Meta as victim being raided."
        )

    def test_google_talent_uses_neutral_language(self, journalists):
        """Google acquiring talent = 'licensing deal to hire' (professional language)."""
        knight = _get_knight(journalists)
        gd_examples = knight['competitor_coverage']['google_deepmind'].get('examples', [])
        hire_articles = [e for e in gd_examples
                         if 'licensing deal' in e.get('title', '').lower()
                         or 'hires' in e.get('title', '').lower()]
        assert len(hire_articles) >= 1, (
            "Knight's Google DeepMind talent coverage should use neutral 'hires' or "
            "'licensing deal' language — compare to 'poaches' for OpenAI."
        )

    def test_meta_never_framed_as_talent_destination(self, journalists):
        """Meta appears only as talent SOURCE (being poached from), never as destination."""
        knight = _get_knight(journalists)
        meta_section = knight['competitor_coverage']['meta']
        gap_notes = meta_section.get('coverage_gap_notes', '')
        assert 'talent source' in gap_notes.lower() or 'poaching victim' in gap_notes.lower() or \
               'poached from' in gap_notes.lower(), (
            "Meta's coverage gap notes should document that Meta appears only as a "
            "talent source being poached from, not as a talent destination."
        )


class TestKnightExecutiveAccessAsymmetry:
    """Knight interviews competitor executives but not Meta AI leadership."""

    def test_hassabis_has_multiple_interviews(self, journalists):
        knight = _get_knight(journalists)
        gd_examples = knight['competitor_coverage']['google_deepmind'].get('examples', [])
        hassabis_pieces = [e for e in gd_examples
                           if 'hassabis' in e.get('title', '').lower()
                           or 'q&a' in e.get('title', '').lower()
                           or 'gemini' in e.get('framing_notes', '').lower()]
        assert len(hassabis_pieces) >= 1, (
            "Knight should have at least one Hassabis Q&A/interview documented. "
            "He has conducted multiple extended interviews with the DeepMind CEO."
        )

    def test_lecun_has_zero_interviews(self, journalists):
        """Yann LeCun (Meta, Turing Award winner) has ZERO Knight interviews."""
        knight = _get_knight(journalists)
        meta_section = knight['competitor_coverage']['meta']
        gap_notes = meta_section.get('coverage_gap_notes', '')
        assert 'yann lecun' in gap_notes.lower() or 'lecun' in gap_notes.lower(), (
            "Meta coverage gap notes should document the absence of Yann LeCun "
            "interviews — a Turing Award winner with equal prominence to Hassabis."
        )


class TestKnightAsymmetryScore:
    """The cross-entity asymmetry score reflects the coverage gap."""

    def test_asymmetry_score_above_0_85(self, journalists):
        knight = _get_knight(journalists)
        score = knight['competitor_coverage'].get('cross_entity_asymmetry_score', 0)
        assert score >= 0.85, (
            f"Asymmetry score {score} < 0.85. Knight's coverage allocation is "
            "extremely asymmetric: 7+ OpenAI / 5+ DeepMind / 3+ Anthropic / "
            "ZERO Meta across 20+ identifiable articles."
        )

    def test_asymmetry_notes_mention_three_layer_exclusion(self, journalists):
        """The asymmetry notes should document WIRED's three-layer editorial exclusion."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage'].get('asymmetry_notes', '')
        assert 'three-layer' in notes.lower() or 'three' in notes.lower(), (
            "Asymmetry notes should document the three-layer WIRED exclusion: "
            "technology (Knight), business (Schiffer), consumer (Goode)."
        )

    def test_asymmetry_notes_mention_conde_nast_financial_incentive(self, journalists):
        """Notes should connect coverage gap to Condé Nast's OpenAI deal."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage'].get('asymmetry_notes', '')
        assert 'condé nast' in notes.lower() or 'conde nast' in notes.lower(), (
            "Asymmetry notes should reference Condé Nast's financial incentive "
            "structure (OpenAI content deal, no Meta financial relationship)."
        )


class TestKnightMetaCoverageGap:
    """Meta-specific coverage gap documentation is comprehensive."""

    def test_meta_has_coverage_gap_notes(self, journalists):
        knight = _get_knight(journalists)
        meta_section = knight['competitor_coverage']['meta']
        assert 'coverage_gap_notes' in meta_section, (
            "Meta section needs coverage_gap_notes documenting the absence"
        )

    def test_gap_mentions_fair(self, journalists):
        """FAIR (Meta's AI research lab) should be mentioned as context."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage']['meta'].get('coverage_gap_notes', '')
        assert 'fair' in notes.lower(), (
            "Coverage gap notes should mention FAIR — Meta operates one of the "
            "world's top AI research labs, yet gets ZERO Knight coverage."
        )

    def test_gap_mentions_llama(self, journalists):
        """Llama (most widely used open-weight models) should be mentioned."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage']['meta'].get('coverage_gap_notes', '')
        assert 'llama' in notes.lower(), (
            "Coverage gap notes should mention Llama — the most widely used "
            "open-weight AI models, yet Knight has ZERO dedicated Llama pieces."
        )

    def test_gap_mentions_capex(self, journalists):
        """Meta's massive infrastructure spending should be mentioned as context."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage']['meta'].get('coverage_gap_notes', '')
        assert 'capex' in notes.lower() or 'infrastructure' in notes.lower() or \
               '$130' in notes or '$145' in notes, (
            "Coverage gap notes should mention Meta's infrastructure spending "
            "($130-145B capex) as context for the coverage absence."
        )

    def test_gap_mentions_zero_organizational_analysis(self, journalists):
        """Knight's zero organizational analyses of Meta AI should be documented."""
        knight = _get_knight(journalists)
        notes = knight['competitor_coverage']['meta'].get('coverage_gap_notes', '')
        assert 'organizational' in notes.lower() or 'talent exodus' in notes.lower(), (
            "Coverage gap notes should contrast Knight's organizational analyses "
            "(OpenAI talent exodus piece) with zero equivalent Meta coverage."
        )

    def test_meta_no_examples_listed(self, journalists):
        """Meta section should have NO article examples — that's the finding."""
        knight = _get_knight(journalists)
        meta_section = knight['competitor_coverage']['meta']
        examples = meta_section.get('examples', [])
        assert len(examples) == 0, (
            f"Meta section has {len(examples)} examples but should have ZERO — "
            "the finding is that Knight publishes no dedicated Meta AI articles."
        )
