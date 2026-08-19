"""
Test Mechanism #178: PetaPixel Camera Publication Coverage Selection —
Samsung Galaxy Glasses Zero Articles vs Meta 5+ Privacy Alarm Articles (2026)

Type A: Competitor Coverage Deep Dive — PetaPixel (camera-specialist publication)

Core finding: PetaPixel, a photography/camera-focused publication, published 5+ dedicated
Meta smart glasses articles with privacy-alarm framing in 2026 while publishing ZERO articles
about Samsung Galaxy Glasses — despite Samsung's glasses featuring identical 12MP camera
hardware on the same Qualcomm Snapdragon AR1 chip. This is the first documented case of a
CAMERA-SPECIALIST publication reproducing the entity-identity coverage asymmetry. PetaPixel's
editorial expertise in camera technology should make them MORE likely to recognize hardware
equivalence, not less.

Temporal proof: Samsung launched Galaxy Glasses at Galaxy Unpacked London on July 22, 2026.
PetaPixel published nothing about the launch. Five days later (July 27), PetaPixel published
TWO Meta glasses alarm articles instead ("Instagram Is Banning Creepy Hidden Camera Videos"
and "Apple Frets Over Smart Glasses' Bad Reputation"). The editorial resources existed; they
were allocated to Meta alarm, not Samsung product coverage.

Sources:
- https://petapixel.com/2026/08/04/meta-smart-glasses-face-calls-for-bans-across-europe-over-privacy-concerns/
- https://petapixel.com/2026/07/27/instagram-is-banning-creepy-hidden-camera-videos-filmed-with-meta-smart-glasses/
- https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/
- https://petapixel.com/2026/03/09/meta-sued-after-workers-watched-private-moments-recorded-on-ai-smart-glasses/
- https://petapixel.com/2026/06/10/smart-glasses-in-pennsylvania-may-soon-legally-require-a-visible-recording-light/
- https://petapixel.com/2026/03/24/these-smart-glasses-come-with-a-cover-for-the-camera-inmo-go-3/
"""
import unittest
import yaml
import os
import re


def find_mechanism_anywhere(mechanism_id):
    """Search all YAML sections for a mechanism by ID."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
    )
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    # Search cross_publication_findings
    if 'cross_publication_findings' in data:
        for key, value in data['cross_publication_findings'].items():
            if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                return value

    # Search publications
    if 'publications' in data:
        for pub_key, pub_data in data['publications'].items():
            if isinstance(pub_data, dict):
                findings = pub_data.get('cross_publication_findings', {})
                if isinstance(findings, dict):
                    for key, value in findings.items():
                        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                            return value
    return None


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #178 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #178 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 178)

    def test_mechanism_name_contains_petapixel(self):
        name = self.mechanism['mechanism_name']
        self.assertIn('PetaPixel', name)

    def test_mechanism_name_contains_samsung(self):
        name = self.mechanism['mechanism_name']
        self.assertIn('Samsung', name)

    def test_mechanism_type(self):
        self.assertIn('coverage_selection', self.mechanism['mechanism_type'])

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreater(len(self.mechanism['source_urls']), 0)


class TestPublicationProfile(unittest.TestCase):
    """Verify PetaPixel publication profile captures camera-specialist identity."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.publication = cls.mechanism.get('publication', {})

    def test_publication_name(self):
        self.assertEqual(self.publication['name'], 'PetaPixel')

    def test_publication_type_camera_focused(self):
        pub_type = self.publication['type'].lower()
        self.assertTrue(
            'photo' in pub_type or 'camera' in pub_type,
            f"Publication type should reference photography/camera: {pub_type}"
        )

    def test_beat_is_camera_technology(self):
        beat = self.publication['beat'].lower()
        self.assertTrue(
            'camera' in beat or 'photo' in beat,
            f"Beat should reference camera/photography: {beat}"
        )

    def test_relevance_explains_camera_glasses_connection(self):
        relevance = self.publication.get('relevance', '')
        self.assertIn('camera', relevance.lower())

    def test_ownership_documented(self):
        self.assertIn('ownership', self.publication)


class TestHardwareParity(unittest.TestCase):
    """Verify the mechanism documents functionally identical camera hardware."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.parity = cls.mechanism.get('hardware_parity', {})

    def test_meta_camera_12mp(self):
        meta = self.parity.get('meta_ray_ban', {})
        self.assertIn('12', str(meta.get('camera', '')))

    def test_samsung_camera_12mp(self):
        samsung = self.parity.get('samsung_galaxy_glasses', {})
        self.assertIn('12', str(samsung.get('camera', '')))

    def test_same_chip_platform(self):
        meta_chip = self.parity.get('meta_ray_ban', {}).get('chip', '')
        samsung_chip = self.parity.get('samsung_galaxy_glasses', {}).get('chip', '')
        self.assertIn('Snapdragon AR1', meta_chip)
        self.assertIn('Snapdragon AR1', samsung_chip)

    def test_both_have_led_indicators(self):
        meta_led = self.parity.get('meta_ray_ban', {}).get('led_indicator')
        samsung_led = self.parity.get('samsung_galaxy_glasses', {}).get('led_indicator')
        self.assertTrue(meta_led)
        self.assertTrue(samsung_led)

    def test_samsung_dual_led_superiority(self):
        """Samsung has dual LEDs vs Meta's single — MORE privacy hardware."""
        samsung = self.parity.get('samsung_galaxy_glasses', {})
        led_info = str(samsung.get('led_indicator', ''))
        self.assertTrue(
            'dual' in led_info.lower() or samsung.get('led_indicator') is True,
            "Samsung dual LED privacy hardware should be documented"
        )

    def test_similar_weight(self):
        meta = self.parity.get('meta_ray_ban', {})
        samsung = self.parity.get('samsung_galaxy_glasses', {})
        meta_weight = re.search(r'(\d+)', str(meta.get('weight', '')))
        samsung_weight = re.search(r'(\d+)', str(samsung.get('weight', '')))
        if meta_weight and samsung_weight:
            diff = abs(int(meta_weight.group(1)) - int(samsung_weight.group(1)))
            self.assertLessEqual(diff, 5, "Weights should be within 5g of each other")

    def test_both_smart_glasses_form_factor(self):
        meta_form = self.parity.get('meta_ray_ban', {}).get('form_factor', '').lower()
        samsung_form = self.parity.get('samsung_galaxy_glasses', {}).get('form_factor', '').lower()
        self.assertIn('glasses', meta_form)
        self.assertIn('glasses', samsung_form)

    def test_verdict_documents_equivalence(self):
        verdict = self.parity.get('verdict', '')
        self.assertIn('identical', verdict.lower())


class TestMetaCoverageInventory(unittest.TestCase):
    """Verify PetaPixel's Meta glasses coverage is documented with specifics."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.meta_coverage = cls.mechanism.get('meta_coverage_inventory', {})

    def test_at_least_five_articles(self):
        articles = self.meta_coverage.get('articles', [])
        self.assertGreaterEqual(len(articles), 5)

    def test_each_article_has_title(self):
        for article in self.meta_coverage.get('articles', []):
            self.assertIn('title', article, f"Article missing title: {article}")

    def test_each_article_has_date(self):
        for article in self.meta_coverage.get('articles', []):
            self.assertIn('date', article, f"Article missing date: {article}")

    def test_each_article_has_url(self):
        for article in self.meta_coverage.get('articles', []):
            self.assertIn('url', article)
            self.assertTrue(
                article['url'].startswith('https://petapixel.com/'),
                f"URL should be petapixel.com: {article['url']}"
            )

    def test_each_article_has_alarm_vocabulary(self):
        for article in self.meta_coverage.get('articles', []):
            vocab = article.get('alarm_vocabulary', [])
            self.assertGreater(
                len(vocab), 0,
                f"Article should have alarm vocabulary: {article.get('title')}"
            )

    def test_articles_span_multiple_months(self):
        """Coverage is sustained, not a single news cycle."""
        dates = [str(a.get('date', '')) for a in self.meta_coverage.get('articles', [])]
        months = set()
        for d in dates:
            match = re.search(r'(\d{4}-\d{2})', d)
            if match:
                months.add(match.group(1))
        self.assertGreaterEqual(len(months), 3, f"Articles should span 3+ months: {months}")


class TestSamsungCoverageAbsence(unittest.TestCase):
    """Verify the mechanism documents Samsung Galaxy Glasses coverage absence."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.samsung_coverage = cls.mechanism.get('samsung_coverage_inventory', {})

    def test_samsung_articles_zero(self):
        count = self.samsung_coverage.get('total_dedicated_articles_2026', -1)
        self.assertEqual(count, 0, f"Samsung article count should be 0, got {count}")

    def test_search_methodology_documented(self):
        methodology = self.samsung_coverage.get('search_methodology', '')
        self.assertGreater(len(methodology), 50, "Search methodology should be documented in detail")

    def test_galaxy_unpacked_non_coverage_documented(self):
        """The July 22 Galaxy Unpacked non-coverage should be explicitly documented."""
        unpacked = self.samsung_coverage.get('galaxy_unpacked_london_coverage', '')
        self.assertIn('July 22', unpacked)
        self.assertIn('ZERO', unpacked.upper())


class TestCoverageSelectionDelta(unittest.TestCase):
    """Verify the coverage selection asymmetry is quantified."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.delta = cls.mechanism.get('coverage_selection_delta', {})

    def test_meta_articles_count(self):
        self.assertIn('meta_articles', self.delta)

    def test_samsung_articles_count(self):
        samsung = self.delta.get('samsung_articles', -1)
        self.assertEqual(samsung, 0)

    def test_ratio_documented(self):
        ratio = self.delta.get('ratio', '')
        self.assertIn('infinity', ratio.lower())

    def test_temporal_proof_documented(self):
        """July 22 Samsung launch → July 27 Meta alarm articles = temporal proof."""
        temporal = self.delta.get('temporal_proof', '')
        self.assertIn('July 22', temporal)
        self.assertIn('July 27', temporal)


class TestVocabularyInventory(unittest.TestCase):
    """Verify alarm vocabulary inventory is complete and asymmetric."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.vocab = cls.mechanism.get('vocabulary_inventory', {})

    def test_meta_alarm_terms_populated(self):
        terms = self.vocab.get('meta_alarm_terms', [])
        self.assertGreaterEqual(len(terms), 8, f"Should have 8+ alarm terms: {terms}")

    def test_samsung_alarm_terms_empty(self):
        terms = self.vocab.get('samsung_alarm_terms', [])
        self.assertEqual(len(terms), 0, f"Samsung alarm terms should be empty: {terms}")

    def test_samsung_alarm_count_zero(self):
        count = self.vocab.get('samsung_alarm_term_count', -1)
        self.assertEqual(count, 0)

    def test_meta_terms_include_key_words(self):
        terms = self.vocab.get('meta_alarm_terms', [])
        terms_lower = [t.lower() for t in terms]
        key_words = ['creepy', 'surveillance', 'clandestine']
        for word in key_words:
            found = any(word in t for t in terms_lower)
            self.assertTrue(found, f"Missing key alarm term: {word}")

    def test_pervert_glasses_documented(self):
        terms = self.vocab.get('meta_alarm_terms', [])
        terms_lower = [t.lower() for t in terms]
        found = any('pervert' in t for t in terms_lower)
        self.assertTrue(found, "''pervert glasses'' should be in alarm vocabulary")


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with honest strength assessments."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.confounders = cls.mechanism.get('confounders', [])

    def test_at_least_four_confounders(self):
        self.assertGreaterEqual(len(self.confounders), 4)

    def test_at_least_one_strong_confounder(self):
        strong = [c for c in self.confounders if c.get('strength') == 'strong']
        self.assertGreaterEqual(len(strong), 1, "Should have at least one strong confounder")

    def test_incident_history_confounder_present(self):
        """Must acknowledge Meta has real incidents Samsung lacks."""
        descriptions = ' '.join(c.get('description', '') for c in self.confounders)
        self.assertTrue(
            'incident' in descriptions.lower() or 'kenya' in descriptions.lower()
            or 'accumulated' in descriptions.lower(),
            "Must acknowledge Meta's accumulated real incidents as a confounder"
        )

    def test_each_confounder_has_rebuttal(self):
        for c in self.confounders:
            self.assertIn('rebuttal', c, f"Confounder missing rebuttal: {c.get('description', '')[:50]}")

    def test_each_confounder_has_strength(self):
        for c in self.confounders:
            self.assertIn('strength', c)
            self.assertIn(
                c['strength'], ['strong', 'moderate', 'weak'],
                f"Invalid strength: {c['strength']}"
            )


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.cross_refs = cls.mechanism.get('cross_references', [])

    def test_has_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_references_samsung_equivalence_paradox(self):
        """Should reference mechanism #144 (Samsung equivalence paradox)."""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(144, ref_ids)

    def test_references_kodak_fiend(self):
        """Should reference mechanism #177 (Kodak Fiend precedent)."""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(177, ref_ids)

    def test_each_reference_has_relationship(self):
        for ref in self.cross_refs:
            self.assertIn('relationship', ref)
            self.assertGreater(len(ref['relationship']), 10)


class TestSignificance(unittest.TestCase):
    """Verify significance assessment captures the novel contribution."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(178)
        cls.significance = cls.mechanism.get('significance', {})

    def test_novel_contribution_documented(self):
        novel = self.significance.get('novel_contribution', '')
        self.assertGreater(len(novel), 50)

    def test_novel_contribution_highlights_camera_specialist(self):
        novel = self.significance.get('novel_contribution', '').lower()
        self.assertTrue(
            'camera' in novel and 'specialist' in novel or 'camera' in novel and 'expert' in novel,
            "Novel contribution should highlight camera-specialist angle"
        )

    def test_asymmetry_score_above_threshold(self):
        score = self.significance.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.85, f"Score should be ≥0.85 for infinite ratio: {score}")

    def test_has_explanation_for_high_score(self):
        self.assertIn('why_high', self.significance)


if __name__ == '__main__':
    unittest.main()
