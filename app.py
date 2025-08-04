# Flask学習用のベースアプリケーション
# チュートリアル用に段階的に機能を追加していきます

from flask import Flask

# Flaskアプリケーションの初期化
app = Flask(__name__)

@app.route('/')
def index():
    """
    ホームページ
    Hello Worldから始めるFlask学習
    """
    return "<h1>Flask学習チュートリアル</h1><p>準備完了！チュートリアルを開始してください。</p>"

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    """
    return {'status': 'OK', 'message': 'Flask学習アプリケーションが正常に動作しています'}

if __name__ == '__main__':
    # アプリケーション実行
    app.run(debug=True, host='127.0.0.1', port=5000)