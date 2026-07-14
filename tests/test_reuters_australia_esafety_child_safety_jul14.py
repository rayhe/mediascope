"""Tests for Reuters Australia eSafety child safety article (Jul 14, 2026).

Validates entity detection improvements:
- iMessage → Apple cluster (new alias)
- Google Messages → Google cluster (new alias)
- Discord → Discord cluster (new cluster)
- Julie Inman Grant → Australia cluster (new alias)

Also validates framing device detection on a multi-entity regulatory article
where the regulator (Australia/eSafety) is the primary actor and multiple
tech companies are passive subjects of criticism.
"""

import pathlib
import pytest
from mediascope.analyze.entities import detect_entities, get_entity_distribution, get_primary_entity
from mediascope.analyze.framing import detect_framing_devices

_ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "examples"
    / "sample_output"
    / "reuters_australia_esafety_child_safety_2026_07_14_article.txt"
)

@pytest.fixture(scope="module")
def article_text():
    return _ARTICLE_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def mentions(article_text):
    return detect_entities(article_text)


@pytest.fixture(scope="module")
def distribution(mentions):
    return get_entity_distribution(mentions)


# --- Entity detection: new aliases and cluster ---

class TestEntityIMessageApple:
    """iMessage should be detected as an Apple cluster entity."""

    def test_imessage_detected(self, mentions):
        imessage_mentions = [m for m in mentions if m.entity == "iMessage"]
        assert len(imessage_mentions) >= 1, "iMessage should be detected at least once"

    def test_imessage_apple_cluster(self, mentions):
        imessage_mentions = [m for m in mentions if m.entity == "iMessage"]
        for m in imessage_mentions:
            assert m.cluster == "Apple", f"iMessage should map to Apple cluster, got {m.cluster}"

    def test_imessage_canonical_name(self, mentions):
        imessage_mentions = [m for m in mentions if m.entity == "iMessage"]
        for m in imessage_mentions:
            assert m.canonical_name == "iMessage", f"Canonical name should be iMessage, got {m.canonical_name}"


class TestEntityGoogleMessages:
    """Google Messages should be detected as a Google cluster entity."""

    def test_google_messages_detected(self, mentions):
        gm_mentions = [m for m in mentions if m.canonical_name == "Google Messages"]
        assert len(gm_mentions) >= 1, "Google Messages should be detected at least once"

    def test_google_messages_cluster(self, mentions):
        gm_mentions = [m for m in mentions if m.canonical_name == "Google Messages"]
        for m in gm_mentions:
            assert m.cluster == "Google", f"Google Messages should map to Google cluster, got {m.cluster}"


class TestEntityDiscord:
    """Discord should be detected as a Discord cluster entity."""

    def test_discord_detected(self, mentions):
        discord_mentions = [m for m in mentions if m.entity == "Discord"]
        assert len(discord_mentions) >= 1, "Discord should be detected at least once"

    def test_discord_cluster(self, mentions):
        discord_mentions = [m for m in mentions if m.entity == "Discord"]
        for m in discord_mentions:
            assert m.cluster == "Discord", f"Discord should map to Discord cluster, got {m.cluster}"

    def test_discord_count(self, mentions):
        discord_mentions = [m for m in mentions if m.cluster == "Discord"]
        assert len(discord_mentions) == 2, f"Discord should appear exactly 2 times, got {len(discord_mentions)}"


class TestEntityJulieInmanGrant:
    """Julie Inman Grant should be detected as an Australia cluster entity."""

    def test_julie_inman_grant_detected(self, mentions):
        jig_mentions = [m for m in mentions if "Julie Inman Grant" in m.canonical_name]
        assert len(jig_mentions) >= 1, "Julie Inman Grant should be detected at least once"

    def test_julie_inman_grant_australia_cluster(self, mentions):
        jig_mentions = [m for m in mentions if "Julie Inman Grant" in m.canonical_name]
        for m in jig_mentions:
            assert m.cluster == "Australia", f"Julie Inman Grant should map to Australia cluster, got {m.cluster}"


# --- Entity distribution: multi-entity regulatory article ---

class TestMultiEntityDistribution:
    """Multi-entity regulatory article should show distributed entity coverage."""

    def test_australia_highest_count(self, distribution):
        assert distribution.get("Australia", 0) >= 6, (
            f"Australia should have at least 6 mentions as primary actor, got {distribution.get('Australia', 0)}"
        )

    def test_primary_entity_is_australia(self, mentions):
        primary = get_primary_entity(mentions)
        assert primary == "Australia", f"Primary entity should be Australia (regulator), got {primary}"

    def test_meta_present(self, distribution):
        assert "Meta" in distribution, "Meta should be present in entity distribution"

    def test_google_present(self, distribution):
        assert "Google" in distribution, "Google should be present in entity distribution"

    def test_apple_present(self, distribution):
        assert "Apple" in distribution, "Apple should be present in entity distribution"

    def test_snap_present(self, distribution):
        assert "Snap" in distribution, "Snap should be present in entity distribution"

    def test_microsoft_present(self, distribution):
        assert "Microsoft" in distribution, "Microsoft should be present in entity distribution"

    def test_discord_present(self, distribution):
        assert "Discord" in distribution, "Discord should be present in entity distribution"

    def test_at_least_seven_clusters(self, distribution):
        assert len(distribution) >= 7, (
            f"Multi-entity article should have at least 7 entity clusters, got {len(distribution)}"
        )


# --- Framing device detection ---

class TestFramingDevices:
    """Framing device detection for a wire-service regulatory article."""

    @classmethod
    @pytest.fixture(scope="class")
    def devices(cls, article_text):
        return detect_framing_devices(article_text)

    def test_no_comment_detected(self, devices):
        device_types = {d.device_type for d in devices}
        assert "no_comment_implication" in device_types, (
            "no_comment_implication should fire on 'did not immediately respond'"
        )

    def test_regulatory_shadow_detected(self, devices):
        device_types = {d.device_type for d in devices}
        assert "regulatory_shadow" in device_types, (
            "regulatory_shadow should fire on 'raising concerns over' / 'raised concerns about'"
        )

    def test_scale_magnitude_detected(self, devices):
        device_types = {d.device_type for d in devices}
        assert "scale_magnitude" in device_types, (
            "scale_magnitude should fire on 'more than 2,000 complaints'"
        )

    def test_catastrophizing_detected(self, devices):
        device_types = {d.device_type for d in devices}
        assert "catastrophizing" in device_types, (
            "catastrophizing should fire on 'devastating impact'"
        )

    def test_total_device_count_reasonable(self, devices):
        count = len(devices)
        assert 8 <= count <= 20, (
            f"Wire-service article should have 8-20 framing devices, got {count}"
        )
