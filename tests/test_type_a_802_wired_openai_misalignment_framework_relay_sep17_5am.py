"""Type A #802 (800-804 window, third leg E->A): WIRED x OpenAI misalignment-framework
relay register vs Meta glasses adversarial register (mechanism 712).

FIRST dedicated WIRED x OpenAI misalignment-framework mechanism. Arm 1: the WIRED
piece 'OpenAI Releases New Policy for Reporting Incidents of Model Misalignment'
(Sep 2026, characterized via SECONDARY attribution - two independent secondaries
attribute the Kai Chen quote to Wired; direct WIRED fetch failed terminally per
the #647 convention, so no first-hand page read was possible): OpenAI's new
incident-reporting policy gets a platform/relay register - the payer's own safety
framework and alignment chief are given the authoritative voice ('decisions about
AI development need evidence available to people outside frontier labs'; 'the
industry has not solved alignment and monitoring sufficiently to keep scaling at
maximum speed'; +0.15 MANUAL ILLUSTRATIVE). Arm 2 (in-corpus Meta comparator):
WIRED's Ray-Ban Meta / Oakley Meta smart-glasses coverage runs the adversarial
register ('pervert glasses', 'surveillance machine', 'destroying privacy',
'stealth mode', 'stalkers', 'abusers', -0.55 MANUAL ILLUSTRATIVE). Illustrative
OpenAI-minus-Meta delta +0.70. Financial tie: Conde Nast x OpenAI paid content
licensing deal (Aug 2024, estimated in-corpus at $1-5M/yr) while Meta pays Conde
Nast $0; WIRED's wired.yaml already carries deals_disclosed: false on OpenAI
coverage. Verdict directionally_supported_not_proven: direction consistent with
the financial-tie hypothesis but NOT proven - strong confounders ranked
strong-first (story-type selection: a framework announcement naturally invites
relay while watchdog requires unattempted original reporting; secondary-attribution
bound on the WIRED-arm characterization; same-week WSJ incident-listing shows the
relay register is not unique to the Conde Nast deal). Counter-evidence carried:
WIRED is NOT uniformly soft on OpenAI (Jul 10 2026 Maxwell Zeff Apple-hardware-IP
suit piece covers OpenAI adversarially; in-corpus WIRED 'rogue models' piece
covered OpenAI model misbehavior directly) - the register split is story-type
dependent, not blanket softening. MANUAL ILLUSTRATIVE scores only; engine NOT run
on the illustrative arms per the Aug 28 2026 standing rule; engine run once as a
DEGENERATE n=1 check (asymmetry 0.7000000000000001 matches manual delta; t 0.0 /
p 1.0 / Cohen d 0.0 / degenerate CI (0.70, 0.70) / is_significant false; no
significance claimed per the Aug 28 2026 standing rule). NOT a falsification-family
member (ledger holds at 26); no analysis.json update. Novelty verified pre-commit
(zero test_type_a_802 files; no 'Type A #802' in git log; max numeric
mechanism_id 711; zero underscore-form mechanism 712 key substrings repo-wide by
designed keying per #715/#723/#738/#739); count_stats gate (41139/1129; delta
+41/+1 = the #802 file exactly); 800-804 window third leg E->A (anchor patched
post-commit per #565) - Sep 17 2026 05:00 PDT - 41 tests, 7 classes.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_802_wired_openai_misalignment_framework_relay_sep17_5am.py"
MECH_KEY = "wired_openai_misalignment_framework_relay_sep17"
M_ID = 712
ITER = 802
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_712"
NEXT_ID_MARKER = "mechanism" + "_713"
NEXT_ID_NUMERIC = "mechanism_id: 713"
EXPECTED_ORDER = [("A", "802"), ("E", "801"), ("D", "800"), ("C", "799"), ("B", "798")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "competitor-coverage-research.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  fortune_ai_weekly_multi_episode_cross_entity_vocabulary_gradient:")
    return text[start:end]


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
        ["git", *_git_args_prefix(), *args],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_args_prefix() -> list:
    return []


def _git_log_oneline(*args: str) -> str:
    return _git("log", "--oneline", *args)


def _window(n: int = 40) -> list:
    subjects = _git("log", f"-{n}", "--format=%s").splitlines()
    return [
        (m.group(1), m.group(2))
        for m in (re.search(r"Type ([A-E]) #(\d+):", s) for s in subjects)
        if m
    ]


def _iteration_log_tail() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[-12000:]


def _git_log_mains(qualifier: str) -> dict:
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type A #802" in subject:
            mains[sha] = subject
    return mains


class TestNovelty802:
    def test_zero_type_a_802_files_precommit(self):
        files = list((_repo_root() / "tests").glob("test_type_a_802*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_802 file (this one) must exist pre-commit"
        )

    def test_no_type_a_802_in_git_log_precommit(self):
        assert "Type A #802" not in _git_log_oneline("--all"), (
            "no 'Type A #802' in git history before this iteration's commit"
        )

    def test_type_a_802_main_commit_unique_and_anchored(self):
        mains = _git_log_mains("Type A #802: wired")
        assert len(mains) == 1, f"exactly one Type A #802 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #802 main commit"
        )


class TestRotationCycleGuard802:
    def test_window_is_800_804_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"800-804 window third leg E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_no_out_of_window_type_a_commits(self):
        for letter, num in _window():
            if letter == TYPE_LETTER and num == str(ITER):
                continue
            assert not (
                letter == TYPE_LETTER and 796 <= int(num) <= 806
            ), f"unexpected Type A commit #{num} inside 796-806"

    def test_predecessor_is_type_e_801(self):
        window = _window()
        assert window[1] == ("E", "801"), (
            f"immediate predecessor must be Type E #801, got {window[1]}"
        )


class TestMechanism712Content:
    def test_block_key_exists_in_profiles_corpus(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "mechanism_id: 712" in block
        assert "iteration: 802" in block
        assert "iteration_type: A" in block
        assert "time_pdt: '05:00'" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_two_arm_structure(self):
        block = _block()
        assert "publication: WIRED (Conde Nast / Advance Publications)" in block
        assert "entity: OpenAI" in block
        assert "arm1_wired_openai_misalignment_relay:" in block
        assert "meta_comparator:" in block

    def test_arm1_register_and_illustrative_score(self):
        block = _block()
        assert "register: platform_relay_company_voice_authoritative" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block

    def test_wired_article_url_present(self):
        block = _block()
        assert (
            "openai-releases-new-policy-for-reporting-incidents-of-model-misalignment"
            in block
        )

    def test_secondary_attributions_and_bounding(self):
        block = _block()
        assert "subagentic.ai/posts/openai-misalignment-reporting/" in block
        assert "secondary_attributions:" in block
        assert "fetch_status: wired_page_fetch_blocked_per_647_convention" in block
        assert "search-excerpt-bounded per #503" in block

    def test_chen_quote_attributed(self):
        block = _block()
        assert "Kai Chen" in block
        assert "head of alignment research" in block
        assert "decisions about AI development need" in block

    def test_meta_comparator_vocab_in_block(self):
        block = _block()
        assert "pervert glasses" in block
        assert "surveillance machine" in block
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.55" in block

    def test_illustrative_delta_and_scores(self):
        block = _block()
        assert "illustrative_register_delta_openai_minus_meta: 0.70" in block
        assert "openai_arm_scores: [0.15]" in block
        assert "meta_arm_scores: [-0.55]" in block

    def test_conde_nast_paid_deal_and_non_disclosure(self):
        block = _block()
        assert "deal: Conde Nast x OpenAI paid content licensing" in block
        assert "$1-5M per year" in block
        assert "meta_pays: $0" in block
        assert "deals_disclosed_in_coverage: false" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _block()
        assert "Verdict: directionally_supported_not_proven" in block
        assert "directionally consistent with the" in block
        assert "financial-tie prediction" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Story-type selection" in block
        assert "Secondary-attribution bound" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence:" in block
        assert "Maxwell Zeff" in block
        assert "rogue models" in block
        assert "not a blanket softening" in block

    def test_statistical_discipline_manual_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE scores only." in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant False" in block
        assert "no significance claimed (Aug 28" in block
        assert "2026 standing rule)." in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_712_in_block_key(self):
        assert MECH_ID_MARKER not in _block(), (
            "designed keying: underscore-form marker must appear nowhere in block"
        )

    def test_research_method_transparency(self):
        block = _block()
        assert "6 browser.search" in block
        assert "1 browser.open (subagentic.ai" in block
        assert "browser.lookup_citation_url" in block
        assert "failed terminally" in block
        assert "search-excerpt-bounded per #503" in block

    def test_cross_references_to_family(self):
        block = _block()
        assert "mechanism_id: 8" in block
        assert "mechanism_id: 703" in block
        assert "mechanism_id: 709" in block
        assert "mechanism_id: 706" in block


class TestSupersessionAndCorpusPost801:
    def test_max_numeric_id_is_712_not_711(self):
        corpus = yaml.safe_load(_profiles_text())
        ids = [
            b["mechanism_id"]
            for b in corpus["publications"].values()
            if isinstance(b, dict) and "mechanism_id" in b
        ]
        assert max(ids) == 712, f"max numeric mechanism_id must be 712, got {max(ids)}"

    def test_zero_underscore_713_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 713 keys anywhere"

    def test_zero_numeric_713_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 713 mechanism keys in the corpus"
        )

    def test_no_second_712_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d799_zero_underscore_712_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#799 zero-underscore-712 profiles sweep stays green by designed keying"
        )

    def test_d799_zero_underscore_712_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#799 zero-underscore-712 tests sweep stays green (own file excluded)"
        )

    def test_d799_zero_numeric_712_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id: 712", roots=("profiles",))
        assert len(hits) >= 1, (
            "#799 zero-numeric-712 sweep is superseded by design: the #802 block "
            "is the single numeric 712 key"
        )

    def test_d799_max_711_sweep_superseded_by_design(self):
        corpus = yaml.safe_load(_profiles_text())
        ids = [
            b["mechanism_id"]
            for b in corpus["publications"].values()
            if isinstance(b, dict) and "mechanism_id" in b
        ]
        assert max(ids) == 712, (
            "#799 max-711 sweep is superseded by design: the corpus now maxes at 712"
        )

    def test_engine_degenerate_check_recorded_but_not_in_analysis_json(self):
        block = _block()
        assert "calculate_asymmetry([0.15], [-0.55]) returns asymmetry 0.70" in block
        assert "no_analysis_json_update: true" in block


class TestLedger802:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        corpus = _profiles_text()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26." in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - register documentation with" in block


class TestDocSync802:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 41180 |" in readme
        assert "Across 1130 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "41180" in arch and "1130" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog802:
    def test_log_captures_iteration_802(self):
        tail = _iteration_log_tail()
        assert "#802 Type A:" in tail
        assert "05:00 PDT" in tail
        assert "m712" in tail

    def test_log_states_800_804_window(self):
        assert "800-804" in _iteration_log_tail()
