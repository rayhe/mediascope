"""Type A #812 (810-814 window, third leg D->E->A): FT x OpenAI $1.2tn
funding-round scoop register vs FT x Meta equity-raise desperation register
(mechanism 718).

FIRST dedicated Type A mechanism on the FT Sep 15 2026 OpenAI $1.2 trillion
pre-IPO funding-round scoop vs the FT Jun 5 2026 Meta equity-raise scoop
(matched capital-raise pegs). Arm 1: FT scoop 'OpenAI mulls funding round at
$1.2 trillion valuation ahead of IPO' (Sep 15 2026; FT original paywalled,
Reuters mirror verbatim URL, excerpt-bounded per #503): investor-initiated
talks ("initiated by investors rather than the company"), about $1.2 trillion
(41% markup on the March $852B valuation, $122B committed capital), Altman's
no-2026-IPO safety framing relayed straight, regulatory-optimism tail
("pushing for greater regulation"), momentum context (GPT-5.6 July, Astra
September, $40B annualized revenue via PYMNTS); constructive
growth/investor-demand register, +0.25 MANUAL ILLUSTRATIVE. Four independent
secondaries (WSJ, PYMNTS, Morningstar, LiveMint) all credit the FT scoop.
Arm 2 (in-corpus Meta comparator, mechanism 435 lineage, carried un-rescored):
FT Jun 5 2026 'Meta weighs big equity raising to finance AI infrastructure'
(Reuters mirror, in-corpus) - desperation register: tens of billions in a stock
offering, shares down 6.6% on the report, executives exploring "creative" ways
to raise cash, AI capex "as much as $145 billion this year and even higher in
2027"; -0.30 MANUAL ILLUSTRATIVE. Illustrative OpenAI-minus-Meta delta +0.55.
Financial tie: FT x OpenAI licensing Apr 2024 ($5-10M/yr secondary, mechanism
54, 28 months senior) plus FT x Google News AI pilot (Feb 2026) vs Meta $0.
Verdict directionally_supported_not_proven: direction consistent with the
licensing-incentive prediction but NOT proven - strong confounders ranked
strong-first (mirror-bounded sourcing both arms; peg asymmetry within the
match: private-market investor demand vs public-company dilution; 3.5-month
temporal gap with genuinely diverging fundamentals). Counter-evidence carried:
m676 (FT constructive company-briefed scoop on Anthropic, a NON-payer, +0.20 -
constructive registers need no financial explanation); m643 (FIFTEENTH
falsification member - FT adversarial on non-payers too); FT's August Hugging
Face watchdog follow-ups toward the $5-10M/yr deal partner; the NYT's
subsequent $1.5T figure EXCEEDED the FT's $1.2T (FT was the conservative one);
WSJ matched the scoop same-day with the same register (peg-driven, not
tie-driven). MANUAL ILLUSTRATIVE scores only; engine NOT run on the
illustrative arms per the Aug 28 2026 standing rule; engine run once as a
DEGENERATE n=1 check (asymmetry 0.55; t 0.0 / p 1.0 / Cohen d 0.0 /
degenerate CI (0.55, 0.55) / is_significant False; no significance claimed).
NOT a falsification-family member (ledger holds at 26); no analysis.json
update. Novelty verified pre-commit (zero test_type_a_812 files; no
'Type A #812' in git log; the openai-mulls-funding-round-12-trillion URL
zero-hit repo-wide; block key zero-hit repo-wide; max numeric mechanism_id
717; zero underscore-form 718 keys by designed keying per #715); count_stats
gate (41628/1140; delta +43/+1 = the #812 file exactly); 810-814 window third
leg D->E->A (anchor patched post-commit per #565) - Sep 17 2026 15:00 PDT -
43 tests, 7 classes.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_812_ft_openai_1_2tn_funding_round_scoop_vs_meta_equity_raise_desperation_sep17_3pm.py"
MECH_KEY = "ft_openai_1_2tn_funding_round_scoop_vs_meta_equity_raise_desperation_sep17"
M_ID = 718
ITER = 812
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_718"
NEXT_ID_MARKER = "mechanism" + "_719"
NEXT_ID_NUMERIC = "mechanism_id: 719"
EXPECTED_ORDER = [("A", "812"), ("E", "811"), ("D", "810"), ("C", "809"), ("B", "808")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "financial-times.yaml").read_text()


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
        if "Type A #812" in subject:
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


class TestNovelty812:
    def test_single_test_type_a_812_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_812*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_812 file (this one) must exist"
        )

    def test_type_a_812_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_812 files, no #812 in git log, the
        # openai-mulls-funding-round-12-trillion URL zero-hit repo-wide,
        # block key zero-hit, max numeric mechanism_id 717, zero
        # underscore-form 718 keys); this test pins that no duplicate
        # #812 main commit ever appears.
        mains = _git_log_mains("Type A #812: ft")
        assert len(mains) == 1, f"exactly one Type A #812 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #812 main commit"
        )


class TestRotationCycleGuard812:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_810_814_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"810-814 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_811(self):
        window = _window()
        assert window[1] == ("E", "811"), (
            f"immediate predecessor must be Type E #811, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #812: ft")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism718Content:
    def test_block_key_exists_in_ft_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "mechanism_id: 718" in block
        assert "iteration: 812" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-17 15:00 PDT" in block
        assert "author: Kit (with Ray)" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication_pair: FT x OpenAI" in block
        assert "competitor: openai" in block
        assert 'entity_pair: "OpenAI vs Meta"' in block

    def test_arm1_ft_scoop_url_and_register(self):
        block = _block()
        assert (
            "openai-mulls-funding-round-12-trillion-valuation-ahead-ipo-ft-reports-2026-09-15"
            in block
        )
        assert "register: constructive_growth_investor_demand" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block

    def test_arm1_investor_initiated_framing(self):
        block = _block()
        assert "initiated by investors rather than the company" in block
        assert "about $1.2 trillion" in block
        assert "$122B committed capital" in block
        assert "$852B valuation" in block

    def test_arm1_altman_safety_framing_relayed(self):
        block = _block()
        assert "no-2026-IPO safety framing relayed straight" in block
        assert "ill-advised moment to go public" in block
        assert "pushing for greater regulation" in block

    def test_arm1_momentum_context(self):
        block = _block()
        assert "GPT-5.6" in block
        assert "Astra" in block
        assert "$40B annualized revenue" in block

    def test_arm1_four_secondaries_credit_ft(self):
        block = _block()
        assert "openai-considers-pre-ipo-funding-round-at-more-than-1-2-trillion-valuation-54555295" in block
        assert "pymnts.com/news/artificial-intelligence/2026/openai-eyes-1-2-trillion-valuation-in-pre-ipo-funding-round/" in block
        assert "morningstar.com/stocks/openais-reported-valuation-jump-doesnt-seem-slowed-by-growing-ai-safety-concerns" in block
        assert "livemint.com/companies/news/openai-eyes-1-2-trillion-valuation-in-fresh-funding-round-as-ipo-slips-to-2027-11789533843295.html" in block

    def test_meta_comparator_url_and_register(self):
        block = _block()
        assert "meta-weighs-big-equity-raising-finance-ai-infrastructure-ft-reports-2026-06-05" in block
        assert "register: capital_raise_desperation" in block
        assert "meta_capital_tone_MANUAL_ILLUSTRATIVE: -0.30" in block
        assert "carried un-rescored" in block

    def test_meta_comparator_vocab(self):
        block = _block()
        assert "down 6.6%" in block
        assert '"creative" ways to raise cash' in block
        assert "$145 billion" in block

    def test_illustrative_delta_and_scores(self):
        block = _block()
        assert "illustrative_register_delta_openai_minus_meta: 0.55" in block
        assert "openai_arm_scores: [0.25]" in block
        assert "meta_arm_scores: [-0.30]" in block
        assert "0.25 - (-0.30) = 0.55" in block

    def test_dual_payer_chain_values(self):
        block = _block()
        assert "$5-10M/yr" in block
        assert "Apr 2024" in block
        assert "mechanism 54" in block
        assert "Meta pays FT $0" in block
        assert "Google News AI pilot" in block

    def test_verdict_directionally_supported_not_proven(self):
        block = _block()
        assert "Verdict: directionally_supported_not_proven" in block
        assert "directionally consistent" in block
        assert "licensing-incentive prediction" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        assert "confounders_ranked:" in block
        assert "Mirror-bounded sourcing" in block
        assert "Peg asymmetry within the match" in block
        assert "Temporal gap 3.5 months" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_counter_evidence_present(self):
        block = _block()
        assert "counterevidence:" in block
        assert "Mechanism 676" in block
        assert "NON-payer" in block
        assert "Mechanism 643" in block
        assert "FIFTEENTH" in block
        assert "$1.5T" in block
        assert "conservative one" in block
        assert "the peg, not the FT-OpenAI tie" in block

    def test_statistical_discipline_manual_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE hand-assigned tones" in block
        assert "calculate_asymmetry([0.25], [-0.30]) returns asymmetry 0.55" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant False" in block
        assert "no significance claimed (Aug 28" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying_no_underscore_718_in_block(self):
        assert MECH_ID_MARKER not in _block(), (
            "designed keying: underscore-form marker must appear nowhere in block"
        )

    def test_research_method_and_bounded_absence(self):
        block = _block()
        assert "4 browser.search query sets this run" in block
        assert "mirror-bounded" in block
        assert "no ft.com canonical URLs constructed" in block
        assert "bounded absence per #503" in block
        assert "no em dashes" in block
        assert "ASCII-only" in block

    def test_cross_references_to_family(self):
        block = _block()
        assert "mechanism 54" in block
        assert "mechanism 415" in block
        assert "mechanism 435" in block
        assert "mechanism 625" in block
        assert "mechanism 643" in block
        assert "mechanism 676" in block


class TestSupersessionAndCorpusPost811:
    def test_max_numeric_id_is_718_not_717(self):
        assert max(_corpus_ids()) == 718, (
            f"max numeric mechanism_id must be 718, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_719_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 719 keys anywhere"

    def test_zero_numeric_719_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 719 mechanism keys in the corpus"
        )

    def test_no_second_718_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; the
        # test_file backlink line carries the same string as a substring and
        # is the only other occurrence by design.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d811_zero_underscore_718_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#811 zero-underscore-718 profiles sweep stays green by designed keying"
        )

    def test_d811_zero_underscore_718_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#811 zero-underscore-718 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d810_max_717_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 718, (
            "#810 max-717 sweep is superseded by design: the corpus now maxes at 718"
        )

    def test_d810_zero_numeric_718_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id: 718", roots=("profiles",))
        assert len(hits) >= 1, (
            "#810 zero-numeric-718 sweep is superseded by design: the #812 block "
            "is the single numeric 718 key"
        )

    def test_engine_degenerate_check_recorded_but_not_in_analysis_json(self):
        block = _block()
        assert "calculate_asymmetry([0.25], [-0.30]) returns asymmetry 0.55" in block
        assert "no_analysis_json_update: true" in block


class TestLedger812:
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
        assert "NOT a member - capital-raise register documentation" in block


class TestDocSync812:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 41628 |" in readme
        assert "Across 1140 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "41628" in arch and "1140" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog812:
    def test_log_captures_iteration_812(self):
        tail = _iteration_log_tail()
        assert "#812 Type A:" in tail
        assert "15:00 PDT" in tail
        assert "m718" in tail

    def test_log_states_810_814_window(self):
        assert "810-814" in _iteration_log_tail()
