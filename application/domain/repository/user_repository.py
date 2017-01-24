from datetime import datetime

from flask import current_app
from flask import session

from application import db, bcrypt
from application.domain.model.user import User
from application.domain.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):

    model = User

    def find(self, page, user_name):
        query = self.model.query
        if user_name:
            query = query.filter(self.model.user_name.like('%' + user_name + '%'))
        pagination = query.paginate(page, self.model.PER_PAGE)
        return pagination

    def find_by_mail(self, mail):
        return User.query.filter(User.mail == mail).first()

    def save(self, user):
        if user.id is None:
            user.created_at = datetime.today()
            user.created_user = session['user']['user_name']
            user.password = bcrypt.generate_password_hash(user.mail)
        user.updated_at = datetime.today()
        user.updated_user = session['user']['user_name']

        db.session.add(user)
        db.session.commit()
        current_app.logger.debug('save:' + str(user))

    def create(self):
        return User()
