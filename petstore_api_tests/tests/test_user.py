import pytest
import requests
import random
import string
from utils.config import BASE_URL

@pytest.fixture
def user_data():
    username = ''.join(random.choices(string.ascii_lowercase, k=6)) + ''.join(random.choices(string.digits, k=2))
    user = {
        "id": random.randint(10000, 99999),
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": f"{username}@example.com",
        "password": "pass1234",
        "phone": "1234567890",
        "userStatus": 1
    }
    return user

@pytest.fixture
def created_user(user_data):
    url = f"{BASE_URL}/user"
    response = requests.post(url, json=user_data)
    assert response.status_code == 200
    yield user_data
    del_url = f"{BASE_URL}/user/{user_data['username']}"
    requests.delete(del_url)

class TestUserAPI:

    def test_create_user(self, created_user):
        url = f"{BASE_URL}/user/{created_user['username']}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["username"] == created_user["username"]

    def test_update_user(self, created_user):
        url = f"{BASE_URL}/user/{created_user['username']}"
        updated_payload = created_user.copy()
        updated_payload["firstName"] = "Updated"
        updated_payload["userStatus"] = 2

        response = requests.put(url, json=updated_payload)
        assert response.status_code == 200

        get_url = f"{BASE_URL}/user/{created_user['username']}"
        resp = requests.get(get_url)
        assert resp.status_code == 200
        assert resp.json()["firstName"] == "Updated"
        assert resp.json()["userStatus"] == 2

    def test_user_login(self, created_user):
        url = f"{BASE_URL}/user/login"
        params = {
            "username": created_user["username"],
            "password": created_user["password"]
        }
        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert "logged in user session" in response.text

    def test_user_logout(self):
        url = f"{BASE_URL}/user/logout"
        response = requests.get(url)
        assert response.status_code == 200

    def test_delete_user(self, user_data):
        url = f"{BASE_URL}/user"
        resp = requests.post(url, json=user_data)
        assert resp.status_code == 200

        del_url = f"{BASE_URL}/user/{user_data['username']}"
        del_resp = requests.delete(del_url)
        assert del_resp.status_code == 200

        get_resp = requests.get(del_url)
        assert get_resp.status_code == 404
