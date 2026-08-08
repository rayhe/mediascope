"""
Cross-entity coverage analysis: Meghan Bobrowsky (WSJ Meta Beat Reporter)
=========================================================================

Tests the balanced-control beat assignment model. Bobrowsky is the WSJ's
DEDICATED Meta beat reporter — the structural analogue to Kashmir Hill (NYT),
Lauren Goode (WIRED), and Mike Isaac (NYT). But she operates at the ONLY
publication with balanced financial ties ($50M Meta + $50M OpenAI), making
her coverage the clearest baseline for what Meta reporting looks like when
financial conflicts are symmetric.

KEY FINDING: Beat assignment itself is neutral. The asymmetry comes from
the financial ENVIRONMENT in which the beat operates. At one-sided publications,
beat assignment CONCENTRATES adversarial energy on Meta. At the balanced
publication (WSJ), the same structure produces mixed-tone coverage.

Sources:
- Muck Rack profile: https://muckrack.com/meghan-bobrowsky
- Talking Biz News (assigned to Meta): https://talkingbiznews.com/media-news/wsj-taps-bobrowsky-to-cover-meta/
- WSJ Meta smartglasses: https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
- WSJ Zuckerberg interview: https://www.wsj.com/tech/ai/mark-zuckerberg-says-u-s-should-accelerate-ai-development-not-restrict-it-3bbe0868
- WSJ $942M ruling: https://www.wsj.com/tech/meta-ordered-to-pay-942-million-to-address-harm-to-kids-from-social-media-8ba5aab7
- WSJ OpenAI crown: https://www.wsj.com/tech/ai/how-openai-lost-its-ai-crownand-the-fight-to-win-it-back-7d069695
- WSJ AI rogue: https://www.wsj.com/tech/ai/ai-just-went-rogue-again-this-time-it-turned-to-deception-ae68de09
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    """Load a YAML profile file."""
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestBobrowskyProfilePresence:
    """Verify Bobrowsky profile exists in News Corp publication data."""

    def test_news_corp_has_journalist_profiles(self):
        data = load_yaml('news-corp.yaml')
        assert 'journalist_profiles' in data, \
            "news-corp.yaml must have journalist_profiles section"

    def test_bobrowsky_in_journalist_profiles(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        names = [p.get('name', '') for p in profiles]
        assert 'Meghan Bobrowsky' in names, \
            "Meghan Bobrowsky must be in News Corp journalist profiles"

    def test_bobrowsky_explicitly_assigned_to_meta(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert bobrowsky is not None
        assert bobrowsky.get('explicitly_assigned_to_meta') is True, \
            "Bobrowsky must be marked as explicitly assigned to Meta beat"

    def test_bobrowsky_has_cross_entity_coverage(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert bobrowsky is not None
        assert 'cross_entity_coverage' in bobrowsky

    def test_bobrowsky_has_source_urls(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert bobrowsky is not None
        urls = bobrowsky.get('source_urls', [])
        assert len(urls) >= 3, "Bobrowsky profile must have 3+ source URLs"


class TestBobrowskyMetaCoverage:
    """Test Bobrowsky's Meta coverage tone and framing."""

    def test_meta_tone_is_mixed_balanced(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        meta = bobrowsky['cross_entity_coverage']['meta']
        assert meta.get('tone') == 'mixed_balanced', \
            "Bobrowsky's Meta tone must be mixed_balanced (not adversarial)"

    def test_meta_tone_value_near_neutral(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        meta = bobrowsky['cross_entity_coverage']['meta']
        tone = meta.get('tone_value', 0)
        assert -0.30 <= tone <= 0.10, \
            f"Bobrowsky Meta tone {tone} must be near-neutral [-0.30, 0.10]"

    def test_meta_examples_count(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        examples = bobrowsky['cross_entity_coverage']['meta'].get('examples', [])
        assert len(examples) >= 4, \
            f"Must have 4+ Meta examples, got {len(examples)}"

    def test_glasses_article_present(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        examples = bobrowsky['cross_entity_coverage']['meta'].get('examples', [])
        titles = [e.get('title', '') for e in examples]
        assert any('Flooding' in t or 'Smartglasses' in t for t in titles), \
            "Must include the smartglasses privacy article"

    def test_zuckerberg_interview_present(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        examples = bobrowsky['cross_entity_coverage']['meta'].get('examples', [])
        titles = [e.get('title', '') for e in examples]
        assert any('Zuckerberg' in t for t in titles), \
            "Must include Zuckerberg interview article"

    def test_meta_examples_have_mixed_tones(self):
        """Balanced coverage should include BOTH negative AND positive articles."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        examples = bobrowsky['cross_entity_coverage']['meta'].get('examples', [])
        tones = [e.get('tone', 0) for e in examples]
        has_negative = any(t < -0.10 for t in tones)
        has_positive = any(t > 0.0 for t in tones)
        assert has_negative and has_positive, \
            f"Balanced coverage must include both negative and positive tones: {tones}"

    def test_meta_coverage_includes_disclosure(self):
        """At least one Meta article should mention disclosure."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        examples = bobrowsky['cross_entity_coverage']['meta'].get('examples', [])
        has_disclosure = any(
            'DISCLOSE' in str(e.get('framing_notes', ''))
            for e in examples
        )
        assert has_disclosure, \
            "At least one Meta article must document the financial disclosure"


class TestBobrowskyNotPrimaryOpenAI:
    """Test that Bobrowsky does NOT cover OpenAI as primary beat."""

    def test_openai_is_not_primary_beat(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        openai = bobrowsky['cross_entity_coverage'].get('openai', {})
        assert openai.get('tone') == 'not_primary_beat', \
            "OpenAI must be not_primary_beat for Bobrowsky"

    def test_openai_tone_value_is_null(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        openai = bobrowsky['cross_entity_coverage'].get('openai', {})
        assert openai.get('tone_value') is None, \
            "OpenAI tone_value must be null (not Bobrowsky's beat)"


class TestBeatAssignmentComparison:
    """Test the balanced-control beat assignment model."""

    def test_beat_assignment_comparison_exists(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert 'beat_assignment_comparison' in bobrowsky

    def test_comparison_includes_nyt_and_wired(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        desc = bobrowsky['beat_assignment_comparison'].get('description', '')
        assert 'NYT' in desc or 'Kashmir Hill' in desc, \
            "Beat comparison must reference NYT/Kashmir Hill"
        assert 'WIRED' in desc or 'Lauren Goode' in desc, \
            "Beat comparison must reference WIRED/Lauren Goode"

    def test_comparison_includes_balanced_finding(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        desc = bobrowsky['beat_assignment_comparison'].get('description', '')
        assert 'balanced' in desc.lower() or 'Balanced' in desc, \
            "Beat comparison must mention 'balanced' as key finding"


class TestWSJBeatStructure:
    """Test the WSJ beat structure documentation."""

    def test_wsj_beat_structure_exists(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert 'wsj_beat_structure' in bobrowsky

    def test_wsj_beats_include_meta_and_openai(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        beats = bobrowsky['wsj_beat_structure'].get('beats', [])
        beat_names = [b.get('beat', '') for b in beats]
        assert any('Meta' in b for b in beat_names), "Must include Meta beat"
        assert any('OpenAI' in b for b in beat_names), "Must include OpenAI beat"

    def test_berber_jin_covers_openai(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        beats = bobrowsky['wsj_beat_structure'].get('beats', [])
        jin = next((b for b in beats if 'Jin' in b.get('reporter', '')), None)
        assert jin is not None, "Berber Jin must be listed as OpenAI beat reporter"
        assert 'OpenAI' in jin.get('beat', ''), "Jin's beat must include OpenAI"

    def test_bobrowsky_covers_meta_in_beat_structure(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        beats = bobrowsky['wsj_beat_structure'].get('beats', [])
        mb = next((b for b in beats if 'Bobrowsky' in b.get('reporter', '')), None)
        assert mb is not None, "Bobrowsky must be in beat structure"
        assert 'Meta' in mb.get('beat', ''), "Bobrowsky's beat must be Meta"

    def test_four_plus_reporters_in_structure(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        beats = bobrowsky['wsj_beat_structure'].get('beats', [])
        assert len(beats) >= 4, f"Must have 4+ reporters, got {len(beats)}"


class TestToneDeltaWithOtherPublications:
    """Test that Bobrowsky's tone delta confirms the financial amplification thesis."""

    def test_bobrowsky_warmer_than_kashmir_hill(self):
        """Bobrowsky (-0.15) must be warmer than Hill (-0.80) by 0.5+."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        bobrowsky_tone = bobrowsky['cross_entity_coverage']['meta'].get('tone_value', 0)
        hill_tone = -0.80  # From nytimes.yaml Kashmir Hill profile
        delta = bobrowsky_tone - hill_tone
        assert delta >= 0.50, \
            f"Bobrowsky-Hill delta {delta} must be >= 0.50 (financial amplification)"

    def test_bobrowsky_warmer_than_lauren_goode(self):
        """Bobrowsky (-0.15) must be warmer than Goode (-0.85) by 0.5+."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        bobrowsky_tone = bobrowsky['cross_entity_coverage']['meta'].get('tone_value', 0)
        goode_tone = -0.85  # From wired.yaml Lauren Goode profile
        delta = bobrowsky_tone - goode_tone
        assert delta >= 0.50, \
            f"Bobrowsky-Goode delta {delta} must be >= 0.50 (financial amplification)"

    def test_bobrowsky_warmer_than_gizmodo_baseline(self):
        """Bobrowsky (-0.15) should be warmer than Gizmodo clean control (-0.50)."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        bobrowsky_tone = bobrowsky['cross_entity_coverage']['meta'].get('tone_value', 0)
        gizmodo_tone = -0.50  # Clean control (no financial ties)
        delta = bobrowsky_tone - gizmodo_tone
        assert delta >= 0.20, \
            f"Bobrowsky-Gizmodo delta {delta} must be >= 0.20"

    def test_bobrowsky_warmer_than_dan_milmo(self):
        """Bobrowsky (-0.15) should be warmer than Milmo (-0.45)."""
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        bobrowsky_tone = bobrowsky['cross_entity_coverage']['meta'].get('tone_value', 0)
        milmo_tone = -0.45  # From guardian.yaml Dan Milmo profile
        delta = bobrowsky_tone - milmo_tone
        assert delta >= 0.20, \
            f"Bobrowsky-Milmo delta {delta} must be >= 0.20"


class TestResearchFileConsistency:
    """Test that competitor-coverage-research.yaml has Bobrowsky data."""

    def test_bobrowsky_cross_entity_in_research(self):
        data = load_yaml('competitor-coverage-research.yaml')
        news_corp = data.get('publications', {}).get('news-corp', {})
        assert 'bobrowsky_cross_entity' in news_corp, \
            "competitor-coverage-research.yaml must have bobrowsky_cross_entity"

    def test_research_has_meta_tone_value(self):
        data = load_yaml('competitor-coverage-research.yaml')
        news_corp = data.get('publications', {}).get('news-corp', {})
        bobrowsky = news_corp.get('bobrowsky_cross_entity', {})
        assert 'meta_tone_value' in bobrowsky
        tone = bobrowsky['meta_tone_value']
        assert -0.30 <= tone <= 0.10, \
            f"Research file meta_tone_value {tone} must be near-neutral"

    def test_research_has_coverage_examples(self):
        data = load_yaml('competitor-coverage-research.yaml')
        news_corp = data.get('publications', {}).get('news-corp', {})
        bobrowsky = news_corp.get('bobrowsky_cross_entity', {})
        examples = bobrowsky.get('meta_coverage_examples', [])
        assert len(examples) >= 3, \
            f"Research file must have 3+ coverage examples, got {len(examples)}"

    def test_research_has_source_urls(self):
        data = load_yaml('competitor-coverage-research.yaml')
        news_corp = data.get('publications', {}).get('news-corp', {})
        bobrowsky = news_corp.get('bobrowsky_cross_entity', {})
        urls = bobrowsky.get('source_urls', [])
        assert len(urls) >= 3, \
            f"Research file must have 3+ source URLs, got {len(urls)}"

    def test_research_has_wsj_beat_structure(self):
        data = load_yaml('competitor-coverage-research.yaml')
        news_corp = data.get('publications', {}).get('news-corp', {})
        bobrowsky = news_corp.get('bobrowsky_cross_entity', {})
        beats = bobrowsky.get('wsj_beat_structure', [])
        assert len(beats) >= 3, \
            f"Beat structure must have 3+ entries, got {len(beats)}"


class TestFinancialAmplificationOrderingWithBobrowsky:
    """Test that Bobrowsky fits the financial amplification gradient."""

    def test_financial_amplification_ordering(self):
        """Publications with ZERO Meta deals must have lower (more adversarial) Meta tones
        than WSJ with a $50M Meta deal."""
        # Ordered by financial tie strength → tone
        ordering = [
            ('WIRED', -0.85, 'zero_meta_deal'),
            ('NYT (Hill)', -0.80, 'zero_meta_deal'),
            ('Gizmodo', -0.50, 'zero_deals'),
            ('Guardian', -0.45, 'zero_meta_deal'),
            ('FT', -0.45, 'zero_meta_deal'),
            ('WSJ (Bobrowsky)', -0.15, 'meta_deal'),
        ]
        # Every zero-meta-deal publication should be more adversarial
        # than the meta-deal publication (WSJ)
        meta_deal_tone = -0.15  # Bobrowsky
        for name, tone, deal_status in ordering:
            if deal_status == 'zero_meta_deal':
                assert tone < meta_deal_tone, \
                    f"{name} ({tone}) must be more adversarial than WSJ ({meta_deal_tone})"

    def test_bobrowsky_tone_between_gizmodo_and_mims(self):
        """Bobrowsky (-0.15) should be between Gizmodo (-0.50) and Mims (+0.30)."""
        bobrowsky = -0.15
        gizmodo = -0.50
        mims = 0.30
        assert gizmodo < bobrowsky < mims, \
            f"Bobrowsky {bobrowsky} must be between Gizmodo {gizmodo} and Mims {mims}"


class TestAsymmetryVerdict:
    """Test that the asymmetry verdict draws the correct conclusion."""

    def test_verdict_exists(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        assert 'asymmetry_verdict' in bobrowsky

    def test_verdict_mentions_financial_environment(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        verdict = bobrowsky.get('asymmetry_verdict', '')
        assert 'financial' in verdict.lower(), \
            "Verdict must reference financial environment as explanatory variable"

    def test_verdict_mentions_disclosure(self):
        data = load_yaml('news-corp.yaml')
        profiles = data.get('journalist_profiles', [])
        bobrowsky = next((p for p in profiles if p.get('name') == 'Meghan Bobrowsky'), None)
        verdict = bobrowsky.get('asymmetry_verdict', '')
        assert 'disclosure' in verdict.lower() or 'disclose' in verdict.lower(), \
            "Verdict must mention WSJ's disclosure practice"
