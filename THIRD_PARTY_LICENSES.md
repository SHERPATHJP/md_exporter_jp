# Third-Party Licenses

This document inventories the licenses of all third-party software bundled
in or required by this plugin. Required reading before commercial
distribution.

## ⚠️ Important Notice for Commercial Use

The full upstream tool set declares dependencies on `PyMuPDF` (AGPL-3.0 or
commercial) and `pypandoc-binary` (which bundles `pandoc`, GPL-2.0+).
Whether these dependencies are actually distributed depends on which subset
of tools is enabled. **If this plugin is distributed in a commercial
product, the operator should decide whether to:**

1. **Use the "PDF-only" build** — keep only `md_to_pdf` and remove PyMuPDF
   and pandoc-related tools. This eliminates AGPL/GPL exposure entirely.
2. **Obtain a commercial license** — purchase a PyMuPDF commercial license
   from Artifex (https://artifex.com/licensing/) and audit pandoc usage.
3. **Comply with AGPL/GPL terms** — release the larger work under
   compatible terms (rarely desirable for commercial SaaS).

For the SHERPATH Week1 workflow, only `md_to_pdf` is used, so option (1)
is recommended and trivially achievable by removing the unused tool
directories before redistribution.

## Bundled Assets

| Asset | License | Required Action |
|-------|---------|-----------------|
| Noto Sans JP Regular TTF (`md_exporter/assets/fonts/NotoSansJP-Regular.ttf`) | SIL Open Font License 1.1 | Include `OFL.txt` (done) |

## Python Dependencies (from `pyproject.toml`)

| Package | License | Tools Affected | Risk for Commercial Distribution |
|---------|---------|----------------|----------------------------------|
| `markdown` | BSD-3-Clause | All | None |
| `pandas[excel,html,xml]` | BSD-3-Clause | xlsx/csv/html | None |
| `jinja2` | BSD-3-Clause | (transitive) | None |
| `xhtml2pdf` | Apache 2.0 | pdf | None |
| `reportlab` | BSD-3-Clause (community) | pdf (transitive) | None — community edition is BSD-3 |
| `Pillow` | HPND (permissive, MIT-CMU style) | png/pdf images | None |
| **`PyMuPDF`** (a.k.a. `fitz`) | **AGPL-3.0 OR Commercial (Artifex)** | `md_to_png` only | **HIGH** — see notice above |
| **`pypandoc-binary`** | MIT (wrapper) + bundled `pandoc` is **GPL-2.0+** | `md_to_html`, indirectly `md_to_docx`/`md_to_pptx` | **HIGH** if `pandoc` binary is redistributed |
| `dify_plugin` | Apache 2.0 (Dify) | All | None |

## Tool-by-Tool Risk Matrix

| Tool | Uses AGPL/GPL? | Safe for closed-source commercial distribution? |
|------|----------------|---------------------------------------------------|
| `md_to_pdf` | ❌ No | ✅ Yes |
| `md_to_codeblock` | ❌ No | ✅ Yes |
| `md_to_csv` | ❌ No | ✅ Yes |
| `md_to_json` | ❌ No | ✅ Yes |
| `md_to_xml` | ❌ No | ✅ Yes |
| `md_to_md` | ❌ No | ✅ Yes |
| `md_to_xlsx` | ❌ No | ✅ Yes |
| `md_to_latex` | ❌ No | ✅ Yes |
| `md_to_ipynb` | ❌ No | ✅ Yes |
| `md_to_png` | ⚠️ **PyMuPDF (AGPL)** | ❌ Requires Artifex commercial license |
| `md_to_html` | ⚠️ **pypandoc + pandoc (GPL)** | ❌ Distribution of pandoc binary problematic |
| `md_to_html_text` | ⚠️ **pypandoc + pandoc (GPL)** | ❌ Same |
| `md_to_docx` | ⚠️ Indirect via pandoc | ❌ Same |
| `md_to_pptx` | ⚠️ Indirect via pandoc | ❌ Same |

## License Texts

- Apache License 2.0: `LICENSE.txt` (in this distribution)
- SIL Open Font License 1.1: `md_exporter/assets/fonts/OFL.txt`
- Other dependency licenses: see each package's PyPI page or installation
  metadata. The container/runtime that installs these packages should
  surface their license texts to end users where required.

## Recommended Commercial Distribution Steps

1. Decide which tools to ship. For Week1 workflow → **only `md_to_pdf`**.
2. Strip unused tool directories from the package before bundling.
3. Audit the resulting wheel/package set with a license scanner
   (e.g., `pip-licenses`, `licensecheck`).
4. Surface OSS attribution to end users (e.g., a "Licenses" page in your
   product UI listing every third-party component).
5. Have legal counsel review the final bundle before commercial release.
