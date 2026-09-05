"""
Type D #505 - Test & Verify: repo-wide YAML parse guard + 501-505
rotation-cycle integrity + iteration-entry section-completeness guard
Sep 3 2026 23:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation C->D

Failure inventory at run start: risk-window files (499/500/501/502/503/504)
plus the structural suite - see the #505 iteration-log entry for the
verbatim result. Any failures found are repaired in the owning files;
this file only adds guards.

New durable guards in THIS file:
- Repo-wide YAML parse: every profiles/**/*.yaml must yaml.safe_load
  without error. Prior iterations asserted "YAML-parsed" by hand for each
  touched file (#494, #499, #502, #503, #504); no test ever covered the
  whole profiles tree, so a single bad edit in an untouched file would
  only surface at import time. This closes that gap.
- Rotation-cycle integrity: iterations 501-505 keep newest-first relative
  order AND the expected E->A->B->C->D type sequence (line-anchored
  headings per the #495b durable rule - entry prose quotes heading
  literals, so unanchored substring search is banned).
- Entry section completeness: every entry in the 501-505 window carries
  the five required sections (Rotation Transparency, Novelty Verification,
  Statistical discipline, Artifact readiness, Cumulative), checked inside
  the entry's own segment - not a head slice (per #495).

Statistical discipline: metadata and repo-integrity only; no tone scores,
no p_value, no significance claimed.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 505 Type D 2026-09-03 23:00 PDT
"""

import re
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "iteration-log.md"
PROFILES = REPO / "profiles"
TESTS_DIR = REPO / "tests"

FILE_505 = "test_type_d_505_yaml_parse_guard_and_rotation_cycle_sep03_11pm.py"

_TYPE_ITER_RE = re.compile(r"^test_type_[a-e]_(\d+)_")


def _iteration_number(name: str):
    """Iteration number from the numbered test-file convention, else None.

    The test_type_<x>_<NNN>_ convention started at iteration 410; every
    test file added since #505 follows it (git-verified in #535: all 29
    files added after 32ce001 are numbered). Non-numbered files are all
    pre-numbering-era, hence strictly older than #505.
    """
    m = _TYPE_ITER_RE.match(name)
    return int(m.group(1)) if m else None

# Newest-first expectation, verified against the log 2026-09-03
# (501 E 19:00 through 504 C 22:00, plus this 505 D 23:00 run).
EXPECTED_NEWEST_FIRST = [
    (505, "D"),
    (504, "C"),
    (503, "B"),
    (502, "A"),
    (501, "E"),
]

# Line-anchored heading match only (durable rule from #495b).
_HEADING_RE = re.compile(r"^#(\d+) Type ([A-E]):", re.MULTILINE)

REQUIRED_SECTIONS = [
    "Rotation Transparency",
    "Novelty Verification",
    "Statistical discipline",
    "Artifact readiness",
    "Cumulative",
]


def _headings():
    """iteration number -> (log position, hour type) for real headings."""
    found = {}
    for m in _HEADING_RE.finditer(LOG.read_text(encoding="utf-8")):
        found.setdefault(int(m.group(1)), (m.start(), m.group(2)))
    return found


def _segments():
    """iteration number -> entry body text (heading line to next heading)."""
    text = LOG.read_text(encoding="utf-8")
    matches = list(_HEADING_RE.finditer(text))
    segs = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        segs.setdefault(int(m.group(1)), text[m.start():end])
    return segs


def _profile_yamls():
    return sorted(PROFILES.rglob("*.yaml"))


class TestIteration505Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 505" in doc
        assert "2026-09-03" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_505


class TestRepoWideYamlParse:
    def test_profiles_tree_nonempty(self):
        files = _profile_yamls()
        assert len(files) >= 16, f"profiles tree shrank: {len(files)} yamls"

    def test_every_profile_yaml_parses(self):
        failures = []
        for f in _profile_yamls():
            try:
                doc = yaml.safe_load(f.read_text(encoding="utf-8"))
            except Exception as e:  # noqa: BLE001 - collecting, not hiding
                failures.append(f"{f.relative_to(REPO)}: {e}")
                continue
            assert doc is not None, f"{f.relative_to(REPO)} parsed to None"
        assert not failures, "YAML parse failures:\n" + "\n".join(failures)

    def test_competitor_entities_top_level(self):
        doc = yaml.safe_load((PROFILES / "competitor-entities.yaml").read_text(encoding="utf-8"))
        assert isinstance(doc, dict) and "entities" in doc

    def test_competitor_coverage_research_top_level(self):
        doc = yaml.safe_load(
            (PROFILES / "competitor-coverage-research.yaml").read_text(encoding="utf-8")
        )
        assert isinstance(doc, dict) and "cross_publication_findings" in doc

    def test_no_prior_repo_wide_yaml_guard(self):
        # Novelty (durable form, #535): no test file from BEFORE iteration
        # 505 globs the profiles tree for parsing. Iteration 505 itself and
        # numbered successors (iteration >= 505 - e.g. #510's doc-sync
        # landmine scan, committed Sep 4 in a0a1a47) are exempt: numbers are
        # assigned sequentially, so a numbered iteration >= 505 cannot
        # predate #505, and every non-numbered file is pre-numbering-era
        # (before #410). The bare self-exclusion form broke the moment #510
        # legitimately landed; per #530's repair precedent the owning file is
        # fixed, not bypassed.
        hits = []
        for f in TESTS_DIR.glob("test_*.py"):
            num = _iteration_number(f.name)
            if f.name == FILE_505 or (num is not None and num >= 505):
                continue
            src = f.read_text(encoding="utf-8")
            if "rglob" in src and ".yaml" in src and "safe_load" in src:
                hits.append(f.name)
        assert not hits, f"prior (pre-#505) repo-wide yaml guard exists: {hits}"


class TestRotationCycle501to505:
    def test_all_cycle_headings_present(self):
        headings = _headings()
        for num, _ in EXPECTED_NEWEST_FIRST:
            assert num in headings, f"heading for iteration {num} missing"

    def test_newest_first_relative_order(self):
        # Position-independent: the 501-505 window keeps newest-first order
        # wherever it sits in the log (durable form per #495).
        headings = _headings()
        positions = [headings[num][0] for num, _ in EXPECTED_NEWEST_FIRST]
        assert positions == sorted(positions), (
            "501-505 window is not newest-first: "
            + str([n for n, _ in EXPECTED_NEWEST_FIRST])
        )

    def test_type_sequence_e_a_b_c_d(self):
        # EXPECTED_NEWEST_FIRST is newest-first: 505 D ... 501 E.
        headings = _headings()
        seq = [headings[num][1] for num, _ in EXPECTED_NEWEST_FIRST]
        assert seq == ["D", "C", "B", "A", "E"], (
            f"expected newest-first D,C,B,A,E, got {seq}"
        )

    def test_adjacent_type_transitions_follow_rotation(self):
        # A->B->C->D->E->A is the only legal forward step; walk the
        # window oldest -> newest and check each step advances one slot.
        order = ["A", "B", "C", "D", "E"]
        headings = _headings()
        oldest_first = [num for num, _ in reversed(EXPECTED_NEWEST_FIRST)]
        for prev_num, next_num in zip(oldest_first, oldest_first[1:]):
            prev_t = headings[prev_num][1]
            next_t = headings[next_num][1]
            expected = order[(order.index(prev_t) + 1) % 5]
            assert next_t == expected, (
                f"rotation break: #{prev_num} {prev_t} -> #{next_num} {next_t}"
            )


class TestEntrySectionCompleteness501to505:
    def test_all_window_segments_found(self):
        segs = _segments()
        for num, _ in EXPECTED_NEWEST_FIRST:
            assert num in segs, f"no log segment for iteration {num}"

    @pytest.mark.parametrize("num", [505, 504, 503, 502, 501])
    def test_required_sections_present(self, num):
        seg = _segments()[num]
        missing = [s for s in REQUIRED_SECTIONS if s not in seg]
        assert not missing, f"#{num} entry missing sections: {missing}"

    @pytest.mark.parametrize("num", [505, 504, 503, 502, 501])
    def test_entry_names_its_type(self, num):
        expected = dict(EXPECTED_NEWEST_FIRST)[num]
        assert f"Type {expected}" in _segments()[num]
