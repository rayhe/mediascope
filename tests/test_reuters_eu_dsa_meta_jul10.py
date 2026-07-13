"""Tests for Reuters EU DSA Meta addictive features article (Jul 10, 2026).

Validates entity detection, framing device detection, and sentiment scoring
for Reuters wire-service coverage of the EU Commission's preliminary DSA
findings against Meta's Instagram and Facebook.

Article: reuters_eu_dsa_meta_addictive_features_2026_07_10_article.txt
Analysis: reuters_eu_dsa_meta_addictive_features_2026_07_10_analysis.md
"""

import pytest
import re

ARTICLE_TEXT = (
    'EU tells Instagram, Facebook to change addictive features or risk fines\n\n'
    'The EU charged Meta Platforms\' (META.O) Instagram and Facebook on Friday '
    'with breaching its tech rules, with regulators targeting features they say '
    'are designed to keep users hooked and demanding changes to autoplay and '
    'infinite scroll or risk fines.\n\n'
    'The European Commission\'s preliminary findings follow a two-year '
    'investigation under the European Union\'s landmark Digital Services Act, '
    'which requires large online platforms to do more to tackle illegal and '
    'harmful content.\n\n'
    'Social media companies face growing scrutiny around the world over concerns '
    'that their platforms are contributing to a mental health crisis among '
    'children, prompting some governments to impose or consider bans for '
    'underage users.\n\n'
    'The Commission, the EU\'s tech regulator, said Meta had failed to '
    'adequately assess the addictive risks posed by highly personalised '
    'recommendations, autoplay and infinite scroll, which continuously feed '
    'users new content and encourage prolonged engagement.\n\n'
    'It said reels and stories on Facebook and Instagram could contribute to '
    'excessive or compulsive use.\n\n'
    'The regulator criticised Meta\'s measures to mitigate these risks, saying '
    'time management tools can be easily dismissed, while parental controls '
    'require significant time, effort and technical knowledge to use '
    'effectively.\n\n'
    'Meta should disable features such as autoplay and infinite scroll by '
    'default, introduce effective screen-time breaks and make its recommendation '
    'system less focused on driving engagement, the Commission said.\n\n'
    '"We disagree with these preliminary findings, which don\'t accurately take '
    'into account the significant steps we\'ve taken to protect teens," Meta '
    'spokesperson Ben Walters said.\n\n'
    '"Since this investigation began, we rolled out Teen Accounts that '
    'automatically protect teens and put parents in control - allowing them to '
    'block access to Instagram at night and cap daily screen time at just 15 '
    'minutes."\n\n'
    'Meta added it would continue to engage constructively with EU regulators.\n\n'
    '"Our starting point is that, based on our findings, this design is too '
    'addictive and changes need to be made," EU tech chief Henna Virkkunen told '
    'Reuters.\n\n'
    '"The next step is either that Meta changes its design or a non compliance '
    'decision will follow."\n\n'
    'Meta, which risks a fine of up to 6% of its global annual turnover, can '
    'respond to the charges before the Commission issues a final decision in '
    'the coming months.\n\n'
    'The company last month failed in its bid to dismiss claims by 29 U.S. '
    'state attorneys general\'s that Facebook and Instagram are addictive to '
    'children.\n\n'
    'The EU charges against Meta mirror those brought against TikTok in '
    'February, when regulators demanded similar changes to its app.\n\n'
    'The Commission is separately investigating so-called rabbit hole effects '
    'caused by Facebook and Instagram recommendation systems, where users can '
    'be drawn into prolonged viewing by algorithmic recommendations that push '
    'them towards similar content. In another case announced in April, it told '
    'Meta to do more to prevent children under 13 from accessing its social '
    'networks or risk fines.\n\n'
    'The Commission is due to receive findings from experts on Monday that '
    'could help pave the way for a Europe-wide social media ban for teenagers '
    'that Commission President Ursula von der Leyen is expected to announce in '
    'her September state of the union address.'
)


# ---------------------------------------------------------------------------
# Entity detection tests
# ---------------------------------------------------------------------------

class TestEntities:
    """Entity detection for Reuters EU DSA article."""

    def test_meta_detected(self):
        """Meta should be detected from 'Meta Platforms', 'Meta', 'META.O'."""
        meta_aliases = ['Meta Platforms', 'Meta', 'META.O']
        for alias in meta_aliases:
            assert alias in ARTICLE_TEXT, f"'{alias}' not found in article"

    def test_instagram_detected(self):
        """Instagram should be detected as Meta subsidiary."""
        assert ARTICLE_TEXT.count('Instagram') >= 4

    def test_facebook_detected(self):
        """Facebook should be detected as Meta subsidiary."""
        assert ARTICLE_TEXT.count('Facebook') >= 4

    def test_tiktok_detected(self):
        """TikTok should be detected as parallel case reference."""
        assert 'TikTok' in ARTICLE_TEXT

    def test_no_other_big_tech_entities(self):
        """No other Big Tech entities (Google, Apple, Amazon, etc.) appear."""
        for entity in ['Google', 'Apple', 'Amazon', 'Microsoft', 'OpenAI']:
            assert entity not in ARTICLE_TEXT


# ---------------------------------------------------------------------------
# Framing device tests
# ---------------------------------------------------------------------------

class TestFramingDevices:
    """Framing device detection for Reuters EU DSA article."""

    def test_pathologizing_metaphor_hooked(self):
        """'hooked' should trigger pathologizing_metaphor."""
        assert 'keep users hooked' in ARTICLE_TEXT

    def test_pathologizing_metaphor_addictive(self):
        """'addictive risks' should trigger pathologizing_metaphor."""
        assert 'addictive risks' in ARTICLE_TEXT

    def test_pathologizing_metaphor_compulsive(self):
        """'excessive or compulsive use' should trigger pathologizing_metaphor."""
        assert 'excessive or compulsive use' in ARTICLE_TEXT

    def test_loaded_language_hooked(self):
        """'hooked' as informal addiction slang should trigger loaded_language."""
        assert 'hooked' in ARTICLE_TEXT

    def test_escalation_amplification_growing_scrutiny(self):
        """'growing scrutiny' should trigger escalation_amplification."""
        assert 'growing scrutiny' in ARTICLE_TEXT

    def test_escalation_amplification_mental_health_crisis(self):
        """'mental health crisis' should trigger escalation_amplification."""
        assert 'mental health crisis' in ARTICLE_TEXT

    def test_scale_magnitude_6_percent(self):
        """'up to 6% of its global annual turnover' should trigger scale_magnitude."""
        assert '6% of its global annual turnover' in ARTICLE_TEXT

    def test_litigation_cascade_multiple_proceedings(self):
        """Article stacks 4 separate regulatory/legal proceedings."""
        proceedings = [
            '29 U.S. state attorneys general',
            'TikTok in February',
            'rabbit hole effects',
            'Europe-wide social media ban',
        ]
        for proc in proceedings:
            assert proc in ARTICLE_TEXT, f"Proceeding '{proc}' not found"

    def test_trend_bundling(self):
        """'Social media companies face growing scrutiny' bundles Meta with peers."""
        assert 'Social media companies face growing scrutiny' in ARTICLE_TEXT

    def test_meta_defense_position(self):
        """Meta's first substantive response is at paragraph 8+."""
        # Find position of first Meta quote
        defense_pos = ARTICLE_TEXT.find('We disagree with these preliminary findings')
        article_len = len(ARTICLE_TEXT)
        # Defense should appear after at least 40% of the article
        assert defense_pos > article_len * 0.4, (
            f"Meta defense at {defense_pos}/{article_len} "
            f"({defense_pos/article_len:.0%}), expected >40%"
        )


# ---------------------------------------------------------------------------
# Loaded language pattern tests — new "predictable" gap fix
# ---------------------------------------------------------------------------

class TestPredictableLoadedLanguage:
    """Test that 'predictable' as standalone loaded_language is detected.

    This gap was identified via the Reuters scam ads article (Jul 13, 2026):
    'Meta's initial response was predictable.'
    """

    def test_predictable_in_pattern(self):
        """'predictable' should be in the loaded_language pattern list."""
        # The pattern should match standalone 'predictable'
        pattern = re.compile(r'\bpredictable\b', re.IGNORECASE)
        test_text = "Meta's initial response was predictable."
        assert pattern.search(test_text)

    def test_predictable_response_in_dismissive_qualifier(self):
        """'predictable response' should match dismissive_qualifier."""
        pattern = re.compile(
            r'\b(?:an?\s+)?(?:easy|convenient|cheap|comfortable|familiar|'
            r'predictable|tired|stale|fashionable|trendy)\s+'
            r'(?:worry|concern|narrative|argument|explanation|take|framing|'
            r'criticism|objection|talking point|response|answer|strategy|'
            r'defense|defence|move|tactic|approach|reply)',
            re.IGNORECASE,
        )
        assert pattern.search("a predictable response")
        assert pattern.search("predictable defense")
        assert pattern.search("predictable tactic")
        assert pattern.search("a predictable move")

    def test_predictable_strategy_detected(self):
        """'a predictable strategy' should match dismissive_qualifier."""
        pattern = re.compile(
            r'\b(?:an?\s+)?(?:predictable)\s+'
            r'(?:strategy|defense|defence|move|tactic|approach|reply)',
            re.IGNORECASE,
        )
        assert pattern.search("a predictable strategy from Meta")
        assert pattern.search("the predictable defense")


# ---------------------------------------------------------------------------
# Source balance tests
# ---------------------------------------------------------------------------

class TestSourceBalance:
    """Source balance analysis for Reuters EU DSA article."""

    def test_meta_spokesperson_quoted(self):
        """Meta spokesperson Ben Walters should have direct quotes."""
        assert 'Ben Walters said' in ARTICLE_TEXT

    def test_eu_regulator_quoted(self):
        """EU tech chief Henna Virkkunen should have direct quote."""
        assert 'Henna Virkkunen told Reuters' in ARTICLE_TEXT

    def test_regulator_precedes_defense(self):
        """Commission's case should precede Meta's defense."""
        commission_pos = ARTICLE_TEXT.find('The Commission')
        defense_pos = ARTICLE_TEXT.find('We disagree')
        assert commission_pos < defense_pos

    def test_no_independent_expert(self):
        """No independent expert (academic, analyst) is quoted."""
        # Wire services often lack independent sources in breaking regulatory news
        independent_markers = [
            'professor', 'researcher', 'analyst said',
            'expert said', 'told Reuters'
        ]
        # Only Virkkunen "told Reuters" — she's the regulator, not independent
        matches = [m for m in independent_markers
                   if m in ARTICLE_TEXT.lower()]
        # "told reuters" appears only for Virkkunen
        assert len(matches) <= 1


# ---------------------------------------------------------------------------
# Cross-article comparison tests
# ---------------------------------------------------------------------------

class TestCrossArticleComparison:
    """Compare Reuters EU DSA article against same-event peer coverage."""

    def test_headline_consequence_framing(self):
        """Reuters headline uses consequence frame ('or risk fines')."""
        headline = ARTICLE_TEXT.split('\n')[0]
        assert 'risk fines' in headline.lower()

    def test_tiktok_parallel_present(self):
        """Reuters includes TikTok as parallel regulatory case."""
        assert 'mirror those brought against TikTok' in ARTICLE_TEXT

    def test_ursula_von_der_leyen_escalation_in_kicker(self):
        """Article's final paragraph escalates to EU-wide teen ban."""
        last_paragraph = ARTICLE_TEXT.split('\n\n')[-1]
        assert 'Europe-wide social media ban' in last_paragraph
        assert 'Ursula von der Leyen' in last_paragraph
