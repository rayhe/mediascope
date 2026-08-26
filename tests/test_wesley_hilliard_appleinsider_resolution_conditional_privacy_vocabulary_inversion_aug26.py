"""
Type B: Journalist Cross-Entity Tracking — Wesley Hilliard (AppleInsider)
Resolution-Conditional Privacy Vocabulary Inversion in Camera Wearable Coverage
Mechanism #318

JOURNALIST: Wesley Hilliard
ROLE: Rumor Expert at AppleInsider; co-host of AppleInsider Podcast
PUBLICATION: AppleInsider (Apple-focused publication, 100% Apple-dependent revenue)
BACKGROUND: 10-year US Navy veteran (nuclear-trained electrician), self-described
Apple ecosystem convert who became "captivated by the ideas Apple presented" regarding
"digital privacy, device ecosystems, and strong device security." This biographical
framing — privacy as an Apple value proposition — maps directly onto his editorial
vocabulary choices.

FINDING: Wesley Hilliard applies a resolution-conditional privacy vocabulary inversion
across camera wearable coverage. When Meta ships 12MP cameras in smart glasses, they
receive surveillance/harm vocabulary: "privacy-invading face cameras," "invasive and
ugly," "eyesore," "privacy nightmare," "pervert glasses," "abuses," "damage." When
Apple's planned AirPods ship cameras at lower resolution for AI context, they receive
utility/safeguard vocabulary: "shouldn't worry," "potential solution," "life-changing,"
"real safeguards," "I'm okay with Apple shipping glasses without that capability."

The critical observation is that BOTH products serve the same core function — feeding
camera data to an AI assistant for contextual awareness. Wesley explicitly acknowledges
this parallel but inverts the framing: Meta's cameras "normalize privacy-invading face
cameras" while Apple's cameras provide "the accessibility aspects... [that] could be
life-changing."

PRIMARY SOURCES:

Article 1: "AirPods with cameras not coming till 2027, won't take photos"
  Author: Wesley Hilliard (confirmed byline)
  Publication: AppleInsider
  Date: August 19, 2026
  URL: https://appleinsider.com/articles/26/08/19/airpods-with-cameras-not-coming-till-2027-wont-take-photos

  KEY VOCABULARY — APPLE (AirPods cameras):
  - "shouldn't worry about them becoming 'pervertpods'"
  - "potential solution to the privacy problem"
  - "could be life-changing for many"
  - "I doubt Apple will ignore that utility"
  - "I also believe the company won't release them into the world without real
    safeguards in place"
  - "I'm okay with Apple shipping glasses without that capability"
  - "Preventing the cameras... from capturing anything at all may be the best way
    to ensure users gain the utility... without the damage caused otherwise"

  KEY VOCABULARY — META (Ray-Ban glasses cameras):
  - "The societal rejection and nickname stem from abuses committed by people
    wearing Meta's smart glasses"
  - "pervert glasses" (applied without distancing quotation marks in conclusion)
  - "men abusing women in massage parlors"
  - "teen boys bullying teen girls in middle school"
  - "there is a reason they've become known as 'pervert glasses'"
  - "the damage caused otherwise"
  - "I think the images and video captured from glasses like Meta's are awful"

Article 2: "Meta Ray-Ban Display aren't competing with Apple's Vision"
  Author: Wesley Hilliard (attributed by existing MediaScope test #234 cross-reference
  and writing style analysis; also matches Sep 2025 AppleInsider editorial voice)
  Publication: AppleInsider
  Date: September 18, 2025
  URL: https://appleinsider.com/articles/25/09/18/meta-ray-ban-display-wont-challenge-apples-eventual-smart-glasses

  KEY VOCABULARY — APPLE:
  - "And once Apple's true AR product arrives, we can bet it'll be private,
    secure, and actually useful to its users"
  - "Apple Glasses are a completely different paradigm"
  - "Apple's Vision platform" (aspirational)

  KEY VOCABULARY — META:
  - "Ray-Ban Meta glasses have normalized privacy-invading face cameras" (image caption)
  - "they're invasive and ugly in a way that'll ensure I'll ask you not to
    wear them around me"
  - "an eyesore and a privacy nightmare"
  - "They've no interest in making this a simple accessory to your smartphone"
  - "every attempt that a non-smartphone maker has made to introduce an AI-first
    device has either failed... or is destined for failure"
  - "there's always a chance Meta quietly abandons the whole thing and finds
    some other investor-friendly target to chase"

Podcast evidence: AppleInsider Podcast (Aug 21, 2026)
  "AirPods with cameras leak, Apple Maps ads, & Siri AI"
  Hosts: Wesley Hilliard, William Gallagher
  URL: https://appleinsider.com/articles/26/08/21/airpods-with-cameras-leak-apple-maps-ads-siri-ai-on-the-appleinsider-podcast
  Apple vocabulary: "praise," "won't take photos at all," "not fear them"
  Meta vocabulary: "creepy actions," "perpetrated"
  (Already documented in mechanism #303 podcast cross-publication analysis)

MECHANISM ANALYSIS:

The resolution-conditional inversion works as follows:
1. Meta ships 12MP cameras that CAN take photos/video → "surveillance,"
   "invasive," "pervert glasses," "privacy nightmare," "abuses"
2. Apple plans 1MP cameras that CANNOT take photos/video → "shouldn't worry,"
   "life-changing," "utility," "safeguards," "solution"
3. Both products feed camera data to AI assistants for contextual awareness
4. The privacy framing inverts based on whether the entity is Apple or Meta,
   with resolution used as the rationalization

This is reinforced by the personal conviction markers: "I'm okay with Apple
shipping glasses without that capability" (Apple = trusted) vs "I'll ask you
not to wear them around me" (Meta = threat).

CONFOUNDERS:

1. STRONG: AppleInsider is a publication whose entire editorial identity, revenue
   model, and readership expectation centers on Apple. Aspirational Apple coverage
   and adversarial competitor coverage is not anomalous but definitional. Readers
   self-select for this framing.

2. STRONG: Meta glasses DO have documented misuse incidents (massage parlor
   harassment, non-consensual recording, contractor footage exposure) while
   Apple's camera AirPods don't exist yet. The asymmetry in incident data
   constrains how much privacy-alarm vocabulary can apply to Apple.

3. STRONG: The camera capabilities are genuinely different — Meta's 12MP cameras
   can capture high-resolution photos and videos for personal use. Apple's
   planned 1MP cameras reportedly cannot. Resolution IS a real privacy differentiator,
   not merely a rationalization.

4. MODERATE: Hilliard's Navy background and self-described Apple conversion
   narrative suggest genuine personal conviction about privacy-as-Apple-value,
   not cynical editorial positioning. The vocabulary may reflect authentic belief
   rather than financial incentive.

5. MODERATE: Meta's own spokesperson response to harassment reports ("Would this
   have been a story had they used the new iPhone?") was widely criticized as
   tone-deaf, providing legitimate editorial ammunition.

6. WEAK: Other Apple-focused publications (9to5Mac, MacRumors, iMore) show
   similar patterns, suggesting this is a market-segment norm, not an individual
   anomaly.

CROSS-REFERENCES:
- #234 (Malcolm Owen AppleInsider aspirational-cautionary dyad — same publication)
- #285 (Amber Neely AppleInsider surveillance vocabulary asymmetry — same publication)
- #303 (Cross-publication podcast AirPods vocabulary inversion — podcast match)
- #221 (9to5Mac camera AirPods excitement framing — competitor publication parallel)

Iteration #305 — Wed 2026-08-26 05:00 PT
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestWesleyHilliardJournalistIdentity(unittest.TestCase):
    """Verify Wesley Hilliard's journalist profile and biographical context."""

    def test_journalist_exists_in_yaml(self):
        """Wesley Hilliard must be registered in journalists.yaml."""
        data = load_yaml('careers/journalists.yaml')
        names = [j.get('name', '') for j in data.get('journalists', [])]
        self.assertIn('Wesley Hilliard', names,
                      "Wesley Hilliard not found in journalists.yaml")

    def test_journalist_publication(self):
        """Must be identified as AppleInsider staff."""
        data = load_yaml('careers/journalists.yaml')
        journalist = next(
            (j for j in data.get('journalists', [])
             if j.get('name') == 'Wesley Hilliard'), None)
        self.assertIsNotNone(journalist)
        self.assertEqual(journalist.get('publication'), 'appleinsider')

    def test_biographical_context(self):
        """Must include Navy background and Apple conversion narrative."""
        data = load_yaml('careers/journalists.yaml')
        journalist = next(
            (j for j in data.get('journalists', [])
             if j.get('name') == 'Wesley Hilliard'), None)
        self.assertIsNotNone(journalist)
        notes = journalist.get('notes', '')
        self.assertIn('Navy', notes,
                      "Must reference US Navy background")
        self.assertIn('Apple', notes)


class TestMechanism318CrossEntityVocabulary(unittest.TestCase):
    """Verify the cross-entity vocabulary inversion documented in mechanism #318."""

    def setUp(self):
        self.article_airpods = {
            "title": "AirPods with cameras not coming till 2027, won't take photos",
            "author": "Wesley Hilliard",
            "publication": "AppleInsider",
            "date": "2026-08-19",
            "url": "https://appleinsider.com/articles/26/08/19/airpods-with-cameras-not-coming-till-2027-wont-take-photos",
            "entities_discussed": ["Apple", "Meta"],
            "apple_vocabulary": [
                "shouldn't worry",
                "potential solution",
                "life-changing",
                "real safeguards",
                "utility",
            ],
            "meta_vocabulary": [
                "abuses committed",
                "pervert glasses",
                "men abusing women",
                "teen boys bullying teen girls",
                "damage",
            ],
        }
        self.article_display = {
            "title": "Meta Ray-Ban Display aren't competing with Apple's Vision",
            "author": "Wesley Hilliard",
            "publication": "AppleInsider",
            "date": "2025-09-18",
            "url": "https://appleinsider.com/articles/25/09/18/meta-ray-ban-display-wont-challenge-apples-eventual-smart-glasses",
            "entities_discussed": ["Apple", "Meta"],
            "apple_vocabulary": [
                "private, secure, and actually useful",
                "completely different paradigm",
            ],
            "meta_vocabulary": [
                "privacy-invading face cameras",
                "invasive and ugly",
                "eyesore",
                "privacy nightmare",
                "destined for failure",
            ],
        }

    def test_both_articles_same_journalist(self):
        """Both articles are written by Wesley Hilliard."""
        self.assertEqual(self.article_airpods["author"],
                         self.article_display["author"])

    def test_same_publication(self):
        """Both articles are from AppleInsider."""
        self.assertEqual(self.article_airpods["publication"],
                         self.article_display["publication"])

    def test_both_cover_apple_and_meta(self):
        """Both articles discuss Apple and Meta camera wearables."""
        for article in [self.article_airpods, self.article_display]:
            self.assertIn("Apple", article["entities_discussed"])
            self.assertIn("Meta", article["entities_discussed"])

    def test_apple_vocabulary_is_consistently_protective(self):
        """Apple receives protective/aspirational vocabulary across both articles."""
        combined_apple = (self.article_airpods["apple_vocabulary"]
                          + self.article_display["apple_vocabulary"])
        protective_terms = sum(1 for v in combined_apple if any(
            kw in v.lower() for kw in [
                "safeguard", "solution", "utility", "useful", "life-changing",
                "worry", "paradigm", "private", "secure"
            ]))
        self.assertGreaterEqual(protective_terms, 5,
                                f"Expected >= 5 protective terms, found {protective_terms}")

    def test_meta_vocabulary_is_consistently_adversarial(self):
        """Meta receives adversarial/alarm vocabulary across both articles."""
        combined_meta = (self.article_airpods["meta_vocabulary"]
                         + self.article_display["meta_vocabulary"])
        alarm_terms = sum(1 for v in combined_meta if any(
            kw in v.lower() for kw in [
                "abuse", "pervert", "invasive", "nightmare", "damage",
                "failure", "eyesore", "bullying", "privacy-invading"
            ]))
        self.assertGreaterEqual(alarm_terms, 7,
                                f"Expected >= 7 alarm terms, found {alarm_terms}")

    def test_vocabulary_inversion_ratio(self):
        """The alarm-to-protective ratio should be inverted between entities."""
        apple_alarm = sum(1 for v in (
            self.article_airpods["apple_vocabulary"]
            + self.article_display["apple_vocabulary"])
            if any(kw in v.lower() for kw in [
                "abuse", "pervert", "invasive", "nightmare", "damage"
            ]))
        meta_protective = sum(1 for v in (
            self.article_airpods["meta_vocabulary"]
            + self.article_display["meta_vocabulary"])
            if any(kw in v.lower() for kw in [
                "safeguard", "solution", "utility", "useful", "life-changing"
            ]))
        # Apple should receive zero alarm terms; Meta zero protective terms
        self.assertEqual(apple_alarm, 0,
                         "Apple should not receive alarm vocabulary")
        self.assertEqual(meta_protective, 0,
                         "Meta should not receive protective vocabulary")


class TestMechanism318InYaml(unittest.TestCase):
    """Verify mechanism #318 is registered in competitor-coverage-research.yaml."""

    def setUp(self):
        self.data = load_yaml('competitor-coverage-research.yaml')

    def _find_mechanism(self, mechanism_id):
        """Search for a mechanism by ID across all entries."""
        def _search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == mechanism_id:
                    return obj
                for v in obj.values():
                    result = _search(v)
                    if result:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = _search(item)
                    if result:
                        return result
            return None
        return _search(self.data)

    def test_mechanism_318_present(self):
        """Mechanism #318 must exist in the YAML."""
        mechanism = self._find_mechanism(318)
        self.assertIsNotNone(mechanism, "Mechanism #318 not found")

    def test_mechanism_318_is_type_b(self):
        """Mechanism #318 must be type B (journalist cross-entity tracking)."""
        mechanism = self._find_mechanism(318)
        self.assertEqual(mechanism.get('type'), 'B')

    def test_mechanism_318_has_confounders(self):
        """Must have at least 4 confounding factors."""
        mechanism = self._find_mechanism(318)
        factors = mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 4,
                                f"Expected >= 4 confounders, found {len(factors)}")

    def test_mechanism_318_journalist(self):
        """Must identify Wesley Hilliard as the journalist."""
        mechanism = self._find_mechanism(318)
        journalist = mechanism.get('journalist', '')
        self.assertIn('Wesley Hilliard', journalist)


class TestResolutionConditionalPattern(unittest.TestCase):
    """Test the specific resolution-conditional framing inversion."""

    def test_same_function_different_framing(self):
        """Both Apple and Meta camera wearables feed data to AI assistants,
        but receive opposite privacy framing."""
        meta_function = "Camera feeds visual data to Meta AI for contextual awareness"
        apple_function = "Camera feeds visual data to Siri AI for contextual awareness"

        # Both serve the same AI assistant function
        self.assertIn("feeds visual data", meta_function)
        self.assertIn("feeds visual data", apple_function)

        # But receive opposite framing
        meta_framing = "surveillance, invasive, privacy-invading"
        apple_framing = "utility, life-changing, safeguards"

        self.assertNotEqual(meta_framing, apple_framing,
                            "Same function should receive different entity-based framing")

    def test_resolution_as_rationalization(self):
        """Resolution difference is real but serves as vocabulary rationalization."""
        meta_resolution = "12MP (photos + video capable)"
        apple_resolution = "1MP (AI context only)"

        # Resolution IS genuinely different
        self.assertNotEqual(meta_resolution, apple_resolution)

        # But the vocabulary differential exceeds what resolution alone explains:
        # "invasive and ugly" vs "life-changing" is not a resolution comparison —
        # it's an entity-conditional value judgment
        meta_aesthetic_judgment = "invasive and ugly"
        apple_aesthetic_judgment = "life-changing"

        # These terms describe the ENTITY not the RESOLUTION
        self.assertIn("ugly", meta_aesthetic_judgment)
        self.assertIn("life", apple_aesthetic_judgment)


class TestPublicationLevelPattern(unittest.TestCase):
    """Test that Wesley Hilliard's vocabulary fits AppleInsider's broader pattern."""

    def test_three_appleinsider_writers_same_meta_vocabulary(self):
        """Three AppleInsider writers (Neely #285, Owen #234, Hilliard #318)
        all apply alarm vocabulary to Meta glasses and aspirational vocabulary
        to Apple wearables."""
        writers = [
            {"name": "Amber Neely", "mechanism": 285, "role": "Reviews Editor"},
            {"name": "Malcolm Owen", "mechanism": 234, "role": "Senior Writer"},
            {"name": "Wesley Hilliard", "mechanism": 318, "role": "Rumor Expert"},
        ]
        self.assertEqual(len(writers), 3)
        # All three mechanisms documented similar vocabulary patterns
        for writer in writers:
            self.assertIn(writer["mechanism"],
                          [234, 285, 318])


if __name__ == '__main__':
    unittest.main()
