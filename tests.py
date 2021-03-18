from flask import Flask
from flask_restful import Api
from flask_testing import TestCase

from models.contact import ContactModel
from models.tag import TagModel
from models.case import CaseModel

from resources.contact import ContactList, Contact
from resources.tag import TagList, Tag
from resources.case import CaseList, Case

import unittest

from db import db
from ma import ma

from dotenv import load_dotenv


class TestApp(TestCase):
    def create_app(self):
        app = Flask(__name__)
        load_dotenv(".env", verbose=True)
        app.config.from_object("testing_settings")
        app.config.from_envvar("TESTING_SETTINGS")
        app.config["TESTING"] = True
        db.init_app(app)
        ma.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestModels(TestApp):
    def test_contact_model_save(self):
        contact = ContactModel(
            first_name="John",
            last_name="Doe",
            email="john_doe@gmail.com",
            phone="81029851214",
        )
        contact.save_to_db()
        assert ContactModel.find_by_email("john_doe@gmail.com") is not None

    def test_tag_model_save(self):
        tag = TagModel(
            title="To be resolved",
            color="red",
        )
        tag.save_to_db()
        assert TagModel.find_by_title("To be resolved") is not None

    def test_case_model_save(self):
        case = CaseModel(
            title="Service unavailable",
            description="Service connection lost, call sysadmin",
            tag_id=1,
            contact_id=1,
        )
        case.save_to_db()
        assert CaseModel.find_by_title("Service unavailable") is not None

    def test_contact_model_delete(self):
        contact = ContactModel(
            first_name="John",
            last_name="Doe",
            email="john_doe@gmail.com",
            phone="81029851214",
        )
        contact.save_to_db()
        contact = ContactModel.find_by_email("john_doe@gmail.com")
        contact.delete_from_db()
        assert ContactModel.find_by_email("john_doe@gmail.com") is None

    def test_tag_model_delete(self):
        tag = TagModel(
            title="To be resolved",
            color="red",
        )
        tag.save_to_db()
        tag = TagModel.find_by_title("To be resolved")
        tag.delete_from_db()
        assert TagModel.find_by_title("To be resolved") is None

    def test_case_model_delete(self):
        case = CaseModel(
            title="Service unavailable",
            description="Service connection lost, call sysadmin",
            tag_id=1,
            contact_id=1,
        )
        case.save_to_db()
        case = CaseModel.find_by_title("Service unavailable")
        case.delete_from_db()
        assert CaseModel.find_by_title("Service unavailable") is None


if __name__ == "__main__":
    unittest.main()
