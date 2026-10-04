"""Type A -- Iteration #1192 (Sat 2026-10-03 23:00 PDT): m946 WIRED x
OpenAI Oct-2-2026 macOS CVE-2026-100754 accountability original plus the
WIRED "fancy pinky-swear" accord-skepticism arm vs carried WIRED x Meta
accountability arms (m757/m820 via m916, un-rescored per #807) -- a
security-accountability-register deep dive on the deal partner: WIRED's
security desk published an ORIGINAL adversarial-technical piece on the
$1-5M/yr licensing counterparty on Oct 2 (CVE-2026-100754, "insanely
trivial" exploit, chat logs plus browser sessions exposed; four
independent relays carry verbatim WIRED attribution) plus a skeptical-
policy register on the Sep-29 Trump accord OpenAI championed.
Pooled illustrative delta +0.075 near-null; the clean matched-register
read (CVE -0.40 vs m757 NameTag -0.30 = -0.10) has the partner HARDER.
The member-claim form this run lands advances the ledger 46->47 (the
uniform payer-softening prediction fails on the suppression claim:
the deal did not suppress an adversarial WIRED original on the partner
in the same week the partner drew bounded-absence silence on the
rogue-agent disclosure, m916). Second WIRED publication-level member;
first product-security-register member.

Type A THIRD leg of the 1190-1194 window, CONTINUING it
(D #1190 -> E #1191 -> A #1192 -> B #1193 -> C #1194). Committed
predecessors: #1190 Type D (main 3898443d / anchor c747ecb1 /
doc-sync 2fd8c400 / log-hash 123e5d73) and #1191 Type E (main
b0b7f13f / anchor 8e052a5f / doc-sync ebe1a3c7 / log-hash a27ca0db),
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
m946 block lands in profiles/wired.yaml under competitor_relationships
as a 4-space sibling of the type_a_1142 (m916) block, NOT
nytimes.yaml); the in-flight blocks are owned by their runs.
Targeted staging only per the repo-wide traversal lesson. Iteration
numbers follow the rotation schedule, not commit order. Do NOT touch
#1024's m846 (self-flagged sourcing-constraint violation; Ray's
revert/leave/rebuild-from-primary decision still pending).

Verifies:
- m946 (Type A #1192, profiles/wired.yaml competitor_relationships/
  openai block key, 4-space indent (sibling of the type_a_1142 m916
  block per the wired.yaml convention), `mechanism_id: 946` field
  form; block key count 1 - designed: the block key carries no
  nine-four-six substring (1192 is the iteration), so it is a plain
  literal per #715): WIRED x OpenAI Oct-2 macOS CVE-2026-100754
  accountability original + accord-skepticism arm vs carried WIRED x
  Meta arms, post-landing corpus integrity (max numeric mechanism_id
  946; zero next-number nine-four-seven keys in numeric/underscore/
  dash mechanism forms - the nine-four-seven needles are format-built
  per #715 so no guard-literal carrier file exists; the ledger
  advances 46->47 - the member-claim form this run lands present
  (m946, profiles/wired.yaml, 2 occurrences - the #1127 designed
  pattern), the next member-claim form absent repo-wide as designed
  negative guard for the next landing; thirty-fifth (m915) +
  thirty-sixth (m933) + thirty-seventh (m942) + thirty-eighth (m945)
  directions present, thirty-ninth absent; the #1190/#1191 window
  files are NOT edited by this run - their now-stale forward-looking
  pins are recorded as fail-by-design via subprocess in the staleness
  class (#1191's max-945 + zero-946-numeric pins trip on the landed
  946; #1191's zero-946 underscore/dash pins STAY GREEN by design -
  this run lands no underscore/dash nine-four-six literals in
  profiles/ or tests/)) + the #1190 background-suite check (checked
  only, NOT touched; verdict belongs to #1195 per #795).

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
    "test_type_a_1192_wired_openai_oct02_macos_cve100754_"
    "accountability_original_vs_carried_meta_arms_oct03_11pm.py"
)

MAX_ID = 946
NEXT_NUM = 947

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40  # placeholder; patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 63752
README_FILE_COUNT = 1517

# The m946 block key carries no nine-four-six substring (1192 is the
# iteration, not the mechanism), so it is a plain literal per #715.
M946_KEY = (
    "type_a_1192_wired_openai_oct02_macos_cve100754_"
    "accountability_original_vs_carried_meta_arms_oct03_11pm"
)
M946_INDENT = 4
M946_HOME = "profiles/wired.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907),
# in wired.yaml (this run's m946), and competitor-entities.yaml
# (m915/m933/m942/m945) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"
_TW39 = "THIRTY-" + "NINTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1190_full_suite.log"
)
E1191_FILE = (
    "tests/test_type_e_1191_podcast_sentiment_161st_verification_"
    "oct03_11pm.py"
)

# Committed predecessor #1190 Type D chain (verified pre-commit).
PRED_MAIN_1190 = "3898443d"
PRED_ANCHOR_1190 = "c747ecb1"
PRED_DOCSYNC_1190 = "2fd8c400"
PRED_FINAL_1190 = "123e5d73"
# Committed predecessor #1191 Type E chain (verified pre-commit).
PRED_MAIN_1191 = "b0b7f13f"
PRED_ANCHOR_1191 = "8e052a5f"
PRED_DOCSYNC_1191 = "ebe1a3c7"
PRED_FINAL_1191 = "a27ca0db"

# New-to-corpus this run (zero-hit repo-wide pre-commit).
NEW_URLS = [
    "https://www.thehackacademy.com/news/chatgpt-macos-cve-2026-100754-fix/",
    "https://www.webpronews.com/chatgpt-mac-app-flaw-exposed-chat-logs-and-browser-sessions-to-local-attacks/",
    "https://nationalcybersecurity.com/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data-hacking-cybersecurity-infosec-comptia-pentest-hacker/",
    "https://technewsvision.co.uk/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/",
    "https://madrobot.blog/2026/10/02/chatgpt-mac-app-flaw-patched-patrick-wardle-objective-see-chat-logs/",
    "https://www.webpronews.com/openai-flags-gaps-in-trumps-morally-binding-ai-accord-as-industry-self-policing-takes-center-stage/",
    "https://techaiwire.com/articles/openai-fires-three-safety-researchers-metr-redwood/",
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
    iteration-log.md #1190 prose carries next-number needle forms as
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


def _m946_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M946_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M946_KEY]


def _window():
    """Newest-first distinct (type, number) sequence from the log."""
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
class TestNovelty1192:
    def test_single_type_a_1192_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1192*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1192_in_git_log(self):
        # Red pre-commit; green once the main commit lands. Deselect
        # pre-commit.
        log = _git("log", "--format=%H %s", "--grep=Type A #1192")
        assert "Type A #1192" in log

    def test_type_a_1192_commit_set(self):
        # Post-full-run: exactly three commits carry "Type A #1192"
        # (main + anchor followup + log-hash followup per #721).
        # Red pre-commit; deselect pre-commit.
        log = _git("log", "--format=%H", "--grep=Type A #1192")
        assert len([l for l in log.splitlines() if l.strip()]) == 3, log

    def test_new_urls_in_corpus_post_commit(self):
        # The seven URLs were zero-hit repo-wide pre-commit;
        # post-commit they are in-corpus (this file's constant list +
        # the wired.yaml block).
        for url in NEW_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M946_HOME))
        assert text.count(M946_KEY + ":") == 1

    def test_no_1192_row_pre_commit_state_recorded(self):
        # Pre-commit: no #1192 row in the doc tables or the log.
        # Recorded as fail-by-design post-doc-sync.
        assert "Type A #1192" not in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1192:
    def test_anchor_sha_format(self):
        # Red pre-anchor (placeholder); green post-anchor per #565.
        # Deselect pre-commit.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1190_chain_in_history(self):
        for sha in (
            PRED_MAIN_1190,
            PRED_ANCHOR_1190,
            PRED_DOCSYNC_1190,
            PRED_FINAL_1190,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1191_chain_in_history(self):
        for sha in (
            PRED_MAIN_1191,
            PRED_ANCHOR_1191,
            PRED_DOCSYNC_1191,
            PRED_FINAL_1191,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        # Red pre-doc-sync (no #1192 entry in the log yet); green
        # once the doc-sync lands. Deselect pre-commit.
        window = _window()
        assert ("A", "1192") in window
        assert ("E", "1191") in window
        assert ("D", "1190") in window
        # Newest-first ordering: A1192 newer than E1191 newer than D1190.
        assert window.index(("A", "1192")) < window.index(("E", "1191"))
        assert window.index(("E", "1191")) < window.index(("D", "1190"))

    def test_rotation_phrase_in_log_entry(self):
        # Red pre-doc-sync; green once the doc-sync lands. Deselect
        # pre-commit.
        text = _read(LOG_PATH)
        assert "## #1192 Type A:" in text
        entry_start = text.index("## #1192 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1190-1194 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1192:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1192")
        assert "Type A #1192" in log
        assert ANCHORED_SHA in log

# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1192:
    def test_m946_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M946_HOME))
        line = next(l for l in text.splitlines() if l.strip() == M946_KEY + ":")
        assert line.startswith(" " * M946_INDENT)
        assert not line.startswith(" " * (M946_INDENT + 1))

    def test_m946_block_sibling_of_m916_block(self):
        text = _read(os.path.join(REPO_ROOT, M946_HOME))
        assert (
            "    type_a_1142_wired_openai_sep26_rogue_agent_gov_"
            "disclosure_bounded_absence_vs_cameron_jul28_adversarial_"
            "oct02_5am:" in text
        )

    def test_m946_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M946_HOME))
        assert "mechanism_id: 946" in text

    def test_max_numeric_mechanism_id_is_946(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_947_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_947_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_947_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_946_substring_in_block_key(self):
        assert "946" not in M946_KEY


# ---------------------------------------------------------------------------
# 4. m946 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM946ContentDiscipline1192:
    def test_metadata_fields(self):
        d = _m946_data()
        assert d["iteration"] == 1192
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-03 23:00 PDT"
        assert d["scheduled_job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["author"] == "Kit (with Ray)"
        assert d["publication_pair"] == "WIRED x OpenAI"
        assert d["competitor"] == "OpenAI"
        assert d["comparator_entity"] == "Meta"

    def test_new_arms_present(self):
        arms = _m946_data()["new_arms"]
        assert len(arms) == 2
        a1, a2 = arms
        assert a1["arm"] == "A1"
        assert a1["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert a1["wired_original_attested"] is True
        assert "CVE-2026-100754" in a1["peg"]
        assert "insanely trivial" in a1["evidence"]
        assert "Shane Bauer" in a1["evidence"]
        assert a2["arm"] == "A2"
        assert a2["tone_MANUAL_ILLUSTRATIVE"] == -0.20
        assert "fancy pinky-swear" in a2["evidence"]

    def test_meta_arms_carried(self):
        arms = _m946_data()["carried_meta_arms"]
        assert any("-0.30" in a for a in arms)
        assert any("-0.45" in a for a in arms)
        assert any("-0.75" in a for a in arms)

    def test_scorer_delta(self):
        s = _m946_data()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores"] == [-0.40, -0.20]
        assert s["target_avg"] == -0.30
        assert s["peer_scores"] == [-0.30, -0.45]
        assert s["peer_avg"] == -0.375
        assert s["delta"] == 0.075
        assert "-0.10" in s["delta_direction"]
        assert "NOT run" in str(s["scorer"])
        assert s["is_significant"] is False
        assert s["no_analysis_json_update"] is True

    def test_financial_context_prediction(self):
        d = _m946_data()["financial_context"]
        assert "$1-5M/yr" in d["conde_nast_openai_deal"]
        assert d["prediction"] == "softer OpenAI coverage"
        assert "fails" in d["outcome"]

    def test_confounder_strength_ordering(self):
        c = _m946_data()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 1
        assert any("Excerpt-bounded" in x for x in c["strong"])
        assert any("Peg-register" in x for x in c["strong"])

    def test_counter_evidence_present(self):
        ce = _m946_data()["counter_evidence"]
        assert len(ce) == 4
        assert any("m916" in x for x in ce)
        assert any("WSJ-original" in x for x in ce)
        assert any("+0.075" in x for x in ce)
        assert any("m889" in x for x in ce)

    def test_research_method_records_search_sets(self):
        rm = _m946_data()["research_method"]
        assert "4 browser.search query sets" in rm
        assert "0 browser.open" in rm
        assert "no em dashes" in rm
        assert "REJECTED for this run" in rm

    def test_novelty_records_precommit_state(self):
        n = _m946_data()["novelty"]
        assert "zero test_type_a_1192 files on disk pre-commit" in n
        assert "no Type A #1192 in git log pre-commit" in n
        assert "max numeric mechanism_id 945 pre-commit" in n
        assert "zero-hit repo-wide pre-commit" in n
        assert "thirteenth" not in n  # sanity: no stray ordinals

    def test_open_empirical_test(self):
        oet = _m946_data()["open_empirical_test"]
        assert "First-hand open of the CVE piece" in oet
        assert "Oct-1 safety-researcher firings" in oet


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1192:
    def test_manual_illustrative_only(self):
        sd = _m946_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd

    def test_no_analysis_json_update(self):
        assert _m946_data()["no_analysis_json_update"] is True
        assert "analysis.json" not in _git("diff", "--name-only")

    def test_correlation_not_causation(self):
        assert _m946_data()["correlation_not_causation"] is True

    def test_is_falsification_member(self):
        # This run IS a member (ledger 46->47), unlike #1147's NOT.
        assert "falsification-family member" in _m946_data()["falsification_family"]
        assert _m946_data()["falsification_ledger"] == "47"

    def test_artifact_not_grade(self):
        assert "artifact_grade false" in _m946_data()["statistical_discipline"]

# ---------------------------------------------------------------------------
# 6. Falsification ledger (46->47 this run)
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1192:
    def test_forty_sixth_intact_in_verge(self):
        text = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert text.count(_T46) == 2

    def test_forty_seventh_landed_in_wired_m946(self):
        # The member-claim form this run lands: exactly 2 occurrences
        # (the #1127 designed pattern) inside the m946 block.
        text = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert text.count(_T47) == 2
        assert _T47 in _m946_data()["falsification_family"]
        assert _T47 in _m946_data()["novelty"]

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

    def test_directions_thirty_fifth_through_thirty_eighth_present(self):
        for needle in (_TW35, _TW36, _TW37, _TW38):
            assert _needle_hits_profiles(needle) != [], needle

    def test_thirty_ninth_direction_absent(self):
        assert _needle_hits_profiles(_TW39) == []

    def test_ledger_note_advances_to_47(self):
        assert _m946_data()["falsification_ledger"] == "47"


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1191's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1192:
    def test_e1191_max_945_pin_trips_by_design(self):
        # #1191 pinned max numeric mechanism_id 945; this run lands
        # 946, so the pin fails BY DESIGN. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 946

    def test_e1191_zero_946_numeric_pin_trips_by_design(self):
        # The numeric field form mechanism_id: 946 now exists in
        # profiles/wired.yaml. Documented, not repaired.
        assert _repo_grep_numeric_mechanism_id(946) != []

    def test_e1191_zero_946_underscore_pin_stays_green(self):
        # This run lands no underscore-form nine-four-six literal in
        # profiles/ or tests/ (needles are format-built). Stays green.
        assert _repo_grep_underscore_mechanism(946) == []

    def test_e1191_zero_946_dash_pin_stays_green(self):
        assert _repo_grep_dash_mechanism(946) == []

    def test_e1191_forty_seventh_absence_pin_trips_by_design(self):
        # #1191 pinned the forty-seventh member-claim form absent;
        # this run lands it (2 occurrences, m946). Documented, not
        # repaired.
        assert _needle_hits_profiles(_T47) != []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards for #1193)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1192:
    def test_forward_max_946(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_forward_zero_947_all_forms(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_forward_no_type_b_1193_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type B #1193")
        assert log.strip() == ""

    def test_forward_no_forty_eighth_member(self):
        assert _needle_hits_profiles(_T48) == []

    def test_forward_directions_state(self):
        for needle in (_TW35, _TW36, _TW37, _TW38):
            assert _needle_hits_profiles(needle) != [], needle
        assert _needle_hits_profiles(_TW39) == []


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1190-launched suite; checked only per #795)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1192:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_this_run_does_not_touch_suite(self):
        # No Type A #1192 / m946 markers in the suite log; this run
        # checks only. The verdict belongs to #1195 per #795.
        text = _read(SUITE_LOG)
        assert "1192" not in text
        assert "m946" not in text

    def test_suite_verdict_belongs_to_1195(self):
        # The #1190-launched suite's verdict is claimed by the next
        # Type D run (#1195) per #795, never by this run.
        assert "type_d_1190" in SUITE_LOG


# ---------------------------------------------------------------------------
# 10. Doc-sync (deselected pre-commit per #719; green post-doc-sync)
# ---------------------------------------------------------------------------
class TestTypeADocSync1192:
    def test_readme_test_count(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d |" % README_TEST_COUNT in text

    def test_readme_file_count(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_constants_match_post_sync_state(self):
        # Post-first-run patch per #719: constants equal the true
        # collected count and the synced file count.
        assert README_TEST_COUNT == 63687 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1517


# Patched post-first-run per #719 with the true collected count.
COLLECTED_NEW_TESTS = 65


# ---------------------------------------------------------------------------
# 11. Iteration log (deselected pre-commit; green post-doc-sync)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1192:
    def test_1192_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1192 Type A:" in text

    def test_1192_entry_registers_hashes(self):
        # Post-log-hash followup per #721: the entry names the main,
        # anchor, and doc-sync commits.
        text = _read(LOG_PATH)
        entry_start = text.index("## #1192 Type A:")
        entry = text[entry_start : entry_start + 12000]
        assert "Main commit" in entry
        assert "Anchor followup" in entry
        assert "Doc-sync" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1192:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped per the #1147 convention: the working tree
        # carries pre-existing in-flight uncommitted changes (#899
        # nytimes.yaml m771 hunk, #938 test file anchor edit, #900
        # untracked test file, #1012 test-file working-tree edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files (profiles/wired.yaml m946 hunk + the new test
        # file).
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
            assert "m946" not in diff, path
            assert "Type A #1192" not in diff, path


# ---------------------------------------------------------------------------
# 13. ASCII discipline (no em dashes in the new files)
# ---------------------------------------------------------------------------
class TestAsciiDiscipline1192:
    def test_no_em_dash_in_own_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_no_em_dash_in_m946_block(self):
        text = _read(os.path.join(REPO_ROOT, M946_HOME))
        start = text.index(M946_KEY + ":")
        block = text[start : start + 20000]
        assert "\u2014" not in block
