import datetime

from application.domain.repository.post_repository import PostRepository
from application.domain.repository.user_repository import UserRepository
from tests import BaseTestCase


class FollowingTests(BaseTestCase):

    def setUp(self):
        super(FollowingTests, self).setUp()
        self.post_repository = PostRepository()
        self.user_repository = UserRepository()

    def tearDown(self):
        super(FollowingTests, self).tearDown()

    # Followする。
    def test_following(self):
        mail = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '@test.com'
        # ユーザー登録する
        self.app.post('/register', data={
            'user_name': '単体テスト',
            'mail': mail,
            'password': 'test',
            'password_confirmation': 'test'
        })
        # ユーザー登録するとログインするので、ログアウト
        self.app.get('/logout')

        user = self.user_repository.find_by_mail(mail)
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        # フォローする
        result = self.app.get('/following/' + str(user.id))
        self.assertEqual(result.status_code, 302)

    # フォロー済みのユーザーはFollowできない。
    def test_following_fail(self):
        mail = 'test@test.com'
        user = self.user_repository.find_by_mail(mail)
        before = len(user.following)
        # ログインする
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        # フォローする
        result = self.app.get('/following/' + str(user.following[0].following_id))
        self.assertEqual(result.status_code, 302)

        user = self.user_repository.find_by_mail(mail)
        after = len(user.following)
        # 前後で件数が変わっていないことを確認
        self.assertEqual(before, after)

    # follow解除する。
    def test_unfollowing(self):
        mail = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '@test.com'
        # ユーザー登録する
        self.app.post('/register', data={
            'user_name': '単体テスト',
            'mail': mail,
            'password': 'test',
            'password_confirmation': 'test'
        })
        # ユーザー登録するとログインするので、ログアウト
        self.app.get('/logout')

        user = self.user_repository.find_by_mail(mail)
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        # フォローする
        self.app.get('/following/' + str(user.id))

        # フォロー解除する
        result = self.app.get('/unfollow/' + str(user.id))
        self.assertEqual(result.status_code, 302)

    # フォローしてないユーザーはフォロー解除できない。
    def test_unfollowing_fail(self):
        mail = 'test@test.com'
        user = self.user_repository.find_by_mail(mail)
        before = len(user.following)
        # ログインする
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })
        # フォロー解除する
        result = self.app.get('/unfollow/10')
        self.assertEqual(result.status_code, 302)

        user = self.user_repository.find_by_mail(mail)
        after = len(user.following)
        # 前後で件数が変わっていないことを確認
        self.assertEqual(before, after)
