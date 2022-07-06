import pytest
import requests

def test_base_route_hello_world():
    response = requests.get("http://localhost:3000/")
    assert response.status_code == 200


def test_text():
    response = requests.get("http://localhost:3000/")
    assert response.text == 'Welcome to the Application with updated code!'


def test_base_route():
    response = requests.get("http://localhost:3000/stub")
    assert response.status_code == 200


def test_text_Stub():
    response = requests.get("http://localhost:3000/stub")
    assert response.text == 'Value of Stub: 200'

