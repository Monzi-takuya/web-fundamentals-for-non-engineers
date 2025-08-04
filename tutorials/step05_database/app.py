"""
Step 5: Flask + SQLiteデータベース連携
完全なCRUD操作とデータ永続化の実現
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import os

# Flaskアプリケーションの初期化
app = Flask(__name__)

# フラッシュメッセージ用のシークレットキー（本番環境では必ず変更してください）
app.secret_key = 'step5-database-secret-key'

# データベースファイルのパス
DATABASE = 'todo_app.db'

def get_db_connection():
    """
    データベース接続を取得する共通関数
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 辞書形式でデータを取得
    return conn

def init_db_if_not_exists():
    """
    データベースが存在しない場合は初期化する
    """
    if not os.path.exists(DATABASE):
        print(f"⚠️  データベースファイル {DATABASE} が見つかりません。")
        print("📊 初期化スクリプトを実行してください: python init_db.py")
        return False
    return True

@app.route('/')
def index():
    """
    ToDoリスト表示ページ（メインページ）
    データベースから全てのタスクを取得して表示
    """
    if not init_db_if_not_exists():
        return render_template('error.html', 
                             error_message="データベースが初期化されていません。先に 'python init_db.py' を実行してください。")
    
    conn = get_db_connection()
    
    # タスクを取得（新しい順に並び替え）
    todos = conn.execute('''
        SELECT id, title, description, priority, completed, created_at, updated_at
        FROM todos 
        ORDER BY created_at DESC
    ''').fetchall()
    
    # 統計情報を計算
    total_todos = len(todos)
    completed_todos = sum(1 for todo in todos if todo['completed'])
    pending_todos = total_todos - completed_todos
    
    conn.close()
    
    template_data = {
        'todos': todos,
        'total_todos': total_todos,
        'completed_todos': completed_todos,
        'pending_todos': pending_todos,
        'current_date': datetime.now().strftime('%Y年%m月%d日'),
        'page_title': 'ToDoリスト - データベース連携'
    }
    
    return render_template('index.html', **template_data)

@app.route('/add')
def add_form():
    """
    新しいタスク追加フォームページ
    """
    return render_template('add_todo.html', page_title='新しいタスクを追加')

@app.route('/add', methods=['POST'])
def add_todo():
    """
    新しいタスク追加処理
    データベースに永続保存
    """
    # フォームデータを取得
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'medium')
    
    # バリデーション
    if not title:
        flash('タスクのタイトルは必須です', 'error')
        return redirect(url_for('add_form'))
    
    if len(title) > 200:
        flash('タイトルは200文字以内で入力してください', 'error')
        return redirect(url_for('add_form'))
    
    # データベースに挿入
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO todos (title, description, priority, completed, created_at, updated_at)
            VALUES (?, ?, ?, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        ''', (title, description if description else None, priority))
        
        conn.commit()
        new_id = cursor.lastrowid
        
        flash(f'タスク「{title}」を追加しました（ID: {new_id}）', 'success')
        
    except sqlite3.Error as e:
        flash(f'データベースエラー: {str(e)}', 'error')
        conn.rollback()
    finally:
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>')
def edit_form(todo_id):
    """
    タスク編集フォームページ
    """
    conn = get_db_connection()
    
    todo = conn.execute('''
        SELECT id, title, description, priority, completed, created_at
        FROM todos 
        WHERE id = ?
    ''', (todo_id,)).fetchone()
    
    conn.close()
    
    if not todo:
        flash('指定されたタスクが見つかりません', 'error')
        return redirect(url_for('index'))
    
    return render_template('edit_todo.html', todo=todo, page_title=f'タスクを編集 - {todo["title"]}')

@app.route('/edit/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    """
    タスク更新処理
    """
    # フォームデータを取得
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'medium')
    completed = 1 if request.form.get('completed') else 0
    
    # バリデーション
    if not title:
        flash('タスクのタイトルは必須です', 'error')
        return redirect(url_for('edit_form', todo_id=todo_id))
    
    if len(title) > 200:
        flash('タイトルは200文字以内で入力してください', 'error')
        return redirect(url_for('edit_form', todo_id=todo_id))
    
    # データベースを更新
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE todos 
            SET title = ?, description = ?, priority = ?, completed = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (title, description if description else None, priority, completed, todo_id))
        
        if cursor.rowcount == 0:
            flash('指定されたタスクが見つかりません', 'error')
        else:
            conn.commit()
            status_text = "完了" if completed else "未完了"
            flash(f'タスク「{title}」を更新しました（{status_text}）', 'success')
            
    except sqlite3.Error as e:
        flash(f'データベースエラー: {str(e)}', 'error')
        conn.rollback()
    finally:
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """
    タスク削除処理
    """
    conn = get_db_connection()
    try:
        # 削除前にタスク情報を取得
        todo = conn.execute('SELECT title FROM todos WHERE id = ?', (todo_id,)).fetchone()
        
        if not todo:
            flash('指定されたタスクが見つかりません', 'error')
        else:
            # タスクを削除
            cursor = conn.cursor()
            cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
            conn.commit()
            
            flash(f'タスク「{todo["title"]}」を削除しました', 'success')
            
    except sqlite3.Error as e:
        flash(f'データベースエラー: {str(e)}', 'error')
        conn.rollback()
    finally:
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    """
    タスク完了状態の切り替え
    Ajax対応
    """
    conn = get_db_connection()
    try:
        # 現在の状態を取得
        todo = conn.execute('SELECT title, completed FROM todos WHERE id = ?', (todo_id,)).fetchone()
        
        if not todo:
            flash('指定されたタスクが見つかりません', 'error')
        else:
            # 完了状態を切り替え
            new_completed = 0 if todo['completed'] else 1
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE todos 
                SET completed = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE id = ?
            ''', (new_completed, todo_id))
            conn.commit()
            
            status_text = "完了" if new_completed else "未完了"
            flash(f'タスク「{todo["title"]}」を{status_text}に変更しました', 'success')
            
    except sqlite3.Error as e:
        flash(f'データベースエラー: {str(e)}', 'error')
        conn.rollback()
    finally:
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """
    Step 5の説明ページ
    """
    # データベース統計を取得
    conn = get_db_connection()
    
    stats = {}
    try:
        # 基本統計
        stats['total'] = conn.execute('SELECT COUNT(*) FROM todos').fetchone()[0]
        stats['completed'] = conn.execute('SELECT COUNT(*) FROM todos WHERE completed = 1').fetchone()[0]
        stats['pending'] = stats['total'] - stats['completed']
        
        # 優先度別統計
        priority_stats = conn.execute('''
            SELECT priority, COUNT(*) as count 
            FROM todos 
            GROUP BY priority
        ''').fetchall()
        
        stats['by_priority'] = {row['priority']: row['count'] for row in priority_stats}
        
    except sqlite3.Error:
        stats = {'total': 0, 'completed': 0, 'pending': 0, 'by_priority': {}}
    finally:
        conn.close()
    
    features = [
        {
            'name': 'データベース永続化',
            'description': 'SQLiteによる完全なデータ保存',
            'status': 'implemented'
        },
        {
            'name': 'CRUD操作',
            'description': '作成・読み取り・更新・削除の全機能',
            'status': 'implemented'
        },
        {
            'name': 'タスク管理',
            'description': '優先度設定と完了状態管理',
            'status': 'implemented'
        },
        {
            'name': 'データ統計',
            'description': 'リアルタイムな進捗状況表示',
            'status': 'implemented'
        }
    ]
    
    step_info = {
        'current_step': 5,
        'total_steps': 5,
        'step_name': 'データベース連携',
        'next_step': '学習完了！',
        'previous_step': 'フォーム処理・POST通信'
    }
    
    template_data = {
        'features': features,
        'step_info': step_info,
        'stats': stats,
        'page_title': 'Step 5について - データベース連携'
    }
    
    return render_template('about.html', **template_data)

@app.route('/health')
def health_check():
    """
    アプリケーションとデータベースの動作確認用エンドポイント
    """
    db_status = "OK"
    db_info = {}
    
    try:
        conn = get_db_connection()
        
        # データベース統計を取得
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM todos')
        total_count = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM todos WHERE completed = 1')
        completed_count = cursor.fetchone()[0]
        
        db_info = {
            'total_todos': total_count,
            'completed_todos': completed_count,
            'pending_todos': total_count - completed_count,
            'database_file': os.path.abspath(DATABASE),
            'database_size': f"{os.path.getsize(DATABASE) / 1024:.1f} KB" if os.path.exists(DATABASE) else "N/A"
        }
        
        conn.close()
        
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
    
    return {
        'status': 'OK',
        'message': 'Step5 データベース連携 アプリケーションが動作しています',
        'step': 5,
        'description': 'SQLite + CRUD操作 + 完全永続化',
        'database': {
            'status': db_status,
            'info': db_info
        },
        'features': {
            'database_persistence': True,
            'crud_operations': True,
            'data_validation': True,
            'flash_messages': True,
            'task_statistics': True
        },
        'endpoints': [
            {'url': '/', 'description': 'ToDoリスト表示'},
            {'url': '/add', 'description': 'タスク追加フォーム（GET・POST）'},
            {'url': '/edit/<id>', 'description': 'タスク編集フォーム（GET・POST）'},
            {'url': '/delete/<id>', 'description': 'タスク削除（POST）'},
            {'url': '/toggle/<id>', 'description': '完了状態切り替え（POST）'},
            {'url': '/about', 'description': 'Step 5説明'},
            {'url': '/health', 'description': 'ヘルスチェック'}
        ]
    }

# このファイルが直接実行された場合のみWebサーバーを起動
if __name__ == '__main__':
    print("🚀 Flask Step5 データベース連携 サーバーを起動します...")
    print("📍 アクセスURL: http://localhost:5000")
    print("💾 新機能: SQLiteデータベース、CRUD操作、完全永続化")
    print("🔧 初期化: python init_db.py でデータベースを初期化してください")
    print("🛑 停止方法: Ctrl+C")
    
    # 開発サーバーの起動
    app.run(debug=True, host='127.0.0.1', port=5000)