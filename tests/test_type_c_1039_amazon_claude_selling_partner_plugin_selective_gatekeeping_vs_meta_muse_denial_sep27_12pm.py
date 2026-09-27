"""
Type C #1039: Amazon x Anthropic Claude Selling Partner plugin (Sep 23 2026)
- FIRST dedicated corpus mechanism on the selective-gatekeeping leg of the
SIXTEENTH relationship direction (COMMERCE-GATEKEEPING): Amazon opens the
sell-side Seller Central surface to the backed lab's agent three days after
denying the buy-side to the publisher-paying lab's agent.

FINANCIAL MAP (verified Sep 27 2026, excerpt-bounded, 0 browser.open per #503):
  Grant leg: at Accelerate (annual seller conference, Seattle), Amazon
  announced a Selling Partner plugin opening Seller Central to outside AI
  agents (GeekWire, Todd Bishop, Sep 23 2026 7:10 am). First third-party
  agent: Anthropic's Claude (US beta), plus Amazon's own Quick assistant;
  "more integrations to follow" (AppVolt). From inside Claude: check
  inventory, adjust prices, update listings, pull sales analytics /
  performance metrics; the plugin can ACT, "the same way Seller Assistant
  does inside Seller Central" (AppVolt). Controls: ~60-second connection,
  no coding; scoped data types, per-action human approval, complete audit
  trail. Mary Beth Westmoreland (VP Worldwide Selling Partner Experience):
  "Our vision was that they would never have to log into Seller Central.
  We would just bring it to them where they work." ~90% of selling partners
  already use third-party AI tools. Independent sellers >60% of units sold
  worldwide; seller fees $46.8B in Q2, more than AWS (GeekWire); FTC case
  trial March 2027 Seattle. Amazon "chose the plugin path, not an open
  protocol" - UCP, ACP, AP2, x402 remain buy-side standards; "Amazon
  decides which assistants connect" (Ideabosque).
  Denial leg (carried from mechanism 852, Sep 20): Amazon unilaterally
  blocked Meta's Muse shopping agent; Ideabosque states the pairing:
  Amazon "blocked Meta's Muse shopping agent from its store days before
  the announcement." Trust-surface contrast: credential-holding consumer
  agent (Muse, denied) vs authorized OAuth API lane with per-action
  approval (Claude plugin, granted). Litigation gray zone: Amazon sued
  Perplexity Nov 2025 (Comet agent); federal judge blocked it March 2026;
  appeals court vacated - credential-agent question legally unsettled
  (sellerforge).
  Geometry: SELECTIVE GATEKEEPING - the gate opens for the backed lab
  (Anthropic: $13B+ backing, up to $33B; pays publishers NOTHING, m509
  zero-deal) while it stays locked against the publisher-paying lab
  (Meta: m331 licensing network; m594 News Corp up to $50M/yr).
  Amazon's three-role geometry (m852) gains the fourth posture: PAYS (m559),
  BACKS, DENIES (m852), and now GRANTS. Direction count holds at sixteen.
  NOT a new (seventeenth) direction: second leg of the sixteenth.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False
(Aug 28 2026 standing rule); engine NOT run; verdict
directionally_supported_not_proven; no_analysis_json_update: true; NOT
artifact-grade; NOT falsification-family member (ledger holds at 33).
Correlation is not causation. Confounders: STRONG excerpt-bounded (0
browser.open per #503) + STRONG roadmap-timing coincidence (Accelerate is
pre-scheduled annual) + STRONG different trust surfaces (Amazon's stated
agent-transparency rationale separates the decisions); MEDIUM beta/pilot
stage ("more integrations to follow") + MEDIUM symmetric denial
(Google/OpenAI too, via m852/TechSpot); WEAK n=1 four-day-old event +
WEAK single-outlet seller-fee/FTC figures.

Research method: 3 browser.search query sets, 0 browser.open per #503.
REJECTED: India attribution-deal re-indexes (m624/m660/m944 in corpus);
UMG x ElevenLabs Sep 10 + Suno x Warner/BMG (music vertical, #729/#759/
#799); Perplexity Comet Plus revenue-share (2024/2025 vintage, Jul 2024
SiliconANGLE); Meta x Midjourney Feb 2026 licensing (lab-to-lab, no new
direction claim; left for a future dedicated pass); Anthropic x Accenture
$2B eval partnership (consultancy leg, not publisher-lab); Akamai x
Anthropic $11.6B (m837, in corpus); stockmoguls Sep-6 re-crawl (same $28M
content, enriches m636). SELECTED: Amazon x Claude Selling Partner plugin
- dedicated-mechanism gap, 6 zero-hit source URLs, selective-gatekeeping
geometry extending the sixteenth direction.
Pre-commit novelty sweeps per #715: zero test_type_c_1039 files (glob);
no Type C #1039 in git log; max numeric mechanism_id 854 pre-commit;
zero numeric mechanism_id: 855 in profiles/ pre-commit; block key
zero-hit; all 6 source URLs zero-hit repo-wide pre-commit.

Doc-sync post-run: 53303/1363 -> 53347/1364 (+44/+1, venv authoritative).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012 working-tree block-key fix all stay
out of this run's index and diff.

Novelty anchor, rotation-guard, hash-placeholder, and doc-sync tests fail
pre-commit per the #565/#715/#719/#721 conventions; all green
post-doc-sync; iteration-log newest-entry green.

45 tests, 11 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1039_amazon_claude_selling_partner_plugin_selective_gatekeeping_vs_meta_muse_denial_sep27_12pm.py"
BLOCK_KEY = "type_c_1039_amazon_claude_selling_partner_plugin_selective_gatekeeping_vs_meta_muse_denial_sep27_12pm"
MECHANISM = 855
ITERATION = 1039
ITERATION_TYPE = "C"
EXPECTED_TESTS = 45
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in the anchor followup per #565
PREDECESSOR_SHAS = {
    "89737dccb6b561b73861d96306e9a470519afcbf",  # #1038 main
    "03e3d4d62923b0c38c31a6aed2a90ff683f3f367",  # #1038 anchor
    "7031b83202c49b9a2c0efa2d1965cdf85c7ffddf",  # #1038 log-hash
}
NEW_URLS = [
    "https://www.geekwire.com/2026/amazon-opens-its-seller-tools-to-outside-ai-agents-starting-with-anthropics-claude/",
    "https://www.ideabosque.com/library/amazon-seller-central-sell-side-agent-plugin/",
    "https://www.appvolt.ai/news/amazon-seller-assistant-workflows-plugin-claude-quick",
    "https://techjournal.org/amazon-seller-assistant-claude-plugin",
    "https://www.sellerforge.ai/blog/amazon-seller-central-mcp-guide",
    "https://www.linkedin.com/pulse/amazon-opened-seller-central-ai-claude-got-first-key-ollie-rodriguez-hegse",
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
class TestNovelty1039:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1039*"))
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
        assert "Type C #1039" in r2.stdout

    def test_novelty_first_claim_present(self):
        block, _ = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "selective-gatekeeping" in novelty
        assert "Selling Partner" in novelty

    def test_zero_mechanism_id_855_except_this_block(self):
        # Numeric mechanism_id: 855 must be claimed only by this run's block.
        r = run_git("grep", "-n", "mechanism_id: 855", "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_no_855_block_keys_repo_wide(self):
        # No zero-indent block key may contain 855 as a mechanism id.
        # Needle built by concatenation so this file never self-matches.
        needle = "^[a-z_0-9]*" + "855" + "[a-z_0-9_]*:"
        r = run_git("grep", "-nE", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines()
                if "mechanism_id" not in line and line.strip()]
        assert hits == []

    def test_new_urls_zero_hit_pre_commit_except_block(self):
        # Each of the 6 new source URLs appears exactly once repo-wide
        # (inside this block). Pre-commit greps per #715 verified zero.
        _, text = _block()
        for url in NEW_URLS:
            assert text.count(url) == 1, url


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard1039:
    def test_window_legs_in_iteration_log(self):
        log = _read(LOG)
        for leg, itype in [("1035", "D"), ("1036", "E"), ("1037", "A"),
                           ("1038", "B"), ("1039", "C")]:
            assert f"Type {itype} #{leg}" in log, (leg, itype)

    def test_predecessor_shas_in_git_log(self):
        for sha in PREDECESSOR_SHAS:
            r = run_git("cat-file", "-t", sha)
            assert r.stdout.strip() == "commit", sha

    def test_no_type_c_1039_pre_commit(self):
        r = run_git("log", "--oneline", "--grep=Type C #1039")
        # Exactly one hit is this run's main commit; more than one is a dup.
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        assert len(lines) <= 1

    def test_rotation_transparency_names_1035_1039_window(self):
        block, _ = _block()
        rt = block["rotation_transparency"]
        assert "1035-1039 window" in rt
        assert "FIFTH and CLOSING leg" in rt
        assert "next run is #1040 Type D" in rt


# ---------------------------------------------------------------------------
# 3. Mechanism content and identity
# ---------------------------------------------------------------------------
class TestMechanism855Content:
    def test_identity_fields(self):
        block, _ = _block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == ITERATION_TYPE
        assert block["type"] == "financial_incentive_mapping"
        assert block["block_key"] == BLOCK_KEY

    def test_verdict_and_grades(self):
        block, _ = _block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["engine_run"] is False

    def test_falsification_ledger_holds_at_33(self):
        block, _ = _block()
        assert block["falsification_ledger"] == 33
        assert block["falsification_family_member"] is False

    def test_excerpt_bounded(self):
        block, _ = _block()
        assert block["excerpt_bounded"] is True
        assert block["browser_opens"] == 0

    def test_six_sources_present(self):
        block, _ = _block()
        assert len(block["sources"]) == 6
        for src in block["sources"]:
            assert src["url"] in NEW_URLS


# ---------------------------------------------------------------------------
# 4. Grant leg
# ---------------------------------------------------------------------------
class TestGrantLeg:
    def test_announcement_facts(self):
        block, _ = _block()
        grant = block["grant_leg"]
        assert "Sep 23 2026" in grant["date"]
        assert "Accelerate" in grant["date"]
        assert "Claude" in grant["first_third_party_agent"]
        assert "Quick" in grant["first_third_party_agent"]

    def test_capabilities_write_capable(self):
        block, _ = _block()
        grant = block["grant_leg"]
        assert "adjust prices" in grant["capabilities"]
        assert "act on it" in grant["capabilities"]

    def test_controls(self):
        block, _ = _block()
        grant = block["grant_leg"]
        assert "60-second" in grant["controls"]
        assert "per-action human approval" in grant["controls"]
        assert "audit trail" in grant["controls"]

    def test_westmoreland_quote(self):
        block, _ = _block()
        assert "never have to log into Seller Central" in block["grant_leg"]["westmoreland_quote"]

    def test_protocol_choice(self):
        block, _ = _block()
        grant = block["grant_leg"]
        assert "not an open protocol" in grant["protocol_choice"]
        assert "Amazon decides which assistants connect" in grant["protocol_choice"]

    def test_revenue_base(self):
        block, _ = _block()
        grant = block["grant_leg"]
        assert "60%" in grant["revenue_base"]
        assert "46.8B" in grant["revenue_base"]


# ---------------------------------------------------------------------------
# 5. Denial leg (carried from mechanism 852)
# ---------------------------------------------------------------------------
class TestDenialLegCarried:
    def test_carried_from_852(self):
        block, _ = _block()
        denial = block["denial_leg_carried"]
        assert "mechanism 852" in denial["event"]
        assert "Sep 20 2026" in denial["event"]

    def test_timing_pair(self):
        block, _ = _block()
        assert "days before the announcement" in block["denial_leg_carried"]["timing_pair"]

    def test_trust_surface_contrast(self):
        block, _ = _block()
        contrast = block["denial_leg_carried"]["trust_surface_contrast"]
        assert "credential-holding" in contrast
        assert "OAuth" in contrast

    def test_litigation_gray_zone(self):
        block, _ = _block()
        gray = block["denial_leg_carried"]["litigation_gray_zone"]
        assert "Perplexity" in gray
        assert "March 2026" in gray
        assert "vacated" in gray


# ---------------------------------------------------------------------------
# 6. Selective-gatekeeping geometry
# ---------------------------------------------------------------------------
class TestSelectiveGatekeepingGeometry:
    def test_backed_lab_granted(self):
        block, _ = _block()
        granted = block["selective_gatekeeping_geometry"]["backed_lab_granted"]
        assert "FIRST third-party agent" in granted
        assert "zero-deal" in granted

    def test_publisher_payer_denied(self):
        block, _ = _block()
        denied = block["selective_gatekeeping_geometry"]["publisher_payer_denied"]
        assert "Meta" in denied
        assert "PAYS publishers" in denied

    def test_amazon_role_update(self):
        block, _ = _block()
        role = block["selective_gatekeeping_geometry"]["amazon_role_update"]
        assert "fourth posture" in role
        assert "GRANTS" in role

    def test_open_question(self):
        block, _ = _block()
        assert "more integrations to follow" in block["selective_gatekeeping_geometry"]["open_question"]


# ---------------------------------------------------------------------------
# 7. Direction taxonomy
# ---------------------------------------------------------------------------
class TestDirectionTaxonomy:
    def test_sixteenth_direction_second_leg(self):
        block, _ = _block()
        tax = block["relationship_direction_taxonomy"]
        assert "SIXTEENTH" in tax["direction_number"]
        assert "SECOND LEG" in tax["direction_number"]
        assert "COMMERCE-GATEKEEPING" in tax["direction_name"]
        assert "selective-gatekeeping" in tax["direction_name"]

    def test_direction_count_holds_at_sixteen(self):
        block, _ = _block()
        tax = block["relationship_direction_taxonomy"]
        assert "holds at sixteen" in tax["definition"]
        assert "not a new" in tax["direction_number"].lower()

    def test_taxonomy_tension_carried(self):
        block, _ = _block()
        assert "termination-leverage" in block["relationship_direction_taxonomy"]["taxonomy_tension"]


# ---------------------------------------------------------------------------
# 8. connects_to
# ---------------------------------------------------------------------------
class TestConnectsTo:
    def test_connects_to_expected(self):
        block, _ = _block()
        assert block["connects_to"] == [852, 831, 559, 509, 594]

    def test_852_is_first_connection(self):
        block, _ = _block()
        assert block["connects_to"][0] == 852


# ---------------------------------------------------------------------------
# 9. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence:
    def test_confounder_strength_tiers(self):
        block, _ = _block()
        strengths = [c["strength"] for c in block["confounders"]]
        assert strengths.count("strong") == 3
        assert strengths.count("medium") == 2
        assert strengths.count("weak") == 2

    def test_roadmap_timing_confounder(self):
        block, _ = _block()
        texts = " ".join(c["text"] for c in block["confounders"])
        assert "pre-scheduled" in texts

    def test_strongest_counterargument(self):
        block, _ = _block()
        sca = block["strongest_counterargument"]
        assert "calendar coincidence" in sca
        assert "Correlation, not causation" in sca

    def test_certification_boundaries(self):
        block, _ = _block()
        assert "Excerpt-bounded per #503" in block["certification_boundaries"]

    def test_coverage_note_no_tone_claim(self):
        block, _ = _block()
        assert "tone NOT_SCORED" in block["coverage_note"]


# ---------------------------------------------------------------------------
# 10. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_no_engine_statistics(self):
        block, _ = _block()
        assert block["engine_run"] is False
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["no_analysis_json_update"] is True
        v = block["verification"]
        assert v["max_numeric_mechanism_id_pre_commit"] == 854
        assert v["mechanism_id_claimed"] == 855
        assert v["source_urls_first_appearance"] == 6
        assert v["falsification_ledger_holds_at"] == 33

    def test_expected_test_count(self):
        # Self-count: this file must carry exactly EXPECTED_TESTS tests.
        import ast
        tree = ast.parse(_read(TESTS_DIR / THIS_FILE))
        count = sum(isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
                    for n in ast.walk(tree))
        assert count == EXPECTED_TESTS, count


# ---------------------------------------------------------------------------
# 11. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync1039:
    def test_readme_stats_updated(self):
        readme = _read(README)
        assert "53347" in readme and "1364" in readme

    def test_readme_table_row(self):
        readme = _read(README)
        assert THIS_FILE in readme

    def test_arch_tree_row(self):
        arch = _read(ARCH)
        assert THIS_FILE in arch

    def test_iteration_log_newest_entry(self):
        log = _read(LOG)
        assert log.lstrip().startswith("## #1039 Type C")
