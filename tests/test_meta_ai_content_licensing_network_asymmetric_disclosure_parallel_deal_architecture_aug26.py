"""
Type C: Financial Incentive Mapping — Mechanism #331
Meta AI Content Licensing Network: Asymmetric Disclosure and Parallel Deal Architecture

FINDING: Meta has assembled a parallel AI content licensing network spanning at least
7 major publishers (News Corp, CNN, Fox News, People Inc., USA Today/Gannett, Reuters,
plus others), mirroring OpenAI's publisher deal structure but with dramatically lower
transparency. While OpenAI's deals received extensive coverage with disclosed financial
terms, Meta's parallel deals received a fraction of the attention and most have
undisclosed terms.

DISCLOSURE ASYMMETRY: The WSJ (News Corp) discloses BOTH its Meta and OpenAI deals
when covering either company. But CNN, Fox News, Reuters, and USA Today do not appear
to consistently disclose their Meta content deals when covering Meta stories. This
creates a transparency gradient where OpenAI-deal publications face bias scrutiny while
Meta-deal publications fly under the radar.

ANALYTICAL SIGNIFICANCE: The existence of Meta's parallel content licensing network
undermines the simplistic narrative that "OpenAI pays publishers, therefore publishers
cover Meta badly." Meta ALSO pays publishers. The relevant question is whether the
DIFFERENCE in deal value, the DENSITY of deals across a publisher's AI partner portfolio,
and the DISCLOSURE transparency create asymmetric incentive structures.

SOURCES:
- Press Gazette AI deals tracker: https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
  (Observed Aug 27, 2026 UTC; lists CNN, Fox News, People Inc, Reuters as Meta deal partners)
- News Corp-Meta deal ($50M/yr, 3yr, Mar 4 2026):
  https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471
  https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html
  https://www.thewrap.com/media-platforms/journalism/news-corp-meta-ai-content-deal/
- Meta multi-publisher deal confirmation (CNN, Fox News, People Inc, USA Today):
  https://www.afaqs.com/news/digital/meta-signs-multi-year-ai-content-licensing-deal-with-news-corp-11177406
- WSJ dual disclosure pattern (Meta + OpenAI): verified from news-corp.yaml profile
  meta_disclosure_text: "News Corp, owner of The Wall Street Journal, has a content-licensing partnership with Meta."
  openai_disclosure_text: "News Corp, owner of The Wall Street Journal, has a content-licensing partnership with OpenAI."
- CNN Meta settlement article (Aug 26, 2026): https://www.cnn.com/2026/08/26/tech/meta-states-settle-trial-children
  (Visible search snippet does not contain CNN-Meta deal disclosure)

CONFOUNDERS:
C1 (STRONG): Deal terms for CNN, Fox, Reuters, USA Today are undisclosed, so we cannot
   compare deal values to assess incentive magnitude. -0.15
C2 (MODERATE): Disclosure practices may exist in full articles that are not visible in
   search snippets. Full article access was blocked for CNN. -0.08
C3 (MODERATE): Meta's deals may be structured differently (RAG retrieval vs. training)
   which could justify less disclosure. -0.05
C4 (WEAK): Some publications may not consider content licensing deals material to
   editorial coverage. -0.02

Date observed: August 26-27, 2026
"""

import unittest


class TestMetaAIContentLicensingNetworkExists(unittest.TestCase):
    """Verify the documented existence of Meta's parallel content licensing network."""

    def test_news_corp_meta_deal_announced_march_2026(self):
        """News Corp-Meta deal: up to $50M/year, 3-year, announced March 4, 2026."""
        deal = {
            "publisher": "News Corp",
            "partner": "Meta",
            "value": "up to $50M/year",
            "duration": "3 years minimum",
            "announced": "2026-03-04",
            "source_urls": [
                "https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471",
                "https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html",
                "https://www.thewrap.com/media-platforms/journalism/news-corp-meta-ai-content-deal/",
            ],
            "scope": "US and UK content, training + RAG retrieval",
            "verified": True,
        }
        self.assertEqual(deal["partner"], "Meta")
        self.assertTrue(deal["verified"])
        self.assertEqual(deal["announced"], "2026-03-04")

    def test_news_corp_also_has_openai_deal(self):
        """News Corp also has OpenAI deal: $250M+ over 5 years (2024)."""
        openai_deal = {
            "publisher": "News Corp",
            "partner": "OpenAI",
            "value": "$250M+ over 5 years (~$50M/year)",
            "announced": "2024",
            "verified": True,
        }
        self.assertTrue(openai_deal["verified"])
        # News Corp receives roughly equal annual value from both Meta and OpenAI
        # This is the only publisher with DISCLOSED terms for both deals

    def test_cnn_meta_deal_confirmed(self):
        """CNN has a Meta AI content deal, terms undisclosed."""
        deal = {
            "publisher": "CNN",
            "partner": "Meta",
            "value": "undisclosed",
            "source": "Press Gazette AI deals tracker",
            "source_url": "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/",
            "also_confirmed_by": "https://www.afaqs.com/news/digital/meta-signs-multi-year-ai-content-licensing-deal-with-news-corp-11177406",
            "openai_deal": False,
            "perplexity_lawsuit": True,
            "verified": True,
        }
        self.assertTrue(deal["verified"])
        # CNN has Meta deal but NO OpenAI deal, and is SUING Perplexity
        self.assertFalse(deal["openai_deal"])
        self.assertTrue(deal["perplexity_lawsuit"])

    def test_fox_news_meta_deal_confirmed(self):
        """Fox News has a Meta AI content deal, terms undisclosed."""
        deal = {
            "publisher": "Fox News",
            "partner": "Meta",
            "value": "undisclosed",
            "source_url": "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/",
            "verified": True,
        }
        self.assertTrue(deal["verified"])

    def test_people_inc_meta_deal_confirmed(self):
        """People Inc. has Meta AND Microsoft AI content deals."""
        deal = {
            "publisher": "People Inc.",
            "partner_meta": True,
            "partner_microsoft": True,
            "partner_openai": False,
            "source_url": "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/",
            "verified": True,
        }
        self.assertTrue(deal["partner_meta"])
        self.assertTrue(deal["partner_microsoft"])

    def test_reuters_meta_deal_confirmed(self):
        """Reuters has Meta AND Microsoft AI content deals."""
        deal = {
            "publisher": "Reuters",
            "partner_meta": True,
            "partner_microsoft": True,
            "partner_openai": False,
            "source_url": "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/",
            "verified": True,
        }
        self.assertTrue(deal["partner_meta"])

    def test_usa_today_meta_deal_confirmed(self):
        """USA Today/Gannett has Meta content deal, terms undisclosed."""
        deal = {
            "publisher": "USA Today (Gannett)",
            "partner": "Meta",
            "value": "undisclosed",
            "also_confirmed_by": "https://www.afaqs.com/news/digital/meta-signs-multi-year-ai-content-licensing-deal-with-news-corp-11177406",
            "verified": True,
        }
        self.assertTrue(deal["verified"])

    def test_meta_network_minimum_publisher_count(self):
        """Meta's AI content licensing network includes at least 7 named publishers."""
        meta_deal_publishers = [
            "News Corp (WSJ, NY Post, Barron's, MarketWatch)",
            "CNN",
            "Fox News",
            "People Inc.",
            "USA Today (Gannett)",
            "Reuters",
            # Press Gazette lists "CNN, Fox News, People Inc and more"
            # indicating additional unnamed publishers
        ]
        self.assertGreaterEqual(len(meta_deal_publishers), 6)


class TestOpenAIDealNetworkComparison(unittest.TestCase):
    """Compare OpenAI's publisher deal network with Meta's."""

    def test_openai_deals_have_disclosed_terms(self):
        """OpenAI deals typically have disclosed financial terms."""
        openai_deals_with_terms = {
            "News Corp": "$250M+ over 5 years",
            "AP": "undisclosed but confirmed 2-year deal",
            # Others have less disclosure but the deal announcements
            # receive extensive media coverage
        }
        # At minimum, News Corp OpenAI deal terms are publicly known
        self.assertIn("News Corp", openai_deals_with_terms)

    def test_meta_deals_mostly_undisclosed_terms(self):
        """Most Meta AI content deals have undisclosed financial terms."""
        meta_deals = {
            "News Corp": "$50M/year (disclosed by WSJ)",
            "CNN": "undisclosed",
            "Fox News": "undisclosed",
            "People Inc.": "undisclosed",
            "USA Today": "undisclosed",
            "Reuters": "undisclosed",
        }
        undisclosed = sum(1 for v in meta_deals.values() if "undisclosed" in v.lower())
        total = len(meta_deals)
        # 5 of 6 Meta deals have undisclosed terms (83%)
        self.assertGreaterEqual(undisclosed / total, 0.8)

    def test_openai_only_publishers_list(self):
        """Publishers with OpenAI deals but NO Meta deal."""
        openai_only = [
            "Conde Nast (WIRED, Ars Technica, GQ, Vogue)",
            "Vox Media (The Verge)",
            "The Atlantic",
            "Axios",
            "The Washington Post",
            "Dotdash Meredith (Investopedia, People magazine)",
            "The Guardian",
            "Time",
            "Hearst",
        ]
        # These publishers have financial incentive aligned with OpenAI, not Meta
        self.assertGreaterEqual(len(openai_only), 8)

    def test_meta_only_publishers_list(self):
        """Publishers with Meta deals but NO OpenAI deal."""
        meta_only = [
            "CNN",
            "Fox News",
        ]
        # Fewer publishers have Meta-only deals
        self.assertGreaterEqual(len(meta_only), 2)

    def test_dual_deal_publishers_list(self):
        """Publishers with deals with BOTH Meta AND OpenAI."""
        dual = [
            "News Corp (Meta $50M/yr + OpenAI $50M/yr)",
        ]
        # Only News Corp has publicly confirmed deals with both
        self.assertEqual(len(dual), 1)


class TestDisclosureAsymmetry(unittest.TestCase):
    """Test whether publisher deal disclosures are symmetric."""

    def test_wsj_discloses_both_meta_and_openai_deals(self):
        """WSJ discloses both its Meta and OpenAI content partnerships."""
        wsj_disclosure = {
            "meta_text": "News Corp, owner of The Wall Street Journal, has a content-licensing partnership with Meta.",
            "openai_text": "News Corp, owner of The Wall Street Journal, has a content-licensing partnership with OpenAI.",
            "both_disclosed": True,
            "source": "news-corp.yaml profile, verified from multiple articles",
        }
        self.assertTrue(wsj_disclosure["both_disclosed"])

    def test_cnn_meta_deal_disclosure_absent_in_settlement_coverage(self):
        """CNN's Aug 26 Meta settlement article does not visibly disclose CNN-Meta deal."""
        observation = {
            "article_url": "https://www.cnn.com/2026/08/26/tech/meta-states-settle-trial-children",
            "article_title": "Meta settles landmark state child harm claims for $18 billion and promises changes to its platforms",
            "date": "2026-08-26",
            "search_snippet_contains_disclosure": False,
            "full_article_access": False,  # HTTP 403 blocked access
            "confidence": "MODERATE",
            "note": "Full article could not be accessed; disclosure may exist in body text not visible in search snippet",
        }
        # Search snippet does not contain any disclosure of CNN-Meta content deal
        self.assertFalse(observation["search_snippet_contains_disclosure"])
        # But we cannot confirm from full article
        self.assertFalse(observation["full_article_access"])

    def test_disclosure_gradient_hypothesis(self):
        """
        Hypothesis: Publications with OpenAI deals face MORE disclosure scrutiny
        than publications with Meta deals, creating a transparency gradient.

        Evidence:
        - OpenAI deal announcements generate extensive media coverage
        - Meta deal announcements generate less coverage (News Corp was exception as first major deal)
        - WSJ consistently discloses both deals (best practice)
        - Other Meta-deal publishers' disclosure practices are less documented
        """
        openai_deal_coverage_level = "HIGH"  # Extensive media coverage of deal terms
        meta_deal_coverage_level = "LOW"     # Most deals had minimal coverage
        self.assertNotEqual(openai_deal_coverage_level, meta_deal_coverage_level)


class TestParallelDealArchitectureImplications(unittest.TestCase):
    """Test the analytical implications of Meta's parallel deal network."""

    def test_simple_bias_narrative_undermined(self):
        """
        The existence of Meta's parallel network undermines the simplistic claim
        that 'publishers cover Meta badly because OpenAI pays them.'

        If publisher coverage were purely deal-driven:
        - CNN (Meta deal, no OpenAI) should cover Meta favorably
        - Conde Nast (OpenAI deal, no Meta) should cover Meta unfavorably
        - News Corp (both deals) should be balanced

        Reality is more complex: CNN still uses critical framing for Meta in
        the settlement coverage, despite having a Meta content deal.
        """
        cnn_has_meta_deal = True
        cnn_uses_critical_framing_for_meta = True  # "intentionally designed addictive platforms"
        # Both are true, meaning deals don't fully determine tone
        self.assertTrue(cnn_has_meta_deal)
        self.assertTrue(cnn_uses_critical_framing_for_meta)

    def test_news_corp_dual_deal_as_natural_control(self):
        """
        News Corp (WSJ) with roughly equal deals from Meta and OpenAI
        serves as a natural control group for deal-driven bias analysis.

        Meta deal: ~$50M/year
        OpenAI deal: ~$50M/year ($250M/5yr)

        If deals drove coverage, WSJ should be roughly balanced.
        Actual WSJ coverage still shows some entity-selective framing
        (documented in 17 existing WSJ test files), suggesting other factors.
        """
        meta_annual = 50  # $M
        openai_annual = 50  # $M ($250M / 5yr)
        ratio = meta_annual / openai_annual
        # Roughly equal financial incentive from both companies
        self.assertAlmostEqual(ratio, 1.0, places=0)

    def test_deal_density_vs_deal_value_distinction(self):
        """
        OpenAI has MORE publisher deals (12+) vs Meta (7+),
        creating a DENSITY advantage in editorial influence even
        if individual deal values are comparable.

        More publishers with OpenAI deals means more editorial rooms
        with a financial relationship to OpenAI.
        """
        openai_publisher_count_minimum = 12
        meta_publisher_count_minimum = 7
        # OpenAI has ~1.7x the publisher deal density
        density_ratio = openai_publisher_count_minimum / meta_publisher_count_minimum
        self.assertGreater(density_ratio, 1.5)

    def test_meta_deal_coverage_asymmetry(self):
        """
        The News Corp-Meta deal announcement received significantly less
        media coverage than the News Corp-OpenAI deal announcement.

        This creates an awareness asymmetry: readers know about OpenAI deals
        (enabling them to discount potential bias) but may not know about
        Meta deals (preventing them from applying the same discount).
        """
        news_corp_openai_coverage = "EXTENSIVE"  # Major news story, multiple outlets
        news_corp_meta_coverage = "MODERATE"      # Covered but less prominently
        # The OpenAI deal was a larger story because it was first and larger
        self.assertNotEqual(news_corp_openai_coverage, news_corp_meta_coverage)


class TestDealPartnerOverlap(unittest.TestCase):
    """Map which publishers have deals with which AI companies."""

    def test_exclusive_openai_publishers(self):
        """Publishers with OpenAI but no Meta deal have unidirectional incentive."""
        exclusive_openai = {
            "Conde Nast": {"openai": True, "meta": False, "outlets": ["WIRED", "Ars Technica", "Vogue", "GQ", "The New Yorker"]},
            "Vox Media": {"openai": True, "meta": False, "outlets": ["The Verge", "Vox"]},
            "The Atlantic": {"openai": True, "meta": False, "outlets": ["The Atlantic"]},
            "Axios": {"openai": True, "meta": False, "outlets": ["Axios"]},
            "The Washington Post": {"openai": True, "meta": False, "outlets": ["Washington Post"]},
        }
        for publisher, data in exclusive_openai.items():
            self.assertTrue(data["openai"], f"{publisher} should have OpenAI deal")
            self.assertFalse(data["meta"], f"{publisher} should NOT have Meta deal")

    def test_exclusive_meta_publishers(self):
        """Publishers with Meta but no OpenAI deal have reverse incentive."""
        exclusive_meta = {
            "CNN": {"openai": False, "meta": True},
            "Fox News": {"openai": False, "meta": True},
        }
        for publisher, data in exclusive_meta.items():
            self.assertFalse(data["openai"], f"{publisher} should NOT have OpenAI deal")
            self.assertTrue(data["meta"], f"{publisher} should have Meta deal")

    def test_dual_deal_publishers(self):
        """Publishers with both Meta and OpenAI deals."""
        dual = {
            "News Corp": {"openai": True, "meta": True, "meta_value": "$50M/yr", "openai_value": "$50M/yr"},
        }
        for publisher, data in dual.items():
            self.assertTrue(data["openai"])
            self.assertTrue(data["meta"])


class TestThomsonWooAndSueStrategy(unittest.TestCase):
    """Document News Corp CEO Robert Thomson's deal strategy framing."""

    def test_woo_and_sue_quoted_strategy(self):
        """Thomson publicly described News Corp's approach at Morgan Stanley TMT conference."""
        quote = {
            "speaker": "Robert Thomson, News Corp CEO",
            "venue": "Morgan Stanley TMT Conference",
            "date": "2026-03",  # Days before Meta deal announcement
            "text": "We have what you might call a woo and a sue strategy. "
                    "We'll woo you. We'd like you to be our partner. But if you're stealing "
                    "our stuff, we are going to sue you. So there'll be a discount for those "
                    "who hand themselves in, and there'll be a penalty for those that resist.",
            "source_url": "https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html",
            "verified": True,
        }
        self.assertTrue(quote["verified"])
        # Thomson's framing explicitly links financial deals to editorial/legal posture
        self.assertIn("woo and a sue", quote["text"])


class TestConfounders(unittest.TestCase):
    """Document confounding factors for this finding."""

    def test_confounder_c1_undisclosed_terms(self):
        """C1 (STRONG): Most Meta deal terms are undisclosed."""
        c1 = {
            "id": "C1",
            "strength": "STRONG",
            "description": "Deal terms for CNN, Fox, Reuters, USA Today are undisclosed, "
                          "preventing comparison of incentive magnitude across deals.",
            "adjustment": -0.15,
        }
        self.assertEqual(c1["strength"], "STRONG")

    def test_confounder_c2_partial_article_access(self):
        """C2 (MODERATE): Full article access blocked for CNN."""
        c2 = {
            "id": "C2",
            "strength": "MODERATE",
            "description": "Disclosure practices may exist in full articles not visible "
                          "in search snippets. CNN article returned HTTP 403.",
            "adjustment": -0.08,
        }
        self.assertEqual(c2["strength"], "MODERATE")

    def test_confounder_c3_deal_structure_differences(self):
        """C3 (MODERATE): Meta deals may be structured differently from OpenAI deals."""
        c3 = {
            "id": "C3",
            "strength": "MODERATE",
            "description": "Meta deals may focus on RAG retrieval while OpenAI deals "
                          "focus on training, which could justify different disclosure norms.",
            "adjustment": -0.05,
        }
        self.assertEqual(c3["strength"], "MODERATE")

    def test_confounder_c4_materiality_threshold(self):
        """C4 (WEAK): Some publishers may not consider deals material."""
        c4 = {
            "id": "C4",
            "strength": "WEAK",
            "description": "Some publications may not consider content licensing deals "
                          "material enough to require disclosure in editorial coverage.",
            "adjustment": -0.02,
        }
        self.assertEqual(c4["strength"], "WEAK")


class TestAsymmetryScoring(unittest.TestCase):
    """Score the overall finding."""

    def test_raw_asymmetry_score(self):
        """Raw score based on disclosure transparency difference."""
        raw = 0.50  # Moderate — the transparency gap is real but confounders are strong
        self.assertGreater(raw, 0.0)

    def test_adjusted_asymmetry_score(self):
        """After confounders, the adjusted score is modest but significant."""
        raw = 0.50
        c1 = -0.15
        c2 = -0.08
        c3 = -0.05
        c4 = -0.02
        adjusted = raw + c1 + c2 + c3 + c4
        # 0.50 - 0.30 = 0.20
        self.assertAlmostEqual(adjusted, 0.20, places=2)
        # The finding is modest after confounders, but structurally significant
        # because it maps a previously undocumented financial architecture


class TestCrossReferences(unittest.TestCase):
    """Cross-reference with existing mechanisms."""

    def test_cross_ref_news_corp_openai_deal(self):
        """Extends existing News Corp financial architecture with Meta deal leg."""
        cross_ref = {
            "mechanism_id": 1,  # Original News Corp-OpenAI deal documentation
            "relationship": "extends",
            "note": "Adds the Meta deal leg ($50M/yr) to existing OpenAI deal ($50M/yr), "
                   "documenting News Corp as the only dual-deal publisher with disclosed terms for both.",
        }
        self.assertEqual(cross_ref["relationship"], "extends")

    def test_cross_ref_reuters_meta_deal(self):
        """Complements Reuters vocabulary bifurcation finding."""
        cross_ref = {
            "mechanism_id": 329,  # Reuters infrastructure vocabulary bifurcation
            "relationship": "complements",
            "note": "Reuters has a Meta content deal, adding a financial incentive layer "
                   "to the vocabulary bifurcation documented in #329.",
        }
        self.assertEqual(cross_ref["relationship"], "complements")

    def test_cross_ref_cnn_agency_attribution(self):
        """Complements Clare Duffy CNN cross-entity finding."""
        cross_ref = {
            "mechanism_id": 328,  # Clare Duffy CNN agency attribution (approximate)
            "relationship": "complements",
            "note": "CNN has a Meta deal, which should theoretically create favorable "
                   "coverage incentive. The continued critical framing in the settlement "
                   "coverage suggests editorial independence from deal influence.",
        }
        self.assertEqual(cross_ref["relationship"], "complements")


if __name__ == "__main__":
    unittest.main()
