"""Tests for law enforcement outsourced intensity framing patterns.

Added in the Guardian Meta AI CSAM 'junk' tips analysis (2026-07-02).
Validates 4 new outsourced_intensity regex patterns that detect when
journalists use law enforcement officers, investigators, and policy
advocates as vehicles for emotional criticism.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


def _types(text: str) -> list[str]:
    """Return sorted device types detected in text."""
    return sorted(d.device_type for d in detect_framing_devices(text))


def _has_outsourced(text: str) -> bool:
    """Return True if outsourced_intensity is among detected devices."""
    return "outsourced_intensity" in _types(text)


class TestLawEnforcementOutsourcedIntensity:
    """Law enforcement credential + loaded quote patterns."""

    def test_officer_junk_quote(self):
        """ICAC officer calling reports 'junk' should trigger outsourced_intensity."""
        text = (
            'Officers with the task force specifically cited Meta\'s automated '
            'systems. "We get a lot of tips from Meta that are just kind of '
            'junk," an ICAC officer testified during the trial.'
        )
        assert _has_outsourced(text)

    def test_agent_drowning_quote(self):
        """Agent quote about 'drowning in tips' should trigger."""
        text = (
            '"It is killing morale. We are drowning in tips, and we want to '
            'get out there and do this work," an ICAC officer reportedly said.'
        )
        assert _has_outsourced(text)

    def test_investigator_overwhelming_quote(self):
        """Investigator describing overwhelming reports should trigger."""
        text = (
            'Another investigator, speaking anonymously, told The Guardian '
            'the department\'s reports doubled. "It\'s pretty overwhelming '
            'because we\'re getting so many reports," they said.'
        )
        assert _has_outsourced(text)

    def test_special_agent_flood_quote(self):
        """Special agent describing a 'flood' should trigger."""
        text = (
            'A special agent with the task force said the situation was '
            'untenable. "There\'s no way that we can keep up with the flood '
            'that\'s coming in," they warned.'
        )
        assert _has_outsourced(text)

    def test_neutral_officer_quote_no_trigger(self):
        """Officer quote without loaded language should NOT trigger."""
        text = (
            '"We review every report that comes in and assess its merit," '
            'the officer said. "Our team processes them according to protocol."'
        )
        assert not _has_outsourced(text)


class TestTestimonyOutsourcedIntensity:
    """Testimony-outsourced patterns (testified / told the court)."""

    def test_testified_with_loaded_quote(self):
        """Quote with 'testified' + loaded language should trigger."""
        text = (
            '"The reports are just junk — unusable noise that buries real '
            'cases," Zwiebel testified during the state\'s trial.'
        )
        assert _has_outsourced(text)

    def test_told_committee_with_loaded_quote(self):
        """Quote with 'told the committee' + loaded language should trigger."""
        text = (
            '"We are drowning in false positives and it is unsustainable," '
            'the director told the committee.'
        )
        assert _has_outsourced(text)

    def test_neutral_testimony_no_trigger(self):
        """Neutral testimony without loaded language should NOT trigger."""
        text = (
            '"We received approximately 4,000 reports last quarter," '
            'Smith testified during the hearing.'
        )
        assert not _has_outsourced(text)


class TestAdvocacyOutsourcedIntensity:
    """Policy advocate / watchdog outsourced critique patterns."""

    def test_policy_advocate_laid_off_critique(self):
        """Policy advocate quoting about layoffs should trigger."""
        text = (
            'JB Branch, a policy advocate at Public Citizen, said the '
            'increased reliance on AI has made things worse. "A lot of these '
            'tech companies have laid off content moderators and replaced '
            'them with AI security features," Branch told Decrypt.'
        )
        assert _has_outsourced(text)

    def test_watchdog_false_positive_critique(self):
        """Watchdog group quoting about false positives should trigger."""
        text = (
            'A consumer advocate at the watchdog group warned of systemic '
            'problems. "There is an overabundance of false positives being '
            'selected out of an overabundance of caution," she said.'
        )
        assert _has_outsourced(text)

    def test_neutral_advocate_no_trigger(self):
        """Advocate quote without loaded language should NOT trigger."""
        text = (
            'A policy advocate at Public Citizen noted that the legislation '
            '"establishes a framework for reporting requirements that '
            'companies must follow," she said.'
        )
        assert not _has_outsourced(text)


class TestEntityDetectionCSAMArticle:
    """Entity detection for CSAM/child safety article entities."""

    def test_icac_detected(self):
        """ICAC should be detected as US Government entity."""
        from mediascope.analyze.entities import detect_entities

        text = "Officers with the ICAC taskforce in New Mexico testified."
        entities = detect_entities(text)
        icac_entities = [e for e in entities if "ICAC" in e.entity]
        assert len(icac_entities) >= 1
        assert icac_entities[0].cluster == "US Government"

    def test_public_citizen_detected(self):
        """Public Citizen should be detected as Privacy/Civil Liberties Org."""
        from mediascope.analyze.entities import detect_entities

        text = "JB Branch, a policy advocate at Public Citizen, warned."
        entities = detect_entities(text)
        pc_entities = [e for e in entities if "Public Citizen" in e.entity]
        assert len(pc_entities) >= 1
        assert pc_entities[0].cluster == "Privacy/Civil Liberties Orgs"

    def test_report_act_detected(self):
        """Report Act should be detected as Child Safety Legislation."""
        from mediascope.analyze.entities import detect_entities

        text = "The Report Act was signed into law in May 2024."
        entities = detect_entities(text)
        act_entities = [e for e in entities if "Report Act" in e.entity]
        assert len(act_entities) >= 1
        assert act_entities[0].cluster == "Child Safety Legislation"

    def test_cybertipline_detected(self):
        """CyberTipline should be detected as Research Centers entity."""
        from mediascope.analyze.entities import detect_entities

        text = "Meta remains the largest source of reports to NCMEC's CyberTipline."
        entities = detect_entities(text)
        ct_entities = [e for e in entities if "CyberTip" in e.entity]
        assert len(ct_entities) >= 1
        assert ct_entities[0].cluster == "Research Centers"
