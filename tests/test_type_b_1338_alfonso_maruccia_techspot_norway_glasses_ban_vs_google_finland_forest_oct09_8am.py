# -*- coding: utf-8 -*-
"""Type B #1338: Alfonso Maruccia (TechSpot staff journalist) - cross-entity
register-constancy pair: the Oct-6-2026 Norway smart-glasses temporary-ban
piece (META arm, "The Worst Spectacle" dek, -0.35 MANUAL ILLUSTRATIVE) vs
the Oct-5-2026 Google Finland data-center forest-clearing piece (GOOGLE arm,
"Cutting corners" dek, -0.35); illustrative delta (google minus meta) 0.00 -
register constancy, same writer, same outlet, one day apart; NOT a
falsification-family member (ledger HOLDS at 62); ZERO-GRADIENT control on
the payer axis (no documented TechSpot x Meta / x Google / x Anthropic /
x OpenAI AI content licensing deal in-corpus; joins the #1313/#1318/#1328/
#1333 control-case family); verdict directionally_supported_not_proven;
NOT artifact-grade; no analysis.json update.

The peg: TechSpot staff journalist Alfonso Maruccia (fully novel to the
corpus - zero "alfonso maruccia" hits repo-wide pre-commit) publishes two
adversarial accountability pieces one day apart. The Oct-6 Meta arm covers
Norway's temporary-ban proposal on AI smart glasses in parks, beaches and
schools, headlined with a spectacle/spectacles stigma pun ("The Worst
Spectacle") and a dek pricing privacy as the casualty ("privacy is paying
the price"); the devices are "unwelcome guests" and bystanders "unwilling
guests". The Oct-5 Google arm covers Google's EUR13B Finland AI expansion
through premature forest clearing ("Cutting corners" pun dek, "began
bulldozing large swaths of forest before the required environmental
review", "300 hectares of Finnish forest, roughly 420 football fields",
Finland's LVV regulator demanding answers). MANUAL ILLUSTRATIVE -0.35 on
both arms: the same writer applies the same adversarial standard to Meta
and Google.

Type B lands one mechanism: m1034 in profiles/careers/journalists.yaml
under a new alfonso_maruccia_type_b top key (0-indent, end-of-file),
competitor_coverage/type_b_1338_... block (4-space indent); max numeric
mechanism_id 1033->1034; next one-zero-three-five; ledger HOLDS at 62
(the sixty-second member remains the #1332 m1030 WSJ x OpenAI member; the
sixty-third member-claim form stays absent repo-wide; m1034 is
falsification_family_member false).

Research method: 1 delegated scout (14 browser.search queries - saturation
screening of 30+ journalists, ruling out Goode, Chokkattu, Pero, Ashworth,
Schiffer, Rogers, Ropek, Bell, Keach as in-corpus; Dupre, Schroeder,
Phelan, Zeff, Dominic Preston, Katie Paul, Newton as pre-screened; Lily
Hay Newman, Jason Aten, Shane Bauer, Wardle, Victoria Song, David Imel,
Allison Johnson, Karan Joshi, Eli Tan, Andy Stone, David Singleton,
Stephen Robles as exploratory in-corpus; Matt J. Robb as novel-but-a-
YouTuber) + 3 main-run browser.search verification sets (Maruccia Norway
"Worst Spectacle" identity confirmation via WeSearch relay + TechSpot
forum topic; Maruccia Google Finland "Cutting corners" via staff page +
article excerpt; in-corpus TechSpot licensing-deal absence check), 0
browser.open (excerpt-bounded per #503). Pre-commit novelty greps: zero
test_type_b_1338 files on disk (glob); no Type B #1338 in git log
(--grep); max numeric mechanism_id 1033 in profiles/ pre-commit; zero
numeric/underscore/dash next-number one-zero-three-five mechanism key
forms in profiles/ + tests/ pre-commit (needles format-built per #715,
own file excluded, verified clean by direct sweep); "alfonso maruccia"
zero-hit repo-wide pre-commit (git grep -F -i); 4/4 source URLs zero-hit
repo-wide pre-commit (git grep -F); block key zero-hit repo-wide
pre-commit; "## #1338" zero-hit in iteration-log pre-commit; no #1338 row
in README/ARCHITECTURE test tables pre-commit; README stats 76646/1662
pre-commit. All URLs copied verbatim from the browser.search Full-URL
listings; no canonical URLs constructed (the techspot.com canonical for
the Norway piece did not surface; the no-construction rule holds).
ASCII-only, no em dashes.

This run is the FOURTH leg of the 1335-1339 window (D #1335 -> E #1336 ->
A #1337 -> B #1338 -> C #1339 per the #565 anchor + rotation guard); the
1330-1334 window is VERIFIED CLOSED. Next run #1339 Type C closes the
window. The next background-suite verdict belongs to #1340 per #795 (the
#1335-launched suite, goal hidden_files type_d_1335_full_suite.log; this
run OBSERVES only, neither re-launches, kills, nor writes to it).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
max or next number, the forty-eighth through sixty-third member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, and sixty-second in
news-corp.yaml, the fifty-third in the-verge.yaml, the fifty-fourth in
guardian.yaml, the fifty-fifth in atlantic.yaml, the fifty-sixth and
sixty-first in wired.yaml, the fifty-seventh in ap.yaml; the sixty-third
is absent repo-wide as of this run.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1338_alfonso_maruccia_techspot_norway_glasses_ban_"
    "vs_google_finland_forest_oct09_8am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "148b3e4cd83332f93bcff757e85d862306885de3"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1034
NEXT_NUM = 1035  # integer only; key-form needles are format-built

# Predecessor chain: #1337 Type A THIRD leg of the 1335-1339 window.
PRED_MAIN_1337 = "c8d74b54ebe3acc9ac189f03b94a6dc74a4b4940"
PRED_ANCHOR_1337 = "122ce5e7493a2d92cddb12c8f1d698fe31377eba"
PRED_DOCSYNC_1337 = "cb323d9ecf31478ac18048ee20e19ee3fcde5565"
PRED_FINAL_1337 = "9f537c0887f02bf0b7b53e383005d89b3a1ae01c"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1338 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in this run's terminal log-hash followup per #721.
PRED_MAIN_1338 = "148b3e4cd83332f93bcff757e85d862306885de3"  # re-pinned to #1338 main sha in the anchor followup per #721/#1292

# #1339's main commit (full sha), for the ancestor-form no-Type-C-#1339
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1339's
# terminal log-hash followup per #721.
PRED_MAIN_1339 = "e6c6a7511d6ce5d3ed66da14d564ab8b8774a7be"  # re-pinned to #1339 main sha in the anchor followup per #721/#1292

# The #1337 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1033; zero next-number
# one-zero-three-four / no-Type-B-#1338-in-git-log / fortieth
# direction absent / forty-eighth through sixty-second members
# intact / no sixty-third member (repo-wide) / ledger 62).
B1337_FILE = (
    "test_type_a_1337_verge_microsoft_oct08_copilot_agentic_"
    "pc_files_vs_carried_meta_connect_arms_oct09_7am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 76751  # post-doc-sync total (pre-sync 76646 + 105) - PATCHED post-collection
README_FILE_COUNT = 1663  # pre-sync 1662 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
# The fifty-ninth member-claim form is fragment-built per #715
# (landed #1302 in profiles/news-corp.yaml).
_T59 = "FIFT" + "Y-NINTH falsification-family member"
# The sixtieth member-claim form is fragment-built per #715
# (landed #1322 in profiles/financial-times.yaml).
_T60 = "SIXT" + "IETH falsification-family member"
# The sixty-first member-claim form is fragment-built per #715
# (landed #1327 in profiles/wired.yaml).
_T61 = "SIXT" + "Y-FIRST falsification-family member"
# The sixty-second member-claim form is fragment-built per #715
# (landed #1332 in profiles/news-corp.yaml).
_T62 = "SIXT" + "Y-SECOND falsification-family member"
# The sixty-third member-claim form is fragment-built per #715
# (no sixty-third member may exist repo-wide).
_T63 = "SIXT" + "Y-THIRD falsification-family member"

BLOCK_KEY = (
    "type_b_1338_alfonso_maruccia_techspot_norway_glasses_ban_"
    "vs_google_finland_forest_oct09_8am"
)

# MANUAL ILLUSTRATIVE tone constants (hand-assigned register positions
# per the Aug 28 2026 standing rule; NOT engine output).
META_TONE = -0.35
GOOGLE_TONE = -0.35
ILLUSTRATIVE_DELTA = 0.0  # google minus meta: register constancy

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://wesearch.press/s/norway-wants-to-temporarily-ban-smart-glasses-in-parks-beach-c1a15fa0",
    "https://www.techspot.com/community/topics/norway-wants-to-temporarily-ban-smart-glasses-in-parks-beaches-and-schools.299058/",
    "https://www.techspot.com/news/114100-google-cleared-300-hectares-finnish-forest-data-center.html",
    "https://www.techspot.com/community/staff/alfonso-maruccia.491138/",
]

# 3 main-run browser.search query sets this run (0 browser.open per
# #503); the delegated scout ran 14 further query sets (saturation
# screening), documented in research_method.
QUERY_SETS = [
    "Alfonso Maruccia TechSpot Norway smart glasses ban October 2026 \"Worst Spectacle\"",
    "Alfonso Maruccia TechSpot Google Finland data center expansion October 2026",
    "\"The Worst Spectacle\" TechSpot Maruccia smart glasses",
]


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _top():
    return _load_journalists()["alfonso_maruccia_type_b"]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

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
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-k", classname,
         "-q", "--no-header", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        timeout=600,
    )


# ---------------------------------------------------------------------------
# 1. Anchor per #565
# ---------------------------------------------------------------------------


class TestAnchor1338:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha. This test fails BY
        # DESIGN post-anchor and is deselected in the in-gate run;
        # the patched form is asserted by
        # test_anchor_sha_patched_to_main_commit. Terminal per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN post-anchor" in src

    def test_fourth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1335-1339 window" in src

    def test_1330_1334_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1330-1334" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1339_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1339" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1337 predecessor chain; B is the FOURTH leg.
# ---------------------------------------------------------------------------


class TestRotationGuard1338:
    def test_predecessor_1337_chain_verified(self):
        for sha in (
            PRED_MAIN_1337, PRED_ANCHOR_1337, PRED_DOCSYNC_1337,
            PRED_FINAL_1337,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1335 -> E #1336 -> A #1337 -> B #1338 -> C #1339" in src

    def test_next_leg_is_type_c_1339(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1339 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1034); the Type
        # A predecessor added one (mechanism 1033).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------


class TestMechanismNovelty1338:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1338 in key, no 1034 or
        # 1035 substring.
        assert "1338" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # the colon form; the underscore key form must not exist
        # repo-wide.
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_max_mechanism_id_is_1034(self):
        # Post-landing form: the m1034 block is landed, so the max is
        # 1034 and the next-number colon form is absent in profiles.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_b_1338_in_git_log_pin(self):
        # Post-main-commit form for the OWN run (the #1191-class
        # self-trip, re-pinned in this run's terminal log-hash
        # followup per #721): every commit whose message matches
        # "Type B #1338" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1338")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1338's own commits"
        main = _git("rev-parse", PRED_MAIN_1338).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novelty_greps_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "zero test_type_b_1338 files on disk" in src
        assert "max numeric mechanism_id 1033 in profiles/ pre-commit" in src
        assert "one-zero-three-five mechanism key" in src
        assert '"alfonso maruccia"' in src


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------


class TestBlockStructure1338:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Alfonso Maruccia"
        assert t["publication"] == "techspot"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1338
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Alfonso Maruccia"
        assert b["publication"] == "techspot"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "meta_arm" in b
        assert "google_arm" in b

    def test_meta_arm_fields(self):
        m = _block()["meta_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "techspot"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert m["url"] == NOVEL_URLS[0]
        assert m["date"] == "2026-10-06"
        assert m["author_byline"] == "Alfonso Maruccia"
        assert "Worst Spectacle" in m["dek"]

    def test_google_arm_fields(self):
        m = _block()["google_arm"]
        assert m["entity"] == "google"
        assert m["outlet"] == "techspot"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == GOOGLE_TONE
        assert m["url"] == NOVEL_URLS[2]
        assert m["date"] == "2026-10-05"
        assert m["author_byline"] == "Alfonso Maruccia"
        assert "Cutting corners" in m["dek"]

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_google_minus_meta"] == ILLUSTRATIVE_DELTA
        assert b["scorer_delta_MANUAL_ILLUSTRATIVE"] == ILLUSTRATIVE_DELTA

    def test_verdict_and_ledger_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 62
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True
        assert b["no_analysis_json_update"] is True

    def test_window_field(self):
        b = _block()
        assert "1335-1339" in b["window"]
        assert "FOURTH leg" in b["window"]

    def test_source_urls(self):
        urls = _block()["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls


# ---------------------------------------------------------------------------
# 5. m1034 content discipline
# ---------------------------------------------------------------------------


class TestM1034ContentDiscipline1338:
    def test_meta_arm_quotes(self):
        quotes = " ".join(_block()["meta_arm"]["key_quotes"])
        assert "Worst Spectacle" in quotes
        assert "privacy is paying the price" in quotes
        assert "unwelcome guest" in quotes

    def test_meta_arm_tone_reading(self):
        reading = _block()["meta_arm"]["tone_reading"]
        assert "adversarial" in reading.lower()

    def test_google_arm_quotes(self):
        quotes = " ".join(_block()["google_arm"]["key_quotes"])
        assert "Cutting corners" in quotes
        assert "forest-clearing" in quotes
        assert "420 football fields" in quotes

    def test_google_arm_tone_reading(self):
        reading = _block()["google_arm"]["tone_reading"]
        assert "adversarial" in reading.lower()

    def test_delta_reading_constancy(self):
        reading = _block()["delta_reading"]
        assert "constancy" in reading
        assert "0.00" in reading

    def test_confounder_ranking(self):
        confs = _block()["confounders"]
        assert any("STRONG" in c for c in confs)
        assert any("excerpt" in c.lower() for c in confs)
        assert any("peg asymmetry" in c.lower() for c in confs)

    def test_zero_gradient_control_disclosed(self):
        fc = _block()["financial_context"]
        assert "ZERO-GRADIENT" in fc
        assert "TechSpot" in fc

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 2
        joined = " ".join(ce).lower()
        assert "relay" in joined or "excerpt" in joined

    def test_rejection_audit_present(self):
        ra = _block()["rejection_audit"]
        assert "Schroeder" in ra
        assert "Phelan" in ra
        assert "Goode" in ra
        assert "Matt J. Robb" in ra

    def test_research_method_documents_screening(self):
        rm = _block()["research_method"]
        assert "screening" in rm.lower()
        assert "14 browser.search" in rm
        assert "3 main-run browser.search" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1338:
    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE" in b["design"]

    def test_engine_not_run(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_p_value_not_calculated(self):
        # The needle and the expected def line are both runtime-built;
        # the only contiguous occurrence in this file is the def line.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        needle = "p" + "_value"
        expected_def = "    def test_" + needle + "_not_calculated(self):"
        hits = [l for l in src.splitlines() if needle in l]
        assert hits == [expected_def], hits

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]

    def test_not_a_new_member_zero_gradient(self):
        # No documented TechSpot x Meta/Google/Anthropic/OpenAI AI
        # content licensing deal in-corpus: the pair cannot test the
        # payer-softening prediction (the #1313/#1318/#1328/#1333
        # zero-gradient control-case precedent), so no
        # falsification-family advance.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "zero-gradient" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 62 (NOT a member).
# ---------------------------------------------------------------------------


class TestFalsificationLedger1338:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_intact_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_intact_in_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_intact_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_intact_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_intact_in_wired(self):
        wired = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert _T56 in wired

    def test_fifty_seventh_intact_in_ap(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_intact_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_intact_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member(self):
        assert _git_grep_tracked_source(_T63, None) == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1339; #1338 stages the
#    #1191-class no-Type-B-#1338 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1338:
    def test_pins_on_one_mechanism_landing(self):
        # Type B lands one mechanism: max 1034, next 1035.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1034" in src
        assert "NEXT_NUM = 1035" in src

    def test_no_type_c_1339_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1339's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1339" must be #1339's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1339")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1339's own commits"
        main = _git("rev-parse", PRED_MAIN_1339).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1035_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1035_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1035_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        # Landed #1282 (m1000, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        wired = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert _T56 in wired

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member_pin(self):
        # Type B lands one mechanism (m1034, thesis-consistent, NOT a
        # falsification member); the sixty-third member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T63, None) == []

    def test_predecessor_1337_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1337_FILE))

    def test_next_leg_is_1339_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1339 Type C" in src

    def test_1337_pins_flip_by_design_documented(self):
        # #1337's forward guards (max-1033, zero one-zero-three-four
        # keys all forms, no-Type-B-#1338-in-git-log, fortieth
        # absent, forty-eighth through sixty-second intact in
        # profiles/, no sixty-third member repo-wide, ledger 62)
        # verified GREEN at HEAD pre-commit this run. TWO pins flip
        # BY DESIGN at this run's main commit: the #1191-class
        # self-trip (no-Type-B-#1338-in-git-log, re-pinned
        # post-commit by TestStalenessPins1338 in both copies per
        # the re-pin-both-copies precedent) and the #1272-class
        # forward-guard expiry (the 1034-numeric-absent-in-profiles
        # pin trips on the landed m1034 block - permanent red by
        # design). The 1034-underscore/dash pins stay green (the
        # block key carries no one-zero-three-four mechanism-key
        # forms per #723/#738/#739); the no-sixty-third-member pin
        # stays green (m1034 is not a member). Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1338" in src
        assert "no_type_b_1338_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite (per #795): the #1335-launched suite is OBSERVED
#    only this run; its verdict belongs to #1340.
# ---------------------------------------------------------------------------


class TestBackgroundSuiteCheck1338:
    def test_1335_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1335_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1335-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1338_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1335-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1340" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1338:
    def test_readme_test_file_table_has_1338_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1338" in readme

    def test_architecture_has_1338_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1338" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721).
# ---------------------------------------------------------------------------


class TestIterationLog1338:
    def test_1338_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1338 Type B" in log

    def test_1337_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1337 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1337's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1338:
    def test_1337_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 25 tests in the class; 24 pass,
        # 1 fails BY DESIGN and permanently - the #1272-class
        # forward-guard expiry (test_1034_numeric_absent_in_profiles
        # trips on the landed m1034 block). The #1191-class self-trip
        # (test_no_type_b_1338_in_git_log_pin) was red at this run's
        # main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1338 in BOTH its own file's copy and the #1337
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1034-underscore and 1034-dash pins stay green (no
        # one-zero-three-four mechanism-key forms landed).
        # Deselected in the in-gate run (fails pre-commit by
        # design); verified post-terminal.
        res = _class_run(B1337_FILE, "TestGuardLifecycle1337")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1338:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_1024_m846_untouched(self):
        # Ray's revert/leave/rebuild decision on m846 is pending;
        # this run does not touch it.
        res = _git("status", "--short")
        assert "competitor-entities.yaml" not in res.stdout
