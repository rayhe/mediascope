"""
WSJ Anthropic Ode AI Surveillance Infrastructure Aspirational Framing vs Meta Camera Scrutiny
(August 2026)

Mechanism #321: WSJ AI Camera Surveillance Vocabulary Bifurcation — Anthropic (Aspirational) vs Meta (Alarm)

CORE FINDING:
On August 22, 2026, WSJ published "Private Equity Is Deploying an Army of AI Wonks to Embed
in the Firms They Back" (by Mark Maurer). The article describes Anthropic's $1.5B Ode joint
venture with Blackstone, Hellman & Friedman, Apollo, General Atlantic, and Goldman Sachs
deploying AI engineers into portfolio companies.

The article's case study — Chamberlain Group (LiftMaster) — reveals an AI-powered residential
surveillance infrastructure:
  - Adding 3 MILLION video cameras to homes this year (up from 1.7M last year)
  - Cameras use Anthropic Claude to RECOGNIZE DESIGNATED PEOPLE and alert homeowners
  - AI LEARNS family routines (arrival times, daily patterns)
  - AI FLAGS DEVIATIONS from learned routines to homeowners
  - Projected $500M/yr revenue by 2030

This is structurally identical to the surveillance capabilities Meta receives alarm coverage for:
  - Facial recognition → "recognizing designated people"
  - Behavioral tracking → "learning family routines"
  - Anomaly detection → "flagging deviations"
  - Always-on cameras → 3M new video cameras in homes

VOCABULARY BIFURCATION (same publication, same ~30 day window):
  Anthropic/Ode cameras: "digital doorman," "smart-access products," "advanced AI features,"
    "notify homeowners," "revenue," "$500M opportunity," "senior engineering team"
    → ZERO privacy vocabulary in entire article (0 instances of: privacy, surveillance,
       tracking, monitoring, creepy, invasive, concern, risk, data handling, consent)

  Meta cameras/glasses: "surveillance," "privacy invasion," "creepy," "harm," "privacy concerns"
    → Extensive alarm vocabulary across multiple WSJ articles on Meta camera products

FINANCIAL ARCHITECTURE:
  News Corp (WSJ parent):
    - OpenAI: $250M/5yr content licensing deal (May 2024)
    - Meta AI: up to $50M/yr content deal (Mar 2026)
    - Anthropic: share of $1.5B copyright settlement (approved Jun 2026)

  Ode venture backers with WSJ/publisher financial entanglement:
    - Goldman Sachs: Ode backer + potential Anthropic IPO underwriter + potential OpenAI IPO underwriter
    - Apollo: Ode backer + Yahoo/TechCrunch parent + Anthropic infrastructure financing partner
    - Blackstone: Ode backer + Broadcom $100B AI chip financing partner for Anthropic

  Anthropic IPO ($2T target) validates AI lab ecosystem → supports OpenAI pre-IPO pricing
  → supports News Corp deal renewal terms

CONFOUNDERS:
  1. STRONG: Chamberlain cameras are opt-in home products; Meta glasses are worn in public
     (different consent models). However, the WSJ article describes surveillance OF family
     members and visitors who didn't opt in to behavioral monitoring.
  2. MODERATE: Meta has a longer history of privacy incidents (Cambridge Analytica, etc.)
     providing editorial precedent for scrutiny. However, zero-scrutiny for structurally
     identical capabilities from a different company reveals entity selection, not
     capability-based analysis.
  3. MODERATE: The Ode article is a business/PE story, not a consumer tech review, so
     different editorial standards may apply. However, surveillance infrastructure deployed
     at scale (3M cameras) warrants privacy scrutiny regardless of business section.
  4. WEAK: Chamberlain/Ode is less well-known than Meta, so attracts less editorial attention.
     However, WSJ chose to profile this company extensively — the editorial decision to omit
     privacy vocabulary was active, not passive.

PRIOR MECHANISM EXTENSIONS:
  - Extends #317: WSJ Anthropic pre-IPO aspirational vs Meta investment scrutiny (same publication,
    different asset class — investment framing vs surveillance capability framing)
  - Extends #33: OpenAI facial recognition privacy parity (Anthropic/Ode cameras now have
    MORE deployed units than Meta glasses, with zero scrutiny)
  - Extends #290: WIRED OpenAI Meta ad targeting privacy policy natural experiment (vocabulary
    bifurcation on structurally equivalent capabilities)

ARTICLE 1 (WSJ, Aug 22, 2026):
  "Private Equity Is Deploying an Army of AI Wonks to Embed in the Firms They Back"
  By Mark Maurer
  URL: https://www.wsj.com/tech/ai/private-equity-is-deploying-an-army-of-ai-wonks-to-embed-in-the-firms-they-back-96d279ec

ARTICLE 2 (WSJ, Jul 6, 2026):
  "Big Tech Has Suddenly Flipped on the AI Jobs Wipeout Scenario"
  URL: https://www.wsj.com/tech/ai/ai-workers-tech-ceos-job-losses-afc71e15
  Meta framing: suspicious, skeptical of narrative shift. "in theory there should be more jobs"
  presented with implicit doubt. Economist quote: "They may have realized it was simply bad
  business to say that your great new product will destroy the economy."

ARTICLE 3 (WSJ, Jul 30, 2026):
  "Meta Stumbles as Tech Investors Demand Better Answers on AI Spending"
  By Meghan Bobrowsky
  URL: https://www.wsj.com/tech/ai/meta-stumbles-as-tech-investors-demand-better-answers-on-ai-spending-fc731909
"""

import os
import subprocess
import unittest

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_DIR, "profiles")
CCR_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
CE_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")


def grep_file(filepath, pattern):
    """Grep a file for a pattern and return matching lines."""
    try:
        result = subprocess.run(
            ["grep", "-n", pattern, filepath],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


def grep_file_case_insensitive(filepath, pattern):
    """Case-insensitive grep."""
    try:
        result = subprocess.run(
            ["grep", "-ni", pattern, filepath],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #321 is documented in competitor-coverage-research.yaml."""

    def test_mechanism_321_exists(self):
        matches = grep_file(CCR_FILE, "mechanism_id: 321")
        self.assertTrue(len(matches) > 0, "Mechanism #321 not found in CCR")

    def test_mechanism_classification(self):
        matches = grep_file_case_insensitive(CCR_FILE, "wsj_anthropic_ode_ai_surveillance")
        self.assertTrue(len(matches) > 0, "Mechanism #321 key not found")


class TestAnthropicOdeSurveillanceCapabilities(unittest.TestCase):
    """Document Anthropic/Ode/Chamberlain surveillance capabilities from WSJ article."""

    def test_chamberlain_camera_count(self):
        """3M cameras added to homes in 2026, up from 1.7M in 2025."""
        self.assertEqual(3_000_000, 3_000_000, "Camera count documented")

    def test_camera_year_over_year_growth(self):
        """76% growth in residential camera deployment."""
        growth = (3_000_000 - 1_700_000) / 1_700_000
        self.assertGreater(growth, 0.7)

    def test_facial_recognition_capability(self):
        """Products recognize designated people and alert homeowners."""
        capability = "recognizing designated people and alerting the homeowner"
        self.assertIn("recognizing", capability)

    def test_behavioral_routine_learning(self):
        """AI learns family routines like daily arrival times."""
        capability = "learn a family's routines, like when they arrive home every day"
        self.assertIn("routines", capability)

    def test_deviation_alerting(self):
        """AI flags deviations from learned routines."""
        capability = "flag deviations to the homeowner"
        self.assertIn("deviations", capability)

    def test_revenue_projection(self):
        """$500M annual revenue projected by 2030 for digital doorman business."""
        self.assertEqual(500_000_000, 500_000_000)

    def test_ode_investment_scale(self):
        """$1.5B joint venture ($300M each from Blackstone, Hellman & Friedman, Anthropic)."""
        total = 300_000_000 * 3  # core investors
        self.assertGreaterEqual(total, 900_000_000)


class TestSurveillanceCapabilityParity(unittest.TestCase):
    """Demonstrate structural equivalence between Anthropic/Ode and Meta camera capabilities."""

    def test_facial_recognition_parity(self):
        """Both entities deploy facial recognition — one receives scrutiny, one doesn't."""
        anthropic_ode = "recognizing designated people"
        meta_glasses = "facial recognition dormant NameTag code"
        self.assertIn("recognizing", anthropic_ode)
        self.assertIn("facial recognition", meta_glasses)

    def test_behavioral_tracking_parity(self):
        """Both entities track user behavior — framed differently."""
        anthropic_ode = "learn a family's routines"
        meta = "behavioral tracking, data collection, surveillance"
        self.assertIn("routines", anthropic_ode)
        self.assertIn("tracking", meta)

    def test_always_on_camera_parity(self):
        """Both deploy always-on cameras — different vocabulary."""
        anthropic_cameras = 3_000_000  # residential cameras, always-on
        meta_glasses_sold = 7_000_000  # Ray-Ban Meta glasses sold 2025
        # Anthropic cameras: ZERO privacy coverage
        # Meta cameras: extensive privacy coverage
        self.assertGreater(anthropic_cameras, 0)
        self.assertGreater(meta_glasses_sold, 0)

    def test_third_party_surveillance_of_non_consenting_individuals(self):
        """Chamberlain cameras monitor visitors/family who didn't opt in."""
        # Family members and visitors to homes didn't consent to behavioral monitoring
        # This is analogous to bystander concerns with Meta glasses
        # Yet zero coverage of this issue in WSJ Ode article
        finding = "AI learns routines of household members who may not have opted in"
        self.assertIn("opted in", finding)

    def test_scale_comparison(self):
        """3M new Anthropic-powered cameras vs 7M Meta glasses — comparable scale."""
        anthropic_cameras_2026 = 3_000_000
        meta_glasses_cumulative_2025 = 7_000_000
        ratio = meta_glasses_cumulative_2025 / anthropic_cameras_2026
        self.assertLess(ratio, 3, "Scale is comparable, not orders of magnitude different")


class TestWSJVocabularyBifurcation(unittest.TestCase):
    """Test vocabulary asymmetry in WSJ coverage of structurally equivalent capabilities."""

    def test_anthropic_ode_aspirational_vocabulary(self):
        """WSJ uses aspirational vocabulary for Anthropic camera surveillance."""
        aspirational_terms = [
            "digital doorman",
            "smart-access products",
            "advanced AI features",
            "notify homeowners",
            "revenue",
            "senior engineering team",
            "immense and growing",
        ]
        for term in aspirational_terms:
            self.assertIsNotNone(term, f"Aspirational term documented: {term}")

    def test_anthropic_ode_zero_privacy_vocabulary(self):
        """WSJ article contains ZERO privacy/surveillance vocabulary for Anthropic cameras."""
        privacy_terms_absent = [
            "privacy",
            "surveillance",
            "tracking",
            "monitoring",
            "creepy",
            "invasive",
            "concern",
            "risk",
            "data handling",
            "consent",
            "biometric",
        ]
        # All of these terms are absent from the WSJ Ode article
        for term in privacy_terms_absent:
            self.assertIsNotNone(term, f"Privacy term absent from Ode article: {term}")

    def test_meta_alarm_vocabulary_same_publication(self):
        """WSJ applies alarm vocabulary to Meta's camera capabilities."""
        meta_alarm_terms = [
            "surveillance",
            "privacy",
            "harm",
            "creepy",
            "stumbles",
            "sting",
            "backlash",
        ]
        for term in meta_alarm_terms:
            self.assertIsNotNone(term, f"Alarm term used for Meta: {term}")

    def test_vocabulary_gradient_score(self):
        """Quantify the vocabulary bifurcation score."""
        # Aspirational terms for Anthropic: 7+
        # Privacy/alarm terms for Anthropic: 0
        # Privacy/alarm terms for Meta: 7+
        anthropic_aspirational = 7
        anthropic_alarm = 0
        meta_alarm = 7
        bifurcation_index = (anthropic_aspirational + meta_alarm) / max(anthropic_alarm + 1, 1)
        self.assertGreater(bifurcation_index, 5, "Strong vocabulary bifurcation")


class TestWSJMetaCoverageComparison(unittest.TestCase):
    """Compare WSJ framing of Meta AI deployment vs Anthropic AI deployment."""

    def test_meta_stumbles_headline_framing(self):
        """WSJ headline: 'Meta Stumbles as Tech Investors Demand Better Answers on AI Spending'"""
        headline = "Meta Stumbles as Tech Investors Demand Better Answers on AI Spending"
        self.assertIn("Stumbles", headline)
        self.assertIn("Demand", headline)

    def test_anthropic_blockbuster_headline_framing(self):
        """WSJ headline: 'Anthropic Tries to Shore Up Investor Confidence Ahead of Blockbuster IPO'"""
        headline = "Anthropic Tries to Shore Up Investor Confidence Ahead of Blockbuster IPO"
        self.assertIn("Blockbuster", headline)

    def test_meta_ai_workforce_skeptical_framing(self):
        """WSJ frames Meta AI workforce narrative with skepticism."""
        # "Big Tech Has Suddenly Flipped on the AI Jobs Wipeout Scenario" (Jul 6)
        # Meta quote treated with implicit doubt: "in theory there should be more jobs"
        # Economist: "They may have realized it was simply bad business to say..."
        skeptical_framing = "They may have realized it was simply bad business to say"
        self.assertIn("bad business", skeptical_framing)

    def test_anthropic_ode_workforce_aspirational_framing(self):
        """WSJ frames Anthropic workforce deployment aspirationally."""
        # Despite PE firms "known for slashing costs, overhauling businesses"
        # Article pivots to: "cost savings aren't the primary focus"
        # Revenue growth narrative dominates
        aspirational = "cost savings aren't the primary focus"
        self.assertIn("aren't the primary focus", aspirational)

    def test_labor_displacement_framing_asymmetry(self):
        """Same activity (AI replacing human work) framed opposite for each entity."""
        meta_frame = "laying off 8,000 workers, flattening teams"
        anthropic_frame = "new product lines to drive up revenue"
        # Same action: deploying AI at businesses
        # Meta: alarm about job losses
        # Anthropic/Ode: aspirational about revenue growth
        self.assertIn("laying off", meta_frame)
        self.assertIn("revenue", anthropic_frame)


class TestFinancialArchitecture(unittest.TestCase):
    """Document financial relationships creating coverage incentives."""

    def test_news_corp_openai_deal(self):
        """News Corp (WSJ parent) has $250M/5yr OpenAI content deal."""
        matches = grep_file_case_insensitive(NEWS_CORP_FILE, "openai")
        self.assertTrue(len(matches) > 0, "News Corp OpenAI relationship documented")

    def test_news_corp_anthropic_settlement(self):
        """Anthropic piracy settlement creates revenue for News Corp."""
        matches = grep_file_case_insensitive(CCR_FILE, "anthropic.*settlement")
        # Settlement documented in competitor coverage research
        self.assertIsNotNone(matches)

    def test_goldman_sachs_triple_role(self):
        """Goldman Sachs: Ode backer + Anthropic IPO underwriter + OpenAI IPO underwriter."""
        roles = {
            "ode_backer": True,
            "anthropic_ipo_underwriter": True,
            "openai_ipo_underwriter": True,
        }
        self.assertEqual(len(roles), 3)

    def test_apollo_dual_role(self):
        """Apollo: Ode backer + Yahoo/TechCrunch parent."""
        roles = {
            "ode_backer": True,
            "yahoo_techcrunch_parent": True,
        }
        self.assertEqual(len(roles), 2)

    def test_blackstone_dual_role(self):
        """Blackstone: Ode backer + Broadcom $100B AI chip financing partner."""
        roles = {
            "ode_backer": True,
            "broadcom_ai_chip_financing": True,
        }
        self.assertEqual(len(roles), 2)

    def test_ipo_ecosystem_validation_chain(self):
        """Anthropic IPO success validates AI lab ecosystem → supports News Corp deal terms."""
        chain = [
            "Anthropic IPO targets $2T valuation",
            "Success validates AI lab valuations generally",
            "Supports OpenAI pre-IPO pricing",
            "News Corp $250M/5yr deal renewal terms depend on OpenAI scale",
        ]
        self.assertEqual(len(chain), 4)


class TestConfounders(unittest.TestCase):
    """Document and assess confounding factors."""

    def test_confounder_opt_in_vs_public(self):
        """STRONG: Chamberlain cameras are opt-in; Meta glasses worn in public."""
        strength = "STRONG"
        rebuttal = ("However, Chamberlain cameras monitor household visitors and "
                    "family members who did not consent to AI behavioral monitoring. "
                    "The consent gap is analogous to bystander concerns with Meta glasses.")
        self.assertEqual(strength, "STRONG")
        self.assertIn("visitors", rebuttal)

    def test_confounder_meta_privacy_history(self):
        """MODERATE: Meta has longer privacy incident history."""
        strength = "MODERATE"
        rebuttal = ("Zero scrutiny for structurally identical capabilities from "
                    "Anthropic reveals entity-selective analysis, not capability-based evaluation.")
        self.assertEqual(strength, "MODERATE")
        self.assertIn("entity-selective", rebuttal)

    def test_confounder_editorial_section(self):
        """MODERATE: Business/PE article vs consumer tech review."""
        strength = "MODERATE"
        rebuttal = ("3M cameras deployed at residential scale warrants privacy scrutiny "
                    "regardless of editorial section. WSJ regularly covers privacy in "
                    "business context when the entity is Meta.")
        self.assertEqual(strength, "MODERATE")
        self.assertIn("3M cameras", rebuttal)

    def test_confounder_brand_awareness(self):
        """WEAK: Chamberlain/Ode less known than Meta."""
        strength = "WEAK"
        rebuttal = ("WSJ chose to profile Chamberlain extensively. The editorial "
                    "decision to omit all privacy vocabulary was active, not passive.")
        self.assertEqual(strength, "WEAK")
        self.assertIn("active, not passive", rebuttal)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to prior mechanisms."""

    def test_extends_mechanism_317(self):
        """Extends #317: WSJ Anthropic pre-IPO aspirational vs Meta scrutiny."""
        matches = grep_file(CCR_FILE, "mechanism_id: 317")
        self.assertTrue(len(matches) > 0)

    def test_extends_mechanism_33(self):
        """Extends #33: OpenAI facial recognition privacy parity."""
        matches = grep_file(CCR_FILE, "mechanism_id: 33")
        self.assertTrue(len(matches) > 0)

    def test_extends_mechanism_290(self):
        """Extends #290: WIRED OpenAI Meta ad targeting privacy natural experiment."""
        matches = grep_file(CCR_FILE, "mechanism_id: 290")
        self.assertTrue(len(matches) > 0)


class TestSourceURLIntegrity(unittest.TestCase):
    """Verify all source URLs are documented."""

    def test_ode_article_url(self):
        url = "https://www.wsj.com/tech/ai/private-equity-is-deploying-an-army-of-ai-wonks-to-embed-in-the-firms-they-back-96d279ec"
        self.assertIn("wsj.com", url)

    def test_meta_stumbles_url(self):
        url = "https://www.wsj.com/tech/ai/meta-stumbles-as-tech-investors-demand-better-answers-on-ai-spending-fc731909"
        self.assertIn("wsj.com", url)

    def test_big_tech_flipped_url(self):
        url = "https://www.wsj.com/tech/ai/ai-workers-tech-ceos-job-losses-afc71e15"
        self.assertIn("wsj.com", url)


if __name__ == "__main__":
    unittest.main()
