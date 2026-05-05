# Changes from upstream

This project (`md_exporter_jp`) is a fork of
[bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter)
licensed under the Apache License, Version 2.0.

This file documents all modifications made by SHERPATH Inc. to the original
work, as required by Section 4(b) of the Apache License 2.0.

## Forked from upstream commit

- Upstream: https://github.com/bowenliang123/markdown-exporter
- Upstream commit at fork point: `c8033c9` (2026-04-16)
- Upstream version at fork point: `3.6.9`
- This fork version: `3.6.11`

## Summary of modifications

The fork adds first-class Japanese language support to the Markdown-to-PDF
conversion path. The CJK rendering of the upstream `md_to_pdf` tool relies on
xhtml2pdf's font discovery, which is unreliable when the host's temporary
file path contains non-ASCII characters (commonly the case on Windows
machines with Japanese user names). The fork bundles a Japanese-capable TTF
font and patches xhtml2pdf's font registration path to avoid that failure
mode.

### Modified files

| File | Change |
|------|--------|
| `manifest.yaml` | Updated author, name, description, version, repo to identify the fork. Original `name: md_exporter` → `name: md_exporter_jp`. |
| `md_exporter/services/svc_md_to_pdf.py` | Reworked PDF rendering path: pre-registers the bundled Noto Sans JP TTF with reportlab's pdfmetrics; patches `xhtml2pdf.context.pisaContext` to expose the registered font via `fontList`; auto-detects Japanese/CJK content and applies `font-family: NotoSansJP`; adds `orientation` parameter (portrait/landscape, default landscape). |
| `provider/md_exporter.yaml` | Updated provider identity (author, name, description, label) to identify the fork. |
| `tools/md_to_pdf/md_to_pdf.py` | Threaded the new `orientation` parameter through to the service layer. |
| `tools/md_to_pdf/md_to_pdf.yaml` | Added `orientation` parameter declaration with select options `portrait` / `landscape`. |

### Added files

| Path | Purpose |
|------|---------|
| `md_exporter/assets/fonts/NotoSansJP-Regular.ttf` | Bundled Japanese TTF used by the modified PDF service. Licensed under SIL Open Font License v1.1. |
| `md_exporter/assets/fonts/OFL.txt` | License text for the bundled font (added in this fork). |
| `NOTICE` | Attribution notice required by Apache License 2.0. |
| `CHANGES.md` | This file. |
| `THIRD_PARTY_LICENSES.md` | Inventory of third-party dependency licenses. |

### Files NOT modified

All other tools (md_to_docx, md_to_xlsx, md_to_pptx, md_to_png,
md_to_html, md_to_csv, md_to_json, md_to_xml, md_to_codeblock,
md_to_ipynb, md_to_latex, md_to_md) remain identical to the upstream
project except for any whitespace or import-ordering differences
introduced incidentally by editor tooling.

## Trademark

`Markdown Exporter`, `bowenliang123`, and the upstream project's icon are
the property of their respective owners. This fork uses them solely for
attribution purposes. The fork's own identifiers (`md_exporter_jp`,
`Markdown Exporter (Japanese-enabled)`) do not assert any trademark over
the upstream project's name.

## License

Both the upstream project and this fork are distributed under the
Apache License, Version 2.0. See `LICENSE.txt` for the full text.

The bundled Noto Sans JP font is distributed under the SIL Open Font
License, Version 1.1. See `md_exporter/assets/fonts/OFL.txt`.
