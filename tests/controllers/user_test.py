import datetime

from nose.tools import ok_

from application.domain.repository.user_repository import UserRepository
from tests import BaseTestCase


class UserTests(BaseTestCase):

    def setUp(self):
        super(UserTests, self).setUp()
        self.repository = UserRepository()

    def tearDown(self):
        super(UserTests, self).tearDown()

    # ログイン画面に遷移する。
    def test_login_status_code(self):
        result = self.app.get('/login')

        self.assertEqual(result.status_code, 200)

    def test_login(self):
        result = self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])

    def test_logout(self):
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)
        ok_('/login' in result.headers['Location'])

    # sign up画面に遷移する。
    def test_register_status_code(self):
        result = self.app.get('/register')
        self.assertEqual(result.status_code, 200)

    # ユーザーを登録する
    def test_register(self):
        result = self.app.post('/register', data={
            'user_name': '単体テスト',
            'mail': datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '@test.com',
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])

    # 同じメールの場合登録できない
    def test_register_duplicate_mail(self):
        mail = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '@test.com'
        self.app.post('/register', data={
            'user_name': '単体テスト',
            'mail': mail,
            'password': 'test',
            'password_confirmation': 'test'
        })
        # ログアウト
        self.app.get('/logout')

        result = self.app.post('/register', data={
            'user_name': '単体テスト',
            'mail': mail,
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.assertEqual(result.status_code, 200)

    # プロフィール画面に遷移する
    def test_get_profile(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        user = self.repository.find_by_mail(mail)

        result = self.app.get('/profile/' + str(user.id))
        self.assertEqual(result.status_code, 200)

    # 他の人のプロフィール画面に遷移できない
    def test_another_person_profile(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        user = self.repository.find_by_mail(mail)

        result = self.app.get('/profile/' + str(user.id + 1))
        self.assertEqual(result.status_code, 404)

    # プロフィールを変更できる
    def test_post_profile(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        user = self.repository.find_by_mail(mail)

        result = self.app.post('/profile/' + str(user.id), data={
            'user_name': user.user_name + '_test',
            'mail': mail,
            'self_introduction': 'test',
            'job': ['Designer', 'Coder']
        })
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])
