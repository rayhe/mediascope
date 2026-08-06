"""
Test: The Verge × Anthropic Coverage & Rogue AI Safety Comparison
Type A: Competitor Coverage Deep Dive
Date: 2026-08-06
Focus: How The Verge covers Anthropic (no deal) vs OpenAI (deal partner)
       vs Meta (no deal, competitive threat) — with specific focus on
       the July 2026 rogue AI safety incidents

Key Finding: The "Accidentally" Paradox
  OpenAI's unprecedented autonomous cyberattack (real harm, real victims,
  FBI involvement, congressional legislation) receives mitigating framing
  ("accidentally"), while Meta's speculative glasses privacy risk receives
  escalating framing ("predator," "mass surveillance"). Financial
  relationship + competitive threat predict editorial temperature.

Three-Tier Model:
  Entity PAYS The Verge → soft coverage (OpenAI)
  Entity NEITHER PAYS NOR THREATENS → neutral coverage (Anthropic)
  Entity NEITHER PAYS BUT THREATENS business model → adversarial (Meta)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestVergeAnthropicCoverage:
    """Verify Anthropic coverage section exists and has correct structure."""

    def setup_method(self):
        self.research = load_competitor_research()
        self.verge = self.research['publications']['the-verge']

    def test_anthropic_coverage_tone_exists(self):
        assert 'anthropic_coverage_tone' in self.verge

    def test_anthropic_coverage_tone_is_neutral(self):
        """Anthropic (no deal, no threat) should receive neutral coverage."""
        assert self.verge['anthropic_coverage_tone'] == 'neutral'

    def test_anthropic_coverage_summary_exists(self):
        assert 'anthropic_coverage_summary' in self.verge
        assert len(self.verge['anthropic_coverage_summary']) > 100

    def test_anthropic_examples_exist(self):
        assert 'anthropic_examples' in self.verge
        assert len(self.verge['anthropic_examples']) >= 1

    def test_anthropic_mythos_example_documented(self):
        """The Mythos unauthorized access story should be documented."""
        examples = self.verge['anthropic_examples']
        mythos_articles = [e for e in examples if 'Mythos' in e.get('title', '')
                          or 'dangerous' in e.get('title', '').lower()]
        assert len(mythos_articles) >= 1

    def test_anthropic_reporter_is_news_writer(self):
        """Anthropic stories assigned to news writer, not investigator."""
        examples = self.verge['anthropic_examples']
        reporters = [e.get('reporter', '') for e in examples]
        # Jess Weatherbed is a news writer, not investigative
        assert any('Weatherbed' in r for r in reporters)

    def test_anthropic_tone_less_adversarial_than_meta(self):
        """Anthropic tone should be less adversarial than Meta tone."""
        examples = self.verge['anthropic_examples']
        anthropic_tones = [e.get('tone', 0) for e in examples]
        meta_examples = self.verge.get('meta_institutional_examples', [])
        meta_tones = [e.get('tone', 0) for e in meta_examples]
        if anthropic_tones and meta_tones:
            avg_anthropic = sum(anthropic_tones) / len(anthropic_tones)
            avg_meta = sum(meta_tones) / len(meta_tones)
            # Anthropic should be closer to 0 (neutral) than Meta (adversarial)
            assert avg_anthropic > avg_meta

    def test_anthropic_no_financial_relationship(self):
        """Anthropic has no financial deal with Vox Media / The Verge."""
        summary = self.verge['anthropic_coverage_summary']
        assert 'ZERO financial relationship' in summary


class TestVergeRogueAISafetyComparison:
    """Verify the rogue AI safety incident comparison is documented."""

    def setup_method(self):
        self.research = load_competitor_research()
        self.verge = self.research['publications']['the-verge']

    def test_rogue_ai_comparison_exists(self):
        assert 'rogue_ai_safety_comparison' in self.verge

    def test_rogue_ai_comparison_has_substance(self):
        comparison = self.verge['rogue_ai_safety_comparison']
        assert len(comparison) > 500

    def test_accidentally_paradox_documented(self):
        """The 'Accidentally' Paradox should be named and documented."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'Accidentally' in comparison or 'accidentally' in comparison

    def test_three_rogue_incidents_documented(self):
        """All three July 2026 rogue AI incidents should be documented."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'Hugging Face' in comparison
        assert 'hacked 3 companies' in comparison or 'three companies' in comparison.lower()
        assert 'UK AISI' in comparison or 'fake human profiles' in comparison

    def test_real_vs_speculative_harm_contrast(self):
        """Comparison should contrast real cyber harm with speculative risk."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'REAL' in comparison or 'real' in comparison.lower()
        assert 'speculative' in comparison.lower() or 'SPECULATIVE' in comparison

    def test_fbi_involvement_noted(self):
        """FBI involvement in OpenAI incident should be documented."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'FBI' in comparison

    def test_mitigating_vs_escalating_language(self):
        """Should document mitigating (OpenAI) vs escalating (Meta) framing."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'mitigating' in comparison.lower()
        assert 'escalating' in comparison.lower()

    def test_comparison_sources_exist(self):
        assert 'rogue_ai_comparison_sources' in self.verge
        sources = self.verge['rogue_ai_comparison_sources']
        assert len(sources) >= 3


class TestVergeThreeTierModel:
    """Verify the three-tier coverage model is documented and consistent."""

    def setup_method(self):
        self.research = load_competitor_research()
        self.verge = self.research['publications']['the-verge']

    def test_three_tier_model_in_comparison(self):
        """Three-tier model should be documented in the comparison."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'THREE-TIER' in comparison or 'three-tier' in comparison.lower()

    def test_tier_1_pay_equals_soft(self):
        """Tier 1: Entity pays → soft coverage."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'PAYS' in comparison
        # OpenAI should be the pay tier example
        assert 'OpenAI' in comparison

    def test_tier_2_neutral_equals_factual(self):
        """Tier 2: Entity neither pays nor threatens → neutral coverage."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'NEITHER PAYS NOR THREATENS' in comparison
        # Anthropic should be the neutral tier example
        assert 'Anthropic' in comparison

    def test_tier_3_threatens_equals_adversarial(self):
        """Tier 3: Entity threatens business model → adversarial coverage."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'THREATENS' in comparison
        # Meta should be the adversarial tier example
        assert 'Meta' in comparison

    def test_openai_tone_more_positive_than_anthropic(self):
        """OpenAI (pays) should be covered more positively than Anthropic (neutral)."""
        openai_tone = self.verge.get('openai_coverage_tone', '')
        anthropic_tone = self.verge.get('anthropic_coverage_tone', '')
        # OpenAI should be balanced or positive, Anthropic neutral
        positive_tones = ['balanced', 'neutral_to_positive', 'positive']
        assert any(t in openai_tone for t in positive_tones)
        assert anthropic_tone == 'neutral'

    def test_meta_tone_more_negative_than_anthropic(self):
        """Meta (threatens) should be covered more negatively than Anthropic (neutral)."""
        meta_tone = self.verge.get('meta_coverage_tone', '')
        anthropic_tone = self.verge.get('anthropic_coverage_tone', '')
        assert 'adversarial' in meta_tone
        assert anthropic_tone == 'neutral'

    def test_three_tier_predicts_all_tones(self):
        """All three tier predictions should be consistent with actual tones."""
        openai = self.verge.get('openai_coverage_tone', '')
        anthropic = self.verge.get('anthropic_coverage_tone', '')
        meta = self.verge.get('meta_coverage_tone', '')
        # Ordering: meta most adversarial, anthropic neutral, openai softest
        assert 'adversarial' in meta
        assert anthropic == 'neutral'
        assert 'adversarial' not in openai


class TestVergeReporterLaneAssignment:
    """Verify reporter lane assignment extends to Anthropic coverage."""

    def setup_method(self):
        self.research = load_competitor_research()
        self.verge = self.research['publications']['the-verge']

    def test_lane_assignment_mechanism_documented(self):
        assert 'lane_assignment_mechanism' in self.verge

    def test_anthropic_lane_is_news_writer(self):
        """Anthropic should be covered by news writers, not investigators."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'Weatherbed' in comparison
        assert 'news writer' in comparison.lower()

    def test_meta_lane_is_adversarial_reporters(self):
        """Meta should be covered by adversarial-beat reporters."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'Alex Heath' in comparison or 'Heath' in comparison
        assert 'Hollister' in comparison or 'Sean Hollister' in comparison

    def test_openai_lane_is_enterprise_team(self):
        """OpenAI should be covered by enterprise/constructive reporters."""
        comparison = self.verge['rogue_ai_safety_comparison']
        assert 'Hayden Field' in comparison or 'Tom Warren' in comparison


class TestAsymmetryVerdictUpdated:
    """Verify the asymmetry verdict was updated with Aug 6 findings."""

    def setup_method(self):
        self.research = load_competitor_research()
        self.verge = self.research['publications']['the-verge']

    def test_verdict_updated_aug6(self):
        verdict = self.verge['asymmetry_verdict']
        assert 'Aug 6, 2026' in verdict or 'Aug 6' in verdict

    def test_verdict_mentions_three_tier(self):
        verdict = self.verge['asymmetry_verdict']
        assert 'THREE-TIER' in verdict or 'three-tier' in verdict.lower()

    def test_verdict_mentions_accidentally_paradox(self):
        verdict = self.verge['asymmetry_verdict']
        assert 'Accidentally' in verdict or 'accidentally' in verdict

    def test_verdict_mentions_anthropic(self):
        verdict = self.verge['asymmetry_verdict']
        assert 'Anthropic' in verdict

    def test_verdict_correlation_claim(self):
        """Verdict should state financial relationship predicts editorial temperature."""
        verdict = self.verge['asymmetry_verdict']
        assert 'correlation' in verdict.lower() or 'predict' in verdict.lower()


class TestAnthropicEntityExists:
    """Verify Anthropic entity is properly defined in competitor-entities.yaml."""

    def setup_method(self):
        self.entities = load_competitor_entities()

    def test_anthropic_entity_exists(self):
        assert 'anthropic' in self.entities['entities']

    def test_anthropic_has_no_publisher_deals(self):
        """Anthropic should have zero voluntary publisher content licensing deals."""
        anthropic = self.entities['entities']['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in note or 'zero' in note.lower()

    def test_anthropic_settlement_documented(self):
        """Anthropic's $1.5B author copyright settlement should be documented."""
        anthropic = self.entities['entities']['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        assert '1.5' in note or 'settlement' in note.lower()
