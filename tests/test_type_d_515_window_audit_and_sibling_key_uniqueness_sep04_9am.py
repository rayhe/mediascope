"""Type D iteration #515 (2026-09-04 09:00 PDT): 511-514 window audit,
sibling mechanism-key uniqueness, scorer delta consistency since #510.

Novel vs #505 (repo-wide YAML parse, 501-505 rotation, 5-section entry check)
and #510 (doc-surface per-file rows, 506-510 rotation, git-order static list,
window data-mechanism integrity, full 28-block scorer audit):

  1. TestRotation511to514CycleIntegrity - newest-first heading order with the
     D->E->A->B->C rotation and predecessor references (new window).
  2. TestDocSurfaceCompleteness511to514 - README + ARCHITECTURE rows for the
     four window files with row-count vs def-count agreement (new window).
  3. TestGitCommitRelativeOrder510to514 - the five window commits keep relative
     newest-first order in git log. STALENESS-PROOF by design: it asserts
     relative order, not adjacency, so later commits (515+) cannot break it.
     This is the deliberate successor to #510's static-list git-order guard,
     which failed this run and was repaired dynamic in the same file.
  4. TestWindowDataMechanismIntegrity511to514 - YAML facts each window run
     claimed (new window: 511 podcast section, 512 gizmodo mechanism,
     513 Kerr competitor_coverage block, 514 entities.openai mechanism).
  5. TestScorerDeltaConsistencySince510 - delta-only re-audit: scorer blocks
     tied to 512/513 verified against the engine rule; 514 asserted
     qualitative-only (no scorer block). #510 did the full 28-block audit;
     this covers only what changed since.
  6. TestSiblingMechanismKeyUniqueness - text-level scan: no duplicate
     mechanism_NNN/type_b_NNN sibling keys within the same mapping.
     PyYAML silently keeps the last duplicate in one mapping, so a
     copy-paste collision would corrupt data without a parse error.
     Cross-journalist repetition of a shared mechanism number (e.g. 207)
     is by design and is NOT flagged; only same-parent duplicates fail.
  7. TestIterationLogEntrySectionCompleteness - each 511-514 entry carries the
     standard sections (rotation transparency, novelty, method, stats,
     confounders, counter-evidence, artifact readiness, doc sync, cumulative).

Failure repair this run: #510's TestGitOrderConsistency asserted a static
[509..505] list and failed on 1 of 291 tests; repaired dynamic in that file
(newest-five consecutive, anchored to live newest) and re-run green.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
PODCAST = REPO / "podcast-sentiment.md"

WINDOW = {
    511: ("E", "tests/test_type_e_511_podcast_sentiment_twentyfifth_verification_sep04_5am.py", 34),
    512: ("A", "tests/test_type_a_512_gizmodo_google_null_tie_symmetric_adversarial_sep04_6am.py", 50),
    513: ("B", "tests/test_type_b_513_dara_kerr_meta_openai_genre_conditioned_register_split_sep04_7am.py", 35),
    514: ("C", "tests/test_type_c_514_guardian_openai_strategic_partnership_sep04_8am.py", 17),
}


def _load(name):
    return yaml.safe_load((PROFILES / name).read_text(encoding="utf-8"))


def _log_sections():
    """Split iteration-log.md into {number: (type_letter, body)} for 511-514."""
    text = LOG.read_text(encoding="utf-8")
    heads = [(m.start(), int(m.group(1)), m.group(2)) for m in re.finditer(r"^#(\d+) Type ([A-E]):", text, re.M)]
    out = {}
    for idx, (start, num, tletter) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(text)
        if num in WINDOW:
            out[num] = (tletter, text[start:end])
    return out


class TestRotation511to514CycleIntegrity:
    def test_window_headings_newest_first_with_correct_types(self):
        sections = _log_sections()
        assert sorted(sections) == [511, 512, 513, 514], (
            f"expected log sections for 511-514, got {sorted(sections)}"
        )
        order = [(n, sections[n][0]) for n in (514, 513, 512, 511)]
        assert order == [(514, "C"), (513, "B"), (512, "A"), (511, "E")], (
            f"rotation order broken, got {order}"
        )

    def test_each_entry_names_its_predecessor(self):
        sections = _log_sections()
        expected = {514: "513 B", 513: "512 A", 512: "511 E", 511: "510 D"}
        for num, pred in expected.items():
            body = sections[num][1]
            assert "Rotation Transparency" in body, f"#{num} missing Rotation Transparency section"
            assert pred in body, (
                f"#{num} Rotation Transparency does not reference predecessor {pred}"
            )


class TestDocSurfaceCompleteness511to514:
    def test_readme_rows_present_with_correct_counts(self):
        readme = README.read_text(encoding="utf-8")
        for num, (_, fname, count) in WINDOW.items():
            base = fname.rsplit("/", 1)[-1]
            m = re.search(r"\| `" + re.escape(base) + r"` \| (\d+) \|", readme)
            assert m, f"README missing table row for #{num} file {base}"
            assert int(m.group(1)) == count, (
                f"README row for #{num} claims {m.group(1)} tests, expected {count}"
            )

    def test_readme_row_counts_match_def_counts(self):
        for num, (_, fname, count) in WINDOW.items():
            defs = sum(
                1 for line in (REPO / fname).read_text(encoding="utf-8").splitlines()
                if re.match(r"(?:    )?def test_", line)
            )
            assert defs == count, (
                f"#{num} file has {defs} test defs, README row claims {count}"
            )

    def test_architecture_tree_rows_present(self):
        arch = ARCH.read_text(encoding="utf-8")
        for num, (_, fname, _) in WINDOW.items():
            base = fname.rsplit("/", 1)[-1]
            assert base in arch, f"ARCHITECTURE.md missing tree row for #{num} file {base}"


class TestGitCommitRelativeOrder510to514:
    def test_window_commits_keep_relative_newest_first_order(self):
        # Staleness-proof: asserts relative order of the window commits in
        # git history, so future commits above the window cannot break it.
        proc = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=REPO, capture_output=True, text=True, timeout=60,
        )
        nums = [int(m.group(1)) for m in re.finditer(r"Type [A-E] #(\d+)", proc.stdout)]
        window = [n for n in nums if 510 <= n <= 514]
        assert window == [514, 513, 512, 511, 510], (
            f"window commits out of relative order in git log: {window}"
        )


class TestWindowDataMechanismIntegrity511to514:
    def test_512_mechanism_key_in_gizmodo_google_block(self):
        d = _load("gizmodo.yaml")
        google = d["competitor_relationships"]["google"]
        assert any("mechanism_512" in k for k in google), (
            "mechanism_512_gizmodo_google_null_tie_symmetric_adversarial missing "
            "from gizmodo.yaml competitor_relationships.google"
        )
        mech = next(v for k, v in google.items() if "mechanism_512" in k)
        assert mech["mechanism_id"] == 512
        assert mech["iteration_type"] == "A"

    def test_513_competitor_coverage_block_on_dara_kerr(self):
        d = _load("careers/journalists.yaml")
        kerr = next(
            j for j in d["journalists"] if j.get("name") == "Dara Kerr"
        )
        assert "competitor_coverage" in kerr, "Dara Kerr entry missing competitor_coverage"
        assert any("type_b_513" in k for k in kerr["competitor_coverage"]), (
            "type_b_513_dara_kerr block missing from Kerr competitor_coverage"
        )
        block = next(v for k, v in kerr["competitor_coverage"].items() if "type_b_513" in k)
        assert block["iteration"] == 513
        assert block["type"] == "B"
        assert block["date"] == "2026-09-04"

    def test_514_mechanism_key_in_competitor_entities_openai(self):
        d = _load("competitor-entities.yaml")
        openai = d["entities"]["openai"]
        assert any("mechanism_514" in k for k in openai), (
            "mechanism_514_guardian_openai_strategic_partnership missing from "
            "competitor-entities.yaml entities.openai"
        )
        mech = next(v for k, v in openai.items() if "mechanism_514" in k)
        assert mech["mechanism_id"] == 514
        assert mech["iteration"] == 514

    def test_511_podcast_section_present(self):
        text = PODCAST.read_text(encoding="utf-8")
        assert "## Iteration #511" in text, "podcast-sentiment.md missing Iteration #511 section"


class TestScorerDeltaConsistencySince510:
    def _engine_rule_ok(self, block, label):
        p = block.get("p_value")
        sig = block.get("is_significant")
        if p == "NOT_CALCULATED":
            assert sig is False, f"{label}: NOT_CALCULATED p_value with is_significant true"
        elif isinstance(p, (int, float)):
            assert (p < 0.05) == bool(sig), (
                f"{label}: p_value {p} disagrees with is_significant {sig}"
            )
        else:
            pytest.fail(f"{label}: unrecognized p_value {p!r}")

    def test_512_scorer_block_consistent(self):
        d = _load("gizmodo.yaml")
        google = d["competitor_relationships"]["google"]
        mech = next(v for k, v in google.items() if "mechanism_512" in k)
        block = mech["asymmetry_scorer_result"]
        self._engine_rule_ok(block, "mechanism_512")
        assert block["p_value"] == 0.396
        assert block["is_significant"] is False
        calc = block["target_avg_tone"] - block["peer_avg_tone"]
        assert abs(block["asymmetry_score"] - calc) < 0.051, (
            f"mechanism_512 asymmetry_score {block['asymmetry_score']} != "
            f"target_avg_tone - peer_avg_tone = {calc}"
        )
        ci = block["confidence_interval"]
        assert ci[0] <= ci[1], f"mechanism_512 CI inverted: {ci}"

    def test_513_scorer_block_consistent(self):
        d = _load("careers/journalists.yaml")
        kerr = next(j for j in d["journalists"] if j.get("name") == "Dara Kerr")
        block = next(
            v for k, v in kerr["competitor_coverage"].items() if "type_b_513" in k
        )["asymmetry_scorer_result_illustrative"]
        self._engine_rule_ok(block, "type_b_513")
        assert block["p_value"] == "NOT_CALCULATED"
        assert block["is_significant"] is False
        assert block.get("correlation_not_causation") is True
        assert abs(block["target_avg"] - sum(block["target_scores"]) / len(block["target_scores"])) < 0.01
        assert abs(block["peer_avg"] - sum(block["peer_scores"]) / len(block["peer_scores"])) < 0.01
        calc = block["target_avg"] - block["peer_avg"]
        assert abs(block["delta"] - calc) < 0.01, (
            f"type_b_513 delta {block['delta']} != target_avg - peer_avg = {calc}"
        )

    def test_514_mechanism_has_no_scorer_block(self):
        d = _load("competitor-entities.yaml")
        openai = d["entities"]["openai"]
        mech = next(v for k, v in openai.items() if "mechanism_514" in k)
        assert not any("asymmetry_scorer_result" in k for k in mech), (
            "mechanism_514 is qualitative-only; an unexpected scorer block appeared"
        )


class TestSiblingMechanismKeyUniqueness:
    def test_no_duplicate_sibling_mechanism_keys(self):
        # PyYAML keeps only the last of two identical keys in one mapping,
        # so a copy-paste collision silently corrupts data. Scan textually:
        # duplicate numbers under DIFFERENT parents (shared mechanisms like
        # 207 recorded per-journalist) are by design and must not fail.
        import glob as _glob
        issues = []
        for f in _glob.glob(str(PROFILES / "**" / "*.yaml"), recursive=True):
            lines = Path(f).read_text(encoding="utf-8").splitlines()
            stack = []
            for i, line in enumerate(lines, 1):
                if not line.strip() or line.strip().startswith("#"):
                    continue
                m = re.match(r"^(\s*)([^\s].*?):", line)
                if not m:
                    continue
                indent, key = len(m.group(1)), m.group(2).strip().strip("'\"")
                while stack and stack[-1][0] >= indent:
                    stack.pop()
                if stack:
                    sibs = stack[-1][1]
                    if key in sibs and re.match(r"(mechanism_\d+|type_b_\d+)", key):
                        issues.append(f"{f}:{i} duplicate sibling key {key}")
                    sibs.append(key)
                stack.append((indent, [key]))
        assert not issues, "duplicate sibling mechanism keys:\n" + "\n".join(issues)


class TestIterationLogEntrySectionCompleteness:
    REQUIRED = [
        "Rotation Transparency",
        "Novelty Verification",
        "Research method",
        "Statistical discipline",
        "Confounders",
        "Counter-evidence",
        "Artifact readiness",
        "Doc sync",
        "Cumulative",
    ]

    def test_window_entries_carry_all_standard_sections(self):
        sections = _log_sections()
        for num in (511, 512, 513, 514):
            body = sections[num][1]
            missing = [s for s in self.REQUIRED if s not in body]
            assert not missing, f"#{num} entry missing sections: {missing}"
