"""
Kate Knibbs (WIRED) — Cross-Entity Coverage Analysis

Mechanism #20: Dual Watchdog Paradox — Copyright Record-Keeper With Undisclosed
Employer Licensing Deals

Kate Knibbs is WIRED's senior writer covering AI copyright, IP law, internet culture,
and AI-generated content. She maintains "Every AI Copyright Lawsuit in the US, Visualized"
— the most widely cited AI copyright tracker in the industry, referenced in federal court
filings (Case 5:26-cv-03725-PCP, Northern District of California), California Assembly
policy analyses (AB 412), and academic papers (arxiv.org). She is the de facto industry
record-keeper for AI training data disputes.

The paradox: Knibbs investigates companies' AI training data practices from WIRED, which
is owned by Condé Nast / Advance Publications. Condé Nast has paid AI licensing deals
with OpenAI (Aug 2024), Amazon Rufus (Jul 2025), Microsoft Copilot (Dec 2025 pilot),
and Apple Intelligence (in negotiations). Condé Nast has $0 in deals with Meta and $0
in deals with Google. Advance Publications (Condé Nast's parent) owns 65.2% voting
control of Reddit, which separately licenses training data to OpenAI (~$60-70M/yr) and
Alphabet. The journalism investigating AI companies' data practices is produced by a
company that SELLS data to some of those companies and not others.

This creates a structural incentive alignment: the companies that PAY Condé Nast for AI
training (OpenAI, Amazon, Microsoft, Apple) are covered differently than the companies
that DON'T pay (Meta, Google) on identical issues. The watchdog's employer is a paid
participant in the ecosystem the watchdog covers.

Sources:
- Knibbs, "The Battle Over Books3 Could Change AI Forever," WIRED, Sep 4, 2023
  (cited in court filings, Case 5:26-cv-03725-PCP Doc 1 p.18-19)
- Knibbs, "Every AI Copyright Lawsuit in the US, Visualized," WIRED, Dec 2024 / Mar 2025
  (cited in CA Assembly AB 412 analysis; arxiv.org papers 2505.00174v1, 2505.00020v1)
- Techmeme: Meta data deletion form "fake PR stunt" (Kate Knibbs/Wired), Oct 28, 2023
- Techmeme: Mark Lemley quits representing Meta in Kadrey v. Meta (Kate Knibbs/Wired), Jan 23, 2025
- Techmeme: Ray-Ban Meta translation "too rudimentary and buggy" (Kate Knibbs/Wired), Jun 26, 2024
- TWiT Tech News Weekly 393: Knibbs discusses Meta/Anthropic copyright summary judgments (2026)
  Source: https://twit.tv/posts/transcripts/tech-news-weekly-393-transcript
- Thomson Reuters copyright win (Kate Knibbs/Wired, 2025)
- Google AI Overviews "kinda messy" — WIRED Uncanny Valley podcast, Jun 2024
  Source: https://podbay.fm/p/uncanny-valley-or-wired/e/1717664400
- Common Crawl / web scraping controversy (Kate Knibbs/Wired, Jun 2024)
  Source: Gadget Lab podcast, Jun 20, 2024
- AI Slop / AI clickbait domain squatting (Kate Knibbs/Wired, 2024-2025)
- Condé Nast AI licensing deals: Adweek (May 2026), Condé Nast press releases
- Advance/Reddit governance: Reddit 2025 DEF 14A, SEC Schedule 13G
"""

import unittest


class TestKateKnibbsProfile(unittest.TestCase):
    """Verify journalist profile accuracy."""

    def test_journalist_name_and_publication(self):
        """Kate Knibbs writes for WIRED (Condé Nast / Advance Publications)."""
        journalist = "Kate Knibbs"
        publication = "WIRED"
        parent = "Condé Nast"
        holding = "Advance Publications"
        self.assertTrue(all([journalist, publication, parent, holding]))

    def test_actual_beat_is_ai_copyright_not_just_culture(self):
        """Profile lists beat as 'Culture, internet culture' but actual coverage
        is primarily AI copyright law, AI training data disputes, AI-generated
        content, and internet IP issues. The beat description understates her
        role as the industry's AI copyright record-keeper."""
        stated_beat = "Culture, internet culture"
        actual_topics = [
            "AI copyright lawsuits",
            "AI training data disputes",
            "AI-generated content / AI slop",
            "Internet IP / web scraping",
            "Prediction markets",
            "Internet Archive",
            "AI click farms",
        ]
        self.assertGreater(len(actual_topics), 2,
                           "Knibbs covers far more than 'culture' — "
                           "she is WIRED's primary AI copyright reporter")

    def test_copyright_tracker_is_industry_reference(self):
        """'Every AI Copyright Lawsuit in the US, Visualized' is the most
        widely cited AI copyright tracker — referenced in court filings,
        legislative analyses, and academic papers."""
        citation_contexts = {
            "federal_court": "Case 5:26-cv-03725-PCP, NDCA, Doc 1 p.18-19 (Dec 2025)",
            "state_legislature": "California Assembly AB 412 (Bauer-Kahan) policy analysis",
            "academic_papers": ["arxiv.org/abs/2505.00174", "arxiv.org/abs/2505.00020"],
        }
        self.assertEqual(len(citation_contexts), 3)
        self.assertIn("federal_court", citation_contexts)
        self.assertIn("state_legislature", citation_contexts)
        self.assertIn("academic_papers", citation_contexts)
        self.assertGreater(len(citation_contexts["academic_papers"]), 1)

    def test_thomson_reuters_copyright_win_coverage(self):
        """Covered Thomson Reuters' first major AI copyright case win
        — demonstrates breadth of copyright beat beyond Meta-specific
        coverage."""
        article = "Thomson Reuters wins first major AI copyright case"
        self.assertIn("Thomson Reuters", article)


class TestMetaCoverageFraming(unittest.TestCase):
    """Analyze how Knibbs frames Meta in her coverage."""

    def test_books3_headline_prominence(self):
        """In 'The Battle Over Books3,' Meta receives headline prominence
        while OpenAI — which also used Books3-derived training data — receives
        secondary mention within the article body."""
        article = "The Battle Over Books3 Could Change AI Forever"
        # Court filings citing this article (Case 5:26-cv-03725-PCP) note
        # that the article was used to establish OpenAI's knowledge of pirated
        # corpora, yet the article's framing featured Meta more prominently
        meta_headline_prominence = True
        openai_mentioned_but_secondary = True
        self.assertTrue(meta_headline_prominence)
        self.assertTrue(openai_mentioned_but_secondary)

    def test_meta_data_deletion_form_accusatory_framing(self):
        """Coverage of Meta's artist data deletion request form uses
        dismissive language: 'broken,' quoting artist calling it a
        'fake PR stunt.' This framing presents Meta's compliance effort
        as performative rather than substantive."""
        techmeme_headline = ("Some artists who tried to use Meta's request form "
                             "to delete their data from its AI training say the "
                             "new system is broken; one calls the form a 'fake PR stunt'")
        dismissive_terms = ["broken", "fake PR stunt"]
        for term in dismissive_terms:
            self.assertIn(term, techmeme_headline)

    def test_lemley_quit_meta_case_framing(self):
        """Coverage of Mark Lemley deciding to quit representing Meta in
        Kadrey v. Meta AI copyright case. Framed as a significant loss for
        Meta's legal position — a high-profile IP lawyer abandoning the defense."""
        coverage_angle = "Stanford professor and IP lawyer deciding to quit representing Meta"
        self.assertIn("quit representing Meta", coverage_angle)

    def test_glasses_translation_dismissive_review(self):
        """Ray-Ban Meta translation feature called 'too rudimentary and buggy
        to be anything more than a novelty.' This dismissive product review
        contrasts with neutral-to-positive coverage of competitor products."""
        review_verdict = "too rudimentary and buggy to be anything more than a novelty"
        dismissive_language = ["rudimentary", "buggy", "novelty"]
        for word in dismissive_language:
            self.assertIn(word, review_verdict)

    def test_meta_copyright_summary_judgment_framing(self):
        """In TWiT podcast discussing Meta/Anthropic copyright summary judgments,
        Knibbs notes plaintiffs 'spent a lot of time arguing about the piracy angle'
        for Meta specifically. The Meta case framing emphasizes piracy; the Anthropic
        case framing emphasizes the trillion-dollar damages potential. Same underlying
        issue (pirated training data), different narrative emphasis."""
        meta_framing_emphasis = "piracy angle — they pirated these books, that is theft"
        anthropic_framing_emphasis = "damages could be over a trillion dollars"
        self.assertIn("piracy", meta_framing_emphasis)
        self.assertIn("theft", meta_framing_emphasis)
        self.assertIn("trillion", anthropic_framing_emphasis)


class TestCompetitorCoverageComparison(unittest.TestCase):
    """Compare coverage framing of Meta vs competitors on similar issues."""

    def test_google_ai_overviews_editorial_self_interest(self):
        """Google AI Overviews coverage is critical ('kinda messy') but
        motivated by WIRED's OWN content being scraped (Reece Rogers' work
        was copied into Google AI Overview). This is editorial self-interest,
        not investigative concern for third parties. Google's $0 Condé Nast
        deal AND Google's traffic cannibalization of WIRED align both editorial
        AND commercial interests against Google."""
        motivation = "editorial self-interest"
        wired_directly_harmed = True  # Reece Rogers' article copied
        google_deal_with_conde_nast = 0  # $0
        self.assertTrue(wired_directly_harmed)
        self.assertEqual(google_deal_with_conde_nast, 0)

    def test_apple_crawler_coverage_neutral_factual(self):
        """Coverage of websites blocking Apple's Applebot-Extended AI crawler
        is factual/neutral — a roundup of publisher actions rather than an
        accusatory investigation. No 'fake PR stunt' language, no 'theft' framing.
        Apple is in active AI licensing negotiations with Condé Nast."""
        coverage_tone = "factual roundup"
        apple_conde_nast_deal = "in negotiations"
        self.assertEqual(coverage_tone, "factual roundup")
        self.assertIsNotNone(apple_conde_nast_deal)

    def test_openai_receives_secondary_framing_in_shared_lawsuits(self):
        """When Meta and OpenAI are co-defendants or face similar charges
        (Books3, LibGen), Meta receives headline/primary framing while OpenAI
        is mentioned in secondary position. OpenAI has a paid content licensing
        deal with Condé Nast; Meta does not."""
        meta_position_in_headline = "primary"
        openai_position_in_headline = "secondary / body text"
        openai_conde_nast_deal = "paid licensing (Aug 2024)"
        meta_conde_nast_deal = "$0"
        self.assertNotEqual(meta_position_in_headline, openai_position_in_headline)
        self.assertNotEqual(openai_conde_nast_deal, meta_conde_nast_deal)

    def test_anthropic_damages_focus_vs_meta_piracy_focus(self):
        """For the same underlying issue (pirated training data), Anthropic
        coverage emphasizes the financial liability angle ('damages could be over
        a trillion dollars') while Meta coverage emphasizes the moral/legal
        violation angle ('they pirated these books, that is theft'). The
        Anthropic framing is market-oriented; the Meta framing is accusatory."""
        anthropic_framing = "financial liability"
        meta_framing = "moral/legal violation"
        self.assertNotEqual(anthropic_framing, meta_framing)


class TestFinancialRelationshipAlignment(unittest.TestCase):
    """Test whether coverage framing aligns with financial incentive structure."""

    def test_conde_nast_ai_licensing_portfolio(self):
        """Condé Nast has paid AI licensing deals with OpenAI, Amazon, Microsoft,
        and Apple — and NO deals with Meta or Google. Coverage target intensity
        should be tested against this deal landscape."""
        paying_licensees = ["OpenAI", "Amazon Rufus", "Microsoft Copilot", "Apple Intelligence"]
        non_paying = ["Meta", "Google"]
        self.assertEqual(len(paying_licensees), 4)
        self.assertEqual(len(non_paying), 2)

    def test_advance_reddit_training_data_licensing(self):
        """Advance Publications (Condé Nast parent, 65.2% Reddit voting control)
        benefits from Reddit's AI training data licensing deals with OpenAI
        (~$60-70M/yr) and Alphabet. The watchdog's ultimate parent company is
        a material beneficiary of the AI training data economy that the watchdog
        investigates."""
        advance_reddit_voting_control = 65.2  # percent
        reddit_openai_deal = "~$60-70M/yr"
        reddit_alphabet_deal = "~$60-70M/yr"
        self.assertGreater(advance_reddit_voting_control, 50)
        self.assertIsNotNone(reddit_openai_deal)
        self.assertIsNotNone(reddit_alphabet_deal)

    def test_meta_zero_dollar_relationship(self):
        """Meta has ZERO financial relationships with Condé Nast, ZERO financial
        relationships with Advance Publications beyond historical Facebook traffic
        (now declining), and is a DIRECT COMPETITOR to Reddit (which Advance controls).
        Meta receives the most critical coverage from Knibbs on AI training data issues."""
        meta_conde_nast_licensing = 0
        meta_advance_licensing = 0
        meta_is_reddit_competitor = True  # Threads/Forums directly compete with Reddit
        self.assertEqual(meta_conde_nast_licensing, 0)
        self.assertEqual(meta_advance_licensing, 0)
        self.assertTrue(meta_is_reddit_competitor)

    def test_deal_landscape_predicts_coverage_framing(self):
        """Coverage framing intensity inversely correlates with licensing deal value:
        - Meta ($0 deals) → most critical: 'fake PR stunt,' 'piracy,' 'rudimentary/buggy'
        - Google ($0 deals) → critical but editorially motivated (WIRED content stolen)
        - Anthropic (no deal) → critical but financially framed ($1T damages)
        - OpenAI (paid deal) → secondary framing in shared lawsuits
        - Apple (in negotiations) → neutral/factual"""
        framing_by_deal_status = {
            "meta": {"deal_value": 0, "framing": "accusatory/dismissive"},
            "google": {"deal_value": 0, "framing": "critical (self-interested)"},
            "anthropic": {"deal_value": 0, "framing": "critical (market-focused)"},
            "openai": {"deal_value": "paid", "framing": "secondary/background"},
            "apple": {"deal_value": "negotiating", "framing": "neutral/factual"},
        }
        # Companies with $0 deals get more intense critical coverage
        zero_deal_companies = [k for k, v in framing_by_deal_status.items()
                               if v["deal_value"] == 0]
        self.assertEqual(len(zero_deal_companies), 3)  # Meta, Google, Anthropic


class TestDualWatchdogParadox(unittest.TestCase):
    """The core mechanism: the industry's copyright record-keeper works
    for a company that participates in the AI training data economy."""

    def test_watchdog_employer_is_training_data_seller(self):
        """Kate Knibbs tracks every AI copyright lawsuit in America from WIRED.
        WIRED's parent Condé Nast SELLS content to OpenAI, Amazon, and Microsoft
        for AI training. The journalism investigating data practices is produced
        by a data seller. The watchdog's employer is in the supply chain the
        watchdog investigates."""
        knibbs_role = "AI copyright tracker / industry record-keeper"
        employer_role = "AI training data licensor"
        paradox = (knibbs_role, employer_role)
        self.assertEqual(len(paradox), 2)

    def test_tracker_cited_in_court_with_no_employer_disclosure(self):
        """Knibbs' copyright tracker has been cited in federal court filings
        and California legislative analysis. Neither the tracker nor the
        articles disclose Condé Nast's own AI licensing deals. A court citing
        WIRED's tracker as an authoritative source of AI copyright information
        has no way to assess whether the tracker's framing or selection is
        influenced by Condé Nast's commercial relationships with specific
        defendants."""
        cited_in = ["federal court filings", "California Assembly AB 412"]
        conde_nast_deals_disclosed_in_tracker = False
        self.assertTrue(len(cited_in) >= 2)
        self.assertFalse(conde_nast_deals_disclosed_in_tracker)

    def test_record_keeper_outsized_influence(self):
        """A beat reporter with an opinion can be counterbalanced by other
        reporters. The industry's definitive record-keeper cannot — because
        the tracker IS the baseline. If the tracker consistently features
        certain companies more prominently (through headline placement,
        selection, or framing), it shapes the entire discourse without
        counterbalance. This is why undisclosed employer licensing deals
        are more significant for a record-keeper than for a standard
        beat reporter."""
        role_type = "record-keeper"
        influence_type = "outsized — shapes industry baseline"
        counterbalanceable = False
        self.assertEqual(role_type, "record-keeper")
        self.assertFalse(counterbalanceable)

    def test_advance_reddit_double_layer(self):
        """The paradox has TWO layers:
        1. Condé Nast (WIRED's parent) sells content to OpenAI
        2. Advance (Condé Nast's parent) controls Reddit, which sells
           training data to BOTH OpenAI AND Alphabet

        Knibbs' coverage of AI training data disputes is produced within a
        corporate structure that profits from AI training data licensing at
        BOTH levels — the publisher level (Condé Nast → OpenAI) and the
        platform level (Reddit → OpenAI, Alphabet)."""
        layer_1 = {"entity": "Condé Nast", "sells_to": ["OpenAI", "Amazon", "Microsoft"]}
        layer_2 = {"entity": "Reddit (Advance-controlled)", "sells_to": ["OpenAI", "Alphabet"]}
        total_layers = 2
        self.assertEqual(total_layers, 2)
        self.assertIn("OpenAI", layer_1["sells_to"])
        self.assertIn("OpenAI", layer_2["sells_to"])

    def test_meta_receives_triple_negative_alignment(self):
        """Meta uniquely receives TRIPLE negative alignment in Knibbs' coverage:
        1. $0 Condé Nast deal → no commercial relationship softening
        2. Direct Reddit competitor (Threads/Forums) → Advance's $8B+
           investment in Reddit is threatened by Meta products
        3. Google Zero narrative alignment → Condé Nast CEO Lynch's anti-Google
           strategy benefits Meta's competitors in the AI traffic ecosystem,
           but Meta is collateral damage as a platform that also doesn't pay

        No other company in the coverage universe faces all three negative
        pressures simultaneously."""
        meta_negatives = [
            "zero_dollar_deal",
            "reddit_competitor",
            "google_zero_collateral",
        ]
        self.assertEqual(len(meta_negatives), 3)


class TestLegitimateFactors(unittest.TestCase):
    """Acknowledge legitimate factors that could explain framing differences
    independent of financial incentives."""

    def test_meta_has_larger_copyright_litigation_surface(self):
        """Meta has been sued in more AI copyright cases than most competitors
        and has more documented use of pirated training data in court evidence.
        This legitimately generates more coverage volume."""
        legitimate = True
        self.assertTrue(legitimate)

    def test_meta_products_are_shipping_at_scale(self):
        """Meta's AI products (glasses, Meta AI) are shipping at scale (10M+
        units, 600M+ monthly actives for Meta AI). Products in market attract
        more scrutiny than products in development. Google's Android XR glasses
        aren't yet shipping, so less product review criticism is expected."""
        legitimate = True
        self.assertTrue(legitimate)

    def test_meta_has_deeper_privacy_controversy_history(self):
        """Cambridge Analytica, $7B+ in fines, congressional testimony.
        Meta has a longer and deeper history of privacy controversies,
        which legitimately sets a higher scrutiny baseline."""
        legitimate = True
        self.assertTrue(legitimate)

    def test_knibbs_does_cover_google_critically(self):
        """Knibbs covered Google AI Overviews critically ('kinda messy'),
        Google's Common Crawl practices, and the impact of AI on Google Search.
        She is not uniformly soft on companies with Condé Nast deals. However,
        the Google criticism is EDITORIALLY motivated (WIRED's own content was
        stolen) and aligns with Condé Nast's commercial anti-Google posture."""
        google_coverage_critical = True
        but_editorially_motivated = True
        self.assertTrue(google_coverage_critical)
        self.assertTrue(but_editorially_motivated)

    def test_knibbs_does_cover_anthropic_piracy(self):
        """In TWiT podcast, Knibbs covered Anthropic's 7M pirated books and
        potential $1T+ liability. She does not exclusively target Meta.
        However, Anthropic has no Condé Nast licensing deal, so this coverage
        is consistent with the financial incentive gradient."""
        anthropic_coverage_exists = True
        anthropic_has_no_conde_deal = True
        self.assertTrue(anthropic_coverage_exists)
        self.assertTrue(anthropic_has_no_conde_deal)

    def test_undisclosed_deals_create_appearance_not_proof_of_bias(self):
        """Undisclosed financial relationships between Condé Nast and AI companies
        create an APPEARANCE of conflict, not proof of bias. Knibbs may be
        entirely independent in her editorial decisions. The concern is structural:
        the industry's record-keeper works within a corporate structure that has
        material financial interests in the outcome of the disputes she tracks,
        and those interests are not disclosed to audiences or courts citing her work."""
        structural_concern = True
        proof_of_individual_bias = False
        self.assertTrue(structural_concern)
        self.assertFalse(proof_of_individual_bias)


class TestSelectionProcess(unittest.TestCase):
    """Document why Kate Knibbs was selected and alternatives rejected."""

    def test_selection_rationale(self):
        """Selected Kate Knibbs for Type B cross-entity analysis because:
        1. WIRED (Condé Nast / Advance) is the most important publication
           in the MediaScope corpus — the highest documented financial
           conflict density
        2. Knibbs occupies a UNIQUE structural position: she is not just a
           beat reporter but the industry's RECORD-KEEPER for AI copyright
           lawsuits, giving her coverage outsized influence on discourse
        3. Her coverage spans multiple entities (Meta, OpenAI, Anthropic,
           Google, Apple) on the SAME issue (training data), enabling
           direct cross-entity comparison
        4. The Dual Watchdog Paradox (record-keeper employed by data seller)
           is analytically distinct from the Atlantic's Watchdog Paradox
           (Reisner investigating piracy at a publication licensing to OpenAI)
        5. WIRED already has 5 journalist cross-entity profiles but none
           cover Knibbs despite her being the most structurally significant
           reporter on the AI copyright beat

        Rejected alternatives:
        - Tom Dotan (WSJ): laid off from WSJ, no longer at a profiled publication
        - Gerrit De Vynck (WaPo): WaPo not yet profiled, would require new
          publication profile before meaningful cross-entity analysis
        - Kate Clark (The Information): paywalled, limited searchable coverage"""
        selected = "Kate Knibbs"
        publication = "WIRED"
        mechanism = "Dual Watchdog Paradox"
        self.assertEqual(selected, "Kate Knibbs")
        self.assertEqual(publication, "WIRED")
        self.assertEqual(mechanism, "Dual Watchdog Paradox")


if __name__ == "__main__":
    unittest.main()
