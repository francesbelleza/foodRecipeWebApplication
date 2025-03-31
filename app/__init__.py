from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

myapp_obj = Flask(__name__)
myapp_obj.config.from_object(Config)
db = SQLAlchemy(myapp_obj)
migrate = Migrate(myapp_obj, db)

from app import routes, models
