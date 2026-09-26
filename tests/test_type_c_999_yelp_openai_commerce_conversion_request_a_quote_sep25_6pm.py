"""Type C #999: OpenAI x Yelp content-to-commerce licensing (mechanism 831) -
FIRST dedicated corpus mechanism on a commerce-conversion licensing leg;
ELEVENTH relationship direction in the m807 enumeration; FIFTH and CLOSING leg
of the 995-999 rotation window (D #995 -> E #996 -> A #997 -> B #998 -> C #999,
this run). Mechanism 831 in profiles/competitor-entities.yaml as a zero-indent
top-level tail block.

What this covers: Axios reported the OpenAI-Yelp arrangement on July 23, 2026
(Yelp disclosed the agreement in its 2026 earnings). OpenAI licensed Yelp
reviews, ratings, photos and business information (about 330 million cumulative
reviews, 8 million-plus business listings); Yelp branding and links appear in
ChatGPT answers while OpenAI decides how the data is presented; the deal is
non-exclusive (Yelp already licenses data to Apple Maps and Alexa, OpenAI
joins as an additional payer); financial terms undisclosed; Yelp shares rose
about 8% on the disclosure day. The novel leg: a planned in-answer Request a
Quote feature inside ChatGPT that counts as a billable Yelp lead (per-lead
price unpublished, leads carry no source tag), so the consideration path runs
THROUGH the product surface into a transaction layer rather than around it as
a flat fee. Kelly (Media Copilot 99-deal episode) frames the arrangement as
"content to commerce" and predicts an OpenAI-Times settlement on similar
commerce-conversion terms before its IPO; Notbohm (2026 Local Visibility
Index) frames it as "the AI answer is becoming the whole funnel: discovery,
evaluation, and contact in one conversation." Connects to [735, 753, 509, 594]
- all verified pre-commit in HEAD.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade, no analysis.json update. Ledger holds at 30 (not a
falsification-family member). Evidence: 6 sources via browser.search query
sets, excerpt-bounded per #503, 0 browser.open. No coverage-tone claim.
No causal claim. Yelp is a data/review platform, not one of the seven tracked
publications - carried as a structural deal-mechanism comparator, not direct
evidence about publication tone.

Note: this file must NOT carry literal underscore-form key strings for the
designed ID or the next-to-be-designed ID (the #715 convention - needles are
format-built everywhere below).

Pre-commit anchor test and rotation-guard class are deselected for the main
commit (they pin the commit that does not exist yet); both are patched in the
anchor followup via the #565 convention. Doc-sync 3 fail pre-commit per #719.

Doc-sync: 51341/1323 -> 51390/1324; +49/+1 = the #999 file exactly (.venv
python authoritative). 49 tests, 11 classes. FIFTH and CLOSING leg of the
995-999 rotation window: D (#995) -> E (#996) -> A (#997) -> B (#998) ->
C (#999, this run). Concurrency: #899/#938/#900 in-flight untouched.
Sep 25 2026 18:00 PDT.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path("/home/hatch/workspace/repos/mediascope")
PROFILES = REPO / "profiles/competitor-entities.yaml"
TEST_FILE = "test_type_c_999_yelp_openai_commerce_conversion_request_a_quote_sep25_6pm.py"
DATE_STR = "2026-09-25 18:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_831"
NEXT_ID_MARKER = "mechanism" + "_832"
NEXT_ID_DASH = "mechanism" + "-832"

BLOCK_KEY = "type_c_999_yelp_openai_commerce_conversion_request_a_quote_sep25"
EXPECTED_ITERATION = 999
EXPECTED_MECHANISM = 831
EXPECTED_TESTS = 49
README_TESTS_BEFORE, README_TESTS_AFTER = 51341, 51390
README_FILES_BEFORE, README_FILES_AFTER = 1323, 1324
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "0" * 40  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://benfromaiso.substack.com/p/chatgpt-and-yelp-what-the-deal-actually",
    "https://www.ainvest.com/news/yelp-sold-openai-review-moat-money-claim-2609/",
    "https://www.ivet360.com/yelp-necessary-evil-local-marketing-chatgpt-visibility/",
    "https://www.webfx.com/blog/ai/yelp-chatgpt/",
    "https://www.linkedin.com/posts/michael-notbohm-ecxie_chatgpt-and-yelp-what-the-deal-actually-activity-7354981695543844865-ZpYc",
    "https://mediacopilot.substack.com/p/what-99-ai-licensing-deals-reveal",
]

CONNECTS_TO = [735, 753, 509, 594]

STAGED_SET = {
    "profiles/competitor-entities.yaml",
    f"tests/{TEST_FILE}",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}

CONCURRENCY_UNTOUCHED = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=REPO
    )


def _profiles_text():
    return PROFILES.read_text(encoding="utf-8")


def _block():
    text = _profiles_text()
    start = text.index("\n" + BLOCK_KEY + ":")
    return text[start:]


def _block_yaml():
    return yaml.safe_load(_profiles_text())[BLOCK_KEY]


def _git_log_all():
    return run_git("log", "--all", "--format=%H %s").stdout


class TestNovelty999:
    def test_single_type_c_999_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_c_999*.py"))
        assert [f.name for f in files] == [TEST_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "0" * 40
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #999" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = _block()
        assert "zero test_type_c_999 files on disk" in block
        assert "max numeric mechanism id pre-commit 830" in block
        assert "6 of 6 source URLs zero-hit repo-wide pre-commit" in block

    def test_no_literal_underscore_id_keys(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        assert NEXT_ID_MARKER not in block
        assert NEXT_ID_DASH not in block


class TestRotationCycleGuard999:
    @pytest.mark.rotation
    def test_fifth_and_closing_leg_of_995_to_999_window(self):
        text = (REPO / "iteration-log.md").read_text(encoding="utf-8")
        assert "## #995" in text and "Type D" in text
        assert "## #996" in text and "Type E" in text
        assert "## #997" in text and "Type A" in text
        assert "## #998" in text and "Type B" in text
        block = _block_yaml()
        assert block["iteration"] == EXPECTED_ITERATION
        assert block["rotation"] == "C"

    @pytest.mark.rotation
    def test_predecessor_998_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep=#998")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1000_type_d_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type D #1000")
        assert r.stdout.strip() == ""
        assert "## #1000" not in (REPO / "iteration-log.md").read_text(
            encoding="utf-8"
        )

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_c_999_by_commit_time(self):
        matches = [
            l for l in _git_log_all().splitlines() if l.strip()
        ]
        own = run_git("log", "--format=%H", "--", f"tests/{TEST_FILE}").stdout.splitlines()
        competing = [
            l
            for l in matches
            if re.search(r"Type C #999\b", l) and l.split()[0] not in own
        ]
        assert competing == [], f"concurrent Type C #999 commits: {competing}"


class TestMechanism831Content:
    def test_type_c_999_block_present(self):
        """The 999 tail block is present at zero indent in the profiles file."""
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data

    def test_type_c_999_mechanism_id_831_designed_keying(self):
        """Designed mechanism id is 831; colon form only, no literal underscore keys."""
        block = _block_yaml()
        assert block["mechanism_id"] == EXPECTED_MECHANISM
        assert MECH_ID_MARKER not in _block()

    def test_type_c_999_mechanism_name_eleventh_direction(self):
        block = _block_yaml()
        assert "content-to-commerce" in block["mechanism_name"]
        assert "ELEVENTH relationship direction" in block["mechanism_name"]

    def test_type_c_999_axios_jul23_2026(self):
        block = _block()
        assert "July 23, 2026" in block
        assert "Axios" in block

    def test_type_c_999_licensed_data_scope(self):
        block = _block()
        assert "330 million" in block
        assert "8 million" in block
        assert "ratings, photos" in block

    def test_type_c_999_non_exclusive_terms_undisclosed(self):
        block = _block()
        assert "Non-exclusive" in block
        assert "Financial terms undisclosed" in block

    def test_type_c_999_branding_links_openai_presentation(self):
        block = _block()
        assert "Yelp branding and links appear in ChatGPT answers" in block
        assert "OpenAI decides how the data is presented" in block


class TestCommerceConversion999:
    def test_request_a_quote_billable_lead(self):
        """The transaction layer: an in-ChatGPT quote request is a billable Yelp lead."""
        block = _block()
        assert "counts as a billable Yelp lead" in block
        assert "per-lead price is unpublished" in block
        assert "no source tag" in block

    def test_kelly_content_to_commerce_framing(self):
        block = _block()
        assert '"content to commerce"' in block
        assert "request-a-quote button inside the answer" in block
        assert "revenue share or a placement consideration" in block

    def test_notbohm_whole_funnel(self):
        block = _block()
        assert "the whole funnel: discovery, evaluation, and contact in one conversation" in block

    def test_apple_maps_alexa_multi_payer(self):
        """Yelp already licenses data to Apple Maps and Alexa; OpenAI joins as a payer."""
        block = _block()
        assert "Apple Maps and Alexa" in block
        assert "OpenAI joins as an additional payer" in block

    def test_brightlocal_demand_signal(self):
        block = _block()
        assert "99,281 citations" in block
        assert "80% of local answers" in block
        assert "Google Business Profile is absent from the top ten" in block

    def test_local_visibility_index_scarcity(self):
        block = _block()
        assert "ChatGPT recommended 1.2% of locations" in block
        assert "35.9% for the Google local 3-pack" in block

    def test_yelp_comparator_not_publication(self):
        """Yelp is carried as a structural deal-mechanism comparator, not a publication."""
        block = _block()
        assert "not one of the seven tracked publications" in block
        assert "structural deal-mechanism comparator" in block


class TestSourceCorroboration999:
    def test_source_urls_verbatim(self):
        """All six source URLs appear verbatim in the block."""
        block = _block()
        for url in SOURCE_URLS:
            assert url in block, url

    def test_source_url_evidence_tier_pinned(self):
        block = _block()
        assert "Six sources, zero pre-commit corpus hits" in block
        assert "excerpt-bounded per #503" in block

    def test_no_canonical_urls_constructed(self):
        block = _block_yaml()
        assert "no canonical URLs constructed" in block["novelty"]

    def test_six_of_six_zero_hit_pinned_in_novelty(self):
        block = _block_yaml()
        assert "6 of 6 source URLs zero-hit repo-wide pre-commit" in block["novelty"]
        assert 'zero "yelp" strings repo-wide pre-commit' in block["novelty"]


class TestStatisticalDiscipline999:
    def test_qualitative_discipline(self):
        """Qualitative only: no tone scores, no statistics, engine not run."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_verdict_directionally_supported_not_proven(self):
        disc = _block_yaml()["statistical_discipline"]
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert disc["correlation_not_causation"] is True
        assert disc["no_causal_claim"] is True

    def test_confounders_ranked_strong_first(self):
        block = _block_yaml()
        confs = block["confounders_ranked"]
        assert len(confs) == 7
        assert confs[0].startswith("STRONG:")
        assert confs[1].startswith("STRONG:")
        assert confs[2].startswith("STRONG:")
        assert confs[3].startswith("MODERATE:")
        assert confs[5].startswith("WEAK:")
        assert any("Excerpt-bounded per #503" in c for c in confs[:3])

    def test_bounded_absences(self):
        block = _block_yaml()
        absences = block["bounded_absences"]
        assert len(absences) == 6
        assert any("No first-hand Yelp earnings release" in a for a in absences)
        assert any("No coverage-tone claim" in a for a in absences)
        assert any("Deliberate exclusion" in a for a in absences)


class TestSupersessionAndCorpusPost998:
    def test_max_numeric_id_now_831(self):
        """Max numeric mechanism id is now 831 (colon form)."""
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 831

    def test_830_superseded_by_designed_831(self):
        """830 (journalists.yaml) remains the previous max; 831 is the new designed head."""
        out = subprocess.run(
            ["bash", "-c", "grep -rh 'mechanism_id: 83[01]\\b' profiles/ | sort -u"],
            capture_output=True, text=True, cwd=REPO, check=True,
        ).stdout
        assert "mechanism_id: 830" in out
        assert "mechanism_id: 831" in out
        assert len(re.findall(r"mechanism_id:\s*831\b", _profiles_text())) == 1

    def test_zero_832_keys_repo_wide(self):
        """No underscore-832, dash-832, or colon-832 mechanism keys exist (next ID unassigned)."""
        text = _profiles_text()
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_DASH not in text
        assert len(re.findall(r"mechanism_id:\s*832\b", text)) == 0

    def test_832_not_preassigned_in_tests(self):
        """No test source file pre-assigns mechanism 832 (pycache excluded)."""
        out = subprocess.run(
            ["bash", "-c", "grep -rl " + NEXT_ID_MARKER + " tests/*.py 2>/dev/null | head -5"],
            capture_output=True, text=True, cwd=REPO,
        ).stdout
        assert out.strip() == ""

    def test_block_key_unique_and_top_level_parse(self):
        """The block key is unique and parses as a top-level YAML key."""
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == 831


class TestLedger999:
    def test_thirtieth_positive_claim(self):
        """Ledger holds at 30 positive claims (not a falsification-family member)."""
        disc = _block_yaml()["statistical_discipline"]
        assert "30 positive" in disc["ledger"]
        assert disc["falsification_family"] is False

    def test_thirty_first_absent(self):
        """No 31st ledger member is claimed."""
        block = _block()
        assert "no new member" in block

    def test_ledger_note_and_no_analysis_update(self):
        """analysis.json is untouched; artifact grade is false."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["analysis_json_updated"] is False
        assert disc["artifact_grade"] is False

    def test_block_carries_no_member_claim(self):
        """The block makes no falsification-ledger membership claim."""
        block = _block()
        assert "not a falsification-family member" in block


class TestDocSync999:
    def test_readme_stats_updated(self):
        text = (REPO / "README.md").read_text(encoding="utf-8")
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_999(self):
        text = (REPO / "README.md").read_text(encoding="utf-8")
        assert f"`tests/{TEST_FILE}`" in text
        assert text.index(f"`tests/{TEST_FILE}`") > text.index(
            "`tests/test_type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743.py`"
        )

    def test_architecture_tree_row_for_999(self):
        text = (REPO / "docs/ARCHITECTURE.md").read_text(encoding="utf-8")
        row = TEST_FILE + "  # Type C #999:"
        assert row in text
        assert text.index(row) > text.index(
            "tests/test_type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743.py"
        )

    def test_architecture_label(self):
        block = _block()
        assert "Type C #999" in block or "iteration: 999" in block


class TestIterationLog999:
    def _entry(self):
        text = (REPO / "iteration-log.md").read_text(encoding="utf-8")
        return text.split("## #999")[1].split("## #998")[0]

    def test_newest_entry_is_999_prepended(self):
        headings = [
            line
            for line in (REPO / "iteration-log.md").read_text(encoding="utf-8").splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #999")

    def test_entry_mentions_new_mechanism_id_and_yelp(self):
        entry = self._entry().lower()
        assert "mechanism 831" in entry
        assert "yelp" in entry
        assert "995-999" in entry

    def test_entry_date_is_friday_18_00(self):
        entry = self._entry()
        assert "Sep 25 2026, 18:00 PDT" in entry

    def test_hash_placeholders_filled_post_followup(self):
        entry = self._entry()
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness999:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        for path in CONCURRENCY_UNTOUCHED:
            assert path not in staged, path
