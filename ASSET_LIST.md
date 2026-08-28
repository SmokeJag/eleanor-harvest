# 🐆 CHILDREN OF THE HARVEST — DAZ 3D ASSET CHECKLIST
> For the DAZ 3D weekend. Tick each off as you render.
> **Studio:** SmokeJaguar Studios · **Game:** Eleanor: Children of the Harvest

---

## 📐 THE SPECS (match these exactly)

| Asset type | Resolution | Format | Notes |
|-----------|-----------|--------|-------|
| **Character sprites** | 720 × 1080 | **PNG with transparency** (alpha) | Full-body, standing, facing camera |
| **Backgrounds** | 1920 × 1080 | **WEBP** (quality 90) | No transparency needed |
| **Style** | — | — | Semi-realistic Daz render, Gothic-tinged, deep blues + sharp shadows + warm lamplight (the "cozy-dark" look) |

**Consistency rule:** Lock Eleanor's and Neith's face/hair/outfit as a **saved Daz scene** first, then reuse it for every render. Do NOT re-model them each time — that's how characters drift.

---

## 👤 CHARACTER SPRITES (720×1080 PNG, alpha) — the priority

| # | Alias | Character | Description / pose notes | Done |
|---|-------|-----------|--------------------------|------|
| 1 | `eleanor_neutral` | **Eleanor** | Dark-haired, late 20s, sharp determined eyes. Victorian detective: fitted dark coat, satchel. Neutral, watchful. | ☐ |
| 2 | `eleanor_determined` | **Eleanor** | Same model, more intense/ready expression (jaw set, eyes forward). | ☐ |
| 3 | `neith_neutral` | **Neith** | Warm bronze skin, dark hair bound with gold, kohl-lined eyes. Pale linen + gold. Calm, ancient stillness. (Reuse Scales of Ma'at Neith with tweaks.) | ☐ |
| 4 | `maren` | **Maren Holt** | The village woman who breaks the silence. Mid-40s, worn, kind but tired. Plain shawl, work-worn hands. | ☐ |
| 5 | `vicar` | **The Vicar** | Thin, greying, black clerical coat. The keeper of the bargain — weary, guarded. | ☐ |
| 6 | `miller` | **The Miller** | Broad, grey, outlived his mill. Rough apron, weathered face. | ☐ |
| 7 | `schoolteacher` | **The Schoolteacher** | Thin, precise, keeps the records. Neat dark dress, spectacles. | ☐ |
| 8 | `oldnan` | **Old Nan** | The oldest in the village. Crooked, smoke-blackened, ancient and clear-eyed. | ☐ |
| 9 | `innkeeper` | **The Innkeeper** | Broad, ruddy, arms like a blacksmith. Warm, watchful. | ☐ |

*(The Beast is a special case — see below.)*

---

## 🖼️ BACKGROUNDS (1920×1080 WEBP)

| # | Alias | Scene | Description | Done |
|---|-------|-------|-------------|------|
| 1 | `bg village` | **Grymshade village** | Grey, rain-hung, shuttered windows, empty streets. A fold of grey hills. | ☐ |
| 2 | `bg village id` | **The Square / the well** | The village square with the capped stone well at its centre. Used 5× — the key location. | ☐ |
| 3 | `bg inn` | **The Hanged Man** | Warm timbered inn interior, great hearth fire, amber lamplight, low murmur of a room. | ☐ |
| 4 | `bg chapel` | **The Chapel** | Small squat grey-stone chapel, locked door, trapdoor under the altar. | ☐ |

*(Already done — no need to re-render: `bg mansion_ext`, `bg hallway`, `bg library` are the refurbished mansion from the Mansion Mysteries.)*

---

## 🐆 THE BEAST (special)

| Alias | What | Notes | Done |
|-------|------|-------|------|
| `beast` | **The Beast of the moors** | A great black cat, larger than any dog, semi-transparent/ghostly, eyes burning. Seen on the moors and at the well. | ☐ |

*(Not yet an alias in the script — we'll wire it in once you have a render.)*

---

## 🎬 RENDER ORDER (recommended)

1. **Eleanor** (neutral + determined) — the lead, in every scene
2. **Neith** — the partner, in every scene
3. **The three backgrounds** (village, square/well, inn, chapel)
4. **Maren, the Vicar** — the two most important supporting characters
5. **The Miller, Schoolteacher, Old Nan, Innkeeper** — the old voices
6. **The Beast** — the special one

---

## ✅ HOW TO WIRE IN (once rendered)

Drop files into `game/images/`:
- Sprites → `game/images/sprites/`
- Backgrounds → `game/images/backgrounds/`

Then update the `image` aliases in `game/script.rpy` from `Solid("#...")` to the file path, e.g.:
```rpy
image eleanor_neutral = "images/sprites/eleanor_neutral.png"
image bg village = "images/backgrounds/bg_village.webp"
```
I can do this wiring on this machine once the files are synced via git.

---

## ⚠️ REMINDER FOR THE WEEKEND
- **Do NOT render ten things at once.** Do 2–3, check style consistency, then continue.
- **Match the trilogy's look** — Eleanor and Neith must look like their trilogy selves.
- **Save each character as a reusable scene** so the cast stays consistent across renders.
