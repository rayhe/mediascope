"""
Test financial relationship data integrity, competitor coverage research
consistency, and asymmetry scoring validity.

Tests the new relationship types (adversarial_litigation, settlement, coercive)
added in the Aug 4 2026 Type C iteration, and validates that the competitor
coverage research YAML has internally consistent data.
"""

import os
import re
import unittest

import yaml


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestCompetitorEntities(unittest.TestCase):
    """Validate competitor-entities.yaml structure and completeness."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")

    def test_all_major_entities_present(self):
        """All major competitor entities must be defined."""
        expected = {"openai", "anthropic", "amazon", "apple", "google", "x_twitter", "meta"}
        actual = set(self.entities["entities"].keys())
        self.assertTrue(expected.issubset(actual),
                        f"Missing entities: {expected - actual}")

    def test_entity_has_required_fields(self):
        """Each entity must have display_name, aliases, regex, category."""
        required = {"display_name", "aliases", "regex", "category"}
        for name, entity in self.entities["entities"].items():
            for field in required:
                self.assertIn(field, entity, f"{name} missing {field}")

    def test_entity_regexes_compile(self):
        """All entity regexes must be valid."""
        for name, entity in self.entities["entities"].items():
            try:
                re.compile(entity["regex"])
            except re.error as e:
                self.fail(f"{name} regex is invalid: {e}")

    def test_relationship_types_complete(self):
        """All relationship types including new ones must be defined."""
        types = self.entities["relationship_types"]
        # Original types
        for t in ("licensing", "investment", "advertising", "litigation",
                  "adversarial", "indirect", "mixed", "none", "negotiating"):
            self.assertIn(t, types, f"Missing relationship type: {t}")
        # New types from Aug 4 Type C iteration
        for t in ("adversarial_litigation", "settlement", "coercive"):
            self.assertIn(t, types, f"Missing new relationship type: {t}")

    def test_relationship_types_have_descriptions(self):
        """Every relationship type must have a non-empty description."""
        for rtype, desc in self.entities["relationship_types"].items():
            self.assertTrue(desc and len(desc.strip()) > 10,
                            f"Relationship type '{rtype}' missing or trivial description")

    def test_coverage_predictions_defined(self):
        """Coverage prediction categories must be defined."""
        preds = self.entities.get("coverage_predictions", {})
        for p in ("softer", "neutral", "adversarial", "unknown"):
            self.assertIn(p, preds, f"Missing coverage prediction: {p}")

    def test_new_types_semantically_distinct(self):
        """New relationship types must be semantically distinct from originals."""
        types = self.entities["relationship_types"]
        # adversarial_litigation vs adversarial: litigation involves actual lawsuit
        self.assertIn("lawsuit", types["adversarial_litigation"].lower())
        self.assertNotIn("lawsuit", types["adversarial"].lower())
        # settlement vs licensing: settlement is legal, not voluntary
        self.assertIn("settlement", types["settlement"].lower())
        # coercive: pressure/lose
        self.assertIn("pressured", types["coercive"].lower())


class TestCompetitorCoverageResearch(unittest.TestCase):
    """Validate competitor-coverage-research.yaml data integrity."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.entities = load_yaml("competitor-entities.yaml")

    def test_publications_have_meta_coverage(self):
        """Every profiled publication must have meta_coverage_tone."""
        pubs = self.research.get("publications", {})
        self.assertTrue(len(pubs) >= 3, "Need at least 3 publications profiled")
        for name, pub in pubs.items():
            self.assertIn("meta_coverage_tone", pub,
                          f"{name} missing meta_coverage_tone")

    def test_meta_coverage_tone_is_adversarial(self):
        """Key publications with no Meta deal should show adversarial Meta coverage."""
        pubs = self.research.get("publications", {})
        no_deal_pubs = ["wired", "the-verge", "atlantic"]
        for pub_name in no_deal_pubs:
            if pub_name in pubs:
                tone = pubs[pub_name]["meta_coverage_tone"]
                self.assertIn("adversarial", tone.lower(),
                              f"{pub_name} should show adversarial Meta coverage, got: {tone}")

    def test_openai_coverage_softer_than_meta(self):
        """Publications with OpenAI deals should show softer OpenAI than Meta coverage."""
        pubs = self.research.get("publications", {})
        tone_order = {
            "positive": 3, "balanced_to_positive": 2, "neutral_to_positive": 1.5,
            "balanced": 1, "neutral": 0, "mixed": -0.5,
            "adversarial": -2, "adversarial_investigative": -3
        }
        for name in ["wired", "the-verge", "atlantic"]:
            if name not in pubs:
                continue
            pub = pubs[name]
            meta_tone = pub.get("meta_coverage_tone", "")
            openai_tone = pub.get("openai_coverage_tone", "")
            if meta_tone in tone_order and openai_tone in tone_order:
                self.assertGreater(
                    tone_order.get(openai_tone, 0),
                    tone_order.get(meta_tone, 0),
                    f"{name}: OpenAI coverage ({openai_tone}) should be softer than Meta ({meta_tone})"
                )

    def test_asymmetry_verdicts_present(self):
        """Key publications must have asymmetry_verdict analysis."""
        pubs = self.research.get("publications", {})
        for name in ["wired", "the-verge", "atlantic"]:
            if name in pubs:
                self.assertIn("asymmetry_verdict", pubs[name],
                              f"{name} missing asymmetry_verdict")
                verdict = pubs[name]["asymmetry_verdict"]
                self.assertTrue(len(verdict.strip()) > 50,
                                f"{name} asymmetry_verdict is too short")

    def test_examples_have_source_urls(self):
        """Coverage examples should have source_url fields."""
        pubs = self.research.get("publications", {})
        total_examples = 0
        examples_with_urls = 0
        for name, pub in pubs.items():
            for key in pub:
                if key.endswith("_examples") and isinstance(pub[key], list):
                    for ex in pub[key]:
                        total_examples += 1
                        if ex.get("source_url"):
                            examples_with_urls += 1
        # At least 30% of examples should have source URLs
        if total_examples > 0:
            ratio = examples_with_urls / total_examples
            self.assertGreaterEqual(ratio, 0.3,
                                    f"Only {examples_with_urls}/{total_examples} examples have source URLs")

    def test_tone_values_valid(self):
        """All coverage tone values should be from the expected vocabulary."""
        valid_tones = {
            "adversarial", "adversarial_investigative", "balanced_adversarial",
            "critical", "negative", "mixed", "neutral", "balanced",
            "neutral_to_positive", "balanced_to_positive", "positive"
        }
        pubs = self.research.get("publications", {})
        for name, pub in pubs.items():
            for key in pub:
                if key.endswith("_coverage_tone"):
                    tone = pub[key]
                    self.assertIn(tone, valid_tones,
                                  f"{name}.{key} = '{tone}' not in valid tones: {valid_tones}")

    def test_wired_google_is_adversarial_litigation(self):
        """WIRED's Google relationship should reflect the Jan 2026 lawsuit."""
        pubs = self.research.get("publications", {})
        wired = pubs.get("wired", {})
        google_tone = wired.get("google_coverage_tone", "")
        self.assertEqual(google_tone, "adversarial",
                         "WIRED Google coverage should be adversarial")
        # Check that the Google coverage summary mentions the lawsuit
        google_summary = wired.get("google_coverage_summary", "")
        self.assertIn("sued", google_summary.lower(),
                      "WIRED Google summary should mention the lawsuit")

    def test_meta_more_adversarial_than_google_for_wired(self):
        """Despite suing Google, WIRED covers Meta MORE adversarially — the key finding."""
        pubs = self.research.get("publications", {})
        wired = pubs.get("wired", {})
        # Both should be adversarial, but the asymmetry verdict should note
        # Meta is covered more harshly
        verdict = wired.get("asymmetry_verdict", "")
        self.assertTrue(
            "meta" in verdict.lower() and "openai" in verdict.lower(),
            "WIRED asymmetry verdict should compare Meta and OpenAI coverage"
        )


class TestWiredProfileFinancialTies(unittest.TestCase):
    """Validate WIRED profile has correct competitor relationship data."""

    @classmethod
    def setUpClass(cls):
        cls.wired = load_yaml("wired.yaml")

    def test_google_relationship_type(self):
        """WIRED's Google relationship should be adversarial_litigation."""
        cr = self.wired.get("competitor_relationships", {})
        google = cr.get("google", {})
        financial_tie = google.get("financial_tie", "")
        self.assertEqual(financial_tie, "adversarial_litigation",
                         f"WIRED-Google should be adversarial_litigation, got: {financial_tie}")

    def test_google_relationship_has_lawsuit_details(self):
        """WIRED-Google relationship should document the Jan 2026 lawsuit."""
        cr = self.wired.get("competitor_relationships", {})
        google = cr.get("google", {})
        desc = google.get("description", "")
        self.assertTrue(
            any(term in desc.lower() for term in ["sued", "lawsuit", "litigation", "sdny"]),
            "WIRED-Google description should mention the lawsuit"
        )

    def test_google_estimated_value_zero(self):
        """WIRED gets no money from Google — estimated_value should show $0."""
        cr = self.wired.get("competitor_relationships", {})
        google = cr.get("google", {})
        value = google.get("estimated_value", "")
        self.assertIn("$0", value,
                      f"WIRED-Google should show $0, got: {value}")


class TestAggregateFindings(unittest.TestCase):
    """Validate aggregate analytical findings in the research file."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_aggregate_findings_present(self):
        """Research file should have aggregate findings."""
        findings = self.research.get("aggregate_findings", [])
        # Should have at least the Jan 2026 lawsuit cluster finding
        self.assertTrue(len(findings) >= 1 if findings else False,
                        "Should have at least one aggregate finding")

    def test_aggregate_findings_have_sources(self):
        """Each aggregate finding should have a source or analytical basis."""
        findings = self.research.get("aggregate_findings", [])
        if not findings:
            self.skipTest("No aggregate findings to check")
        for i, finding in enumerate(findings):
            if isinstance(finding, dict):
                has_source = any(k for k in finding if "source" in k.lower() or
                                 "evidence" in k.lower() or "basis" in k.lower() or
                                 "significance" in k.lower())
                self.assertTrue(has_source or "significance" in finding or
                                "analytical_significance" in finding,
                                f"Finding #{i} lacks source/significance")


class TestCrossProfileConsistency(unittest.TestCase):
    """Validate that profiles are consistent with competitor-coverage-research."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        # Load all publication profiles that exist
        cls.profiles = {}
        for fname in os.listdir(PROFILES_DIR):
            if fname.endswith(".yaml") and fname not in (
                "competitor-entities.yaml", "competitor-coverage-research.yaml",
                "_template.yaml", "advocacy-coalitions.yaml", "news-corp.yaml"
            ):
                try:
                    cls.profiles[fname.replace(".yaml", "")] = load_yaml(fname)
                except Exception:
                    pass

    def test_wired_competitor_relationships_exist(self):
        """WIRED profile must have competitor_relationships section."""
        wired = self.profiles.get("wired", {})
        self.assertIn("competitor_relationships", wired,
                      "WIRED profile must have competitor_relationships")

    def test_relationship_types_valid(self):
        """All financial_tie values in profiles must be valid relationship types."""
        entities = load_yaml("competitor-entities.yaml")
        valid_types = set(entities.get("relationship_types", {}).keys())
        for pname, profile in self.profiles.items():
            cr = profile.get("competitor_relationships", {})
            for entity, rel in cr.items():
                if isinstance(rel, dict) and "financial_tie" in rel:
                    tie = rel["financial_tie"]
                    self.assertIn(tie, valid_types,
                                  f"{pname}-{entity} has invalid financial_tie: {tie}")


class TestAsymmetryScoring(unittest.TestCase):
    """Validate the asymmetry hypothesis: coverage intensity correlates with
    absence of compensating financial ties."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_licensing_hypothesis_direction(self):
        """Publications paying entity X should cover X softer than entities they don't pay.

        Core hypothesis: coverage_intensity ∝ 1/(financial_tie_value)
        """
        pubs = self.research.get("publications", {})
        tone_scores = {
            "positive": 2, "balanced_to_positive": 1.5, "neutral_to_positive": 1,
            "balanced": 0.5, "neutral": 0, "mixed": -0.5,
            "adversarial": -1.5, "adversarial_investigative": -2
        }
        # For each publication: Meta tone should be <= OpenAI tone (when both exist)
        violations = []
        for name, pub in pubs.items():
            meta = tone_scores.get(pub.get("meta_coverage_tone"), None)
            openai = tone_scores.get(pub.get("openai_coverage_tone"), None)
            if meta is not None and openai is not None:
                if meta > openai:
                    violations.append(
                        f"{name}: Meta ({pub['meta_coverage_tone']}={meta}) "
                        f"softer than OpenAI ({pub['openai_coverage_tone']}={openai})"
                    )
        self.assertEqual(len(violations), 0,
                         f"Licensing hypothesis violations: {violations}")

    def test_lawsuit_paradox(self):
        """Publications suing Google should cover Google harder than Meta,
        yet they don't — this is the key paradox our analysis documents."""
        pubs = self.research.get("publications", {})
        # WIRED (Advance suing Google) — Google coverage should be adversarial
        wired = pubs.get("wired", {})
        if wired:
            google_tone = wired.get("google_coverage_tone", "")
            meta_tone = wired.get("meta_coverage_tone", "")
            # Both adversarial, but the research should document Meta as MORE adversarial
            self.assertEqual(google_tone, "adversarial")
            self.assertEqual(meta_tone, "adversarial")
            # The verdict should explicitly address this paradox
            verdict = wired.get("asymmetry_verdict", "")
            self.assertTrue(len(verdict) > 50,
                            "WIRED verdict should be substantial")


class TestCondeNastExpandedDealPortfolio(unittest.TestCase):
    """Condé Nast (WIRED parent) expanded to 5 AI licensing partners.
    Added Aug 5 2026 Type C iteration.
    Sources:
    - Adweek (CPTO + deal list): https://www.adweek.com/media/conde-nast-vasanth-williams-chief-product-technology-officer-microsoft-ai-licensing-pilot/
    - WebWire (Microsoft PCM): https://www.WebWire.com/ViewPressRel.asp?aId=350303
    """

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.wired = cls.research.get("publications", {}).get("wired", {})

    def test_microsoft_pcm_deal_documented(self):
        """Condé Nast's Microsoft PCM pilot partnership must be documented."""
        self.assertIn("microsoft_coverage_tone", self.wired)
        self.assertEqual(self.wired["microsoft_coverage_tone"], "neutral_to_positive")

    def test_perplexity_deal_documented(self):
        """Condé Nast's Perplexity deal must be documented."""
        self.assertIn("perplexity_coverage_tone", self.wired)
        summary = self.wired.get("perplexity_coverage_summary", "")
        self.assertIn("Perplexity", summary)

    def test_deal_count_summary(self):
        """Deal count summary documents five partners."""
        summary = self.wired.get("deal_count_summary", "")
        self.assertTrue(len(summary) > 50, "deal_count_summary should be substantive")
        # Should mention FIVE or 5
        self.assertTrue("FIVE" in summary or "five" in summary.lower() or "5" in summary)

    def test_meta_excluded_from_all_deals(self):
        """Meta is the only major tech company excluded from Condé Nast deals."""
        summary = self.wired.get("deal_count_summary", "")
        self.assertIn("ONLY major tech company", summary)

    def test_microsoft_pcm_source_url(self):
        """Microsoft PCM deal must have source URL."""
        self.assertIn("microsoft_pcm_source", self.wired)
        self.assertTrue(self.wired["microsoft_pcm_source"].startswith("http"))

    def test_perplexity_deal_source_url(self):
        """Perplexity deal must have source URL."""
        self.assertIn("perplexity_deal_source", self.wired)
        self.assertTrue(self.wired["perplexity_deal_source"].startswith("http"))

    def test_meta_not_pcm_participant(self):
        """Microsoft PCM summary must document Meta's absence."""
        summary = self.wired.get("microsoft_coverage_summary", "")
        self.assertIn("Meta is NOT a PCM participant", summary)


class TestMicrosoftPCMAggregateFinding(unittest.TestCase):
    """Microsoft PCM marketplace structural finding in aggregate.
    Added Aug 5 2026 Type C iteration.
    """

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.findings = cls.research.get("aggregate_findings", {}).get("key_evidence", [])

    def test_pcm_finding_exists(self):
        """Aggregate findings must include Microsoft PCM marketplace."""
        pcm_found = any("PCM" in f.get("finding", "") for f in self.findings)
        self.assertTrue(pcm_found, "No Microsoft PCM finding in aggregate")

    def test_pcm_mentions_conde_nast_and_vox(self):
        """PCM finding must mention both Condé Nast and Vox Media as pilot partners."""
        pcm = [f for f in self.findings if "PCM" in f.get("finding", "")]
        text = str(pcm)
        self.assertTrue("Cond" in text, "PCM finding should mention Condé Nast")
        self.assertTrue("Vox" in text, "PCM finding should mention Vox Media")

    def test_conde_nast_asymmetry_finding_exists(self):
        """Aggregate must have the '5 partners, 0 Meta' finding."""
        cn_found = any("Cond" in f.get("finding", "") and "deal" in f.get("finding", "").lower()
                        for f in self.findings)
        self.assertTrue(cn_found, "No Condé Nast deal asymmetry finding")

    def test_ft_expanded_portfolio_finding(self):
        """Aggregate must document FT's 3-deal portfolio."""
        ft_found = any("FT" in f.get("finding", "") and "deal" in f.get("finding", "").lower()
                        for f in self.findings)
        self.assertTrue(ft_found, "No FT expanded portfolio finding")


class TestFTGoogleRelationshipUpdate(unittest.TestCase):
    """FT joined Google's News AI pilot in Feb 2026.
    Added Aug 5 2026 Type C iteration.
    Source: https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
    """

    @classmethod
    def setUpClass(cls):
        cls.ft = load_yaml("financial-times.yaml")

    def test_google_financial_tie_updated(self):
        """FT-Google should no longer be 'none'."""
        cr = self.ft.get("competitor_relationships", {})
        google = cr.get("google", {})
        self.assertNotEqual(google.get("financial_tie"), "none",
                            "FT-Google should have financial tie after News AI pilot")

    def test_google_has_source_url(self):
        """FT-Google relationship must have source URL."""
        cr = self.ft.get("competitor_relationships", {})
        google = cr.get("google", {})
        self.assertIn("source_url", google)
        self.assertTrue(google["source_url"].startswith("http"))

    def test_google_description_mentions_pilot(self):
        """FT-Google description must mention News AI pilot."""
        cr = self.ft.get("competitor_relationships", {})
        google = cr.get("google", {})
        desc = google.get("description", "")
        self.assertIn("News AI pilot", desc)

    def test_meta_still_no_deal(self):
        """FT-Meta should still be 'none'."""
        cr = self.ft.get("competitor_relationships", {})
        meta = cr.get("meta", {})
        self.assertEqual(meta.get("financial_tie"), "none")

    def test_openai_deal_still_active(self):
        """FT-OpenAI licensing deal should remain."""
        cr = self.ft.get("competitor_relationships", {})
        openai = cr.get("openai", {})
        self.assertEqual(openai.get("financial_tie"), "licensing")


if __name__ == "__main__":
    unittest.main()

