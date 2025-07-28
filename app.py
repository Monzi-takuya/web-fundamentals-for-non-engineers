"""
Flask求人検索アプリケーション
PHPのSymfonyでいうところのControllerの役割を担います
"""
from flask import Flask, render_template, request
from models import db, Job
import os

# Flaskアプリケーションの初期化
app = Flask(__name__)

# データベース設定（SQLite使用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# データベースの初期化
db.init_app(app)

@app.route('/')
def index():
    """
    トップページ（検索フォーム）
    PHPでいうところの IndexController::index() に相当
    """
    return render_template('index.html')

@app.route('/search')
def search():
    """
    検索結果ページ
    PHPでいうところの SearchController::search() に相当
    """
    # GETパラメータを取得
    keyword = request.args.get('keyword', '').strip()
    location = request.args.get('location', '').strip()
    
    # 検索クエリの構築
    query = Job.query
    
    # キーワード検索（タイトル、会社名、キーワードフィールドで検索）
    if keyword:
        search_term = f'%{keyword}%'
        query = query.filter(
            db.or_(
                Job.title.like(search_term),
                Job.company.like(search_term),
                Job.keywords.like(search_term),
                Job.description.like(search_term)
            )
        )
    
    # 勤務地検索
    if location:
        location_term = f'%{location}%'
        query = query.filter(Job.location.like(location_term))
    
    # 検索実行（新しい順で並び替え）
    jobs = query.order_by(Job.created_at.desc()).all()
    
    # 検索条件をテンプレートに渡す
    search_params = {
        'keyword': keyword,
        'location': location,
        'count': len(jobs)
    }
    
    return render_template('results.html', jobs=jobs, search=search_params)

@app.route('/health')
def health_check():
    """
    アプリケーションの動作確認用エンドポイント
    """
    return {'status': 'OK', 'message': 'Flask求人検索アプリケーションが正常に動作しています'}

if __name__ == '__main__':
    # データベーステーブルの作成（存在しない場合）
    with app.app_context():
        db.create_all()
    
    # アプリケーション実行
    # debug=True で開発時のホットリロードが有効
    app.run(debug=True, host='127.0.0.1', port=5000) 