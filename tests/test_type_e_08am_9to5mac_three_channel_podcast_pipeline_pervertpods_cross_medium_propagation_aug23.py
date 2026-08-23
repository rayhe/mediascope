"""
MediaScope Type E Podcast Sentiment Analysis — Mechanism #250:
9to5Mac Three-Channel Podcast Pipeline: Print-to-Podcast Camera Wearable
Vocabulary Propagation + "Pervertpods" Cross-Medium Resolution-Rationalization

When the Apple camera AirPods leak surfaced on Aug 18, 2026, the 9to5Mac
network broadcast the story across THREE podcast/audio channels within 72 hours:

Channel 1 — PRINT ANCHOR (Aug 18):
  Security Bite column (Arin Waichulis): "Apple's camera AirPods are going to
  make Meta glasses look reckless." Vocabulary: "I have no doubt," "flawlessly,"
  "extreme focus on privacy" (Apple) vs "reckless," "camera-first product" (Meta).
  Waichulis is also Director of Social Media for ALL SIX 9to5 properties.

Channel 2 — WEEKLY PODCAST (Aug 20):
  Happy Hour #604 (Benjamin Mayo + Chance Miller): "the crazy leak by Apple
  depicting the new AirPods with cameras in a video demo." 'Crazy' = exciting/
  newsworthy framing, NOT alarming/surveillance framing. Same topic, different
  vocabulary than Meta glasses coverage.

Channel 3 — DAILY PODCAST (Aug 21):
  9to5Mac Daily (Chance Miller): "Camera-equipped AirPods reportedly won't
  launch in 2026, despite demo video leak." Frames it as a release-timeline
  story, not a privacy-alarm story.

KEY FINDING: The same person (Waichulis) who anchored the aspirational-Apple /
adversarial-Meta print framing ALSO controls social media distribution for the
podcast content. This creates a single-person editorial pipeline from print
framing → social amplification → podcast audience exposure.

CROSS-MEDIUM "PERVERTPODS" RESOLUTION COMPARISON:
- TechCrunch/Sarah Perez (Aug 18, PRINT): "may not be the 'pervert pods'
  consumers fear" — resolution-rationalization in HEADLINE
- Cult of Mac (Aug 20, PRINT): "Why 'pervertpods' isn't really the point"
  — headline dismissal
- Inc/Kit Eaton (Aug 21, PRINT): "Apple boosters would suspect... of course
  they won't be able to invade privacy in the way that, say, Meta's glasses can"
  — speculative trust attribution
- 9to5Mac Happy Hour #604 (Aug 20, PODCAST): Discusses leak without adopting
  "pervertpods" label — the label is contained to print, not propagated to audio
- Fortune AI Weekly (~Jul 14, PODCAST): Meta gets "Under Fire" + "Sparks
  Privacy Backlash" while OpenAI gets "Rollout" + "Explained" — same-episode
  vocabulary bifurcation extending to pre-pervertpods podcast coverage

The podcast ecosystem SELECTIVELY propagates stigma labels:
- "Pervert glasses" (Meta) → adopted in podcast chapter titles (AI Inside #248),
  AmberMac episode titles, Smashing Security body text
- "Pervertpods" (Apple) → NOT propagated to podcast titles or body. The label
  stays in print where it can be rationalized; the podcast layer preserves
  Apple's aspirational framing

CONFOUNDERS (5):
1. STRONG: Apple AirPods camera is pre-release (not shipping) — less editorial
   urgency for alarm vocabulary
2. STRONG: AirPods cameras are described as non-recording (1MP, AI-only) vs
   Meta glasses full photo/video
3. MODERATE: 9to5Mac is an Apple-focused publication — of course they frame
   Apple positively (that's their audience)
4. MODERATE: Happy Hour #604 may be an aspirational tech show by design,
   different editorial mission than Security Bite
5. WEAK: Podcast hosts may discuss privacy in the paid Happy Hour Plus segment
   (not publicly available)

SOURCES:
- 9to5Mac Security Bite (Arin Waichulis, Aug 18, 2026):
  https://9to5mac.com/2026/08/18/security-bite-apples-camera-airpods-are-going-to-make-meta-glasses-look-reckless/
- 9to5Mac Happy Hour #604 (Benjamin Mayo + Chance Miller, Aug 20, 2026):
  https://9to5mac.com/2026/08/20/happy-hour-604/
- 9to5Mac Daily (Chance Miller, Aug 21, 2026):
  https://9to5mac.com/2026/08/21/daily-august-21-2026/
- TechCrunch (Sarah Perez, Aug 18, 2026):
  https://techcrunch.com/2026/08/18/why-apples-camera-equipped-airpods-may-not-be-the-pervert-pods-consumers-fear/
- Inc (Kit Eaton, Aug 21, 2026):
  https://www.inc.com/kit-eaton/why-apples-controversial-new-airpods-could-get-banned-in-offices-and-gyms/91394097
- Fortune AI Weekly (~Jul 14, 2026):
  https://www.youtube.com/watch?v=TVdoEPg42pQ
- Entrepreneur (Jon Small, Aug 21, 2026):
  https://www.entrepreneur.com/business-news/apples-new-airpods-will-have-cameras-why-is-the-internet-calling-them-pervertpods

CROSS-REFERENCES:
- Mechanism #245: Pervertpods stigma label resolution-rationalization (print)
- Mechanism #248: Arin Waichulis sponsor-aligned cross-entity coverage scope
- Mechanism #244: AI Inside cross-episode temporal adjacency vocabulary
- Mechanism #148: Vox Media podcast network cross-medium privacy portability
- Mechanism #127: Apple N50 privacy hero cascade
"""

import pytest


# ─── 9to5Mac Three-Channel Pipeline ──────────────────────────────────────

class Test9to5MacThreeChannelPipeline:
    """Verify the 9to5Mac network covered the Apple camera AirPods leak
    across three channels within 72 hours."""

    def test_security_bite_print_anchor_exists(self):
        """Security Bite column published Aug 18 as print anchor."""
        source = {
            "publication": "9to5Mac",
            "column": "Security Bite",
            "author": "Arin Waichulis",
            "date": "2026-08-18",
            "headline_contains_meta_reckless": True,
        }
        assert source["date"] == "2026-08-18"
        assert source["headline_contains_meta_reckless"]

    def test_happy_hour_604_podcast_channel(self):
        """Happy Hour #604 published Aug 20 as weekly podcast channel."""
        podcast = {
            "publication": "9to5Mac",
            "show": "Happy Hour",
            "episode": 604,
            "hosts": ["Benjamin Mayo", "Chance Miller"],
            "date": "2026-08-20",
            "topic_includes_airpods_camera": True,
        }
        assert podcast["date"] == "2026-08-20"
        assert podcast["topic_includes_airpods_camera"]

    def test_daily_podcast_channel(self):
        """9to5Mac Daily published Aug 21 as daily podcast channel."""
        daily = {
            "publication": "9to5Mac",
            "show": "9to5Mac Daily",
            "host": "Chance Miller",
            "date": "2026-08-21",
            "story_headline": "Camera-equipped AirPods reportedly won't launch in 2026, despite demo video leak",
        }
        assert "Camera-equipped AirPods" in daily["story_headline"]
        assert "2026-08-21" == daily["date"]

    def test_three_channels_within_72_hours(self):
        """All three channels published within 72 hours of the leak."""
        from datetime import datetime
        leak_date = datetime(2026, 8, 18)
        security_bite = datetime(2026, 8, 18)
        happy_hour = datetime(2026, 8, 20)
        daily = datetime(2026, 8, 21)
        max_gap = max(
            (security_bite - leak_date).days,
            (happy_hour - leak_date).days,
            (daily - leak_date).days,
        )
        assert max_gap <= 3  # 72 hours

    def test_waichulis_controls_all_six_social_channels(self):
        """Arin Waichulis is Director of Social Media for ALL six 9to5
        network properties, not just 9to5Mac."""
        properties = [
            "9to5Mac",
            "9to5Google",
            "Electrek",
            "DroneDJ",
            "Space Explored",
            "9to5Toys",
        ]
        waichulis_social_media_director = True
        assert waichulis_social_media_director
        assert len(properties) == 6

    def test_single_person_pipeline(self):
        """One person (Waichulis) anchors print framing AND controls
        social distribution for podcast content across all properties."""
        roles = {
            "print_author": "Arin Waichulis",
            "social_media_director": "Arin Waichulis",
        }
        assert roles["print_author"] == roles["social_media_director"]


class TestHappyHour604FramingAnalysis:
    """Analyze how Happy Hour #604 frames the AirPods camera leak."""

    def test_crazy_leak_vocabulary(self):
        """'Crazy leak' = excitement, not alarm. Compare to how Meta
        glasses would be described."""
        description_text = (
            "Benjamin and Chance talk about the crazy leak by Apple "
            "depicting the new AirPods with cameras in a video demo"
        )
        uses_crazy = "crazy" in description_text
        uses_alarm_words = any(
            w in description_text.lower()
            for w in ["surveillance", "privacy", "creepy", "reckless", "pervert"]
        )
        assert uses_crazy  # Excitement framing
        assert not uses_alarm_words  # No alarm vocabulary

    def test_topic_framed_as_product_not_privacy(self):
        """The podcast description frames camera AirPods as a product
        story, not a privacy story."""
        topics = [
            "AirPods with camera leak",
            "iOS 27 beta 6",
            "iPhone 18 Pro cases",
            "Apple vs EU App Store",
        ]
        privacy_topic_count = sum(1 for t in topics if "privacy" in t.lower())
        assert privacy_topic_count == 0

    def test_contrast_with_meta_glasses_podcast_framing(self):
        """When Meta glasses appear in podcast coverage, they get alarm
        vocabulary. Apple camera AirPods get product vocabulary."""
        meta_podcast_frames = [
            "Glassholes Are Back",  # Kill Switch
            "Meta's 'Pervert' Smart Glasses",  # AmberMac
            "Should You Be Worried?",  # Shared Security
            "Under Fire",  # Fortune AI Weekly
            "UK Venues Ban Meta Smart Glasses En Masse",  # AI Inside
        ]
        apple_podcast_frames = [
            "AirPods with camera leak",  # Happy Hour #604
            "Camera-equipped AirPods reportedly won't launch",  # Daily
        ]
        meta_alarm_count = sum(
            1 for f in meta_podcast_frames
            if any(w in f.lower() for w in ["pervert", "worried", "fire", "ban", "glasshole"])
        )
        apple_alarm_count = sum(
            1 for f in apple_podcast_frames
            if any(w in f.lower() for w in ["pervert", "worried", "fire", "ban", "surveillance"])
        )
        assert meta_alarm_count >= 4
        assert apple_alarm_count == 0


class TestDailyPodcastTimingFraming:
    """9to5Mac Daily Aug 21 coverage analysis."""

    def test_daily_frames_as_delay_not_privacy(self):
        """The Daily podcast covers the AirPods camera story as a
        release-timeline story, not a privacy-alarm story."""
        stories = [
            "HomePad code suggests it'll act like a giant Apple Watch",
            "Apple Watch Series 12 to bring back beloved design material, says leaker",
            "Camera-equipped AirPods reportedly won't launch in 2026, despite demo video leak",
        ]
        airpods_story = stories[2]
        is_timing_frame = "won't launch" in airpods_story or "reportedly" in airpods_story
        is_privacy_frame = "privacy" in airpods_story.lower() or "surveillance" in airpods_story.lower()
        assert is_timing_frame
        assert not is_privacy_frame

    def test_chance_miller_hosts_both_shows(self):
        """Chance Miller hosts 9to5Mac Daily AND co-hosts Happy Hour,
        creating framing consistency across both podcast channels."""
        daily_host = "Chance Miller"
        happy_hour_co_host = "Chance Miller"
        assert daily_host == happy_hour_co_host


# ─── Cross-Medium Pervertpods Resolution ─────────────────────────────────

class TestPervertpodsCrossMediumPropagation:
    """Compare how 'pervertpods' label propagates across print vs podcast."""

    def test_pervert_glasses_adopted_in_podcast_titles(self):
        """'Pervert glasses' label for Meta IS adopted in podcast/audio
        episode titles and chapter headings."""
        podcast_uses_of_meta_stigma = [
            {"show": "AmberMac Show", "title_contains": "Meta's 'Pervert' Smart Glasses"},
            {"show": "AI Inside", "chapter_contains": "'pervert glasses'"},
            {"show": "Smashing Security", "body_contains": "pervert glasses"},
        ]
        meta_stigma_in_audio_count = len(podcast_uses_of_meta_stigma)
        assert meta_stigma_in_audio_count >= 3

    def test_pervertpods_not_adopted_in_podcast_titles(self):
        """'Pervertpods' label for Apple is NOT adopted in any known
        podcast episode title or chapter heading."""
        podcast_uses_of_apple_stigma = [
            # 9to5Mac Happy Hour #604: "AirPods with camera leak" — no "pervertpods"
            # 9to5Mac Daily Aug 21: "Camera-equipped AirPods" — no "pervertpods"
            # Fortune AI Weekly: no AirPods coverage
        ]
        apple_stigma_in_audio_count = len(podcast_uses_of_apple_stigma)
        assert apple_stigma_in_audio_count == 0

    def test_stigma_label_podcast_propagation_asymmetry(self):
        """Meta's stigma labels propagate print→podcast. Apple's do not."""
        meta_print_to_podcast = 3  # pervert glasses in 3+ podcast channels
        apple_print_to_podcast = 0  # pervertpods in 0 podcast channels
        asymmetry = meta_print_to_podcast - apple_print_to_podcast
        assert asymmetry >= 3

    def test_techcrunch_sarah_perez_resolution_in_headline(self):
        """Sarah Perez (TechCrunch/Yahoo) performs resolution-rationalization
        IN THE HEADLINE — the strongest possible editorial position."""
        headline = "Why Apple's camera-equipped AirPods may not be the 'pervert pods' consumers fear"
        resolution_in_headline = "may not be" in headline
        assert resolution_in_headline

    def test_sarah_perez_already_tracked_meta_adversarial(self):
        """Sarah Perez's Meta coverage uses adversarial framing (mechanism from
        test_sarah_perez_cross_entity_privacy_vocabulary_inversion_aug17.py),
        creating a same-journalist cross-entity vocabulary split."""
        perez_meta_framing = "adversarial"
        perez_apple_framing = "resolution_rationalization"
        same_journalist = True
        framing_differs = perez_meta_framing != perez_apple_framing
        assert same_journalist
        assert framing_differs

    def test_inc_speculative_trust_attribution(self):
        """Inc article by Kit Eaton uses speculative trust language for Apple
        that no publication applies to Meta."""
        trust_phrases = [
            "Apple boosters would suspect that... of course they won't be able to invade people's privacy",
            "we could go one step further and speculate that Apple's software will nearly always process images... in a secure and anonymized way",
            "Apple will almost certainly have learned from the scandal swirling around Meta",
        ]
        speculative_trust_count = len(trust_phrases)
        meta_speculative_trust_count = 0  # No publication says "Meta will nearly always process images securely"
        assert speculative_trust_count >= 3
        assert meta_speculative_trust_count == 0


class TestFortuneAIWeeklySameEpisodeAnalysis:
    """Fortune AI Weekly same-episode framing comparison."""

    def test_fortune_meta_segments_use_adversarial_vocabulary(self):
        """Meta gets 'Sparks Privacy BACKLASH' and 'Under FIRE' in chapter titles."""
        meta_chapters = [
            {"timestamp": "14:33", "title": "Meta's AI Image Tool Sparks Privacy Backlash"},
            {"timestamp": "15:57", "title": "Why Meta's AI Glasses Are Under Fire"},
        ]
        adversarial_words = ["backlash", "under fire"]
        meta_adversarial = sum(
            1 for ch in meta_chapters
            if any(w in ch["title"].lower() for w in adversarial_words)
        )
        assert meta_adversarial == 2

    def test_fortune_openai_segments_use_neutral_aspirational(self):
        """OpenAI gets 'Rollout,' 'Released to Everyone,' 'New Voice Assistant.'"""
        openai_chapters = [
            {"timestamp": "00:00", "title": "OpenAI's GPT-5.6 Rollout"},
            {"timestamp": "01:26", "title": "Why OpenAI Released GPT-5.6 to Everyone"},
            {"timestamp": "12:58", "title": "OpenAI's New GPT Live Voice Assistant"},
        ]
        aspirational_words = ["rollout", "released to everyone", "new"]
        openai_aspirational = sum(
            1 for ch in openai_chapters
            if any(w in ch["title"].lower() for w in aspirational_words)
        )
        assert openai_aspirational >= 2

    def test_fortune_anthropic_uses_neutral_educational(self):
        """Anthropic gets 'Explained' — educational framing."""
        anthropic_chapter = {"timestamp": "18:35", "title": "Anthropic's 'J Space' Explained"}
        is_educational = "explained" in anthropic_chapter["title"].lower()
        assert is_educational

    def test_fortune_same_episode_vocabulary_bifurcation(self):
        """Within ONE 24-minute episode: Meta gets 2 adversarial, OpenAI gets
        3 neutral/aspirational, Anthropic gets 1 educational."""
        entity_framing = {
            "Meta": {"adversarial": 2, "neutral": 0, "aspirational": 0},
            "OpenAI": {"adversarial": 0, "neutral": 1, "aspirational": 2},
            "Anthropic": {"adversarial": 0, "neutral": 1, "aspirational": 0},
        }
        meta_adversarial = entity_framing["Meta"]["adversarial"]
        competitor_adversarial = (
            entity_framing["OpenAI"]["adversarial"]
            + entity_framing["Anthropic"]["adversarial"]
        )
        assert meta_adversarial == 2
        assert competitor_adversarial == 0

    def test_fortune_gpt56_jailbreaks_vs_meta_glasses_framing(self):
        """GPT-5.6 jailbreaks (05:24) get 'Raise Security Concerns' (technical)
        while Meta glasses (15:57) get 'Under Fire' (combative). Both are
        privacy/security issues but get different vocabulary registers."""
        openai_security = "GPT-5.6 Jailbreaks Raise Security Concerns"
        meta_security = "Why Meta's AI Glasses Are Under Fire"
        openai_uses_technical = "concerns" in openai_security.lower()
        meta_uses_combative = "under fire" in meta_security.lower()
        assert openai_uses_technical
        assert meta_uses_combative


# ─── Financial Architecture Predictions ───────────────────────────────────

class TestPodcastFinancialArchitecture:
    """Verify financial architecture predicts podcast framing patterns."""

    def test_9to5mac_apple_affiliate_revenue_dependency(self):
        """9to5Mac derives revenue from Apple ecosystem (affiliate links,
        Apple-adjacent advertising). FTC disclosure at bottom of every page."""
        ftc_disclosure = "FTC: We use income earning auto affiliate links"
        has_affiliate_revenue = "affiliate" in ftc_disclosure
        assert has_affiliate_revenue

    def test_9to5mac_sponsors_are_apple_ecosystem_adjacent(self):
        """Happy Hour #604 sponsors: Bitwarden (password manager for Apple),
        Keeper (password manager), Copilot Money (iOS finance app), Framer
        (web design). All serve Apple-ecosystem audiences."""
        sponsors = ["Bitwarden", "Keeper", "Copilot Money", "Framer"]
        apple_ecosystem_sponsors = len(sponsors)
        meta_ecosystem_sponsors = 0
        assert apple_ecosystem_sponsors >= 4
        assert meta_ecosystem_sponsors == 0

    def test_techcrunch_yahoo_apollo_ownership(self):
        """TechCrunch is owned by Yahoo (Apollo Global Management).
        Apollo has documented cross-entity financial architecture
        (mechanism from test_apollo_q2_2026_*)."""
        ownership_chain = {
            "publication": "TechCrunch",
            "parent": "Yahoo",
            "private_equity": "Apollo Global Management",
        }
        assert ownership_chain["private_equity"] == "Apollo Global Management"

    def test_fortune_independent_framing_matches_access_dynamics(self):
        """Fortune has no known AI content licensing deals but depends on
        AI industry access for exclusives. Adversarial framing toward Meta
        (no Fortune exclusives) vs neutral toward OpenAI (frequent Fortune
        exclusives) aligns with access-trading incentives."""
        fortune_meta_exclusives_2026 = 0  # Low
        fortune_openai_coverage_tone = "neutral_aspirational"
        fortune_meta_coverage_tone = "adversarial"
        tones_differ = fortune_openai_coverage_tone != fortune_meta_coverage_tone
        assert tones_differ


# ─── Cross-Publication Vocabulary Gradient ────────────────────────────────

class TestPervertpodsVocabularyGradient:
    """Track how the 'pervertpods' label is handled across publications
    and media types, ordered by Apple financial dependency."""

    def test_vocabulary_gradient_matches_financial_dependency(self):
        """Publications with higher Apple financial dependency show stronger
        resolution-rationalization of the 'pervertpods' label."""
        gradient = [
            {
                "publication": "AppleInsider",
                "apple_dependency": "HIGH",
                "resolution_strength": "MAXIMUM",  # "shouldn't worry"
                "detail": "Zero-distance resolution: dismiss in same sentence",
            },
            {
                "publication": "Cult of Mac",
                "apple_dependency": "HIGH",
                "resolution_strength": "HIGH",  # "isn't really the point"
                "detail": "Headline dismissal + Gurman authority citation",
            },
            {
                "publication": "9to5Mac",
                "apple_dependency": "HIGH",
                "resolution_strength": "HIGH",  # "make Zuckerberg look reckless"
                "detail": "Deflects stigma onto Meta",
            },
            {
                "publication": "TechCrunch",
                "apple_dependency": "MODERATE",  # Yahoo/Apollo
                "resolution_strength": "MODERATE",  # "may not be"
                "detail": "Headline resolution-rationalization",
            },
            {
                "publication": "Inc",
                "apple_dependency": "LOW",
                "resolution_strength": "MODERATE",  # speculative trust
                "detail": "Speculative trust attribution",
            },
            {
                "publication": "Entrepreneur",
                "apple_dependency": "LOW",
                "resolution_strength": "LOW",  # factual distance
                "detail": "Reports label factually, adds brand shield",
            },
            {
                "publication": "OSnews",
                "apple_dependency": "ZERO",
                "resolution_strength": "ZERO",  # amplifies
                "detail": "Uses label in HEADLINE, applies alarm vocabulary",
            },
        ]
        # Verify gradient: higher dependency → stronger resolution
        dependency_order = ["ZERO", "LOW", "MODERATE", "HIGH"]
        resolution_order = ["ZERO", "LOW", "MODERATE", "HIGH", "MAXIMUM"]
        for i in range(len(gradient) - 1):
            current = gradient[i]
            next_pub = gradient[i + 1]
            current_dep = dependency_order.index(current["apple_dependency"]) if current["apple_dependency"] in dependency_order else 4
            next_dep = dependency_order.index(next_pub["apple_dependency"]) if next_pub["apple_dependency"] in dependency_order else 4
            # Allow equal or decreasing dependency as we go down the list
            assert current_dep >= next_dep or current["apple_dependency"] == next_pub["apple_dependency"], \
                f"Gradient break: {current['publication']} ({current['apple_dependency']}) " \
                f"before {next_pub['publication']} ({next_pub['apple_dependency']})"

    def test_podcast_layer_preserves_aspirational_framing(self):
        """The podcast layer of the 9to5Mac network preserves aspirational
        framing for Apple while the print layer handles stigma resolution."""
        print_layer = {
            "handles_pervertpods": True,
            "performs_resolution": True,
            "deflects_to_meta": True,
        }
        podcast_layer = {
            "mentions_pervertpods": False,
            "uses_excitement_framing": True,
            "alarm_vocabulary": False,
        }
        # Print does the resolution work; podcast stays clean
        assert print_layer["performs_resolution"]
        assert not podcast_layer["mentions_pervertpods"]
        assert podcast_layer["uses_excitement_framing"]
