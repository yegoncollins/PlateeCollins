import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = "static"
SQLALCHEMY_DATABASE_URI="sqlite:////"+os.path.join(basedir, "database.db")
SECRET_KEY="dnjinjiewnewnbibirwbibiefbiqbe"