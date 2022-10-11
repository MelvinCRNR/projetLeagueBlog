from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import subprocess

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Veuillez vous connecter pour accéder à cette page."

from app import routes, models

if __name__ == "__main__":
    print("test")
    app.run("0.0.0.0", port=5000, debug=False)

