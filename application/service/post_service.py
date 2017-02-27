from application.domain.repository.post_repository import PostRepository


class PostService(object):
    repository = PostRepository()

    def find_by_id(self, post_id):
        return self.repository.find_by_id(post_id)

    def find_by_user_id(self, page, user_id):
        return self.repository.find_by_user_id(page, user_id)

    def find_timelines(self, page, user_id):
        return self.repository.find_all(page)

    def save(self, user):
        return self.repository.save(user)

    def destroy(self, user):
        return self.repository.destroy(user)

    def create(self):
        return self.repository.create()