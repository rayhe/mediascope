"""
Cross-entity analysis: Adi Robertson (The Verge)
Created: 2026-08-08 05:00 PT (Type B: Journalist Cross-Entity Tracking)

The Verge's longest-tenured editorial staff member (14+ years, founding member
Nov 2011) and the publication's primary VR/AR/XR voice post-Alex Heath departure
(Sep 2025). Her single-publication career makes her a pure institutional control
— no multi-outlet migration DiD is available, but she demonstrates how The
Verge's *internal* editorial framework shapes XR coverage.

KEY FINDING — THE COMFORT/DISCOMFORT PARADOX:
Robertson applies a comfort-based evaluation framework that systematically
disadvantages Meta:

  Meta Quest Pro (Nov 2022):
    Score: 2/5
    Language: "irredeemably bad software," "uniquely tortuous" strap,
             "grainy" display, "doesn't look remotely like the real world"
    Verdict: "launched without plan or purpose"

  Magic Leap 2 (Oct 2022, same year):
    Score: No numeric score (hands-on)
    Language: "A significantly improved device," "sharp and vibrant,"
             "text is easy to read"
    Context: Also has wired puck, limited FoV, enterprise-only pricing

  Magic Leap One (Aug 2018):
    Language: "surprisingly comfortable"
    Context: $2,295, massive hype-reality gap

  Apple Vision Pro (Jun 2023):
    Language: Wrote the Verge announcement article
    Context: 12 cameras, 5 sensors, 6 mics — far more surveillance
             hardware than Ray-Ban Meta. No "if you're okay with Apple"

  Meta Quest 2 (Oct 2020):
    Language: "The new default for VR, if you're okay with Facebook"
    Context: Privacy-conditional framing in headline/lede

  Meta Quest 3 (Sep 2023):
    Language: "An upgraded VR game console with an extra feature...
              I can't tell if Meta is trying too hard"
    Context: Dismissive, reductive framing

KEY FINDING — THE PRIVACY CONDITIONAL PATTERN:
Robertson applies privacy-conditional language exclusively to Meta products:
  - Quest 2: "if you're okay with Facebook" (headline-level)
  - Ray-Ban Stories: "camera-toting glasses" (surveillance-adjacent)
  - Apple Vision Pro: NO privacy conditional despite 12 cameras + 5 sensors
  - Magic Leap: NO privacy conditional despite integrated cameras
  - Snap Spectacles: NO privacy conditional despite 4 cameras

This mirrors the Chokkattu/Ashworth "Creep Paradox" found on WIRED's product
desk — the privacy frame is applied ONLY to Meta, never to competitors with
equal or greater surveillance hardware.

INSTITUTIONAL AMPLIFICATION:
Post-Alex Heath departure (Sep 2025), Robertson becomes The Verge's primary
XR/RL voice. Her framing patterns are no longer one reporter's perspective
— they ARE The Verge's perspective on Meta's wearables strategy.

PMC ACQUISITION CONTEXT (Jun 2026):
Under Penske Media Corporation ownership, Robertson's coverage direction on
XR is the primary test case for whether PMC's entertainment media portfolio
(Variety, Rolling Stone, Deadline — with Apple TV+ ad revenue dependencies)
changes The Verge's Meta coverage posture.

Sources:
  - Wikipedia: Meta Quest Pro reception (Adi Robertson, The Verge, 2/5 review)
  - Techmeme: Quest 3 hands-on (Sep 27, 2023, Adi Robertson / The Verge)
  - Techmeme: Quest 2 review (Sep 16, 2020, Adi Robertson / The Verge)
  - Techmeme: Meta Connect 2024 (Adi Robertson / The Verge, publisher value)
  - Mixed-News.com: Magic Leap 2 hands-on review roundup (Robertson quoted)
  - Wareable.com: Magic Leap One first impressions roundup (Robertson quoted)
  - TechTaffy: Apple Vision Pro announcement by Adi Robertson / The Verge
  - TWiT Tech News Weekly Episode 200: Robertson on Ray-Ban Stories
  - KGOnTech: AWE 2024 panel with Adi Robertson as panelist
  - Journalists YAML career profile: 14+ year tenure, Cornell BA
"""
import yaml
import os
import unittest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestRobertsonProfileExists(unittest.TestCase):
    """Adi Robertson exists in the journalists career database."""

    @classmethod
    def setUpClass(cls):
        cls.careers = load_yaml('careers/journalists.yaml')
        cls.journalists = cls.careers.get('journalists', cls.careers) \
            if isinstance(cls.careers, dict) else cls.careers

    def _find_robertson(self):
        items = self.journalists if isinstance(self.journalists, list) else []
        for j in items:
            if isinstance(j, dict) and j.get('name') == 'Adi Robertson':
                return j
        # fallback: search in all dicts
        if isinstance(self.journalists, dict):
            for key, val in self.journalists.items():
                if isinstance(val, list):
                    for j in val:
                        if isinstance(j, dict) and j.get('name') == 'Adi Robertson':
                            return j
        return None

    def test_robertson_in_database(self):
        """Adi Robertson exists in the journalist career database."""
        self.assertIsNotNone(self._find_robertson())

    def test_robertson_single_publication(self):
        """Robertson is a single-publication journalist (The Verge only)."""
        j = self._find_robertson()
        self.assertIsNotNone(j)
        notes = j.get('notes', '')
        # Either has single-publication flag or notes mention single-publication
        career = j.get('career', [])
        verge_entries = [c for c in career if isinstance(c, dict)
                         and 'verge' in str(c.get('publication', '')).lower()]
        self.assertGreater(len(verge_entries), 0,
                           "Robertson should have Verge career entries")

    def test_robertson_vr_ar_beat(self):
        """Robertson covers VR/AR/XR beat."""
        j = self._find_robertson()
        self.assertIsNotNone(j)
        notes = str(j.get('notes', ''))
        career_str = str(j.get('career', ''))
        combined = notes + career_str
        vr_ar_terms = ['VR', 'AR', 'virtual reality', 'augmented reality',
                       'mixed reality', 'Quest', 'XR']
        found = any(t in combined for t in vr_ar_terms)
        self.assertTrue(found,
                        "Robertson's profile should reference VR/AR coverage")

    def test_robertson_tenure_length(self):
        """Robertson has 10+ year tenure at The Verge."""
        j = self._find_robertson()
        self.assertIsNotNone(j)
        notes = str(j.get('notes', ''))
        # Profile should mention long tenure
        self.assertTrue(
            any(t in notes for t in ['14+', '13+', '12+', '11+', '10+',
                                      'founding', '2011']),
            "Profile should document Robertson's long tenure or founding status")

    def test_robertson_quest_pro_documented(self):
        """Quest Pro review (2/5) is documented in Robertson's profile."""
        j = self._find_robertson()
        self.assertIsNotNone(j)
        notes = str(j.get('notes', ''))
        career_str = str(j.get('career', ''))
        combined = notes + career_str
        self.assertTrue(
            'Quest Pro' in combined or 'quest pro' in combined.lower(),
            "Robertson's profile should reference Quest Pro coverage")


class TestRobertsonMetaFraming(unittest.TestCase):
    """Robertson's Meta coverage uses deficit framing patterns."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_robertson_analysis_exists(self):
        """Robertson cross-entity analysis exists in Verge research."""
        analysis = self._get_robertson_analysis()
        self.assertTrue(len(analysis) > 0,
                        "Robertson cross-entity framing analysis should exist")

    def test_meta_deficit_framing(self):
        """Meta products receive deficit framing (what's wrong, missing)."""
        analysis = self._get_robertson_analysis()
        meta = analysis.get('meta_framing', {})
        pattern = meta.get('pattern', '')
        self.assertIn('deficit', pattern.lower(),
                      "Meta framing should be documented as deficit pattern")

    def test_quest_pro_language_documented(self):
        """Quest Pro 'irredeemably bad' language is documented."""
        analysis = self._get_robertson_analysis()
        meta = analysis.get('meta_framing', {})
        markers = meta.get('language_markers', [])
        marker_str = ' '.join(str(m) for m in markers).lower()
        self.assertTrue(
            'irredeemably' in marker_str or 'tortuous' in marker_str
            or 'launched without' in marker_str,
            "Quest Pro harsh language should be documented")

    def test_quest_pro_score(self):
        """Quest Pro 2/5 score is documented."""
        analysis = self._get_robertson_analysis()
        meta = analysis.get('meta_framing', {})
        examples = meta.get('examples', [])
        quest_pro = [e for e in examples
                     if 'quest pro' in str(e).lower()]
        self.assertGreater(len(quest_pro), 0,
                           "Quest Pro should be in examples")
        qp = quest_pro[0]
        self.assertIn('score', qp)
        self.assertEqual(qp['score'], '2/5')

    def test_quest_2_privacy_conditional(self):
        """Quest 2 'if you're okay with Facebook' conditional documented."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        meta_examples = privacy.get('meta_examples', [])
        meta_str = ' '.join(str(e) for e in meta_examples).lower()
        self.assertTrue(
            "if you're okay" in meta_str or 'okay with facebook' in meta_str
            or 'privacy conditional' in meta_str,
            "Quest 2 privacy conditional should be documented")

    def test_quest_3_reductive_framing(self):
        """Quest 3 'game console with an extra feature' reductive framing."""
        analysis = self._get_robertson_analysis()
        meta = analysis.get('meta_framing', {})
        examples = meta.get('examples', [])
        quest_3 = [e for e in examples
                   if 'quest 3' in str(e).lower()]
        self.assertGreater(len(quest_3), 0,
                           "Quest 3 should be in examples")


class TestRobertsonCompetitorFraming(unittest.TestCase):
    """Robertson's competitor coverage uses improvement/neutral framing."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_magic_leap_improvement_framing(self):
        """Magic Leap receives improvement framing (what's better)."""
        analysis = self._get_robertson_analysis()
        competitor = analysis.get('competitor_framing', {})
        ml = competitor.get('magic_leap', {})
        pattern = ml.get('pattern', '')
        self.assertIn('improvement', pattern.lower(),
                      "Magic Leap should receive improvement framing")

    def test_magic_leap_2_positive_language(self):
        """Magic Leap 2 gets 'sharp and vibrant' (same year as Quest Pro 2/5)."""
        analysis = self._get_robertson_analysis()
        competitor = analysis.get('competitor_framing', {})
        ml = competitor.get('magic_leap', {})
        markers = ml.get('language_markers', [])
        marker_str = ' '.join(str(m) for m in markers).lower()
        self.assertTrue(
            'sharp' in marker_str or 'vibrant' in marker_str
            or 'improved' in marker_str or 'comfortable' in marker_str,
            "Magic Leap should have positive language markers")

    def test_magic_leap_no_privacy_conditional(self):
        """Magic Leap receives no privacy conditional despite cameras."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        absent = privacy.get('absent_from', [])
        absent_str = ' '.join(str(a) for a in absent).lower()
        self.assertIn('magic leap', absent_str,
                      "Magic Leap should be in absent-privacy-conditional list")

    def test_apple_vision_pro_no_privacy_conditional(self):
        """Apple Vision Pro gets no privacy conditional despite 12 cameras."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        absent = privacy.get('absent_from', [])
        absent_str = ' '.join(str(a) for a in absent).lower()
        self.assertTrue(
            'apple' in absent_str or 'vision pro' in absent_str,
            "Apple Vision Pro should be in absent-privacy-conditional list")

    def test_apple_camera_count_greater(self):
        """Apple Vision Pro has MORE surveillance hardware than Meta glasses."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        hardware = privacy.get('hardware_comparison', {})
        apple_cameras = hardware.get('apple_vision_pro_cameras', 0)
        meta_glasses_cameras = hardware.get('meta_ray_ban_cameras', 0)
        self.assertGreater(apple_cameras, meta_glasses_cameras,
                           "Apple VP should have more cameras than Meta glasses")


class TestRobertsonComfortDiscomfortParadox(unittest.TestCase):
    """The Comfort/Discomfort Paradox: same-year products get opposite frames."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_comfort_paradox_documented(self):
        """The Comfort/Discomfort Paradox is documented as a named pattern."""
        analysis = self._get_robertson_analysis()
        self.assertIn('comfort_discomfort_paradox', analysis)

    def test_same_year_comparison(self):
        """Quest Pro and Magic Leap 2 are both 2022 — same-year comparison."""
        analysis = self._get_robertson_analysis()
        paradox = analysis.get('comfort_discomfort_paradox', {})
        self.assertEqual(paradox.get('meta_product_year'), 2022)
        self.assertEqual(paradox.get('competitor_product_year'), 2022)

    def test_score_disparity(self):
        """Quest Pro got 2/5; Magic Leap 2 got positive hands-on (no score)."""
        analysis = self._get_robertson_analysis()
        paradox = analysis.get('comfort_discomfort_paradox', {})
        self.assertEqual(paradox.get('meta_score'), '2/5')
        self.assertEqual(paradox.get('competitor_score'), 'no_numeric_positive_hands_on')

    def test_wired_puck_equivalence(self):
        """Both Quest Pro and ML2 have similar limitations (ML2 has wired puck)."""
        analysis = self._get_robertson_analysis()
        paradox = analysis.get('comfort_discomfort_paradox', {})
        shared = paradox.get('shared_limitations', [])
        shared_str = ' '.join(str(s) for s in shared).lower()
        self.assertTrue(
            'puck' in shared_str or 'tethered' in shared_str
            or 'wired' in shared_str,
            "Shared limitation (wired puck/tethering) should be documented")


class TestRobertsonPrivacyConditionalPattern(unittest.TestCase):
    """Privacy-conditional framing applied ONLY to Meta, never competitors."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_privacy_conditional_meta_only(self):
        """Privacy conditional is Meta-exclusive in Robertson's coverage."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        self.assertTrue(privacy.get('meta_exclusive', False),
                        "Privacy conditional should be marked meta_exclusive")

    def test_meta_examples_count(self):
        """At least 2 Meta privacy conditional examples documented."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        meta_examples = privacy.get('meta_examples', [])
        self.assertGreaterEqual(len(meta_examples), 2,
                                "Need >= 2 Meta privacy conditional examples")

    def test_absent_from_count(self):
        """At least 3 competitors documented as absent from privacy framing."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        absent = privacy.get('absent_from', [])
        self.assertGreaterEqual(len(absent), 3,
                                "Need >= 3 competitors absent from privacy conditional")

    def test_snap_spectacles_absent(self):
        """Snap Spectacles (4 cameras) gets no privacy conditional."""
        analysis = self._get_robertson_analysis()
        privacy = analysis.get('privacy_conditional_pattern', {})
        absent = privacy.get('absent_from', [])
        absent_str = ' '.join(str(a) for a in absent).lower()
        self.assertTrue(
            'snap' in absent_str or 'spectacles' in absent_str,
            "Snap Spectacles should be in absent list")


class TestRobertsonInstitutionalAmplification(unittest.TestCase):
    """Post-Heath departure makes Robertson The Verge's primary XR voice."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_post_heath_amplification(self):
        """Post-Alex Heath departure amplification is documented."""
        analysis = self._get_robertson_analysis()
        amplification = analysis.get('institutional_amplification', {})
        self.assertIn('heath_departure', amplification)

    def test_heath_departure_date(self):
        """Alex Heath departure dated Sep 2025."""
        analysis = self._get_robertson_analysis()
        amplification = analysis.get('institutional_amplification', {})
        self.assertIn('2025', str(amplification.get('heath_departure', '')))

    def test_pmc_acquisition_context(self):
        """PMC acquisition (Jun 2026) context documented."""
        analysis = self._get_robertson_analysis()
        amplification = analysis.get('institutional_amplification', {})
        self.assertIn('pmc_acquisition', amplification)

    def test_pmc_entertainment_dependencies(self):
        """PMC's entertainment portfolio ad dependencies documented."""
        analysis = self._get_robertson_analysis()
        amplification = analysis.get('institutional_amplification', {})
        pmc = amplification.get('pmc_acquisition', {})
        brands = pmc.get('entertainment_properties', [])
        brands_str = ' '.join(str(b) for b in brands).lower()
        self.assertTrue(
            'variety' in brands_str or 'rolling stone' in brands_str
            or 'deadline' in brands_str,
            "PMC entertainment properties should be listed")


class TestRobertsonFramingMechanism(unittest.TestCase):
    """The mechanism is institutional posture + humanities lens, not financial."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_mechanism_documented(self):
        """Framing mechanism is documented."""
        analysis = self._get_robertson_analysis()
        self.assertIn('mechanism', analysis)

    def test_mechanism_is_institutional(self):
        """Mechanism is institutional posture, not direct financial."""
        analysis = self._get_robertson_analysis()
        mech = analysis.get('mechanism', '')
        self.assertIn('institutional', mech.lower(),
                      "Mechanism should reference institutional posture")

    def test_humanities_lens_noted(self):
        """Cornell humanities background noted as framing influence."""
        analysis = self._get_robertson_analysis()
        background = analysis.get('background', {})
        education = str(background.get('education', ''))
        self.assertTrue(
            'cornell' in education.lower() or 'humanities' in education.lower(),
            "Humanities educational background should be documented")

    def test_source_urls_present(self):
        """Source URLs backing the analysis are documented."""
        analysis = self._get_robertson_analysis()
        sources = analysis.get('source_urls', [])
        self.assertGreaterEqual(len(sources), 4,
                                "Need >= 4 source URLs for the analysis")


class TestRobertsonCreepParadoxAlignment(unittest.TestCase):
    """Robertson's pattern aligns with Chokkattu/Ashworth's Creep Paradox."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_robertson_analysis(self):
        verge = self.research.get('publications', {}).get('the-verge', {})
        return verge.get('robertson_cross_entity_framing', {})

    def test_creep_paradox_cross_reference(self):
        """Links to Chokkattu/Ashworth Creep Paradox as parallel finding."""
        analysis = self._get_robertson_analysis()
        refs = analysis.get('cross_references', [])
        refs_str = ' '.join(str(r) for r in refs).lower()
        self.assertTrue(
            'chokkattu' in refs_str or 'creep paradox' in refs_str
            or 'ashworth' in refs_str,
            "Should cross-reference Chokkattu/Ashworth Creep Paradox")

    def test_pattern_consistency(self):
        """Privacy frame applied to Meta only — consistent across desks."""
        analysis = self._get_robertson_analysis()
        consistency = analysis.get('cross_desk_consistency', '')
        self.assertTrue(
            len(consistency) > 0,
            "Cross-desk consistency note should exist")


if __name__ == '__main__':
    unittest.main()
