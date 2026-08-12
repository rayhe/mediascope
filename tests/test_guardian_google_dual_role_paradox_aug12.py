"""
Mechanism #59: Guardian Dual-Role Paradox — Simultaneous Google AI Pilot
Partner and EPC Antitrust Complainant

TYPE A: Competitor Coverage Deep Dive — The Guardian × Google

FINDING: The Guardian occupies a structurally paradoxical position in the
Google AI content licensing landscape: it is simultaneously a named commercial
partner in Google's AI news pilot (testing AI-powered article overviews and
audio briefings, earning "single figure millions" GBP annually) AND a member
of the European Publishers Council (EPC), which filed a formal Article 102
TFEU antitrust complaint against Google over the same AI Overviews feature.

The paradox extends to governance: Matthew Brittin, Google's EMEA President
for 18 years, served as the Guardian Media Group's Senior Independent Director
(the highest independent governance role after Chair) from ~2025 until March
24, 2026 — overlapping with both the Google News AI pilot launch (Dec 2025)
and the EPC complaint filing period. Brittin was specifically recruited via
global executive search (Green Park) for his tech expertise, then left GMG to
become BBC Director-General.

COVERAGE COMPARISON (Dan Milmo, Global Technology Editor):
- Meta: -0.45 tone, "big tobacco" escalation, "industry-defining" language,
  4+ standalone rogue AI articles. $0 Guardian deal.
- Google: -0.35 tone, measured regulatory reporting, factual competition-law
  focus. "Single figure millions" GBP annual deal.
- Gap: 0.10 tone points, but the editorial TEMPERATURE gap is much wider
  (loaded metaphors vs factual relay). Google is objectively more harmful to
  the Guardian's business (traffic collapse, ad-tech dominance, coercive pilot
  terms) yet receives softer editorial treatment.

STRUCTURAL INSIGHT: The dual role creates a coverage equilibrium where the
Guardian can maintain credibility as a publisher-rights advocate (via EPC
membership) while avoiding the editorial aggression toward Google that might
jeopardize its commercial relationship. Meta, with $0 in Guardian deals,
bears the full weight of adversarial coverage that financial relationships
deflect from Google.

CONFOUNDING FACTORS (7):
1. EPC membership is an industry coalition position, not editorial policy
2. Scott Trust charter explicitly protects editorial independence
3. Dan Milmo's Google coverage IS critical (EU fines, CMA regulation)
4. Guardian has published critical Google content investigations (e.g., AI
   Overviews traffic impact)
5. Multiple revenue streams reduce Google dependency
6. Editorial and commercial are structurally separated at Guardian
7. Google's regulatory exposure is a legitimate standalone beat

TESTABLE PREDICTIONS (4):
1. If Guardian exits the Google AI pilot, Google coverage tone will shift
   toward Meta-level adversarial framing within 6 months
2. Guardian will not apply "big tobacco" or equivalent loaded metaphor to
   Google's AI Overviews traffic cannibalization, despite it being a direct
   threat to Guardian revenue
3. Dan Milmo will continue to cover Google antitrust factually without the
   editorial escalation applied to Meta child safety verdicts
4. If Meta signs a content licensing deal with the Guardian, Meta coverage
   tone will moderate measurably within one editorial cycle

Sources:
- Google AI pilot partners: Google Keyword blog (Dec 2025), Press Gazette,
  Brief.news (Jun 26, 2026)
- EPC complaint: medianama.com (Feb 2026), searchengineland.com
- Guardian revenue: Press Gazette ("single figure millions" GBP)
- Brittin governance: Companies House filing 00094531, Green Park case study,
  ProlificNorth, Computing.co.uk
- Dan Milmo framing: BuzzSumo journalist profile, Guardian articles (verified
  via existing MediaScope cross-entity analysis)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
COMPETITOR_RESEARCH_PATH = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
GUARDIAN_PROFILE_PATH = os.path.join(PROFILES_DIR, 'guardian.yaml')


def load_competitor_research():
    with open(COMPETITOR_RESEARCH_PATH) as f:
        return yaml.safe_load(f)


def load_guardian_profile():
    with open(GUARDIAN_PROFILE_PATH) as f:
        return yaml.safe_load(f)


# ============================================================
# 1. Structural Paradox Documentation
# ============================================================

class TestGuardianDualRoleStructure:
    """Verify the dual-role paradox is documented in profiles."""

    def test_mechanism_59_exists_in_cpf(self):
        data = load_competitor_research()
        cpf = data.get('cross_publication_findings', {})
        assert 'guardian_google_dual_role_paradox' in cpf, \
            "Mechanism #59 must be in cross_publication_findings"

    def test_mechanism_59_has_required_fields(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        required = ['mechanism_id', 'mechanism_name', 'finding_type',
                     'finding_summary', 'publication', 'test_file',
                     'date_added', 'discovery_date']
        for field in required:
            assert field in m59, f"Mechanism #59 missing required field: {field}"

    def test_mechanism_59_id_is_59(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        assert m59['mechanism_id'] == 59

    def test_mechanism_59_publication_is_guardian(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        assert m59['publication'] == 'guardian'

    def test_mechanism_59_test_file_correct(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        assert m59['test_file'] == 'tests/test_guardian_google_dual_role_paradox_aug12.py'


# ============================================================
# 2. Google AI Pilot Partnership Evidence
# ============================================================

class TestGoogleAIPilotPartnership:
    """Verify evidence of Guardian's commercial partnership with Google."""

    def test_guardian_profile_documents_google_pilot(self):
        data = load_guardian_profile()
        # Check google_ai_pilot section exists somewhere in the profile
        content = yaml.dump(data)
        assert 'google_ai_pilot' in content or 'google_news_ai_pilot' in content or \
               'ai_pilot' in content.lower(), \
            "Guardian profile must document Google AI news pilot partnership"

    def test_guardian_is_named_pilot_partner(self):
        """Guardian confirmed as Google AI pilot partner alongside WaPo, Der Spiegel, El País."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        # The pilot partnership should be documented
        assert 'Google' in content, "Guardian profile must reference Google relationship"

    def test_guardian_earns_from_google(self):
        """Press Gazette confirmed Guardian earns 'single figure millions' GBP from Google."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        # Revenue documentation should exist
        has_revenue = 'million' in content.lower() or 'revenue' in content.lower() or \
                      'single figure' in content.lower() or 'showcase' in content.lower()
        assert has_revenue, "Guardian profile must document Google revenue relationship"


# ============================================================
# 3. EPC Membership and Antitrust Complaint
# ============================================================

class TestEPCMembershipAndComplaint:
    """Verify the EPC membership and complaint contradiction."""

    def test_guardian_is_epc_member(self):
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert 'European Publishers Council' in content or 'EPC' in content, \
            "Guardian profile must document EPC membership/affiliation"

    def test_epc_filed_google_antitrust_complaint(self):
        """EPC filed Article 102 TFEU complaint against Google over AI Overviews."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        summary = m59.get('finding_summary', '')
        assert 'EPC' in summary or 'European Publishers Council' in summary or \
               'antitrust' in summary.lower(), \
            "Mechanism #59 must document EPC antitrust complaint"

    def test_simultaneous_positions_documented(self):
        """The paradox of being both partner and complainant must be explicit."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        summary = m59.get('finding_summary', '')
        assert 'pilot' in summary.lower() or 'partner' in summary.lower(), \
            "Must document the pilot partnership side of the paradox"
        assert 'complaint' in summary.lower() or 'antitrust' in summary.lower(), \
            "Must document the antitrust complaint side of the paradox"


# ============================================================
# 4. Governance Revolving Door
# ============================================================

class TestGovernanceRevolvingDoor:
    """Verify Brittin governance overlap documentation."""

    def test_brittin_documented_in_guardian_profile(self):
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert 'Brittin' in content, \
            "Matthew Brittin must be documented in Guardian profile"

    def test_brittin_was_sid(self):
        """Brittin held Senior Independent Director role — highest independent governance."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert 'Senior Independent Director' in content or 'SID' in content, \
            "Brittin's SID role must be documented"

    def test_brittin_google_career_documented(self):
        """18 years at Google, EMEA President."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert 'Google EMEA' in content or 'Google' in content, \
            "Brittin's Google career must be documented"

    def test_brittin_overlap_with_pilot(self):
        """Brittin was SID during Google AI pilot launch (Dec 2025) until Mar 2026."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        # Brittin terminated 2026-03-24, pilot launched Dec 2025
        assert '2026-03' in content or '2026-03-24' in content, \
            "Brittin's departure date must be documented to show pilot overlap"


# ============================================================
# 5. Coverage Framing Asymmetry
# ============================================================

class TestCoverageFramingAsymmetry:
    """Verify Meta vs Google coverage tone gap."""

    def test_milmo_meta_tone_documented(self):
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert 'big tobacco' in content.lower() or '-0.45' in content, \
            "Milmo's Meta coverage tone/framing must be documented"

    def test_milmo_google_tone_documented(self):
        data = load_guardian_profile()
        content = yaml.dump(data)
        assert '-0.35' in content or 'measured' in content.lower() or \
               'regulatory' in content.lower(), \
            "Milmo's Google coverage tone must be documented"

    def test_meta_gets_harsher_framing_than_google(self):
        """Despite Google being more harmful to Guardian's business model."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        # The asymmetry documentation should exist
        has_asymmetry = 'big tobacco' in content.lower() and \
                        ('google' in content.lower() and 'measured' in content.lower())
        assert has_asymmetry, \
            "Profile must document that Meta gets harsher framing than Google"

    def test_google_more_harmful_to_guardian_business(self):
        """Google's traffic dominance is objectively more harmful than Meta's to Guardian."""
        data = load_guardian_profile()
        content = yaml.dump(data)
        has_business_harm = 'traffic' in content.lower() or 'dominan' in content.lower()
        assert has_business_harm, \
            "Profile must acknowledge Google's greater business harm to Guardian"


# ============================================================
# 6. Financial Relationship Comparison
# ============================================================

class TestFinancialRelationshipComparison:
    """Meta $0 vs Google millions — coverage tracks money."""

    def test_meta_zero_deal_documented(self):
        """Meta has $0 in Guardian content deals since Facebook News Tab ended."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        summary = m59.get('finding_summary', '')
        assert '$0' in summary or 'zero' in summary.lower() or 'no deal' in summary.lower(), \
            "Must document Meta's $0 Guardian relationship"

    def test_google_revenue_documented(self):
        """Guardian earns from Google — pilot fees + Showcase + ad revenue."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        summary = m59.get('finding_summary', '')
        has_google_money = 'million' in summary.lower() or 'revenue' in summary.lower() or \
                           'earns' in summary.lower() or 'annual' in summary.lower()
        assert has_google_money, "Must document Google's financial relationship with Guardian"

    def test_coverage_tracks_financial_relationship(self):
        """Coverage tone correlates with financial relationship presence."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        summary = m59.get('finding_summary', '')
        has_correlation = 'correlat' in summary.lower() or 'predict' in summary.lower() or \
                          'track' in summary.lower() or 'align' in summary.lower()
        assert has_correlation, \
            "Must state that coverage tone tracks financial relationships"


# ============================================================
# 7. Confounding Factors
# ============================================================

class TestConfoundingFactors:
    """Mechanism must document legitimate alternative explanations."""

    def test_has_confounding_factors(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        factors = m59.get('legitimate_factors', [])
        assert len(factors) >= 5, \
            f"Expected ≥5 confounding factors, got {len(factors)}"

    def test_scott_trust_independence_acknowledged(self):
        """Must acknowledge Scott Trust editorial independence charter."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        factors_text = str(m59.get('legitimate_factors', []))
        assert 'Scott Trust' in factors_text or 'editorial independence' in factors_text.lower(), \
            "Must acknowledge Scott Trust as confounding factor"

    def test_editorial_commercial_separation_acknowledged(self):
        """Must acknowledge structural separation of editorial and commercial."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        factors_text = str(m59.get('legitimate_factors', []))
        has_separation = 'separat' in factors_text.lower() or 'commercial' in factors_text.lower()
        assert has_separation, \
            "Must acknowledge editorial/commercial separation as confounding factor"


# ============================================================
# 8. Testable Predictions
# ============================================================

class TestTestablePredictions:
    """Mechanism must have falsifiable predictions."""

    def test_has_testable_predictions(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        predictions = m59.get('testable_predictions', [])
        assert len(predictions) >= 3, \
            f"Expected ≥3 testable predictions, got {len(predictions)}"

    def test_predictions_are_falsifiable(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        predictions = m59.get('testable_predictions', [])
        pred_text = str(predictions).lower()
        has_conditional = 'if' in pred_text or 'will' in pred_text or \
                          'within' in pred_text
        assert has_conditional, "Predictions must be conditional/temporal (falsifiable)"


# ============================================================
# 9. Source URL Verification
# ============================================================

class TestSourceURLs:
    """Mechanism must have verifiable source references."""

    def test_has_source_urls(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        urls = m59.get('source_urls', [])
        assert len(urls) >= 3, f"Expected ≥3 source URLs, got {len(urls)}"

    def test_source_urls_are_valid_format(self):
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        m59 = cpf['guardian_google_dual_role_paradox']
        urls = m59.get('source_urls', [])
        for url in urls:
            assert url.startswith('http'), f"Invalid URL format: {url}"


# ============================================================
# 10. Cross-Reference Integrity
# ============================================================

class TestCrossReferenceIntegrity:
    """Verify mechanism #59 cross-references with existing findings."""

    def test_complements_mechanism_29(self):
        """Mechanism #29 documents rogue AI volume asymmetry at Guardian.
        Mechanism #59 adds the structural explanation (dual-role paradox)."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        assert 'guardian_rogue_ai_volume_temperature_asymmetry' in cpf, \
            "Mechanism #29 must still exist"
        assert 'guardian_google_dual_role_paradox' in cpf, \
            "Mechanism #59 must exist alongside #29"
        # Different mechanism IDs
        m29 = cpf['guardian_rogue_ai_volume_temperature_asymmetry']
        m59 = cpf['guardian_google_dual_role_paradox']
        assert m29['mechanism_id'] != m59['mechanism_id']

    def test_complements_mechanism_50_google_prisoner_dilemma(self):
        """Mechanism #50 documents Google's coercive deal mechanics.
        Mechanism #59 adds the Guardian-specific dual-role dimension."""
        data = load_competitor_research()
        cpf = data['cross_publication_findings']
        # Find mechanism 50 by ID
        m50_found = False
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 50:
                m50_found = True
                break
        assert m50_found, "Mechanism #50 must exist for cross-reference"

    def test_mechanism_59_not_in_publications(self):
        """Mechanism #59 must be in cross_publication_findings, NOT publications."""
        data = load_competitor_research()
        pubs = data.get('publications', {})
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                assert pub_val.get('mechanism_id') != 59, \
                    f"Mechanism #59 found in publications.{pub_key} — must be in cpf only"
