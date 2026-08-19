"""
Mechanism #174: OpenAI Zero-Ad-Revenue-Share Publisher Financial Captivity Architecture

Discovery: OpenAI's VP of Media Partnerships Varun Shetty confirmed at the WAN-IFRA
World News Media Congress (Marseille, Jun 3 2026) that OpenAI has "no plans" to share
advertising revenue with publishers whose content is surfaced next to ChatGPT ads.

This creates a one-directional financial captivity architecture:

1. Publishers license content to OpenAI for FLAT fees ($300-400M/yr total, 20+ deals)
2. OpenAI uses that content in ChatGPT Search, displayed alongside ads
3. OpenAI keeps 100% of ad revenue (projected $2.5B 2026, $100B by 2030)
4. Publishers get: flat licensing + "referral traffic" + vague subscription lift promises
5. Zero contractual share of the ad revenue their content generates

Industry Comparison — Revenue Share Models:
  Google AdSense: 68-80% to publishers (updated 2024 to 80% sell-side)
  Perplexity: Initially offered per-citation rev share, then removed ads entirely
  Prorata AI: 50% ad revenue share with cited publishers
  Microsoft Copilot: Announced plans to pay publishers for cited content
  Meta (Instant Articles): Revenue sharing (program discontinued)
  OpenAI: 0% — confirmed by VP Media Partnerships, Jun 3 2026

Career Capture — Varun Shetty:
  - NYU School of Law (J.D.) → Skadden Arps (antitrust litigation) →
    Wilson Sonsini (antitrust) → Foursquare → Shyp → New York Times
    (Executive Director Strategy & BD, managed Google/Snapchat partnerships,
    led VR business) → Meta (6+ years: Director Product Marketing for Media
    Partners, then Director BD & Product Partnerships for WhatsApp) →
    OpenAI (VP Media Partnerships, Jan 2024-present)
  - Former antitrust lawyer who now runs the media partnerships program
  - Led WhatsApp partnerships at Meta before moving to OpenAI
  - At NYT, managed partnerships with Google and Snapchat

WAN-IFRA Dependency Programs:
  - "Newsroom AI Catalyst" — $1.5M co-funded by OpenAI, 128 newsrooms
  - "Prototype Development Fund" — $1.5M total ($750K top performers)
  - "OpenAI Academy for News" — case studies embedding OpenAI tools in workflows
  These programs create switching costs: newsrooms that build workflows around
  OpenAI tools face migration costs if they leave the ecosystem.

Financial Captivity Chain:
  Publisher signs content deal → Receives flat fee ($5-50M/yr each) →
  Content used in ChatGPT Search with ads → OpenAI keeps 100% ad revenue →
  Publisher also receives OpenAI newsroom grants/tools →
  Publisher editorial judgment on OpenAI becomes financially conflicted →
  Adversarial coverage risks: losing licensing deal + newsroom AI grants +
  referral traffic + being labeled as a holdout (NYT model)

Contrast with Meta:
  Meta has ZERO content licensing deals with adversarial publications
  (WIRED, Gizmodo, NYT, Verge). No newsroom dependency programs.
  No financial leverage. Cost of adversarial Meta coverage = $0.
  This is why financial relationships predict coverage tone.

Source URLs:
  - Press Gazette: https://pressgazette.co.uk/platforms/openai-not-planning-to-share-advertising-revenue-with-publishers/
  - RightsTech: https://rightstech.com/2026/06/openai-not-planning-to-share-advertising-revenue-with-publishers/
  - Search Engine Land: https://searchengineland.com/openai-searchgpt-chatgpt-integration-447379
  - Twipe: https://www.twipemobile.com/openai-shares-ai-strategies-for-publishers/
  - Pulse: https://www.pulse.bot/entertainment/news/openai-not-planning-to-share-advertising-revenue-with-publishers-9d05c358-0f4b-465f-8ee5-b27c3bd3461c/
  - The Org (Shetty career): https://Theorg.com/org/openai/org-chart/varun-shetty
  - RocketReach (Shetty career): https://rocketreach.co/varun-shetty-email_5632603
  - Digiday coupon phase: https://digiday.com/marketing/openais-chatgpt-reaches-the-coupon-stage-of-building-an-ad-business/
  - AdWeek 90% miss: https://www.adweek.com/media/openais-ad-business-is-on-pace-to-miss-its-own-forecast-by-90-analyst-says/
  - Google AdSense rev share: https://support.google.com/adsense/answer/180195?hl=en
  - WAN-IFRA Newsroom AI Catalyst: https://wan-ifra.org/newsroom-ai-catalyst-prototype-development-fund/
  - OpenAI Newsroom AI Catalyst: http://openai.com/index/newsroom-ai-catalyst-global-program-with-wan-ifra/

Confounders: 5 documented (2 STRONG, 2 MODERATE, 1 WEAK)
Asymmetry Score: 0.82
Cross-references: #172 (OpenAI CPA ad maturation), #162 (Advance Reddit),
  #40 (FT-OpenAI deal), #43 (Condé Nast-OpenAI deal)
"""

import unittest
import yaml
import os


YAML_PATH = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')


def _load_yaml():
    with open(YAML_PATH, 'r') as f:
        return yaml.safe_load(f)


def _get_cpf():
    data = _load_yaml()
    return data.get('cross_publication_findings', {})


def _get_mechanism_174():
    cpf = _get_cpf()
    for v in cpf.values():
        if isinstance(v, dict) and v.get('mechanism_id') == 174:
            return v
    return None


class TestMechanism174Exists(unittest.TestCase):
    """Verify mechanism #174 is registered in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.cpf = _get_cpf()
        cls.mechanism = _get_mechanism_174()

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #174 must exist in cross_publication_findings")

    def test_has_asymmetry_score(self):
        self.assertIsNotNone(self.mechanism)
        self.assertIn('asymmetry_score', self.mechanism)
        self.assertGreaterEqual(self.mechanism['asymmetry_score'], 0.7)

    def test_has_finding(self):
        self.assertIsNotNone(self.mechanism)
        finding = self.mechanism.get('finding', '')
        self.assertIn('revenue', finding.lower())

    def test_has_source_urls(self):
        self.assertIsNotNone(self.mechanism)
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3)


class TestZeroAdRevenueShareConfirmation(unittest.TestCase):
    """Validate the zero ad revenue share confirmation is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_shetty_confirmation_documented(self):
        """VP of Media Partnerships confirmed no ad revenue sharing."""
        self.assertIsNotNone(self.mechanism)
        finding = str(self.mechanism.get('finding', '')) + str(self.mechanism.get('evidence', ''))
        self.assertTrue(
            'shetty' in finding.lower() or 'varun' in finding.lower(),
            "Mechanism must document Varun Shetty's confirmation"
        )

    def test_wan_ifra_congress_cited(self):
        """WAN-IFRA World News Media Congress as venue."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism)
        self.assertTrue(
            'wan-ifra' in text.lower() or 'wan_ifra' in text.lower() or 'marseille' in text.lower(),
            "Must cite WAN-IFRA Congress or Marseille as venue"
        )

    def test_zero_percent_documented(self):
        """Zero percent revenue share clearly stated."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            '0%' in text or 'zero' in text or 'not at this point' in text,
            "Must clearly state zero/0% ad revenue share"
        )

    def test_confirmation_date(self):
        """Confirmation date of June 3, 2026."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism)
        self.assertTrue(
            'june 2026' in text.lower() or 'jun 2026' in text.lower()
            or '2026-06' in text or 'june 3' in text.lower(),
            "Must cite June 2026 as confirmation date"
        )


class TestRevenueShareComparisonFramework(unittest.TestCase):
    """Validate the cross-platform revenue share comparison is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_google_adsense_comparison(self):
        """Google AdSense 68-80% revenue share as baseline comparison."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'adsense' in text or 'google' in text,
            "Must compare with Google AdSense revenue share"
        )
        self.assertTrue(
            '68%' in str(self.mechanism) or '80%' in str(self.mechanism),
            "Must cite Google's 68% or 80% publisher revenue share"
        )

    def test_perplexity_comparison(self):
        """Perplexity initially offered rev share, then removed ads."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'perplexity' in text,
            "Must compare with Perplexity's revenue share model"
        )

    def test_prorata_comparison(self):
        """Prorata AI offered 50% ad revenue share."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'prorata' in text or '50%' in str(self.mechanism),
            "Must compare with Prorata AI's 50% revenue share"
        )

    def test_meta_zero_deal_contrast(self):
        """Meta has zero content licensing deals with adversarial publications."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'meta' in text,
            "Must contrast with Meta's zero-deal position"
        )


class TestShettyCareerCapture(unittest.TestCase):
    """Validate Varun Shetty's career trajectory is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_meta_whatsapp_background(self):
        """Shetty's Meta/WhatsApp partnership background."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'meta' in text and ('whatsapp' in text or 'product' in text),
            "Must document Shetty's Meta background"
        )

    def test_nyt_background(self):
        """Shetty's New York Times strategy role."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'new york times' in text or 'nyt' in text or 'times' in text,
            "Must document Shetty's NYT background"
        )

    def test_antitrust_law_background(self):
        """Shetty's antitrust legal background."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'antitrust' in text or 'law' in text or 'skadden' in text,
            "Must document Shetty's antitrust law background"
        )

    def test_career_trajectory_length(self):
        """Career spans 7+ positions across law, media, tech."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        career_markers = sum(1 for term in ['skadden', 'wilson sonsini', 'foursquare',
                                            'new york times', 'meta', 'openai', 'nyu']
                           if term in text)
        self.assertGreaterEqual(career_markers, 3,
                               "Must document at least 3 career stops")


class TestWanIfraNewroomDependencyPrograms(unittest.TestCase):
    """Validate WAN-IFRA/OpenAI newsroom dependency programs documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_newsroom_ai_catalyst_documented(self):
        """Newsroom AI Catalyst program ($1.5M, 128 newsrooms)."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'catalyst' in text or 'newsroom' in text,
            "Must document Newsroom AI Catalyst program"
        )

    def test_prototype_development_fund(self):
        """Prototype Development Fund ($1.5M total)."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'prototype' in text or 'fund' in text or 'grant' in text,
            "Must document Prototype Development Fund"
        )

    def test_switching_cost_analysis(self):
        """Switching costs from embedded OpenAI tools."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'switching' in text or 'dependency' in text or 'embed' in text or 'workflow' in text,
            "Must analyze switching cost / dependency creation"
        )

    def test_program_count(self):
        """At least 2 dependency programs documented."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        program_markers = sum(1 for term in ['catalyst', 'prototype', 'academy',
                                             'fund', 'grant']
                            if term in text)
        self.assertGreaterEqual(program_markers, 2,
                               "Must document at least 2 newsroom dependency programs")


class TestFinancialCaptivityChain(unittest.TestCase):
    """Validate the financial captivity chain logic is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_flat_fee_vs_ad_revenue_ratio(self):
        """Flat licensing fees vs. ad revenue ratio documented."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism)
        self.assertTrue(
            '300' in text or '400' in text or 'flat' in text.lower(),
            "Must document flat licensing fee total ($300-400M)"
        )

    def test_ad_revenue_projection(self):
        """OpenAI ad revenue projections ($2.5B 2026, $100B 2030)."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism)
        self.assertTrue(
            '2.5' in text or '100' in text,
            "Must document OpenAI ad revenue projections"
        )

    def test_content_deal_materiality_ratio(self):
        """Content deals become <0.4% of ad revenue by 2030 projection."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            '0.4%' in str(self.mechanism) or 'rounding error' in text or 'material' in text
            or 'diminish' in text or 'fraction' in text,
            "Must analyze content deal materiality vs. ad revenue"
        )

    def test_coverage_incentive_directionality(self):
        """Softer coverage incentivized for deal-holders, harder for non-deal entities."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'incentiv' in text or 'softer' in text or 'adversarial' in text,
            "Must analyze coverage incentive directionality"
        )


class TestConfoundingFactors(unittest.TestCase):
    """Validate confounding factors are documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_confounders_present(self):
        self.assertIsNotNone(self.mechanism)
        confounders = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(confounders), 3)

    def test_at_least_one_strong_confounder(self):
        self.assertIsNotNone(self.mechanism)
        confounders = self.mechanism.get('confounding_factors', [])
        severities = [c.get('severity', '').upper() for c in confounders if isinstance(c, dict)]
        self.assertIn('STRONG', severities, "Must have at least one STRONG confounder")

    def test_emarketer_counter_forecast_acknowledged(self):
        """eMarketer counter-forecast (90% miss) as confounder."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'emarketer' in text or '90%' in str(self.mechanism) or 'counter' in text,
            "Must acknowledge eMarketer's counter-forecast as confounder"
        )


class TestSourceUrlVerification(unittest.TestCase):
    """Validate source URLs are present and cover key claims."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_press_gazette_source(self):
        """Press Gazette primary source for Shetty confirmation."""
        self.assertIsNotNone(self.mechanism)
        urls = str(self.mechanism.get('source_urls', []))
        self.assertTrue('pressgazette' in urls, "Must cite Press Gazette source")

    def test_google_adsense_source(self):
        """Google AdSense official documentation."""
        self.assertIsNotNone(self.mechanism)
        urls = str(self.mechanism.get('source_urls', []))
        self.assertTrue(
            'google' in urls.lower() or 'adsense' in urls.lower(),
            "Must cite Google AdSense revenue share documentation"
        )

    def test_minimum_source_count(self):
        """At least 6 source URLs."""
        self.assertIsNotNone(self.mechanism)
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 6, "Must have at least 6 source URLs")

    def test_wan_ifra_source(self):
        """WAN-IFRA or OpenAI newsroom catalyst source."""
        self.assertIsNotNone(self.mechanism)
        urls = str(self.mechanism.get('source_urls', []))
        self.assertTrue(
            'wan-ifra' in urls.lower() or 'openai' in urls.lower(),
            "Must cite WAN-IFRA or OpenAI newsroom program source"
        )


class TestCrossReferences(unittest.TestCase):
    """Validate cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_cross_refs_present(self):
        self.assertIsNotNone(self.mechanism)
        cross_refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(cross_refs), 2)

    def test_mechanism_172_referenced(self):
        """Cross-ref to #172 (OpenAI CPA ad maturation)."""
        self.assertIsNotNone(self.mechanism)
        cross_refs = self.mechanism.get('cross_references', [])
        ref_ids = [c.get('mechanism_id', c) if isinstance(c, dict) else c
                   for c in cross_refs]
        self.assertIn(172, ref_ids, "Must cross-reference mechanism #172")


class TestLitigationSplitDocumented(unittest.TestCase):
    """Validate the deal vs. litigation split creates a two-tier system."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_174()

    def test_nyt_litigation_contrast(self):
        """NYT suing vs. deal-holders creates two-tier coverage incentive."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        self.assertTrue(
            'litigation' in text or 'suing' in text or 'lawsuit' in text
            or 'new york times' in text or 'copyright' in text,
            "Must document NYT litigation vs. deal-holder contrast"
        )

    def test_deal_holder_list(self):
        """Key deal holders documented."""
        self.assertIsNotNone(self.mechanism)
        text = str(self.mechanism).lower()
        deal_markers = sum(1 for term in ['condé nast', 'conde nast', 'financial times',
                                          'washington post', 'guardian', 'news corp',
                                          'vox media', 'atlantic', 'hearst']
                         if term in text)
        self.assertGreaterEqual(deal_markers, 3,
                               "Must list at least 3 major deal holders")


if __name__ == '__main__':
    unittest.main()
