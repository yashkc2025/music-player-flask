import os

current_dir = os.path.abspath(os.path.dirname(__file__))

class appConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(current_dir, "database.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    UPLOAD_FOLDER = "music_files"
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = "secret"
