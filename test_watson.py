import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

# =========================
# STEP 1: GET TOKEN
# =========================

token_response = requests.post(
    "https://iam.cloud.ibm.com/identity/token",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data={
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": API_KEY
    }
)

access_token = token_response.json()["access_token"]

print("✅ Token Generated Successfully")


# =========================
# STEP 2: CALL WATSONX AGENT
# =========================

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

payload = {
    "input": "Generate interview questions for Python developer"
}

response = requests.post(API_URL, headers=headers, json=payload)

print("\n🎯 FINAL RESPONSE:\n")
print(response.text)
