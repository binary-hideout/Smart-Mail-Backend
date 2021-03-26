import os

from flask import Flask
from flask_restful import Api

from resources.contact import Contact, ContactList
from resources.case import Case, CaseList
from resources.tag import Tag, TagList

from apps.db import db
from apps.ma import ma

from dotenv import load_dotenv


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "smartmail.sqlite"),
    )
    load_dotenv(".env", verbose=True)
    if test_config is None:
        app.config.from_pyfile("default_settings.py", silent=True)
        app.config.from_envvar("APPLICATION_SETTINGS")
    else:
        app.config.from_pyfile("testing_settings.py", silent=True)
        app.config.from_envvar("TESTING_SETTINGS")
    api = Api()
    db.init_app(app)
    ma.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.add_resource(Contact, "/contact/<string:email>")
    api.add_resource(ContactList, "/contacts")
    api.add_resource(Case, "/case/<string:title>")
    api.add_resource(CaseList, "/cases")
    api.add_resource(Tag, "/tag/<string:title>")
    api.add_resource(TagList, "/tags")
    api.init_app(app)

    return app


app = create_app()