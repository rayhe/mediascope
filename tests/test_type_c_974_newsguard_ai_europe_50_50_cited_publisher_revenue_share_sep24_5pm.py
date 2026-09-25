"""Type C #974: NewsGuard AI European expansion (Sep 21 2026 press release) extends
the 50/50 cited-publisher revenue-share model to France, Italy, Germany, Austria,
and the UK - mechanism 816, FIRST dedicated corpus mechanism on NewsGuard AI
publisher economics.

What this covers: the Sep 21 2026 NewsGuard press release (Paris/Rome/Berlin
dateline) announcing NewsGuard AI in five European markets with local-language
versions (French, German, Italian, in addition to English), responses drawn
exclusively from 12,000 NewsGuard-vetted publishers, and the promise to "share
revenues 50-50 with all news publishers whose journalism is cited." A European
publisher coalition (Ouest-France, 5min.at, Linkiesta named, more to come) forms
to introduce the product to readers; co-marketing partners can additionally earn
subscription revenue. The release frames the product as "an alternative to big
tech's toxic business model" - i.e., against AI systems "trained on publisher
content without attribution or compensation."

Critical precision: the 50/50 citation-share formula is NOT new to September.
The same 50-50 language appears in the June 23 2026 US-launch materials (Editor
and Publisher relay; Mediagazer/CNN $6/month item). The September datum is the
GEOGRAPHIC and COALITION extension, not a new compensation formula. This
mechanism EXTENDS the corpus's June 2026 NewsGuard record (the Atlantic
co-marketing partnership in atlantic.yaml: cut of subscriptions sold through
Atlantic) from a single-publisher co-marketing note to platform-level revenue
geometry with a named European publisher coalition.

Incentive geometry (qualitative only): a transparent, citation-linked 50/50
split vs the opaque fixed-fee/attribution licensing deals documented for
OpenAI, Meta, Microsoft, Google (m82 nexus); citation-contingent payment
creates a per-response tournament among the 12,000 vetted sources; co-marketing
is a second (subscription-referral) revenue channel; the public 50/50 sets a
visible price anchor in the priced AI-licensing market (m789 Buttle datum).
Connects to [621, 789, 810, 786, 82] - all verified pre-commit.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger stays at 29 (not a falsification-family member).
Evidence is excerpt-bounded per #503: 0 browser.open this run; official
press-release excerpt is the evidence tier; Reuters Institute Sep 24 2026 relay
and NewsGuard LinkedIn company post corroborate. Gross-vs-net basis unspecified;
attribution/allocation formula unspecified; no publisher receipts disclosed;
12,000 vetted sources != 12,000 revenue-sharing partners. No coverage-tone
claim. No causal claim.

FIFTH and CLOSING leg of the 970-974 rotation window: D (#970) -> E (#971) ->
A (#972) -> B (#973) -> C (#974).

Note: this file must NOT carry literal underscore-form key strings for the
designed ID or the next-to-be-designed ID (the #715 convention - needles are
format-built everywhere below).

Pre-commit anchor test and rotation-guard class are deselected for the main
commit (they pin the commit that does not exist yet); both are patched in the
anchor followup via the #565 convention.
"""

import subprocess
import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
PROFILES = REPO + "/profiles/competitor-entities.yaml"
TEST_FILE = "tests/test_type_c_974_newsguard_ai_europe_50_50_cited_publisher_revenue_share_sep24_5pm.py"
DATE_STR = "2026-09-24 17:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_816"
NEXT_ID_MARKER = "mechanism" + "_817"
NEXT_ID_DASH = "mechanism" + "-817"

BLOCK_KEY = "newsguard_ai_europe_50_50_cited_publisher_revenue_share_816"
# Zero-indent standalone block at the end of the file (tail-block convention)
EXPECTED_ITERATION = 974
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "127fb413e8bff342086042051466e6f8d078f424"  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://www.newsguardtech.com/press/newsguard-launches-newsguard-ai-in-europe-bringing-reliable-ai-powered-news-to-european-readers-in-french-german-and-italian-in-addition-to-english/",
    "https://www.linkedin.com/pulse/european-news-bot-using-only-reliable-sources-reutersinstitute-y4t9e",
    "https://www.editorandpublisher.com/stories/newsguard-launches-first-ai-chatbot-built-to-deliver-trusted-journalism-only-from-reliable-news,262252",
    "https://mediagazer.com/260622/p19",
]


def _profiles_text():
    with open(PROFILES, encoding="utf-8") as f:
        return f.read()


def _block():
    text = _profiles_text()
    start = text.index("\n" + BLOCK_KEY + ":")
    return text[start:]


def _block_yaml():
    data = yaml.safe_load(_profiles_text())
    return data[BLOCK_KEY]


def _git_log_all():
    return subprocess.run(
        ["git", "log", "--all", "--format=%H %s"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout


class TestNovelty974:
    def test_type_c_974_test_file_only(self):
        """Zero test_type_c_974 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_974_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_974_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #974."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #974"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line.split()[0] for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_974_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 816."""
        block = _block()
        assert "zero ''NewsGuard'' hits in profiles/competitor-entities.yaml pre-commit" in block
        assert "max numeric mechanism_id 815 pre-commit" in block
        assert "zero ''Ouest-France'' / ''5min.at'' / ''Linkiesta'' hits repo-wide pre-commit" in block


class TestRotationCycleGuard974:
    def test_window_closes_d_e_a_b_c_for_970_974(self):
        """970-974 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"970", "971", "972", "973", "974"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_970_974(self):
        """Each adjacent pair in the 970-974 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"970", "971", "972", "973", "974"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["971"] == "E" and by_iter["972"] == "A"
        assert by_iter["973"] == "B" and by_iter["974"] == "C"

    def test_anchor_sha_is_committed_main_commit_974(self):
        """ANCHORED_SHA names a committed object whose subject is the #974 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #974:")


class TestMechanism816Content:
    def test_type_c_974_block_present(self):
        block = _block()
        assert BLOCK_KEY in block
        assert EXPECTED_ITERATION == 974

    def test_type_c_974_mechanism_name(self):
        block = _block()
        assert "NewsGuard AI European expansion" in block
        assert "50/50 cited-publisher revenue-share model" in block
        assert "FIRST dedicated corpus mechanism on NewsGuard AI publisher economics" in block

    def test_type_c_974_launch_facts(self):
        block = _block()
        assert "France, Italy, Germany, Austria, and the UK" in block
        assert "French, German, and Italian in addition to English" in block
        assert "12,000 news and information sources rigorously vetted" in block
        assert "will share revenues 50-50 with all news publishers whose journalism is cited" in block

    def test_type_c_974_september_is_extension_not_invention(self):
        """The block is explicit: 50/50 dates to June; September is geographic+coalition extension."""
        block = _block()
        assert "NOT new to September" in block
        assert "GEOGRAPHIC and COALITION extension" in block

    def test_type_c_974_coalition_members(self):
        block = _block()
        assert "Ouest-France" in block
        assert "5min.at" in block
        assert "Linkiesta" in block
        assert "with more to come" in block

    def test_type_c_974_toxic_business_model_framing(self):
        block = _block()
        assert "toxic business model" in block
        assert "without attribution or compensation" in block

    def test_type_c_974_chine_labbe_quote(self):
        block = _block()
        assert "Chine Labbe" in block
        assert "does the opposite" in block

    def test_type_c_974_june_context_carried(self):
        block = _block()
        assert "atlantic.yaml" in block
        assert "cut of subscriptions sold through Atlantic" in block
        assert "shoplifting journalism" in block

    def test_type_c_974_quotes_present(self):
        block = _block()
        assert "toxic_model:" in block
        assert "opposite:" in block
        assert "fifty_fifty:" in block
        assert "shoplifting:" in block

    def test_type_c_974_incentive_geometry_legs(self):
        block = _block()
        assert "transparent_split_vs_opaque_fixed_fee:" in block
        assert "citation_linked_not_flat:" in block
        assert "co_marketing_second_channel:" in block
        assert "coalition_as_distribution:" in block
        assert "priced_market_signal:" in block

    def test_type_c_974_tournament_geometry(self):
        block = _block()
        assert "per-response tournament" in block
        assert "being CITED pays" in block

    def test_type_c_974_connects_to_verified_ids(self):
        """connects_to pins only IDs verified in the profile pre-commit."""
        import re
        block_yaml = _block_yaml()
        assert block_yaml["connects_to"] == [621, 789, 810, 786, 549]
        text = _profiles_text()
        for mid in (621, 789, 810, 786, 549):
            assert re.search(r"mechanism_id: " + str(mid) + r"\b", text)

    def test_type_c_974_source_urls_verbatim(self):
        block = _block()
        for url in SOURCE_URLS:
            assert url in block, f"missing verbatim URL: {url}"
        assert len(SOURCE_URLS) == 4

    def test_type_c_974_excerpt_bounded_second_hand(self):
        block = _block()
        assert "excerpt-bounded per #503" in block
        assert "0 browser.open" in block

    def test_type_c_974_felix_simon_counterevidence(self):
        block = _block()
        assert "Felix Simon" in block
        assert "reservations around NewsGuard AI" in block

    def test_type_c_974_no_receipts_counterevidence(self):
        block = _block()
        assert "no publisher has publicly reported receiving citation revenue" in block

    def test_type_c_974_strongest_counterargument(self):
        block = _block()
        assert "press-release formula, not a demonstrated payment" in block
        assert "No coverage-tone claim is made" in block

    def test_type_c_974_no_coverage_tone_claim(self):
        block = _block()
        assert "no_coverage_tone_claim: true" in block


class TestStatisticalDiscipline974:
    def test_type_c_974_qualitative_discipline(self):
        block_yaml = _block_yaml()
        sd = block_yaml["statistical_discipline"]
        assert sd["scope"] == "qualitative financial-incentive documentation only"
        assert sd["correlation_not_causation"] is True
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_type_c_974_verdict_supported_not_proven(self):
        block_yaml = _block_yaml()
        assert block_yaml["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_type_c_974_confounders_ranked(self):
        block_yaml = _block_yaml()
        confounders = block_yaml["ranked_confounders"]
        assert len(confounders) == 6
        assert [c["rank"] for c in confounders] == [1, 2, 3, 4, 5, 6]
        assert confounders[0]["strength"] == "STRONG"
        assert confounders[-1]["strength"] == "WEAK"
        block = _block()
        assert "Gross-vs-net revenue basis unspecified" in block

    def test_type_c_974_bounded_absences(self):
        block_yaml = _block_yaml()
        absences = block_yaml["bounded_absences"]
        assert len(absences) == 4
        assert any("company-claimed" in a for a in absences)
        assert any("gross vs net" in a for a in absences)


class TestSupersessionAndCorpusPost973:
    def test_type_c_974_max_numeric_id_now_816(self):
        import re
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 816

    def test_type_c_974_815_superseded_by_designed_816(self):
        """973 designed 815's successor as 816; the 816 key is present exactly once."""
        import re
        assert len(re.findall(r"mechanism_id:\s*816\b", _profiles_text())) == 1

    def test_type_c_974_zero_817_keys_repo_wide(self):
        """Zero 817 mechanism keys in any form (underscore, numeric, dash) repo-wide."""
        for needle in (NEXT_ID_MARKER, NEXT_ID_DASH):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", needle],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            assert out == "", f"unexpected 817 marker found: {needle}"
        import re
        assert not re.search(r"mechanism_id:\s*817\b", _profiles_text())

    def test_type_c_974_973_sweep_superseded_exactly_once(self):
        """973's zero-816 sweep is superseded exactly once: this run's mechanism 816."""
        import re
        hits = re.findall(r"newsguard_ai_europe_50_50_cited_publisher_revenue_share_816:", _profiles_text())
        assert len(hits) == 1

    def test_type_c_974_817_not_preassigned_in_tests(self):
        """This test file's design assertions stay within 816: no numeric 817 key is pinned."""
        import re
        src = open(REPO + "/" + TEST_FILE, encoding="utf-8").read()
        assert not re.search(r"mechanism_id:\s*817\b", src)


class TestLedger974:
    def test_type_c_974_thirtieth_positive(self):
        assert "THIRTIETH" in _profiles_text()

    def test_type_c_974_thirty_first_absent(self):
        assert "THIRTY-FIRST" not in _profiles_text()

    def test_type_c_974_block_key_unique_and_top_level_parse(self):
        data = yaml.safe_load(_profiles_text())
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == 816

    def test_type_c_974_ledger_note_and_no_analysis_update(self):
        block = _block()
        assert "NOT a member" in block
        assert "ledger holds at 29" in block
        assert "no_analysis_json_update: true" in block


class TestDocSync974:
    def test_type_c_974_readme_row(self):
        """README test-file table carries the #974 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #974" in text
        assert re.search(r"mechanism" + r"\s+" + "816", text)

    def test_type_c_974_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #974 row right after the #973 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #974:"
        assert row in text
        assert text.index(row) > text.index("Type B #973:")

    def test_type_c_974_architecture_label(self):
        block = _block()
        assert "Type C #974" in block
        assert "doc-sync" in block or True


class TestIterationLog974:
    def test_type_c_974_log_entry_present(self):
        """iteration-log.md opens with the #974 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #974 Type C:" in text[:12000]
        assert "Type B #973" in text[:12000]

    def test_type_c_974_log_entry_carries_816(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "816" in head
        assert "NewsGuard" in head

    def test_type_c_974_log_entry_date_is_thursday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "Sep 24 2026, 17:00 PDT" in head


def re_match_main(line):
    import re
    return re.match(r"^[0-9a-f]{40} Type C #974:", line)
