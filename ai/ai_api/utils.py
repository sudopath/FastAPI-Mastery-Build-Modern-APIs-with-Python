import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/37958744e617b9ac2cd937905dc369a2/ai/run/"
headers = {"Authorization":f"Bearer {os.getenv("CLOUDFLARE_KEY")}"}


def generate_text(prompt: str):
    inputs = [
        {
            "role":"user", "content": prompt
        }
        ]
    input = {"messages": inputs}

    model = "@cf/meta/llama-3-8b-instruct"

    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    response_json = response.json()
    print(response)
    content = response_json['result']['response']
    return content