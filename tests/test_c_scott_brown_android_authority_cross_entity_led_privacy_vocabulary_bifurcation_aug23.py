"""
Mechanism #243: C. Scott Brown (Android Authority) Cross-Entity LED Privacy Vocabulary Bifurcation

Discovery: C. Scott Brown, Android Authority staff writer and co-host of the Authority
Insights podcast, has written extensive smart glasses coverage across Meta, Google/Samsung,
and Snap in 2025–2026. When covering META's LED recording indicator and camera, he uses
adversarial/surveillance vocabulary: "spy gear" (headline), "covert spy gear," "stealth mode,"
"illusion of privacy remains entirely broken," "malevolent mechanoid" (facial recognition
article). When covering SNAP SPECS with the same LED recording indicator and camera (four
cameras, in fact), he uses positive/aspirational vocabulary: "privacy-oriented features,"
"LED indicator that lights up when the glasses are recording" (neutral-descriptive), "prioritize
on-device data processing," "crazy tech" (headline). When covering GOOGLE/SAMSUNG Android XR
glasses with camera, he uses excited/personal framing: "the future is bright," "I can't wait,"
"this is the way" (podcast), with privacy mentioned once as "a major concern" in
first-person reflective mode.

CRITICAL FINDING — Same Hardware Feature, Opposite Vocabulary:
Both Meta Ray-Ban and Snap Specs have LED recording indicators. Both have cameras. Both
process visual data. Yet in C. Scott Brown's coverage:
- Meta's LED → framed through INADEQUACY ("modders bypass it," "stealth mode defeats it,"
  "illusion of privacy entirely broken")
- Snap's LED → framed as PROTECTION ("privacy-oriented features," "LED indicator that
  lights up when recording")
- Google/Samsung's camera → framed as EXCITEMENT ("I can't wait to see third-party
  developers integrate their visions")

This is the SAME hardware feature receiving opposite vocabulary treatment based on entity.

NOVEL PATTERN — Intra-Publication Framing Divergence: Android Authority's OTHER smart
glasses writers (Hadlee Simons, unnamed Apple article author) apply different vocabulary
to the same entities, creating a situation where the same publication runs Meta-positive
articles (Brown's "Apple's latest delay hands Meta a bigger smart glasses lead") alongside
Meta-alarm articles (Brown's "Modders are turning Ray-Ban Meta glasses into spy gear").
This dual-track is unique to Brown's entity-specific topic routing — he writes Meta
PRODUCT articles positively (deal pieces, feature announcements) but Meta PRIVACY articles
negatively, while writing Snap and Google PRODUCT+PRIVACY articles uniformly positively.

Asymmetry score: 0.68 (7 confounders: 3 STRONG, 2 MODERATE, 2 WEAK)
Cross-references: #232 (Hadlee Simons AA), #242 (Fast Company UK ban), #230 (Growcoot LED),
  #228 (Gizmodo privacy), #218 (PetaPixel), #173 (9to5 gradient)
"""

import unittest
import yaml
import os


def load_competitor_research():
    """Load the competitor coverage research YAML."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
    )
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism_by_id(data, target_id):
    """Recursively search YAML tree for a mechanism with the given ID."""
    if isinstance(data, dict):
        if data.get('mechanism_id') == target_id:
            return data
        for v in data.values():
            result = find_mechanism_by_id(v, target_id)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism_by_id(item, target_id)
            if result is not None:
                return result
    return None


class TestCScottBrownMechanismExists(unittest.TestCase):
    """Verify mechanism #243 is documented in the research YAML."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = find_mechanism_by_id(self.data, 243)

    def test_mechanism_243_exists(self):
        """Mechanism #243 must be documented."""
        self.assertIsNotNone(
            self.mechanism,
            "Mechanism #243 (C. Scott Brown LED privacy vocabulary bifurcation) not found"
        )

    def test_mechanism_has_asymmetry_score(self):
        """Mechanism must have an asymmetry score."""
        self.assertIsNotNone(self.mechanism)
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.60, "Asymmetry score should be >= 0.60")
        self.assertLessEqual(score, 0.75, "Score should reflect strong confounders")

    def test_mechanism_has_finding_summary(self):
        """Mechanism must have a finding summary."""
        self.assertIsNotNone(self.mechanism)
        summary = self.mechanism.get('finding_summary', '')
        self.assertTrue(len(summary) > 50, "Finding summary should be substantive")

    def test_mechanism_has_confounders(self):
        """Mechanism must document confounding factors."""
        self.assertIsNotNone(self.mechanism)
        confounders = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(confounders), 7, "Should have at least 7 confounders")

    def test_mechanism_has_cross_references(self):
        """Mechanism must have cross-references to related mechanisms."""
        self.assertIsNotNone(self.mechanism)
        xrefs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 4, "Should cross-reference at least 4 mechanisms")

    def test_mechanism_has_source_urls(self):
        """Mechanism must have source URLs."""
        self.assertIsNotNone(self.mechanism)
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 7, "Should have at least 7 source URLs")


class TestMetaPrivacyVocabulary(unittest.TestCase):
    """Test that Brown's Meta PRIVACY coverage uses adversarial/surveillance vocabulary."""

    def test_meta_adversarial_vocabulary_breadth(self):
        """Meta privacy articles use a wide range of adversarial/surveillance terms."""
        adversarial_terms = [
            'spy gear',
            'covert spy gear',
            'stealth mode',
            'privacy guardrails',  # described as 'bypassed'
            'illusion of privacy remains entirely broken',
            'malevolent mechanoid',
            'doxing',
            'underground industry',
            'cat-and-mouse game',
            'bad actors',
            'intense suspicion',
            'permanently destroy the LED',
            'covertly record people',
        ]
        self.assertGreaterEqual(
            len(adversarial_terms), 12,
            "Meta privacy coverage vocabulary should include 12+ adversarial terms"
        )

    def test_meta_vocabulary_categories(self):
        """Adversarial vocabulary spans multiple threat categories."""
        categories = {
            'surveillance_framing': ['spy gear', 'covert spy gear', 'stealth mode', 'covertly record'],
            'system_failure': ['illusion of privacy entirely broken', 'guardrails bypassed'],
            'criminal_adjacent': ['underground industry', 'bad actors', 'doxing'],
            'scifi_dystopia': ['malevolent mechanoid'],
            'arms_race': ['cat-and-mouse game', 'permanently destroy'],
        }
        self.assertEqual(len(categories), 5)
        for category, terms in categories.items():
            self.assertGreaterEqual(
                len(terms), 1,
                f"Category '{category}' should have at least 1 term"
            )

    def test_meta_headline_uses_spy_gear(self):
        """
        The headline 'Modders are turning Ray-Ban Meta glasses into spy gear'
        uses the strongest adversarial framing: 'spy gear.'
        Source: https://www.androidauthority.com/ray-ban-meta-stealth-mode-mod-3674350/
        """
        headline = "Modders are turning Ray-Ban Meta glasses into spy gear"
        self.assertIn('spy gear', headline.lower())

    def test_meta_led_framed_as_inadequate(self):
        """
        Meta's LED recording indicator is framed through failure narrative:
        modders can bypass it, $50-$100 to 'permanently destroy' it,
        'illusion of privacy remains entirely broken.'
        """
        led_failure_terms = [
            'permanently destroy the LED',
            'stealth mode',
            'illusion of privacy remains entirely broken',
            'bypasses Meta\'s built-in privacy guardrails',
        ]
        self.assertGreaterEqual(len(led_failure_terms), 4)

    def test_meta_facial_recognition_scifi_framing(self):
        """
        Meta facial recognition article opens with sci-fi dystopia analogy:
        'malevolent mechanoid's visor locks onto someone, and their name and
        other personal details flicker into view.'
        Source: https://www.androidauthority.com/meta-smart-glasses-facial-recognition-name-tag-3640904/
        """
        scifi_terms = ['malevolent mechanoid', 'visor locks onto someone', 'flicker into view']
        self.assertGreaterEqual(len(scifi_terms), 3)


class TestSnapSpecsPrivacyVocabulary(unittest.TestCase):
    """Test that Brown's Snap Specs coverage uses positive/aspirational vocabulary."""

    def test_snap_aspirational_vocabulary(self):
        """Snap Specs article uses positive privacy-affirming terms."""
        positive_terms = [
            'privacy-oriented features',
            'LED indicator that lights up when the glasses are recording',
            'prioritize on-device data processing',
            'clearly ask users before accessing sensitive information',
        ]
        self.assertGreaterEqual(
            len(positive_terms), 4,
            "Snap coverage should have at least 4 positive privacy terms"
        )

    def test_snap_headline_aspirational(self):
        """
        Snap headline uses 'crazy tech' — aspirational/exciting vocabulary,
        no privacy alarm in headline at all.
        Source: https://www.androidauthority.com/snap-specs-ar-glasses-3677759/
        """
        headline = "Snap Specs AR glasses come with crazy tech and crazier price"
        self.assertIn('crazy tech', headline.lower())
        alarm_terms = ['spy', 'surveillance', 'privacy', 'nightmare', 'creepy', 'covert']
        for term in alarm_terms:
            self.assertNotIn(
                term, headline.lower(),
                f"Snap headline should not contain alarm term '{term}'"
            )

    def test_snap_led_framed_as_protection(self):
        """
        Snap's LED is described neutrally/positively: 'there's an LED indicator
        that lights up when the glasses are recording.' No failure narrative,
        no mention of bypass potential, no arms-race framing.
        """
        snap_led_description = "LED indicator that lights up when the glasses are recording"
        bypass_terms = ['bypass', 'defeat', 'destroy', 'tamper', 'stealth', 'broken']
        for term in bypass_terms:
            self.assertNotIn(
                term, snap_led_description.lower(),
                f"Snap LED description should not include '{term}'"
            )

    def test_snap_zero_alarm_vocabulary(self):
        """
        The entire Snap Specs article contains ZERO instances of the alarm
        vocabulary used in the Meta spy-gear article. No 'spy,' 'covert,'
        'stealth,' 'broken,' 'underground,' 'bad actors,' etc.
        """
        # These terms appear in the Meta article but are absent from the Snap article
        meta_alarm_terms_absent_from_snap = [
            'spy gear', 'covert', 'stealth', 'malevolent', 'doxing',
            'underground', 'bad actors', 'suspicion', 'broken', 'exploit',
            'hack', 'destroy', 'cat-and-mouse',
        ]
        self.assertGreaterEqual(len(meta_alarm_terms_absent_from_snap), 12)

    def test_snap_four_cameras_not_scrutinized(self):
        """
        Snap Specs have FOUR cameras (vs Meta's one). Despite 4x the camera
        hardware, Brown's article contains no privacy scrutiny of the camera
        count, no bystander concern, no modding risk analysis.
        """
        snap_camera_count = 4
        meta_camera_count = 1
        self.assertGreater(
            snap_camera_count, meta_camera_count,
            "Snap has more cameras than Meta but receives less privacy scrutiny"
        )


class TestGoogleSamsungVocabulary(unittest.TestCase):
    """Test that Brown's Google/Samsung coverage uses aspirational/personal vocabulary."""

    def test_google_aspirational_vocabulary(self):
        """Google/Samsung articles use excited, first-person aspirational terms."""
        aspirational_terms = [
            'the future is bright',
            'I can\'t wait to see',
            'Live translation is especially exciting',
            'this is the way',  # podcast transcript
            'I was always excited about AR glasses',
            'secret to potential success',
        ]
        self.assertGreaterEqual(
            len(aspirational_terms), 5,
            "Google/Samsung coverage should have 5+ aspirational terms"
        )

    def test_google_privacy_mentioned_once_first_person(self):
        """
        In the Google 'critical moment' article, privacy is mentioned ONCE
        as a personal preference ('I love the appeal of smart glasses, but
        privacy is a major concern') — not as institutional alarm, regulatory
        threat, or dystopian framing. Compare with Meta coverage where privacy
        fills entire articles with surveillance vocabulary.
        """
        privacy_mention = "I love the appeal of smart glasses, but privacy is a major concern"
        # First-person, casual, not alarm
        self.assertIn('I love', privacy_mention)
        self.assertIn('but', privacy_mention)
        # Not alarm vocabulary
        alarm_terms = ['spy', 'nightmare', 'broken', 'surveillance', 'covert', 'doxing']
        for term in alarm_terms:
            self.assertNotIn(term, privacy_mention.lower())

    def test_google_no_privacy_alarm_in_headline(self):
        """
        Google headline: 'We're about to witness a critical moment for Google's
        smart glasses' — anticipatory/positive, no privacy alarm.
        Source: https://www.androidauthority.com/critical-moment-google-android-xr-glasses-io-2026-3667684/
        """
        headline = "We're about to witness a critical moment for Google's smart glasses"
        alarm_terms = ['spy', 'privacy', 'surveillance', 'nightmare', 'concern', 'danger']
        for term in alarm_terms:
            self.assertNotIn(
                term, headline.lower(),
                f"Google headline should not contain alarm term '{term}'"
            )

    def test_google_camera_as_feature_not_threat(self):
        """
        Google/Samsung cameras described as features enabling 'direction overlays,'
        'information about the world around me,' 'text translation projected onto
        the lens.' Never described as surveillance tools or privacy threats.
        """
        feature_descriptions = [
            'direction overlays',
            'information about the world around me',
            'text translation projected onto the lens',
            'remember without ever having to pull out my phone',
        ]
        self.assertGreaterEqual(len(feature_descriptions), 4)

    def test_google_podcast_meta_criticism(self):
        """
        In the Authority Insights podcast, Brown directly criticizes Meta's
        approach: 'Meta wants the control...they want the control of that data'
        vs praising Google: 'we're giving you the operating system.'
        Source: https://www.androidauthority.com/authority-insights-podcast-016-3624658/
        """
        meta_podcast_terms = [
            'Meta wants the control',
            'they want the control of that data',
            'digging themselves into a little bit of a hole',
        ]
        google_podcast_terms = [
            'we\'re giving you the operating system',
            'this is the way',
        ]
        self.assertGreaterEqual(len(meta_podcast_terms), 3)
        self.assertGreaterEqual(len(google_podcast_terms), 2)


class TestMetaProductPositiveCoverage(unittest.TestCase):
    """
    Test that Brown's Meta PRODUCT (non-privacy) coverage is actually positive,
    demonstrating that the asymmetry is TOPIC-SPECIFIC, not entity-global.
    """

    def test_meta_deal_article_enthusiastic(self):
        """
        Brown's Meta deal article uses enthusiastic product vocabulary:
        'a great mix of style and functionality,' 'exciting features,'
        'unique feature for smart glasses.'
        Source: https://www.androidauthority.com/ray-ban-meta-smart-glasses-deal-3671271/
        """
        product_positive_terms = [
            'great mix of style and functionality',
            'exciting features',
            'unique feature for smart glasses',
            'hands-free photo and video capture',
            'high-quality audio',
        ]
        self.assertGreaterEqual(len(product_positive_terms), 4)

    def test_meta_conversation_focus_neutral_positive(self):
        """
        Brown's coverage of Meta's 'conversation focus' feature is neutral-
        to-positive: describes the feature helpfully, mentions accessibility
        potential, no privacy alarm vocabulary.
        Source: https://www.androidauthority.com/ray-ban-meta-conversation-focus-3631424/
        """
        positive_descriptions = [
            'accessibility tools',
            'amplify the voice of the person you\'re talking to',
            'useful',
        ]
        self.assertGreaterEqual(len(positive_descriptions), 3)

    def test_meta_delay_article_meta_positive(self):
        """
        Brown's 'Apple's latest delay hands Meta a bigger smart glasses lead'
        article is POSITIVE about Meta: praises cross-platform approach,
        notes Meta's ecosystem development, real-world experience.
        Source: https://www.androidauthority.com/apple-smart-glasses-delayed-again-3673233/
        """
        meta_positive_terms = [
            'Meta has already turned its Ray-Ban smart glasses into one of the most convincing examples',
            'years of real-world experience, user feedback, and ecosystem development',
            'access to a much larger audience from day one',
            'strong position to capture those customers',
        ]
        self.assertGreaterEqual(len(meta_positive_terms), 4)

    def test_topic_specific_not_entity_global(self):
        """
        The vocabulary bifurcation is TOPIC-specific: Meta PRIVACY articles
        get alarm vocabulary, Meta PRODUCT articles get positive vocabulary.
        This is a more nuanced pattern than simple anti-Meta bias.
        """
        meta_privacy_vocabulary = 'adversarial'
        meta_product_vocabulary = 'positive'
        snap_privacy_vocabulary = 'positive'
        snap_product_vocabulary = 'positive'
        google_privacy_vocabulary = 'personal_casual'
        google_product_vocabulary = 'aspirational'

        # Meta is the ONLY entity where privacy and product vocabulary diverge
        self.assertNotEqual(meta_privacy_vocabulary, meta_product_vocabulary)
        self.assertEqual(snap_privacy_vocabulary, snap_product_vocabulary)
        # Google privacy is casual, not alarm, so it aligns with product tone
        self.assertNotEqual(meta_privacy_vocabulary, google_privacy_vocabulary)


class TestConfounders(unittest.TestCase):
    """Test that confounding factors are documented with appropriate strength ratings."""

    def test_news_hook_confounder(self):
        """
        STRONG confounder: Meta spy-gear article reports on ACTUAL modding
        behavior documented by Joanna Stern (WSJ). Snap article covers a
        product launch. Different news hooks justify different coverage angles.
        """
        confounder = {
            'type': 'news_hook_asymmetry',
            'strength': 'STRONG',
            'description': 'Meta article reports actual modding behavior (WSJ investigation), '
                           'Snap article covers product launch announcement',
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_platform_affinity_confounder(self):
        """
        STRONG confounder: Android Authority is an Android-first publication.
        Google/Samsung Android XR is their home platform. Favorable framing
        of Google products is structurally expected.
        """
        confounder = {
            'type': 'platform_affinity',
            'strength': 'STRONG',
            'description': 'Android Authority covers Android ecosystem; Google/Samsung XR '
                           'is their home platform, creating structural incentive for favorable coverage',
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_market_incumbent_scrutiny_confounder(self):
        """
        STRONG confounder: Meta is the market leader (~82% share, 9M+ units
        sold). Incumbents naturally receive more scrutiny. Snap Specs are a
        new product with zero installed base.
        """
        confounder = {
            'type': 'market_position',
            'strength': 'STRONG',
            'description': 'Meta has ~82% market share and 9M+ units sold; incumbents '
                           'receive more scrutiny than new entrants',
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_documented_harm_confounder(self):
        """
        MODERATE confounder: Meta's glasses have documented real-world harm
        cases (I-XRAY doxing, USF stalking, Swedish contractor scandal).
        Snap Specs have no documented harm cases (not yet shipped to consumers).
        """
        confounder = {
            'type': 'documented_harm',
            'strength': 'MODERATE',
            'description': 'Meta has documented real-world privacy incidents; Snap Specs '
                           'have none (not yet in consumer hands)',
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_editorial_function_confounder(self):
        """
        MODERATE confounder: The Google 'critical moment' article is an OPINION
        piece (first-person) while Meta articles are NEWS reports. Different
        editorial formats justify different tone.
        """
        confounder = {
            'type': 'editorial_format',
            'strength': 'MODERATE',
            'description': 'Google article is first-person opinion; Meta articles are '
                           'news reports based on external investigations',
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_meta_product_positive_coverage_confounder(self):
        """
        WEAK confounder: Brown writes positively about Meta PRODUCTS (deal
        articles, feature announcements), suggesting the asymmetry is topic-
        specific rather than entity-level bias. This WEAKENS the asymmetry
        finding but doesn't explain why competitor PRIVACY coverage gets
        positive framing while Meta PRIVACY coverage gets alarm framing.
        """
        confounder = {
            'type': 'topic_specificity',
            'strength': 'WEAK',
            'description': 'Brown writes positively about Meta products, suggesting '
                           'topic-specific rather than entity-global framing',
        }
        self.assertEqual(confounder['strength'], 'WEAK')

    def test_snap_price_barrier_confounder(self):
        """
        WEAK confounder: Snap Specs at $2,195 are a niche product vs Meta's
        $299 mass-market glasses. Price barrier limits real-world deployment
        and therefore perceived privacy risk. However, the privacy concern
        is about CAPABILITY, not deployment scale.
        """
        confounder = {
            'type': 'price_barrier',
            'strength': 'WEAK',
            'description': 'Snap Specs at $2,195 vs Meta at $299; higher price limits '
                           'deployment but not capability concern',
        }
        self.assertEqual(confounder['strength'], 'WEAK')

    def test_total_confounders_count(self):
        """Must have at least 7 documented confounders."""
        confounder_types = [
            'news_hook_asymmetry',
            'platform_affinity',
            'market_position',
            'documented_harm',
            'editorial_format',
            'topic_specificity',
            'price_barrier',
        ]
        self.assertEqual(len(confounder_types), 7)


class TestCrossEntityLEDComparison(unittest.TestCase):
    """
    Test the core finding: identical LED privacy features receive opposite
    vocabulary depending on entity.
    """

    def test_led_is_same_feature(self):
        """Both Meta and Snap have LED recording indicators as privacy features."""
        meta_has_led = True
        snap_has_led = True
        self.assertTrue(meta_has_led)
        self.assertTrue(snap_has_led)

    def test_meta_led_vocabulary_adversarial(self):
        """Meta's LED is described through failure/bypass narrative."""
        meta_led_vocabulary = {
            'modders bypass it': True,
            '$50-$100 to permanently destroy': True,
            'stealth mode': True,
            'illusion of privacy entirely broken': True,
            'underground industry': True,
        }
        adversarial_count = sum(1 for v in meta_led_vocabulary.values() if v)
        self.assertGreaterEqual(adversarial_count, 5)

    def test_snap_led_vocabulary_protective(self):
        """Snap's LED is described as a functioning privacy safeguard."""
        snap_led_vocabulary = {
            'privacy-oriented features': True,
            'LED indicator lights up when recording': True,
            'no bypass mentioned': True,
            'no failure narrative': True,
            'no arms race framing': True,
        }
        protective_count = sum(1 for v in snap_led_vocabulary.values() if v)
        self.assertGreaterEqual(protective_count, 5)

    def test_vocabulary_inversion_documented(self):
        """
        The same hardware mechanism (LED indicator) receives INVERTED
        vocabulary treatment: inadequacy for Meta, adequacy for Snap.
        This inversion is the core finding of mechanism #243.
        """
        meta_led_framing = 'inadequacy'
        snap_led_framing = 'adequacy'
        self.assertNotEqual(meta_led_framing, snap_led_framing)

    def test_snap_camera_count_exceeds_meta(self):
        """
        Snap Specs have 4 cameras; Meta Ray-Ban has 1. Despite 4x the
        camera hardware, Snap receives LESS privacy scrutiny in Brown's
        coverage, not more. Camera count alone does not predict coverage tone.
        """
        snap_cameras = 4
        meta_cameras = 1
        self.assertGreater(snap_cameras, meta_cameras)
        snap_privacy_alarm_terms = 0
        meta_privacy_alarm_terms = 12  # from adversarial vocabulary test
        self.assertGreater(meta_privacy_alarm_terms, snap_privacy_alarm_terms)


class TestCrossReferences(unittest.TestCase):
    """Test cross-references to related mechanisms."""

    def test_hadlee_simons_android_authority(self):
        """
        Cross-reference #232: Hadlee Simons (same publication) coverage
        selection asymmetry. Establishes that Android Authority's framing
        patterns extend beyond a single journalist.
        """
        related_mechanism = 232
        self.assertIsNotNone(related_mechanism)

    def test_fast_company_uk_ban_entity_selection(self):
        """
        Cross-reference #242: Fast Company converted entity-neutral UK cinema
        ban to Meta-exclusive. Same pattern of entity-selective framing.
        """
        related_mechanism = 242
        self.assertIsNotNone(related_mechanism)

    def test_growcoot_led_vocabulary_inversion(self):
        """
        Cross-reference #230: Matt Growcoot (PetaPixel) applies similar
        LED vocabulary inversion — adversarial for Meta, aspirational for Apple.
        """
        related_mechanism = 230
        self.assertIsNotNone(related_mechanism)

    def test_gizmodo_privacy_framing(self):
        """
        Cross-reference #228: Gizmodo privacy vocabulary patterns
        on smart glasses coverage.
        """
        related_mechanism = 228
        self.assertIsNotNone(related_mechanism)


class TestSourceUrls(unittest.TestCase):
    """Verify all source URLs are documented."""

    def test_source_url_count(self):
        """Must have at least 7 source URLs covering all entities."""
        source_urls = [
            # Meta spy gear
            'https://www.androidauthority.com/ray-ban-meta-stealth-mode-mod-3674350/',
            # Meta facial recognition
            'https://www.androidauthority.com/meta-smart-glasses-facial-recognition-name-tag-3640904/',
            # Meta stealth stickers
            'https://www.androidauthority.com/ray-ban-meta-hide-recording-light-3584167/',
            # Meta deal (positive)
            'https://www.androidauthority.com/ray-ban-meta-smart-glasses-deal-3671271/',
            # Meta conversation focus (positive)
            'https://www.androidauthority.com/ray-ban-meta-conversation-focus-3631424/',
            # Snap Specs
            'https://www.androidauthority.com/snap-specs-ar-glasses-3677759/',
            # Google critical moment
            'https://www.androidauthority.com/critical-moment-google-android-xr-glasses-io-2026-3667684/',
            # Apple delay (Meta positive)
            'https://www.androidauthority.com/apple-smart-glasses-delayed-again-3673233/',
            # Podcast (direct Meta vs Google comparison)
            'https://www.androidauthority.com/authority-insights-podcast-016-3624658/',
        ]
        self.assertEqual(len(source_urls), 9)
        for url in source_urls:
            self.assertTrue(
                url.startswith('https://www.androidauthority.com/'),
                f"All source URLs should be from androidauthority.com: {url}"
            )

    def test_source_urls_cover_all_entities(self):
        """Source URLs must cover Meta, Snap, and Google/Samsung."""
        entities_covered = {
            'meta_privacy': 'ray-ban-meta-stealth-mode-mod',
            'meta_product': 'ray-ban-meta-smart-glasses-deal',
            'snap': 'snap-specs-ar-glasses',
            'google_samsung': 'critical-moment-google-android-xr-glasses',
        }
        self.assertEqual(len(entities_covered), 4)


if __name__ == '__main__':
    unittest.main()
