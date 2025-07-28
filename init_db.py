"""
データベース初期化スクリプト
テーブル作成とダミーデータの投入を行います
PHPでいうところのMigrationとSeederの役割を兼ねます
"""
from app import app
from models import db, Job

def init_database():
    """データベースの初期化"""
    with app.app_context():
        # 既存のテーブルを削除して再作成
        db.drop_all()
        db.create_all()
        
        # ダミーデータの作成
        sample_jobs = [
            Job(
                title='Webエンジニア（フルスタック）',
                company='株式会社テックイノベーション',
                location='東京都渋谷区',
                salary='年収400万円〜600万円',
                description='PHP/Symfony、React/TypeScriptを使用したWebアプリケーション開発。企画から運用まで幅広く携わっていただきます。',
                keywords='PHP Symfony React TypeScript フルスタック'
            ),
            Job(
                title='Pythonエンジニア（AI・機械学習）',
                company='AI Solutions合同会社',
                location='東京都新宿区',
                salary='年収500万円〜800万円',
                description='機械学習モデルの開発・運用、データパイプラインの構築を担当。Python、TensorFlow、PyTorchの経験者歓迎。',
                keywords='Python AI 機械学習 TensorFlow PyTorch データサイエンス'
            ),
            Job(
                title='フロントエンドエンジニア',
                company='株式会社デジタルクリエイト',
                location='大阪府大阪市',
                salary='年収350万円〜550万円',
                description='Vue.js、Nuxt.jsを用いたSPAの開発。UIライブラリの作成や画面設計から実装まで担当。',
                keywords='Vue.js Nuxt.js JavaScript SPA フロントエンド'
            ),
            Job(
                title='バックエンドエンジニア（Node.js）',
                company='クラウドテック株式会社',
                location='リモート勤務可',
                salary='年収450万円〜700万円',
                description='Node.js/Express、AWS環境でのAPI開発。マイクロサービス architecture の設計・実装経験者優遇。',
                keywords='Node.js Express AWS API マイクロサービス クラウド'
            ),
            Job(
                title='DevOpsエンジニア',
                company='インフラソリューション株式会社',
                location='東京都港区',
                salary='年収550万円〜900万円',
                description='Kubernetes、Docker、Terraformを用いたインフラ構築・運用自動化。CI/CDパイプラインの構築。',
                keywords='DevOps Kubernetes Docker Terraform CI/CD インフラ'
            ),
            Job(
                title='モバイルアプリエンジニア（Flutter）',
                company='モバイルファースト株式会社',
                location='福岡県福岡市',
                salary='年収400万円〜650万円',
                description='Flutter/Dartを使用したクロスプラットフォームアプリ開発。iOS/Android両対応。',
                keywords='Flutter Dart モバイルアプリ iOS Android クロスプラットフォーム'
            ),
            Job(
                title='データエンジニア',
                company='ビッグデータアナリティクス株式会社',
                location='東京都品川区',
                salary='年収500万円〜750万円',
                description='Apache Spark、Kafka を用いた大規模データ処理基盤の構築。データウェアハウスの設計・運用。',
                keywords='データエンジニア Apache Spark Kafka データウェアハウス ETL'
            ),
            Job(
                title='QAエンジニア（自動化テスト）',
                company='品質保証ソリューションズ合同会社',
                location='東京都中央区',
                salary='年収380万円〜580万円',
                description='Selenium、Cypress を用いた自動テストの設計・実装。テスト戦略の立案からテスト実行まで。',
                keywords='QA テスト自動化 Selenium Cypress 品質保証'
            )
        ]
        
        # データベースに追加
        for job in sample_jobs:
            db.session.add(job)
        
        # コミット
        db.session.commit()
        
        print(f"✅ データベースの初期化が完了しました。{len(sample_jobs)}件の求人データを投入しました。")

if __name__ == '__main__':
    init_database() 