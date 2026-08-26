"""
WSJ Pre-IPO Aspirational Narrative Amplification vs Meta AI Spending Credibility Scrutiny
(August 2026)

Mechanism #317: WSJ Anthropic Pre-IPO TAM Aspirational Framing vs Meta Investment Interrogation

CORE FINDING:
During the same two-week window (Aug 11-26, 2026), the Wall Street Journal applies dramatically
different editorial standards to AI investment credibility for two companies:

  Anthropic: "blockbuster IPO," "$30 trillion potential revenue," "could top SpaceX,"
             "more than doubled its revenue," "cutting-edge AI models"
             → ASPIRATIONAL INVESTMENT NARRATIVE

  Meta:      "stumbles," "waited in vain," "erasing more than $140 billion," "eke out $784
             million - a precipitous drop," "just trust us," "mountain of lawsuits"
             → CREDIBILITY SCRUTINY / FAILURE NARRATIVE

The credibility-scrutiny asymmetry is the core mechanism. Meta has ~5.2x Anthropic's quarterly
revenue ($60.8B vs $11.6B), positive free cash flow ($784M vs unprofitable), and concrete
AI infrastructure serving 3.27B monthly users. Anthropic projects $190-200B in 2028 revenue
(~17x its current annualized run rate) and claims a $30T+ TAM exceeding US GDP (~$28T).

Yet WSJ frames Anthropic's projections aspirationally and Meta's actual spending with scrutiny.

ARTICLE 1 (Aug 25, 2026):
  "Anthropic Expected to Tell Investors It Sees Over $30 Trillion in Potential Revenue"
  By Corrie Driebusch
  URL: https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea

ARTICLE 2 (Aug 11, 2026):
  "Anthropic Tries to Shore Up Investor Confidence Ahead of Blockbuster IPO"
  By Berber Jin, Corrie Driebusch, Kate Clark
  URL: https://www.wsj.com/tech/ai/anthropic-tries-to-shore-up-investor-confidence-ahead-of-blockbuster-ipo-0ff736ad

ARTICLE 3 (Jul 30, 2026):
  "Meta Stumbles as Tech Investors Demand Better Answers on AI Spending"
  By Meghan Bobrowsky
  URL: https://www.wsj.com/tech/ai/meta-stumbles-as-tech-investors-demand-better-answers-on-ai-spending-fc731909

ARTICLE 4 (Jul 22, 2026):
  "The AI Backlash Is Starting to Sting"
  URL: https://www.wsj.com/tech/ai/the-ai-backlash-is-starting-to-sting-129a708d

FINANCIAL ARCHITECTURE:
  News Corp (WSJ parent):
    - OpenAI content licensing: $50M/yr ($250M/5yr, signed May 2024)
    - Meta AI content licensing: up to $50M/yr (signed Mar 2026)
    - Anthropic settlement revenue: share of $1.5B (approved Jun 2026)
    - Anthropic IPO success validates AI lab valuations, supporting OpenAI pre-IPO
      narrative and News Corp deal terms

CREDIBILITY SCRUTINY ASYMMETRY:
  Anthropic $30T TAM: exceeds US GDP, 17x revenue growth projected, minimal scrutiny (1 skeptical quote)
  Meta $130-145B capex: backed by $60.8B revenue and positive FCF, intensive scrutiny (5+ skeptical quotes)

Sources:
- https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea
- https://www.wsj.com/tech/ai/anthropic-tries-to-shore-up-investor-confidence-ahead-of-blockbuster-ipo-0ff736ad
- https://www.wsj.com/tech/ai/meta-stumbles-as-tech-investors-demand-better-answers-on-ai-spending-fc731909
- https://www.wsj.com/tech/ai/the-ai-backlash-is-starting-to-sting-129a708d
"""

import os
import subprocess
import unittest

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_DIR, "profiles")
CCR_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")


def grep_file(filepath, pattern):
    """Grep a file for a pattern and return matching lines."""
    try:
        result = subprocess.run(
            ["grep", "-n", pattern, filepath],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except Exception:
        return []


def grep_file_i(filepath, pattern):
    """Case-insensitive grep."""
    try:
        result = subprocess.run(
            ["grep", "-in", pattern, filepath],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except Exception:
        return []


def grep_count(filepath, pattern):
    """Count matches."""
    try:
        result = subprocess.run(
            ["grep", "-c", pattern, filepath],
            capture_output=True, text=True, timeout=5
        )
        return int(result.stdout.strip()) if result.stdout.strip() else 0
    except Exception:
        return 0


class TestMechanism317Exists(unittest.TestCase):
    """Verify mechanism #317 is documented in competitor-coverage-research.yaml."""

    def test_mechanism_317_id_present(self):
        """Mechanism ID 317 exists in the file."""
        matches = grep_file(CCR_FILE, "mechanism_id: 317")
        self.assertGreater(len(matches), 0, "mechanism_id: 317 not found in CCR")

    def test_mechanism_317_key_present(self):
        """Mechanism #317 key block exists."""
        matches = grep_file(CCR_FILE, "wsj_anthropic_pre_ipo_aspirational")
        self.assertGreater(len(matches), 0, "Mechanism #317 key not found")

    def test_mechanism_317_type(self):
        """Mechanism has correct type."""
        matches = grep_file(CCR_FILE, "pre_ipo_aspirational_narrative_investment_scrutiny_bifurcation")
        self.assertGreater(len(matches), 0, "Mechanism type not found")

    def test_mechanism_317_publication(self):
        """Mechanism identifies WSJ."""
        matches = grep_file(CCR_FILE, "Wall Street Journal")
        self.assertGreater(len(matches), 0, "WSJ not mentioned")


class TestAnthropicAspirationArticles(unittest.TestCase):
    """Verify the Anthropic aspirational articles are documented."""

    def test_anthropic_30t_tam_url(self):
        """Anthropic $30T TAM article URL is present."""
        matches = grep_file(CCR_FILE, "a611efea")
        self.assertGreater(len(matches), 0, "$30T TAM article URL not found")

    def test_anthropic_blockbuster_ipo_url(self):
        """Anthropic blockbuster IPO article URL is present."""
        matches = grep_file(CCR_FILE, "0ff736ad")
        self.assertGreater(len(matches), 0, "Blockbuster IPO article URL not found")

    def test_anthropic_vocabulary_blockbuster(self):
        """Aspirational vocabulary 'blockbuster' documented."""
        matches = grep_file_i(CCR_FILE, "blockbuster")
        # Should appear in mechanism #317 context
        self.assertGreater(len(matches), 0, "'blockbuster' vocabulary not documented")

    def test_anthropic_vocabulary_potential_revenue(self):
        """Aspirational vocabulary 'potential revenue' documented."""
        matches = grep_file_i(CCR_FILE, "potential revenue")
        self.assertGreater(len(matches), 0, "'potential revenue' vocabulary not documented")

    def test_anthropic_vocabulary_cutting_edge(self):
        """Aspirational vocabulary 'cutting-edge' documented."""
        matches = grep_file_i(CCR_FILE, "cutting-edge")
        self.assertGreater(len(matches), 0, "'cutting-edge' vocabulary not documented")

    def test_anthropic_vocabulary_doubled(self):
        """Aspirational vocabulary about revenue doubling documented."""
        matches = grep_file_i(CCR_FILE, "doubled")
        self.assertGreater(len(matches), 0, "'doubled' vocabulary not documented")


class TestMetaScrutinyArticles(unittest.TestCase):
    """Verify Meta scrutiny articles are documented."""

    def test_meta_stumbles_url(self):
        """Meta 'stumbles' article URL is present."""
        matches = grep_file(CCR_FILE, "fc731909")
        self.assertGreater(len(matches), 0, "Meta stumbles article URL not found")

    def test_meta_backlash_url(self):
        """AI backlash article URL is present."""
        matches = grep_file(CCR_FILE, "129a708d")
        self.assertGreater(len(matches), 0, "AI backlash article URL not found")

    def test_meta_vocabulary_stumbles(self):
        """Scrutiny vocabulary 'stumbles' documented."""
        matches = grep_file_i(CCR_FILE, "stumbles")
        self.assertGreater(len(matches), 0, "'stumbles' vocabulary not documented")

    def test_meta_vocabulary_precipitous(self):
        """Scrutiny vocabulary 'precipitous' documented."""
        matches = grep_file_i(CCR_FILE, "precipitous")
        self.assertGreater(len(matches), 0, "'precipitous' vocabulary not documented")

    def test_meta_vocabulary_erasing(self):
        """Scrutiny vocabulary about erasing market value documented."""
        matches = grep_file_i(CCR_FILE, "erasing")
        self.assertGreater(len(matches), 0, "'erasing' vocabulary not documented")

    def test_meta_vocabulary_just_trust_us(self):
        """Scrutiny framing 'just trust us' documented."""
        matches = grep_file_i(CCR_FILE, "just trust us")
        self.assertGreater(len(matches), 0, "'just trust us' vocabulary not documented")


class TestCredibilityScrutinyAsymmetry(unittest.TestCase):
    """Verify the core credibility scrutiny asymmetry is documented."""

    def test_anthropic_tam_value(self):
        """Anthropic TAM value ($30T+) documented."""
        matches = grep_file_i(CCR_FILE, "anthropic_tam")
        self.assertGreater(len(matches), 0, "Anthropic TAM not documented")

    def test_anthropic_quarterly_revenue(self):
        """Anthropic quarterly revenue ($11.6B) documented."""
        matches = grep_file(CCR_FILE, "anthropic_quarterly_revenue")
        self.assertGreater(len(matches), 0, "Anthropic quarterly revenue not documented")

    def test_meta_quarterly_revenue(self):
        """Meta quarterly revenue ($60.8B) documented."""
        matches = grep_file(CCR_FILE, "meta_quarterly_revenue")
        self.assertGreater(len(matches), 0, "Meta quarterly revenue not documented")

    def test_growth_multiple(self):
        """Anthropic projected growth multiple (~17x) documented."""
        matches = grep_file(CCR_FILE, "anthropic_projected_growth_multiple")
        self.assertGreater(len(matches), 0, "Growth multiple not documented")

    def test_tone_delta(self):
        """Tone delta documented."""
        # Within mechanism #317 context, tone_delta should exist
        matches = grep_file(CCR_FILE, "tone_delta: 0.75")
        self.assertGreater(len(matches), 0, "Tone delta 0.75 not documented")


class TestFinancialArchitecture(unittest.TestCase):
    """Verify the financial architecture is correctly documented."""

    def test_openai_deal_in_mechanism(self):
        """OpenAI deal referenced in mechanism."""
        matches = grep_file(CCR_FILE, "openai_deal")
        self.assertGreater(len(matches), 0, "OpenAI deal not referenced")

    def test_meta_deal_in_mechanism(self):
        """Meta deal referenced in mechanism."""
        matches = grep_file(CCR_FILE, "meta_deal")
        self.assertGreater(len(matches), 0, "Meta deal not referenced")

    def test_anthropic_settlement_in_mechanism(self):
        """Anthropic settlement referenced in mechanism."""
        matches = grep_file(CCR_FILE, "anthropic_settlement")
        self.assertGreater(len(matches), 0, "Anthropic settlement not referenced")

    def test_ipo_validation_incentives(self):
        """IPO validation incentive chain documented."""
        matches = grep_file(CCR_FILE, "ipo_validation_incentives")
        self.assertGreater(len(matches), 0, "IPO validation incentives not documented")

    def test_news_corp_profile_has_openai_deal(self):
        """News Corp profile includes OpenAI licensing deal."""
        matches = grep_file_i(NEWS_CORP_FILE, "openai")
        self.assertGreater(len(matches), 0, "OpenAI not in News Corp profile")

    def test_news_corp_profile_has_meta_deal(self):
        """News Corp profile includes Meta licensing deal."""
        matches = grep_file_i(NEWS_CORP_FILE, "meta.*licensing")
        self.assertGreater(len(matches), 0, "Meta licensing not in News Corp profile")


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented."""

    def test_has_confounders_section(self):
        """Mechanism has confounders documented."""
        matches = grep_file(CCR_FILE, "Beat assignment")
        self.assertGreater(len(matches), 0, "Beat assignment confounder not documented")

    def test_counter_confounding_documented(self):
        """Counter-confounding evidence documented."""
        matches = grep_file(CCR_FILE, "COUNTER-CONFOUNDING")
        self.assertGreater(len(matches), 0, "Counter-confounders not documented")

    def test_scrutiny_ratio_inversion(self):
        """Documents the inverted scrutiny-to-projection ratio."""
        matches = grep_file_i(CCR_FILE, "ratio of scrutiny")
        self.assertGreater(len(matches), 0, "Scrutiny ratio inversion not documented")

    def test_disclosure_asymmetry_documented(self):
        """Documents that Anthropic IPO articles lack financial disclosure."""
        matches = grep_file_i(CCR_FILE, "zero financial disclosure")
        self.assertGreater(len(matches), 0, "Disclosure asymmetry not documented")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    def test_references_mechanism_288(self):
        """Cross-references mechanism #288 (WSJ data practice vocabulary)."""
        # Check that mechanism_id: 288 appears near mechanism #317 context
        matches = grep_file(CCR_FILE, "mechanism_id: 288")
        self.assertGreater(len(matches), 0, "No reference to mechanism #288")

    def test_references_mechanism_72(self):
        """Cross-references mechanism #72."""
        matches = grep_file(CCR_FILE, "mechanism_id: 72")
        self.assertGreater(len(matches), 0, "No reference to mechanism #72")

    def test_references_mechanism_73(self):
        """Cross-references mechanism #73."""
        matches = grep_file(CCR_FILE, "mechanism_id: 73")
        self.assertGreater(len(matches), 0, "No reference to mechanism #73")


class TestSourceURLIntegrity(unittest.TestCase):
    """Verify all source URLs are present and properly formatted."""

    def test_has_wsj_source_urls(self):
        """Source URLs from wsj.com are present."""
        matches = grep_file(CCR_FILE, "wsj.com/tech/ai")
        self.assertGreater(len(matches), 5, "Insufficient WSJ source URLs")

    def test_all_four_articles_have_urls(self):
        """All four article URL slugs present."""
        slugs = ["a611efea", "0ff736ad", "fc731909", "129a708d"]
        for slug in slugs:
            matches = grep_file(CCR_FILE, slug)
            self.assertGreater(len(matches), 0, f"Article URL slug {slug} not found")

    def test_reporter_names_documented(self):
        """Reporter names are documented."""
        reporters = ["Corrie Driebusch", "Meghan Bobrowsky", "Berber Jin"]
        for reporter in reporters:
            matches = grep_file(CCR_FILE, reporter)
            self.assertGreater(len(matches), 0, f"Reporter {reporter} not documented")


if __name__ == "__main__":
    unittest.main()
