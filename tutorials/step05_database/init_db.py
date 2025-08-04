"""
Step 5: データベース初期化スクリプト
SQLiteデータベースとテーブルの作成
"""

import sqlite3
import os
from datetime import datetime

def init_database():
    """
    データベースとテーブルを初期化する
    """
    # データベースファイルのパス
    db_path = 'todo_app.db'
    
    # 既存のデータベースファイルがあれば削除（開発時のみ）
    if os.path.exists(db_path):
        print(f"⚠️  既存のデータベースファイル {db_path} を削除します...")
        os.remove(db_path)
    
    # SQLiteデータベースに接続（ファイルが存在しなければ自動作成）
    print(f"📊 データベースファイル {db_path} を作成します...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # todosテーブルの作成
    print("📝 todosテーブルを作成します...")
    cursor.execute('''
        CREATE TABLE todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'medium',
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # サンプルデータの挿入
    print("🎯 サンプルデータを挿入します...")
    sample_todos = [
        (
            'Flask基礎学習を完了する',
            'Step 1からStep 5まで順番に学習する',
            'high',
            0,
            '2024-01-15 10:00:00',
            '2024-01-15 10:00:00'
        ),
        (
            'データベース操作を理解する',
            'CRUD操作とSQLの基本を学ぶ',
            'high',
            0,
            '2024-01-16 09:00:00',
            '2024-01-16 09:00:00'
        ),
        (
            'CSS レイアウトの改善',
            'レスポンシブデザインの実装',
            'medium',
            1,
            '2024-01-14 14:30:00',
            '2024-01-17 16:45:00'
        ),
        (
            'JavaScript関数の整理',
            'コードのリファクタリングと最適化',
            'low',
            1,
            '2024-01-13 11:15:00',
            '2024-01-18 10:20:00'
        )
    ]
    
    cursor.executemany('''
        INSERT INTO todos (title, description, priority, completed, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_todos)
    
    # 変更をコミット
    conn.commit()
    
    # データ確認
    cursor.execute('SELECT COUNT(*) FROM todos')
    count = cursor.fetchone()[0]
    print(f"✅ {count}件のサンプルデータを挿入しました")
    
    # 接続を閉じる
    conn.close()
    
    print(f"🎉 データベースの初期化が完了しました！")
    print(f"📁 データベースファイル: {os.path.abspath(db_path)}")
    
    return db_path

def show_table_info():
    """
    テーブル情報を表示する（学習用）
    """
    db_path = 'todo_app.db'
    
    if not os.path.exists(db_path):
        print("❌ データベースファイルが見つかりません。先にinit_database()を実行してください。")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\n📊 テーブル構造:")
    print("=" * 50)
    
    # テーブル情報を取得
    cursor.execute("PRAGMA table_info(todos)")
    columns = cursor.fetchall()
    
    for column in columns:
        col_id, name, data_type, not_null, default_value, pk = column
        pk_mark = " (主キー)" if pk else ""
        null_mark = " NOT NULL" if not_null else ""
        default_mark = f" DEFAULT {default_value}" if default_value else ""
        
        print(f"  {name}: {data_type}{null_mark}{default_mark}{pk_mark}")
    
    print("\n📝 サンプルデータ:")
    print("=" * 50)
    
    # データを表示
    cursor.execute("SELECT id, title, priority, completed, created_at FROM todos LIMIT 5")
    rows = cursor.fetchall()
    
    for row in rows:
        todo_id, title, priority, completed, created_at = row
        status = "✅ 完了" if completed else "⏳ 未完了"
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(priority, "⚪")
        
        print(f"  ID:{todo_id} | {status} | {priority_icon} {priority} | {title}")
        print(f"       作成日: {created_at}")
        print()
    
    conn.close()

if __name__ == '__main__':
    print("🚀 Step 5: データベース初期化を開始します...")
    print()
    
    # データベース初期化
    db_file = init_database()
    
    print()
    
    # テーブル情報表示
    show_table_info()
    
    print("💡 次のステップ:")
    print("  1. python app.py を実行してFlaskアプリを起動")
    print("  2. ブラウザで http://localhost:5000 にアクセス")
    print("  3. データベース連携機能を体験")