"""
Type C #1034: Amazon x Meta Muse agentic-commerce denial (Sep 20 2026) +
Meta x Shopify agentic-checkout deal (Sep 21/22 2026) - FIRST dedicated
corpus mechanism on the agentic-commerce licensing split; SIXTEENTH
relationship direction per the m807 enumeration (COMMERCE-GATEKEEPING,
access-denial as licensing leverage).

FINANCIAL MAP (verified Sep 2026, excerpt-bounded, 0 browser.open per #503):
  Denial leg: Amazon unilaterally blocked Meta's Muse personal AI agent
  (launched US Sep 8 2026 with Muse Spark model; #1 US app stores within a
  week, 2.5M+ downloads) from shopping on Amazon.com on Sep 20 2026.
  Popup: "continued access by an unauthorized AI agent violates Amazon's
  Conditions of Use". Objections: no permission requested; no
  self-identification while browsing; credential capture/storage claims.
  Amazon asked Meta to exclude Amazon from Muse; Meta declined (TechSpot).
  Amazon plans to block Google and OpenAI agents too (TechSpot).
  Deal leg: Shopify CEO Tobi Lutke Monday: "partnering deeply with Muse
  to enable agentic checkout with Shop Pay on all Shopify stores";
  Shopify +15% in two days to $147.74; paid per checkout.
  Muse commerce stack: Stripe Link (300M+ methods, 1M+ businesses),
  Shopify Shop Pay, PayPal via Mastercard Agent Pay, Expedia, Instacart
  (Azoma/GlobeNewswire). Muse business model: free tokens, "small fee
  from transactions" (Zuckerberg at Connect); $20/$100 tiers + merchant
  fee (memeburn).
  Geometry: m831's commerce-conversion direction (11th) gains (a) a
  second-lab replication - Meta x Shopify, the payer lab taking the
  merchant fee itself; and (b) the enforcement mirror - Amazon's denial
  converts the ABSENCE of a deal into an enforceable access exclusion.
  Amazon's three-role geometry completes: PAYS publishers (NYT,
  Conde Nast, Hearst Rufus/Alexa - m559), BACKS zero-deal labs
  (Anthropic $13B+ up to $33B; OpenAI $50B), DENIES rival lab's agent.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False
(Aug 28 2026 standing rule); engine NOT run; verdict
directionally_supported_not_proven; no_analysis_json_update: true; NOT
artifact-grade; NOT falsification-family member (ledger holds at 31).
Correlation is not causation. Confounders: STRONG excerpt-bounded (0
browser.open per #503) + STRONG platform-economics reading (Ben
Thompson: Amazon protecting e-commerce UI position) + STRONG symmetric
denial (Google/OpenAI too, cuts both ways); MEDIUM Meta non-cooperation
+ MEDIUM credential-claim dispute + MEDIUM Shopify paid deal; WEAK n=1
event + WEAK launch-scale inflation risk.

Research method: 2 browser.search query sets, 0 browser.open per #503.
REJECTED: Meta Connect hardware (Muse Charm, camera-free glasses - not
financial-incentive); Disney IMAX Enhanced VR (hardware content bundle,
not publisher-lab); Meta x News Corp $150M (in corpus via m594); NYT
$28M litigation costs (stockmoguls Sep 6 - enriches m636, no dedicated
mechanism); Anthropic settlement claims dispute (TechCrunch Sep 6 -
publisher-vs-author, not lab-publisher). SELECTED: Amazon x Meta Muse
agentic-commerce denial + Meta x Shopify commerce-conversion
counterpart - dedicated-mechanism gap, 8 zero-hit source URLs,
sixteenth-direction geometry.
Pre-commit novelty sweeps per #715: zero test_type_c_1034 files (glob);
no Type C #1034 in git log; max numeric mechanism_id 851 pre-commit;
zero numeric mechanism_id: 852 in profiles/ pre-commit; block key
zero-hit; all 8 source URLs zero-hit repo-wide pre-commit.

Doc-sync post-run: 53056/1358 -> 53114/1359 (+58/+1, venv authoritative).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012 working-tree block-key fix all stay
out of this run's index and diff.

Novelty anchor, rotation-guard, hash-placeholder, and doc-sync tests fail
pre-commit per the #565/#715/#719/#721 conventions; all green
post-doc-sync; iteration-log newest-entry green.

58 tests, 11 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1034_amazon_meta_muse_agentic_commerce_denial_shopify_shop_pay_commerce_conversion_sixteenth_direction_sep27_7am.py"
BLOCK_KEY = "type_c_1034_amazon_meta_muse_agentic_commerce_denial_shopify_shop_pay_commerce_conversion_sixteenth_direction_sep27_7am"
MECHANISM = 852
ITERATION = 1034
ITERATION_TYPE = "C"
EXPECTED_TESTS = 58
ANCHORED_SHA = "5df0bd19b01927b375d7e014d6536f9677d379b6"  # patched in the anchor followup per #565
PREDECESSOR_SHAS = {
    "8b58e3c438caf4ce43fef3a58f4258984909d4ff",  # #1033 main
    "f1bdcdd327fcfa34684ecd557ebe060257cb74a2",  # #1033 anchor
    "aa98f70f9a15c6f3a3687e8eaf258873c30fa2e4",  # #1033 log-hash
}
NEW_URLS = [
    "https://WWW.FOOL.COM/investing/2026/09/23/amazon-blocked-meta-s-ai-shopping-agent-shopify-welcomed-it-and-gets-paid-on-every-checkout/",
    "https://www.thetimes.com/us/news-today/article/muse-ai-app-meta-shopping-amazon-7xlckg53b",
    "https://www.techspot.com/news/113981-amazon-blocked-meta-muse-agentic-ai-shopping-service.html",
    "https://developmentstoday.com/news/amazon-blocks-meta-muse-ai-agent-shopping",
    "https://www.androidheadlines.com/2026/09/amazon-blocks-meta-muse-ai-agent-shopping.html",
    "https://www.globenewswire.com/news-release/2026/09/24/3368168/0/en/what-tools-help-brands-optimize-for-meta-muse-azoma-sets-out-how-brands-get-recommended-by-meta-s-ai-shopping-agent.html",
    "https://chatmaxima.com/blog/meta-muse-ai-agent-businesses-whatsapp-messenger/",
    "https://memeburn.com/meta-connect-2026-recap-every-new-device-is-a-door-into-muse/",
]

REPO = Path(__file__).resolve().parents[1]
TESTS_DIR = REPO / "tests"
PROFILE = REPO / "profiles" / "competitor-entities.yaml"
LOG = REPO / "iteration-log.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"


def _read(path):
    return Path(path).read_text(encoding="utf-8")


def run_git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO)] + list(args),
        capture_output=True, text=True, timeout=60,
    )


def _block():
    data = yaml.safe_load(_read(PROFILE))
    assert BLOCK_KEY in data, "block key missing from competitor-entities.yaml"
    return data[BLOCK_KEY], _read(PROFILE)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1034:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1034*"))
        assert len(matches) == 1
        assert matches[0].name == THIS_FILE

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # Fails pre-anchor by design; passes after the anchor followup per
        # #565: the committed test must carry the real main-commit SHA.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #1034" in r2.stdout

    def test_novelty_first_claim_present(self):
        block, _ = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "commerce-gatekeeping" in novelty
        assert "agentic-commerce licensing split" in novelty

    def test_zero_mechanism_id_852_except_this_block(self):
        # Numeric mechanism_id: 852 must be claimed only by this run's block.
        r = run_git("grep", "-n", "mechanism_id: 852", "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_no_852_block_keys_repo_wide(self):
        # No zero-indent block key may contain 852 as a mechanism id.
        # Needle built by concatenation so this file never self-matches.
        needle = "^[a-z_0-9]*" + "852" + "[a-z_0-9_]*:"
        r = run_git("grep", "-nE", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines()
                if "mechanism_id" not in line and line.strip()]
        assert hits == []

    def test_new_urls_zero_hit_pre_commit_except_block(self):
        # Each of the 8 new source URLs appears exactly once repo-wide
        # (inside this block). Pre-commit greps per #715 verified zero.
        _, text = _block()
        for url in NEW_URLS:
            assert text.count(url) == 1, url


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard1034:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1030 Type D" in text
        assert "## #1031 Type E" in text
        assert "## #1032 Type A" in text
        assert "## #1033 Type B" in text
        assert "1030-1034" in text

    @pytest.mark.rotation
    def test_fifth_leg_of_1030_to_1034_window(self):
        block, _ = _block()
        assert "FIFTH and CLOSING leg of the 1030-1034 window" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1033_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1033")
        assert "Type B #1033" in r.stdout
        block, _ = _block()
        rt = block["rotation_transparency"]
        assert "Aditya Soni" in rt
        assert "mechanism 851" in rt
        for sha in PREDECESSOR_SHAS:
            rr = run_git("cat-file", "-t", sha)
            assert rr.stdout.strip() == "commit", sha

    @pytest.mark.rotation
    def test_no_successor_1035_type_d_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type D #1035")
        assert "Type D #1035" not in r.stdout

    @pytest.mark.rotation
    def test_no_concurrent_type_c_1034_by_commit_time(self):
        # Own commits (touching this test file) are excluded per the #1018
        # convention: the guard is about a racing iteration, not this run.
        r = run_git("log", "--format=%H %s", "--grep", "Type C #1034")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [
            line for line in matches
            if line.split()[0] not in own
        ]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 852 block content
# ---------------------------------------------------------------------------
class TestMechanism852Content:
    def test_block_key_unique_at_zero_indent(self):
        _, text = _block()
        lines = [l for l in text.splitlines() if l.startswith(BLOCK_KEY + ":")]
        assert len(lines) == 1

    def test_mechanism_id_and_iteration_fields(self):
        block, _ = _block()
        assert block["mechanism_id"] == 852
        assert block["iteration"] == 1034
        assert block["iteration_type"] == "C"
        assert block["type"] == "financial_incentive_mapping"
        assert block["date_analyzed"] == "2026-09-27"
        assert block["time_pdt"] == "07:00"

    def test_type_c_financial_mapping_fields(self):
        block, _ = _block()
        assert block["type_label"] == "Financial Incentive Mapping"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"
        assert "COMMERCE-GATEKEEPING" in block["mechanism_name"]

    def test_researcher_author_attribution(self):
        block, _ = _block()
        assert block["researcher"] == "Kit (with Ray)"
        assert block["author"] == "Kit (with Ray)"

    def test_verification_fields(self):
        block, _ = _block()
        v = block["verification"]
        assert v["max_numeric_mechanism_id_pre_commit"] == 851
        assert v["mechanism_id_claimed"] == 852
        assert v["source_urls_first_appearance"] == 8
        assert v["search_sets"] == 2
        assert v["falsification_ledger_holds_at"] == 31
        assert v["browser_opens"] == 0

    def test_ascii_only_block(self):
        _, text = _block()
        start = text.index(BLOCK_KEY)
        nxt = text.find("\ntype_c_", start + len(BLOCK_KEY))
        block_text = text[start:] if nxt == -1 else text[start:nxt]
        assert all(ord(c) < 128 for c in block_text)
        assert "\u2014" not in block_text


# ---------------------------------------------------------------------------
# 4. Denial leg
# ---------------------------------------------------------------------------
class TestDenialLeg:
    def test_denial_date_sep_20(self):
        block, _ = _block()
        d = block["denial_leg"]
        assert "Sep 20 2026" in d["date"]

    def test_popup_text(self):
        block, _ = _block()
        d = block["denial_leg"]
        assert "unauthorized AI agent violates Amazon" in d["popup_text"]
        assert "Conditions of Use" in d["popup_text"]

    def test_amazon_objections(self):
        block, _ = _block()
        d = block["denial_leg"]
        objs = " ".join(d["objections"])
        assert "never requested permission" in objs
        assert "does not identify itself" in objs
        assert "credentials" in objs

    def test_meta_declined_exclusion(self):
        block, _ = _block()
        d = block["denial_leg"]
        assert "declined" in d["meta_decline"]
        assert "TechSpot" in d["meta_decline"]

    def test_spokesperson_quote(self):
        block, _ = _block()
        _, text = _block()
        assert "operate openly and respect service provider decisions" in text

    def test_generalization_to_google_openai(self):
        block, _ = _block()
        d = block["denial_leg"]
        assert "Google" in d["generalization"]
        assert "OpenAI" in d["generalization"]

    def test_credential_dispute_noted(self):
        block, _ = _block()
        d = block["denial_leg"]
        assert "disputes" in d["credential_dispute"]
        assert "secure virtual machines" in d["credential_dispute"]

# ---------------------------------------------------------------------------
# 5. Deal leg
# ---------------------------------------------------------------------------
class TestDealLeg:
    def test_lutke_quote(self):
        block, _ = _block()
        d = block["deal_leg"]
        assert "partnering deeply with Muse" in d["lutke_quote"]
        assert "Shop Pay" in d["lutke_quote"]
        assert "Tobi Lutke" in d["lutke_quote"]

    def test_shop_pay_all_stores(self):
        block, _ = _block()
        assert "all Shopify stores" in _read(PROFILE)

    def test_market_reaction(self):
        block, _ = _block()
        d = block["deal_leg"]
        assert "147.74" in d["market_reaction"]
        assert "15%" in d["market_reaction"]

    def test_paid_per_checkout(self):
        block, _ = _block()
        d = block["deal_leg"]
        assert "checkout" in d["consideration"]
        assert "Paid" in d["consideration"]

    def test_second_lab_replication_of_m831(self):
        block, _ = _block()
        d = block["deal_leg"]
        assert "m831" in d["geometry"]
        assert "merchant fee" in d["geometry"]


# ---------------------------------------------------------------------------
# 6. Muse commerce stack
# ---------------------------------------------------------------------------
class TestMuseCommerceStack:
    def test_muse_launch_sep_8(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        assert "Sep 8 2026" in s["launch"]
        assert "Muse Spark" in s["launch"]

    def test_launch_scale(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        assert "2.5M+" in s["launch_scale"]
        assert "number one" in s["launch_scale"].lower() or "#1" in s["launch_scale"]

    def test_commerce_stack_members(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        stack = " ".join(s["stack"])
        assert "Stripe Link" in stack
        assert "Shop Pay" in stack
        assert "PayPal" in stack
        assert "Expedia" in stack
        assert "Instacart" in stack

    def test_stripe_protections(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        assert "first AI agent" in s["stripe_protections"]
        assert "purchase protections" in s["stripe_protections"]

    def test_business_model(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        assert "small fee from transactions" in s["business_model"]
        assert "$20" in s["business_model"]

    def test_meta_deals_stripe_shopify(self):
        block, _ = _block()
        s = block["muse_commerce_stack"]
        assert "Stripe" in s["meta_deals"]
        assert "Shopify" in s["meta_deals"]


# ---------------------------------------------------------------------------
# 7. Direction taxonomy
# ---------------------------------------------------------------------------
class TestDirectionTaxonomy:
    def test_sixteenth_direction_number(self):
        block, _ = _block()
        t = block["relationship_direction_taxonomy"]
        assert "SIXTEENTH" in t["direction_number"]

    def test_direction_name_commerce_gatekeeping(self):
        block, _ = _block()
        t = block["relationship_direction_taxonomy"]
        assert "COMMERCE-GATEKEEPING" in t["direction_name"]
        assert "access-denial as licensing leverage" in t["direction_name"]

    def test_prior_directions_enumerated(self):
        block, _ = _block()
        t = block["relationship_direction_taxonomy"]
        priors = t["prior_directions"]
        for tag in ["sue-then-sign", "commerce-conversion (m831)",
                    "publisher-traffic-gate (m828)", "ecosystem-grant (m849)"]:
            assert tag in priors, tag
        assert priors.count(")") == 15

    def test_taxonomy_tension_carried(self):
        block, _ = _block()
        t = block["relationship_direction_taxonomy"]
        assert "m737" in t["taxonomy_tension"]
        assert "termination-leverage" in t["taxonomy_tension"]

    def test_shopify_leg_extends_eleventh_not_new(self):
        block, _ = _block()
        t = block["relationship_direction_taxonomy"]
        assert "second-lab replication of the 11th direction" in t["definition"]
        assert "not a new direction itself" in t["definition"]

    def test_amazon_three_role_geometry(self):
        block, _ = _block()
        g = block["amazon_three_role_geometry"]
        assert "PAYS publishers" in g["role_1_payer"]
        assert "Anthropic" in g["role_2_backer"]
        assert "DENIES" in g["role_3_gatekeeper"]
        assert "Stratechery" in g["structural_reading"]


# ---------------------------------------------------------------------------
# 8. Connects-to links
# ---------------------------------------------------------------------------
class TestConnectsTo:
    def test_connects_to_list(self):
        block, _ = _block()
        assert block["connects_to"] == [831, 849, 559, 594, 509]

    def test_m831_commerce_conversion_origin(self):
        block, _ = _block()
        assert 831 in block["connects_to"]
        _, text = _block()
        assert "m831" in text

    def test_m849_predecessor_link(self):
        block, _ = _block()
        assert 849 in block["connects_to"]
        assert "ecosystem-grant" in _read(PROFILE)


# ---------------------------------------------------------------------------
# 9. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence:
    def test_confounder_strengths_ranked(self):
        block, _ = _block()
        confs = block["confounders"]
        assert len(confs) == 8
        strengths = [c["strength"] for c in confs]
        assert strengths == [
            "strong", "strong", "strong",
            "medium", "medium", "medium",
            "weak", "weak",
        ]

    def test_platform_economics_confounder(self):
        block, _ = _block()
        text = " ".join(c["text"] for c in block["confounders"])
        assert "Ben Thompson" in text
        assert "primary e-commerce user interface" in text

    def test_symmetric_denial_confounder(self):
        block, _ = _block()
        text = " ".join(c["text"] for c in block["confounders"])
        assert "block Google and OpenAI agents too" in text
        assert "cuts both ways" in text

    def test_counterevidence_present(self):
        block, _ = _block()
        ce = block["counterevidence"]
        assert len(ce) == 4
        joined = " ".join(ce)
        assert "symmetric platform policy" in joined
        assert "tollbooth" in joined
        assert "WHO collects the agent-commerce toll" in joined

    def test_strongest_counterargument(self):
        block, _ = _block()
        sca = block["strongest_counterargument"]
        assert "one-week platform spat" in sca
        assert "earns its keep only if the denial persists or replicates" in sca
        assert "Correlation, not causation" in sca


# ---------------------------------------------------------------------------
# 10. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_tone_not_scored(self):
        block, _ = _block()
        assert block["tone_scores"] == "NOT_SCORED"

    def test_engine_not_run(self):
        block, _ = _block()
        assert block["engine_run"] is False
        assert block["no_analysis_json_update"] is True

    def test_falsification_ledger_holds_at_31(self):
        block, _ = _block()
        assert block["falsification_ledger"] == 31
        assert block["falsification_family_member"] is False

    def test_not_artifact_grade(self):
        block, _ = _block()
        assert block["artifact_grade"] is False

    def test_verdict_and_no_analysis_json_update(self):
        block, _ = _block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["coverage_note"].startswith("No editorial-tone claim")


# ---------------------------------------------------------------------------
# 11. Doc sync
# ---------------------------------------------------------------------------
class TestDocSync1034:
    def test_readme_stats_updated(self):
        text = _read(README)
        assert "53114" in text
        assert "1359" in text

    def test_readme_test_table_row(self):
        text = _read(README)
        assert "Type C #1034" in text
        assert "COMMERCE-GATEKEEPING" in text
        assert THIS_FILE in text

    def test_architecture_tree_row(self):
        text = _read(ARCH)
        assert THIS_FILE in text
        assert "Type C #1034" in text

    def test_iteration_log_newest_entry(self):
        text = _read(LOG)
        first = next(l for l in text.splitlines() if l.startswith("## #"))
        assert first.startswith("## #1034 Type C")
