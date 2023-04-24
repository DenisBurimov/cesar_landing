# flake8: noqa F401
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_mail import Message
from flask import current_app as app
from app.forms import ContactForm
from app.logger import log
from app import mail

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        log(log.INFO, "Form submitted")
        message = Message(  # noqa F841
            subject="Real Neighbourhood Offer",
            # sender="mailtrap@realneighborhoodoffer.com",
            sender=app.config.get("MAIL_DEFAULT_SENDER"),
            recipients=["denysburimov@gmail.com"],
        )
        message.html = f"<b>Address:</b> {form.address.data} \n <b>Phone:</b> {form.phone.data}"
        mail.send(message)
        flash("Submitted", "info")
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form)
