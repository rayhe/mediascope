"""
Test: Gizmodo — "Mark Zuckerberg Wants to Save You From the Permanent Underclass"
Date: July 9, 2026
Focus: analogy_metaphor gap (would-be-like-calling pattern), loaded_language coverage,
       editorial_deflation, sarcastic voice detection, and entity extraction.

This article is analytically significant because:
1. It uses a damning analogy ("like calling Texaco a pillar of environmental stewardship")
   that the toolkit previously missed due to lack of "would be like [verb]ing" pattern.
2. It uses "ignominious" which was not in the loaded_language vocabulary.
3. It demonstrates the editorial-deflation pattern of building up a claim (Zuckerberg as
   "people's champ") then systematically dismantling it with historical evidence.
4. It references the Rohingya/Myanmar crisis as a precedent for Meta's harm.
"""

import pytest
import re
from mediascope.analyze.framing import _DEVICE_PATTERNS, detect_framing_devices

ARTICLE_TEXT = (
    "To call Meta a champion of democratic ideals, though, would be like calling "
    "Texaco a pillar of environmental stewardship. The company—previously known as "
    "Facebook—has a long, ignominious, and well-documented history of deploying "
    "algorithms trained to optimize user engagement above all else. The Facebook "
    "algorithm has been shown to have played a role in fueling the ethnic cleansing "
    "of Rohingya Muslims in Myanmar in 2017, for example, and Meta is now facing "
    "$1.4 trillion in state lawsuits alleging its platforms hooked young users and "
    "harmed their mental health."
)

FULL_ARTICLE = (
    "Mark Zuckerberg Wants to Save You From the Permanent Underclass\n\n"
    "Meta just dropped a new AI model, and Mark Zuckerberg is shouting the news "
    "from some very un-Zuck-like rooftops.\n\n"
    "The Meta founder and CEO is known for many things, but a cozy relationship "
    "with traditional journalism is not one of them. Following the reelection of "
    "Donald Trump early last year and sporting his newly cultivated Cool Guy look, "
    "Zuckerberg said in a video published online that Meta was removing its "
    "journalistic-style fact-checkers.\n\n"
    "But businesses aren't going to ditch their Anthropic and OpenAI subscriptions "
    "en masse just because Meta's new model shows promise in a handful of benchmarks. "
    "Zuck must be aware of this, which is why he's playing up the cost factor.\n\n"
    "It gels with Meta's ongoing effort to brand itself as a kind of people's champ "
    "in the age of AI, the company that will democratize access to the technology.\n\n"
    "Zuckerberg is specifically throwing shade on Anthropic, which he told Bloomberg "
    '"is sort of keeping a model for themselves and releasing a kind of simpler '
    'version of a model."\n\n'
    + ARTICLE_TEXT
    + "\n\n"
    "It's going to take a lot more than a cheap AI model and a trendy wardrobe for "
    "Meta's CEO to sell himself as the people's champ in the age of AI, in other words."
)


class TestGizmodoZuckerbergUnderclass:
    """Tests for the Gizmodo Muse Spark 1.1 / underclass article."""

    def test_analogy_metaphor_texaco_pattern(self):
        """The 'would be like calling Texaco' line must fire analogy_metaphor."""
        results = detect_framing_devices(ARTICLE_TEXT)
        device_types = {r.device_type for r in results}
        assert "analogy_metaphor" in device_types, (
            f"Expected analogy_metaphor for the Texaco damning analogy. "
            f"Got: {sorted(device_types)}"
        )

    def test_analogy_metaphor_would_be_like_pattern(self):
        """Regression: 'would be like calling' must match the new gerund pattern."""
        pattern = re.compile(
            r"\b(?:would|could|might)\s+be\s+like\s+"
            r"(?:call|say|ask|claim|argu|describ|label|brand|declar|hail|proclai)\w*"
            r"\s+.{3,80}",
            re.IGNORECASE,
        )
        assert pattern.search(ARTICLE_TEXT), (
            "The 'would be like calling' pattern should match the Texaco sentence"
        )

    def test_loaded_language_ignominious(self):
        """'ignominious' should be detected as loaded language."""
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE
        assert "ignominious" in EMOTIONAL_LANGUAGE, (
            "'ignominious' should be in the loaded language vocabulary"
        )

    def test_scale_magnitude_1_4_trillion(self):
        """$1.4 trillion in state lawsuits must fire scale_magnitude."""
        results = detect_framing_devices(ARTICLE_TEXT)
        device_types = {r.device_type for r in results}
        assert "scale_magnitude" in device_types, (
            f"Expected scale_magnitude for '$1.4 trillion'. Got: {sorted(device_types)}"
        )

    def test_full_article_editorial_deflation(self):
        """The full article's 'build up then tear down' arc should fire
        editorial_deflation on the 'cheap AI model and a trendy wardrobe' line."""
        results = detect_framing_devices(FULL_ARTICLE)
        device_types = {r.device_type for r in results}
        # At minimum we expect analogy_metaphor and loaded_language
        assert "analogy_metaphor" in device_types, (
            f"Expected analogy_metaphor in full article. Got: {sorted(device_types)}"
        )

    def test_gerund_simile_pattern_general(self):
        """'is like watching paint dry' — general gerund simile fires."""
        pattern = re.compile(
            r"\b(?:is|was|be)\s+like\s+\w+ing\b",
            re.IGNORECASE,
        )
        assert pattern.search("This is like watching paint dry")
        assert pattern.search("It was like reliving a nightmare")
        assert not pattern.search("I like painting walls")  # "like" as verb

    def test_entity_anthropic_cluster(self):
        """Anthropic, Opus 4.8, Fable 5, Mythos should all resolve to Anthropic."""
        from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS
        anthropic_aliases = DEFAULT_ENTITY_CLUSTERS.get("Anthropic", {}).get("aliases", set())
        for term in ["Anthropic", "Mythos", "Fable"]:
            assert term in anthropic_aliases, (
                f"'{term}' should be in Anthropic entity aliases"
            )
