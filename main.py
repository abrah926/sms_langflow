import os
import requests


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "bcc46440-0965-4238-837e-04af612bf803"
FLOW_ID = "6350faf1-81ef-4327-b5a2-db05a7125b6f"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "Bernardo" # The endpoint name of the flow


def run_flow(message: str,) -> dict:

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": 'chat',
        "input_type": 'chat',
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

