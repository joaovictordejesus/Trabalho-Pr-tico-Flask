#João Victor de Jesus
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.alquimias import validate_user_password, create_user, user_exists, create_post, get_timeline

@app.route('/')
@login_required
def index():
    user = current_user if current_user.is_authenticated else None
    posts = get_timeline() if user else []
    return render_template('index.html', user=user, posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        user = validate_user_password(username, password)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        bio = request.form.get('bio', None)
        profile_pic = request.form.get('profile_pic', None)
        if user_exists(username):
            return redirect(url_for('login'))
        user = create_user(username, password, bio=bio, profile_pic=profile_pic)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
