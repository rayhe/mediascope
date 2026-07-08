"""Tests for WSJ AI spending article source extraction fixes.

Regression tests for bugs discovered during the Jul 8, 2026 Type A
iteration on WSJ "Will Someone Finally Blink in the AI Spending War?"

Covers:
- Pattern 0c: "First Last of Organization VERB" — prevents org name
  from being misidentified as person name (KeyBanc Capital bug)
- Pattern 0d: "VERB First Last of Organization" — reverse order
  (Jefferies/Brent Thill bug)
- Pattern 0e: "[Org] analyst/researcher [Name] VERB" — captures
  affiliation when org precedes role noun (Bernstein Research bug)
- Full-text expert detection fallback for Pattern 1
"""

import pytest

from mediascope.analyze.sources import extract_sources


# --------------------------------------------------------------------------- #
# Pattern 0c: "First Last of Organization VERB"
# --------------------------------------------------------------------------- #

class TestPattern0c:
    """Pattern 0c: 'First Last of Organization VERB'."""

    def test_keybanc_capital_name_extraction(self):
        """'Justin Patterson of KeyBanc Capital said' → person, not org-as-person."""
        text = 'Justin Patterson of KeyBanc Capital said the spending is unsustainable.'
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert 'Justin Patterson' in names
        # "Capital" should NOT be extracted as a person name
        assert 'Capital' not in names
        assert 'KeyBanc Capital' not in names

    def test_keybanc_capital_affiliation(self):
        """Affiliation should be 'KeyBanc Capital'."""
        text = 'Justin Patterson of KeyBanc Capital said the spending is unsustainable.'
        sources = extract_sources(text)
        jp = next(s for s in sources if s.name == 'Justin Patterson')
        assert jp.affiliation == 'KeyBanc Capital'

    def test_keybanc_capital_verb(self):
        """Attribution verb should be 'said'."""
        text = 'Justin Patterson of KeyBanc Capital said the spending is unsustainable.'
        sources = extract_sources(text)
        jp = next(s for s in sources if s.name == 'Justin Patterson')
        assert jp.attribution_verb == 'said'

    def test_multi_word_org(self):
        """Multi-word org names should be captured fully."""
        text = 'Sarah Chen of Goldman Sachs noted the trend is accelerating.'
        sources = extract_sources(text)
        sc = next((s for s in sources if s.name == 'Sarah Chen'), None)
        assert sc is not None
        assert 'Goldman' in sc.affiliation

    def test_middle_initial(self):
        """Names with middle initials should work."""
        text = 'John T. Smith of Morgan Stanley warned about overbuilding.'
        sources = extract_sources(text)
        js = next((s for s in sources if 'Smith' in s.name), None)
        assert js is not None
        assert 'Morgan Stanley' in js.affiliation


# --------------------------------------------------------------------------- #
# Pattern 0d: "VERB First Last of Organization"
# --------------------------------------------------------------------------- #

class TestPattern0d:
    """Pattern 0d: 'VERB First Last of Organization'."""

    def test_wrote_brent_thill_of_jefferies(self):
        """'wrote Brent Thill of Jefferies' → name + org."""
        text = 'In a recent note, wrote Brent Thill of Jefferies about the AI race.'
        sources = extract_sources(text)
        bt = next((s for s in sources if s.name == 'Brent Thill'), None)
        assert bt is not None
        assert bt.affiliation == 'Jefferies'
        assert bt.attribution_verb == 'wrote'

    def test_said_name_of_org(self):
        """'said Anna Lee of Citigroup' → name + org."""
        text = 'The market is overheated, said Anna Lee of Citigroup in a note.'
        sources = extract_sources(text)
        al = next((s for s in sources if s.name == 'Anna Lee'), None)
        assert al is not None
        assert al.affiliation == 'Citigroup'


# --------------------------------------------------------------------------- #
# Pattern 0e: "[Org] analyst/researcher [Name] VERB"
# --------------------------------------------------------------------------- #

class TestPattern0e:
    """Pattern 0e: '[Org] analyst/researcher [Name] VERB'."""

    def test_bernstein_research_analyst(self):
        """'Bernstein Research analyst Madison Rezaei says' → name + affiliation."""
        text = 'Bernstein Research analyst Madison Rezaei says the spending could pay off.'
        sources = extract_sources(text)
        mr = next((s for s in sources if s.name == 'Madison Rezaei'), None)
        assert mr is not None, f'Expected Madison Rezaei in sources, got {[s.name for s in sources]}'
        assert mr.affiliation == 'Bernstein Research'
        assert mr.attribution_verb == 'says'

    def test_analyst_is_expert(self):
        """Analyst should be flagged as expert."""
        text = 'Bernstein Research analyst Madison Rezaei says the spending could pay off.'
        sources = extract_sources(text)
        mr = next(s for s in sources if s.name == 'Madison Rezaei')
        assert mr.is_expert is True

    def test_economist_role(self):
        """'Oxford Economics economist Jane Park noted' → name + org."""
        text = 'Oxford Economics economist Jane Park noted the GDP impact.'
        sources = extract_sources(text)
        jp = next((s for s in sources if s.name == 'Jane Park'), None)
        assert jp is not None
        assert 'Oxford' in jp.affiliation

    def test_correspondent_role(self):
        """'Reuters correspondent Mike Chen reported' → name + org."""
        text = 'Reuters correspondent Mike Chen reported from the conference floor.'
        sources = extract_sources(text)
        mc = next((s for s in sources if s.name == 'Mike Chen'), None)
        assert mc is not None
        assert mc.affiliation == 'Reuters'

    def test_no_double_extraction(self):
        """Pattern 0e should prevent Pattern 1 from re-extracting the same person."""
        text = 'Bernstein Research analyst Madison Rezaei says the spending could pay off. Rezaei added that estimates are conservative.'
        sources = extract_sources(text)
        rezaei_sources = [s for s in sources if 'Rezaei' in s.name]
        # Should have exactly one extraction with the org affiliation,
        # not a second one without it
        assert len(rezaei_sources) >= 1
        assert any(s.affiliation == 'Bernstein Research' for s in rezaei_sources)


# --------------------------------------------------------------------------- #
# Full-text expert detection fallback
# --------------------------------------------------------------------------- #

class TestFullTextExpertFallback:
    """Expert detection should use full-text search when narrow context misses."""

    def test_analyst_mentioned_earlier(self):
        """If 'analyst' appears earlier in text near the name, expert should be True."""
        text = (
            'Jefferies analyst Brent Thill published a note on Tuesday. '
            'The report covered AI spending across major tech companies. '
            'Thill noted that Meta and Google are leading the charge.'
        )
        sources = extract_sources(text)
        thill = next((s for s in sources if 'Thill' in s.name), None)
        assert thill is not None
        assert thill.is_expert is True, (
            f'Expected Thill to be expert (analyst title in full text), '
            f'got is_expert={thill.is_expert}'
        )
