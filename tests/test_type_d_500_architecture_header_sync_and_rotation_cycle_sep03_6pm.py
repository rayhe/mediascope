"""
Type D #500 - Test & Verify: ARCHITECTURE.md stale header repair + cross-doc
header-agreement guard + 490-500 rotation-cycle integrity
Sep 3 2026 18:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation C->D

Failure inventory at run start (1 failure; 244 passed across the 496-499
window files plus the structural suite):
- test_structural_consistency.py::TestTestFileListingConsistency::test_architecture_test_file_count_header
  "ARCHITECTURE.md claims 826 test files, but 827 exist on disk."
  Root cause: the #499 run re-synced README.md headers via
  scripts/count_stats.py --check, which only covers README.md, and missed the
  parallel "N tests across M test files" header in the docs/ARCHITECTURE.md
  tests/ tree section (still 27615/826 from the #498 sync).

Fix applied by this iteration (docs only, no test logic touched):
- docs/ARCHITECTURE.md tests/ tree header -> authoritative count_stats.py
  numbers (re-synced after this file and its doc rows landed).

New durable guards in THIS file:
- Cross-doc header agreement: the first "N tests across M test files" header
  in README.md and in docs/ARCHITECTURE.md must agree on both numbers, and
  the file count must equal the test_*.py files on disk. This is the exact
  shape of the #499 miss (README-only sync tooling).
- Rotation-cycle integrity: iterations 490-500 keep newest-first relative
  order AND the expected A->B->C->D->E type sequence. Newest-first:
  500/D 499/C 498/B 497/A 496/E 495/D 494/C 493/B 492/A 491/E 490/D.

Statistical discipline: metadata and repo-integrity only; no tone scores,
no p_value, no significance claimed.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 500 Type D 2026-09-03 18:00 PDT
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "iteration-log.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
SCRIPTS = REPO / "scripts"
TESTS_DIR = REPO / "tests"

FILE_500 = "test_type_d_500_architecture_header_sync_and_rotation_cycle_sep03_6pm.py"
WINDOW_FILES = {
    496: "test_type_e_496_podcast_sentiment_twentysecond_verification_sep03_2pm.py",
    497: "test_type_a_497_ft_google_deepmind_power_centre_replication_sep03_3pm.py",
    498: "test_type_b_498_kara_swisher_vox_openai_deal_falsification_sep03_4pm.py",
    499: "test_type_c_499_atlantic_openai_partnership_sep03_5pm.py",
}
# Newest-first expectation, verified against the log 2026-09-03
# (490 D 08:00 through 499 C 17:00).
EXPECTED_NEWEST_FIRST = [
    (500, "D"),
    (499, "C"),
    (498, "B"),
    (497, "A"),
    (496, "E"),
    (495, "D"),
    (494, "C"),
    (493, "B"),
    (492, "A"),
    (491, "E"),
    (490, "D"),
]

# Line-anchored heading match only. Per the #495b lesson, entry prose can
# quote heading literals mid-line, so an unanchored substring search can
# match a quotation instead of the real heading.
_HEADING_RE = re.compile(r"^#(\d+) Type ([A-E]):", re.MULTILINE)
# The README prose header uses markdown bold ("**27660 tests** across ..."),
# so the match must tolerate the bold markup. Fixed #500: the first version
# of this regex missed the README header entirely.
_COUNT_HEADER_RE = re.compile(r"(\d+) tests\*{0,2} across (\d+) test files")


def _headings():
    """iteration number -> (log position, hour type) for real headings."""
    found = {}
    for m in _HEADING_RE.finditer(LOG.read_text(encoding="utf-8")):
        found.setdefault(int(m.group(1)), (m.start(), m.group(2)))
    return found


def _count_header(doc_text):
    m = _COUNT_HEADER_RE.search(doc_text)
    assert m, "missing 'N tests across M test files' header"
    return int(m.group(1)), int(m.group(2))


class TestIteration500Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 500" in doc
        assert "2026-09-03" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_500


class TestRotationCycle490to500:
    def test_all_cycle_headings_present(self):
        headings = _headings()
        for num, _ in EXPECTED_NEWEST_FIRST:
            assert num in headings, f"heading for iteration {num} missing"

    def test_newest_first_relative_order(self):
        # Position-independent: the 490-500 window keeps newest-first order
        # wherever it sits in the log (durable form per #495).
        headings = _headings()
        positions = [headings[num][0] for num, _ in EXPECTED_NEWEST_FIRST]
        assert positions == sorted(positions), (
            "490-500 headings are not in newest-first relative order"
        )

    def test_hour_type_sequence(self):
        # The A->B->C->D->E rotation must hold across the whole window.
        headings = _headings()
        actual = [(num, headings[num][1]) for num, _ in EXPECTED_NEWEST_FIRST]
        assert actual == EXPECTED_NEWEST_FIRST


class TestWindow496to499Persistence:
    def test_window_test_files_exist(self):
        for num, fname in WINDOW_FILES.items():
            assert (TESTS_DIR / fname).exists(), f"#{num} file missing: {fname}"

    @pytest.mark.parametrize("fname", list(WINDOW_FILES.values()))
    def test_readme_rows_present(self, fname):
        assert fname in README.read_text(encoding="utf-8")

    @pytest.mark.parametrize("fname", list(WINDOW_FILES.values()))
    def test_architecture_rows_present(self, fname):
        assert fname in ARCH.read_text(encoding="utf-8")


class TestEntry500:
    def test_500_heading_unique(self):
        count = len(_HEADING_RE.findall(LOG.read_text(encoding="utf-8")))
        occurrences = [
            int(m.group(1))
            for m in _HEADING_RE.finditer(LOG.read_text(encoding="utf-8"))
        ]
        assert occurrences.count(500) == 1
        assert count >= 1  # sanity: the heading regex itself works

    def test_500_newest_relative(self):
        # #500 is newest iff it precedes #499; relative form stays true
        # forever (durable form per #495, no absolute-top assertion).
        headings = _headings()
        assert 500 in headings and 499 in headings
        assert headings[500][0] < headings[499][0]

    def test_500_rotation_transparency(self):
        headings = _headings()
        log = LOG.read_text(encoding="utf-8")
        seg = log[headings[500][0]:headings[499][0]]
        assert "499 C -> 500 D" in seg
        assert "next after C is D" in seg


class TestCrossDocHeaderAgreement:
    """Durable guard for the #499 miss: README-only sync tooling left the
    ARCHITECTURE.md tests/ tree header stale. Both docs' headers must agree
    with each other and with the files on disk."""

    def test_headers_agree(self):
        readme_tests, readme_files = _count_header(README.read_text(encoding="utf-8"))
        arch_tests, arch_files = _count_header(ARCH.read_text(encoding="utf-8"))
        assert (readme_tests, readme_files) == (arch_tests, arch_files), (
            f"README header {(readme_tests, readme_files)} != "
            f"ARCHITECTURE header {(arch_tests, arch_files)}"
        )

    def test_header_file_count_matches_disk(self):
        _, arch_files = _count_header(ARCH.read_text(encoding="utf-8"))
        on_disk = len(list(TESTS_DIR.glob("test_*.py")))
        assert arch_files == on_disk, (
            f"ARCHITECTURE header claims {arch_files} test files, "
            f"but {on_disk} exist on disk"
        )


class TestDocSync500:
    def test_count_stats_check_passes(self):
        """scripts/count_stats.py --check is the canonical README sync gate."""
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "count_stats.py"), "--check", "--pytest"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=str(REPO),
        )
        assert result.returncode == 0, (
            f"count_stats.py --check failed:\n{result.stdout}\n{result.stderr}"
        )

    def test_500_row_in_readme_table(self):
        assert FILE_500 in README.read_text(encoding="utf-8")

    def test_500_row_in_architecture_tree(self):
        assert FILE_500 in ARCH.read_text(encoding="utf-8")


class TestYamlIntegrity500:
    @pytest.mark.parametrize(
        "path",
        [
            REPO / "profiles" / "competitor-entities.yaml",
            REPO / "profiles" / "competitor-coverage-research.yaml",
            REPO / "profiles" / "the-verge.yaml",
            REPO / "profiles" / "careers" / "journalists.yaml",
        ],
    )
    def test_yaml_parses(self, path):
        assert yaml.safe_load(path.read_text(encoding="utf-8")) is not None
