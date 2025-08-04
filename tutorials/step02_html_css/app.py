"""
Step 2: Flask + HTML + CSS でページ返却
HTMLテンプレートとCSSを使った本格的なWebページの作成
"""

from flask import Flask, render_template
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
        'page_title': 'ToDoリスト - 今日のタスク'
    }
    
    # HTMLテンプレートを使ってページを生成
    return render_template('todo_list.html', **template_data)

@app.route('/about')
def about():
    """
    アプリケーション説明ページ
    Step 2で新しく追加される機能の説明
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
            'name': 'ベーステンプレート',
            'description': 'HTML構造の効率的な管理',
            'status': 'implemented'
        },
        {
            'name': '静的ファイル配信',
            'description': 'CSS、JavaScript、画像ファイルの管理',
            'status': 'implemented'
        }
    ]
    
    # Step情報
    step_info = {
        'current_step': 2,
        'total_steps': 5,
        'step_name': 'HTML + CSS テンプレート',
        'next_step': 'JavaScript DOM操作',
        'previous_step': 'Flask基礎セットアップ'
    }
    
    template_data = {
        'features': features,
        'step_info': step_info,
        'page_title': 'Step 2について - HTMLテンプレートとCSS'
    }
    
    return render_template('about.html', **template_data)

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    Step 2の機能が正常に動作しているかチェック
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
        'message': 'Step2 Flask+HTML+CSS アプリケーションが動作しています',
        'step': 2,
        'description': 'HTML テンプレート + CSS スタイリング',
        'features': {
            'templates': template_status,
            'static_files': static_status,
            'sample_data_count': len(todo_sample_data)
        },
        'endpoints': [
            {'url': '/', 'description': 'ToDoリスト表示'},
            {'url': '/about', 'description': 'アプリケーション説明'},
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
    print("🚀 Flask Step2 HTMLテンプレート + CSS サーバーを起動します...")
    print("📍 アクセスURL: http://localhost:5000")
    print("🎨 新機能: HTMLテンプレート、基本的なCSS")
    print("📱 基本的なレスポンシブ対応")
    print("🛑 停止方法: Ctrl+C")
    
    # 開発サーバーの起動
    app.run(debug=True, host='127.0.0.1', port=5000)