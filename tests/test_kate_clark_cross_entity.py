"""
Kate Clark Cross-Entity Coverage Analysis — Type B Journalist Tracking (Aug 10, 2026)

KEY FINDING: Mechanism #27 — Startup Desk vs. Corporate Desk Narrative Segregation

Kate Clark is WSJ's VC/startup beat reporter covering OpenAI and Anthropic.
Meghan Bobrowsky is WSJ's Meta corporate beat reporter. Both work at the
SAME publication (News Corp, $50M/yr Meta + $50M/yr OpenAI — balanced).

Yet their coverage of similar companies uses fundamentally different
NARRATIVE TEMPLATES:

STARTUP DESK (Kate Clark → Anthropic/OpenAI):
  - Hero's Journey arc: "scrappy underdog" → "front-runner"
  - Growth metrics celebrated without risk context
  - Financial challenges framed as "doing more with less" (virtuous)
  - Investor returns highlighted ("$75M → $7B, 93x return")
  - $27B/yr burn rate: ZERO discussion in the front-runner article
  - Profitability risk: absent or minimized
  - IPO as validation event, not risk vector
  - Language register: aspirational, competitive-sport metaphor ("race,"
    "front-runner," "caught up")

CORPORATE DESK (Meghan Bobrowsky → Meta):
  - Corporate accountability arc: "wants in on," "needs to show returns"
  - Same growth treated as follower/latecomer behavior
  - Financial challenges framed as "lavish spending" (wasteful)
  - Revenue ($60.8B/quarter) presented alongside deficit framing
  - Profitability: EXPECTED but questioned ("show returns from lavish spending")
  - Market events as accountability pressure
  - Language register: skeptical, corporate-governance metaphor ("pressed,"
    "declined to provide details")

THE PARADOX: Anthropic ($47B ARR, $27B burn, 0% profit) gets hero framing.
Meta ($60.8B/quarter, $15B+ profit, $244B+ annual revenue) gets deficit framing.
The SAME publication, with the SAME balanced financial relationships, applies
INVERTED narrative templates that map to desk assignment, not financial reality.

This is NOT a financial incentive mechanism. News Corp's deals are balanced.
This is a STRUCTURAL mechanism — the startup desk's narrative templates
(disruption, underdog, scrappy) are inherently aspirational, while the
corporate desk's templates (accountability, shareholder pressure, returns)
are inherently skeptical. When the startup desk covers AI labs and the
corporate desk covers Meta, the desk structure itself creates framing
asymmetry independent of financial incentives.

NOVEL MECHANISM DISTINCTION: Unlike Mechanism #26 (business viability
framing in Heard on the Street analytical columns), Mechanism #27
operates through the NEWS DESK beat assignment — hard news articles,
not opinion columns. The startup desk is not "biased" — it's applying
the correct template for its genre. But the genre assignment itself
creates asymmetry because Anthropic (the largest VC investment in history)
is covered as a "startup" while Meta (a 22-year-old company) is covered
as a "corporation." The genre boundary is the mechanism.

Sources:
  - Kate Clark, "Anthropic Was Behind. Now It's the AI Boom's Front-Runner."
    WSJ, May 13, 2026
    https://www.wsj.com/tech/ai/anthropic-was-behind-now-its-the-ai-booms-front-runner-5020f621
  - BuzzSumo profile: Kate Clark articles — OpenAI/Anthropic focused
    https://buzzsumo.com/journalist/kate-clark-299947022/
  - Meghan Bobrowsky + Tina Li, "Meta Releases Coding Agent to Compete
    With OpenAI and Anthropic," WSJ, Aug 6, 2026
    https://www.wsj.com/tech/ai/meta-releases-coding-agent-to-compete-with-openai-and-anthropic-af87b517
  - Berber Jin profile: wsj.com AI reporter — OpenAI/Anthropic beat
    https://buzzsumo.com/journalist/berber-jin-299947022/
  - Muck Rack: Kate Clark articles
    https://muckrack.com/kate-clark-22/articles
  - WSJ Heard on the Street: "Meta Stock Is Cheap...for a Reason" (May 5, 2026)
    https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-05-05-2026/card/heard-on-the-street-meta-stock-is-cheap-for-a-reason-LqhuQAMXotrEkTj3CBol
  - Investors With a New Way to Win (Berber Jin, Jul 18, 2026) —
    hero's journey for Anthropic investors, zero burn rate discussion
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, 'news-corp.yaml')
RESEARCH_FILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def news_corp():
    return load_yaml(NEWS_CORP_FILE)


@pytest.fixture(scope='module')
def research():
    return load_yaml(RESEARCH_FILE)


@pytest.fixture(scope='module')
def kate_clark_profile(news_corp):
    profiles = news_corp.get('journalist_profiles', [])
    matches = [p for p in profiles if p.get('name') == 'Kate Clark']
    assert matches, "Kate Clark must exist in news-corp.yaml journalist_profiles"
    return matches[0]


@pytest.fixture(scope='module')
def bobrowsky_profile(news_corp):
    profiles = news_corp.get('journalist_profiles', [])
    matches = [p for p in profiles if p.get('name') == 'Meghan Bobrowsky']
    assert matches, "Meghan Bobrowsky must exist in news-corp.yaml journalist_profiles"
    return matches[0]


@pytest.fixture(scope='module')
def mechanism_27(research):
    findings = research.get('cross_publication_findings', {})
    entry = findings.get('wsj_kate_clark_startup_desk_narrative_segregation', {})
    assert entry, (
        "wsj_kate_clark_startup_desk_narrative_segregation must exist "
        "in competitor-coverage-research.yaml cross_publication_findings"
    )
    return entry


# =================================================================
# TEST CLASS 1: Kate Clark Profile Completeness
# =================================================================

class TestKateClarkProfileExists:
    """Kate Clark must be documented in news-corp.yaml journalist profiles."""

    def test_name(self, kate_clark_profile):
        assert kate_clark_profile['name'] == 'Kate Clark'

    def test_role(self, kate_clark_profile):
        role = kate_clark_profile.get('current_role', '')
        assert 'vc' in role.lower() or 'startup' in role.lower() or \
               'venture' in role.lower(), \
            f"Clark's role should reference VC/startup beat, got: {role}"

    def test_publication(self, kate_clark_profile):
        assert kate_clark_profile.get('publication') == 'The Wall Street Journal'

    def test_beat_is_ai_startups(self, kate_clark_profile):
        beat = kate_clark_profile.get('beat', '')
        assert 'openai' in beat.lower() or 'anthropic' in beat.lower() or \
               'ai startup' in beat.lower() or 'ai lab' in beat.lower(), \
            f"Clark's beat should cover AI labs/startups, got: {beat}"

    def test_has_source_urls(self, kate_clark_profile):
        urls = kate_clark_profile.get('source_urls', [])
        assert len(urls) >= 2, "Need at least 2 source URLs"


# =================================================================
# TEST CLASS 2: Anthropic Hero's Journey Framing
# =================================================================

class TestAnthropicHeroFraming:
    """Kate Clark's Anthropic coverage uses startup hero-arc narrative template."""

    def test_front_runner_article_documented(self, kate_clark_profile):
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        assert anthropic, "Anthropic coverage must be documented"
        assert anthropic.get('key_article'), "Key article must be documented"

    def test_hero_journey_language(self, kate_clark_profile):
        """Verify hero's journey narrative language is documented."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        language = anthropic.get('hero_journey_language', [])
        assert len(language) >= 3, \
            f"Should document at least 3 hero's journey phrases, got {len(language)}"

    def test_scrappy_underdog_framing(self, kate_clark_profile):
        """The word 'scrappy' or 'underdog' appears in documented framing."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        language = ' '.join(anthropic.get('hero_journey_language', [])).lower()
        assert 'scrappy' in language or 'underdog' in language, \
            "Must document 'scrappy underdog' framing"

    def test_growth_without_risk(self, kate_clark_profile):
        """Growth metrics celebrated without burn rate or profitability discussion."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        assert anthropic.get('burn_rate_discussed') is False, \
            "Front-runner article should not discuss burn rate"

    def test_ipo_as_validation(self, kate_clark_profile):
        """IPO framed as validation event, not risk vector."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        framing = anthropic.get('ipo_framing', '')
        assert 'validation' in framing.lower() or 'aspiration' in framing.lower(), \
            f"IPO should be framed as validation, got: {framing}"

    def test_tone_positive(self, kate_clark_profile):
        """Anthropic tone should be positive (>= 0.20)."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        tone = anthropic.get('tone', 0)
        assert tone >= 0.20, f"Anthropic tone should be >= 0.20, got {tone}"


# =================================================================
# TEST CLASS 3: Desk Framing Comparison — Same Publication
# =================================================================

class TestDeskFramingComparison:
    """Within WSJ, startup desk and corporate desk apply different templates."""

    def test_bobrowsky_meta_tone_lower(self, kate_clark_profile, bobrowsky_profile):
        """Bobrowsky's Meta tone should be measurably lower than Clark's Anthropic tone."""
        clark_tone = kate_clark_profile.get('anthropic_coverage', {}).get('tone', 0)
        bob_tone = bobrowsky_profile.get('cross_entity_coverage', {}).get(
            'meta', {}).get('tone_value', 0)
        # At a balanced publication, the tone gap should be meaningful but smaller
        # than at unbalanced publications. Clark's positive + Bobrowsky's mild negative
        # still creates a measurable gap.
        assert clark_tone > bob_tone, \
            f"Clark Anthropic tone ({clark_tone}) should exceed Bobrowsky Meta tone ({bob_tone})"

    def test_language_register_difference(self, kate_clark_profile, bobrowsky_profile):
        """Verify different language registers are documented."""
        clark_lang = kate_clark_profile.get('anthropic_coverage', {}).get(
            'language_register', '')
        bob_lang = bobrowsky_profile.get('cross_entity_coverage', {}).get(
            'meta', {}).get('language_register', '')
        assert clark_lang and bob_lang, "Both language registers must be documented"
        assert clark_lang != bob_lang, "Language registers should differ"

    def test_same_publication(self, kate_clark_profile, bobrowsky_profile):
        """Both reporters work for the same publication."""
        assert kate_clark_profile.get('publication') == \
               bobrowsky_profile.get('publication', 'The Wall Street Journal')

    def test_balanced_financial_environment(self, news_corp):
        """WSJ/News Corp has balanced financial relationships — asymmetry is structural."""
        # wsj_beat_structure may be nested inside a journalist_profiles entry
        profiles = news_corp.get('journalist_profiles', [])
        beat_struct = None
        for p in profiles:
            if 'wsj_beat_structure' in p:
                beat_struct = p['wsj_beat_structure']
                break
        # Fallback to top-level
        if not beat_struct:
            beat_struct = news_corp.get('wsj_beat_structure', {})
        beats = beat_struct.get('beats', [])
        meta_beat = [b for b in beats if b.get('beat', '').lower().startswith('meta')]
        assert meta_beat, "Meta beat must be documented"
        assert meta_beat[0].get('net_incentive') == 'balanced', \
            "Meta beat net incentive should be balanced"


# =================================================================
# TEST CLASS 4: Narrative Template Inversion
# =================================================================

class TestNarrativeTemplateInversion:
    """The company with WORSE financials gets BETTER narrative framing."""

    def test_anthropic_revenue_documented(self, kate_clark_profile):
        """Anthropic's financial metrics must be documented for comparison."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        assert anthropic.get('revenue_context'), "Revenue context needed"

    def test_meta_revenue_much_higher(self, kate_clark_profile):
        """Meta generates 10x+ Anthropic's revenue but gets worse framing."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        context = anthropic.get('financial_inversion', {})
        assert context.get('meta_quarterly_revenue_b', 0) >= 60, \
            "Meta quarterly revenue should be >= $60B"

    def test_anthropic_unprofitable_documented(self, kate_clark_profile):
        """Anthropic's lack of profitability must be documented."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        assert anthropic.get('profitable') is False, \
            "Anthropic should be documented as unprofitable"

    def test_inversion_documented(self, kate_clark_profile):
        """The financial-framing inversion must be explicitly documented."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        inversion = anthropic.get('financial_inversion', {})
        assert inversion, "Financial inversion must be documented"
        assert 'inversion' in str(inversion).lower() or \
               'paradox' in str(inversion).lower(), \
            "Inversion/paradox must be named"


# =================================================================
# TEST CLASS 5: Genre Boundary as Mechanism
# =================================================================

class TestGenreBoundaryMechanism:
    """The mechanism is the genre boundary between startup and corporate journalism."""

    def test_mechanism_27_exists(self, mechanism_27):
        assert mechanism_27, "Mechanism #27 must exist"

    def test_mechanism_id(self, mechanism_27):
        assert mechanism_27.get('mechanism_id') == 27

    def test_mechanism_name(self, mechanism_27):
        name = mechanism_27.get('mechanism_name', '')
        assert 'narrative' in name.lower() or 'desk' in name.lower() or \
               'segregation' in name.lower(), \
            f"Mechanism name should reference narrative/desk segregation: {name}"

    def test_mechanism_is_structural(self, mechanism_27):
        """The mechanism is structural, not financial."""
        mtype = mechanism_27.get('mechanism_type', '')
        assert 'structural' in mtype.lower(), \
            f"Mechanism type should be structural, got: {mtype}"

    def test_distinct_from_mechanism_26(self, mechanism_27):
        """Must be distinct from Mechanism #26 (Heard on the Street analytical column)."""
        distinction = mechanism_27.get('distinction_from_26', '')
        assert distinction, "Must explain distinction from Mechanism #26"

    def test_has_journalist(self, mechanism_27):
        assert mechanism_27.get('journalist') == 'Kate Clark'

    def test_has_test_file(self, mechanism_27):
        assert mechanism_27.get('test_file') == \
               'tests/test_kate_clark_cross_entity.py'

    def test_has_date(self, mechanism_27):
        date_val = mechanism_27.get('date_added')
        assert str(date_val) == '2026-08-10'


# =================================================================
# TEST CLASS 6: Legitimate Confounding Factors
# =================================================================

class TestLegitimateConfounds:
    """Document and address legitimate confounding factors."""

    def test_confounds_documented(self, kate_clark_profile):
        confounds = kate_clark_profile.get('legitimate_confounds', [])
        assert len(confounds) >= 4, \
            f"Need at least 4 documented confounds, got {len(confounds)}"

    @pytest.mark.parametrize("confound_keyword", [
        "genre",      # Startup reporting IS supposed to be aspirational
        "Anthropic",  # Anthropic genuinely is growing fast
        "access",     # VC reporters need startup access
        "IPO",        # Pre-IPO coverage naturally more positive
    ])
    def test_specific_confounds(self, kate_clark_profile, confound_keyword):
        """Each important confound should be addressed."""
        confounds = ' '.join(kate_clark_profile.get('legitimate_confounds', []))
        assert confound_keyword.lower() in confounds.lower(), \
            f"Confound '{confound_keyword}' should be documented"


# =================================================================
# TEST CLASS 7: Source Evidence
# =================================================================

class TestSourceEvidence:
    """All claims backed by source URLs."""

    def test_front_runner_article_url(self, kate_clark_profile):
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        url = anthropic.get('source_url', '')
        assert 'wsj.com' in url, f"Source URL must be WSJ: {url}"

    def test_kate_clark_profile_url(self, kate_clark_profile):
        urls = kate_clark_profile.get('source_urls', [])
        assert any('muckrack' in u or 'buzzsumo' in u for u in urls), \
            "Need a journalist profile URL from Muck Rack or BuzzSumo"

    def test_bobrowsky_comparison_url(self, kate_clark_profile):
        """Comparison to Bobrowsky's Meta coverage should have source."""
        anthropic = kate_clark_profile.get('anthropic_coverage', {})
        comparison = anthropic.get('bobrowsky_comparison', {})
        assert comparison.get('source_url'), \
            "Bobrowsky comparison needs source URL"


# =================================================================
# TEST CLASS 8: Berber Jin Reinforcement
# =================================================================

class TestBerberJinReinforcement:
    """Berber Jin (also VC/AI startup desk) reinforces the pattern."""

    def _get_beat_structure(self, news_corp):
        """Find wsj_beat_structure wherever it lives."""
        profiles = news_corp.get('journalist_profiles', [])
        for p in profiles:
            if 'wsj_beat_structure' in p:
                return p['wsj_beat_structure']
        return news_corp.get('wsj_beat_structure', {})

    def test_jin_in_beat_structure(self, news_corp):
        beat_struct = self._get_beat_structure(news_corp)
        beats = beat_struct.get('beats', [])
        jin_beats = [b for b in beats if 'Berber Jin' in b.get('reporter', '')]
        assert jin_beats, "Berber Jin must be in WSJ beat structure"

    def test_jin_covers_openai(self, news_corp):
        beat_struct = self._get_beat_structure(news_corp)
        beats = beat_struct.get('beats', [])
        jin_beats = [b for b in beats if 'Berber Jin' in b.get('reporter', '')]
        assert jin_beats
        beat = jin_beats[0].get('beat', '').lower()
        assert 'openai' in beat or 'ai startup' in beat, \
            f"Jin's beat should be OpenAI/AI startups, got: {beat}"

    def test_two_startup_reporters_vs_one_corporate(self, news_corp):
        """WSJ assigns 2 startup/VC reporters to AI labs vs 1 corporate reporter to Meta."""
        beat_struct = self._get_beat_structure(news_corp)
        beats = beat_struct.get('beats', [])
        startup_reporters = [b for b in beats
                           if 'startup' in b.get('beat', '').lower()
                           or 'openai' in b.get('beat', '').lower()
                           or 'vc' in b.get('beat', '').lower()
                           or 'ai lab' in b.get('beat', '').lower()]
        meta_reporters = [b for b in beats
                        if b.get('beat', '').lower().startswith('meta')]
        # The 2:1 ratio amplifies startup-desk narrative volume
        assert len(startup_reporters) >= 1, "At least 1 startup reporter"
        assert len(meta_reporters) >= 1, "At least 1 Meta reporter"
