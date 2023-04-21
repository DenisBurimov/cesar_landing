from flask import Blueprint, render_template, flash
from app.forms import ContactForm

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Submitted", "info")
    return render_template("index.html", form=form)
