"""
Test: Snap-Perplexity-Publisher Financial Chain (Mechanism #133)

Validates the financial chain mapping connecting Snap Inc. to publisher
coverage incentives through Perplexity, OpenAI, and historical Discover
revenue-sharing relationships.

Key finding: Snap sits at the intersection of at least THREE documented
financial flows connecting to Condé Nast (WIRED's parent), while Meta
has ZERO. The entity with MORE cameras (Snap, 4) and MORE publisher
financial ties receives ZERO privacy scrutiny; the entity with FEWER
cameras (Meta, 1) and ZERO ties receives alarm vocabulary.

Source: Snap Q2 2026 earnings (Reuters Aug 3), Snap-Perplexity $400M deal
(BestMediaInfo Q3 2025), Snap Discover PMP beta (MarTech 2018), OpenAI
My AI (SiliconANGLE Feb 2023), Perplexity publisher program (VarIndia 2026),
Lynch March 2026 CEO memo confirming Perplexity deal.
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


class TestSnapEntityFinancialData:
    """Verify Snap entity has required Q2 2026 financial data."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']

    def test_snap_entity_exists(self):
        assert 'snap' in self.entities['entities']

    def test_snap_has_q2_2026_earnings(self):
        assert 'q2_2026_earnings' in self.snap
        q2 = self.snap['q2_2026_earnings']
        assert q2['total_revenue_b'] == 1.60
        assert q2['revenue_yoy_pct'] == 19
        assert q2['dau_m'] == 493

    def test_snap_q2_north_america_dau_decline(self):
        """North America DAU declined 7% — platform shrinking in primary market."""
        q2 = self.snap['q2_2026_earnings']
        assert q2['north_america_dau_decline_pct'] == 7

    def test_snap_has_q1_2026_earnings(self):
        assert 'q1_2026_earnings' in self.snap
        q1 = self.snap['q1_2026_earnings']
        assert q1['mau_m'] == 956
        assert q1['dau_m'] == 483

    def test_snap_direct_revenue_milestone(self):
        """Snap direct revenue hit $1B ARR with 25M+ Snapchat+ subscribers."""
        q1 = self.snap['q1_2026_earnings']
        assert q1['direct_revenue_arr_b'] == 1.0
        assert q1['snapchat_plus_subscribers_m'] == 25

    def test_snap_has_q2_source_urls(self):
        q2 = self.snap['q2_2026_earnings']
        assert 'source_urls' in q2
        assert len(q2['source_urls']) >= 1


class TestSnapPerplexityDeal:
    """Verify Snap-Perplexity $400M deal documentation."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.perplexity = self.snap.get('ai_partnerships', {}).get('perplexity', {})

    def test_perplexity_deal_exists(self):
        assert 'ai_partnerships' in self.snap
        assert 'perplexity' in self.snap['ai_partnerships']

    def test_perplexity_deal_value(self):
        assert self.perplexity['value_m'] == 400

    def test_perplexity_deal_structure(self):
        assert self.perplexity['structure'] == 'cash + equity'

    def test_perplexity_financial_direction(self):
        """Perplexity pays Snap, not the other way around."""
        assert self.perplexity['financial_direction'] == 'Perplexity pays Snap'

    def test_perplexity_revenue_not_recognized(self):
        """Revenue NOT yet recognized as of Q1 2026."""
        status = self.perplexity['revenue_recognition_status']
        assert 'NOT' in status or 'not' in status

    def test_perplexity_publisher_chain_documented(self):
        """The chain Snap → Perplexity → Condé Nast must be documented."""
        chain = self.perplexity['perplexity_publisher_chain']
        assert 'Condé Nast' in chain or 'Conde Nast' in chain

    def test_perplexity_revenue_sharing_details(self):
        """Perplexity's $42.5M pool and 80% publisher share must be documented."""
        chain = self.perplexity['perplexity_publisher_chain']
        assert '42.5' in chain
        assert '80%' in chain

    def test_perplexity_deal_has_source_urls(self):
        assert 'source_urls' in self.perplexity
        assert len(self.perplexity['source_urls']) >= 1


class TestSnapOpenAIRelationship:
    """Verify Snap-OpenAI API customer relationship."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.openai = self.snap.get('ai_partnerships', {}).get('openai', {})

    def test_openai_partnership_exists(self):
        assert 'openai' in self.snap['ai_partnerships']

    def test_openai_relationship_type(self):
        """Snap is an API customer, not a content partner."""
        assert self.openai['type'] == 'api_customer'

    def test_openai_my_ai_product(self):
        assert 'My AI' in self.openai['product']

    def test_openai_launch_date(self):
        assert self.openai['launched'] == '2023-02-27'

    def test_openai_financial_direction(self):
        """Money flows FROM Snap TO OpenAI."""
        assert 'Snap pays OpenAI' in self.openai['financial_direction']

    def test_openai_child_safety_note(self):
        """Snap My AI had child safety issues — must be documented."""
        note = self.openai['note']
        assert 'child safety' in note.lower() or 'Washington Post' in note


class TestSnapDiscoverPublisherRelationship:
    """Verify Snap Discover platform revenue-sharing with publishers."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.publisher_rels = self.snap.get('publisher_financial_relationships', {})

    def test_discover_platform_documented(self):
        assert 'discover_platform' in self.publisher_rels

    def test_discover_revenue_sharing_type(self):
        discover = self.publisher_rels['discover_platform']
        assert discover['type'] == 'revenue_sharing'

    def test_conde_nast_discover_confirmed(self):
        """Condé Nast was a confirmed Snap Discover PMP partner."""
        discover = self.publisher_rels['discover_platform']
        assert discover['conde_nast_confirmed'] is True

    def test_meta_contrast_documented(self):
        """Meta has ZERO equivalent publisher platform relationships."""
        assert 'meta_contrast' in self.publisher_rels
        contrast = self.publisher_rels['meta_contrast']
        assert 'ZERO' in contrast or 'zero' in contrast.lower()


class TestSnapMetaFinancialContrast:
    """Verify the financial chain contrast between Snap and Meta."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']

    def test_snap_has_multiple_financial_connections(self):
        """Snap must have at least 3 documented financial connections to publishers."""
        connections = 0
        # Discover direct
        if self.snap.get('publisher_financial_relationships', {}).get('discover_platform'):
            connections += 1
        # Perplexity indirect
        if self.snap.get('ai_partnerships', {}).get('perplexity'):
            connections += 1
        # OpenAI indirect
        if self.snap.get('ai_partnerships', {}).get('openai'):
            connections += 1
        assert connections >= 3

    def test_snap_cameras_more_than_meta(self):
        """Snap Specs have MORE cameras than Meta Ray-Ban."""
        specs = self.snap['hardware_devices']['specs_consumer']
        assert specs['cameras']['total'] == 4

    def test_snap_privacy_scrutiny_zero(self):
        """Snap Specs received ZERO privacy scrutiny."""
        specs = self.snap['hardware_devices']['specs_consumer']
        assert specs['surveillance_framing_count'] == 0


class TestMechanism133Structure:
    """Verify mechanism #133 exists and has required structure."""

    def setup_method(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.mechanism = self._find_mechanism(133)

    def _find_mechanism(self, mech_id):
        """Search all sections for a mechanism by ID."""
        for top_key, top_val in self.research.items():
            if isinstance(top_val, dict):
                # Direct match
                if top_val.get('mechanism_id') == mech_id:
                    return top_val
                # Nested match
                for key, val in top_val.items():
                    if isinstance(val, dict):
                        if val.get('mechanism_id') == mech_id:
                            return val
                        # Double nested
                        for k2, v2 in val.items():
                            if isinstance(v2, dict) and v2.get('mechanism_id') == mech_id:
                                return v2
        return None

    def test_mechanism_133_exists(self):
        assert self.mechanism is not None, "Mechanism #133 not found in any section"

    def test_mechanism_133_has_finding_summary(self):
        assert 'finding_summary' in self.mechanism
        assert len(self.mechanism['finding_summary']) > 100

    def test_mechanism_133_has_confounders(self):
        assert 'confounders' in self.mechanism
        assert len(self.mechanism['confounders']) >= 3

    def test_mechanism_133_has_falsifiable_predictions(self):
        assert 'falsifiable_predictions' in self.mechanism
        assert len(self.mechanism['falsifiable_predictions']) >= 2

    def test_mechanism_133_has_source_urls(self):
        assert 'source_urls' in self.mechanism
        assert len(self.mechanism['source_urls']) >= 5


class TestMechanism133CrossReferences:
    """Verify mechanism #133 cross-references related mechanisms."""

    def setup_method(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.mechanism = self._find_mechanism(133)

    def _find_mechanism(self, mech_id):
        for top_key, top_val in self.research.items():
            if isinstance(top_val, dict):
                if top_val.get('mechanism_id') == mech_id:
                    return top_val
                for key, val in top_val.items():
                    if isinstance(val, dict):
                        if val.get('mechanism_id') == mech_id:
                            return val
                        for k2, v2 in val.items():
                            if isinstance(v2, dict) and v2.get('mechanism_id') == mech_id:
                                return v2
        return None

    def test_references_mechanism_35(self):
        """Must reference Condé Nast financial dependency mechanism."""
        assert self.mechanism is not None
        refs = self.mechanism.get('related_mechanisms', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        assert 35 in ids

    def test_references_mechanism_130(self):
        """Must reference Snap privacy positioning amplification."""
        assert self.mechanism is not None
        refs = self.mechanism.get('related_mechanisms', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        assert 130 in ids

    def test_references_mechanism_132(self):
        """Must reference Boxall privacy vocabulary inversion."""
        assert self.mechanism is not None
        refs = self.mechanism.get('related_mechanisms', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        assert 132 in ids


class TestFinancialChainCompleteness:
    """Verify the complete financial chain is documented in entities."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_perplexity_publisher_program_details(self):
        """Perplexity's publisher program must be documented with pool size."""
        snap = self.entities['entities']['snap']
        chain = snap['ai_partnerships']['perplexity']['perplexity_publisher_chain']
        assert '$42.5' in chain or '42.5' in chain

    def test_snap_total_source_urls(self):
        """Snap entity must have comprehensive source URLs."""
        snap = self.entities['entities']['snap']
        assert 'source_urls' in snap
        assert len(snap['source_urls']) >= 4

    def test_snap_q3_guidance_documented(self):
        """Q3 2026 revenue guidance must be documented."""
        snap = self.entities['entities']['snap']
        q2 = snap['q2_2026_earnings']
        assert 'q3_guidance_revenue_b' in q2


class TestPerplexityCondeNastVerification:
    """Verify that Condé Nast's Perplexity deal is documented and sourced."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_conde_nast_ai_partners_include_perplexity(self):
        """Condé Nast strategic pivot must list Perplexity as AI partner."""
        # conde_nast_strategic_pivot is under advance_dual_asset_monetization, not entities
        pivot = self.entities.get('advance_dual_asset_monetization', {}).get('conde_nast_strategic_pivot', {})
        if not pivot:
            # Try alternate structure
            for key, val in self.entities.items():
                if isinstance(val, dict) and 'conde_nast_strategic_pivot' in val:
                    pivot = val['conde_nast_strategic_pivot']
                    break
        assert pivot, "Condé Nast strategic pivot section not found"
        assert 'ai_partners' in pivot
        assert 'Perplexity' in pivot['ai_partners']

    def test_conde_nast_ai_deal_count(self):
        """Condé Nast must have 5 documented AI deals."""
        pivot = self.entities.get('advance_dual_asset_monetization', {}).get('conde_nast_strategic_pivot', {})
        if not pivot:
            for key, val in self.entities.items():
                if isinstance(val, dict) and 'conde_nast_strategic_pivot' in val:
                    pivot = val['conde_nast_strategic_pivot']
                    break
        if not pivot:
            pytest.skip("Condé Nast strategic pivot not found")
        assert pivot.get('ai_deal_count', 0) >= 5
