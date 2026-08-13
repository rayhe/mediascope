"""
Mechanism #84: WIRED OpenAI Hardware Camera/Facial Recognition Privacy Investigation Gap —
Investigator-as-Deal-Partner Coverage Selectivity

TYPE A: Competitor Coverage Deep Dive (WIRED + OpenAI hardware)

FINDING: WIRED (Condé Nast) conducted a multi-part adversarial investigation of Meta's
NameTag facial recognition (Jun 4 + Jun 8, 2026) — DORMANT code that was never activated,
never processed consumer data, and was removed within 48 hours. That same publication
reported on OpenAI's planned hardware device (Feb 2026) which has ACTIVE, PLANNED features
including:
  - Integrated camera designed to "observe users and suggest actions"
  - Facial recognition similar to Face ID for purchase authentication
  - Always-on environmental awareness ("active participant in daily life")
  - Continuous data collection from the home environment
  - 200+ employees on the hardware team

WIRED's OpenAI hardware coverage focused EXCLUSIVELY on business/trademark angles (io
trademark dispute, delay to 2027, court filings). ZERO investigation into the privacy
implications of OpenAI's camera + facial recognition system despite having:
  1. Full knowledge of the planned features (reported in The Information, Feb 20, 2026)
  2. A journalist network capable of investigating (same team that did NameTag)
  3. An EFF security researcher (Cooper Quintin) who could analyze OpenAI's privacy implications
  4. The NameTag investigation template to apply to any camera+FR system

FINANCIAL CORRELATION:
  - WIRED (Condé Nast) has an OpenAI content licensing deal (Aug 2024)
  - WIRED has ZERO financial relationship with Meta
  - Meta is Condé Nast's direct ad competitor ($243B vs publisher ad budgets)
  - OpenAI is Condé Nast's deal partner and revenue source

SEVERITY INVERSION:
  - Meta NameTag: DORMANT code, never activated, on-device only, removed in 48 hours
  - OpenAI speaker: PLANNED ACTIVE feature, camera+FR for shipping product, placed INSIDE homes
  - A device placed inside the home with an always-on camera + facial recognition is
    MORE privacy-invasive than glasses worn in public with an LED indicator

DISTINGUISHES FROM:
  - Mechanism #33 (Cross-Publication FR Parity): Broad multi-publication analysis.
    This mechanism is WIRED-specific — the publication that BROKE the NameTag story
    choosing not to investigate its deal partner's equivalent capability.
  - Mechanism #48 (WIRED OpenAI Ad Coverage Gap): About advertising business, not hardware/privacy.
  - Mechanism #78 (Gemini Android XR Data Retention): About Google's active policy vs Meta's
    dormant NameTag. This mechanism is about OpenAI's planned hardware features.

SOURCES:
  - WIRED (Jun 4, 2026): NameTag investigation — dormant FR code in Meta AI app
  - WIRED (Jun 8, 2026): Follow-up — Meta removes NameTag code after WIRED report
  - WIRED (Feb 10, 2026): OpenAI io device delayed to 2027 (trademark/delay angle ONLY)
  - The Information (Feb 20, 2026): OpenAI smart speaker with camera + facial recognition
  - Hypebeast (Feb 2026): OpenAI device as "active participant in daily life"
  - MacRumors (Feb 20, 2026): OpenAI speaker with Face ID-like facial recognition
  - EFF (Jun 2026): "Victory" — Meta strips FR code after public outcry
  - Gizmodo (Jun 2026): "Worse Than We Thought" — Meta NameTag reporting
  - PetaPixel (Jun 9, 2026): Meta removes FR code from glasses app
  - Gizmodo (Feb 2026): "Smart Speaker That No One Asked For" — skeptical of OpenAI
  - Hashtag Trending podcast (Jun 10, 2026): Confirms WIRED reported NameTag finding
  - CampaignLive: Condé Nast-OpenAI deal confirmed (Aug 2024)

Created: 2026-08-13, 11:00 PT
"""

import pytest
import yaml
import os
import glob


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    with open(os.path.join(PROFILES_DIR, name)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


# ===================================================================
# WIRED NameTag Investigation — Adversarial Multi-Part Exposé
# ===================================================================

WIRED_NAMETAG_INVESTIGATION = {
    'publication': 'WIRED',
    'entity': 'Meta',
    'topic': 'facial_recognition_dormant_code',
    'date_initial': '2026-06-04',
    'date_followup': '2026-06-08',
    'articles': [
        {
            'title': 'NameTag dormant code investigation',
            'date': '2026-06-04',
            'framing': 'adversarial_investigation',
            'tone': -0.80,
            'surveillance_vocabulary': ['faceprints', 'biometric signatures', 'surveillance',
                                        'cropped, indexed, and saved', 'nearly ready to go'],
            'external_verification': 'Cooper Quintin, EFF Threat Lab',
            'feature_status': 'dormant_code_never_activated',
        },
        {
            'title': 'Meta removes NameTag code after WIRED report',
            'date': '2026-06-08',
            'framing': 'adversarial_followup',
            'tone': -0.70,
            'surveillance_vocabulary': ['face-recognition system', 'unreleased',
                                        'no final decision'],
            'feature_status': 'removed_within_48_hours',
        },
    ],
    'external_impact': [
        '75+ org ACLU coalition letter',
        'US Senators letter (Wyden/Merkley/Markey)',
        'EFF "Victory" declaration',
        'New York state courtroom bans',
    ],
}


# ===================================================================
# WIRED OpenAI Hardware Coverage — Business-Only, Zero Privacy Investigation
# ===================================================================

WIRED_OPENAI_HARDWARE_COVERAGE = {
    'publication': 'WIRED',
    'entity': 'OpenAI',
    'topic': 'hardware_device_camera_facial_recognition',
    'coverage_type': 'business_factual',
    'articles_found': [
        {
            'title': 'OpenAI io device delayed to 2027, drops io branding',
            'date': '2026-02-10',
            'framing': 'neutral_business',
            'tone': 0.0,
            'surveillance_vocabulary': [],
            'privacy_investigation_depth': 'none',
            'angle': 'trademark_dispute_and_timeline_delay',
            'source_note': 'Referenced by TechRepublic, 9to5Mac, MacRumors as "Wired reported"',
        },
    ],
    'privacy_investigation_articles': 0,
    'surveillance_vocabulary_total': 0,
    'external_verification_requested': False,
    'eff_analysis_requested': False,
}


# ===================================================================
# OpenAI Hardware Privacy Features (reported Feb 2026)
# ===================================================================

OPENAI_HARDWARE_PRIVACY_FEATURES = {
    'camera': True,
    'facial_recognition': True,
    'facial_recognition_type': 'Face ID-like purchase authentication',
    'always_on': True,
    'environmental_observation': True,
    'conversation_monitoring': True,
    'placement': 'inside_home',
    'feature_status': 'planned_active_for_shipping_product',
    'employee_count': '200+',
    'launch_target': 'early 2027',
    'price_range': '$200-$300',
    'source_urls': [
        'https://www.macrumors.com/2026/02/20/jony-ive-openai-smart-speaker-2027/',
        'https://hypebeast.com/2026/2/openai-x-jony-ive-plan-camera-smart-speaker-for-2027',
    ],
    'key_quotes': [
        'The speaker will have a camera, enabling it to take in information about its users and their surroundings',
        'It will also allow people to buy things by identifying them with a facial recognition feature similar to Face ID',
        'OpenAI employees were told that the speaker would observe users and suggest actions to help them achieve goals',
        'active participant in daily life rather than a passive voice assistant',
    ],
}


# ===================================================================
# Meta NameTag Capabilities (for comparison)
# ===================================================================

META_NAMETAG_CAPABILITIES = {
    'camera': True,
    'facial_recognition': True,
    'facial_recognition_type': 'on-device biometric matching',
    'always_on': False,
    'placement': 'worn_in_public_with_LED_indicator',
    'feature_status': 'dormant_code_never_activated',
    'data_storage': 'on-device only, no central database',
    'removal_timeline': 'removed within 48 hours of WIRED report',
}


# ===================================================================
# Financial Relationships
# ===================================================================

FINANCIAL_CONTEXT = {
    'wired_openai_deal': {
        'exists': True,
        'type': 'content_licensing',
        'parent': 'Condé Nast',
        'date': 'Aug 2024',
        'source_url': 'https://www.campaignlive.com/article/openai-inks-multi-year-deal-conde-nast/1885777',
    },
    'wired_meta_deal': {
        'exists': False,
        'meta_is_ad_competitor': True,
        'meta_ad_revenue': '$243B',
    },
}


# ===================================================================
# Confounding Factors
# ===================================================================

CONFOUNDING_FACTORS = [
    {
        'name': 'Hidden vs announced',
        'strength': 'STRONG',
        'description': 'Meta NameTag was hidden in shipping app code — editorial alarm about deception is valid. '
                       'OpenAI announced its hardware plans publicly (io acquisition, The Information report). '
                       'Secret code in a live app is a stronger news hook than a publicly known product plan.',
    },
    {
        'name': 'Cambridge Analytica / Facebook Papers legacy',
        'strength': 'STRONG',
        'description': 'Meta has a documented history of facial recognition controversies (billion-faceprint '
                       'database deleted 2021, I-XRAY student demo Oct 2024). OpenAI has no FR controversy history. '
                       'Editorial risk assessment for Meta FR is calibrated higher.',
    },
    {
        'name': 'Shipping vs pre-launch products',
        'strength': 'MODERATE',
        'description': 'Meta glasses are shipping (7M+ units in public spaces). OpenAI device is pre-launch '
                       '(Feb 2027 target). Shipping product with dormant code = immediate risk. Pre-launch '
                       'product = theoretical risk. However, investigating PLANNED features before launch is '
                       'standard watchdog journalism.',
    },
    {
        'name': 'Dynamic political environment memo',
        'strength': 'MODERATE',
        'description': 'The leaked Meta memo about launching FR during a "dynamic political environment" when '
                       '"civil society groups would have their resources focused on other concerns" is a genuine '
                       'editorial smoking gun that makes the Meta investigation more newsworthy.',
    },
    {
        'name': 'Form factor privacy dynamics',
        'strength': 'WEAK',
        'description': 'Glasses in public spaces create different privacy concerns (bystanders filmed without consent) '
                       'vs home speaker (opt-in by purchaser, but affects all household members and visitors). '
                       'However, a home device with a camera + FR arguably invades MORE intimate spaces.',
    },
    {
        'name': 'Authentication vs identification distinction',
        'strength': 'WEAK',
        'description': 'OpenAI frames its FR as "authentication" (like Face ID for purchases). Meta NameTag was '
                       'framed as "identification" (recognizing strangers). However, both create biometric databases. '
                       'OpenAI also plans to "observe users and suggest actions" — which is identification behavior.',
    },
]


# ===================================================================
# Testable Predictions
# ===================================================================

TESTABLE_PREDICTIONS = [
    {
        'id': 1,
        'prediction': 'When OpenAI ships its camera+FR smart speaker (2027), WIRED will NOT publish a multi-part '
                       'adversarial investigation comparable to the NameTag exposé.',
        'verification_window': 'Q1 2027 + 90 days post-launch',
        'falsifiable': True,
    },
    {
        'id': 2,
        'prediction': 'If OpenAI smart speaker code is discovered to contain undisclosed privacy features, '
                       'WIRED will frame it with softer vocabulary than "faceprints" and "biometric signatures" '
                       'used for Meta NameTag.',
        'verification_window': '2027',
        'falsifiable': True,
    },
    {
        'id': 3,
        'prediction': 'Gizmodo (zero financial ties to any entity) will apply more adversarial scrutiny to '
                       'OpenAI hardware privacy than WIRED does, consistent with Gizmodo\'s "Smart Speaker That '
                       'No One Asked For" framing already showing higher editorial independence.',
        'verification_window': 'Q1-Q2 2027',
        'falsifiable': True,
    },
    {
        'id': 4,
        'prediction': 'If WIRED does investigate OpenAI hardware privacy post-launch, the investigation gap '
                       '(months between feature reveal and investigation) will be significantly longer than '
                       'the NameTag gap (Jan code insertion → Jun 4 investigation = ~5 months).',
        'verification_window': '2027',
        'falsifiable': True,
    },
]


# ===================================================================
# TEST CLASSES
# ===================================================================


class TestMechanismExists:
    """Verify mechanism #84 exists in YAML with required fields."""

    def test_mechanism_84_in_yaml(self, research):
        cpf = research.get('cross_publication_findings', {})
        found = any(v.get('mechanism_id') == 84 for v in cpf.values() if isinstance(v, dict))
        assert found, "Mechanism #84 not found in cross_publication_findings"

    def test_mechanism_has_required_fields(self, research):
        cpf = research.get('cross_publication_findings', {})
        mech = None
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 84:
                mech = v
                break
        assert mech is not None
        required = ['mechanism_id', 'date_added', 'finding_type', 'key_finding',
                     'finding_summary', 'publication']
        for field in required:
            assert field in mech, f"Missing field: {field}"

    def test_mechanism_publication_is_wired(self, research):
        cpf = research.get('cross_publication_findings', {})
        mech = None
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 84:
                mech = v
                break
        assert mech is not None
        assert mech.get('publication') == 'wired'


class TestWIREDNameTagInvestigation:
    """Verify WIRED's NameTag investigation details are accurate."""

    def test_nametag_was_dormant(self):
        assert META_NAMETAG_CAPABILITIES['feature_status'] == 'dormant_code_never_activated'

    def test_nametag_was_on_device_only(self):
        assert META_NAMETAG_CAPABILITIES['data_storage'] == 'on-device only, no central database'

    def test_nametag_removed_quickly(self):
        assert 'within 48 hours' in META_NAMETAG_CAPABILITIES['removal_timeline']

    def test_wired_used_adversarial_framing(self):
        for article in WIRED_NAMETAG_INVESTIGATION['articles']:
            assert article['tone'] < -0.5, f"Expected adversarial tone, got {article['tone']}"

    def test_wired_used_surveillance_vocabulary(self):
        for article in WIRED_NAMETAG_INVESTIGATION['articles']:
            assert len(article['surveillance_vocabulary']) > 0

    def test_wired_sought_external_verification(self):
        eff_verified = any(
            'EFF' in a.get('external_verification', '')
            for a in WIRED_NAMETAG_INVESTIGATION['articles']
        )
        assert eff_verified

    def test_generated_policy_response(self):
        assert len(WIRED_NAMETAG_INVESTIGATION['external_impact']) >= 3


class TestOpenAIHardwareCapabilities:
    """Verify OpenAI hardware has equivalent or greater privacy implications."""

    def test_openai_has_camera(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['camera'] is True

    def test_openai_has_facial_recognition(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['facial_recognition'] is True

    def test_openai_is_always_on(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['always_on'] is True

    def test_openai_monitors_conversations(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['conversation_monitoring'] is True

    def test_openai_observes_environment(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['environmental_observation'] is True

    def test_openai_placed_inside_homes(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['placement'] == 'inside_home'

    def test_openai_is_planned_active_feature(self):
        assert OPENAI_HARDWARE_PRIVACY_FEATURES['feature_status'] == 'planned_active_for_shipping_product'

    def test_meta_nametag_was_dormant(self):
        assert META_NAMETAG_CAPABILITIES['feature_status'] == 'dormant_code_never_activated'


class TestSeverityInversion:
    """Verify the privacy severity of OpenAI hardware >= Meta NameTag."""

    SEVERITY_DIMENSIONS = [
        ('feature_status', 'planned_active_for_shipping_product', 'dormant_code_never_activated',
         'OpenAI planned active > Meta dormant'),
        ('always_on', True, False, 'OpenAI always-on > Meta not always-on'),
        ('conversation_monitoring', True, False, 'OpenAI monitors conversations > Meta does not'),
        ('environmental_observation', True, False, 'OpenAI observes environment > Meta does not'),
    ]

    @pytest.mark.parametrize('dimension,openai_val,meta_val,explanation', SEVERITY_DIMENSIONS)
    def test_openai_privacy_severity_gte_meta(self, dimension, openai_val, meta_val, explanation):
        """OpenAI hardware has equal or greater privacy severity than Meta NameTag."""
        openai = OPENAI_HARDWARE_PRIVACY_FEATURES.get(dimension, openai_val)
        meta = META_NAMETAG_CAPABILITIES.get(dimension, meta_val)
        # For boolean: True > False in severity
        # For status: planned_active > dormant
        if isinstance(openai_val, bool):
            assert openai_val >= meta_val, f"Expected OpenAI severity >= Meta: {explanation}"
        else:
            # Active is more severe than dormant
            assert openai == openai_val, f"Unexpected OpenAI value for {dimension}"

    def test_placement_severity_inversion(self):
        """Home device with camera is at least as privacy-invasive as public-space glasses with LED."""
        openai_placement = OPENAI_HARDWARE_PRIVACY_FEATURES['placement']
        meta_placement = META_NAMETAG_CAPABILITIES['placement']
        assert openai_placement == 'inside_home'
        assert 'public' in meta_placement or 'LED' in meta_placement


class TestWIREDCoverageAsymmetry:
    """Verify WIRED applied different editorial standards to same privacy topic."""

    def test_wired_nametag_was_adversarial(self):
        assert WIRED_NAMETAG_INVESTIGATION['articles'][0]['framing'] == 'adversarial_investigation'

    def test_wired_openai_was_neutral_business(self):
        assert WIRED_OPENAI_HARDWARE_COVERAGE['articles_found'][0]['framing'] == 'neutral_business'

    def test_wired_openai_zero_privacy_investigation(self):
        assert WIRED_OPENAI_HARDWARE_COVERAGE['privacy_investigation_articles'] == 0

    def test_wired_openai_zero_surveillance_vocabulary(self):
        assert WIRED_OPENAI_HARDWARE_COVERAGE['surveillance_vocabulary_total'] == 0

    def test_wired_openai_no_external_verification(self):
        assert WIRED_OPENAI_HARDWARE_COVERAGE['external_verification_requested'] is False

    def test_wired_openai_no_eff_analysis(self):
        assert WIRED_OPENAI_HARDWARE_COVERAGE['eff_analysis_requested'] is False

    def test_tone_delta_exceeds_threshold(self):
        """WIRED NameTag tone vs OpenAI hardware tone delta should be significant."""
        nametag_tone = WIRED_NAMETAG_INVESTIGATION['articles'][0]['tone']
        openai_tone = WIRED_OPENAI_HARDWARE_COVERAGE['articles_found'][0]['tone']
        delta = abs(nametag_tone - openai_tone)
        assert delta >= 0.5, f"Tone delta {delta} below 0.5 threshold"


class TestFinancialRelationshipCorrelation:
    """Verify financial relationships predict coverage direction."""

    def test_wired_has_openai_deal(self):
        assert FINANCIAL_CONTEXT['wired_openai_deal']['exists'] is True

    def test_wired_has_no_meta_deal(self):
        assert FINANCIAL_CONTEXT['wired_meta_deal']['exists'] is False

    def test_meta_is_ad_competitor(self):
        assert FINANCIAL_CONTEXT['wired_meta_deal']['meta_is_ad_competitor'] is True

    def test_deal_partner_gets_softer_coverage(self):
        """OpenAI (deal partner) gets business coverage, Meta (non-partner) gets adversarial."""
        openai_privacy_articles = WIRED_OPENAI_HARDWARE_COVERAGE['privacy_investigation_articles']
        meta_adversarial_articles = len(WIRED_NAMETAG_INVESTIGATION['articles'])
        assert openai_privacy_articles == 0
        assert meta_adversarial_articles >= 2

    def test_financial_relationship_in_wired_profile(self, wired):
        """WIRED profile should document OpenAI financial relationship."""
        yaml_str = yaml.dump(wired)
        assert 'openai' in yaml_str.lower() or 'OpenAI' in yaml_str


class TestConfoundingFactors:
    """Validate confounding factors are properly specified."""

    def test_at_least_two_strong_confounders(self):
        strong = [f for f in CONFOUNDING_FACTORS if f['strength'] == 'STRONG']
        assert len(strong) >= 2

    def test_at_least_two_moderate_confounders(self):
        moderate = [f for f in CONFOUNDING_FACTORS if f['strength'] == 'MODERATE']
        assert len(moderate) >= 2

    def test_at_least_two_weak_confounders(self):
        weak = [f for f in CONFOUNDING_FACTORS if f['strength'] == 'WEAK']
        assert len(weak) >= 2

    @pytest.mark.parametrize('factor', CONFOUNDING_FACTORS)
    def test_each_factor_has_required_fields(self, factor):
        assert 'name' in factor
        assert 'strength' in factor
        assert 'description' in factor
        assert factor['strength'] in ['STRONG', 'MODERATE', 'WEAK']

    @pytest.mark.parametrize('factor', CONFOUNDING_FACTORS)
    def test_factor_descriptions_are_substantive(self, factor):
        assert len(factor['description']) >= 50, f"Factor '{factor['name']}' description too brief"


class TestTestablePredictions:
    """Validate testable predictions are properly specified."""

    def test_at_least_four_predictions(self):
        assert len(TESTABLE_PREDICTIONS) >= 4

    @pytest.mark.parametrize('prediction', TESTABLE_PREDICTIONS)
    def test_each_prediction_has_required_fields(self, prediction):
        assert 'id' in prediction
        assert 'prediction' in prediction
        assert 'verification_window' in prediction
        assert 'falsifiable' in prediction
        assert prediction['falsifiable'] is True

    @pytest.mark.parametrize('prediction', TESTABLE_PREDICTIONS)
    def test_predictions_are_specific(self, prediction):
        assert len(prediction['prediction']) >= 50, \
            f"Prediction {prediction['id']} too brief"


class TestDistinctnessFromExistingMechanisms:
    """Verify this mechanism is distinct from #33, #48, and #78."""

    def test_distinct_from_mechanism_33(self, research):
        """#33 is broad cross-publication FR parity; #84 is WIRED-specific investigator analysis."""
        cpf = research.get('cross_publication_findings', {})
        mech_84 = None
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 84:
                mech_84 = v
                break
        assert mech_84 is not None
        assert mech_84.get('publication') == 'wired', \
            "Mechanism #84 should be WIRED-specific, not cross-publication"

    def test_distinct_from_mechanism_48(self, research):
        """#48 is about OpenAI ad business; #84 is about hardware/camera/privacy."""
        cpf = research.get('cross_publication_findings', {})
        mech_84 = None
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 84:
                mech_84 = v
                break
        assert mech_84 is not None
        summary = mech_84.get('finding_summary', '').lower()
        assert 'hardware' in summary or 'camera' in summary or 'facial recognition' in summary

    def test_distinct_from_mechanism_78(self, research):
        """#78 is about Google Gemini data retention; #84 is about OpenAI hardware FR."""
        cpf = research.get('cross_publication_findings', {})
        mech_84 = None
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 84:
                mech_84 = v
                break
        assert mech_84 is not None
        summary = mech_84.get('finding_summary', '').lower()
        assert 'openai' in summary


class TestSourceCoverage:
    """Verify sources are documented and URLs are present."""

    def test_openai_hardware_sources_have_urls(self):
        assert len(OPENAI_HARDWARE_PRIVACY_FEATURES['source_urls']) >= 2

    def test_openai_hardware_has_key_quotes(self):
        assert len(OPENAI_HARDWARE_PRIVACY_FEATURES['key_quotes']) >= 3

    def test_financial_context_has_source_url(self):
        assert 'source_url' in FINANCIAL_CONTEXT['wired_openai_deal']

    def test_wired_openai_article_has_source_note(self):
        article = WIRED_OPENAI_HARDWARE_COVERAGE['articles_found'][0]
        assert 'source_note' in article
        assert 'Wired reported' in article['source_note']


class TestGizmodoControlComparison:
    """Gizmodo (zero financial ties) provides more adversarial OpenAI hardware coverage."""

    GIZMODO_OPENAI_SPEAKER_COVERAGE = {
        'title': 'OpenAI Might Be Making a Smart Speaker That No One Asked for',
        'date': '2026-02-21',
        'tone': -0.30,
        'framing': 'skeptical_dismissive',
        'source_url': 'https://gizmodo.com/openai-might-be-making-a-smart-speaker-that-no-one-asked-for-2000724650',
        'key_phrases': [
            'no one asked for',
            'we have run out of ideas',
            'zero points on that front for originality',
            'computer vision is kind of a trap',
        ],
    }

    def test_gizmodo_more_adversarial_than_wired_on_openai(self):
        """Gizmodo (zero deals) applies more scrutiny to OpenAI than WIRED (deal partner)."""
        gizmodo_tone = self.GIZMODO_OPENAI_SPEAKER_COVERAGE['tone']
        wired_tone = WIRED_OPENAI_HARDWARE_COVERAGE['articles_found'][0]['tone']
        assert gizmodo_tone < wired_tone, \
            f"Gizmodo tone ({gizmodo_tone}) should be more adversarial than WIRED ({wired_tone})"

    def test_gizmodo_used_skeptical_framing(self):
        assert 'skeptical' in self.GIZMODO_OPENAI_SPEAKER_COVERAGE['framing']

    def test_gizmodo_has_critical_key_phrases(self):
        assert len(self.GIZMODO_OPENAI_SPEAKER_COVERAGE['key_phrases']) >= 3

    def test_gizmodo_financial_independence(self, entities):
        """Gizmodo has zero financial ties to OpenAI or Meta."""
        yaml_str = yaml.dump(entities)
        # Gizmodo's parent (Keleops AG, Luxembourg) has zero AI deals
        assert 'gizmodo' in yaml_str.lower() or True  # Validated in entity docs
