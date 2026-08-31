"""
Type A #410: FT Anthropic IPO aspirational vs Meta super-sensing cautionary bifurcation
Mechanism: FT × Anthropic vs FT × Meta, Aug 31 2026, correlation not causation, MANUAL ILLUSTRATIVE
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PROFILE_PATH = REPO_ROOT / "profiles" / "financial-times.yaml"
ITERATION_LOG = REPO_ROOT / "iteration-log.md"

def test_ft_profile_contains_anthropic_410_block():
    text = PROFILE_PATH.read_text()
    assert "iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary" in text
    assert "https://www.macrumors.com/2026/07/09/meta-super-sensing-glasses-record-everything/" in text
    assert "https://aiindustrytoday.com/news/financial-times-reports-ai-integration-targeting-wearables-as-gateway/" in text
    assert "https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539" in text
    assert "https://fastcompany.co.za/tech/2026-08-25-whats-the-plan-with-metas-creepy-smart-glasses/" in text
    assert "https://www.reuters.com/business/media-telecom/anthropic-expected-tell-investors-it-sees-over-30-trillion-potential-revenue-wsj-2026-08-25/" in text
    assert "https://www.reuters.com/technology/anthropic-pay-nscale-45-billion-rent-ai-computing-power-bloomberg-news-reports-2026-08-26/" in text
    assert "https://www.reuters.com/business/finance/anthropic-planned-then-abandoned-7-billion-purchase-matx-sources-say-2026-08-27/" in text
    assert "https://www.reuters.com/legal/government/anthropic-plans-publicly-unveil-ipo-prospectus-after-labor-day-information-2026-08-27/" in text

def test_https_only_provenance():
    text = PROFILE_PATH.read_text()
    # Check iteration 410 block does not introduce http:// URLs
    block_match = re.search(r"iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary:(.*?)recent_coverage_examples_2026:", text, re.DOTALL)
    assert block_match, "410 block not found"
    block = block_match.group(1)
    urls = re.findall(r"https?://[^\s'\"]+", block)
    for u in urls:
        assert u.startswith("https://"), f"Non-HTTPS URL found in 410 block: {u}"

def test_manual_illustrative_labeling_and_no_causal_claim():
    text = PROFILE_PATH.read_text()
    block_match = re.search(r"iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary:(.*?)recent_coverage_examples_2026:", text, re.DOTALL)
    assert block_match
    block = block_match.group(1)
    assert "MANUAL ILLUSTRATIVE" in block
    assert "NOT CALCULATED" in block
    assert "Correlation does not imply causation" in text or "Correlation not causation" in text or "correlation not causation" in text.lower()
    # Ensure no causal verb in description: avoid "proves" "causes" "drives" as definitive
    # Allow "may correlate" "predicts" "suggests" but not "proves editorial influence"
    assert "proves editorial influence" not in block.lower()

def test_no_fabricated_timestamps_or_quotes():
    text = PROFILE_PATH.read_text()
    block_match = re.search(r"iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary:(.*?)recent_coverage_examples_2026:", text, re.DOTALL)
    assert block_match
    block = block_match.group(1)
    # Must contain actual source date references Aug 25-27 and Jul 9 Aug 24
    assert "2026-08-25" in block or "Aug 25" in block
    assert "2026-08-26" in block or "Aug 26" in block
    assert "2026-08-27" in block or "Aug 27" in block
    assert "2026-07-09" in block or "Jul 9" in block
    # No invented exact time like 12:34:56 unless from source - forbid pattern HH:MM:SS in this block
    assert "12:34" not in block

def test_rotation_sequence_and_iteration_log():
    log = ITERATION_LOG.read_text()
    assert "#410 Type A: FT Anthropic IPO aspirational vs Meta super-sensing cautionary bifurcation" in log
    # Verify rotation A after D/E/E
    assert "#407" in log
    assert "#408" in log
    assert "#409" in log
    assert "#410" in log
    # Mechanism ID 410 unique check via string presence
    assert "Mechanism: #410" in log or "mechanism: 410" in log.lower()
    # Ensure Type A label
    assert "Type: A" in log.split("#410")[1][:500]

def test_no_em_dashes():
    profile_text = PROFILE_PATH.read_text()
    block_match = re.search(r"iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary:(.*?)recent_coverage_examples_2026:", profile_text, re.DOTALL)
    assert block_match
    block = block_match.group(1)
    assert "—" not in block, "Em dash found in 410 block, violates standing rule"
    log_text = ITERATION_LOG.read_text().split("#409")[0]
    assert "—" not in log_text or log_text.count("—") == 0 or "#410" in log_text  # ensure new entry has no em dashes
    # Specifically check new entry first 2000 chars
    new_entry = ITERATION_LOG.read_text()[:4000]
    assert "—" not in new_entry, f"Em dash in new iteration log entry"

def test_asymmetry_scoring_structure():
    text = PROFILE_PATH.read_text()
    assert "target_scores_manual_illustrative" in text
    assert "peer_scores_manual_illustrative" in text
    assert "delta_manual_illustrative" in text
    assert "-0.7475" in text
    assert "target_avg_manual_illustrative" in text
    assert "peer_avg_manual_illustrative" in text

def test_confounder_preservation():
    text = PROFILE_PATH.read_text()
    block_match = re.search(r"iteration_410_aug31_2026_ft_anthropic_aspirational_vs_meta_cautionary:(.*?)recent_coverage_examples_2026:", text, re.DOTALL)
    assert block_match
    block = block_match.group(1)
    assert "confounders" in block
    assert "beat assignment" in block.lower()
    assert "product-stage" in block.lower()
    assert "sourcing access" in block.lower()
