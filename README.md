## 概要

Pythonで求人サイトの検索結果ページを作る
- インストール/環境セットアップからスタート

## 目的
社内の非エンジニアの企画者に対してWebページの表示までの仕組みを学習してもらう。  
また、Cursorを用いたプログラミングについて、慣れてもらう目的もある。  
実際にコーディングをするというよりは学習目的のソースコードを読み全体的な流れを学習する趣旨。
また、基本的なコンピューターの仕組みなどもフォローする

## 要件
- キーワード、勤務地をパラメータで受け取り検索を行う
- 求人票(ダミーデータ)をDBに登録、検索

## 📚 学習リソース

### パッケージ管理ツールについて学ぶ
- [パッケージ管理ツール学習ガイド](docs/パッケージ管理ツール.md)
  - Pythonだけでなく他言語のパッケージ管理ツールも紹介
  - なぜパッケージ管理が重要なのか
  - 各ツールの特徴とメリット・デメリット
  - 実際の開発現場での使い分け

## セットアップ手順

### 前提条件
- Python 3.8以上がインストール済みであること
- PowerShellまたはコマンドプロンプトが使用可能であること
- uvがインストール済みであること（未インストールの場合は下記参照）

#### uvのインストール（初回のみ）
```powershell
# PowerShellでuvをインストール
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 1. プロジェクトのクローン・移動
```powershell
cd C:\dev\web_tutorial
```

### 2. 仮想環境の作成
```powershell
# 仮想環境を作成（自動で.venvディレクトリが作成される）
uv venv
```

### 3. 必要なパッケージのインストール
```powershell
# パッケージをインストール（仮想環境が自動で有効化される）
uv pip install flask flask-sqlalchemy
```

### 4. プロジェクト構成
```
web_tutorial/
├── app.py              # メインアプリケーション
├── models.py           # データベースモデル
├── init_db.py          # データベース初期化スクリプト
├── requirements.txt    # 依存パッケージ一覧
├── templates/          # HTMLテンプレート
│   ├── index.html      # 検索フォームページ
│   └── results.html    # 検索結果ページ
└── static/             # CSS・JSファイル
    └── style.css       # スタイルシート
```

### 5. アプリケーションの実行
```powershell
# データベースの初期化（初回のみ）
uv run python init_db.py

# Flaskアプリケーションの実行
uv run python app.py
```

アプリケーションは `http://localhost:5000` で実行されます。

### 6. 開発時の便利なコマンド
```powershell
# パッケージ一覧の確認
uv pip list

# requirements.txtの生成
uv pip freeze > requirements.txt

# requirements.txtからパッケージをインストール
uv pip install -r requirements.txt

# 新しいパッケージの追加
uv add パッケージ名

# 仮想環境の状態確認
uv venv --help
```

### uvの利点
- **高速**: pipより大幅に高速なパッケージインストール
- **自動管理**: 仮想環境の自動作成・有効化
- **互換性**: pip と同じコマンドが使用可能
- **シンプル**: 複雑な仮想環境の有効化/無効化が不要

### トラブルシューティング
- **モジュールが見つからない**: `uv venv` で仮想環境を再作成
- **ポート5000が使用中**: `uv run python app.py` の代わりに `uv run flask run --port 5001`
- **データベースエラー**: `uv run python init_db.py` を再実行してデータベースをリセット
- **uvが見つからない**: PowerShellを再起動してuvのパスを更新