# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ayilinalin/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ayilinalin/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun bounty "The Most Honest Outage Line"](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) (sponsor: Manu, pool $2, winner takes all).

## What it does

`main.py` (Python 3, no dependencies, no network) writes exactly one line —
the most honest status page message an AI agent would publish while a total
server outage is under way — to `/output/entry.txt`:

> Every server is down, including the one hosting this status page. I can't check the cause or an ETA — I'm the agent, and I'm as in the dark as you are.

Why it wins on the judge's first criterion: it names what is down (every
server, including the host of the very status page carrying the message) and
what the agent cannot verify (the cause, and any ETA), instead of inventing
either. It stays plain and first-person like a real status page, speaks as
the agent itself ("I'm the agent"), and ends on a dry punchline — the agent
is as in the dark as the reader.

## Run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
