---
name: rackapp-update
description: Update an existing RackApp when the rack changes - add, remove, move or correct modules, add cases or photos - then rebuild and republish. Use when the user says they bought, sold, moved or swapped a module, or that something in their RackApp is wrong.
---

# Update the rack

1. Read `my-rack/rack.json`. If they sent a new photo, read it and identify what changed (see the identification steps in the `rackapp-setup` skill).
2. Show the change as a short before/after list and ask them to confirm it.
3. Edit `rack.json`: rows stay left to right, new modules get `name`, `maker`, `hp`, `category`, `panel`, `short` and `notes`, and the `notes` and `systemFacts` of affected modules are updated if partnerships changed. Keep slugs stable for modules that stay.
4. For each **new** module, gather its manual exactly as in stage 5 of `rackapp-setup`. Keep the manual notes of removed modules unless the user asks to delete them; they do no harm.
5. Check `my-rack/walkthroughs/` for walkthroughs that use a removed module and tell the user which ones.
6. Rebuild and republish to the URL in `my-rack/site.json` (`python3 tools/build.py my-rack dist`, then publish `dist/site/index.html` with its `data/` and `img/` files, passing the URL as `url`).
