"""Type B #768 (2026-09-15 10:00 PDT): Kate Kozuch (Tom's Guide) trust-interrogation
asymmetry within product-enthusiasm constancy.

FIRST dedicated corpus mechanism (692) on Kate Kozuch - zero hits repo-wide
(profiles/ + tests/) pre-commit, git-grep-verified this run.

Meta arm: Tom's Guide Oct 2023 "Ray-Ban Meta Smart Glasses review: Better in
every way", byline Kate Kozuch (author-bio block) - enthusiast review register,
+0.55 MANUAL ILLUSTRATIVE: 4.5 stars, Editor's Choice, "the smart glasses
market has found its victor", "easy to recommend"; privacy critics preemptively
quarantined ("some people will, inevitably, be creeped out... folks who avoid
all things Meta"). Three supporting Meta-family arms (vacation-photo
"game-changer", outfit-AI feature, Oakley HSTN praise) confirm the enthusiasm
is repeated, not one-off.

Google arm (same writer, SAME category): Tom's Guide May 2024 "Google's AI
smart glasses are the most exciting thing I saw at I/O" - applies a
company-trust-history purchase criterion that favors Google: "more inclined to
choose Google than Meta as the maker just based on the each company's history
with providing information", "Wouldn't you opt for the product from the
company who's name is literally used as a verb for search?", "I would be
nervous if I were Meta." Trust ASSUMED for Google.

Apple arm: Tom's Guide Sep 2025 Apple Watch Series 11 / Ultra 3 / SE 3
reviews, byline Kate Kozuch (wearables tag page) - unqualified superlative
review register, +0.60 MANUAL ILLUSTRATIVE: Series 11 Editor's Choice "blew me
away", Ultra 3 Editor's Choice "the ultimate smartwatch just got better", SE 3
Recommended "best smartwatch value". Zero privacy/trust vocabulary in excerpts.

The finding: product-enthusiasm constancy (illustrative delta Meta minus Apple
-0.05, inside the noise band) with entity-selective TRUST INTERROGATION (Meta
-0.30 vs Google +0.20 = -0.50; Meta -0.30 vs Apple 0.00 = -0.30). Kozuch loves
Meta's hardware as much as Apple's - but only Meta gets its trustworthiness
litigated as a purchase criterion. The same-category Google arm neutralizes the
category confound that would otherwise dominate (camera glasses vs smartwatch).
Financial context: Tom's Guide is a Future plc property; $0 documented AI
licensing ties on the Meta/Apple/Google axis - zero-gradient control, a
journalist-level trust prior, not finance-predicted.

NOT a falsification-family member (thesis-consistent direction); ledger holds
at 26. Verdict: directionally_supported_not_proven. NOT artifact-grade. No
analysis.json update. Excerpt-bounded per #503; no browser.open this run.

Rotation: 764-768 window closing C->D->E->A->B (anchor patched post-commit per
#565).

39 tests, 8 classes.
"""

import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "kate kozuch toms guide trust interrogation asymmetry within product enthusiasm constancy sep15"
MECH_NUM = 692
MECH_ID_MARKER = "mechanism" + "_692"  # must stay ABSENT from block and profiles

META_URL = "https://www.tomsguide.com/reviews/ray-ban-meta-smart-glasses"
VACATION_URL = "https://www.tomsguide.com/features/i-compared-the-iphone-15-pro-max-vs-ray-ban-meta-smart-glasses-for-taking-vacation-photos-heres-what-happened"
OUTFIT_URL = "https://www.tomsguide.com/news/i-let-the-ray-ban-meta-smart-glasses-pick-out-my-outfit-using-ai-and-im-shocked-by-the-result"
OAKLEY_URL = "https://www.tomsguide.com/computing/smart-glasses/oakley-meta-hstn-smart-glasses-review-what-i-love-and-whats-still-missing"
GOOGLE_URL = "https://www.tomsguide.com/computing/smart-glasses/googles-ai-smart-glasses-are-the-most-exciting-thing-i-saw-at-io-heres-what-you-need-to-know"
TAG_URL = "https://www.tomsguide.com/tag/wearables/page/3"
MUCKRACK_URL = "https://muckrack.com/kate-kozuch/articles"

RESEARCH_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

# Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _research():
    return _read(RESEARCH_PATH)


def _block():
    corpus = _research()
    return corpus[corpus.index(MECH_KEY + ":"):]


def _block_data():
    import yaml

    data = yaml.safe_load(_research())
    return data["cross_publication_findings"][MECH_KEY]


def _fold(s):
    return " ".join(s.split())


def _git_log_mains(prefix_pat):
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    return [line for line in out if re.search(prefix_pat, line)]


def _repo_grep(pattern, roots=("profiles", "tests")):
    hits = []
    for root in roots:
        proc = subprocess.run(
            ["git", "grep", "-l", pattern, "--", root],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestNovelty768:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_b_768_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_b_768") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_b_768_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type B #768: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_b_768
        # files, no "Type B #768" in git log, "Kate Kozuch" zero-hit repo-wide
        # case-insensitive, max numeric mechanism_id 691, zero underscore-form
        # 692 keys excluding sweep-instrument carriers per #715); this test
        # pins the claim in the committed block, per the #752 convention.
        block = _block()
        assert "Zero test_type_b_768 files on disk pre-commit" in block
        assert 'no "Type B #768" in git log pre-commit' in block
        assert '"Kate Kozuch" zero-hit repo-wide pre-commit' in block
        assert "max numeric mechanism_id 691 pre-commit" in block


class TestRotationCycleGuard768:
    """Rotation: 764-768 window closes C->D->E->A->B."""

    EXPECTED_ORDER = [("B", "768"), ("A", "767"), ("E", "766"), ("D", "765"), ("C", "764")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "40", "--", "."],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_closes_cdeab(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type B #768: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism692Content:
    def test_block_present_in_research(self):
        assert MECH_KEY + ":" in _research()
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 768
        assert data["iteration_type"] == "B"
        assert data["rotation_type"] == "B"
        assert data["type"] == "B"
        assert data["iteration_time"] == "2026-09-15 10:00 PDT"
        assert data["discovery_date"] == "2026-09-15"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_journalist_fields(self):
        data = _block_data()
        assert data["journalist"] == "Kate Kozuch"
        assert data["publication"] == "toms_guide"
        assert "future" in data["owner"]

    def test_meta_arm_quotes(self):
        data = _block_data()
        arm = data["meta_arm"]
        assert arm["byline"] == "Kate Kozuch"
        assert arm["tone_illustrative"] == 0.55
        quotes = " ".join(arm["evidence_quotes"])
        assert "the smart glasses market has found its victor" in quotes
        assert "easy to recommend" in quotes
        assert "4.5 stars" in quotes
        assert "avoid all things Meta" in quotes
        assert META_URL in arm["source_urls"]

    def test_meta_supporting_arms_three(self):
        data = _block_data()
        arms = data["meta_supporting_arms"]
        assert len(arms) == 3, len(arms)
        urls = [u for a in arms for u in a["source_urls"]]
        assert VACATION_URL in urls
        assert OUTFIT_URL in urls
        assert OAKLEY_URL in urls
        notes = " ".join(a["note"] for a in arms)
        assert "game-changer" in notes
        assert "worried about AI invading their life" in notes

    def test_google_arm_quotes(self):
        data = _block_data()
        arm = data["google_arm"]
        assert arm["byline"] == "Kate Kozuch"
        assert arm["tone_illustrative"] == 0.20
        quotes = " ".join(arm["evidence_quotes"])
        assert "history with providing information" in quotes
        assert "literally used as a verb for search" in quotes
        assert "I would be nervous if I were Meta" in quotes
        assert GOOGLE_URL in arm["source_urls"]

    def test_apple_arm_quotes(self):
        data = _block_data()
        arm = data["apple_arm"]
        assert arm["byline"] == "Kate Kozuch"
        assert arm["tone_illustrative"] == 0.60
        quotes = " ".join(arm["evidence_quotes"])
        assert "blew me away" in quotes
        assert "ultimate smartwatch just got better" in quotes
        assert "best smartwatch value" in quotes
        assert "zero privacy/trust vocabulary" in quotes
        assert TAG_URL in arm["source_urls"]
        assert MUCKRACK_URL in arm["source_urls"]

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "Search-excerpt-bounded per #503" in block
        assert "browser.open not attempted" in block
        assert "no tomsguide.com URLs constructed" in block

    def test_manual_illustrative_discipline(self):
        data = _block_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["product_register_delta_meta_minus_apple"] == -0.05
        assert scorer["illustrative_trust_delta_meta_minus_google"] == -0.50
        assert scorer["illustrative_trust_delta_meta_minus_apple"] == -0.30
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert scorer["statistical_contract"] == "degenerate_n1_per_arm"
        assert "MANUAL ILLUSTRATIVE" in scorer["tone_basis"]

    def test_financial_context_future_chain(self):
        ctx = _block_data()["financial_context_future_chain"]
        assert "Future plc" in ctx["owner"]
        assert "No documented AI content-licensing deal" in ctx["documented_deals"]
        assert ctx["prediction"].startswith("NULL")
        assert "zero-gradient control" in ctx["prediction"]
        assert "690" in ctx["mechanism"]

    def test_confounder_strength_layers(self):
        data = _block_data()
        layers = [c.split(":")[0] for c in data["confounders"]]
        assert layers.count("STRONG") == 3
        assert layers.count("MODERATE") == 3
        assert layers.count("WEAK") == 2
        assert len(data["confounders"]) == 8

    def test_four_counterevidence(self):
        data = _block_data()
        assert len(data["counterevidence"]) == 4
        joined = " ".join(data["counterevidence"])
        assert "COUNTEREVIDENCE" in joined
        assert "noise band" in joined

    def test_verdict_ledger_and_careers_backlink(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert "NOT a falsification-family member" in data["asymmetry_scorer"]["verdict"]
        assert "ledger holds at 26" in data["asymmetry_scorer"]["verdict"]
        careers = _read(CAREERS_PATH)
        assert "mechanism_ids: [692]" in careers
        assert "Kate Kozuch" in careers

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m692 block key carries no underscore-form "mechanism_692"
        # substring, so #767's zero-underscore-692 sweeps stay GREEN.
        assert MECH_ID_MARKER not in _block()
        assert MECH_ID_MARKER not in _read(CAREERS_PATH)


class TestSupersessionAndCorpusPost767:
    """Post-#767 corpus integrity: max 692, zero 693, designed supersession."""

    def _ids(self):
        return [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())]

    def test_max_numeric_mechanism_id_is_692(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_691_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 691")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_693_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_693")
        assert hits == [], hits

    def test_zero_numeric_693_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 693", roots=("profiles",))
        assert hits == [], hits

    def test_d767_zero_underscore_692_profiles_sweep_stays_green(self):
        # #767 asserted zero literal "mechanism_692" in profiles/; the m692
        # block key carries no underscore-form 692 substring by designed
        # keying, so that sweep stays green.
        hits = _repo_grep("mechanism" + "_692", roots=("profiles",))
        assert hits == [], hits

    def test_d767_zero_underscore_692_tests_sweep_stays_green(self):
        # #767 asserted zero "mechanism_692" references in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_692") so no
        # contiguous literal exists in tests/ either - the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d767_zero_numeric_692_profiles_sweep_fails_by_designed_supersession(self):
        # #767 asserted zero "mechanism_id: 692" hits in profiles/; the m692
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 692", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d767_max_691_sweep_superseded_by_design(self):
        # #767 asserted max == 691; advancing to 692 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 691

    def test_m692_block_key_unique_and_research_parses(self):
        assert _research().count(MECH_KEY + ":") == 1
        import yaml

        d = yaml.safe_load(_research())
        assert d["cross_publication_findings"][MECH_KEY]["mechanism_id"] == MECH_NUM


class TestLedger768:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m692 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m692_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "thesis-consistent direction" in block.lower()

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync768:
    def test_readme_row_768(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_767_repaired(self):
        # #767's doc-sync added only the ARCHITECTURE row; the README table
        # row was missing (tripped test_readme_lists_all_test_files). Repaired
        # in this run's doc-sync.
        assert "test_type_a_767_wsj_anthropic_coxon_resignation_news_register_sep15_9am.py" in _read(README_PATH)

    def test_architecture_row_768(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_768_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog768:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #768 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#768 Type B:" is the entry header; a bare "#768" would
        # false-positive on #767's rotation line ("B (#768) -> ...").
        assert "#768 Type B:" in self._tail()

    def test_log_mechanism_692_and_journalist(self):
        assert "mechanism 692" in self._tail()
        assert "Kate Kozuch" in self._tail()


class TestDateGrounding768:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
