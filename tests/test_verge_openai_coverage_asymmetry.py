"""
Type A: Competitor Coverage Deep Dive — The Verge (PMC) × OpenAI
================================================================

Tests the institutional coverage asymmetry between The Verge's treatment of
OpenAI (content licensing deal partner, $0 from Meta) vs Meta ($0 deal).

Key finding: The Verge uses a multi-lane reporter system that assigns OpenAI
to enterprise-scoop reporters (product launches, competitive framing) and Meta
to multiple adversarial beats (privacy alarm, regulatory pressure, consumer
harm, subscription criticism). The dedicated wearables reviewer (Victoria Song)
is actually balanced, but institutional framing is set by editorial commentary
and non-product beat reporters.

The io device paradox is the strongest evidence: OpenAI's $6.5B Jony Ive
acquisition will produce a camera-equipped AI wearable device (directly
competing with Meta glasses), yet received ZERO pre-emptive privacy alarm
from The Verge, while Meta's single-camera glasses get activist-backlash
framing.

Sources:
- Techmeme: https://www.techmeme.com/251021/p33 (Hayden Field, ChatGPT Atlas)
- Techmeme: https://www.techmeme.com/250709/p35 (Hayden Field, io acquisition)
- Techmeme: https://www.techmeme.com/250724/p36 (Tom Warren, GPT-5 launch)
- Muck Rack: https://muckrack.com/victoria-song/articles (Song coverage arc)
- AIVAnet reprint: https://www.aivanet.com/2026/07/with-smart-glasses-meta-holds-all-the-cards-but-fails-to-play-them-well/
- Reuters: https://www.reuters.com/technology/openai-signs-content-deals-with-atlantic-vox-media-2024-05-29/
- 10up case study: https://10up.com/our-work/penske-media-ai-integration/ (Azure OpenAI enterprise)
"""

import yaml
import pytest
import os
import re


PROFILE_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_verge_profile():
    path = os.path.join(PROFILE_DIR, 'the-verge.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    path = os.path.join(PROFILE_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILE_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestFourLaneReporterSystem:
    """The Verge assigns different reporters to OpenAI vs Meta, creating
    systematic framing divergence comparable to WIRED's desk assignment
    and FT's within-reporter patterns."""

    def test_has_cross_entity_analysis(self):
        profile = load_verge_profile()
        assert 'cross_entity_coverage_analysis' in profile

    def test_identifies_openai_reporters(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        openai_section = analysis['openai_coverage']
        reporters = openai_section.get('primary_reporters', [])
        reporter_names = [r['name'] for r in reporters]
        # Hayden Field is the primary OpenAI reporter
        assert any('Hayden Field' in n for n in reporter_names)

    def test_identifies_meta_reporters(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        reporters = meta_section.get('adversarial_beat_reporters', [])
        reporter_names = [r['name'] for r in reporters]
        # Multiple reporters assigned to adversarial Meta beats
        assert len(reporter_names) >= 2

    def test_song_classified_as_balanced(self):
        """Victoria Song, the dedicated wearables reviewer, is balanced —
        the institutional adversarial tone comes from other reporters."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        song_note = meta_section.get('product_reviewer_note', '')
        assert 'balanced' in song_note.lower() or 'fair' in song_note.lower()

    def test_four_lane_mechanism_documented(self):
        """The Verge uses a four-lane system: enterprise scoops (OpenAI),
        product reviews (balanced), regulatory/policy (adversarial Meta),
        business investigations (adversarial Meta)."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        mechanism = analysis.get('lane_assignment_mechanism', '')
        assert 'lane' in mechanism.lower() or 'assignment' in mechanism.lower()


class TestOpenAICoverageArticles:
    """Specific OpenAI article examples showing constructive/neutral framing."""

    def test_has_openai_article_examples(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        openai_section = analysis['openai_coverage']
        examples = openai_section.get('article_examples', [])
        assert len(examples) >= 3

    def test_atlas_browser_product_framing(self):
        """ChatGPT Atlas: AI browser with 'browser memories' that tracks
        browsing data — reported as product feature, not surveillance."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        openai_section = analysis['openai_coverage']
        examples = openai_section.get('article_examples', [])
        atlas_articles = [e for e in examples if 'Atlas' in e.get('title', '')]
        assert len(atlas_articles) >= 1
        atlas = atlas_articles[0]
        # Should be neutral/positive framing
        assert atlas.get('tone', 0) >= -0.2

    def test_io_acquisition_no_privacy_alarm(self):
        """OpenAI's $6.5B Jony Ive acquisition — AI wearable device with
        cameras. ZERO pre-emptive privacy alarm from The Verge."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        openai_section = analysis['openai_coverage']
        examples = openai_section.get('article_examples', [])
        io_articles = [e for e in examples if 'io' in e.get('title', '').lower()
                       or 'ive' in e.get('title', '').lower()
                       or 'acquisition' in e.get('title', '').lower()]
        assert len(io_articles) >= 1
        io_art = io_articles[0]
        # No surveillance framing despite camera-equipped AI wearable
        assert io_art.get('surveillance_terms', 0) == 0

    def test_openai_no_sustained_investigation(self):
        """No sustained investigative campaign against OpenAI despite
        comparable privacy/safety concerns (hacking incidents, NDA scandal,
        data training practices)."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        openai_section = analysis['openai_coverage']
        assert 'no sustained investigative' in openai_section.get(
            'investigation_pattern', '').lower() or \
            'no sustained' in openai_section.get('coverage_pattern', '').lower()


class TestMetaInstitutionalCoverage:
    """Meta coverage articles showing adversarial institutional framing
    despite balanced product reviews."""

    def test_has_meta_institutional_examples(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        examples = meta_section.get('article_examples', [])
        assert len(examples) >= 3

    def test_activist_backlash_framing(self):
        """'Meta holds all the cards' opens with activist guerrilla ads
        calling glasses 'pervert technology' and 'mass surveillance
        predator glasses' — foregrounding opposition voices."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        examples = meta_section.get('article_examples', [])
        backlash_articles = [e for e in examples
                             if 'holds all the cards' in e.get('title', '').lower()
                             or 'pervert' in e.get('framing', '').lower()
                             or 'activist' in e.get('framing', '').lower()]
        assert len(backlash_articles) >= 1

    def test_subscription_paywall_adversarial(self):
        """Conversation Focus paywall story framed as consumer harm
        and disability/accessibility attack."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        examples = meta_section.get('article_examples', [])
        paywall_articles = [e for e in examples
                            if 'subscription' in e.get('title', '').lower()
                            or 'conversation focus' in e.get('title', '').lower()
                            or 'paywall' in e.get('framing', '').lower()]
        assert len(paywall_articles) >= 1

    def test_meta_more_adversarial_than_openai(self):
        """The Verge's institutional Meta tone is more adversarial
        than its OpenAI tone."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        meta_section = analysis['meta_institutional_coverage']
        openai_section = analysis['openai_coverage']
        meta_tone = meta_section.get('institutional_tone_score', 0)
        openai_tone = openai_section.get('tone_score', 0)
        assert meta_tone < openai_tone


class TestIoDeviceParadox:
    """The io device paradox: OpenAI's $6.5B Jony Ive acquisition will produce
    a camera-equipped AI wearable device (directly competing with Meta glasses),
    yet received ZERO pre-emptive privacy alarm while Meta's single-camera
    glasses get activist-backlash and surveillance framing."""

    def test_io_device_paradox_documented(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        paradox = analysis.get('io_device_paradox', {})
        assert paradox

    def test_io_zero_surveillance_terms(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        paradox = analysis.get('io_device_paradox', {})
        assert paradox.get('openai_io_surveillance_terms', -1) == 0

    def test_meta_nonzero_surveillance_terms(self):
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        paradox = analysis.get('io_device_paradox', {})
        assert paradox.get('meta_glasses_surveillance_terms', 0) > 0

    def test_both_have_cameras(self):
        """Both devices have cameras, yet only Meta gets surveillance framing."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        paradox = analysis.get('io_device_paradox', {})
        assert paradox.get('openai_io_has_cameras') is True
        assert paradox.get('meta_glasses_has_cameras') is True

    def test_financial_correlation(self):
        """OpenAI pays The Verge (licensing); Meta does not."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        paradox = analysis.get('io_device_paradox', {})
        financial = paradox.get('financial_correlation', '')
        assert 'openai' in financial.lower() and 'meta' in financial.lower()


class TestFinancialPredictsTone:
    """Financial relationships predict coverage tone at The Verge."""

    def test_openai_deal_exists(self):
        profile = load_verge_profile()
        relationships = profile.get('revenue_relationships', [])
        openai_deals = [r for r in relationships
                        if 'OpenAI' in r.get('partner', '')]
        assert len(openai_deals) >= 1

    def test_meta_deal_absent(self):
        """Meta has no AI content licensing deal with PMC/Vox Media."""
        profile = load_verge_profile()
        relationships = profile.get('revenue_relationships', [])
        meta_deals = [r for r in relationships
                      if r.get('partner', '') == 'Meta'
                      and r.get('relationship_type', '') == 'licensing']
        assert len(meta_deals) == 0

    def test_bilateral_openai_financial_flow(self):
        """PMC has money flowing BOTH directions with OpenAI ecosystem:
        receiving licensing fees AND paying for Azure OpenAI services."""
        profile = load_verge_profile()
        relationships = profile.get('revenue_relationships', [])
        openai_related = [r for r in relationships
                          if 'OpenAI' in r.get('partner', '')
                          or 'Azure' in r.get('partner', '')
                          or 'Microsoft' in r.get('partner', '')]
        # Should have both the licensing deal AND the Azure enterprise deal
        assert len(openai_related) >= 2

    def test_coverage_asymmetry_score(self):
        """The Verge covers Meta ~0.65+ points more negatively than OpenAI."""
        research = load_competitor_research()
        verge = research['publications']['the-verge']
        verdict = verge.get('asymmetry_verdict', '')
        # Should mention the tone delta
        assert '0.6' in verdict or '0.7' in verdict or '0.65' in verdict


class TestReporterAssignmentTaxonomy:
    """The Verge's four-lane system is now the FOURTH publication-level
    mechanism documented (after WIRED desk assignment, NYT between-reporter,
    FT within-reporter)."""

    def test_four_publication_mechanisms(self):
        """Four distinct lane assignment mechanisms now documented."""
        research = load_competitor_research()
        verge = research['publications']['the-verge']
        mechanism = verge.get('lane_assignment_mechanism', '')
        # Verge should document its mechanism
        assert 'four' in mechanism.lower() or 'multi' in mechanism.lower() or \
               'lane' in mechanism.lower()

    def test_mechanism_type_distinct(self):
        """Verge uses 'multi-beat' lane assignment — distinct from
        WIRED (desk), NYT (between-reporter), FT (within-reporter)."""
        research = load_competitor_research()
        verge = research['publications']['the-verge']
        mechanism = verge.get('lane_assignment_mechanism', '')
        # Should not be identical to other mechanisms
        assert 'multi' in mechanism.lower() or 'beat' in mechanism.lower()


class TestDisclosureGaps:
    """The Verge discloses its Google lawsuit ('Disclosure is our brand')
    but does NOT disclose OpenAI/Azure financial relationships."""

    def test_google_lawsuit_disclosed(self):
        profile = load_verge_profile()
        conflicts = profile.get('known_conflicts', [])
        litigation_conflicts = [c for c in conflicts
                                if c.get('type') == 'litigation']
        assert len(litigation_conflicts) >= 1

    def test_openai_deal_not_disclosed_in_coverage(self):
        """OpenAI content licensing deal not disclosed in Verge articles
        covering Meta AI or Meta vs OpenAI comparisons."""
        profile = load_verge_profile()
        conflicts = profile.get('known_conflicts', [])
        revenue_conflicts = [c for c in conflicts
                             if c.get('type') == 'revenue']
        assert len(revenue_conflicts) >= 1
        # Should note non-disclosure
        desc = revenue_conflicts[0].get('description', '').lower()
        assert 'not disclosed' in desc or 'no verge article' in desc or \
               'has disclosed' not in desc

    def test_azure_enterprise_not_disclosed(self):
        """Azure OpenAI enterprise agreement not disclosed."""
        profile = load_verge_profile()
        conflicts = profile.get('known_conflicts', [])
        azure_conflicts = [c for c in conflicts
                           if c.get('type') == 'azure_openai_enterprise']
        assert len(azure_conflicts) >= 1
        desc = azure_conflicts[0].get('description', '').lower()
        assert 'not disclosed' in desc

    def test_selective_disclosure_pattern(self):
        """The Verge selectively discloses: Google lawsuit (adversarial)
        yes, OpenAI deals (aligned) no. Disclosure only when adversarial."""
        profile = load_verge_profile()
        analysis = profile['cross_entity_coverage_analysis']
        disclosure = analysis.get('disclosure_pattern', '')
        assert 'selective' in disclosure.lower() or \
               'google' in disclosure.lower()
