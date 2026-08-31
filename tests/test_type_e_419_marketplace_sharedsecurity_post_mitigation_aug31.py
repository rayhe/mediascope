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

def test_iteration_419_present():
    txt = read(ITER)
    assert "#419" in txt, "#419 must be in iteration-log"
    # Use robust header search to avoid false positives from #424 mentioning #419
    m = re.search(r"^#419 Type E:", txt, re.MULTILINE)
    assert m is not None, "#419 Type E header must be in iteration-log"
    assert "Type E" in txt[m.start():m.start()+800], "Type E near #419"

def test_rotation_d_to_e():
    txt = read(ITER)
    # check previous #418 D and #419 E ordering - use header patterns at line start to avoid false positives from #424 mentioning old IDs
    m418 = re.search(r"^#418 Type D:", txt, re.MULTILINE)
    m419 = re.search(r"^#419 Type E:", txt, re.MULTILINE)
    assert m418 is not None and m419 is not None, "Both #418 and #419 headers must exist"
    idx418 = m418.start()
    idx419 = m419.start()
    assert idx419 < idx418, "#419 must be prepended newest-first before #418"
    # rotation transparency text
    assert "418 D" in txt or "Type D at 2026-08-31 07:00" in txt
    assert "08:00 PDT" in txt
    assert "rotation E after 418 D" in txt.lower() or "next after D is E" in txt

def test_marketplace_url():
    txt = read(PODCAST)
    assert "https://www.marketplace.org/episode/2026/08/26/metas-push-to-make-their-smart-glasses-cool" in txt

def test_shared_security_url():
    txt = read(PODCAST)
    assert "https://sharedsecurity.net/2026/03/16/" in txt

def test_guilty_feminist_urls():
    txt = read(PODCAST)
    assert "https://zeno.fm/podcast/the-guilty-feminist/" in txt
    assert "https://guiltyfeminist.com/episode/" in txt

def test_engadget_ehe_url():
    txt = read(PODCAST)
    assert "https://www.engadget.com/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in txt

def test_ai2day_url():
    txt = read(PODCAST)
    assert "https://www.youtube.com/watch?v=0qiKNKRetCw" in txt

def test_it_guys_url():
    txt = read(PODCAST)
    assert "https://theitguysfix.com/2026/08/28/5-pm-technology-news-recap-papercut-patch-2-gputhor-apple-price-hikes-meta-glasses-privacy-august-28-2026/" in txt

def test_cnet_url():
    txt = read(PODCAST)
    assert "https://www.cnet.com/tech/mobile/meta-closes-loophole-that-let-people-record-secretly-with-smart-glasses/" in txt

def test_startup_fortune_url():
    txt = read(PODCAST)
    assert "https://startupfortune.com/meta-closes-a-second-loophole-that-let-ray-ban-glasses-record-in-secret/" in txt

def test_tech_insider_gadget_review():
    txt = read(PODCAST)
    assert "https://tech-insider.org/meta-ai-glasses-recording-led-fix-2026/" in txt
    assert "https://www.gadgetreview.com/metas-smart-glasses-now-stop-recording-when-the-led-is-covered" in txt

def test_twelve_https_sources():
    # Count https URLs in podcast episodes 125 and 126 sections
    txt = read(PODCAST)
    # find last 2 episodes
    idx125 = txt.rfind("### 125.")
    assert idx125 != -1, "Episode 125 must exist"
    snippet = txt[idx125:]
    urls = re.findall(r"https://[^\s\)]+", snippet)
    assert len(urls) >= 12, f"Need >=12 HTTPS URLs in new episodes, got {len(urls)}"

def test_manual_illustrative_label():
    txt = read(PODCAST)
    idx125 = txt.rfind("### 125.")
    snippet = txt[idx125:]
    assert "MANUAL ILLUSTRATIVE" in snippet, "Must label subjective scores MANUAL ILLUSTRATIVE"
    assert "DO NOT claim" in snippet

def test_no_em_dashes():
    txt = read(PODCAST)
    idx125 = txt.rfind("### 125.")
    snippet = txt[idx125:idx125+20000]
    assert "—" not in snippet, "Must not contain em dash"
    assert "–" not in snippet, "Must not contain en dash"

def test_no_en_dashes_iteration():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+25000]
    assert "—" not in snippet
    assert "–" not in snippet

def test_confounders_present():
    txt = read(PODCAST)
    idx125 = txt.rfind("### 125.")
    snippet = txt[idx125:]
    assert "Confounders" in snippet
    assert "[STRONG]" in snippet
    assert "[MODERATE]" in snippet

def test_financial_context_correlational():
    txt = read(PODCAST)
    idx125 = txt.rfind("### 125.")
    snippet = txt[idx125:]
    assert "Financial Context" in snippet or "financial" in snippet.lower()
    # must say correlational not causal or similar
    lower = snippet.lower()
    assert "correlational" in lower or "correlation does not" in lower or "not proof" in lower

def test_editorial_independence_acknowledged():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+30000].lower()
    assert "editorial independence" in snippet or "no documented editorial directive" in snippet

def test_guilty_feminist_seventh_verification():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+30000]
    assert "Guilty Feminist" in snippet
    assert "seventh" in snippet.lower() or "7th" in snippet or "Seventh Verification" in snippet

def test_attention_sphere_seventh():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+30000]
    assert "Attention Sphere" in snippet
    assert "seventh" in snippet.lower() or "7th" in snippet or "No matching podcast" in snippet

def test_everyone_hates_elon_holding():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+60000]
    assert "Everyone Hates Elon" in snippet
    assert "no new campaign" in snippet.lower()

def test_marketplace_quotes():
    txt = read(PODCAST)
    assert "didn't perform so well" in txt or "didn" in txt
    assert "pervert glasses" in txt.lower()

def test_shared_security_baseline():
    txt = read(PODCAST)
    assert "Privacy Problem With Meta" in txt or "Privacy Problem" in txt

def test_no_duplicate_ai2day_claim():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+30000]
    assert "duplicate prevention" in snippet.lower() or "Duplicate Prevention" in snippet

def test_mechanism_id_419():
    txt = read(ITER)
    assert "Mechanism ID" in txt or "mechanism" in txt.lower()
    assert "#419" in txt

def test_primary_sources_https():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+40000]
    urls = re.findall(r"https://[^\s\n]+", snippet)
    assert len(urls) >= 12, f"Need >=12 primary sources in #419 iteration-log, got {len(urls)}"

def test_iter_log_sources_verbatim():
    txt = read(ITER)
    idx419 = re.search(r"^#419 Type E:", txt, re.MULTILINE).start() if re.search(r"^#419 Type E:", txt, re.MULTILINE) else txt.find("#419")
    snippet = txt[idx419:idx419+40000]
    assert "https://www.marketplace.org/episode/2026/08/26/metas-push-to-make-their-smart-glasses-cool" in snippet
    assert "https://sharedsecurity.net/2026/03/16/" in snippet

def test_podcast_episode_numbers():
    txt = read(PODCAST)
    assert "### 125." in txt
    assert "### 126." in txt

