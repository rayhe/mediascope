"""
Tests for cross-platform financial incentive mapping.

Validates the comprehensive financial relationship matrix across all major
AI platforms (OpenAI, Amazon, Google, Microsoft, Perplexity/ProRata) for
each MediaScope-profiled publication. Tests the aggregate incentive gradient:
17 competitor revenue streams across 7/8 publications vs. 0 Meta deals.

Source URLs verified 2026-08-05:
- LLM Pulse: https://llmpulse.ai/blog/openai-publisher-deals/
- Press Gazette: https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Digiday (Amazon Rufus): https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/
- MediaPost (Alexa+): https://www.Mediapost.Com/publications/article/403742/
- Microsoft PCM blog: https://about.ads.microsoft.com/en/blog/post/february-2026/building-toward-a-sustainable-content-economy-for-the-agentic-web
- TechCrunch (Google pilot): https://techcrunch.com/2025/12/10/google-is-testing-ai-powered-article-overviews-on-select-publications-google-news-pages/
- WSJ (Marketplaces): https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00
"""

import yaml
import os
import pytest


@pytest.fixture(scope="module")
def entities():
    """Load competitor-entities.yaml once for all tests."""
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


class TestExcludedPublisherStructure:
    """Validate that all excluded publishers have complete deal data."""

    def test_all_eight_publications_present(self, entities):
        """All 8 MediaScope-profiled publications appear in excluded_publishers."""
        names = [p["name"] for p in entities["meta_ai_deals"]["excluded_publishers"]]
        expected_fragments = [
            "Condé Nast", "Vox Media", "Atlantic", "New York Times",
            "Financial Times", "Guardian", "MIT", "Gizmodo"
        ]
        for frag in expected_fragments:
            assert any(frag in n for n in names), f"Missing publication containing '{frag}'"

    def test_each_publisher_has_meta_deal_field(self, entities):
        """Every excluded publisher explicitly declares meta_deal status."""
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            assert "meta_deal" in pub, f"{pub['name']} missing meta_deal field"

    def test_all_meta_deals_are_none(self, entities):
        """All 8 excluded publishers have meta_deal = 'none'."""
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            assert pub["meta_deal"] == "none", f"{pub['name']} has unexpected meta_deal: {pub['meta_deal']}"

    def test_each_publisher_has_deal_count(self, entities):
        """Every excluded publisher has a deal_count field."""
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            assert "deal_count" in pub, f"{pub['name']} missing deal_count"

    def test_deal_count_matches_deals_list(self, entities):
        """deal_count matches revenue-generating (non-negotiating, non-litigation) deals."""
        non_revenue_types = {"negotiating", "adversarial_litigation"}
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            deals = pub.get("deals_with_competitors", [])
            if isinstance(deals, list) and len(deals) > 0 and isinstance(deals[0], dict):
                revenue_deals = [d for d in deals if d.get("type") not in non_revenue_types]
                assert pub["deal_count"] == len(revenue_deals), (
                    f"{pub['name']}: deal_count {pub['deal_count']} != "
                    f"revenue deals length {len(revenue_deals)}"
                )


class TestCondeNastFinancialRelationships:
    """Condé Nast (WIRED) should have 5 competitor revenue streams."""

    def _get_conde_nast(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "Condé Nast" in pub["name"]:
                return pub
        pytest.fail("Condé Nast not found in excluded_publishers")

    def test_conde_nast_has_openai_deal(self, entities):
        pub = self._get_conde_nast(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("OpenAI" in p for p in partners)

    def test_conde_nast_has_amazon_rufus_deal(self, entities):
        pub = self._get_conde_nast(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Rufus" in p for p in partners), "Missing Amazon Rufus deal"

    def test_conde_nast_has_amazon_alexa_deal(self, entities):
        pub = self._get_conde_nast(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Alexa" in p for p in partners), "Missing Amazon Alexa+ deal"

    def test_conde_nast_has_microsoft_pcm(self, entities):
        pub = self._get_conde_nast(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Microsoft" in p for p in partners), "Missing Microsoft PCM deal"

    def test_conde_nast_has_perplexity_deal(self, entities):
        pub = self._get_conde_nast(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Perplexity" in p for p in partners), "Missing Perplexity Comet Plus deal"

    def test_conde_nast_deal_count_is_five(self, entities):
        pub = self._get_conde_nast(entities)
        assert pub["deal_count"] == 5

    def test_conde_nast_zero_meta_deals(self, entities):
        pub = self._get_conde_nast(entities)
        assert pub["meta_deal"] == "none"

    def test_conde_nast_openai_date_aug_2024(self, entities):
        pub = self._get_conde_nast(entities)
        openai = [d for d in pub["deals_with_competitors"] if d["partner"] == "OpenAI"][0]
        assert "2024-08" in openai["date"]

    def test_conde_nast_all_deals_have_source_urls(self, entities):
        """Every Condé Nast deal (except Apple negotiating) has a source URL."""
        pub = self._get_conde_nast(entities)
        for deal in pub["deals_with_competitors"]:
            if "Apple" not in deal["partner"]:
                assert deal.get("source_url"), f"Deal with {deal['partner']} missing source_url"


class TestVoxMediaFinancialRelationships:
    """Vox Media (The Verge) should have 3 competitor revenue streams."""

    def _get_vox(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "Vox Media" in pub["name"]:
                return pub
        pytest.fail("Vox Media not found")

    def test_vox_has_openai_deal(self, entities):
        pub = self._get_vox(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("OpenAI" in p for p in partners)

    def test_vox_has_microsoft_pcm(self, entities):
        pub = self._get_vox(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Microsoft" in p for p in partners)

    def test_vox_has_amazon_alexa(self, entities):
        pub = self._get_vox(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Amazon" in p for p in partners)

    def test_vox_deal_count_is_three(self, entities):
        pub = self._get_vox(entities)
        assert pub["deal_count"] == 3

    def test_vox_zero_meta_deals(self, entities):
        pub = self._get_vox(entities)
        assert pub["meta_deal"] == "none"


class TestNYTFinancialRelationships:
    """NYT has Amazon deals and is suing OpenAI — paradoxical AI posture."""

    def _get_nyt(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "New York Times" in pub["name"]:
                return pub
        pytest.fail("NYT not found")

    def test_nyt_has_amazon_rufus(self, entities):
        pub = self._get_nyt(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Rufus" in p for p in partners)

    def test_nyt_has_openai_litigation(self, entities):
        pub = self._get_nyt(entities)
        openai_deals = [d for d in pub["deals_with_competitors"] if "OpenAI" in d["partner"]]
        assert len(openai_deals) == 1
        assert openai_deals[0]["type"] == "adversarial_litigation"

    def test_nyt_amazon_deal_value_documented(self, entities):
        pub = self._get_nyt(entities)
        rufus = [d for d in pub["deals_with_competitors"] if "Rufus" in d["partner"]][0]
        assert "$20-25M" in rufus["value"]

    def test_nyt_zero_meta_deals(self, entities):
        pub = self._get_nyt(entities)
        assert pub["meta_deal"] == "none"


class TestFTFinancialRelationships:
    """FT has 3 competitor revenue streams: OpenAI, Google, Microsoft."""

    def _get_ft(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "Financial Times" in pub["name"]:
                return pub
        pytest.fail("FT not found")

    def test_ft_has_openai(self, entities):
        pub = self._get_ft(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("OpenAI" in p for p in partners)

    def test_ft_has_google_pilot(self, entities):
        pub = self._get_ft(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Google" in p for p in partners)

    def test_ft_has_microsoft_pcm(self, entities):
        pub = self._get_ft(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Microsoft" in p for p in partners)

    def test_ft_deal_count_is_three(self, entities):
        pub = self._get_ft(entities)
        assert pub["deal_count"] == 3

    def test_ft_google_pilot_joined_feb_2026(self, entities):
        pub = self._get_ft(entities)
        google = [d for d in pub["deals_with_competitors"] if "Google" in d["partner"]][0]
        assert "2026-02" in google["date"] or "Feb 2026" in google.get("scope", "")


class TestGuardianFinancialRelationships:
    """The Guardian has 2 competitor revenue streams."""

    def _get_guardian(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "Guardian" in pub["name"]:
                return pub
        pytest.fail("Guardian not found")

    def test_guardian_has_openai(self, entities):
        pub = self._get_guardian(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("OpenAI" in p for p in partners)

    def test_guardian_has_google_pilot(self, entities):
        pub = self._get_guardian(entities)
        partners = [d["partner"] for d in pub["deals_with_competitors"]]
        assert any("Google" in p for p in partners)

    def test_guardian_openai_includes_enterprise_chatgpt(self, entities):
        """Guardian deal includes ChatGPT Enterprise rollout internally."""
        pub = self._get_guardian(entities)
        openai = [d for d in pub["deals_with_competitors"] if "OpenAI" in d["partner"]][0]
        assert "Enterprise" in openai.get("scope", "")

    def test_guardian_google_pilot_is_original_cohort(self, entities):
        pub = self._get_guardian(entities)
        google = [d for d in pub["deals_with_competitors"] if "Google" in d["partner"]][0]
        assert "2025-12" in google["date"]

    def test_guardian_zero_meta_deals(self, entities):
        pub = self._get_guardian(entities)
        assert pub["meta_deal"] == "none"


class TestGizmodoCleanlControl:
    """Gizmodo has zero deals — clean control for isolating editorial culture."""

    def _get_gizmodo(self, entities):
        for pub in entities["meta_ai_deals"]["excluded_publishers"]:
            if "Gizmodo" in pub["name"]:
                return pub
        pytest.fail("Gizmodo not found")

    def test_gizmodo_zero_competitor_deals(self, entities):
        pub = self._get_gizmodo(entities)
        assert pub["deal_count"] == 0

    def test_gizmodo_zero_meta_deals(self, entities):
        pub = self._get_gizmodo(entities)
        assert pub["meta_deal"] == "none"

    def test_gizmodo_empty_deals_list(self, entities):
        pub = self._get_gizmodo(entities)
        assert pub["deals_with_competitors"] == []

    def test_gizmodo_still_adversarial(self, entities):
        """Gizmodo should be marked as adversarial despite no financial incentive."""
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        giz = [p for p in matrix if "Gizmodo" in p["name"]][0]
        assert giz["adversarial_meta_coverage"] is True


class TestAggregateIncentiveMatrix:
    """Validate the aggregate financial incentive matrix statistics."""

    def test_matrix_has_eight_publications(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        assert len(matrix) == 8

    def test_total_competitor_deals_is_eighteen(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        assert matrix["total_competitor_deal_count"] == 18

    def test_total_meta_deals_is_zero(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        assert matrix["total_meta_deal_count"] == 0

    def test_all_publications_adversarial(self, entities):
        """All 8 publications show adversarial Meta coverage."""
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        for pub in matrix:
            assert pub["adversarial_meta_coverage"] is True, f"{pub['name']} not adversarial"

    def test_all_publications_zero_meta_deals(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        for pub in matrix:
            assert pub["meta_deals"] == 0, f"{pub['name']} has non-zero meta_deals"

    def test_wired_leads_with_five_deals(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        wired = [p for p in matrix if "WIRED" in p["name"]][0]
        assert wired["competitor_deals"] == 5

    def test_ft_and_verge_have_three_deals(self, entities):
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        ft = [p for p in matrix if "Financial Times" in p["name"]][0]
        verge = [p for p in matrix if "Verge" in p["name"]][0]
        assert ft["competitor_deals"] == 3
        assert verge["competitor_deals"] == 3

    def test_sum_of_individual_deals_equals_total(self, entities):
        """Sanity check: sum of individual deal counts = total."""
        matrix = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        pubs = matrix["publications"]
        individual_sum = sum(p["competitor_deals"] for p in pubs)
        assert individual_sum == matrix["total_competitor_deal_count"]


class TestGoogleNewsAIPilot:
    """Validate Google News AI pilot data in cross_platform_summary."""

    def test_pilot_has_nine_or_more_participants(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert len(pilot["confirmed_participants"]) >= 9

    def test_guardian_in_pilot(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert any("Guardian" in p for p in pilot["confirmed_participants"])

    def test_ft_in_pilot(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert any("Financial Times" in p for p in pilot["confirmed_participants"])

    def test_washington_post_in_pilot(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert any("Washington Post" in p for p in pilot["confirmed_participants"])

    def test_pilot_announced_dec_2025(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert "2025-12" in pilot["announced"]

    def test_gemini_has_ap(self, entities):
        pilot = entities["meta_ai_deals"]["cross_platform_summary"]["google_news_ai_pilot"]
        assert any("Associated Press" in p for p in pilot["gemini_real_time_partners"])


class TestMicrosoftPCM:
    """Validate Microsoft PCM data."""

    def test_pcm_has_seven_pilot_partners(self, entities):
        pcm = entities["meta_ai_deals"]["cross_platform_summary"]["microsoft_pcm"]
        assert len(pcm["pilot_partners"]) == 7

    def test_conde_nast_in_pcm(self, entities):
        pcm = entities["meta_ai_deals"]["cross_platform_summary"]["microsoft_pcm"]
        assert "Condé Nast" in pcm["pilot_partners"]

    def test_vox_media_in_pcm(self, entities):
        pcm = entities["meta_ai_deals"]["cross_platform_summary"]["microsoft_pcm"]
        assert "Vox Media LLC" in pcm["pilot_partners"]

    def test_yahoo_is_demand_partner(self, entities):
        pcm = entities["meta_ai_deals"]["cross_platform_summary"]["microsoft_pcm"]
        assert "Yahoo" in str(pcm["demand_partners"])


class TestMetaAIDeals:
    """Validate Meta's own deal data for contrast."""

    def test_meta_has_thirteen_partners(self, entities):
        partners = entities["meta_ai_deals"]["partners"]
        assert len(partners) == 13

    def test_news_corp_is_largest_meta_deal(self, entities):
        nc = [p for p in entities["meta_ai_deals"]["partners"] if p["name"] == "News Corp"][0]
        assert "$50M/yr" in nc["terms"]

    def test_reuters_is_first_meta_deal(self, entities):
        partners = entities["meta_ai_deals"]["partners"]
        dates = [(p["name"], p["date"]) for p in partners]
        reuters = [d for d in dates if "Reuters" in d[0]][0]
        assert "2024-10" in reuters[1]

    def test_no_mediascope_profiled_publication_has_meta_deal(self, entities):
        """Cross-check: no MediaScope publication appears in Meta's partner list."""
        meta_partners = [p["name"].lower() for p in entities["meta_ai_deals"]["partners"]]
        meta_parents = [p.get("parent", "").lower() for p in entities["meta_ai_deals"]["partners"]]
        all_meta = " ".join(meta_partners + meta_parents)
        adversarial_pubs = ["wired", "verge", "atlantic", "new york times",
                            "financial times", "guardian", "mit technology review", "gizmodo"]
        for pub in adversarial_pubs:
            assert pub not in all_meta, f"{pub} found in Meta's partner list"
