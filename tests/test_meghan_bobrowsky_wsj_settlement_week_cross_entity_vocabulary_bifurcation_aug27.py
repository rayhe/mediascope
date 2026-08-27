"""
Test: Meghan Bobrowsky (WSJ) Settlement-Week Cross-Entity Vocabulary Bifurcation

Mechanism #337: WSJ Same-Publication Settlement-Week Vocabulary Bifurcation

FINDING:
On Aug 26, 2026, Meghan Bobrowsky (WSJ's dedicated Meta beat reporter) published
the Meta $18B child safety settlement article with full accountability vocabulary:
"profit-driven addictive features" (Florida AG quote amplified), "knowingly making
its platforms addictive," self-referencing WSJ's own "Facebook Files" investigation,
and trial/litigation framing.

In the SAME 48-hour window (Aug 25-26), WSJ published:
- "Anthropic Expected to Tell Investors It Sees Over $30 Trillion in Potential Revenue"
  (Corrie Driebusch) — aspirational IPO framing, "potential revenue opportunities"
- "Number of the Week: $30 Trillion+" (WSJ editors) — amplifying the aspirational TAM
- Anthropic-Ode PE consulting JV ($1.5B) — positive enterprise framing
- OpenAI data retention pledge — competitive/aspirational framing

Anthropic's OWN $1.5B copyright piracy settlement (for downloading 7 million pirated
books from Library Genesis and Pirate Library Mirror) receives no comparable standalone
WSJ accountability article. It is mentioned only in passing within a rare-books feature
story about AI companies buying physical books.

The vocabulary register inversion:
- Meta settlement: accountability ("addictive," "harmed," "ordered to pay," "sued," "misled")
- Anthropic same-week: aspiration ("potential revenue," "$2 trillion valuation,"
  "vaulted ahead," "IPO," "front-runner," "$30 trillion")

Financial architecture:
- News Corp (WSJ parent) has a $50M+ content licensing deal with OpenAI
- News Corp has a $50M+ content licensing deal with Meta (balanced)
- Anthropic has no disclosed News Corp content deal
- BUT: Anthropic's $1.5B Ode JV includes Goldman Sachs, Apollo, General Atlantic —
  overlapping with News Corp's private equity investor base

Cross-validates: Mechanism #27 (WSJ desk-level tone gap), Mechanism #22 (WSJ
aspirational Anthropic framing)

CONFOUNDERS:
- STRONG: Bobrowsky is the dedicated Meta beat reporter — covering the settlement
  is literally her job. The Anthropic IPO coverage is handled by different reporters
  (Driebusch, Ramkumar). This is desk/beat assignment, not individual bias.
- STRONG: The Meta settlement ($18B) is objectively a larger, more consequential
  news story than Anthropic's $30T TAM claim. Different coverage volume is expected.
- MODERATE: Meta's settlement resolves claims of harming children, which carries
  inherently more adversarial moral weight than a copyright piracy settlement
  involving pirated books.
- MODERATE: Pre-IPO companies receive aspirational coverage as an industry norm;
  WSJ's Anthropic coverage follows standard financial journalism templates.
- WEAK: Self-referencing Facebook Files is standard WSJ practice (they reference
  their own investigations regularly).

Adjusted asymmetry score: 0.28 (modest after heavy confounder load — the vocabulary
differential is real but largely explained by structural factors)
"""
import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestMechanism337Existence:
    """Verify mechanism #337 is documented in competitor-coverage-research.yaml."""

    def _collect_mechanism_ids(self, obj):
        """Recursively collect all mechanism_id values from nested YAML."""
        ids = []
        if isinstance(obj, dict):
            if 'mechanism_id' in obj:
                ids.append(obj['mechanism_id'])
            for v in obj.values():
                ids.extend(self._collect_mechanism_ids(v))
        elif isinstance(obj, list):
            for item in obj:
                ids.extend(self._collect_mechanism_ids(item))
        return ids

    def _find_mechanism(self, obj, target_id):
        """Recursively find a mechanism dict by its mechanism_id."""
        if isinstance(obj, dict):
            if obj.get('mechanism_id') == target_id:
                return obj
            for v in obj.values():
                result = self._find_mechanism(v, target_id)
                if result:
                    return result
        elif isinstance(obj, list):
            for item in obj:
                result = self._find_mechanism(item, target_id)
                if result:
                    return result
        return None

    def test_mechanism_337_exists(self):
        data = load_yaml('competitor-coverage-research.yaml')
        all_ids = self._collect_mechanism_ids(data)
        assert 337 in all_ids, "Mechanism #337 should exist in competitor-coverage-research.yaml"

    def test_mechanism_337_has_description(self):
        data = load_yaml('competitor-coverage-research.yaml')
        mech = self._find_mechanism(data, 337)
        assert mech is not None, "Mechanism #337 should be findable"
        assert 'description' in mech or 'pattern' in mech, \
            "Mechanism #337 should have a description or pattern"


class TestBobrowskySettlementArticle:
    """Verify the Meta settlement article attributes are documented."""

    def test_settlement_article_url(self):
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data)
        assert 'meta-reaches-18-billion-settlement' in yaml_str or 'child-safety-claims' in yaml_str, \
            "Bobrowsky's Meta settlement article URL should be documented"

    def test_settlement_article_accountability_vocabulary(self):
        """The Meta settlement article should document accountability vocabulary."""
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        accountability_terms = ['accountability', 'addictive', 'harmed', 'settlement', 'profit-driven']
        found = sum(1 for t in accountability_terms if t in yaml_str)
        assert found >= 2, f"Should document accountability vocabulary, found {found}/5 terms"

    def test_facebook_files_self_reference(self):
        """The article self-references WSJ's Facebook Files — document this."""
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'facebook files' in yaml_str, \
            "Should document WSJ's self-referencing of Facebook Files in settlement coverage"


class TestSameWeekAnthropicCoverage:
    """Verify documentation of same-week Anthropic aspirational coverage at WSJ."""

    def test_anthropic_30t_tam_documented(self):
        """The $30T TAM aspirational article should be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data).lower()
        assert '30 trillion' in yaml_str or '30t' in yaml_str or 'tam' in yaml_str, \
            "Anthropic $30T TAM coverage should be documented"

    def test_anthropic_ipo_aspirational_framing(self):
        """Anthropic IPO coverage should be documented as aspirational."""
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'aspirational' in yaml_str, "Aspirational framing should be documented"

    def test_anthropic_piracy_settlement_coverage_gap(self):
        """Anthropic $1.5B piracy settlement should be documented as lacking
        comparable standalone accountability article at WSJ."""
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data).lower()
        # Should document either the piracy settlement coverage gap or the books mention
        assert 'pirat' in yaml_str or 'copyright' in yaml_str or '1.5 billion' in yaml_str, \
            "Anthropic's piracy settlement coverage treatment should be documented"


class TestVocabularyRegisterInversion:
    """Verify the vocabulary register differential is documented."""

    def test_meta_accountability_register(self):
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'accountability' in yaml_str or 'skeptical' in yaml_str, \
            "Meta accountability vocabulary register should be documented"

    def test_bobrowsky_tone_value(self):
        """Bobrowsky's documented tone for Meta should be in the mixed/negative range."""
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data)
        assert '-0.15' in yaml_str or '-0.2' in yaml_str or 'mixed' in yaml_str.lower(), \
            "Bobrowsky's mixed-to-negative tone value should be documented"


class TestConfounderDocumentation:
    """Verify confounders are properly documented for mechanism #337."""

    def test_strong_confounders_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data).lower()
        # Should document beat assignment as a confounder
        assert 'beat' in yaml_str and 'assignment' in yaml_str, \
            "Beat assignment confounder should be documented"

    def test_news_value_differential_confounder(self):
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'news value' in yaml_str or 'moral weight' in yaml_str or 'consequential' in yaml_str, \
            "News value differential confounder should be documented"


class TestFinancialArchitecture:
    """Verify the financial relationships are documented."""

    def test_news_corp_openai_deal(self):
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'openai' in yaml_str, "News Corp-OpenAI deal should be documented"

    def test_news_corp_meta_deal(self):
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        assert 'meta' in yaml_str, "News Corp-Meta deal should be documented"

    def test_balanced_deal_structure(self):
        """WSJ is the balanced control — $50M/$50M."""
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data)
        assert '50' in yaml_str, "Balanced $50M deal amounts should be documented"


class TestCrossValidation:
    """Cross-validate against previously documented mechanisms."""

    def test_cross_references_mechanism_27(self):
        """Should reference or relate to Mechanism #27 (desk-level tone gap)."""
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data)
        # Mechanism 27 documents the Clark vs Bobrowsky desk gap
        assert '27' in yaml_str, "Should cross-reference desk-level mechanism #27"

    def test_wsj_desk_gap_consistent(self):
        """The settlement-week finding should be consistent with prior desk gap."""
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data).lower()
        # The prior finding: 0.60-point gap between startup and corporate desks
        assert 'desk' in yaml_str or 'corporate' in yaml_str, \
            "Desk assignment structure should be documented"


class TestAsymmetryScore:
    """Verify the asymmetry score is conservative and properly bounded."""

    def test_score_within_valid_range(self):
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data)
        # Find the score for mechanism 337
        # Should be modest (< 0.40) given heavy confounder load
        assert '0.28' in yaml_str or '0.2' in yaml_str or '0.3' in yaml_str, \
            "Asymmetry score should be in modest range given confounders"


class TestSourceURLIntegrity:
    """Verify source URLs are present for key evidence."""

    def test_meta_settlement_url(self):
        data = load_yaml('news-corp.yaml')
        yaml_str = yaml.dump(data)
        assert 'wsj.com' in yaml_str, "WSJ article URLs should be present"

    def test_anthropic_tam_url(self):
        """The Anthropic $30T TAM article URL should be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        yaml_str = yaml.dump(data)
        assert 'wsj.com' in yaml_str, "WSJ source URLs should be present"
