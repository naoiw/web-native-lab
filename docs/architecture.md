# Architecture

## 目的

Web Native Lab は「標準HTML/CSSを知っていれば、そのUIライブラリは必要か？」を考えるための実験サイトです。見た目だけでなく操作性・ブラウザ実装・アクセシビリティにも注目します。

## ファイル構成

- public/index.html: 全デモとソース例（EXP. 006 では datalist と select の違いを比較）
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

## 公開環境・デプロイ運用

- 本番URL: https://naoiw.github.io/web-native-lab/ （GitHub Pagesで公開中）
- PagesのSourceは **GitHub Actions**
- `.github/workflows/site.yml` で検証後、`public/` のみデプロイ
- `deploy` は `main` のpushまたは `main` での手動実行のみ。PRでは `validate` だけを実行する
- `main` はRuleset `Protect main` で保護。Require status checks の設定対象は `validate`（`deploy` は対象外）
- 公開にはNode.jsやビルドツール、シークレットは不要

## datalist と select のUX上の違い

- `datalist` は入力支援用。通常の `select` と異なり候補外の値も入力可能で、入力値に基づく候補の絞り込みやポップアップ操作にはブラウザ差がある
- `select` は選択用。選択後もプルダウンから全候補を開き直せる。自由入力不可
- EXP. 006 では、ユーザーが使い分けを体験できるように2種類を併設。どちらもJavaScript不要
- `datalist` の見た目・候補の再表示はJavaScriptで独自に改変せず、ブラウザ標準の挙動を示す
