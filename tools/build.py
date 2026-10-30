#!/usr/bin/env python3
"""Build RackApp from a rack folder.

    python3 tools/build.py [RACK_DIR] [OUT_DIR]

RACK_DIR defaults to my-rack/ (falls back to example-rack/), OUT_DIR to dist/.

A rack folder holds:
  rack.json                 rack name, cases/rows, modules (see docs/data-format.md)
  photos/                   optional case photos, referenced from rack.json
  manuals/<slug>.md         manual notes, front matter + markdown sections
  walkthroughs/<id>.json    one walkthrough per file

Writes:
  OUT_DIR/site/             index.html + data/*.json + img/*  (publish this as an artifact)
  OUT_DIR/rackapp-offline.html   one self-contained file to open in any browser
"""
import base64, glob, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = {"clock", "sequencer", "modulation", "envelope", "vca", "utility", "oscillator", "voice", "filter", "effect",
              "sampler", "io", "mixer", "controller", "measurement", "random", "power"}
PANELS = {"silver", "dark", "white"}


def front_matter(text):
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    return meta, body.strip()


def chunk_manual(slug, body):
    chunks = []
    body = re.sub(r"^# .*\n", "", body).strip()
    for sec in re.split(r"\n(?=## )", "\n" + body):
        sec = sec.strip()
        if not sec:
            continue
        title, _, txt = sec.partition("\n")
        title = title.lstrip("# ").strip()
        buf = ""
        for p in re.split(r"\n(?=\n|- |\d+\. )", txt.strip()):
            if len(buf) + len(p) > 1400 and buf:
                chunks.append({"m": slug, "s": title, "t": buf.strip()})
                buf = ""
            buf += p + "\n"
        if buf.strip():
            chunks.append({"m": slug, "s": title, "t": buf.strip()})
    return chunks


def validate(rack):
    errors = []
    mods = rack.get("modules", {})
    if not rack.get("cases"):
        errors.append("rack.json has no cases")
    placed = set()
    for c in rack.get("cases", []):
        for r in c.get("rows", []):
            for s in r.get("modules", []):
                if s not in mods:
                    errors.append(f"case {c.get('id')}: module '{s}' is not defined in modules")
                placed.add(s)
    for s in rack.get("desk", []):
        if s not in mods:
            errors.append(f"desk: module '{s}' is not defined in modules")
        placed.add(s)
    for s, m in mods.items():
        for k in ("name", "hp", "category"):
            if k not in m:
                errors.append(f"module '{s}' is missing '{k}'")
        if m.get("category") not in CATEGORIES:
            errors.append(f"module '{s}' has unknown category '{m.get('category')}'")
        if m.get("panel", "silver") not in PANELS:
            errors.append(f"module '{s}' has unknown panel '{m.get('panel')}'")
        if s not in placed:
            errors.append(f"module '{s}' is not placed in any case row or the desk")
    return errors


def resize_photo(src, dst):
    try:
        from PIL import Image, ImageOps
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        im.thumbnail((1400, 1400))
        im.save(dst, "JPEG", quality=72, optimize=True)
    except Exception:
        shutil.copyfile(src, dst)


def build(rack_dir, out_dir):
    rack = json.load(open(os.path.join(rack_dir, "rack.json")))
    errors = validate(rack)
    if errors:
        raise SystemExit("rack.json problems:\n  - " + "\n  - ".join(errors))

    site = os.path.join(out_dir, "site")
    shutil.rmtree(site, ignore_errors=True)
    os.makedirs(os.path.join(site, "data"))
    os.makedirs(os.path.join(site, "img"))

    modules, chunks = {}, []
    for slug, mod in rack["modules"].items():
        mod = dict(mod)
        if mod.get("kind") == "blank":
            mod["kind"] = "power"  # drawn as an inert panel
        mod.setdefault("panel", "silver")
        mod.setdefault("maker", "")
        mod.setdefault("short", "")
        mod["guide"] = mod.pop("notes", "")
        path = os.path.join(rack_dir, "manuals", f"{slug}.md")
        mod["hasManual"] = os.path.exists(path)
        if mod["hasManual"]:
            meta, body = front_matter(open(path).read())
            for k in ("manual_url", "product_url", "read_from"):
                if meta.get(k):
                    mod[k] = meta[k]
            mod["manualWords"] = len(body.split())
            chunks += chunk_manual(slug, body)
        if mod["guide"]:
            chunks.append({"m": slug, "s": "Notes: how it fits your rack", "t": mod["guide"]})
        modules[slug] = mod
    if rack.get("systemFacts"):
        chunks.append({"m": "_system", "s": "Things to remember about this system", "t": "\n".join("- " + f for f in rack["systemFacts"])})

    cases = []
    for c in rack["cases"]:
        c = dict(c)
        photo = c.get("photo")
        if photo and os.path.exists(os.path.join(rack_dir, photo)):
            name = f"img/case-{c['id']}.jpg".lower()
            resize_photo(os.path.join(rack_dir, photo), os.path.join(site, name))
            c["photo"] = name
        else:
            c["photo"] = None
        cases.append(c)

    walks = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rack_dir, "walkthroughs", "*.json")))]
    walks.sort(key=lambda w: w.get("created", ""), reverse=True)

    data = [{"rackName": rack.get("rackName", "My Rack"), "cases": cases, "desk": rack.get("desk", []),
             "modules": modules, "systemFacts": rack.get("systemFacts", [])}, chunks, walks]
    for name, obj in zip(("modules", "manuals", "walkthroughs"), data):
        json.dump(obj, open(os.path.join(site, "data", f"{name}.json"), "w"), ensure_ascii=False)
    html = open(os.path.join(ROOT, "app", "index.html")).read()
    open(os.path.join(site, "index.html"), "w").write(html)

    # single-file offline copy: data and photos inlined
    for c in data[0]["cases"]:
        if c["photo"]:
            c["photo"] = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(site, c["photo"]), "rb").read()).decode()
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    marker = "<script>\n(() => {"
    assert marker in html, "app/index.html changed shape: offline build marker not found"
    offline = html.replace(marker, f"<script>window.__RACK_DATA = {blob};</script>\n{marker}", 1)
    offline = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
               '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
               '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
               '</head><body>' + offline + "</body></html>")
    open(os.path.join(out_dir, "rackapp-offline.html"), "w").write(offline)

    n = sum(1 for m in modules.values() if m.get("kind") != "power")
    print(f"Built '{data[0]['rackName']}': {n} modules, {sum(m['hasManual'] for m in modules.values())} manuals, "
          f"{len(chunks)} search chunks, {len(walks)} walkthroughs")
    print(f"  {site}/  (publish this)")
    print(f"  {os.path.join(out_dir, 'rackapp-offline.html')}  (open in any browser)")


if __name__ == "__main__":
    rack_dir = sys.argv[1] if len(sys.argv) > 1 else (os.path.join(ROOT, "my-rack") if os.path.exists(os.path.join(ROOT, "my-rack", "rack.json")) else os.path.join(ROOT, "example-rack"))
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "dist")
    build(os.path.abspath(rack_dir), os.path.abspath(out_dir))
