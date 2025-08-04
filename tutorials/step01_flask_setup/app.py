"""
Step 1: Flask基礎セットアップ / Hello World
最小限のFlaskアプリケーション - ルーティングの基本を学ぶ
"""

from flask import Flask

# Flaskアプリケーションの初期化
# __name__ は現在のPythonモジュール名を表す
app = Flask(__name__)

@app.route('/')
def index():
    """
    ホームページ（ルートURL）
    http://localhost:5000/ にアクセスした時に表示される
    """
    return """
    <h1>🎯 Flask学習 - Step 1</h1>
    <h2>ToDoアプリへようこそ！</h2>
    <p>これは最初のFlaskアプリケーションです。</p>
    <ul>
        <li><a href="/hello">Hello Worldページ</a></li>
        <li><a href="/about">このアプリについて</a></li>
    </ul>
    <hr>
    <p><strong>学習ポイント:</strong></p>
    <ul>
        <li>✅ 仮想環境の作成・有効化</li>
        <li>✅ Flaskアプリケーションの基本構造</li>
        <li>✅ ルーティング（@app.route）の使い方</li>
        <li>✅ HTTPリクエスト・レスポンスの仕組み</li>
    </ul>
    """

@app.route('/hello')
def hello():
    """
    Hello Worldページ
    プログラミング学習の伝統的な最初のプログラム
    """
    return """
    <h1>👋 Hello, World!</h1>
    <p>おめでとうございます！初めてのFlaskページが表示されています。</p>
    <p>このページのURL: <code>/hello</code></p>
    <p><a href="/">ホームページに戻る</a></p>
    """

@app.route('/about')
def about():
    """
    アプリケーションの説明ページ
    複数のルートがどのように動作するかを示す
    """
    return """
    <h1>📝 ToDoアプリについて</h1>
    <h2>これから作成するアプリケーション</h2>
    <p>このFlask学習を通じて、以下の機能を持つToDoアプリを段階的に作成します：</p>
    <ol>
        <li><strong>Step 1 (現在)</strong>: Flask基礎・Hello World</li>
        <li><strong>Step 2</strong>: HTMLテンプレート・CSS</li>  
        <li><strong>Step 3</strong>: JavaScript・DOM操作</li>
        <li><strong>Step 4</strong>: フォーム送信・POST処理</li>
        <li><strong>Step 5</strong>: データベース・完成版</li>
    </ol>
    <h3>🎯 最終的な機能</h3>
    <ul>
        <li>ToDoアイテムの追加・削除・編集</li>
        <li>美しいWebデザイン</li>
        <li>JavaScriptによる動的操作</li>
        <li>データの永続化（データベース保存）</li>
    </ul>
    <p><a href="/">ホームページに戻る</a></p>
    """

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    開発・運用時の監視に使用される
    """
    return {
        'status': 'OK',
        'message': 'Step1 Flaskアプリケーションが正常に動作しています',
        'step': 1,
        'description': 'Flask基礎セットアップ / Hello World'
    }

# このファイルが直接実行された場合のみWebサーバーを起動
if __name__ == '__main__':
    print("🚀 Flask開発サーバーを起動します...")
    print("📍 アクセスURL: http://localhost:5000")
    print("⚡ 開発モード: デバッグ情報表示、ファイル変更時の自動再起動")
    print("🛑 停止方法: Ctrl+C")
    
    # 開発サーバーの起動
    # debug=True: 開発モード（エラー詳細表示、ホットリロード）
    # host='127.0.0.1': ローカルホストのみからアクセス可能
    # port=5000: ポート番号5000で起動
    app.run(debug=True, host='127.0.0.1', port=5000)