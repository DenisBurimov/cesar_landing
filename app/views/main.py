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
        contact_notice = "Contact already exists in your database:"
        if not contact:
            log(log.INFO, "New contact has been saved to the database")
            Contact(
                address=form.address.data,
                phone=form.phone.data
            ).save()
            contact_notice = "New contact has been saved to the database. "
        message = Message(  # noqa F841
            subject="Real Neighbourhood Offer",
            sender=app.config.get("MAIL_DEFAULT_SENDER"),
            recipients=["lopezcesar209@gmail.com"],
            # recipients=["denysburimov@gmail.com"],
        )
        message.html = f"""
            <div><img src="https://realneighborhoodoffer.com/static/img/logo_header.png" alt="logo" class="logo"></div>
            <div>{contact_notice}</div>
            <div><b>Address:</b> {form.address.data}</div>
            <div><b>Phone:</b> {form.phone.data}</div>
            """
        mail.send(message)
        flash("You have successfully sent your contacts to us. We'll call you back!", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        log(log.INFO, "Form submit failed")
        return render_template("index.html", form=form)
    return render_template("index.html", form=form)


@main_blueprint.route("/reviews")
def reviews():
    return redirect(url_for("main.index"))


@main_blueprint.route("/our-company")
def our_company():
    return redirect(url_for("main.index"))
