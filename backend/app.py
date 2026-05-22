from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variables
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
PROJECT_ID = os.getenv("PROJECT_ID")


# Input model
class UserInput(BaseModel):
    message: str


# Generate IBM token
def get_token():
    try:
        response = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": API_KEY
            }
        )

        token_data = response.json()

        print("TOKEN RESPONSE:", token_data)

        return token_data.get("access_token")

    except Exception as e:
        print("TOKEN ERROR:", str(e))
        return None


# Home route
@app.get("/")
def home():
    return {"message": "Backend is running"}


# Chat route
@app.post("/chat")
def chat(user: UserInput):

    # Generate token
    token = get_token()

    if not token:
        return {
            "output": "❌ Token generation failed"
        }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Watsonx request body
    payload = {
        "input": user.message,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200,
            "min_new_tokens": 1
        },
        "model_id": "ibm/granite-3-8b-instruct",
        "project_id": PROJECT_ID
    }

    try:
        response = requests.post(
            f"{API_URL}/ml/v1/text/generation?version=2023-05-29",
            headers=headers,
            json=payload
        )

        print("STATUS CODE:", response.status_code)
        print("RAW RESPONSE:", response.text[:1000])

        # Convert response to JSON
        result = response.json()

        # Handle IBM errors
        if "errors" in result:
            return {
                "output": f"❌ Watsonx Error: {result['errors']}"
            }

        # Extract generated text
        if "results" in result:
            try:
                generated_text = result["results"][0]["generated_text"]

                return {
                    "output": generated_text
                }

            except Exception as e:
                return {
                    "output": f"⚠️ Failed to extract generated text: {str(e)}"
                }

        # Unexpected response format
        return {
            "output": json.dumps(result, indent=2)
        }

    except Exception as e:
        print("CHAT ERROR:", str(e))

        return {
            "output": f"❌ Backend Error: {str(e)}"
        }