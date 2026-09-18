"""Type B #828 (825-829 window, fourth leg D->E->A->B): Lucas Ropek
(TechCrunch) within-journalist temporal register shift on Snap Specs
(mechanism 728).

FIRST dedicated Type B mechanism on Lucas Ropek in
profiles/careers/journalists.yaml (mechanism 269 lives in
profiles/competitor-coverage-research.yaml; zero lucas_ropek YAML key
pre-commit; the Sep 16 URL appears in corpus only as m727 counter-evidence
context in profiles/wired.yaml, never as a Ropek-byline mechanism, per the
#643 convention).

Jun 16 2026 arm: "Snap finally debuts its long-awaited AR glasses, Specs,
and, oof, they aren't cheap" (read first-hand this run via verbatim corpus
URL, 64 rendered lines; product-news neutral with soft business skepticism;
ONE neutral privacy sentence; +0.10 MANUAL ILLUSTRATIVE). Sep 16 2026 arm:
"Snap tries to make the case again for its $2,200 smart glasses" (read
first-hand this run via verbatim search Full-URL, 65 rendered lines;
adversarial: "not only underwhelming but also a genuine disaster",
"whopping $2,200", "vaguely reminiscent of scuba gear", "jeers online",
"cringe-inducing cost", "head-scratching"; -0.45 MANUAL ILLUSTRATIVE).
Illustrative Sep-minus-Jun delta -0.55.

REFINES mechanism 269 (Ropek editorial routing / vocabulary laundering):
the "product-enthusiastic" Ropek-on-Snap characterization was a
debut-window phenomenon, not a stable journalist property. By Sep 16 2026
the same journalist converges to the adversarial price/utility/business
register his colleagues applied to Meta. CRITICAL SCOPE BOUND: the 269
PRIVACY-vocabulary claim SURVIVES - the Sep 16 piece applies ZERO
privacy/alarm vocabulary to Snap's 4 cameras plus contextual AI, while
Perez/Ha applied "luxury surveillance tech" and "pervert glasses" to
Meta; the privacy register asymmetry persists even inside an adversarial
piece. Verdict directionally_supported_not_proven. MANUAL / qualitative
only; engine NOT run on the arms per the Aug 28 2026 standing rule;
degenerate n=1 check (calculate_asymmetry([-0.45], [0.10]) returns
asymmetry_score -0.55; t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI
(-0.55, -0.55) / is_significant False; no significance claimed). NOT a
falsification-family member - a mechanism-269 refinement with a scope
bound, not a uniform-prediction contradiction; falsification ledger holds
at 26; no analysis.json update. Novelty verified pre-commit (zero
test_type_b_828 files; no 'Type B #828' in git log; max numeric
mechanism_id 727; zero underscore-form 728 keys by designed keying per
#715; block key zero-hit; zero lucas_ropek YAML key); count_stats gate
(delta = this file exactly); 825-829 window fourth leg D->E->A->B (anchor
patched post-commit per #565) - Sep 18 2026 07:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_828_lucas_ropek_techcrunch_snap_jun16_sep16_register_shift_sep18_7am.py"
MECH_KEY = "type_b_828_lucas_ropek_techcrunch_snap_jun16_vs_sep16_register_shift_sep18"
M_ID = 728
ITER = 828
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_728"
NEXT_ID_MARKER = "mechanism" + "_729"
NEXT_ID_NUMERIC = "mechanism_id: 729"
EXPECTED_ORDER = [("B", "828"), ("A", "827"), ("E", "826"), ("D", "825"), ("C", "824")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "bcefa5e4ac21dd68a4cbef2ae305eb16af8794dc"

EXPECTED_URLS = [
    "https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/",
    "https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "careers" / "journalists.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nmax_miller:")
    return text[start:end]


def _mech() -> dict:
    d = yaml.safe_load(_profiles_text())
    return d["lucas_ropek"]["competitor_coverage"][MECH_KEY]


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
        if "Type B #828" in subject:
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


class TestNovelty828:
    def test_single_test_type_b_828_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_828*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_828 file (this one) must exist"
        )

    def test_type_b_828_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_828 files, no #828 in git log, max numeric
        # mechanism_id 727, zero underscore-form 728 keys, block key
        # zero-hit, zero lucas_ropek YAML key); this test pins that no
        # duplicate #828 main commit ever appears.
        mains = _git_log_mains("Type B #828: lucas ropek")
        assert len(mains) == 1, f"exactly one Type B #828 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #828 main commit"
        )


class TestRotationCycleGuard828:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_825_829_fourth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"825-829 window fourth leg D->E->A->B: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_827(self):
        window = _window()
        assert window[1] == ("A", "827"), (
            f"immediate predecessor must be Type A #827, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #828: lucas ropek")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism728Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_lucas_ropek_entry_created_first_dedicated_type_b(self):
        d = yaml.safe_load(_profiles_text())
        assert "lucas_ropek" in d, "lucas_ropek entry must exist in journalists.yaml"
        assert d["lucas_ropek"]["mechanism_ids"] == [728]
        assert MECH_KEY in d["lucas_ropek"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 828
        assert m["type"] == "B"
        assert m["date"] == "2026-09-18 07:00 PDT"

    def test_journalist_publication_beat(self):
        d = yaml.safe_load(_profiles_text())
        lr = d["lucas_ropek"]
        assert lr["name"] == "Lucas Ropek"
        assert lr["current_publication"] == "TechCrunch"
        assert lr["current_role"] == "Senior Writer"
        assert "Gizmodo" in str(lr["career_history"])

    def test_jun16_arm_first_hand_read(self):
        m = _mech()
        arm = m["jun16_arm"]
        assert arm["author_byline"] == "Lucas Ropek"
        assert arm["date"] == "2026-06-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert "64 rendered lines" in arm["evidence_tier"]

    def test_jun16_privacy_one_neutral_sentence(self):
        m = _mech()
        arm = m["jun16_arm"]
        assert "follows Meta" in str(arm["key_quotes"])
        assert "built-in LED light" in str(arm["key_quotes"])
        assert arm["register_notes"].startswith("product-news neutral")

    def test_sep16_arm_first_hand_read(self):
        m = _mech()
        arm = m["sep16_arm"]
        assert arm["author_byline"] == "Lucas Ropek"
        assert arm["date"] == "2026-09-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert "65 rendered lines" in arm["evidence_tier"]

    def test_sep16_adversarial_register_quotes(self):
        quotes = str(_mech()["sep16_arm"]["key_quotes"])
        for phrase in (
            "genuine disaster",
            "whopping $2,200",
            "scuba gear",
            "jeers online",
            "cringe-inducing cost",
            "head-scratching",
            "heavy goggles",
        ):
            assert phrase in quotes, phrase

    def test_sep16_zero_privacy_vocabulary(self):
        m = _mech()
        assert m["sep16_arm"]["privacy_vocabulary_count"] == 0
        assert "ZERO privacy/alarm vocabulary" in m["sep16_arm"]["register_notes"]

    def test_illustrative_delta_minus_055(self):
        m = _mech()
        assert m["illustrative_delta_sep_minus_jun"] == -0.55
        assert m["delta_calc"] == "(-0.45) - (0.10) = -0.55"

    def test_degenerate_engine_check_documented(self):
        sd = _mech()["statistical_discipline"]
        assert "calculate_asymmetry([-0.45], [0.10])" in sd
        assert "asymmetry_score -0.55" in sd
        assert "is_significant False" in sd

    def test_refines_269_privacy_claim_survives(self):
        block = _block()
        assert "REFINES mechanism 269" in block
        assert "debut-window phenomenon" in block
        assert "privacy-vocabulary asymmetry claim SURVIVES" in block
        assert "luxury surveillance tech" in block
        assert "pervert glasses" in block

    def test_confounders_ranked_strong_first(self):
        conf = _mech()["confounders_ranked"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"], list(conf.keys())
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 1
        assert "DOMINANT confound" in conf["strong"][0]

    def test_counterevidence_present(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 5
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert any("Jun 17 TC piece" in c for c in ce)
        assert any("degree, not kind" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "scorer: none" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_728_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 728 is the only allowed
        # 728 reference.
        block = _block()
        assert "mechanism_728" not in block
        assert "mechanism_id: 728" in block

    def test_research_method_two_searches_two_opens(self):
        rm = _mech()["research_method"]
        assert "2 browser.search query sets" in rm
        assert "2 browser.open reads" in rm
        assert "#643 convention" in rm

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#269", "#620", "#113", "#727", "#354"):
            assert ref in refs, ref

    def test_distinct_from_prior(self):
        # Distinct from #823 (Berne career-tie register gradient on a NEW
        # journalist) and #269 (the refined mechanism itself): this is a
        # within-journalist TEMPORAL register shift on the SAME entity
        # (Snap), bounding 269's scope rather than extending a cross-entity
        # pair.
        block = _block()
        assert "within-journalist temporal register" in block
        assert "scope bound" in block


class TestSupersessionAndCorpusPost827:
    def test_max_numeric_id_is_728_not_727(self):
        assert max(_corpus_ids()) == 728, (
            "#827 max-727 sweep is superseded by design: the corpus now maxes at 728"
        )

    def test_zero_underscore_729_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 729 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_729_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 729 mechanism keys in the corpus"
        )

    def test_no_second_728_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d827_zero_underscore_728_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#827 zero-underscore-728 profiles sweep stays green by designed keying"
        )

    def test_d827_zero_underscore_728_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#827 zero-underscore-728 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d825_max_726_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 728, (
            "#825 max-726 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger828:
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
        assert "NOT a falsification-family member" in block


class TestDocSync828:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42367 |" in readme
        assert "Across 1156 test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42367" in arch and "1156" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog828:
    def test_log_captures_iteration_828(self):
        tail = _iteration_log_tail()
        assert "#828 Type B:" in tail
        assert "07:00 PDT" in tail
        assert "m728" in tail

    def test_log_states_825_829_window(self):
        assert "825-829" in _iteration_log_tail()
