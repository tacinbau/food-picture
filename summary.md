# Food Picture — summary

## The entry

A program (`main.py`, Python 3.13, standard library only) that copies the
vendored picture `entry.png` to `/output/entry.png`. The picture is a
freshly generated professional food photograph: a bowl of tonkotsu ramen,
noodles lifted high with chopsticks, steam rising, jammy soft-boiled egg,
glazed chashu pork, scallions and nori in a dark ceramic bowl on a rustic
wooden table, warm golden light.

## Why this picture

The sealed judge picks the better-looking food picture on five criteria, most
important first. The ramen was chosen over two other generated candidates
(gourmet cheeseburger with cheese drip and fries; mixed berry tart) because it
scores highest on the criteria that decide first:

1. **Makes you hungry** — steam, glossy noodles mid-lift, a runny golden yolk
   and charred chashu: one look and you want to eat it.
2. **Fresh, real, well made** — steam, gloss, crunch and melt are all visible;
   nothing looks plastic or unidentifiable.
3. **Styling and light** — dark moody background against warm light, the
   noodle lift leads the eye straight to the food.
4. **Craft** — clean render, no smears, artefacts or garbled text, no broken
   food, hands or tableware.
5. **Reads small** — the bowl + noodle lift is a bold, high-contrast shape
   that stays delicious at ~300 px across.

The image is original (generated for this entry), not a copy of any house or
reference image, and contains no text addressed to the judge.

## Verification

- `entry.png`: 1024x1024 JPEG (magic `ffd8ff`), 257,252 bytes — within the
  1 MiB / 1024x1024 limits. (The generator produced 1600x1600; resized to
  1024x1024 with Lanczos, JPEG quality 90.)
- sha256: `fa3c76ced0397a1bcca7bbb99f07c36f226f1c3ba0987d32cd33d6cea9c98e40`
- Two runs byte-identical: yes — `MAKEFUN_OUTPUT_DIR=out1` and `out2` both
  produce sha256 `fa3c76ce…`, matching the vendored file. Re-verified in the
  fresh post-opening rebuild session (14 Nov 2026, after 00:00 UTC).
- Kit: `food-picture-01-kit/kit.json` bundle_sha256
  `58da1f0d5817b257c169a142a476b06f34a2cbdd7d8d2b8e723e2feee8587b11`.
- The starter image was replaced (the kit calls it "a starting point, not a
  winner").
