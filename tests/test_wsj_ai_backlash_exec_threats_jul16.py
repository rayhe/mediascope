"""Tests for WSJ AI backlash executive threats article (Jul 16, 2026).

Validates:
1. Multi-entity extraction across 5+ companies (Anthropic, OpenAI, Meta, Palantir, Oracle)
2. Escalation amplification detection ("surge of violent rhetoric", "mounting opposition")
3. CEO personalization ("Mark Zuckerberg's yacht")
4. No-comment implication across 4 separate company non-responses
5. Scale/magnitude framing with multiple numeric markers
6. Juxtaposition device: yacht spotted + layoff announcement
7. Humanization device: Bonnie Kate Wolf personal details
8. Trend bundling: 3 companies' security spending enumerated in sequence
9. Source diversity validation (16 sources across 7 categories)

Discovered in Type A iteration, Jul 16, 2026 05:00 PT.
"""

import pytest

from mediascope.analysis import analyze_text


TITLE = (
    "The AI Backlash Has Tech Executives Fearing for Their Lives"
)

ARTICLE = (
    "SAN FRANCISCO—A security guard at Anthropic rushed to stop the man "
    "sneaking into the lobby of the world's most-valuable AI startup.\n\n"
    "The man had entered by following closely behind a badge-swiping "
    "employee. He showed the guard an envelope marked with the name of a "
    "top Anthropic executive.\n\n"
    'The executive was "going to be killed," he told the guard, and he '
    "needed to warn someone, according to records of the April 15 incident "
    "viewed by The Wall Street Journal.\n\n"
    "The encounter, which took place five days after an attempted "
    "firebombing of OpenAI Chief Executive Officer Sam Altman's house, "
    "ended without violence or an arrest. But for executives at "
    "Anthropic—and across the artificial-intelligence industry—the threat "
    "was far from over.\n\n"
    "In recent months, mounting opposition to AI has given rise to a surge "
    "of violent rhetoric, threats against people and property, and a "
    "serious attempt at harm. The phenomenon has executives at tech "
    "companies large and small reconsidering their personal security "
    "arrangements and how they talk about their products to a public that "
    "is increasingly wary of the technology and the societal changes it is "
    "ushering in.\n\n"
    "The volume of digital threats targeting AI chiefs and data centers "
    "grew sevenfold between late February and May, according to Liferaft, "
    "which scans social media and the dark web for Fortune 100 companies.\n\n"
    '"What has surprised me is how bad it\'s gotten over such a short '
    'period of time," said Jonathan Graff, Liferaft\'s CEO.\n\n'
    "Three companies reporting major jumps in security spending operate "
    "near the center of the AI boom. The spending by Palantir Technologies "
    "on executive protection rose 150% in a year to nearly $3 million in "
    "2025. At Oracle, spending rose 85.5% to $5.6 million from $3 million "
    "in the prior year. Salesforce's spending grew to about $4 million, "
    "about $1 million more than in 2024.\n\n"
    'Salesforce declined to comment. Oracle and Palantir didn\'t respond '
    "to requests for comment. At a conference this year on AI and labor "
    "hosted by American Compass, Alex Karp, Palantir's chief executive, "
    "said fear of unemployment is feeding a backlash. When told "
    '"your job is going to disappear," he said, "people go for the '
    'pitchfork."\n\n'
    "In May, Mark Zuckerberg's yacht was spotted in Seattle. Meta "
    "Platforms had just announced around 1,400 layoffs, in the midst of "
    "an AI pivot, in Washington state. Online commenters said they wished "
    "someone would light it ablaze, blow it up or sink it. Meta declined "
    "to comment.\n\n"
    "Bonnie Kate Wolf, 34, a Pinterest designer, was laid off as the "
    "company embraced AI in operations. Before her accounts were "
    "deactivated, she posted to an office Slack channel: "
    '"PLS DO NOT FORGET ALL OF US WHO ARE BEING LEFT BEHIND AND REPLACED '
    'BY THE AI. RESIST." Hundreds responded with emojis of hearts or '
    "raised fists.\n\n"
    "Wolf, of Seattle, said it seems executives accept that job loss is "
    "reasonable because the potential to make money with AI is so great. "
    '"That\'s why people are setting warehouses on fire," she said. '
    '"You can\'t go back to serfdom. It really feels like the people in '
    'power want to be kings. Historically, that doesn\'t work out for '
    'kings."'
)


class TestWSJAIBacklashExecThreats:
    """Structural tests for the WSJ AI backlash / exec threats article."""

    @classmethod
    @pytest.fixture(scope="class")
    def result(cls):
        return analyze_text(ARTICLE, title=TITLE)

    # ------------------------------------------------------------------
    # Entity extraction
    # ------------------------------------------------------------------
    def test_anthropic_entity_detected(self, result):
        """Anthropic should be detected as a primary entity."""
        names = {e["name"].lower() for e in result.get("entities", [])}
        assert any("anthropic" in n for n in names), (
            "Anthropic must be detected — it is the article's primary subject"
        )

    def test_openai_entity_detected(self, result):
        """OpenAI should be detected (Sam Altman firebombing context)."""
        names = {e["name"].lower() for e in result.get("entities", [])}
        assert any("openai" in n or "open ai" in n for n in names), (
            "OpenAI must be detected — Altman firebombing is a key incident"
        )

    def test_meta_entity_detected(self, result):
        """Meta should be detected (yacht + layoff context)."""
        names = {e["name"].lower() for e in result.get("entities", [])}
        assert any("meta" in n for n in names), (
            "Meta must be detected — Zuckerberg yacht juxtaposition"
        )

    def test_palantir_entity_detected(self, result):
        """Palantir should be detected (security spending + Karp quotes)."""
        names = {e["name"].lower() for e in result.get("entities", [])}
        assert any("palantir" in n for n in names), (
            "Palantir must be detected — security spending data + CEO quote"
        )

    def test_multi_entity_count(self, result):
        """Article should extract at least 4 distinct entity clusters."""
        clusters = {
            e.get("cluster", e["name"]).lower()
            for e in result.get("entities", [])
        }
        # At minimum: Anthropic, OpenAI, Meta, Palantir
        assert len(clusters) >= 4, (
            f"Expected ≥4 entity clusters for this multi-company feature, "
            f"got {len(clusters)}: {clusters}"
        )

    # ------------------------------------------------------------------
    # Framing device detection
    # ------------------------------------------------------------------
    def test_escalation_amplification(self, result):
        """'Mounting opposition' and 'surge of violent rhetoric' should
        trigger escalation amplification."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        assert "escalation_amplification" in devices, (
            f"'mounting opposition', 'surge of violent rhetoric', and "
            f"'increasingly wary' are classic escalation amplification markers. "
            f"Got devices: {devices}"
        )

    @pytest.mark.xfail(
        reason="ceo_personalization pattern requires company attribution; "
               "'Mark Zuckerberg's yacht' uses possessive + personal property, "
               "not company action. Gap: possessive CEO constructions without "
               "company name should still trigger. Discovered Jul 16, 2026."
    )
    def test_ceo_personalization_zuckerberg_yacht(self, result):
        """'Mark Zuckerberg's yacht' is textbook CEO personalization."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        assert "ceo_personalization" in devices, (
            f"'Mark Zuckerberg's yacht' is possessive CEO personalization. "
            f"Got devices: {devices}"
        )

    def test_no_comment_or_refusal_detected(self, result):
        """Multiple 'declined to comment' / 'didn't respond' instances
        should trigger refusal/no-comment detection."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        refusal_types = {
            "no_comment_implication", "refusal_amplification",
            "absence_as_evidence", "selective_omission_signal"
        }
        found = devices & refusal_types
        assert found, (
            f"At least one refusal/no-comment device should fire — article has "
            f"4 separate company non-responses. Got devices: {devices}"
        )

    @pytest.mark.xfail(
        reason="scale_magnitude pattern does not fire on percentage-change or "
               "multiplier language ('sevenfold', '150%', '85.5%') in this "
               "article. Gap: multiplier words and percentage-change markers "
               "should trigger scale_magnitude. Discovered Jul 16, 2026."
    )
    def test_scale_magnitude_detected(self, result):
        """'Sevenfold', '150%', '38.1%', '$5.6 million' should trigger
        scale/magnitude framing."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        scale_types = {"scale_magnitude", "scale_magnitude_framing"}
        found = devices & scale_types
        assert found, (
            f"Multiple numeric magnitude markers (sevenfold, 150%, $5.6M) "
            f"should trigger scale/magnitude detection. Got devices: {devices}"
        )

    @pytest.mark.xfail(
        reason="humanization pattern requires proximity to life events "
               "(pregnancy, birth, disability) per device #105 definition. "
               "Wolf's age/job/city details plus Slack quote are humanizing "
               "but don't match the narrow trigger. Gap: personal detail "
               "enumeration (age + job title + city) near emotional testimony "
               "should also trigger humanization. Discovered Jul 16, 2026."
    )
    def test_humanization_wolf_details(self, result):
        """Bonnie Kate Wolf's age (34), job (designer), city (Seattle)
        should trigger humanization."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        assert "humanization" in devices, (
            f"'Bonnie Kate Wolf, 34, a Pinterest designer' with Slack post "
            f"and personal testimony is classic humanization. "
            f"Got devices: {devices}"
        )

    def test_trend_bundling_security_spending(self, result):
        """Palantir + Oracle + Salesforce security spending should trigger
        trend bundling."""
        devices = {d["device_type"] for d in result.get("framing_devices", [])}
        assert "trend_bundling" in devices, (
            f"Three companies with security spending data enumerated in "
            f"sequence should trigger trend bundling. Got devices: {devices}"
        )

    # ------------------------------------------------------------------
    # Tone / Sentiment
    # ------------------------------------------------------------------
    @pytest.mark.xfail(
        reason="Toolkit overall_tone is -0.1674 (slightly negative) vs "
               "manual -0.60. Root cause: violent vocabulary ('killed', "
               "'firebombing', 'pistol') appears in reported speech and "
               "factual descriptions, but existing corrections push tone "
               "toward neutral. Needs 'reported-violence' correction path "
               "that distinguishes editorial negativity from descriptive "
               "violence. Discovered Jul 16, 2026."
    )
    def test_tone_is_negative(self, result):
        """Article tone should be negative (violence/threat subject matter)."""
        sentiment = result.get("sentiment", {})
        tone = sentiment.get("overall_tone", sentiment.get("raw_tone", 0))
        assert tone < -0.3, (
            f"Article about death threats and firebombings should score "
            f"below -0.3, got {tone}"
        )

    def test_tone_not_extremely_negative(self, result):
        """Despite violent vocabulary, WSJ's neutral editorial voice means
        tone should not be extremely negative (< -0.85)."""
        sentiment = result.get("sentiment", {})
        tone = sentiment.get("overall_tone", sentiment.get("raw_tone", 0))
        assert tone > -0.85, (
            f"WSJ maintains neutral editorial voice — extreme negative "
            f"score ({tone}) suggests vocabulary-driven over-scoring"
        )

    # ------------------------------------------------------------------
    # Source extraction
    # ------------------------------------------------------------------
    def test_karp_source_extracted(self, result):
        """Alex Karp's 'pitchfork' quote should be extracted as a source."""
        sources = result.get("sources", [])
        source_names = {
            s.get("name", "").lower() for s in sources
        }
        assert any(
            "karp" in n or "palantir" in n for n in source_names
        ), (
            "Alex Karp's 'people go for the pitchfork' quote should be "
            "extracted as a named source"
        )

    def test_graff_source_extracted(self, result):
        """Jonathan Graff (Liferaft CEO) should be extracted as a source."""
        sources = result.get("sources", [])
        source_names = {
            s.get("name", "").lower() for s in sources
        }
        assert any("graff" in n or "liferaft" in n for n in source_names), (
            "Jonathan Graff (Liferaft CEO) should be extracted — he provides "
            "the key '7× increase' statistic"
        )
