# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:03:28 2018

@author: pangi
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from models import Student
import datetime

class AddStudent(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register Student')

class AddAssignment(FlaskForm):
    assignment = StringField('Assignment Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[])
    standard = IntegerField('Standard Number', validators=[DataRequired()])
    max_points = IntegerField('Max Points', validators=[DataRequired()])
    date_assigned = DateField('Date Assigned', default=datetime.datetime.now())