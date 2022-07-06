import pytest
import requests

def test_base_route_hello_world():
    response = requests.get("http://localhost:3000/")
    assert response.status_code == 200

