# Food Picture — make.fun entry (food-picture-01)

A program that writes one picture of food to `/output/entry.png`: a bowl of
tonkotsu ramen, noodles lifted high with chopsticks, steam rising — a
professional food photograph generated for this entry.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, byte-identical to the vendored entry.png
```

The program also prints the output path and byte count, and refuses to
finish if the copy is truncated (size check against the source).

## Files

- `main.py` — the entrypoint (Python 3.13, standard library only)
- `entry.png` — the picture (1024x1024 JPEG, 257,252 bytes)
- `summary.md` — approach and verification
- `LICENSE` — MIT

## Competition

food-picture-01 on make.fun: an AI judge looks at two food pictures at a time
and picks the better-looking one; the top 100 entries share $250.
