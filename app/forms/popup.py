from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class PopUpForm(FlaskForm):
    address = StringField("Property Address", [DataRequired()])
    first_name = StringField("First name", [DataRequired()])
    last_name = StringField("Last Name", [DataRequired()])
    email = EmailField("Email", [DataRequired()])

    # TODO Change to message
    message = StringField("Message", [DataRequired()])
    phone = StringField("Phone number", [DataRequired()])
    submit = SubmitField("Submit")
