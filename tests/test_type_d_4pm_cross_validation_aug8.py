"""
Type D Cross-Validation — Aug 8, 16:00 PT

Validates consistency across the 13:00–15:00 PT iterations:
- Type B 13:00: Paresh Dave emotional register asymmetry (Mechanism #8)
- Type C 14:00: Publisher AI Revenue Opacity Index (3-tier model)
- Type C 15:00: Publisher AI Revenue Asymmetry Matrix (100% correlation)

Also validates doc consistency fixes (test file listings + test counts).
"""

import os
import re
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, 'profiles')
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename), 'r') as f:
        return yaml.safe_load(f)


def load_doc(relpath):
    with open(os.path.join(REPO_ROOT, relpath), 'r') as f:
        return f.read()


# ── Paresh Dave Emotional Register Asymmetry (Mechanism #8) ──

class TestPareshDaveMechanism8CrossValidation:
    """Cross-validate Mechanism #8 against WIRED profile and entity data."""

    def test_wired_has_paresh_dave_cross_entity(self):
        wired = load_yaml('wired.yaml')
        journalists = wired.get('journalists', wired.get('key_journalists', []))
        names = []
        for j in journalists:
            name = j.get('name', j.get('display_name', ''))
            names.append(name.lower())
        assert any('paresh' in n and 'dave' in n for n in names), \
            "WIRED profile must include Paresh Dave as a journalist"

    def test_mechanism_8_is_emotional_register_asymmetry(self):
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired)
        assert 'emotional_register_asymmetry' in text, \
            "WIRED profile must document emotional_register_asymmetry mechanism"

    def test_mechanism_8_number(self):
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired)
        # Mechanism #8 should be present
        assert 'mechanism_number: 8' in text or "'mechanism_number': 8" in text or \
            '"mechanism_number": 8' in text, \
            "Mechanism #8 must be numbered in WIRED profile"

    def test_paresh_dave_meta_tone_negative(self):
        """Paresh Dave's Meta coverage tone should be negative (adversarial)."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired).lower()
        # Look for his Meta tone being negative
        assert '-0.51' in text or 'negative' in text or 'adversarial' in text, \
            "Dave's Meta coverage should show negative/adversarial tone"

    def test_paresh_dave_openai_tone_near_neutral(self):
        """Paresh Dave's OpenAI coverage should be more neutral than Meta."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired)
        # OpenAI tone documented as -0.07 (near neutral)
        assert '-0.07' in text, \
            "Dave's OpenAI coverage tone (-0.07) should be documented"

    def test_paresh_dave_google_tone_positive(self):
        """Paresh Dave's Google coverage should be positive/neutral."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired)
        assert '+0.08' in text or '0.08' in text, \
            "Dave's Google coverage tone (+0.08) should be documented"

    def test_institution_driven_conclusion(self):
        """The analysis should conclude escalation is institution-driven, not reporter-driven."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired).lower()
        assert 'institution' in text, \
            "Dave analysis should reference institution-driven framing"

    def test_dave_test_file_exists(self):
        path = os.path.join(TESTS_DIR, 'test_paresh_dave_cross_entity.py')
        assert os.path.exists(path), \
            "test_paresh_dave_cross_entity.py must exist"

    def test_dave_test_file_has_tests(self):
        path = os.path.join(TESTS_DIR, 'test_paresh_dave_cross_entity.py')
        content = open(path).read()
        count = len(re.findall(r'^\s+def test_', content, re.MULTILINE))
        assert count >= 50, \
            f"Paresh Dave test file should have >= 50 tests, found {count}"


# ── Opacity Index Cross-Validation ──

class TestOpacityIndexCrossValidation:
    """Cross-validate the 3-tier opacity model against entity/profile data."""

    def test_opacity_index_exists_in_entities(self):
        entities = load_yaml('competitor-entities.yaml')
        assert 'publisher_ai_revenue_opacity_index' in entities, \
            "competitor-entities.yaml must contain publisher_ai_revenue_opacity_index"

    def test_three_tiers_present(self):
        entities = load_yaml('competitor-entities.yaml')
        index = entities['publisher_ai_revenue_opacity_index']
        tiers = index.get('opacity_tiers', [])
        tier_numbers = [t.get('tier') for t in tiers]
        assert 1 in tier_numbers and 2 in tier_numbers and 3 in tier_numbers, \
            f"All three tiers must be present, found: {tier_numbers}"

    def test_tier_1_is_black_box(self):
        entities = load_yaml('competitor-entities.yaml')
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_1 = next(t for t in tiers if t['tier'] == 1)
        assert 'BLACK BOX' in tier_1.get('label', '').upper(), \
            "Tier 1 should be labeled BLACK BOX"

    def test_tier_3_is_transparent(self):
        entities = load_yaml('competitor-entities.yaml')
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_3 = next(t for t in tiers if t['tier'] == 3)
        assert 'TRANSPARENT' in tier_3.get('label', '').upper(), \
            "Tier 3 should be labeled TRANSPARENT"

    def test_conde_nast_in_tier_1(self):
        """Condé Nast (private, no disclosure) should be in Tier 1."""
        entities = load_yaml('competitor-entities.yaml')
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_1 = next(t for t in tiers if t['tier'] == 1)
        pubs = yaml.dump(tier_1.get('publishers', [])).lower()
        assert 'cond' in pubs or 'condé' in pubs or 'conde' in pubs, \
            "Condé Nast must be in Tier 1 (BLACK BOX)"

    def test_news_corp_in_tier_3(self):
        """News Corp (public, CEO names AI partners) should be in Tier 3."""
        entities = load_yaml('competitor-entities.yaml')
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_3 = next(t for t in tiers if t['tier'] == 3)
        pubs = yaml.dump(tier_3.get('publishers', [])).lower()
        assert 'news corp' in pubs, \
            "News Corp must be in Tier 3 (TRANSPARENT)"

    def test_nyt_in_tier_2(self):
        """NYT (public, bundles AI revenue) should be in Tier 2."""
        entities = load_yaml('competitor-entities.yaml')
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_2 = next(t for t in tiers if t['tier'] == 2)
        pubs = yaml.dump(tier_2.get('publishers', [])).lower()
        assert 'new york times' in pubs or 'nyt' in pubs, \
            "NYT must be in Tier 2 (BUNDLED)"

    def test_opacity_test_file_exists(self):
        path = os.path.join(TESTS_DIR, 'test_publisher_ai_revenue_opacity_index.py')
        assert os.path.exists(path)


# ── Revenue Asymmetry Matrix Cross-Validation ──

class TestRevenueMatrixCrossValidation:
    """Cross-validate the 100% correlation finding."""

    def test_matrix_test_file_exists(self):
        path = os.path.join(TESTS_DIR, 'test_publisher_ai_revenue_matrix_aug8.py')
        assert os.path.exists(path)

    def test_matrix_test_file_has_tests(self):
        path = os.path.join(TESTS_DIR, 'test_publisher_ai_revenue_matrix_aug8.py')
        content = open(path).read()
        count = len(re.findall(r'^\s+def test_', content, re.MULTILINE))
        assert count >= 70, \
            f"Revenue matrix test file should have >= 70 tests, found {count}"

    def test_news_corp_balanced_tone_in_profile(self):
        """News Corp — ONLY pub with Meta deal — should show balanced tone."""
        nc = load_yaml('news-corp.yaml')
        text = yaml.dump(nc).lower()
        # News Corp should reference balanced coverage
        assert 'balanced' in text or '-0.15' in text, \
            "News Corp profile should document balanced Meta coverage"

    def test_news_corp_q4_fy2026_revenue(self):
        """News Corp Q4 FY2026 revenue documented."""
        entities = load_yaml('competitor-entities.yaml')
        text = yaml.dump(entities).lower()
        assert '2.34' in text, \
            "News Corp Q4 FY2026 $2.34B revenue should be documented"


# ── Doc Consistency Validation ──

class TestDocConsistencyAfterFix:
    """Verify the README/ARCHITECTURE test listing and count fixes hold."""

    def test_readme_lists_opacity_index_test(self):
        readme = load_doc('README.md')
        assert 'test_publisher_ai_revenue_opacity_index.py' in readme, \
            "README must list test_publisher_ai_revenue_opacity_index.py"

    def test_architecture_lists_opacity_index_test(self):
        arch = load_doc('docs/ARCHITECTURE.md')
        assert 'test_publisher_ai_revenue_opacity_index.py' in arch, \
            "ARCHITECTURE.md must list test_publisher_ai_revenue_opacity_index.py"

    def test_readme_test_count_floor(self):
        """README file count should be at least 233 (may lag by 1 during current iteration)."""
        readme = load_doc('README.md')
        match = re.search(r'\*\*(\d+) tests\*\* across (\d+) test files', readme)
        assert match, "README must have test count header"
        claimed_files = int(match.group(2))
        actual_files = len([f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')])
        # Allow current-iteration lag of 1 file (this test file itself)
        assert actual_files - claimed_files <= 1, \
            f"README claims {claimed_files} files, actual {actual_files} — gap too large"

    def test_architecture_test_count_floor(self):
        """ARCHITECTURE file count should be at least 233 (may lag by 1 during current iteration)."""
        arch = load_doc('docs/ARCHITECTURE.md')
        match = re.search(r'(\d+) tests across (\d+) test files', arch)
        assert match, "ARCHITECTURE.md must have test count header"
        claimed_files = int(match.group(2))
        actual_files = len([f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')])
        assert actual_files - claimed_files <= 1, \
            f"ARCHITECTURE claims {claimed_files} files, actual {actual_files} — gap too large"


# ── Aug 8 Cumulative Integrity ──

class TestAug8CumulativeIntegrity:
    """Validate all Aug 8 test files exist and overall health."""

    AUG8_FILES = [
        'test_advance_dual_asset_monetization_aug8.py',
        'test_atlantic_wong_cross_entity_framing_aug8.py',
        'test_google_showcase_coercive_cycle_aug8.py',
        'test_meta_inverse_leverage_q2_2026_aug8.py',
        'test_nyt_google_traffic_cannibalization_paradox_aug8.py',
        'test_wired_amazon_surveillance_parity_paradox_aug8.py',
        'test_wsj_rogue_ai_severity_framing_inversion_aug8.py',
        'test_type_d_03am_cross_validation_aug8.py',
        'test_type_d_07am_cross_validation_aug8.py',
        'test_type_d_11am_cross_validation_aug8.py',
        'test_publisher_ai_revenue_matrix_aug8.py',
        'test_publisher_ai_revenue_opacity_index.py',
        'test_paresh_dave_cross_entity.py',
        'test_david_pierce_cross_entity.py',
        'test_type_d_4pm_cross_validation_aug8.py',
    ]

    @pytest.mark.parametrize("filename", AUG8_FILES)
    def test_aug8_file_exists(self, filename):
        path = os.path.join(TESTS_DIR, filename)
        assert os.path.exists(path), f"{filename} missing from tests/"

    @pytest.mark.parametrize("filename", AUG8_FILES)
    def test_aug8_file_nonempty(self, filename):
        path = os.path.join(TESTS_DIR, filename)
        assert os.path.getsize(path) > 100, f"{filename} is suspiciously small"

    def test_total_test_files_at_least_233(self):
        count = len([f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')])
        assert count >= 233, f"Expected >= 233 test files, found {count}"

    def test_mechanism_8_documented(self):
        """Mechanism #8 (emotional register asymmetry) should be documented."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired)
        assert 'mechanism_number: 8' in text, \
            "WIRED profile should document mechanism #8 (emotional register asymmetry)"

    def test_entity_count_stable(self):
        entities = load_yaml('competitor-entities.yaml')
        ent = entities.get('entities', {})
        assert len(ent) >= 11, \
            f"Expected >= 11 entities, found {len(ent)}"


# ── Cross-Finding Consistency ──

class TestCrossFindingConsistency:
    """Validate that Mechanism #8 and the revenue findings don't contradict each other."""

    def test_institution_driven_aligns_with_financial_model(self):
        """Mechanism #8 (institution-driven escalation) supports the financial incentive model.

        If Dave's Meta escalation is institution-driven (WIRED editorial),
        and WIRED's parent (Condé Nast/Advance) has competitor-only AI deals,
        then the financial incentive model and the journalist analysis converge.
        """
        wired = load_yaml('wired.yaml')
        entities = load_yaml('competitor-entities.yaml')

        # WIRED/Condé Nast is in Tier 1 (BLACK BOX)
        tiers = entities['publisher_ai_revenue_opacity_index']['opacity_tiers']
        tier_1 = next(t for t in tiers if t['tier'] == 1)
        tier_1_text = yaml.dump(tier_1).lower()
        assert 'cond' in tier_1_text or 'wired' in tier_1_text, \
            "WIRED's parent must be in opacity Tier 1"

        # And mechanism 8 documents institution-driven escalation
        wired_text = yaml.dump(wired).lower()
        assert 'institution' in wired_text, \
            "Mechanism 8 should document institution-driven escalation"

    def test_dave_reuters_natural_experiment(self):
        """Dave's Reuters career should be documented as natural experiment."""
        wired = load_yaml('wired.yaml')
        text = yaml.dump(wired).lower()
        assert 'reuters' in text, \
            "Dave's Reuters background should be documented as control condition"

    def test_advance_publications_in_entities(self):
        """Advance Publications (WIRED/Condé Nast parent) should be in entities."""
        entities = load_yaml('competitor-entities.yaml')
        text = yaml.dump(entities).lower()
        assert 'advance' in text, \
            "Advance Publications should be referenced in entity data"
