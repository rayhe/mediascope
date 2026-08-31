import pathlib, re, sys
import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
PODCAST = REPO / "podcast-sentiment.md"
ITER = REPO / "iteration-log.md"

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def test_podcast_sentiment_exists():
    assert PODCAST.exists(), "podcast-sentiment.md must exist"

def test_iteration_log_exists():
    assert ITER.exists(), "iteration-log.md must exist"

def test_424_present_podcast():
    txt = read(PODCAST)
    assert "#424" in txt or "Iteration 424" in txt or "Mechanism #424" in txt or "424 Type E" in txt, "#424 must be present in podcast-sentiment.md"

def test_424_present_iteration_log():
    txt = read(ITER)
    assert "#424" in txt, "#424 must be in iteration-log.md"
    # newest-first prepend check: #424 appears before #423
    idx424 = txt.find("#424")
    idx423 = txt.find("#423")
    if idx423 != -1:
        assert idx424 < idx423, "#424 must be prepended newest-first before #423"

def test_rotation_d_to_e():
    txt = read(ITER)
    # Ensure rotation transparency mentions D->E
    assert "423 Type D" in txt or "#423" in txt
    # Check that #424 entry states Type E and previous was D
    segment = txt[txt.find("#424"):txt.find("#424")+3000] if "#424" in txt else txt
    assert "Type E" in segment, "Type E must be stated near #424"
    assert "D->E" in segment or "C->D->E" in segment or "423" in segment.lower() or "Previous entry #423" in segment or "rotation" in segment.lower()

def test_everyone_hates_elon_classification():
    txt = read(PODCAST)
    # Must classify EHE as activist group not podcast
    lower = txt.lower()
    assert "everyone hates elon" in lower
    # Find near #424 block - check activist classification
    # Simple global check but ensure activist wording present
    assert "activist group" in lower, "Must classify Everyone Hates Elon as activist group"
    assert "not a podcast" in lower or "not podcast" in lower, "Must state EHE is not a podcast"

def test_attention_sphere_absence_verification():
    txt = read(PODCAST)
    lower = txt.lower()
    assert "attention sphere" in lower
    # Must state no matching podcast found, not invent episodes
    assert "no matching podcast" in lower or "no identifiable podcast" in lower or "no matching show" in lower, "Must state absence for Attention Sphere"
    # Ensure we do not fabricate an episode title for Attention Sphere
    # Check that we do not have a fake episode pattern like "Attention Sphere Episode #"
    assert "attention sphere episode" not in lower or "no matching" in lower, "Must not fabricate Attention Sphere episodes"

def test_guilty_feminist_through_498():
    txt = read(PODCAST)
    lower = txt.lower()
    assert "guilty feminist" in lower
    # Must mention #498 or Politics Aug 31 2026
    assert "498" in txt or "Politics" in txt, "Must mention #498 Politics"
    assert "guiltyfeminist.com/list-of-episodes" in txt or "guiltyfeminist.com" in lower, "Must cite official episode list"
    # Must state no Meta/wearables episode through #498
    assert "no" in lower and "meta" in lower, "Must state no Meta/wearables episode finding"

def test_exact_urls_present():
    txt = read(PODCAST)
    # Required URLs per task spec
    assert "https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in txt, "Engadget EHE bus stop URL required"
    assert "https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/" in txt or "hyperallergic.com" in txt, "Hyperallergic Epstein poster URL required"
    assert "https://guiltyfeminist.com/list-of-episodes/" in txt, "Guilty Feminist official list URL required"

def test_no_fabricated_attention_sphere_episode_titles():
    txt = read(PODCAST)
    # Ensure we do not list fake episodes for Attention Sphere
    # If we mention Attention Sphere, ensure we do not invent titles
    # Simple heuristic: count episode patterns near Attention Sphere
    segments = txt.split("Attention Sphere")
    for seg in segments[1:]:
        snippet = seg[:500].lower()
        # Must not contain fabricated episode titles like "Episode 1: Meta"
        assert "episode 1" not in snippet or "no" in snippet, "Must not fabricate Attention Sphere episode list"

def test_correlation_not_causation_epstein_gf():
    txt = read(PODCAST)
    lower = txt.lower()
    # Must explicitly reject causal link between GF #483 and EHE poster
    if "epstein" in lower and "guilty feminist" in lower:
        # Must contain non-causal caveat
        assert "no evidence" in lower or "not a causal" in lower or "shared cultural" in lower or "not causal" in lower or "no direct relationship" in lower, "Must include non-causal caveat for Epstein poster vs Guilty Feminist #483"

def test_absence_monitoring_not_favorable():
    txt = read(PODCAST)
    lower = txt.lower()
    # Must treat absence as monitoring evidence, not favorable sentiment
    assert "monitoring evidence" in lower or "absence as monitoring" in lower or "absence is" in lower, "Must treat absence as monitoring evidence"
    assert "not evidence of favorable" in lower or "not evidence of unfavorable" in lower or "not favorable" in lower, "Must state absence is not evidence of favorable or unfavorable sentiment"

def test_no_empirical_significance_from_absence():
    txt = read(ITER)
    lower = txt.lower()
    # Ensure iteration-log does not claim empirical significance from absence
    segment = txt[txt.find("#424"):txt.find("#424")+4000] if "#424" in txt else txt[:4000]
    assert "no empirical significance" in segment.lower() or "do not claim" in segment.lower() or "no p-value" in segment.lower() or "illustrative" in segment.lower() or "monitoring correction" in segment.lower(), "Must note no empirical significance claim from absence"

def test_no_em_dashes_in_new_block():
    txt = read(PODCAST)
    # Check the #424 block for em dashes or en dashes
    if "#424" in txt:
        block = txt[txt.find("#424"):txt.find("#424")+8000]
        assert "—" not in block, "No em dashes allowed in #424 block"
        assert "–" not in block, "No en dashes allowed in #424 block"
    txt_iter = read(ITER)
    if "#424" in txt_iter:
        block = txt_iter[txt_iter.find("#424"):txt_iter.find("#424")+8000]
        assert "—" not in block, "No em dashes allowed in #424 iteration-log block"
        assert "–" not in block, "No en dashes allowed in #424 iteration-log block"

def test_manual_illustrative_label_if_scores():
    txt = read(PODCAST)
    if "#424" in txt:
        block = txt[txt.find("#424"):txt.find("#424")+8000]
        # If block contains "/10" score, must label MANUAL ILLUSTRATIVE
        if "/10" in block:
            assert "MANUAL ILLUSTRATIVE" in block, "Synthetic scores must be labeled MANUAL ILLUSTRATIVE"

def test_source_classification_and_dates():
    txt = read(PODCAST)
    # Must have exact dates for Guilty Feminist episodes (allow with or without comma)
    assert ("August 31, 2026" in txt or "Aug 31, 2026" in txt or "August 31 2026" in txt or "Aug 31 2026" in txt), "Must have date for #498 Aug 31 2026"
    assert ("August 24, 2026" in txt or "Aug 24, 2026" in txt or "August 24 2026" in txt or "Aug 24 2026" in txt), "Must have date for #497"
    assert "Engadget" in txt and "July" in txt, "Must have Engadget July 2026 context"
