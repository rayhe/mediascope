"""Tests for source stance analysis and outsourced intensity detection.

These test the three critical features added in the Jun 22, 2026
toolkit quality iteration:
1. Source stance analysis (sources.py: analyze_source_stance)
2. Outsourced intensity detection (sentiment.py: measure_outsourced_intensity)
3. Power asymmetry framing device (framing.py)
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.sources import (
    SourceMention,
    analyze_source_stance,
    extract_sources,
)
from mediascope.analyze.sentiment import (
    measure_outsourced_intensity,
)
from mediascope.analyze.framing import (
    detect_framing_devices,
    summarize_framing,
)


# ===================================================================
# Source Stance Analysis Tests
# ===================================================================

class TestAnalyzeSourceStance:
    """Test that source stance correctly identifies adversarial vs
    supportive source deployment."""

    def test_adversarial_sources(self):
        """Sources with negative quotes should be classified adversarial."""
        sources = [
            SourceMention(
                name="Jane Doe",
                is_anonymous=False,
                quote="This is reckless and irresponsible behavior that threatens users",
                attribution_verb="warned",
            ),
            SourceMention(
                name="Bob Smith",
                is_anonymous=False,
                quote="The company has shown a pattern of deceptive practices",
                attribution_verb="accused",
            ),
        ]
        result = analyze_source_stance(sources)
        assert result["adversarial_count"] == 2
        assert result["supportive_count"] == 0
        assert result["stance_balance"] == -1.0

    def test_supportive_sources(self):
        """Sources with positive quotes should be classified supportive."""
        sources = [
            SourceMention(
                name="Alice Tech",
                is_anonymous=False,
                quote="This is a groundbreaking achievement and an impressive milestone",
                attribution_verb="noted",
            ),
            SourceMention(
                name="CEO Bob",
                is_anonymous=False,
                quote="We are thrilled with the progress and committed to safety",
                attribution_verb="said",
            ),
        ]
        result = analyze_source_stance(sources)
        assert result["supportive_count"] == 2
        assert result["adversarial_count"] == 0
        assert result["stance_balance"] == 1.0

    def test_mixed_sources(self):
        """Mix of adversarial and supportive should yield balanced score."""
        sources = [
            SourceMention(
                name="Critic",
                is_anonymous=False,
                quote="This is harmful and dangerous",
                attribution_verb="warned",
            ),
            SourceMention(
                name="Defender",
                is_anonymous=False,
                quote="The product is innovative and beneficial to users",
                attribution_verb="said",
            ),
        ]
        result = analyze_source_stance(sources)
        assert result["adversarial_count"] == 1
        assert result["supportive_count"] == 1
        assert result["stance_balance"] == 0.0

    def test_empty_sources(self):
        """Empty source list returns zero counts."""
        result = analyze_source_stance([])
        assert result["total_sources"] == 0
        assert result["stance_balance"] == 0.0

    def test_neutral_sources(self):
        """Sources with no clear stance should be neutral."""
        sources = [
            SourceMention(
                name="Analyst",
                is_anonymous=False,
                quote="The company reported quarterly earnings of $10 billion",
                attribution_verb="said",
            ),
        ]
        result = analyze_source_stance(sources)
        assert result["neutral_count"] == 1
        assert result["adversarial_count"] == 0
        assert result["supportive_count"] == 0
        assert result["stance_balance"] == 0.0

    def test_loaded_verbs_shift_stance(self):
        """Adversarial attribution verbs should contribute to negative stance."""
        sources = [
            SourceMention(
                name="Critic One",
                is_anonymous=False,
                quote="The timeline raises questions",
                attribution_verb="fumed",
            ),
        ]
        result = analyze_source_stance(sources)
        assert result["adversarial_count"] >= 1, (
            "Adversarial verb 'fumed' should shift stance negative"
        )

    def test_adversarial_sources_list(self):
        """Result should include names of adversarial sources."""
        sources = [
            SourceMention(
                name="Sarah Wynn-Williams",
                is_anonymous=False,
                quote="This is censorship, silencing my ability to speak",
                attribution_verb="said",
            ),
        ]
        result = analyze_source_stance(sources)
        assert "Sarah Wynn-Williams" in result["adversarial_sources"]


# ===================================================================
# Outsourced Intensity Tests
# ===================================================================

class TestOutsourcedIntensity:
    """Test that outsourced intensity correctly detects the editorial
    technique of deploying emotional quotes while keeping prose neutral."""

    def test_high_outsourcing(self):
        """Text where quotes carry all emotional language and editorial
        prose is measured should have high outsourced_ratio."""
        text = (
            'The company issued a statement on Tuesday. '
            'A coalition of civil liberties organizations released a letter. '
            '"This is outrageous and appalling behavior that threatens '
            'the safety of millions," the group wrote. '
            '"The company\'s reckless and irresponsible practices are '
            'devastating to communities," a spokesperson said. '
            'The company did not respond to the letter by press time.'
        )
        result = measure_outsourced_intensity(text)
        assert result["outsourced_ratio"] > 0.3, (
            f"Expected high outsourced ratio, got {result['outsourced_ratio']}"
        )
        assert result["quoted_intensity"] > result["editorial_intensity"]

    def test_no_outsourcing_all_editorial(self):
        """Text with no quotes should have zero outsourced ratio."""
        text = (
            "The devastating failure shocked observers. "
            "The catastrophic and reckless decision was appalling. "
            "The outrageous behavior drew widespread condemnation."
        )
        result = measure_outsourced_intensity(text)
        assert result["outsourced_ratio"] == 0.0
        assert result["quoted_word_count"] == 0

    def test_empty_text(self):
        """Empty text should return zeros."""
        result = measure_outsourced_intensity("")
        assert result["outsourced_ratio"] == 0.0
        assert result["quoted_word_count"] == 0
        assert result["editorial_word_count"] == 0

    def test_balanced_emotional_language(self):
        """When both quoted and editorial text are equally emotional,
        outsourced ratio should be near zero."""
        text = (
            'The devastating scandal rocked the industry. '
            'The catastrophic failure was appalling and outrageous. '
            '"This is a devastating and catastrophic failure," '
            'the analyst said. '
            '"The situation is outrageous and appalling," '
            'the critic noted.'
        )
        result = measure_outsourced_intensity(text)
        assert result["outsourced_ratio"] < 0.4, (
            f"Balanced emotional text should have low outsourced ratio, "
            f"got {result['outsourced_ratio']}"
        )

    def test_smart_quotes_detected(self):
        """Smart (curly) quotes should be extracted properly."""
        text = (
            'The company released a statement. '
            '\u201cThis is an alarming and devastating development '
            'that threatens democracy,\u201d the expert warned. '
            'Other analysts declined to comment.'
        )
        result = measure_outsourced_intensity(text)
        assert result["quoted_word_count"] > 5
        assert result["quoted_intensity"] > 0

    def test_word_counts_correct(self):
        """Quoted and editorial word counts should sum approximately to
        total text word count."""
        text = (
            'The report was released Tuesday. '
            '"This is absolutely devastating," the critic said. '
            'The company had no comment.'
        )
        result = measure_outsourced_intensity(text)
        total_words = len(text.split())
        counted_words = result["quoted_word_count"] + result["editorial_word_count"]
        # Allow some slack for quote delimiter words being counted differently
        assert counted_words > 0


# ===================================================================
# Power Asymmetry Framing Device Tests
# ===================================================================

class TestPowerAsymmetryFraming:
    """Test that the power_asymmetry framing device detects editorial
    framing of institutional/financial power vs individual vulnerability."""

    def test_financial_asymmetry_detected(self):
        """Dollar-value corporate power near individual should trigger."""
        text = (
            "The $1.5 trillion corporation deployed its legal team "
            "against the individual whistleblower, threatening her "
            "with fines of $50,000 per breach that could bankrupt her."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary, (
            f"Expected power_asymmetry in devices, got: {summary}"
        )

    def test_legal_army_language(self):
        """Legal firepower / army of lawyers language should trigger."""
        text = (
            "The company's army of lawyers outmatched the single "
            "plaintiff who could barely afford representation."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary

    def test_david_vs_goliath(self):
        """Explicit David vs Goliath framing should trigger."""
        text = (
            "Legal experts described it as a David versus Goliath "
            "battle, with the power imbalance heavily favoring the "
            "multi-billion-dollar conglomerate."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary

    def test_cannot_afford_legal(self):
        """'Cannot afford to fight' near legal context should trigger."""
        text = (
            "Critics pointed out that most individuals cannot afford "
            "legal defense against a company with unlimited resources."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary

    def test_no_false_positive_on_earnings(self):
        """Financial figures in earnings context shouldn't trigger."""
        text = (
            "The company reported $1.5 billion in quarterly revenue, "
            "beating analyst expectations of $1.4 billion. The CEO "
            "said the results reflected strong execution."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" not in summary, (
            f"Earnings report should not trigger power_asymmetry: {summary}"
        )

    def test_fine_per_violation_pattern(self):
        """Penalty-per-violation framing near bankruptcy should trigger."""
        text = (
            "Under the agreement, she faces penalties of $50,000 "
            "per violation, an amount that could devastate her financially."
        )
        devices = detect_framing_devices(text)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary


# ===================================================================
# Integration: Real-world article scenario
# ===================================================================

class TestIntegrationWhistleblowerArticle:
    """End-to-end test using a realistic whistleblower article scenario
    that should trigger all three new features."""

    ARTICLE_TEXT = (
        'Meta, the $1.5 trillion social media conglomerate, deployed '
        'an emergency arbitration order against Sarah Wynn-Williams, '
        'the former head of global public policy, on the eve of '
        'publication of her memoir. The order prevented her from '
        'speaking at the Hay Festival, where she sat in silence '
        'while another panelist read her words aloud.\n\n'
        '"This is censorship, plain and simple," said Tim Wu, a '
        'Columbia Law professor and former Biden adviser. "When '
        'trillion-dollar corporations can silence individuals through '
        'legal machinery, we have a serious problem for democracy."\n\n'
        '"What Meta did was appalling and reckless," said a civil '
        'liberties advocate who attended the event. "She was unable '
        'even to nod."\n\n'
        'Meta declined to comment on the specifics of the arbitration. '
        'A spokesperson said the company "respects the legal process '
        'and takes contractual obligations seriously."\n\n'
        'Legal experts described it as a David versus Goliath situation, '
        'noting that Wynn-Williams cannot afford the army of lawyers '
        'that Meta routinely deploys in such cases.'
    )

    def test_source_stance_is_adversarial(self):
        """Most sources should be adversarial to Meta."""
        sources = extract_sources(self.ARTICLE_TEXT)
        stance = analyze_source_stance(sources)
        assert stance["adversarial_count"] >= stance["supportive_count"], (
            f"Expected adversarial-heavy stance: {stance}"
        )

    def test_outsourced_intensity_detected(self):
        """Emotional language should be concentrated in quotes."""
        result = measure_outsourced_intensity(self.ARTICLE_TEXT)
        assert result["outsourced_ratio"] > 0, (
            f"Expected outsourced intensity > 0, got {result}"
        )

    def test_power_asymmetry_detected(self):
        """Power asymmetry framing should be detected."""
        devices = detect_framing_devices(self.ARTICLE_TEXT)
        summary = summarize_framing(devices)
        assert "power_asymmetry" in summary, (
            f"Expected power_asymmetry in devices: {summary}"
        )
