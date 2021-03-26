import os
import tempfile

import pytest

from smartmail.apps.db import db
from smartmail.apps.ma import ma

from smartmail import create_app


@pytest.fixture
def app():
    app = create_app({"TESTING": True, "DATABASE": "sqlite:///data.db"})
    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        db.create_all()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

