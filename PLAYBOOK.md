# Mike Salemi email playbook (knowledge base)

Built 21 Nov 2026 from all 1,042 retained Kartra emails (922 broadcasts, 104 sequence steps, 16 notifications). Rebuild with `scripts/analysis/build_knowledge.py`.

## How to read the numbers

- **Main cohort = 406 "broad" broadcasts** (sent to 500+ people, 2019-2025, 1,500-3,250 recipients each). The 515 sends to small segments (median 26 people, mostly 2020-2022 customer/program emails) inflate rates and are kept separate.
- **Click index** = an email's click rate ÷ the median click rate of broad emails sent the *same year*. 1.00 = typical for its year, 1.50 = 50% more clicks than typical. This removes the big year-to-year swings (median broad click rate: 2019 1.1%, 2020-22 ~3-6%, 2023 0.6%, 2024 0.7%, 2025 2.3%).
- **Opens are almost useless as a signal.** Open index stays between 0.95 and 1.07 for every grouping below (Apple Mail privacy auto-opens since 2021). Judge subject lines and timing by **clicks**, not opens.
- **Revenue** = Kartra's per-email revenue field (USD). It credits the email that got the last click and is not reconciled sales, but it is the only per-email money signal. The total across all broadcasts is $42,997, and $37,749 of it comes from the 406 broad emails.

## The 10 things that matter most

1. **Physical how-to emails are the engine.** Short emails built around one exercise or stretch with one video link ("Kettlebell Halo: Use These Progressions", "Try This Variation - The Coiled Kettlebell Swing", "Use this DEEP Hip Stretch to Alleviate Low Back Pain") have a median **click index of 1.33** (109 emails) and many of the archive's best click rates (5-8%). This is what the list signed up for.
2. **Podcast announcements are the weakest email Mike sends.** There are 134 "[🎙️NEW EP.]" emails, a third of all broad sends. They have a median click index of 0.80 and earned **$197 in total**. Most are on Thursday, which is why Thursday looked bad until podcasts were removed. Recommendation: fold the episode into a value email or the P.S. instead of a standalone send.
3. **Abstract men's-work essays don't get clicks.** The bottom of the archive is reflective essays with no concrete hook, e.g. "You weren't made for a world of noise." (0.04%) and "the cost of keeping everyone happy but yourself" (0.12%). Men's-work topics *can* work (B1098 "Men, The Key to True Strength", index 4.4), but they win when they open with a concrete personal story and give one specific invitation.
4. **Money comes from the kettlebell/movement products, not the men's coaching products.** Revenue field by offer mentioned in the email:

   | Offer | Emails | Active | Revenue field | Click index |
   |---|---:|---|---:|---:|
   | Kettlebell Lifestyle | 62 | 2020-2024 | $19,984 | 1.30 |
   | Mastering the Kettlebell (MTK) | 25 | 2019-2025 | $14,972 | 2.09 |
   | Bulgarian Bag program (Athleticism for Life) | 16 | 2023-2025 | $5,738 | 1.77 |
   | Hold Your Ground / Men of Movement retreat | 120 | 2021-2025 | $5,275 | 0.97 |
   | Somatic breathwork | 45 | 2020-2025 | $3,343 | 1.32 |
   | Path to Inspired Action (group coaching) | 62 | 2020-2024 | $3,229 | 0.95 |
   | 1:1 Mentorship / coaching | 34 | 2020-2025 | $3,140 | 1.15 |
   | Enneagram | 15 | 2023-2025 | $881 | 2.01 |
   | Primal Reset Retreat | 23 | 2024-2025 | $433 | 0.96 |
   | Vital Man Collective | 31 | 2025 | $0 | 0.76 |

   (An email can mention more than one offer, so the rows overlap.) B532 "Just for Men - Hold Your Ground Retreat" carries a single $4,000 field, so retreat revenue is one sale, not a trend. Retreats are high-ticket and sold by conversation, so the revenue field undercounts them.
5. **Deadline/offer emails make the money.** Promo and deadline emails (64) have click index 1.16 and $21,674 revenue field, 57% of broad-email revenue from 16% of sends. Top earners: B86 "$500 coupon" ($2,982), B1004 Bulgarian Bag pre-order ($2,674), B99 "life is what you make it!" ($2,619, a story-led launch), B608 "Special Offer … Ends Tomorrow" ($1,994), B950 "4 Hours Remaining" ($1,750). Discount language: click index 1.40 vs 1.09 without (non-podcast).
6. **Shorter wins clicks.** Non-podcast broad emails by body length (click index): under 150 words 1.91 · 150-300 1.25 · 300-500 1.05 · 500-800 1.00 · 800+ 0.24. Revenue peaks at 300-500 words ($18,004), where launch emails have room to explain the offer.
7. **Number of links:** one link earns most of the revenue ($23,342 across 106 emails). Emails with 2-4 links get the most clicks (index 1.80), but extra links spread clicks around rather than sell. Rule: one primary CTA, repeated; secondary links only in the P.S.
8. **The P.S. works.** Non-podcast emails with a P.S. have click index 1.49 vs 1.03 without. Mike uses the P.S. as the "soft sell" slot (an early-bird reminder under a free stretch video, as in B1087).
9. **Timing is a second-order lever.** Weekdays without podcasts, by click index: Wed 1.33 · Sat 1.33 · Thu 1.31 · Fri 1.19 · Sun 1.11 · Mon 1.09 · **Tue 0.94** (the weakest). Hour (Pacific): 00-06 1.80 (n=32; early sends sit at the top of the inbox) · 10-15 ~1.17 · 07-09 1.00. Revenue-heavy sends cluster 16:00-18:00 ($12,546) because deadline emails go out late afternoon.
10. **Cadence:** after an 8+ day gap, the next email gets click index 1.27; 4-7 day gaps 0.91. Two sends on the same day raise unsubscribes (index 1.23). Mike's normal rhythm is 2-3 days apart.

## Subject lines (non-podcast broad emails, by click index)

- **Name the specific thing:** "how to / this / these + exercise or outcome" scores 1.48 (n=28). Examples: "The BEST At Home Band Exercise" (7.7% CTR), "Build Athleticism With These 2 Kettlebell Exercises!", "Like a bench press, but WAY more athletic...KB Swiss Ball Drop & Recover!"
- **One CAPS word for emphasis** scores 1.31 (n=48): "DEEP", "BEST", "WAY", "BIG".
- **A number** scores 1.18: "2 Kettlebell Exercises", "4 Hours Remaining", "$500 coupon".
- **Body outcome or pain point:** "Alleviate Low Back Pain", "My Back Stiffness is Gone" (a customer quote as the subject).
- **Avoid:** ellipsis teasers ("Why Men Lie Awake at Night...") score 0.75; vague abstract lines; [🎙️NEW EP.] brackets; questions (0.78); "[ ]" tags on non-promo emails.
- **{first_name} in the subject** was used 5 times. Two of them were big money emails (B86, B99), but it also raised unsubscribes (index 1.49). Save it for launches.
- **Length:** 40-55 characters is the best bucket (1.18).

## Mike's voice

### Who he is in the emails
A movement coach (kettlebells, Bulgarian bag, mobility, breathwork) who grew into a men's leadership coach and podcast host. He writes as a peer and a coach, not a guru: enthusiastic, earnest, a bit goofy when excited, grateful to his readers. Sign-offs evolved from "Train intentionally," (training era) to "Yours in Health & Happiness," / "With love and respect," (men's-work era).

### Structure he actually uses
1. **Greeting:** "Hi {first_name}," (212 of 272 non-podcast broad emails). Sometimes "Hey {first_name}," or "Hello {first_name},". Never "Dear".
2. **Opening line, one of four moves:**
   - a recent real moment: "Recently, I led a recovery workshop for the Santa Clara County Sheriff's Department…", "Since returning home from Kuwait last week…", "Yesterday, my wife and…"
   - a principle stated plainly: "Exercise progressions are there to help methodically and intentionally make your body 'smarter.'"
   - a confession or hook: "I'm crazy...let's just get that out on the table.", "There was a time when thinking about strength, all that mattered to me was the number on the bar…"
   - straight to the news: "The day has come!"
3. **One idea in short paragraphs.** Mostly 1-2 sentences per paragraph, median sentence 16 words, lots of white space.
4. **A concrete example or image**, e.g. "it's cool to do a standing broad jump. But if you … stick the landing on a narrow balance beam…"
5. **One CTA, written as a natural sentence:** "Click here and add these progressions…", "You can check out the video here.", "By clicking here you'll get to learn more…". Benefit-led, never "CLICK NOW".
6. **A warm, personal close:** "Let me know if you try it out and how it goes for you!", "I'll see you inside!", "Hope to see you there!"
7. **Sign-off:** "Train intentionally," / "Best," / "Best regards," / "Yours in Health & Happiness," / "With love and respect," then "Mike" or "Mike Salemi".
8. **P.S.** with the offer or deadline: "P.S. This week is the final week for men to inquire about early bird pricing…"

### Signature words and phrases
- train intentionally · move well and feel well for a lifetime · athleticism / athletic for life · smarter body · balanced warriors · joint mobility · "working in" · follow-along video · progressions
- men's work: hold your ground · inspired action · brotherhood · vulnerability is courage · true strength · "for men to thrive" · intentional discomfort
- excitement markers: "Let's goooooo!", "Buuuuuuut", "haha", "beyond excited", "literally have goosebumps", "heck no!"
- gratitude: "For this, I am incredibly grateful…it means a lot."
- reader address: "If you've been a follower of my work for a while, you know…", "If you're like me,", "I don't know about you, but…"

### Sales style
- Launches: story → mission → bullet list of exactly what you get (videos, calls, lifetime access, guarantee) → price/coupon → scarcity that is real (spots, hours) → "I'll see you inside!"
- Deadlines: short, factual, countdown subject ("Final 5 Hours to Save 50%+ on ALL Online Programs").
- He states product specifics (400+ videos, 30-day money-back guarantee, code TEAMSALEMI10). **Never invent codes, prices, dates or guarantees.** Ask for them.

### Do / don't when writing as Mike
- **Do:** one idea; a real moment or concrete movement cue; short paragraphs; one CTA link phrased as a benefit; the P.S. for the offer; warm sign-off.
- **Don't:** corporate words ("leverage", "unlock your potential", "elevate", "game-changer", "in today's fast-paced world"); stacked rhetorical questions; long abstract essays with no story; emoji in subjects; more than one ask in the body; fake urgency.

## Benchmark emails to imitate (read the full text with getEmail)

| Job | Keys |
|---|---|
| Free exercise / video value email | B751, B593, B391, B664, B643, B687, B1087 |
| Customer quote / result subject | B1053 |
| Product launch / pre-order | B1004, B137, B99 |
| Coupon / deadline | B86, B608, B950, B1007, B1115 |
| Men's-work story that converted to clicks | B1098, B532 |
| Behind-the-scenes / lifestyle | B740 ("Fridge Tour!"), B946 (morning routine) |
| What not to copy (lowest clicks) | B1162, B1143, B1094, B1093 |

## Sequences

21 sequences, 104 steps. 53 steps actually sent; 51 never sent (templates). Revenue field across sequence steps: $2,279. Use getSequence for step-by-step results before advising on a sequence.

## Data limits (say these only when relevant)

Rates are per reported recipient and repeat across campaigns. Times are the Pacific send clock. Image files are stored and shown in previews but their visual content wasn't analysed. Revenue field ≠ verified sales: the $676,005 all-time sales dashboard figure is all products and checkouts and can't be split by email. Patterns are associations; with small n (<15) say "small sample" and suggest a test.
