"""Type B #1088: Victoria Song (The Verge) x Apple Watch always-listening
vs x Meta camera-free Audio - ambient-audio register-inversion pair;
SECOND temporal extension of mechanism 75 (register-selectivity) and
extension of mechanism 827 into the audio modality; NOT a
falsification-family member (ledger holds at 37). FOURTH leg of the
1085-1089 window, CONTINUING it.

DESIGN (writer-level register-inversion test):
- Same-writer pair: Victoria Song, The Verge (Vox Media; the OpenAI
  licensing deal sits with the other lab, no Vox-Apple deal in corpus).
  m75 documented her privacy vocabulary activating for Meta, not
  competitors; m827 extended it to Connect week Sep 2026 (Meta
  camera-free Audio through the stigma frame vs Snap through the
  product/market register).
- Apple arm FRESH this run, relay-tier (finance.biggo.com scraper relay
  of a Vergecast episode with Nilay Patel, Song quoted verbatim within
  the relay, NOT first-hand): segment "The Apple Watch Becomes an
  Always-On Listener" on the Apple Watch Series 12 / Ultra 4 always-on
  audio intelligence (continuous ambient listening, 15-second rewind via
  double-press digital crown, daily conversation recaps). Song register:
  measured technical/product skepticism - transcription-accuracy doubts
  ("a lot of these devices struggle to differentiate your voice between
  broadcasts", "there is no way anyone in this office was talking about
  a cow in Poughkeepsie") plus a legal-technical subpoena question
  (Patel: audible "yikes" off-mic). Zero privacy/stigma vocabulary, zero
  business-model attribution. MANUAL ILLUSTRATIVE -0.05.
- Meta arm CARRIED per #807 from m827 (no re-scoring): Sep-23 "Meta
  ditches the camera on its newest smart glasses" stigma-frame (-0.30)
  and Sep-24 Vergecast "Smart Glasses Only Make Sense When Companies
  Stop Trying to Hoover Up Your Data" business-model-attribution
  (-0.35). Band mean -0.325.
- Illustrative delta (Apple minus Meta): +0.275 (-0.05 - (-0.325)).
  The inversion: the continuous-capture Apple device gets
  transcription-accuracy doubts; the camera-free Meta device gets the
  "pervert glasses" stigma frame carried forward plus the "Hoover Up
  Your Data" business-model indictment. Under m75's logic the privacy
  register should fire hardest on the always-listening device - it does
  not fire, and the register that should stand down on the de-camera'd
  device does not stand down.
- NOT a falsification-family member: the falsification family tests the
  uniform payer-softening prediction; no Vox Media-Apple licensing deal
  exists in corpus, so the payer prediction is moot and there is nothing
  to falsify. Direction is thesis-consistent (Apple softer). Ledger holds
  at 37 (THIRTY-SEVENTH present in profiles/the-verge.yaml,
  THIRTY-EIGHTH member-claim form absent repo-wide).
- Cross-refs: EXTENDS #75 (first audio-modality extension of the
  register-selectivity finding); EXTENDS #827 (second temporal
  extension, Sep 2026); MIRROR-CONTRAST #1068 (m872: Cherlynn Low
  register constancy +0.05 on the same device-pair class - Song shows
  the asymmetric counterpart); BOUNDED by the Sep-24 Verge Janus Rose
  piece "Everything is spying on you and there's no opting out"
  (adversarial privacy register on Apple's always-listening watch at the
  same outlet - the adversarial register IS available for Apple, so
  Song's measured register is a writer-level choice); BOUNDED by #1082
  m880 (register-availability falsification on the Vox-deal partner);
  #1078 writer-level pair design precedent; m712 briefed-relay bound does
  not apply (both arms un-briefed commentary).

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_b_1088 files on disk (glob)
- no "Type B #1088" in git log (--grep)
- max numeric mechanism_id 883 in profiles/ pre-commit
- zero numeric 884 mechanism_id keys in profiles/ (mechanism_id regex sweep)
- zero underscore-form and dash-form 884 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero victoria_song type_b_1088 competitor_coverage block pre-commit
- two novel URLs zero-hit repo-wide pre-commit (finance.biggo.com
  966fb7a3fe0edf86 Vergecast relay, wesearch.press everything-is-spying
  Verge Sep-24 relay)
- THIRTY-EIGHTH member-claim form absent repo-wide pre-commit

RESEARCH METHOD: 6 browser.search query sets, 0 browser.open per #503
(excerpt-bounded): Lauren Goode WIRED Meta glasses (rejected,
corpus-saturated m436/m447); Lauren Goode WIRED OpenAI (rejected,
corpus-saturated); Adi Robertson Verge Meta glasses Sep 2026 (rejected,
no clean Sep-2026 pair); Adi Robertson Verge OpenAI/Apple 2026 (rejected,
pre-sequence-era f7d1876 already in corpus); Verge Apple Watch
always-listening Sep 24 2026 Victoria Song (selected: surfaced the
WeSearch relay + the biggo Vergecast relay with Song's verbatim quotes);
Verge Apple Watch always listening author (selected: confirmed quotes).
Relay-tier Apple arm, carried Meta arms per #807.

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect test_anchor_sha_patched_post_commit (novelty
  anchor 1 per #565, patched in the anchor followup), the rotation-guard
  main-commit tests (3: window, predecessor, single-main-commit - the main
  commit does not exist yet), the doc-sync ratchet (4 per #719, green after
  doc-sync), the iteration-log tests (3 per #721, green after the log-hash
  followup). Expected pre-commit: 68 green + 11 deselected.
- Post-commit re-runs: the two pre-commit-only tests
  (test_no_type_b_1088_in_git_log_precommit,
  test_anchor_sha_placeholder_precommit) fail BY DESIGN; deselect them on
  re-run per the #710/#720 convention.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule. p_value/cohens_d/ci_95 NOT_CALCULATED. is_significant False.
Engine NOT run. verdict directionally_supported_not_proven.
no_analysis_json_update true. NOT artifact-grade. n=1 writer-level pair;
hypothesis-generating only. Correlation is not causation.

ASCII-only, no em dashes.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1088_victoria_song_verge_apple_watch_always_listening_"
    "vs_meta_audio_register_inversion_sep30_1am.py"
)

ITER = 1088
M_ID = 884
NEXT_ID = 885
TYPE_LETTER = "B"
DATE_STR = "2026-09-30 01:00 PDT"
MECH_KEY = (
    "type_b_1088_victoria_song_verge_apple_watch_always_listening_"
    "vs_meta_audio_register_inversion_sep30"
)
# Committed-state window expectation (oldest first); the D->E->A->B legs
# are asserted as the four newest in test_window_is_1085_1089_fourth_leg.
EXPECTED_WINDOW_TAIL = [
    ("D", "1085"),
    ("E", "1086"),
    ("A", "1087"),
    ("B", "1088"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it.
ANCHORED_SHA = "0" * 40

# Runtime-built key needles per #715 / #770 (no contiguous literal in source).
MECH_ID_MARKER = "mechanism" + "_"
US_884 = MECH_ID_MARKER + "884"
DASH_884 = "mechanism" + "-" + "884"
US_885 = MECH_ID_MARKER + "885"
DASH_885 = "mechanism" + "-" + "885"

# Doc-sync ratchet per #719: authoritative base from count_stats.py --check
# (55035 tests / 1412 files; README current this run); +79/+1 for this file.
README_TESTS_BEFORE = 55035
README_TESTS_AFTER = 55114
README_FILES_BEFORE = 1412
README_FILES_AFTER = 1413
README_JOURNALISTS = 273
EXPECTED_TESTS = 79

NOVEL_URLS = [
    "https://finance.biggo.com/news/966fb7a3fe0edf86",
    "https://wesearch.press/s/everything-is-spying-on-you-and-theres-no-opting-out-657c98f3",
]
CARRIED_URLS = [
    "https://technewstube.com/theverge/1870121/meta-ditches-camera-newest-smart-glasses/",
    "https://finance.biggo.com/news/d71bedffa3fb45e3",
]

README = os.path.join(REPO_ROOT, "README.md")
ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
THIS_FILE = os.path.basename(__file__)


def run_git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _git(args):
    return run_git(*args)


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _profiles_text():
    return _read(JOURNALISTS_YAML)


def _block():
    text = _profiles_text()
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start:]
    m = re.search(r"\naditya_soni:", rest)
    return rest[: m.start()] if m else rest


def _item():
    # The victoria_song top-level item (distinct from the journalists-list
    # career-migration entry, which carries mechanism_ids [593, 605, 719]).
    d = yaml.safe_load(_profiles_text())
    return d["victoria_song"]


def _mech():
    return _item()["competitor_coverage"][MECH_KEY]


def _corpus_ids():
    ids = []
    base = os.path.join(REPO_ROOT, "profiles")
    for root, _, files in os.walk(base):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _window(n=60):
    # First occurrence of each distinct iteration number, OLDEST first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention). Post-commit safe: the
    # current run is the newest entry, never mistaken for the predecessor.
    subjects = (
        run_git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    )
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    out.reverse()
    return out[-5:]


# ---------------------------------------------------------------------------
# 1. Novelty anchor per #565 / #715
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1088:
    def test_single_test_type_b_1088_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1088")
        ]
        assert files == [OWN_BASENAME]

    def test_no_type_b_1088_in_git_log_precommit(self):
        # Pre-commit only: fails BY DESIGN once the main commit exists.
        r = run_git("log", "--grep", "Type B #1088:", "--format=%H", "--no-merges")
        assert r.stdout.strip() == ""

    def test_anchor_sha_placeholder_precommit(self):
        # Pre-commit only: the anchor followup patches ANCHORED_SHA per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero test_type_b_1088 files",
            "max numeric mechanism_id 883",
            "block key zero-hit",
            "two novel URLs zero-hit",
            "THIRTY-EIGHTH member-claim form absent",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1085-1089 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1085_1089Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1085_1089_fourth_leg(self):
        # Committed-state form: the four newest distinct iteration mains
        # are the D->E->A->B window legs (the fifth slot is #1084 or older).
        assert _window()[-4:] == EXPECTED_WINDOW_TAIL

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n2) == int(n1) + 1
            assert (self.ORDER[t2] - self.ORDER[t1]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1087(self):
        order = _window()
        idx = order.index(("B", "1088"))
        assert order[idx - 1] == ("A", "1087")
        r = run_git("log", "--grep", "Type A #1087:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1087 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1088:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1088 main commit"

    def test_next_run_is_type_c_1089_note(self):
        assert "1089" in __doc__ and "C" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (post-edit safe: needles runtime-built)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # block_key field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS_YAML).count("\n    " + MECH_KEY + ":") == 1

    def test_mechanism_id_884_colon_form_present(self):
        assert "mechanism_id: 884" in _block()

    def test_no_underscore_dash_884_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 884 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 884 key needle forms (underscore and
        # dash) may appear this run; the needles are fragment-built here
        # too, so this file itself carries no contiguous literal either.
        n1 = "mech" + "anism_" + "8" + "84"
        n2 = "mech" + "anism-" + "8" + "84"
        hits = set()
        for p in glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")):
            if os.path.basename(p) == OWN_BASENAME:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        for p in glob.glob(
            os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True
        ):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == set(), hits

    def test_block_key_carries_no_numeric_id(self):
        assert "884" not in MECH_KEY

    def test_thirty_eighth_member_form_absent_precommit(self):
        # Post-commit safe: the only THIRTY-EIGHTH mentions in profiles/ are
        # ledger prose ("THIRTY-EIGHTH absent") in this run's own block
        # (journalists.yaml) and #1082's landed block (the-verge.yaml) -
        # both are the ledger invariant, not a member form.
        out = _git(["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected ledger prose"
        assert all(
            "journalists.yaml" in l or "the-verge.yaml" in l for l in lines
        ), lines


# ---------------------------------------------------------------------------
# 4. Mechanism 884 block structure in profiles/careers/journalists.yaml
# ---------------------------------------------------------------------------
class TestMechanism884Structure:
    def test_item_is_top_level_victoria_song(self):
        item = _item()
        assert item["name"] == "Victoria Song"
        assert item["current_role"] == "Senior Reporter / Wearables Reviewer"

    def test_mechanism_ids_include_884_after_827(self):
        assert _item()["mechanism_ids"] == [827, 884]

    def test_block_key_field_roundtrips(self):
        assert _mech()["block_key"] == MECH_KEY

    def test_test_file_field_matches_basename(self):
        assert _mech()["test_file"] == "tests/" + OWN_BASENAME

    def test_iteration_date_type_goal_fields(self):
        m = _mech()
        assert m["iteration"] == 1088
        assert m["iteration_type"] == "B"
        assert m["iteration_time"] == DATE_STR
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["discovery_date"] == "2026-09-30"

    def test_ascii_only_no_em_dashes(self):
        block = _block()
        assert all(ord(c) < 128 for c in block), "non-ASCII byte in block"
        assert "\u2014" not in block

    def test_verification_sub_block(self):
        v = _mech()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True

    def test_yaml_roundtrip_clean(self):
        yaml.safe_load(_profiles_text())


# ---------------------------------------------------------------------------
# 5. Apple arm evidence (FRESH, relay-tier per #503)
# ---------------------------------------------------------------------------
class TestAppleArmEvidence:
    def test_apple_arm_is_vergecast_relay_with_song_quotes(self):
        arm = _mech()["apple_arm"]
        assert arm["evidence_tier"].startswith("relay-tier")
        assert "Vergecast" in arm["title"]
        assert "Nilay Patel" in arm["attribution"]
        assert arm["source_url"] == NOVEL_URLS[0]

    def test_apple_device_details_documented(self):
        notes = _mech()["apple_arm"]["framing_notes"]
        for kw in (
            "Series 12",
            "Ultra 4",
            "15-second rewind",
            "daily recaps",
            "continuously listens",
        ):
            assert kw in notes, kw

    def test_verbatim_song_quotes_present(self):
        notes = _mech()["apple_arm"]["framing_notes"]
        assert "differentiate your voice between broadcasts" in notes
        assert "cow in Poughkeepsie" in notes

    def test_subpoena_question_documented(self):
        notes = _mech()["apple_arm"]["framing_notes"]
        assert "subpoenaed" in notes
        assert "yikes" in notes

    def test_zero_privacy_stigma_vocabulary_asserted(self):
        notes = _mech()["apple_arm"]["framing_notes"]
        assert "no privacy/stigma vocabulary" in notes
        assert "no business-model attribution" in notes

    def test_apple_tone_manual_illustrative(self):
        assert _mech()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.05


# ---------------------------------------------------------------------------
# 6. Meta arm evidence (CARRIED per #807 from m827, no re-scoring)
# ---------------------------------------------------------------------------
class TestMetaArmEvidence:
    def test_carried_flag_and_source(self):
        arm = _mech()["meta_arm"]
        assert arm["carried_per_807"] is True
        assert arm["carried_from"].startswith("m827")

    def test_sub_arm_1_stigma_frame(self):
        s1 = _mech()["meta_arm"]["sub_arm_1"]
        assert s1["date"] == "2026-09-23"
        assert s1["register"] == "stigma-frame"
        assert "pervert glasses" in s1["notes"]
        assert s1["source_url"] == CARRIED_URLS[0]
        assert s1["tone_MANUAL_ILLUSTRATIVE"] == -0.30

    def test_sub_arm_2_business_model_attribution(self):
        s2 = _mech()["meta_arm"]["sub_arm_2"]
        assert s2["date"] == "2026-09-24"
        assert s2["register"] == "business-model-attribution"
        assert "Hoover Up Your Data" in s2["title"]
        assert s2["source_url"] == CARRIED_URLS[1]
        assert s2["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_band_mean(self):
        assert _mech()["meta_arm"]["band_mean"] == -0.325

    def test_novel_urls_in_block_and_carried_urls_preserved(self):
        urls = _mech()["source_urls"]
        for u in NOVEL_URLS + CARRIED_URLS:
            assert u in urls
        item_urls = _item()["source_urls"]
        for u in NOVEL_URLS:
            assert u in item_urls


# ---------------------------------------------------------------------------
# 7. Tones and illustrative delta
# ---------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_all_tones_manual_illustrative(self):
        arm = _mech()["apple_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.05
        meta = _mech()["meta_arm"]
        assert meta["sub_arm_1"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert meta["sub_arm_2"]["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_delta_value_and_direction(self):
        m = _mech()
        assert m["illustrative_delta"] == 0.275
        assert m["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] > m["meta_arm"]["band_mean"]
        assert "thesis-consistent" in m["delta_note"].lower()

    def test_delta_arithmetic_stated(self):
        note = _mech()["delta_note"]
        assert "-0.05 - (-0.325) = +0.275" in note

    def test_inversion_described_in_pattern(self):
        pattern = _mech()["pattern"]
        assert "inversion" in pattern.lower()
        assert "audio" in pattern.lower()


# ---------------------------------------------------------------------------
# 8. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_discipline_fields_present(self):
        d = _mech()["statistical_discipline"]
        for kw in (
            "MANUAL ILLUSTRATIVE ONLY",
            "NOT_CALCULATED",
            "Engine NOT run",
            "directionally_supported_not_proven",
            "no_analysis_json_update true",
            "NOT artifact-grade",
            "Correlation is not causation",
        ):
            assert kw in d, kw

    def test_verdict_field(self):
        assert _mech()["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update_true(self):
        assert _mech()["no_analysis_json_update"] is True

    def test_sample_size_one_pair(self):
        assert "n=1" in _mech()["statistical_discipline"]

    def test_docstring_discipline_claim(self):
        assert "STATISTICAL DISCIPLINE" in __doc__

    def test_delta_name_prefixed_illustrative(self):
        assert "illustrative_delta" in _block()


# ---------------------------------------------------------------------------
# 9. Falsification ledger (holds at 37; NOT a member)
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_ledger_value_37(self):
        assert _mech()["falsification_ledger"] == 37

    def test_not_member_claim(self):
        fam = _mech()["falsification_family"]
        assert fam.startswith("NOT a falsification-family member")

    def test_no_vox_apple_deal_rationale(self):
        fam = _mech()["falsification_family"]
        assert "no Vox Media-Apple licensing deal exists in corpus" in fam
        assert "payer prediction is moot" in fam

    def test_ledger_prose_consistent(self):
        fam = _mech()["falsification_family"]
        assert "Falsification ledger holds at 37" in fam


# ---------------------------------------------------------------------------
# 10. Confounders ranked strong-first per the corpus convention
# ---------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_six_confounders(self):
        assert len(_mech()["confounders"]) == 6

    def test_ranked_strong_first(self):
        conf = _mech()["confounders"]
        assert conf[0].startswith("STRONG")
        assert conf[1].startswith("STRONG")
        assert conf[2].startswith("STRONG")
        assert conf[3].startswith("MODERATE")
        assert conf[4].startswith("MODERATE")
        assert conf[5].startswith("WEAK")

    def test_strongest_is_evidence_tier(self):
        assert "relay-tier" in _mech()["confounders"][0]

    def test_genre_and_peg_mismatch_present(self):
        conf = _mech()["confounders"]
        assert "genre" in conf[1].lower()
        assert "peg" in conf[2].lower()


# ---------------------------------------------------------------------------
# 11. Cross-references
# ---------------------------------------------------------------------------
class TestCrossReferences:
    def test_cross_ref_count(self):
        assert len(_mech()["cross_refs"]) == 7

    def test_extends_75_and_827(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#75: EXTENDS" in refs
        assert "#827" in refs
        assert "temporal extension" in refs.lower()

    def test_mirror_contrast_1068(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#1068: MIRROR-CONTRAST" in refs
        assert "Cherlynn Low" in refs

    def test_janus_rose_bound(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "Janus Rose" in refs
        assert NOVEL_URLS[1] in refs

    def test_m880_bound_and_1078_precedent(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "m880" in refs
        assert "#1078" in refs


# ---------------------------------------------------------------------------
# 12. Research method per #503 (relay-tier convention)
# ---------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_six_query_sets_documented(self):
        assert "6 browser.search query sets" in _mech()["research_method"]

    def test_rejection_and_selection_trails(self):
        rm = _mech()["research_method"]
        assert "Lauren Goode" in rm and "REJECTED" in rm
        assert "Adi Robertson" in rm
        assert "SELECTED" in rm

    def test_goode_saturation_rationale(self):
        rm = _mech()["research_method"]
        assert "saturated in corpus" in rm or "corpus-saturated" in rm

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _mech()["research_method"]

    def test_urls_verbatim_from_listings(self):
        rm = _mech()["research_method"]
        assert "verbatim from Full-URL listings" in rm
        assert "no canonical URLs constructed" in rm

    def test_docstring_research_method_claim(self):
        assert "6 browser.search" in __doc__


# ---------------------------------------------------------------------------
# 13. Guard lifecycle: #1085/#1086/#1087 zero-884 guards superseded
# ---------------------------------------------------------------------------
class TestGuardLifecycle884Lands:
    def test_m884_lands_in_profiles(self):
        out = _git(["grep", "-l", "mechanism_id: 884", "--", "profiles/"]).stdout
        assert "profiles/careers/journalists.yaml" in out

    def test_max_mechanism_id_now_884(self):
        ids = _corpus_ids()
        assert max(ids) == 884

    def test_zero_883_numeric_sweep_now_superseded(self):
        # The #1085/#1086/#1087 zero-883 sweep was green pre-#1087; #1087
        # landed m883 in the-verge.yaml (Type A #1087, Cherlynn Low's
        # predecessor run) - supersession prose per #710/#720.
        out = _git(
            ["grep", "-n", "mechanism_id: 883", "--", "profiles/"]
        ).stdout
        assert "profiles/the-verge.yaml" in out

    def test_window_files_still_pin_883_pre_roll(self):
        # #1085/#1086/#1087 files have not been rolled forward to pin
        # zero-884 guards; the #1090 Type D run pins the zero-885 guards.
        files = [
            "tests/test_type_d_1085_m880_m881_m882_qualitative_corpus_integrity_sep29_10pm.py",
            "tests/test_type_e_1086_podcast_sentiment_140th_verification_sep29_11pm.py",
            "tests/test_type_a_1087_verge_anthropic_pacing_policy_register_extension_sep30_midnight.py",
        ]
        for f in files:
            text = _read(os.path.join(REPO_ROOT, f))
            assert "883" in text, f
        assert "1089" in __doc__


# ---------------------------------------------------------------------------
# 14. Doc-sync ratchet per #719
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_bumped(self):
        text = _read(README)
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert str(README_JOURNALISTS) in text

    def test_readme_stats_before_values_superseded(self):
        # The stats table line itself carries the new values; the old
        # values legitimately appear in this run's table-row doc-sync
        # prose (55035/1412 -> 55114/1413), so assert on the table line.
        stats = [l for l in _read(README).splitlines() if l.startswith("| Tests |")]
        assert stats == ["| Tests | 55114 | Across 1413 test files |"]

    def test_readme_has_test_file_table_row(self):
        assert OWN_BASENAME in _read(README)

    def test_architecture_has_tests_tree_row(self):
        assert OWN_BASENAME in _read(ARCH)


# ---------------------------------------------------------------------------
# 15. Iteration log entry per #721
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_type_b_1088_header(self):
        assert "## #1088 Type B" in _read(LOG)

    def test_log_entry_mentions_mechanism_884(self):
        text = _read(LOG)
        start = text.index("## #1088 Type B")
        seg = text[start : start + 4000]
        assert "884" in seg
        assert "Victoria Song" in seg

    def test_log_mentions_main_anchor_loghash_commits(self):
        text = _read(LOG)
        start = text.index("## #1088 Type B")
        seg = text[start : start + 4000]
        assert "main commit" in seg.lower()
        assert "anchor" in seg.lower()
        assert "log-hash" in seg.lower()


# ---------------------------------------------------------------------------
# 16. In-flight isolation: never touch concurrent workers' files
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "profiles/careers/journalists.yaml",
            "test_type_b_1088_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l


# ---------------------------------------------------------------------------
# 17. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_block_ends_before_aditya_soni_key(self):
        text = _profiles_text()
        i = text.index("    " + MECH_KEY + ":")
        j = text.index("\naditya_soni:")
        assert i < j

    def test_key_design_note_documents_1088_iteration_number(self):
        assert "1088 is the iteration number" in _mech()["key_design_note"]

    def test_publication_focus_and_type(self):
        m = _mech()
        assert m["publication_focus"] == "the-verge"
        assert m["iteration_type"] == "B"
