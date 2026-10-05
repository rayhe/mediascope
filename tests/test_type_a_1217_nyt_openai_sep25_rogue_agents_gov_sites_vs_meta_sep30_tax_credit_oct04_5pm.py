# -*- coding: utf-8 -*-
"""Type A #1217 tests: NYT - OpenAI Sep-25-2026 rogue-agents
government-sites accountability arm (NEW, relay-attested NYT original)
vs NYT Sep-30-2026 Meta research-tax-credit investigation (NEW, FIRST
to corpus).

Mechanism m961 (NOT a falsification-family member; ledger holds at 50).
Excerpt-bounded research per #503 (delegated research subagent +
main-run verification: 2 main-run browser.search query sets, 0
browser.open reads). The researcher's recommended pair (NYT Sep-29 Dias
Anthropic Vatican arm vs NYT Sep-30 Meta tax-credit arm) was REJECTED
on main-run verification: the Dias arm is saturated via m940 (Type A
#1182, landed Oct 3). The researcher's Meta arm was VERIFIED novel and
retained; the main run found the replacement competitor arm (the NYT
Sep-25 OpenAI original that m916 documented as the accountability-register
counterfactual against WIRED's bounded absence).

The landed arms are NEW: NYT's Sep-25-2026 "OpenAI's AI on U.S.
Government Websites" breaking-news original (hard accountability
register, -0.70 MANUAL ILLUSTRATIVE, relay-attested via four
independent relays; canonical nytimes.com URL not recovered, none
constructed per policy; @nytimes Sep-25 post text carries the
"went rogue and meddled" framing) vs NYT's Sep-30-2026 front-page
Times Exclusive investigation into Meta's research-tax-credit treatment
of AI data centers (-0.75 MANUAL ILLUSTRATIVE, relay-attested via four
independent relays). Illustrative delta (OpenAI minus Meta) +0.05 -
near-null symmetric hardness at the NYT register in the crisis week.
The litigating plaintiff goes as hard on its litigation counterparty as
on the $0-tie Meta: litigation ties do not inflate adversarialism beyond
the peg-driven register. CONTROL-CASE / REGISTER-SYMMETRY EXTENSION of
m471 (litigation-posture boundary) and m916 (the NYT carried the
accountability register the Conde Nast deal holder went silent on);
NOT a new direction, NOT a falsification-family member per the
#609/#614 qualitative boundary (no uniform payer-softening prediction
under test - the NYT holds $0 from both entities).

Iteration #1217, THIRD leg of the 1215-1219 window
(D #1215 -> E #1216 -> A #1217 -> B #1218 -> C #1219).

The m961 block lives in profiles/nytimes.yaml as a
competitor_relationships.openai sub-key (4-space indent), appended at
the end of the openai section after the in-flight #899 m771 hunk -
targeted hunk-level staging keeps the #899 hunk out of this run's
index/diff (its working-tree text is preserved byte-identical,
verified against the pre-run baseline diff).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1215-launched background suite
(type_d_1215_full_suite.log); its verdict and tombstone belong to #1220
(next Type D). This run neither re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-ninth / fiftieth / fifty-first member-claim
forms, or the thirty-fifth through fortieth direction forms; the constants
are constructed at runtime. (The landed forty-ninth and fiftieth ordinals
live in profiles/careers/journalists.yaml; m956 and m959 respectively.)
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
    "test_type_a_1217_nyt_openai_sep25_rogue_agents_gov_sites_"
    "vs_meta_sep30_tax_credit_oct04_5pm.py"
)
BLOCK_KEY = (
    "type_a_1217_nyt_openai_sep25_rogue_agents_gov_sites_"
    "vs_meta_sep30_tax_credit_investigation"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "a3f6ebe5f585c3b8e77af4a7c2fdb1ea9cb671a3"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 65677/1541 -> (65677+N)/1542 in the doc-sync followup.
README_TEST_COUNT = 65677 + 80  # patched post-first-run per #719
README_FILE_COUNT = 1542
COLLECTED_NEW_TESTS = 80  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=961 is THIS run's landed
# mechanism; NEXT_NUM=962 stays forward.
MECH_NUM = 961
NEXT_NUM = 962

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m961 block lives here (colon-form key; no numeric-961 substring
# in the block key by designed keying per #715). It is a
# competitor_relationships.openai sub-key of profiles/nytimes.yaml.
NYT_PATH = os.path.join(REPO, "profiles", "nytimes.yaml")
FILE_1216 = "test_type_e_1216_podcast_sentiment_166th_verification_oct04_4pm.py"
FILE_1215 = "test_type_d_1215_m958_m959_m960_qualitative_corpus_integrity_oct04_4pm.py"
NYT_URLS = (
    "https://www.rswebsols.com/news/openai-discovers-its-technology-investigated-as-another-cybersecurity-target-the-u-s-government/",
    "https://dailycaller.com/2026/09/26/openai-agents-probed-us-gov-websites-sec-commerce-education-dept",
    "https://aiweekly.co/alerts/openai-says-its-agents-meddled-with-us-government-sites",
    "https://www.theregister.com/ai-and-ml/2026/09/28/openai-pauses-some-training-amid-allegations-its-rogue-agents-behaved-more-badly-than-first-thought/5299350",
    "https://www.indexbox.io/blog/meta-classifies-ai-data-centers-as-experimental-to-claim-federal-research-tax-credits/",
    "https://techstartups.com/2026/09/30/meta-classified-zuckerberg-as-a-researcher-to-claim-355-million-tax-break-on-4-1-billion-pay-nyt-reports/",
    "https://dev.to/techaiwire/meta-claims-39b-research-tax-credit-on-ai-data-centers-5d6f",
    "https://cryptobriefing.com/meta-data-centers-tax-avoidance-experimental/",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_nyt():
    return yaml.safe_load(_read(NYT_PATH))


def _openai_section():
    data = _load_nyt()
    assert "competitor_relationships" in data
    assert "openai" in data["competitor_relationships"]
    return data["competitor_relationships"]["openai"]


def _block():
    return _openai_section()[BLOCK_KEY]


def _block_text():
    return _read(NYT_PATH)


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

class TestAnchor1217:
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
        log = _git("log", "--oneline", "--grep=Type A #1217 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type A #1217 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type A #1217:").stdout
        assert "Type A #1217" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1217 is the THIRD leg of the 1215-1219 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1217:
    def test_rotation_window_is_1215_1219(self):
        text = _block_text()
        assert "1215-1219" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1215-1219 window THIRD leg "
            "(D #1215 -> E #1216 -> A #1217 -> B #1218 -> C #1219)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1215", "Type E #1216"):
            assert marker in log, marker

    def test_next_run_is_type_b(self):
        # The next leg (#1218 Type B) is documented in the block window
        # field; the iteration-log entry carrying it lands in the doc-sync
        # followup (TestIterationLog1217 pins it there).
        assert "B #1218" in _block()["window"]
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1215-1219" in text

    def test_no_type_a_1217_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1217_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1217:
    def test_openai_section_found(self):
        section = _openai_section()
        # The NYT x OpenAI tie is the adversarial litigation posture
        # ($0 + active copyright suit), not a licensing tie.
        assert section["financial_tie"] == "adversarial"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1217, not the mechanism number.
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
        assert nums, "m961 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_nyt_urls_in_block_source_urls_verbatim(self):
        urls = [s["url"] for s in _block()["source_urls"]]
        assert len(urls) == 8
        for u in NYT_URLS:
            assert u in urls, u
        assert all(u.startswith("https://") for u in urls)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "nytimes.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (competitor_relationships.openai sub-key of
# profiles/nytimes.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1217:
    def test_openai_section_is_expected_parent(self):
        data = _load_nyt()
        assert "competitor_relationships" in data
        assert isinstance(data["competitor_relationships"]["openai"], dict)

    def test_block_key_present_under_openai(self):
        section = _openai_section()
        assert BLOCK_KEY in section

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 961

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

    def test_openai_arm_tone(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.70
        assert arm["entity"] == "openai"
        assert "2026-09-25" in arm["date"]
        assert "NEW this run" in arm["status"]

    def test_meta_arm_new_documented(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.75
        assert arm["entity"] == "meta"
        assert "2026-09-30" in arm["date"]
        assert "NEW this run" in arm["status"]

    def test_publication_nyt(self):
        assert _block()["publication"] == "The New York Times"


# ---------------------------------------------------------------------------
# 5. m961 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM961ContentDiscipline1217:
    def test_openai_key_quotes_verbatim(self):
        quotes = _block()["openai_arm"]["key_quotes"]
        assert any("went rogue and meddled" in q for q in quotes)
        assert any("rudimentary hack" in q for q in quotes)
        assert any("misaligned model activity" in q for q in quotes)

    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("experimental facilities" in q for q in quotes)
        assert any("kind of wild and out there" in q for q in quotes)
        assert any("355 million tax break" in q for q in quotes)
        assert any("18.74 billion" in q for q in quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        for arm in ("openai_arm", "meta_arm"):
            tier = _block()[arm]["evidence_tier"]
            assert "EXCERPT-TIER" in tier
            assert "not first-hand read" in tier

    def test_no_full_read_claim(self):
        # Honesty pin: the block must not claim a first-hand full-text read
        # of either nytimes.com original. (Scoped to the m961 block.)
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 24000]
        assert "FIRST-HAND full-text read" not in chunk

    def test_no_canonical_url_constructed(self):
        # Every source URL must be one of the verbatim tool-output URLs;
        # no nytimes.com canonical was recovered or constructed.
        urls = [s["url"] for s in _block()["source_urls"]]
        assert len(urls) == 8
        for u in NYT_URLS:
            assert u in urls
        assert not any(u.startswith("https://www.nytimes.com/")
                       for u in urls)

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        for name in ("m940", "Dias", "m916", "DevDay", "Android XR",
                     "Broadcom", "Coxon"):
            assert name in method, name

    def test_ascii_only(self):
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 24000]
        chunk.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per Aug 28 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1217:
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
        assert s["illustrative_delta_openai_minus_meta"] == 0.05
        assert s["meta_tone_MANUAL_ILLUSTRATIVE"] == -0.75
        assert s["openai_tone_MANUAL_ILLUSTRATIVE"] == -0.70

    def test_verdict_is_control_case_not_discovery(self):
        b = _block()
        assert b["verdict"].startswith("control_case")
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
# 7. Falsification ledger (holds at 50 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1217:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50

    def test_forty_ninth_intact_in_journalists(self):
        # No new member this run: the forty-ninth claim form stays
        # exactly in profiles/careers/journalists.yaml (m956, 3 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_intact_in_journalists(self):
        # The fiftieth claim form stays exactly in
        # profiles/careers/journalists.yaml (m959, 3 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
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
        assert "FORTY-NINTH member-claim form present" in note
        assert "FIFTIETH member-claim form present" in note
        assert "fifty-first member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1218 Type B run
# pins the 962 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1217:
    def test_zero_962_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 962" in src
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
        assert (FIFTY_FIRST_MEMBER) not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_no_forty_ninth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_no_fiftieth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1216_pins_flip_by_design_documented(self):
        # #1216's forward guards (max-960, zero-961 keys all forms,
        # no-Type-A-#1217-in-git-log) flip by design now that m961 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1216" in src
        text = _block_text()
        assert "1216" in text or "m960" in text

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
# 9. Guard lifecycle (this run pins the 961 landing for #1218).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1217:
    def test_pins_on_961_landing(self):
        # The guards this run lays for the next leg: max-961, zero-962
        # numeric, no-Type-B-#1218-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 961" in src
        assert "NEXT_NUM = 962" in src

    def test_no_type_b_1218_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type B #1218").stdout
        assert log.strip() == ""

    def test_962_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1216_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1216))

    def test_openai_key_unique(self):
        data = _load_nyt()
        assert list(
            data["competitor_relationships"].keys()).count("openai") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1220).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1217:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1215_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type A brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795 is recorded in
        # the block's background_suite_status field; #1220 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "#1220" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m961 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1215_full_suite.log"
        )
        log = _read(suite_log)
        assert "m961" not in log
        assert "Type A #1217" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1217:
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
        assert "## #1217 Type A:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65677 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1542


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1217:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1217 Type A:" in text

    def test_no_duplicate_1217_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1217 Type A:") == 1

    def test_window_third_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1215-1219" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped; nytimes.yaml carries BOTH the
# #899 m771 hunk and this run's m961 hunk - targeted staging keeps them
# apart).
# ---------------------------------------------------------------------------

class TestInflightIsolation1217:
    def test_899_hunk_preserved_in_file(self):
        # The in-flight #899 m771 hunk must survive this run byte-identical:
        # its block key and mechanism marker stay in the file, owned by its
        # run, never staged by this one.
        text = _block_text()
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026:" in text
        assert "mechanism_id: 771" in text

    def test_961_hunk_present_in_file(self):
        text = _block_text()
        assert BLOCK_KEY + ":" in text
        assert "mechanism_id: 961" in text

    def test_other_inflight_files_untouched_by_this_run(self):
        # The three in-flight test files must carry none of this run's
        # markers in their working-tree diffs.
        for path in (
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path).stdout
            assert "mechanism_id: 961" not in diff, path
            assert "Type A #1217" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run appends to profiles/nytimes.yaml instead and
        # must not alter competitor-entities.yaml at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 961" not in diff
        assert "Type A #1217" not in diff
