from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField

from application.controllers.form.validators import Length, DataRequired


class PostForm(FlaskForm):
    content = TextAreaField('今どうしてる？', [DataRequired('このフィールドは必須です'), Length(max=128)])

