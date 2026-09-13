#!/usr/bin/env python3
"""Regenerates the four pages from _head.part, _foot.part and _body/*.html."""
import os, pathlib

PAGES = [
    ("home",     "index.html",          "Gabriel Fritsch",
     "Gabriel Fritsch is a PhD candidate in economics at the University of Oxford and a member of technical staff at Mantic AI. Research on fiscal policy, sovereign debt, and international macroeconomics."),
    ("research", "research/index.html", "Research &middot; Gabriel Fritsch",
     "Working papers and work in progress on fiscal policy, sovereign default, sudden stops, and geopolitical fragmentation."),
    ("teaching", "teaching/index.html", "Teaching &middot; Gabriel Fritsch",
     "Courses taught at the University of Oxford and the Oxford University Economics Summer School."),
    ("writing",  "writing/index.html",  "Writing &middot; Gabriel Fritsch",
     "Essays, and selected research reports from the Goldman Sachs LatAm Economics team."),
]
SLOTS = {"home": "__H__", "research": "__R__", "teaching": "__T__", "writing": "__W__"}

root = pathlib.Path(__file__).parent
head = (root / "_head.part").read_text()
foot = (root / "_foot.part").read_text()

for slug, out, title, desc in PAGES:
    h = head.replace("__TITLE__", title).replace("__DESC__", desc)
    for s, token in SLOTS.items():
        h = h.replace(token, ' aria-current="page"' if s == slug else "")
    dest = root / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(h + (root / "_body" / f"{slug}.html").read_text() + foot)
    print("built", out)
