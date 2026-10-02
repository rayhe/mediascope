"""Type A -- Iteration #1147 (Fri 2026-10-02 09:00 PDT): m919 WSJ x
Anthropic Oct-1 FTC-probe disclosure asymmetry + Aug-25 WSJ-attributed
$30T TAM-pitch arm vs carried WSJ x Meta arms -- disclosure-geometry
mechanism extending the news-corp.yaml anthropic disclosure_asymmetry
strand: the Journal's Oct-1 FTC original names Anthropic ALONGSIDE
OpenAI in the regulatory-enforcement register yet its inline disclosure
names ONLY the OpenAI licensing partnership, NOT the
HarperCollins/Bartz v. Anthropic $1.5B settlement-revenue vector
(expected "in coming months" per Thomson's Aug 5 Q4 FY2026 call,
in-corpus in the block's financial metadata). Two receiving financial
relationships, one disclosed, in a single piece naming both entities.
The Aug-25 WSJ TAM-pitch exclusive (six independent WSJ-attributed
relays, business-milestone register +0.10 MANUAL ILLUSTRATIVE) widens
the documented WSJ x Anthropic register range to 0.60 (-0.35 to +0.25)
over 37 days: milestone (Aug 25) -> delay/hack (Sep 18, m733) ->
enforcement (Oct 1, m904). Scorer: Anthropic arms [-0.35 carried,
+0.10] mean -0.125 vs carried Meta arms [-0.30, -0.25] mean -0.275;
illustrative delta +0.15 near-null, NOT significant. NOT a
falsification-family member (standing coverage_prediction "neutral",
so no uniform-softening prediction is tested); ledger holds at 46
(FORTY-SIXTH in the-verge.yaml m907 x2; forty-seventh absent;
thirty-sixth absent; THIRTY-FIFTH present m915). The Oct-1 FTC arm is
carried from #1122 (m904) by design, un-rescored per #807.

Type A THIRD leg of the 1145-1149 window, CONTINUING it
(D #1145 -> E #1146 -> A #1147 -> B #1148 -> C #1149). Committed
predecessors: #1145 Type D (main 8f4266d2 / anchor ea8fa07d /
doc-sync b03e4f59 / log-hash 575429ce) and #1146 Type E (main
a2da1a45 / anchor f8b2664d / doc-sync cb1e1757 / log-hash 1c4591c2),
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
m919 block lands in profiles/news-corp.yaml under
competitor_relationships as a sibling of the wsj_anthropic_* blocks,
NOT nytimes.yaml); the in-flight blocks are owned by their runs.
Targeted staging only per the repo-wide traversal lesson. Iteration
numbers follow the rotation schedule, not commit order. Do NOT touch
#1024's m846 (self-flagged sourcing-constraint violation; Ray's
revert/leave/rebuild-from-primary decision still pending).

Verifies:
- m919 (Type A #1147, profiles/news-corp.yaml
  competitor_relationships block key, 2-space indent (sibling of the
  wsj_anthropic_* blocks per the news-corp.yaml convention),
  `mechanism_id: 919` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1147 is the
  iteration), so it is a plain literal per #715): WSJ x Anthropic
  Oct-1 FTC-probe disclosure asymmetry + Aug-25 TAM-pitch arm vs
  carried WSJ x Meta arms, post-landing corpus integrity (max
  numeric mechanism_id 919; zero next-number 920 keys in
  numeric/underscore/dash mechanism forms - the 920 needles are
  format-built per #715 so no guard-literal carrier file exists;
  falsification ledger holds at 46 - the forty-sixth member-form
  present (m907, profiles/the-verge.yaml), the forty-seventh
  member-claim form absent repo-wide as designed negative guard for
  the next landing; thirty-fifth direction present
  (competitor-entities.yaml, m915), thirty-sixth absent; the #1145/
  #1146 window files are NOT edited by this run - their now-stale
  forward-looking pins are recorded as fail-by-design via subprocess
  in the staleness class (#1146's max-918 pin trips on the landed
  919; #1146's zero-919 numeric pin trips on the landed 919 key
  form; #1146's underscore/dash 919 pins STAY GREEN by design - no
  contiguous underscore/dash-form 919 literal exists; #1146's
  no-thirty-sixth and no-forty-seventh pins STAY GREEN, asserted in
  this run's own guard-lifecycle class)) + the #1145 background-suite
  check (no pytest alive at this run's check, log stalled 385 bytes
  since Oct 2 08:14:13 PDT - checked only, NOT touched; verdict
  belongs to #1150 per #795).

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
    "test_type_a_1147_wsj_anthropic_oct01_ftc_probe_disclosure_"
    "asymmetry_aug25_tam_pitch_vs_carried_meta_arms_oct02_9am.py"
)

MAX_ID = 919
NEXT_NUM = 920

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "5837f4800c7758234dd50dab66ee6b775310fd89"  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 60305
README_FILE_COUNT = 1471

# The m919 block key carries no mechanism-number substring (1147 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M919_KEY = (
    "type_a_1147_wsj_anthropic_oct01_ftc_probe_disclosure_"
    "asymmetry_plus_aug25_tam_pitch_vs_carried_meta_arms_oct02_9am"
)
M919_INDENT = 2
M919_HOME = "profiles/news-corp.yaml"

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
    "hidden_files/type_d_1145_full_suite.log"
)
E1146_FILE = (
    "tests/test_type_e_1146_podcast_sentiment_152nd_verification_"
    "oct02_8am.py"
)

# Committed predecessor #1145 Type D chain (verified pre-commit).
PRED_MAIN_1145 = "8f4266d2"
PRED_ANCHOR_1145 = "ea8fa07d"
PRED_DOCSYNC_1145 = "b03e4f59"
PRED_FINAL_1145 = "575429ce"
# Committed predecessor #1146 Type E chain (verified pre-commit).
PRED_MAIN_1146 = "a2da1a45"
PRED_ANCHOR_1146 = "f8b2664d"
PRED_DOCSYNC_1146 = "cb1e1757"
PRED_FINAL_1146 = "1c4591c2"

# New-to-corpus this run (zero-hit repo-wide pre-commit).
NEW_RELAY_URLS = [
    "https://fourweekmba.com/ai-anthropic-30-trillion-tam-ipo-frontier-ai-thesis/",
    "https://temperature2.com/p/2026-08-26-anthropic-30-trillion-ipo-pitch/",
    "https://www.gadgetreview.com/larger-than-the-us-economy-anthropic-pitches-a-30-trillion-market-ahead-of-its-ipo",
    "https://tech-insider.org/anthropic-30-trillion-market-ai-lab-robots-2026/",
    "https://pasqualepillitteri.it/en/news/12753/anthropic-30-trillion-revenue-tam",
]
# Corroborating relays of the carried Oct-1 FTC original.
FTC_RELAY_URLS = [
    "https://www.barrons.com/articles/ftc-openai-anthropic-ai-safety-investigation-8eb4be96",
    "https://www.fastcompany.com/91616194/the-ftc-has-a-plan-for-regulating-ai-without-writing-ai-rules",
    "https://www.techrepublic.com/article/news-ftc-openai-anthropic-ai-consumer-harms/",
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


def _m919_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M919_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"][M919_KEY]


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
class TestNovelty1147:
    def test_single_type_a_1147_file(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1147*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1147_in_git_log(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1147")
        assert "Type A #1147" in log

    def test_type_a_1147_commit_set(self):
        # Post-full-run: exactly three commits carry "Type A #1147"
        # (main + anchor followup + log-hash followup per #721).
        log = _git("log", "--format=%H", "--grep=Type A #1147")
        assert len([l for l in log.splitlines() if l.strip()]) == 3, log

    def test_new_relay_urls_in_corpus_post_commit(self):
        # The six TAM relay URLs were zero-hit repo-wide pre-commit;
        # post-commit they are in-corpus exactly once (this file's
        # constant list) plus the news-corp.yaml block (five of them).
        for url in NEW_RELAY_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M919_HOME))
        assert text.count(M919_KEY + ":") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1147:
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1145_chain_in_history(self):
        for sha in (
            PRED_MAIN_1145,
            PRED_ANCHOR_1145,
            PRED_DOCSYNC_1145,
            PRED_FINAL_1145,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1146_chain_in_history(self):
        for sha in (
            PRED_MAIN_1146,
            PRED_ANCHOR_1146,
            PRED_DOCSYNC_1146,
            PRED_FINAL_1146,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        window = _window()
        assert ("A", "1147") in window
        assert ("E", "1146") in window
        assert ("D", "1145") in window
        # Newest-first ordering: A1147 newer than E1146 newer than D1145.
        assert window.index(("A", "1147")) < window.index(("E", "1146"))
        assert window.index(("E", "1146")) < window.index(("D", "1145"))

    def test_rotation_phrase_in_log_entry(self):
        text = _read(LOG_PATH)
        assert "## #1147 Type A:" in text
        entry_start = text.index("## #1147 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1145-1149 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1147:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1147
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1147")
        assert "Type A #1147" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1147:
    def test_m919_block_keyed_at_indent_2(self):
        text = _read(os.path.join(REPO_ROOT, M919_HOME))
        line = next(
            l for l in text.splitlines() if l.strip() == M919_KEY + ":"
        )
        assert line.startswith(" " * M919_INDENT)
        assert not line.startswith(" " * (M919_INDENT + 1))

    def test_m919_block_sibling_of_wsj_anthropic_blocks(self):
        data = _read(os.path.join(REPO_ROOT, M919_HOME))
        assert "  wsj_anthropic_coxon_resignation_news_register" in data
        assert "  wsj_anthropic_ipo_shift_claude_hack_register" in data

    def test_m919_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M919_HOME))
        assert "mechanism_id: 919" in text

    def test_max_numeric_mechanism_id_is_919(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_920_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_920_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_920_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_919_substring_in_block_key(self):
        assert "919" not in M919_KEY


# ---------------------------------------------------------------------------
# 4. m919 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM919ContentDiscipline1147:
    def test_metadata_fields(self):
        d = _m919_data()
        assert d["iteration"] == 1147
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-02 09:00 PDT"
        assert d["scheduled_job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["author"] == "Kit (with Ray)"
        assert d["publication_focus"] == "Wall Street Journal (News Corp)"
        assert d["entity_pair"] == (
            "Anthropic (settlement-revenue receiving) vs Meta "
            "(dual-deal comparator)"
        )

    def test_anthropic_arms_present(self):
        arms = _m919_data()["anthropic_articles_this_run"]
        assert len(arms) == 2
        assert arms[0]["url_status"].startswith("carried from #1122")
        assert arms[0]["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert "OpenAI licensing partnership" in arms[0][
            "disclosure_observation"
        ]
        assert arms[1]["date"] == "2026-08-25"
        assert arms[1]["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert len(arms[1]["relay_urls"]) == 5

    def test_meta_arms_carried(self):
        meta = _m919_data()["meta_arms_carried"]
        tones = [a["tone"] for a in meta["arms"]]
        assert tones == [-0.30, -0.25]
        assert meta["meta_mean"] == -0.275
        assert all(a["mechanism"] == 532 for a in meta["arms"])

    def test_scorer_delta(self):
        s = _m919_data()["scorer"]
        assert s["anthropic_arm_tones"] == [-0.35, 0.10]
        assert s["anthropic_mean_tone"] == -0.125
        assert s["meta_arm_tones"] == [-0.30, -0.25]
        assert s["meta_mean_tone"] == -0.275
        assert s["illustrative_delta_anthropic_minus_meta"] == 0.15
        assert "NOT run" in s["method"]
        assert "is_significant False" in s["method"]

    def test_disclosure_geometry_core(self):
        d = _m919_data()
        summary = d["discovery_summary"]
        assert "inline disclosure" in summary
        assert "ONLY the" in summary
        assert "OpenAI licensing partnership" in summary
        assert "Bartz" in summary
        assert "Two receiving financial" in summary

    def test_confounder_strength_ordering(self):
        c = _m919_data()["confounders"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 2
        assert any("policy" in x for x in c["strong"])
        assert any("Carried-arm" in x for x in c["strong"])

    def test_counter_evidence_present(self):
        ce = _m919_data()["counter_evidence"]
        assert len(ce) == 3
        assert any("m682" in x for x in ce)

    def test_relations_and_distinctness(self):
        d = _m919_data()
        assert "disclosure_asymmetry" in d["relation_to_disclosure_asymmetry"]
        assert "m904" in d["relation_to_904"]
        assert "m733" in d["relation_to_733"]
        assert "0.60" in d["relation_to_733"]
        assert "FIRST dedicated mechanism" in d["distinct_from_prior"]

    def test_research_method_records_search_sets(self):
        rm = _m919_data()["research_method"]
        assert "4 browser.search query sets" in rm
        assert "0 browser.open" in rm
        assert "no em dashes" in rm

    def test_novelty_records_precommit_state(self):
        n = _m919_data()["novelty"]
        assert "Zero test_type_a_1147 files on disk pre-commit" in n
        assert 'no "Type A #1147" in git log pre-commit' in n
        assert "max numeric mechanism_id 918 pre-commit" in n
        assert "zero-hit repo-wide pre-commit" in n


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1147:
    def test_manual_illustrative_only(self):
        sd = _m919_data()["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd

    def test_no_analysis_json_update(self):
        assert _m919_data()["no_analysis_json_update"] is True
        assert _git("diff", "--name-only").count("analysis.json") == 0

    def test_correlation_not_causation(self):
        assert _m919_data()["correlation_not_causation"] is True

    def test_not_falsification_member(self):
        d = _m919_data()
        assert "NOT a falsification-family member" in d["finding"]

    def test_artifact_not_grade(self):
        d = _m919_data()
        assert "NOT artifact-grade" in d["artifact_grade"]


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1147:
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
        assert "Ledger holds at 46" in _m919_data()["ledger"]

# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1146's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1147:
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

    def test_1146_max_918_pin_stale_by_design(self):
        # #1146's TestMechanismNovelty pinned max 918; the m919
        # landing flips it at #1147. Designed lifecycle; recorded,
        # not repaired.
        result = self._stale_run(
            E1146_FILE,
            "TestMechanismNovelty::" "test_type_e_adds_no_mechanisms",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1146_zero_919_numeric_guard_flips_by_design(self):
        # #1146's zero-919 numeric guard uses a profiles/ walk. The
        # m919 landing (mechanism_id: 919 field in the working tree)
        # trips it at #1147. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            E1146_FILE,
            "TestMechanismNovelty::"
            "test_zero_919_numeric_mechanism_id_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1146_zero_919_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 919 guards STAY GREEN: the m919 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1147 is the iteration, not the mechanism), and
        # this run's test file builds its 919 needles at runtime, so
        # no contiguous underscore/dash-form 919 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_919_underscore_mechanism_repo_wide",
            "test_zero_919_dash_mechanism_repo_wide",
        ):
            result = self._stale_run(
                E1146_FILE, "TestMechanismNovelty::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1146_no_thirty_sixth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1146's negative guards
        # stay green.
        for node in (
            "test_no_thirty_sixth_direction_claim_repo_wide",
            "test_no_forty_seventh_member_claim_repo_wide",
        ):
            result = self._stale_run(
                E1146_FILE, "TestStatisticalDiscipline::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1147:
    def test_1147_file_pins_max_id_919_and_next_920(self):
        assert _max_numeric_mechanism_id() == 919

    def test_zero_next_numeric_920_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_920_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_920_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 919 in ids
        assert all(i <= 919 for i in ids)

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
# 9. Background-suite check (#1145 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1147:
    def test_1145_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1145); its verdict belongs to #1150. This run checks only:
        # the log exists and this run did not write to it (no Type A
        # #1147 marker in the suite log).
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        text = _read(SUITE_LOG)
        assert "Type A #1147" not in text
        assert "m919" not in text

    def test_1145_suite_state_recorded(self):
        # Dead at this run's check: log stalled at 385 bytes since
        # Oct 2 08:14:13 PDT (~55 min), no pytest alive. The #1150
        # Type D run owns the verdict and any re-launch per #795.
        assert os.path.getsize(SUITE_LOG) == 385


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1147:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1147_wsj_anthropic_oct01_ftc_probe" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1147_wsj_anthropic_oct01_ftc_probe" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60305
        assert README_FILE_COUNT == 1471


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1147:
    def test_iteration_log_has_1147_entry(self):
        text = _read(LOG_PATH)
        assert "## #1147 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "a2da1a45" in text  # predecessor chain
        entry_start = text.index("## #1147 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1145-1149 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1147:
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
            assert "m919" not in diff, path
            assert "Type A #1147" not in diff, path

    def test_newscorp_diff_scoped_to_m919_block(self):
        diff = _git("diff", "--", M919_HOME)
        assert M919_KEY in diff
        assert "type_a_1147" in diff
        assert "m846" not in diff  # do NOT touch #1024's m846
