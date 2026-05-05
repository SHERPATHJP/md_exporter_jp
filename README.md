# md_exporter_jp — Markdown Exporter (Japanese, PDF-only)

A commercial-safe, Japanese-language-aware fork of
[bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter)
for Dify. This fork ships a single tool — **`md_to_pdf`** — designed to
render Markdown into a PDF with reliable Japanese / CJK support, using the
bundled Noto Sans JP font.

> Forked from [`bowenliang123/markdown-exporter`](https://github.com/bowenliang123/markdown-exporter)
> at upstream commit `c8033c9` (version 3.6.9). Licensed under
> [Apache License 2.0](LICENSE.txt). See [NOTICE](NOTICE) for attribution
> and [CHANGES.md](CHANGES.md) for the list of modifications.

## Features

- **Markdown → PDF** with proper Japanese / Chinese / Korean text rendering
- **Bundled Noto Sans JP** TTF font (no external font lookup needed)
- **Page orientation** parameter (`portrait` / `landscape`, default `landscape`)
- Pure-Python rendering pipeline: `markdown` + `xhtml2pdf` + `reportlab`
- **No AGPL / GPL dependencies** — safe for closed-source commercial distribution

## Why this fork?

The upstream `bowenliang123/markdown-exporter` is excellent but ships a wide
suite of converters, some of which depend on packages with copyleft licenses
(PyMuPDF, GPL-bundled Pandoc). For products that distribute as closed-source
commercial offerings, those dependencies require careful handling.

This fork takes the opposite approach: **strip everything that isn't needed
for Japanese-friendly PDF generation**, leaving only permissively-licensed
dependencies (Apache 2.0 / BSD-3 / OFL).

It also patches the PDF rendering path so the bundled TTF font is registered
through `reportlab`'s `pdfmetrics` directly, avoiding `xhtml2pdf`'s
font-discovery code path that can fail when the host's temp directory contains
non-ASCII characters (a common failure mode on Japanese Windows hosts).

## Differences vs. upstream

| Area | Upstream `md_exporter` | This fork (`md_exporter_jp`) |
|---|---|---|
| Tools shipped | 14 (pdf, png, docx, pptx, xlsx, html, csv, json, xml, md, codeblock, ipynb, latex, html-text) | **1 (`md_to_pdf` only)** |
| Heavy dependencies | PyMuPDF (AGPL), Pandoc (GPL) | **Removed** |
| Bundled font | none | **Noto Sans JP Regular (OFL 1.1)** |
| `md_to_pdf` font registration | `xhtml2pdf` font discovery | Pre-registered via `reportlab.pdfmetrics` |
| `md_to_pdf` orientation | portrait (fixed) | `portrait` / `landscape` (selectable) |

For the full diff and rationale, see [CHANGES.md](CHANGES.md).

## `md_to_pdf` parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `md_text` | string | ✅ | — | Markdown source |
| `output_filename` | string | — | auto | Output file basename (no extension) |
| `orientation` | enum | — | `landscape` | `portrait` or `landscape` (A4) |

## Installation

This fork is **not published** to the Dify Marketplace. Install via package
upload:

1. Download or build a `.difypkg` (see below)
2. In your Dify workspace, go to **Plugins → Install from package**
3. Upload the `.difypkg` file

### Building locally

```bash
git clone https://github.com/SHERPATHJP/md_exporter_jp.git
cd md_exporter_jp

# Pack as .difypkg (no directory entries; Dify's plugin daemon rejects them)
zip -r -D -X md_exporter_jp.difypkg . \
  -x ".git/*" "*.DS_Store" "*/__pycache__/*" "test/*" "dev/*"
```

## What's bundled in the `.difypkg`

The shipped package includes the following license and attribution files:

| File | Purpose |
|---|---|
| `LICENSE.txt` | Apache License 2.0 full text |
| `NOTICE` | SHERPATH copyright + upstream attribution + Noto Sans JP attribution |
| `CHANGES.md` | Apache 2.0 §4(b) modification record (fork commit, modified files) |
| `THIRD_PARTY_LICENSES.md` | Inventory of every third-party dependency and asset license |
| `md_exporter/assets/fonts/OFL.txt` | SIL Open Font License 1.1 full text (for the bundled Noto Sans JP) |

These are also present in the source tree of this repository.

## Dependencies

```
dify_plugin     # Apache 2.0
markdown        # BSD-3-Clause
xhtml2pdf       # Apache 2.0
  └── reportlab  # BSD-3-Clause (transitive, community edition)
```

Bundled assets:
- Noto Sans JP Regular TTF — **SIL Open Font License 1.1**
  (`md_exporter/assets/fonts/NotoSansJP-Regular.ttf`,
  full text in `md_exporter/assets/fonts/OFL.txt`)

For the complete license inventory, see
[`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).

## License

Apache License, Version 2.0 — see [`LICENSE.txt`](LICENSE.txt).

This is a derivative work of
[bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter)
(Apache 2.0). Attribution and modification notes are in
[`NOTICE`](NOTICE) and [`CHANGES.md`](CHANGES.md).

## Acknowledgments

- [bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter) — the upstream we forked
- [xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf) (Apache 2.0)
- [reportlab](https://www.reportlab.com/opensource/) (BSD-3-Clause community edition)
- [Python-Markdown](https://github.com/Python-Markdown/markdown) (BSD-3-Clause)
- [Noto Sans JP](https://fonts.google.com/noto/specimen/Noto+Sans+JP) by Google / Adobe (OFL 1.1)
