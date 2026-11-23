# Web Native Lab

ブラウザ標準のHTML・CSS・Web APIを、実際に触って確かめる実験カタログです。

- **Live demo**: ページ上でそのまま操作
- **Source**: 各サンプルの「ソースを見る」から最小実装を確認
- **No framework**: React / Vue / UIライブラリを使用しない
- **No build**: Node.js、npm、ビルドツール不要
- **Progressive enhancement**: 可能な限りHTMLとCSSのみ。必要な場合だけ少量のJavaScriptを使用

公開先（Pages設定後）: https://naoiw.github.io/web-native-lab/

## コンテンツ

| セクション | 実験 | JS |
| --- | --- | --- |
| HTML / Interaction | details / summary | 不要 |
| HTML / Interaction | Popover API | 不要 |
| HTML / Interaction | dialog / showModal | 開くために必要 |
| Forms / Feedback | date / color / range | 不要 |
| Forms / Feedback | Constraint Validation | 検証はHTML標準、デモ送信結果の表示のみJS |
| Forms / Feedback | datalist | 不要 |
| Forms / Feedback | progress / meter | 不要（値の動的変更にはJSなどが必要） |
| CSS / Layout | :has() | 不要 |
| CSS / Layout | Container Queries | 不要 |
| CSS / Layout | Scroll Snap | 不要 |

## ローカル実行

静的ファイルなので public/index.html を直接開けます。ローカルサーバーを使う場合:

    python3 -m http.server 8000 --directory public

ブラウザで http://localhost:8000 を開いてください。

## チェック

    python3 scripts/check_site.py

外部依存なしでHTMLのローカル参照先とページ内アンカーをチェックします。完全なHTML構文バリデータではありません。

## GitHub Pages

.github/workflows/site.yml で検証とデプロイを自動化しています。

1. Settings → Pages → Build and deployment → Source を **GitHub Actions** に設定
2. main へのpushで validate 実行後、GitHub Pagesへ公開
3. PR時は validate のみ実行。Rulesetsでは **validate** を必須チェックに指定可能

デプロイ対象は public/ のみです。環境変数、シークレット、npm install は不要です。

## 設計指針

- サンプルの **NO JS / SMALL JS** を明示
- すべてのサンプルにMDNの参照リンクを付与
- ブラウザによる実装や外観の違いは自然なものとして扱う
- アクセシビリティを優先し、キーボードで試せるようにする
- サンプルのHTML/CSS/JSの責務を混同しない

追加すると面白い候補は、dialogの非モーダル表示、form-associated custom elements、CSS anchor positioning、@starting-style、View Transitions、HTML autocomplete属性などです。ブラウザ対応状況を確認してから追加します。

## License

[MIT](LICENSE)
