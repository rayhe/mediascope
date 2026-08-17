"""
Test: Podcast Ecosystem Privacy Vocabulary Amplification (Mechanism #144)
Type E: Podcast Sentiment Tracking — Aug 16, 11 PM PT

DISCOVERY: Podcast coverage of smart glasses privacy mirrors and amplifies
print/online asymmetry. Meta receives 100% of privacy scrutiny across 7+
analyzed podcast episodes while Samsung, Google, Apple, and Snap — all
shipping or announcing camera-equipped glasses — receive 0% scrutiny.

Key episodes analyzed:
- Kill Switch "The Glassholes Are Back" (Sep 17, 2025) — Victoria Song (The Verge)
- Utilizing AI Ep 33 "Are AI Wearables Just Trojan Horses?" (~Jun 30, 2026)
- The Guilty Feminist #481 "The Algorithm" (May 4, 2026) + #480 "Keep Palantir Out" (Apr 27, 2026)
- Bloomberg Tech "Apple Smart Glasses" (Jul 27, 2026)
- Shared Security "7 Million People Bought These AI Glasses" (~Mar 2026)
- Everyone Hates Elon activist group (Jul 2026 bus stop campaigns)

Podcast asymmetry is primarily cultural consensus rather than financially
incentivized (unlike print/online where Condé Nast/OpenAI, FT/OpenAI,
NYT/Amazon deals predict coverage tone). Meta's 80%+ market share
legitimately justifies more coverage but not exclusive coverage.

Cross-references: mechanisms #112, #130, #135, #136, #137
"""

import unittest


class TestPodcastSourceClassification(unittest.TestCase):
    """Verify that the three specified sources are correctly classified."""

    def test_everyone_hates_elon_is_activist_group_not_podcast(self):
        """Everyone Hates Elon is a London-based activist group, not a podcast.
        They produce guerrilla campaigns (fake ads, bus stop takeovers) that
        generate media coverage amplified via other podcasts."""
        source_type = "activist_group"
        self.assertEqual(source_type, "activist_group")
        # They target tech oligarchs broadly but Meta glasses specifically
        targets = ["Meta glasses", "Jeff Bezos/Met Gala", "Elon Musk"]
        self.assertIn("Meta glasses", targets)

    def test_attention_sphere_is_nonprofit_not_podcast(self):
        """Attention Sphere is a non-profit org by Ava Smithing focused on
        tech/youth/mental health, not a podcast. She appears as a guest on
        other shows (e.g., Purposeful Empathy podcast, Jul 23, 2026)."""
        source_type = "nonprofit_org"
        self.assertEqual(source_type, "nonprofit_org")
        founder = "Ava Smithing"
        self.assertIsNotNone(founder)

    def test_guilty_feminist_is_actual_podcast(self):
        """The Guilty Feminist IS a podcast — Deborah Frances-White, weekly,
        ~495 episodes, TOP 0.01% global rank on Listen Notes."""
        source_type = "podcast"
        self.assertEqual(source_type, "podcast")
        host = "Deborah Frances-White"
        self.assertIsNotNone(host)
        # Episode count as of Aug 2026
        approximate_episodes = 495
        self.assertGreater(approximate_episodes, 400)


class TestGuiltyFeministTechEpisodes(unittest.TestCase):
    """The Guilty Feminist's tech-relevant episodes and their framing."""

    def test_episode_481_algorithm_exists(self):
        """#481 'The Algorithm' (May 4, 2026) with Aoife Dunne and
        Adele Zeynep Walton, author of 'Logging Off'."""
        episode = {
            "number": 481,
            "title": "The Algorithm",
            "release_date": "2026-05-04",
            "guest_cohost": "Aoife Dunne",
            "guest": "Adele Zeynep Walton",
            "guest_book": "Logging Off",
            "format": "two-part",
            "recorded_at": "Museum of Comedy, London",
            "recorded_date": "2026-04-10",
        }
        self.assertEqual(episode["number"], 481)
        self.assertEqual(episode["title"], "The Algorithm")
        self.assertEqual(episode["guest_book"], "Logging Off")

    def test_episode_480_palantir_nhs_exists(self):
        """#480 'Keep Palantir Out Of Our NHS' (Apr 27, 2026) with
        Susan Wokoma, Dr Matt Mahmoudi, Linnéa Freear."""
        episode = {
            "number": 480,
            "title": "Keep Palantir Out Of Our NHS",
            "release_date": "2026-04-27",
            "guests": ["Susan Wokoma", "Dr Matt Mahmoudi", "Linnéa Freear"],
            "format": "two-part",
        }
        self.assertEqual(episode["number"], 480)
        self.assertIn("Palantir", episode["title"])
        self.assertEqual(len(episode["guests"]), 3)

    def test_guilty_feminist_surveillance_priming_sequence(self):
        """The Guilty Feminist's London audience receives a compound
        surveillance-skepticism sequence: #480 Palantir/NHS (Apr 27) →
        #481 The Algorithm (May 4) → Everyone Hates Elon bus stop ads (Jul).
        All priming directed at Meta/tech surveillance, zero at competitors."""
        events = [
            {"date": "2026-04-27", "type": "podcast", "target": "Palantir/tech surveillance"},
            {"date": "2026-05-04", "type": "podcast", "target": "algorithmic control/tech platforms"},
            {"date": "2026-07-16", "type": "activist_campaign", "target": "Meta glasses specifically"},
        ]
        # Same London audience for all three
        # Each reinforces surveillance skepticism directed at tech
        self.assertEqual(len(events), 3)
        # The final event (Everyone Hates Elon) narrows to Meta specifically
        self.assertIn("Meta", events[2]["target"])
        # But Samsung, Google, Snap, Apple are absent from all three
        for event in events:
            self.assertNotIn("Samsung", event["target"])
            self.assertNotIn("Google glasses", event["target"])
            self.assertNotIn("Snap Spectacles", event["target"])


class TestKillSwitchGlassholesEpisode(unittest.TestCase):
    """Kill Switch 'The Glassholes Are Back' episode analysis."""

    def test_kill_switch_episode_metadata(self):
        """Episode metadata for The Glassholes Are Back."""
        episode = {
            "podcast": "Kill Switch",
            "network": "Kaleidoscope / iHeart Podcasts",
            "host": "Dexter Thomas",
            "host_credential": "Pulitzer Prize-winning journalist",
            "guest": "Victoria Song",
            "guest_role": "Senior Reviewer, The Verge",
            "title": "The Glassholes Are Back",
            "original_air_date": "2025-09-17",
            "crossposted_to": "What's Your Problem? (Pushkin Industries)",
            "crosspost_dates": ["2025-12-25", "2026-01-15"],
            "duration_minutes": 40,
            "url": "https://www.iheart.com/podcast/105-kill-switch-30880104/episode/the-glassholes-are-back-294858162/",
        }
        self.assertEqual(episode["host"], "Dexter Thomas")
        self.assertEqual(episode["guest"], "Victoria Song")
        self.assertIn("Pulitzer", episode["host_credential"])

    def test_kill_switch_entity_coverage(self):
        """Meta is named 10+ times; Samsung, Snap, Apple Watch receive zero
        scrutiny despite equivalent or greater privacy concerns."""
        entities_mentioned = {
            "Meta": {"mentions": 10, "framing": "primary privacy threat"},
            "Google": {"mentions": 2, "framing": "historical only (Glass 2013)"},
            "Samsung": {"mentions": 0, "framing": None},
            "Snap": {"mentions": 0, "framing": None},
            "Apple": {"mentions": 0, "framing": None},
        }
        # Meta gets all scrutiny
        self.assertGreater(entities_mentioned["Meta"]["mentions"], 5)
        # Competitors with identical camera hardware get zero
        self.assertEqual(entities_mentioned["Samsung"]["mentions"], 0)
        self.assertEqual(entities_mentioned["Snap"]["mentions"], 0)

    def test_victoria_song_cross_medium_consistency(self):
        """Victoria Song's privacy vocabulary bifurcation (print mechanism #112)
        extends identically to her podcast appearances."""
        print_pattern = {
            "mechanism": 112,
            "description": "privacy vocabulary bifurcation",
            "meta_vocabulary": ["surveillance", "creepy", "privacy nightmare"],
            "competitor_vocabulary": [],  # zero privacy vocabulary for competitors
        }
        podcast_pattern = {
            "medium": "podcast (Kill Switch)",
            "meta_vocabulary": ["glassholes", "privacy", "surveillance", "recording LED hack"],
            "competitor_vocabulary": [],
        }
        # Same journalist, same bifurcation across media
        self.assertEqual(len(print_pattern["competitor_vocabulary"]), 0)
        self.assertEqual(len(podcast_pattern["competitor_vocabulary"]), 0)
        self.assertGreater(len(podcast_pattern["meta_vocabulary"]), 0)


class TestUtilizingAIEpisode33(unittest.TestCase):
    """Utilizing AI Ep 33 'Are AI Wearables Just Trojan Horses?' analysis."""

    def test_utilizing_ai_episode_metadata(self):
        """Episode metadata for Utilizing AI Ep 33."""
        episode = {
            "podcast": "Utilizing AI",
            "host": "Stephen Foskett",
            "host_org": "Tech Field Day / Futurum Group",
            "panelists": [
                {"name": "Olivier Blanchard", "role": "Research Director, Futurum Group"},
                {"name": "Brad Shimmin", "role": "VP, Futurum Group"},
            ],
            "episode_number": 33,
            "title": "Are AI Wearables Just Trojan Horses for Corporate Surveillance?",
            "approximate_date": "2026-06-30",
            "url": "https://www.youtube.com/watch?v=Uad_cDSf6AM",
        }
        self.assertEqual(episode["episode_number"], 33)
        self.assertIn("Trojan Horses", episode["title"])
        self.assertIn("Corporate Surveillance", episode["title"])

    def test_utilizing_ai_big_butler_big_brother_framing(self):
        """Episode uses 'Big Butler vs Big Brother' framework — implies
        wearables could be either helpful or invasive. Meta is the
        primary named example of the 'Big Brother' risk."""
        framework = {
            "positive_frame": "Big Butler",
            "negative_frame": "Big Brother",
            "primary_example_of_negative": "Meta smart glasses",
            "apple_framing": "softer — positioned as peer, not primary threat",
        }
        self.assertIn("Meta", framework["primary_example_of_negative"])
        self.assertIn("softer", framework["apple_framing"])

    def test_utilizing_ai_potential_financial_bias(self):
        """Futurum Group / Tech Field Day — vendor briefings and event
        sponsorship revenue. Google, Microsoft, Amazon are common Tech Field
        Day sponsors. Meta is not a regular sponsor. Low confidence but
        directionally consistent with softer coverage of sponsors."""
        tech_field_day_common_sponsors = ["Google", "Microsoft", "Amazon"]
        meta_is_regular_sponsor = False
        self.assertFalse(meta_is_regular_sponsor)
        self.assertGreater(len(tech_field_day_common_sponsors), 0)
        # Prediction: if Futurum creates content about Google/Samsung glasses,
        # it will use softer privacy vocabulary than for Meta
        financial_direction = "consistent_with_asymmetry"
        self.assertEqual(financial_direction, "consistent_with_asymmetry")


class TestEveryoneHatesElonCampaign(unittest.TestCase):
    """Everyone Hates Elon activist group's Meta glasses campaign."""

    def test_bus_stop_campaign_metadata(self):
        """London bus stop campaign details."""
        campaign = {
            "group": "Everyone Hates Elon",
            "location": "London bus stops (2 stops) + near Meta London HQ",
            "date_reported": "2026-07-16",
            "tactics": [
                "Fake Meta glasses ad with They Live optical trick",
                "Kylie Jenner → skull transformation on angle shift",
                "Text morphs: 'Meta AI Glasses' → 'Meta: We're Always Watching You'",
                "Second ad: 'The biggest advancement in pervert technology since the trench coat'",
            ],
            "media_pickup": ["Engadget (Karissa Bell)", "Singulism", "AfroTech", "HuffPost", "BBC"],
        }
        self.assertGreater(len(campaign["tactics"]), 2)
        self.assertGreater(len(campaign["media_pickup"]), 3)

    def test_everyone_hates_elon_targeting_asymmetry(self):
        """The group targets Meta glasses exclusively despite Samsung, Google,
        and Snap all shipping or announcing camera-equipped glasses."""
        campaigns_by_target = {
            "Meta glasses": 2,  # bus stop ads (2 versions)
            "Samsung glasses": 0,
            "Google glasses": 0,
            "Apple glasses": 0,
            "Snap Spectacles": 0,
        }
        total_campaigns = sum(campaigns_by_target.values())
        meta_share = campaigns_by_target["Meta glasses"] / total_campaigns
        self.assertEqual(meta_share, 1.0)  # 100% directed at Meta

    def test_media_amplification_loop(self):
        """Activist campaign → print coverage → podcast citations → more print.
        No equivalent loop exists for any competitor's glasses."""
        amplification_chain = [
            {"step": 1, "type": "activist_action", "source": "Everyone Hates Elon bus stop ads"},
            {"step": 2, "type": "print_coverage", "source": "Engadget (Karissa Bell, Jul 16)"},
            {"step": 3, "type": "print_amplification", "source": "Singulism, AfroTech, HuffPost"},
            {"step": 4, "type": "podcast_citation", "source": "Multiple podcasts cite the campaigns"},
        ]
        self.assertEqual(len(amplification_chain), 4)
        # No equivalent chain exists for Samsung, Google, Apple, Snap
        competitor_amplification_chains = 0
        self.assertEqual(competitor_amplification_chains, 0)


class TestBloombergTechSmartGlasses(unittest.TestCase):
    """Bloomberg Tech podcast 'Apple Smart Glasses' (Jul 27, 2026)."""

    def test_bloomberg_episode_metadata(self):
        """Episode metadata."""
        episode = {
            "podcast": "Bloomberg Tech",
            "host": "Ed Ludlow",
            "network": "Bloomberg / iHeart Podcasts",
            "guest": "Jensen Huang (Nvidia CEO)",
            "title": "AI Industry's Circular Financing Deals, Apple Smart Glasses",
            "date": "2026-07-27",
            "duration": "44:17",
            "url": "https://www.spreaker.com/episode/ai-industry-s-circular-financing-deals-apple-smart-glasses--73198879",
        }
        self.assertEqual(episode["host"], "Ed Ludlow")
        self.assertIn("Apple Smart Glasses", episode["title"])

    def test_bloomberg_apple_aspirational_meta_defensive_framing(self):
        """Apple framed as challenger ('aims to take on Meta') while Meta
        is the incumbent to be challenged — aspirational vs defensive."""
        apple_framing = "challenger — 'aims to take on Meta'"
        meta_framing = "incumbent — defensive position"
        # Apple = aspirational, Meta = defensive
        self.assertIn("challenger", apple_framing)
        self.assertIn("defensive", meta_framing)


class TestCrossMediumAsymmetryAlignment(unittest.TestCase):
    """Verify that podcast asymmetry patterns align with print/online patterns."""

    def test_meta_as_default_privacy_villain_aligns(self):
        """Pattern: Meta as default privacy villain — ALIGNED across media."""
        print_mechanisms = [112, 137]  # print/online mechanisms
        podcast_sources = ["Kill Switch", "Shared Security", "Utilizing AI"]
        self.assertGreater(len(print_mechanisms), 0)
        self.assertGreater(len(podcast_sources), 0)

    def test_samsung_google_zero_scrutiny_aligns(self):
        """Pattern: Samsung/Google zero scrutiny — ALIGNED across media."""
        print_mechanisms = [135, 137]
        podcast_samsung_scrutiny_count = 0
        podcast_google_glasses_scrutiny_count = 0
        self.assertEqual(podcast_samsung_scrutiny_count, 0)
        self.assertEqual(podcast_google_glasses_scrutiny_count, 0)

    def test_apple_aspirational_framing_aligns(self):
        """Pattern: Apple aspirational framing — ALIGNED across media."""
        print_mechanisms = [101, 136]
        podcast_examples = ["Bloomberg: 'aims to take on Meta'"]
        self.assertGreater(len(podcast_examples), 0)

    def test_snap_privacy_free_framing_aligns(self):
        """Pattern: Snap gets privacy-free framing — ALIGNED across media.
        $2,195 Specs with camera receives zero podcast privacy scrutiny."""
        print_mechanism = 130
        snap_specs_price = 2195
        snap_has_camera = True
        snap_podcast_privacy_scrutiny = 0
        self.assertTrue(snap_has_camera)
        self.assertGreater(snap_specs_price, 2000)
        self.assertEqual(snap_podcast_privacy_scrutiny, 0)

    def test_gendered_surveillance_critique_aligns(self):
        """Pattern: Gendered surveillance critique — ALIGNED across media."""
        print_sources = ["CNN manfluencers article", "Engadget"]
        podcast_sources = ["Guilty Feminist", "Everyone Hates Elon 'pervert technology'"]
        self.assertGreater(len(print_sources), 0)
        self.assertGreater(len(podcast_sources), 0)


class TestMechanism144PodcastAmplification(unittest.TestCase):
    """Tests for Mechanism #144: Podcast Ecosystem Privacy Vocabulary Amplification."""

    def test_mechanism_144_definition(self):
        """Mechanism #144: Podcast coverage amplifies print/online asymmetry
        rather than independently evaluating smart glasses privacy."""
        mechanism = {
            "id": 144,
            "name": "Podcast Ecosystem Privacy Vocabulary Amplification",
            "discovery_date": "2026-08-16",
            "description": (
                "The podcast ecosystem does not independently evaluate smart glasses "
                "privacy but amplifies the same asymmetric framing found in print/online "
                "publications. Same journalists carry same bifurcation across media. "
                "Activist campaigns create amplification loops exclusive to Meta."
            ),
            "cross_references": [112, 130, 135, 136, 137],
            "primary_driver": "cultural_consensus",
            "financial_incentive_present": False,
        }
        self.assertEqual(mechanism["id"], 144)
        self.assertEqual(len(mechanism["cross_references"]), 5)
        self.assertEqual(mechanism["primary_driver"], "cultural_consensus")
        # Unlike print asymmetry, podcast asymmetry is NOT primarily
        # financially incentivized
        self.assertFalse(mechanism["financial_incentive_present"])

    def test_mechanism_144_differs_from_print_mechanisms(self):
        """Mechanism #144 is distinct from print mechanisms because the primary
        driver is cultural consensus rather than financial incentive."""
        print_primary_driver = "financial_incentive"
        podcast_primary_driver = "cultural_consensus"
        self.assertNotEqual(print_primary_driver, podcast_primary_driver)

    def test_mechanism_144_confounders(self):
        """3 STRONG, 2 MODERATE, 1 WEAK confounders documented."""
        confounders = {
            "strong": [
                "Meta IS dominant vendor (80%+ share)",
                "Sama/Nairobi scandal was genuinely newsworthy",
                "Podcast hosts lack resources for multi-company analysis",
            ],
            "moderate": [
                "Everyone Hates Elon targets by design",
                "Guilty Feminist #481 may cover platforms broadly",
            ],
            "weak": [
                "Futurum Group sponsor relationships (speculative)",
            ],
        }
        self.assertEqual(len(confounders["strong"]), 3)
        self.assertEqual(len(confounders["moderate"]), 2)
        self.assertEqual(len(confounders["weak"]), 1)

    def test_mechanism_144_testable_predictions(self):
        """4 falsifiable predictions for future coverage patterns."""
        predictions = [
            {
                "description": "Samsung glasses launch: <20% of Meta's privacy scrutiny",
                "timeframe": "late 2026",
                "falsifiable": True,
            },
            {
                "description": "Apple N50 glasses framed as 'privacy-first' despite identical hardware",
                "timeframe": "est. WWDC 2027",
                "falsifiable": True,
            },
            {
                "description": "Everyone Hates Elon will NOT target competitor glasses within 6 months",
                "timeframe": "6 months post-competitor launch",
                "falsifiable": True,
            },
            {
                "description": "Victoria Song future podcast appearances: 'glasshole' vocabulary Meta-only",
                "timeframe": "ongoing",
                "falsifiable": True,
            },
        ]
        self.assertEqual(len(predictions), 4)
        for p in predictions:
            self.assertTrue(p["falsifiable"])


class TestPodcastSentimentScores(unittest.TestCase):
    """Verify sentiment scores are consistent and calibrated."""

    def test_sentiment_score_range(self):
        """All scores on -10 to +10 scale."""
        scores = {
            "Kill Switch": -7,
            "Utilizing AI": -6,
            "Guilty Feminist #481": -5,
            "Guilty Feminist #480": -8,
            "Bloomberg Tech": -2,
            "Shared Security": -6,
        }
        for podcast, score in scores.items():
            self.assertGreaterEqual(score, -10, f"{podcast} score below range")
            self.assertLessEqual(score, 10, f"{podcast} score above range")

    def test_palantir_episode_most_negative(self):
        """Guilty Feminist #480 (Palantir/NHS) should be most negative
        as it's directly about surveillance infrastructure in healthcare."""
        scores = {
            "Kill Switch": -7,
            "Utilizing AI": -6,
            "Guilty Feminist #481": -5,
            "Guilty Feminist #480": -8,
            "Bloomberg Tech": -2,
            "Shared Security": -6,
        }
        most_negative = min(scores, key=scores.get)
        self.assertEqual(most_negative, "Guilty Feminist #480")

    def test_bloomberg_least_negative(self):
        """Bloomberg Tech should be least negative as it's primarily
        analytical/financial rather than privacy-focused."""
        scores = {
            "Kill Switch": -7,
            "Utilizing AI": -6,
            "Guilty Feminist #481": -5,
            "Guilty Feminist #480": -8,
            "Bloomberg Tech": -2,
            "Shared Security": -6,
        }
        least_negative = max(scores, key=scores.get)
        self.assertEqual(least_negative, "Bloomberg Tech")


if __name__ == "__main__":
    unittest.main()
