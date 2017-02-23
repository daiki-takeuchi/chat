from flask_wtf import FlaskForm
from wtforms import ValidationError, TextAreaField
from wtforms import validators, StringField, IntegerField

from application.controllers.form.fields import MultiCheckboxField
from application.controllers.form.validators import Length, DataRequired
from application.domain.repository.user_repository import UserRepository

repository = UserRepository()


class UserForm(FlaskForm):
    id = IntegerField('Id')
    user_name = StringField('ユーザー名', [DataRequired(), Length(max=128)])
    mail = StringField('メールアドレス', [DataRequired(),
                                   Length(max=256),
                                   validators.Email('正しいメールアドレスにしてください。')])
    string_of_files = ['one\r\ntwo\r\nthree\r\n']
    job = MultiCheckboxField('job', choices=[('Designer', 'pencil'),
                                             ('Coder', 'terminal'),
                                             ('Developer', 'laptop')])
    self_introduction = TextAreaField('自己紹介文', [Length(max=2048)])

    def validate_mail(self, field):
        user = repository.find_by_mail(mail=field.data)
        if user and user.id != self.id.data:
            raise ValidationError('このメールアドレスは既に登録されています。')
