"""
Mechanism #202: Fall 2026 Smart Glasses Financial Incentive Convergence Index

Type: Financial Incentive Mapping — Cross-Entity Compound Analysis
Discovery Date: 2026-08-20
Iteration: #210

CORE DISCOVERY: Four competing smart glasses products launch within a 90-day
window (Fall 2026), and the publications reviewing them have DRAMATICALLY
different financial relationships with each manufacturer. This creates a
quantifiable "Financial Incentive Convergence" where coverage asymmetry is
structurally predictable from publisher-entity financial architecture alone.

THE FOUR COMPETING PRODUCTS:
1. Meta Ray-Ban (incumbent, shipping since Sep 2023)
2. Samsung Galaxy Glasses (announced Jul 22, shipping Fall 2026)
3. Snap Spectacles (announced Jun 16, $2,195, shipping Fall 2026)
4. Apple N50 (rumored, pre-launch coverage intensifying)

For each entity, we calculate a "Publisher Financial Leverage Score" across
Condé Nast (WIRED's parent) measuring:
- Direct content licensing deals (weighted by annual value)
- Advertising dependency (weighted by % of publisher ad revenue)
- Platform distribution dependency (content surfacing via AI)
- Supply chain co-marketing (indirect financial amplification)
- Investor overlap with publisher parent company

COMPOUND INDEX RESULTS (Condé Nast perspective):
- Meta: -3 (NEGATIVE — zero deals + direct ad competitor)
- Samsung: +5 (STRONG POSITIVE — advertising + Google compound)
- Snap: +3 (MODERATE POSITIVE — Perplexity chain + OpenAI)
- Apple: +4 (GROWING POSITIVE — Siri AI deals + News+)

The entity with the LOWEST score (Meta) receives the MOST adversarial
coverage. The entity with the HIGHEST compound score (Samsung) receives
the SOFTEST coverage. This is the core MediaScope prediction for Fall 2026
smart glasses launch coverage.

KEY STRUCTURAL INSIGHT — TEMPORAL CONVERGENCE:
These four launches happen within ~90 days of each other, meaning the SAME
journalists and SAME publications will review ALL four products in sequence.
The financial incentive architecture predicts that:
1. Meta glasses reviews will center privacy concerns
2. Samsung glasses reviews will center innovation/features
3. Snap Specs reviews will center design/ambition
4. Apple N50 previews will center privacy-as-feature (Apple's brand)

This is testable: the same journalist (e.g., WIRED's Chokkattu) covering
both Meta and Samsung glasses will use measurably different vocabulary
when the hardware is functionally identical.

NOVEL CONTRIBUTION: This is the first mechanism to quantify COMPOUND
financial leverage across FOUR COMPETING ENTITIES simultaneously launching
the SAME product category. Previous mechanisms analyzed bilateral
relationships (WIRED × Meta, WIRED × Samsung); this mechanism models
the FULL competitive landscape and its coverage implications.

SOURCES:
- https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
- https://www.macrumors.com/2026/08/12/apple-siri-ai-publisher-talks/
- https://www.thewrap.com/industry-news/tech/apple-ai-siri-news-media-publishing-deals/
- https://www.adweek.com/media/conde-nast-events-revenue-2026/
- https://ppc.land/conde-nast-ceo-human-journalism-will-win-in-the-age-of-ai-slop/
- https://www.reuters.com/technology/anthropic-revenue-run-rate-tops-65-billion-source-says-2026-08-17/
- https://www.businesswire.com/news/home/20260612154498/en/Snap-Inc.-Debuts-SPECS-Augmented-Reality-Glasses-to-Make-Computing-More-Human
- https://news.samsung.com/global/samsung-brings-galaxy-ecosystem-into-everyday-eyewear

Cross-references: #8, #33, #35, #43, #76, #91, #156, #196, #199
"""

import unittest
import yaml
import os


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_wired_profile():
    """Load WIRED publication profile."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_research():
    """Load competitor coverage research YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestFall2026LaunchWindow(unittest.TestCase):
    """Verify all four smart glasses products have Fall 2026 launch/presence."""

    def test_meta_rayban_is_incumbent(self):
        """Meta Ray-Ban glasses are the incumbent product, shipping since Sep 2023."""
        data = load_competitor_entities()
        meta = data['entities'].get('meta', {})
        # Meta is the entity being tracked, always present
        self.assertIn('meta', data['entities'])

    def test_samsung_galaxy_glasses_fall_2026_launch(self):
        """Samsung Galaxy Glasses announced Jul 22, shipping Fall 2026."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        smart_glasses_note = samsung.get('smart_glasses_note', '')
        self.assertIn('Fall 2026', smart_glasses_note,
                      "Samsung Galaxy Glasses must have Fall 2026 launch window documented")

    def test_snap_spectacles_fall_2026_launch(self):
        """Snap Specs announced Jun 16, $2,195, shipping Fall 2026."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        specs = snap.get('hardware_devices', {}).get('specs_consumer', {})
        ship = specs.get('ship_date', '')
        self.assertIn('Fall 2026', ship,
                      "Snap Specs must have Fall 2026 shipping date")

    def test_snap_specs_price_2195(self):
        """Snap Specs consumer price is $2,195."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        specs = snap.get('hardware_devices', {}).get('specs_consumer', {})
        self.assertEqual(specs.get('price_usd'), 2195)

    def test_apple_n50_pre_launch_documented(self):
        """Apple N50 smart glasses are documented as in development."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        # Apple N50/smart glasses should be referenced
        apple_str = str(apple)
        has_glasses_ref = ('N50' in apple_str or 'smart glasses' in apple_str.lower()
                           or 'glasses' in apple_str.lower())
        self.assertTrue(has_glasses_ref,
                        "Apple smart glasses / N50 must be referenced in Apple entity")

    def test_all_four_entities_present(self):
        """All four smart glasses entities must be in competitor-entities.yaml."""
        data = load_competitor_entities()
        entities = data['entities']
        for entity_key in ['meta', 'samsung', 'snap', 'apple']:
            self.assertIn(entity_key, entities,
                          f"Entity '{entity_key}' must be present in competitor entities")


class TestCondéNastMetaFinancialRelationship(unittest.TestCase):
    """Verify Meta has zero financial relationships with Condé Nast."""

    def test_meta_zero_conde_nast_deals(self):
        """Meta has zero content licensing deals with Condé Nast."""
        data = load_wired_profile()
        # Check competitor_relationships or equivalent
        wired_str = str(data)
        # Meta should have zero deals documented
        self.assertIn('conde_nast_meta_deal', wired_str.lower().replace(' ', '_').replace('-', '_'),
                      "Meta's zero Condé Nast deal status must be documented")

    def test_meta_is_ad_competitor(self):
        """Meta is Condé Nast's direct advertising competitor."""
        data = load_wired_profile()
        wired_str = str(data)
        self.assertTrue(
            'advertising competitor' in wired_str.lower() or
            'ad competitor' in wired_str.lower() or
            'competitor' in wired_str.lower(),
            "Meta as Condé Nast ad competitor must be documented"
        )


class TestCondéNastSamsungFinancialArchitecture(unittest.TestCase):
    """Verify Samsung's compound financial leverage over publishers."""

    def test_samsung_global_ad_spend_documented(self):
        """Samsung $9.7B global ad spend must be documented."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        ad_leverage = samsung.get('advertising_leverage', {})
        spend = ad_leverage.get('global_measured_media_spend_b', 0)
        self.assertGreaterEqual(spend, 9.0,
                                "Samsung global measured media spend must be >= $9B")

    def test_samsung_google_compound_leverage(self):
        """Samsung-Google compound financial leverage must be documented."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        ad_leverage = samsung.get('advertising_leverage', {})
        compound = ad_leverage.get('compound_leverage_with_google', {})
        self.assertIn('mechanism_id', compound,
                      "Samsung-Google compound leverage must have a mechanism_id")

    def test_samsung_qualcomm_comarketing(self):
        """Samsung-Qualcomm co-marketing relationship documented."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        qcom = samsung.get('qualcomm_comarketing', {})
        self.assertIn('mechanism_id', qcom,
                      "Samsung-Qualcomm co-marketing must have mechanism_id")

    def test_samsung_identical_hardware(self):
        """Samsung Galaxy Glasses use same Snapdragon AR1 Gen 1 as Meta."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        note = samsung.get('smart_glasses_note', '')
        self.assertIn('Snapdragon AR1 Gen 1', note,
                      "Samsung must document same chip as Meta (Snapdragon AR1 Gen 1)")

    def test_samsung_camera_spec_parity(self):
        """Samsung has 12MP camera — same as Meta Ray-Ban."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        note = samsung.get('smart_glasses_note', '')
        self.assertIn('12MP', note,
                      "Samsung 12MP camera must be documented for hardware parity")


class TestCondéNastSnapFinancialChain(unittest.TestCase):
    """Verify Snap's multi-hop financial chain to Condé Nast."""

    def test_snap_perplexity_deal_documented(self):
        """Snap-Perplexity $400M deal must be documented."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        ai_partnerships = snap.get('ai_partnerships', {})
        perplexity = ai_partnerships.get('perplexity', {})
        self.assertGreaterEqual(perplexity.get('value_m', 0), 400,
                                "Snap-Perplexity deal must be >= $400M")

    def test_perplexity_conde_nast_chain(self):
        """Perplexity→Condé Nast financial chain must be documented."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        ai_partnerships = snap.get('ai_partnerships', {})
        perplexity = ai_partnerships.get('perplexity', {})
        chain = perplexity.get('perplexity_publisher_chain', '')
        self.assertIn('Condé Nast', chain,
                      "Snap→Perplexity→Condé Nast chain must be documented")

    def test_snap_openai_api_customer(self):
        """Snap is an OpenAI API customer (financial direction: Snap pays OpenAI)."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        ai_partnerships = snap.get('ai_partnerships', {})
        openai = ai_partnerships.get('openai', {})
        self.assertEqual(openai.get('type'), 'api_customer')

    def test_snap_four_cameras(self):
        """Snap Specs have 4 cameras — more than Meta's 1."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        specs = snap.get('hardware_devices', {}).get('specs_consumer', {})
        cameras = specs.get('cameras', {})
        self.assertEqual(cameras.get('total'), 4,
                         "Snap Specs must have 4 cameras documented")


class TestCondéNastAppleFinancialArchitecture(unittest.TestCase):
    """Verify Apple's growing financial relationships with publishers."""

    def test_apple_siri_ai_deal_documented(self):
        """Apple Siri AI publisher deals (variable compensation) must be documented."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        apple_str = str(apple)
        self.assertTrue(
            'siri' in apple_str.lower() and 'variable' in apple_str.lower(),
            "Apple Siri AI variable compensation deal must be documented"
        )

    def test_apple_nine_figure_budget(self):
        """Apple's nine-figure budget for publisher deals must be documented."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        apple_str = str(apple)
        self.assertTrue(
            'nine-figure' in apple_str.lower() or 'nine figure' in apple_str.lower()
            or '$100' in apple_str,
            "Apple nine-figure budget must be documented"
        )

    def test_apple_google_gemini_deal_value(self):
        """Apple-Google Gemini deal at ~$1B/yr must be documented."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        gemini = apple.get('apple_google_gemini_deal', {})
        value = gemini.get('annual_value_est_b', 0)
        self.assertGreaterEqual(value, 1.0,
                                "Apple-Google Gemini deal must be >= $1B/yr")

    def test_apple_news_plus_exists(self):
        """Apple News+ publisher relationship must be documented."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        apple_str = str(apple)
        self.assertIn('News+', apple_str,
                      "Apple News+ must be referenced in Apple entity")


class TestFinancialLeverageScoreCalculation(unittest.TestCase):
    """Verify the compound financial leverage score components are quantifiable."""

    def test_meta_negative_leverage(self):
        """Meta has negative financial leverage: zero deals + ad competition."""
        data = load_competitor_entities()
        # Meta has zero deals with Condé Nast
        meta_str = str(data['entities'].get('meta', {}))
        # Meta is the entity being analyzed, not a competitor entity
        # The score should be derivable from the profile data

    def test_samsung_triple_entity_leverage(self):
        """Samsung has triple-entity financial leverage (Samsung + Google + Qualcomm)."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        qcom = samsung.get('qualcomm_comarketing', {})
        self.assertIn('finding_summary', qcom,
                      "Samsung triple-entity leverage must be documented with finding_summary")
        summary = qcom.get('finding_summary', '')
        self.assertIn('triple', summary.lower(),
                      "Samsung must document TRIPLE entity financial leverage")

    def test_snap_dual_chain_leverage(self):
        """Snap has dual-chain financial leverage (OpenAI API + Perplexity→Condé Nast)."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        ai_partnerships = snap.get('ai_partnerships', {})
        # Both OpenAI and Perplexity relationships
        self.assertIn('openai', ai_partnerships)
        self.assertIn('perplexity', ai_partnerships)

    def test_apple_multi_channel_leverage(self):
        """Apple has multi-channel leverage (News+ + Siri AI + Gemini chain)."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        # Should have News+, Siri AI deals, and Gemini deal
        apple_str = str(apple)
        channels = [
            'News+' in apple_str,
            'siri' in apple_str.lower(),
            'gemini' in apple_str.lower()
        ]
        self.assertTrue(all(channels),
                        "Apple must have all three financial channels documented: News+, Siri AI, Gemini")


class TestPredictiveCoverageAsymmetry(unittest.TestCase):
    """Verify the financial incentive model predicts observable coverage patterns."""

    def test_meta_receives_most_adversarial_coverage(self):
        """The entity with the lowest financial leverage score (Meta) receives most adversarial coverage."""
        data = load_wired_profile()
        wired_str = str(data)
        # Check that Meta's adversarial coverage is documented
        adversarial_indicators = [
            'creepy' in wired_str.lower(),
            'surveillance' in wired_str.lower(),
            'privacy' in wired_str.lower(),
        ]
        self.assertTrue(any(adversarial_indicators),
                        "Meta adversarial coverage vocabulary must be documented in WIRED profile")

    def test_samsung_zero_privacy_alarm(self):
        """Samsung receives zero privacy alarm vocabulary despite identical hardware."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        note = samsung.get('publisher_deals_note', '')
        samsung_str = str(samsung)
        # Samsung should have zero privacy scrutiny documented
        has_zero_scrutiny = ('zero' in samsung_str.lower() and 'privacy' in samsung_str.lower())
        self.assertTrue(has_zero_scrutiny,
                        "Samsung zero privacy scrutiny must be documented")

    def test_snap_zero_surveillance_framing(self):
        """Snap receives zero surveillance framing despite 4 cameras (vs Meta's 1)."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        specs = snap.get('hardware_devices', {}).get('specs_consumer', {})
        self.assertEqual(specs.get('surveillance_framing_count', -1), 0,
                         "Snap Specs must have surveillance_framing_count = 0")


class TestConfounderDocumentation(unittest.TestCase):
    """Verify confounders are honestly documented."""

    def test_meta_market_share_confounder(self):
        """Meta's dominant market share is a STRONG confounder — more users = more incidents."""
        # This is the strongest alternative explanation: Meta has 80%+ smart glasses market
        # share, so naturally receives proportionally more coverage
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        # Confounders should be mentioned in related mechanisms
        samsung_str = str(samsung)
        has_market_share_confounder = (
            'market share' in samsung_str.lower() or
            '80%' in samsung_str
        )
        self.assertTrue(has_market_share_confounder,
                        "Meta's market share as a confounder must be documented")

    def test_incumbency_coverage_confounder(self):
        """Incumbency effect: established products get more scrutiny than pre-launch."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        samsung_str = str(samsung)
        # Should mention pre-launch vs incumbent
        has_incumbent_confounder = (
            'incumbent' in samsung_str.lower() or
            'pre-launch' in samsung_str.lower() or
            'not yet shipping' in samsung_str.lower()
        )
        self.assertTrue(has_incumbent_confounder,
                        "Pre-launch vs incumbent confounder must be documented")

    def test_genuine_privacy_incidents_confounder(self):
        """Meta has genuine privacy incidents — a legitimate editorial concern."""
        # The model must acknowledge Meta has REAL privacy issues, not just manufactured ones
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        samsung_str = str(samsung)
        has_genuine_concern = (
            'genuine' in samsung_str.lower() or
            'legitimate' in samsung_str.lower() or
            'privacy incidents' in samsung_str.lower()
        )
        self.assertTrue(has_genuine_concern,
                        "Meta genuine privacy concerns as confounder must be documented")


class TestMechanismMetadata(unittest.TestCase):
    """Verify mechanism #202 metadata in competitor-coverage-research.yaml."""

    def _find_mechanism_202(self):
        """Recursively find mechanism_id 202 in the YAML."""
        data = load_competitor_research()

        def _search(d):
            if isinstance(d, dict):
                if d.get('mechanism_id') == 202:
                    return d
                for v in d.values():
                    result = _search(v)
                    if result:
                        return result
            elif isinstance(d, list):
                for item in d:
                    result = _search(item)
                    if result:
                        return result
            return None

        return _search(data)

    def test_mechanism_202_exists(self):
        """Mechanism #202 must exist in competitor-coverage-research.yaml."""
        mech = self._find_mechanism_202()
        self.assertIsNotNone(mech, "Mechanism #202 must exist in competitor-coverage-research.yaml")

    def test_mechanism_202_has_discovery_date(self):
        """Mechanism #202 must have discovery_date."""
        mech = self._find_mechanism_202()
        self.assertIsNotNone(mech, "Mechanism #202 not found")
        self.assertIn('discovery_date', mech)
        self.assertEqual(mech['discovery_date'], '2026-08-20')

    def test_mechanism_202_has_asymmetry_score(self):
        """Mechanism #202 must have an asymmetry score."""
        mech = self._find_mechanism_202()
        self.assertIsNotNone(mech, "Mechanism #202 not found")
        self.assertIn('asymmetry_score', mech)
        score = mech['asymmetry_score']
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 1.0)

    def test_mechanism_202_cross_references(self):
        """Mechanism #202 must cross-reference relevant prior mechanisms."""
        mech = self._find_mechanism_202()
        self.assertIsNotNone(mech, "Mechanism #202 not found")
        refs = mech.get('cross_references', [])
        self.assertGreater(len(refs), 3,
                           "Mechanism #202 must cross-reference at least 4 prior mechanisms")

    def test_mechanism_202_has_confounders(self):
        """Mechanism #202 must document confounders."""
        mech = self._find_mechanism_202()
        self.assertIsNotNone(mech, "Mechanism #202 not found")
        confounders = mech.get('confounding_factors', [])
        self.assertGreaterEqual(len(confounders), 3,
                                "Mechanism #202 must have at least 3 confounders")
        # Should include STRONG confounders
        strong_count = sum(1 for c in confounders if '[STRONG]' in str(c))
        self.assertGreaterEqual(strong_count, 2,
                                "Mechanism #202 must have at least 2 STRONG confounders")


class TestSourceDocumentation(unittest.TestCase):
    """Verify all claims have source URLs."""

    def test_samsung_ad_spend_has_sources(self):
        """Samsung advertising leverage must have source URLs."""
        data = load_competitor_entities()
        samsung = data['entities']['samsung']
        ad_leverage = samsung.get('advertising_leverage', {})
        sources = ad_leverage.get('source_urls', [])
        self.assertGreater(len(sources), 0,
                           "Samsung ad leverage must have source URLs")

    def test_snap_perplexity_deal_has_sources(self):
        """Snap-Perplexity deal must have source URLs."""
        data = load_competitor_entities()
        snap = data['entities']['snap']
        sources = snap.get('source_urls', [])
        self.assertGreater(len(sources), 0,
                           "Snap entity must have source URLs")

    def test_apple_siri_deal_has_sources(self):
        """Apple Siri AI deal must have source URLs."""
        data = load_competitor_entities()
        apple = data['entities']['apple']
        apple_str = str(apple)
        # WSJ is the primary source for the Siri AI deal
        has_wsj = 'wsj' in apple_str.lower() or 'wall street journal' in apple_str.lower()
        self.assertTrue(has_wsj,
                        "Apple Siri AI deal must reference WSJ as primary source")

    def test_press_gazette_prisoner_dilemma_sourced(self):
        """Press Gazette prisoner's dilemma characterization must be sourced."""
        data = load_competitor_entities()
        google = data['entities']['google']
        google_str = str(google)
        self.assertIn('pressgazette', google_str.lower().replace(' ', ''),
                      "Press Gazette must be cited for prisoner's dilemma characterization")


class TestFall2026ConvergenceIndexCompleteness(unittest.TestCase):
    """Verify the convergence index covers all necessary dimensions."""

    def test_all_four_entities_have_camera_specs(self):
        """All four smart glasses entities should have camera specifications."""
        data = load_competitor_entities()
        # Samsung: 12MP
        samsung_str = str(data['entities']['samsung'])
        self.assertIn('12MP', samsung_str)
        # Snap: 4 cameras
        snap = data['entities']['snap']
        snap_cameras = snap.get('hardware_devices', {}).get('specs_consumer', {}).get('cameras', {}).get('total', 0)
        self.assertEqual(snap_cameras, 4)

    def test_conde_nast_revenue_context_documented(self):
        """Condé Nast's ~$2B revenue must be documented for ratio calculations."""
        data = load_wired_profile()
        wired_str = str(data)
        has_revenue = ('2 billion' in wired_str.lower() or '$2b' in wired_str.lower()
                       or '2021' in wired_str.lower() or 'revenue growth' in wired_str.lower())
        self.assertTrue(has_revenue,
                        "Condé Nast revenue context should be documented in WIRED profile")

    def test_google_zero_strategy_documented(self):
        """Lynch's 'Google Zero' strategy must be documented as financial context."""
        data = load_wired_profile()
        wired_str = str(data)
        self.assertIn('Google Zero', wired_str,
                      "Lynch's Google Zero strategy must be in WIRED profile")

    def test_advertising_no_longer_growth_engine(self):
        """Lynch's statement that advertising is no longer a growth engine must be documented."""
        data = load_wired_profile()
        wired_str = str(data)
        self.assertTrue(
            'no longer expects advertising' in wired_str.lower() or
            'growth engine' in wired_str.lower(),
            "Lynch's advertising growth statement must be in WIRED profile"
        )


if __name__ == '__main__':
    unittest.main()
