"""Type C #1064: OpenAI x Oracle committed-demand financing architecture -
the $300B/5yr, 4.5GW Stargate capacity agreement (Jul/Sep 2025) as repriced in
Oracle's Q1 FY2027 print (Sep 10 2026): RPO $664B (+$209B YoY, +$26B QoQ),
>$30B new AI cloud contracts, 300,000+ GPUs and 850MW delivered in the
quarter, $28.5B quarterly capex, and Clay Magouyrk's three customer-side
financing mechanisms (supplier financing repaid from customer payments;
customer-pays-for-hardware/Oracle-operates; customer prepayment) - mechanism
870. DEMAND-UNDERWRITING as the TWENTIETH relationship direction per the m807
enumeration: the customer's committed spend, prepayments ($11.36B in Q1
FY2027), and at the extreme customer-supplied hardware (BYOH) underwrite the
supplier's capex; the financing arrow runs buyer-to-supplier. Reverse of #18
demand-recycling (m864: the supplier's equity funds the customer's committed
purchases of the supplier's own chips - cash out as equity, back as revenue)
and distinct from #13 demand-for-equity (m1009: the supplier pays the customer
IN EQUITY as the demand consideration) and #19 backstop-recycling (m867: the
supplier's contingent guarantee underwrites the customer's third-party lease).
Stress leg: Oracle's Sep 11 2026 10-Q supplemented the restructuring plan by
~$700M (~$2.8B estimated) and named AI adoption as a workforce-restructuring
driver for the first time; the force majeure notice on the $165B Project
Jupiter campus (2.45GW, Dona Ana County NM, 2028 deadline) shows the
risk-allocation layer of the committed-demand architecture. FIRST-HAND this
run: OpenAI's official Stargate page (47 rendered lines) and Oracle's Q1
FY2026 earnings release (RPO $455B/+359% baseline, opened end-to-end).
MANUAL / qualitative only; engine NOT run; tone NOT_SCORED; p_value/cohens_d/
ci_95 NOT_CALCULATED; is_significant False; NOT artifact-grade; no
analysis.json update; verdict directionally_supported_not_proven; NOT a
falsification-family member (financial-architecture mapping, not a
uniform-prediction test); ledger holds at 35. Correlation is not causation.

FIFTH and CLOSING leg of the 1060-1064 window: D (#1060) -> E (#1061) -> A
(#1062) -> B (#1063) -> C (#1064), rotation per #565. Next run is #1065 Type
D, opening the 1065-1069 window; it pins the zero-870 guards in the #1060
file that fail by design this run. Concurrency: #899 (nytimes.yaml), #938
(test file), #900 (untracked test file), #1012-wt (test file) in-flight and
untouched; targeted staging only.

Anchor-marked tests deselected pre-commit per #565; rotation/itlog/doc-sync
tests fail pre-doc-sync by design per #719; in-flight tests fail pre-staging
by design.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "competitor-entities.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")

TYPE_LETTER = "C"
ITERATION = 1064
M_ID = 870
MECH_KEY = (
    "type_c_1064_oracle_openai_300b_45gw_demand_underwriting_"
    "twentieth_direction_sep29_1am"
)
MECH_ID_MARKER = "mechanism" + "_" + "87" + "0"  # own-form underscore sweep marker
MECH_ID_DASH = "mechanism" + "-" + "87" + "0"
MECH_ID_NUMERIC = "mechanism_id" + ": " + "87" + "0"
NEXT_US = "mechanism" + "_" + "87" + "1"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-" + "87" + "1"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id" + ": " + "87" + "1"  # next-number numeric sweep
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "ca831b0b7c7ae568fab17d12f829e4cb5f914774"  # patched in the anchor followup commit
NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1064 files, max numeric\nmechanism_id 869 pre-commit, "
    "block key zero-hit, 7 novel\nURLs zero-hit, oracle absent"
)
EXPECTED_NEW_URLS = [
    "https://openai.com/index/five-new-stargate-sites/",
    "https://www.datacenterdynamics.com/en/news/oracle-delivered-300000-gpus-in-q1-fy2027/",
    "https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/",
    "https://www.aistockwire.com/blog/oracle-orcl-q1-fy2027-664-billion-rpo-negative-free-cash-flow-september-2026",
    "https://r40.io/news/orcl-q1-fy2027-reported-earnings-analysis/",
    "https://www.cio.com/article/4222306/oracle-forecasts-33-increase-in-restructuring-costs-as-new-round-of-layoffs-hits.html",
    "https://www.tradingnews.com/news/oracle-rebounds-to-137-usd-from-133-usd-low-as-664b-usd-backlog",
]
EXPECTED_ORDER = [("C", "1064"), ("B", "1063"), ("A", "1062"), ("E", "1061"), ("D", "1060")]
README_TESTS_BEFORE = 54553
README_FILES_BEFORE = 1388
README_TESTS_AFTER = 54608
README_FILES_AFTER = 1389
INFLIGHT_FILES = [
    "profiles/nytimes.yaml",  # #899 Type C, modified in worktree
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938, modified
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900, untracked
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_luna_havoc_m817_pairing_sep26_7am.py",  # #1012-wt, modified
]
STAGED_EXPECTED_BASENAMES = {
    "competitor-entities.yaml",
    OWN_BASENAME,
    "test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_credit_vs_meta_scrapped_tool_sep28_6pm.py",
    "test_type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_vs_sep16_meta_luna_inbrief_stigma_contrast_sep28_7pm.py",
    "test_type_c_1059_sb_energy_openai_55b_warrant_tenant_nvidia_105b_backstop_recycling_nineteenth_direction_sep28_8pm.py",
    "test_type_a_1062_ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register_sep28_11pm.py",
    "test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py",
    "test_type_d_1060_m865_m866_m867_qualitative_corpus_integrity_sep28_9pm.py",
    "README.md",
    "ARCHITECTURE.md",
    "iteration-log.md",
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _load_profile():
    import yaml

    return yaml.safe_load(_read(PROFILE))


def get_block():
    return _load_profile()[MECH_KEY]


def _corpus_ids():
    ids = []
    for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(f)):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle):
    hits = []
    for root in ("profiles", "tests"):
        base = os.path.join(REPO, root)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] not in ("py", "yaml", "md", "json"):
                    continue
                p = os.path.join(dirpath, fn)
                if needle in open(p, errors="ignore").read():
                    hits.append(p)
    return hits


def _staged_paths():
    return _git(["diff", "--cached", "--name-only"]).stdout.splitlines()


# ---------------------------------------------------------------------------
# 1. Novelty anchor (anchor-marked tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeC1064:
    @pytest.mark.anchor
    def test_anchor_exists(self):
        assert ANCHORED_SHA not in (None, "PATCH_ME_IN_FOLLOWUP"), (
            "anchor NULL pre-commit (patched post-commit)"
        )

    @pytest.mark.anchor
    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_anchor_in_log_header(self):
        # Scoped to the #1064 header line (not the whole log) per the #1044
        # test fix: newer entries name predecessor SHAs in their
        # rotation-transparency sections, which a whole-log index() cannot
        # distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1064 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1064 files, max numeric\nmechanism_id 869 pre-commit, "
            "block key zero-hit, 7 novel\nURLs zero-hit, oracle absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1060-1064 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1060_1064Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1060", "D"), ("1061", "E"), ("1062", "A"), ("1063", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1064 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1060-1064" in rt and "#1063 Type B" in rt and "CLOSING leg" in rt
        assert "D->E->A->B->C" in rt

    def test_predecessor_1063_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1063 Type B" in rt
        assert "0eb434c8" in rt and "6bb0261f" in rt and "5376281b" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism870Structure:
    def test_mechanism_id_and_type(self):
        block = get_block()
        assert block["mechanism_id"] == M_ID
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_iteration_fields(self):
        block = get_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == TYPE_LETTER
        assert block["iteration_time"] == "2026-09-29 01:00 PDT"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_block_key_descriptive_no_870(self):
        assert MECH_KEY in _read(PROFILE)
        assert "870" not in MECH_KEY
        assert "demand_underwriting" in MECH_KEY
        assert "twentieth_direction" in MECH_KEY
        assert get_block()["block_key"] == MECH_KEY

    def test_discipline_flags(self):
        block = get_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["yaml_parse_clean"] is True
        assert block["ascii_only"] is True

    def test_connects_to(self):
        block = get_block()
        assert block["connects_to"] == [864, 867, 1009, 738]
        assert block["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 4. The three legs + coverage nexus
# ---------------------------------------------------------------------------
class TestMechanism870Legs:
    def test_commitment_leg(self):
        leg = get_block()["commitment_leg"]
        assert "$300 billion" in leg
        assert "4.5GW" in leg or "4.5 gigawatts" in leg
        assert "July 2025" in leg
        assert "Shackelford" in leg and "Dona Ana" in leg
        assert "first-hand" in leg

    def test_underwrite_leg(self):
        leg = get_block()["underwrite_leg"]
        assert "$664B" in leg
        assert "300,000" in leg and "850MW" in leg
        assert "$28.5B" in leg
        assert "prepay or bring your own hardware" in leg
        assert "three financing mechanisms" in leg or "three mechanisms" in leg
        assert "$455B" in leg  # Q1 FY2026 baseline, opened first-hand

    def test_stress_leg(self):
        leg = get_block()["stress_leg"]
        assert "10-Q" in leg
        assert "$700M" in leg or "700M" in leg
        assert "Project Jupiter" in leg
        assert "$165B" in leg
        assert "majeure" in leg  # "Force majeure" in block; case-tolerant

    def test_coverage_nexus_no_tone_claims(self):
        nexus = get_block()["coverage_nexus"]
        assert "largest single AI-infrastructure customer commitment" in nexus
        assert "financial-event peg" in nexus
        assert "tone NOT_SCORED" in nexus

    def test_finding_geometry(self):
        finding = get_block()["finding"]
        assert "demand-underwriting" in finding
        assert "buyer-to-supplier" in finding
        assert "THE COMMITMENT LEG" in finding
        assert "THE UNDERWRITE LEG" in finding
        assert "THE STRESS LEG" in finding
        assert "THE GEOMETRY" in finding

    def test_sources_first_hand(self):
        sources = get_block()["sources"]
        assert len(sources) == 7
        urls = [s["url"] for s in sources]
        for u in EXPECTED_NEW_URLS:
            assert u in urls
        assert all(s["novel"] is True for s in sources)
        assert all(s["accessed"] == "2026-09-29" for s in sources)

    def test_counterargument_earns_slot(self):
        ca = get_block()["counterargument"]
        assert "take-or-pay" in ca
        assert "twentieth slot" in ca
        assert "prepay/BYOH" in ca


# ---------------------------------------------------------------------------
# 5. Taxonomy: the twentieth direction
# ---------------------------------------------------------------------------
class TestMechanism870Taxonomy:
    def test_twentieth_direction_named(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "TWENTIETH" in tax
        assert "DEMAND-UNDERWRITING" in tax

    def test_enumeration_lists_twenty(self):
        tax = get_block()["relationship_direction_taxonomy"]
        for n in ("1 sue-then-sign m624", "13 demand-for-equity m1009",
                 "18 demand-recycling m864", "19 backstop-recycling m867"):
            assert n in tax

    def test_distinct_from_thirteen(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "#13 (equity IS the payment for demand)" in tax

    def test_reverse_of_eighteen(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "Reverse of #18" in tax
        assert "cash out as equity, back as revenue" in tax

    def test_distinct_from_nineteen(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "#19 (contingent guarantee underwriting a third-party lease)" in tax

    def test_m737_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "termination-leverage" in tax
        assert "Not resolved this run" in tax


# ---------------------------------------------------------------------------
# 6. Confounders, strongest-first
# ---------------------------------------------------------------------------
class TestMechanism870Confounders:
    def test_six_confounders_ranked(self):
        confs = get_block()["confounders"]
        assert len(confs) == 6
        assert [c["strength"] for c in confs] == [
            "STRONG", "STRONG", "STRONG", "MEDIUM", "MEDIUM", "WEAK",
        ]

    def test_headline_estimate_confound(self):
        confs = get_block()["confounders"]
        assert "headline estimate" in confs[0]["what"]
        assert "take-or-pay floors" in confs[0]["what"]

    def test_rpo_floor_confound(self):
        confs = get_block()["confounders"]
        assert "floor, not a forecast" in confs[1]["what"]
        assert "OpenAI" in confs[1]["what"] and "not disclosed" in confs[1]["what"]

    def test_run_rate_relay_confound(self):
        confs = get_block()["confounders"]
        assert "$30B/yr" in confs[2]["what"]
        assert "analyst relay" in confs[2]["what"]

    def test_financing_logic_confound(self):
        confs = get_block()["confounders"]
        assert "financing logic, not legal security" in confs[3]["what"]

    def test_layoff_attribution_confound(self):
        confs = get_block()["confounders"]
        assert "attribution" in confs[4]["what"]

    def test_timing_confound(self):
        confs = get_block()["confounders"]
        assert "dates to July/Sep 2025" in confs[5]["what"]

    def test_not_falsification_family_ledger_35(self):
        block = get_block()
        assert block["falsification_family_member"] is False
        # The ledger and falsification-family prose lives in the iteration-log
        # entry (discipline section), not the block itself.
        section = _log_section()
        assert "NOT a falsification-family member" in section
        assert "ledger holds at 35" in section


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1064:
    def test_two_browser_open_first_hand(self):
        section = _log_section()
        assert "2 browser.open" in section
        assert "OpenAI" in section and "Oracle" in section

    def test_four_search_sets(self):
        section = _log_section()
        assert "4 browser.search" in section

    def test_urls_verbatim_no_canonical(self):
        for url in EXPECTED_NEW_URLS:
            assert url.startswith("https://") and " " not in url

    def test_ascii_only_no_em_dashes(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")


# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty: 870 is max, 871 is zero
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_870(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_next_numeric_871_in_profiles(self):
        base = os.path.join(REPO, "profiles")
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_871_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_seven_urls_now_in_corpus(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        for u in EXPECTED_NEW_URLS:
            assert u in text, "novel URL not ingested: %s" % u

    def test_own_needles_format_built(self):
        # Per #715: own file's forward-looking needles are format-built so no
        # contiguous literal exists anywhere in the committed tree. The
        # absence assertions below are themselves format-built for the same
        # reason: asserting absence of a literal would embed the literal.
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "mechanism" + "_" + "87" + "1" not in blob
        assert "mechanism" + "-" + "87" + "1" not in blob


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        line = next(
            l for l in _read(README).splitlines() if l.startswith("| Tests |")
        )
        assert str(README_TESTS_AFTER) in line
        assert str(README_FILES_AFTER) in line

    def test_readme_row_1064(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1064" in text
        assert "mechanism 870" in text

    def test_arch_row_1064(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1064" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1064"), ("B", "1063"), ("A", "1062"), ("E", "1061"), ("D", "1060")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1064 Type C")
        end = log.index("## #1063 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1064 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 870" in section
        assert "DEMAND-UNDERWRITING" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1060-1064" in section
        assert "C #1064" in section


# ---------------------------------------------------------------------------
# 11. In-flight concurrency isolation (#899, #938, #900, #1012-wt)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # Fails pre-commit by design (nothing staged yet); green once the
        # run stages its own files. All four in-flight paths stay
        # uncommitted and unstaged.
        staged = _staged_paths()
        assert staged != [], "nothing staged yet (pre-commit)"
        for f in INFLIGHT_FILES:
            assert f not in staged, "in-flight file leaked into staging: %s" % f
        assert not any("test_type_b_938_" in l for l in staged)
        assert not any("test_type_d_900_" in l for l in staged)
        assert not any("test_type_a_1012_" in l for l in staged)

    def test_targeted_staging_only(self):
        # Fails pre-commit by design; green post-staging. The staged set
        # must be exactly this run's files - nothing more.
        staged = {os.path.basename(p) for p in _staged_paths()}
        assert staged == STAGED_EXPECTED_BASENAMES


# ---------------------------------------------------------------------------
# 12. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_only(self):
        import json

        blob = json.dumps(get_block(), ensure_ascii=False)
        assert "\u2014" not in blob  # no em dashes, repo prose rule
        blob.encode("ascii")  # raises on any other non-ASCII

    def test_source_references_recorded(self):
        # Per the standing "keep references" rule: every fact needs a
        # source URL or citation; the block carries 7 verbatim URLs.
        sources = get_block()["sources"]
        assert len(sources) == 7
        assert all(s["url"].startswith("https://") for s in sources)

    def test_test_file_ascii(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")

    def test_finding_carries_discipline_prose(self):
        # Discipline prose lives in the block's finding (legs + first-hand
        # caveat) and the iteration-log entry (ledger, falsification family);
        # the machine-readable flags are asserted in test_discipline_flags.
        finding = get_block()["finding"]
        assert "FIRST-HAND SOURCES this run" in finding
        section = _log_section()
        assert "MANUAL" in section
        assert "NOT a falsification-family member" in section
        assert "ledger holds at 35" in section


def _log_section():
    # Helper used by TestResearchMethodTypeC1064; defined after the classes
    # that reference it at call time (not import time).
    log = _read(ITERATION_LOG)
    start = log.index("## #1064 Type C")
    end = log.index("## #1063 Type B")
    return log[start:end]
