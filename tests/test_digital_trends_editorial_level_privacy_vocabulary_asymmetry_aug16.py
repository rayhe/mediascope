"""
Tests for mechanism #138: Digital Trends (Designtechnica Corp) Editorial-Level
Smart Glasses Privacy Vocabulary Asymmetry.

DISCOVERY: Digital Trends' Managing Editor (Nadeem Sarwar) personally writes
Meta coverage with adversarial privacy vocabulary ("creep's weapon") even when
reporting Meta's PROACTIVE privacy fixes, while the same publication covers
Samsung/Google smart glasses with zero privacy alarm terms across multiple
writers. This is an editorial-level pattern, not individual journalist bias.

Sources:
  - https://www.digitaltrends.com/wearables/meta-will-disable-the-camera-on-ai-smart-glasses-if-you-tamper-or-cover-the-indicator-light/
  - https://www.digitaltrends.com/cool-tech/smart-glasses-were-already-creepy-now-theyre-helping-people-cheat/
  - https://www.digitaltrends.com/wearables/meta-is-building-face-recognition-into-your-glasses-and-civil-rights-groups-are-not-happy-about-it/
  - https://www.digitaltrends.com/wearables/apple-smart-glasses-might-avoid-the-creepy-reputation-of-meta-ray-bans-with-a-light-trick/
  - https://www.digitaltrends.com/wearables/smart-glasses-are-back-and-this-time-theyre-pretending-to-be-normal/
  - https://www.digitaltrends.com/cool-tech/samsungs-upcoming-galaxy-glasses-have-leaked-and-the-looks-dont-impress/
  - https://www.digitaltrends.com/wearables/samsung-galaxy-xr-hands-on-preview/
  - https://www.digitaltrends.com/wearables/samsungs-first-ar-glasses-are-coming-in-2026-with-immersive-multimodal-ai-experiences/
"""
import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_research():
    with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


def load_entities():
    with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
        return yaml.safe_load(f)


def find_mechanism(data, mech_id):
    """Recursively search for a mechanism by ID in the YAML data."""
    if isinstance(data, dict):
        if data.get("mechanism_id") == mech_id:
            return data
        for v in data.values():
            result = find_mechanism(v, mech_id)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism(item, mech_id)
            if result:
                return result
    return None


def find_key(data, key_name):
    """Recursively find a key in nested dicts."""
    if isinstance(data, dict):
        if key_name in data:
            return data[key_name]
        for v in data.values():
            result = find_key(v, key_name)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_key(item, key_name)
            if result is not None:
                return result
    return None


@pytest.fixture(scope="module")
def research_data():
    return load_research()


@pytest.fixture(scope="module")
def entities_data():
    return load_entities()


@pytest.fixture(scope="module")
def mechanism(research_data):
    mech = find_mechanism(research_data, 138)
    assert mech is not None, "Mechanism #138 not found in research data"
    return mech


# ---------------------------------------------------------------------------
# 1. Mechanism existence and structural integrity
# ---------------------------------------------------------------------------


class TestMechanismExists:
    """Mechanism #138 must exist with required fields."""

    def test_mechanism_138_exists(self, research_data):
        mech = find_mechanism(research_data, 138)
        assert mech is not None, "Mechanism #138 not found in research data"

    def test_mechanism_id_is_138(self, mechanism):
        assert mechanism.get("mechanism_id") == 138

    def test_has_finding_summary(self, mechanism):
        assert "finding_summary" in mechanism
        assert len(mechanism["finding_summary"]) > 100

    def test_has_discovery_date(self, mechanism):
        assert mechanism.get("discovery_date") == "2026-08-16"

    def test_has_test_file(self, mechanism):
        assert "test_digital_trends_editorial_level" in mechanism.get(
            "test_file", ""
        )

    def test_has_source_urls(self, mechanism):
        urls = mechanism.get("source_urls", [])
        assert len(urls) >= 6, f"Expected 6+ source URLs, got {len(urls)}"
        for url in urls:
            assert url.startswith("http"), f"Invalid URL: {url}"

    def test_has_mechanism_name(self, mechanism):
        name = mechanism.get("mechanism_name", "")
        assert "Digital Trends" in name
        assert len(name) > 20


# ---------------------------------------------------------------------------
# 2. Managing Editor editorial gatekeeping
# ---------------------------------------------------------------------------


class TestManagingEditorGatekeeping:
    """Nadeem Sarwar as Managing Editor personally sets adversarial Meta tone."""

    def test_managing_editor_role_documented(self, mechanism):
        summary = mechanism.get("finding_summary", "")
        assert "Managing Editor" in summary

    def test_creeps_weapon_documented(self, mechanism):
        """Meta LED fix article opened with 'creep's weapon' despite positive news."""
        summary = mechanism.get("finding_summary", "")
        assert "creep" in summary.lower()

    def test_remediation_adversarial_framing(self, mechanism):
        """Even positive Meta coverage uses adversarial opening."""
        summary = mechanism.get("finding_summary", "")
        has_fix_ref = any(
            term in summary.lower()
            for term in ["led", "tamper", "fix", "disable", "proactive"]
        )
        assert has_fix_ref, (
            "Mechanism should document that Meta's proactive privacy fix was "
            "framed adversarially"
        )

    def test_nadeem_sarwar_identified(self, mechanism):
        """Managing Editor Nadeem Sarwar identified by name."""
        summary = mechanism.get("finding_summary", "")
        assert "Nadeem Sarwar" in summary or "Nadeem" in summary


# ---------------------------------------------------------------------------
# 3. Samsung/Google zero-scrutiny documentation
# ---------------------------------------------------------------------------


class TestSamsungGoogleZeroScrutiny:
    """Samsung/Google receive zero privacy alarm terms despite identical hardware."""

    def test_same_hardware_documented(self, mechanism):
        """Snapdragon AR1 Gen 1 chip shared between Meta and Samsung."""
        summary = mechanism.get("finding_summary", "")
        has_hw = any(
            term in summary
            for term in ["Snapdragon AR1", "same chip", "12MP", "identical"]
        )
        assert has_hw, "Same hardware specs not documented"

    def test_samsung_zero_privacy_terms(self, mechanism):
        """Samsung articles have zero privacy alarm vocabulary."""
        summary = mechanism.get("finding_summary", "")
        assert "zero" in summary.lower() or "ZERO" in summary

    def test_meta_articles_have_privacy_terms(self, mechanism):
        """Meta articles list privacy alarm terms."""
        meta_articles = mechanism.get("meta_articles", [])
        if meta_articles:
            articles_with_terms = [
                a for a in meta_articles
                if a.get("privacy_alarm_terms")
            ]
            assert len(articles_with_terms) >= 2, (
                f"Expected 2+ Meta articles with privacy alarm terms, got "
                f"{len(articles_with_terms)}"
            )

    def test_samsung_articles_empty_privacy_terms(self, mechanism):
        """Samsung articles have empty privacy_alarm_terms lists."""
        sg_articles = mechanism.get("samsung_google_articles", [])
        if sg_articles:
            for article in sg_articles:
                terms = article.get("privacy_alarm_terms", [])
                assert len(terms) == 0, (
                    f"Samsung article '{article.get('title')}' has privacy terms: "
                    f"{terms}"
                )


# ---------------------------------------------------------------------------
# 4. Cross-entity vocabulary analysis
# ---------------------------------------------------------------------------


class TestCrossEntityVocabulary:
    """Privacy vocabulary inversely proportional to competitive threat."""

    META_ALARM_TERMS = [
        "creep",
        "creepy",
        "weapon",
        "hot water",
        "vile",
        "slap in the face",
        "secretly",
        "silently",
        "social laundering",
        "covert",
        "without consent",
    ]

    def test_meta_vocabulary_adversarial(self, mechanism):
        """Meta coverage uses adversarial vocabulary in summary."""
        summary = mechanism.get("finding_summary", "").lower()
        matches = [term for term in self.META_ALARM_TERMS if term in summary]
        assert len(matches) >= 2, (
            f"Expected 2+ alarm terms in finding_summary, found: {matches}"
        )

    def test_samsung_articles_positive_tone(self, mechanism):
        """Samsung articles have neutral/positive tone scores."""
        sg_articles = mechanism.get("samsung_google_articles", [])
        if sg_articles:
            for article in sg_articles:
                tone = article.get("tone_score", 0)
                assert tone >= -0.2, (
                    f"Samsung article '{article.get('title')}' has adversarial "
                    f"tone {tone}"
                )


# ---------------------------------------------------------------------------
# 5. Multi-writer consistency
# ---------------------------------------------------------------------------


class TestMultiWriterConsistency:
    """Pattern holds across multiple Digital Trends writers."""

    def test_multiple_meta_writers(self, mechanism):
        """At least 2 different writers produce adversarial Meta coverage."""
        meta_articles = mechanism.get("meta_articles", [])
        if meta_articles:
            writers = {a.get("author", "unknown") for a in meta_articles if a.get("author")}
            assert len(writers) >= 2, (
                f"Expected 2+ distinct Meta article authors, got: {writers}"
            )

    def test_samsung_google_writers(self, mechanism):
        """Samsung/Google coverage written by identifiable writers."""
        sg_articles = mechanism.get("samsung_google_articles", [])
        if sg_articles:
            writers = {a.get("author", "unknown") for a in sg_articles if a.get("author")}
            assert len(writers) >= 1

    def test_article_urls_valid(self, mechanism):
        """All article URLs are valid digitaltrends.com URLs."""
        for key in ["meta_articles", "samsung_google_articles"]:
            articles = mechanism.get(key, [])
            for article in articles:
                url = article.get("url", "")
                assert "digitaltrends.com" in url, (
                    f"Article '{article.get('title')}' has non-DT URL: {url}"
                )


# ---------------------------------------------------------------------------
# 6. Financial context
# ---------------------------------------------------------------------------


class TestFinancialContext:
    """Financial relationships and entity existence."""

    def test_designtechnica_entity_exists(self, entities_data):
        """Designtechnica Corp entity must exist in competitor-entities.yaml."""
        entity = find_key(entities_data, "designtechnica_corp")
        assert entity is not None, (
            "designtechnica_corp entity not found in competitor-entities.yaml"
        )

    def test_designtechnica_has_display_name(self, entities_data):
        entity = find_key(entities_data, "designtechnica_corp")
        assert entity is not None
        assert "Digital Trends" in entity.get("display_name", "")

    def test_valnet_partnership_documented(self, entities_data):
        """Strategic advertising partnership with Valnet documented."""
        entity = find_key(entities_data, "designtechnica_corp")
        assert entity is not None
        desc = str(entity)
        assert "Valnet" in desc or "valnet" in desc

    def test_meta_zero_financial_ties(self, entities_data):
        """No known Meta financial relationships."""
        entity = find_key(entities_data, "designtechnica_corp")
        assert entity is not None
        meta_ties = entity.get("meta_financial_ties", "none")
        assert meta_ties == "none" or "zero" in str(meta_ties).lower()

    def test_google_samsung_advertising_dependency(self, entities_data):
        """Google and Samsung advertising dependency documented."""
        entity = find_key(entities_data, "designtechnica_corp")
        assert entity is not None
        desc = str(entity)
        assert "Google" in desc or "Samsung" in desc or "advertising" in desc

    def test_financial_context_in_mechanism(self, mechanism):
        """Mechanism has financial context section."""
        fc = mechanism.get("financial_context", {})
        assert fc, "Mechanism should have financial_context section"
        assert fc.get("meta_financial_ties") == "none"


# ---------------------------------------------------------------------------
# 7. Confounders
# ---------------------------------------------------------------------------


class TestConfounders:
    """Proper confounder documentation with strength ratings."""

    def test_has_confounders(self, mechanism):
        confounders = mechanism.get("confounders", [])
        assert len(confounders) >= 4, (
            f"Expected 4+ confounders, got {len(confounders)}"
        )

    def test_strong_confounder_present(self, mechanism):
        """At least one STRONG confounder must exist."""
        confounders = mechanism.get("confounders", [])
        strengths = [c.get("strength", "").upper() for c in confounders]
        assert "STRONG" in strengths, (
            f"No STRONG confounder found. Strengths: {strengths}"
        )

    def test_meta_track_record_confounder(self, mechanism):
        """Meta's genuine privacy track record acknowledged as confounder."""
        confounders = mechanism.get("confounders", [])
        texts = [str(c).lower() for c in confounders]
        any_track_record = any(
            "track record" in t or "cambridge analytica" in t or "ftc" in t
            for t in texts
        )
        assert any_track_record, "Meta privacy track record confounder missing"

    def test_market_presence_confounder(self, mechanism):
        """Samsung pre-launch vs Meta 7M+ units confounder documented."""
        confounders = mechanism.get("confounders", [])
        texts = [str(c).lower() for c in confounders]
        any_market = any(
            "pre-launch" in t or "7m" in t or "not shipping" in t or "market" in t
            for t in texts
        )
        assert any_market, "Market presence difference confounder missing"


# ---------------------------------------------------------------------------
# 8. Falsifiable predictions
# ---------------------------------------------------------------------------


class TestFalsifiablePredictions:
    """Mechanism must include testable predictions."""

    def test_has_predictions(self, mechanism):
        predictions = mechanism.get("falsifiable_predictions", [])
        assert len(predictions) >= 2, (
            f"Expected 2+ falsifiable predictions, got {len(predictions)}"
        )

    def test_predictions_are_falsifiable(self, mechanism):
        """Each prediction marked as falsifiable."""
        predictions = mechanism.get("falsifiable_predictions", [])
        for pred in predictions:
            assert pred.get("falsifiable") is True, (
                f"Prediction not marked falsifiable: {pred}"
            )

    def test_prediction_testability(self, mechanism):
        """Each prediction should be concrete and testable."""
        predictions = mechanism.get("falsifiable_predictions", [])
        for pred in predictions:
            text = pred.get("prediction", "")
            assert len(text) > 30, f"Prediction too vague: {text}"


# ---------------------------------------------------------------------------
# 9. Cross-reference integrity
# ---------------------------------------------------------------------------


class TestCrossReferences:
    """Mechanism must reference related mechanisms."""

    def test_has_cross_references(self, mechanism):
        refs = mechanism.get("cross_references", [])
        assert len(refs) >= 2, (
            f"Expected 2+ cross-references, got {len(refs)}"
        )

    def test_references_remediation_silence(self, mechanism):
        """Should reference mechanism #134 (WIRED remediation silence)."""
        refs = mechanism.get("cross_references", [])
        assert 134 in refs, (
            "Should reference #134 (WIRED remediation silence)"
        )

    def test_references_safe_target(self, mechanism):
        """Should reference mechanism #8 (safe target coefficient)."""
        refs = mechanism.get("cross_references", [])
        assert 8 in refs, "Should reference #8 (safe target coefficient)"

    def test_references_andy_boxall(self, mechanism):
        """Should reference mechanism #132 (Andy Boxall cross-entity)."""
        refs = mechanism.get("cross_references", [])
        assert 132 in refs, (
            "Should reference #132 (Andy Boxall cross-entity via Valnet)"
        )
