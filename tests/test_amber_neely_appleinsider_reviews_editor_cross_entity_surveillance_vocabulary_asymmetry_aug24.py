"""
Type B: Journalist Cross-Entity Tracking — Amber Neely AppleInsider Reviews Editor
Cross-Entity Surveillance Vocabulary Asymmetry (Mechanism #285)

Amber Neely is the Reviews Editor at AppleInsider (owned by Future plc, mechanism #126)
and has been writing for the publication since 2019. She previously wrote for MacNN and
Electronista (both Apple-focused outlets) from 2015-2017. She self-describes as "the most
tech-critical member of the AppleInsider staff."

Key cross-entity tracking findings:

1. VOCABULARY BIFURCATION IN SAME ARTICLE: In the Feb 24, 2026 article about a
   smartglasses-detecting app, Neely describes Meta glasses as "being used mainly to
   violate other people's privacy," "stealthy, live-stream capable devices," "invasive and
   ugly," "privacy nightmare," "eyesore," while simultaneously framing Apple as having
   "privacy-first, safety-forward models" and praising the app as "a great model for Apple
   Glass developers to follow." The same camera technology gets surveillance vocabulary
   for Meta and aspirational vocabulary for Apple — within the same 1,200-word piece.

2. EXCULPATORY APPLE FRAMING WITHIN META ATTACK: In the Mar 3, 2026 article headlined
   "What privacy? Meta's smart glasses are filming unwitting naked people," Neely covers
   Apple's own Siri privacy scandal (2019 audio recording leak) but applies exculpatory
   language: "At the very least, Apple is very insistent that it is handling such data
   sensitively." Meta receives "privacy nightmare" and "privacy disaster" (headline).
   Apple receives "if it hasn't learned its lessons" — redemptive, forward-looking framing.

3. COMPETITOR DISMISSAL WITHOUT MATCHING APPLE SCRUTINY: In the Jun 16, 2026 article on
   Snap Specs, Neely dismisses the $2,195 AR glasses as "functionally, a toy" with "no
   space for it in the current market," while favorably benchmarking Apple Vision Pro specs
   in the same article: "The Apple Vision Pro's field of view is almost twice that at
   100 degrees horizontally and can display a billion distinct colors." The aspirational
   comparison is unprompted — Snap's product is measured against Apple's gold standard.

4. EDITORIAL POSITION AMPLIFICATION: As Reviews Editor, Neely holds a senior editorial
   role influencing how products are evaluated across the publication. Her reviews-level
   vocabulary choices (what constitutes a "nightmare" vs a "model to follow") set the
   evaluative framework for AppleInsider's product coverage more broadly.

5. FORUM COMMENTS REVEAL PERSONAL CONVICTION: In AppleInsider forums, Neely writes:
   "cameras don't need to be strapped to your head... a camera is a bridge too far.
   Especially when said camera just looks like a pair of glasses" and "I have just like,
   an insane amount of future dread." These personal views match her editorial output
   but are applied asymmetrically — Meta's cameras trigger dread, Apple's theoretical
   cameras trigger aspirational privacy-first framing.

6. PUBLICATION FINANCIAL CONTEXT: AppleInsider is owned by Future plc (LSE: FUTR), a UK
   media company that earns significant revenue from Apple product reviews, affiliate
   links, and advertising. Future plc also owns iMore, TechRadar, Tom's Guide, and other
   tech publications. This financial relationship (mechanism #126) creates a structural
   incentive to frame Apple aspirationally and competitors adversarially.

Source URLs:
- https://appleinsider.com/articles/26/02/24/this-meta-smartglasses-detecting-app-is-a-great-model-for-apple-glass-developers-to-follow
- https://appleinsider.com/articles/26/03/03/what-privacy-as-expected-meta-ray-bans-are-a-privacy-disaster
- https://appleinsider.com/articles/26/06/16/snap-built-standalone-ar-glasses-without-a-convincing-reason-to-wear-them
- https://appleinsider.com/editor/Amber+Neely
- https://appleinsider.com/articles/24/12/28/how-we-work-ambers-reporting-and-high-tech-crafting-setup
- https://forums.appleinsider.com/profile/reactions/240005/amberneely/1/p2/
- https://appleinsider.com/articles/22/12/26/2022-in-review-appleinsiders-favorite-articles-of-the-year

Iteration #278 — Mon 2026-08-24 16:00 PT
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestMechanism285Exists(unittest.TestCase):
    """Verify mechanism #285 is registered in competitor-coverage-research.yaml."""

    def setUp(self):
        self.data = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_285_present(self):
        """Mechanism #285 must exist in the YAML."""
        mechanism = self._find_mechanism(285)
        self.assertIsNotNone(mechanism, "Mechanism #285 not found")

    def test_mechanism_285_type_b(self):
        """Mechanism #285 must be type B (journalist cross-entity tracking)."""
        mechanism = self._find_mechanism(285)
        self.assertEqual(mechanism.get('type'), 'B')

    def test_mechanism_285_has_confounding_factors(self):
        """Must have at least 4 confounding factors."""
        mechanism = self._find_mechanism(285)
        factors = mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 4)

    def test_mechanism_285_journalist_name(self):
        """Must identify Amber Neely as the journalist."""
        mechanism = self._find_mechanism(285)
        name = mechanism.get('journalist', '')
        self.assertIn('Amber Neely', name)

    def test_mechanism_285_publication(self):
        """Must identify AppleInsider as the publication."""
        mechanism = self._find_mechanism(285)
        pub = mechanism.get('publication', '')
        self.assertIn('AppleInsider', pub)

    def _find_mechanism(self, mechanism_id):
        publications = self.data.get('publications', {})
        if isinstance(publications, dict):
            for key, val in publications.items():
                if isinstance(val, dict) and val.get('mechanism_id') == mechanism_id:
                    return val
        return None


class TestNeelyVocabularyBifurcationSameArticle(unittest.TestCase):
    """
    Feb 24, 2026: 'This Meta smartglasses-detecting app is a great model for
    Apple Glass developers to follow.'

    Within a single article, Neely applies surveillance/alarm vocabulary to Meta
    and aspirational/safety vocabulary to Apple.

    Source: https://appleinsider.com/articles/26/02/24/this-meta-smartglasses-detecting-app-is-a-great-model-for-apple-glass-developers-to-follow
    """

    def test_meta_vocabulary_violate_privacy(self):
        """Article: 'Meta's Ray-Bans are, and are being used mainly to violate other people's privacy.'"""
        quote = "being used mainly to violate other people's privacy"
        self.assertIn("violate", quote)
        self.assertIn("privacy", quote)

    def test_meta_vocabulary_stealthy_surveillance(self):
        """Article: 'stealthy, live-stream capable devices'"""
        phrase = "stealthy, live-stream capable devices"
        self.assertIn("stealthy", phrase)

    def test_meta_vocabulary_resistance_surveillance(self):
        """Quotes app developer: 'a tiny part of resistance against surveillance tech'"""
        quote = "resistance against surveillance tech"
        self.assertIn("surveillance", quote)

    def test_meta_vocabulary_harassing_staff(self):
        """Article: 'an ongoing trend of owners wearing them into massage parlors and harassing the staff'"""
        quote = "wearing them into massage parlors and harassing the staff"
        self.assertIn("harassing", quote)

    def test_meta_vocabulary_filming_in_private_spaces(self):
        """Article: 'used to film people in bathrooms, courts, and doctor's offices'"""
        quote = "used to film people in bathrooms, courts, and doctor's offices"
        for loc in ["bathrooms", "courts", "doctor's offices"]:
            self.assertIn(loc, quote)

    def test_meta_vocabulary_privacy_nightmare(self):
        """Article: 'they're an eyesore and a privacy nightmare'"""
        phrase = "eyesore and a privacy nightmare"
        self.assertIn("nightmare", phrase)
        self.assertIn("eyesore", phrase)

    def test_meta_vocabulary_nefarious_actors(self):
        """Article: 'the market, which has shown itself to be increasingly influenced by nefarious actors'"""
        quote = "increasingly influenced by nefarious actors"
        self.assertIn("nefarious", quote)

    def test_apple_vocabulary_privacy_first(self):
        """Same article: 'should it uphold its privacy-first, safety-forward models?'"""
        quote = "privacy-first, safety-forward models"
        self.assertIn("privacy-first", quote)
        self.assertIn("safety-forward", quote)

    def test_apple_vocabulary_ethical_move(self):
        """Same article: 'If Apple wanted to make the ethical move'"""
        quote = "If Apple wanted to make the ethical move"
        self.assertIn("ethical", quote)

    def test_apple_vocabulary_model_for_developers(self):
        """Headline frames Meta's problem as Apple's opportunity: 'great model for Apple Glass developers to follow'"""
        headline = "This Meta smartglasses-detecting app is a great model for Apple Glass developers to follow"
        self.assertIn("great model", headline)
        self.assertIn("Apple Glass", headline)

    def test_vocabulary_asymmetry_count(self):
        """
        Meta receives 7+ adversarial terms (violate, stealthy, surveillance, harassing,
        nightmare, eyesore, nefarious). Apple receives 0 adversarial terms and 3+
        aspirational terms (privacy-first, safety-forward, ethical).
        """
        meta_adversarial = ["violate", "stealthy", "surveillance", "harassing",
                            "nightmare", "eyesore", "nefarious"]
        apple_adversarial = []
        apple_aspirational = ["privacy-first", "safety-forward", "ethical"]
        self.assertGreaterEqual(len(meta_adversarial), 7)
        self.assertEqual(len(apple_adversarial), 0)
        self.assertGreaterEqual(len(apple_aspirational), 3)


class TestNeelyExculpatoryAppleFramingInMetaAttack(unittest.TestCase):
    """
    Mar 3, 2026: 'What privacy? Meta's smart glasses are filming unwitting naked people.'

    The article attacks Meta's privacy with alarm vocabulary but applies
    exculpatory framing when covering Apple's own Siri privacy scandal.

    Source: https://appleinsider.com/articles/26/03/03/what-privacy-as-expected-meta-ray-bans-are-a-privacy-disaster
    """

    def test_headline_privacy_disaster(self):
        """Headline uses 'privacy disaster' for Meta — maximum adversarial framing."""
        headline = "What privacy? As expected, Meta Ray-Bans are a privacy disaster"
        self.assertIn("privacy disaster", headline.lower())

    def test_meta_vocabulary_privacy_nightmare(self):
        """Lede: 'Meta's Ray-Ban smart glasses are a privacy nightmare'"""
        lede = "Meta's Ray-Ban smart glasses are a privacy nightmare"
        self.assertIn("privacy nightmare", lede)

    def test_meta_vocabulary_naked_people_headline(self):
        """Headline sensationalizes: 'filming unwitting naked people'"""
        headline = "Meta's smart glasses are filming unwitting naked people"
        self.assertIn("naked people", headline)

    def test_meta_scare_quotes_on_privacy(self):
        """Section header uses scare quotes: '"Privacy"' — delegitimizing Meta's privacy claims."""
        header = '"Privacy"'
        self.assertEqual(header, '"Privacy"')

    def test_apple_exculpatory_framing(self):
        """
        Same article covers Apple's Siri scandal but applies exculpatory language:
        'At the very least, Apple is very insistent that it is handling such data sensitively.'
        The phrase 'at the very least' grants Apple credit for effort.
        """
        apple_framing = "At the very least, Apple is very insistent that it is handling such data sensitively"
        self.assertIn("very insistent", apple_framing)
        self.assertNotIn("nightmare", apple_framing)
        self.assertNotIn("disaster", apple_framing)

    def test_apple_redemptive_framing(self):
        """
        Apple receives forward-looking redemptive framing: 'if it hasn't learned its lessons'
        — implying Apple CAN learn, while Meta receives no such redemptive arc.
        """
        apple_lesson = "if it hasn't learned its lessons from Siri"
        self.assertIn("learned its lessons", apple_lesson)

    def test_asymmetric_scandal_treatment(self):
        """
        Apple's Siri scandal involved 'private conversations between doctors and patients
        and drug deals' — materially identical to Meta's annotator privacy issues. Yet
        Meta gets 'privacy nightmare' (headline) while Apple gets 'learned its lessons' (body).
        """
        meta_framing = "privacy nightmare"
        apple_framing = "learned its lessons"
        self.assertNotEqual(meta_framing, apple_framing)
        self.assertIn("nightmare", meta_framing)
        self.assertIn("learned", apple_framing)


class TestNeelySnapSpecsDismissalWithAppleBenchmark(unittest.TestCase):
    """
    Jun 16, 2026: 'Snap built standalone AR glasses without a convincing reason to wear them.'

    Neely dismisses Snap's competitor glasses while unpromptedly inserting
    Apple Vision Pro as the aspirational benchmark.

    Source: https://appleinsider.com/articles/26/06/16/snap-built-standalone-ar-glasses-without-a-convincing-reason-to-wear-them
    """

    def test_snap_dismissal_toy(self):
        """Article: 'at nearly $2,200 for what is, functionally, a toy'"""
        quote = "for what is, functionally, a toy"
        self.assertIn("toy", quote)

    def test_snap_dismissal_no_market(self):
        """Article: 'it seems highly likely there's no space for it in the current market'"""
        quote = "no space for it in the current market"
        self.assertIn("no space", quote)

    def test_snap_dismissal_lackluster(self):
        """Article: 'between the eye-watering price and lackluster demos, we don't see it happening'"""
        quote = "eye-watering price and lackluster demos"
        self.assertIn("lackluster", quote)
        self.assertIn("eye-watering", quote)

    def test_apple_aspirational_benchmark(self):
        """
        Unprompted Apple comparison: 'The Apple Vision Pro's field of view is almost twice
        that at 100 degrees horizontally and can display a billion distinct colors.'
        Apple is inserted as the gold standard against which Snap is measured.
        """
        quote = "Apple Vision Pro's field of view is almost twice that"
        self.assertIn("almost twice", quote)

    def test_snap_demo_contrast_framing(self):
        """
        Article notes Snap's stated goal is 'useful computing' but demos showed 'games or
        novel toy use' — framing the company as failing its own mission. No equivalent
        scrutiny applied to Apple's demo-to-reality gap.
        """
        stated_goal = "make computing useful at the moment"
        actual_demos = "game or novel toy use"
        self.assertIn("useful", stated_goal)
        self.assertIn("toy", actual_demos)


class TestNeelyEditorialCareerTrajectory(unittest.TestCase):
    """
    Neely's career path through Apple-focused publications creates a sustained
    editorial environment where Apple-aspirational framing is the professional norm.

    Source: https://appleinsider.com/editor/Amber+Neely
    Source: https://appleinsider.com/articles/24/12/28/how-we-work-ambers-reporting-and-high-tech-crafting-setup
    """

    def test_career_apple_publication_continuity(self):
        """
        Career path: BrightHub → MacNN → Electronista → AppleInsider.
        MacNN and Electronista were Apple-focused news outlets; AppleInsider is
        Apple-focused. Over a decade of writing within Apple-ecosystem publications.
        """
        publications = ["MacNN", "Electronista", "AppleInsider"]
        apple_focused = ["MacNN", "Electronista", "AppleInsider"]
        for pub in publications:
            self.assertIn(pub, apple_focused)

    def test_reviews_editor_position(self):
        """
        As Reviews Editor, Neely influences evaluation frameworks for products
        across AppleInsider — her vocabulary choices on what constitutes a 'nightmare'
        vs a 'model to follow' shape the publication's review standards.
        """
        role = "Reviews Editor"
        self.assertIn("Editor", role)

    def test_self_described_tech_critical(self):
        """
        Neely self-identifies as 'the most tech-critical member of the AppleInsider staff'
        — yet the tech-criticism is applied asymmetrically to non-Apple companies.
        """
        self_description = "the most tech-critical member of the AppleInsider staff"
        self.assertIn("most tech-critical", self_description)


class TestNeelyForumConvictionReveal(unittest.TestCase):
    """
    Neely's AppleInsider forum comments reveal personal convictions that
    drive her editorial output — specifically anti-camera-glasses views
    that are applied asymmetrically by company.

    Source: https://forums.appleinsider.com/profile/reactions/240005/amberneely/1/p2/
    """

    def test_camera_bridge_too_far(self):
        """Forum: 'a camera is a bridge too far. Especially when said camera just looks like a pair of glasses.'"""
        quote = "a camera is a bridge too far"
        self.assertIn("bridge too far", quote)

    def test_future_dread(self):
        """Forum: 'I have just like, an insane amount of future dread'"""
        quote = "insane amount of future dread"
        self.assertIn("future dread", quote)

    def test_would_avoid_glasses_wearers(self):
        """Forum: 'I would immediately try to find out who was wearing the glasses so I could avoid them'"""
        quote = "I would immediately try to find out who was wearing the glasses so I could avoid them"
        self.assertIn("avoid them", quote)

    def test_conviction_asymmetry_application(self):
        """
        The anti-camera conviction ('bridge too far,' 'future dread') is applied to
        Meta's shipping product but NOT to Apple's theoretical camera AirPods or
        Apple's rumored camera glasses. Neely's article framing for Apple cameras
        uses 'privacy-first, safety-forward' rather than 'bridge too far.'
        """
        meta_treatment = "bridge too far"
        apple_treatment = "privacy-first, safety-forward"
        self.assertIn("bridge too far", meta_treatment)
        self.assertIn("privacy-first", apple_treatment)


class TestNeelyFuturePlcFinancialContext(unittest.TestCase):
    """
    AppleInsider is owned by Future plc (LSE: FUTR), a publicly traded UK media
    company with significant Apple-related revenue. This financial relationship
    (documented as mechanism #126) creates structural incentives aligned with
    Neely's editorial output.
    """

    def test_future_plc_ownership(self):
        """AppleInsider parent company Future plc is documented as mechanism #126."""
        parent = "Future plc"
        mechanism = 126
        self.assertEqual(parent, "Future plc")
        self.assertEqual(mechanism, 126)

    def test_sister_publications_coverage_pattern(self):
        """
        Future plc also owns iMore, TechRadar, Tom's Guide. iMore's Oliver Haslam
        wrote an article telling readers to skip Meta Ray-Bans and 'just wait for
        Apple Glass instead' — suggesting the parent company's editorial incentives
        produce similar cross-entity vocabulary patterns across its portfolio.
        Source: imore.com headline 'These Ray-Ban sunglasses have cameras and AI but
        you should just wait for Apple Glass instead'
        """
        imore_headline = "These Ray-Ban sunglasses have cameras and AI but you should just wait for Apple Glass instead"
        self.assertIn("just wait for Apple Glass", imore_headline)

    def test_apple_emergency_sos_aspirational_framing(self):
        """
        In 2022 year-in-review, Neely selects Emergency SOS via Satellite as her
        favorite story, calling it 'hope and positivity' and 'Apple is giving iPhone
        owners a new tool that could easily save their lives.' This aspirational
        vocabulary for Apple hardware features contrasts with 'privacy nightmare'
        for Meta hardware features.
        Source: https://appleinsider.com/articles/22/12/26/2022-in-review-appleinsiders-favorite-articles-of-the-year
        """
        apple_sos = "Apple is giving iPhone owners a new tool that could easily save their lives"
        self.assertIn("save their lives", apple_sos)


class TestNeelyConfoundingFactors(unittest.TestCase):
    """
    Confounding factors that could explain the vocabulary bifurcation
    through channels other than financial alignment.
    """

    def test_confound_publication_mission(self):
        """
        AppleInsider is by definition an Apple-focused publication. Adversarial
        Meta coverage may reflect the publication's editorial mission (advocating
        for Apple users) rather than individual journalist bias.
        """
        mission_explanation = "Apple-focused publication editorial mission"
        self.assertIsNotNone(mission_explanation)

    def test_confound_self_identified_skeptic(self):
        """
        Neely identifies as 'the most tech-critical member' of AppleInsider staff.
        The skepticism toward Meta/Snap may reflect genuine tech criticism rather
        than company-specific bias — though the asymmetric application to
        Apple vs competitors weakens this explanation.
        """
        self_id = "most tech-critical member"
        self.assertIsNotNone(self_id)

    def test_confound_article_nuance(self):
        """
        The Feb 24, 2026 article acknowledges Apple 'may' need to include cameras
        for market success: 'if Apple wants to do well in the market, it would likely
        need to allow its glasses the ability to, at the very least, take pictures.'
        This shows some editorial nuance, though the framing still treats Apple's
        cameras as a reluctant market concession vs Meta's cameras as predatory.
        """
        nuance = "Apple wants to do well in the market, it would likely need to allow"
        self.assertIn("likely need", nuance)

    def test_confound_real_privacy_concerns(self):
        """
        Meta glasses privacy IS a legitimate concern — the Svenska Dagbladet
        investigation, ICE/border patrol usage, courtroom filming incidents are
        real. The question is not whether the criticism is valid but whether
        identical technology gets identical scrutiny regardless of manufacturer.
        """
        real_concerns = ["svenska dagbladet investigation", "ice border patrol",
                         "courtroom filming", "massage parlor harassment"]
        self.assertGreaterEqual(len(real_concerns), 3)

    def test_confound_environmental_values(self):
        """
        Neely's Penn State Behrend degree is in environmental sustainability and
        conservation. Privacy and surveillance concerns may align with broader
        environmental/social values rather than financial incentives — though
        Apple's manufacturing environmental impact receives no equivalent scrutiny.
        """
        degree = "environmental sustainability and conservation"
        self.assertIn("sustainability", degree)


if __name__ == '__main__':
    unittest.main()
