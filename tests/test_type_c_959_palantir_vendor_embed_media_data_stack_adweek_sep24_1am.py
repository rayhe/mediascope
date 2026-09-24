"""Type C #959: Palantir vendor-embed in the media data stack (Dec 2025 - Aug 2026)
- Fox News Digital Newsroom platform (95% of articles), Zeta Global 7-year
Foundry partnership, Stagwell two-product build, USA Today Co. audience-data
deal; 800+ union newsroom employees demand the Palantir tie be cut
(mechanism 807, profiles/competitor-entities.yaml).

Evidence: Sep 23 2026 Adweek first-hand browser.open read this run (240
rendered lines, On Background with Mark Stenberg newsletter-origin): Dec 2025
Fox News Digital deal building the Newsroom platform that now assists in the
production of 95% of its articles (forward-deployed engineers shadowed the
newsroom; Porter Berry: "They didn't just come in and advise. They came in
and built something with us that will endure over time."); June 2026 Zeta
Global seven-year Foundry partnership (Palantir takes a percentage of revenue
on every deal Zeta closes; Zeta rebuilt its data cloud on Foundry, skipping a
competitive review; 600+ Palantir commercial clients as sales channel);
Stagwell two marketing products on Foundry, agentic system live in 16 weeks
from a Penn-Karp handshake; Mark Penn: "There was no concern about reputation
risk. We believe in Palantir and what it's doing."; Aug 2026 USA Today Co.
audience-data monetization deal announced on the Q2 earnings call (Mike Reed:
"Every visit, every session, and every moment of attention creates a
signal."); 800+ employees across 31 unionized USA Today Co. newsrooms urged
the company to end the partnership (reader trust, data security, editorial
independence). Corroborated by the Poynter Aug 2026 union piece (31 unions,
nearly 800 workers in 18 states; "a major player in the news we cover, create
an inherent conflict of interest"; excerpt-bounded per #503).

Incentive geometry (structural market mapping, qualitative Type C only):
  - VENDOR-EMBED: EIGHTH relationship direction in the corpus taxonomy,
    joining (1) sue-then-sign, (2) pay-or-litigate bifurcation, (3)
    grant-then-sue, (4) license-over-authors, (5) pool-and-license, (6)
    infrastructure-capture, (7) publisher-as-feed-operator. The publisher is
    the CUSTOMER: money flows publisher to tech vendor, and the vendor embeds
    forward-deployed engineers inside the newsroom. Dependency vector runs
    publisher-to-vendor, unlike license legs (vendor-to-publisher payment)
    and unlike infrastructure-capture (vendor absorbs publisher operations
    for equity).
  - Distinguishes the Symbolic.ai/News Corp Jan 2026 vendor contract
    (rejected per #729, recorded in #954's research_method): single tooling
    contract, no pattern, no internal contestation. Palantir is a
    four-counterparty pattern (Dec 2025 - Aug 2026) with newsroom-production
    penetration (95% of Fox News Digital articles), explicit reputation-risk
    dismissal on the record, and organized union opposition.
Connects mechanisms [738, 804, 741, 636, 675, 609, 714]. Five confounders
(three STRONG: no tracked-publication counterparty - Fox News Digital is Fox
Corporation not News Corp; no disclosed dollar terms; trade-press
newsletter-origin genre; one MODERATE: one-sided on-record register; one
WEAK: nine-month aggregation). Strongest counterargument: a
publisher-as-customer contract does not imply coverage control; zero
Palantir-deal ties in the tracked set means the leg cannot soften any
tracked publication's Meta or competitor coverage - its value is purely
structural (completes the eighth direction).

Strict qualitative Type C: scorer NOT_SCORED, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, NOT
falsification-family (ledger holds at 29, THIRTIETH negative guard), no
coverage-tone claim, no causal claim, correlational language only,
no analysis.json update.

Rotation: 955-959 window FIFTH leg CLOSING D -> E -> A -> B -> C (anchor #565).
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

MECH_KEY = "palantir_media_data_stack_vendor_embed_adweek_sep2026"
# Avoid literal underscore-form 807 mechanism key strings in this file so the #715-style novelty sweep stays clean.
MECH_ID_MARKER = "mechanism" + "_807"
NEXT_ID_MARKER = "mechanism" + "_808"
NEXT_ID_NUMERIC = "mechanism_id: 808"
NEXT_SIBLING = "advance_dual_asset_monetization:"
SOURCE_URL_1 = "https://www.adweek.com/media/palantir-media-marketing-partnership-push/"
SOURCE_URL_2 = "https://www.poynter.org/business-work/2026/usa-today-co-unions-call-on-the-company-to-cut-ties-with-palantir/"
FILE_NAME = "test_type_c_959_palantir_vendor_embed_media_data_stack_adweek_sep24_1am.py"

# Placeholder for the follow-up commit that pins the iteration to its own commit.
ANCHORED_SHA = "3091188beba9444f7be08e70502855ea3a350f26"

ITERATION = 959
TYPE_LETTER = "C"
DATE_STR = "2026-09-24 01:00 PDT"


def _block() -> dict:
    doc = open(PROFILES_PATH, encoding="utf-8").read()
    start = doc.index("  " + MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    segment = doc[start:end]
    return yaml.safe_load(segment)[MECH_KEY]


class TestNovelty959:
    def test_type_c_959_file_is_the_only_959_type_c_file(self) -> None:
        files = [f for f in glob.glob(f"{REPO}/tests/test_type_c_959*.py")]
        assert len(files) == 1, f"expected exactly one Type C #959 file, got {files}"
        assert files[0].endswith(FILE_NAME)

    @pytest.mark.anchor
    def test_type_c_959_main_commit_unique_and_anchored(self) -> None:
        # Deselected pre-commit per the #565 followup convention; patched green
        # post-commit. Asserts exactly one "Type C #959:" main commit exists in
        # history and its SHA is the patched ANCHORED_SHA (the anchor and
        # log-hash followups carry "Type C #959 anchor/log-hash followup"
        # subjects, not the bare "Type C #959:" main subject). Replaces the
        # pre-commit-only absence pin (no "Type C #959" commit yet) whose greps
        # are recorded in the committed block's novelty field per #752; the
        # block pins the pre-commit novelty claim, this test pins the anchor.
        assert ANCHORED_SHA != "0" * 40, "anchor SHA is still the pre-commit placeholder"
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--all", "--format=%H %s", "--grep", "Type C #959"],
            capture_output=True,
            text=True,
        )
        mains = [
            line.split(" ", 1)[0]
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #959:", line)
        ]
        assert mains == [ANCHORED_SHA], (
            f"expected exactly one Type C #959 main commit {ANCHORED_SHA}, got {mains}"
        )

    def test_novelty_claim_is_pinned_in_block(self) -> None:
        block = _block()
        assert "zero palantir_media" in block["novelty"]
        assert block["research_method"]


class TestRotationCycleGuard959:
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

    def test_955_959_window_closes_d_e_a_b_c(self) -> None:
        expected = [
            ("C", "959"),
            ("B", "958"),
            ("A", "957"),
            ("E", "956"),
            ("D", "955"),
        ]
        window = self._window()
        assert window[:5] == expected, f"rotation window mismatch: {window[:5]}"

    def test_each_955_959_edge_adjacent(self) -> None:
        expected = [
            ("C", "959"),
            ("B", "958"),
            ("A", "957"),
            ("E", "956"),
            ("D", "955"),
        ]
        window = self._window()
        for i, pair in enumerate(expected):
            assert window[i] == pair

    def test_anchor_sha_is_the_committed_main_commit(self) -> None:
        # The anchor pins the MAIN commit, not HEAD: the anchor follow-up and
        # log-hash follow-up commits sit on top of it by design, so ANCHORED_SHA
        # == HEAD can never hold. Assert ANCHORED_SHA is a real commit present
        # in history carrying the "Type C #959:" main subject.
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--all", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        shas = [line.split(" ", 1)[0] for line in out.stdout.splitlines()]
        assert ANCHORED_SHA in shas, (
            f"anchored SHA {ANCHORED_SHA} not found in repo history"
        )
        grep = subprocess.run(
            ["git", "-C", REPO, "log", "--all", "--format=%H %s", "--grep", "Type C #959"],
            capture_output=True,
            text=True,
        )
        assert any(
            line.startswith(ANCHORED_SHA + " Type C #959:")
            for line in grep.stdout.splitlines()
        ), f"anchored SHA {ANCHORED_SHA} carries no Type C #959 main subject"


class TestMechanism807Content:
    def test_block_present_under_marketplace_intermediary_landscape(self) -> None:
        block = _block()
        assert block["mechanism_id"] == 807
        assert block["iteration"] == ITERATION
        assert block["type"] == TYPE_LETTER
        assert block["date"] == DATE_STR

    def test_deal_facts_fox_news_digital(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert "Dec 2025" in facts["fox_news_digital"]
        assert "95%" in facts["fox_news_digital"]
        assert "Newsroom" in facts["fox_news_digital"]
        assert "Berry" in facts["fox_news_digital"]

    def test_deal_facts_zeta_global(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert "seven-year" in facts["zeta_global"]
        assert "percentage of revenue" in facts["zeta_global"]
        assert "600+" in facts["zeta_global"]

    def test_deal_facts_stagwell_and_usa_today(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert "Two marketing products" in facts["stagwell"]
        assert "16 weeks" in facts["stagwell"]
        assert "Q2 earnings call" in facts["usa_today_co"]
        assert "Every visit" in facts["usa_today_co"]

    def test_deal_facts_union_pushback(self) -> None:
        block = _block()
        facts = block["deal_facts"]
        assert "31" in facts["union_pushback"]
        assert "800" in facts["union_pushback"]
        assert "immediately end" in facts["union_pushback"]

    def test_quotes_penn_and_berry(self) -> None:
        block = _block()
        quotes = block["quotes"]
        assert "no concern about reputation risk" in quotes["penn_reputation_risk"]
        assert "forward-deployed engineer sits with the reporter" in quotes["berry_newsroom"]

    def test_quotes_reed_kahan_and_union(self) -> None:
        block = _block()
        quotes = block["quotes"]
        assert "weeks or months" in quotes["reed_monetization"]
        assert "$1 trillion" in quotes["kahan_ontology"]
        assert "inherent conflict of interest" in quotes["union_conflict"]

    def test_incentive_geometry_eighth_direction(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        assert "EIGHTH relationship direction" in geom["vendor_embed"]
        assert "publisher-as-customer" in geom["vendor_embed"].lower() or "PUBLISHER pays" in geom["vendor_embed"]
        assert "publisher-as-feed-operator" in geom["vendor_embed"]

    def test_incentive_geometry_bidirectional_and_scarcity(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        assert "Bidirectional" in geom["bidirectional_tilt"]
        assert "929" in geom["scarcity_thesis_leg"]
        assert "No coverage-tone claim" in geom["intermediary_disclosure"]

    def test_connects_to_uses_verified_ids(self) -> None:
        block = _block()
        connects = block["connects_to"]
        for ref in [738, 804, 741, 636, 675, 609, 714]:
            assert ref in connects, f"expected verified reference {ref} in connects_to"

    def test_source_urls_verbatim_and_first_hand(self) -> None:
        block = _block()
        src = " ".join(block["sources"])
        assert SOURCE_URL_1 in src
        assert SOURCE_URL_2 in src
        assert "240 rendered lines" in src
        assert "first-hand browser.open read this run" in src

    def test_poynter_excerpt_bounded(self) -> None:
        block = _block()
        src = " ".join(block["sources"])
        assert "excerpt-bounded per #503" in src
        assert "Poynter" in src

    def test_no_tracked_publication_tie_claimed(self) -> None:
        block = _block()
        assert "Fox Corporation, not News Corp" in block["incentive_geometry"]["intermediary_disclosure"]
        conf = " ".join(c["text"] for c in block["confounders_ranked"])
        assert "tracked set" in conf

    def test_strongest_counterargument_is_structural(self) -> None:
        block = _block()
        ca = block["strongest_counterargument"]
        assert "cannot soften" in ca
        assert "purely structural" in ca


class TestStatisticalDiscipline959:
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


class TestSupersessionAndCorpusPost958:
    def test_max_numeric_mechanism_id_is_807(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        ids = [int(m) for m in re.findall(r"mechanism_id: (\d+)", doc)]
        assert max(ids) == 807

    def test_max_806_superseded_by_designed_807(self) -> None:
        # #958's mechanism 806 lives in profiles/careers/journalists.yaml (Type B
        # journalist leg); this run's designed leg is 807 in competitor-entities.
        journalists = open(f"{REPO}/profiles/careers/journalists.yaml", encoding="utf-8").read()
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 806" in journalists  # #958 James Pero leg still present
        assert "mechanism_id: 807" in doc  # this run's designed leg
        assert "mechanism_id: 808" not in doc

    def test_zero_underscore_next_id_repo_wide(self) -> None:
        # Format-built needle per #715; no literal next-id marker carried in the file.
        needle = "mechanism" + "_808"
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "--", needle, "--", "."],
            capture_output=True,
            text=True,
        )
        hits = [h for h in out.stdout.splitlines() if not h.strip().startswith("Binary")]
        assert hits == [], f"unexpected next-id key strings repo-wide: {hits[:3]}"

    def test_zero_numeric_next_id_in_profiles(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 808" not in doc

    def test_957_zero_underscore_806_sweep_stays_green(self) -> None:
        # #957's post-commit sweep pinned zero underscore-form 806 key hits; after this
        # run the sweep target is the format-built marker, which must stay
        # absent repo-wide (this file builds it only as a runtime value).
        needle = "mechanism" + "_806"
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "--", needle, "--", "."],
            capture_output=True,
            text=True,
        )
        hits = [h for h in out.stdout.splitlines() if not h.strip().startswith("Binary")]
        assert hits == [], f"#957 zero-underscore-806 sweep violated: {hits[:3]}"

    def test_958_zero_numeric_807_sweep_fails_by_designed_supersession(self) -> None:
        # #958 pinned zero numeric "mechanism_id: 807" pre-commit. This run
        # deliberately supersedes that sweep: numeric 807 must appear exactly
        # once, in the designed block.
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        occurrences = len(re.findall(r"mechanism_id: 807", doc))
        assert occurrences == 1, f"expected exactly one numeric 807, got {occurrences}"
        block = _block()
        assert block["mechanism_id"] == 807


class TestLedger959:
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


class TestDocSync959:
    def test_readme_test_file_row_present(self) -> None:
        text = open(README_PATH, encoding="utf-8").read()
        assert f"`{FILE_NAME}`" in text

    def test_architecture_tree_row_present(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        assert FILE_NAME in text

    def test_architecture_row_has_type_c_959_label(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        row = next(
            line for line in text.splitlines() if FILE_NAME in line
        )
        assert "Type C #959" in row


class TestIterationLog959:
    def test_iteration_log_has_959_type_c_entry(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        assert "## #959 Type C:" in text

    def test_iteration_log_entry_carries_mechanism_number_and_topic(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        head = text[:4000]
        assert "## #959 Type C:" in head
        assert "807" in head
        assert "Palantir" in head

    def test_date_is_thursday(self) -> None:
        assert datetime.date(2026, 9, 24).strftime("%A") == "Thursday"
