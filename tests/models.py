from flask_testing import TestCase
from tests.test_app import AppTest
from db import db

class ModelTest(TestCase):

    def create_app(self):
        return AppTest.create_app(self)

    def set_up(self):
        db.create_all()

    def tear_down(self):
        pass