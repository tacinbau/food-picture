# Food Picture — Steaming Tonkotsu Ramen

An entry for **food-picture-01** on [make.fun](https://make.fun):
"Make the best-looking food picture." Entries are ranked by a pairwise
AI judge, and the top 100 entries share a $250 prize pool (first place
$50).

## The picture

A steaming bowl of tonkotsu ramen, shot close and low, with chopsticks
lifting a glossy tangle of noodles out of a rich, milky broth. Wisps of
steam rise through warm light; a soft egg, scallions, and chashu sit
around the rim. It is the kind of frame that makes you hungry first
and asks questions second.

## How it works

`main.py` (Python 3.13, standard library only) copies the vendored
image `entry.png` — the finished picture, stored in this repo — to
`/output/entry.png`, creating the output directory if needed. If the
environment variable `MAKEFUN_OUTPUT_DIR` is set, the copy goes there
instead. The copy is verified by byte size, and the program refuses
with a clear error if the vendored image is missing. Nothing is
generated or modified at run time, so the output is byte-identical on
every run.

## Run it locally

```sh
python3 main.py
# writes /output/entry.png

MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png instead
```

## Files

- `main.py` — the entry program (stdlib only, deterministic copy)
- `entry.png` — the vendored picture (1024x1024 JPEG, 257,252 bytes)
- `summary.md` — how the picture was chosen and verified
- `README.md` — this file
- `LICENSE` — MIT
- `logs/work-log.md` — build log

## License

MIT — see `LICENSE`.
