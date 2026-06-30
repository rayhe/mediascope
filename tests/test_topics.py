"""Tests for mediascope.analyze.topics — topic classification engine.

Covers:
    - Each of the 11 standardized topic buckets
    - Confidence scoring (keyword coverage + density)
    - Top-N filtering
    - Custom topic injection
    - Edge cases (empty text, no matches, tie-breaking)
    - Multi-topic articles
"""

import pytest
from mediascope.analyze.topics import (
    TOPIC_KEYWORDS,
    TopicScore,
    classify_topic,
)


# ── Individual topic detection ───────────────────────────────────────

class TestLayoffsTopicDetection:
    """Layoffs topic bucket detection."""

    def test_detects_layoff_keywords(self):
        text = (
            "Meta announced massive layoffs today, cutting 10,000 jobs "
            "in a restructuring effort. The headcount reduction affects "
            "Reality Labs and the Applied AI team. Severance packages "
            "include four months of pay."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "layoffs" in topic_names

    def test_reduction_in_force(self):
        text = "The company issued a reduction in force notice affecting 500 employees."
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "layoffs" in topic_names


class TestAIDevelopmentTopicDetection:
    """AI development topic bucket detection."""

    def test_detects_ai_keywords(self):
        text = (
            "Meta released a new large language model trained on 2 trillion tokens. "
            "The generative AI system powers the Meta AI assistant and AI agent features. "
            "The foundation model uses a transformer architecture with reinforcement learning."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names

    def test_detects_llm_keyword(self):
        text = "The LLM powering ChatGPT was fine-tuned for safety using RLHF."
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names


class TestPrivacyDataTopicDetection:
    """Privacy/data topic bucket detection."""

    def test_detects_privacy_keywords(self):
        text = (
            "Meta faces scrutiny over data collection practices and user data sharing. "
            "The data breach exposed 500 million records. GDPR regulators are investigating "
            "facial recognition and biometric data usage."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names


class TestAntitrustRegulationTopicDetection:
    """Antitrust/regulation topic bucket detection."""

    def test_detects_antitrust_keywords(self):
        text = (
            "The FTC filed an antitrust suit alleging Meta holds monopoly power "
            "in personal social networking. The DOJ is considering remedies including "
            "a potential breakup of Instagram and WhatsApp."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "antitrust_regulation" in topic_names


class TestChildSafetyTopicDetection:
    """Child safety topic bucket detection."""

    def test_detects_child_safety_keywords(self):
        text = (
            "Congress grilled Meta's CEO about children's safety online. "
            "COPPA enforcement is under review as underage users flood Instagram. "
            "Age verification technology remains inadequate for protecting minors."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "child_safety" in topic_names


class TestContentModerationTopicDetection:
    """Content moderation topic bucket detection."""

    def test_detects_moderation_keywords(self):
        text = (
            "Meta's content moderation policies failed to catch misinformation "
            "about the election. Hate speech removal rates dropped as trust and safety "
            "teams were cut. Deepfake detection remains a challenge."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "content_moderation" in topic_names


class TestFinancialResultsTopicDetection:
    """Financial results topic bucket detection."""

    def test_detects_financial_keywords(self):
        text = (
            "Meta reported quarterly earnings that beat expectations, with revenue "
            "of $56.3 billion and earnings per share of $6.29. The stock price "
            "rose 5% after the guidance was raised. Analysts revised market cap forecasts."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "financial_results" in topic_names


class TestProductLaunchTopicDetection:
    """Product launch topic bucket detection."""

    def test_detects_launch_keywords(self):
        text = (
            "Meta unveiled its new Ray-Ban smart glasses at the annual event, "
            "announcing general availability starting next month. The rollout "
            "includes a beta program for early access to AI features."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "product_launch" in topic_names


class TestExecutiveBehaviorTopicDetection:
    """Executive behavior topic bucket detection."""

    def test_detects_executive_keywords(self):
        text = (
            "The CEO faced scrutiny from the board of directors over executive "
            "compensation packages. The leadership change came after the former "
            "executive's resignation amid a corporate governance scandal."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "executive_behavior" in topic_names


class TestLitigationTopicDetection:
    """Litigation topic bucket detection."""

    def test_detects_litigation_keywords(self):
        text = (
            "A class action lawsuit was filed against Meta alleging privacy violations. "
            "The plaintiff seeks $5 billion in damages. The judge denied the injunction, "
            "and the case will proceed to trial in district court."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "litigation" in topic_names


class TestDefenseMilitaryTopicDetection:
    """Defense/military topic bucket detection."""

    def test_detects_military_keywords(self):
        text = (
            "Anduril won a $159 million Army contract for smart glasses that give "
            "soldiers enhanced battlefield awareness. The weapons system integrates "
            "drone feeds and tactical AI for combat operations. Pentagon officials "
            "praised the Special Operations prototype."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "defense_military" in topic_names

    def test_detects_defense_contractors(self):
        text = (
            "Anduril and Palantir are competing for defense contracts as the "
            "Department of Defense modernizes its military AI capabilities. "
            "The prototyping contract includes drone and autonomous weapons research."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "defense_military" in topic_names

    def test_beats_ai_development_on_military_article(self):
        """Military AR article should rank defense_military above ai_development."""
        text = (
            "Meta's smart glasses are being adapted for military use by defense "
            "contractor Anduril. The Army's IVAS program and Special Operations "
            "Command are evaluating tactical AI headsets for soldiers in combat. "
            "The defense technology prototyping contract was awarded by the Pentagon."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "defense_military" in topic_names
        dm_idx = topic_names.index("defense_military")
        if "ai_development" in topic_names:
            ai_idx = topic_names.index("ai_development")
            assert dm_idx < ai_idx, (
                "defense_military should rank above ai_development for military articles"
            )


class TestWorkplaceCultureTopicDetection:
    """Workplace culture topic bucket detection."""

    def test_detects_workplace_keywords(self):
        text = (
            "Employee morale at Meta has plummeted following the reassignment of "
            "thousands of workers to AI projects. Internal memos describe the work "
            "as drudgery. A union drive is gaining momentum amid burnout."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "workplace_culture" in topic_names


# ── Confidence scoring ───────────────────────────────────────────────

class TestConfidenceScoring:
    """Confidence score calculation."""

    def test_more_keywords_higher_confidence(self):
        # Few keywords
        sparse = "There was a layoff at the company."
        # Many keywords
        dense = (
            "The layoff affected 10,000 workers. Job cuts included headcount reduction "
            "across divisions. Restructuring and downsizing continued with severance packages."
        )
        sparse_topics = classify_topic(sparse)
        dense_topics = classify_topic(dense)

        sparse_layoff = next((t for t in sparse_topics if t.topic == "layoffs"), None)
        dense_layoff = next((t for t in dense_topics if t.topic == "layoffs"), None)

        assert sparse_layoff is not None
        assert dense_layoff is not None
        assert dense_layoff.confidence > sparse_layoff.confidence

    def test_confidence_between_0_and_1(self):
        text = (
            "The artificial intelligence model uses deep learning and machine learning "
            "for natural language processing. The LLM was trained on billions of tokens."
        )
        topics = classify_topic(text)
        for topic in topics:
            assert 0.0 <= topic.confidence <= 1.0

    def test_matched_keywords_populated(self):
        text = "The FTC filed an antitrust lawsuit against Meta for monopoly power."
        topics = classify_topic(text)
        antitrust = next((t for t in topics if t.topic == "antitrust_regulation"), None)
        assert antitrust is not None
        assert len(antitrust.matched_keywords) > 0
        # Should have matched "FTC", "antitrust", "monopoly"
        assert "antitrust" in antitrust.matched_keywords or "FTC" in antitrust.matched_keywords


# ── Top-N and sorting ────────────────────────────────────────────────

class TestTopNFiltering:
    """Top-N topic filtering."""

    def test_default_top_3(self):
        text = (
            "Meta's CEO announced layoffs amid an antitrust lawsuit. "
            "The privacy data breach led to FTC fines. "
            "AI development continues despite content moderation failures. "
            "Quarterly earnings beat expectations."
        )
        topics = classify_topic(text)
        assert len(topics) <= 3

    def test_custom_top_n(self):
        text = (
            "Meta's CEO announced layoffs amid an antitrust lawsuit. "
            "Privacy violations led to litigation. "
            "AI development continues despite content moderation failures."
        )
        topics = classify_topic(text, top_n=5)
        assert len(topics) <= 5

    def test_top_1(self):
        text = "The antitrust lawsuit from the FTC alleges monopoly power."
        topics = classify_topic(text, top_n=1)
        assert len(topics) == 1

    def test_sorted_by_confidence_descending(self):
        text = (
            "Meta's layoffs were announced alongside its quarterly earnings report. "
            "The restructuring cuts 10,000 jobs. Revenue was $56B. Stock rose."
        )
        topics = classify_topic(text, top_n=5)
        if len(topics) >= 2:
            for i in range(len(topics) - 1):
                assert topics[i].confidence >= topics[i + 1].confidence


# ── Custom topics ────────────────────────────────────────────────────

class TestCustomTopics:
    """Custom topic injection."""

    def test_custom_topic_detected(self):
        custom = {"smart_glasses": ["smart glasses", "Ray-Ban", "wearable", "heads-up display"]}
        text = "Meta's smart glasses with Ray-Ban branding include a heads-up display."
        topics = classify_topic(text, custom_topics=custom)
        topic_names = [t.topic for t in topics]
        assert "smart_glasses" in topic_names

    def test_custom_and_standard_coexist(self):
        custom = {"metaverse": ["metaverse", "virtual reality", "VR headset"]}
        text = (
            "Meta's metaverse division posted a $4B loss in quarterly earnings. "
            "Virtual reality headset sales remain slow. Revenue guidance was lowered."
        )
        topics = classify_topic(text, top_n=5, custom_topics=custom)
        topic_names = [t.topic for t in topics]
        assert "metaverse" in topic_names
        assert "financial_results" in topic_names


# ── Edge cases ───────────────────────────────────────────────────────

class TestEdgeCases:
    """Edge cases for topic classification."""

    def test_empty_text_returns_empty(self):
        assert classify_topic("") == []

    def test_no_topic_matches(self):
        text = "The weather today is sunny and warm with a light breeze from the west."
        topics = classify_topic(text)
        assert len(topics) == 0

    def test_short_text_still_works(self):
        text = "FTC antitrust lawsuit filed."
        topics = classify_topic(text)
        assert len(topics) >= 1

    def test_all_topic_keywords_exist(self):
        """Verify all standard topic buckets have keyword lists."""
        expected_topics = [
            "layoffs", "ai_development", "privacy_data",
            "antitrust_regulation", "child_safety", "content_moderation",
            "financial_results", "product_launch", "executive_behavior",
            "litigation", "workplace_culture", "government_oversight",
            "ai_generated_content",
        ]
        for topic in expected_topics:
            assert topic in TOPIC_KEYWORDS
            assert len(TOPIC_KEYWORDS[topic]) > 0


# ── Multi-topic articles ─────────────────────────────────────────────

class TestMultiTopicArticles:
    """Articles matching multiple topics."""

    def test_layoffs_and_financial(self):
        text = (
            "Meta announced 10,000 layoffs in its quarterly earnings report. "
            "The restructuring will save $3 billion annually. Revenue was $56B, "
            "beating analyst expectations. Headcount reduction targets Reality Labs."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "layoffs" in topic_names
        assert "financial_results" in topic_names

    def test_privacy_and_litigation(self):
        text = (
            "A class action lawsuit was filed over Meta's data collection practices. "
            "The privacy violation exposed user data from 500 million accounts. "
            "The plaintiff seeks damages for GDPR violations in district court."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names
        assert "litigation" in topic_names

    def test_child_safety_addiction_framing(self):
        """Child safety detected when article uses addiction framing."""
        text = (
            "State attorneys general accused Meta of designing Facebook "
            "and Instagram to addict children. The lawsuit alleges social "
            "media addiction has caused depression and self-harm in teens. "
            "Meta violated the Children's Online Privacy Protection Act "
            "for children under age 13."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "child_safety" in topic_names

    def test_child_safety_harm_framing(self):
        """Child safety detected with harm-to-children language."""
        text = (
            "Research shows social media platforms are harmful to children "
            "and adolescent mental health. Protecting children online requires "
            "stronger age verification and children's mental health resources."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "child_safety" in topic_names
