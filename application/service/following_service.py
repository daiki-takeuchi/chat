from application.domain.repository.following_repository import FollowingRepository


class FollowingService(object):
    repository = FollowingRepository()

    def find(self, user_id, following_id):
        return self.repository.find(user_id, following_id)

    def save(self, following):
        return self.repository.save(following)

    def destroy(self, following):
        return self.repository.destroy(following)
