"""
Test: Guardian Samsung Galaxy Glasses London Geographic Proximity & Privacy Parity
Natural Experiment (Mechanism #169)

TYPE A: Competitor Coverage Deep Dive — Guardian × Samsung

FINDING: Samsung Galaxy Glasses were announced on July 22, 2026 at Galaxy Unpacked
in LONDON, ENGLAND — The Guardian's home city. The Guardian published ZERO articles
about Samsung Galaxy Glasses despite:
  (a) The event taking place in London
  (b) Samsung Galaxy Glasses having IDENTICAL hardware to Meta Ray-Ban (same
      Snapdragon AR1 Gen 1 chip, same 12MP camera, same LED privacy indicator,
      same tamper-detection auto-disable)
  (c) Extensive Guardian adversarial coverage of Meta glasses privacy concerns

DISTINCTION FROM MECHANISM #83:
  Mechanism #83 (Aug 13): Focuses on Google-Samsung-Guardian FINANCIAL TRIANGLE
    (Samsung as Google's Android XR platform, Guardian as Google News AI pilot).
  Mechanism #169 (Aug 18): Focuses on two novel variables:
    1. GEOGRAPHIC PROXIMITY — Samsung chose London for Unpacked; Guardian is HQ'd
       in London. London-based publication ignoring a major London tech launch with
       privacy-relevant hardware is testable independent of financial relationships.
    2. CROSS-PUBLICATION PRIVACY VOCABULARY INVERSION — Samsung's LED auto-disable
       (confirmed Jul 28, 2026) is IDENTICAL to Meta's approach. Yet publications
       frame Samsung as "takes privacy seriously" (GSMArena, SamMobile) while
       framing Meta's identical feature as insufficient/reactive. The Guardian's
       silence prevents any vocabulary comparison for their coverage.

HARDWARE PRIVACY PARITY (verified from manufacturer specs):
  Samsung Galaxy Glasses:
    - Camera: 12MP (eye-level), Sony IMX681 sensor
    - Chip: Qualcomm Snapdragon AR1 Gen 1
    - Privacy LED: Yes, visible to wearer and bystanders
    - Tamper detection: Camera disabled if LED blocked/destroyed
    - AI processing: Google Gemini (multimodal, cloud-processed)
    - Architecture: Phone-tethered companion device
    - Price: $379-$499, fall 2026 launch
  Meta Ray-Ban Gen 2:
    - Camera: 12MP
    - Chip: Qualcomm Snapdragon AR1 Gen 1 (SAME)
    - Privacy LED: Yes, visible to wearer and bystanders (SAME)
    - Tamper detection: Camera disabled if LED blocked (SAME)
    - AI processing: Meta AI (multimodal, cloud-processed)
    - Architecture: Phone-tethered companion device (SAME)
    - Price: $299-$799

CROSS-PUBLICATION VOCABULARY INVERSION (Samsung privacy features):
  GSMArena (Jul 28, 2026): "Samsung's smart glasses have this important privacy
    feature" — positive framing of LED + tamper detection
  SamMobile (Jul 28, 2026): "Samsung's smart glasses take privacy pretty
    seriously" — aspirational framing
  MakeUseOf (Apr 2026): "Enhanced Privacy Features" as a Samsung ADVANTAGE
  The Gadgeteer (Apr 29, 2026): "Privacy questions are already on the table" —
    neutral, attributed to category not Samsung specifically

  vs. Meta glasses coverage at same outlets:
    Multiple: "surveillance," "creepy," "pervert glasses," "invasion of privacy,"
    "nightmare," "insidious," "predatory behavior"

COVERAGE AT OTHER OUTLETS (proving Samsung Unpacked London newsworthiness):
  eWeek, Android Authority, ZDNET, wareable.com, gagadget.com, The Gadgeteer,
  TechTimes, ghacks, GSMArena, SamMobile, MakeUseOf — all covered Samsung Galaxy
  Glasses. Event held at scale in London with major press attendance.

GUARDIAN SEARCH VERIFICATION (Aug 18, 2026 — 27 days post-Unpacked):
  site:theguardian.com Samsung Galaxy Glasses → 0 results
  site:theguardian.com Samsung smart glasses Android XR → 0 results
  theguardian.com Samsung Galaxy Glasses Unpacked London → 0 Guardian results

SOURCE URLs:
  Samsung Galaxy Glasses Wikipedia: https://en.wikipedia.org/wiki/Samsung_Galaxy_Glasses
  eWeek Samsung/Google XR glasses: https://www.eweek.com/news/samsung-google-first-android-xr-smart-glasses/
  Android Authority Samsung/Google glasses: https://www.androidauthority.com/samsung-google-android-xr-glasses-warby-parker-gentle-monster-google-io-2026-3668380/
  GSMArena Samsung privacy feature: https://www.gsmarena.com/samsungs_smart_glasses_have_this_important_privacy_feature-news-73909.php
  SamMobile Samsung privacy: https://www.sammobile.com/news/samsungs-smart-glasses-take-privacy-seriously/
  gagadget Samsung Galaxy Glasses: https://gagadget.com/en/710069-samsung-galaxy-glasses-are-coming-in-july-heres-what-we-know/
  The Gadgeteer Samsung Galaxy Glasses: https://the-gadgeteer.com/2026/04/29/samsung-galaxy-glasses/
  wareable Samsung Galaxy Glasses: https://www.wareable.com/wearable-tech/samsungs-smart-galaxy-glasses-camera-phone-tether-ar-display-confirmation

CROSS-REFERENCES:
  #83: Guardian Samsung/Google coverage silence (FINANCIAL triangle — distinct from
       geographic proximity angle; #169 extends with London proximity + privacy parity)
  #163: WIRED Snap SPECS coverage selection silence (same mechanism class —
       parent company with competitor financial ties ignoring competitor product)
  #166: Kali Hays BBC cross-entity coverage selection (UK public broadcaster
       showing same London-based pattern)
  #167: Condé Nast Google Zero distribution dependency (Google financial influence
       on editorial coverage selection)
"""

import unittest
import yaml
import os
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(filename):
    path = os.path.join(REPO_ROOT, 'profiles', filename)
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism_anywhere(data, slug_fragment):
    """Find a mechanism in the publications section by slug fragment."""
    pubs = data.get('publications', {})
    if isinstance(pubs, dict):
        for key, value in pubs.items():
            if slug_fragment in key and isinstance(value, dict):
                return value
    return None


def find_mechanism_anywhere(data, slug_fragment):
    """Find a mechanism in any section by slug fragment."""
    for section_name in ['cross_publication_findings', 'aggregate_findings', 'publications']:
        section = data.get(section_name, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if slug_fragment in key and isinstance(value, dict):
                    return value
    return None


class TestMechanismExistence(unittest.TestCase):
    """Mechanism #169 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_mechanism_exists(self):
        self.assertIsNotNone(
            self.mechanism,
            "Mechanism for Guardian Samsung Galaxy Glasses London geographic proximity must exist"
        )

    def test_mechanism_id_is_169(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 169)

    def test_finding_type(self):
        ft = self.mechanism.get('finding_type', '')
        self.assertTrue(
            'coverage_selection' in ft.lower() or 'geographic_proximity' in ft.lower(),
            f"Finding type must include coverage_selection or geographic_proximity, got: {ft}"
        )

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 6, "Must have at least 6 source URLs")

    def test_has_test_file(self):
        tf = self.mechanism.get('test_file', '')
        self.assertIn('guardian_samsung_galaxy_glasses_london', tf)

    def test_has_confounders(self):
        conf = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(conf), 5, "Must have at least 5 confounders")

    def test_has_cross_references(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 3)

    def test_date_is_august_2026(self):
        date = str(self.mechanism.get('date_added', self.mechanism.get('date', '')))
        self.assertIn('2026-08', date)

    def test_asymmetry_score(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.65)
        self.assertLessEqual(score, 0.85)

    def test_distinction_from_mechanism_83(self):
        """Mechanism #169 must explicitly reference and distinguish from #83."""
        refs = self.mechanism.get('cross_references', [])
        has_83_ref = any(
            ref.get('mechanism_id') == 83
            for ref in refs if isinstance(ref, dict)
        )
        self.assertTrue(has_83_ref, "Must cross-reference mechanism #83 (Guardian Samsung financial triangle)")


class TestSamsungGlassesHardware(unittest.TestCase):
    """Samsung Galaxy Glasses hardware specs match Meta Ray-Ban for privacy parity."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_samsung_camera_resolution(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertEqual(hw.get('camera_megapixels'), 12)

    def test_samsung_chip(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        chip = hw.get('chip', '')
        self.assertIn('AR1', chip, "Samsung must use Snapdragon AR1 Gen 1")

    def test_samsung_privacy_led(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertTrue(hw.get('privacy_led'), "Samsung must have privacy LED")

    def test_samsung_tamper_detection(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertTrue(hw.get('tamper_detection_auto_disable'),
                       "Samsung must have tamper detection auto-disable")

    def test_samsung_phone_tethered(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertTrue(hw.get('phone_tethered'))

    def test_samsung_price_range(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertGreaterEqual(hw.get('price_min_usd', 0), 350)
        self.assertLessEqual(hw.get('price_max_usd', 999), 550)

    def test_samsung_launch_location_london(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        location = hw.get('launch_event_location', '')
        self.assertIn('London', location)

    def test_samsung_launch_date(self):
        hw = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        self.assertIn('2026-07-22', str(hw.get('launch_date', '')))

    def test_meta_camera_resolution(self):
        hw = self.mechanism.get('meta_rayban_hardware', {})
        self.assertEqual(hw.get('camera_megapixels'), 12)

    def test_meta_chip_matches_samsung(self):
        hw = self.mechanism.get('meta_rayban_hardware', {})
        chip = hw.get('chip', '')
        self.assertIn('AR1', chip, "Meta must also use Snapdragon AR1 Gen 1")

    def test_meta_privacy_led(self):
        hw = self.mechanism.get('meta_rayban_hardware', {})
        self.assertTrue(hw.get('privacy_led'))

    def test_meta_tamper_detection(self):
        hw = self.mechanism.get('meta_rayban_hardware', {})
        self.assertTrue(hw.get('tamper_detection_auto_disable'))

    def test_chip_parity(self):
        """Both products must use the same Snapdragon AR1 Gen 1 chip."""
        samsung = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        meta = self.mechanism.get('meta_rayban_hardware', {})
        self.assertEqual(samsung.get('chip'), meta.get('chip'),
                        "Samsung and Meta must use the SAME chip")

    def test_privacy_feature_parity(self):
        """Both products must have same privacy features."""
        samsung = self.mechanism.get('samsung_galaxy_glasses_hardware', {})
        meta = self.mechanism.get('meta_rayban_hardware', {})
        self.assertEqual(samsung.get('privacy_led'), meta.get('privacy_led'))
        self.assertEqual(samsung.get('tamper_detection_auto_disable'),
                        meta.get('tamper_detection_auto_disable'))


class TestLondonGeographicProximity(unittest.TestCase):
    """The London geographic proximity angle is the novel contribution."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_geographic_proximity_documented(self):
        geo = self.mechanism.get('geographic_proximity', {})
        self.assertIsNotNone(geo, "Must have geographic_proximity section")

    def test_guardian_hq_london(self):
        geo = self.mechanism.get('geographic_proximity', {})
        self.assertIn('London', str(geo.get('guardian_headquarters', '')))

    def test_samsung_event_london(self):
        geo = self.mechanism.get('geographic_proximity', {})
        self.assertIn('London', str(geo.get('samsung_unpacked_location', '')))

    def test_same_city(self):
        geo = self.mechanism.get('geographic_proximity', {})
        self.assertTrue(geo.get('same_city'),
                       "Guardian HQ and Samsung Unpacked must be in the same city")

    def test_days_since_event(self):
        geo = self.mechanism.get('geographic_proximity', {})
        days = geo.get('days_since_event_at_discovery', 0)
        self.assertGreaterEqual(days, 27,
                               "Must be at least 27 days since Jul 22 Unpacked")


class TestCrossPublicationVocabularyInversion(unittest.TestCase):
    """Cross-publication vocabulary inversion: Samsung 'seriously' vs Meta 'surveillance'."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_vocabulary_inversion_documented(self):
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        self.assertIsNotNone(vi, "Must have vocabulary inversion documentation")

    def test_samsung_positive_framings(self):
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        samsung_framings = vi.get('samsung_privacy_framings', [])
        self.assertGreaterEqual(len(samsung_framings), 2,
                               "Must document at least 2 Samsung positive framings")

    def test_meta_adversarial_framings(self):
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        meta_framings = vi.get('meta_privacy_framings', [])
        self.assertGreaterEqual(len(meta_framings), 3,
                               "Must document at least 3 Meta adversarial framings")

    def test_gsmarena_samsung_positive(self):
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        samsung_framings = vi.get('samsung_privacy_framings', [])
        outlet_names = [f.get('outlet', '') for f in samsung_framings if isinstance(f, dict)]
        self.assertTrue(any('gsmarena' in n.lower() for n in outlet_names),
                       "GSMArena Samsung positive framing must be documented")

    def test_sammobile_samsung_positive(self):
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        samsung_framings = vi.get('samsung_privacy_framings', [])
        outlet_names = [f.get('outlet', '') for f in samsung_framings if isinstance(f, dict)]
        self.assertTrue(any('sammobile' in n.lower() for n in outlet_names),
                       "SamMobile Samsung positive framing must be documented")

    def test_identical_feature_different_framing(self):
        """Same LED+tamper-detect feature framed positively for Samsung, adversarially for Meta."""
        vi = self.mechanism.get('cross_publication_vocabulary_inversion', {})
        self.assertTrue(vi.get('identical_feature_different_framing', False),
                       "Must flag that identical features receive different framing")


class TestCoverageAtOtherOutlets(unittest.TestCase):
    """Other outlets covered Samsung Galaxy Glasses London launch — proving newsworthiness."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_other_outlets_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        self.assertGreaterEqual(len(outlets), 8,
                               "At least 8 other outlets covered Samsung Galaxy Glasses")

    def test_eweek_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('eweek' in n.lower() for n in names))

    def test_android_authority_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('android authority' in n.lower() for n in names))

    def test_zdnet_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('zdnet' in n.lower() for n in names))

    def test_wareable_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('wareable' in n.lower() for n in names))

    def test_gsmarena_covered(self):
        outlets = self.mechanism.get('coverage_at_other_outlets', [])
        names = [o.get('outlet', '') if isinstance(o, dict) else str(o) for o in outlets]
        self.assertTrue(any('gsmarena' in n.lower() for n in names))


class TestGuardianGoogleFinancialContext(unittest.TestCase):
    """Guardian-Google financial relationship documented as context (distinct from #83)."""

    @classmethod
    def setUpClass(cls):
        cls.guardian = load_yaml('guardian.yaml')

    def test_google_financial_tie_exists(self):
        cr = self.guardian.get('competitor_relationships', {})
        google = cr.get('google', {})
        self.assertEqual(google.get('financial_tie'), 'mixed')

    def test_samsung_competitor_relationship_exists(self):
        cr = self.guardian.get('competitor_relationships', {})
        samsung = cr.get('samsung', {})
        self.assertIsNotNone(samsung, "Guardian must have samsung competitor relationship entry")

    def test_samsung_relationship_references_google(self):
        cr = self.guardian.get('competitor_relationships', {})
        samsung = cr.get('samsung', {})
        desc = samsung.get('description', '')
        self.assertIn('Google', desc,
                     "Samsung relationship must reference Google Android XR partnership")

    def test_samsung_coverage_prediction(self):
        cr = self.guardian.get('competitor_relationships', {})
        samsung = cr.get('samsung', {})
        pred = samsung.get('coverage_prediction', '')
        self.assertIn('neutral', pred.lower(),
                     "Samsung coverage prediction should be neutral-to-absent")


class TestBrittinRevolvingDoor(unittest.TestCase):
    """Matthew Brittin's Google → GMG SID → BBC DG path as context."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_brittin_documented(self):
        brittin = self.mechanism.get('brittin_revolving_door', {})
        self.assertIsNotNone(brittin)

    def test_brittin_google_tenure(self):
        brittin = self.mechanism.get('brittin_revolving_door', {})
        self.assertGreaterEqual(brittin.get('google_years', 0), 18)

    def test_brittin_gmg_role(self):
        brittin = self.mechanism.get('brittin_revolving_door', {})
        role = brittin.get('gmg_role', '')
        self.assertIn('Senior Independent Director', role)

    def test_brittin_departure_before_samsung_launch(self):
        brittin = self.mechanism.get('brittin_revolving_door', {})
        departure = str(brittin.get('gmg_departure_date', ''))
        self.assertIn('2026-03', departure,
                     "Brittin departed GMG in March 2026, 4 months before Samsung launch")

    def test_brittin_bbc_destination(self):
        brittin = self.mechanism.get('brittin_revolving_door', {})
        dest = brittin.get('destination', '')
        self.assertIn('BBC', dest)


class TestConfounders(unittest.TestCase):
    """Confounders must be thorough and honest."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_has_strong_confounders(self):
        conf = self.mechanism.get('confounding_factors', [])
        strong = [c for c in conf if isinstance(c, dict) and c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2, "Must have at least 2 STRONG confounders")

    def test_product_launch_coverage_pattern_confounder(self):
        """Guardian may not cover product launches generally."""
        conf = self.mechanism.get('confounding_factors', [])
        factors = [c.get('factor', '') for c in conf if isinstance(c, dict)]
        self.assertTrue(
            any('product launch' in f.lower() or 'reviews' in f.lower() for f in factors),
            "Must address whether Guardian covers product launches at all"
        )

    def test_not_yet_shipping_confounder(self):
        """Samsung glasses not yet shipping."""
        conf = self.mechanism.get('confounding_factors', [])
        factors = [c.get('factor', '') for c in conf if isinstance(c, dict)]
        self.assertTrue(
            any('shipping' in f.lower() or 'fall 2026' in f.lower() or 'not yet' in f.lower()
                for f in factors),
            "Must address Samsung not yet shipping"
        )

    def test_market_share_confounder(self):
        """Meta's dominant market share naturally attracts more coverage."""
        conf = self.mechanism.get('confounding_factors', [])
        factors = [c.get('factor', '') for c in conf if isinstance(c, dict)]
        self.assertTrue(
            any('market share' in f.lower() or 'dominant' in f.lower() for f in factors),
            "Must address Meta's dominant market share"
        )


class TestCrossReferences(unittest.TestCase):
    """Cross-references must link to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_cross_ref_83(self):
        """Must reference mechanism #83 (Guardian Samsung financial triangle)."""
        refs = self.mechanism.get('cross_references', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(83, ids)

    def test_cross_ref_163(self):
        """Must reference mechanism #163 (WIRED Snap SPECS silence)."""
        refs = self.mechanism.get('cross_references', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(163, ids)

    def test_cross_ref_166(self):
        """Must reference mechanism #166 (Kali Hays BBC)."""
        refs = self.mechanism.get('cross_references', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(166, ids)

    def test_cross_ref_167(self):
        """Must reference mechanism #167 (Condé Nast Google Zero)."""
        refs = self.mechanism.get('cross_references', [])
        ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(167, ids)

    def test_cross_ref_relationships_not_empty(self):
        refs = self.mechanism.get('cross_references', [])
        for ref in refs:
            if isinstance(ref, dict):
                self.assertTrue(ref.get('relationship', ''),
                              f"Cross-ref to #{ref.get('mechanism_id')} must have relationship description")


class TestTestablePredictions(unittest.TestCase):
    """Testable predictions for falsifiability."""

    @classmethod
    def setUpClass(cls):
        cls.ccr = load_yaml('competitor-coverage-research.yaml')
        cls.mechanism = find_mechanism_anywhere(
            cls.ccr, 'guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity'
        )

    def test_has_predictions(self):
        preds = self.mechanism.get('testable_predictions', [])
        self.assertGreaterEqual(len(preds), 3, "Must have at least 3 testable predictions")

    def test_predictions_are_specific(self):
        preds = self.mechanism.get('testable_predictions', [])
        for pred in preds:
            self.assertGreaterEqual(len(str(pred)), 50,
                                  "Each prediction must be substantive (50+ chars)")


if __name__ == '__main__':
    unittest.main()
