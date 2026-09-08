"""Type A #592 (2026-09-07 17:00 PDT): The Verge x Google adversarial-litigation
boundary replication.

PMC (The Verge parent) sues Google on TWO fronts (AI Overviews D.D.C. Sep
2025; adtech SDNY Jan 2026) while admitting ad-revenue dependence on Google's
exchange - the strongest adversarial publisher-entity posture in the corpus,
stronger than NYT's single OpenAI suit in #471. The naive negative-sign
prediction says Verge Google coverage should run adversarial across domains.
Observed: Verge non-litigation Google coverage (May-Jul 2026, n=3) runs
neutral-to-product-forward (avg -0.0833) while same-window Verge Meta glasses
coverage runs adversarial (avg -0.55, Victoria Song columns): illustrative
delta +0.4667, n.s.

This replicates the NYT #471 boundary condition at a second adversarial
posture publication: adversarial financial posture predicts adversarial tone
WITHIN the litigation domain only. It also resolves the adversarial-posture
confound named in #492 as domain-bounded, not entity-wide. The three Google
items: the I/O 2026 Android XR glasses news piece (slug-derived title,
0.0), the May 19 2026 Gemini sparkle icon Docs/Workspace piece (attested
secondary quote, -0.05), and Preston's Jul 22 2026 Samsung/Google hands-on
(dek-level privacy equivalence carried from #492, -0.2). The three Meta
comparators are carried from #492's meta_comparator_set; two lack verbatim
URLs and carry url: null with explicit evidence-tier labels.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading search
in iteration-log.md; relative newest-first ordering between neighbors, never
absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERGE_PROFILE = os.path.join(REPO, "profiles", "the-verge.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_590_verge_google_adversarial_litigation_boundary_replication"

ANDROID_XR_URL = "https://www.theverge.com/tech/933125/android-xr-samsung-warby-parker-gentle-monster-project-aura-xreal-google-io-2026"
GEMINI_ICON_URL = "https://www.theverge.com/tech/931752/google-io-2026-gemini-icon-docs-workspace"
PRESTON_MIRROR_URL = "https://technewstube.com/theverge/1852147/samsungs-smart-glasses-actually-look-like/"
HOLDS_CARDS_MIRROR_URL = "https://www.aivanet.com/2026/07/with-smart-glasses-meta-holds-all-the-cards-but-fails-to-play-them-well/"

GOOGLE_URLS = (ANDROID_XR_URL, GEMINI_ICON_URL, PRESTON_MIRROR_URL)


def _mechanism():
    with open(VERGE_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["google"][MECH_KEY]


def _mechanism_text():
    return yaml.dump(_mechanism(), default_flow_style=False, sort_keys=False, allow_unicode=False)


def _segment(log_text, num):
    """Return the text of iteration #num's log entry (heading to next heading)."""
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
    starts = [pos for pos, n in headings if n == str(num)]
    assert starts, f"#{num} heading not found"
    start = starts[0]
    later = [pos for pos, _ in headings if pos > start]
    end = min(later) if later else len(log_text)
    return log_text[start:end]


class TestMechanism590Structure:
    def test_yaml_parses(self):
        with open(VERGE_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_google(self):
        with open(VERGE_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["google"]

    def test_mechanism_id_and_iteration(self):
        m = _mechanism()
        assert m["mechanism_id"] == 590
        assert m["iteration"] == 592
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-07 17:00 PDT"

    def test_required_metadata_fields(self):
        m = _mechanism()
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert "Verge" in m["publication_focus"]
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_six_articles(self):
        assert len(_mechanism()["articles"]) == 6

    def test_google_block_financial_tie_unchanged(self):
        with open(VERGE_PROFILE) as f:
            doc = yaml.safe_load(f)
        google = doc["competitor_relationships"]["google"]
        assert google["financial_tie"] == "adversarial_litigation"
        assert google["coverage_prediction"] == "adversarial"


class TestGoogleArticlesEvidence:
    def _google_articles(self):
        return [a for a in _mechanism()["articles"] if a["url"] in GOOGLE_URLS]

    def test_three_google_articles(self):
        assert len(self._google_articles()) == 3

    def test_android_xr_piece_slug_derived_not_first_hand(self):
        a = next(a for a in self._google_articles() if a["url"] == ANDROID_XR_URL)
        assert a["manual_illustrative_tone"] == 0.0
        assert a["register"] == "neutral_news_explainer"
        assert "NOT first-hand body text" in a["verification"]
        assert a["evidence_tier"] == "slug_plus_citation_context"

    def test_gemini_icon_piece_attested_secondary(self):
        a = next(a for a in self._google_articles() if a["url"] == GEMINI_ICON_URL)
        assert a["manual_illustrative_tone"] == -0.05
        assert "ai.nidal.cloud" in a["verification"]
        assert a["evidence_tier"] == "attested_secondary_quote"

    def test_preston_hands_on_carried_from_492(self):
        a = next(a for a in self._google_articles() if a["url"] == PRESTON_MIRROR_URL)
        assert a["manual_illustrative_tone"] == -0.2
        assert "Carried from #492" in a["verification"]
        assert "privacy problems as Meta's" in " ".join(a["key_phrases"])

    def test_google_tones_neutral_band(self):
        for a in self._google_articles():
            assert -0.25 <= a["manual_illustrative_tone"] <= 0.05, a["title"]


class TestMetaComparatorEvidence:
    def _meta_articles(self):
        return [a for a in _mechanism()["articles"] if a["entity"] == "meta"]

    def test_three_meta_articles(self):
        assert len(self._meta_articles()) == 3

    def test_led_tamper_carryover_no_verbatim_url(self):
        a = next(a for a in self._meta_articles() if "privacy light" in a["title"])
        assert a["url"] is None
        assert "Carried from #492" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.55

    def test_pervert_glasses_carryover_no_verbatim_url(self):
        a = next(a for a in self._meta_articles() if "pervert glasses" in a["title"])
        assert a["url"] is None
        assert "Carried from #492" in a["verification"]
        assert a["manual_illustrative_tone"] == -0.6

    def test_holds_all_cards_mirror_in_corpus(self):
        a = next(a for a in self._meta_articles() if "holds all the cards" in a["title"])
        assert a["url"] == HOLDS_CARDS_MIRROR_URL
        assert a["manual_illustrative_tone"] == -0.5
        assert "mass surveillance predator glasses" in " ".join(a["key_phrases"])

    def test_meta_tones_adversarial(self):
        for a in self._meta_articles():
            assert a["manual_illustrative_tone"] <= -0.5, a["title"]


class TestScorerReproduction:
    def test_delta_matches_profile(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["asymmetry_score"] == 0.4667

    def test_target_peer_means(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_entity"] == "google"
        assert s["peer_entities"] == ["meta"]
        assert s["target_avg_tone"] == -0.0833
        assert s["peer_avg_tone"] == -0.55
        # arithmetic check: google mean - meta mean
        assert round(s["target_avg_tone"] - s["peer_avg_tone"], 4) == 0.4667

    def test_means_reproduce_from_article_tones(self):
        articles = _mechanism()["articles"]
        google_tones = [a["manual_illustrative_tone"] for a in articles if a["entity"] == "google"]
        meta_tones = [a["manual_illustrative_tone"] for a in articles if a["entity"] == "meta"]
        assert round(sum(google_tones) / 3, 4) == -0.0833
        assert round(sum(meta_tones) / 3, 4) == -0.55

    def test_not_significant(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["is_significant"] is False

    def test_standing_rule_fields_not_calculated(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["confidence_interval"] == "NOT_CALCULATED"

    def test_manual_illustrative_note_present(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "correlation_not_causation" in s["methodology"]

    def test_discipline_block_present(self):
        m = _mechanism()
        assert "NOT_CALCULATED" in m["statistical_discipline"]
        assert "n=3 vs n=3" in m["statistical_discipline"]
        assert "+0.4667" in m["statistical_discipline"]

    def test_litigation_domain_control_present(self):
        m = _mechanism()
        assert "D.D.C., Sep 2025" in m["litigation_domain_control"]["ai_overviews_suit"]
        assert "SDNY, Jan 2026" in m["litigation_domain_control"]["adtech_suit"]


class TestSourceHygiene:
    def test_non_null_source_urls_https(self):
        m = _mechanism()
        for u in m["source_urls"]:
            assert u.startswith("https://"), u

    def test_four_source_urls_unique(self):
        m = _mechanism()
        assert len(m["source_urls"]) == 4
        assert len(set(m["source_urls"])) == 4

    def test_non_null_article_urls_match_source_urls(self):
        m = _mechanism()
        article_urls = {a["url"] for a in m["articles"] if a["url"] is not None}
        assert article_urls == set(m["source_urls"])

    def test_no_constructed_urls(self):
        urls = {a["url"] for a in _mechanism()["articles"] if a["url"] is not None}
        for expected in GOOGLE_URLS + (HOLDS_CARDS_MIRROR_URL,):
            assert expected in urls

    def test_no_em_dashes_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert "—" not in text
        assert "–" not in text

    def test_ascii_only_in_new_mechanism_text(self):
        _mechanism_text().encode("ascii")


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        conf = _mechanism()["confounders"]
        tiers = {c.split(":")[0] for c in conf}
        assert {"STRONG", "MODERATE", "WEAK"} <= tiers

    def test_evidence_tier_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "evidence-tier" in conf.lower()

    def test_product_maturity_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "news-peg" in conf.lower()

    def test_genre_confound_present(self):
        conf = " ".join(_mechanism()["confounders"])
        assert "genre" in conf.lower()

    def test_counter_evidence_present(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) >= 2
        assert any("illustrative-band" in c for c in ce)

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "Correlation is not causation" in m["finding"]

    def test_research_method_names_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["research_method"]

    def test_cross_references_in_finding(self):
        finding = _mechanism()["finding"]
        for ref in ("492", "471", "589", "557", "547"):
            assert ref in finding

    def test_distinct_from_names_replication(self):
        df = " ".join(_mechanism()["distinct_from"])
        assert "REPLICATION" in df


class TestIterationLogEntry:
    def test_592_heading_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 592)
        assert "Verge x Google" in seg

    def test_rotation_transparency(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 592)
        assert "591 E -> 592 A" in seg
