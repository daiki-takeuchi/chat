from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from application import db
from application.domain.model.base_model import BaseModel


class Post(BaseModel, db.Model):
    __tablename__ = 'posts'
    PER_PAGE = 10

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(String(128))

    user = relationship("User", lazy='joined')

    def __init__(self,
                 user_id=None,
                 content=None,
                 created_at=None,
                 created_user=None,
                 updated_at=None,
                 updated_user=None):
        super(Post, self).__init__(created_at, created_user, updated_at, updated_user)
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return "<Post:" + \
                "'id='{}".format(self.id) + \
                "', user='{}".format(self.user) + \
                "', content='{}".format(self.content) + \
                "', created_at='{}".format(self.created_at) + \
                "', created_user='{}".format(self.created_user) + \
                "', updated_at='{}".format(self.updated_at) + \
                "', updated_user='{}".format(self.updated_user) + \
                "'>"
