"""Type B #833 (830-834 window, fourth leg D->E->A->B): Jay Peters
(The Verge) within-journalist cross-entity privacy-register comparison,
Meta Ray-Ban Gen 2 review vs Snap Specs hands-on (mechanism 731).

FIRST dedicated Type B mechanism on Jay Peters in
profiles/careers/journalists.yaml (prior corpus mentions are incidental:
a photo credit in profiles/the-verge.yaml, a name-drop in
profiles/competitor-coverage-research.yaml, Techmeme-attribution and
iPhone-Duo quotes in two test files; zero jay_peters YAML key pre-commit,
per the #643 convention).

Meta arm: "Ray-Ban Meta Gen 2 review: all-day smart glasses with the
same tricky questions" (byline confirmed via the Reviews section of
Peters' own site jaypeters.net, read this run, 96 rendered lines; the arm
itself is search-excerpt-bounded per #503 because the browser.open of the
review link failed terminally this run - NOT first-hand; Verge Score 7;
product merits positive: battery "nearly a full day", "They're ultimately
still Meta Ray-Ban glasses ... If you've used the first generation
before, you pretty much get the idea"; privacy-scrutiny-forward register:
the title centers "tricky questions", the mirror dek reads "Better
Battery, Same Privacy Concerns", and the subtle eye-level camera appears
as BOTH a Good and a Bad; -0.10 MANUAL ILLUSTRATIVE). Snap arm: "I wore
Snap's $2,200 smart glasses" (Sep 16 2026 19:40 ET; read this run via the
WeSearch mirror, 133 rendered lines, first ~120 words of publisher body,
fair-use-limited; canonical URL provenance-recorded as
https://www.theverge.com/tech/996422/snap-specs-hands-on-ar-glasses;
experiential positive: "My favorite part of wearing the Specs, Snap's
new augmented reality glasses, was playing dominoes", "It was unlike
anything I've tried in other VR headsets or smart glasses - the ability
to sit with another person and have a shared digital experience", "Snap
really believes in AR glasses", "Snap has spent half a decade working
toward its first consumer pair of AR glasses"; ZERO privacy/alarm
vocabulary; +0.35 MANUAL ILLUSTRATIVE). Illustrative Snap-minus-Meta
delta +0.45.

EXTENDS mechanism 269 (Ropek editorial routing / vocabulary laundering):
the privacy-vocabulary asymmetry now holds for a SECOND journalist - a
Verge senior reporter, published within roughly two hours of Ropek's
Sep-16 TechCrunch piece, adjacent to the #727/#728 Sep-16
natural-experiment window. CRITICAL SCOPE BOUND: Peters' Oct 2025 Meta
Ray-Ban Display piece was positive ("hugely impressive demo", "could
pass as normal eyewear") - the register split is product/story-level, NOT
a stable anti-Meta journalist bias; genre asymmetry (scored review of a
shipping mass-market product vs hands-on first impression of debut AR
hardware) and product maturity ($379 mass-market camera glasses vs $2,195
developer-leaning AR device) are the DOMINANT confounders. Verdict
directionally_supported_not_proven. MANUAL / qualitative only; engine NOT
run on the arms per the Aug 28 2026 standing rule; no significance
claimed. NOT a falsification-family member - a mechanism-269 extension
with a scope bound, not a uniform-prediction contradiction;
falsification ledger holds at 26; no analysis.json update. Novelty
verified pre-commit (zero test_type_b_833 files; no 'Type B #833' in git
log; max numeric mechanism_id 730; zero underscore-form 731 keys by
designed keying per #715; block key zero-hit; zero jay_peters YAML key);
count_stats gate (delta = this file exactly); 830-834 window fourth leg
D->E->A->B (anchor patched post-commit per #565) - Sep 18 2026 12:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_833_jay_peters_verge_meta_gen2_vs_snap_specs_hands_on_sep18_12pm.py"
MECH_KEY = "type_b_833_jay_peters_verge_meta_gen2_tricky_questions_vs_snap_specs_experiential_sep18"
M_ID = 731
ITER = 833
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_731"
NEXT_ID_MARKER = "mechanism" + "_732"
NEXT_ID_NUMERIC = "mechanism_id: 732"
EXPECTED_ORDER = [("B", "833"), ("A", "832"), ("E", "831"), ("D", "830"), ("C", "829")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "8fa33337851e77b4b9abb7bca4c69b5f4e5426de"

EXPECTED_URLS = [
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
    end = text.index("\nmax_miller:")
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
        if "Type B #833" in subject:
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


class TestNovelty833:
    def test_single_test_type_b_833_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_833*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_833 file (this one) must exist"
        )

    def test_type_b_833_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_833 files, no #833 in git log, max numeric
        # mechanism_id 730, zero underscore-form 731 keys, block key
        # zero-hit, zero jay_peters YAML key); this test pins that no
        # duplicate #833 main commit ever appears.
        mains = _git_log_mains("Type B #833: Jay Peters")
        assert len(mains) == 1, f"exactly one Type B #833 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #833 main commit"
        )


class TestRotationCycleGuard833:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_830_834_fourth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"830-834 window fourth leg D->E->A->B: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_832(self):
        window = _window()
        assert window[1] == ("A", "832"), (
            f"immediate predecessor must be Type A #832, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #833: Jay Peters")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism731Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_jay_peters_entry_created_first_dedicated_type_b(self):
        d = yaml.safe_load(_profiles_text())
        assert "jay_peters" in d, "jay_peters entry must exist in journalists.yaml"
        assert d["jay_peters"]["mechanism_ids"] == [731]
        assert MECH_KEY in d["jay_peters"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 833
        assert m["type"] == "B"
        assert m["date"] == "2026-09-18 12:00 PDT"

    def test_journalist_publication_beat(self):
        d = yaml.safe_load(_profiles_text())
        jp = d["jay_peters"]
        assert jp["name"] == "Jay Peters"
        assert jp["current_publication"] == "The Verge"
        assert jp["current_role"] == "Senior Reporter"
        assert "Vox Media" in str(jp["publication_owner"])
        assert "Techmeme" in str(jp["career_history"])

    def test_meta_arm_search_excerpt_bounded(self):
        m = _mech()
        arm = m["meta_arm"]
        assert arm["author_byline"] == "Jay Peters"
        assert arm["publication"] == "the-verge"
        assert "tricky questions" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert "search-excerpt-bounded" in arm["evidence_tier"]
        assert "failed terminally this run" in arm["evidence_tier"]
        assert "https://jaypeters.net" in arm["byline_attribution_urls"]

    def test_meta_arm_privacy_scrutiny_register_quotes(self):
        quotes = str(_mech()["meta_arm"]["key_quotes"])
        for phrase in (
            "tricky questions",
            "Same Privacy Concerns",
            "Verge Score 7",
            "subtle camera positioned at eye level",
            "still Meta Ray-Ban glasses",
            "nearly a full day",
        ):
            assert phrase in quotes, phrase
        arm = _mech()["meta_arm"]
        assert arm["privacy_vocabulary_present"] is True
        assert "tricky questions" in arm["register_notes"]

    def test_snap_arm_first_hand_read(self):
        m = _mech()
        arm = m["snap_arm"]
        assert arm["author_byline"] == "Jay Peters"
        assert arm["date"] == "2026-09-16"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.35
        assert "133 rendered lines" in arm["evidence_tier"]
        assert "fair-use-limited" in arm["evidence_tier"]
        for url in EXPECTED_URLS:
            assert url in arm["byline_attribution_urls"] or url == "https://jaypeters.net", url
        assert "https://www.theverge.com/tech/996422/snap-specs-hands-on-ar-glasses" in arm["byline_attribution_urls"]
        assert "https://wesearch.press/s/i-wore-snaps-2200-smart-glasses-22a6aee7" in arm["byline_attribution_urls"]

    def test_snap_arm_experiential_register_quotes(self):
        quotes = str(_mech()["snap_arm"]["key_quotes"])
        for phrase in (
            "playing dominoes",
            "unlike anything I",
            "shared digital experience",
            "Snap really believes in AR glasses",
            "half a decade",
        ):
            assert phrase in quotes, phrase

    def test_snap_arm_zero_privacy_vocabulary(self):
        m = _mech()
        assert m["snap_arm"]["privacy_vocabulary_count"] == 0
        assert "ZERO privacy/alarm vocabulary" in m["snap_arm"]["register_notes"]

    def test_illustrative_delta_plus_045(self):
        m = _mech()
        assert m["illustrative_delta_snap_minus_meta"] == 0.45
        assert m["delta_calc"] == "(0.35) - (-0.10) = 0.45"

    def test_extends_269_second_journalist(self):
        block = _block()
        assert "EXTENDS mechanism 269" in block
        assert "SECOND journalist" in block
        assert "within roughly two hours of Ropek" in block

    def test_scope_bound_peters_meta_display_counterevidence(self):
        block = _block()
        assert "CRITICAL SCOPE BOUND" in block
        assert "hugely impressive demo" in block
        assert "could pass as normal eyewear" in block
        assert "NOT a stable anti-Meta journalist bias" in block

    def test_confounders_ranked_strong_first(self):
        conf = _mech()["confounders_ranked"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"], list(conf.keys())
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 2
        assert "DOMINANT confound" in conf["strong"][0]
        assert "genre" in conf["strong"][0].lower()

    def test_counterevidence_present(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 5
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert any("Oct 2025 Meta Ray-Ban Display" in c for c in ce)
        assert any("thinner evidence tier" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "scorer: none" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_731_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 731 is the only allowed
        # 731 reference.
        block = _block()
        assert "mechanism_731" not in block
        assert "mechanism_id: 731" in block

    def test_research_method_three_searches_two_opens(self):
        mech = _mech()
        rm = mech["research_method"]
        assert "3 browser.search query sets" in rm
        assert "2 browser.open reads" in rm
        assert "failed terminally this run" in rm
        assert "#643 convention" in mech["design"]

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#269", "#728", "#727", "#113", "#620"):
            assert ref in refs, ref

    def test_distinct_from_prior(self):
        # Distinct from #823 (Berne career-tie register gradient on a NEW
        # journalist) and #728 (Ropek temporal register shift on the SAME
        # entity): this is a within-journalist CROSS-ENTITY privacy-register
        # comparison on a second journalist, extending 269 with a scope
        # bound rather than refining a temporal shift.
        block = _block()
        assert "cross-entity privacy-register comparison" in block
        assert "scope bound" in block
        assert "SECOND journalist" in block

    def test_prior_mentions_incidental_not_mechanisms(self):
        notes = _profiles_text()
        assert "prior corpus mentions are incidental" in notes
        assert "photo credit in profiles/the-verge.yaml" in notes
        assert "zero jay_peters YAML key pre-commit" in notes


class TestSupersessionAndCorpusPost832:
    def test_max_numeric_id_is_731_not_730(self):
        assert max(_corpus_ids()) == 731, (
            "#832 max-730 sweep is superseded by design: the corpus now maxes at 731"
        )

    def test_zero_underscore_732_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 732 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_732_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 732 mechanism keys in the corpus"
        )

    def test_no_second_731_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d832_zero_underscore_731_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#832 zero-underscore-731 profiles sweep stays green by designed keying"
        )

    def test_d832_zero_underscore_731_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#832 zero-underscore-731 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d832_max_730_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 731, (
            "#832 max-730 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger833:
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


class TestDocSync833:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42609 |" in readme
        assert "Across 1161 test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42609" in arch and "1161" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog833:
    def test_log_captures_iteration_833(self):
        tail = _iteration_log_tail()
        assert "#833 Type B:" in tail
        assert "12:00 PDT" in tail
        assert "m731" in tail

    def test_log_states_830_834_window(self):
        assert "830-834" in _iteration_log_tail()
