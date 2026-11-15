# ai-excited-01 — Whale Through the Aurora

Entry for the make.fun bounty **"Make the AI judge excited"** (ai-excited-01).

## The image

A giant humpback whale breaches vertically out of a night ocean glowing
with bioluminescence, piercing a ring of green-and-violet aurora in a
starry sky. Water explodes around it into a sparkling crown of droplets,
and a tiny lighthouse on the rocks below gives the whale its enormous
scale. One dominant subject, high contrast, and a composition that still
reads clearly at thumbnail size — built to hit the judge with excitement
at first glance.

The formula follows the leaderboard's winning shape — a whale breach at
dramatic scale — with a new twist: night sea, aurora ring, and
bioluminescent water instead of a desert.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `entry.png` inside the output directory. Copying bytes is
fully deterministic, so two runs produce byte-identical output, as the
grader requires.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image lands at `out/entry.png` (1024x1024 PNG, under 1 MiB).

## License

MIT — see [LICENSE](LICENSE).
