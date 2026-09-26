"""Type C #1014: Stack Overflow dual-AI-payer architecture - OverflowAPI legs with
Google Cloud (Feb 29 2024) and OpenAI (May 6 2024) - FIRST developer-knowledge
dual-payer publisher in the corpus; both legs undisclosed-fee (unweightable per
m735); Meta $0 bounded absence; mechanism 840 in profiles/competitor-entities.yaml,
connects_to [594, 621, 696, 735]; FIFTH and CLOSING leg of the 1010-1014 window
D->E->A->B->C per #565 (anchor + rotation guard); 52 tests, 10 classes.

Qualitative financial-incentive mapping per the Aug 28 2026 standing rule: tone
NOT_SCORED, p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT
run, no_analysis_json_update True, NOT artifact-grade, NOT falsification-family
member, ledger holds at 30, verdict directionally_supported_not_proven. 0
browser.open (excerpt-bounded per #503); browser.search query sets for the
Google-leg and OpenAI-leg discovery. doc-sync (52070/1338 -> 52122/1339; +52/+1,
venv python).

The anchor test, rotation-guard class, staged-set test, and hash-placeholder test
fail pre-commit by design (anchor patched post-commit; rotation guard checks
committed predecessors; staging happens right before the commit; hashes filled
by the log-hash followup). Novelty tests: run pre-commit
(`-m 'not anchor and not rotation'`); the zero-form sweeps are verified by the
pre-commit grep battery documented in the iteration log instead.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
PROFILE = os.path.join(REPO, "profiles", "competitor-entities.yaml")

THIS_FILE = "test_type_c_1014_stackoverflow_dual_ai_payer_google_openai_overflowapi_sep26_9am.py"
BLOCK_KEY = "type_c_1014_stackoverflow_dual_ai_payer_google_openai_overflowapi_sep26_9am"
ITERATION = 1014
ITERATION_TYPE = "C"
MECHANISM = 840
NEXT_NUM = 841
EXPECTED_TESTS = 52

# Patched by the anchor followup (#565): full 40-hex of the main commit.
ANCHORED_SHA = "2362c57410284fde6698e2a9f6abd33d227c28b0"

NEW_URLS = [
    "https://stackoverflow.co/company/press/archive/google-cloud-strategic-gen-ai-partnership/",
    "https://www.devopsdigest.com/stack-overflow-partners-with-google-cloud?destination=node/12261",
    "https://vuink.com/post/grpupehapu-d-dpbz/2024/02/29/google-brings-stack-overflows-knowledge-base-to-gemini",
    "https://techstartups.com/2024/05/06/openai-partners-with-stack-overflow-to-supercharge-developer-experience/",
    "https://readwrite.com/openai-and-stack-overflow-sign-deal-to-boost-chatgpt/",
    "https://www.theregister.com/software/2024/05/07/stack-overflow-and-openai-agree-to-use-each-other/1141862?td=amp-keepreading",
    "https://www.engadget.com/ai/stack-overflow-and-openai-partner-up-to-bring-more-technical-knowledge-into-chatgpt-184524095.html",
    "https://aitoolradar.io/blog/how-ai-broke-stack-overflow",
]

CONNECTS_TO = [594, 621, 696, 735]

README_TESTS_BEFORE = 52070
README_FILES_BEFORE = 1338
README_TESTS_AFTER = 52122
README_FILES_AFTER = 1339

STAGED_SET = {
    "profiles/competitor-entities.yaml",
    "tests/" + THIS_FILE,
    "iteration-log.md",
    "README.md",
    "docs/ARCHITECTURE.md",
}

PREDECESSOR_SHAS = {
    "a11199707577599ea5410e26f3a788d58dbc01e4",  # #1013 Type B main
    "2fc529f6596ff6d8344f0a62755715db6329226e",  # #1013 Type B anchor
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True
    )


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_block():
    with open(PROFILE, encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc[BLOCK_KEY]


def worktree_max_mechanism_id():
    n7 = "mechanism" + "_id" + ":"
    maxid = 0
    for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
            maxid = max(maxid, int(m.group(1)))
    return maxid


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1014:
    def test_single_new_test_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "test_type_c_1014*"))
        assert [os.path.basename(f) for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_unpatched_pre_commit(self):
        # Fails post-anchor-followup by design: ANCHORED_SHA is patched to the
        # main commit SHA once it lands (#565).
        assert ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP"

    def test_novelty_claim_present(self):
        block = load_block()
        assert "FIRST" in block["novelty"]
        assert "Stack Overflow" in block["novelty"]
        assert "dual-AI-payer" in block["novelty"]

    def test_zero_underscore_or_dash_840_keys_pre_commit(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying (colon-form only) keeps this green even
        # after the mechanism 840 block is staged.
        n1 = "mechanism" + "_840"
        n2 = "mechanism" + "-840"
        for needle in (n1, n2):
            r = run_git("grep", "-l", needle, "--",
                        "profiles/", "tests/", "docs/", "iteration-log.md")
            assert r.stdout.strip() == "", (needle, r.stdout)


# ---------------------------------------------------------------------------
# 2. Rotation guard: FIFTH and CLOSING leg of the 1010-1014 window
# ---------------------------------------------------------------------------
class TestRotationGuard1014:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1010 Type D" in text
        assert "## #1011 Type E" in text
        assert "## #1012 Type A" in text
        assert "## #1013 Type B" in text
        assert "1010-1014" in text

    @pytest.mark.rotation
    def test_fifth_leg_of_1010_to_1014_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"
        assert "1010-1014 window" in block["rotation_transparency"]
        assert "FIFTH leg" in block["rotation_transparency"]
        assert "CLOSING the window" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1013_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1013")
        assert r.stdout.strip() != ""
        assert os.path.exists(
            os.path.join(
                REPO,
                "tests",
                "test_type_b_1013_samuel_gibbs_guardian_meta_register_"
                "temporal_shift_vs_apple_vision_pro_aspirational_sep26_8am.py",
            )
        )

    @pytest.mark.rotation
    def test_no_successor_1015_type_d_commit_yet(self):
        # The next window opens at #1015 Type D; nothing of it may exist yet.
        r = run_git("log", "--oneline", "--grep", "Type D #1015")
        assert r.stdout.strip() == ""
        assert "## #1015" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_c_1014_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type C #1014")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 840 block content
# ---------------------------------------------------------------------------
class TestMechanism840Content:
    def test_block_key_unique_at_zero_indent(self):
        with open(PROFILE, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        matches = [k for k in doc if k == BLOCK_KEY]
        assert matches == [BLOCK_KEY]
        assert doc[BLOCK_KEY]["block_key"] == BLOCK_KEY

    def test_mechanism_id_iteration_type_date_time(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "09:00"

    def test_type_and_label(self):
        block = load_block()
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_no_cash_payment_claim(self):
        # Neither lab may be called a cash payer: both legs are
        # undisclosed-fee, and the block must say so explicitly.
        block = load_block()
        assert "no cash amounts reported in any source" in block["finding"]
        assert "NO cash-payment claim is made for either leg" in block["incentive_geometry"]["fee_status"]
        assert "UNDISCLOSED" in block["google_leg"]["financial_terms"]
        assert "UNDISCLOSED" in block["openai_leg"]["financial_terms"]

    def test_verdict_directionally_supported_not_proven(self):
        assert load_block()["verdict"] == "directionally_supported_not_proven"

    def test_researcher_author(self):
        block = load_block()
        assert block["researcher"] == "Kit (with Ray)"
        assert block["author"] == "Kit (with Ray)"

    def test_leg_dates(self):
        block = load_block()
        assert block["google_leg"]["announced"] == "2024-02-29"
        assert block["openai_leg"]["announced"] == "2024-05-06"
        assert block["google_leg"]["partner"] == "Google Cloud"
        assert block["openai_leg"]["partner"] == "OpenAI"

    def test_reciprocal_structure_documented(self):
        block = load_block()
        assert "reciprocal" in block["incentive_geometry"]["reciprocity"].lower()
        assert "OverflowAPI" in block["google_leg"]["product_surface"]
        assert "OverflowAPI" in block["openai_leg"]["product_surface"]


# ---------------------------------------------------------------------------
# 4. Dual-payer incentive architecture
# ---------------------------------------------------------------------------
class TestDualPayerArchitecture1014:
    def test_dual_payer_family_membership(self):
        family = load_block()["incentive_geometry"]["family"]
        for member in ("594", "621", "696"):
            assert member in family, member
        assert "News Corp" in family

    def test_connects_to_all_exist(self):
        corpus = _read(PROFILE)
        for mid in CONNECTS_TO:
            assert ("mechanism_id: %d" % mid) in corpus, mid

    def test_unweightable_per_m735(self):
        block = load_block()
        assert "cannot be dollar-weighted" in block["finding"]
        assert "m735" in block["finding"]
        assert "Unweightable in dollar terms" in block["incentive_geometry"]["fee_status"]

    def test_meta_zero_bounded_absence(self):
        block = load_block()
        assert "Meta has no OverflowAPI leg" in block["finding"]
        assert "a $0 anchor on the Meta side" in block["finding"]
        assert "bounded absence" in block["incentive_geometry"]["meta_leg"]
        assert "m732" in block["incentive_geometry"]["meta_leg"]

    def test_both_legs_undisclosed_fee(self):
        block = load_block()
        for leg in ("google_leg", "openai_leg"):
            assert "UNDISCLOSED" in block[leg]["financial_terms"], leg

    def test_non_exclusive_overflowapi(self):
        assert "NON-EXCLUSIVE" in load_block()["google_leg"]["product_surface"]

    def test_first_developer_knowledge_publisher(self):
        block = load_block()
        assert "FIRST developer-knowledge" in block["novelty"]
        assert "non-news" in block["incentive_geometry"]["family"]


# ---------------------------------------------------------------------------
# 5. Source corroboration
# ---------------------------------------------------------------------------
class TestSourceCorroboration1014:
    def test_eight_sources(self):
        assert len(load_block()["sources"]) == 8

    def test_primary_stackoverflow_press_present(self):
        urls = [s["url"] for s in load_block()["sources"]]
        assert any("stackoverflow.co/company/press" in u for u in urls)

    def test_openai_leg_sources_present(self):
        urls = [s["url"] for s in load_block()["sources"]]
        openai_urls = [u for u in urls if "openai" in u]
        assert len(openai_urls) >= 3, openai_urls

    def test_google_leg_sources_present(self):
        urls = [s["url"] for s in load_block()["sources"]]
        google_urls = [u for u in urls if "google" in u]
        assert len(google_urls) >= 3, google_urls

    def test_new_urls_first_appearance(self):
        text = _read(PROFILE)
        for url in NEW_URLS:
            assert text.count(url) == 1, url

    def test_excerpt_bounded_note_honest(self):
        note = load_block()["excerpt_bounded_note"]
        assert "0 browser.open" in note
        assert "NOT opened" in note


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1014:
    def test_tone_not_scored(self):
        assert load_block()["tone_scores"] == "NOT_SCORED"

    def test_engine_not_run_and_no_analysis_update(self):
        block = load_block()
        assert block["engine_run"] is False
        assert block["no_analysis_json_update"] is True

    def test_artifact_grade_false(self):
        assert load_block()["artifact_grade"] is False

    def test_excerpt_bounded_browser_opens_zero(self):
        block = load_block()
        assert block["excerpt_bounded"] is True
        assert block["browser_opens"] == 0
        assert block["verification"]["browser_opens"] == 0

    def test_correlation_not_causation(self):
        block = load_block()
        assert "Correlation, not causation" in block["finding"]
        assert "Hypothesis-generating only" in block["finding"]

    def test_confounders_eight_ranked_strong_first(self):
        confs = load_block()["confounders"]
        assert len(confs) == 8
        strengths = [c["strength"] for c in confs]
        assert strengths.count("strong") == 3
        assert strengths.count("medium") == 3
        assert strengths.count("weak") == 2
        assert strengths[:3] == ["strong", "strong", "strong"]

    def test_counterevidence_five(self):
        assert len(load_block()["counterevidence"]) == 5

    def test_strongest_counterargument_present(self):
        sca = load_block()["strongest_counterargument"]
        assert sca
        assert "distress monetization" in sca
        assert "Correlation, not causation" in sca


# ---------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_c_1014_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_c_1014*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_840_post_staging(self):
        # 839 in-tree pre-commit; 840 once this run's block is appended.
        # The in-flight #899 m771 hunk does not change the max.
        assert worktree_max_mechanism_id() == MECHANISM

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "84" + "1"
        out = run_git("grep", "-nE",
                      "mechanism_id:[[:space:]]*" + d1 + "([^0-9]|$)",
                      "--", "profiles/").stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude own file (the sweep-carrier for 841).
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "84" + "1"
        n2 = "mech" + "anism" + "-" + "84" + "1"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1014:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block = load_block()
        assert block["falsification_ledger"] == 30
        assert "holds at 30" in block["falsification_note"]

    def test_falsification_note_pinned_wordings(self):
        note = load_block()["falsification_note"]
        assert "THIRTIETH" in note
        assert "#1000" in note


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1014:
    def test_readme_stats_table_updated(self):
        row = "| Tests | %d | Across %d test files |" % (
            README_TESTS_AFTER, README_FILES_AFTER)
        assert row in _read(README), row

    def test_readme_table_row_for_1014(self):
        readme = _read(README)
        assert ("`tests/" + THIS_FILE + "`") in readme
        assert ("| %d |" % EXPECTED_TESTS) in readme

    def test_architecture_tree_row_for_1014(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 10. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1014:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m840 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1013) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1014 must be present.
        text = _read(LOG)
        entry = text.split("## #1014")[1].split("## #1013")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h not in PREDECESSOR_SHAS
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrent_files_untouched_by_this_run(self):
        # The in-flight #899/#938/#900 working-tree edits are owned by
        # their runs; this run stages only its own files.
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_"):
            assert not any(f in l for l in staged), f
        # The #899 in-flight nytimes.yaml hunk marker is still intact in
        # the worktree (untouched by this run).
        r = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r.stdout
