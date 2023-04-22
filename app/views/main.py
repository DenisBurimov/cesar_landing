from flask import Blueprint, render_template, flash, redirect, url_for
from flask_mail import Message
from app.forms import ContactForm
from app.logger import log
from app import mail

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        log(log.INFO, "Form submitted")
        message = Message(
            subject="Real Neighbourhood Offer",
            sender="mailtrap@realneighborhoodoffer.com",
            recipients=["denysburimov@gmail.com"],
        )
        # mail.send(message)
        flash("Submitted", "info")
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form)
