## 概要

Pythonで求人サイトの検索結果ページを作る
- インストール/環境セットアップからスタート

## 目的
社内の非エンジニアの企画者に対してWebページの表示までの仕組みを学習してもらう
また、Cursorを用いたプログラミングについて、慣れてもらう目的もある
実際にコーディングをするというよりは学習目的のソースコードを読み全体的な流れを学習する趣旨

## 要件
- キーワード、勤務地をパラメータで受け取り検索を行う
- 求人票(ダミーデータ)をDBに登録、検索

## セットアップ手順

### 前提条件
- Python 3.8以上がインストール済みであること
- PowerShellまたはコマンドプロンプトが使用可能であること

### 1. プロジェクトのクローン・移動
```powershell
cd C:\dev\php_tutorial
```

### 2. 仮想環境の作成と有効化
```powershell
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
.\venv\Scripts\Activate.ps1
```

⚠️ PowerShellで実行ポリシーエラーが出る場合：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. 必要なパッケージのインストール
```powershell
pip install flask flask-sqlalchemy
```

### 4. プロジェクト構成
```
php_tutorial/
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
python init_db.py

# Flaskアプリケーションの実行
python app.py
```

アプリケーションは `http://localhost:5000` で実行されます。

### 6. 開発時の便利なコマンド
```powershell
# 仮想環境を無効化
deactivate

# パッケージ一覧の確認
pip list

# requirements.txtの生成
pip freeze > requirements.txt
```

### トラブルシューティング
- **モジュールが見つからない**: 仮想環境が有効化されているか確認
- **ポート5000が使用中**: `python app.py` の代わりに `flask run --port 5001`
- **データベースエラー**: `init_db.py` を再実行してデータベースをリセット