from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms import validators, StringField, IntegerField

from application.controllers.form.validators import Length, DataRequired
from application.domain.repository.user_repository import UserRepository

repository = UserRepository()


class UserForm(FlaskForm):
    id = IntegerField('Id')
    user_name = StringField('ユーザー名', [DataRequired(), Length(max=128)])
    mail = StringField('メールアドレス', [DataRequired(),
                                   Length(max=256),
                                   validators.Email('正しいメールアドレスにしてください。')])

    def validate_mail(self, field):
        user = repository.find_by_mail(mail=field.data)
        if user and user.id != self.id.data:
            raise ValidationError('このメールアドレスは既に登録されています。')
