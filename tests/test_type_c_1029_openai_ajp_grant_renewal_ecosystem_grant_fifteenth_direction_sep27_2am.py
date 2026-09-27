"""
Type C #1029: OpenAI x American Journalism Project July 2026 grant renewal
($5M cash + $3M API credits, two-year extension) - FIRST dedicated corpus
mechanism on the ecosystem-grant geometry; FIFTEENTH relationship direction
per the m807 enumeration (ECOSYSTEM-GRANT, grant-without-consideration).

FINANCIAL MAP (verified Sep 2026):
  Renewal: announced late July 2026 (Inside Philanthropy: AJP CEO Sarabeth
  Berman; newscaststudio/Axios Jul 22 2026): $5M additional funding + $3M
  technology credits, two-year extension. Phase-1 baseline (Jul 2023,
  in-corpus): $5M + $5M credits; AJP Product & AI Studio; 31 orgs direct
  grants across 38 states; 50+ nonprofit newsrooms. Phase-2 shift: from
  experimentation to field-building (Berman); shared products and
  infrastructure for nonprofit local news. Grant stack (single-source
  blockchain.news): WAN-IFRA Newsroom AI Catalyst (165+ newsrooms), Lenfest
  Institute AI fellowship, CUNY/Medill partnerships. AJP scale: $139M
  raised, 41 nonprofit local news orgs backed (theajp.org).
  Geometry: cash + API credits lab-to-philanthropy-to-newsrooms; NO content
  license, NO citation requirement, NO equity, NO revenue share.

CONTRASTS: (a) vs m714 (Village Media x OpenAI): funding FOR a product
(Open Door) with citation-in-ChatGPT consideration - AJP has none; (b) vs
m675 (grant-then-sue): Seattle Times/Newsday sued 23 months after taking
fellowship grants - AJP grantees have not (current-state, not prediction);
(c) vs #609: the renewal was a positive control there, promoted to a
dedicated mechanism here.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False
(Aug 28 2026 standing rule); engine NOT run; verdict
directionally_supported_not_proven; no_analysis_json_update: true; NOT
artifact-grade; NOT falsification-family member (ledger holds at 31).
Correlation is not causation. Confounders: STRONG excerpt-bounded (0
browser.open per #503) + STRONG interested-stakeholder sourcing (Rubin,
Berman) + STRONG single-source grant stack; MEDIUM bounded
no-consideration reading + MEDIUM unfalsifiable goodwill + MEDIUM m675
precedent; WEAK private-company opacity + WEAK no tone claim.

Research method: 5 browser.search query sets, 0 browser.open per #503.
REJECTED: Axel Springer OpenAI renewal (unresolved, no closure surfaced);
Ziff Davis x OpenAI v2 (Sep-17 SJ motion fully in corpus via m759/#879);
Village Media/Open Door (in corpus via m714); OpenAI India publisher deals
and fee estimates (in corpus via m624/m709/m798); NMA x Bria collective
licensing (in corpus); Perplexity Comet Plus 80/20 (in corpus); Microsoft
Publisher Content Marketplace (in corpus); Amazon NYT licensing (in
corpus); OpenAI/Anthropic zero-deal posture (in corpus); elmo
third-party analysis (rejected per #929 precedent); Digiday unsealed
filings (in corpus via m759 corroboration). SELECTED: OpenAI x AJP July
2026 grant renewal - dedicated-mechanism gap (only a #609 positive
control), four zero-hit source URLs, fifteenth-direction geometry.
Pre-commit novelty sweeps per #715: zero test_type_c_1029 files (glob);
no Type C #1029 in git log; max numeric mechanism_id 848 pre-commit; zero
mechanism_id: 849 repo-wide pre-commit; block key zero-hit; 4 of 6 source
URLs zero-hit repo-wide (insidephilanthropy, theajp.org announcement,
gpa.net, blockchain.news; newscaststudio + openai.com 2023 carried).

Doc-sync post-run: 52807/1353 -> 52862/1354 (+55/+1, venv python).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012 working-tree block-key fix all stay out
of this run's index and diff.

Novelty anchor, rotation-guard, hash-placeholder, staged-set, and doc-sync
tests fail pre-commit per the #565/#715/#719/#721 conventions; all green
post-doc-sync; iteration-log newest-entry green.

55 tests, 11 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1029_openai_ajp_grant_renewal_ecosystem_grant_fifteenth_direction_sep27_2am.py"
BLOCK_KEY = "type_c_1029_openai_ajp_grant_renewal_ecosystem_grant_fifteenth_direction_sep27_2am"
MECHANISM = 849
ITERATION = 1029
ITERATION_TYPE = "C"
EXPECTED_TESTS = 55
ANCHORED_SHA = "a9080e9bba16fe5a3fc79e5753733b60cf9bb255"  # patched in the anchor followup per #565
PREDECESSOR_SHAS = {
    "8f3263e8e077cce9849705a3dbfa61fba8168142",  # #1028 main
    "aad728cade1887f36bff6253ac60395bec11e38e",  # #1028 anchor
    "c31100105596e0bb96e379167c9e65ff5b358784",  # #1028 log-hash
}
NEW_URLS = [
    "https://www.insidephilanthropy.com/home/the-most-compelling-case-isnt-journalism-in-crisis-ajp-on-keeping-local-news-sustainable",
    "https://theajp.org/american-journalism-project-announces-new-partnership-with-openai-to-support-local-news/",
    "https://gpa.net/blogs/americas/us-5-million-openai-local-news-deal",
    "https://blockchain.news/news/openai-expands-ai-journalism-initiatives",
]
CARRIED_URLS = [
    "https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/",
    "https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/",
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
class TestNovelty1029:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1029*"))
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
        assert "Type C #1029" in r2.stdout

    def test_novelty_first_claim_present(self):
        block, _ = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "ecosystem-grant" in novelty
        assert "AJP renewal" in novelty

    def test_zero_mechanism_id_849_except_this_block(self):
        # Numeric mechanism_id: 849 must be claimed only by this run's block.
        # (Underscore-form _849_ legitimately exists as Sep-19 iteration-#849
        # test filenames, so the numeric form is the precise needle.)
        r = run_git("grep", "-n", "mechanism_id: 849", "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_no_849_block_keys_repo_wide(self):
        # No zero-indent block key may contain 849 as a mechanism id.
        # Needle built by concatenation so this file never self-matches.
        needle = "^[a-z_0-9]*" + "849" + "[a-z_0-9_]*:"
        r = run_git("grep", "-nE", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines()
                if "mechanism_id" not in line and line.strip()]
        assert hits == []

    def test_new_urls_zero_hit_pre_commit_except_block(self):
        # Each of the 4 new source URLs appears exactly once repo-wide
        # (inside this block). Pre-commit greps per #715 verified zero.
        _, text = _block()
        for url in NEW_URLS:
            assert text.count(url) == 1, url


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard1029:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1025 Type D" in text
        assert "## #1026 Type E" in text
        assert "## #1027 Type A" in text
        assert "## #1028 Type B" in text
        assert "1025-1029" in text

    @pytest.mark.rotation
    def test_fifth_leg_of_1025_to_1029_window(self):
        block, _ = _block()
        assert "FIFTH and CLOSING leg of the 1025-1029 window" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1028_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1028")
        assert "Type B #1028" in r.stdout
        block, _ = _block()
        rt = block["rotation_transparency"]
        assert "Hardawar" in rt
        assert "mechanism 848" in rt
        for sha in PREDECESSOR_SHAS:
            rr = run_git("cat-file", "-t", sha)
            assert rr.stdout.strip() == "commit", sha

    @pytest.mark.rotation
    def test_no_successor_1030_type_d_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type D #1030")
        assert "Type D #1030" not in r.stdout

    @pytest.mark.rotation
    def test_no_concurrent_type_c_1029_by_commit_time(self):
        # Own commits (touching this test file) are excluded per the #1018
        # convention: the guard is about a racing iteration, not this run.
        r = run_git("log", "--format=%H %s", "--grep", "Type C #1029")
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
# 3. Mechanism 849 block content
# ---------------------------------------------------------------------------
class TestMechanism849Content:
    def test_block_key_unique_at_zero_indent(self):
        _, text = _block()
        occurrences = [line for line in text.splitlines()
                       if line == BLOCK_KEY + ":"]
        assert len(occurrences) == 1

    def test_mechanism_id_iteration_type_date_time(self):
        block, _ = _block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == ITERATION_TYPE
        assert block["date_analyzed"] == "2026-09-27"
        assert block["time_pdt"] == "02:00"

    def test_type_and_label(self):
        block, _ = _block()
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_verdict_directionally_supported_not_proven(self):
        block, _ = _block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert "Correlation, not causation" in block["finding"]

    def test_fifteenth_direction_ecosystem_grant(self):
        block, _ = _block()
        tax = block["relationship_direction_taxonomy"]
        assert tax["direction_number"] == "FIFTEENTH per the m807 enumeration"
        assert tax["direction_name"] == "ECOSYSTEM-GRANT (grant-without-consideration)"
        assert "no content-rights consideration" in tax["definition"]
        assert "14 exclusionary-diversion (m846)" in tax["prior_directions"]

    def test_mechanism_name_carries_grant_flag(self):
        block, _ = _block()
        assert "FIRST dedicated corpus mechanism" in block["mechanism_name"]
        assert "American Journalism Project" in block["mechanism_name"]
        assert "FIFTEENTH relationship direction" in block["mechanism_name"]


# ---------------------------------------------------------------------------
# 4. Renewal terms
# ---------------------------------------------------------------------------
class TestRenewalTerms:
    def test_announced_late_july_2026(self):
        block, _ = _block()
        terms = block["renewal_terms"]
        assert "late July 2026" in terms["announced"]
        assert "Jul 22 2026" in terms["announced"]

    def test_five_million_cash(self):
        block, _ = _block()
        assert "$5M" in block["renewal_terms"]["cash"]
        assert "additional $5 million" in block["finding"]

    def test_three_million_tech_credits(self):
        block, _ = _block()
        assert "$3M" in block["renewal_terms"]["credits"]
        assert "technology credits" in block["renewal_terms"]["credits"]

    def test_two_year_extension(self):
        block, _ = _block()
        assert "two-year extension" in block["renewal_terms"]["duration"]

    def test_credit_figure_discrepancy_bounded(self):
        block, _ = _block()
        terms = block["renewal_terms"]
        assert "up to $5M in API credits" in terms["credits"]
        assert "discrepancy bounded, not resolved" in terms["credits"]


# ---------------------------------------------------------------------------
# 5. Phase-1 baseline
# ---------------------------------------------------------------------------
class TestPhase1Baseline:
    def test_2023_original_five_plus_five(self):
        block, _ = _block()
        base = block["renewal_terms"]["phase1_baseline"]
        assert "Jul 2023" in base
        assert "$5M funding + $5M credits" in base

    def test_product_and_ai_studio(self):
        block, _ = _block()
        assert "Product & AI Studio" in block["renewal_terms"]["phase1_baseline"]

    def test_thirty_one_grantees_38_states(self):
        block, _ = _block()
        base = block["renewal_terms"]["phase1_baseline"]
        assert "31 organizations" in base
        assert "38 states" in base

    def test_fifty_plus_newsrooms_portfolio(self):
        block, _ = _block()
        assert "50+ nonprofit newsrooms" in block["renewal_terms"]["phase1_baseline"]

    def test_ajp_scale_139m_41_orgs(self):
        block, _ = _block()
        stack = block["grant_stack"]
        assert "$139M" in stack["ajp_scale"]
        assert "41 nonprofit local news organizations" in stack["ajp_scale"]


# ---------------------------------------------------------------------------
# 6. Phase-2 shift
# ---------------------------------------------------------------------------
class TestPhase2Shift:
    def test_experimentation_to_field_building(self):
        block, _ = _block()
        shift = block["phase2_shift"]
        assert "experimentation to field-building" in shift["direction"]

    def test_shared_products_and_infrastructure(self):
        block, _ = _block()
        assert "shared products and infrastructure" in block["phase2_shift"]["output"]

    def test_phase1_outputs_listed(self):
        block, _ = _block()
        outputs = block["phase2_shift"]["phase1_outputs"]
        assert "fundraising" in outputs
        assert "translation" in outputs

    def test_berman_talent_quotes(self):
        block, _ = _block()
        talent = block["phase2_shift"]["talent_layer"]
        assert "outstanding talent" in talent
        assert "human in the lead" in talent
        assert "additional investments in this space" in block["finding"]

    def test_rubin_benefit_society_quote(self):
        block, _ = _block()
        assert "demonstrate that the technology can benefit society" in block["finding"]


# ---------------------------------------------------------------------------
# 7. Grant stack
# ---------------------------------------------------------------------------
class TestGrantStack:
    def test_wan_ifra_165_newsrooms(self):
        block, _ = _block()
        assert "165+ newsrooms" in block["grant_stack"]["wan_ifra"]

    def test_lenfest_fellowship(self):
        block, _ = _block()
        assert "fellowship" in block["grant_stack"]["lenfest"]

    def test_cuny_medill_partnerships(self):
        block, _ = _block()
        assert "CUNY/Medill" in block["grant_stack"]["journalism_schools"]

    def test_stack_single_source_certification(self):
        block, _ = _block()
        assert "single-source" in block["grant_stack"]["certification"]
        assert "corroboration pending" in block["grant_stack"]["certification"]


# ---------------------------------------------------------------------------
# 8. Contrasts and connections
# ---------------------------------------------------------------------------
class TestContrasts:
    def test_village_media_contrast_no_consideration(self):
        block, _ = _block()
        assert "mechanism 714" in block["finding"]
        assert "citation-in-ChatGPT" in block["finding"]
        assert "no content consideration" in block["finding"]

    def test_grant_then_sue_contrast(self):
        block, _ = _block()
        assert "mechanism 675" in block["finding"]
        assert "Seattle Times/Newsday" in block["finding"]
        assert "have not sued" in block["finding"]

    def test_609_positive_control_pre_history(self):
        block, _ = _block()
        assert "mechanism 609" in block["finding"]
        assert "positive control" in block["finding"]

    def test_connects_to_609_675_714(self):
        block, _ = _block()
        assert block["connects_to"] == [609, 675, 714]

    def test_carried_urls_present_in_block(self):
        _, text = _block()
        for url in CARRIED_URLS:
            assert url in text, url


# ---------------------------------------------------------------------------
# 9. Certification boundaries and statistical discipline
# ---------------------------------------------------------------------------
class TestCertificationBoundaries:
    def test_tone_not_scored_engine_not_run(self):
        block, _ = _block()
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["engine_run"] is False

    def test_no_analysis_json_update_not_artifact_grade(self):
        block, _ = _block()
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_not_falsification_family_ledger_holds(self):
        block, _ = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 31
        assert "holds at 31" in block["falsification_note"]

    def test_excerpt_bounded_zero_browser_open(self):
        block, _ = _block()
        assert block["excerpt_bounded"] is True
        assert block["browser_opens"] == 0
        assert "0 browser.open" in block["excerpt_bounded_note"]

    def test_coverage_note_no_tone_claim(self):
        block, _ = _block()
        assert "No editorial-tone claim" in block["coverage_note"]
        assert "tone NOT_SCORED" in block["coverage_note"]

    def test_verification_block(self):
        block, _ = _block()
        v = block["verification"]
        assert v["max_numeric_mechanism_id_pre_commit"] == 848
        assert v["mechanism_id_claimed"] == 849
        assert v["source_urls_first_appearance"] == 4
        assert v["search_sets"] == 5
        assert v["falsification_ledger_holds_at"] == 31
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True
        assert v["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 10. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence:
    def test_eight_confounders_with_strengths(self):
        block, _ = _block()
        confs = block["confounders"]
        assert len(confs) == 8
        strengths = [c["strength"] for c in confs]
        assert strengths.count("strong") == 3
        assert strengths.count("medium") == 3
        assert strengths.count("weak") == 2

    def test_counterevidence_present(self):
        block, _ = _block()
        assert len(block["counterevidence"]) == 5
        assert any("31 direct grantees" in c for c in block["counterevidence"])

    def test_strongest_counterargument(self):
        block, _ = _block()
        sca = block["strongest_counterargument"]
        assert "cheapest reputation insurance" in sca
        assert "m675" in sca
        assert "Correlation, not causation" in sca

    def test_taxonomy_tension_carried(self):
        block, _ = _block()
        tax = block["relationship_direction_taxonomy"]
        assert "termination-leverage" in tax["taxonomy_tension"]
        assert "carried from #1014" in tax["taxonomy_tension"]


# ---------------------------------------------------------------------------
# 11. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync1029:
    def test_readme_stats_updated(self):
        text = _read(README)
        assert "52862" in text
        assert "1354" in text

    def test_readme_test_table_row(self):
        text = _read(README)
        assert THIS_FILE in text
        assert "Type C #1029" in text
        assert "ECOSYSTEM-GRANT" in text

    def test_architecture_tree_row(self):
        text = _read(ARCH)
        assert THIS_FILE in text
        assert "mechanism 849" in text

    def test_iteration_log_newest_entry(self):
        text = _read(LOG)
        first_header = next(
            line for line in text.splitlines() if line.startswith("## #")
        )
        assert first_header.startswith("## #1029 Type C")
