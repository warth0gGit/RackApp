# RackApp data format

Everything about one person's rack lives in a single folder, `my-rack/` by default (it is git-ignored, so personal data never gets committed). `example-rack/` uses the same format and is the reference.

```
my-rack/
  rack.json               rack name, cases, rows, modules
  photos/                 case photos (optional, used for the Photo view)
  manuals/<slug>.md       manual notes, one per module
  manuals/pdf/<slug>.pdf  downloaded manuals (optional, never published)
  walkthroughs/<id>.json  one walkthrough per file
  site.json               written after publishing: {"url": "<artifact url>"}
```

`python3 tools/build.py my-rack dist` turns this into `dist/site/` (the page to publish) and `dist/rackapp-offline.html`.

## rack.json

```json
{
  "rackName": "Sam's Rack",
  "cases": [
    {
      "id": "A",
      "name": "Main case",
      "type": "Intellijel 7U Performance Case, 104 HP",
      "note": "Left of the desk",
      "photo": "photos/main-case.jpg",
      "rows": [
        { "label": "Top row: clocks and modulation", "modules": ["pams-new-workout", "maths", "blank-1"] }
      ]
    }
  ],
  "desk": ["keystep-37"],
  "systemFacts": ["Short, true facts about the whole system that change how you patch it."],
  "modules": {
    "maths": {
      "name": "Maths",
      "maker": "Make Noise",
      "hp": 20,
      "category": "modulation",
      "panel": "silver",
      "short": "Dual function generator and analog computer",
      "notes": "- **Role here:** ...\n- **Good partners:** ...",
      "status": "Not connected"
    }
  }
}
```

- **Slugs** are lowercase kebab-case and unique (`maths`, `pams-new-workout`). Two of the same module get `-2`, `-3`.
- **Rows** list modules left to right exactly as mounted. Include blank panels and power modules as their own entries with `"kind": "blank"` (or `"kind": "power"`) and `"category": "power"` so the drawing keeps the real spacing.
- **desk** holds controllers and sequencers that sit outside the cases (`"hp": 0`, `"kind": "desk"`).
- **category** is one of: `clock`, `sequencer`, `modulation`, `envelope`, `vca`, `utility`, `oscillator`, `voice`, `filter`, `effect`, `sampler`, `io`, `mixer`, `controller`, `measurement`, `random`, `power`.
- **panel** is the panel colour for the drawing: `silver`, `dark` or `white`.
- **notes** (Markdown) say how the module fits this particular rack: its role and its best partners among the owner's other modules.
- **status** (optional) flags something unusual, like a module that is mounted but not connected.

`tools/build.py` validates all of this and stops with a list of problems if anything is off.

## manuals/<slug>.md

```markdown
---
slug: maths
name: Maths
maker: Make Noise
hp: 20
category: modulation
manual_url: https://... (the official manual that was read)
product_url: https://... (official product page)
read_from: One line on what was actually read, e.g. "Official PDF manual v1.2"
---
# Maths
## Overview
## Panel controls and jacks
## Modes, menus and settings
## How to (common procedures)
## Specifications
## Tips and gotchas
```

Notes are written in plain language from the official manual (close paraphrase, not long verbatim copies). Every `##` section becomes searchable in the app, and the chat cites them as `Module › Section`. When no official manual exists, say so in `read_from` and work from the maker's product page.

## walkthroughs/<id>.json

```json
{
  "id": "kebab-case-id",
  "title": "Short task title in the owner's words",
  "summary": "One or two sentences on what this walkthrough does.",
  "goal": "One sentence: what the owner will hear or have at the end.",
  "category": "Sequencing & clock | Sound design | Modulation | Effects & space | Sampling & looping | Generative | Performance | Recording & I/O | Module basics",
  "level": "Beginner | Intermediate | Advanced",
  "created": "YYYY-MM-DD",
  "modules": ["slugs, in order of use"],
  "youNeed": ["cables, adapters or prep"],
  "patch": [{ "from": "Module · Jack", "to": "Module · Jack", "note": "short why or setting" }],
  "sections": [
    {
      "title": "Phase title",
      "intro": "One plain sentence",
      "steps": [{ "do": "One action with **exact control names**", "why": "Optional one-line reason" }],
      "note": "Optional tip"
    }
  ],
  "troubleshooting": [{ "problem": "...", "fix": "..." }],
  "sources": [{ "label": "Module manual › section", "url": "official manual URL" }]
}
```

House style: plain language, one action per step, exact jack and knob names, a reason where it helps a beginner, 3 to 6 sections of 3 to 8 steps.
