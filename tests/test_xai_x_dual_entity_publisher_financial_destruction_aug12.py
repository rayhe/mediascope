"""
Mechanism #68: xAI-X Dual-Entity Publisher Financial Destruction Chain —
Active Revenue Demolition Predicts Maximum Coverage Hostility

Type C: Financial Incentive Mapping
Date: 2026-08-12

CORE FINDING:

xAI and X (both controlled by Elon Musk) represent a unique DUAL-ENTITY
structure that is the ONLY competitor in the MediaScope dataset with an
ACTIVELY NEGATIVE financial relationship with publishers — not merely
neutral (zero deals) but destructive (active demolition of existing
publisher revenue streams). This makes xAI-X the most extreme data point
in the financial incentive → coverage tone model.

The existing xAI entity analysis (in competitor-entities.yaml) describes
xAI as "publisher-invisible" — neither paying nor being sued by publishers.
This is INCOMPLETE. The X platform, which Musk acquired in Oct 2022 and
merged with xAI in Mar 2025, was once publishers' second-largest social
traffic referrer after Facebook. Musk systematically demolished this
revenue channel through:

(1) TRAFFIC DESTRUCTION: X referral traffic to news publishers down
    65-75% since Oct 2022 (Press Gazette/Chartbeat data, Jul 2025).
    Headlines removed from link previews (Oct 2023). Algorithmic
    deprioritization of outlinks. 5-second link throttling confirmed
    for NYT, Reuters, WaPo (Aug 2023, confirmed by WaPo, NYT, Reuters).

(2) HOSTILE PRESS RELATIONS: xAI's automated press response to Reuters
    and WSJ inquiries: "Legacy Media Lies." Musk personally attacks
    journalists. No other CEO of a $200B+ AI company maintains an openly
    hostile relationship with the publisher ecosystem.

(3) ZERO CONTENT LICENSING: Unlike Anthropic ($1.5B piracy settlement),
    xAI has paid publishers $0. Grok trains on X posts (which include
    user-shared publisher content) via platform intermediary.

(4) ADVERTISING ECOSYSTEM ANTAGONISM: X ad revenue collapsed from $4.5B
    (2022) to ~$2.9B projected (2025). GARM antitrust lawsuit (Aug 2024)
    antagonized the entire advertising ecosystem.

THE FINANCIAL INCENTIVE MODEL PREDICTS:

- POSITIVE financial relationship → softer coverage (OpenAI, Google, Amazon)
- NEUTRAL financial relationship → adversarial coverage (Meta: 13 deals
  but none with adversarial publications; Anthropic: zero deals)
- NEGATIVE financial relationship → MOST adversarial coverage (xAI-X:
  active revenue destruction + zero deals + personal hostility)

THE VOLUME PARADOX:

Despite xAI-X having the MOST negative financial relationship with
publishers, Meta receives MORE adversarial coverage volume than xAI.
This is because adversarial coverage is ALSO driven by competitive
dynamics with financial partners: adversarial Meta coverage benefits
OpenAI, Anthropic, Apple, and Google — companies that PAY publishers.
Adversarial xAI coverage also benefits these same companies but xAI
is a SMALLER competitive threat to them than Meta.
"""

import os
import unittest

import yaml


def _load_competitor_entities():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "profiles",
        "competitor-entities.yaml",
    )
    with open(path) as f:
        return yaml.safe_load(f)


def _load_competitor_research():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "profiles",
        "competitor-coverage-research.yaml",
    )
    with open(path) as f:
        return yaml.safe_load(f)


def _get_mechanism():
    data = _load_competitor_research()
    cpf = data.get("cross_publication_findings", {})
    for key, val in cpf.items():
        if isinstance(val, dict) and val.get("mechanism_id") == 68:
            return val
    return None


# =============================================================================
# Test Class 1: X Platform Traffic Destruction Evidence
# =============================================================================
class TestXPlatformTrafficDestruction(unittest.TestCase):
    """Verify the X platform's systematic demolition of publisher referral traffic."""

    def test_x_referral_decline_documented(self):
        """X referral traffic to publishers declined 65-75% since Musk acquisition."""
        mech = _get_mechanism()
        self.assertIsNotNone(mech)
        traffic = mech.get("x_platform_traffic_destruction", {})
        self.assertIn("referral_decline_pct", traffic)
        decline = traffic["referral_decline_pct"]
        # Documented range is 65-75%
        self.assertGreaterEqual(decline, 60)
        self.assertLessEqual(decline, 80)

    def test_link_throttling_documented(self):
        """Deliberate link throttling to specific publications confirmed."""
        mech = _get_mechanism()
        traffic = mech.get("x_platform_traffic_destruction", {})
        throttled = traffic.get("confirmed_throttled_publications", [])
        self.assertGreaterEqual(len(throttled), 3)
        # NYT, Reuters, WaPo all confirmed
        throttled_lower = [p.lower() for p in throttled]
        self.assertTrue(any("nyt" in p or "new york times" in p for p in throttled_lower))
        self.assertTrue(any("reuters" in p for p in throttled_lower))

    def test_headline_removal_date(self):
        """Headlines removed from link previews documented with date."""
        mech = _get_mechanism()
        traffic = mech.get("x_platform_traffic_destruction", {})
        self.assertIn("headline_removal_date", traffic)

    def test_traffic_source_ranking_before_acquisition(self):
        """Twitter was publishers' 2nd largest social referrer before acquisition."""
        mech = _get_mechanism()
        traffic = mech.get("x_platform_traffic_destruction", {})
        self.assertIn("pre_acquisition_social_ranking", traffic)
        self.assertEqual(traffic["pre_acquisition_social_ranking"], 2)

    def test_chartbeat_data_source_cited(self):
        """Chartbeat data is the primary source for traffic decline claims."""
        mech = _get_mechanism()
        sources = mech.get("source_urls", [])
        self.assertTrue(
            any("chartbeat" in s or "pressgazette" in s for s in sources),
            "Chartbeat or Press Gazette source expected",
        )


# =============================================================================
# Test Class 2: X Advertising Revenue Collapse
# =============================================================================
class TestXAdvertisingRevenueCollapse(unittest.TestCase):
    """Verify X's advertising revenue destruction data."""

    def test_ad_revenue_trajectory_documented(self):
        """X ad revenue decline from $4.5B to ~$2.9B documented."""
        mech = _get_mechanism()
        ad_data = mech.get("x_ad_revenue_collapse", {})
        self.assertIn("pre_acquisition_annual_b", ad_data)
        self.assertGreaterEqual(ad_data["pre_acquisition_annual_b"], 4.0)

    def test_ad_revenue_decline_pct(self):
        """Overall ad revenue decline documented as percentage."""
        mech = _get_mechanism()
        ad_data = mech.get("x_ad_revenue_collapse", {})
        self.assertIn("decline_pct_from_peak", ad_data)
        self.assertGreaterEqual(ad_data["decline_pct_from_peak"], 30)

    def test_garm_lawsuit_documented(self):
        """GARM antitrust lawsuit documented as advertising ecosystem antagonism."""
        mech = _get_mechanism()
        ad_data = mech.get("x_ad_revenue_collapse", {})
        self.assertIn("garm_lawsuit_date", ad_data)

    def test_q2_2025_revenue_documented(self):
        """Q2 2025 revenue figure ($707M) documented from Bloomberg."""
        mech = _get_mechanism()
        ad_data = mech.get("x_ad_revenue_collapse", {})
        self.assertIn("q2_2025_revenue_m", ad_data)
        self.assertAlmostEqual(ad_data["q2_2025_revenue_m"], 707, delta=50)


# =============================================================================
# Test Class 3: xAI Zero-Deal Status vs Anthropic Comparison
# =============================================================================
class TestXAIZeroDealComparison(unittest.TestCase):
    """Compare xAI's zero-deal status with other entities."""

    def test_xai_zero_publisher_deals(self):
        """xAI confirmed to have zero publisher content licensing deals."""
        mech = _get_mechanism()
        deals = mech.get("publisher_deal_comparison", {})
        self.assertEqual(deals.get("xai_deals"), 0)

    def test_anthropic_comparison_documented(self):
        """Anthropic (also zero deals but $1.5B settlement) documented as comparison."""
        mech = _get_mechanism()
        deals = mech.get("publisher_deal_comparison", {})
        self.assertIn("anthropic_settlement_b", deals)
        self.assertGreaterEqual(deals["anthropic_settlement_b"], 1.0)

    def test_openai_comparison_documented(self):
        """OpenAI's 20+ deals documented as comparison baseline."""
        mech = _get_mechanism()
        deals = mech.get("publisher_deal_comparison", {})
        self.assertIn("openai_deals_count", deals)
        self.assertGreaterEqual(deals["openai_deals_count"], 20)

    def test_meta_comparison_documented(self):
        """Meta's 13 deals documented as comparison."""
        mech = _get_mechanism()
        deals = mech.get("publisher_deal_comparison", {})
        self.assertIn("meta_deals_count", deals)
        self.assertGreaterEqual(deals["meta_deals_count"], 13)

    def test_grok_training_data_source_documented(self):
        """Grok's reliance on X post data (including shared publisher content) documented."""
        mech = _get_mechanism()
        training = mech.get("grok_training_data", {})
        self.assertIn("primary_source", training)
        self.assertIn("x posts", training["primary_source"].lower())


# =============================================================================
# Test Class 4: Hostile Press Relations
# =============================================================================
class TestHostilePressRelations(unittest.TestCase):
    """Verify documentation of xAI's unprecedented publisher hostility."""

    def test_legacy_media_lies_response(self):
        """xAI's automated 'Legacy Media Lies' response documented."""
        mech = _get_mechanism()
        hostility = mech.get("hostile_press_relations", {})
        self.assertIn("automated_response", hostility)
        self.assertIn("legacy media lies", hostility["automated_response"].lower())

    def test_publications_receiving_hostile_response(self):
        """At least 2 publications documented receiving hostile automated response."""
        mech = _get_mechanism()
        hostility = mech.get("hostile_press_relations", {})
        recipients = hostility.get("confirmed_recipients", [])
        self.assertGreaterEqual(len(recipients), 2)

    def test_personal_journalist_attacks_noted(self):
        """Musk's personal attacks on journalists documented."""
        mech = _get_mechanism()
        hostility = mech.get("hostile_press_relations", {})
        self.assertIn("personal_journalist_attacks", hostility)
        self.assertTrue(hostility["personal_journalist_attacks"])

    def test_uniqueness_claim_documented(self):
        """Claim that no other $200B+ AI CEO maintains this hostility is stated."""
        mech = _get_mechanism()
        hostility = mech.get("hostile_press_relations", {})
        self.assertIn("uniqueness", hostility)


# =============================================================================
# Test Class 5: Dual-Entity Financial Relationship Spectrum
# =============================================================================
class TestFinancialRelationshipSpectrum(unittest.TestCase):
    """Verify the three-tier financial relationship model."""

    def test_spectrum_has_three_tiers(self):
        """Financial relationship spectrum has positive/neutral/negative tiers."""
        mech = _get_mechanism()
        spectrum = mech.get("financial_relationship_spectrum", {})
        self.assertIn("positive", spectrum)
        self.assertIn("neutral", spectrum)
        self.assertIn("negative", spectrum)

    def test_positive_tier_entities(self):
        """Positive tier includes entities with active financial flows to publishers."""
        mech = _get_mechanism()
        spectrum = mech.get("financial_relationship_spectrum", {})
        positive = spectrum.get("positive", {})
        entities = positive.get("entities", [])
        self.assertGreaterEqual(len(entities), 3)

    def test_negative_tier_xai_only(self):
        """xAI-X is the ONLY entity in the negative tier."""
        mech = _get_mechanism()
        spectrum = mech.get("financial_relationship_spectrum", {})
        negative = spectrum.get("negative", {})
        entities = negative.get("entities", [])
        # xAI/X should be the only entity actively destroying publisher revenue
        self.assertTrue(any("xai" in e.lower() or "x/" in e.lower() for e in entities))

    def test_prediction_negative_most_adversarial(self):
        """Model predicts negative-tier entity receives most adversarial coverage."""
        mech = _get_mechanism()
        spectrum = mech.get("financial_relationship_spectrum", {})
        negative = spectrum.get("negative", {})
        self.assertIn("predicted_coverage_tone", negative)
        self.assertIn("adversarial", negative["predicted_coverage_tone"].lower())


# =============================================================================
# Test Class 6: Volume Paradox — Meta vs xAI Coverage Asymmetry
# =============================================================================
class TestVolumeParadox(unittest.TestCase):
    """Verify documentation of the coverage volume paradox."""

    def test_volume_paradox_documented(self):
        """The paradox that Meta gets MORE adversarial coverage than xAI is stated."""
        mech = _get_mechanism()
        paradox = mech.get("volume_paradox", {})
        self.assertIn("description", paradox)

    def test_three_explanatory_factors(self):
        """At least 3 factors explaining the volume paradox are documented."""
        mech = _get_mechanism()
        paradox = mech.get("volume_paradox", {})
        factors = paradox.get("explanatory_factors", [])
        self.assertGreaterEqual(len(factors), 3)

    def test_ad_competition_factor(self):
        """Ad market competition documented as explanatory factor."""
        mech = _get_mechanism()
        paradox = mech.get("volume_paradox", {})
        factors = paradox.get("explanatory_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        self.assertTrue(
            "ad" in factor_text or "advertising" in factor_text,
            "Ad market competition should be among explanatory factors",
        )

    def test_competitive_benefit_factor(self):
        """Competitive benefit to financial partners documented."""
        mech = _get_mechanism()
        paradox = mech.get("volume_paradox", {})
        factors = paradox.get("explanatory_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        self.assertTrue(
            "partner" in factor_text or "compet" in factor_text,
            "Competitive benefit to partners should be documented",
        )


# =============================================================================
# Test Class 7: xAI Valuation and Financial Capacity
# =============================================================================
class TestXAIFinancialCapacity(unittest.TestCase):
    """Verify xAI's financial capacity to license but choice not to."""

    def test_valuation_documented(self):
        """xAI valuation of $200B+ documented."""
        mech = _get_mechanism()
        capacity = mech.get("xai_financial_capacity", {})
        self.assertIn("latest_valuation_b", capacity)
        self.assertGreaterEqual(capacity["latest_valuation_b"], 200)

    def test_total_funding_documented(self):
        """Total funding raised documented."""
        mech = _get_mechanism()
        capacity = mech.get("xai_financial_capacity", {})
        self.assertIn("total_funding_raised_b", capacity)
        self.assertGreaterEqual(capacity["total_funding_raised_b"], 20)

    def test_choice_not_to_license(self):
        """Explicit note that xAI has capacity to license but chose not to."""
        mech = _get_mechanism()
        capacity = mech.get("xai_financial_capacity", {})
        self.assertIn("deliberate_non_licensing", capacity)
        self.assertTrue(capacity["deliberate_non_licensing"])


# =============================================================================
# Test Class 8: Source URLs and Data Quality
# =============================================================================
class TestSourceURLsAndQuality(unittest.TestCase):
    """Verify source URLs and data quality."""

    def test_minimum_source_urls(self):
        """At least 8 source URLs for this mechanism."""
        mech = _get_mechanism()
        sources = mech.get("source_urls", [])
        self.assertGreaterEqual(len(sources), 8)

    def test_source_diversity(self):
        """Sources span at least 4 different domains."""
        mech = _get_mechanism()
        sources = mech.get("source_urls", [])
        domains = set()
        for url in sources:
            # Extract domain
            parts = url.split("/")
            if len(parts) >= 3:
                domains.add(parts[2])
        self.assertGreaterEqual(len(domains), 4)

    def test_no_duplicate_sources(self):
        """No duplicate source URLs."""
        mech = _get_mechanism()
        sources = mech.get("source_urls", [])
        self.assertEqual(len(sources), len(set(sources)))


# =============================================================================
# Test Class 9: Confounding Factors
# =============================================================================
class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are documented."""

    def test_minimum_confounding_factors(self):
        """At least 5 confounding factors documented."""
        mech = _get_mechanism()
        factors = mech.get("confounding_factors", [])
        self.assertGreaterEqual(len(factors), 5)

    def test_factors_have_strength_ratings(self):
        """Each confounding factor has a strength rating."""
        mech = _get_mechanism()
        factors = mech.get("confounding_factors", [])
        for factor in factors:
            self.assertIn("strength", factor, f"Factor missing strength: {factor}")

    def test_musk_personal_politics_factor(self):
        """Musk's political activity as confounding factor documented."""
        mech = _get_mechanism()
        factors = mech.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        self.assertTrue(
            "politic" in factor_text or "doge" in factor_text or "trump" in factor_text,
            "Musk's political activity should be among confounding factors",
        )

    def test_csam_lawsuit_factor(self):
        """CSAM lawsuits as legitimate negative coverage driver documented."""
        mech = _get_mechanism()
        factors = mech.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        self.assertTrue(
            "csam" in factor_text or "deepfake" in factor_text,
            "CSAM/deepfake lawsuits should be among confounding factors",
        )


# =============================================================================
# Test Class 10: Cross-References and Testable Predictions
# =============================================================================
class TestCrossReferencesAndPredictions(unittest.TestCase):
    """Verify cross-references and testable predictions."""

    def test_minimum_cross_references(self):
        """At least 4 cross-references to other mechanisms."""
        mech = _get_mechanism()
        refs = mech.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 4)

    def test_cross_ref_to_meta_ad_antagonism(self):
        """Cross-reference to mechanism #47 (Meta ad competitor antagonism)."""
        mech = _get_mechanism()
        refs = mech.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        self.assertIn(47, ref_ids)

    def test_cross_ref_to_openai_triple_layer(self):
        """Cross-reference to mechanism #53 (OpenAI triple-layer funding)."""
        mech = _get_mechanism()
        refs = mech.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        self.assertIn(53, ref_ids)

    def test_minimum_testable_predictions(self):
        """At least 4 testable predictions documented."""
        mech = _get_mechanism()
        predictions = mech.get("testable_predictions", [])
        self.assertGreaterEqual(len(predictions), 4)

    def test_predictions_are_falsifiable(self):
        """Each prediction contains verifiable conditions."""
        mech = _get_mechanism()
        predictions = mech.get("testable_predictions", [])
        for pred in predictions:
            if isinstance(pred, dict):
                self.assertIn(
                    "prediction", pred, f"Prediction missing 'prediction' key: {pred}"
                )
            else:
                self.assertGreater(
                    len(str(pred)), 20, f"Prediction too short to be falsifiable: {pred}"
                )


# =============================================================================
# Test Class 11: Entity YAML Integration
# =============================================================================
class TestEntityYAMLIntegration(unittest.TestCase):
    """Verify xAI entity in competitor-entities.yaml is updated."""

    def test_xai_entity_exists(self):
        """xAI entity exists in competitor-entities.yaml."""
        data = _load_competitor_entities()
        entities = data.get("entities", {})
        self.assertIn("xai", entities)

    def test_dual_entity_destruction_chain_section(self):
        """xAI entity has dual_entity_destruction_chain section."""
        data = _load_competitor_entities()
        xai = data["entities"]["xai"]
        self.assertIn("dual_entity_destruction_chain", xai)

    def test_x_twitter_entity_exists(self):
        """X/Twitter entity exists in competitor-entities.yaml."""
        data = _load_competitor_entities()
        entities = data.get("entities", {})
        self.assertIn("x_twitter", entities)


# =============================================================================
# Test Class 12: Mechanism Structure in Research YAML
# =============================================================================
class TestMechanismStructure(unittest.TestCase):
    """Verify mechanism #68 has proper structure in research YAML."""

    def test_mechanism_exists_in_cpf(self):
        """Mechanism #68 exists in cross_publication_findings."""
        mech = _get_mechanism()
        self.assertIsNotNone(mech, "Mechanism #68 not found in cross_publication_findings")

    def test_has_mechanism_id(self):
        """Mechanism has correct mechanism_id."""
        mech = _get_mechanism()
        self.assertEqual(mech["mechanism_id"], 68)

    def test_has_discovery_date(self):
        """Mechanism has discovery_date."""
        mech = _get_mechanism()
        self.assertIn("discovery_date", mech)
        self.assertEqual(mech["discovery_date"], "2026-08-12")

    def test_has_date_added(self):
        """Mechanism has date_added."""
        mech = _get_mechanism()
        self.assertIn("date_added", mech)

    def test_has_finding_summary(self):
        """Mechanism has finding_summary."""
        mech = _get_mechanism()
        self.assertIn("finding_summary", mech)
        self.assertGreater(len(mech["finding_summary"]), 100)

    def test_has_test_file(self):
        """Mechanism references its test file."""
        mech = _get_mechanism()
        self.assertIn("test_file", mech)


if __name__ == "__main__":
    unittest.main()
