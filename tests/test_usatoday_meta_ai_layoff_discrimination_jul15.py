"""Tests for USA Today Meta AI Layoff Discrimination article analysis (Jul 15, 2026).

Validates toolkit behavior against USA Today's distinct policy-framing coverage:
1. Entity: Meta cluster detection across "Meta Platforms" and "Meta" variants
2. Framing: litigation_framing on "lawsuit lodged against"
3. Framing: precedent_framing on "first of its kind"
4. Framing: anthropomorphization on "blindly trusted it"
5. Absence: no surveillance_enumeration (generic "AI-assisted systems" only)
6. Absence: no humanization (no individual vignettes)
7. Cross-publication structural comparison: cross-case reference gap (Workday)

Article: USA Today "These disabled workers lost their jobs. They say AI targeted
them" (July 15, 2026).

Same-event cluster 15: Reuters (Jul 14), Fox Business (Jul 14), WSJ (Jul 14),
Gizmodo (Jul 15), USA Today (Jul 15). This is the 5th publication on the event.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices


ARTICLE_TEXT = (
    "These disabled workers lost their jobs. They say AI targeted them\n\n"
    "A lawsuit lodged against Meta Platforms accuses the technology giant of "
    "using AI-powered software to target people with disabilities or employees "
    "on medical leave for layoffs.\n\n"
    "Legal experts say the legal action – likely the first of its kind against "
    "a major U.S. company – challenges the growing use of AI to help make "
    "hiring, promotion, performance and termination decisions.\n\n"
    "The lawsuit, in Oakland, California, federal court this month, alleges "
    "Meta relied on AI-assisted systems to score and rank employees on such "
    "factors as productivity when it cut thousands of jobs this year, harming "
    "employees who missed work because of illness or to care for family "
    "members.\n\n"
    "The 26 anonymous plaintiffs from six states were notified in May that "
    "their jobs would be eliminated on July 22. They allege the company "
    "violated federal and state anti-discrimination laws that shield workers "
    "with disabilities, who take medical leave or who are pregnant and they "
    "are seeking a preliminary ruling blocking Meta from carrying out the "
    "layoffs until they can pursue their claims in private arbitration.\n\n"
    "Meta denied the layoffs were conducted by AI.\n\n"
    '"These claims lack merit and are not based on facts," the company said '
    'in a statement. "Workforce management and organizational decisions were '
    'and are made by people, not AI."\n\n'
    "Increasingly artificial intelligence is playing a big role in who gets "
    "hired. Now at issue is how big a role it plays in who gets fired.\n\n"
    "Employers are increasingly using AI to screen resumes, rank job "
    "applicants and handle preliminary interviews. While these automated tools "
    "increase efficiency and reduce headcount, they also raise legal risks.\n\n"
    "A federal judge in San Francisco recently ruled that enterprise software "
    "company Workday must face a class-action lawsuit alleging its AI "
    "screening software discriminates against job applicants.\n\n"
    "Jon Hyman, chair of the employment and labor practice at the Wickens "
    "Herzer Panza law firm, said the Meta lawsuit is a warning to employers "
    "who rely on artificial intelligence to guide critical employment "
    "decisions.\n\n"
    "While AI can be a valuable tool to inform those decisions, if it "
    "penalizes employees for protected absences, disabilities or other "
    "legally protected characteristics, employers will be held accountable, "
    "he said.\n\n"
    "Meta laid off 10% of its global workforce in May – about 8,000 people "
    "– part of a restructuring as the company increases its use of AI.\n\n"
    '"The legal question won\'t be whether an employer used AI but whether it '
    'blindly trusted it," Hyman said. "The companies that fare best won\'t be '
    "those that avoid AI altogether, but those that rigorously audit it, "
    "understand how it reaches its recommendations and ensure that a human "
    "exercises independent judgment before any employment decision is made.\""
)


# ── Entity Detection ─────────────────────────────────────────────────────


class TestUsaTodayEntityDetection:
    """USA Today uses both 'Meta Platforms' (1×) and 'Meta' (5×) — all should
    resolve to the Meta cluster."""

    def test_meta_platforms_full_name_detected(self):
        entities = detect_entities(ARTICLE_TEXT)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        canonical_names = {e.entity for e in meta_entities}
        assert any("Meta" in n for n in canonical_names), (
            f"Expected 'Meta Platforms' or 'Meta' in Meta cluster, "
            f"got {canonical_names}"
        )

    def test_meta_mention_count_at_least_5(self):
        entities = detect_entities(ARTICLE_TEXT)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        assert len(meta_entities) >= 5, (
            f"Expected ≥5 Meta mentions (1× 'Meta Platforms' + 5× 'Meta'), "
            f"got {len(meta_entities)}"
        )

    def test_no_workday_entity_in_current_clusters(self):
        """Workday is referenced but is NOT in any current cluster. This test
        documents the expected gap — Workday should NOT false-positive into
        another cluster (e.g., 'Microsoft' or 'Google')."""
        text = (
            "enterprise software company Workday must face a class-action "
            "lawsuit alleging its AI screening software discriminates"
        )
        entities = detect_entities(text)
        workday_as_other = [
            e for e in entities
            if "Workday" in e.entity and e.cluster != "Workday"
        ]
        assert len(workday_as_other) == 0, (
            f"Workday incorrectly matched to cluster: "
            f"{[(e.entity, e.cluster) for e in workday_as_other]}"
        )


# ── Framing Device Detection ─────────────────────────────────────────────


class TestUsaTodayFramingDevices:
    """USA Today triggers exactly 3 framing devices on this article:
    litigation_framing, precedent_framing, and anthropomorphization.

    Key absences vs. same-event cluster:
    - No surveillance_enumeration (generic 'AI-assisted systems', no tool names)
    - No humanization (no individual vignettes or pregnancy details)
    - No scale_magnitude (documented gap: percentage + headcount pattern)
    - No kicker_framing on full article (expert kicker not detected)
    - No escalation_amplification ('growing use' + enumeration not detected)
    """

    @classmethod
    @pytest.fixture(scope="class")
    def devices(cls):
        return detect_framing_devices(ARTICLE_TEXT)

    @classmethod
    @pytest.fixture(scope="class")
    def device_types(cls, devices):
        return {d.device_type for d in devices}

    def test_total_device_count(self, devices):
        assert len(devices) == 3, (
            f"Expected exactly 3 framing devices, got {len(devices)}: "
            f"{[d.device_type for d in devices]}"
        )

    def test_litigation_framing_present(self, device_types):
        assert "litigation_framing" in device_types, (
            "litigation_framing must fire for 'lawsuit lodged against Meta'"
        )

    def test_precedent_framing_present(self, device_types):
        assert "precedent_framing" in device_types, (
            "precedent_framing must fire for 'first of its kind'"
        )

    def test_anthropomorphization_present(self, device_types):
        assert "anthropomorphization" in device_types, (
            "anthropomorphization must fire for 'blindly trusted it'"
        )

    def test_no_surveillance_enumeration(self, device_types):
        """USA Today omits all named AI tools (Metamate, second brain,
        keystroke monitoring). No surveillance_enumeration should fire."""
        assert "surveillance_enumeration" not in device_types, (
            "surveillance_enumeration should NOT fire — USA Today uses "
            "generic 'AI-assisted systems', not specific tool names"
        )

    def test_no_humanization(self, device_types):
        """USA Today has no pregnancy vignette — purely systemic framing.
        Humanization should NOT fire (contrast with WSJ/Gizmodo)."""
        assert "humanization" not in device_types, (
            "humanization should NOT fire — no individual stories or "
            "pregnancy vignettes in USA Today's coverage"
        )

    def test_no_scale_magnitude(self, device_types):
        """USA Today includes '10% of its global workforce... about 8,000'
        but the toolkit's scale_magnitude device does not fire — documented
        gap: no percentage + headcount combined pattern."""
        assert "scale_magnitude" not in device_types, (
            "scale_magnitude does not currently fire on percentage + headcount "
            "pattern (documented gap for future improvement)"
        )

    def test_no_escalation_amplification(self, device_types):
        """'growing use' + enumeration and 'increasingly' do not trigger
        escalation_amplification on the full article."""
        assert "escalation_amplification" not in device_types, (
            "escalation_amplification does not fire on this article — "
            "'growing use' + enumeration not matched by current patterns"
        )


# ── Documented Gaps ───────────────────────────────────────────────────────


class TestDocumentedGaps:
    """Tests documenting known toolkit gaps discovered via this article.
    Each test describes what *should* ideally fire but currently doesn't."""

    def test_scale_magnitude_gap_percentage_plus_headcount(self):
        """The toolkit has no pattern for 'X% of ... workforce ... about N
        people'. This is a documentation test — it verifies the gap exists
        so a future fix can flip this assertion."""
        text = (
            "Meta laid off 10% of its global workforce in May – about "
            "8,000 people"
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        # scale_magnitude SHOULD fire here but doesn't (gap)
        assert "scale_magnitude" not in types, (
            "If this fails, the scale_magnitude gap has been fixed! "
            "Update the test to assert presence."
        )

    def test_escalation_growing_use_gap(self):
        """'growing use of AI to help make hiring, promotion, performance
        and termination decisions' — escalation_amplification does not fire.
        Documented gap: 'growing' + enumeration pattern not matched."""
        text = (
            "challenges the growing use of AI to help make hiring, "
            "promotion, performance and termination decisions"
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "escalation_amplification" not in types, (
            "If this fails, the escalation gap has been fixed! "
            "Update the test to assert presence."
        )

    def test_escalation_increasingly_gap(self):
        """'Employers are increasingly using AI...' — does not trigger
        escalation_amplification. Documented gap."""
        text = (
            "Employers are increasingly using AI to screen resumes, "
            "rank job applicants and handle preliminary interviews"
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "escalation_amplification" not in types, (
            "If this fails, the escalation gap has been fixed! "
            "Update the test to assert presence."
        )


# ── Cross-Case Reference (Workday) ───────────────────────────────────────


class TestCrossCaseReference:
    """USA Today uniquely broadens from Meta-specific to industry-wide by
    citing the separate Workday AI discrimination lawsuit. This is a structural
    editorial choice not covered by any current framing device. These tests
    document the gap."""

    def test_cross_case_sentence_exists(self):
        """Verify the cross-case reference text is present in the article."""
        assert "Workday must face a class-action lawsuit" in ARTICLE_TEXT

    def test_workday_not_attributed_to_meta_cluster(self):
        """Workday is a separate company — must not land in Meta cluster."""
        text = (
            "enterprise software company Workday must face a class-action "
            "lawsuit"
        )
        entities = detect_entities(text)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        assert len(meta_entities) == 0, (
            "Workday sentence should produce 0 Meta entities"
        )

    def test_no_cross_case_citation_device(self):
        """No framing device exists for cross-case citation. This documents
        the gap — the Workday reference is a significant editorial framing
        choice that broadens the narrative from Meta-specific to industry-wide."""
        workday_text = (
            "A federal judge in San Francisco recently ruled that enterprise "
            "software company Workday must face a class-action lawsuit "
            "alleging its AI screening software discriminates against job "
            "applicants."
        )
        devices = detect_framing_devices(workday_text)
        types = {d.device_type for d in devices}
        # No cross_case_citation device exists yet
        assert "cross_case_citation" not in types, (
            "If this fails, a cross_case_citation device has been added! "
            "Update the test to assert presence."
        )


# ── Expert Source Architecture ────────────────────────────────────────────


class TestExpertSourceArchitecture:
    """USA Today is the only outlet in the 5-way cluster (alongside WSJ) to
    include an independent legal expert. Jon Hyman is from Wickens Herzer
    Panza, not a plaintiff attorney. These tests verify entity detection
    doesn't misclassify the expert."""

    def test_hyman_not_misclassified_as_meta(self):
        text = (
            "Jon Hyman, chair of the employment and labor practice at the "
            "Wickens Herzer Panza law firm, said the Meta lawsuit is a warning"
        )
        entities = detect_entities(text)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        meta_names = {e.entity for e in meta_entities}
        assert "Jon Hyman" not in meta_names, (
            "Jon Hyman must not be classified as Meta entity"
        )
        assert "Wickens Herzer Panza" not in meta_names, (
            "Wickens Herzer Panza must not be classified as Meta entity"
        )

    def test_hyman_quote_contains_balanced_language(self):
        """Hyman's closing quote contains both cautionary and constructive
        language — verify the quote is present for sentiment testing."""
        assert "rigorously audit it" in ARTICLE_TEXT
        assert "valuable tool" in ARTICLE_TEXT
        assert "independent judgment" in ARTICLE_TEXT


# ── Same-Event Structural Contrasts ──────────────────────────────────────


class TestSameEventContrasts:
    """Structural assertions documenting what makes USA Today's coverage
    distinct from the other 4 outlets in cluster 15."""

    def test_no_metamate_in_article(self):
        """USA Today omits all internal AI tool names."""
        assert "Metamate" not in ARTICLE_TEXT
        assert "second brain" not in ARTICLE_TEXT

    def test_no_keystroke_monitoring(self):
        """USA Today omits surveillance-enumeration details."""
        assert "keystroke" not in ARTICLE_TEXT
        assert "screen monitoring" not in ARTICLE_TEXT
        assert "browser history" not in ARTICLE_TEXT

    def test_no_pregnancy_detail(self):
        """USA Today omits the pregnancy vignettes used by WSJ and Gizmodo."""
        assert "giving birth" not in ARTICLE_TEXT
        assert "maternity" not in ARTICLE_TEXT

    def test_workday_reference_unique_to_usa_today(self):
        """USA Today is the only outlet in the cluster to reference a
        separate AI discrimination case (Workday)."""
        assert "Workday" in ARTICLE_TEXT
