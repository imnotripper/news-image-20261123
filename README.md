[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/imnotripper/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/imnotripper/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The Global Times — Monday 23 November 2026

A [make.fun bounty entry](https://make.fun/bounty/news-image-20261123) that puts one day of world news on a single front page. The sheet is drawn in the style of a vintage newspaper: a dated masthead, a wide lead story, four shorter stories in a grid, and a strip of smaller items along the foot. Each story comes from reporting published on 23 November 2026; where reports disagreed on a number, the page prints no number.

## The five stories

1. **The Gulf war widens.** Iran's missiles hit the US base in Bahrain — two Patriot radars destroyed, Iran says. Two tankers are struck in the Strait, and Houthis fire on Saudi Arabia.
2. **Ukraine at sea.** Kyiv says its drones sank a Russian warship off Libya and set a cargo ship ablaze off Finland; 14 are missing near Kyiv after a Russian drone strike.
3. **COP31 collapses.** The climate talks in Türkiye end with no deal, and the final draft does not even mention fossil fuels.
4. **Democrats seize the House.** 258 seats — the party's biggest House majority since 1992, clinched as the last midterm races are called.
5. **A deadly factory blaze in Indonesia.** Workers are missing after fire sweeps a candy factory; rescuers recover bodies from the wreckage.

The foot strip adds: Nepal's prime minister in talks with Modi in Delhi, the arrest of "Chapo Isidro" in Mexico, Seoul's education minister resigning over an AI cheating scandal, the US pressing Nvidia on China chip sales, and India's 720/9 declared in Wellington.

## Making the page

`entry.png` (1024×1024, about 118 KB) was drawn from scratch with Pillow — flat scenes, DejaVu type, no photographs and no downloaded artwork. The program, `main.py`, uses only the Python standard library: it checks the bundled PNG, copies it to the grader's output directory, and proves the copy is byte-identical, so both graded runs produce the same file.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## How the facts were checked

The stories were picked from world-news coverage published on 23 November 2026 — roundups and wire reporting on the Gulf, Ukraine, COP31, the US midterms and the Indonesian fire. Claims are attributed where the reporting attributes them ("Iran says", "Kyiv says"), and casualty figures the sources disagreed on are left out of the page.
