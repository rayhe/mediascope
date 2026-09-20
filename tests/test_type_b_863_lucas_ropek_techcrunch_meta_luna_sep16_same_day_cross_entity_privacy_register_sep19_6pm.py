"""Type B #863 (860-864 window, fifth leg D->E->A->B->C): Lucas Ropek
(TechCrunch) within-journalist SAME-DAY cross-entity privacy-register pair
(mechanism 749).

FIRST Type B mechanism to place a Meta arm on Lucas Ropek in
profiles/careers/journalists.yaml (mechanism 728 covered his Snap temporal
shift; mechanism 269 lives in profiles/competitor-coverage-research.yaml).
The Luna URL appears in corpus zero times pre-commit (grep-verified this
run in profiles/ and tests/), per the #643 convention.

Meta arm: "After accusations of selling 'perv glasses,' Meta prepares to
sell a pair without a camera" (read first-hand this run via verbatim
techcrunch.com URL, 36 rendered lines; In Brief digest; byline confirmed
via author avatar caption "Lucas Ropek"; Sep 16 2026 1:12 PM PDT). Register:
surveillance vocabulary in Ropek's OWN voice attached to a camera-free
product - "deeply disturbed certain consumers who see them as invasive
emblems of a dystopian surveillance society run amok", "as the company
weathers complaints that it's selling 'pervert glasses'", "a pair that
doesn't come with integrated spy equipment"; -0.50 MANUAL ILLUSTRATIVE.

Snap arm (carried from mechanism 728, #828, unrescored): "Snap tries to
make the case again for its $2,200 smart glasses" (Sep 16 2026, morning;
adversarial on price/utility/business, ZERO privacy/alarm vocabulary in
65 lines despite 4 cameras and contextual AI that "builds an understanding
of your goals, priorities, relationships, and routines"; -0.45 carried).

Illustrative Meta-minus-Snap delta -0.05 (near tone-parity): the finding is
VOCABULARY-TYPE asymmetry, not a tone delta. The same journalist, same day,
same publication, same product category: the entity receiving the
surveillance register has ZERO cameras; the entity spared it has FOUR.
CLOSES the #828 scope bound (Ropek had never applied the surveillance
register to Meta in his own voice; now he has) and REFINES mechanism 269
with a same-day camera/no-camera inversion.

Ruled-out alternatives this run: PetaPixel Sep 16 Luna piece (byline not
visible in page render, m230 Growcoot extension not pursued); Tom's Guide
"pervert glasses antidote" Luna piece (byline not established); Mariella
Moon Engadget Luna piece (Sep 16, neutral news-desk register; no
same-journalist competitor comparator established).

Verdict directionally_supported_not_proven. MANUAL / qualitative only;
engine NOT run on the arms per the Aug 28 2026 standing rule; degenerate
n=1 check (calculate_asymmetry([-0.50], [-0.45]) returns asymmetry_score
-0.05; t 0.0 / p 1.0 / Cohen d 0.0; degenerate CI (-0.05, -0.05) /
is_significant False; no significance claimed). NOT a falsification-family
member - a mechanism-269 refinement that closes a mechanism-728 scope
bound; falsification ledger holds at 26; no analysis.json update. Novelty
verified pre-commit (zero test_type_b_863 files; no 'Type B #863' in git
log; max numeric mechanism_id 748; zero underscore-form 749 keys by
designed keying per #715; Luna URL zero-hit in profiles/ and tests/;
block key zero-hit; lucas_ropek YAML key already exists from #828).
860-864 window fifth leg D->E->A->B->C (anchor patched post-commit per
#565) - Sep 19 2026 18:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_863_lucas_ropek_techcrunch_meta_luna_sep16_same_day_cross_entity_privacy_register_sep19_6pm.py"
MECH_KEY = "type_b_863_lucas_ropek_techcrunch_meta_luna_sep16_same_day_cross_entity_privacy_register_sep19"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_749"
NEXT_ID_MARKER = "mechanism" + "_750"
NEXT_ID_NUMERIC = "mechanism_id: 750"
EXPECTED_ORDER = [("B", "863"), ("A", "862"), ("E", "861"), ("D", "860"), ("C", "859")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "5e06d7d49afeeb356c0fab52b0659584a0a7e830"

EXPECTED_URLS = [
    "https://techcrunch.com/2026/09/16/after-accusations-of-selling-perv-glasses-meta-prepares-to-sell-a-pair-without-a-camera/",
    "https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "careers" / "journalists.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\njay_peters:")
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
        if "Type B #863" in subject:
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


def _iteration_log_head() -> str:
    # iteration-log.md is newest-first (entries prepended at the top), so
    # read the head, not the tail.
    return (_repo_root() / "iteration-log.md").read_text()[:30000]


class TestNovelty863:
    def test_single_test_type_b_863_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_863*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_863 file (this one) must exist"
        )

    def test_type_b_863_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_863 files, no #863 in git log, max numeric
        # mechanism_id 748, zero underscore-form 749 keys, Luna URL
        # zero-hit in profiles/ and tests/, block key zero-hit,
        # lucas_ropek YAML key already exists from #828); this test pins
        # that no duplicate #863 main commit ever appears.
        mains = _git_log_mains("Type B #863: lucas ropek")
        assert len(mains) == 1, f"exactly one Type B #863 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #863 main commit"
        )


class TestRotationCycleGuard863:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_860_864_fifth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"860-864 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_862(self):
        window = _window()
        assert window[1] == ("A", "862"), (
            f"immediate predecessor must be Type A #862, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #863: lucas ropek")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism749Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_mechanism_ids_extended(self):
        d = yaml.safe_load(_profiles_text())
        assert "lucas_ropek" in d, "lucas_ropek entry must exist in journalists.yaml"
        assert d["lucas_ropek"]["mechanism_ids"] == [728, 749]
        assert MECH_KEY in d["lucas_ropek"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 863
        assert m["type"] == "B"
        assert m["date"] == "2026-09-19 18:00 PDT"

    def test_meta_arm_first_hand_read(self):
        m = _mech()
        arm = m["meta_arm"]
        assert arm["author_byline"] == "Lucas Ropek"
        assert arm["date"] == "2026-09-16"
        assert arm["time"] == "1:12 PM PDT"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert "36 rendered lines" in arm["evidence_tier"]
        assert "author avatar caption" in arm["evidence_tier"]

    def test_meta_arm_surveillance_vocabulary_quotes(self):
        quotes = str(_mech()["meta_arm"]["key_quotes"])
        for phrase in (
            "dystopian surveillance society run amok",
            "pervert glasses",
            "integrated spy equipment",
            "gargantuan amount of money",
        ):
            assert phrase in quotes, phrase

    def test_meta_arm_url_is_new_to_corpus(self):
        url = _mech()["meta_arm"]["url"]
        assert url == EXPECTED_URLS[0]
        # The URL must exist in exactly the profiles block and this test
        # file - it was zero-hit in corpus pre-commit per #643.
        hits = set(_repo_grep("after-accusations-of-selling-perv-glasses"))
        assert hits == {
            "profiles/careers/journalists.yaml",
            f"tests/{TEST_BASENAME}",
        }, hits

    def test_snap_arm_carried_from_728(self):
        m = _mech()
        arm = m["snap_arm"]
        assert arm["author_byline"] == "Lucas Ropek"
        assert arm["date"] == "2026-09-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert "carried from #828" in arm["tone_basis"]
        assert "ZERO privacy/alarm vocabulary" in arm["register_notes"]
        assert "4 cameras" in arm["register_notes"]

    def test_illustrative_delta_minus_005(self):
        m = _mech()
        assert m["illustrative_delta_meta_minus_snap"] == -0.05
        assert m["delta_calc"] == "(-0.50) - (-0.45) = -0.05"

    def test_degenerate_engine_check_documented(self):
        sd = _mech()["statistical_discipline"]
        assert "calculate_asymmetry([-0.50], [-0.45])" in sd
        assert "asymmetry_score -0.05" in sd
        assert "is_significant False" in sd

    def test_refines_269_and_closes_828_scope_bound(self):
        block = _block()
        assert "REFINES mechanism 269" in block
        assert "CLOSES the #828" in block
        assert "scope bound" in block
        assert "same-day camera/no-camera inversion" in block

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
        assert any("controversy-anchored" in c for c in ce)
        assert any("vocabulary-type, not tone-direction" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "scorer: none" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_749_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 749 is the only allowed
        # 749 reference.
        block = _block()
        assert "mechanism_749" not in block
        assert "mechanism_id: 749" in block

    def test_research_method_ruled_out_alternatives(self):
        rm = _mech()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "1 browser.open first-hand read" in rm
        assert "ruled-out alternatives" in rm

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#269", "#728", "#620", "#733", "#113"):
            assert ref in refs, ref

    def test_distinct_from_prior(self):
        # Distinct from #828 (within-journalist TEMPORAL register shift on
        # Snap) and #269 (the refined mechanism itself): this is a
        # within-journalist SAME-DAY CROSS-ENTITY privacy-register pair
        # placing a Meta arm on Ropek, closing 269/728's scope bound
        # rather than extending a temporal pair.
        block = _block()
        assert "SAME-DAY cross-entity privacy-register" in block
        assert "closes the" in block.lower()


class TestSupersessionAndCorpusPost862:
    def test_max_numeric_id_is_749_not_748(self):
        assert max(_corpus_ids()) == 749, (
            "#862 max-748 sweep is superseded by design: the corpus now maxes at 749"
        )

    def test_zero_underscore_750_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 750 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_750_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 750 mechanism keys in the corpus"
        )

    def test_no_second_749_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d828_zero_underscore_749_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#828 zero-underscore-749 profiles sweep stays green by designed keying"
        )

    def test_d828_zero_underscore_749_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#828 zero-underscore-749 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d862_max_748_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 749, (
            "#862 max-748 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger863:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        # Membership-claim form ("TWENTY-NTH falsification-family member"),
        # not the "absent" meta-assertions other runs added to profiles/.
        members26 = _repo_grep(
            "TWENTY-SIXTH falsification-family member", roots=("profiles",)
        )
        assert len(members26) >= 1, "TWENTY-SIXTH member claim must exist"
        assert _repo_grep(
            "TWENTY-SEVENTH falsification-family member", roots=("profiles",)
        ) == [], "no TWENTY-SEVENTH member claim may exist"

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block


class TestDocSync863:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 44097 |" in readme
        assert "Across 1191 test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "44097" in arch and "1191" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog863:
    def test_log_captures_iteration_863(self):
        head = _iteration_log_head()
        assert "#863 Type B:" in head
        assert "18:00 PDT" in head
        assert "m749" in head

    def test_log_states_860_864_window(self):
        assert "860-864" in _iteration_log_head()
