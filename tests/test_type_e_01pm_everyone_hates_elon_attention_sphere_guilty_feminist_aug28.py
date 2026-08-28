"""
Type E Aug 28 13:00 PT — Everyone Hates Elon / Attention Sphere / Guilty Feminist audit
Mechanism #360 — Podcast Sentiment Asymmetry Aug 28
- EHE is activist group not podcast, campaign evidence, source URLs HTTPS
- No new Aug 28 campaign beyond July coverage (dual verification)
- Vocabulary cluster 3 independent sources
- Attention Sphere no-show dual verification
- Guilty Feminist Aug 2026 slate 5 episodes existence, zero tech episodes, audience metrics
- No significance claim, causal caution
- NBC News gendered entry
- Blood in the Machine still most recent Pervert Glasses podcast
- Cross-medium alignment qualitative
"""
import os, re, yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
POD = ROOT / "podcast-sentiment.md"
YAML = ROOT / "profiles" / "competitor-entities.yaml"

def read_pod():
    return POD.read_text(encoding="utf-8", errors="ignore")

def test_ehe_activist_group_status():
    txt = read_pod()
    assert "Everyone Hates Elon" in txt
    # activist group not podcast
    assert "activist group" in txt.lower()
    assert "NOT a podcast" in txt or "not a podcast" in txt.lower()

def test_ehe_campaign_evidence():
    txt = read_pod()
    # quotes from Engadget
    assert "pervert technology since trench coat" in txt.lower() or "pervert technology" in txt.lower()
    assert "We're always watching" in txt or "always watching" in txt.lower()
    # Epstein poster
    assert "Glasses for people who don't do consent" in txt or "Epstein" in txt

def test_ehe_source_urls_https():
    txt = read_pod()
    # check 5 EHE URLs present and HTTPS
    urls = [
        "https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/",
        "https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5",
        "https://singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
        "https://community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
        "https://petapixel.com/2026/07/15/fake-ads-for-meta-ai-glasses-featuring-jeff-bezos-epstein-plastered-around-london/"
    ]
    for u in urls:
        assert u in txt, f"missing EHE URL {u}"
        assert u.startswith("https://") or u.startswith("HTTPS://") or u.lower().startswith("https://")

def test_no_new_aug28_campaign():
    txt = read_pod()
    assert "No new Aug 28 campaign" in txt or "no new Aug 28 campaign" in txt.lower()
    assert "37 days since Samsung" in txt or "37 days" in txt
    # dual verification
    assert "2 independent searches" in txt or "dual verification" in txt.lower() or "Aug 28 07:00 + 13:00" in txt

def test_vocabulary_cluster_3_sources():
    txt = read_pod()
    # 3 independent source groups
    assert "AmberMac Ep056" in txt or "AmberMac" in txt
    assert "Blood in the Machine" in txt
    assert "EHE" in txt
    # exclusive targeting
    assert "0 competitor" in txt.lower() or "0% competitor" in txt or "exclusive Meta targeting" in txt.lower() or "exclusive Meta" in txt

def test_attention_sphere_no_show_dual():
    txt = read_pod()
    assert "Attention Sphere" in txt
    assert "No matching podcast" in txt or "No result" in txt
    # dual verification Aug 28 07:00 + 13:00
    assert "2 independent searches" in txt or "Aug 28 07:00" in txt
    # misidentified
    assert "misidentified" in txt.lower()
    assert "Left to Their Own Devices" in txt

def test_guilty_feminist_slate_episodes():
    txt = read_pod()
    # 5 episodes
    assert "#494" in txt and "Ventnor Fringe" in txt
    assert "#495" in txt and "Architecture of Autocracy" in txt
    assert "#496" in txt and "Intimacy" in txt
    assert "#497" in txt and "Nuance Drought" in txt
    assert "Wilderness Festival" in txt

def test_guilty_feminist_zero_tech():
    txt = read_pod()
    assert "ZERO episodes about Meta" in txt or "0 tech episodes" in txt.lower() or "zero tech episodes" in txt.lower()
    assert "No claim of statistical significance" in txt or "no significance claim" in txt.lower() or "No significance claim" in txt

def test_guilty_feminist_audience_metrics():
    txt = read_pod()
    assert "724 episodes" in txt
    assert "TOP 0.01%" in txt or "TOP 0.01" in txt
    assert "41.38% US" in txt or "41.38%" in txt
    assert "22.66% GB" in txt or "22.66%" in txt

def test_nbc_gendered_entry():
    txt = read_pod()
    assert "NBC News" in txt
    assert "Fears grow over privacy" in txt
    assert "mostly women speak out" in txt.lower() or "mostly women" in txt.lower()
    assert "Yasmin Vossoughian" in txt

def test_blood_in_machine_most_recent():
    txt = read_pod()
    assert "Blood in the Machine" in txt
    assert "Pervert Glasses" in txt
    assert "most recent podcast" in txt.lower() or "most recent" in txt.lower()

def test_causal_caution_and_methodology():
    txt = read_pod()
    # causal caution required
    assert "Causal caution" in txt or "Correlation does not prove causation" in txt or "correlation does not prove" in txt.lower()
    # methodology limits — no invented quotes/timestamps without source
    assert "search-limited" in txt.lower() or "Search-limited methodology" in txt
    # financial predictor vs cultural consensus distinction
    assert "financial predictor" in txt.lower() or "Financial predictor" in txt
