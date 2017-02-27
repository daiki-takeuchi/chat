import datetime
import unittest

from application import app, db


class BaseTestCase(unittest.TestCase):

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
        db.drop_all()
        db.create_all()
        self.create_user()

    def tearDown(self):
        db.session.remove()

    def create_user(self):
        self.app.post('/register', data={
            'user_name': '単体テスト1',
            'mail': 'test@test.com',
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.app.post('/register', data={
            'user_name': '単体テスト2',
            'mail': 'test@test2.com',
            'password': 'test',
            'password_confirmation': 'test'
        })
        self.app.post('/register', data={
            'user_name': '単体テスト3',
            'mail': datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '@test.com',
            'password': 'test',
            'password_confirmation': 'test'
        })
