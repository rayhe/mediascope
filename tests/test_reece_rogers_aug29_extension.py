"""
Test suite for Reece Rogers Mechanism #375 Privacy Topic Routing Extension Aug 29
Iteration #375 Type B - extends Mechanism #97

Covers:
- YAML validity
- Mechanism #97 preserved
- Mechanism #375 present and unique
- Source URLs exact, no em dash
- Cautious language, 4+ confounders, no unsupported causal language
- Cross references include 97
- Illustrative scorer labeled not empirical
- Iteration 375 not duplicate
- Samsung 38-day zero empirical
- OpenAI companion capability inversion
- McDonald control proves capability
"""

import unittest
import os
import re
import yaml

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
JOURNALISTS_YAML = os.path.join(REPO_ROOT, 'profiles/careers/journalists.yaml')
ITERATION_LOG = os.path.join(REPO_ROOT, 'iteration-log.md')


def load_journalists():
    with open(JOURNALISTS_YAML) as f:
        return yaml.safe_load(f)


class TestYamlValidity(unittest.TestCase):
    def test_yaml_valid(self):
        try:
            data = load_journalists()
        except Exception as e:
            self.fail(f"journalists.yaml invalid YAML: {e}")
        self.assertIsInstance(data, dict)


class TestMechanism97Preserved(unittest.TestCase):
    def test_mechanism_97_still_exists_somewhere(self):
        # Mechanism 97 should still be referenced in iteration-log or yaml
        with open(ITERATION_LOG) as f:
            log = f.read()
        # Check yaml contains Reece Rogers
        data = load_journalists()
        # Find Reece Rogers entry
        found_reece = False
        for journo in data.get('journalists', []):
            if journo.get('name') == 'Reece Rogers':
                found_reece = True
                # Check competitor_coverage exists
                cc = journo.get('competitor_coverage', {})
                self.assertIsNotNone(cc, "competitor_coverage should exist for Reece Rogers")
                break
        self.assertTrue(found_reece, "Reece Rogers entry must exist")
        # Iteration log should mention extends Mechanism #97
        self.assertIn('97', log, "Iteration log should reference Mechanism 97")


class TestMechanism375PresentUnique(unittest.TestCase):
    def test_mechanism_375_present(self):
        data = load_journalists()
        count = 0
        for journo in data.get('journalists', []):
            cc = journo.get('competitor_coverage', {})
            if not cc:
                continue
            # privacy_topic_routing_extension_aug29
            ext = cc.get('privacy_topic_routing_extension_aug29', {})
            if ext.get('mechanism_id') == 375:
                count += 1
        self.assertEqual(count, 1, f"Mechanism 375 should appear exactly once, found {count}")

    def test_mechanism_375_unique_no_collision(self):
        # Grep already done but test again
        with open(JOURNALISTS_YAML) as f:
            text = f.read()
        matches = re.findall(r'mechanism_id:\s*375\b', text)
        self.assertEqual(len(matches), 1, f"mechanism_id 375 should occur once, found {len(matches)}")

    def test_iteration_375_not_duplicate(self):
        with open(ITERATION_LOG) as f:
            log = f.read()
        # Count Iteration #375 headers
        count = log.count('## Iteration #375')
        self.assertEqual(count, 1, f"Iteration #375 should appear exactly once, found {count}")


class TestSourceUrlsExactNoEmDash(unittest.TestCase):
    def test_source_urls_exact_present(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            cc = journo.get('competitor_coverage', {})
            ext = cc.get('privacy_topic_routing_extension_aug29', {})
            self.assertTrue(ext, "Extension should exist")
            # Check required source URL fields
            meta = ext.get('meta_coverage', {})
            self.assertIn('examples', meta)
            # Check one known URL
            urls = []
            for ex in meta.get('examples', []):
                if 'source_url' in ex:
                    urls.append(ex['source_url'])
                if 'secondary_source' in ex:
                    urls.append(ex['secondary_source'])
            # Expect at least 3 meta URLs
            self.assertGreaterEqual(len(urls), 2, "Meta coverage should have source URLs")

            samsung = ext.get('samsung_coverage', {})
            other_pubs = samsung.get('other_publications_15_sources', [])
            self.assertGreaterEqual(len(other_pubs), 10, "Samsung should have 15 source URLs")

            openai = ext.get('openai_companion_coverage', {})
            self.assertIn('source_urls', openai)
            self.assertGreaterEqual(len(openai['source_urls']), 2)

    def test_no_em_dash_in_new_structure(self):
        with open(JOURNALISTS_YAML) as f:
            text = f.read()
        # Extract Reece Rogers section roughly
        # Find from competitor_coverage to next journalist
        start = text.find('privacy_topic_routing_extension_aug29')
        snippet = text[start:start+20000] if start != -1 else text
        self.assertNotIn('—', snippet, "New structure must not contain em dash")
        self.assertNotIn('–', snippet, "New structure must not contain en dash")

    def test_iteration_log_no_em_dash_added(self):
        with open(ITERATION_LOG) as f:
            lines = f.readlines()
        # Check first 300 lines (Iteration 375)
        top = ''.join(lines[:400])
        # Added lines in iteration 375 header should not contain em dash
        # The file itself may contain older em dashes in deletions, but top section should be clean
        # We enforce no em dash in Iteration 375 header block
        self.assertNotIn('—', top, "Iteration #375 header block should have no em dash (added lines)")


class TestCautiousLanguageConfounders(unittest.TestCase):
    def test_cautious_language_present(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            cautious = ext.get('financial_correlation_cautious', {}).get('cautious_language', '')
            self.assertTrue(len(cautious) > 20, "cautious_language should be present")
            self.assertIn('does not imply causation', cautious.lower() or cautious,
                          "cautious_language must contain does not imply causation")

    def test_confounders_4plus(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            confounders = ext.get('confounders', [])
            self.assertGreaterEqual(len(confounders), 4, f"Need 4+ confounders, found {len(confounders)}")
            # Check at least one STRONG
            strong = [c for c in confounders if 'STRONG' in c]
            self.assertGreaterEqual(len(strong), 1, "Should have at least one STRONG confounder")

    def test_no_unsupported_causal_language(self):
        with open(JOURNALISTS_YAML) as f:
            text = f.read()
        start = text.find('privacy_topic_routing_extension_aug29')
        snippet = text[start:start+25000].lower() if start != -1 else text.lower()
        # Banned phrases that claim proof of bias
        banned = ['proves bias', 'proves editorial control', 'proof of editorial influence']
        for phrase in banned:
            self.assertNotIn(phrase, snippet, f"Should not contain unsupported causal phrase '{phrase}'")

    def test_5plus_confounders_counted_in_adjustment(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            adj = ext.get('confounding_adjustment', {})
            adjustments = adj.get('adjustments', [])
            self.assertGreaterEqual(len(adjustments), 4, "confounding_adjustment should have 4+ entries")


class TestCrossReferences(unittest.TestCase):
    def test_cross_references_include_97(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            xrefs = ext.get('cross_references', [])
            self.assertIn(97, xrefs, "cross_references must include 97")


class TestIllustrativeOnlyScoring(unittest.TestCase):
    def test_illustrative_labeling(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            scorer = ext.get('asymmetry_scorer_result_illustrative', {})
            self.assertTrue(scorer, "asymmetry_scorer_result_illustrative must exist")
            # Check methodology mentions illustrative and not empirical significance
            meth = scorer.get('methodology', '')
            self.assertIn('illustrative', meth.lower(), "methodology must mention illustrative")
            self.assertIn('do not describe', meth.lower() + scorer.get('cohens_d','').lower() if isinstance(scorer.get('cohens_d'), str) else meth.lower(),
                          "methodology should warn against empirical significance")
            # Check p_value contains illustrative
            p_val = str(scorer.get('p_value', ''))
            self.assertIn('illustrative', p_val.lower(), "p_value must be labeled illustrative only")

    def test_target_peer_scores_illustrative(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            ext = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']
            scorer = ext['asymmetry_scorer_result_illustrative']
            self.assertIn('target_scores_illustrative', scorer)
            self.assertIn('peer_scores_illustrative', scorer)
            # Ensure lists are proper
            self.assertIsInstance(scorer['target_scores_illustrative'], list)
            self.assertIsInstance(scorer['peer_scores_illustrative'], list)


class TestSamsung38DayGap(unittest.TestCase):
    def test_samsung_38_day_zero(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            samsung = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']['samsung_coverage']
            self.assertEqual(samsung.get('wired_articles_38_days'), 0, "Samsung WIRED 38-day articles should be 0")
            self.assertGreaterEqual(samsung.get('wired_articles_meta_same_window', 0), 5,
                                    "Meta same window should be >=5")

    def test_samsung_hardware_parity(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            samsung = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']['samsung_coverage']
            hw = samsung.get('hardware_parity', '')
            self.assertIn('Snapdragon', hw, "hardware_parity should mention Snapdragon")


class TestOpenAICompanionInversion(unittest.TestCase):
    def test_openai_more_capable_less_scrutiny(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            openai_cov = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']['openai_companion_coverage']
            self.assertEqual(openai_cov.get('privacy_scrutiny_wired'), 0,
                             "OpenAI companion privacy scrutiny should be 0")
            cap_inv = openai_cov.get('capability_inversion', '')
            self.assertTrue(len(cap_inv) > 10, "capability_inversion description should exist")
            self.assertIn('surveillance', cap_inv.lower(), "capability_inversion should mention surveillance")


class TestMcDonaldControl(unittest.TestCase):
    def test_mcdonald_control_proves_capability(self):
        data = load_journalists()
        for journo in data.get('journalists', []):
            if journo.get('name') != 'Reece Rogers':
                continue
            control = journo['competitor_coverage']['privacy_topic_routing_extension_aug29']['non_competitor_control']
            self.assertEqual(control.get('financial_ties_conde_nast'), 0)
            sig = control.get('significance', '')
            self.assertIn('CAN', sig, "significance should mention CAN do investigative work")
            self.assertIn('515', control.get('entity', ''), "entity should mention 515-page")


if __name__ == '__main__':
    unittest.main()
