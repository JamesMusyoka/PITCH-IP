from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(255))

     email = db.Column(db.String(255), unique=True, index=True)
     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
     pass_secure = db.Column(db.String(255))
     bio = db.Column(db.String(255))
     profile_pic_path = db.Column(db.String())
     password_secure = db.Column(db.String(255))
     pitch = db.relationship('Review', backref='user', lazy="dynamic")
      
     def __repr__(self):
         return f'User {self.username}'

     @login_manager.user_loader
     def load_user(user_id):
        return User.query.get(int(user_id))
     def save_user(self):
        db.session.add(self)
        db.session.commit()
    

     @property
     def password(self):
         raise AttributeError('You cannot read the password attribute')

     @password.setter
     def password(self, password):
         self.password_hash = generate_password_hash(password)

     def check_password(self, password):
             return check_password_hash(self.pass_secure, password)

     def __repr__(self):
         return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    @classmethod
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()

    @classmethod
    def retrieve_posts(cls,id):
        '''
        Function that queries the databse and returns pitches based on the
        category 
        '''

        pitch = Pitch.query.filter_by(id=id).all()
        return pitches

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key= True)
    details = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
