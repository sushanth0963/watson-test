import requests

# 🔴 STEP 1: PASTE YOUR API KEY HERE
API_KEY = "pUWpllW55qll5icl0LvUbi5TVX9WV8aIh2kg_sZe1LBn"

# 🔴 STEP 2: PASTE YOUR PUBLIC ENDPOINT (ai_service)
API_URL = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/95abf1d1-be28-46c2-b61b-a53cbf290ff6/ai_service?version=2021-05-01"


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