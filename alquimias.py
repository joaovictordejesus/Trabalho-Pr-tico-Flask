#João Vicotr de Jesus
from app.models.models import User, Post
from app import db

def validate_user_password(username, password):
    user = User.query.filter_by(username=username).first()
    return user if user and user.password == password else None

def user_exists(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password, bio=None, profile_pic=None, remember=False):
    new_user = User(username=username, password=password, bio=bio, profile_pic=profile_pic)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body, user):
    new_post = Post(body=body, author=user)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_timeline():
    return Post.query.order_by(Post.timestamp.desc()).limit(5).all()
