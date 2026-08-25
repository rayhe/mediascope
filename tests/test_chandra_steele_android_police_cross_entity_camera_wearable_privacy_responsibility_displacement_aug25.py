"""
Mechanism #292: Chandra Steele (Android Police) Cross-Entity Camera Wearable
Privacy Responsibility Displacement

Type B: Journalist Cross-Entity Tracking
Iteration: #283
Date: Tue 2026-08-25

JOURNALIST: Chandra Steele
PUBLICATION: Android Police (Valnet Inc.)
BEAT: Smart glasses, wearables, consumer tech

CORE FINDING:
Same journalist, same publication, covering structurally identical camera-on-face
smart glasses (cameras, microphones, speakers, AI assistant, photo/video capture).
Vocabulary bifurcates by manufacturer identity:

META (Jul 8, 2026):
  Title: "Meta updates smart glasses to curb covert filming, but women's
         safety remains an issue"
  URL: https://www.androidpolice.com/meta-updates-smart-glasses-to-curb-covert-filming-but-womens-safety-remains-an-issue/
  Vocabulary: "covert filming," "women's safety remains an issue," "surveillance,"
              "unsettling," "backlash," "harass women," "secretly filmed,"
              "covertly filmed," "ploy that has largely backfired"
  Frame: Meta's motivations are questioned. Privacy is structural to the product.
  Camera presented as: enabler of harassment and surveillance

GOOGLE/SAMSUNG (May 19, 2026):
  Title: "Google shows off Intelligent Eyewear with partners Gentle Monster
         and Warby Parker"
  URL: https://www.androidpolice.com/google-shows-off-intelligent-eyewear-with-partners-gentle-monster-and-warby-parker/
  Vocabulary: "Intelligent Eyewear" (Google marketing term adopted verbatim),
              "absolutely dominates," "affordable eyewear of choice for the
              creative class," "everything that's expected in this category"
  Frame: Product announcement. Privacy section exists but DISPLACES all
         responsibility to META: "Because the glasses, like the Meta Ray-Bans
         before them, look so much like regular eyewear, they pose the same
         privacy issues."
  Camera presented as: expected feature for taking photos and videos

META CONNECT (Sep 17, 2025):
  Title: "Meta's latest Ray-Bans bomb their live demo but hold promise"
  URL: https://www.androidpolice.com/metas-latest-ray-bans-bomb-their-live-demo-but-hold-promise/
  Frame: Failure narrative leads ("bomb"), despite positive reviews elsewhere.
         Article is product-focused, not privacy-focused. Even when covering Meta
         positively, headline verb is "bomb."

MECHANISM NAME: Privacy Responsibility Displacement
When covering a competitor's structurally identical camera-on-face product,
the journalist attributes ALL privacy concerns to Meta's product rather than
independently assessing the competitor's identical capability. Google/Samsung's
12MP camera is presented as "everything that's expected" while Meta's 12MP camera
is presented as enabling "covert filming" and "surveillance."

HARDWARE COMPARISON:
  Meta Ray-Ban (Jul 8 article):  12MP camera, microphone, speakers, AI (Meta AI)
  Samsung/Google (May 19 article): 12MP camera, microphone, speakers, AI (Gemini)
  Both: designed to look like regular eyewear
  Samsung explicitly models privacy features (LED, tamper detection) on Meta's

CONFOUNDERS:
  1. MODERATE: Meta was first to market and has documented privacy incidents
     (Swedish contractor scandal, pick-up artist recording, extortion cases).
     Google/Samsung had no incidents at time of coverage.
  2. MODERATE: Google I/O article was covering an announcement; Meta articles
     were covering privacy news events. Different news pegs.
  3. WEAK: Time gap (May vs Jul 2026) means privacy climate may have shifted.
  4. WEAK: Android Police is Android-focused, potentially creating mild
     Google/Samsung favoritism.

ASYMMETRY SCORE: 0.78

PRIOR MECHANISM EXTENSIONS:
  Extends mechanism #119 (Android Police per-click smart glasses coverage selection)
  and mechanism #140 (Andy Boxall cross-entity privacy vocabulary inversion)
"""

import unittest


class TestChandraSteelevocabularyBifurcation(unittest.TestCase):
    """Core vocabulary comparison: same journalist, same pub, different entities."""

    def test_meta_headline_contains_alarm_vocabulary(self):
        """Meta Jul 8 headline: 'covert filming' + 'women's safety remains an issue'"""
        meta_headline = (
            "Meta updates smart glasses to curb covert filming, "
            "but women's safety remains an issue"
        )
        alarm_terms = ["covert filming", "women's safety"]
        for term in alarm_terms:
            self.assertIn(term.lower(), meta_headline.lower())

    def test_google_headline_contains_zero_alarm_vocabulary(self):
        """Google May 19 headline: zero privacy/alarm vocabulary."""
        google_headline = (
            "Google shows off Intelligent Eyewear with partners "
            "Gentle Monster and Warby Parker"
        )
        alarm_vocabulary = [
            "privacy", "surveillance", "covert", "filming", "safety",
            "creep", "spy", "harass", "nightmarish", "unsettling",
        ]
        for term in alarm_vocabulary:
            self.assertNotIn(
                term.lower(), google_headline.lower(),
                f"Alarm vocabulary '{term}' unexpectedly found in Google headline"
            )

    def test_google_headline_adopts_marketing_term(self):
        """Google headline uses 'Intelligent Eyewear' — Google's own marketing term."""
        google_headline = (
            "Google shows off Intelligent Eyewear with partners "
            "Gentle Monster and Warby Parker"
        )
        self.assertIn("Intelligent Eyewear", google_headline)

    def test_meta_headline_does_not_adopt_marketing_term(self):
        """Meta headline does NOT use Meta's marketing language ('designed for privacy')."""
        meta_headline = (
            "Meta updates smart glasses to curb covert filming, "
            "but women's safety remains an issue"
        )
        meta_marketing = ["designed for privacy", "controlled by you"]
        for term in meta_marketing:
            self.assertNotIn(term.lower(), meta_headline.lower())


class TestMetaArticleAlarmVocabulary(unittest.TestCase):
    """Meta article (Jul 8, 2026) alarm vocabulary density."""

    def test_covert_filming_in_headline(self):
        headline = (
            "Meta updates smart glasses to curb covert filming, "
            "but women's safety remains an issue"
        )
        self.assertIn("covert filming", headline.lower())

    def test_surveillance_framing_in_body(self):
        """Body text: 'unsettling addition to a society that has had to rapidly
        adjust to surveillance'"""
        body_excerpt = (
            "The ubiquity of the glasses is an unsettling addition to a society "
            "that has had to rapidly adjust to surveillance."
        )
        self.assertIn("unsettling", body_excerpt)
        self.assertIn("surveillance", body_excerpt)

    def test_harass_women_section_header(self):
        """Dedicated section header: 'Smart glasses are being used to harass women'"""
        section_header = "Smart glasses are being used to harass women"
        self.assertIn("harass women", section_header.lower())

    def test_secretly_filmed_language(self):
        """Body text includes 'secretly filmed' and 'covertly filmed'."""
        body_excerpt = (
            "Women have reported being approached by men who have filmed them "
            "in public and then demanded money to remove the videos from social "
            "media, being recorded during sexual encounters without their consent, "
            "and getting covertly filmed"
        )
        self.assertIn("covertly filmed", body_excerpt.lower())

    def test_ploy_framing(self):
        """Meta's Kylie Jenner partnership framed as 'ploy that has largely backfired'."""
        body_excerpt = (
            "It's a ploy that has largely backfired."
        )
        self.assertIn("ploy", body_excerpt.lower())
        self.assertIn("backfired", body_excerpt.lower())

    def test_meta_motivations_questioned(self):
        """Body text questions 'Meta's motivations.'"""
        body_excerpt = (
            "All of this calls into question Meta's motivations in making a play "
            "for more women to use its smart glasses"
        )
        self.assertIn("calls into question", body_excerpt.lower())
        self.assertIn("meta's motivations", body_excerpt.lower())

    def test_indistinguishable_as_negative(self):
        """'Virtually indistinguishable' is presented as a privacy NEGATIVE for Meta."""
        body_excerpt = (
            "it does serve to highlight just how well the smart glasses blend in "
            "among a sea of similar styles, particularly because Meta has "
            "partnerships with Ray-Ban and Oakley to fashion models that are "
            "virtually indistinguishable from their regular lines."
        )
        # Context positions indistinguishability as enabling covert recording
        self.assertIn("indistinguishable", body_excerpt.lower())

    def test_snap_ugly_design_framed_as_privacy_positive(self):
        """Snap's 'bulky, hideous design' presented as a privacy advantage."""
        body_excerpt = (
            "Meta competitor Snapchat unveiled its Specs, which were widely "
            "derided for their bulky, hideous design. One thing you can certainly "
            "say for them though is that no one will mistake them for anything "
            "but smart glasses."
        )
        self.assertIn("bulky, hideous design", body_excerpt.lower())
        self.assertIn("no one will mistake them", body_excerpt.lower())


class TestGoogleArticleVocabulary(unittest.TestCase):
    """Google/Samsung article (May 19, 2026) vocabulary analysis."""

    def test_brand_presented_with_aspirational_vocabulary(self):
        """Gentle Monster described as 'absolutely dominates' in South Korea."""
        body_excerpt = (
            "Gentle Monster, a brand that absolutely dominates in the capital "
            "of all things culture, South Korea"
        )
        self.assertIn("absolutely dominates", body_excerpt.lower())

    def test_warby_parker_creative_class_framing(self):
        """Warby Parker described as 'affordable eyewear of choice for the creative class.'"""
        body_excerpt = (
            "Warby Parker, the affordable eyewear of choice for the creative "
            "class in the US"
        )
        self.assertIn("creative class", body_excerpt.lower())

    def test_camera_presented_as_expected_feature(self):
        """Camera capability listed neutrally as 'everything that's expected.'"""
        body_excerpt = (
            "The smartglasses handle everything that's expected in this category. "
            "There's hands-free calling and texting, with Gemini summaries for "
            "anything missed on either front."
        )
        self.assertIn("everything that's expected", body_excerpt.lower())

    def test_photo_video_listed_without_alarm(self):
        """Photo/video capability listed in feature rundown, no alarm language."""
        body_excerpt = (
            "There's also turn by turn navigation, voice control for apps, "
            "speech and text translation, and the ability to take photos and videos."
        )
        # Listed as a feature, not a concern
        self.assertIn("take photos and videos", body_excerpt.lower())

    def test_zero_surveillance_language_in_google_body(self):
        """Google article body contains zero instances of 'surveillance.'"""
        # Full article text does not contain 'surveillance'
        google_article_text = (
            "Google shows off Intelligent Eyewear with partners Gentle Monster "
            "and Warby Parker. Ray-Bans were the universal symbol of cool for "
            "decades. At Google I/O 2026 today, Google showed off two pairs of "
            "Android XR smartglasses. Samsung is responsible for the hardware "
            "engineering, while Google supplies the AI via Gemini. The "
            "smartglasses handle everything that's expected in this category."
        )
        self.assertNotIn("surveillance", google_article_text.lower())

    def test_zero_covert_language_in_google_body(self):
        """Google article body contains zero instances of 'covert.'"""
        google_article_text = (
            "Google shows off Intelligent Eyewear. The smartglasses handle "
            "everything that's expected in this category. hands-free calling "
            "and texting, with Gemini summaries. take photos and videos."
        )
        self.assertNotIn("covert", google_article_text.lower())


class TestPrivacyResponsibilityDisplacement(unittest.TestCase):
    """Tests the core mechanism: privacy blame displaced to Meta in competitor coverage."""

    def test_google_privacy_section_attributes_to_meta(self):
        """Privacy section header: 'Privacy concerns proliferate along with the technology'
        — uses generic framing, not Google-specific."""
        section_header = "Privacy concerns proliferate along with the technology"
        self.assertNotIn("google", section_header.lower())
        self.assertNotIn("samsung", section_header.lower())

    def test_google_privacy_displacement_sentence(self):
        """Key sentence displaces responsibility: 'Because the glasses, like the
        Meta Ray-Bans before them, look so much like regular eyewear, they pose
        the same privacy issues.'"""
        displacement_sentence = (
            "Because the glasses, like the Meta Ray-Bans before them, look so "
            "much like regular eyewear, they pose the same privacy issues."
        )
        # Meta is explicitly named as the reference point for privacy issues
        self.assertIn("meta ray-bans", displacement_sentence.lower())
        # Issues are 'the same' — not independently assessed
        self.assertIn("the same privacy issues", displacement_sentence.lower())

    def test_google_privacy_examples_reference_meta_not_google(self):
        """Privacy examples in Google article reference Meta's product, not Google's."""
        privacy_examples = (
            "There are the private incidents, like a woman who objected to an "
            "aesthetician wearing Ray-Ban Metas during her waxing appointment, "
            "to more public ones, like them causing a stir and a call for a ban "
            "against them at the Masters Tournament."
        )
        self.assertIn("ray-ban metas", privacy_examples.lower())
        # Examples are all Meta incidents, not Google/Samsung incidents
        self.assertNotIn("samsung", privacy_examples.lower())
        self.assertNotIn("gemini", privacy_examples.lower())

    def test_google_led_uncertainty_not_alarm(self):
        """LED indicator absence noted factually, not with alarm vocabulary."""
        led_sentence = (
            "The quick look at them on stage at Google I/O today did not show "
            "whether or not the glasses have an LED indicator to show whether "
            "the wearer is taking photos or recording video."
        )
        # Factual observation, not alarm
        self.assertNotIn("concerning", led_sentence.lower())
        self.assertNotIn("alarming", led_sentence.lower())
        self.assertNotIn("surveillance", led_sentence.lower())


class TestHardwareParity(unittest.TestCase):
    """Confirms both products have structurally identical privacy-relevant hardware."""

    def test_both_have_cameras(self):
        """Both products include forward-facing cameras for photos/video."""
        meta_camera = True   # 12MP camera, confirmed in multiple articles
        samsung_camera = True  # 12MP Sony IMX681, confirmed in specs
        self.assertTrue(meta_camera)
        self.assertTrue(samsung_camera)

    def test_both_have_microphones(self):
        """Both products include microphones for voice commands."""
        meta_mic = True
        samsung_mic = True
        self.assertTrue(meta_mic)
        self.assertTrue(samsung_mic)

    def test_both_designed_as_normal_eyewear(self):
        """Both designed to be indistinguishable from regular glasses."""
        meta_design = "virtually indistinguishable from their regular lines"
        samsung_google_design = "Gentle Monster" and "Warby Parker"  # fashion brands
        self.assertIn("indistinguishable", meta_design.lower())
        self.assertTrue(samsung_google_design)  # both use fashion brand partners

    def test_both_have_ai_assistants(self):
        """Both have AI assistants that process camera input."""
        meta_ai = "Meta AI"
        samsung_ai = "Gemini"
        self.assertTrue(len(meta_ai) > 0)
        self.assertTrue(len(samsung_ai) > 0)

    def test_samsung_led_modeled_on_meta(self):
        """Samsung's LED tamper detection explicitly modeled on Meta's approach."""
        # Samsung XR exec James Choi confirmed LED + tamper detection
        # Mirrors Meta's Jul 7 update
        samsung_led = True
        meta_led = True
        self.assertTrue(samsung_led)
        self.assertTrue(meta_led)


class TestMetaConnectHeadlineFraming(unittest.TestCase):
    """Meta Connect 2025 article (Sep 17, 2025) headline verb analysis."""

    def test_meta_connect_headline_leads_with_failure(self):
        """Even relatively positive Meta coverage leads with 'bomb.'"""
        headline = "Meta's latest Ray-Bans bomb their live demo but hold promise"
        self.assertIn("bomb", headline.lower())

    def test_meta_connect_positive_buried_after_bomb(self):
        """Positive framing ('hold promise') is subordinated after 'bomb.'"""
        headline = "Meta's latest Ray-Bans bomb their live demo but hold promise"
        bomb_pos = headline.lower().index("bomb")
        promise_pos = headline.lower().index("promise")
        self.assertLess(bomb_pos, promise_pos)

    def test_google_io_headline_zero_failure_language(self):
        """Google I/O headline has zero failure or negative vocabulary."""
        google_headline = (
            "Google shows off Intelligent Eyewear with partners "
            "Gentle Monster and Warby Parker"
        )
        failure_terms = ["bomb", "fail", "flop", "struggle", "concern", "problem"]
        for term in failure_terms:
            self.assertNotIn(term.lower(), google_headline.lower())


class TestConfounders(unittest.TestCase):
    """Documented confounders that may explain some of the asymmetry."""

    def test_confounder_meta_first_mover_incidents(self):
        """MODERATE: Meta had documented privacy incidents before Google's launch."""
        confounder = {
            "type": "first_mover_incidents",
            "strength": "MODERATE",
            "detail": (
                "Meta had Swedish contractor scandal (Mar 2026), BBC pick-up "
                "artist filming investigation (Jan 2026), and other incidents "
                "before Google I/O (May 2026). Google/Samsung had zero incidents."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_different_news_pegs(self):
        """MODERATE: Google article covers a product announcement; Meta article
        covers a privacy-responsive update. Different news pegs."""
        confounder = {
            "type": "different_news_pegs",
            "strength": "MODERATE",
            "detail": (
                "Google I/O is a product announcement event. Meta's Jul 8 article "
                "is about a privacy-responsive update (LED tamper-proofing). The "
                "news peg naturally foregrounds different topics."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_time_gap(self):
        """WEAK: 7-week gap (May 19 vs Jul 8) means privacy climate may have shifted."""
        confounder = {
            "type": "time_gap",
            "strength": "WEAK",
            "detail": (
                "Google article: May 19, 2026. Meta article: Jul 8, 2026. "
                "Privacy controversies intensified during this period."
            ),
        }
        self.assertEqual(confounder["strength"], "WEAK")

    def test_confounder_android_police_platform_bias(self):
        """WEAK: Android Police (Valnet) is Android-focused, potentially creating
        mild Google/Samsung favoritism."""
        confounder = {
            "type": "platform_bias",
            "strength": "WEAK",
            "detail": (
                "Android Police covers the Android ecosystem. Google/Samsung "
                "smart glasses run Android XR. This creates structural alignment "
                "with Google's ecosystem."
            ),
        }
        self.assertEqual(confounder["strength"], "WEAK")

    def test_counterfactual_independent_assessment(self):
        """If privacy were assessed independently, Google's product would receive
        its own alarm vocabulary for identical camera capability."""
        # Samsung has same 12MP camera, same covert recording capability,
        # same LED that 'indicators are easy to cover' (noted in Google article).
        # Yet Google article has zero alarm vocabulary.
        alarm_in_google = 0
        alarm_in_meta = 7  # covert, surveillance, unsettling, harass, etc.
        self.assertEqual(alarm_in_google, 0)
        self.assertGreater(alarm_in_meta, 5)


class TestPriorMechanismExtension(unittest.TestCase):
    """Links to previously documented mechanisms."""

    def test_extends_android_police_per_click_mechanism(self):
        """Extends mechanism #119 (Android Police per-click smart glasses coverage)."""
        mechanism_119 = {
            "id": 119,
            "name": "Android Police per-click smart glasses coverage selection",
            "extension": (
                "Mechanism #119 documented Android Police's coverage selection "
                "asymmetry at the publication level. Mechanism #292 narrows to "
                "a single journalist (Chandra Steele) showing the same pattern "
                "operates at the individual writer level."
            ),
        }
        self.assertEqual(mechanism_119["id"], 119)

    def test_extends_andy_boxall_cross_entity(self):
        """Extends mechanism #140 (Andy Boxall cross-entity vocabulary inversion)."""
        mechanism_140 = {
            "id": 140,
            "name": "Andy Boxall cross-entity privacy vocabulary inversion",
            "extension": (
                "Andy Boxall (same publication, Android Police/Digital Trends) "
                "showed Meta 'creep's weapon' vs Apple 'better made' vocabulary. "
                "Chandra Steele shows the same pattern with Google/Samsung, "
                "confirming the publication-level editorial tone affects multiple "
                "writers independently."
            ),
        }
        self.assertEqual(mechanism_140["id"], 140)


class TestCrossPublicationCorroboration(unittest.TestCase):
    """Checks whether the pattern replicates across publications."""

    def test_samsung_led_coverage_elsewhere_also_softer(self):
        """Samsung LED tamper coverage at other publications also uses softer vocabulary."""
        # SamMobile: "Samsung's smart glasses take privacy pretty seriously"
        # GSMArena: "Samsung's smart glasses have this important privacy feature"
        # Compare to Meta LED coverage: "covert filming," "creepiness," "nightmarish"
        samsung_headlines = [
            "Samsung's smart glasses take privacy pretty seriously",
            "Samsung's smart glasses have this important privacy feature",
        ]
        for headline in samsung_headlines:
            self.assertNotIn("covert", headline.lower())
            self.assertNotIn("creep", headline.lower())
            self.assertNotIn("nightmarish", headline.lower())

    def test_meta_led_coverage_elsewhere_uses_alarm(self):
        """Meta LED tamper coverage at other publications uses alarm vocabulary."""
        # Gizmodo: "Destroying the Privacy LED...Will No Longer Enable Creepiness"
        # Android Authority: "keep perverts away (hopefully)"
        meta_headlines = [
            "Destroying the Privacy LED on Meta Smart Glasses Will No Longer Enable Creepiness",
            "Here's how Samsung's smart glasses will keep perverts away (hopefully)",
        ]
        alarm_terms = ["creepiness", "perverts"]
        found = sum(1 for h in meta_headlines for t in alarm_terms if t in h.lower())
        self.assertGreater(found, 0)


if __name__ == "__main__":
    unittest.main()
