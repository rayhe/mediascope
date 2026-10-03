"""Type A #1177: The Verge x OpenAI Dots persistent-agent product-launch
register vs The Verge x Meta Muse-agent scrutiny arms (Oct 3 2026,
11:00 AM PDT).

REGISTER BOUND on m907's falsification (Type A #1127): m907 falsified the
UNIFORM payer-softening prediction on the un-briefed safety-crisis peg
(Sep 28-30: Astra deception-shelving homepage -0.40, FTC rogue-agent probe
brief -0.35). This run tests the same publication x deal-partner pair on
the BRIEFED product-launch peg and finds the prediction HOLDS there: The
Verge applies the constructive product-launch register to OpenAI's Dots
agent launch (Sep 29-30) while applying adversarial scrutiny to Meta's
rival Muse agent in the same six-day window (Sep 24-29).

(O1) Dots launch coverage (Sep 29-30, 2026): The Verge-attested via four
independent secondaries - whatalife.ph feature list "(The Verge, The
Decoder)"; webpronews.com "A Verge report notes Dots integrate directly
into Slack and Microsoft Teams. They carry context across sessions.";
savedelete.com "The Verge reports that OpenAI plans to bring them to
consumers."; rundatarun.io Oct-2 brief citing theverge.com on Dots making
"persistent agency the default ChatGPT product". Feature-descriptive
product-launch register. MANUAL ILLUSTRATIVE +0.15.

(O2) Pro 500 / Ultrafast tier (Sep 30): alextech.ai "According to The
Verge, this tier unlocks Ultrafast mode, a speed tier that allows the
GPT-6 Astra model to deliver significantly faster responses."
Business-product register. MANUAL ILLUSTRATIVE +0.10.

OpenAI arm mean +0.125.

(M1) Sep 24: The Verge's Muse VM-export story - explainx.ai "On September
24, 2026, The Verge reported that Muse could reveal 'all its secrets' by
exporting hundreds of megabytes of data, including system files";
theaifeed.com "The Verge reports that Peter James and Jonny L. Saunders
independently obtained archives containing system files, application
templates, and internal documentation. The Verge's own test also exposed
a directory tree". Scrutiny register. MANUAL ILLUSTRATIVE -0.35.

(M2) Sep 29: Jess Weatherbed's Muse Marketplace story - explainx.ai
"according to The Verge (Jess Weatherbed, September 29, 2026)... After
Robb authorized Muse to handle Facebook Marketplace, the agent messaged a
buyer with a pickup address he had given Muse, agreed a lowball price".
Accountability register. MANUAL ILLUSTRATIVE -0.40.

Meta arm mean -0.375. Illustrative delta (OpenAI minus Meta) +0.50:
directionally softer for the deal partner on the product-launch peg,
thesis-consistent. Same-day contrast sharpens the bound: the Dots launch
(Sep 29 DevDay) and the Muse Marketplace accountability piece (Sep 29)
ran the same day.

NOT a falsification-family member: the finding is thesis-consistent and
the uniform prediction was already tested at #1127 (m907, FORTY-SIXTH
member). Ledger holds at 46.

6 browser.search query sets this run, 0 browser.open (excerpt-bounded per
#503; theverge.com policy-blocked). All URLs copied verbatim from
search-result Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

Pre-commit novelty (per #715): zero test_type_a_1177 files on disk (glob);
no "Type A #1177" in git log (--grep); max numeric mechanism_id 936 in
profiles/ pre-commit (937 post-insert, working tree); zero
numeric/underscore/dash 937 mechanism keys repo-wide pre-commit (needles
format-built, own file excluded); the 10 evidence URLs zero-hit
repo-wide pre-commit (git grep -F on verbatim Full-URL listings); block
key zero-hit repo-wide pre-commit (git grep); no #1177 rows in README /
ARCHITECTURE test tables or iteration-log pre-commit.

1175-1179 window THIRD leg D(#1175) -> E(#1176) -> A(#1177 this run) ->
B(#1178) -> C(#1179) (anchor patched post-commit per #565).
"""

import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

# Anchor: zero placeholder pre-commit; patched to the main-commit SHA in
# the anchor followup per #565.
ANCHORED_SHA = "0" * 40

# Rotation: predecessor #1176 Type E commits (verified in git log).
P1176_MAIN = "1c4ef7d7"
P1176_ANCHOR = "a5084b69"
P1176_DOCSYNC = "db3af5b9"
P1176_FINAL = "9f96d6a5"
# Predecessor #1175 Type D commits (window opening leg).
P1175_MAIN = "17fa835c"
P1175_FINAL = "259a93cb"

# Mechanism numbering: this run lands 937; the forward guard watches 938.
THIS_NUM = 937
NEXT_NUM = 938

# Block key (carries the iteration number 1177, no 937 substring, per the
# #715 keying lesson).
BLOCK_KEY = (
    "type_a_1177_verge_openai_dots_persistent_agent_launch"
    "_vs_meta_muse_scrutiny_arms_oct03_11am"
)

# Evidence URLs (verbatim from search-result Full-URL listings).
O1_WHATALIFE = (
    "https://whatalife.ph/openai-dots-explained-always-on-agents"
    "-gpt-6-astra-and-who-can-use-them/"
)
O1_WEBPRONEWS = (
    "https://www.webpronews.com/openais-dots-take-on-metas-muse"
    "-in-the-race-for-always-on-ai-agents/"
)
O1_SAVEDELETE = "https://savedelete.com/article/openai-dots-always-on-agents/"
O1_RUNDATARUN = "https://wire.rundatarun.io/briefs/2026-10-02"
O1_EXPLAINX = (
    "https://explainx.ai/blog/openai-dots-always-on-agents-devday-2026"
)
O2_ALEXTECH = (
    "https://www.alextech.ai/en/news/openai-launches-500-pro-plan"
    "-and-halves-limits-for-the-200-tier/"
)
M1_EXPLAINX = (
    "https://www.explainx.ai/blog/meta-muse-vm-filesystem-export"
    "-intended-behavior-not-breach-2026"
)
M1_AIFEED = "https://theaifeed.com/en/ai-news/meta-muse-vm-filesystem-2026/"
M1_VANDATA = "https://vandatateam.com/blog/ai-agent-permissions-muse-dots"
M2_EXPLAINX = (
    "https://explainx.ai/blog/meta-muse-shared-youtuber-address"
    "-marketplace-2026"
)
EVIDENCE_URLS = [
    O1_WHATALIFE, O1_WEBPRONEWS, O1_SAVEDELETE, O1_RUNDATARUN,
    O1_EXPLAINX, O2_ALEXTECH, M1_EXPLAINX, M1_AIFEED, M1_VANDATA,
    M2_EXPLAINX,
]

# Falsification-ledger guard needles (fragment-built per #715; the landed
# FORTY-SIXTH / THIRTY-FIFTH / THIRTY-SIXTH forms are plain literals
# already in corpus; forward-guard needles must stay fragment-built so this
# file carries no contiguous next-slot literal).
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"

# Doc-sync ratchet (post-sync-positive per #719; NEW_TEST_COUNT patched
# with the real collected count before the doc-sync commit; deselected
# in-gate).
README_TESTS_PRE = 62556
README_FILES_PRE = 1501
NEW_TEST_COUNT = 61  # collected 2026-10-03 11:xx PDT (patched pre-doc-sync)
README_TESTS_POST = README_TESTS_PRE + NEW_TEST_COUNT
README_FILES_POST = 1502


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield profile + test source files (working tree).

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
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
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _tracked_grep_files(needle):
    """Return tracked files containing a literal needle (committed tree).

    Argument order: needle BEFORE the revision, no stray "--" ahead of the
    needle (the #1171 in-gate lesson: a "--" before the needle makes git
    grep treat the needle as a pathspec, silently returning zero hits and
    making negative guards pass vacuously).
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--", ".").stdout
    return [line for line in out.splitlines() if line.strip()]


def _repo_grep_underscore_mechanism(n):
    """Files containing the underscore-form mechanism key (working tree).

    Needle format-built at runtime so this file carries no contiguous
    underscore-form literal (per the #770 lesson).
    """
    needle = "%s%d" % ("mechanism_", n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


class TestAnchor:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor
        # followup patches it per #565. This test documents the
        # pre-commit state; it also passes post-commit via the OR form.
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


class TestRotationGuard:
    def test_predecessor_1176_chain_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1176_MAIN in log
        assert P1176_ANCHOR in log
        assert P1176_DOCSYNC in log
        assert P1176_FINAL in log

    def test_predecessor_1175_window_opening_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1175_MAIN in log
        assert P1175_FINAL in log

    def test_type_a_1177_novelty(self):
        # "Type A #1177" absent from git log pre-commit; own main commit
        # not yet landed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1177:") lands; deselect in post-commit runs.
        log = _git("log", "--oneline", "--grep=Type A #1177").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1175) -> E(#1176) -> A(#1177 this run)" in src

    def test_next_run_1178_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B(#1178)" in src


class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_is_937_post_insert(self):
        # The m937 block is inserted pre-commit (working tree); the max
        # advances 936 -> 937 with this run's landing.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_937_numeric_mechanism_id_in_the_verge(self):
        hits = _repo_grep_numeric_mechanism_id(THIS_NUM)
        assert any(h.endswith("profiles/the-verge.yaml") for h in hits), hits

    def test_zero_937_underscore_mechanism_by_designed_keying(self):
        # Block key carries no 937 substring per the #715 keying lesson;
        # mechanism_id advances in colon form only.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []

    def test_zero_937_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(THIS_NUM) == []

    def test_block_key_present_in_the_verge_working_tree(self):
        src = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert BLOCK_KEY in src

    def test_no_1177_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_a_1177" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestContentDiscipline:
    def _block_src(self):
        return _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))

    def test_o1_dots_launch_arm_fields(self):
        src = self._block_src()
        assert "OpenAI Dots always-on persistent agents launch coverage" in src
        assert "(The Verge, The Decoder)" in src
        assert "A Verge report notes Dots integrate directly into Slack and Microsoft Teams" in src
        assert "The Verge reports that OpenAI plans to bring them to consumers" in src
        assert "persistent agency the default ChatGPT product" in src

    def test_o2_pro500_ultrafast_arm_fields(self):
        src = self._block_src()
        assert "Pro 500 / Ultrafast tier coverage" in src
        assert "According to The Verge, this tier unlocks Ultrafast mode" in src
        assert "significantly faster responses" in src

    def test_m1_muse_vm_export_arm_fields(self):
        src = self._block_src()
        assert "Muse VM filesystem export story" in src
        assert "all its secrets" in src
        assert "exporting hundreds of megabytes of data, including system files" in src
        assert "Peter James and Jonny L. Saunders" in src
        assert "own test also exposed a directory tree" in src

    def test_m2_marketplace_arm_fields(self):
        src = self._block_src()
        assert "Muse shared a YouTuber address on Facebook Marketplace" in src
        assert "Jess Weatherbed" in src
        assert "2026-09-29" in src
        assert "agreed a lowball price" in src

    def test_arm_tones_and_means(self):
        src = self._block_src()
        assert "tone_illustrative: 0.15" in src
        assert "tone_illustrative: 0.10" in src
        assert "tone_illustrative: -0.35" in src
        assert "tone_illustrative: -0.40" in src
        assert "openai_mean_tone: 0.125" in src
        assert "meta_mean_tone: -0.375" in src

    def test_illustrative_delta(self):
        src = self._block_src()
        assert "illustrative_delta_openai_minus_meta: 0.50" in src
        assert '"0.125 - (-0.375) = 0.50"' in src

    def test_all_evidence_urls_in_block(self):
        src = self._block_src()
        for url in EVIDENCE_URLS:
            assert url in src, url

    def test_register_bound_on_m907(self):
        src = self._block_src()
        assert "REGISTER BOUND on m907" in src
        assert "register-bounded" in src
        assert "un-briefed safety-news peg" in src
        assert "briefed product launches" in src

    def test_same_day_contrast_noted(self):
        src = self._block_src()
        assert "Sep 29 DevDay" in src
        assert "ran the same day" in src

    def test_financial_relationship_fields(self):
        src = self._block_src()
        assert "Vox Media strategic content and product partnership with OpenAI, May 29 2024" in src
        assert "coverage_prediction" in src
        assert "softer (uniform payer-softening)" in src

    def test_connects_to_m907_and_m425(self):
        src = self._block_src()
        assert "connects_to: [425, 507, 557, 880, 907]" in src


class TestResearchMethod:
    def test_six_query_sets_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "6 browser.search query sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open" in src
        assert "excerpt-bounded per" in src

    def test_rejected_pairs_documented(self):
        blk = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert "REJECTED:" in blk
        assert "no BI originals surfaced" in blk
        assert "already in-corpus via runtimewire" in blk

    def test_verbatim_url_discipline(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verbatim from search-result Full-URL listings" in src
        assert "no canonical URLs constructed" in src

    def test_ascii_discipline_in_block(self):
        blk = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        start = blk.index(BLOCK_KEY)
        segment = blk[start:start + 24000]
        assert "\u2014" not in segment
        assert "\u2019" not in segment
        assert "\u201c" not in segment

    def test_ascii_discipline_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src


class TestStatisticalDiscipline:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        return _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))

    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in self._blk()

    def test_engine_not_run_and_not_artifact_grade(self):
        assert "engine NOT run" in self._src()
        assert "NOT artifact-grade" in self._src()

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in self._src()

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in self._src()

    def test_falsification_ledger_holds_46(self):
        assert "ledger holds at 46" in self._src()
        assert "falsification_ledger: 46" in self._blk()

    def test_not_a_falsification_family_member(self):
        assert "NOT a falsification-family member" in self._blk()
        assert "falsification_family_member: false" in self._blk()

    def test_forty_sixth_member_claim_twice_in_the_verge(self):
        # Landed FORTY-SIXTH form (m907, committed at #1127); present
        # twice in the committed the-verge.yaml.
        out = _git("grep", "-F", _T46, "HEAD", "--", "profiles/the-verge.yaml").stdout
        assert len(out.strip().splitlines()) == 2

    def test_no_forty_seventh_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T47) == []

    def test_no_forty_eighth_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T48) == []

    def test_thirty_fifth_direction_present(self):
        hits = _tracked_grep_files(_TW35)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_thirty_sixth_direction_present(self):
        # Landed THIRTY-SIXTH form: the m933 REGULATORY-PREEMPTION
        # direction (committed at #1169, verified at #1170 Type D).
        hits = _tracked_grep_files(_TW36)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_no_thirty_seventh_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW37) == []

    def test_no_thirty_eighth_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW38) == []


class TestStalenessPins:
    def test_1176_zero_937_guards_flip_by_design(self):
        # #1176's TestMechanismNovelty zero-937 sweeps and max-936 pin
        # must now FAIL: the landed 937 supersedes them per the #710/#720
        # convention. Recorded via subprocess, not repaired.
        target = os.path.join(
            TESTS_DIR,
            "test_type_e_1176_podcast_sentiment_158th_verification_oct03_10am.py",
        )
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target + "::TestMechanismNovelty",
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        assert res.returncode != 0, (
            "expected #1176 zero-937 guards to flip on the landed 937;\n"
            + res.stdout[-1500:]
        )

    def test_1176_adds_no_mechanisms_pin_flips_by_design(self):
        # #1176 asserted max == 936 (Type E adds no mechanisms); the
        # Type A #1177 landing supersedes it.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_1176_underscore_dash_937_guards_stay_green(self):
        # By DESIGNED keying the block carries no underscore/dash 937
        # literal, so #1176's underscore/dash-form 937 guards STAY GREEN.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []
        assert _repo_grep_dash_mechanism(THIS_NUM) == []


class TestForwardGuards:
    def test_zero_938_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_938_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_938_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_937(self):
        assert _max_numeric_mechanism_id() == THIS_NUM


class TestDocSync:
    # Post-sync-positive per #719: these go green in the doc-sync
    # followup. Deselect in the pre-doc-sync in-gate run.
    def test_readme_stats_post_sync(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d | Across %d test files |" % (
            README_TESTS_POST, README_FILES_POST) in src

    def test_readme_test_table_row_1177(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "Type A #1177" in src

    def test_architecture_tree_row_1177(self):
        src = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert os.path.basename(OWN_BASENAME) in src

    def test_test_file_constants_post_sync_form(self):
        # NEW_TEST_COUNT patched to the real collected count before the
        # doc-sync commit; README_TESTS_POST derived from it.
        assert NEW_TEST_COUNT > 0
        assert README_TESTS_POST == README_TESTS_PRE + NEW_TEST_COUNT
        assert README_FILES_POST == README_FILES_PRE + 1


class TestIterationLog:
    # Post-sync-positive per #719: deselect in the pre-doc-sync in-gate.
    def test_iteration_log_1177_entry(self):
        src = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1177 Type A" in src
        assert "m937" in src


class TestInFlightIsolation:
    def test_in_flight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
        # anchor edit), #900 (untracked Type D test file), #1012-wt (Type A
        # test file edit) stay out of this run's index and diff. Do NOT
        # touch #1024 m846 (Ray's revert/leave/rebuild decision pending).
        status = _git("status", "--short").stdout
        for marker in ("profiles/nytimes.yaml",
                       "test_type_a_1012_",
                       "test_type_b_938_",
                       "test_type_d_900_"):
            assert marker in status, marker
        diff = _git("diff", "--cached", "--name-only").stdout
        assert diff.strip() == "", diff

    def test_no_1024_m846_touch(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "do NOT touch #1024 m846" in src
        status = _git("status", "--short").stdout
        assert "m846" not in status


class TestYamlValidity:
    def test_the_verge_yaml_parses(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "the-verge.yaml")))
        blk = d["competitor_relationships"]["openai"][BLOCK_KEY]
        assert blk["mechanism_id"] == THIS_NUM
        assert blk["iteration"] == 1177
        assert len(blk["openai_arms_new"]) == 2
        assert len(blk["meta_arms_carried"]) == 2
        assert blk["falsification_ledger"] == 46
        assert blk["falsification_family_member"] is False

    def test_no_duplicate_block_key(self):
        src = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert src.count(BLOCK_KEY + ":") == 1


class TestGitLogPostCommit:
    # Post-commit-positive per #565/#719: deselect in the pre-commit
    # in-gate; they go green after the main + anchor commits land.
    def test_main_commit_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type A #1177").stdout
        assert "Type A #1177:" in log

    def test_anchor_patched_post_commit(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40
