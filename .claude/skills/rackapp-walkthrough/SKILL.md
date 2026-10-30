---
name: rackapp-walkthrough
description: Write a new step-by-step patching walkthrough for the user's RackApp, or save drafts they made on the site, then republish. Use when the user asks how to patch a sound or technique, asks for a walkthrough, or asks to file away drafts from their RackApp.
---

# Add a walkthrough to RackApp

1. Read `my-rack/rack.json` and the manual notes for every module you plan to use (`my-rack/manuals/<slug>.md`). Use only modules the user owns, and check every control name and setting against the notes.
2. Write the walkthrough to `my-rack/walkthroughs/<id>.json` in the schema in `docs/data-format.md`. Match the house style of the existing walkthroughs: plain language, one action per step, exact jack and knob names, a short reason where it helps, a full patch list, 3 to 6 sections, a troubleshooting list and sources.
3. **Drafts saved on the site** live in the published artifact's database, in the `walkthroughs` collection. To file them away, read that collection for the URL in `my-rack/site.json`, check each draft against the manuals, fix what's wrong, drop the `status`, `savedAt` and `request` fields, and save it as a JSON file as above.
4. Rebuild and republish: `python3 tools/build.py my-rack dist`, then publish `dist/site/index.html` with its `data/` and `img/` files to the URL in `my-rack/site.json` (pass it as the artifact `url`; keep its existing capabilities).
5. Give the user the walkthrough's title and the link. If you're in a chat where they asked a patching question, also answer it there.
