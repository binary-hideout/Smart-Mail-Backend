import os
import tempfile

from smartmail import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/contacts')
    assert response.data == b'{"content": []}'