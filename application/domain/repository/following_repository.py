from application.domain.model.following import Following
from application.domain.repository.base_repository import BaseRepository


class FollowingRepository(BaseRepository):

    model = Following

    def find(self, user_id, following_id):
        query = self.model.query
        if user_id:
            query = query.filter(self.model.user_id == user_id)
        if following_id:
            query = query.filter(self.model.following_id == following_id)
        ret = query.first()
        if ret is None:
            ret = self.create()
        return ret

    def create(self):
        return Following()
