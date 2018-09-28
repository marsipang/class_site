# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:51:02 2018

@author: pangi
"""

#from app import app
from flask import Flask, render_template, flash, url_for, Blueprint, redirect
from students.forms import *
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from models import User
from app import db
import datetime

student_bp = Blueprint('students', __name__, template_folder='templates')

@student_bp.route('/addstudent', methods=['GET', 'POST'])
def add_student():
    form = AddStudent()
    if form.validate_on_submit():
        begin = 2018
        end = 2019
        class_size = len(Student.query.filter_by(school_year_end=end).all())
        sid = str(end) + '_' + str(class_size + 1)
        student = Student(student_id=sid, first_name=form.first_name.data, last_name=form.last_name.data,
                          school_year_begin=begin, school_year_end=end)
        db.session.add(student)
        db.session.commit()
        flash('New student to the roster!')
        return redirect(url_for('login.home'))
    return render_template('add_student.html', title='Add Student', form=form)

@student_bp.route('/addassignment', methods=['GET', 'POST'])
def add_student():
    form = AddAssignment()
    if form.validate_on_submit():
        students = len(Student.query.filter_by(school_year_end=end).all())
        assignment = Assignment(student_id=, first_name=form.first_name.data, last_name=form.last_name.data,
                          school_year_begin=begin, school_year_end=end)
        db.session.add(student)
        db.session.commit()
        flash('New student to the roster!')
        return redirect(url_for('login.home'))
    return render_template('add_student.html', title='Add Student', form=form)
