# Architecture

## 目的

Web Native Lab は「標準HTML/CSSを知っていれば、そのUIライブラリは必要か？」を考えるための実験サイトです。見た目だけでなく操作性・ブラウザ実装・アクセシビリティにも注目します。

## ファイル構成

- public/index.html: 23実験とソース例（EXP. 006 では datalist と select の違いを比較）
- public/styles.css: UIとCSSの実験
- public/lab-chrome.css: 姉妹サイト共通のヘッダー・フッターとコンテンツ幅
- public/app.js: dialog起動、フォーム送信結果の表示、output計算結果の更新のみ
- public/assets/: picture切り替え・イメージマップ・動画posterのローカルSVG
- public/favicon.svg: アイコン
- public/robots.txt / sitemap.xml: クローラー向け
- scripts/check_site.py: ビルド不要の参照チェック
- .github/workflows/site.yml: PR検証 + mainデプロイ

## 共通ヘッダー・フッター

`public/lab-chrome.css` は `naoiw/web-native-lab` と `naoiw/css-native-lab` で同一内容です。最大コンテンツ幅を1360pxに統一し、ヘッダー・フッターのフォント、文字サイズ、間隔、スマホ表示も一致させています。サイト名・ロゴ記号・アクセントカラー・MDNリンク先は各サイト固有です。共通デザインを変更する際は両方のCSSを更新してください。CSSファイルはそれぞれのリポジトリ内で配信し、相互のデプロイには依存しません。

## 実験追加ルール

1. デモに固有のアンカー、タイトル、説明を付ける
2. NO JS / SMALL JS / EXPERIMENTAL を正確に付ける
3. ブラウザで操作できるプレビューを用意する
4. ソースを最小コードで示し、実装と意味が食い違わないようにする
5. MDNへのリンクを付ける
6. 実際の対応状況と制限事項を確認する
7. 外部ライブラリを追加しない。必要な事情があればまずIssueで検討する

## ブラウザ互換性

ブラウザのバージョン、OS、ユーザー設定で一部の表示・挙動は異なります。本サイトは機能の存在を示すものであり、完全な互換性を保証しません。

ダイアログは `showModal()` にJavaScriptを使用し、フォームの検証はHTML標準で実行していますが結果メッセージ表示にはJavaScriptを使用します。EXP. 015の `output` 計算結果を動的更新するためにもJavaScriptを使います。

- EXP. 016: `details[name]` の排他的開閉には対応ブラウザが必要
- EXP. 018: `picture` はviewport幅800pxを境に画像が切り替わり、コンテナ幅を変更しても画像は切り替わらない
- EXP. 019: イメージマップは固定座標（300×160）。デモは縮小せず横スクロールさせる
- EXP. 020: audio/videoタグは標準だが、ソースのみMDNのCC0外部メディアを使用する。オフラインでは再生不可
- EXP. 022: 宣言的Shadow DOMはHTMLパーサーで生成するため、コンテンツをinnerHTMLで後挿入する場合と挙動が異なる
- EXP. 023: selectedcontentとcustomizable selectはブラウザ対応状況に差がある。非対応環境では通常のselectにフォールバック
- file inputのファイルはブラウザ内で選択するだけであり、外部へのアップロードは行わない

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
