from datetime import datetime

from application import bcrypt, db
from application.domain.model.following import Following
from application.domain.model.user import User


def init_data():
    # データの作成
    create_user()
    create_followers()


def create_user():
    # ログイン用のユーザー
    user = User(
                 user_name='単体テスト',
                 mail='test@test.com',
                 password=bcrypt.generate_password_hash('test'),
                 created_at=datetime.today(),
                 created_user='test',
                 updated_at=datetime.today(),
                 updated_user='test')
    db.session.add(user)

    for num in range(12):
        user = User(
                 user_name='単体テスト' + str(num),
                 mail='test@test' + str(num) + '.com',
                 password=bcrypt.generate_password_hash('test'),
                 created_at=datetime.today(),
                 created_user='test',
                 updated_at=datetime.today(),
                 updated_user='test')
        db.session.add(user)
    db.session.commit()


def create_followers():
    for num in range(2, 5):
        following = Following(
            user_id=1,
            following_id=num,
            created_at=datetime.today(),
            created_user='test',
            updated_at=datetime.today(),
            updated_user='test')
        db.session.add(following)
    db.session.commit()
