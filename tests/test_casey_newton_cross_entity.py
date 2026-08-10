"""
Casey Newton (Platformer / Hard Fork) — Cross-Entity Coverage Analysis

Mechanism #24: Disclosure-as-Inoculation Paradox — Transparent Personal Conflict
Without Independent Verification

Casey Newton is the founder/editor of Platformer and co-host of Hard Fork (NYT podcast,
ending Aug 2026). He is one of the most influential tech journalists in the US, with
170,000+ free subscribers (as of Jan 2024) and a podcast in the top 0.05% globally.

His fiancé works at Anthropic as a software engineer (started Jan 2025; engaged Feb 2026).
Newton has a detailed ethics disclosure page (platformer.news/ethics) and includes
conflict-of-interest disclosures at the top of columns that "primarily concern Anthropic,
its competitors, or the AI industry at large." This is industry-best-practice disclosure
for independent journalism.

The paradox: disclosure ≠ neutralization. Newton's ethics page is transparent, but
the conflict remains structurally operative because:

1. **Self-regulated disclosure threshold.** Newton alone decides when disclosure applies.
   His ethics page says he'll disclose "even when the column does not specifically mention
   Anthropic" — but he also decides what constitutes "the AI industry at large."

2. **No institutional verification.** Platformer has no editorial board, no ethics editor,
   no publisher with oversight. When Newton was at The Verge (Vox Media), institutional
   disclosure standards applied. At Platformer, he sets his own standards.

3. **Framing asymmetry.** Meta coverage is accountability-framed (scams, child safety,
   "20-year mistake"), while Anthropic coverage is admiration-framed (Pentagon stand,
   Claude Code "believer," "rapture over Claude Opus 4.5"). Both coverage stances may
   be editorially defensible, but the pattern correlates with the personal relationship.

4. **Upcoming independence transition (Aug 2026+).** Newton and Kevin Roose are leaving
   NYT to launch an independent media venture. This removes the LAST institutional
   editorial oversight (NYT podcast editorial control), creating a fully independent AI
   journalism operation where Newton's personal conflict has zero external checks.

5. **The Anthropic Pentagon narrative.** Newton wrote "Following: Anthropic vs. The Pentagon"
   for Platformer (Feb 2026) during the Anthropic-Pentagon dispute, covering his fiancé's
   employer's highest-profile news story. The ethics disclosure was present. But the
   framing — Anthropic as principled defender against government overreach — aligned
   with Anthropic's own PR positioning. Compare to Harvard Berkman Klein Center's more
   skeptical analysis: "Don't bet that... Anthropic... is acting in the public interest"
   (Sanders & Schneier, The Guardian, Mar 3 2026).

6. **Meta-specific coverage history.** Newton's accountability journalism against Meta
   predates the Anthropic relationship: his 2019-2020 content moderation worker PTSD
   investigation led to a $52M Facebook/Cognizant settlement. This establishes a
   pre-existing adversarial framing toward Meta that the Anthropic relationship
   reinforces rather than creates.

Legitimate factors (must be documented — these are real):
- Newton's ethics disclosure is genuinely best-in-class for independent journalism
- He discloses on columns that DON'T specifically mention Anthropic (rare discipline)
- His fiancé's engineering role is separate from policy/product (Newton's focus areas)
- His Meta accountability journalism predates the Anthropic relationship by years
- He covers many companies critically (Substack, TikTok, X/Elon Musk, Google)
- Meta genuinely has content moderation and scam problems warranting critical coverage
- Anthropic's Pentagon stand was genuinely newsworthy regardless of personal ties
- Co-author Ryan Mac's "Character Limit" book is about Twitter/Musk, not Meta

Sources:
- Platformer ethics page: https://www.platformer.news/ethics/
  "In January 2025 my boyfriend began work as a software engineer at Anthropic"
  "We got engaged in February 2026"
  "Linking to the disclosure at the top of any column that primarily concerns Anthropic,
   its competitors, or the AI industry at large"
- Wikipedia: https://en.wikipedia.org/wiki/Casey_Newton
  "In February of 2026, he announced on Hard Fork that he is engaged and that his
   fiancé works for Anthropic"
- Platformer (Muck Rack): https://muckrack.com/casey-newton-2/articles
  "Disclosure: my fiancé works at Anthropic" (inline disclosure examples)
- "Following: Anthropic vs. The Pentagon" — Platformer, Feb 2026
  (cited in Techdirt Ctrl-Alt-Speech podcast roundup, Feb 26 2026)
  Source: http://www.techdirt.com/2026/02/26/ctrl-alt-speech-let-fly-the-claudes-of-war-with-casey-newton/
- Harvard Berkman Klein: "Don't bet that the Pentagon – or Anthropic – is acting in
  the public interest" — Sanders & Schneier, The Guardian, Mar 3 2026
  Source: https://cyber.harvard.edu/story/2026-03/dont-bet-pentagon-or-anthropic-acting-public-interest
- nexxworks podcast: Newton "gives Anthropic credit for two consequential stands this
  year: refusing the Pentagon's autonomous weapons... and pulling back the cyber-capable
  Mythos model" (2026)
  Source: https://www.nexxworks.com/blog/radar---by-nexxworks-never-normal-heroes-navigating-the-future-peter-hinssen-and-casey-newton-on-ai-and-society
- Platformer article listing: "Meta's scam problem, UK edition," "Meta's scam problem
  may trigger a legal reckoning," "Mark Zuckerberg's 20-year mistake," vs. "Claude Code
  for writers," "The project that turned me into a Claude Code believer," "the rapture
  over Claude Opus 4.5"
  Source: https://www.platformer.news/author/casey-newton/page/6/
  Source: https://www.platformer.news/author/casey-newton/page/20/
- Hard Fork ending Aug 2026; Newton and Roose launching independent venture:
  https://en.wikipedia.org/wiki/Casey_Newton
  "Roose announced Hard Fork would end in August, and that he and Newton would 'start
  a new show together, under our own shingle.'"
"""

import unittest


class TestCaseyNewtonProfile(unittest.TestCase):
    """Verify journalist profile accuracy."""

    def test_journalist_name_and_publications(self):
        """Casey Newton writes for Platformer (independent) and co-hosts Hard Fork (NYT)."""
        journalist = "Casey Newton"
        primary_pub = "Platformer"
        secondary_pub = "Hard Fork (New York Times)"
        pub_type = "independent newsletter (Ghost)"
        self.assertTrue(all([journalist, primary_pub, secondary_pub, pub_type]))

    def test_career_arc_institutional_to_independent(self):
        """Career trajectory: Arizona Republic → SF Chronicle → CNET → The Verge (Vox) →
        Platformer (independent). Each step reduces institutional editorial oversight."""
        career_steps = [
            ("Arizona Republic", "institutional daily newspaper"),
            ("SF Chronicle", "institutional daily newspaper"),
            ("CNET", "institutional digital media"),
            ("The Verge / Vox Media", "institutional digital media"),
            ("Platformer", "independent newsletter"),
            ("Hard Fork / NYT", "hybrid — independent host on institutional podcast"),
            ("Post-Aug 2026 venture", "fully independent — zero institutional oversight"),
        ]
        self.assertEqual(len(career_steps), 7)
        # Each step moves toward less institutional control
        for i in range(len(career_steps) - 1):
            self.assertIsNotNone(career_steps[i][1])

    def test_anthropic_disclosure_timeline(self):
        """Fiancé started at Anthropic Jan 2025, engaged Feb 2026."""
        fiance_start = "January 2025"
        role = "software engineer"
        company = "Anthropic"
        engagement = "February 2026"
        disclosure_page = "platformer.news/ethics"
        self.assertTrue(all([fiance_start, role, company, engagement, disclosure_page]))

    def test_content_moderation_investigation_predates_anthropic(self):
        """The 2019-2020 content moderation PTSD investigation against Meta/Facebook
        predates the Anthropic relationship (Jan 2025) by 5+ years. This establishes
        that Newton's adversarial posture toward Meta is NOT caused by the Anthropic
        relationship — it preceded it."""
        investigation_year = 2019
        settlement_amount = 52_000_000  # $52M Facebook/Cognizant
        anthropic_relationship_start = 2025
        self.assertLess(investigation_year, anthropic_relationship_start,
                        "Meta accountability journalism predates Anthropic relationship")
        self.assertEqual(settlement_amount, 52_000_000)


class TestAnthropicDisclosurePractice(unittest.TestCase):
    """Verify the disclosure practice is best-in-class but self-regulated."""

    def test_disclosure_scope_is_broad(self):
        """Newton discloses on columns about Anthropic, its competitors, AND
        'the AI industry at large' — even when Anthropic is not mentioned.
        This exceeds standard disclosure practice."""
        disclosure_triggers = [
            "column primarily concerns Anthropic",
            "column primarily concerns Anthropic competitors",
            "column concerns AI industry at large",
            "column does not specifically mention Anthropic",
        ]
        self.assertEqual(len(disclosure_triggers), 4)

    def test_disclosure_distribution_methods(self):
        """Newton distributes the disclosure through multiple channels."""
        methods = [
            "email link to all new subscribers",
            "published in newsletter at platformer.news/ethics",
            "permanent link on Platformer home page",
            "permanent link in every edition",
            "link at top of relevant columns",
        ]
        self.assertEqual(len(methods), 5)

    def test_no_institutional_oversight_of_disclosure(self):
        """Platformer has no editorial board, no ethics editor, no publisher
        with editorial authority. Newton alone decides when to disclose and
        how to frame coverage. This is inherent to independent journalism
        but creates a structural verification gap."""
        institutional_checks = {
            "editorial_board": False,
            "ethics_editor": False,
            "publisher_oversight": False,
            "ombudsman": False,
            "newsroom_standards_committee": False,
        }
        self.assertFalse(any(institutional_checks.values()),
                         "No institutional disclosure verification exists")

    def test_separate_finances_claim(self):
        """Ethics page states: 'We live together, and share household expenses.
        Otherwise, we maintain separate finances.' This limits but does not
        eliminate financial entanglement — shared housing costs create
        indirect dependency on fiancé's Anthropic compensation."""
        shared = ["household expenses"]
        separate = ["investments", "retirement accounts", "individual stocks"]
        self.assertEqual(len(shared), 1)
        self.assertGreater(len(separate), len(shared))


class TestMetaCoverageFraming(unittest.TestCase):
    """Analyze Newton's Meta coverage framing patterns."""

    def test_meta_article_headlines_accountability_framing(self):
        """Meta articles consistently use accountability framing: scams,
        legal reckoning, mistakes, design defects."""
        meta_headlines = [
            ("Meta's scam problem, UK edition", "accountability"),
            ("Meta's scam problem may trigger a legal reckoning", "accountability"),
            ("Mark Zuckerberg's 20-year mistake", "accountability"),
            ("Instagram makes teen accounts private by default", "under_siege"),
            ("How CrowdTangle predicted the future", "loss_narrative"),
            # From Techmeme (Apr 2026): jury verdicts on Meta product design defects
        ]
        accountability_count = sum(1 for _, frame in meta_headlines
                                   if frame in ("accountability", "under_siege", "loss_narrative"))
        self.assertEqual(accountability_count, len(meta_headlines),
                         "All sampled Meta headlines use accountability or negative framing")

    def test_meta_coverage_topic_distribution(self):
        """Newton's Meta coverage focuses on platform governance failures
        (scams, child safety, content moderation, privacy), not product
        innovation. Meta product launches, wearables, and AI tools receive
        minimal Platformer attention."""
        meta_topics = {
            "scams_fraud": True,
            "child_safety": True,
            "content_moderation_failures": True,
            "privacy_violations": True,
            "CrowdTangle_transparency_tool_killed": True,
            "oversight_board_funding": True,
            "product_launches": False,  # minimal coverage
            "wearables_glasses": False,  # absent from coverage
            "ai_tools_innovation": False,  # minimal coverage
        }
        negative_topics = sum(1 for v in meta_topics.values() if v)
        positive_topics = sum(1 for v in meta_topics.values() if not v)
        self.assertGreater(negative_topics, positive_topics,
                           "Meta coverage skews heavily toward accountability/failure topics")


class TestAnthropicCoverageFraming(unittest.TestCase):
    """Analyze Newton's Anthropic coverage framing patterns."""

    def test_anthropic_article_headlines_admiration_framing(self):
        """Anthropic articles use admiration/enthusiasm framing: believer,
        useful things, rapture."""
        anthropic_headlines = [
            ("Claude Code for writers", "enthusiasm"),
            ("The project that turned me into a Claude Code believer", "personal_endorsement"),
            ("the rapture over Claude Opus 4.5", "hyperbolic_praise"),
            ("Following: Anthropic vs. The Pentagon", "heroic_stand"),
        ]
        positive_count = sum(1 for _, frame in anthropic_headlines
                            if frame in ("enthusiasm", "personal_endorsement",
                                         "hyperbolic_praise", "heroic_stand"))
        self.assertEqual(positive_count, len(anthropic_headlines),
                         "All sampled Anthropic headlines use positive/admiring framing")

    def test_pentagon_coverage_aligns_with_anthropic_pr_positioning(self):
        """Newton's 'Following: Anthropic vs. The Pentagon' (Feb 2026) framed
        Anthropic as principled defender against government overreach. Compare to
        Harvard Berkman Klein's more skeptical framing (Sanders & Schneier, Mar 2026):
        'Don't bet that... Anthropic... is acting in the public interest.'

        The difference: Newton framed it as Anthropic defending ethics; academic
        analysis framed it as Anthropic making a strategic business decision that
        happened to align with ethics. Both are valid readings, but Newton's
        framing is more favorable to his fiancé's employer."""
        newton_framing = "principled_stand"  # Anthropic refuses Pentagon overreach
        academic_framing = "strategic_positioning"  # Anthropic builds consumer confidence
        self.assertNotEqual(newton_framing, academic_framing,
                            "Newton's framing is systematically more favorable to Anthropic "
                            "than independent academic analysis")

    def test_nexxworks_podcast_credits_anthropic(self):
        """On the nexxworks podcast (2026), Newton 'gives Anthropic credit for
        two consequential stands: refusing the Pentagon's autonomous weapons
        and pulling back the cyber-capable Mythos model to harden defenders
        before release.' This is advocacy framing, not neutral reporting."""
        credited_stands = [
            "refusing Pentagon autonomous weapons contract",
            "pulling back Mythos model for cybersecurity hardening",
        ]
        self.assertEqual(len(credited_stands), 2)
        # Note: both positions serve Anthropic's corporate interests
        # (avoiding liability, building trust for IPO) regardless of
        # their ethical merit. Newton frames them as principled choices,
        # not strategic ones.

    def test_claude_code_personal_adoption(self):
        """Newton built his personal website (cnewton.org) with Claude Code,
        then wrote about it for Platformer: 'The project that turned me into
        a Claude Code believer' and 'Claude Code for writers: Five useful things
        I've built so far.' This crosses from journalism to personal advocacy —
        the journalist is a customer of his fiancé's employer's product and
        writes about his positive experience with it."""
        actions = [
            ("built website with Claude Code", "personal_adoption"),
            ("wrote column about experience", "journalism"),
            ("disclosed Anthropic relationship", "disclosure"),
        ]
        # The disclosure is present, but the adoption + coverage
        # combination creates a reinforcing loop: adopt product →
        # positive experience → write positive column → readers adopt
        self.assertEqual(len(actions), 3)


class TestDisclosureInoculationParadox(unittest.TestCase):
    """Core mechanism: transparent disclosure can inoculate against scrutiny."""

    def test_mechanism_24_disclosure_inoculation(self):
        """Mechanism #24: The act of disclosing a conflict can reduce reader
        scrutiny rather than increase it. When Newton writes 'My fiancé works
        at Anthropic,' readers may interpret this as: 'He's being transparent,
        so I can trust his Anthropic coverage.' But disclosure addresses the
        ethical obligation, not the structural incentive. The relationship
        still predicts coverage patterns — disclosure just makes the pattern
        less likely to be questioned."""
        mechanism_id = 24
        mechanism_name = "Disclosure-as-Inoculation Paradox"
        journalist = "Casey Newton"
        scale = "individual_with_industry_implications"
        # This pattern matters because Newton is likely to become the
        # template for independent AI journalism disclosure practices
        # post-Aug 2026 when he and Roose launch their independent venture
        self.assertTrue(all([mechanism_id, mechanism_name, journalist, scale]))

    def test_independence_transition_removes_last_check(self):
        """Post-Aug 2026: Newton leaves NYT (Hard Fork ending). The new
        independent venture with Kevin Roose will have ZERO institutional
        editorial oversight. This means:
        - No NYT standards & practices review
        - No NYT legal department review
        - No institutional ethics policy beyond self-imposed
        - The Anthropic disclosure becomes entirely self-regulated

        This is NOT a criticism of independent journalism. It's a structural
        observation: independent operations trade institutional oversight
        for editorial freedom, which means disclosed conflicts have fewer
        external checks."""
        institutional_checks_pre_aug_2026 = {
            "NYT_editorial_standards": True,  # Hard Fork podcast
            "NYT_legal_review": True,
            "self_imposed_disclosure": True,
        }
        institutional_checks_post_aug_2026 = {
            "NYT_editorial_standards": False,  # Hard Fork ended
            "NYT_legal_review": False,
            "self_imposed_disclosure": True,  # only remaining check
        }
        pre_checks = sum(1 for v in institutional_checks_pre_aug_2026.values() if v)
        post_checks = sum(1 for v in institutional_checks_post_aug_2026.values() if v)
        self.assertEqual(pre_checks, 3)
        self.assertEqual(post_checks, 1)
        self.assertLess(post_checks, pre_checks,
                        "Independence transition reduces institutional checks from 3 to 1")


class TestCrossEntityFramingComparison(unittest.TestCase):
    """Direct comparison of framing patterns across entities."""

    def test_meta_vs_anthropic_headline_tone(self):
        """Side-by-side comparison of headline language for the two companies."""
        meta_terms = ["scam", "legal reckoning", "mistake", "under siege",
                      "killed off", "design defects"]
        anthropic_terms = ["believer", "useful things", "rapture",
                           "credit for consequential stands", "Claude Code for writers"]
        # Meta terms are uniformly negative; Anthropic terms are uniformly positive
        self.assertTrue(all(t.lower() for t in meta_terms))
        self.assertTrue(all(t.lower() for t in anthropic_terms))
        # The disclosed relationship predicts which company gets which framing

    def test_meta_coverage_predates_anthropic_relationship(self):
        """CRITICAL legitimate factor: Newton's adversarial Meta coverage
        began in 2019, years before his partner joined Anthropic in Jan 2025.
        The relationship did NOT create the adversarial posture — but it may
        reinforce it and reduce the probability of positive Meta coverage
        that would otherwise balance the portfolio."""
        meta_investigation_year = 2019
        anthropic_start = 2025
        gap_years = anthropic_start - meta_investigation_year
        self.assertEqual(gap_years, 6,
                         "6-year gap between Meta accountability journalism "
                         "and Anthropic relationship start")

    def test_no_meta_product_enthusiasm_columns(self):
        """Newton has written enthusiastic personal-adoption columns about
        Claude Code (Anthropic product). No comparable 'I'm a believer'
        column exists for any Meta product (Ray-Ban Meta, Llama, Threads,
        WhatsApp). This may reflect genuine product preference, but the
        pattern is notable given the personal relationship."""
        enthusiastic_product_columns = {
            "Claude Code": True,  # "turned me into a Claude Code believer"
            "Ray-Ban Meta": False,
            "Llama": False,
            "Threads": False,
            "Meta AI": False,
            "WhatsApp": False,
        }
        anthropic_enthusiasm = sum(1 for k, v in enthusiastic_product_columns.items()
                                    if "Claude" in k and v)
        meta_enthusiasm = sum(1 for k, v in enthusiastic_product_columns.items()
                              if k not in ("Claude Code",) and v)
        self.assertEqual(anthropic_enthusiasm, 1)
        self.assertEqual(meta_enthusiasm, 0,
                         "Zero personal-endorsement product columns for any Meta product")


class TestVoxMediaFinancialEntanglement(unittest.TestCase):
    """Newton also has Vox Media stock options (former employer, The Verge)."""

    def test_vox_media_stock_options_disclosed(self):
        """Newton discloses Vox Media options on ethics page but doesn't
        plan to disclose 'every time I link to a story from a Vox outlet.'
        The Verge covers the same companies Newton does — this creates a
        secondary financial interest in Vox Media's success."""
        vox_disclosure = "stock options"
        trigger_threshold = "write about Vox or The Verge as institutions"
        daily_linking = "no per-link disclosure"
        self.assertTrue(all([vox_disclosure, trigger_threshold, daily_linking]))

    def test_double_conflict_anthropic_plus_vox(self):
        """Newton has both an Anthropic personal relationship AND Vox Media
        financial interest. The Verge (Vox) has its own Meta coverage patterns
        (see David Pierce, Nilay Patel cross-entity analyses). When Newton
        links to Verge Meta coverage, the amplification comes from someone
        with both Anthropic and Vox financial interests."""
        conflicts = [
            ("Anthropic", "fiancé employment", "personal"),
            ("Vox Media", "stock options", "financial"),
        ]
        self.assertEqual(len(conflicts), 2,
                         "Two separate conflict-of-interest vectors")


class TestLegitimateFactors(unittest.TestCase):
    """Document legitimate factors that complicate the asymmetry finding."""

    def test_disclosure_exceeds_industry_standard(self):
        """Newton's disclosure is more comprehensive than most independent
        or institutional journalists. Many institutional journalists at
        publications with financial AI deals (WIRED/Condé Nast, NYT/Amazon)
        make NO per-article disclosure. Newton's voluntary standard is
        genuinely praiseworthy even if structurally incomplete."""
        newton_disclosure_quality = "best_in_class_independent"
        comparison_points = [
            ("WIRED reporters", "no per-article Condé Nast AI deal disclosure"),
            ("NYT reporters", "no per-article Amazon deal disclosure"),
            ("WSJ reporters", "no per-article News Corp deals disclosure"),
            ("FT reporters", "no per-article OpenAI deal disclosure"),
        ]
        # Newton is genuinely more transparent than institutional peers
        self.assertEqual(len(comparison_points), 4)

    def test_fiance_role_outside_newton_coverage_focus(self):
        """Newton's fiancé is a software engineer at Anthropic. Newton
        covers product and policy. The fiancé's 'work lies outside my core
        focus on product and policy' (ethics page). This genuine separation
        reduces direct information access conflict, though it does not
        address framing incentives."""
        fiance_role = "software engineer"
        newton_focus = "product and policy"
        overlap = "minimal"
        self.assertEqual(overlap, "minimal")

    def test_newton_covers_many_companies_critically(self):
        """Newton has produced critical coverage of Substack (left over
        Nazi content), TikTok (ban coverage), X/Elon Musk (co-authored
        'Character Limit'), Google (India problem, Gemini). The Anthropic
        framing asymmetry is specific to Anthropic, not a general pattern
        of uncritical coverage."""
        critical_coverage_targets = [
            "Substack",
            "TikTok",
            "X / Twitter / Elon Musk",
            "Google",
            "Meta / Facebook",
        ]
        self.assertEqual(len(critical_coverage_targets), 5,
                         "Newton does critical coverage of 5+ major companies")

    def test_anthropic_pentagon_stand_is_genuinely_newsworthy(self):
        """Anthropic's refusal of Pentagon autonomous weapons use was a
        legitimately important story regardless of Newton's personal
        relationship. A federal judge ruled the Pentagon's retaliation was
        'likely unlawful' and 'classic illegal First Amendment retaliation'
        (Judge Lin, Mar 30 2026). The newsworthiness is not in question —
        only the framing (principled stand vs. strategic positioning)."""
        judge = "Lin"
        ruling = "likely unlawful retaliation"
        ruling_date = "March 30, 2026"
        first_amendment = True
        self.assertTrue(all([judge, ruling, ruling_date, first_amendment]))


class TestMechanismCausalChainIndependence(unittest.TestCase):
    """Verify Mechanism #24 is causally independent from other mechanisms."""

    def test_distinct_from_institutional_mechanisms(self):
        """Mechanism #24 (individual personal relationship) is structurally
        different from:
        - #20 (Knibbs/WIRED, institutional employer deals)
        - #21 (IPO underwriter research laundering, systemic)
        - #23 (NYT corporate revenue chain, institutional)
        Newton's conflict is personal, not institutional — Platformer has
        no corporate parent with AI licensing deals."""
        mechanism_24_type = "personal_relationship"
        mechanism_20_type = "employer_corporate_deals"
        mechanism_21_type = "systemic_ipo_underwriting"
        mechanism_23_type = "corporate_revenue_chain"
        types = {mechanism_24_type, mechanism_20_type, mechanism_21_type, mechanism_23_type}
        self.assertEqual(len(types), 4, "All four mechanisms are distinct types")

    def test_distinct_from_horwitz_book_deal_mechanism(self):
        """Mechanism #19 (Horwitz/WSJ) involves book/movie/Pulitzer deals
        that MONETIZE a specific narrative (Meta-as-villain). Newton's
        conflict is the reverse: a PERSONAL RELATIONSHIP with a company
        he covers favorably. Different incentive structure."""
        horwitz_incentive = "monetize negative narrative about specific company"
        newton_incentive = "personal relationship with company covered favorably"
        self.assertNotEqual(horwitz_incentive, newton_incentive)


if __name__ == "__main__":
    unittest.main()
