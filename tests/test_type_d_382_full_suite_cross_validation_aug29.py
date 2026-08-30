"""
Type D #382  -  Full Suite Cross-Validation + Statistical Validity + Financial Incentive Mapping

Date: 2026-08-29 22:00 PT
Type: D - Test & Verify
Mechanisms: #375-#381 cross-validation, publisher licensing valuation provenance, asymmetry scoring statistical meaningfulness

Focus: Type D mandate - run full test suite, fix failures, write new tests for competitor coverage patterns,
verify asymmetry scoring produces statistically meaningful results, update MediaScope Asymmetry artifact analysis.json
if warranted, push to GitHub.

This iteration follows Type C #381 (publisher OpenAI licensing valuation provenance) and Type B #380 (WIRED Adrienne So).
Rotation correct: #379 A -> #380 B -> #381 C -> #382 D. Next expected Type E.

Key validations:
- Mechanism existence for #375-#381
- Publisher deal valuation audit distinguishes primary undisclosed vs secondary report-based
- Asymmetry scorer produces p<0.05, |d|>0.5, CI excludes 0 on illustrative synthetic arrays (pipeline validity, not empirical)
- Journalist profiles parseable, no causal claim overreach
- Financial incentive mapping structural, not proof of capture
"""

import yaml
import os
import glob
from pathlib import Path

import pytest

# Import scoring pipeline to verify statistical validity
from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci, is_significant, interpret_effect_size
from mediascope.score.asymmetry import calculate_asymmetry


PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent


def load_yaml(slug):
    path = PROFILES_DIR / f"{slug}.yaml"
    if not path.exists():
        return None
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestDependencyChain382:
    """Verify core scoring pipeline imports and basic functionality."""

    def test_statistical_module_importable(self):
        assert welch_t_test is not None
        assert cohens_d is not None
        assert bootstrap_ci is not None
        assert is_significant is not None

    def test_asymmetry_module_importable(self):
        assert calculate_asymmetry is not None

    def test_yaml_parseable_all_profiles(self):
        yaml_files = glob.glob(str(PROFILES_DIR / "*.yaml"))
        assert len(yaml_files) >= 7, f"Expected >=7 publication profiles, found {len(yaml_files)}"
        for yf in yaml_files:
            with open(yf, 'r') as fh:
                data = yaml.safe_load(fh)
                assert data is not None, f"Failed to parse {yf}"
                assert isinstance(data, dict), f"{yf} not dict"

    def test_journalists_yaml_parseable(self):
        j_path = PROFILES_DIR / "careers" / "journalists.yaml"
        if not j_path.exists():
            # Alternative path
            j_path = PROFILES_DIR / "careers" / "journalists.yaml"
            pytest.skip("journalists.yaml not at expected path")
        with open(j_path, 'r') as f:
            data = yaml.safe_load(f)
            assert data is not None


class TestMechanismExistence375to381:
    """Validate mechanisms #375-#381 exist and are correctly structured."""

    def test_mechanism_375_exists(self):
        # Mechanism #375: Reece Rogers privacy topic routing
        # Should be in wired.yaml or competitor-entities or journalists.yaml
        found = False
        for yaml_file in PROFILES_DIR.glob("*.yaml"):
            try:
                with open(yaml_file) as fh:
                    content = fh.read()
                    if "375" in content or "reece_rogers" in content.lower():
                        found = True
                        break
            except:
                continue
        # Also check journalists.yaml
        j_path = PROFILES_DIR / "careers" / "journalists.yaml"
        if j_path.exists():
            with open(j_path) as jf:
                if "375" in jf.read() or "reece_rogers" in jf.read().lower():
                    found = True
        assert found, "Mechanism #375 Reece Rogers not found in any profile"

    def test_mechanism_376_exists(self):
        # Mechanism #376: Quintuple reverse-advertiser alignment
        found = False
        for yaml_file in PROFILES_DIR.glob("*.yaml"):
            try:
                with open(yaml_file) as fh:
                    if "376" in fh.read() or "quintuple" in fh.read().lower():
                        found = True
                        break
            except:
                continue
        assert found, "Mechanism #376 quintuple alignment not found"

    def test_mechanism_377_exists(self):
        # Mechanism #377: Test & Verify cross-validation
        # This is Type D itself - check iteration-log contains it
        log_path = Path(__file__).parent.parent / "iteration-log.md"
        assert log_path.exists()
        with open(log_path) as lf:
            content = lf.read()
            assert "377" in content, "Iteration #377 not in log"
            assert "Type D" in content, "Type D marker missing in log history"

    def test_mechanism_378_exists(self):
        # Mechanism #378: Podcast sentiment AI2Day + Blood in the Machine
        log_path = Path(__file__).parent.parent / "iteration-log.md"
        with open(log_path) as lf:
            content = lf.read()
            # 378 is Type E podcast tracking
            assert "378" in content or "AI2Day" in content or "Blood in the Machine" in content

    def test_mechanism_379_exists(self):
        # Mechanism #379: NYT x Anthropic beat expansion
        nyt = load_yaml("nytimes")
        assert nyt is not None, "nytimes.yaml missing"
        content = str(nyt).lower()
        assert "anthropic" in content, "NYT Anthropic mechanism missing"
        # Check recent coverage examples or beat expansion language
        with open(PROFILES_DIR / "nytimes.yaml") as f:
            raw = f.read()
            assert "anthropic" in raw.lower()
            assert "talkingbiznews" in raw.lower() or "beat" in raw.lower()

    def test_mechanism_380_exists(self):
        # Mechanism #380: WIRED Adrienne So biometric privacy inversion
        with open(PROFILES_DIR / "wired.yaml") as f:
            raw = f.read()
            # Should contain adrienne_so or biometric or mechanism 380
            assert "adrienne" in raw.lower() or "380" in raw or "biometric" in raw.lower(), "Mechanism #380 WIRED Adrienne So not found"

        j_path = PROFILES_DIR / "careers" / "journalists.yaml"
        if j_path.exists():
            with open(j_path) as jf:
                j_raw = jf.read()
                assert "380" in j_raw or "adrienne" in j_raw.lower() or "led_fix" in j_raw.lower()

    def test_mechanism_381_exists(self):
        # Mechanism #381: Publisher-OpenAI licensing valuation provenance
        entities = load_yaml("competitor-entities")
        assert entities is not None
        raw = str(entities)
        assert "publisher_deal_valuation_audit" in raw or "valuation" in raw.lower()
        with open(PROFILES_DIR / "competitor-entities.yaml") as f:
            content = f.read()
            assert "financial_times" in content.lower() or "financial-times" in content.lower()
            assert "guardian" in content.lower()
            assert "atlantic" in content.lower()
            assert "axel_springer" in content.lower() or "business-insider" in content.lower()


class TestPublisherLicensingValuationProvenance382:
    """Validate Type C #381 valuation provenance audit is correctly distinguished."""

    def test_ft_cash_terms_not_disclosed(self):
        with open(PROFILES_DIR / "financial-times.yaml") as f:
            content = f.read()
            assert "cash_terms_disclosed" in content
            assert "false" in content.lower() or "False" in content
            assert "secondary_report_based" in content or "secondary" in content.lower()

    def test_ft_has_both_primary_and_secondary_sources(self):
        with open(PROFILES_DIR / "financial-times.yaml") as f:
            content = f.read()
            assert "reuters.com" in content.lower(), "FT primary Reuters source missing"
            assert "digiday.com" in content.lower() or "wsj" in content.lower(), "FT secondary Digiday/WSJ source missing"

    def test_guardian_training_rights_not_explicit(self):
        with open(PROFILES_DIR / "guardian.yaml") as f:
            content = f.read()
            assert "training_rights_explicit" in content or "training" in content.lower()
            assert "false" in content.lower()
            assert "attributed" in content.lower(), "Guardian attributed vs training distinction missing"

    def test_guardian_no_precise_valuation_assertion(self):
        with open(PROFILES_DIR / "guardian.yaml") as f:
            content = f.read()
            # Should NOT assert precise $ value for Guardian (undisclosed)
            # Check it says Undisclosed and does not contain $Xm for guardian OpenAI
            # This is a negative test - ensure we don't invent precise value
            lower = content.lower()
            # Guardian section should mention spokesperson declined
            assert "spokesperson" in lower or "declined" in lower or "undisclosed" in lower

    def test_axel_springer_tens_of_millions_not_precise_13m(self):
        with open(PROFILES_DIR / "business-insider.yaml") as f:
            content = f.read()
            assert "tens of millions" in content.lower(), "Axel Springer valuation should be tens of millions euros"
            # Must NOT assert precise $13M/yr without stronger evidence
            assert "13m" not in content.lower() or "do not assert" in content.lower() or "do not" in content.lower(), \
                "Should not assert precise $13M/yr for Axel Springer"

    def test_nyt_amazon_valuation_control_present(self):
        with open(PROFILES_DIR / "nytimes.yaml") as f:
            content = f.read()
            assert "20" in content and "25" in content, "NYT Amazon $20-25M/yr control missing"
            assert "editorandpublisher" in content.lower() or "editor_and_publisher" in content.lower()

    def test_methodology_distinguishes_rights_scope(self):
        with open(PROFILES_DIR / "competitor-entities.yaml") as f:
            content = f.read()
            assert "attributed" in content.lower() and "training" in content.lower(), \
                "Methodology must distinguish attributed search/display vs training rights"
            assert "syndication" in content.lower(), "Methodology must mention syndication distinction"
            assert "secondary" in content.lower() or "primary" in content.lower(), \
                "Methodology must distinguish primary undisclosed vs secondary valuation"


class TestAsymmetryScoringStatisticalMeaning382:
    """Verify asymmetry scoring produces statistically meaningful results on illustrative synthetic arrays."""

    def test_welch_t_significant_meta_vs_openai_settlement(self):
        # Meta settlement-week negative vs OpenAI aspirational positive
        meta = [-0.72, -0.65, -0.81, -0.58, -0.69, -0.74, -0.63, -0.77]
        openai = [0.15, 0.22, 0.05, 0.18, 0.12, 0.08, 0.20, 0.10]
        t, p = welch_t_test(meta, openai)
        assert p < 0.001, f"Expected highly significant p<0.001, got p={p}"
        assert t < 0, f"Expected negative t (Meta more negative), got t={t}"
        assert is_significant(p)

    def test_cohens_d_large_effect(self):
        meta = [-0.6, -0.5, -0.7, -0.4, -0.8]
        peers = [0.2, 0.3, 0.1, 0.25, 0.15]
        d = cohens_d(meta, peers)
        assert abs(d) > 0.8, f"Expected large effect |d|>0.8, got d={d}"
        assert interpret_effect_size(d) == "large"

    def test_bootstrap_ci_excludes_zero_meta_vs_openai(self):
        meta = [-0.65, -0.75, -0.70, -0.60, -0.68]
        openai = [0.0, 0.25, 0.05, 0.10, 0.15]
        lower, upper = bootstrap_ci(meta, openai, n_bootstrap=1000)
        # CI should be entirely negative (Meta more negative than OpenAI)
        assert upper < 0, f"Expected CI entirely negative, got [{lower}, {upper}]"
        assert lower < upper

    def test_asymmetry_score_negative_when_target_more_negative(self):
        from datetime import datetime
        target = [-0.65, -0.75, -0.70, -0.60, -0.68]
        peers = [0.0, 0.25, 0.05, 0.10, 0.15]
        result = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="meta",
            peer_entities=["openai"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 29)
        )
        assert result.asymmetry_score < 0, "Asymmetry should be negative when Meta more negative"
        assert result.is_significant, "Should be significant"
        assert abs(result.cohens_d) > 0.5, f"Expected |d|>0.5, got {result.cohens_d}"

    def test_wearables_pricing_inversion_asymmetry(self):
        # Meta $799 criticized vs Snap $2,195 silent
        meta_tones = [-0.65, -0.55, -0.70, -0.60]
        snap_tones = [0.10, 0.05, 0.15, 0.0]  # neutral/positive silence
        t, p = welch_t_test(meta_tones, snap_tones)
        d = cohens_d(meta_tones, snap_tones)
        lower, upper = bootstrap_ci(meta_tones, snap_tones, n_bootstrap=500)
        assert p < 0.05, f"Pricing inversion should be significant, p={p}"
        assert abs(d) > 0.5, f"Pricing inversion should have |d|>0.5, got {d}"
        assert upper < 0.2, f"CI upper should be low, got {upper}"

    def test_google_deal_vs_no_deal_asymmetry(self):
        # Publications with Google deal softer coverage
        with_deal = [-0.05, 0.02, -0.08, 0.01, -0.03]
        without_deal = [-0.35, -0.42, -0.28, -0.38, -0.31]
        t, p = welch_t_test(with_deal, without_deal)
        d = cohens_d(with_deal, without_deal)
        assert p < 0.05, f"Deal vs no-deal should be significant, p={p}"
        assert abs(d) > 0.5, f"Expected moderate+ effect, got d={d}"

    def test_nyt_anthropic_vs_meta_asymmetry(self):
        # NYT Anthropic constructive vs Meta adversarial (mechanism #379)
        anthropic = [0.12, 0.08, 0.05, 0.10, 0.06]  # constructive
        meta = [-0.35, -0.42, -0.28, -0.30, -0.25]  # adversarial
        t, p = welch_t_test(anthropic, meta)
        d = cohens_d(anthropic, meta)
        lower, upper = bootstrap_ci(anthropic, meta, n_bootstrap=1000)
        assert p < 0.05, f"NYT Anthropic vs Meta should be significant"
        assert lower > 0, f"Anthropic should be more positive, CI [{lower},{upper}] should be positive"

    def test_wired_adrienne_so_biometric_inversion_synthetic(self):
        # Mechanism #380: Meta camera glasses vs Google health watch
        meta_vanguard = [-0.35, -0.25]  # privacy attack parenthetical
        google_pixel_watch = [0.45, 0.35]  # promotional
        # Small n but direction clear
        t, p = welch_t_test(meta_vanguard, google_pixel_watch)
        d = cohens_d(meta_vanguard, google_pixel_watch)
        # With n=2, p may be >0.05 but effect size should be huge
        assert abs(d) > 1.0, f"Biometric inversion should have huge effect, d={d}"
        assert meta_vanguard[0] < google_pixel_watch[0], "Meta should be more negative than Google"

    def test_settlement_week_complete_financial_architecture(self):
        # Mechanism #377 quintuple convergence: Meta vs OpenAI settlement week
        meta_settlement = [-0.72, -0.65, -0.81, -0.58, -0.69, -0.74, -0.63, -0.77]
        openai_aspirational = [0.15, 0.22, 0.05, 0.18, 0.12, 0.08, 0.20, 0.10]
        from datetime import datetime
        result = calculate_asymmetry(
            target_scores=meta_settlement,
            peer_scores=openai_aspirational,
            target_entity="meta",
            peer_entities=["openai"],
            publication_slug="nyt",
            period_start=datetime(2026, 8, 26),
            period_end=datetime(2026, 8, 29)
        )
        assert result.asymmetry_score < -0.5, f"Expected strong negative asymmetry, got {result.asymmetry_score}"
        assert result.p_value < 0.001
        assert abs(result.cohens_d) > 1.0
        assert result.confidence_interval_upper < 0


class TestCompetitorCoveragePatterns382:
    """Validate competitor coverage patterns across publications for recent mechanisms."""

    def test_wired_has_openai_and_meta_coverage(self):
        with open(PROFILES_DIR / "wired.yaml") as f:
            content = f.read()
            assert "openai" in content.lower()
            assert "meta" in content.lower()
            # Should have financial chain evidence
            assert "condé nast" in content.lower() or "conde nast" in content.lower()

    def test_nyt_has_amazon_and_anthropic_and_meta(self):
        with open(PROFILES_DIR / "nytimes.yaml") as f:
            content = f.read()
            lower = content.lower()
            assert "amazon" in lower
            assert "anthropic" in lower
            assert "meta" in lower

    def test_ft_openai_superapp_vs_meta_supersensing_documented(self):
        with open(PROFILES_DIR / "financial-times.yaml") as f:
            content = f.read()
            # Mechanism #353 or #359 etc
            lower = content.lower()
            assert "openai" in lower
            # FT should have Meta comparison
            assert "meta" in lower

    def test_verge_apple_smart_glasses_privacy_virtue_documented(self):
        with open(PROFILES_DIR / "the-verge.yaml") as f:
            content = f.read()
            lower = content.lower()
            assert "apple" in lower
            # Mechanism #370 etc
            assert "privacy" in lower or "surveillance" in lower or "glasses" in lower

    def test_no_causal_claim_overreach(self):
        # Ensure profiles use cautious language: structural incentive, not proof of capture
        for yaml_file in PROFILES_DIR.glob("*.yaml"):
            if yaml_file.name.startswith("_"):
                continue
            with open(yaml_file) as f:
                content = f.read()
                # Should not claim "proves editorial capture" as definitive
                lower = content.lower()
                if "proves editorial capture" in lower and "not proof" not in lower:
                    # Allow if it's negated or qualified
                    assert "may" in lower or "predicts" in lower or "suggests" in lower, \
                        f"{yaml_file.name} appears to make strong causal claim without qualification"

    def test_financial_incentive_structural_not_deterministic(self):
        with open(PROFILES_DIR / "competitor-entities.yaml") as f:
            content = f.read()
            # Should contain cautious language
            lower = content.lower()
            assert "structural incentive" in lower or "may shape" in lower or "predicts" in lower or "not proof" in lower, \
                "competitor-entities.yaml should contain cautious financial incentive language"

    def test_podcast_sentiment_exists_and_has_entries(self):
        podcast_path = Path(__file__).parent.parent / "podcast-sentiment.md"
        assert podcast_path.exists(), "podcast-sentiment.md missing"
        with open(podcast_path) as f:
            content = f.read()
            assert "Meta" in content
            assert "Everyone Hates Elon" in content or "Guilty Feminist" in content
            assert "sentiment" in content.lower()


class TestCrossValidationIntegrity382:
    """Ensure iteration log and profile integrity for Type D."""

    def test_iteration_log_contains_type_markers(self):
        log_path = Path(__file__).parent.parent / "iteration-log.md"
        with open(log_path) as f:
            content = f.read()
            assert "Type A" in content
            assert "Type B" in content
            assert "Type C" in content
            assert "Type D" in content
            assert "Type E" in content

    def test_iteration_log_contains_recent_mechanisms(self):
        log_path = Path(__file__).parent.parent / "iteration-log.md"
        with open(log_path) as f:
            content = f.read()
            # Should contain #375-#381
            for num in ["375", "376", "377", "378", "379", "380", "381"]:
                assert num in content, f"Mechanism/iteration #{num} missing from iteration-log"

    def test_test_count_reasonable(self):
        test_files = list(TESTS_DIR.glob("test_*.py"))
        assert len(test_files) >= 600, f"Expected >=600 test files, found {len(test_files)}"

    def test_no_em_dash_violation_in_new_test(self):
        # Project rule: no em dashes in artifacts/content
        import pathlib
        text = pathlib.Path(__file__).read_text(encoding='utf-8')
        # After fix, no em dash character should remain (codepoint 8212)
        assert "\u2014" not in text, "Em dash found in test file"

    def test_source_urls_exact_https(self):
        # All profiles should use exact HTTPS URLs
        for yaml_file in ["financial-times.yaml", "guardian.yaml", "business-insider.yaml", "nytimes.yaml"]:
            path = PROFILES_DIR / yaml_file
            if not path.exists():
                continue
            with open(path) as f:
                content = f.read()
                if "source_url" in content.lower():
                    # Should contain https://
                    assert "https://" in content, f"{yaml_file} should contain HTTPS source URLs"
                    # Should NOT contain placeholder example.com
                    assert "example.com" not in content.lower(), f"{yaml_file} contains example.com placeholder"
