"""
Cross-entity analysis: Inc.com (Mansueto Ventures) Privacy Vocabulary Redirected Attribution

Mechanism #137 — Type A: Competitor Coverage Deep Dive
Publication+Competitor pair: Inc.com covering Samsung/Google vs Meta smart glasses

KEY FINDING — PRIVACY VOCABULARY REDIRECTED ATTRIBUTION:
Inc.com (Mansueto Ventures) published "Samsung and Google's New Smart Glasses Have a Secret
Weapon That Meta Can't Easily Copy" by Connor Jewiss on July 29, 2026. The article spends
3 paragraphs detailing Meta's privacy scandals (Kenya contractors, FTC investigation,
Senate letter from Markey/Wyden/Merkley), presents Samsung's privacy claim at face value
("At Samsung, privacy is not an afterthought" — Samsung exec James Choi), and applies ZERO
privacy scrutiny to Samsung/Google's identical camera+AI architecture (same Snapdragon AR1
Gen 1 chip, same camera capability, same AI processing, same data collection requirements).

Privacy vocabulary count:
  Meta-directed: 7+ alarm terms ("intimate footage," "contractors in Kenya," "facial
  recognition," "stalking and harassment," "surveillance," "nonconsensual recording,"
  "backlash")
  Samsung/Google-directed: 0 alarm terms (Samsung exec claim taken at face value)
  Ratio: ∞:1

CROSS-ENTITY CONTRAST AT INC.COM:
Meta articles use "scandal" language (Soren Kaplan: "The Real Problem With Meta's AI
Tracking Scandal," "The Same Legal Theory Used Against Meta Is Now Coming for AI").
Google articles use aspirational framing (Jason Aten: "At I/O, Google Just Shipped Apple's
AI Promises"; Kit Eaton: "Google May Have Just Found a Way to Beat Nvidia"; Georgia Fearn:
Hassabis as responsible AI regulator). Mild Google criticism exists (Kevin Haynes on Google
Earth AI) but never uses "scandal" language.

FINANCIAL CONTEXT:
Mansueto Ventures revenue $23.1M (ZoomInfo), 55% from advertising (Digiday 2025).
Google Analytics 4 in tech stack (LeadIQ), standard Google programmatic/search dependency.
Joe Mansueto founded Morningstar (tracks Alphabet stock). ZERO Meta content licensing deals,
ZERO Meta advertising partnerships specific to Mansueto.

5 CONFOUNDERS:
1. STRONG: Meta genuinely has worse privacy track record (Cambridge Analytica legacy,
   Kenya contractors confirmed)
2. STRONG: Samsung/Google glasses hadn't shipped yet — no real-world privacy incidents
3. MODERATE: Article genre is competitive analysis, not investigation — naturally positions
   challenger vs incumbent
4. MODERATE: Samsung/Google explicitly made privacy positioning part of launch strategy —
   covering it is newsworthy
5. WEAK: Different ownership structures (Meta owns social graphs; Samsung/Google own
   search/ecosystem data differently)

3 FALSIFIABLE PREDICTIONS:
1. When Samsung/Google glasses ship (Fall 2026), Inc.com will NOT apply "scandal" framing
   to comparable Google data collection revelations
2. Inc.com coverage of Google's Personal Intelligence feature (Gmail, Calendar access) will
   receive softer privacy vocabulary than comparable Meta AI features
3. Inc.com will NOT run "Samsung's Smart Glasses Tracking Scandal" or equivalent loaded
   headline when Samsung/Google camera privacy issues emerge post-launch

SOURCE URLS:
- Inc.com Samsung/Google glasses article (Jul 29): https://www.inc.com/connor-jewiss/samsung-and-googles-new-smart-glasses-have-a-secret-weapon-that-meta-cant-easily-copy/91380954
- Inc.com Meta AI tracking scandal (Jul 14): https://www.inc.com/soren-kaplan/the-real-problem-with-metas-ai-tracking-scandal-isnt-the-data-leak/91373167
- Inc.com Meta legal theory (Jul 28): http://www.inc.com/soren-kaplan/the-same-legal-theory-used-against-meta-is-now-coming-for-ai/91380693
- Inc.com Google I/O (May 21): http://www.inc.com/jason-aten/at-i-o-google-just-shipped-apples-ai-promises/91191832
- Inc.com Google vs Nvidia (Jul 21): https://www.inc.com/kit-eaton/google-may-have-just-found-a-way-to-beat-nvidia-at-its-own-ai-game/91377317
- Inc.com DeepMind watchdog (Jul 15): https://www.inc.com/georgia-fearn/google-deepmind-founder-wall-street-style-watchdog-stop-dangerous-ai/91373798
- Inc.com Google Earth AI (Aug 2): http://www.inc.com/kevin-haynes/google-earths-new-ai-feature-could-create-false-images-of-real-places-it-lasted-1-day/91383508
"""

import pathlib
import re

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


def _load_entities() -> dict:
    return yaml.safe_load(
        (_PROFILES / "competitor-entities.yaml").read_text()
    )


def _find_mechanism_137() -> dict:
    """Find mechanism #137 in the research YAML (any top-level section)."""
    research = _load_research()
    for section in research.values():
        if isinstance(section, dict):
            if section.get("mechanism_id") == 137:
                return section
            for v in section.values():
                if isinstance(v, dict) and v.get("mechanism_id") == 137:
                    return v
    return None


# ===================================================================
# 1. MECHANISM EXISTENCE AND STRUCTURAL INTEGRITY
# ===================================================================


class TestMechanism137StructuralIntegrity:
    """Verify mechanism #137 exists with all required fields."""

    def test_mechanism_exists(self):
        """Mechanism #137 must exist in competitor-coverage-research.yaml."""
        mech = _find_mechanism_137()
        assert mech is not None, "Mechanism #137 must exist"

    def test_mechanism_id_is_137(self):
        """Mechanism ID must be exactly 137."""
        mech = _find_mechanism_137()
        assert mech is not None
        assert mech["mechanism_id"] == 137

    def test_has_finding_summary(self):
        """Mechanism #137 must have a finding_summary."""
        mech = _find_mechanism_137()
        assert mech is not None
        assert mech.get("finding_summary"), "Must have finding_summary"
        assert len(mech["finding_summary"]) > 100, "Finding summary should be substantive"

    def test_has_discovery_date(self):
        """Mechanism #137 must have discovery_date 2026-08-16."""
        mech = _find_mechanism_137()
        assert mech is not None
        assert mech.get("discovery_date") == "2026-08-16"

    def test_rotation_type_a(self):
        """Mechanism #137 is Type A: Competitor Coverage Deep Dive."""
        mech = _find_mechanism_137()
        assert mech is not None
        assert mech.get("rotation_type") == "A"

    def test_has_source_urls(self):
        """Mechanism #137 must have >= 5 source URLs."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert len(urls) >= 5, f"Need >= 5 source URLs, got {len(urls)}"

    def test_source_urls_are_valid_format(self):
        """All source URLs must start with http:// or https://."""
        mech = _find_mechanism_137()
        assert mech is not None
        for url in mech.get("source_urls", []):
            assert url.startswith("http://") or url.startswith("https://"), (
                f"Invalid URL format: {url}"
            )

    def test_has_test_file_reference(self):
        """Mechanism #137 must reference this test file."""
        mech = _find_mechanism_137()
        assert mech is not None
        tf = mech.get("test_file", "")
        assert "test_inc_mansueto" in tf

    def test_has_journalist(self):
        """Must document the journalist."""
        mech = _find_mechanism_137()
        assert mech is not None
        journalist = mech.get("journalist", "")
        assert "Jewiss" in journalist or "Connor" in journalist

    def test_has_publication(self):
        """Must document the publication."""
        mech = _find_mechanism_137()
        assert mech is not None
        pub = mech.get("publication", "")
        assert "Inc" in pub


# ===================================================================
# 2. PRIVACY VOCABULARY REDIRECTED ATTRIBUTION
# ===================================================================


class TestIncPrivacyVocabularyRedirectedAttribution:
    """Verify the core privacy vocabulary asymmetry between Meta and Samsung/Google."""

    def test_meta_privacy_alarm_term_count(self):
        """Meta receives 7+ privacy alarm terms in the Samsung/Google article."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        meta_count = pv.get("meta_directed_alarm_terms_count", 0)
        assert meta_count >= 7, f"Meta should have >= 7 alarm terms, got {meta_count}"

    def test_samsung_google_privacy_alarm_term_count(self):
        """Samsung/Google receives 0 privacy alarm terms."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        sg_count = pv.get("samsung_google_alarm_terms_count", 0)
        assert sg_count == 0, f"Samsung/Google should have 0 alarm terms, got {sg_count}"

    def test_privacy_vocabulary_ratio_infinite(self):
        """Privacy vocabulary ratio is infinite (7+:0)."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        ratio = pv.get("ratio", "")
        assert "inf" in str(ratio).lower() or "∞" in str(ratio), (
            f"Ratio should be infinite, got {ratio}"
        )

    def test_meta_alarm_terms_include_kenya(self):
        """Meta alarm terms include Kenya contractors reference."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        terms = pv.get("meta_directed_alarm_terms", [])
        terms_lower = [t.lower() for t in terms]
        assert any("kenya" in t for t in terms_lower), (
            f"Must include Kenya contractors reference: {terms}"
        )

    def test_meta_alarm_terms_include_facial_recognition(self):
        """Meta alarm terms include facial recognition."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        terms = pv.get("meta_directed_alarm_terms", [])
        terms_lower = [t.lower() for t in terms]
        assert any("facial recognition" in t for t in terms_lower), (
            f"Must include facial recognition: {terms}"
        )

    def test_meta_alarm_terms_include_surveillance(self):
        """Meta alarm terms include surveillance."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        terms = pv.get("meta_directed_alarm_terms", [])
        terms_lower = [t.lower() for t in terms]
        assert any("surveillance" in t for t in terms_lower), (
            f"Must include surveillance: {terms}"
        )

    def test_samsung_claim_taken_at_face_value(self):
        """Samsung exec's privacy claim taken at face value with zero scrutiny."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        assert pv.get("samsung_claim_at_face_value") is True

    def test_samsung_exec_quote_documented(self):
        """Samsung exec James Choi quote is documented."""
        mech = _find_mechanism_137()
        assert mech is not None
        pv = mech.get("privacy_vocabulary", {})
        quote = pv.get("samsung_exec_quote", "")
        assert "privacy" in quote.lower() and "afterthought" in quote.lower()

    def test_same_hardware_architecture(self):
        """Samsung/Google glasses share same Snapdragon AR1 Gen 1 chip as Meta."""
        mech = _find_mechanism_137()
        assert mech is not None
        hw = mech.get("hardware_parity", {})
        assert hw.get("same_chip") is True or "snapdragon" in str(hw).lower()


# ===================================================================
# 3. CROSS-ENTITY FRAMING ASYMMETRY AT INC.COM
# ===================================================================


class TestIncCrossEntityFramingAsymmetry:
    """Verify Meta articles use scandal language while Google articles use aspirational framing."""

    def test_meta_articles_documented(self):
        """At least 2 Meta articles at Inc.com documented."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        meta = ce.get("meta_articles", [])
        assert len(meta) >= 2, f"Need >= 2 Meta articles, got {len(meta)}"

    def test_google_articles_documented(self):
        """At least 3 Google articles at Inc.com documented."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        google = ce.get("google_articles", [])
        assert len(google) >= 3, f"Need >= 3 Google articles, got {len(google)}"

    def test_meta_articles_use_scandal_language(self):
        """Meta articles use 'scandal' or equivalently alarming language."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        meta = ce.get("meta_articles", [])
        alarm_count = sum(
            1 for a in meta
            if any(
                w in str(a.get("framing", "")).lower()
                for w in ["scandal", "alarm", "legal theory", "tracking"]
            )
        )
        assert alarm_count >= 1, "At least 1 Meta article should use alarm/scandal framing"

    def test_google_articles_use_aspirational_framing(self):
        """Google articles use aspirational/positive framing."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        google = ce.get("google_articles", [])
        aspirational_count = sum(
            1 for a in google
            if any(
                w in str(a.get("framing", "")).lower()
                for w in ["aspirational", "positive", "responsible", "shipped"]
            )
        )
        assert aspirational_count >= 2, (
            f"At least 2 Google articles should use aspirational framing, got {aspirational_count}"
        )

    def test_google_mild_criticism_no_scandal(self):
        """Google Earth AI article has mild criticism but never 'scandal' language."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        google = ce.get("google_articles", [])
        earth_articles = [
            a for a in google
            if "earth" in str(a.get("title", "")).lower()
            or "false images" in str(a.get("title", "")).lower()
        ]
        assert len(earth_articles) >= 1, "Google Earth article must be documented"
        for a in earth_articles:
            framing = str(a.get("framing", "")).lower()
            # Framing should indicate mild/factual tone, not scandal-level alarm
            assert "mild" in framing or "factual" in framing, (
                f"Google Earth article should have mild/factual framing, got: {framing}"
            )

    def test_all_cross_entity_articles_have_urls(self):
        """All cross-entity comparison articles have source URLs."""
        mech = _find_mechanism_137()
        assert mech is not None
        ce = mech.get("cross_entity_framing", {})
        for category in ["meta_articles", "google_articles"]:
            articles = ce.get(category, [])
            for a in articles:
                url = a.get("url", a.get("source_url", ""))
                assert url, f"Article missing URL: {a.get('title', 'unknown')}"


# ===================================================================
# 4. MANSUETO VENTURES FINANCIAL DEPENDENCIES
# ===================================================================


class TestMansuetofFinancialDependencies:
    """Verify Mansueto Ventures financial dependency documentation."""

    def test_mansueto_entity_exists(self):
        """mansueto_ventures entity must exist in competitor-entities.yaml."""
        entities = _load_entities()
        ent = entities.get("entities", {})
        if "mansueto_ventures" not in ent:
            ent = entities.get("publisher_entities", {})
        assert "mansueto_ventures" in ent, "mansueto_ventures must exist in entities or publisher_entities"

    def test_ad_revenue_share(self):
        """Mansueto Ventures ad revenue is 55% of total."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        share = mv.get("ad_revenue_share", "")
        assert "55" in str(share), f"Ad revenue share should be 55%, got {share}"

    def test_revenue_documented(self):
        """Mansueto Ventures revenue is $23.1M."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        rev = mv.get("revenue", "")
        assert "23.1" in str(rev), f"Revenue should be $23.1M, got {rev}"

    def test_google_analytics_4_in_tech_stack(self):
        """Mansueto Ventures uses Google Analytics 4."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        tech = mv.get("tech_stack", [])
        if isinstance(tech, list):
            assert any("google analytics" in str(t).lower() or "ga4" in str(t).lower() for t in tech)
        else:
            assert "google analytics" in str(tech).lower() or "ga4" in str(tech).lower()

    def test_google_programmatic_dependency(self):
        """Google programmatic advertising dependency documented."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        deps = mv.get("google_dependencies", [])
        assert any("programmatic" in str(d).lower() for d in deps), (
            f"Must document Google programmatic dependency: {deps}"
        )

    def test_google_search_dependency(self):
        """Google search traffic dependency documented."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        deps = mv.get("google_dependencies", [])
        assert any("search" in str(d).lower() for d in deps), (
            f"Must document Google search dependency: {deps}"
        )

    def test_zero_meta_financial_ties(self):
        """Zero Meta financial ties."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        meta_ties = mv.get("meta_financial_ties", "")
        assert meta_ties in ("none", "zero", None, "") or "none" in str(meta_ties).lower(), (
            f"Meta financial ties should be none, got {meta_ties}"
        )

    def test_morningstar_connection(self):
        """Joe Mansueto founded Morningstar (tracks Alphabet stock)."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        owner = str(mv.get("owner", ""))
        notes = str(mv.get("notes", mv.get("morningstar_connection", "")))
        combined = (owner + notes).lower()
        assert "morningstar" in combined or "mansueto" in owner.lower()

    def test_publications_include_inc(self):
        """Publications include Inc.com."""
        entities = _load_entities()
        mv = entities.get("entities", {}).get("mansueto_ventures") or entities.get("publisher_entities", {}).get("mansueto_ventures", {})
        pubs = mv.get("publications", [])
        assert any("inc" in str(p).lower() for p in pubs)


# ===================================================================
# 5. CONFOUNDERS
# ===================================================================


class TestConfounders:
    """Verify 5 confounders with proper strength ratings."""

    def test_five_confounders(self):
        """Must have exactly 5 confounders."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        assert len(confounders) == 5, f"Need 5 confounders, got {len(confounders)}"

    def test_two_strong_confounders(self):
        """Must have exactly 2 STRONG confounders."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        strong = [c for c in confounders if c.get("strength", "").upper() == "STRONG"]
        assert len(strong) == 2, f"Need 2 STRONG confounders, got {len(strong)}"

    def test_strong_confounder_meta_track_record(self):
        """STRONG confounder: Meta genuinely has worse privacy track record."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        strong = [c for c in confounders if c.get("strength", "").upper() == "STRONG"]
        factor_text = " ".join(str(c.get("factor", "")) + str(c.get("detail", "")) for c in strong).lower()
        assert "track record" in factor_text or "cambridge" in factor_text or "kenya" in factor_text

    def test_strong_confounder_not_shipped(self):
        """STRONG confounder: Samsung/Google glasses hadn't shipped yet."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        strong = [c for c in confounders if c.get("strength", "").upper() == "STRONG"]
        factor_text = " ".join(str(c.get("factor", "")) + str(c.get("detail", "")) for c in strong).lower()
        assert "shipped" in factor_text or "ship" in factor_text or "haven" in factor_text

    def test_moderate_confounders_exist(self):
        """Must have MODERATE confounders."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        moderate = [c for c in confounders if c.get("strength", "").upper() == "MODERATE"]
        assert len(moderate) >= 2, f"Need >= 2 MODERATE confounders, got {len(moderate)}"

    def test_weak_confounder_exists(self):
        """Must have at least 1 WEAK confounder."""
        mech = _find_mechanism_137()
        assert mech is not None
        confounders = mech.get("confounders", [])
        weak = [c for c in confounders if c.get("strength", "").upper() == "WEAK"]
        assert len(weak) >= 1, f"Need >= 1 WEAK confounder, got {len(weak)}"

    def test_all_confounders_have_detail(self):
        """All confounders must have a detail field."""
        mech = _find_mechanism_137()
        assert mech is not None
        for c in mech.get("confounders", []):
            assert c.get("detail"), f"Confounder missing detail: {c.get('factor')}"


# ===================================================================
# 6. FALSIFIABLE PREDICTIONS
# ===================================================================


class TestFalsifiablePredictions:
    """Verify 3 testable predictions documented."""

    def test_three_predictions(self):
        """Must have exactly 3 falsifiable predictions."""
        mech = _find_mechanism_137()
        assert mech is not None
        predictions = mech.get("testable_predictions", mech.get("falsifiable_predictions", []))
        assert len(predictions) == 3, f"Need 3 predictions, got {len(predictions)}"

    def test_prediction_post_launch_scandal_framing(self):
        """Prediction 1: Inc.com won't apply scandal framing to Samsung/Google post-launch."""
        mech = _find_mechanism_137()
        assert mech is not None
        predictions = mech.get("testable_predictions", mech.get("falsifiable_predictions", []))
        preds_text = " ".join(str(p.get("prediction", p) if isinstance(p, dict) else p) for p in predictions).lower()
        assert "scandal" in preds_text or "ship" in preds_text

    def test_prediction_personal_intelligence(self):
        """Prediction 2: Google's Personal Intelligence gets softer vocabulary."""
        mech = _find_mechanism_137()
        assert mech is not None
        predictions = mech.get("testable_predictions", mech.get("falsifiable_predictions", []))
        preds_text = " ".join(str(p.get("prediction", p) if isinstance(p, dict) else p) for p in predictions).lower()
        assert "personal intelligence" in preds_text or "gmail" in preds_text or "softer" in preds_text

    def test_prediction_samsung_headline(self):
        """Prediction 3: No Samsung scandal headline post-launch."""
        mech = _find_mechanism_137()
        assert mech is not None
        predictions = mech.get("testable_predictions", mech.get("falsifiable_predictions", []))
        preds_text = " ".join(str(p.get("prediction", p) if isinstance(p, dict) else p) for p in predictions).lower()
        assert "samsung" in preds_text


# ===================================================================
# 7. CROSS-REFERENCES
# ===================================================================


class TestCrossReferences:
    """Verify mechanism #137 properly cross-references related mechanisms."""

    def test_references_mechanism_30(self):
        """Must reference #30 (genre-determined framing)."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 30 in ref_ids, f"Must reference #30, have {ref_ids}"

    def test_references_mechanism_33(self):
        """Must reference #33 (facial recognition parity)."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 33 in ref_ids, f"Must reference #33, have {ref_ids}"

    def test_references_mechanism_130(self):
        """Must reference #130 (Snap competitive privacy positioning amplification)."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 130 in ref_ids, f"Must reference #130, have {ref_ids}"

    def test_references_mechanism_132(self):
        """Must reference #132 (Andy Boxall cross-entity privacy vocabulary inversion)."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 132 in ref_ids, f"Must reference #132, have {ref_ids}"

    def test_references_mechanism_134(self):
        """Must reference #134 (WIRED remediation silence)."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 134 in ref_ids, f"Must reference #134, have {ref_ids}"

    def test_at_least_five_cross_references(self):
        """Must have at least 5 cross-references."""
        mech = _find_mechanism_137()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        assert len(refs) >= 5, f"Need >= 5 cross-references, got {len(refs)}"


# ===================================================================
# 8. SOURCE URL COVERAGE
# ===================================================================


class TestSourceURLCoverage:
    """Verify all key source URLs are present and valid format."""

    def test_samsung_google_primary_article_url(self):
        """Primary Samsung/Google glasses article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91380954" in u or "secret-weapon" in u for u in urls), (
            "Primary Samsung/Google article URL missing"
        )

    def test_meta_tracking_scandal_url(self):
        """Meta AI tracking scandal article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91373167" in u or "tracking-scandal" in u for u in urls), (
            "Meta tracking scandal URL missing"
        )

    def test_meta_legal_theory_url(self):
        """Meta legal theory article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91380693" in u or "legal-theory" in u for u in urls), (
            "Meta legal theory URL missing"
        )

    def test_google_io_url(self):
        """Google I/O aspirational article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91191832" in u or "shipped-apples" in u for u in urls), (
            "Google I/O URL missing"
        )

    def test_google_nvidia_url(self):
        """Google vs Nvidia article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91377317" in u or "beat-nvidia" in u for u in urls), (
            "Google vs Nvidia URL missing"
        )

    def test_deepmind_watchdog_url(self):
        """DeepMind watchdog article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91373798" in u or "watchdog" in u for u in urls), (
            "DeepMind watchdog URL missing"
        )

    def test_google_earth_url(self):
        """Google Earth AI article URL is in source_urls."""
        mech = _find_mechanism_137()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert any("91383508" in u or "google-earth" in u for u in urls), (
            "Google Earth AI URL missing"
        )

    def test_all_urls_are_http(self):
        """All source URLs use http or https scheme."""
        mech = _find_mechanism_137()
        assert mech is not None
        for url in mech.get("source_urls", []):
            assert re.match(r"https?://", url), f"URL must start with http(s)://: {url}"
