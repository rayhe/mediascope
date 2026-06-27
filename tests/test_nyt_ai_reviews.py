"""Tests for NYT AI reviews article improvements.

Validates:
1. New anonymous source patterns for government officials and person-involved constructions
2. Juxtaposition false positive fix — "government" + "public" in policy context should not fire
3. Full article framing device detection accuracy
"""

import re
import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import ANONYMOUS_SOURCE_PATTERNS


class TestGovernmentOfficialsAnonymousSource:
    """New pattern: 'N government/administration officials said'."""

    def test_two_government_officials_said(self):
        text = "two government officials said the plan was under review"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert any("government officials said" in m for m in matches), (
            "Should detect 'two government officials said' as anonymous source"
        )

    def test_three_administration_officials_confirmed(self):
        text = "three administration officials confirmed the policy shift"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'three administration officials confirmed'"
        )

    def test_several_senior_officials_told(self):
        text = "several senior officials told Reuters about the meeting"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'several senior officials told'"
        )

    def test_two_intelligence_officials_indicated(self):
        text = "two intelligence officials indicated the assessment was ongoing"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'two intelligence officials indicated'"
        )

    def test_four_federal_aides_said(self):
        text = "four federal aides said the decision was imminent"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'four federal aides said'"
        )


class TestPersonInvolvedAnonymousSource:
    """New pattern: 'one/a person involved in / close to X said'."""

    def test_one_person_involved_in_process(self):
        text = "one person involved in the process said the timeline was aggressive"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'one person involved in the process'"
        )

    def test_a_person_close_to_the_talks(self):
        text = "a person close to the talks said agreement was unlikely"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'a person close to the talks'"
        )

    def test_one_person_briefed_on_discussions(self):
        text = "one person briefed on the discussions said it was complicated"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'one person briefed on the discussions'"
        )

    def test_a_person_inside_the_negotiations(self):
        text = "a person inside the negotiations said progress was slow"
        matches = []
        for p in ANONYMOUS_SOURCE_PATTERNS:
            matches.extend(p.findall(text))
        assert len(matches) > 0, (
            "Should detect 'a person inside the negotiations'"
        )


class TestJuxtapositionFalsePositiveFix:
    """Verify 'government' + 'public' in policy context does not fire."""

    def test_government_public_policy_no_fire(self):
        """'Government up to 30 days... release to the public' is NOT military/consumer."""
        text = (
            "The order asked tech companies to give the U.S. government "
            "up to 30 days to evaluate A.I. models before their release "
            "to the public."
        )
        devices = detect_framing_devices(text)
        juxtapositions = [d for d in devices if d.device_type == "juxtaposition"]
        assert len(juxtapositions) == 0, (
            f"Policy language 'government...public' should NOT fire juxtaposition, "
            f"but got: {[d.evidence_text for d in juxtapositions]}"
        )

    def test_government_review_public_comment_no_fire(self):
        """Standard regulatory language should not trigger juxtaposition."""
        text = "The government opened a public comment period on the new AI rules."
        devices = detect_framing_devices(text)
        juxtapositions = [d for d in devices if d.device_type == "juxtaposition"]
        assert len(juxtapositions) == 0

    def test_military_consumer_still_fires(self):
        """Legitimate military/consumer juxtaposition should still fire."""
        text = (
            "The military-grade surveillance technology was being sold "
            "directly to consumer electronics companies."
        )
        devices = detect_framing_devices(text)
        juxtapositions = [d for d in devices if d.device_type == "juxtaposition"]
        assert len(juxtapositions) > 0, (
            "Legitimate military/consumer juxtaposition should still fire"
        )

    def test_pentagon_civilian_still_fires(self):
        """Pentagon + civilian context should still fire."""
        text = "The Pentagon program was repurposed for civilian applications."
        devices = detect_framing_devices(text)
        juxtapositions = [d for d in devices if d.device_type == "juxtaposition"]
        assert len(juxtapositions) > 0, (
            "Pentagon/civilian juxtaposition should still fire"
        )


class TestAnonymousAuthorityFramingPatterns:
    """Verify framing device anonymous_authority catches new patterns."""

    def test_government_officials_framing(self):
        text = "two government officials said the new approach was risky"
        devices = detect_framing_devices(text)
        anon = [d for d in devices if d.device_type == "anonymous_authority"]
        assert len(anon) > 0, (
            "Should detect 'two government officials said' as anonymous_authority framing"
        )

    def test_person_involved_framing(self):
        text = "one person involved in the process said it was chaotic"
        devices = detect_framing_devices(text)
        anon = [d for d in devices if d.device_type == "anonymous_authority"]
        assert len(anon) > 0, (
            "Should detect 'one person involved in the process' as anonymous_authority framing"
        )


class TestNYTAIReviewsArticleFullAnalysis:
    """Full article analysis for the NYT AI reviews article."""

    ARTICLE = """The Trump administration is pressing Meta to submit its artificial intelligence models for voluntary review, which would allow the government to evaluate the A.I.'s abilities and vulnerabilities, four people familiar with the confidential request said.

The request, which was made in emails with Meta, is the latest example of the administration's efforts to step up oversight of the A.I. industry after promoting a hands-off approach to the powerful technology. Less than two weeks ago, the government ordered Anthropic to remove access to its newest model, citing national security concerns.

Meta is the only major U.S. developer of A.I. technology that has not reached an agreement to voluntarily share its models with the federal government for review, said the people familiar with the request, who spoke on the condition of anonymity because they were not authorized to discuss the matter publicly. OpenAI, Anthropic, Google, xAI and Microsoft have all agreed to submit their models to the government's A.I. safety group, known as the Center for A.I. Standards and Innovation.

"We share the administration's goal of advancing U.S. leadership on robust and secure frontier A.I.," Francis Brennan, a Meta spokesman, said in a statement on Tuesday. "While we are working through the details, we hope to sign the agreement soon."

Ben Kass, a Commerce Department spokesman, said the Center for A.I. Standards and Innovation, which is housed in the department, regularly engaged with companies about voluntary agreements.

"This story is not unusual," he said. "It is the very work CAISI is supposed to be doing."

The latest batch of A.I. models have increased concerns about cybersecurity, though some industry insiders say the fears are overblown, since the new technology can be used to defend computer networks as easily as it can be used to attack them.

The companies have been submitting their A.I. models for review for several months as a good-will gesture, so intelligence and defense officials could ensure that the latest A.I. products did not pose a risk to national security, two government officials said.

On June 2, President Trump signed an executive order that gave the government responsibility for A.I. reviews. The order asked tech companies to give the U.S. government up to 30 days to evaluate A.I. models before their release to the public. It gave the government until the end of July to develop a process for the reviews.

But it is unclear who will lead the efforts and what type of standards the models would be held to, one person involved in the process said.

The Center for A.I. Standards and Innovation has stepped up its efforts to play a role in the model review process. Overseen by Commerce Secretary Howard Lutnick, the agency was created by the Biden administration to vet A.I. models and has a technical staff to lead those evaluations.

Meta released its latest A.I. model, Muse Spark, in April, and it nearly matched the performance of models from rivals like Google, OpenAI and Anthropic.

Meta's policy team has been negotiating with the Commerce Department about how to proceed, the people familiar with the confidential request said. It's unclear whether they will be able to reach an agreement.

Even companies that have given the administration previews of their A.I. models have run into problems. Anthropic, which gave its newest and most powerful model, Fable 5, to the administration for review, was surprised last week when the White House gave the company less than 90 minutes to close access to its new A.I. because of national security concerns.

The problem, two people with knowledge of discussions said, stemmed from a paper written by researchers at Amazon that showed a vulnerability in the model that could be exploited for cyberattacks.

In the days since, talks between Anthropic and the administration have been productive, two people with knowledge of the talks said. Mr. Trump made comments over the weekend to Axios that he no longer saw Anthropic as a security concern.

It was unclear who would sign off on Anthropic's restoring access to its model and whether other companies would be held to the same standard, the two people said.

Ana Swanson contributed reporting from Washington."""

    def test_isolation_framing_detected(self):
        devices = detect_framing_devices(self.ARTICLE)
        isolation = [d for d in devices if d.device_type == "isolation_framing"]
        assert len(isolation) >= 1, "Should detect Meta isolation framing"
        assert "only major" in isolation[0].evidence_text.lower()

    def test_pressure_language_detected(self):
        devices = detect_framing_devices(self.ARTICLE)
        pressure = [d for d in devices if d.device_type == "pressure_language"]
        assert len(pressure) >= 2, (
            f"Should detect 'pressing' and 'confidential request', got {len(pressure)}"
        )

    def test_anonymous_authority_count(self):
        devices = detect_framing_devices(self.ARTICLE)
        anon = [d for d in devices if d.device_type == "anonymous_authority"]
        assert len(anon) >= 5, (
            f"Should detect 5+ anonymous authority instances (3 original + 2 new patterns), "
            f"got {len(anon)}: {[d.evidence_text[:40] for d in anon]}"
        )

    def test_no_false_juxtaposition(self):
        """No juxtaposition false positives in policy reporting."""
        devices = detect_framing_devices(self.ARTICLE)
        juxtapositions = [d for d in devices if d.device_type == "juxtaposition"]
        assert len(juxtapositions) == 0, (
            f"No juxtaposition expected in policy article, got: "
            f"{[d.evidence_text[:60] for d in juxtapositions]}"
        )

    def test_total_device_types(self):
        """Article should have exactly 4 device types: anonymous_authority,
        isolation_framing, pressure_language, sovereignty_framing.
        sovereignty_framing fires because the article frames the AI review
        request through national security language near Meta."""
        devices = detect_framing_devices(self.ARTICLE)
        types = set(d.device_type for d in devices)
        assert types == {"anonymous_authority", "isolation_framing", "pressure_language", "sovereignty_framing"}, (
            f"Expected exactly 4 device types, got: {types}"
        )


class TestFramingDeviceRegistry:
    """Validate total framing device count stays in sync with documentation.

    METHODOLOGY.md documents 27 framing device types:
      - 10 core (pattern-matched)
      - 14 extended (pattern-matched, added from real-article analysis)
      - 3 structural (post-pass heuristics: kicker, analogy stacking, speculative)

    The 27 pattern-based types are registered in _DEVICE_PATTERNS.
    The 3 structural types are detected in the post-pass of detect_framing_devices().
    Update this test when adding new device types.
    """

    def test_pattern_based_device_count(self):
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        assert len(_DEVICE_PATTERNS) == 30, (
            f"Expected 30 pattern-based device types, got {len(_DEVICE_PATTERNS)}. "
            f"If you added a new type, update METHODOLOGY.md §4.1 and this test. "
            f"Current types: {sorted(_DEVICE_PATTERNS.keys())}"
        )

    def test_all_expected_types_registered(self):
        """Every documented device type must be present in the registry."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        expected_pattern_types = {
            # Core (10)
            "guilt_by_association", "anonymous_authority", "catastrophizing",
            "false_balance", "selective_omission_signal", "emotional_appeal",
            "loaded_language", "power_asymmetry", "ceo_personalization",
            "litigation_framing",
            # Extended (13)
            "straw_man", "refusal_amplification", "juxtaposition",
            "timeline_implication", "military_techno_optimism",
            "selective_rehabilitation", "rhetorical_question",
            "ironic_quotation", "isolation_framing", "pressure_language",
            "self_referential_investigation", "geopolitical_regulatory_pressure",
            "sovereignty_framing",
            # Scale/magnitude (1)
            "scale_magnitude",
            # Corporate reassurance (1)
            "corporate_reassurance_undercut",
            # Hypocrisy (1)
            "hypocrisy_frame",
            # Sarcastic correction (1)
            "sarcastic_correction",
            # Outsourced intensity (1)
            "outsourced_intensity",
            # Precedent analogy (1)
            "precedent_analogy",
            # Confession framing (1)
            "confession_framing",
        }
        actual = set(_DEVICE_PATTERNS.keys())
        missing = expected_pattern_types - actual
        extra = actual - expected_pattern_types
        assert not missing, f"Missing documented types from registry: {missing}"
        assert not extra, f"Undocumented types in registry: {extra}"

    def test_structural_types_in_detect_function(self):
        """The 3 structural/post-pass types must be produced by detect_framing_devices."""
        import inspect
        from mediascope.analyze.framing import detect_framing_devices
        src = inspect.getsource(detect_framing_devices)
        for structural_type in ["kicker_framing", "analogy_stacking", "speculative_framing"]:
            assert structural_type in src, (
                f"Structural device type '{structural_type}' not found in "
                f"detect_framing_devices() source. Update METHODOLOGY.md if removed."
            )
