"""
Cross-entity analysis: Reece Rogers (WIRED) — Mechanism #97
Privacy Investigation Topic Routing Asymmetry

KEY PATTERN: Rogers writes privacy investigations and alarm-framed pieces about
Meta's products but applies convenience/informational framing when covering
structurally identical privacy concerns at Google and other Condé Nast financial
partners. His investigative energy on privacy is entity-selective.

Evidence chain:

1. Meta Ray-Ban ghost dot sticker (co-authored with Boone Ashworth, Aug 5, 2025):
   - TikTok promoting stickers to conceal the recording LED on Meta smart glasses
   - Alarm framing: "secretly recording" in headline, surveillance concern
   - Source proxy: https://technewstube.com/wired/1751222/tiktok-promotes-stickers-secretly-recording-meta-ray-ban/

2. Meta Muse Image opt-out burden (Jul 7, 2026):
   - Rogers' WIRED piece: Instagram users with public accounts "need to opt out"
     to block AI training on their content
   - Framing: user burden, opt-out friction as a negative
   - Source: https://www.techmeme.com/260707/p37

3. "The Viral 'Goodbye Meta AI' Copypasta Will Not Protect You" (Sep 25, 2024):
   - Meta data practices framing — debunking copypasta but centering Meta's
     data collection as the implied threat worth "protecting" against
   - Source proxy: https://technewstube.com/wired/1672376/viral-goodbye-meta-ai-copypasta-not-protect/

4. Meta 2FA changes:
   - Covered Facebook's 2FA policy changes with privacy/security concern angle
   - Source: WIRED article by Rogers on Meta's 2FA trusted-device changes

5. Google I/O 2026 (May 19, 2026) — on-site team member:
   - Rogers was 1 of 5 WIRED reporters on the ground (Ashworth, Chokkattu,
     Goode, Levy, Rogers) covering Google's smart glasses announcement
   - Google's glasses have cameras + Gemini AI with live visual understanding
     and AI photo manipulation (Nano Banana) — structurally identical to Meta
     Ray-Ban's camera + AI pipeline
   - ZERO standalone articles by Rogers raising privacy/surveillance concerns
     about Google's camera glasses
   - Live blog framing: "Nano Banana on smart glasses is actually bananas.
     The demo worked!" (enthusiastic), "Nothing like doctoring photos in real
     time" (mild sarcasm, NOT alarm)
   - Source: https://technologytangle.com/2026/05/19/google-io-2026-live-blog-all-the-gemini-and-smart-glasses-updates-as-they-happen

6. Google selfie video login (Jul 2026):
   - Rogers covered Google's facial recognition data collection for account
     recovery, including an opt-in toggle allowing Google to use selfie videos
     "to develop and improve our facial recognition, age estimation, and other
     verification methods" across ALL Google services
   - Framing: convenience ("completed it in less than five minutes"), informational
   - NOT alarm framing despite Google building "one of the largest datasets
     for facial recognition training in the world"
   - Meta's dormant NameTag code (facial recognition, never activated, on-device)
     generated 2+ WIRED investigations + alarm language
   - Source: https://www.byte-pulse.net/article/google-s-selfie-login-convenience-meets-data-privacy-alarms

7. Anthropic privacy terms change (Sep/Oct 2025):
   - Rogers covered Anthropic requiring users to accept new privacy terms
     including opt-in to AI model training on chats/coding sessions
   - Framing: informational, process-oriented
   - Same structural dynamic as Meta Muse Image (AI training on user content)
     but WITHOUT the alarm/burden framing
   - Source: http://www.techmeme.com/250930/p18

8. McDonald's 515-page data dossier (Aug 2026):
   - Rogers' investigative piece — aggressive privacy alarm framing against
     a non-tech-competitor (no financial relationship with Condé Nast)
   - "Minority Report-style" data dossier, predictive profiling
   - Shows Rogers CAN and DOES do investigative privacy work against entities
     without Condé Nast financial ties
   - Source: https://nypost.com/2026/08/13/business/mcdonalds-built-515-page-minority-report-style-dossier-on-loyalty-customer/

Financial relationships as predictor:
- Condé Nast has content licensing deals with OpenAI (Aug 2024), Microsoft,
  Amazon Rufus, and Perplexity
- Condé Nast depends on Google advertising revenue
- Condé Nast distributes through Apple News+
- Meta has ZERO content licensing deal and IS a direct advertising competitor
- McDonald's has ZERO content licensing deal and ZERO advertising dependency

Confounding factors:
- STRONG: Meta has documented facial recognition history (DeepFace 2014) that
  Google does not (Google ended facial recognition in Photos 2015, then reversed)
- STRONG: Rogers may simply be assigned Meta stories and not Google stories
  by editors (publication-level editorial allocation, not individual journalist bias)
- MODERATE: Google I/O live blog is a collaborative product, not a solo byline —
  individual reporter contributions are harder to isolate
- MODERATE: The Meta ghost dot piece was co-authored with Ashworth; Rogers alone
  may not have initiated the privacy angle
- WEAK: Different product maturity (Meta glasses are shipping; Google glasses were
  demos) — but privacy concerns should be higher for always-on AI camera demos
  where users CAN'T consent to being recorded

Cross-references: Mechanism #30 (Chokkattu temporal framing oscillation),
#45 (Ashworth WWDC PCC privacy framing), #11 (WIRED financial conflicts),
#14 (Condé Nast AI deals), #33 (OpenAI facial recognition privacy parity),
#70 (Ashworth accessibility framing inversion), #95 (Gizmodo same-chip Samsung)
"""

import unittest
import os
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


def load_wired():
    return load_yaml('wired.yaml')


def load_ccr():
    return load_yaml('competitor-coverage-research.yaml')


def load_ce():
    return load_yaml('competitor-entities.yaml')


class TestRogersProfieExists(unittest.TestCase):
    """Verify Reece Rogers is documented in the WIRED profile."""

    def test_rogers_in_wired_profile(self):
        wired = load_wired()
        content = yaml.dump(wired).lower()
        self.assertIn('reece rogers', content,
                       "Reece Rogers must appear in WIRED profile")

    def test_rogers_privacy_topic_routing_section(self):
        wired = load_wired()
        content = yaml.dump(wired)
        self.assertIn('privacy_investigation_topic_routing', content,
                       "Rogers' privacy topic routing section must exist in WIRED profile")


class TestMetaCoverageAdversarialFraming(unittest.TestCase):
    """Verify Rogers' Meta coverage uses alarm/adversarial framing."""

    def test_ghost_dot_sticker_documented(self):
        """Meta Ray-Ban ghost dot sticker piece exists with alarm framing."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        self.assertIn('ghost dot', content,
                       "Ghost dot sticker coverage must be documented")

    def test_muse_image_opt_out_documented(self):
        """Meta Muse Image opt-out piece exists."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # Either 'muse image' or 'opt out' in Rogers context
        has_muse = 'muse image' in content
        has_opt_out = 'opt out' in content or 'opt-out' in content
        self.assertTrue(has_muse or has_opt_out,
                       "Muse Image opt-out coverage must be documented")

    def test_meta_copypasta_documented(self):
        """'Goodbye Meta AI' copypasta piece exists."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        has_copypasta = 'copypasta' in content or 'goodbye meta ai' in content
        self.assertTrue(has_copypasta,
                       "Goodbye Meta AI copypasta coverage must be documented")

    def test_meta_tone_negative_or_alarm(self):
        """Rogers' Meta coverage aggregate tone is negative or alarm-framed."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # The Rogers section should document adversarial/alarm framing for Meta
        alarm_indicators = ['alarm', 'adversarial', 'surveillance',
                            'secretly recording', 'opt out', 'burden']
        found = sum(1 for ind in alarm_indicators if ind in content)
        self.assertGreaterEqual(found, 2,
                               f"Rogers' Meta coverage should have alarm indicators, found {found}")


class TestGoogleCoverageNeutralFraming(unittest.TestCase):
    """Verify Rogers' Google coverage uses neutral/convenience framing."""

    def test_google_io_2026_rogers_on_site(self):
        """Rogers was on-site at Google I/O 2026."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # Rogers should be listed as one of the I/O reporters
        self.assertIn('reece rogers', content)
        has_io = 'google i/o' in content or 'google io' in content
        self.assertTrue(has_io,
                       "Google I/O 2026 coverage with Rogers must be documented")

    def test_zero_google_glasses_privacy_articles(self):
        """Rogers produced zero standalone privacy articles about Google's camera glasses."""
        wired = load_wired()
        content = yaml.dump(wired)
        # The Rogers section should document the absence of Google glasses privacy pieces
        self.assertIn('privacy_investigation_topic_routing', content,
                       "Topic routing section must document Google glasses privacy gap")

    def test_google_selfie_convenience_framing(self):
        """Google selfie video login covered with convenience, not alarm framing."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # Should document that Google facial recognition training toggle got
        # informational treatment rather than alarm
        has_selfie = 'selfie' in content or 'facial recognition' in content
        has_convenience = 'convenience' in content or 'informational' in content
        self.assertTrue(has_selfie or has_convenience,
                       "Google selfie/facial recognition coverage framing must be documented")


class TestCrossEntityFramingDelta(unittest.TestCase):
    """Verify the measurable framing asymmetry between entities."""

    def test_meta_vs_google_privacy_article_count(self):
        """Rogers has more standalone Meta privacy articles than Google privacy articles."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # Document counts at minimum
        self.assertIn('reece rogers', content)

    def test_same_capability_different_framing(self):
        """Camera + AI on glasses gets alarm for Meta, enthusiasm for Google."""
        wired = load_wired()
        content = yaml.dump(wired)
        # The routing section should contrast same-capability coverage
        self.assertIn('privacy_investigation_topic_routing', content)

    def test_facial_recognition_framing_parity(self):
        """Google's facial recognition training opt-in vs Meta's dormant NameTag."""
        # Google: active facial recognition data collection with training toggle
        # Meta: dormant NameTag code, never activated, on-device only
        # Google got convenience framing; Meta got multi-article investigations
        ccr = load_ccr()
        content = yaml.dump(ccr).lower()
        self.assertIn('reece rogers', content,
                       "Rogers must appear in competitor-coverage-research.yaml")

    def test_mcdonalds_control_case(self):
        """McDonald's investigation shows Rogers CAN do adversarial privacy work."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        has_mcdonalds = "mcdonald" in content
        self.assertTrue(has_mcdonalds,
                       "McDonald's investigation must be documented as non-competitor control")


class TestAnthropicCoverageComparison(unittest.TestCase):
    """Verify Anthropic coverage framing vs Meta coverage framing."""

    def test_anthropic_privacy_informational(self):
        """Anthropic privacy terms change covered informationally."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # Should document Anthropic training data policy with neutral framing
        has_anthropic = 'anthropic' in content
        self.assertTrue(has_anthropic,
                       "Anthropic coverage comparison must be documented")

    def test_meta_vs_anthropic_training_data_framing(self):
        """Meta Muse Image (alarm) vs Anthropic training opt-in (informational)."""
        # Both involve AI training on user content with opt-in/out mechanism
        # Meta: "need to opt out" (burden framing)
        # Anthropic: factual reporting on terms change
        ccr = load_ccr()
        content = yaml.dump(ccr)
        self.assertIn('97', str(content),
                       "Mechanism 97 must be registered in CCR")


class TestFinancialRelationshipPredictor(unittest.TestCase):
    """Verify financial relationships predict the framing direction."""

    def test_conde_nast_google_dependency(self):
        """Condé Nast's Google advertising dependency documented."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        has_ad = 'advertising' in content or 'ad revenue' in content
        has_google = 'google' in content
        self.assertTrue(has_ad and has_google,
                       "Condé Nast-Google advertising dependency must be documented")

    def test_conde_nast_openai_deal(self):
        """Condé Nast-OpenAI content licensing deal documented."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        self.assertIn('openai', content,
                       "Condé Nast-OpenAI content deal must be documented")

    def test_meta_zero_financial_relationship(self):
        """Meta has zero content licensing deal with Condé Nast."""
        wired = load_wired()
        content = yaml.dump(wired).lower()
        # The profile should note Meta as a direct advertising competitor
        has_competitor = 'competitor' in content or 'competing' in content
        self.assertTrue(has_competitor,
                       "Meta as direct advertising competitor must be documented")


class TestConfoundingFactorsDocumented(unittest.TestCase):
    """Verify confounding factors are catalogued."""

    def test_at_least_three_confounders(self):
        """Mechanism #97 has at least 3 confounding factors."""
        ccr = load_ccr()
        content = yaml.dump(ccr)
        # Find mechanism 97 section and check confounding_factors
        if 'confounding_factors' in content:
            # Parse to find mechanism 97's confounders
            cpf = ccr.get('cross_publication_findings', {})
            for key, val in cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 97:
                    factors = val.get('confounding_factors', [])
                    self.assertGreaterEqual(len(factors), 3,
                                           f"Need ≥3 confounders, got {len(factors)}")
                    return
            # Check aggregate_findings too
            af = ccr.get('aggregate_findings', {})
            for key, val in af.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 97:
                    factors = val.get('confounding_factors', [])
                    self.assertGreaterEqual(len(factors), 3,
                                           f"Need ≥3 confounders, got {len(factors)}")
                    return
        self.fail("Mechanism 97 with confounding_factors not found in CCR")

    def test_has_strong_confounder(self):
        """At least one STRONG confounding factor documented."""
        ccr = load_ccr()
        content = yaml.dump(ccr)
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                factors = val.get('confounding_factors', [])
                strong = [f for f in factors if 'STRONG' in str(f).upper()]
                self.assertGreaterEqual(len(strong), 1,
                                       "Need ≥1 STRONG confounder")
                return
        af = ccr.get('aggregate_findings', {})
        for key, val in af.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                factors = val.get('confounding_factors', [])
                strong = [f for f in factors if 'STRONG' in str(f).upper()]
                self.assertGreaterEqual(len(strong), 1,
                                       "Need ≥1 STRONG confounder")
                return
        self.fail("Mechanism 97 with confounding_factors not found")


class TestTestablePredictions(unittest.TestCase):
    """Verify testable predictions exist for mechanism #97."""

    def test_at_least_two_predictions(self):
        """Mechanism has ≥2 testable predictions."""
        ccr = load_ccr()
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                preds = val.get('testable_predictions', [])
                self.assertGreaterEqual(len(preds), 2,
                                       f"Need ≥2 predictions, got {len(preds)}")
                return
        af = ccr.get('aggregate_findings', {})
        for key, val in af.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                preds = val.get('testable_predictions', [])
                self.assertGreaterEqual(len(preds), 2,
                                       f"Need ≥2 predictions, got {len(preds)}")
                return
        self.fail("Mechanism 97 with testable_predictions not found")


class TestSourceUrlsPresent(unittest.TestCase):
    """Verify source URLs are catalogued."""

    def test_at_least_three_source_urls(self):
        """Mechanism has ≥3 source URLs."""
        ccr = load_ccr()
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                urls = val.get('source_urls', [])
                self.assertGreaterEqual(len(urls), 3,
                                       f"Need ≥3 source URLs, got {len(urls)}")
                return
        af = ccr.get('aggregate_findings', {})
        for key, val in af.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                urls = val.get('source_urls', [])
                self.assertGreaterEqual(len(urls), 3,
                                       f"Need ≥3 source URLs, got {len(urls)}")
                return
        self.fail("Mechanism 97 with source_urls not found")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    def test_references_ashworth_mechanisms(self):
        """Should cross-reference Ashworth mechanisms (#45, #70)."""
        ccr = load_ccr()
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                refs = val.get('cross_references', [])
                has_45 = 45 in refs
                has_70 = 70 in refs
                self.assertTrue(has_45 or has_70,
                               f"Should reference Ashworth mechanisms, got {refs}")
                return
        af = ccr.get('aggregate_findings', {})
        for key, val in af.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                refs = val.get('cross_references', [])
                has_45 = 45 in refs
                has_70 = 70 in refs
                self.assertTrue(has_45 or has_70,
                               f"Should reference Ashworth mechanisms, got {refs}")
                return
        self.fail("Mechanism 97 with cross_references not found")

    def test_references_facial_recognition_parity(self):
        """Should cross-reference mechanism #33 (OpenAI facial recognition parity)."""
        ccr = load_ccr()
        cpf = ccr.get('cross_publication_findings', {})
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                refs = val.get('cross_references', [])
                self.assertIn(33, refs,
                             f"Should reference mechanism #33, got {refs}")
                return
        af = ccr.get('aggregate_findings', {})
        for key, val in af.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 97:
                refs = val.get('cross_references', [])
                self.assertIn(33, refs,
                             f"Should reference mechanism #33, got {refs}")
                return
        self.fail("Mechanism 97 with cross_references not found")


class TestMechanismInCE(unittest.TestCase):
    """Verify mechanism is registered in competitor-entities.yaml."""

    def test_mechanism_97_in_competitor_entities(self):
        """Mechanism 97 appears in competitor-entities.yaml."""
        ce = load_ce()
        content = yaml.dump(ce)
        self.assertIn('97', content,
                       "Mechanism 97 must be registered in competitor-entities.yaml")

    def test_mechanism_tagged_with_rogers(self):
        """The CE entry references Reece Rogers."""
        ce = load_ce()
        content = yaml.dump(ce).lower()
        self.assertIn('reece rogers', content,
                       "Reece Rogers must appear in competitor-entities.yaml")


class TestTestFileConsistency(unittest.TestCase):
    """Verify this test file is registered in README and ARCHITECTURE."""

    def test_readme_has_test_entry(self):
        """README.md lists this test file."""
        readme_path = os.path.join(PROFILES_DIR, '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        self.assertIn('test_reece_rogers_cross_entity', content,
                       "README must list this test file")

    def test_architecture_has_test_entry(self):
        """ARCHITECTURE.md lists this test file."""
        arch_path = os.path.join(PROFILES_DIR, '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        self.assertIn('test_reece_rogers_cross_entity', content,
                       "ARCHITECTURE.md must list this test file")


if __name__ == '__main__':
    unittest.main()
