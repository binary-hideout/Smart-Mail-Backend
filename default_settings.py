import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
APP_SECRET_KEY = os.environ["APP_SECRET_KEY"]