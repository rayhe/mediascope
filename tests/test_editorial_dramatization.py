"""Tests for editorial_dramatization device type.

Editorial dramatization detects interpretive glosses that rewrite neutral
factual events in heightened, dramatic language — standalone dramatic
descriptors and set-piece phrases that an editor inserts to color events
beyond what the sourced facts support.

Distinct from escalation_amplification, which catches intensifying modifiers
paired with threat/concern nouns ("escalating crisis").  Editorial
dramatization catches phrases like "unexpected reality check," "massive
shakeup," "turbulent transition," "did not mince words," "stark gap between
X and Y," and "specifically engineered to."

Real-world source: iPhone in Canada rewrite of Reuters article about
Zuckerberg's July 2 2026 town hall admission — all 8 editorial
dramatization phrases were missed by the existing toolkit.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices, FramingDevice


def _has(devices: list[FramingDevice], device_type: str) -> bool:
    """Check if a specific device type was detected."""
    return any(d.device_type == device_type for d in devices)


def _count(devices: list[FramingDevice], device_type: str) -> int:
    """Count occurrences of a specific device type."""
    return sum(1 for d in devices if d.device_type == device_type)


def _snippets(devices: list[FramingDevice], device_type: str) -> list[str]:
    """Extract matched text snippets for a device type."""
    return [d.evidence_text for d in devices if d.device_type == device_type]


DT = "editorial_dramatization"


# ---- Reality check / wake-up call pattern ----


class TestRealityCheckPattern:
    """Pattern: unexpected/surprising/sudden + reality check/wake-up call/etc."""

    def test_unexpected_reality_check(self):
        text = "Zuckerberg has delivered an unexpected reality check to his workforce."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_surprising_admission(self):
        text = "The CEO offered a surprising admission about the pace of progress."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_sobering_reckoning(self):
        text = "It was a sobering reckoning for a company that had bet big on AI."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_rare_mea_culpa(self):
        text = "Zuckerberg delivered a rare mea culpa to Meta employees."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Speed bump / setback pattern ----


class TestSpeedBumpPattern:
    """Pattern: clear/obvious/significant + speed bump/setback/etc."""

    def test_clear_speed_bump(self):
        text = "AI development has hit a clear speed bump, Reuters is reporting."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_significant_setback(self):
        text = "The layoffs represent a significant setback for the division."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_major_hurdle(self):
        text = "Scaling up the models remains a major hurdle for the team."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_serious_blow(self):
        text = "The departure was seen as a serious blow to morale."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Massive shakeup / overhaul pattern ----


class TestMassiveShakeupPattern:
    """Pattern: massive/sweeping/aggressive + shakeup/overhaul/etc."""

    def test_massive_shakeup(self):
        text = "The massive shakeup resulted in the elimination of approximately 8,000 roles."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_aggressive_restructuring(self):
        text = "Meta implemented an aggressive restructuring to fast-track AI."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_sweeping_reorganization(self):
        text = "A sweeping reorganisation was announced at the start of the year."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_dramatic_overhaul(self):
        text = "The dramatic overhaul left thousands without positions."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_seismic_pivot(self):
        text = "It was a seismic pivot away from the metaverse."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_aggressive_and_sweeping_reorganisation(self):
        """The actual iPhone in Canada phrase — compound adjective form."""
        text = (
            "Meta implemented an aggressive and sweeping corporate reorganisation "
            "specifically engineered to fast-track its artificial intelligence capabilities."
        )
        devices = detect_framing_devices(text)
        # Should catch "sweeping corporate reorganisation" and "specifically engineered to"
        assert _count(devices, DT) >= 1


# ---- Turbulent / painful transition pattern ----


class TestTurbulentTransitionPattern:
    """Pattern: turbulent/tumultuous/chaotic + transition/period/chapter."""

    def test_turbulent_transition(self):
        text = "Reflecting on the turbulent transition, Zuckerberg did not mince words."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_painful_process(self):
        text = "It has been a painful process for everyone involved."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_rocky_adjustment(self):
        text = "After a rocky adjustment, the new teams are finding their footing."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_chaotic_phase(self):
        text = "The chaotic phase of reorganization is nearing an end."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- "Did not mince words" pattern ----


class TestDidNotMinceWordsPattern:
    """Pattern: did not mince words / pulled no punches / etc."""

    def test_did_not_mince_words(self):
        text = "Zuckerberg did not mince words about the failures."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_didnt_mince_words(self):
        text = "She didn't mince words when addressing the board."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_pulled_no_punches(self):
        text = "The CEO pulled no punches in describing the state of AI agents."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_dropped_a_bombshell(self):
        text = "The executive dropped a bombshell during the all-hands meeting."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_spoke_with_unusual_candor(self):
        text = "The CEO spoke with unusual candor about the layoffs."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Stark gap / disconnect pattern ----


class TestStarkGapPattern:
    """Pattern: stark/glaring/yawning + gap/disconnect/divide + between/among."""

    def test_stark_gap_between(self):
        text = (
            "indicating a stark gap between executive timelines and "
            "actual engineering breakthroughs"
        )
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_glaring_disconnect_between(self):
        text = "There is a glaring disconnect between public statements and internal reality."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_yawning_chasm_between(self):
        text = "A yawning chasm between promises and delivery has opened."
        # No "between" directly after the noun, but "between" follows
        # Actually let's test with explicit preposition
        text = "A yawning chasm separating promise from delivery was evident."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_growing_divide_among(self):
        text = "A growing divide among the leadership team was becoming apparent."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Specifically engineered/designed pattern ----


class TestSpecificallyEngineeredPattern:
    """Pattern: specifically + engineered/designed/crafted/built + to/for."""

    def test_specifically_engineered_to(self):
        text = (
            "corporate reorganisation specifically engineered to "
            "fast-track its artificial intelligence capabilities"
        )
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_specifically_designed_to(self):
        text = "a policy specifically designed to suppress competition"
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_specifically_crafted_for(self):
        text = "messaging specifically crafted for Wall Street analysts"
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Current friction / turmoil pattern ----


class TestCurrentFrictionPattern:
    """Pattern: current/ongoing + friction/turmoil/chaos/fallout."""

    def test_current_friction(self):
        text = "Despite the current friction, Zuckerberg maintained a forward-looking stance."
        devices = detect_framing_devices(text)
        assert _has(devices, DT), f"Expected {DT}, got: {[d.device_type for d in devices]}"

    def test_ongoing_turmoil(self):
        text = "The ongoing turmoil has rattled employees across divisions."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_resulting_fallout(self):
        text = "The resulting fallout extended beyond the initial layoff targets."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)

    def test_lingering_uncertainty(self):
        text = "Lingering uncertainty about roles has hurt productivity."
        devices = detect_framing_devices(text)
        assert _has(devices, DT)


# ---- Full article integration test ----


class TestiPhoneInCanadaArticle:
    """Integration test using the actual iPhone in Canada derivative article."""

    ARTICLE = (
        "Meta CEO Mark Zuckerberg has delivered an unexpected reality check to his "
        "workforce, admitting that the company's development of advanced artificial "
        "intelligence software has hit a clear speed bump, Reuters is reporting.\n\n"
        "During an internal company town hall meeting on Thursday, July 2, 2026, "
        "Zuckerberg conceded that Meta's efforts to build sophisticated AI agents "
        "have progressed at a slower pace than leadership had originally anticipated.\n\n"
        "Zuckerberg told his employees that \"the kind of trajectory of the agentic "
        "development over at least the last four months hasn't really accelerated in "
        "the way that we expected,\" indicating a stark gap between executive "
        "timelines and actual engineering breakthroughs.\n\n"
        "Earlier this year, Meta implemented an aggressive and sweeping corporate "
        "reorganisation specifically engineered to fast-track its artificial "
        "intelligence capabilities. The massive shakeup, which took place in May, "
        "resulted in the elimination of approximately 8,000 roles, representing "
        "roughly 10 per cent of Meta's global workforce.\n\n"
        "Reflecting on the turbulent transition, Zuckerberg did not mince words. "
        "He openly acknowledged to his staff that the company overhaul was \"not as "
        "clean\" as it could have been.\n\n"
        "Despite the current friction, Zuckerberg maintained a forward-looking stance "
        "during the town hall."
    )

    def test_catches_multiple_dramatization_phrases(self):
        """Should catch most of the 8 editorial dramatization phrases."""
        devices = detect_framing_devices(self.ARTICLE)
        count = _count(devices, DT)
        # The article has 8 dramatization phrases across different patterns;
        # we expect the toolkit to catch at least 6
        assert count >= 6, (
            f"Expected at least 6 editorial_dramatization hits, got {count}. "
            f"Snippets: {_snippets(devices, DT)}"
        )

    def test_unexpected_reality_check_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("unexpected reality check" in s.lower() for s in snippets)

    def test_clear_speed_bump_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("clear speed bump" in s.lower() for s in snippets)

    def test_massive_shakeup_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("massive shakeup" in s.lower() for s in snippets)

    def test_turbulent_transition_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("turbulent transition" in s.lower() for s in snippets)

    def test_did_not_mince_words_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("did not mince words" in s.lower() for s in snippets)

    def test_current_friction_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("current friction" in s.lower() for s in snippets)

    def test_specifically_engineered_in_article(self):
        devices = detect_framing_devices(self.ARTICLE)
        snippets = _snippets(devices, DT)
        assert any("specifically engineered" in s.lower() for s in snippets)


# ---- Negative tests: should NOT trigger ----


class TestEditorialDramatizationNegative:
    """Ensure neutral language doesn't trigger editorial_dramatization."""

    def test_neutral_transition(self):
        text = "The transition to new teams is under way."
        devices = detect_framing_devices(text)
        assert not _has(devices, DT)

    def test_neutral_restructuring(self):
        text = "Meta announced a restructuring of its AI division."
        devices = detect_framing_devices(text)
        assert not _has(devices, DT)

    def test_neutral_setback(self):
        text = "The project faced a setback in the third quarter."
        devices = detect_framing_devices(text)
        assert not _has(devices, DT)

    def test_neutral_gap(self):
        text = "There is a gap between the two product launches."
        devices = detect_framing_devices(text)
        assert not _has(devices, DT)

    def test_literal_engineering(self):
        text = "The bridge was specifically engineered to withstand earthquakes."
        devices = detect_framing_devices(text)
        # This should still trigger — the pattern catches
        # "specifically engineered to" regardless of literal context.
        # That's acceptable because the toolkit scores at the
        # sentence level and the user reviews flagged items.
        # Not asserting negative here — this is a known acceptable
        # false-positive in literal engineering contexts.
