"""Type B #838 (835-839 window, fifth leg D->E->A->B->C): Dominic Preston
(The Verge) within-journalist temporal register shift on Meta, Sep 3
2026 vs Sep 16 2026 (mechanism 734).

FIRST dedicated Type B mechanism on Dominic Preston in
profiles/careers/journalists.yaml (mechanism 503 lives in
profiles/competitor-coverage-research.yaml; zero dominic_preston YAML
key pre-commit; the Sep-16 Luna URL appears zero times repo-wide
pre-commit, per the #643 convention).

Carried Sep-3 arms (Type B #503): Preston applies privacy-PROBLEMS
vocabulary to Google/Samsung camera hardware (Jul 22 2026 hands-on
dek: "With a camera on every pair, Google's and Samsung's AI glasses
face the same privacy problems as Meta's") while his Meta arm runs as
straight news-desk relay with ZERO privacy vocabulary (Jul 9 2026
Muse Spark 1.1: "Meta says its new AI model is ready to compete on
coding"; mild deficit frame "reentering the AI race"; one controversy
note) - an inversion of the naive financial-incentive prediction;
0.00 MANUAL ILLUSTRATIVE, un-rescored this run per the #807 pattern.
NEW Sep-16 arm: "Meta is reportedly ready to launch less pervy smart
glasses" (The Verge, Sep 16 2026; byline Dominic Preston, News Editor,
confirmed via the WeSearch mirror provenance record this run, 137
rendered lines, retrieval 2026-09-16T08:58:41.764Z, excerpt first
~120 words of publisher body fair-use-limited; canonical URL
provenance-recorded as
https://www.theverge.com/tech/996138/meta-luna-ray-ban-smart-glasses-camera-free-connect,
not navigated; publication 2026-09-16T04:54:46-04:00; dek "New
camera-free frames might avoid the 'pervert glasses' nickname, The
Information reports") - the first Preston-byline Meta piece to carry
privacy-STIGMA vocabulary in the headline/dek; -0.30 MANUAL
ILLUSTRATIVE. Illustrative Sep16-minus-Sep3 delta -0.30.

REFINES mechanism 503 (Preston inverted privacy-vocabulary
application): the Sep-3 inversion - privacy language lands on
Google/Samsung while Meta gets straight relay - was a September-3
phenomenon, not a stable journalist property. By Sep 16 2026 the same
journalist attaches the "pervert glasses" stigma vocabulary to Meta's
own privacy-concession product in the headline/dek. CRITICAL SCOPE
BOUND: the mechanism-503 claim SURVIVES - Preston generates no
independent privacy investigation of Meta in either arm; the stigma
vocabulary arrives via the quoted public nickname and The
Information's report, and the news-desk relay posture is constant
across both arms. The register shift is headline-framing, not
investigative-posture. Verdict directionally_supported_not_proven.
MANUAL / qualitative only; engine NOT run on the arms per the Aug 28
2026 standing rule; no significance claimed. NOT a
falsification-family member - a mechanism-503 refinement with a
temporal scope bound, not a uniform-prediction contradiction;
falsification ledger holds at 26; no analysis.json update. Novelty
verified pre-commit (zero test_type_b_838 files; no 'Type B #838' in
git log; max numeric mechanism_id 733; zero assigned underscore-form
734 keys - only the #837 forward marker; block key zero-hit; zero
dominic_preston YAML key in careers/journalists.yaml; canonical Luna
URL zero-hit repo-wide); count_stats gate (delta = this file
exactly); 835-839 window fifth leg D->E->A->B->C (anchor patched
post-commit per #565) - Sep 18 2026 17:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_838_dominic_preston_verge_meta_sep3_inversion_vs_sep16_luna_stigma_sep18_5pm.py"
MECH_KEY = "type_b_838_dominic_preston_verge_meta_sep3_inversion_vs_sep16_luna_stigma_sep18"
M_ID = 734
ITER = 838
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_734"
NEXT_ID_MARKER = "mechanism" + "_735"
NEXT_ID_NUMERIC = "mechanism_id: 735"
EXPECTED_ORDER = [("B", "838"), ("A", "837"), ("E", "836"), ("D", "835"), ("C", "834")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "e65a3341884a968fb0790b68c21c0a77b7570f4d"

EXPECTED_URLS = [
    "https://www.theverge.com/tech/996138/meta-luna-ray-ban-smart-glasses-camera-free-connect",
    "https://wesearch.press/s/meta-is-reportedly-ready-to-launch-less-pervy-smart-glasses-c8d219e5",
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
    return d["dominic_preston"]["competitor_coverage"][MECH_KEY]


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
        if "Type B #838" in subject:
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


class TestNovelty838:
    def test_single_test_type_b_838_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_838*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_838 file (this one) must exist"
        )

    def test_type_b_838_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_838 files, no #838 in git log, max numeric
        # mechanism_id 733, zero assigned underscore-form 734 keys - only
        # the #837 forward marker, block key zero-hit, zero
        # dominic_preston YAML key in careers/journalists.yaml, canonical
        # Luna URL zero-hit repo-wide); this test pins that no duplicate
        # #838 main commit ever appears.
        mains = _git_log_mains("Type B #838: Dominic Preston")
        assert len(mains) == 1, f"exactly one Type B #838 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #838 main commit"
        )


class TestRotationCycleGuard838:
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

    def test_predecessor_is_type_a_837(self):
        window = _window()
        assert window[1] == ("A", "837"), (
            f"immediate predecessor must be Type A #837, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #838: Dominic Preston")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism734Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_dominic_preston_entry_created_first_dedicated_type_b(self):
        d = yaml.safe_load(_profiles_text())
        assert "dominic_preston" in d, "dominic_preston entry must exist in journalists.yaml"
        assert d["dominic_preston"]["mechanism_ids"] == [734]
        assert MECH_KEY in d["dominic_preston"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 838
        assert m["type"] == "B"
        assert m["date"] == "2026-09-18 17:00 PDT"

    def test_journalist_publication_beat(self):
        d = yaml.safe_load(_profiles_text())
        dp = d["dominic_preston"]
        assert dp["name"] == "Dominic Preston"
        assert dp["current_publication"] == "The Verge"
        assert dp["current_role"] == "News Editor"
        assert "Vox Media" in str(dp["publication_owner"])
        assert "Android Police" in str(dp["career_history"])

    def test_carried_mechanism_503_home(self):
        d = yaml.safe_load(_profiles_text())
        arm = d["dominic_preston"]["smart_glasses_coverage"]["meta_muse_spark_ai_model_jul09"]
        assert arm["carried_mechanism_id"] == 503
        assert arm["carried_mechanism_home"] == "profiles/competitor-coverage-research.yaml"

    def test_sep03_meta_arm_carried_zero_privacy_vocab(self):
        m = _mech()
        arm = m["meta_arm_sep03_carried"]
        assert arm["author_byline"] == "Dominic Preston"
        assert arm["headline"] == "Meta says its new AI model is ready to compete on coding"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.0
        assert arm["privacy_vocabulary_present"] is False
        assert "Type B #503" in arm["carried_from"]
        assert "ZERO privacy vocabulary" in arm["register_notes"]

    def test_sep03_meta_arm_key_quotes(self):
        quotes = str(_mech()["meta_arm_sep03_carried"]["key_quotes"])
        for phrase in (
            "ready to compete on coding",
            "step-change",
            "reentering the AI race",
        ):
            assert phrase in quotes, phrase

    def test_sep03_contrast_arm_privacy_problems_on_google_samsung(self):
        m = _mech()
        arm = m["contrast_google_samsung_arm_sep03_carried"]
        assert "same privacy problems as Meta" in arm["dek_quote"]
        assert arm["date"] == "2026-07-22"
        assert "inversion" in arm["register_notes"]

    def test_sep16_luna_arm_stigma_headline(self):
        m = _mech()
        arm = m["meta_arm_sep16_new"]
        assert arm["author_byline"] == "Dominic Preston"
        assert arm["headline"] == "Meta is reportedly ready to launch less pervy smart glasses"
        assert "pervert glasses" in arm["dek"]
        assert "The Information reports" in arm["dek"]
        assert arm["date"] == "2026-09-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.3
        assert arm["privacy_vocabulary_present"] is True

    def test_sep16_luna_arm_key_quotes(self):
        quotes = str(_mech()["meta_arm_sep16_new"]["key_quotes"])
        for phrase in (
            "less pervy smart glasses",
            "pervert glasses",
            "six microphones",
            "privacy crisis",
            "harass others",
        ):
            assert phrase in quotes, phrase

    def test_sep16_luna_arm_urls_verbatim(self):
        m = _mech()
        urls = m["meta_arm_sep16_new"]["byline_attribution_urls"]
        for url in EXPECTED_URLS:
            assert url in urls, url
        assert "996138" in urls[0]

    def test_sep16_luna_arm_byline_confirmed_news_editor(self):
        m = _mech()
        conf = m["meta_arm_sep16_new"]["byline_confirmation"]
        assert "Dominic Preston" in conf
        assert "News Editor" in conf
        assert "2026-09-16T04:54:46-04:00" in conf
        assert "not navigated" in conf

    def test_illustrative_delta_minus_030(self):
        m = _mech()
        assert m["illustrative_delta_sep16_minus_sep03"] == -0.3
        assert m["delta_calc"] == "(-0.30) - (0.00) = -0.30"

    def test_refines_503_not_inversion_of_voice(self):
        block = _block()
        assert "REFINES mechanism 503" in block
        assert "September-3 phenomenon" in block
        assert "directionally_supported_not_proven" in block

    def test_critical_scope_bound_503_claim_survives(self):
        block = _block()
        assert "CRITICAL SCOPE BOUND" in block
        assert "SURVIVES" in block
        assert "headline-framing, not investigative-posture" in block

    def test_confounders_ranked_strong_first(self):
        conf = _mech()["confounders_ranked"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"], list(conf.keys())
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 2
        assert "DOMINANT confound" in conf["strong"][0]
        assert "story-subject asymmetry" in conf["strong"][0]

    def test_counterevidence_present(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 5
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert any("thinner evidence tier" in c for c in ce)
        assert any("n=1 new arm" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "scorer: none" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_734_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 734 is the only allowed
        # 734 reference. MECH_ID_MARKER is the concatenated form so this
        # file itself never carries the literal marker.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 734" in block

    def test_research_method_ten_search_sets_three_opens(self):
        mech = _mech()
        rm = mech["research_method"]
        assert "10 browser.search query sets" in rm
        assert "3 browser.open reads" in rm
        assert "No canonical URLs constructed" in rm
        assert "#643 convention" in mech["design"]

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#503", "#269", "#828", "#727", "#728", "#833"):
            assert ref in refs, ref

    def test_first_dedicated_type_b_preston(self):
        notes = _profiles_text()
        assert "FIRST dedicated Type B mechanism on Dominic Preston" in notes
        assert "zero dominic_preston YAML key pre-commit" in notes


class TestSupersessionAndCorpusPost837:
    def test_max_numeric_id_is_734_not_733(self):
        assert max(_corpus_ids()) == 734, (
            "#837 max-733 sweep is superseded by design: the corpus now maxes at 734"
        )

    def test_zero_underscore_735_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 735 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_735_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 735 mechanism keys in the corpus"
        )

    def test_no_second_734_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d837_zero_underscore_734_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#837 zero-underscore-734 profiles sweep stays green by designed keying"
        )

    def test_d837_zero_underscore_734_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#837 zero-underscore-734 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d837_max_733_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 733 + 1, (
            "#837 max-733 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger838:
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


class TestDocSync838:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42847 |" in readme
        assert "Across 1166 test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42847" in arch and "1166" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog838:
    def test_log_captures_iteration_838(self):
        tail = _iteration_log_tail()
        assert "#838 Type B:" in tail
        assert "17:00 PDT" in tail
        assert "m734" in tail

    def test_log_states_835_839_window(self):
        assert "835-839" in _iteration_log_tail()
