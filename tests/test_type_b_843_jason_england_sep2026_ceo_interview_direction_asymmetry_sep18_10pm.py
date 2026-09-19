"""Type B #843 (840-844 window, fourth leg D->E->A->B): Jason England
(Tom's Guide, Future plc) same-writer, same-month, same-genre
(CEO-interview/platform) cross-entity quote-platforming direction
asymmetry, Sep 2026 (mechanism 737).

FIRST dedicated Type B mechanism on Jason England in
profiles/careers/journalists.yaml (mechanism 146 lives in
profiles/competitor-coverage-research.yaml; zero jason_england YAML
key pre-commit; both Sep-2026 arms confirmed on England's Muck Rack
profile this run, Sep 18 2026; canonical Tom's Guide article URLs NOT
constructed per the #643 convention; excerpt evidence tier only).

Meta arm: "Exclusive: Even Realities CEO slams Meta Ray-Bans - we
don't thrive on selling data" (Tom's Guide, Sep 2026; byline Jason
England confirmed via his Muck Rack profile this run; verbatim Muck
Rack excerpt: "While Silicon Valley races to strap cameras,
speakers and multimodal surveillance tools onto our faces, one
smart glasses maker is picking a fight direct with Big Tech's
entire playbook. Meta, Google and Snap want you to believe that a
front-facing camera is essential for the future of AI wearables.
Apple's even rumored to be jumping in on this too."). Headline verb
"slams" directs the surveillance vocabulary AT Meta; -0.40 MANUAL
ILLUSTRATIVE.

Snap arm: "Snap CEO says covert smart glasses are 'creepy' - why
Specs look bold on purpose" (Tom's Guide, Sep 2026; Specs launched
Sep 16 2026; byline Jason England confirmed via his Muck Rack profile
this run; verbatim excerpt: "Most smart glasses makers treat their
technology like something to apologize for (or something to covertly
hide), shrinking cameras and batteries until the frames pass for
standard Wayfarers. Snap is doing the exact opposite... it's clear
that the bold, thick-framed silhouette has split opinions."). The
'creepy' privacy-stigma quote is deflected onto a generic covert
category while Snap's own camera glasses (which record video, per the
Times Sep 2026 Specs launch coverage) get positive design framing
("look bold on purpose"); +0.25 MANUAL ILLUSTRATIVE.

Illustrative Meta-minus-Snap delta -0.65: quote-platforming direction
asymmetry - the journalist headlined one CEO's attack vocabulary
against Meta and another CEO's stigma vocabulary away from Snap's own
cameras.

REFINES mechanism 146 (England competitive aspiration inversion):
extends the Aug-17 Google/Samsung aspiration-vs-Meta-alarm pattern to
Snap in September 2026 and documents the editorial mechanism (which
CEO attack quotes get headline verbs vs design-halo verbs). CRITICAL
SCOPE BOUND: the vocabulary in both arms is sourced (CEO quotes), so
this is NOT evidence that England's authorial voice is adversarial
to Meta in this genre; England's own July voice on Meta WAS
adversarial in his own register (the super-sensing piece: "Meta has
lost the privacy plot", first-hand cloudfront mirror read this run,
70 rendered lines), so the Meta arm is voice-consistent. Verdict
directionally_supported_not_proven. MANUAL / qualitative only;
engine NOT run on the arms per the Aug 28 2026 standing rule; no
significance claimed. NOT a falsification-family member - a
mechanism-146 refinement with a direction-asymmetry scope bound, not
a uniform-prediction contradiction; falsification ledger holds at 26;
no analysis.json update. Novelty verified pre-commit (zero
test_type_b_843 files; no 'Type B #843' in git log; max numeric
mechanism_id 736; zero assigned underscore-form 737 keys; block key
zero-hit; zero jason_england YAML key in careers/journalists.yaml
pre-commit; Even Realities and Snap Sep-2026 headline strings
zero-hit repo-wide); count_stats gate (delta = this file exactly);
840-844 window fourth leg D->E->A->B (anchor patched post-commit per
#565) - Sep 18 2026 22:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_b_843_jason_england_sep2026_ceo_interview_direction_asymmetry_sep18_10pm.py"
MECH_KEY = "type_b_843_jason_england_sep2026_ceo_interview_platform_direction_asymmetry_sep18_10pm"
M_ID = 737
ITER = 843
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_737"
NEXT_ID_MARKER = "mechanism" + "_738"
NEXT_ID_NUMERIC = "mechanism_id: 738"
EXPECTED_ORDER = [("B", "843"), ("A", "842"), ("E", "841"), ("D", "840"), ("C", "839")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "5dfd629f5d6975c28dffc197e48f6c30f2d4806f"

EXPECTED_URLS = [
    "http://muckrack.com/jason-england/articles",
    "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/5",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "careers" / "journalists.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    return text[start:]


def _mech() -> dict:
    d = yaml.safe_load(_profiles_text())
    return d["jason_england"]["competitor_coverage"][MECH_KEY]


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
        if "Type B #843" in subject:
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


class TestNovelty843:
    def test_single_test_type_b_843_file(self):
        files = list((_repo_root() / "tests").glob("test_type_b_843*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_b_843 file (this one) must exist"
        )

    def test_type_b_843_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_843 files, no #843 in git log, max numeric
        # mechanism_id 736, zero assigned underscore-form 737 keys, block
        # key zero-hit, zero jason_england YAML key in
        # careers/journalists.yaml, Sep-2026 arm headline strings zero-hit
        # repo-wide); this test pins that no duplicate #843 main commit
        # ever appears.
        mains = _git_log_mains("Type B #843: Jason England")
        assert len(mains) == 1, f"exactly one Type B #843 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type B #843 main commit"
        )


class TestRotationCycleGuard843:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_840_844_fourth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"840-844 window fourth leg D->E->A->B: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_842(self):
        window = _window()
        assert window[1] == ("A", "842"), (
            f"immediate predecessor must be Type A #842, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type B #843: Jason England")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism737Content:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_jason_england_entry_created_first_dedicated_type_b(self):
        d = yaml.safe_load(_profiles_text())
        assert "jason_england" in d, "jason_england entry must exist in journalists.yaml"
        assert d["jason_england"]["mechanism_ids"] == [737]
        assert MECH_KEY in d["jason_england"]["competitor_coverage"]

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 843
        assert m["type"] == "B"
        assert m["date"] == "2026-09-18 22:00 PDT"

    def test_journalist_publication_beat(self):
        d = yaml.safe_load(_profiles_text())
        je = d["jason_england"]
        assert je["name"] == "Jason England"
        assert je["current_publication"] == "Tom's Guide"
        assert je["current_role"] == "Managing Editor, Computing"
        assert "Future plc" in str(je["publication_owner"])
        assert "smart_glasses" in je["beats"]

    def test_first_dedicated_type_b_england(self):
        notes = _profiles_text()
        assert "FIRST dedicated Type B mechanism on Jason England" in notes
        assert "zero jason_england YAML key pre-commit" in notes

    def test_mechanism_146_home_documented(self):
        notes = str(_profiles_text())
        assert "mechanism 146 lives in profiles/competitor-coverage-research.yaml" in notes

    def test_meta_arm_headline_slams(self):
        m = _mech()
        arm = m["meta_arm"]
        assert arm["author_byline"] == "Jason England"
        assert "slams Meta Ray-Bans" in arm["headline"]
        assert "selling data" in arm["headline"]
        assert arm["headline_verb"] == "slams (Meta Ray-Bans)"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert arm["privacy_vocabulary_present"] is True
        assert arm["privacy_vocabulary_direction"] == "directed_at_meta"

    def test_meta_arm_key_quotes(self):
        quotes = str(_mech()["meta_arm"]["key_quotes"])
        for phrase in (
            "don't thrive on selling data",
            "multimodal surveillance tools onto our faces",
            "essential for the future of AI wearables",
        ):
            assert phrase in quotes, phrase

    def test_meta_arm_byline_confirmed_muckrack(self):
        m = _mech()
        conf = m["meta_arm"]["byline_confirmation"]
        assert "Jason England" in conf
        assert "Muck Rack" in conf
        assert "not constructed per the #643 convention" in conf

    def test_snap_arm_headline_creepy_bold(self):
        m = _mech()
        arm = m["snap_arm"]
        assert arm["author_byline"] == "Jason England"
        assert "'creepy'" in arm["headline"]
        assert "look bold on purpose" in arm["headline"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.25
        assert arm["privacy_vocabulary_present"] is True
        assert arm["privacy_vocabulary_direction"] == "deflected_from_snap_own_cameras"

    def test_snap_arm_key_quotes(self):
        quotes = str(_mech()["snap_arm"]["key_quotes"])
        for phrase in (
            "covertly hide",
            "pass for standard Wayfarers",
            "doing the exact opposite",
            "bold, thick-framed silhouette",
        ):
            assert phrase in quotes, phrase

    def test_snap_arm_record_video_sourced(self):
        m = _mech()
        arm = m["snap_arm"]
        assert arm["snap_specs_record_video"] is True
        assert "record video" in arm["record_video_source"]
        assert "thetimes.com" in arm["record_video_source"]

    def test_snap_arm_byline_confirmed_muckrack(self):
        m = _mech()
        conf = m["snap_arm"]["byline_confirmation"]
        assert "Jason England" in conf
        assert "Specs launched Sep 16 2026" in conf

    def test_both_arms_same_genre(self):
        m = _mech()
        assert m["meta_arm"]["genre"] == m["snap_arm"]["genre"] == "CEO-interview/platform piece"

    def test_both_arms_excerpt_tier(self):
        m = _mech()
        assert "excerpt-tier" in m["meta_arm"]["read"]
        assert "excerpt-tier" in m["snap_arm"]["read"]

    def test_source_urls_verbatim(self):
        d = yaml.safe_load(_profiles_text())
        urls = d["jason_england"]["source_urls"]
        for url in EXPECTED_URLS:
            assert url in urls, url

    def test_illustrative_delta_minus_065(self):
        m = _mech()
        assert m["illustrative_delta_meta_minus_snap"] == -0.65
        assert m["delta_calc"] == "(-0.40) - (0.25) = -0.65"

    def test_refines_146_not_inversion_of_voice(self):
        block = _block()
        assert "REFINES mechanism 146" in block
        assert "quote-platforming" in block
        assert "directionally_supported_not_proven" in block

    def test_critical_scope_bound_sourced_vocabulary(self):
        block = _block()
        assert "CRITICAL SCOPE BOUND" in block
        assert "NOT evidence that England" in block

    def test_confounders_ranked_strong_first(self):
        conf = _mech()["confounders_ranked"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"], list(conf.keys())
        assert len(conf["strong"]) == 3
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 2
        assert "DOMINANT confound" in conf["strong"][0]

    def test_counterevidence_present(self):
        ce = _mech()["counterevidence"]
        assert len(ce) == 5
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)
        assert any("n=1 pair" in c for c in ce)

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "scorer: none" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in _mech()["verdict"]

    def test_designed_keying_no_underscore_737_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 737 is the only allowed
        # 737 reference. MECH_ID_MARKER is the concatenated form so this
        # file itself never carries the literal marker.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 737" in block

    def test_research_method_query_sets_and_opens(self):
        mech = _mech()
        rm = mech["research_method"]
        assert "8 browser.search query sets" in rm
        assert "4 browser.open reads" in rm
        assert "No canonical URLs constructed" in rm
        assert "#643 convention" in mech["research_method"]

    def test_cross_references(self):
        refs = str(_mech()["cross_refs"])
        for ref in ("#146", "#818", "#727", "#828", "#833"):
            assert ref in refs, ref


class TestSupersessionAndCorpusPost842:
    def test_max_numeric_id_is_737_not_736(self):
        assert max(_corpus_ids()) == 737, (
            "#842 max-736 sweep is superseded by design: the corpus now maxes at 737"
        )

    def test_zero_underscore_738_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 738 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_738_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 738 mechanism keys in the corpus"
        )

    def test_no_second_737_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_d842_zero_underscore_737_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#842 zero-underscore-737 profiles sweep stays green by designed keying"
        )

    def test_d842_zero_underscore_737_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#842 zero-underscore-737 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d842_max_736_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 736 + 1, (
            "#842 max-736 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger843:
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


class TestDocSync843:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 43093 |" in readme
        assert "Across 1171 test files" in readme

    def test_readme_type_b_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "43093" in arch and "1171" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog843:
    def test_log_captures_iteration_843(self):
        tail = _iteration_log_tail()
        assert "#843 Type B:" in tail
        assert "22:00 PDT" in tail
        assert "m737" in tail

    def test_log_states_840_844_window(self):
        assert "840-844" in _iteration_log_tail()
