from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Email,Length,Required
from .my_geetest.field import RecaptchaField

class LoginForm(Form):
    email = StringField("Email",validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class LoginFormWithAuth(Form):
    email = StringField("Email",validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    re = RecaptchaField('9536bfe265bed0797caaf220966f0ac1','81bdb06b771546145d78ba37d29a41fb')
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')