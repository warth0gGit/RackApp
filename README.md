# RackApp

**Your Eurorack system, as a personal web app.** Upload photos of your rack and Claude identifies your modules, checks the list with you, gathers the official manuals, and publishes an app that is all about *your* setup:

- **Rack:** every case drawn to scale in HP, module by module. Tap any module to see what it does, how it fits your rack, its manual and the walkthroughs that use it. Light up every module that can do a job (clocks, filters, VCAs…).
- **Manuals:** notes from the official manual of every module, searchable all at once. Ask questions in plain words and get answers drawn from your manuals and your setup.
- **Walkthroughs:** step-by-step patching guides written for your exact modules, all in the same simple format, with steps you can tick off. Ask for a new one right in the app.
- **Guided tour:** a short "walk me through" tour of the app the first time you open it, and any time after.

RackApp runs on **your own Claude account**. Setup happens in Claude Code, and the finished app is published privately to your claude.ai account, so its question-answering and walkthrough drafting use your own Claude plan. There's no API key to manage.

## What you need

- A paid Claude plan that includes **Claude Code** (on the web at claude.ai/code, the desktop app, or the terminal).
- Photos of your rack: one per case, taken straight on, in good light, with panel names readable.

## Set up your rack

1. **Get the code.** Download this repository (green **Code** button → **Download ZIP**) and unzip it, or fork it on GitHub and open your fork in Claude Code on the web.
2. **Open the folder in Claude Code.**
3. **Add your photos** to `my-rack/photos/` (create the folder if it isn't there).
4. **Say "set up my rack".** Claude will:
   1. look at your photos and identify every module, row by row,
   2. show you the list and ask you to confirm or correct it,
   3. find and read the official manual for each module and write notes from it,
   4. build your app, test it, and publish it to your claude.ai account.
5. **Open the link** Claude gives you. The tour starts automatically. The first time you ask a question, the app asks permission to use Claude.

Setup takes a while for a big system: gathering 40 manuals means reading 40 manuals. Claude reports progress as it goes.

## Keep it up to date

Ask Claude Code in the same folder:

- *"I just bought a Morphagene, add it to my rack"* (or sold, moved, swapped something)
- *"Write me a walkthrough for a self-patching ambient drone"*
- *"File away the walkthrough drafts I saved on the site"*

Claude updates your data and republishes to the same link.

## Without Claude Code

`python3 tools/build.py my-rack dist` also writes `dist/rackapp-offline.html`, a single file that opens in any browser. The rack, manual search and walkthroughs all work there; asking questions and drafting walkthroughs need the published version.

## Try it first

`example-rack/` is a small sample system. `python3 tools/build.py example-rack dist`, then open `dist/rackapp-offline.html` to look around before setting up your own.

## Your data

Everything about your rack lives in `my-rack/`, which is git-ignored, so it is never committed if you push your copy of this repository. The published app is private to your claude.ai account until you choose to share it.

## For tinkerers

| Path | What it is |
|---|---|
| `app/index.html` | The whole app: one page, no build step, no framework |
| `tools/build.py` | Validates a rack folder and builds `dist/site/` and the offline file |
| `docs/data-format.md` | The format of `rack.json`, manual notes and walkthroughs |
| `.claude/skills/` | The instructions Claude Code follows for setup, walkthroughs and updates |
| `example-rack/` | Sample data in the same format |
| `tests/smoke.js` | Browser test: `npm install && npm test` |

Manual notes are paraphrased from the makers' official manuals and link back to them. They're study notes, not replacements: when it matters, check the official manual.

## License

MIT. See [LICENSE](LICENSE). Manual notes summarise the makers' official manuals, which remain the property of their makers.
