from login import db,app
from flask_login import LoginManager,UserMixin

login_manager =LoginManager(app)

login_manager.login_view ='Login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),nullable=False,primary_key=True)
    username=db.Column(db.String(),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return 'user {}'.format(self.username)
