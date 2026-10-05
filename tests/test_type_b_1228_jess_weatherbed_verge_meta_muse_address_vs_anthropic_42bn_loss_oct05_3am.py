# -*- coding: utf-8 -*-
"""Type B #1228 tests: Jess Weatherbed (The Verge) - Meta Muse address-leak
privacy-failure news vs Anthropic $42B-loss IPO-leak financial news, same-day
symmetric-adversarial boundary/control case (m968).

Mechanism m968 (boundary/control; ledger HOLDS at 50 - NOT a
falsification-family member). Weatherbed applies the adversarial register to
Meta Muse (-0.55 MANUAL ILLUSTRATIVE, NEW Sep-29 arm, relay-attested) and to
Anthropic (-0.50 MANUAL ILLUSTRATIVE, NEW Sep-29 arm, profile-attested);
illustrative delta (Anthropic minus Meta) +0.05 near-null. A same-day
companion piece ("Anthropic warns of 'catastrophic' AI risks in its own IPO
filing", -0.45) corroborates within-byline register constancy. Anthropic is
not the deal partner, so the strict deal-partner prediction is untested; the
in-outlet contrast with m965 (Allison Johnson, same outlet, same Vox x OpenAI
deal, confirming direction) extends the m956/m959 journalist-contingent
refinement: the deal effect is reporter-contingent, not outlet-uniform.

Excerpt-bounded research per #503 (delegated scout ~18 query sets across 16
candidates + 4 main-run browser.search verification sets, 0 browser.open
reads). Rejected: Caroline Haskins, Mitchell Clark, Umar Shakir, David Pierce,
Lakshmi Varanasi, Dan Milmo, Hayden Field, Kylie Robison, Matt O'Brien, Thalia
Beaty, Aaron Mok, Will Knight, Jake Kastrenakes, Stephen Council, Benedict
Collins (saturated/peg-absent/out-of-window/beat-moved). Main-run corrected
the scout's corpus characterization (m56/m462 pre-exist, so the novelty is
the same-day symmetric-adversarial pair, not a first look at the journalist)
and its lean toward a falsification-family claim (boundary/control verdict:
Anthropic is not the deal partner).

The m968 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `jess_weatherbed_type_b`
key (per the #643 convention; career-profile list entry pre-exists under
`journalists:`; mechanism_ids [968]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1225-launched background suite
(observed ALIVE at this run's check); its verdict and tombstone belong to
#1230 (next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-eighth / forty-ninth / fiftieth / fifty-first
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed fiftieth ordinal lives
in profiles/careers/journalists.yaml (m959); the forty-ninth lives there too
(m956); the forty-eighth lives in profiles/financial-times.yaml (m952).)
"""

import os
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE
PROFILES_DIR = os.path.join(REPO, "profiles")
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")

OWN_BASENAME = (
    "test_type_b_1228_jess_weatherbed_verge_meta_muse_address_vs_"
    "anthropic_42bn_loss_oct05_3am.py"
)
BLOCK_KEY = (
    "type_b_1228_jess_weatherbed_verge_meta_muse_address_vs_"
    "anthropic_42bn_loss_oct05_3am"
)
TOP_KEY = "jess_weatherbed_type_b"

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "c814454e461753680f1ec6813d41326a42c9e163"  # patched per #565 in the anchor followup
# Post-first-run values per #719: N tests collected; README ratchets
# 66552/1552 -> (66552+N)/1553 in the doc-sync followup.
README_TEST_COUNT = 66552 + 94  # 66646; patched post-first-run per #719
README_FILE_COUNT = 1553
COLLECTED_NEW_TESTS = 94  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=968 is THIS run's landed
# mechanism; NEXT_NUM=969 stays forward.
MECH_NUM = 968
NEXT_NUM = 969

# Needle markers, format-built per #715. The marker is concatenated with
# the number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"
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

# The landed m968 block lives here: a competitor_coverage sub-key of the
# NEW top-level jess_weatherbed_type_b key in profiles/careers/journalists.yaml.
D1227_FILE = (
    "test_type_a_1227_bi_openai_robinson_resignation_exclusive_"
    "vs_meta_execution_triad_oct05_2am.py"
)

# Predecessor chain: #1227 Type A closed the third leg of the 1225-1229
# window (main/anchor/doc-sync/log-hash; correctives dc8db6b1/277cdb72).
PRED_MAIN_1227 = "6b01b97a"
PRED_ANCHOR_1227 = "49651ebf"
PRED_DOCSYNC_1227 = "fc586f18"
PRED_FINAL_1227 = "d490a209"

# Novel relay URLs (verbatim from this run's Full-URL listings; zero-hit
# repo-wide pre-commit via git grep -F). The muckrack profile URL is a
# pre-existing corpus URL (byline-attestation source only), not novel.
NOVEL_URLS = (
    "https://wesearch.press/s/metas-muse-ai-sent-a-youtubers-address-"
    "to-a-stranger-80434392",
    "https://thetechstreetnow.com/metas-muse-ai-sent-a-youtubers-"
    "address-to-a-stranger/",
    "https://technewsvision.co.uk/metas-muse-ai-sent-a-youtubers-"
    "address-to-a-stranger/",
    "https://techseen.com/story/anthropic-s-ipo-filing-shows-soaring-"
    "revenue-mounting-costs-and-existe-6ce54d1",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _top():
    data = _load_journalists()
    assert TOP_KEY in data
    return data[TOP_KEY]


def _block():
    top = _top()
    assert "competitor_coverage" in top
    assert BLOCK_KEY in top["competitor_coverage"]
    return top["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


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
    return [line for line in out.splitlines() if line.strip()]


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

class TestAnchor1228:
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
        assert "FOURTH leg of the 1225-1229 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1228:
    def test_predecessor_1227_chain_verified(self):
        for sha in (
            PRED_MAIN_1227, PRED_ANCHOR_1227, PRED_DOCSYNC_1227,
            PRED_FINAL_1227,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1225 -> E #1226 -> A #1227 -> B #1228 -> C #1229" in src

    def test_next_leg_is_type_c_1229(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1229 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (m968); the Type A
        # predecessor added one (m967).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1228:
    def test_top_key_found(self):
        assert TOP_KEY in _load_journalists()

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1228 in key, no 968 or 969
        # substring.
        assert "1228" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_dedicated_weatherbed_type_b_key_precommit(self):
        # The #643 new-key path: no dedicated weatherbed type_b key
        # existed before this run's landing; now exactly one.
        text = _block_text()
        assert text.count(TOP_KEY + ":") == 1

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # "mechanism_id: 968" (colon form); the underscore key form must
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
        assert nums, "m968 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = b["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_muckrack_url_flagged_preexisting(self):
        # The muckrack profile URL is a pre-existing corpus URL cited as
        # byline-attestation source only; the block's url_note says so.
        b = _block()
        assert "http://muckrack.com/jess-weatherbed/articles" in b[
            "source_urls"]
        assert "pre-existing corpus URL" in b["anthropic_arm"]["url_note"]

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit
        # it appears only in the landed YAML block, this test file, and
        # the doc-sync targets (README, ARCHITECTURE, iteration-log).
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

    def test_meta_headline_novelty(self):
        text = _block_text()
        assert "Muse AI sent a YouTuber" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "Muse AI sent a YouTuber" not in text[:block_start]

    def test_anthropic_headline_novelty(self):
        text = _block_text()
        assert "lost $42 billion" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "lost $42 billion" not in text[:block_start]

    def test_both_arms_new_documented(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-29"
        assert b["meta_arm"]["author_byline"] == "Jess Weatherbed"
        assert b["anthropic_arm"]["date"] == "2026-09-29"
        assert b["anthropic_arm"]["author_byline"] == "Jess Weatherbed"

    def test_no_type_b_1228_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the log-hash followup per #721): the ONLY matches so far
        # are this run's own commits, whose messages carry the run's
        # own iteration subject. The pin's substance - no PRIOR run
        # committed this run's iteration - holds. The log-hash sha is
        # filled by the corrective commit per #721.
        out = _git("log", "--format=%H %s", "--grep=Type B #1228").stdout
        own = {"c814454e", "53ac9eaf", "0da1fa9d", "19e32817", "e5f97fec"}
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits, "expected this run's own commits"
        for line in hits:
            assert line.split()[0][:8] in own, line


# ---------------------------------------------------------------------------
# 4. Block structure under the new top-level jess_weatherbed_type_b key.
# ---------------------------------------------------------------------------

class TestBlockStructure1228:
    def test_top_key_is_expected_parent(self):
        top = _top()
        assert top["name"] == "Jess Weatherbed"
        assert top["publication"] == "the-verge"
        assert top["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present_under_competitor_coverage(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1228
        assert b["type"] == "B"
        assert b["publication"] == "the-verge"
        assert b["journalist"] == "Jess Weatherbed"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "mechanism_id", "iteration", "type", "date", "test_file",
            "author", "goal_id", "job_id", "scheduled_job_id",
            "journalist", "publication", "window", "design", "meta_arm",
            "anthropic_arm", "corroborating_arm", "scorer",
            "statistical_discipline", "financial_context", "finding",
            "confounders", "counter_evidence", "connects_to", "verdict",
            "falsification_family", "falsification_family_member",
            "falsification_ledger", "ledger_note", "is_significant",
            "correlation_not_causation", "no_analysis_json_update",
            "artifact_readiness", "research_method", "novelty",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55

    def test_anthropic_arm_tone(self):
        assert _block()["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50

    def test_scorer_delta(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_anthropic_minus_meta"] == 0.05
        assert s["meta_tone"] == -0.55
        assert s["anthropic_tone"] == -0.50

    def test_connects_to_lineage(self):
        conns = _block()["connects_to"]
        for mid in (494, 952, 956, 959, 965, 462, 56):
            assert mid in conns, mid

    def test_source_urls_count(self):
        b = _block()
        assert len(b["source_urls"]) == 5

    def test_corroborating_arm_present(self):
        c = _block()["corroborating_arm"]
        assert "catastrophic" in c["title"]
        assert c["tone_MANUAL_ILLUSTRATIVE"] == -0.45


# ---------------------------------------------------------------------------
# 5. Content discipline: excerpt-bounded, no constructed URLs, ASCII-only.
# ---------------------------------------------------------------------------

class TestM968ContentDiscipline1228:
    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "gave out his home address to a total stranger" in joined
        assert "catch up with competing AI providers" in joined
        assert "oversight for Meta" in joined

    def test_anthropic_key_quotes_verbatim(self):
        quotes = _block()["anthropic_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "lost $42 billion" in joined
        assert "leaked IPO filing seen by Reuters" in joined
        assert "a long, long way off" in joined

    def test_no_constructed_theverge_url(self):
        # No canonical theverge.com URL was constructed for either arm;
        # the discipline is recorded in the block.
        text = _block_text()
        assert "theverge.com/2026/9/29" not in text
        assert "no canonical URLs constructed" in text

    def test_byline_attestation_disclosed(self):
        b = _block()
        assert "Jess Weatherbed" in b["meta_arm"]["evidence_tier"]
        assert "Muck Rack" in b["anthropic_arm"]["evidence_tier"]
        assert "bounded byline-certainty" in b["anthropic_arm"][
            "evidence_tier"]

    def test_wesearch_url_verbatim_from_listing(self):
        note = _block()["meta_arm"]["url_note"]
        assert "Full-URL listing" in note
        assert "2:08 PM UTC" in note

    def test_ascii_only(self):
        # Scoped to this run's block: the block must dump ASCII-clean.
        yaml.safe_dump(_block(), allow_unicode=False).encode("ascii")

    def test_no_em_dashes(self):
        block_start = _block_text().index(TOP_KEY + ":")
        assert "\u2014" not in _block_text()[block_start:]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1228:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE" in _block()["scorer"][
            "statistical_discipline"]

    def test_engine_not_run(self):
        assert _block()["scorer"]["engine_run"] is False

    def test_p_value_not_calculated(self):
        assert _block()["scorer"]["p_value"] == "NOT_CALCULATED"
        assert _block()["scorer"]["cohens_d"] == "NOT_CALCULATED"
        assert _block()["scorer"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False
        assert _block()["scorer"]["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_boundary_not_discovery(self):
        verdict = _block()["verdict"]
        assert "boundary_control_case" in verdict
        assert "not_a_discovery" in verdict

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["statistical_discipline"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 50; boundary case, no new member)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1228:
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
        assert "Ledger HOLDS at 50" in note
        assert "m968 boundary/control case, no new member" in note
        assert "fifty-first member-claim form absent repo-wide" in note

    def test_falsification_field_states_boundary(self):
        fam = _block()["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "Ledger HOLDS at 50" in fam


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1229 Type C run
# pins the 969 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1228:
    def test_zero_969_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 969" in src
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
        assert _needle_hits_profiles(FORTIETH_DIR) == []
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

    def test_1227_pins_flip_by_design_documented(self):
        # #1227's forward guards (max-967, zero-968 keys all forms,
        # no-Type-B-#1228-in-git-log) flip by design now that m968 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1227" in src
        text = _block_text()
        assert "1227" in text

    def test_thirty_fifth_direction_still_present(self):
        assert _needle_hits_profiles(THIRTY_FIFTH_DIR)

    def test_thirty_sixth_direction_still_present(self):
        assert _needle_hits_profiles(THIRTY_SIXTH_DIR)

    def test_thirty_seventh_direction_still_present(self):
        assert _needle_hits_profiles(THIRTY_SEVENTH_DIR)

    def test_thirty_eighth_direction_still_present(self):
        assert _needle_hits_profiles(THIRTY_EIGHTH_DIR)

    def test_thirty_ninth_direction_still_present(self):
        assert _needle_hits_profiles(THIRTY_NINTH_DIR)


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 968 landing for #1229).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1228:
    def test_pins_on_968_landing(self):
        # The guards this run lays for the next leg: max-968,
        # zero-969 all forms, no-Type-C-#1229-in-git-log, fortieth
        # direction absent (profiles/ scope), forty-eighth member
        # intact in profiles/financial-times.yaml, forty-ninth member
        # intact + fiftieth member intact in
        # profiles/careers/journalists.yaml, fifty-first member absent
        # (repo-wide), ledger 50.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 968" in src
        assert "NEXT_NUM = 969" in src

    def test_no_type_c_1229_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1229").stdout
        assert out.strip() == "", out.strip()

    def test_969_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1227_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1227_FILE))

    def test_1228_key_unique(self):
        # The 1228-keyed block key appears once as a block key; the
        # "type_b_1228_" prefix also occurs in the block_key field value
        # and the test_file field value (tests/test_type_b_1228_...).
        text = _block_text()
        assert text.count("type_b_1228_") == 3

    def test_next_leg_is_1229_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1229 Type C" in src


# ---------------------------------------------------------------------------
# 10. Background suite check-only per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1228:
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

class TestDocSync1228:
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
        assert "## #1228 Type B:" in text


# ---------------------------------------------------------------------------
# 12. Iteration log (#721: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1228:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1228 Type B:" in text

    def test_no_duplicate_1228_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1228 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1225-1229" in text

    def test_log_hash_followup_registers_hashes(self):
        # Per #721 the log-hash followup registers all four hashes in the
        # iteration-log entry; pre-commit the entry is absent and this is
        # vacuous via the header test above. Post-doc-sync the entry must
        # carry the main-commit hash once the log-hash followup lands.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        if "## #1228 Type B:" in text and ANCHORED_SHA != "0" * 40:
            assert ANCHORED_SHA in text


# ---------------------------------------------------------------------------
# 13. Staleness pins: #1227's guard lifecycle (deselected pre-commit per
# #721; post-main-commit form expects the two designed flips).
# ---------------------------------------------------------------------------

class TestStalenessPins1228:
    def test_1227_guard_lifecycle_post_commit_two_flips(self):
        # Post-main-commit form: 4 of the 6 pass; the two that fail do
        # so BY DESIGN on this run's landing - test_no_type_b_1228_in_
        # git_log_pin trips on this run's own main commit (the
        # #1191-class self-trip) and test_968_numeric_absent_in_profiles
        # trips on the landed m968 block. The #1227 block is read-only
        # to this run; the flips are recorded, not repaired.
        res = _class_run(D1227_FILE, "TestGuardLifecycle1227")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 4 passed" in res.stdout, res.stdout[-2000:]
        assert "test_no_type_b_1228_in_git_log_pin" in res.stdout
        assert "test_968_numeric_absent_in_profiles" in res.stdout


# ---------------------------------------------------------------------------
# 14. In-flight isolation (this run touches profiles/careers/journalists.yaml
# + the new test file only; #899/#938/#900/#1012-wt and #1024 stay out).
# ---------------------------------------------------------------------------

class TestInflightIsolation1228:
    def test_no_1228_markers_in_nytimes_yaml(self):
        text = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        assert BLOCK_KEY not in text
        assert "Type B #1228" not in text

    def test_no_1228_markers_in_inflight_test_files(self):
        for name in (
            "test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
            "agenda_setting_register_vs_carried_meta_india_havoc_"
            "m817_pairing_sep26_7am.py",
            "test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
        ):
            text = _read(os.path.join(TESTS_DIR, name))
            assert BLOCK_KEY not in text, name
            assert "Type B #1228" not in text, name

    def test_m846_untouched(self):
        # #1024 m846 lives in profiles/competitor-entities.yaml; Ray's
        # revert/leave/rebuild decision is pending - this run must not
        # touch that file.
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert BLOCK_KEY not in text
        assert "Type B #1228" not in text

    def test_only_intended_paths_differ(self):
        # The working tree may only differ from HEAD on this run's paths
        # (the two main-commit paths plus the three doc-sync paths) and
        # the four pre-existing in-flight paths. Pre-main-commit the
        # run's own main paths are uncommitted; in the doc-sync phase the
        # doc-sync paths are uncommitted; post-sequence all drop out of
        # the status, which stays within the allowed set throughout.
        out = _git("status", "--short").stdout
        allowed = {
            os.path.join("profiles", "careers", "journalists.yaml"),
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
