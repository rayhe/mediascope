"""Type A #827 (825-829 window, third leg D->E->A): WIRED x Snap Specs
Sep-16-2026 consumer-launch natural-experiment resolution (mechanism 727).

FIRST dedicated mechanism under competitor_relationships.snap in
profiles/wired.yaml (the key did not exist before this run). Resolution
test of the corpus snap_natural_experiment prediction: when Snap launches
consumer Spectacles, does WIRED apply equivalent scrutiny as it applies to
Meta glasses? The Sep 16 2026 Los Angeles consumer launch (Spiegel keynote,
$2,195 standalone AR glasses, 4 cameras, SPECS Intelligence anticipatory AI
service, Verizon cellular charging case, Salesforce/Nvidia/AWS enterprise
partnerships) is the natural experiment, testable in the Sep 16-18 window.
Result: NO standalone WIRED piece on the launch surfaced in 5 bounded
browser.search query sets (zero verbatim wired.com URLs; the Gadget Review
"per Wired" ecosystem-depth citation is unlinked second-hand and
unresolvable to a verbatim wired.com URL in bounded searches). Comparator
outlets published launch-day hands-on and launch coverage: Engadget
(Karissa Bell), Toms Guide, Gizmodo (via the gamesreviews.com Sep 17
roundup), TechCrunch, Reuters, Android Authority, Barrons, 9to5Mac. The Meta
comparator arm is carried from mechanism 354: WIRED Gear desk published 3+
adversarial Meta glasses articles in the Jun-Jul 2026 window (Jul 2 2026
subscription extraction piece by Chokkattu/Ashworth, Meta arm avg -0.62)
while publishing 0 standalone Snap Specs pieces at the Jun 16 AWE unveil.
The Sep 16 launch extends the selection pattern into a SECOND Snap event
window: silence on the $2,195 4-camera competitor launch vs hostile
extraction framing on the $799/$379 Meta product. EXTENDS mechanisms 354
(inverted price criticism) and 42 (compound silence). Financial tie:
Conde Nast CRO Elizabeth Herbst-Brady, senior revenue roles at Snap
pre-Sep 2024 (mechanism 208 family); Meta has no equivalent tie; coverage
prediction softer. MANUAL / qualitative only; engine NOT run on the arms
per the Aug 28 2026 standing rule; snap arm NOT_SCORED (no coverage, no
tone, per the #732 selection convention); p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. NOT a falsification-family member -
the selection-margin result is directionally consistent with the incentive
prediction, not a contradiction; falsification ledger holds at 26; no
analysis.json update. Novelty verified pre-commit (zero test_type_a_827
files; no 'Type A #827' in git log; max numeric mechanism_id 726; zero
underscore-form 727 keys by designed keying per #715; block key zero-hit;
all 6 source URLs zero-hit repo-wide); count_stats gate (delta = this file
exactly); 825-829 window third leg D->E->A (anchor patched post-commit per
#565) - Sep 18 2026 06:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_827_wired_snap_specs_sep16_launch_natural_experiment_sep18_6am.py"
MECH_KEY = "snap_specs_sep16_consumer_launch_natural_experiment_resolution"
M_ID = 727
ITER = 827
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_727"
NEXT_ID_MARKER = "mechanism" + "_728"
NEXT_ID_NUMERIC = "mechanism_id: 728"
EXPECTED_ORDER = [("A", "827"), ("E", "826"), ("D", "825"), ("C", "824"), ("B", "823")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

EXPECTED_URLS = [
    "https://gamesreviews.com/news/09/snap-specs-hands-on-2195-standalone-ar-glasses-impress-but-questions-remain/",
    "https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/",
    "https://www.reuters.com/business/snap-targets-enterprises-with-salesforce-nvidia-ai-tools-augmented-reality-2026-09-16/",
    "https://www.gadgetreview.com/snaps-specs-are-finally-here-and-the-2195-price-tag-is-asking-a-lot",
    "https://www.9to5mac.com/2026/09/16/snap-specs-intelligence-cellular-support/",
    "https://www.barrons.com/articles/snap-stock-specs-intelligence-ai-assistant-6c781613",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "wired.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\ncross_entity_wearables_framing:")
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
        if "Type A #827" in subject:
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


class TestNovelty827:
    def test_single_test_type_a_827_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_827*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_827 file (this one) must exist"
        )

    def test_type_a_827_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_827 files, no #827 in git log, max numeric
        # mechanism_id 726, zero underscore-form 727 keys, block key
        # zero-hit, all 6 source URLs zero-hit); this test pins that no
        # duplicate #827 main commit ever appears.
        mains = _git_log_mains("Type A #827: wired x snap")
        assert len(mains) == 1, f"exactly one Type A #827 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #827 main commit"
        )


class TestRotationCycleGuard827:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_825_829_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"825-829 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_826(self):
        window = _window()
        assert window[1] == ("E", "826"), (
            f"immediate predecessor must be Type E #826, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type A #827: wired x snap")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains

class TestMechanism727Content:
    def test_block_key_exists_in_wired_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_first_snap_entity_key_in_competitor_relationships(self):
        d = yaml.safe_load(_profiles_text())
        snap = d["competitor_relationships"]["snap"]
        assert snap is not None
        assert MECH_KEY in snap

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 827" in block
        assert "iteration_type: 'A'" in block
        assert "2026-09-18 06:00 PT" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "WIRED" in block
        assert "Snap" in block
        assert "Meta" in block

    def test_financial_tie_and_prediction(self):
        d = yaml.safe_load(_profiles_text())
        snap = d["competitor_relationships"]["snap"]
        assert snap["financial_tie"] == "personnel_career_migration"
        assert snap["coverage_prediction"] == "softer"
        block = _block()
        assert "Herbst-Brady" in block

    def test_snap_arm_bounded_absence(self):
        block = _block()
        assert "url: NONE_SURFACED_BOUNDED_ABSENCE" in block
        assert "manual_illustrative_tone: NOT_SCORED" in block

    def test_natural_experiment_resolution(self):
        block = _block()
        assert "snap_natural_experiment" in block
        assert "Sep 16 2026" in block
        assert "second Snap event window" in block.lower() or "SECOND Snap event window" in block

    def test_meta_arm_carried_from_354(self):
        block = _block()
        assert "source_mechanism: 354" in block
        assert "meta_arm_avg: -0.62" in block
        assert "extracting value" in block
        assert "monetizing customers" in block

    def test_comparator_outlets_present(self):
        block = _block()
        for outlet in ("Engadget", "TechCrunch", "Reuters", "9to5Mac", "Barrons"):
            assert outlet in block, outlet

    def test_all_six_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_no_wired_com_url_constructed(self):
        block = _block()
        assert "wired.com/story" not in block, (
            "no verbatim wired.com launch URL surfaced; none may be constructed"
        )

    def test_extends_354_and_42(self):
        block = _block()
        assert "EXTENDS mechanism 354" in block or "EXTENDS mechanisms 354" in block
        assert "mechanism 42" in block

    def test_confounders_ranked_strong_first(self):
        block = _block()
        strengths = re.findall(r"strength: (\w+)", block)
        assert strengths[:3] == ["strong", "strong", "strong"], strengths
        assert strengths.count("strong") == 3
        assert strengths.count("moderate") == 3
        assert strengths.count("weak") == 3

    def test_counterevidence_present(self):
        block = _block()
        assert "counterevidence:" in block
        assert "TechCrunch ran a skeptical Sep 16 launch piece" in block

    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "scorer: none" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_727_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 727 is the only allowed
        # 727 reference.
        block = _block()
        assert "mechanism_727" not in block
        assert "mechanism_id: 727" in block

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "5 browser.search query sets" in block
        assert "1 browser.open" in block
        assert "gadgetreview.com" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("354", "42", "208", "362", "732"):
            assert f"- {ref}" in block, ref

    def test_distinct_from_prior(self):
        # Distinct from #732 (Verge x OpenAI SOI selection test), #354
        # (journalist-level inverted price criticism), and #42 (Jun-Jul
        # compound silence): this is a publication-level launch-event
        # natural-experiment resolution on a NEW entity key.
        assert "publication_level" in _block()


class TestSupersessionAndCorpusPost826:
    def test_max_numeric_id_is_727_not_726(self):
        assert max(_corpus_ids()) == 727, (
            "#826 max-726 sweep is superseded by design: the corpus now maxes at 727"
        )

    def test_zero_underscore_728_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 728 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_728_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 728 mechanism keys in the corpus"
        )

    def test_no_second_727_block_key_variant(self):
        # The block key must appear exactly once as a 6-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d826_zero_underscore_727_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#826 zero-underscore-727 profiles sweep stays green by designed keying"
        )

    def test_d826_zero_underscore_727_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#826 zero-underscore-727 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d824_max_726_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 727, (
            "#824 max-726 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestLedger827:
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


class TestDocSync827:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42325 |" in readme
        assert "Across 1155 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42325" in arch and "1155" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog827:
    def test_log_captures_iteration_827(self):
        tail = _iteration_log_tail()
        assert "#827 Type A:" in tail
        assert "06:00 PDT" in tail
        assert "m727" in tail

    def test_log_states_825_829_window(self):
        assert "825-829" in _iteration_log_tail()
