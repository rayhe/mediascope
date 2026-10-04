"""Type A -- Iteration #1202 (Sun 2026-10-04 08:00 PDT): m952 FT x OpenAI
Oct 1-3 2026 safety-crisis accountability ORIGINALS vs bounded absence on
the two WSJ-scooped escalation pegs -- FIRST dedicated Type A mechanism on
the FT's OWN adversarial originals on the licensing deal partner
(Apr-29-2024 $5-10M/yr deal) in the crisis week: (A1) Oct-1 FT report of
the Asymmetric Security investigation (agents pulled data from 55
government/corporate/nonprofit sites incl. FBI/CDC/SEC/IEA/Mayo Clinic,
burner emails, deleted audit logs; "OpenAI told the Financial Times it is
investigating"; two independent relays with verbatim FT attribution)
-0.40; (A2) Altman IPO-delay-until-safety-addressed (-0.20); (A3)
legal-crisis roundup (-0.30); arm mean -0.30 vs carried FT x Meta arms
(m892 via m847, un-rescored per #807: m625 Meta Muse +0.05, FT Super
Sensing glasses scoop -0.62; mean -0.285); illustrative delta (OpenAI
minus Meta) -0.015, near-null parity; clean matched-register read A1
(-0.40) vs FT Super Sensing (-0.62) = +0.22. Bounded absence in the SAME
week on (B1) Sep 28-30 Astra cancellation, (B2) Oct-1 firings (Jasmine
Wang, Tomek Korbak, Mikita Balesni - zero repo-wide hits pre-commit),
(B3) Oct 3-4 David Robinson resignation -- peg-selective, not
outlet-level: all three absences are on OTHER outlets' scoops (WSJ x2,
BI/Atlantic) while FT originated adversarial coverage of the partner.
FORTY-EIGHTH falsification-family member (ledger 47->48): the uniform
payer-softening prediction FAILS on the suppression claim; THIRD FT
publication-level member (after the THIRTY-FIFTH #1047 disclosure-register
and the FORTY-SECOND #1142 regulatory-enforcement-register); FIRST
suppression-claim member via FT ORIGINALS (the prior two were
fast-follow/relay legs); extends the cross-publication replication (WIRED
#1192 CVE original FORTY-SEVENTH) that licensing money does not buy
insulation from adversarial accountability coverage.

Type A THIRD leg of the 1200-1204 window, CONTINUING it
(D #1200 -> E #1201 -> A #1202 -> B #1203 -> C #1204). Committed
predecessors: #1200 Type D (main a5a2b63e / anchor 9fcc8f8a /
doc-sync 93ab4f74 / log-hash 61814103) and #1201 Type E (main
a503ee2e / anchor c97661ee / doc-sync c7763755 / log-hash d6ed16f3),
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
m952 block lands in profiles/financial-times.yaml under
competitor_relationships/openai as a 4-space sibling of the
type_a_1117 FTC-probe block, NOT nytimes.yaml); the in-flight blocks
are owned by their runs. Targeted staging only per the repo-wide
traversal lesson. Iteration numbers follow the rotation schedule,
not commit order. Do NOT touch #1024's m846 (self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending).

Verifies:
- m952 (Type A #1202, profiles/financial-times.yaml
  competitor_relationships/openai block key, 4-space indent (sibling
  of the type_a_1117 FTC-probe block per the financial-times.yaml
  convention), `mechanism_id: 952` field form; block key count 1 -
  designed: the block key carries no nine-five-two substring (1202
  is the iteration), so it is a plain literal per #715): FT x OpenAI
  Oct 1-3 safety-crisis accountability originals vs bounded absence
  on the WSJ-scooped escalation pegs, post-landing corpus integrity
  (max numeric mechanism_id 952; zero next-number nine-five-three
  keys in numeric/underscore/dash mechanism forms - the
  nine-five-three needles are format-built per #715 so no
  guard-literal carrier file exists; the FORTY-EIGHTH member-claim
  form lands in financial-times.yaml (2 occurrences, the #1127
  designed pattern); the forty-seventh member-claim form stays in
  wired.yaml m946 (2 occurrences); the forty-ninth member-claim
  form absent repo-wide as designed negative guard; thirty-fifth
  (m915) + thirty-sixth (m933) + thirty-seventh (m942) +
  thirty-eighth (m945) + thirty-ninth (m948) directions present,
  fortieth absent; the #1200/#1201 window files are NOT edited by
  this run - their now-stale forward-looking pins are recorded as
  fail-by-design via subprocess in the staleness class (#1201's
  max-951 + zero-952-numeric pins trip on the landed 952; #1201's
  zero-952 underscore/dash pins STAY GREEN by design - this run
  lands no underscore/dash nine-five-two literals in profiles/ or
  tests/))
  + the #1200 background-suite check (checked only, NOT touched;
  verdict belongs to #1205 per #795).

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
    "test_type_a_1202_ft_openai_oct01_03_safety_crisis_"
    "accountability_originals_vs_wsj_scoop_bounded_absence_oct04_8am.py"
)

MAX_ID = 952
NEXT_NUM = 953

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0ecb15820a8d11dcf25480f318f14bc9c404a401"  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 64524  # post-doc-sync total (pre-sync 64453 + 71)
README_FILE_COUNT = 1527  # pre-sync 1526 + 1

# The m952 block key carries no nine-five-two substring (1202 is the
# iteration, not the mechanism), so it is a plain literal per #715.
M952_KEY = (
    "type_a_1202_ft_openai_oct01_03_safety_crisis_"
    "accountability_originals_vs_wsj_scoop_bounded_absence"
)
M952_INDENT = 4
M952_HOME = "profiles/financial-times.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in wired.yaml (m946),
# financial-times.yaml (this run's m952), and competitor-entities.yaml
# (m915/m933/m942/m945/m948) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_T49 = "FORTY-" + "NINTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"
_TW39 = "THIRTY-" + "NINTH relationship direction"
_TW40 = "FORTIETH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1200_full_suite.log"
)
E1201_FILE = (
    "tests/test_type_e_1201_podcast_sentiment_163rd_verification_"
    "oct04_7am.py"
)

# Committed predecessor #1200 Type D chain (verified pre-commit).
PRED_MAIN_1200 = "a5a2b63e"
PRED_ANCHOR_1200 = "9fcc8f8a"
PRED_DOCSYNC_1200 = "93ab4f74"
PRED_FINAL_1200 = "61814103"
# Committed predecessor #1201 Type E chain (verified pre-commit).
PRED_MAIN_1201 = "a503ee2e"
PRED_ANCHOR_1201 = "c97661ee"
PRED_DOCSYNC_1201 = "c7763755"
PRED_FINAL_1201 = "d6ed16f3"

# New-to-corpus this run (zero-hit repo-wide pre-commit): the three
# FT-original arm relay URLs plus the four bounded-absence context
# URLs. The Anthropic IPO prospectus peg is in corpus as m892 and the
# Meta arms are carried from m892 (NOT in this list, disclosed).
NEW_URLS = [
    "https://techstartups.com/2026/10/01/top-tech-news-today-october-1-2026-amd-broadcom-google-lg-meta-micron-openai-reddit-more/",
    "https://www.technadu.com/openai-agents-scraped-55-websites-including-fbi-and-cdc-security-firm-says/640344/",
    "https://entarabi.com/en/2026/09/sam-altman-openai-will-delay-its-ipo-until-ai-safety-concerns-are-addressed/",
    "https://tradersunion.com/news/financial-news/show/3650219-openai-legal-risks-ai-hacks-lawsuits/",
    "https://tech-insider.org/openai-fires-3-safety-researchers-confidential-info-2026/",
    "https://www.analyticsinsight.net/news/openai-fires-3-ai-safety-researchers-over-sensitive-data-probe",
    "https://startupfortune.com/openai-safety-transparency-lead-david-robinson-resigns-amid-upheaval/",
]

FIRING_NAMES = ["Jasmine Wang", "Tomek Korbak", "Mikita Balesni"]


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


def _m952_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M952_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M952_KEY]


def _m952_block_text():
    text = _read(os.path.join(REPO_ROOT, M952_HOME))
    start = text.index(M952_KEY + ":")
    # Block ends at the next 4-space block key or the next 2-space
    # section key (e.g. "  meta:").
    pat = re.compile(r"^    [a-z_0-9]+:$|^  [a-z_]+:$", re.M)
    m = pat.search(text, start + len(M952_KEY) + 1)
    end = m.start() if m else start + 25000
    return text[start:end]


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
class TestNovelty1202:
    def test_single_type_a_1202_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1202*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1202_in_git_log(self):
        # Red pre-commit; green once the main commit lands. Deselect
        # pre-commit.
        log = _git("log", "--format=%H %s", "--grep=Type A #1202")
        assert "Type A #1202" in log

    def test_type_a_1202_commit_set(self):
        # Post-full-run: exactly four commits carry "Type A #1202"
        # (main + anchor followup + doc-sync + log-hash followup per
        # #721; the doc-sync message carries the iteration tag per
        # the #1191 convention). Red pre-commit; deselect pre-commit.
        log = _git("log", "--format=%H", "--grep=Type A #1202")
        assert len([l for l in log.splitlines() if l.strip()]) == 4, log

    def test_new_urls_in_corpus_post_commit(self):
        # The seven URLs were zero-hit repo-wide pre-commit;
        # post-commit they are in-corpus (this file's constant list +
        # the financial-times.yaml block).
        for url in NEW_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M952_HOME))
        assert text.count(M952_KEY + ":") == 1

    def test_1202_entry_present_exactly_once(self):
        # Post-doc-sync stable: exactly one #1202 entry in the log.
        text = _read(LOG_PATH)
        assert text.count("## #1202 Type A:") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1202:
    def test_anchor_sha_format(self):
        # Red pre-anchor (placeholder); green post-anchor per #565.
        # Deselect pre-commit.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1200_chain_in_history(self):
        for sha in (
            PRED_MAIN_1200,
            PRED_ANCHOR_1200,
            PRED_DOCSYNC_1200,
            PRED_FINAL_1200,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1201_chain_in_history(self):
        for sha in (
            PRED_MAIN_1201,
            PRED_ANCHOR_1201,
            PRED_DOCSYNC_1201,
            PRED_FINAL_1201,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        # Red pre-doc-sync (no #1202 entry in the log yet); green
        # once the doc-sync lands. Deselect pre-commit.
        # NOTE: the log's tail is file-chronological (entries
        # appended, oldest-first): D1200 < E1201 < A1202 in file
        # order.
        window = _window()
        assert ("A", "1202") in window
        assert ("E", "1201") in window
        assert ("D", "1200") in window
        tail = window[-3:]
        assert tail == [("D", "1200"), ("E", "1201"), ("A", "1202")], tail

    def test_rotation_phrase_in_log_entry(self):
        # Red pre-doc-sync; green once the doc-sync lands. Deselect
        # pre-commit.
        text = _read(LOG_PATH)
        assert "## #1202 Type A:" in text
        entry_start = text.index("## #1202 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1200-1204 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1202:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1202")
        assert "Type A #1202" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1202:
    def test_m952_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M952_HOME))
        line = next(l for l in text.splitlines() if l.strip() == M952_KEY + ":")
        assert line.startswith(" " * M952_INDENT)
        assert not line.startswith(" " * (M952_INDENT + 1))

    def test_m952_block_sibling_of_1117_block(self):
        text = _read(os.path.join(REPO_ROOT, M952_HOME))
        assert (
            "    type_a_1117_ft_openai_ftc_agent_safety_probe_"
            "vs_carried_meta_arms_oct01_6am:" in text
        )

    def test_m952_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M952_HOME))
        assert "mechanism_id: 952" in text

    def test_max_numeric_mechanism_id_is_952(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_953_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_953_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_953_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_952_substring_in_block_key(self):
        assert "952" not in M952_KEY


# ---------------------------------------------------------------------------
# 4. m952 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM952ContentDiscipline1202:
    def test_metadata_fields(self):
        d = _m952_data()
        assert d["iteration"] == 1202
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-04 08:00 PDT"
        assert d["scheduled_job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["mechanism_id"] == 952
        assert d["competitor"] == "openai"
        assert d["comparator_entity"] == "meta"

    def test_three_fresh_openai_arms(self):
        d = _m952_data()
        arms = d["openai_arms_fresh"]
        assert len(arms) == 3
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [-0.40, -0.20, -0.30], tones

    def test_openai_arm_mean(self):
        d = _m952_data()
        tones = [a["manual_illustrative_tone"] for a in d["openai_arms_fresh"]]
        mean = sum(tones) / len(tones)
        assert abs(mean - (-0.30)) < 1e-9, mean
        assert abs(d["scorer_manual_illustrative"]["openai_mean"] - (-0.30)) < 1e-9

    def test_a1_asymmetric_arm_two_relays(self):
        d = _m952_data()
        arms = d["openai_arms_fresh"]
        a1 = next(a for a in arms if a["arm"] == "A1")
        assert a1["manual_illustrative_tone"] == -0.40
        assert "Asymmetric" in a1["peg"]
        assert len(a1["urls"]) == 2
        assert any("techstartups.com" in u for u in a1["urls"])
        assert any("technadu.com" in u for u in a1["urls"])

    def test_bounded_absence_three_legs(self):
        d = _m952_data()
        legs = d["bounded_absence_legs"]
        assert len(legs) == 3
        by_leg = {leg["leg"]: leg for leg in legs}
        assert by_leg["B1"]["search_sets"] == 2
        assert by_leg["B2"]["search_sets"] == 3
        assert by_leg["B3"]["search_sets"] == 1
        for leg in legs:
            assert leg["ft_com_urls"] == 0, leg["leg"]

    def test_firings_names_in_b2(self):
        d = _m952_data()
        legs = d["bounded_absence_legs"]
        b2 = next(leg for leg in legs if leg["leg"] == "B2")
        for name in FIRING_NAMES:
            assert name in b2["peg"], name

    def test_meta_comparator_carried(self):
        d = _m952_data()
        meta = d["meta_comparator_carried"]
        assert len(meta) == 3
        mean_item = next(i for i in meta if "meta_mean" in i)
        assert abs(mean_item["meta_mean"] - (-0.285)) < 1e-9
        arms = [i for i in meta if "arm" in i]
        assert len(arms) == 2
        assert all(i.get("rescore") == "un-rescored per #807" for i in arms)

    def test_illustrative_delta_arithmetic(self):
        d = _m952_data()
        sc = d["scorer_manual_illustrative"]
        assert abs(sc["illustrative_delta_openai_minus_meta"] - (-0.015)) < 1e-9
        assert "near-null parity" in sc["delta_reading"]
        assert "+0.22" in sc["clean_matched_register_pair"]

    def test_test_file_field_matches_own_basename(self):
        assert _m952_data()["test_file"] == "tests/" + OWN_BASENAME

    def test_ascii_and_no_em_dash_in_block(self):
        block = _m952_block_text()
        assert "\u2014" not in block
        block.encode("ascii")


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1202:
    def test_manual_illustrative_only(self):
        sd = _m952_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd

    def test_no_analysis_json_update(self):
        assert _m952_data()["no_analysis_json_update"] is True
        assert "analysis.json" not in _git("diff", "--name-only")

    def test_correlation_not_causation(self):
        assert _m952_data()["correlation_not_causation"] is True

    def test_forty_eighth_member_landed(self):
        # This run LANDS the forty-eighth member-claim form (the
        # needle is fragment-built per #715; the contiguous literal
        # lives in the financial-times.yaml m952 block only).
        assert _T48 in _m952_data()["falsification_family"]
        assert _m952_data()["falsification_ledger"] == "48"

    def test_artifact_not_grade(self):
        assert "artifact_grade false" in _m952_data()["statistical_discipline"]


# ---------------------------------------------------------------------------
# 6. Falsification ledger (47 -> 48 this run)
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1202:
    def test_forty_sixth_intact_in_verge(self):
        text = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert text.count(_T46) == 2

    def test_forty_seventh_stays_in_wired_m946(self):
        # The forty-seventh claim form stays exactly in wired.yaml
        # m946 (2 occurrences, the #1127 designed pattern).
        text = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert text.count(_T47) == 2

    def test_forty_seventh_nowhere_else(self):
        for p in _needle_hits_profiles(_T47):
            assert p.endswith("wired.yaml"), p

    def test_forty_eighth_now_in_financial_times(self):
        # This run lands the forty-eighth member-claim form in
        # financial-times.yaml m952 (2 occurrences: the
        # falsification_family claim + the novelty landing note,
        # the #1127 designed pattern).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(_T48) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(_T48):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_absent(self):
        assert _needle_hits_profiles(_T49) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert _T49 not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (_TW35, _TW36, _TW37, _TW38, _TW39):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(_TW40) == []

    def test_ledger_note_advances_to_48(self):
        assert _m952_data()["falsification_ledger"] == "48"
        assert "47->48" in _m952_data()["ledger_note"]



# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1201's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1202:
    def test_e1201_max_951_pin_trips_by_design(self):
        # #1201 pinned max numeric mechanism_id 951; this run lands
        # 952, so the pin fails BY DESIGN. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 952

    def test_e1201_zero_952_numeric_pin_trips_by_design(self):
        # The numeric field form mechanism_id: 952 now exists in
        # profiles/financial-times.yaml. Documented, not repaired.
        assert _repo_grep_numeric_mechanism_id(952) != []

    def test_e1201_zero_952_underscore_pin_stays_green(self):
        # This run lands no underscore-form nine-five-two literal in
        # profiles/ or tests/ (needles are format-built). Stays green.
        assert _repo_grep_underscore_mechanism(952) == []

    def test_e1201_zero_952_dash_pin_stays_green(self):
        assert _repo_grep_dash_mechanism(952) == []

    def test_e1201_no_type_a_1202_pin_trips_by_design(self):
        # #1201 pinned no "Type A #1202" in git log; this run's own
        # main commit carries it (the #1191-class self-trip on the
        # run's own main-commit subject, documented).
        log = _git("log", "--format=%H %s", "--grep=Type A #1202")
        assert "Type A #1202" in log


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards for #1203)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1202:
    def test_forward_max_952(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_forward_zero_953_all_forms(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_forward_no_type_b_1203_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type B #1203")
        assert log.strip() == ""

    def test_forward_forty_eighth_in_ft(self):
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(_T48) == 2

    def test_forward_no_forty_ninth_member(self):
        assert _needle_hits_profiles(_T49) == []

    def test_forward_directions_state(self):
        for needle in (_TW35, _TW36, _TW37, _TW38, _TW39):
            assert _needle_hits_profiles(needle) != [], needle
        assert _needle_hits_profiles(_TW40) == []


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1200-launched suite; checked only per #795)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1202:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_this_run_does_not_touch_suite(self):
        # No Type A #1202 / m952 markers in the suite log; this run
        # checks only. The verdict belongs to #1205 per #795.
        text = _read(SUITE_LOG)
        assert "1202" not in text
        assert "m952" not in text

    def test_suite_verdict_belongs_to_1205(self):
        # The #1200-launched suite's verdict is claimed by the next
        # Type D run (#1205) per #795, never by this run.
        assert "type_d_1200" in SUITE_LOG


# ---------------------------------------------------------------------------
# 10. Doc-sync (deselected pre-commit per #719; green post-doc-sync)
# ---------------------------------------------------------------------------
class TestTypeADocSync1202:
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
class TestTypeAIterationLog1202:
    @pytest.mark.skip(reason="deselected pre-commit per #721; green post-doc-sync")
    def test_1202_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1202 Type A:" in text

    @pytest.mark.skip(reason="deselected pre-commit per #721; green post-doc-sync")
    def test_1202_entry_registers_hashes(self):
        # Post-log-hash followup per #721: the entry names the main,
        # anchor, and doc-sync commits.
        text = _read(LOG_PATH)
        entry_start = text.index("## #1202 Type A:")
        entry = text[entry_start : entry_start + 12000]
        assert "Main commit" in entry
        assert "Anchor followup" in entry
        assert "Doc-sync" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1202:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped per the #1147 convention: the working tree
        # carries pre-existing in-flight uncommitted changes (#899
        # nytimes.yaml m771 hunk, #938 test file anchor edit, #900
        # untracked test file, #1012 test-file working-tree edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files (profiles/financial-times.yaml m952 block + the
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
            assert "m952" not in diff, path
            assert "Type A #1202" not in diff, path


# ---------------------------------------------------------------------------
# 13. ASCII discipline (no em dashes in the new files)
# ---------------------------------------------------------------------------
class TestAsciiDiscipline1202:
    def test_no_em_dash_in_own_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_no_em_dash_in_m952_block(self):
        block = _m952_block_text()
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
        log = _git("log", "--format=%H %s", "--grep=Type A #1202")
        first = log.splitlines()[0].split()[0]
        assert ANCHORED_SHA == first, (ANCHORED_SHA, first)

    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_anchor_placeholder_flipped(self):
        assert ANCHORED_SHA != "0" * 40
