"""#416 Type B: NYT Policy Beat Adversarial Spillover - Cecilia Kang Cross-Entity Tracking Aug 31 2026 05:00 PDT

Journalist: Cecilia Kang NYT national technology correspondent DC policy beat 2015-present.
Fresh journalist no prior competitor_coverage in journalists.yaml.
Corpus 3 articles 2024-2026 same journalist.
"""

import pytest
import yaml


@pytest.fixture(scope="module")
def journalists():
    with open("profiles/careers/journalists.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def kang_entry(journalists):
    for j in journalists.get("journalists", []):
        if j.get("name") == "Cecilia Kang":
            return j
    pytest.fail("Cecilia Kang entry not found")


@pytest.fixture(scope="module")
def cross_entity(kang_entry):
    return kang_entry.get("competitor_coverage", {}).get("cross_entity_analysis", {})


class TestKangFreshJournalist:
    def test_kang_exists(self, kang_entry):
        assert kang_entry is not None

    def test_has_competitor_coverage(self, kang_entry):
        assert "competitor_coverage" in kang_entry

    def test_has_cross_entity_analysis(self, cross_entity):
        assert cross_entity

    def test_mechanism_id_416(self, cross_entity):
        assert cross_entity.get("mechanism_id") == 416

    def test_mechanism_name(self, cross_entity):
        assert "nyt_policy_beat" in cross_entity.get("mechanism_name", "")

    def test_pattern(self, cross_entity):
        assert "adversarial_spillover" in cross_entity.get("pattern", "")

    def test_journalist_name(self, cross_entity):
        assert cross_entity.get("journalist") == "Cecilia Kang"

    def test_publication_nyt(self, cross_entity):
        assert "New York Times" in cross_entity.get("publication", "")

    def test_date_range(self, cross_entity):
        assert "2024-04-06" in cross_entity.get("date_range", "")


class TestCorpus:
    def test_meta_coverage_exists(self, cross_entity):
        assert "meta_coverage" in cross_entity

    def test_google_coverage_exists(self, cross_entity):
        assert "google_coverage" in cross_entity

    def test_cross_entity_anchor_exists(self, cross_entity):
        assert "cross_entity_anchor" in cross_entity

    def test_meta_title(self, cross_entity):
        assert "Meta to Pay Up" in cross_entity["meta_coverage"]["title"]

    def test_google_title(self, cross_entity):
        assert "Google" in cross_entity["google_coverage"]["title"]

    def test_anchor_title(self, cross_entity):
        assert "tech giants cut corners" in cross_entity["cross_entity_anchor"]["title"].lower()

    def test_meta_tone_manual_illustrative(self, cross_entity):
        assert cross_entity["meta_coverage"]["tone_manual_illustrative"] == -6

    def test_google_tone_manual_illustrative(self, cross_entity):
        assert cross_entity["google_coverage"]["tone_manual_illustrative"] == -1

    def test_anchor_tone_manual_illustrative(self, cross_entity):
        assert cross_entity["cross_entity_anchor"]["tone_manual_illustrative"] == -2

    def test_meta_privacy_count(self, cross_entity):
        assert cross_entity["meta_coverage"]["privacy_terms_count"] == 7

    def test_google_privacy_zero(self, cross_entity):
        assert cross_entity["google_coverage"]["privacy_terms_count"] == 0

    def test_sources_exist(self, cross_entity):
        assert len(cross_entity.get("sources", [])) >= 5


class TestAnalysis:
    def test_analysis_exists(self, cross_entity):
        assert "analysis" in cross_entity

    def test_headline_tone_adversarial_vs_procedural(self, cross_entity):
        ht = cross_entity["analysis"]["headline_tone"]
        assert "adversarial" in ht.lower()
        assert "procedural" in ht.lower()

    def test_agency_attribution(self, cross_entity):
        aa = cross_entity["analysis"]["agency_attribution"]
        assert "Meta" in aa and "Google" in aa

    def test_confounder_strong_exists(self, cross_entity):
        assert "confounders_strong" in cross_entity["analysis"]

    def test_financial_relationship_note_correlation_not_causation(self, cross_entity):
        note = cross_entity["analysis"]["financial_relationship_note"]
        assert "correlation does not imply causation" in note.lower()

    def test_editorial_independence_acknowledged(self, cross_entity):
        assert cross_entity["analysis"]["editorial_independence_acknowledgment"] is True


class TestMethodology:
    def test_no_p_value_calculated(self, cross_entity):
        desc = cross_entity.get("description", "")
        assert "NOT CALCULATED" in desc or "p_value" in desc.lower()
