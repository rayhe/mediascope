"""Type B #1063: James Pero (Gizmodo) Sep-25 Meta VR glasses hands-on enthusiasm
vs Sep-28 Meta smart-glasses PR Cleanup adversarial analysis - within-journalist
WITHIN-ENTITY register split (mechanism 869).

New arm (this mechanism, mechanism 869): Gizmodo "VR Headsets Are So Cooked",
byline James Pero (bounded attribution: author-page listing at
gizmodo.com/author/jpero carrying both pieces, plus a WeSearch record naming
James Pero, Sep 25 2026 18:45 UTC, with the canonical Gizmodo URL; bounded per
iteration-492), Sep 25 2026 - read first-hand this run via the verbatim
gizmodo.com canonical URL, full end-to-end read. Unreserved enthusiasm for the
Meta VR glasses demo ("the promise feels real", "good news for the future of
VR", Meta VR Glasses do things "better", "really sharp, really clear", "no
noticeable lag", "both hand and eye tracking were very snappy", "VR glasses
are the thing I want"); genuine hardware caveats noted (70-degree FOV versus
Quest 3's 110 degrees, possible light bleed, price); acknowledges Meta's VR
pullback and layoffs without souring the demo verdict. MANUAL ILLUSTRATIVE
+0.50.

Counter arm (this mechanism, also read first-hand this run, not carried):
Gizmodo "Meta's Smart Glasses PR Cleanup Campaign Is in Full Swing", byline
James Pero (bounded attribution: author-page listing; bounded per
iteration-492), Sep 28 2026 - read first-hand this run via the verbatim
gizmodo.com canonical URL, full end-to-end read. Adversarial PR-campaign
framing ("Meta is finally feeling the heat", the audio-only launch
"conspicuous", backlash "palpable"; camera-free glasses and Private Processing
read as privacy-remediation theater; celebrity ambassadors read as perception
management aimed at the pervert perception; Connect read as a persuasion
effort); credits the privacy measures as real, which bounds the negativity.
MANUAL ILLUSTRATIVE -0.30.

Illustrative delta (VR minus smart-glasses) +0.80: 0.50 - (-0.30). Three-day,
same-writer, same-outlet, same Meta Connect window. This is a TEMPORAL
REPLICATION of mechanism 818 (Sep-24 VR enthusiasm +0.40 vs Audio stigma
-0.20, illustrative +0.60) with fresh Sep-25/28 arms: the register follows
product category and news peg (hands-on demo vs privacy analysis), not a
uniform anti-Meta stance. Useful counterevidence against broad entity-level
bias claims. NOT a falsification-family member (m818 already tested and
falsified the uniform brand-directed prediction); ledger holds at 35. MANUAL
ILLUSTRATIVE; engine NOT run; no analysis.json; NOT artifact-grade; verdict
directionally_supported_not_proven; correlation not causation.

FOURTH leg of the 1060-1064 window: D (#1060) -> E (#1061) -> A (#1062) ->
B (#1063) -> C (#1064), rotation per #565. Concurrency: #899 (nytimes.yaml),
#938 (test file), #900 (untracked test file), #1012-wt (test file) in-flight
and untouched; targeted staging only.

Anchor-marked tests deselected pre-commit per #565; rotation/itlog/doc-sync
tests fail pre-doc-sync by design per #719; in-flight tests fail pre-staging
by design.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")

TYPE_LETTER = "B"
ITERATION = 1063
M_ID = 870
OWN_M_ID = 869  # own mechanism for this file's structure tests; M_ID tracks the corpus max
JOURNALIST_SLUG = "james_pero"
MECH_KEY = (
    "type_b_1063_james_pero_gizmodo_vr_headsets_cooked_enthusiasm_"
    "vs_pr_cleanup_adversarial_sep29"
)
MECH_ID_MARKER = "mechanism" + "_" + "86" + "9"  # own-form underscore sweep marker
MECH_ID_DASH = "mechanism" + "-" + "86" + "9"
MECH_ID_NUMERIC = "mechanism_id" + ": " + "86" + "9"
NEXT_US = "mechanism" + "_" + "87" + "1"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-" + "87" + "1"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id" + ": " + "87" + "1"  # next-number numeric sweep
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "0eb434c87be07e10bf42ee0baa84e704017eb04a"  # patched in the anchor followup commit
NOVELTY_CLAIMS = (
    "zero\ntest_type_b_1063 files, max numeric\nmechanism_id 868 pre-commit, "
    "block key zero-hit, two new\nURLs zero-hit"
)
EXPECTED_NEW_URLS = [
    "https://gizmodo.com/vr-headsets-are-so-cooked-2000817445",
    "https://gizmodo.com/meta-smart-glasses-public-perception-2000818140",
]
EXPECTED_ORDER = [("B", "1063"), ("A", "1062"), ("E", "1061"), ("D", "1060"), ("C", "1059")]
README_TESTS_BEFORE = 54505
README_FILES_BEFORE = 1387
README_TESTS_AFTER = 54553
README_FILES_AFTER = 1388
INFLIGHT_FILES = [
    "profiles/nytimes.yaml",  # #899 Type C, modified in worktree
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938, modified
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900, untracked
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt, modified
]
STAGED_EXPECTED_BASENAMES = {
    "journalists.yaml",
    OWN_BASENAME,
    "test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_credit_vs_meta_scrapped_tool_sep28_6pm.py",
    "test_type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_vs_sep16_meta_luna_inbrief_stigma_contrast_sep28_7pm.py",
    "test_type_c_1059_sb_energy_openai_55b_warrant_tenant_nvidia_105b_backstop_recycling_nineteenth_direction_sep28_8pm.py",
    "test_type_d_1060_m865_m866_m867_qualitative_corpus_integrity_sep28_9pm.py",
    "README.md",
    "ARCHITECTURE.md",
    "iteration-log.md",
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _load_journalists():
    import yaml

    return yaml.safe_load(_read(JOURNALISTS_YAML))


def get_block():
    data = _load_journalists()
    return data[JOURNALIST_SLUG]["competitor_coverage"][MECH_KEY]


def get_item():
    return _load_journalists()[JOURNALIST_SLUG]


def _repo_grep(needle):
    hits = []
    for root in ("profiles", "tests"):
        base = os.path.join(REPO, root)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] not in ("py", "yaml", "md", "json"):
                    continue
                p = os.path.join(dirpath, fn)
                if needle in open(p, errors="ignore").read():
                    hits.append(p)
    return hits


def _staged_paths():
    return _git(["diff", "--cached", "--name-only"]).stdout.splitlines()


# ---------------------------------------------------------------------------
# 1. Novelty anchor (anchor-marked tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1063:
    @pytest.mark.anchor
    def test_anchor_exists(self):
        assert ANCHORED_SHA not in (None, "PATCH_ME_IN_FOLLOWUP"), (
            "anchor NULL pre-commit (patched post-commit)"
        )

    @pytest.mark.anchor
    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_anchor_in_log_header(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1063 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1063 Type B")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_b_1063 files, max numeric\nmechanism_id 868 pre-commit, "
            "block key zero-hit, two new\nURLs zero-hit"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1060-1064 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1060_1064Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1060", "D"), ("1061", "E"), ("1062", "A")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fourth_leg_b(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1063 Type B") == 1
        rt = get_block()["rotation_transparency"]
        assert "1060-1064" in rt and "B #1063" in rt and "C #1064" in rt

    def test_predecessor_1062_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1062 Type A" in rt
        assert "7ff7f866" in rt and "0ff5eded" in rt and "8e3ed7fd" in rt

    def test_iteration_type_b(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism869Structure:
    def test_ids(self):
        b = get_block()
        assert b["mechanism_id"] == OWN_M_ID
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == "B"

    def test_block_key_design_note(self):
        b = get_block()
        assert b["block_key"] == MECH_KEY
        # Colon-form key carries no numeric mechanism id in any form.
        assert "869" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert MECH_ID_DASH not in MECH_KEY
        assert "m818" in b["design"] or "mechanism 818" in b["design"]

    def test_goal_job_author_fields(self):
        b = get_block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["author"] == "Kit (with Ray)"

    def test_test_file_reference(self):
        b = get_block()
        assert b["test_file"] == "tests/" + OWN_BASENAME

    def test_date_field(self):
        b = get_block()
        assert b["date"] == "2026-09-29 00:00 PDT"

    def test_rotation_transparency_present(self):
        rt = get_block()["rotation_transparency"]
        assert "1060-1064" in rt
        assert "#1060" in rt and "#1061" in rt and "#1062" in rt


# ---------------------------------------------------------------------------
# 4. Mechanism arms: two first-hand Sep-2026 reads
# ---------------------------------------------------------------------------
class TestMechanism869Arms:
    def test_vr_arm_source(self):
        arm = get_block()["new_vr_arm"]
        assert arm["title"] == "VR Headsets Are So Cooked"
        assert arm["url"] == EXPECTED_NEW_URLS[0]
        assert arm["date"] == "2026-09-25"
        assert arm["publication"] == "Gizmodo (Keleops AG)"
        assert "James Pero" in arm["byline"]
        assert "iteration-492" in arm["byline"]

    def test_vr_arm_first_hand(self):
        arm = get_block()["new_vr_arm"]
        assert arm["evidence_tier"].startswith("full-text first-hand this run")
        assert "1 browser.open" in arm["evidence_tier"]
        assert "hands-on demo" in arm["genre"]

    def test_vr_arm_quotes(self):
        quotes = get_block()["new_vr_arm"]["key_quotes"]
        assert len(quotes) == 7
        blob = "\n".join(quotes)
        assert "the promise feels real" in blob
        assert "good news for the future of VR" in blob
        assert "really sharp, really clear" in blob
        assert "no noticeable lag" in blob
        assert "very snappy" in blob
        assert "VR glasses are the thing I want" in blob

    def test_vr_arm_tone(self):
        arm = get_block()["new_vr_arm"]
        assert arm["tone_score"] == 0.50
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "70-degree" in arm["register_notes"]

    def test_sg_arm_source(self):
        arm = get_block()["smart_glasses_arm"]
        assert arm["title"] == "Meta's Smart Glasses PR Cleanup Campaign Is in Full Swing"
        assert arm["url"] == EXPECTED_NEW_URLS[1]
        assert arm["date"] == "2026-09-28"
        assert "James Pero" in arm["byline"]
        assert "read first-hand this run" in arm["mechanism_note"]

    def test_sg_arm_first_hand(self):
        arm = get_block()["smart_glasses_arm"]
        assert arm["evidence_tier"].startswith("full-text first-hand this run")
        assert "1 browser.open" in arm["evidence_tier"]
        assert "privacy/PR analysis" in arm["genre"]

    def test_sg_arm_tone(self):
        arm = get_block()["smart_glasses_arm"]
        assert arm["tone_score"] == -0.30
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        quotes = arm["key_quotes"]
        assert len(quotes) == 3
        assert "Meta is finally feeling the heat" in quotes


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer: illustrative delta math and statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism869Scorer:
    def test_tones(self):
        assert get_block()["new_vr_arm"]["tone_score"] == 0.50
        assert get_block()["smart_glasses_arm"]["tone_score"] == -0.30

    def test_delta_plus_0_80(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["illustrative_delta_vr_minus_smart_glasses"] == 0.80
        assert round(0.50 - (-0.30), 2) == s["illustrative_delta_vr_minus_smart_glasses"]

    def test_calc_string(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["delta_calc"] == "0.50 - (-0.30) = 0.80"
        assert "m818" in s["interpretation"]

    def test_statistical_discipline(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert get_block()["not_artifact_grade"] is True
        assert "not_proven" in get_block()["verdict"]

    def test_falsification_ledger_35(self):
        b = get_block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 35
        assert "ledger holds at 35" in b["falsification_note"]
        assert b["no_analysis_json_update"] is True

    def test_engine_not_run(self):
        sd = get_block()["statistical_discipline"]
        assert "engine NOT run" in sd
        assert "Aug 28 2026" in sd


# ---------------------------------------------------------------------------
# 6. Confounders, counterevidence, strongest counterargument
# ---------------------------------------------------------------------------
class TestMechanism869Confounders:
    def test_confounders_present(self):
        cfs = get_block()["confounders"]
        assert len(cfs) == 6
        assert cfs[0].startswith("[STRONG]")
        assert cfs[1].startswith("[STRONG]")
        assert cfs[2].startswith("[STRONG]")
        assert cfs[5].startswith("[WEAK]")
        blob = "\n".join(cfs)
        assert "n=1 per arm" in blob
        assert "Genre confound" in blob
        assert "Product-category confound" in blob

    def test_counterevidence_present(self):
        ce = get_block()["counterevidence"]
        assert len(ce) == 3
        blob = "\n".join(ce)
        assert "VR pullback" in blob
        assert "Private Processing" in blob
        assert "three days" in blob

    def test_strongest_counterargument(self):
        sca = get_block()["strongest_counterargument"]
        assert "genre-and-category-first" in sca
        assert "+0.80" in sca
        assert "not a controlled contrast" in sca

    def test_connects_to(self):
        assert get_block()["connects_to"] == [818, 806, 791, 746, 211, 269, 743]
        assert "TEMPORAL REPLICATION" in get_block()["extends"]


# ---------------------------------------------------------------------------
# 7. Research method: two first-hand opens, bounded byline, novelty greps
# ---------------------------------------------------------------------------
class TestResearchMethodTypeB1063:
    def test_opens_and_method(self):
        rm = get_block()["research_method"]
        assert "2 browser.open successes this run" in rm
        assert "0 browser.open failures" in rm
        assert "iteration-492" in rm

    def test_url_attestation(self):
        rm = get_block()["research_method"]
        assert "verbatim" in rm
        assert "no canonical URLs constructed" in rm

    def test_novelty_greps_documented(self):
        rm = get_block()["research_method"]
        assert "max numeric mechanism_id 868 pre-commit" in rm
        assert "block key zero-hit pre-commit" in rm
        assert "zero-hit repo-wide pre-commit" in rm


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_869(self):
        ids = []
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(f)):
                ids.append(int(m.group(1)))
        assert max(ids) == M_ID

    def test_zero_next_numeric_870_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_870_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_own_underscore_dash_needles_zero_in_sources(self):
        # Format-built per #715: no literal own-number key string is
        # carried anywhere; the needles must be pure zero repo-wide.
        assert _repo_grep(MECH_ID_MARKER) == []
        assert _repo_grep(MECH_ID_DASH) == []

    def test_block_key_in_journalists_yaml(self):
        assert MECH_KEY in _read(JOURNALISTS_YAML)


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        line = next(
            l for l in _read(README).splitlines() if l.startswith("| Tests |")
        )
        assert str(README_TESTS_AFTER) in line
        assert str(README_FILES_AFTER) in line

    def test_readme_row_1063(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type B #1063" in text
        assert "mechanism 869" in text

    def test_arch_row_1063(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type B #1063" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("B", "1063"), ("A", "1062"), ("E", "1061"), ("D", "1060"), ("C", "1059")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1063 Type B")
        end = log.index("## #1062 Type A")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1063 Type B") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 869" in section
        assert "James Pero" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1060-1064" in section
        assert "B #1063" in section


# ---------------------------------------------------------------------------
# 11. In-flight concurrency isolation (#899, #938, #900, #1012-wt)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # Fails pre-commit by design (nothing staged yet); green once the
        # run stages its own files. All four in-flight paths stay
        # uncommitted and unstaged.
        staged = _staged_paths()
        assert staged != [], "nothing staged yet (pre-commit)"
        for f in INFLIGHT_FILES:
            assert f not in staged, "in-flight file leaked into staging: %s" % f
        assert not any("test_type_b_938_" in l for l in staged)
        assert not any("test_type_d_900_" in l for l in staged)
        assert not any("test_type_a_1012_" in l for l in staged)

    def test_targeted_staging_only(self):
        # Fails pre-commit by design; green post-staging. The staged set
        # must be exactly this run's files - nothing more.
        staged = {os.path.basename(p) for p in _staged_paths()}
        assert staged == STAGED_EXPECTED_BASENAMES


# ---------------------------------------------------------------------------
# 12. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_only(self):
        data = _load_journalists()
        import json

        blob = json.dumps(data[JOURNALIST_SLUG], ensure_ascii=False)
        assert "\u2014" not in blob  # no em dashes, repo prose rule
        blob.encode("ascii")  # raises on any other non-ASCII

    def test_urls_verbatim(self):
        for url in EXPECTED_NEW_URLS:
            assert url.startswith("https://") and " " not in url

    def test_test_file_ascii(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")

    def test_source_references_recorded(self):
        # Per the standing "keep references" rule: both arms carry their
        # verbatim first-hand source URLs.
        assert get_block()["new_vr_arm"]["url"] == EXPECTED_NEW_URLS[0]
        assert get_block()["smart_glasses_arm"]["url"] == EXPECTED_NEW_URLS[1]
