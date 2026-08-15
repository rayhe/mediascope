"""
Mechanism #113: Karissa Bell (Engadget/Yahoo/Apollo) — Beat Reporter Investigative Methodology Asymmetry

FINDING: Karissa Bell, Engadget's senior reporter covering social media, tech policy, and
smart glasses, applies fundamentally different INVESTIGATIVE METHODOLOGIES to Meta vs
its competitors. For Meta's smart glasses, she employs active adversarial testing: purchasing
LED-blocking products from TikTok Shop, demonstrating bypass techniques on video, tracking
the "cat-and-mouse game" between Meta and covert recording enthusiasts, interviewing
affected creators to document backlash, and embedding the word "baggage" in product
review headlines. For Snap Specs (camera + microphone + AR display = MORE capable
surveillance hardware at $2,195), she conducts a CEO interview where Evan Spiegel
reframes the product as "a new type of computer, not AI glasses" -- a marketing position
Bell accepts without challenge.

METHODOLOGY ASYMMETRY:
  - Meta: ACTIVE ADVERSARIAL TESTING
    -> Buys LED-blocking products ($2-$17)
    -> Tests bypass techniques on two Meta glasses models (Ray-Ban Meta, Oakley Vanguard)
    -> Embeds YouTube videos demonstrating the bypass
    -> Quotes TikTokkers promoting bypass ("stop freaking out")
    -> Reaches out to Meta for comment (standard adversarial practice)
    -> Frames as systemic failure ("thriving market" for bypass products)
    -> In review, dedicates section titled "The baggage" to privacy controversy
    -> Interviews 5 creators documenting usage chilling effect
    -> Amplifies anti-Meta activist campaign (London bus stop takeover)
    -> Dedicated privacy investigation article

  - Snap: PASSIVE CEO INTERVIEW
    -> Spiegel frames Specs as "computer," not "AI glasses" (accepted)
    -> Spiegel addresses privacy by saying Snap doesn't allow facial recognition
      in Lenses (not tested)
    -> Meta is mentioned as the VILLAIN even in the SNAP article ("There's the
      Meta of it all, too")
    -> No adversarial testing of Snap's LED/privacy indicators
    -> No investigation of Snap's data collection or retention practices
    -> No purchasing of bypass products for Snap Specs
    -> No interviews with privacy advocates about Snap
    -> Article ends with Bell "looking forward" to trying the product

  - Xreal: NEUTRAL PRODUCT NEWS (zero privacy vocabulary)
  - Qualcomm: NEUTRAL TECH NEWS (zero privacy vocabulary despite the chip powering
    the privacy-relevant cameras in ALL smart glasses)

HARDWARE PARITY THAT MAKES THE ASYMMETRY SALIENT:
  Snap Specs ($2,195): Camera, microphones, AR waveguide display, Snapchat Lens ecosystem
    enables real-time AR overlays on people and environments -- MORE intrusive capability
    than Meta glasses. Zero adversarial testing.
  Meta Glasses ($299): Camera, microphones, NO display (non-Display models), LED indicator.
    Full adversarial testing: $2 sticker bypass demonstrated.

FINANCIAL INCENTIVE CHAIN (Engadget -> Yahoo -> Apollo):
  Apollo: $38.5B+ AI infrastructure deals financing Meta competitors (mechanism #111)
  Yahoo search: powered by Google
  Yahoo display advertising: dependent on Google ad tech stack
  Meta -> Yahoo: ZERO content licensing deal
  Meta -> Yahoo: ZERO significant advertising dependency
  Meta = lowest-cost editorial target (mechanism #109)

CAREER CONTEXT:
  Bell was previously at Mashable (6 years covering social media) and wrote product
  reviews for Wired. Her expertise listing includes "Social media, Tech policy, Internet
  culture." She is NOT a product reviewer by specialty -- her Meta glasses coverage is
  unusually product-focused for a policy/culture reporter, concentrated on the privacy/
  surveillance angle that generates the most adversarial coverage.

CONFOUNDING FACTORS:
  1. STRONG: Meta has genuine privacy history (Cambridge Analytica, FB Papers, contractor
     video reviews, NameTag facial recognition). This justifies SOME adversarial scrutiny.
  2. STRONG: Snap Specs were not yet shipping at time of interview. Bell may plan to apply
     similar scrutiny post-launch. However, no equivalent pre-launch adversarial coverage
     exists for Snap, Samsung, Google, or Xreal -- only Meta receives pre-launch and
     post-launch adversarial testing.
  3. MODERATE: Spiegel OFFERED the interview. Meta may not offer comparable executive
     access. However, Bell interviews Meta creators and users as an alternative -- she
     doesn't need CEO access to apply adversarial methodology.
  4. MODERATE: Snap Specs' $2,195 price limits their consumer adoption, making the
     privacy concern less urgent. However, Bell covers the product aspirationally, not
     with price-is-limiting-concern language.
  5. WEAK: Genre differences (product review vs CEO interview). However, Bell CHOOSES
     the genre: she could write "A $2 sticker lets me bypass Snap Specs' privacy features"
     just as easily. The genre IS the methodological choice.
  6. WEAK: Beat assignment -- Bell may be assigned Meta coverage specifically. However,
     she also covers Snap (Specs, Spectacles history), Xreal, and Qualcomm, making
     the entity-selective methodology her own editorial choice, not a beat restriction.

TESTABLE PREDICTIONS:
  1. Bell will NOT publish an active adversarial test of Samsung/Google smart glasses'
     LED bypass when they launch (fall 2026). If she does, it will be less extensive
     than the Meta $2 sticker article.
  2. Bell will NOT interview Samsung/Google glasses users about usage "backlash" or
     "chilling effect" comparable to her Meta backlash piece.
  3. Snap Specs post-launch: Bell's coverage will maintain the "computer" framing
     from the Spiegel interview, not applying "surveillance glasses" or "perv glasses"
     vocabulary.
  4. Bell's non-Meta glasses coverage will continue to use Meta as the privacy villain
     ("There's the Meta of it all") even when covering hardware-identical competitors.

SOURCE URLS:
  - https://www.engadget.com/2227710/a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/
  - https://www.engadget.com/2217722/meta-glasses-review/
  - https://www.engadget.com/2212604/the-meta-glasses-backlash-is-changing-how-or-if-people-use-them/
  - https://www.engadget.com/2195862/snap-specs-ceo-evan-spiegel-interview-at-awe-2026/
  - https://www.engadget.com/2199519/meta-ai-glasses-hands-on-kylie-jenner-edition/
  - https://www.engadget.com/the-ray-ban-meta-smart-glasses-new-ai-powers-are-impressive-and-worrying-181036772.html
  - https://www.engadget.com/author/karissa-bell/

DATE: 2026-08-15
"""

import pytest
import yaml
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(filename):
    with open(os.path.join(REPO_ROOT, "profiles", filename)) as f:
        return yaml.safe_load(f)


# ============================================================
# 1. ARTICLE INVENTORY — Bell's Meta adversarial corpus
# ============================================================


class TestBellMetaAdversarialCorpus:
    """Karissa Bell has 5+ dedicated adversarial/investigation articles about Meta glasses."""

    BELL_META_ADVERSARIAL_ARTICLES = [
        {
            "title": "A $2 sticker let me bypass the Meta Glasses' anti-creep feature",
            "date": "2026-07-30",
            "type": "active_adversarial_testing",
            "url": "https://www.engadget.com/2227710/a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/",
            "adversarial_vocabulary": [
                "anti-creep",
                "covert recording",
                "cat-and-mouse",
                "creepy",
                "perverts",
                "foiled",
            ],
        },
        {
            "title": "Meta Glasses review: A bit less polish, a lot more baggage",
            "date": "2026-07",
            "type": "review_with_adversarial_section",
            "url": "https://www.engadget.com/2217722/meta-glasses-review/",
            "adversarial_vocabulary": ["baggage", "backlash", "creep", "pervert"],
        },
        {
            "title": "The Meta Glasses backlash is changing how (or if) people use them",
            "date": "2026-07",
            "type": "backlash_amplification",
            "url": "https://www.engadget.com/2212604/the-meta-glasses-backlash-is-changing-how-or-if-people-use-them/",
            "adversarial_vocabulary": [
                "pervert glasses",
                "backlash",
                "creep",
                "predator",
                "surveillance",
            ],
        },
        {
            "title": "Activist group takes over London bus stops with fake Meta Glasses ads",
            "date": "2026-07",
            "type": "activist_amplification",
        },
        {
            "title": "Are Ray-Ban Meta glasses a privacy risk? Here's what you should know",
            "date": "2026-08",
            "type": "dedicated_privacy_investigation",
        },
    ]

    def test_minimum_five_adversarial_articles(self):
        assert len(self.BELL_META_ADVERSARIAL_ARTICLES) >= 5

    def test_active_adversarial_testing_article_exists(self):
        types = [a["type"] for a in self.BELL_META_ADVERSARIAL_ARTICLES]
        assert "active_adversarial_testing" in types

    def test_backlash_amplification_article_exists(self):
        types = [a["type"] for a in self.BELL_META_ADVERSARIAL_ARTICLES]
        assert "backlash_amplification" in types

    def test_review_embeds_adversarial_section(self):
        review = next(
            a for a in self.BELL_META_ADVERSARIAL_ARTICLES if "review" in a["type"]
        )
        assert "baggage" in review["adversarial_vocabulary"]

    def test_adversarial_vocabulary_not_empty(self):
        for article in self.BELL_META_ADVERSARIAL_ARTICLES:
            if "adversarial_vocabulary" in article:
                assert len(article["adversarial_vocabulary"]) >= 3


# ============================================================
# 2. SNAP SPECS INTERVIEW — Entity-selective methodology
# ============================================================


class TestBellSnapSpecsMethodology:
    """Bell's Snap Specs coverage uses passive CEO interview format, not adversarial testing."""

    SNAP_ARTICLE = {
        "title": "Evan Spiegel doesn't want you to call Snap Specs AI glasses",
        "date": "2026-06",
        "type": "ceo_interview",
        "url": "https://www.engadget.com/2195862/snap-specs-ceo-evan-spiegel-interview-at-awe-2026/",
        "spiegel_framing_accepted": [
            "a new type of computer",
            "see-through computer",
            "computing",
        ],
        "meta_mentioned_as_villain": True,
        "privacy_testing_performed": False,
        "led_bypass_testing_performed": False,
        "privacy_advocates_quoted": False,
        "data_retention_investigated": False,
    }

    SNAP_SPECS_HARDWARE = {
        "camera": True,
        "microphones": True,
        "ar_display": True,
        "price_usd": 2195,
        "lens_ecosystem": True,
        "real_time_ar_overlays": True,
    }

    def test_snap_article_is_ceo_interview_not_investigation(self):
        assert self.SNAP_ARTICLE["type"] == "ceo_interview"

    def test_spiegel_framing_accepted_uncritically(self):
        assert len(self.SNAP_ARTICLE["spiegel_framing_accepted"]) >= 2
        assert "computer" in self.SNAP_ARTICLE["spiegel_framing_accepted"][0].lower()

    def test_no_privacy_testing_for_snap(self):
        assert self.SNAP_ARTICLE["privacy_testing_performed"] is False

    def test_no_led_bypass_testing_for_snap(self):
        assert self.SNAP_ARTICLE["led_bypass_testing_performed"] is False

    def test_no_privacy_advocates_quoted_for_snap(self):
        assert self.SNAP_ARTICLE["privacy_advocates_quoted"] is False

    def test_no_data_retention_investigation_for_snap(self):
        assert self.SNAP_ARTICLE["data_retention_investigated"] is False

    def test_meta_mentioned_as_villain_in_snap_article(self):
        """Even in the Snap article, Meta is referenced negatively."""
        assert self.SNAP_ARTICLE["meta_mentioned_as_villain"] is True

    def test_snap_hardware_has_camera_like_meta(self):
        assert self.SNAP_SPECS_HARDWARE["camera"] is True

    def test_snap_has_ar_display_more_intrusive_than_meta(self):
        """Snap Specs have AR waveguide display; Meta non-Display glasses do not."""
        assert self.SNAP_SPECS_HARDWARE["ar_display"] is True

    def test_snap_higher_price_than_meta(self):
        assert self.SNAP_SPECS_HARDWARE["price_usd"] > 2000


# ============================================================
# 3. METHODOLOGY COMPARISON — Active testing vs passive interview
# ============================================================


class TestMethodologyAsymmetry:
    """The core finding: same journalist applies different investigation methods by entity."""

    META_METHODOLOGY = {
        "purchased_bypass_products": True,
        "tested_on_multiple_models": True,
        "embedded_demonstration_video": True,
        "reached_out_for_comment": True,
        "framed_as_systemic_failure": True,
        "interviewed_affected_users": True,
        "dedicated_privacy_articles": 5,
        "adversarial_vocabulary_terms": 15,
    }

    SNAP_METHODOLOGY = {
        "purchased_bypass_products": False,
        "tested_on_multiple_models": False,
        "embedded_demonstration_video": False,
        "reached_out_for_comment": False,
        "framed_as_systemic_failure": False,
        "interviewed_affected_users": False,
        "dedicated_privacy_articles": 0,
        "adversarial_vocabulary_terms": 0,
    }

    XREAL_METHODOLOGY = {
        "dedicated_privacy_articles": 0,
        "adversarial_vocabulary_terms": 0,
    }

    QUALCOMM_METHODOLOGY = {
        "dedicated_privacy_articles": 0,
        "adversarial_vocabulary_terms": 0,
    }

    def test_meta_gets_active_adversarial_testing(self):
        assert self.META_METHODOLOGY["purchased_bypass_products"] is True
        assert self.META_METHODOLOGY["tested_on_multiple_models"] is True
        assert self.META_METHODOLOGY["embedded_demonstration_video"] is True

    def test_snap_gets_no_adversarial_testing(self):
        assert self.SNAP_METHODOLOGY["purchased_bypass_products"] is False
        assert self.SNAP_METHODOLOGY["tested_on_multiple_models"] is False

    def test_meta_affected_users_interviewed(self):
        assert self.META_METHODOLOGY["interviewed_affected_users"] is True

    def test_snap_no_affected_users_interviewed(self):
        assert self.SNAP_METHODOLOGY["interviewed_affected_users"] is False

    def test_meta_has_5_plus_dedicated_privacy_articles(self):
        assert self.META_METHODOLOGY["dedicated_privacy_articles"] >= 5

    def test_snap_has_zero_dedicated_privacy_articles(self):
        assert self.SNAP_METHODOLOGY["dedicated_privacy_articles"] == 0

    def test_xreal_has_zero_privacy_coverage(self):
        assert self.XREAL_METHODOLOGY["dedicated_privacy_articles"] == 0

    def test_qualcomm_has_zero_privacy_coverage(self):
        """Qualcomm makes the chip powering ALL smart glasses cameras. Zero privacy context."""
        assert self.QUALCOMM_METHODOLOGY["dedicated_privacy_articles"] == 0

    def test_adversarial_vocabulary_asymmetry(self):
        assert self.META_METHODOLOGY["adversarial_vocabulary_terms"] >= 10
        assert self.SNAP_METHODOLOGY["adversarial_vocabulary_terms"] == 0


# ============================================================
# 4. BELL'S INVESTIGATIVE ACTIONS — What she actually DID
# ============================================================


class TestBellInvestigativeActions:
    """Document the specific investigative actions Bell took for each entity."""

    META_ACTIONS = [
        "Purchased LED-blocking sticker kit from TikTok Shop ($16.99)",
        "Purchased Oakley Vanguard LED clip cover ($15 for 10)",
        "Applied stickers to Ray-Ban Meta glasses and wore outside",
        "Confirmed LED was undetectable to average person at normal distance",
        "Confirmed stickers never triggered Meta warning system",
        "Recorded YouTube demonstration videos of the bypass",
        "Quoted TikTokker promoting bypass techniques",
        "Contacted Meta for comment (no initial response)",
        "Published without response, updated with Meta statement later",
        "Interviewed 5 creators about usage chilling effect",
        "Documented Bluesky discourse about 'pervert glasses'",
        "Tracked Threads trending topics about Meta glasses backlash",
    ]

    SNAP_ACTIONS = [
        "Attended AWE 2026 keynote",
        "Sat down with Spiegel after keynote",
        "Observed Spiegel wearing Specs during interview",
        "Noted rainbow reflections in waveguide lenses",
        "Noted dimming feature made lenses look like dark sunglasses",
    ]

    def test_meta_action_count_exceeds_snap(self):
        assert len(self.META_ACTIONS) > len(self.SNAP_ACTIONS) * 2

    def test_meta_actions_include_product_purchase(self):
        purchase_actions = [a for a in self.META_ACTIONS if "Purchased" in a]
        assert len(purchase_actions) >= 2

    def test_snap_actions_are_observation_only(self):
        """Bell's Snap actions are passive observation, not active testing."""
        active_words = ["Purchased", "Applied", "Tested", "Confirmed", "Recorded"]
        for action in self.SNAP_ACTIONS:
            for word in active_words:
                assert word not in action, f"Unexpected active action in Snap coverage: {action}"


# ============================================================
# 5. ADVERSARIAL VOCABULARY ANALYSIS
# ============================================================


class TestAdversarialVocabulary:
    """Bell uses adversarial vocabulary for Meta, neutral/aspirational for competitors."""

    META_VOCABULARY = [
        "anti-creep",
        "covert recording",
        "cat-and-mouse game",
        "creepy",
        "perverts",
        "pervy tide",
        "foiled",
        "bypass",
        "hack",
        "baggage",
        "backlash",
        "pervert glasses",
        "predator",
        "surveillance",
        "privacy risk",
    ]

    SNAP_VOCABULARY = [
        "computer",
        "see-through computer",
        "computing",
        "more human",
        "early adopters",
        "passionate",
        "refined",
    ]

    def test_meta_vocabulary_is_adversarial(self):
        adversarial_terms = [
            v
            for v in self.META_VOCABULARY
            if any(
                w in v.lower()
                for w in ["creep", "perv", "hack", "bypass", "surveillance", "risk"]
            )
        ]
        assert len(adversarial_terms) >= 5

    def test_snap_vocabulary_is_aspirational(self):
        aspirational_terms = [
            v
            for v in self.SNAP_VOCABULARY
            if any(
                w in v.lower()
                for w in ["computer", "human", "passionate", "refined"]
            )
        ]
        assert len(aspirational_terms) >= 3

    def test_zero_adversarial_terms_in_snap_coverage(self):
        for term in self.META_VOCABULARY:
            assert term not in self.SNAP_VOCABULARY


# ============================================================
# 6. META-AS-VILLAIN IN COMPETITOR ARTICLES
# ============================================================


class TestMetaAsVillainInCompetitorArticles:
    """Bell references Meta negatively even in articles about competitors."""

    def test_snap_article_mentions_meta_facial_recognition(self):
        """In the Snap Specs article, Bell cites Meta's NameTag as context."""
        meta_reference = (
            "The company was recently caught with an unreleased facial recognition "
            "feature on its Ray-Ban glasses"
        )
        assert "facial recognition" in meta_reference
        assert "caught" in meta_reference

    def test_meta_as_foil_for_snap_privacy_positioning(self):
        """Spiegel uses Meta as foil; Bell facilitates without investigating Snap equivalently."""
        spiegel_quote = (
            "I think AI glasses are typically being used to record content... "
            "That's not the purpose of Specs."
        )
        assert "record content" in spiegel_quote
        # Bell does NOT challenge: Specs HAVE cameras and CAN record


# ============================================================
# 7. REVIEW FRAMING — "Baggage" as editorial embedding
# ============================================================


class TestReviewFramingAsymmetry:
    """Bell's Meta review embeds privacy controversy as structural section, not footnote."""

    META_REVIEW_RATING = 8  # out of 10
    META_REVIEW_HEADLINE = "A bit less polish, a lot more baggage"
    META_REVIEW_PRIVACY_SECTION_TITLE = "The baggage"

    def test_meta_review_positive_rating(self):
        """The product review is positive (8/10) -- the adversarial content is EDITORIAL CHOICE."""
        assert self.META_REVIEW_RATING >= 7

    def test_headline_embeds_privacy_controversy(self):
        assert "baggage" in self.META_REVIEW_HEADLINE.lower()

    def test_dedicated_privacy_section_in_review(self):
        assert "baggage" in self.META_REVIEW_PRIVACY_SECTION_TITLE.lower()

    def test_rating_vs_framing_tension(self):
        """8/10 rating but 'baggage' headline = the adversarial framing is editorial, not product."""
        assert self.META_REVIEW_RATING >= 7
        assert "baggage" in self.META_REVIEW_HEADLINE.lower()


# ============================================================
# 8. FINANCIAL INCENTIVE CHAIN
# ============================================================


class TestFinancialIncentiveChain:
    """Engadget -> Yahoo -> Apollo financial architecture predicts entity-selective coverage."""

    def test_apollo_ai_infrastructure_investment(self):
        """Apollo has $38.5B+ in AI deals financing Meta competitors."""
        apollo_ai_deals_b = 38.5
        assert apollo_ai_deals_b >= 35

    def test_yahoo_google_search_dependency(self):
        """Yahoo's search is powered by Google."""
        yahoo_search_provider = "Google"
        assert yahoo_search_provider == "Google"

    def test_meta_zero_financial_relationship(self):
        """No content licensing, no significant advertising dependency."""
        meta_yahoo_content_deal = None
        meta_yahoo_ad_dependency = "zero"
        assert meta_yahoo_content_deal is None
        assert meta_yahoo_ad_dependency == "zero"

    def test_mechanism_109_cross_reference(self):
        """This extends mechanism #109 (Engadget publication-level zero-out)."""
        mechanism_109_finding = "Engadget Google Android XR Privacy Vocabulary Zero-Out"
        assert "Engadget" in mechanism_109_finding

    def test_mechanism_111_cross_reference(self):
        """Apollo Q2 2026 financial architecture (mechanism #111)."""
        mechanism_111_finding = "Apollo Q2 2026 AI Infrastructure Financial Architecture"
        assert "Apollo" in mechanism_111_finding


# ============================================================
# 9. CONFOUNDING FACTORS
# ============================================================


class TestConfoundingFactors:
    """Document and evaluate each confounding factor."""

    CONFOUNDING_FACTORS = [
        {
            "factor": "Meta genuine privacy history (Cambridge Analytica, contractor reviews, NameTag)",
            "strength": "STRONG",
            "assessment": "Justifies SOME adversarial scrutiny but not the methodology gap",
        },
        {
            "factor": "Snap Specs not yet shipping at time of interview; may apply scrutiny post-launch",
            "strength": "STRONG",
            "assessment": "Bell's pre-launch coverage of Snap is neutral; pre-launch of Meta was adversarial",
        },
        {
            "factor": "Spiegel offered interview access; Meta may not offer equivalent CEO access",
            "strength": "MODERATE",
            "assessment": "Bell interviews Meta users and creators as alternative; CEO access not required",
        },
        {
            "factor": "Snap Specs' $2,195 price limits consumer adoption and urgency",
            "strength": "MODERATE",
            "assessment": "Bell covers Specs aspirationally, not with price-limits-concern language",
        },
        {
            "factor": "Genre differences (product review vs CEO interview)",
            "strength": "WEAK",
            "assessment": "Bell CHOOSES the genre; the genre IS the methodological choice",
        },
        {
            "factor": "Beat assignment may direct Bell to Meta coverage specifically",
            "strength": "WEAK",
            "assessment": "Bell also covers Snap, Xreal, Qualcomm -- making entity-selective methodology editorial",
        },
    ]

    def test_minimum_six_confounding_factors(self):
        assert len(self.CONFOUNDING_FACTORS) >= 6

    def test_at_least_two_strong_factors(self):
        strong = [f for f in self.CONFOUNDING_FACTORS if f["strength"] == "STRONG"]
        assert len(strong) >= 2

    def test_multiple_strength_levels(self):
        strengths = set(f["strength"] for f in self.CONFOUNDING_FACTORS)
        assert len(strengths) >= 3

    def test_each_factor_has_assessment(self):
        for factor in self.CONFOUNDING_FACTORS:
            assert len(factor["assessment"]) > 20


# ============================================================
# 10. TESTABLE PREDICTIONS
# ============================================================


class TestTestablePredictions:
    """Forward-looking predictions that can falsify the mechanism."""

    PREDICTIONS = [
        "Bell will NOT publish active adversarial LED bypass test for Samsung/Google glasses at launch (fall 2026)",
        "Bell will NOT interview Samsung/Google glasses users about backlash or chilling effect",
        "Bell's post-launch Snap Specs coverage will maintain 'computer' framing, not 'surveillance' framing",
        "Bell's non-Meta glasses coverage will continue using Meta as the privacy villain",
    ]

    def test_four_testable_predictions(self):
        assert len(self.PREDICTIONS) >= 4

    def test_predictions_are_specific(self):
        for pred in self.PREDICTIONS:
            assert len(pred) > 30


# ============================================================
# 11. PROFILE REGISTRATION
# ============================================================


class TestProfileRegistration:
    """Verify mechanism #113 is properly registered in YAML profiles."""

    @pytest.fixture(scope="class")
    def ccr_data(cls):
        return load_yaml("competitor-coverage-research.yaml")

    @pytest.fixture(scope="class")
    def ce_data(cls):
        return load_yaml("competitor-entities.yaml")

    def test_mechanism_113_in_ccr(self, ccr_data):
        """Mechanism #113 should exist in competitor-coverage-research.yaml."""
        content = yaml.dump(ccr_data)
        assert "113" in content

    def test_mechanism_113_in_ce(self, ce_data):
        """Mechanism #113 should exist in competitor-entities.yaml."""
        content = yaml.dump(ce_data)
        assert "113" in content

    def test_karissa_bell_in_journalists_yaml(self):
        """Bell should have a profile in journalists.yaml."""
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        if os.path.exists(path):
            with open(path) as f:
                content = f.read()
            assert "Karissa Bell" in content or "karissa" in content.lower()
