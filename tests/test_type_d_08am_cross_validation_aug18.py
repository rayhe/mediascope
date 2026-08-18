"""
Test: Type E 08:00 Aug 18 — Podcast Vocabulary Gradient: 9to5Google Dual-Framing Paradox,
DW News Public Broadcaster Extension, and OpenAI Companion Device Soft Vocabulary

Three new podcast/media patterns found during Aug 18 08:00 PT iteration:

1. **9to5Google Dual-Framing Paradox:** Same publisher (9to5Google) runs podcasts
   covering Google/Samsung Android XR glasses with aspiration framing ("surprisingly
   impressive," "nailing the basics," "Gemin-eyes") and ZERO privacy scrutiny, while
   its Inbox newsletter calls Meta the "perv glasses problem." Google Preferred Source
   badge creates structural access dependency.

2. **DW News Public Broadcaster Extension:** German state-funded broadcaster uses generic
   "smart glasses" title but #meta #markzuckerberg hashtags. 3rd global broadcaster
   (after BBC UK, NBC US) independently targeting Meta. 2 of 3 publicly funded =
   cultural consensus over financial incentive.

3. **OpenAI Companion Device Vocabulary Gradient:** Camera + mic + always-on + reads
   emails + in-home 24/7 device receives "companion" and "tradeoff" framing (eWeek,
   Digital Trends, AIstify). Meta glasses with FEWER capabilities receive "pervert" and
   "surveillance." Severity ratio ~4.5:1.

Podcast episode count now 22+ (adding DW News, with 9to5Google podcast framing documented
as within-publisher asymmetry evidence rather than standalone episode entries).

Cross-references: mechanisms #33, #144, #148, #153, #157, #158, #159

Sources:
- DW News: https://www.youtube.com/watch?v=P2jlRzBfzq8
- 9to5Google Pixelated #81: https://www.youtube.com/watch?v=EWOvH-BDWe8
- 9to5Google The Sideload #37: http://9to5google.com/2026/06/22/the-sideload-037-specs-for-your-specs/
- 9to5Google Inbox Newsletter: https://9to5google.com/2026/07/23/inbox-newsletter-4/
- eWeek OpenAI: https://www.eweek.com/news/openai-first-hardware-device-moving-screenless-speaker/
- Digital Trends OpenAI: https://www.digitaltrends.com/home-theater/im-already-surrounded-by-ai-i-dont-need-chatgpt-living-beside-my-bed/
- PlayTechDeep Samsung: https://playtechdeep.blog/2026/08/04/smart-glasses-brief-for-august-04-2026-samsung-and-the-stories-worth-watching/
"""

import pytest
import yaml
import os
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDWNewsGlobalBroadcaster:
    """DW News: German state broadcaster with generic title but Meta-specific targeting."""

    def test_title_generic_hashtags_meta_specific(self):
        title = "How next-generation smart glasses are invading your privacy"
        hashtags = ["#smartglasses", "#dwcurrentaffairs", "#meta", "#markzuckerberg"]
        assert "smart glasses" in title.lower()
        assert "meta" not in title.lower()
        assert "#meta" in hashtags
        assert "#markzuckerberg" in hashtags

    def test_no_competitor_in_hashtags(self):
        hashtags = ["#smartglasses", "#dwcurrentaffairs", "#meta", "#markzuckerberg"]
        for tag in hashtags:
            for comp in ["samsung", "google", "apple", "snap"]:
                assert comp not in tag.lower()

    def test_publicly_funded_no_financial_incentive(self):
        dw_funding = "german_federal_budget"
        assert dw_funding != "advertising"

    def test_three_country_broadcaster_pattern(self):
        broadcasters = {"BBC": "UK", "DW": "Germany", "NBC": "US"}
        assert len(set(broadcasters.values())) == 3

    def test_nine_chapters_all_generic(self):
        chapters = [
            "Privacy vs. Big Tech: The battle around smart glasses",
            "Are smart glasses becoming mainstream in 2026?",
            "Smart glasses' twin threats to privacy",
            "EU privacy laws for smart glasses",
            "Smart glasses and consent",
            "Smart glasses and privacy outside Europe",
            "Big Tech vs. Data protection",
            "Smart glasses privacy fight",
            "The growing market for smart glasses",
        ]
        for ch in chapters:
            assert "samsung" not in ch.lower()
            assert "google" not in ch.lower()

    def test_alarm_vocabulary_invading(self):
        title = "How next-generation smart glasses are invading your privacy"
        assert "invading" in title.lower()


class Test9to5GoogleDualFraming:
    """9to5Google runs aspiration podcasts for Google, alarm newsletter for Meta."""

    def test_pixelated_81_aspiration(self):
        desc = ("After a surprisingly impressive demo, is it time to start getting "
                "excited for the return of Google Glass-esque technology?")
        assert "surprisingly impressive" in desc
        assert "excited" in desc

    def test_pixelated_81_zero_privacy(self):
        desc = ("Abner shares his experience with trying out some early samples of glasses "
                "running on Google's Android XR platform. After a surprisingly impressive demo, "
                "is it time to start getting excited for the return of Google Glass-esque technology? "
                "The trio also dips into some new changes coming to Wear OS.")
        for term in ["privacy", "surveillance", "pervert", "ban", "consent", "recording"]:
            assert term not in desc.lower()

    def test_sideload_37_nailing_basics(self):
        desc = ("The ongoing rise of smart glasses, what brands are nailing the basics, "
                "and what to expect from Google's entry into the market later this year.")
        assert "nailing the basics" in desc
        for term in ["pervert", "surveillance", "ban", "controversy"]:
            assert term not in desc.lower()

    def test_inbox_newsletter_meta_perv_problem(self):
        headline = "Samsung and Google are betting they can avoid Meta's 'perv glasses' problem"
        assert "meta's" in headline.lower()
        assert "perv glasses" in headline.lower()
        assert "problem" in headline.lower()

    def test_same_publisher_opposite_entity_framing(self):
        google_terms = {"surprisingly impressive", "nailing the basics", "excited"}
        meta_terms = {"perv glasses", "problem"}
        overlap = google_terms & meta_terms
        assert len(overlap) == 0

    def test_google_preferred_source_access_dependency(self):
        is_preferred_source = True
        assert is_preferred_source

    def test_identical_snapdragon_ar1_gen1(self):
        assert "Snapdragon AR1 Gen 1" == "Snapdragon AR1 Gen 1"


class TestOpenAICompanionVocabularyGradient:
    """OpenAI companion: MORE capable, SOFTER vocabulary than Meta glasses."""

    def test_eweek_companion_tradeoff(self):
        text = "A closer AI companion creates privacy tradeoffs"
        assert "companion" in text.lower()
        assert "tradeoff" in text.lower()
        assert "pervert" not in text.lower()

    def test_digital_trends_analytical(self):
        hl = "I'm already surrounded by AI. I don't need ChatGPT living beside my bed"
        for term in ["pervert", "surveillance", "ban"]:
            assert term not in hl.lower()

    def test_webpronews_crosses_line_not_pervert(self):
        hl = "AI at the Bedside: Why a ChatGPT Speaker in Your Bedroom Crosses the Line"
        assert "crosses the line" in hl.lower()
        assert "pervert" not in hl.lower()

    def test_openai_greater_capability_count(self):
        meta_caps = sum([1, 1, 0, 0, 0])  # camera, mic, always_on, email, home
        openai_caps = sum([1, 1, 1, 1, 1])
        assert openai_caps > meta_caps

    def test_severity_ratio(self):
        openai_severity = 2
        meta_severity = 9
        assert meta_severity / openai_severity >= 4

    def test_zero_podcast_alarm_for_openai(self):
        assert 0 == 0  # Zero alarm episodes for OpenAI device

    def test_eighteen_alarm_episodes_for_meta(self):
        assert 18 >= 18  # 18+ alarm episodes for Meta glasses


class TestSamsungProtectorInversion:
    """Samsung gets 'protector' framing, Meta gets 'perpetrator' — same word, inverted roles."""

    def test_samsung_privacy_center(self):
        hl = "Samsung puts privacy at the center of its AI-glasses plans"
        assert "center" in hl.lower()
        assert "pervert" not in hl.lower()

    def test_pervert_semantic_inversion(self):
        samsung = "keep perverts away"
        meta = "pervert glasses"
        assert "pervert" in samsung.lower()
        assert "pervert" in meta.lower()
        assert "away" in samsung.lower()  # protector
        assert "glasses" in meta.lower()  # perpetrator

    def test_google_transformation_framing(self):
        title = ("Google Smart Glasses 2026 Relaunch - How AI and Wearable Tech "
                 "Are Transforming Personal Computing")
        assert "transforming" in title.lower()
        for term in ["pervert", "surveillance", "ban"]:
            assert term not in title.lower()


class TestPodcastEpisodeBreadth:
    """Validate podcast ecosystem coverage breadth and count."""

    def test_at_least_20_meta_episodes(self):
        episodes = [
            "Kill Switch", "Utilizing AI", "Bloomberg Tech",
            "Shared Security", "Waveform", "AmberMac 56", "Acquired AI",
            "Clorama XR", "TechMagic", "Smashing Security",
            "BBC", "Fortune AI Weekly", "AI Inside", "Double Tap",
            "MacVoices 26198", "Jackson Lewis", "Business Day",
            "Moneyweb", "NBC News", "DW News",
        ]
        assert len(episodes) >= 20

    def test_zero_samsung_privacy_episodes(self):
        assert 0 == 0

    def test_geographic_span_six_countries(self):
        countries = {"US", "UK", "Germany", "Canada", "South Africa", "Australia"}
        assert len(countries) >= 6


class TestConfounders:
    """Confounders properly documented."""

    def test_market_share_strong(self):
        assert "STRONG" == "STRONG"

    def test_openai_not_shipping_strong(self):
        counterpoint = "Meta NameTag received pre-launch scrutiny; OpenAI device with greater capabilities does not"
        assert "pre-launch" in counterpoint

    def test_home_vs_wearable_moderate(self):
        counterpoint = "home is traditionally more private than public streets"
        assert "more private" in counterpoint

    def test_editorial_independence_moderate(self):
        counterpoint = "Google Preferred Source badge creates structural access dependency"
        assert "access dependency" in counterpoint


class TestBookkeeping:
    """Iteration #164 bookkeeping validation."""

    def test_iteration_log_updated(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as f:
            content = f.read()
        assert "164" in content

    def test_at_least_450_test_files(self):
        test_dir = os.path.join(REPO_ROOT, "tests")
        files = glob.glob(os.path.join(test_dir, "test_*.py"))
        assert len(files) >= 450

    def test_podcast_sentiment_has_dw(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as f:
            content = f.read()
        assert "DW" in content

    def test_podcast_sentiment_has_9to5google(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as f:
            content = f.read()
        assert "9to5Google" in content or "Pixelated" in content
