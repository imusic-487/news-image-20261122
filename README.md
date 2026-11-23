# The World in One Page — 22 November 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)
[![50 stories](https://img.shields.io/badge/stories-50-red.svg)](entry.png)

One image that sums up the world's news of **Sunday 22 November 2026**:
50 stories across 7 regions, each with its source named.

## The day in one line

COP31 collapses in Antalya with no deal; Iran says it hit US Patriot
radars at bases in Bahrain; Mexican forces capture cartel boss
"El Chapo Isidro" in Sinaloa, 11 dead; Democrats clinch 258 House
seats, their largest majority since 1992.

## What the image holds

- **4 lead diagrams** — the COP31 draft with "fossil fuels" struck out,
  a schematic Gulf map of the Bahrain strikes, a Sinaloa wanted poster,
  and a House-seats bar chart (258 vs 177, majority line at 218).
- **12 more lead stories** — Kryvyi Rih, the Kyiv drone strike and the
  Sparta II fire, the Cikande factory fire, the market correction, the
  Delta outage, the GTA 6 launch record, the EU–Indonesia trade deal,
  French protests, the Nigeria boat accident, the Brazil storm, the
  South Korean exam scandal, and the Nvidia spy probe.
- **Stories 17–50** in brief, plus a schematic world map and a UTC
  timeline of the day.
- **DATE CHECK** — what was left out on purpose because it broke before
  22 November, and what the one-sided claims are.
- **CLAIM** means one side's account, not independently confirmed.

## Entry

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`, byte for byte, and verifies the copy by size and
image signature. No network, no randomness: two runs write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entry for the [make.fun bounty](https://make.fun/bounty/news-image-20261122)
"Sum up 22 November's world news in one image".
