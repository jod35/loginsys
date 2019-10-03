from login import app
from flask import render_template
from login.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def create_user():
    form=SignUpForm()
    return render_template('signup.html',form=form)