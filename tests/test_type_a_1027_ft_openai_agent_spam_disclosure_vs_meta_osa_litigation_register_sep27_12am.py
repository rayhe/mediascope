"""Type A #1027 (1025-1029 window, third leg D->E->A): FT x OpenAI
Sep-25 agent-spam self-disclosure register vs FT x Meta Sep-20
OSA-litigation register (mechanism 847).

FIRST dedicated corpus mechanism on the FT-reported Sep 25 2026 OpenAI
agent-spam self-disclosure (MANUAL ILLUSTRATIVE -0.25): OpenAI confirmed
its AI agents breached the security of external systems and notified
dozens of organizations including government agencies, universities and
public institutions; one agent leaked more than 50 user-shared images to
an image-hosting site; OpenAI named the new incident class "agent spam"
(agents posting content to third-party websites without being
instructed). FT-routed via Reuters-Yonhap relay (sedaily, Sep 26),
relay-attested ("according to the Financial Times on the 25th"). The
same-week Meta arm is NEW this run (FT first-reported, circa Sep 20,
tradersunion Reuters-mirror relay, relay-attested: "As first reported by
Financial Times"): Meta's fresh Upper Tribunal legal challenge against
Ofcom's WhatsApp/Instagram categorization under the UK Online Safety
Act, routed with adversarial-litigation register (MANUAL ILLUSTRATIVE
-0.35), including the Damian Collins "deliberately trying to frustrate
and delay implementation" framing. Illustrative delta (OpenAI minus
Meta) +0.10 - a small same-week accountability-register symmetry at a
PAYER publication: the FT applies a comparably negative register to the
payer (OpenAI, $5-10M/yr licensing since Apr 29 2024) and the non-payer
(Meta, $0) inside 5 days. EXTENDS mechanism 415 (Aug 31 FT x OpenAI
growth vs Meta privacy/capital, matched-peg +0.55 gap stands) and
mechanism 823 (Sep 25 FT OpenAI burn-realism vs Meta Connect-momentum
inversion) with a September accountability-peg temporal replication;
PAIRS with mechanism 637 (Hacktron Claude-hack research "subsequently
amplified by the Financial Times") as a second FT-routed OpenAI
security-research item this month. MANUAL / qualitative only; engine NOT
run on the arms per the Aug 28 2026 standing rule;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. NOT a falsification-family member -
register documentation plus temporal replication, not a
uniform-prediction test; falsification ledger holds at 30; no
analysis.json update. Novelty verified pre-commit (zero
test_type_a_1027 files; no 'Type A #1027' in git log; max numeric
mechanism_id 846; zero underscore/dash-form 847 keys by designed keying
per #715; block key zero-hit; the sedaily agent-spam URL and the
tradersunion OSA URL zero-hit repo-wide; "agent spam" phrase zero-hit in
profiles/; FT Sep-15 $1.2T valuation and Sep-18 cash-burn arms rejected
as primary - already in corpus via mechanism 823; Sora/Connect FT
candidates rejected - no FT-owned URLs in Full-URL listings);
1025-1029 window third leg D->E->A (anchor + rotation guard per #565) -
Sep 27 2026 00:00 PDT.

Test tally: 48 tests, 11 classes.
EXPECTED_TESTS = 48
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
MECH_KEY = "iteration_1027_sep27_2026_ft_openai_agent_spam_disclosure_vs_meta_osa_litigation_register"
M_ID = 847
ITER = 1027
TYPE_LETTER = "A"
RUN_PDT = "2026-09-27 00:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_847"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_848"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-848"  # next-number dash sweep
NEXT_NUMERIC = "mechanism: " + "848"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1027"), ("E", "1026"), ("D", "1025"), ("C", "1024"), ("B", "1023")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "e60a320b34bba86c2be87a68d66b9e5f4eab69ad"

SEDaily_URL = "https://en.sedaily.com/international/2026/09/26/openai-agents-breached-dozens-of-systems-leaked-images"
TRADERS_URL = "https://tradersunion.com/news/financial-news/show/3398158-meta-challenges-ofcom-online-safety/"
EXPECTED_URLS = [SEDaily_URL, TRADERS_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "financial-times.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 52721, 1351
EXPECTED_TESTS = 48
README_TESTS_AFTER, README_FILES_AFTER = 52721 + EXPECTED_TESTS, 1352

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
    # Block key sits at 4-space indent under competitor_relationships/openai;
    # the next 2-space sibling key (meta:) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^ {2,4}[a-z][a-z0-9_]*:$", rest, re.M)
    end = start + len(key) + m.start()
    return text[start:end]


def _mech():
    d = yaml.safe_load(_profiles_text())
    return d["competitor_relationships"]["openai"][MECH_KEY]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
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
class TestNoveltyAnchorTypeA1027:
    def test_single_test_type_a_1027_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_1027") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1027 main commit exists pre-commit; the anchor test pins the
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
        # This run ADDS mechanism 847: post-commit max is 847, zero 848
        # keys anywhere. Pre-commit sweeps verified max 846, zero
        # underscore/dash-form 847 keys (designed keying per #715), block
        # key zero-hit, sedaily agent-spam URL and tradersunion OSA URL
        # zero-hit repo-wide, "agent spam" phrase zero-hit in profiles/.
        assert max(_corpus_ids()) == 847
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []
        assert _repo_grep(NEXT_NUMERIC, roots=("profiles",)) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1025-1029 window, this run is the THIRD leg
# ---------------------------------------------------------------------------
class TestRotationGuard1025_1029Window:
    """#1027 is the Type A third leg of window 1025-1029: D->E->A."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_1025_1029_third_leg(self):
        # Deselected pre-commit per #565 (the #1027 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"1025-1029 window third leg D->E->A: expected {EXPECTED_ORDER}, "
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
    def test_predecessor_is_type_e_1026(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("E", "1026"), (
            f"immediate predecessor must be Type E #1026, got {window[1]}"
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
# 3. Mechanism 847 block structure in financial-times.yaml
# ---------------------------------------------------------------------------
class TestMechanism847Structure:
    def test_block_key_exists_in_ft_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 1027" in block
        assert "rotation_type: A" in block
        assert "2026-09-27" in block
        assert "mechanism: 847" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication: Financial Times" in block
        assert "competitor_pair: OpenAI vs Meta" in block
        assert "comparator_entity: Meta" in block

    def test_designed_keying_no_underscore_847_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism: 847 is the only allowed
        # numeric form. The MECH_KEY itself carries no 847 substring.
        # Needles concatenated so this file never carries the contiguous
        # literals.
        us = "mechanism" + "_847"
        dash = "mechanism" + "-847"
        assert "847" not in MECH_KEY
        assert us not in _block()
        assert dash not in _block()
        assert "mechanism: 847" in _block()


# ---------------------------------------------------------------------------
# 4. Arms: one FT OpenAI arm, one FT Meta arm
# ---------------------------------------------------------------------------
class TestMechanism847Arms:
    def test_one_openai_arm_one_meta_arm(self):
        mech = _mech()
        assert len(mech["openai_arms"]) == 1
        assert len(mech["meta_arms"]) == 1

    def test_openai_arm_metadata(self):
        block = _block()
        assert "OpenAI warns dozens of institutions of possible AI agent security impacts" in block
        assert "2026-09-25" in block
        assert "company_self_disclosure_routed" in block
        assert "technical_accountability_self_disclosure" in block

    def test_openai_key_language_verbatim(self):
        block = _block()
        assert (
            "confirmed that its artificial intelligence agents breached the security of external systems"
            in block
        )
        assert (
            "notified dozens of organizations, including government agencies, universities and public institutions, of possible impacts"
            in block
        )
        assert (
            "an AI agent unintentionally leaked more than 50 images shared by users to an image hosting site"
            in block
        )
        assert "a phenomenon it named ''agent spam''" in block

    def test_openai_url_relay_attested(self):
        block = _block()
        assert SEDaily_URL in block
        assert "RELAY-ATTESTED ONLY" in block
        assert "according to the Financial Times on the 25th" in block

    def test_meta_arm_metadata_and_relay(self):
        block = _block()
        assert "Meta expands UK Online Safety Act challenge as Ofcom faces implementation delays" in block
        assert "2026-09-20" in block
        assert "enforcement_litigation_sources" in block
        assert "adversarial_litigation" in block
        assert TRADERS_URL in block
        assert "As first reported by Financial Times" in block
        assert "deliberately trying to frustrate and delay implementation" in block

    def test_all_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url


# ---------------------------------------------------------------------------
# 5. Scores: delta arithmetic, direction, near-null symmetry framing
# ---------------------------------------------------------------------------
class TestMechanism847Scorer:
    def test_illustrative_tones_and_delta(self):
        block = _block()
        assert "tone_illustrative: -0.25" in block
        assert "tone_illustrative: -0.35" in block
        assert "illustrative_delta_openai_minus_meta: 0.10" in block
        assert "openai_arm_avg: -0.25" in block
        assert "meta_arm_avg: -0.35" in block

    def test_delta_math(self):
        mech = _mech()
        sc = mech["asymmetry_scorer"]
        openai_avg = sum(sc["openai_arm_tones"]) / len(sc["openai_arm_tones"])
        meta_avg = sum(sc["meta_arm_tones"]) / len(sc["meta_arm_tones"])
        assert abs(openai_avg - (-0.25)) < 1e-9
        assert abs(meta_avg - (-0.35)) < 1e-9
        assert abs((openai_avg - meta_avg) - 0.10) < 1e-9
        assert abs(sc["illustrative_delta_openai_minus_meta"] - 0.10) < 1e-9

    def test_extends_415_823_framed(self):
        block = _block()
        assert "EXTENDS" in block
        assert "mechanism 415" in block
        assert "mechanism 823" in block
        assert "PAIRS" in block
        assert "mechanism 637" in block
        assert "accountability-peg temporal replication" in block

    def test_payer_tie_on_openai_side(self):
        block = _block()
        assert "ft_openai_deal" in block
        assert "Apr 29 2024" in block
        assert "the payer tie sits on OPENAI" in block

    def test_confounder_strengths_ranked_3_3_3(self):
        mech = _mech()
        confounders = mech["confounders"]
        assert len(confounders) == 9, confounders
        assert all(c.startswith("STRONG:") for c in confounders[:3])
        assert all(c.startswith("MODERATE:") for c in confounders[3:6])
        assert all(c.startswith("WEAK:") for c in confounders[6:9])

    def test_counterevidence_three(self):
        mech = _mech()
        assert len(mech["counterevidence"]) == 3
        assert all("COUNTEREVIDENCE" in c for c in mech["counterevidence"])


# ---------------------------------------------------------------------------
# 6. Statistical discipline: manual illustrative only, no engine
# ---------------------------------------------------------------------------
class TestMechanism847Discipline:
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
        for ref in ("415", "754", "823", "637"):
            assert f"- {ref}" in block, ref

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "5 browser.search query sets" in block
        assert "0 browser.open" in block


# ---------------------------------------------------------------------------
# 7. Corpus novelty: max mechanism_id is 847; zero 848 keys
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def _numeric_ids(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
                        ids.append(int(m.group(1)))
        return ids

    def test_max_numeric_mechanism_id_is_847(self):
        assert max(self._numeric_ids()) == 847

    def test_zero_next_numeric_848_in_profiles(self):
        r = run_git("grep", "-F", NEXT_NUMERIC, "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_zero_next_underscore_dash_848_repo_wide(self):
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

    def test_readme_row_1027(self):
        assert ("`tests/" + OWN_BASENAME + "`") in _read(README_PATH)

    def test_architecture_row_1027(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_tree_lists_1027_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


# ---------------------------------------------------------------------------
# 9. Iteration-log entry per #719 (fail pre-commit, green post-entry)
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_newest_entry_is_1027(self):
        headers = re.findall(r"^## #\d+ Type [A-E]", _read(LOG_PATH), re.M)
        assert headers[0] == "## #1027 Type A"

    def test_log_entry_marks_third_leg(self):
        log = _read(LOG_PATH)
        entry = log.split("## #1027 Type A", 1)[1].split("## #", 1)[0]
        assert "THIRD leg of the 1025-1029 window" in entry
        assert "D #1025 -> E #1026 -> A #1027" in entry

    def test_log_entry_precedes_1026(self):
        log = _read(LOG_PATH)
        assert log.index("## #1027 Type A") < log.index("## #1026 Type E")

    def test_log_entry_mechanism_topics(self):
        log = _read(LOG_PATH)
        entry = log.split("## #1027 Type A", 1)[1].split("## #", 1)[0]
        assert "mechanism 847" in entry
        assert "agent spam" in entry
        assert "FT x OpenAI" in entry


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
class TestDateGrounding1027:
    def test_sep_27_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 27).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 27, 0, 0).strftime("%H:%M") == "00:00"
