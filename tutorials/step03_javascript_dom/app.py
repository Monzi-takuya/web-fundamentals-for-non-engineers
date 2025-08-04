"""
Step 3: Flask + HTML + CSS + JavaScript でインタラクティブなWebページ
DOM操作とイベント処理による動的なWebページの作成
"""

from flask import Flask, render_template, jsonify, request
from datetime import datetime

# Flaskアプリケーションの初期化
app = Flask(__name__)

# サンプル ToDo データ（後のステップではデータベースから取得）
todo_sample_data = [
    {
        'id': 1,
        'title': 'Flask学習を完了する',
        'description': 'Step 1からStep 5まで順番に学習する',
        'completed': False,
        'priority': 'high',
        'created_at': '2024-01-15'
    },
    {
        'id': 2,
        'title': 'HTMLとCSSを理解する',
        'description': 'テンプレートエンジンとスタイリングの基礎を学ぶ',
        'completed': True,
        'priority': 'medium',
        'created_at': '2024-01-14'
    },
    {
        'id': 3,
        'title': 'JavaScript DOM操作を学習',
        'description': '動的なWebページ作成の基礎',
        'completed': False,
        'priority': 'medium',
        'created_at': '2024-01-16'
    },
    {
        'id': 4,
        'title': 'データベース連携を実装',
        'description': 'SQLiteを使った永続化の実装',
        'completed': False,
        'priority': 'low',
        'created_at': '2024-01-17'
    },
    {
        'id': 5,
        'title': 'JavaScriptでDOM操作を体験',
        'description': 'ボタンクリックで要素を表示・非表示・変更',
        'completed': False,
        'priority': 'high',
        'created_at': '2024-01-18'
    }
]

@app.route('/')
def index():
    """
    ToDoリスト表示ページ（メインページ）
    HTMLテンプレートにサンプルデータを渡して表示
    """
    # データの集計
    total_todos = len(todo_sample_data)
    completed_todos = len([todo for todo in todo_sample_data if todo['completed']])
    pending_todos = total_todos - completed_todos
    
    # 完了率の計算
    completion_rate = round((completed_todos / total_todos) * 100) if total_todos > 0 else 0
    
    # テンプレートに渡すデータを準備
    template_data = {
        'todos': todo_sample_data,
        'stats': {
            'total': total_todos,
            'completed': completed_todos,
            'pending': pending_todos,
            'completion_rate': completion_rate
        },
        'current_date': datetime.now().strftime('%Y年%m月%d日'),
        'page_title': 'ToDoリスト - JavaScript インタラクション'
    }
    
    # HTMLテンプレートを使ってページを生成
    return render_template('todo_list.html', **template_data)

@app.route('/about')
def about():
    """
    アプリケーション説明ページ
    Step 3で新しく追加される機能の説明
    """
    # アプリの機能一覧
    features = [
        {
            'name': 'HTMLテンプレート',
            'description': 'Jinja2を使用したテンプレートエンジン',
            'status': 'implemented'
        },
        {
            'name': 'CSS スタイリング',
            'description': '基本的なスタイリングとレイアウト',
            'status': 'implemented'
        },
        {
            'name': 'JavaScript DOM操作',
            'description': '要素の取得・作成・削除・変更',
            'status': 'implemented'
        },
        {
            'name': 'イベント処理',
            'description': 'ボタンクリック・フォーム入力への反応',
            'status': 'implemented'
        },
        {
            'name': '動的コンテンツ',
            'description': 'ページ読み込み後の内容変更',
            'status': 'implemented'
        }
    ]
    
    # Step情報
    step_info = {
        'current_step': 3,
        'total_steps': 5,
        'step_name': 'JavaScript DOM操作',
        'next_step': 'フォーム送信・POST処理',
        'previous_step': 'HTML + CSS テンプレート'
    }
    
    template_data = {
        'features': features,
        'step_info': step_info,
        'page_title': 'Step 3について - JavaScript DOM操作'
    }
    
    return render_template('about.html', **template_data)

# ===== Step 3で新規追加: JavaScript機能用API =====

@app.route('/api/toggle-todo/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    """
    ToDoの完了状態を切り替える（JavaScriptから呼び出される）
    """
    for todo in todo_sample_data:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            return jsonify({
                'success': True,
                'todo_id': todo_id,
                'completed': todo['completed'],
                'message': f"タスク「{todo['title']}」を{'完了'if todo['completed'] else '未完了'}に変更しました"
            })
    
    return jsonify({'success': False, 'message': 'タスクが見つかりません'}), 404

@app.route('/api/hide-todo/<int:todo_id>', methods=['POST'])
def hide_todo(todo_id):
    """
    ToDoを一時的に非表示にする（学習用機能）
    """
    return jsonify({
        'success': True,
        'todo_id': todo_id,
        'message': f"タスクID {todo_id} を非表示にしました（学習用機能）"
    })

@app.route('/api/show-completed', methods=['GET'])
def show_completed():
    """
    完了済みタスクのみを返す
    """
    completed_todos = [todo for todo in todo_sample_data if todo['completed']]
    return jsonify({
        'success': True,
        'todos': completed_todos,
        'count': len(completed_todos)
    })

@app.route('/api/show-pending', methods=['GET'])
def show_pending():
    """
    未完了タスクのみを返す
    """
    pending_todos = [todo for todo in todo_sample_data if not todo['completed']]
    return jsonify({
        'success': True,
        'todos': pending_todos,
        'count': len(pending_todos)
    })

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    Step 3の機能が正常に動作しているかチェック
    """
    # テンプレートフォルダの確認
    template_status = True
    static_status = True
    
    try:
        # テンプレートが正常に読み込めるかテスト
        render_template('base.html')
    except:
        template_status = False
    
    return {
        'status': 'OK' if template_status and static_status else 'Warning',
        'message': 'Step3 Flask+HTML+CSS+JavaScript アプリケーションが動作しています',
        'step': 3,
        'description': 'JavaScript DOM操作とイベント処理',
        'features': {
            'templates': template_status,
            'static_files': static_status,
            'javascript_api': True,
            'sample_data_count': len(todo_sample_data)
        },
        'endpoints': [
            {'url': '/', 'description': 'ToDoリスト表示'},
            {'url': '/about', 'description': 'アプリケーション説明'},
            {'url': '/api/toggle-todo/<id>', 'description': 'タスク完了切り替え'},
            {'url': '/api/hide-todo/<id>', 'description': 'タスク非表示'},
            {'url': '/api/show-completed', 'description': '完了済みタスク表示'},
            {'url': '/api/show-pending', 'description': '未完了タスク表示'},
            {'url': '/health', 'description': 'ヘルスチェック'}
        ]
    }

# カスタムフィルター（テンプレートで使用）
@app.template_filter('priority_class')
def priority_class(priority):
    """
    優先度に応じたCSSクラスを返すフィルター
    """
    priority_classes = {
        'high': 'priority-high',
        'medium': 'priority-medium', 
        'low': 'priority-low'
    }
    return priority_classes.get(priority, 'priority-low')

@app.template_filter('status_icon')
def status_icon(completed):
    """
    完了状態に応じたアイコンを返すフィルター
    """
    return '✅' if completed else '⏰'

# このファイルが直接実行された場合のみWebサーバーを起動
if __name__ == '__main__':
    print("🚀 Flask Step3 JavaScript DOM操作 サーバーを起動します...")
    print("📍 アクセスURL: http://localhost:5000")
    print("🎨 新機能: JavaScript DOM操作、イベント処理")
    print("⚡ インタラクティブ機能: ボタンクリック、動的表示")
    print("🛑 停止方法: Ctrl+C")
    
    # 開発サーバーの起動
    app.run(debug=True, host='127.0.0.1', port=5000)