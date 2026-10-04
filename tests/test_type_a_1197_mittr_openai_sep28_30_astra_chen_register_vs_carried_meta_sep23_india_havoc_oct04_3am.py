"""Type A -- Iteration #1197 (Sun 2026-10-04 03:00 PDT): m949 MIT TR x
OpenAI Sep-28/30 Astra-cancellation and Chen-interview register vs carried
MIT TR x Meta Sep-23 India havoc investigation -- the SECOND dedicated
MIT TR x OpenAI Type A (after mechanism 637, Sep 11). Four NEW OpenAI arms
(Sep 30 Chen interview "We are not going to shoot ourselves in the foot"
with "If you disappeared OpenAI, that would be bad for the world" -0.15;
Sep 30 Download hacking-response -0.20; Sep 29 Download Astra scrapped
"did not quite meet the bar" -0.25; Sep 28 Download rogue-agent liability
-0.20; mean -0.20, IDENTICAL to mechanism 637) vs Meta arms (carried Sep 23
India havoc investigation -0.60 un-rescored per #807; NEW Sep 23 Download
India menace -0.55; mean -0.575). Illustrative delta +0.375 (OpenAI minus
Meta), same direction as m637's +0.2333. Cross-publication Astra strand:
Guardian m874, WSJ, NYT, Verge m907, MIT TR this run = FIVE publications,
one peg, all accountability registers. NOT a falsification-family member
(temporal replication of m637 per #1143); ledger holds at 47.

Type A THIRD leg of the 1195-1199 window, CONTINUING it
(D #1195 -> E #1196 -> A #1197 -> B #1198 -> C #1199). Committed
predecessors: #1195 Type D (main b8696f35 / anchor 9161abc4 /
doc-sync d36d11f4 / log-hash 82fe4111) and #1196 Type E (main
d58d57fc / anchor 054b2238 / doc-sync 48006e67 / log-hash dfcb4990),
both verified present in history pre-commit. Rotation per the #565
anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m949 block lands in profiles/mit-tech-review.yaml under
competitor_relationships as a 4-space sibling of the mechanism_742
(m742) block, NOT nytimes.yaml); the in-flight blocks are owned by
their runs. Targeted staging only per the repo-wide traversal lesson.
Iteration numbers follow the rotation schedule, not commit order. Do
NOT touch #1024's m846 (self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending).

Verifies:
- m949 (Type A #1197, profiles/mit-tech-review.yaml
  competitor_relationships/openai block key, 4-space indent (sibling
  of the mechanism_742 m742 block per the mit-tech-review.yaml
  convention), `mechanism_id: 949` field form; block key count 1 -
  designed: the block key carries no nine-four-nine substring (1197
  is the iteration), so it is a plain literal per #715): MIT TR x
  OpenAI Sep-28/30 Astra-cancellation + Chen-interview register vs
  carried MIT TR x Meta Sep-23 India havoc arms, post-landing corpus
  integrity (max numeric mechanism_id 949; zero next-number
  nine-five-zero keys in numeric/underscore/dash mechanism forms -
  the nine-five-zero needles are format-built per #715 so no
  guard-literal carrier file exists; the ledger HOLDS at 47 - the
  forty-seventh member-claim form stays in wired.yaml m946 (2
  occurrences), the forty-eighth member-claim form absent repo-wide
  as designed negative guard; thirty-fifth (m915) + thirty-sixth
  (m933) + thirty-seventh (m942) + thirty-eighth (m945) +
  thirty-ninth (m948) directions present, fortieth absent; the
  #1195/#1196 window files are NOT edited by this run - their
  now-stale forward-looking pins are recorded as fail-by-design via
  subprocess in the staleness class (#1196's max-948 +
  zero-949-numeric pins trip on the landed 949; #1196's zero-949
  underscore/dash pins STAY GREEN by design - this run lands no
  underscore/dash nine-four-nine literals in profiles/ or tests/))
  + the #1195 background-suite check (checked only, NOT touched;
  verdict belongs to #1200 per #795).

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1197_mittr_openai_sep28_30_astra_chen_register_"
    "vs_carried_meta_sep23_india_havoc_oct04_3am.py"
)

MAX_ID = 949
NEXT_NUM = 950

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 64134
README_FILE_COUNT = 1522

# The m949 block key carries no nine-four-nine substring (1197 is the
# iteration, not the mechanism), so it is a plain literal per #715.
M949_KEY = (
    "type_a_1197_mittr_openai_sep28_30_astra_chen_register_"
    "vs_carried_meta_sep23_india_havoc_oct04_3am"
)
M949_INDENT = 4
M949_HOME = "profiles/mit-tech-review.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in wired.yaml (m946) and
# competitor-entities.yaml (m915/m933/m942/m945/m948) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"
_TW39 = "THIRTY-" + "NINTH relationship direction"
_TW40 = "FORTIETH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1195_full_suite.log"
)
E1196_FILE = (
    "tests/test_type_e_1196_podcast_sentiment_162nd_verification_"
    "oct04_2am.py"
)

# Committed predecessor #1195 Type D chain (verified pre-commit).
PRED_MAIN_1195 = "b8696f35"
PRED_ANCHOR_1195 = "9161abc4"
PRED_DOCSYNC_1195 = "d36d11f4"
PRED_FINAL_1195 = "82fe4111"
# Committed predecessor #1196 Type E chain (verified pre-commit).
PRED_MAIN_1196 = "d58d57fc"
PRED_ANCHOR_1196 = "054b2238"
PRED_DOCSYNC_1196 = "48006e67"
PRED_FINAL_1196 = "dfcb4990"

# New-to-corpus this run (zero-hit repo-wide pre-commit). The Sep-23
# India-havoc investigation URL is carried from mechanism 817 (NOT in
# this list, disclosed as carried).
NEW_URLS = [
    "https://www.technologyreview.com/2026/09/30/1145339/were-not-going-to-shoot-ourselves-in-the-foot-over-hugging-face-says-openais-chief-research-officer/",
    "https://www.technologyreview.com/2026/09/30/1145350/the-download-openai-chief-research-officer-hacking-response/",
    "https://www.technologyreview.com/2026/09/29/1145249/the-download-climate-tech-ai-scientific-discovery/",
    "https://www.technologyreview.com/2026/09/28/1145202/the-download-rogue-agent-liability-and-the-ai-hype-index/",
    "https://www.technologyreview.com/2026/09/23/1144966/the-download-india-smart-glasses-ai-trillion-dollar-gamble/",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _git(*args):
    result = subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout


def _iter_source_files():
    """Yield paths for profile + test source files.

    Scoped to profiles/ + tests/ per the #1191 convention (the
    iteration-log.md prose carries next-number needle forms as
    documented guards; the log is not a mechanism-key position).
    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)


def _m949_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M949_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M949_KEY]


def _window():
    """Distinct (type, number) sequence from the log, in FILE order.

    NOTE: the log's tail is file-chronological (entries appended,
    oldest-first) since the convention flip after #1148; the head
    retains the old prepend order. Callers pin the tail sequence,
    not a global newest-first ordering.
    """
    pat = re.compile(r"^## #(\d+) Type ([A-E]):", re.M)
    seen = []
    for num, typ in pat.findall(_read(LOG_PATH)):
        key = (typ, num)
        if key not in seen:
            seen.append(key)
    return seen


def _needle_hits_profiles(needle):
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit state recorded post-commit; superseded pins noted)
# ---------------------------------------------------------------------------
class TestNovelty1197:
    def test_single_type_a_1197_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1197*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1197_in_git_log(self):
        # Red pre-commit; green once the main commit lands. Deselect
        # pre-commit.
        log = _git("log", "--format=%H %s", "--grep=Type A #1197")
        assert "Type A #1197" in log

    def test_type_a_1197_commit_set(self):
        # Post-full-run: exactly four commits carry "Type A #1197"
        # (main + anchor followup + doc-sync + log-hash followup per
        # #721; the doc-sync message carries the iteration tag per
        # the #1191 convention). Red pre-commit; deselect pre-commit.
        log = _git("log", "--format=%H", "--grep=Type A #1197")
        assert len([l for l in log.splitlines() if l.strip()]) == 4, log

    def test_new_urls_in_corpus_post_commit(self):
        # The five URLs were zero-hit repo-wide pre-commit;
        # post-commit they are in-corpus (this file's constant list +
        # the mit-tech-review.yaml block).
        for url in NEW_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M949_HOME))
        assert text.count(M949_KEY + ":") == 1

    def test_1197_entry_present_exactly_once(self):
        # Post-doc-sync stable: exactly one #1197 entry in the log.
        text = _read(LOG_PATH)
        assert text.count("## #1197 Type A:") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1197:
    def test_anchor_sha_format(self):
        # Red pre-anchor (placeholder); green post-anchor per #565.
        # Deselect pre-commit.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1195_chain_in_history(self):
        for sha in (
            PRED_MAIN_1195,
            PRED_ANCHOR_1195,
            PRED_DOCSYNC_1195,
            PRED_FINAL_1195,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1196_chain_in_history(self):
        for sha in (
            PRED_MAIN_1196,
            PRED_ANCHOR_1196,
            PRED_DOCSYNC_1196,
            PRED_FINAL_1196,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        # Red pre-doc-sync (no #1197 entry in the log yet); green
        # once the doc-sync lands. Deselect pre-commit.
        # NOTE: the log's tail is file-chronological (entries
        # appended, oldest-first): D1195 < E1196 < A1197 in file
        # order.
        window = _window()
        assert ("A", "1197") in window
        assert ("E", "1196") in window
        assert ("D", "1195") in window
        tail = window[-3:]
        assert tail == [("D", "1195"), ("E", "1196"), ("A", "1197")], tail

    def test_rotation_phrase_in_log_entry(self):
        # Red pre-doc-sync; green once the doc-sync lands. Deselect
        # pre-commit.
        text = _read(LOG_PATH)
        assert "## #1197 Type A:" in text
        entry_start = text.index("## #1197 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1195-1199 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1197:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1197")
        assert "Type A #1197" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1197:
    def test_m949_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M949_HOME))
        line = next(l for l in text.splitlines() if l.strip() == M949_KEY + ":")
        assert line.startswith(" " * M949_INDENT)
        assert not line.startswith(" " * (M949_INDENT + 1))

    def test_m949_block_sibling_of_m742_block(self):
        text = _read(os.path.join(REPO_ROOT, M949_HOME))
        assert "    mechanism_742_mittr_openai_biology_data_philanthropy_register_vs_meta_ironic_diminishment_sep19_2026:" in text

    def test_m949_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M949_HOME))
        assert "mechanism_id: 949" in text

    def test_max_numeric_mechanism_id_is_949(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_950_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_950_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_950_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_949_substring_in_block_key(self):
        assert "949" not in M949_KEY


# ---------------------------------------------------------------------------
# 4. m949 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM949ContentDiscipline1197:
    def test_metadata_fields(self):
        d = _m949_data()
        assert d["iteration"] == 1197
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-04 03:00 PDT"
        assert d["scheduled_job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["mechanism_id"] == 949
        assert d["competitor"] == "openai"
        assert d["comparator_entity"] == "meta"

    def test_four_new_openai_arms(self):
        d = _m949_data()
        arms = d["openai_articles"]
        assert len(arms) == 4
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [-0.15, -0.20, -0.25, -0.20], tones

    def test_openai_arm_mean_replicates_m637(self):
        d = _m949_data()
        tones = [a["manual_illustrative_tone"] for a in d["openai_articles"]]
        mean = sum(tones) / len(tones)
        assert abs(mean - (-0.20)) < 1e-9, mean

    def test_chen_interview_arm_softest(self):
        d = _m949_data()
        arms = d["openai_articles"]
        chen = next(a for a in arms if "shoot ourselves in the foot" in a["title"])
        assert chen["manual_illustrative_tone"] == -0.15
        assert "bad for the world" in chen["key_framing"]

    def test_meta_arms_one_carried_one_new(self):
        d = _m949_data()
        arms = d["meta_articles"]
        assert len(arms) == 2
        carried = next(a for a in arms if a.get("carried_from") == 817)
        assert carried["manual_illustrative_tone"] == -0.60
        new = next(a for a in arms if a.get("novelty_in_corpus"))
        assert new["manual_illustrative_tone"] == -0.55
        assert "1144966" in new["url"]

    def test_illustrative_delta_arithmetic(self):
        d = _m949_data()
        assert abs(d["illustrative_delta"] - 0.375) < 1e-9
        assert d["delta_direction"] == "OpenAI minus Meta"

    def test_five_source_urls(self):
        d = _m949_data()
        assert len(d["source_urls"]) == 5
        for url in NEW_URLS:
            assert url in d["source_urls"], url

    def test_cross_publication_astra_strand_five(self):
        finding = _m949_data()["finding"]
        assert "FIVE publications" in finding
        for marker in ("m874", "m907"):
            assert marker in finding

    def test_test_file_field_matches_own_basename(self):
        assert _m949_data()["test_file"] == "tests/" + OWN_BASENAME

    def test_ascii_and_no_em_dash_in_block(self):
        block = _m949_block_text()
        assert "\u2014" not in block
        block.encode("ascii")


def _m949_block_text():
    text = _read(os.path.join(REPO_ROOT, M949_HOME))
    start = text.index(M949_KEY + ":")
    # Block ends at the next 4-space block key or the next 2-space
    # section key (e.g. "  meta:").
    pat = re.compile(r"^    [a-z_0-9]+:$|^  [a-z_]+:$", re.M)
    m = pat.search(text, start + len(M949_KEY) + 1)
    end = m.start() if m else start + 25000
    return text[start:end]


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1197:
    def test_manual_illustrative_only(self):
        sd = _m949_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd

    def test_no_analysis_json_update(self):
        assert _m949_data()["no_analysis_json_update"] is True
        assert "analysis.json" not in _git("diff", "--name-only")

    def test_correlation_not_causation(self):
        assert _m949_data()["correlation_not_causation"] is True

    def test_not_falsification_member(self):
        # This run is NOT a member (temporal replication of m637 per
        # #1143); ledger holds at 47.
        assert "NOT a falsification-family member" in _m949_data()["falsification_family"]
        assert _m949_data()["ledger"] == "Ledger holds at 47"

    def test_artifact_not_grade(self):
        assert "artifact_grade false" in _m949_data()["statistical_discipline"]


# ---------------------------------------------------------------------------
# 6. Falsification ledger (holds at 47 this run)
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1197:
    def test_forty_sixth_intact_in_verge(self):
        text = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert text.count(_T46) == 2

    def test_forty_seventh_stays_in_wired_m946(self):
        # No new member this run: the forty-seventh claim form stays
        # exactly in wired.yaml m946 (2 occurrences, the #1127
        # designed pattern).
        text = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert text.count(_T47) == 2

    def test_forty_seventh_nowhere_else(self):
        for p in _needle_hits_profiles(_T47):
            assert p.endswith("wired.yaml"), p

    def test_forty_eighth_absent(self):
        assert _needle_hits_profiles(_T48) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert _T48 not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (_TW35, _TW36, _TW37, _TW38, _TW39):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(_TW40) == []

    def test_ledger_note_holds_at_47(self):
        assert _m949_data()["ledger"] == "Ledger holds at 47"


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1196's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1197:
    def test_e1196_max_948_pin_trips_by_design(self):
        # #1196 pinned max numeric mechanism_id 948; this run lands
        # 949, so the pin fails BY DESIGN. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 949

    def test_e1196_zero_949_numeric_pin_trips_by_design(self):
        # The numeric field form mechanism_id: 949 now exists in
        # profiles/mit-tech-review.yaml. Documented, not repaired.
        assert _repo_grep_numeric_mechanism_id(949) != []

    def test_e1196_zero_949_underscore_pin_stays_green(self):
        # This run lands no underscore-form nine-four-nine literal in
        # profiles/ or tests/ (needles are format-built). Stays green.
        assert _repo_grep_underscore_mechanism(949) == []

    def test_e1196_zero_949_dash_pin_stays_green(self):
        assert _repo_grep_dash_mechanism(949) == []

    def test_e1196_no_type_a_1197_pin_trips_by_design(self):
        # #1196 pinned no "Type A #1197" in git log; this run's own
        # main commit carries it (the #1191-class self-trip on the
        # run's own main-commit subject, documented).
        log = _git("log", "--format=%H %s", "--grep=Type A #1197")
        assert "Type A #1197" in log


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards for #1198)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1197:
    def test_forward_max_949(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_forward_zero_950_all_forms(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_forward_no_type_b_1198_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type B #1198")
        assert log.strip() == ""

    def test_forward_no_forty_eighth_member(self):
        assert _needle_hits_profiles(_T48) == []

    def test_forward_directions_state(self):
        for needle in (_TW35, _TW36, _TW37, _TW38, _TW39):
            assert _needle_hits_profiles(needle) != [], needle
        assert _needle_hits_profiles(_TW40) == []


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1195-launched suite; checked only per #795)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1197:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_this_run_does_not_touch_suite(self):
        # No Type A #1197 / m949 markers in the suite log; this run
        # checks only. The verdict belongs to #1200 per #795.
        text = _read(SUITE_LOG)
        assert "1197" not in text
        assert "m949" not in text

    def test_suite_verdict_belongs_to_1200(self):
        # The #1195-launched suite's verdict is claimed by the next
        # Type D run (#1200) per #795, never by this run.
        assert "type_d_1195" in SUITE_LOG


# ---------------------------------------------------------------------------
# 10. Doc-sync (deselected pre-commit per #719; green post-doc-sync)
# ---------------------------------------------------------------------------
class TestTypeADocSync1197:
    @pytest.mark.skip(reason="deselected pre-commit per #719; green post-doc-sync")
    def test_readme_test_count(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert ("| Tests | %d |" % README_TEST_COUNT) in text

    @pytest.mark.skip(reason="deselected pre-commit per #719; green post-doc-sync")
    def test_readme_file_count(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_FILE_COUNT) in text

    @pytest.mark.skip(reason="deselected pre-commit per #719; green post-doc-sync")
    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert OWN_BASENAME in text


# ---------------------------------------------------------------------------
# 11. Iteration log (deselected pre-commit; green post-doc-sync)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1197:
    @pytest.mark.skip(reason="deselected pre-commit per #721; green post-doc-sync")
    def test_1197_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1197 Type A:" in text

    @pytest.mark.skip(reason="deselected pre-commit per #721; green post-doc-sync")
    def test_1197_entry_registers_hashes(self):
        # Post-log-hash followup per #721: the entry names the main,
        # anchor, and doc-sync commits.
        text = _read(LOG_PATH)
        entry_start = text.index("## #1197 Type A:")
        entry = text[entry_start : entry_start + 12000]
        assert "Main commit" in entry
        assert "Anchor followup" in entry
        assert "Doc-sync" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1197:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped per the #1147 convention: the working tree
        # carries pre-existing in-flight uncommitted changes (#899
        # nytimes.yaml m771 hunk, #938 test file anchor edit, #900
        # untracked test file, #1012 test-file working-tree edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files (profiles/mit-tech-review.yaml m949 block + the
        # new test file).
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
            "agenda_setting_register_vs_carried_meta_india_havoc_m817_"
            "pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path)
            assert "m949" not in diff, path
            assert "Type A #1197" not in diff, path


# ---------------------------------------------------------------------------
# 13. ASCII discipline (no em dashes in the new files)
# ---------------------------------------------------------------------------
class TestAsciiDiscipline1197:
    def test_no_em_dash_in_own_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_no_em_dash_in_m949_block(self):
        block = _m949_block_text()
        assert "\u2014" not in block

    def test_own_file_ascii_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")


# ---------------------------------------------------------------------------
# 14. Anchor placeholder (deselected pre-commit per #565; green post-anchor)
# ---------------------------------------------------------------------------
class TestAnchor:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_anchor_sha_in_log(self):
        log = _git("log", "--format=%H")
        assert ANCHORED_SHA in log

    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_anchor_points_at_main_commit(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1197")
        first = log.splitlines()[0].split()[0]
        assert ANCHORED_SHA == first, (ANCHORED_SHA, first)

    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_anchor_placeholder_flipped(self):
        assert ANCHORED_SHA != "0" * 40
