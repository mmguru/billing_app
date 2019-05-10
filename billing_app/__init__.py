from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt = Bcrypt
from flask_login import LoginManager
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
