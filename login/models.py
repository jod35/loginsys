from login import db

class User(db.Model):
    id=db.Column(db.Integer(),nullable=False,primary_key=True)
    username=db.Column(db.String(),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return 'user {}'.format(self.username)
