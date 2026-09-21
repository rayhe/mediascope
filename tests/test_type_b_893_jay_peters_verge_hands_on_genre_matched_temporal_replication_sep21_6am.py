"""Type B #893 (890-894 window, fourth leg D->E->A->B): Jay Peters
(The Verge) genre-matched hands-on temporal replication, Meta Ray-Ban
Display Oct 2025 vs Snap Specs Sep 2026 (mechanism 767).

REFINES mechanism 731 (Type B #833): #833 compared Peters' scored Meta
Gen-2 review (privacy-scrutiny-forward, -0.10 MANUAL ILLUSTRATIVE) against
his Snap Specs hands-on (experiential-positive, +0.35) and found an
illustrative Snap-minus-Meta delta of +0.45, with genre asymmetry (scored
review of a shipping mass-market product vs hands-on first impression of
debut AR hardware) flagged as the DOMINANT confounder. This run tests that
scope bound directly with a GENRE-MATCHED pair: Peters' Oct 2 2025 Meta
Ray-Ban Display hands-on ("The smart glasses race is really on now":
"hugely impressive demo", "could totally pass for something a normal
person would wear"; warm experiential, +0.30 MANUAL ILLUSTRATIVE) vs his
Sep 16 2026 Snap Specs hands-on (+0.35, carried un-rescored from #833 per
#807). Illustrative genre-matched delta: +0.05 (inside noise). The Gen-2
review arm is carried as the review-genre reference (-0.10 per #807): the
within-entity within-journalist genre delta (Meta hands-on +0.30 vs Meta
review -0.10) is +0.40, EIGHT TIMES the genre-matched cross-entity delta.
Reading: for this journalist, story genre predicts register better than
entity does.

Meta arm evidence tier: search-excerpt-bounded per #503. browser.open of
the techcratic.com mirror failed terminally this run and the developer
hard-stopped browser_search after the outage, so no first-hand read was
possible; quotes are excerpt-tier from multiple search-result snippets
this run, NOT first-hand. The techcratic.com mirror URL is novel to the
corpus (zero pre-commit hits). Snap arm and review arm carried un-rescored
from #833 per #807 (NOT re-read this run).

Verdict directionally_supported_not_proven. MANUAL / qualitative only;
engine NOT run on the arms per the Aug 28 2026 standing rule; no
significance claimed. NOT a falsification-family member: a mechanism-731
scope-bound refinement (temporal replication with a genre-matched pair),
not a uniform-prediction contradiction; falsification ledger holds at 29;
no analysis.json update. Novelty verified pre-commit (zero test_type_b_893
files; no 'Type B #893' in git log; max numeric mechanism_id 766 in-tree
including the concurrent #892 m766 which COMMITTED as 3abca63 during this
run; zero underscore-form 767 keys by designed keying per #715; block key
zero-hit; techcratic mirror URL zero-hit); count_stats gate (45786/1220;
delta +52/+1 = the #893 file exactly, venv python); 890-894 window fourth
leg D->E->A->B (anchor patched post-commit per #565); the concurrent Type
C #884 (competitor-entities.yaml m762) remains uncommitted and untouched -
Sep 21 2026 06:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_893_jay_peters_verge_hands_on_genre_matched_temporal_replication_sep21_6am.py"
MECH_KEY = "type_b_893_jay_peters_verge_hands_on_genre_matched_meta_display_oct2025_vs_snap_specs_sep2026_temporal_replication"
M_ID = 767
ITER = 893
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_767"
NEXT_ID_MARKER = "mechanism" + "_768"
NEXT_ID_NUMERIC = "mechanism_id: 768"
EXPECTED_ORDER = [("B", "893"), ("A", "892"), ("E", "891"), ("D", "890"), ("C", "889")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "ee0f04e9ccaf4e617f8f8beed11dbe42b4ff24c8"
EXPECTED_TEST_COUNT = 52
POST_COMMIT_TESTS = 45786
POST_COMMIT_FILES = 1220

EXPECTED_URLS = [
    "https://techcratic.com/index.php/2025/10/02/the-smart-glasses-race-is-really-on-now/the-verge/the-verge/",
    "https://www.theverge.com/tech/996422/snap-specs-hands-on-ar-glasses",
    "https://wesearch.press/s/i-wore-snaps-2200-smart-glasses-22a6aee7",
    "https://jaypeters.net",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "careers" / "journalists.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\ndominic_preston:")
    return text[start:end]


def _mech() -> dict:
    d = yaml.safe_load(_profiles_text())
    return d["jay_peters"]["competitor_coverage"][MECH_KEY]


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
        if "Type B #893" in subject:
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
    return (_repo_root() / "iteration-log.md").read_text()[:12000]


class TestNovelty893:
    @pytest.mark.anchor
    def test_single_test_type_b_893_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_893*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_893 file (this one) must exist"
        )

    @pytest.mark.anchor
    def test_type_b_893_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_893 files, no #893 in git log, max numeric
        # mechanism_id 766 in-tree including concurrent #892's m766, zero
        # underscore-form 767 keys, block key zero-hit, techcratic mirror
        # URL zero-hit); this test pins that no duplicate #893 main commit
        # ever appears.
        mains = _git_log_mains("Type B #893: Jay Peters")
        assert len(mains) == 1, f"exactly one Type B #893 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #893 main commit"
        )

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "ANCHORED_SHA must be patched to the real main-commit SHA"
        assert len(ANCHORED_SHA) == 40


class TestRotationCycleGuard893:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_890_894_fourth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"890-894 window fourth leg D->E->A->B: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    @pytest.mark.rotation
    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    @pytest.mark.rotation
    def test_predecessor_is_type_a_892_committed(self):
        # The #892 run COMMITTED as 3abca63 during this run (no longer
        # in-flight); it is the real third leg of the window.
        window = _window()
        assert window[1] == ("A", "892"), (
            f"immediate predecessor must be Type A #892, got {window[1]}"
        )

    @pytest.mark.rotation
    def test_concurrent_884_still_in_flight_not_in_subjects(self):
        # The concurrent Type C #884 run (competitor-entities.yaml m762)
        # remains uncommitted. Iteration numbers follow the rotation
        # schedule, not commit order, so the subject sequence must read
        # 893 -> 892 -> 891 -> 890 with the in-flight 884 skipped.
        subjects = _git("log", "-25", "--format=%s", "--no-merges").splitlines()
        nums = []
        for line in subjects:
            m = re.match(r"Type [A-E] #(\d+)", line)
            if m and (not nums or nums[-1] != m.group(1)):
                nums.append(m.group(1))
        assert nums[:4] == ["893", "892", "891", "890"], nums[:4]
        assert "884" not in nums

    @pytest.mark.rotation
    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #893: Jay Peters")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism767Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_jay_peters_mechanism_ids_extended(self):
        d = yaml.safe_load(_profiles_text())
        assert d["jay_peters"]["mechanism_ids"] == [731, 767]
        assert MECH_KEY in d["jay_peters"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 893
        assert m["type"] == "B"
        assert m["date"] == "2026-09-21 06:00 PDT"

    def test_mechanism_id_767(self):
        assert _mech()["mechanism_id"] == 767

    def test_journalist_publication_beat(self):
        d = yaml.safe_load(_profiles_text())
        jp = d["jay_peters"]
        assert jp["name"] == "Jay Peters"
        assert jp["current_publication"] == "The Verge"
        assert jp["current_role"] == "Senior Reporter"
        assert "Vox Media" in str(jp["publication_owner"])
        assert "Techmeme" in str(jp["career_history"])

    def test_meta_arm_oct2025_display_hands_on(self):
        m = _mech()
        arm = m["meta_arm"]
        assert arm["author_byline"] == "Jay Peters"
        assert arm["publication"] == "the-verge"
        assert "smart glasses race" in arm["title"]
        assert arm["date"] == "2025-10-02"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert "search-excerpt-bounded" in arm["evidence_tier"]
        assert "failed terminally this run" in arm["evidence_tier"]
        assert "hard-stopped" in arm["evidence_tier"]
        assert arm["privacy_vocabulary_present"] is False

    def test_meta_arm_key_quotes(self):
        quotes = str(_mech()["meta_arm"]["key_quotes"])
        for phrase in (
            "hugely impressive demo",
            "could totally pass for something a normal person would wear",
            "an Apple version of those glasses",
        ):
            assert phrase in quotes, phrase

    def test_meta_arm_mirror_url_novel(self):
        arm = _mech()["meta_arm"]
        assert EXPECTED_URLS[0] in arm["byline_attribution_urls"]
        assert "https://jaypeters.net" in arm["byline_attribution_urls"]
        assert "mirror" in arm["canonical_url_note"]
        assert "zero pre-commit hits" in arm["canonical_url_note"]

    def test_snap_arm_carried_from_833(self):
        m = _mech()
        arm = m["snap_arm"]
        assert "#833" in arm["carried_from"]
        assert "un-rescored per #807" in arm["carried_from"]
        assert arm["author_byline"] == "Jay Peters"
        assert arm["date"] == "2026-09-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.35
        assert "NOT re-read this run" in arm["evidence_tier"]
        assert arm["privacy_vocabulary_count"] == 0
        assert EXPECTED_URLS[1] in arm["byline_attribution_urls"]
        assert EXPECTED_URLS[2] in arm["byline_attribution_urls"]

    def test_snap_arm_carried_quotes(self):
        quotes = str(_mech()["snap_arm"]["key_quotes_carried"])
        for phrase in (
            "playing dominoes",
            "unlike anything I",
            "Snap really believes in AR glasses",
        ):
            assert phrase in quotes, phrase

    def test_review_reference_arm_carried(self):
        arm = _mech()["review_reference_arm"]
        assert "#833" in arm["carried_from"]
        assert "tricky questions" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert "privacy-scrutiny-forward" in arm["register_notes"]

    def test_genre_matched_delta_plus_005(self):
        m = _mech()
        assert m["illustrative_delta_genre_matched_snap_minus_meta"] == 0.05
        assert m["delta_calc"] == "(0.35) - (0.30) = 0.05"

    def test_within_entity_genre_delta_040(self):
        m = _mech()
        assert m["illustrative_delta_genre_within_entity_meta_hands_on_minus_review"] == 0.40
        assert m["genre_delta_calc"] == "(0.30) - (-0.10) = 0.40"

    def test_genre_delta_eight_times_cross_entity(self):
        m = _mech()
        ratio = (
            m["illustrative_delta_genre_within_entity_meta_hands_on_minus_review"]
            / m["illustrative_delta_genre_matched_snap_minus_meta"]
        )
        assert ratio == 8.0, ratio
        assert "EIGHT TIMES" in m["design"]

    def test_refines_731_not_new_accusation(self):
        m = _mech()
        assert "REFINEMENT of mechanism 731" in m["design"]
        assert "not a new entity-bias accusation" in m["design"]
        assert "GENRE-MATCHED" in m["design"]

    def test_confounders_ranked_strong_first(self):
        conf = _mech()["confounders_ranked"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"], list(conf.keys())
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 2
        assert "eleven-month temporal gap" in conf["strong"][0]
        assert "product-maturity asymmetry" in conf["strong"][1]
        assert "DOMINANT confounder" in _block()

    def test_counterevidence_present(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 5
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert any("reattributes the +0.45 delta" in c for c in ce)
        assert any("entity-x-genre interaction" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "MANUAL_ILLUSTRATIVE" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_767_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 767 is the only allowed
        # 767 reference. MECH_ID_MARKER is the concatenated form so this
        # file itself never carries the literal marker.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 767" in block

    def test_research_method(self):
        m = _mech()
        rm = m["research_method"]
        assert "browser.search query sets this run" in rm
        assert "hard-stopped by developer directive" in rm
        assert "failed terminally" in rm
        assert "#503" in rm
        assert "#807" in rm

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#731", "#833", "#269", "#727/#728"):
            assert ref in refs, ref

    def test_distinct_from_833(self):
        # #833 was a cross-genre comparison (scored review vs hands-on);
        # this run is the genre-matched temporal replication that tests
        # #833's own scope bound.
        block = _block()
        assert "Directly tests the #833 scope bound" in block
        assert "GENRE-MATCHED hands-on pair" in block

    def test_smart_glasses_coverage_entry_added(self):
        d = yaml.safe_load(_profiles_text())
        cov = d["jay_peters"]["smart_glasses_coverage"]
        entry = cov["meta_rayban_display_oct2025_hands_on"]
        assert entry["headline"] == "The smart glasses race is really on now"
        assert entry["date"] == "2025-10-02"
        assert entry["tone"] == "experiential_positive"
        assert entry["mechanism_id"] == 767

    def test_expected_urls_present_somewhere(self):
        text = _profiles_text()
        for url in EXPECTED_URLS:
            assert url in text, url


class TestSupersession893:
    def test_max_numeric_id_is_767(self):
        assert max(_corpus_ids()) == 767, (
            "corpus now maxes at 767: supersedes #833 max-731, #891 max-765, "
            "and #892 committed max-766 sweeps by design"
        )

    def test_zero_underscore_768_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 768 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_768_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 768 mechanism keys in the corpus"
        )

    def test_no_second_893_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_833_max_731_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 767, (
            "#833 max-731 sweep is superseded by design"
        )

    def test_891_max_765_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 767, (
            "#891 max-765 sweep is superseded by design"
        )

    def test_892_committed_766_acknowledged(self):
        # The concurrent #892 run committed mechanism 766 (3abca63) during
        # this run; the corpus max is now 767, not 766.
        ids = _corpus_ids()
        assert 766 in ids, "concurrent #892 mechanism 766 must be present"
        assert max(ids) == 767

    def test_concurrent_884_change_not_in_this_commit_scope(self):
        # The concurrent Type C #884 block in competitor-entities.yaml stays
        # uncommitted and is NOT part of this run's scope.
        status = _git("status", "--short")
        assert "profiles/competitor-entities.yaml" in status, (
            "concurrent #884 change must remain uncommitted in the working tree"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger893:
    def test_twenty_ninth_member_form_present_once(self):
        hits = _repo_grep("TWENTY-NINTH falsification-family member", roots=("profiles",))
        assert len(hits) == 1, (
            f"exactly one TWENTY-NINTH member-form in profiles/, got {hits}"
        )

    def test_no_thirtieth_member_form(self):
        hits = _repo_grep("THIRTIETH falsification-family member", roots=("profiles",))
        assert hits == [], (
            f"zero THIRTIETH member-forms in profiles/ (negative-guard strings only), got {hits}"
        )

    def test_block_states_ledger_holds_at_29(self):
        assert "holds at 29" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block


class TestDocSync893:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert f"| Tests | {POST_COMMIT_TESTS} |" in readme
        assert f"Across {POST_COMMIT_FILES} test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert str(POST_COMMIT_TESTS) in arch and str(POST_COMMIT_FILES) in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog893:
    def test_log_captures_iteration_893(self):
        head = _iteration_log_head()
        assert "#893 Type B:" in head
        assert "06:00 PDT" in head
        assert "m767" in head

    def test_log_states_890_894_window(self):
        assert "890-894" in _iteration_log_head()

    def test_log_notes_892_committed_predecessor(self):
        head = _iteration_log_head()
        assert "#892" in head
        assert "3abca63" in head
