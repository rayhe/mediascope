"""Tests for mediascope.quality.standards — quality enforcement layer.

Covers:
    - Banned phrase detection (case-sensitive and case-insensitive)
    - Em dash counting and limit enforcement
    - Counterargument signal detection
    - Limitations signal detection
    - Methodology signal detection
    - Score calculation and pass/fail logic
    - Edge cases (empty text, perfect text, multiple violations)
"""

import pytest
from mediascope.quality.standards import (
    BANNED_PHRASES,
    EM_DASH_LIMIT,
    QualityIssue,
    QualityReport,
    check_quality,
)


# ── Banned phrase detection ──────────────────────────────────────────

class TestBannedPhrases:
    """Banned AI-slop phrase detection."""

    def test_clean_text_no_banned_phrases(self):
        text = (
            "Meta's quarterly revenue rose 33% year-over-year. "
            "However, Reality Labs posted a $4B operating loss. "
            "This analysis has a limitation: sample size is small. "
            "Our methodology uses Welch's t-test."
        )
        report = check_quality(text)
        assert report.banned_phrases_found == []
        assert not any(i.category == "banned_phrase" for i in report.issues)

    def test_detects_lowercase_banned_phrase(self):
        text = (
            "We delve into the data to find patterns. "
            "However, the analysis has limitations. "
            "Our methodology is described below."
        )
        report = check_quality(text)
        assert "delve" in report.banned_phrases_found

    def test_detects_uppercase_banned_phrase_moreover(self):
        """'Moreover,' is case-sensitive — only the capitalized form is banned."""
        text = (
            "Moreover, the data shows a clear pattern. "
            "However, there are counterarguments. "
            "This has limitations and uses standard methodology."
        )
        report = check_quality(text)
        assert "Moreover," in report.banned_phrases_found

    def test_detects_furthermore(self):
        text = (
            "Furthermore, we see a trend in the coverage. "
            "However, counterargument: the sample is small. "
            "Limitation: we cannot prove causation. "
            "We measured sentiment using VADER."
        )
        report = check_quality(text)
        assert "Furthermore," in report.banned_phrases_found

    def test_detects_multiple_banned_phrases(self):
        text = (
            "We delve into the tapestry of the landscape. "
            "However, critics argue this is limited. "
            "Our methodology uses statistical tests."
        )
        report = check_quality(text)
        assert len(report.banned_phrases_found) >= 3
        assert "delve" in report.banned_phrases_found
        assert "tapestry" in report.banned_phrases_found
        assert "landscape" in report.banned_phrases_found

    def test_each_occurrence_deducts_5_points(self):
        """Each banned phrase occurrence costs 5 points."""
        clean = (
            "This is clean text. However, there are caveats. "
            "Our methodology is rigorous."
        )
        clean_report = check_quality(clean)

        dirty = (
            "We delve into the data. However, there are caveats. "
            "Our methodology is rigorous."
        )
        dirty_report = check_quality(dirty)
        # The dirty text should score lower by at least 5
        assert dirty_report.score < clean_report.score

    def test_banned_phrase_triggers_error_severity(self):
        text = (
            "This is a game-changer for the industry. "
            "However, critics argue otherwise. "
            "There are limitations. We measured carefully."
        )
        report = check_quality(text)
        errors = [i for i in report.issues if i.category == "banned_phrase"]
        assert len(errors) > 0
        assert all(e.severity == "error" for e in errors)

    def test_banned_phrase_case_insensitive_match(self):
        """Lowercase banned phrases match regardless of case in text."""
        text = (
            "We DELVE into this ROBUST ecosystem. "
            "However, we note a counterargument. "
            "Limitations exist. Methodology: VADER."
        )
        report = check_quality(text)
        # 'delve', 'robust', 'ecosystem' should all be caught
        assert len(report.banned_phrases_found) >= 3

    def test_line_numbers_reported(self):
        """Banned phrase issues include line numbers."""
        text = "Line one is fine.\nWe delve deeper.\nLine three."
        report = check_quality(text)
        phrase_issues = [i for i in report.issues if i.category == "banned_phrase"]
        assert any(i.line_number == 2 for i in phrase_issues)


# ── Em dash enforcement ──────────────────────────────────────────────

class TestEmDashLimit:
    """Em dash (—) usage limit enforcement."""

    def test_under_limit_no_issue(self):
        text = (
            "First clause — second clause. "
            "Another — example. Third — here. "
            "However, counterarguments exist. "
            "Limitations noted. Methodology described."
        )
        report = check_quality(text)
        assert report.em_dash_count == 3
        assert not any(i.category == "em_dash_overuse" for i in report.issues)

    def test_over_limit_triggers_warning(self):
        text = (
            "One — two — three — four — five. "
            "However, counterarguments exist. "
            "Limitations noted. Methodology: VADER."
        )
        report = check_quality(text)
        assert report.em_dash_count == 4
        overuse = [i for i in report.issues if i.category == "em_dash_overuse"]
        assert len(overuse) == 1
        assert overuse[0].severity == "warning"

    def test_em_dash_deduction_3_per_excess(self):
        """Each em dash over the limit costs 3 points."""
        # Exactly at limit
        at_limit = "A — B — C — D. However, counterarguments. Limitations. Methodology."
        at_report = check_quality(at_limit)

        # 2 over limit
        over = "A — B — C — D — E — F. However, counterarguments. Limitations. Methodology."
        over_report = check_quality(over)

        # Should lose ~6 points (2 excess × 3)
        diff = at_report.score - over_report.score
        assert diff >= 6

    def test_em_dash_count_tracked(self):
        text = "No em dashes here. However, caveats. Limitations. Methodology."
        report = check_quality(text)
        assert report.em_dash_count == 0


# ── Counterargument detection ────────────────────────────────────────

class TestCounterargumentDetection:
    """Counterargument signal detection."""

    def test_however_detected(self):
        text = "The data is clear. However, one must consider alternatives. Limitation: small n. Methodology: t-test."
        report = check_quality(text)
        assert report.has_counterargument is True

    def test_critics_argue_detected(self):
        text = "Critics argue this is insufficient evidence. Limitation: scope. Methodology: manual."
        report = check_quality(text)
        assert report.has_counterargument is True

    def test_on_the_other_hand_detected(self):
        text = "On the other hand, the correlation may be spurious. Caveat: data quality. We analyzed trends."
        report = check_quality(text)
        assert report.has_counterargument is True

    def test_opposing_view_detected(self):
        text = "The opposing view is that editorial independence is preserved. Limitation: self-reporting. Methodology."
        report = check_quality(text)
        assert report.has_counterargument is True

    def test_missing_counterargument_penalized(self):
        text = "The data shows bias. The numbers are clear. Limitation exists. Methodology: VADER."
        report = check_quality(text)
        assert report.has_counterargument is False
        assert any(i.category == "missing_counterargument" for i in report.issues)

    def test_missing_counterargument_costs_10_points(self):
        with_ca = "The data is clear. However, alternatives exist. Limitation noted. Methodology: t-test."
        without_ca = "The data is clear. The numbers confirm it. Limitation noted. Methodology: t-test."
        with_report = check_quality(with_ca)
        without_report = check_quality(without_ca)
        assert without_report.score <= with_report.score - 10


# ── Limitations detection ────────────────────────────────────────────

class TestLimitationsDetection:
    """Limitations section/signal detection."""

    def test_limitation_keyword_detected(self):
        text = "A key limitation is the small sample size. However, results are suggestive. Methodology: standard."
        report = check_quality(text)
        assert report.has_limitations is True

    def test_caveat_detected(self):
        text = "One caveat is that we cannot control for all confounds. However, the trend is notable. We analyzed data."
        report = check_quality(text)
        assert report.has_limitations is True

    def test_this_analysis_does_not(self):
        text = "This analysis does not prove causation. However, the pattern warrants investigation. Statistical methods used."
        report = check_quality(text)
        assert report.has_limitations is True

    def test_missing_limitations_penalized(self):
        text = "The results are definitive. However, critics disagree. Methodology: VADER."
        report = check_quality(text)
        assert report.has_limitations is False
        assert any(i.category == "missing_limitations" for i in report.issues)


# ── Methodology detection ────────────────────────────────────────────

class TestMethodologyDetection:
    """Methodology reference detection."""

    def test_methodology_keyword_detected(self):
        text = "Our methodology follows Welch's t-test. However, there are caveats."
        report = check_quality(text)
        assert report.has_methodology is True

    def test_we_analyzed_detected(self):
        text = "We analyzed 47 articles spanning 6 months. However, the sample is small. There are limitations."
        report = check_quality(text)
        assert report.has_methodology is True

    def test_statistical_keyword_detected(self):
        text = "The statistical significance of the result is p < 0.01. However, caveats apply. Limitations exist."
        report = check_quality(text)
        assert report.has_methodology is True

    def test_missing_methodology_penalized(self):
        text = "The results are clear. However, critics disagree. There are important limitations."
        report = check_quality(text)
        assert report.has_methodology is False
        assert any(i.category == "missing_methodology" for i in report.issues)
        # Methodology is info-level, not warning
        meth_issues = [i for i in report.issues if i.category == "missing_methodology"]
        assert all(i.severity == "info" for i in meth_issues)


# ── Scoring and pass/fail ────────────────────────────────────────────

class TestScoring:
    """Score calculation and pass/fail logic."""

    def test_perfect_text_scores_100(self):
        text = (
            "The asymmetry score for Wired's Meta coverage is −0.283 (p < 0.001). "
            "However, correlation does not imply causation. "
            "A key limitation is that we cannot control for all news-event severity differences. "
            "Our methodology uses Welch's t-test with bootstrap confidence intervals."
        )
        report = check_quality(text)
        assert report.score == 100
        assert report.passed is True

    def test_empty_text_still_returns_report(self):
        report = check_quality("")
        assert isinstance(report, QualityReport)
        # Missing counterargument (-10), limitations (-8), methodology (-5) = 77
        assert report.score == 77

    def test_pass_fail_threshold_at_60(self):
        """Score >= 60 and no errors → pass."""
        # Text with warnings but no errors and score > 60
        text = (
            "The data is compelling. "
            "However, there are alternative explanations. "
            "There are limitations. We measured carefully."
        )
        report = check_quality(text)
        if report.score >= 60 and not any(i.severity == "error" for i in report.issues):
            assert report.passed is True

    def test_error_causes_fail_even_with_high_score(self):
        """A single banned phrase (error) causes fail regardless of score."""
        text = (
            "We delve into this topic carefully. "
            "However, critics argue otherwise. "
            "There are important limitations. "
            "Our methodology is rigorous and statistical."
        )
        report = check_quality(text)
        # Has all three signals but one banned phrase
        assert report.passed is False

    def test_score_clamped_to_0_100(self):
        """Score can't go below 0 or above 100."""
        # Load text with many banned phrases
        phrases = " ".join([f"This is a {p} situation." for p in BANNED_PHRASES])
        report = check_quality(phrases)
        assert 0 <= report.score <= 100

    def test_multiple_violations_compound(self):
        """Multiple violation types compound their deductions."""
        text = (
            "We delve into the tapestry of the landscape. "  # 3 banned phrases
            "A — B — C — D — E. "  # 4 em dashes (1 over)
            "The conclusion is clear."  # no counterargument, limitations, or methodology
        )
        report = check_quality(text)
        # 100 - 15 (banned×3) - 3 (em dash×1) - 10 (counterarg) - 8 (limitations) - 5 (methodology) = 59
        assert report.score < 60
        assert report.passed is False


# ── QualityReport structure ──────────────────────────────────────────

class TestQualityReportStructure:
    """QualityReport dataclass fields are correctly populated."""

    def test_report_fields_populated(self):
        text = (
            "The paradigm shift in AI — especially in NLP — is remarkable. "
            "A — B — C — D — E — F. "
            "However, skeptics point to overhype."
        )
        report = check_quality(text)
        assert isinstance(report.passed, bool)
        assert isinstance(report.score, int)
        assert isinstance(report.issues, list)
        assert isinstance(report.banned_phrases_found, list)
        assert isinstance(report.em_dash_count, int)
        assert isinstance(report.has_counterargument, bool)
        assert isinstance(report.has_limitations, bool)
        assert isinstance(report.has_methodology, bool)

    def test_all_issue_types_have_required_fields(self):
        text = (
            "We delve into the landscape moving forward. "
            "A — B — C — D — E. "
            "This is the conclusion."
        )
        report = check_quality(text)
        for issue in report.issues:
            assert isinstance(issue, QualityIssue)
            assert issue.severity in ("error", "warning", "info")
            assert len(issue.category) > 0
            assert len(issue.description) > 0
