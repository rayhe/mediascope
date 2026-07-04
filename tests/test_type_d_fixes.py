"""Tests for Type D fixes: compound publication source extraction
and bare confession framing patterns.

Added 2026-07-04 as part of Type D toolkit quality iteration.
"""

import pytest
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.framing import detect_framing_devices


class TestCompoundPublicationSources:
    """Compound publication names (e.g. 'Business Insider', 'Daily Beast')
    should be extractable as organizational sources via Pattern 6, even
    though they are in _NAME_STOP_NAMES to prevent person-name false
    positives from Patterns 1-3.
    """

    def test_according_to_business_insider(self):
        text = "According to Business Insider, the project began in 2024."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Business Insider" in names

    def test_according_to_daily_beast(self):
        text = "According to the Daily Beast, sources confirmed the story."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Daily Beast" in names or "The Daily Beast" in names

    def test_business_insider_source_type(self):
        text = "According to Business Insider, the initiative was scrapped."
        sources = extract_sources(text)
        bi = [s for s in sources if s.name == "Business Insider"]
        assert len(bi) == 1
        assert bi[0].source_type == "organizational"

    def test_daily_beast_source_type(self):
        text = "According to the Daily Beast, internal documents showed delays."
        sources = extract_sources(text)
        db = [s for s in sources if "Daily Beast" in s.name]
        assert len(db) == 1
        assert db[0].source_type == "organizational"

    def test_business_insider_verb_form(self):
        """'Business Insider reported' should match as org source."""
        text = "Business Insider reported that Meta was restructuring."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Business Insider" in names

    def test_daily_mail_according_to(self):
        text = "According to the Daily Mail, plans were underway."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Daily Mail" in names

    def test_person_name_stops_still_work(self):
        """Compound pub names should NOT match as person names (Pattern 1)."""
        text = "Business Insider said the deal was done."
        sources = extract_sources(text)
        # Should be organizational, not a named person source
        bi = [s for s in sources if s.name == "Business Insider"]
        for s in bi:
            assert s.source_type == "organizational", \
                "Business Insider should be organizational, not a person name"

    def test_beast_fragment_still_blocked(self):
        """Single-word 'Beast' should not appear as standalone source."""
        text = "The Daily Beast reported on the internal documents."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Beast" not in names

    def test_insider_fragment_still_blocked(self):
        """Single-word 'Insider' should not appear as standalone source."""
        text = "Business Insider reported on the breach."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Insider" not in names


class TestBareConfessionFraming:
    """The 'bare' confession pattern catches 'a rare admission' etc.
    without the 'in' prefix that the original pattern required.
    """

    def test_a_rare_admission(self):
        text = "A rare admission from Zuckerberg came during the town hall."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_the_rare_admission(self):
        text = "The rare admission that AI agents had not progressed surprised employees."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_possessive_rare_admission(self):
        text = "His rare admission came during an all-hands meeting."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_named_possessive_rare_acknowledgment(self):
        text = "Zuckerberg's rare acknowledgment that bets haven't come to fruition."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_in_prefix_still_works(self):
        """Original 'in a rare admission' pattern should still match."""
        text = "In a rare admission, he told employees the layoffs were haphazard."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_stunning_concession(self):
        text = "A stunning concession from the CEO signaled a shift in strategy."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) >= 1

    def test_no_false_positive_normal_admission(self):
        """Plain 'admission' without a qualifier should NOT match."""
        text = "The admission fee for the conference was fifty dollars."
        devices = detect_framing_devices(text)
        confession = [d for d in devices if d.device_type == "confession_framing"]
        assert len(confession) == 0
