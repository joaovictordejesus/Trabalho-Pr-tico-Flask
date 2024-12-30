#João Victor de Jesus Augusto
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import Mapped
from app import db, login

class User(UserMixin, db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.String(256))
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")

    def _repr_(self):
        return f"<User {self.username}>"

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    _tablename_ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author: Mapped[User] = relationship("User", back_populates="posts")

    def _repr_(self):
        return f"<Post {self.id} by User {self.user_id}>"
