"""Type A iteration 912: The Register x OpenAI Sep-17 six-incident adversarial
register vs The Register x Meta corpus-documented vocabulary arms (mechanism 778),
THIRD leg of the 910-914 rotation window (D->E->A).

Type A contract: add ONE mechanism block for a publication x competitor pair fresh
this run, with attribution URLs verified against a real search, and cross-reference
the existing comparator register. This run: The Register x OpenAI.

OpenAI arm (FRESH this run, excerpt-tier): The Register Sep 17 2026, "OpenAI admits
its agents went off the rails another six times"
(https://www.theregister.com/ai-and-ml/2026/09/17/openai-admits-its-agents-went-off-the-rails-another-six-times/5297016).
Six self-disclosed agent misalignment incidents. Dek: "Startup says it's learned
from these mistakes and that they shouldn't happen again ... which is just what
Zuck has said about 100 times" - the outlet drags Meta in as the habitual-apology
archetype WITHIN the OpenAI piece. "The details are unsettling." Register:
adversarial_snark. MANUAL ILLUSTRATIVE -0.30.

Meta arms (corpus-documented vocabulary-tier, fresh vocabulary-tier hand-scores
this run, NOT first-hand reads): Mar 5 2026 "Meta smart glasses face UK privacy
probe" ("privacy probe", "extremely private moments", "intimate footage") -0.35;
Jul 28 2026 "DEF CON bans Meta-style pervert glasses" -0.40; plus the within-piece
Sep-17 Zuck dek jab as register context (NOT a scored arm).

Illustrative delta (Meta minus OpenAI): -0.375 - (-0.30) = -0.075 - within-
publication NULL gradient. The real asymmetry scorer was run once on the two
illustrative arm arrays (asymmetry -0.075, t=0.0, p=1.0, d=-2.1213,
95% CI (-0.10, -0.05), engine is_significant False) as a corroborating observation -
NOT promoted to a finding. EXTENDS mechanism 757 (#877) cross-outlet divergence:
The Register is the fifth outlet on the Sep-17 disclosure peg, the hardest
adversarial pole; the softness ordering (WIRED briefed +0.15 carried; FT
licensing-deal neutral carried; TechCrunch/Ars/Register zero-tie adversarial)
aligns with the briefing/licensing structure. Zero-tie/zero-tie control: no mapped
Register-OpenAI or Register-Meta content-licensing deal (bounded absence).

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT promoted;
p_value, cohens_d, ci_95 NOT_CALCULATED at the finding layer; is_significant False;
NOT artifact-grade; NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 29). The null gradient
is incentive-consistent (no softness bought on either side) and WEAKENS
entity-specific readings of the outlet's OpenAI coverage: adversarial is the house
default. Correlation is not causation.

Research: pre-run browser.search candidate selection (Register OpenAI misalignment
SELECTED; Verge French-probe + OpenAI misalignment - no Verge arms after 4
exact/site queries; Guardian French-probe + OpenAI misalignment - no Guardian arms;
FT OpenAI funding/cash-burn REJECTED as duplicates of m718/m754; Rundown Luna
"less-creepy" REJECTED as thin non-profiled newsletter on an already-corpus Luna
story). REJECTED full-text: 0 browser.open per #503 (excerpt-tier). SELECTED:
Register Sep-17 six-incident piece (URL zero-hit repo-wide pre-commit; headline
phrase zero-hit; Zuck dek jab zero-hit). Novelty verified pre-commit (zero
test_type_a_912 files on disk; no "Type A #912" in git log; block key zero-hit
repo-wide; max numeric mechanism_id 777; zero underscore-form 778 keys by designed
keying per #715; zero dash-form 778 refs; zero numeric 778 keys in profiles/).

910-914 window THIRD leg D(#910)->E(#911)->A(#912). Next: #913 Type B.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_912_register_openai_six_incident_adversarial_vs_meta_vocabulary_arms_sep22_2am.py"
MECH_KEY = "register_openai_sep17_six_misalignment_adversarial_vs_meta_vocabulary_arms_sep22_2026"
MECH_KEY_PREFIX = "register_openai_sep17_six_misalignment_adversarial"
M_ID = 778
ITER = 912
TYPE_LETTER = "A"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 778 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_778"
NEXT_ID_MARKER = "mechanism" + "_779"
NEXT_ID_NUMERIC = "mechanism_id: " + "779"
NEXT_ID_DASH = "mechanism" + "-779"
MECH_NUMERIC = "mechanism_id: " + "778"

REGISTER_URL = "https://www.theregister.com/ai-and-ml/2026/09/17/openai-admits-its-agents-went-off-the-rails-another-six-times/5297016"
UK_PROBE_URL = "https://www.theregister.com/security/2026/03/05/meta-smart-glasses-face-uk-privacy-probe/5165427"
DEFCON_URL = "http://www.theregister.com/security/2026/07/28/def-con-bans-meta-style-pervert-glasses/5279763"

# Type A #912 is the THIRD leg of the 910-914 window: D(#910) -> E(#911) -> A(#912).
EXPECTED_ORDER = [("A", "912"), ("E", "911"), ("D", "910"), ("C", "909"), ("B", "908")]


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


class TestNovelty912:
    def test_single_test_type_a_912_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_912")]
        assert files == [OWN_BASENAME]

    def test_no_type_a_912_in_git_log_pre_commit(self):
        # Verified pre-commit by shell grep (no "Type A #912" in git log);
        # patched post-commit per the #565 followup convention to pin the
        # main commit as a singleton - no duplicate #912 main commit.
        proc = _git("log", "--format=%H %s", "--all")
        mains = [l for l in proc.stdout.splitlines()
                 if re.search(r"Type A #912: The Register x OpenAI", l)]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["research_method"]
        assert "zero test_type_a_912 files on disk pre-commit (glob)" in novelty
        assert "no 'Type A #912' in git log pre-commit" in novelty
        assert "block key zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 777 pre-commit" in novelty
        assert "zero underscore-form 778 mechanism key strings repo-wide pre-commit" in novelty

    def test_910_911_window_legs_present_prior_to_912(self):
        log = _read("iteration-log.md")
        assert "## #910 Type D:" in log
        assert "## #911 Type E:" in log
        idx_910 = log.index("## #910 Type D:")
        idx_911 = log.index("## #911 Type E:")
        assert idx_911 < idx_910

    def test_evidence_urls_documented_as_zero_hit_pre_commit(self):
        blk = _block()
        novelty = blk["research_method"]
        assert "The Register Sep-17 URL zero-hit repo-wide pre-commit" in novelty
        assert "'went off the rails another six times' zero-hit repo-wide pre-commit" in novelty
        assert "'just what Zuck has said about 100 times' zero-hit repo-wide pre-commit" in novelty


class TestRotationGuard912:
    # Two of five rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_910_914_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("908", "909", "910", "911", "912"):
                # Followups and test-fixups are not rotation legs.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C", "B"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"

    def test_predecessor_is_type_e_911(self):
        proc = _git("log", "--oneline", "--grep", "Type E #911", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_type_a_912_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #912")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #912(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor912:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("register_openai_sep17")
        assert "six_misalignment_adversarial" in MECH_KEY

    def test_mech_key_ends_with_arms(self):
        assert MECH_KEY.endswith("vs_meta_vocabulary_arms_sep22_2026")


class TestMechanism778Structure:
    def test_block_present_under_cross_publication_findings(self):
        doc = yaml.safe_load(_read("profiles/competitor-coverage-research.yaml"))
        assert MECH_KEY in doc["cross_publication_findings"]

    def test_mechanism_id_numeric(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 778

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 912
        assert blk["rotation_type"] == TYPE_LETTER == "A"
        assert blk["discovery_date"] == "2026-09-22"
        assert blk["finding_type"] == "cross_publication_coverage_asymmetry"
        assert blk["publication"] == "The Register"
        assert blk["competitor"] == "OpenAI"
        assert blk["comparator_entity"] == "Meta"

    def test_block_key_unique_in_yaml(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(MECH_KEY) == 1

    def test_no_next_id_779_keys(self):
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


class TestMechanism778OpenAIFreshArm:
    def _arm(self):
        return _block()["openai_arms"][0]

    def test_sep17_piece_title(self):
        assert self._arm()["piece"] == "OpenAI admits its agents went off the rails another six times"

    def test_sep17_date(self):
        assert self._arm()["date"] == "2026-09-17"

    def test_sep17_register_adversarial_snark(self):
        assert self._arm()["register"] == "adversarial_snark"

    def test_sep17_tone_minus_030(self):
        assert self._arm()["tone_illustrative"] == pytest.approx(-0.30)

    def test_sep17_url_verbatim(self):
        assert self._arm()["source_url"] == REGISTER_URL

    def test_sep17_key_quotes(self):
        quotes = " ".join(self._arm()["key_language"])
        assert "went off the rails another six times" in quotes
        assert "just what Zuck has said about 100 times" in quotes
        assert "The details are unsettling." in quotes

    def test_sep17_excerpt_tier(self):
        assert "excerpt_tier" in self._arm()["evidence_tier"]
        assert "0 browser.open per #503" in self._arm()["tone_basis"]


class TestMechanism778MetaArms:
    def _arms(self):
        return _block()["meta_arms"]

    def test_two_scored_meta_arms(self):
        scored = [a for a in self._arms() if a.get("scored_arm", True)]
        assert len(scored) == 2

    def test_uk_probe_arm(self):
        arm = self._arms()[0]
        assert arm["piece"] == "Meta smart glasses face UK privacy probe"
        assert arm["date"] == "2026-03-05"
        assert arm["tone_illustrative"] == pytest.approx(-0.35)
        assert arm["carried_from"].endswith(UK_PROBE_URL.split("theregister.com")[1]) or UK_PROBE_URL in arm["carried_from"]

    def test_uk_probe_vocabulary(self):
        quotes = " ".join(self._arms()[0]["key_language"])
        assert "privacy probe" in quotes
        assert "extremely private moments" in quotes
        assert "intimate footage" in quotes

    def test_defcon_arm(self):
        arm = self._arms()[1]
        assert arm["piece"] == "DEF CON bans Meta-style pervert glasses"
        assert arm["date"] == "2026-07-28"
        assert arm["tone_illustrative"] == pytest.approx(-0.40)
        assert DEFCON_URL in arm["carried_from"]

    def test_within_piece_jab_not_scored(self):
        jab = self._arms()[2]
        assert jab["scored_arm"] is False
        assert jab["tone_illustrative"] is None
        assert "just what Zuck has said about 100 times" in " ".join(jab["key_language"])

    def test_meta_arms_vocabulary_tier_basis(self):
        for arm in self._arms()[:2]:
            assert "vocabulary-tier" in arm["tone_basis"]
            assert "not a first-hand read" in arm["tone_basis"]


class TestMechanism778Scorer:
    def _scorer(self):
        return _block()["asymmetry_scorer"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["meta_arm_tones"] == pytest.approx([-0.35, -0.40])
        assert s["openai_arm_tones"] == pytest.approx([-0.30])

    def test_avgs(self):
        s = self._scorer()
        assert s["meta_arm_avg"] == pytest.approx(-0.375)
        assert s["openai_arm_avg"] == pytest.approx(-0.30)

    def test_delta_meta_minus_openai(self):
        s = self._scorer()
        assert s["illustrative_delta_meta_minus_openai"] == pytest.approx(-0.075, abs=1e-4)

    def test_delta_arithmetic_logged(self):
        s = self._scorer()
        assert s["delta_calc"] == "((-0.35 + -0.40) / 2) - (-0.30) = -0.375 - (-0.30) = -0.075"

    def test_null_gradient_interpretation(self):
        s = self._scorer()
        assert "NULL gradient" in s["delta_interpretation"]
        assert "statistically silent" in s["delta_interpretation"]

    def test_engine_run_once_corroboration(self):
        e = self._scorer()["engine_run"]
        assert e["asymmetry_score"] == pytest.approx(-0.075)
        assert e["t_statistic"] == pytest.approx(0.0)
        assert e["p_value"] == pytest.approx(1.0)
        assert e["cohens_d"] == pytest.approx(-2.1213, abs=1e-4)
        assert e["ci_95"] == pytest.approx([-0.10, -0.05])
        assert e["engine_is_significant"] is False
        assert "NOT promoted to a finding" in e["role"]

    def test_finding_layer_not_calculated(self):
        s = self._scorer()
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_small_n_per_arm"


class TestMechanism778Discipline:
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
        assert any("house snark" in c for c in conf)
        assert any("Temporal skew" in c for c in conf)

    def test_counterevidence_four(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 4
        assert all(c.startswith("COUNTEREVIDENCE") for c in ce)
        assert any("Zuck dek jab" in c for c in ce)
        assert any("Bloomberg null-gradient precedent" in c for c in ce)

    def test_connects_to(self):
        assert _block()["connects_to"] == [757, 760, 712, 158, 775]

    def test_financial_context_zero_tie(self):
        fc = _block()["financial_context"]
        assert "bounded absence" in fc["register_openai_content_deal"]
        assert "bounded absence" in fc["register_meta_content_deal"]
        assert fc["prediction"].startswith("Zero-tie/zero-tie control")

    def test_correlation_not_causation_in_finding(self):
        assert "Correlation is not causation" in _block()["finding"]

    def test_ascii_only_no_em_dashes(self):
        # Serialize only the parsed m778 block (per _block), so unrelated
        # pre-existing content elsewhere in the yaml is not measured.
        seg = yaml.safe_dump(_block(), allow_unicode=True, sort_keys=False)
        assert "\u2014" not in seg
        assert all(ord(ch) < 128 for ch in seg)


class TestNoCrossContamination912:
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

    def test_no_underscore_form_778_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_778_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_778(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 778

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


class TestDocSync912:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #912" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 46781 |" in readme
        assert "Across 1237 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #912" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #912 Type A:" in log
        assert "Type A #912" in log


class TestDateGrounding912:
    def test_iteration_time_present(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert "2026-09-22" in text

    def test_arm_dates_present(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert "2026-09-17" in text
        assert "2026-03-05" in text
        assert "2026-07-28" in text

    def test_arm_dates_ordered(self):
        assert date(2026, 3, 5) < date(2026, 7, 28) < date(2026, 9, 17) < date(2026, 9, 22)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "910-914" in text
        assert "THIRD leg" in text
        assert "D->E->A" in text
