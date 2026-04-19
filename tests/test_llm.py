import sys
import os
import json

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from src.main import app

def run_tests():
    print("Initializing TestClient (this will load the dataset)...")
    with TestClient(app) as client:
        print("\n--- Test 1: Basic Location Filter ---")
        payload1 = {"location": "Banashankari", "budget": "medium"}
        print(f"Request: {payload1}")
        response1 = client.post("/api/recommend", json=payload1)
        if response1.status_code == 200:
            print("Response OK. Recommendations count:", len(response1.json().get("recommendations", [])))
            print("Sample Recommendation:", json.dumps(response1.json().get("recommendations", [])[0:1], indent=2))
        else:
            print("Error:", response1.text)

        print("\n--- Test 2: Specific Cuisine and High Budget ---")
        payload2 = {"location": "Bangalore", "cuisine": "Italian", "budget": "high", "min_rating": 4.0}
        print(f"Request: {payload2}")
        response2 = client.post("/api/recommend", json=payload2)
        if response2.status_code == 200:
            print("Response OK. Recommendations count:", len(response2.json().get("recommendations", [])))
            print("Sample Recommendation:", json.dumps(response2.json().get("recommendations", [])[0:1], indent=2))
        else:
            print("Error:", response2.text)

        print("\n--- Test 3: Edge Case (No match) ---")
        payload3 = {"location": "NowhereCity", "cuisine": "Alien"}
        print(f"Request: {payload3}")
        response3 = client.post("/api/recommend", json=payload3)
        if response3.status_code == 200:
            print("Response OK.", response3.json())
        else:
            print("Error:", response3.text)

if __name__ == "__main__":
    run_tests()
