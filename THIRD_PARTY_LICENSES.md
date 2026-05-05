# Third-Party Licenses

This document inventories the licenses of all third-party software bundled
in or required by this plugin.

## Build profile: PDF-only (commercial-safe)

This build deliberately removes all tools and dependencies that require
AGPL or GPL licenses. The result is safe for closed-source commercial
distribution under Apache 2.0.

### Removed (vs upstream `bowenliang123/md_exporter`)

| Removed dependency | License | Reason |
|--------------------|---------|--------|
| `PyMuPDF` (`fitz`) | AGPL-3.0 (or commercial) | Used only by `md_to_png` — tool removed |
| `pypandoc-binary` (bundled `pandoc`) | wrapper MIT, bundled binary GPL-2.0+ | Used by `md_to_docx` / `md_to_pptx` / `md_to_md` — tools removed |
| `pandas[excel,html,xml]` | BSD-3-Clause | Not needed without xlsx/csv tools |
| `pillow` | HPND | Not needed without image tools |

### Removed tools

`md_to_codeblock`, `md_to_csv`, `md_to_docx`, `md_to_html`, `md_to_html_text`,
`md_to_ipynb`, `md_to_json`, `md_to_latex`, `md_to_md`, `md_to_png`,
`md_to_pptx`, `md_to_xlsx`, `md_to_xml`.

Only `md_to_pdf` is shipped.

## Bundled assets

| Asset | License |
|-------|---------|
| Noto Sans JP Regular TTF (`md_exporter/assets/fonts/NotoSansJP-Regular.ttf`) | SIL Open Font License 1.1 (full text in `OFL.txt`) |

## Python dependencies (`requirements.txt`)

| Package | License | Used by |
|---------|---------|---------|
| `dify_plugin` | Apache 2.0 | core |
| `markdown` | BSD-3-Clause | `md_to_pdf` (markdown → HTML) |
| `xhtml2pdf` | Apache 2.0 | `md_to_pdf` (HTML → PDF) |
| `reportlab` (transitive of xhtml2pdf, community edition) | BSD-3-Clause | `md_to_pdf` (font registration) |

All licenses are permissive and compatible with closed-source commercial
distribution.

## Apache 2.0 attribution

This plugin is a fork of `bowenliang123/markdown-exporter`
(<https://github.com/bowenliang123/markdown-exporter>), licensed under
Apache License 2.0. See `LICENSE.txt` and `NOTICE` for full attribution
and `CHANGES.md` for the list of modifications.
