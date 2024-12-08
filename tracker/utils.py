import requests
from django.conf import settings

def get_emissions(activity_type, value, unit):
    """
    Interacts with the Climatiq API to calculate emissions.
    """
    api_url = "https://beta3.api.climatiq.io/estimate"
    headers = {
        "Authorization": f"Bearer {settings.CLIMATIQ_API_KEY}",  # Include API key in headers
        "Content-Type": "application/json"
    }
    payload = {
        "activity_type": activity_type,
        "parameters": {
            "value": value,
            "unit": unit
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
