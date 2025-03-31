# Need to create:
#   [DONE] Recipe model with following:
#          [x] id: primary key
#          [x] title: max length 80 characters
#          [x] description: text
#          [x] ingredients: text
#          [x] instructions: text
#          [x] created: datetime

from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False) #cant be empty
    description = db.Column(db.Text, nullable = False)
    ingredients = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    created = db.Column(db.DateTime, default=datetime.utcnow) # use current time



