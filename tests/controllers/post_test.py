from nose.tools import ok_

from application.domain.repository.post_repository import PostRepository
from application.domain.repository.user_repository import UserRepository
from tests import BaseTestCase


class PostTests(BaseTestCase):

    def setUp(self):
        super(PostTests, self).setUp()
        self.post_repository = PostRepository()
        self.user_repository = UserRepository()

    def tearDown(self):
        super(PostTests, self).tearDown()

    # ホーム画面に遷移する。
    def test_get_root(self):
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    # ログインしていない場合は、ログイン画面に移動する。
    def test_root_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 302)
        ok_('/login' in result.headers['Location'])

    # ホーム画面で２ページ目の発言が表示できる
    def test_root_page(self):
        # ログインする
        self.app.post('/login', data={
            'mail': 'test@test.com',
            'password': 'test'
        })

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

        result = self.app.get('/page/2')
        self.assertEqual(result.status_code, 200)

    # 発言が削除できる
    def test_delete_tweet(self):
        # ログインする
        mail = 'test@test.com'
        self.app.post('/login', data={
            'mail': mail,
            'password': 'test'
        })

        # 1件ツイートを作成
        self.app.post('/', data={'content': 'test1'})
        # 自分のツイートを検索
        user = self.user_repository.find_by_mail(mail)
        posts = self.post_repository.find_by_user_id(page=1, user_id=user.id)
        # 最新1件目
        post = posts.items[0]

        result = self.app.get('/delete/' + str(post.id))
        self.assertEqual(result.status_code, 302)
        ok_('/' in result.headers['Location'])
