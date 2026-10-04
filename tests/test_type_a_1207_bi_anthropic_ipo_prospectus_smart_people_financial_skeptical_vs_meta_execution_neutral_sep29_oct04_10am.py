# -*- coding: utf-8 -*-
"""Type A #1207 tests: Business Insider - Anthropic Sep-29-2026 IPO
prospectus "smart people" financial-skeptical register vs carried Meta
product-execution neutral triad (m399, un-rescored per #807).

Mechanism m955 (NOT a falsification-family member; ledger holds at 48).
Excerpt-bounded research per #503 (13 browser.search query sets, 0
browser.open reads). Rejected as corpus-saturated or peg-absent: The
Verge Sep-29 Anthropic IPO-prospectus risk-factor arm (in corpus via
m883, Type A #1087 - relay-attested via 10news.org, -0.40); Guardian
Sep-29 Anthropic existential-risks IPO-document arm (in corpus via
m886, Type A #1092); Snap SPECS First Look Oct 1-2 (no tracked
publication originals surfaced - Reuters/BusinessWire/roadtovr relays
only; bounded absence per the iteration-492 rule); Apple Gurman Sep-28
Vision Pro N224 "life support" + 2027 smart glasses (no theverge.com /
wired.com / gizmodo.com originals surfaced - MacRumors/AppleInsider/
Gadgets360 relays only); Apple $5.7B Taction haptics verdict Sep 25
(no gizmodo.com original surfaced - notebookcheck/gadgets360/techrepublic
relays only); Verge x Anthropic pacing-policy (in corpus via m883);
BI x Anthropic Nasdaq IPO scoop (in corpus via m745, Type A #857).

The landed arm is NEW: BI's Sep-29-2026 "What smart people are saying
about Anthropic's leaked IPO prospectus numbers" (financial-skeptical
register, -0.30 MANUAL ILLUSTRATIVE, relay-attested via five
independent mirrors; canonical businessinsider.com URL not recovered,
none constructed per policy; biztoc timestamps the BI original
2026-09-29 17:18:17). The Meta arms are CARRIED from m399 (#399,
un-rescored per #807): BI's Meta product-execution triad (Dec 2025 -
Apr 2026, +0.08 avg) - Phoenix delay framed as polishing, Ray-Ban
Display scarcity as demand-positive, retail expansion as strategic
growth; no financial-viability questioning. Illustrative delta
(Anthropic minus Meta) -0.38. Cross-lab: m399's OpenAI arm (the DEAL
partner, Axel Springer x OpenAI licensing) scored -0.42 on the same
financial-skepticism register family; the non-deal lab (Anthropic, $0
Axel Springer tie) now draws -0.30 on its own IPO paper - 0.12 apart,
near-parity. The register follows the financial peg (fundraising/IPO
scrutiny genre), not the payer. TEMPORAL REPLICATION of m399's
deal-partner-hardness finding at the non-deal lab; EXTENDS the BI
control case (m399's own verdict: the Axel Springer deal buys no stable
softness). The "smart people" roundup format hedges the skepticism
through third-party voices (Akoner, Marcus, Hendricks, Williams) -
one notch softer than m399's direct investor-alarm register (-0.42),
same family.

Iteration #1207, THIRD leg of the 1205-1209 window
(D #1205 -> E #1206 -> A #1207 -> B #1208 -> C #1209).

The m955 block lives in profiles/business-insider.yaml as a
competitor_relationships.anthropic sub-key (4-space indent, sibling of
m420/m745), appended before the `meta:` key.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1205-launched background suite
(re-launched ~09:00 PDT Oct 4, log type_d_1205_full_suite.log); its
verdict and tombstone belong to #1210 (next Type D). This run neither
re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-eighth / forty-ninth member-claim forms, or
the thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed forty-eighth ordinal lives in
financial-times.yaml (m952).)
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
    "test_type_a_1207_bi_anthropic_ipo_prospectus_smart_people_"
    "financial_skeptical_vs_meta_execution_neutral_sep29_oct04_10am.py"
)
BLOCK_KEY = (
    "type_a_1207_bi_anthropic_ipo_prospectus_smart_people_"
    "financial_skeptical_vs_meta_execution_neutral_sep29"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "ec95a251fa8d96a120d9b47597c9ea0d5be24383"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 64858/1531 -> (64858+N)/1532 in the doc-sync followup.
README_TEST_COUNT = 64858 + 75  # patched post-first-run per #719
README_FILE_COUNT = 1532
COLLECTED_NEW_TESTS = 75  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=955 is THIS run's landed
# mechanism; NEXT_NUM=956 stays forward.
MECH_NUM = 955
NEXT_NUM = 956

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m955 block lives here (colon-form key; no numeric-955 substring
# in the block key by designed keying per #715). It is a
# competitor_relationships.anthropic sub-key of profiles/business-insider.yaml.
BI_PATH = os.path.join(REPO, "profiles", "business-insider.yaml")
FILE_1206 = "test_type_e_1206_podcast_sentiment_164th_verification_oct04_930am.py"
FILE_1205 = "test_type_d_1205_m952_m953_m954_qualitative_corpus_integrity_oct04_9am.py"
BI_URLS = (
    "https://postgoo.com/posts/6abc750e5eb878472d47bed0?type=article",
    "https://cncbnews.com/article/2026/09/what-smart-people-are-saying-about-anthropics-leaked-ipo-prospectus-numbers",
    "https://misryoum.com/what-smart-people-are-saying-about-anthropics-leaked-ipo-prospectus-numbers",
    "https://www.collector.com.tr/1017818011",
    "https://biztoc.com/x/a10989637617ed19",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_bi():
    return yaml.safe_load(_read(BI_PATH))


def _anthropic_section():
    data = _load_bi()
    assert "competitor_relationships" in data
    assert "anthropic" in data["competitor_relationships"]
    return data["competitor_relationships"]["anthropic"]


def _block():
    return _anthropic_section()[BLOCK_KEY]


def _block_text():
    return _read(BI_PATH)


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

class TestAnchor1207:
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
        log = _git("log", "--oneline", "--grep=Type A #1207 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type A #1207 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type A #1207:").stdout
        assert "Type A #1207" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1207 is the THIRD leg of the 1205-1209 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1207:
    def test_rotation_window_is_1205_1209(self):
        text = _block_text()
        assert "1205-1209" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1205-1209 window THIRD leg "
            "(D #1205 -> E #1206 -> A #1207 -> B #1208 -> C #1209)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1205", "Type E #1206"):
            assert marker in log, marker

    def test_next_run_is_type_b(self):
        # The next leg (#1208 Type B) is documented in the block window
        # field; the iteration-log entry carrying it lands in the doc-sync
        # followup (TestIterationLog1207 pins it there).
        assert "B #1208" in _block()["window"]
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1205-1209" in text

    def test_no_type_a_1207_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1207_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1207:
    def test_anthropic_section_found(self):
        section = _anthropic_section()
        assert section["financial_tie"] == "none"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1207, not the mechanism number.
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
        assert nums, "m955 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_bi_urls_in_block_source_urls_verbatim(self):
        urls = [s["url"] for s in _block()["source_urls"]]
        for u in BI_URLS:
            assert u in urls, u
        assert all(u.startswith("https://") for u in urls)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
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


# ---------------------------------------------------------------------------
# 4. Block structure (competitor_relationships.anthropic sub-key of
# profiles/business-insider.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1207:
    def test_anthropic_section_is_expected_parent(self):
        data = _load_bi()
        assert "competitor_relationships" in data
        assert isinstance(data["competitor_relationships"]["anthropic"], dict)

    def test_block_key_present_under_anthropic(self):
        section = _anthropic_section()
        assert BLOCK_KEY in section

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == 955

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id",
            "scheduled_job_id", "date_analyzed", "block_key", "test_file",
            "author", "publication", "competitor_pair", "window", "design",
            "anthropic_arm", "meta_arm", "scorer", "financial_relationship",
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

    def test_anthropic_arm_tone(self):
        arm = _block()["anthropic_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert arm["entity"] == "anthropic"
        assert "2026-09-29" in arm["date"]

    def test_meta_arm_carried_documented(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.08
        assert arm["entity"] == "meta"
        assert "CARRIED from m399" in arm["status"]

    def test_publication_business_insider(self):
        assert _block()["publication"] == "business-insider"


# ---------------------------------------------------------------------------
# 5. m955 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM955ContentDiscipline1207:
    def test_key_quotes_verbatim(self):
        quotes = _block()["anthropic_arm"]["key_quotes"]
        assert any("IPO math is staggering" in q for q in quotes)
        assert any("gobsmacking numbers" in q for q in quotes)
        assert any("a lot of work to do" in q for q in quotes)
        assert any("long way from proving" in q for q in quotes)
        assert any("The more they lose, the more they win" in q for q in quotes)
        assert any("shareholder dilution on this will be" in q for q in quotes)

    def test_meta_arm_quotes_carried(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("get the details right" in q for q in quotes)
        assert any("high demand" in q for q in quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        tier = _block()["anthropic_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in tier
        assert "not first-hand read" in tier

    def test_no_full_read_claim(self):
        # Honesty pin: the block must not claim a first-hand full-text read
        # of the businessinsider.com prospectus-numbers page. (Scoped to the
        # m955 block: the m399 meta arms legitimately carry archived reads.)
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 16000]
        assert "FIRST-HAND full-text read" not in chunk

    def test_no_canonical_url_constructed(self):
        # Every source URL must be one of the verbatim tool-output URLs.
        urls = [s["url"] for s in _block()["source_urls"]]
        assert len(urls) == 5
        for u in BI_URLS:
            assert u in urls
        assert not any(u.startswith("https://www.businessinsider.com/")
                       for u in urls)

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        for name in ("m883", "m886", "Snap SPECS First Look",
                     "Gurman", "Taction", "m745"):
            assert name in method, name

    def test_ascii_only(self):
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 16000]
        chunk.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per Aug 28 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1207:
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
        assert s["illustrative_delta_anthropic_minus_meta"] == -0.38
        assert s["meta_tone_MANUAL_ILLUSTRATIVE"] == 0.08
        assert s["anthropic_tone_MANUAL_ILLUSTRATIVE"] == -0.30

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
# 7. Falsification ledger (holds at 48 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1207:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 48

    def test_forty_eighth_intact_in_ft(self):
        # No new member this run: the forty-eighth claim form stays
        # exactly in financial-times.yaml m952 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_EIGHTH_MEMBER):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_absent(self):
        assert _needle_hits_profiles(FORTY_NINTH_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FORTY_NINTH_MEMBER not in open(
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

    def test_ledger_note_holds_at_48(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 48" in note
        assert "FORTY-EIGHTH member-claim form present" in note
        assert "FORTY-NINTH member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1208 Type B run
# pins the 956 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1207:
    def test_zero_956_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 956" in src
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

    def test_no_forty_ninth_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_EIGHTH_MEMBER) not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1206_pins_flip_by_design_documented(self):
        # #1206's forward guards (max-954, zero-955 keys all forms,
        # no-Type-A-#1207-in-git-log) flip by design now that m955 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1206" in src
        text = _block_text()
        assert "1206" in text or "m954" in text

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
# 9. Guard lifecycle (this run pins the 955 landing for #1208).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1207:
    def test_pins_on_955_landing(self):
        # The guards this run lays for the next leg: max-955, zero-956
        # numeric, no-Type-B-#1208-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 955" in src
        assert "NEXT_NUM = 956" in src

    def test_no_type_b_1208_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type B #1208").stdout
        assert log.strip() == ""

    def test_956_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1206_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1206))

    def test_anthropic_key_unique(self):
        data = _load_bi()
        assert list(
            data["competitor_relationships"].keys()).count("anthropic") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1210).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1207:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1205_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type A brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795 is recorded in
        # the block's background_suite_status field; #1210 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "#1210" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m955 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1205_full_suite.log"
        )
        log = _read(suite_log)
        assert "m955" not in log
        assert "Type A #1207" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1207:
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
        assert "## #1207 Type A:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64858 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1532


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1207:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1207 Type A:" in text

    def test_no_duplicate_1207_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1207 Type A:") == 1

    def test_window_third_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1205-1209" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1207:
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
            assert "mechanism_id: 955" not in diff, path
            assert "Type A #1207" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run appends to profiles/business-insider.yaml instead and
        # must not alter competitor-entities.yaml at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 955" not in diff
        assert "Type A #1207" not in diff
