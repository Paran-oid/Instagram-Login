from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app import db 
import sqlalchemy as sa 
from app.models import User 


class Form(FlaskForm):
    username=StringField("Username/Email:", render_kw={"placeholder":"Enter your username"} ,validators=[DataRequired()])
    password=PasswordField("Password:", render_kw={"placeholder":"Enter your pasword"}, validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Login")

class Registration(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    password2=PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self, username):
        user=db.session.scalar(sa.select(User).where(User.username == username.data))
        if user:
            raise ValidationError("Enter a different name")

    def validate_email(self, email):
        user=db.session.scalar(sa.select(User).where(User.email == email.data))
        if user:
            raise ValidationError("Enter a different email")