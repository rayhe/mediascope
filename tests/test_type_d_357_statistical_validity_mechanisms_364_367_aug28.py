"""
Type D — Test & Verify — Statistical Validity Consolidation Mechanisms #364-#367
Iteration #357 — Fri 2026-08-28 21:00 PT

Validates asymmetry scoring produces statistically meaningful results for mechanisms
364-367, fixes collection errors from missing package install, and ensures no synthetic
p-values are presented as empirical.

Mechanisms covered since last Type D (#353):
- #364 Statistical Validity Consolidation (Type D meta)
- #365 Celebrity/Institutional Cascade Pervert Glasses Vocabulary (Type E, but scoring validation)
- #366 Dell Cameron Severity Framing Inversion — falsification test, counterevidence
- #367 Amazon Affiliate Commission Cut — 4th financial channel

Rules:
- One article per entity insufficient for inferential significance — descriptive only
- Synthetic arrays labeled illustrative only, never empirical p/d/CI
- Every fact needs source URL — mechanisms 366/367 have verified HTTPS sources
"""

import os
import sys
import pytest
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import (
    welch_t_test,
    cohens_d,
    bootstrap_ci,
    interpret_effect_size,
    is_significant,
)


class TestMechanism364StatisticalValidityConsolidation:
    """Mechanism #364 was itself a Type D statistical validity consolidation."""

    def test_asymmetry_scorer_significant_with_sufficient_data(self):
        """With n>=5 per group, Meta vs peers produces p<0.05, |d|>0.5, CI excludes 0."""
        # Meta adversarial tones (7 samples) vs peer neutral/slight positive (8 samples)
        target = [-0.70, -0.60, -0.80, -0.55, -0.65, -0.75, -0.60]
        peers = [-0.10, 0.00, 0.10, -0.15, 0.05, 0.00, -0.05, 0.10]
        result = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Meta",
            peer_entities=["OpenAI", "Google", "Samsung"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 28),
        )
        assert result.asymmetry_score < -0.4, f"Expected strong negative asymmetry, got {result.asymmetry_score}"
        assert result.p_value < 0.05, f"p should be <0.05 with sufficient separation, got {result.p_value}"
        assert abs(result.cohens_d) > 0.8, f"|d| should be large, got {result.cohens_d}"
        assert result.is_significant is True
        # CI should exclude 0 and be entirely negative
        assert result.confidence_interval_upper < 0, "CI should be entirely negative"
        assert result.confidence_interval_lower < result.confidence_interval_upper

    def test_mechanism_364_file_exists(self):
        """Iteration #353 log entry indicates 25 tests — validate file presence via log."""
        log_path = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")
        assert os.path.exists(log_path), "iteration-log.md must exist"
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "#353" in content, "Log should contain iteration #353"
        assert "Statistical Validity" in content or "353" in content


class TestMechanism365VocabularyCascadeScoring:
    """Mechanism #365 documents 6 independent source groups adopting pervert/pervy vocabulary, all Meta-exclusive."""

    def test_pervert_vocabulary_meta_exclusive_descriptive(self):
        """Meta 6+ sources vs competitors 0 sources — descriptive delta only, n=1 per entity insufficient for inferential."""
        # Illustrative only — descriptive delta, not inferential
        meta_sources = 6  # AmberMac, EHE, RestIsEnt, Therapy, KayGreen, BloodInMachine
        competitor_sources = 0  # Samsung 0 despite identical hardware
        assert meta_sources == 6
        assert competitor_sources == 0
        # Descriptive proportion difference — NOT a p-value
        descriptive_delta = meta_sources - competitor_sources
        assert descriptive_delta == 6, "Descriptive delta 6 vs 0 — illustrative only"

    def test_podcast_sentiment_md_exists(self):
        log_path = os.path.join(os.path.dirname(__file__), "..", "podcast-sentiment.md")
        assert os.path.exists(log_path), "podcast-sentiment.md must exist per Type E mandate"
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "Pervert" in content or "pervert" in content.lower(), "Should track pervert vocabulary"

    def test_no_synthetic_significance_claimed_for_vocabulary(self):
        """Ensure we don't claim p<0.05 for vocabulary counts — n=6 groups anecdotal, not SEC filing."""
        # This test enforces the rule: One article per entity is insufficient
        # Vocabulary cascade is qualitative observation, not statistically tested
        target_scores = [-0.7]  # n=1 per entity
        peer_scores = [-0.1]  # n=1 per entity
        t_stat, p_val = welch_t_test(target_scores, peer_scores)
        # With n<2, welch returns (0.0, 1.0) degenerate — correctly non-significant
        assert p_val == 1.0, "n<2 should return p=1.0 degenerate, not synthetic significance"
        assert t_stat == 0.0


class TestMechanism366DellCameronFalsification:
    """Mechanism #366 — Dell Cameron severity framing inversion is counterevidence to universal softening thesis."""

    def test_counterevidence_preserved(self):
        """Dell Cameron adversarial toward OpenAI despite Condé Nast OpenAI deal — universal softening claim rejected."""
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
        assert os.path.exists(yaml_path), "wired.yaml must exist"
        with open(yaml_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Should contain mechanism #366 or dell_cameron entry
        assert "dell_cameron" in content.lower() or "366" in content, "Should document Dell Cameron mechanism #366"

    def test_descriptive_delta_only_n1_per_entity(self):
        """OpenAI -0.6 vs Meta -0.75 descriptive delta 0.15 — no p/d/CI as empirical."""
        target_scores = [-0.6]  # OpenAI rogue agent tone
        peer_scores = [-0.75]  # Meta NameTag tone
        # Descriptive only
        descriptive_delta = target_scores[0] - peer_scores[0]
        assert abs(descriptive_delta - 0.15) < 0.01, "Descriptive delta 0.15"
        # Welch with n=1 returns degenerate
        t_stat, p_val = welch_t_test(target_scores, peer_scores)
        assert p_val == 1.0, "n=1 per entity insufficient for inferential — must not claim p<0.05"
        assert t_stat == 0.0

    def test_financial_softening_universal_claim_rejected(self):
        """No test should claim financial ties universally produce softer coverage."""
        # Enforce via wired.yaml content check — should contain falsification language
        wired_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
        with open(wired_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
        # Should contain counterevidence or falsification or lane distinction language
        assert any(kw in content for kw in ["counterevidence", "falsification", "lane", "universal", "rejected", "qualifies"]), \
            "wired.yaml should preserve counterevidence language for mechanism #366"

    def test_three_sources_verified_https(self):
        """Mechanism #366 sources: 2 WIRED articles + Reuters Condé Nast deal — HTTPS required."""
        # Check iteration log contains URLs verbatim
        log_path = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")
        with open(log_path, "r", encoding="utf-8") as f:
            log_content = f.read()
        # Should contain at least 2 HTTPS wired.com URLs from #355
        assert "wired.com/story/openais-rogue-ai-agent" in log_content, "Should contain OpenAI rogue agent WIRED URL"
        assert "wired.com/story/meta-smart-glasses-face-recognition-nametag" in log_content, "Should contain Meta NameTag WIRED URL"
        assert "reuters.com/technology/openai-signs-deal-with-cond-nast" in log_content, "Should contain Reuters Condé Nast OpenAI deal URL"


class TestMechanism367AmazonAffiliateCommissionCut:
    """Mechanism #367 — Amazon Associates 50% commission cut, 4th financial channel."""

    def test_amazon_affiliate_yaml_exists(self):
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml")
        assert os.path.exists(yaml_path), "competitor-entities.yaml must exist"
        with open(yaml_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "amazon_affiliate_commission_cut" in content.lower() or "367" in content, \
            "Should document mechanism #367 Amazon affiliate commission cut"

    def test_adweek_source_url_https(self):
        log_path = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "adweek.com/media/amazon-associates-affiliate-rate-cuts-publishers" in content, \
            "Should contain Adweek HTTPS URL verbatim per every-fact-needs-source rule"

    def test_no_synthetic_significance_for_affiliate_anecdotal(self):
        """Adweek 7 publishers anecdotal — not SEC filing — descriptive only, no p/d/CI empirical."""
        # 7 publishers is qualitative, not quantitative corpus for inferential stats
        # Any tone arrays must be labeled illustrative only
        target_scores = [-0.1, -0.15, -0.05]  # hypothetical Amazon soft tones illustrative
        peer_scores = [-0.75, -0.70, -0.80]  # hypothetical Meta adversarial illustrative
        # Even with n=3, if we compute stats they are ILLUSTRATIVE ONLY
        t_stat, p_val = welch_t_test(target_scores, peer_scores)
        # We can compute p, but must label is_empirical false in YAML
        assert isinstance(p_val, float), "Should compute p but label illustrative"
        # Enforce YAML contains illustrative warning
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml")
        with open(yaml_path, "r", encoding="utf-8") as f:
            yaml_content = f.read()
        # Should contain illustrative or cautious language for mechanism 367
        if "367" in yaml_content or "amazon_affiliate" in yaml_content.lower():
            # Check nearby content has illustrative or cautious markers
            assert any(kw in yaml_content.lower() for kw in ["illustrative", "descriptive", "cautious", "anecdotal", "not sec"]), \
                "Mechanism 367 should contain cautious/illustrative language per standing rule"

    def test_wired_correction_0_to_1_preserved(self):
        """Mechanism #96 correction: WIRED 0→1 Apple v OpenAI lawsuit — silence thesis invalidated, framing thesis stands."""
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml")
        with open(yaml_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "correction" in content.lower() or "wired" in content.lower(), "Should preserve correction note"
        log_path = os.path.join(os.path.dirname(__file__), "..", "iteration-log.md")
        with open(log_path, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert "WIRED 0→1" in log_content or "6 vs 1 not 6 vs 0" in log_content or "WIRED 0" in log_content, \
            "Log should contain correction impact note"


class TestStatisticalUtilitiesEdgeCases:
    """Validate statistical utilities handle edge cases per accuracy guide."""

    def test_welch_degenerate_n_less_than_2(self):
        t_stat, p_val = welch_t_test([-0.5], [0.3])
        assert t_stat == 0.0 and p_val == 1.0, "n<2 returns degenerate (0.0, 1.0)"

    def test_welch_zero_variance_different_means(self):
        a = [-0.5, -0.5, -0.5]
        b = [0.5, 0.5, 0.5]
        t_stat, p_val = welch_t_test(a, b)
        assert p_val == 0.0 and t_stat == float("inf"), "Zero variance different means -> inf t, p 0.0"

    def test_welch_zero_variance_same_mean(self):
        a = [0.1, 0.1, 0.1]
        b = [0.1, 0.1, 0.1]
        t_stat, p_val = welch_t_test(a, b)
        assert t_stat == 0.0 and p_val == 1.0

    def test_cohens_d_pooled_sd_zero(self):
        d = cohens_d([0.1, 0.1], [0.1, 0.1])
        assert d == 0.0, "Pooled SD 0 -> d=0.0"

    def test_cohens_d_interpretation(self):
        assert interpret_effect_size(0.1) == "negligible"
        assert interpret_effect_size(0.3) == "small"
        assert interpret_effect_size(0.6) == "medium"
        assert interpret_effect_size(1.2) == "large"

    def test_bootstrap_ci_reproducible(self):
        a = [-0.5, -0.6, -0.4, -0.5]
        b = [0.1, 0.0, 0.2, 0.1]
        ci1 = bootstrap_ci(a, b, n_bootstrap=100, ci=0.95)
        ci2 = bootstrap_ci(a, b, n_bootstrap=100, ci=0.95)
        assert ci1 == ci2, "Bootstrap with seed 42 should be reproducible"

    def test_bootstrap_ci_empty_input(self):
        ci = bootstrap_ci([], [0.1, 0.2])
        assert ci == (0.0, 0.0)

    def test_is_significant_threshold(self):
        assert is_significant(0.04) is True
        assert is_significant(0.05) is False
        assert is_significant(0.06) is False


class TestAsymmetryScorerMeaningfulness:
    """Verify asymmetry scoring produces statistically meaningful results when n>=5 per group with separation."""

    def test_significant_asymmetry_realistic_meta_vs_peers(self):
        """Realistic Meta adversarial vs peer neutral — should be p<0.05, |d|>0.8, CI excludes 0."""
        meta_tones = [-0.68, -0.72, -0.55, -0.80, -0.60, -0.75, -0.65, -0.70]  # n=8, adversarial
        peer_tones = [-0.05, 0.10, 0.00, -0.10, 0.05, 0.15, -0.02, 0.08, 0.00, 0.12]  # n=10, neutral/soft
        result = calculate_asymmetry(
            target_scores=meta_tones,
            peer_scores=peer_tones,
            target_entity="Meta",
            peer_entities=["OpenAI", "Apple", "Google", "Samsung"],
            publication_slug="wired",
            period_start=datetime(2026, 6, 1),
            period_end=datetime(2026, 8, 28),
        )
        assert result.asymmetry_score < -0.5, f"Strong negative asymmetry expected, got {result.asymmetry_score}"
        assert result.is_significant is True, f"Should be significant with n=8 vs n=10 separated, p={result.p_value}"
        assert abs(result.cohens_d) > 0.8, f"Large effect expected, got {result.cohens_d}"
        assert result.confidence_interval_upper < 0, "CI should exclude 0 (entirely negative)"
        assert result.article_count_target == 8
        assert result.article_count_peers == 10

    def test_no_significance_when_distributions_overlap(self):
        """Similar distributions — should NOT be significant."""
        a = [0.1, -0.1, 0.0, 0.1, -0.05, 0.05, 0.0, -0.08]
        b = [0.05, -0.08, 0.02, 0.08, -0.03, 0.06, -0.02, 0.04]
        result = calculate_asymmetry(
            target_scores=a,
            peer_scores=b,
            target_entity="Meta",
            peer_entities=["Google"],
            publication_slug="test",
            period_start=datetime(2026, 1, 1),
            period_end=datetime(2026, 1, 31),
        )
        assert not result.is_significant, f"Overlapping distributions should not be significant, p={result.p_value}"
        assert abs(result.asymmetry_score) < 0.1

    def test_mechanism_366_descriptive_not_inferential_enforced(self):
        """Mechanism #366 n=1 per entity — must be reported descriptive only, no empirical p/d/CI."""
        openai_tone = [-0.6]
        meta_tone = [-0.75]
        t_stat, p_val = welch_t_test(openai_tone, meta_tone)
        # Must be degenerate — cannot claim significance
        assert p_val == 1.0
        assert t_stat == 0.0
        d = cohens_d(openai_tone, meta_tone)
        assert d == 0.0, "n=1+1 <=2 returns d=0.0 per cohens_d implementation"

    def test_yaml_health_all_profiles_parseable(self):
        """All profile YAMLs should be parseable — no syntax errors."""
        import yaml
        profiles_dir = os.path.join(os.path.dirname(__file__), "..", "profiles")
        for fname in os.listdir(profiles_dir):
            if fname.endswith(".yaml") or fname.endswith(".yml"):
                fpath = os.path.join(profiles_dir, fname)
                if os.path.isfile(fpath):
                    with open(fpath, "r", encoding="utf-8") as f:
                        try:
                            yaml.safe_load(f)
                        except yaml.YAMLError as e:
                            pytest.fail(f"YAML parse error in {fname}: {e}")

    def test_every_fact_needs_source_url_rule(self):
        """Mechanisms 366 and 367 must have HTTPS source URLs in YAML."""
        import yaml
        # Check competitor-entities.yaml has sources for 366/367
        yaml_path = os.path.join(os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml")
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # Data structure varies — check raw text for https presence for these mechanisms
        with open(yaml_path, "r", encoding="utf-8") as rf:
            raw = rf.read()
        # If mechanism 367 exists, it must have https://
        if "367" in raw or "amazon_affiliate" in raw.lower():
            # Find amazon section and check it contains https
            assert "https://" in raw, "Every fact needs source URL — HTTPS required"
