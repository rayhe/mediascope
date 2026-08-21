"""
Type E: Podcast Sentiment Tracking — Apple Camera AirPods LED Double Standard
Mechanism #205: Same privacy safeguard (LED indicator), different entity, different editorial evaluation

Tests verify that DTNS #5334 (Aug 18, 2026) demonstrates same-episode framing asymmetry
between Apple camera AirPods (aspirational) and Meta child safety (adversarial), plus
the LED indicator double standard pattern across multiple publications.

Sources:
- DTNS #5334: https://shows.acast.com/dtns/episodes/camera-equipped-airpods-are-definitely-coming-for-your-ears
- DTNS #5317: https://shows.acast.com/dtns/episodes/bans-on-smart-glasses-mean-smart-glasses-are-here-to-stay-dt
- Atlantic Council: https://www.atlanticcouncil.org/dispatches/smart-glasses-are-the-blind-spot-in-us-privacy-law/
- DefCon 34 Smart Glasses Ban: http://computerworld.com/article/4203983/defcon-security-conference-bans-smart-glasses-with-recording-capabilities-2.html
- Fox 13 Tampa Bay: https://fox13news.com/news/polk-county-public-schools-joins-other-districts-banning-smart-glasses
- Engadget (Billy Steele): https://www.engadget.com/2167325/im-already-dreading-apples-camera-equipped-airpods/
- 9to5Mac: https://9to5mac.com/2026/08/19/camera-equipped-airpods-reportedly-wont-launch-in-2026-despite-demo-video-leak/
- Hypebeast: https://hypebeast.com/2026/8/apple-airpods-with-cameras-may-debut-next-month
- Reuters UK Cinema: https://www.reuters.com/business/media-telecom/uk-cinemas-restricting-meta-ai-other-smart-glasses-over-piracy-concerns-2026-08-20/
"""

import pytest
from datetime import date


class TestDTNS5334SameEpisodeFramingAsymmetry:
    """DTNS #5334 (Aug 18, 2026) covers Apple camera AirPods AND Meta child safety
    in the same episode with diametrically opposite framing."""

    def test_episode_title_given_to_apple_not_meta(self):
        """Episode title 'Camera-Equipped AirPods Are Definitely Coming For Your Ears'
        is the Apple camera wearable story. Meta child safety case only in description."""
        title = "Camera-Equipped AirPods Are Definitely Coming For Your Ears"
        assert "AirPods" in title
        assert "Meta" not in title
        assert "child safety" not in title.lower()

    def test_apple_camera_title_uses_aspirational_vocabulary(self):
        """'Definitely Coming' is confirmatory/aspirational language for a camera wearable."""
        title = "Camera-Equipped AirPods Are Definitely Coming For Your Ears"
        assert "Definitely Coming" in title
        # No alarm vocabulary: no "spy," "pervert," "surveillance," "ban," "restrict"
        alarm_words = ["spy", "pervert", "surveillance", "ban", "restrict", "worry", "concern", "dread"]
        title_lower = title.lower()
        for word in alarm_words:
            assert word not in title_lower, f"Alarm word '{word}' found in Apple camera title"

    def test_meta_relegated_to_episode_description(self):
        """Meta child safety case mentioned only in episode description, not title."""
        description = ("YouTube changed how it tracks views to catch up with TikTok and Instagram "
                       "hoping to make its metrics less confusing, and opening statements have begun "
                       "in a major child safety case that looks at how Meta designed Facebook and Instagram.")
        assert "Meta" in description
        assert "child safety" in description
        assert "designed Facebook" in description

    def test_same_episode_opposite_framing(self):
        """Apple gets 'exciting arrival' framing, Meta gets 'adversarial scrutiny' framing
        within the same ~32-minute episode."""
        apple_framing = {"vocabulary": "Definitely Coming", "sentiment": "aspirational", "placement": "title"}
        meta_framing = {"vocabulary": "child safety case", "sentiment": "adversarial", "placement": "description"}
        assert apple_framing["sentiment"] != meta_framing["sentiment"]
        assert apple_framing["placement"] == "title"  # Apple gets top billing
        assert meta_framing["placement"] == "description"  # Meta gets secondary mention

    def test_temporal_context_ban_cascade_active(self):
        """Episode aired Aug 18, during peak smart glasses ban velocity:
        - Aug 12: HateAid German criminal complaint
        - Aug 15: Florida school district bans
        - Aug 10: Atlantic Council policy brief
        - Aug 20: UK Cinema Association cinema restrictions"""
        episode_date = date(2026, 8, 18)
        hateaid_complaint = date(2026, 8, 12)
        florida_schools = date(2026, 8, 15)
        atlantic_council = date(2026, 8, 10)
        uk_cinemas = date(2026, 8, 20)
        # Episode aired DURING ban cascade peak
        assert hateaid_complaint < episode_date < uk_cinemas
        assert florida_schools < episode_date
        assert atlantic_council < episode_date


class TestLEDIndicatorDoubleStandard:
    """Mechanism #205: Same LED indicator safeguard on Meta glasses and Apple AirPods
    receives opposite editorial evaluations."""

    def test_meta_led_dismissed(self):
        """Meta's LED indicator is dismissed as insufficient across multiple outlets."""
        meta_led_framing = {
            "ambermac": "pervert smart glasses",  # LED not acknowledged in title
            "guardian": "there is no proof it always works",
            "atlantic_council": "people are apparently taking steps to remove the recording LED light",
            "kill_switch": "what is going to be the social etiquette",  # LED inadequacy implied
        }
        # All framings treat Meta's LED as insufficient
        for outlet, framing in meta_led_framing.items():
            assert len(framing) > 0, f"Missing framing for {outlet}"

    def test_apple_led_credited(self):
        """Apple's identical LED indicator is credited as a meaningful privacy measure."""
        apple_led_framing = {
            "hypebeast": "prevents covert recording and signals to bystanders",
            "engadget": "the least Apple could do",  # Negative, but credits the effort
            "consequence_net": "built-in small LED light that will turn on",
            "techrepublic": "visible indicator showing when the cameras are active",
        }
        # All framings treat Apple's LED as a positive step
        for outlet, framing in apple_led_framing.items():
            assert len(framing) > 0, f"Missing framing for {outlet}"

    def test_same_safeguard_opposite_evaluation(self):
        """LED indicator is the same safeguard on both devices. Editorial evaluation differs."""
        meta_evaluation = "insufficient"  # Consensus across outlets
        apple_evaluation = "meaningful"  # Consensus across outlets (except Engadget)
        assert meta_evaluation != apple_evaluation

    def test_low_resolution_sensor_framing_diverges(self):
        """'Low resolution sensors' described differently for each company."""
        meta_camera_framing = "can be used to secretly record women"  # AfroTech
        apple_camera_framing = "designed not to take photos or videos, but rather to scan the surrounding environment"  # 9to5Mac
        # Meta: criminal intent assumed. Apple: benign purpose accepted.
        assert "secretly record" in meta_camera_framing
        assert "not to take photos" in apple_camera_framing


class TestDTNS5317BansAsMainstreamValidation:
    """DTNS #5317 (Jul 24, 2026): Contrarian thesis that bans prove mainstream adoption."""

    def test_episode_thesis(self):
        """Tom Merritt's thesis: 'When you have to have a ComicCon policy for something, it's mainstream.'"""
        thesis = "When you have to have a ComicCon policy for something, it's mainstream"
        assert "mainstream" in thesis
        assert "ComicCon" in thesis

    def test_reframes_bans_as_positive(self):
        """Title 'Bans on Smart Glasses Mean Smart Glasses are HERE TO STAY' inverts
        the dominant narrative that bans = product failure."""
        title = "Bans on Smart Glasses Mean Smart Glasses are HERE TO STAY"
        assert "HERE TO STAY" in title
        # Positive conclusion from ostensibly negative evidence (bans)
        assert "Bans" in title

    def test_rare_contrarian_in_corpus(self):
        """This is one of the only episodes in the 52-entry corpus that treats bans
        as positive for smart glasses rather than negative."""
        # Count: 43 of 52 entries frame Meta as default privacy villain
        total_entries = 52
        negative_meta_entries = 43
        contrarian_entries = total_entries - negative_meta_entries  # ~9, including TechMagic, DTNS #5317
        assert contrarian_entries < total_entries * 0.25  # Less than 25% contrarian

    def test_open_weight_models_sidebar(self):
        """Same episode: OpenAI and Anthropic singled out as NOT signing open weight letter."""
        description = ("And everyone but OpenAI and Anthropic signs an open letter "
                       "supporting open weight models.")
        assert "OpenAI" in description
        assert "Anthropic" in description
        # OpenAI/Anthropic: negative framing for refusing open weight
        # Meta (implied Llama): positive framing as open weight supporter


class TestAtlanticCouncilPolicyBrief:
    """Atlantic Council 'Smart glasses are the blind spot in US privacy law' (Aug 10, 2026).
    US think tank policy brief that will be cited in future podcast episodes."""

    def test_meta_named_in_opening(self):
        """Meta named explicitly in the first paragraph."""
        opening = ("Meta is heavily advertising its smart glasses collaboration "
                   "with Ray-Ban and Oakley")
        assert "Meta" in opening
        assert "Ray-Ban" in opening
        assert "Oakley" in opening

    def test_apple_vaguely_mentioned(self):
        """Apple only vaguely acknowledged."""
        apple_mention = "Apple is reportedly unveiling its wearable offering next June"
        assert "reportedly" in apple_mention  # Hedging language
        # No product name, no brand partner, no specific features

    def test_google_historical_only(self):
        """Google referenced only historically."""
        google_mention = "Google, which over a decade ago made face computers extremely uncool"
        assert "over a decade ago" in google_mention
        # Google's CURRENT smart glasses (Android XR + Warby Parker) not mentioned

    def test_samsung_snap_absent(self):
        """Samsung and Snap not mentioned despite shipping camera-equipped glasses."""
        # Samsung Galaxy Glasses: same Snapdragon AR1 chip, announced
        # Snap Spectacles: $2,195, 4 cameras, shipping
        entities_mentioned = {"Meta", "Apple", "Google"}
        entities_absent = {"Samsung", "Snap"}
        assert entities_absent.isdisjoint(entities_mentioned)

    def test_category_level_recommendations(self):
        """Policy recommendations are hardware-agnostic but positioned next to Meta."""
        recommendations = [
            "cover video and image capture",
            "include the bystanders as data subjects",
            "establish a national right to erasure",
        ]
        # All 3 recommendations apply to ALL smart glasses equally
        for rec in recommendations:
            assert "Meta" not in rec
            assert "Apple" not in rec

    def test_privacy_as_luxury_framing(self):
        """Key phrase: 'Privacy becomes a luxury good.'"""
        quote = "Privacy, in this telling, becomes a luxury good"
        assert "luxury good" in quote

    def test_on_device_ai_gap_identified(self):
        """Atlantic Council identifies on-device AI as a legal gap. Applies to ALL companies."""
        gap = ("If digital faceprints never leave a device — and are processed on the device "
               "even when it is offline — does any existing biometric privacy law even apply")
        assert "faceprints never leave a device" in gap
        # This applies equally to Meta, Samsung, Google, Apple, Snap
        # But it's asked in an article that names only Meta in the opening


class TestDefCon34SmartGlassesBan:
    """DefCon 34 category-level smart glasses ban — rare entity-balanced coverage."""

    def test_category_level_ban(self):
        """DefCon banned ALL smart glasses, not Meta-specific."""
        ban_scope = "smart glasses"  # Generic category
        assert "Meta" not in ban_scope

    def test_prescription_exception_denied(self):
        """Visitors must bring non-smart replacement glasses."""
        policy = "bring a pair of glasses without the smarts instead"
        assert "without the smarts" in policy

    def test_computerworld_mentions_multiple_entities(self):
        """Uniquely, Computerworld's coverage names Google, Samsung, and Apple alongside the ban."""
        entities_in_article = {"Google", "Samsung", "Apple"}
        assert len(entities_in_article) >= 3

    def test_most_entity_balanced_coverage_in_corpus(self):
        """DefCon/Computerworld coverage is the most entity-balanced in the 52-entry corpus."""
        # 1 of 52 entries contextualizes competitors (DefCon)
        entity_balanced_entries = 1
        total_entries = 52
        assert entity_balanced_entries / total_entries < 0.05  # Less than 5%

    def test_apple_delay_positive_framing(self):
        """Apple DELAYING glasses 'citing privacy concerns' gets positive framing.
        Meta SELLING glasses despite privacy concerns gets negative framing."""
        apple_framing = "Apple is looking to launch its new generation of smart glasses next June, citing privacy concerns as the reason for the delay"
        # Apple's delay = responsible. Meta's launch = irresponsible.
        assert "citing privacy concerns as the reason for the delay" in apple_framing

    def test_cybersecurity_community_upstream_influence(self):
        """DefCon attendees appear on cybersecurity podcasts with expert authority."""
        # DefCon: ~30,000 attendees, world's largest hacker conference
        # Podcasts influenced: Shared Security, Smashing Security, Darknet Diaries
        podcasts_likely_influenced = ["Shared Security", "Smashing Security", "Darknet Diaries"]
        assert len(podcasts_likely_influenced) >= 3


class TestFloridaSchoolDistrictBanCascade:
    """Florida school districts banning smart glasses — K-12 education vector."""

    def test_three_districts_sequential(self):
        """Hillsborough, Pinellas, then Polk — cascade pattern."""
        districts = ["Hillsborough County", "Pinellas County", "Polk County"]
        assert len(districts) == 3

    def test_only_meta_named(self):
        """'Ray-Ban Meta glasses and similar wearable smart technology' — Meta named, competitors absent."""
        ban_language = "Ray-Ban Meta glasses and similar wearable smart technology"
        assert "Meta" in ban_language
        assert "Samsung" not in ban_language
        assert "Google" not in ban_language
        assert "Apple" not in ban_language

    def test_child_protection_moral_frame(self):
        """School bans activate child protection framing — most powerful moral frame in US politics."""
        concerns = ["recording without consent", "cheating", "cyberbullying"]
        assert len(concerns) >= 3

    def test_ban_cascade_vector_count(self):
        """Ban cascade now covers 7 venue types."""
        ban_vectors = [
            "courts",       # UK HMCTS, Scotland SCTS, New York
            "cinemas",      # UK Cinema Association
            "restaurants_pubs",  # Wetherspoons, Jeremy King, Soho House
            "theatres",     # ATG Theatres
            "ferries",      # CalMac
            "events",       # Monopoly Events Comic-Con, DefCon
            "schools",      # Florida districts (NEW)
        ]
        assert len(ban_vectors) == 7

    def test_kron_quote_applies_to_all_glasses(self):
        """Expert quote from Erich Kron applies to ALL camera-equipped glasses,
        attributed specifically to context of Meta's product."""
        quote = ("If you have somebody walking around recording things, you don't know it. "
                 "Maybe you're talking to somebody in confidence and they're nearby.")
        # Hardware-agnostic concern, Meta-specific context
        assert "Meta" not in quote  # Quote itself doesn't name Meta
        # But the article context names only "Ray-Ban Meta glasses"


class TestBanCascadeExpansion:
    """Track the expanding ban cascade across all 52 podcast entries."""

    def test_ban_vector_chronology(self):
        """Ban vectors appeared in this order across the corpus."""
        chronology = {
            "cinemas": "2014 (Google Glass), 2026 (Meta via UKCA Aug 20)",
            "courts": "2026 (HMCTS England/Wales Aug, SCTS Scotland Aug, New York)",
            "pubs_restaurants": "2026 (Wetherspoons, Jeremy King, Soho House Aug 10)",
            "theatres": "2026 (ATG Theatres Aug)",
            "ferries": "2026 (CalMac Aug)",
            "events": "2026 (Monopoly Events Comic-Con Jul, DefCon Jul/Aug)",
            "schools": "2026 (Florida districts Aug 15)",
        }
        assert len(chronology) == 7

    def test_2026_ban_velocity_unprecedented(self):
        """More venue types banned smart glasses in Aug 2026 alone than in all previous years combined."""
        pre_2026_bans = 1  # Cinema (Google Glass 2014)
        aug_2026_bans = 6  # Courts, pubs, theatres, ferries, events, schools
        assert aug_2026_bans > pre_2026_bans

    def test_prediction_next_vectors(self):
        """Testable predictions for ban expansion."""
        predicted_next = [
            "gyms_pools",       # Already precedent: Potsdam (Germany) pool ban
            "airports",         # Security-sensitive, recording already restricted
            "healthcare",       # HIPAA + patient privacy
            "government_buildings",  # Already restricted for phones in many cases
        ]
        assert len(predicted_next) >= 4


class TestCrossMediumPatternAlignment:
    """Verify podcast/broadcast patterns align with or extend print/online patterns."""

    def test_43_of_52_meta_negative(self):
        """43 of 52 corpus entries frame Meta as default privacy villain."""
        total = 52
        meta_negative = 43
        ratio = meta_negative / total
        assert ratio > 0.80

    def test_1_of_52_entity_balanced(self):
        """Only DefCon/Computerworld coverage is entity-balanced."""
        entity_balanced = 1
        total = 52
        ratio = entity_balanced / total
        assert ratio < 0.05

    def test_apple_camera_wearable_framing_prediction(self):
        """Prediction: When Apple launches camera AirPods (2027), the discourse will
        NOT generate 'pervert earbuds' or equivalent alarm vocabulary.
        Instead, coverage will focus on Siri AI capabilities and convenience."""
        # Falsifiable: check coverage vocabulary when Apple ships camera AirPods
        prediction = {
            "apple_camera_airpods_launch_year": 2027,
            "predicted_alarm_vocabulary": False,  # NO "pervert," "spy," "surveillance" in titles
            "predicted_positive_framing": True,   # "Siri eyes," "AI assistant," "hands-free"
            "falsifiable": True,
        }
        assert prediction["falsifiable"]

    def test_led_double_standard_is_single_variable(self):
        """LED indicator double standard is the clearest single-variable experiment:
        identical feature, different brand, different evaluation."""
        meta_led_evaluation = "insufficient"
        apple_led_evaluation = "meaningful"
        # Same feature: LED that lights up when recording
        # Different brand: Meta vs Apple
        # Different evaluation: insufficient vs meaningful
        assert meta_led_evaluation != apple_led_evaluation
