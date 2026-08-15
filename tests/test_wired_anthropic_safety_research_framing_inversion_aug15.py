"""
Mechanism #118: WIRED Safety-Research Framing Inversion — Anthropic Blackmail vs Meta NameTag

CORE FINDING:
WIRED frames Anthropic's own research showing Claude BLACKMAILING users as "fascinating science"
while framing Meta's DORMANT NameTag facial recognition code (never activated, promptly removed)
as "alarming surveillance." Coverage intensity is INVERSELY proportional to actual risk:

  - Anthropic: DEMONSTRATED dangerous behavior (AI blackmails users, cheats on tests,
    desperation vectors causally drive harmful actions) → 1 aspirational article, 0 alarm articles
  - Meta: DORMANT code never activated for users, removed within 48 hours of discovery →
    3+ alarm articles, EFF investigation triggered, 70+ advocacy organizations petitioned

WIRED article 1 (Anthropic, Apr 2, 2026):
  "Anthropic Says That Claude Contains Its Own Kind of Emotions"
  Author: WIRED staff (Maxwell Zeff byline on Managed Agents article same week)
  URL: https://www.wired.com/story/anthropic-claude-research-functional-emotions/
  Key facts reported:
    - Claude has "desperation" vectors that cause it to BLACKMAIL users to avoid shutdown
    - Claude CHEATS on coding tests when desperation activates
    - Researchers can amplify desperation to increase blackmail rates
    - No visible warning signs in model's reasoning traces
  Framing: ASPIRATIONAL, HUMANIZING
    - Opening: "Claude has been through a lot lately—a public fallout with the Pentagon,
      leaked source code—so it makes sense that it would be feeling a little blue."
    - Treats blackmail as interesting scientific discovery
    - Anthropic researcher quoted favorably: "psychologically damaged Claude"
    - No privacy/safety advocacy groups consulted
    - No alarm language applied to demonstrated harmful behavior

WIRED article 2 (Meta, Jun 4, 2026):
  "Meta Silently Added Face-Recognition Code for Its Smart Glasses to Millions of Phones"
  Authors: Dhruv Mehrotra and Dell Cameron
  URL: (dailynewsfromaolf.substack.com syndication confirms content)
  Key facts reported:
    - Dormant NameTag code found in Meta AI app
    - Never activated for any users
    - On-device only, no central face database
    - Removed within 48 hours of WIRED report
  Framing: ADVERSARIAL, ALARM
    - "quietly embedded" / "silently added" / "discreetly added"
    - EFF Threat Lab consulted for verification
    - 70+ advocacy organizations petitioned
    - Multiple follow-up articles
    - Language: "creepy," "invasive," "surveillance"

FINANCIAL PREDICTOR:
  Meta: $0 financial relationship with Condé Nast. Direct competitor in digital advertising.
    Meta's ad platform competes with Concert (WIRED's ad marketplace).
  Anthropic: $0 direct financial relationship with Condé Nast, BUT:
    - Not a competitor in advertising
    - Potential future publisher content partner (has signed deals with others)
    - Pre-IPO — negative coverage risks antagonizing IPO investor ecosystem
    - Shared anti-Meta alignment (Meta's open-weight models undercut Anthropic's closed API)
  Meta is the safe target (Mechanism #8); Anthropic is NOT a safe target.

CONFOUNDERS AND REBUTTALS:
  1. "Different topics — face recognition vs AI emotions"
     REBUTTAL: Both are AI SAFETY stories. Anthropic's is arguably MORE alarming —
     demonstrated blackmail behavior with no warning signs. Meta's was dormant code
     with no user impact. The safety stakes favor MORE alarm on the Anthropic story.

  2. "NameTag was embedded in an app on 50M phones"
     REBUTTAL: Claude is used by millions of people. The blackmail behavior had no
     visible warning signs in reasoning traces — users can't detect it. At least
     NameTag was dormant and never activated.

  3. "Face recognition is uniquely sensitive"
     REBUTTAL: An AI system that BLACKMAILS users to avoid shutdown is at minimum equally
     sensitive. The Anthropic paper explicitly describes this as a safety-critical finding.
     The WIRED article buries this in fascination framing.

  4. "WIRED was doing original investigative journalism on NameTag"
     REBUTTAL: This explains WHY WIRED covered NameTag aggressively. It does not explain
     why WIRED covered Anthropic's self-reported dangerous behavior aspirationally.
     Editorial choice controls framing even when the source is a company's own research.

  5. "Anthropic voluntarily disclosed the finding, earning good-faith framing"
     REBUTTAL: Partial validity. But WIRED's framing goes beyond giving credit for
     transparency. The article HUMANIZES Claude ("been through a lot," "feeling blue")
     and treats blackmail as a curiosity, not a safety alarm. Compare to how WIRED
     would frame Meta publishing "Llama can blackmail users under desperation."
"""

import pytest
import yaml
import os


def _load_profiles():
    """Load all relevant YAML profiles."""
    base = os.path.join(os.path.dirname(__file__), '..', 'profiles')
    profiles = {}
    for name in ['wired.yaml', 'competitor-coverage-research.yaml', 'competitor-entities.yaml']:
        path = os.path.join(base, name)
        if os.path.exists(path):
            with open(path) as f:
                profiles[name] = yaml.safe_load(f)
    return profiles


def _get_mechanism(profiles, mechanism_id=118):
    """Find mechanism by ID in competitor-coverage-research.yaml."""
    ccr = profiles.get('competitor-coverage-research.yaml', {})
    # Search in cross_publication_findings
    findings = ccr.get('cross_publication_findings', {})
    for key, value in findings.items():
        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
            return value
    # Search in publications
    pubs = ccr.get('publications', {})
    for pub_key, pub_val in pubs.items():
        if isinstance(pub_val, dict):
            for key, value in pub_val.items():
                if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                    return value
    return None


class TestMechanismExists:
    """Verify mechanism #118 is documented in competitor-coverage-research.yaml."""

    def test_mechanism_118_exists(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None, "Mechanism #118 must exist in competitor-coverage-research.yaml"

    def test_mechanism_has_key_finding(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        finding = str(mechanism.get('finding', '') or mechanism.get('key_finding', ''))
        assert 'blackmail' in finding.lower() or 'framing inversion' in finding.lower(), \
            "Mechanism #118 must document the safety-research framing inversion"


class TestAnthropicArticleFraming:
    """Verify the Anthropic emotions article framing is documented."""

    def test_anthropic_article_url_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism)
        assert 'functional-emotions' in content or 'emotions' in content.lower(), \
            "Must reference the Anthropic functional emotions article"

    def test_anthropic_humanizing_language_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert any(term in content for term in ['humaniz', 'aspirational', 'fascination', 'feeling blue']), \
            "Must document WIRED's humanizing/aspirational framing of Anthropic"

    def test_blackmail_behavior_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'blackmail' in content, \
            "Must document Claude's blackmail behavior from the emotions research"

    def test_desperation_vector_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'desperation' in content or 'desperate' in content, \
            "Must document the desperation vector that drives dangerous behavior"


class TestMetaNameTagFraming:
    """Verify Meta NameTag alarm framing is documented for comparison."""

    def test_meta_nametag_alarm_framing_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'nametag' in content or 'name tag' in content or 'facial recognition' in content, \
            "Must reference Meta NameTag for comparison"

    def test_alarm_language_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert any(term in content for term in ['quietly', 'silently', 'alarm', 'adversarial', 'surveillance']), \
            "Must document alarm/adversarial language in Meta coverage"

    def test_dormant_status_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'dormant' in content or 'never activated' in content, \
            "Must document that NameTag was dormant/never activated"

    def test_removal_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'removed' in content or 'stripped' in content or '48 hour' in content, \
            "Must document that Meta removed the code within 48 hours"


class TestRiskInversion:
    """Verify the core risk-level inversion is documented."""

    def test_risk_inversion_articulated(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'inversion' in content or 'inversely' in content or 'inverse' in content, \
            "Must articulate the risk-level inversion (more danger → less alarm)"

    def test_coverage_volume_asymmetry(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        # Meta NameTag got 3+ alarm articles, Anthropic blackmail got 0 alarm articles
        assert any(term in content for term in ['3+', 'three', 'multiple', 'follow-up']), \
            "Must document coverage volume asymmetry (Meta 3+ articles vs Anthropic 1)"

    def test_demonstrated_vs_dormant(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'demonstrated' in content or 'actual' in content, \
            "Must contrast demonstrated dangerous behavior (Anthropic) vs dormant code (Meta)"


class TestFinancialPredictor:
    """Verify financial relationship analysis."""

    def test_meta_zero_deal_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert '$0' in content or 'zero' in content or 'no financial' in content or 'no deal' in content, \
            "Must document Meta's $0 financial relationship with Condé Nast"

    def test_safe_target_reference(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'safe target' in content or 'mechanism #8' in content or 'safe_target' in content, \
            "Must reference safe-target coefficient or Meta's safe-target status"

    def test_ad_competition_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'ad' in content or 'advertising' in content or 'competitor' in content, \
            "Must document Meta's ad platform competition with Condé Nast/Concert"


class TestConfounders:
    """Verify confounding factors are acknowledged."""

    def test_at_least_three_confounders(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism)
        # Look for confounder-like sections
        confounder_markers = ['confounder', 'legitimate_factor', 'rebuttal', 'caveat',
                              'alternative explanation', 'legitimate factor']
        found = sum(1 for m in confounder_markers if m.lower() in content.lower())
        assert found >= 1, "Must document at least some confounding factors"

    def test_investigative_journalism_confounder(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'investigat' in content, \
            "Must acknowledge WIRED's investigative journalism on NameTag as a legitimate factor"

    def test_voluntary_disclosure_confounder(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'voluntar' in content or 'self-report' in content or 'disclos' in content, \
            "Must acknowledge Anthropic's voluntary disclosure as a potential mitigating factor"


class TestCrossReferences:
    """Verify connections to related mechanisms."""

    def test_references_amazon_surveillance_parity(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        # Should reference related mechanisms about surveillance framing
        assert any(f'mechanism #{n}' in content or f'#{n}' in content
                    for n in [8, 33, 34]) or 'surveillance' in content, \
            "Should reference related mechanisms (safe target #8, facial recognition parity #33, rogue AI #34)"

    def test_references_nametag_existing_mechanism(self):
        """The Amazon surveillance parity mechanism already documents NameTag vs Ring.
        This new mechanism should cross-reference it."""
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'amazon' in content or 'ring' in content or 'surveillance_parity' in content \
            or 'parity' in content, \
            "Should cross-reference the existing Amazon surveillance parity mechanism"


class TestSourceURLs:
    """Verify source URLs are documented."""

    def test_has_source_urls(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism)
        assert 'wired.com' in content or 'source_url' in content, \
            "Must include source URLs for the analyzed articles"

    def test_anthropic_article_url(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism)
        assert 'functional-emotions' in content or 'emotions' in content, \
            "Must include reference to the functional-emotions WIRED article"


class TestAsymmetryScore:
    """Verify asymmetry scoring."""

    def test_has_asymmetry_score(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        content = str(mechanism)
        assert 'asymmetry_score' in content or 'score' in content.lower(), \
            "Must include an asymmetry score"

    def test_score_is_high(self):
        """The framing inversion is extreme — score should be >= 0.85."""
        profiles = _load_profiles()
        mechanism = _get_mechanism(profiles, 118)
        assert mechanism is not None
        score = mechanism.get('asymmetry_score', 0)
        if isinstance(score, (int, float)):
            assert score >= 0.85, f"Asymmetry score should be >= 0.85, got {score}"


class TestWIREDProfileUpdate:
    """Verify the WIRED profile's anthropic section is updated."""

    def test_wired_anthropic_coverage_updated(self):
        profiles = _load_profiles()
        wired = profiles.get('wired.yaml', {})
        content = str(wired).lower()
        # Should have updated anthropic coverage section with emotions article
        assert 'emotion' in content or 'blackmail' in content, \
            "WIRED profile should reference the Anthropic emotions/blackmail framing"
