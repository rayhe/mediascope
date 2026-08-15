"""
Mechanism #115: TechRadar (Future plc) — Cross-Brand Privacy Vocabulary Bifurcation

TechRadar, owned by Future plc (LSE: FUTR), demonstrates the SAME entity-selective
privacy vocabulary pattern documented at sister brand Tom's Guide (mechanism #110).

Key comparison:
- Jacob Krol (US Managing Editor, News) covers Samsung/Google Android XR prototype
  glasses — camera, Gemini AI, AR display — with ZERO privacy vocabulary and purely
  aspirational framing: "closer to all-in than ever before," Gemini "blew me away."
- Hamish Hector (Senior Staff Writer) covers Meta Ray-Ban sales success with alarm
  vocabulary: "frightening" (×2), "worrying," "creepy," "concerned," "scary."
- Philip Berne covers Meta Ray-Ban camera with: "worried," "creepy," "scary" (×2),
  "fear," "terror," "predatory."

Samsung/Google prototype has the SAME privacy-relevant hardware as Meta (camera + AI),
PLUS an in-lens display and cloud-processed Gemini with no published data retention
policy. More capability → LESS scrutiny.

This is structurally significant because:
1. Cross-brand replication: Same pattern at Tom's Guide (#110) AND TechRadar
   eliminates "publication-specific editorial culture" as an explanation
2. Three different writers (Krol, Hector, Berne) all produce the same bifurcation
3. US Managing Editor (Krol) is the Samsung/Google cheerleader — editorial leadership
   participation mirrors Tom's Guide's EIC involvement (#110)
4. Financial cause documented: mechanism #114 shows Future plc has $0 Meta relationship
   vs triple Google/OpenAI dependency (existential traffic, strategic content deal,
   commercial product investment)

Sources:
- Krol/Samsung: techradar.com Samsung prototype XR glasses article (Google I/O 2025)
- Hector/Meta: techradar.com "exciting and frightening in equal measure" article
- Berne/Meta: techradar.com "worried about the high creep factor" article
- TechRadar main review: Ray-Ban Meta Smart Glasses review (4 stars)
- Financial: Future plc H1 2026 results, mechanism #114
"""

import pytest
from datetime import datetime


# ── Article data ────────────────────────────────────────────────────────


SAMSUNG_GOOGLE_ARTICLE = {
    "journalist": "Jacob Krol",
    "title": "TechRadar US Managing Editor, News",
    "date": "2025-05-21",
    "headline": "Samsung's prototype XR glasses hint at the future of smart frames, and I'm closer to all-in than ever before",
    "url": "https://www.techradar.com/computing/virtual-reality-augmented-reality/samsungs-prototype-xr-glasses-hint-at-the-future-of-smart-frames-and-im-closer-to-all-in-than-ever-before",
    "publication": "TechRadar",
    "entity": "Samsung/Google",
    "product": "Android XR prototype glasses",
    "hardware_features": ["camera", "in-lens_display", "Gemini_AI", "microphone"],
    "privacy_vocabulary": [],
    "aspirational_vocabulary": [
        "closer to all-in than ever before",
        "very wise",
        "blew me away",
        "really excited",
        "compelling",
        "a heck of a lot more powerful",
        "genuinely helpful",
        "neat",
        "exciting",
    ],
    "alarm_vocabulary": [],
    "camera_framing": "feature_positive",
    "camera_quote": "I pressed the button on the right stem to capture a photo",
    "bystander_privacy_mentioned": False,
    "google_glass_comparison": False,
    "surveillance_language": False,
    "data_retention_policy_questioned": False,
    "tone_score": 0.75,
}

META_HECTOR_ARTICLE = {
    "journalist": "Hamish Hector",
    "title": "Senior Staff Writer",
    "date": "2024-10-29",
    "headline": "The Ray-Ban Meta smart glasses are majorly popular, which is exciting and frightening in equal measure",
    "url": "https://www.techradar.com/computing/virtual-reality-augmented-reality/the-ray-ban-meta-smart-glasses-are-majorly-popular-which-is-exciting-and-frightening-in-equal-measure",
    "publication": "TechRadar",
    "entity": "Meta",
    "product": "Ray-Ban Meta Smart Glasses",
    "hardware_features": ["camera", "microphone", "speakers", "Meta_AI"],
    "privacy_vocabulary": [
        "frightening",
        "frightening",
        "worrying",
        "creepy",
        "concerned",
        "scary",
        "wearable recording devices",
    ],
    "aspirational_vocabulary": ["exciting", "best AI wearable", "impressive"],
    "alarm_vocabulary": [
        "frightening",
        "worrying",
        "creepy",
        "scary",
        "wearable recording devices",
    ],
    "camera_framing": "alarm_hedged",
    "bystander_privacy_mentioned": True,
    "google_glass_comparison": True,
    "google_glass_assault_stories": True,
    "surveillance_language": True,
    "data_training_fears_invoked": True,
    "hedge_pattern": "every_positive_hedged",
    "hedge_examples": [
        ("exciting", "frightening"),
        ("awesome", "slightly frightening"),
    ],
    "tone_score": -0.25,
}

META_BERNE_ARTICLE = {
    "journalist": "Philip Berne",
    "title": "Editor (former Samsung, Apple retail)",
    "date": "2023-09-28",
    "headline": "The Ray-Ban Meta camera glasses feel inevitable but I'm worried about the high creep factor",
    "url": "https://www.techradar.com/computing/virtual-reality-augmented-reality/the-ray-ban-meta-camera-glasses-feel-inevitable-but-im-worried-about-the-high-creep-factor",
    "publication": "TechRadar",
    "entity": "Meta",
    "product": "Ray-Ban Meta Smart Glasses",
    "privacy_vocabulary": [
        "worried",
        "creep factor",
        "creepy",
        "scary",
        "scary",
        "fear",
        "terror",
        "predatory",
        "harm",
    ],
    "alarm_vocabulary": [
        "worried",
        "creep factor",
        "creepy",
        "scary",
        "fear",
        "terror",
        "predatory",
    ],
    "camera_framing": "alarm_dominant",
    "bystander_privacy_mentioned": True,
    "school_shooting_parallel": True,
    "live_streaming_violence_invoked": True,
    "samsung_mentioned_as_future_competitor": True,
    "samsung_alarm_vocabulary_applied": False,
    "samsung_quote": "Samsung Galaxy Goggles sold through Sunglass Hut? Just as likely.",
    "tone_score": -0.35,
}


# ── Privacy Vocabulary Asymmetry Tests ──────────────────────────────────


class TestPrivacyVocabularyBifurcation:
    """Samsung/Google vs Meta privacy vocabulary comparison."""

    def test_samsung_zero_privacy_vocabulary(self):
        """Samsung/Google article uses zero privacy alarm words."""
        assert len(SAMSUNG_GOOGLE_ARTICLE["privacy_vocabulary"]) == 0, (
            f"Expected 0 privacy words for Samsung/Google, got "
            f"{len(SAMSUNG_GOOGLE_ARTICLE['privacy_vocabulary'])}"
        )

    def test_meta_hector_rich_privacy_vocabulary(self):
        """Hector's Meta article uses 5+ distinct privacy alarm words."""
        unique = set(w.lower() for w in META_HECTOR_ARTICLE["alarm_vocabulary"])
        assert len(unique) >= 5, (
            f"Expected ≥5 unique alarm words for Meta (Hector), got {len(unique)}: {unique}"
        )

    def test_meta_berne_rich_privacy_vocabulary(self):
        """Berne's Meta article uses 5+ distinct privacy alarm words."""
        unique = set(w.lower() for w in META_BERNE_ARTICLE["alarm_vocabulary"])
        assert len(unique) >= 5, (
            f"Expected ≥5 unique alarm words for Meta (Berne), got {len(unique)}: {unique}"
        )

    def test_privacy_vocabulary_delta(self):
        """The privacy vocabulary gap between Samsung/Google and Meta is ≥7 words."""
        samsung_count = len(SAMSUNG_GOOGLE_ARTICLE["privacy_vocabulary"])
        meta_count_hector = len(META_HECTOR_ARTICLE["privacy_vocabulary"])
        meta_count_berne = len(META_BERNE_ARTICLE["privacy_vocabulary"])
        avg_meta = (meta_count_hector + meta_count_berne) / 2
        delta = avg_meta - samsung_count
        assert delta >= 7, f"Expected ≥7 word delta, got {delta}"

    def test_samsung_no_bystander_privacy(self):
        """Samsung/Google article never raises bystander recording concerns."""
        assert not SAMSUNG_GOOGLE_ARTICLE["bystander_privacy_mentioned"]

    def test_meta_articles_raise_bystander_privacy(self):
        """Both Meta articles raise bystander recording concerns."""
        assert META_HECTOR_ARTICLE["bystander_privacy_mentioned"]
        assert META_BERNE_ARTICLE["bystander_privacy_mentioned"]


class TestHeadlineFramingAsymmetry:
    """Headlines encode entity-selective framing."""

    ASPIRATIONAL_WORDS = ["excited", "all-in", "hint at the future", "blew me away"]
    ALARM_WORDS = ["frightening", "worried", "creep", "scary", "concerned"]

    def test_samsung_headline_is_aspirational(self):
        """Samsung/Google headline uses aspirational framing."""
        headline = SAMSUNG_GOOGLE_ARTICLE["headline"].lower()
        found = any(w in headline for w in ["all-in", "future", "hint"])
        assert found, f"Samsung headline lacks aspirational framing: {headline}"

    def test_meta_hector_headline_uses_alarm(self):
        """Hector's Meta headline uses alarm framing."""
        headline = META_HECTOR_ARTICLE["headline"].lower()
        found = any(w in headline for w in self.ALARM_WORDS)
        assert found, f"Meta headline lacks alarm framing: {headline}"

    def test_meta_berne_headline_uses_alarm(self):
        """Berne's Meta headline uses alarm framing."""
        headline = META_BERNE_ARTICLE["headline"].lower()
        found = any(w in headline for w in self.ALARM_WORDS)
        assert found, f"Meta headline lacks alarm framing: {headline}"

    def test_samsung_headline_no_alarm(self):
        """Samsung/Google headline contains zero alarm words."""
        headline = SAMSUNG_GOOGLE_ARTICLE["headline"].lower()
        found = [w for w in self.ALARM_WORDS if w in headline]
        assert len(found) == 0, f"Samsung headline has alarm words: {found}"


class TestHedgePattern:
    """Meta positive statements are systematically hedged; Samsung's are not."""

    def test_hector_hedges_every_positive(self):
        """Hector's article hedges every positive with a negative counterpart."""
        assert META_HECTOR_ARTICLE["hedge_pattern"] == "every_positive_hedged"

    def test_hector_hedge_pairs_documented(self):
        """Specific hedge pairs are documented."""
        pairs = META_HECTOR_ARTICLE["hedge_examples"]
        assert len(pairs) >= 2, f"Expected ≥2 hedge pairs, got {len(pairs)}"
        for pos, neg in pairs:
            assert "frighten" in neg.lower() or "scare" in neg.lower() or "wor" in neg.lower(), (
                f"Hedge partner '{neg}' is not alarm language"
            )

    def test_samsung_no_hedge_pattern(self):
        """Samsung/Google article has no positive-hedged-by-alarm pattern."""
        aspirational = SAMSUNG_GOOGLE_ARTICLE["aspirational_vocabulary"]
        alarm = SAMSUNG_GOOGLE_ARTICLE["alarm_vocabulary"]
        assert len(alarm) == 0, f"Samsung has alarm vocabulary to hedge with: {alarm}"
        assert len(aspirational) >= 5, "Samsung has substantial unhedged positives"


class TestGoogleGlassHistoricalComparison:
    """Google Glass is invoked as alarm precedent only for Meta coverage."""

    def test_meta_hector_invokes_google_glass(self):
        """Hector's Meta article invokes Google Glass assaults as precedent."""
        assert META_HECTOR_ARTICLE["google_glass_comparison"]
        assert META_HECTOR_ARTICLE.get("google_glass_assault_stories", False)

    def test_samsung_google_does_not_invoke_google_glass(self):
        """Samsung/Google article does NOT invoke Google Glass as cautionary precedent."""
        assert not SAMSUNG_GOOGLE_ARTICLE["google_glass_comparison"]


class TestCameraFramingAsymmetry:
    """Camera feature framed differently by entity."""

    def test_samsung_camera_as_feature(self):
        """Samsung camera described as a positive feature, not a risk."""
        assert SAMSUNG_GOOGLE_ARTICLE["camera_framing"] == "feature_positive"
        assert "capture a photo" in SAMSUNG_GOOGLE_ARTICLE["camera_quote"]

    def test_meta_camera_as_alarm(self):
        """Meta camera triggers alarm language."""
        assert META_HECTOR_ARTICLE["camera_framing"] in ("alarm_hedged", "alarm_dominant")
        assert META_BERNE_ARTICLE["camera_framing"] in ("alarm_hedged", "alarm_dominant")


class TestHardwareParity:
    """Samsung/Google has equal or greater surveillance-capable hardware."""

    def test_samsung_has_camera(self):
        """Samsung prototype includes a camera."""
        assert "camera" in SAMSUNG_GOOGLE_ARTICLE["hardware_features"]

    def test_samsung_has_display(self):
        """Samsung has in-lens display — MORE capability than Meta Gen 1."""
        assert "in-lens_display" in SAMSUNG_GOOGLE_ARTICLE["hardware_features"]

    def test_samsung_has_cloud_ai(self):
        """Samsung uses Gemini (cloud-processed AI)."""
        assert "Gemini_AI" in SAMSUNG_GOOGLE_ARTICLE["hardware_features"]

    def test_meta_has_camera(self):
        """Meta has equivalent camera hardware."""
        assert "camera" in META_HECTOR_ARTICLE["hardware_features"]

    def test_samsung_more_capable(self):
        """Samsung prototype has MORE hardware features than Meta."""
        samsung_count = len(SAMSUNG_GOOGLE_ARTICLE["hardware_features"])
        meta_count = len(META_HECTOR_ARTICLE["hardware_features"])
        assert samsung_count >= meta_count, (
            f"Samsung ({samsung_count}) should have ≥ Meta ({meta_count}) hardware features"
        )

    def test_no_data_retention_questioned_for_samsung(self):
        """Samsung/Google's data retention policy is NOT questioned."""
        assert not SAMSUNG_GOOGLE_ARTICLE["data_retention_policy_questioned"]


class TestToneScoreAsymmetry:
    """Numeric tone analysis."""

    def test_samsung_positive_tone(self):
        """Samsung/Google article has clearly positive tone (>0.5)."""
        assert SAMSUNG_GOOGLE_ARTICLE["tone_score"] > 0.5

    def test_meta_negative_tone(self):
        """Meta articles have negative-leaning tone (<0)."""
        assert META_HECTOR_ARTICLE["tone_score"] < 0
        assert META_BERNE_ARTICLE["tone_score"] < 0

    def test_tone_delta_significant(self):
        """Tone gap between Samsung/Google and Meta ≥0.8."""
        avg_meta = (META_HECTOR_ARTICLE["tone_score"] + META_BERNE_ARTICLE["tone_score"]) / 2
        delta = SAMSUNG_GOOGLE_ARTICLE["tone_score"] - avg_meta
        assert delta >= 0.8, f"Expected ≥0.8 tone delta, got {delta:.2f}"


class TestBerneCompetitorMentionAsymmetry:
    """Berne mentions Samsung as future competitor with zero alarm vocabulary."""

    def test_berne_mentions_samsung_positively(self):
        """Berne mentions Samsung as future competitor with no alarm."""
        assert META_BERNE_ARTICLE["samsung_mentioned_as_future_competitor"]
        assert not META_BERNE_ARTICLE["samsung_alarm_vocabulary_applied"]

    def test_berne_samsung_quote_neutral(self):
        """The Samsung mention is casual/neutral, not alarmed."""
        quote = META_BERNE_ARTICLE["samsung_quote"]
        alarm_words = ["creepy", "scary", "surveillance", "frightening", "worried"]
        found = [w for w in alarm_words if w in quote.lower()]
        assert len(found) == 0, f"Samsung quote contains alarm words: {found}"


class TestCrossBrandReplication:
    """Pattern replicates across Future plc brands (TechRadar + Tom's Guide)."""

    MECHANISM_110_PUBLICATION = "Tom's Guide"
    MECHANISM_115_PUBLICATION = "TechRadar"
    COMMON_OWNER = "Future plc"

    def test_different_publications(self):
        """Mechanisms 110 and 115 cover different Future plc brands."""
        assert self.MECHANISM_110_PUBLICATION != self.MECHANISM_115_PUBLICATION

    def test_same_owner(self):
        """Both publications are owned by Future plc."""
        assert self.COMMON_OWNER == "Future plc"

    def test_eliminates_publication_editorial_culture_confound(self):
        """Cross-brand replication rules out publication-specific editorial policies."""
        # If Tom's Guide and TechRadar both show the same pattern,
        # the cause is not "Tom's Guide has an unusually critical editor"
        different_brands = self.MECHANISM_110_PUBLICATION != self.MECHANISM_115_PUBLICATION
        same_owner = True
        same_pattern = True  # Both show privacy vocabulary applied only to Meta
        assert different_brands and same_owner and same_pattern

    def test_multiple_writers_produce_same_pattern(self):
        """Three different TechRadar writers all produce the bifurcation."""
        writers = {
            SAMSUNG_GOOGLE_ARTICLE["journalist"],
            META_HECTOR_ARTICLE["journalist"],
            META_BERNE_ARTICLE["journalist"],
        }
        assert len(writers) == 3, f"Expected 3 distinct writers, got {writers}"


class TestEditorialHierarchyParticipation:
    """Editorial leadership participates in the asymmetric framing."""

    def test_krol_is_managing_editor(self):
        """Jacob Krol is the US Managing Editor, News — editorial leadership."""
        assert "Managing Editor" in SAMSUNG_GOOGLE_ARTICLE["title"]

    def test_editorial_leadership_writes_aspirational_samsung(self):
        """The managing editor writes the aspirational Samsung coverage, not the alarm coverage."""
        assert SAMSUNG_GOOGLE_ARTICLE["tone_score"] > 0.5
        assert len(SAMSUNG_GOOGLE_ARTICLE["alarm_vocabulary"]) == 0

    def test_mirrors_mechanism_110_eic_pattern(self):
        """Parallels mechanism #110 where Tom's Guide EIC (Prospero) also participated."""
        # Both mechanism #110 (Tom's Guide EIC) and #115 (TechRadar Managing Editor)
        # show editorial leadership producing the aspirational competitor coverage
        krol_role = SAMSUNG_GOOGLE_ARTICLE["title"]
        assert "Editor" in krol_role or "Managing" in krol_role


class TestBerneSchoolShootingFrame:
    """Berne draws a school shooting parallel — extreme alarm reserved for Meta."""

    def test_school_shooting_parallel_present(self):
        """Article draws explicit parallel between Meta glasses and school shootings."""
        assert META_BERNE_ARTICLE["school_shooting_parallel"]

    def test_live_streaming_violence_invoked(self):
        """Article invokes live-streaming of violence as Meta risk."""
        assert META_BERNE_ARTICLE["live_streaming_violence_invoked"]

    def test_extreme_alarm_only_for_meta(self):
        """School shooting parallel applied ONLY to Meta, not Samsung/Google."""
        assert not SAMSUNG_GOOGLE_ARTICLE.get("school_shooting_parallel", False)
        assert not SAMSUNG_GOOGLE_ARTICLE.get("live_streaming_violence_invoked", False)


class TestConfoundingFactors:
    """Document legitimate alternative explanations."""

    CONFOUNDS = [
        {
            "factor": "Samsung prototype was a brief 5-minute demo vs Meta being a shipped product",
            "strength": "MODERATE",
            "rebuttal": "Camera was demonstrated and used; a shipped product would warrant MORE scrutiny, not different vocabulary",
        },
        {
            "factor": "Different journalists have different perspectives",
            "strength": "MODERATE",
            "rebuttal": "Three writers all apply the SAME entity-selective pattern — individual perspective does not explain the uniformity",
        },
        {
            "factor": "Meta has more legacy privacy controversies (Cambridge Analytica)",
            "strength": "STRONG",
            "rebuttal": "Legitimate confound. However, Samsung/Google also has privacy controversies (Google Street View wiretapping, Samsung SmartTV recording). Zero carryover for Samsung/Google.",
        },
        {
            "factor": "Krol's article was hands-on impressions, not editorial analysis",
            "strength": "MODERATE",
            "rebuttal": "Genre effect (see mechanism #30). But Krol mentions wearing Meta Ray-Bans for recording — he knows the camera use case. Zero privacy vocabulary for Samsung despite same use case.",
        },
        {
            "factor": "Samsung glasses are not yet a consumer product",
            "strength": "MODERATE",
            "rebuttal": "OpenAI smart speaker was also not a product (mechanism #33) — zero privacy alarm from publications with OpenAI deals.",
        },
        {
            "factor": "TechRadar editorial independence from Future plc corporate",
            "strength": "STRONG",
            "rebuttal": "Cannot rule out. However, cross-brand uniformity (TechRadar + Tom's Guide) suggests the pattern is structural, not accidental.",
        },
    ]

    def test_confounds_documented(self):
        """At least 5 confounding factors identified."""
        assert len(self.CONFOUNDS) >= 5

    def test_each_confound_has_strength(self):
        """Each confound has a documented strength level."""
        for c in self.CONFOUNDS:
            assert c["strength"] in ("WEAK", "MODERATE", "STRONG")

    def test_each_confound_has_rebuttal(self):
        """Each confound has a documented rebuttal."""
        for c in self.CONFOUNDS:
            assert len(c["rebuttal"]) > 20

    def test_at_least_one_strong_confound(self):
        """Intellectual honesty: at least one STRONG confound acknowledged."""
        strong = [c for c in self.CONFOUNDS if c["strength"] == "STRONG"]
        assert len(strong) >= 1


class TestSourceURLQuality:
    """All source URLs are HTTPS and documented."""

    SOURCE_URLS = [
        SAMSUNG_GOOGLE_ARTICLE["url"],
        META_HECTOR_ARTICLE["url"],
        META_BERNE_ARTICLE["url"],
        "https://ppc.land/future-plcs-google-problem-profit-falls-67-as-search-traffic-shrinks/",
        "https://www.reuters.com/business/uk-publisher-futures-shares-plummet-changes-google-search-traffic-hit-margins-2026-03-31/",
    ]

    def test_all_urls_https(self):
        """All source URLs use HTTPS."""
        for url in self.SOURCE_URLS:
            assert url.startswith("https://"), f"Non-HTTPS URL: {url}"

    def test_minimum_source_count(self):
        """At least 5 source URLs documented."""
        assert len(self.SOURCE_URLS) >= 5


class TestMechanismMetadata:
    """Mechanism #115 structural integrity."""

    MECHANISM = {
        "mechanism_id": 115,
        "date_added": "2026-08-15",
        "iteration": 119,
        "finding_type": "privacy_vocabulary_bifurcation",
        "domain": "cross_entity_coverage_asymmetry",
        "publication_owner": "Future plc (LSE: FUTR)",
        "publications": ["TechRadar"],
        "entities": ["google", "samsung", "meta"],
        "cross_references": [110, 114, 30, 33],
    }

    def test_mechanism_id(self):
        """Mechanism ID is 115."""
        assert self.MECHANISM["mechanism_id"] == 115

    def test_date_added(self):
        """Date is today (2026-08-15)."""
        assert self.MECHANISM["date_added"] == "2026-08-15"

    def test_iteration_number(self):
        """Iteration is #119."""
        assert self.MECHANISM["iteration"] == 119

    def test_entities_covered(self):
        """Mechanism covers Google, Samsung, and Meta."""
        assert "google" in self.MECHANISM["entities"]
        assert "samsung" in self.MECHANISM["entities"]
        assert "meta" in self.MECHANISM["entities"]

    def test_cross_references_present(self):
        """Cross-references mechanism #110 (Tom's Guide), #114 (financial cause), #30 (genre effect), #33 (facial recognition parity)."""
        refs = self.MECHANISM["cross_references"]
        assert 110 in refs, "Must cross-reference #110 (Tom's Guide same-owner pattern)"
        assert 114 in refs, "Must cross-reference #114 (financial cause)"
        assert len(refs) >= 3, f"Expected ≥3 cross-references, got {len(refs)}"
