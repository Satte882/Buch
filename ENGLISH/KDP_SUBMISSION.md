# KDP Submission – REASONABLE MEASURES

status: ready-for-live-kdp
market: Amazon.com
language: English

This is the operational entry checklist for the English release. `ENGLISH/KDP_METADATA.md` remains the source for positioning rationale; this file contains the values to enter or upload in KDP.

## 1. Book Details

| KDP field | Value |
|---|---|
| Language | English |
| Book title | `REASONABLE MEASURES` |
| Subtitle | leave blank |
| Series | none |
| Edition number | leave blank unless KDP specifically requires an edition marker |
| Primary author | use the exact same author identity as the published German edition; do not create a variant spelling |
| Translator | **OPEN LIVE-SUBMISSION GATE** — KDP requires translated works to identify a translator; do not invent or misattribute a human translator |
| Description | use the HTML block from `ENGLISH/KDP_METADATA.md` |
| Publishing rights | I own the copyright / necessary publishing rights |
| Primary marketplace | Amazon.com |

## 2. AI Content Disclosure

The English text must be disclosed as an **AI-generated translation** under KDP's current definition because an AI-based system generated the translated text, even though the edition subsequently received human-directed editorial review and a complete manuscript QA pass.

Enter:

- AI-generated content: **Yes**
- Type: **Text / Translation** (use the closest wording shown in the current KDP form)
- Do not classify this translation as merely AI-assisted.

## 3. Keywords

Enter one phrase per keyword field:

1. `government overreach`
2. `civil liberties`
3. `counterterrorism investigation`
4. `law enforcement ethics`
5. `national security`
6. `institutional power`
7. `security versus freedom`

## 4. Categories

Choose up to three closest available Amazon.com categories for each format:

1. Mystery, Thriller & Suspense > Thrillers > Political
2. Mystery, Thriller & Suspense > Thrillers > Psychological
3. Mystery, Thriller & Suspense > Thrillers > Terrorism

If the live picker uses different wording, select the closest semantic equivalent. Do not choose an unrelated category merely for ranking potential.

## 5. Audience

| Field | Value |
|---|---|
| Adult / general fiction | Yes |
| Children's / YA reading age | leave unset |
| Sexually explicit images or title | No |

## 6. Kindle eBook

### Upload

- manuscript file: `ENGLISH/REASONABLE_MEASURES.epub`
- format: reflowable EPUB 3
- CI package validation: PASS
- W3C EPUBCheck 5.3.0 / EPUB 3.3: **PASS — 0 errors, 0 warnings**
- ISBN: not required for KDP eBook
- cover: English front cover with exact title `REASONABLE MEASURES`

### Price

- Amazon.com target list price: **$4.99**
- royalty: **70%** where eligible
- territories: select the rights actually controlled for the English edition; do not infer rights not owned

### Live QA before publish

In Kindle Previewer / KDP preview verify:

- title page says `REASONABLE MEASURES`
- navigation TOC contains Prologue + Chapters 1–47
- chapter headings do not split or disappear
- italics/bold render correctly
- paragraph flow responds normally to font-size changes
- no print page numbers, headers, fixed margins or blank print pages appear
- final sentence remains: `How strong is your counterhypothesis?`

## 7. Paperback

### Interior

- manuscript file: `ENGLISH/NORMALFALL.docx`
- title inside file: `REASONABLE MEASURES`
- trim size: **5.06 × 7.81 in (12.85 × 19.84 cm)**
- bleed: **No bleed**
- interior: **black ink on white paper**
- CI render guard: **568 pages**
- KDP Previewer page count: **OPEN — authoritative for cover/spine production**

### ISBN

- use a new ISBN for the English paperback
- do not reuse the German print ISBN
- KDP-provided ISBN is acceptable if the release strategy does not require an independently owned ISBN

### Price

- provisional Amazon.com target: **$18.99**
- confirm only after KDP has rendered the final page count and printing cost

## 8. Paperback Cover Gate

Do **not** finalize the print cover from the CI page count alone.

Required sequence:

1. create the paperback project in KDP
2. upload `ENGLISH/NORMALFALL.docx`
3. set **black ink, white paper, 5.06 × 7.81 in, no bleed**
4. run KDP Previewer and record the final KDP page count
5. generate/download the exact KDP Cover Calculator template for those settings
6. build the one-page full-wrap PDF against that template
7. verify embedded fonts, safe areas, barcode area and PDF dimensions
8. upload the cover and rerun Previewer

English cover direction remains the approved minimalist NORMALFALL concept, localized rather than redesigned by default:

- white/off-white field
- dark typography
- front: `REASONABLE MEASURES` + translated epigraph only
- no author name unless a separate cover decision is made
- no stock thriller imagery / weapon / silhouette / blood motif
- spine: `REASONABLE MEASURES`
- back: restrained / mostly clear; protect barcode area

## 9. Release Gates

Only these items remain external/live:

- [ ] translator contributor treatment resolved correctly in the current KDP form
- [ ] Kindle front cover supplied and previewed
- [ ] Paperback interior uploaded; final KDP page count recorded
- [ ] Paperback Cover Calculator template downloaded and final full-wrap cover produced
- [ ] final prices / territories confirmed in KDP
- [ ] Kindle Previewer and Paperback Previewer pass without errors

Everything else in the English text, metadata, EPUB and paperback interior is already produced in the repository.
