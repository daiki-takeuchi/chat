from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from application import db, bcrypt
from application.domain.model.base_model import BaseModel
from application.domain.model.following import Following
from application.domain.model.post import Post


class User(BaseModel, db.Model):
    __tablename__ = 'users'
    PER_PAGE = 10

    user_name = Column(String(128))
    mail = Column(String(128))
    password = Column(String(256))

    posts = relationship(Post, cascade='all, delete-orphan')
    following = relationship(Following, foreign_keys=[Following.user_id], cascade='all, delete-orphan')
    follower = relationship(Following, foreign_keys=[Following.following_id], cascade='all, delete-orphan')

    def __init__(self,
                 user_name=None,
                 mail=None,
                 password=None,
                 created_at=None,
                 created_user=None,
                 updated_at=None,
                 updated_user=None):
        super(User, self).__init__(created_at, created_user, updated_at, updated_user)
        self.user_name = user_name
        self.mail = mail
        self.password = password

    def can_login(self, password):
        if self.id:
            return bcrypt.check_password_hash(self.password, password)
        else:
            return False

    def is_followed(self, user_id):
        for follower in self.follower:
            if follower.user_id == user_id:
                return True
        return False

    def __repr__(self):
        return "<User:" + \
                "'id='{}".format(self.id) + \
                "', user_name='{}".format(self.user_name) + \
                "', mail='{}".format(self.mail) + \
                "', created_at='{}".format(self.created_at) + \
                "', created_user='{}".format(self.created_user) + \
                "', updated_at='{}".format(self.updated_at) + \
                "', updated_user='{}".format(self.updated_user) + \
                "'>"

    def serialize(self):
        return {
           'id': self.id,
           'user_name': self.user_name,
           'mail': self.mail,
           'created_user': self.created_user,
           'updated_at': self.updated_at,
           'updated_user': self.updated_user
        }
