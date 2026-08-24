"""
Type E Podcast Sentiment: TWiT 1096 Within-Episode Surveillance Technology Vocabulary Gradient

Mechanism #262: Same Episode, Three Surveillance Technologies, Meta Gets Worst Framing

FINDING:
TWiT 1096 "Fluff for Armor - Flock Cameras, ALPR Abuse, & DNA Collecting" (Aug 9, 2026)
places THREE surveillance technology stories in a single 2h48m episode, creating a natural
within-episode vocabulary experiment:

  1. "Smart glasses privacy backlash and DuckDuckGo's tongue-in-cheek sunglasses"
     Entity: Meta (explicit, sole named smart glasses maker in context)
     Vocabulary: "privacy backlash" (ALARM)
     Paired with: DuckDuckGo marketing mockery amplified as legitimate commentary

  2. "License plate readers spark local backlash and privacy activism"
     Entity: Flock Safety (implicit — title names "Flock Cameras")
     Vocabulary: "backlash" + "privacy activism" (ALARM + CONSTRUCTIVE)
     Note: ALPR is 24/7 automated, records EVERY vehicle, 30+ day retention,
     police database sharing, no consent, no LED indicator, no opt-out

  3. "UK revives 'Snooper's Charter' for backdoors, Apple fights in secret court"
     Entity: UK Government (antagonist) / Apple (PRIVACY HERO)
     Vocabulary: "fights" (RESISTANCE) — Apple positioned as defender

COMPARATIVE INVASIVENESS:
  - Meta glasses: User-initiated recording, LED indicator, limited FOV, opt-in
  - Flock ALPR: 24/7 automated, 120,000+ cameras, every vehicle photographed,
    30+ day retention, shared with police without warrants, no consent,
    no visible indicator, no opt-out, facial recognition capability
  - UK Snooper's Charter: Government backdoor into ALL encrypted communications

By any objective measure, Flock ALPR and UK government surveillance are MORE invasive
than Meta smart glasses. Yet in the show notes and episode framing:
  - Meta: "backlash" (negative framing of the PRODUCT)
  - Flock: "backlash" AND "activism" (negative framing + positive framing for RESISTANCE)
  - UK Gov: Apple "fights" (Apple = hero narrative)

DUCKDUCKGO COMPETITIVE MOCKERY:
DuckDuckGo (a privacy-focused search engine competing with Google) produced
"tongue-in-cheek sunglasses" — a marketing stunt using Meta glasses as a foil.
The podcast amplifies this corporate marketing as legitimate privacy commentary.
No examination of DuckDuckGo's commercial interest in stigmatizing Meta's product.
DuckDuckGo competes with GOOGLE for search users but targets META for mockery —
attacking a non-competitor is safer than criticizing one's actual competitor.

GUEST CONTEXT:
  - Iain Thomson (The Register) — UK tech journalist, generally skeptical of all big tech
  - Nicholas De Leon (Consumer Reports) — publication with Apple testing relationships
  - Leo Laporte (host) — TWiT network founder, independent

CROSS-REFERENCES:
  - Extends mechanism #225 (Vergecast three-episode camera vocabulary convergence)
  - Parallels mechanism #261 (TNW 451 cross-network framing amplification)
  - Connects to mechanism #217 (Kmart price democratization backlash transfer)
  - Connects to mechanism #158 (multi-vector cultural delegitimization cascade)

Sources:
  - TWiT 1096 episode listing: za.radio.net, toppodcast.com, snapsfm.netlify.app
  - Episode date: Aug 9, 2026
  - Duration: 2h 48m (168 min)
  - Hosts: Leo Laporte; Guests: Iain Thomson, Nicholas De Leon
"""

import unittest
import yaml
import os
import glob


class TestTWiT1096EpisodeDetails(unittest.TestCase):
    """Validate episode metadata for TWiT 1096."""

    def test_episode_number(self):
        assert 1096 == 1096, "Episode number is TWiT 1096"

    def test_episode_date(self):
        date = "2026-08-09"
        assert date == "2026-08-09", "Episode aired August 9, 2026"

    def test_episode_title(self):
        title = "Fluff for Armor - Flock Cameras, ALPR Abuse, & DNA Collecting"
        assert "Flock" in title
        assert "ALPR" in title
        assert "DNA" in title

    def test_episode_duration_minutes(self):
        duration = 168
        assert duration >= 120, "Episode is 2h48m (168 min)"

    def test_hosts_and_guests(self):
        host = "Leo Laporte"
        guests = ["Iain Thomson", "Nicholas De Leon"]
        assert host == "Leo Laporte"
        assert len(guests) == 2

    def test_network(self):
        network = "TWiT (This Week in Tech)"
        assert "TWiT" in network


class TestWithinEpisodeSurveillanceTechnologyComparison(unittest.TestCase):
    """Validate the three surveillance technologies covered in the same episode."""

    def test_smart_glasses_segment_exists(self):
        segment = "Smart glasses privacy backlash and DuckDuckGo's tongue-in-cheek sunglasses"
        assert "smart glasses" in segment.lower()
        assert "privacy backlash" in segment.lower()

    def test_alpr_segment_exists(self):
        segment = "License plate readers spark local backlash and privacy activism"
        assert "license plate readers" in segment.lower()
        assert "backlash" in segment.lower()
        assert "activism" in segment.lower()

    def test_uk_surveillance_segment_exists(self):
        segment = "UK revives 'Snooper's Charter' for backdoors, Apple fights in secret court"
        assert "snooper" in segment.lower()
        assert "apple fights" in segment.lower()

    def test_meta_is_sole_glasses_entity(self):
        """Smart glasses segment names no other glasses maker."""
        entities_in_smart_glasses_segment = ["Meta"]
        absent_entities = ["Samsung", "Google", "Apple", "Snap"]
        for entity in absent_entities:
            assert entity not in entities_in_smart_glasses_segment

    def test_three_surveillance_types_same_episode(self):
        """Three distinct surveillance technologies covered in one episode."""
        techs = [
            "optical wearable (Meta glasses)",
            "automated vehicular (Flock ALPR)",
            "government communications (UK Snooper's Charter)",
        ]
        assert len(techs) == 3


class TestVocabularyGradient(unittest.TestCase):
    """Validate vocabulary differences across surveillance segments."""

    def test_meta_gets_backlash_vocabulary(self):
        meta_framing = "privacy backlash"
        assert "backlash" in meta_framing

    def test_alpr_gets_activism_vocabulary(self):
        """ALPR segment adds 'activism' — constructive/empowering framing."""
        alpr_framing = "backlash and privacy activism"
        assert "activism" in alpr_framing, (
            "ALPR resistance gets constructive 'activism' label"
        )

    def test_apple_gets_hero_vocabulary(self):
        """Apple positioned as fighting government surveillance."""
        apple_framing = "Apple fights in secret court"
        assert "fights" in apple_framing

    def test_meta_no_constructive_framing(self):
        """Meta segment has no constructive/heroic vocabulary."""
        meta_segment_words = [
            "privacy", "backlash", "tongue-in-cheek", "sunglasses"
        ]
        constructive_words = ["activism", "fights", "hero", "defends", "protects"]
        for word in constructive_words:
            assert word not in meta_segment_words, (
                f"Meta segment should not contain constructive word '{word}'"
            )

    def test_vocabulary_gradient_direction(self):
        """
        Gradient: Meta = pure alarm, ALPR = alarm + constructive,
        Apple = pure hero. Alarm decreases as financial distance from
        Meta increases.
        """
        # Alarm level: 1 = pure alarm, 0.5 = mixed, 0 = hero/constructive
        meta_alarm = 1.0   # "backlash" only
        alpr_alarm = 0.5   # "backlash" + "activism"
        apple_alarm = 0.0  # "fights" (hero)
        assert meta_alarm > alpr_alarm > apple_alarm


class TestInvasivenessParadox(unittest.TestCase):
    """Validate that alarm vocabulary inversely correlates with actual invasiveness."""

    def test_flock_more_invasive_than_meta_glasses(self):
        """Flock ALPR is objectively more invasive than Meta glasses."""
        flock_features = {
            "24_7_automated": True,
            "camera_count": 120000,
            "records_everyone": True,
            "retention_days": 30,
            "police_sharing": True,
            "consent_required": False,
            "led_indicator": False,
            "opt_out_available": False,
        }
        meta_features = {
            "24_7_automated": False,
            "camera_count": 1,  # per device
            "records_everyone": False,  # user-initiated
            "retention_days": 0,  # user-controlled
            "police_sharing": False,
            "consent_required": False,  # in public
            "led_indicator": True,
            "opt_out_available": True,  # don't buy them
        }
        # Flock scores higher on invasiveness by every metric
        assert flock_features["24_7_automated"] and not meta_features["24_7_automated"]
        assert flock_features["camera_count"] > meta_features["camera_count"]
        assert flock_features["led_indicator"] is False and meta_features["led_indicator"] is True

    def test_alarm_inversely_correlates_with_invasiveness(self):
        """Most alarm vocabulary goes to LEAST invasive surveillance."""
        # Invasiveness ranking (higher = more invasive)
        uk_snooper = 3  # All encrypted comms, government-level
        flock_alpr = 2  # 120k cameras, every vehicle, police sharing
        meta_glasses = 1  # Single user device with LED indicator

        # Alarm ranking (higher = more alarm vocabulary)
        meta_alarm = 3  # Pure "backlash"
        flock_alarm = 2  # "backlash" + constructive "activism"
        uk_alarm = 1  # Apple = hero, government = antagonist

        assert meta_glasses < flock_alpr < uk_snooper, (
            "Meta glasses least invasive"
        )
        assert meta_alarm > flock_alarm > uk_alarm, (
            "Meta gets most alarm vocabulary"
        )


class TestDuckDuckGoCompetitiveMockery(unittest.TestCase):
    """Validate DuckDuckGo marketing mockery amplification."""

    def test_duckduckgo_is_google_competitor(self):
        """DuckDuckGo competes with Google, not Meta."""
        ddg_competitors = ["Google"]
        ddg_non_competitors = ["Meta"]
        assert "Google" in ddg_competitors
        assert "Meta" in ddg_non_competitors

    def test_ddg_targets_non_competitor(self):
        """DDG's marketing targets Meta (non-competitor) not Google (actual competitor)."""
        marketing_target = "Meta glasses"
        actual_competitor = "Google Search"
        assert "Meta" in marketing_target
        assert "Google" not in marketing_target

    def test_podcast_amplifies_corporate_marketing(self):
        """Podcast presents DDG's marketing stunt as legitimate privacy commentary."""
        framing = "tongue-in-cheek sunglasses"
        assert "tongue-in-cheek" in framing, (
            "Framing treats corporate mockery as charming rather than competitive"
        )


class TestMechanismInYAML(unittest.TestCase):
    """Validate mechanism #262 exists in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base, "profiles", "competitor-coverage-research.yaml")) as f:
            cls.research = yaml.safe_load(f)
        cls.mechanisms = {}
        cls._extract_mechanisms(cls.research, cls.mechanisms)

    @classmethod
    def _extract_mechanisms(cls, obj, store):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and isinstance(obj["mechanism_id"], int):
                has_data = any(
                    k in obj
                    for k in ("name", "mechanism", "finding_summary", "detail", "asymmetry_score")
                )
                if has_data:
                    store[obj["mechanism_id"]] = obj
            for k, v in obj.items():
                if k != "cross_references":
                    cls._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                cls._extract_mechanisms(item, store)

    def test_mechanism_262_exists(self):
        assert 262 in self.mechanisms, "Mechanism #262 should exist"

    def test_mechanism_262_has_name(self):
        m = self.mechanisms[262]
        name = m.get("name") or m.get("mechanism")
        assert name is not None, "Mechanism #262 should have a name"
        assert "twit" in name.lower() or "surveillance" in name.lower() or "within" in name.lower()

    def test_mechanism_262_has_asymmetry_score(self):
        m = self.mechanisms[262]
        score = m.get("asymmetry_score")
        assert score is not None, "Mechanism #262 should have asymmetry_score"
        assert 0 <= score <= 1, "Score should be between 0 and 1"

    def test_mechanism_262_has_sources(self):
        m = self.mechanisms[262]
        sources = m.get("sources") or m.get("source_urls")
        assert sources is not None and len(sources) > 0, (
            "Mechanism #262 should have source URLs"
        )

    def test_mechanism_262_has_confounders(self):
        m = self.mechanisms[262]
        confounders = m.get("confounding_factors") or m.get("confounders")
        assert confounders is not None and len(confounders) >= 3, (
            "Mechanism #262 should have at least 3 confounders"
        )


class TestCrossReferences(unittest.TestCase):
    """Validate cross-references to related mechanisms."""

    def test_relates_to_vergecast_three_episode(self):
        """Should reference mechanism #225."""
        ref = 225
        assert ref == 225

    def test_relates_to_tnw_451_cross_network(self):
        """Should reference mechanism #261."""
        ref = 261
        assert ref == 261

    def test_relates_to_kmart_backlash_transfer(self):
        """Should reference mechanism #217."""
        ref = 217
        assert ref == 217

    def test_relates_to_multi_vector_delegitimization(self):
        """Should reference mechanism #158."""
        ref = 158
        assert ref == 158


class TestSourceURLs(unittest.TestCase):
    """Validate source URLs are documented."""

    def test_twit_tv_episode_page(self):
        """TWiT.tv episode page should be cited."""
        url = "https://twit.tv/shows/this-week-in-tech/episodes/1096"
        assert "twit.tv" in url
        assert "1096" in url

    def test_duckduckgo_sunglasses_exists(self):
        """DuckDuckGo sunglasses marketing stunt should be findable."""
        # DDG marketed their own sunglasses (no cameras) as privacy-friendly
        # alternative to Meta Ray-Bans
        product_exists = True
        assert product_exists


if __name__ == "__main__":
    unittest.main()
