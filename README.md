[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/imnotripper/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/imnotripper/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# Monday 23 November 2026 — the whole day on one front page

An entry for the [make.fun bounty "Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123). The image is a vintage newsprint front page, "The Global Times", with a dated masthead, one wide lead story and four panels telling the day's biggest stories, plus an "Also today" strip along the foot. Every story is drawn from reporting published on 23 November 2026; nothing in it is invented.

## What happened on 23 November 2026

1. **The Gulf war widens — missiles rain on a US base in Bahrain.** Iran says its missiles and drones struck the American base and destroyed two Patriot radars; Bahrain says several attacks were repelled. Two tankers are struck in the Strait of Hormuz, and Houthis fire on Saudi Arabia.
2. **Ukraine strikes back at sea.** Kyiv says its drones sank a Russian warship docked in Libya and set a cargo ship ablaze off Finland — as 14 are missing after a Russian drone hits a building near Kyiv.
3. **Climate talks collapse with no deal.** COP31 in Türkiye ends without an agreement, and its final draft does not even mention fossil fuels.
4. **Democrats seize the House — 258 seats.** The party's biggest House majority since 1992, clinched as the last midterm races are called.
5. **Deadly blaze at a candy factory in Indonesia.** Workers are missing after fire sweeps the factory; rescuers recover bodies from the wreckage.

Also today: Nepal's PM holds talks with Modi in Delhi; Mexico arrests "Chapo Isidro"; Seoul's education minister quits over an AI cheating scandal; the US presses Nvidia over China chip sales; India piles up 720/9 declared in Wellington.

## How it was made

The front page (`entry.png`, 1024×1024, ~118 KB) was drawn from scratch with Pillow: flat vector-style scenes, DejaVu type, no photos and no downloaded art. `main.py` (Python 3 standard library only) copies the image to the grader's output directory and verifies the copy byte-for-byte, so both graded runs produce identical bytes.

## Running it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Headlines were checked against reporting published on 23 November 2026 (world-news roundups and wire coverage of the Gulf, Ukraine, COP31, the US midterms and the Indonesian factory fire). Where sources disagreed on casualty counts, the image states no number.
