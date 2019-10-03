from login import app,db
from flask import render_template,request,redirect
from login.forms import SignUpForm,LoginForm
from login.models import User
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET', 'POST'])
def create_user():
    form=SignUpForm()
    if request.method == 'POST':
        new_user=User(
            username=request.form.get('username'),
            email=request.form.get('email'),
            password=bcrypt.generate_password_hash(request.form.get('password')),
        )
        db.session.add(new_user)
        db.session.commit()


        
        return redirect('/')
    return render_template('signup.html',form=form)

@app.route('/login')
def Login():
    form = LoginForm()
    return render_template('login.html',form=form)