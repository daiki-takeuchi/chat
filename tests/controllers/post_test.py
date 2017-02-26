from nose.tools import ok_

from tests import BaseTestCase


class PostTests(BaseTestCase):

    def setUp(self):
        super(PostTests, self).setUp()

    def tearDown(self):
        super(PostTests, self).tearDown()

    # ログインしていない場合は、ログイン画面に移動する。
    def test_root_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 302)
        ok_('/login' in result.headers['Location'])
