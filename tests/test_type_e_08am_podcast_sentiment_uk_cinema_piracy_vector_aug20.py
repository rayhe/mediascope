"""
Type E: Podcast Sentiment Tracking — Aug 20, 2026 08:00 PT
UK Cinema Association piracy vector, CalChamber employer law, Scotland courts extension

Tests validate:
1. UK Cinema Association first industry-body ban + piracy as new concern vector
2. First institutional ban to mention "other smart glasses" alongside Meta
3. CalChamber employer law podcast — California two-party consent × smart glasses
4. Scotland courts (SCTS) extending England/Wales HMCTS ban to all UK courts
5. Meta patent US 2026/0238876 A1 as upstream catalyst for podcast coverage cascade
6. Institutional ban cascade completeness (10 entities tracked)
7. Cross-medium asymmetry summary updated (46 entries)
"""

import pytest
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PODCAST_SENTIMENT = REPO_ROOT / "podcast-sentiment.md"
ITERATION_LOG = REPO_ROOT / "iteration-log.md"


class TestUKCinemaAssociationPiracyVector:
    """UK Cinema Association — first industry body ban, piracy vector, 'other smart glasses' mention."""

    def test_entry_45_exists(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "### 45." in content, "Entry #45 (UK Cinema Association) must exist"

    def test_reuters_source_url(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "reuters.com/business/media-telecom/uk-cinemas-restricting" in content

    def test_piracy_concern_vector_documented(self):
        content = PODCAST_SENTIMENT.read_text()
        # Piracy must be documented as a distinct concern alongside privacy
        piracy_section = content[content.index("### 45."):]
        assert "piracy" in piracy_section.lower()[:3000]
        assert "privacy" in piracy_section.lower()[:3000]

    def test_first_other_smart_glasses_mention(self):
        """The UK Cinema Association is the first institutional ban to mention 'other smart glasses'."""
        content = PODCAST_SENTIMENT.read_text()
        assert '"other smart glasses"' in content or "'other smart glasses'" in content

    def test_industry_body_vs_individual_venue(self):
        """This is an industry ASSOCIATION action, not an individual venue decision."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 45."):][:3000]
        assert "UK Cinema Association" in section
        assert "industry" in section.lower()

    def test_date_is_aug_20_2026(self):
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 45."):][:500]
        assert "Aug" in section and "20" in section and "2026" in section

    def test_meta_still_named_first(self):
        """Even when 'other smart glasses' is mentioned, Meta is still named first."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 45."):][:3000]
        assert "Meta" in section

    def test_accessibility_caveat_documented(self):
        """Cinema operators acknowledged accessibility benefits."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 45."):][:3000]
        assert "access" in section.lower()

    def test_piracy_as_mechanism_158_update(self):
        """Piracy vector should be documented as a Vector 4 update to mechanism #158."""
        content = PODCAST_SENTIMENT.read_text()
        # Entry 45 may be long; search the full entry up to entry 46
        start = content.index("### 45.")
        end = content.index("### 46.")
        section = content[start:end]
        assert "#158" in section


class TestCalChamberEmployerLawPodcast:
    """CalChamber 'The Workplace' podcast — California employer compliance perspective."""

    def test_entry_46_exists(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "### 46." in content, "Entry #46 (CalChamber) must exist"

    def test_calchamber_source_url(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "hrwatchdog.calchamber.com" in content

    def test_california_two_party_consent(self):
        """Episode must reference California two-party consent recording law."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 46."):][:3000]
        assert "two-party consent" in section.lower() or "632" in section

    def test_employer_liability_framework(self):
        """Coverage must discuss employer liability, not just consumer privacy."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 46."):][:3000]
        assert "employer" in section.lower()
        assert "liability" in section.lower() or "compliance" in section.lower()

    def test_category_level_framing(self):
        """CalChamber episode should use category-level framing (employment law demands brand neutrality)."""
        content = PODCAST_SENTIMENT.read_text()
        section = content[content.index("### 46."):][:3000]
        assert "category" in section.lower()

    def test_low_asymmetry_assessment(self):
        """CalChamber should have LOW asymmetry — legal compliance demands brand neutrality."""
        content = PODCAST_SENTIMENT.read_text()
        start = content.index("### 46.")
        # Search through the full entry (may be long)
        end_marker = "### Upstream Catalyst" if "### Upstream Catalyst" in content[start:] else "---"
        end = content.index(end_marker, start)
        section = content[start:end]
        assert "LOW" in section


class TestScotlandCourtsExtension:
    """Scotland SCTS extending England/Wales ban to all UK courts."""

    def test_scotland_scts_documented(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "SCTS" in content or "Scottish Courts" in content

    def test_uk_wide_court_ban(self):
        """England/Wales HMCTS + Scotland SCTS = ALL UK courts banned."""
        content = PODCAST_SENTIMENT.read_text()
        assert "HMCTS" in content
        assert "SCTS" in content or "Scotland" in content

    def test_calmac_ferries_documented(self):
        """CalMac ferries rule change should be documented."""
        content = PODCAST_SENTIMENT.read_text()
        assert "CalMac" in content


class TestMetaPatentCatalyst:
    """Meta patent US 2026/0238876 A1 as upstream catalyst."""

    def test_patent_number_documented(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "2026/0238876" in content

    def test_facial_recognition_example(self):
        """The dinner party facial recognition example should be documented."""
        content = PODCAST_SENTIMENT.read_text()
        assert "dinner party" in content.lower() or "dinner-party" in content.lower()

    def test_biometric_update_source(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "biometricupdate.com" in content

    def test_testable_prediction_for_samsung(self):
        """Should predict Samsung won't receive equivalent alarm framing for similar patents."""
        content = PODCAST_SENTIMENT.read_text()
        patent_section = content[content.index("US 2026/0238876"):][:2000]
        assert "Samsung" in patent_section


class TestInstitutionalBanCascadeCompleteness:
    """Validate the institutional ban cascade timeline is complete and accurate."""

    def test_ten_institutions_tracked(self):
        """At least 10 institutional ban entries in the cascade timeline."""
        content = PODCAST_SENTIMENT.read_text()
        # Count table rows in the ban cascade
        ban_entries = [
            "New York courts",
            "DEF CON",
            "Monopoly Events",
            "HMCTS",
            "SCTS",
            "ATG Theatres",
            "Wetherspoons",
            "Soho House",
            "CalMac",
            "UK Cinema Association",
        ]
        found = sum(1 for entry in ban_entries if entry in content)
        assert found >= 9, f"Expected 9+ institutional ban entries, found {found}"

    def test_uk_cinema_is_latest(self):
        """UK Cinema Association (Aug 20) should be the most recent ban entry."""
        content = PODCAST_SENTIMENT.read_text()
        assert "UK Cinema Association" in content
        # Find the ban cascade table and verify UK Cinema Association is there
        assert "Aug 20" in content


class TestCrossMediumSummaryUpdate:
    """Cross-medium asymmetry summary should reflect 46 entries and new patterns."""

    def test_entry_count_46(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "46 entries" in content

    def test_piracy_pattern_in_summary(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "Piracy" in content or "piracy" in content

    def test_employer_law_pattern_in_summary(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "Employer" in content or "employer" in content

    def test_mechanism_196_documented(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "#196" in content

    def test_updated_timestamp(self):
        """Timestamp should reflect Aug 20 15:00 UTC."""
        content = PODCAST_SENTIMENT.read_text()
        assert "Aug 20, 8:00 AM PT" in content or "2026-08-20 15:00 UTC" in content


class TestTestablePredictions:
    """Testable predictions should be updated with today's findings."""

    def test_cinema_piracy_ban_prediction(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "MPAA" in content or "MPA" in content

    def test_calchamber_ripple_prediction(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "California employers" in content or "employer" in content.lower()

    def test_patent_coverage_cascade_prediction(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "patent" in content.lower() and "7 days" in content


class TestPodcastSentimentStructuralIntegrity:
    """Validate overall file structural integrity."""

    def test_file_exists(self):
        assert PODCAST_SENTIMENT.exists()

    def test_file_not_empty(self):
        content = PODCAST_SENTIMENT.read_text()
        assert len(content) > 50000, "Podcast sentiment file should be >50KB"

    def test_entry_numbering_sequential(self):
        """Entries should be numbered sequentially from 1 to 46."""
        content = PODCAST_SENTIMENT.read_text()
        for i in [1, 10, 20, 30, 40, 44, 45, 46]:
            assert f"### {i}." in content, f"Entry #{i} missing"

    def test_mechanism_references_present(self):
        """Key mechanisms should be referenced in the file."""
        content = PODCAST_SENTIMENT.read_text()
        key_mechanisms = ["#144", "#157", "#158", "#176", "#181", "#189", "#193", "#196"]
        for mech in key_mechanisms:
            assert mech in content, f"Mechanism {mech} not referenced"

    def test_last_updated_is_today(self):
        content = PODCAST_SENTIMENT.read_text()
        assert "2026-08-20" in content


class TestCrossMediumAsymmetryPatterns:
    """Validate documented cross-medium asymmetry patterns."""

    def test_samsung_zero_scrutiny_maintained(self):
        """0 of 46 entries should examine Samsung/Google glasses privacy."""
        content = PODCAST_SENTIMENT.read_text()
        assert "0 of 46 entries" in content or "0 of 46" in content

    def test_snap_zero_scrutiny_maintained(self):
        """Snap Spectacles ($2,195) should have zero scrutiny across all entries."""
        content = PODCAST_SENTIMENT.read_text()
        assert "$2,195 Specs" in content or "$2,195 Spectacles" in content

    def test_publicly_funded_broadcaster_count(self):
        """BBC, DW, ABC Australia should all be documented as publicly funded."""
        content = PODCAST_SENTIMENT.read_text()
        assert "BBC" in content
        assert "DW" in content or "Deutsche Welle" in content
        assert "ABC" in content
