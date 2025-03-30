from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_apply_discounts():
    payload = {
        "campaign_ids": ["fixed50", "points68", "seasonal_300_40"]
    }

    response = client.post("/apply-discounts", json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert "final_price" in response.json()

def test_invalid_campaign():
    payload = {
        "campaign_ids": ["not_exist"]
    }

    response = client.post("/apply-discounts", json=payload)
    print("Invalid campaign response:", response.json())

    assert response.status_code == 404

if __name__ == "__main__":
    print("Running tests manually...")
    test_apply_discounts()
    test_invalid_campaign()
    print("All tests passed!")
