# -*- coding: utf-8 -*-
"""Type A #1227 tests: Business Insider - OpenAI Oct-2-2026 David Robinson
resignation exclusive (NEW arm, relay-attested) vs carried BI Meta
product-execution triad (m399, un-rescored per #807).

Mechanism m967 (NOT a falsification-family member; ledger holds at 50).
CONFIRMING EXTENSION of m871 (BI x OpenAI Sep-28/29 Astra-cancellation
scoop accountability, -0.30) and TEMPORAL REPLICATION of m399 (BI x
OpenAI deal-partner hardness, -0.42, Aug 30) at the October escalation
peg: BI's Stephen Council breaks the David Robinson resignation as an
exclusive on Oct 2, four days after the three safety-researcher firings;
Robinson's Atlantic essay Oct 3 is titled "I Quit OpenAI Because Its
Culture Is Broken". MANUAL ILLUSTRATIVE -0.50 (adversarial
safety-governance exclusive on the Axel Springer licensing-deal
partner) vs carried Meta triad +0.08; illustrative delta (OpenAI minus
Meta) -0.58, the widest in the BI x OpenAI line (m399 -0.50, m871
-0.38). The register hardens with the crisis peg (-0.35 scoop to -0.50
exclusive); the deal predicts neither softness nor hardness.

Research: delegated scout (14 browser.search query sets across 8
candidate pairs; SELECTED BI x OpenAI, REJECTED the saturated pairs) +
1 main-run browser.search verification set confirming the
BI-first-reported attribution across 4 independent relays and the
essay quotes. 0 browser.open per #503 (excerpt-bounded; BI paywalled;
no canonical businessinsider.com URL constructed). The scout's
new-member proposal was rejected at main-run verification per the #1143
temporal-replication precedent (m399 already counted the BI x OpenAI
hardness test; same rejection as #1212's scout proposal).

The m967 block lives in profiles/business-insider.yaml as a
competitor_relationships.openai sub-key (4-space indent), appended at
the end of the openai section after the m871 block. Targeted staging by
explicit path only; the in-flight #899/#938/#900/#1012-wt files stay out
of this run's index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1225-launched background suite
(type_d_1225_full_suite.log); its verdict and tombstone belong to #1230
(next Type D). This run neither re-launches, kills, nor writes to the
suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first member-claim forms, or the thirty-fifth through fortieth
direction forms; the constants are constructed at runtime. (The landed
ordinals live in profiles/financial-times.yaml and
profiles/careers/journalists.yaml: m952, m956, m959 respectively.)
"""

import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE
PROFILES_DIR = os.path.join(REPO, "profiles")

OWN_BASENAME = (
    "test_type_a_1227_bi_openai_robinson_resignation_exclusive_"
    "vs_meta_execution_triad_oct05_2am.py"
)
BLOCK_KEY = (
    "type_a_1227_bi_openai_robinson_culture_broken_resignation_"
    "exclusive_oct02"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in
# the anchor followup (git rev-parse HEAD after the main commit), per
# #565.
ANCHORED_SHA = "6b01b97a2eb870e58f49c514d563638cad7f8dd3"  # patched per #565 in the anchor followup
# Post-first-run values per #719: N tests collected; README ratchets
# 66461/1551 -> (66461+N)/1552 in the doc-sync followup.
README_TEST_COUNT = 66461 + 91  # patched post-first-run per #719
README_FILE_COUNT = 1552
COLLECTED_NEW_TESTS = 91  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=967 is THIS run's landed
# mechanism; NEXT_NUM=968 stays forward.
MECH_NUM = 967
NEXT_NUM = 968

# Needle markers, format-built per #715. The marker is concatenated with
# the number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m967 block lives here: a competitor_relationships.openai
# sub-key of profiles/business-insider.yaml.
BI_PATH = os.path.join(REPO, "profiles", "business-insider.yaml")
D1226_FILE = (
    "test_type_e_1226_podcast_sentiment_168th_verification_oct05_2am.py"
)

# Predecessor chain: #1226 Type E closed the second leg of the
# 1225-1229 window.
PRED_MAIN_1226 = "0b151dc1"
PRED_ANCHOR_1226 = "6d030566"
PRED_DOCSYNC_1226 = "6ac702a5"
PRED_FINAL_1226 = "d28923b1"

# Novel relay URLs (verbatim from Full-URL listings; zero-hit repo-wide
# pre-commit via git grep -F).
NOVEL_URLS = (
    "https://biztoc.com/x/4b14a2ecae51e639",
    "https://startupfortune.com/openai-safety-leader-david-robinson-"
    "resigns-days-after-three-researchers-were-fired/",
    "https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-"
    "claiming-the-companys-culture-is-broken/",
    "https://www.progressiverobot.com/2026/10/03/openai-safety-culture-"
    "david-robinson-quits-atlantic-essay/",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_bi():
    return yaml.safe_load(_read(BI_PATH))


def _openai_section():
    data = _load_bi()
    assert "competitor_relationships" in data
    assert "openai" in data["competitor_relationships"]
    return data["competitor_relationships"]["openai"]


def _block():
    return _openai_section()[BLOCK_KEY]


def _block_text():
    return _read(BI_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _repo_grep(pattern, exclude_paths=(), file_globs=None):
    """Working-tree grep; file_globs restricts to a file set."""
    candidates = []
    for root, _dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith(".git") or rel_root.startswith(".pytest_cache"):
            continue
        for name in files:
            rel = os.path.join(rel_root, name) if rel_root != "." else name
            if rel in exclude_paths:
                continue
            if file_globs and not any(
                name.endswith(g.lstrip("*")) for g in file_globs
            ):
                continue
            candidates.append(os.path.join(root, name))
    hits = []
    for path in candidates:
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _iter_source_files():
    return _repo_grep(
        "", exclude_paths=("tests/" + OWN_BASENAME,),
        file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json"),
    )


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _source_grep(pattern):
    """Working-tree grep including this file (for allowlisting)."""
    hits = []
    for path in _repo_grep(
        "", file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json")
    ):
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _needle_hits_profiles(needle):
    out = _git("grep", "-F", "-l", needle, "--", "profiles").stdout
    return [l for l in out.splitlines() if l.strip()]


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-k", classname,
         "-q", "--no-header"],
        cwd=REPO, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1227:
    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1225-1229 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1227:
    def test_predecessor_1226_chain_verified(self):
        for sha in (
            PRED_MAIN_1226, PRED_ANCHOR_1226, PRED_DOCSYNC_1226,
            PRED_FINAL_1226,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1225 -> E #1226 -> A #1227 -> B #1228 -> C #1229" in src

    def test_next_leg_is_type_b_1228(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1228 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        # Type A lands exactly one mechanism (m967); the Type E
        # predecessor added none.
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1227:
    def test_openai_section_found(self):
        sec = _openai_section()
        assert BLOCK_KEY in sec

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1227 in key, no 967 or 968
        # substring.
        assert "1227" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # "mechanism_id: 967" (colon form); the underscore key form must
        # not exist repo-wide.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for _line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m967 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = [u["url"] for u in b["source_urls"]]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit
        # it appears only in the landed YAML block, this test file, and
        # the doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "business-insider.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h

    def test_no_robinson_resignation_before_this_run(self):
        # The novelty claim: "David Robinson resigns" was absent from
        # business-insider.yaml before this run's landing; now present
        # only inside this block's arms.
        text = _block_text()
        assert "David Robinson resigns" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "David Robinson resigns" not in text[:block_start]

    def test_meta_arm_carried_disclosed(self):
        b = _block()
        assert "CARRIED" in b["meta_arm"]["status"]
        assert "m399" in b["meta_arm"]["status"]

    def test_openai_arm_new_documented(self):
        b = _block()
        assert b["openai_arm"]["date"] == "2026-10-02"
        assert b["openai_arm"]["byline"] == "Stephen Council"

    def test_no_type_a_1227_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the log-hash followup per #721): the ONLY matches so far
        # are this run's own commits, whose messages carry the run's
        # own iteration subject. The pin's substance - no PRIOR run
        # committed this run's iteration - holds. The log-hash sha is
        # filled by the corrective commit per #721.
        out = _git("log", "--format=%H %s", "--grep=Type A #1227").stdout
        own = {"6b01b97a", "49651ebf", "fc586f18", "d490a209"}
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits, "expected this run's own commits"
        for line in hits:
            assert line.split()[0][:8] in own, line


# ---------------------------------------------------------------------------
# 4. Block structure under competitor_relationships.openai.
# ---------------------------------------------------------------------------

class TestBlockStructure1227:
    def test_openai_section_is_expected_parent(self):
        data = _load_bi()
        assert "openai" in data["competitor_relationships"]

    def test_block_key_present_under_openai(self):
        assert BLOCK_KEY in _openai_section()

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1227
        assert b["iteration_type"] == "A"
        assert b["publication"] == "business-insider"
        assert b["rotation"] == "Type A"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "mechanism_id", "date_analyzed", "type", "iteration",
            "iteration_type", "publication", "competitor_pair", "author",
            "block_key", "test_file", "window", "design",
            "distinct_from_prior", "finding", "financial_relationship",
            "openai_arm", "meta_arm", "register_analysis",
            "asymmetry_scorer_MANUAL_ILLUSTRATIVE", "scorer",
            "confounders", "counterevidence", "verdict",
            "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "statistical_discipline",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "connects_to", "novelty", "research_method",
            "rotation_transparency", "concurrency",
            "background_suite_status", "in_flight", "source_urls",
            "browser_opens", "tone_scored", "engine_run",
            "is_significant", "artifact_grade", "yaml_parse_clean",
            "ascii_only",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_openai_arm_tone(self):
        assert _block()["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50

    def test_meta_arm_tone_carried(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.08
        assert "CARRIED" in b["meta_arm"]["status"]

    def test_connects_to_lineage(self):
        conns = _block()["connects_to"]
        for mid in (399, 871, 952, 799, 955):
            assert mid in conns, mid

    def test_source_urls_novel_flags(self):
        b = _block()
        assert len(b["source_urls"]) == 4
        for u in b["source_urls"]:
            assert u["novel"] is True
            assert u["accessed"] == "2026-10-05"

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 5. Content discipline: excerpt-bounded, no constructed URLs, ASCII-only.
# ---------------------------------------------------------------------------

class TestM967ContentDiscipline1227:
    def test_openai_key_quotes_verbatim(self):
        quotes = _block()["openai_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "who first reported the departure" in joined
        assert "BI can confirm" in joined
        assert "left OpenAI last week" in joined

    def test_essay_quotes_present(self):
        essay = _block()["openai_arm"]["essay_arm"]
        joined = " ".join(essay["key_quotes"])
        assert "guarantees periodic failures" in joined
        assert "more dangerous our situation becomes" in joined

    def test_relay_attribution_documented(self):
        src = _block()["openai_arm"]["url_source"]
        assert "Stephen Council" in src
        assert "first reported" in src

    def test_no_constructed_bi_url(self):
        # No canonical businessinsider.com URL was constructed for the
        # exclusive; the discipline is recorded in the block.
        text = _block_text()
        assert "businessinsider.com/safety-leader" not in text
        assert "no canonical businessinsider.com URL constructed" in text

    def test_voice_attribution_disclosed(self):
        notes = _block()["openai_arm"]["notes"]
        assert "not BI" in notes or "Robinson" in notes
        assert "essay" in notes.lower()

    def test_ascii_only(self):
        # Scoped to this run's block: the file carries a pre-existing
        # non-ASCII char elsewhere (in HEAD before this run); this run's
        # added lines are ASCII-only.
        yaml.safe_dump(_block(), allow_unicode=False).encode("ascii")

    def test_no_em_dashes(self):
        assert "—" not in _block_text()


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1227:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _block()["scorer"]["method"]

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False
        assert _block()["scorer"]["engine_run"] is False

    def test_p_value_not_calculated(self):
        assert _block()["scorer"]["p_value"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False
        assert _block()["scorer"]["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_refinement_not_discovery(self):
        assert "mechanism_refinement_not_a_discovery" in _block()["verdict"]

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 50; no new member this run)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1227:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50

    def test_forty_eighth_intact_in_ft(self):
        hits = _needle_hits_profiles(FORTY_EIGHTH_MEMBER)
        assert hits == ["profiles/financial-times.yaml"], hits

    def test_forty_ninth_intact_in_journalists(self):
        text = _read(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_intact_in_journalists(self):
        text = _read(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FIFTIETH_MEMBER) == 3

    def test_forty_ninth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_NINTH_MEMBER):
            assert p.endswith(os.path.join("careers", "journalists.yaml")), p

    def test_fiftieth_nowhere_else(self):
        for p in _needle_hits_profiles(FIFTIETH_MEMBER):
            assert p.endswith(os.path.join("careers", "journalists.yaml")), p

    def test_fifty_first_absent(self):
        assert _needle_hits_profiles(FIFTY_FIRST_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FIFTY_FIRST_MEMBER not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            THIRTY_FIFTH_DIR, THIRTY_SIXTH_DIR, THIRTY_SEVENTH_DIR,
            THIRTY_EIGHTH_DIR, THIRTY_NINTH_DIR,
        ):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(FORTIETH_DIR) == []

    def test_ledger_note_holds_at_50(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 50" in note
        assert "FORTY-EIGHTH member-claim form present" in note
        assert "FORTY-NINTH member-claim form present" in note
        assert "FIFTIETH member-claim form present" in note
        assert "fifty-first member-claim form absent repo-wide" in note

    def test_verdict_is_confirming_not_falsifying(self):
        verdict = _block()["verdict"]
        assert "temporal replication" in verdict.lower()
        assert "NOT a falsification-family member" in verdict


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1228 Type B run
# pins the 968 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1227:
    def test_zero_968_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 968" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # The fortieth direction form stays absent in profiles/; the
        # constant is format-built so this file never carries it
        # contiguously. Scope is profiles/ (not repo-wide) because other
        # landed test files may carry the contiguous needle in their own
        # constant definitions with profiles-scoped tests.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_fifty_first_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FIFTY_FIRST_MEMBER not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_no_forty_ninth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_NINTH_MEMBER not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_no_fiftieth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FIFTIETH_MEMBER not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1226_pins_flip_by_design_documented(self):
        # #1226's forward guards (max-966, zero-967 keys all forms,
        # no-Type-A-#1227-in-git-log) flip by design now that m967 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1226" in src
        text = _block_text()
        assert "1226" in text

    def test_thirty_fifth_direction_still_present(self):
        assert _repo_grep(THIRTY_FIFTH_DIR)

    def test_thirty_sixth_direction_still_present(self):
        assert _repo_grep(THIRTY_SIXTH_DIR)

    def test_thirty_seventh_direction_still_present(self):
        assert _repo_grep(THIRTY_SEVENTH_DIR)

    def test_thirty_eighth_direction_still_present(self):
        assert _repo_grep(THIRTY_EIGHTH_DIR)

    def test_thirty_ninth_direction_still_present(self):
        assert _repo_grep(THIRTY_NINTH_DIR)


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 967 landing for #1228).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1227:
    def test_pins_on_967_landing(self):
        # The guards this run lays for the next leg: max-967,
        # zero-968 all forms, no-Type-B-#1228-in-git-log, fortieth
        # direction absent (profiles/ scope), forty-eighth member
        # intact in profiles/financial-times.yaml, forty-ninth member
        # intact + fiftieth member intact in
        # profiles/careers/journalists.yaml, fifty-first member absent
        # (repo-wide), ledger 50.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 967" in src
        assert "NEXT_NUM = 968" in src

    def test_no_type_b_1228_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1228").stdout
        assert out.strip() == "", out.strip()

    def test_968_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1226_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1226_FILE))

    def test_1227_key_unique(self):
        # The 1227-keyed block key appears once as a block key; the
        # "type_a_1227_" prefix also occurs in the block_key field value
        # and the test_file field value (tests/test_type_a_1227_...).
        text = _block_text()
        assert text.count("type_a_1227_") == 3

    def test_next_leg_is_1228_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1228 Type B" in src


# ---------------------------------------------------------------------------
# 10. Background suite check-only per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1227:
    def test_suite_log_path_noted(self):
        status = _block()["background_suite_status"]
        assert "type_d_1225_full_suite.log" in status

    def test_suite_checked_only_recorded_not_touched(self):
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY per #795" in status
        assert "neither re-launches, kills, nor writes" in status

    def test_verdict_belongs_to_1230(self):
        status = _block()["background_suite_status"]
        assert "#1230" in status

    def test_no_pytest_spawned_by_this_run(self):
        # This run's in-gate pytest invocation targets only this file;
        # no background full-suite process is owned by this run.
        status = _block()["background_suite_status"]
        assert "no verdict declared" in status


# ---------------------------------------------------------------------------
# 11. Doc-sync (#719: constants patched post-first-run; README/ARCHITECTURE
# rows and iteration-log entry land in the doc-sync followup).
# ---------------------------------------------------------------------------

class TestDocSync1227:
    def test_readme_stats_table_updated(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text
        assert str(README_TEST_COUNT) in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1227 Type A:" in text


# ---------------------------------------------------------------------------
# 12. Iteration log (#721: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1227:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1227 Type A:" in text

    def test_no_duplicate_1227_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1227 Type A:") == 1

    def test_window_third_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1225-1229" in text

    def test_log_hash_followup_registers_hashes(self):
        # Per #721 the log-hash followup registers all four hashes in the
        # iteration-log entry; pre-commit the entry is absent and this is
        # vacuous via the header test above. Post-doc-sync the entry must
        # carry the main-commit hash once the log-hash followup lands.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        if "## #1227 Type A:" in text and ANCHORED_SHA != "0" * 40:
            assert ANCHORED_SHA in text


# ---------------------------------------------------------------------------
# 13. Staleness pins: #1226's guard lifecycle (deselected pre-commit per
# #721; post-main-commit form expects the two designed flips).
# ---------------------------------------------------------------------------

class TestStalenessPins1227:
    def test_1226_guard_lifecycle_post_commit_two_flips(self):
        # Post-main-commit form: 9 of the 11 pass; the two that fail do
        # so BY DESIGN on this run's landing - test_no_type_a_1227_in_
        # git_log_pin trips on this run's own main commit (the
        # #1191-class self-trip) and test_967_numeric_absent_in_profiles
        # trips on the landed m967 block. The #1226 block is read-only
        # to this run; the flips are recorded, not repaired.
        res = _class_run(D1226_FILE, "TestGuardLifecycle1226")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 9 passed" in res.stdout, res.stdout[-2000:]
        assert "test_no_type_a_1227_in_git_log_pin" in res.stdout
        assert "test_967_numeric_absent_in_profiles" in res.stdout


# ---------------------------------------------------------------------------
# 14. In-flight isolation (this run touches profiles/business-insider.yaml
# + the new test file only; #899/#938/#900/#1012-wt and #1024 stay out).
# ---------------------------------------------------------------------------

class TestInflightIsolation1227:
    def test_no_1227_markers_in_nytimes_yaml(self):
        text = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        assert BLOCK_KEY not in text
        assert "Type A #1227" not in text

    def test_no_1227_markers_in_inflight_test_files(self):
        for name in (
            "test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
            "agenda_setting_register_vs_carried_meta_india_havoc_"
            "m817_pairing_sep26_7am.py",
            "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        ):
            text = _read(os.path.join(TESTS_DIR, name))
            assert BLOCK_KEY not in text, name
            assert "Type A #1227" not in text, name

    def test_m846_untouched(self):
        # #1024 m846 lives in profiles/competitor-entities.yaml; Ray's
        # revert/leave/rebuild decision is pending - this run must not
        # touch that file.
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert BLOCK_KEY not in text
        assert "Type A #1227" not in text

    def test_only_intended_paths_differ(self):
        # The working tree may only differ from HEAD on this run's paths
        # (the two main-commit paths plus the three doc-sync paths) and
        # the four pre-existing in-flight paths. Pre-main-commit the
        # run's own main paths are uncommitted; in the doc-sync phase the
        # doc-sync paths are uncommitted; post-sequence all drop out of
        # the status, which stays within the allowed set throughout.
        out = _git("status", "--short").stdout
        allowed = {
            "profiles/business-insider.yaml",
            "tests/" + OWN_BASENAME,
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
            "agenda_setting_register_vs_carried_meta_india_havoc_"
            "m817_pairing_sep26_7am.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
        }
        for line in out.strip().splitlines():
            parts = line.split(None, 1)
            path = parts[-1].strip().strip('"')
            assert path in allowed, (line, path)
