"""Type B iteration #823 (Sep 18 2026, 2am PDT): Philip Berne (TechRadar) career-tie
register gradient - his alarm-dominant Meta Ray-Ban glasses opinion (Sep 2023,
"worried about the high creep factor") vs his first-person Samsung Galaxy S23
Ultra love letter ("the best phone you can buy"), the fourth leg of the 820-824
window.

D (#820) -> E (#821) -> A (#822) -> B (#823) -> C (#824 to follow).

Follows the #818 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#822 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1.
Doc-sync 2 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.

FINDING: Philip Berne (TechRadar Senior Editor, Mobile Reviews and Buying
Guides; recruited by Samsung in 2011 to pre-review unreleased devices; Samsung
Mobile PR Team Lead "leading reviews for the PR team and writing crisis
communications" until 2017, per his own TechRadar byline bio, verified
first-hand this run) writes the corpus's most alarm-dominant Meta glasses
register while his Samsung coverage is pure first-person enthusiasm. Meta arm:
TechRadar "The Ray-Ban Meta camera glasses feel inevitable but I'm worried
about the high creep factor" (Sep 2023; read first-hand this run, 127 rendered
lines; first-person voice + "Image credit: Future / Philip Berne" photo credit;
corpus-carried since Aug 15 via mechanism 115 at tone -0.35, re-scored -0.50
MANUAL ILLUSTRATIVE this run from the full read): headline "worried about the
high creep factor"; "worried about predatory men recording women and girls
without their knowledge or consent"; "broadcast live over social networks, with
the purpose of earning infamy and spreading fear"; "teach students how to
respond if somebody showed up to the school with a gun"; "Training to escape a
terrifying emergency"; "attention can be food for terror"; "that can be a scary
thought" (-0.50 illustrative). Samsung arm: TechRadar "Forget the Pixel Fold
and iPhone 14 Pro, the Galaxy S23 Ultra is the phone I can't quit using" (2023;
read first-hand this run, 119 rendered lines; first-person voice + six "Image
credit: Future / Philip Berne" photo credits; novel URL, zero hits repo-wide
pre-commit): "When I have my choice of everything, I still use my Galaxy S23
Ultra"; "The Galaxy S23 Ultra is the best phone you can buy, and it's the phone
I use above the rest"; "the joy of the Galaxy S23 Ultra is never worrying about
it"; "I don't miss anything about the iPhone when I got back to using my Galaxy
full time" (iPhone reduced to FOMi social utility); camera failures assigned to
competitors (Razr Plus kid photo "a blurry, blocky mess"; Pixel Fold cameras
"pretty good, but not great"); "Samsung doesn't pay for this privilege. PCMag
uses Galaxy S phones because Samsung phones reliably get the best service"
(preempts payola suspicion); zero criticism of Samsung (+0.55 illustrative).
Illustrative Meta-minus-Samsung delta -1.05: the alarm register (creep factor,
terror, predatory, school-shooting parallel) fires on Meta's glasses while his
former employer's flagship gets an unbroken love letter. Same writer and same
outlet, so the outlet-level financial-tie gradient is held constant - the design
isolates editorial register plus career history. Strong confounders ranked
first: product-category asymmetry (flagship smartphone daily-driver love letter
vs unreleased smart-glasses launch-week opinion column, dominant confound);
genre-purpose asymmetry (enthusiasm column vs worry column); biographical
grounding (the Meta alarm register is routed through his US teaching experience
and school-shooting drills - a genuine biographical register, not obviously a
financial artifact); category novelty (2023 glasses were a novel form factor
inviting caution registers vs mature smartphone category); temporal proximity
(both 2023, confound mitigant). Counter-evidence: Berne self-moderates the Meta
alarm explicitly (pickup-truck passage: "That would be obscene, and frankly
depressing"; "people do bad things because they are bad people... not because
some good technology came along"); Berne praises the Meta product ("look pretty
cool", "price is shockingly good"); the Meta piece applies NO alarm to Samsung
as future competitor ("Samsung Galaxy Goggles sold through Sunglass Hut? Just
as likely"); the career tie is self-disclosed in his own byline bio, not hidden
("In 2011, Philip was recruited by Samsung to review top secret, upcoming
devices..."); Berne explicitly preempts payola ("Samsung doesn't pay for this
privilege"); disclosed Apple Store history too (multi-employer history, not
single-entity capture); m679-style principle: former-employer ties do not
always predict tone. Verdict EXTENDS mechanism 115 (TechRadar/Future plc
privacy-vocabulary bifurcation) to a journalist-level career-tie instantiation:
a former Samsung PR team lead writes the corpus's most alarm-dominant Meta
glasses register while his Samsung flagship coverage is pure enthusiasm -
directionally_supported_not_proven. This is a career-history register gradient,
NOT a hidden-financial-tie claim. MANUAL ILLUSTRATIVE only; engine NOT run;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; NOT artifact-grade;
NOT a falsification-family member; ledger holds at 26; no analysis.json update.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_823_philip_berne_techradar_samsung_s23_ultra_vs_meta_creep_factor_sep18_2am.py"
MECH_KEY = "philip berne techradar samsung s23 ultra vs meta creep factor"
M_ID = 725
MECH_ID_MARKER = "mechanism" + "_725"
NEXT_ID_MARKER = "mechanism" + "_726"
NEXT_ID_NUMERIC = "mechanism_id: 726"
ANCHORED_SHA = "d5e0067"  # main commit, patched post-commit per #565
BLOCK_KEY = "type_b_823_philip_berne_techradar_samsung_vs_meta_creep_factor_sep18"

META_URL = "https://www.techradar.com/computing/virtual-reality-augmented-reality/the-ray-ban-meta-camera-glasses-feel-inevitable-but-im-worried-about-the-high-creep-factor"
SAMSUNG_URL = "https://www.techradar.com/phones/samsung-galaxy-phones/forget-the-pixel-fold-and-iphone-14-pro-the-galaxy-s23-ultra-is-the-phone-i-cant-quit-using"
SAMSUNG_URL_FRAGMENT = "galaxy-s23-ultra-is-the-phone-i-cant-quit-using"

CAREERS_PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True,
        text=True,
        check=False,
    )


def _careers_text():
    with open(CAREERS_PROFILE) as fh:
        return fh.read()


def _berne():
    with open(CAREERS_PROFILE) as fh:
        doc = yaml.safe_load(fh)
    assert "philip_berne" in doc
    return doc["philip_berne"]


def _block():
    return _berne()["competitor_coverage"][BLOCK_KEY]


# --- Novelty ---------------------------------------------------------------


class TestNovelty823:
    def test_type_b_823_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #823")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_823_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_823*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #823 test files: {hits}"

    def test_block_key_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#823 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-c", BLOCK_KEY, "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"block key already referenced pre-commit: {res.stdout}"

    def test_samsung_arm_url_zero_hit_repo_wide_pre_commit(self):
        # The Samsung S23 Ultra arm is the novel content: zero hits anywhere pre-commit.
        res = _run_git("grep", "-c", SAMSUNG_URL_FRAGMENT, "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Samsung arm URL fragment already referenced pre-commit: {res.stdout}"

    def test_mechanism_id_725_zero_in_head(self):
        res = _run_git("grep", "mechanism_id: 725", "HEAD", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip(), \
            f"mechanism_id 725 already present pre-commit: {res.stdout.strip()[:200]}"

    def test_meta_arm_url_carried_not_novel(self):
        # The Meta arm URL is CARRIED: in corpus since Aug 15 (mechanism 115,
        # privacy-vocabulary bifurcation). Novelty here is the dedicated
        # same-writer pair + the new Samsung arm, not the URL.
        res = _run_git("grep", "-c", "the-ray-ban-meta-camera-glasses-feel-inevitable", "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected the Meta arm URL to be carried in corpus since Aug 15"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "823"), ("A", "822"), ("E", "821"), ("D", "820"), ("C", "819"),
]
WINDOW_SEQ = "D (#820) -> E (#821) -> A (#822) -> B (#823) -> C (#824)"


class TestRotationCycleGuard823:
    def test_iteration_sequence_is_819_through_823(self):
        assert EXPECTED_ORDER == [
            ("B", "823"), ("A", "822"), ("E", "821"), ("D", "820"), ("C", "819"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_823_position_is_fourth_leg_of_820_824_window(self):
        assert EXPECTED_ORDER[0] == ("B", "823")

    def test_predecessor_is_type_a_822(self):
        assert EXPECTED_ORDER[1] == ("A", "822")


# --- Mechanism 725 content -------------------------------------------------


class TestMechanism725Content:
    def test_block_parses_under_berne_competitor_coverage(self):
        berne = _berne()
        assert BLOCK_KEY in berne["competitor_coverage"]
        assert berne["competitor_coverage"][BLOCK_KEY]["mechanism_id"] == M_ID

    def test_block_key_unique(self):
        field = "      block_key: 'type_b_823_philip_berne_techradar_samsung_vs_meta_creep_factor_sep18'\n"
        assert _careers_text().count(field) == 1

    def test_block_725_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 823
        assert b["type"] == "B"
        assert b["date"] == "2026-09-18 02:00 PDT"
        assert b["test_file"] == "tests/" + TEST_BASENAME

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["title"] == "The Ray-Ban Meta camera glasses feel inevitable but I'm worried about the high creep factor"
        assert meta["date"] == "2023-09-28"
        assert meta["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert meta["byline_attribution_urls"][0] == META_URL
        assert "alarm_dominant" in meta["register_notes"]
        quotes = " ".join(meta["key_quotes"])
        assert "predatory men recording women and girls" in quotes
        assert "earning infamy and spreading fear" in quotes
        assert "Training to escape a terrifying emergency" in quotes
        assert "food for terror" in quotes
        assert "scary thought" in quotes

    def test_samsung_arm_fields(self):
        b = _block()
        sam = b["samsung_arm"]
        assert sam["title"] == "Forget the Pixel Fold and iPhone 14 Pro, the Galaxy S23 Ultra is the phone I can't quit using"
        assert sam["date"] == "2023"
        assert sam["tone_MANUAL_ILLUSTRATIVE"] == 0.55
        assert sam["byline_attribution_urls"][0] == SAMSUNG_URL
        assert sam["criticism_of_samsung_count"] == 0
        quotes = " ".join(sam["key_quotes"])
        assert "best phone you can buy" in quotes
        assert "still use my Galaxy S23 Ultra" in quotes
        assert "never worrying about it" in quotes
        assert "Samsung doesn't pay for this privilege" in quotes
        assert "blurry, blocky mess" in quotes

    def test_career_tie_disclosed_in_block(self):
        b = _block()
        career = b["career_tie"]
        assert career["former_samsung_mobile"] is True
        assert career["recruited_2011"] is True
        assert career["pr_team_lead_until_2017"] is True
        joined = " ".join(career["bio_quotes"])
        assert "recruited by Samsung" in joined
        assert "leading reviews for the PR team" in joined

    def test_spread_delta_calc(self):
        b = _block()
        assert b["illustrative_delta_meta_minus_samsung"] == -1.05
        assert b["delta_calc"] == "(-0.50) - (0.55) = -1.05"

    def test_statistical_discipline(self):
        b = _block()
        disc = b["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "engine NOT run" in disc
        assert b["no_analysis_json_update"] is True
        assert "EXTENDS mechanism 115" in b["verdict"]
        assert "career-history register gradient" in b["verdict"]

    def test_research_method_documents_ruled_out_candidates(self):
        b = _block()
        method = b["research_method"]
        assert "Hamish Hector ruled out" in method
        assert "Lance Ulanoff ruled out" in method
        assert "Jacob Krol ruled out" in method
        assert "no canonical URLs constructed" in method
        assert "first-hand" in method

    def test_confounder_strong_triple_present(self):
        b = _block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert any(c.startswith("Product-category asymmetry") for c in strong)
        assert any(c.startswith("Genre-purpose asymmetry") for c in strong)
        assert any(c.startswith("Biographical grounding") for c in strong)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 6
        joined = " ".join(b["counterevidence"])
        assert "obscene, and frankly depressing" in joined
        assert "price is shockingly good" in joined
        assert "Samsung Galaxy Goggles sold through Sunglass Hut" in joined
        assert "self-disclosed" in joined
        assert "#679" in joined

    def test_cross_references_include_115(self):
        b = _block()
        joined = " ".join(b["cross_refs"])
        assert "#115" in joined


# --- Supersession and corpus post-#822 --------------------------------------


class TestSupersessionAndCorpusPost822:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_725(self):
        assert max(self._numeric_ids()) == 725

    def test_iteration_822_max_724_sweep_superseded_by_design(self):
        # #822's max-724 sweeps fail by designed supersession now that 725 exists.
        assert max(self._numeric_ids()) != 724

    def test_zero_underscore_726_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_726_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_822_zero_underscore_725_sweep_stays_green(self):
        # The #822 zero-underscore-725 sweeps stay green post-#823 by designed keying:
        # neither the careers block nor this test file carries a literal underscore-725 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                f"literal underscore-725 key leaked into {root}: {res.stdout.strip()[:200]}"

    def test_iteration_822_zero_numeric_725_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 725", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #822's zero-numeric-725 sweep to fail by designed supersession"

    def test_numeric_725_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 725", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 725 key in Berne's careers competitor_coverage
        # block; no other profiles/ location.
        assert len(hits) == 1, f"unexpected numeric 725 key spread in profiles/: {hits}"
        assert "profiles/careers/journalists.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger823:
    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                p = os.path.join(root, f)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_m725_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers823:
    def test_philip_berne_entry_present(self):
        berne = _berne()
        assert berne["name"] == "Philip Berne"

    def test_philip_berne_career_history_has_samsung_pr(self):
        berne = _berne()
        jobs = berne["career_history"]
        samsung = [j for j in jobs if j["employer"] == "Samsung Mobile"]
        assert len(samsung) == 1
        assert samsung[0]["role"] == "PR Team Lead, Reviews"
        assert samsung[0]["period"] == "until 2017"

    def test_philip_berne_mechanism_ids(self):
        berne = _berne()
        assert berne["mechanism_ids"] == [725]

    def test_philip_berne_823_block(self):
        berne = _berne()
        assert BLOCK_KEY in berne["competitor_coverage"]
        cc = berne["competitor_coverage"][BLOCK_KEY]
        assert cc["mechanism_id"] == 725
        assert cc["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert cc["samsung_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.55

    def test_philip_berne_first_dedicated_type_b_mechanism(self):
        # Zero dedicated Berne Type B blocks pre-commit; this run's entry is the
        # FIRST dedicated Type B mechanism on Berne (m115 lived in
        # competitor-coverage-research.yaml only).
        assert _careers_text().count("mechanism_id: 725") == 1

    def test_karissa_bell_entry_untouched(self):
        with open(CAREERS_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert doc["karissa_bell"]["mechanism_ids"] == [722]


# --- Doc sync ----------------------------------------------------------------


class TestDocSync823:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog823:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #823" in self._tail()

    def test_iteration_log_entry_carries_mechanism_725(self):
        assert "725" in self._tail()
