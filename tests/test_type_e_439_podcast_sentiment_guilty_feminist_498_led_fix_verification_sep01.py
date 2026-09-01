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

def test_439_present_podcast():
    txt = read(PODCAST)
    assert "#439" in txt, "#439 must be in podcast-sentiment.md"

def test_439_present_iteration_log():
    txt = read(ITER)
    assert "#439" in txt, "#439 must be in iteration-log.md"
    idx439 = txt.find("#439")
    idx438 = txt.find("#438")
    if idx438 != -1:
        assert idx439 < idx438, "#439 must be prepended newest-first before #438"

def test_rotation_d_to_e():
    txt = read(ITER)
    seg = txt[txt.find("#439"):txt.find("#439")+4000] if "#439" in txt else txt[:4000]
    assert "Type E" in seg, "Type E must be stated near #439"
    assert "D->E" in seg or "438" in seg, "Rotation D->E must be mentioned near #439"

def test_guilty_feminist_498_present():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    assert "498" in block, "Must mention episode 498"
    lower = block.lower()
    assert "guilty feminist" in lower
    assert "politics" in lower, "Must mention 498 Politics title"
    assert "felicity ward" in lower or "hannah spencer" in lower, "Must mention hosts/guests for 498"
    assert "guiltyfeminist.com/list-of-episodes/" in block, "Must cite official episode list for 498"

def test_guilty_feminist_498_date_verification():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    assert "2026-08-31" in block or "31 August 2026" in block, "Must include 498 release date Aug 31 2026"
    assert "20 August 2026" in block or "2026-08-20" in block, "Must include recording date Aug 20 2026"

def test_guilty_feminist_498_no_meta_coverage():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    lower = block.lower()
    assert "meta" in lower or "ai" in lower or "surveillance" in lower or "privacy" in lower or "wearables" in lower
    assert "absence" in lower, "Must note absence finding for 498 regarding Meta/AI/wearables/privacy/surveillance"

def test_guilty_feminist_498_eleventh_verification():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    lower = block.lower()
    assert "eleventh" in lower or "11th" in lower, "Must state eleventh verification"

def test_everyone_hates_elon_classification_and_22day_hold_extended():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    lower = block.lower()
    assert "everyone hates elon" in lower
    assert "activist group" in lower, "Must classify EHE as activist group"
    assert "not a podcast" in lower or "not podcast" in lower, "Must state EHE is not a podcast"
    assert "22-day" in lower or "22 day" in lower or "22-day hold" in lower or "23-day" in lower, "Must state extended hold since Aug 10"
    assert "https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in txt.lower() or "engadget.com" in lower

def test_attention_sphere_eleventh_verification_no_match():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+20000] if "#439" in txt else txt
    lower = block.lower()
    assert "attention sphere" in lower
    assert "no matching podcast" in lower or "no identifiable podcast" in lower, "Must state no matching podcast found for Attention Sphere"
    assert "eleventh" in lower or "11th" in lower, "Must state eleventh verification for Attention Sphere"

def test_meta_second_led_fix_sources_present():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+20000] if "#439" in txt else txt
    required = [
        "https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/",
        "https://9to5google.com/2026/07/07/meta-ray-ban-smart-glasses-privacy-light-camera-update/",
        "https://glassalmanac.com/theres-no-place-to-escape-from-smart-glasses-prompts-2026-criminal-complaint-against-meta/",
    ]
    for url in required:
        assert url.lower() in block.lower() or url.lower() in txt.lower(), f"Missing required LED fix URL {url}"

def test_shared_security_urls_present():
    txt = read(PODCAST)
    assert "https://www.youtube.com/watch?v=gxZj-XGIQ3Y" in txt, "Shared Security YouTube URL required"

def test_no_em_dashes_in_new_blocks():
    txt = read(PODCAST)
    if "#439" in txt:
        block = txt[txt.find("#439"):txt.find("#439")+25000]
        assert "—" not in block, "No em dashes allowed in #439 podcast block"
        assert "–" not in block, "No en dashes allowed in #439 podcast block"
    txt_iter = read(ITER)
    if "#439" in txt_iter:
        block = txt_iter[txt_iter.find("#439"):txt_iter.find("#439")+15000]
        assert "—" not in block, "No em dashes allowed in #439 iteration-log block"
        assert "–" not in block, "No en dashes allowed in #439 iteration-log block"

def test_https_urls_exact():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt[-25000:]
    urls = re.findall(r"https://[^\s\)]+", block)
    assert len(urls) >= 10, f"Expected >=10 HTTPS URLs in #439 block, found {len(urls)}"
    for u in urls:
        assert u.startswith("https://"), "All URLs must be HTTPS"

def test_manual_illustrative_labeling():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    assert "MANUAL ILLUSTRATIVE" in block, "Sentiment scores must be labeled MANUAL ILLUSTRATIVE"

def test_correlation_not_causation():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+60000] if "#439" in txt else txt
    lower = block.lower()
    assert "correlation does not imply causation" in lower or "correlational structural incentive" in lower or "not proof of editorial control" in lower, "Must include correlation not causation language"

def test_absence_monitoring_evidence():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+60000] if "#439" in txt else txt
    lower = block.lower()
    assert "monitoring evidence" in lower, "Must treat absence as monitoring evidence"
    assert "not evidence of favorable" in lower or "not favorable" in lower, "Must state absence is not favorable/unfavorable"

def test_no_empirical_significance_from_absence():
    txt = read(ITER)
    seg = txt[txt.find("#439"):txt.find("#439")+6000] if "#439" in txt else txt[:6000]
    lower = seg.lower()
    assert "no empirical significance" in lower or "do not claim" in lower or "illustrative" in lower or "monitoring correction" in lower, "Must note no empirical significance from absence"

def test_hardware_capability_inversion_mechanism():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+20000] if "#439" in txt else txt
    lower = block.lower()
    assert "hardware capability inversion" in lower or "mechanism #359" in lower or "closes loophole" in lower or "led fix" in lower, "Must reference hardware capability inversion or LED fix"

def test_meta_dominant_confounders_strong():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+60000] if "#439" in txt else txt
    lower = block.lower()
    assert "[strong]" in lower or "strong confounder" in lower, "Must rank confounders with STRONG marking"
    assert "80%" in block or "7m" in lower or "69.2%" in block or "dominant" in lower, "Must mention Meta dominant market share confounder"

def test_testable_predictions_present():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+60000] if "#439" in txt else txt
    lower = block.lower()
    assert "testable prediction" in lower or "prediction" in lower, "Must include testable predictions"
    assert "samsung" in lower, "Must include Samsung prediction"

def test_no_new_empirical_wired_asymmetry_claim():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+60000] if "#439" in txt else txt
    lower = block.lower()
    assert "no new empirical wired asymmetry" in lower or "does not claim new empirical significance" in lower or "type e validates podcast extension" in lower or "no new empirical" in lower, "Must state no new empirical WIRED asymmetry claimed for Type E"

def test_left_to_their_own_devices_no_august_episode():
    txt = read(PODCAST)
    block = txt[txt.find("#439"):txt.find("#439")+25000] if "#439" in txt else txt
    lower = block.lower()
    assert "left to their own devices" in lower, "Must mention Left to Their Own Devices"
    assert "no august" in lower or "no new episode" in lower or "absence" in lower, "Must note no August episode for Left to Their Own Devices"

def test_hateaid_complaint_present():
    txt = read(PODCAST)
    assert "hateaid" in txt.lower() or "glassalmanac" in txt.lower(), "Must reference HateAid criminal complaint Aug 12 2026"

