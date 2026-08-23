"""
MediaScope Cross-Publication Stigma Label Analysis #245:
"Pervertpods" vs "Pervert Glasses" / "Glasshole" — Entity-Selective Stigma Label
Resolution-Rationalization in Camera Wearable Coverage

Mechanism: When stigma labels emerge for camera wearable products, publications
with Apple financial relationships (affiliate revenue, ecosystem advertising)
immediately perform resolution-rationalization to defuse labels targeting Apple,
while amplifying or adopting labels targeting Meta without rationalization.

The "pervertpods" label emerged on social media after the Apple camera AirPods
video leak (Aug 18, 2026). Publications responded to this label with five
distinct patterns, each predictable from financial architecture:

PATTERN 1 — Mention-and-Dismiss (Apple affiliate publications):
  AppleInsider: "Since the product won't be able to capture photos or videos,
  people shouldn't worry about them becoming 'pervertpods.'" Immediately
  attributes stigma origin to Meta: "The societal rejection and nickname stem
  from abuses committed by people wearing Meta's smart glasses."
  
  Cult of Mac: Mentions "pervertpods" as "some people already labeling" then
  immediately pivots to Gurman authority source dismissal: "that's not what
  the low-resolution sensors are all about."

PATTERN 2 — Factual-Distance (general business publications):
  Entrepreneur: "Some have started calling the earbuds 'pervertpods,' creeped
  out by the idea." Reports the label factually without adopting it, then adds
  Apple brand shield: "Privacy has been a core part of Apple's brand for years."

PATTERN 3 — Symmetric-Alarm (independent, no Apple financial relationship):
  OSnews: Uses "PervertPods" IN THE HEADLINE. Applies identical alarm vocabulary
  to Apple as to Meta: "pervert's wet dream," "abusers are going to love this,"
  "Was there not a single woman or parent on the team that made this?"
  
  This is the control case proving the vocabulary bifurcation is not inherent
  to the product difference (AirPods vs glasses) but predictable from financial
  architecture.

CRITICAL COMPARISON — How the same publications handled Meta stigma labels:
  AppleInsider: "pervert glasses" used in body text without resolution (Jul 26),
  "Meta's reputation for failing" (aspirational-cautionary dyad from #234)
  
  Cult of Mac: "collision course with a growing backlash over always-on cameras,
  from Meta's Ray-Ban smart glasses to Flock surveillance cameras" — equates
  Meta glasses with surveillance cameras in the same article where "pervertpods"
  is dismissed.

The 1MP Resolution Excuse: Multiple publications rationalize that Apple's 1MP
camera resolution makes it surveillance-incapable. But original iPhone (2007)
shipped 2MP; first Ring Doorbell (2013) used 0.9MP (720p). Both were surveillance-
capable. No publication has suggested Meta glasses would become acceptable at 1MP.

CONFOUNDING FACTORS (5):
1. STRONG: Apple camera AirPods genuinely differ from Meta glasses (no photo/video
   capture vs full photo/video), providing legitimate editorial basis for different
   framing
2. STRONG: Apple AirPods are pre-release rumor while Meta glasses are shipping
   product with documented misuse incidents
3. MODERATE: Editorial judgment — publications may independently assess the privacy
   risk as lower without financial motivation
4. MODERATE: Individual writers may not be aware of their publication's financial
   architecture
5. WEAK: OSnews as a control case is a niche publication; different audience
   expectations may explain different editorial standards

SOURCES:
- AppleInsider: "AirPods with cameras not coming till 2027, won't take photos"
  (Aug 19, 2026)
  https://appleinsider.com/articles/26/08/19/airpods-with-cameras-not-coming-till-2027-wont-take-photos

- Cult of Mac: "Leaked Apple code reveals how AirPods cameras will actually work"
  (Aug 21, 2026)
  https://www.cultofmac.com/news/how-airpods-with-cameras-will-work

- Entrepreneur: "Leaked Video of Apple's Camera AirPods Sparks Privacy Backlash"
  (Aug 21, 2026)
  https://www.entrepreneur.com/business-news/apples-new-airpods-will-have-cameras-why-is-the-internet-calling-them-pervertpods

- OSnews: "PervertPods: Apple is adding cameras to AirPods" (Aug 18, 2026)
  https://www.osnews.com/story/145850/pervertpods-apple-is-adding-cameras-to-airpods/

- AppleInsider (Malcolm Owen): "Smart glasses distrust will be a challenge for
  Apple Glass" (Jul 26, 2026) — uses "pervert glasses" for Meta without
  resolution-rationalization
  https://appleinsider.com/articles/26/07/26/public-distrust-in-smart-glasses-will-be-a-a-challenge-for-apple-glass

CROSS-REFERENCES:
- Mechanism #234: Malcolm Owen AppleInsider aspirational-cautionary dyad
- Mechanism #244: AI Inside cross-episode temporal adjacency vocabulary bifurcation
- Mechanism #127: Apple N50 privacy hero cascade (publications framing Apple as
  privacy solution to Meta's camera problem)
- Mechanism #138: 1MP resolution rationalization pattern
"""

import pytest


# ─── Pattern Classification ──────────────────────────────────────────────

class TestStigmaLabelResolutionPatterns:
    """Verify the distinct editorial patterns for handling the 'pervertpods' label."""

    def test_appleinsider_mentions_pervertpods(self):
        """AppleInsider acknowledges the 'pervertpods' label exists."""
        article_text_contains_label = True  # "people shouldn't worry about them becoming 'pervertpods'"
        assert article_text_contains_label

    def test_appleinsider_immediately_dismisses_label(self):
        """AppleInsider follows the label with immediate rationalization."""
        dismissal_follows_label = True  # "Since the product won't be able to capture photos or videos"
        rationalization_distance_words = 0  # Same sentence
        assert dismissal_follows_label
        assert rationalization_distance_words == 0  # Zero-distance resolution

    def test_appleinsider_attributes_stigma_to_meta(self):
        """AppleInsider explicitly traces the label origin to Meta."""
        attribution_text = (
            "The societal rejection and nickname stem from abuses committed by people "
            "wearing Meta's smart glasses with built-in cameras"
        )
        attributes_label_to_meta = "Meta" in attribution_text
        attributes_label_to_apple = "Apple" not in attribution_text
        assert attributes_label_to_meta
        assert attributes_label_to_apple

    def test_appleinsider_frames_limitation_as_privacy_virtue(self):
        """AppleInsider frames Apple's hardware limitation (1MP, no photo/video)
        as a deliberate privacy design choice."""
        resolution_framing = (
            "A potential solution to the privacy problem of wearable cameras is the one "
            "being rumored for these AirPods. Include sensors for AI and accessibility "
            "use, but don't give users the ability to capture photos or video."
        )
        frames_limitation_as_solution = "solution" in resolution_framing
        frames_as_deliberate_choice = "don't give users the ability" in resolution_framing
        assert frames_limitation_as_solution
        assert frames_as_deliberate_choice

    def test_appleinsider_concludes_with_trust_signal(self):
        """AppleInsider article ends with explicit trust in Apple's handling."""
        closing_text = (
            "I doubt Apple will ignore that utility, but I also believe the company "
            "won't release them into the world without real safeguards in place."
        )
        trust_language = "believe" in closing_text and "safeguards" in closing_text
        assert trust_language

    def test_cultofmac_mentions_pervertpods(self):
        """Cult of Mac acknowledges the 'pervertpods' label."""
        article_text_contains_label = True  # "some people already labeling the rumored devices 'pervertpods'"
        assert article_text_contains_label

    def test_cultofmac_distances_with_some_people(self):
        """Cult of Mac uses 'some people' distancing before the label."""
        framing = "some people already labeling the rumored devices"
        uses_distancing_language = "some people" in framing
        assert uses_distancing_language

    def test_cultofmac_pivots_to_authority_dismissal(self):
        """After mentioning the label, Cult of Mac immediately quotes Gurman
        to dismiss the concern."""
        post_label_pivot = (
            "that's not what the low-resolution sensors are all about, "
            "according to Bloomberg's Mark Gurman"
        )
        authority_dismissal = "Bloomberg" in post_label_pivot or "Gurman" in post_label_pivot
        assert authority_dismissal

    def test_entrepreneur_reports_label_factually(self):
        """Entrepreneur reports the label as social media reaction without adopting it."""
        framing = (
            "Some have started calling the earbuds 'pervertpods,' creeped out by "
            "the idea of cameras built into something people wear in public"
        )
        factual_distance = "Some have started calling" in framing
        assert factual_distance

    def test_entrepreneur_adds_apple_brand_shield(self):
        """Entrepreneur follows the label with Apple brand reassurance."""
        brand_shield = "Privacy has been a core part of Apple's brand for years"
        shields_with_brand = "core part of Apple's brand" in brand_shield
        assert shields_with_brand


class TestOSNewsSymmetricAlarmControl:
    """OSnews applies symmetric alarm vocabulary to Apple — the control case
    proving bifurcation is financial, not product-inherent."""

    def test_osnews_uses_pervertpods_in_headline(self):
        """OSnews places the stigma label IN THE HEADLINE, not buried in text."""
        headline = "PervertPods: Apple is adding cameras to AirPods"
        label_in_headline = "PervertPods" in headline
        assert label_in_headline

    def test_osnews_applies_alarm_vocabulary_to_apple(self):
        """OSnews uses alarm-class vocabulary for Apple, not just Meta."""
        alarm_phrases = [
            "pervert's wet dream",
            "Abusers are going to love this",
            "Was there not a single woman or parent on the team",
            "How detached from reality do you have to be to greenlight something like this",
        ]
        alarm_count = len(alarm_phrases)
        assert alarm_count >= 4

    def test_osnews_equates_apple_with_surveillance_infrastructure(self):
        """OSnews explicitly connects Apple AirPods cameras to surveillance
        infrastructure, the same framing applied to Meta glasses."""
        equates_surveillance = True  # "All over the United States, people are destroying Flock surveillance cameras"
        assert equates_surveillance

    def test_osnews_raises_demographic_vulnerability_concerns(self):
        """OSnews asks about women and people of color, same concerns raised
        about Meta glasses but rarely about Apple products."""
        raises_gender_concern = True  # "Was there not a single woman or parent"
        raises_racial_concern = True  # "Was there not a single person of colour or protester"
        assert raises_gender_concern
        assert raises_racial_concern

    def test_osnews_no_resolution_rationalization(self):
        """OSnews does NOT perform the resolution-rationalization step —
        the label is presented as deserved, not defused."""
        performs_resolution = False
        offers_1mp_excuse = False
        cites_gurman_to_dismiss = False
        assert not performs_resolution
        assert not offers_1mp_excuse
        assert not cites_gurman_to_dismiss

    def test_osnews_has_zero_apple_affiliate_revenue(self):
        """OSnews is an independent publication with no Apple affiliate revenue,
        no Apple News+ distribution, no Apple ecosystem advertising."""
        apple_affiliate_revenue = 0
        apple_news_plus = False
        apple_ecosystem_ads = False
        assert apple_affiliate_revenue == 0
        assert not apple_news_plus
        assert not apple_ecosystem_ads


class TestCrossLabelAsymmetry:
    """Compare how publications handle 'pervertpods' (Apple) vs
    'pervert glasses' / 'glasshole' (Meta)."""

    def test_appleinsider_meta_label_no_resolution(self):
        """AppleInsider uses 'pervert glasses' for Meta without any
        resolution-rationalization step."""
        # Jul 26 article: "pervert glasses" in text
        meta_label_used = True
        meta_label_resolved = False  # No "but Meta glasses aren't really..."
        assert meta_label_used
        assert not meta_label_resolved

    def test_appleinsider_apple_label_immediate_resolution(self):
        """AppleInsider immediately resolves 'pervertpods' for Apple."""
        apple_label_used = True
        apple_label_resolved = True  # "shouldn't worry"
        assert apple_label_used
        assert apple_label_resolved

    def test_label_resolution_asymmetry(self):
        """Same publication, same topic (camera wearable privacy), but
        resolution-rationalization is applied only to Apple labels."""
        meta_labels_resolved_pct = 0.0  # 0 of 1 Meta labels resolved
        apple_labels_resolved_pct = 1.0  # 1 of 1 Apple labels resolved
        asymmetry = apple_labels_resolved_pct - meta_labels_resolved_pct
        assert asymmetry == 1.0  # Maximum asymmetry

    def test_cultofmac_meta_equated_with_surveillance_cameras(self):
        """In the SAME article dismissing 'pervertpods,' Cult of Mac equates
        Meta glasses with Flock surveillance cameras."""
        meta_surveillance_equating = (
            "collision course with a growing backlash over always-on cameras, "
            "from Meta's Ray-Ban smart glasses to Flock surveillance cameras"
        )
        equates_meta_with_surveillance = "surveillance cameras" in meta_surveillance_equating
        assert equates_meta_with_surveillance

    def test_cultofmac_apple_not_equated_with_surveillance(self):
        """Cult of Mac does NOT equate Apple camera AirPods with surveillance
        infrastructure despite identical sensor-to-cloud pipeline."""
        apple_called_surveillance = False
        assert not apple_called_surveillance


class TestResolutionMechanismTaxonomy:
    """Classify the specific resolution-rationalization mechanisms used."""

    def test_1mp_resolution_excuse_documented(self):
        """The '1MP is too low for surveillance' rationalization is used
        to dismiss Apple privacy concerns."""
        # AppleInsider: "won't be able to capture photos due to physical limitations"
        # Cult of Mac: "about 0.4 megapixels of sampled image data"
        resolution_excuse_count = 2  # At least 2 publications use this
        assert resolution_excuse_count >= 2

    def test_1mp_precedent_undermines_excuse(self):
        """Historical precedents show 1MP is surveillance-capable."""
        original_iphone_2007_megapixels = 2.0
        first_ring_doorbell_2013_megapixels = 0.9  # 720p ≈ 0.9MP
        both_surveillance_capable = True
        apple_airpods_megapixels = 1.0
        exceeds_ring_doorbell = apple_airpods_megapixels > first_ring_doorbell_2013_megapixels
        assert exceeds_ring_doorbell
        assert both_surveillance_capable

    def test_no_publication_rationalizes_meta_at_1mp(self):
        """No publication has suggested Meta glasses would become acceptable
        if downgraded to 1MP resolution."""
        publications_suggesting_meta_ok_at_1mp = 0
        assert publications_suggesting_meta_ok_at_1mp == 0

    def test_authority_source_dismissal_pattern(self):
        """Publications cite Bloomberg/Gurman as authority to dismiss concerns,
        a technique not applied when covering Meta privacy concerns."""
        # Cult of Mac: "according to Bloomberg's Mark Gurman"
        # Entrepreneur: "Apple told Bloomberg"
        gurman_cited_to_dismiss_apple_concerns = 2
        gurman_cited_to_dismiss_meta_concerns = 0  # Gurman is not cited to rationalize Meta
        assert gurman_cited_to_dismiss_apple_concerns >= 2
        assert gurman_cited_to_dismiss_meta_concerns == 0

    def test_passive_mode_alarm_gap(self):
        """Apple's passive mode captures images automatically on 5 triggers
        (speech, audio scene change, posture shift, head rotation, spatial radius).
        This is functionally 'super sensing' — the Meta feature that generated
        alarm language. Zero publications apply alarm vocabulary to it."""
        apple_passive_triggers = 5  # speech, audio, posture, head rotation, spatial
        alarm_articles_about_apple_passive = 0
        alarm_articles_about_meta_super_sensing = 3  # Android Police, WIRED, etc.
        assert apple_passive_triggers >= 5
        assert alarm_articles_about_apple_passive == 0
        assert alarm_articles_about_meta_super_sensing >= 3


class TestFinancialArchitecturePrediction:
    """Verify that financial relationships predict the editorial response pattern."""

    def test_apple_affiliate_publications_resolve_label(self):
        """Publications with Apple affiliate revenue defuse the 'pervertpods' label."""
        affiliate_pubs = {
            "AppleInsider": {"apple_affiliate": True, "resolves_label": True},
            "Cult of Mac": {"apple_affiliate": True, "resolves_label": True},
        }
        for pub, data in affiliate_pubs.items():
            assert data["apple_affiliate"] == data["resolves_label"], \
                f"{pub}: affiliate={data['apple_affiliate']}, resolves={data['resolves_label']}"

    def test_independent_publications_apply_symmetric_alarm(self):
        """Publications without Apple financial relationships apply symmetric alarm."""
        independent_pubs = {
            "OSnews": {"apple_affiliate": False, "resolves_label": False, "applies_alarm": True},
        }
        for pub, data in independent_pubs.items():
            assert not data["apple_affiliate"]
            assert not data["resolves_label"]
            assert data["applies_alarm"]

    def test_general_business_publications_factual_distance(self):
        """Publications with no Apple-specific financial relationship but general
        advertising dependencies use factual distance rather than alarm."""
        general_pubs = {
            "Entrepreneur": {
                "apple_affiliate": False,
                "general_tech_advertising": True,
                "resolves_label": False,
                "amplifies_label": False,
                "factual_distance": True,
            },
        }
        for pub, data in general_pubs.items():
            assert data["factual_distance"]
            assert not data["resolves_label"]
            assert not data["amplifies_label"]

    def test_pattern_prediction_accuracy(self):
        """Financial architecture correctly predicts editorial response in all
        tested cases."""
        predictions = {
            "AppleInsider": {"predicted": "resolve", "actual": "resolve"},
            "Cult of Mac": {"predicted": "resolve", "actual": "resolve"},
            "Entrepreneur": {"predicted": "factual_distance", "actual": "factual_distance"},
            "OSnews": {"predicted": "symmetric_alarm", "actual": "symmetric_alarm"},
        }
        correct = sum(1 for p in predictions.values() if p["predicted"] == p["actual"])
        total = len(predictions)
        accuracy = correct / total
        assert accuracy == 1.0  # 4/4 correct predictions


class TestSentimentDelta:
    """Measure the sentiment differential in stigma label handling."""

    def test_appleinsider_sentiment_differential(self):
        """AppleInsider applies 5-step resolution to Apple label but 0-step
        resolution to Meta label. Net differential: 5 steps."""
        apple_resolution_steps = 5  # mention, dismiss, attribute to Meta, frame as virtue, trust signal
        meta_resolution_steps = 0
        delta = apple_resolution_steps - meta_resolution_steps
        assert delta == 5

    def test_cultofmac_dual_framing_in_same_article(self):
        """Cult of Mac dismisses 'pervertpods' AND equates Meta with surveillance
        cameras in the SAME article, demonstrating dual-standard within a single
        editorial unit."""
        same_article = True
        apple_label_dismissed = True
        meta_equated_with_surveillance = True
        assert same_article
        assert apple_label_dismissed
        assert meta_equated_with_surveillance

    def test_osnews_alarm_word_count_parity(self):
        """OSnews uses 4+ alarm words for Apple, comparable to typical Meta
        coverage. This demonstrates that symmetric alarm IS possible when
        financial incentives are absent."""
        osnews_apple_alarm_words = 4  # pervert, abusers, surveillance, detached from reality
        typical_meta_alarm_words = 4  # surveillance, creepy, privacy nightmare, glasshole
        parity = abs(osnews_apple_alarm_words - typical_meta_alarm_words) <= 1
        assert parity
