"""
Cross-entity coverage analysis: Jeff Horwitz (Reuters, previously WSJ)

Mechanism #18 — Triple-Deal Narrative Lock-In: The same investigative journalist
applies maximum-depth investigation techniques (internal documents, undercover
experiments, whistleblower cultivation) exclusively to Meta, while covering
competitors with surface-level factual reporting. The asymmetry direction aligns
with compounding personal financial/reputational incentives:

1. Book Deal: "Broken Code: Inside Facebook and the Fight to Expose Its Toxic
   Secrets" (Doubleday, Nov 2023) — ongoing royalties tied to Meta-as-villain narrative
2. Movie Deal: "The Social Reckoning" (Sony/Columbia, Oct 9, 2026) — Jeremy Allen
   White plays Horwitz as heroic journalist protagonist
3. Pulitzer Prize: 2026 Beat Reporting, won specifically for "Meta investigations"
   at Reuters — professional identity locked to Meta as the target

Key finding: INVESTIGATIVE TECHNIQUE EXCLUSIVITY — internal documents, undercover
experiments (fake 14-year-old accounts, purchasing scam ads), and whistleblower
cultivation are applied ONLY to Meta. Competitor coverage uses wire-service neutral
reporting exclusively. The same reporter who creates fake accounts on Meta to test
safeguards has never created fake accounts on YouTube, TikTok, or Snap to test
comparable safeguards — despite LA trial finding YouTube liable for the SAME child
safety violations ($1.8M, 7 counts).

Sources:
- WSJ: Facebook Files series (2021) — 20K+ internal documents
- Reuters: Meta scam ads series (2025-2026) — undercover ad purchase experiment
- Reuters: Meta AI chatbots and children (2025-2026) — fake 14-year-old account
- Reuters: Instagram eating disorders (2026) — internal Meta documents
- Reuters: UK AISI rogue AI findings (Aug 4, 2026) — neutral wire report on OpenAI/Anthropic
- Book: "Broken Code" (Doubleday, Nov 2023)
- Film: "The Social Reckoning" (Sony/Columbia, dir. Aaron Sorkin, Oct 9, 2026)
- Pulitzer: 2026 Beat Reporting (Reuters, Meta investigations)
- LA Trial: Meta $4.2M + YouTube $1.8M, 7 counts each (2026)

Date analyzed: 2026-08-10
"""

import unittest
import yaml
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def get_horwitz():
    """Extract the reuters_jeff_horwitz section from aggregate_findings in competitor-coverage-research.yaml."""
    data = load_competitor_research()
    return data.get('aggregate_findings', {}).get('reuters_jeff_horwitz')


# ---------------------------------------------------------------------------
# Test Class 1: Basic Profile
# ---------------------------------------------------------------------------
class TestJeffHorwitzBasicProfile(unittest.TestCase):
    """Verify Horwitz profile exists with required fields."""

    def test_profile_exists(self):
        horwitz = get_horwitz()
        self.assertIsNotNone(horwitz, "jeff_horwitz must exist in competitor-coverage-research.yaml")

    def test_name(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['name'], 'Jeff Horwitz')

    def test_current_publication_reuters(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['current_publication'], 'Reuters')

    def test_previous_publication_wsj(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['previous_publication'], 'Wall Street Journal')

    def test_beat_includes_investigations(self):
        horwitz = get_horwitz()
        beat = horwitz['beat'].lower()
        self.assertTrue('investigation' in beat or 'accountability' in beat,
                        f"Beat '{horwitz['beat']}' should reference investigations")

    def test_career_trajectory_wsj_to_reuters(self):
        """Career trajectory should show WSJ -> Reuters migration."""
        horwitz = get_horwitz()
        trajectory = horwitz['career_trajectory']
        outlets = [entry['outlet'] for entry in trajectory]
        self.assertIn('Wall Street Journal', outlets)
        self.assertIn('Reuters', outlets)
        wsj_idx = outlets.index('Wall Street Journal')
        reuters_idx = outlets.index('Reuters')
        self.assertLess(wsj_idx, reuters_idx, "WSJ should precede Reuters in career trajectory")

    def test_has_cross_entity_coverage_analysis(self):
        horwitz = get_horwitz()
        self.assertIn('cross_entity_coverage_analysis', horwitz)

    def test_date_analyzed(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['date_analyzed'], '2026-08-10')


# ---------------------------------------------------------------------------
# Test Class 2: Triple-Deal Narrative Lock-In (Mechanism #18)
# ---------------------------------------------------------------------------
class TestTripleDealNarrativeLockIn(unittest.TestCase):
    """Verify mechanism #19 is fully documented with all three deal types."""

    def test_mechanism_id_is_19(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['mechanism_id'], 19)

    def test_mechanism_name(self):
        horwitz = get_horwitz()
        self.assertEqual(horwitz['mechanism_name'], 'triple_deal_narrative_lock_in')

    def test_mechanism_description_present(self):
        horwitz = get_horwitz()
        desc = horwitz['mechanism_description'].lower()
        self.assertIn('internal documents', desc)
        self.assertIn('undercover', desc)
        self.assertIn('meta', desc)

    def test_triple_deal_structure_has_three_deals(self):
        horwitz = get_horwitz()
        deals = horwitz['triple_deal_structure']
        self.assertIn('book_deal', deals)
        self.assertIn('movie_deal', deals)
        self.assertIn('pulitzer_prize', deals)

    def test_all_three_deals_have_incentive_field(self):
        horwitz = get_horwitz()
        deals = horwitz['triple_deal_structure']
        for deal_key in ['book_deal', 'movie_deal', 'pulitzer_prize']:
            self.assertIn('incentive', deals[deal_key],
                          f"{deal_key} missing 'incentive' field")
            self.assertTrue(len(deals[deal_key]['incentive']) > 50,
                            f"{deal_key} incentive should be substantive")

    def test_compounding_pattern_documented(self):
        """Triple deal compounding pattern should be in cross_entity_patterns."""
        horwitz = get_horwitz()
        patterns = horwitz['cross_entity_coverage_analysis']['cross_entity_patterns']
        names = [p['pattern_name'] for p in patterns]
        self.assertIn('TRIPLE DEAL COMPOUNDING', names)


# ---------------------------------------------------------------------------
# Test Class 3: Book Deal Incentive Structure
# ---------------------------------------------------------------------------
class TestBookDealIncentiveStructure(unittest.TestCase):
    """Verify 'Broken Code' book deal specifics."""

    def test_book_title(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        self.assertIn('Broken Code', book['title'])

    def test_book_publisher_doubleday(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        self.assertEqual(book['publisher'], 'Doubleday')

    def test_book_publication_date(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        self.assertEqual(book['publication_date'], '2023-11')

    def test_book_incentive_mentions_royalties(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        self.assertIn('royalt', book['incentive'].lower())

    def test_book_incentive_mentions_meta_villain_narrative(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        incentive = book['incentive'].lower()
        self.assertTrue('meta' in incentive and 'villain' in incentive,
                        "Book incentive should reference Meta-as-villain narrative")

    def test_book_has_source_url(self):
        horwitz = get_horwitz()
        book = horwitz['triple_deal_structure']['book_deal']
        self.assertIn('source_url', book)
        self.assertTrue(book['source_url'].startswith('http'))


# ---------------------------------------------------------------------------
# Test Class 4: Movie Deal Incentive Structure
# ---------------------------------------------------------------------------
class TestMovieDealIncentiveStructure(unittest.TestCase):
    """Verify 'The Social Reckoning' movie details."""

    def test_movie_title(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertEqual(movie['title'], 'The Social Reckoning')

    def test_movie_studio(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertIn('Sony', movie['studio'])

    def test_movie_director_sorkin(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertEqual(movie['director'], 'Aaron Sorkin')

    def test_movie_actor_jeremy_allen_white(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertEqual(movie['actor_playing_horwitz'], 'Jeremy Allen White')

    def test_movie_release_date_oct_2026(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertEqual(movie['release_date'], '2026-10-09')

    def test_movie_release_timing_incentive(self):
        """Release timing should note maximum incentive during months before release."""
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        incentive = movie['incentive'].lower()
        self.assertTrue('october' in incentive or 'release' in incentive)
        self.assertIn('dramatic arc', incentive)

    def test_movie_has_source_url(self):
        horwitz = get_horwitz()
        movie = horwitz['triple_deal_structure']['movie_deal']
        self.assertIn('source_url', movie)
        self.assertTrue(movie['source_url'].startswith('http'))


# ---------------------------------------------------------------------------
# Test Class 5: Pulitzer Coverage Identity
# ---------------------------------------------------------------------------
class TestPulitzerCoverageIdentity(unittest.TestCase):
    """Verify Pulitzer citation specifically for Meta investigations."""

    def test_pulitzer_category(self):
        horwitz = get_horwitz()
        pulitzer = horwitz['triple_deal_structure']['pulitzer_prize']
        self.assertEqual(pulitzer['category'], 'Beat Reporting')

    def test_pulitzer_year_2026(self):
        horwitz = get_horwitz()
        pulitzer = horwitz['triple_deal_structure']['pulitzer_prize']
        self.assertEqual(pulitzer['year'], 2026)

    def test_pulitzer_citation_meta_focus(self):
        horwitz = get_horwitz()
        pulitzer = horwitz['triple_deal_structure']['pulitzer_prize']
        self.assertIn('Meta', pulitzer['citation_focus'])

    def test_pulitzer_incentive_professional_identity(self):
        """Pulitzer should lock professional identity to Meta as target."""
        horwitz = get_horwitz()
        pulitzer = horwitz['triple_deal_structure']['pulitzer_prize']
        incentive = pulitzer['incentive'].lower()
        self.assertTrue('professional identity' in incentive or 'locked' in incentive,
                        "Pulitzer incentive should reference professional identity lock-in")

    def test_pulitzer_has_source_url(self):
        horwitz = get_horwitz()
        pulitzer = horwitz['triple_deal_structure']['pulitzer_prize']
        self.assertIn('source_url', pulitzer)
        self.assertTrue(pulitzer['source_url'].startswith('http'))


# ---------------------------------------------------------------------------
# Test Class 6: Investigative Depth Asymmetry
# ---------------------------------------------------------------------------
class TestInvestigativeDepthAsymmetry(unittest.TestCase):
    """Internal documents, undercover experiments, whistleblower cultivation applied only to Meta."""

    def test_meta_tone_strongly_negative(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        self.assertLessEqual(meta['tone'], -0.60,
                             f"Meta tone {meta['tone']} should be strongly negative (<= -0.60)")

    def test_meta_register_adversarial(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        self.assertIn('adversarial', meta['register'].lower())

    def test_meta_investigative_depth_maximum(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        self.assertEqual(meta['investigative_depth'], 'maximum')

    def test_meta_internal_documents_used(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        techniques = meta['techniques_applied']
        internal_docs = [t for t in techniques if t.get('internal_documents')]
        self.assertTrue(len(internal_docs) >= 1, "Must have internal documents technique")

    def test_meta_undercover_experiments_used(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        techniques = meta['techniques_applied']
        undercover = [t for t in techniques if t.get('undercover_experiments')]
        self.assertTrue(len(undercover) >= 1, "Must have undercover experiments technique")

    def test_meta_whistleblower_cultivation_used(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        techniques = meta['techniques_applied']
        whistleblowers = [t for t in techniques if t.get('whistleblower_cultivation')]
        self.assertTrue(len(whistleblowers) >= 1, "Must have whistleblower cultivation technique")

    def test_meta_has_at_least_four_articles(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        self.assertGreaterEqual(len(meta['recent_articles']), 4,
                                "Meta coverage should have at least 4 articles documented")

    def test_meta_loaded_language_documented(self):
        horwitz = get_horwitz()
        meta = horwitz['cross_entity_coverage_analysis']['meta_coverage']
        loaded = meta['loaded_language']
        self.assertGreaterEqual(len(loaded), 3, "Should document at least 3 loaded language examples")
        # Check for key phrases
        loaded_lower = [w.lower() for w in loaded]
        self.assertTrue(any('toxic' in w for w in loaded_lower),
                        "'toxic' family phrase should be in loaded language")

    def test_investigative_depth_ratio_documented(self):
        horwitz = get_horwitz()
        ratio = horwitz['cross_entity_coverage_analysis']['investigative_depth_ratio']
        self.assertIn('maximum', ratio['meta'].lower())
        self.assertIn('surface', ratio['openai'].lower())
        self.assertIn('absent', ratio['google_youtube'].lower())


# ---------------------------------------------------------------------------
# Test Class 7: Competitor Coverage Absence
# ---------------------------------------------------------------------------
class TestCompetitorCoverageAbsence(unittest.TestCase):
    """No comparable investigative depth for Google/YouTube/Apple/OpenAI."""

    def test_openai_tone_near_neutral(self):
        horwitz = get_horwitz()
        openai = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['openai']
        self.assertGreaterEqual(openai['tone'], -0.20,
                                f"OpenAI tone {openai['tone']} should be near-neutral")

    def test_openai_register_factual(self):
        horwitz = get_horwitz()
        openai = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['openai']
        self.assertIn('neutral', openai['register'].lower())

    def test_openai_investigative_depth_surface(self):
        horwitz = get_horwitz()
        openai = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['openai']
        self.assertEqual(openai['investigative_depth'], 'surface')

    def test_openai_no_internal_documents(self):
        horwitz = get_horwitz()
        openai = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['openai']
        techniques = openai['techniques_applied']
        internal_docs = [t for t in techniques if t.get('internal_documents')]
        self.assertEqual(len(internal_docs), 0, "OpenAI coverage should have NO internal documents")

    def test_openai_no_undercover_experiments(self):
        horwitz = get_horwitz()
        openai = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['openai']
        techniques = openai['techniques_applied']
        undercover = [t for t in techniques if t.get('undercover_experiments')]
        self.assertEqual(len(undercover), 0, "OpenAI coverage should have NO undercover experiments")

    def test_google_youtube_investigative_depth_none(self):
        horwitz = get_horwitz()
        yt = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['google_youtube']
        self.assertEqual(yt['investigative_depth'], 'none')

    def test_google_youtube_zero_articles(self):
        horwitz = get_horwitz()
        yt = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['google_youtube']
        self.assertEqual(len(yt['recent_articles']), 0,
                         "Google/YouTube should have ZERO investigative articles")

    def test_google_youtube_notable_absence_documented(self):
        """LA trial gap must be documented as notable absence."""
        horwitz = get_horwitz()
        yt = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['google_youtube']
        absence = yt['notable_absence'].lower()
        self.assertIn('la trial', absence.lower().replace('la ', 'la '),
                      "Notable absence should reference LA trial")
        self.assertIn('youtube', absence)

    def test_apple_investigative_depth_none(self):
        horwitz = get_horwitz()
        apple = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['apple']
        self.assertEqual(apple['investigative_depth'], 'none')

    def test_snap_tiktok_investigative_depth_none(self):
        horwitz = get_horwitz()
        snap = horwitz['cross_entity_coverage_analysis']['competitor_coverage']['snap_tiktok']
        self.assertEqual(snap['investigative_depth'], 'none')

    def test_tone_gap_meta_vs_openai(self):
        """Gap between Meta tone and OpenAI tone should be >= 0.50."""
        horwitz = get_horwitz()
        cea = horwitz['cross_entity_coverage_analysis']
        meta_tone = cea['meta_coverage']['tone']
        openai_tone = cea['competitor_coverage']['openai']['tone']
        gap = openai_tone - meta_tone
        self.assertGreaterEqual(gap, 0.50,
                                f"Tone gap {gap} should be >= 0.50 (Meta adversarial vs OpenAI neutral)")

    def test_asymmetry_score_high(self):
        horwitz = get_horwitz()
        score = horwitz['cross_entity_coverage_analysis']['asymmetry_score']
        self.assertGreaterEqual(score, 0.70,
                                f"Asymmetry score {score} should be >= 0.70")


# ---------------------------------------------------------------------------
# Test Class 8: Legitimate Factors
# ---------------------------------------------------------------------------
class TestLegitimateFactors(unittest.TestCase):
    """Document the legitimate reasons that partially explain the asymmetry."""

    def test_legitimate_factors_exist(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        self.assertGreaterEqual(len(factors), 5,
                                "Should document at least 5 legitimate factors")

    def test_frances_haugen_access_documented(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'].lower() for f in factors]
        self.assertTrue(any('haugen' in f for f in factor_names),
                        "Frances Haugen access should be documented as legitimate factor")

    def test_leaked_documents_documented(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'].lower() for f in factors]
        self.assertTrue(any('leak' in f or 'document' in f for f in factor_names),
                        "Leaked documents availability should be documented")

    def test_specialization_documented(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'].lower() for f in factors]
        self.assertTrue(any('specializ' in f for f in factor_names),
                        "Journalist specialization should be documented")

    def test_facebook_files_predated_deals(self):
        """Facebook Files (2021) predated book deal (2023) and movie deal."""
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'].lower() for f in factors]
        self.assertTrue(any('predate' in f for f in factor_names),
                        "Should document that Facebook Files predated deals")

    def test_reuters_editorial_independence_documented(self):
        """Reuters has no content licensing deals — unlike Condé Nast/PMC."""
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        factor_names = [f['factor'].lower() for f in factors]
        self.assertTrue(any('reuters' in f for f in factor_names),
                        "Reuters editorial independence should be documented")

    def test_each_factor_has_weight(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        for factor in factors:
            self.assertIn('weight', factor,
                          f"Factor '{factor['factor']}' missing weight field")
            self.assertIn(factor['weight'], ['low', 'medium', 'high'],
                          f"Factor weight should be low/medium/high, got '{factor['weight']}'")

    def test_each_factor_has_description(self):
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        for factor in factors:
            self.assertIn('description', factor,
                          f"Factor '{factor['factor']}' missing description")
            self.assertTrue(len(factor['description']) > 20,
                            f"Factor '{factor['factor']}' description too short")

    def test_high_weight_factors_count(self):
        """At least 3 factors should be high weight (strong legitimate explanations)."""
        horwitz = get_horwitz()
        factors = horwitz['cross_entity_coverage_analysis']['legitimate_factors']
        high_weight = [f for f in factors if f['weight'] == 'high']
        self.assertGreaterEqual(len(high_weight), 3,
                                "At least 3 factors should be high weight")

    def test_asymmetry_note_acknowledges_valid_reporting(self):
        """The asymmetry note should acknowledge Horwitz's Meta reporting IS valid."""
        horwitz = get_horwitz()
        note = horwitz['cross_entity_coverage_analysis']['asymmetry_note'].lower()
        self.assertTrue("isn't" in note or 'not' in note or 'valid' in note,
                        "Asymmetry note should acknowledge the reporting validity")


if __name__ == '__main__':
    unittest.main()
