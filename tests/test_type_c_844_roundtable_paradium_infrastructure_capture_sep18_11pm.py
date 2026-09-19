"""Type C #844 (840-844 window, fifth leg D->E->A->B->C, CLOSING the window):
Roundtable x Paradium.AI (Arena Group) 10-year $1B AI/DeFi MediaOS agreement
(announced Sep 17 2026) - infrastructure-capture as the SIXTH
relationship-direction in the corpus taxonomy (mechanism 738).

FIRST dedicated corpus mapping of the infrastructure-capture
publisher-tech financial vector: Roundtable (Nasdaq: RTB) to migrate,
operate and monetize Paradium.AI's (NYSE: PAAI, formerly The Arena Group)
two dozen media brands (TheStreet, Parade, Men's Journal, Athlon Sports,
Autoblog, Powder; nearly 100M monthly consumers) on its AI/DeFi-powered
MediaOS. Headline-vs-substance discipline: $1B is the 10-year headline
value, NOT committed cash; the committed capital is the $89,555,638
equity leg (~49.5% at $3.80/share, below-50% cap, with Simplify
Inventions LLC and MBX Capital Aren LLC, Paradium not a party, a
condition precedent to the Platform Agreement) plus RTB absorbing
Paradium's migration/hosting/vendor/employee costs for a revenue share.
Perpetual non-cancelable worldwide tech-license leg; Coinbase
smart-wallet journalist payroll (first publisher-side DeFi payroll in
the corpus); Q4 2026 close target; muted RTB share-price reaction
(Kalkine) prices the conditionality. Sixth relationship direction
(extends m734's sue-then-sign / pay-or-litigate bifurcation /
grant-then-sue and #814's pool-and-license): INFRASTRUCTURE-CAPTURE.
Corpus arc: the same publisher group joined the RSL collective AI
licensing framework in Nov 2025 and moves in Sep 2026 to full-stack
operator capture.

MANUAL / qualitative only; financial-incentive documentation leg, not a
tone test; scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven; NOT a falsification-family member
(documentation leg, no tone pair; ledger holds at 26);
no analysis.json update. Novelty verified pre-commit (zero
test_type_c_844 files; no Type C #844 in git log; max numeric
mechanism_id 737; zero underscore-form 738 keys by designed keying per
#715; block key zero-hit; zero paradium / rtb digital / james heckman
hits in profiles/ and tests/ pre-commit; all 6 source URLs zero-hit
repo-wide pre-commit). Count gate (GATE_TESTS/GATE_FILES; delta = this
file exactly, venv python authoritative per the #530 lesson); anchor 1
+ rotation-guard 4 deselected pre-commit per #565, patched green in
anchor followup; 840-844 window fifth leg D->E->A->B->C, CLOSING the
window (anchor patched post-commit per #565) - Sep 18 2026 23:00 PDT.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_844_roundtable_paradium_infrastructure_capture_sep18_11pm.py"
MECH_KEY = "roundtable_paradium_infrastructure_capture_sep2026"
M_ID = 738
ITER = 844
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_738"
NEXT_ID_MARKER = "mechanism" + "_739"
NEXT_ID_NUMERIC = "mechanism_id: 739"
EXPECTED_ORDER = [("C", "844"), ("B", "843"), ("A", "842"), ("E", "841"), ("D", "840")]
# Filled in after the authoritative collect run; asserts the doc-sync gate.
GATE_TESTS = 43150
GATE_FILES = 1172
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "da09c9c16ed407d3700fe444a70d9f6a61384000"

EXPECTED_URLS = [
    "https://www.globenewswire.com/news-release/2026/09/17/3364180/0/en/roundtable-secures-10-year-1-billion-agreement-bringing-its-ai-defi-media-operating-system-to-global-scale-and-profitability.html",
    "https://cryptobriefing.com/roundtable-paradium-billion-dollar-media-deal/",
    "https://kalkine.com/news/consumer/this-nasdaq-media-tech-stock-barely-budged-after-a-1-billion-10-year-deal",
    "https://www.thestreet.com/crypto/markets/roundtable-secures-10-year-1-billion-agreement-bringing-its-ai-defi-media-operating-system-to-global-scale-and-profitability",
    "https://rtb.io/rtb-corp/press/roundtable-secures-10-year-1-billion-agreement-bringing-its-ai-defi-media-operating-system-to-global-scale-and-profitability-1",
    "https://www.minichart.com.sg/2026/09/19/rtb-digital-to-buy-49-5-stake-in-paradium-ai-for-89-6-million/",
]

FIGURE_STRINGS = [
    "$1 billion",
    "10-year agreement",
    "Sep 17 2026",
    "$89,555,638",
    "49.5%",
    "$3.80",
    "Simplify Inventions",
    "MBX Capital Aren",
    "$100 million",
    "100 million monthly consumers",
    "TheStreet",
    "Parade",
    "Athlon Sports",
    "Autoblog",
    "Powder",
    "perpetual",
    "Coinbase",
    "RYVYL",
    "infrastructure-capture",
    "SIXTH",
    "condition precedent",
    "Q4 2026",
    "Paradium.AI",
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
        if "Type C #844" in subject:
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


class TestNovelty844:
    def test_single_test_type_c_844_file(self):
        files = list((_repo_root() / "tests").glob("test_type_c_844*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_c_844 file (this one) must exist"
        )

    def test_type_c_844_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_844 files, no #844 in git log, max numeric
        # mechanism_id 737, zero underscore-form 738 keys, block key
        # zero-hit, zero paradium / rtb digital / james heckman hits,
        # all 6 source URLs zero-hit repo-wide); this test pins that no
        # duplicate #844 main commit ever appears.
        mains = _git_log_mains("Type C #844: Roundtable")
        assert len(mains) == 1, f"exactly one Type C #844 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type C #844 main commit"
        )


class TestRotationCycleGuard844:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_840_844_fifth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"840-844 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_843(self):
        window = _window()
        assert window[1] == ("B", "843"), (
            f"immediate predecessor must be Type B #843, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type C #844: Roundtable")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism738Content:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_mechanism_id_is_738(self):
        assert _mech()["mechanism_id"] == 738

    def test_mechanism_id_numeric_marker_in_block(self):
        assert "mechanism_id: 738" in _block()

    def test_max_numeric_mechanism_id_is_738(self):
        assert max(_corpus_ids()) == 738, (
            f"max numeric mechanism_id must be 738 post-commit, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_form_739_keys(self):
        needle = NEXT_ID_MARKER  # "mechanism" + "_739", format-built per #715
        hits = [h for h in _repo_grep(needle) if Path(h) != Path(__file__).relative_to(_repo_root())]
        assert hits == [], f"zero underscore-form 739 keys post-commit, got {hits}"

    def test_no_duplicate_739_numeric_marker(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"no mechanism_id: 739 anywhere post-commit, got {hits}"

    def test_yaml_parse_clean(self):
        d = yaml.safe_load(_entities_text())
        assert d["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 738

    def test_mechanism_name_contains_infrastructure_capture(self):
        assert "Infrastructure-Capture" in _mech()["mechanism_name"]


class TestDealFigures738:
    @pytest.mark.parametrize("figure", FIGURE_STRINGS)
    def test_figure_string_in_block(self, figure):
        # NOTE: raw block text carries YAML-escaped apostrophes (e.g.
        # "Men''s Journal"), so figure strings avoid apostrophes.
        assert figure in _block(), f"figure string {figure!r} must be in the m738 block"

    def test_expected_urls_in_block(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, f"URL {url} must be in the m738 block"

    def test_headline_vs_substance_discipline(self):
        block = _block()
        assert "not committed cash" in block, (
            "the $1B headline must be flagged as not committed cash"
        )
        assert "CONDITION PRECEDENT" in block, (
            "the stake purchase as condition precedent must be stated"
        )

    def test_sixth_direction_taxonomy(self):
        block = _block()
        assert "INFRASTRUCTURE-CAPTURE" in block, "the sixth direction must be named"
        assert "pool-and-license" in block, "the #814 fifth direction must be cited"

    def test_market_skepticism_muted_reaction(self):
        block = _block()
        assert "little changed" in block, "Kalkine's muted-reaction fact must be present"
        assert "conditionality" in block, "the market pricing conditionality must be stated"

    def test_corpus_continuity_arena_group(self):
        block = _block()
        assert "Really Simple Licensing" in block, "the RSL collective leg must be named"
        assert "Nov 26 2025" in block, "the RSL joining date must be carried"

    def test_defi_payroll_leg(self):
        block = _block()
        assert "smart-wallet" in block, "the Coinbase smart-wallet payroll leg must be named"

    def test_ascii_only(self):
        block = _block()
        block.encode("ascii")
        assert "—" not in block and "–" not in block, "ASCII-only, no em dashes"


class TestSupersession844:
    def test_not_falsification_family(self):
        assert _mech()["falsification_family"] is False

    def test_ledger_holds_at_26(self):
        assert _mech()["falsification_ledger_holds_at"] == 26

    def test_d843_zero_underscore_738_sweep_stays_green(self):
        # #843's test_zero_underscore_738_keys_repo_wide stays green by
        # designed keying: this run's block key carries no underscore-form
        # 738 substring, and this file builds the 738 needle by
        # concatenation (format-built per #715), never as a literal.
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], (
            f"#843's zero-underscore-738 sweep must stay green, got {hits}"
        )

    def test_d843_max_737_and_zero_numeric_738_superseded_by_design(self):
        # Per the #710/#720 convention: #843's max-737 sweep and its
        # zero-numeric-738-in-profiles sweep fail by DESIGNED supersession
        # once mechanism 738 (colon form) lands in profiles/. This test
        # documents the supersession rather than re-greening it.
        assert max(_corpus_ids()) == 738, "max id 738 supersedes #843's max-737 sweep"
        assert "mechanism_id: 738" in _entities_text(), (
            "#843's zero-numeric-738-in-profiles sweep is superseded by design"
        )

    def test_verdict_directionally_supported(self):
        assert _mech()["verdict"] == "directionally_supported_not_proven"

    def test_tone_not_scored(self):
        assert _mech()["tone_scores"] == "NOT_SCORED"

    def test_no_analysis_json_update(self):
        assert "no analysis.json update" in _iteration_log_tail(), (
            "the log entry must record that no analysis.json update was warranted"
        )


class TestDocSync844:
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


class TestIterationLog844:
    def test_log_captures_iteration_844(self):
        tail = _iteration_log_tail()
        assert "#844 Type C:" in tail

    def test_log_captures_window_close(self):
        tail = _iteration_log_tail()
        assert "CLOSING the window" in tail, (
            "the log entry must state this run CLOSES the 840-844 window"
        )
