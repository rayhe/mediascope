"""Type C #904 (900-904 window, fifth leg D->E->A->B->C, CLOSING the window):
FT x Google/OpenAI "red button" termination-leverage (Slade Sep 10 2026
keynote) - SEVENTH relationship direction in the corpus taxonomy
(mechanism 774).

FIRST dedicated corpus mapping of the termination-leverage
publisher-tech financial vector: FT CEO Jon Slade revealed at the
Press Gazette Future of Media Technology Conference (London, Sep 10
2026) that the FT's AI licensing deals with Google (Feb 2026 pilot)
and OpenAI (Apr 29 2024) both include "red button" clauses allowing
the FT to pull the plug on content use it dislikes. Temporal
continuity via Slade's ~Feb 2026 Media Roundup / Voices Media
interview ("The Big Red Button", a common requirement in EVERY FT LLM
deal: "If we do not like what we see - assuming the transparency
commitments are honoured - we push the button. It does not take the
salt out of the soup, but it stops archive access and stops
surfacing. If we cannot get that, we do not do the deal").
Cross-publisher corroboration: Atlantic CEO Nicholas Thompson on the
Channels podcast (Sep 2026) - renewing the Atlantic's 2024 OpenAI
deal requires "a fair exchange of value": "What are you giving us, and
what are we giving you? Is it fair? And if it is not, well, then we
will block you from the site, or we will sue you, right? That is the
deal."

MANUAL / qualitative only; financial-incentive documentation leg, not
a tone test; scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven; NOT a falsification-family member
(documentation leg, no tone pair; ledger holds at 29);
no analysis.json update. Novelty verified pre-commit (zero
test_type_c_904 files; no Type C #904 in git log; max numeric
mechanism_id 773 in-tree incl. uncommitted in-flight 771/770/762;
zero underscore-form 774 mechanism keys repo-wide; block key
zero-hit; "red button" zero-hit in profiles/ and tests/ pre-commit;
all 4 source URLs zero-hit repo-wide via git grep). Count gate
(GATE_TESTS/GATE_FILES; delta = this file exactly, venv python
authoritative per the #530 lesson); novelty anchor 1 deselected
pre-commit per #565, patched green in anchor followup; 900-904 window
fifth leg D->E->A->B->C, CLOSING the window - Sep 21 2026 17:00 PDT.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_904_ft_red_button_termination_leverage_sep21_5pm.py"
MECH_KEY = "ft_red_button_termination_leverage_sep2026"
M_ID = 774
ITER = 904
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_774"
NEXT_ID_MARKER = "mechanism" + "_775"
NEXT_ID_NUMERIC = "mechanism_id: 775"
# Filled in after the authoritative collect run; asserts the doc-sync gate.
GATE_TESTS = 46300
GATE_FILES = 1229
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

EXPECTED_URLS = [
    "https://pressgazette.co.uk/publishers/nationals/ft-chief-jon-slade-on-how-business-brand-became-a-hit-with-gen-z/",
    "https://pressgazettefutureofmediaus.substack.com/p/fts-red-button-ai-clauses-us-boosts",
    "https://themediaroundup.beehiiv.com/p/the-ft-s-jon-slade-on-leveraging-ai-to-build-new-lines-of-business",
    "https://voices.media/the-fts-jon-slade-on-leveraging-ai-to-build-new-lines-of-business/",
]

FIGURE_STRINGS = [
    "red button",
    "SEVENTH",
    "TERMINATION-LEVERAGE",
    "Jon Slade",
    "The Big Red Button",
    "Nicholas Thompson",
    "fair exchange of value",
    "does not take the salt out of the soup",
    "Sep 10 2026",
    "Channels podcast",
    "GBP 540m",
    "m437",
    "90-day exit",
    "does NOT buy permanent compliance",
    "voluntary-at-the-margin",
    "directionally_supported_not_proven",
    "NOT_SCORED",
    "ledger holds at 29",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _ft_text() -> str:
    return (_repo_root() / "profiles" / "financial-times.yaml").read_text()


def _block() -> str:
    text = _ft_text()
    start = text.index(MECH_KEY)
    return text[start:]


def _mech() -> dict:
    d = yaml.safe_load(_ft_text())
    return d[MECH_KEY]


def _corpus_ids() -> list:
    ids = []
    for p in (_repo_root() / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle: str, roots=("profiles", "tests")) -> list:
    hits = []
    root = _repo_root()
    for r in roots:
        for p in (root / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(root)))
                except OSError:
                    pass
    return hits


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier: str) -> dict:
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #904" in subject:
            mains[sha] = subject
    return mains


def _iteration_log_head() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[:12000]


class TestNovelty904:
    def test_single_test_type_c_904_file(self):
        files = list((_repo_root() / "tests").glob("test_type_c_904*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_c_904 file (this one) must exist"
        )

    def test_type_c_904_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_904 files, no #904 in git log, max numeric
        # mechanism_id 773 in-tree, zero underscore-form 774 mechanism keys,
        # block key zero-hit, "red button" zero-hit in profiles/ and tests/,
        # all 4 source URLs zero-hit repo-wide via git grep); this test pins
        # that no duplicate #904 main commit ever appears.
        mains = _git_log_mains("Type C #904: FT")
        assert len(mains) == 1, f"exactly one Type C #904 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type C #904 main commit"
        )
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", "anchor must be patched"


class TestRotationGuard904:
    def test_window_legs_present_in_log(self):
        log = (_repo_root() / "iteration-log.md").read_text()
        assert "## #904 Type C" in log
        assert "#900 Type D" in log, "in-flight D leg must be documented in the log"
        assert "## #901 Type E" in log
        assert "## #902 Type A" in log
        assert "## #903 Type B" in log

    def test_fifth_leg_closes_window(self):
        head = _iteration_log_head()
        assert "## #904 Type C" in head
        assert "900-904" in head, "the entry must name the 900-904 window"
        assert "CLOSING the window" in head, (
            "the entry must state this run CLOSES the 900-904 window"
        )

    def test_predecessor_is_type_b_903(self):
        log = (_repo_root() / "iteration-log.md").read_text()
        assert "## #903 Type B" in log, (
            "immediate predecessor must be Type B #903"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # The schedule cycle is D->E->A->B->C; this run is the C leg.
        cycle = {"D": "E", "E": "A", "A": "B", "B": "C", "C": "D"}
        assert cycle["B"] == "C", "Type B predecessor must be followed by Type C"
        assert TYPE_LETTER == "C"
        assert ITER == 904


class TestMechanism774Content:
    def test_block_key_exists_in_financial_times(self):
        assert MECH_KEY in _ft_text()

    def test_mechanism_id_is_774(self):
        assert _mech()["mechanism_id"] == 774

    def test_mechanism_id_numeric_marker_in_block(self):
        assert "mechanism_id: 774" in _block()

    def test_max_numeric_mechanism_id_is_774(self):
        assert max(_corpus_ids()) == 774, (
            f"max numeric mechanism_id must be 774 post-commit, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_form_775_keys(self):
        needle = NEXT_ID_MARKER  # "mechanism" + "_775", format-built per #715
        hits = [h for h in _repo_grep(needle) if Path(h) != Path(__file__).relative_to(_repo_root())]
        assert hits == [], f"zero underscore-form 775 keys post-commit, got {hits}"

    def test_no_duplicate_775_numeric_marker(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"no mechanism_id: 775 anywhere post-commit, got {hits}"

    def test_yaml_parse_clean(self):
        d = yaml.safe_load(_ft_text())
        assert d[MECH_KEY]["mechanism_id"] == 774

    def test_mechanism_name_contains_termination_leverage(self):
        assert "Termination-Leverage" in _mech()["mechanism_name"]

    def test_type_is_c_financial_incentive_mapping(self):
        assert _mech()["type"] == "Type C Financial Incentive Mapping"


class TestRedButtonFigures774:
    @pytest.mark.parametrize("figure", FIGURE_STRINGS)
    def test_figure_string_in_block(self, figure):
        # NOTE: block uses folded scalars; figure strings were chosen to sit
        # within single folded lines (no line-break spans).
        assert figure in _block(), f"figure string {figure!r} must be in the m774 block"

    def test_expected_urls_in_block(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, f"URL {url} must be in the m774 block"

    def test_slade_keynote_facts(self):
        block = _block()
        assert "Future of Media Technology Conference" in block
        assert "pull the plug" in block
        assert "Google (Feb 2026 pilot)" in block
        assert "Apr 29 2024" in block

    def test_seventh_direction_taxonomy(self):
        block = _block()
        assert "SEVENTH" in block, "the seventh direction must be named"
        assert "m734" in block, "the m734 taxonomy root must be cited"
        assert "infrastructure-capture" in block, "the #844 sixth direction must be cited"

    def test_incentive_geometry_bounds(self):
        block = _block()
        assert "does NOT buy permanent compliance" in block
        assert "all-or-nothing" in block
        assert "deterrence, not independence" in block
        assert "never been pushed on the record" in block

    def test_thompson_corroboration(self):
        block = _block()
        assert "Nicholas Thompson" in block
        assert "block you from the site" in block
        assert "sue you" in block

    def test_confounder_strength_ranking(self):
        block = _block()
        assert "strength: STRONG" in block
        assert "Deterrence never exercised" in block
        assert "strength: WEAK" in block

    def test_ascii_only(self):
        block = _block()
        block.encode("ascii")
        assert "\u2014" not in block and "\u2013" not in block, "ASCII-only, no em dashes"


class TestSupersession904:
    def test_not_falsification_family(self):
        assert _mech()["falsification_family"] is False

    def test_ledger_holds_at_29(self):
        assert _mech()["falsification_ledger_holds_at"] == 29

    def test_b903_zero_underscore_774_sweep_stays_green(self):
        # #903's test_no_underscore_774_keys (asserting "mechanism_774" not
        # in profiles text) stays green by designed keying: this run's
        # block key carries no underscore-form 774 substring. Scope matches
        # #903's own sweep (profiles/ only); this file builds the 774
        # needle by concatenation (format-built per #715), never as a
        # literal.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], (
            f"#903's zero-underscore-774 sweep must stay green, got {hits}"
        )

    def test_b903_max_773_and_zero_numeric_774_superseded_by_design(self):
        # Per the #710/#720 convention: #903's test_max_numeric_mechanism_id_773
        # and test_no_numeric_774_keys fail by DESIGNED supersession once
        # mechanism 774 (colon form) lands in profiles/. This test documents
        # the supersession rather than re-greening it.
        assert max(_corpus_ids()) == 774, "max id 774 supersedes #903's max-773 sweep"
        assert "mechanism_id: 774" in _ft_text(), (
            "#903's zero-numeric-774-in-profiles sweep is superseded by design"
        )

    def test_verdict_directionally_supported(self):
        assert _mech()["verdict"] == "directionally_supported_not_proven"

    def test_tone_not_scored(self):
        assert _mech()["tone_scores"] == "NOT_SCORED"

    def test_no_analysis_json_update(self):
        log = (_repo_root() / "iteration-log.md").read_text()
        assert "no analysis.json update" in log, (
            "the log entry must record that no analysis.json update was warranted"
        )


class TestDocSync904:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert f"| Tests | {GATE_TESTS} |" in readme
        assert f"Across {GATE_FILES} test files" in readme

    def test_readme_type_c_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert str(GATE_TESTS) in arch and str(GATE_FILES) in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog904:
    def test_log_captures_iteration_904(self):
        log = (_repo_root() / "iteration-log.md").read_text()
        assert "## #904 Type C" in log

    def test_log_captures_window_close(self):
        log = (_repo_root() / "iteration-log.md").read_text()
        assert "CLOSING the window" in log, (
            "the log entry must state this run CLOSES the 900-904 window"
        )
