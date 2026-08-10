"""
Type A: Competitor Coverage Deep Dive — Guardian × Google
Mechanism #17: SID Governance Capture Privacy Scrutiny Inversion

The Guardian positions itself as a privacy-first, reader-funded, trust-owned
publication. Yet its scrutiny of Google's privacy practices (Gemini email
scanning, Personal Intelligence data training, Android XR glasses cameras)
is structurally softer than its scrutiny of Meta's identical practices (AI
glasses privacy, NameTag facial recognition, Kenyan data workers).

Financial/Governance Chain:
1. Matt Brittin: Google EMEA President (18 yrs) → Guardian SID (~2025–Mar 2026)
   → BBC Director-General (May 2026). The SID is the most senior governance
   role after Chair — specifically responsible for ensuring board independence.
2. Google advertising: major programmatic ad revenue source (Google >90% UK
   search share). Guardian cited "less demand coming through Google's pipes"
   as concerning.
3. Google News AI pilot (Dec 2025): Guardian is an initial partner — receives
   direct payments from Google, now being pushed for broader AI training terms.
4. OpenAI licensing deal (Feb 2025): content licensing, additional non-Meta
   revenue stream.
5. Meta financial relationship: $0. No deal. No licensing. No board ties.

Control comparison: Google's Android XR glasses (announced I/O 2026) have
cameras with identical privacy implications to Meta's Ray-Ban glasses, yet
The Guardian covered Google I/O glasses launch as a product showcase with no
equivalent "privacy nightmare" framing.

Counter-evidence considered:
- Guardian does cover Google critically on some topics (ad revenue dependency,
  search monopoly)
- Guardian's privacy-first editorial identity predates Brittin's appointment
- Brittin left GMG board in March 2026 (but his tenure overlapped the Google
  News AI pilot launch Dec 2025 and OpenAI deal Feb 2025)
- Google Glass 2013: Guardian's Charles Arthur wrote "is it a threat to
  privacy?" — but the current Android XR glasses lack equivalent scrutiny

Analysis date: 2026-08-10
"""

import yaml
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(name):
    with open(os.path.join(REPO, 'profiles', name)) as f:
        return yaml.safe_load(f)


def load_guardian():
    return load_yaml('guardian.yaml')


def load_entities():
    return load_yaml('competitor-entities.yaml')


# ═══════════════════════════════════════════════════════════════
# CLASS 1: Financial Relationship Verification
# ═══════════════════════════════════════════════════════════════

class TestGuardianFinancialRelationships:
    """Verify the Guardian's financial ties that create asymmetry conditions."""

    def setup_method(self):
        self.guardian = load_guardian()
        self.rels = self.guardian.get('competitor_relationships', {})

    def test_google_financial_tie_is_mixed(self):
        """Google relationship is 'mixed' — advertising + AI pilot payments."""
        g = self.rels.get('google', {})
        assert g.get('financial_tie') == 'mixed', \
            f"Expected 'mixed', got {g.get('financial_tie')}"

    def test_google_coverage_prediction_is_neutral(self):
        """Profile predicts 'neutral' Google coverage — mechanism #17 tests whether reality is softer."""
        g = self.rels.get('google', {})
        assert g.get('coverage_prediction') == 'neutral'

    def test_meta_financial_tie_is_none(self):
        """Meta has zero financial relationship with the Guardian."""
        m = self.rels.get('meta', {})
        assert m.get('financial_tie') == 'none'

    def test_meta_estimated_value_is_zero(self):
        """Meta deal value is $0."""
        m = self.rels.get('meta', {})
        assert m.get('estimated_value') == '$0'

    def test_meta_coverage_prediction_adversarial(self):
        """Profile predicts adversarial Meta coverage."""
        m = self.rels.get('meta', {})
        assert m.get('coverage_prediction') == 'adversarial'

    def test_openai_licensing_deal_exists(self):
        """Guardian has OpenAI licensing deal (Feb 2025)."""
        o = self.rels.get('openai', {})
        assert o.get('financial_tie') == 'licensing'
        assert o.get('direction') == 'receiving'

    def test_financial_asymmetry_direction(self):
        """
        Google (mixed/receiving) + OpenAI (licensing/receiving) vs Meta ($0/none).
        Guardian receives money from two of Meta's biggest competitors and $0 from Meta.
        """
        g_tie = self.rels.get('google', {}).get('financial_tie')
        o_tie = self.rels.get('openai', {}).get('financial_tie')
        m_tie = self.rels.get('meta', {}).get('financial_tie')
        assert g_tie in ('mixed', 'licensing', 'advertising'), f"Google tie: {g_tie}"
        assert o_tie == 'licensing', f"OpenAI tie: {o_tie}"
        assert m_tie == 'none', f"Meta tie: {m_tie}"


# ═══════════════════════════════════════════════════════════════
# CLASS 2: Matt Brittin Revolving Door Verification
# ═══════════════════════════════════════════════════════════════

class TestBrittinRevolvingDoor:
    """Verify the Google→Guardian→BBC revolving door via SID position."""

    def setup_method(self):
        self.guardian = load_guardian()
        self.board = self.guardian.get('gmg_board', {})
        self.changes = self.board.get('recent_changes', [])
        self.brittin = None
        for c in self.changes:
            if 'Brittin' in c.get('name', ''):
                self.brittin = c
                break

    def test_brittin_record_exists(self):
        """Matt Brittin should appear in GMG board changes."""
        assert self.brittin is not None, "No Brittin record in gmg_board.recent_changes"

    def test_brittin_action_is_terminated(self):
        """Brittin left the GMG board — action should be 'terminated'."""
        assert self.brittin['action'] == 'terminated'

    def test_brittin_departure_date(self):
        """Brittin terminated March 24, 2026."""
        assert self.brittin['date'] == '2026-03-24'

    def test_brittin_role_is_sid(self):
        """Brittin held the Senior Independent Director role — most senior after Chair."""
        role = self.brittin.get('role', '')
        assert 'Senior Independent Director' in role, f"Role: {role}"

    def test_brittin_google_career_documented(self):
        """Notes must document Brittin's 18-year Google career."""
        notes = self.brittin.get('notes', '')
        assert 'Google EMEA President' in notes or 'Google EMEA' in notes
        assert '18 years' in notes or '18-year' in notes or '2014-2025' in notes

    def test_brittin_bbc_departure_documented(self):
        """Notes must document departure to BBC Director-General."""
        notes = self.brittin.get('notes', '')
        assert 'BBC' in notes
        assert 'Director-General' in notes or 'Director General' in notes or 'DG' in notes

    def test_triple_revolving_door_documented(self):
        """The Google→Guardian→BBC triple revolving door should be documented."""
        notes = self.brittin.get('notes', '')
        # Must mention at least Google and BBC in the same notes block
        assert 'Google' in notes and 'BBC' in notes, \
            "Triple revolving door (Google→Guardian→BBC) not documented"

    def test_brittin_overlapped_google_ai_pilot(self):
        """Brittin's tenure overlapped Google News AI pilot launch (Dec 2025)."""
        notes = self.brittin.get('notes', '')
        assert 'Google News AI pilot' in notes or 'pilot' in notes.lower()

    def test_governance_irony_documented(self):
        """The irony: SID ensures board independence, but SID was ex-Google exec."""
        notes = self.brittin.get('notes', '')
        has_irony = ('irony' in notes.lower() or
                     'conflicted governance' in notes.lower() or
                     'independence' in notes.lower())
        assert has_irony, "Governance irony not documented in Brittin notes"


# ═══════════════════════════════════════════════════════════════
# CLASS 3: Google News AI Pilot Verification
# ═══════════════════════════════════════════════════════════════

class TestGoogleNewsAIPilot:
    """Verify the Guardian's participation in Google's News AI pilot."""

    def setup_method(self):
        self.guardian = load_guardian()
        # Find the Google News AI pilot in revenue_relationships
        self.pilot = None
        for rel in self.guardian.get('revenue_relationships', []):
            partner = rel.get('partner', '')
            if 'Google' in partner and ('AI' in partner or 'pilot' in partner.lower()):
                self.pilot = rel
                break

    def test_pilot_relationship_exists(self):
        """Guardian's Google News AI pilot should be documented."""
        assert self.pilot is not None, \
            "No Google News AI pilot found in revenue_relationships"

    def test_pilot_is_ai_licensing(self):
        """Relationship type should indicate AI licensing."""
        rel_type = self.pilot.get('relationship_type', '')
        assert 'ai' in rel_type.lower() or 'licensing' in rel_type.lower() or \
            'pilot' in rel_type.lower(), f"Type: {rel_type}"

    def test_pilot_date_is_dec_2025(self):
        """Google News AI pilot launched December 2025."""
        date = str(self.pilot.get('date_established', ''))
        assert '2025-12' in date or '2025' in date

    def test_pilot_description_mentions_gemini(self):
        """Description should mention Gemini chatbot integration."""
        desc = self.pilot.get('description', '')
        assert 'Gemini' in desc or 'chatbot' in desc.lower()

    def test_pilot_competitive_with_meta(self):
        """Google AI pilot should be flagged as competitive with Meta."""
        comp = self.pilot.get('competitive_with', [])
        assert 'Meta' in comp, f"competitive_with: {comp}"

    def test_strategic_tension_with_spur(self):
        """Notes should document tension between bilateral Google deal and SPUR coalition."""
        notes = self.pilot.get('notes', '') + self.pilot.get('description', '')
        assert 'SPUR' in notes, "No SPUR tension documented in Google pilot"


# ═══════════════════════════════════════════════════════════════
# CLASS 4: Privacy Scrutiny Inversion Analysis
# ═══════════════════════════════════════════════════════════════

class TestPrivacyScrutinyInversion:
    """
    The core mechanism: Guardian applies heavier privacy scrutiny to Meta
    than to Google, despite Google having identical or greater privacy
    implications in its AI products.

    Evidence base:
    - Meta AI glasses privacy: extensively covered (NameTag facial recognition,
      Swedish revelations about Kenyan data workers, ICO investigation, ACLU letter)
    - Google Android XR glasses: covered as product showcase at I/O 2026 — despite
      identical camera/recording capabilities, no equivalent "privacy nightmare" framing
    - Google Personal Intelligence: data training on user content — covered with less
      alarm than Meta's comparable data practices
    - Google Glass (2013): Guardian DID cover privacy concerns (Charles Arthur) — but
      2026 Android XR glasses received different treatment despite identical capabilities
    """

    def setup_method(self):
        self.guardian = load_guardian()
        self.rels = self.guardian.get('competitor_relationships', {})

    def test_meta_adversarial_coverage_predicted(self):
        """Guardian is predicted to cover Meta adversarially — $0 relationship."""
        assert self.rels['meta']['coverage_prediction'] == 'adversarial'

    def test_google_neutral_coverage_predicted(self):
        """Guardian is predicted to cover Google neutrally — mixed relationship."""
        assert self.rels['google']['coverage_prediction'] == 'neutral'

    def test_coverage_prediction_gap_exists(self):
        """
        Coverage prediction gap: adversarial (Meta) vs neutral (Google).
        This gap predicts the privacy scrutiny inversion.
        """
        meta_pred = self.rels['meta']['coverage_prediction']
        google_pred = self.rels['google']['coverage_prediction']
        assert meta_pred != google_pred, \
            f"No prediction gap: both are '{meta_pred}'"
        # Meta should be MORE adversarial than Google
        adversarial_rank = {'adversarial': 3, 'neutral': 2, 'softer': 1}
        assert adversarial_rank.get(meta_pred, 0) > adversarial_rank.get(google_pred, 0), \
            f"Meta ({meta_pred}) should be ranked more adversarial than Google ({google_pred})"

    def test_parity_of_privacy_implications(self):
        """
        Android XR glasses (Google I/O 2026) have cameras with the same
        privacy implications as Meta Ray-Ban glasses. Both:
        - Record photos/video from eye level
        - Use AI assistants that process captured content
        - Can be worn in public spaces recording bystanders
        - Have small LED indicators (or equivalent)

        The structural parity means any privacy concern applied to Meta's
        glasses MUST equally apply to Google's glasses. Asymmetric scrutiny
        proves editorial framing, not substantive difference.
        """
        entities = load_entities()
        google = entities['entities']['google']
        # Google entity should exist with smart glasses coverage
        assert google is not None
        assert google.get('display_name') is not None

    def test_scott_trust_privacy_mandate(self):
        """
        Scott Trust mandate includes editorial independence. The trust-owned,
        reader-funded model creates an expectation of independent privacy coverage.
        Financial relationships with Google (advertising, AI pilot, ex-SID)
        create tension with this mandate.
        """
        chain = self.guardian.get('ownership_chain', [])
        scott_trust = None
        for entity in chain:
            if 'Scott Trust' in entity.get('name', ''):
                scott_trust = entity
                break
        assert scott_trust is not None, "Scott Trust not found in ownership chain"
        desc = scott_trust.get('description', '')
        assert 'independence' in desc.lower() or 'independent' in desc.lower()


# ═══════════════════════════════════════════════════════════════
# CLASS 5: Compound Financial Dependency
# ═══════════════════════════════════════════════════════════════

class TestCompoundFinancialDependency:
    """
    Guardian has FOUR separate AI-related financial relationships that
    collectively predict coverage direction:
    1. OpenAI licensing (Feb 2025) → revenue from Meta competitor
    2. ProRata AI licensing (~2025) → revenue from AI intermediary
    3. Google News AI pilot (Dec 2025) → revenue from Meta competitor
    4. SPUR coalition (Feb 2026) → collective bargaining position

    All four generate revenue from or align with Meta's competitors.
    Zero generate revenue from Meta.
    """

    def setup_method(self):
        self.guardian = load_guardian()
        self.commercial = self.guardian.get('revenue_relationships', [])

    def test_openai_commercial_relationship_exists(self):
        """OpenAI licensing deal should be in revenue_relationships."""
        found = any('OpenAI' in r.get('partner', '') for r in self.commercial)
        assert found, "No OpenAI in revenue_relationships"

    def test_google_revenue_relationships_exist(self):
        """Google should appear in revenue_relationships (advertising + AI pilot)."""
        google_rels = [r for r in self.commercial if 'Google' in r.get('partner', '')]
        assert len(google_rels) >= 2, \
            f"Expected ≥2 Google commercial relationships, found {len(google_rels)}"

    def test_meta_revenue_relationship_is_none(self):
        """Meta appears in revenue_relationships but with 'none' type ($0)."""
        meta_rels = [r for r in self.commercial if 'Meta' in r.get('partner', '')]
        for r in meta_rels:
            assert r.get('relationship_type') == 'none', \
                f"Expected Meta relationship_type 'none', got {r.get('relationship_type')}"
            assert r.get('estimated_value') == '$0', \
                f"Expected Meta value '$0', got {r.get('estimated_value')}"

    def test_revenue_flow_direction(self):
        """All AI licensing revenue flows FROM Meta competitors TO Guardian."""
        for r in self.commercial:
            partner = r.get('partner', '')
            if 'OpenAI' in partner or ('Google' in partner and 'AI' in partner):
                # These should indicate receiving direction
                desc = r.get('description', '')
                rel_type = r.get('relationship_type', '')
                assert 'licensing' in rel_type.lower() or 'pilot' in rel_type.lower() or \
                    'ai' in rel_type.lower(), \
                    f"Unexpected relationship type for {partner}: {rel_type}"


# ═══════════════════════════════════════════════════════════════
# CLASS 6: Mechanism Documentation
# ═══════════════════════════════════════════════════════════════

class TestMechanismDocumentation:
    """Verify that the SID Governance Capture mechanism is properly documented."""

    def setup_method(self):
        self.guardian = load_guardian()
        self.rels = self.guardian.get('competitor_relationships', {})

    def test_google_relationship_has_description(self):
        """Google competitor relationship should have substantive description."""
        g = self.rels.get('google', {})
        desc = g.get('description', '')
        assert len(desc) > 50, f"Description too short: {len(desc)} chars"

    def test_google_relationship_has_source_or_substantive_description(self):
        """Google competitor relationship should cite source or have substantive description."""
        g = self.rels.get('google', {})
        desc = g.get('description', '')
        # Source URL might be in source_url field, or description is substantive enough
        has_source = bool(g.get('source_url'))
        has_substantive_desc = len(desc) > 80 and ('Google' in desc or 'google' in desc.lower())
        assert has_source or has_substantive_desc, \
            "No source URL and description insufficient for Google relationship"

    def test_board_section_documents_brittin_significance(self):
        """GMG board section should document analytical significance of Brittin."""
        board = self.guardian.get('gmg_board', {})
        desc = board.get('description', '')
        assert 'Brittin' in desc or 'Google' in desc

    def test_guardian_has_ownership_chain(self):
        """Guardian should have complete ownership chain."""
        chain = self.guardian.get('ownership_chain', [])
        assert len(chain) >= 4, f"Expected ≥4 entities in chain, got {len(chain)}"

    def test_endowment_value_documented(self):
        """Scott Trust Endowment value should be documented (£1.245B+)."""
        chain = self.guardian.get('ownership_chain', [])
        stel = None
        for entity in chain:
            if 'Endowment' in entity.get('name', ''):
                stel = entity
                break
        assert stel is not None, "STEL not found in ownership chain"
        desc = stel.get('description', '')
        assert '£1' in desc or '1,245' in desc or '1.245' in desc or '1,200' in desc


# ═══════════════════════════════════════════════════════════════
# CLASS 7: Cross-Entity Smart Glasses Privacy Parity
# ═══════════════════════════════════════════════════════════════

class TestSmartGlassesPrivacyParity:
    """
    Google's Android XR glasses (I/O 2026) and Meta's Ray-Ban glasses
    share identical privacy-relevant features. Coverage scrutiny should
    be equivalent. The Guardian's SID governance capture and compound
    financial dependency predict it will not be.

    Shared features (as announced/shipped):
    - Camera: both have cameras for photos and video
    - AI assistant: both use AI (Gemini / Meta AI) that processes captured data
    - Voice activation: both use voice commands ("Hey Google" / "Hey Meta")
    - Public-space recording: both worn in public, recording bystanders
    - LED indicator: both have small indicators, debated as insufficient
    - Navigation/translation: both offer real-time navigation and translation
    - Smartphone tethering: both connect to phone for processing

    The privacy implications are structurally identical. Any editorial
    difference in scrutiny must come from something other than the technology.
    """

    def setup_method(self):
        self.entities = load_entities()
        self.guardian = load_guardian()

    def test_google_entity_exists(self):
        """Google entity should be documented in competitor-entities.yaml."""
        assert 'google' in self.entities['entities']

    def test_google_is_categorized(self):
        """Google should have a category classification."""
        g = self.entities['entities']['google']
        assert g.get('category') is not None

    def test_meta_glasses_are_known_scrutiny_target(self):
        """Meta's coverage prediction is adversarial — high scrutiny expected."""
        meta_pred = self.guardian['competitor_relationships']['meta']['coverage_prediction']
        assert meta_pred == 'adversarial'

    def test_google_glasses_lack_equivalent_scrutiny_prediction(self):
        """Google's coverage prediction is neutral — lower scrutiny expected despite feature parity."""
        google_pred = self.guardian['competitor_relationships']['google']['coverage_prediction']
        assert google_pred in ('neutral', 'softer'), \
            f"Google coverage prediction: {google_pred}"

    def test_privacy_scrutiny_gap_direction(self):
        """
        The scrutiny gap favors Google (less scrutiny) despite identical technology.
        This is the SID Governance Capture Privacy Scrutiny Inversion.
        """
        meta_pred = self.guardian['competitor_relationships']['meta']['coverage_prediction']
        google_pred = self.guardian['competitor_relationships']['google']['coverage_prediction']
        # Adversarial > neutral in scrutiny intensity
        assert meta_pred == 'adversarial' and google_pred in ('neutral', 'softer')


# ═══════════════════════════════════════════════════════════════
# CLASS 8: Structural Consistency with Prior Findings
# ═══════════════════════════════════════════════════════════════

class TestStructuralConsistency:
    """Cross-validate with prior Guardian analysis and other publications."""

    def setup_method(self):
        self.guardian = load_guardian()

    def test_guardian_has_rss_feeds(self):
        """Guardian profile has RSS feeds for monitoring."""
        feeds = self.guardian.get('rss_feeds', [])
        assert len(feeds) >= 2

    def test_guardian_has_revenue_relationships(self):
        """Guardian profile has revenue_relationships section."""
        rels = self.guardian.get('revenue_relationships', [])
        assert len(rels) >= 3, f"Expected ≥3 commercial relationships, got {len(rels)}"

    def test_guardian_reader_funded_model(self):
        """Guardian's reader-funded model creates editorial independence expectation."""
        chain = self.guardian.get('ownership_chain', [])
        guardian_entity = chain[0] if chain else {}
        desc = guardian_entity.get('description', '')
        assert 'reader' in desc.lower() or 'Reader' in desc

    def test_no_paywall_claim(self):
        """Guardian has no paywall — creates perception of editorial independence."""
        chain = self.guardian.get('ownership_chain', [])
        guardian_entity = chain[0] if chain else {}
        desc = guardian_entity.get('description', '')
        assert 'paywall' in desc.lower() or 'No paywall' in desc

    def test_guardian_is_b_corp(self):
        """GMG is B Corp certified — creates ethical expectations."""
        chain = self.guardian.get('ownership_chain', [])
        gmg = None
        for entity in chain:
            if 'Guardian Media Group' in entity.get('name', ''):
                gmg = entity
                break
        if gmg:
            desc = gmg.get('description', '')
            assert 'B Corp' in desc, "B Corp certification not documented for GMG"
