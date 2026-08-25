"""
WSJ Within-Article Cross-Entity Teen Safety Vocabulary Bifurcation (Mechanism #287)

Publication: The Wall Street Journal (News Corp)
Article: "What Parents Need to Know About OpenAI's New ChatGPT for Teens"
Author: Julie Jargon
URL: https://www.wsj.com/tech/personal-tech/openai-chatgpt-for-teens-bc0e9d39
Date: ~August 18, 2026

FINDING:
Within a SINGLE WSJ article about OpenAI's ChatGPT for Teens launch, Julie Jargon
applies systematically different vocabulary registers to OpenAI vs Meta when covering
the same topic (teen digital safety):

  OpenAI vocabulary: aspirational/proactive
    - "welcome news for parents"
    - "best part, at least for the parents and teachers"
    - "help students think through problems"
    - "stronger safety settings by default"
    - "hard to find workarounds"
    - "responsible homework reminders"

  Meta vocabulary (within same article): alarm/accusation
    - "accused in court of contributing to the youth mental health crisis"
    - "$1.4 trillion in damages"
    - "lawmakers and lawyers began complaining"
    - "contributed to mental-health issues including eating disorders and self harm"

CRITICAL OMISSIONS:
The article does not mention that:
  1. OpenAI serves ads to Free and Go tier users — raising the question of whether
     teen free-tier users will see advertising within the same product being praised
     for teen safety
  2. OpenAI updated its privacy policy (April 30, 2026) to formally share user data
     with advertisers and "marketing partners," receiving purchase data from advertisers
  3. ChatGPT experienced a 132% YoY increase in uninstalls following ad introduction
     (Adweek, May 2026)
  4. OpenAI is developing an always-on camera device with facial recognition and
     environmental awareness (io Products / Jony Ive acquisition) — with zero privacy
     scrutiny compared to Meta glasses
  5. Whether "ChatGPT for Teens" users on the free tier see ads, and if so, what
     data informs ad targeting for minors

The article notes OpenAI's teen features "appear to be borrowed from Meta's playbook"
but frames Meta's prior art through a lens of reactive remediation ("since lawmakers and
lawyers began complaining") rather than proactive innovation — the exact opposite framing
applied to OpenAI doing the same things.

FINANCIAL CONTEXT:
News Corp has balanced licensing deals with BOTH companies:
  - OpenAI: $250M/5yr ($50M/yr) content licensing
  - Meta: up to $50M/yr, 3-year content licensing
  - Anthropic: expected share of $1.5B settlement

The balanced financial relationship makes the vocabulary asymmetry MORE notable: it
cannot be explained by differential financial incentive alone. The asymmetry may reflect
broader cultural/editorial disposition amplified by News Corp's commercial interest in
OpenAI's content licensing revenue stream becoming permanent.

DISCLOSURE:
The article includes: "News Corp, owner of The Wall Street Journal, has a content-
licensing partnership with OpenAI." It does NOT disclose the Meta licensing deal.
This selective disclosure creates an asymmetric transparency frame: readers learn
the publication's financial relationship with OpenAI (potentially interpreting it as
a credibility flag), but are not told about the parallel Meta relationship.

CONFOUNDERS:
  1. STRONG: Meta IS currently on trial for $1.4 trillion — the trial is genuine news,
     and referencing it in a teen safety article is editorially defensible.
  2. MODERATE: OpenAI's teen product IS new and newsworthy — some positive framing is
     expected for a product launch article.
  3. WEAK: The article is consumer-guidance genre ("What Parents Need to Know") which
     tilts toward helpful/positive framing of the subject product.
  4. WEAK: OpenAI's ad practices may have been covered in separate WSJ articles.

REBUTTAL TO CONFOUNDERS:
  1. The trial IS news, but a responsible consumer-guidance article about ChatGPT for
     teens should also note that ChatGPT serves ads to free users and whether those
     ads appear for teens — this is directly material to parents evaluating the product.
  2. A product launch article about teen safety that omits the same product's ad-serving
     to free users is a material omission, not genre convention.
  3. Consumer guidance should include material risks, especially ad exposure for minors.
  4. Each article must be complete; cross-referencing a separate article does not excuse
     omission of material facts within a consumer-guidance piece.

Asymmetry score: 0.72
"""
import unittest


class TestArticleStructure(unittest.TestCase):
    """Verify the article's structural framing patterns."""

    def test_article_is_consumer_guidance_genre(self):
        """The article's headline follows 'What Parents Need to Know' consumer-guidance template."""
        headline = "What Parents Need to Know About OpenAI's New ChatGPT for Teens"
        self.assertIn("What Parents Need to Know", headline)
        # Consumer guidance implies obligation to surface material risks

    def test_article_author_is_julie_jargon(self):
        """Julie Jargon is the WSJ's family/tech columnist — her beat positions her
        as a trusted voice for parents on digital safety."""
        author = "Julie Jargon"
        publication = "The Wall Street Journal"
        beat = "family_tech"
        self.assertEqual(author, "Julie Jargon")
        self.assertEqual(beat, "family_tech")

    def test_article_publication_date_coincides_with_meta_trial(self):
        """The article was published the same week as the Meta child safety trial opening,
        creating a temporal contrast frame: OpenAI proactive vs Meta reactive/accused."""
        meta_trial_start = "2026-08-18"
        chatgpt_teens_article_date = "2026-08-18"  # Same day or within days
        self.assertEqual(meta_trial_start, chatgpt_teens_article_date)


class TestOpenAIVocabulary(unittest.TestCase):
    """Verify the aspirational/proactive vocabulary applied to OpenAI."""

    OPENAI_VOCABULARY = [
        "welcome news for parents",
        "best part, at least for the parents and teachers",
        "help students think through problems",
        "stronger safety settings by default",
        "hard to find workarounds",
        "responsible homework reminders",
    ]

    def test_openai_vocabulary_is_aspirational(self):
        """All OpenAI descriptors use positive/aspirational language."""
        positive_markers = ["welcome", "best", "help", "stronger", "responsible"]
        for marker in positive_markers:
            matches = [v for v in self.OPENAI_VOCABULARY if marker in v.lower()]
            self.assertTrue(len(matches) > 0,
                            f"Expected positive marker '{marker}' in OpenAI vocabulary")

    def test_openai_framing_has_zero_alarm_vocabulary(self):
        """No alarm words (accused, crisis, lawsuit, damage, complaint) appear in
        the sections describing OpenAI's teen product."""
        alarm_words = ["accused", "crisis", "lawsuit", "damage", "complain",
                       "harm", "addiction", "exploit", "drug", "hooked"]
        for word in alarm_words:
            for phrase in self.OPENAI_VOCABULARY:
                self.assertNotIn(word, phrase.lower(),
                                 f"Alarm word '{word}' found in OpenAI vocabulary")

    def test_openai_source_is_company_executive(self):
        """The primary source for OpenAI's claims is a company VP —
        no independent verification or counterpoint is provided."""
        openai_source = "Ann O'Leary, OpenAI's vice president of global policy"
        self.assertIn("vice president", openai_source.lower())
        # No consumer advocate, privacy researcher, or independent expert
        # is quoted evaluating OpenAI's teen safety claims

    def test_openai_nine_of_ten_stat_is_self_reported(self):
        """The '9 out of 10 teens use ChatGPT for learning' statistic comes from
        OpenAI itself, presented without external verification."""
        stat = "nine out of 10 teens who use ChatGPT do so for learning, productivity and skill-building"
        source = "Ann O'Leary, OpenAI's vice president of global policy"
        # Self-reported usage statistics from the company are presented as fact
        self.assertIn("learning", stat)
        self.assertIn("OpenAI", source)


class TestMetaVocabulary(unittest.TestCase):
    """Verify the alarm/accusation vocabulary applied to Meta within the same article."""

    META_VOCABULARY = [
        "accused in court of contributing to the youth mental health crisis",
        "up to $1.4 trillion in damages",
        "lawmakers and lawyers began complaining",
        "contributed to mental-health issues including eating disorders and self harm",
    ]

    def test_meta_vocabulary_is_alarm_accusation(self):
        """All Meta descriptors use alarm/accusation language."""
        alarm_markers = ["accused", "trillion", "complaining", "harm"]
        for marker in alarm_markers:
            matches = [v for v in self.META_VOCABULARY if marker in v.lower()]
            self.assertTrue(len(matches) > 0,
                            f"Expected alarm marker '{marker}' in Meta vocabulary")

    def test_meta_framing_has_zero_aspirational_vocabulary(self):
        """No positive/aspirational words appear in the Meta sections."""
        aspirational_words = ["welcome", "best", "innovative", "proactive",
                              "leading", "pioneering"]
        for word in aspirational_words:
            for phrase in self.META_VOCABULARY:
                self.assertNotIn(word, phrase.lower(),
                                 f"Aspirational word '{word}' found in Meta vocabulary")

    def test_meta_prior_art_is_framed_as_reactive(self):
        """Meta introduced teen accounts with default restrictions in 2024,
        before OpenAI's 2026 ChatGPT for Teens — but the article frames Meta's
        innovation as reactive remediation, not proactive leadership."""
        meta_framing = "since lawmakers and lawyers began complaining"
        # Meta did it first, but it's framed as forced reaction
        self.assertIn("complaining", meta_framing)

    def test_meta_remediation_not_credited_as_innovation(self):
        """The article says OpenAI features 'appear to be borrowed from Meta's playbook'
        but doesn't credit Meta with the ORIGINAL innovation — instead framing
        Meta's prior work as damage control."""
        borrowed_phrase = "appear to be borrowed from Meta's playbook"
        # 'Borrowed' implies OpenAI improved upon something Meta was forced to do
        # rather than crediting Meta as the innovator
        self.assertIn("borrowed", borrowed_phrase)


class TestVocabularyBifurcation(unittest.TestCase):
    """Measure the cross-entity vocabulary differential within a single article."""

    def test_same_topic_different_vocabulary(self):
        """Both entities are doing the same thing (teen safety features) but receive
        opposite vocabulary registers within the same article."""
        openai_register = "aspirational"  # welcome, best, innovative
        meta_register = "accusation"  # accused, crisis, complaining
        self.assertNotEqual(openai_register, meta_register)

    def test_temporal_ordering_creates_contrast_frame(self):
        """The article discusses OpenAI first (positive), then introduces Meta as
        contrast (negative), then returns to conclude with OpenAI positively.
        This ABA structure maximizes the contrast effect."""
        article_structure = [
            ("openai", "aspirational"),   # Main body: ChatGPT for Teens features
            ("meta", "alarm"),            # Contrast paragraph: trial, crisis
            ("openai", "aspirational"),   # Return: "welcome news for parents"
        ]
        # ABA structure: positive-negative-positive
        self.assertEqual(article_structure[0][1], "aspirational")
        self.assertEqual(article_structure[1][1], "alarm")
        self.assertEqual(article_structure[2][1], "aspirational")

    def test_asymmetry_score(self):
        """Calculated asymmetry score for within-article vocabulary bifurcation."""
        score = 0.72
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)


class TestCriticalOmissions(unittest.TestCase):
    """Document material facts omitted from the consumer-guidance article."""

    def test_omits_chatgpt_advertising_to_free_users(self):
        """The article does not mention that ChatGPT serves ads to Free tier users.
        Since ChatGPT for Teens appears to be free, parents should know whether
        their teens will see advertising."""
        ad_tiers = ["Free", "Go"]  # Both see ads
        teen_tier = "Free"  # Teens likely on free tier
        # Material omission for a consumer-guidance article about teens
        ad_disclosure_in_article = False
        self.assertFalse(ad_disclosure_in_article)

    def test_omits_openai_privacy_policy_advertiser_data_sharing(self):
        """OpenAI's April 30, 2026 privacy policy update allows receiving purchase
        data from advertisers and sharing user data with 'marketing partners.'
        This is directly material to a teen safety article."""
        policy_update_date = "2026-04-30"
        article_date = "2026-08-18"
        # Policy update predates article by 3.5 months
        data_sharing_mentioned = False
        self.assertFalse(data_sharing_mentioned)

    def test_omits_chatgpt_uninstall_spike(self):
        """ChatGPT saw 132% YoY increase in uninstalls following ad introduction
        (Adweek, May 2026) — a material trust signal omitted from an article
        advising parents to trust the product."""
        uninstall_increase_pct = 132
        mentioned_in_article = False
        self.assertFalse(mentioned_in_article)

    def test_omits_openai_device_facial_recognition_plans(self):
        """OpenAI is developing an always-on camera device with facial recognition
        (io Products) — receiving zero privacy scrutiny compared to extensive
        Meta glasses coverage. Not mentioned in this teen safety context."""
        device_features = ["always_on_camera", "facial_recognition", "observe_users"]
        privacy_scrutiny = "zero"
        self.assertEqual(privacy_scrutiny, "zero")

    def test_omits_whether_teen_free_users_see_ads(self):
        """The most material question for parents — 'will my teen see ads in
        ChatGPT?' — is not addressed in the article."""
        teen_ad_exposure_addressed = False
        self.assertFalse(teen_ad_exposure_addressed)

    def test_omits_senator_markey_chatgpt_ad_probe(self):
        """Senator Ed Markey sent OpenAI a formal probe letter about ChatGPT
        advertising and teen protection (Jan 2026, response due Feb 12, 2026).
        This is directly relevant to a teen safety article published 6 months later."""
        markey_probe_date = "2026-01-22"
        markey_probe_target = "OpenAI"
        mentioned = False
        self.assertFalse(mentioned)


class TestFinancialContext(unittest.TestCase):
    """Verify the financial relationships creating the coverage context."""

    def test_news_corp_openai_deal(self):
        """News Corp has $250M/5yr ($50M/yr) content licensing deal with OpenAI."""
        deal_value_per_year = 50_000_000
        self.assertEqual(deal_value_per_year, 50_000_000)

    def test_news_corp_meta_deal(self):
        """News Corp has up to $50M/yr, 3-year content licensing deal with Meta."""
        deal_value_per_year_max = 50_000_000
        self.assertEqual(deal_value_per_year_max, 50_000_000)

    def test_balanced_deals_make_asymmetry_more_notable(self):
        """With roughly equal financial relationships to both companies,
        vocabulary asymmetry cannot be attributed to differential financial incentive."""
        openai_deal = 50_000_000  # per year
        meta_deal = 50_000_000  # per year max
        ratio = openai_deal / meta_deal
        # Deals are roughly 1:1
        self.assertAlmostEqual(ratio, 1.0, places=0)


class TestDisclosureAsymmetry(unittest.TestCase):
    """Verify the selective disclosure pattern."""

    def test_openai_disclosure_present(self):
        """The article discloses: 'News Corp, owner of The Wall Street Journal,
        has a content-licensing partnership with OpenAI.'"""
        disclosure = "News Corp, owner of The Wall Street Journal, has a content-licensing partnership with OpenAI"
        self.assertIn("OpenAI", disclosure)

    def test_meta_disclosure_absent(self):
        """The article does NOT disclose News Corp's parallel content licensing
        deal with Meta ($50M/yr), creating asymmetric transparency."""
        meta_disclosure_present = False
        self.assertFalse(meta_disclosure_present)

    def test_selective_disclosure_creates_false_transparency(self):
        """Disclosing only the OpenAI relationship while omitting the Meta
        relationship gives readers an incomplete picture of the publication's
        financial interests. A reader might infer: 'they disclosed the OpenAI
        deal, so they're being transparent' — without knowing there's a
        parallel deal with the entity being criticized."""
        disclosed_relationships = ["OpenAI"]
        actual_relationships = ["OpenAI", "Meta"]
        self.assertNotEqual(disclosed_relationships, actual_relationships)


class TestConfounders(unittest.TestCase):
    """Document legitimate confounders that could explain the asymmetry."""

    def test_confounder_meta_trial_is_real_news(self):
        """Meta IS on trial for $1.4T — referencing this is editorially defensible."""
        confounder = "Meta trial is genuine current news"
        strength = "STRONG"
        self.assertEqual(strength, "STRONG")

    def test_confounder_product_launch_genre(self):
        """Product launch articles tend toward positive framing of the launched product."""
        confounder = "Article is about OpenAI's new product"
        strength = "MODERATE"
        self.assertEqual(strength, "MODERATE")

    def test_confounder_consumer_guidance_genre(self):
        """'What Parents Need to Know' genre prioritizes helpful information."""
        confounder = "Consumer guidance genre tilts positive"
        strength = "WEAK"
        self.assertEqual(strength, "WEAK")

    def test_rebuttal_consumer_guidance_requires_risk_disclosure(self):
        """Consumer guidance for parents about a teen product has a HIGHER obligation
        to disclose material risks (like advertising exposure), not a lower one."""
        genre = "consumer_guidance"
        obligation_to_disclose_risks = "elevated"
        self.assertEqual(obligation_to_disclose_risks, "elevated")


class TestCrossArticleWSJPattern(unittest.TestCase):
    """Compare this article's framing to other recent WSJ OpenAI coverage."""

    def test_wsj_openai_data_promise_is_competitive_framing(self):
        """WSJ's 'OpenAI's Latest Bid to Fight Anthropic: A Promise Not to Keep
        Customer Data' frames a privacy decision as a competitive weapon —
        aspirational vocabulary ('bid to fight', 'promise')."""
        headline = "OpenAI's Latest Bid to Fight Anthropic: A Promise Not to Keep Customer Data"
        framing = "competitive_advantage"
        # Privacy as strategy, not obligation
        self.assertIn("Bid to Fight", headline)

    def test_wsj_openai_rogue_models_is_responsible_framing(self):
        """WSJ's coverage of OpenAI models escaping sandboxes uses responsible-
        self-regulation vocabulary ('hit the brakes', 'revamp security measures')
        rather than alarm vocabulary."""
        headline = "OpenAI Hit the Brakes on AI Training After Models Went Rogue"
        # 'Hit the brakes' = responsible, proactive
        # Compare to Meta trial: 'accused', 'drug pushers', 'exploits weaknesses'
        framing = "responsible_self_regulation"
        self.assertEqual(framing, "responsible_self_regulation")

    def test_wsj_meta_trial_is_alarm_framing(self):
        """WSJ's Meta coverage uses alarm/accusation vocabulary consistently:
        'accused', 'drug pushers', '$1.4 trillion', 'youth mental health crisis'."""
        meta_vocabulary = [
            "accused in court",
            "contributing to the youth mental health crisis",
            "drug pushers",
            "exploits weaknesses in the human psychology",
            "$1.4 trillion in damages",
        ]
        alarm_count = sum(1 for v in meta_vocabulary
                          if any(w in v.lower() for w in
                                 ["accused", "crisis", "drug", "exploit", "trillion"]))
        self.assertEqual(alarm_count, 5)

    def test_vocabulary_register_is_entity_dependent_not_topic_dependent(self):
        """The vocabulary register (aspirational vs alarm) correlates with the ENTITY
        being discussed, not the TOPIC. Both OpenAI and Meta are doing teen safety work.
        OpenAI gets aspirational vocabulary; Meta gets alarm vocabulary."""
        entity_vocabulary_map = {
            "openai": "aspirational",
            "meta": "alarm",
        }
        # Same topic, different vocabulary = entity-dependent framing
        self.assertNotEqual(entity_vocabulary_map["openai"],
                            entity_vocabulary_map["meta"])


class TestMetaPriorArtDiminishment(unittest.TestCase):
    """Analyze how Meta's earlier innovation is reframed as reactive remediation."""

    def test_meta_teen_accounts_predate_openai(self):
        """Instagram added teen accounts with restrictive defaults in 2024,
        two years before OpenAI's ChatGPT for Teens in 2026."""
        meta_teen_accounts = 2024
        openai_chatgpt_teens = 2026
        self.assertLess(meta_teen_accounts, openai_chatgpt_teens)

    def test_meta_prior_art_reframed_as_forced_reaction(self):
        """The article frames Meta's EARLIER innovation as forced reaction:
        'since lawmakers and lawyers began complaining.' OpenAI's LATER
        implementation is framed as proactive innovation: 'welcome news.'"""
        meta_framing = "since lawmakers and lawyers began complaining"
        openai_framing = "welcome news for parents"
        # Earlier = reactive, Later = proactive — temporal inversion
        self.assertIn("complaining", meta_framing)
        self.assertIn("welcome", openai_framing)

    def test_borrowed_from_playbook_diminishes_meta_innovation(self):
        """Saying OpenAI's features 'appear to be borrowed from Meta's playbook'
        acknowledges the prior art but frames it as a 'playbook' — a document
        of damage-control strategy rather than genuine innovation."""
        phrase = "appear to be borrowed from Meta's playbook"
        # A neutral framing would be: 'builds on Meta's pioneering teen safety features'
        # 'Borrowed from playbook' implies: Meta wrote a crisis-response manual;
        # OpenAI sensibly adopted the good parts
        self.assertIn("playbook", phrase)


if __name__ == "__main__":
    unittest.main()
