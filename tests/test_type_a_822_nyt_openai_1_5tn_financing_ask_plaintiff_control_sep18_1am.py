"""Type A #822 (820-824 window, third leg D->E->A): NYT x OpenAI $1.5tn
financing-ask relay - PLAINTIFF-CONTROL on the FT-scooped peg (mechanism
724).

PLAINTIFF-CONTROL extending the mechanism 471 litigation-posture boundary
condition with a peg-matched quantitative anchor. On Wed Sep 16 2026
(04:01:30, via the biztoc mirror timestamp) the New York Times - the
plaintiff actively suing OpenAI and Microsoft for billions since Dec 2023 -
published "OpenAI Considers New Financing at a $1.5 Trillion Valuation,"
relaying OpenAI's OWN ask of $1.5tn, higher than the investor-offered $1.2tn
the FT scooped the day before (m718). The Times carried OpenAI's momentum
case straight: $40B+ annualized revenue in August 2026 (~2x end-2025),
Codex coding-tool traction as the basis for the ask, GPT-6 Astra and
GPT-5.6 Sol shipped since July. Register: straight business-momentum relay,
MANUAL ILLUSTRATIVE +0.15. Illustrative NYT-minus-FT delta -0.10 on the
identical peg: the paid licensee's paper (+0.25, m718) is marginally more
constructive than the litigating plaintiff's (+0.15); both non-adversarial.
The arm sits inside the carried NYT x Meta baseline register range
(mechanism 69 positive open-source strand; -0.65 voluntary-review holdout;
0.0 Arena scoop) - the multi-billion-dollar plaintiff tie does not push
non-lawsuit OpenAI coverage below the Meta floor. Same-week
litigation-domain coverage stays adversarial (Sep 17 unredacted filings: the
NYT-led plaintiffs argue new OpenAI/Microsoft executive quotes "eviscerate"
the fair-use defense), so the boundary is domain-specific, not bleed-through.
Counter-evidence carried: m679 (WSJ -0.40 payer expose), m721 (Gizmodo $0-tie
-0.20 runs harsher than the litigating NYT). Verdict EXTENDS mechanism 471;
directionally_supported_not_proven. MANUAL ILLUSTRATIVE only; engine NOT run
on the illustrative arms per the Aug 28 2026 standing rule; engine run once
as a DEGENERATE n=1 check (calculate_asymmetry([0.15], [0.25]) returns
asymmetry_score -0.10; t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI
(-0.10, -0.10) / is_significant False; no significance claimed). NOT a
falsification-family member - extends boundary condition 471; falsification
ledger holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_a_822 files; no 'Type A #822' in git log; max numeric
mechanism_id 723; zero underscore-form 724 keys by designed keying per #715;
block key zero-hit pre-commit); count_stats gate (delta = this file exactly);
820-824 window third leg D->E->A (anchor patched post-commit per #565) - Sep
18 2026 01:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_822_nyt_openai_1_5tn_financing_ask_plaintiff_control_sep18_1am.py"
MECH_KEY = "nyt_openai_1_5tn_financing_ask_plaintiff_control_sep18"
M_ID = 724
ITER = 822
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_724"
NEXT_ID_MARKER = "mechanism" + "_725"
NEXT_ID_NUMERIC = "mechanism_id: 725"
EXPECTED_ORDER = [("A", "822"), ("E", "821"), ("D", "820"), ("C", "819"), ("B", "818")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "nytimes.yaml").read_text()


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
        if "Type A #822" in subject:
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


class TestNovelty822:
    def test_single_test_type_a_822_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_822*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_822 file (this one) must exist"
        )

    def test_type_a_822_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_822 files, no #822 in git log, max numeric
        # mechanism_id 723, zero underscore-form 724 keys, block key
        # zero-hit); this test pins that no duplicate #822 main commit ever
        # appears.
        mains = _git_log_mains("Type A #822: nyt x openai")
        assert len(mains) == 1, f"exactly one Type A #822 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #822 main commit"
        )


class TestRotationCycleGuard822:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_820_824_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"820-824 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_821(self):
        window = _window()
        assert window[1] == ("E", "821"), (
            f"immediate predecessor must be Type E #821, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #822: nyt x openai")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism724Content:
    def test_block_key_exists_in_nytimes_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "mechanism_id: 724" in block
        assert "iteration: 822" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-18 01:00 PDT" in block
        assert "author: 'Kit (with Ray)'" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication_pair: NYT x OpenAI" in block
        assert "competitor: openai" in block
        assert 'entity_pair: "OpenAI vs Meta"' in block

    def test_plaintiff_control_framing(self):
        block = _block()
        assert "PLAINTIFF-CONTROL" in block
        assert "the plaintiff actively SUING OpenAI and Microsoft for billions" in block
        assert "Dec 2023" in block

    def test_arm1_headline_and_timestamp(self):
        block = _block()
        assert "OpenAI Considers New Financing at a $1.5 Trillion Valuation" in block
        assert "This story appeared on nytimes.com, 2026-09-16 04:01:30" in block
        assert "register: straight_business_momentum_relay" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block

    def test_arm1_ask_vs_bid_asymmetry(self):
        block = _block()
        assert "Investors offered $1.2tn; OpenAI is pushing for $1.5tn" in block
        assert "no decisions made; OpenAI declined to comment" in block
        assert "the comparison the Times itself used" in block

    def test_arm1_momentum_facts_carried(self):
        block = _block()
        assert "More than $40B annualized revenue in August 2026" in block
        assert "Codex coding-tool traction" in block
        assert "GPT-6 Astra and GPT-5.6 Sol shipped since July" in block

    def test_arm1_reuters_attestation(self):
        block = _block()
        assert "the New York Times subsequently reported on September 16" in block
        assert "given advances in its latest AI models" in block
        assert "the Times \"subsequently reported\" confirms the relay position" in block

    def test_arm1_no_adversarial_qualifiers(self):
        block = _block()
        assert "no adversarial qualifiers" in block
        assert "perhaps briefly" in block
        assert "m721" in block

    def test_arm1_four_secondaries_as_source_urls(self):
        block = _block()
        assert "https://biztoc.com/x/b851a0a137639d75" in block
        assert "https://temperature2.com/p/2026-09-16-openai-1-2t-round-after-ipo-delay/" in block
        assert (
            "https://www.reuters.com/commentary/breakingviews/openai-plays-15-trln-chicken-with-chatbot-frenzy-2026-09-16/"
            in block
        )
        assert (
            "https://www.forbes.com/sites/siladityaray/2026/09/16/openai-is-reportedly-weighing-new-funding-round-at-15-trillion-valuation/"
            in block
        )

    def test_arm2_ft_peg_matched_comparator_carried(self):
        block = _block()
        assert "carried un-rescored from m718" in block
        assert "register: constructive_growth_investor_demand" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "mechanism 54" in block

    def test_illustrative_delta_and_scores(self):
        block = _block()
        assert "illustrative_register_delta_nyt_minus_ft: -0.10" in block
        assert "nyt_openai_arm_scores: [0.15]" in block
        assert "ft_openai_arm_scores: [0.25]" in block
        assert "0.15 - 0.25 = -0.10" in block

    def test_meta_baseline_arms_carried(self):
        block = _block()
        assert "Mechanism 69" in block
        assert "Jun 23 2026: Meta AI voluntary-review holdout coverage, adversarial -0.65" in block
        assert "Jun 26 2026: Arena prediction-markets scoop, neutral 0.0" in block
        assert "register_range: 'positive to -0.65'" in block

    def test_meta_baseline_no_entity_inversion(self):
        block = _block()
        assert "sits INSIDE the Meta register range" in block
        assert "no entity-level inversion below the Meta floor" in block

    def test_extends_mechanism_471_boundary(self):
        block = _block()
        assert "Verdict: EXTENDS mechanism 471" in block
        assert "litigation-posture boundary condition" in block
        assert "verdict: directionally_supported_not_proven" not in block
        assert "directionally_supported_not_proven" in block

    def test_financial_context_adversarial_posture(self):
        block = _block()
        assert "predictor: adversarial_legal_posture" in block
        assert "prediction: adversarial_if_blanket" in block
        assert "billions in damages sought" in block
        assert "naive financial determinism fails here by profile prediction" in block

    def test_same_week_lawsuit_domain_counterevidence(self):
        block = _block()
        assert "Sep 17 2026 unredacted filings" in block
        assert "eviscerate" in block
        assert "the boundary is domain-specific, not bleed-through" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Paywall-bounded sourcing" in block
        assert "Relay convergence within the peg" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_counter_evidence_present(self):
        block = _block()
        assert "counterevidence:" in block
        assert "m679" in block
        assert "-0.40" in block
        assert "out-neutrals the neutral non-payer" in block

    def test_statistical_discipline_manual_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE tones only" in block
        assert "calculate_asymmetry([0.15], [0.25]) returns asymmetry_score -0.10" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "degenerate CI (-0.10, -0.10)" in block
        assert "is_significant False" in block
        assert "no significance claimed" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_724_in_block(self):
        assert MECH_ID_MARKER not in _block(), (
            "designed keying: underscore-form marker must appear nowhere in block"
        )

    def test_research_method_and_bounded_absence(self):
        block = _block()
        assert "6 browser.search query sets this run" in block
        assert "2 browser.open reads" in block
        assert "0 browser.open on the NYT original" in block
        assert "bounded absence per #503" in block
        assert "no NYT URLs constructed" in block
        assert "ASCII-only" in block
        assert "no em dashes" in block

    def test_cross_references_to_peg_lineage(self):
        block = _block()
        assert "m718" in block
        assert "m715" in block
        assert "m712" in block
        assert "m721" in block
        assert "m471" in block
        assert "m679" in block

    def test_distinct_from_prior(self):
        block = _block()
        assert "Distinct from #471" in block
        assert "Distinct from #712/#715/#718/#721" in block
        assert "plaintiff-control" in block

    def test_rotation_transparency_820_824(self):
        block = _block()
        assert "820-824 window third leg" in block
        assert "815-819 window verified closed" in block


class TestSupersessionAndCorpusPost821:
    def test_max_numeric_id_is_724_not_723(self):
        assert max(_corpus_ids()) == 724, (
            f"max numeric mechanism_id must be 724, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_725_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 725 keys anywhere"

    def test_zero_numeric_725_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 725 mechanism keys in the corpus"
        )

    def test_no_second_724_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d820_zero_underscore_724_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#820 zero-underscore-724 profiles sweep stays green by designed keying"
        )

    def test_d820_zero_underscore_724_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#820 zero-underscore-724 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d815_max_720_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 724, (
            "#815 max-720 sweep is superseded by design: the corpus now maxes at 724"
        )

    def test_engine_degenerate_check_recorded_but_not_in_analysis_json(self):
        block = _block()
        assert "calculate_asymmetry([0.15], [0.25]) returns asymmetry_score -0.10" in block
        assert "no_analysis_json_update: true" in block


class TestLedger822:
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
        assert "NOT a falsification-family member - extends boundary condition 471" in block


class TestDocSync822:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42094 |" in readme
        assert "Across 1150 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42094" in arch and "1150" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog822:
    def test_log_captures_iteration_822(self):
        tail = _iteration_log_tail()
        assert "#822 Type A:" in tail
        assert "01:00 PDT" in tail
        assert "m724" in tail

    def test_log_states_820_824_window(self):
        assert "820-824" in _iteration_log_tail()
