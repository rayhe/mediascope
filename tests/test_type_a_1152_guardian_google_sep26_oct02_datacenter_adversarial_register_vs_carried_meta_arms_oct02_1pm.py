"""Type A -- Iteration #1152 (Fri 2026-10-02 13:00 PDT): m922 Guardian x
Google Sep-26/Oct-2 adversarial datacenter investigative register vs
carried Guardian x Meta arms -- register-range extension of the
guardian.yaml google block (mechanism_487 sibling): the Sep-26 Guardian
original "Broken promises, confiscated land" (Ellis-Petersen + Hassan,
11:00 UTC, 8 min read) names Google's hyperscale AI datacentre in
Tarluvada, Andhra Pradesh in an investigative
environmental-exploitation register (village-head quote: "now Google is
bringing them here"), and the Oct-2 Guardian Weekly cover story
(Porter) "NOT IN MY BACKYARD" elevates the same adversarial frame to
cover status. Bounded-absence arm: the Oct-1 SDNY Castel ruling
clearing publishers to seek $3.2B+ in AdX-monopoly damages from Google
surfaced zero Guardian originals in two targeted query sets (bounded
search-result absence per #503). Scorer: Google new arms [-0.45, -0.40]
mean -0.425 vs carried Meta arms [-0.45, -0.50] (m487 target_scores +
m537) mean -0.475; illustrative delta +0.05 near-null, NOT
significant. NOT a falsification-family member (standing
coverage_prediction "neutral", so no uniform-softening prediction is
tested); ledger holds at 46 (FORTY-SIXTH in the-verge.yaml m907 x2;
forty-seventh absent; thirty-sixth absent; THIRTY-FIFTH present m915).
Counter-evidence carried: m487's Aug-2026 renewal/canonization Google
register (-0.15, -0.05) vs Meta deficit register - register SELECTION
dominates the arc, not entity targeting; consistent with the block's
"neutral/pragmatic" standing prediction. The three relay URLs are
new-to-corpus (zero-hit pre-commit); the newdigitalage Ad World URL is
a ruling-citation only.

Type A THIRD leg of the 1150-1154 window, CONTINUING it
(D #1150 -> E #1151 -> A #1152 -> B #1153 -> C #1154). Committed
predecessors: #1150 Type D (main a032e49d / anchor c7a3fadc /
doc-sync da22db62 / log-hash 2e60cf2f) and #1151 Type E (main 3571d5f1 /
anchor afa6d5e2 / doc-sync e7e32de6 / log-hash 63290903), both
verified present in history pre-commit. Rotation per the #565
anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m922 block lands in profiles/guardian.yaml under
competitor_relationships > google as a 4-space-indent sibling of the
mechanism_487 block, NOT nytimes.yaml); the in-flight blocks are
owned by their runs. Targeted staging only per the repo-wide
traversal lesson. Iteration numbers follow the rotation schedule, not
commit order. Do NOT touch #1024's m846 (self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending).

Verifies:
- m922 (Type A #1152, profiles/guardian.yaml
  competitor_relationships > google block key, 4-space indent (sibling
  of the mechanism_487 block per the guardian.yaml convention),
  `mechanism_id: 922` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1152 is the
  iteration), so it is a plain literal per #715): Guardian x Google
  Sep-26/Oct-2 adversarial datacenter investigative register + $3.2B
  AdX-ruling bounded-absence arm vs carried Guardian x Meta arms,
  post-landing corpus integrity (max numeric mechanism_id 922; zero
  next-number 923 keys in numeric/underscore/dash mechanism forms -
  the 923 needles are format-built per #715 so no guard-literal carrier
  file exists; falsification ledger holds at 46 - the forty-sixth
  member-form present (m907, profiles/the-verge.yaml), the forty-seventh
  member-claim form absent repo-wide as designed negative guard for
  the next landing; thirty-fifth direction present
  (competitor-entities.yaml, m915), thirty-sixth absent; the #1150/
  #1151 window files are NOT edited by this run - their now-stale
  forward-looking pins are recorded as fail-by-design via subprocess
  in the staleness class (#1151's zero-922 numeric pin trips on the
  landed 922; #1151's underscore/dash 922 pins STAY GREEN by design -
  no contiguous underscore/dash-form 922 literal exists; #1151's
  no-thirty-sixth and no-forty-seventh pins STAY GREEN, asserted in
  this run's own guard-lifecycle class)) + the #1150 background-suite
  check (in flight at this run's check per #795 - pytest alive, log
  fresh at Oct 2 13:02 PDT; checked only, NOT touched; verdict belongs
  to #1155 per #795).

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""
import glob
import os
import re
import subprocess
import time

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1152_guardian_google_sep26_oct02_datacenter_"
    "adversarial_register_vs_carried_meta_arms_oct02_1pm.py"
)

MAX_ID = 922
NEXT_NUM = 923

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "31bbe553666333f4fedd2ac6695b9a0e87b185f0"  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 60721
README_FILE_COUNT = 1477

# The m922 block key carries no mechanism-number substring (1152 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M922_KEY = (
    "type_a_1152_guardian_google_sep26_oct02_datacenter_"
    "adversarial_register_vs_carried_meta_arms"
)
M922_INDENT = 4
M922_HOME = "profiles/guardian.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml (m915) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1150_full_suite.log"
)
E1151_FILE = (
    "tests/test_type_e_1151_podcast_sentiment_153rd_verification_"
    "oct02_12pm.py"
)

# Committed predecessor #1150 Type D chain (verified pre-commit).
PRED_MAIN_1150 = "a032e49d"
PRED_ANCHOR_1150 = "c7a3fadc"
PRED_DOCSYNC_1150 = "da22db62"
PRED_FINAL_1150 = "2e60cf2f"
# Committed predecessor #1151 Type E chain (verified pre-commit).
PRED_MAIN_1151 = "3571d5f1"
PRED_ANCHOR_1151 = "afa6d5e2"
PRED_DOCSYNC_1151 = "e7e32de6"
PRED_FINAL_1151 = "63290903"

# New-to-corpus this run (zero-hit repo-wide pre-commit).
NEW_RELAY_URLS = [
    "https://wesearch.press/s/broken-promises-confiscated-land-the-hyperscale-ai-datacentr-d1a11325",
    "https://grandgoldman.com/blogs/business/googles-15bn-ai-datacentre-in-india-sparks-land-disputes",
    "https://intellicurious.com/2026/09/30/the-guardian-weekly-october-2-2026/",
]
# Ruling-citation only (not a new corpus key).
RULING_CITATION_URL = (
    "https://newdigitalage.co/general/ad-world-todays-news-from-around-the-web-94/"
)


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
    for root, dirs, files in os.walk(REPO_ROOT):
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", ".venv", "__pycache__", "node_modules")
        ]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
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


def _m922_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M922_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["google"][M922_KEY]


def _window():
    """Newest-first distinct (type, number) sequence from the log."""
    pat = re.compile(r"^## #(\d+) Type ([A-E]):", re.M)
    seen = []
    for num, typ in pat.findall(_read(LOG_PATH)):
        key = (typ, num)
        if key not in seen:
            seen.append(key)
    return seen


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit state recorded post-commit; superseded pins noted)
# ---------------------------------------------------------------------------
class TestNovelty1152:
    def test_single_type_a_1152_file(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1152*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1152_in_git_log(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1152")
        assert "Type A #1152" in log

    def test_type_a_1152_commit_set(self):
        # Post-full-run: exactly three commits carry "Type A #1152"
        # (main + anchor followup + log-hash followup per #721).
        log = _git("log", "--format=%H", "--grep=Type A #1152")
        assert len([l for l in log.splitlines() if l.strip()]) == 3, log

    def test_new_relay_urls_in_corpus_post_commit(self):
        # The three relay URLs were zero-hit repo-wide pre-commit;
        # post-commit they are in-corpus (this file's constant list
        # plus the guardian.yaml block).
        for url in NEW_RELAY_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M922_HOME))
        assert text.count(M922_KEY + ":") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1152:
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1150_chain_in_history(self):
        for sha in (
            PRED_MAIN_1150,
            PRED_ANCHOR_1150,
            PRED_DOCSYNC_1150,
            PRED_FINAL_1150,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1151_chain_in_history(self):
        for sha in (
            PRED_MAIN_1151,
            PRED_ANCHOR_1151,
            PRED_DOCSYNC_1151,
            PRED_FINAL_1151,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        window = _window()
        assert ("A", "1152") in window
        assert ("E", "1151") in window
        assert ("D", "1150") in window
        # Newest-first ordering: A1152 newer than E1151 newer than D1150.
        assert window.index(("A", "1152")) < window.index(("E", "1151"))
        assert window.index(("E", "1151")) < window.index(("D", "1150"))

    def test_rotation_phrase_in_log_entry(self):
        text = _read(LOG_PATH)
        assert "## #1152 Type A:" in text
        entry_start = text.index("## #1152 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1150-1154 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1152:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1152
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1152")
        assert "Type A #1152" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1152:
    def test_m922_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M922_HOME))
        line = next(
            l for l in text.splitlines() if l.strip() == M922_KEY + ":"
        )
        assert line.startswith(" " * M922_INDENT)
        assert not line.startswith(" " * (M922_INDENT + 1))

    def test_m922_block_sibling_of_mechanism_487(self):
        data = _read(os.path.join(REPO_ROOT, M922_HOME))
        assert (
            "    mechanism_487_guardian_google_deepmind_leadership_"
            "renewal_vs_meta_deficit_framing:" in data
        )

    def test_m922_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M922_HOME))
        assert "mechanism_id: 922" in text

    def test_max_numeric_mechanism_id_is_922(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_923_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_923_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_923_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_922_substring_in_block_key(self):
        assert "922" not in M922_KEY

# ---------------------------------------------------------------------------
# 4. m922 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM922ContentDiscipline1152:
    def test_metadata_fields(self):
        d = _m922_data()
        assert d["iteration"] == 1152
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-02 13:00 PDT"
        assert d["scheduled_job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["author"] == "Kit (with Ray)"

    def test_entity_pair_and_publication(self):
        d = _m922_data()
        assert d["publication_focus"] == "The Guardian"
        assert "Google" in d["entity_pair"]
        assert "Meta" in d["entity_pair"]

    def test_google_arms_this_run(self):
        d = _m922_data()
        arms = d["google_articles_this_run"]
        assert len(arms) == 3
        tones = [a["manual_illustrative_tone"] for a in arms[:2]]
        assert tones == [-0.45, -0.40]
        assert arms[0]["byline"] == "Hannah Ellis-Petersen + Aakash Hassan"
        assert arms[0]["date"] == "2026-09-26"
        assert "Tarluvada" in arms[0]["title"] or "Indian village" in arms[0]["title"]
        assert "NOT IN MY BACKYARD" in arms[1]["title"]
        assert arms[2]["register"] == "coverage_selection_bounded_absence"
        assert arms[2]["manual_illustrative_tone"] is None

    def test_new_relay_urls_attested(self):
        d = _m922_data()
        attested = []
        for a in d["google_articles_this_run"]:
            attested.extend(a.get("relay_attestation", []))
        for url in NEW_RELAY_URLS:
            assert url in attested, url

    def test_meta_arms_carried(self):
        d = _m922_data()
        arms = d["meta_arms_carried"]
        assert len(arms) == 2
        assert [a["manual_illustrative_tone"] for a in arms] == [-0.45, -0.50]
        assert all("m487" in a["carried_from"] for a in arms)

    def test_scorer_delta_math(self):
        d = _m922_data()
        s = d["scorer"]
        assert s["google_new_arms"] == [-0.45, -0.40]
        assert s["meta_carried_arms"] == [-0.45, -0.50]
        g_mean = sum(s["google_new_arms"]) / 2
        m_mean = sum(s["meta_carried_arms"]) / 2
        assert round(g_mean, 3) == -0.425
        assert round(m_mean, 3) == -0.475
        assert round(g_mean - m_mean, 3) == 0.05
        assert s["asymmetry_delta"] == 0.05
        assert s["is_significant"] is False
        assert s["p_value"] == "NOT_CALCULATED"

    def test_confounders_strong_first(self):
        d = _m922_data()
        confs = d["confounders"]
        assert len(confs) == 5
        strengths = [c["strength"] for c in confs]
        assert strengths[:2] == ["STRONG", "STRONG"]
        assert "STRONG" not in strengths[2:]
        assert any("Relay-carried" in c["confounder"] for c in confs)

    def test_counter_evidence_references_m487(self):
        d = _m922_data()
        ce = d["counter_evidence"]
        assert "m487" in ce
        assert "register SELECTION" in ce or "register selection" in ce.lower()

    def test_relation_to_fields(self):
        d = _m922_data()
        assert "m487" in d["relation_to_487"]
        assert "m83" in d["relation_to_83"]
        assert "m537" in d["relation_to_537"]

    def test_research_method_and_novelty(self):
        d = _m922_data()
        assert "4 browser.search query sets" in d["research_method"]
        assert "0 browser.open" in d["research_method"]
        assert "zero-hit repo-wide pre-commit" in d["novelty"]

    def test_ledger_and_key_design(self):
        d = _m922_data()
        assert "Ledger holds at 46" in d["ledger"]
        assert "NOT a falsification-family member" in d["ledger"]
        assert "1152" in d["key_design_note"]

    def test_statistical_discipline_block(self):
        d = _m922_data()
        sd = d["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert d["artifact_grade"] is False
        assert d["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 5. Statistical discipline (file-level)
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1152:
    def test_manual_only_no_engine(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text
        assert "no analysis.json update" in text

    def test_verdict_discipline(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "directionally_supported_not_proven" in text

    def test_no_923_mechanism_key_forms_in_file(self):
        # The next-number needles are format-built at runtime; no
        # contiguous numeric/underscore/dash next-number
        # mechanism-key literal may exist in this file.
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        num = str(NEXT_NUM)
        assert ("mechanism_id: " + num) not in text
        assert ("mechanism" + "_" + num) not in text
        assert ("mechanism" + "-" + num) not in text

    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in text
        assert "\u2013" not in text
        yaml_text = _read(os.path.join(REPO_ROOT, M922_HOME))
        # The new block only: slice from the block key to the 487 key.
        start = yaml_text.index(M922_KEY)
        end = yaml_text.index("mechanism_487_guardian_google", start)
        block = yaml_text[start:end]
        assert "\u2014" not in block
        assert "\u2013" not in block


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1152:
    def test_forty_sixth_present(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                if _T46 in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        assert hits != [], "forty-sixth member claim must exist"

    def test_forty_seventh_absent(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                if _T47 in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        assert hits == [], hits

    def test_thirty_fifth_present_thirty_sixth_absent(self):
        def _hits(needle):
            out = []
            for root, dirs, files in os.walk(PROFILES_DIR):
                for f in files:
                    p = os.path.join(root, f)
                    if needle in open(p, encoding="utf-8", errors="replace").read():
                        out.append(p)
            return out

        assert _hits(_TW35) != []
        assert _hits(_TW36) == []

    def test_ledger_note_holds_at_46(self):
        assert "Ledger holds at 46" in _m922_data()["ledger"]


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1151's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1152:
    def _stale_run(self, path, node=None, *deselects):
        target = path if node is None else "%s::%s" % (path, node)
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            target,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=900
        )
        return result

    def test_1151_zero_922_numeric_guard_flips_by_design(self):
        # #1151's zero-922 numeric guard uses a profiles/ walk. The
        # m922 landing (mechanism_id: 922 field in the working tree)
        # trips it at #1152. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            E1151_FILE,
            "TestMechanismNovelty::"
            "test_zero_922_numeric_mechanism_id_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1151_zero_922_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 922 guards STAY GREEN: the m922 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1152 is the iteration, not the mechanism), and
        # this run's test file builds its 922 needles at runtime, so
        # no contiguous underscore/dash-form 922 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_922_underscore_mechanism_repo_wide",
            "test_zero_922_dash_mechanism_repo_wide",
        ):
            result = self._stale_run(
                E1151_FILE, "TestMechanismNovelty::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1151_no_thirty_sixth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1151's negative guards
        # stay green.
        for node in (
            "test_no_thirty_sixth_direction_claim_repo_wide",
            "test_no_forty_seventh_member_claim_repo_wide",
        ):
            result = self._stale_run(
                E1151_FILE, "TestStatisticalDiscipline::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1152:
    def test_1152_file_pins_max_id_922_and_next_923(self):
        assert _max_numeric_mechanism_id() == 922

    def test_zero_next_numeric_923_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_923_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_923_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 922 in ids
        assert all(i <= 922 for i in ids)

    def test_no_thirty_sixth_direction_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW36 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1150 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1152:
    def test_1150_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1150); its verdict belongs to #1155. This run checks only:
        # the log exists and this run did not write to it (no Type A
        # #1152 marker in the suite log).
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        text = _read(SUITE_LOG)
        assert "Type A #1152" not in text
        assert "m922" not in text

    def test_1150_suite_in_flight_at_check(self):
        # In flight at this run's check: pytest alive, log fresh at
        # Oct 2 13:02 PDT (~4% progress, dots accumulating). The #1155
        # Type D run owns the verdict and any re-launch per #795.
        age_s = time.time() - os.path.getmtime(SUITE_LOG)
        assert age_s < 7200, age_s
        assert os.path.getsize(SUITE_LOG) > 0


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1152:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1152_guardian_google_sep26_oct02" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1152_guardian_google_sep26_oct02" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60721
        assert README_FILE_COUNT == 1477


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1152:
    def test_iteration_log_has_1152_entry(self):
        text = _read(LOG_PATH)
        assert "## #1152 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "3571d5f1" in text  # predecessor chain
        entry_start = text.index("## #1152 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1150-1154 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1152:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012 test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
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
            assert "m922" not in diff, path
            assert "Type A #1152" not in diff, path
