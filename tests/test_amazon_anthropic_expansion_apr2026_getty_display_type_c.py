"""
Iteration #361 Type C — Amazon Apr 20 2026 Anthropic Expansion Mirroring OpenAI + Getty Display-Only Deal

Validates financial incentive mapping updates for Amazon dual-lab closed loop and OpenAI visual licensing.

Source URLs required:
- https://www.geekwire.com/2026/amazon-doubles-down-on-anthropic-with-25b-investment-mirroring-its-openai-cloud-deal/
- https://techcrunch.com/2026/04/20/anthropic-takes-5b-from-amazon-and-pledges-100b-in-cloud-spending-in-return/
- https://www.tradingview.com/news/marketbeat:6504963f6094b:0-getty-images-openai-deal-gives-the-stock-a-new-ai-licensing-story/
- https://www.barchart.com/story/news/3000014/getty-images-openai-deal-gives-the-stock-a-new-ai-licensing-story

No em dash anywhere.
"""
import yaml
import pathlib
import json

PROFILE_PATH = pathlib.Path("~/workspace/repos/mediascope/profiles/competitor-entities.yaml").expanduser()

def load_profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # support both flat and nested under entities
    if "entities" in data:
        return data["entities"]
    return data

def test_profile_loads():
    data = load_profile()
    assert "amazon" in data
    assert "openai" in data

def test_amazon_anthropic_expansion_fields():
    data = load_profile()
    amazon = data["amazon"]
    # find anthropic_investment layer
    layers = amazon.get("sextuple_publisher_leverage", {}).get("layers", [])
    anth_layer = None
    for l in layers:
        if l.get("name") == "anthropic_investment":
            anth_layer = l
            break
    assert anth_layer is not None, "anthropic_investment layer missing"
    detail = anth_layer.get("detail", "")
    # Must mention mirroring OpenAI, 5GW, $100B, milestone
    assert "mirrors" in detail.lower() or "mirroring" in detail.lower()
    assert "5GW" in detail or "5 GW" in detail or "5GW" in detail.replace(" ", "")
    assert "$100B" in detail or "100B" in detail
    assert anth_layer.get("anthropic_total_invested_b") == 13
    assert anth_layer.get("anthropic_potential_total_b") == 33
    assert anth_layer.get("anthropic_apr_2026_fresh_b") == 5
    assert anth_layer.get("anthropic_milestone_additional_b") == 20
    assert anth_layer.get("anthropic_aws_commitment_b") == 100
    assert anth_layer.get("anthropic_trainium_gw") == 5
    assert anth_layer.get("anthropic_openai_mirroring") is True
    # source URLs include required domains
    urls = anth_layer.get("source_urls", [])
    urls_str = " ".join(urls)
    assert "geekwire.com" in urls_str
    assert "techcrunch.com" in urls_str

def test_amazon_detail_no_em_dash():
    data = load_profile()
    layers = data["amazon"]["sextuple_publisher_leverage"]["layers"]
    for l in layers:
        if l["name"] == "anthropic_investment":
            detail = l.get("detail", "")
            assert "—" not in detail, "em dash found in anthropic_investment detail"
            assert "–" not in detail, "en dash found — use hyphen per project rule (no em dash)"

def test_openai_getty_display_deal():
    data = load_profile()
    openai = data["openai"]
    portfolio = openai.get("publisher_content_deal_portfolio", {})
    td = portfolio.get("total_deals")
    assert (isinstance(td, int) and td >= 24) or ("24" in str(td))
    partners = portfolio.get("notable_partners", [])
    partners_str = " ".join(partners)
    assert "Getty Images" in partners_str
    assert "display" in partners_str.lower()
    # getty sub-block
    getty = portfolio.get("getty_images_display_deal_jun2026")
    assert getty is not None, "getty_images_display_deal_jun2026 missing"
    assert getty.get("structure", "").lower().find("display-only") != -1 or "display-only" in getty.get("structure", "").lower()
    assert "NO model training" in getty.get("structure", "") or "no model training" in getty.get("structure", "").lower() or "NO training" in getty.get("structure", "")
    # source URLs
    src = getty.get("source_urls", [])
    src_str = " ".join(src)
    assert "tradingview.com" in src_str or "barchart.com" in src_str
    # check prices
    assert getty.get("low_price") == 0.58
    assert getty.get("rally_price") == 1.29

def test_openai_getty_no_em_dash():
    data = load_profile()
    getty = data["openai"]["publisher_content_deal_portfolio"]["getty_images_display_deal_jun2026"]
    dumped = json.dumps(getty, ensure_ascii=False)
    assert "—" not in dumped

def test_source_urls_https():
    data = load_profile()
    anth_urls = None
    for l in data["amazon"]["sextuple_publisher_leverage"]["layers"]:
        if l["name"] == "anthropic_investment":
            anth_urls = l.get("source_urls", [])
    for url in anth_urls:
        assert url.startswith("https://"), f"URL must be https: {url}"
    getty_urls = data["openai"]["publisher_content_deal_portfolio"]["getty_images_display_deal_jun2026"]["source_urls"]
    for url in getty_urls:
        assert url.startswith("https://"), f"Getty URL must be https: {url}"

def test_amazon_dual_lab_financial_mechanism():
    """Verify dual-lab $63B closed loop logic is described."""
    data = load_profile()
    # Check openai_investment layer still present
    layers = data["amazon"]["sextuple_publisher_leverage"]["layers"]
    names = [l["name"] for l in layers]
    assert "openai_investment" in names
    assert "anthropic_investment" in names
    # Verify anthropic detail mentions both sides profit
    anth_detail = [l for l in layers if l["name"] == "anthropic_investment"][0]["detail"]
    assert "both sides" in anth_detail.lower() or "both" in anth_detail.lower()
