#!/user/bin/env python
# flake8: noqa F401
import click
from app import create_app, db, models

app = create_app()
