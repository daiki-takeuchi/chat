from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from application import db
from application.domain.model.base_model import BaseModel
from application.domain.model.user import User


class Following(BaseModel, db.Model):
    __tablename__ = 'following'
    PER_PAGE = 10

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    following_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    follower = relationship(User, lazy="joined", primaryjoin=user_id == User.id)
    following = relationship(User, lazy="joined", primaryjoin=following_id == User.id)

    def __init__(self,
                 user_id=None,
                 following_id=None,
                 created_at=None,
                 created_user=None,
                 updated_at=None,
                 updated_user=None):
        super(Following, self).__init__(created_at, created_user, updated_at, updated_user)
        self.user_id = user_id
        self.following_id = following_id

    def __repr__(self):
        return "<Following:" + \
                "'id='{}".format(self.id) + \
                "', follower='{}".format(self.follower) + \
                "', following='{}".format(self.following) + \
                "', created_at='{}".format(self.created_at) + \
                "', created_user='{}".format(self.created_user) + \
                "', updated_at='{}".format(self.updated_at) + \
                "', updated_user='{}".format(self.updated_user) + \
                "'>"
