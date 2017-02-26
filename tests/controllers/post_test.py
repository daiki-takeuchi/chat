import unittest

from nose.tools import ok_

from application import app


class PostTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        app.config.from_object('config.testing')
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    # ログインしていない場合は、ログイン画面に移動する。
    def test_root_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 302)
        ok_('/login' in result.headers['Location'])
