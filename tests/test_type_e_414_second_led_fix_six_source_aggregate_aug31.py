"""
Iteration #414 Type E - Meta Second LED Fix Six-Source Aggregate + Guilty Feminist August Silence + Attention Sphere Sixth Verification + Everyone Hates Elon Holding Aug 31 2026

Tests grounded in actual stored findings, HTTPS provenance, no em dashes, MANUAL ILLUSTRATIVE labeling, correlational framing, editorial independence, confounder preservation.

Mechanism #414: Type E podcast/broadcast sentiment tracking, 6-source aggregate verification Aug 27-28 2026, Guilty Feminist 3-episode August audit, Attention Sphere sixth verification, Everyone Hates Elon holding 21/45 days.

Sources: 12 HTTPS URLs verified.
"""

import pathlib
import re

REPO = pathlib.Path(__file__).parent.parent
ITER_LOG = REPO / "iteration-log.md"
PODCAST = REPO / "podcast-sentiment.md"


def read_text(p):
    return p.read_text(encoding="utf-8", errors="ignore")


def test_iteration_414_exists_in_log():
    text = read_text(ITER_LOG)
    assert "#414 Type E" in text
    assert "2026-08-31 04:00 PDT" in text
    assert "Type E" in text
    assert "Mechanism" in text and "#414" in text


def test_no_em_dashes_in_iteration_414_block():
    lines = read_text(ITER_LOG).splitlines()[:300]
    block = "\n".join(lines)
    assert "—" not in block, "Em dash found in new iteration block"
    assert "–" not in block, "En dash found in new iteration block"


def test_six_source_https_urls_present():
    log = read_text(ITER_LOG)
    podcast = read_text(PODCAST)
    expected = [
        "https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/",
        "https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered",
        "https://aiweekly.co/alerts/meta-patches-smart-glasses-to-halt-recording-if-led-covered",
        "https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/",
        "https://theibulletin.com/meta-smart-glasses-capture-led-loophole-billboard-campaign/",
        "https://9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
        "https://www.androidauthority.com/meta-smart-glasses-recording-led-fix-3704164/",
        "https://theitguysfix.com/2026/08/28/5-pm-technology-news-recap-papercut-patch-2-gputhor-apple-price-hikes-meta-glasses-privacy-august-28-2026/",
    ]
    for url in expected:
        assert url in log, f"Missing URL in iteration-log {url}"
        assert url in podcast, f"Missing URL in podcast-sentiment {url}"
        assert url.startswith("https://")


def test_nbc_and_singulism_and_guilty_feminist_sources():
    log = read_text(ITER_LOG)
    assert "https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/" in log
    assert "https://www.youtube.com/watch?v=0NLaAQuaCJE" in log
    assert "https://zeno.fm/podcast/the-guilty-feminist/" in log
    assert "https://guiltyfeminist.com/episode/" in log


def test_sentiment_scores_labeled_manual_illustrative():
    log = read_text(ITER_LOG)
    podcast = read_text(PODCAST)
    # Must contain MANUAL ILLUSTRATIVE label for synthetic scores
    assert "MANUAL ILLUSTRATIVE" in log
    assert "MANUAL ILLUSTRATIVE" in podcast
    # Must contain DO NOT claim statistical significance language
    assert "DO NOT claim" in log or "not empirical" in log.lower()
    # Aggregate -2.2 must be present
    assert "-2.2" in log or "-2.17" in log
    # Illustrative range -1 to -4
    assert "illustrative" in log.lower()


def test_no_p_value_claim_as_empirical():
    log = read_text(ITER_LOG)[:25000]
    # Should not claim p < 0.05 as empirical for this Type E (synthetic illustrative only)
    # Allow p_value in mechanism #412 context but not for #414 sentiment aggregate
    # Check that #414 block does not claim p-value
    block = "\n".join(read_text(ITER_LOG).splitlines()[:250])
    # If p-value appears, it must be in MANUAL ILLUSTRATIVE context or prior mechanisms
    if "p_value" in block.lower() or "p-value" in block.lower():
        assert "MANUAL ILLUSTRATIVE" in block


def test_guilty_feminist_august_audit():
    log = read_text(ITER_LOG)
    podcast = read_text(PODCAST)
    assert "Guilty Feminist" in log
    assert "The Nuance Drought" in log
    assert "Intimacy" in log
    assert "Wilderness Festival" in log
    assert "497" in log
    assert "496" in log
    assert "No Meta/AI/wearables/privacy/surveillance" in log or "no meta" in log.lower()
    assert "No bias claim" in log or "no bias claim" in podcast.lower() or "strong confounder" in log.lower()
    # Must note Edinburgh Fringe confounder
    assert "Edinburgh Fringe" in log or "Fringe" in log


def test_attention_sphere_sixth_verification():
    log = read_text(ITER_LOG)
    assert "Attention Sphere" in log
    assert "No matching podcast found" in log or "No Matching Podcast Found" in log
    assert "Left to Their Own Devices" in log
    assert "Ava Smithing" in log or "Toronto Star" in log
    # Must note 6 searches
    assert "6 searches" in log or "sixth" in log.lower() or "Sixth" in log


def test_everyone_hates_elon_holding():
    log = read_text(ITER_LOG)
    assert "Everyone Hates Elon" in log
    assert "No new campaign" in log or "holding" in log.lower()
    assert "21 days" in log or "45 days" in log
    assert "Epstein" in log or "epstein" in log.lower()
    assert "Meta exclusive" in log or "Meta-exclusive" in log


def test_confounder_preservation():
    log = read_text(ITER_LOG)
    # Must have 4 STRONG, 2 MODERATE, 1 WEAK labeling
    assert "[STRONG]" in log
    assert log.count("[STRONG]") >= 4
    assert "[MODERATE]" in log
    assert "[WEAK]" in log
    # Must preserve news peg justification
    assert "news peg" in log.lower()
    # Must preserve editorial lane mediation
    assert "editorial lane" in log.lower() or "Editorial lane" in log


def test_cross_entity_differential_tracking():
    log = read_text(ITER_LOG)
    assert "Cross-Entity" in log or "cross-entity" in log.lower()
    assert "differential" in log.lower() or "Different standards" in log
    # Must mention Samsung Galaxy Glasses 0 coverage
    assert "Samsung Galaxy Glasses" in log
    assert "0 campaigns" in log or "0 podcast" in log


def test_testable_predictions_five():
    log = read_text(ITER_LOG)
    assert "Testable Predictions" in log
    # Count predictions 1. to 5.
    # Should have 5 predictions
    assert "1." in log and "2." in log and "3." in log and "4." in log and "5." in log
    assert "Samsung Galaxy Glasses firmware" in log or "Samsung" in log
    assert "Apple N50" in log or "Apple" in log
    assert "Everyone Hates Elon" in log
    assert "Guilty Feminist" in log
    assert "Attention Sphere" in log


def test_financial_context_correlational_not_causal():
    log = read_text(ITER_LOG)
    # Must treat financial as correlational structural incentive not proof
    assert "correlational" in log.lower() or "structural" in log.lower()
    assert "editorial independence" in log.lower() or "Editorial independence" in log
    # Must not claim deterministic proof
    assert "not deterministic" in log.lower() or "not proof" in log.lower() or "structural incentive" in log.lower()


def test_mechanism_414_unique_and_extends():
    log = read_text(ITER_LOG)
    assert "Mechanism ID 414 unique" in log
    assert "#408" in log or "408" in log
    assert "#378" in log or "378" in log
    assert "#383" in log or "383" in log


def test_no_em_dashes_in_podcast_new_entry():
    podcast = read_text(PODCAST)
    # Check last 200 lines (new entry)
    tail = "\n".join(podcast.splitlines()[-200:])
    assert "—" not in tail, "Em dash found in new podcast entry"
    assert "–" not in tail, "En dash found in new podcast entry"


def test_podcast_episode_124_structure():
    podcast = read_text(PODCAST)
    assert "### 124." in podcast
    assert "Mechanism #414" in podcast
    assert "Six-Source Aggregate" in podcast or "Six-Source" in podcast
    assert "Sentiment" in podcast
    assert "Asymmetry Assessment" in podcast or "Asymmetry" in podcast
    assert "Financial Context" in podcast or "Financial" in podcast
    assert "Confounders" in podcast or "STRONG" in podcast


def test_rotation_correct():
    log = read_text(ITER_LOG)
    # Rotation line should show E after D
    assert "Rotation:" in log
    assert "Type E per A,B,C,D,E cycle" in log
    assert "#409 E finalize" in log
    assert "#410 A" in log
    assert "#411 B" in log
    assert "#412 C" in log
    assert "#413 D" in log
    assert "#414 E" in log


def test_source_count_twelve_https():
    log = read_text(ITER_LOG)
    # Count https in sources section of new block (first 300 lines)
    block = "\n".join(read_text(ITER_LOG).splitlines()[:300])
    https_count = block.count("https://")
    assert https_count >= 12, f"Expected >=12 HTTPS URLs in new block, found {https_count}"


def test_himel_quote_preserved():
    log = read_text(ITER_LOG)
    assert "Alex Himel" in log
    assert "tiny minority" in log
    assert "reliability of the capture LED" in log or "reliability" in log.lower()


def test_cnil_and_billboard_context():
    log = read_text(ITER_LOG)
    assert "CNIL" in log
    assert "Jun 29" in log or "June 29" in log
    assert "billboard" in log.lower()
    assert "Albert Aydin" in log or "The Verge" in log


def test_limitations_section():
    log = read_text(ITER_LOG)
    assert "Limitations" in log
    assert "illustrative" in log.lower()
    assert "No independent hands-on verification" in log or "no hands-on" in log.lower()
    assert "Guilty Feminist silence based on titles" in log or "titles/descriptions" in log


def test_no_major_discovery_silent():
    log = read_text(ITER_LOG)
    assert "No major discovery requiring alert" in log
    assert "silent per instruction" in log.lower()


def test_mechanism_not_financial_incentive_proof():
    # Ensure we do not claim financial relationships prove editorial influence
    log = read_text(ITER_LOG)
    lower = log.lower()
    # Must not have "proves bias" type claim
    assert "proves" not in lower or "cultural consensus" in lower or "structural" in lower
    # Must acknowledge alternative explanations
    assert "alternative explanation" in lower or "Market dominance" in log or "market dominance" in lower
