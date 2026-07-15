"""Tests for Gizmodo smart glasses celebrity backlash article (Jul 14, 2026).

Article: "Smart Glasses Backlash Is Reaching New Celebrity Heights"
Publication: Gizmodo
Date: July 14, 2026
URL: https://gizmodo.com/smart-glasses-backlash-is-reaching-new-celebrity-heights-2000784767

Analysis context: Celebrity cultural authority framing, Google Glass failure
precedent analogy, source balance (3:1 adversarial), and a Ray-Ban compound
word false-positive fix in source extraction.
"""

import pytest

from mediascope.analysis import detect_entities, detect_framing_devices, extract_sources


ARTICLE_TEXT = (
    "Smart glasses are, without argument, more popular than they have ever been. "
    "Meta alone has sold millions of pairs, and even Apple is reportedly interested "
    "in the category, with Google and Samsung waiting in the wings. But for each "
    "step smart glasses take towards going mainstream, there are just as many "
    "people taking a step (or several) back, and some of those people are actual "
    "celebrities.\n\n"
    "Can I just say, for the record, fuck the glasses, Lorde said on stage after "
    "lamenting the fact that it is difficult to tell when someone is wearing "
    "normal glasses or smart glasses with a camera on them.\n\n"
    "The sentiment is not particularly novel plenty of people are averse to the "
    "idea of smart glasses but rarely have we seen this level of backlash on a "
    "stage that is not overtly political or backed by an advocacy group. The "
    "comments also feel especially pointed given the fact that we just saw "
    "arguably the biggest celebrity smart glasses co-sign by Kylie Jenner, who "
    "helped design a version of Metas smart glasses called the Starfire Kylie "
    "Edition. Those glasses have been the center of a major ad push involving "
    "Jenner, which has helped cement Metas smart glasses on an even more "
    "mainstream level.\n\n"
    "Lorde is not alone in the celebrity world in pushing back against smart "
    "glasses. Tyler the Creator recently blasted Ray-Ban Meta AI glasses on "
    "Instagram, writing, Anyone who uses these glasses is a real weirdo, linking "
    "to an article from Wired about smart glasses and surveillance.\n\n"
    "What is most interesting about the celebrity backlash against smart glasses "
    "is the potential implications. Way back in 2013, when Google tried, and "
    "failed, to force Google Glass onto the scene, the proverbial nail in the "
    "coffin was not regulation, policy, or anything even remotely official; it "
    "was social perception. People did not buy Google Glass in large part because "
    "they did not want to be perceived as a glasshole. And in terms of swaying "
    "public opinion, celebrities are far more likely to move the needle than, "
    "say, the New York court system.\n\n"
    "The question is, whose stance will win out? Kylies or Lordes?"
)


# ── Entity detection ──────────────────────────────────────────────────────

class TestEntities:
    """Verify entity detection on this article."""

    @pytest.fixture(autouse=True)
    def _run(self):
        self.entities = detect_entities(ARTICLE_TEXT)
        self.names = [e.entity for e in self.entities]
        self.clusters = {e.entity: e.cluster for e in self.entities}

    def test_meta_detected(self):
        assert "Meta" in self.names

    def test_meta_cluster(self):
        assert self.clusters.get("Meta") == "Meta"

    def test_apple_detected(self):
        assert "Apple" in self.names

    def test_google_detected(self):
        assert "Google" in self.names

    def test_samsung_detected(self):
        assert "Samsung" in self.names

    def test_kylie_jenner_detected(self):
        assert "Kylie Jenner" in self.names

    def test_kylie_jenner_cluster(self):
        assert self.clusters.get("Kylie Jenner") == "Celebrity/Influencer"

    def test_ray_ban_meta_clustered_to_meta(self):
        """Ray-Ban Meta should be clustered under Meta."""
        assert self.clusters.get("Ray-Ban Meta") == "Meta" or \
               any(e.cluster == "Meta" for e in self.entities
                   if "Ray-Ban" in e.entity or "Ray" in e.entity)

    def test_instagram_clustered_to_meta(self):
        assert self.clusters.get("Instagram") == "Meta"

    def test_wired_detected(self):
        assert "Wired" in self.names or "WIRED" in self.names

    def test_starfire_clustered_to_meta(self):
        """Starfire (Kylie Edition product) should be clustered under Meta."""
        assert self.clusters.get("Starfire") == "Meta"


# ── Framing device detection ─────────────────────────────────────────────

class TestFramingDevices:
    """Verify framing devices on this article."""

    @pytest.fixture(autouse=True)
    def _run(self):
        self.devices = detect_framing_devices(ARTICLE_TEXT)
        self.device_types = [d.device_type for d in self.devices]

    def test_loaded_language_backlash(self):
        """'backlash' and 'blasted' should trigger loaded_language."""
        assert "loaded_language" in self.device_types

    def test_loaded_language_blasted(self):
        """'blasted' should be detected as loaded language."""
        blasted_hits = [d for d in self.devices
                        if d.device_type == "loaded_language"
                        and "blasted" in d.evidence_text.lower()]
        assert len(blasted_hits) >= 1

    def test_failure_precedent_google_glass(self):
        """Google Glass reference ('Way back in 2013, when Google tried,
        and failed') should trigger failure_precedent."""
        assert "failure_precedent" in self.device_types


# ── Source extraction ─────────────────────────────────────────────────────

class TestSources:
    """Verify source extraction on this article."""

    @pytest.fixture(autouse=True)
    def _run(self):
        self.sources = extract_sources(ARTICLE_TEXT)
        self.source_names = [s.name for s in self.sources]

    def test_lorde_detected_as_source(self):
        """Lorde (said on stage) should be detected as a named source."""
        assert "Lorde" in self.source_names

    def test_ray_ban_not_false_positive(self):
        """'blasted Ray-Ban' should NOT extract 'Ray' as a source.
        Regression test: hyphenated compound words after attribution
        verbs must not be split into false-positive single-name sources.
        Discovered Jul 14, 2026."""
        assert "Ray" not in self.source_names

    def test_no_ray_source(self):
        """No source named 'Ray' should appear — it's a brand prefix."""
        ray_sources = [s for s in self.sources if s.name == "Ray"]
        assert len(ray_sources) == 0, (
            f"False positive: 'Ray' detected as source with verb "
            f"'{ray_sources[0].attribution_verb}'"
        )
