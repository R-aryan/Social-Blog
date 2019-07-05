from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from companyblog.models import User


### creating login FlaskForm
class LoginForm(FlaskForm):
    email= StringField('Enter your email ID: ', validators=[DataRequired(),Email()])
    password= PasswordField('Enter Your password :', validators=[DataRequired()])
    submit= SubmitField('Log In')


class RegistrationForm(FlaskForm):

    name= StringField('Enter Your name:',validators=[DataRequired()])
    username= StringField('Enter Your username:',validators=[DataRequired()])
    email= StringField('Enter Your email :',validators=[DataRequired(),Email()])
    password= PasswordField('Enter password :', validators=[DataRequired(),EqualTo('pass_confirm',message='Password Must Match')])
    pass_confirm=PasswordField('Re-enter password',validators=[DataRequired()])
    submit=SubmitField('Register')


    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValueError('Your email is already registered....!!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValueError('Your Username is already registered...!!!!')


class UpdateUserForm(FlaskForm):
    username= StringField('Enter Your username:',validators=[DataRequired()])
    email= StringField('Enter Youe email :',validators=[DataRequired(),Email()])
    picture=FileField('Update Profile picture :',validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValueError('Your email is already registered....!!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValueError('Your Username is already registered...!!!!')
