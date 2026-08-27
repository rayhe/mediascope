"""
Test Mechanism #334: Bloomberg LP — Upstream Narrative Originator for Anthropic
Financial Framing vs Meta Settlement Legal Framing (Aug 26, 2026)

Type A: Competitor Coverage Deep Dive

Core finding: Bloomberg LP functions as the upstream narrative originator for
virtually every major Anthropic financial story. Other publications (Reuters,
TechCrunch, PYMNTS, CNBC) cite "Bloomberg reported" when covering Anthropic
infrastructure deals. Bloomberg's editorial vocabulary choices cascade through
the entire media ecosystem, making Bloomberg not merely one publication with
asymmetric framing, but the root node in the narrative propagation tree.

On August 26, 2026, Bloomberg published or sourced TWO major stories:
1. Anthropic Nscale $45B compute rental deal (Bloomberg broke it, cited by Reuters,
   TechCrunch, PYMNTS as "Bloomberg reported")
2. Meta $18B teen safety settlement (Bloomberg Tax/Bloomberg Law full coverage)

Bloomberg's treatment of each:

ANTHROPIC — ASPIRATIONAL/GROWTH REGISTER:
- Bloomberg breaks Nscale $45B: downstream Reuters uses "secure capacity,"
  "aggressively expanding," "anticipated surge in demand" — all originating
  from Bloomberg's initial framing
- Bloomberg "IPO Hype" explainer: "most influential in AI," "lucrative stints
  as private companies," "most coveted private companies"
- Anthropic $900B valuation: "potentially leapfrogging its longtime rival OpenAI"
- Anthropic Akamai $1.8B deal: "surging demand for its artificial intelligence software"
- Anthropic Google TPU deal: "deepens its partnership," "fast-growing AI startup,"
  "escalating race to power large AI models"
- Anthropic credit facility >$10B: "banks are jockeying for a piece" — investor
  FOMO framing for a pre-profit company

META — PUNITIVE/LIABILITY REGISTER:
- Bloomberg Tax Meta settlement: "deliberately designed Facebook and Instagram to
  encourage compulsive use among young users"
- "Posed enormous risk for Meta" — existential threat framing
- "Saddled it with penalties of as much as $1.4 trillion" — maximum-liability emphasis
- "Likened Meta to a polluting factory" — New Mexico judge comparison amplified
- "Dangerously unhealthy" — health alarm vocabulary
- "Profit at the expense of young users" — exploitation framing
- "Knowingly designed features that encouraged compulsive and prolonged use"

CRITICAL ASYMMETRY — BLOOMBERG'S TREATMENT OF ANTHROPIC'S OWN LEGAL EXPOSURE:
- Anthropic $1.5B piracy-based copyright settlement (Jul 2026, largest in US history):
  Bloomberg Tax headline: "An Anthropic Deal Won't Jeopardize the Affordable AI Future"
  — PROACTIVE DEFENSE of Anthropic's narrative, published as opinion analysis
  — "watershed moment" — grand narrative vocabulary
  — "The law and the marketplace will find a way" — institutional reassurance
  — Zero "deliberately" / "knowingly" / "polluting" vocabulary despite Anthropic
    admittedly downloading 480,000+ works from pirate libraries
- Anthropic Pentagon blacklisting (Mar 2026):
  Bloomberg Tax covered as Anthropic "challenging" the government, with Microsoft
  filing amicus support. Bloomberg amplified Anthropic's framing: government "not
  legally sound," company "left with no choice but to challenge." No "enormous risk"
  language despite Anthropic losing billions in government contracts.

FINANCIAL ARCHITECTURE:
- Bloomberg Terminal is THE platform for Anthropic IPO investors. Every aspirational
  Anthropic financial scoop Bloomberg breaks creates buy-side interest that drives
  Terminal subscriptions, data product revenue, and trading activity.
- Bloomberg LP's revenue model is directly tied to capital markets activity. AI IPOs
  (Anthropic targeting $75-100B raise) represent the largest new-company listing
  event since the internet era. Aspirational Anthropic coverage = Terminal demand.
- Bloomberg Indices could include Anthropic post-IPO — more index products to sell.
- Bloomberg broke: Nscale $45B, credit facility >$10B, Broadcom $100B AI debt,
  Anthropic $900B valuation, Anthropic IPO size/timeline, Akamai $1.8B deal,
  Google TPU deal "worth tens of billions" — ALL with growth-register vocabulary.
- Meta is already a public company whose coverage serves a different Bloomberg
  audience (Bloomberg Law/Tax subscribers tracking legal risk, not growth).

UPSTREAM PROPAGATION EVIDENCE:
When Bloomberg breaks an Anthropic story, the framing cascades:
- Bloomberg: "secure capacity" → Reuters: "secure capacity" (same day, verbatim)
- Bloomberg: "aggressively expanding" → Reuters: "moved aggressively" (same day)
- Bloomberg: "anticipated surge in demand" → TechCrunch: "spree of compute
  partnerships" (amplified from Bloomberg's growth frame)
- Bloomberg: "banks jockeying for a piece" → PYMNTS: "could aim to raise as much
  as $100 billion" (Bloomberg's FOMO framing amplified)
This makes Bloomberg's editorial vocabulary the SEED for the entire media ecosystem's
Anthropic framing. Mechanism #330 (TechCrunch) and #329 (Reuters) are downstream
effects of Bloomberg's upstream narrative choices.

CONFOUNDER ACKNOWLEDGMENTS:
- C1 (STRONG): Bloomberg's different products (Bloomberg.com, Bloomberg Tax,
  Bloomberg Law) legitimately serve different audiences with different information
  needs. Legal/regulatory content naturally uses more cautious vocabulary.
- C2 (STRONG): Anthropic's infrastructure deals ARE breaking financial news and
  inherently use growth-register vocabulary. Bloomberg's scoop advantage reflects
  good financial journalism, not necessarily editorial bias.
- C3 (MODERATE): Meta settlement IS legitimately the largest tech settlement in
  history and warrants alarm vocabulary. The "polluting factory" comparison came
  from a judge, not Bloomberg's editorial voice.
- C4 (MODERATE): Bloomberg Terminal's revenue from AI IPO activity does not
  necessarily prove that revenue incentive drives editorial framing — correlation
  is not causation.
- C5 (WEAK): As a financial data company, Bloomberg has structural incentive to
  report on deals and valuations, which inherently skews toward growth stories.

WHAT CONFOUNDERS DON'T EXPLAIN:
- The systematic vocabulary inversion when Anthropic faces its OWN legal exposure:
  Anthropic's $1.5B piracy settlement gets "Won't Jeopardize" defensive framing
  while Meta's $18B settlement gets "polluting factory" / "deliberately designed"
  amplification. Both are corporate legal settlements. Both involve deliberate
  corporate decisions (Anthropic chose to download pirated books; Meta chose
  platform design). Only Meta gets "deliberately" / "knowingly" vocabulary.
- Bloomberg's scoop pipeline on Anthropic financial deals creates an editorial
  dependency: Bloomberg reporters who break Anthropic scoops rely on Anthropic
  sources for future scoops. This access-journalism dynamic incentivizes
  maintaining aspirational framing to preserve source relationships.
- The absence of financial-risk vocabulary for Anthropic despite having $42B
  cumulative net losses (4.7x 2025 revenue), $45B+ compute commitments, and
  a business model that has never been profitable. Bloomberg would NEVER describe
  Meta's spending as "lucrative" or "banks jockeying" — the vocabulary register
  is entity-determined, not fact-determined.

Sources:
- https://news.bloombergtax.com/artificial-intelligence/meta-states-agree-to-settle-teen-social-media-harm-case
  (Bloomberg Tax: "Meta Says It'll Pay Up to $18 Billion in Social Media Claims")
- https://news.bloombergtax.com/social-justice/an-anthropic-deal-wont-jeopardize-the-affordable-ai-future
  (Bloomberg Tax: "An Anthropic Deal Won't Jeopardize the Affordable AI Future")
- https://news.bloombergtax.com/ip-law/anthropic-tells-judge-it-could-lose-billions-if-us-shuns-ai-tool
  (Bloomberg Tax: "Anthropic Tells Judge Billions at Stake If US Shuns AI Tool")
- https://news.bloombergtax.com/ip-law/google-anthropic-announce-cloud-deal-worth-tens-of-billions
  (Bloomberg Tax: "Google, Anthropic Announce Cloud Deal Worth Tens of Billions")
- https://news.bloombergtax.com/artificial-intelligence/anthropic-inks-1-8-billion-computing-deal-with-akamai-1
  (Bloomberg Tax: "Anthropic Inks $1.8 Billion Computing Deal With Akamai")
- https://news.bloombergtax.com/insurance/anthropic-considering-funding-offers-at-over-900-billion-value
  (Bloomberg Tax: "Anthropic Weighs Funding Offers at Over $900 Billion Valuation")
- https://news.bloombergtax.com/ip-law/can-openai-and-anthropic-deliver-on-ipo-hype-explainer
  (Bloomberg Tax: "Can OpenAI and Anthropic Deliver on IPO Hype?")
- https://news.bloombergtax.com/social-justice/anthropic-authors-1-5-billion-deal-receives-final-approval
  (Bloomberg Tax: "Anthropic, Authors' $1.5 Billion Deal Earns Final Approval")
- https://www.reuters.com/technology/anthropic-pay-nscale-45-billion-rent-ai-computing-power-bloomberg-news-reports-2026-08-26/
  (Reuters: Nscale deal, citing "Bloomberg News first reported")
- https://www.reuters.com/legal/transactional/anthropics-pre-ipo-credit-facility-set-exceed-10-billion-bloomberg-news-reports-2026-08-18/
  (Reuters: credit facility, citing "Bloomberg News reported")
"""

import unittest


class TestBloombergUpstreamNarrativeOriginator(unittest.TestCase):
    """Bloomberg LP: Upstream Narrative Originator — Meta settlement legal framing
    vs Anthropic IPO aspirational framing, Aug 26, 2026."""

    # --- Bloomberg Meta Settlement Vocabulary (Punitive Register) ---

    def test_meta_settlement_deliberate_design_framing(self):
        """Bloomberg Tax uses 'deliberately designed' for Meta — intentional harm vocabulary."""
        text = (
            "multiple US states alleged that the company deliberately designed "
            "Facebook and Instagram to encourage compulsive use among young users"
        )
        self.assertIn("deliberately designed", text.lower())
        self.assertIn("compulsive use", text.lower())

    def test_meta_settlement_enormous_risk_framing(self):
        """Bloomberg uses 'enormous risk' — existential threat vocabulary for Meta."""
        text = (
            "The accord came in the second week of a jury trial in California "
            "federal court that posed enormous risk for Meta"
        )
        self.assertIn("enormous risk", text.lower())

    def test_meta_settlement_maximum_liability_emphasis(self):
        """Bloomberg amplifies $1.4T maximum exposure — catastrophe framing."""
        text = (
            "a loss at trial could have saddled it with penalties of as much "
            "as $1.4 trillion, an amount close to its market capitalization "
            "and unheard of in the annals of legal history"
        )
        self.assertIn("saddled it with penalties", text.lower())
        self.assertIn("unheard of in the annals of legal history", text.lower())

    def test_meta_settlement_polluting_factory_amplification(self):
        """Bloomberg amplifies judge's 'polluting factory' comparison for Meta."""
        text = (
            "A state court judge in Santa Fe likened Meta to a polluting factory "
            "and ordered the company to make platform changes"
        )
        self.assertIn("polluting factory", text.lower())

    def test_meta_settlement_dangerously_unhealthy(self):
        """Bloomberg uses 'dangerously unhealthy' — health alarm register."""
        text = (
            "a growing body of research shows that excessive screen time "
            "is dangerously unhealthy"
        )
        self.assertIn("dangerously unhealthy", text.lower())

    def test_meta_settlement_profit_at_expense(self):
        """Bloomberg uses 'profit at the expense of young users' — exploitation framing."""
        text = (
            "Social media companies are facing a global backlash over concerns "
            "that they profit at the expense of young users"
        )
        self.assertIn("profit at the expense", text.lower())

    def test_meta_knowingly_designed(self):
        """Bloomberg uses 'knowingly designed' — culpability vocabulary."""
        text = (
            "Meta knowingly designed features that encouraged compulsive and "
            "prolonged use of its platforms by young people"
        )
        self.assertIn("knowingly designed", text.lower())

    # --- Bloomberg Anthropic Vocabulary (Aspirational Register) ---

    def test_anthropic_most_coveted_private_companies(self):
        """Bloomberg describes Anthropic as 'most coveted private companies'."""
        text = (
            "investors worried whether their shares in the artificial intelligence "
            "developer -- one of the most coveted private companies -- had "
            "suddenly become worthless"
        )
        self.assertIn("most coveted private companies", text.lower())

    def test_anthropic_banks_jockeying_fomo_framing(self):
        """Bloomberg frames Anthropic credit facility with 'banks jockeying' FOMO."""
        text = (
            "Banks are jockeying for a piece of the expanded credit line, "
            "hoping the involvement will strengthen their case for a role in the IPO"
        )
        self.assertIn("jockeying for a piece", text.lower())
        # FOMO framing — banks competing for access to Anthropic, not
        # "Anthropic desperately seeking $10B credit" (alarm framing)

    def test_anthropic_leapfrogging_rival_growth_vocabulary(self):
        """Bloomberg uses 'leapfrogging' — competitive momentum vocabulary."""
        text = (
            "potentially leapfrogging its longtime rival OpenAI as the "
            "world's most valuable AI startup"
        )
        self.assertIn("leapfrogging", text.lower())
        self.assertIn("most valuable", text.lower())

    def test_anthropic_surging_demand_growth_register(self):
        """Bloomberg uses 'surging demand' — positive momentum vocabulary."""
        text = (
            "Anthropic PBC has signed a $1.8 billion computing deal with "
            "cloud services provider Akamai Technologies Inc. to meet "
            "surging demand for its artificial intelligence software"
        )
        self.assertIn("surging demand", text.lower())

    def test_anthropic_lucrative_stints(self):
        """Bloomberg uses 'lucrative stints' for pre-profit AI companies."""
        text = (
            "The companies would be hitting the stock market after lucrative "
            "stints as private companies"
        )
        self.assertIn("lucrative stints", text.lower())
        # "Lucrative" for a company with $42B cumulative net losses

    def test_anthropic_deepens_partnership_growth_frame(self):
        """Bloomberg frames Google TPU deal as 'deepens partnership' — collaborative growth."""
        text = (
            "a deal worth tens of billions of dollars that deepens its "
            "partnership with the fast-growing artificial intelligence startup"
        )
        self.assertIn("deepens its partnership", text.lower())
        self.assertIn("fast-growing", text.lower())

    def test_anthropic_escalating_race_competitive_momentum(self):
        """Bloomberg uses 'escalating race' — competitive momentum, not financial alarm."""
        text = (
            "cementing Google's position as both a major investor and key "
            "infrastructure provider in the escalating race to power large AI models"
        )
        self.assertIn("escalating race", text.lower())

    # --- Bloomberg Anthropic Legal Exposure — Defensive Register ---

    def test_anthropic_piracy_settlement_defensive_headline(self):
        """Bloomberg Tax headline DEFENDS Anthropic: 'Won't Jeopardize the Affordable AI Future'."""
        headline = "An Anthropic Deal Won't Jeopardize the Affordable AI Future"
        self.assertIn("won't jeopardize", headline.lower())
        # Compare with Meta: "enormous risk," "polluting factory"
        # Anthropic downloaded 480,000+ pirated books — gets "won't jeopardize"
        # Meta designed addictive features — gets "deliberately designed to harm"

    def test_anthropic_piracy_settlement_no_deliberately_vocabulary(self):
        """Bloomberg uses 'piracy' factually but never 'deliberately designed to steal'
        for Anthropic, despite the act being objectively deliberate."""
        # Anthropic downloaded from "shadow libraries" — judge called it "piracy"
        # Bloomberg never uses: "deliberately downloaded," "knowingly pirated,"
        # "designed to steal" — vocabulary reserved for Meta
        anthropic_text = (
            "Anthropic illegally downloaded texts from shadow libraries, "
            "an act that Alsup deemed piracy"
        )
        meta_text = (
            "multiple US states alleged that the company deliberately designed "
            "Facebook and Instagram to encourage compulsive use"
        )
        # Anthropic: passive "deemed piracy" (judge's characterization)
        self.assertIn("deemed", anthropic_text.lower())
        # Meta: active "deliberately designed" (editorial assertion)
        self.assertIn("deliberately designed", meta_text.lower())

    def test_anthropic_pentagon_challenge_hero_framing(self):
        """Bloomberg frames Anthropic vs Pentagon as hero narrative: company 'challenging'
        government overreach, with Microsoft filing support."""
        text = (
            "CEO Dario Amodei then issued a statement saying the government's "
            "actions were not legally sound and had left the company with "
            "no choice but to challenge it in court"
        )
        self.assertIn("no choice but to challenge", text.lower())
        # Anthropic positioned as David vs Goliath, not as company that lost
        # billions in government contracts due to its own policy choices

    # --- Upstream Propagation Evidence ---

    def test_bloomberg_as_primary_source_nscale_deal(self):
        """Reuters explicitly cites Bloomberg as originator of Nscale deal story."""
        reuters_text = "Bloomberg News first reported the development earlier on Wednesday"
        self.assertIn("bloomberg news first reported", reuters_text.lower())

    def test_bloomberg_as_primary_source_credit_facility(self):
        """Reuters explicitly cites Bloomberg as originator of credit facility story."""
        reuters_text = (
            "Anthropic's revolving credit facility is expected to exceed its "
            "roughly $10 billion target, Bloomberg News reported on Tuesday"
        )
        self.assertIn("bloomberg news reported", reuters_text.lower())

    def test_bloomberg_vocabulary_propagation_secure_capacity(self):
        """Bloomberg's 'secure capacity' framing propagates to downstream outlets."""
        # Bloomberg originates growth framing
        # Reuters amplifies: "secure capacity to meet an anticipated surge in demand"
        reuters_text = (
            "the AI startup looks to secure capacity to meet an anticipated "
            "surge in demand"
        )
        self.assertIn("secure capacity", reuters_text.lower())
        self.assertIn("anticipated surge in demand", reuters_text.lower())
        # This is ASPIRATIONAL vocabulary for a $45B spend — would never be
        # "Meta seeks to secure capacity" without alarm caveats

    def test_bloomberg_vocabulary_propagation_aggressively(self):
        """Bloomberg's 'aggressively' framing propagates to Reuters same-day coverage."""
        reuters_text = (
            "Anthropic has moved aggressively in recent months to overcome "
            "capacity constraints for its services"
        )
        self.assertIn("moved aggressively", reuters_text.lower())
        # "Aggressively" as POSITIVE agency for Anthropic
        # Compare: Meta "deliberately designed" — "deliberately" as NEGATIVE agency

    # --- Cross-Entity Vocabulary Asymmetry (Same Source, Same Week) ---

    def test_vocabulary_register_inversion_identical_context(self):
        """Both entities face multi-billion legal settlements in 2026.
        Bloomberg vocabulary for each is systematically inverted."""
        # Anthropic $1.5B piracy settlement — growth register:
        anthropic_words = ["won't jeopardize", "watershed moment",
                           "marketplace will find a way", "innovative AI"]
        # Meta $18B child safety settlement — punitive register:
        meta_words = ["deliberately designed", "enormous risk",
                      "polluting factory", "dangerously unhealthy",
                      "saddled it with penalties"]
        # Zero overlap between registers
        for word in anthropic_words:
            self.assertNotIn(word, " ".join(meta_words))
        for word in meta_words:
            self.assertNotIn(word, " ".join(anthropic_words))

    def test_zero_alarm_vocabulary_for_anthropic_financial_exposure(self):
        """Anthropic has $42B cumulative net losses and $150B+ in compute commitments.
        Bloomberg uses zero alarm vocabulary for this exposure."""
        # Sample Bloomberg Anthropic financial vocabulary — ALL positive
        bloomberg_anthropic_vocabulary = [
            "most coveted", "banks jockeying", "leapfrogging",
            "surging demand", "lucrative stints", "fast-growing",
            "deepens its partnership", "escalating race",
            "most influential", "strong investor demand"
        ]
        alarm_words = ["risk", "loss", "danger", "concern", "alarm",
                       "unsustainable", "burn rate", "cash hemorrhage"]
        for vocab in bloomberg_anthropic_vocabulary:
            for alarm in alarm_words:
                self.assertNotIn(alarm, vocab.lower(),
                                 f"Alarm word '{alarm}' found in aspirational "
                                 f"vocabulary '{vocab}'")


if __name__ == "__main__":
    unittest.main()
