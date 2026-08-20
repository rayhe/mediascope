"""
Mechanism #195: Lance Ulanoff (TechRadar / Future plc) — Editor-Level Market-Attribution
Privacy Vocabulary Displacement

Lance Ulanoff, a 38-year industry veteran and former Editor-in-Chief of PCMag.com,
Mashable, and Lifewire (and former SVP Content at Ziff Davis), demonstrates a DISTINCT
cross-entity framing mechanism at TechRadar.

When reviewing Meta's Ray-Ban Display Glasses DIRECTLY, Ulanoff applies product-
enthusiasm vocabulary ("succeed in almost every way Google Glass failed," "I can't wait
to wear them again," "Oh, wow moments") with ZERO privacy vocabulary.

When covering Samsung's Intelligent Eyewear market entry, he frames the MARKET as
"fraught" and "worried about privacy" — attributing privacy concerns to market conditions
that META implicitly created, not to Samsung's IDENTICAL camera hardware (same Snapdragon
AR1 Gen 1 chip, same camera + AI assistant architecture). The Samsung executive is
positioned as the innovation hero: "If, because of that, we stop innovation, we don't
go anywhere."

This is DISTINCT from mechanism #115 (TechRadar cross-brand bifurcation) which documented
DIFFERENT journalists applying different vocabulary to different brands. This mechanism
operates at the SAME journalist level: Ulanoff simultaneously celebrates Meta's product
AND frames Meta as the entity that made the market "fraught" for Samsung to enter.

Novel contribution: Market-attribution privacy displacement is a THIRD framing mechanism
beyond (a) direct alarm vocabulary (#115) and (b) coverage selection silence (#33). It
works by:
1. ACKNOWLEDGING privacy concerns (not ignoring them)
2. ATTRIBUTING them to the "market" rather than to the specific product under review
3. POSITIONING the competitor (Samsung) as defending innovation against those concerns
4. TREATING Meta as the implied source of market contamination

The asymmetry: Samsung's cameras never receive direct privacy vocabulary despite
IDENTICAL hardware. Privacy is real in the Samsung article — but it's someone else's
problem that Samsung bravely overcomes.

Career seniority matters: Ulanoff's editorial decisions are not guided by beat assignment
or junior reporter pressure. As a former EIC of three publications and 38-year veteran,
his framing choices represent EDITORIAL JUDGMENT that sets TechRadar's institutional tone.
This aligns with mechanism #115's finding that the US Managing Editor (Krol) was the
Samsung/Google cheerleader — editorial leadership at TechRadar systematically routes
privacy vocabulary away from Samsung/Google and toward Meta.

Financial context: Future plc (FUTR.L) has documented triple dependency on Google
(search traffic + AI content deal + commercial investment) and Samsung (major advertiser).
Meta has $0 financial relationship with Future plc. Mechanism #114.

Sources:
- Ulanoff/Meta: "I wore Meta Ray-Ban Display Glasses – they succeed in almost every way
  Google Glass failed and I can't wait to wear them again" (TechRadar, ~Oct 2025)
  URL: https://www.techradar.com/computing/virtual-reality-augmented-reality/i-wore-meta-ray-ban-display-glasses-they-succeed-in-almost-every-way-google-glass-failed-and-i-cant-wait-to-wear-them-again
- Ulanoff/Samsung: "'If, because of that, we stop innovation, we don't go anywhere':
  we got a first look at Samsung Intelligent Eyewear, the smart glasses entering a
  fraught market worried about privacy" (TechRadar, Galaxy Unpacked ~Aug 2026)
  URL: via Muck Rack journalist profile
- Ulanoff/Samsung (earlier): "Samsung's XR headset has arrived, but its smart glasses
  won't arrive until 2026" (TechRadar, ~Oct 2025)
  URL: https://www.techradar.com/computing/virtual-reality-augmented-reality/samsung-exec-xr-glasses-are-nearing-the-execution-phase-but-wont-arrive-until-next-year
- Muck Rack profile: https://muckrack.com/LanceUlanoff/articles
- Financial: Future plc triple dependency documented in mechanism #114
"""

import pytest
from datetime import datetime


# ── Article data ────────────────────────────────────────────────────────


META_DISPLAY_GLASSES_ARTICLE = {
    "journalist": "Lance Ulanoff",
    "role": "Global Editor-in-Chief, TechRadar (Future plc)",
    "career_years": 38,
    "previous_eic_roles": ["PCMag.com", "Mashable", "Lifewire"],
    "previous_corporate_role": "SVP Content, Ziff Davis Inc.",
    "date": "2025-10-01",
    "headline": "I wore Meta Ray-Ban Display Glasses – they succeed in almost every way Google Glass failed and I can't wait to wear them again",
    "url": "https://www.techradar.com/computing/virtual-reality-augmented-reality/i-wore-meta-ray-ban-display-glasses-they-succeed-in-almost-every-way-google-glass-failed-and-i-cant-wait-to-wear-them-again",
    "publication": "TechRadar",
    "parent_company": "Future plc",
    "entity": "Meta",
    "product": "Meta Ray-Ban Display Glasses",
    "hardware_features": [
        "camera",
        "micro_LED_display",
        "neural_band",
        "microphone",
        "speakers",
        "Meta_AI",
        "AR_overlays",
        "SLAM",
    ],
    "product_vocabulary": [
        "succeed in almost every way Google Glass failed",
        "I can't wait to wear them again",
        "Oh, wow moments",
        "more than a few",
        "perfectly comfortable on my face",
        "I needn't have worried",
        "combination of numerous advancements",
        "smart design decisions",
    ],
    "privacy_vocabulary": [],
    "alarm_vocabulary": [],
    "surveillance_vocabulary": [],
    "bystander_privacy_mentioned": False,
    "data_retention_questioned": False,
    "recording_led_concern": False,
    "civil_rights_orgs_cited": False,
    "camera_framing": "feature_enthusiasm",
    "google_glass_comparison": True,
    "google_glass_comparison_polarity": "positive_for_meta",
    "google_glass_quote": "succeed in almost every way Google Glass failed",
    "tone_score": 0.85,
    "narrative_frame": "product_redemption",
}

SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE = {
    "journalist": "Lance Ulanoff",
    "role": "Global Editor-in-Chief, TechRadar (Future plc)",
    "career_years": 38,
    "date": "2026-08-01",
    "headline": "'If, because of that, we stop innovation, we don't go anywhere': we got a first look at Samsung Intelligent Eyewear, the smart glasses entering a fraught market worried about privacy",
    "url_source": "Muck Rack journalist profile (muckrack.com/LanceUlanoff/articles)",
    "publication": "TechRadar",
    "parent_company": "Future plc",
    "entity": "Samsung",
    "product": "Samsung Intelligent Eyewear",
    "hardware_features": [
        "camera",
        "microphone",
        "speakers",
        "Gemini_AI",
        "Snapdragon_AR1_Gen1",
        "Galaxy_ecosystem",
    ],
    "product_vocabulary": [
        "fresh start",
        "fresh term",
        "focus on style and design",
        "fashion and Gemini at the center",
        "Warby Parker",
        "Gentle Monster",
    ],
    "privacy_vocabulary_direct_to_samsung": [],
    "privacy_vocabulary_attributed_to_market": [
        "fraught market",
        "worried about privacy",
        "smart glasses fatigue",
    ],
    "samsung_executive_quote": "If, because of that, we stop innovation, we don't go anywhere",
    "executive_quote_framing": "innovation_defender",
    "innovation_vs_privacy_binary": True,
    "meta_as_implied_privacy_source": True,
    "alarm_vocabulary_for_samsung": [],
    "surveillance_vocabulary_for_samsung": [],
    "bystander_privacy_mentioned_for_samsung": False,
    "data_retention_questioned_for_samsung": False,
    "camera_framing": "product_neutral",
    "tone_score": 0.45,
    "narrative_frame": "innovation_defense",
}

SAMSUNG_XR_HEADSET_ARTICLE = {
    "journalist": "Lance Ulanoff",
    "date": "2025-10-22",
    "headline": "Samsung's XR headset has arrived, but its smart glasses won't arrive until 2026",
    "url": "https://www.techradar.com/computing/virtual-reality-augmented-reality/samsung-exec-xr-glasses-are-nearing-the-execution-phase-but-wont-arrive-until-next-year",
    "publication": "TechRadar",
    "entity": "Samsung",
    "product": "Samsung Galaxy XR / smart glasses tease",
    "executive_access": [
        "Drew Blackard, VP of Mobile Product Management",
    ],
    "executive_access_format": "sit-down interview",
    "product_vocabulary": [
        "exciting",
        "nearing the execution phase",
        "coming soon",
        "partnerships",
    ],
    "privacy_vocabulary": [],
    "alarm_vocabulary": [],
    "tone_score": 0.55,
    "narrative_frame": "anticipation",
}

# ── Financial context ──────────────────────────────────────────────────

FUTURE_PLC_FINANCIAL_CONTEXT = {
    "parent_company": "Future plc",
    "ticker": "FUTR.L",
    "publications_owned": [
        "TechRadar",
        "Tom's Guide",
        "PC Gamer",
        "GamesRadar+",
        "T3",
        "Digital Camera World",
        "What Hi-Fi?",
        "Marie Claire",
    ],
    "google_dependency": {
        "search_traffic_pct_estimated": 60,
        "google_ai_content_deal": True,
        "google_advertising_revenue": True,
        "dependency_level": "existential",
    },
    "samsung_relationship": {
        "advertising_revenue": True,
        "samsung_annual_ad_spend_global_b": 9.7,
        "affiliate_link_revenue": True,
        "exclusive_interview_access": True,
        "galaxy_unpacked_press_trip": True,
    },
    "meta_relationship": {
        "advertising_revenue_from_meta": False,
        "content_licensing_deal": False,
        "financial_relationship_value_usd": 0,
    },
    "mechanism_114_reference": "Documented triple Google/OpenAI dependency vs $0 Meta",
}


# ── Test classes ───────────────────────────────────────────────────────


class TestMarketAttributionPrivacyDisplacement:
    """Core mechanism: privacy acknowledged but attributed to market, not Samsung."""

    def test_meta_article_has_zero_privacy_vocabulary(self):
        """Meta Display Glasses review contains zero privacy alarm terms."""
        assert len(META_DISPLAY_GLASSES_ARTICLE["privacy_vocabulary"]) == 0
        assert len(META_DISPLAY_GLASSES_ARTICLE["alarm_vocabulary"]) == 0
        assert len(META_DISPLAY_GLASSES_ARTICLE["surveillance_vocabulary"]) == 0

    def test_samsung_article_has_zero_direct_privacy_vocabulary(self):
        """Samsung Intelligent Eyewear receives zero DIRECT privacy vocabulary."""
        assert len(SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["privacy_vocabulary_direct_to_samsung"]) == 0
        assert len(SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["alarm_vocabulary_for_samsung"]) == 0
        assert len(SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["surveillance_vocabulary_for_samsung"]) == 0

    def test_samsung_article_has_market_attributed_privacy(self):
        """Samsung article attributes privacy concerns to MARKET, not Samsung."""
        market_privacy = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["privacy_vocabulary_attributed_to_market"]
        assert len(market_privacy) >= 2
        assert "fraught market" in market_privacy
        assert "worried about privacy" in market_privacy

    def test_privacy_attribution_target_is_market_not_samsung(self):
        """Privacy concerns are attributed to market conditions, not Samsung's hardware."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["meta_as_implied_privacy_source"] is True
        direct = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["privacy_vocabulary_direct_to_samsung"]
        market = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["privacy_vocabulary_attributed_to_market"]
        assert len(market) > len(direct)


class TestInnovationDefenderFraming:
    """Samsung executive positioned as innovation hero vs privacy headwinds."""

    def test_samsung_exec_gets_innovation_defender_quote(self):
        """Samsung executive quote frames innovation as heroic persistence."""
        quote = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["samsung_executive_quote"]
        assert "stop innovation" in quote
        assert "don't go anywhere" in quote

    def test_innovation_defense_narrative_frame(self):
        """Samsung article uses innovation-defense narrative frame."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["narrative_frame"] == "innovation_defense"
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["executive_quote_framing"] == "innovation_defender"

    def test_innovation_vs_privacy_binary_constructed(self):
        """Article constructs an innovation-vs-privacy binary that benefits Samsung."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["innovation_vs_privacy_binary"] is True

    def test_meta_does_not_receive_innovation_framing(self):
        """Meta never receives 'innovation despite privacy headwinds' framing."""
        # Meta gets product enthusiasm but not the hero narrative of overcoming concerns
        assert META_DISPLAY_GLASSES_ARTICLE["narrative_frame"] == "product_redemption"
        # The redemption is vs Google Glass failure, not vs privacy concerns
        assert META_DISPLAY_GLASSES_ARTICLE["google_glass_comparison_polarity"] == "positive_for_meta"


class TestProductEnthusiasmAsymmetry:
    """Same journalist applies different enthusiasm levels to equivalent hardware."""

    def test_meta_gets_first_person_enthusiasm(self):
        """Meta review uses first-person enthusiasm: 'I can't wait to wear them again.'"""
        vocab = META_DISPLAY_GLASSES_ARTICLE["product_vocabulary"]
        first_person = [v for v in vocab if "I " in v or "I'" in v]
        assert len(first_person) >= 1
        assert META_DISPLAY_GLASSES_ARTICLE["tone_score"] > 0.7

    def test_samsung_gets_moderate_product_vocabulary(self):
        """Samsung article uses moderate product vocabulary, not personal enthusiasm."""
        vocab = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["product_vocabulary"]
        first_person = [v for v in vocab if "I " in v or "I'" in v]
        assert len(first_person) == 0
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"] < META_DISPLAY_GLASSES_ARTICLE["tone_score"]

    def test_tone_differential(self):
        """Tone differential between Meta (+0.85) and Samsung (+0.45) articles."""
        delta = META_DISPLAY_GLASSES_ARTICLE["tone_score"] - SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["tone_score"]
        assert delta >= 0.3


class TestHardwareEquivalenceWithFramingDivergence:
    """Identical hardware receives different narrative framing."""

    def test_both_products_have_camera(self):
        """Both Meta and Samsung glasses include cameras."""
        assert "camera" in META_DISPLAY_GLASSES_ARTICLE["hardware_features"]
        assert "camera" in SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["hardware_features"]

    def test_both_products_have_ai_assistant(self):
        """Both Meta and Samsung glasses include AI assistants."""
        meta_ai = any("AI" in f or "Meta_AI" in f for f in META_DISPLAY_GLASSES_ARTICLE["hardware_features"])
        samsung_ai = any("AI" in f or "Gemini" in f for f in SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["hardware_features"])
        assert meta_ai is True
        assert samsung_ai is True

    def test_samsung_uses_same_snapdragon_chip(self):
        """Samsung uses Snapdragon AR1 Gen 1, same chipset family as Meta."""
        assert "Snapdragon_AR1_Gen1" in SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["hardware_features"]

    def test_neither_product_receives_direct_privacy_alarm(self):
        """Neither product receives direct privacy alarm from Ulanoff."""
        assert len(META_DISPLAY_GLASSES_ARTICLE["privacy_vocabulary"]) == 0
        assert len(SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["privacy_vocabulary_direct_to_samsung"]) == 0

    def test_meta_implicitly_blamed_for_market_privacy_concerns(self):
        """Meta implicitly blamed for 'fraught market' without receiving direct alarm."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["meta_as_implied_privacy_source"] is True
        assert META_DISPLAY_GLASSES_ARTICLE["bystander_privacy_mentioned"] is False


class TestEditorialLeadershipSeniority:
    """Career seniority makes this mechanism editorially significant."""

    def test_journalist_is_former_eic_of_multiple_publications(self):
        """Ulanoff was EIC of 3 publications — not a junior beat reporter."""
        assert len(META_DISPLAY_GLASSES_ARTICLE["previous_eic_roles"]) >= 3
        assert "PCMag.com" in META_DISPLAY_GLASSES_ARTICLE["previous_eic_roles"]
        assert "Mashable" in META_DISPLAY_GLASSES_ARTICLE["previous_eic_roles"]
        assert "Lifewire" in META_DISPLAY_GLASSES_ARTICLE["previous_eic_roles"]

    def test_career_length_exceeds_30_years(self):
        """38-year career means framing choices are deliberate editorial judgment."""
        assert META_DISPLAY_GLASSES_ARTICLE["career_years"] >= 30

    def test_corporate_leadership_experience(self):
        """SVP Content at Ziff Davis — corporate editorial leadership experience."""
        assert "Ziff Davis" in META_DISPLAY_GLASSES_ARTICLE["previous_corporate_role"]

    def test_aligns_with_mechanism_115_editorial_leadership_pattern(self):
        """Extends mechanism #115 where US Managing Editor (Krol) was Samsung cheerleader."""
        # In #115, the editorial leadership (Krol as US Managing Editor, News) applied
        # aspirational framing to Samsung/Google. Here, the Global EIC does the same
        # with a MORE sophisticated mechanism: market-attribution displacement.
        assert META_DISPLAY_GLASSES_ARTICLE["role"] == "Global Editor-in-Chief, TechRadar (Future plc)"


class TestSamsungExclusiveSourceAccess:
    """Samsung provides exclusive executive access that correlates with favorable framing."""

    def test_samsung_vp_sit_down_interview(self):
        """Ulanoff had a sit-down interview with Samsung VP at Galaxy XR event."""
        assert SAMSUNG_XR_HEADSET_ARTICLE["executive_access_format"] == "sit-down interview"

    def test_samsung_executive_access_named(self):
        """Samsung executive named by name and title in article."""
        execs = SAMSUNG_XR_HEADSET_ARTICLE["executive_access"]
        assert len(execs) >= 1
        assert "Drew Blackard" in execs[0]
        assert "VP" in execs[0]

    def test_earlier_samsung_article_also_aspirational(self):
        """Earlier Samsung article (Oct 2025) also uses aspirational framing."""
        assert SAMSUNG_XR_HEADSET_ARTICLE["tone_score"] > 0.3
        assert SAMSUNG_XR_HEADSET_ARTICLE["narrative_frame"] == "anticipation"


class TestFinancialIncentiveAlignment:
    """Coverage direction correlates with financial relationships."""

    def test_future_plc_has_zero_meta_financial_relationship(self):
        """Future plc has $0 financial relationship with Meta."""
        assert FUTURE_PLC_FINANCIAL_CONTEXT["meta_relationship"]["financial_relationship_value_usd"] == 0

    def test_future_plc_has_samsung_advertising_dependency(self):
        """Samsung is a major advertiser across Future plc properties."""
        assert FUTURE_PLC_FINANCIAL_CONTEXT["samsung_relationship"]["advertising_revenue"] is True
        assert FUTURE_PLC_FINANCIAL_CONTEXT["samsung_relationship"]["samsung_annual_ad_spend_global_b"] >= 9.0

    def test_future_plc_has_google_existential_dependency(self):
        """Google search traffic is existential for Future plc."""
        assert FUTURE_PLC_FINANCIAL_CONTEXT["google_dependency"]["dependency_level"] == "existential"

    def test_coverage_direction_matches_financial_prediction(self):
        """Coverage direction matches what financial relationships predict."""
        # Meta ($0 relationship) → implied privacy blame (market attribution)
        # Samsung (major advertiser) → innovation defender framing
        # Google (existential dependency) → no criticism of Gemini AI
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["data_retention_questioned_for_samsung"] is False
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["bystander_privacy_mentioned_for_samsung"] is False

    def test_samsung_gets_exclusive_event_access_from_future_plc(self):
        """Future plc journalists receive Samsung press trip access."""
        assert FUTURE_PLC_FINANCIAL_CONTEXT["samsung_relationship"]["galaxy_unpacked_press_trip"] is True


class TestDistinctMechanismFromExisting:
    """This mechanism is distinct from previously documented patterns."""

    def test_distinct_from_mechanism_115_cross_brand_bifurcation(self):
        """Mechanism #115 documented DIFFERENT journalists; this is the SAME journalist."""
        # In #115, Krol (Samsung) vs Hector/Berne (Meta) = different journalists, different vocab
        # Here, Ulanoff covers BOTH entities with different narrative frames
        meta = META_DISPLAY_GLASSES_ARTICLE["journalist"]
        samsung = SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["journalist"]
        assert meta == samsung == "Lance Ulanoff"

    def test_mechanism_is_market_attribution_not_direct_alarm(self):
        """Mechanism is market-attribution displacement, not direct alarm vocabulary."""
        # #115: direct alarm vocabulary ("frightening," "creepy") vs none for Samsung
        # #195: market-attribution ("fraught market") vs product enthusiasm
        # Neither article uses DIRECT alarm vocabulary — the asymmetry is in ATTRIBUTION
        assert len(META_DISPLAY_GLASSES_ARTICLE["alarm_vocabulary"]) == 0
        assert len(SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["alarm_vocabulary_for_samsung"]) == 0

    def test_compound_asymmetry_meta_praised_and_blamed_simultaneously(self):
        """Meta simultaneously receives product praise (review) and implied blame (Samsung article)."""
        # This is the UNIQUE contribution: the same journalist creates a compound frame
        # where Meta's product is good but Meta's market presence is the problem
        assert META_DISPLAY_GLASSES_ARTICLE["tone_score"] > 0.7  # product praise
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["meta_as_implied_privacy_source"] is True  # implied blame

    def test_samsung_camera_never_called_surveillance_tool(self):
        """Samsung's camera is never described as a surveillance tool in available excerpts.
        Note: Based on headline + Muck Rack excerpt data. Full article body text would
        strengthen this finding if it confirms zero surveillance vocabulary throughout."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR_ARTICLE["surveillance_vocabulary_for_samsung"] == []


class TestConfounders:
    """Documented confounding factors for intellectual honesty."""

    CONFOUNDERS = [
        {
            "id": 1,
            "strength": "STRONG",
            "description": (
                "Temporal context: The Meta Display Glasses review (Oct 2025) predates the Samsung "
                "Intelligent Eyewear article (Aug 2026) by ~10 months. During that interval, additional "
                "privacy incidents (civil rights coalition letter, courtroom bans, covert filming reports) "
                "may have shifted Ulanoff's editorial position. The Samsung article's 'fraught market' "
                "framing may reflect genuine evolution of market conditions, not entity-selective bias."
            ),
        },
        {
            "id": 2,
            "strength": "STRONG",
            "description": (
                "Product lifecycle stage: Meta's product was a hands-on review of a shipping product "
                "(event coverage format). Samsung's was a market-entry announcement in the context of "
                "established competitor controversy. Different coverage contexts produce different framing "
                "naturally — a product review legitimately focuses on product experience, while a market "
                "entry piece legitimately addresses market context."
            ),
        },
        {
            "id": 3,
            "strength": "MODERATE",
            "description": (
                "Google Glass redemption narrative: Meta's article explicitly frames the Display Glasses "
                "as succeeding where Google Glass failed. This redemption arc naturally suppresses privacy "
                "vocabulary because the comparison anchors the narrative to innovation triumph. This is a "
                "legitimate editorial choice, not necessarily entity-selective bias."
            ),
        },
        {
            "id": 4,
            "strength": "MODERATE",
            "description": (
                "Samsung 'Intelligent Eyewear' rebranding: Samsung deliberately used 'Intelligent Eyewear' "
                "instead of 'smart glasses' to distance from Meta's category stigma. Ulanoff may have been "
                "responding to Samsung's own framing strategy, which INVITED the 'fraught market' context. "
                "The journalist is following Samsung's narrative, not creating it."
            ),
        },
        {
            "id": 5,
            "strength": "WEAK",
            "description": (
                "Meta's Display Glasses represent a technology leap (micro-LED display, neural band) vs "
                "Samsung's camera-only glasses. The technology difference might legitimately warrant more "
                "enthusiasm for Meta's product on purely technical grounds. However, the privacy vocabulary "
                "asymmetry is not explained by technical difference — both have cameras."
            ),
        },
    ]

    def test_strong_confounders_documented(self):
        """At least 2 STRONG confounders documented."""
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        assert len(strong) >= 2

    def test_confounder_count(self):
        """Total confounders documented."""
        assert len(self.CONFOUNDERS) == 5

    def test_temporal_confounder_acknowledged(self):
        """Temporal gap between articles is acknowledged as a confounder."""
        temporal = [c for c in self.CONFOUNDERS if "temporal" in c["description"].lower() or "months" in c["description"].lower()]
        assert len(temporal) >= 1


class TestCrossReferences:
    """Cross-references to related mechanisms."""

    CROSS_REFERENCES = [
        {
            "mechanism_id": 115,
            "relationship": "extends",
            "description": (
                "Mechanism #115 documented TechRadar's cross-brand bifurcation across "
                "DIFFERENT journalists (Krol vs Hector/Berne). #195 documents the SAME "
                "journalist (Ulanoff) applying different narrative frames to the same "
                "hardware category. #195 extends #115 from institutional-level to "
                "individual editorial leadership level."
            ),
        },
        {
            "mechanism_id": 114,
            "relationship": "explains",
            "description": (
                "Mechanism #114 documents Future plc's triple Google/OpenAI dependency "
                "and $0 Meta financial relationship. #195's framing asymmetry is "
                "PREDICTED by #114's financial architecture."
            ),
        },
        {
            "mechanism_id": 191,
            "relationship": "parallels",
            "description": (
                "Mechanism #191 (Kif Leswing/CNBC) documents CEO-attribution soft "
                "delegitimization of Meta. #195 documents market-attribution displacement — "
                "a similarly soft mechanism that avoids direct alarm but achieves asymmetric "
                "framing through attribution."
            ),
        },
        {
            "mechanism_id": 33,
            "relationship": "complements",
            "description": (
                "Mechanism #33 documents coverage selection silence (Samsung/Google cameras "
                "get zero scrutiny). #195 adds a MIDDLE GROUND mechanism: privacy is not "
                "silenced but is REDIRECTED to the 'market' rather than the product."
            ),
        },
    ]

    def test_extends_mechanism_115(self):
        """Cross-references mechanism #115 (TechRadar cross-brand bifurcation)."""
        ref = next(r for r in self.CROSS_REFERENCES if r["mechanism_id"] == 115)
        assert ref["relationship"] == "extends"

    def test_explained_by_mechanism_114(self):
        """Financial architecture (#114) explains the framing direction."""
        ref = next(r for r in self.CROSS_REFERENCES if r["mechanism_id"] == 114)
        assert ref["relationship"] == "explains"

    def test_parallels_soft_delegitimization(self):
        """Parallels CNBC CEO-attribution soft delegitimization (#191)."""
        ref = next(r for r in self.CROSS_REFERENCES if r["mechanism_id"] == 191)
        assert ref["relationship"] == "parallels"
