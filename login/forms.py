from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class SignUpForm(FlaskForm):
    username=StringField("Your Username",validators=[DataRequired(),Length(min=4,max=40)])
    email=StringField("Your Email",validators=[DataRequired(),Length(max=80)])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo('confirm')])
    confirm=StringField("Confirm the Password",validators=[DataRequired()])
    submit=SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email=StringField("Your Email",validators=[DataRequired(),Length(max=80)])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Log In")

    

