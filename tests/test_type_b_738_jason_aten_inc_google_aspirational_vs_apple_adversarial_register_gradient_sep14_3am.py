"""
Type B iteration #738: Jason Aten (Inc.) cross-entity register gradient -
Google-aspirational vs Apple-adversarial (mechanism 677).

Google arm (in-corpus since Aug 16 2026, mechanism 137 context): "At I/O, Google
Just Shipped Apple's AI Promises" (Inc., Thu May 21 2026) - corpus-coded framing
"aspirational, Google as deliverer of Apple promises, positive competitive".

Apple arm (NEW): "For Years, People Have Worried Their Devices Were Listening.
Apple Just Made It a Feature" (Inc., Fri Sep 11 2026; byline via
inc.com/jason-aten/ URL slug; Search-excerpt-bounded per developer constraint)
applies an adversarial always-listening register: "most people just hear yada,
yada, yada, you are recording me"; "I am not sure any of us are ready for a
world where listening devices become ubiquitous and are normalized - even if
they provide real utility"; "I am not sure Apple has counted the cost associated
with a feature that requires this much explanation to reassure people's privacy
concerns." MANUAL ILLUSTRATIVE Apple-arm register -0.55.

JOURNALIST-LEVEL INSTANTIATION of mechanism 137: the Aug 16 outlet-level finding
documented Mansueto Ventures' Google financial dependency (55% advertising
revenue, Google programmatic/search traffic dependency, zero Meta deals)
correlating with softer Google coverage; Aten's own Google-aspirational column
is the journalist-level case of that outlet pattern, now paired with his
Apple-adversarial column. EXTENSION of mechanism 671 (#728, Kit Eaton): Eaton
gave Inc. its Meta-positive/Apple-adversarial inversion; Aten adds a
Google-aspirational/Apple-adversarial gradient at the same outlet - two Inc.
columnists, both Apple-adversarial on Audio Intelligence (Eaton has since
published a second Apple piece, the Sep 10 workplace-ban column: three
adversarial-leaning Inc. columns total), each soft on a different non-Apple
entity. The common Inc. thread is Apple-adversariality, consistent with the
naive payer-softening prediction (no AI-lab licensing deals at Inc. in corpus;
no payer, no softening) - illustrative only, NOT a financial proof.

Statistical discipline (Aug 28 2026 standing contract): MANUAL ILLUSTRATIVE;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine NOT run;
NOT artifact-grade; no engine divergence pin. Verdict:
directionally_supported_not_proven. NOT a falsification-family member (ledger
holds at 24). Correlation is not causation.

Rotation: Type B (A/B/C/D/E cycle). Window 734-738 closes C (#734) -> D (#735)
-> E (#736) -> A (#737) -> B (#738); novelty anchor patched in the followup per
the #565 convention (two-commit: main, then anchor SHA patch). Search
excerpt-bounded on the Apple arm per #503 (browser.open terminal per turn); no
analysis.json update warranted (journalist mechanism only). Sep 14 2026 03:00
PDT - 42 tests, 10 classes.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = os.path.basename(__file__)

MECHANISM_KEY = "jason_aten_inc_google_aspirational_vs_apple_adversarial_register_gradient"
APPLE_URL = "https://www.inc.com/jason-aten/for-years-people-have-worried-their-devices-were-listening-apple-just-made-it-a-feature/91404202"
GOOGLE_URL = "http://www.inc.com/jason-aten/at-i-o-google-just-shipped-apples-ai-promises/91191832"
EATON_META_URL = "https://www.inc.com/kit-eaton/meta-bets-on-augmented-reality-devices-as-future-of-wearable-tech.html"
EATON_APPLE_URL = "https://www.inc.com/kit-eaton/the-apple-watch-got-a-massive-ai-upgrade-and-the-controversy-could-get-it-banned-at-the-office/91403791"
TC_URL = "https://techcrunch.com/2026/09/09/apple-watchs-new-ai-features-are-normalizing-the-idea-that-technology-is-always-listening/"
HEADLINE = "For Years, People Have Worried Their Devices Were Listening. Apple Just Made It a Feature"
GOOGLE_HEADLINE = "At I/O, Google Just Shipped Apple's AI Promises"
URL_SLUG = "inc.com/jason-aten/"
CAREERS_KEY = "jason_aten"
FILE_737 = "test_type_a_737_ft_anthropic_slowdown_week_profitability_scoop_sep14_2am.py"

YAML_PATH = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
CAREERS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")


def load_block():
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)
    return data["cross_publication_findings"][MECHANISM_KEY]


def load_careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


class TestNovelty738:
    def test_single_test_file_for_738(self):
        matches = [f for f in os.listdir(TESTS_DIR) if re.search(r"_738_", f)]
        assert matches == [THIS_FILE], f"expected only this file for #738, got {matches}"

    def test_mechanism_677_unique_in_profiles(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn)).read()
                count += len(re.findall(r"(?m)^\s*mechanism_id:\s*677\s*$", text))
        assert count == 1, f"expected exactly one mechanism_id: 677 in profiles/, got {count}"

    def test_main_commit_unique_or_absent(self):
        out = subprocess.run(
            ["git", "log", "--oneline"], capture_output=True, text=True, cwd=REPO
        ).stdout
        hits = [line for line in out.splitlines() if "Type B #738" in line]
        assert len(hits) <= 1, f"duplicate Type B #738 main commits: {hits}"


class TestMechanism738Content:
    def test_block_present(self):
        block = load_block()
        assert block is not None

    def test_pair_and_journalist(self):
        block = load_block()
        assert block["finding_type"] == "journalist_cross_entity"
        assert block["journalist"] == "Jason Aten"
        assert block["rotation_type"] == "B"
        assert block["iteration"] == 738
        assert block["mechanism_id"] == 677
        assert block["competitor"] == "Google/Apple"
        assert block["publication"] == "Inc. (Mansueto Ventures)"

    def test_apple_url_verbatim(self):
        block = load_block()
        assert APPLE_URL in block["source_urls"]

    def test_google_url_verbatim(self):
        block = load_block()
        assert GOOGLE_URL in block["source_urls"]

    def test_eaton_urls_carried(self):
        block = load_block()
        assert EATON_META_URL in block["source_urls"]
        assert EATON_APPLE_URL in block["source_urls"]

    def test_techcrunch_url_verbatim(self):
        block = load_block()
        assert TC_URL in block["source_urls"]

    def test_headline_and_byline_in_finding(self):
        block = load_block()
        assert HEADLINE in block["finding"]
        assert GOOGLE_HEADLINE in block["finding"]
        assert URL_SLUG in block["finding"]

    def test_apple_body_quotes_in_finding(self):
        block = load_block()
        assert "you are recording me" in block["finding"]
        assert "ubiquitous and are normalized" in block["finding"]
        assert "counted the cost" in block["finding"]

    def test_test_file_field_matches(self):
        block = load_block()
        assert block["test_file"] == "tests/" + THIS_FILE
        assert block["test_count"] == 42


class TestStatisticalDiscipline738:
    def test_manual_illustrative(self):
        assert "MANUAL ILLUSTRATIVE" in load_block()["finding"]

    def test_not_calculated_triple(self):
        finding = load_block()["finding"]
        assert "p_value NOT_CALCULATED" in finding
        assert "cohens_d NOT_CALCULATED" in finding
        assert "ci_95 NOT_CALCULATED" in finding

    def test_is_significant_false(self):
        assert "is_significant False" in load_block()["finding"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in load_block()["finding"]

    def test_search_excerpt_bounded(self):
        block = load_block()
        prose = block["finding"] + " ".join(block["confounders"])
        assert "Search-excerpt-bounded" in prose


class TestRefinement738:
    def test_connects_to_includes_137(self):
        assert 137 in load_block()["connects_to"]

    def test_connects_to_chain(self):
        connects = load_block()["connects_to"]
        for mid in (137, 150, 668, 670, 671, 674):
            assert mid in connects, f"mechanism {mid} missing from connects_to"

    def test_instantiation_language(self):
        finding = load_block()["finding"]
        assert "INSTANTIATION" in finding
        assert "mechanism 137" in finding

    def test_verdict(self):
        assert load_block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family(self):
        finding = load_block()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "ledger holds at 24" in finding

    def test_career_entry_present(self):
        careers = load_careers()
        assert CAREERS_KEY in careers
        assert careers[CAREERS_KEY]["current_publication"] == "Inc."
        assert "mechanism 677" in careers[CAREERS_KEY]["notes"]


class TestConfounders738:
    def test_confounder_strength_layers(self):
        confounders = load_block()["confounders"]
        assert len(confounders) == 9
        assert sum(1 for c in confounders if c.startswith("STRONG:")) == 3
        assert sum(1 for c in confounders if c.startswith("MODERATE:")) == 3
        assert sum(1 for c in confounders if c.startswith("WEAK:")) == 3

    def test_three_counterevidence(self):
        counter = load_block()["counterevidence"]
        assert len(counter) == 3
        assert all(c.startswith("COUNTEREVIDENCE:") for c in counter)

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in load_block()["finding"]

    def test_bounded_absence_language(self):
        block = load_block()
        prose = block["finding"] + " ".join(block["confounders"])
        assert "iteration-492" in prose
        assert "not a proven zero" in prose


class TestIterationLog738:
    def _tail(self):
        with open(LOG_PATH) as f:
            return "\n".join(f.read().splitlines()[-40:])

    def test_log_entry_present(self):
        assert "#738" in self._tail()

    def test_log_mechanism_677(self):
        assert "mechanism 677" in self._tail()

    def test_log_journalist(self):
        assert "Jason Aten" in self._tail()

    def test_log_rotation_window(self):
        assert "734-738" in self._tail()


class TestRotationCycleGuard738:
    ANCHORED_SHA = "42d3bb6f10ccdb5f9dbc4d8468fc49d1eb39f9c2"  # main-commit SHA, patched post-commit per #565

    @staticmethod
    def _rotation_files():
        result = {}
        for fn in os.listdir(TESTS_DIR):
            m = re.match(r"test_type_([a-e])_(\d+)_", fn)
            if m:
                result.setdefault(int(m.group(2)), []).append((m.group(1), fn))
        return result

    def test_24_rotation_files_contiguous(self):
        files = self._rotation_files()
        for n in range(715, 739):
            assert n in files and len(files[n]) == 1, f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_closes_to_b(self):
        files = self._rotation_files()
        assert files[734][0][0] == "c"
        assert files[735][0][0] == "d"
        assert files[736][0][0] == "e"
        assert files[737][0][0] == "a"
        assert files[738][0][0] == "b"
        assert files[738][0][1] == THIS_FILE

    def test_anchor_sha_pinned_post_commit(self):
        actual = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
        ).stdout.strip()
        assert self.ANCHORED_SHA != "ANCHORED_SHA", "anchor not yet patched post-commit"
        assert actual == self.ANCHORED_SHA, f"HEAD {actual} != anchored {self.ANCHORED_SHA}"


class TestDocSync738:
    def test_readme_row(self):
        with open(os.path.join(REPO, "README.md")) as f:
            assert THIS_FILE in f.read()

    def test_architecture_row(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as f:
            assert THIS_FILE in f.read()


class TestSweepSupersession738:
    def test_max_mechanism_677(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn)).read()
                ids.extend(int(x) for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text))
        assert max(ids) == 677

    def test_zero_mechanism_678_keys(self):
        carriers = {
            FILE_737,
            THIS_FILE,
        }
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn)).read()
                    assert "mechanism_678_" not in text, f"mechanism_678_ key in {fn}"
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if "mechanism_678_" in open(fp).read():
                hits.append(fn)
        assert hits == [], f"mechanism_678_ keys outside sweep carriers: {hits}"

    def test_737_forward_sweep_designed_supersession(self):
        sweep_path = os.path.join(TESTS_DIR, FILE_737)
        assert os.path.exists(sweep_path)
        assert "mechanism_677" in open(sweep_path).read()
        block = load_block()
        assert block["mechanism_id"] == 677

    def test_ledger_holds(self):
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn)).read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding738:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_11_2026_is_friday(self):
        assert self._weekday("2026-09-11") == "Friday"

    def test_may_21_2026_is_thursday(self):
        assert self._weekday("2026-05-21") == "Thursday"

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"
