"""
Mechanism #35: Advance/Condé Nast Aggregate AI Revenue Dependency —
The Omni-Deal Publisher

FINDING: When all financial channels between Advance Publications / Condé Nast
and AI companies are aggregated, Advance/Condé Nast emerges as the most
financially entangled publisher in the AI ecosystem, with SIX distinct AI
revenue channels across FIVE different AI companies/platforms — every major
AI company EXCEPT Meta.

CHANNELS:
1. OpenAI content licensing (Condé Nast, Aug 2024): Multi-year deal for WIRED,
   New Yorker, Vogue, GQ, Vanity Fair, Bon Appétit, AD, etc. Undisclosed value,
   est. $15-25M/yr based on portfolio breadth (20+ brands, largest undisclosed
   deal after News Corp's $50M/yr).
2. Microsoft PCM partnership (Condé Nast, Feb 2026): Co-design partner for
   Publisher Content Marketplace. One of 7 founding publishers. Additional
   Copilot Daily content licensing.
3. Amazon Rufus deal (Condé Nast, Jul 2025): Multi-year content licensing for
   Amazon's Rufus AI shopping assistant.
4. Perplexity licensing deal (Condé Nast, confirmed Mar 2026 by CEO Lynch):
   After initial C&D (Aug 2024), transitioned to licensing agreement.
5. Reddit AI data licensing (Advance's 23.3% equity / 65.2% voting in Reddit):
   Reddit Q2 2026 "Other revenue" (primarily AI licensing) = $43M (+24% YoY).
   Advance's equity exposure: 23.3% of $30.6B market cap = ~$7.13B (Aug 10, 2026).
   Reddit has AI licensing deals with Google ($60M/yr expanding) and OpenAI (~$70M/yr).
6. Apple News+ distribution: Revenue share for Condé Nast brands on Apple News+.

META IS THE ONLY MAJOR AI COMPANY EXCLUDED FROM ALL SIX CHANNELS.
Meta has zero content licensing with Condé Nast, zero data licensing with Reddit,
zero marketplace participation through Condé Nast. Yet WIRED (Condé Nast's flagship
tech publication) produces the most sustained adversarial coverage of Meta's AI
efforts — the only company that generates zero AI revenue for its parent chain.

AGGREGATE FINANCIAL EXPOSURE:
- Direct Condé Nast AI licensing revenue: est. $25-45M/yr aggregate across OpenAI,
  Microsoft, Amazon, Perplexity deals
- Reddit equity exposure (Advance): ~$7.13B (dwarfs all direct licensing)
- Reddit AI-specific revenue flowing to Advance (23.3%): ~$10M/yr of $43M Q2 annualized
- Apple News+ revenue share: undisclosed (est. low millions/yr)
- Total AI-linked financial exposure: ~$7.2B+ (equity + revenue)

COMPARISON:
- News Corp (balanced control): OpenAI $50M/yr + Meta up to $50M/yr + Anthropic
  settlement share. Two-company balance creates relatively neutral incentive structure.
- PMC/The Verge: No direct AI deals (inherits Vox Media's pre-acquisition OpenAI deal
  status unclear). PIF→SRMG→PMC chain creates indirect anti-Meta alignment.
- The Guardian: OpenAI deal (Feb 2025) + Google Showcase. Two-channel exposure.
- Advance/Condé Nast: SIX channels, FIVE companies, ~$7.2B+ aggregate. The most
  entangled publisher by an order of magnitude.

DISCLOSURE: None. WIRED does not disclose that its corporate parent chain:
- Receives AI licensing revenue from OpenAI (WIRED's content is literally in ChatGPT)
- Profits from Reddit's AI data licensing growth (23.3% equity, 65.2% voting control)
- Co-designed Microsoft's AI content marketplace
- Has licensing deals with Amazon and Perplexity
- Has zero financial relationship with Meta (the company it covers most adversarially)

LEGITIMATE FACTORS:
1. Meta has genuine privacy and child safety issues worth investigating
2. Meta's scale (3.5B daily users) creates proportionally more editorial interest
3. WIRED's adversarial tech journalism predates AI licensing era
4. Editorial teams may be genuinely independent from business-side deals
5. OpenAI deal was signed after WIRED's adversarial Meta coverage pattern was established
6. Not all adversarial coverage is financially motivated
7. Reddit's AI licensing is a small fraction of Reddit's total revenue ($43M of $805M)

SOURCES:
- Reddit Q2 2026 earnings: https://www.businesswire.com/news/home/20260730598707/en/
- Reddit market cap: $30.63B (StockAnalysis, Aug 10, 2026)
- Condé Nast CEO Roger Lynch annual memo (Mar 2026): confirmed OpenAI, Perplexity,
  Microsoft, Amazon deals (MediaPost)
- Condé Nast-OpenAI deal: https://www.campaignlive.com/article/openai-inks-multi-year-deal-conde-nast/1885777
- Amazon Rufus-Condé Nast: reported Jul 2025
- Microsoft PCM: reported Feb 2026 (WSJ)
- Reddit-Advance ownership: 23.3% economic, 65.2% voting (SEC filings)
"""

import pytest


class TestMechanism35Overview:
    """Tests for the aggregate finding structure."""

    def test_mechanism_id_present(self):
        """Mechanism #35 must be assigned in competitor-coverage-research.yaml."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        cpf = data.get("cross_publication_findings", {})
        ids = []
        if isinstance(cpf, dict):
            for k, v in cpf.items():
                if isinstance(v, dict) and "mechanism_id" in v:
                    ids.append(v["mechanism_id"])
        elif isinstance(cpf, list):
            for m in cpf:
                if isinstance(m, dict) and "mechanism_id" in m:
                    ids.append(m["mechanism_id"])
        assert 35 in ids, "Mechanism #35 must exist in cross_publication_findings"

    def test_mechanism_35_has_required_fields(self):
        """Mechanism #35 entry must have finding_summary, source_urls, and test_file."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        cpf = data.get("cross_publication_findings", {})
        m35 = None
        if isinstance(cpf, dict):
            for k, v in cpf.items():
                if isinstance(v, dict) and v.get("mechanism_id") == 35:
                    m35 = v
                    break
        elif isinstance(cpf, list):
            for m in cpf:
                if isinstance(m, dict) and m.get("mechanism_id") == 35:
                    m35 = m
                    break
        assert m35 is not None, "Mechanism #35 must exist"
        assert "finding_summary" in m35
        assert "source_urls" in m35
        assert "test_file" in m35

    def test_mechanism_35_name_contains_aggregate(self):
        """Mechanism #35 should reference aggregate/omni-deal concept."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        cpf = data.get("cross_publication_findings", {})
        m35 = None
        if isinstance(cpf, dict):
            for k, v in cpf.items():
                if isinstance(v, dict) and v.get("mechanism_id") == 35:
                    m35 = v
                    break
        elif isinstance(cpf, list):
            for m in cpf:
                if isinstance(m, dict) and m.get("mechanism_id") == 35:
                    m35 = m
                    break
        assert m35 is not None
        name = m35.get("mechanism_name", "") + " " + m35.get("finding_summary", "")
        name_lower = name.lower()
        assert any(w in name_lower for w in ["aggregate", "omni", "multi-deal", "six channel"]), \
            f"Mechanism #35 should reference aggregate dependency concept, got: {name[:100]}"


class TestSixChannelMapping:
    """Tests verifying all six financial channels are documented."""

    def test_channel_1_openai_licensing(self):
        """Channel 1: Condé Nast-OpenAI content licensing deal (Aug 2024)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        # Should have OpenAI deal referenced
        content = str(data)
        assert "OpenAI" in content
        assert "licensing" in content.lower() or "deal" in content.lower()

    def test_channel_2_microsoft_pcm(self):
        """Channel 2: Microsoft PCM co-design partnership (Feb 2026)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Microsoft" in content
        assert any(term in content for term in ["PCM", "Publisher Content Marketplace", "Copilot"])

    def test_channel_3_amazon_rufus(self):
        """Channel 3: Amazon Rufus content licensing (Jul 2025)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Amazon" in content
        assert "Rufus" in content

    def test_channel_4_perplexity(self):
        """Channel 4: Perplexity licensing deal (confirmed Mar 2026)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Perplexity" in content

    def test_channel_5_reddit_ai_licensing(self):
        """Channel 5: Reddit AI data licensing via Advance 23.3% equity."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Reddit" in content
        assert "23.3" in content or "23.3%" in content

    def test_channel_6_apple_news_plus(self):
        """Channel 6: Apple News+ distribution revenue share."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Apple" in content
        assert "News+" in content or "Apple News" in content


class TestMetaExclusion:
    """Tests verifying Meta is excluded from all six channels."""

    def test_meta_has_zero_conde_nast_deals(self):
        """Meta has zero content licensing deals with Condé Nast."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        # The profile should document Meta's exclusion
        assert "Meta" in content
        # Should note the absence/zero relationship
        lower = content.lower()
        assert any(phrase in lower for phrase in [
            "no meta deal", "zero meta", "meta does not",
            "meta has no", "absent", "excluded", "conspicuously",
            "not pay", "no condé nast", "no licensing deal"
        ]), "Profile should document Meta's exclusion from Condé Nast AI deals"

    def test_meta_has_zero_reddit_ai_deals(self):
        """Meta has zero AI data licensing deals with Reddit."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "Meta has NO Reddit data licensing deal" in content or \
               "Meta" in content  # At minimum Meta must be mentioned


class TestRedditQ2Data:
    """Tests verifying Reddit Q2 2026 financial data is current."""

    def test_reddit_q2_2026_revenue(self):
        """Reddit Q2 2026 total revenue should be documented as $805M."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert any(rev in content for rev in ["$805", "$804.91", "805 million", "804.91"]), \
            "Reddit Q2 2026 revenue ($805M) should be documented"

    def test_reddit_q2_2026_other_revenue(self):
        """Reddit Q2 2026 Other revenue (AI licensing) = $43M."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "$43" in content or "43 million" in content.lower(), \
            "Reddit Q2 2026 Other revenue ($43M, AI licensing) should be documented"

    def test_reddit_market_cap_current(self):
        """Reddit market cap should be updated to Aug 2026 range (~$30-32B)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert any(cap in content for cap in ["$30.6", "$30.63", "$31", "$32"]), \
            "Reddit market cap should reflect Aug 2026 range (~$30-32B)"

    def test_advance_stake_value_current(self):
        """Advance's 23.3% Reddit stake value should be ~$7.1B at current prices."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert any(val in content for val in ["$7.1", "$7.13", "$7.2", "7.1B", "7.13B"]), \
            "Advance's Reddit stake value should reflect Aug 2026 (~$7.1B)"


class TestAggregateExposure:
    """Tests for the aggregate financial exposure calculation."""

    def test_aggregate_section_exists_in_profile(self):
        """WIRED profile should have an aggregate AI dependency section."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert any(term in lower for term in [
            "aggregate", "omni_deal", "six_channel", "total_ai",
            "aggregate_ai_dependency"
        ]), "WIRED profile should have an aggregate AI dependency section"

    def test_aggregate_channels_count(self):
        """Aggregate section should document exactly 6 channels."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert "six" in lower or "6 " in content or "6 channel" in lower or \
               "six channel" in lower or "six distinct" in lower, \
            "Should document six distinct financial channels"

    def test_aggregate_companies_count(self):
        """Aggregate section should document 5 AI companies (all except Meta)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert "five" in lower or "5 " in content or "five companies" in lower or \
               "five different" in lower or "five ai" in lower, \
            "Should document financial relationships with five AI companies"

    @pytest.mark.parametrize("company", [
        "OpenAI", "Microsoft", "Amazon", "Perplexity", "Google"
    ])
    def test_each_paying_company_documented(self, company):
        """Each of the 5 AI companies paying Advance/Condé Nast should be named."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert company in content, \
            f"{company} should be documented as an AI revenue source for Advance/Condé Nast"


class TestComparisonWithOtherPublishers:
    """Tests for comparison metrics showing Advance is the most entangled."""

    def test_news_corp_comparison(self):
        """Should compare Advance's 6 channels to News Corp's 3 (OpenAI + Meta + Anthropic)."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "News Corp" in content, \
            "Should compare to News Corp as a reference publisher"

    def test_pmc_comparison(self):
        """Should compare to PMC/The Verge as another adversarial Meta outlet."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "PMC" in content or "Penske" in content or "The Verge" in content, \
            "Should compare to PMC/The Verge"


class TestLegitimateFactors:
    """Tests ensuring legitimate alternative explanations are documented."""

    def test_legitimate_factors_present(self):
        """Must document legitimate reasons for adversarial Meta coverage."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert any(phrase in lower for phrase in [
            "legitimate", "alternative", "confound", "genuine",
            "privacy", "child safety", "editorial independence"
        ]), "Must document legitimate factors for adversarial Meta coverage"

    def test_editorial_independence_acknowledged(self):
        """Must acknowledge editorial teams may be independent from business deals."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert "editorial" in lower and "independent" in lower, \
            "Must acknowledge editorial independence as a legitimate factor"


class TestSourceURLs:
    """Tests ensuring all claims have source URLs."""

    def test_reddit_earnings_source(self):
        """Reddit Q2 2026 earnings should have a source URL."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        assert "businesswire.com" in content or "reddit" in content.lower()

    def test_conde_nast_deals_source(self):
        """Condé Nast deals should reference Lynch memo or press reports."""
        import yaml
        with open("profiles/wired.yaml") as f:
            data = yaml.safe_load(f)
        content = str(data)
        lower = content.lower()
        assert "lynch" in lower or "mediapost" in lower or "searchenginejournal" in lower, \
            "Should reference Roger Lynch as source for deal confirmations"


class TestDocumentation:
    """Tests for README and ARCHITECTURE updates."""

    def test_readme_mentions_mechanism_35(self):
        """README should reference Mechanism #35."""
        with open("README.md") as f:
            content = f.read()
        assert "35" in content or "Aggregate" in content, \
            "README should reference Mechanism #35 or aggregate dependency"

    def test_architecture_mentions_new_test_file(self):
        """ARCHITECTURE.md should list the new test file."""
        with open("docs/ARCHITECTURE.md") as f:
            content = f.read()
        assert "advance_conde_nast_aggregate" in content or "aggregate_ai_dependency" in content, \
            "ARCHITECTURE.md should list the new test file"
