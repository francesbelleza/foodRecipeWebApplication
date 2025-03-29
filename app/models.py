# Need to create:
#   Recipe model with following:
#          [] id: primary key
#          [] title: max length 80 characters
#          [] description: text
#          [] ingredients: text
#          [] instructions: text
#          [] created: datetime






from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
