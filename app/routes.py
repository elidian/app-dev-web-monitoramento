
from app import app, db
from app.forms import LoginForm, RegistrationForm, RegistrationCamForm
from flask import render_template, flash, redirect, url_for, request, json, session
from flask_login import current_user, login_user, logout_user, login_required, confirm_login
from app.models.user_model import User
from app.models.cam_model import Cam
from app.models.post_cam_model import PostCam
from app.models.post_user_model import PostUser
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    if session['account_type'] == 'session_cam':
        post = PostCam.query.filter(PostCam.cam_name==current_user.name, PostCam.id==current_user.id).all()
    elif session['account_type'] == 'session_user':
        post = PostUser.query.filter(PostUser.user_name==current_user.name, PostUser.id==current_user.id).all()
    else:
        post = None
    return render_template('index.html', title='Home Page', posts=post)

@app.route('/api/v1/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        confirm_login()
        new_user = User.query.filter(User.name==form.name.data).first()
        new_cam = Cam.query.filter(Cam.name==form.name.data).first()
        if User.query.filter(User.name==form.name.data).first() is not None:
            if not new_user.check_password(form.password.data):
                flash('Invalid user name or password')
                return redirect(url_for('login'))
            flash('login user: okay')
            login_user(new_user, remember=form.remember_me.data)
            session['account_type'] = 'session_user'
        elif new_cam is not None:
            if not new_cam.check_password(form.password.data):
                flash('Invalid cam name or password')
                return redirect(url_for('login'))
            flash('login cam: okay')
            login_user(new_cam, remember=form.remember_me.data)
            session['account_type'] = 'session_cam'
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/api/v1/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/api/v1/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, cpf=form.cpf.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/api/v1/registercam', methods=['GET', 'POST'])
def register_cam():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationCamForm()
    if form.validate_on_submit():
        cam = Cam(name=form.name.data, end=form.end.data, password=form.password.data)
        db.session.add(cam)
        db.session.commit()
        flash('Congratulations, you are now a registered cam!')
        return redirect(url_for('login'))
    return render_template('register_cam.html', title='Register Cam', form=form)