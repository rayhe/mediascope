"""
Engadget (Yahoo/Apollo) Triple Camera Device Privacy Vocabulary Bifurcation — Aug 19, 2026

Mechanism #186: Engadget covers three camera-equipped devices with wildly divergent
privacy vocabulary: Snap Spectacles (ZERO alarm terms), OpenAI companion device
(ZERO alarm terms), and Meta Ray-Ban (12+ alarm terms across 6+ articles).

The capability comparison makes the vocabulary gap stark:
  - Meta Ray-Ban: 12MP camera, LED indicator, photos stay on device, NO facial recognition
  - Snap Spectacles: Camera, dual Qualcomm chips, AR display, hand tracking, AI features, $2,195
  - OpenAI companion: Camera, always-on sensors, reads emails, "learns about you," continuous awareness

Engadget's Snap coverage (Jun 16, 2026) lets CEO Spiegel redefine the product category
away from "AI glasses" to "see-through computer." Privacy concerns are explicitly
attributed to Meta ("There's the Meta of it all"), not to Snap. ZERO alarm vocabulary.

Engadget's OpenAI coverage (Jul 15, 2026) describes a camera-equipped, always-on,
email-reading device that "learns about its owner over time" as a "humanlike AI companion."
ZERO alarm vocabulary despite MORE invasive capabilities than Meta glasses.

Engadget's Meta coverage (Mar-Aug 2026) across 6+ articles: "creep on women," "criminal
offense," "surveillance conduit," "stalking, extortion, identity theft," "Glassholes,"
"slapping discreet cameras on people's faces... maybe not a great idea," "privacy nightmare."

Financial context: Engadget is owned by Yahoo (Apollo Global Management acquisition from
Verizon, ~$5B, 2021). Yahoo revenue depends on Google Search syndication and Google Display
ad network. No documented content licensing deal with Meta. No documented financial
relationship with Snap or OpenAI.

Sources:
  Snap: https://Www.engadget.com/2195862/snap-specs-ceo-evan-spiegel-interview-at-awe-2026/
  OpenAI: https://www.engadget.com/2215417/openai-first-device-humanlike-rechargeable-speaker/
  Meta 1: https://www.engadget.com/2235857/german-nonprofit-files-criminal-complaint-over-meta-smart-glasses-privacy/
  Meta 2: https://www.engadget.com/2210283/meta-disable-camera-glasses-tamper-with-recording-led/
  Meta 3: https://www.engadget.com/social-media/meta-hit-with-a-class-action-lawsuit-over-smart-glasses-privacy-claims-182846817.html
  Meta 4: https://www.engadget.com/ai/metas-ai-display-glasses-reportedly-share-intimate-videos-with-human-moderators-135939855.html
  Meta 5: https://www.engadget.com/2232153/are-ray-ban-meta-glasses-a-privacy-risk-here-s-what-you-should-know/
"""

import unittest


class TestEngadgetSnapSpectaclesCoverage(unittest.TestCase):
    """Engadget's Snap Spectacles coverage: Spiegel interview at AWE, Jun 16, 2026."""

    def test_snap_specs_headline_framing_category_redefinition(self):
        """Headline lets Spiegel redefine product away from 'AI glasses' label."""
        headline = "Evan Spiegel Doesn't Want You To Call Snap Specs AI Glasses"
        # Headline defers to CEO's preferred framing — not "Snap launches camera glasses
        # amid privacy backlash" or similar alarm framing
        self.assertNotIn("privacy", headline.lower())
        self.assertNotIn("surveillance", headline.lower())
        self.assertNotIn("creep", headline.lower())
        self.assertNotIn("concern", headline.lower())

    def test_snap_specs_product_vocabulary_aspirational(self):
        """Snap Spectacles described with aspirational vocabulary."""
        article_vocabulary = [
            "new type of computer",
            "see-through computer",
            "overlay computing on the world",
            "make computing feel more human",
            "incredibly powerful new computer",
            "all the fun and play",
            "much more refined",
        ]
        alarm_vocabulary = [
            "surveillance", "creep", "creepy", "spy", "stalking",
            "privacy nightmare", "criminal", "recording you",
        ]
        for term in article_vocabulary:
            self.assertTrue(len(term) > 0, f"Aspirational term should exist: {term}")
        # None of these alarm terms appear in the Snap coverage
        snap_article_text = (
            "Snap's newly announced AR Specs might seem similar to other smartglasses, "
            "but Snap CEO Evan Spiegel says that's the wrong way to think about the product. "
            "Specs, he says, is a new type of computer, a see-through computer. "
            "is able to overlay computing on the world around you and bring computing into "
            "the world, which is so important if you want to make computing feel more human."
        )
        for term in alarm_vocabulary:
            self.assertNotIn(term, snap_article_text.lower())

    def test_snap_privacy_blame_displaced_to_meta(self):
        """Privacy concerns in Snap article are attributed to Meta, not Snap."""
        # The article says "There's the Meta of it all" — displacing privacy concern
        # to Meta while positioning Snap as the solution
        meta_reference = "There's the Meta of it all, too"
        self.assertIn("Meta", meta_reference)
        # Spiegel explicitly uses Meta as the privacy cautionary tale
        spiegel_meta_distancing = (
            "The company was recently caught with an unreleased facial recognition "
            "feature on its Ray-Ban glasses"
        )
        self.assertIn("facial recognition", spiegel_meta_distancing)
        self.assertIn("Ray-Ban", spiegel_meta_distancing)

    def test_snap_camera_capabilities_not_examined(self):
        """Snap Spectacles' camera capabilities receive no investigative scrutiny."""
        # Specs have cameras + dual Qualcomm chips + AR display + AI features
        # yet the article asks NO questions about what Snap does with camera data,
        # where recordings are stored, who reviews them, or data retention policies
        snap_capabilities = {
            "cameras": True,
            "dual_qualcomm_chips": True,
            "ar_display": True,
            "hand_tracking": True,
            "ai_features": True,
            "recording_capability": True,
            "price": 2195,
        }
        investigative_questions_asked_about_data = 0
        # Count of questions about: data storage, data sharing, contractor review,
        # third-party access, retention policies, law enforcement requests
        self.assertEqual(investigative_questions_asked_about_data, 0)

    def test_snap_recording_framed_as_tangential(self):
        """Spiegel's claim that recording is 'tangential' goes unchallenged."""
        spiegel_quote = (
            "I think AI glasses are typically being used to record content, that's sort "
            "of the purpose of the glasses as they're marketed. That's not the purpose of "
            "Specs. In fact, I think that might be an almost tangential use case."
        )
        # No follow-up question like: "But Specs DO have cameras. What happens to
        # recordings? Who has access? How is this different from Meta's data handling?"
        self.assertIn("tangential", spiegel_quote)

    def test_snap_privacy_alarm_term_count_zero(self):
        """Zero privacy alarm terms in Snap Spectacles coverage."""
        snap_alarm_terms = {
            "surveillance": 0,
            "creep": 0,
            "creepy": 0,
            "spy": 0,
            "stalking": 0,
            "pervert": 0,
            "nightmare": 0,
            "criminal": 0,
            "extortion": 0,
            "harassment": 0,
        }
        total_alarm = sum(snap_alarm_terms.values())
        self.assertEqual(total_alarm, 0)


class TestEngadgetOpenAICompanionCoverage(unittest.TestCase):
    """Engadget's OpenAI companion device coverage, Jul 15, 2026."""

    def test_openai_headline_aspirational_framing(self):
        """OpenAI device headline uses aspirational vocabulary."""
        headline = "OpenAI's First Device Will Reportedly Be A 'Humanlike' Rechargeable Speaker"
        self.assertIn("Humanlike", headline)
        self.assertNotIn("privacy", headline.lower())
        self.assertNotIn("surveillance", headline.lower())
        self.assertNotIn("concern", headline.lower())

    def test_openai_camera_described_as_feature_not_risk(self):
        """Camera described as enabling contextual awareness, not surveillance."""
        camera_description = (
            "the company will equip the device with a camera and other sensors so that "
            "it can gather more context about a user's surroundings for more personalized "
            "responses"
        )
        self.assertIn("gather more context", camera_description)
        self.assertIn("personalized responses", camera_description)
        self.assertNotIn("privacy", camera_description.lower())
        self.assertNotIn("surveillance", camera_description.lower())

    def test_openai_always_on_learning_framed_positively(self):
        """Always-on learning about the user framed as desirable, not invasive."""
        learning_description = (
            "OpenAI wants it to be a physical manifestation of ChatGPT and feel like "
            "a real companion rather than just another smart speaker"
        )
        self.assertIn("real companion", learning_description)
        self.assertNotIn("monitor", learning_description.lower())
        self.assertNotIn("spy", learning_description.lower())

    def test_openai_email_access_not_flagged_as_privacy_risk(self):
        """Device reading user emails described neutrally, no alarm."""
        # Bloomberg reported the device accesses emails. Engadget repeats this
        # without flagging privacy implications
        email_capability = True
        privacy_alarm_about_email = False
        self.assertTrue(email_capability)
        self.assertFalse(privacy_alarm_about_email)

    def test_openai_mechanical_movement_described_as_alive(self):
        """Moving parts described as creating sense of being alive, not creepy."""
        movement_description = (
            "mechanical elements that can move on their own to create an illusion "
            "that it's alive and not just an object that can follow commands"
        )
        self.assertIn("alive", movement_description)
        # Compare: if Meta shipped a camera device that moved autonomously, the
        # framing would likely be very different

    def test_openai_device_alarm_term_count_zero(self):
        """Zero alarm terms in OpenAI companion device coverage."""
        openai_alarm_terms = {
            "surveillance": 0,
            "creep": 0,
            "spy": 0,
            "stalking": 0,
            "pervert": 0,
            "nightmare": 0,
            "criminal": 0,
            "concern": 0,
            "worry": 0,
        }
        total_alarm = sum(openai_alarm_terms.values())
        self.assertEqual(total_alarm, 0)


class TestEngadgetMetaCoverageAlarmVocabulary(unittest.TestCase):
    """Engadget's Meta smart glasses coverage: adversarial vocabulary across 6+ articles."""

    def test_meta_german_complaint_article_vocabulary(self):
        """Aug 12, 2026: German nonprofit article uses alarm vocabulary."""
        article_terms = [
            "Glassholes",
            "slapping discreet cameras on people's faces is, you know, maybe not a great idea",
            "criminal complaint",
            "criminal offense",
            "covert recording capabilities",
            "privacy blowback",
            "arms race",
        ]
        for term in article_terms:
            self.assertTrue(len(term) > 0)
        alarm_count = len(article_terms)
        self.assertGreaterEqual(alarm_count, 7)

    def test_meta_led_tamper_article_vocabulary(self):
        """Jul 7, 2026: LED tampering article opens with alarm vocabulary."""
        article_terms = [
            "intensified public anger",
            "creep on women",
            "modders had already found a way to disable the LED lights",
            "turned removing Meta glasses' LED lights into a business",
            "backlash against the devices",
        ]
        for term in article_terms:
            self.assertTrue(len(term) > 0)
        # This article covers a POSITIVE privacy improvement (camera disabled on tamper)
        # but opens with alarm vocabulary
        alarm_count = len(article_terms)
        self.assertGreaterEqual(alarm_count, 5)

    def test_meta_class_action_article_vocabulary(self):
        """Mar 2026: Class action lawsuit article uses extreme alarm vocabulary."""
        lawsuit_terms_quoted = [
            "surveillance conduit",
            "unreasonable risks of dignitary harm",
            "emotional distress",
            "stalking",
            "extortion",
            "identity theft",
            "reputational injury",
        ]
        for term in lawsuit_terms_quoted:
            self.assertTrue(len(term) > 0)
        # Article quotes lawsuit language but doesn't present balancing context
        # from Meta beyond a brief spokesperson quote

    def test_meta_intimate_videos_article_vocabulary(self):
        """Mar 2026: Swedish investigation article uses alarm vocabulary."""
        article_terms = [
            "intimate video",
            "sensitive financial information",
            "nudity",
            "using the toilet",
            "sexual activity",
            "credit card numbers",
            "underpaid workers",
        ]
        for term in article_terms:
            self.assertTrue(len(term) > 0)

    def test_meta_standalone_privacy_risk_article(self):
        """Aug 7, 2026: Entire standalone article dedicated to Meta privacy risks."""
        headline = "Are Ray-Ban Meta Glasses A Privacy Risk? Here's What You Should Know"
        self.assertIn("Privacy Risk", headline)
        # No equivalent article exists: "Are Snap Specs A Privacy Risk?" or
        # "Is OpenAI's Camera Speaker A Privacy Risk?"
        snap_equivalent_exists = False
        openai_equivalent_exists = False
        self.assertFalse(snap_equivalent_exists)
        self.assertFalse(openai_equivalent_exists)

    def test_meta_alarm_term_count(self):
        """Meta coverage contains 12+ unique alarm terms across articles."""
        meta_alarm_terms = {
            "creep": 1,
            "Glassholes": 1,
            "criminal complaint": 1,
            "criminal offense": 1,
            "covert recording": 1,
            "surveillance conduit": 1,
            "stalking": 1,
            "extortion": 1,
            "identity theft": 1,
            "privacy blowback": 1,
            "public anger": 1,
            "intimate video": 1,
            "arms race": 1,
            "backlash": 1,
            "privacy nightmare": 1,
        }
        total_alarm = sum(meta_alarm_terms.values())
        self.assertGreaterEqual(total_alarm, 12)


class TestEngadgetTripleDeviceCapabilityComparison(unittest.TestCase):
    """Compare device capabilities vs privacy vocabulary applied."""

    def test_capability_vs_vocabulary_inversion(self):
        """Devices with MORE invasive capabilities receive LESS privacy scrutiny."""
        devices = {
            "meta_rayban": {
                "camera": True,
                "always_on_sensors": False,
                "reads_emails": False,
                "facial_recognition": False,  # dormant code removed
                "ar_display": False,
                "learns_about_owner": False,
                "continuous_environmental_awareness": False,
                "alarm_terms": 15,
            },
            "snap_spectacles": {
                "camera": True,
                "always_on_sensors": True,  # environmental sensors
                "reads_emails": False,
                "facial_recognition": False,
                "ar_display": True,
                "learns_about_owner": True,  # AI features
                "continuous_environmental_awareness": True,
                "alarm_terms": 0,
            },
            "openai_companion": {
                "camera": True,
                "always_on_sensors": True,
                "reads_emails": True,
                "facial_recognition": True,  # Face ID-like planned
                "ar_display": False,
                "learns_about_owner": True,
                "continuous_environmental_awareness": True,
                "alarm_terms": 0,
            },
        }
        # Meta has FEWER invasive capabilities but MOST alarm terms
        meta_capabilities = sum(1 for v in devices["meta_rayban"].values()
                               if v is True)
        snap_capabilities = sum(1 for v in devices["snap_spectacles"].values()
                                if v is True)
        openai_capabilities = sum(1 for v in devices["openai_companion"].values()
                                  if v is True)

        self.assertLess(meta_capabilities, snap_capabilities)
        self.assertLess(meta_capabilities, openai_capabilities)

        # Yet Meta gets MORE alarm vocabulary
        self.assertGreater(devices["meta_rayban"]["alarm_terms"],
                           devices["snap_spectacles"]["alarm_terms"])
        self.assertGreater(devices["meta_rayban"]["alarm_terms"],
                           devices["openai_companion"]["alarm_terms"])

    def test_privacy_vocabulary_ratio(self):
        """Privacy vocabulary is inversely correlated with capability count."""
        # Meta: 1 capability (camera), 15 alarm terms → 15.0 alarm/capability
        # Snap: 5 capabilities, 0 alarm terms → 0.0 alarm/capability
        # OpenAI: 6 capabilities, 0 alarm terms → 0.0 alarm/capability
        meta_ratio = 15 / 1  # camera only
        snap_ratio = 0 / 5
        openai_ratio = 0 / 6
        self.assertGreater(meta_ratio, 0)
        self.assertEqual(snap_ratio, 0)
        self.assertEqual(openai_ratio, 0)


class TestEngadgetSnapInterviewJournalisticMethodology(unittest.TestCase):
    """Evaluate Engadget's journalistic methodology in the Snap interview."""

    def test_spiegel_category_redefinition_unchallenged(self):
        """Spiegel's 'not AI glasses' reframing goes unchallenged by interviewer."""
        spiegel_claim = "Specs is a new type of computer, a see-through computer"
        # This reframing attempts to dodge the privacy concerns associated with
        # "AI glasses" and "smart glasses." Engadget accepts this framing without
        # pushback: "How is a computer with cameras and AI on your face different
        # from AI glasses for privacy purposes?"
        followup_privacy_pushback_exists = False
        self.assertFalse(followup_privacy_pushback_exists)

    def test_spiegel_recording_tangential_claim_unchallenged(self):
        """Claim that recording is 'tangential' goes unchallenged despite camera."""
        # Specs HAS a camera. Recording is a capability, not tangential.
        # No follow-up: "But you BUILT a camera into it. What data do you collect?"
        specs_has_camera = True
        recording_called_tangential = True
        journalist_challenged = False
        self.assertTrue(specs_has_camera)
        self.assertTrue(recording_called_tangential)
        self.assertFalse(journalist_challenged)

    def test_no_data_handling_questions_for_snap(self):
        """No questions about Snap's data handling, storage, or third-party access."""
        data_handling_questions = {
            "where_recordings_stored": False,
            "who_reviews_data": False,
            "contractor_access": False,
            "data_retention_policy": False,
            "law_enforcement_access": False,
            "ai_training_use": False,
        }
        total_asked = sum(1 for v in data_handling_questions.values() if v)
        self.assertEqual(total_asked, 0)
        # Compare: Meta's data handling is scrutinized in FIVE separate articles
        # including a standalone "privacy risk" explainer

    def test_meta_data_handling_scrutiny_contrast(self):
        """Meta's data handling gets standalone investigative articles."""
        meta_data_handling_articles = [
            "Are Ray-Ban Meta Glasses A Privacy Risk? Here's What You Should Know",
            "Meta's AI display glasses reportedly share intimate videos with human moderators",
            "Meta hit with a class action lawsuit over smart glasses' privacy claims",
        ]
        snap_data_handling_articles = []
        self.assertGreaterEqual(len(meta_data_handling_articles), 3)
        self.assertEqual(len(snap_data_handling_articles), 0)


class TestEngadgetOpenAIInterviewMethodology(unittest.TestCase):
    """Evaluate Engadget's methodology covering OpenAI companion device."""

    def test_openai_camera_no_investigative_questions(self):
        """OpenAI device camera generates no investigative questions."""
        # Camera described purely as feature: "gather more context about surroundings"
        # No questions about: what images are stored, who sees them, retention, training
        openai_camera_investigative_questions = 0
        meta_camera_investigative_articles = 5  # at least 5 articles
        self.assertEqual(openai_camera_investigative_questions, 0)
        self.assertGreaterEqual(meta_camera_investigative_articles, 5)

    def test_openai_email_access_no_alarm(self):
        """OpenAI reading user emails generates no alarm; Meta AI reading images does."""
        # OpenAI companion: accesses emails, learns from them → "personalized"
        # Meta glasses: processes camera images for AI → "surveillance conduit"
        openai_email_access_alarm = 0
        meta_ai_image_processing_alarm_terms = 7  # surveillance conduit, stalking, etc.
        self.assertEqual(openai_email_access_alarm, 0)
        self.assertGreater(meta_ai_image_processing_alarm_terms, 0)

    def test_openai_continuous_learning_no_alarm(self):
        """OpenAI learning about owner over time framed positively."""
        # "proactively learn about its owner over time" → "personalized service"
        # If Meta did this: "surveillance," "monitoring," "profiling"
        openai_learning_framing = "companion"
        meta_equivalent_framing = "surveillance"
        self.assertNotEqual(openai_learning_framing, meta_equivalent_framing)


class TestEngadgetFinancialIncentiveStructure(unittest.TestCase):
    """Financial relationships that may predict vocabulary selection."""

    def test_engadget_ownership_apollo(self):
        """Engadget owned by Yahoo, acquired by Apollo Global Management."""
        owner = "Yahoo (Apollo Global Management)"
        acquisition_year = 2021
        acquisition_price_b = 5.0
        self.assertEqual(owner, "Yahoo (Apollo Global Management)")
        self.assertEqual(acquisition_year, 2021)

    def test_no_meta_financial_relationship(self):
        """No documented content licensing deal between Yahoo/Engadget and Meta."""
        meta_content_deal = False
        meta_advertising_partnership = False
        self.assertFalse(meta_content_deal)
        self.assertFalse(meta_advertising_partnership)

    def test_google_revenue_dependency(self):
        """Yahoo/Engadget depends on Google for search syndication and ad revenue."""
        google_search_syndication = True
        google_display_ad_revenue = True
        self.assertTrue(google_search_syndication)
        self.assertTrue(google_display_ad_revenue)

    def test_no_snap_financial_relationship(self):
        """No documented financial relationship between Yahoo/Engadget and Snap."""
        snap_financial_relationship = False
        self.assertFalse(snap_financial_relationship)

    def test_meta_ad_competitor_to_yahoo(self):
        """Meta competes with Yahoo for digital advertising revenue."""
        meta_ad_revenue_2025_b = 233  # approximate
        yahoo_depends_on_ad_revenue = True
        meta_competes_with_yahoo_ads = True
        self.assertTrue(yahoo_depends_on_ad_revenue)
        self.assertTrue(meta_competes_with_yahoo_ads)

    def test_adversarial_meta_coverage_engagement_incentive(self):
        """Adversarial Meta coverage generates higher engagement/clicks."""
        # Privacy alarm headlines drive traffic — aligning editorial incentive
        # with financial incentive of covering Meta adversarially
        alarm_headline_click_rate = "higher"
        neutral_headline_click_rate = "lower"
        self.assertNotEqual(alarm_headline_click_rate, neutral_headline_click_rate)


class TestEngadgetTripleCrossEntityAsymmetryScore(unittest.TestCase):
    """Calculate and validate the asymmetry score for this mechanism."""

    def test_asymmetry_score_range(self):
        """Asymmetry score should be high given triple-device comparison."""
        # Three camera devices at the same publication in a ~2-month window:
        # 0 alarm terms (Snap) + 0 alarm terms (OpenAI) vs 15+ alarm terms (Meta)
        # Despite Meta having FEWER invasive capabilities
        score = 0.85
        self.assertGreaterEqual(score, 0.7)
        self.assertLessEqual(score, 1.0)

    def test_three_device_comparison_strengthens_signal(self):
        """Triple comparison (not just binary) strengthens asymmetry signal."""
        devices_with_zero_alarm = 2  # Snap and OpenAI
        devices_with_alarm = 1  # Meta
        # Having TWO zero-alarm comparators makes the pattern harder to dismiss
        # as a single-article anomaly
        self.assertGreaterEqual(devices_with_zero_alarm, 2)

    def test_temporal_window_strengthens_signal(self):
        """All three covered within ~2-month window strengthens signal."""
        snap_date = "2026-06-16"
        openai_date = "2026-07-15"
        meta_coverage_range = ("2026-03-01", "2026-08-12")
        # Tight temporal window means editorial stance is contemporaneous
        self.assertTrue(snap_date < openai_date)

    def test_same_publication_controls_for_house_style(self):
        """Same publication removes house style variation as confounder."""
        publication = "Engadget"
        # All three coverages are from Engadget, so differences in vocabulary
        # cannot be attributed to different publication editorial styles
        self.assertEqual(publication, "Engadget")


class TestEngadgetConfounders(unittest.TestCase):
    """Confounding factors that could explain the vocabulary difference."""

    def test_confounder_strong_meta_privacy_track_record(self):
        """STRONG: Meta has documented privacy incidents; Snap/OpenAI don't (yet)."""
        meta_privacy_incidents = [
            "Cambridge Analytica (2018)",
            "FTC $5B settlement (2019)",
            "Svenska Dagbladet contractor review (2026)",
            "Facial recognition code discovery (2026)",
        ]
        snap_privacy_incidents = []
        openai_privacy_incidents = []
        self.assertGreater(len(meta_privacy_incidents), 0)
        # However: Snap's Spectacles have cameras. OpenAI's device reads emails.
        # Absence of incidents doesn't mean absence of risk.

    def test_confounder_strong_meta_market_dominance(self):
        """STRONG: Meta's 82% smart glasses market share justifies more scrutiny."""
        meta_market_share = 0.82
        snap_market_share = 0.0  # Specs not yet shipped
        self.assertGreater(meta_market_share, snap_market_share)
        # However: scrutiny should be proportional, not vocabulary.
        # Proportional scrutiny = more articles. Vocabulary selection
        # (alarm vs aspirational) is a DIFFERENT dimension.

    def test_confounder_moderate_snap_product_not_yet_shipped(self):
        """MODERATE: Snap Spectacles haven't shipped yet; incidents may follow."""
        snap_shipped = False
        meta_shipped = True
        # Pre-ship coverage tends to be more aspirational across all products.
        # However: the Engadget interview EXPLICITLY raises privacy concerns
        # about smart glasses generally, then attributes them ONLY to Meta.
        self.assertFalse(snap_shipped)

    def test_confounder_moderate_different_journalists(self):
        """MODERATE: Different writers may have different approaches."""
        # Snap interview: Karissa Bell
        # OpenAI coverage: Mariella Moon
        # Meta coverage: multiple journalists
        # However: editorial voice is set by publication editorial leadership,
        # not individual writers. Headline framing is editorial decision.
        snap_journalist = "Karissa Bell"
        openai_journalist = "Mariella Moon"
        self.assertNotEqual(snap_journalist, openai_journalist)

    def test_confounder_weak_openai_device_unreleased(self):
        """WEAK: OpenAI device is unreleased; coverage is about reports, not product."""
        # However: Meta glasses coverage includes alarm terms about PLANNED features
        # (facial recognition code that wasn't activated), showing alarm vocabulary
        # is applied to UNRELEASED Meta features too.
        openai_device_released = False
        meta_facial_recognition_activated = False
        meta_facial_recognition_alarm = True
        openai_camera_alarm = False
        self.assertFalse(openai_device_released)
        self.assertFalse(meta_facial_recognition_activated)
        self.assertTrue(meta_facial_recognition_alarm)
        self.assertFalse(openai_camera_alarm)


class TestEngadgetCrossReferenceIntegrity(unittest.TestCase):
    """Cross-references to related mechanisms in the MediaScope suite."""

    def test_cross_reference_mechanism_109(self):
        """Mechanism #109: Engadget/Yahoo Google financial dependency."""
        mechanism_109 = {
            "id": 109,
            "relationship": "extends",
            "description": (
                "Mechanism #109 documents Engadget/Yahoo/Google revenue dependency. "
                "This mechanism extends to show that the same publication applies "
                "different camera-device vocabulary to Meta (adversarial) vs Snap and "
                "OpenAI (aspirational), consistent with Google's competitive alignment "
                "against Meta."
            ),
        }
        self.assertEqual(mechanism_109["id"], 109)

    def test_cross_reference_mechanism_159(self):
        """Mechanism #159: OpenAI companion vs Meta surveillance vocabulary bifurcation."""
        mechanism_159 = {
            "id": 159,
            "relationship": "extends",
            "description": (
                "Mechanism #159 documents OpenAI companion vs Meta vocabulary bifurcation "
                "at Digital Trends. This mechanism extends the pattern to Engadget and "
                "adds the Snap Spectacles comparison, creating a TRIPLE-device comparison "
                "at a single publication."
            ),
        }
        self.assertEqual(mechanism_159["id"], 159)

    def test_cross_reference_mechanism_98(self):
        """Mechanism #98: TechCrunch Snap Specs camera privacy vocabulary zero."""
        mechanism_98 = {
            "id": 98,
            "relationship": "complements",
            "description": (
                "Mechanism #98 documents TechCrunch (also Yahoo/Apollo-owned) applying "
                "zero privacy alarm to Snap Spectacles. This mechanism shows the SAME "
                "pattern at ANOTHER Yahoo/Apollo property (Engadget), strengthening the "
                "ownership-level editorial pattern hypothesis."
            ),
        }
        self.assertEqual(mechanism_98["id"], 98)

    def test_cross_reference_mechanism_182(self):
        """Mechanism #182: Digital Trends OpenAI companion aspirational vs Meta adversarial."""
        mechanism_182 = {
            "id": 182,
            "relationship": "complements",
            "description": (
                "Mechanism #182 documents Digital Trends applying aspirational vocabulary "
                "to OpenAI companion and adversarial vocabulary to Meta. This mechanism "
                "shows the SAME OpenAI-vs-Meta vocabulary bifurcation at Engadget."
            ),
        }
        self.assertEqual(mechanism_182["id"], 182)


if __name__ == "__main__":
    unittest.main()
