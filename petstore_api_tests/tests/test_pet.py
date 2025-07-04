import pytest
import requests
from utils.config import BASE_URL
import random
import time

@pytest.fixture
def pet_data():
    pet_id = random.randint(100000, 999999)
    pet = {
        "id": pet_id,
        "name": f"Pet{pet_id}",
        "photoUrls": [],
        "status": "available"
    }
    return pet

@pytest.fixture
def created_pet(pet_data):
    url = f"{BASE_URL}/pet"
    response = requests.post(url, json=pet_data)
    assert response.status_code == 200
    yield pet_data
    requests.delete(f"{BASE_URL}/pet/{pet_data['id']}")

class TestPetAPI:

    def test_add_pet(self, created_pet):
        url = f"{BASE_URL}/pet/{created_pet['id']}"
        resp = requests.get(url)
        assert resp.status_code == 200
        assert resp.json()["name"] == created_pet["name"]

    def test_update_pet(self, created_pet):
        url = f"{BASE_URL}/pet"
        updated_pet = created_pet.copy()
        updated_pet["name"] = "UpdatedName"
        updated_pet["status"] = "sold"
        resp = requests.put(url, json=updated_pet)
        assert resp.status_code == 200

        get_url = f"{BASE_URL}/pet/{created_pet['id']}"
        resp2 = requests.get(get_url)
        assert resp2.status_code == 200
        assert resp2.json()["name"] == "UpdatedName"
        assert resp2.json()["status"] == "sold"

    # Тест только для статуса "available" — для портфолио этого достаточно
    def test_find_pet_by_status(self, created_pet):
        time.sleep(2)  # Иногда нужно подождать
        url = f"{BASE_URL}/pet/findByStatus"
        resp = requests.get(url, params={"status": "available"})
        assert resp.status_code == 200
        assert any(pet["id"] == created_pet["id"] for pet in resp.json())

    def test_delete_pet(self, pet_data):
        url = f"{BASE_URL}/pet"
        resp = requests.post(url, json=pet_data)
        assert resp.status_code == 200

        del_url = f"{BASE_URL}/pet/{pet_data['id']}"
        del_resp = requests.delete(del_url)
        assert del_resp.status_code == 200

        get_resp = requests.get(del_url)
        assert get_resp.status_code == 404
