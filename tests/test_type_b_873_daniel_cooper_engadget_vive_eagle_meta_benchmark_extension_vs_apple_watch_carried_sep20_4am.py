"""
Type B #873 (rotation window 870-874, FOURTH leg: D->E->A->B): Daniel Cooper
(Engadget senior editor) - HTC Vive Eagle Sep-15-2026 review extends mechanism
295's within-review Meta privacy-benchmarking to a THIRD review unit, with a
carried same-week Apple Watch Series 12 comparator arm.

MECHANISM #755: within-journalist, within-review entity-framing temporal
extension plus same-week cross-entity comparator. NEW Meta-framing arm:
Cooper's "HTC Vive Eagle review: Pricey smart glasses that fail to impress"
(Engadget, Sep 15 2026, 7.4/10) - "the inherent issues (privacy and otherwise)
of any Meta product", self-declared "AI camera glasses skeptic", "hard to
rationalize the premium on moral grounds"; HTC earns a privacy Pro ("Welcome
focus on user privacy"). CARRIED Apple arm per #807 (not re-scored this run):
Cooper's own "Apple Watch Series 12 will listen to your conversations" (circa
Sep 10 2026) - less adversarial register per the Sep-13 Conditt block
(mechanism 150 refinement): alarm headline but full safeguards relay (opt-in,
secure enclave, no audio storage, deleted immediately) plus "less dystopian"
accessibility hedge. Illustrative tones: Meta -0.30 (new arm, hand-scored),
Apple -0.10 (carried); illustrative delta (Apple minus Meta) +0.20 -
within-journalist, within-week entity asymmetry: Meta gets the adversarial
register, Apple the softer one. Verdict directionally_supported_not_proven.

NOVELTY VERIFICATION (run pre-commit, Sep 20 2026 ~04:15 PDT, before any edits):
- glob: zero test_type_b_873*.py files on disk
- git log --all --grep="Type B #873": zero hits (no prior #873 main commit)
- numeric mechanism_id max in profiles/: 754 (755 is this run's own addition)
- format-built underscore needles: zero underscore-form 755 key strings repo-wide
  (__pycache__ artifacts excluded per the #715 pattern-rescope lesson)
- zero numeric "mechanism_id: 755" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- "daniel_cooper" top-level slug zero-hit pre-commit (m295 lives in
  profiles/competitor-coverage-research.yaml, not journalists.yaml)
- New Meta-framing arm URL zero-hit repo-wide pre-commit; Muck Rack URL
  zero-hit; carried Apple arm IN CORPUS (profiles/wired.yaml + Sep-13 Conditt
  block) - carried per #807, not a new arm
- REJECTED candidates this run: Alex Heath (Type B #563 in corpus), Scott
  Stein (#588, #868), Victoria Song (#618, #813), Lauren Goode / Julian
  Chokkattu / Boone Ashworth / Karissa Bell / Devindra Hardawar (Type B
  analyses in corpus), Alex Cranz / David Pierce / Tom Warren / Adi Robertson /
  Wes Davis (no clean Sep-2026 bylined arms), Mariella Moon (Luna arm good, no
  Moon competitor arm)

ROTATION: this is the FOURTH leg of rotation window 870-874 (D->E->A->B).
Prior legs present in iteration-log.md: #870 Type D, #871 Type E, #872 Type A
(03:00 PDT). Expected cycle position: B (873) after A (872) after E (871)
after D (870) after C (869).

RESEARCH METHOD: 7 browser.search query sets this run (Heath; Cranz/Pierce;
Warren/Robertson/Davis; theverge.com Luna attribution; Mariella Moon; Cooper
Vive Eagle byline - SELECTED; Cooper Apple Watch URL - carried-arm
verification). 0 browser.open per #503 (developer constraint: open declared
terminal; search-excerpt bounded evidence only). All URLs copied verbatim from
Full-URL listings. No URL construction. No zero-coverage claims per #492.

DESIGN NOTES:
- Cooper's Meta tone is expressed INSIDE a competitor's scored review
  (m295's own design); arm independence limited by construction (STRONG
  confounder, disclosed).
- The Apple arm is carried un-rescored per #807 (STRONG confounder, disclosed).
- p_value / cohens_d / ci_95 are NOT_CALCULATED (deliberate): a mechanical
  significance test on hand-scored items would manufacture precision that
  does not exist. is_significant is false. engine NOT run (illustrative arms
  only; Apple arm carried). correlation_not_causation is true.
- NOT a falsification-family member (temporal extension of an existing
  mechanism, not a uniform-prediction test); falsification ledger holds at 27.
- no analysis.json update (NOT artifact-grade).
- ASCII prose only (no em dashes), per repository conventions.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
OWN_BASENAME = "test_type_b_873_daniel_cooper_engadget_vive_eagle_meta_benchmark_extension_vs_apple_watch_carried_sep20_4am.py"
BLOCK_KEY = "type_b_873_daniel_cooper_engadget_vive_eagle_meta_benchmark_extension_vs_apple_watch_carried"
JOURNALIST = "Daniel Cooper"
ITERATION = 873
ITER_TYPE = "B"
MECH_ID = 755
ANCHORED_SHA = "b0b804f6aafb961db7a1f02e2a5bf1702407b128"  # patched post-commit per #565
# NEXT_ID / MECH_ID needles are format-built so the file never carries a
# literal underscore-form key string (per the #715 lesson).
MECH_ID_MARKER = "mechanism" + "_755"
NEXT_ID_MARKER = "mechanism" + "_756"
NEXT_ID_NUMERIC = "mechanism_id: " + "756"
NEXT_ID_DASH = "mechanism" + "-756"
NEW_ARM_URL = "https://www.engadget.com/2257186/htc-vive-eagle-review/"
CARRIED_ARM_URL = "https://www.engadget.com/2254031/apple-watch-series-12-will-listen-to-your-conversations/"
MUCKRACK_URL = "https://muckrack.com/daniel-cooper/articles"
# Format-built so the file never carries the literal ledger string (per #715).
LEDGER_28_NEEDLE = "falsification ledger: " + "28"
# Rotation window 870-874: D -> E -> A -> B; this run is the FOURTH leg.
EXPECTED_ORDER = [("B", "873"), ("A", "872"), ("E", "871"), ("D", "870"), ("C", "869")]
SCHEDULED_LOCAL = "Sun 2026-09-20 04:00:00 PDT"


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO, capture_output=True, text=True, timeout=60
    )


def _repo_grep(needle):
    """All repo files containing the needle (excludes __pycache__, per the
    #715 pattern-rescope lesson)."""
    hits = []
    for root, dirs, files in os.walk(REPO):
        if ".git" in root or "__pycache__" in root:
            continue
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "node_modules")]
        for f in files:
            p = os.path.join(root, f)
            if "__pycache__" in p:
                continue
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    if needle in fh.read():
                        hits.append(p)
            except (OSError, UnicodeError):
                pass
    return hits


def _read(relpath):
    with open(os.path.join(REPO, relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _get_block():
    data = _load_journalists()
    cooper = data["daniel_cooper"]
    return cooper["competitor_coverage"][BLOCK_KEY]


def _corpus_ids():
    ids = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "mechanism_id" and isinstance(v, int):
                    ids.append(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        try:
            with open(p, encoding="utf-8") as fh:
                d = yaml.safe_load(fh)
        except Exception:
            continue
        if d is not None:
            walk(d)
    # 867-871 are iteration-specific keys, not mechanism IDs.
    return [i for i in ids if i not in (867, 868, 869, 870, 871)]


# ---------------------------------------------------------------------------
# 1. Novelty: Type B #873 did not exist before this run
# ---------------------------------------------------------------------------

class TestNovelty873:
    def test_single_test_type_b_873_file(self):
        files = [f for f in os.listdir(os.path.join(REPO, "tests"))
                 if f.startswith("test_type_b_873")]
        assert files == [OWN_BASENAME]

    def test_type_b_873_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type B #873")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type B #873(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        method = _get_block()["research_method"]
        assert "zero test_type_b_873" in method
        assert "no Type B #873 in git log" in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism_id 754 pre-commit" in method
        assert "zero underscore-form 755" in method

    def test_870_871_872_window_legs_present_prior_to_873(self):
        log = _read("iteration-log.md")
        assert "## #870 Type D:" in log
        assert "## #871 Type E:" in log
        assert "## #872 Type A:" in log
        idx_870 = log.index("## #870 Type D:")
        idx_871 = log.index("## #871 Type E:")
        idx_872 = log.index("## #872 Type A:")
        assert idx_872 < idx_871 < idx_870

    def test_max_numeric_mechanism_id_755(self):
        """Max numeric mechanism_id in profiles/ is 755: this run's own
        addition (754 was the max pre-commit per the run's pre-commit grep)."""
        ids = _corpus_ids()
        assert max(ids) == 755, f"max mechanism_id should be 755, got {max(ids)}"
        assert ids.count(755) == 1, "mechanism_id 755 must appear exactly once"

    def test_no_underscore_756_keys(self):
        """Zero underscore-form 756 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-756 keys: {hits}"

    def test_no_dash_756_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-756 keys: {hits}"

    def test_no_numeric_756_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC)
        assert hits == [], f"unexpected numeric 756 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 870-874 window, fourth leg D->E->A->B
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard873:
    def test_window_is_870_874_fourth_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("869", "870", "871", "872", "873"):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["B", "A", "E", "D", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"

    def test_predecessor_is_type_a_872(self):
        proc = _git("log", "--oneline", "--grep", "Type A #872", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
# ---------------------------------------------------------------------------

class TestNoveltyAnchor873:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_b_873_daniel_cooper")
        assert BLOCK_KEY.endswith("apple_watch_carried")
        assert "vive_eagle" in BLOCK_KEY
        assert BLOCK_KEY == "type_b_873_daniel_cooper_engadget_vive_eagle_meta_benchmark_extension_vs_apple_watch_carried"


# ---------------------------------------------------------------------------
# 4. Mechanism 755 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism755Structure:
    def test_daniel_cooper_slug_entry_exists(self):
        data = _load_journalists()
        assert "daniel_cooper" in data, "top-level daniel_cooper slug entry missing"
        cooper = data["daniel_cooper"]
        assert cooper["name"] == JOURNALIST
        assert cooper["current_publication"] == "Engadget"

    def test_block_key_unique(self):
        """The 873 block key appears exactly once repo-wide."""
        hits = _repo_grep(BLOCK_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/careers/journalists.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 873
        assert block["type"] == "B"
        assert block["mechanism_id"] == 755
        assert block["goal_id"] == "goal_54093bda4145"

    def test_designed_keying_no_underscore_755(self):
        """Per #715: no underscore-form 755 key strings repo-wide."""
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], f"unexpected underscore-755 keys: {hits}"

    def test_required_fields_present(self):
        block = _get_block()
        for field in ("design", "finding", "new_meta_framing_arm",
                      "carried_apple_arm", "asymmetry_scorer_result_illustrative",
                      "confounders", "counterevidence", "connects_to",
                      "verdict", "research_method", "test_file"):
            assert field in block, f"missing field: {field}"

    def test_mechanism_ids_include_295_and_755(self):
        data = _load_journalists()
        ids = data["daniel_cooper"]["mechanism_ids"]
        assert 295 in ids, "m295 (Aug-25 Cooper mechanism) must be cross-referenced"
        assert 755 in ids, "m755 (this run) must be listed"

    def test_test_file_field_matches_own_basename(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + OWN_BASENAME


# ---------------------------------------------------------------------------
# 5. New Meta-framing arm: HTC Vive Eagle review (Sep 15 2026)
# ---------------------------------------------------------------------------

class TestMechanism755MetaArm:
    def test_arm_metadata(self):
        arm = _get_block()["new_meta_framing_arm"]
        assert arm["url"] == NEW_ARM_URL
        assert arm["byline"] == "Daniel Cooper (sole)"
        assert arm["date"] == "2026-09-15"
        assert arm["publication"] == "engadget"
        assert arm["rating"] == "7.4 / 10"

    def test_inherent_issues_marker(self):
        arm = _get_block()["new_meta_framing_arm"]
        markers = arm["meta_register_markers_verbatim"]
        assert any("inherent issues (privacy and otherwise) of any Meta product" in m
                   for m in markers)

    def test_skeptic_self_declaration(self):
        arm = _get_block()["new_meta_framing_arm"]
        markers = arm["meta_register_markers_verbatim"]
        assert any("AI camera glasses skeptic" in m for m in markers)

    def test_htc_privacy_pro_documented(self):
        arm = _get_block()["new_meta_framing_arm"]
        assert "Welcome focus on user privacy" in arm["pros"]
        markers = arm["meta_register_markers_verbatim"]
        assert any("at least gestures toward user privacy" in m for m in markers)

    def test_burn_billions_marker(self):
        arm = _get_block()["new_meta_framing_arm"]
        markers = arm["meta_register_markers_verbatim"]
        assert any("burn billions upon billions" in m for m in markers)

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["new_meta_framing_arm"]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]
        assert "INSIDE a competitor" in arm["in_review_framing_note"]


# ---------------------------------------------------------------------------
# 6. Carried Apple arm (per #807, not re-scored this run)
# ---------------------------------------------------------------------------

class TestMechanism755AppleArmCarried:
    def test_carried_url(self):
        arm = _get_block()["carried_apple_arm"]
        assert arm["url"] == CARRIED_ARM_URL
        assert arm["byline"] == "Daniel Cooper (sole)"

    def test_carried_characterization(self):
        arm = _get_block()["carried_apple_arm"]
        assert "Less adversarial register" in arm["carried_characterization"]
        assert "per #807" in arm["carried_characterization"]
        assert "Sep-13 Conditt block" in arm["carried_characterization"]

    def test_excerpt_consistent_markers(self):
        arm = _get_block()["carried_apple_arm"]
        markers = arm["apple_register_markers_verbatim"]
        assert any("listen out for" in m for m in markers)
        assert any("opt-in" in m for m in markers)
        assert any("less dystopian" in m for m in markers)

    def test_date_disclosed_as_derived(self):
        arm = _get_block()["carried_apple_arm"]
        assert "never filled by guessing" in arm["date_note"]

    def test_carried_tone_basis(self):
        arm = _get_block()["carried_apple_arm"]
        assert arm["tone_illustrative"] == -0.1
        assert "Carried un-rescored per #807" in arm["tone_basis"]


# ---------------------------------------------------------------------------
# 7. Scorer: illustrative delta arithmetic
# ---------------------------------------------------------------------------

class TestMechanism755Scorer:
    def _scorer(self):
        return _get_block()["asymmetry_scorer_result_illustrative"]

    def test_delta_arithmetic(self):
        s = self._scorer()
        assert s["illustrative_delta_apple_minus_meta"] == pytest.approx(0.2)
        assert s["delta_calc"] == "-0.10 - (-0.30) = +0.20"
        assert round(s["target_avg"] - s["reference_avg"], 2) == pytest.approx(0.2)

    def test_two_entity_band(self):
        s = self._scorer()
        assert s["two_entity_band"] == [-0.3, -0.1]
        assert s["target_entity"] == "Apple"
        assert s["reference_entity"] == "Meta"

    def test_connects_to_295_and_150(self):
        block = _get_block()
        assert block["connects_to"] == [295, 150]
        assert "295" in block["extends"]

    def test_meta_tone_and_apple_tone(self):
        block = _get_block()
        assert block["new_meta_framing_arm"]["tone_illustrative"] == -0.3
        assert block["carried_apple_arm"]["tone_illustrative"] == -0.1

    def test_third_review_unit_extension(self):
        block = _get_block()
        assert "THIRD review unit" in block["design"] or "third review unit" in block["finding"]
        assert "XGIMI MemoMind One Jun 2026 -> HTC Vive Eagle Sep 2026" in block["extends"]


# ---------------------------------------------------------------------------
# 8. Statistical discipline
# ---------------------------------------------------------------------------

class TestMechanism755Discipline:
    def _scorer(self):
        return _get_block()["asymmetry_scorer_result_illustrative"]

    def test_p_d_ci_not_calculated(self):
        s = self._scorer()
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        s = self._scorer()
        assert s["is_significant"] is False
        assert _get_block()["is_significant"] is False
        assert "engine NOT run" in s["engine"]

    def test_verdict_and_correlation(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["correlation_not_causation"] is True
        assert self._scorer()["correlation_not_causation"] is True

    def test_no_analysis_json_and_not_artifact_grade(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert self._scorer()["artifact_grade"] == "NOT artifact-grade"

    def test_falsification_ledger_holds_at_27(self):
        block = _get_block()
        fam = block["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "ledger holds at 27" in fam
        assert _repo_grep(LEDGER_28_NEEDLE) == []

    def test_research_method_recorded(self):
        method = _get_block()["research_method"]
        assert "7 browser.search query sets" in method
        assert "0 browser.open" in method
        assert "per #503" in method
        assert "no zero-coverage claims per the #492 rule" in method

    def test_confounder_distribution(self):
        confs = _get_block()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3, f"expected 3 STRONG, got {len(strong)}"
        assert len(moderate) == 3, f"expected 3 MODERATE, got {len(moderate)}"
        assert len(weak) == 2, f"expected 2 WEAK, got {len(weak)}"
        assert strong[0] == confs[0], "strongest confounder must come first"

    def test_counterevidence_count(self):
        ces = _get_block()["counterevidence"]
        assert len(ces) == 3, f"expected 3 counterevidence items, got {len(ces)}"


# ---------------------------------------------------------------------------
# 9. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync873:
    def test_readme_row(self):
        readme = _read("README.md")
        assert "test_type_b_873_daniel_cooper" in readme
        assert "Type B #873" in readme
        assert "44642" in readme and "1201" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_b_873_daniel_cooper" in arch
        assert "44642 tests across 1201 test files" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog873:
    def _entry(self):
        log = _read("iteration-log.md")
        return log.split("## #873 Type B")[1].split("## #872")[0]

    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #873 Type B" in log

    def test_entry_documents_mechanism(self):
        entry = self._entry()
        assert "755" in entry
        assert "Daniel Cooper" in entry
        assert "Vive Eagle" in entry

    def test_entry_documents_window(self):
        entry = self._entry()
        assert "870-874" in entry
        assert "FOURTH leg" in entry


# ---------------------------------------------------------------------------
# 11. Date grounding
# ---------------------------------------------------------------------------

class TestDateGrounding873:
    def test_run_date_is_sunday(self):
        import datetime
        assert datetime.date(2026, 9, 20).strftime("%A") == "Sunday"

    def test_meta_arm_date_is_tuesday(self):
        import datetime
        assert datetime.date(2026, 9, 15).strftime("%A") == "Tuesday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Sun 2026-09-20 04:00:00 PDT"
        block = _get_block()
        assert block["date"] == "2026-09-20 04:00 PDT"


# ---------------------------------------------------------------------------
# 12. Register extension: m295 series Jun -> Sep intensification
# ---------------------------------------------------------------------------

class TestRegisterExtension873:
    def test_series_lineage_documented(self):
        block = _get_block()
        xrefs = " ".join(block["cross_references"])
        assert "mechanism 295" in xrefs
        assert "XGIMI MemoMind One Jun 2026" in xrefs

    def test_register_intensification(self):
        block = _get_block()
        assert "INTENSIFIES" in block["finding"] or "intensification" in block["extends"]

    def test_same_week_entity_asymmetry(self):
        block = _get_block()
        assert "within-week entity asymmetry" in block["finding"]
