from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, RadioField, \
        BooleanField
from wtforms.validators import DataRequired, AnyOf, Length, Optional, EqualTo

class LoginForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField('提交')

class RegisterForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired(), \
            Length(3,25, message='用户名长度在3~25之间')])
    password = PasswordField("输入密码", validators=[DataRequired(), \
            Length(3,20, message='密码长度在3~20之间'), \
            EqualTo('confirmation', message='两次输入密码不一致！')])
    confirmation = PasswordField('请重复密码')
    submit = SubmitField('提交')
