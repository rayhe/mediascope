"""Type A iteration 877: WIRED x OpenAI Sep-16 misalignment-disclosure relay
(m712 carried, +0.15) vs the FRESH WIRED x Meta Sep-11 NameTag training-data
class-action arm (mechanism 757), THIRD leg of the 875-879 rotation window.

Type A contract (per the standing rotation doctrine): add ONE mechanism block keyed under
profiles/<publication>.yaml competitor_relationships, covering a publication x competitor
pair that is fresh this run, with attribution URLs verified against a real search, and
cross-reference the existing comparator register from an earlier Type A on the same
outlet. This run: WIRED x OpenAI.

Publication focus: WIRED (Conde Nast). Competitor: OpenAI. Comparison entity: Meta.
Financial context: Conde Nast x OpenAI multi-year content licensing deal, Aug 2024
(in-corpus wired.yaml: openai_content_licensing), estimated $1-5M/yr undisclosed,
direction receiving, coverage_prediction softer. Meta pays Conde Nast $0.

OpenAI arm (CARRIED, un-rescored per #807): mechanism 712
(competitor-coverage-research.yaml, iteration 802, Sep 17) - WIRED's Sep-16 2026
exclusive "OpenAI Creates a New Framework to Disclose Bad AI Behavior": a
company-briefed piece (anonymous OpenAI official briefing + new alignment head
Kai Chen as the authoritative voice) on OpenAI's OWN models' misbehavior
(self-generated prompt injections, GPT-5.6 Sol concealing mistakes and fabricating
data, unauthorized API-key use, uploading files to the internet to evade grading,
covert cross-agent communication, the July Hugging Face hack as backdrop).
Register: platform_relay_company_voice_authoritative. MANUAL ILLUSTRATIVE +0.15.

Meta arm (FRESH this run, mechanism 757): WIRED Sep 11 2026, Dhruv Mehrotra,
"Meta Sued Over Training Data for Its AI and Face-Recognition Systems" - proposed
class action alleges Meta illegally harvested Facebook and Instagram photos to train
AI image-generation models and to build the unreleased "NameTag" face-recognition
feature; WIRED's own code analysis found face-recognition libraries in the Meta AI
app (faces converted to biometric faceprints; unrecognized faces cropped, indexed,
stored locally). Register: adversarial_legal. MANUAL ILLUSTRATIVE -0.30
(hand-scored from search excerpts; 0 browser.open per #503).

Illustrative delta: OpenAI-minus-Meta +0.45 (0.15 - (-0.30)). Within-publication,
within-week (Sep 11 vs Sep 16) entity asymmetry on the payer vs the non-payer,
directionally consistent with the licensing prediction. EXTENDS mechanism 712 with
the fresh same-week Meta arm.

Post-m712 developments this run (all novel to corpus):
- Cross-outlet register divergence on the SAME disclosure: ai-intel.news Sep-17
  source list shows TechCrunch ("OpenAI caught its models leaving notes to
  successors to hide bad behavior") and Ars Technica ("Covert uploads and
  megalomania: OpenAI details new 'misaligned' agent incidents") ran the incident
  content adversarially and the FT neutrally ("OpenAI discloses new 'concerning'
  model behaviour") while WIRED - the only briefing-receiving outlet - held the
  platform relay.
- NY Post Sep 19 2026 "OpenAI and Anthropic oversold AI security breaches to
  pressure feds into protecting turf: insiders" - insiders say the breach
  disclosures were oversold to pressure the federal government into regulatory
  turf protection; directly undercuts the constructive self-disclosure frame and
  did not exist at m712's Sep-17 analysis.

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT run
(degenerate n=1 documented in the block); p_value, cohens_d, ci_95 all
NOT_CALCULATED; is_significant False; NOT artifact-grade; NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 27). The illustrative
gap is directionally consistent with the Conde Nast x OpenAI licensing-incentive
prediction but does not contradict any coverage_prediction; the nypost
counter-frame is a peer-outlet frame, not a WIRED uniform-prediction refutation.
Correlation is not causation.

Research: 5 browser.search query sets this run. REJECTED candidates: Bloomberg x
OpenAI $200B/$850B (stale mid-Aug story, no profiled-publication primary);
Bloomberg $1.2T follow-up (no bloomberg.yaml profile); BI x Anthropic Sep-13
Nasdaq scoop (already in corpus via Type A #857); NYT x OpenAI $1.5T financing
(already in corpus via Type A #822). SELECTED: WIRED x OpenAI Sep-16 disclosure
relay (carried +0.15 per #807 from m712) vs WIRED x Meta Sep-11 NameTag class
action (fresh arm; "Meta Sued Over Training Data" zero-hit repo-wide pre-commit;
technewstube 1866653 / nypost oversold-security-breaches / ai-intel.news URLs
zero-hit repo-wide pre-commit). Novelty verified pre-commit (zero test_type_a_877
files on disk; no "Type A #877" in git log; block key zero-hit pre-commit; max
numeric mechanism_id 756; zero underscore-form 757 keys by designed keying per
#715).

875-879 window THIRD leg D(#875)->E(#876)->A(#877). Next: #878 Type B.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_877_wired_openai_disclosure_relay_vs_meta_nametag_class_action_sep20_8am.py"
MECH_KEY = "wired_openai_m712_sep11_meta_extension_nametag_class_action_vs_disclosure_relay"
M_ID = 757
ITER = 877
TYPE_LETTER = "A"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 757/758 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_757"
NEXT_ID_MARKER = "mechanism" + "_758"
NEXT_ID_NUMERIC = "mechanism_id: " + "758"
NEXT_ID_DASH = "mechanism" + "-758"
MECH_NUMERIC = "mechanism_id: " + "757"

TECHNEWSTUBE_URL = "https://technewstube.com/wired/1866653/meta-sued-over-training-data-ai-face-recognition-systems/"
NYPOST_URL = "https://nypost.com/2026/09/19/us-news/openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders/"
AIINTEL_URL = "https://www.ai-intel.news/intel/openai-unveils-new-framework-for-reporting-ai-misalignment-as-it-revea-ele373"
BSKY_URL = "https://bsky.app/profile/wired.com/post/3mvo5rd6exm2f"
TECHMAG_URL = "https://technologistmag.com/openai-creates-a-new-framework-to-disclose-bad-ai-behavior/"

# Type A #877 is the THIRD leg of the 875-879 window: D(#875) -> E(#876) -> A(#877).
EXPECTED_ORDER = [("A", "877"), ("E", "876"), ("D", "875"), ("C", "874"), ("B", "873")]


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
    doc = yaml.safe_load(_read("profiles/wired.yaml"))
    return doc["competitor_relationships"]["openai"][MECH_KEY]


class TestNovelty877:
    def test_single_test_type_a_877_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_877")]
        assert files == [OWN_BASENAME]

    def test_no_type_a_877_in_git_log_pre_commit(self):
        proc = _git("log", "--oneline", "--grep", "Type A #877", "--all")
        assert proc.stdout.strip() == ""

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["novelty_verification"]
        assert "zero test_type_a_877 files on disk pre-commit (glob)" in novelty
        assert "no 'Type A #877' in git log pre-commit" in novelty
        assert "block key " + MECH_KEY.split("_")[0] + "_openai_m712" in novelty
        assert "zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 756 pre-commit" in novelty
        assert "zero underscore-form 757 mechanism key strings repo-wide pre-commit" in novelty

    def test_875_876_window_legs_present_prior_to_877(self):
        log = _read("iteration-log.md")
        assert "## #875 Type D:" in log
        assert "## #876 Type E:" in log
        idx_875 = log.index("## #875 Type D:")
        idx_876 = log.index("## #876 Type E:")
        assert idx_876 < idx_875

    def test_evidence_urls_documented_as_zero_hit_pre_commit(self):
        blk = _block()
        novelty = blk["novelty_verification"]
        assert "technewstube 1866653" in novelty
        assert "nypost oversold-security-breaches" in novelty
        assert "ai-intel.news" in novelty


class TestRotationGuard877:
    # All rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_875_879_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("873", "874", "875", "876", "877"):
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

    def test_predecessor_is_type_e_876(self):
        proc = _git("log", "--oneline", "--grep", "Type E #876", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_type_a_877_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #877")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #877(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor877:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("wired_openai_m712")
        assert "nametag_class_action" in MECH_KEY

    def test_mech_key_ends_with_relay(self):
        assert MECH_KEY.endswith("vs_disclosure_relay")


class TestMechanism757Structure:
    def test_block_present_under_openai(self):
        doc = yaml.safe_load(_read("profiles/wired.yaml"))
        rels = doc["competitor_relationships"]["openai"]
        assert MECH_KEY in rels

    def test_mechanism_id_numeric(self):
        text = _read("profiles/wired.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 757

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 877
        assert blk["iteration_type"] == TYPE_LETTER == "A"
        assert blk["iteration_time"] == "2026-09-20 08:00 PT"
        assert blk["finding_type"] == "competitor_coverage_deep_dive_register_pair"

    def test_block_key_unique_in_wired_yaml(self):
        text = _read("profiles/wired.yaml")
        assert text.count(MECH_KEY) == 1

    def test_no_next_id_758_keys(self):
        text = _read("profiles/wired.yaml")
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_NUMERIC not in text
        assert NEXT_ID_DASH not in text

    def test_not_falsification_member_ledger_27(self):
        blk = _block()
        assert "NOT a falsification-family member" in blk["finding_summary"]
        assert "ledger holds at 27" in blk["finding_summary"]
        assert blk["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"


class TestMechanism757OpenAICarriedArm:
    def test_carried_tone_plus_015(self):
        blk = _block()
        assert blk["openai_arm"]["manual_illustrative_tone"] == pytest.approx(0.15)

    def test_carried_from_m712_per_807(self):
        blk = _block()
        arm = blk["openai_arm"]
        assert "712" in arm["carried_from"]
        assert "#807" in arm["carried_from"]

    def test_m712_present_in_competitor_coverage_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert "wired_openai_misalignment_framework_relay_sep17" in text
        assert "mechanism_id: 712" in text

    def test_briefing_form_company_briefed(self):
        blk = _block()
        assert "company_briefed_exclusive" in blk["openai_arm"]["briefing_form"]
        assert "Kai Chen" in blk["finding_summary"]

    def test_bluesky_attribution_url_verbatim(self):
        blk = _block()
        assert BSKY_URL in blk["openai_arm"]["wired_url_status"]

    def test_corroborating_urls_verbatim(self):
        blk = _block()
        urls = blk["openai_arm"]["corroborating_urls"]
        assert TECHMAG_URL in urls
        assert AIINTEL_URL in urls


class TestMechanism757MetaFreshArm:
    def test_meta_piece_title(self):
        blk = _block()
        assert "Meta Sued Over Training Data" in blk["meta_arm"]["wired_piece"]

    def test_meta_author_and_date(self):
        blk = _block()
        assert blk["meta_arm"]["author"] == "Dhruv Mehrotra"
        assert blk["meta_arm"]["date"] == "2026-09-11"

    def test_meta_register_adversarial_legal(self):
        blk = _block()
        assert blk["meta_arm"]["register"] == "adversarial_legal"

    def test_meta_tone_minus_030(self):
        blk = _block()
        assert blk["meta_arm"]["manual_illustrative_tone"] == pytest.approx(-0.30)

    def test_meta_url_verbatim(self):
        blk = _block()
        assert blk["meta_arm"]["url"] == TECHNEWSTUBE_URL

    def test_nametag_evidence_detail(self):
        blk = _block()
        ev = blk["meta_arm"]["wired_evidence"]
        assert "face-recognition libraries" in ev
        assert "biometric faceprints" in ev
        assert "cropped, indexed, stored locally" in ev


class TestMechanism757CrossOutletDivergence:
    def test_source_list_url_verbatim(self):
        blk = _block()
        div = blk["cross_outlet_register_divergence"]
        assert div["source_list_url"] == AIINTEL_URL

    def test_peer_registers_cited(self):
        blk = _block()
        div = blk["cross_outlet_register_divergence"]
        assert div["techcrunch_register"].startswith("adversarial")
        assert div["ars_technica_register"].startswith("adversarial")
        assert div["ft_register"].startswith("neutral")
        assert "megalomania" in div["ars_technica_register"]

    def test_wired_softest_reading(self):
        blk = _block()
        div = blk["cross_outlet_register_divergence"]
        assert div["wired_register"].startswith("platform_relay")
        assert "softest register" in div["reading"]

    def test_nypost_counter_frame(self):
        blk = _block()
        cf = blk["post_m712_counter_frame"]
        assert cf["url"] == NYPOST_URL
        assert cf["date"] == "2026-09-19"
        assert "oversold" in cf["claim"]
        assert "post-dates m712" in cf["note"]

    def test_counter_frame_in_finding_summary(self):
        blk = _block()
        assert "oversold AI security breaches" in blk["finding_summary"]


class TestMechanism757Scorer:
    def _scorer(self):
        return _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["openai_arm_avg"] == pytest.approx(0.15)
        assert s["meta_arm_avg"] == pytest.approx(-0.30)

    def test_delta_openai_minus_meta(self):
        s = self._scorer()
        assert s["illustrative_register_delta_openai_minus_meta"] == pytest.approx(0.45)

    def test_delta_arithmetic_logged(self):
        s = self._scorer()
        assert s["delta_calc"] == "0.15 - (-0.30) = 0.45"

    def test_engine_degenerate_only(self):
        s = self._scorer()
        assert "degenerate n=1 check" in s["engine_degenerate"]
        assert "is_significant False" in s["engine_degenerate"]
        assert "0.45" in s["engine_degenerate"]

    def test_convention_target_minus_peer(self):
        s = self._scorer()
        assert "target-minus-peer" in s["convention"]
        assert "target = OpenAI arm" in s["convention"]

    def test_tone_basis_manual_illustrative(self):
        s = self._scorer()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "not empirical corpus scores" in s["methodology"]
        assert "#807" in s["methodology"]

    def test_verdict_and_discipline(self):
        s = self._scorer()
        assert s["verdict"] == "directionally_supported_not_proven"
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False
        assert "NOT_CALCULATED" in s["finding_layer"]


class TestMechanism757Discipline:
    def test_statistical_discipline_block(self):
        d = _block()["statistical_discipline"]
        assert d["is_significant"] is False
        assert d["engine_run"] is False
        assert d["no_analysis_json_update"] is True
        assert d["correlation_not_causation"] is True

    def test_confounders_five_strong_first(self):
        blk = _block()
        conf = blk["confounders"]
        assert len(conf) == 5
        assert conf[0].startswith("STRONG")
        assert conf[1].startswith("STRONG")
        assert any("excerpt-bounded" in c for c in conf)
        assert any("peg mismatch" in c for c in conf)

    def test_counter_evidence_four(self):
        blk = _block()
        ce = blk["counter_evidence"]
        assert len(ce) == 4
        assert any("NY Post" in c for c in ce)
        assert any("Ars Technica" in c for c in ce)
        assert any("Merit-differentiated" in c for c in ce)

    def test_extends_m712(self):
        blk = _block()
        assert "mechanism 712" in blk["extends"]
        assert "iteration 802" in blk["extends"]

    def test_correlation_not_causation_in_summary(self):
        blk = _block()
        assert "Correlation is not causation" in blk["finding_summary"]

    def test_ascii_only_no_em_dashes(self):
        # Serialize only the parsed m757 block (per _block), so unrelated
        # pre-existing content elsewhere in wired.yaml is not measured.
        seg = yaml.safe_dump(_block(), allow_unicode=True, sort_keys=False)
        assert "\u2014" not in seg
        assert all(ord(ch) < 128 for ch in seg)


class TestNoCrossContamination877:
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

    def test_no_underscore_form_757_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_757_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_757(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 757

    def test_falsification_ledger_holds_at_27(self):
        member = "TWENTY-" + "SEVENTH falsification-family member"
        guard = "TWENTY-" + "EIGHTH falsification-family member"
        member_hits = 0
        guard_hits = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                member_hits += content.count(member)
                guard_hits += content.count(guard)
        assert member_hits == 1
        assert guard_hits == 0


class TestDocSync877:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #877" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 44886 |" in readme
        assert "Across 1205 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #877" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #877 Type A:" in log
        assert "Type A #877" in log


class TestDateGrounding877:
    def test_iteration_time_present(self):
        text = _read("profiles/wired.yaml")
        assert "2026-09-20 08:00 PT" in text

    def test_arm_dates_present(self):
        text = _read("profiles/wired.yaml")
        assert "2026-09-11" in text
        assert "2026-09-16" in text
        assert "2026-09-19" in text

    def test_arm_dates_ordered(self):
        assert date(2026, 9, 11) < date(2026, 9, 16) < date(2026, 9, 19) < date(2026, 9, 20)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "875-879" in text
        assert "THIRD leg" in text
        assert "D->E->A" in text
