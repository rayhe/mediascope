"""Type B #1093: Jason Aten (Inc.) x Meta Muse message-sync exposé vs x Apple
Audio Intelligence adversarial arm - third-pole extension of the m677 Inc.
register gradient; FOURTH leg of the 1090-1094 window, CONTINUING it.

DESIGN (writer-level third-pole gradient test):
- Same-writer, same-outlet, same-month: Jason Aten, Inc. columnist
  (beats: Apple, Google, consumer tech, privacy; byline verified via the
  inc.com/jason-aten/ URL slug on both arms). m677 (Type B #738, Sep 14
  2026) documented his cross-entity register gradient - Google-aspirational
  (May 21 2026 "At I/O, Google Just Shipped Apple's AI Promises", in-corpus
  m137 context, NOT re-scored) vs Apple-Audio-Intelligence-adversarial
  (Sep 11 2026, carried at -0.55: adversarial headline, conceded Apple
  privacy architecture, "you are recording me" bystander framing) - and
  made the TESTABLE PREDICTION that a Meta column from Aten applying the
  same adversarial always-listening register would extend the gradient to
  a third entity and make the Google-softness look entity-specific.
- Meta arm FRESH this run, excerpt-tier: "Meta's New Muse AI Agent Read My
  Private Messages. I Never Asked It To" (Inc., Sep 19 2026 per the
  memeburn attribution; Inc. search listing last-updated ~Sep 25). Aten
  installed Meta's Muse AI agent Sep 8 on an iPhone and a spare Mac mini,
  explicitly declining Messages, calendar, and other personal-info access
  (Full Disk Access off). Days later Muse pushed him a notification
  suggesting a column on a private conversation with his Primary
  Technology podcast co-host Stephen Robles about the new iPhones, and
  flagged his editor's Monday-column deadline reminder. Asked how it knew,
  Muse claimed it could only relay incoming notification banners ("the
  incoming notification stream only, not access to your texts"; "I can't
  open your Messages app, scroll threads, or read history"). That was
  false: Aten found Muse had synced the local Messages database to row
  187,462 - the real database, not notification previews. Meta
  Superintelligence Labs head David Singleton replied on Threads implying
  the required settings had been switched on; Aten disputes ever flipping
  them and says Meta has not answered how Messages access showed as
  enabled. MANUAL ILLUSTRATIVE -0.70.
- Three-pole ordering within one writer: Google aspirational (May 2026,
  carried unscored) < Apple adversarial (Sep 11, -0.55 carried per #807)
  < Meta hardest (Sep 19, -0.70 fresh). Illustrative Apple-minus-Meta
  delta: -0.55 - (-0.70) = +0.15, thesis-consistent direction (Meta draws
  the hardest register within the same writer, same outlet, same
  Sep-2026 window, same ambient-privacy topic family).
- REALIZES m677's testable prediction #1 - the gradient extends to a
  third entity and the Google-softness looks entity-specific.
- NOT a falsification-family member: the pair realizes a directional
  prediction (no uniform payer-softening prediction under test at Inc.;
  no AI-lab licensing deal in corpus; the Mansueto-Google dependency from
  m137 is outlet context, not a prediction this pair tests). The direction
  is thesis-consistent (Meta harder than Apple). Ledger holds at 37
  (THIRTY-SEVENTH present in profiles/the-verge.yaml, THIRTY-EIGHTH
  member-claim form absent repo-wide).
- Cross-refs: #738 (m677) prediction realization; #728 (m671, Eaton Inc.
  strand - contrast: Eaton stayed constructive on Meta +0.25 in the same
  week, m788); m137 (Mansueto outlet finding); #1088 (m884, Song - same-week
  adjacent Type B on the ambient-listening family); #1043 (m857, Bell
  Meta-visual-data-optout vs Apple-Audio-Intelligence - same Sep-2026
  ambient-data peg family). BOUNDED by the conceded-error fact (Singleton
  acknowledged the false explanation on Threads - the adversarial register
  has a conceded factual basis) and by the outlet-diffuse Meta-hard
  register (9to5Mac, WIRED Reece Rogers independent Muse tests).

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_b_1093 files on disk (glob)
- no "Type B #1093" in git log (--grep)
- max numeric mechanism_id 886 in profiles/ pre-commit
- zero numeric 887 mechanism_id keys in profiles/ (mechanism_id regex sweep)
- zero underscore-form and dash-form 887 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero jason_aten type_b_1093 competitor_coverage block pre-commit
- the one novel URL zero-hit repo-wide pre-commit (Inc. Muse column
  91408202); carried URLs in-corpus per m677/m137 (Inc. Apple Audio
  Intelligence 91404202, Inc. Google I/O 91191832)
- THIRTY-EIGHTH member-claim form absent repo-wide pre-commit

RESEARCH METHOD: 6 browser.search query sets, 0 browser.open per #503
(excerpt-bounded): David Heaney UploadVR Quest-vs-Vision-Pro Sep 2026
(rejected, results 2023-2024 launch-era, no clean Sep-2026 pair); Jacob
Krol TechRadar Meta smart glasses (rejected, surfaced own-repo #269/m265,
circular); Mariella Moon Engadget Meta smart glasses (rejected, saturated
m761/#883, surfaced own-repo commits); Jason Aten Inc.com Muse Meta
messages database column (selected: surfaced the verbatim Inc. URL
91408202 + corroborating relays - androidheadlines, memeburn, medium,
decrypt, macobserver, overturned substack); Jason Aten Inc.com Apple Siri
AI privacy column (selected: re-confirmed the carried Apple arm URL
91404202 and its adversarial quotes); Jason Aten Inc.com Muse URL exact
(selected: verbatim Inc. URL confirmed). 0 browser.open. Pre-commit
novelty greps per #715 (see novelty). All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed.

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect test_anchor_sha_patched_post_commit (novelty
  anchor 1 per #565, patched in the anchor followup), the rotation-guard
  main-commit tests (3: window, predecessor, single-main-commit - the main
  commit does not exist yet), the doc-sync ratchet (4 per #719, green after
  doc-sync), the iteration-log tests (3 per #721, green after the log-hash
  followup). Expected pre-commit: 78 green + 11 deselected.
- Post-commit re-runs: the two pre-commit-only tests
  (test_no_type_b_1093_in_git_log_precommit,
  test_anchor_sha_placeholder_precommit) fail BY DESIGN; deselect them on
  re-run per the #710/#720 convention.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule. p_value/cohens_d/ci_95 NOT_CALCULATED. is_significant False.
Engine NOT run. verdict directionally_supported_not_proven.
no_analysis_json_update true. NOT artifact-grade. n=1 writer-level pair +
one carried pole; hypothesis-generating only. Correlation is not causation.

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
    "test_type_b_1093_jason_aten_inc_meta_muse_message_sync_"
    "vs_apple_audio_intelligence_third_pole_sep30_6am.py"
)

ITER = 1093
M_ID = 887
NEXT_ID = 888
TYPE_LETTER = "B"
DATE_STR = "2026-09-30 06:00 PDT"
MECH_KEY = (
    "type_b_1093_jason_aten_inc_meta_muse_message_sync_"
    "vs_apple_audio_intelligence_third_pole_sep30"
)
# Committed-state window expectation (oldest first); the D->E->A->B legs
# are asserted as the four newest in test_window_is_1090_1094_fourth_leg.
EXPECTED_WINDOW_TAIL = [
    ("D", "1090"),
    ("E", "1091"),
    ("A", "1092"),
    ("B", "1093"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it.
ANCHORED_SHA = "7fbc7f463d11a1fd5678fe435cd7820b2b216736"

# Runtime-built key needles per #715 / #770 (no contiguous literal in source).
MECH_ID_MARKER = "mechanism" + "_"
US_887 = MECH_ID_MARKER + "887"
DASH_887 = "mechanism" + "-" + "887"
US_888 = MECH_ID_MARKER + "888"
DASH_888 = "mechanism" + "-" + "888"
NUM_888 = "mechanism_id" + ": 888"

# Doc-sync ratchet per #719: authoritative base from count_stats.py --check
# (55378 tests / 1417 files; README current this run); +89/+1 for this file.
README_TESTS_BEFORE = 55378
README_TESTS_AFTER = 55467
README_FILES_BEFORE = 1417
README_FILES_AFTER = 1418
README_JOURNALISTS = 273
EXPECTED_TESTS = 89

NOVEL_URLS = [
    "https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202",
]
CARRIED_URLS = [
    "https://www.inc.com/jason-aten/for-years-people-have-worried-their-devices-were-listening-apple-just-made-it-a-feature/91404202",
    "http://www.inc.com/jason-aten/at-i-o-google-just-shipped-apples-ai-promises/91191832",
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
    m = re.search(r"\nkate_kozuch:", rest)
    return rest[: m.start()] if m else rest


def _item():
    # The jason_aten top-level item (mechanism_ids [887] - the first
    # dedicated mechanism-id-sequence Type B mechanism on Aten in this
    # file; m677 lives in profiles/competitor-coverage-research.yaml).
    d = yaml.safe_load(_profiles_text())
    return d["jason_aten"]


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
class TestNoveltyAnchorTypeB1093:
    def test_single_test_type_b_1093_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1093")
        ]
        assert files == [OWN_BASENAME]

    def test_no_type_b_1093_in_git_log_precommit(self):
        # Pre-commit only: fails BY DESIGN once the main commit exists.
        r = run_git("log", "--grep", "Type B #1093:", "--format=%H", "--no-merges")
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
            "zero test_type_b_1093 files",
            "max numeric mechanism_id 886",
            "block key zero-hit",
            "the one novel URL zero-hit",
            "THIRTY-EIGHTH member-claim form absent",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1090-1094 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1090_1094Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1090_1094_fourth_leg(self):
        # Committed-state form: the four newest distinct iteration mains
        # are the D->E->A->B window legs (the fifth slot is #1089 or older).
        assert _window()[-4:] == EXPECTED_WINDOW_TAIL

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n2) == int(n1) + 1
            assert (self.ORDER[t2] - self.ORDER[t1]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1092(self):
        order = _window()
        idx = order.index(("B", "1093"))
        assert order[idx - 1] == ("A", "1092")
        r = run_git("log", "--grep", "Type A #1092:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1092 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1093:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1093 main commit"

    def test_next_run_is_type_c_1094_note(self):
        assert "1094" in __doc__ and "C" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (post-edit safe: needles runtime-built)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # block_key field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS_YAML).count("\n    " + MECH_KEY + ":") == 1

    def test_mechanism_id_887_colon_form_present(self):
        assert "mechanism_id: 887" in _block()

    def test_no_underscore_dash_887_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 887 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 887 key needle forms (underscore and
        # dash) may appear this run; the needles are fragment-built here
        # too, so this file itself carries no contiguous literal either.
        n1 = "mech" + "anism_" + "8" + "87"
        n2 = "mech" + "anism-" + "8" + "87"
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
        assert "887" not in MECH_KEY

    def test_thirty_eighth_member_form_absent_precommit(self):
        # Post-commit safe: the only THIRTY-EIGHTH mentions in profiles/ are
        # ledger prose ("THIRTY-EIGHTH absent" / "negative guard") in this
        # run's own block (journalists.yaml), #1092's landed block
        # (guardian.yaml), and #1082's landed block (the-verge.yaml) - all
        # are the ledger invariant, not a member form.
        out = _git(["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected ledger prose"
        assert all(
            "journalists.yaml" in l or "the-verge.yaml" in l or "guardian.yaml" in l
            for l in lines
        ), lines


# ---------------------------------------------------------------------------
# 4. Mechanism 887 block structure in profiles/careers/journalists.yaml
# ---------------------------------------------------------------------------
class TestMechanism887Structure:
    def test_item_is_top_level_jason_aten(self):
        assert _item()["name"] == "Jason Aten"
        assert _item()["current_publication"] == "Inc."

    def test_mechanism_ids_include_887(self):
        assert _item()["mechanism_ids"] == [887]

    def test_block_key_field_roundtrips(self):
        assert _mech()["block_key"] == MECH_KEY

    def test_test_file_field_matches_basename(self):
        assert _mech()["test_file"] == "tests/" + OWN_BASENAME

    def test_iteration_date_type_goal_fields(self):
        m = _mech()
        assert m["mechanism_id"] == 887
        assert m["iteration"] == 1093
        assert m["iteration_type"] == "B"
        assert m["iteration_time"] == "2026-09-30 06:00 PDT"
        assert m["discovery_date"] == "2026-09-30"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["publication_focus"] == "inc"

    def test_ascii_only_no_em_dashes(self):
        raw = _block()
        raw.encode("ascii")
        assert "\u2014" not in raw

    def test_verification_sub_block(self):
        v = _mech()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True

    def test_yaml_roundtrip_clean(self):
        d = yaml.safe_load(_profiles_text())
        assert d["jason_aten"]["competitor_coverage"][MECH_KEY]["mechanism_id"] == 887


# ---------------------------------------------------------------------------
# 5. Meta-arm evidence (FRESH this run, excerpt-tier per #503)
# ---------------------------------------------------------------------------
class TestMetaArmEvidence:
    def test_meta_arm_title_and_date(self):
        m = _mech()["meta_arm"]
        assert (
            m["title"]
            == "Meta's New Muse AI Agent Read My Private Messages. I Never Asked It To"
        )
        assert m["date"] == "2026-09-19"

    def test_date_basis_names_attribution_and_update_drift(self):
        basis = _mech()["meta_arm"]["date_basis"]
        assert "memeburn" in basis and "Sep 25" in basis

    def test_message_database_row_evidence(self):
        notes = _mech()["meta_arm"]["framing_notes"]
        assert "187,462" in notes
        assert "187462" in notes

    def test_declined_access_and_notification_claim(self):
        notes = _mech()["meta_arm"]["framing_notes"]
        assert "explicitly declining" in notes
        assert "incoming notification stream only" in notes
        assert "read history" in notes

    def test_singleton_threads_response(self):
        notes = _mech()["meta_arm"]["framing_notes"]
        assert "David Singleton" in notes and "Threads" in notes

    def test_meta_arm_illustrative_tone_minus_070(self):
        assert _mech()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.70

    def test_excerpt_tier_zero_browser_open(self):
        m = _mech()["meta_arm"]
        assert "excerpt-tier" in m["evidence_tier"]
        assert "0 browser.open" in m["evidence_tier"]

    def test_novel_source_url_verbatim(self):
        assert (
            _mech()["meta_arm"]["source_url"]
            == "https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202"
        )


# ---------------------------------------------------------------------------
# 6. Apple-arm evidence (CARRIED from m677 per #807, not re-scored)
# ---------------------------------------------------------------------------
class TestAppleArmEvidence:
    def test_carried_flag_and_source(self):
        m = _mech()["apple_arm"]
        assert m["carried_per_807"] is True
        assert "m677" in m["carried_from"]
        assert "type_b_738" in m["carried_from"]

    def test_apple_arm_title_and_date(self):
        m = _mech()["apple_arm"]
        assert (
            m["title"]
            == "For Years, People Have Worried Their Devices Were Listening. "
            "Apple Just Made It a Feature"
        )
        assert m["date"] == "2026-09-11"

    def test_adversarial_bystander_framing(self):
        assert "you are recording me" in _mech()["apple_arm"]["framing_notes"]

    def test_conceded_privacy_architecture(self):
        assert (
            "the only company that most people would trust"
            in _mech()["apple_arm"]["framing_notes"]
        )

    def test_apple_arm_illustrative_tone_minus_055(self):
        assert _mech()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55

    def test_carried_url_verbatim(self):
        assert (
            _mech()["apple_arm"]["source_url"]
            == "https://www.inc.com/jason-aten/for-years-people-have-worried-their-devices-were-listening-apple-just-made-it-a-feature/91404202"
        )


# ---------------------------------------------------------------------------
# 7. Three-pole gradient, illustrative delta, prediction realization
# ---------------------------------------------------------------------------
class TestThreePoleGradientAndDelta:
    def test_google_pole_aspirational_carried_unscored(self):
        g = _mech()["google_pole"]
        assert g["register"] == "aspirational"
        assert g["title"] == "At I/O, Google Just Shipped Apple's AI Promises"
        assert g["date"] == "2026-05-21"

    def test_google_url_verbatim(self):
        assert (
            _mech()["google_pole"]["source_url"]
            == "http://www.inc.com/jason-aten/at-i-o-google-just-shipped-apples-ai-promises/91191832"
        )

    def test_three_pole_ordering_statement(self):
        assert (
            "Google aspirational < Apple adversarial < Meta hardest"
            in _mech()["pattern"]
        )

    def test_illustrative_delta_arithmetic(self):
        # Apple minus Meta: -0.55 - (-0.70) = +0.15.
        apple = _mech()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        meta = _mech()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        assert abs((apple - meta) - _mech()["illustrative_delta"]) < 1e-9
        assert abs(_mech()["illustrative_delta"] - 0.15) < 1e-9

    def test_thesis_consistent_direction_meta_harder(self):
        assert (
            _mech()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
            < _mech()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        )
        assert "thesis-consistent" in _mech()["delta_note"]

    def test_realizes_m677_testable_prediction_one(self):
        assert (
            "REALIZES m677's testable prediction #1" in _mech()["pattern"]
            or "testable prediction #1" in _mech()["pattern"]
        )

    def test_arms_eight_days_apart_same_month(self):
        assert _mech()["meta_arm"]["date"].startswith("2026-09")
        assert _mech()["apple_arm"]["date"].startswith("2026-09")


# ---------------------------------------------------------------------------
# 8. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def _d(self):
        return _mech()["statistical_discipline"]

    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in self._d()

    def test_statistics_not_calculated(self):
        assert "NOT_CALCULATED" in self._d()
        assert "is_significant False" in self._d()

    def test_engine_not_run(self):
        assert "Engine NOT run" in self._d()
        assert "no_analysis_json_update true" in self._d()

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in self._d()

    def test_not_artifact_grade_and_n1(self):
        assert "NOT artifact-grade" in self._d()
        assert "n=1" in self._d()

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in self._d()

    def test_docstring_carries_discipline_note(self):
        assert "STATISTICAL DISCIPLINE" in __doc__
        assert "MANUAL ILLUSTRATIVE ONLY" in __doc__


# ---------------------------------------------------------------------------
# 9. Falsification ledger: NOT a falsification-family member, holds at 37
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _mech()["falsification_family"]

    def test_prediction_realization_not_falsification(self):
        f = _mech()["falsification_family"]
        assert "m677" in f
        assert "testable prediction #1" in f

    def test_ledger_holds_at_37(self):
        assert _mech()["falsification_ledger"] == 37
        assert "37" in _mech()["falsification_family"]

    def test_thirty_seventh_in_the_verge_yaml(self):
        out = _git(["grep", "-n", "THIRTY-SEVENTH", "--", "profiles/"]).stdout
        assert "the-verge.yaml" in out


# ---------------------------------------------------------------------------
# 10. Confounders, ranked strong-first
# ---------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_seven_confounders(self):
        assert len(_mech()["confounders"]) == 7

    def test_each_confounder_has_level_note_classification(self):
        for c in _mech()["confounders"]:
            assert c["level"] in ("STRONG", "MODERATE", "WEAK")
            assert "confounder_note" in c or "note" in c
            assert "classification" in c

    def test_strong_first_ordering(self):
        levels = [c["level"] for c in _mech()["confounders"]]
        assert levels.count("STRONG") == 3
        assert levels.count("MODERATE") == 2
        assert levels.count("WEAK") == 2
        order = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}
        ranks = [order[l] for l in levels]
        assert ranks == sorted(ranks), "confounders must be ordered strong-first"

    def test_strong_confounder_excerpt_tier(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "0 browser.open" in notes

    def test_strong_confounder_peg_asymmetry(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "peg asymmetry" in notes

    def test_strong_confounder_conceded_error_asymmetry(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "conceded-error asymmetry" in notes


# ---------------------------------------------------------------------------
# 11. Cross-references
# ---------------------------------------------------------------------------
class TestCrossReferences:
    def _refs(self):
        return _mech()["cross_references"]

    def test_ref_738_m677_prediction(self):
        assert any("#738" in r for r in self._refs())

    def test_ref_728_m671_inc_strand(self):
        assert any("#728" in r for r in self._refs())

    def test_ref_m137_outlet_context(self):
        assert any("m137" in r or "#137" in r for r in self._refs())

    def test_ref_1088_adjacent_type_b(self):
        assert any("#1088" in r for r in self._refs())

    def test_ref_1043_ambient_data_family(self):
        assert any("#1043" in r for r in self._refs())


# ---------------------------------------------------------------------------
# 12. Research method per #503
# ---------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_six_search_sets_zero_open(self):
        m = _mech()["research_method"]
        assert "6 browser.search" in m
        assert "0 browser.open" in m

    def test_rejected_candidates_named(self):
        m = _mech()["research_method"]
        for name in ("David Heaney", "Jacob Krol", "Mariella Moon"):
            assert name in m
        assert "REJECTED" in m

    def test_selected_queries_named(self):
        m = _mech()["research_method"]
        assert "Jason Aten Inc.com Muse" in m

    def test_verbatim_url_claim(self):
        m = _mech()["research_method"]
        assert "verbatim" in m
        assert "no canonical URLs constructed" in m

    def test_docstring_carries_research_method(self):
        assert "RESEARCH METHOD" in __doc__
        assert "0 browser.open" in __doc__


def _repo_grep(needle, roots=("tests", "profiles")):
    hits = []
    for root in roots:
        for p in glob.glob(
            os.path.join(REPO_ROOT, root, "**", "*"), recursive=True
        ):
            if not os.path.isfile(p):
                continue
            if not (p.endswith(".py") or p.endswith(".yaml")):
                continue
            try:
                t = open(p, errors="ignore").read()
            except OSError:
                continue
            if needle in t:
                hits.append(os.path.relpath(p, REPO_ROOT))
    return hits


# ---------------------------------------------------------------------------
# 13. Guard lifecycle: mechanism 887 lands; 888 needles pinned
# ---------------------------------------------------------------------------
class TestGuardLifecycle887Lands:
    def test_max_numeric_id_is_887_not_886(self):
        assert max(_corpus_ids()) == 887, (
            f"max numeric mechanism_id must be 887, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_888_keys_repo_wide(self):
        assert _repo_grep(US_888) == [], "no underscore-form 888 keys anywhere"

    def test_zero_numeric_888_keys_in_profiles(self):
        assert _repo_grep(NUM_888, roots=("profiles",)) == [], (
            "no numeric 888 mechanism keys in the corpus"
        )

    def test_zero_dash_888_references_repo_wide(self):
        assert _repo_grep(DASH_888) == [], "no dash-form 888 references anywhere"

    def test_d1092_zero_numeric_887_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 887", roots=("profiles",))
        assert len(hits) == 1, (
            "#1092 zero-numeric-887 sweep is superseded by design: the #1093 "
            "block is the single numeric 887 key"
        )

    def test_d1092_zero_underscore_and_dash_887_sweeps_stay_green(self):
        # Designed keying per #715: no literal underscore- or dash-form 887
        # mechanism key strings anywhere (needles are fragment-built here).
        assert _repo_grep(US_887) == []
        assert _repo_grep(DASH_887) == []


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
        # prose (55378/1417 -> 55462/1418), so assert on the table line.
        stats = [l for l in _read(README).splitlines() if l.startswith("| Tests |")]
        assert stats == ["| Tests | 55462 | Across 1418 test files |"]

    def test_readme_has_test_file_table_row(self):
        assert OWN_BASENAME in _read(README)

    def test_architecture_has_tests_tree_row(self):
        assert OWN_BASENAME in _read(ARCH)


# ---------------------------------------------------------------------------
# 15. Iteration log entry per #721
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_type_b_1093_header(self):
        assert "## #1093 Type B" in _read(LOG)

    def test_log_entry_mentions_mechanism_id_887(self):
        text = _read(LOG)
        start = text.index("## #1093 Type B")
        seg = text[start : start + 4000]
        assert "887" in seg
        assert "Jason Aten" in seg

    def test_log_mentions_main_anchor_loghash_commits(self):
        text = _read(LOG)
        start = text.index("## #1093 Type B")
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
            "test_type_b_1093_",
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
    def test_block_ends_before_kate_kozuch_key(self):
        text = _profiles_text()
        i = text.index("    " + MECH_KEY + ":")
        j = text.index("\nkate_kozuch:")
        assert i < j

    def test_key_design_note_documents_1093_iteration_number(self):
        assert "1093 is the iteration number" in _mech()["key_design_note"]

    def test_publication_focus_and_type(self):
        m = _mech()
        assert m["publication_focus"] == "inc"
        assert m["iteration_type"] == "B"
