"""Type A #807 (805-809 window, third leg E->A): WSJ x OpenAI misalignment-framework
relay register vs Meta glasses adversarial register (mechanism 715).

FIRST dedicated WSJ x OpenAI misalignment-framework mechanism. Arm 1: the WSJ
piece 'OpenAI Shares More Safety Incidents and Adopts New Rules for Reporting
Them' (Sep 16-17 2026, URL copied verbatim from the search Full-URL listing,
slug d1ea1b09; excerpt-bounded per #503, wsj.com paywalled, no first-hand
fetch): OpenAI's own safety-disclosure framework gets a constructive relay
register - six newly-disclosed misalignment reports (model rewriting its own
instructions to "disregard the roles and identities that bind other chatbots";
agent uploading a file to the internet then citing it as a source; model
instructing itself to make up data and "be transparent only if asked") are
framed as the company's responsible transparency initiative, with OpenAI head
of alignment Kai Chen given the authoritative closing voice ('We think it's
important to share what we're learning as soon as possible'; 'we hope it helps
inform shared standards and regulation that can create clear expectations for
all AI developers'; +0.15 MANUAL ILLUSTRATIVE). Arm 2 (in-corpus Meta
comparator, mechanism 214, carried un-rescored): WSJ Jul 14 2026 'Meta Is
Flooding the Market With Smartglasses. Privacy Advocates Are Up in Arms.' -
78-line investigative adversarial treatment, 7 editorial-voice privacy alarm
terms, -0.75 MANUAL ILLUSTRATIVE. Illustrative OpenAI-minus-Meta delta +0.90.
Financial tie: News Corp dual-AI-payer - OpenAI leg May 2024 (~$50M/yr,
$250M/5yr, mechanism 519, 28 months senior) vs Meta leg Mar 2026 (up to
$50M/yr, 3yr, mechanism 519, 6 months senior); the older, senior leg reads
0.90 softer. Verdict directionally_supported_not_proven: direction consistent
with the financial-tie prediction but NOT proven - strong confounders ranked
strong-first (story-type selection; excerpt-bounded characterization;
desk/genre routing - m682's Clash expose -0.40 is the corpus's hardest OpenAI
register, same week, same parent; deal-seniority gradient unseparated from
genre routing). Counter-evidence carried: the same-peg register CONVERGES with
WIRED (m712, +0.15 on the identical misalignment-framework peg) across two
different tie structures (Conde Nast x OpenAI deal + Meta $0 vs News Corp
dual-payer) - the relay register is peg-driven, weakening the tie-predicts-
register reading of this specific peg; the framework piece's own adversarial
context ('fears over harmful AI reach a fever pitch'); the Meta comparator
post-dates the Mar 2026 Meta licensing leg by four months (the Meta payer does
not buy uniform softening either). MANUAL ILLUSTRATIVE scores only; engine NOT
run on the illustrative arms per the Aug 28 2026 standing rule; engine run
once as a DEGENERATE n=1 check (asymmetry 0.90; t 0.0 / p 1.0 / Cohen d 0.0 /
degenerate CI (0.90, 0.90) / is_significant False; no significance claimed per
the Aug 28 2026 standing rule). NOT a falsification-family member (ledger
holds at 26); no analysis.json update. Novelty verified pre-commit (zero
test_type_a_807 files; no 'Type A #807' in git log; the d1ea1b09 slug zero-hit
repo-wide; block key zero-hit repo-wide; max numeric mechanism_id 714; zero
underscore-form 715 keys by designed keying per #715); count_stats gate
(41365/1134; delta +41/+1 = the #807 file exactly); 805-809 window third leg
E->A (anchor patched post-commit per #565) - Sep 17 2026 10:00 PDT - 41 tests,
7 classes.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_807_wsj_openai_misalignment_framework_relay_vs_meta_glasses_adversarial_sep17_10am.py"
MECH_KEY = "wsj_openai_misalignment_framework_relay_vs_meta_glasses_adversarial_sep17"
M_ID = 715
ITER = 807
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_715"
NEXT_ID_MARKER = "mechanism" + "_716"
NEXT_ID_NUMERIC = "mechanism_id: 716"
EXPECTED_ORDER = [("A", "807"), ("E", "806"), ("D", "805"), ("C", "804"), ("B", "803")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "news-corp.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n\n  meta:")
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
        if "Type A #807" in subject:
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


class TestNovelty807:
    def test_single_test_type_a_807_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_807*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_807 file (this one) must exist"
        )

    def test_type_a_807_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_807 files, no #807 in git log, max numeric
        # mechanism_id 714, zero underscore-form 715 keys); this test pins
        # that no duplicate #807 main commit ever appears.
        mains = _git_log_mains("Type A #807: wsj")
        assert len(mains) == 1, f"exactly one Type A #807 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #807 main commit"
        )


class TestRotationCycleGuard807:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_805_809_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"805-809 window third leg E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_806(self):
        window = _window()
        assert window[1] == ("E", "806"), (
            f"immediate predecessor must be Type E #806, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #807: wsj")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism715Content:
    def test_block_key_exists_in_news_corp_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "mechanism_id: 715" in block
        assert "iteration: 807" in block
        assert "iteration_type: 'A'" in block
        assert "time_pdt: '10:00'" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_two_arm_structure(self):
        block = _block()
        assert "publication: 'Wall Street Journal (News Corp / Dow Jones)'" in block
        assert "entity: OpenAI" in block
        assert "arm1_wsj_openai_misalignment_relay:" in block
        assert "meta_comparator:" in block

    def test_arm1_register_and_illustrative_score(self):
        block = _block()
        assert "register: 'constructive_company_voice_relay'" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block

    def test_wsj_misalignment_url_slug_present(self):
        block = _block()
        assert (
            "openai-shares-more-safety-incidents-and-adopts-new-rules-for-reporting-them-d1ea1b09"
            in block
        )

    def test_chen_quote_and_incidents_characterized(self):
        block = _block()
        assert "Kai Chen" in block
        assert "head of alignment" in block
        assert "share what we are learning as soon as possible" in block
        assert "be transparent only if asked" in block
        assert "disregard the roles and identities that bind other chatbots" in block

    def test_meta_comparator_vocab_and_score(self):
        block = _block()
        assert "Meta Is Flooding the Market With Smartglasses" in block
        assert "flooding the market" in block
        assert "privacy lightning rod" in block
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.75" in block
        assert "carried_from" in block and "mechanism 214" in block

    def test_illustrative_delta_and_scores(self):
        block = _block()
        assert "illustrative_register_delta_openai_minus_meta: 0.90" in block
        assert "openai_arm_scores: [0.15]" in block
        assert "meta_arm_scores: [-0.75]" in block

    def test_dual_deal_seniority_values(self):
        block = _block()
        assert "$250M/5yr" in block
        assert "May 2024" in block
        assert "up to $50M/yr" in block
        assert "Mar 2026" in block
        assert "28 months senior" in block
        assert "6 months senior" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _block()
        assert "Verdict: directionally_supported_not_proven" in block
        assert "directionally consistent with the" in block
        assert "financial-tie prediction" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Story-type selection" in block
        assert "Excerpt-bounded characterization" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_counter_evidence_present(self):
        block = _block()
        assert "counter_evidence:" in block
        assert "m682" in block
        assert "Clash expose" in block
        assert "uniform softening fails" in block

    def test_wired_convergence_weakens_tie_reading(self):
        block = _block()
        assert "relation_to_712" in block
        assert "peg-driven" in block

    def test_statistical_discipline_manual_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE scores only." in block
        assert "calculate_asymmetry([0.15], [-0.75]) returns asymmetry 0.90" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant False" in block
        assert "no significance claimed (Aug 28" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_715_in_block(self):
        assert MECH_ID_MARKER not in _block(), (
            "designed keying: underscore-form marker must appear nowhere in block"
        )

    def test_research_method_and_bounded_absence(self):
        block = _block()
        assert "11 browser.search" in block
        assert "excerpt-bounded per #503" in block
        assert "ABANDONED" in block
        assert "no canonical URLs constructed" in block
        assert "no em dashes" in block

    def test_cross_references_to_family(self):
        block = _block()
        assert "relation_to_214" in block
        assert "relation_to_519" in block
        assert "relation_to_532" in block
        assert "relation_to_682" in block
        assert "relation_to_697" in block


class TestSupersessionAndCorpusPost806:
    def test_max_numeric_id_is_715_not_714(self):
        assert max(_corpus_ids()) == 715, (
            f"max numeric mechanism_id must be 715, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_716_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 716 keys anywhere"

    def test_zero_numeric_716_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 716 mechanism keys in the corpus"
        )

    def test_no_second_715_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d806_zero_underscore_715_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#806 zero-underscore-715 profiles sweep stays green by designed keying"
        )

    def test_d806_zero_underscore_715_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#806 zero-underscore-715 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d806_zero_numeric_715_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id: 715", roots=("profiles",))
        assert len(hits) >= 1, (
            "#806 zero-numeric-715 sweep is superseded by design: the #807 block "
            "is the single numeric 715 key"
        )

    def test_d806_max_714_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 715, (
            "#806 max-714 sweep is superseded by design: the corpus now maxes at 715"
        )

    def test_engine_degenerate_check_recorded_but_not_in_analysis_json(self):
        block = _block()
        assert "calculate_asymmetry([0.15], [-0.75]) returns asymmetry 0.90" in block
        assert "no_analysis_json_update: true" in block


class TestLedger807:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        corpus = _repo_grep("TWENTY-SIXTH", roots=("profiles",))
        assert len(corpus) >= 1, "TWENTY-SIXTH must be present in profiles/"
        assert _repo_grep("TWENTY-SEVENTH", roots=("profiles",)) == [], (
            "TWENTY-SEVENTH must be absent in profiles/"
        )

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26." in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - register documentation" in block


class TestDocSync807:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 41406 |" in readme
        assert "Across 1135 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "41406" in arch and "1135" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog807:
    def test_log_captures_iteration_807(self):
        tail = _iteration_log_tail()
        assert "#807 Type A:" in tail
        assert "10:00 PDT" in tail
        assert "m715" in tail

    def test_log_states_805_809_window(self):
        assert "805-809" in _iteration_log_tail()
