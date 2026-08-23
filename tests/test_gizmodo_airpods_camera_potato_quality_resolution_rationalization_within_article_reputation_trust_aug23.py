"""
Test Mechanism #251: Gizmodo AirPods Camera "Potato Quality" Resolution-Rationalization —
Within-Article Reputation Trust Differential

Type A: Competitor Coverage Deep Dive (Gizmodo × Apple vs Gizmodo × Meta)

Core finding: In a single article (Aug 21, 2026), Gizmodo explicitly compares Apple's
unreleased camera AirPods to Meta's shipping Ray-Ban smart glasses — and systematically
resolves privacy concerns for Apple while leaving identical concerns unresolved for Meta
in contemporaneous articles.

The AirPods article uses THREE resolution-rationalization techniques:
1. TECHNICAL MINIMIZATION: "potato quality" converts Apple's 1MP sensor from a
   limitation to a privacy ADVANTAGE ("not so good that they represent a huge privacy
   liability")
2. ALARM-AND-RESOLUTION: Raises the alarm about passive mode ("should have your alarm
   bells sounding") then immediately resolves it with on-device processing ("peripheral
   inference...on-device detection")
3. CORPORATE TRUST PROXY: "I can't imagine that Apple, a company that stakes its
   reputation on being a cut above in terms of user privacy, will want to tread down
   the route" — uses Apple's reputation as the resolution mechanism

In the same month, Gizmodo's Meta coverage:
- "Smart Glasses Are a Hit Even as Privacy Concerns Pile Up" (Jul 31) — concerns
  presented as open wounds, no resolution-rationalization
- "Smart Glasses Are Catching on With U.S. Police" (Aug 11) — surveillance angle,
  no corporate trust proxy
- Meta used as the NEGATIVE ANCHOR within the AirPods article itself

Crucially, AirPods "passive mode" (320×320 continuous capture) is functionally analogous
to Meta's "super sensing" feature — yet one gets "potato quality" and the other gets
"nightmarish" framing across publications.

This extends Gizmodo's clean-control status (no financial relationships with either
Apple or Meta) by showing that REPUTATIONAL trust differentials produce measurable
vocabulary bifurcation even absent financial incentives. However, Gizmodo's affiliate
revenue model (product review → purchase links) creates a SECONDARY financial incentive:
Apple products generate higher affiliate revenue than Meta glasses, so maintaining
Apple's privacy reputation indirectly serves Gizmodo's business model.

Sources:
- https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
- https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
- https://gizmodo.com/smart-glasses-are-catching-on-with-u-s-police-2000797054
- https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809
- https://gizmodo.com/dear-meta-smart-glasses-wearers-youre-being-watched-too-2000728928
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

    def _extract_all_mechanisms(obj, out=None):
        if out is None:
            out = {}
        if isinstance(obj, dict):
            mid = obj.get('mechanism_id')
            if mid is not None:
                # Prefer entries with more keys (real entries over cross-ref stubs)
                if mid not in out or len(obj) > len(out[mid]):
                    out[mid] = obj
            for v in obj.values():
                _extract_all_mechanisms(v, out)
        elif isinstance(obj, list):
            for item in obj:
                _extract_all_mechanisms(item, out)
        return out

    all_mechanisms = _extract_all_mechanisms(data)
    return all_mechanisms.get(mechanism_id)


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #251 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #251 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 251)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)
        self.assertEqual(self.mechanism['discovery_date'], '2026-08-23')

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreaterEqual(len(self.mechanism['source_urls']), 4)

    def test_has_asymmetry_score(self):
        self.assertIn('asymmetry_score', self.mechanism)
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_has_finding_summary(self):
        self.assertIn('finding_summary', self.mechanism)
        self.assertGreater(len(self.mechanism['finding_summary']), 100)


class TestArticleAnalysis(unittest.TestCase):
    """Verify the AirPods article analysis captures key patterns."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.airpods_article = cls.mechanism.get('airpods_article', {})

    def test_airpods_article_exists(self):
        self.assertIsNotNone(self.airpods_article)
        self.assertIn('url', self.airpods_article)

    def test_airpods_article_url(self):
        self.assertIn('gizmodo.com', self.airpods_article['url'])

    def test_airpods_article_date(self):
        self.assertIn('date', self.airpods_article)
        self.assertEqual(self.airpods_article['date'], '2026-08-21')

    def test_headline_is_defensive_frame(self):
        """Headline tells readers NOT to make the smart glasses comparison."""
        headline = self.airpods_article.get('headline', '')
        # Headline should contain negation framing
        self.assertTrue(
            "aren't" in headline.lower() or "not" in headline.lower() or "no," in headline.lower(),
            f"Headline should contain defensive negation: {headline}"
        )


class TestResolutionRationalizationTechniques(unittest.TestCase):
    """Verify three resolution-rationalization techniques are documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.techniques = cls.mechanism.get('resolution_rationalization_techniques', [])

    def test_has_three_techniques(self):
        self.assertGreaterEqual(len(self.techniques), 3)

    def test_technical_minimization_technique(self):
        """'Potato quality' converts limitation to privacy advantage."""
        names = [t.get('name', '') for t in self.techniques]
        self.assertTrue(
            any('technical_minimization' in n.lower() or 'potato' in n.lower()
                for n in names),
            f"Missing technical minimization technique. Found: {names}"
        )

    def test_alarm_and_resolution_technique(self):
        """Alarm raised then immediately resolved within same paragraph."""
        names = [t.get('name', '') for t in self.techniques]
        self.assertTrue(
            any('alarm' in n.lower() and 'resolution' in n.lower()
                for n in names),
            f"Missing alarm-and-resolution technique. Found: {names}"
        )

    def test_corporate_trust_proxy_technique(self):
        """Apple reputation used as the resolution mechanism."""
        names = [t.get('name', '') for t in self.techniques]
        self.assertTrue(
            any('trust' in n.lower() or 'reputation' in n.lower()
                for n in names),
            f"Missing corporate trust proxy technique. Found: {names}"
        )


class TestVocabularyBifurcation(unittest.TestCase):
    """Verify vocabulary analysis captures Apple vs Meta language."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.vocabulary = cls.mechanism.get('vocabulary_analysis', {})

    def test_apple_vocabulary_exists(self):
        self.assertIn('apple_framing_vocabulary', self.vocabulary)
        apple_vocab = self.vocabulary['apple_framing_vocabulary']
        self.assertGreater(len(apple_vocab), 3)

    def test_meta_vocabulary_exists(self):
        self.assertIn('meta_framing_vocabulary', self.vocabulary)
        meta_vocab = self.vocabulary['meta_framing_vocabulary']
        self.assertGreater(len(meta_vocab), 3)

    def test_potato_quality_in_apple_vocabulary(self):
        """Key minimization phrase should be documented."""
        apple_vocab = self.vocabulary['apple_framing_vocabulary']
        vocab_str = str(apple_vocab).lower()
        self.assertIn('potato', vocab_str)

    def test_sentiment_delta(self):
        """Within-article sentiment delta should be significant."""
        self.assertIn('within_article_sentiment_delta', self.vocabulary)
        delta = self.vocabulary['within_article_sentiment_delta']
        self.assertGreaterEqual(delta, 0.3,
                                "Delta should be >= 0.3 for same-article comparison")


class TestCrossEntityComparison(unittest.TestCase):
    """Verify cross-entity comparison with contemporaneous Meta coverage."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.comparison = cls.mechanism.get('contemporaneous_meta_coverage', [])

    def test_has_comparisons(self):
        self.assertGreaterEqual(len(self.comparison), 2)

    def test_comparison_includes_pile_up(self):
        """'Privacy Concerns Pile Up' article should be referenced."""
        urls = [c.get('url', '') for c in self.comparison]
        self.assertTrue(
            any('pile-up' in u or '2000792911' in u for u in urls),
            "Should reference 'Privacy Concerns Pile Up' article"
        )

    def test_comparison_includes_police(self):
        """'Catching on With U.S. Police' article should be referenced."""
        urls = [c.get('url', '') for c in self.comparison]
        self.assertTrue(
            any('police' in u or '2000797054' in u for u in urls),
            "Should reference 'Catching on With Police' article"
        )

    def test_meta_coverage_has_no_resolution(self):
        """Pure Meta articles should show concerns unresolved."""
        for comp in self.comparison:
            # Skip Apple-framed articles that use Meta as cautionary example
            title = comp.get('title', '')
            if 'Apple' in title:
                continue
            resolution = comp.get('resolution_rationalization', False)
            self.assertFalse(resolution,
                             f"Meta article should have no resolution-rationalization: {title}")


class TestPassiveModeParityAnalysis(unittest.TestCase):
    """Verify passive mode / super sensing functional equivalence is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.parity = cls.mechanism.get('passive_mode_parity', {})

    def test_parity_section_exists(self):
        self.assertTrue(len(self.parity) > 0,
                        "Passive mode parity analysis should exist")

    def test_apple_passive_mode_documented(self):
        self.assertIn('apple_passive_mode', self.parity)

    def test_meta_super_sensing_documented(self):
        self.assertIn('meta_comparable_feature', self.parity)

    def test_framing_difference_documented(self):
        self.assertIn('framing_asymmetry', self.parity)


class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.confounders = cls.mechanism.get('confounding_factors', [])

    def test_has_confounders(self):
        self.assertGreaterEqual(len(self.confounders), 3)

    def test_includes_strong_confounder(self):
        strengths = [c.get('strength', '') for c in self.confounders]
        self.assertIn('STRONG', strengths)

    def test_includes_incident_history_confounder(self):
        """Meta's actual incidents vs Apple's no incidents should be acknowledged."""
        descriptions = ' '.join(c.get('description', '') for c in self.confounders)
        self.assertTrue(
            'incident' in descriptions.lower() or 'track record' in descriptions.lower(),
            "Should document that Meta has actual privacy incidents while Apple doesn't"
        )

    def test_includes_affiliate_confounder(self):
        """Affiliate revenue as secondary financial incentive."""
        descriptions = ' '.join(c.get('description', '') for c in self.confounders)
        self.assertTrue(
            'affiliate' in descriptions.lower(),
            "Should document affiliate revenue as secondary financial incentive"
        )


class TestCleanControlImplication(unittest.TestCase):
    """Verify clean control interpretation is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.control = cls.mechanism.get('clean_control_implications', {})

    def test_clean_control_section_exists(self):
        self.assertTrue(len(self.control) > 0)

    def test_documents_no_direct_financial_tie(self):
        self.assertIn('direct_financial_relationships', self.control)
        self.assertEqual(self.control['direct_financial_relationships'], 'none')

    def test_documents_affiliate_secondary(self):
        self.assertIn('secondary_financial_channel', self.control)

    def test_documents_baseline_implications(self):
        self.assertIn('baseline_interpretation', self.control)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)
        cls.refs = cls.mechanism.get('cross_references', [])

    def test_has_cross_references(self):
        self.assertGreaterEqual(len(self.refs), 3)

    def test_references_matt_wille_mechanism(self):
        """Should reference mechanism #179 (Matt Wille beat reporter)."""
        ref_ids = [r.get('mechanism_id') for r in self.refs]
        self.assertIn(179, ref_ids)

    def test_references_gizmodo_clean_control(self):
        """Should reference mechanism #98 (Gizmodo Anthropic clean control)."""
        ref_ids = [r.get('mechanism_id') for r in self.refs]
        self.assertIn(98, ref_ids)

    def test_references_apple_airpods_leak_pattern(self):
        """Should reference the broader Apple AirPods leak coverage pattern."""
        ref_ids = [r.get('mechanism_id') for r in self.refs]
        # Mechanism #247 is the cross-publication Apple camera AirPods vocabulary gradient
        self.assertIn(247, ref_ids)


class TestMetaCoverageTone(unittest.TestCase):
    """Verify meta_coverage_tone field is present."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(251)

    def test_meta_coverage_tone_exists(self):
        self.assertIn('meta_coverage_tone', self.mechanism)


if __name__ == '__main__':
    unittest.main()
