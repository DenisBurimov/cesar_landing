import os
import base64
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models.utils import ModelMixin


def gen_secret_key():
    return base64.b32encode(os.urandom(20)).decode("utf-8")


class User(db.Model, UserMixin, ModelMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    deleted = db.Column(db.Boolean, default=False)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter(
            func.lower(cls.username) == func.lower(username)
        ).first()
        if user and check_password_hash(user.password, password):
            return user

    def __repr__(self):
        return f"<{self.id}: {self.username} ({self.role})>"


class AnonymousUser(AnonymousUserMixin):
    pass
