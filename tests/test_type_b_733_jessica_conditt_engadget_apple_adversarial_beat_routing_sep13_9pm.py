"""
Type B iteration #733: Jessica Conditt (Engadget) adversarial always-listening
register on Apple Audio Intelligence - journalist-level refinement of mechanism
#150's beat-assignment routing claim (mechanism 674).

Apple arm (NEW): "Apple Watch's New Audio Intelligence Enables A Real-Life
Conversation Rewind" (Engadget, event-day Wed Sep 9 2026; "By Jessica Conditt"
byline confirmed via Engadget's own homepage listings in bounded searches)
applies an adversarial always-listening register to Apple: "Apple Watch, as it
turns out, is a fabulous piece of spy equipment. This is by Apple's own
admission and it's at the heart of the company's new Audio Intelligence feature
for Apple Watch Series 12"; homepage dek "Apple says its taking privacy concerns
seriously with its new spyware feature for Watch Series 12" (one listing
variant; the article page reads "transcription feature"). MANUAL ILLUSTRATIVE
register -0.55.

Meta arm: bounded absence - zero written Meta wearables coverage by Conditt
surfaced in bounded searches (iteration-492, not a proven zero); her only
Meta-adjacent corpus presence is the Sep 26 2024 Engadget Podcast (PS5 Pro /
Meta Connect 2024 episode) where she handled the PlayStation segment while
Karissa Bell handled Meta Connect 2024, Orion, and Ray-Ban Meta.

REFINEMENT of mechanism #150: #150 claimed Engadget's privacy-vocabulary asymmetry
"operates through editorial beat assignment (Karissa Bell's Meta-only privacy
investigations), not individual journalist bias." The Conditt arm complicates
that clause: the adversarial always-listening register IS reporter-portable to
Apple inside the same newsroom (Conditt adversarial on Apple, as adversarial as
Bell on Meta), while Low's zero-alarm register is reporter-portable across Meta,
Snap, and Apple (per #723 / mechanism 668). Registers are reporter-stable and
entity-portable; the Meta-vs-Apple outlet asymmetry is a composition effect of
WHO covers WHICH entity (Bell assigned Meta investigations, Conditt assigned
Apple news, Low assigned hands-on), not entity animus per se.

Statistical discipline (Aug 28 2026 standing contract): MANUAL ILLUSTRATIVE;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine NOT run;
NOT artifact-grade; no engine divergence pin. Verdict:
directionally_supported_not_proven. NOT a falsification-family member (ledger
holds at 24). Correlation is not causation.

Rotation: Type B (A/B/C/D/E cycle). Window 729-733 closes C (#729) -> D (#730)
-> E (#731) -> A (#732) -> B (#733); novelty anchor patched in the followup per
the #565 convention (two-commit: main, then anchor SHA patch). Search
excerpt-bounded per #503 (browser.open terminal per turn); no analysis.json
update warranted (journalist mechanism only). Sep 13 2026 21:00 PDT - 42 tests,
10 classes.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = os.path.basename(__file__)

MECHANISM_KEY = "jessica_conditt_engadget_apple_adversarial_beat_routing_refinement"
APPLE_URL = "https://Www.engadget.com/2254194/apple-watch-new-audio-intelligence-enables-a-real-life-conversation-rewind/"
PODCAST_URL = "https://www.engadget.com/gaming/playstation/engadget-podcast-ps5-pro-hands-on-and-metas-wild-orion-ar-glasses-133029580.html?src=rss&rand=43"
COOPER_URL = "https://Www.engadget.com/2254031/apple-watch-series-12-will-listen-to-your-conversations/"
REGISTER_URL = "https://www.theregister.com/security/2026/09/10/watch-out-apple-timepiece-can-grab-snippets-of-conversation-without-both-speakers-consent/5295666"
HEADLINE = "Apple Watch's New Audio Intelligence Enables A Real-Life Conversation Rewind"
BYLINE = "By Jessica Conditt"
BODY_QUOTE = "Apple Watch, as it turns out, is a fabulous piece of spy equipment"
CAREERS_KEY = "jessica_conditt"

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


class TestNovelty733:
    def test_single_test_file_for_733(self):
        matches = [f for f in os.listdir(TESTS_DIR) if re.search(r"_733_", f)]
        assert matches == [THIS_FILE], f"expected only this file for #733, got {matches}"

    def test_mechanism_674_unique_in_profiles(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn)).read()
                count += len(re.findall(r"(?m)^\s*mechanism_id:\s*674\s*$", text))
        assert count == 1, f"expected exactly one mechanism_id: 674 in profiles/, got {count}"

    def test_main_commit_unique_or_absent(self):
        out = subprocess.run(
            ["git", "log", "--oneline"], capture_output=True, text=True, cwd=REPO
        ).stdout
        hits = [line for line in out.splitlines() if "Type B #733" in line]
        assert len(hits) <= 1, f"duplicate Type B #733 main commits: {hits}"


class TestMechanism733Content:
    def test_block_present(self):
        block = load_block()
        assert block is not None

    def test_pair_and_journalist(self):
        block = load_block()
        assert block["finding_type"] == "journalist_cross_entity"
        assert block["journalist"] == "Jessica Conditt"
        assert block["rotation_type"] == "B"
        assert block["iteration"] == 733
        assert block["mechanism_id"] == 674
        assert block["competitor"] == "Apple"
        assert block["publication"] == "Engadget (Yahoo/Apollo)"

    def test_apple_url_verbatim(self):
        block = load_block()
        assert APPLE_URL in block["source_urls"]

    def test_podcast_url_verbatim(self):
        block = load_block()
        assert PODCAST_URL in block["source_urls"]

    def test_headline_and_byline_in_finding(self):
        block = load_block()
        assert HEADLINE in block["finding"]
        assert BYLINE in block["finding"]

    def test_spy_equipment_quote_in_finding(self):
        block = load_block()
        assert BODY_QUOTE in block["finding"]

    def test_dek_variant_in_finding(self):
        block = load_block()
        assert "spyware feature" in block["finding"]
        assert "transcription feature" in block["finding"]

    def test_test_file_field_matches(self):
        block = load_block()
        assert block["test_file"] == "tests/" + THIS_FILE
        assert block["test_count"] == 42


class TestStatisticalDiscipline733:
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


class TestRefinement733:
    def test_connects_to_includes_150(self):
        assert 150 in load_block()["connects_to"]

    def test_connects_to_chain(self):
        connects = load_block()["connects_to"]
        for mid in (113, 150, 151, 668, 670, 671):
            assert mid in connects, f"mechanism {mid} missing from connects_to"

    def test_refinement_language(self):
        finding = load_block()["finding"]
        assert "REFINEMENT of #150" in finding
        assert "composition effect" in finding
        assert "reporter-portable" in finding

    def test_verdict(self):
        assert load_block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family(self):
        finding = load_block()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "ledger holds at 24" in finding

    def test_career_entry_present(self):
        careers = load_careers()
        assert CAREERS_KEY in careers
        assert careers[CAREERS_KEY]["current_publication"] == "Engadget"


class TestConfounders733:
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
        finding = load_block()["finding"]
        assert "iteration-492" in finding
        assert "not a proven zero" in finding


class TestIterationLog733:
    def _head(self):
        with open(LOG_PATH) as f:
            return "\n".join(f.read().splitlines()[:25])

    def test_log_entry_present(self):
        assert "#733" in self._head()

    def test_log_mechanism_674(self):
        assert "mechanism 674" in self._head()

    def test_log_journalist(self):
        assert "Jessica Conditt" in self._head()

    def test_log_rotation_window(self):
        assert "729-733" in self._head()


class TestRotationCycleGuard733:
    ANCHORED_SHA = "2c4e7dc1b83a612984c4bd4e0fad0f2eb9a2c60d"  # main-commit SHA, patched post-commit per #565

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
        for n in range(710, 734):
            assert n in files and len(files[n]) == 1, f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_closes_to_b(self):
        files = self._rotation_files()
        assert files[729][0][0] == "c"
        assert files[730][0][0] == "d"
        assert files[731][0][0] == "e"
        assert files[732][0][0] == "a"
        assert files[733][0][0] == "b"
        assert files[733][0][1] == THIS_FILE

    def test_anchor_sha_pinned_post_commit(self):
        actual = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
        ).stdout.strip()
        assert self.ANCHORED_SHA != "ANCHORED_SHA", "anchor not yet patched post-commit"
        assert actual == self.ANCHORED_SHA, f"HEAD {actual} != anchored {self.ANCHORED_SHA}"


class TestDocSync733:
    def test_readme_row(self):
        with open(os.path.join(REPO, "README.md")) as f:
            assert THIS_FILE in f.read()

    def test_architecture_row(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as f:
            assert THIS_FILE in f.read()


class TestSweepSupersession733:
    def test_max_mechanism_674(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn)).read()
                ids.extend(int(x) for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text))
        assert max(ids) == 674

    def test_zero_mechanism_675_keys(self):
        carriers = {
            "test_type_a_732_verge_openai_doj_soi_coverage_selection_sep13_8pm.py",
            THIS_FILE,
        }
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn)).read()
                    assert "mechanism_675_" not in text, f"mechanism_675_ key in {fn}"
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if "mechanism_675_" in open(fp).read():
                hits.append(fn)
        assert hits == [], f"mechanism_675_ keys outside sweep carriers: {hits}"

    def test_732_forward_sweep_designed_supersession(self):
        sweep_path = os.path.join(
            TESTS_DIR, "test_type_a_732_verge_openai_doj_soi_coverage_selection_sep13_8pm.py"
        )
        assert os.path.exists(sweep_path)
        assert "mechanism_674" in open(sweep_path).read()
        block = load_block()
        assert block["mechanism_id"] == 674

    def test_ledger_holds(self):
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn)).read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding733:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_9_2026_is_wednesday(self):
        assert self._weekday("2026-09-09") == "Wednesday"

    def test_sep_10_2026_is_thursday(self):
        assert self._weekday("2026-09-10") == "Thursday"

    def test_sep_13_2026_is_sunday(self):
        assert self._weekday("2026-09-13") == "Sunday"
