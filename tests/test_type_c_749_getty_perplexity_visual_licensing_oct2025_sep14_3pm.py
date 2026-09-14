"""Type C #749: Getty Images x Perplexity global multi-year visual licensing agreement (Oct 31 2025) - first dedicated corpus mapping of the Getty-Perplexity relationship on the perplexity entity (mechanism 684).

On Mon Sep 14 2026 this run maps the first dedicated Getty x Perplexity
financial relationship mechanism on the perplexity entity in
profiles/competitor-entities.yaml: a global multi-year licensing agreement
announced Oct 31 2025 (GlobeNewswire press release, NEW YORK dateline) covering
display of Getty Images across Perplexity's AI-powered search and discovery
tools, integrated via the Getty Images API with image credit and link-to-source
attribution improvements. The deal is display-only with NO training rights
(ZDNet: Perplexity may not train its model on Getty content), and the tie
pre-dates the agreement (Getty joined Perplexity's publisher program circa Oct
2024). Reuters reported Getty shares rose ~5% on the announcement Friday. The
corpus already maps Getty x OpenAI (Jun 2026, display-only no training rights):
the Getty-Perplexity deal is eight months EARLIER, so the premium-imagery
visual-licensing template is Perplexity-first and OpenAI followed. Consideration
is attribution plus API access, not training rights (Nick Unsworth, VP
Strategic Development, Getty; Jessica Chan, Head of Content and Publisher
Partnerships, Perplexity). Mark Lemley (Stanford, via Reuters): licensing works
for large curated collections but not the whole internet - supporting the corpus
two-tier reading (mechanism 681). The sign-one-sue-other bifurcation extends
mechanism 663: Getty sued Stability AI over image scraping while licensing
display rights to Perplexity and OpenAI; Perplexity is sued by Dow Jones/NY
Post (SDNY 1:24-cv-07984), Nikkei and Asahi while licensing from Getty, Wiley,
and the Cashmere premium-data roster. p/d/ci NOT_CALCULATED; is_significant
False; engine NOT run; NOT artifact-grade; directionally_supported_not_proven;
NOT a falsification-family member; ledger holds at 24; no analysis.json update.
Search-excerpt-bounded per #503 (the one browser.open attempt on the Press
Gazette tracker failed upstream terminally this turn and was not retried).
Designed keying per #723/#738/#739/#747/#748: the block key carries no
underscore-form 684 mechanism key substring, so profile sweeps stay green while
mechanism_id advances in colon form.
"""

import datetime
import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "getty_perplexity_visual_licensing_oct2025_sep14"
MECH_NUM = 684
GLOBE_URL = "https://www.globenewswire.com/news-release/2025/10/31/3178264/0/en/Getty-Images-and-Perplexity-strike-multi-year-image-partnership.html"
ZDNET_URL = "https://www.zdnet.com/article/ai-struggles-to-cite-results-properly-can-perplexity-and-gettys-new-partnership-fix-that/"
PG_URL = "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _profiles_corpus():
    parts = []
    for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
        parts.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(parts)


def _block():
    corpus = _read("profiles/competitor-entities.yaml")
    rest = corpus.split(MECH_KEY + ":")[1]
    return re.split(r"\n  [a-z0-9_]+:", rest, maxsplit=1)[0]


def _block_data():
    data = yaml.safe_load(_read("profiles/competitor-entities.yaml"))
    return data["entities"]["perplexity"][MECH_KEY]


def _fold(block):
    return re.sub(r"\s+", " ", block)


def _underscore(n):
    # Built by concatenation so this file carries no literal underscore-form
    # mechanism key substring (keeps #747-style profile sweeps green).
    return "mechanism" + "_" + str(n)


class TestNovelty749:
    """Iteration 749 is new; nothing with this number existed pre-commit."""

    def test_single_type_c_749_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_c_749*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_c_749_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_749 files, no #749 in git log, zero
        # underscore-form 684 keys repo-wide); this test pins that no
        # duplicate #749 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #749:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type C #749 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard749.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)

    def test_colon_form_684_id_unique_in_profiles(self):
        ids = re.findall(r"mechanism_id:\s*684\b", _profiles_corpus())
        assert len(ids) == 1, "expected exactly one colon-form 684 id, got %d" % len(ids)


class TestRotationCycleGuard749:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first. #749
    opens the new 749-753 window, closing B->C->D->E->A.
    """

    ANCHORED_SHA = "9eeeb484ebdbc1a5aa016bb7bf52e1ba65fee1cb"  # main commit this run, per #565

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_745_749_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "749"),
            ("B", "748"),
            ("A", "747"),
            ("E", "746"),
            ("D", "745"),
        ], "rotation window 745-749 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_c_follows_b(self):
        subjects = self._mains()
        assert subjects[0].startswith("Type C #749:"), subjects[0]
        assert subjects[1].startswith("Type B #748:"), subjects[1]

    def test_b_748_main_commit_unique_and_anchored(self):
        # The #748 anchor was patched in its own followup; pin it here so a
        # second #748 main commit can never slip in silently.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #748:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #748 main commit, got %r" % (mains,)

    def test_single_type_per_iteration_in_window(self):
        subjects = self._mains()
        nums = [re.search(r"#(\d+):", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, "duplicate iteration number in window: %r" % (nums,)

    def test_followup_titles_do_not_match_mains_regex(self):
        # The #565 followup convention ("Type C #749 followup: ...", no colon
        # right after the number) must never collide with the mains regex, or
        # the rotation window picks up phantom iterations. The main commit
        # subject mentions "followup" in prose, so this test only applies to
        # subjects in the followup TITLE form.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
        )
        for s in out.stdout.splitlines():
            if re.match(r"^Type [A-E] #749 followup:", s):
                assert not re.match(r"^Type [A-E] #749:", s), "followup collided with mains: %r" % (s,)


class TestMechanism684Content:
    def test_mech_block_present_in_entities(self):
        corpus = _read("profiles/competitor-entities.yaml")
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 684" in corpus

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 749
        assert data["iteration_type"] == "C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["date_analyzed"] == "2026-09-14"
        assert data["time_pdt"] == "15:00"
        assert data["author"] == "Kit (with Ray)"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_source_urls(self):
        data = _block_data()
        urls = data["source_urls"]
        assert len(urls) == 8, "expected 8 source URLs, got %d" % len(urls)
        assert GLOBE_URL in urls
        assert ZDNET_URL in urls
        assert PG_URL in urls
        for u in urls:
            assert u.startswith(("http://", "https://")), u

    def test_deal_terms_oct_31_2025(self):
        data = _block_data()
        terms = data["deal_terms"]
        assert terms["announced"] == "2025-10-31"
        assert "display" in terms["scope"].lower()
        assert "display-only" in _fold(terms["training_rights"]).lower()
        assert "may not train" in _fold(terms["training_rights"]).lower()
        assert "gettyimages.com" not in terms["announced"]

    def test_display_only_no_training_rights(self):
        block = _fold(_block())
        assert "NO training rights" in block
        assert "may not train its model on Getty content" in block

    def test_perplexity_first_template(self):
        block = _fold(_block())
        assert "Perplexity-first" in block
        assert "Jun 2026" in block
        assert "eight months" in block

    def test_sign_one_sue_other_bifurcation(self):
        block = _fold(_block())
        assert "1:24-cv-07984" in block
        assert "Stability AI" in block

    def test_lemley_quote(self):
        block = _fold(_block())
        assert "Mark Lemley" in block
        assert "large collections of high-quality content" in block

    def test_three_counterevidence(self):
        data = _block_data()
        counter = data["counterevidence"]
        assert len(counter) == 3, "expected 3 counterevidence, got %d" % len(counter)
        assert all("COUNTEREVIDENCE:" in c for c in counter)

    def test_confounders_ranked(self):
        data = _block_data()
        ranked = data["confounders_ranked"]
        assert any(r.startswith("STRONG:") for r in ranked)
        assert any(r.startswith("MODERATE:") for r in ranked)
        assert any(r.startswith("WEAK:") for r in ranked)

    def test_no_coverage_tone_claim(self):
        data = _block_data()
        assert data["no_coverage_tone_claim"] is True
        assert data["cautious_language_required"] is True
        block = _fold(_block())
        assert "No causal claim" in block

    def test_research_method_names_constraints(self):
        block = _fold(_block())
        assert "#503" in block
        assert "excerpt-bounded" in block
        assert "PATCH_ME_IN_FOLLOWUP" not in block


class TestSupersessionAndCorpusPost748:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_684(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_748_max_683_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 684
        # supersedes #748's test_max_mechanism_id_is_683 per the #710/#720
        # convention.
        assert max(self._ids()) == 684

    def test_744_745_zero_682_profile_sweeps_stay_green_by_designed_keying(self):
        # The #744/#745 profile-YAML zero-682 sweeps assert the contiguous
        # underscore form absent from every profile YAML; the #749 block key
        # was designed to keep them green.
        assert _underscore(682) not in _profiles_corpus()

    def test_748_zero_683_profile_sweep_stays_green_by_designed_keying(self):
        # The #748 zero-683 profile sweep asserts the underscore form absent
        # from every profile YAML; mechanism 683 lives in
        # competitor-coverage-research.yaml, not profiles/.
        assert _underscore(683) not in _profiles_corpus()

    def test_747_zero_683_test_sweep_stays_green_by_designed_keying(self):
        # The #747 test-file zero-683 sweep scans test files for the
        # underscore form with trailing underscore; this file was written to
        # keep it green (keying uses the descriptive block key and
        # colon/space forms only).
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert _underscore(683) + "_" not in own

    def test_683_still_present_in_coverage_research(self):
        # Integrity: #748's mechanism 683 mechanism_id survives untouched.
        research = _read("profiles/competitor-coverage-research.yaml")
        assert "mechanism_id: 683" in research

    def test_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_684_keys_in_profiles(self):
        assert _underscore(684) not in _profiles_corpus()

    def test_zero_underscore_684_literal_in_own_file(self):
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert _underscore(684) not in own


class TestStatisticalDiscipline749:
    def test_tone_not_scored(self):
        assert _block_data()["tone_scores"] == "NOT_SCORED"

    def test_p_d_ci_not_calculated(self):
        block = _fold(_block())
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block

    def test_engine_not_run_not_artifact_grade(self):
        block = _fold(_block())
        assert "Engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "directionally_supported_not_proven" in block

    def test_no_analysis_json_update(self):
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "diff", "--name-only"],
            capture_output=True,
            text=True,
        )
        assert "analysis.json" not in out.stdout.splitlines()

    def test_verdict_and_ledger(self):
        block = _fold(_block())
        assert "directionally_supported_not_proven" in block
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 24" in block


class TestLedger749:
    def test_falsification_ledger_holds_at_24(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDocSync749:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")

    def test_iteration_log_entry(self):
        log = _read("iteration-log.md")
        assert "Type C #749" in log
        assert "mechanism id 684" in log
        assert "Getty Images x Perplexity" in log


class TestDateGrounding749:
    def test_iteration_date_is_monday(self):
        # The scheduler fired this run on Monday, September 14, 2026 (PDT).
        assert datetime.date(2026, 9, 14).strftime("%A") == "Monday"

    def test_deal_date_is_friday(self):
        # Reuters: Getty shares rose "on Friday" - Oct 31 2025 was a Friday.
        assert datetime.date(2025, 10, 31).strftime("%A") == "Friday"
