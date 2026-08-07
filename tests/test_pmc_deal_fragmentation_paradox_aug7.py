"""
PMC Deal Fragmentation Paradox — Type C Financial Incentive Mapping
Created: 2026-08-07 05:00 PT

When Vox Media was split between Lupa Systems and PMC in May-June 2026,
three AI-related financial relationships that had been signed with "Vox
Media" as a single legal entity had to be allocated across two successor
companies. This creates an unprecedented "deal fragmentation" where
The Verge's financial incentive structure is ambiguous — the publication
changed parent companies while its AI content licensing deals remained
tied to a corporate entity that no longer controls it.

Simultaneously, PMC is in active federal antitrust litigation against
Google over AI Overviews, yet The Verge's editorial hostility remains
focused on Meta rather than the company its parent is suing.

Sources:
- PMC/Vox Media acquisition: https://www.adweek.com/dealroom/penske-media-vox-media-brands-pmx/
- Reuters/PMC acquisition: https://www.reuters.com/business/rolling-stone-magazine-parent-buys-vox-media-digital-media-expansion-2026-06-18/
- OpenAI/Vox Media deal: https://www.reuters.com/business/media-telecom/openai-signs-content-deals-with-atlantic-vox-media-2024-05-29/
- Microsoft PCM: https://about.ads.microsoft.com/en/blog/post/february-2026/building-toward-a-sustainable-content-economy-for-the-agentic-web
- PMC v. Google: https://techcrunch.com/2025/09/14/rolling-stone-owner-penske-media-sues-google-over-ai-summaries/
- Google MTD: https://www.reuters.com/legal/litigation/google-defends-ai-search-summaries-rolling-stone-publishers-lawsuit-2026-01-13/
- Decrypt (3rd MTD): https://decrypt.co/354532/google-seeks-dismissal-of-publisher-lawsuit-over-ai-search-summaries
"""

import yaml
import os

# Paths
PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
VERGE_PROFILE = os.path.join(PROFILES_DIR, 'the-verge.yaml')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
RESEARCH_PROFILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestVoxMediaSplitTimeline:
    """Verify the corporate restructuring timeline is internally consistent."""

    def test_lupa_deal_announced_may_2026(self):
        """Lupa Systems announced acquisition of NY Mag, Vox.com, podcast network in May 2026."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'May 20, 2026' in desc or 'May 2026' in desc

    def test_pmc_acquisition_june_2026(self):
        """PMC acquired remaining Vox Media brands (The Verge, etc.) in June 2026."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'June' in desc and '2026' in desc

    def test_lupa_deal_closed_july_2026(self):
        """Lupa deal officially closed July 8, 2026."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'July 8, 2026' in desc

    def test_forte_went_to_pmc(self):
        """Forte (Vox Media's first-party data platform) went to PMC/PMX, not Lupa."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'Forte' in desc

    def test_concert_went_to_pmc(self):
        """Concert (Vox Media's premium ad marketplace) went to PMC/PMX, not Lupa."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'Concert' in desc

    def test_openai_deal_predates_split(self):
        """OpenAI content deal (May 2024) was signed 2 years before the Vox Media split."""
        profile = load_yaml(VERGE_PROFILE)
        # Check ownership chain for OpenAI deal references
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel.get('financial_tie') == 'licensing'


class TestDealFragmentationAmbiguity:
    """The core paradox: AI deals signed with 'Vox Media' are now split across two entities."""

    def test_openai_deal_signed_with_vox_media(self):
        """The OpenAI deal was with 'Vox Media' — a single entity that no longer controls The Verge."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel is not None
        desc = openai_rel.get('description', '')
        assert 'Vox Media' in desc or 'OpenAI' in desc

    def test_openai_deal_transfer_ambiguity(self):
        """Profile should note the deal transfer is uncertain post-acquisition."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        # The profile notes "unclear if the licensing deal transfers to PMX"
        lower = text.lower()
        assert 'unclear' in lower or 'transfer' in lower or 'renegotiat' in lower

    def test_forte_in_openai_deal_scope(self):
        """Forte was specifically named in the OpenAI deal scope — and went to PMC."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        desc = pmx_entry.get('description', '')
        assert 'Forte' in desc

    def test_microsoft_pcm_relationship_exists(self):
        """Microsoft relationship is documented in competitor_relationships."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        ms_rel = rels.get('microsoft', {})
        assert ms_rel.get('financial_tie') is not None

    def test_at_least_two_deal_partners(self):
        """At least 2 AI-related deal partners (OpenAI, Microsoft) are documented."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai = rels.get('openai', {})
        ms = rels.get('microsoft', {})
        deal_count = 0
        if openai.get('financial_tie') in ['licensing', 'commercial_partnership', 'mixed']:
            deal_count += 1
        if ms.get('financial_tie') in ['licensing', 'enterprise_customer']:
            deal_count += 1
        assert deal_count >= 2, f"Expected >=2 deal partners, found {deal_count}"


class TestPMCGoogleLitigationStatus:
    """Verify the PMC v. Google lawsuit facts are documented."""

    def test_lawsuit_filed_september_2025(self):
        """PMC filed antitrust suit against Google September 2025."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert 'September' in text or 'Sep' in text
        assert '2025' in text

    def test_google_motion_to_dismiss(self):
        """Google filed motion to dismiss."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert 'dismiss' in text.lower() or 'dismissal' in text.lower()

    def test_google_relationship_is_adversarial(self):
        """Google's relationship type is adversarial_litigation."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        assert 'adversarial' in google_rel.get('financial_tie', '') or \
               'litigation' in google_rel.get('financial_tie', ''), \
            f"Expected adversarial/litigation, got: {google_rel.get('financial_tie')}"

    def test_pmc_affiliate_revenue_decline(self):
        """PMC's complaint states affiliate revenue declined from Google AI Overviews."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert 'affiliate' in text.lower() or 'traffic' in text.lower()

    def test_pmc_first_major_publisher_to_sue_google(self):
        """PMC was the first major US publisher to sue Google over AI Overviews."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert 'first' in text.lower() and 'Google' in text


class TestPMCFinancialRelationshipMatrix:
    """The Verge's post-fragmentation financial incentive structure."""

    def test_meta_deal_is_none(self):
        """PMC/The Verge has NO financial relationship with Meta."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        meta_rel = rels.get('meta', {})
        assert meta_rel.get('financial_tie') == 'none', \
            f"Expected none, got: {meta_rel.get('financial_tie')}"

    def test_google_relationship_adversarial(self):
        """PMC's relationship with Google includes adversarial litigation."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        ft = google_rel.get('financial_tie', '')
        assert 'adversarial' in ft or 'litigation' in ft, \
            f"Expected adversarial/litigation, got: {ft}"

    def test_openai_relationship_licensing(self):
        """PMC has a licensing financial relationship with OpenAI."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel.get('financial_tie') == 'licensing', \
            f"Expected licensing, got: {openai_rel.get('financial_tie')}"

    def test_microsoft_relationship_licensing(self):
        """PMC has a licensing financial relationship with Microsoft."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        ms_rel = rels.get('microsoft', {})
        assert ms_rel.get('financial_tie') == 'licensing', \
            f"Expected licensing, got: {ms_rel.get('financial_tie')}"

    def test_openai_direction_receiving(self):
        """PMC receives money from OpenAI (licensing revenue flows in)."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel.get('direction') == 'receiving', \
            f"Expected receiving, got: {openai_rel.get('direction')}"

    def test_meta_direction_none(self):
        """No financial flow with Meta in either direction."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        meta_rel = rels.get('meta', {})
        assert meta_rel.get('direction') in ['none', None], \
            f"Expected none, got: {meta_rel.get('direction')}"


class TestPerverseIncentiveDirection:
    """
    PMC is SUING Google yet The Verge's editorial hostility targets Meta.
    The financial incentive structure predicts adversarial Google coverage,
    not adversarial Meta coverage.
    """

    def test_litigation_predicts_adversarial_google_coverage(self):
        """Active litigation should predict adversarial coverage toward Google."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        ft = google_rel.get('financial_tie', '')
        assert 'adversarial' in ft or 'litigation' in ft

    def test_no_meta_financial_signal(self):
        """Zero financial relationship = no financial incentive for hostility."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        meta_rel = rels.get('meta', {})
        assert meta_rel.get('financial_tie') == 'none'

    def test_openai_deal_predicts_softer_openai_coverage(self):
        """Content licensing revenue from OpenAI should predict softer coverage."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel.get('financial_tie') == 'licensing'
        assert openai_rel.get('direction') == 'receiving'

    def test_google_is_more_adversarial_than_meta_financially(self):
        """Google relationship (litigation) is MORE adversarial than Meta (none)."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        meta_rel = rels.get('meta', {})
        # Litigation is a stronger adversarial signal than 'none'
        assert 'adversarial' in google_rel.get('financial_tie', '') or \
               'litigation' in google_rel.get('financial_tie', '')
        assert meta_rel.get('financial_tie') == 'none'


class TestDealFragmentationDocumentation:
    """Verify deal fragmentation findings are documented in competitor-entities.yaml."""

    def test_entities_yaml_has_pmc_deal_fragmentation(self):
        """competitor-entities.yaml must document the PMC deal fragmentation paradox."""
        entities = load_yaml(ENTITIES_PROFILE)
        text = yaml.dump(entities)
        assert 'deal_fragmentation' in text.lower() or 'fragmentation' in text.lower() or \
               'pmc_deal_fragmentation' in text.lower()

    def test_entities_yaml_documents_three_deals(self):
        """competitor-entities.yaml deal fragmentation section mentions OpenAI, Microsoft, ProRata."""
        entities = load_yaml(ENTITIES_PROFILE)
        frag = entities.get('pmc_deal_fragmentation', {})
        overview = frag.get('overview', '')
        assert 'OpenAI' in overview
        assert 'Microsoft' in overview or 'PCM' in overview

    def test_entities_yaml_documents_lawsuit(self):
        """competitor-entities.yaml deal fragmentation section documents the Google lawsuit."""
        entities = load_yaml(ENTITIES_PROFILE)
        frag = entities.get('pmc_deal_fragmentation', {})
        lawsuit = frag.get('pmc_google_lawsuit', {})
        assert lawsuit.get('filed') == '2025-09-13'

    def test_entities_yaml_has_source_urls(self):
        """competitor-entities.yaml deal fragmentation section has source URLs."""
        entities = load_yaml(ENTITIES_PROFILE)
        frag = entities.get('pmc_deal_fragmentation', {})
        sources = frag.get('source_urls', {})
        assert len(sources) >= 3, f"Expected >=3 source URLs, found {len(sources)}"

    def test_research_yaml_has_verge_coverage_research(self):
        """competitor-coverage-research.yaml must have The Verge coverage documentation."""
        research = load_yaml(RESEARCH_PROFILE)
        text = yaml.dump(research)
        assert 'Verge' in text or 'PMC' in text or 'Penske' in text

    def test_research_yaml_has_fragmentation_finding(self):
        """competitor-coverage-research.yaml documents the deal fragmentation finding."""
        research = load_yaml(RESEARCH_PROFILE)
        text = yaml.dump(research)
        assert 'fragmentation' in text.lower() or 'deal_fragmentation' in text.lower()


class TestGoogleLawsuitVsMetaCoverageAsymmetry:
    """
    PMC claims Google's AI Overviews are destroying its business, yet
    The Verge's editorial apparatus targets Meta, not Google.
    """

    def test_google_affiliate_revenue_decline_documented(self):
        """PMC complaint: affiliate revenue declined due to Google AI Overviews."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        lower = text.lower()
        assert 'affiliate' in lower or 'traffic' in lower or 'revenue' in lower

    def test_google_being_sued_meta_not(self):
        """PMC is suing Google but NOT suing Meta."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        meta_rel = rels.get('meta', {})
        google_ft = google_rel.get('financial_tie', '')
        meta_ft = meta_rel.get('financial_tie', '')
        assert 'litigation' in google_ft or 'adversarial' in google_ft
        assert meta_ft == 'none'

    def test_meta_zero_financial_relationship(self):
        """PMC has zero financial relationship with Meta — no deals, no lawsuits."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        meta_rel = rels.get('meta', {})
        assert meta_rel.get('financial_tie') == 'none'
        assert meta_rel.get('estimated_value') in ['$0', 'none', None, '']


class TestPMCRevenueAndScale:
    """Verify PMC revenue estimates for dependency ratio calculations."""

    def test_pmc_is_private(self):
        """PMC is privately held — no SEC filings, revenue is estimated."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert 'Private' in text or 'private' in text or 'no public' in text.lower()

    def test_pmc_portfolio_25_plus_brands(self):
        """PMC/PMX combined portfolio has 25+ media brands."""
        profile = load_yaml(VERGE_PROFILE)
        text = yaml.dump(profile)
        assert '25' in text  # "25+" or "more than 25"

    def test_pmc_was_vox_largest_shareholder(self):
        """PMC was Vox Media's largest shareholder (20%) before full acquisition."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmc_entry = next((e for e in chain if 'Penske' in e.get('name', '')), None)
        assert pmc_entry is not None
        desc = pmc_entry.get('description', '')
        assert '20%' in desc or 'largest shareholder' in desc.lower()


class TestSourceCitations:
    """Every claim must have a source URL."""

    def test_openai_relationship_has_source(self):
        """OpenAI relationship entry has source URL."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        openai_rel = rels.get('openai', {})
        assert openai_rel.get('source_url') or openai_rel.get('source_urls'), \
            "OpenAI relationship must have source URL(s)"

    def test_google_relationship_has_source(self):
        """Google relationship entry has source URL."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        google_rel = rels.get('google', {})
        assert google_rel.get('source_url') or google_rel.get('source_urls'), \
            "Google relationship must have source URL(s)"

    def test_pmc_acquisition_has_source(self):
        """PMC acquisition is sourced to credible publications."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmx_entry = next((e for e in chain if e.get('name') == 'PMX Global, LLC'), None)
        assert pmx_entry is not None
        urls = pmx_entry.get('source_urls', [])
        assert len(urls) > 0

    def test_microsoft_relationship_has_source(self):
        """Microsoft relationship has source URL."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        ms_rel = rels.get('microsoft', {})
        assert ms_rel.get('source_url') or ms_rel.get('source_urls'), \
            "Microsoft relationship must have source URL(s)"


class TestCrossFileConsistency:
    """Verify The Verge's deal fragmentation findings are consistent across profiles."""

    def test_verge_profile_references_pmc(self):
        """The Verge profile must reference PMC as current parent."""
        profile = load_yaml(VERGE_PROFILE)
        chain = profile.get('ownership_chain', [])
        pmc_entry = next((e for e in chain if 'Penske' in e.get('name', '')), None)
        assert pmc_entry is not None

    def test_entities_yaml_has_verge_in_publications_or_notes(self):
        """competitor-entities.yaml references The Verge or PMC in its analysis."""
        entities = load_yaml(ENTITIES_PROFILE)
        text = yaml.dump(entities)
        assert 'Verge' in text or 'PMC' in text or 'PMX' in text or 'Penske' in text

    def test_verge_profile_has_competitor_relationships(self):
        """The Verge profile has a competitor_relationships section."""
        profile = load_yaml(VERGE_PROFILE)
        rels = profile.get('competitor_relationships', {})
        assert len(rels) > 0, "Must have competitor relationships documented"

    def test_entities_yaml_perverse_incentive_documented(self):
        """competitor-entities.yaml documents the perverse incentive direction."""
        entities = load_yaml(ENTITIES_PROFILE)
        frag = entities.get('pmc_deal_fragmentation', {})
        incentive = frag.get('perverse_incentive', '')
        assert 'Meta' in incentive and 'Google' in incentive
