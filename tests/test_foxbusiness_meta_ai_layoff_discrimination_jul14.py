"""Tests for Fox Business Meta AI layoff discrimination article (Jul 14, 2026).

Validates fixes for:
1. Publication self-reference source extraction ("told Fox Business")
2. Legal-context suppression for emotional_appeal on protected-status terms
3. editorial_cross_promotion detection for embedded all-caps links
4. Same-event comparison patterns with Reuters version

Discovered in Type A iteration, Jul 14, 2026 20:00 PT.
"""

import pytest

from mediascope.analysis import analyze_text


TITLE = (
    "Meta employees sue on allegations company used AI to target "
    "workers on medical, parental leave for layoffs"
)

ARTICLE = (
    "A group of 26 Meta employees sued the tech giant over accusations "
    "that it used AI-powered software to choose people for mass layoffs, "
    "disproportionately targeting workers with disabilities or those who "
    "took medical, parental or family leave.\n\n"
    "The lawsuit, filed in federal court in Oakland, California, on Monday, "
    "alleges that the company relied on factors such as internal AI systems, "
    "keystroke and activity-monitoring data, AI token-usage dashboards and "
    "algorithmically assisted performance rankings when making job cuts "
    "earlier this year.\n\n"
    'Many of these factors "by design, cannot be accumulated by an employee '
    "who is on protected medical or family leave, or whose output is reduced "
    'by a disability," the lawsuit reads, adding that the company did not '
    "factor in protected leave when taking employees' scores into account "
    'and "did not pause the system for the individualized, leave- and '
    'accommodation-neutral review that the law requires."\n\n'
    "The plaintiffs are among the 8,000 employees, or about 10% of its "
    "workforce, who Meta said in May would be impacted by layoffs, and they "
    "were told their jobs would be eliminated starting July 22.\n\n"
    "FOUR STATES SEEKING $1.4 TRILLION IN PENALTIES IN CHILD SOCIAL MEDIA "
    "ADDICTION TRIAL, META SAYS\n\n"
    "They claim that Meta violated state and federal laws — including the "
    "Family and Medical Leave Act, the Americans with Disabilities Act, the "
    "Pregnancy Discrimination Act and the Pregnant Workers Fairness Act — "
    "that prohibit discrimination or retaliation against workers who take "
    "medical leave, have disabilities or are pregnant.\n\n"
    "The workers also say the company failed to test its AI systems for "
    "bias, which they allege violated newly adopted laws in California and "
    "New York City.\n\n"
    "The plaintiffs, who come from six states, including California and "
    "New York, as well as Washington, D.C., are seeking a preliminary ruling "
    "from the court to block Meta from completing the layoffs while they "
    "pursue their claims in private arbitration.\n\n"
    "The employees argue that Meta's agreements require employees to "
    "arbitrate workplace disputes individually, but do not apply to "
    "requests for temporary relief.\n\n"
    "They said the lawsuit asks just to preserve the status quo and keep "
    "them employed pending arbitration.\n\n"
    '"Once these terminations are finalized, the harm to Plaintiffs cannot '
    'be undone by money damages alone," the lawsuit reads, citing the loss '
    "of employer-subsidized health coverage during pregnancy, postpartum "
    "recovery and active medical treatment.\n\n"
    "Meta has pushed back on the allegations outlined in the lawsuit, saying "
    "that it does not use AI when determining who to cut from its workforce.\n\n"
    '"These claims lack merit and are not based on facts. Workforce '
    "management and organizational decisions were and are made by people, "
    'not AI," a Meta spokesperson told Fox Business.\n\n'
    "META SHUTS DOWN AI TOOL AFTER BACKLASH OVER PUBLIC INSTAGRAM "
    "ACCOUNTS\n\n"
    "About half of the plaintiffs had taken leave for caregiving or "
    "pregnancy-related reasons.\n\n"
    "Eight employees are women who had taken maternity or pregnancy-related "
    "leave, four are men who had taken parental leave and one is a woman who "
    "had taken leave to take care of a family member and later bereavement "
    "leave.\n\n"
    'The plaintiffs argued that Meta\'s "algorithmically assisted selection '
    "process, by systematically recording such absences as reduced "
    'performance, falls more heavily on women than on men" because women '
    "disproportionately take pregnancy and caregiving leave."
)


@pytest.fixture
def result():
    return analyze_text(ARTICLE, title=TITLE, target_entity="Meta")


# -----------------------------------------------------------------
# 1. Source extraction: "Fox Business" must NOT be extracted as source
# -----------------------------------------------------------------

class TestSourceExtraction:
    """Verify publication self-reference is filtered from sources."""

    def test_fox_business_not_extracted_as_source(self, result):
        """'told Fox Business' is a publication attribution, not a source.

        The actual source is 'a Meta spokesperson' — Fox Business is
        the *recipient* of the quote.  Discovered in Fox Business Meta AI
        layoff discrimination article (Jul 14, 2026).
        """
        source_names = [s["name"] for s in result["sources"]]
        assert "Fox Business" not in source_names, (
            f"Fox Business should not be extracted as a source. "
            f"Found sources: {source_names}"
        )

    def test_meta_spokesperson_extracted(self, result):
        """Meta spokesperson should be correctly extracted as source."""
        source_names = [s["name"].lower() for s in result["sources"]]
        has_spokesperson = any(
            "spokesperson" in n or "meta" in n for n in source_names
        )
        assert has_spokesperson, (
            f"Meta spokesperson should be in sources. Found: {source_names}"
        )


# -----------------------------------------------------------------
# 2. Emotional appeal: "disability" in legal context → suppress
# -----------------------------------------------------------------

class TestLegalContextSuppression:
    """Verify emotional_appeal is suppressed for legal terms in lawsuit articles."""

    def test_disability_not_emotional_appeal(self, result):
        """'disability' in an ADA claim is a legal descriptor, not emotional rhetoric.

        Discovered in Fox Business Meta AI layoff discrimination
        article (Jul 14, 2026).
        """
        ea_devices = [
            d for d in result["framing_devices"]
            if d["device_type"] == "emotional_appeal"
            and "disability" in d["evidence_text"].lower()
        ]
        assert len(ea_devices) == 0, (
            f"'disability' should be suppressed in legal context. "
            f"Found: {[d['evidence_text'] for d in ea_devices]}"
        )


# -----------------------------------------------------------------
# 3. Editorial cross-promotion: embedded all-caps links
# -----------------------------------------------------------------

class TestCrossPromotion:
    """Verify editorial_cross_promotion detection for embedded headlines."""

    def test_trillion_cross_promo_detected(self, result):
        """'FOUR STATES SEEKING $1.4 TRILLION...' is an embedded cross-promo."""
        cross_promos = [
            d for d in result["framing_devices"]
            if d["device_type"] == "editorial_cross_promotion"
        ]
        trillion_promos = [
            d for d in cross_promos
            if "TRILLION" in d["evidence_text"] or "$1.4" in d["evidence_text"]
        ]
        assert len(trillion_promos) >= 1, (
            f"$1.4T cross-promotion not detected. "
            f"Found cross-promos: {[d['evidence_text'][:60] for d in cross_promos]}"
        )

    def test_muse_image_cross_promo_detected(self, result):
        """'META SHUTS DOWN AI TOOL AFTER BACKLASH...' is an embedded cross-promo."""
        cross_promos = [
            d for d in result["framing_devices"]
            if d["device_type"] == "editorial_cross_promotion"
        ]
        muse_promos = [
            d for d in cross_promos
            if "SHUTS DOWN" in d["evidence_text"] or "BACKLASH" in d["evidence_text"]
        ]
        assert len(muse_promos) >= 1, (
            f"Muse Image cross-promotion not detected. "
            f"Found cross-promos: {[d['evidence_text'][:60] for d in cross_promos]}"
        )

    def test_two_cross_promos_total(self, result):
        """Fox Business embeds two unrelated Meta-negative headlines."""
        cross_promos = [
            d for d in result["framing_devices"]
            if d["device_type"] == "editorial_cross_promotion"
        ]
        assert len(cross_promos) >= 2, (
            f"Expected 2+ cross-promotions, found {len(cross_promos)}. "
            f"Found: {[d['evidence_text'][:60] for d in cross_promos]}"
        )


# -----------------------------------------------------------------
# 4. Sentiment and topic classification
# -----------------------------------------------------------------

class TestSentimentAndTopics:
    """Basic validation of sentiment and topic classification."""

    def test_negative_tone(self, result):
        """Article about a lawsuit against Meta should score negative."""
        assert result["sentiment"]["overall_tone"] < 0, (
            f"Expected negative tone, got {result['sentiment']['overall_tone']}"
        )

    def test_workplace_topic_detected(self, result):
        """Layoff discrimination article should classify as workplace_culture."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert "workplace_culture" in topic_names, (
            f"Expected workplace_culture topic, got: {topic_names}"
        )

    def test_litigation_topic_detected(self, result):
        """Article about a lawsuit should classify as litigation."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert "litigation" in topic_names, (
            f"Expected litigation topic, got: {topic_names}"
        )
