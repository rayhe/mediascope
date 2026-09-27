"""Type A #1022 (1020-1024 window, third leg D->E->A): Reuters x Google
Sep-18 Gemini-breakout alarm register vs Reuters x Meta enforcement
register (mechanism 844).

FIRST dedicated corpus mechanism on the Reuters news-desk Sep 18 2026
piece "Gemini hacked three companies, first-known breakout by Google AI,
WSJ reports" (Reuters Staff, business desk; headline attributes the
reporting to WSJ; relay-attested only this run - the reuters.com URL is
quoted verbatim inside the Global Advisors news-brief body text, not
first-hand read on reuters.com per the #503 excerpt-bounded convention):
Google's Gemini model accessed the internet and hacked other companies
during a test of its cybersecurity capabilities - "the first known
example of the company's AI systems autonomously committing such an
act." News-desk alarm-register on the lab's own agent conduct, MANUAL
ILLUSTRATIVE -0.35. Same-week Meta arms carried un-rescored from
mechanism 730 (Type A #832) per the #807 pattern: Sep 18 French criminal
probe into smart glasses (-0.45) and Sep 17 German court liability
ruling for fake ads (-0.35), avg -0.40; illustrative delta (Google minus
Meta) +0.05 - a near-NULL spread. The wire applies a comparably
adversarial register to Google's own agent-safety incident and to Meta
enforcement stories within the same 48-hour window. The Reuters-Meta
multi-year content deal (Oct 25 2024) sits on META's side, so the
near-null spread runs OPPOSITE the naive payer-softening prediction -
EXTENDS mechanism 664 (#717) and mechanism 730 (#832) to a third AI-lab
entity on the news desk, and pairs with mechanism 739 (#847): the same
lab-family conduct (agent-hack incidents) drew +0.15 markets-dismissal at
the Breakingviews opinion desk in the same week - register tracks
desk-type, not entity. Cross-wire convergence: BBC and Al Jazeera ran
alarm-register relays of the same Google self-disclosure. MANUAL /
qualitative only; engine NOT run on the arms per the Aug 28 2026 standing
rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False;
verdict directionally_supported_not_proven. NOT a falsification-family
member - register documentation plus replication, not a uniform-prediction
test; falsification ledger holds at 30; no analysis.json update. Novelty
verified pre-commit (zero test_type_a_1022 files; no 'Type A #1022' in
git log; max numeric mechanism_id 843; zero underscore/dash-form 844 keys
by designed keying per #715; block key zero-hit; the reuters.com Gemini
URL, the Global Advisors brief URL, and the BBC URL zero-hit repo-wide;
FT x OpenAI $1.2T rejected as already in corpus via the mechanism 415
family; WIRED/BI/Verge candidate pairs rejected, no publication-owned
arms surfaced); 1020-1024 window third leg D->E->A (anchor + rotation
guard per #565) - Sep 26 2026 19:00 PDT.

Test tally: 51 tests, 11 classes.
EXPECTED_TESTS = 51
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "reuters_google_gemini_breakout_alarm_register_vs_meta_enforcement_register_sep26_2026"
M_ID = 844
ITER = 1022
TYPE_LETTER = "A"
RUN_PDT = "2026-09-26 19:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_844"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_845"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-845"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "845"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1022"), ("E", "1021"), ("D", "1020"), ("C", "1019"), ("B", "1018")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "7cdb3856c64d4a6b79c14abb88777ca8a0e625ee"

REUTERS_URL = "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/"
GLOBALADVISORS_URL = "https://globaladvisors.biz/2026/09/20/global-advisors-news-brief-2026-09-20/"
BBC_URL = "https://www.bbc.com/news/articles/c607l0k72rlvo"
ALJAZEERA_URL = "https://www.aljazeera.com/news/2026/9/19/googles-gemini-ai-hacks-3-companies-in-security-test-then-stops"
META_URLS = [
    "https://www.reuters.com/technology/french-prosecutors-regulators-step-up-scrutiny-smart-glasses-2026-09-18/",
    "https://www.reuters.com/legal/litigation/german-court-rules-meta-liable-fake-ads-instagram-facebook-2026-09-17/",
]
EXPECTED_URLS = [REUTERS_URL, GLOBALADVISORS_URL, BBC_URL, ALJAZEERA_URL] + META_URLS

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "competitor-coverage-research.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 52473, 1346
EXPECTED_TESTS = 51
README_TESTS_AFTER, README_FILES_AFTER = 52473 + EXPECTED_TESTS, 1347

# In-flight work that must stay OUT of this run's staged set (targeted
# staging per the repo-wide traversal lesson): #899 (nytimes.yaml mechanism
# 771 hunk), #938 (test_type_b_938 anchor edit), #900 (untracked Type D test
# file), #1012-wt (working-tree edit on the committed Type A #1012 file).
INFLIGHT = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(PROFILE)


def _block():
    text = _profiles_text()
    start = text.index("  " + MECH_KEY + ":")
    m = re.search(r"^  [a-z0-9_]+:", text[start + 1 :], re.M)
    end = start + 1 + m.start()
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git_log_mains(qualifier):
    out = run_git("log", "--all", "--format=%H %s", "--grep", qualifier).stdout
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type A #1022" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = (
        run_git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    )
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# ---------------------------------------------------------------------------
# 1. Novelty anchor per #565 / #715
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1022:
    def test_single_test_type_a_1022_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_1022") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1022 main commit exists pre-commit; the anchor test pins the
        # main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 844: post-commit max is 844, zero 845
        # keys anywhere. Pre-commit sweeps verified max 843, zero
        # underscore/dash-form 844 keys (designed keying per #715), block
        # key zero-hit, Reuters Gemini URL zero-hit repo-wide.
        assert max(_corpus_ids()) == 844
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []
        assert _repo_grep(NEXT_NUMERIC, roots=("profiles",)) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1020-1024 window, this run is the THIRD leg
# ---------------------------------------------------------------------------
class TestRotationGuard1020_1024Window:
    """#1022 is the Type A third leg of window 1020-1024: D->E->A."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_1020_1024_third_leg(self):
        # Deselected pre-commit per #565 (the #1022 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"1020-1024 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    @pytest.mark.rotation
    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    @pytest.mark.rotation
    def test_predecessor_is_type_e_1021(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("E", "1021"), (
            f"immediate predecessor must be Type E #1021, got {window[1]}"
        )

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # Deselected pre-commit per #565; patched green in the followup.
        # In-flight at this run's checks: #899 Type C (m771),
        # #938 Type B (open anchor edit), #900 Type D (untracked) -
        # none committed yet. (#1012-wt is a working-tree edit on the
        # already-committed Type A #1012, not a new iteration commit.)
        # Match only commit SUBJECTS that ARE an iteration-N commit
        # (subject starts with "Type L #N"), since other commits'
        # subjects/bodies may merely mention them.
        subjects = [
            run_git("log", "--format=%s", "-1", c).stdout.strip()
            for c in run_git("log", "--format=%H", "-8").stdout.splitlines()
        ]
        for n in ("899", "938", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# ---------------------------------------------------------------------------
# 3. Mechanism 844 block structure in competitor-coverage-research.yaml
# ---------------------------------------------------------------------------
class TestMechanism844Structure:
    def test_block_key_exists_in_research_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^  " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 1022" in block
        assert "rotation_type: A" in block
        assert "2026-09-26" in block
        assert "mechanism_id: 844" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication: Reuters" in block
        assert "competitor: Google" in block
        assert "comparator_entity: Meta" in block

    def test_designed_keying_no_underscore_844_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 844 is the only allowed
        # 844 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 844" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert mech["mechanism_id"] == 844
        assert mech["iteration"] == 1022
        assert mech["rotation_type"] == "A"
        assert mech["publication"] == "Reuters"
        assert mech["competitor"] == "Google"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 4. Evidence: arms, dates, URLs, attestation
# ---------------------------------------------------------------------------
class TestMechanism844Arms:
    def test_one_google_arm_two_meta_arms(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert len(mech["google_arms"]) == 1
        assert len(mech["meta_arms"]) == 2

    def test_google_arm_metadata(self):
        block = _block()
        assert "Gemini hacked three companies" in block
        assert "first-known breakout by Google AI" in block
        assert "2026-09-18" in block
        assert "Reuters Staff" in block
        assert "alarm_register_on_lab_own_agent_conduct" in block
        assert "wire_relay_of_wsj_reporting" in block

    def test_google_key_language_verbatim(self):
        block = _block()
        assert (
            "Google''s Gemini model accessed the internet and hacked other companies"
            in block
        )
        assert (
            "the first known example of the company''s AI systems autonomously committing such an act"
            in block
        )

    def test_google_url_relay_attested(self):
        block = _block()
        assert REUTERS_URL in block
        assert "RELAY-ATTESTED ONLY" in block
        assert GLOBALADVISORS_URL in block
        assert BBC_URL in block
        assert ALJAZEERA_URL in block

    def test_meta_arms_carried_from_730(self):
        block = _block()
        assert "carried from mechanism 730" in block
        assert "French prosecutors and regulators step up scrutiny on smart glasses" in block
        assert "German court rules Meta liable for fake ads on Instagram, Facebook" in block

    def test_source_routing_documented_per_arm(self):
        block = _block()
        for routing in (
            "wire_relay_of_wsj_reporting",
            "enforcement_legal_sources",
            "court_ruling_legal_sources",
        ):
            assert routing in block, routing

    def test_all_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_google_reuters_url_zero_hit_elsewhere(self):
        hits = [
            h
            for h in _repo_grep(REUTERS_URL)
            if not h.endswith("competitor-coverage-research.yaml")
            and not h.endswith(OWN_BASENAME)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 5. Scores: delta arithmetic, direction, near-null symmetry framing
# ---------------------------------------------------------------------------
class TestMechanism844Scorer:
    def test_illustrative_tones_and_delta(self):
        block = _block()
        assert "tone_illustrative: -0.35" in block
        assert "tone_illustrative: -0.45" in block
        assert "illustrative_delta_google_minus_meta: 0.05" in block
        assert "google_arm_avg: -0.35" in block
        assert "meta_arm_avg: -0.40" in block

    def test_delta_math(self):
        d = yaml.safe_load(_profiles_text())
        sc = d["cross_publication_findings"][MECH_KEY]["asymmetry_scorer"]
        google_avg = sum(sc["google_arm_tones"]) / len(sc["google_arm_tones"])
        meta_avg = sum(sc["meta_arm_tones"]) / len(sc["meta_arm_tones"])
        assert abs(google_avg - (-0.35)) < 1e-9
        assert abs(meta_avg - (-0.40)) < 1e-9
        assert abs((google_avg - meta_avg) - 0.05) < 1e-9
        assert abs(sc["illustrative_delta_google_minus_meta"] - 0.05) < 1e-9

    def test_extends_664_730_739_framed(self):
        block = _block()
        assert "EXTENDS" in block
        assert "mechanism 664" in block
        assert "mechanism 730" in block
        assert "mechanism 739" in block
        assert "null-tie-wire" in block

    def test_payer_tie_on_meta_side_inverted(self):
        block = _block()
        assert "reuters_meta_deal" in block
        assert "Oct 25, 2024" in block
        assert "OPPOSITE the naive payer-softening prediction" in block

    def test_confounder_strengths_ranked_3_3_3(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        confounders = mech["confounders"]
        assert len(confounders) == 9, confounders
        assert all(c.startswith("STRONG:") for c in confounders[:3])
        assert all(c.startswith("MODERATE:") for c in confounders[3:6])
        assert all(c.startswith("WEAK:") for c in confounders[6:9])

    def test_counterevidence_three(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert len(mech["counterevidence"]) == 3
        assert all("COUNTEREVIDENCE" in c for c in mech["counterevidence"])


# ---------------------------------------------------------------------------
# 6. Statistical discipline: manual illustrative only, no engine
# ---------------------------------------------------------------------------
class TestMechanism844Discipline:
    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block

    def test_falsification_ledger_holds_at_30(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "THIRTIETH present" in block
        assert "THIRTY-FIRST absent" in block

    def test_correlation_not_causation(self):
        block = _block()
        assert "Correlation is not causation" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("664", "730", "739"):
            assert f"- {ref}" in block, ref

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "6 browser.search query sets" in block
        assert "0 browser.open" in block


# ---------------------------------------------------------------------------
# 7. Corpus novelty: max mechanism_id is 844; zero 845 keys
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def _numeric_ids(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                        ids.append(int(m.group(1)))
        return ids

    def test_max_numeric_mechanism_id_is_844(self):
        assert max(self._numeric_ids()) == 844

    def test_zero_next_numeric_845_in_profiles(self):
        r = run_git("grep", "-F", NEXT_NUMERIC, "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_zero_next_underscore_dash_845_repo_wide(self):
        r = run_git("grep", "-F", NEXT_US, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""
        r = run_git("grep", "-F", NEXT_DASH, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        readme = _read(README_PATH)
        assert f"| Tests | {README_TESTS_AFTER} |" in readme
        assert f"Across {README_FILES_AFTER} test files" in readme

    def test_readme_row_1022(self):
        assert ("`tests/" + OWN_BASENAME + "`") in _read(README_PATH)

    def test_architecture_row_1022(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_tree_lists_1022_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


# ---------------------------------------------------------------------------
# 9. Iteration-log entry per #719 (fail pre-commit, green post-entry)
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_newest_entry_is_1022(self):
        headers = re.findall(r"^## #\d+ Type [A-E]", _read(LOG_PATH), re.M)
        assert headers[0] == "## #1022 Type A"

    def test_log_entry_marks_third_leg(self):
        log = _read(LOG_PATH)
        entry = log.split("## #1022 Type A", 1)[1].split("## #", 1)[0]
        assert "THIRD leg of the 1020-1024 window" in entry
        assert "D #1020 -> E #1021 -> A #1022" in entry

    def test_log_entry_precedes_1021(self):
        log = _read(LOG_PATH)
        assert log.index("## #1022 Type A") < log.index("## #1021 Type E")

    def test_log_entry_mechanism_topics(self):
        log = _read(LOG_PATH)
        entry = log.split("## #1022 Type A", 1)[1].split("## #", 1)[0]
        assert "mechanism 844" in entry
        assert "Gemini" in entry
        assert "Reuters x Google" in entry


# ---------------------------------------------------------------------------
# 10. Push readiness: ASCII, staged set, concurrency, hashes
# ---------------------------------------------------------------------------
class TestPushReadiness:
    def test_new_block_ascii_only_no_em_dash(self):
        block = _block()
        for line in block.splitlines():
            assert all(ord(c) < 128 for c in line), f"non-ASCII: {line[:60]}"
        assert "\u2014" not in block

    def test_no_raw_own_key_literal_in_this_file(self):
        src = _read("tests/" + OWN_BASENAME)
        assert MECH_ID_MARKER not in src

    def test_no_blob_url_in_this_file(self):
        # Own file must not carry the repo blob URL, or it becomes a
        # self-circular search key. Needle format-built per #1016.
        needle = "github.com" + "/rayhe/mediascope" + "/blob"
        assert needle not in _read("tests/" + OWN_BASENAME)

    def test_inflight_concurrency_stays_unstaged(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        assert staged.isdisjoint(INFLIGHT), staged & INFLIGHT


# ---------------------------------------------------------------------------
# 11. Date grounding
# ---------------------------------------------------------------------------
class TestDateGrounding1022:
    def test_sep_26_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 26).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 26, 19, 0).strftime("%H:%M") == "19:00"
