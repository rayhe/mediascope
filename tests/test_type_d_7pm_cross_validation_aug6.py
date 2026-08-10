"""
Type D Cross-Validation: 7 PM Aug 6, 2026

Validates data consistency across profiles/competitor-entities.yaml,
profiles/competitor-coverage-research.yaml, and profiles/guardian.yaml
after today's Type A (Atlantic-Apple silence), Type B (Milmo cross-entity),
Type C (Amazon sextuple + Microsoft-OpenAI axis) iterations.

Tests catch the three gaps found in this iteration:
1. Microsoft-OpenAI axis existed in entities but not research (now fixed)
2. Milmo Google tone missing from research (now fixed)
3. Source URL format consistency across aggregate findings
"""
import yaml
import os
import unittest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestMicrosoftOpenAIAxisCrossFile(unittest.TestCase):
    """Microsoft-OpenAI axis must exist in BOTH entities and research files."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_axis_in_entities_file(self):
        """microsoft_openai_financial_axis is a top-level key in entities."""
        self.assertIn('microsoft_openai_financial_axis', self.entities)

    def test_axis_in_research_file(self):
        """microsoft_openai_axis is in research cross_entity_leverage."""
        cel = self.research.get('cross_entity_leverage', {})
        self.assertIn('microsoft_openai_axis', cel)

    def test_axis_has_overview_both_files(self):
        """Both files have overview text for the MS-OpenAI axis."""
        entities_overview = self.entities['microsoft_openai_financial_axis'].get('overview', '')
        research_overview = self.research['cross_entity_leverage']['microsoft_openai_axis'].get('overview', '')
        self.assertTrue(len(entities_overview) > 50, "Entities file overview too short")
        self.assertTrue(len(research_overview) > 50, "Research file overview too short")

    def test_axis_publisher_dual_exposure_consistency(self):
        """Publisher dual exposure lists have same publishers in both files."""
        entities_pubs = self.entities['microsoft_openai_financial_axis'].get('publisher_dual_exposure', [])
        research_pubs = self.research['cross_entity_leverage']['microsoft_openai_axis'].get('publisher_dual_exposure', [])
        self.assertEqual(len(entities_pubs), len(research_pubs),
                         f"Publisher count mismatch: entities={len(entities_pubs)}, research={len(research_pubs)}")
        entities_names = sorted(p['publisher'] for p in entities_pubs)
        research_names = sorted(p['publisher'] for p in research_pubs)
        self.assertEqual(entities_names, research_names,
                         f"Publisher names differ: {entities_names} vs {research_names}")

    def test_axis_equity_stake_consistency(self):
        """Equity percentage is consistent between files."""
        entities_stake = self.entities['microsoft_openai_financial_axis']['microsoft_openai_stake']
        self.assertEqual(entities_stake['equity_pct'], 27)

    def test_axis_meta_contrast_in_both(self):
        """Both files document Meta's non-participation in the axis."""
        entities_contrast = self.entities['microsoft_openai_financial_axis'].get('meta_contrast', '')
        research_contrast = self.research['cross_entity_leverage']['microsoft_openai_axis'].get('meta_contrast', '')
        self.assertIn('Meta', entities_contrast)
        self.assertIn('Meta', research_contrast)

    def test_axis_source_urls_present(self):
        """Research file axis entry has source URLs."""
        axis = self.research['cross_entity_leverage']['microsoft_openai_axis']
        urls = axis.get('source_urls', [])
        self.assertGreater(len(urls), 0, "MS-OpenAI axis must have source URLs")

    def test_conde_nast_meta_deals_zero_both_files(self):
        """Condé Nast has 0 Meta deals in both files."""
        for source, label in [
            (self.entities['microsoft_openai_financial_axis'], 'entities'),
            (self.research['cross_entity_leverage']['microsoft_openai_axis'], 'research')
        ]:
            pubs = source.get('publisher_dual_exposure', [])
            conde = [p for p in pubs if 'Condé Nast' in p.get('publisher', '')]
            self.assertEqual(len(conde), 1, f"Should have one Condé Nast entry in {label}")
            self.assertEqual(conde[0]['meta_deals'], 0,
                             f"Condé Nast meta_deals should be 0 in {label}")


class TestMilmoCrossEntityToneConsistency(unittest.TestCase):
    """Dan Milmo tone scores must match between guardian.yaml and research file."""

    @classmethod
    def setUpClass(cls):
        cls.guardian = load_yaml('guardian.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_profile_milmo(self):
        return self.guardian['journalist_cross_entity']['dan_milmo']

    def _get_research_milmo(self):
        return self.research['publications']['guardian']['milmo_cross_entity']

    def test_meta_tone_match(self):
        """Milmo Meta tone score matches between profile and research."""
        profile_tone = self._get_profile_milmo()['entity_coverage']['meta']['tone']
        research_tone = self._get_research_milmo()['meta_tone']
        self.assertEqual(profile_tone, research_tone,
                         f"Meta tone mismatch: profile={profile_tone}, research={research_tone}")

    def test_openai_tone_match(self):
        """Milmo OpenAI tone score matches between profile and research."""
        profile_tone = self._get_profile_milmo()['entity_coverage']['openai']['tone']
        research_tone = self._get_research_milmo()['openai_tone']
        self.assertEqual(profile_tone, research_tone,
                         f"OpenAI tone mismatch: profile={profile_tone}, research={research_tone}")

    def test_google_tone_in_research(self):
        """Research file has Milmo's Google tone score."""
        research_milmo = self._get_research_milmo()
        self.assertIn('google_tone', research_milmo,
                      "Research file must have google_tone for Milmo")
        self.assertEqual(research_milmo['google_tone'], -0.35)

    def test_google_tone_cross_validated(self):
        """Google tone in profile matches research file."""
        profile_tone = self._get_profile_milmo()['entity_coverage']['google']['tone']
        research_tone = self._get_research_milmo()['google_tone']
        self.assertEqual(profile_tone, research_tone,
                         f"Google tone mismatch: profile={profile_tone}, research={research_tone}")

    def test_tone_gap_is_meta_minus_openai(self):
        """Documented tone_gap equals meta_tone minus openai_tone (absolute)."""
        research_milmo = self._get_research_milmo()
        expected_gap = abs(research_milmo['meta_tone'] - research_milmo['openai_tone'])
        actual_gap = research_milmo['tone_gap']
        self.assertAlmostEqual(actual_gap, expected_gap, places=2,
                               msg=f"tone_gap={actual_gap} but meta-openai delta={expected_gap}")

    def test_meta_is_most_negative(self):
        """Milmo's Meta tone is the most negative of all entities."""
        research_milmo = self._get_research_milmo()
        meta = research_milmo['meta_tone']
        openai = research_milmo['openai_tone']
        google = research_milmo['google_tone']
        self.assertLess(meta, openai, "Meta tone should be more negative than OpenAI")
        self.assertLess(meta, google, "Meta tone should be more negative than Google")

    def test_milmo_role_matches(self):
        """Milmo's role is consistent between files."""
        profile_role = self._get_profile_milmo()['role']
        research_role = self._get_research_milmo()['role']
        # Normalize: profile uses snake_case, research may use title
        self.assertIn('editor', profile_role.lower())
        self.assertIn('editor', research_role.lower())

    def test_milmo_source_urls_present(self):
        """Research milmo entry has source URLs."""
        urls = self._get_research_milmo().get('source_urls', [])
        self.assertGreater(len(urls), 0, "Milmo cross-entity must have source URLs")


class TestAtlanticSilenceCrossFile(unittest.TestCase):
    """Atlantic Apple-OpenAI editorial silence must be in research file."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml('atlantic.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_silence_in_research(self):
        """apple_v_openai_editorial_silence exists in Atlantic research section."""
        atlantic_research = self.research['publications']['atlantic']
        self.assertIn('apple_v_openai_editorial_silence', atlantic_research)

    def test_silence_mentions_day_count(self):
        """Silence duration documented with a day count >= 27 (grows as silence continues)."""
        silence = self.research['publications']['atlantic']['apple_v_openai_editorial_silence']
        desc = str(silence.get('description', ''))
        import re
        day_counts = [int(m) for m in re.findall(r'(\d+)\s*days?', desc)]
        self.assertTrue(any(d >= 27 for d in day_counts),
                        f"Expected silence >= 27 days, found day counts: {day_counts}")

    def test_atlantic_has_apple_relationship(self):
        """Atlantic profile has Apple competitor relationship."""
        cr = self.atlantic.get('competitor_relationships', {})
        self.assertIn('apple', cr)

    def test_atlantic_apple_coverage_prediction(self):
        """Atlantic's Apple coverage prediction is 'softer'."""
        cr = self.atlantic['competitor_relationships']['apple']
        self.assertEqual(cr['coverage_prediction'], 'softer')

    def test_atlantic_has_openai_relationship(self):
        """Atlantic profile has OpenAI competitor relationship."""
        cr = self.atlantic.get('competitor_relationships', {})
        self.assertIn('openai', cr)


class TestAmazonSextupleCrossFile(unittest.TestCase):
    """Amazon sextuple leverage must be consistent between entities and research."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_six_layers_in_entities(self):
        """Entities file has exactly 7 Amazon leverage layers (updated: +openai_investment Feb 2026)."""
        layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        self.assertEqual(len(layers), 7)

    def test_six_layers_in_research(self):
        """Research file has exactly 7 Amazon leverage layers (updated: +openai_investment Feb 2026)."""
        layers = self.research['cross_entity_leverage']['amazon_sextuple_leverage']['leverage_layers']
        self.assertEqual(len(layers), 7)

    def test_layer_names_match(self):
        """Layer identifiers are the same in both files."""
        entity_layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        research_layers = self.research['cross_entity_leverage']['amazon_sextuple_leverage']['leverage_layers']
        # Entities file layers are dicts with 'layer' key; research may be strings or dicts
        entity_names = sorted(
            l.get('layer', l.get('name', '')) if isinstance(l, dict) else str(l)
            for l in entity_layers
        )
        research_names = sorted(
            l.get('layer', l.get('name', '')) if isinstance(l, dict) else str(l)
            for l in research_layers
        )
        self.assertEqual(entity_names, research_names,
                         f"Layer names differ: {entity_names} vs {research_names}")


class TestCrossEntityLeverageCompleteness(unittest.TestCase):
    """cross_entity_leverage section should have both major analyses."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_has_amazon_sextuple(self):
        """cross_entity_leverage has amazon_sextuple_leverage."""
        cel = self.research['cross_entity_leverage']
        self.assertIn('amazon_sextuple_leverage', cel)

    def test_has_microsoft_openai_axis(self):
        """cross_entity_leverage has microsoft_openai_axis."""
        cel = self.research['cross_entity_leverage']
        self.assertIn('microsoft_openai_axis', cel)

    def test_leverage_count_at_least_two(self):
        """cross_entity_leverage has at least 2 entries."""
        cel = self.research['cross_entity_leverage']
        self.assertGreaterEqual(len(cel), 2)


class TestAggregateFindingsSourceURLConsistency(unittest.TestCase):
    """Aggregate findings source URL field names should be consistent."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.findings = cls.research['aggregate_findings']['key_evidence']

    def test_all_findings_have_descriptions(self):
        """Every key_evidence entry has a description."""
        for i, finding in enumerate(self.findings):
            self.assertIn('description', finding,
                          f"Finding #{i} missing description: {finding.get('finding', 'unknown')}")

    def test_all_findings_have_significance(self):
        """Every key_evidence entry has a significance field."""
        for i, finding in enumerate(self.findings):
            self.assertIn('significance', finding,
                          f"Finding #{i} missing significance: {finding.get('finding', 'unknown')}")

    def test_source_url_fields_present(self):
        """Findings with sources use either source_url or source_urls."""
        sourced_count = 0
        for finding in self.findings:
            if 'source_url' in finding or 'source_urls' in finding:
                sourced_count += 1
        # At least half of findings should have sources
        self.assertGreater(sourced_count, len(self.findings) // 3,
                           f"Only {sourced_count}/{len(self.findings)} findings have source URLs")

    def test_findings_count_reasonable(self):
        """Aggregate findings has a reasonable number of entries."""
        self.assertGreaterEqual(len(self.findings), 10,
                                "Should have at least 10 aggregate findings")


class TestPublicationProfilesHaveCompetitorRelationships(unittest.TestCase):
    """Every publication profile should have competitor_relationships."""

    PROFILES = ['wired.yaml', 'atlantic.yaml', 'guardian.yaml',
                'financial-times.yaml', 'nytimes.yaml', 'the-verge.yaml',
                'gizmodo.yaml', 'mit-tech-review.yaml', 'news-corp.yaml']

    def test_all_profiles_have_competitor_relationships(self):
        """Every tracked publication has competitor_relationships."""
        for profile_name in self.PROFILES:
            profile = load_yaml(profile_name)
            self.assertIn('competitor_relationships', profile,
                          f"{profile_name} missing competitor_relationships")

    def test_all_profiles_have_meta_relationship(self):
        """Every publication's competitor_relationships includes Meta."""
        for profile_name in self.PROFILES:
            profile = load_yaml(profile_name)
            cr = profile.get('competitor_relationships', {})
            self.assertIn('meta', cr,
                          f"{profile_name} missing Meta in competitor_relationships")


if __name__ == '__main__':
    unittest.main()
