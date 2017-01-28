from flask_wtf import FlaskForm
from wtforms import ValidationError, PasswordField
from wtforms import validators, StringField, IntegerField
from wtforms.validators import EqualTo

from application.controllers.form.validators import Length, DataRequired
from application.domain.repository.user_repository import UserRepository

repository = UserRepository()


class UserForm(FlaskForm):
    id = IntegerField('Id')
    user_name = StringField('ユーザー名', [DataRequired(), Length(max=128)])
    mail = StringField('メールアドレス', [DataRequired(),
                                   Length(max=256),
                                   validators.Email('正しいメールアドレスにしてください。')])
    password = PasswordField('新しいパスワード',[DataRequired()])
    password_confirmation = PasswordField('新しいパスワード（確認）',
                                              [DataRequired(),
                                               EqualTo('password',
                                                       message='パスワードとパスワード（確認）が一致していません')])

    def validate_mail(self, field):
        user = repository.find_by_mail(mail=field.data)
        if user and user.id != self.id.data:
            raise ValidationError('このメールアドレスは既に登録されています。')
