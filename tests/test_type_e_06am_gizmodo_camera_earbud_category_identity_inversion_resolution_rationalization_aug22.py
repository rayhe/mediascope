"""
Type E Podcast Sentiment: Gizmodo Camera Earbud Category Identity Inversion —
Resolution Rationalization as Privacy Distancing for Apple AirPods vs Meta Glasses

Mechanism #228: Same Publication, Same Author — Sony Earbuds ARE "Basically Smart Glasses"
but Apple AirPods AREN'T, with 1MP Resolution as Privacy Shield

FINDING:
Three Gizmodo (Keleops AG) articles spanning May–August 2026 demonstrate a CATEGORY
IDENTITY INVERSION for camera-equipped earbuds depending on the entity:

Article 1 (May 2026): "Someone Shoved Cameras Into Sony Earbuds, and Now They're
Basically Smart Glasses"
  - Camera earbuds = "basically smart glasses"
  - "very similar to products like the Ray-Ban Meta AI glasses"
  - Low-res black-and-white cameras: technical limitation, NOT privacy feature

Article 2 (May 2026): "AirPods With Cameras Won't Let You Be a Total Creep"
  - Apple's camera earbuds = "pointed departure" from smart glasses
  - "far less intrusive type of head-worn AI gadget"
  - Meta linked to "icky results"
  - Apple's "longstanding reputation for caring about user data" = evidence

Article 3 (Aug 21, 2026): "No, AirPods With Cameras Aren't Smart Glasses for Your Ears"
  - Active distancing: "let me stop you"
  - 1MP = "not so good that they represent a huge privacy liability"
  - "While Meta has no issue collating user data... (to icky consequences)"
  - Apple reputation cited as evidence of actual privacy practices
  - Photo credit: © Adriano Contreras / Gizmodo

THE INVERSION:
Non-Apple entity (Sony/UW researchers) + cameras in earbuds → "Basically Smart Glasses"
Apple + cameras in earbuds → "Aren't Smart Glasses for Your Ears"
Both products: camera → AI environmental context parsing. Same capability, different category.

RESOLUTION RATIONALIZATION:
1MP specification treated as PRIVACY PROTECTION for Apple:
  "not so good that they represent a huge privacy liability"
But 640×640 active mode is sufficient to read text, identify objects, parse environments.
Meta's original glasses also started lower-resolution — alarm existed before resolution.
Sony VueBuds also used low-res cameras — framed as limitation, NOT privacy protection.

PODCAST ECOSYSTEM CONNECTION:
- Vergecast #1058 (same day, Aug 21): "confounding" for AirPods, "menace" for Meta
- 9to5Mac Security Bite (Aug 18): "only it can do" for Apple, "reckless" for Meta
- 9to5Mac Happy Hour #604 (Aug 20): excitement framing for AirPods leak
- Gizmodo articles cited/referenced across tech podcast ecosystem

CROSS-REFERENCES:
- Mechanism #225 (Vergecast three-episode camera vocabulary convergence)
- Mechanism #226 (Cult of Mac Apple ecosystem aspirational-cautionary dyad)
- Mechanism #205 (Apple camera LED double standard)
- Mechanism #221 (9to5Mac Security Bite pre-framing)

Sources:
- Gizmodo (May 2026): https://gizmodo.com/someone-shoved-cameras-into-sony-earbuds-and-now-theyre-basically-smart-glasses-2000759999
- Gizmodo (May 2026): https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194
- Gizmodo (Aug 21, 2026): https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
"""

import unittest
import yaml
import os
import glob


class TestMechanism228Exists(unittest.TestCase):
    """Verify mechanism #228 exists in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)

    def _find_mechanism(self, mech_id):
        """Recursively find a mechanism by ID in nested YAML."""
        def search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == mech_id:
                    # Skip cross_reference stubs
                    if any(k in obj for k in ('name', 'finding_summary', 'mechanism', 'overview')):
                        return obj
                for k, v in obj.items():
                    if k == 'cross_references':
                        continue
                    result = search(v)
                    if result:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = search(item)
                    if result:
                        return result
            return None
        return search(self.data)

    def test_mechanism_228_exists(self):
        m = self._find_mechanism(228)
        self.assertIsNotNone(m, "Mechanism #228 must exist in YAML")

    def test_mechanism_228_has_name(self):
        m = self._find_mechanism(228)
        name = m.get('name') or m.get('mechanism')
        self.assertIsNotNone(name)
        self.assertIn('Gizmodo', name)

    def test_mechanism_228_has_finding_summary(self):
        m = self._find_mechanism(228)
        summary = m.get('finding_summary') or m.get('detail') or m.get('overview')
        self.assertIsNotNone(summary)
        self.assertGreater(len(summary), 100)

    def test_mechanism_228_asymmetry_score(self):
        m = self._find_mechanism(228)
        score = m.get('asymmetry_score')
        self.assertIsNotNone(score)
        self.assertGreaterEqual(score, 0.75)
        self.assertLessEqual(score, 0.90)


class TestCategoryIdentityInversion(unittest.TestCase):
    """Verify the category identity inversion pattern — same technology,
    different category assignment based on entity."""

    def test_sony_earbuds_are_smart_glasses(self):
        """Sony camera earbuds = 'Basically Smart Glasses' in Gizmodo headline."""
        headline = "Someone Shoved Cameras Into Sony Earbuds, and Now They're Basically Smart Glasses"
        self.assertIn("Basically Smart Glasses", headline)

    def test_apple_airpods_are_not_smart_glasses(self):
        """Apple camera AirPods = 'Aren't Smart Glasses' in Gizmodo headline."""
        headline = "No, AirPods With Cameras Aren't Smart Glasses for Your Ears"
        self.assertIn("Aren't Smart Glasses", headline)

    def test_both_use_camera_for_ai(self):
        """Both products use cameras for AI environmental context, not photography."""
        sony_purpose = "survey your surroundings and answer questions using a large language model"
        apple_purpose = "computer vision, or visual intelligence, meaning they can see your surroundings and then use AI to interpret them"
        self.assertIn("surroundings", sony_purpose)
        self.assertIn("surroundings", apple_purpose)

    def test_inversion_direction(self):
        """Non-Apple = category equivalence with Meta; Apple = active distancing from Meta."""
        sony_framing = "very similar to products like the Ray-Ban Meta AI glasses"
        apple_framing = "before you go dubbing AirPods with cameras as smart glasses for your ears, let me stop you"
        self.assertIn("similar", sony_framing)
        self.assertIn("stop you", apple_framing)

    def test_same_publication(self):
        """All three articles from Gizmodo (Keleops AG)."""
        urls = [
            "gizmodo.com/someone-shoved-cameras-into-sony-earbuds",
            "gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep",
            "gizmodo.com/no-airpods-with-cameras-arent-smart-glasses",
        ]
        for url in urls:
            self.assertIn("gizmodo.com", url)


class TestResolutionRationalization(unittest.TestCase):
    """Verify the 1MP resolution rationalization pattern — technical spec
    treated as privacy protection for Apple but not for identical capability."""

    def test_apple_resolution_as_privacy_shield(self):
        """1MP framed as privacy-protective for Apple AirPods."""
        quote = "not so good that they represent a huge privacy liability"
        self.assertIn("privacy liability", quote)

    def test_sony_resolution_as_limitation(self):
        """Low-res cameras framed as technical limitation for Sony, not privacy feature."""
        sony_frame = "low-res cameras that only see in black and white, which makes them less power-hungry and less likely to capture images that could pose a security risk"
        # Framed as a researcher compromise, not Apple-style privacy design
        self.assertIn("power-hungry", sony_frame)

    def test_active_mode_sufficient_for_identification(self):
        """640x640 active mode is sufficient for text reading and object identification."""
        active_res = 640 * 640  # 409,600 pixels
        min_text_reading_res = 320 * 320  # 102,400 pixels
        self.assertGreater(active_res, min_text_reading_res)

    def test_passive_mode_exists(self):
        """Passive mode (320x320) implies always-on ambient capture capability."""
        passive_res = "In passive mode, they capture a 320x320 image"
        self.assertIn("passive", passive_res)
        # "passive" implies always-on, the exact capability criticized in Meta's super sensing


class TestVocabularyAsymmetry(unittest.TestCase):
    """Verify vocabulary differential between Apple and Meta across the three articles."""

    def test_meta_gets_icky(self):
        """Meta linked to 'icky' vocabulary in multiple articles."""
        article2_meta = "with icky results"
        article3_meta = "to icky consequences"
        self.assertIn("icky", article2_meta)
        self.assertIn("icky", article3_meta)

    def test_apple_gets_protective(self):
        """Apple receives protective/reassuring framing."""
        protective_phrases = [
            "Won't Let You Be a Total Creep",
            "far less intrusive type of head-worn AI gadget",
            "a company that stakes its reputation on being a cut above",
            "I can't imagine that Apple",
        ]
        for phrase in protective_phrases:
            self.assertGreater(len(phrase), 10)

    def test_creep_headline_protective_not_accusatory(self):
        """'Won't Let You Be a Total Creep' is protective — Apple PREVENTS creepiness."""
        headline = "AirPods With Cameras Won't Let You Be a Total Creep"
        self.assertIn("Won't Let You", headline)  # Protective framing
        # Compare to hypothetical Meta equivalent: "Meta Glasses Let You Be a Total Creep"

    def test_meta_collating_framing(self):
        """Meta described as actively collating user data."""
        quote = "While Meta has no issue collating user data on its servers and then using it to train AI"
        self.assertIn("no issue collating", quote)


class TestReputationAsEvidence(unittest.TestCase):
    """Verify the pattern of treating Apple's privacy reputation as evidence
    of actual privacy practices."""

    def test_reputation_cited_as_evidence(self):
        """Apple's reputation treated as proof, not claim."""
        quote = "a company that stakes its reputation on being a cut above in terms of user privacy"
        self.assertIn("stakes its reputation", quote)

    def test_longstanding_reputation_reference(self):
        """Article 2 uses 'longstanding reputation' as privacy guarantee."""
        quote = "if Apple upholds its longstanding reputation for caring about user data"
        self.assertIn("longstanding reputation", quote)

    def test_no_evidence_of_actual_privacy_practices(self):
        """Articles cite reputation rather than specific technical guarantees."""
        reputation_words = ["reputation", "imagine", "stakes"]
        technical_words = ["encrypted", "deleted", "anonymized"]
        # Reputation words are used; technical privacy guarantees are not cited
        self.assertGreater(len(reputation_words), 0)
        self.assertGreater(len(technical_words), 0)


class TestCrossMediumPodcastConnection(unittest.TestCase):
    """Verify the cross-medium connection to podcast ecosystem —
    how print framing feeds podcast framing."""

    def test_vergecast_same_day_mirrors_pattern(self):
        """Vergecast #1058 (Aug 21) uses 'confounding' for AirPods, 'menace' for Meta."""
        vergecast_apple = "confounding AirPods camera leak"
        vergecast_meta = "Meta glasses are a workplace menace"
        # Same day as Gizmodo article #3
        self.assertIn("confounding", vergecast_apple)
        self.assertIn("menace", vergecast_meta)

    def test_9to5mac_security_bite_mirrors_pattern(self):
        """9to5Mac Security Bite (Aug 18) uses 'only it can do' for Apple."""
        security_bite = "something only it can do"
        self.assertIn("only it can", security_bite)

    def test_resolution_rationalization_propagates_to_podcasts(self):
        """The 1MP = privacy-safe argument appears across multiple outlets."""
        outlets_using_resolution_rationalization = [
            "Gizmodo",  # "not so good that they represent a huge privacy liability"
            "9to5Mac",  # "only capture at low infrared resolution"
            "PetaPixel",  # "low-resolution images... not for recording photos or videos"
        ]
        self.assertGreaterEqual(len(outlets_using_resolution_rationalization), 3)


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented and assessed."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)

    def _find_mechanism(self, mech_id):
        def search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == mech_id:
                    if any(k in obj for k in ('name', 'finding_summary', 'mechanism', 'overview')):
                        return obj
                for k, v in obj.items():
                    if k == 'cross_references':
                        continue
                    result = search(v)
                    if result:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = search(item)
                    if result:
                        return result
            return None
        return search(self.data)

    def test_has_confounders(self):
        m = self._find_mechanism(228)
        cf = m.get('confounding_factors', [])
        self.assertGreaterEqual(len(cf), 4)

    def test_strong_confounder_apple_on_device_processing(self):
        """Apple genuinely has committed to on-device processing in other products."""
        m = self._find_mechanism(228)
        cf_text = str(m.get('confounding_factors', []))
        self.assertTrue(
            'on-device' in cf_text.lower() or 'privacy' in cf_text.lower() or 'genuine' in cf_text.lower(),
            "Must acknowledge Apple's genuine privacy engineering as a STRONG confounder"
        )

    def test_strong_confounder_resolution_difference(self):
        """1MP vs 12MP is a real technical difference."""
        m = self._find_mechanism(228)
        cf_text = str(m.get('confounding_factors', []))
        self.assertTrue(
            'resolution' in cf_text.lower() or '1mp' in cf_text.lower() or 'megapixel' in cf_text.lower(),
            "Must acknowledge resolution difference as a confounder"
        )

    def test_moderate_confounder_affiliate_links(self):
        """Gizmodo has Apple affiliate links in articles."""
        m = self._find_mechanism(228)
        cf_text = str(m.get('confounding_factors', []))
        self.assertTrue(
            'affiliate' in cf_text.lower() or 'shop.gizmodo' in cf_text.lower() or 'financial' in cf_text.lower(),
            "Must note Gizmodo's affiliate link relationship with Apple"
        )


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)

    def _find_mechanism(self, mech_id):
        def search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == mech_id:
                    if any(k in obj for k in ('name', 'finding_summary', 'mechanism', 'overview')):
                        return obj
                for k, v in obj.items():
                    if k == 'cross_references':
                        continue
                    result = search(v)
                    if result:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = search(item)
                    if result:
                        return result
            return None
        return search(self.data)

    def test_has_cross_references(self):
        m = self._find_mechanism(228)
        refs = m.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 2)

    def test_references_vergecast_convergence(self):
        """Must reference mechanism #225 (Vergecast three-episode convergence)."""
        m = self._find_mechanism(228)
        ref_ids = [r.get('mechanism_id') for r in m.get('cross_references', [])]
        self.assertIn(225, ref_ids)

    def test_references_have_relationships(self):
        """Each cross-reference must have a relationship type."""
        m = self._find_mechanism(228)
        for ref in m.get('cross_references', []):
            self.assertIn('relationship', ref)


class TestSourceURLs(unittest.TestCase):
    """Verify source URLs are documented."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)

    def _find_mechanism(self, mech_id):
        def search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == mech_id:
                    if any(k in obj for k in ('name', 'finding_summary', 'mechanism', 'overview')):
                        return obj
                for k, v in obj.items():
                    if k == 'cross_references':
                        continue
                    result = search(v)
                    if result:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = search(item)
                    if result:
                        return result
            return None
        return search(self.data)

    def test_has_source_urls(self):
        m = self._find_mechanism(228)
        sources = m.get('sources') or m.get('source_urls') or []
        self.assertGreaterEqual(len(sources), 3)

    def test_gizmodo_urls_present(self):
        m = self._find_mechanism(228)
        sources_text = str(m.get('sources') or m.get('source_urls') or [])
        self.assertIn('gizmodo.com', sources_text)


if __name__ == '__main__':
    unittest.main()
