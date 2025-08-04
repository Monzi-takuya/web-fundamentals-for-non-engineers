# 応用: Jinja2カスタムフィルター詳細解説

## 🎯 このドキュメントの目的

**応用レベル**のJinja2カスタムフィルターについて詳しく解説します。  
基本的なテンプレート機能を理解した後に学習してください。

## 📋 前提知識

この解説を理解するには以下の知識が必要です：
- ✅ Jinja2テンプレートの基本（変数表示・条件分岐・ループ）
- ✅ Python関数の基本的な書き方
- ✅ Flaskアプリケーションの基本構造

## 🔧 カスタムフィルターとは？

### 1. フィルターの概念

**フィルター**とは、テンプレート内でデータを変換・加工する機能です。

```html
<!-- 基本的な使い方 -->
{{ 変数名 | フィルター名 }}

<!-- 実例 -->
{{ user_name | upper }}  <!-- 大文字に変換 -->
{{ price | round(2) }}   <!-- 小数点2桁で四捨五入 -->
```

### 2. 標準フィルター vs カスタムフィルター

#### 標準フィルター（Jinja2に最初から用意されている）
```html
{{ "hello world" | title }}     <!-- "Hello World" -->
{{ [1, 2, 3] | length }}        <!-- 3 -->
{{ "2024-01-15" | replace("-", "/") }}  <!-- "2024/01/15" -->
```

#### カスタムフィルター（自分で作成する）
```html
{{ todo.priority | priority_class }}    <!-- "priority-high" -->
{{ todo.completed | status_icon }}      <!-- "✅" または "⏰" -->
{{ todo.created_at | days_ago }}        <!-- "3日前" -->
```

## 📝 カスタムフィルターの基本文法

### 1. 基本的な関数の定義

```python
@app.template_filter('フィルター名')
def フィルター関数名(値):
    """フィルターの説明"""
    # 値を加工する処理
    return 加工した値
```

### 2. 実際の例

```python
@app.template_filter('japanese_date')
def japanese_date(date_string):
    """日付を日本語形式に変換"""
    # "2024-01-15" → "2024年1月15日"
    year, month, day = date_string.split('-')
    return f"{year}年{int(month)}月{int(day)}日"
```

**テンプレートでの使用:**
```html
<p>作成日: {{ todo.created_at | japanese_date }}</p>
<!-- 結果: 作成日: 2024年1月15日 -->
```

## 🎨 実践的なカスタムフィルター例

### 1. 優先度に応じたCSSクラス

```python
@app.template_filter('priority_class')
def priority_class(priority):
    """優先度に応じたCSSクラス名を返す"""
    priority_classes = {
        'high': 'priority-high',      # 高優先度
        'medium': 'priority-medium',  # 中優先度
        'low': 'priority-low'         # 低優先度
    }
    return priority_classes.get(priority, 'priority-low')  # デフォルト値
```

**使用例:**
```html
<div class="todo-card {{ todo.priority | priority_class }}">
    <h3>{{ todo.title }}</h3>
</div>

<!-- 結果例 -->
<div class="todo-card priority-high">
    <h3>Flask学習を完了する</h3>
</div>
```

### 2. 完了状態のアイコン表示

```python
@app.template_filter('status_icon')
def status_icon(completed):
    """完了状態に応じたアイコンを返す"""
    return '✅' if completed else '⏰'
```

**使用例:**
```html
<span class="status-icon">{{ todo.completed | status_icon }}</span>
<span class="status-text">
    {{ '完了' if todo.completed else '未完了' }}
</span>
```

### 3. 日付の相対表示

```python
from datetime import datetime, date

@app.template_filter('days_ago')
def days_ago(date_string):
    """日付から何日前かを計算"""
    try:
        # "2024-01-15" 形式から日付オブジェクトに変換
        target_date = datetime.strptime(date_string, '%Y-%m-%d').date()
        today = date.today()
        
        # 日数の差を計算
        days_diff = (today - target_date).days
        
        if days_diff == 0:
            return "今日"
        elif days_diff == 1:
            return "昨日"
        elif days_diff < 7:
            return f"{days_diff}日前"
        elif days_diff < 30:
            weeks = days_diff // 7
            return f"{weeks}週間前"
        else:
            months = days_diff // 30
            return f"{months}ヶ月前"
    except:
        return date_string  # エラー時は元の値を返す
```

**使用例:**
```html
<p class="created-date">
    📅 {{ todo.created_at | days_ago }}に作成
</p>
<!-- 結果例: 📅 3日前に作成 -->
```

## 🔢 引数を持つカスタムフィルター

### 1. 単一引数のフィルター

```python
@app.template_filter('truncate_jp')
def truncate_jp(text, length=20):
    """日本語対応の文字列切り取り"""
    if len(text) <= length:
        return text
    return text[:length] + "..."
```

**使用例:**
```html
<!-- 引数なし（デフォルト20文字） -->
<p>{{ todo.description | truncate_jp }}</p>

<!-- 引数あり（10文字で切り取り） -->
<p>{{ todo.description | truncate_jp(10) }}</p>
```

### 2. 複数引数のフィルター

```python
@app.template_filter('highlight')
def highlight(text, keyword, css_class='highlight'):
    """指定したキーワードをハイライト"""
    if not keyword:
        return text
    
    highlighted = text.replace(
        keyword, 
        f'<span class="{css_class}">{keyword}</span>'
    )
    return highlighted
```

**使用例:**
```html
<!-- デフォルトCSSクラス -->
<p>{{ todo.description | highlight('Flask') }}</p>

<!-- カスタムCSSクラス -->
<p>{{ todo.description | highlight('Flask', 'custom-highlight') }}</p>
```

## 🛡️ 安全な出力とHTMLエスケープ

### 1. HTMLを含むフィルターの注意点

```python
from markupsafe import Markup

@app.template_filter('priority_badge')
def priority_badge(priority):
    """優先度バッジのHTMLを生成"""
    badges = {
        'high': '<span class="badge badge-danger">🔴 高</span>',
        'medium': '<span class="badge badge-warning">🟡 中</span>',
        'low': '<span class="badge badge-success">🟢 低</span>'
    }
    
    html = badges.get(priority, badges['low'])
    return Markup(html)  # HTMLとして安全にマーク
```

**使用例:**
```html
<!-- HTMLタグがそのまま出力される -->
<div class="priority">
    {{ todo.priority | priority_badge }}
</div>
```

### 2. 危険な例（避けるべき）

```python
# ❌ 危険：ユーザー入力をそのままHTMLに
@app.template_filter('dangerous_html')
def dangerous_html(user_input):
    return f'<div>{user_input}</div>'  # XSS攻撃の可能性
```

## 📊 実践的な活用例

### 1. 数値の表示フォーマット

```python
@app.template_filter('format_number')
def format_number(value):
    """数値を3桁区切りで表示"""
    try:
        return f"{int(value):,}"
    except:
        return value

@app.template_filter('percentage')
def percentage(value, total):
    """パーセンテージを計算"""
    try:
        if total == 0:
            return "0%"
        return f"{round((value / total) * 100)}%"
    except:
        return "0%"
```

**使用例:**
```html
<p>総タスク数: {{ stats.total | format_number }}</p>
<!-- 結果: 総タスク数: 1,234 -->

<p>完了率: {{ stats.completed | percentage(stats.total) }}</p>
<!-- 結果: 完了率: 75% -->
```

### 2. 文字列の変換・整形

```python
@app.template_filter('snake_to_title')
def snake_to_title(snake_str):
    """snake_case を Title Case に変換"""
    return ' '.join(word.capitalize() for word in snake_str.split('_'))

@app.template_filter('add_emoji')
def add_emoji(status):
    """ステータスに応じた絵文字を追加"""
    emoji_map = {
        'completed': '✅',
        'in_progress': '🔄',
        'pending': '⏳',
        'cancelled': '❌'
    }
    emoji = emoji_map.get(status, '❓')
    return f"{emoji} {status.replace('_', ' ').title()}"
```

**使用例:**
```html
<h3>{{ 'user_profile' | snake_to_title }}</h3>
<!-- 結果: User Profile -->

<span class="status">{{ todo.status | add_emoji }}</span>
<!-- 結果: ✅ Completed -->
```

## 🎯 フィルターチェーン（連続適用）

### 複数フィルターの組み合わせ

```html
<!-- フィルターを連続で適用 -->
{{ todo.title | truncate_jp(15) | upper }}

<!-- 実行順序 -->
1. todo.title を truncate_jp(15) で15文字に切り取り
2. その結果を upper で大文字に変換
```

### 実践例

```html
<div class="todo-summary">
    <span class="priority">{{ todo.priority | priority_badge }}</span>
    <span class="title">{{ todo.title | truncate_jp(20) }}</span>
    <span class="date">{{ todo.created_at | days_ago }}</span>
</div>
```

## 🧪 フィルターのテスト方法

### 1. 単体でのテスト

```python
# Pythonコンソールまたは別ファイルでテスト
def test_filters():
    # days_ago フィルターのテスト
    result = days_ago('2024-01-10')
    print(f"days_ago test: {result}")
    
    # priority_class フィルターのテスト
    result = priority_class('high')
    print(f"priority_class test: {result}")

if __name__ == '__main__':
    test_filters()
```

### 2. テンプレートでのデバッグ

```html
<!-- デバッグ用：フィルター適用前後の値を表示 -->
<p>元の値: {{ todo.priority }}</p>
<p>フィルター後: {{ todo.priority | priority_class }}</p>
```

## ⚠️ 注意点とベストプラクティス

### 1. エラーハンドリング

```python
@app.template_filter('safe_divide')
def safe_divide(value, divisor):
    """安全な割り算（ゼロ除算対応）"""
    try:
        if divisor == 0:
            return "N/A"
        return round(value / divisor, 2)
    except (TypeError, ValueError):
        return "エラー"
```

### 2. パフォーマンスの考慮

```python
# ❌ 避けるべき：重い処理をフィルター内で実行
@app.template_filter('slow_filter')
def slow_filter(value):
    # データベースアクセスや重い計算は避ける
    # time.sleep(1)  # 重い処理の例
    return value

# ✅ 推奨：軽量な変換処理のみ
@app.template_filter('light_filter')
def light_filter(value):
    return str(value).strip().title()
```

### 3. 命名規則

```python
# ✅ 推奨：分かりやすい名前
@app.template_filter('format_currency')     # 通貨フォーマット
@app.template_filter('time_since')          # 経過時間
@app.template_filter('status_color')        # ステータス色

# ❌ 避けるべき：略語や不明確な名前
@app.template_filter('fmt')                 # 何をフォーマットするか不明
@app.template_filter('proc')                # 何を処理するか不明
```

## 🚀 応用課題

### 自分で作ってみよう

以下のカスタムフィルターを作成してみてください：

1. **`file_size`**: バイト数を人間が読みやすい形式に（例：1024 → "1KB"）
2. **`color_by_value`**: 数値に応じて色を決定（例：高い値→赤、低い値→青）
3. **`markdown_to_html`**: 簡単なMarkdown記法をHTMLに変換
4. **`mask_email`**: メールアドレスを部分的に隠す（例：user@example.com → u***@example.com）

## 💭 よくある質問

### Q1: フィルターはどこに定義すべき？
**A**: 小規模なら`app.py`内、大規模なら別ファイル（`filters.py`など）に分離

### Q2: フィルターとPython関数の違いは？
**A**: フィルターはテンプレート専用、Python関数は汎用。フィルターは`@app.template_filter`でFlaskに登録

### Q3: 標準フィルターで十分な場合は？
**A**: カスタムフィルターは必要最小限に。まず標準フィルターで実現できないか検討

### Q4: フィルターの引数は何個まで？
**A**: 制限はないが、可読性のため2-3個程度に抑える

---

**カスタムフィルターを使いこなして、テンプレートをより効率的で読みやすくしましょう！**