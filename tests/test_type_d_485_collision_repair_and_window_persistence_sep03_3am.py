"""
Type D #485 - Mechanism-number collision repair verification + 480-484 window persistence
Sep 3 2026 03:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation C->D

Mechanism #485 defines no data mechanism; it repairs and verifies. The 02:00 PDT
Sep 3 run committed a Type B Brian X. Chen finding as mechanism #458, colliding
with the existing #458 (Type C Fox Corp DARK PUBLIC, Sep 2 2026 00:00 PDT,
committed first and referenced by #459's persistence guard). Two mechanisms
sharing one number breaks the repo's unique-sequential-numbering invariant, so
this iteration renumbers the Chen mechanism to #484 (chronological successor of
#483), rewrites its iteration-log entry in the standard newest-first format at
file top (replacing the non-standard bottom-appended "## Iteration 458" entry),
and extends the persistence regression guard to the 480-484 window.

Workstreams:
(1) collision repair verification - Fox #458 intact and sole owner of 458
    across the YAML stores; Chen mechanism fully moved to 484 (top-level anchor,
    key_journalists entry, test filename, log entry); old 458 test filename gone;
(2) window persistence - test files, iteration-log headings, and YAML anchors
    for #480 (podcast), #481 (Atlantic), #482 (NYT Weise), #483 (Schibsted),
    #484 (NYT Chen) all present; newest-first log ordering 485 > 484 > 483;
(3) README sync - table rows for the #483, #484 (renamed), and #485 test files.

Statistical discipline: this iteration asserts metadata and repair integrity
only; no tone scores, no p_value, no significance claimed.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 485 Type D 2026-09-03 03:00 PDT
"""

import re
from pathlib import Path

import yaml

REPO = Path(".")
LOG = REPO / "iteration-log.md"
NYT = REPO / "profiles" / "nytimes.yaml"
COMP = REPO / "profiles" / "competitor-entities.yaml"
ATL = REPO / "profiles" / "atlantic.yaml"
POD = REPO / "podcast-sentiment.md"
README = REPO / "README.md"

CHEN_484_FILE = "test_type_b_484_brian_x_chen_meta_vs_apple_privacy_vocabulary_bifurcation_sep03.py"
CHEN_458_FILE = "test_type_b_458_brian_x_chen_meta_vs_apple_privacy_vocabulary_bifurcation_sep03.py"
CHEN_484_KEY = "brian_x_chen_meta_vs_apple_privacy_vocabulary_bifurcation_484"

EM_DASH = chr(92) + "u2014"


def _nyt():
    return yaml.safe_load(NYT.read_text())


def _comp_text():
    return COMP.read_text()


class TestIteration485IDs:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 485" in doc
        assert "2026-09-03" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name.startswith("test_type_d_485_")


class TestCollisionRepair:
    def test_fox_458_intact_in_competitor_entities(self):
        text = _comp_text()
        assert text.count("mechanism_id: 458") == 1
        idx = text.index("mechanism_id: 458")
        assert "Fox Corporation" in text[max(0, idx - 3000):idx]

    def test_no_458_in_nytimes_yaml(self):
        text = NYT.read_text()
        assert "mechanism_id: 458" not in text
        assert "bifurcation_458" not in text
        assert "test_type_b_458_brian_x_chen" not in text

    def test_chen_484_anchor(self):
        d = _nyt()
        assert CHEN_484_KEY in d
        m = d[CHEN_484_KEY]
        assert m["mechanism_id"] == 484
        assert m["iteration"] == 484
        assert m["iteration_type"] == "B"

    def test_chen_484_journalist_entry(self):
        d = _nyt()
        entry = next(j for j in d["key_journalists"] if j.get("name") == "Brian X. Chen")
        assert entry["cross_entity_coverage_analysis"]["mechanism_id"] == 484

    def test_chen_484_id_count_in_nyt_yaml(self):
        assert NYT.read_text().count("mechanism_id: 484") == 2

    def test_old_test_filename_gone(self):
        assert not (REPO / "tests" / CHEN_458_FILE).exists()

    def test_new_test_filename_present(self):
        assert (REPO / "tests" / CHEN_484_FILE).exists()

    def test_no_duplicate_458_across_stores(self):
        total = _comp_text().count("mechanism_id: 458") + NYT.read_text().count("mechanism_id: 458")
        assert total == 1

    def test_log_has_no_bottom_appended_458_entry(self):
        assert "## Iteration 458 - Thu 2026-09-03" not in LOG.read_text()

    def test_log_has_484_heading(self):
        assert any(l.startswith("#484 Type B") for l in LOG.read_text().split("\n"))

    def test_log_newest_first_ordering(self):
        text = LOG.read_text()
        i485 = re.search(r"^#485 Type D", text, re.M).start()
        i484 = re.search(r"^#484 Type B", text, re.M).start()
        i483 = re.search(r"^#483 Type C", text, re.M).start()
        assert i485 < i484 < i483


class TestWindowPersistence480to484:
    def test_window_test_files_exist(self):
        expected = [
            "test_type_e_480_podcast_sentiment_sifted_sixth_vertical_sep02_10pm.py",
            "test_type_a_481_atlantic_openai_watchdog_entity_selection_asymmetry_sep02_11pm.py",
            "test_type_b_482_karen_weise_amazon_microsoft_headline_verb_asymmetry_sep03.py",
            "test_type_c_483_schibsted_openai_realtime_deal_sep03_1am.py",
            CHEN_484_FILE,
        ]
        for f in expected:
            assert (REPO / "tests" / f).exists(), f"missing {f}"

    def test_window_log_headings_present(self):
        text = LOG.read_text()
        for h in ["#480 Type E", "#481 Type A", "#482 Type B", "#483 Type C", "#484 Type B"]:
            assert h in text, f"missing log heading {h}"

    def test_480_podcast_anchor(self):
        assert "## Iteration #480" in POD.read_text()

    def test_481_atlantic_anchor(self):
        d = yaml.safe_load(ATL.read_text())
        m = d["competitor_relationships"]["openai"]["mechanism_481_atlantic_openai_watchdog_entity_selection_asymmetry"]
        assert m["iteration"] == 481

    def test_482_nyt_anchor(self):
        d = _nyt()
        entry = next(j for j in d["key_journalists"] if j.get("name") == "Karen Weise")
        cca = entry["cross_entity_coverage_analysis"]
        mechs = [v for k, v in cca.items() if "482" in k]
        assert len(mechs) == 1
        assert mechs[0]["mechanism_id"] == 482
        assert mechs[0]["iteration"] == 482

    def test_483_competitor_entities_anchor(self):
        text = _comp_text()
        assert "mechanism_483_schibsted_openai_realtime_content_deal" in text

    def test_window_yamls_parse(self):
        for p in [NYT, COMP, ATL]:
            yaml.safe_load(p.read_text())


class TestREADMESync:
    def test_483_row_present(self):
        assert "test_type_c_483_schibsted_openai_realtime_deal_sep03_1am.py" in README.read_text()

    def test_484_renamed_row_present(self):
        text = README.read_text()
        assert CHEN_484_FILE in text
        assert CHEN_458_FILE not in text

    def test_485_row_present(self):
        assert Path(__file__).name in README.read_text()

    def test_header_counts_format(self):
        assert re.search(r"\|\s*Tests\s*\|\s*\d+\s*\|", README.read_text())


class TestHygiene485:
    def test_no_em_dash_escape_form(self):
        src = Path(__file__).read_text()
        assert EM_DASH not in src

    def test_no_em_dash_byte(self):
        assert chr(0x2015) not in Path(__file__).read_text()

    def test_no_causal_claim(self):
        banned = ["proves that", "caused by", "demonstrates editorial", "confirms bias"]
        for i, line in enumerate(Path(__file__).read_text().split("\n"), 1):
            low = line.lower()
            if "assert" in low or "banned" in low:
                continue
            assert not any(b in low for b in banned), f"line {i}: {line[:80]}"

    def test_log_mentions_485(self):
        assert "#485" in LOG.read_text()

    def test_chen_sources_https_only(self):
        d = _nyt()
        for s in d[CHEN_484_KEY]["sources"]:
            assert s.startswith("https://"), s
