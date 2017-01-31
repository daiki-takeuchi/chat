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

    def find_follower(self, page, user_id):
        query = self.model.query
        if user_id:
            query = query.filter(self.model.following_id == user_id)
        pagination = query.order_by(self.model.created_at.desc()).paginate(page, self.model.PER_PAGE)
        return pagination

    def find_following(self, page, user_id):
        query = self.model.query
        if user_id:
            query = query.filter(self.model.user_id == user_id)
        pagination = query.order_by(self.model.created_at.desc()).paginate(page, self.model.PER_PAGE)
        return pagination

    def create(self):
        return Following()
