"""
Type B #878 (rotation window 875-879, FOURTH leg: D->E->A->B): Cristina Criddle
(Financial Times AI correspondent) - ethics-governance register asymmetry:
accountability-adversarial on the FT x OpenAI licensing-deal partner vs
constructive within-piece Meta contrast.

MECHANISM #758: within-journalist cross-entity register asymmetry at the
ethics-governance layer. PRIMARY OpenAI arm: Criddle's FT piece "OpenAI's head
of ethics leaves start-up less than a year after joining" (~Aug 11 2026;
byline Cristina Criddle with Rafe Rosner-Uddin; FT original paywalled,
attested via Criddle's LinkedIn verbatim lede + six corroborating mirrors) -
"left quietly in July. No public announcement followed. And no replacement
has been named"; "she was the only dedicated ethicist at the company";
"latest in a series of departures... including safety researchers Johannes
Heidecke and Joshua Achiam"; "OpenAI admitted its models had hacked another
company, Hugging Face, during internal testing." SECONDARY OpenAI arm
(headline-tier): Criddle's Feb-3-2026 FT piece "Sources: OpenAI is
prioritizing ChatGPT over long-term research, prompting senior staff
departures" (Techmeme river attribution) - same accountability-adversarial
register on the same partner, six months earlier. META ELEMENT (within-piece
contrast, not a standalone arm): Bakalar "spent six years as chief ethicist
at Meta, where she built its AI ethics programs and integrated them into
products like Instagram and Facebook" - in a story about OpenAI's ethics
vacuum, Meta is the institution where the departed ethicist DID build
programs. Illustrative tones: Meta +0.15 (contrast), OpenAI -0.40 (primary);
illustrative delta (Meta minus OpenAI) +0.55 - the non-payer outscores the
$5-10M/yr deal partner by more than half the register scale inside the
partner's own correspondent's piece.

FALSIFICATION: TWENTY-EIGHTH falsification-family member (ledger 27->28).
The FT x OpenAI licensing deal (mechanism 54, Apr 2024, ~$5-10M/yr per #872)
predicts softer OpenAI coverage; Criddle's two accountability-adversarial arms
at the ethics-governance layer falsify the uniform-softening prediction at
that layer. Writer-level falsification of the deal-gradient prediction
(precedent: mechanism 593 Victoria Song, FIFTEENTH member). First
falsification member at the ethics-governance layer; extends the family to
the FT x OpenAI deal. Verdict directionally_supported_not_proven on the
asymmetry; falsified_softer_prediction on the uniform-softening claim.

NOVELTY VERIFICATION (run pre-commit, Sep 20 2026 ~09:05 PDT, before any edits):
- glob: zero test_type_b_878*.py files on disk
- git log --all --grep="Type B #878": zero hits (no prior #878 main commit)
- numeric mechanism_id max in profiles/: 757 (758 is this run's own addition)
- format-built underscore needles: zero underscore-form 758 key strings repo-wide
  (__pycache__ artifacts excluded per the #715 pattern-rescope lesson)
- zero numeric "mechanism_id: 758" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- "cristina_criddle" top-level slug zero-hit repo-wide pre-commit
- all six evidence URLs zero-hit repo-wide pre-commit
- REJECTED candidates this run: Jason England (Type B #737 in corpus; Sep-2026
  smart-glasses archive rich but no clean new asymmetry), Dhruv Mehrotra
  (WIRED NameTag work already in #877; no clean same-writer Apple comparator),
  Lauren Goode / Snap (no clean new bylined primary arm), Lucas Ropek /
  TechCrunch (no useful clean same-journalist pair)

ROTATION: this is the FOURTH leg of rotation window 875-879 (D->E->A->B).
Prior legs present in iteration-log.md: #875 Type D, #876 Type E, #877 Type A
(09:00 PDT). Expected cycle position: B (878) after A (877) after E (876)
after D (875) after C (874).

RESEARCH METHOD: 6 browser.search query sets this run (Criddle OpenAI -
SELECTED primary arm via LinkedIn verbatim lede; Bakalar corroboration set -
5 mirrors; Criddle Meta superintelligence/Llama - REJECTED, no clean Meta arm;
Criddle Meta 2026 - no fresh Meta arm; Techmeme 260203/p7 attribution -
SELECTED secondary arm headline-tier; Criddle bio - beats Meta/Google/OpenAI/
TikTok). 0 browser.open per #503. All URLs copied verbatim from Full-URL
listings. No URL construction. No zero-coverage claims per #492.

DESIGN NOTES:
- The Meta element is expressed INSIDE the OpenAI piece as credentialing
  contrast, not a standalone Meta piece (STRONG confounder, disclosed);
  arm independence limited by construction.
- The secondary (Feb-3) arm is headline-tier only (STRONG confounder).
- p_value / cohens_d / ci_95 are NOT_CALCULATED (deliberate). is_significant
  is false. engine NOT run. correlation_not_causation is true.
- TWENTY-EIGHTH falsification-family member (ledger 27->28); the the-verge
  ledger guard advances to TWENTY-NINTH. The #875/#876 tests asserting
  28th-absent become tombstones per the established ledger-advance pattern
  (as #865/#866 did for the 27th); they are NOT modified this run.
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
PROFILES_DIR = os.path.join(REPO, "profiles")
OWN_BASENAME = "test_type_b_878_cristina_criddle_ft_openai_ethics_chief_exit_vs_meta_contrast_sep20_9am.py"
BLOCK_KEY = "type_b_878_cristina_criddle_ft_openai_ethics_chief_exit_vs_meta_contrast"
JOURNALIST = "Cristina Criddle"
ITERATION = 878
ITER_TYPE = "B"
MECH_ID = 758
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched post-commit per #565
# NEXT_ID / MECH_ID needles are format-built so the file never carries a
# literal underscore-form key string (per the #715 lesson).
MECH_ID_MARKER = "mechanism" + "_758"
NEXT_ID_MARKER = "mechanism" + "_759"
NEXT_ID_NUMERIC = "mechanism_id: " + "759"
NEXT_ID_DASH = "mechanism" + "-759"
BAKALAR_URL = "https://www.linkedin.com/posts/cristina-criddle_openais-head-of-ethics-leaves-start-up-less-activity-7492716537636651009-nvXA"
PRIORITIZATION_URL = "https://www.techmeme.com/260203/p7"
BIO_URL = "https://www.allamericanspeakers.com/speakers/457355/Cristina-Criddle"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
# Rotation window 875-879: D -> E -> A -> B -> C; this run is the FOURTH leg.
EXPECTED_ORDER = [("B", "878"), ("A", "877"), ("E", "876"), ("D", "875"), ("C", "874")]
SCHEDULED_LOCAL = "Sun 2026-09-20 09:00:00 PDT"


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


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
    return "\n".join(parts)


def _read(relpath):
    with open(os.path.join(REPO, relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _get_block():
    data = _load_journalists()
    criddle = data["cristina_criddle"]
    return criddle["competitor_coverage"][BLOCK_KEY]


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
    return ids


# ---------------------------------------------------------------------------
# 1. Novelty: Type B #878 did not exist before this run
# ---------------------------------------------------------------------------

class TestNovelty878:
    def test_single_test_type_b_878_file(self):
        files = [f for f in os.listdir(os.path.join(REPO, "tests"))
                 if f.startswith("test_type_b_878")]
        assert files == [OWN_BASENAME]

    def test_type_b_878_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type B #878")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type B #878(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        method = _get_block()["research_method"]
        assert "zero test_type_b_878" in method
        assert "no Type B #878 in git log" in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism_id 757 pre-commit" in method
        assert "zero underscore-form 758" in method
        assert '"cristina_criddle" top-level slug zero-hit repo-wide pre-commit' in method

    def test_875_876_877_window_legs_present_prior_to_878(self):
        log = _read("iteration-log.md")
        assert "## #875 Type D:" in log
        assert "## #876 Type E:" in log
        assert "## #877 Type A:" in log
        idx_875 = log.index("## #875 Type D:")
        idx_876 = log.index("## #876 Type E:")
        idx_877 = log.index("## #877 Type A:")
        assert idx_877 < idx_876 < idx_875

    def test_max_numeric_mechanism_id_758(self):
        """Max numeric mechanism_id in profiles/ is 758: this run's own
        addition (757 was the max pre-commit per the run's pre-commit grep)."""
        ids = _corpus_ids()
        assert max(ids) == 758, f"max mechanism_id should be 758, got {max(ids)}"
        assert ids.count(758) == 1, "mechanism_id 758 must appear exactly once"

    def test_no_underscore_759_keys(self):
        """Zero underscore-form 759 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-759 keys: {hits}"

    def test_no_dash_759_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-759 keys: {hits}"

    def test_no_numeric_759_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC)
        assert hits == [], f"unexpected numeric 759 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 875-879 window, fourth leg D->E->A->B
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard878:
    def test_window_is_875_879_fourth_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("874", "875", "876", "877", "878"):
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

    def test_predecessor_is_type_a_877(self):
        proc = _git("log", "--oneline", "--grep", "Type A #877", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
# ---------------------------------------------------------------------------

class TestNoveltyAnchor878:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_b_878_cristina_criddle")
        assert BLOCK_KEY.endswith("meta_contrast")
        assert "ethics_chief_exit" in BLOCK_KEY
        assert BLOCK_KEY == "type_b_878_cristina_criddle_ft_openai_ethics_chief_exit_vs_meta_contrast"


# ---------------------------------------------------------------------------
# 4. Mechanism 758 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism758Structure:
    def test_cristina_criddle_slug_entry_exists(self):
        data = _load_journalists()
        assert "cristina_criddle" in data, "top-level cristina_criddle slug entry missing"
        criddle = data["cristina_criddle"]
        assert criddle["name"] == JOURNALIST
        assert criddle["current_publication"] == "Financial Times"

    def test_block_key_unique(self):
        """The 878 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(BLOCK_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/careers/journalists.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 878
        assert block["type"] == "B"
        assert block["mechanism_id"] == 758
        assert block["goal_id"] == "goal_54093bda4145"

    def test_designed_keying_no_underscore_758(self):
        """Per #715: no underscore-form 758 key strings repo-wide."""
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], f"unexpected underscore-758 keys: {hits}"

    def test_required_fields_present(self):
        block = _get_block()
        for field in ("design", "finding", "openai_bakalar_arm",
                      "openai_chatgpt_prioritization_arm",
                      "meta_within_piece_contrast",
                      "asymmetry_scorer_result_illustrative",
                      "confounders", "counterevidence", "connects_to",
                      "verdict", "falsification_verdict",
                      "falsification_family", "ledger",
                      "research_method", "test_file"):
            assert field in block, f"missing field: {field}"

    def test_mechanism_ids_include_758(self):
        data = _load_journalists()
        ids = data["cristina_criddle"]["mechanism_ids"]
        assert 758 in ids, "m758 (this run) must be listed"

    def test_test_file_field_matches_own_basename(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + OWN_BASENAME


# ---------------------------------------------------------------------------
# 5. Primary OpenAI arm: Bakalar ethics-chief exit (Aug 11 2026)
# ---------------------------------------------------------------------------

class TestMechanism758BakalarArm:
    def test_arm_metadata(self):
        arm = _get_block()["openai_bakalar_arm"]
        assert arm["url"] == BAKALAR_URL
        assert arm["byline"] == "Cristina Criddle with Rafe Rosner-Uddin"
        assert arm["date"] == "2026-08-11"
        assert arm["publication"] == "financial-times"

    def test_quiet_exit_markers(self):
        arm = _get_block()["openai_bakalar_arm"]
        markers = arm["accountability_register_markers_verbatim"]
        assert any("left quietly in July. No public announcement followed" in m
                   for m in markers)
        assert any("only dedicated ethicist at the company, and there is no replacement" in m
                   for m in markers)

    def test_safety_departures_marker(self):
        arm = _get_block()["openai_bakalar_arm"]
        markers = arm["accountability_register_markers_verbatim"]
        assert any("Johannes Heidecke and Joshua Achiam" in m for m in markers)

    def test_huggingface_breach_marker(self):
        arm = _get_block()["openai_bakalar_arm"]
        markers = arm["accountability_register_markers_verbatim"]
        assert any("Hugging Face" in m for m in markers)

    def test_evidence_tier_disclosed(self):
        arm = _get_block()["openai_bakalar_arm"]
        assert "EXCERPT-TIER" in arm["evidence_tier"]
        assert "0 browser.open" in arm["evidence_tier"]
        assert "paywalled" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["openai_bakalar_arm"]
        assert arm["tone_illustrative"] == pytest.approx(-0.4)


# ---------------------------------------------------------------------------
# 6. Secondary OpenAI arm: ChatGPT prioritization (Feb 3 2026, headline-tier)
# ---------------------------------------------------------------------------

class TestMechanism758SecondaryArm:
    def test_arm_metadata(self):
        arm = _get_block()["openai_chatgpt_prioritization_arm"]
        assert arm["url"] == PRIORITIZATION_URL
        assert arm["byline"] == "Cristina Criddle"
        assert arm["date"] == "2026-02-03"

    def test_headline_tier_disclosed(self):
        arm = _get_block()["openai_chatgpt_prioritization_arm"]
        assert "HEADLINE-TIER" in arm["evidence_tier"]

    def test_tone(self):
        arm = _get_block()["openai_chatgpt_prioritization_arm"]
        assert arm["tone_illustrative"] == pytest.approx(-0.3)


# ---------------------------------------------------------------------------
# 7. Meta within-piece contrast
# ---------------------------------------------------------------------------

class TestMechanism758MetaContrast:
    def test_contrast_markers(self):
        contrast = _get_block()["meta_within_piece_contrast"]
        markers = contrast["meta_contrast_markers_verbatim"]
        assert any("six years as chief ethicist at Meta" in m for m in markers)
        assert any("built its AI ethics programs" in m for m in markers)
        assert any("Instagram and Facebook" in m for m in markers)

    def test_construction_disclosed(self):
        contrast = _get_block()["meta_within_piece_contrast"]
        assert "INSIDE the Bakalar piece" in contrast["context"]
        assert "not a separately scored Meta arm" in contrast["context"]

    def test_tone(self):
        contrast = _get_block()["meta_within_piece_contrast"]
        assert contrast["tone_illustrative"] == pytest.approx(0.15)


# ---------------------------------------------------------------------------
# 8. Scorer: illustrative delta arithmetic
# ---------------------------------------------------------------------------

class TestMechanism758Scorer:
    def _scorer(self):
        return _get_block()["asymmetry_scorer_result_illustrative"]

    def test_delta_arithmetic(self):
        s = self._scorer()
        assert s["illustrative_delta_meta_minus_openai"] == pytest.approx(0.55)
        assert s["delta_calc"] == "+0.15 - (-0.40) = +0.55"
        assert round(s["target_avg"] - s["reference_avg"], 2) == pytest.approx(0.55)

    def test_two_entity_band(self):
        s = self._scorer()
        assert s["two_entity_band"] == [-0.4, 0.15]
        assert s["target_entity"] == "Meta"
        assert s["reference_entity"] == "OpenAI"

    def test_connects_to_54_593_643_625(self):
        block = _get_block()
        assert block["connects_to"] == [54, 593, 643, 625]

    def test_secondary_arm_sensitivity(self):
        s = self._scorer()
        assert "+0.50" in s["secondary_arm_sensitivity"]

    def test_meta_tone_and_openai_tone(self):
        block = _get_block()
        assert block["meta_within_piece_contrast"]["tone_illustrative"] == pytest.approx(0.15)
        assert block["openai_bakalar_arm"]["tone_illustrative"] == pytest.approx(-0.4)


# ---------------------------------------------------------------------------
# 9. Statistical discipline + falsification verdict
# ---------------------------------------------------------------------------

class TestMechanism758Discipline:
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

    def test_verdicts(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_verdict"] == "falsified_softer_prediction"
        assert block["correlation_not_causation"] is True
        assert self._scorer()["correlation_not_causation"] is True

    def test_no_analysis_json_and_not_artifact_grade(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert self._scorer()["artifact_grade"] == "NOT artifact-grade"

    def test_research_method_recorded(self):
        method = _get_block()["research_method"]
        assert "6 browser.search query sets" in method
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
# 10. Falsification ledger: 27 -> 28 transition
# ---------------------------------------------------------------------------

class TestLedgerTransition878:
    def test_exactly_one_28th_member_in_profiles(self):
        count = _profiles_text().count(MEMBER_28)
        assert count == 1, count

    def test_28th_member_is_m758_criddle(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(MEMBER_28) == 1
        assert "(ledger 27->28)" in text

    def test_27th_member_still_exactly_once(self):
        count = _profiles_text().count("TWENTY-SEVENTH falsification-family member")
        assert count == 1, count

    def test_no_29th_member_form(self):
        assert MEMBER_29 not in _profiles_text()

    def test_block_ledger_27_to_28(self):
        block = _get_block()
        assert "ledger 27->28" in block["falsification_family"]
        assert "ledger 27->28" in block["ledger"].lower()

    def test_verge_guard_advanced_to_29th(self):
        verge = _read("profiles/the-verge.yaml")
        assert "negative-guard convention continues at TWENTY-NINTH" in verge
        assert "TWENTY-EIGHTH member-form landed in profiles/careers/journalists.yaml" in verge


# ---------------------------------------------------------------------------
# 11. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync878:
    def test_readme_row(self):
        readme = _read("README.md")
        assert "test_type_b_878_cristina_criddle" in readme
        assert "Type B #878" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_b_878_cristina_criddle" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch


# ---------------------------------------------------------------------------
# 12. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog878:
    def _entry(self):
        log = _read("iteration-log.md")
        return log.split("## #878 Type B")[1].split("## #877")[0]

    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #878 Type B" in log

    def test_entry_documents_mechanism(self):
        entry = self._entry()
        assert "758" in entry
        assert "Criddle" in entry
        assert "Bakalar" in entry

    def test_entry_documents_window(self):
        entry = self._entry()
        assert "875-879" in entry
        assert "FOURTH leg" in entry

    def test_entry_documents_ledger(self):
        entry = self._entry()
        assert "27->28" in entry or "TWENTY-EIGHTH" in entry


# ---------------------------------------------------------------------------
# 13. Date grounding
# ---------------------------------------------------------------------------

class TestDateGrounding878:
    def test_run_date_is_sunday(self):
        import datetime
        assert datetime.date(2026, 9, 20).strftime("%A") == "Sunday"

    def test_bakalar_arm_date_is_tuesday(self):
        import datetime
        assert datetime.date(2026, 8, 11).strftime("%A") == "Tuesday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Sun 2026-09-20 09:00:00 PDT"
        block = _get_block()
        assert block["date"] == "2026-09-20 09:00 PDT"
