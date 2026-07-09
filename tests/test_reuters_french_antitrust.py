"""Tests for Reuters French antitrust article improvements (Jul 8, 2026).

Covers:
1. "The Information" false positive — lowercase "the information" as a
   common noun must NOT match the publication entity.
2. New entity clusters — European regulatory bodies and French media
   associations (DVP, APIG, Le Monde, Les Echos, Autorité de la concurrence).
3. New topic: content_licensing — publishing fees, neighboring rights,
   remuneration.
4. Source extraction — DVP as an organizational source with appositive
   clause between name and verb.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic

# -------------------------------------------------------------------------
# Article text for this test suite
# -------------------------------------------------------------------------
REUTERS_ARTICLE = (
    "France's competition authority on Wednesday ordered Meta Platforms to "
    "put forward a payment plan and resume talks with French media groups "
    "that are seeking a year of unpaid fees for the use of their content online.\n\n"
    "The case is one of a growing number between publishers and tech companies "
    "over the use of content published on social media or used for AI training "
    "that have triggered litigation.\n\n"
    "Lodged by French media associations DVP and APIG, the French complaint "
    "alleged that Meta attempted to impose its own method for calculating fees "
    "for the re-use of published content on its services, while refusing to "
    "provide the information needed for them to evaluate the remuneration.\n\n"
    "The authority said Meta likely abused its dominant position, and it "
    "ordered the Facebook owner to put forward details of its payment plan "
    "within 15 days.\n\n"
    "In a statement, Meta said it disagreed with the competition authority's "
    "decisions but would engage with the process.\n\n"
    '"We remain committed to reaching a fair deal with DVP and APIG and we '
    'hope these decisions will mean the publishers now engage in good faith," '
    "it said in an emailed statement.\n\n"
    "Media rights group DVP, which includes the newspapers Le Monde and "
    "Les Echos, said it was satisfied with the decision and welcomed the "
    "renewed talks."
)


# =========================================================================
# 1. "The Information" false positive
# =========================================================================

class TestTheInformationFalsePositive:
    """Lowercase 'the information' must not be detected as The Information."""

    def test_lowercase_the_information_not_matched(self):
        """'the information needed' is a common noun phrase, not the pub."""
        text = (
            "Meta refused to provide the information needed for them "
            "to evaluate the remuneration."
        )
        entities = detect_entities(text)
        entity_names = [e.canonical_name for e in entities]
        cluster_names = [e.cluster for e in entities]
        # Should NOT have "The Information" as Media/Publications
        assert "The Information" not in entity_names, (
            "Lowercase 'the information' incorrectly matched as The Information"
        )
        # Should also not appear in any cluster under that name
        for e in entities:
            if e.cluster == "Media/Publications":
                assert e.canonical_name != "The Information"

    def test_capitalized_the_information_still_matched(self):
        """Properly capitalised 'The Information' should still match."""
        text = (
            "The Information reported that Meta is working on a new "
            "hardware product for 2027."
        )
        entities = detect_entities(text)
        entity_names = [e.canonical_name for e in entities]
        assert "The Information" in entity_names, (
            "Capitalised 'The Information' should be detected"
        )

    def test_mixed_case_article_no_false_positive(self):
        """Full Reuters article should not have 'The Information' entity."""
        entities = detect_entities(REUTERS_ARTICLE)
        the_info_matches = [
            e for e in entities
            if e.canonical_name == "The Information"
        ]
        assert len(the_info_matches) == 0, (
            f"Found {len(the_info_matches)} false positive 'The Information' "
            f"matches in article"
        )


# =========================================================================
# 2. New entity clusters
# =========================================================================

class TestEuropeanRegulatoryEntities:
    """European regulatory body entities."""

    def test_autorite_de_la_concurrence(self):
        """French competition authority detected."""
        text = "The Autorité de la concurrence imposed fines on Meta."
        entities = detect_entities(text)
        clusters = {e.cluster for e in entities}
        assert "EU Regulatory" in clusters

    def test_frances_competition_authority(self):
        """'France's competition authority' detected."""
        text = "France's competition authority ordered Meta to comply."
        entities = detect_entities(text)
        names = [e.canonical_name for e in entities]
        assert "France's competition authority" in names


class TestFrenchMediaAssociationEntities:
    """French media association entities — DVP, APIG, Le Monde, Les Echos."""

    def test_dvp_detected(self):
        """DVP detected as French Media Associations entity."""
        text = "DVP lodged a complaint against Meta over publishing fees."
        entities = detect_entities(text)
        dvp_hits = [e for e in entities if e.canonical_name == "DVP"]
        assert len(dvp_hits) >= 1
        assert dvp_hits[0].cluster == "French Media Associations"

    def test_apig_detected(self):
        """APIG detected as French Media Associations entity."""
        text = "APIG represents major French publishers."
        entities = detect_entities(text)
        apig_hits = [e for e in entities if e.canonical_name == "APIG"]
        assert len(apig_hits) >= 1
        assert apig_hits[0].cluster == "French Media Associations"

    def test_le_monde_detected(self):
        """Le Monde detected as French Media Associations entity."""
        text = "DVP includes newspapers Le Monde and Les Echos."
        entities = detect_entities(text)
        names = [e.canonical_name for e in entities]
        assert "Le Monde" in names

    def test_les_echos_detected(self):
        """Les Echos detected as French Media Associations entity."""
        text = "DVP includes newspapers Le Monde and Les Echos."
        entities = detect_entities(text)
        names = [e.canonical_name for e in entities]
        assert "Les Echos" in names

    def test_full_article_entity_coverage(self):
        """Full Reuters article should detect DVP, APIG, Le Monde, Les Echos."""
        entities = detect_entities(REUTERS_ARTICLE)
        names = {e.canonical_name for e in entities}
        expected = {"DVP", "APIG", "Le Monde", "Les Echos"}
        missing = expected - names
        assert not missing, f"Missing entities in article: {missing}"


# =========================================================================
# 3. content_licensing topic
# =========================================================================

class TestContentLicensingTopic:
    """New content_licensing topic bucket."""

    def test_full_article_classifies_content_licensing(self):
        """Reuters French antitrust article should match content_licensing."""
        results = classify_topic(REUTERS_ARTICLE, top_n=10)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics, (
            f"content_licensing not in classified topics: {topics}"
        )

    def test_publishing_fees_keyword(self):
        """'publishing fees' triggers content_licensing."""
        text = "Publishers are demanding publishing fees from tech platforms."
        results = classify_topic(text, top_n=5)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics

    def test_neighboring_rights_keyword(self):
        """'neighboring rights' triggers content_licensing."""
        text = "The EU directive on neighboring rights requires platforms to pay."
        results = classify_topic(text, top_n=5)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics

    def test_remuneration_keyword(self):
        """'remuneration' triggers content_licensing."""
        text = "The publishers could not evaluate the remuneration offered."
        results = classify_topic(text, top_n=5)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics

    def test_content_fees_keyword(self):
        """'content fees' triggers content_licensing."""
        text = "Negotiations over content fees have stalled."
        results = classify_topic(text, top_n=5)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics

    def test_news_licensing_keyword(self):
        """'news licensing' triggers content_licensing."""
        text = "News licensing agreements are being renegotiated globally."
        results = classify_topic(text, top_n=5)
        topics = [r.topic for r in results]
        assert "content_licensing" in topics


# =========================================================================
# 4. Source extraction — DVP
# =========================================================================

class TestDVPSourceExtraction:
    """DVP should be extracted as an organizational source."""

    def test_dvp_source_in_full_article(self):
        """DVP should appear as a source in the full Reuters article."""
        sources = extract_sources(REUTERS_ARTICLE)
        source_names = [s.name.lower() for s in sources]
        # DVP said it was satisfied — should be captured
        assert any("dvp" in n for n in source_names), (
            f"DVP not extracted as source. Found: {[s.name for s in sources]}"
        )

    def test_dvp_source_type_organizational(self):
        """DVP source should be typed as organizational."""
        sources = extract_sources(REUTERS_ARTICLE)
        dvp_sources = [s for s in sources if "dvp" in s.name.lower()]
        if dvp_sources:
            assert dvp_sources[0].source_type == "organizational"

    def test_meta_also_extracted_as_source(self):
        """Meta should still be extracted as a source (regression check)."""
        sources = extract_sources(REUTERS_ARTICLE)
        source_names = [s.name.lower() for s in sources]
        assert any("meta" in n for n in source_names), (
            f"Meta not extracted as source. Found: {[s.name for s in sources]}"
        )

    def test_acronym_with_appositive_clause(self):
        """Acronym org with appositive clause should still match."""
        text = (
            "DVP, which includes several major newspapers, said it was "
            "satisfied with the ruling."
        )
        sources = extract_sources(text)
        source_names = [s.name for s in sources]
        assert any("DVP" in n for n in source_names), (
            f"DVP with appositive not extracted. Found: {source_names}"
        )
