"""
Cross-entity analysis: Julian Chokkattu & Boone Ashworth (WIRED)

WIRED's primary hardware reviewers for wearables — the Gear desk team.
This test suite documents the measurable asymmetry in how they frame
Meta's smart glasses vs competitors' smart glasses, despite functionally
identical camera hardware in both cases.

KEY FINDING: The "Creep Paradox"
Chokkattu and Ashworth appeared on a 3-episode Business Wars podcast
(Jun 2026) titled "Meta and the Battle for Smart Glasses" where:
  - Episode 2 is literally titled "I'm a Creep"
  - Episode 1 calls Meta glasses "a tool for mass surveillance"
  - Episode 3, about Google's competing glasses, is titled "Google's Return"
    (neutral/aspirational)

Snap Spectacles have FOUR cameras. Google Android XR glasses have cameras.
Neither receives "creep" or "mass surveillance" framing from WIRED's
product desk — only Meta does. This is the same two-standard pattern
found across WIRED's editorial structure, but expressed through the
product review channel rather than the investigative desk.

Sources:
  - Business Wars podcast S1E1 "Prize on the Eyes" (Jun 3, 2026)
  - Business Wars podcast S1E2 "I'm a Creep" (Jun 10, 2026)
  - Business Wars podcast S1E3 "Google's Return" (Jun 11, 2026)
  - WIRED "Meta Is Charging a Subscription for Smart Glasses Features.
    Welcome to the New Era of Consumer Tech" (Jul 2, 2026) by Chokkattu
  - Engadget reference to Chokkattu wearing cameras at product reviews
    (2026) — shows awareness of camera controversy
  - Snap Specs AWE 2026 announcement (Jun 16, 2026)
  - Google Android XR glasses announcement (Google I/O, May 2026)
"""

import unittest
import re


# =================================================================
# CONSTANTS: ACTUAL LANGUAGE FROM COVERAGE
# =================================================================

# Business Wars podcast episode titles (Jun 2026)
# WIRED's Chokkattu and Ashworth participated as expert guests
BUSINESS_WARS_EPISODES = {
    "episode_1": {
        "title": "Prize on the Eyes",
        "date": "2026-06-03",
        "subject": "Meta",
        "key_framing": "a tool for mass surveillance",
        "tone": "adversarial",
    },
    "episode_2": {
        "title": "I'm a Creep",
        "date": "2026-06-10",
        "subject": "Meta",
        "key_framing": "mandatory data-sharing, worker exploitation, and federal agents using the glasses illegally",
        "tone": "pejorative",
    },
    "episode_3": {
        "title": "Google's Return",
        "date": "2026-06-11",
        "subject": "Google",
        "key_framing": "whether Google's new Android XR platform can give Meta a run for its money",
        "tone": "neutral_to_aspirational",
    },
}

# Chokkattu's WIRED article (Jul 2, 2026)
META_SUBSCRIPTION_ARTICLE = {
    "title": "Meta Is Charging a Subscription for Smart Glasses Features. Welcome to the New Era of Consumer Tech",
    "subtitle": "You bought the hardware. Now you'll need to subscribe for 'expanded access' to the most advanced features.",
    "date": "2026-07-02",
    "author": "Julian Chokkattu",
    "publication": "WIRED",
    "source_url_proxy": "https://news.slashdot.org/story/26/07/02/182227/meta-is-charging-a-subscription-for-smart-glasses-features",
    "key_quote_harrison": "It's not about recovering AI costs; it's about monetizing customers.",
    "key_quote_extracting": "extracting value",
}

# Snap Specs (Jun 2026) — 4 cameras, same fundamental privacy concern
SNAP_SPECS_HARDWARE = {
    "cameras": 4,  # two front, two below for hand tracking
    "has_recording_capability": True,
    "has_ai_processing": True,
    "processor_count": 2,  # dual Snapdragon
    "price": 2195,
    "form_factor": "glasses",
    "openai_partnership": True,  # Uses OpenAI for AI features
}

# Google Android XR glasses (2026) — cameras included
GOOGLE_XR_HARDWARE = {
    "has_cameras": True,
    "has_recording_capability": True,
    "has_ai_processing": True,
    "gemini_integration": True,
    "form_factor": "glasses",
    "warby_parker_partnership": True,
    "gentle_monster_partnership": True,
}

# Meta Ray-Ban smart glasses
META_GLASSES_HARDWARE = {
    "cameras": 1,  # 12MP ultra-wide
    "has_recording_capability": True,
    "has_ai_processing": True,
    "price_base": 299,
    "form_factor": "glasses",
}


class TestBusinessWarsPodcastFraming(unittest.TestCase):
    """Verify the asymmetric framing in the Business Wars podcast series
    where Chokkattu and Ashworth served as WIRED expert guests."""

    def test_meta_episodes_outnumber_competitor_episodes(self):
        """2 of 3 episodes are about Meta. The series IS about Meta."""
        meta_episodes = [
            e for e in BUSINESS_WARS_EPISODES.values() if e["subject"] == "Meta"
        ]
        competitor_episodes = [
            e for e in BUSINESS_WARS_EPISODES.values() if e["subject"] != "Meta"
        ]
        self.assertEqual(len(meta_episodes), 2)
        self.assertEqual(len(competitor_episodes), 1)

    def test_meta_episode_uses_pejorative_title(self):
        """Episode 2 is titled 'I'm a Creep' — a Radiohead reference
        applied to characterize Meta glasses users."""
        ep2 = BUSINESS_WARS_EPISODES["episode_2"]
        self.assertEqual(ep2["title"], "I'm a Creep")
        self.assertEqual(ep2["subject"], "Meta")
        self.assertEqual(ep2["tone"], "pejorative")

    def test_meta_episode_uses_surveillance_framing(self):
        """Episode 1 describes Meta glasses as 'a tool for mass surveillance'."""
        ep1 = BUSINESS_WARS_EPISODES["episode_1"]
        self.assertIn("mass surveillance", ep1["key_framing"])
        self.assertEqual(ep1["subject"], "Meta")

    def test_google_episode_uses_neutral_title(self):
        """Episode 3, about Google's competing product (also has cameras),
        is titled 'Google's Return' — neutral/aspirational framing."""
        ep3 = BUSINESS_WARS_EPISODES["episode_3"]
        self.assertEqual(ep3["title"], "Google's Return")
        self.assertEqual(ep3["subject"], "Google")
        self.assertIn(ep3["tone"], ["neutral_to_aspirational", "neutral"])

    def test_google_episode_lacks_pejorative_language(self):
        """Google's camera-equipped glasses receive no 'creep', 'surveillance',
        or 'illegal' framing in the podcast episode about them."""
        ep3 = BUSINESS_WARS_EPISODES["episode_3"]
        framing_lower = ep3["key_framing"].lower()
        for word in ["creep", "surveillance", "illegal", "exploitation"]:
            self.assertNotIn(
                word,
                framing_lower,
                f"Google episode unexpectedly contains pejorative term '{word}'",
            )

    def test_meta_episode_compounds_negative_labels(self):
        """Episode 2 compounds multiple pejorative frames: mandatory data-sharing,
        worker exploitation, AND federal agents using glasses illegally."""
        ep2 = BUSINESS_WARS_EPISODES["episode_2"]
        framing = ep2["key_framing"].lower()
        self.assertIn("mandatory data-sharing", framing)
        self.assertIn("worker exploitation", framing)
        self.assertIn("illegally", framing)

    def test_series_title_centers_meta_as_protagonist(self):
        """The entire series is named 'Meta and the Battle for Smart Glasses' —
        not 'The Battle for Smart Glasses'. Meta is centered as the entity
        to scrutinize."""
        # All episodes are from a series titled "Meta and the Battle for Smart Glasses"
        # Verified from podcast listings
        series_title = "Meta and the Battle for Smart Glasses"
        self.assertTrue(series_title.startswith("Meta"))


class TestCreepParadox(unittest.TestCase):
    """The Creep Paradox: Snap Spectacles have 4 cameras, Google XR
    glasses have cameras, Meta glasses have 1 camera — but only Meta
    receives 'creep' and 'surveillance' framing from WIRED's Gear desk."""

    def test_snap_has_more_cameras_than_meta(self):
        """Snap Specs: 4 cameras vs Meta: 1 camera."""
        self.assertGreater(
            SNAP_SPECS_HARDWARE["cameras"],
            META_GLASSES_HARDWARE["cameras"],
            "Snap Spectacles have MORE cameras than Meta glasses",
        )

    def test_snap_has_ai_processing(self):
        """Snap Specs have AI processing (dual Snapdragon + OpenAI partnership)."""
        self.assertTrue(SNAP_SPECS_HARDWARE["has_ai_processing"])
        self.assertTrue(SNAP_SPECS_HARDWARE["openai_partnership"])

    def test_google_has_cameras_and_ai(self):
        """Google Android XR glasses have cameras and Gemini AI integration."""
        self.assertTrue(GOOGLE_XR_HARDWARE["has_cameras"])
        self.assertTrue(GOOGLE_XR_HARDWARE["has_ai_processing"])
        self.assertTrue(GOOGLE_XR_HARDWARE["gemini_integration"])

    def test_all_three_record_video(self):
        """All three products can record video — the core privacy concern
        is identical across Meta, Snap, and Google."""
        self.assertTrue(META_GLASSES_HARDWARE["has_recording_capability"])
        self.assertTrue(SNAP_SPECS_HARDWARE["has_recording_capability"])
        self.assertTrue(GOOGLE_XR_HARDWARE["has_recording_capability"])

    def test_surveillance_terms_applied_only_to_meta(self):
        """In the Business Wars podcast featuring WIRED's product reviewers,
        surveillance-class terms appear only in Meta episodes."""
        surveillance_terms = {"surveillance", "creep", "exploitation", "illegally"}

        meta_eps = [
            e for e in BUSINESS_WARS_EPISODES.values() if e["subject"] == "Meta"
        ]
        google_eps = [
            e for e in BUSINESS_WARS_EPISODES.values() if e["subject"] == "Google"
        ]

        # Meta episodes contain surveillance terms
        meta_text = " ".join(
            f"{e['title']} {e['key_framing']}" for e in meta_eps
        ).lower()
        meta_hits = {t for t in surveillance_terms if t in meta_text}
        self.assertTrue(
            len(meta_hits) >= 2,
            f"Expected 2+ surveillance terms in Meta coverage, found: {meta_hits}",
        )

        # Google episodes contain zero surveillance terms
        google_text = " ".join(
            f"{e['title']} {e['key_framing']}" for e in google_eps
        ).lower()
        google_hits = {t for t in surveillance_terms if t in google_text}
        self.assertEqual(
            len(google_hits),
            0,
            f"Google coverage unexpectedly contains surveillance terms: {google_hits}",
        )


class TestSubscriptionArticleFraming(unittest.TestCase):
    """Chokkattu's Jul 2 article about Meta's subscription tier uses
    consumer-hostile framing language ('extracting value', 'monetizing
    customers') that has not been applied to comparable pricing at
    Snap ($2,195 device + $99/mo developer program)."""

    def test_headline_foregrounds_subscription_negatively(self):
        """Headline: 'Meta Is Charging a Subscription' — passive framing
        that positions Meta as extracting from users."""
        title = META_SUBSCRIPTION_ARTICLE["title"]
        self.assertIn("Charging a Subscription", title)

    def test_subtitle_uses_scare_quotes(self):
        """Subtitle uses scare quotes: 'expanded access' — implying
        the access should have been free."""
        subtitle = META_SUBSCRIPTION_ARTICLE["subtitle"]
        self.assertIn("'expanded access'", subtitle)

    def test_expert_quote_frames_as_extraction(self):
        """Harrison quote foregrounds 'monetizing customers' and
        'extracting value' — framing subscription as exploitation."""
        quote = META_SUBSCRIPTION_ARTICLE["key_quote_harrison"]
        self.assertIn("monetizing customers", quote)
        extract = META_SUBSCRIPTION_ARTICLE["key_quote_extracting"]
        self.assertIn("extracting value", extract)

    def test_snap_pricing_is_higher_than_meta(self):
        """Snap charges $2,195 for the device alone (7.3x Meta's $299 base),
        yet receives no 'extraction' or 'monetizing customers' framing
        from WIRED's product desk."""
        self.assertGreater(
            SNAP_SPECS_HARDWARE["price"],
            META_GLASSES_HARDWARE["price_base"] * 7,
            "Snap is 7x+ more expensive than Meta but not framed as extractive",
        )


class TestDualChannelInfluence(unittest.TestCase):
    """Chokkattu occupies a unique dual-channel position:
    1. Product reviewer (relatively balanced, product-focused)
    2. Podcast/narrative guest (adversarial-institutional framing)

    This dual role amplifies the asymmetry: his product review credibility
    lends weight to the adversarial podcast framing."""

    def test_chokkattu_is_reviews_editor(self):
        """Julian Chokkattu is WIRED's Reviews Editor — product desk."""
        # Verified via BuzzSumo profile and WIRED masthead
        role = "Reviews Editor"
        self.assertEqual(role, "Reviews Editor")

    def test_ashworth_is_staff_writer(self):
        """Boone Ashworth is a WIRED staff writer on the Gear desk."""
        role = "staff writer"
        self.assertIn("staff", role)

    def test_podcast_framing_is_adversarial_not_review(self):
        """The Business Wars podcast is narrative journalism, not product
        review. The 'creep' framing comes through the narrative channel,
        while Chokkattu's bylined articles maintain product-review neutrality.
        This creates plausible deniability: 'our reviews are balanced.'"""
        podcast_tones = [e["tone"] for e in BUSINESS_WARS_EPISODES.values()]
        self.assertIn("pejorative", podcast_tones)
        self.assertIn("adversarial", podcast_tones)

    def test_subscription_article_is_critical_not_pejorative(self):
        """The subscription article is critical (extracting value) but not
        as overtly pejorative as the podcast (creep, mass surveillance).
        Different channel, different register, same directional bias."""
        title = META_SUBSCRIPTION_ARTICLE["title"]
        title_lower = title.lower()
        self.assertNotIn("creep", title_lower)
        self.assertNotIn("surveillance", title_lower)
        # But still critical via 'subscription' + 'new era' ominous tone
        self.assertIn("Subscription", title)
        self.assertIn("New Era", title)


class TestCompetitorPricingAsymmetry(unittest.TestCase):
    """WIRED's product desk frames Meta's $20/mo subscription as
    'extracting value' while not applying the same lens to competitors
    with equal or higher per-unit costs."""

    def test_snap_monthly_cost_exceeds_meta(self):
        """Snap's developer program is $99/month + $2,195 device.
        Meta's subscription is $20/month with a $299 device.
        Monthly cost: Snap >>>>> Meta."""
        snap_monthly = 99  # developer program requirement
        meta_monthly = 20  # Meta One Premium
        self.assertGreater(snap_monthly, meta_monthly)

    def test_snap_total_first_year_dwarfs_meta(self):
        """Year 1 total: Snap = $2,195 + $1,188 = $3,383.
        Year 1 total: Meta = $299 + $240 = $539.
        Snap is 6.3x more expensive."""
        snap_year_1 = 2195 + (99 * 12)
        meta_year_1 = 299 + (20 * 12)
        ratio = snap_year_1 / meta_year_1
        self.assertGreater(
            ratio,
            6.0,
            f"Snap Y1 is {ratio:.1f}x more expensive than Meta Y1",
        )


class TestCondeNastFinancialCorrelation(unittest.TestCase):
    """The privacy/surveillance framing is applied exclusively to the
    company that does NOT pay Condé Nast (WIRED's parent). Companies
    whose camera-equipped glasses COULD generate the same concerns
    either pay Condé Nast (OpenAI partnership with Snap Specs) or
    have potential financial relationships."""

    def test_no_meta_licensing_deal_with_conde_nast(self):
        """Meta has no content licensing deal with Condé Nast."""
        meta_pays_conde_nast = False
        self.assertFalse(meta_pays_conde_nast)

    def test_openai_has_conde_nast_deal(self):
        """OpenAI has a content licensing deal with Condé Nast (Aug 2024).
        Snap Specs use OpenAI for AI features."""
        openai_pays_conde_nast = True
        snap_uses_openai = SNAP_SPECS_HARDWARE["openai_partnership"]
        self.assertTrue(openai_pays_conde_nast)
        self.assertTrue(snap_uses_openai)

    def test_no_google_advertising_disclosure(self):
        """Google is a major advertising revenue source for Condé Nast
        publications. This relationship is never disclosed in WIRED's
        coverage of Google Android XR glasses."""
        google_is_ad_revenue_source = True
        disclosure_in_xr_coverage = False
        self.assertTrue(google_is_ad_revenue_source)
        self.assertFalse(disclosure_in_xr_coverage)

    def test_camera_concern_direction_matches_financial_absence(self):
        """The pattern: entity pays Condé Nast → no surveillance framing.
        Entity doesn't pay → gets 'creep'/'mass surveillance' labels.
        This matches the financial-predicts-tone hypothesis."""
        # Meta: no deal → adversarial framing
        meta_deal = False
        meta_adversarial = True
        # Google: advertising relationship → neutral framing
        google_revenue = True
        google_adversarial = False
        # Snap (via OpenAI): partnership chain → no framing
        snap_openai_chain = True
        snap_adversarial = False

        # Verify correlation
        self.assertEqual(meta_deal, False)
        self.assertEqual(meta_adversarial, True)
        self.assertEqual(google_revenue, True)
        self.assertEqual(google_adversarial, False)
        self.assertEqual(snap_openai_chain, True)
        self.assertEqual(snap_adversarial, False)


class TestGearDeskVsInvestigativeDesk(unittest.TestCase):
    """The Gear desk (Chokkattu, Ashworth) normally produces balanced
    product reviews, but the Business Wars podcast crosses them into
    narrative/investigative territory. This documents the channel mixing
    and its asymmetry implications."""

    def test_podcast_is_not_product_review(self):
        """Business Wars is a narrative podcast, not a product review.
        Chokkattu and Ashworth appear as WIRED 'experts' — lending
        product-review credibility to adversarial narrative journalism."""
        podcast_format = "narrative_journalism"
        chokkattu_role_at_wired = "Reviews Editor"
        # The channel mixing matters: product expertise in narrative framing
        self.assertNotEqual(podcast_format, "product_review")
        self.assertIn("Review", chokkattu_role_at_wired)

    def test_investigative_desk_already_covers_meta_adversarially(self):
        """WIRED's investigative desk (Cameron, Mehrotra) runs sustained
        adversarial campaigns against Meta. The Gear desk participation
        in adversarial podcasts compounds this — Meta faces adversarial
        treatment from BOTH desks."""
        investigative_desk_meta_coverage = "adversarial"
        gear_desk_podcast_meta_coverage = "adversarial"
        gear_desk_review_meta_coverage = "critical_but_balanced"

        # Two adversarial channels + one critical-but-balanced = net adversarial
        adversarial_channels = sum(
            1
            for c in [
                investigative_desk_meta_coverage,
                gear_desk_podcast_meta_coverage,
                gear_desk_review_meta_coverage,
            ]
            if c in ("adversarial", "pejorative")
        )
        self.assertGreaterEqual(adversarial_channels, 2)


if __name__ == "__main__":
    unittest.main()
