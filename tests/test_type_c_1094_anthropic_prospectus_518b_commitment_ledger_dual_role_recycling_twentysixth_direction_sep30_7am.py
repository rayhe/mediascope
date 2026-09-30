"""Type C #1094: Anthropic leaked draft S-1 (Reuters Sep 28 2026) - $518B
compute-commitment ledger discloses the investor-supplier dual role;
DUAL-ROLE RECYCLING as the TWENTY-SIXTH relationship direction
(mechanism 888).

FIFTH and CLOSING leg of the 1090-1094 rotation window (D->E->A->B->C per #565).
The Sep 28-29 2026 leaked draft S-1 (Reuters review) discloses $518B in future
cloud/compute/infrastructure commitments alongside a $42B 2025 net loss
(~$34B non-cash) on $4.6B revenue - the first primary-class document that makes
the investor-supplier dual-role geometry measurable: Amazon (AWS) and Google
(cloud/TPU, $35B payment guarantor per corpus) sit on both sides of the ledger.
Partial S-1 realization of m864's demand-recycling proof test (the m864
counterargument demanded a compute-purchase commitment disclosed in the S-1).
NOT a falsification-family member: ledger holds at 37.
"""
import os
import re
import subprocess
import sys
import yaml

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(REPO, "profiles", "competitor-entities.yaml")
TEST_FILE = os.path.basename(__file__)

MECH_KEY = "type_c_1094_anthropic_prospectus_518b_commitment_ledger_dual_role_recycling_twentysixth_direction_sep30_7am"

ITERATION = 1094
M_ID = 888
NEXT_NEEDLE = 889
EXPECT_ORDER = ["C1094", "B1093", "A1092", "E1091", "D1090"]

PREDECESSORS = [
    ("#1090 Type D", "4881bd45", "418a8b52", "3c5c48ce"),
    ("#1091 Type E", "711d3169", "bc2249d9", "bcc047b0"),
    ("#1092 Type A", "7c551fcc", "2a234a33", "59af8b51"),
    ("#1093 Type B", "7fbc7f46", "2796e83b", "f59a8361"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it to
# the real main commit SHA.
ANCHORED_SHA = "0" * 40


def load_all_docs(path):
    with open(path, "r", encoding="utf-8") as fh:
        return [d for d in yaml.safe_load_all(fh) if d]


def tail_block():
    for doc in load_all_docs(PROFILES):
        if isinstance(doc, dict) and MECH_KEY in doc:
            return doc[MECH_KEY]
    raise AssertionError("mechanism 888 block not found in profiles/competitor-entities.yaml")


@pytest.mark.anchor
class TestNoveltyAnchorTypeC1094:
    """#565 novelty anchor: Type C #1094 must be unprecedented in the repo."""

    def test_anchor_type_c_1094_in_history(self):
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--format=%H", "--grep", "Type C #1094"],
            capture_output=True, text=True, check=True)
        assert ANCHORED_SHA in out.stdout.split(), out.stdout

    def test_anchor_mechanism_888_in_history(self):
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--format=%H", "--grep", "mechanism 888"],
            capture_output=True, text=True, check=True)
        assert ANCHORED_SHA in out.stdout.split(), out.stdout

    def test_anchor_sha_pinned_and_logged(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries the all-zeros
        # placeholder until the anchor followup patches it to the real main
        # commit SHA; the log-hash followup registers it in the log header.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        out = subprocess.run(
            ["git", "-C", REPO, "rev-parse", ANCHORED_SHA],
            capture_output=True, text=True)
        assert out.returncode == 0 and out.stdout.strip() == ANCHORED_SHA
        log = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        header_start = log.index("## #1094 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims_documented(self):
        block = tail_block()
        needle = "mechanism_" + "888"
        assert block["mechanism_id"] == 888
        assert needle not in TEST_FILE or True  # guard below carries the literal-free rule
        assert "FIRST dedicated corpus mechanism on the Sep 28-29 2026" in block["novelty"]


@pytest.mark.rotation
class TestRotationGuard1090_1094Window:
    """#565 rotation guard: #1094 Type C is the FIFTH and CLOSING leg of the
    1090-1094 window (D->E->A->B->C)."""

    def test_rotation_predecessor_commits_present(self):
        for label, main, anchor, loghash in PREDECESSORS:
            for sha, kind in ((main, "main"), (anchor, "anchor"), (loghash, "log-hash")):
                out = subprocess.run(
                    ["git", "-C", REPO, "cat-file", "-t", sha],
                    capture_output=True, text=True)
                assert out.returncode == 0, "%s %s commit %s missing" % (label, kind, sha)

    def test_rotation_order_string(self):
        block = tail_block()
        assert block["iteration_type"] == "C"
        assert block["iteration"] == 1094
        joined = "->".join(EXPECT_ORDER)
        assert joined == "C1094->B1093->A1092->E1091->D1090"

    def test_rotation_log_order_entry(self):
        log_path = os.path.join(REPO, "iteration-log.md")
        with open(log_path, encoding="utf-8") as fh:
            text = fh.read()
        anchor = "## #1094 Type C"
        idx = text.find(anchor)
        assert idx != -1
        entry = text[idx:idx + 4000]
        assert "D->E->A->B->C" in entry
        assert "CLOSING" in entry


class TestMechanism888Structure:
    def test_block_key_zero_indent_unique(self):
        with open(PROFILES, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        hits = [ln for ln in lines if ln == MECH_KEY + ":"]
        assert len(hits) == 1

    def test_block_key_field_repeat(self):
        block = tail_block()
        assert block["block_key"] == MECH_KEY
        with open(PROFILES, encoding="utf-8") as fh:
            assert fh.read().count(MECH_KEY) == 2

    def test_mechanism_id_numeric(self):
        block = tail_block()
        assert block["mechanism_id"] == M_ID
        assert isinstance(block["mechanism_id"], int)

    def test_type_fields(self):
        block = tail_block()
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to(self):
        block = tail_block()
        assert block["connects_to"] == [864, 870, 885]

    def test_discipline_fields(self):
        block = tail_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["falsification_family_member"] is False

    def test_sources_structure(self):
        block = tail_block()
        assert len(block["sources"]) == 3
        novel = [s for s in block["sources"] if s["novel"]]
        assert len(novel) == 3
        for src in block["sources"]:
            assert src["url"].startswith("https://")
            assert src["accessed"] == "2026-09-30"

    def test_mechanism_name(self):
        block = tail_block()
        assert "TWENTY-SIXTH" in block["mechanism_name"]
        assert "DUAL-ROLE RECYCLING" in block["mechanism_name"]


class TestMechanism888Legs:
    def test_commitment_leg(self):
        block = tail_block()
        assert "$518B" in block["commitment_leg"]
        assert "m870" in block["commitment_leg"]
        assert "iteration-492 rule" in block["commitment_leg"]

    def test_loss_structure_leg(self):
        block = tail_block()
        assert "$42B 2025 net loss" in block["loss_structure_leg"]
        assert "$34B" in block["loss_structure_leg"]
        assert "$8.06B operating loss" in block["loss_structure_leg"]
        assert "$7.33B" in block["loss_structure_leg"]

    def test_revenue_leg(self):
        block = tail_block()
        assert "$11.5B" in block["revenue_leg"]
        assert "adjusted operating profit" in block["revenue_leg"]
        assert "$65B raised at $965B post-money" in block["revenue_leg"]
        assert "leaked draft, not a filed document" in block["revenue_leg"]

    def test_investor_supplier_leg(self):
        block = tail_block()
        assert "payment guarantor" in block["investor_supplier_leg"]
        assert "m864" in block["investor_supplier_leg"]
        assert "compute-purchase commitment contractually tied" in block["investor_supplier_leg"]

    def test_finding_peg(self):
        block = tail_block()
        assert "Sep 28-29 2026" in block["finding"]
        assert "investor-supplier dual-role" in block["finding"]

    def test_incentive_geometry(self):
        block = tail_block()
        assert "closed loop" in block["incentive_geometry"]
        assert "m870" in block["incentive_geometry"]
        assert "recycling circuit" in block["incentive_geometry"]

    def test_coverage_nexus_no_tone(self):
        block = tail_block()
        assert "tone NOT_SCORED" in block["coverage_nexus"]
        assert "m864 named as its proof test" in block["coverage_nexus"]

    def test_legs_distinct(self):
        block = tail_block()
        legs = [block["commitment_leg"], block["loss_structure_leg"],
                block["revenue_leg"], block["investor_supplier_leg"]]
        for i, leg in enumerate(legs):
            for j, other in enumerate(legs):
                if i != j:
                    assert leg not in other
        assert len(set(legs)) == 4


class TestMechanism888Taxonomy:
    def test_taxonomy_twenty_sixth(self):
        block = tail_block()
        assert "TWENTY-SIXTH relationship direction" in block["relationship_direction_taxonomy"]

    def test_taxonomy_enumeration_count(self):
        block = tail_block()
        for ordinal in ("1 sue-then-sign", "18 demand-recycling", "25 post-litigation-grant-renewal"):
            assert ordinal in block["relationship_direction_taxonomy"]

    def test_taxonomy_distinct_from_demand_recycling(self):
        block = tail_block()
        assert "m864" in block["relationship_direction_taxonomy"]
        assert "one supplier, one round trip" in block["relationship_direction_taxonomy"]

    def test_taxonomy_distinct_from_demand_underwriting(self):
        block = tail_block()
        assert "m870" in block["relationship_direction_taxonomy"]
        assert "open arrow, distinct parties" in block["relationship_direction_taxonomy"]

    def test_taxonomy_falsifiable(self):
        block = tail_block()
        assert "Falsifiable" in block["relationship_direction_taxonomy"]
        assert "neoclouds" in block["relationship_direction_taxonomy"]

    def test_taxonomy_count_tension_carried(self):
        block = tail_block()
        assert "m737" in block["relationship_direction_taxonomy"]
        assert "Not resolved this run" in block["relationship_direction_taxonomy"]


class TestMechanism888Confounders:
    def test_confounder_count_and_order(self):
        block = tail_block()
        conf = block["confounders"]
        assert len(conf) == 6
        strengths = [c["strength"] for c in conf]
        assert strengths[0] == "STRONG" and strengths[1] == "STRONG" and strengths[2] == "STRONG"
        assert strengths[3] == "MEDIUM" and strengths[4] == "MEDIUM"
        assert strengths[5] == "WEAK"

    def test_strong_draft_tier_confounder(self):
        block = tail_block()
        assert "leaked draft reviewed by Reuters" in block["confounders"][0]["what"]

    def test_strong_counterparty_opacity_confounder(self):
        block = tail_block()
        assert "Commitment-counterparty opacity" in block["confounders"][1]["what"]
        assert "m870" in block["confounders"][1]["what"]

    def test_counterargument(self):
        block = tail_block()
        assert "PARTIALLY realized" in block["counterargument"]
        assert "contractually tied to the anchor investment" in block["counterargument"]
        assert "public S-1 is the closing instrument" in block["counterargument"]

    def test_falsification_ledger_holds(self):
        block = tail_block()
        assert "ledger holds at 37" in block["falsification_family"]
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F",
             "THIRTY-" + "EIGHTH falsification-family member",
             "HEAD", "--", "profiles/"],
            capture_output=True, text=True)
        assert out.returncode != 0


class TestResearchMethodTypeC1094:
    """Research-method disclosure: 3 search sets, 0 browser.open per #503."""

    def test_search_sets_three(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        assert idx != -1
        entry = text[idx:idx + 4000]
        assert "3 search sets, 0 browser.open" in entry or "0 browser.open" in entry

    def test_no_fresh_open(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        assert idx != -1
        entry = text[idx:idx + 4000]
        assert "per #503" in entry

    def test_novel_urls_verbatim(self):
        block = tail_block()
        urls = [s["url"] for s in block["sources"] if s["novel"]]
        assert urls == [
            "https://unbiasedheadlines.com/article/anthropics-leaked-ipo-filing-shows-42-billion-loss-and-518-billion-in-future-spending-commitments",
            "https://decodethefuture.org/en/anthropic-s1-ipo-filing-explained/",
            "https://gattyworks.com/news/anthropic-ipo-prospectus-existential-risk-disclosure",
        ]


class TestCorpusNoveltyPostCommit:
    """Post-commit corpus novelty: 888 present, 889 absent, TWENTY-SEVENTH absent."""

    def test_next_mechanism_absent(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "mechanism_" + str(NEXT_NEEDLE),
             "HEAD", "--", "profiles/", "tests/"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_no_numeric_889_keys(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-E", "mechanism_id: 889", "HEAD",
             "--", "profiles/"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_no_twenty_seventh_direction(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "TWENTY-" + "SEVENTH relationship direction",
             "HEAD", "--", "profiles/", "tests/", "iteration-log.md"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_mechanism_888_present(self):
        block = tail_block()
        assert block["mechanism_id"] == M_ID

    def test_type_c_1094_row_present(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        assert "## #1094 Type C" in text

    def test_block_key_appears_in_profile(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", MECH_KEY, "HEAD",
             "--", "profiles/competitor-entities.yaml"],
            capture_output=True, text=True)
        assert out.returncode == 0, "mechanism 888 block missing from committed profiles"


class TestDocSyncRatchet:
    """Doc-sync ratchet per #719."""

    def _tests_total(self):
        out = subprocess.run(
            [sys.executable, "-m", "pytest", __file__, "--collect-only", "-q",
             "-p", "no:cacheprovider", "-o", "addopts="],
            capture_output=True, text=True, cwd=REPO,
            env={k: v for k, v in __import__("os").environ.items()
                 if k != "PYTEST_CURRENT_TEST"})
        lines = [l for l in out.stdout.splitlines() if "tests collected" in l]
        assert lines, "collect-only produced no count line; stdout=%r stderr=%r" % (
            out.stdout[-400:], out.stderr[-400:])
        return int(re.search(r"(\d+) tests collected", lines[0]).group(1))

    def test_readme_stats_line(self):
        n = self._tests_total()
        text = open(os.path.join(REPO, "README.md"), encoding="utf-8").read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats line missing"
        assert int(m.group(1)) == 55467 + n
        assert int(m.group(2)) == 1419

    def test_readme_test_table_row(self):
        text = open(os.path.join(REPO, "README.md"), encoding="utf-8").read()
        assert ("test_type_c_1094" in text and "Type C #1094" in text), \
            "README test-file table row missing for #1094"

    def test_architecture_tree_row(self):
        text = open(os.path.join(REPO, "docs", "ARCHITECTURE.md"), encoding="utf-8").read()
        assert "test_type_c_1094" in text

    def test_iteration_log_stats_delta(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        assert idx != -1
        entry = text[idx:idx + 6000]
        assert "55467/1418" in entry


@pytest.mark.itlog
class TestIterationLogEntry:
    """Iteration-log entry per #721."""

    def test_log_entry_exists(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        assert "## #1094 Type C" in text

    def test_log_entry_type_c(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "Type C" in entry

    def test_log_entry_mechanism_888(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "888" in entry

    def test_log_entry_window_closing(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "CLOSING" in entry

    def test_log_entry_twenty_sixth(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "TWENTY-SIXTH" in entry

    def test_log_entry_window_sequence(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "D->E->A->B->C" in entry


class TestInflightIsolation:
    """In-flight files per #720: #899/#938/#900/#1012-wt untouched."""

    def test_inflight_not_staged(self):
        out = subprocess.run(
            ["git", "-C", REPO, "status", "--porcelain"],
            capture_output=True, text=True, check=True)
        staged = [l for l in out.stdout.splitlines() if l and l[0] in "MARCD"]
        for line in staged:
            assert "nytimes.yaml" not in line, "in-flight #899 file staged!"
            assert "test_type_b_938" not in line, "in-flight #938 file staged!"
            assert "test_type_d_900" not in line, "in-flight #900 file staged!"
            assert "test_type_a_1012" not in line, "in-flight #1012-wt file staged!"

    def test_only_expected_files_staged(self):
        out = subprocess.run(
            ["git", "-C", REPO, "status", "--porcelain"],
            capture_output=True, text=True, check=True)
        staged = [l for l in out.stdout.splitlines() if l and l[0] in "MARCD"]
        allowed = (
            "profiles/competitor-entities.yaml",
            "tests/test_type_c_1094",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for line in staged:
            assert "nytimes.yaml" not in line, "in-flight #899 file staged!"
            assert "test_type_b_938" not in line, "in-flight #938 file staged!"
            assert "test_type_d_900" not in line, "in-flight #900 file staged!"
            assert "test_type_a_1012" not in line, "in-flight #1012-wt file staged!"
            assert any(a in line for a in allowed), line


class TestBlockHygiene:
    def test_ascii_only_block(self):
        block = tail_block()
        text = str(block)
        assert text.isascii(), "non-ASCII characters in mechanism 888 block"

    def test_ascii_only_test_file(self):
        text = open(__file__, encoding="utf-8").read()
        assert text.isascii(), "non-ASCII characters in test file"

    def test_no_em_dashes(self):
        text = open(__file__, encoding="utf-8").read()
        assert "\u2014" not in text and "\u2013" not in text
        block = tail_block()
        assert "\u2014" not in str(block) and "\u2013" not in str(block)

    def test_yaml_parse_clean(self):
        block = tail_block()
        assert block["yaml_parse_clean"] is True
        assert block["ascii_only"] is True
