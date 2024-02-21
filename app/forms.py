from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    username=StringField("Username/Email:", render_kw={"placeholder":"Enter your username"} ,validators=[DataRequired()])
    password=PasswordField("Password:", render_kw={"placeholder":"Enter your pasword"}, validators=[DataRequired()])
    submit=SubmitField("Login")
