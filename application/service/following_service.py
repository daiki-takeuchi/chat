from application.domain.repository.following_repository import FollowingRepository


class FollowingService(object):
    repository = FollowingRepository()

    def find(self, user_id, following_id):
        return self.repository.find(user_id, following_id)

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_follower(self, page, user_id):
        return self.repository.find_follower(page, user_id)

    def find_following(self, page, user_id):
        return self.repository.find_following(page, user_id)

    def save(self, following):
        return self.repository.save(following)

    def destroy(self, following):
        return self.repository.destroy(following)
