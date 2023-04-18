from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    TextAreaField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired
from datetime import datetime


class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("start_date", validators=[DataRequired()])
    start_time = TimeField("start_time", validators=[DataRequired()])
    end_date = DateField("end_date", validators=[DataRequired()])
    end_time = TimeField("end_time", validators=[DataRequired()])
    description = TextAreaField("description")
    private = BooleanField("private")
    submit = SubmitField("submit")

    def validate_end_date(form, field):
        return False
