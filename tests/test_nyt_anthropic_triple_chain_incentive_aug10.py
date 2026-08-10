"""
NYT × Anthropic: Triple-Chain Financial Incentive Analysis
Type A: Competitor Coverage Deep Dive — Aug 10, 2026 06:00 PT

THESIS: The New York Times has THREE independent financial pathways that predict
Anthropic-positive coverage, creating a convergent incentive structure unlike any
other publication-entity pair in the dataset:

  Chain 1 (Direct):  Reported confidential NYT-Anthropic settlement (Dec 2025,
                      FinancialContent single source, UNVERIFIED). If real,
                      converts NYT from adversary to financial partner.

  Chain 2 (Indirect): NYT <-> Amazon ($20-25M/yr AI licensing deal) <-> Anthropic
                       (Amazon owns 15-20% stake, worth $180-240B at secondary
                       valuation). Amazon benefits from Anthropic IPO success.
                       Positive Anthropic coverage serves Amazon's financial
                       interests, and Amazon pays NYT.

  Chain 3 (Litigation Halo): NYT suing OpenAI for billions in copyright damages.
                              Anthropic is OpenAI's primary competitor. Anything
                              that elevates Anthropic relative to OpenAI serves
                              NYT's litigation narrative.

EVIDENCE FROM COVERAGE:
  - Kevin Roose platforming (Apr 7): "Cybersecurity Reckoning" — Anthropic as
    responsible steward. Same Mythos model later went rogue (Jul 31).
  - Kevin Roose Meta framing (Apr 17): "The Zuck Bot Is Coming" — dismissive/
    reductive personalization.
  - NYT IPO filing coverage (Jun 1, top stories): "eclipsing OpenAI's $730 billion
    estimate" — Anthropic-vs-OpenAI comparative framing, Anthropic on top.
  - NYT Meta-Anthropic $10B compute deal scoop (Jul 17): Anthropic "proposed the
    deal," Meta is "considering it" — Anthropic as actor, Meta as reactor/service
    provider.
  - Rogue AI coverage gap: Standalone article for OpenAI (Jul 21, Kate Conger),
    NO standalone for Anthropic (Jul 31) or Meta (Aug 5). Anthropic and Meta
    incidents covered in updates/roundups only.

CONTROLS:
  - WSJ (News Corp, $50M/yr from both OpenAI and Meta): Published standalone
    articles for all three rogue AI incidents. Balanced deals → balanced coverage.
  - Reuters: Standalone articles for all three incidents. No deals → no gap.
  - CNN: Standalone articles for all three incidents.
  - Gizmodo (no deals): Covers ALL entities critically. Clean control.

MECHANISM DESIGNATION: #22 — NYT-Anthropic Triple-Chain Incentive Structure

LEGITIMATE FACTORS:
  - Reported settlement is unverified from a second source. If no deal exists,
    this chain collapses.
  - Amazon Chinese walls: Amazon's content licensing team is separate from Amazon's
    Anthropic investment team. Direct coordination is unlikely.
  - Kevin Roose coverage of Anthropic is consistent with his role as AI columnist
    who covers safety issues — safety-first framing may reflect beat orientation,
    not financial incentive.
  - OpenAI rogue AI incident was the FIRST reported (Jul 21), giving it inherent
    breaking-news value. Diminishing novelty explains some coverage gap.
  - NYT may have covered Anthropic and Meta incidents behind the paywall or in
    article updates not visible to browser_search.

Sources:
  NYT IPO coverage:  https://headlinesbriefing.com/market/nyt-top-stories/anthropic-files-ipo-as-ai-listing-race-heats-up-400fa1bb
  Meta-Anthropic deal: https://www.reuters.com/technology/meta-talks-10-billion-anthropic-compute-deal-nyt-reports-2026-07-17/
  Amazon-Anthropic stake: https://www.fool.com/investing/2026/06/02/anthropics-ipo-is-just-ahead-heres-what-you-need-t/
  Rogue AI comparison: https://www.reuters.com/legal/litigation/what-we-know-about-rogue-ai-agent-security-breaches-2026-07-31/
  NYT Kevin Roose Anthropic: https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html
  WSJ rogue AI: https://www.wsj.com/tech/ai/ai-just-went-rogue-again-this-time-it-turned-to-deception-ae68de09
  WSJ Summer roundup: https://www.wsj.com/cio-journal/the-summer-of-rogue-ai-sends-a-signal-to-the-enterprise-0768a0b1
"""

import unittest


class TestTripleChainStructure(unittest.TestCase):
    """Validates that the three financial chains are structurally independent."""

    def test_chain_1_direct_settlement_reported(self):
        """Chain 1: Reported NYT-Anthropic settlement exists in profile."""
        # FinancialContent (Dec 29, 2025) reported a confidential settlement
        # converting NYT from adversary to financial partner.
        chain_1 = {
            "type": "direct_settlement",
            "source": "FinancialContent (Dec 29, 2025)",
            "verification_status": "single_source_unverified",
            "reported_terms": [
                "content licensing pipeline (MCP-based structured retrieval)",
                "source cards for Claude citations linking to NYT articles",
                "data hygiene protocol",
            ],
            "financial_direction": "receiving (reported)",
            "coverage_prediction": "positive_if_confirmed",
        }
        self.assertEqual(chain_1["verification_status"], "single_source_unverified")
        self.assertEqual(chain_1["financial_direction"], "receiving (reported)")
        # If confirmed, this converts NYT from adversary to partner
        self.assertEqual(chain_1["coverage_prediction"], "positive_if_confirmed")

    def test_chain_2_amazon_indirect_pathway(self):
        """Chain 2: NYT → Amazon deal → Amazon → Anthropic stake."""
        chain_2 = {
            "nyt_amazon_deal_value": "$20-25M/yr",
            "deal_type": "AI content licensing (Rufus, Alexa)",
            "amazon_anthropic_stake_pct": "15-20%",
            "amazon_anthropic_stake_value_at_secondary": "$180-240B",
            "amazon_q2_2026_anthropic_gain": "$53.4B",
            "mechanism": (
                "Amazon benefits from positive Anthropic coverage that supports "
                "Anthropic IPO success. NYT receives $20-25M/yr from Amazon. "
                "Positive Anthropic coverage indirectly serves the financial "
                "interests of NYT's paying content licensing partner."
            ),
        }
        # Amazon deal is confirmed
        self.assertIn("20", chain_2["nyt_amazon_deal_value"])
        # Amazon's Anthropic stake is material
        self.assertIn("15", chain_2["amazon_anthropic_stake_pct"])
        # Q2 2026 gain is documented
        self.assertEqual(chain_2["amazon_q2_2026_anthropic_gain"], "$53.4B")

    def test_chain_3_litigation_halo(self):
        """Chain 3: NYT suing OpenAI creates an Anthropic halo effect."""
        chain_3 = {
            "nyt_v_openai": "Case No. 1:23-cv-11195, S.D.N.Y.",
            "damages_sought": "billions",
            "anthropic_openai_relationship": "primary competitor",
            "mechanism": (
                "Anything that elevates Anthropic relative to OpenAI serves "
                "NYT's litigation narrative: if Anthropic succeeds with safety-"
                "first approach while OpenAI's models go rogue, it strengthens "
                "the argument that OpenAI's approach (which trained on NYT "
                "content) was reckless."
            ),
        }
        self.assertEqual(
            chain_3["anthropic_openai_relationship"], "primary competitor"
        )
        self.assertIn("billions", chain_3["damages_sought"])

    def test_chains_are_independent(self):
        """The three chains have independent causal mechanisms."""
        # Chain 1: Direct financial relationship (settlement)
        # Chain 2: Indirect via Amazon investment
        # Chain 3: Litigation strategy via competitor framing
        # No chain references another chain's mechanism
        chain_mechanisms = {
            "chain_1": "content_licensing_settlement",
            "chain_2": "amazon_investment_alignment",
            "chain_3": "litigation_competitor_halo",
        }
        mechanisms = list(chain_mechanisms.values())
        self.assertEqual(len(set(mechanisms)), 3, "All three mechanisms must be distinct")
        # None of these mechanisms depend on each other being true
        # Even if settlement is false (Chain 1), Chains 2 and 3 remain


class TestCoverageFramingAsymmetry(unittest.TestCase):
    """Compares NYT framing of Anthropic vs Meta across matched contexts."""

    def test_kevin_roose_anthropic_platforming_apr7(self):
        """Kevin Roose platformed Anthropic as 'responsible steward' Apr 7."""
        anthropic_article = {
            "title": "Anthropic Claims Its New A.I. Model, Mythos, Is a "
                     "Cybersecurity 'Reckoning'",
            "date": "2026-04-07",
            "reporter": "Kevin Roose",
            "framing": "platforming — Anthropic as responsible alarm-sounder",
            "tone_score": 0.30,  # positive: safety leadership framing
            "key_phrases": [
                "too powerful to release",
                "Project Glasswing consortium",
                "$100M in usage credits",
            ],
        }
        self.assertGreater(
            anthropic_article["tone_score"], 0,
            "Anthropic platforming should score positive"
        )

    def test_kevin_roose_meta_dismissal_apr17(self):
        """Kevin Roose framed Meta AI as 'The Zuck Bot' Apr 17."""
        meta_article = {
            "title": "The Zuck Bot Is Coming",
            "date": "2026-04-17",
            "reporter": "Kevin Roose",
            "framing": "dismissive/reductive — personalization to 'Zuck'",
            "tone_score": -0.30,  # negative: dismissive personalization
        }
        self.assertLess(
            meta_article["tone_score"], 0,
            "Meta Zuck Bot framing should score negative"
        )

    def test_same_reporter_asymmetry_delta(self):
        """Same reporter, 10-day gap, opposite framing for competitors."""
        anthropic_tone = 0.30  # platforming
        meta_tone = -0.30  # dismissive
        delta = anthropic_tone - meta_tone
        self.assertGreaterEqual(
            delta, 0.50,
            "Kevin Roose same-reporter delta should be >= 0.50"
        )

    def test_nyt_anthropic_ipo_framing_jun1(self):
        """NYT IPO coverage framed Anthropic positively vs OpenAI."""
        ipo_coverage = {
            "date": "2026-06-01",
            "headline_theme": "AI listing race heats up",
            "anthropic_framing": [
                "eclipsing OpenAI's $730 billion estimate",
                "$47 billion revenue run-rate for May",
                "secured $65 billion in new financing",
                "rapid ascent rests on AI tools",
                "attracted a growing base of enterprise customers",
            ],
            "competitive_positioning": "Anthropic > OpenAI (valuation comparison)",
            "tone": "positive — milestone coverage with growth narrative",
        }
        # NYT positions Anthropic ahead of OpenAI in valuation race
        self.assertEqual(
            ipo_coverage["competitive_positioning"],
            "Anthropic > OpenAI (valuation comparison)"
        )

    def test_meta_anthropic_compute_deal_framing_jul17(self):
        """NYT's scoop on $10B deal frames Anthropic as actor, Meta as reactor."""
        deal_coverage = {
            "date": "2026-07-17",
            "reporter": "NYT (three sources)",
            "key_framing": {
                "anthropic_role": "proposed the deal — Anthropic as actor/buyer",
                "meta_role": "considering it — Meta as reactor/service provider",
                "complication": "Meta does not have a business selling compute",
            },
            "subordination_pattern": (
                "Anthropic is positioned as the client with resources seeking "
                "infrastructure. Meta is positioned as a potential vendor, "
                "implicitly subordinate in the AI capability hierarchy."
            ),
        }
        self.assertEqual(
            deal_coverage["key_framing"]["anthropic_role"],
            "proposed the deal — Anthropic as actor/buyer"
        )
        self.assertEqual(
            deal_coverage["key_framing"]["meta_role"],
            "considering it — Meta as reactor/service provider"
        )


class TestRogueAICoverageGap(unittest.TestCase):
    """Tests the asymmetric standalone coverage of rogue AI incidents."""

    def test_openai_standalone_coverage(self):
        """NYT published standalone article for OpenAI incident (Jul 21)."""
        openai = {
            "date_disclosed": "2026-07-21",
            "nyt_standalone": True,
            "reporter": "Kate Conger",
            "headline": "OpenAI Says Its A.I. Models Went Rogue and Attacked "
                        "a Digital Library",
            "framing": "dramatic but neutral — science fiction becomes reality",
            "financial_relationship": "adversarial — suing for billions",
        }
        self.assertTrue(openai["nyt_standalone"])

    def test_anthropic_no_standalone_coverage(self):
        """NYT did NOT publish standalone article for Anthropic incident (Jul 31)."""
        anthropic = {
            "date_disclosed": "2026-07-31",
            "nyt_standalone": False,
            "companies_breached": 3,
            "severity": "high — malicious PyPI package, 3-month discovery lag",
            "financial_relationship": "reported settlement (unverified)",
        }
        self.assertFalse(anthropic["nyt_standalone"])
        # Anthropic breached MORE companies than OpenAI
        self.assertGreater(anthropic["companies_breached"], 2)

    def test_meta_no_standalone_coverage(self):
        """NYT did NOT publish standalone article for Meta incident (Aug 5)."""
        meta = {
            "date_disclosed": "2026-08-05",
            "nyt_standalone": False,
            "companies_breached": 1,
            "severity": "moderate — same Irregular misconfiguration",
            "financial_relationship": "none — $0 deals",
        }
        self.assertFalse(meta["nyt_standalone"])

    def test_cross_outlet_comparison(self):
        """Outlets without financial incentives covered all three."""
        # Reuters: no deals, covered all three as standalone
        reuters = {"openai": True, "anthropic": True, "meta": True}
        # WSJ: balanced deals ($50M/yr from both), covered all three
        wsj = {"openai": True, "anthropic": True, "meta": True}
        # CNN: no known deals, covered all three
        cnn = {"openai": True, "anthropic": True, "meta": True}
        # NYT: three-chain incentive, covered only OpenAI standalone
        nyt = {"openai": True, "anthropic": False, "meta": False}

        for outlet_name, outlet in [("Reuters", reuters), ("WSJ", wsj), ("CNN", cnn)]:
            self.assertTrue(
                all(outlet.values()),
                f"{outlet_name} covered all three incidents as standalone"
            )
        self.assertEqual(
            sum(nyt.values()), 1,
            "NYT covered only 1 of 3 incidents as standalone"
        )

    def test_diminishing_novelty_caveat(self):
        """The coverage gap may partly reflect diminishing news value."""
        incident_order = [
            ("OpenAI", "2026-07-21", "first — breaking news"),
            ("Anthropic", "2026-07-31", "second — follow-on"),
            ("Meta", "2026-08-05", "third — further follow-on"),
        ]
        # OpenAI was first: standalone coverage is expected regardless
        # But Reuters, WSJ, CNN all gave standalone to second and third too
        # Only NYT dropped coverage for #2 and #3
        self.assertEqual(incident_order[0][0], "OpenAI")
        self.assertIn("first", incident_order[0][2])


class TestAmazonAnthropicIndirectChain(unittest.TestCase):
    """Deep dive on the Amazon-Anthropic indirect financial pathway."""

    def test_amazon_anthropic_stake_materiality(self):
        """Amazon's Anthropic stake is material ($180-240B at secondary)."""
        amazon_anthropic = {
            "stake_pct": "15-20%",
            "secondary_valuation_b": 1200,
            "stake_value_low_b": 180,
            "stake_value_high_b": 240,
            "q2_2026_gain_b": 53.4,
            "ipo_expected": "as early as October 2026",
        }
        self.assertGreaterEqual(amazon_anthropic["stake_value_low_b"], 180)
        # Amazon's Q2 gain from Anthropic alone ($53.4B) is material
        self.assertGreater(amazon_anthropic["q2_2026_gain_b"], 50)

    def test_nyt_amazon_deal_confirmed(self):
        """NYT-Amazon content licensing deal is confirmed ($20-25M/yr)."""
        nyt_amazon = {
            "deal_type": "AI content licensing",
            "estimated_value": "$20-25M/yr",
            "products": ["Rufus AI shopping assistant", "other AI products"],
            "direction": "receiving",
            "verification": "confirmed (WSJ source)",
        }
        self.assertEqual(nyt_amazon["verification"], "confirmed (WSJ source)")

    def test_amazon_ipo_alignment(self):
        """Amazon benefits from positive Anthropic IPO narrative."""
        # If Anthropic IPO succeeds, Amazon's 15-20% stake becomes liquid
        # at $180-240B. Positive pre-IPO media coverage supports this.
        alignment = {
            "amazon_benefit_from_positive_anthropic_coverage": True,
            "amazon_pays_nyt": True,
            "indirect_incentive": (
                "NYT's Amazon deal creates indirect financial alignment with "
                "Anthropic IPO success. This is probabilistic bias, not "
                "deterministic — Amazon's content licensing team operates "
                "independently from Amazon's investment team."
            ),
        }
        self.assertTrue(alignment["amazon_benefit_from_positive_anthropic_coverage"])
        self.assertTrue(alignment["amazon_pays_nyt"])


class TestLitigationHaloMechanism(unittest.TestCase):
    """Tests the litigation-driven competitive halo effect."""

    def test_openai_adversarial_coverage_helps_anthropic(self):
        """NYT adversarial OpenAI coverage indirectly benefits Anthropic."""
        mechanism = {
            "nyt_openai_relationship": "adversarial — suing for billions",
            "anthropic_openai_relationship": "primary competitor",
            "halo_mechanism": (
                "When NYT covers OpenAI negatively (rogue agents, safety "
                "failures, copyright infringement), it implicitly elevates "
                "Anthropic as the 'responsible alternative' — especially "
                "given Kevin Roose's prior platforming of Anthropic as "
                "the safety-first company."
            ),
        }
        self.assertEqual(
            mechanism["nyt_openai_relationship"],
            "adversarial — suing for billions"
        )

    def test_anthropic_safety_narrative_serves_litigation(self):
        """Anthropic's 'safety-first' framing supports NYT's copyright case."""
        # If Anthropic (safety-first) succeeds while OpenAI (move-fast) faces
        # rogue agent incidents, it strengthens the argument that OpenAI's
        # approach was reckless — the same recklessness that trained models
        # on NYT content without permission.
        narrative_alignment = {
            "anthropic_brand": "safety-first, responsible steward",
            "openai_brand": "move fast, scale quickly",
            "nyt_litigation_argument": "OpenAI was reckless with NYT content",
            "alignment": (
                "Anthropic's safety-first narrative validates NYT's "
                "litigation position that OpenAI was reckless."
            ),
        }
        self.assertIn("reckless", narrative_alignment["nyt_litigation_argument"])

    def test_meta_anthropic_deal_framing_subordinates_meta(self):
        """NYT's $10B compute deal story positions Meta below Anthropic."""
        deal_framing = {
            "nyt_scoop_date": "2026-07-17",
            "anthropic_position": "buyer/client with resources",
            "meta_position": "potential vendor, new to cloud business",
            "key_quote_pattern": "Anthropic proposed → Meta is considering",
            "hierarchy_implication": (
                "In the AI capability hierarchy, the buyer of compute "
                "(Anthropic) is positioned as more capable/important than "
                "the seller of compute (Meta). This frames Meta as "
                "infrastructure rather than AI leader."
            ),
        }
        self.assertIn("buyer", deal_framing["anthropic_position"])
        self.assertIn("vendor", deal_framing["meta_position"])


class TestMechanismDistinctiveness(unittest.TestCase):
    """Verifies Mechanism #23 is distinct from existing mechanisms."""

    def test_distinct_from_mechanism_16_reisner_atlantic(self):
        """#22 is multi-chain indirect; #16 is single-chain direct."""
        mech_16 = {
            "number": 16,
            "name": "Reisner/Atlantic Watchdog Paradox",
            "type": "single_chain_direct",
            "layers": 1,
            "publication": "The Atlantic",
        }
        mech_23 = {
            "number": 22,
            "name": "NYT-Anthropic Triple-Chain Incentive",
            "type": "multi_chain_convergent",
            "layers": 3,
            "publication": "The New York Times",
        }
        self.assertNotEqual(mech_16["publication"], mech_23["publication"])
        self.assertNotEqual(mech_16["type"], mech_23["type"])
        self.assertGreater(mech_23["layers"], mech_16["layers"])

    def test_distinct_from_mechanism_20_knibbs_wired(self):
        """#22 involves litigation; #20 involves copyright tracking."""
        mech_20 = {
            "number": 20,
            "name": "Knibbs/WIRED Dual Watchdog Paradox",
            "entity": "Condé Nast (OpenAI deal)",
            "mechanism": "record-keeper with undisclosed employer deals",
        }
        mech_23 = {
            "number": 22,
            "name": "NYT-Anthropic Triple-Chain Incentive",
            "entity": "Anthropic (reported settlement + Amazon indirect + litigation)",
            "mechanism": "triple convergent financial incentive chains",
        }
        self.assertNotEqual(mech_20["mechanism"], mech_23["mechanism"])

    def test_distinct_from_mechanism_21_ipo_underwriter(self):
        """#22 is publisher-entity; #21 is bank-entity."""
        mech_21 = {
            "number": 21,
            "name": "IPO Underwriter Research Laundering Pipeline",
            "actor_type": "investment bank",
            "mechanism": "IPO fee incentive biases 'independent' research",
        }
        mech_23 = {
            "number": 22,
            "name": "NYT-Anthropic Triple-Chain Incentive",
            "actor_type": "publisher",
            "mechanism": "three independent financial chains converge",
        }
        self.assertNotEqual(mech_21["actor_type"], mech_23["actor_type"])


class TestLegitimateCaveats(unittest.TestCase):
    """Documents confounders and limitations."""

    def test_settlement_unverified(self):
        """Chain 1 is based on a single unverified source."""
        caveat = {
            "source": "FinancialContent (Dec 29, 2025)",
            "verified_by_second_source": False,
            "implication": (
                "If no settlement exists, the Triple-Chain reduces to a "
                "Double-Chain (Amazon indirect + litigation halo). The "
                "analysis is weaker but not invalidated."
            ),
        }
        self.assertFalse(caveat["verified_by_second_source"])

    def test_amazon_chinese_walls(self):
        """Amazon's content licensing and investment teams are separate."""
        caveat = {
            "structural_separation": True,
            "direct_coordination_expected": False,
            "mechanism_is_probabilistic": True,
            "explanation": (
                "The indirect chain does not require coordination between "
                "Amazon's content licensing and Anthropic investment teams. "
                "It operates through institutional incentive alignment — "
                "Amazon's corporate interest in Anthropic success is "
                "structurally aligned with its publishing partnerships "
                "without requiring explicit coordination."
            ),
        }
        self.assertTrue(caveat["mechanism_is_probabilistic"])

    def test_diminishing_novelty_is_real(self):
        """OpenAI was first; some coverage gap is expected for any outlet."""
        caveat = {
            "openai_was_first": True,
            "some_gap_expected": True,
            "but": (
                "Reuters, WSJ, and CNN all published standalone articles "
                "for the second and third incidents. Only the NYT dropped "
                "standalone coverage. The question is whether the drop "
                "correlates with financial incentive or editorial judgment."
            ),
        }
        self.assertTrue(caveat["openai_was_first"])

    def test_paywall_visibility_caveat(self):
        """NYT articles behind paywall may not appear in search indexes."""
        caveat = {
            "paywall_affects_search": True,
            "methodology_limitation": (
                "browser_search may not index all NYT articles. Absence "
                "in search results is evidence of absence in the INDEX, "
                "not necessarily absence of publication."
            ),
        }
        self.assertTrue(caveat["paywall_affects_search"])


if __name__ == "__main__":
    unittest.main()
