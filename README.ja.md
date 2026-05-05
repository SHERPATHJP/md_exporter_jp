# md_exporter_jp — Markdown エクスポーター（日本語対応版・PDF専用）

[🇬🇧 English](README.md) | 🇯🇵 日本語

[bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter) を fork した、日本語 PDF 出力に特化した Dify プラグインです。**`md_to_pdf` ツール 1 つだけ**を提供し、同梱した Noto Sans JP フォントで日本語・中国語・韓国語を含む Markdown を PDF として出力します。商用利用に安全な依存ライブラリ構成（Apache 2.0 / BSD-3 / OFL のみ）になっています。

> [`bowenliang123/markdown-exporter`](https://github.com/bowenliang123/markdown-exporter) の commit `c8033c9`（バージョン 3.6.9）から fork。
> [Apache License 2.0](LICENSE.txt) で配布。帰属表示は [NOTICE](NOTICE)、改変履歴は [CHANGES.md](CHANGES.md) を参照。

## 特徴

- **Markdown → PDF** 変換（日本語・中国語・韓国語の文字も正しく描画）
- **Noto Sans JP** TTF フォントを同梱（外部フォント探索が不要）
- **ページ向き** パラメータ（`portrait` / `landscape`、デフォルト `landscape`）
- 純 Python パイプライン: `markdown` + `xhtml2pdf` + `reportlab`
- **AGPL / GPL 依存なし** — クロソース商用配布で安全

## なぜ fork したのか

オリジナルの `bowenliang123/markdown-exporter` は優れたプラグインですが、PDF 以外にも多数の変換ツールを含み、その中には PyMuPDF (AGPL) や同梱 Pandoc (GPL) など強力なコピーレフトライセンスの依存があります。これらを商用クロソース製品で扱うには法的判断が複雑になります。

この fork は逆のアプローチを取り、**日本語 PDF 出力に必要のない部分を全て削除**して、許諾的ライセンス（Apache 2.0 / BSD-3 / OFL）の依存だけを残しました。

加えて、PDF 描画パスを修正して、同梱 TTF フォントを `reportlab` の `pdfmetrics` で直接登録するようにしてあります。これにより、`xhtml2pdf` のフォント探索コードが一時ディレクトリパスに非ASCII文字を含む環境（日本語 Windows ホストでよくあるケース）で失敗する問題を回避しています。

## 上流との差分

| 項目 | 上流 `md_exporter` | この fork (`md_exporter_jp`) |
|---|---|---|
| 提供ツール数 | 14（pdf, png, docx, pptx, xlsx, html, csv, json, xml, md, codeblock, ipynb, latex, html-text） | **1（`md_to_pdf` のみ）** |
| 重い依存 | PyMuPDF (AGPL), Pandoc (GPL) | **削除** |
| 同梱フォント | なし | **Noto Sans JP Regular (OFL 1.1)** |
| `md_to_pdf` のフォント登録 | `xhtml2pdf` のフォント探索 | `reportlab.pdfmetrics` で事前登録 |
| `md_to_pdf` の向き | portrait 固定 | `portrait` / `landscape` 選択可 |

詳細な diff と背景は [CHANGES.md](CHANGES.md) を参照してください。

## `md_to_pdf` のパラメータ

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|---|---|---|---|---|
| `md_text` | string | ✅ | — | 変換元の Markdown |
| `output_filename` | string | — | 自動 | 出力ファイル名（拡張子なし） |
| `orientation` | enum | — | `landscape` | `portrait` または `landscape`（A4） |

## インストール

このプラグインは Dify Marketplace では公開していません。パッケージアップロード方式でインストールしてください。

1. `.difypkg` ファイルを取得（または下記でビルド）
2. Dify ワークスペースの **プラグイン → パッケージからインストール** へ移動
3. `.difypkg` ファイルをアップロード

### ローカルでビルド

```bash
git clone https://github.com/SHERPATHJP/md_exporter_jp.git
cd md_exporter_jp

# .difypkg として固める（ディレクトリエントリは含めない。Dify の plugin daemon が拒否するため）
zip -r -D -X md_exporter_jp.difypkg . \
  -x ".git/*" "*.DS_Store" "*/__pycache__/*" "test/*" "dev/*"
```

## `.difypkg` に同梱されているファイル

公開している `.difypkg` には以下のライセンス・帰属関連ファイルが含まれています:

| ファイル | 内容 |
|---|---|
| `LICENSE.txt` | Apache License 2.0 全文 |
| `NOTICE` | SHERPATH の Copyright + 上流 (bowenliang123) への帰属表示 + Noto Sans JP の帰属表示 |
| `CHANGES.md` | Apache 2.0 §4(b) 準拠の改変記録（fork 元 commit、改変ファイル一覧） |
| `THIRD_PARTY_LICENSES.md` | 第三者依存ライブラリ・アセットのライセンス一覧 |
| `md_exporter/assets/fonts/OFL.txt` | SIL Open Font License 1.1 全文（同梱フォント用） |

これらはこのリポジトリのソースツリーにも同じものが置かれています。

## 依存ライブラリ

```
dify_plugin     # Apache 2.0
markdown        # BSD-3-Clause
xhtml2pdf       # Apache 2.0
  └── reportlab  # BSD-3-Clause（推移依存・コミュニティ版）
```

同梱アセット:
- Noto Sans JP Regular TTF — **SIL Open Font License 1.1**
  （`md_exporter/assets/fonts/NotoSansJP-Regular.ttf`、
  全文は `md_exporter/assets/fonts/OFL.txt`）

依存ライブラリのライセンス一覧の完全版は
[`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) を参照してください。

## ライセンス

Apache License, Version 2.0 — [`LICENSE.txt`](LICENSE.txt) を参照。

このプラグインは
[bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter)
（Apache 2.0）の派生物です。帰属表示と改変記録は
[`NOTICE`](NOTICE) と [`CHANGES.md`](CHANGES.md) にあります。

## 謝辞

- [bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter) — fork 元
- [xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf)（Apache 2.0）
- [reportlab](https://www.reportlab.com/opensource/)（BSD-3-Clause コミュニティ版）
- [Python-Markdown](https://github.com/Python-Markdown/markdown)（BSD-3-Clause）
- [Noto Sans JP](https://fonts.google.com/noto/specimen/Noto+Sans+JP) by Google / Adobe（OFL 1.1）
