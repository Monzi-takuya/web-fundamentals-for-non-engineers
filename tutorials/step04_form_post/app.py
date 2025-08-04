"""
Step 4: Flask フォーム処理とPOST通信
HTMLフォームを使ったデータ送信とサーバー処理の基礎
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

# Flaskアプリケーションの初期化
app = Flask(__name__)

# フラッシュメッセージ用のシークレットキー（本番環境では必ず変更してください）
app.secret_key = 'step4-learning-secret-key'

# サンプル ToDo データ（メモリ上で管理）
# Step 5でデータベースに移行予定
todo_data = [
    {
        'id': 1,
        'title': 'Flask基礎学習を完了する',
        'description': 'Step 1からStep 4まで順番に学習する',
        'priority': 'high',
        'created_at': '2024-01-15'
    },
    {
        'id': 2,
        'title': 'フォーム処理を理解する',
        'description': 'POST通信とデータ送信の仕組みを学ぶ',
        'priority': 'medium',
        'created_at': '2024-01-16'
    }
]

# 次のIDを管理する変数
next_id = 3

@app.route('/')
def index():
    """
    ToDoリスト表示ページ（メインページ）
    フォーム送信後はここにリダイレクトされる
    """
    # データの集計
    total_todos = len(todo_data)
    
    # テンプレートに渡すデータを準備
    template_data = {
        'todos': todo_data,
        'total_todos': total_todos,
        'current_date': datetime.now().strftime('%Y年%m月%d日'),
        'page_title': 'ToDoリスト - フォーム送信機能'
    }
    
    return render_template('index.html', **template_data)

@app.route('/add')
def add_form():
    """
    新しいタスク追加フォームページ
    GETリクエストでフォーム表示
    """
    return render_template('add_todo.html', page_title='新しいタスクを追加')

@app.route('/add', methods=['POST'])
def add_todo():
    """
    新しいタスク追加処理
    POSTリクエストでフォームデータを受信
    """
    global next_id
    
    # フォームデータを取得
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'medium')
    
    # 基本的なバリデーション
    if not title:
        flash('タスクのタイトルは必須です', 'error')
        return redirect(url_for('add_form'))
    
    if len(title) > 100:
        flash('タイトルは100文字以内で入力してください', 'error')
        return redirect(url_for('add_form'))
    
    # 新しいタスクを作成
    new_todo = {
        'id': next_id,
        'title': title,
        'description': description if description else 'なし',
        'priority': priority,
        'created_at': datetime.now().strftime('%Y-%m-%d')
    }
    
    # メモリ上のデータに追加
    todo_data.append(new_todo)
    next_id += 1
    
    # 成功メッセージを表示
    flash(f'タスク「{title}」を追加しました', 'success')
    
    # メインページにリダイレクト
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """
    タスク削除処理
    POSTリクエストで削除実行
    """
    global todo_data
    
    # 指定されたIDのタスクを検索
    todo_to_delete = None
    for todo in todo_data:
        if todo['id'] == todo_id:
            todo_to_delete = todo
            break
    
    if todo_to_delete:
        # タスクを削除
        todo_data.remove(todo_to_delete)
        flash(f'タスク「{todo_to_delete["title"]}」を削除しました', 'success')
    else:
        flash('削除するタスクが見つかりません', 'error')
    
    # メインページにリダイレクト
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """
    Step 4の説明ページ
    フォーム処理機能の概要
    """
    features = [
        {
            'name': 'HTMLフォーム',
            'description': 'ユーザー入力を受け取るフォーム',
            'status': 'implemented'
        },
        {
            'name': 'POST通信',
            'description': 'データをサーバーに送信',
            'status': 'implemented'
        },
        {
            'name': 'バリデーション',
            'description': '入力値の検証処理',
            'status': 'implemented'
        },
        {
            'name': 'フラッシュメッセージ',
            'description': '操作結果のフィードバック',
            'status': 'implemented'
        }
    ]
    
    step_info = {
        'current_step': 4,
        'total_steps': 5,
        'step_name': 'フォーム処理とPOST通信',
        'next_step': 'データベース連携',
        'previous_step': 'JavaScript DOM操作'
    }
    
    template_data = {
        'features': features,
        'step_info': step_info,
        'page_title': 'Step 4について - フォーム処理とPOST通信'
    }
    
    return render_template('about.html', **template_data)

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    """
    return {
        'status': 'OK',
        'message': 'Step4 フォーム処理・POST通信 アプリケーションが動作しています',
        'step': 4,
        'description': 'HTMLフォーム + POST通信 + バリデーション',
        'features': {
            'form_processing': True,
            'post_requests': True,
            'flash_messages': True,
            'basic_validation': True,
            'data_count': len(todo_data)
        },
        'endpoints': [
            {'url': '/', 'description': 'ToDoリスト表示'},
            {'url': '/add', 'description': 'タスク追加フォーム（GET・POST）'},
            {'url': '/delete/<id>', 'description': 'タスク削除（POST）'},
            {'url': '/about', 'description': 'Step 4説明'},
            {'url': '/health', 'description': 'ヘルスチェック'}
        ]
    }

# このファイルが直接実行された場合のみWebサーバーを起動
if __name__ == '__main__':
    print("🚀 Flask Step4 フォーム処理とPOST通信 サーバーを起動します...")
    print("📍 アクセスURL: http://localhost:5000")
    print("📝 新機能: HTMLフォーム、POST通信、バリデーション")
    print("💬 フラッシュメッセージ対応")
    print("🛑 停止方法: Ctrl+C")
    
    # 開発サーバーの起動
    app.run(debug=True, host='127.0.0.1', port=5000)