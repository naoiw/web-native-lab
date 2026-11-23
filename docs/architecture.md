# Architecture

## 目的

Web Native Lab は「標準HTML/CSSを知っていれば、そのUIライブラリは必要か？」を考えるための実験サイトです。見た目だけでなく操作性・ブラウザ実装・アクセシビリティにも注目します。

## ファイル構成

- public/index.html: 全デモとソース例
- public/styles.css: UIとCSSの実験
- public/app.js: dialog起動とフォーム送信結果の表示だけ
- public/favicon.svg: アイコン
- public/robots.txt / sitemap.xml: クローラー向け
- scripts/check_site.py: ビルド不要の参照チェック
- .github/workflows/site.yml: PR検証 + mainデプロイ

## 実験追加ルール

1. デモに固有のアンカー、タイトル、説明を付ける
2. NO JS / SMALL JS を正確に付ける
3. ブラウザで操作できるプレビューを用意する
4. ソースを最小コードで示し、実装と意味が食い違わないようにする
5. MDNへのリンクを付ける
6. 実際の対応状況と制限事項を確認する
7. 外部ライブラリを追加しない。必要な事情があればまずIssueで検討する

## ブラウザ互換性

ブラウザのバージョン、OS、ユーザー設定で一部の表示・挙動は異なります。本サイトは機能の存在を示すものであり、完全な互換性を保証しません。

特にダイアログは showModal にJavaScriptを使用し、フォーム検証はHTML標準で実行していますが結果メッセージ表示にはJavaScriptを使用します。

## GitHub Pages

- GitHub Actionsで public/ のみアップロード
- deployは main の push または main での手動実行のみ
- PRではvalidateのみ、デプロイしない
- Required status checkの推奨名: validate
