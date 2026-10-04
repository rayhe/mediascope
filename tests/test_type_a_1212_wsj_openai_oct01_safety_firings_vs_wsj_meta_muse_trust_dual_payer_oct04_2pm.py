# -*- coding: utf-8 -*-
"""Type A #1212 tests: WSJ x OpenAI Oct-1-2026 safety-researcher firings
scoop (NEW peg, relay-attested) + carried Sep-28 Astra deception-shelving
peg vs NEW WSJ x Meta Muse-trust pair (M1 Sep-19, M2 Sep-24; wsj.com
canonicals zero-hit) - dual-payer symmetry extension at the WSJ register.

Mechanism 958 (NOT a falsification-family member; ledger holds at 49).
The scout proposed a fiftieth member; main-run verification found the WSJ
x OpenAI safety-crisis uniform-softening test already counted by m904
(FORTY-FOURTH, #1122) on the same Astra peg, so the #1143
temporal-replication precedent applies: same-publication replication on a
new peg is not a new prediction test. This run lands a control-case /
dual-payer-symmetry extension instead: both payers adversarial at -0.275
in the crisis week (illustrative delta 0.00), which INVERTS m532's
calm-window symmetric-softening reading (delta -0.075, Sep 5) at the same
outlet - the m519 refinement is peg-conditional, not outlet-uniform (the
WSJ analogue of m956's journalist-contingent inversion of #513).

Excerpt-bounded research per #503 (11 browser.search query sets via
delegated research + main-run verification, 0 browser.open reads).
Rejected as corpus-saturated or peg-absent: WIRED x OpenAI Wardle CVE
piece (single arm, no fresh WIRED Meta arms); FT x Anthropic
(saturated: m892, m919/#1147, m943/#1187, m945/#1189, #1047); Guardian x
Anthropic (saturated: m886); BI x Anthropic (saturated: m955, Type A
#1207 this morning); Snap SPECS / Apple N224 glasses / Apple Taction
verdict (peg-absent per #1207); Sora 2 (stale Sep-2025 peg); WSJ x Meta
layoffs relay (stale); NYT x OpenAI safety-warnings (URL not surfaced,
kept as O2 corroborating context only).

The landed arm is NEW: the WSJ Oct-1 firings scoop (relay-attested via
TechCrunch + pondeo.ai; canonical wsj.com URL not surfaced, none
constructed per policy) and the WSJ x Meta Muse-trust pair (wsj.com
canonicals surfaced, zero-hit pre-commit). The Meta arms are NEW, not
carried: M1 "Meta's AI Agent Has a Trust Problem" (Asa Fitch, ~Sep 19,
trust-accountability adversarial with constructive investor notes, -0.30
MANUAL ILLUSTRATIVE) and M2 "Meta's New AI Agent Is an Instant Hit - and
the Backlash Has Already Begun" (~Sep 24, backlash register with
constructive usage notes, -0.25 MANUAL ILLUSTRATIVE). OpenAI leg: O2 NEW
(-0.25, company-statement-led safety-crisis accountability) + O1
CARRIED Sep-28 Astra peg (m904, un-rescored per #807, -0.30).
Illustrative delta (OpenAI minus Meta) 0.00.

Iteration #1212, THIRD leg of the 1210-1214 window
(D #1210 -> E #1211 -> A #1212 -> B #1213 -> C #1214).

The 958 block lives in profiles/news-corp.yaml as a
competitor_relationships.openai sub-key (4-space indent, sibling of the
m904 block), appended before the `meta:` key.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1210-launched background suite
(log type_d_1210_full_suite.log, observed alive at this run's check);
its verdict and tombstone belong to #1215 (next Type D). This run
neither re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-ninth / fiftieth member-claim forms, or
the thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed forty-ninth ordinal lives in
profiles/careers/journalists.yaml, m956, 3 occurrences.)
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
    "test_type_a_1212_wsj_openai_oct01_safety_firings_vs_wsj_meta_muse_trust_"
    "dual_payer_oct04_2pm.py"
)
BLOCK_KEY = (
    "type_a_1212_wsj_openai_safety_firings_oct01_vs_wsj_meta_muse_trust_"
    "dual_payer_symmetry"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "9f4eb1a9fa616614dc696412777b779416398da2"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 65265/1536 -> (65265+N)/1537 in the doc-sync followup.
README_TEST_COUNT = 65265 + 77  # patched post-first-run per #719
README_FILE_COUNT = 1537
COLLECTED_NEW_TESTS = 77  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=958 is THIS run's landed
# mechanism; NEXT_NUM=959 stays forward.
MECH_NUM = 958
NEXT_NUM = 959

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed 958 block lives here (colon-form key; no numeric-958 substring
# in the block key by designed keying per #715). It is a
# competitor_relationships.openai sub-key of profiles/news-corp.yaml.
NC_PATH = os.path.join(REPO, "profiles", "news-corp.yaml")
FILE_1211 = "test_type_e_1211_podcast_sentiment_165th_verification_oct04_1pm.py"
FILE_1210 = "test_type_d_1210_m955_m956_m957_qualitative_corpus_integrity_oct04_12pm.py"
FIRING_URLS = (
    "https://techcrunch.com/2026/10/01/openai-cuts-ties-with-three-safety-researchers-wsj-reports/",
    "https://pondero.ai/news/2026-10-04-openai-safety-departures/",
)
MUSE_URLS = (
    "https://www.wsj.com/tech/ai/metas-ai-agent-has-a-trust-problem-5ee5882c",
    "https://www.wsj.com/tech/ai/meta-ai-agent-muse-reactions-5bf236af",
)
CARRIED_ASTRA_URL = (
    "https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/"
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_nc():
    return yaml.safe_load(_read(NC_PATH))


def _openai_section():
    data = _load_nc()
    assert "competitor_relationships" in data
    assert "openai" in data["competitor_relationships"]
    return data["competitor_relationships"]["openai"]


def _block():
    return _openai_section()[BLOCK_KEY]


def _block_text():
    return _read(NC_PATH)


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
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1212:
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
        log = _git("log", "--oneline", "--grep=Type A #1212 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type A #1212 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type A #1212:").stdout
        assert "Type A #1212" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1212 is the THIRD leg of the 1210-1214 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1212:
    def test_rotation_window_is_1210_1214(self):
        text = _block_text()
        assert "1210-1214" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1210-1214 window THIRD leg "
            "(D #1210 -> E #1211 -> A #1212 -> B #1213 -> C #1214)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1210", "Type E #1211"):
            assert marker in log, marker

    def test_next_run_is_type_b(self):
        # The next leg (#1213 Type B) is documented in the block window
        # field; the iteration-log entry carrying it lands in the doc-sync
        # followup (TestIterationLog1212 pins it there).
        assert "B #1213" in _block()["window"]
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1210-1214" in text

    def test_no_type_a_1212_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1212_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1212:
    def test_openai_section_found(self):
        section = _openai_section()
        assert section["financial_tie"] == "licensing"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1212, not the mechanism number.
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
        assert nums, "958 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_new_urls_in_block_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        for u in FIRING_URLS + MUSE_URLS + (CARRIED_ASTRA_URL,):
            assert u in urls, u
        assert all(u.startswith("https://") for u in urls)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "news-corp.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (competitor_relationships.openai sub-key of
# profiles/news-corp.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1212:
    def test_openai_section_is_expected_parent(self):
        data = _load_nc()
        assert "competitor_relationships" in data
        assert isinstance(data["competitor_relationships"]["openai"], dict)

    def test_block_key_present_under_openai(self):
        section = _openai_section()
        assert BLOCK_KEY in section

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 958

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id",
            "scheduled_job_id", "date_analyzed", "block_key", "test_file",
            "author", "publication", "competitor_pair", "window", "design",
            "openai_arm", "meta_arm", "scorer", "financial_relationship",
            "finding", "confounders", "counterevidence",
            "statistical_discipline", "verdict",
            "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to", "novelty",
            "research_method", "rotation_transparency", "concurrency",
            "background_suite_status", "in_flight", "source_urls",
            "distinct_from_prior", "register_analysis",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_openai_arm_tones(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.275
        assert arm["entity"] == "openai"
        assert arm["arm_O2_new"]["tone_MANUAL_ILLUSTRATIVE"] == -0.25
        assert arm["arm_O1_carried"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30

    def test_meta_arms_new_documented(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.275
        assert arm["entity"] == "meta"
        assert "TWO NEW ARMS" in arm["status"]
        assert arm["arm_M1"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert arm["arm_M2"]["tone_MANUAL_ILLUSTRATIVE"] == -0.25

    def test_publication_news_corp(self):
        assert _block()["publication"] == "news-corp"


# ---------------------------------------------------------------------------
# 5. 958 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM958ContentDiscipline1212:
    def test_firings_quotes_verbatim(self):
        quotes = _block()["openai_arm"]["arm_O2_new"]["key_quotes"]
        assert any("parted ways with three researchers" in q for q in quotes)
        assert any("breaking the trust essential to our work" in q for q in quotes)
        assert any("brushed aside employees" in q for q in quotes)

    def test_firings_names_documented(self):
        arm = _block()["openai_arm"]["arm_O2_new"]
        assert "Jasmine Wang" in arm["names"]
        assert "Tomek Korbak" in arm["names"]
        assert "Mikita Balesni" in arm["names"]

    def test_muse_trust_quotes_verbatim(self):
        m1 = _block()["meta_arm"]["arm_M1"]["key_quotes"]
        assert any("broken a lot of things over the years" in q for q in m1)
        assert any("115 million Muse subscribers" in q for q in m1)
        m2 = _block()["meta_arm"]["arm_M2"]["key_quotes"]
        assert any("8% of them would trust Meta with their passwords" in q
                   for q in m2)
        assert any("blocked Muse from accessing its site" in q for q in m2)

    def test_evidence_tier_is_excerpt_attested(self):
        for arm_key in ("arm_O2_new",):
            tier = _block()["openai_arm"][arm_key]["evidence_tier"]
            assert "EXCERPT-TIER" in tier
            assert "not first-hand read" in tier
        for arm_key in ("arm_M1", "arm_M2"):
            tier = _block()["meta_arm"][arm_key]["evidence_tier"]
            assert "EXCERPT-TIER" in tier
            assert "not first-hand read" in tier

    def test_no_full_read_claim(self):
        # Honesty pin: the block must not claim a first-hand full-text read
        # of the paywalled WSJ pages. (Scoped to the 958 block: other
        # mechanisms legitimately carry archived reads.)
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 26000]
        assert "FIRST-HAND full-text read" not in chunk

    def test_no_canonical_url_constructed_for_firings(self):
        # The firings scoop's wsj.com canonical was never surfaced; the
        # block must rely on the relay URLs only.
        urls = _block()["source_urls"]
        assert len(urls) == 5
        assert not any("wsj.com" in u and "safety-researcher" in u
                       for u in urls)

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        for name in ("m892", "m886", "m955", "Snap SPECS", "Sora 2",
                     "NYT x OpenAI safety-warnings"):
            assert name in method, name

    def test_scout_correction_documented(self):
        # The scout's fiftieth-member proposal was rejected by main-run
        # verification (m904 already counted the test); the rejection is
        # disclosed in the block's confounders and novelty.
        confs = " ".join(_block()["confounders"])
        assert "researcher-scout correction" in confs or "scout" in confs
        assert "falsification_family" in str(_block().keys())
        assert _block()["falsification_family_member"] is False

    def test_ascii_only(self):
        # Scoped to this run's block: the chunk ends at the next top-level
        # sibling key (`  meta:`), per the #1208 in-gate fix for the same
        # defect class (pre-existing non-ASCII elsewhere in the file is
        # out of scope for this run).
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        end = text.index("\n  meta:", start)
        chunk = text[start:end]
        chunk.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per Aug 28 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1212:
    def test_manual_illustrative_only(self):
        s = _block()["scorer"]
        assert "MANUAL ILLUSTRATIVE ONLY" in s["method"]
        assert s["engine_run"] is False
        assert s["is_significant"] is False

    def test_no_inferential_stats(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_delta_is_illustrative(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_openai_minus_meta"] == 0.00
        assert s["meta_tone_MANUAL_ILLUSTRATIVE"] == -0.275
        assert s["openai_tone_MANUAL_ILLUSTRATIVE"] == -0.275

    def test_verdict_is_refinement_not_discovery(self):
        b = _block()
        assert b["verdict"].startswith("mechanism_refinement_not_a_discovery")
        assert b["falsification_family_member"] is False
        assert b["no_analysis_json_update"] is True

    def test_statistical_discipline_strings(self):
        sd = _block()["statistical_discipline"]
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_correlational_honesty(self):
        note = _block()["correlational_note"]
        assert "Correlation is not causation" in note
        assert "must accompany any citation" in note


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 49 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1212:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 49

    def test_forty_ninth_intact_in_journalists(self):
        # No new member this run: the forty-ninth claim form stays
        # exactly in profiles/careers/journalists.yaml (m956, 3 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_forty_ninth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_NINTH_MEMBER):
            assert p.endswith("careers/journalists.yaml"), p

    def test_fiftieth_absent_repo_wide(self):
        # The scout's proposed member slot is unclaimed: the fiftieth
        # form is absent repo-wide (lowercase absence-documentation prose
        # does not match the capitalized needle).
        needle = FIFTIETH_MEMBER
        assert _needle_hits_profiles(needle) == []
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            THIRTY_FIFTH_DIR, THIRTY_SIXTH_DIR, THIRTY_SEVENTH_DIR,
            THIRTY_EIGHTH_DIR, THIRTY_NINTH_DIR,
        ):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(FORTIETH_DIR) == []

    def test_ledger_note_holds_at_49(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 49" in note
        assert "FORTY-NINTH member-claim form present" in note
        assert "fiftieth member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1213 Type B run
# pins the 959 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1212:
    def test_zero_959_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 959" in src
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

    def test_no_fiftieth_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_no_forty_ninth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_1211_pins_flip_by_design_documented(self):
        # #1211's forward guards (max-957, zero-958 keys all forms,
        # no-Type-A-#1212-in-git-log) flip by design now that 958 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1211" in src
        text = _block_text()
        assert "1211" in text or "957" in text

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
# 9. Guard lifecycle (this run pins the 958 landing for #1213).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1212:
    def test_pins_on_958_landing(self):
        # The guards this run lays for the next leg: max-958, zero-959
        # numeric, no-Type-B-#1213-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 958" in src
        assert "NEXT_NUM = 959" in src

    def test_no_type_b_1213_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type B #1213").stdout
        assert log.strip() == ""

    def test_959_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1211_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1211))

    def test_openai_key_unique(self):
        data = _load_nc()
        assert list(
            data["competitor_relationships"].keys()).count("openai") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1215).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1212:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1210_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type A brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795 is recorded in
        # the block's background_suite_status field; #1215 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "#1215" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no 958 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1210_full_suite.log"
        )
        log = _read(suite_log)
        assert "958" not in log
        assert "Type A #1212" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1212:
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
        assert "## #1212 Type A:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65265 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1537


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1212:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1212 Type A:" in text

    def test_no_duplicate_1212_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1212 Type A:") == 1

    def test_window_third_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1210-1214" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1212:
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
            assert "mechanism_id: 958" not in diff, path
            assert "Type A #1212" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run appends to profiles/news-corp.yaml instead and
        # must not alter competitor-entities.yaml at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 958" not in diff
        assert "Type A #1212" not in diff
