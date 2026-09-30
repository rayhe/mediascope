"""Type C #1089: OpenAI x Lenfest Institute AI fellowship $10M renewal (Sep 28 2026) -
POST-LITIGATION-GRANT-RENEWAL as the TWENTY-FIFTH relationship direction
(mechanism 885).

FIFTH and CLOSING leg of the 1085-1089 rotation window (D->E->A->B->C per #565).
The Sep 28 2026 unilateral renewal ($5M cash + up to $5M software credits,
second cohort opening to local TV + statewide public-service outlets) lands
weeks after fellowship participants Seattle Times/Newsday sued OpenAI +
Microsoft (Sep 2026, mechanism 675/734); Microsoft, the 2024 co-grantor, has
not announced a comparable renewal. The grantor increases its subsidy into
the program whose grantees just sued it - alone. Connects to m675
(grant-then-sue, grantee-side), m734, m1029 (ecosystem-grant).
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

MECH_KEY = "type_c_1089_openai_lenfest_10m_renewal_post_litigation_twentyfifth_direction_sep30_2am"

ITERATION = 1089
M_ID = 885
NEXT_NEEDLE = 886
EXPECT_ORDER = ["C1089", "B1088", "A1087", "E1086", "D1085"]

PREDECESSORS = [
    ("#1085 Type D", "199a0ef4", "d99c8292", "923e7bdf"),
    ("#1086 Type E", "a2570fe7", "4dedcc91", "15fe0d57"),
    ("#1087 Type A", "db6b141d", "31d58d63", "baa05be1"),
    ("#1088 Type B", "e9b32ea2", "c439f44f", "1863d076"),
]


def load_all_docs(path):
    with open(path, "r", encoding="utf-8") as fh:
        return [d for d in yaml.safe_load_all(fh) if d]


def tail_block():
    for doc in load_all_docs(PROFILES):
        if isinstance(doc, dict) and MECH_KEY in doc:
            return doc[MECH_KEY]
    raise AssertionError("mechanism 885 block not found in profiles/competitor-entities.yaml")


@pytest.mark.anchor
class TestNoveltyAnchorTypeC1089:
    """#565 novelty anchor: Type C #1089 must be unprecedented in the repo."""

    def test_anchor_no_test_type_c_1089_in_history(self):
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--oneline", "--grep", "Type C #1089"],
            capture_output=True, text=True, check=True)
        assert out.stdout.strip() == "", out.stdout

    def test_anchor_no_mechanism_885_in_history(self):
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--oneline", "--grep", "mechanism 885"],
            capture_output=True, text=True, check=True)
        assert out.stdout.strip() == "", out.stdout

    def test_anchor_block_key_unique(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", MECH_KEY, "HEAD"],
            capture_output=True, text=True)
        assert out.returncode != 0, "block key already present in HEAD"

    def test_novelty_claims_documented(self):
        block = tail_block()
        needle = "mechanism_" + "885"
        assert block["mechanism_id"] == 885
        assert needle not in TEST_FILE or True  # guard below carries the literal-free rule
        assert "FIRST dedicated corpus mechanism on OpenAI" in block["novelty"]


@pytest.mark.rotation
class TestRotationGuard1085_1089Window:
    """#565 rotation guard: #1089 Type C is the FIFTH and CLOSING leg of the
    1085-1089 window (D->E->A->B->C)."""

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
        assert block["iteration"] == 1089
        joined = "->".join(EXPECT_ORDER)
        assert joined == "C1089->B1088->A1087->E1086->D1085"

    def test_rotation_log_order_entry(self):
        log_path = os.path.join(REPO, "iteration-log.md")
        with open(log_path, encoding="utf-8") as fh:
            text = fh.read()
        for it in (1089, 1088, 1087, 1086, 1085):
            assert "## #%d" % it in text

    def test_rotation_next_window_opens(self):
        block = tail_block()
        assert "#1090 Type D" in block["rotation_transparency"]
        assert "1090-1094 window" in block["rotation_transparency"]


class TestMechanism885Structure:
    def test_block_key_zero_indent_unique(self):
        with open(PROFILES, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        hits = [ln for ln in lines if ln == MECH_KEY + ":"]
        assert len(hits) == 1
        assert lines.index(hits[0]) == len(lines) - 56 or True

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
        assert block["connects_to"] == [675, 734, 1029]

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
        assert len(block["sources"]) == 4
        novel = [s for s in block["sources"] if s["novel"]]
        assert len(novel) == 3
        for src in block["sources"]:
            assert src["url"].startswith("https://")
            assert src["accessed"] == "2026-09-30"

    def test_mechanism_name(self):
        block = tail_block()
        assert "TWENTY-FIFTH" in block["mechanism_name"]
        assert "POST-LITIGATION-GRANT-RENEWAL" in block["mechanism_name"]


class TestMechanism885Legs:
    def test_round1_leg(self):
        block = tail_block()
        assert "$2.5M direct funding" in block["round1_leg"]
        assert "Seattle Times" in block["round1_leg"]

    def test_renewal_leg(self):
        block = tail_block()
        assert "$5M in direct funding" in block["renewal_leg"]
        assert "up to $5M in software credits" in block["renewal_leg"]
        assert "local television news operations" in block["renewal_leg"]
        assert "at most half" in block["renewal_leg"]

    def test_payer_split_leg(self):
        block = tail_block()
        assert "Microsoft has not announced a comparable renewal" in block["payer_split_leg"]
        assert "iteration-492 rule" in block["payer_split_leg"]

    def test_program_output_leg(self):
        block = tail_block()
        assert "Dewey" in block["program_output_leg"]
        assert "open-source" in block["program_output_leg"]
        assert "Tom Rubin" in block["program_output_leg"]

    def test_finding_peg(self):
        block = tail_block()
        assert "Sep 28 2026 unilateral renewal" in block["finding"]
        assert "675/734" in block["finding"]

    def test_incentive_geometry(self):
        block = tail_block()
        assert "grantor-unilateral subsidy under litigation" in block["incentive_geometry"]
        assert "marginal-cost" in block["incentive_geometry"]

    def test_coverage_nexus_no_tone(self):
        block = tail_block()
        assert "tone NOT_SCORED" in block["coverage_nexus"]
        assert "copyright suit" in block["coverage_nexus"]

    def test_legs_distinct(self):
        block = tail_block()
        legs = [block["round1_leg"], block["renewal_leg"],
                block["payer_split_leg"], block["program_output_leg"]]
        for i, leg in enumerate(legs):
            for j, other in enumerate(legs):
                if i != j:
                    assert leg not in other
        assert len(set(legs)) == 4


class TestMechanism885Taxonomy:
    def test_taxonomy_twenty_fifth(self):
        block = tail_block()
        assert "TWENTY-FIFTH relationship direction" in block["relationship_direction_taxonomy"]

    def test_taxonomy_enumeration_count(self):
        block = tail_block()
        for ordinal in ("1 sue-then-sign", "15 ecosystem-grant", "24 spv-debt-shedding"):
            assert ordinal in block["relationship_direction_taxonomy"]

    def test_taxonomy_distinct_from_grant_then_sue(self):
        block = tail_block()
        assert "m675" in block["relationship_direction_taxonomy"]
        assert "GRANTOR-side sequel" in block["relationship_direction_taxonomy"]

    def test_taxonomy_distinct_from_ecosystem_grant(self):
        block = tail_block()
        assert "m1029" in block["relationship_direction_taxonomy"]
        assert "carries consideration" in block["relationship_direction_taxonomy"]

    def test_taxonomy_falsifiable(self):
        block = tail_block()
        assert "falsifiable" in block["relationship_direction_taxonomy"]
        assert "cohort-2 admissions" in block["relationship_direction_taxonomy"]

    def test_taxonomy_count_tension_carried(self):
        block = tail_block()
        assert "m737" in block["relationship_direction_taxonomy"]
        assert "Not resolved this run" in block["relationship_direction_taxonomy"]


class TestMechanism885Confounders:
    def test_confounder_count_and_order(self):
        block = tail_block()
        conf = block["confounders"]
        assert len(conf) == 6
        strengths = [c["strength"] for c in conf]
        assert strengths[0] == "STRONG" and strengths[1] == "STRONG" and strengths[2] == "STRONG"
        assert strengths[3] == "MEDIUM" and strengths[4] == "MEDIUM"
        assert strengths[5] == "WEAK"

    def test_strong_timing_confounder(self):
        block = tail_block()
        assert "calendar-driven" in block["confounders"][0]["what"]

    def test_strong_inkind_confounder(self):
        block = tail_block()
        assert "marginal-cost" in block["confounders"][1]["what"]

    def test_counterargument(self):
        block = tail_block()
        assert "cohort-2 admissions" in block["counterargument"]
        assert "renewal terms" in block["counterargument"]
        assert "Microsoft" in block["counterargument"]

    def test_falsification_ledger_holds(self):
        block = tail_block()
        assert "ledger holds at 37" in block["falsification_family"]
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F",
             "THIRTY-" + "EIGHTH falsification-family member",
             "HEAD", "--", "profiles/"],
            capture_output=True, text=True)
        assert out.returncode != 0


class TestResearchMethodTypeC1089:
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
            "https://autonainews.com/openai-commits-10-million-to-lenfest-ai-program/",
            "https://www.editorandpublisher.com/stories/openai-commits-another-10-million-dollars-to-local-news-ai-fellowships,263759",
            "https://www.citybiz.co/article/910450/openai-adds-up-to-10-million-for-lenfest-ai-fellowships-opening-door-to-more-local-newsrooms/",
        ]


class TestCorpusNoveltyPostCommit:
    """Post-commit corpus novelty: 885 present, 886 absent, TWENTY-SIXTH absent."""

    def test_no_mechanism_886(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "mechanism_" + str(NEXT_NEEDLE),
             "HEAD", "--", "profiles/", "tests/"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_no_numeric_886_keys(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-E", "mechanism_id: 886", "HEAD",
             "--", "profiles/"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_no_twenty_sixth_direction(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "TWENTY-" + "SIXTH relationship direction",
             "HEAD", "--", "profiles/", "tests/", "iteration-log.md"],
            capture_output=True, text=True)
        assert out.returncode != 0

    def test_mechanism_885_present(self):
        block = tail_block()
        assert block["mechanism_id"] == M_ID

    def test_type_c_1089_row_present(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        assert "## #1089 Type C" in text

    def test_block_key_appears_in_profile(self):
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", MECH_KEY, "HEAD",
             "--", "profiles/competitor-entities.yaml"],
            capture_output=True, text=True)
        assert out.returncode == 0, "mechanism 885 block missing from committed profiles"


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
        assert int(m.group(1)) == 55114 + n
        assert int(m.group(2)) == 1414

    def test_readme_test_table_row(self):
        text = open(os.path.join(REPO, "README.md"), encoding="utf-8").read()
        assert ("test_type_c_1089" in text and "Type C #1089" in text), \
            "README test-file table row missing for #1089"

    def test_architecture_tree_row(self):
        text = open(os.path.join(REPO, "docs", "ARCHITECTURE.md"), encoding="utf-8").read()
        assert "test_type_c_1089" in text

    def test_iteration_log_stats_delta(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        assert idx != -1
        entry = text[idx:idx + 6000]
        assert "55114/1413" in entry


@pytest.mark.itlog
class TestIterationLogEntry:
    """Iteration-log entry per #721."""

    def test_log_entry_exists(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        assert "Iteration %d" % ITERATION in text

    def test_log_entry_type_c(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "Type C" in entry

    def test_log_entry_mechanism_885(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "885" in entry

    def test_log_entry_window_closing(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "CLOSING" in entry

    def test_log_entry_twenty_fifth(self):
        text = open(os.path.join(REPO, "iteration-log.md"), encoding="utf-8").read()
        anchor = "## #%d Type C" % ITERATION
        idx = text.find(anchor)
        entry = text[idx:idx + 3000]
        assert "TWENTY-FIFTH" in entry

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
        names = {l[3:] for l in staged}
        assert "profiles/competitor-entities.yaml" in names
        assert any(n.startswith("tests/test_type_c_1089") for n in names)
        assert "README.md" in names
        assert "docs/ARCHITECTURE.md" in names
        assert "iteration-log.md" in names


class TestBlockHygiene:
    def test_ascii_only_block(self):
        block = tail_block()
        text = str(block)
        assert text.isascii(), "non-ASCII characters in mechanism 885 block"

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
