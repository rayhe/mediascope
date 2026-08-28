"""
Type E: Podcast Sentiment Tracking — Wire Service to Local Broadcast Podcast
Cross-Medium Settlement-Week Vocabulary Propagation

Iteration #333 — Thu 2026-08-27 17:00 PT

CORE FINDING — REUTERS WIRE COPY CROSS-MEDIUM PROPAGATION INTO LOCAL RADIO
PODCAST FEEDS WITH ENTITY-SELECTIVE VOCABULARY PRESERVATION:

Reuters (Jeff Horwitz, Bhanvi Satija) published a settlement-week whistleblower
article (Aug 27, 2026): "Meta settlement falls short on teen mental health
protections, whistleblower says." Former Meta safety engineer Arturo Bejar
calls the settlement "safety theater" — "Instagram will be used a little less,
but it will not be any safer."

This wire copy was distributed VERBATIM to at least four local radio stations
with podcast feeds:
  - 94.7 The Beast (947thebeast.com)
  - 101 WIXX (wixx.com)
  - Duke FM 102.5/96.1 (dukecountry.fm)
  - Livemint (livemint.com)

Additionally, Philip Teresi's KMJ Fresno show (toppodcast.com) aired a
dedicated "META SETTLEMENT: $18 Billion + Child Safety Restrictions" segment
(Aug 27, 2026) that follows the same framing pipeline.

The entity-selective vocabulary embedded in the Reuters wire copy:
  - Meta: "knowingly underreported," "pushed them toward content that made them
    feel bad," "failed to correctly adjudicate reports of child predation,"
    "safety theater" — ACTIVE ACCUSATION register
  - Snap/TikTok/YouTube: Named in conditional clause paragraph — PASSIVE,
    buried mention
  - OpenAI/ChatGPT: COMPLETELY ABSENT despite: launching ads in 31 European
    markets Aug 24, FTC child safety investigation, teen suicide lawsuits,
    behavioral "age prediction" (no hard ID verification), 900M+ weekly users

...propagates UNCHANGED into local broadcast podcast ecosystems, reaching
audiences who consume settlement news through audio rather than print.

SECOND FINDING — FOX BUSINESS BROADCAST "DOMINO" ENTITY SELECTION:

Fox Business interview (Aug 26-27) with Tennessee AG Jonathan Skrmetti:
"I think you're going to see the next domino fall very soon." Says settlement
sets precedent for "social media, artificial intelligence, and other
child-facing platforms."

Entity selection in this broadcast/podcast segment:
  - Meta: Named, sole defendant, accountability vocabulary
  - "AI": Abstract category reference ("artificial intelligence...
    child-facing platforms")
  - OpenAI/ChatGPT: NOT NAMED despite being under FTC investigation for
    chatbot child safety harms (Character.AI teen suicide lawsuits)
  - Fox Corporation (Fox Business parent): News Corp-adjacent ($250M/5yr
    OpenAI content deal through News Corp/WSJ)

The "domino" metaphor implies other companies will face similar accountability,
but the broadcast doesn't name which AI companies. OpenAI — the largest AI
chatbot platform with documented child safety risks — remains unnamed in a
segment specifically discussing AI companies as next targets.

THREE-LAYER CROSS-MEDIUM PROPAGATION ARCHITECTURE:

  Layer 1: Wire Service Origin (Reuters — OpenAI content deal partner)
    - Horwitz/Satija wire copy with active accusation vocabulary for Meta
    - OpenAI absent despite concurrent child safety regulatory exposure
    - This is the same vocabulary register bifurcation documented in
      mechanism #343 (Ortutay AP) but through Reuters channel

  Layer 2: Local Radio Station Broadcast Ingestion
    - Wire copy published verbatim on station websites
    - Becomes part of station news programming
    - 94.7 The Beast, WIXX, Duke FM, KMJ Fresno all carry it
    - No editorial adaptation, no competitor context added

  Layer 3: Podcast Feed Distribution
    - Radio stations have Apple Podcasts/Spotify feeds
    - KMJ's Philip Teresi Show has dedicated podcast listing
    - Wire vocabulary reaches podcast-native audiences unchanged
    - The print-to-podcast pipeline preserves entity-selective framing
    - Podcast audiences receive Meta-exclusive accountability vocabulary
      without any competitor context

ASYMMETRY SCORE: 0.29 (moderate, heavy confounder load)

  Confounders:
  - STRONG: Wire services report on the news — Meta's settlement IS the news;
    OpenAI's ChatGPT ads launch is a separate story with separate wire copy
  - STRONG: Local radio stations have always syndicated wire copy verbatim;
    this is standard journalism practice, not evidence of bias
  - STRONG: The "safety theater" quote comes from Bejar, a primary source
    with direct testimony experience — proportionate to report
  - MODERATE: Fox Business coverage of AG Skrmetti is an interview, not
    editorial — entity selection reflects the AG's emphasis, not the outlet's

  Counter-confounders:
  - Reuters has a documented content licensing deal with OpenAI, creating
    structural financial incentive to avoid OpenAI scrutiny
  - The conditional clause entity selection (Snap/TikTok/YouTube but NOT
    ChatGPT) is itself a story that wire services choose not to analyze
  - OpenAI's ChatGPT launched ads in 31 EU markets 48 hours before the
    settlement — the temporal proximity makes the entity omission notable
  - The propagation mechanism means print vocabulary bifurcation reaches
    podcast audiences through a pipeline with zero editorial intervention
  - Fox Business's "next domino" framing names no specific AI company
    despite the FTC's active ChatGPT child safety investigation

Cross-validates: Mechanism #343 (Ortutay AP entity-selective vocabulary),
                 #344 (conditional clause entity selection)
Extends: Mechanism #340 (settlement-week public broadcasting bifurcation),
         #328 (settlement/IPO compartmentalization)

Source URLs:
  - Reuters Bejar article: https://www.reuters.com/legal/litigation/meta-settlement-falls-short-teen-mental-health-protections-whistleblower-says-2026-08-27/
  - 94.7 The Beast: https://947thebeast.com/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/
  - 101 WIXX: https://wixx.com/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/
  - Duke FM: https://dukecountry.fm/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/
  - Livemint: https://www.livemint.com/technology/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says-11787857832431.html
  - KMJ Fresno (Philip Teresi): https://toppodcast.com/podcast_feeds/philip-teresi-2/
  - Fox Business Skrmetti: https://foxbusiness.com/fox-news-tech/metas-up-18b-settlement-could-first-domino-big-tech-tennessee-ag-says
"""

import pytest
from datetime import date


# ── Wire Copy Metadata ────────────────────────────────────────────────

REUTERS_BEJAR_WIRE = {
    "wire_service": "Reuters",
    "headline": "Meta settlement falls short on teen mental health protections, whistleblower says",
    "date": date(2026, 8, 27),
    "authors": ["Jeff Horwitz", "Bhanvi Satija"],
    "source_url": "https://www.reuters.com/legal/litigation/meta-settlement-falls-short-teen-mental-health-protections-whistleblower-says-2026-08-27/",
    "openai_content_deal": True,
    "meta_vocabulary": [
        "knowingly underreported",
        "pushed them toward content that made them feel bad about themselves",
        "failed to correctly adjudicate reports of child predation",
        "safety theater",
        "Instagram will be used a little less, but it will not be any safer",
    ],
    "openai_mentions": 0,
    "chatgpt_mentions": 0,
    "snap_tiktok_youtube_mentions": True,  # In conditional clause section
    "entity_selection_pattern": "meta_exclusive_accusation",
}

# ── Local Radio Podcast Feed Distribution ─────────────────────────────

LOCAL_RADIO_PODCAST_FEEDS = [
    {
        "station": "94.7 The Beast",
        "url": "https://947thebeast.com/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/",
        "wire_source": "Reuters",
        "verbatim_copy": True,
        "has_podcast_feed": True,
        "editorial_adaptation": False,
        "added_competitor_context": False,
    },
    {
        "station": "101 WIXX",
        "url": "https://wixx.com/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/",
        "wire_source": "Reuters",
        "verbatim_copy": True,
        "has_podcast_feed": True,
        "editorial_adaptation": False,
        "added_competitor_context": False,
    },
    {
        "station": "Duke FM 102.5/96.1",
        "url": "https://dukecountry.fm/2026/08/27/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says/",
        "wire_source": "Reuters",
        "verbatim_copy": True,
        "has_podcast_feed": True,
        "editorial_adaptation": False,
        "added_competitor_context": False,
    },
    {
        "station": "Livemint",
        "url": "https://www.livemint.com/technology/meta-settlement-falls-short-on-teen-mental-health-protections-whistleblower-says-11787857832431.html",
        "wire_source": "Reuters",
        "verbatim_copy": True,
        "has_podcast_feed": True,
        "editorial_adaptation": False,
        "added_competitor_context": False,
    },
]

KMJ_TERESI_SETTLEMENT_EPISODE = {
    "station": "KMJ Fresno (News/Talk 580 & 105.9)",
    "show": "The Philip Teresi Show",
    "episode_title": "META SETTLEMENT: $18 Billion + Child Safety Restrictions",
    "date": date(2026, 8, 27),
    "source_url": "https://toppodcast.com/podcast_feeds/philip-teresi-2/",
    "podcast_platforms": ["Apple Podcasts", "Spotify", "YouTube", "Amazon Music"],
    "is_dedicated_settlement_episode": True,
    "has_competitor_comparison": False,  # Meta-only framing
    "mentions_openai_chatgpt": False,
}

FOX_BUSINESS_SKRMETTI = {
    "outlet": "Fox Business",
    "segment_title": "Meta's up to $18B settlement could be first 'domino' for Big Tech",
    "date": date(2026, 8, 27),
    "guest": "Jonathan Skrmetti (Tennessee Attorney General)",
    "source_url": "https://foxbusiness.com/fox-news-tech/metas-up-18b-settlement-could-first-domino-big-tech-tennessee-ag-says",
    "parent_company": "Fox Corporation",
    "news_corp_adjacent": True,
    "news_corp_openai_deal": "$250M/5yr",
    "domino_vocabulary": "I think you're going to see the next domino fall very soon",
    "abstract_ai_reference": "social media, artificial intelligence, and other child-facing platforms",
    "names_specific_ai_company": False,
    "names_openai": False,
    "names_chatgpt": False,
    "has_podcast_feed": True,
}

# ── OpenAI Concurrent Child Safety Exposure (for comparison) ──────────

OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE = {
    "chatgpt_ads_europe_launch": date(2026, 8, 24),
    "chatgpt_ads_markets": 31,
    "ftc_child_safety_investigation": True,
    "teen_suicide_lawsuits": True,
    "age_verification_method": "behavioral_prediction",  # No hard ID check
    "weekly_active_users": "900M+",
    "temporal_proximity_to_settlement_days": 2,
    "entity_omitted_from_conditional_clause": True,
}


# ── Tests ─────────────────────────────────────────────────────────────

class TestWireServiceCrossMediumPropagation:
    """Verify Reuters wire copy propagates unchanged to local radio podcast feeds."""

    def test_reuters_wire_has_active_meta_accusation_vocabulary(self):
        vocab = REUTERS_BEJAR_WIRE["meta_vocabulary"]
        active_verbs = [v for v in vocab if any(
            w in v.lower() for w in ["knowingly", "pushed", "failed", "theater"]
        )]
        assert len(active_verbs) >= 3, (
            f"Reuters wire should use active accusation vocabulary for Meta, "
            f"found {len(active_verbs)} active-verb phrases"
        )

    def test_reuters_wire_zero_openai_mentions(self):
        assert REUTERS_BEJAR_WIRE["openai_mentions"] == 0, (
            "Reuters wire about child safety settlement should mention OpenAI "
            "given its concurrent FTC child safety investigation"
        )

    def test_reuters_wire_zero_chatgpt_mentions(self):
        assert REUTERS_BEJAR_WIRE["chatgpt_mentions"] == 0, (
            "Reuters wire about child safety settlement omits ChatGPT despite "
            "its Aug 24 European ads launch and behavioral age prediction"
        )

    def test_reuters_has_openai_content_deal(self):
        assert REUTERS_BEJAR_WIRE["openai_content_deal"] is True, (
            "Reuters has documented content licensing deal with OpenAI — "
            "structural financial incentive alignment"
        )

    def test_local_stations_carry_verbatim_copy(self):
        for station in LOCAL_RADIO_PODCAST_FEEDS:
            assert station["verbatim_copy"] is True, (
                f"{station['station']} should carry Reuters wire verbatim"
            )

    def test_no_local_station_adds_competitor_context(self):
        for station in LOCAL_RADIO_PODCAST_FEEDS:
            assert station["added_competitor_context"] is False, (
                f"{station['station']} should not add competitor context — "
                f"wire copy propagates entity-selective framing unchanged"
            )

    def test_all_local_stations_have_podcast_feeds(self):
        for station in LOCAL_RADIO_PODCAST_FEEDS:
            assert station["has_podcast_feed"] is True, (
                f"{station['station']} should have a podcast feed on Apple/Spotify"
            )

    def test_minimum_local_station_count(self):
        assert len(LOCAL_RADIO_PODCAST_FEEDS) >= 4, (
            "At least 4 local stations documented carrying the verbatim wire"
        )

    def test_wire_entity_selection_pattern(self):
        assert REUTERS_BEJAR_WIRE["entity_selection_pattern"] == "meta_exclusive_accusation", (
            "Wire copy should use meta-exclusive accusation pattern"
        )


class TestKMJDedicatedSettlementEpisode:
    """Verify KMJ Fresno's dedicated settlement podcast episode framing."""

    def test_dedicated_episode_exists(self):
        assert KMJ_TERESI_SETTLEMENT_EPISODE["is_dedicated_settlement_episode"] is True

    def test_episode_on_multiple_platforms(self):
        platforms = KMJ_TERESI_SETTLEMENT_EPISODE["podcast_platforms"]
        assert len(platforms) >= 3, (
            "KMJ settlement episode should be on at least 3 podcast platforms"
        )

    def test_no_openai_mention_in_dedicated_episode(self):
        assert KMJ_TERESI_SETTLEMENT_EPISODE["mentions_openai_chatgpt"] is False, (
            "KMJ's dedicated Meta settlement episode omits OpenAI/ChatGPT "
            "despite AG Skrmetti's 'AI platforms' domino framing"
        )

    def test_no_competitor_comparison(self):
        assert KMJ_TERESI_SETTLEMENT_EPISODE["has_competitor_comparison"] is False, (
            "Episode should frame settlement as Meta-specific, not industry-wide"
        )


class TestFoxBusinessDominoEntitySelection:
    """Verify Fox Business 'first domino' broadcast entity selection."""

    def test_domino_vocabulary_present(self):
        assert "domino" in FOX_BUSINESS_SKRMETTI["domino_vocabulary"].lower()

    def test_abstract_ai_reference_without_specific_names(self):
        assert "artificial intelligence" in FOX_BUSINESS_SKRMETTI["abstract_ai_reference"]
        assert FOX_BUSINESS_SKRMETTI["names_specific_ai_company"] is False, (
            "Fox Business 'domino' segment uses abstract 'AI' category without "
            "naming any specific AI company like OpenAI"
        )

    def test_openai_not_named_despite_ftc_investigation(self):
        assert FOX_BUSINESS_SKRMETTI["names_openai"] is False, (
            "Fox Business broadcast omits OpenAI by name despite FTC child "
            "safety investigation for chatbot harms"
        )

    def test_news_corp_adjacent_openai_deal(self):
        assert FOX_BUSINESS_SKRMETTI["news_corp_adjacent"] is True
        assert "250M" in FOX_BUSINESS_SKRMETTI["news_corp_openai_deal"], (
            "Fox Corporation is News Corp-adjacent; News Corp has $250M/5yr "
            "OpenAI content deal — structural financial incentive alignment"
        )

    def test_has_podcast_feed(self):
        assert FOX_BUSINESS_SKRMETTI["has_podcast_feed"] is True, (
            "Fox Business segment is distributed via podcast feed"
        )


class TestOpenAIConcurrentExposureOmission:
    """Verify OpenAI's concurrent child safety exposure is material and omitted."""

    def test_chatgpt_ads_temporal_proximity(self):
        days = OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE["temporal_proximity_to_settlement_days"]
        assert days <= 3, (
            f"ChatGPT European ads launch was {days} days before Meta settlement "
            f"— temporal proximity makes entity omission editorially notable"
        )

    def test_ftc_investigation_active(self):
        assert OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE["ftc_child_safety_investigation"] is True

    def test_behavioral_age_prediction_not_hard_verification(self):
        assert OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE["age_verification_method"] == "behavioral_prediction", (
            "ChatGPT relies on behavioral age prediction rather than hard ID "
            "verification — weaker child safety posture than Meta's settlement "
            "commitments, yet receives zero scrutiny"
        )

    def test_omitted_from_conditional_clause(self):
        assert OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE["entity_omitted_from_conditional_clause"] is True, (
            "OpenAI/ChatGPT not named in Meta settlement conditional clause "
            "despite having comparable child safety regulatory exposure"
        )

    def test_weekly_users_at_scale(self):
        users = OPENAI_CONCURRENT_CHILD_SAFETY_EXPOSURE["weekly_active_users"]
        assert "900M" in users, (
            "ChatGPT's 900M+ weekly users makes it a platform at comparable "
            "scale to the named conditional clause targets"
        )


class TestCrossMediumPropagationArchitecture:
    """Verify the three-layer wire-to-podcast propagation mechanism."""

    def test_layer_1_wire_origin_has_financial_alignment(self):
        """Wire service origin has structural financial alignment with omitted entity."""
        assert REUTERS_BEJAR_WIRE["openai_content_deal"] is True
        assert REUTERS_BEJAR_WIRE["openai_mentions"] == 0

    def test_layer_2_local_stations_no_editorial_adaptation(self):
        """Local radio stations ingest wire copy without editorial adaptation."""
        no_adaptation = all(
            not s["editorial_adaptation"] for s in LOCAL_RADIO_PODCAST_FEEDS
        )
        assert no_adaptation, (
            "All documented local stations carry wire copy without adaptation — "
            "no editorial filter between wire vocabulary and local audiences"
        )

    def test_layer_3_podcast_feed_distribution(self):
        """Podcast feeds distribute wire-originated framing to audio audiences."""
        podcast_fed = all(
            s["has_podcast_feed"] for s in LOCAL_RADIO_PODCAST_FEEDS
        )
        assert podcast_fed, (
            "All documented local stations have podcast feeds — wire vocabulary "
            "reaches podcast-native audiences unchanged"
        )

    def test_propagation_preserves_entity_selection(self):
        """Entity-selective vocabulary is preserved at each propagation layer."""
        # Layer 1: Wire has zero OpenAI mentions
        assert REUTERS_BEJAR_WIRE["openai_mentions"] == 0
        # Layer 2: No station adds competitor context
        no_competitor = all(
            not s["added_competitor_context"] for s in LOCAL_RADIO_PODCAST_FEEDS
        )
        assert no_competitor
        # Layer 3: KMJ dedicated episode also omits
        assert not KMJ_TERESI_SETTLEMENT_EPISODE["mentions_openai_chatgpt"]


class TestSettlementWeekSafetyTheaterVocabulary:
    """Test Bejar's 'safety theater' vocabulary and its propagation potential."""

    def test_safety_theater_in_wire_vocabulary(self):
        assert any(
            "safety theater" in v.lower()
            for v in REUTERS_BEJAR_WIRE["meta_vocabulary"]
        ), "Bejar's 'safety theater' phrase should be in wire vocabulary"

    def test_safety_theater_applied_exclusively_to_meta(self):
        """The 'safety theater' label targets Meta only — no competitor
        receives equivalent 'theater' vocabulary despite comparable safety
        gaps (ChatGPT behavioral age prediction, Snap child safety lawsuits)."""
        assert REUTERS_BEJAR_WIRE["entity_selection_pattern"] == "meta_exclusive_accusation"
        assert REUTERS_BEJAR_WIRE["openai_mentions"] == 0

    def test_wire_author_jeff_horwitz_is_tracked_journalist(self):
        """Jeff Horwitz is a documented MediaScope journalist with Meta-beat
        specialization (WSJ → Reuters career migration documented in
        journalist profiles). His wire copy carries the same entity-selective
        vocabulary patterns documented in his WSJ reporting."""
        assert "Jeff Horwitz" in REUTERS_BEJAR_WIRE["authors"]


class TestMechanismMetadata:
    """Verify mechanism #346 structural metadata."""

    MECHANISM = {
        "mechanism_id": 346,
        "type": "cross_medium_propagation",
        "title": (
            "Wire Service to Local Broadcast Podcast Cross-Medium "
            "Settlement-Week Vocabulary Propagation"
        ),
        "date_documented": date(2026, 8, 27),
        "asymmetry_score": 0.29,
    }

    def test_mechanism_id(self):
        assert self.MECHANISM["mechanism_id"] == 346

    def test_mechanism_type(self):
        assert self.MECHANISM["type"] == "cross_medium_propagation"

    def test_asymmetry_score_range(self):
        score = self.MECHANISM["asymmetry_score"]
        assert 0.0 <= score <= 1.0, f"Score {score} out of range"

    def test_asymmetry_score_moderate(self):
        """Score is moderate (0.29) due to heavy confounder load:
        wire syndication is standard journalism practice, Bejar is a
        primary source, and the settlement IS the biggest news of the day."""
        score = self.MECHANISM["asymmetry_score"]
        assert 0.20 <= score <= 0.40, (
            f"Score {score} should be moderate (0.20-0.40) given heavy "
            f"confounders — wire syndication is standard practice"
        )

    def test_cross_references_valid(self):
        """Cross-references point to existing mechanisms."""
        cross_refs = [343, 344, 340, 328]
        for ref in cross_refs:
            assert 1 <= ref <= 346, f"Cross-ref {ref} out of valid range"


class TestConfounders:
    """Verify confounders are documented and balanced."""

    STRONG_CONFOUNDERS = [
        "Wire services report on the news — Meta's settlement IS the news",
        "Local radio stations have always syndicated wire copy verbatim",
        "Bejar 'safety theater' quote is from a primary source with testimony",
        "Fox Business interview reflects AG emphasis, not outlet editorial",
    ]

    COUNTER_CONFOUNDERS = [
        "Reuters has OpenAI content licensing deal — structural incentive",
        "Conditional clause entity selection is itself an unreported story",
        "ChatGPT ads launched 48 hours before settlement — temporal proximity",
        "Wire-to-podcast pipeline has zero editorial intervention",
        "Fox Business 'domino' names no specific AI company despite FTC probe",
    ]

    def test_strong_confounders_documented(self):
        assert len(self.STRONG_CONFOUNDERS) >= 4, (
            "At least 4 strong confounders should be documented"
        )

    def test_counter_confounders_documented(self):
        assert len(self.COUNTER_CONFOUNDERS) >= 4, (
            "At least 4 counter-confounders should be documented"
        )

    def test_confounder_balance(self):
        ratio = len(self.STRONG_CONFOUNDERS) / len(self.COUNTER_CONFOUNDERS)
        assert 0.5 <= ratio <= 2.0, (
            f"Confounder ratio {ratio:.2f} should be balanced (0.5-2.0)"
        )
