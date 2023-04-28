# flake8: noqa F401
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_mail import Message
from flask import current_app as app
from app.forms import ContactForm
from app.logger import log
from app import mail
from app.models import Contact

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        log(log.INFO, "Form submitted: [%s, %s]", form.address.data, form.phone.data)
        contact: Contact = Contact.query.filter_by(address=form.address.data).first()
        new_contact_notice = ""
        if not contact:
            log(log.INFO, "New contact has been saved to the database")
            Contact(
                address=form.address.data,
                phone=form.phone.data
            ).save()
            new_contact_notice = "New contact has been saved to the database. "
        message = Message(  # noqa F841
            subject="Real Neighbourhood Offer",
            # sender="mailtrap@realneighborhoodoffer.com",
            sender=app.config.get("MAIL_DEFAULT_SENDER"),
            recipients=["lopezcesar209@gmail.com"],
        )
        message.html = f"{new_contact_notice}<b>Address:</b> {form.address.data} \n <b>Phone:</b> {form.phone.data}"
        mail.send(message)
        flash("You have successfully sent your contacts to us. We'll call you back!", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        log(log.INFO, "Form submit failed")
        return render_template("index.html", form=form)
    return render_template("index.html", form=form)
