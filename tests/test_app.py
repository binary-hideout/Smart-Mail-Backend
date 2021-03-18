from flask import Flask
from flask_restful import Api
from flask_testing import TestCase

from dotenv import load_dotenv

class AppTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        load_dotenv(".env", verbose=True)
        app.config.from_object("testing_settings")
        app.config.from_envvar("TESTING_SETTINGS")
        app.config['TESTING'] = True
        api = Api(app)
        return api