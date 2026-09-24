"""Type C #964: Platkin LLP publisher collective v. OpenAI + Microsoft (first
suit Jun 24 2026: nearly 400 local/regional newspapers; second suit Sep 16
2026: 26 new publishers, 60 publishers / 550-plus publications) - FIRST
dedicated corpus mechanism on litigation-tier consolidation: one boutique
firm aggregates the sue tier into a 550-publication bloc expecting
consolidation with the NYT-led MDL (mechanism 810,
profiles/competitor-entities.yaml, entities.openai).

Evidence: 4 browser.search query sets this run, 0 browser.open
(excerpt-bounded per #503). Jun 24 2026 first suit (NJ Globe, Editor and
Publisher, PYMNTS): Platkin LLP - boutique firm founded earlier in 2026 by
former New Jersey AG Matthew J. Platkin and AG-office litigators - filed on
behalf of nearly 400 local/regional newspapers against OpenAI and Microsoft;
systematic-copying and DMCA 1202 CMI-stripping allegations; Altman House of
Lords "impossible to train" testimony; largest coordinated legal effort by
local/regional newspapers. Sep 16 2026 second suit (Law.com Sep 17;
Memphis Magazine Sep 16): 26 new publishers joined (Times Publishing
Company/Tampa Bay Times, Austin Chronicle Corp., Alternative Newsweekly
Foundation, SwimSwam Partners per Insider NJ via Cryptopolitan; Memphis
Magazine/Memphis Flyer/Memphis Parent plus Noisy Creek colleagues);
collective now 60 publishers / 550-plus publications; expects consolidation
with the In re OpenAI Copyright Infringement MDL very soon. Matt Platkin:
"The scale of this coalition should be a wake-up call."

Incentive geometry (structural litigation-economics mapping, qualitative
Type C only):
  - LITIGATION-POOLING: NINTH relationship direction per the m807
    enumeration (sue-then-sign, pay-or-litigate bifurcation, grant-then-sue,
    license-over-authors, pool-and-license, infrastructure-capture,
    publisher-as-feed-operator, vendor-embed). Publishers aggregate CLAIMS
    through a single law firm to sue - the mirror of pool-and-license
    (m720: publishers aggregate RIGHTS through a network operator to sell).
    Money-flow geometry is cost-amortization across 550 publications plus
    MDL-riding, not a payer leg. Taxonomy-count tension noted: m737's
    finding enumerated termination-leverage as its seventh direction; the
    m807 enumeration used here does not list it; not resolved this run.
  - Scale economics: the NYT's $28M-plus solo litigation spend (m753)
    amortized across 550 publications through one boutique firm - the sue
    tier's answer to the sign tier's bilateral deal costs.
  - MDL-riding: same procedural logic as m762's MDL-family linkage; the
    bloc inherits the September 2026 escalation's pricing momentum (m756
    partial-summary-judgment motions; m759 unsealed testimony) without the
    MDL plaintiffs' spend.
  - Sign-tier parallel: the sue tier consolidates while the sign tier
    expands in the same month (India attribution blitz Sep 7-8, Village
    Media Sep 16) - the sign-or-sue bifurcation is not resolving; both
    poles are scaling.
  - Local-news texture: the bloc is local/regional - same surface as m714's
    Village Media sign-tier leg; the local-news vertical now has a sign leg
    and a sue leg in the same month.
Connects mechanisms [636, 720, 675, 762, 756, 759, 753, 714]. Six ranked
confounders (three STRONG: 0 browser.open this run; 60/550 figures are
plaintiff-side self-reported; MDL consolidation expected not ordered; two
MODERATE: n=1 law firm; local/regional composition; one WEAK: Jun 24 first
suit is three months old). Three bounded absences per the iteration-492
rule. Strongest counterargument: collective scale is leverage, not victory -
the 550-publication bloc aggregates bargaining power on both the litigation
and settlement paths; its value is structural (completes the ninth
direction), not predictive of case outcomes or of any tracked publication's
coverage.

Strict qualitative Type C: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, scorer none,
engine NOT run, verdict directionally_supported_not_proven, NOT
artifact-grade, NOT falsification-family (ledger holds at 29, THIRTIETH
negative guard), no coverage-tone claim, no causal claim, correlational
language only, no analysis.json update.

Rotation: 960-964 window FIFTH leg CLOSING D -> E -> A -> B -> C (anchor
#565). Pre-commit anchor test and rotation-guard class are deselected for
the main commit (they pin the commit that does not exist yet); patch
ANCHORED_SHA in the anchor follow-up commit. Doc-sync and iteration-log
entry tests go green pre-commit (docs updated before the main commit).
"""

from __future__ import annotations

import datetime
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
PROFILES_PATH = f"{REPO}/profiles/competitor-entities.yaml"
LOG_PATH = f"{REPO}/iteration-log.md"
README_PATH = f"{REPO}/README.md"
ARCH_PATH = f"{REPO}/docs/ARCHITECTURE.md"

MECH_KEY = "platkin_collective_60_publishers_550_publications_litigation_pooling_sep2026"
# Avoid literal underscore-form 810/811 mechanism key strings in this file so
# the #715-style novelty sweep stays clean.
MECH_ID_MARKER = "mechanism" + "_810"
NEXT_ID_MARKER = "mechanism" + "_811"
NEXT_ID_NUMERIC = "mechanism_id: 811"
# Stable end boundary: the next 2-space entity key after this block. The slice
# may include the in-flight #884 block; parsed[MECH_KEY] selects this one.
NEXT_SIBLING = "\n  anthropic:"
SOURCE_URL_1 = "https://memphismagazine.com/the-memo/memphis-magazine-joins-landmark-copyright-lawsuit-against-op/"
SOURCE_URL_2 = "https://www.law.com/njlawjournal/2026/09/17/former-nj-ags-firm-helms-copyright-fight-against-openai-microsoft-on-behalf-of-500-plus-regional-news-publishers/"
SOURCE_URL_3 = "https://www.tradingkey.com/news/cryptocurrencies/262172046-cryptopolitan"
SOURCE_URL_4 = "https://newjerseyglobe.com/media/nearly-400-local-newspapers-sue-openai-microsoft-over-alleged-copyright-theft/"
FILE_NAME = "test_type_c_964_platkin_collective_60_publishers_550_publications_litigation_pooling_sep24_7am.py"

# Placeholder for the follow-up commit that pins the iteration to its own commit.
ANCHORED_SHA = "4484e24988020771601c2859dd7cbf9ac484cf99"

ITERATION = 964
TYPE_LETTER = "C"
DATE_STR = "2026-09-24 07:00 PDT"


def _block() -> dict:
    doc = open(PROFILES_PATH, encoding="utf-8").read()
    start = doc.index("    " + MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    segment = doc[start:end]
    return yaml.safe_load(segment)[MECH_KEY]


class TestNovelty964:
    def test_type_c_964_file_is_the_only_964_type_c_file(self) -> None:
        matches = sorted(
            os.path.basename(p)
            for p in glob.glob(f"{REPO}/tests/test_type_c_964_*.py")
        )
        assert matches == [FILE_NAME], f"unexpected 964 test files: {matches}"

    @pytest.mark.anchor
    def test_type_c_964_main_commit_unique_and_anchored(self) -> None:
        # Deselected pre-commit: pins the commit that does not exist yet.
        # Replaces the pre-commit-only absence pin (no "Type C #964" commit
        # yet) whose greps are recorded in the committed block's novelty field
        # per #752; the block pins the pre-commit novelty claim, this test
        # pins the anchor.
        assert ANCHORED_SHA != "0" * 40, "anchor SHA is still the pre-commit placeholder"
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--all", "--format=%H %s", "--grep", "Type C #964"],
            capture_output=True,
            text=True,
        )
        mains = [
            line.split(" ", 1)[0]
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #964:", line)
        ]
        assert mains == [ANCHORED_SHA], (
            f"expected exactly one Type C #964 main commit {ANCHORED_SHA}, got {mains}"
        )

    def test_novelty_claim_is_pinned_in_block(self) -> None:
        block = _block()
        assert "platkin" in block["novelty"]
        assert "NINTH relationship direction" in block["novelty"]
        assert block["research_method"]


class TestRotationCycleGuard964:
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

    def test_960_964_window_closes_d_e_a_b_c(self) -> None:
        expected = [
            ("C", "964"),
            ("B", "963"),
            ("A", "962"),
            ("E", "961"),
            ("D", "960"),
        ]
        window = self._window()
        assert window[:5] == expected, f"rotation window mismatch: {window[:5]}"

    def test_each_960_964_edge_adjacent(self) -> None:
        expected = [
            ("C", "964"),
            ("B", "963"),
            ("A", "962"),
            ("E", "961"),
            ("D", "960"),
        ]
        window = self._window()
        for i, pair in enumerate(expected):
            assert window[i] == pair

    def test_anchor_sha_is_the_committed_main_commit(self) -> None:
        # The anchor pins the MAIN commit, not HEAD: the anchor follow-up and
        # log-hash follow-up commits sit on top of it by design, so ANCHORED_SHA
        # == HEAD can never hold. Assert ANCHORED_SHA is a real commit present
        # in history carrying the "Type C #964:" main subject.
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
            ["git", "-C", REPO, "log", "--all", "--format=%H %s", "--grep", "Type C #964"],
            capture_output=True,
            text=True,
        )
        assert any(
            line.startswith(ANCHORED_SHA + " Type C #964:")
            for line in grep.stdout.splitlines()
        ), f"anchored SHA {ANCHORED_SHA} carries no Type C #964 main subject"


class TestMechanism810Content:
    def test_block_present_under_entities_openai(self) -> None:
        block = _block()
        assert block["mechanism_id"] == 810
        assert block["iteration"] == ITERATION
        assert block["rotation"] == "Type C"
        assert block["date_analyzed"] == "2026-09-24"
        assert block["time_pdt"] == "07:00"

    def test_mechanism_name_carries_parties_and_scale(self) -> None:
        block = _block()
        assert "Platkin LLP" in block["mechanism_name"]
        assert "550" in block["mechanism_name"]

    def test_first_suit_facts(self) -> None:
        block = _block()
        facts = " ".join(block["suit_facts"])
        assert "Jun 24 2026" in facts
        assert "400" in facts
        assert "DMCA" in facts
        assert "Altman" in facts
        assert "systematic copying" in facts

    def test_second_suit_facts(self) -> None:
        block = _block()
        facts = " ".join(block["suit_facts"])
        assert "Sep 16 2026" in facts
        assert "26 new publishers" in facts
        assert "60 publishers" in facts
        assert "550-plus publications" in facts

    def test_second_suit_named_publishers(self) -> None:
        block = _block()
        facts = " ".join(block["suit_facts"])
        assert "Tampa Bay Times" in facts
        assert "Austin Chronicle" in facts
        assert "Memphis Magazine" in facts
        assert "Noisy Creek" in facts

    def test_firm_facts(self) -> None:
        block = _block()
        facts = " ".join(block["suit_facts"])
        assert "Matthew J. Platkin" in facts
        assert "boutique" in facts

    def test_mdl_linkage(self) -> None:
        block = _block()
        facts = " ".join(block["suit_facts"])
        assert "multi-district litigation" in facts
        assert "consolidat" in facts
        assert "1:25-md-03143" in facts

    def test_quotes(self) -> None:
        block = _block()
        quotes = block["quotes"]
        assert "wake-up call" in quotes["wake_up_call"]
        assert "school board meetings" in quotes["school_board_meetings"]
        assert "not about stopping AI innovation" in quotes["platkin_linkedin"]

    def test_ninth_direction_litigation_pooling(self) -> None:
        block = _block()
        tax = block["relationship_direction_taxonomy"]
        assert "NINTH relationship direction" in tax
        assert "LITIGATION-POOLING" in tax
        assert "mirror" in tax
        assert "aggregate CLAIMS" in tax

    def test_taxonomy_count_tension_noted(self) -> None:
        block = _block()
        assert "m737" in block["relationship_direction_taxonomy"]
        assert "termination-leverage" in block["relationship_direction_taxonomy"]

    def test_incentive_geometry_legs(self) -> None:
        block = _block()
        geom = block["incentive_geometry"]
        assert "$28M" in geom["scale_economics"]
        assert "MDL" in geom["mdl_riding"]
        assert "both poles are scaling" in geom["sign_tier_parallel"]
        assert "sign leg" in geom["local_news_texture"]
        assert "sue leg" in geom["local_news_texture"]

    def test_connects_to_uses_verified_ids(self) -> None:
        block = _block()
        connects = block["connects_to"]
        for ref in [636, 720, 675, 762, 756, 759, 753, 714]:
            assert ref in connects, f"expected verified reference {ref} in connects_to"

    def test_source_urls_verbatim(self) -> None:
        block = _block()
        src = block["source_urls"]
        assert SOURCE_URL_1 in src
        assert SOURCE_URL_2 in src
        assert SOURCE_URL_3 in src
        assert SOURCE_URL_4 in src

    def test_sources_excerpt_bounded_and_attributed(self) -> None:
        block = _block()
        src = " ".join(block["sources"])
        assert "excerpt-bounded per #503" in src
        assert "0 browser.open" in src
        assert "Second-hand attribution marked" in src
        assert "Insider NJ" in src

    def test_strongest_counterargument_is_structural(self) -> None:
        block = _block()
        ca = block["strongest_counterargument"]
        assert "leverage, not victory" in ca
        assert "not predictive of case outcomes" in ca


class TestStatisticalDiscipline964:
    def test_qualitative_type_c_discipline(self) -> None:
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["scorer"] == "none"
        assert sd["engine_run"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_verdict(self) -> None:
        block = _block()
        assert block["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_confounders_ranked_and_counterargument_present(self) -> None:
        block = _block()
        confs = block["ranked_confounders"]
        strengths = [c["strength"] for c in confs]
        assert len(confs) == 6
        assert "STRONG" in strengths and "MODERATE" in strengths and "WEAK" in strengths
        assert len(block["counterevidence"]) == 3
        assert block["strongest_counterargument"]

    def test_bounded_absences_present(self) -> None:
        block = _block()
        assert len(block["bounded_absences"]) == 3
        assert "iteration-492" in " ".join(block["bounded_absences"])


class TestSupersessionAndCorpusPost963:
    def test_max_numeric_mechanism_id_is_810(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        ids = [int(m) for m in re.findall(r"mechanism_id: (\d+)", doc)]
        assert max(ids) == 810

    def test_max_809_superseded_by_designed_810(self) -> None:
        # #963's mechanism 809 lives in profiles/careers/journalists.yaml (Type B
        # journalist leg); this run's designed leg is 810 in competitor-entities.
        journalists = open(f"{REPO}/profiles/careers/journalists.yaml", encoding="utf-8").read()
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 809" in journalists  # #963 leg still present
        assert "mechanism_id: 810" in doc  # this run's designed leg
        assert "mechanism_id: 811" not in doc

    def test_zero_underscore_next_id_repo_wide(self) -> None:
        # Format-built needle per #715; no literal next-id marker carried in the file.
        needle = "mechanism" + "_811"
        out = subprocess.run(
            ["git", "-C", REPO, "grep", "-F", "--", needle, "--", "."],
            capture_output=True,
            text=True,
        )
        hits = [h for h in out.stdout.splitlines() if not h.strip().startswith("Binary")]
        assert hits == [], f"unexpected next-id key strings repo-wide: {hits[:3]}"

    def test_zero_numeric_next_id_in_profiles(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "mechanism_id: 811" not in doc

    def test_963_zero_numeric_810_sweep_fails_by_designed_supersession(self) -> None:
        # #963 pinned zero numeric "mechanism_id: 810" pre-commit. This run
        # deliberately supersedes that sweep: numeric 810 must appear exactly
        # once, in the designed block.
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        occurrences = len(re.findall(r"mechanism_id: 810", doc))
        assert occurrences == 1, f"expected exactly one numeric 810, got {occurrences}"
        block = _block()
        assert block["mechanism_id"] == 810


class TestLedger964:
    def test_thirtieth_negative_guard_intact(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert "THIRTIETH" in doc
        assert "THIRTY-FIRST" not in doc

    def test_block_key_unique_and_entities_parse(self) -> None:
        doc = open(PROFILES_PATH, encoding="utf-8").read()
        assert doc.count("    " + MECH_KEY + ":") == 1
        parsed = yaml.safe_load(open(PROFILES_PATH, encoding="utf-8"))
        assert MECH_KEY in parsed["entities"]["openai"]

    def test_not_falsification_family_member(self) -> None:
        block = _block()
        assert "NOT a member" in block["falsification_family"]
        assert "29" in block["falsification_family"]

    def test_no_analysis_json_update(self) -> None:
        block = _block()
        assert block["no_analysis_json_update"] is True


class TestDocSync964:
    def test_readme_test_file_row_present(self) -> None:
        text = open(README_PATH, encoding="utf-8").read()
        assert f"`{FILE_NAME}`" in text

    def test_architecture_tree_row_present(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        assert FILE_NAME in text

    def test_architecture_row_has_type_c_964_label(self) -> None:
        text = open(ARCH_PATH, encoding="utf-8").read()
        row = next(
            line for line in text.splitlines() if FILE_NAME in line
        )
        assert "Type C #964" in row


class TestIterationLog964:
    def test_iteration_log_has_964_type_c_entry(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        assert "## #964 Type C:" in text

    def test_iteration_log_entry_carries_mechanism_number_and_topic(self) -> None:
        text = open(LOG_PATH, encoding="utf-8").read()
        head = text[:4000]
        assert "## #964 Type C:" in head
        assert "810" in head
        assert "Platkin" in head

    def test_date_is_thursday(self) -> None:
        assert datetime.date(2026, 9, 24).strftime("%A") == "Thursday"
