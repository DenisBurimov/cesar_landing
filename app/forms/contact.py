from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ContactForm(FlaskForm):
    address = StringField("Address")
    phone = StringField("Phone")
    submit = SubmitField("Get my offer")
