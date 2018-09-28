# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:51:02 2018

@author: pangi
"""

#from app import app
from flask import Flask, render_template, flash, url_for, Blueprint, redirect
from forms import *
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from models import User
from app import db

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/')
def home():
    return render_template('home.html')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('login.home'))
    return render_template('login.html', title='Sign In', form=form)

@login_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.home'))

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login.login'))
    return render_template('registration.html', title='Register', form=form)

@login_bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)