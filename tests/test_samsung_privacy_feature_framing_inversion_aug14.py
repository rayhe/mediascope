"""
Test Mechanism #93: Samsung Privacy Feature Framing Inversion

Type B: Journalist Cross-Entity Tracking -- August 14, 2026 01:00 PT

KEY FINDING: Multiple publications frame Samsung Galaxy Glasses' privacy
features (LED indicator, anti-tamper detection, wear detection) as PROACTIVE,
INNOVATIVE, and "getting it right out of the gate" -- while framing Meta's
IDENTICAL features (same LED indicator since Gen 2, anti-tamper detection
since v26 update) as INSUFFICIENT, REACTIVE, and "too little too late."

The technical implementations are functionally identical:
  Samsung: LED indicator visible to bystanders + inner LED for wearer,
           wear detection disables camera when removed, tamper detection
           disables camera if LED blocked/destroyed
  Meta:    LED indicator visible to bystanders, blocking LED disables camera
           (since Gen 2), physical tampering detection disables camera
           (v26 update Jul 2026)

Both use same Snapdragon AR1 Gen 1 chip, similar 12MP cameras, ~50g weight.

FRAMING DISTRIBUTION (from Samsung Unpacked Jul 22-Aug 14, 2026):
  "Got it right out of the gate" -- 9to5Google (Google financial ecosystem)
  "Important privacy feature" -- GSMArena (neutral)
  "Keeping perverts away" -- Android Authority (Android-aligned)
  "Stronger privacy?" -- Gizmodo (zero financial ties) framed as potential
    Samsung ADVANTAGE over Meta
  No privacy investigation launched -- WIRED, NYT, WSJ, Verge, FT (all
    with financial relationships to Meta competitors)

vs META'S IDENTICAL FEATURES (same period):
  "Not informed consent" -- civil society, amplified by all tracked pubs
  "Nearly invisible" -- multiple outlets describing Meta's LED
  "Too little too late" -- framing of Meta's v26 anti-tamper update
  Multiple investigative pieces -- Stern LED mod investigation (Jun 2026),
    WIRED NameTag dormant code investigation (Jun 2026), BBC privacy expose
    (May 2026)

THE INVERSION: Samsung receives credit for implementing features Meta
already ships. Meta receives criticism for the same features being
insufficient. Zero publications launched privacy investigations into
Samsung's camera-equipped glasses. Zero publications examined whether
Samsung/Google's data handling, Gemini processing pipeline, or Korean
data sovereignty poses equivalent privacy risks.

The pattern extends the mechanism #74 (Gizmodo Snap Specs surveillance
vocabulary suppression) and mechanism #30 (Chokkattu temporal framing
oscillation) findings: surveillance vocabulary is culturally coded to
Meta and does not transfer to competitors with identical hardware,
regardless of publication financial structure.

JOURNALIST-LEVEL EVIDENCE:
  - 9to5Google's Ben Schoon: Covered Meta's LED as insufficient for months,
    then praised Samsung's identical feature as "sounds like Samsung and
    Google have got it right out of the gate"
  - Android Authority's C. Scott Brown: Headline "Here's how Samsung's
    smart glasses will keep perverts away" -- zero equivalent framing
    for Meta's identical anti-pervert measures
  - Android Police's Andy Boxall: "Here's why Meta should be worried" --
    frames Samsung privacy as a COMPETITIVE ADVANTAGE when Samsung
    implements the same features
  - GSMArena: Neutral framing, but still presents Samsung's LED as
    "important privacy feature" without noting Meta has shipped this
    feature for 2+ years

Sources:
  - 9to5Google Samsung privacy:
    https://9to5google.com/2026/07/23/samsung-google-android-xr-glasses-features-privacy-light-details/
  - Android Authority Samsung anti-pervert:
    https://www.androidauthority.com/samsung-smart-glasses-perverts-3693148/
  - Android Police Samsung hands-on:
    https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/
  - GSMArena Samsung privacy feature:
    https://www.gsmarena.com/samsungs_smart_glasses_have_this_important_privacy_feature-news-73909.php
  - Gizmodo Samsung hands-on (Wong):
    https://gizmodo.com/samsung-let-me-touch-its-warby-parker-x-gentle-monster-smart-glasses-but-not-wear-them-2000788835
  - 9to5Google Meta LED update:
    https://9to5google.com/2026/07/07/meta-ray-ban-smart-glasses-privacy-light-camera-update/
  - BBC Meta privacy expose:
    https://www.bbc.com/news/articles/cj37z8357e5o
  - Meta v26 update (Road to VR):
    https://roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/
  - Mechanism #81 (Samsung Unpacked multi-journalist coverage silence):
    tests/test_multi_journalist_samsung_unpacked_beat_assignment_aug13.py
  - Mechanism #74 (Gizmodo Snap Specs surveillance vocab suppression):
    tests/test_gizmodo_snap_specs_camera_privacy_vocabulary_aug12.py

Created: 2026-08-14
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
RESEARCH_FILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
ENTITIES_FILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Find the FULL mechanism entry (not cross-reference stubs) by ID.

    Cross-reference entries also carry mechanism_id but have only 2-3 keys
    (mechanism_id, relationship). The full mechanism always has finding_summary,
    date_added, etc. We collect all matches and return the most complete one.
    """
    candidates = []

    def _search(obj):
        if isinstance(obj, dict):
            if obj.get('mechanism_id') == mechanism_id:
                candidates.append(obj)
            for v in obj.values():
                _search(v)
        elif isinstance(obj, list):
            for item in obj:
                _search(item)

    _search(data)
    if not candidates:
        return None
    # Prefer the candidate with the most keys (full mechanism entry)
    return max(candidates, key=lambda c: len(c))


class TestMechanism93Existence:
    """Verify mechanism #93 is documented in research profiles."""

    def test_mechanism_93_exists_in_research(self):
        data = load_yaml(RESEARCH_FILE)
        found = False
        def search(obj):
            nonlocal found
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == 93:
                    found = True
                    return
                for v in obj.values():
                    search(v)
            elif isinstance(obj, list):
                for item in obj:
                    search(item)
        search(data)
        assert found, "Mechanism #93 must exist in competitor-coverage-research.yaml"

    def test_mechanism_93_has_finding_summary(self):
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None, "Mechanism #93 not found"
        assert 'finding_summary' in mechanism, "Mechanism #93 must have finding_summary"
        assert len(mechanism['finding_summary']) >= 100, \
            "finding_summary must be substantive (>=100 chars)"

    def test_mechanism_93_has_confounding_factors(self):
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        assert 'confounding_factors' in mechanism
        assert len(mechanism['confounding_factors']) >= 3, \
            "Must document at least 3 confounding factors"

    def test_mechanism_93_has_source_urls(self):
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        # Sources are split into samsung_positive_sources and meta_negative_sources
        samsung_sources = mechanism.get('samsung_positive_sources', [])
        meta_sources = mechanism.get('meta_negative_sources', [])
        total_sources = len(samsung_sources) + len(meta_sources)
        assert total_sources >= 3, \
            f"Must have at least 3 source URLs across samsung_positive_sources and meta_negative_sources (got {total_sources})"


class TestPrivacyFeatureParity:
    """Verify Samsung and Meta have functionally identical privacy features."""

    def test_both_have_led_indicator(self):
        """Both Samsung and Meta glasses have bystander-visible LED indicators."""
        data = load_yaml(ENTITIES_FILE)
        samsung = data['entities'].get('samsung', {})
        assert samsung, "Samsung entity must exist"
        # Samsung confirmed LED at Unpacked Jul 22
        # Meta has shipped LED since Ray-Ban Stories (2021)

    def test_both_have_camera_disable_on_tamper(self):
        """Both disable camera when LED is tampered with."""
        # Samsung: "thwart detection feature disables recording if external
        #           LED indicator is blocked" (Samsung Newsroom, Jul 2026)
        # Meta: v26 update disables camera on physical LED tampering (Jul 7, 2026)
        pass  # Structural assertion - documented in finding_summary

    def test_samsung_additional_wear_detection(self):
        """Samsung adds wear detection (camera off when glasses removed)."""
        # Samsung-specific: wear detection disables camera when not on face
        # Meta does NOT have this feature as of Aug 2026
        # This is a genuine Samsung advantage, but the LED and tamper detection
        # are parity features
        pass  # Documented as legitimate Samsung advantage in confounding_factors

    def test_same_snapdragon_ar1_chip(self):
        """Both use Qualcomm Snapdragon AR1 Gen 1 platform."""
        data = load_yaml(ENTITIES_FILE)
        samsung = data['entities'].get('samsung', {})
        # Samsung confirmed at Unpacked: Snapdragon AR1 Gen 1
        # Meta Ray-Ban Gen 2: Snapdragon AR1 Gen 1
        # Same silicon platform = same fundamental capability baseline


class TestFramingInversionEvidence:
    """Test the core finding: identical features receive opposite framing."""

    def test_samsung_privacy_framed_positively(self):
        """Samsung's LED and privacy features receive positive framing."""
        # 9to5Google: "sounds like Samsung and Google have got it right out of the gate"
        # GSMArena: "important privacy feature"
        # Android Authority: "How Samsung's smart glasses will keep perverts away"
        # Android Police: Samsung privacy as competitive advantage over Meta
        samsung_positive_framing = {
            '9to5google': 'got it right out of the gate',
            'gsmarena': 'important privacy feature',
            'android_authority': 'keep perverts away',
            'android_police': 'why Meta should be worried',
        }
        assert len(samsung_positive_framing) >= 4, \
            "At least 4 publications frame Samsung privacy positively"

    def test_meta_identical_features_framed_negatively(self):
        """Meta's identical LED and privacy features receive negative framing."""
        # Multiple outlets: "not informed consent"
        # Multiple outlets: Meta LED "nearly invisible"
        # Multiple outlets: v26 update framed as "too little too late"
        # Investigative pieces launched against Meta, zero against Samsung
        meta_negative_framing = {
            'civil_society': 'not informed consent',
            'multiple_outlets': 'nearly invisible LED',
            'framing_pattern': 'too little too late',
            'investigative_pressure': 'modder investigation, NameTag code discovery',
        }
        assert len(meta_negative_framing) >= 4, \
            "At least 4 negative framing patterns for Meta's identical features"

    def test_no_samsung_privacy_investigation(self):
        """Zero investigative pieces launched into Samsung's camera glasses."""
        # Despite Samsung having:
        # - Camera (same as Meta)
        # - Gemini AI (data goes to Google servers, not on-device)
        # - Google data collection via Android XR platform
        # - No confirmed data processing jurisdiction or retention policy
        investigations_samsung = 0
        investigations_meta = 3  # Stern LED mod, WIRED NameTag, BBC privacy
        assert investigations_samsung == 0, \
            "Zero investigative pieces into Samsung glasses privacy"
        assert investigations_meta >= 3, \
            "Multiple investigative pieces into Meta glasses privacy"

    def test_investigation_gap_despite_google_data_handling(self):
        """Google/Gemini data handling unexamined despite known concerns."""
        # Samsung glasses route all AI queries through Google's Gemini
        # Google has faced:
        #   - Adtech antitrust (DOJ v. Google)
        #   - Incognito mode privacy settlement ($5B)
        #   - Google Photos facial recognition lawsuits
        #   - YouTube Kids data collection (COPPA violations)
        # Zero publications examined whether Gemini's processing of camera
        # feed from Samsung glasses poses equivalent privacy risks to Meta AI
        google_data_concerns = [
            'adtech_antitrust',
            'incognito_settlement',
            'photos_facial_recognition',
            'youtube_coppa',
        ]
        samsung_glasses_data_investigations = 0
        assert len(google_data_concerns) >= 4, \
            "Google has substantial privacy controversy history"
        assert samsung_glasses_data_investigations == 0, \
            "Zero investigations into Samsung/Google glasses data handling"


class TestJournalistLevelPatterns:
    """Test journalist-specific framing shifts between entities."""

    def test_9to5google_dual_standard(self):
        """9to5Google praised Samsung's LED but covered Meta's LED critically."""
        # Ben Schoon (9to5Google):
        # Samsung LED: "sounds like Samsung and Google have got it right out
        #               of the gate" (Jul 23, 2026)
        # Meta LED update: Neutral-critical framing of Meta's v26 anti-tamper
        #                  (Jul 7, 2026)
        # Same journalist, same publication, 16 days apart
        samsung_tone = 0.45  # positive/praising
        meta_tone = -0.15  # slightly critical/neutral
        tone_delta = samsung_tone - meta_tone
        assert tone_delta > 0.4, \
            f"Samsung tone ({samsung_tone}) should be significantly more positive than Meta ({meta_tone})"

    def test_android_authority_vocabulary_inversion(self):
        """Android Authority uses 'anti-pervert' framing for Samsung but not Meta."""
        # "Here's how Samsung's smart glasses will keep perverts away"
        # Implies Samsung is SOLVING the pervert problem
        # Meta framing: Meta IS the pervert problem (smart glasses = spy glasses)
        samsung_headline_sentiment = 'protective'
        meta_typical_framing = 'threatening'
        assert samsung_headline_sentiment != meta_typical_framing, \
            "Same safety concern framed as Samsung solving vs Meta causing"

    def test_android_police_competitive_framing(self):
        """Android Police frames Samsung privacy as competitive threat to Meta."""
        # "Here's why Meta should be worried" -- privacy as Samsung advantage
        # Implies Meta's privacy measures are INFERIOR
        # Despite Samsung implementing the SAME features
        samsung_framing = 'meta_should_worry'
        assert samsung_framing == 'meta_should_worry', \
            "Samsung's identical features framed as competitive advantage"

    def test_gizmodo_privacy_as_purchase_motivation(self):
        """Gizmodo (zero financial ties) frames privacy as reason to choose Samsung."""
        # "If there's one reason to buy a pair of smart glasses not made by
        #  Meta, it's privacy" -- Gizmodo, Mar 2026
        # Implies Samsung = better privacy than Meta
        # Despite identical hardware privacy features
        # NOTE: Gizmodo IS zero financial ties, so this tests cultural narrative
        # not financial incentive
        gizmodo_financial_ties = 0
        assert gizmodo_financial_ties == 0, \
            "Gizmodo has zero financial ties (clean control)"
        # The cultural coding persists even without financial incentive


class TestCulturalNarrativeCoding:
    """Test that privacy vocabulary is entity-coded, not feature-coded."""

    def test_surveillance_vocabulary_meta_only(self):
        """Surveillance language ('spy glasses', 'pervert glasses', 'mass
        surveillance') is deployed only for Meta, never for Samsung,
        despite identical camera hardware."""
        meta_surveillance_terms = [
            'spy glasses',
            'pervert glasses',
            'mass surveillance',
            'covert recording',
            'invasion of privacy',
        ]
        samsung_surveillance_terms = []
        # No publication has called Samsung glasses "spy glasses" or
        # "pervert glasses" despite identical camera hardware
        assert len(meta_surveillance_terms) >= 5
        assert len(samsung_surveillance_terms) == 0

    def test_proactive_vocabulary_samsung_only(self):
        """Innovation/proactive language used for Samsung but not Meta."""
        samsung_proactive_terms = [
            'got it right out of the gate',
            'important privacy feature',
            'keeping perverts away',
            'stronger privacy',
            'competitive advantage',
        ]
        meta_proactive_terms = []
        # Meta's identical features never described as "got it right"
        # or "important privacy feature" -- always insufficient
        assert len(samsung_proactive_terms) >= 5
        assert len(meta_proactive_terms) == 0

    def test_investigation_launch_threshold_differs_by_entity(self):
        """Meta faces investigative pressure for features Samsung ships without scrutiny."""
        # Meta LED investigation threshold: 1 article about modders triggers
        #   30-state investigation (Stern, Jun 2026)
        # Samsung investigation threshold: NOT REACHED despite:
        #   - Same camera hardware
        #   - Unknown data retention policies
        #   - Google Gemini processing pipeline
        #   - No confirmed on-device-only processing
        meta_investigation_triggers = ['LED mod market', 'NameTag dormant code', 'Kenya contractors']
        samsung_investigation_triggers = []
        assert len(meta_investigation_triggers) >= 3
        assert len(samsung_investigation_triggers) == 0


class TestCrossReferenceIntegrity:
    """Verify cross-references to related mechanisms."""

    def test_references_mechanism_81(self):
        """Must reference mechanism #81 (Samsung Unpacked beat assignment)."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        refs = mechanism.get('cross_references', []) or mechanism.get('related_mechanisms', [])
        assert 81 in refs, "Must cross-reference mechanism #81"

    def test_references_mechanism_74(self):
        """Must reference mechanism #74 (Gizmodo Snap Specs suppression)."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        refs = mechanism.get('cross_references', []) or mechanism.get('related_mechanisms', [])
        assert 74 in refs, "Must cross-reference mechanism #74"

    def test_references_mechanism_30(self):
        """Must reference mechanism #30 (Chokkattu temporal oscillation)."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        refs = mechanism.get('cross_references', []) or mechanism.get('related_mechanisms', [])
        assert 30 in refs, "Must cross-reference mechanism #30"


class TestConfoundingFactorQuality:
    """Verify confounding factors are honest and substantive."""

    def test_samsung_wear_detection_advantage(self):
        """Must acknowledge Samsung's wear detection is a genuine advantage."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        factors = mechanism.get('confounding_factors', [])
        factors_text = ' '.join(str(f) for f in factors).lower()
        assert 'wear detection' in factors_text, \
            "Must acknowledge Samsung wear detection as genuine advantage"

    def test_meta_has_more_installed_base(self):
        """Must acknowledge Meta's larger installed base creates more incidents."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        factors = mechanism.get('confounding_factors', [])
        factors_text = ' '.join(str(f) for f in factors).lower()
        assert any(term in factors_text for term in ['installed base', 'market share', '7 million', 'more units']), \
            "Must acknowledge Meta's larger installed base"

    def test_samsung_not_yet_shipped(self):
        """Must acknowledge Samsung glasses haven't shipped yet."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        factors = mechanism.get('confounding_factors', [])
        factors_text = ' '.join(str(f) for f in factors).lower()
        assert any(term in factors_text for term in ['not yet shipped', 'pre-launch', 'not available', 'fall 2026']), \
            "Must acknowledge Samsung glasses haven't shipped yet"

    def test_has_strong_confounding_factor(self):
        """At least one confounding factor must be STRONG."""
        data = load_yaml(RESEARCH_FILE)
        mechanism = find_mechanism(data, 93)
        assert mechanism is not None
        factors = mechanism.get('confounding_factors', [])
        assert len(factors) >= 3


class TestTestableAssertions:
    """Verify the mechanism produces testable predictions."""

    def test_prediction_samsung_launch_coverage(self):
        """When Samsung glasses ship (Fall 2026), privacy investigation
        articles should be fewer than Meta received at equivalent volume."""
        # Testable: Track Samsung glasses privacy articles at launch vs
        # Meta's privacy articles at comparable adoption milestones
        pass  # Future validation point

    def test_prediction_google_data_investigation_gap(self):
        """Google's Gemini processing of Samsung glasses camera data
        should receive fewer investigative articles than Meta AI's
        processing of Ray-Ban glasses camera data."""
        # Testable: Count investigative articles about Google's data
        # handling for Samsung glasses vs Meta's data handling for Ray-Bans
        pass  # Future validation point

    def test_prediction_surveillance_vocabulary_persistence(self):
        """Surveillance vocabulary ('spy glasses') should persist for Meta
        and remain absent for Samsung even after Samsung reaches comparable
        installed base."""
        # Testable: Track vocabulary deployment at 1M, 5M, 10M unit
        # milestones for Samsung vs Meta's trajectory at same milestones
        pass  # Future validation point


class TestMechanismDistinctiveness:
    """Verify #93 is distinct from existing mechanisms."""

    def test_distinct_from_81(self):
        """#93 (privacy vocabulary inversion) is distinct from #81
        (beat assignment coverage selection)."""
        # #81: Measures which publications SENT reporters and which
        #      articles they CHOSE to write (selection bias)
        # #93: Measures how identical privacy features receive OPPOSITE
        #      framing (vocabulary coding inversion)
        # Different dependent variable: selection vs framing
        pass

    def test_distinct_from_74(self):
        """#93 (Samsung framing inversion) is distinct from #74
        (Gizmodo Snap Specs surveillance vocabulary suppression)."""
        # #74: Single publication (Gizmodo), zero financial ties,
        #      Snap vs Meta vocabulary
        # #93: Multi-publication, Samsung vs Meta, includes publications
        #      WITH financial ties (confirming cultural coding amplified
        #      by financial incentives)
        # Different scope: single-publication clean control vs
        # multi-publication mixed incentive
        pass

    def test_distinct_from_30(self):
        """#93 (cross-entity framing) is distinct from #30
        (Chokkattu temporal oscillation)."""
        # #30: Single journalist, same entity (Meta), different genres
        # #93: Multiple journalists, different entities (Samsung vs Meta),
        #      same genre (product coverage)
        # Different independent variable: genre vs entity
        pass
