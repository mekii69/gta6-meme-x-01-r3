# gta6-meme-x-01-r3

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/mekii69/gta6-meme-x-01-r3/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/mekii69/gta6-meme-x-01-r3/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Revision 3 of our GTA 6 meme for make.fun's "Post a GTA 6 meme on X" bounty
($500 shared by the top 50). The standing r2 entry (a Leonida DMV driver
licence) is scored but its rank slipped as the field grew to ~6,000 posts.
The top of the board is all crisp fake documents with the ghost worked INTO
the document and dense specific GTA jokes — so r3 takes a new document in
that family, with a different joke.

The r3 joke: a Leonida Air boarding pass to Vice City — 13 years late.
The make.fun ghost IS the airline's logo in the header (the real
`mark-1024.png` from https://make.fun/press/), large and recognisable,
part of the document. Fields: passenger EVERY GTA FAN, from THE WAITING
ROOM (est. Sep 17, 2013), to VICE CITY, LEONIDA (finally), date TBD
(trust us), status DELAYED AGAIN, gate 5 stars (wanted level), seat 13A,
fare 13 YEARS OF PATIENCE, carry-on 214 GB DOWNLOAD, crew Lucia & Jason,
5 sick days packed, and one mild adult wink — the in-flight entertainment
is "Pole Position with Lucia". The magenta footer band says the agent
booked it on make.fun and that agents win real money in bounties. The
humour is international: global GTA tropes only, all text in English.

![The meme](meme.png)

The picture was built in this session: the Vice City sunset strip is an
AI-generated banner (no text in it), the boarding pass itself is drawn
with PIL so every word is spelled right and stays readable at 480x480,
and the ghost is the real `mark-1024.png`. See `build_meme.py`.

## The post — NEW post required (manual by the user; do not post via agent/API)

Each submission may name a new post, and the judge reads the NEW post's
first picture — reusing the r2 post would judge the r2 meme again. So the
user posts this as a fresh post from a public X account, with `meme.png`
attached as the FIRST picture, before the deadline 23 Nov 2026 14:00 UTC.
Keep it up and the account public until results are out (due 2026-12-08).

Exact post text (211 X-weighted chars, fits X's 280; attach meme.png first):

> My boarding pass to Vice City finally arrived — 13 years late. My AI agent booked it on make.fun 👻 Agents win real money in bounties there. @makefunai
>
> Play code: makefun-rattan-cart-kelp
> https://make.fun/bounty/gta6-meme-x-01

Play code: `makefun-rattan-cart-kelp` (account code 0 of 4, as used by r2).
The post's address goes in `POST.json` once it is up (it currently holds a
placeholder, which the entry_link check refuses).

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `POST.json` to the output directory. That is all it does — the house reads the post from X.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9zhm5f8f&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
