import pathlib, re
import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
PODCAST = REPO / "podcast-sentiment.md"
ITER = REPO / "iteration-log.md"

def read(p):
    return p.read_text(encoding="utf-8", errors="ignore")

def test_podcast_sentiment_exists():
    assert PODCAST.exists()

def test_iteration_log_exists():
    assert ITER.exists()

def test_429_present_podcast():
    txt = read(PODCAST)
    assert "#429" in txt or "Mechanism #429" in txt or "429 Type E" in txt, "#429 must be in podcast-sentiment.md"

def test_429_present_iteration_log():
    txt = read(ITER)
    assert "#429" in txt, "#429 must be in iteration-log.md"
    idx429 = txt.find("#429")
    idx428 = txt.find("#428")
    if idx428 != -1:
        assert idx429 < idx428, "#429 must be prepended newest-first before #428"

def test_rotation_d_to_e():
    txt = read(ITER)
    seg = txt[txt.find("#429"):txt.find("#429")+4000] if "#429" in txt else txt[:4000]
    assert "Type E" in seg, "Type E must be stated near #429"
    assert "D->E" in seg or "428" in seg, "Rotation D->E must be mentioned near #429"

def test_meta_second_led_fix_six_sources_present():
    txt = read(PODCAST)
    required = [
        "https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered",
        "https://9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
        "https://aiweekly.co/alerts/meta-patches-smart-glasses-to-halt-recording-if-led-covered",
        "https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/",
        "https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/",
        "https://en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed",
    ]
    for url in required:
        assert url in txt, f"Missing required LED fix URL {url}"

def test_ai2day_url_present():
    txt = read(PODCAST)
    assert "https://www.youtube.com/watch?v=0qiKNKRetCw" in txt, "AI2Day YouTube URL required"

def test_ai2day_positive_counterexample_framing():
    txt = read(PODCAST)
    lower = txt.lower()
    assert "ai2day" in lower
    assert "positive counterexample" in lower or "mitigation framing" in lower, "Must note AI2Day as positive counterexample"

def test_guilty_feminist_498_ninth_verification():
    txt = read(PODCAST)
    assert "498" in txt, "Must mention #498"
    lower = txt.lower()
    assert "guilty feminist" in lower
    assert "guiltyfeminist.com/list-of-episodes/" in txt, "Must cite official episode list"
    assert "ninth verification" in lower or "ninth" in lower, "Must state ninth verification"

def test_everyone_hates_elon_classification_and_21day_hold():
    txt = read(PODCAST)
    lower = txt.lower()
    assert "everyone hates elon" in lower
    assert "activist group" in lower, "Must classify EHE as activist group"
    assert "not a podcast" in lower or "not podcast" in lower, "Must state EHE is not a podcast"
    assert "21-day" in lower or "21 day" in lower or "21-day hold" in lower, "Must state 21-day hold"
    assert "https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in txt

def test_attention_sphere_ninth_verification_no_match():
    txt = read(PODCAST)
    lower = txt.lower()
    assert "attention sphere" in lower
    assert "no matching podcast" in lower or "no identifiable podcast" in lower, "Must state no matching podcast found"
    assert "ninth" in lower, "Must state ninth verification for Attention Sphere"
    # Ensure we do not fabricate episodes
    assert "attention sphere episode #1" not in lower, "Must not fabricate Attention Sphere episodes"

def test_no_em_dashes_in_new_blocks():
    txt = read(PODCAST)
    if "#429" in txt:
        block = txt[txt.find("#429"):txt.find("#429")+12000]
        assert "—" not in block, "No em dashes allowed in #429 podcast block"
        assert "–" not in block, "No en dashes allowed in #429 podcast block"
    txt_iter = read(ITER)
    if "#429" in txt_iter:
        block = txt_iter[txt_iter.find("#429"):txt_iter.find("#429")+12000]
        assert "—" not in block, "No em dashes allowed in #429 iteration-log block"
        assert "–" not in block, "No en dashes allowed in #429 iteration-log block"

def test_https_urls_exact():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+15000] if "#429" in txt else txt[-15000:]
    # Ensure at least 10 HTTPS URLs in #429 block
    urls = re.findall(r"https://[^\s\)]+", block)
    assert len(urls) >= 10, f"Expected >=10 HTTPS URLs in #429 block, found {len(urls)}"
    for u in urls:
        assert u.startswith("https://"), "All URLs must be HTTPS"

def test_manual_illustrative_labeling():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+15000] if "#429" in txt else txt
    assert "MANUAL ILLUSTRATIVE" in block, "Sentiment scores must be labeled MANUAL ILLUSTRATIVE"
    assert "illustrative" in block.lower(), "Must note illustrative not empirical"

def test_correlation_not_causation():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+60000] if "#429" in txt else txt
    lower = block.lower()
    assert "correlation does not imply causation" in lower or "correlational structural incentive" in lower or "not proof of editorial control" in lower, "Must include correlation not causation language"

def test_absence_monitoring_evidence():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+60000] if "#429" in txt else txt
    lower = block.lower()
    assert "monitoring evidence" in lower, "Must treat absence as monitoring evidence"
    assert "not evidence of favorable" in lower or "not favorable" in lower, "Must state absence is not favorable/unfavorable"

def test_no_empirical_significance_from_absence():
    txt = read(ITER)
    seg = txt[txt.find("#429"):txt.find("#429")+5000] if "#429" in txt else txt[:5000]
    lower = seg.lower()
    assert "no empirical significance" in lower or "do not claim" in lower or "illustrative" in lower or "monitoring correction" in lower, "Must note no empirical significance from absence"

def test_epstein_non_causal_caveat():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+15000] if "#429" in txt else txt
    lower = block.lower()
    if "epstein" in lower and "guilty feminist" in lower:
        assert "correlational" in lower or "no evidence" in lower or "not causal" in lower or "shared cultural" in lower, "Must include non-causal caveat for Epstein imagery"

def test_hardware_capability_inversion_mechanism():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+15000] if "#429" in txt else txt
    lower = block.lower()
    assert "hardware capability inversion" in lower or "mechanism #359" in lower or "closes loophole" in lower, "Must reference hardware capability inversion or closes loophole framing"

def test_meta_dominant_confounders_strong():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+60000] if "#429" in txt else txt
    lower = block.lower()
    assert "[strong]" in lower or "strong confounder" in lower, "Must rank confounders with STRONG marking"
    assert "80%" in block or "7m" in lower or "69.2%" in block, "Must mention Meta dominant market share confounder"

def test_testable_predictions_present():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+60000] if "#429" in txt else txt
    lower = block.lower()
    assert "testable prediction" in lower or "prediction" in lower, "Must include testable predictions"
    assert "samsung" in lower, "Must include Samsung prediction"

def test_no_new_empirical_wired_asymmetry_claim():
    txt = read(PODCAST)
    block = txt[txt.find("#429"):txt.find("#429")+60000] if "#429" in txt else txt
    lower = block.lower()
    assert "no new empirical wired asymmetry" in lower or "does not claim new empirical significance" in lower or "type e validates podcast extension" in lower, "Must state no new empirical WIRED asymmetry claimed for Type E"
