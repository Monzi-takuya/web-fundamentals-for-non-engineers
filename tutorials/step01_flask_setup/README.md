# Step 1: Flask基礎セットアップ / Hello World

## 🎯 このステップで学ぶこと

- **仮想環境**の概念と作成方法
- **Flask**の基本構造とWebサーバーの仕組み
- **ルーティング**の基本概念
- **HTTP GETリクエスト**の処理方法

## 📚 対応する理論学習

このステップは以下のドキュメントと連携しています：
- `docs/01_コンピューター基礎知識/06_推奨_プログラミング言語という道具箱.md`
- `docs/02_Web基礎理解/02_必須_クライアントサーバーモデル.md`

## 🚀 実践内容

### 作成するアプリケーション
- 最小限のFlaskアプリケーション
- "Hello World" と "ToDoアプリへようこそ" の表示
- 複数のページ（ルート）の実装

### ファイル構成
```
step01_flask_setup/
├── README.md           # このファイル
├── app.py             # メインのFlaskアプリケーション
├── requirements.txt   # 必要なパッケージ
└── docs/
    └── 解説_Flask基礎とWebサーバー.md
```

## 📝 セットアップ手順

### 1. このフォルダに移動
```powershell
cd tutorials/step01_flask_setup
```

### 2. 仮想環境の作成・有効化
```powershell
# 仮想環境作成
python -m venv venv

# 仮想環境有効化 (Windows)
venv\Scripts\activate

# 仮想環境有効化確認（プロンプトに(venv)が表示される）
```

### 3. Flaskのインストール
```powershell
pip install -r requirements.txt
```

### 4. アプリケーションの実行

#### Pythonスクリプトの実行方法の基本

**`python ファイル名.py` コマンドの仕組み**：

```powershell
python app.py
```

**このコマンドが何をしているか：**
- `python`: **Pythonインタープリター**（Python言語を理解して実行するプログラム）を起動
- `app.py`: 実行したい**Pythonスクリプトファイル**を指定

**初学者が知っておくべきポイント**：

1. **拡張子 `.py` の意味**
   - `.py` = Pythonスクリプトファイルを示す拡張子
   - コンピューターが「これはPythonで書かれたプログラムだ」と認識

2. **他のファイルでも同じ方法で実行可能**
   ```powershell
   python hello.py        # hello.pyを実行
   python calculator.py   # calculator.pyを実行
   python game.py         # game.pyを実行
   ```

3. **実行の流れ**
   ```mermaid
   flowchart LR
   A["python app.py<br/>コマンド実行"] --> B["Pythonインタープリター<br/>がapp.pyを読み込み"]
   B --> C["コードを1行ずつ<br/>解釈・実行"]
   C --> D["結果をコンソールや<br/>ブラウザに表示"]
   ```

**実際の実行**：
```powershell
python app.py
```

### 5. ブラウザで確認
- http://localhost:5000 - ホームページ
- http://localhost:5000/hello - Hello Worldページ  
- http://localhost:5000/about - アプリケーション説明

## 🔍 学習ポイント

### 1. 仮想環境とは？
- **目的**: プロジェクトごとに独立したPython環境を作成
- **利点**: パッケージの競合を避け、プロジェクトを分離
- **実際の開発**: 必ず仮想環境を使用する

#### `python -m venv venv` コマンドの詳細解説

```powershell
python -m venv venv
```

**コマンドの構造**:
- `python`: Pythonインタープリターを実行
- `-m venv`: **venvモジュール**を実行（`-m`はモジュール実行オプション）
- `venv`: **作成する仮想環境のフォルダ名**（これは自由に変更可能）

**初学者が混乱しやすいポイント**:
```powershell
# 最初の 'venv' = Pythonの標準モジュール名（固定）
# 後ろの 'venv' = 作成するフォルダ名（自由に変更可能）

python -m venv my_project     # my_projectフォルダに仮想環境作成
python -m venv todo_env       # todo_envフォルダに仮想環境作成  
python -m venv .venv          # .venvフォルダに仮想環境作成（よく使われる）
```

**フォルダ名の慣習**:
- `venv` : 一般的（このチュートリアルで使用）
- `.venv` : 隠しフォルダとして作成（プロジェクトによく使われる）
- `env` : 短縮版
- `プロジェクト名_env` : プロジェクト固有の名前

**作成後のフォルダ構造**:
```
tutorials/step01_flask_setup/
├── venv/                    # ← これが作成される仮想環境
│   ├── Scripts/            # Windows用実行ファイル
│   ├── Lib/                # インストールされるパッケージ
│   └── pyvenv.cfg          # 仮想環境設定ファイル
├── app.py
└── requirements.txt
```

### 2. Flaskの基本構造
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')          # URLルーティング
def index():             # 関数名は自由
    return "Hello World" # レスポンス内容

if __name__ == '__main__':
    app.run(debug=True)  # 開発サーバー起動
```

### 3. ルーティングの仕組み
- `@app.route('/')` = URLパスとPython関数を結びつける
- `/` = ルートパス (http://localhost:5000/)
- `/hello` = http://localhost:5000/hello にアクセス可能

### 4. Webサーバーとしての動作
- **クライアント**: ブラウザがHTTP GETリクエストを送信
- **サーバー**: Flaskアプリがリクエストを受信・処理
- **レスポンス**: HTML文字列をブラウザに返却

## 🎓 次のステップへ

Step 1完了後は **Step 2: HTML+CSS** に進みます。  
ここで学んだルーティングの概念を使って、より本格的なWebページを作成します。

## 💡 エラーが発生した場合

### よくあるエラーと対処法
1. **ModuleNotFoundError: No module named 'flask'**
   - 仮想環境が有効化されていない可能性
   - `venv\Scripts\activate` を実行してから `pip install flask`

2. **Address already in use**
   - ポート5000が使用中
   - `python app.py` の代わりに別のポートを指定

3. **仮想環境が作成できない**
   - Pythonのインストールを確認
   - PowerShellの実行ポリシーを確認

---

**🔥 重要**: このステップをしっかり理解してから次に進みましょう！  
仮想環境とFlaskの基本はすべての基礎になります。