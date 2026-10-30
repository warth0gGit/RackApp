# RackApp

RackApp turns photos of someone's Eurorack system into a personal web app: a to-scale drawing of their rack, searchable manual notes they can ask questions of, and a library of step-by-step patching walkthroughs. It is published as an artifact in the user's own claude.ai account, so its Claude features run on their own plan.

## When someone opens this repo

- No `my-rack/rack.json` yet: offer to set up their rack and follow the `rackapp-setup` skill.
- Asking how to patch something, or for a walkthrough: `rackapp-walkthrough` skill.
- Their rack changed: `rackapp-update` skill.

## Layout

- `app/index.html`: the app itself (one page, no build step). Data loads from `data/*.json` beside it, or from `window.__RACK_DATA` in the offline build.
- `tools/build.py`: validates a rack folder and writes `dist/site/` (to publish) and `dist/rackapp-offline.html`.
- `example-rack/`: a small sample rack in the same format. Use it for testing; never put a user's data in it.
- `my-rack/`: the user's own data. Git-ignored; never commit it.
- `docs/data-format.md`: the schema for every file in a rack folder.
- `tests/smoke.js`: browser test of a built app (`node tests/smoke.js [path-to-offline-html]`).

## Rules

- The user's data stays in `my-rack/`. Don't copy it into `example-rack/`, `app/` or anywhere committed.
- Manual notes are paraphrased from official sources, and say what was read in `read_from`. Never invent control names or specs.
- After changing `app/index.html`, run `python3 tools/build.py example-rack dist && node tests/smoke.js`.
