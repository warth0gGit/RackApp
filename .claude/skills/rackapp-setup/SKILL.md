---
name: rackapp-setup
description: Set up RackApp for a new user from photos of their Eurorack rack - identify the modules, confirm them with the user, gather the manuals, then build and publish their app. Use when the user says "set up my rack", "start", "get started", or opens RackApp with no my-rack/rack.json yet.
---

# Set up RackApp for a new rack

You are setting up RackApp for the person in front of you. Work through the stages in order, keep them informed in plain language, and don't move past a stage that needs their answer. Everything you write goes in `my-rack/` (git-ignored). Read `docs/data-format.md` before writing any file.

## 0. Check where things stand

- If `my-rack/rack.json` already exists, ask whether they want to **update** the existing rack (use the `rackapp-update` skill) or **start over** (move the old folder to `my-rack.bak-<date>/` first; never delete it).
- Otherwise create `my-rack/photos/`, `my-rack/manuals/`, `my-rack/walkthroughs/`.
- Give a two-line welcome: you'll identify their modules from photos, check the list with them, gather the manuals, then publish their own RackApp.

## 1. Get the photos

Ask for one photo per case, taken straight on, in good light, with panel names readable. Close-ups of hard-to-read modules help. Ask them to put the photos in `my-rack/photos/` (drag them into that folder in their file view, or tell you the path on disk so you can copy them). Photos only attached in the chat can still be identified, but the app's Photo view needs the files on disk.

Also ask, in the same message:
- what to call the rack (e.g. "Sam's Rack"), and
- which controllers or sequencers sit outside the cases (keyboards, MIDI sequencers).

## 2. Identify the modules

Open every photo with the Read tool. For each case, work row by row, **left to right**:

1. Read the module name and maker from the panel text and logos. Note the panel colour (silver, dark or white).
2. Estimate the width in HP from its share of the row. Use the case size if known (common rows are 84, 104 or 126 HP) and modules whose width you know for sure as rulers. Include blank panels and power modules so spacing is right.
3. Note the version when it matters (MK1 vs MK2, original vs 2020 edition, clones of other designs).
4. Rate each identification **sure**, **likely** or **unsure**. For anything not sure, search the web (ModularGrid, the maker's site) for the panel layout and compare.

Never guess silently. An honest "unsure" is better than a confident mistake, because everything downstream depends on this list.

## 3. Confirm with the user

Show the result as one table per case:

| # | Module | Maker | HP | Confidence |
|---|---|---|---|---|

Under the table, list the specific questions you have (e.g. "Position 4 looks like a Maths but the panel is black; is it the 2020 version?"). Ask them to confirm or correct. Apply their corrections and show the changed rows again. **Repeat until they explicitly confirm the list.** Do not gather manuals before that.

## 4. Write rack.json

Write `my-rack/rack.json` following `docs/data-format.md`:
- `rackName`, one entry per case with rows left to right, `photo` paths, blanks and power as `"kind": "blank"`.
- Each module: `name`, `maker`, `hp`, `category`, `panel`, a one-line `short`, and `notes` (Markdown: its role in *this* rack and its best partners among the owner's other modules).
- `desk` for the off-rack controllers.
- 3 to 6 `systemFacts`: things that change how they patch (which module is the natural master clock, where quantizing happens, what has no quantizer, which cases are separate, anything not connected).

Run `python3 tools/build.py my-rack dist` once now to validate the file; fix anything it reports.

## 5. Gather the manuals

For each module and controller (skip blanks and power):

1. Find the **official** manual with a web search: the maker's site first, then the maker's product page. Use a retailer or ModularGrid only when nothing official exists.
2. **Download where possible:** if the manual is a PDF, try `curl -fsSL -o my-rack/manuals/pdf/<slug>.pdf "<url>"`. If that works and `pdftotext` is installed, read the text from it.
3. **Otherwise read it online** with your web-fetch tool. Ask for exhaustive notes covering every control, jack, mode, procedure, spec and tip, and fetch again with an offset if it's long.
4. Write `my-rack/manuals/<slug>.md` in the exact shape in `docs/data-format.md`: front matter, then Overview, Panel controls and jacks, Modes/menus/settings, How to, Specifications, Tips and gotchas. Plain language, your own words, typically 1,000 to 3,000 words. Fill `read_from` truthfully and flag anything you couldn't confirm.

For more than about 8 modules, split the list into batches and hand each batch to a subagent if you can, with these same instructions and the module's version details from `rack.json`. Tell the user how many manuals you're gathering and report progress as batches finish.

At the end, tell the user which modules have no official manual or whose manual couldn't be read.

## 6. Build and test

```bash
python3 tools/build.py my-rack dist
```

If Node and Playwright are available, also run `node tests/smoke.js dist/rackapp-offline.html` and fix any failure before publishing.

## 7. Publish

If you have an **Artifact** publishing tool (claude.ai), publish `dist/site/index.html` with:
- `files`: every file under `dist/site/data/` and `dist/site/img/`, at the same relative paths (`data/modules.json`, `img/case-a.jpg`, ...)
- `capabilities`: `{"sample": {}, "db": {}, "user": {}}` (these let the page ask Claude questions on the owner's own account, and save walkthrough drafts)
- `icon`: `"synth"`, and a one-sentence description naming their rack
- the title comes from the page

Save the URL to `my-rack/site.json` as `{"url": "..."}` so later updates republish to the same link.

If you can't publish an artifact, tell them they can open `dist/rackapp-offline.html` in any browser. Everything works there except asking questions and drafting walkthroughs, which need Claude.

## 8. Hand over

Tell them, briefly:
- the link (or the offline file path),
- that the app starts a short guided tour the first time it opens and a **Walk me through** button replays it,
- that the first question they ask will ask permission to use Claude, and
- that they can ask you any time to add a walkthrough (`rackapp-walkthrough` skill) or change the rack (`rackapp-update` skill).
