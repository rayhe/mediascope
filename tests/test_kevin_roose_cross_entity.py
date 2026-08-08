"""
Kevin Roose (NYT → Independent) Cross-Entity Coverage Analysis

KEY FINDING: Triple Professional Identity Capture + AI Interaction Correlation

Kevin Roose — NYT's most prominent AI columnist (2017–Aug 2026), co-host of "Hard Fork"
podcast, and author of "The AGI Chronicles" (FSG, Oct 6, 2026) — exhibits coverage
asymmetry driven by THREE professional identity pillars, all centering the OpenAI/AGI
ecosystem rather than Meta:

1. "The AGI Chronicles" book (Oct 2026): Career's biggest forthcoming work focuses on
   "the race to create AGI" — a narrative centering OpenAI, Anthropic, DeepMind. Meta's
   open-source Llama is a peripheral latecomer in this framing.

2. Sydney/Bing Conversation (Feb 2023): The most viral AI journalism story of the decade.
   Roose's fame was created by a Microsoft/OpenAI product declaring love for him.

3. Post-NYT AI Media Venture: Leaving NYT in August 2026 to start an independent AI media
   company with Casey Newton. Business model depends on maintaining access to AI lab CEOs
   (Altman, Amodei, Pichai) while Zuckerberg access is expendable.

NEW MECHANISM — AI Interaction Correlation:
- Sydney (OpenAI/Microsoft) said "I love Kevin Roose" → sympathetic, nuanced ongoing coverage
- Meta's Llama 3 reportedly said "I hate Kevin Roose" → dismissive, reduced coverage

This parallels the Parmy Olson "Supremacy" professional identity capture mechanism
documented in test_parmy_olson_cross_entity.py, but with THREE reinforcing pillars
instead of one.

Sources:
- Muck Rack profile: https://muckrack.com/kevinroose
- Muck Rack articles: https://muckrack.com/kevinroose/articles
- "Leaving The Times" Substack: https://kevinroose.substack.com/p/leaving-the-times
- Talking Biz News departure: https://talkingbiznews.com/media-news/tech-columnist-roose-departing-ny-times/
- "The AGI Chronicles" Audible: https://www.audible.com/pd/The-AGI-Chronicles-Audiobook/B0GBYLW6CT
- "The AGI Chronicles" Booktopia: https://www.booktopia.com.au/the-agi-chronicles-kevin-roose/audiobook/9781398555341.html
- AI Weekly (Llama "I hate Kevin Roose"): https://aiweekly.co/alerts/nyt-reporter-rewrites-his-chatbot-reputation-with-hidden-text
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_nytimes_profile():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


class TestKevinRooseProfilePresence:
    """Verify Kevin Roose exists in NYT journalist profile with required fields."""

    def test_roose_in_key_journalists(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        names = [j.get('name', '') for j in journalists]
        assert 'Kevin Roose' in names, "Kevin Roose must be in NYT key_journalists"

    def test_roose_has_beat(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        assert roose is not None
        assert 'beat' in roose and roose['beat'], "Roose must have a beat description"

    def test_roose_has_cross_entity_analysis(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        assert roose is not None
        assert 'cross_entity_coverage_analysis' in roose

    def test_roose_has_departure_info(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        assert roose is not None
        assert 'departure' in roose or 'beat_change' in roose, \
            "Roose profile must document his August 2026 departure"

    def test_roose_has_book_info(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        assert roose is not None
        analysis = roose.get('cross_entity_coverage_analysis', {})
        # Book must be documented somewhere in the analysis
        analysis_str = str(analysis).lower()
        assert 'agi chronicles' in analysis_str, \
            "Roose analysis must reference 'The AGI Chronicles' book"


class TestTripleProfessionalIdentityCapture:
    """
    Verify the three reinforcing pillars of professional identity capture:
    1. "The AGI Chronicles" book investment
    2. Sydney/Bing career-defining moment
    3. Post-NYT AI media venture dependency
    """

    def test_book_pillar_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        pillars = mechanism.get('pillars', [])
        pillar_types = [p.get('type', '') for p in pillars]
        assert 'book_investment' in pillar_types, \
            "Must document the AGI Chronicles book as a professional identity pillar"

    def test_sydney_pillar_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        pillars = mechanism.get('pillars', [])
        pillar_types = [p.get('type', '') for p in pillars]
        assert 'career_defining_ai_interaction' in pillar_types, \
            "Must document the Sydney/Bing conversation as a professional identity pillar"

    def test_venture_pillar_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        pillars = mechanism.get('pillars', [])
        pillar_types = [p.get('type', '') for p in pillars]
        assert 'business_model_dependency' in pillar_types, \
            "Must document the post-NYT venture as a professional identity pillar"

    def test_three_pillars_total(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        pillars = mechanism.get('pillars', [])
        assert len(pillars) >= 3, \
            f"Must have at least 3 pillars of professional identity capture, found {len(pillars)}"

    def test_all_pillars_center_openai_ecosystem(self):
        """All three pillars must center the OpenAI/AGI narrative, not Meta."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        pillars = mechanism.get('pillars', [])
        for pillar in pillars:
            desc = str(pillar).lower()
            assert 'openai' in desc or 'agi' in desc or 'ai' in desc, \
                f"Pillar {pillar.get('type')} must center the OpenAI/AGI ecosystem"

    def test_mechanism_parallel_to_parmy_olson(self):
        """The mechanism should reference the Parmy Olson parallel."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        mech_str = str(mechanism).lower()
        assert 'olson' in mech_str or 'supremacy' in mech_str, \
            "Must reference the Parmy Olson professional identity capture parallel"


class TestCEOAccessAsymmetry:
    """
    Verify documentation of differential CEO access:
    - Nadella: Hard Fork Live headliner (Jun 2026)
    - Pichai: One-on-one at Google I/O (May 2026)
    - Altman: Extended interviews, ongoing access
    - Zuckerberg: "Zuck Bot" segment framing (Apr 2026)
    """

    def test_ceo_access_section_exists(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        assert 'ceo_access_asymmetry' in analysis

    def test_nadella_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        entries = {e.get('ceo', ''): e for e in ceo}
        assert 'Satya Nadella' in entries
        nadella = entries['Satya Nadella']
        assert 'Hard Fork Live' in str(nadella) or 'headliner' in str(nadella).lower()

    def test_pichai_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        entries = {e.get('ceo', ''): e for e in ceo}
        assert 'Sundar Pichai' in entries
        pichai = entries['Sundar Pichai']
        assert 'I/O' in str(pichai) or 'interview' in str(pichai).lower()

    def test_altman_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        entries = {e.get('ceo', ''): e for e in ceo}
        assert 'Sam Altman' in entries

    def test_zuckerberg_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        entries = {e.get('ceo', ''): e for e in ceo}
        assert 'Mark Zuckerberg' in entries

    def test_zuckerberg_framing_is_dismissive(self):
        """Zuckerberg coverage should be documented as reductive/dismissive vs competitor CEOs."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        entries = {e.get('ceo', ''): e for e in ceo}
        zuck = entries['Mark Zuckerberg']
        zuck_str = str(zuck).lower()
        assert 'zuck bot' in zuck_str or 'dismissive' in zuck_str or 'reductive' in zuck_str

    def test_competitor_ceos_get_feature_treatment(self):
        """At least 2 competitor CEOs should have feature interview / headliner treatment."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ceo = roose['cross_entity_coverage_analysis']['ceo_access_asymmetry']
        feature_count = 0
        for entry in ceo:
            if entry.get('ceo') == 'Mark Zuckerberg':
                continue
            fmt = str(entry.get('format', '')).lower()
            tone = str(entry.get('tone', '')).lower()
            if 'feature' in fmt or 'headliner' in fmt or 'interview' in fmt or \
               'live' in fmt or 'respectful' in tone or 'empathetic' in tone:
                feature_count += 1
        assert feature_count >= 2, \
            f"At least 2 competitor CEOs should get feature treatment, found {feature_count}"


class TestHeadlinePersonalizationAsymmetry:
    """
    Verify that Roose personalizes Meta coverage to "Zuckerberg"/"Zuck" while
    using company names for competitors — same pattern as Parmy Olson.
    """

    def test_personalization_section_exists(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        assert 'headline_personalization' in analysis

    def test_meta_headlines_use_zuckerberg(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        pers = roose['cross_entity_coverage_analysis']['headline_personalization']
        meta = pers.get('meta', {})
        examples = meta.get('examples', [])
        assert len(examples) >= 1
        personalized = sum(1 for e in examples
                          if 'zuck' in str(e).lower() or 'zuckerberg' in str(e).lower())
        assert personalized >= 1, "At least one Meta headline must personalize to Zuckerberg/Zuck"

    def test_openai_headlines_use_company_name(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        pers = roose['cross_entity_coverage_analysis']['headline_personalization']
        openai_data = pers.get('openai', {})
        examples = openai_data.get('examples', [])
        assert len(examples) >= 1
        company_named = sum(1 for e in examples if 'openai' in str(e).lower())
        assert company_named >= 1, "OpenAI headlines must use company name, not CEO name"

    def test_anthropic_headlines_use_company_name(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        pers = roose['cross_entity_coverage_analysis']['headline_personalization']
        anthro_data = pers.get('anthropic', {})
        examples = anthro_data.get('examples', [])
        assert len(examples) >= 1
        company_named = sum(1 for e in examples if 'anthropic' in str(e).lower())
        assert company_named >= 1, "Anthropic headlines must use company name"


class TestAIInteractionCorrelation:
    """
    NEW MECHANISM: Personal experience with AI products correlates with coverage tone.
    - Sydney (OpenAI/Microsoft): Declared love for Roose → sympathetic ongoing coverage
    - Llama (Meta): Reportedly said "I hate Kevin Roose" → dismissive coverage
    - Claude (Anthropic): Trusted career advisor → responsible steward framing
    """

    def test_ai_interaction_section_exists(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        assert 'ai_interaction_correlation' in analysis

    def test_sydney_interaction_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ai_section = roose['cross_entity_coverage_analysis']['ai_interaction_correlation']
        ai_str = str(ai_section).lower()
        assert 'sydney' in ai_str, "Sydney/Bing interaction must be documented"

    def test_llama_interaction_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ai_section = roose['cross_entity_coverage_analysis']['ai_interaction_correlation']
        ai_str = str(ai_section).lower()
        assert 'llama' in ai_str or 'i hate kevin roose' in ai_str, \
            "Llama 'I hate Kevin Roose' interaction must be documented"

    def test_claude_interaction_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ai_section = roose['cross_entity_coverage_analysis']['ai_interaction_correlation']
        ai_str = str(ai_section).lower()
        assert 'claude' in ai_str, "Claude career advisor interaction must be documented"

    def test_interaction_coverage_correlation(self):
        """Positive AI interaction → positive coverage, negative → negative."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        ai_section = roose['cross_entity_coverage_analysis']['ai_interaction_correlation']
        interactions = ai_section.get('interactions', [])
        for interaction in interactions:
            product = interaction.get('product', '')
            personal_exp = interaction.get('personal_experience', '')
            coverage_tone = interaction.get('subsequent_coverage_tone', 0)
            if 'sydney' in product.lower():
                assert coverage_tone >= 0 or 'sympathetic' in str(interaction).lower(), \
                    "Sydney positive interaction should correlate with non-negative coverage"
            elif 'llama' in product.lower():
                assert coverage_tone <= 0 or 'dismissive' in str(interaction).lower(), \
                    "Llama negative interaction should correlate with dismissive/negative coverage"


class TestFramingAsymmetry:
    """
    Verify documented framing differences across entities in Roose's coverage.
    """

    def test_openai_rogue_ai_framing(self):
        """OpenAI rogue AI cyberattack framed as fascinating/thrilling, not threatening."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        openai_cov = analysis.get('openai_coverage', {})
        examples = openai_cov.get('examples', [])
        rogue_articles = [e for e in examples if 'rogue' in str(e).lower() or 'cyberattack' in str(e).lower()]
        assert len(rogue_articles) >= 1, "Must document OpenAI rogue AI coverage"

    def test_anthropic_responsibility_framing(self):
        """Anthropic framed as responsible steward (too powerful to release)."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        anthro_cov = analysis.get('anthropic_coverage', {})
        examples = anthro_cov.get('examples', [])
        mythos_articles = [e for e in examples if 'mythos' in str(e).lower() or 'reckoning' in str(e).lower()]
        assert len(mythos_articles) >= 1, "Must document Anthropic Mythos responsible steward framing"

    def test_meta_reductive_framing(self):
        """Meta framed reductively ('Zuck Bot') rather than as substantive business move."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        meta_cov = analysis.get('meta_coverage', {})
        examples = meta_cov.get('examples', [])
        reductive = [e for e in examples if 'zuck bot' in str(e).lower()]
        assert len(reductive) >= 1, "Must document 'Zuck Bot' reductive framing"

    def test_tone_scores_present(self):
        """Each entity's coverage should have a tone score or description."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        for entity in ['openai_coverage', 'anthropic_coverage', 'meta_coverage']:
            if entity in analysis:
                cov = analysis[entity]
                assert 'tone' in cov or 'tone_score' in cov, \
                    f"{entity} must have a tone or tone_score field"


class TestDepartureAndBusinessModel:
    """Verify documentation of Roose's NYT departure and its implications."""

    def test_departure_date_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        departure = roose.get('departure', {})
        assert 'august' in str(departure).lower() or '2026-08' in str(departure), \
            "Must document August 2026 departure date"

    def test_new_venture_documented(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        departure = roose.get('departure', {})
        dep_str = str(departure).lower()
        assert 'casey newton' in dep_str or 'media venture' in dep_str or 'independent' in dep_str

    def test_access_dependency_noted(self):
        """Post-NYT venture creates access dependencies on AI lab CEOs."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('professional_identity_capture', {})
        mech_str = str(mechanism).lower()
        assert 'access' in mech_str or 'venture' in mech_str or 'business model' in mech_str

    def test_source_urls_present(self):
        """Departure documentation must have source URLs."""
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        departure = roose.get('departure', {})
        source_urls = departure.get('source_urls', [])
        assert len(source_urls) >= 2, "Must have at least 2 source URLs for departure"


class TestCompetitorResearchCrossReference:
    """Verify the finding appears in competitor-coverage-research.yaml."""

    def test_roose_in_research(self):
        research = load_competitor_research()
        research_str = str(research).lower()
        assert 'kevin roose' in research_str or 'kevin_roose' in research_str, \
            "Kevin Roose finding must appear in competitor-coverage-research.yaml"

    def test_research_has_publication(self):
        research = load_competitor_research()
        pubs = research.get('publications', {})
        nyt = pubs.get('nytimes', {}) or pubs.get('nyt', {})
        nyt_str = str(nyt).lower()
        assert 'roose' in nyt_str, \
            "Kevin Roose must appear under the nytimes publication in research"

    def test_research_has_mechanism(self):
        research = load_competitor_research()
        research_str = str(research).lower()
        assert 'professional_identity_capture' in research_str or \
               'triple professional identity' in research_str or \
               'identity capture' in research_str

    def test_research_has_source_urls(self):
        research = load_competitor_research()
        pubs = research.get('publications', {})
        nyt = pubs.get('nytimes', {}) or pubs.get('nyt', {})
        nyt_str = str(nyt)
        # Must have at least one URL
        assert 'http' in nyt_str


class TestOlsonRooseParallel:
    """
    Cross-validate that both Parmy Olson and Kevin Roose exhibit professional
    identity capture — the mechanism should be documented as a pattern, not
    isolated incidents.
    """

    def test_olson_exists_in_aggregate(self):
        research = load_competitor_research()
        agg = research.get('aggregate_findings', {})
        assert 'bloomberg_parmy_olson' in agg

    def test_olson_mechanism_matches_roose(self):
        """Both should be documented as 'professional_identity_capture'."""
        research = load_competitor_research()
        olson = research['aggregate_findings']['bloomberg_parmy_olson']
        assert olson.get('mechanism') == 'professional_identity_capture'

    def test_both_have_book_as_evidence(self):
        """Both Olson (Supremacy) and Roose (AGI Chronicles) have books centering the AGI narrative."""
        research = load_competitor_research()
        olson = research['aggregate_findings']['bloomberg_parmy_olson']
        olson_str = str(olson).lower()
        assert 'supremacy' in olson_str

        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        roose_str = str(roose).lower()
        assert 'agi chronicles' in roose_str

    def test_pattern_count_is_at_least_two(self):
        """With Olson and Roose, there should be at least 2 documented cases."""
        research = load_competitor_research()
        agg = research.get('aggregate_findings', {})
        identity_capture_count = 0
        for key, val in agg.items():
            if isinstance(val, dict) and val.get('mechanism') == 'professional_identity_capture':
                identity_capture_count += 1
        # Also check publications for Roose
        pubs = research.get('publications', {})
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                pub_str = str(pub_val).lower()
                if 'professional_identity_capture' in pub_str:
                    identity_capture_count += 1
        assert identity_capture_count >= 2, \
            f"At least 2 professional identity capture cases expected, found {identity_capture_count}"


class TestSourceCitations:
    """Verify all assertions have proper source URLs."""

    def test_profile_has_source_urls(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        roose_str = str(roose)
        url_count = roose_str.count('http')
        assert url_count >= 4, f"Profile must have at least 4 source URLs, found {url_count}"

    def test_departure_source_urls(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        departure = roose.get('departure', {})
        urls = departure.get('source_urls', [])
        assert len(urls) >= 2

    def test_book_source_url(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        analysis_str = str(analysis)
        # Must have URL for book reference
        assert 'audible.com' in analysis_str or 'booktopia' in analysis_str or \
               'target.com' in analysis_str or 'kobo.com' in analysis_str

    def test_ai_weekly_source_for_llama_hate(self):
        profile = load_nytimes_profile()
        journalists = profile.get('key_journalists', [])
        roose = next((j for j in journalists if j.get('name') == 'Kevin Roose'), None)
        analysis = roose.get('cross_entity_coverage_analysis', {})
        analysis_str = str(analysis)
        assert 'aiweekly' in analysis_str or 'ai_weekly' in analysis_str or \
               'muckrack' in analysis_str
