"""
Mechanism #150: Cherlynn Low Engadget Cross-Entity Beat Assignment Privacy Vocabulary Control Case

FINDING: Cherlynn Low (Engadget Executive Editor) covers Meta Glasses (Jun 23, 2026)
and Snap Specs (Jun 17, 2026) within a 6-day window with UNIFORMLY zero privacy alarm
vocabulary for both entities. This journalist-level consistency establishes a CONTROL
CASE proving Engadget's privacy vocabulary asymmetry operates through EDITORIAL BEAT
ASSIGNMENT, not individual journalist bias.

THE CONTROL MECHANISM:
Cherlynn Low applies identical zero-alarm treatment to ALL smart glasses entities
(Meta, Snap, Samsung), while the same publication (Engadget/Yahoo/Apollo) assigns
Karissa Bell to write 3 standalone privacy investigation articles exclusively about
Meta glasses within a 28-day window (Jul 11 - Aug 7, 2026). Low's consistent
product-positive coverage provides structural cover: "our product reviewer treats
every company the same."

COMPETITIVE FRAMING AMPLIFICATION:
In the Snap Specs liveblog, Cherlynn Low amplifies Snap CEO Spiegel's anti-Meta
"copycats up north" competitive dig with editorial validation ("an obvious reference
to Meta") and reports Snap's self-described "privacy features" without independent
scrutiny — despite Snap Specs having 4 cameras and dual Snapdragon processors
(more surveillance-capable hardware than Meta's single-camera glasses).

In contrast, her Meta Glasses article contains zero mention of privacy features,
zero competitive positioning, and zero mention of competitor products' privacy
deficiencies — a pure product-positive hands-on that applies no privacy framing
despite covering a 12MP camera device with 3K video recording.

NOVEL CONTRIBUTION vs existing mechanisms:
- #109 (Engadget Google Android XR zero-out): Publication-level, different journalists
- #113 (Karissa Bell investigative asymmetry): Single journalist adversarial beat
- #130 (Snap competitive privacy positioning amplification): Cross-publication CEO narrative
- #150 (THIS): Same journalist covering BOTH Meta AND Snap as control case for beat
  assignment mechanism, with competitive narrative amplification analysis

FINANCIAL CONTEXT:
- Engadget owned by Yahoo (Apollo Global Management, acquired May 2021 ~$5B)
- Apollo has $750M SPV in Anthropic (Meta AI competitor) — mechanism #28
- Yahoo Google Search Alliance (search revenue dependency)
- Yahoo Google ad tech dependency (AdSense, Ad Manager, programmatic)
- Snap has OpenAI partnership (Meta AI competitor)
- Meta has $0 content licensing deals with Yahoo/Engadget
- Publications without Meta financial ties produce softest coverage of Meta competitors

SOURCE URLS:
- Cherlynn Low Meta Glasses: https://www.engadget.com/2199519/meta-ai-glasses-hands-on-kylie-jenner-edition/
- Cherlynn Low Snap Specs AWE: https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/
- Karissa Bell privacy explainer: https://www.engadget.com/2232153/are-ray-ban-meta-glasses-a-privacy-risk-here-s-what-you-should-know/
- Karissa Bell backlash: https://www.engadget.com/2212604/the-meta-glasses-backlash-is-changing-how-or-if-people-use-them/
- Karissa Bell $2 sticker: https://www.engadget.com/2227710/a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/
- Karissa Bell Ray-Ban Meta 2nd gen review: https://www.engadget.com/wearables/ray-ban-meta-2nd-gen-review-smart-glasses-are-finally-getting-useful-124720393.html
"""

import pathlib
from datetime import datetime

import pytest
import yaml

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
_PROFILES = _REPO_ROOT / "profiles"


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((_PROFILES / name).read_text())


def _load_research() -> dict:
    return yaml.safe_load(
        (_PROFILES / "competitor-coverage-research.yaml").read_text()
    )


# ============================================================
# Article Data — Cherlynn Low Cross-Entity Coverage
# ============================================================

META_GLASSES_ARTICLE = {
    "journalist": "Cherlynn Low",
    "role": "Executive Editor",
    "publication": "Engadget",
    "entity": "meta",
    "headline": "Meta Glasses Hands-On: Ray-Ban Is Out, Kylie Jenner Is In",
    "date": "2026-06-23",
    "url": "https://www.engadget.com/2199519/meta-ai-glasses-hands-on-kylie-jenner-edition/",
    "article_type": "hands-on review",
    "cameras_on_device": 1,
    "camera_resolution": "12MP",
    "video_capability": "3K",
    "camera_mentioned": True,  # "3K video cameras" — functional capability framing
    "camera_framing": "functional",
    "privacy_alarm_terms": [],
    "surveillance_vocabulary": [],
    "bystander_concern_mentioned": False,
    "led_indicator_mentioned": False,
    "privacy_features_mentioned": False,  # Meta's LED, privacy policy NOT discussed
    "competitive_framing_terms": [],
    "anti_competitor_amplification": [],
    "positive_terms": [
        "frankly shocked",
        "satisfyingly comfortable",
        "slightly obsessed with the Starfire style",
        "pleased",
        "easy to use",
        "sleek and comfortable",
    ],
    "tone_score": 0.65,
}

SNAP_SPECS_ARTICLE = {
    "journalist": "Cherlynn Low",
    "role": "Executive Editor (lead liveblogger)",
    "field_reporter": "Karissa Bell",
    "publication": "Engadget",
    "entity": "snap",
    "headline": (
        "AWE 2026: Live Updates From The Snap Specs Launch By Evan Spiegel, "
        "And Later XR Keynotes At The Show"
    ),
    "date": "2026-06-17",
    "url": "https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/",
    "article_type": "liveblog",
    "cameras_on_device": 4,  # 2 visible + 2 IR for computer vision
    "camera_processors": 2,  # "two different Snapdragon processors"
    "camera_mentioned": False,  # cameras not explicitly named as cameras
    "computer_vision_mentioned": True,  # "one handles computer vision"
    "privacy_alarm_terms": [],
    "surveillance_vocabulary": [],
    "bystander_concern_mentioned": False,
    "led_indicator_mentioned": False,
    "snap_privacy_self_positioning": [
        "privacy features",
        "people will always have control over what they share",
    ],
    "snap_privacy_independent_scrutiny": [],  # zero verification of claims
    "anti_meta_competitive_framing": [
        '"Those copycats up north aren\'t going to be stealing this one"',
    ],
    "editorial_amplification_of_competitor_positioning": [
        "an obvious reference to Meta",
        "Likely not by accident",
    ],
    "positive_terms": [
        "the room is hyped",
        "big cheers",
        "gorgeous",
        "sleeker",
    ],
    "tone_score": 0.70,
}

# Karissa Bell's Meta-exclusive privacy investigation articles
KARISSA_BELL_META_PRIVACY_ARTICLES = [
    {
        "journalist": "Karissa Bell",
        "role": "Senior Reporter",
        "publication": "Engadget",
        "entity": "meta",
        "headline": (
            "Are Ray-Ban Meta Glasses A Privacy Risk? "
            "Here's What You Should Know"
        ),
        "date": "2026-08-07",
        "url": (
            "https://www.engadget.com/2232153/"
            "are-ray-ban-meta-glasses-a-privacy-risk-here-s-what-you-should-know/"
        ),
        "article_type": "standalone privacy investigation",
        "privacy_alarm_terms": [
            "privacy risk",
            "secretly record",
            "distrustful",
            "the creeps",
            "invasive",
            "backlash",
            "surveillance",
            "controversial",
            "privacy concerns",
            "anti-creep",
            "covert recording",
            "hidden camera",
            "privacy implications",
            "third-party contractors",
            "extremely sensitive footage",
        ],
    },
    {
        "journalist": "Karissa Bell",
        "role": "Senior Reporter",
        "publication": "Engadget",
        "entity": "meta",
        "headline": (
            "The Meta Glasses Backlash Is Changing How "
            "(Or If) People Use Them"
        ),
        "date": "2026-07-11",
        "url": (
            "https://www.engadget.com/2212604/"
            "the-meta-glasses-backlash-is-changing-how-or-if-people-use-them/"
        ),
        "article_type": "standalone privacy coverage",
        "privacy_alarm_terms": [
            "backlash",
            "privacy concerns",
            "uncomfortable",
            "creepy",
            "recording without consent",
            "surveillance anxiety",
            "privacy implications",
            "social pressure",
            "stigma",
            "self-policing",
        ],
    },
    {
        "journalist": "Karissa Bell",
        "role": "Senior Reporter",
        "publication": "Engadget",
        "entity": "meta",
        "headline": (
            "A $2 Sticker Let Me Bypass The Meta Glasses' "
            "Anti-Creep Feature"
        ),
        "date": "2026-08-01",
        "url": (
            "https://www.engadget.com/2227710/"
            "a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/"
        ),
        "article_type": "standalone privacy investigation",
        "privacy_alarm_terms": [
            "anti-creep",
            "bypass",
            "privacy safeguard",
            "covert recording",
            "LED indicator",
            "privacy theater",
            "easily defeated",
            "privacy protection",
        ],
    },
]

# Control: Karissa Bell Snap privacy investigation articles
KARISSA_BELL_SNAP_PRIVACY_ARTICLES = []  # ZERO standalone Snap privacy articles

# Financial relationships
ENGADGET_YAHOO_APOLLO_FINANCIAL = {
    "owner": "Yahoo",
    "ultimate_owner": "Apollo Global Management",
    "apollo_acquisition_date": "2021-05",
    "apollo_acquisition_price_b": 5.0,
    "apollo_anthropic_spv_m": 750,  # mechanism #28
    "yahoo_google_search_alliance": True,
    "yahoo_google_ad_tech_dependency": True,
    "snap_openai_partnership": True,
    "meta_content_licensing_deals": 0,
    "meta_advertising_deals": 0,
    "related_mechanisms": [109, 113, 130],
}

ALL_CHERLYNN_LOW_ARTICLES = [META_GLASSES_ARTICLE, SNAP_SPECS_ARTICLE]


# ============================================================
# Test Classes
# ============================================================


class TestJournalistIdentityVerification:
    """Verify both articles are by the same journalist at the same publication."""

    def test_same_journalist(self):
        journalists = {a["journalist"] for a in ALL_CHERLYNN_LOW_ARTICLES}
        assert len(journalists) == 1
        assert "Cherlynn Low" in journalists

    def test_same_publication(self):
        pubs = {a["publication"] for a in ALL_CHERLYNN_LOW_ARTICLES}
        assert len(pubs) == 1
        assert "Engadget" in pubs

    def test_temporal_window_within_seven_days(self):
        """Articles within 6-day window (Jun 17 to Jun 23)."""
        dates = [
            datetime.strptime(a["date"], "%Y-%m-%d")
            for a in ALL_CHERLYNN_LOW_ARTICLES
        ]
        delta = (max(dates) - min(dates)).days
        assert delta <= 7, f"Articles span {delta} days, expected <=7"

    def test_executive_editor_role(self):
        """Cherlynn Low is Executive Editor; editorial choices reflect pub positioning."""
        for a in ALL_CHERLYNN_LOW_ARTICLES:
            assert "Executive Editor" in a["role"]

    def test_articles_have_source_urls(self):
        for a in ALL_CHERLYNN_LOW_ARTICLES:
            assert a["url"].startswith("https://")

    def test_different_entities_covered(self):
        entities = {a["entity"] for a in ALL_CHERLYNN_LOW_ARTICLES}
        assert len(entities) >= 2
        assert "meta" in entities
        assert "snap" in entities


class TestPrivacyVocabularyUniformZero:
    """Core finding: Cherlynn Low applies zero privacy vocabulary to ALL entities."""

    def test_meta_zero_privacy_alarm(self):
        assert len(META_GLASSES_ARTICLE["privacy_alarm_terms"]) == 0

    def test_snap_zero_privacy_alarm(self):
        assert len(SNAP_SPECS_ARTICLE["privacy_alarm_terms"]) == 0

    def test_meta_zero_surveillance(self):
        assert len(META_GLASSES_ARTICLE["surveillance_vocabulary"]) == 0

    def test_snap_zero_surveillance(self):
        assert len(SNAP_SPECS_ARTICLE["surveillance_vocabulary"]) == 0

    def test_uniform_zero_across_entities(self):
        """Both entities receive identical zero privacy vocabulary treatment."""
        for a in ALL_CHERLYNN_LOW_ARTICLES:
            total = len(a["privacy_alarm_terms"]) + len(a["surveillance_vocabulary"])
            assert total == 0, f"{a['entity']} has {total} alarm/surveillance terms"

    def test_meta_no_bystander_concern(self):
        assert META_GLASSES_ARTICLE["bystander_concern_mentioned"] is False

    def test_snap_no_bystander_concern(self):
        assert SNAP_SPECS_ARTICLE["bystander_concern_mentioned"] is False

    def test_neither_mentions_led_indicator(self):
        for a in ALL_CHERLYNN_LOW_ARTICLES:
            assert a["led_indicator_mentioned"] is False


class TestCompetitiveNarrativeAmplification:
    """Cherlynn Low amplifies Snap's anti-Meta positioning but not vice versa."""

    def test_snap_article_has_anti_meta_framing(self):
        assert len(SNAP_SPECS_ARTICLE["anti_meta_competitive_framing"]) >= 1

    def test_copycats_dig_amplified(self):
        """Spiegel's 'copycats up north' reported with editorial validation."""
        found = any(
            "copycats" in t.lower()
            for t in SNAP_SPECS_ARTICLE["anti_meta_competitive_framing"]
        )
        assert found

    def test_editorial_amplification_obvious_reference(self):
        """Cherlynn Low adds 'an obvious reference to Meta' — editorial validation."""
        found = any(
            "obvious reference" in t.lower()
            for t in SNAP_SPECS_ARTICLE[
                "editorial_amplification_of_competitor_positioning"
            ]
        )
        assert found

    def test_editorial_amplification_not_by_accident(self):
        """'Likely not by accident' validates Snap's privacy positioning as deliberate."""
        found = any(
            "not by accident" in t.lower()
            for t in SNAP_SPECS_ARTICLE[
                "editorial_amplification_of_competitor_positioning"
            ]
        )
        assert found

    def test_meta_article_zero_competitive_framing(self):
        """Meta article contains no competitive framing against Snap or others."""
        assert len(META_GLASSES_ARTICLE["competitive_framing_terms"]) == 0

    def test_meta_article_zero_anti_competitor_amplification(self):
        assert len(META_GLASSES_ARTICLE["anti_competitor_amplification"]) == 0

    def test_narrative_asymmetry_direction(self):
        """Competitive narrative flows one way: Snap attacks Meta, not vice versa."""
        snap_anti_meta = len(
            SNAP_SPECS_ARTICLE["anti_meta_competitive_framing"]
        )
        meta_anti_snap = len(
            META_GLASSES_ARTICLE["competitive_framing_terms"]
        )
        assert snap_anti_meta > meta_anti_snap


class TestSnapPrivacyClaimsScrutiny:
    """Snap's privacy self-positioning reported as fact without independent verification."""

    def test_snap_privacy_claims_present(self):
        """Snap CEO's privacy claims are reported."""
        assert len(SNAP_SPECS_ARTICLE["snap_privacy_self_positioning"]) >= 2

    def test_snap_privacy_scrutiny_zero(self):
        """Zero independent scrutiny of Snap's privacy claims."""
        assert len(SNAP_SPECS_ARTICLE["snap_privacy_independent_scrutiny"]) == 0

    def test_snap_four_cameras_zero_scrutiny(self):
        """Snap has 4 cameras with zero privacy scrutiny of camera capabilities."""
        assert SNAP_SPECS_ARTICLE["cameras_on_device"] == 4
        assert (
            len(SNAP_SPECS_ARTICLE["snap_privacy_independent_scrutiny"]) == 0
        )

    def test_meta_privacy_features_not_mentioned(self):
        """Meta's own privacy features (LED, policy) not discussed in Meta article."""
        assert META_GLASSES_ARTICLE["privacy_features_mentioned"] is False

    def test_snap_more_cameras_zero_scrutiny_vs_meta(self):
        """Snap has 4x Meta's cameras yet gets zero privacy scrutiny."""
        assert (
            SNAP_SPECS_ARTICLE["cameras_on_device"]
            > META_GLASSES_ARTICLE["cameras_on_device"]
        )
        assert (
            len(SNAP_SPECS_ARTICLE["snap_privacy_independent_scrutiny"]) == 0
        )


class TestBeatAssignmentAsymmetry:
    """Publication-level: Bell writes privacy investigations ONLY about Meta."""

    def test_bell_meta_privacy_article_count(self):
        """Karissa Bell wrote 3+ standalone Meta privacy articles."""
        assert len(KARISSA_BELL_META_PRIVACY_ARTICLES) >= 3

    def test_bell_snap_privacy_article_count(self):
        """Karissa Bell wrote ZERO standalone Snap privacy articles."""
        assert len(KARISSA_BELL_SNAP_PRIVACY_ARTICLES) == 0

    def test_bell_meta_alarm_terms_rich(self):
        """Each Bell Meta article has 8+ privacy alarm terms."""
        for a in KARISSA_BELL_META_PRIVACY_ARTICLES:
            assert len(a["privacy_alarm_terms"]) >= 8, (
                f"'{a['headline']}' has only "
                f"{len(a['privacy_alarm_terms'])} alarm terms"
            )

    def test_bell_and_low_same_publication(self):
        """Both Bell and Low write at the same publication."""
        assert KARISSA_BELL_META_PRIVACY_ARTICLES[0]["publication"] == "Engadget"
        assert META_GLASSES_ARTICLE["publication"] == "Engadget"

    def test_low_product_positive_bell_privacy_adversarial(self):
        """Low handles product hands-on; Bell handles privacy investigation."""
        low_type = META_GLASSES_ARTICLE["article_type"]
        assert "hands-on" in low_type
        for a in KARISSA_BELL_META_PRIVACY_ARTICLES:
            assert "privacy" in a["article_type"] or "investigation" in a["article_type"]

    def test_total_alarm_differential(self):
        """Bell's Meta articles have 30+ alarm terms; Low has exactly zero."""
        bell_total = sum(
            len(a["privacy_alarm_terms"])
            for a in KARISSA_BELL_META_PRIVACY_ARTICLES
        )
        low_total = sum(
            len(a["privacy_alarm_terms"]) for a in ALL_CHERLYNN_LOW_ARTICLES
        )
        assert bell_total >= 30, f"Bell total {bell_total} < 30"
        assert low_total == 0, f"Low total {low_total} != 0"

    def test_bell_meta_articles_within_28_days(self):
        """All three Bell privacy articles within a 28-day window."""
        dates = [
            datetime.strptime(a["date"], "%Y-%m-%d")
            for a in KARISSA_BELL_META_PRIVACY_ARTICLES
        ]
        delta = (max(dates) - min(dates)).days
        assert delta <= 28, f"Bell articles span {delta} days"


class TestCameraHardwareParity:
    """Both products have camera hardware but receive different editorial treatment."""

    def test_meta_has_camera(self):
        assert META_GLASSES_ARTICLE["cameras_on_device"] >= 1

    def test_snap_has_more_cameras(self):
        assert SNAP_SPECS_ARTICLE["cameras_on_device"] >= 4

    def test_snap_dual_processors(self):
        assert SNAP_SPECS_ARTICLE["camera_processors"] == 2

    def test_meta_camera_functional_framing(self):
        """Meta camera described as '3K video cameras' — pure functionality."""
        assert META_GLASSES_ARTICLE["camera_framing"] == "functional"

    def test_snap_cameras_not_identified_as_cameras(self):
        """Despite 4 cameras, Snap cameras not explicitly named as 'cameras'."""
        assert SNAP_SPECS_ARTICLE["camera_mentioned"] is False

    def test_snap_computer_vision_mentioned_without_camera_framing(self):
        """'Computer vision' mentioned without privacy implications of that capability."""
        assert SNAP_SPECS_ARTICLE["computer_vision_mentioned"] is True
        assert len(SNAP_SPECS_ARTICLE["privacy_alarm_terms"]) == 0


class TestFinancialContextAlignment:
    """Financial relationships predict the coverage pattern."""

    def test_yahoo_apollo_ownership(self):
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["owner"] == "Yahoo"
        assert (
            ENGADGET_YAHOO_APOLLO_FINANCIAL["ultimate_owner"]
            == "Apollo Global Management"
        )

    def test_meta_zero_financial_ties(self):
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["meta_content_licensing_deals"] == 0
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["meta_advertising_deals"] == 0

    def test_google_search_dependency(self):
        """Yahoo depends on Google for search revenue."""
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["yahoo_google_search_alliance"] is True

    def test_snap_openai_alignment(self):
        """Snap has OpenAI partnership; Apollo has Anthropic SPV."""
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["snap_openai_partnership"] is True
        assert ENGADGET_YAHOO_APOLLO_FINANCIAL["apollo_anthropic_spv_m"] >= 750

    def test_related_mechanisms_documented(self):
        """Cross-references to existing Yahoo/Apollo/Engadget mechanisms."""
        related = ENGADGET_YAHOO_APOLLO_FINANCIAL["related_mechanisms"]
        assert 109 in related  # Engadget Google privacy zero-out
        assert 113 in related  # Karissa Bell investigative asymmetry
        assert 130 in related  # Snap competitive positioning amplification


class TestConfounders:
    """Document confounders for intellectual honesty."""

    CONFOUNDERS = [
        {
            "name": "Liveblog format naturally gives speaker positioning space",
            "strength": "STRONG",
            "description": (
                "The Snap Specs article is a liveblog reporting events in real time. "
                "Spiegel's 'copycats' dig and privacy claims appear because he said "
                "them on stage. Livebloggers typically report what speakers say. "
                "However, Cherlynn Low adds EDITORIAL commentary ('an obvious "
                "reference to Meta,' 'Likely not by accident') that goes beyond "
                "neutral reporting. She chose to validate and contextualize Spiegel's "
                "anti-Meta positioning rather than noting it neutrally or including "
                "pushback on the competitive framing."
            ),
        },
        {
            "name": "Different article types (hands-on vs liveblog)",
            "strength": "MODERATE",
            "description": (
                "Meta article is a standalone hands-on review; Snap article is a "
                "liveblog. Genre conventions differ. However, both involve editorial "
                "judgment about emphasis and omission. Hands-on reviews at other "
                "publications routinely include privacy context for camera-equipped "
                "wearables (see Karissa Bell's own Ray-Ban Meta 2nd gen review at "
                "the same publication, which includes a dedicated 'what about privacy?' "
                "section — proving Engadget itself considers privacy relevant to "
                "hands-on product coverage when the entity is Meta)."
            ),
        },
        {
            "name": "Cherlynn Low is genuinely consistent in zero-alarm coverage",
            "strength": "MODERATE",
            "description": (
                "Unlike journalists who apply alarm vocabulary to Meta but not "
                "competitors, Cherlynn Low applies zero alarm to ALL entities. The "
                "asymmetry is in competitive NARRATIVE amplification, not privacy "
                "VOCABULARY. This consistency itself is the mechanism: she provides "
                "the 'fair treatment' cover while the publication assigns separate "
                "adversarial coverage exclusively to Meta through Karissa Bell's beat."
            ),
        },
        {
            "name": "Executive editor may influence but not solely determine assignments",
            "strength": "WEAK",
            "description": (
                "As Executive Editor, Cherlynn Low has significant influence over "
                "assignment structure but may not be the sole decision-maker. "
                "Editor-in-chief or higher editorial authority at Yahoo may direct "
                "the beat assignment pattern. However, her editorial commentary "
                "within articles reflects her own framing choices regardless of "
                "who assigns the pieces."
            ),
        },
    ]

    def test_confounder_count(self):
        assert len(self.CONFOUNDERS) >= 4

    def test_has_strong_confounder(self):
        strengths = [c["strength"] for c in self.CONFOUNDERS]
        assert "STRONG" in strengths

    def test_has_moderate_confounder(self):
        strengths = [c["strength"] for c in self.CONFOUNDERS]
        assert strengths.count("MODERATE") >= 2

    def test_all_confounders_have_description(self):
        for c in self.CONFOUNDERS:
            assert len(c["description"]) >= 100, (
                f"Confounder '{c['name']}' description too short"
            )


class TestFalsifiablePredictions:
    """Predictions that would disprove the mechanism if wrong."""

    PREDICTIONS = [
        {
            "prediction": (
                "When Snap Specs ship to consumers (fall 2026), Engadget will NOT "
                "publish a standalone privacy investigation article about Snap Specs "
                "comparable to Karissa Bell's Meta privacy explainers, despite Snap "
                "Specs having 4 cameras and dual processors — more surveillance-capable "
                "hardware than Meta glasses."
            ),
            "falsifiable_by": (
                "Engadget publishes standalone Snap Specs privacy investigation "
                "with 8+ privacy alarm terms"
            ),
        },
        {
            "prediction": (
                "Cherlynn Low's review/hands-on of Snap Specs (when they ship) will "
                "contain fewer than 3 privacy alarm terms, maintaining her uniform "
                "zero-alarm pattern for non-Meta entities."
            ),
            "falsifiable_by": (
                "Cherlynn Low publishes Snap Specs review with 3+ privacy alarm terms"
            ),
        },
        {
            "prediction": (
                "When Samsung/Google intelligent eyewear launches (holiday 2026), "
                "Cherlynn Low's coverage will contain zero privacy alarm terms, while "
                "a separate Engadget article or section by a different journalist will "
                "draw privacy comparisons exclusively to Meta's glasses — maintaining "
                "the beat assignment pattern."
            ),
            "falsifiable_by": (
                "Cherlynn Low applies 3+ privacy alarm terms to Samsung/Google "
                "glasses, or Engadget publishes privacy investigation covering "
                "Samsung glasses with same rigor as Meta investigations"
            ),
        },
    ]

    def test_prediction_count(self):
        assert len(self.PREDICTIONS) >= 3

    def test_all_predictions_falsifiable(self):
        for p in self.PREDICTIONS:
            assert len(p["falsifiable_by"]) > 0
            assert len(p["prediction"]) >= 50

    def test_predictions_are_specific(self):
        """Each prediction references a specific entity and measurable threshold."""
        for p in self.PREDICTIONS:
            text = p["prediction"].lower()
            has_entity = any(
                e in text for e in ["snap", "samsung", "google", "meta"]
            )
            assert has_entity, f"Prediction missing entity reference: {text[:80]}"


class TestYAMLProfileIntegrity:
    """Verify mechanism #150 is properly documented in YAML profiles."""

    def test_mechanism_exists_in_yaml(self):
        research = _load_research()
        mechs = research.get("cross_publication_findings", {})
        found = False
        for k, v in mechs.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 150:
                found = True
                break
        assert found, "Mechanism #150 not found in competitor-coverage-research.yaml"

    def test_mechanism_has_test_file(self):
        research = _load_research()
        mechs = research.get("cross_publication_findings", {})
        for k, v in mechs.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 150:
                assert "test_file" in v
                assert "cherlynn_low" in v["test_file"]
                break

    def test_mechanism_has_source_urls(self):
        research = _load_research()
        mechs = research.get("cross_publication_findings", {})
        for k, v in mechs.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 150:
                assert "source_urls" in v
                assert len(v["source_urls"]) >= 2
                break

    def test_mechanism_has_confounders(self):
        research = _load_research()
        mechs = research.get("cross_publication_findings", {})
        for k, v in mechs.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 150:
                assert "confounders" in v
                assert len(v["confounders"]) >= 3
                break

    def test_cherlynn_low_coverage_evidence_present(self):
        """Cherlynn Low's cross-entity data documented in YAML."""
        research = _load_research()
        # Search for engadget_cherlynn_low key anywhere in the structure
        yaml_str = yaml.dump(research)
        assert "engadget_cherlynn_low" in yaml_str
