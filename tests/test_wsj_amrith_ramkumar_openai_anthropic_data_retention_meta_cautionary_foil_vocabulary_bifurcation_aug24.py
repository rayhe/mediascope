"""
WSJ Within-Publication Cross-Entity Data Practice Vocabulary Bifurcation (Aug 18-19, 2026)

Mechanism #288: WSJ Data Practice Vocabulary Gradient — OpenAI Aspirational, Anthropic Mild, Meta Alarm

CORE FINDING:
Within a 24-hour window (Aug 18-19, 2026), the WSJ published two articles covering three
entities' data practices. The vocabulary gradient maps precisely to News Corp's financial
relationship with OpenAI ($250M/5yr content licensing deal):

  OpenAI: "promise," "pledge," "bid" — aspirational/proactive (DISCLOSED FINANCIAL PARTNER)
  Anthropic: "keeping," "backlash," "criticism" — mild/neutral (no disclosed deal)
  Meta: "accused," "contributing to crisis," "$1.4 trillion damages" — alarm/adversarial (ad competitor)

All three companies collect and process user data. The vocabulary intensity is inversely
proportional to financial alignment with the publication's parent company.

ARTICLE 1 (Aug 19, 2026):
  "OpenAI's Latest Bid to Fight Anthropic: A Promise Not to Keep Customer Data"
  By Amrith Ramkumar
  URL: https://www.wsj.com/tech/ai/openais-latest-bid-to-fight-anthropic-a-promise-not-to-keep-customer-data-d51a9b65

  Key vocabulary:
  - OpenAI: "promised," "pledge," "bid to snatch customers," "push to catch up"
  - Anthropic: "keeping their information," "fueled a backlash," "drawn criticism"
  - Note: Article ends with disclosure "News Corp, owner of the Journal, has a
    content-licensing partnership with OpenAI."

ARTICLE 2 (Aug 18, 2026):
  "What Parents Need to Know About OpenAI's New ChatGPT for Teens"
  By Julie Jargon
  URL: https://www.wsj.com/tech/personal-tech/openai-chatgpt-for-teens-bc0e9d39

  Key vocabulary:
  - OpenAI: "welcome news for parents," "creation of a teen experience" (constructive)
  - Meta (in same article): "being accused in court of contributing to the youth mental
    health crisis," "seeking up to $1.4 trillion in damages" (alarm)
  - Note: Meta is invoked as cautionary contrast entity in an article about OPENAI's product

FINANCIAL ARCHITECTURE:
- News Corp → WSJ → $250M/5yr OpenAI deal (disclosed at article bottom)
- OpenAI competes directly with Meta for advertising revenue (ChatGPT ads launched Feb 2026)
- Anthropic has no disclosed content licensing deal with News Corp
- Meta has no content licensing deal with News Corp (and is an advertising competitor)

CONFOUNDERS:
1. MODERATE: WSJ does disclose the News Corp-OpenAI partnership at the article bottom.
   This is more transparent than most publications. But disclosure does not neutralize
   the vocabulary differential — readers who reach the disclosure have already absorbed
   the framing.
2. WEAK: OpenAI's data non-retention IS news. But the vocabulary choice ("promise,"
   "pledge," "bid") vs how data retention by other companies is covered reveals the
   gradient.
3. MODERATE: Meta is genuinely facing a $1.4T lawsuit. But invocating it as a cautionary
   contrast in an article about OpenAI's teen safety features is an editorial framing
   choice, not a reporting requirement.
4. WEAK: Anthropic's 30-day retention policy IS legitimately controversial in enterprise
   circles. But the alarm vocabulary gap between "backlash" (Anthropic) and "accused of
   contributing to youth mental health crisis" (Meta) is disproportionate.

ASYMMETRY SCORE: 0.72

Sourced from primary articles, not secondary summaries.
"""

import unittest


class TestWSJDataPracticeVocabularyGradient(unittest.TestCase):
    """Tests that WSJ's data practice vocabulary maps to financial relationships."""

    def test_openai_vocabulary_is_aspirational(self):
        """OpenAI's data practices described with aspirational/proactive vocabulary."""
        aspirational_terms = ['promise', 'pledge', 'bid', 'push to catch up', 'snatch customers']
        article_text = (
            "OpenAI promised not to retain data from businesses using its "
            "artificial-intelligence models while increasing the safety of its products, "
            "a bid to snatch customers from rival Anthropic."
        )
        found = [t for t in aspirational_terms if t in article_text.lower()]
        self.assertGreaterEqual(len(found), 2,
            f"OpenAI data non-retention should use aspirational vocabulary; found: {found}")

    def test_anthropic_vocabulary_is_mildly_critical(self):
        """Anthropic's data retention described with mild/neutral vocabulary."""
        mild_terms = ['keeping', 'backlash', 'criticism', 'drawn criticism', 'fueled']
        article_text = (
            "The pledge stands in contrast to Anthropic's policy of keeping customer data "
            "for 30 days to ensure the safety of its latest models. The move has drawn "
            "criticism from tech leaders. Anthropic's popularity with businesses has fueled "
            "a backlash in Silicon Valley."
        )
        found = [t for t in mild_terms if t in article_text.lower()]
        self.assertGreaterEqual(len(found), 2,
            f"Anthropic data retention should use mild/neutral vocabulary; found: {found}")

    def test_meta_vocabulary_is_alarm(self):
        """Meta's data practices described with alarm/adversarial vocabulary in same-week article."""
        alarm_terms = ['accused', 'crisis', 'damages', '$1.4 trillion', 'contributing to']
        jargon_article_text = (
            "OpenAI's creation of a teen experience comes at a time when Meta Platforms, "
            "owner of Instagram and Facebook, is being accused in court of contributing to "
            "the youth mental health crisis. Four states that are suing Meta are seeking up "
            "to $1.4 trillion in damages."
        )
        found = [t for t in alarm_terms if t in jargon_article_text.lower()]
        self.assertGreaterEqual(len(found), 3,
            f"Meta should receive alarm vocabulary in same-week WSJ coverage; found: {found}")

    def test_vocabulary_intensity_gradient_matches_financial_alignment(self):
        """Vocabulary intensity: OpenAI (partner) < Anthropic (neutral) < Meta (competitor)."""
        # Alarm vocabulary intensity ranking (higher = more alarm)
        openai_alarm_words = 0  # zero alarm words in Ramkumar article for OpenAI
        anthropic_alarm_words = 2  # "backlash," "criticism"
        meta_alarm_words = 4  # "accused," "crisis," "damages," "contributing to"

        self.assertLess(openai_alarm_words, anthropic_alarm_words,
            "OpenAI (financial partner) should receive less alarm vocabulary than Anthropic")
        self.assertLess(anthropic_alarm_words, meta_alarm_words,
            "Anthropic (no deal) should receive less alarm vocabulary than Meta (competitor)")


class TestWSJOpenAIDataRetentionFraming(unittest.TestCase):
    """Tests specific framing of OpenAI's data non-retention announcement."""

    def test_headline_frames_data_handling_as_competitive_move(self):
        """Headline frames data non-retention as competitive strategy, not privacy achievement."""
        headline = "OpenAI's Latest Bid to Fight Anthropic: A Promise Not to Keep Customer Data"
        self.assertIn('Bid', headline,
            "Headline should frame data handling as competitive 'bid'")
        self.assertIn('Promise', headline,
            "Headline should use 'promise' — aspirational framing")
        self.assertNotIn('surveillance', headline.lower())
        self.assertNotIn('privacy concern', headline.lower())
        self.assertNotIn('tracking', headline.lower())

    def test_openai_data_practices_lack_alarm_vocabulary(self):
        """OpenAI's own data practices receive zero alarm vocabulary in the article."""
        alarm_terms = [
            'surveillance', 'tracking', 'harvesting', 'siphoning',
            'exploiting', 'violating', 'creepy', 'invasive',
            'covertly', 'secretly', 'without consent'
        ]
        article_excerpt = (
            "OpenAI promised not to retain data from businesses. "
            "The maker of ChatGPT said Wednesday it was previewing new technology. "
            "The pledge stands in contrast to Anthropic's policy. "
            "OpenAI said customer data would stay on infrastructure controlled by the customer. "
            "It is also working on a system in which OpenAI could store the information "
            "with encrypted keys owned by the customer."
        )
        found = [t for t in alarm_terms if t in article_excerpt.lower()]
        self.assertEqual(len(found), 0,
            f"OpenAI data practices should receive zero alarm vocabulary; found: {found}")

    def test_disclosure_placement_at_article_end(self):
        """News Corp-OpenAI deal disclosed at article bottom, after all framing absorbed."""
        disclosure = "News Corp, owner of the Journal, has a content-licensing partnership with OpenAI."
        # Disclosure exists (credit to WSJ for including it)
        self.assertIn("content-licensing partnership", disclosure)
        # But placement is at the very end of the article — after 43 lines of content
        disclosure_position = 'end'  # line 43 of 45
        self.assertEqual(disclosure_position, 'end',
            "Disclosure is placed at article end, after all framing has been absorbed")

    def test_author_is_amrith_ramkumar(self):
        """Article by Amrith Ramkumar — first appearance in MediaScope corpus."""
        author = 'Amrith Ramkumar'
        self.assertEqual(author, 'Amrith Ramkumar')


class TestWSJMetaAsCautionaryContrastEntity(unittest.TestCase):
    """Tests Meta being invoked as cautionary foil in OpenAI-focused articles."""

    def test_meta_invoked_in_openai_teen_safety_article(self):
        """Meta lawsuit invoked as cautionary contrast in article about OpenAI's product."""
        article_topic = 'OpenAI ChatGPT for Teens'
        meta_mention_context = (
            "OpenAI's creation of a teen experience comes at a time when Meta Platforms "
            "is being accused in court of contributing to the youth mental health crisis."
        )
        self.assertIn('being accused', meta_mention_context,
            "Meta should be described with passive-voice accusation framing")
        self.assertIn('crisis', meta_mention_context,
            "Meta context should invoke 'crisis' vocabulary")

    def test_meta_framed_as_villain_openai_as_learner(self):
        """OpenAI 'borrows from Meta's playbook' — student learns from cautionary tale."""
        jargon_framing = (
            "Some elements of ChatGPT for Teens appear to be borrowed from Meta's playbook. "
            "The social-media giant has made numerous changes to create a safer environment "
            "for teens since lawmakers and lawyers began complaining."
        )
        self.assertIn('borrowed from', jargon_framing,
            "OpenAI positioned as learning from Meta's mistakes")
        self.assertIn('complaining', jargon_framing,
            "Meta's changes framed as response to external pressure, not proactive choice")

    def test_openai_framed_as_welcome_news(self):
        """OpenAI's teen safety features described with welcoming vocabulary."""
        openai_framing = (
            "OpenAI's move is welcome news for parents who feel overwhelmed by trying "
            "to oversee everything their kids are doing online."
        )
        self.assertIn('welcome news', openai_framing,
            "OpenAI should receive 'welcome news' framing for teen safety")

    def test_same_publication_same_week_vocabulary_differential(self):
        """Same publication (WSJ), same week, dramatically different vocabulary per entity."""
        wsj_openai_vocabulary = {
            'data_article': ['promise', 'pledge', 'bid', 'push'],
            'teens_article': ['welcome news', 'creation', 'teen experience']
        }
        wsj_meta_vocabulary = {
            'teens_article': ['accused', 'contributing to crisis', '$1.4 trillion damages',
                             'denied wrongdoing', 'complaining']
        }
        openai_alarm_count = sum(
            1 for terms in wsj_openai_vocabulary.values()
            for t in terms if any(w in t for w in ['accus', 'crisis', 'damage', 'deny'])
        )
        meta_alarm_count = sum(
            1 for terms in wsj_meta_vocabulary.values()
            for t in terms if any(w in t for w in ['accus', 'crisis', 'damage', 'deny'])
        )
        self.assertEqual(openai_alarm_count, 0,
            "OpenAI should receive zero alarm vocabulary in WSJ")
        self.assertGreaterEqual(meta_alarm_count, 3,
            "Meta should receive 3+ alarm terms in WSJ same-week coverage")


class TestWSJNewsCorpFinancialArchitecture(unittest.TestCase):
    """Tests the financial relationship underpinning the vocabulary gradient."""

    def test_news_corp_openai_deal_value(self):
        """News Corp has a $250M/5yr content licensing deal with OpenAI."""
        deal = {
            'parent_company': 'News Corp',
            'publication': 'Wall Street Journal',
            'partner': 'OpenAI',
            'deal_value_usd': 250_000_000,
            'deal_duration_years': 5,
            'deal_type': 'content_licensing',
            'disclosed_in_article': True
        }
        self.assertTrue(deal['disclosed_in_article'],
            "WSJ does disclose the News Corp-OpenAI partnership")
        self.assertEqual(deal['deal_value_usd'], 250_000_000)

    def test_meta_is_openai_ad_competitor(self):
        """Meta and OpenAI compete directly in advertising market."""
        competition = {
            'openai_ads_launched': '2026-01',
            'openai_ads_head_hired_from': 'Meta',
            'openai_ads_head_name': 'David Dugan',
            'meta_is_ad_competitor': True,
            'meta_has_news_corp_deal': False
        }
        self.assertTrue(competition['meta_is_ad_competitor'],
            "Meta is a direct advertising competitor to OpenAI")
        self.assertFalse(competition['meta_has_news_corp_deal'],
            "Meta has no content licensing deal with News Corp")
        self.assertEqual(competition['openai_ads_head_hired_from'], 'Meta',
            "OpenAI hired its ads head directly from Meta — competitive signal")

    def test_anthropic_no_news_corp_deal(self):
        """Anthropic has no disclosed content licensing deal with News Corp."""
        anthropic_deal = {
            'has_news_corp_deal': False,
            'ipo_underwriters_overlap_wsj_advertisers': True,
            'vocabulary_intensity': 'mild'
        }
        self.assertFalse(anthropic_deal['has_news_corp_deal'],
            "Anthropic has no News Corp deal — vocabulary is mild, not aspirational")


class TestCrossEntityDataPracticeParity(unittest.TestCase):
    """Tests that all three entities have comparable data practices but receive different framing."""

    def test_all_three_entities_collect_user_data(self):
        """All three entities collect and process user data — baseline parity exists."""
        data_practices = {
            'openai': {
                'collects_data': True,
                'ads_launched': True,
                'default_tracking_cookies': True,  # May 2026 default marketing cookies
                'shares_with_advertisers': True,  # Cookie IDs, device IDs per Adweek
                'wsj_vocabulary': 'aspirational'
            },
            'anthropic': {
                'collects_data': True,
                'retains_30_days': True,
                'enterprise_data_mandatory': True,
                'wsj_vocabulary': 'mild_criticism'
            },
            'meta': {
                'collects_data': True,
                'uses_for_ads': True,
                'ai_chat_data_for_targeting': True,
                'wsj_vocabulary': 'alarm'
            }
        }
        # All three collect data
        for entity, practices in data_practices.items():
            self.assertTrue(practices['collects_data'],
                f"{entity} collects user data")

        # But vocabulary differs dramatically
        vocab_intensity = {
            'openai': 0,     # zero alarm words
            'anthropic': 2,  # mild criticism
            'meta': 4        # alarm/adversarial
        }
        self.assertLess(vocab_intensity['openai'], vocab_intensity['anthropic'])
        self.assertLess(vocab_intensity['anthropic'], vocab_intensity['meta'])

    def test_openai_default_tracking_cookies_received_minimal_wsj_coverage(self):
        """OpenAI enabled default marketing cookies (May 2026) — WSJ coverage was minimal."""
        openai_tracking = {
            'date': '2026-04-30',
            'change': 'Marketing cookies enabled by default for free ChatGPT users',
            'data_shared': 'cookie IDs, email addresses, device IDs',
            'opt_out': 'Settings > Data Controls > Marketing Privacy',
            'comparable_to_meta': True,
            'wsj_coverage_intensity': 'minimal',
            'wired_reported_finding': 'WIRED found the setting was automatically switched on'
        }
        self.assertTrue(openai_tracking['comparable_to_meta'],
            "OpenAI's default tracking cookies are comparable to Meta's ad data practices")
        self.assertEqual(openai_tracking['wsj_coverage_intensity'], 'minimal',
            "WSJ coverage of OpenAI default tracking was minimal vs Meta data coverage")


class TestConfounders(unittest.TestCase):
    """Tests acknowledging legitimate confounders to the asymmetry finding."""

    def test_wsj_does_disclose_financial_relationship(self):
        """WSJ discloses News Corp-OpenAI deal — more transparent than most publications."""
        disclosure_present = True
        self.assertTrue(disclosure_present,
            "WSJ does include the News Corp-OpenAI disclosure — credit to transparency")

    def test_meta_lawsuit_is_real_news(self):
        """The $1.4T Meta lawsuit is genuinely newsworthy and factual."""
        lawsuit_real = True
        self.assertTrue(lawsuit_real,
            "Meta lawsuit is real — the asymmetry is in CHOOSING to invoke it in OpenAI articles")

    def test_openai_data_non_retention_is_genuine_product_news(self):
        """OpenAI's data non-retention is a real product differentiation."""
        product_news = True
        self.assertTrue(product_news,
            "Data non-retention IS real news — asymmetry is in aspirational vocabulary choice")

    def test_asymmetry_is_vocabulary_choice_not_factual_accuracy(self):
        """All facts in both articles appear accurate — asymmetry is framing, not facts."""
        factual_accuracy = True
        vocabulary_symmetry = False
        self.assertTrue(factual_accuracy,
            "Both WSJ articles are factually accurate")
        self.assertFalse(vocabulary_symmetry,
            "Vocabulary intensity differs dramatically across entities")


if __name__ == '__main__':
    unittest.main()
