from wtforms.validators import Required, Length, Email, Regexp
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import Required
from ..auth.my_geetest.field import RecaptchaField



class PostForm(Form):
    body = TextAreaField("What is on your mind?",validators=[Required()])
    submit = SubmitField("Submit")

class PostFormWithAuthCode(Form):
    body = TextAreaField("What is on your mind?",validators=[Required()])
    re = RecaptchaField('9536bfe265bed0797caaf220966f0ac1', '81bdb06b771546145d78ba37d29a41fb')
    submit = SubmitField("Submit")