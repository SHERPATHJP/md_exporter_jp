#!/usr/bin/env python3
"""
Markdown to PDF conversion service (Japanese-enabled fork)
Provides Markdown to PDF conversion with proper Japanese/CJK font rendering
using bundled Noto Sans JP TTF font.

Modified from original by SHERPATH for Japanese language support.
Original: https://github.com/bowenliang123/markdown-exporter (Apache 2.0)

Implementation notes:
- Bundles Noto Sans JP TTF (SIL OFL).
- Pre-registers the TTF with reportlab's pdfmetrics so xhtml2pdf does not need
  to write the font to a temporary file (which fails on environments where the
  temp path contains non-ASCII characters).
- Patches xhtml2pdf's pisaContext on first use to expose the registered font
  via xhtml2pdf's internal fontList. This avoids the @font-face CSS path
  entirely and lets the conversion just refer to ``font-family: NotoSansJP``.
- Page orientation is selectable via the ``orientation`` parameter
  (``portrait`` or ``landscape``, default ``landscape``).
"""

from pathlib import Path

from ..utils.markdown_utils import convert_markdown_to_html, get_md_text
from ..utils.text_utils import contains_chinese, contains_japanese

# Bundled Japanese font (Noto Sans JP, SIL Open Font License)
_FONT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"
_FONT_FILE = _FONT_DIR / "NotoSansJP-Regular.ttf"
_FONT_FAMILY = "NotoSansJP"

_initialized = False


def _initialize_font() -> None:
    """Register the bundled Japanese TTF and patch xhtml2pdf to use it.

    Idempotent: safe to call multiple times.
    """
    global _initialized
    if _initialized:
        return

    if not _FONT_FILE.exists():
        msg = f"Bundled font missing: {_FONT_FILE}"
        raise FileNotFoundError(msg)

    from reportlab.pdfbase import pdfmetrics  # noqa: PLC0415
    from reportlab.pdfbase.pdfmetrics import registerFontFamily  # noqa: PLC0415
    from reportlab.pdfbase.ttfonts import TTFont  # noqa: PLC0415
    from xhtml2pdf import context as _xhtml_ctx  # noqa: PLC0415

    pdfmetrics.registerFont(TTFont(_FONT_FAMILY, str(_FONT_FILE)))
    pdfmetrics.registerFont(TTFont(f"{_FONT_FAMILY}-Bold", str(_FONT_FILE)))
    pdfmetrics.registerFont(TTFont(f"{_FONT_FAMILY}-Italic", str(_FONT_FILE)))
    pdfmetrics.registerFont(TTFont(f"{_FONT_FAMILY}-BoldItalic", str(_FONT_FILE)))
    registerFontFamily(
        _FONT_FAMILY,
        normal=_FONT_FAMILY,
        bold=f"{_FONT_FAMILY}-Bold",
        italic=f"{_FONT_FAMILY}-Italic",
        boldItalic=f"{_FONT_FAMILY}-BoldItalic",
    )

    _orig_init = _xhtml_ctx.pisaContext.__init__

    def _patched_init(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        _orig_init(self, *args, **kwargs)
        self.fontList[_FONT_FAMILY.lower()] = _FONT_FAMILY
        self.asianFontsRegistered = True

    _xhtml_ctx.pisaContext.__init__ = _patched_init
    _initialized = True


def _build_css(orientation: str) -> str:
    """Build the CSS block applied to Japanese/Chinese content."""
    page_size = "A4 landscape" if orientation == "landscape" else "A4 portrait"
    return f"""
    <style>
        @page {{
            size: {page_size};
            margin: 1.5cm;
        }}
        html, body, p, h1, h2, h3, h4, h5, h6, ul, ol, li, td, th, blockquote, pre, code, em, strong, span, div {{
            font-family: '{_FONT_FAMILY}', sans-serif;
            -pdf-word-wrap: CJK;
        }}
        body {{ font-size: 11pt; line-height: 1.6; }}
        h1 {{ font-size: 18pt; margin-top: 16pt; margin-bottom: 8pt; }}
        h2 {{ font-size: 15pt; margin-top: 14pt; margin-bottom: 6pt; }}
        h3 {{ font-size: 13pt; margin-top: 12pt; margin-bottom: 4pt; }}
        strong, b {{ font-weight: bold; }}
        em, i {{ font-style: italic; }}
        code, pre {{
            background-color: #f4f4f4;
            padding: 2pt 4pt;
            border-radius: 3pt;
        }}
        blockquote {{
            border-left: 3pt solid #ccc;
            padding-left: 8pt;
            margin-left: 0;
            color: #555;
        }}
        table {{ border-collapse: collapse; margin: 8pt 0; }}
        th, td {{ border: 1pt solid #ccc; padding: 4pt 8pt; }}
        th {{ background-color: #f0f0f0; }}
    </style>
    """


def convert_to_html_with_font_support(md_text: str, orientation: str = "landscape") -> str:
    """Convert Markdown to HTML; apply CJK font CSS only when needed."""
    html_str = convert_markdown_to_html(md_text)

    if not contains_chinese(md_text) and not contains_japanese(md_text):
        return html_str

    _initialize_font()
    return f"""
    {_build_css(orientation)}
    {html_str}
    """


def convert_md_to_pdf(
    md_text: str,
    output_path: Path,
    is_strip_wrapper: bool = False,
    orientation: str = "landscape",
) -> None:
    """Convert Markdown text to PDF format with Japanese support.

    Args:
        md_text: Markdown text to convert
        output_path: Path to save the output PDF file
        is_strip_wrapper: Whether to remove code block wrapper if present
        orientation: ``portrait`` or ``landscape`` (default: ``landscape``).
    """
    from xhtml2pdf import pisa  # noqa: PLC0415

    if orientation not in ("portrait", "landscape"):
        orientation = "landscape"

    processed_md = get_md_text(md_text, is_strip_wrapper=is_strip_wrapper)
    html_str = convert_to_html_with_font_support(processed_md, orientation=orientation)

    result_file_bytes = pisa.CreatePDF(
        src=html_str,
        dest_bytes=True,
        encoding="utf-8",
        capacity=400 * 1024 * 1024,
    )

    output_path.write_bytes(result_file_bytes)
