"""Regression tests for chilling_effect framing device.

Detects self-censorship and avoidance behavior by product users/owners
due to social stigma, fear of confrontation, or reputational risk.  The
rhetorical power comes from showing that even the product's own advocates
modify their behavior to avoid negative social consequences.

Discovered via PetaPixel "Meta Smart Glasses Owners Too Scared to Wear
Them in Public" (Jul 14, 2026) and Engadget wearables user interview
coverage (Jul 2026).

Added: Type D iteration, Jul 31 2026.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _types(text: str) -> list[str]:
    return [d.device_type for d in detect_framing_devices(text)]


# ---------------------------------------------------------------------------
# Core self-censorship patterns
# ---------------------------------------------------------------------------

class TestSelfCensorship:
    """Users afraid or reluctant to wear/use the product in public."""

    def test_too_scared_to_wear(self):
        text = "Meta Smart Glasses Owners Too Scared to Wear Them in Public"
        assert "chilling_effect" in _types(text)

    def test_too_afraid_to_use(self):
        text = "Some users are too afraid to use them around strangers."
        assert "chilling_effect" in _types(text)

    def test_too_uncomfortable_to_wear(self):
        text = "I felt too uncomfortable to wear them at the coffee shop."
        assert "chilling_effect" in _types(text)

    def test_too_embarrassed_to_bring(self):
        text = "She was too embarrassed to bring them to the office."
        assert "chilling_effect" in _types(text)

    def test_too_self_conscious(self):
        text = "I'm too self-conscious to wear them in public."
        assert "chilling_effect" in _types(text)

    def test_too_nervous_to_put_on(self):
        text = "He was too nervous to put on the glasses at the restaurant."
        assert "chilling_effect" in _types(text)


class TestAvoidanceBehavior:
    """Users actively hiding or putting away their device."""

    def test_more_mindful_crowded(self):
        text = (
            "I've been a little bit more mindful of them, especially "
            "in more crowded environments."
        )
        assert "chilling_effect" in _types(text)

    def test_more_careful_in_public(self):
        text = "I'm more careful about wearing them in public now."
        assert "chilling_effect" in _types(text)

    def test_more_selective_outside(self):
        text = "Users are becoming more selective about wearing them outside."
        assert "chilling_effect" in _types(text)


class TestReconsidering:
    """Users having second thoughts about purchase or wearing."""

    def test_not_a_good_idea(self):
        text = "maybe it's not a good idea to have those"
        assert "chilling_effect" in _types(text)

    def test_second_thoughts_buying(self):
        text = "I'm having second thoughts about buying a pair."
        assert "chilling_effect" in _types(text)

    def test_reconsidering_wearing(self):
        text = "Many users are reconsidering wearing them daily."
        assert "chilling_effect" in _types(text)

    def test_thought_twice_purchase(self):
        text = "After seeing the comments, I thought twice about the purchase."
        assert "chilling_effect" in _types(text)


class TestSocialLabeling:
    """Social labeling causing avoidance — users called predators/creeps."""

    def test_basically_a_predator(self):
        text = "if you wear those glasses you're basically a predator"
        assert "chilling_effect" in _types(text)

    def test_people_assume_creep(self):
        text = "other people just assume that automatically you're a creep"
        assert "chilling_effect" in _types(text)

    def test_wearers_look_like_stalkers(self):
        text = "wearers look like stalkers to most people on the street"
        assert "chilling_effect" in _types(text)

    def test_people_think_spy(self):
        text = "they're just spies wearing fancy sunglasses"
        assert "chilling_effect" in _types(text)


class TestInappropriateness:
    """Users acknowledging contexts where wearing is inappropriate."""

    def test_not_appropriate_to_wear(self):
        text = (
            "There are a lot of times where it's not appropriate to wear "
            "cameras on your face."
        )
        assert "chilling_effect" in _types(text)

    def test_not_the_right_place_to_use(self):
        text = "It's not the right place to use smart glasses."
        assert "chilling_effect" in _types(text)


class TestRefusalToWear:
    """Users explicitly refusing to wear the device in social contexts."""

    def test_wont_wear_in_public(self):
        text = "I won't wear them in public anymore."
        assert "chilling_effect" in _types(text)

    def test_stopped_wearing_around_people(self):
        text = "I stopped wearing them around people."
        assert "chilling_effect" in _types(text)

    def test_decided_against_wearing_outside(self):
        text = "She decided against wearing them outside."
        assert "chilling_effect" in _types(text)


# ---------------------------------------------------------------------------
# False-positive guards
# ---------------------------------------------------------------------------

class TestFalsePositiveGuards:
    """Ensure chilling_effect doesn't fire on unrelated text."""

    def test_no_fire_on_plain_wearing(self):
        """Simple wearing statement should not trigger."""
        text = "I wear my Meta glasses every day and love them."
        assert "chilling_effect" not in _types(text)

    def test_no_fire_on_weather_scared(self):
        """'Scared' in non-product context should not trigger."""
        text = "I was too scared to go outside in the thunderstorm."
        assert "chilling_effect" not in _types(text)

    def test_no_fire_on_privacy_discussion(self):
        """Generic privacy discussion without self-censorship framing."""
        text = "Privacy concerns about smart glasses continue to grow."
        assert "chilling_effect" not in _types(text)

    def test_no_fire_on_product_review(self):
        """Positive product mention should not trigger."""
        text = "The Meta Ray-Ban glasses are comfortable to wear all day."
        assert "chilling_effect" not in _types(text)


# ---------------------------------------------------------------------------
# Full-text integration: PetaPixel article excerpt
# ---------------------------------------------------------------------------

class TestPetaPixelArticleExcerpt:
    """End-to-end test on the PetaPixel smart glasses self-censorship article."""

    ARTICLE_EXCERPT = (
        'Dubbed online as "pervert glasses," Meta\'s partnership with '
        "Ray-Bans has been a successful one for Mark Zuckerberg's company — "
        "selling more than seven million pairs last year. But some users, "
        "mainly men, engaging in predatory behavior, like recording people "
        "without consent and posting the footage online, have prompted a "
        "backlash against the smart spectacles.\n\n"
        '"I\'ve been a little bit more mindful of them, especially in more '
        'crowded environments," says creator Martino Wong. "There have been '
        "times in which I basically fold them up and hang them on my shirt, "
        "so as to show more clearly that I'm not actively using them.\"\n\n"
        '"I saw all these comments about if you wear those glasses you\'re '
        "basically a predator or a creep, and I was like, 'oh, maybe it's "
        "not a good idea to have those,'\" freelance video producer Will "
        "Kujaa says.\n\n"
        '"There are a lot of times where it\'s not appropriate to wear '
        'cameras on your face."'
    )

    @classmethod
    @pytest.fixture(scope="class")
    def devices(cls):
        return detect_framing_devices(cls.ARTICLE_EXCERPT)

    @classmethod
    @pytest.fixture(scope="class")
    def device_types(cls, devices):
        return [d.device_type for d in devices]

    def test_chilling_effect_detected(self, device_types):
        assert "chilling_effect" in device_types

    def test_multiple_chilling_instances(self, devices):
        """Article contains multiple chilling_effect instances."""
        ce = [d for d in devices if d.device_type == "chilling_effect"]
        assert len(ce) >= 3, (
            f"Expected >= 3 chilling_effect instances, got {len(ce)}: "
            f"{[d.evidence_text[:60] for d in ce]}"
        )

    def test_surveillance_creep_also_detected(self, device_types):
        """Recording without consent should also fire surveillance_creep."""
        assert "surveillance_creep" in device_types

    def test_loaded_language_detected(self, device_types):
        """Pejoratives 'pervert', 'predator', 'creep' should fire loaded_language."""
        assert "loaded_language" in device_types

    def test_walking_camera_detected(self, device_types):
        """'cameras on your face' should fire walking_camera."""
        assert "walking_camera" in device_types

    def test_ironic_quotation_pervert_glasses(self, device_types):
        """'pervert glasses' in quotes should fire ironic_quotation."""
        assert "ironic_quotation" in device_types
