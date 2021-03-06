from flask_wtf import file
from wtforms import ValidationError
from wtforms import validators
from wtforms.compat import string_types
from wtforms.validators import StopValidation


class Length(validators.Length):
    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            message = self.message
            if message is None:
                if self.max == -1:
                    message = field.ngettext('%(min)d 文字以上の入力が必要です',
                                             '%(min)d 文字以上の入力が必要です', self.min)
                elif self.min == -1:
                    message = field.ngettext('%(max)d 文字以内で入力してください',
                                             '%(max)d 文字以内で入力してください', self.max)
                else:
                    message = field.gettext('%(min)d 文字以上、%(max)d 文字以内で入力してください')

            raise ValidationError(message % dict(min=self.min, max=self.max, length=l))


class DataRequired(validators.DataRequired):
    def __call__(self, form, field):
        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if self.message is None:
                message = field.gettext('{}は必須です'.format(field.label.text))
            else:
                message = self.message

            field.errors[:] = []
            raise StopValidation(message)
