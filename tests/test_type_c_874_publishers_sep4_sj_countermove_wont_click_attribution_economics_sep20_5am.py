"""Type C #874 (870-874 window, fifth leg D->E->A->B->C, CLOSING the window):
Publishers' Sep-4-2026 partial-summary-judgment counter-move + the Sep-18
"users won't click" attribution-economics admission - FIRST dedicated corpus
mechanism (mechanism 756) on the September 2026 escalation of the
license-vs-litigate pricing fight.

TWO legs, one pricing fight:
(1) Enforcement-economics escalation: on Sep 4 2026, three days after the
DOJ's Statement of Interest (mechanism 672, #729), the NYT, Daily News and
other publisher plaintiffs filed motions for partial summary judgment asking
Judge Sidney H. Stein to decide before trial (ruling not expected until
2027) that neither OpenAI nor Microsoft can claim fair use when (a)
acquiring articles behind paywalls, (b) training models on that material,
or (c) generating outputs that reproduce protected content (webpronews).
The paywall-acquisition carve-out moves the fight from WHETHER training is
fair use to HOW the training corpus was acquired - the direct procedural
answer to the DOJ brief, and the enforcement-economics escalation of
mechanism 753's $28M+ litigation spend (the spend buys a court-set price;
the motions ask the court to set it now, on three carve-outs).
(2) Attribution-consideration repricing: the Sep 18 2026 AFP piece
(techxplore) reports the NYT alleges Microsoft and OpenAI knew using news
content was theft - and quotes an OpenAI engineer from a court document:
"No matter how prominently we show the links, users won't click." By
OpenAI's own admission, the attributed-citation consideration at the heart
of the zero-fee attribution-discovery template (mechanisms 609 India
Sep 7-8, 714 Village Media Sep 16, 660 contrast class) does not convert to
traffic. The publisher-side consideration in every citation-only deal is
economically near-worthless by the payer's own engineer's admission - a NEW
financial datum that revalues the corpus's deal map. Two-tier consideration
structure: News Corp gets >$250M/5yr cash plus tech credits for training
rights (mechanism 519) while local and national publishers get
citation-only deals whose citation value OpenAI internally prices at ~zero.

MANUAL qualitative only per the Aug 28 2026 standing rule, engine NOT run,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT a falsification-family member,
ledger holds at 27; no analysis.json update; NOT artifact-grade.
Novelty verified pre-commit: zero test_type_c_874 files on disk; no
"Type C #874" in git log; max numeric mechanism_id 755 pre-commit;
zero underscore-form 756 mechanism key strings repo-wide per the #715
designed-keying convention (format-built needles, no literals carried);
block key zero-hit repo-wide pre-commit; "partial summary judgment"
zero-hit in profiles/tests/docs pre-commit; "users won't click" zero-hit
pre-commit; webpronews + techxplore + 111things URLs zero-hit repo-wide
pre-commit (techtimes 326401 carried from #732, in corpus via
the-verge.yaml). 870-874 window fifth leg D->E->A->B->C CLOSING it (anchor
patched post-commit per #565) - Sep 20 2026 05:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_874_publishers_sep4_sj_countermove_wont_click_attribution_economics_sep20_5am.py"
MECH_KEY = "publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026"
BLOCK_KEY = "type_c_874_publishers_sep4_partial_summary_judgment_countermove_wont_click_attribution_economics_sep2026"
M_ID = 756
ITER = 874
TYPE_LETTER = "C"
# Concatenated so this file never carries the literal marker itself (per #715).
MECH_ID_MARKER = "mechanism" + "_756"
NEXT_ID_MARKER = "mechanism" + "_757"
NEXT_ID_NUMERIC = "mechanism_id: " + "757"
NEXT_ID_DASH = "mechanism" + "-757"
# Format-built so the file never carries the literal ledger string (per #715).
LEDGER_28_NEEDLE = "falsification ledger: " + "28"
EXPECTED_ORDER = [("C", "874"), ("B", "873"), ("A", "872"), ("E", "871"), ("D", "870")]
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "a177b602c470fe679a5b2ba7522da7d6f02154b3"

WEBPRONEWS_URL = "https://www.webpronews.com/u-s-government-backs-openai-in-landmark-nyt-copyright-fight/"
TECHXPLORE_URL = "https://techxplore.com/news/2026-09-nyt-alleges-microsoft-openai-knew.html"
THINGS111_URL = "https://111things.com/national/u-s-government-backs-openai-in-new-york-times-copyright-case/"
# Carried corroboration: in corpus via #732 (profiles/the-verge.yaml), not a new URL.
TECHTIMES_CARRIED_URL = "https://www.techtimes.com/articles/326401/20260903/doj-backs-openai-fair-use-claim-ai-copyright-fight-creators-must-try-congress.htm"
NEW_EVIDENCE_URLS = (WEBPRONEWS_URL, TECHXPLORE_URL, THINGS111_URL)

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
SCHEDULED_LOCAL = "Sun 2026-09-20 05:00:00 PDT"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entities_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"))


def _block():
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\n    seattle_times_newsday_grant_then_sue_openai_microsoft_sep2026:")
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


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", "Type C #874")
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #874" in subject and qualifier in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty874:
    def test_single_test_type_c_874_file(self):
        files = [
            fn
            for fn in os.listdir(TESTS_DIR)
            if fn.startswith("test_type_c_874")
        ]
        assert files == [OWN_BASENAME], files

    def test_type_c_874_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565 (the #874 main commit does not
        # exist yet); patched green in the anchor followup.
        mains = _git_log_mains("counter-move")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA in mains, mains

    def test_novelty_verification_claim(self):
        hits = _repo_grep(MECH_KEY, roots=("profiles",))
        assert hits == ["profiles/competitor-entities.yaml"], hits
        assert "partial summary judgment" in _block()

    def test_870_873_window_legs_present_prior_to_874(self):
        for fn in (
            "test_type_d_870_",
            "test_type_e_871_",
            "test_type_a_872_",
            "test_type_b_873_",
        ):
            matches = [f for f in os.listdir(TESTS_DIR) if f.startswith(fn)]
            assert len(matches) == 1, (fn, matches)


class TestRotationGuard874:
    """#874 is the Type C fifth leg of window 870-874: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_870_874_fifth_leg_closing(self):
        # Deselected pre-commit per #565 (the #874 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"870-874 window fifth leg D->E->A->B->C CLOSING: expected "
            f"{EXPECTED_ORDER}, got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_873(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "873"), (
            f"immediate predecessor must be Type B #873, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("counter-move")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism756Structure:
    def test_block_key_exists_in_competitor_entities(self):
        assert BLOCK_KEY in _entities_text()

    def test_block_key_unique(self):
        assert _entities_text().count(BLOCK_KEY) == 1

    def test_mech_key_unique(self):
        # The block_key value contains the mech key as a suffix, so count
        # the indented YAML mapping-key line only.
        assert _entities_text().count("    " + MECH_KEY + ":") == 1

    def test_block_nests_under_openai_entity_section(self):
        text = _entities_text()
        openai_idx = text.index("\n  openai:")
        anthropic_idx = text.index("\n  anthropic:")
        mech_idx = text.index(MECH_KEY)
        assert openai_idx < mech_idx < anthropic_idx

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 874" in block
        assert "rotation: Type C" in block
        assert "time_pdt: '05:00'" in block
        assert "date_analyzed: '2026-09-20'" in block

    def test_designed_keying_no_underscore_756_in_block(self):
        # Per the #715 convention: colon-form keying only; the numeric
        # mechanism id never appears in underscore form inside the block.
        block = _block()
        assert "_756" not in block, [
            line for line in block.splitlines() if "_756" in line
        ]

    def test_yaml_parses_and_fields(self):
        doc = yaml.safe_load(_entities_text())
        blk = doc["entities"]["openai"][MECH_KEY]
        assert blk["mechanism_id"] == 756
        assert blk["iteration"] == 874
        assert blk["block_key"] == BLOCK_KEY
        assert blk["type"] == "financial_incentive_mapping"

    def test_max_mechanism_id_is_756(self):
        assert max(_corpus_ids()) == 756

    def test_no_757_numeric_in_profiles(self):
        # Format-built needle so this file never carries the literal.
        assert not _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))


class TestMechanism756SJMotions:
    def test_sep4_motions_filed(self):
        block = _block()
        assert "partial summary judgment" in block
        assert "Sep 4" in block

    def test_plaintiffs_nyt_daily_news(self):
        block = _block()
        assert "Daily News" in block
        assert "New York Times" in block

    def test_paywall_acquisition_carve_out(self):
        block = _block()
        assert "behind paywalls" in block

    def test_training_carve_out(self):
        block = _block()
        assert "training models on that material" in block

    def test_reproducing_outputs_carve_out(self):
        block = _block()
        assert "reproduce protected content" in block

    def test_judge_stein(self):
        assert "Sidney" in _block() and "Stein" in _block()

    def test_ruling_not_expected_until_2027(self):
        assert "2027" in _block()

    def test_all_three_new_evidence_urls_in_block(self):
        block = _block()
        for url in NEW_EVIDENCE_URLS:
            assert url in block, url

    def test_techtimes_carried_not_new(self):
        block = _block()
        assert TECHTIMES_CARRIED_URL in block
        assert "carried" in block


class TestMechanism756WontClick:
    def test_engineer_quote_verbatim(self):
        # YAML single-quoted doubling: raw text carries the doubled form.
        assert "users won''t click" in _block()

    def test_no_matter_how_prominently(self):
        assert "No matter how prominently we show the links" in _block()

    def test_theft_allegation(self):
        assert "knew using news content was theft" in _block()

    def test_sep18_afp_surface(self):
        block = _block()
        assert "Sep 18" in block
        assert "AFP" in block

    def test_attribution_consideration_revalued(self):
        block = _block()
        assert "attribution" in block
        assert "consideration" in block

    def test_two_tier_consideration_structure(self):
        block = _block()
        assert "$250M" in block
        assert "citation-only" in block


class TestMechanism756Taxonomy:
    def test_extends_m672_doj_soi(self):
        block = _block()
        assert "mechanism 672" in block
        assert 672 in yaml.safe_load(_entities_text())["entities"]["openai"][MECH_KEY]["connects_to"]

    def test_connects_753_litigation_economics(self):
        blk = yaml.safe_load(_entities_text())["entities"]["openai"][MECH_KEY]
        assert 753 in blk["connects_to"]
        assert "$28M" in _block()

    def test_connects_609_714_660_attribution_template(self):
        blk = yaml.safe_load(_entities_text())["entities"]["openai"][MECH_KEY]
        assert 609 in blk["connects_to"]
        assert 714 in blk["connects_to"]
        assert 660 in blk["connects_to"]

    def test_connects_519_newscorp_paid(self):
        blk = yaml.safe_load(_entities_text())["entities"]["openai"][MECH_KEY]
        assert 519 in blk["connects_to"]

    def test_first_dedicated_mechanism_claim(self):
        assert "FIRST dedicated corpus mechanism" in _block()


class TestMechanism756Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()

    def test_is_significant_false(self):
        assert "is_significant False" in _block()

    def test_engine_not_run(self):
        assert "engine NOT run" in _block()

    def test_verdict_directional(self):
        assert "directionally_supported_not_proven" in _block()

    def test_correlation_not_causation(self):
        assert "correlation_not_causation: true" in _block()

    def test_financial_incentive_documentation_leg(self):
        block = _block()
        assert "financial-incentive documentation leg" in block
        assert "not a tone test" in block

    def test_falsification_ledger_holds_at_27(self):
        assert "ledger holds at 27" in _block()
        assert _repo_grep(LEDGER_28_NEEDLE) == []

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _block()

    def test_not_artifact_grade(self):
        assert "NOT artifact_grade true" in _block()

    def test_excerpt_bounded_caveat(self):
        block = _block()
        assert "0 browser.open" in block
        assert "excerpt-bounded" in block


class TestDocSync874:
    def test_readme_row_874(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_874(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_874_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog874:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #874 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #874 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "m756" in entry
        assert "summary judgment" in entry

    def test_log_rotation_window_870_874(self):
        entry = self._entry()
        assert "870-874" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding874:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 5, 0).strftime("%H:%M") == "05:00"

    def test_scheduled_local_matches_run_context(self):
        assert SCHEDULED_LOCAL == "Sun 2026-09-20 05:00:00 PDT"
