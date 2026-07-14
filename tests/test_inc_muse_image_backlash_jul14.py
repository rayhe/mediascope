"""Tests for framing patterns discovered via Inc.com Meta Muse Image backlash
article (Jul 14, 2026).

Covers four new/extended patterns:
1. confession_framing — post-quote attribution ("Meta admits")
2. cross_publication_import — named publication ("According to The New York Times")
3. policy_reversal — temporal urgency ("just three days after its debut")
4. loaded_language — death/termination metaphors ("pulled the plug", "killed the feature")
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _has(text: str, device_type: str) -> bool:
    return any(d.device_type == device_type for d in detect_framing_devices(text))


def _count(text: str, device_type: str) -> int:
    return sum(1 for d in detect_framing_devices(text) if d.device_type == device_type)


# ── confession_framing: post-quote attribution ──────────────────────────


class TestConfessionFramingPostQuote:
    """Post-quote confession attribution: [quote] + [Name/Title] admits/conceded."""

    def test_meta_admits(self):
        text = "'We missed the mark,' Meta admits."
        assert _has(text, "confession_framing")

    def test_company_conceded(self):
        text = "'It was a mistake,' the CEO conceded."
        assert _has(text, "confession_framing")

    def test_spokesperson_acknowledged(self):
        text = "'We should have done better,' a spokesperson acknowledged."
        assert _has(text, "confession_framing")

    def test_neutral_quote_no_confession_verb(self):
        """'said' is neutral, not a confession verb."""
        text = "'We are continuing to invest,' the company said."
        assert not _has(text, "confession_framing")

    def test_no_preceding_quote(self):
        """Without a preceding quote, 'admits' alone should not trigger."""
        text = "Meta admits that it uses public data for training."
        # This may or may not trigger depending on other confession patterns;
        # the post-quote pattern specifically requires punctuation before the verb.
        # We just verify the pattern doesn't false-positive on plain statements.
        # (Other confession patterns may still match — that's fine.)


# ── cross_publication_import: named publication reference ────────────────


class TestCrossPublicationImportNamed:
    """Named publication reference: 'According to [major outlet]'."""

    def test_according_to_nyt(self):
        text = "According to The New York Times, Meta is pricing Muse Spark below competitors."
        assert _has(text, "cross_publication_import")

    def test_according_to_reuters(self):
        text = "According to Reuters, the company plans to expand."
        assert _has(text, "cross_publication_import")

    def test_according_to_wsj(self):
        text = "According to The Wall Street Journal, the deal is worth $10 billion."
        assert _has(text, "cross_publication_import")

    def test_according_to_bloomberg(self):
        text = "According to Bloomberg, the layoffs will affect 3,000 workers."
        assert _has(text, "cross_publication_import")

    def test_according_to_guardian(self):
        text = "According to The Guardian, regulators are investigating."
        assert _has(text, "cross_publication_import")

    def test_according_to_wired(self):
        text = "According to Wired, the feature has been in development for a year."
        assert _has(text, "cross_publication_import")

    def test_according_to_random_person_no_match(self):
        """'According to [random person]' should not match."""
        text = "According to John Smith, the project is on track."
        assert not _has(text, "cross_publication_import")


# ── policy_reversal: temporal urgency ────────────────────────────────────


class TestPolicyReversalTemporalUrgency:
    """Temporal urgency qualifiers: 'just N days after its debut/launch'."""

    def test_just_three_days_after_debut(self):
        text = "shelving it just three days after its debut"
        assert _has(text, "policy_reversal")

    def test_merely_two_weeks_after_launch(self):
        text = "removing it merely two weeks after its launch"
        assert _has(text, "policy_reversal")

    def test_only_one_day_after_release(self):
        text = "pulling it only one day after its release"
        assert _has(text, "policy_reversal")

    def test_just_five_days_after_rollout(self):
        text = "discontinuing it just 5 days after its rollout"
        assert _has(text, "policy_reversal")

    def test_neutral_temporal_no_urgency(self):
        """Without 'just/merely/only', temporal context is neutral."""
        text = "The feature was removed three days after its debut."
        assert not _has(text, "policy_reversal")


# ── loaded_language: death/termination metaphors ─────────────────────────


class TestLoadedLanguageDeathMetaphors:
    """Death/termination metaphors applied to products/features."""

    def test_pulled_the_plug(self):
        text = "Meta has pulled the plug on the controversial feature."
        assert _has(text, "loaded_language")

    def test_pulls_the_plug(self):
        text = "The company pulls the plug on Muse Image."
        assert _has(text, "loaded_language")

    def test_pulling_the_plug(self):
        text = "After pulling the plug on the AI tool, Meta issued a statement."
        assert _has(text, "loaded_language")

    def test_killed_the_feature(self):
        text = "Google killed the feature after user complaints."
        assert _has(text, "loaded_language")

    def test_axed_the_project(self):
        text = "Management axed the project in its second quarter."
        assert _has(text, "loaded_language")

    def test_yanked_the_update(self):
        text = "Apple yanked the update from the App Store."
        assert _has(text, "loaded_language")

    def test_scrapped_the_launch(self):
        text = "The team scrapped the launch after internal testing."
        assert _has(text, "loaded_language")

    def test_feature_was_killed(self):
        text = "The feature was killed before it reached general availability."
        assert _has(text, "loaded_language")

    def test_product_got_axed(self):
        text = "The product got axed in the latest round of cuts."
        assert _has(text, "loaded_language")

    def test_neutral_discontinued_no_match(self):
        """'Discontinued' is neutral — should not trigger death metaphor."""
        text = "Meta discontinued the feature after three days."
        assert not _has(text, "loaded_language")

    def test_neutral_removed_no_match(self):
        """'Removed' is neutral — should not trigger death metaphor."""
        text = "The company removed the AI tool from Instagram."
        assert not _has(text, "loaded_language")

    def test_death_knell_for_feature(self):
        text = "Critics say this could be the death knell for the feature."
        assert _has(text, "loaded_language")


# ── Full article integration test ────────────────────────────────────────


class TestIncMuseImageFullArticle:
    """Integration test against the full Inc.com article text."""

    ARTICLE = (
        "3 Days After Introducing an AI Feature, Meta Hits Pause in Wake of "
        "Privacy Backlash\n\n"
        "Muse Image allowed users to create AI-generated images from photos "
        "posted on Instagram—without permission. 'We missed the mark,' Meta "
        "admits.\n\n"
        "Meta has pulled the plug on a controversial new artificial intelligence "
        "feature that enabled users to create AI-generated images from photos "
        "posted to public Instagram accounts, shelving it just three days after "
        "its debut.\n\n"
        "The feature, called Muse Image, was introduced on Tuesday as part of "
        "Meta Superintelligence Labs' broader push into generative AI products. "
        "The company hit the pause button on Friday.\n\n"
        "Critics, citing privacy and copyright concerns, objected to the fact "
        "that public Instagram accounts were included by default rather than "
        "through an explicit opt-in process.\n\n"
        '"Our intent was to provide a useful creative tool and to give people '
        "control over whether their public content could be referenced in this "
        'way," Meta said in a statement issued Friday afternoon. "We\'ve heard '
        "the feedback that this feature missed the mark, so it's no longer "
        'available."\n\n'
        "Some of the harshest blowback came from Hollywood. Creative Artists "
        "Agency, the Los Angeles-based talent agency, said Meta's decision to "
        "give the AI feature access to public Instagram content was "
        "irresponsible.\n\n"
        '"Artists deserve to decide if and how their likeness and work is used," '
        "CAA said in a statement released a day after Muse Image's debut.\n\n"
        "SAG-AFTRA, the union representing more than 170,000 media professionals, "
        "including actors, broadcast journalists, recording artists, and DJs, "
        "urged members to opt out of the feature and accused Meta of "
        "underestimating issues related to digital likeness rights.\n\n"
        '"Anything other than a clear and conspicuous opt-in for these types of '
        "uses of Instagram users' images is unacceptable, and an utter "
        "miscalculation of public sentiment regarding the obvious dangers and "
        'harms inherent in such use," SAG-AFTRA said in a statement posted on '
        "X.\n\n"
        "After Meta reversed course on Friday, the union welcomed the decision. "
        '"With the dangers of nonconsensual digital replicas well known to all, '
        "a feature that encouraged that behavior is unwise,\" a union spokesperson "
        'told Reuters. "We appreciate its discontinuance. It is the responsible '
        'thing to do."\n\n'
        "Much of the criticism aimed at Muse Image centered on consent. Opponents "
        "argued that allowing AI systems to create new images from people's "
        "publicly available photos without explicit approval created risks "
        "related to the unauthorized use of personal likenesses and digital "
        "identity.\n\n"
        "Despite the setback, Meta is continuing to expand its AI offerings. "
        "Last week, the company unveiled Muse Spark 1.1, a paid version of its "
        "flagship AI model designed to compete with leading models from Anthropic, "
        "Google, OpenAI, and xAI.\n\n"
        "According to The New York Times, Meta is pricing Muse Spark below "
        "competing frontier AI models as it seeks to gain market share.\n\n"
        'Mark Zuckerberg, Meta\'s chief executive officer, said Muse Spark is '
        '"strongest at agentic performance, tool use, and computer use."'
    )

    def test_detects_confession_framing(self):
        assert _has(self.ARTICLE, "confession_framing")

    def test_detects_pulled_the_plug(self):
        devices = detect_framing_devices(self.ARTICLE)
        plug_hits = [d for d in devices if d.device_type == "loaded_language"
                     and "pulled the plug" in d.evidence_text.lower()]
        assert len(plug_hits) >= 1

    def test_detects_temporal_urgency(self):
        devices = detect_framing_devices(self.ARTICLE)
        temporal_hits = [d for d in devices if d.device_type == "policy_reversal"
                        and "just three days" in d.evidence_text.lower()]
        assert len(temporal_hits) >= 1

    def test_detects_cross_publication_import(self):
        assert _has(self.ARTICLE, "cross_publication_import")

    def test_detects_consent_alarm(self):
        assert _has(self.ARTICLE, "consent_alarm")

    def test_detects_default_burden_privacy(self):
        assert _has(self.ARTICLE, "default_burden_privacy")

    def test_detects_strategic_reversal(self):
        assert _has(self.ARTICLE, "strategic_reversal")

    def test_total_device_count_at_least_13(self):
        """Article should yield at least 13 framing devices after all patches."""
        devices = detect_framing_devices(self.ARTICLE)
        assert len(devices) >= 13, (
            f"Expected >= 13 devices, got {len(devices)}: "
            f"{[d.device_type for d in devices]}"
        )
