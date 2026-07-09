"""Tests for the Superintelligence Labs proper-noun suppression in topic
classification, and the Reuters Muse Image wire article analysis.

Discovery: the Reuters Muse Image rollout wire article (Jul 7, 2026)
scored ai_ethics_safety at 0.17 solely because "Meta Superintelligence
Labs" contains the keyword "superintelligence".  The org name is a
proper noun, not an AI safety concept reference.

Fix: topics.py now suppresses "superintelligence"/"superintelligent"
matches when they appear inside a "Superintelligence Labs" proper-noun
span, paralleling the education-topic analogy suppression.
"""

from mediascope.analyze.topics import classify_topic


def _topic_names(topics):
    return {t.topic for t in topics}


def _topic_keywords(topics, topic_name):
    for t in topics:
        if t.topic == topic_name:
            return set(t.matched_keywords)
    return set()


class TestSuperintelligenceOrgSuppression:
    """Tests for filtering 'superintelligence' in org-name contexts."""

    def test_meta_superintelligence_labs_not_ai_safety(self):
        """'Meta Superintelligence Labs' should NOT trigger ai_ethics_safety."""
        text = (
            "Meta Platforms said on Tuesday it is rolling out Muse Image, "
            "its first image-generation model from Meta Superintelligence Labs."
        )
        topics = classify_topic(text)
        assert "ai_ethics_safety" not in _topic_names(topics)

    def test_superintelligence_labs_alone_not_ai_safety(self):
        """'Superintelligence Labs' without 'Meta' prefix suppressed too."""
        text = (
            "The model was developed by Superintelligence Labs, "
            "the division Meta assembled last year."
        )
        topics = classify_topic(text)
        assert "ai_ethics_safety" not in _topic_names(topics)

    def test_conceptual_superintelligence_still_fires(self):
        """Standalone 'superintelligence' as concept should still trigger."""
        text = (
            "The debate over superintelligence and AI safety continues. "
            "Researchers warn that superintelligent systems pose risks. "
            "The alignment problem remains unsolved."
        )
        topics = classify_topic(text)
        assert "ai_ethics_safety" in _topic_names(topics)
        kw = _topic_keywords(topics, "ai_ethics_safety")
        assert "superintelligence" in kw

    def test_mixed_org_and_conceptual_preserves_conceptual(self):
        """When both org-name and conceptual uses exist, keep conceptual."""
        text = (
            "Meta Superintelligence Labs released new models. "
            "Meanwhile, researchers warn about superintelligence risk "
            "and the need for AI safety research."
        )
        topics = classify_topic(text)
        assert "ai_ethics_safety" in _topic_names(topics)
        kw = _topic_keywords(topics, "ai_ethics_safety")
        assert "superintelligence" in kw

    def test_reuters_muse_image_no_ai_safety_topic(self):
        """Full Reuters Muse Image wire article should not score ai_ethics_safety."""
        text = (
            "Meta expands generative AI tools with Muse Image rollout\n\n"
            "Meta Platforms said on Tuesday it is rolling out Muse Image, "
            "its first image-generation model from Meta Superintelligence Labs, "
            "as the Facebook owner expands generative AI tools across its apps.\n\n"
            "The company said Muse Image, which is integrated into its Meta AI "
            "chatbot, can interpret complex prompts, use photos as inputs and let "
            "users edit generated images directly through sketches or annotations.\n\n"
            "In April, the company launched Muse Spark, the first text-and-reasoning "
            "AI model from the Meta Superintelligence Labs team it assembled last "
            "year to catch up with rivals in the AI race.\n\n"
            "The company also announced an early preview of Muse Video, its video "
            "generation model."
        )
        topics = classify_topic(text)
        assert "ai_ethics_safety" not in _topic_names(topics)
        # Should still detect product_launch and ai_development
        names = _topic_names(topics)
        assert "product_launch" in names
        assert "ai_development" in names

    def test_superintelligent_adjective_in_org_name_suppressed(self):
        """'superintelligent' near 'Labs' should also be suppressed."""
        text = (
            "The superintelligence Labs team published a research paper "
            "on image generation methods."
        )
        topics = classify_topic(text)
        # Should not fire ai_ethics_safety just from org-name context
        assert "ai_ethics_safety" not in _topic_names(topics)
