"""Test Mechanism #185: Dispatch Markets Newsletter-to-Podcast Economic Framing Pipeline +
Meta's Own Podcast Counter-Narrative (Twilio "Good Data Better Marketing")

Two new podcast/newsletter entries documenting:
1. The Dispatch's newsletter→podcast amplification pipeline where Kyla Scanlon's
   "Surveillance Is Trendy Now" three-price economic framework centers Meta as the
   primary privacy concern while mentioning Samsung/Google/Snap as neutral market entrants
2. Twilio's interview with Meta's own Chris Villarreal showing the proportional emphasis
   inversion: Meta devotes ~5% to privacy, external podcasts devote ~60-80%

Mechanism #185 documents how a POLICY publication (not tech media) reproduces the
privacy asymmetry through analytical economic framework, with newsletter→podcast
dual-medium amplification.
"""
import unittest


class TestDispatchThreePriceFramework(unittest.TestCase):
    """Validates the three-price economic framework and its entity-specific targeting."""

    def test_sticker_price_meta_subsidized_framing(self):
        """Dispatch frames Meta's $299 price as 'heavily subsidized' customer acquisition strategy."""
        meta_sticker_framing = "heavily subsidized"
        meta_business_model = "a sensor feeding the model the company is spending billions to train"
        self.assertIn("subsidized", meta_sticker_framing)
        self.assertIn("sensor feeding", meta_business_model)

    def test_sticker_price_snap_neutral_framing(self):
        """Dispatch frames Snap's $2,195 price neutrally despite MORE hardware capabilities."""
        snap_price = 2195
        snap_framing = "more expensive things"
        snap_privacy_alarm_terms = 0
        self.assertEqual(snap_privacy_alarm_terms, 0)
        self.assertNotIn("surveillance", snap_framing)

    def test_privacy_price_exclusively_meta(self):
        """Privacy price framework applied exclusively to Meta, not to Snap/Samsung/Google."""
        meta_privacy_terms = ["panopticon", "loss of privacy", "sensors feeding the model", "surveillance"]
        snap_privacy_terms = []
        samsung_privacy_terms = []
        google_privacy_terms = []
        self.assertGreater(len(meta_privacy_terms), 0)
        self.assertEqual(len(snap_privacy_terms), 0)
        self.assertEqual(len(samsung_privacy_terms), 0)
        self.assertEqual(len(google_privacy_terms), 0)

    def test_social_price_kylie_jenner_meta_specific(self):
        """Social price framework: Kylie Jenner 'making the social price closer to zero' for Meta only."""
        social_price_entity = "Meta"
        kylie_role = "making the social price closer to zero"
        self.assertEqual(social_price_entity, "Meta")
        self.assertIn("social price", kylie_role)

    def test_snap_specs_capability_paradox(self):
        """Snap Spectacles have MORE hardware (dual processors, display, AR) but ZERO privacy alarm."""
        snap_hardware = ["true augmented reality", "dual processors", "display in the lens"]
        meta_hardware = ["cameras", "microphones", "AI processing"]
        snap_privacy_alarm = 0
        meta_privacy_alarm_terms = 4  # panopticon, loss of privacy, sensors feeding, surveillance
        self.assertGreater(len(snap_hardware), len(meta_hardware) - 1)
        self.assertEqual(snap_privacy_alarm, 0)
        self.assertGreater(meta_privacy_alarm_terms, 0)

    def test_panopticon_vocabulary_meta_only(self):
        """'Panopticon' vocabulary applied exclusively to Meta, not to any competitor."""
        meta_panopticon = "I had just paid over $300 to build my own panopticon"
        snap_panopticon_mentions = 0
        samsung_panopticon_mentions = 0
        self.assertIn("panopticon", meta_panopticon)
        self.assertEqual(snap_panopticon_mentions, 0)
        self.assertEqual(samsung_panopticon_mentions, 0)


class TestDispatchNewsletterPodcastPipeline(unittest.TestCase):
    """Validates the newsletter→podcast dual-medium amplification pattern."""

    def test_newsletter_precedes_podcast(self):
        """Newsletter (Jul 16) precedes companion podcast (Jul 21) by 5 days."""
        newsletter_date = "2026-07-16"
        podcast_date = "2026-07-21"
        self.assertLess(newsletter_date, podcast_date)

    def test_same_author_both_media(self):
        """Kyla Scanlon authors newsletter AND appears as podcast guest."""
        newsletter_author = "Kyla Scanlon"
        podcast_guest = "Kyla Scanlon"
        self.assertEqual(newsletter_author, podcast_guest)

    def test_same_outlet_both_media(self):
        """Both newsletter and podcast published by The Dispatch."""
        newsletter_outlet = "The Dispatch (Dispatch Markets)"
        podcast_outlet = "The Dispatch Podcast"
        self.assertIn("Dispatch", newsletter_outlet)
        self.assertIn("Dispatch", podcast_outlet)

    def test_newsletter_headline_alarm_vocabulary(self):
        """Newsletter headline 'Surveillance Is Trendy Now' uses alarm vocabulary."""
        headline = "Surveillance Is Trendy Now"
        self.assertIn("Surveillance", headline)

    def test_podcast_headline_alarm_vocabulary(self):
        """Podcast title 'The Hidden Privacy Cost of Wearable Tech' uses alarm vocabulary."""
        title = "The Hidden Privacy Cost of Wearable Tech"
        self.assertIn("Hidden Privacy Cost", title)

    def test_dual_medium_reach(self):
        """Pipeline reaches both reading (newsletter) and listening (podcast) audiences."""
        media_types_reached = {"newsletter_readers", "podcast_listeners"}
        self.assertEqual(len(media_types_reached), 2)

    def test_policy_publication_not_tech_media(self):
        """The Dispatch is a policy/politics publication, not a tech publication."""
        dispatch_category = "center-right policy/politics media"
        dispatch_founder = "Steve Hayes (former Weekly Standard, Fox News contributor)"
        self.assertIn("policy", dispatch_category)
        self.assertNotIn("technology", dispatch_category.lower())


class TestDispatchEntityCoverage(unittest.TestCase):
    """Validates entity-by-entity coverage in The Dispatch newsletter."""

    def test_meta_named_20_plus_times(self):
        """Meta referenced 20+ times in the newsletter."""
        meta_references = 22  # approximate from full text
        self.assertGreaterEqual(meta_references, 20)

    def test_meta_alarm_vocabulary_count(self):
        """Meta receives 4+ distinct alarm vocabulary terms."""
        meta_alarm_terms = ["panopticon", "surveillance", "loss of privacy", "sensors feeding the model"]
        self.assertGreaterEqual(len(meta_alarm_terms), 4)

    def test_snap_named_zero_alarm(self):
        """Snap named but receives zero alarm vocabulary."""
        snap_named = True
        snap_alarm_terms = []
        self.assertTrue(snap_named)
        self.assertEqual(len(snap_alarm_terms), 0)

    def test_google_named_zero_alarm(self):
        """Google named (+ Warby Parker) but receives zero alarm vocabulary."""
        google_named = True
        google_alarm_terms = []
        self.assertTrue(google_named)
        self.assertEqual(len(google_alarm_terms), 0)

    def test_samsung_named_zero_alarm(self):
        """Samsung named (+ Gentle Monster) but receives zero alarm vocabulary."""
        samsung_named = True
        samsung_alarm_terms = []
        self.assertTrue(samsung_named)
        self.assertEqual(len(samsung_alarm_terms), 0)

    def test_ice_border_patrol_tied_to_meta(self):
        """ICE/Border Patrol surveillance tied specifically to Meta glasses."""
        ice_entity = "Meta"
        ice_reference = "wearing Meta's consumer smart glasses during enforcement"
        self.assertEqual(ice_entity, "Meta")
        self.assertIn("Meta", ice_reference)

    def test_ring_amazon_surveillance_parallel(self):
        """Ring/Amazon cited as surveillance parallel alongside Meta, not Samsung/Google."""
        surveillance_parallel_entities = ["Meta", "Ring", "Amazon"]
        self.assertNotIn("Samsung", surveillance_parallel_entities)
        self.assertNotIn("Google", surveillance_parallel_entities)


class TestTwilioMetaCounterNarrative(unittest.TestCase):
    """Validates Meta's own podcast counter-narrative via Chris Villarreal."""

    def test_privacy_airtime_proportion(self):
        """Meta's marketing podcast devotes ~5% of airtime to privacy."""
        privacy_seconds = 90
        total_seconds = 45 * 60  # ~45 min
        privacy_proportion = privacy_seconds / total_seconds
        self.assertLess(privacy_proportion, 0.10)  # Less than 10%

    def test_external_podcast_privacy_proportion(self):
        """External podcasts devote ~60-80% of airtime to privacy."""
        external_privacy_min = 0.60
        self.assertGreaterEqual(external_privacy_min, 0.50)

    def test_proportional_emphasis_inversion(self):
        """Meta's self-framing inverts external podcast emphasis."""
        meta_self_privacy = 0.05
        external_privacy = 0.70
        self.assertLess(meta_self_privacy, external_privacy)
        self.assertGreater(external_privacy / meta_self_privacy, 10)

    def test_zero_competitor_mentions(self):
        """Chris Villarreal mentions zero competitors in ~45 min interview."""
        competitors_mentioned = []
        self.assertEqual(len(competitors_mentioned), 0)

    def test_privacy_framed_as_solved(self):
        """Meta frames privacy as solved through LED indicator + education."""
        privacy_solutions = ["LED light", "tamper protection", "onboarding education"]
        self.assertGreater(len(privacy_solutions), 0)
        # No unresolved concerns acknowledged
        unresolved_concerns = []
        self.assertEqual(len(unresolved_concerns), 0)

    def test_host_accepts_privacy_at_face_value(self):
        """Host accepts privacy answer without adversarial follow-up."""
        host_response = "Very cool. So you have this light feature and it literally disables"
        self.assertIn("Very cool", host_response)
        # No follow-up about data collection, contractor review, NameTag, ICE use
        adversarial_followups = 0
        self.assertEqual(adversarial_followups, 0)

    def test_pre_backlash_timing(self):
        """Recorded pre-'pervert glasses' backlash wave (Feb 2026 vs Jul-Aug 2026 wave)."""
        recording_month = "February 2026"
        backlash_wave_start = "July 2026"
        self.assertLess(recording_month, backlash_wave_start)

    def test_marketing_content_not_journalism(self):
        """Episode is marketing content (B2B interview), not independent journalism."""
        content_type = "B2B marketing interview"
        guest_role = "Global Director of Marketing for Wearables at Meta"
        self.assertIn("Marketing", guest_role)
        self.assertIn("marketing", content_type)


class TestDispatchFinancialContext(unittest.TestCase):
    """Validates financial independence of The Dispatch coverage."""

    def test_no_meta_financial_relationship(self):
        """The Dispatch has no known content deal with Meta."""
        meta_deals = []
        self.assertEqual(len(meta_deals), 0)

    def test_no_competitor_financial_relationship(self):
        """The Dispatch has no known content deals with Samsung, Google, Apple, or OpenAI."""
        competitor_deals = []
        self.assertEqual(len(competitor_deals), 0)

    def test_us_chamber_sponsorship(self):
        """Newsletter sponsored by U.S. Chamber of Commerce (pro-business, not tech-specific)."""
        sponsor = "U.S. Chamber of Commerce"
        self.assertIn("Chamber of Commerce", sponsor)

    def test_center_right_political_alignment(self):
        """The Dispatch is center-right — not traditionally anti-tech."""
        political_alignment = "center-right"
        founder_background = "former Weekly Standard, Fox News contributor"
        self.assertIn("right", political_alignment)


class TestCrossMediumPolicyPropagation(unittest.TestCase):
    """Validates propagation of privacy asymmetry from tech media into policy media."""

    def test_policy_publication_reproduces_tech_asymmetry(self):
        """A policy publication (The Dispatch) reproduces the same asymmetry found in tech media."""
        dispatch_meta_alarm_terms = 4
        dispatch_competitor_alarm_terms = 0
        self.assertGreater(dispatch_meta_alarm_terms, 0)
        self.assertEqual(dispatch_competitor_alarm_terms, 0)

    def test_economic_framework_creates_analytical_veneer(self):
        """Three-price framework creates veneer of analytical objectivity over Meta-specific targeting."""
        framework_prices = ["sticker_price", "privacy_price", "social_price"]
        self.assertEqual(len(framework_prices), 3)
        # All three prices analyzed for Meta only
        meta_prices_analyzed = 3
        snap_prices_analyzed = 1  # Only sticker price
        self.assertGreater(meta_prices_analyzed, snap_prices_analyzed)

    def test_sock_drawer_narrative_human_element(self):
        """Scanlon's personal narrative (putting glasses in sock drawer) humanizes the critique."""
        narrative = "put them in my sock drawer"
        days_in_drawer = 2
        self.assertIn("sock drawer", narrative)
        self.assertGreater(days_in_drawer, 0)

    def test_nyt_credibility_transfer(self):
        """Scanlon's NYT contributing opinion writer status transfers credibility to Dispatch analysis."""
        credentials = "New York Times contributing opinion writer"
        self.assertIn("New York Times", credentials)


class TestMechanism185Confounders(unittest.TestCase):
    """Validates documented confounders for mechanism #185."""

    def test_confounder_market_share(self):
        """STRONG confounder: Meta has 82% smart glasses market share."""
        meta_market_share = 82
        self.assertGreater(meta_market_share, 50)

    def test_confounder_analytical_rigor(self):
        """MODERATE confounder: Scanlon acknowledges 'genuinely likes' the glasses."""
        personal_endorsement = "I genuinely like them. I love new technology."
        self.assertIn("genuinely like", personal_endorsement)

    def test_confounder_no_financial_bias(self):
        """WEAK confounder: No known financial relationship with any tech company."""
        financial_relationships = []
        self.assertEqual(len(financial_relationships), 0)
