from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(LoginForm):
    user_type = RadioField("用户类型", choices=[(1, '普通用户'), (2, '管理员用户')])
