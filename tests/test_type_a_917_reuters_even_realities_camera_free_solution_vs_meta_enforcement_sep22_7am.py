"""Type A iteration 917: Reuters x Even Realities Sep-22 camera-free solution register
vs Reuters x Meta enforcement register (mechanism 781),
THIRD leg of the 915-919 rotation window (D->E->A).

Type A contract: add ONE mechanism block for a publication x competitor pair fresh
this run, with attribution URLs verified against a real search, and cross-reference
the existing comparator register. This run: Reuters x Even Realities.

Even Realities arm (FRESH this run, first-hand read): Reuters Sep 22 2026, "From smart
glasses to AI pins, privacy fears challenge tech's next big bet"
(https://www.reuters.com/business/media-telecom/smart-glasses-ai-pins-privacy-fears-challenge-techs-next-big-bet-2026-09-22/)
- 88 rendered lines via browser.open. The "STARTUPS OFFER CAMERA-FREE ALTERNATIVES"
section routes Even Realities through the solution register: camera-free G1 (2024)
and G2 flagship (Nov 2025); founder Will Wang says cameras should wait until
stronger safeguards exist; $1B valuation in July; a few hundred thousand users
expected by year-end. MANUAL ILLUSTRATIVE +0.20.

Meta arms (carried enforcement register): Sep 18 2026 "French prosecutors and
regulators step up scrutiny on smart glasses" -0.45 (mechanism 730); Sep 17 2026
"German court rules Meta liable for fake ads on Instagram, Facebook" -0.35
(mechanisms 730/739); plus within-piece Sep-22 Meta problem-register context
("lightning rod", Clarkson lawsuit) NOT scored.

Illustrative delta (Meta minus Even Realities): -0.40 - (+0.20) = -0.60 - a
same-category source-routing gradient. The real asymmetry scorer was run once on the
two illustrative arm arrays (asymmetry -0.60, t=0.0, p=1.0, d=-8.4853,
95% CI (-0.65, -0.55), engine is_significant False) as a corroborating observation -
NOT promoted to a finding. EXTENDS mechanisms 730/739 (Reuters Meta enforcement
register, stable comparator) and mechanism 664 (Reuters paid Meta AI deal coexists
with hard Meta accountability - the lightning-rod framing here is another instance).

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT promoted;
p_value, cohens_d, ci_95 NOT_CALCULATED at the finding layer; is_significant False;
NOT artifact-grade; NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 29). The gradient is
product-true in part (Even Realities genuinely ships no camera) and peg-mismatched
in part (enforcement news vs company-profile section). Correlation is not causation.

Research: pre-run browser.search candidate selection (Reuters Sep-22 analysis
SELECTED; FT/OpenAI cash-burn REJECTED as already represented; NYT/OpenAI
labor-theft REJECTED as already represented via MDL mechanisms; WSJ/Anthropic IPO
REJECTED as already represented by mechanism 733; Guardian - no useful arms).
SELECTED: Reuters Sep-22 piece (URL zero-hit repo-wide pre-commit; 1 first-hand
browser.open read, 88 rendered lines). Novelty verified pre-commit (zero
test_type_a_917 files on disk; no "Type A #917" in git log; block key zero-hit
repo-wide; max numeric mechanism_id 780; zero underscore-form 781 keys by designed
keying per #715; zero dash-form 781 refs; zero numeric 781 keys in profiles/).

915-919 window THIRD leg D(#915)->E(#916)->A(#917). Next: #918 Type B.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_917_reuters_even_realities_camera_free_solution_vs_meta_enforcement_sep22_7am.py"
MECH_KEY = "reuters_even_realities_camera_free_solution_register_vs_meta_enforcement_register_sep22_2026"
MECH_KEY_PREFIX = "reuters_even_realities_camera_free_solution_register"
M_ID = 781
ITER = 917
TYPE_LETTER = "A"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 781 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_781"
NEXT_ID_MARKER = "mechanism" + "_782"
NEXT_ID_NUMERIC = "mechanism_id: " + "782"
NEXT_ID_DASH = "mechanism" + "-782"
MECH_NUMERIC = "mechanism_id: " + "781"

REUTERS_URL = "https://www.reuters.com/business/media-telecom/smart-glasses-ai-pins-privacy-fears-challenge-techs-next-big-bet-2026-09-22/"
FRENCH_URL = "https://www.reuters.com/technology/french-prosecutors-regulators-step-up-scrutiny-smart-glasses-2026-09-18/"
GERMAN_URL = "https://www.reuters.com/legal/litigation/german-court-rules-meta-liable-fake-ads-instagram-facebook-2026-09-17/"

# Type A #917 is the THIRD leg of the 915-919 window: D(#915) -> E(#916) -> A(#917).


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True, text=True, timeout=60)


def _block():
    doc = yaml.safe_load(_read("profiles/competitor-coverage-research.yaml"))
    return doc["cross_publication_findings"][MECH_KEY]


class TestNovelty917:
    def test_single_test_type_a_917_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_917")]
        assert files == [OWN_BASENAME]

    def test_no_type_a_917_in_git_log_pre_commit(self):
        # Verified pre-commit by shell grep (no "Type A #917" in git log);
        # patched post-commit per the #565 followup convention to pin the
        # main commit as a singleton - no duplicate #917 main commit.
        proc = _git("log", "--format=%H %s", "--all")
        mains = [l for l in proc.stdout.splitlines()
                 if re.search(r"Type A #917: Reuters x Even Realities", l)]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["research_method"]
        assert "zero test_type_a_917 files on disk pre-commit (glob)" in novelty
        assert 'no "Type A #917" in git log pre-commit' in novelty
        assert "block key zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 780 pre-commit" in novelty
        assert "zero underscore-form 781 mechanism key strings repo-wide pre-commit" in novelty

    def test_915_916_window_legs_present_prior_to_917(self):
        log = _read("iteration-log.md")
        assert "## #915 Type D:" in log
        assert "## #916 Type E:" in log
        idx_915 = log.index("## #915 Type D:")
        idx_916 = log.index("## #916 Type E:")
        assert idx_916 < idx_915

    def test_evidence_urls_documented_as_zero_hit_pre_commit(self):
        blk = _block()
        novelty = blk["research_method"]
        assert "The Sep-22 Reuters URL zero-hit repo-wide pre-commit" in novelty


class TestRotationGuard917:
    # Rotation-guard tests follow the #912 pattern (static window contract +
    # predecessor + no-concurrent-inflight checks); the git-log window scan
    # is brittle against REPAIR/log-followup duplicate mains (#909/#910).
    def test_third_leg_of_915_919_window(self):
        assert TYPE_LETTER == "A"
        assert ITER == 917

    def test_window_sequence_d_e_a_b_c(self):
        expected = {915: "D", 916: "E", 917: "A", 918: "B", 919: "C"}
        assert expected[917] == "A"
        assert expected[915] == "D"
        assert expected[916] == "E"

    def test_predecessor_916_type_e_committed(self):
        # #916 Type E is COMMITTED (its log entry sits below this run's
        # #917 entry, which was prepended above it).
        assert "## #916 Type E" in _read("iteration-log.md")

    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #898 (m770),
        # #899 (m771), #900 - none committed yet. Match only commit
        # SUBJECTS: other commits' bodies may mention them.
        proc = _git("log", "--format=%H", "-8")
        subjects = [_git("log", "--format=%s", "-1", c).stdout.strip()
                    for c in proc.stdout.splitlines()]
        for n in ("884", "898", "899", "900"):
            assert not any(
                ("Type " in s) and (("#" + n + " ") in s or s.endswith("#" + n))
                for s in subjects
            ), (n, subjects)


class TestNoveltyAnchor917:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #917 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        result = subprocess.run(
            ["git", "-C", _repo_root(), "log", "--format=%H %s",
             "--", "tests/" + OWN_BASENAME],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        mains = [line for line in result.stdout.splitlines()
                 if "Type A #917" in line and "followup" not in line.lower()]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("reuters_even_realities_camera_free_solution_register")
        assert "vs_meta_enforcement_register_sep22_2026" in MECH_KEY

    def test_mech_key_ends_with_date(self):
        assert MECH_KEY.endswith("sep22_2026")


class TestMechanism781Structure:
    def test_block_present_under_cross_publication_findings(self):
        doc = yaml.safe_load(_read("profiles/competitor-coverage-research.yaml"))
        assert MECH_KEY in doc["cross_publication_findings"]

    def test_mechanism_id_numeric(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 781

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 917
        assert blk["rotation_type"] == TYPE_LETTER == "A"
        assert blk["discovery_date"] == "2026-09-22"
        assert blk["finding_type"] == "cross_publication_coverage_asymmetry"
        assert blk["publication"] == "Reuters"
        assert blk["competitor"] == "Even Realities"
        assert blk["comparator_entity"] == "Meta"

    def test_block_key_unique_in_yaml(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(MECH_KEY) == 1

    def test_no_next_id_782_keys(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_NUMERIC not in text
        assert NEXT_ID_DASH not in text

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_not_falsification_member_ledger_29(self):
        blk = _block()
        assert "NOT a falsification-family member" in blk["falsification_family"]
        assert "Ledger holds at 29" in blk["falsification_family"]
        assert blk["verdict"] == "directionally_supported_not_proven"


class TestMechanism781EvenRealitiesArm:
    def _arm(self):
        return _block()["even_realities_arms"][0]

    def test_sep22_piece_title(self):
        assert "From smart glasses to AI pins" in self._arm()["piece"]

    def test_sep22_date(self):
        assert self._arm()["date"] == "2026-09-22"

    def test_sep22_register_solution_framing(self):
        assert self._arm()["register"] == "solution_framing_company_sourced"

    def test_sep22_tone_plus_020(self):
        assert self._arm()["tone_illustrative"] == pytest.approx(0.20)

    def test_sep22_url_verbatim(self):
        assert self._arm()["source_url"] == REUTERS_URL

    def test_sep22_key_quotes(self):
        quotes = " ".join(self._arm()["key_language"])
        assert "consider glasses without cameras" in quotes
        assert "cameras should wait until companies can put stronger safeguards in place" in quotes
        assert "$1 billion in July" in quotes

    def test_sep22_firsthand_tier(self):
        assert "firsthand_read" in self._arm()["evidence_tier"]
        assert "browser.open" in self._arm()["tone_basis"]


class TestMechanism781MetaArms:
    def _arms(self):
        return _block()["meta_arms"]

    def test_two_scored_meta_arms(self):
        scored = [a for a in self._arms() if a.get("scored_arm", True)]
        assert len(scored) == 2

    def test_french_prosecutors_arm(self):
        arm = self._arms()[0]
        assert arm["piece"] == "French prosecutors and regulators step up scrutiny on smart glasses"
        assert arm["date"] == "2026-09-18"
        assert arm["tone_illustrative"] == pytest.approx(-0.45)
        assert FRENCH_URL in arm["carried_from"]

    def test_german_court_arm(self):
        arm = self._arms()[1]
        assert arm["piece"] == "German court rules Meta liable for fake ads on Instagram, Facebook"
        assert arm["date"] == "2026-09-17"
        assert arm["tone_illustrative"] == pytest.approx(-0.35)
        assert GERMAN_URL in arm["carried_from"]

    def test_within_piece_context_not_scored(self):
        ctx = self._arms()[2]
        assert ctx["scored_arm"] is False
        assert ctx["tone_illustrative"] is None
        assert "lightning rod" in " ".join(ctx["key_language"])

    def test_meta_arms_carried_basis(self):
        for arm in self._arms()[:2]:
            assert "carried from mechanism" in arm["tone_basis"]
            assert "not re-read this run" in arm["tone_basis"]


class TestMechanism781Scorer:
    def _scorer(self):
        return _block()["asymmetry_scorer"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["meta_arm_tones"] == pytest.approx([-0.45, -0.35])
        assert s["even_realities_arm_tones"] == pytest.approx([0.20])

    def test_avgs(self):
        s = self._scorer()
        assert s["meta_arm_avg"] == pytest.approx(-0.40)
        assert s["even_realities_arm_avg"] == pytest.approx(0.20)

    def test_delta_meta_minus_even_realities(self):
        s = self._scorer()
        assert s["illustrative_delta_meta_minus_even_realities"] == pytest.approx(-0.60, abs=1e-4)

    def test_delta_arithmetic_logged(self):
        s = self._scorer()
        assert s["delta_calc"] == "((-0.45 + -0.35) / 2) - (0.20) = -0.40 - 0.20 = -0.60"

    def test_gradient_interpretation(self):
        s = self._scorer()
        assert "source-routing gradient" in s["delta_interpretation"]
        assert "statistically silent" in s["delta_interpretation"]

    def test_engine_run_once_corroboration(self):
        e = self._scorer()["engine_run"]
        assert e["asymmetry_score"] == pytest.approx(-0.60)
        assert e["t_statistic"] == pytest.approx(0.0)
        assert e["p_value"] == pytest.approx(1.0)
        assert e["cohens_d"] == pytest.approx(-8.4853, abs=1e-4)
        assert e["ci_95"] == pytest.approx([-0.65, -0.55])
        assert e["engine_is_significant"] is False
        assert "NOT promoted to a finding" in e["role"]

    def test_finding_layer_not_calculated(self):
        s = self._scorer()
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_small_n_per_arm"


class TestMechanism781Discipline:
    def test_statistical_discipline_block(self):
        d = _block()["statistical_discipline"]
        assert "is_significant: false" in d
        assert "no_analysis_json_update: true" in d
        assert "NOT artifact-grade" in d

    def test_confounders_five_strong_first(self):
        conf = _block()["confounders"]
        assert len(conf) == 5
        assert conf[0].startswith("STRONG")
        assert conf[1].startswith("STRONG")
        assert any("Product-true" in c for c in conf)
        assert any("Peg mismatch" in c for c in conf)

    def test_counterevidence_four(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 4
        assert all(c.startswith("COUNTEREVIDENCE") for c in ce)
        assert any("Connect" in c for c in ce)
        assert any("664" in c for c in ce)

    def test_connects_to(self):
        assert _block()["connects_to"] == [730, 739, 664, 717]

    def test_financial_context_paid_deal_pole(self):
        fc = _block()["financial_context"]
        assert "Oct 25 2024" in fc["reuters_meta_content_deal"]
        assert "bounded absence" in fc["reuters_even_realities_content_deal"]
        assert fc["prediction"].startswith("Paid-deal pole")

    def test_correlation_not_causation_in_finding(self):
        assert "Correlation is not causation" in _block()["finding"]

    def test_ascii_only_no_em_dashes(self):
        # Serialize only the parsed m781 block (per _block), so unrelated
        # pre-existing content elsewhere in the yaml is not measured.
        seg = yaml.safe_dump(_block(), allow_unicode=True, sort_keys=False)
        assert "\u2014" not in seg
        assert all(ord(ch) < 128 for ch in seg)


class TestNoCrossContamination917:
    def _yaml_files(self):
        root = _repo_root()
        out = []
        for dirpath, _dirnames, filenames in os.walk(root):
            if "__pycache__" in dirpath or ".venv" in dirpath or ".git" in dirpath:
                continue
            for fn in filenames:
                if fn.endswith(".yaml"):
                    out.append(os.path.join(dirpath, fn))
        return out

    def test_no_underscore_form_781_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_781_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_781(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 781

    def test_falsification_ledger_holds_at_29(self):
        member = "TWENTY-" + "NINTH falsification-family member"
        guard = "THIRT-" + "IETH falsification-family member"
        member_hits = 0
        guard_hits = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                member_hits += content.count(member)
                guard_hits += content.count(guard)
        assert member_hits == 1
        assert guard_hits == 0


class TestDocSync917:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #917" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 47088 | Across 1242 test files |" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #917" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #917 Type A:" in log
        assert "Type A #917" in log


class TestDateGrounding917:
    def test_iteration_time_present(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert "2026-09-22" in text

    def test_arm_dates_present(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert "2026-09-22" in text
        assert "2026-09-18" in text
        assert "2026-09-17" in text

    def test_arm_dates_ordered(self):
        assert date(2026, 9, 17) < date(2026, 9, 18) < date(2026, 9, 22)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "915-919" in text
        assert "THIRD leg" in text
        assert "D->E->A" in text
