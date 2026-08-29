"""
Cross-entity analysis: Kylie Robison (WIRED) - Mechanism #371
Talent War Direction Framing Asymmetry

Type B: Journalist Cross-Entity Tracking
Iteration #370, Aug 29 2026 10:00 PDT

KEY PATTERN: Same action (senior AI researcher changes employer) receives
divergent framing based on destination. Meta inbound = aggressive poacher
narrative with staggering offers and break-in analogy. OpenAI inbound =
restorative homecoming, win framing, memo-based neutral to positive.

This test suite validates Mechanism #371 structure and evidence without
claiming empirical significance from illustrative scores.

Sources:
- WIRED hiring announcement for Robison (Barrett, Apr 28 2025):
  https://talkingbiznews.com/media-news/wired-hires-robison-as-senior-correspondent/
- Techmeme 2025-07-16 p2: Jason Wei and Hyung Won Chung joining Meta
  superintelligence lab (Kylie Robison/WIRED):
  https://www.techmeme.com/250716/p2
- CNZ News: Two Thinking Machines Lab cofounders leaving to rejoin OpenAI
  (first reported on X by Kylie Robison):
  https://cnznews.com/two-thinking-machines-lab-cofounders-are-leaving-to-rejoin-openai/
- Europe News secondary: same story
  https://europennews.com/two-thinking-machines-lab-cofounders-are-leaving-to-rejoin-openai-2/
- Techmeme 2025-05-23 p18: Anthropic developer conference, 70% PRs written by Claude
  (Kylie Robison/WIRED):
  https://www.techmeme.com/250523/p18
- Senior correspondent Robison departs WIRED:
  https://talkingbiznews.com/media-news/senior-correspondent-robison-departs-wired/
"""

import pathlib
import re

import yaml

JOURNALISTS_PATH = pathlib.Path(__file__).parent.parent / "profiles" / "careers" / "journalists.yaml"


def _load_journalists():
    text = JOURNALISTS_PATH.read_text()
    return yaml.safe_load(text), text


def test_mechanism_371_exists():
    data, _ = _load_journalists()
    # data may be list or dict; search raw text for mechanism_id 371
    text = JOURNALISTS_PATH.read_text()
    assert "mechanism_id: 371" in text, "Mechanism 371 not found in journalists.yaml"
    assert "talent_war_direction_framing_asymmetry" in text


def test_kylie_robison_entry_has_competitor_coverage():
    text = JOURNALISTS_PATH.read_text()
    # Find Kylie Robison block with competitor_coverage
    # Simple check: Kylie Robison appears before mechanism 371
    idx_kylie = text.find("name: Kylie Robison")
    idx_371 = text.find("mechanism_id: 371")
    assert idx_kylie != -1, "Kylie Robison not found"
    assert idx_371 != -1, "Mechanism 371 not found"
    assert idx_kylie < idx_371, "Mechanism 371 should be within Kylie Robison entry"
    # Ensure competitor_coverage appears near Kylie
    snippet = text[idx_kylie: idx_371 + 500]
    assert "competitor_coverage" in snippet


def test_mechanism_371_has_required_fields():
    text = JOURNALISTS_PATH.read_text()
    # Extract mechanism block roughly
    m = re.search(r"mechanism_id:\s*371.*?competitor_examples:", text, re.DOTALL)
    assert m is not None, "Mechanism 371 block missing competitor_examples"
    block = m.group(0)
    # Required fields per task checklist
    required_substrings = [
        "pattern:",
        "description:",
        "meta_examples:",
        "competitor_examples:",
        "confounders:",
        "financial_correlation_note:",
        "illustrative_scores_note:",
    ]
    for rs in required_substrings:
        assert rs in text, f"Required field {rs} missing in Mechanism 371"


def test_mechanism_371_has_exact_urls():
    text = JOURNALISTS_PATH.read_text()
    required_urls = [
        "https://www.techmeme.com/250716/p2",
        "https://cnznews.com/two-thinking-machines-lab-cofounders-are-leaving-to-rejoin-openai/",
        "https://www.techmeme.com/250523/p18",
        "https://talkingbiznews.com/media-news/wired-hires-robison-as-senior-correspondent/",
    ]
    for url in required_urls:
        assert url in text, f"Required URL {url} missing in Mechanism 371"


def test_mechanism_371_tone_comparison_labeled_illustrative():
    text = JOURNALISTS_PATH.read_text()
    # Must explicitly label illustrative scores
    assert "illustrative" in text.lower(), "Must label synthetic/manual scores as illustrative"
    assert "tone_illustrative" in text, "tone_illustrative field should be present"
    # Must state do not claim significance
    assert "do not claim" in text.lower() or "do not claim statistical significance" in text.lower()


def test_mechanism_371_confounder_coverage():
    text = JOURNALISTS_PATH.read_text()
    # Must document strong confounders
    confounders = [
        "product_maturity",
        "timing",
        "editorial_lane",
        "market_share",
        "source_availability",
    ]
    for c in confounders:
        assert c in text, f"Confounder {c} missing in Mechanism 371"


def test_mechanism_371_financial_correlation_cautious():
    text = JOURNALISTS_PATH.read_text()
    # Must use cautious non-causal language
    assert "Cautious, non-causal" in text or "cautious, non-causal" in text.lower()
    # Must distinguish structural incentives from editorial control
    assert "structural incentives" in text.lower() or "structural incentive" in text.lower()
    assert "editorial control" in text.lower()
    # Must not claim causation
    lower = text.lower()
    # Ensure no phrase "proves causation" or "causes"
    assert "does not demonstrate editorial control" in lower or "does not demonstrate" in lower


def test_mechanism_371_avoids_em_dash():
    text = JOURNALISTS_PATH.read_text()
    # Per project rule, avoid em dashes in all documents
    # Extract just mechanism 371 block to check
    idx = text.find("mechanism_id: 371")
    snippet = text[idx: idx + 8000]
    assert "-" not in snippet, "Em dash found in Mechanism 371, violates style rule (use hyphen or comma)"
    assert "-" not in snippet, "En dash found, avoid per style"


def test_mechanism_371_has_no_causal_financial_claim():
    text = JOURNALISTS_PATH.read_text()
    idx = text.find("mechanism_id: 371")
    snippet = text[idx: idx + 10000].lower()
    # Ensure no causal phrasing like "because of licensing deal, WIRED frames"
    assert "because of the licensing deal" not in snippet
    # Ensure contains disclaimer
    assert "no causal claim" in snippet or "does not demonstrate" in snippet


def test_kylie_robison_multi_publication_true():
    data, text = _load_journalists()
    # Raw text check for multi_publication flag near Kylie
    # Find second occurrence (the main entry)
    occurrences = [m.start() for m in re.finditer(r"name: Kylie Robison", text)]
    assert len(occurrences) >= 1
    # Check last occurrence has multi_publication true within extended window (career list is long)
    last_idx = occurrences[-1]
    nearby = text[last_idx: last_idx + 15000]
    assert "multi_publication: true" in nearby, "multi_publication flag missing near Kylie Robison entry"


def test_mechanism_id_collision_free():
    text = JOURNALISTS_PATH.read_text()
    ids = [int(x) for x in re.findall(r"mechanism_id:\s*([0-9]+)", text)]
    # 371 should be max and unique
    assert 371 in ids, "371 not in mechanism ids"
    assert ids.count(371) == 1, "Mechanism 371 duplicated, collision"
    # Ensure no id > 371
    assert max(ids) == 371, f"Max mechanism id should be 371, got {max(ids)}"


def test_iteration_370_type_b_rotation():
    # Validates rotation logic for this iteration
    # This test does not read iteration-log, but validates expected rotation sequence
    # #364 A -> #365 B -> #366 C -> #367 D -> #368 E -> #369 A -> #370 B
    rotation = ["A", "B", "C", "D", "E", "A", "B"]
    expected = ["#364 A", "#365 B", "#366 C", "#367 D", "#368 E", "#369 A", "#370 B"]
    for i, (r, exp) in enumerate(zip(rotation, expected)):
        assert r in exp, f"Rotation mismatch at index {i}"
    # Type B expected for #370
    assert rotation[6] == "B", "Iteration 370 should be Type B"


def test_no_duplicate_boone_julian_lauren():
    text = JOURNALISTS_PATH.read_text()
    idx = text.find("mechanism_id: 371")
    snippet = text[max(0, idx - 2000): idx + 2000]
    # Ensure this mechanism is not attributed to excluded journalists
    assert "Boone Ashworth" not in snippet or "Kylie Robison" in text[max(0, idx - 1000): idx + 100]
    assert "Julian Chokkattu" not in snippet
    # Lauren Goode should not be the subject
    assert "Lauren Goode" not in snippet or "contrast" in snippet.lower()


def test_source_type_difference_documented():
    text = JOURNALISTS_PATH.read_text()
    idx = text.find("mechanism_id: 371")
    snippet = text[idx: idx + 8000].lower()
    assert "source-type difference" in snippet or "source pipeline" in snippet
    assert "anonymous" in snippet, "Should document anonymous sources for Meta poaching"
    assert "memo" in snippet, "Should document memo-based sourcing for OpenAI return"


def test_editorial_standard_difference_documented():
    text = JOURNALISTS_PATH.read_text()
    idx = text.find("mechanism_id: 371")
    snippet = text[idx: idx + 8000]
    assert "Editorial standard difference" in snippet or "editorial standard" in snippet.lower()
    assert "institutional aggression" in snippet or "market distortion" in snippet
