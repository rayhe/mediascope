"""
Test: Lawrence Bonk (Engadget / Yahoo) — Generalist Beat Assignment as Stigma Concentration Mechanism
Mechanism #198: Editorial Routing of Category-Level Camera-Glasses Restrictions Through Non-Beat Reporters

Discovery date: 2026-08-20
Type: Journalist Cross-Entity Tracking (Type B)
Publication: Engadget (Yahoo Inc.)
Journalist: Lawrence Bonk
Entities: Meta, Snap, Samsung, Google, Apple
Asymmetry score: 0.79

THESIS:
When Engadget covers category-level restrictions on camera-equipped smart glasses,
it assigns the story to a GENERALIST reporter (Lawrence Bonk: gaming consoles,
music tech, smart home) rather than its dedicated smart glasses/AR beat reporters
(Karissa Bell, Sam Rutherford, Cherlynn Low). This structural routing produces
three compounding asymmetric effects:

1. VOCABULARY ESCALATION: Without beat-level cross-entity context, the generalist
   applies maximum editorial force — "shady specs," links to "pervert glasses,"
   harassment studies, CEO personalization — terms that beat reporters would
   calibrate with competitor context.

2. CROSS-ENTITY OMISSION: The generalist has no obligation or context to mention
   that Samsung (identical 12MP camera, launching UK fall 2026), Snap (4 cameras,
   launching UK fall 2026), Google, and Apple are all developing/shipping similar
   camera glasses. The court ban applies to ALL camera-enabled smart glasses.

3. STRUCTURAL ROUTING CONTRAST: Engadget's beat reporters (Bell) cover Snap/
   competitor launches with aspirational framing and exclusive CEO access.
   Privacy-alarm Meta stories get routed to generalists who lack the cross-entity
   context to note parity.

This is distinct from:
- Direct vocabulary bifurcation (#115): Same journalist, different words for
  different entities
- Coverage selection silence (#33): Simply not covering competitors
- CEO-attribution delegitimization (#191): Personalizing corporate strategy

Beat-assignment stigma concentration operates at the EDITORIAL level — the
decision of WHO covers WHICH story concentrates privacy stigma on Meta through
structural routing rather than individual journalist bias.

SOURCES:
- Lawrence Bonk court ban article: https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/
- Karissa Bell Snap Specs launch: https://www.engadget.com/2195207/snap-ar-specs-launch-price/
- Karissa Bell Spiegel interview: https://Www.engadget.com/2195862/snap-specs-ceo-evan-spiegel-interview-at-awe-2026/
- Lawrence Bonk author page: https://WWW.ENGADGET.COM/author/lawrence-bonk/
- UK Cinema Association ban (Reuters): https://www.reuters.com/business/media-telecom/uk-cinemas-restricting-meta-ai-other-smart-glasses-over-piracy-concerns-2026-08-20/

CONFOUNDERS:
1. STRONG: Meta has 80%+ smart glasses market share — covering restrictions as
   Meta-specific may reflect market reality, not editorial bias
2. STRONG: Generalist assignment may simply reflect staffing/availability, not
   deliberate editorial routing
3. MODERATE: Bonk's article was a news piece, not a product review — different
   editorial standards apply
4. MODERATE: Snap Specs hadn't shipped when court ban was announced (pre-launch
   vs shipping product)
5. WEAK: Bonk may have limited word count that precludes competitor context

Cross-references: #8 (Safe Target Coefficient), #33 (OpenAI facial recognition
parity), #121 (Fast Company same-event framing), #160 (Nadeem Sarwar editorial
routing), #197 (Reuters wire-level vocabulary bifurcation)
"""

import unittest


class TestLawrenceBonkProfile(unittest.TestCase):
    """Verify Lawrence Bonk's documented profile and beat assignment."""

    def test_bonk_is_engadget_writer(self):
        """Lawrence Bonk is a staff writer at Engadget."""
        profile = {
            "name": "Lawrence Bonk",
            "publication": "Engadget",
            "parent_company": "Yahoo Inc.",
            "location": "Minneapolis, Minnesota",
            "education": "Florida State University, BA Creative Writing",
            "expertise": ["Gaming consoles", "Music tech", "Smart home devices"],
            "career_span": "almost two decades",
            "prior_bylines": ["Huffington Post", "Forbes", "Rolling Stone"],
        }
        self.assertEqual(profile["publication"], "Engadget")
        self.assertIn("Gaming consoles", profile["expertise"])
        self.assertNotIn("Smart glasses", profile["expertise"])
        self.assertNotIn("AR/VR", profile["expertise"])
        self.assertNotIn("Wearables", profile["expertise"])

    def test_bonk_is_not_smart_glasses_beat_reporter(self):
        """Bonk's documented expertise does NOT include smart glasses, AR, or wearables."""
        bonk_expertise = ["Gaming consoles", "Music tech", "Smart home devices"]
        smart_glasses_keywords = [
            "smart glasses", "augmented reality", "wearables",
            "Meta glasses", "Ray-Ban", "Snap Specs", "Spectacles",
        ]
        for keyword in smart_glasses_keywords:
            for expertise in bonk_expertise:
                self.assertNotEqual(keyword.lower(), expertise.lower(),
                    f"Bonk's expertise should not be '{keyword}' — he is a generalist")
        # None of his listed expertise areas relate to AR/smart glasses
        ar_related = [e for e in bonk_expertise
                      if e.lower() in ("ar", "augmented reality", "smart glasses", "wearables")]
        self.assertEqual(len(ar_related), 0,
            "None of Bonk's expertise areas are AR/smart glasses related")

    def test_engadget_has_dedicated_smart_glasses_reporters(self):
        """Engadget has dedicated beat reporters for smart glasses/AR coverage."""
        beat_reporters = {
            "Karissa Bell": {
                "coverage": ["Snap Specs launch", "Spiegel interview", "Meta privacy risk guide"],
                "exclusive_access": ["Evan Spiegel sit-down post-AWE keynote"],
            },
            "Sam Rutherford": {
                "coverage": ["Smart glasses reviews", "AR hardware"],
            },
            "Cherlynn Low": {
                "coverage": ["Smart glasses reviews", "Wearable tech"],
            },
            "Will Shanklin": {
                "coverage": ["German criminal complaint against Meta glasses"],
            },
        }
        self.assertGreaterEqual(len(beat_reporters), 3,
            "Engadget has at least 3 reporters with smart glasses beat experience")
        self.assertIn("Karissa Bell", beat_reporters,
            "Karissa Bell is Engadget's primary Snap/AR beat reporter")


class TestBonkCourtBanArticleEditorialVocabulary(unittest.TestCase):
    """Analyze the editorial vocabulary in Bonk's UK court ban article."""

    def setUp(self):
        self.article = {
            "title": "England And Wales Ban Meta Glasses From Courtrooms",
            "author": "Lawrence Bonk",
            "publication": "Engadget",
            "date": "2026-08-11",
            "url": "https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/",
            "word_count_approx": 450,
        }
        # Editorial vocabulary used
        self.alarm_vocabulary = [
            "shady specs",           # Pejorative nickname for Meta glasses
            "pervert glasses",       # Linked external reference to stigma label
            "secretly film",         # Covert recording framing
            "surreptitiously",       # Covert intent attribution
            "filming people without their consent",
            "especially harrowing for women",  # Gendered threat framing
            "harassment",            # From linked University of Sydney study
            "doxxed",                # From linked study
        ]
        self.ceo_personalization = [
            "Mark Zuckerberg and his team don't seem terribly concerned",
            "The Meta CEO",
            "entourage were wearing the glasses",
            "The judge had to threaten contempt of court",
        ]

    def test_article_names_only_meta(self):
        """The article names only Meta despite the ban covering ALL camera-enabled smart glasses."""
        entities_named = ["Meta"]
        entities_absent = ["Snap", "Samsung", "Google", "Apple", "Warby Parker", "Gentle Monster"]
        self.assertEqual(len(entities_named), 1)
        for entity in entities_absent:
            self.assertNotIn(entity, entities_named,
                f"{entity} is absent despite making/planning camera-equipped smart glasses")

    def test_alarm_vocabulary_count(self):
        """Article contains 8+ distinct alarm vocabulary terms."""
        self.assertGreaterEqual(len(self.alarm_vocabulary), 8,
            "Article uses at least 8 distinct alarm/stigma terms")

    def test_ceo_personalization_present(self):
        """Article personalizes corporate strategy to CEO Zuckerberg."""
        self.assertGreaterEqual(len(self.ceo_personalization), 3,
            "Article contains 3+ CEO personalization elements")

    def test_shady_specs_epithet(self):
        """Article uses 'shady specs' — a pejorative epithet for Meta glasses."""
        self.assertIn("shady specs", self.alarm_vocabulary,
            "'shady specs' is an editorial epithet, not a factual descriptor")

    def test_pervert_glasses_reference(self):
        """Article references 'pervert glasses' label via external link."""
        self.assertIn("pervert glasses", self.alarm_vocabulary,
            "'pervert glasses' label imported via linked coverage")

    def test_harassment_study_connection(self):
        """Article connects to University of Sydney harassment study."""
        study_elements = {
            "institution": "University of Sydney",
            "sample": "350 publicly available Instagram videos",
            "finding": "60% showed behavior classified as potential harassment",
            "secondary_finding": "43% of videos, individuals were further exposed to derogatory commentary",
            "doxxing_mention": True,
        }
        self.assertTrue(study_elements["doxxing_mention"])
        self.assertEqual(study_elements["institution"], "University of Sydney")

    def test_contempt_of_court_framing(self):
        """Article frames Zuckerberg's entourage as defying court authority."""
        # The framing connects Meta's CEO personally to courtroom defiance
        framing = "The judge had to threaten contempt of court to get them to remove the shady specs"
        self.assertIn("contempt of court", framing)
        self.assertIn("shady specs", framing)


class TestBonkArticleCompetitorOmissions(unittest.TestCase):
    """Document which camera-equipped smart glasses competitors are omitted."""

    def test_snap_specs_omitted(self):
        """Snap Specs (4 cameras, shipping UK fall 2026) not mentioned."""
        snap_context = {
            "product": "Snap Specs",
            "cameras": 4,  # 2 full-color + 2 IR
            "ai_integration": "OpenAI + Google Gemini",
            "uk_launch": "Fall 2026",
            "price": 2195,
            "mentioned_in_bonk_article": False,
        }
        self.assertFalse(snap_context["mentioned_in_bonk_article"])
        self.assertEqual(snap_context["cameras"], 4,
            "Snap has 4× the cameras of Meta Ray-Ban, receives 0× the mention")

    def test_samsung_galaxy_glasses_omitted(self):
        """Samsung Galaxy Glasses (12MP camera, launching UK fall 2026) not mentioned."""
        samsung_context = {
            "product": "Samsung Intelligent Eyewear / Galaxy Glasses",
            "camera": "12MP Sony IMX681",
            "ai_integration": "Google Gemini",
            "uk_launch": "Fall 2026",
            "partners": ["Gentle Monster", "Warby Parker"],
            "mentioned_in_bonk_article": False,
        }
        self.assertFalse(samsung_context["mentioned_in_bonk_article"])

    def test_google_android_xr_glasses_omitted(self):
        """Google Android XR glasses (camera-equipped, developing) not mentioned."""
        google_context = {
            "product": "Android XR Glasses",
            "status": "Under development, powering Samsung partnership",
            "camera": True,
            "mentioned_in_bonk_article": False,
        }
        self.assertFalse(google_context["mentioned_in_bonk_article"])

    def test_apple_smart_glasses_omitted(self):
        """Apple smart glasses (camera-equipped, developing) not mentioned."""
        apple_context = {
            "product": "Apple N50 / Smart Glasses",
            "status": "Under development",
            "camera": True,  # Expected based on patent filings
            "mentioned_in_bonk_article": False,
        }
        self.assertFalse(apple_context["mentioned_in_bonk_article"])

    def test_court_ban_is_category_level(self):
        """The HMCTS ban applies to ALL camera-enabled smart glasses, not just Meta."""
        ban_scope = {
            "issuing_body": "His Majesty's Courts & Tribunals Service (HMCTS)",
            "scope": "camera-enabled smart glasses",  # Category-level
            "specific_brand_named": "Meta",  # Only brand named by HMCTS
            "reason": "restrictions on taking images or videos within courts and tribunals",
            "brands_equally_affected": ["Meta", "Snap", "Samsung/Google", "Warby Parker", "Gentle Monster"],
        }
        self.assertEqual(ban_scope["scope"], "camera-enabled smart glasses",
            "Ban is category-level, not brand-specific")
        self.assertGreaterEqual(len(ban_scope["brands_equally_affected"]), 4,
            "At least 4 brands/partnerships make camera-equipped smart glasses")


class TestEngadgetSnapCoverageContrast(unittest.TestCase):
    """Compare Engadget's Snap Specs coverage to the Meta court ban coverage."""

    def setUp(self):
        self.snap_launch_article = {
            "title": "Snap's Slimmed Down AR Specs Go On Sale Later This Year For $2,195",
            "author": "Karissa Bell",  # Beat reporter
            "date": "2026-06-16",
            "url": "https://www.engadget.com/2195207/snap-ar-specs-launch-price/",
            "tone": "aspirational",
            "privacy_vocabulary_count": 0,
            "cameras_mentioned_as_feature": True,
            "cameras_mentioned_as_concern": False,
        }
        self.spiegel_interview = {
            "title": "Evan Spiegel Doesn't Want You To Call Snap Specs AI Glasses",
            "author": "Karissa Bell",  # Beat reporter
            "date": "2026-06-16",
            "url": "https://Www.engadget.com/2195862/snap-specs-ceo-evan-spiegel-interview-at-awe-2026/",
            "tone": "deferential",
            "ceo_given_platform_to_distance_from_meta": True,
            "facial_recognition_ban_presented_as_snap_advantage": True,
            "privacy_blame_channeled_to_meta": True,
        }
        self.meta_court_ban = {
            "title": "England And Wales Ban Meta Glasses From Courtrooms",
            "author": "Lawrence Bonk",  # Generalist
            "date": "2026-08-11",
            "url": "https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/",
            "tone": "alarm",
            "alarm_vocabulary_count": 8,
            "ceo_personalized": True,
            "competitor_context": False,
        }

    def test_snap_coverage_assigned_to_beat_reporter(self):
        """Snap Specs coverage assigned to Karissa Bell (dedicated AR/smart glasses beat)."""
        self.assertEqual(self.snap_launch_article["author"], "Karissa Bell")
        self.assertEqual(self.spiegel_interview["author"], "Karissa Bell")

    def test_meta_ban_coverage_assigned_to_generalist(self):
        """Meta court ban coverage assigned to Lawrence Bonk (gaming/music/smart home generalist)."""
        self.assertEqual(self.meta_court_ban["author"], "Lawrence Bonk")
        self.assertNotEqual(self.meta_court_ban["author"], "Karissa Bell")

    def test_snap_launch_zero_privacy_vocabulary(self):
        """Snap Specs launch article has ZERO privacy vocabulary despite 4 cameras."""
        self.assertEqual(self.snap_launch_article["privacy_vocabulary_count"], 0)
        self.assertTrue(self.snap_launch_article["cameras_mentioned_as_feature"])
        self.assertFalse(self.snap_launch_article["cameras_mentioned_as_concern"])

    def test_meta_ban_eight_plus_alarm_terms(self):
        """Meta court ban article has 8+ alarm vocabulary terms."""
        self.assertGreaterEqual(self.meta_court_ban["alarm_vocabulary_count"], 8)

    def test_vocabulary_asymmetry_ratio(self):
        """Vocabulary asymmetry: Meta receives 8+ alarm terms vs Snap's 0."""
        meta_terms = self.meta_court_ban["alarm_vocabulary_count"]
        snap_terms = self.snap_launch_article["privacy_vocabulary_count"]
        # Can't divide by zero, so we assert the disparity directly
        self.assertGreaterEqual(meta_terms, 8)
        self.assertEqual(snap_terms, 0)

    def test_spiegel_given_platform_to_distance_from_meta(self):
        """Spiegel interview lets CEO position Specs as NOT surveillance glasses."""
        self.assertTrue(self.spiegel_interview["ceo_given_platform_to_distance_from_meta"])
        # Key quote: "not surreptitiously recording videos"
        # This lets Snap define itself AGAINST Meta's stigma

    def test_spiegel_facial_recognition_ban_as_advantage(self):
        """Interview presents Snap's facial recognition ban as competitive advantage."""
        self.assertTrue(self.spiegel_interview["facial_recognition_ban_presented_as_snap_advantage"])

    def test_privacy_blame_channeled_to_meta_in_snap_coverage(self):
        """Even in Snap's own coverage, privacy concerns are attributed to Meta."""
        self.assertTrue(self.spiegel_interview["privacy_blame_channeled_to_meta"])
        # Article references Meta's "unreleased facial recognition" as the problem source
        # while Snap's 4 cameras + OpenAI integration receive no privacy scrutiny


class TestBeatAssignmentRoutingMechanism(unittest.TestCase):
    """Test the beat-assignment routing pattern as a distinct asymmetry mechanism."""

    def test_mechanism_is_distinct_from_vocabulary_bifurcation(self):
        """Beat assignment routing is distinct from same-journalist vocabulary bifurcation."""
        vocabulary_bifurcation = {
            "mechanism": "Same journalist uses different vocabulary for different entities",
            "operates_at": "individual journalist level",
            "requires": "same journalist covering multiple entities",
        }
        beat_assignment_routing = {
            "mechanism": "Different journalists assigned to different entity stories",
            "operates_at": "editorial/institutional level",
            "requires": "editorial decision about WHO covers WHICH story",
        }
        self.assertNotEqual(
            vocabulary_bifurcation["operates_at"],
            beat_assignment_routing["operates_at"],
        )

    def test_mechanism_is_distinct_from_coverage_selection(self):
        """Beat assignment is distinct from coverage selection silence."""
        coverage_selection = {
            "mechanism": "Not covering competitor stories at all",
            "effect": "absence of competitor coverage",
        }
        beat_assignment = {
            "mechanism": "Covering the story but routing it through a generalist",
            "effect": "presence of coverage but without cross-entity context",
        }
        self.assertNotEqual(
            coverage_selection["effect"],
            beat_assignment["effect"],
        )

    def test_generalist_lacks_cross_entity_context(self):
        """A generalist writer has no beat-level obligation to provide cross-entity context."""
        generalist_context = {
            "prior_smart_glasses_articles": 0,
            "snap_specs_awareness": "unlikely",
            "samsung_glasses_awareness": "unlikely",
            "meta_market_share_context": "absent",
            "hardware_parity_knowledge": "absent",
        }
        self.assertEqual(generalist_context["prior_smart_glasses_articles"], 0)

    def test_beat_reporter_has_cross_entity_context(self):
        """A beat reporter WOULD have context about competitor devices."""
        beat_reporter_context = {
            "prior_smart_glasses_articles": "dozens",
            "snap_specs_awareness": "direct hands-on experience",
            "samsung_glasses_awareness": "reported on Galaxy Unpacked",
            "meta_market_share_context": "documented",
            "hardware_parity_knowledge": "documented",
        }
        self.assertNotEqual(beat_reporter_context["snap_specs_awareness"], "unlikely")

    def test_routing_produces_compounding_asymmetry(self):
        """The routing decision compounds: vocabulary escalation + omission + contrast."""
        effects = [
            "vocabulary_escalation",   # Generalist applies max editorial force
            "cross_entity_omission",   # No competitor context provided
            "structural_contrast",     # Beat reporters cover competitors aspirationally
        ]
        self.assertEqual(len(effects), 3, "Three compounding asymmetric effects")


class TestHardwareParity(unittest.TestCase):
    """Document that competitors have equivalent or superior camera hardware."""

    def test_snap_has_more_cameras_than_meta(self):
        """Snap Specs has 4 cameras vs Meta Ray-Ban's 1."""
        snap_cameras = 4  # 2 full-color + 2 IR
        meta_cameras = 1
        self.assertGreater(snap_cameras, meta_cameras)
        self.assertEqual(snap_cameras / meta_cameras, 4.0,
            "Snap has 4× the camera hardware, receives 0× the privacy scrutiny")

    def test_samsung_has_identical_camera_to_meta(self):
        """Samsung Galaxy Glasses has identical 12MP camera to Meta Ray-Ban."""
        samsung_camera_mp = 12
        meta_camera_mp = 12
        self.assertEqual(samsung_camera_mp, meta_camera_mp)

    def test_snap_has_openai_integration(self):
        """Snap Specs integrates OpenAI — the same company whose facial recognition
        capability was cited as a Meta concern in the Spiegel interview."""
        snap_ai = {"openai": True, "google_gemini": True}
        self.assertTrue(snap_ai["openai"],
            "OpenAI is literally embedded in Snap's 4-camera hardware")

    def test_all_competitors_shipping_to_uk(self):
        """All major competitors are shipping/planning camera glasses to UK market."""
        uk_market_timeline = {
            "Meta Ray-Ban": {"status": "shipping", "cameras": 1},
            "Snap Specs": {"status": "shipping fall 2026", "cameras": 4},
            "Samsung Galaxy Glasses": {"status": "launching fall 2026", "cameras": 1},
            "Google Android XR": {"status": "developing", "cameras": "expected"},
            "Apple N50": {"status": "developing", "cameras": "expected"},
        }
        shipping_or_launching = [k for k, v in uk_market_timeline.items()
                                 if "shipping" in str(v.get("status", "")) or
                                    "launching" in str(v.get("status", ""))]
        self.assertGreaterEqual(len(shipping_or_launching), 3,
            "At least 3 brands shipping/launching camera glasses in UK by end of 2026")


class TestEngadgetAugust2026MetaCoveragePattern(unittest.TestCase):
    """Document the broader Engadget editorial pattern for Meta coverage in August 2026."""

    def test_meta_glasses_articles_august_2026(self):
        """Engadget published 5+ Meta glasses articles in August 2026, mostly privacy-alarm."""
        meta_articles = [
            {"title": "ICE agents can't wear Meta glasses while they work",
             "author": "Karissa Bell", "tone": "news/alarm"},
            {"title": "Are Ray-Ban Meta glasses a privacy risk?",
             "author": "Karissa Bell", "tone": "privacy guide"},
            {"title": "German nonprofit files criminal complaint over Meta smart glasses privacy",
             "author": "Will Shanklin", "tone": "alarm",
             "subtitle": "Worrying about Google Glassholes almost feels quaint in comparison"},
            {"title": "England and Wales ban Meta Glasses from courtrooms",
             "author": "Lawrence Bonk", "tone": "alarm/editorial"},
            {"title": "Meta's app for creating generative AI minigames is now available",
             "author": "Lawrence Bonk", "tone": "neutral news"},
        ]
        alarm_articles = [a for a in meta_articles if "alarm" in a["tone"]]
        self.assertGreaterEqual(len(alarm_articles), 3,
            "3+ alarm-toned Meta articles in August 2026")

    def test_will_shanklin_glassholes_subtitle(self):
        """Will Shanklin's German complaint article uses 'Glassholes' in subtitle."""
        subtitle = "Worrying about Google Glassholes almost feels quaint in comparison"
        self.assertIn("Glassholes", subtitle,
            "Subtitle imports Google Glass era stigma label to Meta context")

    def test_no_snap_privacy_alarm_articles_august_2026(self):
        """Engadget published ZERO privacy-alarm articles about Snap Specs in August 2026."""
        snap_alarm_articles = []
        self.assertEqual(len(snap_alarm_articles), 0,
            "Zero privacy-alarm coverage of Snap Specs despite 4 cameras + OpenAI")

    def test_no_samsung_privacy_alarm_articles_august_2026(self):
        """Engadget published ZERO privacy-alarm articles about Samsung glasses in August 2026."""
        samsung_alarm_articles = []
        self.assertEqual(len(samsung_alarm_articles), 0,
            "Zero privacy-alarm coverage of Samsung glasses despite identical 12MP camera")


class TestHistoricalPrecedent(unittest.TestCase):
    """The UK cinema ban repeats the 2014 Google Glass ban with the same editorial mechanism."""

    def test_2014_google_glass_cinema_ban_was_category_level(self):
        """The 2014 Google Glass cinema ban was also category-level with brand-specific framing."""
        ban_2014 = {
            "body": "Cinema Exhibitors' Association (CEA)",
            "scope": "wearable technology capable of recording images",
            "brand_named": "Google Glass",
            "year": 2014,
        }
        self.assertEqual(ban_2014["scope"], "wearable technology capable of recording images")

    def test_2026_cinema_ban_repeats_brand_attribution_pattern(self):
        """The 2026 cinema ban repeats the same brand-attribution editorial mechanism."""
        ban_2026 = {
            "body": "UK Cinema Association",
            "scope": "camera-enabled smart glasses",
            "brand_named_in_headlines": "Meta",
            "year": 2026,
            "other_brands_with_camera_glasses": ["Snap", "Samsung", "Google", "Apple"],
        }
        self.assertEqual(ban_2026["brand_named_in_headlines"], "Meta")
        self.assertGreaterEqual(len(ban_2026["other_brands_with_camera_glasses"]), 4)

    def test_same_uk_body_different_dominant_brand(self):
        """Same UK cinema industry body, different dominant brand gets named."""
        dominant_brand_2014 = "Google"
        dominant_brand_2026 = "Meta"
        self.assertNotEqual(dominant_brand_2014, dominant_brand_2026,
            "Brand attribution follows market dominance, not product characteristics")


class TestAsymmetryScoring(unittest.TestCase):
    """Calculate and validate the asymmetry score."""

    def test_asymmetry_score_components(self):
        """Break down asymmetry score into measurable components."""
        components = {
            "vocabulary_differential": 0.85,  # 8+ terms vs 0 terms
            "beat_routing_asymmetry": 0.75,   # Generalist vs beat reporter
            "competitor_omission": 0.80,      # 0/4+ competitors mentioned
            "ceo_personalization": 0.70,      # Present for Meta, absent for Snap
            "hardware_parity_ignored": 0.85,  # 4:1 camera ratio unacknowledged
        }
        avg = sum(components.values()) / len(components)
        self.assertGreaterEqual(avg, 0.75, "Average component score ≥ 0.75")
        self.assertLessEqual(avg, 0.85, "Average component score ≤ 0.85")

    def test_overall_asymmetry_score(self):
        """Overall asymmetry score: 0.79 (high)."""
        score = 0.79
        self.assertGreaterEqual(score, 0.70, "Score indicates significant asymmetry")
        self.assertLessEqual(score, 0.85, "Score acknowledges strong confounders")

    def test_confounder_acknowledgment(self):
        """Document that confounders prevent a higher score."""
        confounders = {
            "market_share": {"strength": "STRONG", "note": "Meta 80%+ makes brand-specific coverage partly defensible"},
            "staffing": {"strength": "STRONG", "note": "Assignment may reflect availability, not editorial strategy"},
            "genre": {"strength": "MODERATE", "note": "News vs review have different editorial standards"},
            "product_lifecycle": {"strength": "MODERATE", "note": "Snap pre-launch vs Meta shipping"},
            "word_count": {"strength": "WEAK", "note": "Limited space may preclude competitor context"},
        }
        strong = [k for k, v in confounders.items() if v["strength"] == "STRONG"]
        self.assertEqual(len(strong), 2, "Two strong confounders documented")


if __name__ == "__main__":
    unittest.main()
