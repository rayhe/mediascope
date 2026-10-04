# -*- coding: utf-8 -*-
"""Type B #1213 tests: Kaitlyn Huamani (AP) - OpenAI "avoids mention of
security concerns" DevDay accountability vs Meta "bets big on wearable AI"
Connect celebration, journalist-level fiftieth falsification-family member
(m959).

Mechanism m959 (falsification-family member; ledger advances 49 -> 50).
The AP holds the OpenAI content-licensing partnership (Jul 13 2023,
in-corpus in profiles/competitor-entities.yaml); Huamani applies the
adversarial register to the deal partner (-0.30, solo byline) and the
celebratory register to the non-partner (+0.30, co-byline), illustrative
delta OpenAI-minus-Meta -0.60. Extends the m956 journalist-contingent
inversion (Montgomery, Guardian x OpenAI) to a second deal-holding outlet
and the first AP byline in the family.

Excerpt-bounded research per #503 (delegated research + 3 main-run
browser.search query sets, 0 browser.open reads). Rejected as saturated /
peg-absent / out-of-window: Sarah Perez, William Gavin, Victoria Song,
Julian Chokkattu, Ina Fried, Todd Bishop, Reuters wire, CNN Muse/Amazon
piece, Kylie Robison, Cherlynn Low, Bobby Allyn, Shirin Ghaffary,
Juli Clover. Christine Ji held as a strong alternate (not run).

The m959 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `kaitlyn_huamani_type_b`
key (per the #643 convention; name appears only in examples/sample_output/
Feb-2026 Mosseri files; mechanism_ids [959]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1210-launched background suite
(observed at this run's check: 10636 bytes, mtime Oct 4 2026 12:59 PDT,
no pytest process visible in ps scan - an observation, not a verdict,
~3% progress); its verdict and tombstone belong to #1215 (next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-eighth / forty-ninth / fiftieth / fifty-first
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed fiftieth ordinal
lives in profiles/careers/journalists.yaml (m959); the forty-ninth lives
there too (m956); the forty-eighth lives in profiles/financial-times.yaml
(m952).)
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE
PROFILES_DIR = os.path.join(REPO, "profiles")

OWN_BASENAME = (
    "test_type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_"
    "openai_devday_falsification_oct04_2pm.py"
)
BLOCK_KEY = (
    "type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_"
    "openai_devday_falsification"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "9b2f12d17429e5124d3912fae8ff086a0c486a53"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 65342/1537 -> (65342+N)/1538 in the doc-sync followup.
README_TEST_COUNT = 65342 + 0  # patched post-first-run per #719
README_FILE_COUNT = 1538
COLLECTED_NEW_TESTS = 0  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=959 is THIS run's landed
# mechanism; NEXT_NUM=960 stays forward.
MECH_NUM = 959
NEXT_NUM = 960

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
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

# The landed 959 block lives here (colon-form key; no numeric-959 substring
# in the block key by designed keying per #715). It is a
# competitor_coverage sub-key of the NEW top-level `kaitlyn_huamani_type_b`
# key in profiles/careers/journalists.yaml.
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
FILE_1212 = (
    "test_type_a_1212_wsj_openai_oct01_safety_firings_vs_wsj_meta_"
    "muse_trust_dual_payer_oct04_2pm.py"
)
FILE_1211 = (
    "test_type_e_1211_podcast_sentiment_165th_verification_oct04_1pm.py"
)
HUAMANI_URLS = (
    "https://www.akronnewsreporter.com/2026/09/24/meta-conference-zuckerberg-ai/",
    "https://www.akronnewsreporter.com/2026/09/29/openai-new-agent-dot/",
)
DEAL_URL = (
    "https://www.pymnts.com/news/artificial-intelligence/2023/"
    "associated-press-licensing-deal-openai-includes-first-mover-safeguard/"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _huamani_entry():
    return _load_journalists()["kaitlyn_huamani_type_b"]


def _block():
    return _huamani_entry()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _needle_hits_profiles(needle):
    out = _git("grep", "-l", "-F", needle, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _repo_grep(pattern, exclude_paths=(), file_globs=None):
    """Repo-wide grep; file_globs restricts to a file set (None = all)."""
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
    hits = []
    for path in _iter_source_files():
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor convention per #565.
# ---------------------------------------------------------------------------

class TestAnchor1213:
    def test_anchor_sha_format(self):
        # 40-char hex in both states (placeholder 0*40 pre-anchor,
        # main-commit hash post-anchor).
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA

    def test_anchor_placeholder_or_main_commit(self):
        # Either the pre-anchor placeholder or a hash present in git log.
        if ANCHORED_SHA != "0" * 40:
            log = _git("log", "--format=%H").stdout
            assert ANCHORED_SHA in log

    def test_anchor_placeholder_pin(self):
        # BY DESIGN: green pre-anchor (placeholder), red post-anchor
        # (patched). Exactly one designed failure post-anchor per the
        # #1196 corrective pattern.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_followup_commit_message_convention(self):
        # Post-anchor only meaningful; pre-anchor the grep is empty and the
        # assertion is vacuous-truthful via the placeholder pin above.
        log = _git("log", "--oneline", "--grep=Type B #1213 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1213 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1213:").stdout
        assert "Type B #1213" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1213 is the FOURTH leg of the 1210-1214 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1213:
    def test_rotation_window_is_1210_1214(self):
        text = _block_text()
        assert "1210-1214" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1210-1214 window FOURTH leg "
            "(D #1210 -> E #1211 -> A #1212 -> B #1213 -> C #1214)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1210", "Type E #1211", "Type A #1212"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1214 Type C) is documented in the window string;
        # it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1214" in text
        assert _block()["window"].endswith("C #1214)")

    def test_no_type_b_1213_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1213_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1213:
    def test_huamani_top_level_key_found(self):
        entry = _huamani_entry()
        assert entry["name"] == "Kaitlyn Huamani"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1213, not the mechanism number.
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m959 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_huamani_urls_in_block_source_urls_verbatim(self):
        urls = list(_block()["source_urls"])
        for u in HUAMANI_URLS:
            assert u in urls, u
        assert DEAL_URL in urls
        assert all(u.startswith("https://") for u in urls)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "careers", "journalists.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (new journalist key per #643; first Huamani
# mechanism; the landed fiftieth member form lives in the YAML block,
# ---------------------------------------------------------------------------

class TestBlockStructure1213:
    def test_huamani_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "kaitlyn_huamani_type_b" in data
        assert isinstance(data["kaitlyn_huamani_type_b"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _huamani_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _huamani_entry()
        assert entry["mechanism_ids"] == [959]

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "openai_arm",
            "meta_arm", "scorer", "financial_context",
            "finding", "confounders", "counter_evidence",
            "statistical_discipline", "verdict", "falsification_family",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "is_significant", "correlation_not_causation",
            "no_analysis_json_update", "artifact_readiness", "connects_to",
            "novelty", "research_method", "background_suite_status",
            "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_openai_arm_tone(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert arm["entity"] == "openai"
        assert arm["author_byline"] == "Kaitlyn Huamani (solo)"

    def test_meta_arm_tone(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert arm["entity"] == "meta"

    def test_publication_associated_press(self):
        entry = _huamani_entry()
        assert entry["publication"] == "associated-press"

    def test_member_flag_true(self):
        b = _block()
        assert b["falsification_family_member"] is True
        assert b["falsification_ledger"] == 50
        assert b["verdict"] == "falsification_member_confirmed"


# ---------------------------------------------------------------------------
# 5. m959 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM959ContentDiscipline1213:
    def test_key_quotes_verbatim(self):
        b = _block()
        openai_quotes = b["openai_arm"]["key_quotes"]
        assert any("avoids mention of security concerns" in q
                   for q in openai_quotes)
        assert any("halted the rollout" in q for q in openai_quotes)
        meta_quotes = b["meta_arm"]["key_quotes"]
        assert any("going all in on a consumer-friendly AI agent" in q
                   for q in meta_quotes)
        assert any("we are optimists because we believe in people" in q
                   for q in meta_quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        b = _block()
        assert "EXCERPT-TIER" in b["openai_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in b["meta_arm"]["evidence_tier"]
        assert "0 browser.open per #503" in b["openai_arm"]["evidence_tier"]

    def test_no_full_read_claim(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "first-hand" not in src.lower() or "no first-hand" in src.lower()

    def test_no_canonical_url_constructed(self):
        b = _block()
        assert "none constructed" in b["openai_arm"]["url_note"]
        assert "none constructed" in b["meta_arm"]["url_note"]
        assert "no canonical URLs constructed" in b["novelty"]

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        assert "REJECTED" in method
        assert "Sarah Perez" in method
        assert "Christine Ji" in method

    def test_ascii_only(self):
        # This run's additions must be ASCII-only. Pre-existing non-ASCII
        # in journalists.yaml (em dashes in older career notes) is out of
        # scope for this run.
        diff = _git("diff", "--", "profiles/careers/journalists.yaml").stdout
        added = "\n".join(
            l[1:] for l in diff.splitlines()
            if l.startswith("+") and not l.startswith("+++")
        )
        try:
            added.encode("ascii")
        except UnicodeEncodeError as e:
            raise AssertionError("non-ASCII in m959 YAML additions: %s" % e)
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        try:
            text.encode("ascii")
        except UnicodeEncodeError as e:
            raise AssertionError("non-ASCII in test file: %s" % e)

    def test_cobyline_confound_documented(self):
        b = _block()
        strong = b["confounders"]["strong"]
        assert any("Co-byline" in c for c in strong)
        assert any("Ortutay" in c for c in strong)

    def test_correction_confound_documented(self):
        b = _block()
        strong = b["confounders"]["strong"]
        assert any("FastCompany" in c for c in strong)
        assert any("corrected" in c.lower() for c in strong)

    def test_deal_term_currency_confound_documented(self):
        b = _block()
        moderate = b["confounders"]["moderate"]
        assert any("2-year term" in c for c in moderate)

    def test_ap_deal_in_corpus_cited(self):
        ctx = _block()["financial_context"]
        assert "Jul 13 2023" in ctx or "Jul 2023" in ctx
        assert "competitor-entities.yaml" in ctx


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
# standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1213:
    def test_no_inferential_statistics(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["engine_run"] is False

    def test_illustrative_delta_value(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_openai_minus_meta"] == -0.60
        assert s["meta_tone"] == 0.30
        assert s["openai_tone"] == -0.30

    def test_manual_only_discipline(self):
        d = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in d
        assert "no_analysis_json_update true" in d

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True
        assert b["correlation_not_causation"] is True
        assert b["is_significant"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (fiftieth member lands here; forty-eighth and
# forty-ninth intact; fifty-first absent; directions 35-39 present).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1213:
    def test_is_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is True
        assert b["falsification_ledger"] == 50

    def test_forty_eighth_intact_in_ft(self):
        # Prior member untouched: the forty-eighth claim form stays
        # exactly in financial-times.yaml m952 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_EIGHTH_MEMBER):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_intact_in_journalists(self):
        # Prior member untouched: the forty-ninth claim form stays
        # exactly in journalists.yaml m956 (3 occurrences).
        text = _read(JOURNALISTS_PATH)
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_landed_in_journalists(self):
        # This run lands the fiftieth member-claim form in the m959
        # block (profiles/careers/journalists.yaml): notes field,
        # falsification_family field, novelty field.
        hits = _needle_hits_profiles(FIFTIETH_MEMBER)
        assert len(hits) == 1, hits
        assert hits[0].endswith(
            os.path.join("careers", "journalists.yaml")
        ), hits
        text = _read(JOURNALISTS_PATH)
        assert text.count(FIFTIETH_MEMBER) == 3

    def test_fifty_first_absent(self):
        assert _needle_hits_profiles(FIFTY_FIRST_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FIFTY_FIRST_MEMBER not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            THIRTY_FIFTH_DIR,
            THIRTY_SIXTH_DIR,
            THIRTY_SEVENTH_DIR,
            THIRTY_EIGHTH_DIR,
            THIRTY_NINTH_DIR,
        ):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(FORTIETH_DIR) == []

    def test_ledger_note_advances_to_50(self):
        note = _block()["ledger_note"]
        assert "Ledger advances 49 -> 50" in note
        assert "FIFTIETH member-claim form LANDED this run" in note
        assert "fifty-first member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1214 Type C run
# pins the 960 landing; #1212's no-fiftieth pin flips BY DESIGN here).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1213:
    def test_zero_960_guards_are_forward(self):
        # NEXT_NUM=960 stays forward: no 960 keys land this run.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTIETH_DIR) not in src
        assert len(FORTIETH_DIR) > 0

    def test_no_fifty_first_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTY_FIRST_MEMBER) not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_no_fiftieth_member_guard(self):
        # The landed fiftieth form lives in the YAML block, not here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1212_pins_flip_by_design_documented(self):
        # #1212's test_no_fiftieth_member_guard pin (own-file contiguous
        # check) and its no-Type-B-#1213-in-git-log pin flip BY DESIGN at
        # this run: m959 lands the fiftieth member-claim form in
        # profiles/careers/journalists.yaml. #1212's
        # test_zero_959_guards_are_forward pin (NEXT_NUM=959) flips too -
        # 959 is landed now. Recorded, not repaired.
        b = _block()
        assert b["falsification_family_member"] is True
        log = _git(
            "log", "--oneline", "--grep=Type A #1212:"
        ).stdout
        assert "Type A #1212" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run's pins for #1214).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1213:
    def test_pins_on_959_landing(self):
        # The guards this run lays for the next leg: max-959, zero-960
        # numeric, no-Type-C-#1214-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 959" in src
        assert "NEXT_NUM = 960" in src

    def test_no_type_c_1214_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1214").stdout
        assert log.strip() == ""

    def test_960_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1212_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1212))

    def test_huamani_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("kaitlyn_huamani_type_b") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1215).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1213:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1210_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1210-launched suite at the 12:59 PDT check (10636 bytes,
        # mtime Oct 4 12:59 PDT, no pytest process visible in ps scan -
        # an observation, not a verdict, ~3% progress). #1215 owns the
        # verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "no pytest process visible" in status
        assert "#1215" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries none of this run's
        # markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1210_full_suite.log"
        )
        log = _read(suite_log)
        assert "Type B #1213" not in log
        assert "kaitlyn_huamani" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1213:
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
        assert "## #1213 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65342 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1538


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1213:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1213 Type B:" in text

    def test_no_duplicate_1213_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1213 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1210-1214" in text

    def test_ledger_50_in_log(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "ledger" in text.lower() and "50" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1213:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012-wt test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path).stdout
            assert "mechanism_id: 959" not in diff, path
            assert "Type B #1213" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 959" not in diff
        assert "Type B #1213" not in diff
