"""
Type D #495 - Test & Verify: brittle self-top assertion repair + 491-494 window persistence
Sep 3 2026 13:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation C->D

Failure inventory at start of run (all caused by legitimate newest-first prepends):
- test_type_a_492...::test_iteration_log_rotation ......... asserted the whole log text starts with the #492 heading; broke when #493 landed
- test_type_a_492...::test_novelty_block_present ........... asserted inside a 6000-char head slice; broke when #493/#494 pushed #492 down
- test_type_b_493...::TestIterationLog493::test_log_starts_with_493 ... asserted the whole log starts with the #493 heading; broke when #494 landed
- test_type_b_493...::TestIterationLog493::test_log_names_fowler ... read only the first 4000 chars; broke when #494 landed
- test_type_d_490...::test_top_has_newest_first_490_then_488_headings ... absolute top-3 broke
- test_type_d_490...::test_newest_first_ordering_490_to_485 ... absolute top-6 broke
- test_type_d_490...::test_readme_header_counts_synced / test_architecture_header_counts_synced ... hardcoded counts stale
- test_structural_consistency.py::test_readme_per_file_test_counts ... README said 40 (collected) vs table convention (def counts: 28)
- test_structural_consistency.py::test_architecture_test_file_count_header ... stale header

Repairs applied by this iteration (all in the owning files, additive "fixed #495" notes):
- #492 file: relative newest-first ordering (493 > 492 > 491) + segment-scoped novelty block
- #493 file: relative ordering (494 > 493 > 492) + segment-scoped Fowler block
- #490 file: relative window ordering + dynamic header-sync via scripts/count_stats.py
- README: #490 per-file row 40 -> 28 (table convention is raw def counts; verified
  against test_ap_appeals_deep_dive.py: 11 defs + 2 parametrize, README says 11)

New durable guards in THIS file:
- Ban the brittle shapes repo-wide: whole-log .startswith("#NNN") and
  headings[0].startswith("#NNN") position assertions (existence checks like
  any(l.startswith("#488")) remain allowed).
- 491-494 window persistence in relative (position-independent) form.

Statistical discipline: metadata and repair integrity only; no tone scores,
no p_value, no significance claimed.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 495 Type D 2026-09-03 13:00 PDT
"""

import io
import re
import subprocess
import sys
import tokenize
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "iteration-log.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
SCRIPTS = REPO / "scripts"

FILE_491 = "test_type_e_491_podcast_sentiment_twentyfirst_verification_sep03_9am.py"
FILE_492 = "test_type_a_492_verge_google_samsung_glasses_149_correction_sep03_10am.py"
FILE_493 = "test_type_b_493_geoffrey_fowler_company_agnostic_privacy_testing_sep03_11am.py"
FILE_494 = "test_type_c_494_vox_media_openai_partnership_sep03_12pm.py"
FILE_495 = "test_type_d_495_brittle_assertion_repair_and_window_persistence_sep03_1pm.py"

# Whole-text receivers whose .startswith("#NNN") is a brittle absolute-top
# position assertion. Loop variables over lines (l, line) are existence
# checks and remain allowed.
_BRITTLE_STARTSWITH = re.compile(
    r"(?:\b(?:log|text|content)\.startswith\(\s*['\"]#\d{3}"
    r"|headings\[0\]\.startswith\(\s*['\"]#\d{3})"
)


def _strip_comments(source: str) -> str:
    """Remove # comments via tokenize so '#' inside strings is preserved."""
    out = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.COMMENT:
            continue
        out.append((tok.type, tok.string))
    return tokenize.untokenize(out)


def _heading_positions():
    log = LOG.read_text(encoding="utf-8")
    positions = {}
    for m in re.finditer(r"^#(\d+) Type [A-E]:", log, re.MULTILINE):
        positions.setdefault(int(m.group(1)), m.start())
    return positions


class TestIteration495Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 495" in doc
        assert "2026-09-03" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_495


class TestBrittleAssertionBan:
    """Repo-wide ban on the absolute-top assertion shapes that failed today.

    Rationale (fixed #495): iteration-log.md is newest-first, so any test
    asserting ITS OWN entry is at the absolute top (log.startswith("#NNN"))
    or inside a fixed head slice (log[:6000]) breaks the moment the next
    hourly iteration legitimately prepends. The durable form is relative
    newest-first ordering between neighboring entries.
    """

    def _offending_files(self):
        offenders = []
        for path in sorted((REPO / "tests").glob("test_*.py")):
            if path.name == Path(__file__).name:
                continue  # this guard file names the banned shapes in its self-test below
            code = _strip_comments(path.read_text(encoding="utf-8"))
            if _BRITTLE_STARTSWITH.search(code):
                offenders.append(path.name)
        return offenders

    def test_no_absolute_log_top_startswith(self):
        offenders = self._offending_files()
        assert not offenders, (
            "Brittle absolute-top log assertions found (use relative "
            "newest-first ordering instead):\n" + "\n".join(offenders)
        )

    def test_ban_covers_known_historical_shapes(self):
        # The ban regex must catch the exact shapes that failed in #492/#493.
        assert _BRITTLE_STARTSWITH.search('assert log.startswith("#492 Type A:")')
        assert _BRITTLE_STARTSWITH.search("assert headings[0].startswith('#490 Type D:')")
        # ...while allowing existence checks over lines.
        assert not _BRITTLE_STARTSWITH.search('any(l.startswith("#488 Type B:") for l in lines)')
        assert not _BRITTLE_STARTSWITH.search('assert meta["date"].startswith("2026-06")')

    def test_repaired_files_pass_ban(self):
        # The three files repaired this iteration must be clean, comments aside.
        repaired = (
            FILE_492,
            FILE_493,
            "test_type_d_490_log_repair_and_window_persistence_sep03_8am.py",
        )
        for fname in repaired:
            code = _strip_comments((REPO / "tests" / fname).read_text(encoding="utf-8"))
            assert not _BRITTLE_STARTSWITH.search(code), fname


class TestWindow491to494Persistence:
    def test_window_test_files_exist(self):
        for fname in (FILE_491, FILE_492, FILE_493, FILE_494):
            assert (REPO / "tests" / fname).exists(), fname

    def test_log_headings_newest_first_relative(self):
        # Position-independent: the 491-494 window keeps newest-first order
        # wherever it sits in the log.
        pos = _heading_positions()
        for n in (491, 492, 493, 494):
            assert n in pos, f"#{n} heading missing from iteration-log.md"
        assert pos[494] < pos[493] < pos[492] < pos[491]

    def test_495_entry_newest_and_unique(self):
        # #495 is newest iff it precedes #494; relative form stays true forever.
        pos = _heading_positions()
        assert 495 in pos, "#495 heading missing from iteration-log.md"
        assert pos[495] < pos[494]
        count = len(re.findall(r"^#495 Type D:", LOG.read_text(encoding="utf-8"), re.MULTILINE))
        assert count == 1

    def test_495_entry_rotation_transparency(self):
        # Line-anchored positions (same quoted-mention hazard as #492/#493).
        pos = _heading_positions()
        log = LOG.read_text(encoding="utf-8")
        seg = log[pos[495]:pos[494]]
        assert "494 C -> 495 D" in seg
        assert "next after C is D" in seg

    @pytest.mark.parametrize("fname", [FILE_491, FILE_492, FILE_493, FILE_494])
    def test_readme_rows_present(self, fname):
        assert fname in README.read_text(encoding="utf-8")

    @pytest.mark.parametrize("fname", [FILE_491, FILE_492, FILE_493, FILE_494])
    def test_architecture_rows_present(self, fname):
        assert fname in ARCH.read_text(encoding="utf-8")


class TestDocSync495:
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

    def test_495_row_in_readme_table(self):
        assert FILE_495 in README.read_text(encoding="utf-8")

    def test_495_row_in_architecture_tree(self):
        assert FILE_495 in ARCH.read_text(encoding="utf-8")


class TestYamlIntegrity495:
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
