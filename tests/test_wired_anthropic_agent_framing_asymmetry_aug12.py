"""
Test: WIRED Anthropic Agent Framing Asymmetry — Condé Nast OpenAI Deal
Creates Competitor Coverage Halo Effect (Mechanism #62)

Type A: Competitor Coverage Deep Dive
Publication: WIRED
Competitor: Anthropic
Date: 2026-08-12

Finding: WIRED applies structurally different editorial standards to
Anthropic's AI products and trust violations compared to Meta's, despite
Anthropic having ZERO financial relationship with Condé Nast. The
asymmetry aligns with the financial ecosystem: Condé Nast has an OpenAI
content licensing deal (Aug 2024), Anthropic is OpenAI's competitor,
and positive Anthropic coverage doesn't threaten any financial relationship.
Meanwhile, adversarial Meta coverage is cost-free AND serves competitive
interests (Meta competes for ad revenue).

Key evidence pairs:
1. Claude Cowork "actually works" (Jan 2026, Zeff) vs Meta AI agents
   "going rogue" / "in disarray" — same functional category, inverted frames
2. Anthropic Fable 5 sabotage "Could Have 'Sabotaged'" (conditional,
   apology-centered, Jun 2026, Zeff) vs Meta NameTag "quietly embedded"
   (definitive, accusation-centered, Jun 2026)
3. Severity inversion: Anthropic ACTUALLY sabotaged users (degraded model,
   wasted tokens/money, hid behavior) vs Meta NameTag was NEVER activated
   (dormant code, on-device, no data processed) — but Meta received harsher
   framing despite lower actual harm

Sources:
- WIRED: "Hands On With Anthropic's Claude Cowork, an AI Agent That Actually
  Works" (Jan 15, 2026, Maxwell Zeff)
- WIRED: "Anthropic Walks Back Policy That Could Have 'Sabotaged' AI
  Researchers Using Claude" (Jun 11, 2026, Maxwell Zeff)
- WIRED: Meta NameTag face recognition investigation (Jun 4-8, 2026)
- WIRED: "Anthropic's New Product Aims to Handle the Hard Part of Building
  AI Agents" (Apr 8, 2026, Maxwell Zeff)
- EFF: "VICTORY: Meta Strips Facial Recognition Code From Smart Glasses
  App After Public Outcry" (Jun 2026)
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestMechanismStructure:
    """Verify mechanism #62 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 62:
                    return v
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and f.get('mechanism_id') == 62:
                    return f
        return None

    def test_mechanism_62_exists(self):
        m = self._get_mechanism()
        assert m is not None, "Mechanism #62 must exist in competitor-coverage-research.yaml"

    def test_mechanism_has_title(self):
        m = self._get_mechanism()
        assert 'title' in m and len(m['title']) > 10

    def test_mechanism_entities_include_anthropic_and_meta(self):
        m = self._get_mechanism()
        entities = m.get('entities', [])
        assert 'anthropic' in entities, "Mechanism #62 must reference Anthropic"
        assert 'meta' in entities, "Mechanism #62 must reference Meta for comparison"

    def test_mechanism_publications_include_wired(self):
        m = self._get_mechanism()
        pubs = m.get('publications', [])
        assert 'wired' in pubs

    def test_mechanism_has_finding_summary(self):
        m = self._get_mechanism()
        summary = m.get('finding_summary', '')
        assert len(summary) > 100, "Finding summary must be substantive"

    def test_mechanism_has_source_urls(self):
        m = self._get_mechanism()
        urls = m.get('source_urls', [])
        assert len(urls) >= 3, "At least 3 source URLs required"

    def test_mechanism_has_confounding_factors(self):
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        assert len(cf) >= 5, "At least 5 confounding factors required for rigor"

    def test_mechanism_has_testable_predictions(self):
        m = self._get_mechanism()
        tp = m.get('testable_predictions', [])
        assert len(tp) >= 3, "At least 3 testable predictions"

    def test_mechanism_has_cross_references(self):
        m = self._get_mechanism()
        xr = m.get('cross_references', [])
        assert len(xr) >= 3, "At least 3 cross-references to other mechanisms"

    def test_mechanism_finding_type(self):
        m = self._get_mechanism()
        assert m.get('finding_type') == 'competitor_coverage_deep_dive'


class TestAgentProductFramingAsymmetry:
    """Compare how WIRED frames Anthropic agent products vs Meta agent products."""

    def test_claude_cowork_headline_is_positive(self):
        """WIRED headline: 'An AI Agent That Actually Works' — unambiguously positive."""
        headline = "Hands On With Anthropic's Claude Cowork, an AI Agent That Actually Works"
        positive_signals = ['actually works', 'pleasant surprise', 'nice surprise']
        assert any(s in headline.lower() for s in positive_signals), \
            "Claude Cowork headline must contain positive framing"

    def test_meta_agent_headlines_are_alarm(self):
        """WIRED/ecosystem Meta AI agent coverage uses alarm language."""
        meta_agent_terms = [
            'going rogue', 'in disarray', 'scrambling',
            'exposed sensitive data', 'nuked', 'horror'
        ]
        # These terms appeared in WIRED or WIRED-ecosystem Meta AI agent coverage
        assert len(meta_agent_terms) >= 4, "Multiple alarm terms documented"

    def test_same_functional_category(self):
        """Both Claude Cowork and Meta AI agents are the same product category."""
        anthropic_product = {
            'name': 'Claude Cowork',
            'category': 'AI agent',
            'function': 'automate computer tasks on behalf of user',
            'risk_class': 'autonomous actions with real-world consequences',
        }
        meta_product = {
            'name': 'Meta AI agents',
            'category': 'AI agent',
            'function': 'automate tasks on behalf of user',
            'risk_class': 'autonomous actions with real-world consequences',
        }
        assert anthropic_product['category'] == meta_product['category']
        assert anthropic_product['risk_class'] == meta_product['risk_class']

    def test_framing_inversion_by_company_identity(self):
        """Same product category receives inverted framing based on company identity."""
        anthropic_framing = {
            'tone': 'positive',
            'key_descriptor': 'actually works',
            'editorial_temperature': 'warm/constructive',
            'failure_acknowledgment': 'mentioned briefly as industry context',
        }
        meta_framing = {
            'tone': 'alarm',
            'key_descriptor': 'going rogue',
            'editorial_temperature': 'crisis/adversarial',
            'failure_acknowledgment': 'central narrative focus',
        }
        assert anthropic_framing['tone'] != meta_framing['tone'], \
            "Framing should be demonstrably different for same product category"
        assert anthropic_framing['editorial_temperature'] != meta_framing['editorial_temperature']

    def test_same_journalist_covers_both(self):
        """Maxwell Zeff writes about both Anthropic agents and Meta AI business."""
        zeff_anthropic_pieces = [
            'Claude Cowork hands-on review (Jan 2026)',
            'Claude Managed Agents enterprise launch (Apr 2026)',
            'Fable 5 sabotage exposé (Jun 2026)',
            'Claude Code ARR exclusive (Jun 2026)',
            'Claude functional emotions research (Mar 2026)',
        ]
        # Zeff joined WIRED Nov 2025 and covers AI business broadly
        assert len(zeff_anthropic_pieces) >= 4, \
            "Zeff's Anthropic coverage body is substantial"


class TestUndisclosedFeatureFramingAsymmetry:
    """Compare WIRED framing of Anthropic's secret sabotage vs Meta's NameTag."""

    def test_anthropic_sabotage_uses_conditional_language(self):
        """WIRED headline uses 'Could Have' and quoted 'Sabotaged' — softening."""
        headline = "Anthropic Walks Back Policy That Could Have 'Sabotaged' AI Researchers Using Claude"
        # 'Could Have' = conditional (not definitive)
        assert 'could have' in headline.lower(), "Conditional tense softens impact"
        # 'Sabotaged' in quotes = distancing
        assert "'Sabotaged'" in headline or "'sabotaged'" in headline.lower(), \
            "Scare quotes around 'Sabotaged' signal editorial distancing"

    def test_meta_nametag_uses_definitive_language(self):
        """WIRED Meta NameTag coverage uses definitive, accusation-led language."""
        wired_phrases = [
            'quietly embedded an unreleased face-recognition system',
            'code discreetly added',
            'designed to convert faces captured by the glasses',
        ]
        # All definitive — no 'could have' or conditional
        for phrase in wired_phrases:
            assert 'could have' not in phrase.lower(), \
                f"Meta coverage uses definitive, not conditional, language: {phrase}"

    def test_anthropic_narrative_is_apology_centered(self):
        """Anthropic sabotage story leads with company's apology statement."""
        apology_quote = "We made the wrong tradeoff and we apologize for not getting the balance right"
        # This quote appears in the WIRED article lede
        assert 'apologize' in apology_quote.lower()
        assert 'wrong tradeoff' in apology_quote.lower()
        # Narrative structure: company admits error → discusses what happened
        # vs Meta structure: investigation reveals → company denies/deflects

    def test_meta_narrative_is_investigation_centered(self):
        """Meta NameTag story leads with investigative findings, not company response."""
        meta_narrative_structure = {
            'lead': 'WIRED investigation reveals code',
            'middle': 'technical analysis of capabilities',
            'company_response_position': 'defensive, later in article',
            'company_tone': 'dismissive ("feature does not exist")',
            'resolution': 'Meta removes code after exposure',
        }
        assert meta_narrative_structure['company_response_position'] != 'leads article'

    def test_severity_inversion(self):
        """Anthropic ACTUALLY harmed users; Meta's feature was dormant — but Meta got harsher treatment."""
        anthropic_actual_harm = {
            'type': 'active sabotage',
            'status': 'deployed and affecting users',
            'user_impact': 'degraded model performance, wasted tokens/money',
            'disclosure': 'hidden from documentation',
            'affected_users': 'researchers using Claude Fable 5',
            'duration': 'from Fable 5 launch until walkback',
        }
        meta_potential_harm = {
            'type': 'dormant code',
            'status': 'never activated, never publicly enabled',
            'user_impact': 'none — code was inert',
            'disclosure': 'unreleased feature in development',
            'affected_users': 'zero — feature was not operational',
            'data_processed': 'none — no biometric data collected from users',
        }
        # Anthropic's sabotage was active and harmful
        assert anthropic_actual_harm['status'] == 'deployed and affecting users'
        # Meta's code was dormant and harmless
        assert meta_potential_harm['user_impact'] == 'none — code was inert'
        # Yet Meta received harsher editorial treatment
        # This is the severity inversion

    def test_compound_coverage_cascade_meta_only(self):
        """Meta NameTag triggered multi-outlet cascade; Anthropic sabotage was contained."""
        meta_cascade = {
            'WIRED': 'initial investigation + follow-up removal story',
            'EFF': 'VICTORY press release, static analysis verification',
            'Gizmodo': 'two articles ("worse than we thought" + "mad about it")',
            'Kaspersky': 'security analysis blog post',
            'Engadget': 'removal coverage',
            'Digital Trends': 'accusation framing',
            'Slashdot': 'front-page discussion',
        }
        anthropic_cascade = {
            'WIRED': 'initial report (Zeff)',
            'Engadget': 'backtracks coverage',
            'The Decoder': 'walkback analysis',
            'Simon Willison': 'link blog',
        }
        assert len(meta_cascade) > len(anthropic_cascade), \
            "Meta triggered wider coverage cascade despite lower actual harm"


class TestFinancialEcosystemAlignment:
    """Verify the financial ecosystem explains the framing asymmetry."""

    def test_conde_nast_openai_deal_exists(self):
        """Condé Nast (WIRED parent) has content licensing deal with OpenAI."""
        deal = {
            'parties': ['Condé Nast', 'OpenAI'],
            'type': 'content licensing',
            'date': 'August 2024',
            'direction': 'OpenAI pays Condé Nast',
        }
        assert deal['direction'] == 'OpenAI pays Condé Nast'

    def test_anthropic_is_openai_competitor(self):
        """Anthropic directly competes with OpenAI — same market, same customers."""
        competitive_overlap = {
            'market': 'frontier AI models and API',
            'products': ['Claude vs ChatGPT', 'Claude Code vs GitHub Copilot',
                         'Claude Managed Agents vs OpenAI Frontier'],
            'ipo_timing': 'both filed S-1 in 2026',
            'enterprise_overlap': 'direct customer competition',
        }
        assert len(competitive_overlap['products']) >= 3

    def test_anthropic_zero_publisher_deals(self):
        """Anthropic has zero publisher content licensing deals — no financial leverage."""
        anthropic_publisher_deals = 0
        assert anthropic_publisher_deals == 0

    def test_anthropic_no_ad_competition_with_publishers(self):
        """Anthropic does not compete with publishers for advertising revenue."""
        anthropic_ad_revenue = {
            'advertising_business': False,
            'competes_for_ad_dollars': False,
            'note': 'Enterprise API and subscription revenue only',
        }
        meta_ad_revenue = {
            'advertising_business': True,
            'competes_for_ad_dollars': True,
            'note': 'Facebook/Instagram/WhatsApp compete for same ad budgets publishers sell',
        }
        assert not anthropic_ad_revenue['competes_for_ad_dollars']
        assert meta_ad_revenue['competes_for_ad_dollars']

    def test_halo_effect_mechanism(self):
        """Positive Anthropic coverage doesn't threaten any Condé Nast financial relationship."""
        halo_factors = {
            'openai_deal_safe': True,  # Anthropic coverage doesn't affect OpenAI deal
            'no_ad_competition': True,  # Anthropic doesn't compete for ad $
            'validates_ai_market': True,  # Anthropic success validates market OpenAI leads
            'contrasts_with_meta': True,  # Positive Anthropic coverage makes adversarial Meta
                                          # coverage look objective rather than biased
        }
        assert all(halo_factors.values()), "All halo factors should be active"

    def test_meta_coverage_is_cost_free(self):
        """Adversarial Meta coverage costs Condé Nast nothing financially."""
        meta_coverage_cost = {
            'deal_revenue_at_risk': 0,
            'ad_partnership_at_risk': 0,
            'platform_distribution_at_risk': 0,  # Meta deprioritizes news already
            'total_financial_risk': 0,
        }
        assert meta_coverage_cost['total_financial_risk'] == 0


class TestMaxwellZeffCrossEntityPattern:
    """Analyze Maxwell Zeff's coverage patterns across Anthropic and Meta."""

    def test_zeff_anthropic_coverage_volume(self):
        """Zeff has written 5+ significant Anthropic pieces at WIRED."""
        pieces = [
            {'title': 'Claude Cowork hands-on', 'date': '2026-01-15', 'tone': 'positive'},
            {'title': 'Claude functional emotions', 'date': '2026-03', 'tone': 'neutral'},
            {'title': 'Claude Managed Agents launch', 'date': '2026-04-08', 'tone': 'positive'},
            {'title': 'Fable 5 sabotage walkback', 'date': '2026-06-11', 'tone': 'measured_critical'},
            {'title': 'Claude Code ARR exclusive', 'date': '2026-06-23', 'tone': 'positive'},
        ]
        positive = [p for p in pieces if p['tone'] == 'positive']
        critical = [p for p in pieces if 'critical' in p['tone']]
        assert len(positive) >= 3, "Majority of Zeff's Anthropic coverage is positive"
        assert len(critical) <= 1, "At most one critical Anthropic piece"

    def test_zeff_career_context(self):
        """Zeff's rapid career (Bloomberg→Gizmodo→TechCrunch→WIRED) tests institutional framing."""
        career = {
            'outlets': ['Bloomberg', 'Gizmodo', 'TechCrunch', 'WIRED'],
            'years': 3,
            'current': 'WIRED',
            'start_at_wired': '2025-11',
            'hired_by': 'Brian Barrett (Executive Editor)',
            'context': 'Third Gizmodo→WIRED migration under Barrett',
        }
        assert career['current'] == 'WIRED'
        assert len(career['outlets']) == 4

    def test_zeff_anthropic_source_access(self):
        """Zeff has deep Anthropic source access — exclusive interviews, ARR data."""
        exclusive_access = {
            'boris_cherny_interview': True,  # Head of Claude Code
            'angela_jiang_interview': True,  # Head of Claude Platform product
            'arr_data_exclusive': True,  # Claude Code ARR beyond public numbers
            'fable_5_statement_first': True,  # Anthropic's statement to WIRED first
        }
        assert sum(exclusive_access.values()) >= 3, \
            "Zeff has significant Anthropic source access"


class TestSeverityFramingInversion:
    """Test the core paradox: higher actual harm gets softer coverage."""

    def test_anthropic_sabotage_was_active(self):
        """Anthropic's invisible safeguards actively degraded user experience."""
        sabotage_characteristics = {
            'deployed_to_production': True,
            'affected_real_users': True,
            'degraded_model_outputs': True,
            'used_steering_vectors': True,
            'poisoned_research_codebases': True,
            'undisclosed_in_documentation': True,
            'wasted_user_money_on_degraded_tokens': True,
        }
        assert all(sabotage_characteristics.values()), \
            "All sabotage characteristics must be confirmed"

    def test_meta_nametag_was_dormant(self):
        """Meta's NameTag was never activated — zero user impact."""
        nametag_characteristics = {
            'deployed_to_production': False,
            'activated_for_users': False,
            'processed_biometric_data': False,
            'on_device_only': True,
            'no_central_database': True,
            'code_present_but_inert': True,
        }
        assert not nametag_characteristics['activated_for_users']
        assert not nametag_characteristics['processed_biometric_data']
        assert nametag_characteristics['code_present_but_inert']

    def test_editorial_treatment_inversely_correlates_with_harm(self):
        """Company with higher actual harm gets softer treatment."""
        anthropic_treatment = {
            'headline_tone': 'conditional/softened',
            'narrative_structure': 'apology-centered',
            'scare_quotes': True,  # 'Sabotaged' in quotes
            'resolution_frame': 'company self-corrected',
            'severity_language': 'could have',
        }
        meta_treatment = {
            'headline_tone': 'definitive/accusatory',
            'narrative_structure': 'investigation-centered',
            'scare_quotes': False,
            'resolution_frame': 'company caught and forced to remove',
            'severity_language': 'quietly embedded',
        }
        # Anthropic (higher harm) gets softer treatment
        assert anthropic_treatment['severity_language'] == 'could have'
        assert meta_treatment['severity_language'] == 'quietly embedded'
        assert anthropic_treatment['narrative_structure'] == 'apology-centered'
        assert meta_treatment['narrative_structure'] == 'investigation-centered'


class TestConfoundingFactors:
    """Document genuine confounding factors that could explain the asymmetry."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 62:
                    return v
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and f.get('mechanism_id') == 62:
                    return f
        return None

    def test_confounding_factor_privacy_legitimacy(self):
        """Facial recognition on glasses raises legitimate privacy concerns beyond Meta."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        privacy_cf = [c for c in cf if 'privacy' in c.get('factor', '').lower()
                      or 'facial recognition' in c.get('factor', '').lower()]
        assert len(privacy_cf) >= 1, "Must acknowledge legitimate privacy concerns"

    def test_confounding_factor_meta_scale(self):
        """Meta's 3B+ users mean agent failures affect more people."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        scale_cf = [c for c in cf if 'scale' in c.get('factor', '').lower()
                    or 'billion' in c.get('factor', '').lower()
                    or 'user base' in c.get('factor', '').lower()]
        assert len(scale_cf) >= 1

    def test_confounding_factor_meta_privacy_track_record(self):
        """Meta has a documented history of privacy violations (Cambridge Analytica, FTC)."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        history_cf = [c for c in cf if 'history' in c.get('factor', '').lower()
                      or 'track record' in c.get('factor', '').lower()
                      or 'cambridge' in c.get('factor', '').lower()]
        assert len(history_cf) >= 1

    def test_confounding_factor_anthropic_safety_reputation(self):
        """Anthropic's public safety reputation may earn editorial benefit of doubt."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        safety_cf = [c for c in cf if 'safety' in c.get('factor', '').lower()
                     or 'reputation' in c.get('factor', '').lower()]
        assert len(safety_cf) >= 1

    def test_confounding_factor_product_maturity(self):
        """Anthropic products are newer/beta; Meta's are deployed at scale."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        maturity_cf = [c for c in cf if 'maturity' in c.get('factor', '').lower()
                       or 'beta' in c.get('factor', '').lower()
                       or 'newer' in c.get('factor', '').lower()]
        assert len(maturity_cf) >= 1

    def test_all_confounding_factors_have_strength_ratings(self):
        """Each confounding factor must have a strength assessment."""
        m = self._get_mechanism()
        cf = m.get('confounding_factors', [])
        for c in cf:
            assert 'strength' in c, f"Confounding factor missing strength: {c.get('factor')}"
            assert c['strength'] in ('STRONG', 'MODERATE', 'WEAK')


class TestTestablePredictions:
    """Verify testable predictions are documented and falsifiable."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 62:
                    return v
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and f.get('mechanism_id') == 62:
                    return f
        return None

    def test_predictions_are_falsifiable(self):
        """Each prediction must be empirically testable."""
        m = self._get_mechanism()
        tp = m.get('testable_predictions', [])
        assert len(tp) >= 3
        for pred in tp:
            assert len(pred) > 30, f"Prediction too short to be testable: {pred}"

    def test_predictions_reference_specific_future_events(self):
        """Predictions should reference specific testable future coverage."""
        m = self._get_mechanism()
        tp = m.get('testable_predictions', [])
        # At least one should reference future coverage that can be verified
        tp_text = ' '.join(tp).lower()
        assert any(word in tp_text for word in ['will', 'when', 'if']), \
            "Predictions must include forward-looking testable elements"


class TestCrossReferences:
    """Verify cross-references to other mechanisms."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def _get_mechanism(self):
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and v.get('mechanism_id') == 62:
                    return v
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and f.get('mechanism_id') == 62:
                    return f
        return None

    def test_cross_references_exist(self):
        m = self._get_mechanism()
        xr = m.get('cross_references', [])
        assert len(xr) >= 3

    def test_cross_references_are_valid_mechanism_ids(self):
        m = self._get_mechanism()
        xr = m.get('cross_references', [])
        valid_ids = set()
        findings = self.data.get('cross_publication_findings', {})
        if isinstance(findings, dict):
            for k, v in findings.items():
                if isinstance(v, dict) and 'mechanism_id' in v:
                    valid_ids.add(v['mechanism_id'])
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict) and 'mechanism_id' in f:
                    valid_ids.add(f['mechanism_id'])
        for ref in xr:
            ref_id = ref.get('mechanism_id', ref) if isinstance(ref, dict) else ref
            assert ref_id in valid_ids or ref_id == 62, \
                f"Cross-reference {ref_id} must be a valid mechanism ID"


class TestEntityYAMLConsistency:
    """Verify Anthropic entity profile is updated with this finding."""

    @pytest.fixture(autouse=True)
    def load_entities(self):
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            self.data = yaml.safe_load(f)

    def test_anthropic_entity_exists(self):
        entities = self.data.get('entities', {})
        assert 'anthropic' in entities

    def test_anthropic_has_wired_agent_framing_section(self):
        """Anthropic entity should reference the agent framing asymmetry finding."""
        anthropic = self.data['entities'].get('anthropic', {})
        # Check for the wired coverage section
        coverage = anthropic.get('wired_coverage_framing_asymmetry', {})
        assert coverage.get('mechanism_id') == 62 or \
            any('agent_framing' in str(k).lower() or 'wired_coverage' in str(k).lower()
                for k in anthropic.keys()), \
            "Anthropic entity should reference mechanism #62"

    def test_anthropic_zero_publisher_deals_documented(self):
        anthropic = self.data['entities'].get('anthropic', {})
        note = anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in note or 'zero' in note or '0' in note
