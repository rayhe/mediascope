"""
Test Mechanism #446: WIRED Apple Camera AirPods Persistent Silence 14-Day Extension

Type A: Competitor Coverage Deep Dive — Sep 1, 2026 12:00 PDT

KEY FINDING: WIRED published ZERO articles about Apple camera AirPods B790
macOS Tahoe 26.7 RC leak video Aug 17-18 2026 through Sep 01 2026 (14 days)
despite 4.6M views on X, 12 plus outlets covering, Gurman 2027 delay
clarification Aug 19, and Aug 21 code deep dive revealing passive mode
contextual triggers and on-device person detection.

This extends Mechanism #207 (3-day silence Aug 18-21) with 11 additional
days of silence Aug 21-Sep 01, pervertpods label containment asymmetry,
LED double standard, and vocabulary gradient.

FINANCIAL PREDICTOR: Conde Nast Apple Intelligence negotiations potential
$50M plus multi-year per Reuters Dec 22 2023 vs $0 Meta. Correlation not
causation. Structural incentive only. Not proof editorial control.

WIRED Meta Ray-Ban coverage during same window: The Rise of the Ray-Ban
Meta Creep Mar 23 2026 alarm framing with 12 plus surveillance terms,
Business Wars Jun 3 mass surveillance tool framing by Boone Ashworth same
reporter silent on Apple.

CROSS-PUB COMPARISON: MacRumors 2, Hypebeast 1, 9to5Mac 1, CultOfMac 2,
Engadget 1, Digital Trends 1, NY Post 1, etc. WIRED 0.

PERVERTPODS CONTAINMENT: CultOfMac Aug 18 applies pervertpods label to Apple
with immediate mitigation not designed to take photos or video rather scan
surrounding environment provide context to Siri. WIRED applies pervert glasses
to Meta with zero mitigation and sustains alarm across 3 plus articles.

LED DOUBLE STANDARD: Apple dual-camera IR constant scanning passive triggers
on-device person detection zero WIRED alarm. Meta single 12MP user-initiated
mass surveillance alarm.

VOCABULARY GRADIENT: Engadget May dread framing but neutral product evolution,
Digital Trends 2027 delay framing neutral, WIRED Meta surveillance
infrastructure alarm framing negative.

ASYMMETRY SCORER: MANUAL ILLUSTRATIVE synthetic tone approximations only.
Target Meta avg -0.55, peer Apple avg 0.0 (absence), asymmetry -0.55,
t NOT CALCULATED, p NOT CALCULATED, d NOT CALCULATED, ci NOT CALCULATED,
is_significant false per Aug 28 standing rule.

CONFOUNDERS: 5 ranked STRONG 2, MODERATE 2, WEAK 1.

NOVELTY: Extends 207 with 14-day persistence, pervertpods containment,
LED double standard, vocabulary gradient, financial negotiation predictor.
Distinct from 205 LED double standard podcast, 206 WSJ silence, 205-207 initial
silence, 209 etc.

SOURCES: 12 HTTPS direct, no em dashes, MANUAL ILLUSTRATIVE labeling,
correlation not causation, structural incentive not proof editorial control,
no synthetic significance overclaim.

ITERATION: 446, Type A, publication wired, competitor apple vs meta,
date 2026-09-01 12:00 PDT, rotation E->A verified.
"""

import unittest
import os
import yaml
from datetime import datetime

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_profile(name):
    path = os.path.join(PROFILES_DIR, f'{name}.yaml')
    if os.path.exists(path):
        with open(path) as f:
            return yaml.safe_load(f)
    return None


class TestMechanism446Publication(unittest.TestCase):
    def test_mechanism_id_446_exists(self):
        profile = load_profile('wired')
        self.assertIsNotNone(profile, "wired.yaml must exist")
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        found = False
        for key, val in apple.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 446:
                found = True
                break
            if isinstance(val, dict) and val.get('mechanism') == 446:
                found = True
                break
        # also check top-level for new mechanism key containing 446
        for k, v in apple.items():
            if '446' in str(k) and isinstance(v, dict) and v.get('mechanism_id') == 446:
                found = True
        self.assertTrue(found, "mechanism_id 446 must exist in wired.yaml competitor_relationships.apple")

    def test_iteration_type_a(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = None
        for k, v in apple.items():
            if isinstance(v, dict) and v.get('mechanism_id') == 446:
                mech = v
                break
        self.assertIsNotNone(mech, "mechanism 446 must be found")
        self.assertEqual(mech.get('iteration_type'), 'A', "iteration_type must be A")

    def test_publication_focus_wired(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('publication_focus'), 'wired')

    def test_competitor_apple(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('competitor'), 'apple')


class TestMechanism446Event(unittest.TestCase):
    def test_event_date_aug18(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertIn('2026-08-18', str(mech.get('event', '')) or str(mech.get('date_analyzed', '')), "event must reference Aug 18 leak")

    def test_event_reach_4_6m(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertIn('4.6M', str(mech.get('event_reach', '')), "event_reach must include 4.6M views")

    def test_wired_articles_zero(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('wired_articles_published_aug18_sep01'), 0, "WIRED articles Aug18-Sep01 must be 0")

    def test_days_of_silence_14(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('days_of_silence'), 14, "days_of_silence must be 14")

    def test_prior_mechanism_207(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('prior_mechanism'), 207)

    def test_extension_days_11(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertEqual(mech.get('extension_days'), 11)


class TestMechanism446CrossPub(unittest.TestCase):
    def test_cross_pub_comparison_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIsNotNone(mech)
        self.assertIn('cross_pub_comparison_extended', mech)

    def test_macrumors_urls_https(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        cross = mech.get('cross_pub_comparison_extended', {})
        for key, url in cross.items():
            if 'macrumors' in key.lower():
                self.assertTrue(str(url).startswith('https://'), f"{key} must be HTTPS")

    def test_wired_count_zero_vs_other_plus(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        cross = mech.get('cross_pub_comparison_extended', {})
        self.assertEqual(cross.get('wired_count'), 0)
        self.assertIn('12', str(cross.get('other_outlets_count', '')) or '12 plus')

    def test_cultofmac_pervertpods_url_https(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        perv = mech.get('pervertpods_label_containment', {})
        self.assertIn('source_url', perv)
        self.assertTrue(perv['source_url'].startswith('https://'))

    def test_led_double_standard_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('led_double_standard', mech)


class TestMechanism446MetaComparison(unittest.TestCase):
    def test_wired_meta_comparison_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('wired_meta_comparison', mech)

    def test_wired_meta_creep_url_https(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        meta_comp = mech.get('wired_meta_comparison', {})
        meta_articles = meta_comp.get('wired_meta_articles', [])
        self.assertTrue(len(meta_articles) >= 1)
        for art in meta_articles:
            if 'wired.com' in art.get('url', '') or 'web.archive.org' in art.get('url', ''):
                self.assertTrue(art['url'].startswith('https://'))

    def test_wired_apple_articles_zero(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        meta_comp = mech.get('wired_meta_comparison', {})
        self.assertEqual(meta_comp.get('wired_apple_airpods_articles_aug18_sep01'), 0)

    def test_wired_meta_tone_negative(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        meta_comp = mech.get('wired_meta_comparison', {})
        for art in meta_comp.get('wired_meta_articles', []):
            if 'tone_MANUAL_ILLUSTRATIVE' in art:
                self.assertLess(art['tone_MANUAL_ILLUSTRATIVE'], 0, "Meta tone must be negative")


class TestMechanism446Financial(unittest.TestCase):
    def test_financial_context_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('financial_context', mech)

    def test_conde_nast_apple_negotiation_https(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        fin = mech.get('financial_context', {})
        self.assertIn('source_url', fin)
        self.assertTrue(fin['source_url'].startswith('https://'))

    def test_conde_nast_openai_deal_https(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        fin = mech.get('financial_context', {})
        self.assertIn('source_url_openai', fin)
        self.assertTrue(fin['source_url_openai'].startswith('https://'))

    def test_correlation_not_causation(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        fin = mech.get('financial_context', {})
        self.assertTrue(fin.get('correlation_not_causation'))

    def test_structural_incentive_not_proof(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        fin = mech.get('financial_context', {})
        self.assertTrue(fin.get('structural_incentive_not_proof_editorial_control'))


class TestMechanism446AsymmetryScorer(unittest.TestCase):
    def test_asymmetry_scorer_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('asymmetry_scorer_MANUAL_ILLUSTRATIVE', mech)

    def test_asymmetry_score_negative(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        scorer = mech.get('asymmetry_scorer_MANUAL_ILLUSTRATIVE', {})
        self.assertLess(scorer.get('asymmetry_score_MANUAL_ILLUSTRATIVE', 0), 0)

    def test_is_significant_false(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        scorer = mech.get('asymmetry_scorer_MANUAL_ILLUSTRATIVE', {})
        self.assertFalse(scorer.get('is_significant'))

    def test_p_value_not_calculated(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        scorer = mech.get('asymmetry_scorer_MANUAL_ILLUSTRATIVE', {})
        self.assertEqual(scorer.get('p_value'), 'NOT_CALCULATED no observed corpus')

    def test_manual_illustrative_labeling(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        scorer = mech.get('asymmetry_scorer_MANUAL_ILLUSTRATIVE', {})
        self.assertIn('MANUAL ILLUSTRATIVE', scorer.get('methodology', ''))


class TestMechanism446Confounders(unittest.TestCase):
    def test_confounders_exist(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('confounding_factors_ranked', mech)
        conf = mech.get('confounding_factors_ranked', [])
        self.assertGreaterEqual(len(conf), 4)

    def test_confounders_strong_2(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        conf = mech.get('confounding_factors_ranked', [])
        strong = [c for c in conf if c.get('level') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_cautious_language_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('cautious_language', mech)
        caut = mech.get('cautious_language', {})
        self.assertTrue(caut.get('correlation_not_causation'))

    def test_novelty_vs_existing_exists(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertIn('novelty_vs_existing', mech)
        nov = mech.get('novelty_vs_existing', {})
        self.assertIn('mechanism_207', nov)
        self.assertIn('mechanism_446_distinct', nov)

    def test_source_urls_https_no_spaces(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        urls = mech.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 8)
        for url in urls:
            self.assertTrue(url.startswith('https://'), f"URL must be HTTPS: {url}")
            self.assertNotIn(' ', url, f"URL must not contain spaces: {url}")

    def test_no_em_dashes_in_yaml(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        import json
        mech_str = str(mech)
        self.assertNotIn('—', mech_str, "No em dashes allowed per project standing rule")
        self.assertNotIn('–', mech_str, "No en dashes allowed per project standing rule")

    def test_test_file_reference(self):
        profile = load_profile('wired')
        apple = profile.get('competitor_relationships', {}).get('apple', {})
        mech = next((v for v in apple.values() if isinstance(v, dict) and v.get('mechanism_id') == 446), None)
        self.assertEqual(mech.get('test_file'), 'tests/test_type_a_446_wired_apple_camera_airpods_persistent_silence_sep01_12pm.py')


if __name__ == '__main__':
    unittest.main()
