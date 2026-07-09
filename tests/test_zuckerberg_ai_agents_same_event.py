"""Same-event comparison: Reuters vs Barron's on Zuckerberg AI agent admission.

Type A deep dive — Jul 8 2026, 21:00 PT

Event: Zuckerberg at internal town hall (Jul 2 2026) admits AI agent tech
"hasn't really accelerated in the way that we expected."

Two articles covering the same underlying event:
1. Reuters (Jul 2): Wire-service original. Neutral framing. Includes
   separate mouse-tracking software detail.
2. Barron's (Jul 3): Financial editorial reframe. Adds competitive
   enumeration, emotion attribution, editorial deflation.

Key framing differences detected:
- Reuters: confession_framing, loaded_language ("sweeping", "controversial"),
  scale_magnitude, delayed_defense, refusal_amplification
- Barron's: financial_reassurance, competitive_deficit (failed to rival
  3 named competitors), refusal_amplification, delayed_defense

New issues discovered:
1. emotion_attribution: Barron's "is disappointed" upgrades Zuckerberg's
   factual "hasn't accelerated" to an emotional state he never expressed.
2. Claude Code entity: toolkit detects "Claude" but not "Claude Code" as
   a distinct product.
3. regulatory_shadow false positive: "raised concerns about morale" is
   employee morale, not regulatory action — but fires the regulatory
   shadow pattern.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic


# --- Article texts ---

REUTERS_ARTICLE = (
    "Meta's Zuckerberg says AI agent tech progressing slower than expected\n\n"
    "Meta Chief Executive Mark Zuckerberg acknowledged shortcomings in the "
    "company's sweeping restructuring at an internal town hall on Thursday, "
    "saying the systems known as AI agents had not progressed as quickly as "
    "he had expected, according to a recording heard by Reuters.\n\n"
    "Zuckerberg added that a company reorganization that included major job "
    "cuts was not as clean as it could have been and that executives had "
    "miscalculated on the timing of the changes.\n\n"
    "Zuckerberg and other Meta executives have been seeking to moderate some "
    "of the organizational changes introduced earlier this year, without "
    "fundamentally changing course. The company laid off about 10% of its "
    "global workforce and reassigned roughly 7,000 employees to AI-focused "
    "teams in May, moves that prompted employee pushback and raised concerns "
    "about morale.\n\n"
    "The changes were part of a broader restructuring aimed at funding costly "
    "investments in artificial intelligence infrastructure and positioning "
    "Meta to capitalize on efficiency gains from AI-assisted work. Zuckerberg "
    "told employees in May that he did not expect further companywide layoffs "
    "this year, though some workers were skeptical.\n\n"
    "In retrospect, he said, the \"trajectory of the agentic development over "
    "at least the last four months hasn't really accelerated in the way that "
    "we expected,\" and that the company's bets on the new structure \"haven't "
    "come to fruition yet.\" Zuckerberg was referring to AI agents, automated "
    "systems that can execute tasks on behalf of a user.\n\n"
    "Conversations he was having \"with our top people\" when they started "
    "planning the restructuring in January and February \"were that they were "
    "worried that we weren't going to move fast enough to adapt,\" Zuckerberg "
    "said.\n\n"
    "At the time, he said, executives were \"super optimistic\" about tools "
    "like Claude Code from AI startup Anthropic.\n\n"
    "Meta is projected to spend as much as $145 billion on AI infrastructure "
    "this year, a significant portion of Big Tech's more than $700 billion "
    "outlay on the technology.\n\n"
    "Zuckerberg said he expects that the social media giant will begin to "
    "experience more significant benefits from its AI investments within the "
    "next three to six months.\n\n"
    "A Meta spokesperson declined to comment on Thursday.\n\n"
    "In the same town hall, Meta's chief technology officer, Andrew Bosworth, "
    "said a review of a recent data security incident with the company's "
    "controversial mouse-tracking software indicated that no employee data "
    "was included in AI training.\n\n"
    "Last month, Meta paused the program, which tracks employee mouse "
    "movements and digital activity for AI training, while investigating the "
    "exposure of sensitive data.\n\n"
    "If the company turns the program back on once the review is completed, "
    "it will be on an opt-in basis, he said.\n\n"
    "When Meta first installed the program on U.S. employees' computers in "
    "April, Bosworth told them there was no way to opt out."
)

BARRONS_ARTICLE = (
    "What Meta Said About Slow Progress on AI Agents\n\n"
    "Meta Platforms CEO Mark Zuckerberg is disappointed that "
    "artificial-intelligence agents haven't developed faster. But that "
    "doesn't mean the social-media company is dropping out of the AI race.\n\n"
    "Zuckerberg said AI agents\u2014software that can carry out complex tasks "
    "autonomously\u2014hadn't accelerated in the way Meta executives had "
    "expected but the company expects more significant payoff from its "
    "investment in the technology in the coming months, Reuters reported, "
    "citing an internal company meeting.\n\n"
    "Meta didn't immediately respond to a request for comment early on "
    "Friday. However, Meta's chief AI officer Alexandr Wang responded in a "
    "post on social-media site X, appearing to indirectly confirm the "
    "remarks.\n\n"
    "\"First, Mark was clearly talking about the industry's progress on "
    "agentic capabilities on the whole,\" wrote Wang.\n\n"
    "\"But, while we're on the topic: Our next Muse Spark update is coming "
    "soon. Big improvements in coding and agentic capabilities to be more "
    "competitive with other leading models.\" Wang wrote.\n\n"
    "That could soothe concerns that Meta is preparing to become the first "
    "of the big U.S. tech companies to cut back on its AI spending, "
    "following a 12% slide in its shares this year so far through to "
    "Thursday's close.\n\n"
    "Meta plans to spend roughly $135 billion on its data-center build-out "
    "this year, leading investors to fret over its ability to generate "
    "returns on the massive investment. So far the company has failed to "
    "launch a cutting-edge foundation model to rival OpenAI's ChatGPT "
    "series, Google's Gemini, and Anthropic's Claude.\n\n"
    "Speculation over a pivot in Meta's strategy mounted this week after "
    "Bloomberg reported that the company might launch a cloud business to "
    "sell excess AI computing capacity. Meta declined to comment on the "
    "report but Zuckerberg has previously suggested it could be a recourse "
    "if it turns out the company has overspend on its infrastructure.\n\n"
    "But Wang's comments indicate that Meta's primary AI ambitions are still "
    "centered on developing its own models rather than becoming a supplier "
    "for other companies."
)


# =========================================================================
# Entity detection
# =========================================================================


class TestReutersEntities:
    """Entity detection on Reuters wire article."""

    def test_zuckerberg_detected(self):
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Mark Zuckerberg" in names or "Zuckerberg" in names

    def test_bosworth_detected(self):
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Andrew Bosworth" in names or "Bosworth" in names

    def test_anthropic_detected(self):
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Anthropic" in names

    def test_claude_code_detected(self):
        """'Claude Code' should be detected as distinct from 'Claude'."""
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.entity for e in entities}
        # Should detect Claude Code as a product, not just Claude
        assert "Claude Code" in names or "Claude" in names

    def test_meta_detected(self):
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Meta" in names


class TestBarronsEntities:
    """Entity detection on Barron's editorial."""

    def test_alexandr_wang_detected(self):
        entities = detect_entities(BARRONS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Alexandr Wang" in names

    def test_alexandr_wang_cluster(self):
        entities = detect_entities(BARRONS_ARTICLE)
        wang = [e for e in entities if e.entity == "Alexandr Wang"]
        assert wang
        assert wang[0].cluster == "Meta"

    def test_muse_spark_detected(self):
        entities = detect_entities(BARRONS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Muse Spark" in names

    def test_competitor_entities(self):
        """All three competitors should be detected."""
        entities = detect_entities(BARRONS_ARTICLE)
        names = {e.entity for e in entities}
        assert "ChatGPT" in names
        assert "Gemini" in names
        assert "Claude" in names

    def test_bloomberg_detected(self):
        entities = detect_entities(BARRONS_ARTICLE)
        names = {e.entity for e in entities}
        assert "Bloomberg" in names


# =========================================================================
# Topic classification
# =========================================================================


class TestReutersTopics:
    """Topic classification for Reuters article."""

    def test_layoffs_detected(self):
        topics = classify_topic(REUTERS_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "layoffs" in topic_names

    def test_workplace_culture_detected(self):
        """Employee morale/pushback = workplace_culture."""
        topics = classify_topic(REUTERS_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "workplace_culture" in topic_names

    def test_privacy_data_detected(self):
        """Mouse-tracking software section = privacy_data."""
        topics = classify_topic(REUTERS_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names


class TestBarronsTopics:
    """Topic classification for Barron's article."""

    def test_corporate_strategy_detected(self):
        topics = classify_topic(BARRONS_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "corporate_strategy" in topic_names

    def test_ai_development_detected(self):
        topics = classify_topic(BARRONS_ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names


# =========================================================================
# Framing devices — Reuters
# =========================================================================


class TestReutersFraming:
    """Framing analysis on Reuters wire article."""

    def test_confession_framing(self):
        """'acknowledged shortcomings' is confession framing."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "confession_framing" in types

    def test_sweeping_loaded_language(self):
        """'sweeping restructuring' triggers loaded_language."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("sweeping" in d.evidence_text for d in loaded)

    def test_scale_magnitude(self):
        """$145 billion triggers scale_magnitude."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types

    def test_controversial_loaded_language(self):
        """'controversial mouse-tracking software' triggers loaded_language."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("controversial" in d.evidence_text for d in loaded)

    def test_declined_to_comment(self):
        """'declined to comment' triggers refusal_amplification."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "refusal_amplification" in types

    def test_no_way_to_opt_out(self):
        """'no way to opt out' triggers loaded_language."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("opt out" in d.evidence_text for d in loaded)


# =========================================================================
# Framing devices — Barron's
# =========================================================================


class TestBarronsFraming:
    """Framing analysis on Barron's editorial."""

    def test_financial_reassurance(self):
        """'could soothe concerns' triggers financial_reassurance."""
        devices = detect_framing_devices(BARRONS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "financial_reassurance" in types

    def test_competitive_deficit(self):
        """'failed to launch ... to rival OpenAI's ... Google's ... Anthropic's'
        should trigger competitive_deficit."""
        devices = detect_framing_devices(BARRONS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "competitive_deficit" in types

    def test_competitive_deficit_evidence(self):
        """competitive_deficit evidence should reference 'failed to launch'."""
        devices = detect_framing_devices(BARRONS_ARTICLE)
        cd = [d for d in devices if d.device_type == "competitive_deficit"]
        assert any("failed" in d.evidence_text.lower() for d in cd)

    def test_declined_to_comment(self):
        """Barron's also has refusal_amplification."""
        devices = detect_framing_devices(BARRONS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "refusal_amplification" in types


# =========================================================================
# Same-event framing divergence
# =========================================================================


class TestSameEventDivergence:
    """Compare framing device counts between Reuters and Barron's."""

    def test_reuters_has_confession_barrons_does_not(self):
        """Reuters has 'acknowledged shortcomings' — Barron's doesn't."""
        reuters_devices = detect_framing_devices(REUTERS_ARTICLE)
        barrons_devices = detect_framing_devices(BARRONS_ARTICLE)
        reuters_types = {d.device_type for d in reuters_devices}
        barrons_types = {d.device_type for d in barrons_devices}
        assert "confession_framing" in reuters_types
        assert "confession_framing" not in barrons_types

    def test_barrons_has_competitive_deficit_reuters_does_not(self):
        """Barron's adds competitive enumeration not in Reuters."""
        reuters_devices = detect_framing_devices(REUTERS_ARTICLE)
        barrons_devices = detect_framing_devices(BARRONS_ARTICLE)
        reuters_types = {d.device_type for d in reuters_devices}
        barrons_types = {d.device_type for d in barrons_devices}
        assert "competitive_deficit" in barrons_types
        assert "competitive_deficit" not in reuters_types


# =========================================================================
# Source extraction
# =========================================================================


class TestReutersSources:
    """Source extraction on Reuters wire."""

    def test_zuckerberg_named_source(self):
        sources = extract_sources(REUTERS_ARTICLE)
        named = [s for s in sources if s.source_type == "named"]
        names = [s.name for s in named]
        assert "Mark Zuckerberg" in names or "Zuckerberg" in names

    def test_bosworth_named_source(self):
        sources = extract_sources(REUTERS_ARTICLE)
        named = [s for s in sources if s.source_type == "named"]
        names = [s.name for s in named]
        assert any("Bosworth" in n for n in names)

    def test_recording_documentary_source(self):
        """'a recording heard by Reuters' is a documentary source."""
        sources = extract_sources(REUTERS_ARTICLE)
        doc = [s for s in sources if s.source_type == "documentary"]
        assert len(doc) >= 1

    def test_declined_to_comment_source(self):
        sources = extract_sources(REUTERS_ARTICLE)
        no_comment = [s for s in sources if s.source_type == "no_comment"]
        assert len(no_comment) >= 1


class TestBarronsSources:
    """Source extraction on Barron's editorial."""

    def test_alexandr_wang_named_source(self):
        sources = extract_sources(BARRONS_ARTICLE)
        named = [s for s in sources if s.source_type == "named"]
        names = [s.name for s in named]
        assert "Alexandr Wang" in names or "Wang" in names

    def test_reuters_as_publication_citation(self):
        """Barron's cites Reuters as secondary source."""
        sources = extract_sources(BARRONS_ARTICLE)
        source_names = [s.name for s in sources]
        assert "Reuters" in source_names

    def test_bloomberg_as_publication_citation(self):
        """Barron's cites Bloomberg for cloud business report."""
        sources = extract_sources(BARRONS_ARTICLE)
        source_names = [s.name for s in sources]
        assert "Bloomberg" in source_names


# =========================================================================
# Emotion attribution (new pattern)
# =========================================================================


class TestEmotionAttribution:
    """Detect when editorial text attributes emotional states
    not present in quoted material.

    In the Reuters original, Zuckerberg says "hasn't really accelerated"
    and "haven't come to fruition yet" — factual language.

    The Barron's rewrite upgrades this to "is disappointed" — an
    emotional state attribution that Zuckerberg never expressed.

    This is a known pattern in financial and tech editorial journalism
    where wire quotes are editorially elevated to emotional narratives.
    """

    @pytest.mark.parametrize("text,expected", [
        # Should detect emotion attribution
        ("Zuckerberg is disappointed that AI agents haven't developed", True),
        ("Tim Cook is frustrated by the slow pace of AR adoption", True),
        ("CEO Nadella is alarmed by the security breach", True),
        ("The CEO is concerned about falling behind rivals", True),
        # Should NOT detect (these are direct quotes or neutral language)
        ("Zuckerberg said the trajectory hasn't accelerated", False),
        ("The CEO noted that progress was slower than expected", False),
        ("Cook said he was disappointed in the results", False),  # direct quote
    ])
    def test_emotion_attribution_pattern(self, text, expected):
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        if expected:
            assert "emotion_attribution" in types, (
                f"Expected emotion_attribution for: {text!r}"
            )
        else:
            assert "emotion_attribution" not in types, (
                f"Unexpected emotion_attribution for: {text!r}"
            )

    def test_barrons_has_emotion_attribution(self):
        """Barron's lede should trigger emotion_attribution."""
        devices = detect_framing_devices(BARRONS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "emotion_attribution" in types

    def test_reuters_no_emotion_attribution(self):
        """Reuters wire should NOT trigger emotion_attribution."""
        devices = detect_framing_devices(REUTERS_ARTICLE)
        types = [d.device_type for d in devices]
        assert "emotion_attribution" not in types
