"""Tests for NYT article analysis improvements (Jun 22, 2026 iteration).

Tests the active-negative agency detection, workplace coercion/revolt
framing patterns, investment-near-layoffs juxtaposition, source stop-word
filtering, and framing-corrected headline alignment.
"""

import pytest
from mediascope.analyze.sentiment import (
    analyze_composite,
    _measure_agency,
    _measure_emotional_intensity,
)
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.sources import extract_sources


# --- Active-Negative Agency ---

class TestActiveNegativeAgency:
    """Test that active-negative verbs pull agency toward negative."""

    def test_tracking_employees(self):
        text = "Meta is tracking its employees' computer use and monitoring their mouse clicks."
        score = _measure_agency(text)
        assert score < 0, f"Expected negative agency, got {score}"

    def test_forcing_and_cutting(self):
        text = "The company is forcing employees to adopt AI tools and cutting jobs."
        score = _measure_agency(text)
        assert score < 0, f"Expected negative agency, got {score}"

    def test_active_positive_dominates(self):
        text = "The company launched an innovative platform and expanded globally."
        score = _measure_agency(text)
        assert score > 0, f"Expected positive agency, got {score}"

    def test_mixed_active(self):
        """When both positive and negative active verbs are present."""
        text = "Meta announced a new product and launched initiatives but is also tracking employees and laying off workers."
        score = _measure_agency(text)
        # Should be near zero or slightly negative due to equal count
        assert score <= 0.2, f"Expected near-zero or negative, got {score}"

    def test_harvesting_extracting(self):
        text = "The company is harvesting employee data and extracting their work patterns."
        score = _measure_agency(text)
        assert score < 0, f"Expected negative agency, got {score}"


# --- Workplace Framing Devices ---

class TestWorkplaceFramingDevices:
    """Test framing detection for workplace coercion and revolt patterns."""

    def test_no_opt_out(self):
        text = '"There is no option to opt-out on your corporate laptop," the CTO replied.'
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types, f"Expected loaded_language, got {types}"

    def test_revolt(self):
        text = "Many workers immediately revolted at the announcement."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types, f"Expected loaded_language for 'revolted', got {types}"

    def test_nihilistic(self):
        text = 'Employees have since shared nihilistic memes about the layoffs.'
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types, f"Expected loaded_language for 'nihilistic', got {types}"

    def test_countdown_to_layoffs(self):
        text = "Employees have created at least three websites counting down to the May 20 layoffs."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types, f"Expected loaded_language for countdown, got {types}"

    def test_training_replacements(self):
        text = "Workers fretted over whether they had been training their own replacements."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types, f"Expected loaded_language for 'training replacements', got {types}"


# --- Investment-Near-Layoffs Juxtaposition ---

class TestInvestmentLayoffsJuxtaposition:
    """Test juxtaposition detection for AI spending near job cuts."""

    def test_spending_billions_near_cuts(self):
        text = (
            "spending hundreds of billions of dollars on developing A.I. models "
            "and data centers. But the company is also cutting jobs to offset its "
            "A.I. spending, saying last month that it would slash 10 percent of "
            "its work force."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "juxtaposition" in types, f"Expected juxtaposition, got {types}"

    def test_layoffs_near_ai_spending(self):
        text = (
            "The company laid off 8,000 employees. The cuts will allow the "
            "company to offset the other investments we're making in AI infrastructure."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "juxtaposition" in types, f"Expected juxtaposition, got {types}"

    def test_no_false_positive_generic_spending(self):
        """Pure spending discussion without layoffs should not trigger."""
        text = "The company is spending billions on AI infrastructure and data centers."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "juxtaposition" not in types, f"Unexpected juxtaposition: {[d.evidence_text for d in devices if d.device_type == 'juxtaposition']}"


# --- Source Extraction Stop-Words ---

class TestSourceStopWords:
    """Test that common words are filtered from source name extraction."""

    def test_after_meta_not_extracted(self):
        text = "After Meta said late last month that it would start tracking employees."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "After Meta" not in names, f"'After Meta' falsely extracted as source: {names}"

    def test_since_google_not_extracted(self):
        text = "Since Google announced the changes, analysts have been concerned."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Since Google" not in names, f"'Since Google' falsely extracted: {names}"

    def test_real_name_still_extracted(self):
        text = 'Tracy Clayton said the program was designed to train AI products.'
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Tracy Clayton" in names, f"Real name 'Tracy Clayton' not extracted: {names}"


# --- Framing-Corrected Headline Alignment ---

class TestFramingCorrectedAlignment:
    """Test that headline alignment adjusts when framing correction fires."""

    def test_negative_headline_with_framing_corrected_body(self):
        """When both headline and body are truly negative but VADER reads
        the body as positive, framing correction should fix alignment."""
        # This article has "Miserable" in headline (VADER negative) and
        # adversarial framing in body (VADER positive but corrected negative)
        with open('examples/sample_output/nyt_meta_ai_employees_miserable_2026_05_08_article.txt') as f:
            full = f.read()
            text = full.split('---\n', 1)[1]

        result = analyze_composite(text, "Meta's Embrace of A.I. Is Making Its Employees Miserable")
        assert result.framing_corrected, "Expected framing correction to fire"
        assert result.headline_body_alignment > 0, (
            f"Expected positive alignment (both negative), got {result.headline_body_alignment}"
        )


# --- Full NYT Article Integration ---

class TestNYTArticleIntegration:
    """End-to-end test on the NYT Meta AI employee article."""

    @pytest.fixture
    def article_text(self):
        with open('examples/sample_output/nyt_meta_ai_employees_miserable_2026_05_08_article.txt') as f:
            full = f.read()
            return full.split('---\n', 1)[1]

    def test_overall_tone_negative(self, article_text):
        result = analyze_composite(article_text, "Meta's Embrace of A.I. Is Making Its Employees Miserable")
        assert result.overall_tone < 0, f"Expected negative tone, got {result.overall_tone}"

    def test_framing_correction_fired(self, article_text):
        result = analyze_composite(article_text, "Meta's Embrace of A.I. Is Making Its Employees Miserable")
        assert result.framing_corrected is True

    def test_agency_negative(self, article_text):
        score = _measure_agency(article_text)
        assert score < 0, f"Expected negative agency, got {score}"

    def test_framing_devices_at_least_5(self, article_text):
        devices = detect_framing_devices(article_text)
        assert len(devices) >= 5, f"Expected >=5 framing devices, got {len(devices)}"

    def test_emotional_intensity_high(self, article_text):
        intensity = _measure_emotional_intensity(article_text)
        assert intensity >= 0.4, f"Expected high emotional intensity, got {intensity}"

    def test_no_false_source_after_meta(self, article_text):
        sources = extract_sources(article_text)
        names = [s.name for s in sources]
        assert "After Meta" not in names, f"'After Meta' falsely extracted"


class TestSecurityContextEmotionalIntensity:
    """Test domain-aware emotional intensity scoring for cybersecurity articles."""

    def test_security_article_lower_intensity(self):
        """Security vocabulary in cybersecurity context should score lower."""
        text = (
            "The hackers exploited a vulnerability in the AI agent's account "
            "recovery flow. The attack vector was a simple prompt injection — "
            "attackers asked the agent to change the email address, and it "
            "complied. The exploit bypassed two-factor authentication. The "
            "vulnerability had been present since the agent was deployed. "
            "Cybersecurity experts warned that these attacks on AI agents "
            "would become more common as companies deploy more agents for "
            "account recovery and red-teaming becomes standard practice."
        )
        from mediascope.analyze.sentiment import _measure_emotional_intensity
        intensity = _measure_emotional_intensity(text)
        # Should be substantially lower than 1.0 because security terms
        # are downweighted in security-context articles
        assert intensity < 0.6, (
            f"Security article should have low emotional intensity, got {intensity}"
        )

    def test_non_security_article_normal_intensity(self):
        """Same security terms in a non-security context should score normally."""
        text = (
            "The critics blasted the proposal as a devastating attack on "
            "privacy. The scheme would exploit vulnerable communities and "
            "breach the public trust. 'This is outrageous and offensive,' "
            "said the spokesperson. The plan was described as reckless and "
            "unconscionable by advocacy groups."
        )
        from mediascope.analyze.sentiment import _measure_emotional_intensity
        intensity = _measure_emotional_intensity(text)
        # Without security context signals, should score higher
        assert intensity >= 0.3, (
            f"Non-security article with emotional language should score higher, got {intensity}"
        )


class TestAppositiveSourceExtraction:
    """Test extraction of sources with appositive clauses between name and verb."""

    def test_name_comma_appositive_comma_verb(self):
        """'Name, title at org, agrees.' should be detected."""
        from mediascope.analyze.sources import extract_sources
        text = (
            'Jessica Ji, a senior research analyst at Georgetown\'s Center '
            'for Security and Emerging Technology, agrees. "It raises '
            'questions like: Were there even guardrails in place?" she says.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Jessica Ji" in names, (
            f"Expected 'Jessica Ji' in sources, got {names}"
        )

    def test_name_comma_title_comma_says(self):
        """'Name, a professor of X at Y, says' should be detected."""
        from mediascope.analyze.sources import extract_sources
        text = (
            'Sarah Chen, a professor of computer science at Stanford '
            'University, says the findings are concerning.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Sarah Chen" in names, (
            f"Expected 'Sarah Chen' in sources, got {names}"
        )

    def test_no_false_positive_sentence_spanning(self):
        """Pattern should not match across sentence boundaries."""
        from mediascope.analyze.sources import extract_sources
        text = (
            'John Smith, who had never seen anything like it. '
            '"This is remarkable," said Dr. Alice Chen.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        # John Smith should NOT be matched (period between name and verb)
        assert "John Smith" not in names, (
            f"'John Smith' should not be extracted (sentence boundary), got {names}"
        )
