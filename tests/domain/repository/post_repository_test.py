from datetime import datetime

from application import db
from application.domain.model.post import Post
from application.domain.repository.post_repository import PostRepository
from tests import BaseTestCase


class PostRepositoryTests(BaseTestCase):

    def setUp(self):
        super(PostRepositoryTests, self).setUp()
        self.post_repository = PostRepository()

    def tearDown(self):
        super(PostRepositoryTests, self).tearDown()

    def test_find_all(self):
        before = self.post_repository.find_all()
        # 一件登録する
        post = Post(
            user_id=1,
            content='test',
            created_at=datetime.today(),
            created_user='test',
            updated_at=datetime.today(),
            updated_user='test')
        db.session.add(post)
        db.session.commit()

        after = self.post_repository.find_all()
        self.assertGreater(len(after), len(before))

    def test_create(self):
        post = self.post_repository.create()
        self.assertIsNone(post.id)
