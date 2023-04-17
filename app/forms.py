from flask_wtf import FlaskForm
from wtforms import (
    StringField,DateField,TimeField,TextAreaField,BooleanField,SubmitField
)
from wtforms.validators import DataRequired
from datetime import datetime

class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[DataRequired()])
    start_time = TimeField('start_time', validators=[DataRequired()])
    end_date = DateField('end_date', validators=[DataRequired()])
    end_time = TimeField('end_time', validators=[DataRequired()])
    description = TextAreaField('description')
    private = BooleanField('private')
    submit = SubmitField('submit')

# name 	string 	name 	StringField
# start_datetime (date part) 	date 	start_date 	DateField
# start_datetime (time part) 	time 	start_time 	TimeField
# end_datetime (date part) 	date 	end_date 	DateField
# end_datetime (time part) 	time 	end_time 	TimeField
# description 	string 	description 	TextAreaField
# private 	Boolean 	private 	BooleanField
