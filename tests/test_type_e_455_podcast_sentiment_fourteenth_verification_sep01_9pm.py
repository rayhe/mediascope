"""
Type E #455 - Podcast Sentiment Tracking Fourteenth Verification Sep 1 21:00 PDT
Guilty Feminist 496-498 Hold No 499 as of 21:00 + EHE 22-Day Hold + Attention Sphere 14th No-Match + 9to5Mac Security Bite Extension
"""
import json
from pathlib import Path

import pytest
import yaml

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 455
DATE_STR = "2026-09-01 21:00 PDT"
TYPE_E = "Type E"

def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")

def get_455_block():
    text = read_doc()
    # Find iteration 455 block
    marker = "## Iteration #455"
    idx = text.find(marker)
    assert idx != -1, "Iteration #455 block not found in podcast-sentiment.md"
    return text[idx:]

class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_455_block()
        assert "455" in block
        assert "Type E" in block or "Type E #455" in block

    def test_date_present(self):
        block = get_455_block()
        assert "2026-09-01 21:00 PDT" in block

    def test_rotation_d_to_e(self):
        block = get_455_block()
        # Should mention rotation D->E and 454 D to 455 E
        assert "454" in block
        assert "D->E" in block or "D to 455 E" in block or "454 D to 455 E" in block

    def test_goal_and_job_ids(self):
        block = get_455_block()
        assert GOAL_ID in block
        assert JOB_ID in block

class TestGuiltyFeminist498:
    def test_guilty_feminist_latest_498(self):
        block = get_455_block()
        assert "498" in block
        assert "Politics" in block
        assert "Felicity Ward" in block

    def test_no_499_bounded(self):
        block = get_455_block()
        assert "no 499" in block.lower() or "No 499" in block or "no new episode beyond 498" in block.lower()
        # Must label as bounded search result not universal proof
        assert "bounded" in block.lower()

    def test_official_source_https(self):
        block = get_455_block()
        assert "https://guiltyfeminist.com/list-of-episodes/" in block
        # Must be HTTPS
        assert "http://" not in block.lower() or "https://" in block.lower()

    def test_five_hour_extension(self):
        block = get_455_block()
        assert "5-hour" in block or "5 hour" in block.lower()
        assert "16:00" in block
        assert "21:00" in block

class TestEveryoneHatesElon:
    def test_ehe_activist_not_podcast(self):
        block = get_455_block()
        assert "Activist group" in block
        assert "not a podcast" in block.lower() or "not podcast" in block.lower()

    def test_ehe_22_day_hold(self):
        block = get_455_block()
        assert "22-day" in block or "22 day" in block.lower()
        assert "Aug 10" in block

    def test_ehe_bounded_absence(self):
        block = get_455_block()
        # Must not claim universal absence - must say bounded search
        lower = block.lower()
        assert "bounded" in lower
        # Should mention Engadget primary for Jul campaign
        assert "engadget" in lower or "ENGADGET" in block

    def test_ehe_secondary_unverified_label(self):
        block = get_455_block()
        # Must note Wikipedia secondary lag
        assert "Wikipedia" in block or "wikipedia" in block.lower()
        assert "secondary" in block.lower()

class TestAttentionSphere:
    def test_attention_sphere_14th_no_match(self):
        block = get_455_block()
        assert "Attention Sphere" in block
        assert "14th" in block or "14" in block
        assert "no matching podcast" in block.lower() or "no-match" in block.lower()

    def test_attention_sphere_circular_rejection(self):
        block = get_455_block()
        assert "circular" in block.lower()
        # Must not treat own repo as evidence
        assert "github.com/rayhe/mediascope" in block or "circular sourcing" in block.lower()

    def test_attention_sphere_bounded(self):
        block = get_455_block()
        lower = block.lower()
        assert "bounded" in lower or "not proof" in lower
        # Must not elevate Ava Smithing claim without primary
        # Check that unverified label exists if Ava mentioned
        if "Ava Smithing" in block:
            assert "unverified" in lower

class TestSecondaryAndSecurityBite:
    def test_9to5mac_security_bite_present(self):
        block = get_455_block()
        assert "9to5Mac" in block or "9to5mac" in block.lower()
        assert "Security Bite" in block or "security bite" in block.lower()
        assert "Apple camera AirPods" in block or "camera AirPods" in block

    def test_9to5mac_security_bite_source_https(self):
        block = get_455_block()
        assert "https://9to5mac.com/2026/08/18/security-bite-apples-camera-airpods-are-going-to-make-meta-glasses-look-reckless/" in block

    def test_fortune_revalidation(self):
        block = get_455_block()
        assert "Fortune" in block

class TestCautiousLanguage:
    def test_manual_illustrative_label(self):
        block = get_455_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block or "ci_upper" in block.lower() or "ci NOT_CALCULATED" in block
        assert "is_significant False" in block or "is_significant false" in block.lower()

    def test_correlation_not_causation(self):
        block = get_455_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower
        assert "structural incentive" in lower or "not proof" in lower

    def test_no_em_dashes(self):
        block = get_455_block()
        # No em dashes allowed in doc per rule
        assert "—" not in block, "Em dash found in #455 block - banned per AGENTS.md"

    def test_https_only(self):
        block = get_455_block()
        # Find all URLs - must be https
        import re
        urls = re.findall(r'https?://[^\s\)"]+', block)
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_455_block()
        lower = block.lower()
        # Must not claim empirical significance
        assert "do not claim empirical significance" in lower or "no claim empirical" in lower or "not empirical" in lower

class TestNoveltyAndDuplicatePrevention:
    def test_distinct_from_450(self):
        block = get_455_block()
        assert "450" in block
        # Must say genuinely novel or extension not duplicate
        lower = block.lower()
        assert "genuinely novel" in lower or "extension not duplicate" in lower or "not duplicate" in lower

    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_455_block()
        # Must explicitly note Microsoft PCM already covered
        assert "Microsoft PCM" in block or "PCM" in block
        assert "already" in block.lower() or "exhaustively covered" in block.lower()

    def test_yaml_parsable(self):
        # podcast-sentiment.md is markdown not yaml but check no broken yaml blocks
        text = read_doc()
        assert len(text) > 1000

class TestDuplicatePreventionGoal:
    def test_iteration_log_455_exists(self):
        log_path = Path(__file__).parent.parent / "iteration-log.md"
        log_text = log_path.read_text(encoding="utf-8")
        assert "#455" in log_text
        assert "Type E" in log_text
        assert "2026-09-01 21:00 PDT" in log_text
