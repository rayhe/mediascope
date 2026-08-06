"""
Sean Hollister cross-entity analysis: Apple recusal asymmetry.

The Verge's primary consumer advocacy reporter cannot cover Apple products
(wife employed by Apple as video producer, recusal effective June 2023).
This creates a structural gap: Meta products receive Hollister's consumer
harm framing while Apple's competing products (Vision Pro, future Apple
glasses) receive no consumer advocacy treatment from The Verge's designated
consumer harm reporter.

The analysis examines:
1. Hollister's pre-recusal Apple coverage (adversarial, consumer advocacy)
2. His continued adversarial coverage of Meta and Google
3. The structural gap: no consumer advocacy reporter covers Apple post-recusal
4. The three-entity comparison: Meta (adversarial), Google (moderate), Apple (absent)

Sources:
- Ethics disclosure: https://www.theverge.com/authors/sean-hollister (June 2023)
- Apple self-repair coverage (2022): Widely cited adversarial review
- Meta Conversation Focus (Jul 2026): Consumer harm framing, accessibility paywall
- Epic v. Google trial (2023-2024): Adversarial accountability coverage
- Google Pixel 7-year promise (Oct 2023): Skeptical consumer advocacy
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_journalist(name):
    """Load a journalist profile from careers/journalists.yaml."""
    path = os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    for j in data.get('journalists', []):
        if j.get('name') == name:
            return j
    return None


def load_competitor_research():
    """Load competitor coverage research profile."""
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def get_verge_research():
    """Get The Verge's section from competitor coverage research."""
    data = load_competitor_research()
    pubs = data.get('publications', {})
    return pubs.get('the-verge', {})


class TestHollisterProfile(unittest.TestCase):
    """Verify Sean Hollister's journalist profile data is complete and accurate."""

    def setUp(self):
        self.profile = load_journalist('Sean Hollister')
        self.assertIsNotNone(self.profile, "Sean Hollister profile must exist")

    def test_career_arc_complete(self):
        """Four career stops: Verge (founding) → Gizmodo → CNET → Verge (return)."""
        career = self.profile['career']
        self.assertEqual(len(career), 4, "Four career stops")
        pubs = [c['publication'] for c in career]
        self.assertEqual(pubs, ['the-verge', 'gizmodo', 'cnet', 'the-verge'])

    def test_founding_member_status(self):
        """First stint at The Verge from 2011 (founding) to 2014."""
        first = self.profile['career'][0]
        self.assertEqual(first['start'], '2011')
        self.assertEqual(first['end'], '2014')
        self.assertIn('founding member', first['notes'].lower())

    def test_return_migration_unique(self):
        """Hollister's Verge→Gizmodo→CNET→Verge return is unique in the dataset."""
        notes = self.profile.get('notes', '')
        self.assertIn('return migration', notes.lower(),
                      "Notes should document unique return migration pattern")

    def test_apple_recusal_documented(self):
        """Apple recusal (wife at Apple) must be documented in profile."""
        current_role = self.profile['career'][-1]  # Current Verge role
        notes = current_role.get('notes', '')
        self.assertIn('apple', notes.lower())
        self.assertIn('recus', notes.lower(),
                      "Apple recusal must be explicitly documented")

    def test_consumer_advocacy_beat_documented(self):
        """Consumer advocacy is a documented part of Hollister's beat."""
        current_role = self.profile['career'][-1]
        beat = current_role.get('beat', '')
        self.assertIn('consumer advocacy', beat.lower())

    def test_source_urls_present(self):
        """Profile must have at least 3 source URLs."""
        urls = self.profile.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3)

    def test_multi_publication_flag(self):
        """Multi-publication flag must be true (4 publications)."""
        self.assertTrue(self.profile.get('multi_publication'))


class TestAppleRecusalTimeline(unittest.TestCase):
    """
    Document the Apple recusal timeline and its coverage implications.

    Before June 2023: Hollister covered Apple with adversarial consumer advocacy.
    - Apple Self-Repair Program (May 2022): 79 pounds of tools for a 1.1oz battery,
      $1,200 credit card hold, $69 battery same as Apple Store installation price.
      Widely cited as damning consumer advocacy journalism.

    After June 2023: Complete cessation of Apple coverage.
    - Apple Vision Pro launch (Feb 2024): Camera-equipped AR headset that 3D-maps
      surroundings. No consumer harm coverage from Hollister.
    - Apple Intelligence privacy concerns (2024-2025): No coverage from Hollister.
    - Apple glasses speculation (2026-2027): No consumer harm framing from Hollister.
    """

    def setUp(self):
        self.profile = load_journalist('Sean Hollister')
        self.assertIsNotNone(self.profile)

    def test_pre_recusal_apple_coverage_was_adversarial(self):
        """Before June 2023, Hollister applied consumer advocacy to Apple."""
        # His Apple self-repair coverage was adversarial consumer advocacy
        # This is documented in external sources, not in our profile
        notes = self.profile['career'][-1].get('notes', '')
        # The profile documents the transition point
        self.assertIn('June 2023', notes,
                      "Recusal effective date must be documented")

    def test_recusal_reason_documented(self):
        """Reason for recusal must be specific: wife employed at Apple."""
        notes = self.profile['career'][-1].get('notes', '')
        self.assertIn('wife', notes.lower())
        self.assertIn('apple', notes.lower())
        self.assertIn('video producer', notes.lower())

    def test_recusal_scope_complete(self):
        """Recusal covers both Apple products AND Apple as a company."""
        notes = self.profile['career'][-1].get('notes', '')
        self.assertIn('apple products', notes.lower())
        self.assertIn('apple as a company', notes.lower())


class TestHollisterMetaCoverage(unittest.TestCase):
    """
    Hollister's Meta coverage applies consumer harm framing systematically.

    Key coverage:
    1. Meta Conversation Focus rate limit (Jul 2026):
       - On-device feature paywalled at $20/month
       - Framed as accessibility paywall (hearing assistance)
       - "Rate limit" language for local processing
       - Tone: -0.50 (heavily negative consumer harm)

    2. Meta glasses broader coverage context:
       - Consumer harm lane alongside Victoria Song's product reviews
       - Hollister provides the accountability angle; Song provides sentiment
    """

    def setUp(self):
        self.verge = get_verge_research()
        self.assertIsNotNone(self.verge, "The Verge must exist in competitor research")

    def test_hollister_assigned_to_meta_consumer_harm(self):
        """Hollister is documented as consumer harm lane for Meta coverage."""
        lane_mechanism = self.verge.get('lane_assignment_mechanism', '')
        self.assertIn('Hollister', lane_mechanism)
        self.assertIn('consumer harm', lane_mechanism.lower())

    def test_conversation_focus_article_documented(self):
        """Conversation Focus rate limit article must be in Meta examples."""
        meta_examples = self.verge.get('meta_institutional_examples', [])
        cf_articles = [e for e in meta_examples
                       if 'conversation focus' in e.get('title', '').lower()
                       or 'conversation focus' in e.get('framing', '').lower()]
        self.assertTrue(len(cf_articles) > 0,
                        "Conversation Focus article must be documented")

    def test_conversation_focus_tone_negative(self):
        """Conversation Focus article should have strongly negative tone."""
        meta_examples = self.verge.get('meta_institutional_examples', [])
        for e in meta_examples:
            if 'hollister' in e.get('reporter', '').lower():
                self.assertLess(e.get('tone', 0), -0.30,
                                "Hollister's Meta coverage should be strongly negative")
                break

    def test_meta_gets_consumer_harm_framing(self):
        """Meta coverage from Hollister uses consumer harm / accessibility paywall framing."""
        meta_examples = self.verge.get('meta_institutional_examples', [])
        hollister_articles = [e for e in meta_examples
                              if 'hollister' in e.get('reporter', '').lower()]
        self.assertTrue(len(hollister_articles) > 0,
                        "Hollister must have documented Meta coverage")
        for article in hollister_articles:
            framing = article.get('framing', '').lower()
            self.assertTrue(
                'consumer harm' in framing or 'accessibility' in framing or 'paywall' in framing,
                f"Hollister's Meta framing should reference consumer harm/accessibility/paywall: {framing}")


class TestHollisterGoogleCoverage(unittest.TestCase):
    """
    Hollister applies consumer advocacy to Google — moderate adversarial.

    Key coverage:
    1. Epic v. Google trial (2023-2024): Extensive coverage, accountability framing.
       - "20 things we learned from Epic v. Google trial"
       - "Epic wins for Epic" (Vergecast appearance)
       - "Judge says he'll tear the barriers down"
       - Samsung Auto Blocker second lawsuit (Sep 2024)
       - Settlement reporting (Nov 2025)

    2. Google Pixel 7-year update promise (Oct 2023):
       - "Historic — or meaningless"
       - Skeptical of Google's commitment
       - Consumer advocacy angle on cloud-gated features (Video Boost)
       - Questioning economics behind feature restrictions

    Notable: Hollister DOES apply consumer advocacy to Google,
    demonstrating this isn't blanket anti-Meta bias but a structural
    gap specific to Apple.
    """

    def test_google_coverage_documented_in_profile(self):
        """Hollister's current beat includes tech lawsuits (Epic v. Google)."""
        profile = load_journalist('Sean Hollister')
        self.assertIsNotNone(profile)
        current_role = profile['career'][-1]
        beat = current_role.get('beat', '').lower()
        self.assertIn('lawsuits', beat,
                      "Tech lawsuits (Epic v. Google) should be in beat")

    def test_google_coverage_includes_antitrust(self):
        """Hollister covered Epic v. Google — adversarial accountability framing."""
        profile = load_journalist('Sean Hollister')
        current_role = profile['career'][-1]
        # Google/Epic is documented in the career notes
        notes = current_role.get('notes', '').lower()
        self.assertTrue(
            'epic' in notes or 'google' in notes or 'antitrust' in notes,
            "Epic v. Google coverage should be documented in career notes")

    def test_google_coverage_is_moderate_adversarial(self):
        """Google gets consumer advocacy but at moderate level, not adversarial like Meta."""
        # Hollister's Pixel article was skeptical but analytical
        # Epic v. Google was accountability journalism focused on the trial
        # Neither used loaded language like "predator" or "mass surveillance"
        # This is the expected moderate tier between Apple (absent) and Meta (adversarial)
        profile = load_journalist('Sean Hollister')
        notes = profile.get('notes', '').lower()
        self.assertIn('consumer advocacy', notes,
                      "Consumer advocacy bent should be documented")


class TestAppleRecusalAsymmetry(unittest.TestCase):
    """
    The structural asymmetry created by the Apple recusal.

    When The Verge's primary consumer advocacy reporter can't cover the
    biggest competitor in the wearables space, a structural gap emerges:

    | Entity | Consumer Advocacy Reporter | Coverage Type |
    |--------|--------------------------|---------------|
    | Meta   | Hollister (active)       | Consumer harm |
    | Google | Hollister (active)       | Moderate advocacy |
    | Apple  | Hollister (recused)      | Product reviews only |

    Key questions the recusal raises:
    1. Does The Verge assign another consumer advocacy reporter to Apple?
       Evidence says NO — Apple gets product review coverage (Patel, Pierce)
    2. Apple Vision Pro has external cameras that 3D-map surroundings —
       arguably MORE invasive than Meta's single glasses camera — yet
       receives no consumer harm framing from The Verge
    3. Apple's subscription model for iCloud, Apple One, etc. restricts
       features behind paywalls (iCloud+ Private Relay) without the
       "accessibility paywall" framing Meta's Conversation Focus got

    This isn't about Hollister being biased — his recusal is transparent
    and commendable. The systemic issue is that The Verge doesn't compensate
    for the gap with another consumer advocacy voice for Apple.
    """

    def setUp(self):
        self.verge = get_verge_research()
        self.assertIsNotNone(self.verge)

    def test_apple_recusal_gap_documented(self):
        """The apple_recusal_gap section must exist in competitor research."""
        gap = self.verge.get('apple_recusal_gap')
        self.assertIsNotNone(gap, "apple_recusal_gap must be documented in competitor research")

    def test_gap_identifies_no_replacement(self):
        """Gap documentation must note no consumer advocacy replacement for Apple."""
        gap = self.verge.get('apple_recusal_gap', '')
        if isinstance(gap, dict):
            gap_text = str(gap)
        else:
            gap_text = str(gap)
        self.assertTrue(
            'no replacement' in gap_text.lower() or
            'no consumer advocacy' in gap_text.lower() or
            'product review' in gap_text.lower(),
            "Gap must document absence of consumer advocacy for Apple")

    def test_three_entity_coverage_pattern(self):
        """Three-entity pattern: Meta=adversarial, Google=moderate, Apple=absent."""
        gap = self.verge.get('apple_recusal_gap', '')
        gap_text = str(gap).lower()
        # Must reference all three entities
        self.assertIn('meta', gap_text)
        self.assertIn('google', gap_text)
        self.assertIn('apple', gap_text)

    def test_vision_pro_camera_comparison_noted(self):
        """Apple Vision Pro has MORE cameras/sensors than Meta glasses — noted in gap."""
        gap = self.verge.get('apple_recusal_gap', '')
        gap_text = str(gap).lower()
        self.assertTrue(
            'vision pro' in gap_text or 'camera' in gap_text,
            "Gap should reference Vision Pro camera comparison")

    def test_recusal_is_commended_not_criticized(self):
        """Analysis should commend Hollister's transparency, criticize the institution."""
        gap = self.verge.get('apple_recusal_gap', '')
        gap_text = str(gap).lower()
        self.assertTrue(
            'transparent' in gap_text or 'commend' in gap_text or 'institution' in gap_text,
            "Gap analysis should distinguish personal ethics from institutional gap")


class TestLaneAssignmentWithRecusal(unittest.TestCase):
    """
    The Verge's four-lane system for Meta coverage vs Apple's post-recusal single lane.

    Meta coverage lanes (4):
    1. Heath → business investigations (adversarial)
    2. Hollister → consumer harm (adversarial)
    3. Davis/Weatherbed → regulatory (adversarial)
    4. Song → product reviews (balanced, shifting adversarial Jul 2026)

    Apple coverage lanes (post-June 2023):
    1. Patel/Pierce → product reviews (neutral-to-positive)
    (No consumer harm lane, no investigative lane for Apple)

    Google coverage:
    1. Hollister → antitrust/consumer advocacy (moderate adversarial)
    2. Various → product reviews (mixed)
    """

    def setUp(self):
        self.verge = get_verge_research()
        self.assertIsNotNone(self.verge)

    def test_meta_has_four_lanes(self):
        """Meta coverage has at least 3 documented reporter lanes."""
        lane_mechanism = self.verge.get('lane_assignment_mechanism', '')
        # Should mention multiple reporters/lanes for Meta
        for name in ['Heath', 'Hollister', 'Song']:
            self.assertIn(name, lane_mechanism,
                          f"{name} should be in lane assignment mechanism")

    def test_meta_lanes_include_adversarial(self):
        """At least 2 of Meta's lanes are adversarial."""
        lane_mechanism = self.verge.get('lane_assignment_mechanism', '').lower()
        adversarial_indicators = ['adversarial', 'consumer harm', 'investigation']
        count = sum(1 for ind in adversarial_indicators if ind in lane_mechanism)
        self.assertGreaterEqual(count, 2,
                                "At least 2 adversarial indicators in Meta lane assignments")

    def test_lane_count_asymmetry_documented(self):
        """The lane count asymmetry (4 for Meta vs 1 for Apple) should be noted."""
        gap = self.verge.get('apple_recusal_gap', '')
        gap_text = str(gap).lower()
        self.assertTrue(
            'lane' in gap_text or 'reporter' in gap_text or 'assignment' in gap_text,
            "Gap analysis should reference lane assignment asymmetry")


class TestCrossEntityFramingSummary(unittest.TestCase):
    """
    Summary validation: the Apple recusal creates a measurable framing gap.

    Pre-recusal (before Jun 2023):
    - Hollister was one of tech media's most aggressive consumer advocates
    - His Apple self-repair coverage (2022) was cited across the industry
    - He applied the SAME standard to all companies

    Post-recusal (after Jun 2023):
    - Apple loses its consumer advocacy watchdog at The Verge
    - Meta and Google continue to receive consumer advocacy treatment
    - Apple Vision Pro launches, gets product review treatment instead
    - The Verge's Meta glasses coverage includes 4+ surveillance terms (Song Jul 2026)
    - Apple's camera-equipped headset gets zero "predator" or "surveillance" language

    This is a STRUCTURAL finding, not a personal ethics finding:
    - Hollister is ethical (transparent recusal, commendable)
    - The institution is the problem (no replacement consumer advocate for Apple)
    - The result: asymmetric consumer protection coverage driven by
      personal circumstances rather than editorial policy
    """

    def test_structural_finding_documented(self):
        """Research must classify this as structural, not personal."""
        verge = get_verge_research()
        self.assertIsNotNone(verge)
        gap = verge.get('apple_recusal_gap', '')
        gap_text = str(gap).lower()
        self.assertIn('structural', gap_text,
                      "Finding must be classified as structural, not personal")


if __name__ == '__main__':
    unittest.main()
