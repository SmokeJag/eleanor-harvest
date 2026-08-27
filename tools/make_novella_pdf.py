#!/usr/bin/env python3
"""Build a clean novella PDF of 'Children of the Harvest' for non-gamer readers.
Usage: python make_novella_pdf.py <export.md> <out.pdf>
Strips Ren'Py game-isms (scene labels, 'You choose' menus, episode markers)
so it reads as a plain story.
"""
import re, html, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Flowable)
from reportlab.lib.styles import ParagraphStyle

src_path, out_path = sys.argv[1], sys.argv[2]
src = open(src_path, encoding="utf-8").read()
lines = src.split("\n")

blocks = []
for ln in lines:
    s = ln.rstrip()
    if not s.strip() or s.strip() == "*A novel-style reading of the game script.*":
        continue
    if s.strip() == "---":
        blocks.append(("hr", ""))
        continue
    if s.startswith("# "):
        blocks.append(("h1", s[2:].strip()))
        continue
    if s.startswith("### "):
        label = s[4:].strip()
        clean = {
            "The Grand Hallway": None,
            "The Village": None,
            "bg village id": "The Square",
            "bg inn": "The Hanged Man",
            "bg chapel": "The Chapel",
            "Black": None,
        }.get(label, None)
        if label == "Black":
            continue
        blocks.append(("h2", clean if clean else label))
        continue
    if s.strip().startswith("*") and s.strip().endswith("*") and len(s.strip()) > 6:
        continue  # drop episode/act markers
    dm = re.match(r"^\*\*([^*]+):\*\*\s*(.*)$", s)
    if dm:
        blocks.append(("dialogue", (dm.group(1), dm.group(2))))
        continue
    if s.strip().startswith("> -") or "You choose" in s or s.strip().startswith("> "):
        continue  # drop choice menus
    blocks.append(("p", s))

INK = colors.HexColor("#1a1a1a")
DARK = colors.HexColor("#6b3a1a")

st_title = ParagraphStyle("t", fontName="Times-Bold", fontSize=28, leading=34, alignment=1, textColor=INK, spaceAfter=6)
st_sub = ParagraphStyle("s", fontName="Times-Italic", fontSize=15, leading=20, alignment=1, textColor=colors.HexColor("#555555"))
st_pub = ParagraphStyle("pub", fontName="Times-Roman", fontSize=11, leading=16, alignment=1, textColor=colors.HexColor("#888888"))
st_chap = ParagraphStyle("c", fontName="Times-Bold", fontSize=14, leading=18, alignment=1, textColor=DARK, spaceBefore=14, spaceAfter=6)
st_body = ParagraphStyle("b", fontName="Times-Roman", fontSize=12, leading=18, alignment=4, textColor=INK, spaceAfter=8)
st_dialogue = ParagraphStyle("d", parent=st_body, spaceAfter=5)

def esc(t): return html.escape(t)

class HR(Flowable):
    def wrap(self, aw, ah): return aw, 1*mm
    def draw(self):
        self.canv.setStrokeColor(colors.HexColor("#cccccc"))
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 0, self.width, 0)

story = []
first_h1 = True
for kind, data in blocks:
    if kind == "h1":
        if first_h1:
            story.append(Spacer(1, 60*mm))
            story.append(Paragraph(esc(data), st_title))
            story.append(Paragraph("An Eleanor Thorne Mystery", st_sub))
            story.append(Spacer(1, 10*mm))
            story.append(HR())
            story.append(Spacer(1, 14*mm))
            story.append(Paragraph("SmokeJaguar Studios", st_pub))
            story.append(PageBreak())
            first_h1 = False
        else:
            story.append(Paragraph(esc(data), st_title))
            story.append(Spacer(1, 10))
    elif kind == "h2":
        story.append(Paragraph(esc(data), st_chap))
    elif kind == "p":
        story.append(Paragraph(esc(data), st_body))
    elif kind == "dialogue":
        name, text = data
        story.append(Paragraph(f'<font color="#8a2a2a"><b>{esc(name)}:</b></font> {esc(text)}', st_dialogue))
    elif kind == "hr":
        story.append(Spacer(1, 3))
        story.append(HR())
        story.append(Spacer(1, 3))

def footer(canv, doc):
    canv.saveState()
    canv.setFont("Times-Italic", 9)
    canv.setFillColor(colors.HexColor("#888888"))
    canv.drawCentredString(A4[0]/2, 14*mm, "Children of the Harvest")
    canv.restoreState()

doc = BaseDocTemplate(out_path, pagesize=A4,
                      leftMargin=24*mm, rightMargin=24*mm, topMargin=20*mm, bottomMargin=20*mm,
                      title="Children of the Harvest", author="SmokeJaguar Studios")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
doc.build(story)
print("PDF written:", out_path)
