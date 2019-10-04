from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///login.db'
app.config['SECRET_KEY']='ASAJDIASJDIAJDIJ23IO4U893U7483UEO2K3E23$@$@#$23412'

db=SQLAlchemy(app)
login_manager =LoginManager(app)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.Integer(),unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


    

@app.route('/')
@login_required
def index():
    return "You are %s"%current_user.username

@app.route('/login')
def Login():
    user= User.query.filter_by(username="Jonathan").first()
    login_user(user)
    return "You are logged in"

@app.route('/logout')
def LogOut():
    logout_user()
    return "You are currently logged out"

if __name__ == '__main__':
    app.run(debug=True)