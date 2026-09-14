"""
Type B iteration #743: Hamish Hector (TechRadar) cross-entity register gradient -
Snap-aspirational vs Meta-alarm (mechanism 680).

Snap arm (NEW, Jun 17 2026; byline verified via third-party reprint quoting "By
Hamish Hector, June 17, 2026"; Search-excerpt-bounded per developer constraint):
"Snap's AR glasses cost $2,195 - and despite the high price, I think they could
be the best XR gadget of 2026 if they live up to their prototype" - "They're
incredible, truly sci-fi, and cost $2,195 (Around 1,640)"; "nothing quite like
the Snap Specs on the market right now, and that's a major advantage for Snap
as it leapfrogs Meta, Android XR, and the rest." Zero surveillance/privacy
vocabulary in the surfaced excerpt despite strictly MORE sensor hardware than
Meta's single 12MP camera (dual Snapdragon, hand tracking, environment meshing,
spatial anchoring). MANUAL ILLUSTRATIVE Snap-arm register +0.55.

Meta arm (in-corpus since mechanism 115): "The Ray-Ban Meta smart glasses are
majorly popular, which is exciting and frightening in equal measure" -
corpus-coded alarm_hedged, privacy vocabulary
frightening/worrying/creepy/concerned/scary/"wearable recording devices", every
positive paired with an alarm counterpart, Google Glass assault stories invoked.

Price inversion: the $2,195 device gets the aspirational register, the $379
device gets the alarm register - price does not explain the differential.
Apple arm (corpus context): Hector's Vision Pro column calls it "the most
sophisticated, powerful, and coolest hardware Apple ever built" despite $3,499 -
admiring, no alarm.

JOURNALIST-LEVEL INSTANTIATION of mechanism 115: the outlet-level finding
documented Future plc's Google traffic dependency correlating with softer
non-Meta coverage; Hector's own Snap-aspirational column is the journalist-level
case of that outlet pattern, now paired against his Meta-alarm column.
EXTENSION of the #728/#738 columnist strand: Kit Eaton and Jason Aten gave Inc.
its Meta-positive/Apple-adversarial inversion; Hector adds a TechRadar
Meta-alarm/Snap-aspirational gradient - two outlets where same-journalist
cross-entity pairs diverge on camera wearables. Cross-outlet contrast with
mechanism 354 (WIRED Chokkattu price-hostile on the same $2,195 Snap device):
same hardware, same price, opposite registers across outlets.

Statistical discipline (Aug 28 2026 standing contract): MANUAL ILLUSTRATIVE;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine NOT run;
NOT artifact-grade; no engine divergence pin. Verdict:
directionally_supported_not_proven. NOT a falsification-family member (ledger
holds at 24). Correlation is not causation.

Rotation: Type B (A/B/C/D/E cycle). Window 739-743 closes C (#739) -> D (#740)
-> E (#741) -> A (#742) -> B (#743); novelty anchor patched in the followup per
the #565 convention (two-commit: main, then anchor SHA patch). Search
excerpt-bounded on the Snap arm per #503 (browser.open terminal per turn); no
analysis.json update warranted (journalist mechanism only). Sep 14 2026 08:00
PDT - 47 tests, 10 classes.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = os.path.basename(__file__)

MECH_KEY = "hamish_hector_techradar_snap_sci_fi_vs_meta_alarm_register_gradient"
SNAP_URL = "https://www.techradar.com/computing/virtual-reality-augmented-reality/snaps-ar-glasses-cost-usd2-195-and-despite-the-high-price-i-think-they-could-be-the-best-xr-gadget-of-2026-if-they-live-up-to-their-prototype"
ISPR_URL = "https://ispr.info/2026/06/18/snap-specs-ar-glasses-use-new-combo-of-xr-tech-to-evoke-impressive-presence/"
META_URL = "https://www.techradar.com/computing/virtual-reality-augmented-reality/the-ray-ban-meta-smart-glasses-are-majorly-popular-which-is-exciting-and-frightening-in-equal-measure"
APPLE_URL = "https://www.techradar.com/computing/virtual-reality-augmented-reality/i-dont-know-if-vision-pro-is-alive-or-dead-but-it-is-still-the-most-sophisticated-powerful-and-coolest-hardware-apple-ever-built-and-we-can-surely-thank-it-for-the-glasses-that-will-follow"
SNAP_HEADLINE = "Snap's AR glasses cost $2,195"
META_HEADLINE = "The Ray-Ban Meta smart glasses are majorly popular, which is exciting and frightening in equal measure"
CAREERS_KEY = "hamish_hector"
FILE_742 = "test_type_a_742_wsj_openai_altman_slowdown_relay_sep14_7am.py"

YAML_PATH = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
CAREERS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")


def load_block():
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)
    return data["cross_publication_findings"][MECH_KEY]


def load_careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


class TestNovelty743:
    def test_single_test_file_for_743(self):
        matches = [f for f in os.listdir(TESTS_DIR) if re.search(r"_743_", f)]
        assert matches == [THIS_FILE], f"expected only this file for #743, got {matches}"

    def test_mechanism_680_unique_in_research_yaml(self):
        count = len(
            re.findall(r"(?m)^\s*mechanism_id:\s*680\s*$", open(YAML_PATH).read())
        )
        assert count == 1, f"expected exactly one mechanism_id: 680 in research YAML, got {count}"

    def test_main_commit_unique_or_absent(self):
        out = subprocess.run(
            ["git", "log", "--oneline"], capture_output=True, text=True, cwd=REPO
        ).stdout
        hits = [line for line in out.splitlines() if "Type B #743" in line]
        assert len(hits) <= 1, f"duplicate Type B #743 main commits: {hits}"


class TestMechanism743Content:
    def test_block_present(self):
        block = load_block()
        assert block is not None

    def test_pair_and_journalist(self):
        block = load_block()
        assert block["finding_type"] == "journalist_cross_entity"
        assert block["journalist"] == "Hamish Hector"
        assert block["rotation_type"] == "B"
        assert block["iteration"] == 743
        assert block["mechanism_id"] == 680
        assert block["competitor"] == "Snap/Meta"
        assert block["publication"] == "TechRadar (Future plc)"

    def test_snap_url_verbatim(self):
        block = load_block()
        assert SNAP_URL in block["source_urls"]

    def test_byline_verification_url_verbatim(self):
        block = load_block()
        assert ISPR_URL in block["source_urls"]

    def test_meta_url_verbatim(self):
        block = load_block()
        assert META_URL in block["source_urls"]

    def test_apple_url_verbatim(self):
        block = load_block()
        assert APPLE_URL in block["source_urls"]

    def test_headlines_in_finding(self):
        block = load_block()
        assert SNAP_HEADLINE in block["finding"]
        assert META_HEADLINE in block["finding"]

    def test_snap_body_quotes_in_finding(self):
        block = load_block()
        assert "truly sci-fi" in block["finding"]
        assert "leapfrogs" in block["finding"]
        assert "best XR gadget of 2026" in block["finding"]

    def test_meta_alarm_vocabulary_in_finding(self):
        block = load_block()
        assert "alarm_hedged" in block["finding"]
        assert "frightening" in block["finding"]

    def test_sensor_hardware_contrast_in_finding(self):
        block = load_block()
        assert "dual Snapdragon" in block["finding"]
        assert "12MP camera" in block["finding"]

    def test_test_file_field_matches(self):
        block = load_block()
        assert block["test_file"] == "tests/" + THIS_FILE
        assert block["test_count"] == 47

    def test_discovery_date(self):
        assert load_block()["discovery_date"] == "2026-09-14"


class TestStatisticalDiscipline743:
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


class TestRefinement743:
    def test_connects_to_includes_115(self):
        assert 115 in load_block()["connects_to"]

    def test_connects_to_chain(self):
        connects = load_block()["connects_to"]
        for mid in (115, 150, 354, 362, 395, 671, 677):
            assert mid in connects, f"mechanism {mid} missing from connects_to"

    def test_instantiation_language(self):
        finding = load_block()["finding"]
        assert "INSTANTIATION" in finding
        assert "mechanism 115" in finding

    def test_verdict(self):
        assert load_block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family(self):
        finding = load_block()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "ledger holds at 24" in finding

    def test_career_entry_present(self):
        careers = load_careers()
        assert CAREERS_KEY in careers
        assert careers[CAREERS_KEY]["current_publication"] == "TechRadar"
        assert "mechanism 680" in careers[CAREERS_KEY]["notes"]
        assert 680 in careers[CAREERS_KEY]["mechanism_ids"]
        assert careers[CAREERS_KEY]["smart_glasses_coverage"]["snap_specs_2026"]["mechanism_id"] == 680


class TestConfounders743:
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


class TestIterationLog743:
    def _tail(self):
        with open(LOG_PATH) as f:
            return "\n".join(f.read().splitlines()[-40:])

    def test_log_entry_present(self):
        assert "#743" in self._tail()

    def test_log_mechanism_680(self):
        assert "mechanism 680" in self._tail()

    def test_log_journalist(self):
        assert "Hamish Hector" in self._tail()

    def test_log_rotation_window(self):
        assert "739-743" in self._tail()


class TestRotationCycleGuard743:
    ANCHORED_SHA = "ANCHORED_SHA"  # main-commit SHA, patched post-commit per #565

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
        for n in range(720, 744):
            assert n in files and len(files[n]) == 1, f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_closes_to_b(self):
        files = self._rotation_files()
        assert files[739][0][0] == "c"
        assert files[740][0][0] == "d"
        assert files[741][0][0] == "e"
        assert files[742][0][0] == "a"
        assert files[743][0][0] == "b"
        assert files[743][0][1] == THIS_FILE

    def test_anchor_sha_pinned_post_commit(self):
        actual = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
        ).stdout.strip()
        assert self.ANCHORED_SHA != "ANCHORED_SHA", "anchor not yet patched post-commit"
        assert actual == self.ANCHORED_SHA, f"HEAD {actual} != anchored {self.ANCHORED_SHA}"


class TestDocSync743:
    def test_readme_row(self):
        with open(os.path.join(REPO, "README.md")) as f:
            assert THIS_FILE in f.read()

    def test_architecture_row(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as f:
            assert THIS_FILE in f.read()


class TestSweepSupersession743:
    def test_max_mechanism_680(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn)).read()
                ids.extend(int(x) for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text))
        assert max(ids) == 680

    def test_zero_mechanism_681_keys(self):
        carriers = {
            FILE_742,
            THIS_FILE,
        }
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn)).read()
                    assert "mechanism" + "_681_" not in text, f"mechanism_681_ key in {fn}"
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if "mechanism" + "_681_" in open(fp).read():
                hits.append(fn)
        assert hits == [], f"mechanism_681_ keys outside sweep carriers: {hits}"

    def test_742_max_679_sweep_fails_by_designed_supersession(self):
        # This run advances the numeric mechanism frontier to 680, so #742's
        # test_max_mechanism_id_is_679 fails by designed supersession (#710/#720
        # convention). Documented, not repaired.
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    ids.extend(
                        int(x)
                        for x in re.findall(
                            r"(?m)^\s*mechanism_id:\s*(\d+)\s*$",
                            open(os.path.join(root, fn)).read(),
                        )
                    )
        assert max(ids) == 680

    def test_742_zero_680_profile_sweep_stays_green_by_designed_keying(self):
        # #742's test_zero_underscore_680_keys asserts no underscore-form
        # mechanism_680 string in profiles/. This run's block and careers notes
        # use only descriptive keying / numeric mechanism_id fields, so that
        # sweep stays green.
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn)).read()
        assert "mechanism" + "_680" not in corpus

    def test_zero_680_profile_sweep_path_exists(self):
        sweep_path = os.path.join(TESTS_DIR, FILE_742)
        assert os.path.exists(sweep_path)
        block = load_block()
        assert block["mechanism_id"] == 680

    def test_ledger_holds(self):
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn)).read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding743:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_jun_17_2026_is_wednesday(self):
        assert self._weekday("2026-06-17") == "Wednesday"

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"
