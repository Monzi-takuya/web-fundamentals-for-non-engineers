"""
データベースモデル定義
求人票のデータ構造を定義します
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    """
    求人票テーブル
    PHPでいうところのEloquentモデルやDoctrineエンティティに相当
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)        # 求人タイトル
    company = db.Column(db.String(100), nullable=False)      # 会社名
    location = db.Column(db.String(100), nullable=False)     # 勤務地
    salary = db.Column(db.String(100))                       # 給与
    description = db.Column(db.Text)                         # 求人詳細
    keywords = db.Column(db.String(200))                     # 検索用キーワード
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'
    
    def to_dict(self):
        """
        辞書形式に変換（JSON変換やテンプレート渡しで使用）
        PHPのtoArray()メソッドに相当
        """
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'salary': self.salary,
            'description': self.description,
            'keywords': self.keywords,
            'created_at': self.created_at
        } 