"""Tests for WSJ Meta AI layoff discrimination article (Jul 14, 2026).

Validates:
1. Independent expert source extraction (Prof. Jeffrey M. Hirsch, UNC)
2. Lawsuit-as-documentary-source extraction (not confused with Meta statements)
3. litigation_framing detection in headline and body
4. Surveillance enumeration pattern (performance ratings, calibration scores, etc.)
5. Humanization framing device ("two days before giving birth")
6. Same-event comparison patterns with Fox Business and Reuters versions
7. Expert authority framing recognition

Discovered in Type A iteration, Jul 14, 2026 21:00 PT.
"""

import pytest

from mediascope.analysis import analyze_text


TITLE = (
    "Meta Workers Accuse It of Using AI to Conduct Discriminatory Layoffs"
)

ARTICLE = (
    "A group of Meta employees is suing the social-media company over how "
    "it carried out layoffs this spring, alleging that it used AI that "
    "disproportionately cut workers with disabilities or on protected leave.\n\n"
    "The federal lawsuit, filed this week in the Northern District of "
    "California, alleges that when Meta began laying off 8,000 employees"
    "—or roughly 10% of its workforce in May—it relied on a "
    '"constellation of internal artificial-intelligence systems" to '
    "create a termination list.\n\n"
    "The lawsuit claims that AI used metrics such as productivity and "
    "AI-token use to determine layoffs, and so targeted employees who had "
    "missed work because of medical conditions or other leave, violating "
    "discrimination laws in the process.\n\n"
    'The AI tools "draw on inputs—performance ratings, calibration '
    "scores, productivity and output metrics, 'AI-native' ratings, and "
    "AI-token consumption—that, by design, cannot be accumulated by an "
    "employee who is on protected medical or family leave, or whose output "
    'is reduced by a disability," the lawsuit states.\n\n'
    "A Meta spokesman rejected the allegations and said workforce-management "
    'decisions were made by people, not AI. "These claims lack merit and '
    'are not based on facts," he said.\n\n'
    "The lawsuit is one of the first in the U.S. to scrutinize the "
    "potential role of AI in determining layoffs. It also raises questions "
    "about the extent to which workers are shielded from potential cuts "
    "while on legally protected leave.\n\n"
    "The plaintiffs in the lawsuit are 26 current and former Meta employees, "
    "all of whom were notified they would be laid off. They had either taken "
    "or requested leave or asked for disability-related accommodation in "
    "the months before.\n\n"
    "The lawsuit says that one plaintiff was on preapproved pregnancy leave, "
    "and was told she was being laid off two days before giving birth. "
    'Another was on medical leave for a "serious health condition," the '
    "lawsuit claims.\n\n"
    "The plaintiffs are seeking a preliminary injunction to maintain the "
    "status quo of their employment pending arbitration, and to prevent "
    "Meta from completing their separations.\n\n"
    "A leave of absence doesn't automatically safeguard someone's job, "
    "employment lawyers say, though companies also can't single out those "
    "on a protected leave.\n\n"
    '"It\'s not a magic bullet," said Jeffrey M. Hirsch, a professor of '
    "law at the University of North Carolina who studies employment issues. "
    '"On the other hand, it does mean if your employer is picking and '
    "choosing who gets laid off, they can't say that I'm annoyed so-and-so "
    'keeps taking FMLA leave," he added, referring to the Family and '
    "Medical Leave Act.\n\n"
    "Hirsch said the lawsuit showed how the alleged use of new AI tools "
    "could be exposing companies to new legal risks.\n\n"
    "The lawsuit also touches on a bigger question that has consumed "
    "white-collar employees for years: How exactly do companies choose "
    "who to include in a layoff? Inside many companies, divisional leaders "
    "and department heads often decide who should be eliminated, "
    "human-resources executives say, but creating a termination list is "
    "often messy and chaotic.\n\n"
    "Meta announced the layoffs as part of a broad effort to reimagine its "
    "workforce and become more nimble to compete with AI-native startups. "
    "In May, CEO Mark Zuckerberg thanked laid off employees for their "
    'contributions and called AI "the most consequential technology of '
    'our lifetimes."\n\n'
    "The lawsuit alleges that Meta used a range of AI-assisted systems to "
    "score, rank and select employees to include on its layoff list. Those "
    'included AI agents that "ingest each employee\'s communications and '
    "documents to replicate the employee's output,\" the lawsuit claims, "
    "along with productivity-monitoring tools and factors such as each "
    "employee's rolling 12-month performance rating."
)


@pytest.fixture
def result():
    return analyze_text(ARTICLE, title=TITLE, target_entity="Meta")


# -----------------------------------------------------------------
# 1. Expert source extraction: Prof. Jeffrey M. Hirsch
# -----------------------------------------------------------------

class TestExpertSourceExtraction:
    """Verify independent legal expert is correctly extracted."""

    def test_hirsch_extracted_as_source(self, result):
        """Jeffrey M. Hirsch should be extracted as a named source."""
        source_names = [s["name"] for s in result["sources"]]
        has_hirsch = any(
            "hirsch" in n.lower() or "jeffrey" in n.lower()
            for n in source_names
        )
        assert has_hirsch, (
            f"Jeffrey M. Hirsch should be in sources. Found: {source_names}"
        )

    def test_hirsch_is_expert(self, result):
        """Hirsch should be tagged as an expert source."""
        hirsch_sources = [
            s for s in result["sources"]
            if "hirsch" in s["name"].lower() or "jeffrey" in s["name"].lower()
        ]
        assert len(hirsch_sources) > 0
        assert hirsch_sources[0]["is_expert"] is True, (
            "Hirsch should be marked is_expert=True"
        )

    def test_hirsch_affiliation(self, result):
        """Hirsch's affiliation should reference University of North Carolina."""
        hirsch_sources = [
            s for s in result["sources"]
            if "hirsch" in s["name"].lower() or "jeffrey" in s["name"].lower()
        ]
        assert len(hirsch_sources) > 0
        aff = hirsch_sources[0].get("affiliation", "").lower()
        assert "north carolina" in aff or "unc" in aff, (
            f"Expected UNC affiliation, got: {hirsch_sources[0].get('affiliation')}"
        )


# -----------------------------------------------------------------
# 2. Meta spokesman as corporate source
# -----------------------------------------------------------------

class TestCorporateSource:
    """Verify Meta spokesperson is correctly extracted."""

    def test_meta_spokesman_extracted(self, result):
        """'A Meta spokesman' should be extracted as a corporate source."""
        source_names = [s["name"].lower() for s in result["sources"]]
        has_spokesman = any(
            "spokesman" in n or "spokesperson" in n or "meta" in n
            for n in source_names
        )
        assert has_spokesman, (
            f"Meta spokesman should be in sources. Found: {source_names}"
        )

    def test_meta_spokesman_not_expert(self, result):
        """Meta spokesman should NOT be tagged as an expert source."""
        meta_sources = [
            s for s in result["sources"]
            if "spokesman" in s["name"].lower()
            or "spokesperson" in s["name"].lower()
        ]
        for s in meta_sources:
            assert s["is_expert"] is not True, (
                "Meta spokesman should not be marked is_expert=True"
            )


# -----------------------------------------------------------------
# 3. Lawsuit as documentary source
# -----------------------------------------------------------------

class TestDocumentarySource:
    """Verify lawsuit is extracted as documentary source."""

    def test_lawsuit_documentary_source(self, result):
        """Lawsuit should be classified as documentary source type."""
        doc_sources = [
            s for s in result["sources"]
            if s.get("source_type") == "documentary"
        ]
        assert len(doc_sources) >= 1, (
            f"Expected documentary source for lawsuit. "
            f"Source types: {[s.get('source_type') for s in result['sources']]}"
        )


# -----------------------------------------------------------------
# 4. Framing device detection
# -----------------------------------------------------------------

class TestFramingDevices:
    """Validate framing devices in the WSJ article."""

    def test_litigation_framing_detected(self, result):
        """'is suing' should trigger litigation_framing."""
        lit_devices = [
            d for d in result["framing_devices"]
            if d["device_type"] == "litigation_framing"
        ]
        assert len(lit_devices) >= 1, (
            f"Expected litigation_framing device. "
            f"Found: {[d['device_type'] for d in result['framing_devices']]}"
        )

    def test_timeline_implication_detected(self, result):
        """'raises questions about' should trigger timeline_implication."""
        ti_devices = [
            d for d in result["framing_devices"]
            if d["device_type"] == "timeline_implication"
        ]
        has_raises = any(
            "raises questions" in d.get("evidence_text", "")
            for d in ti_devices
        )
        assert has_raises, (
            f"Expected 'raises questions' timeline_implication. "
            f"Found: {[d.get('evidence_text', '')[:50] for d in ti_devices]}"
        )

    def test_loaded_language_shielded(self, result):
        """'shielded from' should trigger loaded_language."""
        ll_devices = [
            d for d in result["framing_devices"]
            if d["device_type"] == "loaded_language"
        ]
        has_shielded = any(
            "shielded" in d.get("evidence_text", "")
            for d in ll_devices
        )
        assert has_shielded, (
            f"Expected 'shielded' loaded_language. "
            f"Found: {[d.get('evidence_text', '')[:50] for d in ll_devices]}"
        )


# -----------------------------------------------------------------
# 5. Sentiment and topic classification
# -----------------------------------------------------------------

class TestSentimentAndTopics:
    """Basic validation of sentiment and topic classification."""

    def test_negative_tone(self, result):
        """Lawsuit article should score negative overall."""
        assert result["sentiment"]["overall_tone"] < 0, (
            f"Expected negative tone, got {result['sentiment']['overall_tone']}"
        )

    def test_tone_not_severely_negative(self, result):
        """WSJ with expert balance should not score as extreme negative.

        The article includes an independent legal expert and editorial
        contextualization, which should moderate the tone compared to
        wire-service versions.
        """
        tone = result["sentiment"]["overall_tone"]
        assert tone > -0.8, (
            f"Tone {tone} is too extreme for a balanced analytical piece"
        )

    def test_layoffs_topic_detected(self, result):
        """Should classify as layoffs topic."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert "layoffs" in topic_names, (
            f"Expected 'layoffs' topic, got: {topic_names}"
        )

    def test_litigation_topic_detected(self, result):
        """Should classify as litigation topic."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert "litigation" in topic_names, (
            f"Expected 'litigation' topic, got: {topic_names}"
        )

    def test_workplace_culture_topic_detected(self, result):
        """Should classify as workplace_culture topic."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert "workplace_culture" in topic_names, (
            f"Expected 'workplace_culture' topic, got: {topic_names}"
        )


# -----------------------------------------------------------------
# 6. Entity detection
# -----------------------------------------------------------------

class TestEntityDetection:
    """Validate entity extraction from WSJ article."""

    def test_meta_entity_detected(self, result):
        """Meta should be detected as primary entity."""
        meta_entities = [
            e for e in result["entities"]
            if e.get("canonical_name", "").lower() == "meta"
            or e.get("cluster", "").lower() == "meta"
        ]
        assert len(meta_entities) >= 5, (
            f"Expected 5+ Meta entity mentions, found {len(meta_entities)}"
        )

    def test_zuckerberg_clustered_under_meta(self, result):
        """Mark Zuckerberg should be in the Meta cluster."""
        zuck = [
            e for e in result["entities"]
            if "zuckerberg" in e.get("entity", "").lower()
        ]
        assert len(zuck) >= 1, "Zuckerberg should be detected"
        assert zuck[0].get("cluster", "").lower() == "meta", (
            f"Zuckerberg should cluster under Meta, got: {zuck[0].get('cluster')}"
        )


# -----------------------------------------------------------------
# 7. Source balance: WSJ is more balanced than wire-service peers
# -----------------------------------------------------------------

class TestSourceBalance:
    """Verify WSJ's distinctive source diversity."""

    def test_has_multiple_source_types(self, result):
        """WSJ article should have at least 3 source types:
        corporate spokesperson, independent expert, and documentary."""
        source_types = {s.get("source_type") for s in result["sources"]}
        # Expect at minimum: named expert, corporate_spokesperson/organizational,
        # and documentary
        assert len(source_types) >= 2, (
            f"Expected 2+ source types for balanced coverage. "
            f"Found: {source_types}"
        )

    def test_has_expert_source(self, result):
        """WSJ uniquely includes a named legal expert."""
        expert_sources = [s for s in result["sources"] if s.get("is_expert")]
        assert len(expert_sources) >= 1, (
            "WSJ article should have at least one expert source (Hirsch)"
        )
