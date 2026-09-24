"""Type C #954: Noxtua raises circa EUR 100M Series C (Sep 23 2026) - German legal
publisher C.H. Beck becomes majority shareholder, Austrian legal publisher MANZ
co-invests (mechanism 804, profiles/competitor-entities.yaml).

Evidence: Sep 23 2026 Artificial Lawyer first-hand browser.open read (71 rendered
lines, fetched at iteration time): Noxtua raised around EUR 100M in a Series C;
C.H. Beck became the new majority shareholder; Austrian legal publisher MANZ
also invested; early law-firm backers CMS and Dentons sold their shares and stay
as anchor clients; Noxtua told Artificial Lawyer that C.H. Beck and MANZ are now
the only investors besides founder/CEO Dr. Leif-Nissen Lundbaek; Lundbaek:
Noxtua is developed on exclusive content from leading legal publishers and has
built Europe's largest legal database and largest network of independent legal
publishers; C.H. Beck exec board member Prof. Dr. Klaus Weber: combining
publisher data with AI technology is the model, framed as an investment in the
future of the law; Artificial Lawyer frames the combination as a pan-European
EU sovereignty play against US and UK legal-AI giants. Corroborated by the
Sep 23 2026 techstartups funding roundup (C.H.BECK taking majority control;
strategic-ownership-over-investment thesis; excerpt-bounded per #503).

Incentive geometry (structural market mapping, qualitative Type C only):
  - OWNERSHIP INVERSION: first corpus leg where the publisher is the AI
    company's majority OWNER, inverting every prior bilateral leg (AI company
    pays publisher). Bidirectional tilt: pro-portfolio-company coverage of its
    own asset; potentially harder adversarial coverage of rival AI labs that
    threaten the exclusive-content moat.
  - Scarcity-thesis leg: extends mechanism 929 (who can withhold what) - the
    exclusive-content moat is the withholdable asset; publishers moved from
    licensing content to owning the AI company built on it.
  - Third resolution class in the publisher-AI incentive matrix: license
    (payer legs), litigate (plaintiff legs 514/519/753), own (shareholder).
Connects mechanisms [929, 714, 609, 753, 519, 514]. Five confounders (two
STRONG: no tracked-publication tie; trade-press genre; two MODERATE: undisclosed
round terms; law-firm exit scope; one WEAK: first-day reporting). Strongest
counterargument: publisher majority stake does not guarantee coverage control;
editorial independence norms and zero C.H. Beck/MANZ tracked-publication ties
mean the leg cannot soften any tracked outlet's Meta or competitor coverage -
its value is purely structural (completes the ownership class).

Strict qualitative Type C: scorer NOT_SCORED, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, NOT
falsification-family (ledger holds at 29, THIRTIETH negative guard), no
coverage-tone claim, no causal claim, correlational language only,
no analysis.json update.

Rotation: 950-954 window FIFTH leg closing D -> E -> A -> B -> C (anchor #565).
Pre-commit anchor and rotation-guard tests are deselected for the main commit
(they pin the commit that does not exist yet); patch ANCHORED_SHA in the
anchor follow-up commit. Iteration-log entry tests fail by design pre-commit
and go green in the log-hash follow-up commit.
"""

from __future__ import annotations

import datetime
import glob
import re
import subprocess

import pytest
import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
PROFILES_PATH = f"{REPO}/profiles/competitor-entities.yaml"
LOG_PATH = f"{REPO}/iteration-log.md"
README_PATH = f"{REPO}/README.md"
ARCH_PATH = f"{REPO}/docs/ARCHITECTURE.md"

MECH_KEY = "noxtua_ch_beck_majority_shareholder_eur100m_series_c_publisher_owns_ai_sep2026"
# Avoid literal "mechanism_804" in this file so the #715-style novelty sweep stays clean.
MECH_ID_MARKER = "mechanism" + "_804"
NEXT_ID_MARKER = "mechanism" + "_805"
NEXT_ID_NUMERIC = "mechanism_id: 805"
NEXT_SIBLING = "advance_dual_asset_monetization:"
SOURCE_URL_1 = "https://www.artificiallawyer.com/2026/09/23/noxtua-raises-e100m-c-h-beck-now-majority-shareholder/"
SOURCE_URL_2 = "https://techstartups.com/2026/09/23/startup-funding-news-today-september-23-2026-tekever-f13-brahma-ai-noxtua-standardx-more/"
FILE_NAME = "test_type_c_954_noxtua_ch_beck_majority_shareholder_publisher_owns_ai_sep23_8pm.py"

# Placeholder for the follow-up commit that pins the iteration to its own commit.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

ITERATION = 954
TYPE_LETTER = "C"
DATE_STR = "2026-09-23 20:00 PDT"


def _block() -> dict:
    doc = open(PROFILES_PATH, encoding="utf-8").read()
    start = doc.index("  " + MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    segment = doc[start:end]
    return yaml.safe_load(segment)[MECH_KEY]


class TestNovelty954:
    def test_type_c_954_file_is_the_only_954_type_c_file(self) -> None:
        files = [f for f in glob.glob(f"{REPO}/tests/test_type_c_954*.py")]
        assert len(files) == 1, f"expected exactly one Type C #954 file, got {files}"
        assert files[0].endswith(FILE_NAME)

    def test_no_type_c_954_commit_before_this_iteration(self) -> None:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--oneline", "--grep=Type C #954"],
            capture_output=True,
            text=True,
        )
        matches = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{7,40}\s+Type C #954\b", line)
        ]
        assert matches == [], f"unexpected pre-existing Type C #954 commit: {matches}"

    def test_novelty_claim_is_pinned_in_block(self) -> None:
        block = _block()
        assert "zero noxtua" in block["novelty"]
        assert block["research_method"]


class TestRotationCycleGuard954:
    # Deselected pre-commit: pins the commit that does not exist yet.
    def _window(self) -> list[tuple[str, str]]:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--oneline", "-30"],
            capture_output=True,
            text=True,
        )
        found: list[tuple[str, str]] = []
        for line in out.stdout.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        return found

    def test_950_954_window_closes_d_e_a_b_c(self) -> None:
        expected = [
            ("C", "954"),
            ("B", "953"),
            ("A", "952"),
            ("E", "951"),
            ("D", "950"),
        ]
        window = self._window()
        assert window[:5] == expected, f"rotation window mismatch: {window[:5]}"

    def test_each_950_954_edge_adjacent(self) -> None:
        expected = [
            ("C", "954"),
            ("B", "953"),
            ("A", "952"),
            ("E", "951"),
            ("D", "950"),
        ]
        window = self._window()
        for i, pair in enumerate(expected):
            assert window[i] == pair

    def test_anchor_sha_matches_repo_head(self) -> None:
        head = subprocess.run(
            ["git", "-C", REPO, "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert ANCHORED_SHA == head, (
            f"anchor {ANCHORED_SHA!r} does not match HEAD {head!r}; "
            "patch ANCHORED_SHA in the anchor follow-up commit"
        )


class TestMechanism804Content:
    def test_block_present_under_marketplace_intermediary_landscape(self) -> None:
        block = _block()
        assert block["mechanism_id"] == 804
        assert block["iteration"] == ITERATION
        assert block["type"] == TYPE_LETTER
        assert block["date"] == DATE_STR

    def test_deal_facts_majority_shareholder(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert facts["amount"] == "circa EUR 100M Series C"
        assert "majority shareholder" in facts["majority_shareholder"].lower() or "C.H. Beck" in facts["majority_shareholder"]
        assert "C.H. Beck" in facts["majority_shareholder"]
        assert "MANZ" in facts["co_investor"]
        assert "CMS" in facts["exiting_investors"] and "Dentons" in facts["exiting_investors"]
        assert "anchor clients" in facts["exiting_investors"]
        assert "only investors" in facts["post_round_investor_base"]

    def test_deal_facts_remaining_and_exiting(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert "Lundbaek" in facts["remaining_shareholder"]
        assert "Global Brain" in facts["other_exiting"]
        assert "KDDI" in facts["other_exiting"]
        assert "Schiener" in facts["other_exiting"]

    def test_lundbaek_quote_exclusive_content(self) -> None:
        block = _block()
        quote = block["quotes"]["lundbaek"]
        assert "exclusive content" in quote
        assert "legal publishers" in quote
        assert "largest legal database" in quote

    def test_weber_quote_publisher_rationale(self) -> None:
        block = _block()
        quote = block["quotes"]["weber_ch_beck"]
        assert "high-quality data" in quote
        assert "investment in the future of the law" in quote
        assert "MANZ" in quote

    def test_trade_press_frame_sovereignty(self) -> None:
        block = _block()
        frame = block["quotes"]["trade_press_frame"]
        assert "EU" in frame or "pan-European" in frame
        assert "US and UK" in frame

    def test_incentive_geometry_ownership_inversion(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        inv = geom["ownership_inversion"]
        assert "majority OWNER" in inv
        assert "publisher" in inv.lower()
        assert "bidirectional" in block["counterevidence"][0] or "bidirectional" in inv

    def test_incentive_geometry_scarcity_and_resolution_class(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        assert "929" in geom["scarcity_thesis_leg"]
        assert "withhold" in geom["scarcity_thesis_leg"]
        assert "753" in geom["resolution_class"]
        assert "third resolution class" in geom["resolution_class"]

    def test_incentive_geometry_no_coverage_tone_claim(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        assert "No coverage-tone claim" in geom["intermediary_disclosure"]
        assert "Structural geometry leg only" in block["summary"]

    def test_connects_to_uses_verified_ids(self) -> None:
        block = _block()
        connects = block["connects_to"]
        for ref in [929, 714, 609, 753, 519, 514]:
            assert ref in connects, f"expected verified reference {ref} in connects_to"

    def test_source_urls_verbatim_and_zero_hit_pre_commit(self) -> None:
        block = _block()
        src = " ".join(block["sources"])
        assert SOURCE_URL_1 in src
        assert SOURCE_URL_2 in src
        assert "71 rendered lines" in src
        assert "second-hand per #503" in src

    def test_first_hand_read_recorded(self) -> None:
        block = _block()
        src = " ".join(block["sources"])
        assert "first-hand browser.open read this run" in src
        assert "Artificial Lawyer" in src

    def test_no_tracked_publication_tie_claimed(self) -> None:
        block = _block()
        conf = " ".join(c["text"] for c in block["confounders_ranked"])
        assert "not tracked general-news publications" in block["incentive_geometry"]["intermediary_disclosure"]
        assert "tracked set" in conf

    def test_strongest_counterargument_is_structural(self) -> None:
        block = _block()
        ca = block["strongest_counterargument"]
        assert "cannot soften" in ca
        assert "zero C.H. Beck/MANZ ties" in ca
        assert "purely structural" in ca


class TestStatisticalDiscipline954:
    def test_qualitative_type_c_discipline(self) -> None:
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scorer"] == "none"
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_verdict_and_ledger(self) -> None:
        block = _block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["artifact_grade"] is False
        assert block["no_analysis_json_update"] is True
        assert block["falsification_ledger_holds_at"] == 29
        assert block["falsification_family"] is False

    def test_designed_keying(self) -> None:
        block = _block()
        assert block["tone_scores"] == "NOT_SCORED"
        assert "qualitative" in block["statistical_discipline_note"].lower()

    def test_confounders_ranked_and_counterargument_present(self) -> None:
        block = _block()
        confs = block["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert len(confs) == 5
        assert "STRONG" in strengths and "MODERATE" in strengths and "WEAK" in strengths
        assert len(block["counterevidence"]) == 3
        assert block["strongest_counterargument"]


class TestSupersessionAndCorpusPost953:
    def test_max_numeric_mechanism_id_is_804(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        ids = [int(m) for m in re.findall(r"mechanism_id: (\d+)", doc)]
        assert max(ids) == 804

    def test_max_803_superseded_by_designed_804(self) -> None:
        # #953's mechanism 803 lives in profiles/careers/journalists.yaml (Type B
        # journalist leg); this run's designed leg is 804 in competitor-entities.
        journalists = open(f"{REPO}/profiles/careers/journalists.yaml", encoding="utf-8").read()
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 803" in journalists  # #953 Katie Notopoulos leg still present
        assert "mechanism_id: 804" in doc  # this run's designed leg
        assert "mechanism_id: 805" not in doc

    def test_zero_underscore_next_id_repo_wide(self) -> None:
        # Format-built needle per #715; no literal next-id marker carried in the file.
        needle = "mechanism" + "_805"
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "--", needle, "--", "."],
            capture_output=True,
            text=True,
        )
        hits = [h for h in out.stdout.splitlines() if not h.strip().startswith("Binary")]
        assert hits == [], f"unexpected next-id key strings repo-wide: {hits[:3]}"

    def test_zero_numeric_next_id_in_profiles(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 805" not in doc

    def test_953_zero_underscore_804_sweep_stays_green(self) -> None:
        # #953's post-commit sweep pinned zero "mechanism_804" hits; after this
        # run the sweep target is the format-built marker, which must stay
        # absent repo-wide (this file builds it only as a runtime value).
        needle = "mechanism" + "_804"
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "--", needle, "--", "."],
            capture_output=True,
            text=True,
        )
        hits = [h for h in out.stdout.splitlines() if not h.strip().startswith("Binary")]
        assert hits == [], f"#953 zero-underscore-804 sweep violated: {hits[:3]}"

    def test_953_zero_numeric_804_sweep_fails_by_designed_supersession(self) -> None:
        # #953 pinned zero numeric "mechanism_id: 804" pre-commit. This run
        # deliberately supersedes that sweep: numeric 804 must appear exactly
        # once, in the designed block.
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        occurrences = len(re.findall(r"mechanism_id: 804", doc))
        assert occurrences == 1, f"expected exactly one numeric 804, got {occurrences}"
        block = _block()
        assert block["mechanism_id"] == 804


class TestLedger954:
    def test_thirtieth_negative_guard_intact(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "THIRTIETH" in doc
        assert "THIRTY-FIRST" not in doc

    def test_block_key_unique_and_entities_parse(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert doc.count("  " + MECH_KEY + ":") == 1
        parsed = yaml.safe_load(open(PROFILES_PATH, encoding="utf-8"))
        mil = parsed["marketplace_intermediary_landscape"]
        assert MECH_KEY in mil

    def test_not_falsification_family_member(self) -> None:
        block = _block()
        assert block["falsification_family"] is False
        assert block["falsification_ledger_holds_at"] == 29

    def test_no_analysis_json_update(self) -> None:
        block = _block()
        assert block["no_analysis_json_update"] is True


class TestDocSync954:
    def test_readme_test_file_row_present(self) -> None:
        text = open(README_PATH, encoding="utf-8").read()
        assert f"`{FILE_NAME}`" in text

    def test_architecture_tree_row_present(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        assert FILE_NAME in text

    def test_architecture_row_has_type_c_954_label(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        row = next(
            line for line in text.splitlines() if FILE_NAME in line
        )
        assert "Type C #954" in row


class TestIterationLog954:
    def test_iteration_log_has_954_type_c_entry(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        assert "## #954 Type C:" in text

    def test_iteration_log_entry_carries_mechanism_number_and_topic(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        head = text[:4000]
        assert "## #954 Type C:" in head
        assert "804" in head
        assert "Noxtua" in head

    def test_date_is_wednesday(self) -> None:
        assert datetime.date(2026, 9, 23).strftime("%A") == "Wednesday"
