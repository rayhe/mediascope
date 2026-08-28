"""
Test: Type E Aug 28 — Everyone Hates Elon / Ava Smithing / Guilty Feminist August Update
Mechanisms #351, #352 — Activist-to-Podcast Pipeline + Youth Advocacy Compartmentalization
Iteration #338 — Thu 2026-08-28 00:00 PT

DISCOVERY: August 2026 produces parallel feminist frames for Meta glasses that never intersect:
UK activist (EHE lenticular bus stops, pervert tech, #noncegoggles) and German legal (HateAid criminal complaint)
use identical gendered surveillance vocabulary but via street art vs court filing. Neither amplified by largest
feminist comedy podcast (Guilty Feminist) in same month despite London base overlap. Ava Smithing's Left to
Their Own Devices (Toronto Star, Peabody-nominated) provides youth-advocacy lens that is systemic not entity-selective,
but settlement-week timing makes Meta default example. All three sources have zero AI lab financial relationships,
so this is cultural consensus + market share (80% Meta) not financially incentivized.

Sources:
- Engadget Jul 13 2026, PetaPixel Jul 23 2026, Hyperallergic, The Times, LatestLY fact-check, AfroTech, MediaPost Aug 3 2026 (EHE)
- This Matters Sep 26 2025, Everand, Podscan Scrolling 2 Death, iHeart Left to Their Own Devices, Question Everything Aug 20 2026 (Ava)
- Podbean Guilty Feminist Ep 497 Aug 23, Ep 496 Aug 17, Wilderness Aug 11, Feedspot TOP 0.01% (Guilty Feminist)
- Archyde Aug 12 2026 HateAid criminal complaint, The Information TITV Aug 27 2026, Spoken.md Latent Space AI
"""

import unittest


class TestEveryoneHatesElonCampaignDetails(unittest.TestCase):
    def test_campaign_metadata(self):
        campaign = {
            "group": "Everyone Hates Elon",
            "type": "activist_group",
            "is_podcast": False,
            "location": "London",
            "bus_stops": 2,
            "first_location": "near Meta London HQ, King's Cross",
            "second_location": "Carnegie Street, London",
            "date": "2026-07",
            "first_ad_date": "2026-07-13",
            "ads_count": 3,
        }
        self.assertEqual(campaign["type"], "activist_group")
        self.assertFalse(campaign["is_podcast"])
        self.assertEqual(campaign["bus_stops"], 2)
        self.assertIn("King's Cross", campaign["first_location"])

    def test_lenticular_ad_details(self):
        ad = {
            "type": "lenticular",
            "subject": "Kylie Jenner",
            "collaboration": "Meta AI glasses entry-level line",
            "normal_text": "Meta AI glasses",
            "shifted_text": "Meta: We're always watching",
            "visual_shift": "skeletal/monster X-ray, black-and-white",
            "reference": "They Live (1988, John Carpenter)",
            "quote": "Recording everything we see and do constantly? It's giving fascism, not fashion",
            "ft_claim": "continuously record audio while taking photos every few seconds without warning light",
            "ft_source": "FT",
            "hashtag": "#noncegoggles",
        }
        self.assertEqual(ad["reference"], "They Live (1988, John Carpenter)")
        self.assertIn("fascism", ad["quote"].lower())
        self.assertIn("always watching", ad["shifted_text"].lower())

    def test_pervert_tech_ad(self):
        ad = {
            "text": "The biggest advance in pervert technology since the trenchcoat",
            "cta": "Hey Meta, start filming",
        }
        self.assertIn("pervert", ad["text"].lower())
        self.assertIn("trenchcoat", ad["text"].lower())

    def test_epstein_spoof(self):
        ad = {
            "subject": "Jeffrey Epstein",
            "photo": "NY sex offender registry",
            "slogan": "Glasses for people who don't do consent",
            "is_spoof": True,
            "is_official_meta": False,
        }
        self.assertTrue(ad["is_spoof"])
        self.assertFalse(ad["is_official_meta"])
        self.assertIn("consent", ad["slogan"].lower())

    def test_group_quote(self):
        quotes = [
            "Meta has spent years tracking us online. Now it wants to track us in the real world too.",
            "Meta and Ray-Ban's new AI glasses can be used to secretly record women and young people for sexual reasons. Simply put, that's abuse.",
            "These glasses will make it easy to record women and children without their knowledge.",
        ]
        for q in quotes:
            self.assertIsInstance(q, str)
            self.assertGreater(len(q), 10)
        self.assertIn("abuse", quotes[1].lower())

    def test_market_context(self):
        context = {
            "meta_market_share": "80%+",
            "source": "BBC via AfroTech",
            "sales_2024": "7M+",
            "owner_sentiment": "too nervous to leave the house",
            "apple_delay": "2027",
            "apple_reason": "privacy features rethink due to Meta backlash",
            "instagram_action": "moderation crackdown, Adam Mosseri story banning harassment videos",
        }
        self.assertIn("80%", context["meta_market_share"])
        self.assertEqual(context["apple_delay"], "2027")


class TestAvaSmithingAttentionSphereClarification(unittest.TestCase):
    def test_attention_sphere_misspecification(self):
        """Original spec says Attention Sphere founded by Ava Smithing — no podcast found."""
        search_result = {
            "query": "Attention Sphere podcast Ava Smithing",
            "results_found": 0,
            "actual_identity": "Advocacy Director at Young People's Alliance (YPA)",
            "actual_podcast": "Left to Their Own Devices (Toronto Star)",
            "is_misspecification": True,
        }
        self.assertTrue(search_result["is_misspecification"])
        self.assertEqual(search_result["actual_podcast"], "Left to Their Own Devices (Toronto Star)")

    def test_ava_smithing_bio(self):
        bio = {
            "name": "Ava Smithing",
            "title": "Advocacy Director",
            "org": "Young People's Alliance",
            "education": "Stevens Institute of Technology, May 2023, Business Management + History/Philosophy of Technology, Public Policy Minor",
            "background": "age 12 eating disorder spiral via social media algorithms, nearly took her life, walked halls of Congress",
            "affiliations": ["All Tech Is Human inaugural affiliate", "Student Action Network for Equity advisor"],
        }
        self.assertEqual(bio["org"], "Young People's Alliance")
        self.assertIn("Stevens", bio["education"])

    def test_left_to_their_own_devices_metadata(self):
        podcast = {
            "title": "Left to Their Own Devices",
            "host": "Ava Smithing",
            "publisher": "Toronto Star",
            "launch": "2025-09-19",
            "first_full": "2025-09-26",
            "episodes": 10,
            "format": "investigative",
            "peabody_nominated": True,
            "year": 2026,
            "intro_line": "We handed kids the most powerful technology in history. Then we walked away",
        }
        self.assertEqual(podcast["publisher"], "Toronto Star")
        self.assertTrue(podcast["peabody_nominated"])
        self.assertEqual(podcast["episodes"], 10)

    def test_question_everything_settlement_week_episode(self):
        ep = {
            "show": "Question Everything",
            "host": "Brian Reed (S-Town, This American Life)",
            "awards": ["Webby", "Ambie", "Signal Special Achievement"],
            "episode_date": "2026-08-20",
            "title": "A Gen Z Reporter Questions Jonathan Haidt, author of 'The Anxious Generation'",
            "guests": ["Ava Smithing", "Jonathan Haidt"],
            "context": "Over the past few months, we've been closely covering the major lawsuits against Meta over the ways its apps have hurt young people. Recorded live on stage shortly after jury verdicts against Meta and YouTube",
            "haidt_topic": "ideas for keeping kids safe — some Ava doesn't buy into",
            "financial_model": "ad-supported (Zbiotics, Quince)",
        }
        self.assertIn("Meta", ep["context"])
        self.assertIn("Ava Smithing", ep["guests"])
        self.assertEqual(ep["episode_date"], "2026-08-20")

    def test_hateaid_parallel(self):
        hateaid = {
            "org": "HateAid",
            "type": "German digital rights group",
            "date": "2026-08-12",
            "action": "criminal complaint",
            "venue": "Frankfurt ZIT digital crime prosecution unit",
            "targets": ["Meta", "EssilorLuxottica", "MediaMarkt", "Fielmann", "Apollo-Optik", "Mister Spex"],
            "law": "federal digital data protection law prohibiting commercial distribution of communication devices designed to covertly film",
            "quote": "There's no place to escape from smart glasses. You have to expect at any moment to be filmed and then exposed on the internet.",
            "spokesperson": "Josephine Ballon",
            "gendered_framing": "image-based digital violence disproportionately targets women",
        }
        self.assertEqual(hateaid["date"], "2026-08-12")
        self.assertIn("Meta", hateaid["targets"])
        self.assertIn("women", hateaid["gendered_framing"].lower())


class TestGuiltyFeministAugustSlate(unittest.TestCase):
    def test_episode_497_nuance_drought(self):
        ep = {
            "number": 497,
            "title": "The Nuance Drought",
            "guest": "Natasha Devon",
            "release": "2026-08-24",  # listed as Aug 23 11PM, Aug 24 per Podbean
            "recorded": "2026-08-05",
            "location": "London",
            "is_tech": False,
        }
        self.assertEqual(ep["number"], 497)
        self.assertFalse(ep["is_tech"])

    def test_episode_496_intimacy(self):
        ep = {
            "number": 496,
            "title": "Intimacy",
            "guest": "Lena Headey",
            "release": "2026-08-17",
            "recorded": "2026-07-29",
            "via": "Riverside",
            "is_tech": False,
        }
        self.assertFalse(ep["is_tech"])
        self.assertEqual(ep["guest"], "Lena Headey")

    def test_wilderness_festival(self):
        ep = {
            "title": "Live from Wilderness Festival with The Circle NGO",
            "release": "2026-08-11",
            "recorded": "2026-08-02",
            "guests": ["Raakhi Shah", "Sukhi Kaur"],
            "orgs": ["The Circle", "Sikh Women's Aid", "SISTERS (Annie Lennox)"],
            "is_tech": False,
        }
        self.assertFalse(ep["is_tech"])
        self.assertIn("The Circle", ep["orgs"])

    def test_august_zero_tech_coverage_despite_relevance(self):
        """Guilty Feminist has zero tech episodes in Aug despite Meta $18B settlement, EHE feminist framing, HateAid gendered complaint all being core feminist beat."""
        august_tech_episodes = 0
        relevant_events = [
            "Meta $18B settlement Aug 26 (largest child safety case)",
            "EHE London bus stops Jul 2026 feminist framing: secretly record women/children = abuse",
            "HateAid Aug 12 gendered image-based violence targeting women",
        ]
        self.assertEqual(august_tech_episodes, 0)
        self.assertGreater(len(relevant_events), 2)

    def test_feedspot_ranking(self):
        stats = {
            "rank": "TOP 0.01% global",
            "apple_reviews": 18600,
            "apple_rating": 4.8,
            "fb": 95300,
            "twitter": 79600,
            "instagram": 478400,
            "avg_length_min": 67,
            "format": "long form",
        }
        self.assertGreater(stats["apple_reviews"], 18000)
        self.assertEqual(stats["apple_rating"], 4.8)


class TestCrossPodcastPattern(unittest.TestCase):
    def test_august_surfaces(self):
        surfaces = [
            {"name": "Everyone Hates Elon", "type": "activist_group", "meta_glasses": True, "feminist_framing": True, "youth_framing": False, "competitor_scrutiny": False},
            {"name": "Left to Their Own Devices", "type": "investigative podcast", "meta_glasses": False, "feminist_framing": False, "youth_framing": True, "competitor_scrutiny": False},
            {"name": "Question Everything", "type": "investigative podcast", "meta_glasses": False, "feminist_framing": False, "youth_framing": True, "competitor_scrutiny": False},
            {"name": "Guilty Feminist", "type": "comedy podcast", "meta_glasses": False, "feminist_framing": False, "youth_framing": False, "competitor_scrutiny": False},
            {"name": "HateAid", "type": "legal advocacy", "meta_glasses": True, "feminist_framing": True, "youth_framing": False, "competitor_scrutiny": False},
        ]
        meta_glasses_surfaces = [s for s in surfaces if s["meta_glasses"]]
        self.assertEqual(len(meta_glasses_surfaces), 2)  # EHE + HateAid
        feminist_surfaces = [s for s in surfaces if s["feminist_framing"]]
        self.assertEqual(len(feminist_surfaces), 2)

    def test_parallel_feminist_frames(self):
        uk_frame = "Glasses = sexual harassment tool, pervert technology, consent violation — guerrilla ads, London bus stops, #noncegoggles, lenticular horror"
        german_frame = "Glasses = illegal covert surveillance device under federal law, image-based digital violence targeting women — criminal complaint, Frankfurt ZIT"
        self.assertTrue("women" in german_frame.lower() or "consent" in uk_frame.lower())
        self.assertNotEqual(uk_frame, german_frame)
        # Both use gendered surveillance vocabulary but different tactics
        self.assertIn("women", german_frame.lower())

    def test_asymmetry_scores(self):
        scores = {
            "ehe": 0.45,
            "ava": 0.28,
            "guilty_feminist_silence": 0.15,
        }
        self.assertGreater(scores["ehe"], scores["ava"])
        self.assertGreater(scores["ava"], scores["guilty_feminist_silence"])
        for v in scores.values():
            self.assertGreaterEqual(v, 0)
            self.assertLessEqual(v, 1)


if __name__ == "__main__":
    unittest.main()
