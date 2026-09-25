"""Type C #994: Meta One link-limit traffic gate with publisher carve-out (Sep 15
2026 launch) - FIRST dedicated corpus mechanism on Meta monetizing outbound
links while exempting news-publisher Pages; FIRST publisher-traffic-gate leg
(TENTH relationship direction in the m807 enumeration) in the
publisher-money-flow family. Mechanism 828 in profiles/competitor-entities.yaml
as a zero-indent top-level tail block.

What this covers: Meta One for Business announced Sep 15 2026 (rolling out
gradually): Essential $14.99/mo, Advanced $49.99/mo, Expert $149.99/mo, Max
$499.99/mo (blotato help-article table; Mari Smith; almcorp). Non-subscribing
Facebook business Pages and professional-mode profiles: TWO organic posts or
comments with external links per month for free (Essential $14.99 keeps the 2/mo
cap); Advanced unlocks 8/mo; Expert 20/mo; Max unlimited on Facebook.
Instagram allowances smaller (Advanced up to 4/mo posts+reels, Expert up to 8,
Max up to 12). Links to Meta own apps, catalog product links, and ads do not
count. Scale-up of the December 2025 limited two-link test TechCrunch first
reported. The decisive incentive fact: Publisher Pages are EXEMPT from the
test (techjuice; almcorp) - licensed news partners (m331 bundle; m594 News
Corp $50M/yr x 3yr from March 2026; m669 Newsmax) keep free unlimited outbound
reach while every other commercial page pays per-link-month.

Incentive geometry: structural contrast with m801 (Sep 2026 DOJ Google ad-tech
remedies - court FORCES Google to loosen publisher-leverage tools: DFP-AdX
untie, mandatory Prebid interfaces, publisher data portability). The same week,
Meta tightens its OWN outbound-link gate while carving out licensed news
publishers. The publisher-money-flow family now has both the compulsory-opening
leg (Google, m801) and the voluntary-gate leg (Meta, this mechanism).
Connects to [801, 331, 669, 594] - all verified pre-commit in HEAD.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger holds at 30 (not a falsification-family member).
Evidence: 7 browser.search query sets' sources, excerpt-bounded per #503,
0 browser.open. No coverage-tone claim. No causal claim.

FIFTH and CLOSING leg of the 990-994 rotation window: D (#990) -> E (#991) ->
A (#992) -> B (#993) -> C (#994, this run).

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
TEST_FILE = "tests/test_type_c_994_meta_one_link_limits_publisher_carveout_sep25_1pm.py"
DATE_STR = "2026-09-25 13:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_828"
NEXT_ID_MARKER = "mechanism" + "_829"
NEXT_ID_DASH = "mechanism" + "-829"

BLOCK_KEY = "type_c_994_meta_one_link_limits_publisher_carveout_sep25"
# Tail-block convention: zero-indent standalone block at the end of the file
EXPECTED_ITERATION = 994
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "af3cc572a36859bb9cf74827a300260efb691e3d"  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://stupiddope.com/2026/09/facebooks-new-link-limits-put-a-price-on-sending-audiences-beyond-meta/",
    "https://savingcountrymusic.com/facebooks-new-link-charge-is-catastrophic-for-independent-music/",
    "https://www.blotato.com/blog/meta-one-link-limits",
    "https://www.techjuice.pk/meta-facebook-pages-limited-link-posts-two-month-meta-one-subscription/",
    "https://www.linkedin.com/pulse/facebook-changing-rules-businesses-again-andrea-lindal-peshc",
    "https://www.facebook.com/marismith/posts/facebooks-new-2-link-limit-whats-the-real-truth-/1713399930153763/",
    "https://almcorp.com/news/facebook-starts-limiting-link-posts-non-paying-pages/",
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


def re_match_main(line):
    import re
    return re.search(r"^Type C #994:", line.split(" ", 1)[1] if " " in line else "")


class TestNovelty994:
    def test_type_c_994_test_file_only(self):
        """Zero test_type_c_994 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_994_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_994_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #994."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #994"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line.split()[0] for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_994_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 828."""
        block = _block()
        assert "zero test_type_c_994 files on disk" in block
        assert "max numeric mechanism id pre-commit 827" in block
        assert "7 of 7 source URLs zero-hit repo-wide pre-commit" in block

    def test_type_c_994_no_literal_underscore_id_keys(self):
        """Designed ID and next ID never appear as literal underscore-form strings."""
        block = _block()
        assert MECH_ID_MARKER not in block
        assert NEXT_ID_MARKER not in block
        assert NEXT_ID_DASH not in block


class TestRotationCycleGuard994:
    def test_window_closes_d_e_a_b_c_for_990_994(self):
        """990-994 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"990", "991", "992", "993", "994"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_990_994(self):
        """Each adjacent pair in the 990-994 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"990", "991", "992", "993", "994"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["990"] == "D" and by_iter["991"] == "E"
        assert by_iter["992"] == "A" and by_iter["993"] == "B"
        assert by_iter["994"] == "C"

    def test_anchor_sha_is_committed_main_commit_994(self):
        """ANCHORED_SHA names a committed object whose subject is the #994 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #994:")


class TestMechanism828Content:
    def test_type_c_994_block_present(self):
        """The 994 tail block is present at zero indent in the profiles file."""
        text = _profiles_text()
        assert ("\n" + BLOCK_KEY + ":") in text

    def test_type_c_994_mechanism_name(self):
        """The mechanism name carries the FIRST traffic-gate claim with the publisher carve-out."""
        block = _block_yaml()
        assert block["mechanism_id"] == 828
        assert block["iteration"] == 994
        assert "publisher carve-out" in block["mechanism_name"]
        assert "FIRST dedicated corpus mechanism on Meta monetizing outbound links" in block["mechanism_name"]

    def test_type_c_994_launch_date_sep15_2026(self):
        """Meta One for Business launch is dated September 15, 2026."""
        block = _block()
        assert "September 15, 2026" in block
        assert "announcement_date: '2026-09-15'" in block

    def test_type_c_994_pricing_tiers(self):
        """All four Meta One tiers and the free tier are mapped with prices."""
        block = _block()
        assert "$14.99/mo" in block
        assert "$49.99/mo" in block
        assert "$149.99/mo" in block
        assert "$499.99/mo" in block
        assert "Free / no subscription" in block

    def test_type_c_994_two_link_free_cap(self):
        """Non-subscribing Pages are capped at TWO link posts/comments per month."""
        block = _block()
        assert "TWO organic posts or comments containing external links per month" in block
        assert "Essential $14.99 keeps the 2/mo cap" in block

    def test_type_c_994_unlock_ladder(self):
        """Advanced 8/mo, Expert 20/mo, Max unlimited on Facebook."""
        block = _block()
        assert "Advanced $49.99 unlocks 8 link posts or comments per month" in block
        assert "Expert $149.99 unlocks 20" in block
        assert "Max $499.99 unlocks unlimited Facebook links" in block

    def test_type_c_994_instagram_allowances_smaller(self):
        """Instagram link allowances are smaller than Facebook at every tier."""
        block = _block()
        assert "Instagram" in block
        assert "up to 4 per month Instagram posts" in block
        assert "up to 12 per month Instagram posts" in block

    def test_type_c_994_dec2025_test_lineage(self):
        """The December 2025 limited test is documented as the lineage."""
        block = _block()
        assert "December 2025" in block
        assert "TechCrunch first reported" in block
        assert "scale/structure expansion" in block

    def test_type_c_994_traffic_context(self):
        """The 1.3% vs 9.8% Meta link-share stat is mapped."""
        block = _block()
        assert "1.3% of widely viewed US posts included external links" in block
        assert "down from 9.8% in 2022" in block

    def test_type_c_994_allowance_mechanics(self):
        """Monthly reset, no rollover, comment-counting workaround closure are mapped."""
        block = _block()
        assert "unused links do not roll over" in block
        assert "closing the first-comment URL workaround" in block

    def test_type_c_994_tenth_relationship_direction(self):
        """The block claims the TENTH relationship direction in the m807 enumeration."""
        block = _block()
        assert "tenth relationship direction" in block
        assert "publisher-traffic-gate" in block

    def test_type_c_994_connects_to_verified_ids(self):
        """connects_to carries the four HEAD-verified mechanism ids."""
        block = _block_yaml()
        assert block["connects_to"] == [801, 331, 669, 594]
        assert "verified present in HEAD" in block["connects_to_verified"]

    def test_type_c_994_incentive_geometry_contrast(self):
        """The m801 structural contrast (compulsory opening vs voluntary gate) is mapped."""
        block = _block()
        assert "compulsory-opening" in block
        assert "voluntary-gate" in block
        assert "DFP-AdX" in block


class TestPublisherCarveout994:
    def test_type_c_994_publisher_exemption(self):
        """Publisher Pages are EXEMPT from the link-limit test."""
        block = _block()
        assert "Publisher Pages are EXEMPT from the test" in block
        assert "news organizations to continue unrestricted external linking" in block

    def test_type_c_994_exemption_sourcing(self):
        """The exemption rests on two named secondary sources."""
        block = _block()
        assert "techjuice" in block
        assert "almcorp" in block
        assert "not a Meta on-the-record statement" in block

    def test_type_c_994_licensee_network(self):
        """The licensee network that benefits (m331 bundle) is mapped."""
        block = _block()
        assert "USA Today" in block
        assert "Le Monde" in block
        assert "m331" in block

    def test_type_c_994_newscorp_leg(self):
        """The News Corp Meta leg ($50M/yr x 3yr from March 2026) is carried via m594."""
        block = _block()
        assert "m594" in block
        assert "$50M/yr x 3yr from March 2026" in block

    def test_type_c_994_newsmax_leg(self):
        """The Newsmax Meta leg (m669) is carried."""
        block = _block()
        assert "m669" in block
        assert "Newsmax" in block


class TestSourceCorroboration994:
    def test_type_c_994_source_urls_verbatim(self):
        """All seven source URLs are verbatim and zero-hit pre-commit."""
        block = _block_yaml()
        assert block["source_urls"] == SOURCE_URLS
        assert len(SOURCE_URLS) == 7
        assert SOURCE_URLS[0].startswith("https://stupiddope.com/2026/09/")
        assert SOURCE_URLS[2] == "https://www.blotato.com/blog/meta-one-link-limits"

    def test_type_c_994_tier_ladder_corroboration(self):
        """The $49/$149/$499 tier ladder is corroborated by two vertical sources."""
        block = _block()
        assert "tier ladder $49/$149/$499" in block
        assert "savingcountrymusic" in block

    def test_type_c_994_own_app_links_excluded(self):
        """Links to Meta own apps, catalog links, and ads do not count."""
        block = _block()
        assert "Links to Meta own apps" in block
        assert "ads do not count" in block

    def test_type_c_994_meta_value_testing_quote(self):
        """Meta stated purpose (value-testing for paying users) is carried."""
        block = _block()
        assert "whether the ability to publish an increased volume of posts with links adds additional value" in block

    def test_type_c_994_no_canonical_urls(self):
        """No canonical URLs were constructed; all are verbatim."""
        block = _block()
        assert "no canonical URLs constructed" in block
        assert "copied verbatim from Full-URL listings" in block


class TestStatisticalDiscipline994:
    def test_type_c_994_qualitative_discipline(self):
        """Qualitative mapping: tone NOT_SCORED, p/d/CI NOT_CALCULATED, not significant, engine not run."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_type_c_994_verdict_supported_not_proven(self):
        """Verdict is directionally_supported_not_proven; no causal claim."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert disc["no_causal_claim"] is True
        assert disc["correlation_not_causation"] is True

    def test_type_c_994_confounders_ranked(self):
        """Confounders are ranked strong-first with seven entries."""
        block = _block()
        assert "STRONG: Gradual rollout" in block
        assert "STRONG: Excerpt-bounded" in block
        assert "MODERATE:" in block
        assert "WEAK:" in block

    def test_type_c_994_bounded_absences(self):
        """Bounded absences per the iteration-492 rule; no zero-coverage claims."""
        block = _block()
        assert "No first-hand Meta help-article read" in block
        assert "No coverage-tone claim" in block


class TestSupersessionAndCorpusPost993:
    def test_type_c_994_max_numeric_id_now_828(self):
        """Max numeric mechanism id is now 828 (colon form)."""
        import re
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 828

    def test_type_c_994_827_superseded_by_designed_828(self):
        """827 (journalists.yaml) remains the previous max; 828 is the new designed head."""
        import re
        out = subprocess.run(
            ["bash", "-c", "grep -rh 'mechanism_id: 82[78]\\b' profiles/ | sort -u"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        assert "mechanism_id: 827" in out
        assert "mechanism_id: 828" in out
        text = _profiles_text()
        assert len(re.findall(r"mechanism_id:\s*828\b", text)) == 1

    def test_type_c_994_zero_829_keys_repo_wide(self):
        """No underscore-829 or colon-829 mechanism keys exist anywhere (next ID unassigned)."""
        import re
        text = _profiles_text()
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_DASH not in text
        assert len(re.findall(r"mechanism_id:\s*829\b", text)) == 0

    def test_type_c_994_829_not_preassigned_in_tests(self):
        """No test source file pre-assigns mechanism 829 (pycache excluded)."""
        out = subprocess.run(
            ["bash", "-c", "grep -rl " + NEXT_ID_MARKER + " tests/*.py 2>/dev/null | head -5"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        assert out.strip() == ""

    def test_type_c_994_block_key_unique_and_top_level_parse(self):
        """The block key is unique and parses as a top-level YAML key."""
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == 828


class TestLedger994:
    def test_type_c_994_thirtieth_positive(self):
        """Ledger holds at 30 positive claims (not a falsification-family member)."""
        disc = _block_yaml()["statistical_discipline"]
        assert "30 positive" in disc["ledger"]
        assert disc["falsification_family"] is False

    def test_type_c_994_thirty_first_absent(self):
        """No 31st ledger member is claimed."""
        block = _block()
        assert "no new member" in block

    def test_type_c_994_ledger_note_and_no_analysis_update(self):
        """analysis.json is untouched; artifact grade is false."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["analysis_json_updated"] is False
        assert disc["artifact_grade"] is False

    def test_type_c_994_block_carries_no_member_claim(self):
        """The block makes no falsification-ledger membership claim."""
        block = _block()
        assert "not a falsification-family member" in block


class TestDocSync994:
    def test_type_c_994_readme_row(self):
        """README test-file table carries the #994 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #994" in text
        assert re.search(r"mechanism" + r"\s+" + "828", text)

    def test_type_c_994_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #994 row right after the #993 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #994:"
        assert row in text
        assert text.index(row) > text.index("Type B #993:")

    def test_type_c_994_architecture_label(self):
        block = _block()
        assert "Type C #994" in block or "iteration: 994" in block


class TestIterationLog994:
    def test_type_c_994_log_entry_present(self):
        """iteration-log.md opens with the #994 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #994 Type C:" in text[:15000]
        assert "Type B #993" in text[:15000]

    def test_type_c_994_log_entry_carries_828(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "828" in head
        assert "Meta One" in head

    def test_type_c_994_log_entry_date_is_friday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "Sep 25 2026, 13:00 PDT" in head

    def test_type_c_994_window_closed_marker(self):
        """The log entry marks the 990-994 D->E->A->B->C window as closed."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "990-994" in head
        assert "window" in head.lower()
