"""
Gizmodo: "Meta's Social Media Empire Is Under Siege. Its Plan for the Future
Is to Watch You Even More Closely"

Published: ~Jul 11, 2026
URL: https://gizmodo.com/metas-social-media-empire-is-under-siege-its-plan-for-the-future-is-to-watch-you-even-more-closely-2000784135
Author: Gizmodo staff (uncredited)

This article is a *roundup* that bundles 5+ distinct negative narratives about
Meta into a single "siege" frame:
  1. EU DSA charges (infinite scroll, autoplay)
  2. $1.4 trillion penalty demand (4 US states)
  3. Failed VR/metaverse diversification
  4. "Super-sensing" glasses (FT report)
  5. Emotion-tracking fitness patent (Patentlyze)

The article's structure creates an **escalation arc**: regulatory threats →
financial threats → failed diversification → surveillance tech → emotion
tracking → prediction of future legal trouble.  The ironic connection is
explicit ("Somewhat ironically") — Meta is under fire for addictive designs
yet building even more invasive surveillance tech.

Key framing analysis points:
- "Under siege" headline uses military metaphor
- "Somewhat ironically" makes the ironic consolidation explicit
- "And somehow, all of that is supposed to lead to better workouts" — sarcastic
  dismissal (Path K territory)
- "would not be shocking at all to see the company face another wave of similar
  legal scrutiny a decade from now" — predictive recidivism framing
- "mostly failing to diversify" — editorial judgment
- "creepy" — loaded language
- "existential threat" — catastrophizing
- "did not respond" — refusal amplification

Entity detection:
- Patentlyze → cluster #85 (Patent/IP Research)
- 404 Media → cluster Media/Publications
- EU/Commission/Virkkunen → cluster EU Regulatory
"""
import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities, get_entity_distribution
from mediascope.analyze.sentiment import analyze_composite

ARTICLE_TEXT = (
    "Meta social media empire is under siege. Its plan for the future is to "
    "watch you even more closely. "
    "Meta social media platforms are coming under growing legal fire over "
    "their allegedly addictive designs. Still, the company can not seem to "
    "stop thinking up new ways to monitor users more closely and embed "
    "itself even deeper into their lives. "
    "The European Commission this week told Meta to make major changes to "
    "Facebook and Instagram that would make them less addictive. Following "
    "a two-year investigation, the Commissions preliminary findings "
    "determined that the platforms designs violate the European Unions laws "
    "governing digital services. "
    "The investigation focused on features such as infinite scroll and "
    "autoplay, along with highly personalized recommendation algorithms "
    "that continually feed users new content. "
    "European regulators also said Metas efforts to address addiction "
    "risks, including time-management tools, parental controls, and Teen "
    "Accounts, are not effective. "
    "Regulators now want Meta to disable features such as autoplay and "
    "infinite scroll by default, introduce more effective screen-time "
    "breaks, and make its recommendation systems less focused on driving "
    "up engagement. "
    "Protecting the physical and mental health of Europeans must be a "
    "priority for social media platforms, said the Commissions Executive "
    "Vice-President for Tech Sovereignty, Security and Democracy, Henna "
    "Virkkunen, in a press release. "
    "Meta now has an opportunity to respond to the preliminary findings. "
    "But if the Commission ultimately confirms them, the company could "
    "face a fine of up to 6 percent of its annual worldwide revenue. "
    "For its part, Meta told Gizmodo that it disagrees with the "
    "Commissions findings. "
    "Since this investigation began, we rolled out Teen Accounts that "
    "automatically protect teens and put parents in control, allowing "
    "them to block access to Instagram at night and cap daily screen time "
    "at just 15 minutes, a Meta spokesperson said in an emailed statement. "
    "We share the European Commissions commitment to providing teens with "
    "safe, positive online experiences and will continue to engage "
    "constructively with them. "
    "Unfortunately for Meta, this is not the only existential threat to "
    "the core of its businesses. "
    "Across the pond, Meta said in a court filing this week that "
    "California, Colorado, Kentucky, and New Jersey are seeking 1.4 "
    "trillion dollars in potential penalties over allegations that the "
    "company designed Facebook and Instagram to addict young users and "
    "misled the public about their safety. That figure is just under "
    "Metas market capitalization of roughly 1.7 trillion dollars. "
    "This all comes as Meta has perfected the business of collecting data "
    "from its massive, highly attentive user base and using it to sell "
    "targeted ads. During the first three months of 2026, the company "
    "generated 56 billion dollars in revenue, 55 billion coming from "
    "advertising alone. "
    "Now, that very business model is under threat. "
    "In recent years, Meta has spent billions of dollars trying and "
    "mostly failing to diversify beyond social media. First with virtual "
    "reality and now with AI. "
    "Since acquiring Oculus in 2014, the company has scaled back its VR "
    "ambitions, even shutting down its Horizon Worlds metaverse. "
    "Currently, the company is trying its best to compete with frontier "
    "AI labs, but it now appears ready to start leasing space in its "
    "data centers to other AI companies. "
    "Somewhat ironically, new reports also suggest Meta is exploring AI "
    "devices that could collect a lot more data about users and "
    "potentially make them even more dependent on the companys tech. "
    "The Financial Times reported this week that Meta is testing "
    "prototype smart glasses designed to photograph a wearers "
    "surroundings every few seconds. The prototype, reportedly dubbed "
    "super-sensing glasses, could serve as an AI assistant that can "
    "answer questions like where a user left their keys. "
    "If you think that sounds creepy, a recently published Meta patent "
    "application takes things to another level. "
    "Patentlyze recently discovered an application Meta filed late last "
    "year for an AI fitness-coaching device that could continuously "
    "listen to a users voice and track their emotions over time. "
    "The system could detect cues such as laughter, sighs, and tone, "
    "and then connect them with a particular time, location, or "
    "activity. Over time, it could identify patterns such as when and "
    "where a user typically appears happy, sad, stressed, or relaxed. "
    "And somehow, all of that is supposed to lead to better workouts. "
    "Meta did not respond to Gizmodos request for comment on the patent. "
    "However, a Meta spokesperson told 404 Media, Like other companies, "
    "patents at Meta are often filed to disclose concepts that may or may "
    "not be implemented, and a granted patent does not guarantee that "
    "Meta has pursued or will pursue the technology described. "
    "But should Meta continue down this path, it would not be shocking "
    "at all to see the company face another wave of similar legal "
    "scrutiny a decade from now."
)


@pytest.fixture
def framing_devices():
    return detect_framing_devices(ARTICLE_TEXT)


@pytest.fixture
def device_types(framing_devices):
    return {d.device_type for d in framing_devices}


@pytest.fixture
def entities():
    return detect_entities(ARTICLE_TEXT)


@pytest.fixture
def entity_dist(entities):
    return get_entity_distribution(entities)


@pytest.fixture
def sentiment():
    return analyze_composite(ARTICLE_TEXT)


# ── Framing device detection ────────────────────────────────────────────

class TestFramingDetection:
    """Core framing device detection for the siege roundup article."""

    def test_loaded_language_siege(self, device_types):
        """'Under siege' headline military metaphor should trigger loaded_language."""
        assert "loaded_language" in device_types

    def test_catastrophizing_existential(self, device_types):
        """'Existential threat' should trigger catastrophizing."""
        assert "catastrophizing" in device_types

    def test_regulatory_shadow(self, device_types):
        """'Could face a fine' and 'potential penalties' → regulatory_shadow."""
        assert "regulatory_shadow" in device_types

    def test_loaded_language_creepy(self, framing_devices):
        """'Creepy' is explicit editorial loaded language."""
        creepy_hits = [
            d for d in framing_devices
            if d.device_type == "loaded_language"
            and "creepy" in d.evidence_text.lower()
        ]
        assert len(creepy_hits) >= 1

    def test_refusal_amplification(self, device_types):
        """'Did not respond' → refusal_amplification."""
        assert "refusal_amplification" in device_types

    def test_no_comment_implication(self, device_types):
        """'Did not respond to Gizmodos request' → no_comment_implication."""
        assert "no_comment_implication" in device_types

    def test_pathologizing_metaphor(self, device_types):
        """'Dependent on' in surveillance context → pathologizing_metaphor."""
        assert "pathologizing_metaphor" in device_types

    def test_sarcastic_correction_somehow(self, framing_devices):
        """'And somehow, all of that is supposed to lead to better workouts'
        is sarcastic dismissal — the writer uses 'somehow...supposed to'
        to undermine Meta's patent justification."""
        sarcasm_hits = [
            d for d in framing_devices
            if d.device_type == "sarcastic_correction"
            and "somehow" in d.evidence_text.lower()
        ]
        assert len(sarcasm_hits) >= 1, (
            "Missed sarcastic 'somehow...supposed to' dismissal"
        )

    def test_recidivism_framing_predictive(self, framing_devices):
        """'Face another wave of similar legal scrutiny a decade from now'
        is predictive recidivism — framing Meta as a future repeat offender."""
        recidivism_hits = [
            d for d in framing_devices
            if d.device_type == "recidivism_framing"
            and "another wave" in d.evidence_text.lower()
        ]
        assert len(recidivism_hits) >= 1, (
            "Missed predictive recidivism framing in closing paragraph"
        )

    def test_minimum_device_count(self, framing_devices):
        """Article has 5+ distinct negative narratives — should yield >=10 devices."""
        assert len(framing_devices) >= 10


# ── Entity detection ─────────────────────────────────────────────────────

class TestEntityDetection:
    """Entity extraction and cluster assignment."""

    def test_meta_is_primary_entity(self, entity_dist):
        """Meta should be the dominant entity by a large margin."""
        assert "Meta" in entity_dist
        assert entity_dist["Meta"] >= 15

    def test_patentlyze_detected(self, entities):
        """Patentlyze should be detected and assigned to Patent/IP Research cluster."""
        pat_hits = [
            e for e in entities
            if "patentlyze" in e.entity.lower()
        ]
        assert len(pat_hits) >= 1, "Patentlyze not detected"
        assert pat_hits[0].cluster == "Patent/IP Research"

    def test_404_media_detected(self, entities):
        """404 Media should be detected and assigned to Media/Publications cluster."""
        media_hits = [
            e for e in entities
            if "404 media" in e.entity.lower()
        ]
        assert len(media_hits) >= 1, "404 Media not detected"
        assert media_hits[0].cluster == "Media/Publications"

    def test_eu_regulatory_cluster(self, entity_dist):
        """European Commission / Henna Virkkunen → EU Regulatory cluster."""
        assert "EU Regulatory" in entity_dist
        assert entity_dist["EU Regulatory"] >= 2

    def test_financial_times_as_source(self, entities):
        """Financial Times should be detected as a media source entity."""
        ft_hits = [
            e for e in entities
            if "financial times" in e.entity.lower()
        ]
        assert len(ft_hits) >= 1

    def test_horizon_worlds_detected(self, entities):
        """Horizon Worlds should be detected (VR product shutdown reference)."""
        hw_hits = [
            e for e in entities
            if "horizon" in e.entity.lower()
        ]
        assert len(hw_hits) >= 1


# ── Sentiment analysis ───────────────────────────────────────────────────

class TestSentiment:
    """Composite sentiment scoring with correction paths."""

    def test_overall_tone_negative(self, sentiment):
        """Article is editorially negative — corrected tone should be < 0."""
        assert sentiment.overall_tone < 0.0, (
            f"Expected negative corrected tone, got {sentiment.overall_tone:.4f}"
        )

    def test_raw_tone_positive_inversion(self, sentiment):
        """VADER raw polarity is likely positive (polarity inversion on editorial
        content with mixed sentiment language).  This is the known #1 accuracy
        problem for editorial content."""
        # Raw tone can be positive or near-zero due to VADER inversion
        # The key assertion is that framing correction flips it negative
        assert sentiment.framing_corrected is True

    def test_emotional_language_intensity(self, sentiment):
        """'Siege', 'creepy', 'existential threat', 'shocking' → high ELI."""
        assert sentiment.emotional_language_intensity >= 0.4

    def test_speculative_language_high(self, sentiment):
        """'Could face', 'appears ready', 'could collect', 'could continuously'
        → high speculative language ratio."""
        assert sentiment.speculative_language_ratio >= 0.5

    def test_source_authority_framing(self, sentiment):
        """Regulatory sources (EU Commission, court filings) → high authority."""
        assert sentiment.source_authority_framing >= 0.5
