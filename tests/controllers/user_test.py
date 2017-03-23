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

    def test_login_fail(self):
        result = self.app.post('/login', data={
            'mail': 'not_exist_user@test.com',
            'password': 'test'
        })
        self.assertEqual(result.status_code, 200)

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
            'mail': datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + 'test_register@test.com',
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])

    # ユーザー登録が失敗することを確認
    def test_register_fail(self):
        result = self.app.post('/register', data={
            'user_name': '1234567890123456789012345678901234567890'
                         '1234567890123456789012345678901234567890'
                         '1234567890123456789012345678901234567890'
                         '1234567890',
            'mail': None,
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.assertEqual(result.status_code, 200)

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
            'user_name': user.user_name,
            'mail': mail,
            'self_introduction': 'test',
            'job': ['Designer', 'Coder']
        })
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])

    # 既にあるメールアドレスには変更できない。
    def test_post_profile_fail(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        user = self.repository.find_by_mail(mail)

        result = self.app.post('/profile/' + str(user.id), data={
            'user_name': user.user_name,
            'mail': 'test@test1.com',
            'self_introduction': 'test',
            'job': ['Designer', 'Coder']
        })
        user = self.repository.find_by_id(user.id)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(user.mail, mail)

    # ユーザー検索画面に遷移できる
    def test_get_index(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        result = self.app.get('/user')
        self.assertEqual(result.status_code, 200)

    # ユーザー検索できる
    def test_post_index(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        result = self.app.get('/user?user_name=テスト')
        self.assertEqual(result.status_code, 200)

    # ユーザー詳細画面に遷移できる
    def test_get_detail(self):
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        user = self.repository.find_by_mail('test@test2.com')
        result = self.app.get('/user/' + str(user.id))
        self.assertEqual(result.status_code, 200)

    # 存在しないユーザー詳細画面には遷移できない
    def test_detail_not_exist_user(self):
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        result = self.app.get('/user/0')
        self.assertEqual(result.status_code, 404)

    # ユーザー詳細で２ページ目の発言が表示できる
    def test_detail_page(self):
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        user = self.repository.find_by_mail(mail)

        # 10件以上のツイートを作成
        self.app.post('/', data={'content': 'test1'})
        self.app.post('/', data={'content': 'test2'})
        self.app.post('/', data={'content': 'test3'})
        self.app.post('/', data={'content': 'test4'})
        self.app.post('/', data={'content': 'test5'})
        self.app.post('/', data={'content': 'test6'})
        self.app.post('/', data={'content': 'test7'})
        self.app.post('/', data={'content': 'test8'})
        self.app.post('/', data={'content': 'test9'})
        self.app.post('/', data={'content': 'test10'})
        self.app.post('/', data={'content': 'test11'})

        result = self.app.get('/user/' + str(user.id) + '/page/2')
        self.assertEqual(result.status_code, 200)
