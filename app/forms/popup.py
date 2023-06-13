from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class PopUpForm(FlaskForm):
    address = StringField("Property Address", [DataRequired()])
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    email = EmailField("Email")
    message = StringField("Message")
    phone = StringField("Phone number", [DataRequired()])
    submit = SubmitField("Submit")
