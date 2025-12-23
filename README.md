# Webflow管理画面日本語化 Chrome拡張機能

<div align="center">

**英語が苦手でもWebflowを快適に使える！**

Webflowの管理画面を日本語化し、デザイン作業に集中できる環境を提供します。

</div>

---

## 📖 概要

**Webflowは素晴らしいノーコードWebデザインツールですが、英語表示が障壁となることがあります。**

この拡張機能は、Webflowの管理画面（Designer/Editor/Dashboard等）の英語UIを日本語に自動変換します。

### 主な機能

- ✅ **Webflow専用設計** - *.webflow.comドメインでのみ動作（他のサイトには影響しません）
- ✅ **リアルタイム翻訳** - ページ読み込み時および動的に追加される要素も自動翻訳
- ✅ **226個以上のWebflow専門用語** - Designer、Navigator、Style Panel等の専門用語に対応
- ✅ **カスタマイズ可能** - CSVファイルで翻訳用語を自由に追加・編集可能
- ✅ **プライバシー重視** - データを外部サーバーに送信しません
- ✅ **軽量・高速** - ページ表示速度に影響を与えません

### 対応する用語カテゴリ

- デザインツール: Elements, Navigator, Style Panel, Interactions
- CMS機能: Collections, Assets, Dynamic Content
- レイアウト: Flexbox, Grid, Positioning, Spacing
- スタイリング: Typography, Colors, Effects, Transforms
- 公開・設定: Publishing, Hosting, SEO Settings, Custom Code
- アカウント: Dashboard, Team, Billing, Permissions

---

## 🚀 インストール方法

### Chrome Web Storeからインストール（推奨）
※現在、審査申請準備中です。公開され次第、こちらにリンクを掲載します。

### 開発版を手動でインストール
1. このリポジトリをダウンロードまたはクローンします
   ```bash
   git clone https://github.com/yourusername/webflow-ja-extension.git
   ```

2. Google Chromeで `chrome://extensions/` を開きます

3. 右上の「デベロッパーモード」をONにします

4. 「パッケージ化されていない拡張機能を読み込む」をクリックし、ダウンロードしたフォルダを選択します

5. Webflow（https://*.webflow.com）にアクセスして、日本語化を確認してください

---

## 💡 使い方

### 基本的な使用方法

1. 拡張機能をインストール後、Webflowの管理画面にアクセスするだけで自動的に日本語化されます

2. 翻訳が適用されない場合は、ページを再読み込み（F5）してください

### オプション設定

拡張機能のアイコンを右クリック → 「オプション」から以下の機能が利用できます:

- 📋 **用語集一覧表示** - 現在登録されている全ての翻訳用語を確認
- 🔍 **翻訳プレビュー** - テキストを入力して翻訳結果をテスト

---

## 🛠️ 翻訳用語のカスタマイズ

`translation_terms.csv` ファイルを編集することで、翻訳用語を追加・変更できます。

### 編集方法

1. `translation_terms.csv` をテキストエディタまたはExcel/Googleスプレッドシートで開きます

2. 以下の形式で用語を追加します:
   ```csv
   English Term,Japanese Translation
   Your Custom Term,あなたのカスタム用語
   ```

3. ファイルを保存します

4. Chrome拡張機能ページ（`chrome://extensions/`）で本拡張機能の「再読み込み」ボタンをクリックします

5. Webflowのページを再読み込みして、新しい翻訳を確認します

### Googleスプレッドシートで管理する場合

1. Googleスプレッドシートで用語集を管理
2. ファイル → ダウンロード → カンマ区切り形式（.csv）
3. ダウンロードしたファイルで `translation_terms.csv` を上書き
4. 拡張機能を再読み込み

---

## 🔒 プライバシーとセキュリティ

### この拡張機能は以下を保証します:

- ❌ **外部サーバーへのデータ送信なし** - 翻訳処理はすべてブラウザ内で完結
- ❌ **個人情報の収集なし** - ユーザーデータを一切収集しません
- ✅ **Webflow専用動作** - `*.webflow.com` ドメインでのみ機能
- ✅ **オープンソース** - コードは全て公開され、監査可能

### 必要な権限

- `storage` - 将来的な設定保存機能用（現在は使用していません）
- `host_permissions: https://*.webflow.com/*` - Webflowサイトでのみ翻訳機能を実行

---

## 🐛 トラブルシューティング

### 翻訳が適用されない場合

1. ページを再読み込み（F5キー）してください
2. 拡張機能が有効になっているか `chrome://extensions/` で確認
3. 拡張機能を一度無効化 → 再度有効化してみてください
4. それでも解決しない場合は、拡張機能の「再読み込み」をクリック

### 一部のテキストが翻訳されない場合

- Webflowは頻繁にUIを更新しています
- 新しい用語が追加された可能性があります
- `translation_terms.csv` に該当する用語を追加してください
- GitHubのIssuesで報告いただけると、次回のアップデートで対応します

---

## 📝 開発者向け情報

### ファイル構成

```
webflow-ja-extension/
├── manifest.json              # 拡張機能の設定ファイル
├── content.js                 # メインの翻訳ロジック
├── utils.js                   # CSV解析等のユーティリティ関数
├── options.html               # オプションページのHTML
├── options.js                 # オプションページのロジック
├── translation_terms.csv      # 翻訳用語集（226語以上）
├── icon16.png                 # アイコン 16x16
├── icon48.png                 # アイコン 48x48
├── icon128.png                # アイコン 128x128
└── README.md                  # このファイル
```

### 技術スタック

- Manifest V3（最新のChrome拡張機能仕様）
- Vanilla JavaScript（フレームワーク不使用で軽量）
- MutationObserver（動的要素の監視）
- TreeWalker API（効率的なDOM走査）

---

## 🤝 コントリビューション

プルリクエストや改善提案を歓迎します！

### 貢献方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 翻訳用語の追加リクエスト

GitHubのIssuesで以下の情報と共に報告してください:
- 翻訳されていない英語の用語
- その用語が表示されるWebflow内の場所
- 推奨する日本語訳（任意）

---

## 📄 ライセンス

MIT License - 自由に使用・改変・配布できます。

---

## ⚠️ 免責事項

- この拡張機能は非公式プロジェクトであり、Webflow, Inc.とは一切関係ありません
- Webflowの公式サポート外の使用となりますので、ご理解の上ご利用ください
- UIの翻訳は機械的な置換であり、文脈によっては不自然な訳になる場合があります

---

## 📧 お問い合わせ

- バグ報告・機能要望: [GitHub Issues](https://github.com/yourusername/webflow-ja-extension/issues)
- その他のお問い合わせ: [あなたのメールアドレス]

---

<div align="center">

**Webflowを日本語で、もっと快適に。**

⭐ このプロジェクトが役立ったら、GitHubでスターをお願いします！

</div> 