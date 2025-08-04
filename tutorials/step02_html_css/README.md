# Step 2: Flask + HTML + CSS でページ返却

## 🎯 このステップで学ぶこと

- **HTMLテンプレート**の概念と利用方法（Jinja2）
- **ベーステンプレート**による効率的なHTML管理
- **テンプレート継承**と**ブロック**の仕組み
- **静的ファイル**（CSS・画像）の配信方法
- **基本的なCSS**によるスタイリング

## 📚 対応する理論学習

このステップは以下のドキュメントと連携しています：
- `docs/03_Web構成要素/01_必須_HTML：Webページの骨組み.md`
- `docs/03_Web構成要素/02_推奨_CSS：見た目とレイアウト.md`
- `docs/02_Web基礎理解/04_推奨_ブラウザの役割と処理の流れ.md`

## 🚀 実践内容

### 作成するアプリケーション
- **ToDoリスト表示機能**：サンプルデータを使った表示
- **HTMLテンプレート**：Jinja2によるテンプレートエンジン
- **ベーステンプレート**：共通レイアウトの管理
- **基本的なスタイリング**：CSS による見た目の改善

### ファイル構成
```
step02_html_css/
├── README.md              # このファイル
├── app.py                # テンプレート対応Flaskアプリ
├── requirements.txt      # 必要なパッケージ
├── templates/            # HTMLテンプレート
│   ├── base.html         # ベーステンプレート
│   └── todo_list.html    # ToDoリスト表示ページ
├── static/               # 静的ファイル
│   ├── css/
│   │   └── style.css     # スタイルシート
│   └── images/
│       └── favicon.ico   # ファビコン
└── docs/
    └── 解説_HTMLテンプレートとCSS.md
```

## 📝 セットアップ手順

### 1. このフォルダに移動
```powershell
cd tutorials/step02_html_css
```

### 2. 仮想環境の作成・有効化
```powershell
# 仮想環境作成
python -m venv venv

# 仮想環境有効化 (Windows)
venv\Scripts\activate
```

### 3. Flaskのインストール
```powershell
pip install -r requirements.txt
```

### 4. アプリケーションの実行
```powershell
python app.py
```

### 5. ブラウザで確認
- http://localhost:5000 - ToDoリストページ
- http://localhost:5000/about - アプリケーション説明

## 🔍 学習ポイント

### 1. テンプレートエンジン（Jinja2）とは？

**Step 1との違い**:
```python
# Step 1: HTML文字列を直接返却
return "<h1>Hello World</h1>"

# Step 2: HTMLテンプレートファイルを使用
return render_template('todo_list.html', todos=todo_data)
```

**テンプレートの利点**:
- **コードの分離**: PythonコードとHTMLを別ファイルで管理
- **再利用性**: 共通部分を一箇所で管理
- **保守性**: HTMLの修正が簡単
- **動的コンテンツ**: Python変数をHTMLに表示

### 2. ベーステンプレートの仕組み

**テンプレート継承**:
```html
<!-- base.html: 共通レイアウト -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav>共通ナビゲーション</nav>
    {% block content %}{% endblock %}
    <footer>共通フッター</footer>
</body>
</html>

<!-- todo_list.html: 個別ページ -->
{% extends "base.html" %}  <!-- base.htmlを継承 -->
{% block title %}ToDoリスト{% endblock %}
{% block content %}
    <h1>今日のToDo</h1>
    <!-- ここに個別のコンテンツ -->
{% endblock %}
```

**継承の利点**:
- ナビゲーションやフッターを一箇所で管理
- 新しいページを簡単に追加
- サイト全体のデザイン統一

### 3. 静的ファイルの管理

**静的ファイルとは**:
- **CSS**: スタイル（色・フォント・レイアウト）
- **JavaScript**: 動的な動作（Step 3で学習）
- **画像**: ロゴ・アイコン・写真

**Flaskでの配信**:
```python
# staticフォルダに配置したファイルが自動で配信される
static/css/style.css → http://localhost:5000/static/css/style.css
```

**HTMLテンプレートでの読み込み**:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

### 4. 基本的なCSSスタイリング

**基本的なスタイル**:
- **色**: 背景色、文字色
- **フォント**: 文字サイズ、フォントファミリー
- **スペース**: パディング（内側の余白）、マージン（外側の余白）
- **ボーダー**: 枠線、角丸

## 🎨 Jinja2テンプレートの基本機能

### 変数の表示
```html
<!-- Python変数をHTMLに表示 -->
<h1>{{ page_title }}</h1>
<p>総タスク数: {{ stats.total }}</p>
```

### 条件分岐
```html
{% if todo.completed %}
    <span>完了済み</span>
{% else %}
    <span>未完了</span>
{% endif %}
```

### ループ処理
```html
{% for todo in todos %}
    <div class="todo-card">
        <h3>{{ todo.title }}</h3>
        <p>{{ todo.description }}</p>
    </div>
{% endfor %}
```

## 🎓 Step 1からの進歩

| 項目 | Step 1 | Step 2 |
|------|--------|--------|
| **HTML** | Python内で文字列記述 | テンプレートファイルで管理 |
| **CSS** | なし | 外部CSSファイルでスタイリング |
| **構造** | 単一ファイル | HTMLとPythonを分離 |
| **データ表示** | 固定文字列 | 動的データ表示 |
| **保守性** | 低い | 高い（ファイル分離による） |

## 🎓 次のステップへ

Step 2完了後は **Step 3: JavaScript DOM操作** に進みます。  
ここで学んだHTMLテンプレートにJavaScriptを追加して、ボタンクリックなどの操作機能を実装します。

## 💡 エラーが発生した場合

### よくあるエラーと対処法

1. **TemplateNotFound**
   - `templates/` フォルダが存在しない
   - HTMLファイル名のスペルミス

2. **404 Not Found（静的ファイル）**
   - `static/` フォルダの構成を確認
   - CSS・画像ファイルのパスを確認

3. **CSS が適用されない**
   - ブラウザキャッシュをクリア（Ctrl+F5）
   - HTMLでのCSS読み込みパスを確認

4. **レスポンシブが動作しない**
   - `<meta name="viewport">` タグの確認
   - メディアクエリの記述確認

---

**🔥 重要**: このステップではHTMLテンプレートの仕組みが最も重要です！  
テンプレート継承とJinja2の基本をしっかり理解してから次に進みましょう。