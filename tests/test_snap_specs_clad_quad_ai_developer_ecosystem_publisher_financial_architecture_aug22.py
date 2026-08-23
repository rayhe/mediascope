"""
Test: Snap Specs CLAD Quad-AI Developer Ecosystem Publisher Financial Architecture (Mechanism #231)

Validates the previously unmapped DEVELOPER TOOL LAYER financial convergence
connecting Snap Specs to publisher financial incentives through the CLAD
(Closed Loop Agentic Development) framework.

Key finding: Snap's Lens Studio developer tools officially integrate Claude
Code (Anthropic), Codex (OpenAI), and Cursor (Anysphere) as the primary
development environment for SPECS Lenses. Combined with the runtime AI
partnerships (OpenAI GPT + Google Gemini), this creates a QUAD-AI-COMPANY
financial architecture unique to Snap Specs.

When publications cover Snap Specs favorably, they simultaneously serve
financial interests on FOUR AI company axes — each with distinct publisher
financial relationships. Meta Ray-Ban glasses use Meta's own tools and
Meta AI only; no third-party AI revenue flows exist.

Sources:
- Snap newsroom: "Snap Launches New Tools for SPECS Developers" (AWE 2026, Jun 16)
- Snap developer docs: developers.snap.com/lens-studio/features/lens-studio-ai/overview
- MacRumors: "Snap Launches $2,195 'Specs' Augmented Reality Glasses" (Jun 16, 2026)
- CLAD Summer Hackathon (Jul-Aug 2026)
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


class TestSnapCLADDeveloperEcosystem:
    """Verify CLAD developer tool integrations documented in Snap entity."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']

    def test_clad_framework_exists(self):
        """CLAD developer ecosystem must be documented."""
        specs = self.snap['hardware_devices']['specs_consumer']
        assert 'clad_developer_ecosystem' in specs

    def test_clad_has_claude_code(self):
        """Claude Code (Anthropic) integration documented."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'claude_code' in clad['tool_integrations']
        assert clad['tool_integrations']['claude_code']['company'] == 'Anthropic'

    def test_clad_has_codex(self):
        """Codex (OpenAI) integration documented."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'codex' in clad['tool_integrations']
        assert clad['tool_integrations']['codex']['company'] == 'OpenAI'

    def test_clad_has_cursor(self):
        """Cursor (Anysphere) integration documented."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'cursor' in clad['tool_integrations']
        assert clad['tool_integrations']['cursor']['company'] == 'Anysphere'

    def test_clad_has_source_urls(self):
        """CLAD documentation must include primary source URLs."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'source_urls' in clad
        urls = clad['source_urls']
        assert any('newsroom.snap.com' in u for u in urls), \
            "Must include Snap newsroom primary source"
        assert any('developers.snap.com' in u for u in urls), \
            "Must include Snap developer docs primary source"


class TestSnapQuadAICompanyConvergence:
    """Verify the quad-AI-company architecture is mapped across runtime + developer layers."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']

    def test_runtime_ai_openai(self):
        """OpenAI powers Specs runtime AI (My AI + Lenses)."""
        ai = self.snap['hardware_devices']['specs_consumer']['dual_ai_partnership']
        assert 'openai' in ai

    def test_runtime_ai_google(self):
        """Google Gemini powers Specs runtime AI."""
        ai = self.snap['hardware_devices']['specs_consumer']['dual_ai_partnership']
        assert 'google' in ai

    def test_developer_layer_anthropic(self):
        """Anthropic (Claude Code) in developer tool layer."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert clad['tool_integrations']['claude_code']['company'] == 'Anthropic'

    def test_developer_layer_openai_double(self):
        """OpenAI appears in BOTH runtime (GPT) and developer (Codex) layers."""
        runtime = self.snap['hardware_devices']['specs_consumer']['dual_ai_partnership']
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'openai' in runtime
        assert clad['tool_integrations']['codex']['company'] == 'OpenAI'

    def test_quad_ai_company_count(self):
        """Four distinct AI companies across runtime + developer layers."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert clad['quad_ai_company_count'] == 4
        companies = clad['distinct_ai_companies']
        assert 'OpenAI' in companies
        assert 'Google' in companies
        assert 'Anthropic' in companies
        assert 'Anysphere' in companies


class TestQuadAIPublisherFinancialChains:
    """Each AI company in Snap's ecosystem has distinct publisher financial relationships."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']

    def test_openai_publisher_chain(self):
        """OpenAI: 20+ publisher content deals ($300-400M/yr)."""
        chain = self.clad['publisher_financial_chains']['openai']
        assert chain['publisher_deals_count'] >= 20
        assert chain['publisher_deals_annual_value_m'] == '300-400'

    def test_google_publisher_chain(self):
        """Google: dominant ad revenue + Showcase + AI content pilots."""
        chain = self.clad['publisher_financial_chains']['google']
        assert 'advertising_dominance' in chain['relationship_types']
        assert 'news_showcase' in chain['relationship_types']

    def test_anthropic_publisher_chain(self):
        """Anthropic: zero deals, but investor capital creates indirect paths."""
        chain = self.clad['publisher_financial_chains']['anthropic']
        assert chain['direct_publisher_deals'] == 0
        assert chain['indirect_path_via_investors'] is True
        assert chain['google_investment_b'] >= 2
        assert chain['amazon_investment_b'] >= 13

    def test_meta_has_no_developer_tool_ai_chain(self):
        """Meta Ray-Ban glasses use Meta's own tools — no third-party AI revenue flows."""
        chain = self.clad['meta_contrast']
        assert chain['third_party_ai_tool_revenue_flows'] == 0
        assert chain['developer_ecosystem_isolation'] is True


class TestDeveloperToolFinancialMechanism:
    """Validate the financial mechanism: developer tool usage -> AI company revenue -> publisher relationships."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']

    def test_revenue_flow_direction(self):
        """Developers pay AI companies for tool usage (API costs)."""
        mechanism = self.clad['financial_mechanism']
        assert 'developer_to_ai_company' in mechanism['revenue_flow']

    def test_positive_feedback_loop(self):
        """More Specs adoption -> more developer tool usage -> more AI company revenue."""
        mechanism = self.clad['financial_mechanism']
        assert mechanism['feedback_loop_documented'] is True

    def test_meta_ecosystem_isolation(self):
        """Meta developer ecosystem creates zero third-party AI revenue flows."""
        mechanism = self.clad['financial_mechanism']
        assert mechanism['meta_third_party_ai_revenue_flows'] == 0

    def test_mechanism_extends_224(self):
        """This mechanism extends #224 (triple convergence) by adding developer tool layer."""
        assert self.clad['mechanism_id'] == 231
        assert 224 in self.clad['extends_mechanisms']


class TestCLADHackathonEvidence:
    """Verify CLAD ecosystem is active and growing (hackathon evidence)."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']

    def test_clad_summer_hackathon_documented(self):
        """CLAD Summer Hackathon running Jul-Aug 2026."""
        assert 'hackathon' in self.clad
        assert self.clad['hackathon']['name'] == 'CLAD Summer Hackathon'

    def test_hackathon_demonstrates_ecosystem_activity(self):
        """Active developer ecosystem means ongoing AI tool revenue generation."""
        hackathon = self.clad['hackathon']
        assert hackathon['ai_tools_used'] == ['Claude Code', 'Codex', 'Cursor']


class TestSnapSpecsSep16FinancialConvergence:
    """The September 16 launch event concentrates all four AI financial alignments."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']

    def test_sep16_launch_date_confirmed(self):
        specs = self.snap['hardware_devices']['specs_consumer']
        assert specs['consumer_launch_event_date'] == '2026-09-16'

    def test_quad_convergence_at_launch(self):
        """All four AI company relationships active at Sep 16 launch."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert clad['all_active_at_sep16_launch'] is True

    def test_pre_launch_coverage_window(self):
        """25 days from today (Aug 22) to Sep 16 — peak coverage window."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert 'pre_launch_coverage_prediction' in clad

    def test_coverage_incentive_inversion_vs_meta(self):
        """Coverage incentives perfectly inverted: positive Specs coverage aligns with
        publisher financial interests on 5 axes (4 AI + 1 direct Discover); positive Meta coverage aligns with zero."""
        clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']
        assert clad['publisher_financial_alignment_axes_snap'] >= 4  # Updated from ==4 to >=4 after mechanism #239 added 5th axis (Snap Discover direct revenue)
        assert clad['publisher_financial_alignment_axes_meta'] == 0


class TestConfoundingFactors:
    """Document legitimate reasons for different coverage that are NOT financial."""

    def setup_method(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.clad = self.snap['hardware_devices']['specs_consumer']['clad_developer_ecosystem']

    def test_confounding_factors_documented(self):
        """Must document legitimate confounders."""
        assert 'confounding_factors' in self.clad
        factors = self.clad['confounding_factors']
        assert len(factors) >= 2

    def test_market_share_confounder(self):
        """Snap Specs is new with zero market share; Meta has 84% — different scrutiny levels justified."""
        factors = self.clad['confounding_factors']
        factor_names = [f['name'] for f in factors]
        assert 'market_share_differential' in factor_names

    def test_incident_history_confounder(self):
        """Meta has real privacy incidents; Snap Specs has none yet — incident-driven coverage is legitimate."""
        factors = self.clad['confounding_factors']
        factor_names = [f['name'] for f in factors]
        assert 'incident_history_differential' in factor_names
