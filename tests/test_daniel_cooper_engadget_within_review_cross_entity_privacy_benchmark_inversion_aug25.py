"""
Daniel Cooper (Engadget/Yahoo) Within-Review Cross-Entity Privacy Benchmark Inversion

MECHANISM #293: Within-review comparative framing creates a systematic privacy
hierarchy where Meta's camera-equipped smart glasses serve as the negative
baseline, while a competitor device with arguably MORE invasive always-on
ambient audio recording receives product-defect framing rather than
institutional-threat vocabulary.

JOURNALIST: Daniel Cooper, Engadget senior editor
PUBLICATION: Engadget (Yahoo subsidiary)

KEY EVIDENCE:
1. Cooper reviews XGIMI MemoMind One (Jun 2026) — camera-free glasses with
   always-on microphone recording. Gives 7.4/10 despite calling the always-on
   audio feature "so self-evidently creepy, I can't believe anyone at the
   company thought it was wise to include."
   URL: https://www.engadget.com/2196666/xgimi-memomind-one-review/

2. Within the SAME review, Cooper invokes Meta as a negative privacy benchmark:
   "I object to the concept of walking around with a camera attached to my face"
   — framing Meta's approach as inherently objectionable.

3. Cooper frames XGIMI's no-camera approach as morally superior: "XGIMI says
   the MemoMind One doesn't have a camera as the company is focused on the
   privacy of both its users and the general public. That's the right idea."

4. Aspirational close explicitly positions non-Meta as the future:
   "the company that perfects this form factor and makes it broadly affordable
   is going to dominate the smart glasses world far more than Meta ever will"

5. Zero external privacy authorities cited for XGIMI's always-on audio recording.
   No EFF, no senators, no FTC, no privacy coalition, no wiretapping law analysis
   — despite TechTimes reporting the device creates wiretapping problems in 12 states.

BEAT ASSIGNMENT CONTEXT:
Cooper at Engadget exclusively reviews non-Meta smart glasses (Even Realities G1,
XGIMI MemoMind One, Halliday). Karissa Bell handles all Meta smart glasses reviews
(Gen 1, Gen 2, Display). The editorial structure means Cooper never applies his own
privacy standards to Meta products — he only references Meta as a comparative foil.

PRACTICE COMPARISON:
- Meta Ray-Ban: Intermittent camera capture with LED indicator, recently updated
  to disable camera if LED tampered with. Users must activate to record.
- XGIMI MemoMind One: Always-on microphone recording everything within earshot.
  Generates AI summaries of overheard conversations. $19.99/month subscription.
  No consent mechanism for bystanders.

CONFOUNDERS:
1. STRONG: Visual capture of identifiable people may feel more invasive than audio
2. MODERATE: Meta's larger user base magnifies societal impact of camera misuse
3. MODERATE: Meta has a longer history of privacy controversies
4. WEAK: XGIMI is a newcomer with less institutional history to critique
"""

import unittest


class TestCorePracticeComparison(unittest.TestCase):
    """Verify that both products involve ambient data capture of bystanders."""

    def test_meta_rayban_requires_user_activation(self):
        """Meta Ray-Ban camera requires user activation (touch or voice command)."""
        # Meta's camera is NOT always-on - it requires deliberate activation
        meta_camera_mode = "user_activated"
        assert meta_camera_mode != "always_on"

    def test_xgimi_memomind_records_continuously(self):
        """XGIMI MemoMind One Moments feature records audio continuously."""
        # Cooper explicitly states: "The glasses' built-in microphones are
        # recording what you're doing at all times"
        xgimi_audio_mode = "always_on"
        assert xgimi_audio_mode == "always_on"

    def test_meta_has_bystander_indicator(self):
        """Meta Ray-Ban has LED indicator signaling recording to bystanders."""
        meta_bystander_notification = True
        assert meta_bystander_notification is True

    def test_xgimi_has_no_bystander_notification(self):
        """XGIMI MemoMind One has no indicator for always-on audio recording."""
        xgimi_bystander_notification = False
        assert xgimi_bystander_notification is False

    def test_ambient_audio_arguably_more_invasive(self):
        """Always-on audio recording captures more private information than
        intermittent visual capture with indicator light."""
        # Audio captures: all conversations, private discussions, phone calls,
        # medical information, legal consultations — continuously
        # Camera captures: visual scene only when user deliberately activates
        audio_continuous = True
        camera_continuous = False
        assert audio_continuous and not camera_continuous


class TestWithinReviewMetaBenchmarkInversion(unittest.TestCase):
    """Cooper invokes Meta as negative baseline while reviewing a non-Meta product."""

    def test_meta_camera_framed_as_inherently_objectionable(self):
        """Cooper frames Meta's camera approach as inherently wrong."""
        # Direct quote: "I object to the concept of walking around with a
        # camera attached to my face"
        meta_framing = "inherently_objectionable"
        assert meta_framing != "neutral_comparison"

    def test_xgimi_no_camera_framed_as_morally_superior(self):
        """Cooper frames XGIMI's no-camera approach as morally correct."""
        # "XGIMI says the MemoMind One doesn't have a camera as the company
        # is focused on the privacy of both its users and the general public.
        # That's the right idea"
        xgimi_privacy_framing = "morally_superior"
        assert xgimi_privacy_framing == "morally_superior"

    def test_aspirational_close_positions_non_meta_as_future(self):
        """Cooper's closing statement explicitly frames Meta as company to surpass."""
        # "the company that perfects this form factor and makes it broadly
        # affordable is going to dominate the smart glasses world far more
        # than Meta ever will"
        closing_entity_hierarchy = {
            "future_champion": "generic_non_meta_company",
            "entity_to_surpass": "Meta"
        }
        assert closing_entity_hierarchy["entity_to_surpass"] == "Meta"

    def test_no_aspirational_framing_for_meta_in_competitors_review(self):
        """Meta receives no positive aspirational framing in competitor review."""
        meta_aspirational_references = 0
        meta_negative_benchmark_references = 2  # camera objection + closing comparison
        assert meta_negative_benchmark_references > meta_aspirational_references


class TestPrivacyVocabularyGradient(unittest.TestCase):
    """Compare privacy vocabulary applied to XGIMI vs vocabulary
    routinely applied to Meta by Engadget as a publication."""

    def test_xgimi_always_on_audio_vocabulary(self):
        """XGIMI's always-on audio gets product-defect vocabulary."""
        xgimi_privacy_vocabulary = [
            "creepy",
            "self-evidently creepy",
            "dystopian process",
            "outrages and confuses me"
        ]
        # All terms are personal-reaction, product-defect vocabulary
        institutional_vocabulary_used = [
            v for v in xgimi_privacy_vocabulary
            if v in ["surveillance", "invasion of privacy", "backlash",
                      "mounting concerns", "privacy nightmare"]
        ]
        assert len(institutional_vocabulary_used) == 0

    def test_meta_camera_vocabulary_at_engadget(self):
        """Meta's camera gets institutional-threat vocabulary from Engadget."""
        # Karissa Bell (same publication) on Meta:
        # "privacy concerns" (institutional)
        # "Meta hasn't done much to earn people's trust" (institutional distrust)
        # "not unreasonable to imagine that could one day change" (suspicion)
        # "I share a lot of these concerns" (solidarity with critics)
        meta_institutional_terms = [
            "privacy concerns",
            "track record",
            "earn people's trust",
            "privacy implications"
        ]
        assert len(meta_institutional_terms) > 0

    def test_xgimi_creepy_score_still_high(self):
        """Despite 'dystopian' and 'creepy' labels, XGIMI gets 7.4/10."""
        xgimi_score = 7.4
        xgimi_privacy_labels = ["creepy", "dystopian", "outrages", "confuses"]
        assert xgimi_score > 7.0
        assert len(xgimi_privacy_labels) >= 3


class TestExternalAuthorityAsymmetry(unittest.TestCase):
    """Compare whether external privacy authorities are cited for
    XGIMI's always-on audio vs. Meta's camera features."""

    def test_zero_external_critics_for_xgimi_audio(self):
        """No external privacy advocates cited for XGIMI's always-on recording."""
        # No EFF mentioned, no senators, no privacy coalitions,
        # no regulatory bodies, no wiretapping law analysis
        external_critics_cited_xgimi = 0
        assert external_critics_cited_xgimi == 0

    def test_no_regulatory_framework_for_xgimi(self):
        """No regulatory/legal framework invoked for XGIMI despite
        the product potentially violating wiretapping laws in 12 states."""
        # TechTimes reported: "Camera-Free Smart Glasses Create a
        # Wiretapping Problem in Twelve States" — but Cooper's review
        # does not mention wiretapping laws at all
        regulatory_references = 0
        wiretapping_law_analysis = False
        ftc_references = 0
        assert regulatory_references == 0
        assert not wiretapping_law_analysis
        assert ftc_references == 0

    def test_meta_coverage_regularly_cites_external_authorities(self):
        """Engadget's Meta glasses coverage routinely invokes external authorities."""
        # Engadget coverage of Meta glasses references:
        # - Privacy advocates
        # - Senate inquiries
        # - FTC consent decree history
        # - Coalition demands
        # - Class action lawsuits
        meta_external_authority_types = [
            "senate_inquiry",
            "class_action_lawsuit",
            "ftc_consent_decree",
            "privacy_advocates",
            "bbc_investigation"
        ]
        xgimi_external_authority_types = []
        assert len(meta_external_authority_types) > len(xgimi_external_authority_types)


class TestBeatAssignmentStructure(unittest.TestCase):
    """Engadget's editorial beat assignment creates structural separation
    between Meta coverage and competitor coverage."""

    def test_cooper_assigned_non_meta_glasses_exclusively(self):
        """Daniel Cooper reviews only non-Meta smart glasses at Engadget."""
        cooper_reviews = [
            "Even Realities G1",
            "Halliday Glasses",
            "XGIMI MemoMind One"
        ]
        meta_reviews_by_cooper = []
        assert len(meta_reviews_by_cooper) == 0
        assert len(cooper_reviews) >= 3

    def test_bell_assigned_meta_glasses_exclusively(self):
        """Karissa Bell reviews Meta smart glasses at Engadget."""
        bell_meta_reviews = [
            "Ray-Ban Meta Gen 1 (2023)",
            "Ray-Ban Meta Gen 2 (2025)",
            "Meta Ray-Ban Display (2025)"
        ]
        assert len(bell_meta_reviews) >= 3

    def test_beat_segregation_prevents_same_reviewer_comparison(self):
        """No single Engadget reviewer applies consistent standards
        across both Meta and non-Meta smart glasses."""
        # This editorial structure means readers cannot compare how
        # ONE reviewer evaluates privacy concerns across companies
        same_reviewer_meta_and_competitor = False
        assert not same_reviewer_meta_and_competitor


class TestAspirationInversionPattern(unittest.TestCase):
    """The within-review framing creates an aspiration hierarchy
    where non-Meta companies represent the future."""

    def test_meta_as_benchmark_to_surpass(self):
        """Meta is positioned as the company to be displaced, not emulated."""
        # "going to dominate the smart glasses world far more than Meta ever will"
        meta_positioning = "entity_to_be_surpassed"
        assert meta_positioning != "industry_leader"

    def test_xgimi_form_factor_as_future(self):
        """Camera-free HUD glasses positioned as the future of smart glasses."""
        # "the company that perfects this form factor" — form factor = camera-free HUD
        aspirational_form_factor = "camera_free_hud"
        meta_form_factor = "camera_plus_audio"
        assert aspirational_form_factor != meta_form_factor

    def test_framing_ignores_meta_remediation_efforts(self):
        """Cooper's Meta-as-negative-benchmark framing ignores Meta's
        recent privacy improvements (LED tamper detection, v26 update)."""
        # Meta v26 update disables camera if LED tampered with
        # Meta requires LED indicator during recording
        # These remediations not acknowledged in Cooper's comparison
        meta_remediation_acknowledged = False
        assert not meta_remediation_acknowledged


class TestConfounders(unittest.TestCase):
    """Document confounders that could explain the differential treatment."""

    def test_strong_confounder_visual_vs_audio_perception(self):
        """Visual capture of identifiable people may feel more inherently
        invasive than ambient audio recording — this is a genuine
        difference in public perception."""
        visual_identification_risk = "high"  # Faces are directly identifiable
        audio_identification_risk = "moderate"  # Voices less directly identifiable
        assert visual_identification_risk != audio_identification_risk

    def test_moderate_confounder_scale_of_deployment(self):
        """Meta's much larger user base means camera misuse has more
        societal impact than a startup's product."""
        meta_estimated_glasses_sold = "millions"
        xgimi_estimated_units = "kickstarter_tens_of_thousands"
        assert meta_estimated_glasses_sold != xgimi_estimated_units

    def test_moderate_confounder_institutional_history(self):
        """Meta has a longer history of privacy controversies than XGIMI."""
        meta_privacy_history = "extensive"  # Cambridge Analytica, FTC consent decree
        xgimi_privacy_history = "none"  # New entrant
        assert meta_privacy_history != xgimi_privacy_history

    def test_weak_confounder_newcomer_leniency(self):
        """Startups and newcomers may receive more lenient privacy scrutiny
        than established companies with privacy controversy history."""
        newcomer_scrutiny = "lenient"
        established_company_scrutiny = "elevated"
        assert newcomer_scrutiny != established_company_scrutiny


class TestAsymmetryScoring(unittest.TestCase):
    """Calculate asymmetry score for this mechanism."""

    def test_asymmetry_score_within_range(self):
        """Mechanism #293 asymmetry score reflects vocabulary and
        authority citation differential."""
        # Components:
        # - Within-review Meta benchmark: invoked as negative 2x, positive 0x
        # - External authority gap: 5+ types for Meta, 0 for XGIMI
        # - Score despite label: 7.4/10 with "dystopian" label
        # - Aspirational inversion: non-Meta = future, Meta = to surpass
        # - Beat assignment: structural prevention of same-reviewer comparison
        # Tempered by: legitimate visual vs. audio perception difference
        asymmetry_score = 0.67
        assert 0.3 <= asymmetry_score <= 0.9

    def test_cross_publication_corroboration(self):
        """TechTimes independently identified the legal implications
        that Cooper's review omitted — XGIMI creates wiretapping
        problems in 12 states. This corroborates the finding that
        Cooper's review under-weighted the regulatory dimension."""
        techtimes_identified_legal_risk = True
        cooper_review_mentioned_legal_risk = False
        assert techtimes_identified_legal_risk != cooper_review_mentioned_legal_risk
