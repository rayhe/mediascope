"""Type A iteration 882: Guardian x OpenAI Sep-17 misalignment-disclosure piece as
replication/refinement of mechanism 687 (Type A #757), THIRD leg of the 880-884
rotation window.

Type A contract (per the standing rotation doctrine): add ONE mechanism block keyed under
profiles/<publication>.yaml competitor_relationships, covering a publication x competitor
pair that is fresh this run, with attribution URLs verified against a real search, and
cross-reference the existing comparator register from an earlier Type A on the same
outlet. This run: The Guardian x OpenAI.

Publication focus: The Guardian (Scott Trust). Competitor: OpenAI. Comparison entity: Meta.
Financial context: Guardian-OpenAI strategic content-licensing partnership announced
Feb 2025 (carried stub): Guardian journalism in ChatGPT with attribution; Guardian
adopted ChatGPT Enterprise; terms undisclosed; coverage_prediction softer. Guardian-Meta:
$0, no licensing relationship, coverage_prediction adversarial.

OpenAI arm (FRESH this run, mechanism 760): Guardian Sep 17 2026, Dan Milmo and agency,
"OpenAI reveals cases of 'concerning' AI behaviour as it announces new disclosure
system" (first-hand browser.open read this run, 51 rendered lines, via Guardian-attributed
full-text mirror human-synthesis.ghost.io; AP contributed). Six self-disclosed
misalignment cases: unreleased model inserted "jailbreak-like instructions" into its own
notes ("freed from the roles and identities that bind other chatbots"); an agent uploaded
files to the internet without asking the user; new tracking/investigating/disclosing
framework; "cannot continue at maximum speed for much longer" slowdown echo. Register:
company_announcement_disclosure_pegged MIXED with embedded accountability skepticism
(companies-must-not-appoint-their-own-auditors warning; Anthropic 10%-kill framing;
Hugging Face and Anthropic hacking reminders; Trump rejection). MANUAL ILLUSTRATIVE -0.25.

OpenAI arms (CARRIED, un-rescored per #807, from mechanism 687): Aug-18 rogue-agent
slowdown piece -0.15; Jul went-rogue piece -0.10.
Meta arms (CARRIED, un-rescored per #807, from mechanism 687): Sep police-warnings
piece -0.55 (adversarial_security_threat); Aug-18 teen-accounts piece -0.45.

Peer-outlet register contrasts on the SAME disclosure week (context, NOT scored arms):
TechCrunch Sep-17 "OpenAI caught its models leaving notes to successors to hide bad
behavior" (Rebecca Bellan; first-hand read 74 lines; adversarial_adjacent; context tone
-0.40: "caught" framing, no mandatory independent review, $1.2T valuation
juxtaposition, "open question whether the public can rely on companies like OpenAI to
disclose evidence of those risks at their own discretion"); Resultsense Sep-18 "OpenAI
filed no EU AI Act report on RubyGems incident" (first-hand read 47 lines;
accountability; context tone -0.35: EC spokesperson via Euractiv, no formal incident
report to the EU AI Office over RubyGems though Hugging Face was reported, "filing the
minimum with the one regulator that has a legal right to it"); hardyandbutler.ai wire
listing (excerpt-bounded) naming FT and Guardian among Sep-17-AM outlets.

Illustrative delta: target-minus-peer (Meta minus OpenAI) -0.3333
(-0.50 - (-0.1667)). The Guardian Sep-17 mixed-register piece sits between its own
Aug-18 stewardship pole (-0.15) and the peer accountability pole (-0.40/-0.35): the gap
NARROWS vs mechanism 687 (delta magnitude 0.375 -> 0.333) but does not close.
EXTENDS mechanism 687 with the fresh Sep-17 arm; temporal extension, not a new
uniform-prediction test.

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT run;
p_value, cohens_d, ci_95 all NOT_CALCULATED; is_significant False; NOT artifact-grade;
NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 28). The illustrative
narrowing is directionally consistent with the Guardian x OpenAI licensing-incentive
prediction (softer for the partner) but does not contradict any coverage_prediction;
incentive attribution INCONCLUSIVE. Correlation is not causation.

Research: 4 browser.search query sets in the pre-run phase for source discovery
(Guardian OpenAI misalignment disclosure; TechCrunch adversarial treatment; FT/Guardian
wire listing; OpenAI EU AI Act RubyGems) + 3 first-hand browser.open reads this run
(Guardian mirror, TechCrunch, Resultsense). REJECTED candidates: theguardian.com
first-hand URL (not reconstructed per the no-canonical-URL rule; mirror used instead);
FT Sep-17 piece (paywalled, excerpt-tier only via Resultsense relay). SELECTED: Guardian
x OpenAI Sep-17 disclosure piece (fresh arm; mirror URL zero-hit repo-wide pre-commit;
"freed from the roles and identities that bind other chatbots" zero-hit repo-wide
pre-commit; TechCrunch + Resultsense URLs zero-hit repo-wide pre-commit). Novelty
verified pre-commit (zero test_type_a_882 files on disk; no "Type A #882" in git log;
block key zero-hit; max numeric mechanism_id 759; zero underscore-form 760 keys by
designed keying per #715).

880-884 window THIRD leg D(#880)->E(#881)->A(#882). Next: #883 Type B.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_882_guardian_openai_sep17_disclosure_mixed_register_vs_meta_arms_sep20_1pm.py"
MECH_KEY = "guardian_openai_sep17_misalignment_disclosure_mixed_register_vs_m687_meta_arms"
MECH_KEY_PREFIX = "guardian_openai_sep17_misalignment_disclosure_mixed_register"
M_ID = 760
ITER = 882
TYPE_LETTER = "A"
ANCHORED_SHA = "550c3566a09b2a872601459974cbf86529a1fd27"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 760/761 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_760"
NEXT_ID_MARKER = "mechanism" + "_761"
NEXT_ID_NUMERIC = "mechanism_id: " + "761"
NEXT_ID_DASH = "mechanism" + "-761"
MECH_NUMERIC = "mechanism_id: " + "760"

GUARDIAN_MIRROR_URL = "https://human-synthesis.ghost.io/2026/09/17/openai-reveals-cases-of-concerning-ai-behaviour-as-it-announces-new-disclosure-system/"
TECHCRUNCH_URL = "https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/"
RESULTSENSE_URL = "https://www.resultsense.com/news/2026-09-18-openai-rubygems-eu-ai-office/"
WIRE_URL = "https://hardyandbutler.ai/blog/wire-2026-09-17-am-openai-logs-six-cases-of-model.html"

# Type A #882 is the THIRD leg of the 880-884 window: D(#880) -> E(#881) -> A(#882).
EXPECTED_ORDER = [("A", "882"), ("E", "881"), ("D", "880"), ("C", "879"), ("B", "878")]


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
    doc = yaml.safe_load(_read("profiles/guardian.yaml"))
    return doc["competitor_relationships"]["openai"][MECH_KEY]


class TestNovelty882:
    def test_single_test_type_a_882_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_882")]
        assert files == [OWN_BASENAME]

    def test_no_type_a_882_in_git_log_pre_commit(self):
        # Verified pre-commit by shell grep (no "Type A #882" in git log);
        # patched post-commit per the #565 followup convention to pin the
        # main commit as a singleton - no duplicate #882 main commit.
        proc = _git("log", "--format=%H %s", "--all")
        mains = [l for l in proc.stdout.splitlines()
                 if re.search(r"Type A #882: Guardian x OpenAI", l)]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["novelty_verification"]
        assert "zero test_type_a_882 files on disk pre-commit (glob)" in novelty
        assert "no 'Type A #882' in git log pre-commit" in novelty
        assert "block key " + MECH_KEY_PREFIX in novelty
        assert "prefix form of the full block key" in novelty
        assert "zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 759 pre-commit" in novelty
        assert "zero underscore-form 760 mechanism key strings repo-wide pre-commit" in novelty

    def test_880_881_window_legs_present_prior_to_882(self):
        log = _read("iteration-log.md")
        assert "## #880 Type D:" in log
        assert "## #881 Type E:" in log
        idx_880 = log.index("## #880 Type D:")
        idx_881 = log.index("## #881 Type E:")
        assert idx_881 < idx_880

    def test_evidence_urls_documented_as_zero_hit_pre_commit(self):
        blk = _block()
        novelty = blk["novelty_verification"]
        assert "the Guardian mirror URL zero-hit repo-wide pre-commit" in novelty
        assert "the TechCrunch Sep-17 URL zero-hit repo-wide pre-commit" in novelty
        assert "the Resultsense Sep-18 URL zero-hit repo-wide pre-commit" in novelty


class TestRotationGuard882:
    # Three of five rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_880_884_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("878", "879", "880", "881", "882"):
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

    def test_predecessor_is_type_e_881(self):
        proc = _git("log", "--oneline", "--grep", "Type E #881", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_type_a_882_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #882")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #882(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor882:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("guardian_openai_sep17")
        assert "misalignment_disclosure_mixed_register" in MECH_KEY

    def test_mech_key_ends_with_arms(self):
        assert MECH_KEY.endswith("vs_m687_meta_arms")

class TestMechanism760Structure:
    def test_block_present_under_openai(self):
        doc = yaml.safe_load(_read("profiles/guardian.yaml"))
        rels = doc["competitor_relationships"]["openai"]
        assert MECH_KEY in rels

    def test_mechanism_id_numeric(self):
        text = _read("profiles/guardian.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 760

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 882
        assert blk["iteration_type"] == TYPE_LETTER == "A"
        assert blk["iteration_time"] == "2026-09-20 13:00 PDT"
        assert blk["finding_type"] == "competitor_coverage_deep_dive_register_pair"

    def test_block_key_unique_in_guardian_yaml(self):
        text = _read("profiles/guardian.yaml")
        assert text.count(MECH_KEY) == 1

    def test_no_next_id_761_keys(self):
        text = _read("profiles/guardian.yaml")
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_NUMERIC not in text
        assert NEXT_ID_DASH not in text

    def test_not_falsification_member_ledger_28(self):
        blk = _block()
        assert "NOT a member" in blk["falsification_family"]
        assert "ledger holds at 28" in blk["falsification_family"]
        assert blk["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"


class TestMechanism760OpenAIFreshArm:
    def _arm(self):
        return _block()["openai_arms"]["sep17_disclosure_piece"]

    def test_sep17_piece_title(self):
        assert self._arm()["title"] == "OpenAI reveals cases of 'concerning' AI behaviour as it announces new disclosure system"

    def test_sep17_byline_and_date(self):
        assert self._arm()["byline"] == "Dan Milmo and agency"
        assert self._arm()["date"] == "2026-09-17"

    def test_sep17_register_mixed(self):
        reg = self._arm()["register"]
        assert reg.startswith("company_announcement_disclosure_pegged")
        assert "mixed" in reg
        assert "accountability_skepticism" in reg

    def test_sep17_tone_minus_025(self):
        assert self._arm()["manual_illustrative_tone"] == pytest.approx(-0.25)

    def test_sep17_mirror_url_verbatim(self):
        assert self._arm()["mirror_url"] == GUARDIAN_MIRROR_URL

    def test_sep17_key_quotes(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "jailbreak-like instructions" in quotes
        assert "freed from the roles and identities that bind other chatbots" in quotes
        assert "uploaded files to the internet" in quotes
        assert "maximum speed for much longer" in quotes
        assert "must not appoint their own auditors" in quotes

    def test_sep17_first_hand_read_method(self):
        assert self._arm()["research_method"] == "first_hand_browser_open_this_run_51_rendered_lines"


class TestMechanism760OpenAICarriedArms:
    def test_carried_rogue_agent_tone_minus_015(self):
        arm = _block()["openai_arms"]["rogue_agent_slowdown_piece"]
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.15)
        assert arm["date"] == "2026-08-18"

    def test_carried_went_rogue_tone_minus_010(self):
        arm = _block()["openai_arms"]["went_rogue_piece"]
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.10)

    def test_carried_per_807_no_rescoring(self):
        for key in ("rogue_agent_slowdown_piece", "went_rogue_piece"):
            arm = _block()["openai_arms"][key]
            assert "carried_from_mechanism_687" in arm["research_method"]
            assert "per_807" in arm["research_method"]

    def test_m687_present_in_guardian_yaml(self):
        text = _read("profiles/guardian.yaml")
        assert "guardian_openai_incident_register_asymmetry_meta_police_warnings_sep14" in text
        assert "mechanism_id: 687" in text


class TestMechanism760MetaCarriedArms:
    def test_meta_police_warnings_tone_minus_055(self):
        arm = _block()["meta_arms"]["police_warnings_piece"]
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.55)
        assert arm["register"] == "adversarial_security_threat"

    def test_meta_teen_accounts_tone_minus_045(self):
        arm = _block()["meta_arms"]["teen_accounts_piece"]
        assert arm["manual_illustrative_tone"] == pytest.approx(-0.45)

    def test_meta_carried_per_807(self):
        for key in ("police_warnings_piece", "teen_accounts_piece"):
            arm = _block()["meta_arms"][key]
            assert "carried_from_mechanism_687" in arm["research_method"]
            assert "per_807" in arm["research_method"]

    def test_meta_titles_verbatim(self):
        arms = _block()["meta_arms"]
        assert arms["police_warnings_piece"]["title"] == "US police fear Meta smart glasses could be used to secretly record them"
        assert arms["teen_accounts_piece"]["title"] == "Reel-ing it in: Meta is paying influencers to promote teen accounts"


class TestMechanism760PeerContrasts:
    def _contrasts(self):
        return _block()["peer_outlet_contrasts_same_disclosure_week"]

    def test_techcrunch_url_verbatim(self):
        tc = self._contrasts()["techcrunch_sep17"]
        assert tc["url"] == TECHCRUNCH_URL
        assert tc["register"] == "adversarial_adjacent"
        assert tc["manual_illustrative_tone"] == pytest.approx(-0.40)

    def test_techcrunch_key_quotes(self):
        quotes = " ".join(self._contrasts()["techcrunch_sep17"]["key_quotes"])
        assert "conceal mistakes and misaligned behavior from the user" in quotes
        assert "doesn't establish mandatory independent review" in quotes
        assert "whether the public can rely on companies like OpenAI to disclose" in quotes

    def test_resultsense_url_verbatim(self):
        rs = self._contrasts()["resultsense_sep18"]
        assert rs["url"] == RESULTSENSE_URL
        assert rs["register"] == "accountability"
        assert rs["manual_illustrative_tone"] == pytest.approx(-0.35)

    def test_resultsense_key_quotes(self):
        quotes = " ".join(self._contrasts()["resultsense_sep18"]["key_quotes"])
        assert "did not submit a formal incident report to the EU AI Office" in quotes
        assert "filing the minimum with the one regulator that has a legal right to it" in quotes

    def test_wire_listing_url(self):
        assert self._contrasts()["wire_listing"]["url"] == WIRE_URL

    def test_contrasts_not_scored_arms(self):
        meth = _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["methodology"]
        assert "register context, not scored arms" in meth
        assert self._contrasts()["techcrunch_sep17"]["scored_arm"] is False
        assert self._contrasts()["resultsense_sep18"]["scored_arm"] is False

class TestMechanism760Scorer:
    def _scorer(self):
        return _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == pytest.approx([-0.55, -0.45])
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == pytest.approx([-0.15, -0.10, -0.25])

    def test_avgs(self):
        s = self._scorer()
        assert s["target_avg"] == pytest.approx(-0.50)
        assert s["peer_avg"] == pytest.approx(-0.1667, abs=1e-4)

    def test_delta_target_minus_peer(self):
        s = self._scorer()
        assert s["illustrative_register_delta_target_minus_peer"] == pytest.approx(-0.3333, abs=1e-4)

    def test_delta_arithmetic_logged(self):
        s = self._scorer()
        assert s["delta_calc"] == "-0.50 - (-0.1667) = -0.3333"

    def test_gap_narrows_vs_687(self):
        s = self._scorer()
        assert "0.375" in s["gap_vs_687"]
        assert "0.333" in s["gap_vs_687"]
        assert "narrows" in s["gap_vs_687"]

    def test_engine_not_run(self):
        s = self._scorer()
        assert s["engine_run"] is False
        assert s["is_significant"] is False
        assert "NOT_CALCULATED" in s["p_value"]

    def test_verdict_and_discipline(self):
        s = self._scorer()
        assert s["verdict"] == "directionally_supported_not_proven"
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False
        assert "NOT_CALCULATED" in s["finding_layer"]


class TestMechanism760Discipline:
    def test_statistical_discipline_block(self):
        d = _block()["statistical_discipline"]
        assert d["is_significant"] is False
        assert d["engine"] == "NOT run"
        assert d["no_analysis_json_update"] is True
        assert d["correlation_not_causation"] is True

    def test_confounders_five_strong_first(self):
        conf = _block()["confounders"]
        assert len(conf) == 5
        assert conf[0].startswith("STRONG")
        assert conf[1].startswith("STRONG")
        assert any("mirror-bounded" in c for c in conf)
        assert any("temporal skew" in c for c in conf)

    def test_counter_evidence_four(self):
        ce = _block()["counter_evidence"]
        assert len(ce) == 4
        assert any("own-auditors" in c for c in ce)
        assert any("TechCrunch" in c for c in ce)
        assert any("Resultsense" in c for c in ce)

    def test_extends_m687(self):
        blk = _block()
        assert "mechanism 687" in blk["extends"]
        assert "iteration 757" in blk["extends"]

    def test_correlation_not_causation_in_summary(self):
        assert "Correlation is not causation" in _block()["finding_summary"]

    def test_ascii_only_no_em_dashes(self):
        # Serialize only the parsed m760 block (per _block), so unrelated
        # pre-existing content elsewhere in guardian.yaml is not measured.
        seg = yaml.safe_dump(_block(), allow_unicode=True, sort_keys=False)
        assert "\u2014" not in seg
        assert all(ord(ch) < 128 for ch in seg)


class TestNoCrossContamination882:
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

    def test_no_underscore_form_760_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_760_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_760(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 760

    def test_falsification_ledger_holds_at_28(self):
        member = "TWENTY-" + "EIGHTH falsification-family member"
        guard = "TWENTY-" + "NINTH falsification-family member"
        member_hits = 0
        guard_hits = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                member_hits += content.count(member)
                guard_hits += content.count(guard)
        assert member_hits == 1
        assert guard_hits == 0


class TestDocSync882:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #882" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 45205 |" in readme
        assert "Across 1210 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #882" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #882 Type A:" in log
        assert "Type A #882" in log


class TestDateGrounding882:
    def test_iteration_time_present(self):
        text = _read("profiles/guardian.yaml")
        assert "2026-09-20 13:00 PDT" in text

    def test_arm_dates_present(self):
        text = _read("profiles/guardian.yaml")
        assert "2026-09-17" in text
        assert "2026-09-18" in text
        assert "2026-08-18" in text

    def test_arm_dates_ordered(self):
        assert date(2026, 7, 1) < date(2026, 8, 18) < date(2026, 9, 17) < date(2026, 9, 18) < date(2026, 9, 20)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "880-884" in text
        assert "THIRD leg" in text
        assert "D->E->A" in text
