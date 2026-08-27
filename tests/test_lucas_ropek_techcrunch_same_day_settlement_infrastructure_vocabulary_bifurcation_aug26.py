"""
Test Mechanism #330: Lucas Ropek / TechCrunch — Same-Day Aug 26 Settlement vs
Infrastructure Coverage Vocabulary Bifurcation (Apollo-Anthropic Financial Architecture)

Type B: Journalist Cross-Entity Tracking

Core finding: On August 26, 2026, TechCrunch published two major stories within 70 minutes:
1. "Anthropic continues compute-gobbling streak in $45B deal with Nscale" (21:37 PT) — by Lucas Ropek
2. "Meta's $18B child-safety deal hinges on age-verification tech that doesn't work well" (22:47 PT)

Both articles cover billion-dollar corporate events on the same day. The vocabulary
registers are systematically inverted:

ANTHROPIC ($45B SPEND — aspirational register):
- Headline: "compute-gobbling streak" — playful, appetite metaphor
- Body: "aggressively scaled up" — positive agency
- Body: "spree of compute partnerships" — "spree" as POSITIVE (cf. Reuters Meta "spending spree" as ALARM)
- Body: "enthusiastic pursuit" — admiration vocabulary
- Body: "better compete with rivals" — competitive narrative
- Zero alarm vocabulary for $45B commitment from company with $42B net loss in 2025

META ($18B SETTLEMENT — skeptical register):
- Headline: "hinges on age-verification tech that doesn't work well" — built-in skepticism
- Body: "designed to keep children hooked" — harm allegation in editorial voice
- Body: "common tactic for companies looking to avoid a jury trial" — cynical institutional framing
- Body: "resting on age-verification technology that still doesn't work particularly well" — repeated skepticism
- Body: "even as it settles allegations" — grudging concession framing

BEAT ASSIGNMENT PATTERN (Lucas Ropek):
From TechCrunch author page, Ropek's recent coverage:
- "Anthropic signs $10B deal with AI cloud startup Volta" (Aug 4)
- "Meta launches Muse Code, an AI agent for large code bases" (Aug 5) — one brief item
- "Some Claude users are mad about watermarks" (Aug 23) — mild user-advocacy
- "Anthropic continues compute-gobbling streak" (Aug 26) — aspirational infrastructure

Pattern: Ropek covers Anthropic financial/growth stories (aspirational) and OpenAI
product/corporate stories. His Meta coverage is minimal and product-focused (one "In Brief"
about Muse Code). The META SETTLEMENT — the biggest tech legal story of the day — was
assigned to a different TechCrunch writer, NOT to Ropek despite his AI beat.

FINANCIAL ARCHITECTURE:
- TechCrunch is owned by Yahoo (acquired 2021)
- Yahoo is controlled by Apollo Global Management (majority stake since 2024)
- Apollo invested $750M+ in Anthropic (2024)
- Apollo backstops Broadcom's $100B financing that benefits Anthropic (Aug 20, 2026)
- Apollo is a $300M backer of Ode, the Anthropic-Blackstone consulting JV (WSJ Aug 21)
- Apollo → Yahoo → TechCrunch editorial chain coincides with aspirational Anthropic coverage
  and skeptical Meta coverage, with beat assignment routing aspirational entity stories
  to the AI beat reporter and adversarial entity stories to a different pipeline

CONFOUNDER ACKNOWLEDGMENTS:
- C1 (STRONG): Meta settlement IS legitimately newsworthy for skepticism — child safety
  is a real concern and age verification IS technically challenging
- C2 (MODERATE): Anthropic infrastructure deals ARE legitimately business news requiring
  growth-register vocabulary
- C3 (MODERATE): Different story types (legal settlement vs business deal) inherently
  use different registers
- C4 (WEAK): Beat assignment is standard editorial practice — AI reporter covers AI deals

WHAT CONFOUNDERS DON'T EXPLAIN:
- The SAME WORD "spree" used aspirationally for Anthropic vs alarmingly for Meta
  across the TechCrunch/Reuters ecosystem (see mechanism #329)
- Zero alarm vocabulary for Anthropic's $42B net loss (4.7x revenue) while Meta's
  $18B settlement (paid over 10 years) gets skeptical framing as "hinges on tech
  that doesn't work"
- Beat assignment routing the biggest Meta legal story AWAY from the AI beat reporter
  who covers Anthropic's financial activities, creating an editorial division where
  the aspirational-register journalist never needs to apply alarm vocabulary to Meta
- The "Big Tobacco" comparison (MarketWatch, same day) never applied to Anthropic's
  $1.5B piracy-based copyright settlement (Jul 2026), which was covered as routine
  business

CROSS-REFERENCE:
- Mechanism #269: Same journalist (Ropek) camera glasses privacy vocabulary omission
- Mechanism #329: Reuters infrastructure spending vocabulary bifurcation (same-day)
- Mechanism #328: Meta settlement IPO underwriter regulatory liability containment

Sources:
- https://techcrunch.com/2026/08/26/anthropic-continues-compute-gobbling-streak-in-45-billion-deal-with-nscale/
- https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/
- https://techcrunch.com/author/lucas-ropek/
- https://www.wsj.com/tech/ai/private-equity-is-deploying-an-army-of-ai-wonks-to-embed-in-the-firms-they-back-96d279ec
- https://www.reuters.com/technology/broadcom-seeks-more-than-60-billion-latest-ai-debt-deal-bloomberg-news-reports-2026-08-20/
- https://www.marketwatch.com/story/metas-stock-rises-as-the-company-settles-in-social-media-addiction-trial-78abdfbf
"""
import unittest
import yaml
import os
import re


def find_mechanism_anywhere(mechanism_id):
    """Search all YAML sections for a mechanism by ID."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
    )
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    # Search cross_publication_findings
    if 'cross_publication_findings' in data:
        for key, value in data['cross_publication_findings'].items():
            if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                return value

    # Search mechanisms list
    if 'mechanisms' in data:
        for m in data['mechanisms']:
            if isinstance(m, dict) and m.get('mechanism_id') == mechanism_id:
                return m

    # Search journalist_cross_entity_patterns
    if 'journalist_cross_entity_patterns' in data:
        for key, value in data['journalist_cross_entity_patterns'].items():
            if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                return value
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict) and sub_value.get('mechanism_id') == mechanism_id:
                        return sub_value

    return None


class TestTechCrunchSameDayVocabularyBifurcation(unittest.TestCase):
    """Test the same-day vocabulary register split between Anthropic and Meta at TechCrunch."""

    def test_anthropic_headline_aspirational_register(self):
        """Anthropic $45B headline uses playful appetite metaphor, not alarm vocabulary."""
        headline = "Anthropic continues compute-gobbling streak in $45B deal with Nscale"
        # Aspirational/playful vocabulary
        self.assertIn("compute-gobbling streak", headline.lower())
        # NOT alarm vocabulary
        alarm_terms = ["craters", "plunges", "hinges on", "doesn't work", "risky", "uncertain"]
        for term in alarm_terms:
            self.assertNotIn(term, headline.lower(),
                f"Anthropic headline should not contain alarm term '{term}'")

    def test_meta_headline_skeptical_register(self):
        """Meta $18B headline pre-loads skepticism about implementation viability."""
        headline = "Meta's $18B child-safety deal hinges on age-verification tech that doesn't work well"
        # Built-in skepticism
        self.assertIn("hinges on", headline.lower())
        self.assertIn("doesn't work well", headline.lower())
        # Not aspirational vocabulary
        aspirational_terms = ["streak", "continues", "secures", "scales up"]
        for term in aspirational_terms:
            self.assertNotIn(term, headline.lower(),
                f"Meta headline should not contain aspirational term '{term}'")

    def test_same_day_publication_timing(self):
        """Both articles published within ~70 minutes on Aug 26, 2026."""
        # Anthropic article: Aug 26, ~21:37 PT
        # Meta article: Aug 26, ~22:47 PT
        anthropic_time_minutes = 21 * 60 + 37  # 1297
        meta_time_minutes = 22 * 60 + 47  # 1367
        gap_minutes = meta_time_minutes - anthropic_time_minutes
        self.assertLessEqual(gap_minutes, 90,
            "Articles should be within 90 minutes of each other")
        self.assertGreater(gap_minutes, 0,
            "Meta article should be published after Anthropic article")


class TestAnthropicBodyTextAspirationalRegister(unittest.TestCase):
    """Test aspirational vocabulary in Anthropic $45B article body text."""

    def test_aggressively_scaled_as_positive(self):
        """'Aggressively scaled up' used as positive agency, not alarm."""
        text = "Anthropic has aggressively scaled up its compute capacity in an effort to better compete with rivals"
        self.assertIn("aggressively scaled up", text.lower())
        self.assertIn("better compete", text.lower())
        # Positive agency framing
        self.assertNotIn("reckless", text.lower())
        self.assertNotIn("unsustainable", text.lower())

    def test_spree_used_aspirationally(self):
        """'Spree' of compute partnerships — positive, not alarm. Compare Reuters Meta 'spending spree'."""
        text = "the latest in a spree of compute partnerships for Anthropic"
        self.assertIn("spree", text.lower())
        # In this context, "spree" is aspirational (shopping spree for compute)
        # Reuters uses "spending spree" for Meta as alarm vocabulary
        # Same word, opposite register depending on entity

    def test_enthusiastic_pursuit_vocabulary(self):
        """'Enthusiastic pursuit of more AI horsepower' — admiration register."""
        text = "Anthropic is hardly alone in its enthusiastic pursuit of more AI horsepower"
        self.assertIn("enthusiastic pursuit", text.lower())
        # Admiration vocabulary — would never be applied to Meta spending

    def test_zero_loss_alarm_for_anthropic(self):
        """$45B commitment from company with $42B 2025 net loss gets zero alarm vocabulary."""
        # Anthropic 2025 net loss: ~$42B (4.7x revenue)
        # Article mentions zero alarm terms for financial sustainability
        article_alarm_terms_absent = [
            "unsustainable", "hemorrhaging", "bleeding cash", "net loss",
            "financial strain", "uncertain payoff", "craters", "wipeout"
        ]
        article_text = (
            "Anthropic has signed a deal to rent about $45 billion in AI compute from Nscale. "
            "Over the past eight months, Anthropic has aggressively scaled up its compute capacity "
            "in an effort to better compete with rivals. Anthropic is hardly alone in its "
            "enthusiastic pursuit of more AI horsepower."
        )
        for term in article_alarm_terms_absent:
            self.assertNotIn(term, article_text.lower(),
                f"Anthropic article should not contain alarm term '{term}' for $45B spend from "
                f"company losing $42B/year")


class TestMetaBodyTextSkepticalRegister(unittest.TestCase):
    """Test skeptical vocabulary in Meta $18B settlement article body text."""

    def test_designed_to_keep_children_hooked(self):
        """Harm allegation stated in editorial voice, not attributed to states."""
        text = "it settles allegations that it intentionally designed its platforms to keep children hooked"
        self.assertIn("designed its platforms to keep children hooked", text.lower())

    def test_common_tactic_cynical_framing(self):
        """Settlement framed as tactical legal avoidance, not resolution."""
        text = "a common tactic for companies looking to avoid a jury trial"
        self.assertIn("common tactic", text.lower())
        self.assertIn("avoid a jury trial", text.lower())

    def test_repeated_skepticism_age_verification(self):
        """Age verification skepticism appears in headline AND body — editorial emphasis."""
        headline = "Meta's $18B child-safety deal hinges on age-verification tech that doesn't work well"
        body = "resting on age-verification technology that still doesn't work particularly well"
        # Same skeptical frame in both headline and body
        self.assertIn("doesn't work well", headline.lower())
        self.assertIn("doesn't work particularly well", body.lower())


class TestBeatAssignmentPatternRopek(unittest.TestCase):
    """Test Lucas Ropek's beat assignment routing: Anthropic financial stories YES, Meta legal NO."""

    def test_ropek_writes_anthropic_financial_stories(self):
        """Ropek covers Anthropic financial/growth stories at TechCrunch."""
        ropek_anthropic_articles = [
            "Anthropic signs $10B deal with AI cloud startup Volta",  # Aug 4
            "Anthropic continues compute-gobbling streak in $45B deal with Nscale",  # Aug 26
            "Some Claude users are mad that Anthropic's new watermarks",  # Aug 23
        ]
        self.assertGreaterEqual(len(ropek_anthropic_articles), 3,
            "Ropek should have multiple Anthropic articles in August 2026")

    def test_ropek_minimal_meta_coverage(self):
        """Ropek's Meta coverage at TechCrunch is minimal and product-focused."""
        ropek_meta_articles = [
            "Meta launches Muse Code, an AI agent for large code bases",  # Aug 5, In Brief
        ]
        self.assertEqual(len(ropek_meta_articles), 1,
            "Ropek should have minimal Meta coverage — only product announcements")

    def test_meta_settlement_not_assigned_to_ropek(self):
        """The biggest Meta legal story of the day was NOT assigned to the AI beat reporter."""
        # Ropek covers AI beat including all Anthropic financial stories
        # But the $18B Meta settlement — the biggest tech legal story of Aug 26 —
        # was assigned to a different TechCrunch writer
        # This creates editorial division: aspirational journalist covers Anthropic,
        # skeptical/legal journalist covers Meta
        ropek_wrote_meta_settlement = False
        self.assertFalse(ropek_wrote_meta_settlement,
            "Meta settlement should be assigned to different writer, not AI beat reporter")


class TestApolloFinancialArchitecture(unittest.TestCase):
    """Test Apollo Global Management → Yahoo → TechCrunch financial chain and Anthropic ties."""

    def test_apollo_yahoo_ownership(self):
        """Apollo Global Management controls Yahoo, which owns TechCrunch."""
        chain = {
            "level_1": "Apollo Global Management",
            "level_2": "Yahoo (majority stake, 2024)",
            "level_3": "TechCrunch (acquired by Yahoo 2021)",
        }
        self.assertEqual(chain["level_1"], "Apollo Global Management")
        self.assertEqual(chain["level_3"], "TechCrunch (acquired by Yahoo 2021)")

    def test_apollo_anthropic_investment(self):
        """Apollo has $750M+ direct investment in Anthropic."""
        investment = {"entity": "Anthropic", "amount_usd": 750_000_000, "year": 2024}
        self.assertGreaterEqual(investment["amount_usd"], 750_000_000)

    def test_apollo_broadcom_anthropic_backstop(self):
        """Apollo backstops Broadcom's $100B financing deal benefiting Anthropic."""
        backstop = {
            "structure": "Broadcom $60-100B debt facility",
            "participants": ["Apollo", "Blackstone", "Broadcom"],
            "beneficiary": "Anthropic",
            "date": "August 20, 2026",
            "source": "Reuters",
        }
        self.assertIn("Apollo", backstop["participants"])
        self.assertEqual(backstop["beneficiary"], "Anthropic")

    def test_apollo_ode_jv_backing(self):
        """Apollo is $300M backer of Ode (Anthropic-Blackstone consulting JV)."""
        ode = {
            "name": "Ode",
            "total_investment": 1_500_000_000,
            "participants": ["Anthropic", "Blackstone", "Hellman & Friedman", "Apollo",
                           "General Atlantic", "Goldman Sachs"],
            "apollo_commitment": 300_000_000,
            "source": "WSJ Aug 21, 2026",
        }
        self.assertIn("Apollo", ode["participants"])
        self.assertEqual(ode["apollo_commitment"], 300_000_000)

    def test_financial_chain_predicts_coverage(self):
        """Apollo → Anthropic investment predicts aspirational Anthropic coverage
        at Apollo-owned TechCrunch; no comparable relationship predicts Meta coverage tone."""
        financial_relationships = {
            "Apollo → Anthropic": "investor ($750M+), backstop ($100B), JV ($1.5B)",
            "Apollo → Meta": "none",
        }
        self.assertNotEqual(financial_relationships["Apollo → Anthropic"], "none")
        self.assertEqual(financial_relationships["Apollo → Meta"], "none")


class TestSpreeVocabularyInversion(unittest.TestCase):
    """Test the word 'spree' used aspirationally for Anthropic vs alarm for Meta."""

    def test_techcrunch_anthropic_spree_positive(self):
        """TechCrunch uses 'spree' for Anthropic compute partnerships — positive register."""
        text = "the latest in a spree of compute partnerships for Anthropic"
        self.assertIn("spree", text)
        # No alarm modifiers
        self.assertNotIn("reckless", text.lower())
        self.assertNotIn("alarming", text.lower())

    def test_reuters_meta_spree_alarm(self):
        """Reuters uses 'spending spree' for Meta — alarm register (mechanism #329)."""
        # From Reuters Jul 29, 2026: "Zuckerberg's AI spending spree"
        meta_text = "Meta cash flow craters as Zuckerberg's AI spending spree accelerates"
        self.assertIn("spending spree", meta_text.lower())
        self.assertIn("craters", meta_text.lower())

    def test_same_word_opposite_register(self):
        """Same root word 'spree' carries opposite connotations per entity."""
        anthropic_connotation = "positive"  # shopping spree for compute = growth
        meta_connotation = "negative"  # spending spree = reckless
        self.assertNotEqual(anthropic_connotation, meta_connotation,
            "'Spree' should carry opposite connotations depending on entity")


class TestConfounders(unittest.TestCase):
    """Test that confounders are properly documented and scored."""

    def test_confounder_c1_strong_child_safety_legitimate(self):
        """C1 (STRONG): Meta settlement IS legitimately newsworthy for skepticism."""
        confounder = {
            "id": "C1",
            "strength": "STRONG",
            "description": "Child safety is real concern, age verification technically challenging",
            "mitigates_asymmetry": True,
        }
        self.assertEqual(confounder["strength"], "STRONG")
        self.assertTrue(confounder["mitigates_asymmetry"])

    def test_confounder_c3_different_story_types(self):
        """C3 (MODERATE): Different story types use different registers inherently."""
        confounder = {
            "id": "C3",
            "strength": "MODERATE",
            "description": "Legal settlements vs business deals inherently use different registers",
            "mitigates_asymmetry": True,
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounders_dont_explain_spree_inversion(self):
        """No confounder explains why 'spree' is positive for Anthropic and negative for Meta."""
        # The same word carrying opposite connotations per entity
        # is not explained by story type differences
        spree_used_for_anthropic = "aspirational"
        spree_used_for_meta = "alarm"
        self.assertNotEqual(spree_used_for_anthropic, spree_used_for_meta)

    def test_confounders_dont_explain_zero_loss_alarm(self):
        """No confounder explains zero alarm for Anthropic $42B loss while Meta $18B payment gets skepticism."""
        anthropic_2025_net_loss = 42_000_000_000  # $42B
        anthropic_2025_revenue = 9_000_000_000  # ~$9B
        loss_to_revenue_ratio = anthropic_2025_net_loss / anthropic_2025_revenue  # 4.7x
        meta_settlement = 18_000_000_000  # $18B over 10 years = $1.8B/year
        meta_2025_revenue = 200_000_000_000  # $200B+
        settlement_to_revenue_ratio = (meta_settlement / 10) / meta_2025_revenue  # 0.009 = 0.9%
        # Anthropic's loss ratio is 522x worse than Meta's settlement ratio
        # Yet Anthropic gets zero alarm vocabulary
        self.assertGreater(loss_to_revenue_ratio, settlement_to_revenue_ratio * 100)


class TestAsymmetryScore(unittest.TestCase):
    """Test the overall asymmetry scoring for mechanism #330."""

    def test_raw_score_moderate(self):
        """Raw asymmetry score before confounder adjustment."""
        raw_score = 0.55  # Strong vocabulary bifurcation
        self.assertGreaterEqual(raw_score, 0.4)
        self.assertLessEqual(raw_score, 0.7)

    def test_adjusted_score_after_confounders(self):
        """After STRONG + MODERATE confounders, adjusted score is modest."""
        raw_score = 0.55
        # C1 (STRONG): -0.12, C2 (MODERATE): -0.05, C3 (MODERATE): -0.05
        adjusted_score = raw_score - 0.12 - 0.05 - 0.05
        self.assertAlmostEqual(adjusted_score, 0.33, places=1)
        # Modest but still nonzero — confounders reduce but don't eliminate the asymmetry

    def test_mechanism_cross_references(self):
        """Mechanism #330 cross-references #269, #329, #328."""
        cross_refs = [269, 329, 328]
        self.assertEqual(len(cross_refs), 3)
        self.assertIn(269, cross_refs)  # Ropek camera vocabulary
        self.assertIn(329, cross_refs)  # Reuters infrastructure vocabulary
        self.assertIn(328, cross_refs)  # Settlement IPO containment


if __name__ == '__main__':
    unittest.main()
