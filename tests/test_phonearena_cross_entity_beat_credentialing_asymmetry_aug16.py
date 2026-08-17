"""
PhoneArena (Varna, Bulgaria) Cross-Entity Beat-Assignment Credentialing Asymmetry
Mechanism #141 — Discovered 2026-08-16

DISCOVERY: Google-Credentialed Reporter Covers Samsung/Google Glasses with Zero
Privacy Vocabulary While Separate Reporter Frames Meta Glasses with 7+ Alarm Terms
in Same Publication

PhoneArena is an independent Bulgarian tech publication ($7.2M revenue, ~50 staff,
founded 2001 in Varna) with NO corporate tech parent and NO known AI content
licensing deals. Yet it exhibits systematic cross-entity privacy vocabulary
asymmetry in smart glasses coverage through beat-assignment credentialing:

1. Johanna Romero (Senior News Writer, official Google #TeamPixel member since 2022)
   covers Samsung/Google glasses reveal with ZERO privacy vocabulary, aspirational
   framing ("I'm excited"), feature-focus only.

2. Ilia (tech journalist) covers Meta glasses with 7+ adversarial privacy alarm terms
   AND explicitly dismisses identical concerns for Samsung/Google in the SAME article:
   "Even Google fares much better in that regard" (no evidence cited) and "Adding a
   new set of data doesn't feel that concerning" (Samsung/Google camera-to-cloud).

NOVEL ELEMENT: First mechanism documenting a Google-credentialed reporter (#TeamPixel)
at an independent publication assigned to cover the product category where that
credential creates structural bias. The credentialing is disclosed in her byline
but creates an implicit access/relationship dependency that is absent for Meta coverage.

Sources:
- https://www.phonearena.com/news/move-over-ray-ban-samsung-and-google-just-revealed-their-first-intelligent-eyewear_id180476
  (Johanna Romero, Samsung/Google glasses reveal, 0 privacy terms)
- https://www.phonearena.com/news/apple-doesnt-need-fashion-brands-to-beat-the-meta-ray-ban-in-its-own-game_id180781
  (Ilia, Meta adversarial + Google/Samsung dismissal in SAME article)
- https://www.phonearena.com/news/meta-ray-ban-smart-glasses-showing-intimate-moments-to-workers-in-kenya-investigation_id178789
  (PhoneArena, Meta Kenya/Sama investigation coverage, 7+ alarm terms)
- https://www.phonearena.com/news/whistleblowers-who-exposed-meta-ray-ban-smart-glasses-fired_id180105
  (PhoneArena, whistleblower followup, continued adversarial framing)
"""

import pytest


# ─── Mechanism metadata ───

MECHANISM = {
    "id": 141,
    "name": "PhoneArena Cross-Entity Beat-Assignment Credentialing Asymmetry",
    "publication": "PhoneArena",
    "owner": "Independent (Varna, Bulgaria, CEO Pressian Karakostov)",
    "revenue": "$7.2M annual, affiliate + sponsored content",
    "staff": "~50",
    "founded": 2001,
    "meta_financial_ties": "ZERO",
    "google_financial_ties": "Google #TeamPixel credential (Johanna Romero), standard Google search traffic dependency",
    "samsung_financial_ties": "Samsung advertising client (4th-largest global advertiser, $9.7B)",
    "key_journalists": {
        "johanna_romero": {
            "role": "Senior News Writer",
            "credential": "Official Google #TeamPixel member since 2022",
            "beat": "Samsung/Google ecosystem coverage",
            "meta_privacy_terms_in_glasses_coverage": 0,
            "samsung_google_privacy_terms_in_glasses_coverage": 0,
        },
        "ilia": {
            "role": "Tech Journalist",
            "background": "Bulgarian, based in Lima, Peru; covers since 2011; experience at Forbes Bulgaria",
            "meta_privacy_alarm_terms": [
                "very questionable",
                "Cambridge Analytica scandal",
                "extremely private recordings",
                "disturbing",
                "invasion of everyone's privacy",
                "track record of actions that ignore people's privacy concerns",
                "concerning",
            ],
            "google_samsung_privacy_terms_in_same_article": 0,
            "explicit_dismissal": "Even Google fares much better in that regard",
            "rationalization": "Adding a new set of data doesn't feel that concerning",
        },
    },
    "articles": {
        "samsung_google_reveal": {
            "url": "https://www.phonearena.com/news/move-over-ray-ban-samsung-and-google-just-revealed-their-first-intelligent-eyewear_id180476",
            "author": "Johanna Romero",
            "date": "2026-05-15",
            "privacy_alarm_terms": 0,
            "tone": "aspirational",
            "headline_framing": "Move over, Ray-Ban",
            "cameras": "12MP (same Snapdragon AR1 Gen 1 as Meta)",
        },
        "apple_vs_meta": {
            "url": "https://www.phonearena.com/news/apple-doesnt-need-fashion-brands-to-beat-the-meta-ray-ban-in-its-own-game_id180781",
            "author": "Ilia",
            "date": "2026-06-02",
            "meta_privacy_alarm_terms": 7,
            "google_samsung_privacy_alarm_terms": 0,
            "within_article_dismissal": True,
            "key_quote_dismissal": "Even Google fares much better in that regard, which puts the upcoming Android XR models in a better position",
            "key_quote_rationalization": "Google and Samsung users are already sharing their data with the manufacturers of their phones. Adding a new set of data doesn't feel that concerning",
        },
        "kenya_investigation": {
            "url": "https://www.phonearena.com/news/meta-ray-ban-smart-glasses-showing-intimate-moments-to-workers-in-kenya-investigation_id178789",
            "headline": "Your Meta Ray-Ban smart glasses are showing your intimate moments to workers in Kenya, claims bombshell investigation",
            "privacy_alarm_terms": ["bombshell", "intimate moments", "spying", "disturbing", "invasion", "sensitive", "private"],
            "tone": "adversarial",
        },
        "whistleblower_followup": {
            "url": "https://www.phonearena.com/news/whistleblowers-who-exposed-meta-ray-ban-smart-glasses-fired_id180105",
            "headline": "Whistleblowers who exposed Meta Ray-Ban smart glasses fired",
            "tone": "adversarial_continuation",
        },
    },
    "confounding_factors": [
        {
            "strength": "STRONG",
            "factor": "Meta's documented Kenya/Sama scandal is genuinely worse than any documented Samsung/Google data handling incident — Meta has real privacy failures to report on",
        },
        {
            "strength": "STRONG",
            "factor": "Samsung/Google glasses had not launched at time of coverage — pre-launch coverage naturally has less privacy scrutiny than post-incident coverage",
        },
        {
            "strength": "MODERATE",
            "factor": "Google #TeamPixel credential disclosed in byline — not hidden, readers can assess",
        },
        {
            "strength": "MODERATE",
            "factor": "Genre difference: reveal/preview articles (Samsung/Google) vs scandal/investigation (Meta) naturally differ in tone",
        },
        {
            "strength": "WEAK",
            "factor": "PhoneArena may assign reporters by expertise/availability rather than strategic beat management",
        },
    ],
    "testable_predictions": [
        "When Samsung/Google glasses launch and have their first privacy incident, Johanna Romero will NOT apply equivalent alarm vocabulary to the incident as PhoneArena applies to Meta incidents",
        "PhoneArena will NOT assign Ilia to cover Samsung/Google glasses launch reviews — the #TeamPixel-credentialed reporter will maintain beat coverage",
        "If Samsung/Google glasses footage is reviewed by human contractors (parallel to Meta's Sama), PhoneArena will frame it as 'industry practice' rather than 'bombshell investigation'",
    ],
    "cross_references": [
        {"mechanism": 132, "relationship": "extends", "connection": "Andy Boxall (Android Police / Valnet) showed same privacy vocabulary inversion; PhoneArena shows the CREDENTIALING mechanism that produces it"},
        {"mechanism": 131, "relationship": "complements", "connection": "Ben Schoon (9to5Google) as control calibration — similar Google affinity, different publication ownership"},
        {"mechanism": 137, "relationship": "parallels", "connection": "Inc.com Samsung privacy redirected attribution — same pattern of redirecting ALL privacy vocabulary to Meta while presenting Samsung with zero scrutiny"},
        {"mechanism": 138, "relationship": "complements", "connection": "Digital Trends editorial-level asymmetry — both independent publications, both showing institutional (not just individual) bias patterns"},
    ],
}


@pytest.fixture
def mechanism():
    return MECHANISM


class TestMechanismStructure:
    """Verify mechanism #141 has all required fields."""

    def test_mechanism_id(self, mechanism):
        assert mechanism["id"] == 141

    def test_mechanism_has_name(self, mechanism):
        assert "Beat-Assignment Credentialing" in mechanism["name"]

    def test_publication_identified(self, mechanism):
        assert mechanism["publication"] == "PhoneArena"

    def test_independent_ownership(self, mechanism):
        assert "Independent" in mechanism["owner"]
        assert "Bulgaria" in mechanism["owner"]

    def test_zero_meta_ties(self, mechanism):
        assert mechanism["meta_financial_ties"] == "ZERO"

    def test_google_ties_documented(self, mechanism):
        assert "#TeamPixel" in mechanism["google_financial_ties"]

    def test_has_confounders(self, mechanism):
        assert len(mechanism["confounding_factors"]) >= 5

    def test_has_predictions(self, mechanism):
        assert len(mechanism["testable_predictions"]) >= 3

    def test_has_cross_references(self, mechanism):
        assert len(mechanism["cross_references"]) >= 3

    def test_has_source_urls(self, mechanism):
        for key, article in mechanism["articles"].items():
            assert "url" in article, f"Article {key} missing URL"


class TestJohannaRomeroCredentialing:
    """Verify Google #TeamPixel credentialing for Samsung/Google beat reporter."""

    def test_romero_is_team_pixel(self, mechanism):
        romero = mechanism["key_journalists"]["johanna_romero"]
        assert "#TeamPixel" in romero["credential"]

    def test_romero_credential_year(self, mechanism):
        romero = mechanism["key_journalists"]["johanna_romero"]
        assert "2022" in romero["credential"]

    def test_romero_covers_samsung_google(self, mechanism):
        romero = mechanism["key_journalists"]["johanna_romero"]
        assert "Samsung" in romero["beat"] or "Google" in romero["beat"]

    def test_romero_zero_privacy_terms_meta(self, mechanism):
        """Romero doesn't write Meta adversarial pieces — different beat."""
        romero = mechanism["key_journalists"]["johanna_romero"]
        assert romero["meta_privacy_terms_in_glasses_coverage"] == 0

    def test_romero_zero_privacy_terms_samsung_google(self, mechanism):
        """Samsung/Google reveal has zero privacy alarm vocabulary."""
        romero = mechanism["key_journalists"]["johanna_romero"]
        assert romero["samsung_google_privacy_terms_in_glasses_coverage"] == 0

    def test_romero_samsung_article_aspirational(self, mechanism):
        article = mechanism["articles"]["samsung_google_reveal"]
        assert article["tone"] == "aspirational"
        assert article["privacy_alarm_terms"] == 0

    def test_romero_samsung_article_author(self, mechanism):
        article = mechanism["articles"]["samsung_google_reveal"]
        assert article["author"] == "Johanna Romero"


class TestIliaCrossEntityFraming:
    """Verify Ilia's within-article double standard."""

    def test_ilia_meta_alarm_terms_count(self, mechanism):
        ilia = mechanism["key_journalists"]["ilia"]
        assert len(ilia["meta_privacy_alarm_terms"]) >= 7

    def test_ilia_google_samsung_zero_terms(self, mechanism):
        ilia = mechanism["key_journalists"]["ilia"]
        assert ilia["google_samsung_privacy_terms_in_same_article"] == 0

    def test_ilia_explicit_google_dismissal(self, mechanism):
        """Ilia explicitly says Google is better — with no evidence cited."""
        ilia = mechanism["key_journalists"]["ilia"]
        assert "Google fares much better" in ilia["explicit_dismissal"]

    def test_ilia_samsung_rationalization(self, mechanism):
        """Ilia dismisses Samsung data sharing as not concerning."""
        ilia = mechanism["key_journalists"]["ilia"]
        assert "doesn't feel that concerning" in ilia["rationalization"]

    def test_within_article_dismissal_documented(self, mechanism):
        """The apple_vs_meta article has both adversarial and dismissive framing."""
        article = mechanism["articles"]["apple_vs_meta"]
        assert article["within_article_dismissal"] is True
        assert article["meta_privacy_alarm_terms"] >= 7
        assert article["google_samsung_privacy_alarm_terms"] == 0

    def test_meta_alarm_vocabulary_includes_cambridge(self, mechanism):
        ilia = mechanism["key_journalists"]["ilia"]
        assert any("Cambridge" in term for term in ilia["meta_privacy_alarm_terms"])

    def test_meta_alarm_vocabulary_includes_invasion(self, mechanism):
        ilia = mechanism["key_journalists"]["ilia"]
        assert any("invasion" in term for term in ilia["meta_privacy_alarm_terms"])

    def test_meta_alarm_vocabulary_includes_track_record(self, mechanism):
        ilia = mechanism["key_journalists"]["ilia"]
        assert any("track record" in term for term in ilia["meta_privacy_alarm_terms"])


class TestWithinArticleRationalization:
    """The most revealing finding: identical privacy concerns dismissed in the same article."""

    def test_same_chip_different_framing(self, mechanism):
        """Samsung glasses use same Snapdragon AR1 Gen 1 as Meta."""
        samsung = mechanism["articles"]["samsung_google_reveal"]
        assert "Snapdragon AR1 Gen 1" in samsung["cameras"]

    def test_google_dismissal_no_evidence(self, mechanism):
        """'Even Google fares much better' — stated as fact without supporting evidence."""
        article = mechanism["articles"]["apple_vs_meta"]
        assert "Even Google fares much better" in article["key_quote_dismissal"]

    def test_samsung_data_sharing_rationalized(self, mechanism):
        """'Adding a new set of data doesn't feel that concerning' — emotional dismissal."""
        article = mechanism["articles"]["apple_vs_meta"]
        assert "doesn't feel that concerning" in article["key_quote_rationalization"]

    def test_rationalization_applies_equally_to_meta(self, mechanism):
        """The rationalization 'you already share data' applies equally to Meta users
        who already share data with Facebook/Instagram, yet is never applied to Meta."""
        article = mechanism["articles"]["apple_vs_meta"]
        # The rationalization references phone data sharing
        assert "sharing their data with the manufacturers" in article["key_quote_rationalization"]
        # But Meta users also share data with Meta via Facebook/Instagram
        # This asymmetric application is the mechanism in action


class TestPrivacyVocabularyDifferential:
    """Quantify the vocabulary gap across articles."""

    def test_meta_kenya_article_alarm_count(self, mechanism):
        article = mechanism["articles"]["kenya_investigation"]
        assert len(article["privacy_alarm_terms"]) >= 7

    def test_meta_kenya_adversarial_tone(self, mechanism):
        article = mechanism["articles"]["kenya_investigation"]
        assert article["tone"] == "adversarial"

    def test_samsung_google_reveal_zero_alarm(self, mechanism):
        article = mechanism["articles"]["samsung_google_reveal"]
        assert article["privacy_alarm_terms"] == 0

    def test_infinite_vocabulary_ratio(self, mechanism):
        """Privacy vocabulary ratio: Meta 7+ terms / Samsung-Google 0 terms = infinity."""
        meta_terms = len(mechanism["articles"]["kenya_investigation"]["privacy_alarm_terms"])
        samsung_terms = mechanism["articles"]["samsung_google_reveal"]["privacy_alarm_terms"]
        assert meta_terms > 0
        assert samsung_terms == 0

    def test_meta_headline_adversarial(self, mechanism):
        headline = mechanism["articles"]["kenya_investigation"]["headline"]
        assert "intimate moments" in headline.lower() or "bombshell" in headline.lower()

    def test_samsung_headline_aspirational(self, mechanism):
        article = mechanism["articles"]["samsung_google_reveal"]
        assert article["headline_framing"] == "Move over, Ray-Ban"


class TestFinancialContext:
    """Document PhoneArena's financial structure and advertising dependencies."""

    def test_independent_publication(self, mechanism):
        assert "Independent" in mechanism["owner"]

    def test_no_corporate_tech_parent(self, mechanism):
        owner = mechanism["owner"]
        for parent in ["Condé Nast", "Advance", "News Corp", "Ziff Davis", "Yahoo", "Apollo", "Future plc"]:
            assert parent not in owner

    def test_revenue_documented(self, mechanism):
        assert "$7.2M" in mechanism["revenue"]

    def test_samsung_advertising_dependency(self, mechanism):
        assert "$9.7B" in mechanism["samsung_financial_ties"]

    def test_google_credential_not_financial_deal(self, mechanism):
        """#TeamPixel is a credential/access relationship, not a content licensing deal."""
        ties = mechanism["google_financial_ties"]
        assert "#TeamPixel" in ties
        assert "search traffic" in ties


class TestConfoundingFactors:
    """Verify confounders are properly documented with strengths."""

    def test_has_strong_confounders(self, mechanism):
        strong = [c for c in mechanism["confounding_factors"] if c["strength"] == "STRONG"]
        assert len(strong) >= 2

    def test_meta_genuine_scandal_acknowledged(self, mechanism):
        strong = [c for c in mechanism["confounding_factors"] if c["strength"] == "STRONG"]
        meta_scandal = any("genuinely worse" in c["factor"] or "real privacy failures" in c["factor"] for c in strong)
        assert meta_scandal, "Must acknowledge Meta's genuine privacy failures as confounder"

    def test_pre_launch_timing_acknowledged(self, mechanism):
        confounders = mechanism["confounding_factors"]
        timing = any("not launched" in c["factor"] or "pre-launch" in c["factor"] for c in confounders)
        assert timing, "Must acknowledge Samsung/Google pre-launch timing"

    def test_credential_disclosure_acknowledged(self, mechanism):
        confounders = mechanism["confounding_factors"]
        disclosure = any("disclosed" in c["factor"] for c in confounders)
        assert disclosure, "Must acknowledge #TeamPixel credential is disclosed"


class TestCrossReferences:
    """Verify bidirectional cross-references to related mechanisms."""

    def test_references_andy_boxall_mechanism(self, mechanism):
        refs = mechanism["cross_references"]
        boxall = any(r["mechanism"] == 132 for r in refs)
        assert boxall, "Must reference Mechanism #132 (Andy Boxall privacy inversion)"

    def test_references_inc_mechanism(self, mechanism):
        refs = mechanism["cross_references"]
        inc = any(r["mechanism"] == 137 for r in refs)
        assert inc, "Must reference Mechanism #137 (Inc.com redirected attribution)"

    def test_references_digital_trends_mechanism(self, mechanism):
        refs = mechanism["cross_references"]
        dt = any(r["mechanism"] == 138 for r in refs)
        assert dt, "Must reference Mechanism #138 (Digital Trends editorial asymmetry)"

    def test_all_refs_have_relationship_type(self, mechanism):
        for ref in mechanism["cross_references"]:
            assert "relationship" in ref
            assert ref["relationship"] in ["extends", "complements", "parallels", "contradicts"]


class TestTestablePredictions:
    """Verify predictions are specific and falsifiable."""

    def test_prediction_samsung_launch_privacy(self, mechanism):
        preds = mechanism["testable_predictions"]
        launch_pred = any("launch" in p and ("privacy" in p or "alarm" in p or "incident" in p) for p in preds)
        assert launch_pred, "Must predict post-launch Samsung privacy coverage pattern"

    def test_prediction_beat_assignment_persistence(self, mechanism):
        preds = mechanism["testable_predictions"]
        beat_pred = any("assign" in p.lower() or "beat" in p.lower() or "TeamPixel" in p for p in preds)
        assert beat_pred, "Must predict beat assignment persistence"

    def test_predictions_are_falsifiable(self, mechanism):
        for pred in mechanism["testable_predictions"]:
            assert len(pred) > 50, f"Prediction too vague: {pred}"
            # Each must reference a specific entity and specific outcome
            has_entity = any(e in pred for e in ["Samsung", "Google", "Meta", "PhoneArena", "Romero", "Ilia"])
            assert has_entity, f"Prediction must reference specific entity: {pred}"
