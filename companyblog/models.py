## inside models.py file
from companyblog import db,login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):

    __tablename__= 'users'

    id= db.Column(db.Integer,primary_key=True)
    profile_image= db.Column(db.String(64),nullable=False,default='default_profile.png')
    name= db.Column(db.String(120),nullable=False)
    email= db.Column(db.String(64),unique=True,index=True)
    username= db.Column(db.String(64),unique=True,index=True)
    password_hash= db.Column(db.String(128))

    posts= db.relationship('Blogpost',backref='author',lazy=True)

    def __init__(self,name,email,user_name,password):
        self.name=name
        self.email=email
        self.username=user_name
        self.password_hash= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"author name : {self.name}"



class Blogpost(db.Model):

    users=db.relationship(User)

    id= db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title= db.Column(db.String(160),nullable=False)
    text= db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title=title
        self.text=text
        self.user_id=user_id

    def __repr__(self):
        return f"Post Id :{self.id} created on ---Date--- : {self.Date}----Title---: {self.title}"
