from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import ValidationError

from application.controllers.form.validators import DataRequired
from application.domain.repository.user_repository import UserRepository

repository = UserRepository()


class LoginForm(FlaskForm):
    mail = StringField('メールアドレス', [DataRequired()])
    password = PasswordField('パスワード', [DataRequired()])

    def validate_password(self, field):
        user = repository.find_by_mail(self.mail.data)
        if user is None or not user.can_login(field.data):
            raise ValidationError('メールアドレスまたはパスワードが違います。')
