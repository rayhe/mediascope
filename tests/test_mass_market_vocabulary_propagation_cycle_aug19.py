"""
Test: Mechanism #181 — Mass-Market Vocabulary Propagation Cycle
"Pervert Glasses" from Niche Activism to National Syndicated Radio, Late-Night TV, and Public Broadcasting

Validates the complete vocabulary propagation cycle documented in podcast-sentiment.md entries #33-#35:
- Kim Komando Daily Tech Update (500+ US stations, 6-8M weekly) used "pervert glasses" as episode title
- Jimmy Kimmel Live! (ABC, ~2.5M nightly) used "pervert glasses" on late-night network TV
- ABC News Daily Australia (publicly funded) adopted "pervert glasses" vocabulary
- TalkTV / The Sun (News Corp) used alarm framing despite Meta content partnership revenue
- Zero competitor products have ever received "pervert glasses" label

Key findings:
1. Vocabulary propagation from niche UK activism to mass-market American syndication
2. Three publicly funded broadcasters (BBC, DW, ABC Australia) independently converge
3. News Corp financial paradox: Meta partnership revenue + adversarial glasses coverage
4. Cultural consensus overrides financial incentive
"""

import yaml
import os
import unittest


def load_competitor_research():
    """Load the competitor coverage research YAML."""
    yaml_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "profiles",
        "competitor-coverage-research.yaml",
    )
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)


def load_podcast_sentiment():
    """Load the podcast sentiment markdown file."""
    md_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "podcast-sentiment.md",
    )
    with open(md_path, "r") as f:
        return f.read()


class TestMechanism181Exists(unittest.TestCase):
    """Verify mechanism #181 exists in competitor-coverage-research.yaml."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_mechanism_181_present_in_cross_publication_findings(self):
        """Mechanism #181 should exist in cross_publication_findings."""
        cpf = self.data.get("cross_publication_findings", {})
        self.assertIn(
            "mass_market_vocabulary_propagation_cycle",
            cpf,
            "Mechanism #181 (mass_market_vocabulary_propagation_cycle) missing from cross_publication_findings",
        )

    def test_mechanism_181_has_correct_id(self):
        """Mechanism #181 should have mechanism_id 181."""
        cpf = self.data.get("cross_publication_findings", {})
        mech = cpf.get("mass_market_vocabulary_propagation_cycle", {})
        self.assertEqual(mech.get("mechanism_id"), 181)

    def test_mechanism_181_has_asymmetry_score(self):
        """Mechanism #181 should have a top-level asymmetry_score."""
        cpf = self.data.get("cross_publication_findings", {})
        mech = cpf.get("mass_market_vocabulary_propagation_cycle", {})
        score = mech.get("asymmetry_score")
        self.assertIsNotNone(score, "Missing asymmetry_score")
        self.assertGreaterEqual(score, 0.8)
        self.assertLessEqual(score, 1.0)

    def test_mechanism_181_type(self):
        """Mechanism #181 should have podcast_broadcast_vocabulary_propagation type."""
        cpf = self.data.get("cross_publication_findings", {})
        mech = cpf.get("mass_market_vocabulary_propagation_cycle", {})
        self.assertEqual(
            mech.get("type"),
            "podcast_broadcast_vocabulary_propagation",
        )


class TestVocabularyPropagationCycleStages(unittest.TestCase):
    """Validate the documented vocabulary propagation stages."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = self.cpf.get("mass_market_vocabulary_propagation_cycle", {})

    def test_entities_include_meta(self):
        """Meta must be in the entity list — it's the exclusive target."""
        entities = self.mech.get("entities", [])
        self.assertIn("Meta", entities)

    def test_entities_include_competitors(self):
        """Competitors should be listed to document the zero-scrutiny finding."""
        entities = self.mech.get("entities", [])
        for competitor in ["Samsung", "Google", "Apple"]:
            self.assertIn(
                competitor,
                entities,
                f"{competitor} should be listed as entity (zero-scrutiny target)",
            )

    def test_key_finding_mass_audience(self):
        """Mass audience finding should reference Kim Komando and/or Jimmy Kimmel."""
        finding = self.mech.get("key_finding_mass_audience", "")
        self.assertTrue(
            "Komando" in finding or "Kimmel" in finding,
            "Mass audience finding should reference Kim Komando or Jimmy Kimmel",
        )

    def test_key_finding_public_broadcasters(self):
        """Public broadcaster finding should reference BBC, DW, and ABC."""
        finding = self.mech.get("key_finding_public_broadcasters", "")
        for broadcaster in ["BBC", "DW", "ABC"]:
            self.assertIn(
                broadcaster,
                finding,
                f"Public broadcaster finding should reference {broadcaster}",
            )

    def test_key_finding_news_corp_paradox(self):
        """News Corp paradox finding should document the financial override."""
        finding = self.mech.get("key_finding_news_corp_paradox", "")
        self.assertIn("News Corp", finding)
        self.assertTrue(
            "revenue" in finding.lower() or "partnership" in finding.lower(),
            "News Corp finding should reference financial relationship",
        )


class TestPodcastSentimentEntries(unittest.TestCase):
    """Validate the three new podcast entries (#33, #34, #35) exist."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_33_kim_komando_exists(self):
        """Entry #33 (Kim Komando) should exist in podcast-sentiment.md."""
        self.assertIn(
            "Kim Komando",
            self.content,
            "Entry #33 (Kim Komando Daily Tech Update) missing from podcast-sentiment.md",
        )

    def test_entry_33_pervert_glasses_in_title(self):
        """Kim Komando episode should document 'pervert glasses' in episode title."""
        self.assertIn(
            'AKA \'pervert glasses\'',
            self.content,
        )

    def test_entry_33_syndication_scale(self):
        """Kim Komando entry should document syndication scale (500+ stations)."""
        self.assertIn(
            "500+",
            self.content,
            "Kim Komando entry should document 500+ station syndication",
        )

    def test_entry_33_jimmy_kimmel_reference(self):
        """Kim Komando entry should reference Jimmy Kimmel's usage."""
        self.assertIn("Kimmel", self.content)

    def test_entry_34_abc_news_daily_exists(self):
        """Entry #34 (ABC News Daily Australia) should exist."""
        self.assertIn(
            "ABC News Daily",
            self.content,
            "Entry #34 (ABC News Daily Australia) missing",
        )

    def test_entry_34_milica_stilinovic(self):
        """ABC News Daily entry should reference Dr. Milica Stilinovic."""
        self.assertIn("Stilinovic", self.content)

    def test_entry_34_publicly_funded_broadcaster_count(self):
        """ABC entry should note it's the third publicly funded broadcaster."""
        # Check that the three-broadcaster pattern is documented
        lower = self.content.lower()
        self.assertTrue(
            "third publicly funded" in lower or "three publicly funded" in lower
            or "3 publicly funded" in lower or "#3 publicly funded" in lower,
            "ABC entry should note it's the third publicly funded broadcaster",
        )

    def test_entry_35_talktv_exists(self):
        """Entry #35 (TalkTV) should exist."""
        self.assertIn(
            "TalkTV",
            self.content,
            "Entry #35 (TalkTV) missing from podcast-sentiment.md",
        )

    def test_entry_35_sean_keach(self):
        """TalkTV entry should reference Sean Keach of The Sun."""
        self.assertIn("Sean Keach", self.content)

    def test_entry_35_news_corp_paradox(self):
        """TalkTV entry should document the News Corp financial paradox."""
        self.assertIn("News Corp", self.content)


class TestPublicBroadcasterConvergence(unittest.TestCase):
    """Validate the three-continent publicly funded broadcaster convergence."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_bbc_documented(self):
        """BBC should be documented in podcast-sentiment.md."""
        self.assertIn("BBC", self.content)

    def test_dw_documented(self):
        """DW / Deutsche Welle should be documented."""
        self.assertIn("DW", self.content)

    def test_abc_australia_documented(self):
        """ABC Australia should be documented."""
        self.assertIn("ABC News Daily", self.content)

    def test_three_continents_covered(self):
        """Documentation should reference three continents."""
        lower = self.content.lower()
        self.assertTrue(
            "three continents" in lower or "3 continents" in lower,
            "Public broadcaster convergence should document three continents",
        )


class TestNewsCorporateFinancialParadox(unittest.TestCase):
    """Validate the News Corp financial paradox documentation."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_meta_partnership_revenue_documented(self):
        """News Corp's Meta content partnership should be documented."""
        self.assertIn(
            "Meta content partnership",
            self.content,
            "News Corp's Meta financial relationship should be documented",
        )

    def test_openai_licensing_documented(self):
        """News Corp's OpenAI licensing deal should be documented."""
        self.assertIn(
            "250M",
            self.content,
            "News Corp's $250M OpenAI deal should be documented",
        )

    def test_cultural_consensus_overrides(self):
        """Documentation should note cultural consensus overriding financial incentive."""
        lower = self.content.lower()
        self.assertTrue(
            "cultural consensus" in lower and "override" in lower,
            "Should document cultural consensus overriding financial incentive",
        )


class TestVocabularyPropagationTimeline(unittest.TestCase):
    """Validate the documented vocabulary propagation timeline."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_propagation_stages_documented(self):
        """Key propagation stages should be documented."""
        # Check for the major stages
        self.assertIn("niche", self.content.lower())
        self.assertIn("syndicated", self.content.lower())
        self.assertIn("late-night", self.content.lower())

    def test_zero_competitor_vocabulary(self):
        """Documentation should assert zero competitor 'pervert glasses' usage."""
        lower = self.content.lower()
        self.assertTrue(
            "zero competitor" in lower or "no competitor" in lower,
            "Should document that zero competitors have received 'pervert glasses' label",
        )


class TestMechanism181CrossReferences(unittest.TestCase):
    """Validate cross-references in mechanism #181."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = self.cpf.get("mass_market_vocabulary_propagation_cycle", {})

    def test_cross_references_exist(self):
        """Mechanism #181 should have cross-references."""
        refs = self.mech.get("cross_references", [])
        self.assertIsInstance(refs, list)
        self.assertGreater(len(refs), 0, "Should have cross-references")

    def test_cross_references_include_podcast_amplification(self):
        """Should cross-reference mechanism #144 (Podcast Ecosystem Amplification)."""
        refs = self.mech.get("cross_references", [])
        self.assertIn(144, refs, "Should cross-reference #144")

    def test_cross_references_include_multi_vector_cascade(self):
        """Should cross-reference mechanism #158 (Multi-Vector Cascade)."""
        refs = self.mech.get("cross_references", [])
        self.assertIn(158, refs, "Should cross-reference #158")

    def test_cross_references_include_kodak_fiend(self):
        """Should cross-reference mechanism #177 (Kodak Fiend)."""
        refs = self.mech.get("cross_references", [])
        self.assertIn(177, refs, "Should cross-reference #177")


class TestMechanism181SourceURLs(unittest.TestCase):
    """Validate source URLs for mechanism #181."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = self.cpf.get("mass_market_vocabulary_propagation_cycle", {})

    def test_source_urls_exist(self):
        """Mechanism #181 should have source URLs."""
        urls = self.mech.get("source_urls", [])
        self.assertIsInstance(urls, list)
        self.assertGreaterEqual(len(urls), 3, "Should have at least 3 source URLs")

    def test_source_urls_are_https(self):
        """All source URLs should use HTTPS."""
        urls = self.mech.get("source_urls", [])
        for url in urls:
            self.assertTrue(
                url.startswith("https://"),
                f"URL should use HTTPS: {url}",
            )

    def test_source_urls_include_komando(self):
        """Should include a Komando/Deezer source URL."""
        urls = self.mech.get("source_urls", [])
        has_komando = any("komando" in u or "deezer" in u for u in urls)
        self.assertTrue(has_komando, "Should include a Komando source URL")

    def test_source_urls_include_abc_aus(self):
        """Should include an ABC Australia/Podbean source URL."""
        urls = self.mech.get("source_urls", [])
        has_abc = any("podbean" in u for u in urls)
        self.assertTrue(has_abc, "Should include an ABC Australia source URL")

    def test_source_urls_include_talktv(self):
        """Should include a TalkTV/YouTube source URL."""
        urls = self.mech.get("source_urls", [])
        has_talktv = any("youtube" in u for u in urls)
        self.assertTrue(has_talktv, "Should include a TalkTV source URL")


class TestUpdatedSummaryTable(unittest.TestCase):
    """Validate the updated cross-medium asymmetry summary table."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_entry_count_updated_to_37(self):
        """Summary should reference 37 entries (updated from 35)."""
        self.assertIn("37 entries", self.content)

    def test_mass_market_pattern_in_summary(self):
        """Summary table should include mass-market syndication pattern."""
        self.assertIn("Mass-market syndication adoption", self.content)

    def test_public_broadcaster_convergence_in_summary(self):
        """Summary table should include publicly funded broadcaster convergence."""
        self.assertIn("Publicly funded broadcaster convergence", self.content)

    def test_financial_relationship_override_in_summary(self):
        """Summary table should include financial relationship override pattern."""
        self.assertIn("Financial relationship override", self.content)

    def test_vocabulary_propagation_completed_in_summary(self):
        """Summary table should include vocabulary propagation completed pattern."""
        self.assertIn("Vocabulary propagation completed", self.content)


if __name__ == "__main__":
    unittest.main()
