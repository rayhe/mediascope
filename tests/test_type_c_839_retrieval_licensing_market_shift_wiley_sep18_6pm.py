"""Type C #839 (835-839 window, fifth leg D->E->A->B->C, CLOSING the window):
Retrieval licensing, not training licensing - the 2026 deal-structure shift
(Venu Prasad Menon, Sep 6 2026) + Wiley FY2026 $49M AI revenue disclosure
(mechanism 735).

FIRST corpus mechanism mapping the 2026 structural shift in AI-publisher
deals from TRAINING licensing to RETRIEVAL licensing (RAG/display/
attribution), per Menon's Sep 6 2026 LinkedIn analysis. Market quanta:
roughly $3B committed across roughly 50 publisher deals (2023-2026),
concentrated; OpenAI-News Corp $250M/5yr; Reddit $203M aggregate IPO
filing; Wiley FY2026 $49M AI licensing revenue, lifetime $110M+ (SUPERSEDES
the $44M Jan 2025 comparator); dataset market $3.6B (2025) -> $4.4B (2026);
dataset-licensing segment $4.8B (2025) -> $22B+ (2034). Mid-size publishers:
low hundreds of thousands/year at best, often nothing.

Incentive-theory refinement: retrieval/display legs and training legs carry
different incentive mechanics and must be WEIGHTED, not merely counted
against the #834 census of 13 Meta payer legs. Zero-disclosed-fee
attribution deals (India, mechanism 609-family) are unweightable; the
Cashmere RAG-only layer (714-family) is the pure-retrieval-leg example
corroborating Menon's shape. Meta sits on both sides (Dec 2025 bundle m331
and News Corp m549 mix retrieval display with archive training).

MANUAL / qualitative only; market-structure mapping, not a tone test;
scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; verdict directionally_supported_not_proven;
NOT a falsification-family member (structure audit + weighting rule +
Wiley figure update + market sizing; ledger holds at 26);
no analysis.json update. Novelty verified pre-commit (zero test_type_c_839
files; no Type C #839 in git log; max numeric mechanism_id 734; zero
underscore-form 735 keys by designed keying per #715; block key zero-hit;
zero menon-zpcoc / Wiley-FY2026 / lifetime-110M hits repo-wide; Menon URL
first URL to corpus; Adweek Anthropic zero-deal URL already corpus per #509,
not ingested as new; FourWeekMBA India URL first-URL citation, deal covered
by #624). Count gate (42889/1167; delta +42/+1 = this file exactly,
venv python authoritative per the #530 lesson); 37 green pre-commit
(including doc-sync 4 + iteration-log 2 per #719; novelty anchor 1 +
rotation-guard 4 deselected per #565, patched green in anchor followup);
835-839 window fifth leg
D->E->A->B->C, CLOSING the window (anchor patched post-commit per #565) -
Sep 18 2026 18:00 PDT.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_839_retrieval_licensing_market_shift_wiley_sep18_6pm.py"
MECH_KEY = "retrieval_licensing_not_training_market_structure_sep2026"
M_ID = 735
ITER = 839
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_735"
NEXT_ID_MARKER = "mechanism" + "_736"
NEXT_ID_NUMERIC = "mechanism_id: 736"
EXPECTED_ORDER = [("C", "839"), ("B", "838"), ("A", "837"), ("E", "836"), ("D", "835")]
# Filled in after the authoritative collect run; asserts the doc-sync gate.
GATE_TESTS = 42889
GATE_FILES = 1167
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

EXPECTED_URLS = [
    "https://www.linkedin.com/pulse/retrieval-licensing-training-ai-deal-structure-nobodys-menon-zpcoc",
    "https://llmpulse.ai/blog/ai-content-licensing-deals/",
    "https://fourweekmba.com/ai-openai-india-publisher-deals-attribution-strategy/",
]

FIGURE_STRINGS = [
    "$3 billion",
    "roughly 50 publisher deals",
    "$250 million",
    "$203 million",
    "$49 million",
    "$110 million",
    "$3.6 billion",
    "$4.4 billion",
    "$4.8 billion",
    "$22 billion",
    "Wiley FY2026",
    "Venu Prasad Menon",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _entities_text() -> str:
    return (_repo_root() / "profiles" / "competitor-entities.yaml").read_text()


def _block() -> str:
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\nadvance_dual_asset_monetization:")
    return text[start:end]


def _mech() -> dict:
    d = yaml.safe_load(_entities_text())
    return d["marketplace_intermediary_landscape"][MECH_KEY]


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
        if "Type C #839" in subject:
            mains[sha] = subject
    return mains


def _window(n: int = 40) -> list:
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


def _iteration_log_tail() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[-12000:]


class TestNovelty839:
    def test_single_test_type_c_839_file(self):
        files = list((_repo_root() / "tests").glob("test_type_c_839*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_c_839 file (this one) must exist"
        )

    def test_type_c_839_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_839 files, no #839 in git log, max numeric
        # mechanism_id 734, zero underscore-form 735 keys, block key
        # zero-hit, zero menon-zpcoc / Wiley-FY2026 / lifetime-110M hits,
        # Menon URL first URL to corpus); this test pins that no duplicate
        # #839 main commit ever appears.
        mains = _git_log_mains("Type C #839: Retrieval")
        assert len(mains) == 1, f"exactly one Type C #839 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type C #839 main commit"
        )


class TestRotationCycleGuard839:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_835_839_fifth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"835-839 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_838(self):
        window = _window()
        assert window[1] == ("B", "838"), (
            f"immediate predecessor must be Type B #838, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type C #839: Retrieval")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism735Content:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_mechanism_id_is_735(self):
        assert _mech()["mechanism_id"] == 735

    def test_mechanism_id_numeric_marker_in_block(self):
        assert "mechanism_id: 735" in _block()

    def test_max_numeric_mechanism_id_is_735(self):
        assert max(_corpus_ids()) == 735, (
            f"max numeric mechanism_id must be 735 post-commit, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_form_736_keys(self):
        needle = NEXT_ID_MARKER  # "mechanism" + "_736", format-built per #715
        hits = [h for h in _repo_grep(needle) if Path(h) != Path(__file__).relative_to(_repo_root())]
        assert hits == [], f"zero underscore-form 736 keys post-commit, got {hits}"

    def test_no_duplicate_735_numeric_marker(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"no mechanism_id: 736 anywhere post-commit, got {hits}"

    def test_yaml_parse_clean(self):
        d = yaml.safe_load(_entities_text())
        assert d["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 735


class TestMarketFigures735:
    @pytest.mark.parametrize("figure", FIGURE_STRINGS)
    def test_figure_string_in_block(self, figure):
        assert figure in _block(), f"figure string {figure!r} must be in the m735 block"

    def test_expected_urls_in_block(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, f"URL {url} must be in the m735 block"

    def test_wiley_supersession_note(self):
        block = _block()
        assert "$44M" in block, "the superseded $44M Jan 2025 comparator must be named"
        assert "SUPERSEDE" in block, "the block must state the $44M figure is superseded"

    def test_incentive_weighting_rule(self):
        block = _block()
        assert "weighted" in block, "the weighting rule (not merely counted) must be stated"

    def test_zero_fee_attribution_deals_unweightable(self):
        block = _block()
        assert "unweightable" in block, "zero-disclosed-fee attribution legs must be called unweightable"

    def test_corpus_corroboration_cited(self):
        block = _block()
        assert "Cashmere" in block, "the Cashmere RAG-only layer must corroborate the retrieval shape"
        assert "609" in block, "the India attribution-deal mechanism family must be cited"
        assert "834" in block, "the #834 Meta census must be cited as the legs base"

    def test_ascii_only(self):
        block = _block()
        block.encode("ascii")
        assert "—" not in block and "–" not in block, "ASCII-only, no em dashes"


class TestSupersession839:
    def test_not_falsification_family(self):
        assert _mech()["falsification_family"] is False

    def test_ledger_holds_at_26(self):
        assert _mech()["falsification_ledger_holds_at"] == 26

    def test_verdict_directionally_supported(self):
        assert _mech()["verdict"] == "directionally_supported_not_proven"

    def test_tone_not_scored(self):
        assert _mech()["tone_scores"] == "NOT_SCORED"

    def test_no_analysis_json_update(self):
        assert "no analysis.json update" in _iteration_log_tail(), (
            "the log entry must record that no analysis.json update was warranted"
        )


class TestDocSync839:
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


class TestIterationLog839:
    def test_log_captures_iteration_839(self):
        tail = _iteration_log_tail()
        assert "#839 Type C:" in tail
        assert "18:00 PDT" in tail
        assert "m735" in tail

    def test_log_states_835_839_window(self):
        assert "835-839" in _iteration_log_tail()
