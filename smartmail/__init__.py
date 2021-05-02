import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect

from smartmail.resources.contact import Contact, ContactDelete, ContactList
from smartmail.resources.case import Case, CaseDelete, CaseList
from smartmail.resources.tag import Tag, TagDelete, TagList
from smartmail.resources.user import User, UserLogin, UserRegister, UserLogout, TokenRefresh
from smartmail.resources.call import Call
from smartmail.resources.myform import Test

from smartmail.apps.db import db
from smartmail.apps.ma import ma
from smartmail.blacklist import BLACKLIST

from dotenv import load_dotenv


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "smartmail.sqlite"),
    )
    load_dotenv(".env", verbose=True)
    if test_config is None:
        app.config.from_object("smartmail.default_settings")
    else:
        app.config.from_object("smartmail.testing_settings")
    api = Api(app)
    jwt = JWTManager(app)
    csrf = CSRFProtect()

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLACKLIST

    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogout, "/logout")
    api.add_resource(TokenRefresh, "/refresh")
    api.add_resource(Contact, "/contact/<string:email>")
    api.add_resource(ContactDelete, "/contact/delete/<string:email>")
    api.add_resource(ContactList, "/contacts")
    api.add_resource(Case, "/case/<string:title>")
    api.add_resource(CaseDelete, "/case/delete/<string:title>")
    api.add_resource(CaseList, "/cases")
    api.add_resource(Tag, "/tag/<string:title>")
    api.add_resource(TagDelete, "/tag/delete/<string:title>")
    api.add_resource(TagList, "/tags")
    api.add_resource(Call, "/call/<string:email>")
    api.add_resource(Test, "/test")

    return app
