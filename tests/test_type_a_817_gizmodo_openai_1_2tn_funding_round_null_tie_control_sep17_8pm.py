"""Type A #817 (815-819 window, third leg D->E->A): Gizmodo x OpenAI $1.2tn
funding-round register - FOURTH null-tie control on the FT-scooped peg
(mechanism 721).

FOURTH null-tie control in the Gizmodo family (#512 Gizmodo x Google, #577
Gizmodo x Anthropic, #582 Gizmodo x OpenAI rogue-agent incidents). First
peg-matched cross-outlet test of the licensing-incentive gradient on the
Sep 15 2026 FT-scooped $1.2tn OpenAI pre-IPO funding-round peg: three tied
publications (FT, $5-10M/yr, m718; WSJ/News Corp, $50M/yr, m715 relay;
WIRED/Conde Nast, m712 relay) all ran constructive or straight relay
registers on the identical peg; Gizmodo (financial_tie: none, $0, no AI
licensing deals per its profile) ran a skeptical-deflationary horserace
register (-0.20 MANUAL ILLUSTRATIVE, first-hand read this run, 33 rendered
lines). The non-payer did not soften: illustrative Gizmodo-minus-FT delta
-0.45 on the identical peg. Arm 2 carried un-rescored from m582 (three
first-hand OpenAI pieces); Meta comparator carried un-rescored (m582 Meta
arms + m716 "pervert glasses"/"creeps" anchor). Strong confounders ranked
strong-first (house adversarialism: Gizmodo adversarial on Meta too; genre
asymmetry within the peg: original scoop vs aggregation-with-commentary).
Counter-evidence carried: m676 (FT constructive on NON-payer Anthropic
+0.20), m582 (zero ties produce no entity gap at this outlet), peg-driven
relay convergence (cf. m679 WSJ -0.40 expose on the payer same week),
Altman safety quotes relayed straight. MANUAL ILLUSTRATIVE scores only;
engine NOT run on the illustrative arms per the Aug 28 2026 standing rule;
engine run once as a DEGENERATE n=1 check (calculate_asymmetry([-0.20],
[0.25]) returns asymmetry_score -0.45; t 0.0 / p 1.0 / Cohen d 0.0 /
degenerate CI (-0.45, -0.45) / is_significant False; no significance
claimed). NOT a falsification-family member (ledger holds at 26);
no analysis.json update. Novelty verified pre-commit (zero test_type_a_817
files; no 'Type A #817' in git log; the 2000812142 URL zero-hit repo-wide;
block key zero-hit; max numeric mechanism_id 720; zero underscore-form 721
keys by designed keying per #715); count_stats gate (41859/1145; delta
+47/+1 = the #817 file exactly); 815-819 window third leg D->E->A (anchor
patched post-commit per #565) - Sep 17 2026 20:00 PDT - 47 tests, 7
classes.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_817_gizmodo_openai_1_2tn_funding_round_null_tie_control_sep17_8pm.py"
MECH_KEY = "gizmodo_openai_1_2tn_funding_round_null_tie_control_sep17"
M_ID = 721
ITER = 817
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_721"
NEXT_ID_MARKER = "mechanism" + "_722"
NEXT_ID_NUMERIC = "mechanism_id: 722"
EXPECTED_ORDER = [("A", "817"), ("E", "816"), ("D", "815"), ("C", "814"), ("B", "813")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "ae7f94074aa034511b8bddc7ace2d39a93bb60d0"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "gizmodo.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:")
    return text[start:end]


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
        if "Type A #817" in subject:
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


class TestNovelty817:
    def test_single_test_type_a_817_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_817*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_817 file (this one) must exist"
        )

    def test_type_a_817_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_817 files, no #817 in git log, the
        # 2000812142 URL zero-hit repo-wide, block key zero-hit, max numeric
        # mechanism_id 720, zero underscore-form 721 keys); this test pins
        # that no duplicate #817 main commit ever appears.
        mains = _git_log_mains("Type A #817: gizmodo")
        assert len(mains) == 1, f"exactly one Type A #817 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #817 main commit"
        )


class TestRotationCycleGuard817:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_815_819_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"815-819 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_816(self):
        window = _window()
        assert window[1] == ("E", "816"), (
            f"immediate predecessor must be Type E #816, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #817: gizmodo")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism721Content:
    def test_block_key_exists_in_gizmodo_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "mechanism_id: 721" in block
        assert "iteration: 817" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-17 20:00 PDT" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication_pair: Gizmodo x OpenAI" in block
        assert "competitor: openai" in block
        assert 'entity_pair: "OpenAI vs Meta"' in block

    def test_arm1_url_and_register(self):
        block = _block()
        assert (
            "rumored-round-of-funding-could-make-openai-more-valuable-than-anthropic-again-perhaps-briefly-2000812142"
            in block
        )
        assert "register: skeptical_deflationary_horserace" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.20" in block

    def test_arm1_headline_skeptical_qualifiers(self):
        block = _block()
        assert "Rumored Round of Funding" in block
        assert "Perhaps Briefly" in block
        assert "skeptical qualifier plus a diminutive" in block

    def test_arm1_insider_claiming_and_timing_suspicion(self):
        block = _block()
        assert "Insiders are claiming" in block
        assert "anonymous-source skepticism verb" in block
        assert "intriguingly timed round" in block
        assert "Amodei-slowdown week" in block

    def test_arm1_decline_framing_and_sora_dig(self):
        block = _block()
        assert "once the clear leader in frontier AI" in block
        assert "decline framing" in block
        assert "scrapped projects" in block
        assert "Sora" in block
        assert "direct dig" in block
        assert "proportionally less dramatic valuation spike" in block

    def test_arm1_horserace_closing(self):
        block = _block()
        assert "perhaps only briefly" in block
        assert "retake the top spot" in block
        assert "frames OpenAI as chasing Anthropic" in block
        assert "deflated by the Anthropic $2tn-IPO comparator" in block

    def test_arm1_altman_quotes_relayed_straight(self):
        block = _block()
        assert "would not go public in 2026" in block
        assert "easier as a private company" in block
        assert "company voice carried, not distorted" in block

    def test_arm1_ft_scoop_credited(self):
        block = _block()
        assert "according to the Financial Times" in block
        assert "the tied originator is attributed, not laundered" in block

    def test_arm1_byline_bounded_absence(self):
        block = _block()
        assert "not surfaced in page render" in block
        assert "bounded absence per #503" in block
        assert "no byline invented" in block
        assert "33 rendered lines" in block

    def test_arm2_carried_register_pattern(self):
        block = _block()
        assert "Carried un-rescored from m582" in block
        assert "2000807447" in block
        assert "2000804424" in block
        assert "2000807665" in block

    def test_meta_comparator_carried(self):
        block = _block()
        assert "2000721970" in block
        assert "2000784400" in block
        assert "2000750107" in block
        assert "pervert glasses" in block
        assert "creeps" in block

    def test_peg_matched_tied_comparators(self):
        block = _block()
        assert "FT m718" in block
        assert "WSJ m715" in block
        assert "WIRED m712" in block
        assert "$50M/yr" in block
        assert "mechanism 54" in block

    def test_illustrative_delta_and_scores(self):
        block = _block()
        assert "illustrative_register_delta_gizmodo_minus_ft: -0.45" in block
        assert "gizmodo_arm_scores: [-0.20]" in block
        assert "ft_arm_scores: [0.25]" in block
        assert "-0.20 - 0.25 = -0.45" in block

    def test_fourth_null_tie_control_lineage(self):
        block = _block()
        assert "FOURTH null-tie control" in block
        assert "#512 Gizmodo x Google" in block
        assert "#577 Gizmodo x Anthropic" in block
        assert "#582 Gizmodo x OpenAI rogue-agent" in block
        assert "financial_tie: none" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _block()
        assert "verdict: directionally_supported_not_proven" in block
        assert "The non-payer did not soften" in block
        assert "NOT proven" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "House adversarialism" in block
        assert "Genre asymmetry within the peg" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_counter_evidence_present(self):
        block = _block()
        assert "counterevidence:" in block
        assert "m676" in block
        assert "NON-payer" in block
        assert "m582" in block
        assert "peg-driven" in block
        assert "m679" in block
        assert "-0.40 expose" in block

    def test_statistical_discipline_manual_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE tones only" in block
        assert "calculate_asymmetry([-0.20], [0.25]) returns asymmetry_score -0.45" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "degenerate CI (-0.45, -0.45)" in block
        assert "is_significant False" in block
        assert "no significance claimed" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_721_in_block(self):
        assert MECH_ID_MARKER not in _block(), (
            "designed keying: underscore-form marker must appear nowhere in block"
        )

    def test_research_method_and_bounded_absence(self):
        block = _block()
        assert "4 browser.search query sets this run" in block
        assert "bounded absence" in block
        assert "1 browser.open first-hand read this run" in block
        assert "no canonical URLs constructed" in block
        assert "ASCII-only" in block
        assert "no em dashes" in block

    def test_cross_references_to_family(self):
        block = _block()
        assert "mechanism 54" in block
        assert "m512" in block or "#512" in block
        assert "m577" in block or "#577" in block
        assert "m582" in block
        assert "m712" in block
        assert "m715" in block
        assert "m718" in block
        assert "m716" in block

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - null-tie control documentation" in block


class TestSupersessionAndCorpusPost816:
    def test_max_numeric_id_is_721_not_720(self):
        assert max(_corpus_ids()) == 721, (
            f"max numeric mechanism_id must be 721, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_722_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 722 keys anywhere"

    def test_zero_numeric_722_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 722 mechanism keys in the corpus"
        )

    def test_no_second_721_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; the
        # test_file backlink is absent here (no test_file field on this block),
        # so any second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d815_zero_underscore_721_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#815 zero-underscore-721 profiles sweep stays green by designed keying"
        )

    def test_d815_zero_underscore_721_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#815 zero-underscore-721 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d810_max_720_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 721, (
            "#810 max-720 sweep is superseded by design: the corpus now maxes at 721"
        )

    def test_engine_degenerate_check_recorded_but_not_in_analysis_json(self):
        block = _block()
        assert "calculate_asymmetry([-0.20], [0.25]) returns asymmetry_score -0.45" in block
        assert "no_analysis_json_update: true" in block


class TestLedger817:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        corpus = _repo_grep("TWENTY-SIXTH", roots=("profiles",))
        assert len(corpus) >= 1, "TWENTY-SIXTH must be present in profiles/"
        assert _repo_grep("TWENTY-SEVENTH", roots=("profiles",)) == [], (
            "TWENTY-SEVENTH must be absent in profiles/"
        )

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - null-tie control documentation" in block


class TestDocSync817:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 41859 |" in readme
        assert "Across 1145 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "41859" in arch and "1145" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog817:
    def test_log_captures_iteration_817(self):
        tail = _iteration_log_tail()
        assert "#817 Type A:" in tail
        assert "20:00 PDT" in tail
        assert "m721" in tail

    def test_log_states_815_819_window(self):
        assert "815-819" in _iteration_log_tail()
