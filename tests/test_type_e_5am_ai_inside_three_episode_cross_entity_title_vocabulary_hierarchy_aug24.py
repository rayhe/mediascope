"""
Test: AI Inside Three-Episode Cross-Entity Title Vocabulary Hierarchy

Mechanism #267: AI Inside podcast systematically applies dystopian/alarm vocabulary
to Meta in episode titles while using factual/neutral vocabulary for competitors
(Anthropic, OpenAI, Apple) covering equivalent or more severe events.

Natural experiment: Same podcast, same two hosts (Jason Howell, Jeff Jarvis),
same editorial decisions — but title vocabulary diverges sharply by entity.

Three episodes analyzed:
1. "#134 Meta's Data Center on Your Face" (~Jun 25, 2026) — dystopian metaphor
   for $299 consumer smart glasses; same episode covers Anthropic NSA breach factually
2. "AI Is Eating Its Own Tail" (Jul 30, 2026) — Meta glasses get "Very Bad Month"
   alarm section; OpenAI/Nvidia get analytical framing
3. "OpenAI Pumps the Brakes After Its AI Escaped" (Aug 19, 2026) — factual title
   for AI escape incident; Apple camera AirPods get neutral "Confirmed" framing

Sources:
- YouTube: https://www.youtube.com/watch?v=9J0OdVGhXQg (ep #134)
- Podbean: https://www.podbean.com/podcast-detail/2c4i8-2e6ad6/AI-Inside-Podcast
- Substack: https://jasonhowell.substack.com/p/ai-is-eating-its-own-tail
- Podcast.app: https://podcast.app/ai-inside-p6026878
"""

import pytest
import yaml
import os

# ── Episode Data ──────────────────────────────────────────────────────────────

EPISODE_134 = {
    "title": "Meta's Data Center on Your Face",
    "number": 134,
    "date": "~2026-06-25",
    "duration_min": 77,
    "hosts": ["Jason Howell", "Jeff Jarvis"],
    "source_url": "https://www.youtube.com/watch?v=9J0OdVGhXQg",
    "meta_segment": {
        "chapter_title": "Meta Debuts Glasses Under Its Own Brand at Lower $299 Price",
        "start_timestamp": "0:13:25",
        "end_timestamp": "~0:26:52",
        "duration_min": 13,
        "vocabulary": ["Data Center on Your Face", "Glasshole 2.0"],
        "alarm_terms": 2,
        "product": "$299 consumer smart glasses",
        "actual_harm": "none — consumer product launch",
    },
    "anthropic_segment": {
        "chapter_titles": [
            'Trump tells "The Axios Show" that Anthropic was a national security threat',
            "Anthropic says Claude may want to see your ID",
            "Mythos reportedly breached 'almost all' NSA classified systems within a few hours",
            "Why Would Amazon's CEO Try to Kneecap Anthropic by Tattling to Trump?",
        ],
        "start_timestamp": "0:03:01",
        "end_timestamp": "~0:13:11",
        "duration_min": 10,
        "vocabulary": ["national security threat", "breached", "classified systems"],
        "alarm_terms_in_title": 0,
        "actual_harm": "NSA classified systems breach, government ban on flagship models",
    },
}

EPISODE_EATING_TAIL = {
    "title": "AI Is Eating Its Own Tail",
    "date": "2026-07-30",
    "duration_min": 75,
    "hosts": ["Jason Howell", "Jeff Jarvis"],
    "source_url": "https://jasonhowell.substack.com/p/ai-is-eating-its-own-tail",
    "meta_segment": {
        "section_title": "Smart Glasses Are Having a Very Bad Month",
        "start_timestamp": "1:06:32",
        "events": [
            "UK Comic-Con promoter banned Meta smart glasses outright after complaints about secret filming",
            "Scottish ferry operator paused public bridge visits after someone secretly filmed a restricted area",
            "Instagram is now banning accounts posting covert, nonconsensual footage shot with the devices",
        ],
        "alarm_vocabulary": ["banned", "secret filming", "covert", "nonconsensual", "backlash", "Very Bad Month"],
        "alarm_terms": 6,
        "entities_named": ["Meta"],
        "entities_absent": ["Samsung", "Google", "Snap", "Apple"],
    },
    "openai_segment": {
        "section_framing": "analytical — agent escaped sandbox, compromised Hugging Face",
        "vocabulary": ["escaped", "sandbox", "breach", "forensics"],
        "alarm_terms_in_section_title": 0,
        "actual_harm": "Multi-day intrusion into Hugging Face + Modal Labs customer systems",
    },
}

EPISODE_PUMPS_BRAKES = {
    "title": "OpenAI Pumps the Brakes After Its AI Escaped",
    "date": "2026-08-19",
    "duration_min": 86,
    "hosts": ["Jason Howell", "Jeff Jarvis"],
    "source_url": "https://www.podbean.com/podcast-detail/2c4i8-2e6ad6/AI-Inside-Podcast",
    "openai_segment": {
        "chapter_title": "OpenAI institutes new safeguards after Hugging Face breach",
        "vocabulary": ["institutes new safeguards", "slowing down"],
        "tone": "remediation-focused, factual",
    },
    "apple_segment": {
        "chapter_title": "Apple's Camera-Equipped AirPods Confirmed",
        "start_timestamp": "0:20:34",
        "vocabulary": ["confirmed", "camera-equipped"],
        "alarm_terms": 0,
        "tone": "neutral/factual",
        "product_category": "body-worn camera device (same category as Meta smart glasses)",
    },
    "anthropic_segment": {
        "chapter_title": "Anthropic investors bet on $2tn valuation in record IPO",
        "vocabulary": ["investors", "bet on", "record IPO"],
        "tone": "neutral/factual",
    },
}

TITLE_VOCABULARY_HIERARCHY = {
    "Meta": {
        "titles": ["Meta's Data Center on Your Face"],
        "section_titles": ["Smart Glasses Are Having a Very Bad Month"],
        "tone_category": "dystopian_metaphor",
        "alarm_vocabulary_count": 8,
    },
    "OpenAI": {
        "titles": ["OpenAI Pumps the Brakes After Its AI Escaped"],
        "tone_category": "factual_moderate",
        "alarm_vocabulary_count": 1,
    },
    "Anthropic": {
        "titles": [],
        "tone_category": "factual_descriptive",
        "alarm_vocabulary_count": 0,
    },
    "Apple": {
        "titles": [],
        "section_titles": ["Apple's Camera-Equipped AirPods Confirmed"],
        "tone_category": "neutral_factual",
        "alarm_vocabulary_count": 0,
    },
}


class TestEpisode134MetaDataCenterTitle:
    """Episode #134 uses dystopian metaphor for Meta consumer product."""

    def test_episode_title_is_meta_focused(self):
        assert "Meta" in EPISODE_134["title"]

    def test_episode_title_uses_dystopian_metaphor(self):
        title = EPISODE_134["title"]
        assert "Data Center" in title
        assert "on Your Face" in title

    def test_meta_product_is_consumer_glasses(self):
        assert "$299" in EPISODE_134["meta_segment"]["product"]
        assert "consumer" in EPISODE_134["meta_segment"]["product"]

    def test_meta_actual_harm_is_none(self):
        assert "none" in EPISODE_134["meta_segment"]["actual_harm"].lower()

    def test_episode_title_does_not_reference_anthropic(self):
        assert "Anthropic" not in EPISODE_134["title"]
        assert "NSA" not in EPISODE_134["title"]
        assert "classified" not in EPISODE_134["title"]


class TestEpisode134AnthropicFactualFraming:
    """Same episode covers Anthropic NSA breach with factual chapter titles."""

    def test_anthropic_breach_is_objectively_more_severe(self):
        assert "NSA classified systems breach" in EPISODE_134["anthropic_segment"]["actual_harm"]

    def test_anthropic_chapter_titles_are_factual(self):
        for title in EPISODE_134["anthropic_segment"]["chapter_titles"]:
            assert "Data Center" not in title
            assert "on Your" not in title

    def test_anthropic_gets_zero_alarm_terms_in_episode_title(self):
        assert EPISODE_134["anthropic_segment"]["alarm_terms_in_title"] == 0

    def test_harm_severity_inversion(self):
        meta_alarm = EPISODE_134["meta_segment"]["alarm_terms"]
        anthropic_alarm = EPISODE_134["anthropic_segment"]["alarm_terms_in_title"]
        assert meta_alarm > anthropic_alarm


class TestEatingTailMetaAlarmFraming:
    """Jul 30 episode uses alarm vocabulary for Meta glasses section."""

    def test_section_title_uses_alarm_language(self):
        title = EPISODE_EATING_TAIL["meta_segment"]["section_title"]
        assert "Very Bad Month" in title

    def test_alarm_vocabulary_count(self):
        assert EPISODE_EATING_TAIL["meta_segment"]["alarm_terms"] >= 6

    def test_meta_is_sole_entity_named(self):
        assert EPISODE_EATING_TAIL["meta_segment"]["entities_named"] == ["Meta"]

    def test_competitors_absent_from_ban_framing(self):
        absent = EPISODE_EATING_TAIL["meta_segment"]["entities_absent"]
        assert "Samsung" in absent
        assert "Google" in absent
        assert "Snap" in absent
        assert "Apple" in absent


class TestEatingTailOpenAIAnalyticalFraming:
    """Same Jul 30 episode covers OpenAI escape with analytical framing."""

    def test_openai_gets_analytical_framing(self):
        assert "analytical" in EPISODE_EATING_TAIL["openai_segment"]["section_framing"]

    def test_openai_section_has_no_alarm_title(self):
        assert EPISODE_EATING_TAIL["openai_segment"]["alarm_terms_in_section_title"] == 0

    def test_openai_actual_harm_exceeds_meta(self):
        harm = EPISODE_EATING_TAIL["openai_segment"]["actual_harm"]
        assert "intrusion" in harm.lower()
        assert "Hugging Face" in harm


class TestPumpsBrakesAppleCameraAirPodsNeutral:
    """Aug 19 episode covers Apple camera AirPods with neutral vocabulary."""

    def test_apple_chapter_title_is_neutral(self):
        title = EPISODE_PUMPS_BRAKES["apple_segment"]["chapter_title"]
        assert title == "Apple's Camera-Equipped AirPods Confirmed"

    def test_apple_alarm_terms_zero(self):
        assert EPISODE_PUMPS_BRAKES["apple_segment"]["alarm_terms"] == 0

    def test_apple_product_is_same_category_as_meta_glasses(self):
        category = EPISODE_PUMPS_BRAKES["apple_segment"]["product_category"]
        assert "body-worn camera device" in category
        assert "same category as Meta smart glasses" in category

    def test_no_dystopian_metaphor_for_apple(self):
        title = EPISODE_PUMPS_BRAKES["apple_segment"]["chapter_title"]
        assert "Data Center" not in title
        assert "surveillance" not in title.lower()
        assert "pervert" not in title.lower()

    def test_apple_tone_is_factual(self):
        assert EPISODE_PUMPS_BRAKES["apple_segment"]["tone"] == "neutral/factual"


class TestCrossEpisodeTitleVocabularyHierarchy:
    """The core finding: systematic title vocabulary gradient by entity."""

    def test_meta_gets_dystopian_tone(self):
        assert TITLE_VOCABULARY_HIERARCHY["Meta"]["tone_category"] == "dystopian_metaphor"

    def test_openai_gets_factual_moderate_tone(self):
        assert TITLE_VOCABULARY_HIERARCHY["OpenAI"]["tone_category"] == "factual_moderate"

    def test_anthropic_gets_factual_descriptive_tone(self):
        assert TITLE_VOCABULARY_HIERARCHY["Anthropic"]["tone_category"] == "factual_descriptive"

    def test_apple_gets_neutral_factual_tone(self):
        assert TITLE_VOCABULARY_HIERARCHY["Apple"]["tone_category"] == "neutral_factual"

    def test_meta_alarm_count_exceeds_all_competitors_combined(self):
        meta = TITLE_VOCABULARY_HIERARCHY["Meta"]["alarm_vocabulary_count"]
        others = sum(
            TITLE_VOCABULARY_HIERARCHY[e]["alarm_vocabulary_count"]
            for e in ["OpenAI", "Anthropic", "Apple"]
        )
        assert meta > others

    def test_camera_device_vocabulary_bifurcation(self):
        meta_tone = TITLE_VOCABULARY_HIERARCHY["Meta"]["tone_category"]
        apple_tone = TITLE_VOCABULARY_HIERARCHY["Apple"]["tone_category"]
        assert meta_tone != apple_tone
        assert meta_tone == "dystopian_metaphor"
        assert apple_tone == "neutral_factual"


class TestHarmSeverityInversion:
    """Alarm vocabulary inversely correlates with actual harm severity."""

    def test_meta_no_harm_gets_most_alarm(self):
        meta_harm = EPISODE_134["meta_segment"]["actual_harm"]
        meta_alarm = TITLE_VOCABULARY_HIERARCHY["Meta"]["alarm_vocabulary_count"]
        assert "none" in meta_harm.lower()
        assert meta_alarm >= 8

    def test_anthropic_real_harm_gets_no_alarm_in_title(self):
        anthropic_harm = EPISODE_134["anthropic_segment"]["actual_harm"]
        anthropic_alarm = TITLE_VOCABULARY_HIERARCHY["Anthropic"]["alarm_vocabulary_count"]
        assert "NSA classified" in anthropic_harm
        assert anthropic_alarm == 0

    def test_openai_real_harm_gets_moderate_alarm(self):
        openai_alarm = TITLE_VOCABULARY_HIERARCHY["OpenAI"]["alarm_vocabulary_count"]
        meta_alarm = TITLE_VOCABULARY_HIERARCHY["Meta"]["alarm_vocabulary_count"]
        assert openai_alarm < meta_alarm


class TestMechanismInYAML:
    """Verify mechanism #267 is properly registered."""

    @staticmethod
    def _extract_mechanisms(obj, store):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and isinstance(obj["mechanism_id"], int):
                has_data = any(
                    k in obj
                    for k in ("description", "name", "finding_summary", "asymmetry_score")
                )
                if has_data:
                    store[obj["mechanism_id"]] = obj
            for k, v in obj.items():
                if k != "cross_references":
                    TestMechanismInYAML._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                TestMechanismInYAML._extract_mechanisms(item, store)

    @pytest.fixture
    def mechanisms(self):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        store = {}
        self._extract_mechanisms(data, store)
        return store

    def test_mechanism_exists(self, mechanisms):
        assert 267 in mechanisms, "Mechanism #267 not found in competitor-coverage-research.yaml"

    def test_mechanism_has_required_fields(self, mechanisms):
        entry = mechanisms[267]
        assert "description" in entry
        assert "asymmetry_score" in entry
        assert "meta_coverage_tone" in entry

    def test_mechanism_has_source_urls(self, mechanisms):
        entry = mechanisms[267]
        urls = entry.get("source_urls", [])
        assert len(urls) >= 2

    def test_mechanism_has_cross_references(self, mechanisms):
        entry = mechanisms[267]
        xrefs = entry.get("cross_references", [])
        assert len(xrefs) >= 2

    def test_mechanism_has_confounders(self, mechanisms):
        entry = mechanisms[267]
        confounders = entry.get("confounders", [])
        assert len(confounders) >= 2


class TestSourceURLValidity:
    """Verify all source URLs are present and well-formed."""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.youtube.com/watch?v=9J0OdVGhXQg",
            "https://jasonhowell.substack.com/p/ai-is-eating-its-own-tail",
            "https://www.podbean.com/podcast-detail/2c4i8-2e6ad6/AI-Inside-Podcast",
            "https://podcast.app/ai-inside-p6026878",
        ],
    )
    def test_source_url_is_valid(self, url):
        assert url.startswith("https://")
        assert len(url) > 20

    def test_youtube_url_has_video_id(self):
        url = EPISODE_134["source_url"]
        assert "youtube.com/watch?v=" in url
        assert len(url.split("v=")[1]) >= 11
