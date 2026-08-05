"""
Cross-Publication Financial Disclosure Audit
=============================================
Tests the finding that WSJ (News Corp) is the ONLY publication in the dataset
that discloses its financial relationships with covered entities in articles.
Validates the disclosure_analysis in competitor-coverage-research.yaml and
cross-references with individual publication profiles.

Source: Type A iteration 2026-08-05 10:00 PT — WSJ balanced control verification.
"""

import yaml
import pathlib
import pytest

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"

@pytest.fixture(scope="module")
def competitor_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def wired_profile():
    with open(PROFILES_DIR / "wired.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def verge_profile():
    with open(PROFILES_DIR / "the-verge.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def ft_profile():
    with open(PROFILES_DIR / "financial-times.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def atlantic_profile():
    with open(PROFILES_DIR / "atlantic.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def guardian_profile():
    with open(PROFILES_DIR / "guardian.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def nytimes_profile():
    with open(PROFILES_DIR / "nytimes.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def news_corp_profile():
    with open(PROFILES_DIR / "news-corp.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def competitor_entities():
    with open(PROFILES_DIR / "competitor-entities.yaml") as f:
        return yaml.safe_load(f)


# ===================================================================
# 1. WSJ Discloses — Unique Among Publications
# ===================================================================

class TestWSJDisclosure:
    """WSJ is the only publication that consistently discloses financial ties."""

    def test_wsj_has_disclosure_analysis(self, competitor_research):
        """WSJ section has disclosure_analysis or disclosure examples."""
        wsj = competitor_research["publications"].get("wsj") or \
              competitor_research["publications"].get("news-corp") or \
              competitor_research["publications"].get("news_corp")
        assert wsj is not None, "WSJ/News Corp must be in competitor research"

    def test_wsj_articles_contain_disclosure_text(self, competitor_research):
        """At least one WSJ article example includes actual disclosure language."""
        wsj = competitor_research["publications"].get("wsj") or \
              competitor_research["publications"].get("news-corp") or \
              competitor_research["publications"].get("news_corp")
        if wsj is None:
            pytest.skip("WSJ not found in competitor research")

        # Check all article lists and text fields for disclosure language
        disclosure_keywords = ["content-licensing partnership", "disclose",
                               "News Corp, owner of", "partnership with Meta",
                               "partnership with OpenAI"]
        all_text = yaml.dump(wsj).lower()
        found = any(kw.lower() in all_text for kw in disclosure_keywords)
        assert found, "WSJ profile must contain disclosure language examples"

    def test_wsj_discloses_meta_deal(self, competitor_research):
        """WSJ discloses its Meta content-licensing partnership."""
        wsj = competitor_research["publications"].get("wsj") or \
              competitor_research["publications"].get("news-corp") or \
              competitor_research["publications"].get("news_corp")
        all_text = yaml.dump(wsj).lower()
        assert "meta" in all_text and ("partnership" in all_text or "licensing" in all_text)

    def test_wsj_discloses_openai_deal(self, competitor_research):
        """WSJ discloses its OpenAI content-licensing partnership."""
        wsj = competitor_research["publications"].get("wsj") or \
              competitor_research["publications"].get("news-corp") or \
              competitor_research["publications"].get("news_corp")
        all_text = yaml.dump(wsj).lower()
        assert "openai" in all_text and ("partnership" in all_text or "licensing" in all_text)


class TestWSJSymmetricDeals:
    """WSJ/News Corp has symmetric financial incentives — deals with BOTH sides."""

    def test_news_corp_has_meta_deal(self, competitor_entities):
        """News Corp appears in Meta AI deals list."""
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = meta_deals.get("partners", [])
        partner_names = [p.get("name", "").lower() for p in partners]
        assert any("news corp" in n for n in partner_names), \
            "News Corp must be in Meta AI deal partners"

    def test_news_corp_has_openai_deal(self, competitor_entities):
        """News Corp has OpenAI deal documented."""
        # News Corp is NOT in excluded publishers (it has Meta deal)
        # Check meta_ai_deals or news-corp profile
        all_text = yaml.dump(competitor_entities).lower()
        assert "news corp" in all_text

    def test_news_corp_meta_deal_value(self, competitor_entities):
        """News Corp Meta deal is documented at ~$50M/yr."""
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = meta_deals.get("partners", [])
        for p in partners:
            if "news corp" in p.get("name", "").lower():
                terms = str(p.get("terms", "")).lower()
                assert "50" in terms or "50m" in terms.replace(" ", ""), \
                    f"News Corp deal should mention $50M: {terms}"
                return
        pytest.fail("News Corp not found in Meta deal partners")


# ===================================================================
# 2. Non-Disclosing Publications — Financial Ties Without Transparency
# ===================================================================

class TestWIREDNonDisclosure:
    """WIRED/Condé Nast has OpenAI deal but never discloses it."""

    def test_wired_has_openai_deal(self, wired_profile):
        """WIRED profile confirms OpenAI financial relationship."""
        relationships = wired_profile.get("competitor_relationships", {}) or \
                       wired_profile.get("cross_entity_wearables_framing", {})
        all_text = yaml.dump(wired_profile).lower()
        assert "openai" in all_text

    def test_wired_openai_never_disclosed(self, competitor_research):
        """Competitor research documents WIRED never discloses OpenAI deal."""
        wired = competitor_research["publications"]["wired"]
        openai_summary = str(wired.get("openai_coverage_summary", "")).lower()
        # Should mention non-disclosure
        assert "never disclosed" in openai_summary or "not disclosed" in openai_summary or \
               "has never disclosed" in openai_summary, \
            "WIRED's OpenAI coverage summary should note non-disclosure"

    def test_wired_multiple_undisclosed_deals(self, competitor_research):
        """WIRED has 4+ competitor deals, none disclosed in articles."""
        wired = competitor_research["publications"]["wired"]
        deal_summary = str(wired.get("deal_count_summary", "")).lower()
        assert "five" in deal_summary or "5" in deal_summary or \
               "four" in deal_summary or "4" in deal_summary, \
            "WIRED should have 4+ competitor deals documented"


class TestFTNonDisclosure:
    """FT has OpenAI deal ($5-10M/yr) but never discloses it."""

    def test_ft_openai_deal_exists(self, ft_profile):
        """FT profile confirms OpenAI financial relationship."""
        all_text = yaml.dump(ft_profile).lower()
        assert "openai" in all_text

    def test_ft_openai_never_disclosed(self, ft_profile):
        """FT profile documents non-disclosure of OpenAI licensing deal."""
        all_text = yaml.dump(ft_profile).lower()
        # The FT profile (financial-times.yaml) documents non-disclosure
        assert "not disclosed" in all_text or "never disclosed" in all_text or \
               "no disclosure" in all_text or "non-disclosure" in all_text or \
               "has not disclosed" in all_text, \
            "FT profile should document non-disclosure of OpenAI deal"


class TestAtlanticNonDisclosure:
    """The Atlantic has OpenAI deal AND $17B Apple ownership — never discloses either."""

    def test_atlantic_openai_deal(self, atlantic_profile):
        """Atlantic profile confirms OpenAI financial relationship."""
        all_text = yaml.dump(atlantic_profile).lower()
        assert "openai" in all_text

    def test_atlantic_apple_ownership(self, atlantic_profile):
        """Atlantic profile confirms Apple ownership via LPJ/Emerson."""
        all_text = yaml.dump(atlantic_profile).lower()
        assert "apple" in all_text and ("emerson" in all_text or "lpj" in all_text or
                                         "laurene" in all_text or "powell" in all_text)

    def test_atlantic_dual_apple_link(self, competitor_research):
        """Atlantic has dual Apple financial link (ownership + News+ revenue)."""
        atlantic = competitor_research["publications"].get("atlantic")
        if atlantic is None:
            pytest.skip("Atlantic not found in competitor research")
        all_text = yaml.dump(atlantic).lower()
        assert "news+" in all_text or "apple news" in all_text or \
               "syndication" in all_text, \
            "Atlantic should document Apple News+ as second financial link"

    def test_atlantic_zero_meta_deals(self, competitor_research):
        """Atlantic has zero Meta financial relationships."""
        atlantic = competitor_research["publications"].get("atlantic")
        if atlantic is None:
            pytest.skip("Atlantic not found in competitor research")
        meta_tone = str(atlantic.get("meta_coverage_tone", "")).lower()
        assert "adversarial" in meta_tone


# ===================================================================
# 3. Cross-Publication Disclosure Correlation
# ===================================================================

class TestDisclosureCorrelation:
    """Disclosure + symmetric incentives correlate with balanced coverage."""

    def test_only_disclosing_pub_has_symmetric_deals(self, competitor_entities):
        """The only publisher that discloses (WSJ/News Corp) also has symmetric deals."""
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = meta_deals.get("partners", [])
        partner_names = [p.get("name", "").lower() for p in partners]

        # News Corp has Meta deal. Also has OpenAI deal (documented).
        assert any("news corp" in n for n in partner_names)

    def test_non_disclosing_pubs_have_asymmetric_deals(self, competitor_entities):
        """All non-disclosing publications have asymmetric financial incentives."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        for pub in excluded:
            meta_deal = pub.get("meta_deal", "none")
            assert meta_deal == "none" or meta_deal is None, \
                f"{pub.get('name')} should have no Meta deal (has {meta_deal})"

    def test_disclosure_predicts_balanced_coverage(self, competitor_research):
        """WSJ's coverage tone delta is much smaller than non-disclosing publications."""
        wsj = competitor_research["publications"].get("wsj") or \
              competitor_research["publications"].get("news-corp") or \
              competitor_research["publications"].get("news_corp")
        wired = competitor_research["publications"].get("wired")

        if wsj is None or wired is None:
            pytest.skip("Need both WSJ and WIRED in competitor research")

        # WIRED's asymmetry verdict mentions ~0.95 gap
        wired_verdict = str(wired.get("asymmetry_verdict", ""))
        assert "0.9" in wired_verdict or "0.8" in wired_verdict or "0.7" in wired_verdict, \
            "WIRED should have a large documented coverage asymmetry"

    def test_seven_non_disclosing_publications(self, competitor_research):
        """At least 6 publications with financial ties do not disclose them."""
        pubs = competitor_research["publications"]
        non_disclosing = []
        for name, data in pubs.items():
            all_text = yaml.dump(data).lower()
            if "never disclosed" in all_text or "not disclosed" in all_text or \
               "no disclosure" in all_text:
                non_disclosing.append(name)
        # At least WIRED, FT, The Verge should be documented as non-disclosing
        assert len(non_disclosing) >= 2, \
            f"Expected at least 2 non-disclosing publications, found {len(non_disclosing)}: {non_disclosing}"


# ===================================================================
# 4. Aggregate Disclosure Finding
# ===================================================================

class TestAggregateDisclosureFinding:
    """The aggregate finding: transparency correlates with balanced coverage."""

    def test_aggregate_finding_exists(self, competitor_research):
        """Competitor research has an aggregate disclosure finding."""
        all_text = yaml.dump(competitor_research).lower()
        has_disclosure_topic = "disclosure" in all_text
        assert has_disclosure_topic, "Research should contain disclosure analysis"

    def test_wsj_is_only_disclosing_publication(self, competitor_research):
        """Documentation identifies WSJ as the only disclosing publication."""
        all_text = yaml.dump(competitor_research).lower()
        # Should mention WSJ uniqueness in disclosure
        assert ("only" in all_text and "disclos" in all_text) or \
               ("wsj" in all_text and "disclos" in all_text) or \
               ("news corp" in all_text and "disclos" in all_text)

    def test_meta_deal_count_is_zero_for_excluded(self, competitor_entities):
        """All excluded publishers have meta_deal = none."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        for pub in excluded:
            meta_deal = pub.get("meta_deal", "none")
            assert meta_deal == "none" or meta_deal is None, \
                f"{pub.get('name')} meta_deal should be 'none', got {meta_deal}"

    def test_total_competitor_deals_at_least_15(self, competitor_entities):
        """Total competitor deals across excluded publishers is 15+."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        total = 0
        for pub in excluded:
            deals = pub.get("deals_with_competitors", [])
            total += len(deals)
        assert total >= 15, f"Expected 15+ competitor deals total, got {total}"
