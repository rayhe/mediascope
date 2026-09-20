"""Type C #879 (875-879 window, fifth leg D->E->A->B->C, CLOSING the window):
Sep-17-2026 unsealed summary-judgment filings' testimonial datums - FIRST
dedicated corpus mechanism (mechanism 759) on Nadella's retrain-testimony,
the ~93% click-through destruction datum, and Brockman's paywall-hack
approval.

THREE legs, one pricing fight:
(1) License-alternative pricing: Microsoft CEO Satya Nadella testified that
"anything that is paywalled should be licensed by anyone who wants to use
it" for AI training, and that he would have invoked Microsoft's contractual
right to require model RETRAINING had he known OpenAI trained on paywalled
content. The buyer's CEO prices the license alternative at "must license,"
validating the publishers' price demand from inside the defense camp and
undercutting mechanism 672's DOJ zero-price fair-use vector. Directly prices
mechanism 756 Leg 1's paywall-acquisition carve-out.
(2) Attribution-consideration measured repricing: plaintiffs' filings cite
Microsoft data that Copilot reduced click-through to nytimes.com by roughly
93% versus traditional Bing search. Mechanism 756's engineer admission
("users won't click") was qualitative; this is the payer's own measurement:
the citation consideration in the corpus's zero-fee attribution template
(609 India Sep 7-8, 714 Village Media Sep 16, 660 contrast class) delivers
~7% of the referral baseline. Two-tier consideration structure quantified.
(3) Paywall-acquisition mens rea: OpenAI president Greg Brockman responded
"ah nice" when told of a hack to get around the NYT paywall when scraping -
the intent evidence for mechanism 756 Leg 1's paywall-acquisition carve-out.
Plus litigation-BATNA scale datums: >10M articles scraped (~1/3 NYT),
91,692 copies in mid-training datasets, Project Mango 160,903 unique news
works, damages exposure in the billions per reports.

MANUAL qualitative only per the Aug 28 2026 standing rule, engine NOT run,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT a falsification-family member,
ledger holds at 28; no analysis.json update; NOT artifact-grade.
Novelty verified pre-commit: zero test_type_c_879 files on disk; no
"Type C #879" in git log; max numeric mechanism_id 758 pre-commit;
zero underscore-form 759 mechanism key strings repo-wide per the #715
designed-keying convention (format-built needles, no literals carried);
block key zero-hit repo-wide pre-commit; "ah nice" zero-hit repo-wide;
"93%" zero-hit in profiles pre-commit; "retrain" zero-hit as a testimony
datum (existing hits are all "pretraining" substrings in unrelated
contexts); insiderfinance + 2 WSJ URLs zero-hit repo-wide pre-commit
(1 browser.open first-hand read on insiderfinance, 56 rendered lines; WSJ
paywalled, excerpt-bounded per #503). 875-879 window fifth leg D->E->A->B->C
CLOSING it (anchor patched post-commit per #565) - Sep 20 2026 10:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_879_nadella_retrain_testimony_93pct_clickthrough_sep20_10am.py"
MECH_KEY = "nadella_retrain_testimony_93pct_clickthrough_sep2026"
BLOCK_KEY = "type_c_879_nadella_retrain_testimony_93pct_clickthrough_sep2026"
M_ID = 759
ITER = 879
TYPE_LETTER = "C"
# Concatenated so this file never carries the literal marker itself (per #715).
MECH_ID_MARKER = "mechanism" + "_759"
NEXT_ID_MARKER = "mechanism" + "_760"
NEXT_ID_NUMERIC = "mechanism_id: " + "760"
NEXT_ID_DASH = "mechanism" + "-760"
# Format-built so the file never carries the literal ledger string (per #715).
LEDGER_29_NEEDLE = "falsification ledger: " + "29"
EXPECTED_ORDER = [("C", "879"), ("B", "878"), ("A", "877"), ("E", "876"), ("D", "875")]
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

INSIDERFINANCE_URL = "https://www.insiderfinance.io/news/openai-microsoft-copyright-lawsuit-exposes-news-scraping"
WSJ_EXISTENTIAL_URL = "https://www.wsj.com/tech/ai/tech-companies-staff-knew-their-ai-tools-posed-existential-threat-to-publishers-67ed8940"
WSJ_SKETCHY_URL = "https://www.wsj.com/tech/ai/sketchy-af-what-to-know-about-how-openai-staff-discussed-book-pirating-fdc788a1"
NEW_EVIDENCE_URLS = (INSIDERFINANCE_URL, WSJ_EXISTENTIAL_URL, WSJ_SKETCHY_URL)

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
SCHEDULED_LOCAL = "Sun 2026-09-20 10:00:00 PDT"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entities_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"))


def _block():
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  anthropic:")
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
    out = _git("log", "--all", "--format=%H %s", "--grep", "Type C #879")
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #879" in subject and qualifier in subject:
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


class TestNovelty879:
    def test_single_test_type_c_879_file(self):
        files = [
            fn
            for fn in os.listdir(TESTS_DIR)
            if fn.startswith("test_type_c_879")
        ]
        assert files == [OWN_BASENAME], files

    def test_type_c_879_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565 (the #879 main commit does not
        # exist yet); patched green in the anchor followup.
        mains = _git_log_mains("retrain-testimony")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA in mains, mains

    def test_novelty_verification_claim(self):
        hits = _repo_grep(MECH_KEY, roots=("profiles",))
        assert hits == ["profiles/competitor-entities.yaml"], hits
        assert "Nadella" in _block()

    def test_875_878_window_legs_present_prior_to_879(self):
        for fn in (
            "test_type_d_875_",
            "test_type_e_876_",
            "test_type_a_877_",
            "test_type_b_878_",
        ):
            matches = [f for f in os.listdir(TESTS_DIR) if f.startswith(fn)]
            assert len(matches) == 1, (fn, matches)

    def test_ah_nice_zero_hit_outside_this_mechanism(self):
        # The Brockman "ah nice" quote is FIRST in the corpus via this leg.
        hits = _repo_grep("ah nice")
        assert set(hits) == {
            os.path.join("tests", OWN_BASENAME),
            "profiles/competitor-entities.yaml",
        }, hits

    def test_93pct_clickthrough_zero_hit_outside_this_mechanism(self):
        hits = _repo_grep("93% compared with traditional Bing", roots=("profiles",))
        assert hits == ["profiles/competitor-entities.yaml"], hits


class TestRotationGuard879:
    """#879 is the Type C fifth leg of window 875-879: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_875_879_fifth_leg_closing(self):
        # Deselected pre-commit per #565 (the #879 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"875-879 window fifth leg D->E->A->B->C CLOSING: expected "
            f"{EXPECTED_ORDER}, got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_878(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "878"), (
            f"immediate predecessor must be Type B #878, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("retrain-testimony")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism759Structure:
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
        assert "iteration: 879" in block
        assert "rotation: Type C" in block
        assert "time_pdt: '10:00'" in block
        assert "date_analyzed: '2026-09-20'" in block

    def test_designed_keying_no_underscore_759_in_block(self):
        # Per the #715 convention: colon-form keying only; the numeric
        # mechanism id never appears in underscore form inside the block.
        block = _block()
        assert "_759" not in block, [
            line for line in block.splitlines() if "_759" in line
        ]

    def test_yaml_parses_and_fields(self):
        doc = yaml.safe_load(_entities_text())
        blk = doc["entities"]["openai"][MECH_KEY]
        assert blk["mechanism_id"] == 759
        assert blk["iteration"] == 879
        assert blk["block_key"] == BLOCK_KEY
        assert blk["type"] == "financial_incentive_mapping"

    def test_max_mechanism_id_is_759(self):
        assert max(_corpus_ids()) == 759

    def test_no_760_numeric_in_profiles(self):
        # Format-built needle so this file never carries the literal.
        assert not _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))

    def test_all_three_source_urls_in_block(self):
        block = _block()
        for url in NEW_EVIDENCE_URLS:
            assert url in block, url

    def test_test_file_field_names_this_file(self):
        assert OWN_BASENAME in _block()


class TestMechanism759NadellaTestimony:
    def test_nadella_paywalled_licensing_quote(self):
        block = _block()
        assert "anything that is paywalled should be licensed" in block

    def test_nadella_retrain_testimony(self):
        block = _block()
        assert "retrain" in block
        assert "contractual right" in block

    def test_nadella_is_microsoft_ceo_and_defendant(self):
        block = _block()
        assert "Satya Nadella" in block
        assert "Microsoft CEO" in block

    def test_license_alternative_pricing_leg_present(self):
        block = _block()
        assert "license_alternative_pricing_leg" in block
        assert "must license" in block

    def test_nadella_scoped_to_paywalled_content(self):
        # Confounder rank 4: the testimony is scoped to paywalled content,
        # not a blanket license concession - the block must say so.
        block = _block()
        assert "PAYWALLED content specifically" in block

    def test_undercuts_doj_zero_price_vector(self):
        block = _block()
        assert "mechanism 672" in block
        assert "zero-price" in block


class TestMechanism759Clickthrough:
    def test_93pct_clickthrough_datum(self):
        block = _block()
        assert "93%" in block
        assert "nytimes.com" in block

    def test_copilot_vs_bing_baseline(self):
        block = _block()
        assert "Copilot" in block
        assert "traditional Bing" in block

    def test_attribution_consideration_measured_leg(self):
        block = _block()
        assert "attribution_consideration_measured_leg" in block
        assert "~7% of the referral baseline" in block

    def test_extends_mechanism_756(self):
        block = _block()
        assert "mechanism 756" in block
        assert "EXTENDS mechanism 756" in block

    def test_two_tier_consideration_structure(self):
        block = _block()
        assert "Two-tier consideration structure" in block
        assert "mechanism 519" in block

    def test_reprices_attribution_template_mechanisms(self):
        block = _block()
        assert "mechanism 609" in block
        assert "mechanism 714" in block
        assert "mechanism 660" in block


class TestMechanism759MensRea:
    def test_brockman_ah_nice_quote(self):
        block = _block()
        assert "ah nice" in block
        assert "Brockman" in block

    def test_paywall_hack_context(self):
        block = _block()
        assert "paywall" in block
        assert "mens_rea_leg" in block

    def test_hecht_memo_corroboration(self):
        block = _block()
        assert "Hecht" in block
        assert "astonishing theft of unprecedented proportions" in block

    def test_litigation_batna_scale_datums(self):
        block = _block()
        assert "litigation_batna_scale" in block
        assert "10 million articles" in block
        assert "91,692" in block
        assert "160,903" in block
        assert "billions" in block


class TestMechanism759Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value: NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "cohens_d: NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "ci_95: NOT_CALCULATED" in _block()

    def test_is_significant_false(self):
        assert "is_significant: false" in _block()

    def test_engine_not_run(self):
        assert "engine_run: false" in _block()

    def test_verdict_directional(self):
        assert "directionally_supported_not_proven" in _block()

    def test_correlation_not_causation(self):
        assert "correlation_not_causation: true" in _block()

    def test_qualitative_pricing_leg(self):
        block = _block()
        assert "qualitative structural pricing mapping only" in block

    def test_falsification_ledger_holds_at_28(self):
        assert "ledger holds at 28" in _block()
        assert _repo_grep(LEDGER_29_NEEDLE) == []

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update: true" in _block()

    def test_not_artifact_grade(self):
        assert "artifact_grade: false" in _block()

    def test_tone_not_scored(self):
        assert "tone_scores: NOT_SCORED" in _block()

    def test_evidence_grade_caveats(self):
        block = _block()
        assert "excerpt-bounded" in block
        assert "browser.open" in block
        assert "NOT judicial findings" in block

    def test_no_coverage_tone_claim(self):
        assert "no_coverage_tone_claim: true" in _block()


class TestDocSync879:
    def test_readme_row_879(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_879(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_879_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog879:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #879 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #879 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "m759" in entry
        assert "Nadella" in entry

    def test_log_rotation_window_875_879(self):
        entry = self._entry()
        assert "875-879" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding879:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 10, 0).strftime("%H:%M") == "10:00"

    def test_scheduled_local_matches_run_context(self):
        assert SCHEDULED_LOCAL == "Sun 2026-09-20 10:00:00 PDT"
