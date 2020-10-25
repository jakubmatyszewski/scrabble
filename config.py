from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    DEBUG = True

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
