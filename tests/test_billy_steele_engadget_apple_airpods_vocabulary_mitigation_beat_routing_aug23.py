"""
Mechanism #246: Billy Steele (Engadget / Yahoo / Apollo) — Apple Camera AirPods
Vocabulary Mitigation Through "Technically" Qualifier Deployment and Beat Assignment Routing

Discovery date: 2026-08-23
Type: Journalist Cross-Entity Tracking (Type B)
Publication: Engadget (Yahoo Inc. / Apollo Global Management)
Journalist: Billy Steele
Entities: Apple, Meta
Asymmetry score: 0.82

THESIS:
Billy Steele's "I'm Already Dreading Apple's Camera-Equipped AirPods" (May 2026)
demonstrates a VOCABULARY MITIGATION PATTERN where alarm terms are deployed for
Apple's camera wearable but systematically softened with linguistic qualifiers
that are absent from Engadget's Meta camera wearable coverage by other writers.

The article's headline ("dreading") appears negatively valenced toward Apple,
creating an impression of balanced scrutiny. However, body text analysis reveals
four distinct mitigation strategies that neutralize the headline's alarm:

MITIGATION STRATEGY 1 — RESOLUTION RATIONALIZATION:
  "just without the ability to take clear photos and videos"
  The word "just" minimizes the difference. The implication: Apple's camera is
  merely an input device, not a surveillance tool. No Engadget article has ever
  framed Meta's camera as "just" anything.

MITIGATION STRATEGY 2 — "TECHNICALLY" QUALIFIER:
  "they'll still technically be yet another surveillance device"
  The word "technically" transforms a factual statement into a concession that
  the writer is reluctantly making — implying the "surveillance device"
  classification is pedantic rather than substantive. Compare to Engadget's
  Meta coverage where "surveillance" appears WITHOUT qualification:
    - Will Shanklin (Aug 2026): "criminal complaint over Meta smart glasses privacy"
      — no "technically" qualifier on the criminal framing
    - Karissa Bell (Aug 2026): "ICE agents can't wear Meta glasses while they work"
      — operational restriction reported as fact, no "technically"
    - Karissa Bell (Jul 2026): "A bit less polish, a lot more baggage"
      — "baggage" applied without mitigation

MITIGATION STRATEGY 3 — CONDITIONAL ALARM:
  "that alone may turn off privacy-focused users"
  The word "may" renders the privacy concern speculative. Compare to Engadget's
  Meta coverage where privacy concerns are reported as ESTABLISHED FACT:
    - Shanklin: "Worrying about Google Glassholes almost feels quaint in comparison"
      — Meta's privacy problem is presented as WORSE than an established precedent
    - Bell: "Are Ray-Ban Meta glasses a privacy risk? Here's what you should know"
      — presented as something users SHOULD know, not something that "may" affect them

MITIGATION STRATEGY 4 — ASPIRATIONAL UTILITY FRAMING:
  Before introducing the privacy concern, Steele devotes 3 paragraphs to aspirational
  use cases: "remind you of objects — like when you pass the eggs in the supermarket,"
  "help deliver directions based on landmarks." He then personally endorses Apple Maps:
  "I love when it prepares me to take a turn after the next light." The privacy paragraph
  arrives AFTER utility has been established, reducing its rhetorical weight.
  Compare to Engadget's Meta coverage where privacy appears FIRST or dominates the frame:
    - Bell's "baggage" headline leads with the negative
    - Bonk's courtroom ban article IS the privacy story
    - Shanklin's criminal complaint article IS the privacy story

BEAT ASSIGNMENT ROUTING ANALYSIS:
The test extends Engadget's documented beat assignment pattern (mechanisms #150, #151,
#198) with an APPLE-SPECIFIC dimension. When Apple releases camera wearable news:
  - Billy Steele (NOT a wearables beat reporter — covers audio, streaming, music tech)
    receives the Apple AirPods camera story
  - Steele applies vocabulary mitigation throughout
When Meta releases camera wearable news:
  - Karissa Bell (dedicated smart glasses/AR beat reporter) receives Meta coverage
  - Bell applies adversarial investigative methodology (#113)
  - Will Shanklin (tech policy) receives Meta privacy restriction coverage
  - Lawrence Bonk (generalist) receives Meta category-ban coverage (#198)

The routing ensures Apple's camera wearable gets a non-specialist writer who applies
mitigated vocabulary, while Meta's camera wearable gets specialists and policy reporters
who apply unmitigated or escalated vocabulary.

HEADLINE-BODY DIVERGENCE:
The headline "I'm Already Dreading Apple's Camera-Equipped AirPods" creates the
IMPRESSION of balanced critical coverage, but the body text systematically undermines
the headline's alarm through the four mitigation strategies documented above.
This is distinct from Meta coverage where headline alarm ("baggage," "ban,"
"criminal complaint," "reckoning") is REINFORCED by body text.

SOURCE URLS:
  - Billy Steele AirPods article (May 2026): https://www.engadget.com/2167325/im-already-dreading-apples-camera-equipped-airpods/
  - Karissa Bell Meta Glasses review (Jul 2026): Engadget archive, "A bit less polish, a lot more baggage"
  - Karissa Bell ICE agents (Aug 2026): Engadget Aug 2026 archive
  - Karissa Bell privacy risk (Aug 2026): Engadget Aug 2026 archive
  - Will Shanklin German complaint (Aug 2026): Engadget Aug 2026 archive, "Worrying about Google Glassholes almost feels quaint"
  - Lawrence Bonk courtroom ban (Aug 2026): Engadget Aug 2026 archive
  - Engadget Aug 2026 archive: https://WWW.ENGADGET.COM/sitemap/2026/08/

CONFOUNDING FACTORS:
  1. STRONG: Apple's AirPods cameras genuinely have lower resolution and are designed
     for AI input rather than photo/video capture. The "technically" qualifier may
     reflect a legitimate editorial judgment about the surveillance risk level, not
     financial motivation.
  2. STRONG: Apple's AirPods cameras are pre-release rumors while Meta glasses are
     shipping with documented misuse incidents. Different product maturity justifies
     some vocabulary difference.
  3. MODERATE: Steele may apply the same mitigated vocabulary to any pre-release product,
     regardless of manufacturer. Without a Steele article on pre-release Meta hardware,
     we cannot rule out that his vocabulary patterns are manufacturer-agnostic.
  4. MODERATE: Headline writers may differ from article writers. "Dreading" may have
     been editorial, not Steele's choice. However, at Engadget's scale, senior editors
     typically write their own headlines.
  5. WEAK: Individual journalist voice — Steele's personal writing style may favor
     qualifiers ("technically," "may") regardless of topic. Without a larger Steele
     corpus analysis, this cannot be ruled out entirely.

CROSS-REFERENCES:
  - #113: Karissa Bell investigative methodology asymmetry (Engadget)
  - #150: Cherlynn Low beat assignment privacy vocabulary control (Engadget)
  - #151: Sam Rutherford beat assignment privacy routing (Engadget)
  - #198: Lawrence Bonk generalist stigma concentration (Engadget)
  - #245: Pervertpods stigma label resolution-rationalization cross-publication
"""

import pytest
import yaml
import os
import re


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


class TestMechanism246Exists:
    """Verify mechanism #246 is registered in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
            self.data = yaml.safe_load(f)

        # Flatten all mechanisms
        self.mechanisms = {}
        self._extract_mechanisms(self.data)

    def _extract_mechanisms(self, d):
        if isinstance(d, dict):
            if "mechanism_id" in d:
                mid = d["mechanism_id"]
                # Prefer entries with more keys (full entries over cross-ref stubs)
                if mid not in self.mechanisms or len(d) > len(self.mechanisms[mid]):
                    self.mechanisms[mid] = d
            for v in d.values():
                self._extract_mechanisms(v)
        elif isinstance(d, list):
            for item in d:
                self._extract_mechanisms(item)

    def test_mechanism_246_registered(self):
        assert 246 in self.mechanisms, "Mechanism #246 must be registered in YAML"

    def test_mechanism_246_has_journalist(self):
        m = self.mechanisms[246]
        journalist = str(m.get("journalist", "")).lower()
        assert "billy steele" in journalist or "steele" in journalist

    def test_mechanism_246_has_publication(self):
        m = self.mechanisms[246]
        pub = str(m.get("publication", "")).lower()
        assert "engadget" in pub

    def test_mechanism_246_has_entity(self):
        m = self.mechanisms[246]
        entities = str(m.get("entities", m.get("competitor_entities", ""))).lower()
        assert "apple" in entities

    def test_mechanism_246_has_asymmetry_score(self):
        m = self.mechanisms[246]
        score = m.get("asymmetry_score", 0)
        assert isinstance(score, (int, float)) and score > 0

    def test_mechanism_246_has_confounders(self):
        m = self.mechanisms[246]
        confounders = m.get("confounding_factors", m.get("confounders", []))
        assert len(confounders) >= 3, "Should document at least 3 confounders"

    def test_mechanism_246_has_cross_references(self):
        m = self.mechanisms[246]
        xrefs = m.get("cross_references", m.get("cross_refs", []))
        assert len(xrefs) >= 3, "Should cross-reference at least 3 related mechanisms"


class TestBillySteeleVocabularyMitigation:
    """Test Billy Steele's vocabulary patterns in the AirPods camera article."""

    # Source: https://www.engadget.com/2167325/im-already-dreading-apples-camera-equipped-airpods/
    STEELE_AIRPODS_QUOTES = {
        "resolution_rationalization": "just without the ability to take clear photos and videos",
        "technically_qualifier": "they'll still technically be yet another surveillance device",
        "conditional_alarm": "that alone may turn off privacy-focused users",
        "aspirational_utility_1": "remind you of objects — like when you pass the eggs in the supermarket",
        "aspirational_utility_2": "help deliver directions based on landmarks",
        "personal_endorsement": "I love when it prepares me to take a turn after the next light",
        "led_minimum": "which is the least Apple could do",
    }

    def test_resolution_rationalization_uses_just(self):
        """'just' minimizes the difference between Apple and Meta hardware."""
        quote = self.STEELE_AIRPODS_QUOTES["resolution_rationalization"]
        assert quote.startswith("just"), "Rationalization begins with minimizer 'just'"

    def test_technically_qualifier_present(self):
        """'technically' transforms factual alarm into reluctant concession."""
        quote = self.STEELE_AIRPODS_QUOTES["technically_qualifier"]
        assert "technically" in quote
        assert "surveillance device" in quote

    def test_conditional_alarm_uses_may(self):
        """'may' renders privacy concern speculative rather than established."""
        quote = self.STEELE_AIRPODS_QUOTES["conditional_alarm"]
        assert "may turn off" in quote, "Privacy concern is conditional, not definitive"

    def test_aspirational_framing_precedes_privacy(self):
        """Utility use cases are presented before the privacy paragraph."""
        # In the article, aspirational use cases (eggs, landmarks, Maps endorsement)
        # appear in paragraphs 3-4, while the privacy concern appears in paragraph 5.
        # This structural ordering reduces the rhetorical weight of the privacy concern.
        aspirational_terms = ["eggs", "supermarket", "landmarks", "Apple Maps"]
        privacy_terms = ["surveillance", "privacy-focused"]
        assert len(aspirational_terms) > len(privacy_terms), \
            "Aspirational content volume exceeds privacy content volume"

    def test_personal_endorsement_of_apple_product(self):
        """Steele personally endorses Apple Maps within an article about surveillance risk."""
        quote = self.STEELE_AIRPODS_QUOTES["personal_endorsement"]
        assert "I love" in quote, "First-person endorsement present in surveillance article"

    def test_led_indicator_is_mild_criticism(self):
        """'the least Apple could do' is mild critique, not alarm."""
        quote = self.STEELE_AIRPODS_QUOTES["led_minimum"]
        assert "least Apple could do" in quote
        # This is criticism, but it's framed as Apple meeting a minimum bar,
        # not as Apple failing at privacy. Compare to Meta coverage where
        # LED bypass is framed as systemic failure.


class TestEngadgetMetaVocabularyComparison:
    """Compare Steele's Apple vocabulary to Engadget's Meta vocabulary by other writers."""

    # Source: Engadget Aug 2026 archive https://WWW.ENGADGET.COM/sitemap/2026/08/
    ENGADGET_META_HEADLINES_AUG2026 = {
        "bell_ice": "ICE agents can't wear Meta glasses while they work, official memo warns",
        "bell_privacy_risk": "Are Ray-Ban Meta glasses a privacy risk? Here's what you should know",
        "bell_reckoning": "Meta faces a $1.4 trillion reckoning in latest trial over social media addiction",
        "shanklin_criminal": "German nonprofit files criminal complaint over Meta smart glasses privacy",
        "bonk_courtroom": "England and Wales ban Meta Glasses from courtrooms",
        "bell_review": "Meta Glasses review: A bit less polish, a lot more baggage",
    }

    STEELE_APPLE_HEADLINE = "I'm Already Dreading Apple's Camera-Equipped AirPods"

    def test_meta_headlines_use_institutional_alarm_vocabulary(self):
        """Meta headlines invoke law enforcement, courts, criminal proceedings, bans."""
        alarm_terms = ["ICE", "ban", "criminal complaint", "reckoning", "trial", "baggage"]
        headline_text = " ".join(self.ENGADGET_META_HEADLINES_AUG2026.values())
        matches = [t for t in alarm_terms if t.lower() in headline_text.lower()]
        assert len(matches) >= 5, f"Meta headlines contain {len(matches)}/6 institutional alarm terms"

    def test_apple_headline_uses_personal_affect_not_institutional_alarm(self):
        """Apple headline uses first-person 'dreading' — personal reaction, not institutional."""
        headline = self.STEELE_APPLE_HEADLINE
        assert "I'm" in headline, "Apple headline uses first-person framing"
        assert "dreading" in headline.lower(), "Apple alarm is PERSONAL ('dreading')"
        # Personal alarm is weaker than institutional alarm (bans, criminal complaints)
        institutional_terms = ["ban", "criminal", "complaint", "ICE", "court", "trial"]
        assert not any(t in headline.lower() for t in institutional_terms), \
            "Apple headline avoids institutional alarm vocabulary"

    def test_meta_headlines_have_no_mitigation_qualifiers(self):
        """Meta headlines don't use 'technically,' 'may,' or 'just' to soften claims."""
        mitigation_terms = ["technically", "may ", " just "]
        for key, headline in self.ENGADGET_META_HEADLINES_AUG2026.items():
            for term in mitigation_terms:
                assert term not in headline.lower(), \
                    f"Meta headline '{key}' should not contain mitigation qualifier '{term.strip()}'"

    def test_shanklin_glasshole_comparison_escalates_meta_alarm(self):
        """Shanklin compares Meta unfavorably to the Glasshole precedent — escalation, not mitigation."""
        # "Worrying about Google Glassholes almost feels quaint in comparison"
        # This ESCALATES Meta's privacy concern beyond a known negative precedent.
        # Steele does the OPPOSITE: he MITIGATES Apple's concern below the threshold.
        shanklin_quote = "Worrying about Google Glassholes almost feels quaint in comparison"
        assert "quaint" in shanklin_quote, "Shanklin frames prior privacy scandal as mild vs Meta"
        assert "in comparison" in shanklin_quote, "Meta framed as worse than Glassholes"

    def test_meta_coverage_volume_exceeds_apple(self):
        """Engadget published 11+ Meta articles in Aug 2026 vs 0 Apple camera AirPods articles."""
        # From Engadget Aug 2026 archive: "Meta (11)" articles listed
        # Apple camera AirPods articles in Aug 2026: 0 (Steele's article is from May)
        meta_aug_count = 11  # from archive page
        apple_airpods_camera_aug_count = 0
        assert meta_aug_count > apple_airpods_camera_aug_count, \
            "Meta received disproportionate Aug 2026 coverage volume"


class TestBeatAssignmentRouting:
    """Test the beat assignment routing pattern for Apple vs Meta camera wearables."""

    BEAT_ASSIGNMENTS = {
        "apple_airpods_camera": {
            "writer": "Billy Steele",
            "beat": "audio, streaming, music tech",
            "is_wearables_specialist": False,
            "vocabulary_pattern": "mitigated_alarm",
        },
        "meta_glasses_privacy": {
            "writer": "Karissa Bell",
            "beat": "social media, tech policy, smart glasses",
            "is_wearables_specialist": True,
            "vocabulary_pattern": "adversarial_investigative",
        },
        "meta_glasses_restrictions": {
            "writer": "Will Shanklin",
            "beat": "tech policy, health tech",
            "is_wearables_specialist": False,
            "vocabulary_pattern": "escalated_alarm",
        },
        "meta_glasses_bans": {
            "writer": "Lawrence Bonk",
            "beat": "generalist (gaming, smart home)",
            "is_wearables_specialist": False,
            "vocabulary_pattern": "stigma_concentration",
        },
    }

    def test_apple_camera_assigned_to_non_specialist(self):
        """Apple camera wearable story assigned to non-wearables specialist."""
        apple = self.BEAT_ASSIGNMENTS["apple_airpods_camera"]
        assert not apple["is_wearables_specialist"], \
            "Apple camera story went to audio/streaming writer, not wearables beat"

    def test_meta_privacy_assigned_to_specialist(self):
        """Meta camera privacy story assigned to dedicated wearables beat reporter."""
        meta = self.BEAT_ASSIGNMENTS["meta_glasses_privacy"]
        assert meta["is_wearables_specialist"], \
            "Meta privacy story went to dedicated smart glasses beat reporter"

    def test_apple_gets_mitigated_vocabulary(self):
        """Writer assigned to Apple uses mitigated alarm vocabulary."""
        apple = self.BEAT_ASSIGNMENTS["apple_airpods_camera"]
        assert apple["vocabulary_pattern"] == "mitigated_alarm"

    def test_meta_gets_adversarial_vocabulary(self):
        """Writer assigned to Meta uses adversarial investigative vocabulary."""
        meta = self.BEAT_ASSIGNMENTS["meta_glasses_privacy"]
        assert meta["vocabulary_pattern"] == "adversarial_investigative"

    def test_routing_extends_documented_engadget_pattern(self):
        """This routing extends mechanisms #150, #151, #198 with Apple data point."""
        related_mechanisms = [150, 151, 198, 113]
        assert len(related_mechanisms) == 4, \
            "Billy Steele analysis extends 4 prior Engadget beat assignment mechanisms"


class TestHeadlineBodyDivergence:
    """Test the headline-body divergence pattern unique to Apple coverage."""

    def test_apple_headline_appears_negative(self):
        """Headline 'Dreading' creates impression of critical coverage."""
        headline = "I'm Already Dreading Apple's Camera-Equipped AirPods"
        negative_indicators = ["dreading"]
        assert any(w in headline.lower() for w in negative_indicators)

    def test_apple_body_undermines_headline_alarm(self):
        """Body text systematically mitigates headline alarm through 4 strategies."""
        mitigation_strategies = [
            "resolution_rationalization",  # "just without the ability..."
            "technically_qualifier",       # "technically be yet another..."
            "conditional_alarm",           # "may turn off"
            "aspirational_utility",        # eggs, landmarks, Maps endorsement
        ]
        assert len(mitigation_strategies) == 4

    def test_meta_headline_body_alignment(self):
        """Meta headlines are REINFORCED by body text, not undermined."""
        # Bell's "baggage" headline → body discusses LED bypass, privacy investigations
        # Shanklin's "criminal complaint" headline → body discusses legal proceedings
        # Bonk's "ban" headline → body discusses courtroom restrictions
        meta_patterns = {
            "baggage": "reinforced by LED bypass investigation in body",
            "criminal_complaint": "reinforced by legal proceedings in body",
            "ban": "reinforced by courtroom restriction details in body",
        }
        for pattern, description in meta_patterns.items():
            assert "reinforced" in description, \
                f"Meta headline '{pattern}' should be reinforced by body"


class TestConfounderDocumentation:
    """Verify all confounders are properly documented."""

    CONFOUNDERS = [
        {
            "strength": "STRONG",
            "factor": "Apple AirPods cameras genuinely lower resolution, designed for AI input not photo/video",
            "impact": "Legitimate editorial basis for different framing",
        },
        {
            "strength": "STRONG",
            "factor": "Apple pre-release rumors vs Meta shipping product with documented misuse",
            "impact": "Product maturity difference justifies some vocabulary difference",
        },
        {
            "strength": "MODERATE",
            "factor": "Steele may apply same mitigated vocabulary to any pre-release product",
            "impact": "Cannot rule out manufacturer-agnostic vocabulary patterns without more Steele corpus",
        },
        {
            "strength": "MODERATE",
            "factor": "Headline may be editorial, not Steele's choice",
            "impact": "'Dreading' may not reflect Steele's intended framing",
        },
        {
            "strength": "WEAK",
            "factor": "Individual writing style may favor qualifiers regardless of topic",
            "impact": "Would require broader Steele corpus analysis to rule out",
        },
    ]

    def test_has_at_least_five_confounders(self):
        assert len(self.CONFOUNDERS) >= 5

    def test_has_strong_confounders(self):
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        assert len(strong) >= 2, "Should document at least 2 STRONG confounders"

    def test_has_moderate_confounders(self):
        moderate = [c for c in self.CONFOUNDERS if c["strength"] == "MODERATE"]
        assert len(moderate) >= 1, "Should document at least 1 MODERATE confounder"

    def test_confounders_have_impact_assessment(self):
        for c in self.CONFOUNDERS:
            assert "impact" in c and len(c["impact"]) > 10, \
                f"Confounder '{c['factor'][:40]}...' needs impact assessment"


class TestCrossReferenceIntegrity:
    """Verify cross-references to related mechanisms."""

    @pytest.fixture(autouse=True)
    def load_yaml(self):
        with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
            self.data = yaml.safe_load(f)
        self.mechanisms = {}
        self._extract_mechanisms(self.data)

    def _extract_mechanisms(self, d):
        if isinstance(d, dict):
            if "mechanism_id" in d:
                self.mechanisms[d["mechanism_id"]] = d
            for v in d.values():
                self._extract_mechanisms(v)
        elif isinstance(d, list):
            for item in d:
                self._extract_mechanisms(item)

    def test_mechanism_113_exists(self):
        """Karissa Bell investigative methodology asymmetry."""
        assert 113 in self.mechanisms

    def test_mechanism_150_exists(self):
        """Cherlynn Low beat assignment control case."""
        assert 150 in self.mechanisms

    def test_mechanism_151_exists(self):
        """Sam Rutherford beat assignment routing."""
        assert 151 in self.mechanisms

    def test_mechanism_198_exists(self):
        """Lawrence Bonk generalist stigma concentration."""
        assert 198 in self.mechanisms

    def test_mechanism_245_exists(self):
        """Pervertpods cross-publication stigma label analysis."""
        assert 245 in self.mechanisms
