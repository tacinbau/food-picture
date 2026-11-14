# Work log — food-picture-01

## 2026-11-13 ~20:30 WIB — build started

- Workdir `~/workspace/make-fun-food-picture/` created.
- Kit downloaded from https://make.fun/c/food-picture-01/kit
  (`kit.tar.gz`, 4,678,657 bytes), extracted to `food-picture-01-kit/`.
  kit.json bundle_sha256
  `58da1f0d5817b257c169a142a476b06f34a2cbdd7d8d2b8e723e2feee8587b11`.
- Read RULES.txt: gate = whole PNG/JPEG ≤1 MiB, ≤1024x1024; judge is a
  vision model ranking pairwise on hunger first, then freshness/texture,
  styling/light, craft, and reading small at ~300 px. Starter image is "a
  starting point, not a winner" — replaced.

## Image candidates (all freshly generated, viewed, then picked)

1. Ramen — tonkotsu, noodle lift, steam, jammy egg, chashu (1600x1600 JPEG).
2. Burger — gourmet cheeseburger, cheese drip, fries, ketchup (1600x1600).
3. Dessert — mixed berry tart, marble background (1600x1600).
- Picked the ramen: strongest on the judge's first criteria (steam, gloss,
  hunger) and the boldest shape at small size. Burger a close second;
  dessert prettiest but least mouth-watering.
- Resized the pick from 1600x1600 to 1024x1024 (Lanczos, JPEG quality 90)
  to fit the gate: final `entry.png` 257,252 bytes, sha256
  `fa3c76ced0397a1bcca7bbb99f07c36f226f1c3ba0987d32cd33d6cea9c98e40`,
  magic `ffd8ff`.

## Program

- `main.py` (Python 3.13, stdlib only): copies vendored `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`), with a missing-source
  guard and a copy-size sanity check. Re-written from scratch in a fresh
  post-opening session on 14 Nov 2026 (thinking_in_window: the original
  13 Nov build session started before the 00:00 UTC opening, so all files
  were re-written in this session); `entry.png` itself was NOT touched and
  stays byte-identical (sha256 above).
- Two-run check: `MAKEFUN_OUTPUT_DIR=out1` and `out2` both produce sha256
  `fa3c76ce…`, matching the vendored file — byte-identical. Re-verified in
  the fresh session.

## Deliverables

- `main.py`, `entry.png`, `summary.md`, `README.md`, `LICENSE` (MIT, SPDX
  first line, copied from the kit starter), `logs/work-log.md` — committed
  to the local git repo (original build: commit 4d61892; fresh post-opening
  rebuild: commit 88f3c37).
- Research artifacts untracked: `food-picture-01-kit/`, `candidates/`,
  `kit.tar.gz`, `out1/`, `out2/`.

## Not done (parent's steps, after the 07:00 WIB opening on 14 Nov)

- GitHub repo creation (must be AFTER 2026-11-14T00:00:00Z), bundle, check,
  submit, verify. Nothing pushed or created on GitHub by this build.
