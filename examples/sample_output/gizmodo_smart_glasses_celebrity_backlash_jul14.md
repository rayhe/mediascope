# Gizmodo: "Smart Glasses Backlash Is Reaching New Celebrity Heights"

**Publication:** Gizmodo
**Date:** July 14, 2026
**URL:** https://gizmodo.com/smart-glasses-backlash-is-reaching-new-celebrity-heights-2000784767
**Author:** (Not visible in fetched text)
**Topic:** Smart glasses privacy/cultural backlash

## Full Article Text

Smart glasses are, without argument, more popular than they've ever been. Meta alone has sold millions of pairs, and even Apple is reportedly interested in the category, with Google and Samsung waiting in the wings. But for each step smart glasses take towards going mainstream, there are just as many people taking a step (or several) back, and some of those people are actual celebrities.

Here's Lorde talking a whole lot of sh*t during a recent performance about said smart glasses:

> lorde saying fuck meta glasses in a festival that was sponsored by rayban meta AI glasses how can you not love her pic.twitter.com/HWsHZHP9AE

> — ana ✿ (@livinings) July 10, 2026

"Can I just say, for the record, f*ck the glasses," Lorde said on stage after lamenting the fact that it's difficult to tell when someone is wearing normal glasses or smart glasses with a camera on them.

The sentiment isn't particularly novel—plenty of people are averse to the idea of smart glasses—but rarely have we seen this level of backlash on a stage that isn't overtly political or backed by an advocacy group. The comments also feel especially pointed given the fact that we just saw arguably the biggest celebrity smart glasses co-sign by Kylie Jenner, who helped design a version of Meta's smart glasses called the Starfire Kylie Edition. Those glasses have been the center of a major ad push involving Jenner, which has helped cement Meta's smart glasses on an even more mainstream level.

Lorde isn't alone in the celebrity world in pushing back against smart glasses. Tyler the Creator recently blasted Ray-Ban Meta AI glasses on Instagram, writing, "Anyone who uses these glasses is a real weirdo," linking to an article from Wired about smart glasses and surveillance.

What's most interesting about the celebrity backlash against smart glasses is the potential implications. Way back in 2013, when Google tried, and failed, to force Google Glass onto the scene, the proverbial nail in the coffin wasn't regulation, policy, or anything even remotely official; it was social perception. People didn't buy Google Glass in large part because they didn't want to be perceived as a "glasshole." And in terms of swaying public opinion, celebrities are far more likely to move the needle than, say, the New York court system.

The question is, whose stance will win out? Kylie's or Lorde's?

## Manual Analysis

### 1. Entity Detection

**Primary entities:**
- **Meta** — smart glasses manufacturer (negative framing context)
- **Lorde** — musician, anti-glasses advocate
- **Kylie Jenner** — celebrity, pro-glasses endorser (Starfire Kylie Edition)
- **Tyler the Creator** — musician, anti-glasses advocate
- **Apple** — competitor (neutral mention)
- **Google** — competitor + Google Glass historical failure (used as precedent)
- **Samsung** — competitor (neutral mention)
- **Ray-Ban** — co-brand for Meta glasses
- **Wired** — cited publication (Tyler linked to Wired article)

**Entity gaps to check:**
- "Starfire Kylie Edition" — product name, may not be in entity clusters
- "Google Glass" — historical product, should link to Google entity cluster
- "Ray-Ban Meta AI glasses" — product name variant

### 2. Tone & Sentiment

**Overall tone:** Adversarial toward Meta's smart glasses project
**Emotional intensity:** Moderate-high (profanity from Lorde, "weirdo" from Tyler)
**Agency attribution:** Meta presented as commercial aggressor ("flooding the market"), celebrities as organic resistance

The article's editorial voice is clearly sympathetic to the anti-glasses position. The structure gives ~70% space to anti-glasses voices (Lorde, Tyler) vs ~30% to the pro-glasses position (Kylie, mentioned only as context).

### 3. Framing Devices Detected

| # | Device | Evidence |
|---|--------|----------|
| 43 | **Precedent Analogy** | "Way back in 2013, when Google tried, and failed, to force Google Glass onto the scene" — imports Google Glass failure as precedent for Meta |
| 24 | **Juxtaposition** | Kylie Jenner (pro) vs Lorde (anti) explicitly contrasted; "whose stance will win out?" |
| 9 | **Social Proof Amplification** | Implicit — Lorde's statement at a festival (large audience), Tyler's Instagram post (large following) |
| 14 | **Editorial Dramatization** | "talking a whole lot of sh*t" — editorial register break, informal amplification |
| 13 | **Editorial Aside** | "and some of those people are actual celebrities" — direct reader address, emphasis on celebrity status |
| 34 | **Competitive Positioning** | "Apple is reportedly interested in the category, with Google and Samsung waiting in the wings" — normalizes competitor entry |
| 52 | **Policy Reversal** (partial) | Not explicit, but the "glasshole" narrative implies Meta's push is repeating a known-failed pattern |
| 22 | **Kicker Framing** | "The question is, whose stance will win out? Kylie's or Lorde's?" — structures conclusion as a binary contest, implying the anti-glasses stance has equal or greater weight |

**Potential new/undetected devices:**
1. **Celebrity Authority Framing** — Celebrities cited as cultural opinion leaders whose stance determines market outcomes. Different from Expert Consensus Authority (#5) because these aren't domain experts; their power is cultural influence, not domain knowledge. "In terms of swaying public opinion, celebrities are far more likely to move the needle than, say, the New York court system."
2. **Cultural Death Precedent** — Google Glass failure attributed to social perception rather than regulation or technology. This imports a specific causal theory (cultural rejection > regulatory rejection) as established fact. Not quite Precedent Analogy (#43) because it doesn't just compare — it asserts a specific causal mechanism.
3. **Sponsorship Irony** — "a festival that was sponsored by rayban meta AI glasses" — the embedded tweet highlights the irony that Lorde criticized glasses at a sponsored event. This is a form of hypocrisy frame, but applied to the brand, not the critic.

### 4. Source Analysis

| Source | Stance | Type |
|--------|--------|------|
| Lorde | Adversarial | Celebrity, direct quote |
| Tyler the Creator | Adversarial | Celebrity, paraphrased |
| Kylie Jenner | Supportive | Celebrity, no direct quote (described as co-designer) |
| @livinings (ana ✿) | Adversarial | Social media user, embedded tweet |
| Wired | Adversarial | Publication (Tyler linked to article about surveillance) |

**Source balance:** 3:1 adversarial-to-supportive. No Meta spokesperson. No industry analyst. No privacy expert. No supportive user.

**Critical gap:** No Meta response quoted or even noted as absent. The article doesn't use "declined to comment" or similar — Meta is simply not given a voice. This is a form of **Selective Omission Signal** (#72) but more subtle than the typical "did not respond to request for comment" pattern.

### 5. Toolkit Gap Identification

1. **Celebrity/Influencer as Authority Source:** The toolkit's source stance analysis recognizes named experts and organizations but may not correctly classify celebrities as opinion-authority sources with outsized influence attribution. The article treats Lorde and Tyler as cultural gatekeepers whose endorsement or rejection can determine market outcomes — this is different from how the toolkit handles tech analysts or privacy advocates.

2. **Embedded Tweet Entity Extraction:** The embedded tweet from @livinings contains the key context that this was a "festival that was sponsored by rayban meta AI glasses" — this sponsorship detail is editorial gold (irony framing) but it comes from within an embedded tweet, which many entity extractors might skip.

3. **Profanity as Emotional Intensity Signal:** "f*ck the glasses" and "a real weirdo" — these are direct emotional language signals but use censored profanity ("sh*t", "f*ck") that the toolkit's emotional language matcher may not detect due to asterisk censoring.

4. **Binary Kicker Construction:** The closing "whose stance will win out? Kylie's or Lorde's?" is a specific kicker pattern that structures the conclusion as a binary cultural contest. The existing Kicker Framing (#22) detects "negative note unrelated to main topic" but this is a different pattern — it's a structured binary choice that privileges one side through article architecture.
