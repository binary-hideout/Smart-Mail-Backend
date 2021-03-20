import os
import tempfile

import pytest

from models.contact import ContactModel
from models.tag import TagModel
from models.case import CaseModel

def test_contactlist_get_endpoint(client):
    response = client.get("/contacts")
    assert response.status_code == 200

def test_caselist_get_endpoint(client):
    response = client.get("/cases")
    assert response.status_code == 200


def test_taglist_get_endpoint(client):
    response = client.get("/tags")
    assert response.status_code == 200


def test_contact_post_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"first_name": "John", "last_name": "Doe", "phone": "131859131"}
    url = '/contact/john_doe@gmail.com'
    response = client.post(url, json=data, headers=headers)
    assert response.status_code == 201
    assert response.json["first_name"] == "John"
    assert response.json["last_name"] == "Doe"
    with app.app_context():
        assert ContactModel.find_by_email("john_doe@gmail.com")

    
def test_tag_post_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"color": "red"}
    url = '/tag/To be resolved'
    response = client.post(url, json=data, headers=headers)
    assert response.status_code == 201
    assert response.json["title"] == "To be resolved"
    assert response.json["color"] == "red"
    with app.app_context():
        assert TagModel.find_by_title("To be resolved")


def test_case_post_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"description": "Security flaw detected on frontend", "contact_id": 1, "tag_id": 1}
    url = '/case/Security breach'
    response = client.post(url, json=data, headers=headers)
    assert response.status_code == 201
    assert response.json["title"] == "Security breach"
    assert response.json["contact_id"] == 1
    assert response.json["tag_id"] == 1
    with app.app_context():
        assert CaseModel.find_by_title("Security breach")


def test_contact_get_endpoint(app, client):
    response = client.get('/contact/john_doe@gmail.com')
    assert response.status_code == 200
    assert response.json["first_name"] == "John"
    assert response.json["last_name"] == "Doe"
    with app.app_context():
        assert ContactModel.find_by_email("john_doe@gmail.com")


def test_tag_get_endpoint(app, client):
    response = client.get('/tag/To be resolved')
    assert response.status_code == 200
    assert response.json["title"] == "To be resolved"
    assert response.json["color"] == "red"
    with app.app_context():
        assert TagModel.find_by_title("To be resolved")


def test_case_get_endpoint(app, client):
    response = client.get('/case/Security breach')
    assert response.status_code == 200
    assert response.json["title"] == "Security breach"
    assert response.json["tag_id"] == 1
    assert response.json["contact_id"] == 1
    with app.app_context():
        assert CaseModel.find_by_title("Security breach")


def test_contact_put_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"first_name": "Lisa", "last_name": "Doe", "phone": "134214321"}
    url = '/contact/john_doe@gmail.com'
    response = client.put(url, json=data, headers=headers)
    assert response.status_code == 200
    assert response.json["first_name"] == "Lisa"
    assert response.json["phone"] == "+52134214321"
    with app.app_context():
        assert ContactModel.find_by_email("john_doe@gmail.com")


def test_tag_put_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"color": "yellow"}
    url = '/tag/To be resolved'
    response = client.put(url, json=data, headers=headers)
    assert response.status_code == 200
    assert response.json["title"] == "To be resolved"
    assert response.json["color"] == "yellow"
    with app.app_context():
        assert TagModel.find_by_title("To be resolved")


def test_case_put_endpoint(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"description": "Security flaw detected on backend", "contact_id": 1, "tag_id": 1}
    url = '/case/Security breach'
    response = client.put(url, json=data, headers=headers)
    assert response.status_code == 200
    assert response.json["description"] == "Security flaw detected on backend"
    assert response.json["contact_id"] == 1
    assert response.json["tag_id"] == 1
    with app.app_context():
        assert CaseModel.find_by_title("Security breach")


def test_case_delete_endpoint(app, client):
    response = client.delete('/case/Security breach')
    assert response.status_code == 200
    with app.app_context():
        assert CaseModel.find_by_title("Security breach") == None


def test_tag_delete_endpoint(app, client):
    response = client.delete('/tag/To be resolved')
    assert response.status_code == 200
    with app.app_context():
        assert TagModel.find_by_title("To be resolved") == None


def test_contact_delete_endpoint(app, client):
    response = client.delete('/contact/john_doe@gmail.com')
    assert response.status_code == 200
    with app.app_context():
        assert ContactModel.find_by_email("john_doe@gmail.com") == None