from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager

myapp_obj = Flask(__name__)
myapp_obj.config.from_object(Config)

db = SQLAlchemy(myapp_obj)
migrate = Migrate(myapp_obj, db)

login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = Config.LOGIN_VIEW

from app import routes, models
