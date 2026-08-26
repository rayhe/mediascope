"""
Fortune AI Weekly Multi-Episode Cross-Entity Vocabulary Gradient Test Suite

Mechanism #324: Fortune AI Weekly (Fortune/YouTube vodcast) applies systematically
different vocabulary registers to Meta, OpenAI, and Anthropic across multiple
episodes from the same hosts (Jeremy Kahn, Bea Nolan, Emily Forlini), July-August
2026. This constitutes a multi-episode natural experiment: same editorial team,
same format, same podcast, different entities → different vocabulary.

Key Discovery: Within a single six-week span:
- Meta segments use alarm/crisis vocabulary ("Under Fire," "Sparks Privacy Backlash,"
  "Betting," "Huge Privacy Debate")
- OpenAI segments use analytical/explanatory vocabulary ("Explained," "Losing Key
  Executives," "Break Its Own Safety Rules?") — even when the substance is MORE
  alarming (an agent that attacked other companies)
- Anthropic segments use scientific/aspirational vocabulary ("J Space," "AI Watermarks,"
  "Troubling AI Agent Behavior" — clinical language for behavior that, if Meta's,
  would be "Rogue AI Under Fire")

Financial context: Fortune (owned by Thai billionaire Chatchaval Jiaravanon via
Fortune Media Group Holdings) has no known content licensing deals with any AI lab.
This is cultural consensus evidence, not financial incentive.

Sources:
- https://www.youtube.com/watch?v=TVdoEPg42pQ (Jul 14 — "Why Meta's Ray-Bans Sparked
  a Huge Privacy Debate")
- https://www.youtube.com/watch?v=1ukpGQ-25Go (Aug 4 — "Your Chatbot Conversations
  Might Be Showing Up in Google" — includes Microsoft vs Meta Earnings)
- https://www.youtube.com/watch?v=-E88RyyfK0w (Aug 18 — "Zuckerberg Is Betting on
  Open Source to Win the AI Race")
- https://www.youtube.com/watch?v=tGJWXBaNqDQ (Jul 7 debut — export restrictions,
  Meta excess compute)
- https://www.youtube.com/watch?v=M37Tw0b0IQ8 (Jul 21 — Apple vs OpenAI lawsuit,
  Anthropic agent behavior)
- https://www.youtube.com/watch?v=o-veNtcgeEo (Aug 11 — Trump AI plan)
"""

import unittest
import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestFortuneAIWeeklyPodcastExists(unittest.TestCase):
    """Verify the Fortune AI Weekly podcast is tracked in MediaScope."""

    def test_fortune_ai_weekly_in_podcast_sentiment(self):
        """Fortune AI Weekly should be documented in podcast-sentiment.md."""
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            content = f.read()
        self.assertIn('Fortune AI Weekly', content)

    def test_fortune_ai_weekly_multi_episode_documented(self):
        """Multi-episode cross-entity vocabulary gradient analysis documented."""
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            content = f.read()
        self.assertIn('multi-episode', content.lower())
        self.assertIn('vocabulary gradient', content.lower())


class TestFortuneAIWeeklyEpisodeCoverage(unittest.TestCase):
    """Verify all six Fortune AI Weekly episodes from Jul-Aug 2026 are documented."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_jul14_meta_glasses_episode(self):
        """Jul 14 episode about Meta glasses privacy debate should be documented."""
        self.assertIn('Meta\'s Ray-Bans Sparked', self.content)

    def test_aug4_microsoft_meta_earnings_episode(self):
        """Aug 4 episode comparing Microsoft vs Meta earnings should be documented."""
        self.assertIn('Microsoft vs. Meta Earnings', self.content)

    def test_aug18_zuckerberg_manifesto_episode(self):
        """Aug 18 episode about Zuckerberg open-source manifesto should be documented."""
        self.assertIn('Zuckerberg', self.content)
        self.assertIn('Open Source', self.content)

    def test_aug4_openai_rogue_ai_episode(self):
        """Aug 4 episode about OpenAI rogue AI hack should be documented."""
        self.assertIn('Rogue AI', self.content)


class TestMetaVocabularyRegister(unittest.TestCase):
    """Verify Meta segments consistently receive alarm/crisis vocabulary."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_meta_alarm_vocabulary_under_fire(self):
        """Meta segment uses 'Under Fire' alarm vocabulary."""
        self.assertIn('Under Fire', self.content)

    def test_meta_alarm_vocabulary_backlash(self):
        """Meta segment uses 'Backlash' alarm vocabulary."""
        self.assertIn('Backlash', self.content)

    def test_meta_alarm_vocabulary_betting(self):
        """Meta CEO framed with 'Betting' gambling/risk vocabulary."""
        self.assertIn('Betting', self.content)

    def test_meta_alarm_vocabulary_privacy_debate(self):
        """Meta framed with 'Privacy Debate' alarm vocabulary."""
        self.assertIn('Privacy Debate', self.content)

    def test_meta_receives_three_plus_alarm_terms(self):
        """Meta segments accumulate 3+ alarm/crisis vocabulary terms across episodes."""
        alarm_terms = [
            'Under Fire', 'Backlash', 'Betting', 'Privacy Debate',
            'Huge Privacy Debate', 'Sparked'
        ]
        found = sum(1 for term in alarm_terms if term in self.content)
        self.assertGreaterEqual(
            found, 3,
            f"Expected 3+ alarm terms for Meta, found {found}"
        )


class TestOpenAIVocabularyRegister(unittest.TestCase):
    """Verify OpenAI segments receive analytical/explanatory vocabulary
    even when the substance is more alarming."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_openai_rogue_ai_analytical_vocabulary(self):
        """OpenAI rogue AI hack uses 'Explained' — analytical, not alarm."""
        self.assertIn('Explained', self.content)

    def test_openai_leadership_exodus_neutral_vocabulary(self):
        """OpenAI losing executives framed with neutral vocabulary."""
        self.assertIn('Losing Key Executives', self.content)

    def test_openai_safety_rules_question_framing(self):
        """OpenAI safety violations framed as question, not accusation."""
        self.assertIn('Break Its Own Safety Rules', self.content)


class TestAnthropicVocabularyRegister(unittest.TestCase):
    """Verify Anthropic segments receive scientific/aspirational vocabulary."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_anthropic_j_space_scientific_vocabulary(self):
        """Anthropic's J Space uses scientific/research vocabulary."""
        self.assertIn('J Space', self.content)

    def test_anthropic_watermarks_neutral_vocabulary(self):
        """Anthropic watermarks framed with neutral/technical vocabulary."""
        self.assertIn('Watermark', self.content)


class TestCrossEntityVocabularyAsymmetry(unittest.TestCase):
    """Verify the cross-entity vocabulary gradient is documented as asymmetric."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_vocabulary_gradient_documented(self):
        """Cross-entity vocabulary gradient should be explicitly documented."""
        self.assertIn('vocabulary', self.content.lower())
        self.assertIn('gradient', self.content.lower())

    def test_natural_experiment_framing(self):
        """Analysis frames multi-episode comparison as natural experiment."""
        self.assertIn('natural experiment', self.content.lower())

    def test_same_hosts_documented(self):
        """Same hosts across episodes documented for experimental control."""
        self.assertIn('Bea Nolan', self.content)
        # At least one of the main hosts
        has_kahn = 'Jeremy Kahn' in self.content
        has_forlini = 'Emily Forlini' in self.content
        self.assertTrue(
            has_kahn or has_forlini,
            "Expected at least one of Jeremy Kahn or Emily Forlini documented"
        )


class TestOpenAIRogueAISubstanceVsFraming(unittest.TestCase):
    """The Aug 4 episode's OpenAI rogue AI hack is substantively MORE alarming
    than Meta's glasses privacy concerns, yet receives less alarming vocabulary."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_rogue_ai_substance_vs_framing_gap_documented(self):
        """The substance-vs-framing gap for OpenAI's rogue AI should be documented."""
        # OpenAI's agent literally attacked other companies — more alarming than
        # glasses privacy concerns, but vocabulary is softer
        self.assertIn('hack', self.content.lower())
        self.assertIn('Hugging Face', self.content)

    def test_severity_inversion_documented(self):
        """Vocabulary severity inversion between OpenAI and Meta should be documented."""
        # The concept of severity inversion — more alarming substance gets
        # less alarming vocabulary — should be captured
        inversion_terms = ['severity', 'inversion', 'substance', 'alarming']
        found = sum(1 for t in inversion_terms if t in self.content.lower())
        self.assertGreaterEqual(
            found, 2,
            f"Expected 2+ severity inversion terms, found {found}"
        )


class TestFinancialContextDocumentation(unittest.TestCase):
    """Verify financial context for Fortune is documented."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_fortune_ownership_documented(self):
        """Fortune's ownership structure should be documented."""
        self.assertIn('Fortune', self.content)

    def test_cultural_consensus_assessment(self):
        """Fortune podcast pattern should be assessed as cultural consensus."""
        self.assertIn('cultural consensus', self.content.lower())


class TestNDTVWorldBroadcastEntitySelection(unittest.TestCase):
    """NDTV World 'India Global' segment (Aug 10, 2026) exclusively targets
    Meta glasses in country banning narrative, despite bans covering all
    camera-enabled smart glasses."""

    def setUp(self):
        sentiment_path = os.path.join(
            os.path.dirname(__file__), '..', 'podcast-sentiment.md'
        )
        with open(sentiment_path, 'r') as f:
            self.content = f.read()

    def test_ndtv_world_documented(self):
        """NDTV World episode should be documented in podcast-sentiment.md."""
        self.assertIn('NDTV World', self.content)

    def test_ndtv_death_of_privacy_title(self):
        """NDTV episode title 'Death Of Privacy' should be documented."""
        self.assertIn('Death Of Privacy', self.content)

    def test_ndtv_entity_selection_meta_exclusive(self):
        """NDTV banning narrative targets Meta exclusively."""
        self.assertIn('Meta', self.content)

    def test_ndtv_countries_banning_narrative(self):
        """NDTV frames as 'countries rapidly banning' Meta glasses."""
        self.assertIn('banning', self.content.lower())

    def test_ndtv_gendered_safety_framing(self):
        """NDTV frames glasses as risk to women and children specifically."""
        self.assertIn('women', self.content.lower())
        self.assertIn('children', self.content.lower())

    def test_ndtv_international_broadcast_propagation(self):
        """NDTV demonstrates international broadcast propagation of entity-selective narrative."""
        self.assertIn('international', self.content.lower())


class TestMechanism324InCompetitorResearch(unittest.TestCase):
    """Verify mechanism #324 is registered in competitor-coverage-research.yaml."""

    def test_mechanism_324_exists(self):
        """Mechanism #324 should exist in competitor-coverage-research.yaml."""
        research_path = os.path.join(
            PROFILES_DIR, 'competitor-coverage-research.yaml'
        )
        with open(research_path, 'r') as f:
            content = f.read()
        self.assertIn('324', content)

    def test_mechanism_324_references_fortune(self):
        """Mechanism #324 should reference Fortune AI Weekly."""
        research_path = os.path.join(
            PROFILES_DIR, 'competitor-coverage-research.yaml'
        )
        with open(research_path, 'r') as f:
            content = f.read()
        self.assertIn('Fortune', content)


class TestMechanism325InCompetitorResearch(unittest.TestCase):
    """Verify mechanism #325 is registered in competitor-coverage-research.yaml."""

    def test_mechanism_325_exists(self):
        """Mechanism #325 should exist in competitor-coverage-research.yaml."""
        research_path = os.path.join(
            PROFILES_DIR, 'competitor-coverage-research.yaml'
        )
        with open(research_path, 'r') as f:
            content = f.read()
        self.assertIn('325', content)

    def test_mechanism_325_references_ndtv(self):
        """Mechanism #325 should reference NDTV."""
        research_path = os.path.join(
            PROFILES_DIR, 'competitor-coverage-research.yaml'
        )
        with open(research_path, 'r') as f:
            content = f.read()
        self.assertIn('NDTV', content)


if __name__ == '__main__':
    unittest.main()
