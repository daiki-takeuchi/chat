from application.domain.model.post import Post
from application.domain.repository.base_repository import BaseRepository


class PostRepository(BaseRepository):

    model = Post

    def find_all(self, page=None):
        if page:
            return self.model.query.order_by(self.model.created_at.desc()).paginate(page, self.model.PER_PAGE)
        else:
            return self.model.query.order_by(self.model.created_at.desc()).all()

    def find_by_user_id(self, page, user_id):
        query = self.model.query
        if user_id:
            query = query.filter(self.model.user_id == user_id)
        pagination = query.order_by(self.model.created_at.desc()).paginate(page, self.model.PER_PAGE)
        return pagination

    def create(self):
        return Post()
