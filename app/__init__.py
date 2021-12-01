from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"



app = Flask(__name__)
#app.config['SECRET_KEY'] = 'mofo'
#app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config.from_object("config")
db.init_app(app)

uploads = app.config["UPLOAD_FOLDER"]

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

from .models import User, Note

#: create_database(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .app_old import app_old_bp
app.register_blueprint(app_old_bp)
from . pics import pics_bp
app.register_blueprint(pics_bp)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
db.create_all(app=app)

"""
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
"""
