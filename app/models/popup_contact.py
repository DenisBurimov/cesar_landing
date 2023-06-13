from datetime import datetime
from flask_login import UserMixin
from app.models.utils import ModelMixin
from app import db


class Contact(db.Model, UserMixin, ModelMixin):

    # __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    message = db.Column(db.Text)
    phone = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<{self.id}: {self.address} ({self.phone}) ({self.email})>"
