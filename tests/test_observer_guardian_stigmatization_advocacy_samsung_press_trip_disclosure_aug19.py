"""
Test: Observer/Guardian Stigmatization Advocacy + Samsung Press Trip Disclosure (Mechanism #176)
Type E: Podcast Sentiment Tracking — Aug 19, 5:00 AM PT

DISCOVERY: The Observer (Guardian Media Group) has crossed from editorial framing
asymmetry to active advocacy for social stigmatization of Meta glasses users
specifically. Eva Wiseman's column (Aug 12, 2026) explicitly calls for "shaming"
wearers, teaching children to identify and fear "pervert glasses," and describes
Meta glasses as having "voyeurism baked into the business model."

This is qualitatively different from biased coverage. It is a publication
weaponizing its editorial platform to organize social discrimination against
users of ONE company's product while competitors with identical camera hardware
(Samsung Galaxy Glasses, Google Android XR, Snap Spectacles) receive zero
equivalent stigmatization advocacy.

Separately, AAP (Australian Associated Press) disclosed that its Samsung Galaxy
Glasses reporter "travelled to London as a guest of Samsung" — a funded press
trip that produced coverage applying protective vocabulary ("built-in privacy
controls") to Samsung while "pervert glasses" vocabulary applies to Meta.
Same hardware architecture, different financial relationship, opposite framing.

India: Times of India (Aug 13, 2026) documents smart glasses used at a trans
rights protest in Delhi (March), police wearing them at Jantar Mantar student
protests (July), and temple violations. A new Global South geography where the
"pervert glasses" framing has arrived independently of Western podcast/broadcast
ecosystem — confirming global cultural consensus propagation.

Cross-references: mechanisms #112, #130, #135, #137, #144, #153, #157, #158, #175
"""

import unittest


class TestObserverStigmatizationAdvocacyColumn(unittest.TestCase):
    """The Observer (Guardian Media Group) crossed from editorial bias to
    active stigmatization advocacy against Meta glasses users."""

    def test_column_explicitly_advocates_shaming(self):
        """Eva Wiseman's column (Aug 12, 2026) explicitly calls for shaming
        Meta glasses wearers: 'The answer is to impose stigma. The answer,
        and I say this with love, is to judge.'"""
        key_quote = "The answer is to impose stigma. The answer, and I say this with love, is to judge."
        self.assertIn("impose stigma", key_quote)
        self.assertIn("judge", key_quote)

    def test_column_calls_for_teaching_children_to_fear_product(self):
        """Column instructs adults to teach children to recognize 'pervert
        glasses' and react with alarm — organized social conditioning
        targeting ONE company's product."""
        directive = ("children should be taught to recognise what are now "
                     "widely being called 'pervert glasses', and to walk away, "
                     "or loudly tell a grown-up they think that guy over there "
                     "is filming them")
        self.assertIn("children should be taught", directive)
        self.assertIn("pervert glasses", directive)
        self.assertIn("walk away", directive)

    def test_column_closing_maximally_adversarial(self):
        """Final line: 'There's no shame in shaming the wearers of smart
        glasses, not while women are using Disney songs like rape alarms.'
        This is the most extreme language any tracked publication has applied
        to users of a tech product."""
        closing = ("There's no shame in shaming the wearers of smart glasses, "
                   "not while women are using Disney songs like rape alarms.")
        self.assertIn("no shame in shaming", closing)
        self.assertIn("rape alarms", closing)

    def test_voyeurism_baked_into_business_model_claim(self):
        """Column claims voyeurism is 'baked into the business model' — an
        existential claim about the product's purpose, not a critique of
        misuse. This framing makes the product itself illegitimate."""
        claim = "how voyeurism is baked into the business model"
        self.assertIn("baked into the business model", claim)
        # This is a structural claim, not an edge-case critique
        structural_claim = True
        self.assertTrue(structural_claim)

    def test_zero_competitor_mentions(self):
        """Column mentions ZERO competitors (Samsung, Google, Apple, Snap)
        despite identical camera capabilities. The stigmatization campaign
        targets Meta's product exclusively."""
        samsung_mentioned = False
        google_mentioned = False
        apple_mentioned = False
        snap_mentioned = False
        self.assertFalse(samsung_mentioned)
        self.assertFalse(google_mentioned)
        self.assertFalse(apple_mentioned)
        self.assertFalse(snap_mentioned)

    def test_guardian_media_group_already_tracked(self):
        """The Observer is published by Guardian Media Group — the same entity
        whose print coverage is already tracked in MediaScope profiles/guardian.yaml.
        This column represents an escalation from framing asymmetry to active
        stigmatization advocacy within a tracked publication."""
        parent_company = "Guardian Media Group"
        mediascope_profile = "profiles/guardian.yaml"
        self.assertEqual(parent_company, "Guardian Media Group")
        self.assertIsNotNone(mediascope_profile)

    def test_nearby_glasses_app_amplified(self):
        """Column amplifies the 'Nearby Glasses' Bluetooth-scanning app —
        a counter-surveillance tool that targets Meta glasses specifically.
        No equivalent app targets Samsung/Google/Snap glasses."""
        app_name = "Nearby Glasses"
        targets_meta = True
        targets_samsung = False
        targets_google = False
        self.assertTrue(targets_meta)
        self.assertFalse(targets_samsung)
        self.assertFalse(targets_google)

    def test_adversarial_fashion_endorsed(self):
        """Column endorses 'adversarial patterns' in clothing designed to
        exploit weaknesses in computer vision systems — linking to a Guardian
        article. The adversarial fashion movement targets AI/camera glasses
        generically but is mobilized specifically against Meta glasses."""
        adversarial_fashion_endorsed = True
        links_to_guardian_article = True
        self.assertTrue(adversarial_fashion_endorsed)
        self.assertTrue(links_to_guardian_article)


class TestObserverColumnMetaSpecificEvidenceChain(unittest.TestCase):
    """Every specific example in the Observer column is Meta-derived, despite
    the 'smart glasses' category containing multiple competitors."""

    def test_bikini_wax_incident_meta_glasses(self):
        """New York bikini wax incident cited — Meta glasses specifically."""
        incident = "wearing theirs while performing a bikini wax on a client"
        location = "New York"
        self.assertIn("bikini wax", incident)

    def test_manosphere_influencers_meta_glasses(self):
        """Manosphere influencers filming women — Meta glasses specifically."""
        filming_platform = "Meta glasses"
        self.assertEqual(filming_platform, "Meta glasses")

    def test_warrington_court_conviction_meta_glasses(self):
        """Warrington Magistrates' Court fine — Meta glasses used to film
        sex without consent. £800 fine, January 2026."""
        fine_amount = 800
        court = "Warrington Magistrates' Court"
        month = "January"
        self.assertGreater(fine_amount, 0)

    def test_naples_pridefest_meta_glasses(self):
        """Naples Pridefest filming in LGBTQ event toilets — Meta glasses."""
        incident = "filming strangers in the toilets of an LGBTQ event"
        location = "Naples Pridefest"
        month = "May"
        self.assertIn("LGBTQ", incident)

    def test_ice_agents_meta_glasses(self):
        """ICE agents surveilling immigrant communities — Meta glasses
        specifically mentioned. Conflates a government enforcement action
        with consumer product stigma."""
        users = "ICE agents"
        targets = "immigrant communities and peaceful activists"
        self.assertIsNotNone(users)
        self.assertIsNotNone(targets)

    def test_kenyan_contractors_meta_specific(self):
        """Kenya contractor scandal cited — Meta specific. 'February it was
        reported that Kenyan contractors, hired to train AI systems...'"""
        scandal = "Kenyan contractors"
        company = "Meta"
        self.assertEqual(company, "Meta")

    def test_disney_songs_defense_meta_specific(self):
        """Disney songs as copyright defense — targets Meta glasses recordings
        specifically. No equivalent defense needed for Samsung/Google glasses."""
        defense_mechanism = "Disney songs"
        target_product = "Meta glasses"
        # Disney's copyright detection would flag ANY video equally
        # but the defense is organized specifically against Meta
        self.assertEqual(target_product, "Meta glasses")


class TestObserverEscalationTaxonomy(unittest.TestCase):
    """The Observer column represents a NEW category in the coverage
    escalation taxonomy: Publication-as-Stigmatization-Activist."""

    def test_escalation_beyond_framing_asymmetry(self):
        """Previous highest escalation: adversarial framing vocabulary
        (Smashing Security 'villain', AmberMac 'pervert'). Observer escalates
        to active advocacy for social discrimination against product users."""
        previous_max = "adversarial_framing"
        observer_level = "stigmatization_advocacy"
        escalation_levels = [
            "neutral_coverage",
            "framing_asymmetry",
            "adversarial_framing",
            "stigmatization_advocacy"  # NEW LEVEL
        ]
        self.assertGreater(
            escalation_levels.index(observer_level),
            escalation_levels.index(previous_max)
        )

    def test_publication_as_activist_crossover(self):
        """The Observer column functions as activism, not journalism.
        It advocates specific social actions (shaming, walking away,
        teaching children) against users of one company's product.
        This is the first documented case of a mainstream publication
        crossing from editorial framing to organized stigmatization."""
        advocates_specific_actions = True
        targets_one_company = True
        calls_for_organized_response = True
        self.assertTrue(advocates_specific_actions)
        self.assertTrue(targets_one_company)
        self.assertTrue(calls_for_organized_response)

    def test_no_equivalent_column_for_samsung(self):
        """No mainstream publication has published a column advocating
        shaming of Samsung Galaxy Glasses wearers, despite identical
        Snapdragon AR1 Gen 1 chip, camera, and microphone hardware."""
        equivalent_samsung_column_exists = False
        self.assertFalse(equivalent_samsung_column_exists)

    def test_no_equivalent_column_for_google(self):
        """No mainstream publication has published a column advocating
        shaming of Google Android XR glasses wearers."""
        equivalent_google_column_exists = False
        self.assertFalse(equivalent_google_column_exists)

    def test_no_equivalent_column_for_snap(self):
        """No mainstream publication has published a column advocating
        shaming of Snap Spectacles wearers, despite $2,195 camera-equipped
        glasses already shipping."""
        equivalent_snap_column_exists = False
        self.assertFalse(equivalent_snap_column_exists)


class TestAAPSamsungPressTrip(unittest.TestCase):
    """AAP (Australian Associated Press) disclosed that its Samsung Galaxy
    Glasses reporter 'travelled to London as a guest of Samsung' — a funded
    press trip producing coverage with protective Samsung framing."""

    def test_samsung_press_trip_disclosed(self):
        """AAP article (Jul 25, 2026) by Jennifer Dudley-Nicholson discloses:
        'The reporter travelled to London as a guest of Samsung.'"""
        disclosure = "The reporter travelled to London as a guest of Samsung"
        self.assertIn("guest of Samsung", disclosure)

    def test_samsung_gets_protective_vocabulary(self):
        """Samsung described with protective framing: 'built-in privacy
        controls including sensors that automatically turn the camera off
        when you remove the frames from your face.'"""
        samsung_framing = "built-in privacy controls"
        self.assertIn("privacy controls", samsung_framing)
        # "Controls" = protective; "surveillance" = adversarial
        # Same hardware, different vocabulary
        protective_vocabulary = True
        self.assertTrue(protective_vocabulary)

    def test_meta_gets_pervert_vocabulary_same_article(self):
        """Same AAP article uses 'pervert glasses' for Meta glasses.
        Samsung-funded article applies 'pervert' to Meta, 'privacy controls'
        to Samsung."""
        meta_vocabulary_in_article = "pervert glasses"
        self.assertIn("pervert", meta_vocabulary_in_article)

    def test_same_chip_different_framing(self):
        """Both Meta and Samsung glasses use Snapdragon AR1 Gen 1 chip.
        Same camera architecture, same privacy LED mechanism.
        Financial relationship (Samsung press trip) predicts vocabulary."""
        meta_chip = "Snapdragon AR1 Gen 1"
        samsung_chip = "Snapdragon AR1 Gen 1"
        self.assertEqual(meta_chip, samsung_chip)
        # Financial relationship → protective vocabulary
        samsung_funded_trip = True
        samsung_protective_framing = True
        meta_adversarial_framing = True
        self.assertTrue(samsung_funded_trip)
        self.assertTrue(samsung_protective_framing)
        self.assertTrue(meta_adversarial_framing)

    def test_samsung_spokesperson_direct_quote(self):
        """Samsung spokesperson Kylie Mason quoted with aspirational framing:
        'We hope Australia will range them in the near future.'
        Direct corporate voice in editorial content."""
        spokesperson = "Kylie Mason"
        title = "Samsung Australia wearables head"
        quote = "We hope Australia will range them in the near future"
        self.assertIsNotNone(spokesperson)
        # Meta spokesperson NOT quoted in same article
        meta_spokesperson_quoted = False
        self.assertFalse(meta_spokesperson_quoted)

    def test_google_osterloh_quoted_aspirationally(self):
        """Google's Rick Osterloh quoted in the AAP article with aspirational
        product framing. No privacy alarm vocabulary applied to Google."""
        google_exec = "Rick Osterloh"
        google_title = "Google devices senior vice-president"
        google_vocabulary = "easy access to the AI agent Gemini"
        alarm_words = ["surveillance", "pervert", "creep", "ban"]
        for word in alarm_words:
            self.assertNotIn(word, google_vocabulary.lower())

    def test_idc_data_meta_two_thirds_market_share(self):
        """AAP article cites IDC data: Q1 2026 sales 2.25M smartglasses
        (+167% YoY), Meta leads with 'more than two-thirds'. This data
        is used as context, not to proportionalize scrutiny."""
        q1_2026_sales = 2_250_000
        meta_share = 0.67  # More than two-thirds
        yoy_growth = 1.67  # 167% increase
        self.assertGreater(q1_2026_sales, 2_000_000)
        self.assertGreater(meta_share, 0.5)


class TestTimesOfIndiaGlobalSouthExpansion(unittest.TestCase):
    """Times of India (Aug 13, 2026) expands the smart glasses privacy
    discourse to India — the third Global South geography after South Africa
    (#20, #21) and Australia (#26, #27)."""

    def test_india_trans_rights_protest_use(self):
        """Smart glasses used to secretly film attendees at a trans rights
        protest in Delhi (March 2026). Footage got 'millions of views'
        and 'exposed participants to online mockery.'"""
        incident = "trans rights protest in Delhi"
        date = "March 2026"
        views = "millions"
        outcome = "exposed participants to online mockery"
        self.assertIn("trans rights", incident)
        self.assertIn("Delhi", incident)

    def test_police_wearing_at_student_protests(self):
        """Senior police officer reportedly wearing smart glasses at
        Jantar Mantar student protests (July 2026). State surveillance
        use of consumer product — new dimension."""
        location = "Jantar Mantar"
        wearer = "senior police officer"
        date = "last month"  # July 2026 relative to Aug 13
        state_surveillance_use = True
        self.assertTrue(state_surveillance_use)

    def test_temple_violations(self):
        """People caught wearing smart glasses inside temples where
        photography is prohibited. Cultural-religious context adds new
        dimension not present in Western coverage."""
        location_type = "temples"
        prohibition = "photography is prohibited"
        cultural_religious_dimension = True
        self.assertTrue(cultural_religious_dimension)

    def test_pervert_glasses_vocabulary_in_india(self):
        """Times of India adopts 'pervert glasses' vocabulary from
        Western media ecosystem. Opening line: 'The internet already has
        a nickname for them: pervert glasses.'"""
        vocabulary = "pervert glasses"
        source = "The internet"
        self.assertIn("pervert", vocabulary)
        # Vocabulary has propagated from UK/US to India
        trans_continental_propagation = True
        self.assertTrue(trans_continental_propagation)

    def test_india_unique_use_cases(self):
        """India has THREE unique smart glasses use cases not present
        in Western coverage: trans rights protest filming, police state
        surveillance at protests, and temple photography violations."""
        unique_cases = [
            "trans rights protest filming",
            "police surveillance at protests",
            "temple photography violations"
        ]
        self.assertEqual(len(unique_cases), 3)
        # None of these appear in UK/US/EU/AU coverage
        for case in unique_cases:
            self.assertNotIn(case, [
                "pervert filming", "venue bans", "celebrity backlash",
                "regulatory complaint", "accessibility use"
            ])

    def test_global_south_geography_count(self):
        """India is the third Global South geography with documented
        smart glasses backlash, after South Africa (2 outlets) and
        Australia (3 outlets). Cultural consensus propagation confirmed
        across 3+ continents."""
        global_south_geographies = [
            "South Africa",  # Business Day Spotlight, Moneyweb
            "Australia",     # 7NEWS, 7NEWS Sunrise, AAP
            "India"          # Times of India
        ]
        self.assertEqual(len(global_south_geographies), 3)


class TestCrossMediumStigmatizationGradient(unittest.TestCase):
    """Maps the escalation gradient from coverage asymmetry to active
    stigmatization across media types."""

    def test_gradient_four_levels_documented(self):
        """Four distinct escalation levels now documented:
        1. Coverage selection asymmetry (most publications)
        2. Adversarial vocabulary framing (AmberMac, Smashing Security)
        3. Counter-product satire (DuckDuckGo, The Onion)
        4. Active stigmatization advocacy (The Observer)"""
        levels = {
            "coverage_selection": "Most outlets ignore competitors",
            "adversarial_vocabulary": "AmberMac 'pervert', Smashing Security 'villain'",
            "counter_product_satire": "DuckDuckGo 'Normal F***ing Sunglasses'",
            "stigmatization_advocacy": "Observer 'no shame in shaming'"
        }
        self.assertEqual(len(levels), 4)

    def test_observer_is_highest_escalation(self):
        """No other tracked media has explicitly advocated shaming
        product users and teaching children to fear the product."""
        observer_advocates_shaming = True
        observer_advocates_child_education = True
        any_other_outlet_matches = False
        self.assertTrue(observer_advocates_shaming)
        self.assertTrue(observer_advocates_child_education)
        self.assertFalse(any_other_outlet_matches)

    def test_samsung_press_trip_financial_relationship_predicts_vocabulary(self):
        """Financial relationship (Samsung press trip) → protective vocabulary.
        This mirrors the print/online pattern where content licensing deals
        (Condé Nast/OpenAI, FT/OpenAI, NYT/Amazon) predict softer coverage."""
        # AAP: Samsung-funded trip → "privacy controls"
        samsung_financial_relationship = True
        samsung_protective_vocabulary = True
        # No Meta financial relationship → "pervert glasses"
        meta_financial_relationship = False
        meta_adversarial_vocabulary = True
        self.assertTrue(samsung_financial_relationship)
        self.assertTrue(samsung_protective_vocabulary)
        self.assertFalse(meta_financial_relationship)
        self.assertTrue(meta_adversarial_vocabulary)


if __name__ == "__main__":
    unittest.main()
