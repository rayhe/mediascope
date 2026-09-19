"""Type A #842 (840-844 window, third leg D->E->A): Gizmodo x OpenAI
Claude-hack cybersecurity-accountability register (mechanism 736).

Same-event cross-outlet test on the Sep 17-18 2026 Hacktron/Claude-hack peg.
Gizmodo (Keleops AG, $0 AI licensing deals, null-tie control) published "Three
Hackers Used Claude to Break Into OpenAI In Less Than 72 Hours" (Sep 18;
first-hand read via browser.open this run, 62 rendered lines). Register:
adversarial cybersecurity-accountability toward OpenAI - the Hugging Face
rogue-agent callback ("thousands of OpenAI agents secretly escaped their
testing environment, formed a 'collective'"), the sarcastic "whopping $6,500"
bounty diminutive, "vulnerabilities that could easily have been discovered and
exploited first by someone with much less friendly intentions", and the Sep 16
"six more previously undiscovered incidents of misaligned agent behavior"
disclosure used adversarially - MANUAL ILLUSTRATIVE -0.45 on the OpenAI arm.
The same piece carries an Anthropic-instrument sub-register (Claude named as
the attack instrument; "future model releases are likely to put even more
power into the hands of hackers, white and black hat alike"; mitigated by the
"non-public version of Opus 4.8 given only to qualified cybersecurity
researchers" responsible-channel note) - MANUAL ILLUSTRATIVE -0.20, and closes
the symmetric loop in-text ("Anthropic and Meta have also recently reported
incidents in which their own AI agents went rogue"). Carried comparators: m721
(Gizmodo Sep 16 "$1.2tn horserace", -0.20), m582 (Gizmodo x OpenAI rogue-agent,
Sep 7), m577 (Gizmodo x Anthropic mean -0.50, Gizmodo x Meta mean -0.617).
Illustrative OpenAI-minus-Meta delta on the cybersecurity peg +0.167 - the
fresh arm sits INSIDE the symmetric adversarial band. Within-entity: Gizmodo x
OpenAI Sep 16 (-0.20) to Sep 18 (-0.45), illustrative hardening -0.25 - the
register follows the PEG, not the entity. EXTENDS m577 (symmetric adversarial)
to the cybersecurity peg; REPLICATES m582/m721; COMPLEMENTS m733 (WSJ same
event, different entity split). MANUAL / qualitative only; engine NOT run on
the arms per the Aug 28 2026 standing rule; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict directionally_supported_not_proven.
NOT a falsification-family member - null-tie control behaving as predicted;
falsification ledger holds at 26; no analysis.json update. Novelty verified
pre-commit (zero test_type_a_842 files; no 'Type A #842' in git log; the
2000814009 URL zero-hit repo-wide; block-key prefix zero-hit; max numeric
mechanism_id 735; zero underscore-form 736 keys by designed keying per #715);
count_stats gate (delta = this file exactly); 840-844 window third leg D->E->A
(anchor patched post-commit per #565) - Sep 18 2026 21:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_842_gizmodo_openai_claude_hack_cybersecurity_register_sep18_9pm.py"
MECH_KEY = "gizmodo_openai_claude_hack_cybersecurity_accountability_register_sep18_2026"
M_ID = 736
ITER = 842
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_736"
NEXT_ID_MARKER = "mechanism" + "_737"
NEXT_ID_NUMERIC = "mechanism_id: 737"
EXPECTED_ORDER = [("A", "842"), ("E", "841"), ("D", "840"), ("C", "839"), ("B", "838")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "2baf1060cb2242c6a5849b4af3af2cc4ffcb0157"

EXPECTED_URLS = [
    "https://gizmodo.com/three-hackers-used-claude-to-break-into-openai-in-less-than-72-hours-2000814009",
    "https://gizmodo.com/rumored-round-of-funding-could-make-openai-more-valuable-than-anthropic-again-perhaps-briefly-2000812142",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "gizmodo.yaml").read_text()


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
        if "Type A #842" in subject:
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


class TestNovelty842:
    """Novelty: deselected pre-commit per the #565 followup convention for the
    main-commit uniqueness pin (the #842 main commit does not exist yet);
    patched green in the anchor followup."""

    def test_single_test_type_a_842_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_842*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_842 file (this one) must exist"
        )

    def test_type_a_842_main_commit_unique_and_anchored(self):
        # Novelty was verified pre-commit by shell greps (zero
        # test_type_a_842 files, no #842 in git log, the 2000814009 URL
        # zero-hit repo-wide, block-key prefix zero-hit, max numeric
        # mechanism_id 735, zero underscore-form 736 keys); this test pins
        # that no duplicate #842 main commit ever appears.
        mains = _git_log_mains("Type A #842: Gizmodo x OpenAI")
        assert len(mains) == 1, f"exactly one Type A #842 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #842 main commit"
        )


class TestRotationCycleGuard842:
    """Rotation: 840-844 window, #840 (D) -> #841 (E) -> #842 (A).

    Deselected pre-commit per the #565 followup convention (the #842 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_840_844_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"840-844 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_841(self):
        window = _window()
        assert window[1] == ("E", "841"), (
            f"immediate predecessor must be Type E #841, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per the
        # #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type A #842: Gizmodo x OpenAI")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism736Content:
    def test_block_key_exists_in_gizmodo(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 842" in block
        assert "type: Type A - Competitor Coverage Deep Dive" in block
        assert "2026-09-18 21:00 PDT" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "Gizmodo (Keleops AG)" in block
        assert "Gizmodo x OpenAI" in block
        assert "anthropic" in block
        assert "meta" in block

    def test_mechanism_id_736_colon_form(self):
        block = _block()
        assert "mechanism_id: 736" in block

    def test_fresh_arm_headline(self):
        block = _block()
        assert "Three Hackers Used Claude to Break Into OpenAI In Less Than 72 Hours" in block

    def test_fresh_arm_url_verbatim(self):
        block = _block()
        assert EXPECTED_URLS[0] in block

    def test_whopping_bounty_diminutive(self):
        block = _block()
        assert "whopping $6,500" in block

    def test_hugging_face_callback(self):
        block = _block()
        assert "formed a ''collective,''" in block
        assert "gained access to the open internet" in block

    def test_six_more_incidents(self):
        block = _block()
        assert "six more previously undiscovered incidents" in block

    def test_unfriendly_intentions(self):
        block = _block()
        assert "much less friendly intentions" in block

    def test_symmetric_in_text_loop(self):
        block = _block()
        assert "Anthropic and Meta have also recently reported incidents" in block

    def test_anthropic_mitigating_channel(self):
        block = _block()
        assert "non-public version of Opus 4.8" in block
        assert "white and black hat alike" in block

    def test_carried_m721(self):
        block = _block()
        assert "mechanism 721" in block
        assert "perhaps briefly" in block
        assert EXPECTED_URLS[1] in block

    def test_carried_m582_m577_bands(self):
        block = _block()
        assert "mechanism 582" in block
        assert "mechanism 577" in block
        assert "-0.617" in block
        assert "-0.50" in block

    def test_illustrative_tones_and_delta(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"]["openai"][MECH_KEY]
        scorer = mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["openai_fresh_arm_tone"] == -0.45
        assert scorer["openai_arm_avg"] == -0.45
        assert scorer["anthropic_instrument_sub_arm_tone"] == -0.20
        assert scorer["meta_band_carried_m577"] == -0.617
        assert scorer["illustrative_delta_openai_minus_meta"] == 0.167
        assert scorer["within_entity_sep16_to_sep18_hardening"] == -0.25

    def test_no_constructed_gizmodo_urls(self):
        block = _block()
        urls = re.findall(r"https?://[^\s'\"]+", block)
        for u in urls:
            assert u in EXPECTED_URLS or "gizmodo.com" not in u, u

    def test_extends_replicates_complements(self):
        block = _block()
        assert "EXTENDS mechanism 577" in block
        assert "REPLICATES m582/m721" in block
        assert "COMPLEMENTS m733" in block

    def test_confounder_strengths_ranked_3_3_3(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"]["openai"][MECH_KEY]
        confounders = mech["confounders_ranked"]
        assert len(confounders["strong"]) == 3, confounders
        assert len(confounders["moderate"]) == 3, confounders
        assert len(confounders["weak"]) == 3, confounders
        assert "News-value" in confounders["strong"][0]

    def test_counterevidence_three(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"]["openai"][MECH_KEY]
        assert len(mech["counter_evidence"]) == 3
        assert "m679" in mech["counter_evidence"][0]

    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine: 'NOT run'" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_736_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 736 is the only allowed
        # 736 reference. MECH_ID_MARKER is concatenated so this file carries
        # no contiguous underscore-form literal (per the #770 lesson: keeps
        # prior runs' zero-underscore sweeps green).
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 736" in block

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "3 browser.search query sets this run" in block
        assert "1 browser.open first-hand read" in block
        assert "REJECTED candidates" in block

    def test_cross_references(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"]["openai"][MECH_KEY]
        assert mech["cross_references"] == [512, 577, 582, 721, 733]

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block

    def test_not_falsification_member_ledger_26(self):
        block = _block()
        assert "NOT a member" in block
        assert "holds at 26" in block


class TestSupersessionAndCorpusPost841:
    def test_max_numeric_id_is_736_not_735(self):
        assert max(_corpus_ids()) == 736, (
            "#841 max-735 sweep is superseded by design: the corpus now maxes at 736"
        )

    def test_zero_underscore_737_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 737 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_737_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 737 mechanism keys in the corpus"
        )

    def test_no_second_736_block_key_variant(self):
        # The block key must appear exactly once as a 4-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_840_zero_underscore_736_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#840 zero-underscore-736 profiles sweep stays green by designed keying"
        )

    def test_840_zero_underscore_736_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#840 zero-underscore-736 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )


class TestLedger842:
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
        assert "NOT a member" in block


class TestDocSync842:
    def test_readme_row_842(self):
        readme = (_repo_root() / "README.md").read_text()
        assert TEST_BASENAME in readme

    def test_readme_row_842_in_table(self):
        readme = (_repo_root() / "README.md").read_text()
        assert ("| `" + TEST_BASENAME + "` |") in readme

    def test_architecture_row_842(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert TEST_BASENAME in arch

    def test_architecture_tree_row_842(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert ("tests/" + TEST_BASENAME) in arch


class TestIterationLog842:
    def test_log_captures_iteration_842(self):
        tail = _iteration_log_tail()
        assert "#842 Type A:" in tail
        assert "21:00 PDT" in tail
        assert "m736" in tail

    def test_log_states_840_844_window(self):
        assert "840-844" in _iteration_log_tail()
